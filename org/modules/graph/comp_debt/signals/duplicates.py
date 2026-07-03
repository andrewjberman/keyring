#!/usr/bin/env python3
"""DUPLICATES signal -- CALL comp-dups (dup_scan.run_scan). NEVER fork.

MILESTONE 3 (NFRA_COMPDEBT_PRD.md 8.3). comp-dups is the DONE duplicates signal (a
BM25 dup/dead-twin scanner with a Rule-22 dual-evidence dead-confirm). This adapter is a
THIN mapping layer: it CALLS dup_scan.run_scan (or reads the nightly dups_latest.json
ledger) and translates its findings into grounding_lib.Signal objects for fuse.py. It
adds NO new duplicate-detection logic -- reuse, not reimplement.

Level mapping (Rule 22): a duplicate is a SYMPTOM (INFERRED) -- two copies is a
double-management smell, not proof of debt (both copies may be live). It becomes CONFIRMED
only when dup_scan's own dead-confirm leg (dead_status) says CONFIRMED_DEAD -- i.e. the twin
is graph-zero-consumer AND metric-zero over the window. That is exactly the dual-evidence
grounding_lib now generalizes; comp-dups already runs it for the label-collision tier.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).resolve()
_COMP_DEBT = _HERE.parents[1]
if str(_COMP_DEBT) not in sys.path:
    sys.path.insert(0, str(_COMP_DEBT))
import grounding_lib as g  # noqa: E402

REPO = _HERE.parents[5]  # signals/ -> comp_debt -> graph -> modules -> org -> REPO
_DUP_SCAN_PATH = REPO / "org" / "modules" / "graph" / "debtscan" / "dup_scan.py"
_DUPS_LATEST = REPO / "org" / "modules" / "graph" / "debtscan" / "dups_latest.json"

SIGNAL = "duplicates"


def _load_dup_scan():
    """Import debtscan/dup_scan.py by path (it is not an installed package). We CALL it;
    we never copy its logic."""
    spec = importlib.util.spec_from_file_location("dup_scan", _DUP_SCAN_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load dup_scan from {_DUP_SCAN_PATH}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _level_for(dead_status: str | None) -> str:
    """A duplicate is INFERRED unless dup_scan's dual-evidence dead-confirm says
    CONFIRMED_DEAD (the twin is graph-zero AND metric-zero over the window)."""
    if dead_status and "CONFIRMED_DEAD" in dead_status:
        return g.LEVEL_CONFIRMED
    return g.LEVEL_INFERRED


def _firm_ok(firm: str | None, a_firm, b_firm) -> bool:
    """Firm-scope: when --firm is set, keep only findings that touch that firm. dup_scan
    already SUPPRESSES cross-firm pairs (they are by-design), so this is a scope filter,
    not a separation gate -- but it keeps a firm-scoped run from surfacing other firms."""
    if not firm:
        return True
    return firm in (a_firm, b_firm) or a_firm is None or b_firm is None


def signals_from_result(res: dict, *, firm: str | None = None) -> list[g.Signal]:
    """Map a dup_scan.run_scan() result dict into comp-debt Signal objects."""
    out: list[g.Signal] = []

    # TF EXACT-label cross-module collisions -- the real double-management signal.
    for f in res.get("tf_name_findings", []):
        if f.get("tier") != "high":
            continue  # NAME_NEAR_INFO is informational -- not a debt signal
        dead = f.get("dead_status")
        out.append(g.Signal(
            signal=SIGNAL, state="label-collision", level=_level_for(dead),
            grounding={
                "desired": f"comp-dups TF_LABEL_COLLISION: {f.get('a')} <{f.get('a_mod')}> "
                           f"~ {f.get('b')} <{f.get('b_mod')}> (BM25 {f.get('score')})",
                "applied": f"dead_status={dead}" if dead else "dead-confirm not run (not dead-prior)",
                "resource_id": f.get("a"),
            }))

    # CONTENT exact-body dup families -- a copied module under >1 distinct filename.
    for r in res.get("content", {}).get("exact_dups", []):
        members = r.get("members", [])
        out.append(g.Signal(
            signal=SIGNAL, state="content-dup", level=g.LEVEL_INFERRED,
            grounding={
                "desired": f"comp-dups CONTENT_EXACT_DUP x{len(members)} ({r.get('lines')}L) "
                           f"{r.get('distinct_names')}",
                "applied": "content-identity only (no dead-confirm) -- copied module smell, INFERRED",
                "resource_id": members[0] if members else None,
                "members": members,
            }))
    return out


def run(*, firm: str | None = None, from_ledger: bool = False) -> list[g.Signal]:
    """Produce the DUPLICATES signals. from_ledger reads the nightly dups_latest.json
    (cheap); default CALLS dup_scan.run_scan live (fresh)."""
    if from_ledger:
        import json
        try:
            res = json.loads(_DUPS_LATEST.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise RuntimeError(f"cannot read dups_latest.json: {exc}") from exc
    else:
        dup_scan = _load_dup_scan()
        res = dup_scan.run_scan()
    return signals_from_result(res, firm=firm)


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="comp-debt.signals.duplicates",
                                 description="DUPLICATES signal -- CALLs comp-dups; emit-only.")
    ap.add_argument("--firm", default=None)
    ap.add_argument("--from-ledger", action="store_true", help="read dups_latest.json instead of a live scan")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    sigs = run(firm=args.firm, from_ledger=args.from_ledger)
    if args.json:
        import json
        print(json.dumps([s.to_dict() for s in sigs], indent=2))
        return 0
    conf = sum(1 for s in sigs if s.level == g.LEVEL_CONFIRMED)
    print(f"DUPLICATES signals: {len(sigs)} ({conf} CONFIRMED, {len(sigs) - conf} INFERRED)")
    for s in sigs[:40]:
        print(f"  [{s.level:<9}] {s.state:<15} {s.grounding.get('resource_id')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
