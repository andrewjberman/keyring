"""comp-ledger-agreement -- HEADER/BODY agreement scan over deploy-completion ledgers.

ADVISORY. It CLASSIFIES; it does not alarm and it does not block a commit. Escalation to
blocking is Andrew's to grant -- proposed, not implemented (CLAUDE.md: never implement a gate
unless Andrew explicitly asks).

THE DEFECT CLASS (measured 2026-08-19, DS~A + COO): a ledger in
org/critical_paths/change_management/ carried a full close IN ITS BODY -- all five close
conditions discharged -- while its `**Status:**` HEADER still read OPEN. Every scanner keys the
header, so a CORRECTLY-COMPLETED deploy presented as RED indefinitely: a false stranded-leg
alarm against the NEVER-rule instrument we most need believed. A false outage is not a safe
error; it spends credibility and manufactures pressure to "fix" something that is working.

BOTH DIRECTIONS ARE SCANNED, and the second is the dangerous one:
  header-lags-body   OPEN/RED header over a CLOSED body   -> the measured false-alarm class
  body-lags-header   CLOSED header over an UNFINISHED body -> a STRANDED LEG WEARING A CLOSE

WHY IT CLASSIFIES RATHER THAN FLAGS: a checker that cannot tell drift-KIND manufactures the
wrong reflex. "header-lags-body" wants a header edit; "body-lags-header" wants someone to go
look at a deploy that may be half-landed. Collapsing them into one "MISMATCH" count would point
the same reflex at both, and it is the wrong reflex for one of them.

TWO PARSING TRAPS, both live in this corpus and both handled explicitly:
  1. `## CLOSE CONDITIONS` / `## Close conditions` is an OPEN-TIME section listing what must be
     met -- NOT a close. A naive `^## CLOSE` match counts it as closure and INVERTS the verdict
     on exactly the ledgers that are still open.
  2. 123 of 511 ledgers carry NO `**Status:**` header at all. They are reported as their own
     class, never bucketed into agree/disagree -- an instrument that silently folds
     unclassifiable rows into a verdict is reporting a denominator it does not have.

Usage:
  python .tools/comp-ledger-agreement.py [--since YYYY-MM-DD] [--only-disagreeing] [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def _repo_root() -> Path:
    r = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                       cwd=str(Path(__file__).resolve().parent),
                       capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        return Path(r.stdout.strip())
    raise SystemExit("cannot resolve repo root")


LEDGER_DIR = "org/critical_paths/change_management"

# Header vocabulary as MEASURED in the corpus, not as imagined.
CLOSED_HEAD = {"CLOSED", "COMPLETE", "RESOLVED", "RESOLVED-PARKED", "VOID", "SUPERSEDED",
               "DEFERRED-TO-POST-CONSOLIDATION"}
OPEN_HEAD = {"OPEN", "PLAN", "HELD-SOVEREIGN-GATED", "HELD", "PENDING", "RED", "BLOCKED"}

# A genuine close SECTION. `CONDITIONS` is excluded on purpose (trap 1).
CLOSE_SECTION = re.compile(
    r"^##\s+(CLOSED|CLOSE|CLOSURE|CLOSE\s+NOTE|CLOSE\s+BLOCK)\b(?!\s*CONDITIONS)",
    re.IGNORECASE | re.MULTILINE)
CONDITIONS_SECTION = re.compile(r"^##\s+CLOSE\s+CONDITIONS\b", re.IGNORECASE | re.MULTILINE)
STATUS_LINE = re.compile(r"^\*\*Status:\*\*\s*(.+)$", re.MULTILINE)


def header_state(text: str):
    m = STATUS_LINE.search(text)
    if not m:
        return None, ""
    raw = m.group(1).strip()
    tok = re.split(r"[\s,;.]", raw, 1)[0].strip().upper()
    if tok in CLOSED_HEAD:
        return "CLOSED", raw[:110]
    if tok in OPEN_HEAD:
        return "OPEN", raw[:110]
    return "UNKNOWN-VOCAB", raw[:110]


# A close ATTESTATION anywhere in the body: "CLOSED <date>" / "CLOSE(D) at <time> by <serial>".
# NOT anchored to a heading, because most ledgers in this corpus record the close as a bold line
# at the foot and never open a `## CLOSED` section at all.
CLOSE_ATTESTATION = re.compile(
    r"\*{0,2}CLOSE[D]?\*{0,2}\s*(?:AT\s+)?(?:\d{4}-?\d{2}-?\d{2}[T ]?\d{2}:?\d{2}"
    r"|--\s*\S|:\s*\S)",
    re.IGNORECASE)


def body_state(text: str):
    """CLOSED on close EVIDENCE, in any of the forms this corpus actually uses.

    CRITICAL: the `**Status:**` header line is REMOVED before scanning. Leaving it in would
    make the body echo the header, and an instrument whose two inputs are the same input
    CANNOT DISAGREE -- it would report perfect agreement forever and detect nothing.

    The first version of this function keyed ONLY on a `## CLOSED` section heading and
    classified 346 of 382 ledgers as "stranded leg wearing a close" -- an absurd rate that was
    a defect in the DETECTOR, not a finding about the estate. Absence of one heading spelling
    is not absence of a close: the checked instance carried a full close-conditions table, all
    rows PASS, and a bold `**CLOSED <ts> by <serial>.**` line at the foot, under a document
    with exactly one heading. THE DENOMINATOR IS WHAT CAUGHT IT.
    """
    body = STATUS_LINE.sub("", text, count=1)   # never let the header answer for the body
    for m in CLOSE_SECTION.finditer(body):
        line = m.group(0).strip()
        if re.match(r"^##\s+CLOSE\s+CONDITIONS", line, re.IGNORECASE):
            continue
        return "CLOSED", line
    m = CLOSE_ATTESTATION.search(body)
    if m:
        return "CLOSED", m.group(0).strip()[:60]
    # LINE-SCOPED fallback: a close word and a timestamp ON THE SAME LINE. Adjacency-based
    # matching missed the corpus idiom "**Opened+closed same window 2026-08-19 13:47-13:50Z**"
    # -- the date follows "window", not "closed" -- which under-reported 2 of the 6 flagged
    # ledgers as having no close. Third under-read of this predicate tonight; each one was the
    # detector being too narrow, never the estate being broken.
    # DECLARED BIAS: this errs toward FINDING a close. That deliberately shrinks the
    # body-lags-header CANDIDATE set rather than the header-lags-body FINDING set, because the
    # estate's measured pain is FALSE REDS. The cost is that a genuinely stranded leg whose
    # ledger merely mentions a close word beside a time could be missed -- which is why
    # body-lags-header is a CANDIDATE requiring a human read and never a verdict.
    CLOSE_WORD = re.compile(r"clos(?:e|ed)", re.IGNORECASE)
    WHEN = re.compile(r"\d{4}-?\d{2}-?\d{2}|\d{2}:\d{2}")
    NOT_A_CLOSE = re.compile(
        r"close\s+conditions|will\s+close|closes\s+at|to\s+close|before\s+close",
        re.IGNORECASE)
    for line in body.splitlines():
        if not CLOSE_WORD.search(line):
            continue
        if not WHEN.search(line):
            continue
        if NOT_A_CLOSE.search(line):
            continue
        return "CLOSED", line.strip()[:60]
    return "OPEN", ""


def classify(h, b):
    """THE TWO DIRECTIONS ARE NOT EQUALLY DECIDABLE, and pretending they are is how this
    tool would become the thing it was built to catch.

      header-lags-body  rests on POSITIVE evidence -- a close was FOUND in the body while
                        the header says open. Finding something is decidable. -> FINDING.
      body-lags-header  rests on the ABSENCE of close evidence under a CLOSED header. This
                        corpus has no fixed schema (close records appear as bold lines,
                        per-leg table cells, checklists and prose), so "I did not match a
                        close" is not the same claim as "there is no close". That is the
                        clean-zero-from-the-wrong-question class. -> CANDIDATE, needs a read.

    Reporting the second as a verdict would manufacture false stranded-leg alarms at scale --
    precisely the harm this lint exists to prevent, pointed at a wider target."""
    if h is None:
        return "NO-HEADER"
    if h == "UNKNOWN-VOCAB":
        return "UNKNOWN-VOCAB"
    if h == "CLOSED" and b == "CLOSED":
        return "genuinely-closed"
    if h == "OPEN" and b == "OPEN":
        return "genuinely-open"
    if h == "OPEN" and b == "CLOSED":
        return "header-lags-body"
    return "body-lags-header-CANDIDATE"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--since", default=None, help="only ledgers whose filename date >= this (YYYY-MM-DD)")
    ap.add_argument("--only-disagreeing", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--dir", default=None,
                    help="scan an alternate ledger dir -- e.g. a VINTAGE extracted with "
                         "`git show <commit>:<path>`. A record's state must be read at the "
                         "vintage the claim is about; scanning HEAD answers a different "
                         "question than 'what did the scanner see when it fired?'")
    a = ap.parse_args()

    ws = _repo_root()
    scan_dir = Path(a.dir) if a.dir else (ws / LEDGER_DIR)
    files = sorted(scan_dir.glob("*.md"))
    if a.since:
        key = a.since.replace("-", "")
        # The prefix must actually BE a date. A bare `name[:8] >= key` string-compares
        # non-dated filenames too -- "mdpf-tri" sorts above "20260819" and silently joins
        # the scope, so the tool would report on files outside the window it names. The
        # filter's DOMAIN was not the set it claimed; caught by an 08-19 scan returning
        # hand-authored ledgers dated in July.
        files = [f for f in files if f.name[:8].isdigit() and f.name[:8] >= key]

    rows, counts = [], {}
    for f in files:
        t = f.read_text(encoding="utf-8", errors="replace")
        h, hraw = header_state(t)
        b, bmark = body_state(t)
        c = classify(h, b)
        counts[c] = counts.get(c, 0) + 1
        rows.append({"file": f.name, "header": h, "header_text": hraw,
                     "body": b, "body_marker": bmark, "classification": c,
                     "has_conditions_section": bool(CONDITIONS_SECTION.search(t))})

    if a.json:
        print(json.dumps({"scanned": len(rows), "counts": counts, "rows": rows}, indent=2))
        return 0

    n = len(rows)
    dis = [r for r in rows if r["classification"] in ("header-lags-body", "body-lags-header-CANDIDATE")]
    classifiable = sum(v for k, v in counts.items() if k not in ("NO-HEADER", "UNKNOWN-VOCAB"))

    print("=" * 84)
    print(f"comp-ledger-agreement -- ADVISORY header/body scan over {LEDGER_DIR}")
    if a.since:
        print(f"  scope: filename date >= {a.since}")
    print("=" * 84)

    if not a.only_disagreeing:
        for r in rows:
            if r["classification"] in ("genuinely-closed", "genuinely-open"):
                continue
            print(f"\n  [{r['classification']}] {r['file']}")
            print(f"      header: {r['header']}  <- {r['header_text'][:88]}")
            print(f"      body  : {r['body']}" + (f"  <- matched {r['body_marker']!r}"
                                                  if r["body_marker"] else "  <- no close section"))
    else:
        for r in dis:
            print(f"\n  [{r['classification']}] {r['file']}")
            print(f"      header: {r['header']}  <- {r['header_text'][:88]}")
            print(f"      body  : {r['body']}" + (f"  <- matched {r['body_marker']!r}"
                                                  if r["body_marker"] else "  <- no close section"))

    print()
    print("-" * 84)
    print(f"  LEDGERS SCANNED                : {n}")
    print(f"  CLASSIFIABLE (header present)  : {classifiable} of {n}")
    print(f"    genuinely-closed             : {counts.get('genuinely-closed', 0)}")
    print(f"    genuinely-open               : {counts.get('genuinely-open', 0)}")
    print(f"    header-lags-body  [FALSE RED]: {counts.get('header-lags-body', 0)}")
    print(f"    body-lags-header CANDIDATES  : "
          f"{counts.get('body-lags-header-CANDIDATE', 0)}  <- NOT a verdict; see note")
    print(f"  NOT CLASSIFIABLE BY THIS TOOL  : "
          f"{counts.get('NO-HEADER', 0)} no **Status:** header, "
          f"{counts.get('UNKNOWN-VOCAB', 0)} unrecognised header vocabulary")
    print("    -> these are NOT agreement verdicts. This tool has NO opinion on them, and")
    print("       folding them into agree/disagree would report a denominator it does not have.")
    print("-" * 84)
    print("  ADVISORY ONLY -- classifies, does not block. Escalation to blocking is Andrew's.")
    print("  header-lags-body  = a FINDING (positive evidence: a close WAS found in the body).")
    print("                      Remedy: edit the header.")
    print("  body-lags-header  = a CANDIDATE, never a verdict. It rests on ABSENCE of a close")
    print("                      match in a corpus with NO FIXED SCHEMA, so it cannot")
    print("                      distinguish 'no close' from 'a close I could not parse'.")
    print("                      Remedy: a HUMAN READ of the named ledger -- not an alarm.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
