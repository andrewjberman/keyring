#!/usr/bin/env python3
"""to-decomp-ref-lint -- PIPELINE GATE LAYER 2: a NEW task order for a pipeline-registered
project must carry <decomp_ref>.

org/ref/DIRECTIVE_EXECUTION_PIPELINE.md:171 ("build routed", tooling lane; Andrew's word
granted in the ratification). Built 2026-08-24 by 0.8.0_AE_CloudComp~F.

THE CHOKE-POINT PRINCIPLE (:164): nothing executes without a TO. A TO that conformantly
requires a decomp_ref structurally requires the decomp, which requires the PRD, which
requires registration -- so ONE gate at TO issuance enforces the whole upstream funnel
without taxing any other act. This is that gate. It teaches at violation time, which is
why the refusal prints the rule and the fix rather than a code.

SCOPE, deliberately narrow on three axes -- each one is a way this gate could have
become a tax on work it was never meant to touch:
  1. NEW FILES ONLY (git --diff-filter=A). Editing an existing TO is not issuance, and
     retro-fitting <decomp_ref> onto TOs whose criteria were never derived from cells
     produces exactly the false alignment the layer-1 checker refuses.
  2. PIPELINE-REGISTERED PROJECTS ONLY (a dep_stage key in org/projects/{CODE}.json --
     10 of 326 projects on 2026-08-24). dep_stage is OPTIONAL and FORWARD-ONLY by its own
     ratified design; a project that never opted in is not in this gate's scope.
  3. FILES UNDER **/task_orders/ ONLY.
A file failing any of the three is NOT a pass -- it is OUT OF SCOPE, and the report says
which, because "no findings" and "did not look" must never render identically.

RAMP: ANNOUNCE by default; ENFORCE when org/mcp/pipeline-gate2.enforce exists (the
NFRA_COMPRAIL announce-then-enforce shape, marker-file checked, so arming is one
reviewable act and not a code change). Under ANNOUNCE this prints findings and exits 0.
  ⛔ THE MARKER IS THE AUTHORITY, NEVER A COMMENT ABOUT THE MARKER. Rule 21 records the
  measured cost of the inverse: an agent read a stale ramp COMMENT instead of the armed
  marker and reported a live gate as not-yet-enforcing.

OVERRIDE: audited, and it must be a DELIBERATE SENTENCE, not a flag. Put
`# pipeline-gate2-override: <reason>` in the commit message; every use is appended to
org/mcp/pipeline-gate2-override.log with the file and the reason. A repeat override for
one recurring intent is a COVERAGE GAP, not a habit -- route it, do not keep overriding.

Usage:
  to-decomp-ref-lint [--enforce] [--override-reason TEXT] [paths...]
    no paths -> the STAGED ADDED files (git diff --cached --diff-filter=A --name-only)
Exit 0 = clean, out-of-scope, or ANNOUNCE. Exit 1 = REFUSED (enforce). Exit 2 = usage/git error.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
PROJECTS = WORKSPACE / "org" / "projects"
ENFORCE_MARKER = WORKSPACE / "org" / "mcp" / "pipeline-gate2.enforce"
OVERRIDE_LOG = WORKSPACE / "org" / "mcp" / "pipeline-gate2-override.log"

DECOMP_REF_RE = re.compile(r"<decomp_ref>(.*?)</decomp_ref>", re.S)
CELL_ID_RE = re.compile(r"\b[A-Z][A-Z0-9]*-[a-z]{1,4}-[a-z]?\d+\b")
TO_ID_RE = re.compile(r'<task_order\b[^>]*\bid\s*=\s*"([^"]+)"')
PROJECT_ATTR_RE = re.compile(r'<task_order\b[^>]*\bproject\s*=\s*"([^"]+)"')
PROJECT_TAG_RE = re.compile(r"<project(?:_code)?>(.*?)</project(?:_code)?>", re.S)


def staged_added() -> list[str]:
    try:
        out = subprocess.run(
            ["git", "diff", "--cached", "--diff-filter=A", "--name-only"],
            cwd=WORKSPACE, capture_output=True, text=True, check=True).stdout
    except Exception as exc:  # noqa: BLE001
        print(f"to-decomp-ref-lint: GIT-ERROR {exc}", file=sys.stderr)
        raise
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def is_task_order(rel: str) -> bool:
    p = Path(rel.replace("\\", "/"))
    return "task_orders" in p.parts and p.suffix.lower() == ".md"


def project_code(text: str, rel: str) -> tuple[str, str]:
    """(code, how). PRECEDENCE MATCHES to-check.py's FIX B: the TO's own DECLARED project
    wins; the id-derived code is the fallback. Deriving first would make the declared
    field dead code -- the exact bug to-check.py carried and fixed."""
    m = PROJECT_ATTR_RE.search(text) or PROJECT_TAG_RE.search(text)
    if m:
        c = re.match(r"^([A-Z][A-Z0-9_]{2,})", m.group(1).strip().upper())
        if c:
            return c.group(1), "declared on the task_order"
    m = TO_ID_RE.search(text)
    if m:
        return m.group(1).split(".", 1)[0].strip().upper(), "derived from task_order id"
    stem = Path(rel).name
    c = re.match(r"^([A-Z][A-Z0-9_]{2,})", stem.upper())
    if c:
        return c.group(1), "derived from FILENAME (weakest -- the TO declares no project)"
    return "", "unresolved"


def dep_stage(code: str) -> str | None:
    f = PROJECTS / f"{code}.json"
    if not f.is_file():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8")).get("dep_stage")
    except Exception:  # noqa: BLE001
        return None


def audit_override(reason: str, files: list[str]) -> None:
    try:
        OVERRIDE_LOG.parent.mkdir(parents=True, exist_ok=True)
        stamp = subprocess.run(["git", "log", "-1", "--format=%cI"], cwd=WORKSPACE,
                               capture_output=True, text=True).stdout.strip()
        with OVERRIDE_LOG.open("a", encoding="utf-8") as fh:
            fh.write(f"{stamp}\tOVERRIDE\t{','.join(files)}\t{reason}\n")
    except Exception as exc:  # noqa: BLE001
        # An unwritable audit log must be LOUD: an override nobody can see is not audited.
        print(f"  [gate2] WARN: override audit log NOT written ({exc}) -- the override "
              f"is UNAUDITED", file=sys.stderr)


def main(argv: list[str]) -> int:
    enforce = "--enforce" in argv or ENFORCE_MARKER.is_file()
    reason = ""
    args = []
    it = iter([a for a in argv if a != "--enforce"])
    for a in it:
        if a == "--override-reason":
            reason = next(it, "").strip()
        else:
            args.append(a)

    paths = args if args else staged_added()
    considered = len(paths)
    in_scope = [p for p in paths if is_task_order(p)]

    findings: list[str] = []
    checked = 0
    out_of_scope_unregistered = 0
    for rel in in_scope:
        f = WORKSPACE / rel
        if not f.is_file():
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        code, how = project_code(text, rel)
        stage = dep_stage(code) if code else None
        if not stage:
            out_of_scope_unregistered += 1
            continue
        checked += 1
        m = DECOMP_REF_RE.search(text)
        if not m:
            findings.append(
                f"{rel}\n"
                f"      project {code} ({how}) is PIPELINE-REGISTERED (dep_stage={stage}), so this\n"
                f"      NEW task order must carry <decomp_ref> naming the stage-3 decomp run and\n"
                f"      the cells it discharges. It carries none.\n"
                f"      FIX: <decomp_ref>workflows/atom_decomposition/runs/<run>/DECOMP.md -- cells "
                f"X-a-1, X-a-2</decomp_ref>\n"
                f"      WHY: nothing executes without a TO, so requiring the ref HERE requires the\n"
                f"      decomp, the PRD and the registration behind it -- one gate at the neck\n"
                f"      (DIRECTIVE_EXECUTION_PIPELINE.md:164). If no decomp exists yet, that is a\n"
                f"      PIPELINE FAILURE TO SURFACE to COO/CTO, not a reason to cut the TO without one.")
            continue
        if not CELL_ID_RE.search(m.group(1)):
            findings.append(
                f"{rel}\n"
                f"      project {code} ({how}, dep_stage={stage}) carries a <decomp_ref> that names\n"
                f"      NO CELL IDS -- a decomp path alone cannot be joined to any criterion, so the\n"
                f"      layer-1 alignment check has nothing to close against.\n"
                f"      FIX: name the cells this TO discharges inside the <decomp_ref>.")

    mode = "ENFORCE" if enforce else "ANNOUNCE"
    print(f"to-decomp-ref-lint | mode={mode} | considered={considered} file(s), "
          f"{len(in_scope)} under task_orders/, {checked} on pipeline-registered projects, "
          f"{out_of_scope_unregistered} skipped (project not pipeline-registered) | "
          f"findings={len(findings)}")
    for fnd in findings:
        print(f"  REFUSED: {fnd}")

    if not findings:
        return 0
    if reason:
        audit_override(reason, [f.splitlines()[0] for f in findings])
        print(f"  [gate2] OVERRIDDEN (audited -> {OVERRIDE_LOG.relative_to(WORKSPACE)}): {reason}")
        print("  [gate2] A repeat override for one recurring intent is a COVERAGE GAP -- route it.")
        return 0
    if not enforce:
        print("  [gate2] ANNOUNCE mode -- NOT blocking this commit. Arm by creating "
              f"{ENFORCE_MARKER.relative_to(WORKSPACE)}.")
        return 0
    print("  [gate2] BLOCKED. Fix the TO, or state an audited reason with "
          "'# pipeline-gate2-override: <reason>' in the commit message.")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as exc:  # noqa: BLE001
        print(f"to-decomp-ref-lint: ERROR {exc}", file=sys.stderr)
        sys.exit(2)
