#!/usr/bin/env python3
"""comp-iam APPLIED-plane census: generation + VINTAGE HONESTY.

Implements the load-bearing half of CVO's design brief
`org/tier1_exec/3.0.0_SA_CVO/deliverables/COMP_IAM_APPLIED_PLANE_DESIGN_BRIEF_20260720.md`
(Andrew-direct 2026-07-20 + 2026-07-22: "expand comp-iam to include not just terraform iams but also
grants and etc, essentially trying to build `aws iam` into comp-iam" / "avoid regex unless extremely
stable"). Build assigned to 0.8.0_AE_CloudComp 2026-07-22; CVO holds verify-on-land.

WHY THIS MODULE IS THE VINTAGE LOGIC AND NOT THE GENERATOR
----------------------------------------------------------
The generator was never the hard part -- `iam get-account-authorization-details` is one paginated,
fully-structured call and `.tools/comp-tagauthz.py:269` has been making it in production for weeks.
CVO's section 9 names the actual risk and CTO ratified it 2026-07-22:

    "An IAM instrument that answers confidently from a 2026-06-03 census against 111 of 158 roles is
     not a weaker instrument, it is a LYING one -- and it lies in the GRANTED direction, which is the
     dangerous one."

So this module's centre of gravity is: can the caller tell WHEN the census was taken, WHAT it covers,
and WHETHER that is good enough to answer with? Today the answer is no on all three -- the shipped
census (`docs/briefs/cmpaws-iam-axis-census-20260603.json`) carries `_meta` with author/account/method
and NO generated-date field at all. Its only vintage is the filename, which no code reads.

THREE FAILURE MODES THIS CLOSES, all of the same family this estate keeps hitting:
  1. NO VINTAGE      -> an undated census answers as confidently as a fresh one.
  2. STALE VINTAGE   -> a 7-week-old census answers about roles that have since changed.
  3. PARTIAL SCOPE   -> 111 roles presented as "live IAM" when Terraform alone declares 158, with no
                        statement of the denominator. A set-difference against an under-enumerated
                        population reports MISSING as ABSENT.
(3) is Andrew's 2026-07-22 gap verbatim: "nothing set-differences an enumerated grant against its real
population." A census that does not state its own denominator cannot support a set-difference, because
every element it omits looks like an element that does not exist.

NO REGEX. Per Andrew's constraint: this module parses nothing. It reads structured JSON from AWS's own
API and compares whole strings. The only string operation on an identifier is exact equality.

STDLIB-ONLY at import time. boto3/subprocess are touched lazily inside the generator so that every
vintage/freshness predicate is importable and testable with zero AWS and zero third-party deps -- the
same posture `iam_cli._simulate_self_test` already takes for the decision plane.
"""
from __future__ import annotations

from pathlib import Path

# ---------------------------------------------------------------------------------------------
# THE VINTAGE GATE MOVED to census_substrate.py (2026-08-05, the descriptor-substrate extraction,
# Andrew-present; record ANDREW_DIRECT_20260805_0050Z_descriptor_substrate_extraction.md). The
# gate's HISTORY moved with it -- the F1 FUTURE-bypass mutant, the F3 declarative-drift lesson,
# the NO_VINTAGE-is-not-STALE epistemics all live in the substrate's comments now. This module
# RE-EXPORTS THE SAME OBJECTS so every existing import site (iam_cli.py, the 12-test vintage
# suite) is untouched: one gate, one home, N doors. The commit_stream extraction pattern.
# ---------------------------------------------------------------------------------------------
from census_substrate import (  # noqa: F401 -- re-exports ARE the API
    CLOCK_SKEW_TOLERANCE_HOURS,
    DEFAULT_TTL_HOURS,
    FRESH,
    FUTURE,
    NO_VINTAGE,
    STALE,
    _ISO_Z,
    _utcnow,
    census_age_hours,
    census_freshness,
    parse_generated_utc,
)


def census_scope(census: dict) -> dict:
    """What this census actually COVERS, so a caller can state its denominator.

    Returns {account, role_count, scope_note, api}. Every field may be None/absent -- an unstated
    scope is reported as unstated, never inferred. The 2026-06-03 census is customer-role-scoped
    (111 roles) while Terraform declares 158; nothing in its payload says so, which is precisely how
    a partial population passes as a complete one.
    """
    meta = census.get("_meta") or {}
    roles = census.get("roles") or []
    return {
        "account": meta.get("account"),
        "role_count": len(roles),
        "scope_note": meta.get("scope") or meta.get("note"),
        "api": meta.get("api") or meta.get("method"),
        "accounts_swept": meta.get("accounts_swept"),
    }


def provenance_lines(census: dict, census_path, ttl_hours: float = DEFAULT_TTL_HOURS, now=None):
    """The header EVERY applied-plane verdict prints. Mirrors the comp-kuzu provenance pattern.

    Returns a list of printable lines. It always states age and denominator, because a verdict whose
    provenance the reader has to go looking for is a verdict quoted without it.
    """
    verdict, age = census_freshness(census, ttl_hours=ttl_hours, now=now)
    scope = census_scope(census)
    name = Path(census_path).name if census_path else "<in-memory>"
    lines = []
    if verdict == NO_VINTAGE:
        lines.append(f"CENSUS PROVENANCE: {name} -- vintage UNKNOWN (no _meta.generated_utc)")
        lines.append("  !! This census cannot date itself. Its age is not large; it is UNMEASURED.")
    elif verdict == FUTURE:
        lines.append(f"CENSUS PROVENANCE: {name} -- generated "
                     f"{parse_generated_utc(census).strftime(_ISO_Z)} [FUTURE]")
        lines.append(f"  !! IMPOSSIBLE VINTAGE: dated {abs(age):.1f}h in the FUTURE. A census cannot "
                     f"be observed later than now.")
        lines.append("  !! Treat as UNTRUSTWORTHY, not as very fresh -- clock skew or a hand-edited "
                     "date. Pushing the date forward must never buy authority.")
    else:
        lines.append(f"CENSUS PROVENANCE: {name} -- generated {parse_generated_utc(census).strftime(_ISO_Z)} "
                     f"(age {age:.1f}h, TTL {ttl_hours:g}h) [{verdict}]")
    acct = scope["account"] or "UNSTATED"
    swept = scope["accounts_swept"]
    lines.append(f"  account: {acct}" + (f" | accounts swept: {swept}" if swept else
                 " | accounts swept: UNSTATED (single-account read unless said otherwise)"))
    lines.append(f"  roles in census: {scope['role_count']}"
                 + (f" | scope: {scope['scope_note']}" if scope["scope_note"] else
                    " | scope: UNSTATED -- coverage vs live IAM is UNKNOWN"))
    return lines


