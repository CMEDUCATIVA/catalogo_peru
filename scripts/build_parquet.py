"""build_parquet.py - Excel/CSV -> parquet CWICR para Peru."""
import argparse, json, logging, sys
from decimal import Decimal
from pathlib import Path
import polars as pl

logger = logging.getLogger(__name__)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True, type=Path)
    p.add_argument("--region", "-r", default="PE_LIMA")
    p.add_argument("--currency", "-c", default="PEN")
    p.add_argument("--source", "-s", default="sencico")
    p.add_argument("--output", "-o", required=True, type=Path)
    a = p.parse_args()
    logging.basicConfig(level=logging.INFO)
    ext = a.input.suffix.lower()
    if ext == ".xlsx": df = pl.read_excel(str(a.input))
    elif ext == ".csv": df = pl.read_csv(str(a.input), infer_schema_length=10000)
    elif ext == ".json":
        with open(a.input) as f: data = json.load(f)
        if isinstance(data, dict): data = data.get("items", data.get("data", []))
        df = pl.DataFrame(data)
    else: sys.exit(1)
    rows = df.fill_null("").to_dicts()
    for r in rows:
        r.setdefault("currency", a.currency); r.setdefault("region", a.region)
        r.setdefault("source", a.source); r.setdefault("is_active", True)
        rate = r.get("rate", 0)
        if isinstance(rate, (int, float)): r["rate"] = str(Decimal(str(rate)))
    a.output.parent.mkdir(parents=True, exist_ok=True)
    pl.DataFrame(rows).write_parquet(str(a.output), compression="zstd")
    logger.info("Parquet: %s (%d filas)", a.output, len(rows))

if __name__ == "__main__": main()
