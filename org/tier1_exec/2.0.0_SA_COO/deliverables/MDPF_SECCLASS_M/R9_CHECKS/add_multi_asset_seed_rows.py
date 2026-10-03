"""add_multi_asset_seed_rows.py -- MDPF_SECCLASS batch 183 ONE packet: the multi_asset TICKER rows into the seed source.

Reads R9_CHECKS/MULTI_ASSET_ROW_SET_20261003.tsv and adds, for every MOVE and every ticker WRITE line (20 tickers; the 12
`CUSIP:` keys are written by R7_CHECKS/write_cusip_rows.py, not by the seed source), the row set's class and sub class (never
typed here), the sub class as the sector (the first act's rule where no peer sector exists), the feed's name, and a
management style (passive for an index fund, active otherwise -- listed below). None of these tickers is in the module today,
so there is no peer to copy from: the ruled values come from the row set. Idempotent: a ticker already present is left alone.

The 7 MOVE tickers enter the module too, so the seed source stays the one canonical source; the seed script's merge rule
reports them as CONFLICT until move_multi_asset_rows.py has moved the table rows, and as already correct after.

Usage (repo root): python .../R9_CHECKS/add_multi_asset_seed_rows.py [--src <path to etf_classification.py>]
Default --src is the repo's infra/aws/lambda/v2_portal/_shared/etf_classification.py (edited in place).
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
DEFAULT_SRC = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared" / "etf_classification.py"
ROW_SET = HERE / "MULTI_ASSET_ROW_SET_20261003.tsv"
PASSIVE = {"AOR", "VTHRX", "VSMGX", "VTIVX", "VTTHX", "LIPKX", "FTYPX"}   # index-tracking target-date / fixed-mix funds
HDR = ("    # multi_asset (MDPF_SECCLASS, CTO batches 164 and 183, 2026-10-03): allocation funds; class and sub class from the "
       "row set R9_CHECKS/MULTI_ASSET_ROW_SET_20261003.tsv (INFERRED from each fund's name)\n")


def rows():
    out = {}
    for line in ROW_SET.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        f = line.split("\t")
        if f[0] in ("MOVE", "WRITE") and not f[1].startswith("CUSIP:"):
            out[f[1]] = {"name": f[2], "class": f[4], "sub": f[5]}
    return out


def _dict_span(src: str, name: str):
    tree = ast.parse(src)
    for node in tree.body:
        tgt = node.target if isinstance(node, ast.AnnAssign) else (node.targets[0] if isinstance(node, ast.Assign) else None)
        if getattr(tgt, "id", None) == name:
            return node, ast.literal_eval(node.value)
    raise SystemExit("REFUSED: %s not found" % name)


def _append(src: str, name: str, entries: list) -> str:
    node, _ = _dict_span(src, name)
    lines = src.splitlines(keepends=True)
    close = node.end_lineno - 1
    assert lines[close].strip() in ("}", "})"), (name, lines[close])
    return "".join(lines[:close] + [HDR] + entries + lines[close:])


def q(s: str) -> str:
    """Quote a name for a single-quoted Python literal."""
    return s.replace("\\", "\\\\").replace("'", "\\'")


def main(src_path: Path) -> int:
    want = rows()
    assert len(want) == 20, "the row set names %d ticker rows, 20 expected" % len(want)
    src = src_path.read_text(encoding="utf-8")
    _, cls = _dict_span(src, "ETF_CLASSIFICATIONS")
    new = [t for t in want if t not in cls]
    if not new:
        print("OK: nothing to add")
        return 0
    src = _append(src, "ETF_CLASSIFICATIONS", ["    '%s': '%s',\n" % (t, want[t]["class"]) for t in new])
    src = _append(src, "ETF_SUB_ASSET_CLASS", ["    '%s': '%s',\n" % (t, want[t]["sub"]) for t in new])
    src = _append(src, "ETF_SECTOR_MAPPING", ["    '%s': '%s',\n" % (t, want[t]["sub"]) for t in new])
    src = _append(src, "ETF_NAME_OVERRIDES", ["    '%s': '%s',\n" % (t, q(want[t]["name"])) for t in new])
    src = _append(src, "ETF_MANAGEMENT_STYLE", ["    '%s': '%s',\n" % (t, "passive" if t in PASSIVE else "active")
                                                for t in new])
    ast.parse(src)
    src_path.write_text(src, encoding="utf-8", newline="\n")
    print("added %d rows: %s" % (len(new), " ".join(new)))
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=DEFAULT_SRC)
    sys.exit(main(ap.parse_args().src))
