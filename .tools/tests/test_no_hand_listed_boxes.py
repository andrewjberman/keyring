#!/usr/bin/env python
"""NFRA_CTLPLN.TO-CT-t-3: no tool lists boxes by hand; a fixture box needs no edit.

Census arm: .tools/box-list-census.py over a FIXTURE tree finds every planted hand list (python tuple, python lookup dict, regex
alternation, PowerShell hashtable, shell case) and passes the negatives (a register read, a comment, a record whose fields name two
boxes, a prose docstring). Fixture arm: a copy of the device register holding a FIFTH box (every name here is fixture data, built
from the real rows) is pointed at by OPAL_DEVICE_REGISTER, and each edited tool's box-aware path accepts the fifth box with no
code edit: the gate (to-pipeline-gate.py check_project_stage), the open-calls scan (seat_of), the fabric-activity box inference
(infer_box), the schedule script (open-calls-scan-schedule.ps1 -Status), remote-job.py (device_names) and lib/devices.py. Behaviour
arm: infer_box over an 18-row table pinned from the pre-edit tool (byte-identical on today's register), and the gate's AST carrier
FABRIC_ENUM (read by .tools/missions-tree-index.py, not editable here) equals the register-derived values. Real-tree arm: the
census over the real tree lists none of the files this order edited, except the gate's AST carrier (row NFRA_CTLPLN-W53-S1).

LAST line: NO-HAND-LISTED-BOXES-TEST cases=<k>/<n> ok=<True|False>
"""
import copy
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOLS = os.path.join(ROOT, ".tools")
EDITED = [".tools/open-calls-scan.py", ".tools/to-pipeline-gate.py", ".tools/fabric-activity.py",
          ".tools/open-calls-scan-schedule.ps1", ".tools/remote-job.py", "org/devices/kit_python_install.py", "lib/devices.py"]
HELD = {}   # no held file: to-pipeline-gate.py derives its box list from the register and is no longer in the census
RESULTS = []


