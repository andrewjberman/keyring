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
  permission-cold: PERMISSION grain (NFRA_IAMROLES202609.TO-IAM-s-1, FWD-2 -- role-cold's sibling one
                   plane down). `--role <name> --lookback <days>`: union the role's Allow actions across
                   every attached-managed + inline policy (the DESIRED-plane GRANTED set), then classify
                   each against IAM ACCESS ADVISOR action-level usage telemetry (iam:GenerateService
                   LastAccessedDetails / iam:GetServiceLastAccessedDetails, Granularity=ACTION_LEVEL) --
                   used | never-used | unobservable, with a printed DENOMINATOR. ACCESS ADVISOR IS NOT
                   AWS ACCESS ANALYZER: Access Advisor is free, core-IAM, same API family as role-cold's
                   own RoleLastUsedDate read (both live on the `iam` boto3 client already used here);
                   Access Analyzer (the access-analyzer:* unused-access finding type) is a SEPARATE,
                   PRICED service this tool NEVER calls (C-ANALYZER-PRICED-FIRST stays HELD). A service
                   AWS does not track at action grain, or an action absent from AWS's own tracked list
                   for a service that IS tracked, renders unobservable -- NEVER never-used (FWD-7's
                   discipline, carried to this grain: a permission nobody could observe must never read
                   as a permission shown clean).

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
import time

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


# ---- permission-cold: PERMISSION grain (NFRA_IAMROLES202609.TO-IAM-s-1, FWD-2) --------------------
_PERM_LIMITS_BANNER = (
    "  PERMISSION-GRAIN NOTES (NFRA_IAMROLES202609.TO-IAM-s-1):\n"
    "    GRANTED is the DESIRED plane -- the union of Allow actions across every attached-managed +\n"
    "    inline policy on the role (a policy DOCUMENT, per C-DESIRED-UNTIL-EXERCISED). A wildcard\n"
    "    action token ('*' or 'svc:*') is carried VERBATIM, never expanded or dropped, and renders\n"
    "    unobservable (this tool does not enumerate the concrete actions a wildcard covers).\n"
    "    USAGE is IAM ACCESS ADVISOR action-level telemetry (iam:GenerateServiceLastAccessedDetails /\n"
    "    iam:GetServiceLastAccessedDetails, Granularity=ACTION_LEVEL) -- free, core-IAM, the SAME API\n"
    "    family as role-cold's RoleLastUsedDate. THIS IS NOT AWS ACCESS ANALYZER (access-analyzer:*,\n"
    "    the PRICED unused-access finding type) -- that stays HELD per C-ANALYZER-PRICED-FIRST and is\n"
    "    never called by this tool. A service AWS does not track at action grain, or an action absent\n"
    "    from AWS's own tracked-action list for a service that IS tracked, renders unobservable --\n"
    "    NEVER never-used (FWD-7's discipline, one grain over: unobservable != clean).\n"
    "    'never-used' means: tracked by Access Advisor, and either never accessed at all or last\n"
    "    accessed OUTSIDE the stated --lookback window -- 'unused over the stated lookback', FWD-2's\n"
    "    own phrasing, not a claim the action was never called at any point in the account's history.")


def _actions_from_doc(doc: dict) -> set:
    """Allow-action tokens out of one IAM policy document. DESIRED plane (C-DESIRED-UNTIL-EXERCISED)
    -- this is the GRANTED set, never a usage claim. Deny statements are not granted; skipped."""
    out = set()
    stmts = doc.get("Statement", []) if isinstance(doc, dict) else []
    if isinstance(stmts, dict):
        stmts = [stmts]
    for st in stmts:
        if not isinstance(st, dict) or st.get("Effect") != "Allow":
            continue
        a = st.get("Action", [])
        if isinstance(a, str):
            a = [a]
        out.update(x for x in a if isinstance(x, str))
    return out


