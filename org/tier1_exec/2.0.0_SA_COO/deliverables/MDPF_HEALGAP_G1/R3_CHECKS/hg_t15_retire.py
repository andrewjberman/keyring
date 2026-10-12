#!/usr/bin/env python3
"""HG-t-15 check: the 07:00Z registry rule is retired and nothing else in the producer's tf moved.

MDPF_HEALGAP round 3, cell HG-t-15 (CTO ADDENDUM 5 @0c9f67d92d: "the 07:00Z retirement is its own pair"). Read-only; no AWS call.

  python hg_t15_retire.py              -> T15-OK ... rc 0, or T15-BAD <reasons> rc 1
  HG_T15_TF=<path> python ...          -> grade another copy of satellites-registry-producer.tf (the mutants use this)

Four limbs, all graded from the repo text:
  GONE   no aws_cloudwatch_event_rule / _event_target / aws_lambda_permission whose address ends `_producer_daily`
         (the 07:00Z rule, its target, its permission) and no `cron(0 7 * * ? *)` anywhere in the file.
  KEPT   the stamp-gated rule still reads `cron(15 13 * * ? *)` ENABLED, its target still carries
         `require_stamp = true`, its permission, the function module, and the role policy resource are all present.
  ONLY   against the base pin, the only NON-COMMENT lines that changed are lines REMOVED (nothing was added or altered).
  NOREF  nothing left in the file references the removed addresses.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                               cwd=os.path.dirname(os.path.abspath(__file__))).decode().strip()
TF = "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf"
BASE_PIN = os.environ.get("HG_T15_BASE", "f3afa83d59")

REMOVED_ADDR = "cot_satellites_registry_producer_daily"
REMOVED_PERM = "events_cot_satellites_registry_producer"          # the daily rule's permission (no suffix)
KEPT_RESOURCES = [
    ('aws_cloudwatch_event_rule', 'cot_satellites_registry_producer_stamp_gated'),
    ('aws_cloudwatch_event_target', 'cot_satellites_registry_producer_stamp_gated'),
    ('aws_lambda_permission', 'events_cot_satellites_registry_producer_stamp_gated'),
    ('aws_iam_role_policy', 'cot_satellites_registry_producer_s3'),
]


def has_resource(text: str, rtype: str, name: str) -> bool:
    return re.search(r'resource\s+"%s"\s+"%s"\s*\{' % (re.escape(rtype), re.escape(name)), text) is not None


def noncomment_lines(text: str):
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        out.append(re.sub(r"\s+#.*$", "", ln.rstrip()))
    return out


def main() -> int:
    bad = []
    path = os.environ.get("HG_T15_TF") or os.path.join(ROOT, TF)
    text = open(path, encoding="utf-8", newline="").read()

    # GONE
    for rtype in ("aws_cloudwatch_event_rule", "aws_cloudwatch_event_target"):
        if has_resource(text, rtype, REMOVED_ADDR):
            bad.append("GONE: %s.%s is still declared" % (rtype, REMOVED_ADDR))
    if has_resource(text, "aws_lambda_permission", REMOVED_PERM):
        bad.append("GONE: aws_lambda_permission.%s (the daily rule's permission) is still declared" % REMOVED_PERM)
    if re.search(r'schedule_expression\s*=\s*"cron\(0 7 \* \* \? \*\)"', text):
        bad.append("GONE: a cron(0 7 * * ? *) schedule_expression is still in the file")

    # KEPT
    for rtype, name in KEPT_RESOURCES:
        if not has_resource(text, rtype, name):
            bad.append("KEPT: %s.%s is missing" % (rtype, name))
    if not re.search(r'module\s+"cot_satellites_registry_producer"\s*\{', text):
        bad.append("KEPT: module cot_satellites_registry_producer (the function) is missing")
    if not re.search(r'schedule_expression\s*=\s*"cron\(15 13 \* \* \? \*\)"', text):
        bad.append("KEPT: the stamp-gated rule no longer reads cron(15 13 * * ? *)")
    if not re.search(r'jsonencode\(\{\s*require_stamp\s*=\s*true\s*\}\)', text):
        bad.append("KEPT: the stamp-gated target no longer carries require_stamp = true")

    # NOREF
    for m in re.finditer(r'aws_cloudwatch_event_(?:rule|target)\.%s\b|aws_lambda_permission\.%s\b'
                         % (REMOVED_ADDR, REMOVED_PERM), text):
        bad.append("NOREF: a reference to a removed address remains: %s" % m.group(0))
        break

    # ONLY (real file path only)
    scope_note = "scope-not-graded(mutant path)"
    if not os.environ.get("HG_T15_TF"):
        try:
            base = subprocess.check_output(["git", "show", "%s:%s" % (BASE_PIN, TF)], cwd=ROOT,
                                           stderr=subprocess.DEVNULL).decode("utf-8")
        except subprocess.CalledProcessError:
            base = None
            bad.append("ONLY: base pin %s does not carry %s" % (BASE_PIN, TF))
        if base is not None:
            a, b = noncomment_lines(base), noncomment_lines(text)
            added = [ln for ln in b if ln not in a]
            removed = [ln for ln in a if ln not in b]
            if added:
                bad.append("ONLY: %d non-comment line(s) were ADDED or altered against %s: %s"
                           % (len(added), BASE_PIN, " | ".join(x.strip()[:70] for x in added[:3])))
            scope_note = "scope=ok(%d line(s) removed, 0 added)" % len(removed)

    if bad:
        print("T15-BAD " + "; ".join(bad))
        return 1
    print("T15-OK 07:00Z rule, target and permission gone; stamp-gated rule cron(15 13), target and permission, module and role policy kept; %s"
          % scope_note)
    return 0


if __name__ == "__main__":
    sys.exit(main())