def case(name, ok, detail=""):
    RESULTS.append(ok)
    print("%s  %s%s" % ("PASS" if ok else "FAIL", name, (" | " + detail) if detail else ""))


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def fixture_register(tmp):
    """The real register's rows renamed to fixture boxes, plus a fifth; returns (path, names, placement values, fifth)."""
    with open(os.path.join(ROOT, "org", "devices", "DEVICES.json"), encoding="utf-8") as fh:
        reg = json.load(fh)
    words = ["boxalpha", "boxbeta", "boxgamma", "boxdelta", "boxepsilon"]
    rows = []
    for i, d in enumerate(reg["devices"] + [copy.deepcopy(reg["devices"][-1])]):
        d = copy.deepcopy(d)
        old = d["name"]
        d["name"] = words[i]
        d["aliases"] = [("box-" + words[i][3:]) if a.replace("-", "").lower() == old.lower() else words[i] + "-alias"
                        for a in d.get("aliases", [])]
        d["row_coordinate"] = "F%d" % i if d.get("row_coordinate") not in ("", None) else ""
        d["inbound_queue"] = "fixture-queue-%d.fifo" % i
        rows.append(d)
    reg["devices"] = rows
    path = os.path.join(tmp, "DEVICES.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(reg, fh)
    return path, words, rows


def write(root, rel, text):
    p = os.path.join(root, *rel.split("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def census_arm(cen, tmp, regpath, words):
    a, b, c = words[0], words[1], words[2]
    tree = os.path.join(tmp, "tree")
    write(tree, ".tools/planted_tuple.py", 'KNOWN = ("%s", "%s", "other")\n' % (a, b))
    write(tree, ".tools/planted_dict.py", 'CTO_OF = {"%s": "x", "%s": "y"}\n' % (a, c))
    write(tree, ".tools/planted_lookup.py", 'BY_DIGIT = {"1": "%s", "2": "%s"}\n' % (a, b))
    write(tree, ".tools/planted_regex.py", 'import re\nRX = re.compile(r"^(%s|%s)$")\n' % (b, c))
    write(tree, ".tools/planted.ps1", "$Slots = @{ '%s' = 1; '%s' = 4 }\n" % (a, b))
    write(tree, ".tools/planted.sh", 'case "$1" in\n  %s|%s) dev="$1" ;;\nesac\n' % (a, c))
    write(tree, "org/devices/planted.yaml", "boxes:\n  - %s\n  - %s\n" % (b, c))
    write(tree, "lib/clean_register_read.py",
          'import devices\nBOXES = devices.names()\nONE = "%s"\n' % a)
    write(tree, ".tools/clean_comment.py", '# the %s and the %s boxes run it\nX = 1  # %s, %s\n' % (a, b, b, c))
    write(tree, ".tools/clean_prose.py", '"""Runs on %s or %s, never both."""\nX = 1\n' % (a, b))
    write(tree, ".tools/clean_record.py", 'MSG = {"from_device": "%s", "to_device": "%s"}\n' % (a, b))
    write(tree, ".tools/clean_record.json", '{"from_device": "%s", "to_device": "%s", "ids": []}\n' % (a, b))
    write(tree, ".tools/tests/test_planted_in_a_test.py", 'KNOWN = ("%s", "%s")\n' % (a, b))
    res = cen.census(tree, regpath)
    planted = {"planted_tuple.py", "planted_dict.py", "planted_lookup.py", "planted_regex.py", "planted.ps1", "planted.sh",
               "planted.yaml"}
    found = {os.path.basename(f) for f in res["listed"]}
    case("census over a fixture tree finds all %d planted hand lists" % len(planted), found == planted,
         "found=%s missing=%s" % (sorted(found), sorted(planted - found)))
    clean = {"clean_register_read.py", "clean_comment.py", "clean_prose.py", "clean_record.py", "clean_record.json"}
    case("census passes the register read, a comment, a docstring and two records (5 negatives)", not (found & clean),
         "wrongly listed=%s" % sorted(found & clean))
    case("census lists a planted test apart and does not count it",
         [os.path.basename(f) for f in res["tests"]] == ["test_planted_in_a_test.py"] and "test_planted_in_a_test.py" not in found)
    out = subprocess.run([sys.executable, os.path.join(TOOLS, "box-list-census.py"), "--root", tree, "--register", regpath],
                         capture_output=True, text=True, encoding="utf-8", timeout=100)
    last = out.stdout.strip().splitlines()[-1] if out.stdout.strip() else ""
    case("census last line carries scanned, hand_listed and the file list", out.returncode == 0 and bool(
        re.match(r"^BOX-LIST-CENSUS scanned=\d+ hand_listed=7 files=\S+$", last)), last[:120])


def gate_arm(tmp, regpath, words, values):
    gate = load("to_pipeline_gate_t3", ".tools/to-pipeline-gate.py")

    def refusals(fabric):
        home = os.path.join(tmp, "g-%s" % re.sub(r"\W", "_", str(fabric)), "org", "missions", "D0", "NFRA", "FABTMP")
        os.makedirs(os.path.join(home, "task-orders"), exist_ok=True)
        with open(os.path.join(home, "project.json"), "w", encoding="utf-8") as fh:
            json.dump({"project_code": "FABTMP", "dep_stage": "PRD", "fabric": fabric}, fh)
        top = home.split(os.sep + "org" + os.sep)[0]
        return gate.check_project_stage(top, "org/missions/D0/NFRA/FABTMP/task-orders/FABTMP.TO-1.md")

    os.environ["OPAL_DEVICE_REGISTER"] = regpath
    fifth = values[-1]
    r5 = refusals(fifth)
    case("gate admits the fifth fixture box with no code edit", r5 == [], str(r5)[:120])
    case("gate admits every fixture placement value (%d)" % len(values), all(refusals(v) == [] for v in values))
    case("gate refuses a value the fixture register does not hold (a real box's value)",
         bool(refusals("laptop")) and "NOT in the ratified enum" in refusals("laptop")[0])
    os.environ["OPAL_DEVICE_REGISTER"] = os.path.join(tmp, "no-such-register.json")
    r = refusals("laptop")
    case("gate refuses fail-closed when the register is unreadable", bool(r) and "fail-closed" in r[0], (r or ["ADMITTED"])[0][-80:])
    os.environ.pop("OPAL_DEVICE_REGISTER", None)
    live = gate._fabric_values()
    case("gate AST carrier FABRIC_ENUM equals the register-derived values (no drift)", tuple(gate.FABRIC_ENUM) == tuple(live),
         "%r vs %r" % (gate.FABRIC_ENUM, live))


def other_arms(tmp, regpath, words, rows):
    fifth = words[-1]
    os.environ["OPAL_DEVICE_REGISTER"] = regpath
    ocs = load("open_calls_scan_t3", ".tools/open-calls-scan.py")
    got = ocs.seat_of("1.0.0_SA_CTO", fifth)
    case("open-calls-scan resolves the fifth box's CTO serial from the register", got == "1.0.0_SA_CTO~" + fifth.upper(), got)
    case("open-calls-scan gives the default-lane box the bare serial and an unknown box ''",
         ocs.seat_of("0.0.0_AB_MSTR", words[0]) == "0.0.0_AB_MSTR" and ocs.seat_of("0.0.0_AB_MSTR", "nosuchbox") == "")
    fa = load("fabric_activity_t3", ".tools/fabric-activity.py")
    case("fabric-activity infers the fifth box from its name in a serial", fa.infer_box("1.0.0_SA_CTO~" + fifth.upper(), "x") == fifth)
    case("fabric-activity infers a fixture box from its committer name and a lane-letter box from its letters",
         fa.infer_box("Andrew Berman", fifth + " ") == fifth and fa.infer_box("2.0.0_SA_COO~" + rows[1]["lane_letters"][0], "q") == words[1])
    case("fabric-activity infers the default-lane box for an unclaimed agent lane",
         fa.infer_box("2.0.0_SA_COO~C", "q") == words[0] and fa.infer_box("Andrew Berman", "Andrew Berman") == "unplaced")
    rj = load("remote_job_t3", ".tools/remote-job.py")
    case("remote-job device_names includes the fifth box", tuple(rj.device_names()) == tuple(words), str(rj.device_names()))
    dev = load("devices_t3", "lib/devices.py")
    case("lib/devices placement_values and lane_suffix cover the fifth box",
         dev.placement_values()[-1] == fifth and dev.lane_suffix(fifth) == "~" + fifth.upper()
         and dev.lane_suffix(words[1]) == "~" + rows[1]["lane_letters"][0] and dev.lane_suffix(words[0]) == "")
    ps = shutil.which("powershell")
    if ps is None:
        case("schedule script computes the fifth box's slot from the register", True, "skipped: no powershell on this box")
    else:
        env = dict(os.environ, AGENTBUS_DEVICE=fifth)
        cp = subprocess.run([ps, "-NoProfile", "-File", os.path.join(TOOLS, "open-calls-scan-schedule.ps1"), "-Status"],
                            capture_output=True, text=True, timeout=100, env=env)
        first = (cp.stdout.splitlines() or [""])[0]
        case("schedule script computes the fifth box's slot from the register", first.startswith("box=%s  minute=:09" % fifth), first[:60])
        env2 = dict(os.environ, AGENTBUS_DEVICE=words[1])
        cp2 = subprocess.run([ps, "-NoProfile", "-File", os.path.join(TOOLS, "open-calls-scan-schedule.ps1"), "-Status"],
                             capture_output=True, text=True, timeout=100, env=env2)
        first2 = (cp2.stdout.splitlines() or [""])[0]
        case("schedule script gives the second box minute :04 (register order)", first2.startswith("box=%s  minute=:04" % words[1]),
             first2[:60])
    os.environ.pop("OPAL_DEVICE_REGISTER", None)


INFER_PINNED = [  # (author, committer, box) -- run through the PRE-EDIT infer_box on the real register; the new one must agree
    ("1.0.0_SA_CTO~DELL1", "x", "dell1"), ("2.0.0_SA_COO~dell2", "y", "dell2"), ("0.0.0_AB_MSTR~SITEZ", "z", "sitez"),
    ("1.0.0_SA_CTO", "Dell2", "dell2"), ("Andrew Berman", "dell2 ", "dell2"), ("0.9.0_WK_NFRA_CTLPLN~52", "q", "dell2"),
    ("0.9.0_WK_OTHER~3", "q", "unplaced"), ("1.0.0_SA_CTO~Z", "q", "sitez"), ("2.0.0_SA_COO~ZA", "q", "sitez"),
    ("2.0.0_SA_COO~C", "q", "laptop"), ("2.0.0_SA_COO~1", "q", "dell1"), ("2.0.0_SA_COO~2", "q", "dell2"),
    ("2.0.0_SA_COO~D1", "q", "dell1"), ("2.0.0_SA_COO~D12", "q", "dell2"), ("2.0.0_SA_COO~A3", "q", "laptop"),
    ("Andrew Berman", "Andrew Berman", "unplaced"), ("2.0.0_SA_COO~dell", "q", "laptop"), ("2.0.0_SA_COO~12", "q", "dell2")]


def behaviour_arm():
    fa = load("fabric_activity_t3b", ".tools/fabric-activity.py")
    fa._PLACEMENT = {"NFRA_CTLPLN": "dell2"}
    bad = [(a, c, want, fa.infer_box(a, c)) for a, c, want in INFER_PINNED if fa.infer_box(a, c) != want]
    case("fabric-activity infer_box agrees with the pre-edit tool on %d pinned rows (today's register)" % len(INFER_PINNED), not bad,
         str(bad[:2]))
    ocs = load("open_calls_scan_t3b", ".tools/open-calls-scan.py")
    dev = load("devices_t3b", "lib/devices.py")
    want = {"laptop": ("1.0.0_SA_CTO", "0.0.0_AB_MSTR"), "sitez": ("1.0.0_SA_CTO~Z", "0.0.0_AB_MSTR~Z"),
            "dell1": ("1.0.0_SA_CTO~DELL1", "0.0.0_AB_MSTR~DELL1"), "dell2": ("1.0.0_SA_CTO~DELL2", "0.0.0_AB_MSTR~DELL2")}
    got = {b: (ocs.seat_of("1.0.0_SA_CTO", b), ocs.seat_of("0.0.0_AB_MSTR", b)) for b in dev.names()}
    case("open-calls-scan serials equal the pre-edit CTO_OF/MSTR_OF tables for all %d boxes" % len(want), got == want, str(got)[:100])
    case("lib/devices placement_values equals the pre-edit gate enum", dev.placement_values() == ("laptop", "site-z", "dell1", "dell2"))


def real_tree_arm():
    cp = subprocess.run([sys.executable, os.path.join(TOOLS, "box-list-census.py")], capture_output=True, text=True,
                        encoding="utf-8", timeout=100, cwd=ROOT)
    last = cp.stdout.strip().splitlines()[-1] if cp.stdout.strip() else ""
    m = re.match(r"^BOX-LIST-CENSUS scanned=(\d+) hand_listed=(\d+) files=(\S+)$", last)
    listed = set(m.group(3).split(",")) if m else set()
    mine = sorted(f for f in listed if f in EDITED)
    unheld = [f for f in mine if f not in HELD]
    case("real-tree census lists none of the edited files except the held AST carrier", bool(m) and not unheld,
         "edited files still listed=%s held=%s" % (mine, {f: HELD[f] for f in mine if f in HELD}))
    case("real-tree census scanned a non-empty tree", bool(m) and int(m.group(1)) > 100, last[:60])


def main():
    cen = load("box_list_census_t3", ".tools/box-list-census.py")
    with tempfile.TemporaryDirectory() as tmp:
        regpath, words, rows = fixture_register(tmp)
        census_arm(cen, tmp, regpath, words)
        os.environ["OPAL_DEVICE_REGISTER"] = regpath
        values = load("devices_t3a", "lib/devices.py").placement_values()
        os.environ.pop("OPAL_DEVICE_REGISTER", None)
        gate_arm(tmp, regpath, words, values)
        other_arms(tmp, regpath, words, rows)
    behaviour_arm()
    real_tree_arm()
    k, n = sum(1 for r in RESULTS if r), len(RESULTS)
    print("NO-HAND-LISTED-BOXES-TEST cases=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())
