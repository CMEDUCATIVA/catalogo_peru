"""
Datos semilla: Catalogo de Recursos CAPECO para Peru (110 insumos).

Carga materiales, mano de obra y equipos desde la base CAPECO
a la tabla oe_catalog_resource del ERP. Cada recurso se registra
con region=PE_LIMA, currency=PEN.

Idempotente: si el marcador INS-PE-CEM-001 ya existe, omite.
"""

from __future__ import annotations

import logging
import os
import sqlite3
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.catalog.models import CatalogResource

logger = logging.getLogger(__name__)

_MARKER_CODE = "INS-PE-CEM-001"

_UNIT_MAP = {
    "UN0000000001": "m3", "UN0000000002": "hh", "UN0000000003": "m2",
    "UN0000000006": "und", "UN0000000010": "kg", "UN0000000015": "t",
    "UN0000000016": "pza", "UN0000000017": "gal", "UN0000000020": "m",
    "UN0000000022": "bls", "UN0000000028": "hm", "UN0000000032": "gbl",
    "UN0000000034": "mes", "UN0000000038": "pto", "UN0000000047": "kit",
    "UN0000000072": "l", "UN0000000096": "sco", "UN0000000099": "blt",
}

_TYPE_MAP = {
    "MANO DE OBRA": "labor", "MATERIALES": "material",
    "EQUIPO": "equipment", "SUB-CONTRATOS": "subcontractor",
}


def _get_capeco_path() -> str | None:
    """Buscar Capeco.sqlite en el pack."""
    here = os.path.dirname(__file__)
    for _ in range(5):
        candidate = os.path.join(here, "data", "sql", "Capeco.sqlite")
        if os.path.exists(candidate):
            return candidate
        here = os.path.dirname(here)
    return None


def _read_capeco_resources() -> list[dict]:
    """Leer los 110 productos desde Capeco.sqlite."""
    path = _get_capeco_path()
    if not path:
        logger.warning("Capeco.sqlite no encontrado")
        return []

    db = sqlite3.connect(path)
    rows = db.execute("""
        SELECT p.descripcion_producto, p.id_unidad, p.costo_unitariolista,
               c.descripcion_categoria, p.especificaciones
        FROM producto p
        LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
        ORDER BY c.descripcion_categoria, p.descripcion_producto
    """).fetchall()
    db.close()

    resources = []
    for r in rows:
        name = (r[0] or "").strip()
        unit_id = r[1] or ""
        price = r[2] or 1
        cat = r[3] or "MATERIALES"
        spec = r[4] or ""
        if not name: continue

        unit = _UNIT_MAP.get(unit_id, "und")
        res_type = _TYPE_MAP.get(cat, "material")
        short = name[:25].replace(" ", "_").replace("/", "-").upper()
        resource_code = f"INS-PE-{short}"

        resources.append({
            "resource_code": resource_code,
            "name": name,
            "resource_type": res_type,
            "category": cat,
            "unit": unit,
            "base_price": str(Decimal(str(price))),
            "currency": "PEN",
            "region": "PE_LIMA",
            "specifications": {"capeco_unit": unit_id, "notes": spec or ""},
        })
    return resources


async def seed_peru_catalog(session: AsyncSession, project_ids=None) -> dict:
    """Cargar ~110 recursos CAPECO en oe_catalog_resource. Idempotente."""
    existing = await session.execute(
        select(CatalogResource.id).where(
            CatalogResource.resource_code == _MARKER_CODE
        ).limit(1)
    )
    if existing.scalar_one_or_none() is not None:
        logger.info("Catalogo Peru ya existe - seed omitido")
        return {}

    resources = _read_capeco_resources()
    if not resources:
        return {}

    inserted = 0
    by_type: dict[str, int] = {}
    for r in resources:
        item = CatalogResource(
            resource_code=r["resource_code"], name=r["name"],
            resource_type=r["resource_type"], category=r["category"],
            unit=r["unit"], base_price=r["base_price"],
            min_price="0", max_price="0", currency=r["currency"],
            region=r["region"], source="capeco_peru", usage_count=0,
            specifications=r["specifications"], is_active=True,
            metadata_={"seed": True, "pack": "peru"},
        )
        session.add(item)
        by_type[r["resource_type"]] = by_type.get(r["resource_type"], 0) + 1
        inserted += 1

    await session.flush()
    logger.info("Catalogo Peru: %d recursos (%s)", inserted, by_type)
    return {"catalog_peru": inserted, "by_type": by_type}
