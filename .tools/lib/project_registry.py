#!/usr/bin/env python3
"""project_registry -- THE ONLY SANCTIONED WAY TO READ org/projects/*.json.

F-013 (RV-0046). Arch: 1.0.0_SA_CTO. Build: 2.0.0_SA_COO. Bar: MSTR + CTO.

=============================================================================
WHY THIS EXISTS, AND WHY IT IS A LOADER RATHER THAN A LIST
=============================================================================
Andrew, 2026-07-10, verbatim: "just exclude those items, we will deal with them
later."  Four projects are under a SOVEREIGN HOLD. The interim enforcement was a
hardcoded list inside ONE consumer (/drive Step 2). Every other consumer could
still re-expose the class.

FILTER AT THE READ, NOT AT THE RENDER.
  Exclusion is a property of DATA ACCESS, not of PRESENTATION.
  A consumer cannot obtain the raw list, so it CANNOT FORGET TO FILTER IT.
  If a consumer can get the unfiltered list, it will eventually print it.

THE REGISTRY IS A FIELD ON THE PROJECT, NOT A SIDECAR LIST.
  `sovereign_excluded: true` lives on org/projects/{CODE}.json itself.
  A sidecar list is a JOIN, and A JOIN CAN DRIFT -- rename or split the project and
  the list silently stops matching. A colocated field cannot drift.
  Adding a fifth project = ONE JSON EDIT, ZERO CONSUMER CHANGES.

DEFAULT-DENY.
  The safe path is the DEFAULT. The unsafe path must be TYPED OUT, carries a
  written reason, and is AUDITED. Same shape as `# never-override:`.

=============================================================================
THE CONSUMER COUNT WAS WRONG AND THAT IS THE POINT
=============================================================================
The arch was written against "all four consumers" (/drive, /fabric-check,
/overview, /registry-check). A census BY FUNCTION -- who actually OPENS the file,
not who mentions the word -- found ELEVEN:

    activity-check  fabric-check  fabric-commits  fabric-projects  loop-resolve
    operator  prd-check  prd-delta  project-consistency-check  to-check  validator

CENSUS BY FUNCTION, NEVER BY MENTION (CTO, 9b68f4466). A mention-count returns 13 --
it over-reports two and would have missed any consumer reading via a helper. The
exclusion surface is ~3x what everyone believed, which is precisely the argument for
a loader: hand-wiring eleven consumers is worse than hand-wiring four, and consumer
twelve is written next month by someone who has never heard of the hold.

=============================================================================
ACCEPTANCE (CTO, supersedes MSTR's -- his is folded in as case 1)
=============================================================================
1. A fifth project marked excluded -> invisible in every consumer, ZERO consumer
   code changed.                                                    (MSTR's bar)
2. A NEWLY-WRITTEN consumer that uses this loader is excluded WITHOUT ITS AUTHOR
   KNOWING THE HOLD EXISTS.
3. A consumer that BYPASSES the loader FAILS A GATE.   <- makes it structural, not
   voluntary. THAT GATE IS NOT YET BUILT (see GAP below). Until it lands, (1) and
   (2) are real but VOLUNTARY.
4. MUTANT BAR: delete the exclusion field from a project JSON -> that project
   REAPPEARS. A FILTER NEVER OBSERVED TO HIDE ANYTHING HAS NOT BEEN SHOWN TO FILTER.
   See tests/test_project_registry.py.

=============================================================================
GAP -- STATED, NOT PAPERED OVER
=============================================================================
Acceptance (3) -- the gate that FAILS a tool for opening org/projects/*.json
directly -- is NOT BUILT. Without it, consumer #12 simply does not call this loader
and the whole thing is decoration. This module is NECESSARY AND NOT SUFFICIENT.
Do not record F-013 as closed on the strength of this file alone.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent.parent
PROJECTS_DIR = ROOT / "org" / "projects"
AUDIT_LOG = ROOT / "org" / "mcp" / "sovereign-registry-override-audit.log"

EXCLUDE_FIELD = "sovereign_excluded"
REASON_FIELD = "sovereign_reason"


class SovereignOverrideError(RuntimeError):
    """Raised when an unfiltered read is attempted without a written reason."""


def _audit(actor: str, reason: str, count: int) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"{ts}\tSOVEREIGN_UNFILTERED_READ\tactor={actor}\tn_excluded={count}\treason={reason}\n"
    try:
        AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
        with AUDIT_LOG.open("a", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        # Never let an audit-write failure silently DROP the override -- surface it.
        print(f"WARN: could not write sovereign override audit: {line.strip()}")


def _actor() -> str:
    return os.environ.get("OPAL_AGENT_SERIAL") or "UNKNOWN"


def load_projects(
    *,
    include_sovereign_excluded: bool = False,
    reason: str = "",
) -> list[dict[str, Any]]:
    """Every project dict, SOVEREIGN-EXCLUDED ONES REMOVED BY DEFAULT.

    This is the only sanctioned read of org/projects/*.json.

    To read the excluded ones you must say so out loud AND say why:
        load_projects(include_sovereign_excluded=True, reason="RV-0047 audit")
    That call is AUDITED. There is no silent unfiltered read.
    """
    if include_sovereign_excluded and not reason.strip():
        raise SovereignOverrideError(
            "include_sovereign_excluded=True requires a written `reason`. "
            "The sovereign hold is not bypassed by accident, and an unexplained "
            "bypass is indistinguishable from a mistake."
        )

    out: list[dict[str, Any]] = []
    excluded = 0
    for path in sorted(PROJECTS_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            # A malformed project is SURFACED, never silently dropped -- a project
            # that vanishes because its JSON broke is the same blindness we are fixing.
            print(f"WARN: unreadable project {path.name}: {exc}")
            continue
        if not isinstance(data, dict):
            print(f"WARN: project {path.name} is not an object -- skipped")
            continue
        data.setdefault("code", path.stem)
        if data.get(EXCLUDE_FIELD) is True:
            excluded += 1
            if not include_sovereign_excluded:
                continue
        out.append(data)

    if include_sovereign_excluded and excluded:
        _audit(_actor(), reason.strip(), excluded)
    return out


def active_projects(**kw: Any) -> list[dict[str, Any]]:
    """Projects with status == 'active', sovereign-excluded removed by default."""
    return [p for p in load_projects(**kw) if p.get("status") == "active"]


def load_project(
    code: str,
    *,
    include_sovereign_excluded: bool = False,
    reason: str = "",
) -> dict[str, Any] | None:
    """ONE project by code. Returns None if absent OR sovereign-excluded.

    ===================================================================
    THE SECOND READ PATH -- the loader shipped without it and was HALF A FILTER.
    ===================================================================
    The enumerating consumers glob the directory; load_projects() (PLURAL) covers them.
    But operator.py and validator.py do:

        path = PROJECTS_DIR / f"{code}.json"

    -- a DIRECT read by code. It never touches the glob and sails straight past a filter
    that guards only enumeration. And those two are not display tools: THEY ARE THE
    DRIVERS. `operator DATA_SSOTMG` would DRIVE a sovereign-held project with the
    exclusion nominally "in place." Observed live before this landed.

        A FILTER ON THE LIST IS NOT A FILTER ON THE ITEM.

    NAMING NOTE, and it cost real time: this function is `load_project` and its sibling
    is `load_projects`. A `grep -c "def load_project"` MATCHES BOTH -- the singular is a
    substring of the plural -- so a check for "does the singular exist?" returns 1 when
    only the plural does. Use `grep "def load_project("` (with the paren). The verifier
    that confirmed this function existed, when it did not, was itself a mention-match.
    """
    if include_sovereign_excluded and not reason.strip():
        raise SovereignOverrideError(
            "include_sovereign_excluded=True requires a written `reason`."
        )
    path = PROJECTS_DIR / f"{code}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    data.setdefault("code", code)
    if data.get(EXCLUDE_FIELD) is True:
        if not include_sovereign_excluded:
            return None
        _audit(_actor(), reason.strip(), 1)
    return data


def is_sovereign_excluded(code: str) -> bool:
    """Is this project code under the sovereign hold? (Reads the FIELD, not a list.)"""
    path = PROJECTS_DIR / f"{code}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return bool(isinstance(data, dict) and data.get(EXCLUDE_FIELD) is True)


def sovereign_codes() -> list[str]:
    """The excluded codes -- for a tool that must NAME the hold rather than hide it.

    Used by anything that needs to say "N projects are withheld" honestly. Naming the
    count is not exposing the class; SILENTLY dropping them would be the dishonesty.
    """
    codes = []
    for path in sorted(PROJECTS_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and data.get(EXCLUDE_FIELD) is True:
            codes.append(path.stem)
    return codes
