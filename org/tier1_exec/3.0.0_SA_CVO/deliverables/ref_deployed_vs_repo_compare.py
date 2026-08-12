#!/usr/bin/env python3
"""REFERENCE IMPLEMENTATION -- deployed-vs-repo comparison that does NOT cry wolf.

Handed to 0.7.0_AE_CloudOps / 2.0.0_SA_COO for the deployed-vs-built-from census
(CVO 151825Z + AE's 152011Z caveat, which CORRECTS the naive form). NOT a registered
comp-tool and NOT a standing job -- a reference for the census to absorb, run-and-read.

THE THREE THINGS IT ENCODES
1. ARTIFACT-KIND-AWARE NORMALISATION (AE's caveat -- blanket normalisation is its own
   defect). For INTERPRETED-BY-IMPORT artifacts (.py) a CRLF-vs-LF delta is cosmetic:
   normalise, else you get a PERMANENT false STALE that can never clear. For
   EXECUTED-BY-SHEBANG artifacts (.sh) CRLF IS THE DEFECT -- a Linux runner dies with
   `/bin/bash^M: bad interpreter` -- so compare RAW and report a line-ending delta as a
   REAL finding. Normalising it away would silence the one comparison that matters
   (live class: inf-bronze-fetch.sh, mdpf-daily-dispatch.sh).
2. CLASSIFY BY RESIDUAL CONTENT, NEVER BY MARKER TEXT (AE's encode judgement). A
   residual consisting SOLELY of repo-only COMMENT lines that DECLARE a hold is
   DELIBERATELY-HELD, not drift. Generalises past any one marker string.
3. A STATE SPACE WIDER THAN DRIFT/CLEAN (Rule 24 -- get the states right before the
   control; a two-value census forces a confident wrong answer on a third state).

DECLARED BLIND SPOT (AE): the hold marker lives in the REPO and is absent from the
DEPLOYED copy, so the declaration travels WITH THE SOURCE and a census can read it. The
REVERSE -- a marker present only in the deployed artifact -- is INVISIBLE to this check.
Stated so a reader knows which direction it can see.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

# The state space, named before the control (point 3).
IDENTICAL = "IDENTICAL"                    # raw bytes equal
COSMETIC_LINE_ENDINGS = "COSMETIC-LINE-ENDINGS"   # .py only; equal after normalisation
DELIBERATELY_HELD = "DELIBERATELY-HELD"    # residual is only repo-only hold-declaring comments
DRIFT = "DRIFT"                            # real content divergence
LINE_ENDING_DEFECT = "LINE-ENDING-DEFECT"  # .sh with CRLF -- functional, not cosmetic
ABSENT = "ABSENT"                          # no deployed counterpart (never-deployed / not-in-change)

_HOLD_RE = re.compile(r"\b(HELD|HOLD|DEPLOY-SERVE-HELD|DO NOT DEPLOY|PENDING)\b", re.I)


def _sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:10]


def classify(deployed: bytes | None, repo: bytes, name: str) -> tuple:
    """Returns (state, detail). Every branch prints its own denominator upstream."""
    if deployed is None:
        return ABSENT, "no deployed counterpart -- never-deployed OR not-in-this-change (a census with only DRIFT/CLEAN cannot tell these apart)"
    if deployed == repo:
        return IDENTICAL, f"raw sha {_sha(repo)}"

    shebang_executed = name.endswith(".sh")
    dep_n, repo_n = deployed.replace(b"\r\n", b"\n"), repo.replace(b"\r\n", b"\n")
    line_ending_delta = (dep_n != deployed) or (repo_n != repo)

    # (1) .sh -- CRLF is FUNCTIONAL. Do not normalise it away.
    if shebang_executed and line_ending_delta:
        return LINE_ENDING_DEFECT, (
            "CRLF in a shebang-executed artifact -- a Linux runner fails with "
            "'bad interpreter'. This is the defect itself, NOT cosmetic; reported RAW "
            "deliberately (normalising here would hide the only difference that matters)")

    if dep_n == repo_n:
        return (COSMETIC_LINE_ENDINGS,
                f"equal after normalisation ({len(repo_n.splitlines())} lines); raw differed by "
                f"{abs(len(deployed) - len(repo))} bytes = the CRLF signature. A raw-hash comparator "
                f"reports this STALE PERMANENTLY -- it can never clear, because no deploy makes the "
                f"bytes match.")

    # (2) residual content decides -- never the marker's text
    dep_lines, repo_lines = dep_n.decode("utf-8", "replace").splitlines(), repo_n.decode("utf-8", "replace").splitlines()
    repo_only = [ln for ln in repo_lines if ln not in set(dep_lines)]
    dep_only = [ln for ln in dep_lines if ln not in set(repo_lines)]
    residual = [ln for ln in repo_only + dep_only if ln.strip()]
    if residual and not dep_only and all(ln.lstrip().startswith("#") for ln in residual) \
            and any(_HOLD_RE.search(ln) for ln in residual):
        return DELIBERATELY_HELD, (
            f"residual is {len(residual)} repo-only COMMENT line(s) DECLARING a hold -- the file "
            f"states its own disposition: {residual[0].strip()[:90]}")
    return DRIFT, f"{len(residual)} substantive differing line(s) survive normalisation; first: {(residual or ['<whitespace only>'])[0].strip()[:90]}"


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: ref_deployed_vs_repo_compare.py <deployed_file> <repo_file>")
        return 2
    dep_p, repo_p = Path(sys.argv[1]), Path(sys.argv[2])
    deployed = dep_p.read_bytes() if dep_p.exists() else None
    repo = repo_p.read_bytes()
    state, detail = classify(deployed, repo, repo_p.name)
    print(f"{repo_p.name}: {state}\n  {detail}")
    print(f"  DENOMINATOR: repo {len(repo):,} B / deployed "
          f"{len(deployed):,} B" if deployed is not None else "  DENOMINATOR: deployed ABSENT")
    return 0 if state in (IDENTICAL, COSMETIC_LINE_ENDINGS, DELIBERATELY_HELD) else 1


if __name__ == "__main__":
    sys.exit(main())
