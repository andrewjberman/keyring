#!/usr/bin/env python3
"""apply-who-check.py -- who may apply (NFRA_CTLPLN workstream SEATS, cell CT-s-3). READ-ONLY: it changes nothing.

    python .tools/apply-who-check.py --serial <serial> --root <terraform root dir> [--target <address> ...]
        [--orders-root <dir>]

LAST line:  APPLY-WHO serial=<s> kind=<k> root=<name> verdict=<ADMITTED|REFUSED> reason=<...>
The line before it names which source resolved the kind (module, file or built-in).
Exit: 0 ADMITTED, 1 REFUSED, 2 a usage or read error (the wrappers treat rc 2 as a WARN, never as a verdict).

THE RULE (data, here; cited from org/ref/SEAT_RULES.json when that file is present):
  an apply is made by a CLOUDOPS seat, or by a TIER2 seat that holds a non-terminal task order issued to it.
  MSTR, CTO, COO, CVO, CRO, WORKER and UNKNOWN are REFUSED (a COO spawns the worker and cuts the order; it does not apply).

KIND RESOLUTION, in this precedence, the source printed:
  1. module  lib/seat_roles.py kind_of(serial)   (cell CT-s-1 writes it)
  2. file    org/ref/SEAT_ROLES.json             (schema seat-roles/1: kinds[].kind and kinds[].serial_pattern)
  3. built-in the table below, derived from the launcher's patterns (.tools/ajb.ps1 Get-AgentLoopDirective)
A serial that matches nothing is UNKNOWN, never guessed. The lane suffix (~...) is stripped before matching.
"""
from __future__ import annotations

import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RULE_ID = "R-AWSDEVOPS-apply-who"
ADMIT_ALWAYS = ("CLOUDOPS",)
ADMIT_UNDER_ORDER = ("TIER2",)
KINDS = ("MSTR", "CTO", "COO", "CVO", "CRO", "CLOUDOPS", "TIER2", "WORKER")
TERMINAL_TO = {"complete", "superseded", "cancelled"}

# Built-in table, ORDER MATTERS (first match wins; CLOUDOPS before TIER2 because _AE_ is in both).
BUILTIN = (
    ("MSTR", r"^0\.0\.0_AB_MSTR$"),
    ("CTO", r"^1\.[0-9]+\.0_SA_CTO$"),
    ("COO", r"^2\.[0-9]+\.0_SA_COO$"),
    ("CVO", r"^3\.[0-9]+\.0_SA_CVO$"),
    ("CRO", r"^4\.[0-9]+\.0_SA_CRO$"),
    ("CLOUDOPS", r"^0\.[0-9]+\.[0-9]+_AE_CloudOps$"),
    ("CLOUDOPS", r"^0\.8\.0_AE_CloudComp$"),
    ("WORKER", r"^0\.9\.0_WK_[A-Za-z0-9_]+$"),
    ("TIER2", r"^0\.[0-9]+\.[0-9]+_(DS|AE|DE|DT|RD)_[A-Za-z0-9_]+$"),
    ("TIER2", r"^1\.[0-9]+\.[0-9]+_DS_CompLearns$"),
    ("TIER2", r"^2\.1\.0_SC_CompLearns$"),
)
LANE_RE = re.compile(r"~[A-Za-z0-9]+$")
ISSUED_RE = re.compile(r"<issued_to>\s*([^<\s]+)\s*</issued_to>")
STATUS_RE = re.compile(r"<status>\s*([^<\s]+)\s*</status>")
TOID_RE = re.compile(r"<to_id>\s*([^<\s]+)\s*</to_id>")


def base_of(serial: str) -> str:
    return LANE_RE.sub("", serial.strip())


