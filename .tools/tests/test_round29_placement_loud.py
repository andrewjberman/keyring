#!/usr/bin/env python3
"""NFRA_CTLPLN.TO-CT-bc-1 (round-28 ruling 3): .tools/placement-check.py fails loud on an input it cannot reach.

Seven arms. Each builds a synthetic tree in a temporary folder: .tools/placement-check.py and lib/devices.py are copied
in, so the tool's ROOT is the temporary tree; the register, the project rows and the project.json files are written
there. The real register and the real tree are never read or written. No network. ASCII output.

  (a) no org/missions                              -> exit 3, an ERROR: line naming org/missions
  (b) register lists 2 with a tree home, read 1    -> exit 3, the message names 1 and 2 and the code not read
  (c) healthy tree                                 -> exit 0, no ERROR: line, the match=True line
  (d) healthy tree + planted cross-box overlap     -> exit 0 and the OVERLAP line printed (findings never change exit)
  (e) --json with no org/missions                  -> exit 3, one JSON document with an error key
  (f) no org/projects                              -> exit 3, an ERROR: line naming org/projects
  (g) one unreadable project.json (invalid JSON)   -> exit 0, an UNREADABLE finding, no ERROR: line

LAST line: PLACEMENT-LOUD arms=<k>/<n> ok=<True|False>

Standard library only. Run from anywhere: python .tools/tests/test_round29_placement_loud.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
TOOL = os.path.join(ROOT, ".tools", "placement-check.py")
DEVICES_LIB = os.path.join(ROOT, "lib", "devices.py")
DEVICES = {"devices": [{"name": "laptop", "aliases": ["cloud-local"]}, {"name": "sitez", "aliases": ["site-z"]}]}


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def jw(path, obj):
    write(path, json.dumps(obj, indent=1) + "\n")


def make(tmp, *, missions=True, projects=True, reg_rows=(), tree_rows=(), orders=()):
    """reg_rows: (code, status, declared home). tree_rows: (code, status, box, raw text or None).
    orders: (code, task-order text). A tree row with raw text is written verbatim (an unreadable file)."""
    write(os.path.join(tmp, ".tools", "placement-check.py"), open(TOOL, encoding="utf-8").read())
    write(os.path.join(tmp, "lib", "devices.py"), open(DEVICES_LIB, encoding="utf-8").read())
    jw(os.path.join(tmp, "org", "devices", "DEVICES.json"), DEVICES)
    if projects:
        for code, status, home in reg_rows:
            row = {"project_code": code, "status": status}
            if home:
                row["home"] = home
            jw(os.path.join(tmp, "org", "projects", code + ".json"), row)
    if missions:
        for code, status, box, raw in tree_rows:
            path = os.path.join(tmp, "org", "missions", "D0", "X", code, "project.json")
            if raw is not None:
                write(path, raw)
            else:
                jw(path, {"project_code": code, "status": status, "fabric": box})
        for code, text in orders:
            write(os.path.join(tmp, "org", "missions", "D0", "X", code, "task-orders", "TO-1.md"), text)


def run(tmp, args=()):
    env = dict(os.environ)
    env.pop("OPAL_DEVICE_REGISTER", None)
    p = subprocess.run([sys.executable, os.path.join(tmp, ".tools", "placement-check.py")] + list(args), cwd=tmp,
                       env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    return p.returncode, p.stdout or "", p.stderr or ""


def lines_starting(out, prefix):
    return [ln for ln in out.splitlines() if ln.startswith(prefix)]


def arm_a(tmp):
    make(tmp, missions=False, projects=True, reg_rows=[("A", "active", "org/missions/D0/X/A")])
    rc, out, _ = run(tmp)
    errs = lines_starting(out, "ERROR:")
    return rc == 3 and bool(errs) and "org/missions" in errs[0] and "live projects" not in out, "rc=%s errors=%d" % (rc, len(errs))


def arm_b(tmp):
    make(tmp, reg_rows=[("A", "active", "org/missions/D0/X/A"), ("B", "active", "org/missions/D0/X/B")],
         tree_rows=[("A", "active", "laptop", None), ("B", "complete", "sitez", None)])
    rc, out, _ = run(tmp)
    errs = lines_starting(out, "ERROR:")
    ok = (rc == 3 and bool(errs) and "read 1 live project(s)" in errs[0] and "lists 2 with a tree home" in errs[0]
          and "first not read: B" in errs[0])
    return ok, "rc=%s msg=%s" % (rc, errs[0] if errs else "none")


def arm_c(tmp):
    make(tmp, reg_rows=[("A", "active", "org/missions/D0/X/A"), ("B", "active", "org/missions/D0/X/B")],
         tree_rows=[("A", "active", "laptop", None), ("B", "active", "sitez", None)])
    rc, out, _ = run(tmp)
    ok = (rc == 0 and not lines_starting(out, "ERROR:")
          and any("register rows with a tree home: 2 | live projects read: 2 | match=True" in ln for ln in out.splitlines()))
    return ok, "rc=%s" % rc


def arm_d(tmp):
    make(tmp, reg_rows=[("A", "active", "org/missions/D0/X/A"), ("B", "active", "org/missions/D0/X/B")],
         tree_rows=[("A", "active", "laptop", None), ("B", "active", "sitez", None)],
         orders=[("A", "<paths>\nlib/shared.py\n</paths>\n"), ("B", "<paths>\nlib/shared.py\n</paths>\n")])
    rc, out, _ = run(tmp)
    ok = (rc == 0 and not lines_starting(out, "ERROR:") and "  OVERLAP A (laptop) and B (sitez):" in out
          and "FINDINGS: 0 unplaced/unreadable, 1 cross-box write overlap(s)" in out)
    return ok, "rc=%s overlaps_line=%s" % (rc, bool(lines_starting(out, "  OVERLAP A (laptop)")))


def arm_e(tmp):
    make(tmp, missions=False, projects=True, reg_rows=[("A", "active", "org/missions/D0/X/A")])
    rc, out, _ = run(tmp, ["--json"])
    try:
        doc = json.loads(out)
    except ValueError:
        return False, "rc=%s stdout is not one JSON document" % rc
    ok = (rc == 3 and isinstance(doc, dict) and "error" in doc and "cannot read org/missions" in doc["error"]
          and doc.get("live_projects") is None)
    return ok, "rc=%s keys=%s" % (rc, sorted(doc.keys()) if isinstance(doc, dict) else doc)


def arm_f(tmp):
    make(tmp, missions=True, projects=False, tree_rows=[("A", "active", "laptop", None)])
    rc, out, _ = run(tmp)
    errs = lines_starting(out, "ERROR:")
    ok = rc == 3 and bool(errs) and "org/projects" in errs[0]
    return ok, "rc=%s msg=%s" % (rc, errs[0] if errs else "none")


def arm_g(tmp):
    make(tmp, reg_rows=[("A", "active", "org/missions/D0/X/A"), ("B", "active", "org/missions/D0/X/B")],
         tree_rows=[("A", "active", "laptop", None), ("B", "active", "sitez", "{not json")])
    rc, out, _ = run(tmp)
    ok = (rc == 0 and not lines_starting(out, "ERROR:") and bool(lines_starting(out, "  UNREADABLE"))
          and "live projects read: 2" in out)
    return ok, "rc=%s unreadable_line=%s" % (rc, bool(lines_starting(out, "  UNREADABLE")))


ARMS = [("a", "no org/missions -> ERROR, exit 3", arm_a),
        ("b", "register lists 2 with a tree home, read 1 -> ERROR names 1 and 2, exit 3", arm_b),
        ("c", "healthy tree -> exit 0, match=True line, no ERROR", arm_c),
        ("d", "healthy tree + cross-box overlap -> exit 0, OVERLAP printed", arm_d),
        ("e", "--json with no org/missions -> exit 3, JSON error key", arm_e),
        ("f", "no org/projects -> ERROR, exit 3", arm_f),
        ("g", "unreadable project.json -> exit 0, UNREADABLE finding, not ERROR", arm_g)]


def main():
    base = tempfile.mkdtemp(prefix="plc141_")
    passed = 0
    try:
        for key, label, fn in ARMS:
            tmp = os.path.join(base, key)
            os.makedirs(tmp)
            try:
                ok, detail = fn(tmp)
            except Exception as exc:  # an arm that cannot run is a failed arm, named
                ok, detail = False, "exception %s" % exc
            passed += 1 if ok else 0
            print("  %s  (%s) %s  [%s]" % ("PASS" if ok else "FAIL", key, label, detail))
    finally:
        shutil.rmtree(base, ignore_errors=True)
    n = len(ARMS)
    print("PLACEMENT-LOUD arms=%d/%d ok=%s" % (passed, n, passed == n))
    return 0 if passed == n else 1


if __name__ == "__main__":
    sys.exit(main())