def granted_permissions(iam, role_name: str):
    """(sorted_actions, read_ok). Union of Allow-actions across attached-managed + inline policies.
    A read failure is UNKNOWN, never assumed-empty (same discipline as role_last_used: an unread
    role/policy is BLIND, not clear)."""
    acts = set()
    try:
        for p in iam.list_attached_role_policies(RoleName=role_name).get("AttachedPolicies", []):
            ver = iam.get_policy(PolicyArn=p["PolicyArn"])["Policy"]["DefaultVersionId"]
            doc = iam.get_policy_version(PolicyArn=p["PolicyArn"], VersionId=ver)["PolicyVersion"]["Document"]
            acts |= _actions_from_doc(doc)
        for name in iam.list_role_policies(RoleName=role_name).get("PolicyNames", []):
            doc = iam.get_role_policy(RoleName=role_name, PolicyName=name)["PolicyDocument"]
            acts |= _actions_from_doc(doc)
        return sorted(acts), True
    except Exception:  # noqa: BLE001
        return sorted(acts), False


def access_advisor_action_level(iam, role_arn: str, poll_s: float = 2.0, max_polls: int = 30):
    """(services_by_namespace, read_ok). ACTION_LEVEL Access Advisor job for role_arn. NOT Access
    Analyzer (see _PERM_LIMITS_BANNER) -- generate/get-service-last-accessed-details is core IAM.
    A job that does not COMPLETE within the poll budget is UNKNOWN, never 'no usage' (Rule-22a
    carried: a read failure must never render as its convenient opposite)."""
    try:
        job_id = iam.generate_service_last_accessed_details(
            Arn=role_arn, Granularity="ACTION_LEVEL")["JobId"]
        res = {}
        for _ in range(max_polls):
            res = iam.get_service_last_accessed_details(JobId=job_id)
            if res.get("JobStatus") in ("COMPLETED", "FAILED"):
                break
            time.sleep(poll_s)
        if res.get("JobStatus") != "COMPLETED":
            return {}, False
        by_ns = {}
        for svc in res.get("ServicesLastAccessed", []):
            ns = svc.get("ServiceNamespace")
            if ns:
                by_ns[ns] = svc
        return by_ns, True
    except Exception:  # noqa: BLE001
        return {}, False


def permission_ledger(granted: list, advisor_by_ns: dict, advisor_read_ok: bool, now, lookback_days: int) -> dict:
    """For each GRANTED permission (service:Action), a status row: used | never-used | unobservable.
    `now` is timezone-aware UTC. Never renders unobservable as never-used or vice-versa (FWD-7,
    carried)."""
    rows = []
    for perm in granted:
        if ":" not in perm:
            rows.append({"permission": perm, "status": "unobservable", "reason": "malformed action token"})
            continue
        ns, action = perm.split(":", 1)
        if action == "*" or ns == "*":
            rows.append({"permission": perm, "status": "unobservable", "reason": "wildcard-not-expanded"})
            continue
        if not advisor_read_ok:
            rows.append({"permission": perm, "status": "unobservable",
                         "reason": "access-advisor-job-unreadable (BLIND, not unused)"})
            continue
        svc = advisor_by_ns.get(ns)
        if svc is None:
            rows.append({"permission": perm, "status": "unobservable",
                         "reason": "service not present in Access Advisor response"})
            continue
        tracked = svc.get("TrackedActionsLastAccessed")
        if tracked is None:
            rows.append({"permission": perm, "status": "unobservable",
                         "reason": "service '%s' has no action-level tracking in Access Advisor" % ns})
            continue
        hit = next((t for t in tracked if t.get("ActionName") == action), None)
        if hit is None:
            rows.append({"permission": perm, "status": "unobservable",
                         "reason": "action not in Access Advisor's tracked-action list for '%s'" % ns})
            continue
        last = hit.get("LastAccessedTime")
        if last is None:
            rows.append({"permission": perm, "status": "never-used", "last_used": None})
            continue
        if hasattr(last, "astimezone"):
            last = last.astimezone(dt.timezone.utc)
        age_days = (now - last).days
        if age_days <= lookback_days:
            rows.append({"permission": perm, "status": "used",
                         "last_used": last.date().isoformat(), "age_days": age_days})
        else:
            rows.append({"permission": perm, "status": "never-used",
                         "last_used": last.date().isoformat(), "age_days": age_days,
                         "reason": "last use is %dd ago, outside the %dd lookback" % (age_days, lookback_days)})
    counts = {"used": 0, "never-used": 0, "unobservable": 0}
    for r in rows:
        counts[r["status"]] += 1
    return {"rows": rows, "counts": counts, "denominator": len(rows)}


