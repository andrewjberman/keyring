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


CHANNEL_FILE_RE = re.compile(r"(INVESTIGATION|REMEDIATION)_v[^/\\]*\.(md|json)$")


def _collect(val, rows) -> int:
    """Append object rows; return the count of NON-object items (each one a defect, never dropped)."""
    if isinstance(val, dict):
        rows.append(val)
        return 0
    if isinstance(val, list):
        bad = 0
        for item in val:
            if isinstance(item, dict):
                rows.append(item)
            else:
                bad += 1
        return bad
    return 1


def _rows(text: str, raw_json: bool = False):
    """Rows + malformed count. raw_json=True parses the whole body (a .json channel file) --
    MARKDOWN/JSON PARITY with surprise-row-gate.py, which admits both (CVO~A re-grade 2026-09-02:
    JSON channel rows were unwatermarked and unvalidated because this parser was fenced-only)."""
    rows, bad = [], 0
    if raw_json:
        try:
            val = json.loads(text)
        except ValueError:
            return rows, 1
        return rows, _collect(val, rows)
    for m in FENCE_RE.finditer(text):
        try:
            val = json.loads(m.group(1))
        except ValueError:
            bad += 1
            continue
        bad += _collect(val, rows)
    return rows, bad


def _channel_docs(root: str) -> list:
    """Every channel document, .md AND .json, in a stable order."""
    base = os.path.join(root, "org", "surprise_channel")
    found = []
    for pattern in ("*/*.md", "*/*.json"):
        found.extend(p for p in glob.glob(os.path.join(base, pattern))
                     if CHANNEL_FILE_RE.search(os.path.basename(p)))
    return sorted(found)


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
    docs = _channel_docs(root)
    stats = {"documents": 0, "rows": 0, "malformed_blocks": 0, "failures": 0}
    failures = []
    for path in docs:
        stats["documents"] += 1
        rel = os.path.relpath(path, root).replace("\\", "/")
        with open(path, encoding="utf-8", errors="replace") as fh:
            rows, bad = _rows(fh.read(), raw_json=path.lower().endswith(".json"))
        stats["malformed_blocks"] += bad
        validator = validators[_kind(path)]
        for row in rows:
            stats["rows"] += 1
            for err in sorted(validator.iter_errors(row), key=lambda e: list(e.path)):
                failures.append(_tuple(rel, row, err))
    stats["failures"] = len(failures)
    return stats, failures


def _load_baseline(root: str):
    """The baseline tuple set, or None when NO BASELINE FILE EXISTS.

    CVO~A re-grade 2026-09-02, RC4 hole 5: returning an empty set for BOTH a missing file and a
    legitimate zero-tuple baseline meant that once the legacy four were normalized to zero, a
    DELETED baseline file would grade as "matches the baseline". Presence is explicit: None means
    absent and is refused regardless of what the corpus looks like; an empty set means a present
    file that says "zero known failures", which is the state normalization is aiming for."""
    path = os.path.join(root, BASELINE_REL)
    if not os.path.exists(path):
        return None
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


def _canon_hash(row: dict) -> str:
    blob = json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]


def index(root: str) -> list:
    """RC2 (CVO~A re-grade @0dbf12ebb3, the watcher half): one line per row, `path\\tid\\thash`.

    surprise-watch.sh diffs this against its stored copy each poll. A same-id hash change is a
    MUTATION and an id that disappears is a DELETION -- both invisible to a row COUNT, which is
    all the watcher had. Read-only over the channel; the watcher writes only its own state."""
    lines = []
    for path in _channel_docs(root):
        rel = os.path.relpath(path, root).replace("\\", "/")
        with open(path, encoding="utf-8", errors="replace") as fh:
            rows, _ = _rows(fh.read(), raw_json=path.lower().endswith(".json"))
        for row in rows:
            rid = row.get("id")
            if rid:
                lines.append("%s\t%s\t%s" % (rel, rid, _canon_hash(row)))
    return lines


def main(argv: list) -> int:
    root = _root()
    if "--index" in argv:
        # LF only, even on Windows: the consumer is a bash watcher comparing hashes byte-for-byte,
        # and text-mode stdout here would emit \r\n (measured 2026-09-02: 191 false MUTATIONs).
        try:
            sys.stdout.reconfigure(newline="\n")
        except (AttributeError, ValueError):
            pass
        for line in index(root):
            sys.stdout.write(line + "\n")
        return 0
    as_json = "--json" in argv
    stats, failures = sweep(root)
    current = {tuple(t) for t in failures}

    if "--write-baseline" in argv:
        _write_baseline(root, failures, stats)
        print("[surprise-corpus] BASELINE WRITTEN: %d tuple(s) over %d rows / %d documents -> %s"
              % (len(current), stats["rows"], stats["documents"], BASELINE_REL))
        return 0

    baseline = _load_baseline(root)
    if baseline is None:
        print("[surprise-corpus] DENOMINATORS: documents=%d rows=%d malformed_blocks=%d failures=%d "
              "baseline=ABSENT" % (stats["documents"], stats["rows"], stats["malformed_blocks"],
                                    stats["failures"]))
        print("[surprise-corpus] REFUSED: no baseline file at %s. Presence is explicit -- write one "
              "deliberately (--write-baseline), even when it holds zero tuples." % BASELINE_REL,
              file=sys.stderr)
        return 1
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

    if stats["malformed_blocks"]:
        # RC4 hole 2 (CVO~A re-grade): the malformed count was printed and never graded. A block that
        # does not parse is a row nobody can validate; it fails the pass, not just the display.
        print("[surprise-corpus] REFUSED: %d malformed block(s)/item(s) in the corpus. A row that does "
              "not parse is not a known failure, it is an unvalidated one." % stats["malformed_blocks"],
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
