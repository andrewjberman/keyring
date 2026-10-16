#!/usr/bin/env python3
"""NFRA_CTLPLN.TO-CT-ai-1 (FWD-2, FWD-7): read-backs of the device register org/devices/DEVICES.json.

--fwd2  A box added ONCE, in the register, is named by every box-listing tool. The register is copied to a temporary
        folder with ONE fixture box (`fixbox`, the shape of a Dell row); each tool is run at its own path with
        OPAL_DEVICE_REGISTER pointing at the copy. A tool is REACHED when its output or its value names fixbox. A tool
        that cannot be pointed at a register copy is LISTED with its reason and counted NOT REACHED, never failed.
        The real register is never written (its sha1 is printed before and after).
        The two box-list tools that read no register by default (test_box_lists_from_register.py and
        fabric_value_census.py) are run with --register <the copy>; each is REACHED when its BOXES-READ line names fixbox.
        LAST line: FWD2-BOX-ADDED tools=<reached>/<listed> not_reached=<n> named=<k> ok=<True|False>

--fwd7  Every OVERLAP line of .tools/placement-check.py (run unchanged) is classed:
          SHARED        the overlapping (more specific) path is covered by a rule file this test READS and checks
                        for the cited phrase: R1 org/critical_paths/.open_deploys (CLAUDE.md NEVER-2), R2
                        infra/aws/lambda/ci/ (the Lambda function map _description and _note), R3 a layer build_output
                        row of infra/aws/lambda/ci/lambda-layer-map.json.
          SPLIT         both projects name the SAME file (equal paths), no rule covers it: two projects on different
                        boxes would change one file (C-PLACEMENT).
          NOT-SAME-FILE R5: one path is a strict directory-prefix parent of the other and they are different files
                        (decided mechanically by the path-prefix relation; the longer path must be a strict child).
          UNCLASSIFIED  anything else (no rule applies).
        Writes the table to the CT-ai-1 deliverables folder.
        LAST line: FWD7-OVERLAPS total=<n> shared=<a> split=<b> not_same_file=<c> unclassified=<u> ok=<True|False>

Standard library only. No AWS, no network. Run from anywhere: python .tools/tests/test_round19_register.py --fwd2
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTER = os.path.join(ROOT, "org", "devices", "DEVICES.json")
FIXTURE_NAME = "fixbox"
DELIV = os.path.join(ROOT, "org", "missions", "D0", "NFRA", "NFRA_CTLPLN", "deliverables", "0.9.0_WK_NFRA_CTLPLN~106")
TABLE = os.path.join(DELIV, "FWD7_OVERLAP_CLASSES.md")
OVERLAP_RE = re.compile(r"^  OVERLAP (\S+) \((\S+)\) and (\S+) \((\S+)\): (\S+) ~ (\S+)$")
FINDINGS_RE = re.compile(r"FINDINGS: \d+ unplaced/unreadable, (\d+) cross-box write overlap")


def sha1(path):
    with open(path, "rb") as fh:
        return hashlib.sha1(fh.read()).hexdigest()


def run(args, env_extra=None, timeout=240):
    env = dict(os.environ)
    env.update(env_extra or {})
    p = subprocess.run(args, cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=timeout)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


# ---------------------------------------------------------------------------------------------- FWD-2
def fixture_register(tmp):
    with open(REGISTER, encoding="utf-8") as fh:
        reg = json.load(fh)
    src = next(d for d in reg["devices"] if d["name"] == "dell1")      # the Dell shape: role, lane cap, tailnet fields
    box = json.loads(json.dumps(src))
    box.update({
        "name": FIXTURE_NAME, "aliases": [], "row_coordinate": "FX",
        "role": "execution", "role_text": "FIXTURE box for the round-19 FWD-2 read-back. Not a real box.",
        "seat_limit": {"execution_lanes": None}, "lane_letters": [], "lane_letters_default": False,
        "tailnet_name": FIXTURE_NAME, "tailnet_address": "100.64.0.99",
        "inbound_queue": "agentbus-global-fixbox-queue.fifo",
    })
    for k in list(box):
        if k.endswith("_source") or k.endswith("_claim"):
            box[k] = "fixture: NFRA_CTLPLN CT-ai-1 FWD-2 read-back (not a box)" if k.endswith("_source") else "held"
    box.pop("aliases_source", None)
    reg["devices"].append(box)
    path = os.path.join(tmp, "DEVICES.json")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(reg, fh, indent=2)
        fh.write("\n")
    return path


def fwd2():
    py = sys.executable
    before = sha1(REGISTER)
    tmp = tempfile.mkdtemp(prefix="fwd2-register-")
    reg_copy = fixture_register(tmp)
    env = {"OPAL_DEVICE_REGISTER": reg_copy}
    gate = os.path.join(ROOT, ".tools", "to-pipeline-gate.py")
    boxstat = os.path.join(ROOT, ".tools", "box-status-report-check.py")
    value_snip = ("import importlib.util as u,sys;s=u.spec_from_file_location('m',sys.argv[1]);m=u.module_from_spec(s);"
                  "s.loader.exec_module(m);print(%s)")
    # (label, argv, how the output is read, not-reached reason or None)
    tools = [
        ("lib/devices.py names", [py, os.path.join(ROOT, "lib", "devices.py"), "names"], "line"),
        ("to-pipeline-gate.py FABRIC_ENUM", [py, "-c", value_snip % "' '.join(m.FABRIC_ENUM)", gate], "token"),
        ("placement-check.py box rows", [py, os.path.join(ROOT, ".tools", "placement-check.py")], "boxrow"),
        ("crossbox-matrix.py", [py, os.path.join(ROOT, ".tools", "crossbox-matrix.py")], "token"),
        ("seat-list.py show --all", [py, os.path.join(ROOT, ".tools", "seat-list.py"), "show", "--all"], "absent"),
        ("box-status-report-check.py BOXES", [py, "-c", value_snip % "' '.join(sorted(m.BOXES))", boxstat], "token"),
        ("tests/test_box_lists_from_register.py --register",
         [py, os.path.join(ROOT, ".tools", "tests", "test_box_lists_from_register.py"), "--register", reg_copy], "boxes-read"),
        ("tests/fabric_value_census.py --register",
         [py, os.path.join(ROOT, ".tools", "tests", "fabric_value_census.py"), "--register", reg_copy], "boxes-read"),
    ]
    not_reached = []
    rows, named = [], 0
    for label, argv, mode in tools:
        rc, out = run(argv, env)
        if mode == "line":
            hit = FIXTURE_NAME in [x.strip() for x in out.splitlines()]
        elif mode == "token":
            hit = any(re.search(r"(?<![\w-])%s(?![\w-])" % FIXTURE_NAME, x) for x in out.splitlines())
        elif mode == "boxrow":
            hit = any(x.startswith("BOX %s " % FIXTURE_NAME) for x in out.splitlines())
        elif mode == "boxes-read":
            hit = any(x.startswith("BOXES-READ ") and FIXTURE_NAME in x.split() for x in out.splitlines())
        else:
            hit = ("ABSENT %s:" % FIXTURE_NAME) in out
        # boxes-read is reached on the BOXES-READ line alone: the census's exit code is its own token verdict (rc printed)
        hit = bool(hit and (rc == 0 or mode == "boxes-read"))
        named += int(hit)
        rows.append((label, rc, hit))
        shown = [x for x in out.splitlines() if FIXTURE_NAME in x][:2] or ["(no line names %s)" % FIXTURE_NAME]
        print("%s  %-36s rc=%s  %s" % ("NAMED " if hit else "MISS  ", label, rc, " | ".join(s.strip() for s in shown)))
    for label, reason in not_reached:
        print("NOT-REACHED  %-36s %s" % (label, reason))
    listed = len(tools) + len(not_reached)
    reached = len(tools)
    after = sha1(REGISTER)
    print("real register unchanged: %s (sha1 %s)" % (before == after, after[:12]))
    ok = reached > 0 and named == reached and before == after
    print("FWD2-BOX-ADDED tools=%d/%d not_reached=%d named=%d ok=%s" % (reached, listed, len(not_reached), named, ok))
    shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


# ---------------------------------------------------------------------------------------------- FWD-7
def _read(rel):
    with open(os.path.join(ROOT, *rel.split("/")), encoding="utf-8") as fh:
        return fh.read()


def _layer_build_outputs():
    out = set()

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "build_output" and isinstance(v, str):
                    out.add(v)
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(json.loads(_read("infra/aws/lambda/ci/lambda-layer-map.json")))
    return out


def rules_present():
    """The cited phrases must be in the cited files, or the rules are not rules and no overlap may be SHARED on them."""
    checks = {
        "R1 CLAUDE.md NEVER-2 entry-on-worker-branch-until-drain": "the entry sits on the worker's branch until the drain"
                                                                  in _read("CLAUDE.md"),
        "R2 function-map README _description single source of truth":
            "Single source of truth for source-to-deployment mapping" in _read("infra/aws/lambda/ci/function-map/README.md"),
        "R2 function-map README _note names record-terraform-deploy.sh as the updater":
            "run record-terraform-deploy.sh after terraform apply" in _read("infra/aws/lambda/ci/function-map/README.md"),
    }
    return checks, _layer_build_outputs()


def classify(pa, pb, build_outputs):
    spec = pa if len(pa) >= len(pb) else pb        # the more specific of the two overlapping paths
    if spec.startswith("org/critical_paths/.open_deploys"):
        return "SHARED", "R1 CLAUDE.md NEVER-2: a worker deploy's entry is its own file and sits on the worker's branch until the drain"
    if spec == "infra/aws/lambda/ci" or spec.startswith("infra/aws/lambda/ci/"):
        return "SHARED", "R2 infra/aws/lambda/ci/function-map _description+_note: single source of truth, record-terraform-deploy.sh is the named updater"
    if spec in build_outputs:
        return "SHARED", "R3 infra/aws/lambda/ci/lambda-layer-map.json build_output: the one declared builder output of the layer"
    if pa == pb:
        return "SPLIT", "R4 both projects name the same file; no rule file covers it (two boxes change one file)"
    # R5 (CTO-issuer ruling on W106-S3/S4): one path is a strict directory-prefix parent of the other and the two are
    # different files. Decided by the path-prefix relation alone: the longer path must be a strict child of the shorter.
    parent, child = (pa, pb) if len(pa) < len(pb) else (pb, pa)
    if child != parent and child.startswith(parent.rstrip("/") + "/"):
        return "NOT-SAME-FILE", ("R5 strict directory-prefix parent: '%s' is a directory claim over '%s', a different file "
                                 "(the two projects change different files)" % (parent, child))
    return "UNCLASSIFIED", "no rule: no R1-R5 applies to this overlap"


def fwd7():
    rc, out = run([sys.executable, os.path.join(ROOT, ".tools", "placement-check.py")])
    if rc != 0:
        print("ERROR: placement-check.py rc=%s" % rc)
        print("FWD7-OVERLAPS total=0 shared=0 split=0 unclassified=0 ok=False")
        return 1
    checks, build_outputs = rules_present()
    for label, present in checks.items():
        print("rule phrase present: %s  %s" % (present, label))
    lines = out.splitlines()
    found = [m for m in (OVERLAP_RE.match(x) for x in lines) if m]
    cross = [int(m.group(1)) for m in (FINDINGS_RE.search(out),) if m]
    table, counts = [], {"SHARED": 0, "SPLIT": 0, "NOT-SAME-FILE": 0, "UNCLASSIFIED": 0}
    for i, m in enumerate(found, 1):
        a, ba, b, bb, pa, pb = m.groups()
        cls, rule = classify(pa, pb, build_outputs)
        counts[cls] += 1
        spec = pa if len(pa) >= len(pb) else pb
        table.append((i, a, ba, b, bb, spec, cls, rule))
    total = len(found)
    rules_ok = all(checks.values())
    count_ok = (cross == [total]) if cross else False
    os.makedirs(DELIV, exist_ok=True)
    with open(TABLE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# FWD-7 placement overlap classes (NFRA_CTLPLN.TO-CT-ai-1, CT-ai-1)\n\n")
        fh.write("Read: `python .tools/placement-check.py` (unchanged), run in the worktree at HEAD + this commit.\n")
        fh.write("Denominator: %d OVERLAP lines read; the read's own FINDINGS line counts %s cross-box overlap(s) (%s).\n\n"
                 % (total, cross[0] if cross else "none", "agrees" if count_ok else "DISAGREES"))
        fh.write("Classes: SHARED = a rule file this test reads and checks (R1-R3 below); SPLIT = both projects name the same "
                 "file, no rule (R4); NOT-SAME-FILE = one path is a strict directory-prefix parent of the other and the two are "
                 "different files (R5, decided by the path-prefix relation); UNCLASSIFIED = no rule.\n\n")
        fh.write("| # | project A (box) | project B (box) | overlapping path | class | rule |\n")
        fh.write("|---|---|---|---|---|---|\n")
        for i, a, ba, b, bb, spec, cls, rule in table:
            fh.write("| %d | %s (%s) | %s (%s) | `%s` | %s | %s |\n" % (i, a, ba, b, bb, spec, cls, rule))
        fh.write("\nRules, checked present in their files at this read: %s\n" % ", ".join(
            "%s=%s" % (k.split(" ")[0] + " " + k.split(" ")[1], v) for k, v in checks.items()))
        fh.write("\nSummary: total=%d shared=%d split=%d not_same_file=%d unclassified=%d\n" % (
            total, counts["SHARED"], counts["SPLIT"], counts["NOT-SAME-FILE"], counts["UNCLASSIFIED"]))
    for row in table:
        print("  %2d %-14s %-12s %s" % (row[0], row[6], row[5], row[7][:60]))
    ok = total > 0 and counts["UNCLASSIFIED"] == 0 and rules_ok and count_ok
    print("placement cross-check: OVERLAP lines=%d, FINDINGS count=%s, agrees=%s" % (total, cross, count_ok))
    print("FWD7-OVERLAPS total=%d shared=%d split=%d not_same_file=%d unclassified=%d ok=%s" % (
        total, counts["SHARED"], counts["SPLIT"], counts["NOT-SAME-FILE"], counts["UNCLASSIFIED"], ok))
    return 0 if ok else 1


def main(argv):
    if argv == ["--fwd2"]:
        return fwd2()
    if argv == ["--fwd7"]:
        return fwd7()
    print("usage: python .tools/tests/test_round19_register.py --fwd2 | --fwd7", file=sys.stderr)
    return 64


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
