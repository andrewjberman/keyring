"""placement-check.py -- the placement READ (NFRA_CTLPLN FWD-7, contract C-PLACEMENT): which box runs each live project and
workstream, whether two projects on different boxes would change the same files, and which box has room with nothing placed.

    python .tools/placement-check.py              # the read over every live project (status not complete/closed)
    python .tools/placement-check.py --json       # the same, as one JSON document
    python .tools/placement-check.py --self-test  # planted cases for the overlap and resolution rules

A VIEWER, NOT A CHECKER: findings never change the exit code (the monitor moratorium), as .tools/sequence-check.py.
EXCEPT an INPUT the read cannot reach (NFRA_CTLPLN round-28 ruling 3): exit 3 and an `ERROR:` line when org/missions or
org/projects is absent, or when a non-terminal register row (org/projects/*.json) that carries a tree home is not read
as a live project. The expected set is the register's own `home` field (org/missions/...) united with any tree home
found under ROOT, so a sparse checkout cannot shrink the expectation. An UNREADABLE project.json is a finding, not an error.

Sources, each named in the output:
  box         project.json `fabric`, resolved through the device register org/devices/DEVICES.json (lib/devices.py);
              an unresolved value is a finding, never a guess.
  workstream  a FAST lease keyed `<CODE>~<lane>` (org/mcp/drive_mode/); it runs on its project's box (no per-workstream
              field exists yet, so a workstream cannot be split from its project by construction).
  write set   the project's own tree, the `<paths>` of its non-terminal task orders, and its FAST lease surfaces.
OVERLAP: two live projects placed on DIFFERENT boxes whose write sets share a path (equal, or one a directory prefix of
the other) -- the C-PLACEMENT rule "two on different boxes change different files", checked one level up from
.tools/owned-paths-validate.py's per-worker check.
"""
from __future__ import annotations

import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TERMINAL_PROJECT = {"complete", "closed", "cancelled", "superseded", "retired"}
TERMINAL_TO = {"complete", "superseded", "cancelled"}
PATHS_RE = re.compile(r"^<paths>[ \t]*$(.*?)^</paths>[ \t]*$", re.S | re.M)   # tags on their own lines only
STATUS_RE = re.compile(r"<status>\s*([^<\s]+)\s*</status>")


