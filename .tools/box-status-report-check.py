#!/usr/bin/env python3
"""box-status-report-check.py -- validate a BOX STATUS REPORT (the form in
org/tier1_exec/1.0.0_SA_CTO/deliverables/BOX_STATUS_REPORT_FORM_20261013.md) and print its denominators.

    python .tools/box-status-report-check.py <report.md> [--json]
    python .tools/box-status-report-check.py --aggregate <report.md> [<report.md> ...]   # one table across boxes

Exit 0 = OK (every YAML block parses, the header and every project block carry every required key, enum values are legal,
the union count equals the number of project blocks). Exit 1 = REFUSED, with every defect listed. ASCII only.
Andrew-direct 2026-10-13 ~12:3xZ (ANDREW_DIRECT_20261013_123xZ_BOX_STATUS_REPORTS_FOR_THE_LAPTOP_AUDIT_AND_REALLOCATION.md).
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import sys

try:
    import yaml  # PyYAML, installed on every box
except ImportError:  # pragma: no cover
    print("REFUSED: PyYAML is not installed; the validator cannot parse the blocks", file=sys.stderr)
    sys.exit(2)

BLOCK_RE = re.compile(r"```yaml\s*\n(.*?)\n```", re.S)
HEADER_KEYS = ["box", "author", "as_of_utc", "branch_pin", "population", "seats_live", "seats_by_role", "account_state",
               "open_deploy_ledgers", "scheduled_jobs_owned", "open_calls_this_box", "crossbox_open_to_this_box"]
POP_KEYS = ["register_placed", "live_seat_named", "open_order_named", "union"]
PROJECT_KEYS = ["project", "macro", "placement", "status_register", "repos", "client_facing", "client_surface", "intent",
                "desired_outcome_when_done", "status", "seats_on_this_box", "dependencies", "blockers", "next", "andrew_acts",
                "footprint", "if_parked_this_week", "cro_rec", "cro_rec_why"]
STATUS_KEYS = ["round", "dep_stage", "fwd_realized", "last_l10_utc", "open_orders", "last_commit_utc"]
FOOTPRINT_KEYS = ["commits_7d", "seats", "aws_resources_owned", "scheduled_jobs", "open_deploy_ledgers", "standing_holds"]


def _register_boxes() -> set:
    """The box names the device register holds (lib/devices.py names(), NFRA_CTLPLN FWD-2): a box is added once, in
    org/devices/DEVICES.json. Fail-closed: an unreadable register REFUSES (exit 2); it never falls back to a list."""
    spec = importlib.util.spec_from_file_location(
        "opal_devices_for_report", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib", "devices.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    try:
        return set(mod.names())
    except mod.RegisterError as exc:
        print("REFUSED: %s" % exc, file=sys.stderr)
        sys.exit(2)


BOXES = _register_boxes()
REPOS = {"ajb_workspace", "portal", "opal_ai", "mcportal", "aws-infra"}
CLIENT = {"yes", "indirect", "no"}
REC_RE = re.compile(r"^(KEEP|PARK|CLOSE|MERGE_INTO:[A-Z0-9_]+)$")


def load(path: str):
    text = open(path, encoding="utf-8").read()
    blocks = []
    for i, m in enumerate(BLOCK_RE.finditer(text), 1):
        try:
            blocks.append((i, yaml.safe_load(m.group(1))))
        except yaml.YAMLError as exc:
            blocks.append((i, {"__error__": "block %d does not parse: %s" % (i, str(exc).splitlines()[0])}))
    return text, blocks


def check(path: str):
    """(ok, defects, header, projects)."""
    defects = []
    _, blocks = load(path)
    if not blocks:
        return False, ["no ```yaml block found"], None, []
    header = blocks[0][1] if isinstance(blocks[0][1], dict) else None
    if header is None or "box" not in header:
        defects.append("the first yaml block is not the header (no `box` key)")
        header = header or {}
    for k in HEADER_KEYS:
        if k not in header:
            defects.append("header: missing key %s" % k)
    if header.get("box") not in BOXES:
        defects.append("header: box %r is not one of %s" % (header.get("box"), sorted(BOXES)))
    pop = header.get("population") if isinstance(header.get("population"), dict) else {}
    for k in POP_KEYS:
        if k not in pop:
            defects.append("header.population: missing key %s" % k)
    projects = []
    for i, b in blocks[1:]:
        if not isinstance(b, dict):
            defects.append("block %d is not a mapping" % i)
            continue
        if "__error__" in b:
            defects.append(b["__error__"])
            continue
        code = b.get("project", "<no project key>")
        for k in PROJECT_KEYS:
            if k not in b:
                defects.append("%s (block %d): missing key %s" % (code, i, k))
        st = b.get("status") if isinstance(b.get("status"), dict) else {}
        for k in STATUS_KEYS:
            if k not in st:
                defects.append("%s: status missing key %s" % (code, k))
        fp = b.get("footprint") if isinstance(b.get("footprint"), dict) else {}
        for k in FOOTPRINT_KEYS:
            if k not in fp:
                defects.append("%s: footprint missing key %s" % (code, k))
        repos = b.get("repos") or []
        bad = [r for r in repos if r not in REPOS]
        if bad:
            defects.append("%s: repos %s not in %s" % (code, bad, sorted(REPOS)))
        # A bare `yes` / `no` is a YAML 1.1 boolean (laptop CRO msg 108743, 2026-10-13): read it as the enum it was typed as,
        # so an author need not quote it. `true`/`false` read the same way; `indirect` stays a string.
        if isinstance(b.get("client_facing"), bool):
            b["client_facing"] = "yes" if b["client_facing"] else "no"
        if b.get("client_facing") not in CLIENT:
            defects.append("%s: client_facing %r not in %s" % (code, b.get("client_facing"), sorted(CLIENT)))
        if not REC_RE.match(str(b.get("cro_rec", ""))):
            defects.append("%s: cro_rec %r is not KEEP | PARK | CLOSE | MERGE_INTO:<CODE>" % (code, b.get("cro_rec")))
        for key in ("blockers", "dependencies", "next", "andrew_acts"):
            if key in b and not isinstance(b.get(key), list):
                defects.append("%s: %s must be a list ([] when none)" % (code, key))
        for blk in (b.get("blockers") or []):
            if not isinstance(blk, dict) or not all(k in blk for k in ("what", "owner", "clears_when")):
                defects.append("%s: a blocker lacks what/owner/clears_when" % code)
        if len(b.get("next") or []) > 3:
            defects.append("%s: next has more than 3 items" % code)
        projects.append(b)
    union = pop.get("union")
    if isinstance(union, int) and union != len(projects):
        defects.append("header.population.union=%s but the file holds %d project blocks" % (union, len(projects)))
    return not defects, defects, header, projects


def aggregate(paths):
    rows = []
    for p in paths:
        ok, defects, header, projects = check(p)
        box = (header or {}).get("box", "?")
        for b in projects:
            rows.append((box, b.get("project"), b.get("client_facing"), ",".join(b.get("repos") or []),
                         (b.get("status") or {}).get("fwd_realized"), b.get("cro_rec"), len(b.get("blockers") or []),
                         len(b.get("andrew_acts") or []), "OK" if ok else "DEFECTS:%d" % len(defects)))
    print("%-7s %-22s %-8s %-28s %-8s %-18s %-4s %-4s %s" % ("box", "project", "client", "repos", "fwd", "cro_rec", "blk", "act", "file"))
    for r in sorted(rows):
        print("%-7s %-22s %-8s %-28s %-8s %-18s %-4s %-4s %s" % r)
    recs = {}
    for r in rows:
        recs[r[5]] = recs.get(r[5], 0) + 1
    print("AGGREGATE boxes=%d projects=%d recs=%s" % (len(paths), len(rows), json.dumps(recs, sort_keys=True)))


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--aggregate":
        aggregate(argv[1:])
        return 0
    as_json = "--json" in argv
    path = [a for a in argv if not a.startswith("--")][0]
    ok, defects, header, projects = check(path)
    pop = (header or {}).get("population") or {}
    line = "BOX-STATUS-REPORT %s box=%s author=%s blocks=%d population(register=%s live=%s orders=%s union=%s) %s" % (
        path, (header or {}).get("box"), (header or {}).get("author"), len(projects), pop.get("register_placed"),
        pop.get("live_seat_named"), pop.get("open_order_named"), pop.get("union"), "OK" if ok else "REFUSED")
    if as_json:
        print(json.dumps({"ok": ok, "defects": defects, "header": header, "projects": projects}, indent=1, default=str))
    else:
        for d in defects:
            print("  DEFECT: %s" % d)
        print(line)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
