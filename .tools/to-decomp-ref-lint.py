#!/usr/bin/env python3
"""to-decomp-ref-lint -- the L6 issuance gate of the canonical fabric workflow: a NEW task order for a dep_stage-registered
project must carry <decomp_ref>.

org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md ("build routed", tooling lane; Andrew's word
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
     produces exactly the false alignment the L7 completion checker refuses.
  2. WORKFLOW-REGISTERED PROJECTS ONLY (a dep_stage key in org/projects/{CODE}.json --
     10 of 326 projects on 2026-08-24). dep_stage is OPTIONAL and FORWARD-ONLY by its own
     ratified design; a project that never opted in is not in this gate's scope.
  3. FILES UNDER **/task_orders/ ONLY.
A file failing any of the three is NOT a pass -- it is OUT OF SCOPE, and the report says
which, because "no findings" and "did not look" must never render identically.

RAMP: ANNOUNCE by default; ENFORCE when org/mcp/workflow-gate2.enforce exists (the
NFRA_COMPRAIL announce-then-enforce shape, marker-file checked, so arming is one
reviewable act and not a code change). Under ANNOUNCE this prints findings and exits 0.
  ⛔ THE MARKER IS THE AUTHORITY, NEVER A COMMENT ABOUT THE MARKER. Rule 21 records the
  measured cost of the inverse: an agent read a stale ramp COMMENT instead of the armed
  marker and reported a live gate as not-yet-enforcing.

OVERRIDE: audited, and it must be a DELIBERATE SENTENCE, not a flag. Put
`# workflow-gate2-override: <reason>` in the commit message; every use is appended to
org/mcp/workflow-gate2-override.log with the file and the reason. A repeat override for
one recurring intent is a COVERAGE GAP, not a habit -- route it, do not keep overriding.

SEATING LINT (added 2026-08-25, Andrew-direct ~00:2xZ -- "Yeah thats fine you can build it"):
the SAME new-TO pass also refuses a TO addressed to an instance ALREADY HOLDING OPEN TOs ON
ANOTHER WORKFLOW PROJECT -- one project per tier-2 seat instance, his 2026-08-24 ~19:29Z rule.
"Unless it names a fresh lane" needs no separate detection: a fresh lane holds nothing and so
passes BY CONSTRUCTION. Scoped to dep_stage-registered projects on BOTH sides per Rule 27's own
wording; unscoped it would fire on legacy debt (the base 0.8.0 serial alone carries 80 open
pre-workflow TOs) instead of on seating.

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
ISSUED_TO_RE = re.compile(r"<issued_to>(.*?)</issued_to>", re.S)
STATUS_RE = re.compile(r"<status>(.*?)</status>", re.S)
# A concrete seat instance, lane suffix included. Deliberately does NOT match a CLASS token
# ("AE-class"), because the seating rule binds an INSTANCE, not a class.
SERIAL_RE = re.compile(r"\b\d+\.\d+\.\d+_[A-Z]{2}_[A-Za-z][A-Za-z0-9]*(?:~[A-Za-z0-9]+)?\b")
# MEASURED from the live corpus 2026-08-25, not invented (Rule 24: classify the axis that
# exists, do not mint one). Leading token only -- real statuses carry trailing prose
# ("CLOSED -- COO STALE-TO SWEEP", "COMPLETE -- CLOSED 2026-08-2").
TERMINAL_STATUS = {"COMPLETE", "CLOSED", "SUPERSEDED", "CANCELLED", "DONE",
                   "CLOSED-SUPERSEDED"}


def staged_added() -> list[str]:
    try:
        out = subprocess.run(
            ["git", "diff", "--cached", "--diff-filter=A", "--name-only"],
            cwd=WORKSPACE, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True).stdout
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


_TRACKED_TOS = None


def _tracked_task_orders() -> set:
    """Repo-relative paths of TRACKED task-order files, posix-normalised.

    COO 67721 / 67951: a corpus read from the shared WORKING TREE lets a peer's half-written
    file change this gate's verdict, and nothing in the verdict records which state it was
    built against. ~190 dirty paths live here; uncommitted work is visible to peer instruments
    the moment it hits disk, and the remedy is on the READER.

    FAIL-CLOSED-TO-EMPTY IS DELIBERATE: if `git ls-files` cannot run, this returns an EMPTY
    set, which makes the corpus empty and the gate ANNOUNCE rather than refuse. A gate that
    cannot establish committed state must not refuse anyone's commit on a corpus it could not
    read -- and callers print the corpus denominator, so an empty one is visible, not silent.
    """
    global _TRACKED_TOS
    if _TRACKED_TOS is None:
        try:
            out = subprocess.run(
                ["git", "ls-files", "--", "*/task_orders/*.md", "*/task-orders/*.md"],  # R-ii: both roots
                cwd=WORKSPACE, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True).stdout
            _TRACKED_TOS = {ln.strip().replace("\\", "/") for ln in out.splitlines() if ln.strip()}
        except Exception:  # noqa: BLE001
            _TRACKED_TOS = set()
    return _TRACKED_TOS


def _is_tracked(rel: str) -> bool:
    return rel.replace("\\", "/") in _tracked_task_orders()


_TOCHECK = None


def _to_check_resolver():
    """to-check.py's `_assignees_from_field`, loaded once.

    NO NAIVE FALLBACK BY DESIGN. If this cannot load, the seating check reports NOT EVALUATED
    and refuses nothing -- because the fallback I would otherwise write is exactly the prose
    harvest that produced a false accusation against a lane the TO had EXPLICITLY EXCLUDED.
    A gate that cannot resolve its subject must say so, not guess.
    """
    global _TOCHECK
    if _TOCHECK is None:
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "to_check_mod", WORKSPACE / ".tools" / "to-check.py")
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            _TOCHECK = mod._assignees_from_field
        except Exception:  # noqa: BLE001
            _TOCHECK = False
    return _TOCHECK or None


def _is_open(text: str) -> bool:
    """UNKNOWN COUNTS AS OPEN -- fail-closed, deliberately. An unrecognised status makes the
    seat look MORE occupied, so the lint refuses more rather than less. A false refusal is
    loud and gets argued with; a false pass is believed."""
    m = STATUS_RE.search(text)
    if not m:
        return True
    lead = re.split(r"[\s\-]", m.group(1).strip().upper(), maxsplit=1)[0].strip()
    return lead not in TERMINAL_STATUS


def _pipeline_projects() -> set:
    out = set()
    for f in PROJECTS.glob("*.json"):
        try:
            if "dep_stage" in json.loads(f.read_text(encoding="utf-8")):
                out.add(f.stem.upper())
        except Exception:  # noqa: BLE001
            continue
    return out


def _open_to_index(exclude: set) -> tuple[dict, int, int, int, int]:
    """{serial: {PROJECT: [to_id]}} over OPEN TOs on PIPELINE-REGISTERED projects.
    Returns (index, tos_scanned, holdings_indexed, unclassified_serial_occurrences)."""
    pipeline = _pipeline_projects()
    resolve = _to_check_resolver()
    if resolve is None:
        return {}, 0, 0, -1, 0
    idx: dict = {}
    scanned = held = unclassified = untracked_skipped = 0
    tracked = _tracked_task_orders()
    for f in list((WORKSPACE / "org").rglob("task_orders/*.md")) + list((WORKSPACE / "org" / "missions").rglob("task-orders/*.md")):  # R-ii: both roots
        rel = str(f.relative_to(WORKSPACE)).replace("\\", "/")
        if rel in exclude:
            continue
        if rel not in tracked:
            untracked_skipped += 1
            continue          # a peer's in-flight file is NOT a holding
        scanned += 1
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue
        code, _ = project_code(text, rel)
        if code not in pipeline or not _is_open(text):
            continue
        m = ISSUED_TO_RE.search(text)
        if not m:
            continue
        tid = TO_ID_RE.search(text)
        tid = tid.group(1) if tid else Path(rel).name
        assignees, unres = resolve(m.group(1))
        unclassified += unres
        for serial in set(assignees):
            idx.setdefault(serial, {}).setdefault(code, []).append(tid)
            held += 1
    return idx, scanned, held, unclassified, untracked_skipped


def seating_check(new_tos: list) -> tuple[list, list]:
    """ONE PROJECT PER TIER-2 SEAT INSTANCE (Andrew-direct 2026-08-24 ~19:29Z, verbatim:
    "it is a lot easier if they are simply brought on to complete one project at a time. For
    parallelization sake, we can simply bring on ~tilde agents if there are multiple projects
    we want to pursue at once"). Gate authorized Andrew-direct 2026-08-25 ~00:2xZ.

    THE RULE REDUCES TO ONE TEST: a NEW TO on project P addressed to instance S is refused if S
    already holds an OPEN TO on some pipeline project Q != P. "Unless it names a fresh lane"
    needs no separate detection -- a fresh lane holds nothing, so it satisfies the test BY
    CONSTRUCTION.

    SCOPE, both sides restricted to PIPELINE-REGISTERED projects, and this is load-bearing
    rather than convenient. THE AUTHORITY IS ANDREW-DIRECT 2026-08-24 ~19:29Z -- "ONE PROJECT
    PER TIER-2 SEAT INSTANCE", protecting THE SEAT'S CONTEXT, not the box -- built on his
    ~00:2xZ 2026-08-25 word, exactly as this file's own header at :38-40 already says.
    *** CITATION REPAIRED 2026-09-10 by 1.0.0_SA_CTO. This docstring previously claimed
    "CLAUDE.md Rule 27 says it in those words" and quoted a sentence CLAUDE.md HAS NEVER
    CONTAINED. Verified absent on THREE instruments by three seats -- comp-find with
    wrap-proof fragments, `grep -ic`, and native Grep -- each with a working positive control
    on the same file. The header carried the CORRECT attribution the whole time while the
    docstring a reader reaches when asking "why did this refuse" carried a false one, and the
    phrase generalised from TIER-2 to all tiers as it travelled. THE GATE IS UNCHANGED: only
    the citation was wrong, never the enforcement. Whether the rule should reach TIER 1 is
    ANDREW'S call and is NOT taken here. ***
    Unscoped the lint
    would fire on LEGACY DEBT instead of on seating: the base 0.8.0 serial alone carries 80 open
    pre-pipeline TOs across 34 projects, which would make every base serial permanently illegal
    and the refusal meaningless. DECLARED RESIDUAL: a seat carrying non-pipeline TOs is not
    counted as multi-project here.

    NEW FILES ONLY (the caller's --diff-filter=A). A re-address EDITS an existing TO's
    issued_to, and that re-address is the REMEDY for the heaps -- a lint that blocked the fix
    would be the defect. Andrew's authorization carried this condition on the card's face.
    """
    frames: list[str] = []
    v: list[str] = []
    if not new_tos:
        return v, frames
    resolve = _to_check_resolver()
    if resolve is None:
        frames.append("seating: NOT EVALUATED -- to-check.py's assignee resolver could not be "
                      "loaded, and this gate will NOT fall back to harvesting serials out of "
                      "prose. That fallback is what produced a false accusation against a lane "
                      "a TO had explicitly EXCLUDED. UNKNOWN is not a pass and not a refusal.")
        return v, frames
    idx, scanned, held, unclassified, untracked = _open_to_index(
        exclude={rel for rel, _, _ in new_tos})
    frames.append(f"seating-frame: indexed {held} open-TO holding(s) across {len(idx)} seat "
                  f"instance(s), from {scanned} TRACKED TO file(s) ({untracked} untracked "
                  f"in-flight file(s) SKIPPED -- a peer's uncommitted draft is not a holding), "
                  f"scoped to {len(_pipeline_projects())} pipeline-registered project(s); "
                  f"{unclassified} serial occurrence(s) UNCLASSIFIED (not read as assignments, "
                  f"and not read as absences either)")
    for rel, code, text in new_tos:
        m = ISSUED_TO_RE.search(text)
        if not m:
            frames.append(f"seating: {rel} names no <issued_to> -- NOT EVALUATED (no instance "
                          f"to test; this is UNKNOWN, not a pass)")
            continue
        assignees, unres = resolve(m.group(1))
        serials = sorted(set(assignees))
        if not serials:
            frames.append(f"seating: {rel} <issued_to> resolves to NO assignee instance in a "
                          f"recognised notation ({unres} serial occurrence(s) unclassified) -- "
                          f"NOT EVALUATED. A class-addressed TO becomes testable at the seating "
                          f"act, and a serial merely MENTIONED in the field is not an assignment "
                          f"(to-check.py's rule, and the one my first cut broke)")
            continue
        for s in serials:
            other = {q: ids for q, ids in idx.get(s, {}).items() if q != code}
            if not other:
                frames.append(f"seating: {rel} -> {s} holds 0 open TO(s) on any OTHER pipeline "
                              f"project. Legal target.")
                continue
            detail = "; ".join(f"{q} ({len(ids)} open: {', '.join(sorted(ids)[:3])}"
                               f"{'...' if len(ids) > 3 else ''})" for q, ids in sorted(other.items()))
            v.append(
                f"{rel}\n"
                f"      SEATING: this NEW task order for {code} is addressed to {s}, which "
                f"already holds open TOs on {len(other)} OTHER pipeline project(s): {detail}\n"
                f"      ONE PROJECT PER TIER-2 SEAT INSTANCE (Andrew-direct 2026-08-24 ~19:29Z). "
                f"The resource protected is the SEAT'S CONTEXT, not the box.\n"
                f"      FIX: address this TO to a FRESH LANE of that class (e.g. {s.split('~')[0]}~<letter>) "
                f"-- a fresh lane holds nothing and passes by construction. MSTR assigns the letter "
                f"from the spawn-audit UNION disk; do not reuse one.\n"
                f"      NOT a reason to widen an existing lane's load: re-addressing an EXISTING TO "
                f"is an edit and never trips this lint.")
    return v, frames


def audit_override(reason: str, files: list[str]) -> None:
    try:
        OVERRIDE_LOG.parent.mkdir(parents=True, exist_ok=True)
        stamp = subprocess.run(["git", "log", "-1", "--format=%cI"], cwd=WORKSPACE,
                               capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()
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
    seating_subjects: list = []
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
        seating_subjects.append((rel, code, text))
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
                f"      (CANONICAL_FABRIC_WORKFLOW_20260901.md L5/L6). If no decomp exists yet, that is a\n"
                f"      PIPELINE FAILURE TO SURFACE to COO/CTO, not a reason to cut the TO without one.")
            continue
        if not CELL_ID_RE.search(m.group(1)):
            findings.append(
                f"{rel}\n"
                f"      project {code} ({how}, dep_stage={stage}) carries a <decomp_ref> that names\n"
                f"      NO CELL IDS -- a decomp path alone cannot be joined to any criterion, so the\n"
                f"      layer-1 alignment check has nothing to close against.\n"
                f"      FIX: name the cells this TO discharges inside the <decomp_ref>.")

    seat_v, seat_frames = seating_check(seating_subjects)
    findings.extend(seat_v)

    mode = "ENFORCE" if enforce else "ANNOUNCE"
    print(f"to-decomp-ref-lint | mode={mode} | considered={considered} file(s), "
          f"{len(in_scope)} under task_orders/, {checked} on pipeline-registered projects, "
          f"{out_of_scope_unregistered} skipped (project not pipeline-registered) | "
          f"findings={len(findings)}")
    for line in seat_frames:
        print(f"  {line}")
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
