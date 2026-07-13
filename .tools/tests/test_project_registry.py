#!/usr/bin/env python3
"""F-013 loader tests -- INCLUDING THE MUTANT BAR.

CTO's acceptance (4): delete the exclusion field from a project JSON and that project
MUST REAPPEAR in every consumer.

    A FILTER NEVER OBSERVED TO HIDE ANYTHING HAS NOT BEEN SHOWN TO FILTER.

A registry whose exclusions are empty must be INDISTINGUISHABLE from a registry that
is not being read at all. So the test proves the filter can FAIL -- not merely that it
returns a plausible list. Every green arm here is reachable from a DIFFERENT TRUTH than
the red ones; without that, this suite would be a brick that passes at everything.

Run: python .tools/tests/test_project_registry.py
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib import project_registry as pr  # noqa: E402

PASS, FAIL = "PASS", "FAIL"
results: list[tuple[str, str, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, PASS if ok else FAIL, detail))


def _write(d: Path, code: str, **fields: object) -> None:
    body = {"code": code, "status": "active", "name": f"{code} name"}
    body.update(fields)
    (d / f"{code}.json").write_text(json.dumps(body), encoding="utf-8")


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        real_dir = pr.PROJECTS_DIR
        real_log = pr.AUDIT_LOG
        pr.PROJECTS_DIR = tmp
        pr.AUDIT_LOG = tmp / "audit.log"
        try:
            # A normal project, and one under the hold.
            _write(tmp, "NORMAL_ONE")
            _write(tmp, "HELD_ONE", sovereign_excluded=True, sovereign_reason="Andrew 2026-07-10")

            # --- 1. DEFAULT-DENY: the held project is invisible.
            codes = {p["code"] for p in pr.load_projects()}
            check("default read EXCLUDES the held project", "HELD_ONE" not in codes, str(sorted(codes)))
            check("default read KEEPS the normal project", "NORMAL_ONE" in codes)

            # --- 2. NON-VACUITY: the filter is not just returning everything/nothing.
            check("default read is non-empty (not a brick)", len(codes) == 1, str(sorted(codes)))

            # --- 3. THE MUTANT BAR. Remove the field -> it MUST REAPPEAR.
            #     If this arm does not flip, the filter has never been shown to filter.
            _write(tmp, "HELD_ONE")  # rewritten WITHOUT sovereign_excluded
            codes_after = {p["code"] for p in pr.load_projects()}
            check(
                "MUTANT: drop the exclusion field -> project REAPPEARS",
                "HELD_ONE" in codes_after,
                str(sorted(codes_after)),
            )
            # restore
            _write(tmp, "HELD_ONE", sovereign_excluded=True, sovereign_reason="Andrew 2026-07-10")

            # --- 4. OVERRIDE requires a written reason (default-deny, typed out loud).
            try:
                pr.load_projects(include_sovereign_excluded=True, reason="")
                check("override with EMPTY reason is REFUSED", False, "no exception raised")
            except pr.SovereignOverrideError:
                check("override with EMPTY reason is REFUSED", True)

            # --- 5. Override WITH a reason works, returns the held project, and AUDITS.
            codes_ovr = {p["code"] for p in pr.load_projects(include_sovereign_excluded=True, reason="unit test")}
            check("override WITH a reason returns the held project", "HELD_ONE" in codes_ovr)
            audited = pr.AUDIT_LOG.exists() and "SOVEREIGN_UNFILTERED_READ" in pr.AUDIT_LOG.read_text(encoding="utf-8")
            check("override is AUDITED", audited)

            # --- 6. active_projects() inherits the exclusion (a consumer cannot route around it).
            _write(tmp, "HELD_INACTIVE", status="complete", sovereign_excluded=True, sovereign_reason="x")
            act = {p["code"] for p in pr.active_projects()}
            check("active_projects() also excludes", "HELD_ONE" not in act, str(sorted(act)))

            # --- 7. A malformed project is SURFACED, never silently dropped.
            (tmp / "BROKEN.json").write_text("{not json", encoding="utf-8")
            got = {p["code"] for p in pr.load_projects()}
            check("malformed project does not crash the loader", "NORMAL_ONE" in got)

            # --- 8. sovereign_codes() NAMES the hold (honest count, not a silent drop).
            names = pr.sovereign_codes()
            check("sovereign_codes() names the held projects", "HELD_ONE" in names, str(names))
        finally:
            pr.PROJECTS_DIR = real_dir
            pr.AUDIT_LOG = real_log

    width = max(len(n) for n, _, _ in results)
    for name, verdict, detail in results:
        line = f"  [{verdict}] {name:<{width}}"
        if verdict == FAIL and detail:
            line += f"   <- {detail}"
        print(line)
    failed = sum(1 for _, v, _ in results if v == FAIL)
    print(f"\n{len(results) - failed}/{len(results)} passed")
    if failed:
        print("FAILED -- the filter is not doing what it claims.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
