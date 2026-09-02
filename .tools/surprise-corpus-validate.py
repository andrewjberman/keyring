#!/usr/bin/env python3
"""surprise-corpus-validate -- RC4 (CVO~A @0d272d257c release condition 4).

THE STANDING FULL-CORPUS PASS over org/surprise_channel/**. Every fenced JSON row in every
INVESTIGATION_v*/REMEDIATION_v* document is validated against its schema with the FULL
Draft-07 validator, and the result is graded against an EXACT LEGACY BASELINE -- a set of
(document, id, json_pointer, failure_digest) tuples, never the bare count.

WHY IT EXISTS: surprise-row-gate.py is PROSPECTIVE-ONLY by design -- it grades rows NEW in a
commit. Correct for adoption, and its unstated consequence was that the channel's EXISTING
contents were unvalidated by anything: "does the channel conform to its own schemas?" had
been UNKNOWN, not YES. Measured 2026-09-02: 192 rows, 4 failures, invisible to every gate.

WHY AN EXACT-TUPLE BASELINE AND NOT THE NUMBER 4: a count lets one legacy failure be quietly
SWAPPED for a new one at the same count. Tuples make three states distinguishable and each
is reported on its own line: NEW (fail), RESOLVED (fail -- the baseline must be re-written
deliberately, under CVO-owned normalization, never silently shrunk by a passing run), and
BASELINE (known, tolerated, counted). The four known legacy rows do not block unrelated
appends; a fifth does.

USAGE
  surprise-corpus-validate.py                 grade against the committed baseline; exit 1 on
                                              any NEW or RESOLVED tuple
  surprise-corpus-validate.py --write-baseline  (re)write the baseline from the current corpus.
                                              A CVO act by ruling; the tool does not gate that,
                                              the lane does.
  surprise-corpus-validate.py --json          machine-readable summary on stdout

Every run prints its DENOMINATORS: documents, rows, malformed blocks, failures, baseline size,
new, resolved. A denominator certifies the SWEEP, not the schema -- a wrong schema passes
every row it does not describe.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import subprocess
import sys

FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)
BASELINE_REL = "org/surprise_channel/.corpus-baseline.json"


def _root() -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except OSError:
        pass
    return os.getcwd()


def _kind(path: str) -> str:
    return "REMEDIATION" if "REMEDIATION" in os.path.basename(path).upper() else "INVESTIGATION"


def _schemas(root: str) -> dict:
    base = os.path.join(root, "org", "surprise_channel", "schemas")
    with open(os.path.join(base, "investigation_item.schema.json"), encoding="utf-8") as fh:
        inv = json.load(fh)
    with open(os.path.join(base, "remediation_row.schema.json"), encoding="utf-8") as fh:
        rem = json.load(fh)
    return {"INVESTIGATION": inv, "REMEDIATION": rem}


def _rows(text: str):
    rows, bad = [], 0
    for m in FENCE_RE.finditer(text):
        try:
            val = json.loads(m.group(1))
        except ValueError:
            bad += 1
            continue
        if isinstance(val, list):
            rows.extend(v for v in val if isinstance(v, dict))
        elif isinstance(val, dict):
            rows.append(val)
    return rows, bad


def _tuple(doc: str, row: dict, err) -> list:
    ptr = "/" + "/".join(str(p) for p in err.path) if err.path else "/"
    digest = hashlib.sha256(err.message.encode("utf-8")).hexdigest()[:12]
    return [doc, str(row.get("id", "<no id>")), ptr, digest]


def sweep(root: str):
    """Return (stats, failures) where failures is a list of 4-tuples (as lists)."""
    try:
        import jsonschema
    except ImportError:
        print("ERROR: jsonschema is not importable -- the corpus pass cannot run. Fail-closed.",
              file=sys.stderr)
        sys.exit(2)
    schemas = _schemas(root)
    validators = {k: jsonschema.Draft7Validator(v) for k, v in schemas.items()}
    pattern = os.path.join(root, "org", "surprise_channel", "*", "*.md")
    docs = sorted(p for p in glob.glob(pattern)
                  if re.search(r"(INVESTIGATION|REMEDIATION)_v[^/\\]*\.md$", os.path.basename(p)))
    stats = {"documents": 0, "rows": 0, "malformed_blocks": 0, "failures": 0}
    failures = []
    for path in docs:
        stats["documents"] += 1
        rel = os.path.relpath(path, root).replace("\\", "/")
        with open(path, encoding="utf-8", errors="replace") as fh:
            rows, bad = _rows(fh.read())
        stats["malformed_blocks"] += bad
        validator = validators[_kind(path)]
        for row in rows:
            stats["rows"] += 1
            for err in sorted(validator.iter_errors(row), key=lambda e: list(e.path)):
                failures.append(_tuple(rel, row, err))
    stats["failures"] = len(failures)
    return stats, failures


def _load_baseline(root: str) -> set:
    path = os.path.join(root, BASELINE_REL)
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return {tuple(t) for t in data.get("tuples", [])}


def _write_baseline(root: str, failures: list, stats: dict) -> None:
    path = os.path.join(root, BASELINE_REL)
    payload = {
        "_comment": ("EXACT legacy failure tuples (document, id, json_pointer, failure_digest). "
                     "Re-written ONLY deliberately, under CVO-owned normalization (CVO~A @0d272d257c "
                     "RC4). A passing run never shrinks this set. Retire to zero; do not grow."),
        "written_at_rows": stats["rows"],
        "written_at_documents": stats["documents"],
        "tuples": sorted(failures),
    }
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


def main(argv: list) -> int:
    root = _root()
    as_json = "--json" in argv
    stats, failures = sweep(root)
    current = {tuple(t) for t in failures}

    if "--write-baseline" in argv:
        _write_baseline(root, failures, stats)
        print("[surprise-corpus] BASELINE WRITTEN: %d tuple(s) over %d rows / %d documents -> %s"
              % (len(current), stats["rows"], stats["documents"], BASELINE_REL))
        return 0

    baseline = _load_baseline(root)
    new = sorted(current - baseline)
    resolved = sorted(baseline - current)
    known = sorted(current & baseline)

    summary = dict(stats, baseline=len(baseline), new=len(new), resolved=len(resolved), known=len(known))
    if as_json:
        print(json.dumps({"summary": summary, "new": new, "resolved": resolved, "known": known}, indent=1))
    else:
        print("[surprise-corpus] DENOMINATORS: documents=%d rows=%d malformed_blocks=%d failures=%d "
              "baseline=%d known=%d new=%d resolved=%d"
              % (stats["documents"], stats["rows"], stats["malformed_blocks"], stats["failures"],
                 len(baseline), len(known), len(new), len(resolved)))
        for t in new:
            print("  NEW      %s  %s  %s  %s" % tuple(t))
        for t in resolved:
            print("  RESOLVED %s  %s  %s  %s  <- re-baseline deliberately (CVO), a passing run "
                  "never shrinks the set" % tuple(t))
        for t in known:
            print("  KNOWN    %s  %s  %s" % (t[0], t[1], t[2]))

    if not baseline and current:
        print("[surprise-corpus] REFUSED: no baseline at %s and the corpus has %d failure(s). "
              "Write one deliberately (--write-baseline) before grading." % (BASELINE_REL, len(current)),
              file=sys.stderr)
        return 1
    if new or resolved:
        print("[surprise-corpus] REFUSED: %d NEW failure(s), %d RESOLVED baseline tuple(s). The set moved."
              % (len(new), len(resolved)), file=sys.stderr)
        return 1
    print("[surprise-corpus] OK: corpus matches the exact legacy baseline (%d known, 0 new, 0 resolved)."
          % len(known))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
