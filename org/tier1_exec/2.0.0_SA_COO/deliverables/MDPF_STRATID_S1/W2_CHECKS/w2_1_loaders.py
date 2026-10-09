"""MDPF_STRATID workstream 2, W2-1 criterion AC2 (BOUND): the three ETFS producers' `_load_universe` rule, applied to the repo
config, still returns exactly the four tickers in order. The rule is copied from the three loaders (cot :101, inf :88, bd :57):
`tickers = cfg.get("tickers") or cfg.get("etfs") or cfg`; upper/strip each. Their source is read first and must still carry it.
W21-LOADERS-OK, else W21-LOADERS-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import json
import sys

PATH = "infra/aws/etfs/config/etf_universe.json"
LOADERS = ["infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py",
           "infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py",
           "infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily-canonical/lambda_function.py"]
RULE = 'tickers = cfg.get("tickers") or cfg.get("etfs") or cfg'


def main() -> int:
    for p in LOADERS:
        with open(p, encoding="utf-8") as f:
            if RULE not in f.read():
                print("W21-LOADERS-BAD loader rule changed in %s; re-derive this check" % p)
                return 1
    with open(PATH, encoding="utf-8") as f:
        cfg = json.load(f)
    tickers = cfg.get("tickers") or cfg.get("etfs") or cfg
    out = [str(t).upper().strip() for t in tickers]
    if out != ["DIVZ", "IDVZ", "PFDE", "PFOE"]:
        print("W21-LOADERS-BAD the producers would read %r" % out)
        return 1
    print("3 of 3 loaders carry the rule; universe read = %s" % out)
    print("W21-LOADERS-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
