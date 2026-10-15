#!/usr/bin/env python
"""Token census of the fabric value `site-z` / `sitez` (NFRA_CTLPLN.TO-CT-c-6; CLAUDE.md rule 24).

Scans TRACKED files (git ls-files) under .tools/, lib/, org/devices/, org/modules/, .claude/skills/,
org/standards/, org/surprise_channel/schemas/ (skips binaries and files over 1 MB). A HIT is a line where `site-z` or `sitez` appears on a
word boundary (case-insensitive) within the same line as, or within three lines of, the word `fabric`
(case-insensitive). Each hit is classified by the path-keyed table CLASS_BY_PATH below; a hit whose path is
not in the table is UNCLASSIFIED. The table was written by READING every hit (see the rule-24 record).

LAST line: FABRIC-CENSUS files_scanned=<f> hits=<h> enum_source=<e> compares=<c> display=<d> fixture=<x>
unclassified=<u> ok=<True|False>   (ok only when unclassified == 0).
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCOPE = (".tools/", "lib/", "org/devices/", "org/modules/", ".claude/skills/", "org/standards/", "org/surprise_channel/schemas/")
MAX_BYTES = 1024 * 1024
TOKEN = re.compile(r"(?<![A-Za-z0-9_])(site-z|sitez)(?![A-Za-z0-9_])", re.I)
FABRIC = re.compile(r"fabric", re.I)

ENUM_SOURCE, COMPARES, DISPLAY, FIXTURE = "ENUM-SOURCE", "COMPARES", "DISPLAY", "FIXTURE"
# Keyed by path (repo-relative, forward slashes). Filled by reading each hit.
# A key may be `path` (every hit in the file) or `path:line` (that one hit; checked first).
CLASS_BY_PATH = {
    # skills and comments that name the device/fabric in prose
    ".claude/skills/daily-sprint/SKILL.md": DISPLAY,
    ".claude/skills/govern/SKILL.md": DISPLAY,
    ".claude/skills/integrate-directives/SKILL.md": DISPLAY,
    ".claude/skills/integrate/SKILL.md": DISPLAY,
    ".claude/skills/mstr-kill/SKILL.md": DISPLAY,
    ".claude/skills/mstr-review/SKILL.md": DISPLAY,
    ".claude/skills/self-drive/SKILL.md": DISPLAY,
    ".tools/agentbus-sqs.sh": DISPLAY,
    ".tools/comp-system": DISPLAY,
    ".tools/hooks/presence-stamp.sh": DISPLAY,
    ".tools/integrate-directives.py": DISPLAY,
    ".tools/prd-header-notify.py": DISPLAY,
    ".tools/prd_signoff_lib.py": DISPLAY,
    ".tools/proof-of-spec-check.py": DISPLAY,
    "lib/research/filings/fetch.py": DISPLAY,
    "lib/research/social/collect.py": DISPLAY,
    "org/standards/test_artifact_coverage_both_grammars.py": DISPLAY,
    # test data
    ".tools/direct-act-order.py": FIXTURE,
    ".tools/sequence-check.py": FIXTURE,
    ".tools/tests/test_direct_act_order.py": FIXTURE,
    "org/devices/test_readers.py": FIXTURE,
    "org/modules/graph/tests/nerves_resolve_battery/run_battery.py": FIXTURE,
    # surprise-row-gate.py: since CT-d-6 NO line compares (the id-to-fabric derivation reads the device register);
    # the hits are comments, message text and self-test data
    ".tools/surprise-row-gate.py": DISPLAY,
    ".tools/surprise-row-gate.py:3537": FIXTURE,
    ".tools/surprise-row-gate.py:3539": FIXTURE,
    # the census's own files and the Dell tests, keyed PER LINE on purpose: a hit in a NEW file under .tools/tests/, or a new
    # line in one of these, stays UNCLASSIFIED until it is named here (there is no directory or wildcard key)
    ".tools/tests/fabric_value_census.py:2": DISPLAY,
    ".tools/tests/fabric_value_census.py:5": DISPLAY,
    ".tools/tests/fabric_value_census.py:23": FIXTURE,
    ".tools/tests/test_fabric_enum_dell.py:4": DISPLAY,
    ".tools/tests/test_fabric_enum_dell.py:63": FIXTURE,
    ".tools/tests/test_fabric_readers_dell.py:7": DISPLAY,
    ".tools/tests/test_fabric_readers_dell.py:10": DISPLAY,
    ".tools/tests/test_fabric_readers_dell.py:92": FIXTURE,
    ".tools/tests/test_fabric_readers_dell.py:145": FIXTURE,
    ".tools/tests/test_fabric_readers_dell.py:101": FIXTURE,
    ".tools/tests/test_fabric_readers_dell.py:154": FIXTURE,
    # the manager-on-every-box test: a probe list of RETIRED two-box wording that the skill prose must not carry
    # (a negative phrase search over prose; no box list decides a value here)
    ".tools/tests/test_manager_on_every_box.py:266": FIXTURE,
    # the device register's own docstring: the alias form of a box name, described in prose
    "lib/devices.py:84": DISPLAY,
    # the allowed sets
    ".tools/to-pipeline-gate.py": DISPLAY,
    ".tools/to-pipeline-gate.py:93": ENUM_SOURCE,
    "org/devices/DEVICES.json": ENUM_SOURCE,
    "org/standards/PRD_HEADER.schema.json": ENUM_SOURCE,
    # the two surprise-row schemas carry the fabric enum (the Draft-07 limb of the surprise-row gate validates against them)
    "org/surprise_channel/schemas/investigation_item.schema.json": ENUM_SOURCE,
    "org/surprise_channel/schemas/remediation_row.schema.json": ENUM_SOURCE,
}


def tracked_files():
    out = subprocess.run(["git", "ls-files", "-z", "--"] + [s.rstrip("/") for s in SCOPE], cwd=ROOT,
                         capture_output=True, check=True).stdout
    return [p for p in out.decode("utf-8", "replace").split("\0") if p]


def read_text(rel):
    full = os.path.join(ROOT, rel)
    try:
        if os.path.getsize(full) > MAX_BYTES:
            return None
        with open(full, "rb") as fh:
            raw = fh.read()
    except OSError:
        return None
    if b"\0" in raw:
        return None
    return raw.decode("utf-8", "replace")


def parse_args(argv):
    ap = argparse.ArgumentParser(description="token census plus the register box names (FWD-2 read-back)")
    ap.add_argument("--register", default=os.path.join(ROOT, "org", "devices", "DEVICES.json"),
                    help="device register whose box names are printed on the BOXES-READ line (default: the real register)")
    return ap.parse_args(argv)


def register_box_names(path):
    """The box names of a register file (read as JSON; this census compares against no box list)."""
    with open(path, encoding="utf-8") as fh:
        return sorted(d["name"] for d in json.load(fh)["devices"])


def main(argv=None):
    args = parse_args(argv)
    files = tracked_files()
    scanned = 0
    hits = []
    for rel in files:
        text = read_text(rel)
        if text is None:
            continue
        scanned += 1
        lines = text.splitlines()
        fab = [i for i, ln in enumerate(lines) if FABRIC.search(ln)]
        if not fab:
            continue
        for i, ln in enumerate(lines):
            if TOKEN.search(ln) and any(abs(i - j) <= 3 for j in fab):
                hits.append((rel, i + 1, ln.strip()[:140]))
    counts = {ENUM_SOURCE: 0, COMPARES: 0, DISPLAY: 0, FIXTURE: 0, "UNCLASSIFIED": 0}
    for rel, n, snip in hits:
        cls = CLASS_BY_PATH.get("%s:%d" % (rel, n)) or CLASS_BY_PATH.get(rel, "UNCLASSIFIED")
        counts[cls] += 1
        print("%s:%d  %s  | %s" % (rel, n, cls, snip))
    print("BOXES-READ " + " ".join(register_box_names(args.register)))
    ok = counts["UNCLASSIFIED"] == 0
    print("FABRIC-CENSUS files_scanned=%d hits=%d enum_source=%d compares=%d display=%d fixture=%d "
          "unclassified=%d ok=%s" % (scanned, len(hits), counts[ENUM_SOURCE], counts[COMPARES],
                                     counts[DISPLAY], counts[FIXTURE], counts["UNCLASSIFIED"], ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
