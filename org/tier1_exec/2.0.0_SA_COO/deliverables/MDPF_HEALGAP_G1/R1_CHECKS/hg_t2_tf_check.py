"""MDPF_HEALGAP round 1, criterion HG1-t2-AC1: the re-attempt is declared in Terraform as a second target on
the existing `cot-bronze-complete` rule, invoking the runner with {"mode": "pull"}, with the invoke
permission scoped to that rule, and the file is `terraform fmt` clean.

Static read of infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf (no init, no plan, no AWS).
Last line: TF-OK or TF-BAD <reason>.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys

TF = os.path.join("infra", "aws", "terraform", "opal-assets", "cot_rebalancer_reattempt.tf")


def _blocks(text: str, rtype: str) -> list[str]:
    out = []
    for m in re.finditer(rf'resource\s+"{re.escape(rtype)}"\s+"[^"]+"\s*\{{', text):
        depth, i = 1, m.end()
        while i < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        out.append(text[m.start():i])
    return out


def main() -> int:
    if not os.path.isfile(TF):
        print("TF-BAD no file " + TF)
        return 1
    with open(TF, encoding="utf-8") as fh:
        text = fh.read()
    targets = [b for b in _blocks(text, "aws_cloudwatch_event_target")
               if re.search(r'rule\s*=\s*"cot-bronze-complete"', b)
               and re.search(r'arn\s*=\s*module\.cot_rebalancer_runner\.function_arn', b)
               and re.search(r'mode\s*=\s*"pull"', b)]
    if len(targets) != 1:
        print(f"TF-BAD event_target matching rule/arn/input: {len(targets)} (want 1)")
        return 1
    # The permission's source_arn names the rule either literally or through the target's own `rule` attribute
    # (issuer amendment 1: one literal in the file, so the R20 waiver covers exactly one occurrence).
    tname = re.match(r'resource\s+"aws_cloudwatch_event_target"\s+"([^"]+)"', targets[0]).group(1)
    scoped = (r'source_arn\s*=.*rule/(cot-bronze-complete|\$\{aws_cloudwatch_event_target\.'
              + re.escape(tname) + r'\.rule\})"')
    perms = [b for b in _blocks(text, "aws_lambda_permission")
             if re.search(r'function_name\s*=\s*module\.cot_rebalancer_runner\.function_name', b)
             and re.search(r'principal\s*=\s*"events\.amazonaws\.com"', b)
             and re.search(scoped, b)]
    if len(perms) != 1:
        print(f"TF-BAD lambda_permission scoped to rule/cot-bronze-complete: {len(perms)} (want 1)")
        return 1
    tf = shutil.which("terraform")
    if not tf:
        print("TF-BAD terraform not on PATH")
        return 1
    env = dict(os.environ, CHECKPOINT_DISABLE="1")  # no vendor checkpoint call (laptop 1.0.0_SA_CTO msg 106231)
    r = subprocess.run([tf, "fmt", "-check", "-diff", TF], capture_output=True, text=True, timeout=60, check=False, env=env)
    if r.returncode != 0:
        print(r.stdout[-1500:] + r.stderr[-500:])
        print("TF-BAD fmt rc=" + str(r.returncode))
        return 1
    print("TF-OK targets=1 permissions=1 fmt=clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
