#!/usr/bin/env python3
"""to-pipeline-gate.py -- LAYER 2 of the DIRECTIVE EXECUTION PIPELINE enforcement architecture.

AUTHORITY: Andrew-direct 2026-09-01 at the 3.0.0_SA_CVO terminal -- "re-authorize the three
enforcement layers and add the stage-3 preflight" / "we need these set up in a manner that they
are actually mandated" / "I prefer gates and deterministic methodology because anything that is
simply 'guidance' may dissipate or otherwise be inconsistent over long-running sessions."

WHAT THIS GATES, AND WHY IT IS THE KEYSTONE
  org/ref/DIRECTIVE_EXECUTION_PIPELINE.md specifies five enforcement layers. Layer 1 (the
  proof-of-spec validation gate) IS BUILT and DOES enforce -- but only on an instance whose
  GOVERNING TO carries a naming <decomp_ref>. MEASURED 2026-09-01: 130 of 2233 TO files carry
  one = 5.8%. Layer 1 is therefore inert on 94% of the estate, not because it is broken but
  because nothing ever required the TO to carry the element that activates it.

  LAYER 2 IS THAT REQUIREMENT. Gate the neck of the funnel: a TO that conformantly requires a
  decomp structurally requires the decomp, which requires the PRD, which requires registration.
  One gate at TO issuance enforces the entire upstream funnel without taxing any other act.

  PROSPECTIVE ONLY (Andrew-direct, same terminal): this fires on NEWLY ADDED TO files. Existing
  TOs are not back-filled and are not refused. A gate that retroactively refuses 2,103 files
  would be ignored wholesale, which is the failure mode CLAUDE.md rule 21 limb (iii) records.

THE THREE-VALUE PREFLIGHT ENUM, AND WHY NOT TWO
  RUN | DECLARED-NOT-APPLICABLE | (absent -> refused). A two-value RUN/SKIPPED enum forces a
  genuinely-inapplicable tool to be recorded as SKIPPED -- a vocabulary with no not-applicable
  value encodes non-application as a violation. Eight instances of that class were measured on
  2026-09-01 alone.

FAIL-CLOSED. An unreadable file, an unparseable block or an unexpected exception REFUSES.
A gate that fails open is not a gate.
"""
import os
import re
import subprocess
import sys

TO_PATH_RE = re.compile(r"(^|/)org/.*/task_orders/[^/]+\.md$")
DECOMP_RE = re.compile(r"<decomp_ref>(.*?)</decomp_ref>", re.S)
PREFLIGHT_RE = re.compile(r"<preflight>(.*?)</preflight>", re.S)
NONE_WORD_RE = re.compile(r"^\W*(NONE|N/?A|NO\b)", re.I)
OVERRIDE_RE = re.compile(r"^#\s*pipeline-override:\s*(\S.*)$", re.M)

# Each preflight tool must appear with a disposition. The tool names are the ratified ones.
PREFLIGHT_TOOLS = ("comp-schedule", "comp-iam", "comp-adversary")
DISPOSITION_RE = r"(RUN|DECLARED-NOT-APPLICABLE)"


def _repo_root():
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=20)
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:  # noqa: BLE001
        pass
    return os.getcwd()


def _newly_added(root):
    """The set of paths STAGED AS ADDED. Prospective-only scoping lives here.

    A rename (R) counts as added at its new path -- moving a TO into task_orders/ is an
    issuance. A modification (M) does not: this gate never refuses an existing TO.
    """
    try:
        out = subprocess.run(["git", "diff", "--cached", "--name-status"],
                             cwd=root, capture_output=True, text=True, timeout=30)
    except Exception:  # noqa: BLE001
        return None  # fail closed: caller refuses
    if out.returncode != 0:
        return None
    added = set()
    for line in out.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        code = parts[0].strip()
        path = parts[-1].strip()
        if code.startswith("A") or code.startswith("R"):
            added.add(path)
    return added


