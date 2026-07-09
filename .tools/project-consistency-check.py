#!/usr/bin/env python3
"""project-consistency-check -- mutual-consistency lint over org/projects/*.json + REGISTRY.md.

CTO ruling 2026-07-09T190127Z ("BUILD IT", WARN-mode first per announce-then-enforce).

WHY THIS EXISTS
---------------
Stale project records have a DIRECTION. They do not decay randomly -- they decay
toward RE-INVITING COMPLETED WORK, because the text left behind is the text
written while the work was still open. That is a systematic bias, not noise.

Three independent stale records on 2026-07-09 all drifted that way:
  * NFRA_COMPAWS `blocking:` still read "ACTIVE capacity-gated build-ramp"
    (superseded 06-18) beside `status: inactive` + `phase: DEPRIORITIZED...PARKED`.
    That line briefed a live agent to "ramp it". Both its TOs were complete.
  * A commit message said "Staged, NOT yet deployed" for code whose deployed
    sha256 already equalled HEAD.
  * A ledger recorded a restore that the worktree contradicted.
CTO independently hit the same class three times in one hour (NFRA_SYSTEM,
NFRA_TOOLCHECK, NFRA_ENDPOINTS: `status=complete` beside a `blocking:` narrating
in-flight work) and nearly reopened a finished project.

None of them had a gate. This is the gate for the mechanically-detectable subset.

WHAT IT CHECKS
--------------
ERRORS (the 2-step atomic close, per org/XXX.md "Closure Discipline"):
  E1  terminal status but no `completed` date        -- the JSON half is incomplete
  E2  terminal status but still in REGISTRY "Active" -- the ADVI_ROLGAT drift class
  E3  terminal status but absent from REGISTRY "Completed / Archived"
  E4  non-terminal status but listed in REGISTRY "Completed / Archived"
  E5  malformed JSON -- SURFACED, never silently dropped

WARNINGS (heuristic; would over-block if enforced):
  W1  terminal/parked status beside `blocking:` narrating in-flight work
  W2  `status:` outside the sanctioned vocabulary

E2/E3/E4 are the two-step close made checkable: org/XXX.md requires the JSON
status flip and the REGISTRY row move to land in ONE commit. Either alone is
silent drift to the other.

MODES
-----
  (default)  WARN  -- report everything, exit 0. announce-then-enforce.
  --strict         -- exit 1 if any ERROR. Wire into a gate once the backlog clears.
  --quiet          -- only ERRORs.
  --json           -- machine-readable.

Read-only. Never writes. ASCII only (CLAUDE.md Code Quality).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# org/XXX.md "Closure Discipline" names four terminal dispositions. The estate
# has drifted to 11 distinct status strings; W2 surfaces that rather than
# pretending the vocabulary is clean.
TERMINAL = {"complete", "closed", "cancelled", "merged", "complete-as-superseded"}
SANCTIONED = TERMINAL | {"active", "inactive", "on_hold", "on-hold"}

# Language that describes work still moving. Deliberately broader than CTO's
# original "^ACTIVE|in flight|dispatched|pending": ADVI_BFIX4 is `inactive` with
# blocking "TO-2 RULED DO IT ... Next: CTO authors the BFIX4 PRD" -- in-flight
# prose that an anchored ^ACTIVE regex misses entirely.
INFLIGHT = re.compile(
    r"(^\s*ACTIVE\b|in[- ]flight|dispatched|^\s*pending\b|\bNext\s*:|\bunderway\b"
    r"|ramps?\s+as\b|capacity-gated\s+build-ramp)",
    re.IGNORECASE | re.MULTILINE,
)

REG_SECTIONS = {
    "active": "## Active Projects",
    "inactive": "## Inactive / On Hold",
    "completed": "## Completed / Archived Projects",
}

NON_ASCII = re.compile(r"[^\x00-\x7F]")


def ascii_safe(s: str) -> str:
    """Render a record's text printable on a Windows charmap console.

    A lint MUST survive the defect it reports. Several project JSONs carry
    non-ASCII (U+2192 arrows, mojibake) in `blocking`/`phase`. Echoing them
    verbatim raised UnicodeEncodeError mid-report, so main() returned 0 while
    the PROCESS exited 1 -- an advisory-mode lint that silently failed closed.
    Caught by running it, not by reading it. Rule W3 now reports the same
    characters this function neutralizes.
    """
    return NON_ASCII.sub("?", s)


def parse_registry(path: Path) -> dict:
    """Map each REGISTRY section -> set of project codes in its table.

    Tolerant by design: a row is any '| CODE |' line under a section heading.
    Never raises on a malformed row -- a lint that dies on bad input reports
    nothing, which is the failure mode it exists to prevent.
    """
    out = {k: set() for k in REG_SECTIONS}
    if not path.is_file():
        return out
    current = None
    order = list(REG_SECTIONS.items())
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = line.strip()
        matched = False
        for key, heading in order:
            if stripped.startswith(heading):
                current, matched = key, True
                break
        if matched:
            continue
        if stripped.startswith("## "):
            current = None
            continue
        if current and stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not cells:
                continue
            code = cells[0].strip("* `")
            # skip header + separator rows
            if not code or code.lower().startswith(("project code", "code", "---", ":--")):
                continue
            if re.match(r"^[A-Z0-9_]{3,}$", code):
                out[current].add(code)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Mutual-consistency lint for org/projects/*.json")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any ERROR")
    ap.add_argument("--quiet", action="store_true", help="only print ERRORs")
    ap.add_argument("--json", dest="as_json", action="store_true", help="machine-readable output")
    ap.add_argument("--root", default=".", help="repo root")
    args = ap.parse_args()

    root = Path(args.root)
    pdir = root / "org" / "projects"
    registry = parse_registry(pdir / "REGISTRY.md")

    errors: list[tuple] = []
    warns: list[tuple] = []

    for f in sorted(pdir.glob("*.json")):
        name = f.name
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001 -- surface, never drop
            errors.append(("E5", name, f"malformed JSON: {type(e).__name__}: {e}"))
            continue
        if not isinstance(d, dict):
            errors.append(("E5", name, "top-level JSON is not an object"))
            continue

        code = str(d.get("project_code") or f.stem)
        status = str(d.get("status") or "").strip().lower()
        blocking = str(d.get("blocking") or "")
        completed = d.get("completed")
        is_terminal = status in TERMINAL

        if status and status not in SANCTIONED:
            warns.append(("W2", name, f"status={status!r} is outside the sanctioned vocabulary"))

        if is_terminal and not completed:
            errors.append(("E1", name, f"status={status!r} but no `completed` date (JSON half of the 2-step close)"))

        if is_terminal and code in registry["active"]:
            errors.append(("E2", name, f"status={status!r} but still listed under REGISTRY '## Active Projects'"))

        if is_terminal and registry["completed"] and code not in registry["completed"]:
            errors.append(("E3", name, f"status={status!r} but absent from REGISTRY '## Completed / Archived Projects'"))

        if (not is_terminal) and code in registry["completed"]:
            errors.append(("E4", name, f"status={status!r} but listed under REGISTRY '## Completed / Archived Projects'"))

        if status in TERMINAL | {"inactive", "on_hold", "on-hold"} and blocking:
            m = INFLIGHT.search(blocking)
            if m:
                snippet = blocking[: max(0, m.start())][-24:] + blocking[m.start(): m.start() + 46]
                warns.append(("W1", name, f"status={status!r} but blocking narrates in-flight work: ...{ascii_safe(snippet.strip())!r}"))

        # CLAUDE.md Code Quality: no non-ASCII in records -- it breaks charmap
        # consoles, grep, and CI stdout. This lint crashed on U+2192 before the
        # rule existed; the crash IS the evidence for the rule.
        for field in ("blocking", "phase", "name", "description"):
            val = d.get(field)
            if isinstance(val, str):
                found = NON_ASCII.findall(val)
                if found:
                    pts = ", ".join(sorted({f"U+{ord(c):04X}" for c in found})[:4])
                    warns.append(("W3", name, f"non-ASCII in `{field}` ({pts}) -- breaks charmap/grep/CI stdout"))
                    break

    if args.as_json:
        print(json.dumps({
            "errors": [{"rule": r, "file": f, "detail": m} for r, f, m in errors],
            "warnings": [{"rule": r, "file": f, "detail": m} for r, f, m in warns],
        }, indent=2))
        return 1 if (args.strict and errors) else 0

    total = len(list(pdir.glob("*.json")))
    print(f"project-consistency-check -- {total} project JSON(s), REGISTRY: "
          f"{len(registry['active'])} active / {len(registry['completed'])} completed rows")
    print()

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for rule, f, msg in errors:
            print(f"  {rule}  {f:<30} {ascii_safe(msg)}")
        print()
    if warns and not args.quiet:
        print(f"WARNINGS ({len(warns)}):")
        for rule, f, msg in warns:
            print(f"  {rule}  {f:<30} {ascii_safe(msg)}")
        print()

    if not errors and not warns:
        print("OK: no mutual-consistency violations.")
        return 0

    if args.strict and errors:
        print(f"ERROR: {len(errors)} consistency violation(s). Exit 1 (--strict).")
        return 1

    print(f"WARN: {len(errors)} error(s), {len(warns)} warning(s). "
          f"Advisory mode -- rerun with --strict to enforce.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