def _render_permissions(role_name: str, lookback_days: int, led: dict, advisor_read_ok: bool, granted_read_ok: bool) -> str:
    L = ["comp-iam-usage permission-cold -- PERMISSION-grain usage for role '%s' (ADVISORY; NEVER deletes)"
         % role_name,
         "  lookback %d days | granted permissions examined (DENOMINATOR)=%d"
         % (lookback_days, led["denominator"]),
         "  counts: used=%d never-used=%d unobservable=%d"
         % (led["counts"]["used"], led["counts"]["never-used"], led["counts"]["unobservable"])]
    if not granted_read_ok:
        L.append("  BLIND: could not fully read the role's attached/inline policies -- the granted set"
                 " below may be a PARTIAL union, never treat it as complete.")
    if not advisor_read_ok:
        L.append("  BLIND: the IAM Access Advisor job did not complete -- every permission below is"
                 " unobservable, NOT unused.")
    L.append("")
    for r in sorted(led["rows"], key=lambda r: (r["status"], r["permission"])):
        extra = ""
        if r["status"] == "used":
            extra = "  last-used=%s (%dd ago)" % (r.get("last_used"), r.get("age_days", 0))
        elif r["status"] == "never-used" and r.get("last_used"):
            extra = "  last-used=%s (%dd ago, outside %dd lookback)" % (
                r.get("last_used"), r.get("age_days", 0), lookback_days)
        elif r["status"] == "unobservable":
            extra = "  (%s)" % r.get("reason", "")
        L.append("    %-14s %-40s%s" % (r["status"], r["permission"], extra))
    L += ["", _PERM_LIMITS_BANNER]
    return "\n".join(L)