def _check_preflight(body):
    """Return a list of complaints about the preflight block body."""
    problems = []
    for tool in PREFLIGHT_TOOLS:
        pat = re.compile(re.escape(tool) + r"\s*[:=]\s*" + DISPOSITION_RE, re.I)
        m = pat.search(body)
        if not m:
            problems.append(
                "preflight names no disposition for %s -- expected "
                "'%s: RUN' or '%s: DECLARED-NOT-APPLICABLE <reason>'" % (tool, tool, tool))
            continue
        if m.group(1).upper() == "DECLARED-NOT-APPLICABLE":
            # The reason must sit on the SAME LINE as the disposition. Reading to the next
            # 200 chars lets the FOLLOWING TOOL'S line be scored as this tool's reason --
            # caught by the bare-reason control on first exercise, 2026-09-01.
            eol = body.find("\n", m.end())
            tail = (body[m.end():] if eol == -1 else body[m.end():eol]).strip()
            if len(tail) < 8:
                problems.append(
                    "%s is DECLARED-NOT-APPLICABLE with no reason ON ITS OWN LINE -- a bare "
                    "not-applicable is a skip wearing a tidier label" % tool)
    return problems


def check_file(root, rel):
    """Return (violations, notes) for ONE newly-added TO file."""
    v, notes = [], []
    full = os.path.join(root, rel)
    try:
        with open(full, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except Exception as exc:  # noqa: BLE001
        return (["UNREADABLE (%s) -- refusing; a gate that cannot read its subject "
                 "must not pass it" % exc], notes)

    ov = OVERRIDE_RE.search(text)
    if ov:
        notes.append("OVERRIDE taken on %s -- reason: %s" % (rel, ov.group(1).strip()))
        return ([], notes)

    m = DECOMP_RE.search(text)
    if not m:
        v.append("%s: NO <decomp_ref> element. A TO cannot be issued without naming the "
                 "atom-decomp it executes -- that is what makes stage 3 structurally "
                 "required (pipeline layer 2)." % rel)
    else:
        body = m.group(1).strip()
        if not body:
            v.append("%s: <decomp_ref> is EMPTY. The element's CONTENT is the claim, not its "
                     "PRESENCE (CTO 87900)." % rel)
        elif NONE_WORD_RE.match(body):
            notes.append("%s: <decomp_ref> declares NONE -- allowed (one-branch work under its "
                         "own charter), and layer 1 will read it as ANNOUNCE, not ENFORCE." % rel)

    pm = PREFLIGHT_RE.search(text)
    if not pm:
        v.append("%s: NO <preflight> block. Stage 3 must record comp-schedule, comp-iam and "
                 "comp-adversary, each RUN or DECLARED-NOT-APPLICABLE with a reason "
                 "(Andrew-direct 2026-09-01)." % rel)
    else:
        for p in _check_preflight(pm.group(1)):
            v.append("%s: %s" % (rel, p))
    return (v, notes)


def main(argv):
    root = _repo_root()
    added = _newly_added(root)
    if added is None:
        print("[to-pipeline-gate] REFUSED: could not read the staged index. Fail-closed.",
              file=sys.stderr)
        return 1

    # Consider only paths the caller dispatched AND that git says are newly added.
    dispatched = [a.replace("\\", "/") for a in argv[1:]]
    targets = sorted(p for p in dispatched
                     if TO_PATH_RE.search(p) and p in added)

    if not targets:
        print("[to-pipeline-gate] OK: 0 newly-added task_orders/*.md in this commit "
              "(denominator: %d dispatched path(s), %d staged-added)."
              % (len(dispatched), len(added)))
        return 0

    all_v, all_notes = [], []
    for rel in targets:
        v, notes = check_file(root, rel)
        all_v.extend(v)
        all_notes.extend(notes)

    for n in all_notes:
        print("[to-pipeline-gate] NOTE: %s" % n)

    if all_v:
        print("[to-pipeline-gate] REFUSED -- %d violation(s) across %d newly-added TO file(s):"
              % (len(all_v), len(targets)), file=sys.stderr)
        for x in all_v:
            print("    %s" % x, file=sys.stderr)
        print("  FIX: add the two blocks to the TO face, or -- if this TO genuinely stands "
              "outside the pipeline -- add a line '# pipeline-override: <reason>' "
              "(audited, and it prints).", file=sys.stderr)
        return 1

    print("[to-pipeline-gate] OK: %d newly-added TO file(s) carry <decomp_ref> and a complete "
          "<preflight> block." % len(targets))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Exception as exc:  # noqa: BLE001
        print("[to-pipeline-gate] REFUSED: unexpected error (%s). Fail-closed." % exc,
              file=sys.stderr)
        sys.exit(1)
