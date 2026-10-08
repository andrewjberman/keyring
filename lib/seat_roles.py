#!/usr/bin/env python3
"""seat_roles -- the ONE reader of org/ref/SEAT_ROLES.json (what each seat kind IS).

Pure stdlib. Every other reader resolves a serial to a kind ONLY through kind_of().

  python lib/seat_roles.py kind <serial>          print the kind (UNKNOWN, rc 3, when none or two match)
  python lib/seat_roles.py statement <serial>     print the text a seat is handed at start (rc 3 when UNKNOWN)
  python lib/seat_roles.py validate [serial ...]  check the file; each serial given must match exactly ONE kind

validate prints a last line  SEAT-ROLES kinds=<n> ... ok=<True|False>  and exits 0 only when ok=True.
The launcher (.tools/ajb.ps1) treats a non-zero exit, empty output or any failure as "no statement"
and launches anyway: this module must never be a launch dependency, only a launch aid.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROLES_PATH = ROOT / "org" / "ref" / "SEAT_ROLES.json"

SCHEMA = "seat-roles/1"
TOP_KEYS = {"schema", "source", "kinds"}
KIND_KEYS = {"kind", "serial_pattern", "is", "does", "does_not", "drives", "words"}
KINDS = ("MSTR", "CTO", "COO", "CVO", "CRO", "CLOUDOPS", "TIER2", "WORKER")
ANDREW_KINDS = ("MSTR", "CTO", "COO", "CVO", "CRO")
WORDS = ("andrew", "launcher")
UNKNOWN = "UNKNOWN"

_LANE = re.compile(r"~[A-Za-z0-9]+$")


def load(path=None) -> dict:
    """Read the file. A key this reader does not know is REFUSED (ValueError)."""
    p = Path(path) if path else ROLES_PATH
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("top level is not an object")
    extra = set(data) - TOP_KEYS
    if extra:
        raise ValueError("unknown top-level key(s): %s" % sorted(extra))
    kinds = data.get("kinds")
    if not isinstance(kinds, list):
        raise ValueError("kinds is not a list")
    for row in kinds:
        if not isinstance(row, dict):
            raise ValueError("a kinds row is not an object")
        extra = set(row) - KIND_KEYS
        if extra:
            raise ValueError("unknown key(s) in kind %r: %s" % (row.get("kind"), sorted(extra)))
    return data


def base_serial(serial: str) -> str:
    """Strip the lane suffix (~B, ~DELL1, ...): a lane shares its base serial's role."""
    return _LANE.sub("", serial.strip())


def kind_of(serial: str, data=None) -> str:
    """The kind whose serial_pattern matches the base serial; UNKNOWN when none or two match."""
    data = data if data is not None else load()
    base = base_serial(serial)
    hits = [row["kind"] for row in data["kinds"] if re.search(row["serial_pattern"], base)]
    return hits[0] if len(hits) == 1 else UNKNOWN


def _row(kind: str, data) -> dict:
    for row in data["kinds"]:
        if row["kind"] == kind:
            return row
    raise KeyError(kind)


def statement(kind: str, data=None) -> str:
    """The text a seat is handed: is, does, does not, drives. Plain ASCII, a few lines."""
    data = data if data is not None else load()
    row = _row(kind, data)
    who = "Andrew's recorded words" if row["words"] == "andrew" else "carried over from the launcher"
    out = ["SEAT STATEMENT [kind=%s] (org/ref/SEAT_ROLES.json; %s):" % (kind, who)]
    out.append("Is: " + row["is"])
    if row["does"]:
        out.append("Does:")
        out.extend("- " + item for item in row["does"])
    if row["does_not"]:
        out.append("Does not:")
        out.extend("- " + item for item in row["does_not"])
    if row["drives"]:
        out.append("Drives: " + " ".join("/" + name for name in row["drives"]))
    return "\n".join(out)


def validate(serials=(), data=None, skills_dir=None):
    """Return (problems, counts). Closed key set; non-empty is; drives are skill dirs; patterns compile;
    all eight kinds present once; ASCII only; every serial given matches exactly ONE kind."""
    problems = []
    try:
        data = data if data is not None else load()
    except Exception as exc:  # noqa: BLE001 - any failure to read is a validate failure
        return ["load failed: %s" % exc], {"kinds": 0, "drives": 0, "serials": 0}
    if data.get("schema") != SCHEMA:
        problems.append("schema is %r, want %r" % (data.get("schema"), SCHEMA))
    if not str(data.get("source", "")).strip():
        problems.append("source is empty")
    skills = Path(skills_dir) if skills_dir else ROOT / ".claude" / "skills"
    seen = []
    n_drives = 0
    for row in data["kinds"]:
        name = row.get("kind")
        seen.append(name)
        missing = KIND_KEYS - set(row)
        if missing:
            problems.append("%s: missing key(s) %s" % (name, sorted(missing)))
            continue
        if name not in KINDS:
            problems.append("kind %r is not one of %s" % (name, list(KINDS)))
        if not str(row["is"]).strip():
            problems.append("%s: empty is" % name)
        if row["words"] not in WORDS:
            problems.append("%s: words %r not in %s" % (name, row["words"], list(WORDS)))
        if name in ANDREW_KINDS and row["words"] != "andrew":
            problems.append("%s: one of his five kinds must carry words=andrew" % name)
        for field in ("does", "does_not", "drives"):
            if not isinstance(row[field], list) or not all(isinstance(x, str) and x.strip() for x in row[field]):
                problems.append("%s: %s is not a list of non-empty strings" % (name, field))
        try:
            re.compile(row["serial_pattern"])
        except re.error as exc:
            problems.append("%s: serial_pattern does not compile: %s" % (name, exc))
        for skill in row["drives"] if isinstance(row["drives"], list) else []:
            n_drives += 1
            if not (skills / str(skill)).is_dir():
                problems.append("%s: drives %r is not a directory under .claude/skills/" % (name, skill))
        blob = json.dumps(row)
        if any(ord(ch) > 127 for ch in blob):
            problems.append("%s: non-ASCII text" % name)
    for name in KINDS:
        if seen.count(name) != 1:
            problems.append("kind %s appears %d times, want 1" % (name, seen.count(name)))
    if not problems:
        for serial in serials:
            hits = [r["kind"] for r in data["kinds"] if re.search(r["serial_pattern"], base_serial(serial))]
            if len(hits) != 1:
                problems.append("serial %s matches %d kinds %s, want exactly 1" % (serial, len(hits), hits))
    return problems, {"kinds": len(data["kinds"]), "drives": n_drives, "serials": len(list(serials))}


def main(argv) -> int:
    if len(argv) >= 2 and argv[0] in ("kind", "statement"):
        try:
            data = load()
            kind = kind_of(argv[1], data)
            if kind == UNKNOWN:
                if argv[0] == "kind":
                    print(UNKNOWN)
                else:
                    sys.stderr.write("UNKNOWN: %s matches no single kind\n" % argv[1])
                return 3
            print(kind if argv[0] == "kind" else statement(kind, data))
            return 0
        except Exception as exc:  # noqa: BLE001
            sys.stderr.write("ERROR: %s\n" % exc)
            return 2
    if argv and argv[0] == "validate":
        serials = argv[1:]
        problems, counts = validate(serials)
        for p in problems:
            print("PROBLEM: " + p)
        ok = not problems
        print("SEAT-ROLES kinds=%d drives=%d serials=%d problems=%d ok=%s"
              % (counts["kinds"], counts["drives"], counts["serials"], len(problems), ok))
        return 0 if ok else 1
    sys.stderr.write(__doc__ or "")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
