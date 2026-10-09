"""MDPF_HEALGAP round 2, cell HG-t-8 (ruling R2-1): the runner role may read its own run-result objects, and nothing more.

  python hg_t8_iam.py [TF_PATH]   (default infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf)

Reads the `aws_iam_role_policy.cot_rebalancer_runner_write` block and checks:
  - exactly one statement grants s3:GetObject;
  - that statement is Effect Allow with the single resource
    "arn:aws:s3:::${local.monolith_bucket}/blackdiamond/${one(local.monolith_source_scopes.blackdiamond)}/meta/*-result.json"
    (CTO ruling H @1af255b7da: the firm segment is read from monolith.tf's grammar, after the naming gate refused a typed
    'cottonwood' -- row MDPF_HEALGAP-D1-S9);
  - the three statements already present (WriteOwnCottonwoodBronzeMeta, ListCottonwoodForLandingGuard,
    DenyBlackdiamond49fFirmSep) are still present, and no other s3 action is added.
Last line: IAM-OK or IAM-BAD <reason>. Static text read; no AWS call.
"""
from __future__ import annotations

import re
import sys

TF = "infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf"
WANT = '"arn:aws:s3:::${local.monolith_bucket}/blackdiamond/${one(local.monolith_source_scopes.blackdiamond)}/meta/*-result.json"'  # CTO ruling H @1af255b7da: firm read from the grammar, no NEW carrier (row D1-S9)
KEEP = ("WriteOwnCottonwoodBronzeMeta", "ListCottonwoodForLandingGuard", "DenyBlackdiamond49fFirmSep")


def block(text: str) -> str:
    m = re.search(r'resource "aws_iam_role_policy" "cot_rebalancer_runner_write" \{', text)
    if not m:
        return ""
    depth, i = 0, m.end() - 1
    for j in range(i, len(text)):
        depth += {"{": 1, "}": -1}.get(text[j], 0)
        if depth == 0:
            return text[i:j + 1]
    return ""


def statements(b: str) -> list:
    out, depth, start = [], 0, None
    body = b[b.find("Statement"):]
    for j, ch in enumerate(body):
        if ch == "{":
            depth += 1
            if depth == 1:
                start = j
        elif ch == "}":
            if depth == 1 and start is not None:
                out.append(body[start:j + 1])
            depth -= 1
    return out


def main(path: str) -> int:
    with open(path, encoding="utf-8") as fh:
        b = block(fh.read())
    if not b:
        print("IAM-BAD no cot_rebalancer_runner_write block")
        return 1
    sts = statements(b)
    missing = [s for s in KEEP if not any(f'"{s}"' in st for st in sts)]
    if missing:
        print(f"IAM-BAD existing statement(s) removed: {missing}")
        return 1
    gets = [st for st in sts if "s3:GetObject" in st]
    if len(gets) != 1:
        print(f"IAM-BAD statements granting s3:GetObject: {len(gets)} (want 1)")
        return 1
    g = gets[0]
    res = re.findall(r'"arn:aws:s3:::[^"]*"', g)
    if '"Allow"' not in g or res != [WANT]:
        print(f"IAM-BAD GetObject statement effect/resources wrong: resources={res}")
        return 1
    action_vals = re.findall(r'Action\s*=\s*(\[[^\]]*\]|"[^"]*")', b)
    actions = set(a for v in action_vals for a in re.findall(r'"(s3:[A-Za-z*]+)"', v))
    extra = actions - {"s3:PutObject", "s3:ListBucket", "s3:GetObject", "s3:*"}
    if extra:
        print(f"IAM-BAD new s3 action(s): {sorted(extra)}")
        return 1
    print(f"IAM-OK statements={len(sts)} getobject_resource={WANT}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else TF))
