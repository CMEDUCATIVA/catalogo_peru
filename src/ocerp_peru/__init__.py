"""OpenConstructionERP - Peru Partner Pack.

Un solo paquete. Al instalar:
  - Catalogo de recursos: 110 insumos CAPECO (materiales, labor, equipo)
  - Cost items: 35 partidas SENCICO con precios PEN
  - CWICR: regiones PE_LIMA, PE_AREQUIPA, PE_CUSCO
  - Moneda: PEN, Impuesto: IGV 18%
  - Wizard de onboarding
"""

from __future__ import annotations
from ocerp_peru.manifest import MANIFEST
__all__ = ["MANIFEST"]
__version__ = "0.1.0"


def _register_cwicr():
    """Inyectar regiones de Peru en el catalogo CWICR."""
    try:
        from app.modules.costs.cwicr_v3_catalogue import CWICR_V3_CATALOGUES as _C
        from ocerp_peru.cwicr_catalogue import PE_CATALOGUES
        existing = {c.region for c in _C}
        new = tuple(c for c in PE_CATALOGUES if c.region not in existing)
        if new:
            import app.modules.costs.cwicr_v3_catalogue as _m
            _m.CWICR_V3_CATALOGUES = tuple(_C) + new
            import logging
            logging.getLogger(__name__).info("Peru Pack: %d regiones CWICR registradas", len(new))
    except ImportError:
        pass


# ── Funciones de seed (llamadas por el ERP al aplicar el pack) ──
async def seed_resources(session):
    """Seed: Catalogo de recursos CAPECO."""
    from ocerp_peru.seed_catalog import seed_peru_catalog
    return await seed_peru_catalog(session)


async def seed_cost_items(session):
    """Seed: Partidas SENCICO."""
    from ocerp_peru.seed_data import seed_peru_cost_items
    return await seed_peru_cost_items(session)


_register_cwicr()
