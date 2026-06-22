"""
Datos semilla: 35 partidas de construcción peruanas con precios SENCICO 2025.

Este módulo registra las partidas en ``oe_costs_item`` al instalar el pack.
Los precios están en PEN (sol peruano) para Lima Metropolitana.

Fuente: SENCICO — Tablas de Costos Unitarios y Rendimientos.
"""

from __future__ import annotations

import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

# ── 35 partidas peruanas ─────────────────────────────────────────────────

PARTIDAS: list[dict] = [
    # ═══ 01 — OBRAS PROVISIONALES ═══
    {
        "code": "01.01.01",
        "description": "Cartel de identificación de obra 3.60×2.40m (gigantografía)",
        "unit": "und",
        "rate": "850.00",
        "category": "Obras provisionales",
        "classification": {"rne": "GE.010"},
        "tags": ["cartel", "obra", "provisional"],
    },
    {
        "code": "01.01.02",
        "description": "Almacén de obra provisional (madera + calamina)",
        "unit": "m2",
        "rate": "180.00",
        "category": "Obras provisionales",
        "classification": {"rne": "GE.010"},
        "tags": ["almacen", "provisional"],
    },
    {
        "code": "01.01.03",
        "description": "Cerco perimetral con malla arpillera y parantes de madera h=2.40m",
        "unit": "m",
        "rate": "65.00",
        "category": "Obras provisionales",
        "classification": {"rne": "GE.010"},
        "tags": ["cerco", "perimetral", "arpillera"],
    },

    # ═══ 02 — ESTRUCTURAS ═══
    # 02.01 Concreto simple
    {
        "code": "02.01.01",
        "description": "Concreto f'c=100 kg/cm2 para falsos pisos y solados",
        "unit": "m3",
        "rate": "280.00",
        "category": "Concreto simple",
        "classification": {"rne": "E.060"},
        "tags": ["concreto", "falso piso", "solado", "fc=100"],
    },
    {
        "code": "02.01.02",
        "description": "Concreto f'c=140 kg/cm2 para sobrecimientos",
        "unit": "m3",
        "rate": "320.00",
        "category": "Concreto simple",
        "classification": {"rne": "E.060"},
        "tags": ["concreto", "sobrecimiento", "fc=140"],
    },
    {
        "code": "02.01.03",
        "description": "Concreto f'c=175 kg/cm2 para cimientos corridos",
        "unit": "m3",
        "rate": "350.00",
        "category": "Concreto simple",
        "classification": {"rne": "E.060"},
        "tags": ["concreto", "cimiento", "corrido", "fc=175"],
    },
    # 02.02 Concreto armado
    {
        "code": "02.02.01",
        "description": "Concreto premezclado f'c=210 kg/cm2 para elementos estructurales (columnas, vigas, losas)",
        "unit": "m3",
        "rate": "380.00",
        "category": "Concreto armado",
        "classification": {"rne": "E.060", "masterformat": "03 30 00"},
        "tags": ["concreto", "armado", "fc=210", "columna", "viga", "losa"],
        "components": [
            {"type": "material", "desc": "Cemento Portland I (42.5 kg)", "qty": "8.5", "unit": "bls", "rate": "28.00"},
            {"type": "material", "desc": "Piedra chancada 1/2\"", "qty": "0.85", "unit": "m3", "rate": "45.00"},
            {"type": "material", "desc": "Arena gruesa", "qty": "0.52", "unit": "m3", "rate": "35.00"},
            {"type": "material", "desc": "Agua potable", "qty": "0.18", "unit": "m3", "rate": "5.00"},
            {"type": "labor", "desc": "Operario", "qty": "1.5", "unit": "hh", "rate": "28.00"},
            {"type": "labor", "desc": "Oficial", "qty": "1.5", "unit": "hh", "rate": "22.00"},
            {"type": "labor", "desc": "Peón", "qty": "3.0", "unit": "hh", "rate": "15.00"},
            {"type": "equipment", "desc": "Mezcladora 11p3", "qty": "1.0", "unit": "hm", "rate": "30.00"},
            {"type": "equipment", "desc": "Vibradora", "qty": "1.0", "unit": "hm", "rate": "10.00"},
        ],
    },
    {
        "code": "02.02.02",
        "description": "Acero corrugado ASTM A615 grado 60 fy=4200 kg/cm2 (corte + habilitación + colocación)",
        "unit": "kg",
        "rate": "4.20",
        "category": "Concreto armado",
        "classification": {"rne": "E.060", "masterformat": "03 20 00"},
        "tags": ["acero", "corrugado", "fy=4200", "grado 60"],
    },
    {
        "code": "02.02.03",
        "description": "Encofrado y desencofrado de madera para elementos estructurales (uso 3 veces)",
        "unit": "m2",
        "rate": "55.00",
        "category": "Concreto armado",
        "classification": {"rne": "E.060"},
        "tags": ["encofrado", "desencofrado", "madera"],
    },
    # 02.03 Estructuras metálicas
    {
        "code": "02.03.01",
        "description": "Estructura metálica ASTM A36 — perfiles laminados (suministro + montaje + pintura anticorrosiva)",
        "unit": "kg",
        "rate": "12.50",
        "category": "Estructuras metálicas",
        "classification": {"rne": "E.090", "masterformat": "05 12 00"},
        "tags": ["acero", "estructural", "a36", "perfiles"],
    },

    # ═══ 03 — ARQUITECTURA ═══
    # 03.01 Albañilería
    {
        "code": "03.01.01",
        "description": "Muro de ladrillo King Kong de arcilla (18 huecos) con mortero 1:4, junta 1.5cm, aparejo de soga",
        "unit": "m2",
        "rate": "85.00",
        "category": "Albañilería",
        "classification": {"rne": "E.070", "masterformat": "04 20 00"},
        "tags": ["muro", "ladrillo", "king kong", "soga"],
    },
    {
        "code": "03.01.02",
        "description": "Muro de ladrillo King Kong de arcilla (18 huecos) con mortero 1:4, aparejo de cabeza",
        "unit": "m2",
        "rate": "125.00",
        "category": "Albañilería",
        "classification": {"rne": "E.070"},
        "tags": ["muro", "ladrillo", "king kong", "cabeza"],
    },
    {
        "code": "03.01.03",
        "description": "Tabique de ladrillo pandereta (15×10×25cm) con mortero 1:4",
        "unit": "m2",
        "rate": "48.00",
        "category": "Albañilería",
        "classification": {"rne": "E.070"},
        "tags": ["tabique", "ladrillo", "pandereta"],
    },
    # 03.02 Tarrajeo
    {
        "code": "03.02.01",
        "description": "Tarrajeo interior de muros con mortero C:A 1:4 e=1.5cm (rayado + primario + fino)",
        "unit": "m2",
        "rate": "32.00",
        "category": "Acabados",
        "classification": {"rne": "E.070"},
        "tags": ["tarrajeo", "interior", "muro", "mortero"],
    },
    {
        "code": "03.02.02",
        "description": "Tarrajeo de cielorraso con mortero C:A 1:4 e=1.5cm",
        "unit": "m2",
        "rate": "38.00",
        "category": "Acabados",
        "classification": {"rne": "E.070"},
        "tags": ["tarrajeo", "cielo raso", "cielorraso"],
    },
    # 03.03 Pisos
    {
        "code": "03.03.01",
        "description": "Contrapiso de concreto e=5cm (concreto f'c=100 kg/cm2 + mortero 1:4)",
        "unit": "m2",
        "rate": "42.00",
        "category": "Pisos",
        "classification": {"rne": "E.060"},
        "tags": ["contrapiso", "concreto", "nivelacion"],
    },
    {
        "code": "03.03.02",
        "description": "Piso de cerámico nacional 60×60cm (incluye mortero 1:4 + fragua)",
        "unit": "m2",
        "rate": "75.00",
        "category": "Pisos",
        "classification": {"masterformat": "09 30 00"},
        "tags": ["piso", "ceramico", "enchape", "fragua"],
    },
    {
        "code": "03.03.03",
        "description": "Piso de porcelanato 60×60cm (incluye mortero 1:4 + fragua epóxica)",
        "unit": "m2",
        "rate": "120.00",
        "category": "Pisos",
        "classification": {"masterformat": "09 30 00"},
        "tags": ["piso", "porcelanato", "enchape", "fragua"],
    },
    # 03.04 Zócalos
    {
        "code": "03.04.01",
        "description": "Contrazócalo de cemento pulido h=10cm (incluye mortero 1:4 + pulido)",
        "unit": "m",
        "rate": "18.00",
        "category": "Acabados",
        "tags": ["contrazocalo", "cemento", "pulido"],
    },
    {
        "code": "03.04.02",
        "description": "Zócalo de cerámico nacional 30×30cm h=30cm (incluye fragua)",
        "unit": "m",
        "rate": "25.00",
        "category": "Acabados",
        "tags": ["zocalo", "ceramico", "pared"],
    },
    # 03.05 Cielorrasos
    {
        "code": "03.05.01",
        "description": "Cielorraso suspendido con baldosa de fibra mineral 60×60cm (incluye perfilería de aluminio)",
        "unit": "m2",
        "rate": "95.00",
        "category": "Cielorrasos",
        "classification": {"masterformat": "09 50 00"},
        "tags": ["cielo raso", "suspendido", "fibra mineral", "drywall"],
    },
    # 03.06 Carpintería de madera
    {
        "code": "03.06.01",
        "description": "Puerta contraplacada de cedro nacional 0.90×2.10m (incluye marco + bisagras + cerradura)",
        "unit": "und",
        "rate": "650.00",
        "category": "Carpintería",
        "classification": {"masterformat": "08 10 00"},
        "tags": ["puerta", "contraplacada", "cedro", "madera"],
    },
    # 03.07 Carpintería metálica
    {
        "code": "03.07.01",
        "description": "Ventana de aluminio natural con vidrio crudo incoloro 6mm (sistema corredizo)",
        "unit": "m2",
        "rate": "280.00",
        "category": "Carpintería",
        "classification": {"masterformat": "08 50 00"},
        "tags": ["ventana", "aluminio", "vidrio", "corredizo"],
    },
    # 03.08 Pintura
    {
        "code": "03.08.01",
        "description": "Pintura látex en interiores (2 manos: base + acabado sobre superficie tarrajeada)",
        "unit": "m2",
        "rate": "18.00",
        "category": "Pintura",
        "classification": {"masterformat": "09 90 00"},
        "tags": ["pintura", "latex", "interior", "muro"],
    },
    {
        "code": "03.08.02",
        "description": "Pintura esmalte sintético en carpintería metálica (2 manos: anticorrosivo + acabado)",
        "unit": "m2",
        "rate": "28.00",
        "category": "Pintura",
        "classification": {"masterformat": "09 90 00"},
        "tags": ["pintura", "esmalte", "metal", "anticorrosivo"],
    },

    # ═══ 04 — INSTALACIONES SANITARIAS ═══
    {
        "code": "04.01.01",
        "description": "Tubería de PVC clase 10 DN 4\" (110mm) para desagüe (incluye accesorios + pegamento)",
        "unit": "m",
        "rate": "32.00",
        "category": "Sanitarias",
        "classification": {"masterformat": "22 10 00"},
        "tags": ["tuberia", "pvc", "desague", "110mm"],
    },
    {
        "code": "04.01.02",
        "description": "Tubería de CPVC DN 1/2\" (15mm) para agua caliente (incluye accesorios + pegamento)",
        "unit": "m",
        "rate": "22.00",
        "category": "Sanitarias",
        "classification": {"masterformat": "22 10 00"},
        "tags": ["tuberia", "cpvc", "agua caliente", "15mm"],
    },
    {
        "code": "04.01.03",
        "description": "Inodoro one piece blanco estándar (incluye tanque + asiento + accesorios + instalación)",
        "unit": "und",
        "rate": "420.00",
        "category": "Sanitarias",
        "classification": {"masterformat": "22 40 00"},
        "tags": ["inodoro", "one piece", "blanco", "aparato"],
    },
    {
        "code": "04.01.04",
        "description": "Lavatorio de losa blanca tipo Ovalín (incluye grifería cromada + instalación)",
        "unit": "und",
        "rate": "280.00",
        "category": "Sanitarias",
        "classification": {"masterformat": "22 40 00"},
        "tags": ["lavatorio", "losa", "griferia", "ovalin"],
    },

    # ═══ 05 — INSTALACIONES ELÉCTRICAS ═══
    {
        "code": "05.01.01",
        "description": "Tablero eléctrico general trifásico 12 polos (incluye interruptores termomagnéticos + instalación)",
        "unit": "und",
        "rate": "850.00",
        "category": "Eléctricas",
        "classification": {"masterformat": "26 20 00"},
        "tags": ["tablero", "electrico", "trifasico", "interruptor"],
    },
    {
        "code": "05.01.02",
        "description": "Cable eléctrico NHX 90 4mm² (tubería PVC-SAP + alambre + caja de pase)",
        "unit": "m",
        "rate": "12.00",
        "category": "Eléctricas",
        "classification": {"masterformat": "26 05 00"},
        "tags": ["cable", "electrico", "empotrado", "4mm2"],
    },
    {
        "code": "05.01.03",
        "description": "Salida de techo para centro de luz (tubería PVC-SAP + cable 2.5mm² + caja + instalación)",
        "unit": "pto",
        "rate": "65.00",
        "category": "Eléctricas",
        "classification": {"masterformat": "26 50 00"},
        "tags": ["salida", "techo", "luz", "centro"],
    },
    {
        "code": "05.01.04",
        "description": "Tomacorriente doble 16A 220V con puesta a tierra (incluye placa + instalación)",
        "unit": "pto",
        "rate": "55.00",
        "category": "Eléctricas",
        "classification": {"masterformat": "26 50 00"},
        "tags": ["tomacorriente", "doble", "enchufe", "tierra"],
    },

    # ═══ 06 — SEGURIDAD ═══
    {
        "code": "06.01.01",
        "description": "Equipo de protección personal (EPP) básico por trabajador: casco + botas + chaleco + lentes + guantes (mensual)",
        "unit": "mes",
        "rate": "95.00",
        "category": "Seguridad",
        "tags": ["epp", "seguridad", "casco", "botas", "proteccion"],
    },
    {
        "code": "06.01.02",
        "description": "Señalización de seguridad en obra: cintas de peligro + conos + letreros (por frente de trabajo)",
        "unit": "glb",
        "rate": "350.00",
        "category": "Seguridad",
        "tags": ["señalizacion", "seguridad", "cintas", "conos"],
    },
]


