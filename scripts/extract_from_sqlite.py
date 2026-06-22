import sqlite3, json, os, sys
from decimal import Decimal
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data" / "sql"
OUT = BASE / "data" / "partidas_extraidas.json"

CAPECO = DATA / "Capeco.sqlite"
VIVIENDA = DATA / "vivienda_proyecto_final.sqlite"

if not CAPECO.exists() or not VIVIENDA.exists():
    print("ERROR: Bases SQLite no encontradas en data/sql/")
    sys.exit(1)

items = []

# â”€â”€ 1. Extraer unidades â”€â”€
db1 = sqlite3.connect(str(CAPECO))
unidades = {}
for r in db1.execute("SELECT id_unidad, descripcion_unidad FROM unidad"):
    unidades[r[0]] = r[1] or r[0]

# â”€â”€ 2. Extraer productos (insumos) de Capeco â”€â”€
print("Extrayendo insumos de Capeco...")
rows = db1.execute("""
    SELECT p.descripcion_producto, p.id_unidad, p.costo_unitariolista, 
           p.id_monedacosto, c.descripcion_categoria, p.especificaciones
    FROM producto p
    LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
    ORDER BY c.descripcion_categoria, p.descripcion_producto
""").fetchall()

for r in rows:
    name = (r[0] or "").strip()
    unit_id = r[1] or ""
    price = r[2] or 1
    currency = r[3] or "Nuevo Sol"
    cat = r[4] or "MATERIALES"
    spec = r[5] or ""

    if not name:
        continue

    # Mapear moneda
    curr = "PEN" if "Sol" in str(currency) else "USD"
    # Mapear tipo
    if "MANO" in cat.upper():
        res_type = "labor"
    elif "EQUIPO" in cat.upper():
        res_type = "equipment"
    else:
        res_type = "material"

    # Unidad canonica
    unit_map = {"m3": "m3", "m2": "m2", "kg": "kg", "und": "und",
                "hh": "hh", "hm": "hm", "bol": "bls", "pza": "pza",
                "gal": "gal", "gln": "gal", "m": "m", "t": "t",
                "bls": "bls", "rll": "rll", "cja": "cja", "cnt": "cnt",
                "par": "par", "jgo": "jgo", "pln": "pln"}
    unit_name = unidades.get(unit_id, unit_id)
    unit = unit_map.get(unit_id, "und")

    items.append({
        "code": f"INS-{name[:30].replace(' ','_').upper()}",
        "description": name,
        "descriptions": {"es": name},
        "unit": unit,
        "rate": str(Decimal(str(price))),
        "currency": curr,
        "source": "capeco",
        "region": "PE_LIMA",
        "classification": {},
        "components": [],
        "tags": [cat.lower(), res_type, unit],
        "is_active": True,
        "metadata": {
            "type": res_type,
            "category": cat,
            "spec": spec,
            "origin": "capeco_producto",
            "original_unit": unit_name,
        }
    })

print(f"  {len(items)} insumos extraidos")

# â”€â”€ 3. Extraer partidas (costo_unitario) del proyecto vivienda â”€â”€
print("Extrayendo partidas del proyecto vivienda...")
db2 = sqlite3.connect(str(VIVIENDA))

# costo_unitarioplantilla con precios reales
plantilla = db2.execute("""
    SELECT descripcion_costo, id_unidad, costo_unitario, numeracion_costo
    FROM costo_unitarioplantilla
    WHERE costo_unitario > 0
    ORDER BY numeracion_costo
""").fetchall()

partidas_count = 0
for r in plantilla:
    name = (r[0] or "").strip()
    unit_id = r[1] or ""
    price = Decimal(str(r[2]))
    num = (r[3] or "").strip()

    if not name or price <= 0:
        continue

    unit_map = {"m3": "m3", "m2": "m2", "kg": "kg", "und": "und",
                "hh": "hh", "hm": "hm", "bol": "bls", "pza": "pza",
                "gal": "gal", "mes": "mes", "hom": "mes",
                "UN0000000001": "m3", "UN0000000002": "hh",
                "UN0000000003": "m2", "UN0000000006": "und",
                "UN0000000008": "mes", "UN0000000010": "kg",
                "UN0000000020": "m", "UN0000000028": "hm",
                "UN0000000034": "mes"}
    unit = unit_map.get(unit_id, "und")

    items.append({
        "code": num if num else f"PART-{name[:20].replace(' ','_').upper()}",
        "description": name,
        "descriptions": {"es": name},
        "unit": unit,
        "rate": str(price),
        "currency": "PEN",
        "source": "sencico",
        "region": "PE_LIMA",
        "classification": {"rne": ""},
        "components": [],
        "tags": ["plantilla", "personal", "costo indirecto"],
        "is_active": True,
        "metadata": {
            "type": "labor",
            "category": "Personal",
            "origin": "vivienda_proyecto",
            "date": "2008-11-22",
        }
    })
    partidas_count += 1

print(f"  {partidas_count} partidas de personal extraidas")

# â”€â”€ 4. Extraer indices de precios â”€â”€
print("Extrayendo indices de precios...")
indices = db2.execute("""
    SELECT numero_anio, numero_mes, codigo_clase, numero_region, valor_indice
    FROM indice_precio
    ORDER BY numero_anio, numero_mes, codigo_clase
""").fetchall()

# Agrupar por region
regiones_map = {1: "PE_NORTE", 2: "PE_LIMA", 3: "PE_CENTRO",
                4: "PE_SUR", 5: "PE_SELVA", 6: "PE_SUR_ALTIPLANO"}

indices_data = {}
for r in indices:
    anio, mes, clase, region, valor = r
    reg_code = regiones_map.get(region, f"REGION_{region}")
    key = f"{anio}-{mes:02d}"
    if key not in indices_data:
        indices_data[key] = {}
    indices_data[key][f"{reg_code}_{clase}"] = valor

print(f"  {len(indices)} indices extraidos ({len(indices_data)} meses)")

# â”€â”€ 5. Extraer regiones â”€â”€
regiones_rows = db2.execute("SELECT numero_region, descripcion_region FROM region_precio").fetchall()
regiones_info = {r[0]: (r[1] or "").strip() for r in regiones_rows}

# â”€â”€ 6. Guardar todo â”€â”€
output = {
    "meta": {
        "source": "CAPECO + Proyecto Vivienda Delphin",
        "date_extracted": "2025",
        "currency": "PEN",
        "region": "PE_LIMA",
        "total_items": len(items),
    },
    "regiones": [{"code": regiones_map.get(i, f"R{i}"), "name": regiones_info.get(i, "")} for i in range(1,7)],
    "indices_precio": indices_data,
    "items": items,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

db1.close()
db2.close()

print(f"\nTODO LISTO: {OUT}")
print(f"  {len(items)} items extraidos")
print(f"  {len(indices_data)} meses de indices")
print(f"  {len(regiones_info)} regiones")

