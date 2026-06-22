"""Actualizar precios desde SENCICO."""
import argparse, logging
from datetime import date
from decimal import Decimal
from pathlib import Path
import polars as pl

logger = logging.getLogger(__name__)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--parquet", required=True, type=Path)
    p.add_argument("--sencico-xlsx", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    logging.basicConfig(level=logging.INFO)
    df = pl.read_parquet(str(a.parquet))
    dn = pl.read_excel(str(a.sencico_xlsx))
    updated = 0
    for r in dn.iter_rows(named=True):
        code = r.get("rate_code", r.get("code", ""))
        nr = r.get("rate")
        mask = df["rate_code"] == code
        if mask.any():
            idx = mask.arg_true()[0]
            old = Decimal(str(df[idx, "rate"]))
            new = Decimal(str(nr))
            if old != new:
                df[idx, "rate"] = str(new)
                df[idx, "source_date"] = str(date.today())
                updated += 1
    logger.info("Actualizados: %d", updated)
    if not a.dry_run:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        df.write_parquet(str(a.output), compression="zstd")

if __name__ == "__main__": main()
