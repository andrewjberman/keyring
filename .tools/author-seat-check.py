#!/usr/bin/env python3
"""author-seat-check.py -- does a commit's --author serial name a known seat? WARN-only (no refusal yet).

Ruling: 1.0.0_SA_CTO msg 107910, on 4.0.0_SA_CRO~A's finding (107903) that safe-commit admitted
--author 9.9.9_XX_NoSuchSeat on lane-ANY paths. "yes, check it, but WARN first ... A refusal follows after a week of WARN
rows, announced to every manager first." Owner of this file: 4.0.0_SA_CRO~A. Called by .tools/safe-commit.sh.

A serial is KNOWN when its BASE (the serial without its ~lane) is:
  (1) matched by a seat kind's serial_pattern in org/ref/SEAT_ROLES.json (MSTR, CTO, COO, CVO, CRO, CLOUDOPS, TIER2,
      WORKER -- the WORKER pattern is the 0.9.0_WK_<CODE> grammar, so every worker matches by grammar); or
  (2) the base of a serial some lane in .owned-paths.yaml names in permitted_agents.
Anything else prints one line on stderr, "WARN: author <serial> names no known seat", and the commit goes on.

USAGE:  python .tools/author-seat-check.py <serial>      rc 0 always (WARN-only); prints nothing for a known seat
        python .tools/author-seat-check.py --self-test   arms; rc 1 if any arm fails
A register that cannot be read prints a WARN naming it, never a silent pass: an unreadable register cannot say the
author is known.
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERIAL_RE = re.compile(r"^\d+\.\d+\.\d+_[A-Z]{2}_[A-Za-z0-9_]+(~[A-Za-z0-9_-]+)?$")


def base(serial: str) -> str:
    return serial.split("~", 1)[0]


def known_patterns(root: str = ROOT) -> tuple:
    """(regex list, base-serial set, problems) from the two registers."""
    pats, bases, problems = [], set(), []
    try:
        with open(os.path.join(root, "org", "ref", "SEAT_ROLES.json"), encoding="utf-8") as fh:
            for k in json.load(fh).get("kinds", []):
                if isinstance(k, dict) and k.get("serial_pattern"):
                    pats.append(re.compile(k["serial_pattern"]))
    except Exception as exc:  # noqa: BLE001
        problems.append("org/ref/SEAT_ROLES.json unreadable (%s)" % type(exc).__name__)
    try:
        import yaml
        with open(os.path.join(root, ".owned-paths.yaml"), encoding="utf-8") as fh:
            lanes = (yaml.safe_load(fh) or {}).get("lanes") or {}
        for lane in lanes.values():
            for s in (lane or {}).get("permitted_agents") or []:
                s = str(s).strip()
                if SERIAL_RE.match(s):
                    bases.add(base(s))
    except Exception as exc:  # noqa: BLE001
        problems.append(".owned-paths.yaml unreadable (%s)" % type(exc).__name__)
    return pats, bases, problems


def check(serial: str, root: str = ROOT) -> str | None:
    """None when the serial names a known seat; else the WARN line."""
    serial = (serial or "").strip()
    pats, bases, problems = known_patterns(root)
    b = base(serial)
    if serial and (b in bases or any(p.search(b) for p in pats)):
        return None
    why = "; ".join(problems)
    return ("WARN: author %s names no known seat (not in org/ref/SEAT_ROLES.json serial patterns, not a permitted_agents "
            "base in .owned-paths.yaml%s). WARN-only until the announced refusal (1.0.0_SA_CTO msg 107910)."
            % (serial or "<empty>", "; " + why if why else ""))


def self_test() -> int:
    arms = [
        ("a known Tier-1 seat with a lane is silent", "4.0.0_SA_CRO~A", True),
        ("the manager base is silent", "0.0.0_AB_MSTR", True),
        ("a worker matches by grammar", "0.9.0_WK_NFRA_GATSCP~2", True),
        ("a CloudOps lane is silent", "0.7.0_AE_CloudOps~DELL2", True),
        ("a made-up serial warns", "9.9.9_XX_NoSuchSeat", False),
        ("an empty author warns", "", False),
    ]
    fails = 0
    for name, serial, want_known in arms:
        got_known = check(serial) is None
        ok = got_known == want_known
        fails += not ok
        print(("PASS  " if ok else "FAIL  ") + name + " (%s)" % (serial or "<empty>"))
    print("RESULT: %d of %d failed" % (fails, len(arms)))
    return 1 if fails else 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        sys.exit(self_test())
    line = check(sys.argv[1] if len(sys.argv) > 1 else "")
    if line:
        print(line, file=sys.stderr)
    sys.exit(0)
