"""MDPF_STRATID workstream 2, ST-w-5 criterion AC1 (disarm of row MDPF_STRATID-D1-W5-S1): every carrier that ships
`rebalancer_schemas.py` also ships `opal_strategy_matcher.py`, because rebalancer_schemas now imports it. Carriers (census at the cut,
2026-10-09 ~05:3xZ): the six files below. A carrier that names rebalancer_schemas.py and not opal_strategy_matcher.py fails; a
carrier that no longer names rebalancer_schemas.py is printed and passes. W25-SHIP-OK, else W25-SHIP-BAD. Run from the worktree root."""
from __future__ import annotations

import sys

CARRIERS = [
    "infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py",
    "infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/mdpf-gold-lambda.BUILD_MANIFEST.json",
    "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/BUILD_MANIFEST.json",
    "infra/aws/lambda/investor-reporting/performance/build_tools/build_candidate.py",
    "infra/aws/lambda/investor-reporting/PATH_MANIFEST.json",
    ".tools/safe_deploy_core.py",
]


def main() -> int:
    bad = []
    for p in CARRIERS:
        with open(p, encoding="utf-8") as f:
            t = f.read()
        has_rs, has_m = "rebalancer_schemas.py" in t, "opal_strategy_matcher.py" in t
        print("%-90s rebalancer_schemas=%s matcher=%s" % (p, has_rs, has_m))
        if has_rs and not has_m:
            bad.append(p)
    if bad:
        print("W25-SHIP-BAD %d of %d carrier(s) ship rebalancer_schemas.py without the matcher" % (len(bad), len(CARRIERS)))
        return 1
    print("W25-SHIP-OK %d of %d carriers" % (len(CARRIERS), len(CARRIERS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