def devices_module():
    spec = importlib.util.spec_from_file_location("opal_devices", os.path.join(ROOT, "lib", "devices.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def norm(p: str) -> str:
    return p.strip().replace("\\", "/").rstrip("/")


def overlaps(a: str, b: str) -> bool:
    """Equal, or one is a directory prefix of the other. A glob tail is read as its directory."""
    a, b = norm(a.split("*")[0]), norm(b.split("*")[0])
    if not a or not b:
        return False
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


def cross_box_overlaps(projects: list) -> list:
    """PURE. [(code_a, box_a, code_b, box_b, path_a, path_b)] for live projects on different boxes sharing a path."""
    out = []
    for i, p in enumerate(projects):
        for q in projects[i + 1:]:
            if not p["box"] or not q["box"] or p["box"] == q["box"]:
                continue
            for a in p["writes"]:
                hit = next((b for b in q["writes"] if overlaps(a, b)), None)
                if hit:
                    out.append((p["code"], p["box"], q["code"], q["box"], a, hit))
                    break
    return out


def read_projects(dev, reg) -> tuple:
    projects, findings = [], []
    leases = {}
    for f in glob.glob(os.path.join(ROOT, "org", "mcp", "drive_mode", "*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        key = os.path.basename(f)[:-5]
        leases.setdefault(key.split("~")[0], []).append((key, d.get("surface") or []))
    for f in sorted(glob.glob(os.path.join(ROOT, "org", "missions", "D*", "*", "*", "project.json"))):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except (OSError, ValueError) as exc:
            findings.append("UNREADABLE %s (%s)" % (os.path.relpath(f, ROOT), exc))
            continue
        if str(d.get("status", "")).lower() in TERMINAL_PROJECT:
            continue
        code = d.get("project_code") or os.path.basename(os.path.dirname(f))
        home = norm(os.path.relpath(os.path.dirname(f), ROOT))
        # placement names the box that runs the project; fabric is the older field (row NFRA_CTLPLN-S32)
        where = d.get("placement") or d.get("fabric") or ""
        box = dev.resolve(str(where), reg)
        if not box:
            findings.append("UNPLACED %s: placement/fabric %r is not a box in the device register" % (code, where))
        writes = {home}
        for to in glob.glob(os.path.join(ROOT, home, "task-orders", "*.md")):
            text = open(to, encoding="utf-8", errors="replace").read()
            # an order's status is its LAST status tag (1.0.0_SA_CTO ruling 107528)
            sts = STATUS_RE.findall(text)
            if sts and sts[-1].lower() in TERMINAL_TO:
                continue
            for m in PATHS_RE.finditer(text):
                writes.update(norm(x) for x in m.group(1).splitlines()
                              if x.strip() and not re.search(r"\s|^[<#`-]", x.strip()))
        ws = []
        for key, surface in leases.get(code, []):
            writes.update(norm(s) for s in surface if s)
            if "~" in key:
                ws.append(key)
        projects.append({"code": code, "box": box, "fabric": d.get("fabric"), "home": home,
                         "workstreams": sorted(ws), "writes": sorted(writes)})
    return projects, findings


UNREADABLE_RE = re.compile(r"^UNREADABLE (.+?) \(")


def register_homes() -> tuple:
    """(codes, error). The codes of the NON-TERMINAL register rows (org/projects/*.json) that carry a tree home: the
    register's own `home` under org/missions/, united with a tree home found under ROOT. error is an ERROR line when
    the register cannot be read row by row (or is absent) -- the read then cannot prove it reached every project."""
    if not os.path.isdir(os.path.join(ROOT, "org", "projects")):
        return [], "ERROR: placement-check cannot read org/projects (not found under %s); the read cannot prove it reached every project" % ROOT
    codes = {os.path.basename(os.path.dirname(f)) for f in glob.glob(os.path.join(ROOT, "org", "missions", "D*", "*", "*", "project.json"))}
    out = set()
    for f in sorted(glob.glob(os.path.join(ROOT, "org", "projects", "*.json"))):
        try:
            d = json.load(open(f, encoding="utf-8"))
            if not isinstance(d, dict):
                raise ValueError("not a JSON object")
        except (OSError, ValueError) as exc:
            return [], "ERROR: placement-check cannot read register row %s (%s); the read cannot prove it reached every project" % (os.path.relpath(f, ROOT), exc)
        if str(d.get("status", "")).lower() in TERMINAL_PROJECT:
            continue
        code = str(d.get("project_code") or os.path.basename(f)[:-5])
        if str(d.get("home") or "").replace("\\", "/").startswith("org/missions/") or code in codes:
            out.add(code)
    return sorted(out), None


def report(projects, findings, reg) -> dict:
    boxes = {d["name"]: [] for d in reg["devices"]}
    for p in projects:
        if p["box"]:
            boxes.setdefault(p["box"], []).append(p["code"])
    return {"projects": projects, "findings": findings, "overlaps": cross_box_overlaps(projects),
            "boxes": {b: {"placed": sorted(c), "seat_limit": next((d.get("seat_limit") for d in reg["devices"]
                                                                   if d["name"] == b), None)} for b, c in boxes.items()}}


def fail(msg, as_json, live=None) -> int:
    """An input the read cannot reach: exit 3. --json names it in one document; the text form prints the ERROR line."""
    print(json.dumps({"error": msg, "live_projects": live}, indent=1) if as_json else msg)
    print(msg, file=sys.stderr)
    return 3


def main(argv) -> int:
    if argv == ["--self-test"]:
        return self_test()
    as_json = argv == ["--json"]
    if not os.path.isdir(os.path.join(ROOT, "org", "missions")):
        return fail("ERROR: placement-check cannot read org/missions (not found under %s); the read has no projects to place"
                    % ROOT, as_json)
    need, err = register_homes()
    if err:
        return fail(err, as_json)
    dev = devices_module()
    reg = dev.load()
    projects, findings = read_projects(dev, reg)
    # an UNREADABLE project.json is reached (it is named as a finding), so it counts as read
    unreadable = [re.split(r"[\\/]", m.group(1))[-2] for m in map(UNREADABLE_RE.match, findings) if m]
    reached = {p["code"] for p in projects} | set(unreadable)
    n_read = len(projects) + len(unreadable)
    missing = [c for c in need if c not in reached]
    if missing:
        return fail("ERROR: placement-check read %d live project(s) but the register lists %d with a tree home; first not read: %s"
                    % (n_read, len(need), ", ".join(missing[:3])), as_json, live=n_read)
    r = report(projects, findings, reg)
    if as_json:
        r.update({"register_with_tree_home": len(need), "live_projects_read": n_read, "match": True})
        print(json.dumps(r, indent=1))
        return 0
    print("placement-check | live projects: %d | register: %s | boxes: %d" % (len(projects), dev.register_path(),
                                                                          len(r["boxes"])))
    print("placement-check | register rows with a tree home: %d | live projects read: %d | match=True"
          % (len(need), n_read))
    for b, v in r["boxes"].items():
        print("BOX %-7s placed %2d%s  %s" % (b, len(v["placed"]), "  (ROOM: nothing placed)" if not v["placed"] else "",
                                             ", ".join(v["placed"])))
    for p in projects:
        if p["workstreams"]:
            print("  WORKSTREAMS %s on %s: %s" % (p["code"], p["box"], ", ".join(p["workstreams"])))
    print("FINDINGS: %d unplaced/unreadable, %d cross-box write overlap(s)" % (len(findings), len(r["overlaps"])))
    for f in findings:
        print("  " + f)
    for a, ba, b, bb, pa, pb in r["overlaps"]:
        print("  OVERLAP %s (%s) and %s (%s): %s ~ %s" % (a, ba, b, bb, pa, pb))
    return 0


def self_test() -> int:
    P = [{"code": "A", "box": "laptop", "writes": ["org/missions/D0/X/A", "lib/devices.py"]},
         {"code": "B", "box": "sitez", "writes": ["org/missions/D4/Y/B", "lib/"]},
         {"code": "C", "box": "sitez", "writes": ["org/missions/D4/Y/C", "lib/devices.py"]},
         {"code": "D", "box": "laptop", "writes": ["lib/devices.py"]},
         {"code": "E", "box": None, "writes": ["lib/devices.py"]},
         {"code": "F", "box": "sitez", "writes": ["data/assets/scripts/gold/x_*.py"]},
         {"code": "G", "box": "laptop", "writes": ["data/assets/scripts/gold/"]}]
    got = {(a, b) for a, _, b, _, _, _ in cross_box_overlaps(P)}
    cases = [
        ("a file under another box's directory overlaps", ("A", "B") in got),
        ("the same file on two boxes overlaps", ("A", "C") in got),
        ("two projects on ONE box never overlap", ("A", "D") not in got and ("B", "C") not in got),
        ("an unplaced project is a finding, not an overlap", not any("E" in k for k in got)),
        ("a glob tail reads as its directory", ("F", "G") in got),
        ("a sibling path is not an overlap", not overlaps("lib/devices.py", "lib/devices_x.py")),
        ("prefix match is directory-aware", not overlaps("org/missions/D4", "org/missions/D40")),
    ]
    fails = sum(1 for _, ok in cases if not ok)
    for label, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", label))
    print("placement-check --self-test: %d/%d PASS" % (len(cases) - fails, len(cases)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
