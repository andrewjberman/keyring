#!/usr/bin/env python3
"""comp-denytest -- a deny-test harness that DERIVES the expected verdict from the change type.

VERIFY element of the firm-sep-DATA credential-plane program.
  PREVENT = the cross-firm belts (buckets + secrets)
  DETECT  = the prefix-wildcard lint + the sentinel lint
  VERIFY  = this harness

WHY IT EXISTS
-------------
`simulate-principal-policy` will hand you a plausible, wrong verdict in at least three
ways, and every one of them was hit live during NFRA_TERRAFORM-P2 (2026-07-08/09):

  1. WRONG CRITERION.  "Is it denied?" is not a well-formed assertion.  The correct
     success verdict INVERTS by change type:
         ADD a Deny        -> explicitDeny   (implicitDeny would mean the Deny is a no-op
                                              riding on an absent Allow: it proves nothing)
         REMOVE an Allow   -> implicitDeny   (there is no Deny statement; demanding
                                              explicitDeny FALSE-REDs a correct change)
     Group 3 added a Deny; group 4 removed an Allow.  Reusing group 3's assertion on
     group 4 would have reverted a correct security fix.  CTO mis-applied this ONE
     MESSAGE after it was banked -- which is the whole argument for deriving the verdict
     structurally instead of remembering it.  The author does not get to pick.

  2. MULTI-ARN BATCHING.  Passing several ARNs to one --resource-arns call can return a
     FALSE explicitDeny for resources that are actually allowed.  (CVO hit this: a batched
     sentinel reported catastrophic over-restriction on 27 roles that did not exist.)
     This harness refuses to batch.  One resource ARN per call, always.

  3. MISSING CONDITION CONTEXT.  An Allow carrying a Condition (e.g. StringLike on
     s3:prefix) simulates as implicitDeny unless you supply the context key it conditions
     on.  That reads as "the policy is broken" when the EXERCISE was under-specified.
     Pass --context to supply them; the harness records that you did.

USAGE
-----
  comp-denytest --change-type deny-add \
      --principal arn:aws:iam::123:role/foo --principal arn:aws:iam::123:role/bar \
      --resource  arn:aws:secretsmanager:us-east-1:123:secret:opal/bd/* \
      --action secretsmanager:GetSecretValue \
      [--discriminator arn:aws:iam::123:role/unbelted] \
      [--context s3:prefix=platinum/firm/header_metrics.json] \
      [--also-allowed arn:...:secret:opal/auth/jwt-public-key-AbCdEf]

Exit 0 = PASS.  Exit 1 = FAIL (or a mis-formed exercise, which is also a failure).

WHAT THIS DOES **NOT** GUARANTEE (read before trusting it)
----------------------------------------------------------
  * The author still picks `--change-type`.  This harness removes the choice of VERDICT,
    not the choice of CHANGE TYPE.  Declaring `allow-removal` for a Deny-add is still a
    mis-framed exercise; the harness only catches it because the live verdict disagrees
    with the derived one -- i.e. it fails LOUD instead of passing quietly.  That is a real
    improvement over remembering, but it is not impossible-by-default.
    v2 (the actual structural fix): derive `--change-type` from the `terraform plan` diff
    -- a `+ Effect = "Deny"` statement is a deny-add; a removed `Resource` line from an
    Allow is an allow-removal -- so the author declares nothing at all.
  * A PASS is a CAPABILITY proof (what IAM evaluates), never a BEHAVIOUR proof.  A consumer
    that swallows a denied read (`except -> pass` / `return None`) fails SILENT: the Lambda
    still runs, the feature dies, and a liveness check passes.  Exercise that consumer's
    OUTPUT separately.  Two live examples in this estate: the freshness monitor's
    `age_hours = None`, and portal_data_proxy's `[keyword_intelligence] Error getting
    OpenAI key` log line.
  * The `--also-allowed` set is only as complete as the caller's grounding.  A prefix that
    is used but never listed will not be checked.  Ground usage across ALL expression forms
    (literal / env / constant / SSM / DynamoDB / S3 config object / constructed f-string)
    before trusting a narrowing -- CloudTrail alone is a window, and a window misses a
    rarely-read prefix.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys

# Resolve the aws binary ONCE. On this Git-Bash/Windows host the launcher is `aws.CMD`, and
# CreateProcess cannot resolve a bare "aws" to it -- subprocess dies with WinError 2. Fail
# loudly here rather than have every simulate() return a blank that a caller might read as
# a verdict. (A blank is never a pass -- see simulate().)
AWS = shutil.which("aws") or shutil.which("aws.cmd")
if not AWS:
    sys.exit("comp-denytest: cannot locate the `aws` executable on PATH.")

# The whole point: this mapping is code, not a habit.
EXPECTED = {
    "deny-add": "explicitDeny",
    "allow-removal": "implicitDeny",
}
# A wildcard narrow is BOTH: the dropped prefixes fall to implicitDeny, the kept ones stay
# allowed.  It cannot be reduced to a single verdict, so we force the caller to say which.
NEEDS_ALLOWLIST = {"wildcard-narrow"}


def simulate(principal: str, resource: str, action: str, context: list[str]) -> str:
    """One principal, ONE resource, one action.  Never batch -- see reason (2)."""
    cmd = [
        AWS, "iam", "simulate-principal-policy",
        "--policy-source-arn", principal,
        "--action-names", action,
        "--resource-arns", resource,          # exactly one, by construction
        "--query", "EvaluationResults[].EvalDecision",
        "--output", "text",
    ]
    for kv in context:
        key, _, val = kv.partition("=")
        cmd += ["--context-entries",
                f"ContextKeyName={key},ContextKeyValues={val},ContextKeyType=string"]
    out = subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL)
    verdict = out.stdout.strip().replace("\r", "")
    if not verdict:
        # A blank is NOT a pass.  It means the call failed or returned nothing.
        return f"<NO VERDICT: rc={out.returncode} err={out.stderr.strip()[:80]}>"
    return verdict


def main() -> int:
    p = argparse.ArgumentParser(prog="comp-denytest")
    p.add_argument("--change-type", required=True,
                   choices=sorted(set(EXPECTED) | NEEDS_ALLOWLIST))
    p.add_argument("--principal", action="append", required=True,
                   help="repeatable; the roles the change was applied to")
    p.add_argument("--resource", action="append", required=True,
                   help="repeatable; each is simulated in its OWN call")
    p.add_argument("--action", action="append", required=True)
    p.add_argument("--context", action="append", default=[],
                   help="ContextKey=value, for condition-scoped grants (reason 3)")
    p.add_argument("--discriminator", action="append", default=[],
                   help="a principal the change was NOT applied to; must NOT show the "
                        "expected verdict -- proves the change is the deciding control")
    p.add_argument("--also-allowed", action="append", default=[],
                   help="resource ARNs that must remain 'allowed' (no collateral deny)")
    a = p.parse_args()

    if a.change_type in NEEDS_ALLOWLIST:
        print("FAIL: --change-type wildcard-narrow cannot be reduced to one verdict.\n"
              "      Run it as TWO exercises: the dropped prefixes as 'allow-removal',\n"
              "      and the kept prefixes via --also-allowed.", file=sys.stderr)
        return 1

    expected = EXPECTED[a.change_type]
    print(f"change-type = {a.change_type}  ->  DERIVED expected verdict = {expected}")
    print("(the author does not choose this; it is derived from the change type)\n")
    if a.context:
        print(f"condition context supplied: {a.context}\n")

    failures: list[str] = []

    print("=== the change's own principals: every (principal x resource x action) ===")
    for pr in a.principal:
        for rs in a.resource:
            for ac in a.action:
                v = simulate(pr, rs, ac, a.context)
                ok = v == expected
                if not ok:
                    failures.append(f"{pr.split('/')[-1]} {ac} {rs.split(':secret:')[-1]} -> {v} (want {expected})")
                print(f"  [{'PASS' if ok else 'FAIL'}] {pr.split('/')[-1]:<32} {ac:<30} -> {v}")

    if a.discriminator:
        print("\n=== discriminator: unchanged principals must NOT show the expected verdict ===")
        print("    (otherwise the verdict proves default-deny, not YOUR change)")
        for pr in a.discriminator:
            for rs in a.resource:
                v = simulate(pr, rs, a.action[0], a.context)
                ok = v != expected
                if not ok:
                    failures.append(f"DISCRIMINATOR {pr.split('/')[-1]} -> {v}; the verdict is not attributable to the change")
                print(f"  [{'PASS' if ok else 'FAIL'}] {pr.split('/')[-1]:<32} -> {v} (must differ from {expected})")

    if a.also_allowed:
        print("\n=== no collateral deny: these must remain 'allowed' ===")
        for pr in a.principal:
            for rs in a.also_allowed:
                v = simulate(pr, rs, a.action[0], a.context)
                ok = v == "allowed"
                if not ok:
                    failures.append(f"COLLATERAL {pr.split('/')[-1]} lost {rs.split(':secret:')[-1]} -> {v}")
                print(f"  [{'PASS' if ok else 'FAIL'}] {pr.split('/')[-1]:<32} {rs.split(':secret:')[-1][:34]:<34} -> {v}")

    print()
    if failures:
        print(f"RESULT: FAIL ({len(failures)})")
        for f in failures:
            print(f"  !! {f}")
        return 1
    print("RESULT: PASS")
    print("  NOTE: a PASS here is a CAPABILITY proof (IAM evaluation), not a BEHAVIOUR proof.")
    print("  If any consumer swallows a denied read (except -> pass/return None), it fails SILENT:")
    print("  a liveness check will pass while the feature dies. Exercise that consumer's OUTPUT.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
