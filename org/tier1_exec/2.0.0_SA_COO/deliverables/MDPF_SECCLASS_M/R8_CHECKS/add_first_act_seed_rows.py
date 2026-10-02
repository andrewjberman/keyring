"""add_first_act_seed_rows.py -- MDPF_SECCLASS BD forward fix 2, per-ticker first act (CTO rulings batches 139, 144-145).

Adds the ruled rows to the seed source by PEER: each new ticker copies its peer's class, sub class and sector from the module
itself (never typed), and carries its own name, instrument kind and management style. Idempotent: a ticker already present is
left alone. Run once from the repo root; it edits infra/aws/lambda/v2_portal/_shared/etf_classification.py in place.
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
SRC = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared" / "etf_classification.py"

# ticker -> (peer, name, instrument_kind, management_style or None). Ruling per group in the half.
ROWS = {
    # A (batch 145 A: go)
    "AWSHX": ("IVV", "American Funds Washington Mutual Investors Fund Class A", "fund", "active"),
    "MSSGX": ("IJR", "Morgan Stanley Institutional Inception Portfolio Class I", "fund", "active"),
    "DBO":   ("USO", "Invesco DB Oil Fund", "fund", "passive"),
    "SCHH":  ("VNQ", "Schwab U.S. REIT ETF", "fund", "passive"),
    "TRREX": ("VNQ", "T. Rowe Price Real Estate Fund", "fund", "active"),
    "SMA":   ("VNQ", "SmartStop Self Storage REIT Inc.", "single_security", None),
    "OIH":   ("XLE", "VanEck Oil Services ETF", "fund", "passive"),
    # B (batch 145 B: buffer ETFs and JHQTX take structured / Hedge; QQH takes QQQ's row)
    "BMAR":  ("VXX", "Innovator U.S. Equity Buffer ETF - March", "fund", "passive"),
    "QMAR":  ("VXX", "FT Vest Nasdaq-100 Buffer ETF - March", "fund", "passive"),
    "FMAR":  ("VXX", "FT Vest U.S. Equity Buffer ETF - March", "fund", "passive"),
    "JANW":  ("VXX", "AllianzIM U.S. Equity Buffer20 Jan ETF", "fund", "passive"),
    "DECZ":  ("VXX", "TrueShares Structured Outcome (December) ETF", "fund", "passive"),
    "SIXO":  ("VXX", "AllianzIM U.S. Equity 6 Month Buffer10 Allocation ETF", "fund", "passive"),
    "JHQTX": ("VXX", "JPMorgan Hedged Equity 3 Fund Class I", "fund", "active"),
    "QQH":   ("QQQ", "HCM Defender 100 Index ETF", "fund", "active"),
    # D (batch 145 D: GLDM settled by CUSIP -- 98149E303 is SPDR Gold MiniShares)
    "GLDM":  ("GLD", "SPDR Gold MiniShares Trust", "fund", "passive"),
}
HDR = "    # BD per-ticker first act (MDPF_SECCLASS, CTO rulings batches 139 and 145, 2026-10-02): each row copies its peer's class\n"


def _dict_span(src: str, name: str):
    tree = ast.parse(src)
    for node in tree.body:
        tgt = node.target if isinstance(node, ast.AnnAssign) else (node.targets[0] if isinstance(node, ast.Assign) else None)
        if getattr(tgt, "id", None) == name:
            return node, ast.literal_eval(node.value)
    raise SystemExit("REFUSED: %s not found" % name)


def _append(src: str, name: str, entries: list) -> str:
    """Insert `entries` (already formatted lines) before the closing brace of the top-level literal `name`."""
    node, _ = _dict_span(src, name)
    lines = src.splitlines(keepends=True)
    close = node.end_lineno - 1  # 0-based index of the line holding the closing brace
    assert lines[close].strip() in ("}", "})"), (name, lines[close])
    return "".join(lines[:close] + [HDR] + entries + lines[close:])


def main() -> int:
    src = SRC.read_text(encoding="utf-8")
    _, cls = _dict_span(src, "ETF_CLASSIFICATIONS")
    _, sub = _dict_span(src, "ETF_SUB_ASSET_CLASS")
    _, sec = _dict_span(src, "ETF_SECTOR_MAPPING")
    new = [t for t in ROWS if t not in cls]
    if not new:
        print("OK: nothing to add")
        return 0
    for t in new:
        peer = ROWS[t][0]
        if peer not in cls or peer not in sub:
            raise SystemExit("REFUSED: peer %s of %s has no class or sub class in the module" % (peer, t))
    src = _append(src, "ETF_CLASSIFICATIONS", ["    '%s': '%s',\n" % (t, cls[ROWS[t][0]]) for t in new])
    src = _append(src, "ETF_SUB_ASSET_CLASS", ["    '%s': '%s',\n" % (t, sub[ROWS[t][0]]) for t in new])
    src = _append(src, "ETF_SECTOR_MAPPING", ["    '%s': '%s',\n" % (t, sec.get(ROWS[t][0], sub[ROWS[t][0]])) for t in new])
    src = _append(src, "ETF_NAME_OVERRIDES", ["    '%s': '%s',\n" % (t, ROWS[t][1].replace("'", "\\'")) for t in new])
    style = [t for t in new if ROWS[t][3]]
    src = _append(src, "ETF_MANAGEMENT_STYLE", ["    '%s': '%s',\n" % (t, ROWS[t][3]) for t in style])
    singles = [t for t in new if ROWS[t][2] == "single_security"]
    if singles:
        src = _append(src, "_SINGLE_SECURITY_TICKERS", ["    '%s',\n" % t for t in singles])
    SRC.write_text(src, encoding="utf-8", newline="\n")
    print("added %d rows: %s" % (len(new), " ".join(new)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