def kind_from_module(serial: str, root: str):
    path = os.path.join(root, "lib", "seat_roles.py")
    if not os.path.isfile(path):
        return None
    spec = importlib.util.spec_from_file_location("opal_seat_roles", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    got = mod.kind_of(serial)
    if isinstance(got, dict):
        got = got.get("kind")
    got = getattr(got, "kind", got)
    got = str(got or "").strip().upper()
    return (got if got in KINDS else "UNKNOWN", "module lib/seat_roles.py kind_of")


def kind_from_file(serial: str, root: str):
    path = os.path.join(root, "org", "ref", "SEAT_ROLES.json")
    if not os.path.isfile(path):
        return None
    data = json.load(open(path, encoding="utf-8"))
    base = base_of(serial)
    for row in data["kinds"]:
        if re.search(row["serial_pattern"], base):
            return (str(row["kind"]).upper(), "file org/ref/SEAT_ROLES.json")
    return ("UNKNOWN", "file org/ref/SEAT_ROLES.json")


def kind_from_builtin(serial: str):
    base = base_of(serial)
    for kind, pattern in BUILTIN:
        if re.search(pattern, base):
            return (kind, "built-in table (module and file absent or unreadable)")
    return ("UNKNOWN", "built-in table (module and file absent or unreadable)")


def resolve_kind(serial: str, root: str = ROOT) -> tuple:
    """(kind, source text, notes). Precedence module, file, built-in; an unusable higher source is a note, never silent."""
    notes = []
    for label, fn in (("module", kind_from_module), ("file", kind_from_file)):
        try:
            got = fn(serial, root)
        except Exception as exc:  # a broken higher source falls through, said so
            notes.append("%s source unusable (%s: %s)" % (label, type(exc).__name__, exc))
            continue
        if got:
            return got[0], got[1], notes
    kind, source = kind_from_builtin(serial)
    return kind, source, notes


def find_order(serial: str, orders_root: str) -> str | None:
    """The to_id of a NON-terminal task order issued to this serial (exact serial, or its base), else None."""
    want = {serial.strip(), base_of(serial)}
    pattern = os.path.join(orders_root, "D*", "*", "*", "task-orders", "*.md")
    for path in glob.glob(pattern):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                head = fh.read(4000)
        except OSError:
            continue
        issued = ISSUED_RE.search(head)
        if not issued or issued.group(1) not in want:
            continue
        status = STATUS_RE.search(head)
        if status and status.group(1).lower() in TERMINAL_TO:
            continue
        toid = TOID_RE.search(head)
        return toid.group(1) if toid else os.path.basename(path)
    return None


def rule_citation(root: str) -> str:
    path = os.path.join(root, "org", "ref", "SEAT_RULES.json")
    if not os.path.isfile(path):
        return "org/ref/SEAT_RULES.json absent (rule held in this script's head as %s)" % RULE_ID
    try:
        rules = json.load(open(path, encoding="utf-8"))["rules"]
        ids = [r["id"] for r in rules if r.get("area") == "AWSDEVOPS" and "apply" in str(r.get("rule", "")).lower()]
        return "org/ref/SEAT_RULES.json AWSDEVOPS rules naming apply: %s" % (", ".join(ids) or "none")
    except Exception as exc:
        return "org/ref/SEAT_RULES.json unreadable (%s); rule held here as %s" % (type(exc).__name__, RULE_ID)


def decide(serial: str, root_dir: str, orders_root: str, repo_root: str = ROOT) -> dict:
    kind, source, notes = resolve_kind(serial, repo_root)
    name = os.path.basename(root_dir.rstrip("/\\")) or root_dir
    if kind in ADMIT_ALWAYS:
        verdict, reason = "ADMITTED", "a CLOUDOPS seat applies"
    elif kind in ADMIT_UNDER_ORDER:
        order = find_order(serial, orders_root)
        if order:
            verdict, reason = "ADMITTED", "a TIER2 seat under task order %s" % order
        else:
            verdict, reason = "REFUSED", "a TIER2 seat applies only under a task order and none non-terminal is issued to it"
    elif kind == "UNKNOWN":
        verdict, reason = "REFUSED", "the serial matches no seat kind and is never guessed"
    elif kind == "WORKER":
        verdict, reason = "REFUSED", "a WORKER does not apply; its issuer's CLOUDOPS or TIER2 seat applies"
    else:
        verdict, reason = "REFUSED", "a %s does not apply; it cuts or spawns, a CLOUDOPS or TIER2 seat applies" % kind
    return {"serial": serial, "kind": kind, "root": name, "verdict": verdict, "reason": reason,
            "source": source, "notes": notes, "rule": rule_citation(repo_root)}


def render(res: dict, targets: list) -> str:
    lines = ["KIND-SOURCE serial=%s kind=%s source=%s" % (res["serial"], res["kind"], res["source"])]
    for note in res["notes"]:
        lines.append("KIND-NOTE %s" % note)
    lines.append("RULE %s: %s; targets=%d" % (RULE_ID, res["rule"], len(targets)))
    lines.append("APPLY-WHO serial=%s kind=%s root=%s verdict=%s reason=%s" % (
        res["serial"], res["kind"], res["root"], res["verdict"], res["reason"]))
    return "\n".join(lines)


def main(argv: list) -> int:
    serial, root_dir, targets, orders = "", "", [], os.path.join(ROOT, "org", "missions")
    i = 0
    try:
        while i < len(argv):
            arg = argv[i]
            if arg == "--serial":
                serial = argv[i + 1]
                i += 2
            elif arg == "--root":
                root_dir = argv[i + 1]
                i += 2
            elif arg == "--target":
                targets.append(argv[i + 1])
                i += 2
            elif arg == "--orders-root":
                orders = argv[i + 1]
                i += 2
            else:
                raise ValueError("unknown argument %r" % arg)
        if not serial or not root_dir:
            raise ValueError("--serial and --root are required")
    except (IndexError, ValueError) as exc:
        print("ERROR: %s\nusage: apply-who-check.py --serial <serial> --root <dir> [--target <address> ...]" % exc,
              file=sys.stderr)
        return 2
    res = decide(serial, root_dir, orders)
    print(render(res, targets))
    return 0 if res["verdict"] == "ADMITTED" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
