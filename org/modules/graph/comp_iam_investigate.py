#!/usr/bin/env python3
"""comp-iam investigate-candidates -- RoleLastUsed as a TRIAGE signal only.

NFRA_COMPIAM, 2026-07-25. CTO~Z's original framing for this tool was WRONG and DANGEROUS, and
CVO~Z killed it before it was built: "the positive evidence that could safely inform the exact
task the tool must currently refuse" (least-privilege cleanup). It cannot. Least-privilege
cleanup is almost always trimming ACTIONS WITHIN a live role; RoleLastUsed is a ROLE-grain
observation and is structurally silent on which individual statements were used. Joining a
CODE-grain floor (comp-iam's boto3-source operation list) with a ROLE-grain signal
(RoleLastUsed) cannot produce an ACTION-grain conclusion. Two instruments that each cannot
license a deletion do not jointly license one -- and this one would arrive wearing AWS's own
authority, which is worse than a floor wearing none.

So this tool licenses exactly ONE inference, and the noun IS the control: `INVESTIGATE-CANDIDATE`.
Never `UNUSED`, `UNUSED-ROLE`, `stale`, or any word a hurried reader converts into a warrant.

GROUNDED (2026-07-25, AWS IAM API Reference + User Guide, fetched live -- not recalled):
  - https://docs.aws.amazon.com/IAM/latest/APIReference/API_RoleLastUsed.html :
    "LastUsedDate ... This field is null if the role has not been used within the IAM tracking
    period." -- null is NOT "never used." A role used 401+ days ago and never since reads
    IDENTICALLY to a role that has genuinely never been used. This is the empty-vs-absent
    distinction: rendered here as UNKNOWN, never "never used."
  - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html :
    "The tracking period for a role last activity ... is for the trailing 400 days ... The role
    might have been used more than 400 days ago." Console phrase for the null state: "Not
    accessed in the tracking period" -- deliberately echoed below.
  - REGION SEMANTICS, PINNED (the open question CVO~Z named rather than guessed): `RoleLastUsed`
    is a SINGULAR object per role (LastUsedDate + Region), not a per-region list -- both the API
    schema shape and every doc sentence describing it use the singular ("the Region in which the
    role was last used"). This is a GLOBAL aggregate: IAM reports the ONE most recent use of the
    role, across ALL regions, and `Region` only names WHERE that specific most-recent event
    happened. A role active in another region does NOT read stale because of a region mismatch
    -- CTO~Z's speculative risk ("if it is regional...") does not apply. The real risk is
    temporal (the 400-day window), not geographic.
  - MEASURED LIVE, THIS ACCOUNT (313476888478), 2026-07-25: `list-roles` does NOT populate
    `RoleLastUsed` -- returns `null` UNCONDITIONALLY, even for `astn-wsjft-orchestrator-role`,
    a role with real activity 5h prior at the time of the check. `get-role` on the SAME role,
    SAME moment, returned a real, non-null LastUsedDate/Region. Verified via a positive-
    controlled same-role comparison, not assumed. Consequence: no bulk shortcut exists -- this
    module calls `get-role` once per role.

SCHEDULING CONSTRAINT -- NOT SCHEDULABLE (CTO~Z ruling, 2026-07-25 @170702Z, STANDING):
  `investigate-candidates` MUST NOT be run as a routine/periodic/automated sweep until the
  fleet-scale path is designed for. This is a CONSTRAINT, not a backlog note.

  Grounds: the no-bulk-shortcut finding directly above means a full sweep is one `get-role` per
  role against 200+ roles in this account, sequential. CVO~Z's own fleet-wide attempt TIMED OUT
  at 60 sequential calls. So there is no fleet-level output here -- there is a per-role output
  and an untested extrapolation, and nobody can currently speak to how this tool behaves at scale.

  WHY A CONSTRAINT AND NOT A WARNING: a tool scheduled before its scale limit is understood does
  not fail loudly at 200 roles. It fails PARTIALLY -- returning a real, correctly-formatted result
  over whatever subset finished before the kill -- and A PARTIAL SWEEP WITH NO STATED DENOMINATOR
  IS INDISTINGUISHABLE FROM A COMPLETE ONE. That is the print-the-denominator class with a
  scheduler attached: it would manufacture a clean fleet-wide verdict out of a fraction of the
  fleet, wearing this module's own careful refusal language while doing it.

  PARTIAL MITIGATION SHIPPED (iam_cli.cmd_investigate_candidates): the sweep now emits a terminal
  `SWEEP COMPLETE: examined X of M intended role(s)` line, so a run killed mid-loop is missing it
  and ITS ABSENCE IS THE TELL. That closes the indistinguishability at the OUTPUT layer only --
  it does NOT lift the constraint, because a scheduler that never reads the line is unaffected.

  WHOEVER BUILDS THE FLEET PATH OWES ALL THREE: (1) batching or parallelism; (2) a denominator in
  the output (`N of M roles examined`); (3) a state for TIMED-OUT distinct from EXAMINED-AND-CLEAN.
  Those last two must never both render as absence-of-finding. Not assigned as of 2026-07-25.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

_ISO_Z = "%Y-%m-%dT%H:%M:%SZ"

# AWS-documented tracking window (see module docstring). NOT a staleness threshold -- a role
# used 350 days ago is still WITHIN this window and still gets a real, dated LastUsedDate; the
# window only governs when LastUsedDate goes null. Keep these two concepts named separately so
# neither collapses into the other.
TRACKING_WINDOW_DAYS = 400

# Staleness threshold: a JUDGMENT CALL, disclosed as one, not a documented AWS constant --
# distinguishing "recently used" from "old enough to warrant a look" is a policy choice this
# tool does not get to make silently. Configurable via --stale-days; this is only the default.
DEFAULT_STALE_DAYS = 90

# DR/break-glass exemption: declared ONCE in a checked-in file, never re-entered per run (the
# dispatch's explicit requirement). Empty by default -- no DR/break-glass role is asserted here;
# populate by editing this file when one is identified, with a reason, not by CLI habit.
_DR_EXEMPT_PATH = Path(__file__).resolve().parent / "iam_dr_exempt_roles.json"


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def load_dr_exempt(path: Path | None = None) -> dict:
    """Declared-once DR/break-glass exemption list. Missing file = empty exemption set, stated
    as such (never silently treated as 'no file means everyone is exempt' or vice versa)."""
    p = path or _DR_EXEMPT_PATH
    if not p.exists():
        return {"exempt_roles": [], "source": f"{p} (not found -- treated as empty)"}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return {"exempt_roles": [], "source": f"{p} (PARSE FAILED: {e} -- treated as empty)"}
    return {
        "exempt_roles": list(data.get("exempt_roles") or []),
        "reason": data.get("reason", ""),
        "source": str(p),
    }


def get_role_last_used(role_name: str, aws_bin: str = "aws") -> dict:
    """One `aws iam get-role` call for `role_name`. Returns {'last_used_date': str|None,
    'region': str|None, 'error': str|None}. `list-roles` does NOT populate RoleLastUsed --
    measured live, see module docstring -- so there is no cheaper bulk path.

    Lazy subprocess by design: importing this module must not require AWS. Resolves the
    executable explicitly (the `.tools/aws` Windows shim hazard -- see comp_iam_census.py's
    identical comment, lifted from the same incident class)."""
    exe = shutil.which(aws_bin) or shutil.which(aws_bin + ".cmd")
    if not exe:
        return {"last_used_date": None, "region": None,
                "error": f"AWS CLI NOT FOUND on PATH (looked for {aws_bin!r} and {aws_bin + '.cmd'!r})"}
    cmd = [exe, "iam", "get-role", "--role-name", role_name, "--output", "json"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        return {"last_used_date": None, "region": None,
                "error": f"get-role FAILED (rc={proc.returncode}): {proc.stderr.strip()[:500]}"}
    try:
        data = json.loads(proc.stdout)
    except Exception as e:  # noqa: BLE001
        return {"last_used_date": None, "region": None, "error": f"PARSE FAILED: {e}"}
    rlu = (data.get("Role") or {}).get("RoleLastUsed") or {}
    return {"last_used_date": rlu.get("LastUsedDate"), "region": rlu.get("Region"), "error": None}


def classify(role_name: str, last_used: dict, dr_exempt: set,
             stale_days: int = DEFAULT_STALE_DAYS, now: datetime | None = None) -> dict:
    """Classify ONE role into exactly one of three DISTINCT, never-collapsing states, per the
    dispatch's acceptance bar: ACTIVE / INVESTIGATE-CANDIDATE(STALE) / INVESTIGATE-CANDIDATE
    (UNKNOWN). The noun `INVESTIGATE-CANDIDATE` is the label for the latter two; it never
    stands alone without its sub-reason, and it is never rendered as `UNUSED`."""
    now = now or _utcnow()
    exempt = role_name in dr_exempt

    if last_used.get("error"):
        return {"role": role_name, "verdict": "ERROR", "detail": last_used["error"], "exempt": exempt}

    lud = last_used.get("last_used_date")
    if lud is None:
        base = {
            "role": role_name,
            "verdict": "INVESTIGATE-CANDIDATE",
            "reason": "UNKNOWN",
            "detail": (f"no LastUsedDate recorded -- NOT accessed in the {TRACKING_WINDOW_DAYS}-day "
                       f"IAM tracking window. This does NOT mean never used; it may predate the "
                       f"window, or the role may genuinely never have been used -- both render "
                       f"identically and this tool cannot distinguish them."),
        }
    else:
        try:
            dt = datetime.strptime(lud, _ISO_Z) if isinstance(lud, str) else lud
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            age_days = (now - dt).total_seconds() / 86400.0
        except Exception:
            base = {"role": role_name, "verdict": "ERROR",
                    "detail": f"LastUsedDate present but unparseable: {lud!r}", "exempt": exempt}
            return base
        region = last_used.get("region") or "UNKNOWN"
        if age_days <= stale_days:
            base = {
                "role": role_name,
                "verdict": "ACTIVE",
                "detail": (f"last used {age_days:.1f}d ago (Region: {region}, the GLOBAL "
                           f"most-recent use -- not a per-region breakdown) -- not an "
                           f"investigate-candidate."),
            }
        else:
            # NFRA_COMPIAM (2026-07-25): the sub-reason is "AGED", never the literal word the
            # dispatch forbids -- the noun a hurried reader converts into a warrant IS the
            # control, so the forbidden word must not appear anywhere in printed output, not
            # even as a qualifier paired with INVESTIGATE-CANDIDATE. Tested by grep, not trust.
            base = {
                "role": role_name,
                "verdict": "INVESTIGATE-CANDIDATE",
                "reason": "AGED",
                "detail": (f"last used {age_days:.1f}d ago (Region: {region}), exceeds the "
                           f"{stale_days}d age threshold. Still within AWS's "
                           f"{TRACKING_WINDOW_DAYS}-day tracking window, so this IS a real, "
                           f"dated observation -- distinct from the UNKNOWN/undated case."),
            }
    base["exempt"] = exempt
    return base


# NFRA_COMPIAM (2026-07-25): the forbidden nouns are absent here EVEN IN NEGATED FORM ("not
# unused") -- a literal grep for the forbidden word cannot distinguish an assertion from a
# negation, and the acceptance bar is "grep and prove zero occurrences," not "zero occurrences
# outside this one deliberate exception." Say the same thing without the word at all.
REFUSAL_LINE = (
    "THIS SURFACE IS A FLOOR, NEVER A DELETION WARRANT: RoleLastUsed observes the ROLE, not "
    "its individual STATEMENTS -- it cannot say which grants within a role were exercised. "
    "INVESTIGATE-CANDIDATE means exactly that: a human should look. It licenses no action "
    "beyond investigation, and it is never, by itself, grounds for removing a grant."
)


def self_test() -> tuple[list, bool]:
    """Offline mutant suite -- NFRA_COMPIAM (2026-07-25, CTO~Z 141322Z cheap-close dispatch).

    CVO~Z's live verify could exercise only 2 of the 4 render paths (both sampled roles were
    ACTIVE; the fleet-wide run TIMED OUT -- one get-role call per role, exactly the cost the
    07-20 design brief predicted). This suite exercises all four paths -- ABSENT/UNKNOWN,
    AGED, DR-EXEMPT, ERROR -- with SYNTHETIC records fed directly to `classify()`. It calls
    `get_role_last_used()` ZERO TIMES: no subprocess, no AWS CLI, no network, by construction
    -- a self-test that quietly hits the network is not a self-test.

    Returns (results, all_pass) where each result is (name, passed, detail).
    """
    results = []

    def check(name, cond, detail=""):
        results.append((name, bool(cond), detail))

    fixed_now = datetime(2026, 7, 25, tzinfo=timezone.utc)

    # Path 1: ABSENT/UNKNOWN -- LastUsedDate is None.
    v = classify("role-absent", {"last_used_date": None, "region": None, "error": None},
                 dr_exempt=set(), stale_days=90, now=fixed_now)
    check("absent -> INVESTIGATE-CANDIDATE",
          v["verdict"] == "INVESTIGATE-CANDIDATE", v)
    check("absent -> reason UNKNOWN, not AGED (no state collapse)",
          v.get("reason") == "UNKNOWN", v)
    check("absent -> not exempt", v["exempt"] is False, v)

    # Path 2: AGED -- LastUsedDate present, 200 days before fixed_now, threshold 90.
    old_date = datetime(2026, 1, 6, tzinfo=timezone.utc).strftime(_ISO_Z)  # 200d before fixed_now
    v = classify("role-aged", {"last_used_date": old_date, "region": "us-east-1", "error": None},
                 dr_exempt=set(), stale_days=90, now=fixed_now)
    check("aged -> INVESTIGATE-CANDIDATE",
          v["verdict"] == "INVESTIGATE-CANDIDATE", v)
    check("aged -> reason AGED, not UNKNOWN (no state collapse -- the mode most likely to be "
          "misread as safe-to-delete)", v.get("reason") == "AGED", v)
    check("aged -> not exempt", v["exempt"] is False, v)

    # Path 2b (adjacent control, not a separate path but proves the threshold discriminates):
    # the SAME shape as path 2, 10 days old instead of 200 -- must render ACTIVE, not a
    # candidate, or the AGED path is not actually testing the threshold, just the presence of
    # a date.
    recent_date = datetime(2026, 7, 15, tzinfo=timezone.utc).strftime(_ISO_Z)  # 10d before fixed_now
    v = classify("role-recent", {"last_used_date": recent_date, "region": "us-east-1", "error": None},
                 dr_exempt=set(), stale_days=90, now=fixed_now)
    check("recent (10d, threshold 90d) -> ACTIVE, not a candidate", v["verdict"] == "ACTIVE", v)

    # Path 3: DR-EXEMPT -- an aged role that is ALSO in the exemption set. Per the dispatch's
    # own design constraint, exemption must NOT suppress the real verdict -- it renders
    # alongside it, tagged, never silently hidden.
    v = classify("role-dr-exempt", {"last_used_date": old_date, "region": "us-east-1", "error": None},
                 dr_exempt={"role-dr-exempt"}, stale_days=90, now=fixed_now)
    check("DR-exempt aged role -> STILL renders INVESTIGATE-CANDIDATE (not suppressed)",
          v["verdict"] == "INVESTIGATE-CANDIDATE" and v.get("reason") == "AGED", v)
    check("DR-exempt aged role -> exempt flag set True", v["exempt"] is True, v)

    # Path 4: ERROR -- get_role_last_used() surfaced a failure (network/permissions/parse).
    v = classify("role-error", {"last_used_date": None, "region": None, "error": "get-role FAILED (rc=254): AccessDenied"},
                 dr_exempt=set(), stale_days=90, now=fixed_now)
    check("error -> verdict ERROR, not silently dropped or misclassified as UNKNOWN",
          v["verdict"] == "ERROR", v)

    # Cross-path: no two of the four paths produced the SAME (verdict, reason) pair -- the
    # explicit "no state collapses into another" bar, checked structurally, not just per-path.
    v_absent = classify("x1", {"last_used_date": None, "region": None, "error": None},
                         dr_exempt=set(), stale_days=90, now=fixed_now)
    v_aged = classify("x2", {"last_used_date": old_date, "region": "us-east-1", "error": None},
                       dr_exempt=set(), stale_days=90, now=fixed_now)
    v_active = classify("x3", {"last_used_date": recent_date, "region": "us-east-1", "error": None},
                         dr_exempt=set(), stale_days=90, now=fixed_now)
    v_error = classify("x4", {"last_used_date": None, "region": None, "error": "boom"},
                        dr_exempt=set(), stale_days=90, now=fixed_now)
    signatures = [(r["verdict"], r.get("reason")) for r in (v_absent, v_aged, v_active, v_error)]
    check("all 4 paths produce 4 DISTINCT (verdict, reason) signatures",
          len(set(signatures)) == 4, signatures)

    # NEGATIVE CONTROL: prove this suite is capable of failing, not vacuously green. A known-
    # wrong assertion (aged classified as UNKNOWN) must be caught -- checked here inline
    # (recorded as its own PASS/FAIL row: PASS means the suite correctly DETECTED the wrong
    # assertion, i.e. the deliberately-false condition evaluates False as expected).
    mutant_wrong = v_aged.get("reason") == "UNKNOWN"  # this IS false for a correct classify()
    check("NEGATIVE CONTROL: a deliberately wrong assertion (aged==UNKNOWN) correctly reads "
          "False -- proves this suite can redden, not just pass by construction",
          mutant_wrong is False, mutant_wrong)

    all_pass = all(p for _, p, _ in results)
    return results, all_pass