def build_census(account: str | None = None, aws_bin: str = "aws") -> dict:
    """Generate a vintage-stamped APPLIED census from `iam get-account-authorization-details`.

    ONE structured call returns every role/group/user with inline + attached-managed policy documents
    and trust policies, as JSON -- so this is a delegate-don't-parse read with no regex anywhere.
    The stamp is applied HERE, at the moment of the read, from the reader's own clock -- never
    back-filled later from a filename or an mtime, which would date the artifact rather than the
    measurement.

    Lazy subprocess by design: importing this module must not require AWS.
    """
    started = _utcnow()
    # THE TRANSPORT MOVED to census_substrate.run_cli_json (2026-08-05 extraction): the explicit
    # .cmd-aware exe resolver + the three NAMED failure classes (CliNotFound = tooling/PATH,
    # CliCallFailed = the cloud said no, CliEmptyStdout = the rc=0-empty false-clean) -- with
    # their measured history (the 07-22 WinError-2 first cut; "lifting the CALL without its
    # RESOLVER is how a proven mechanism is re-broken at a new site") in the substrate's
    # comments. All three subclass RuntimeError, so this function's failure contract is
    # unchanged for every existing caller. This descriptor is shaper=custom: the AAD
    # normalization below stays HERE, at its tool, riding the shared transport.
    from census_substrate import run_cli_json
    aad = run_cli_json(["iam", "get-account-authorization-details", "--output", "json"],
                       cli_bin=aws_bin)

    roles_raw = aad.get("RoleDetailList") or []
    roles = []
    for r in roles_raw:
        statements = []
        for pol in (r.get("RolePolicyList") or []):          # inline
            statements.extend(_statements_from_document(pol.get("PolicyDocument"),
                                                        "inline:" + str(pol.get("PolicyName"))))
        for att in (r.get("AttachedManagedPolicies") or []):  # managed: recorded, not resolved
            statements.append({"effect": "UNRESOLVED", "actions": [], "resources": [],
                               "source": "managed:" + str(att.get("PolicyArn"))})
        roles.append({
            "role_name": r.get("RoleName"),
            "arn": r.get("Arn"),
            "role_id": r.get("RoleId"),
            # D4: CreateDate is what lets a missing node be ATTRIBUTED to the producer that should
            # have caught it. Without a creation time, "absent from the graph" is a fact with no
            # owner -- and a finding with no owner is a finding nobody acts on.
            "create_date": r.get("CreateDate"),
            "trust_policy": r.get("AssumeRolePolicyDocument"),
            "tags": r.get("Tags") or [],
            "permissions_boundary": r.get("PermissionsBoundary"),
            "statements": statements,
        })

    return {
        "_meta": {
            "generated_utc": started.strftime(_ISO_Z),
            "account": account or _account_from_arns(roles),
            "api": "iam:GetAccountAuthorizationDetails",
            "tool": "comp-iam refresh-census",
            "accounts_swept": 1,
            "scope": ("single-account, ALL roles returned by GetAccountAuthorizationDetails "
                      "(inline statements expanded; attached-managed recorded as UNRESOLVED, "
                      "not fetched -- see BL-managed below)"),
            "managed_policies_resolved": False,
        },
        "summary": {
            "role_count": len(roles),
            "group_count": len(aad.get("GroupDetailList") or []),
            "user_count": len(aad.get("UserDetailList") or []),
            "policy_count": len(aad.get("Policies") or []),
        },
        "roles": roles,
    }


def _statements_from_document(doc, source: str) -> list:
    """Normalize one IAM policy document into the reconcile contract. Structured, no regex.

    AWS returns Action/Resource as either a string or a list; both shapes are normalized to a list.
    Effect is lowercased for comparison only -- the raw document is not rewritten.
    """
    if not isinstance(doc, dict):
        return []
    out = []
    stmts = doc.get("Statement")
    if isinstance(stmts, dict):
        stmts = [stmts]
    for s in (stmts or []):
        if not isinstance(s, dict):
            continue
        out.append({
            "effect": str(s.get("Effect", "")).lower(),
            "actions": _as_list(s.get("Action")),
            "resources": _as_list(s.get("Resource")),
            "condition": s.get("Condition"),
            "sid": s.get("Sid"),
            "source": source,
        })
    return out


def _as_list(v) -> list:
    if v is None:
        return []
    return [str(x) for x in v] if isinstance(v, (list, tuple)) else [str(v)]


def _account_from_arns(roles: list):
    """Account id from a role ARN's fixed 6-field colon layout (AWS-guaranteed), not a regex."""
    for r in roles:
        arn = r.get("arn") or ""
        parts = str(arn).split(":", 5)
        if len(parts) >= 5 and parts[4]:
            return parts[4]
    return None
