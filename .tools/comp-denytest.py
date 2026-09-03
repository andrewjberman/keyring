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

Exit 0 = complete PASS/correct non-positive plan state.  Exit 1 = complete FAIL or a
mis-formed exercise.  Exit 2 = NOT-DECIDABLE (budget expiry, unreadable simulation,
or conditioned implicitDeny); it is distinct from both verdicts.

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
import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import _compbudget

# Resolve the aws binary ONCE. On this Git-Bash/Windows host the launcher is `aws.CMD`, and
# CreateProcess cannot resolve a bare "aws" to it -- subprocess dies with WinError 2. Resolve
# once, but defer absence to simulate() so --help and the offline self-test remain usable. An
# absent binary becomes an unreadable result at rc=2, never a blank or a verdict.
AWS = shutil.which("aws") or shutil.which("aws.cmd")

# The whole point: this mapping is code, not a habit.
EXPECTED = {
    "deny-add": "explicitDeny",
    "allow-removal": "implicitDeny",
}
# A wildcard narrow is BOTH: the dropped prefixes fall to implicitDeny, the kept ones stay
# allowed.  It cannot be reduced to a single verdict, so we force the caller to say which.
NEEDS_ALLOWLIST = {"wildcard-narrow"}

RC_CLEAN = 0
RC_FAIL = 1
RC_NOT_DECIDABLE = 2

STATE_SUBJECT_ABSENT = "SUBJECT_ABSENT_FROM_CORPUS"
STATE_PRESENT_ZERO = "PRESENT_WITH_ZERO_RESULTS"
STATE_PARTIAL_OR_BLIND = "PARTIAL_OR_BLIND"
STATE_NOT_APPLICABLE = "NOT_APPLICABLE"
STATE_NOT_DECIDABLE = "NOT-DECIDABLE"


@dataclass(frozen=True)
class SimulationOutcome:
    """One isolated IAM simulation result; an unreadable call is never a verdict."""

    decision: str | None = None
    missing_context: tuple[str, ...] = ()
    error: str | None = None
    budget_reached: bool = False


class PlanAnswerState(Exception):
    """A correct non-positive answer derived from the fixture/plan itself."""

    def __init__(self, state: str, message: str):
        super().__init__(message)
        self.state = state
        self.message = message


