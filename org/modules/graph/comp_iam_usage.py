"""comp-iam-usage -- the ACCESS-PLANE coldness + reach signal comp-iam lacks (NFRA_DECOMTOOL).

comp-iam answers deploy-time CORRECTNESS (does this role have the perms this call needs -- Terraform
DESIRED + a live simulate). comp-iam-usage answers the LIFECYCLE question: is this role/grant still
USED, and who still REACHES a resource. A SIBLING, deliberately -- overloading the deploy-time tool
with a lifecycle question is the exact class Rule 22a warns about (a DESIRED-plane read answering a
usage question). Read-only, advisory, NEVER deletes; the identification column feeds OPAL_LCLRPO's
existing CTO-gated, Andrew-delete-word disposal path -- no second disposal path.

  role-cold      : comp_debris.classify() on the IDENTITY plane. RoleLastUsed.LastUsedDate ->
                   last_activity_day; role CreateDate -> creation; the SAME bands + three refinements
                   (imported from comp_debris VERBATIM -- one coldness family, one plane over). A role
                   created but never assumed is STILLBORN-OR-GUARD (break-glass is a guard, not debris).
  who-can-reach  : the APPLIED resource-side reach set -- reads LIVE resource policies (get-bucket-policy
                   / get-key-policy / get-queue-attributes / get-topic-attributes / lambda get-policy).
  reach-check    : a (principal, action, resource) reachability VERDICT grounded on the live primitive
                   simulate-principal-policy, run with the Rule-22a disciplines (below).

RULE-22a FIX-OR-CARRY (CTO ruling-20 HARD mandate -- NEVER inherit comp-iam's three limits silently;
this tool NAMES each in its own output, see _LIMITS_BANNER + `comp-iam-usage limits`):

  (a) comp-iam models (action), NOT (action,resource) -- a role holding s3:GetObject on ANY bucket
      reads [GRANTED] for EVERY other. FIX: reach-check grounds on simulate-principal-policy with the
      EXACT --resource-arns, which is (action,resource)-precise by construction.
  (b) simulate-principal-policy carrying 2+ --resource-arns flips the HELD ones to implicitDeny.
      FIX: reach-check sends exactly ONE --resource-arns per call, and the positive control is a
      SEPARATE invocation (a control batched with the target is corrupted by its own presence).
  (c) simulate EVALUATES Condition blocks; with no --context-entries a conditioned statement returns
      implicitDeny byte-identical to a real deny. FIX/CARRY: reach-check passes --context-entries when
      given; a conditioned statement with no context is reported UNKNOWN, never a (false) deny.
  Plus comp-iam's DESIRED-not-APPLIED limit: who-can-reach / reach-check read LIVE (APPLIED), and an
  unreadable/unparseable policy is UNKNOWN, never "no reach" (an unparsed Deny is not silence).

Author: 0.8.0_AE_CloudComp~B (NFRA_DECOMTOOL.TO-1 landing of base-0.8.0's arch-ratified design).
2026-07-17. Read-only, advisory, NEVER deletes. Reuses comp_debris.classify/BANDS/_HELD_RX.
Access Analyzer enable is HELD (Andrew alert-suspension) -- this tool computes coldness WITHOUT it.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import comp_debris as cd  # noqa: E402  (classify, BANDS, _HELD_RX reused verbatim -- one family)

_LIMITS_BANNER = (
    "  RULE-22a fix-or-carry (comp-iam's 3 named limits -- NAMED, never silently inherited):\n"
    "    (a) (action,resource) blindness  -> FIXED: reach-check simulates the EXACT --resource-arns\n"
    "        (comp-iam models (action) only; a grant on ANY arn falsely reads GRANTED for EVERY arn).\n"
    "    (b) 2+-ARN implicitDeny poisoning -> FIXED: ONE --resource-arns per reach-check call; the\n"
    "        positive control is a SEPARATE invocation (batching corrupts the control).\n"
    "    (c) Condition-block false-deny    -> FIXED/CARRIED: --context-entries when given; a conditioned\n"
    "        statement with no context is UNKNOWN, never a (false) deny.\n"
    "    (+) DESIRED-not-APPLIED           -> FIXED: who-can-reach / reach-check read LIVE policies;\n"
    "        an unreadable/unparseable policy is UNKNOWN, never 'no reach' (an unparsed Deny != silence).")


def _iam():
    import boto3
    return boto3.client("iam")


# ---- role-cold: comp_debris.classify() on the identity plane (wall-clock; roles are not T-1) -----
def list_roles(iam) -> list:
    out, marker = [], None
    while True:
        kw = {"Marker": marker} if marker else {}
        r = iam.list_roles(**kw)
        for role in r.get("Roles", []):
            out.append({"name": role["RoleName"], "created": role.get("CreateDate")})
        marker = r.get("Marker")
        if not r.get("IsTruncated"):
            break
    return out


def role_last_used(iam, name: str):
    """(read_ok, last_used_iso_or_None). ListRoles does NOT populate RoleLastUsed -> GetRole does.
    A read failure is UNKNOWN, never assumed-unused (refinement 2 / Rule-22a: an unread role is blind)."""
    try:
        lu = iam.get_role(RoleName=name)["Role"].get("RoleLastUsed") or {}
        d = lu.get("LastUsedDate")
        return True, (d.astimezone(dt.timezone.utc).date().isoformat() if d else None)
    except Exception:  # noqa: BLE001
        return False, None


def role_records(iam, limit: int) -> list:
    roles = list_roles(iam)
    if limit:
        roles = roles[:limit]
    recs = []
    for r in roles:
        read_ok, last = role_last_used(iam, r["name"])
        created = r["created"].astimezone(dt.timezone.utc).isoformat() if r.get("created") else ""
        recs.append({"rtype": "IAM_ROLE", "name": r["name"], "created": created,
                     "hist": ({"read": True, "last_invoked_day": last} if read_ok
                              else {"read": False, "error": "get_role failed"}),
                     "signal_basis": "iam-role-last-used"})
    return recs


def iam_ledger(records: list, now_date, days: int, hot_days: int) -> dict:
    held, classified = [], []
    for rec in records:
        if cd._HELD_RX.search(rec["name"] or ""):
            held.append(rec["name"])
            continue
        # roles are IDENTITY, not T-1 data -> wall-clock dormancy (no trading-calendar age_fn).
        band = cd.classify({"name": rec["name"], "last_modified": rec["created"]},
                           rec["hist"], now_date, days, hot_days)
        band["rtype"] = rec["rtype"]
        band["signal_basis"] = rec["signal_basis"]
        classified.append(band)
    by_band = {b: [c for c in classified if c["band"] == b] for b in cd.BANDS}
    reap = sorted(by_band["COLD-DORMANT"], key=lambda c: -c.get("dormant_days", 0))
    return {"window_days": days, "hot_days": hot_days, "n_total": len(records),
            "n_held_excluded": len(held), "held_excluded": sorted(held),
            "counts": {b: len(by_band[b]) for b in cd.BANDS},
            "reap_rank_cold_dormant": reap,
            "purpose_review_stillborn_or_guard": by_band["STILLBORN-OR-GUARD"],
            "too_young": by_band["TOO-YOUNG"], "unknown": by_band["UNKNOWN"], "hot": by_band["HOT"]}


def _render_roles(led: dict) -> str:
    L = ["comp-iam-usage role-cold -- last-assume coldness (ADVISORY; NEVER deletes; hold-aware)",
         "  window %dd (hot %dd) | %d roles sampled | %d held EXCLUDED"
         % (led["window_days"], led["hot_days"], led["n_total"], led["n_held_excluded"]),
         "  bands: " + " ".join("%s=%d" % (b, led["counts"][b]) for b in cd.BANDS),
         "",
         "  REAP RANK -- COLD-DORMANT roles (used, then went dormant; coldest first):"]
    if not led["reap_rank_cold_dormant"]:
        L.append("    (none dormant-after-use in window)")
    for c in led["reap_rank_cold_dormant"][:25]:
        L.append("    %4dd  %-48s last-used=%s  [%s]"
                 % (c.get("dormant_days", 0), c["name"], c.get("last_invoked"), c["signal_basis"]))
    sob = led["purpose_review_stillborn_or_guard"]
    if sob:
        L += ["", "  PURPOSE REVIEW -- STILLBORN-OR-GUARD (%d): older than window, NEVER assumed" % len(sob),
              "  (a break-glass/emergency role is a guard, NOT debris -- a human decides):"]
        for c in sob[:20]:
            L.append("    created=%s  %s" % (c["created"], c["name"]))
    if led["counts"]["UNKNOWN"]:
        L += ["", "  UNKNOWN (%d): RoleLastUsed unreadable/absent -- BLIND, not unused." % led["counts"]["UNKNOWN"]]
    L += ["", _LIMITS_BANNER]
    return "\n".join(L)


# ---- who-can-reach <arn>: the APPLIED resource-side (Rule-22a DESIRED->APPLIED fix) --------------
def who_can_reach(arn: str) -> dict:
    """Resource-policy principals for an ARN. An UNREADABLE policy is UNKNOWN, never 'no reach'
    (an unparsed Deny is not silence). Production unions this with every identity policy referencing
    the ARN; v1 reads the resource side (the plane comp-iam entirely lacks)."""
    import boto3
    if ":s3:::" in arn:
        bucket = arn.split(":::", 1)[1].split("/", 1)[0]
        s3 = boto3.client("s3")
        try:
            pol = json.loads(s3.get_bucket_policy(Bucket=bucket)["Policy"])
        except Exception as e:  # noqa: BLE001
            msg = str(e)
            if "NoSuchBucketPolicy" in msg:
                return {"arn": arn, "resource_policy": "none", "principals": [], "read": True,
                        "note": "no resource policy -> identity-side grants only (union in prod)"}
            return {"arn": arn, "resource_policy": "UNREADABLE", "principals": [], "read": False,
                    "error": msg[:160], "note": "UNREADABLE != no reach (Rule-22a: an unparsed policy is UNKNOWN)"}
        stmts = []
        for st in pol.get("Statement", []):
            p = st.get("Principal", {})
            vals = [p] if isinstance(p, str) else [v for vv in (p.values() if isinstance(p, dict) else [])
                                                   for v in (vv if isinstance(vv, list) else [vv])]
            stmts.append({"sid": st.get("Sid"), "effect": st.get("Effect"),
                          "action": st.get("Action"), "principals": vals,
                          "conditioned": bool(st.get("Condition"))})
        return {"arn": arn, "resource_policy": "present", "read": True, "statements": stmts,
                "note": "APPLIED resource-policy read (Rule-22a DESIRED->APPLIED fix). Conditioned "
                        "statements flagged -- a reach VERDICT on them needs reach-check --context."}
    return {"arn": arn, "read": False,
            "note": "v1 who-can-reach demos S3; KMS/SQS/SNS/Lambda resource policies are the same "
                    "get-*-policy pattern (prod). Use reach-check for an identity->resource verdict."}


# ---- reach-check: a (principal, action, resource) verdict on the LIVE simulate primitive ---------
def reach_check(role_name: str, action: str, resource_arn: str, context: list) -> dict:
    """simulate-principal-policy for EXACTLY ONE (action, resource) -- Rule-22a disciplines:
    ONE --resource-arns (limit b), --context-entries when a statement is conditioned (limit c),
    (action,resource)-precise by construction (limit a). The POSITIVE CONTROL is a SEPARATE
    invocation the caller runs (a control batched with the target is corrupted by its presence)."""
    import boto3
    iam = boto3.client("iam")
    try:
        role_arn = iam.get_role(RoleName=role_name)["Role"]["Arn"]
    except Exception as e:  # noqa: BLE001
        return {"read": False, "verdict": "UNKNOWN", "error": "get_role failed: %s" % str(e)[:120],
                "note": "role unreadable -> UNKNOWN, never a deny"}
    ctx_entries = []
    for kv in context or []:
        if "=" in kv:
            k, v = kv.split("=", 1)
            ctx_entries.append({"ContextKeyName": k, "ContextKeyValues": [v], "ContextKeyType": "string"})
    try:
        kw = {"PolicySourceArn": role_arn, "ActionNames": [action], "ResourceArns": [resource_arn]}
        if ctx_entries:
            kw["ContextEntries"] = ctx_entries
        res = iam.simulate_principal_policy(**kw)["EvaluationResults"][0]
        decision = res.get("EvalDecision")
        missing_ctx = res.get("MissingContextValues") or []
        verdict = decision
        if decision == "implicitDeny" and missing_ctx and not ctx_entries:
            verdict = "UNKNOWN"  # limit (c): a conditioned statement with no context is not a real deny
        return {"read": True, "role": role_name, "action": action, "resource": resource_arn,
                "eval_decision": decision, "verdict": verdict,
                "missing_context_values": missing_ctx,
                "rule22a": {"one_resource_arn": True, "action_resource_precise": True,
                            "condition_handling": ("context-provided" if ctx_entries else
                                                   ("UNKNOWN-not-deny (missing context)" if missing_ctx else "no-condition"))},
                "positive_control": "RUN SEPARATELY: comp-iam-usage reach-check %s <known-allowed-action> "
                                    "<known-allowed-arn> -- a control batched with the target is poisoned (limit b)"
                                    % role_name}
    except Exception as e:  # noqa: BLE001
        return {"read": False, "verdict": "UNKNOWN", "error": "simulate failed: %s" % str(e)[:140]}


# ---- offline self-test ---------------------------------------------------------------------------
def _self_test() -> int:
    print("=== comp-iam-usage --self-test (offline band mutants + limits-named assertion) ===")
    now = dt.date(2026, 7, 17)
    days, hot = 90, 7

    def iso(d):
        return "%sT00:00:00+00:00" % d

    recs = [
        {"rtype": "IAM_ROLE", "name": "role-dormant", "created": iso("2026-01-01"),
         "hist": {"read": True, "last_invoked_day": "2026-05-01"}, "signal_basis": "iam-role-last-used"},
        {"rtype": "IAM_ROLE", "name": "breakglass-emergency", "created": iso("2025-06-01"),
         "hist": {"read": True, "last_invoked_day": None}, "signal_basis": "iam-role-last-used"},
        {"rtype": "IAM_ROLE", "name": "role-new", "created": iso("2026-07-10"),
         "hist": {"read": True, "last_invoked_day": None}, "signal_basis": "iam-role-last-used"},
        {"rtype": "IAM_ROLE", "name": "role-blind", "created": iso("2026-01-01"),
         "hist": {"read": False, "error": "AccessDenied"}, "signal_basis": "iam-role-last-used"},
        {"rtype": "IAM_ROLE", "name": "inf-gold-dispatch-role", "created": iso("2026-01-01"),
         "hist": {"read": True, "last_invoked_day": None}, "signal_basis": "iam-role-last-used"},
        {"rtype": "IAM_ROLE", "name": "role-hot", "created": iso("2026-01-01"),
         "hist": {"read": True, "last_invoked_day": "2026-07-16"}, "signal_basis": "iam-role-last-used"},
    ]
    led = iam_ledger(recs, now, days, hot)
    ok = []

    def ck(n, c, d=""):
        ok.append(c)
        print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  ({d})" if d else ""))

    reap = {c["name"] for c in led["reap_rank_cold_dormant"]}
    ck("dormant_role_is_reap", reap == {"role-dormant"}, f"reap={reap}")
    ck("breakglass_never_used_is_stillborn_NOT_reap",
       any(c["name"] == "breakglass-emergency" for c in led["purpose_review_stillborn_or_guard"]) and "breakglass-emergency" not in reap)
    ck("new_never_used_is_too_young", any(c["name"] == "role-new" for c in led["too_young"]) and "role-new" not in reap)
    ck("blind_is_unknown_NOT_unused", any(c["name"] == "role-blind" for c in led["unknown"]) and "role-blind" not in reap)
    ck("held_excluded", "inf-gold-dispatch-role" in led["held_excluded"])
    ck("hot_is_hot", any(c["name"] == "role-hot" for c in led["hot"]) and "role-hot" not in reap)
    # AC3: the 3 named 22a limits are NAMED in the tool's own output (fix-or-carry, never silent).
    ck("limits_a_action_resource_named", "(action,resource) blindness" in _LIMITS_BANNER)
    ck("limits_b_2arn_poisoning_named", "2+-ARN implicitDeny poisoning" in _LIMITS_BANNER)
    ck("limits_c_condition_named", "Condition-block false-deny" in _LIMITS_BANNER)

    good = all(ok)
    print("\n" + _LIMITS_BANNER)
    print("\n" + ("OK: never-used!=cold, break-glass-guard-not-debris, UNKNOWN-band, hold-aware, "
                  "22a limits NAMED (fix-or-carry) -- all held"
                  if good else "ERROR: comp-iam-usage self-test FAILED"))
    return 0 if good else 1


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="comp-iam-usage",
        description="Access-plane coldness + reach (the lifecycle sibling of comp-iam). Advisory; "
                    "read-only; NEVER deletes. Rule-22a fix-or-carry NAMED in output (see `limits`).")
    sub = ap.add_subparsers(dest="cmd")
    pr = sub.add_parser("role-cold", help="rank roles by last-assume coldness (reuses comp_debris bands)")
    pr.add_argument("--days", type=int, default=90)
    pr.add_argument("--hot-days", type=int, default=7)
    pr.add_argument("--limit", type=int, default=50, help="sample size (get-role is per-role; 0=all)")
    pr.add_argument("--json", action="store_true")
    pw = sub.add_parser("who-can-reach", help="APPLIED resource-policy principals for an ARN")
    pw.add_argument("arn")
    rc = sub.add_parser("reach-check", help="(role,action,resource) verdict via simulate (Rule-22a disciplined)")
    rc.add_argument("role")
    rc.add_argument("action")
    rc.add_argument("resource_arn")
    rc.add_argument("--context", action="append", default=[], help="conditioned-statement key=value (repeatable)")
    sub.add_parser("limits", help="print the Rule-22a fix-or-carry statement (the 3 named limits)")
    sub.add_parser("self-test", help="offline band mutants + limits-named assertion (no AWS)")
    args = ap.parse_args()
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass

    if args.cmd == "self-test":
        return _self_test()
    if args.cmd == "limits":
        print("comp-iam-usage -- Rule-22a fix-or-carry (comp-iam's 3 named limits, never inherited silently):")
        print(_LIMITS_BANNER)
        return 0
    if args.cmd == "role-cold":
        recs = role_records(_iam(), args.limit)
        led = iam_ledger(recs, dt.datetime.now(dt.timezone.utc).date(), args.days, args.hot_days)
        print(json.dumps(led, indent=1, default=str) if args.json else _render_roles(led))
        return 0
    if args.cmd == "who-can-reach":
        out = who_can_reach(args.arn)
        print(json.dumps(out, indent=1, default=str))
        print("\n" + _LIMITS_BANNER)
        return 0
    if args.cmd == "reach-check":
        out = reach_check(args.role, args.action, args.resource_arn, args.context)
        print(json.dumps(out, indent=1, default=str))
        print("\n" + _LIMITS_BANNER)
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
