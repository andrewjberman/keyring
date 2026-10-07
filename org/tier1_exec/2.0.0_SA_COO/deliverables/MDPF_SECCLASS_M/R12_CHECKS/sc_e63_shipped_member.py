#!/usr/bin/env python3
"""sc_e63_shipped_member.py -- MDPF_SECCLASS round 10 SC-e-63 (rows W31-S1, W34-S1): the deploy gate ships
rivalfunds_classification.py beside the other lib/_shared members, and both E_18 scripts pass a canonical lookup to plan_rows.

READ-ONLY, text read. ok when .tools/safe_deploy_core.py names infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py
in every lib/_shared "members" tuple or list that names etf_classification_scheduled.py, and each E_18 (bd, cot) names
canonical_lookup_from_records and passes canonical_lookup= to plan_rows. Prints SC-E63 ok=<bool>.
"""
import re
import sys
from pathlib import Path

ROOT = Path.cwd()  # the repo root the worker runs from (its own worktree), never this file's tree
CORE = ROOT / ".tools/safe_deploy_core.py"
MEMBER = "infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py"
E18 = ["data/black_diamond/scripts/gold/E_18.detect_new_securities.py", "data/cot/scripts/gold/E_18.detect_new_securities.py"]


def main():
    text = CORE.read_text(encoding="utf-8")
    lists = re.findall(r"\"members\":\s*[\[(]([^\[\]()]*etf_classification_scheduled\.py[^\[\]()]*)[\])]", text)
    with_member = sum(1 for blk in lists if MEMBER in blk)
    callers = []
    for p in E18:
        src = (ROOT / p).read_text(encoding="utf-8")
        callers.append("canonical_lookup_from_records" in src and re.search(r"canonical_lookup\s*=", src) is not None)
    ok = bool(lists) and with_member == len(lists) and all(callers)
    print(f"SC-E63 ok={ok} member_lists={len(lists)} with_rivalfunds={with_member} e18_bd={callers[0]} e18_cot={callers[1]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