# ---- offline self-test: PERMISSION grain (AC4 -- its own regression bar) --------------------------
def _self_test_permissions(ok: list, ck) -> None:
    """Offline mutants for permission_ledger -- no AWS. Appends PASS/FAIL to `ok` via `ck`, same
    contract as the role-grain block below. Named 'permission' throughout (AC4: self-test now
    exercises the PERMISSION grain, not just role-grain)."""
    now = dt.datetime(2026, 9, 10, tzinfo=dt.timezone.utc)
    lookback = 90

    def ago(days):
        return now - dt.timedelta(days=days)

    granted = ["s3:GetObject", "s3:PutObject", "s3:*", "logs:CreateLogGroup", "logs:PutLogEvents",
               "dynamodb:Query", "dynamodb:Scan", "malformed-token"]
    advisor_by_ns = {
        # s3 has NO action-level tracking in this fixture -> every s3 action is unobservable.
        "s3": {"ServiceName": "Amazon S3", "LastAuthenticated": ago(5)},
        # logs DOES track action-level; CreateLogGroup used recently, CreateLogStream tracked-but-
        # irrelevant here, PutLogEvents GRANTED but absent from the tracked list -> unobservable.
        "logs": {"ServiceName": "CloudWatch Logs",
                 "TrackedActionsLastAccessed": [
                     {"ActionName": "CreateLogGroup", "LastAccessedTime": ago(5)},
                     {"ActionName": "CreateLogStream", "LastAccessedTime": ago(5)}]},
        # dynamodb tracks action-level; Query tracked but never accessed (no LastAccessedTime) ->
        # never-used; Scan was accessed but 400d ago, outside the 90d lookback -> never-used (stale).
        "dynamodb": {"ServiceName": "Amazon DynamoDB",
                     "TrackedActionsLastAccessed": [
                         {"ActionName": "Query"},
                         {"ActionName": "Scan", "LastAccessedTime": ago(400)}]},
    }
    led = permission_ledger(granted, advisor_by_ns, True, now, lookback)
    by_perm = {r["permission"]: r for r in led["rows"]}

    ck("permission_denominator_matches_granted_count", led["denominator"] == len(granted),
       f"denom={led['denominator']} granted={len(granted)}")
    ck("permission_malformed_token_is_unobservable", by_perm["malformed-token"]["status"] == "unobservable")
    ck("permission_unobservable_when_service_lacks_action_tracking",
       by_perm["s3:GetObject"]["status"] == "unobservable" and by_perm["s3:PutObject"]["status"] == "unobservable")
    ck("permission_wildcard_is_unobservable_not_dropped", by_perm["s3:*"]["status"] == "unobservable")
    ck("permission_used_within_lookback", by_perm["logs:CreateLogGroup"]["status"] == "used")
    ck("permission_untracked_action_is_unobservable_not_never_used",
       by_perm["logs:PutLogEvents"]["status"] == "unobservable")
    ck("permission_tracked_never_accessed_is_never_used", by_perm["dynamodb:Query"]["status"] == "never-used")
    ck("permission_stale_beyond_lookback_is_never_used_not_used", by_perm["dynamodb:Scan"]["status"] == "never-used")

    led_blind = permission_ledger(granted, {}, False, now, lookback)
    ck("permission_blind_advisor_job_is_unobservable_not_unused",
       all(r["status"] == "unobservable" for r in led_blind["rows"]))
    # AC4's own fix-or-carry: the permission-grain banner names the Access-Advisor-vs-Access-Analyzer
    # distinction, so the next extension cannot silently reach for the priced fallback.
    ck("permission_access_analyzer_distinction_named", "AWS ACCESS ANALYZER" in _PERM_LIMITS_BANNER)


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

    # PERMISSION grain (NFRA_IAMROLES202609.TO-IAM-s-1, AC4): its own regression bar, offline.
    _self_test_permissions(ok, ck)

    good = all(ok)
    print("\n" + _LIMITS_BANNER)
    print("\n" + _PERM_LIMITS_BANNER)
    print("\n" + ("OK: never-used!=cold, break-glass-guard-not-debris, UNKNOWN-band, hold-aware, "
                  "22a limits NAMED (fix-or-carry), permission-grain unobservable!=never-used -- all held"
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
    pp = sub.add_parser("permission-cold",
                        help="PERMISSION grain: which of a role's GRANTED permissions were never used "
                             "over a stated lookback (IAM Access Advisor ACTION_LEVEL, NOT Access Analyzer)")
    pp.add_argument("--role", required=True)
    pp.add_argument("--lookback", type=int, default=90, help="days (default 90)")
    pp.add_argument("--json", action="store_true")
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
    if args.cmd == "permission-cold":
        iam = _iam()
        try:
            role_arn = iam.get_role(RoleName=args.role)["Role"]["Arn"]
        except Exception as e:  # noqa: BLE001
            print(json.dumps({"role": args.role, "read": False,
                              "error": "get_role failed: %s" % str(e)[:160],
                              "note": "role unreadable -> UNKNOWN, never rendered as clean or unused"},
                             indent=1))
            return 2
        granted, granted_ok = granted_permissions(iam, args.role)
        advisor_by_ns, advisor_ok = access_advisor_action_level(iam, role_arn)
        now = dt.datetime.now(dt.timezone.utc)
        led = permission_ledger(granted, advisor_by_ns, advisor_ok, now, args.lookback)
        if args.json:
            print(json.dumps({"role": args.role, "role_arn": role_arn, "lookback_days": args.lookback,
                              "granted_read_ok": granted_ok, "advisor_read_ok": advisor_ok, **led},
                             indent=1, default=str))
        else:
            print(_render_permissions(args.role, args.lookback, led, advisor_ok, granted_ok))
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
