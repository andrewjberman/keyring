"""MDPF_DEMQUE round 2, DQ-t-8 criterion AC2: S_00 is in the scheduled Cottonwood gold run, OPTIONAL, ahead of the first
dimension step. Reads infra/aws/terraform/cot-pipeline/ssm.tf and requires exactly one line
`run_gold S_00 build_canonical_prices_v2.py ... optional` appearing BEFORE the `run_gold A_00` line, and the A_00..D_04 lines
unchanged in count (control arm: 18 run_gold steps before, 19 after). SCHED-OK; else SCHED-BAD <reason>.
"""
from __future__ import annotations

import os
import re
import sys

TF = os.path.join("infra", "aws", "terraform", "cot-pipeline", "ssm.tf")

if __name__ == "__main__":
    text = open(TF, encoding="utf-8").read()
    steps = re.findall(r'"run_gold (\S+) ', text)
    s00 = [m for m in re.finditer(r'"run_gold S_00 build_canonical_prices_v2\.py [^\n]*optional"', text)]
    if len(s00) != 1:
        print("SCHED-BAD S_00 optional lines=%d (steps=%d)" % (len(s00), len(steps)))
        sys.exit(1)
    a00 = text.find('"run_gold A_00 ')
    if a00 < 0 or s00[0].start() > a00:
        print("SCHED-BAD S_00 is not ahead of A_00")
        sys.exit(1)
    others = [s for s in steps if s != "S_00"]
    if len(others) != 18:
        print("SCHED-BAD the 18 existing steps changed: %d" % len(others))
        sys.exit(1)
    print("SCHED-OK steps=%d (S_00 optional, first)" % len(steps))
    sys.exit(0)
