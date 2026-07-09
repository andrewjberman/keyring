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
import json
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



# ---------------------------------------------------------------------------
# v2: DERIVE the change type from the terraform plan, so the author declares nothing.
#
# v1 removed the author's choice of VERDICT. It did not remove the choice of CHANGE TYPE:
# declaring `allow-removal` for a deny-add still mis-framed the test, and only failed
# because the live verdict disagreed. That is fail-loud, not impossible-by-default.
# Here the tool reads the change AND the criterion off the plan itself.
#
#   Produce the input with:  terraform show -json <planfile> > plan.json
# ---------------------------------------------------------------------------
POLICY_TYPES = {"aws_iam_role_policy", "aws_iam_policy", "aws_iam_role_policy_attachment"}
REAL_ACTIONS = {"create", "update", "delete"}


def _doc(blob):
    """A policy attribute that is not a policy document must not crash the derivation."""
    if not blob:
        return None
    try:
        d = json.loads(blob)
    except (TypeError, ValueError):
        return None
    return d if isinstance(d, dict) and "Statement" in d else None


def _stmts(doc):
    if not doc:
        return []
    s = doc["Statement"]
    return s if isinstance(s, list) else [s]


def _res(stmt):
    r = stmt.get("Resource") or []
    return set([r] if isinstance(r, str) else r)


def _key(stmt):
    return (stmt.get("Sid"), stmt.get("Effect"), json.dumps(stmt.get("Action"), sort_keys=True))


def derive_from_plan(path: str):
    """Return (change_type, principals, evidence). Refuses to guess."""
    with open(path, encoding="utf-8") as fh:
        plan = json.load(fh)          # parse-assert: a truncated plan cannot parse
    found, evidence = [], []
    for rc in plan.get("resource_changes", []):
        if rc.get("type") not in POLICY_TYPES:
            continue
        ch = rc.get("change", {})
        acts = set(ch.get("actions", []))
        if not (acts & REAL_ACTIONS):
            continue                   # no-op / read: not a change

        # v3: a managed-policy DETACH removes every Allow that policy carried. The document is
        # not in the plan (it is AWS-managed and lives outside our Terraform -- which is the whole
        # reason SecretsManagerReadWrite was invisible to a grant-shape lint), so classify it by
        # the resource type + action, not by diffing a document we cannot see.
        if rc["type"] == "aws_iam_role_policy_attachment":
            if "delete" in acts:
                b = ch.get("before") or {}
                found.append("allow-removal")
                evidence.append(f"{rc['address']}: DETACH {b.get('policy_arn')} "
                                f"from role {b.get('role')}")
            continue

        # A whole role-policy deleted (not shrunk) is likewise an Allow-removal.
        if "delete" in acts and not ch.get("after"):
            b = _doc((ch.get("before") or {}).get("policy"))
            if any(s.get("Effect") == "Allow" for s in _stmts(b)):
                found.append("allow-removal")
                evidence.append(f"{rc['address']}: role-policy DELETED (carried Allow statements)")
            continue

        before = _doc((ch.get("before") or {}).get("policy"))
        after = _doc((ch.get("after") or {}).get("policy"))
        role = (ch.get("after") or ch.get("before") or {}).get("role")

        b_by, a_by = {_key(s): s for s in _stmts(before)}, {_key(s): s for s in _stmts(after)}
        added_deny = [s for k, s in a_by.items() if k not in b_by and s.get("Effect") == "Deny"]
        shrunk_allow = [
            (b_by[k], s) for k, s in a_by.items()
            if k in b_by and s.get("Effect") == "Allow" and _res(b_by[k]) - _res(s)
        ]
        narrowed = [
            (b_by[k], s) for b, s in shrunk_allow for k in [_key(s)]
            if any("*" in x.rsplit(":", 1)[-1] for x in _res(b_by[k]) - _res(s)) and _res(s)
        ]

        if added_deny:
            found.append("deny-add")
            evidence.append(f"{rc['address']}: + Deny stmt Sid={added_deny[0].get('Sid')} "
                            f"Resource={sorted(_res(added_deny[0]))}")
        elif narrowed:
            found.append("wildcard-narrow")
            evidence.append(f"{rc['address']}: Allow wildcard replaced by an allowlist")
        elif shrunk_allow:
            b, a = shrunk_allow[0]
            found.append("allow-removal")
            evidence.append(f"{rc['address']}: - Resource {sorted(_res(b) - _res(a))} from Allow "
                            f"Sid={a.get('Sid')}")
        else:
            continue
        if role:
            evidence.append(f"    role -> {role}")
    kinds = set(found)
    if not kinds:
        raise SystemExit("comp-denytest --from-plan: no IAM policy change found in the plan. "
                         "Nothing to verify; refusing to guess a change type.")
    if len(kinds) > 1:
        raise SystemExit(f"comp-denytest --from-plan: plan mixes change types {sorted(kinds)}. "
                         "Split it; one exercise cannot carry two criteria.")
    return kinds.pop(), evidence


