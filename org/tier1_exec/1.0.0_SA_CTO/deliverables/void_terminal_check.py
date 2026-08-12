#!/usr/bin/env python3
"""void_terminal_check -- the VOID-terminal machine check (Andrew-approved @eb5a199a99, laptop "3 yes").

Binds run_manifest.status: CERTIFIED to a NON-VOID certifying attempt: the run dir's terminal
certification.json must exist and carry a verdict beginning PASS (PASS or PASS-WITH-REFUSAL).
A VOID attempt RETAINED BESIDE a passing terminal cert (certification.attempt*.VOID.json) is
NORMAL -- attempts accumulate -- and never flags. (The phase-gate lesson: a check that cannot
tell the state it polices from a legitimate neighbouring state trains readers to ignore it.)

SEVERITY TAXONOMY (CVO~Z rider, folded at build time per Andrew's routing note -- a
real-but-inert deviation reported at full severity is how an instrument trains its readers
to ignore it):
  VIOLATION                       rc=1  capability-granting: CERTIFIED status without a passing
                                        terminal cert (absent file, VOID verdict, or unparseable
                                        verdict). The status GRANTS citability (Rule 14(f)) that
                                        no certification supports.
  DEVIATION-NO-CAPABILITY-CHANGE  rc=0  real but inert, distinct severity line: a passing cert
                                        exists but status under-claims (DRY/OPEN); or status is
                                        CERTIFIED with a passing cert but certification_ref is
                                        absent (ref hygiene -- the capability is real, the
                                        pointer is missing).
  CLEAN                           rc=0

Exit 0 = CLEAN or deviations only. Exit 1 = VIOLATION (every one printed). Exit 2 = usage/read
error. CHECK THE RC -- this banner contains the vocabulary of every verdict (binding I).

Usage: python void_terminal_check.py <run_dir> [<run_dir> ...]
"""
import json
import sys
from pathlib import Path

PASSING = ("PASS",)  # verdict must BEGIN with PASS: covers PASS and PASS-WITH-REFUSAL


def check_run(run_dir: Path):
    """Returns (violations, deviations, notes) for one run dir. Denominators printed by caller."""
    violations, deviations, notes = [], [], []
    rj = run_dir / "run.json"
    if not rj.is_file():
        violations.append(f"{run_dir}: run.json ABSENT -- nothing to check is a VIOLATION, not a skip")
        return violations, deviations, notes
    try:
        manifest = json.loads(rj.read_text(encoding="utf-8"))
    except Exception as exc:
        violations.append(f"{run_dir}: run.json unreadable ({type(exc).__name__}) -- fail closed")
        return violations, deviations, notes

    status = manifest.get("status")
    cert_ref = manifest.get("certification_ref")
    term = run_dir / "certification.json"  # the TERMINAL cert; attempt*.VOID.json are history
    term_verdict = None
    if term.is_file():
        try:
            term_verdict = str(json.loads(term.read_text(encoding="utf-8")).get("verdict", ""))
        except Exception as exc:
            term_verdict = None
            notes.append(f"{run_dir}: certification.json unreadable ({type(exc).__name__})")

    term_passes = term_verdict is not None and term_verdict.strip().upper().startswith(PASSING)

    if status == "CERTIFIED":
        if not term.is_file():
            violations.append(
                f"{run_dir}: status=CERTIFIED with NO terminal certification.json -- "
                f"the status grants citability nothing supports")
        elif not term_passes:
            shown = (term_verdict or "<unreadable>")[:60]
            violations.append(
                f"{run_dir}: status=CERTIFIED over a non-passing terminal cert "
                f"(verdict: {shown!r}) -- CERTIFIED-over-VOID is the class this check exists for")
        elif not cert_ref:
            deviations.append(
                f"{run_dir}: DEVIATION-NO-CAPABILITY-CHANGE -- passing cert exists but "
                f"certification_ref is absent (pointer hygiene; capability is real)")
    else:
        if term_passes:
            deviations.append(
                f"{run_dir}: DEVIATION-NO-CAPABILITY-CHANGE -- passing terminal cert exists but "
                f"status={status} under-claims it (inert: under-claiming grants nothing)")
    # Retained VOID attempts beside a passing terminal cert: NORMAL, never flagged.
    return violations, deviations, notes


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    dirs = [Path(a) for a in argv[1:]]
    all_v, all_d = [], []
    for d in dirs:
        v, dev, notes = check_run(d)
        all_v.extend(v)
        all_d.extend(dev)
        for n in notes:
            print(f"  note: {n}")
    print(f"void-terminal-check | runs checked: {len(dirs)} | VIOLATION: {len(all_v)} | "
          f"DEVIATION-NO-CAPABILITY-CHANGE: {len(all_d)}")
    for v in all_v:
        print(f"  VIOLATION: {v}")
    for d_ in all_d:
        print(f"  deviation: {d_}")
    return 1 if all_v else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