async def seed_peru_cost_items(session) -> int:
    """
    Cargar las 35 partidas peruanas en oe_costs_item.

    Idempotente: si la partida 02.02.01 ya existe en PE_LIMA, no la duplica.
    Retorna el número de partidas insertadas.
    """
    from sqlalchemy import select
    from app.modules.costs.models import CostItem

    inserted = 0
    for p in PARTIDAS:
        # Verificar si ya existe
        existing = await session.execute(
            select(CostItem.id).where(
                CostItem.code == p["code"],
                CostItem.region == "PE_LIMA",
            ).limit(1)
        )
        if existing.scalar_one_or_none() is not None:
            continue

        item = CostItem(
            code=p["code"],
            description=p["description"],
            descriptions={"es": p["description"]},
            unit=p["unit"],
            rate=str(Decimal(p["rate"])),
            currency="PEN",
            source="sencico",
            region="PE_LIMA",
            classification=p.get("classification", {}),
            components=p.get("components", []),
            tags=p.get("tags", []),
            is_active=True,
            metadata_={
                "seed": True,
                "pack": "peru",
                "category": p.get("category", ""),
            },
        )
        session.add(item)
        inserted += 1

    if inserted:
        await session.flush()
        logger.info("Perú pack: %d partidas SENCICO cargadas en oe_costs_item", inserted)
    else:
        logger.info("Perú pack: partidas ya existentes — seed omitido")

    return inserted