def main() -> int:
    p = argparse.ArgumentParser(prog="comp-denytest")
    p.add_argument("--change-type", choices=sorted(set(EXPECTED) | NEEDS_ALLOWLIST),
                   help="v1 mode. Prefer --from-plan, which derives this so you cannot mis-declare it.")
    p.add_argument("--from-plan", metavar="PLAN_JSON",
                   help="v2: derive --change-type from `terraform show -json <planfile>`")
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
                   help="'ARN' or 'ARN|ACTION' -- must remain 'allowed' (no collateral deny). STATE the "
                        "action: on a write-removal, inheriting --action[0] asserts the role can still "
                        "WRITE a secret it only READs, which false-FAILs a correct change.")
    p.add_argument("--precheck", metavar="BASELINE_JSON",
                   help="run BEFORE apply: assert each principal is CURRENTLY 'allowed' on each "
                        "(action, resource) and write the baseline here. An allow-removal that was "
                        "never allowed proves nothing.")
    p.add_argument("--baseline", metavar="BASELINE_JSON",
                   help="the file written by --precheck. REQUIRED for an allow-removal: without it "
                        "a post-apply implicitDeny may be vacuous (the principal never had reach).")
    a = p.parse_args()

    if a.from_plan:
        derived, evidence = derive_from_plan(a.from_plan)
        if a.change_type and a.change_type != derived:
            print(
                f"FAIL: you declared --change-type {a.change_type}, but the plan says "
                f"{derived}. The plan wins -- this is exactly the mis-declaration that v1 "
                f"could only catch after the fact, never prevent.",
                file=sys.stderr,
            )
            return 1
        a.change_type = derived
        print("=== change type DERIVED FROM THE PLAN (the author declared nothing) ===")
        for e in evidence:
            print(f"  {e}")
        print()
    if not a.change_type:
        print("FAIL: supply --from-plan (preferred) or --change-type.", file=sys.stderr)
        return 1

    if a.change_type in NEEDS_ALLOWLIST:
        print("FAIL: --change-type wildcard-narrow cannot be reduced to one verdict.\n"
              "      Run it as TWO exercises: the dropped prefixes as 'allow-removal',\n"
              "      and the kept prefixes via --also-allowed.", file=sys.stderr)
        return 1

    # --- non-vacuity: an implicitDeny only proves something if reach EXISTED beforehand. ---
    if a.precheck:
        base, bad = {}, []
        for pr in a.principal:
            for res in a.resource:
                for act in a.action:
                    v = simulate(pr, res, act, a.context)
                    base[f"{pr}|{res}|{act}"] = v
                    print(f"  PRECHECK {pr} {act} {res.rsplit(':', 1)[-1]} -> {v}")
                    if v != "allowed":
                        bad.append(f"{pr} is '{v}' (not 'allowed') on {act} {res}")
        with open(a.precheck, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"baseline": base}, fh, indent=1)
        if bad:
            print("\nFAIL: precheck -- these were not 'allowed' BEFORE the change, so removing an "
                  "Allow cannot be proven by a post-apply implicitDeny:", file=sys.stderr)
            for b in bad:
                print(f"  !! {b}", file=sys.stderr)
            return 1
        print(f"\nPRECHECK PASS: reach exists today; baseline -> {a.precheck}")
        print("  Now apply, then re-run with --baseline to prove the reach is gone.")
        return 0

    if a.change_type == "allow-removal":
        if not a.baseline:
            print("FAIL: an allow-removal REQUIRES --baseline (written by a pre-apply --precheck).\n"
                  "      Without it, 'implicitDeny' is unfalsifiable: a principal that never had\n"
                  "      reach yields the same verdict as one whose reach you just removed.\n"
                  "      Proving a negative requires showing the positive existed.", file=sys.stderr)
            return 1
        try:
            base = json.load(open(a.baseline, encoding="utf-8"))["baseline"]
        except Exception as e:
            print(f"FAIL: cannot read baseline {a.baseline}: {e}", file=sys.stderr)
            return 1
        missing = [f"{pr}|{res}|{act}" for pr in a.principal for res in a.resource
                   for act in a.action if base.get(f"{pr}|{res}|{act}") != "allowed"]
        if missing:
            print("FAIL: the baseline does not record 'allowed' for every (principal, resource, "
                  "action) under test -- it does not cover this exercise:", file=sys.stderr)
            for m in missing:
                print(f"  !! no pre-apply 'allowed' for {m}", file=sys.stderr)
            return 1
        print(f"=== baseline: reach was 'allowed' pre-apply for all "
              f"{len(a.principal) * len(a.resource) * len(a.action)} combination(s). "
              f"An implicitDeny now is a real removal.\n")

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
        # v3.1: each entry is `ARN` or `ARN|ACTION`. Reusing --action[0] here is a TRAP: on a
        # write-removal the tested action is PutSecretValue, so the collateral check would assert
        # a role can still WRITE the secret it is only supposed to READ -- a guaranteed false FAIL
        # (and, on a read-removal, a possible false PASS). The action a collateral check cares about
        # is the one the consumer actually performs, so it must be stated, not inherited.
        # v3.2 (CVO): do not merely default -- REFUSE. On an allow-removal the inherited action IS
        # the action being removed, so a collateral check against it is definitionally wrong: it
        # false-FAILS a correct change (visible), and on a read-removal it false-PASSES (silent --
        # it ships the hole). The tool cannot guess which action the consumer performs.
        bare = [e for e in a.also_allowed if "|" not in e]
        if bare and a.change_type == "allow-removal":
            print("FAIL: --also-allowed needs an explicit ACTION on an allow-removal.\n"
                  f"      These inherited --action[0] ({a.action[0]}) -- which is the action being\n"
                  f"      REMOVED, so the check is meaningless: {bare}\n"
                  "      Pass 'ARN|ACTION' naming the action the CONSUMER actually performs\n"
                  "      (e.g. 'arn:...:secret:foo-??????|secretsmanager:GetSecretValue').",
                  file=sys.stderr)
            return 1

        print("\n=== no collateral deny: these must remain 'allowed' ===")
        for pr in a.principal:
            for entry in a.also_allowed:
                rs, _, act = entry.partition("|")
                act = act or a.action[0]
                v = simulate(pr, rs, act, a.context)
                ok = v == "allowed"
                if not ok:
                    failures.append(f"COLLATERAL {pr.split('/')[-1]} lost {act} on "
                                    f"{rs.split(':secret:')[-1]} -> {v}"
                                    + ("   (no ACTION given -- it inherited --action[0]; "
                                       "pass 'ARN|ACTION' if you meant a different one)"
                                       if not entry.partition('|')[2] else ""))
                print(f"  [{'PASS' if ok else 'FAIL'}] {pr.split('/')[-1]:<30} {act:<30} "
                      f"{rs.split(':secret:')[-1][:30]:<30} -> {v}")

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
