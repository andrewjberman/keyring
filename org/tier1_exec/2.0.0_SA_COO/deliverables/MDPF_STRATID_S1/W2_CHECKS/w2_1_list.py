"""MDPF_STRATID workstream 2, W2-1 criterion AC1: the one Opal ETF list carries full fund names (each cited) and the SMA name
rules as data, beside the unchanged tickers. W21-LIST-OK, else W21-LIST-BAD <reason>. Run from the repo (worktree) root."""
from __future__ import annotations

import json
import re
import sys

PATH = "infra/aws/etfs/config/etf_universe.json"
TICKERS = ["DIVZ", "IDVZ", "PFDE", "PFOE"]


def bad(msg: str) -> int:
    print("W21-LIST-BAD %s" % msg)
    return 1


def main() -> int:
    try:
        with open(PATH, encoding="utf-8") as f:
            cfg = json.load(f)
    except Exception as exc:  # noqa: BLE001
        return bad("unreadable %s: %s" % (PATH, exc))
    if cfg.get("tickers") != TICKERS:
        return bad("tickers moved: %r" % cfg.get("tickers"))
    fn = cfg.get("full_names")
    if not isinstance(fn, dict) or sorted(fn) != sorted(TICKERS):
        return bad("full_names must key exactly %s, got %r" % (TICKERS, None if fn is None else sorted(fn)))
    for t, v in fn.items():
        if not (isinstance(v, dict) and str(v.get("name", "")).strip() and str(v.get("source", "")).strip()):
            return bad("full_names[%s] needs non-empty name and source, got %r" % (t, v))
    rules = cfg.get("sma_name_rules")
    if not isinstance(rules, list) or not rules:
        return bad("sma_name_rules missing or empty")
    compiled = []
    for r in rules:
        if not isinstance(r, dict) or "member" not in r or not r.get("pattern") or not r.get("source"):
            return bad("rule needs member (may be null), pattern, source: %r" % r)
        try:
            compiled.append((re.compile(r["pattern"], re.I), r["member"]))
        except re.error as exc:
            return bad("pattern does not compile %r: %s" % (r["pattern"], exc))

    def members(name: str) -> set:
        return {m for rx, m in compiled if rx.search(name)}

    probes = [("Pathfinder Disciplined Equity", {"pfde"}), ("Pathfinder Focused Opportunity", {"pfoe"}),
              ("Opal_Muni_Sleeve", {None}),
              ("Opal_Muni_Income", set())]  # A7: Andrew-direct ~05:3xZ, Opal_Muni_Income is a Custom model, no rule
    for name, want in probes:
        if members(name) != want:
            return bad("rules give %r for %r, want %r" % (members(name), name, want))
    print("full_names: %s" % ", ".join("%s=%s" % (t, fn[t]["name"]) for t in TICKERS))
    print("sma_name_rules: %d row(s)" % len(rules))
    print("W21-LIST-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