def simulate(principal: str, resource: str, action: str, context: list[str],
             timeout_s: float | None = None) -> SimulationOutcome:
    """One principal, ONE resource, one action. Never batch; return no false verdict."""
    if not AWS:
        return SimulationOutcome(error="cannot locate the `aws` executable on PATH")
    if timeout_s is not None and timeout_s <= 0:
        return SimulationOutcome(error="budget exhausted before the call started",
                                 budget_reached=True)
    cmd = [
        AWS, "iam", "simulate-principal-policy",
        "--policy-source-arn", principal,
        "--action-names", action,
        "--resource-arns", resource,          # exactly one, by construction
        "--output", "json",
    ]
    for kv in context:
        key, _, val = kv.partition("=")
        cmd += ["--context-entries",
                f"ContextKeyName={key},ContextKeyValues={val},ContextKeyType=string"]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL,
                             timeout=timeout_s)
    except subprocess.TimeoutExpired:
        return SimulationOutcome(
            error="simulate-principal-policy exceeded the remaining Rule T budget",
            budget_reached=True,
        )
    if out.returncode != 0:
        return SimulationOutcome(
            error=f"aws rc={out.returncode}: {out.stderr.strip()[:160] or 'no stderr'}")
    try:
        payload = json.loads(out.stdout)
        rows = payload.get("EvaluationResults") or []
        if len(rows) != 1:
            raise ValueError(f"expected one EvaluationResults row, got {len(rows)}")
        row = rows[0]
        verdict = row.get("EvalDecision")
        if verdict not in {"allowed", "implicitDeny", "explicitDeny"}:
            raise ValueError(f"unrecognized EvalDecision {verdict!r}")
        missing = tuple(
            m.get("ContextKeyName", str(m)) if isinstance(m, dict) else str(m)
            for m in (row.get("MissingContextValues") or [])
        )
    except (AttributeError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return SimulationOutcome(error=f"unreadable simulation response: {exc}")
    return SimulationOutcome(decision=verdict, missing_context=missing)



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
    policy_subjects = 0
    changed_policy_subjects = 0
    for rc in plan.get("resource_changes", []):
        if rc.get("type") not in POLICY_TYPES:
            continue
        policy_subjects += 1
        ch = rc.get("change", {})
        acts = set(ch.get("actions", []))
        if not (acts & REAL_ACTIONS):
            continue                   # no-op / read: not a change
        changed_policy_subjects += 1

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
        if policy_subjects == 0:
            raise PlanAnswerState(
                STATE_SUBJECT_ABSENT,
                "the plan contains no IAM policy subject in comp-denytest's corpus; "
                "no principal/resource can be derived",
            )
        if changed_policy_subjects == 0:
            raise PlanAnswerState(
                STATE_PRESENT_ZERO,
                f"the plan contains {policy_subjects} IAM policy subject(s), but zero deny-add / "
                "allow-removal changes; zero population without an IAM change is CORRECT",
            )
        raise PlanAnswerState(
            STATE_NOT_APPLICABLE,
            f"the plan changes {changed_policy_subjects} IAM policy subject(s), but the change "
            "type is not deny-add or allow-removal; this deny-test does not apply",
        )
    if len(kinds) > 1:
        raise SystemExit(f"comp-denytest --from-plan: plan mixes change types {sorted(kinds)}. "
                         "Split it; one exercise cannot carry two criteria.")
    return kinds.pop(), evidence


def _print_answer_state(state: str, message: str) -> None:
    print(f"ANSWER-STATE: {state}")
    print(f"  {message}")


def _policy_change(address: str, actions: list[str], before: list[dict],
                   after: list[dict]) -> dict:
    """A minimal terraform-show shaped fixture row for the offline self-test."""
    def doc(rows):
        return json.dumps({"Version": "2012-10-17", "Statement": rows})

    return {
        "type": "aws_iam_role_policy",
        "address": address,
        "change": {
            "actions": actions,
            "before": {"role": "fixture-role", "policy": doc(before)},
            "after": {"role": "fixture-role", "policy": doc(after)},
        },
    }


def _offline_answer_state_self_test() -> int:
    """Four planted answer-state cases, one invocation, fixtures/stub only; zero live IAM."""
    deny_one = {"Sid": "D", "Effect": "Deny", "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::fixture/denied"}
    allow_added = {"Sid": "A2", "Effect": "Allow", "Action": "s3:ListBucket",
                   "Resource": "arn:aws:s3:::fixture"}

    def conditioned_stub(_principal, _resource, _action, _context, timeout_s=None):
        del timeout_s
        return SimulationOutcome(decision="implicitDeny", missing_context=("aws:SourceVpc",))

    with tempfile.TemporaryDirectory(prefix="comp-denytest-offline-") as td:
        root = Path(td)
        fixtures = {
            STATE_SUBJECT_ABSENT: {"resource_changes": [{
                "type": "aws_s3_bucket", "address": "aws_s3_bucket.fixture",
                "change": {"actions": ["update"]},
            }]},
            STATE_PRESENT_ZERO: {"resource_changes": [
                _policy_change("aws_iam_role_policy.zero", ["no-op"], [], [])]},
            STATE_NOT_APPLICABLE: {"resource_changes": [
                _policy_change("aws_iam_role_policy.allow_add", ["update"], [], [allow_added])]},
            STATE_PARTIAL_OR_BLIND: {"resource_changes": [
                _policy_change("aws_iam_role_policy.deny_add", ["update"], [], [deny_one])]},
        }
        paths = {}
        for state, payload in fixtures.items():
            path = root / f"{state}.plan.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            paths[state] = path

        common = ["--principal", "arn:aws:iam::123:role/fixture-role",
                  "--resource", "arn:aws:s3:::fixture/denied", "--action", "s3:GetObject"]
        cases = [
            (STATE_SUBJECT_ABSENT, ["--from-plan", str(paths[STATE_SUBJECT_ABSENT])] + common, None, RC_CLEAN),
            (STATE_PRESENT_ZERO, ["--from-plan", str(paths[STATE_PRESENT_ZERO])] + common, None, RC_CLEAN),
            (STATE_NOT_APPLICABLE, ["--from-plan", str(paths[STATE_NOT_APPLICABLE])] + common, None, RC_CLEAN),
            (STATE_PARTIAL_OR_BLIND, ["--from-plan", str(paths[STATE_PARTIAL_OR_BLIND])] + common,
             conditioned_stub, RC_NOT_DECIDABLE),
        ]
        passed = 0
        for expected_state, argv, stub, expected_rc in cases:
            capture = io.StringIO()
            with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
                rc = main(argv, simulate_fn=stub)
            body = capture.getvalue().rstrip()
            token_ok = body.count(f"ANSWER-STATE: {expected_state}") == 1
            ok = token_ok and rc == expected_rc
            passed += int(ok)
            print(f"=== OFFLINE CASE {expected_state} (rc={rc}) ===")
            print(body)
            print(f"CASE-CHECK: {'PASS' if ok else 'FAIL'}\n")
    print(f"OFFLINE ANSWER-STATE SELF-TEST: {passed}/4 PASS; ZERO live IAM calls")
    return RC_CLEAN if passed == 4 else RC_FAIL


def main(argv: list[str] | None = None, simulate_fn=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv == ["--offline-self-test"]:
        return _offline_answer_state_self_test()

    p = argparse.ArgumentParser(
        prog="comp-denytest",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "RC VOCABULARY (VERDICT-BEARING, NFRA_COMPEFFICACY PRD v0.5 s.4.4 / FWD-10):\n"
            "  0  clean -- complete passing verdict, or a correct non-positive plan state\n"
            "  1  fail  -- complete failing verdict or malformed exercise\n"
            "  2  NOT-DECIDABLE -- PARTIAL_OR_BLIND: budget expiry, unreadable simulation,\n"
            "       or conditioned implicitDeny; distinct from both clean and fail\n"
            "Rule T carrier: --budget > env COMP_BUDGET_S > default 90 s. Every\n"
            "simulate-principal-policy subprocess receives the remaining budget as timeout=.\n"
            "NON-APPLICATION: this tool has no corpus-width loop or safe partial-verdict cursor;\n"
            "an incomplete explicit tuple is rerun whole with a larger budget, never graded.\n"
            "Offline audit: --offline-self-test plants all four answer states with fixture plans\n"
            "and a conditioned-grant stub in ONE invocation; it makes ZERO live IAM calls."
        ),
    )
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
    p.add_argument("--budget", metavar="N", default=None,
                   help="RULE T: seconds available to the explicit simulation tuple; carrier "
                        "--budget > env COMP_BUDGET_S > default 90 s; 0 = unbounded")
    a = p.parse_args(argv)
    simulator = simulate_fn or simulate

    try:
        budget_s, budget_source = _compbudget.resolve_budget(a.budget)
    except ValueError as exc:
        print(f"FAIL: --budget {exc}", file=sys.stderr)
        return RC_FAIL
    clock = _compbudget.Clock(budget_s)
    print(_compbudget.disclosure_line(budget_s, budget_source))

    if a.from_plan:
        try:
            derived, evidence = derive_from_plan(a.from_plan)
        except PlanAnswerState as state:
            _print_answer_state(state.state, state.message)
            print("NON-APPLICATION: no eligible simulate subprocess and no work loop ran.")
            print(_compbudget.within_budget_line(0, 0, "simulate_call", budget_s,
                                                 budget_source, round(clock.elapsed(), 3)))
            for line in _compbudget.deferred_bucket(0, 0, "simulate_call", []):
                print(line)
            return RC_CLEAN
        if a.change_type and a.change_type != derived:
            print(
                f"FAIL: you declared --change-type {a.change_type}, but the plan says "
                f"{derived}. The plan wins -- this is exactly the mis-declaration that v1 "
                f"could only catch after the fact, never prevent.",
                file=sys.stderr,
            )
            return RC_FAIL
        a.change_type = derived
        print("=== change type DERIVED FROM THE PLAN (the author declared nothing) ===")
        for e in evidence:
            print(f"  {e}")
        print()
    if not a.change_type:
        print("FAIL: supply --from-plan (preferred) or --change-type.", file=sys.stderr)
        return RC_FAIL

    if a.change_type in NEEDS_ALLOWLIST:
        _print_answer_state(
            STATE_NOT_APPLICABLE,
            "wildcard-narrow cannot be reduced to one verdict; run the dropped prefixes as "
            "allow-removal and the kept prefixes via --also-allowed",
        )
        print("NON-APPLICATION: no eligible simulate subprocess and no work loop ran.")
        return RC_CLEAN

    own_total = len(a.principal) * len(a.resource) * len(a.action)
    total_calls = own_total if a.precheck else (
        own_total + len(a.discriminator) * len(a.resource)
        + len(a.principal) * len(a.also_allowed)
    )
    completed_calls = 0

    def run_sim(principal: str, resource: str, action: str) -> SimulationOutcome:
        nonlocal completed_calls
        remaining = clock.remaining()
        outcome = simulator(principal, resource, action, a.context, timeout_s=remaining)
        if outcome.decision is not None and not outcome.missing_context and not outcome.error:
            completed_calls += 1
        return outcome

    def stop_if_not_decidable(outcome: SimulationOutcome, label: str) -> int | None:
        if not (outcome.error or outcome.missing_context):
            return None
        if outcome.budget_reached:
            print(f"BUDGET REACHED: {_compbudget.fmt(budget_s)} s ({budget_source}); scanned "
                  f"{completed_calls} of {total_calls} simulate_call; results are a PREFIX, not "
                  "the answer; resume: rerun the full explicit tuple with a larger --budget "
                  "(no safe cursor -- this verdict requires every declared call).")
        elif outcome.missing_context:
            print("CONDITIONED-UNEVALUATED: implicitDeny with missingContextValues="
                  f"{list(outcome.missing_context)} is byte-identical to a real deny; it is "
                  "not a verdict. Supply every required --context value.")
        else:
            print(f"SIMULATION UNREADABLE: {outcome.error}; this is not a verdict.")
        reason = outcome.error or (
            f"conditioned result missing context {list(outcome.missing_context)}")
        for line in _compbudget.deferred_bucket(1, total_calls, "simulate_call",
                                                [f"{label}: {reason}"]):
            print(line)
        _print_answer_state(STATE_PARTIAL_OR_BLIND,
                            "the simulation plane did not return a complete readable verdict")
        print(f"STATE: {STATE_NOT_DECIDABLE} (rc={RC_NOT_DECIDABLE}, distinct from clean "
              f"rc={RC_CLEAN} and failing rc={RC_FAIL})")
        return RC_NOT_DECIDABLE

    def print_completed_budget() -> None:
        print(_compbudget.within_budget_line(completed_calls, total_calls, "simulate_call",
                                             budget_s, budget_source, round(clock.elapsed(), 3)))
        for line in _compbudget.deferred_bucket(0, total_calls, "simulate_call", []):
            print(line)

    # --- non-vacuity: an implicitDeny only proves something if reach EXISTED beforehand. ---
    if a.precheck:
        base, bad = {}, []
        for pr in a.principal:
            for res in a.resource:
                for act in a.action:
                    outcome = run_sim(pr, res, act)
                    stopped = stop_if_not_decidable(outcome, f"{pr}|{res}|{act}")
                    if stopped is not None:
                        return stopped
                    verdict = outcome.decision
                    base[f"{pr}|{res}|{act}"] = verdict
                    print(f"  PRECHECK {pr} {act} {res.rsplit(':', 1)[-1]} -> {verdict}")
                    if verdict != "allowed":
                        bad.append(f"{pr} is '{verdict}' (not 'allowed') on {act} {res}")
        with open(a.precheck, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"baseline": base}, fh, indent=1)
        print_completed_budget()
        if bad:
            print("\nFAIL: precheck -- these were not 'allowed' BEFORE the change, so removing an "
                  "Allow cannot be proven by a post-apply implicitDeny:", file=sys.stderr)
            for b in bad:
                print(f"  !! {b}", file=sys.stderr)
            return RC_FAIL
        print(f"\nPRECHECK PASS: reach exists today; baseline -> {a.precheck}")
        print("  Now apply, then re-run with --baseline to prove the reach is gone.")
        return RC_CLEAN

    if a.change_type == "allow-removal":
        if not a.baseline:
            print("FAIL: an allow-removal REQUIRES --baseline (written by a pre-apply --precheck).\n"
                  "      Without it, 'implicitDeny' is unfalsifiable: a principal that never had\n"
                  "      reach yields the same verdict as one whose reach you just removed.\n"
                  "      Proving a negative requires showing the positive existed.", file=sys.stderr)
            return RC_FAIL
        try:
            base = json.load(open(a.baseline, encoding="utf-8"))["baseline"]
        except Exception as exc:
            print(f"FAIL: cannot read baseline {a.baseline}: {exc}", file=sys.stderr)
            return RC_FAIL
        missing = [f"{pr}|{res}|{act}" for pr in a.principal for res in a.resource
                   for act in a.action if base.get(f"{pr}|{res}|{act}") != "allowed"]
        if missing:
            print("FAIL: the baseline does not record 'allowed' for every (principal, resource, "
                  "action) under test -- it does not cover this exercise:", file=sys.stderr)
            for m in missing:
                print(f"  !! no pre-apply 'allowed' for {m}", file=sys.stderr)
            return RC_FAIL
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
                outcome = run_sim(pr, rs, ac)
                stopped = stop_if_not_decidable(outcome, f"{pr}|{rs}|{ac}")
                if stopped is not None:
                    return stopped
                verdict = outcome.decision
                ok = verdict == expected
                if not ok:
                    failures.append(f"{pr.split('/')[-1]} {ac} {rs.split(':secret:')[-1]} -> "
                                    f"{verdict} (want {expected})")
                print(f"  [{'PASS' if ok else 'FAIL'}] {pr.split('/')[-1]:<32} {ac:<30} -> {verdict}")

    if a.discriminator:
        print("\n=== discriminator: unchanged principals must NOT show the expected verdict ===")
        print("    (otherwise the verdict proves default-deny, not YOUR change)")
        for pr in a.discriminator:
            for rs in a.resource:
                outcome = run_sim(pr, rs, a.action[0])
                stopped = stop_if_not_decidable(outcome, f"discriminator:{pr}|{rs}|{a.action[0]}")
                if stopped is not None:
                    return stopped
                verdict = outcome.decision
                ok = verdict != expected
                if not ok:
                    failures.append(f"DISCRIMINATOR {pr.split('/')[-1]} -> {verdict}; "
                                    "the verdict is not attributable to the change")
                print(f"  [{'PASS' if ok else 'FAIL'}] {pr.split('/')[-1]:<32} -> {verdict} "
                      f"(must differ from {expected})")

    if a.also_allowed:
        bare = [e for e in a.also_allowed if "|" not in e]
        if bare and a.change_type == "allow-removal":
            print("FAIL: --also-allowed needs an explicit ACTION on an allow-removal.\n"
                  f"      These inherited --action[0] ({a.action[0]}) -- which is the action being\n"
                  f"      REMOVED, so the check is meaningless: {bare}\n"
                  "      Pass 'ARN|ACTION' naming the action the CONSUMER actually performs\n"
                  "      (e.g. 'arn:...:secret:foo-??????|secretsmanager:GetSecretValue').",
                  file=sys.stderr)
            return RC_FAIL

        print("\n=== no collateral deny: these must remain 'allowed' ===")
        for pr in a.principal:
            for entry in a.also_allowed:
                rs, _, act = entry.partition("|")
                act = act or a.action[0]
                outcome = run_sim(pr, rs, act)
                stopped = stop_if_not_decidable(outcome, f"collateral:{pr}|{rs}|{act}")
                if stopped is not None:
                    return stopped
                verdict = outcome.decision
                ok = verdict == "allowed"
                if not ok:
                    failures.append(f"COLLATERAL {pr.split('/')[-1]} lost {act} on "
                                    f"{rs.split(':secret:')[-1]} -> {verdict}"
                                    + ("   (no ACTION given -- it inherited --action[0]; "
                                       "pass 'ARN|ACTION' if you meant a different one)"
                                       if not entry.partition('|')[2] else ""))
                print(f"  [{'PASS' if ok else 'FAIL'}] {pr.split('/')[-1]:<30} {act:<30} "
                      f"{rs.split(':secret:')[-1][:30]:<30} -> {verdict}")

    print_completed_budget()
    print()
    if failures:
        print(f"RESULT: FAIL ({len(failures)})")
        for failure in failures:
            print(f"  !! {failure}")
        return RC_FAIL
    print("RESULT: PASS")
    print("  NOTE: a PASS here is a CAPABILITY proof (IAM evaluation), not a BEHAVIOUR proof.")
    print("  If any consumer swallows a denied read (except -> pass/return None), it fails SILENT:")
    print("  a liveness check will pass while the feature dies. Exercise that consumer's OUTPUT.")
    return RC_CLEAN


if __name__ == "__main__":
    sys.exit(main())
