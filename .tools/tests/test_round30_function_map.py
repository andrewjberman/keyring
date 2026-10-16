#!/usr/bin/env python3
"""test_round30_function_map.py -- unit arms of the per-function Lambda map (NFRA_CTLPLN TO-CT-ca-1, round 30).

Standard library only, ASCII only, offline. It never reads the live map (retired by the cell) and never runs
aws: every fixture is built in a temporary folder from .tools/tests/fixtures/function_map_base_5.json (5 entries
copied from the base map). Arms:
  1 load_entry reads one function file
  2 load_entry raises FileNotFoundError on a missing function
  3 load_all returns the fixture's functions, sorted by name, equal to the fixture
  4 load_all raises ValueError on an empty folder
  5 load_all raises FileNotFoundError on an absent folder
  6 load_all writes nothing (the folder listing is unchanged)
  7 the reader module is ASCII
  8 the fixture holds exactly 5 entries
  9 naming-gate function_map_problem: a missing folder is reported (fails loud)
 10 naming-gate function_map_problem: an empty folder is reported (fails loud)
 11 naming-gate function_map_problem: the real folder is accepted (when it exists in this tree)
 12 parity-gates.sh lambda-sourcemap with a planted missing folder exits non-zero with an ERROR line
 13 the test file is ASCII

Usage: python .tools/tests/test_round30_function_map.py
Last line: FUNCTION-MAP arms=<k>/<n> ok=<True|False>
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "lib"))
sys.path.insert(0, os.path.join(REPO, ".tools"))
import opal_lambda_map as olm  # noqa: E402

FIXTURE = os.path.join(HERE, "fixtures", "function_map_base_5.json")
FOLDER_REL = os.path.join("infra", "aws", "lambda", "ci", "function-map")

ARMS = []


def arm(name, cond, detail=""):
    ARMS.append((name, bool(cond)))
    print("%s %s %s" % ("PASS" if cond else "FAIL", name, detail))


def load_fixture():
    with open(FIXTURE, encoding="ascii") as f:
        return json.load(f)["functions"]


def build_root(functions):
    """A temporary repository root whose function-map folder holds one <name>.json per fixture entry."""
    root = tempfile.mkdtemp(prefix="fm-root-")
    folder = os.path.join(root, FOLDER_REL)
    os.makedirs(folder)
    for name, entry in functions.items():
        with open(os.path.join(folder, name + ".json"), "w", encoding="ascii", newline="") as f:
            f.write(json.dumps(entry, indent=2, sort_keys=False, ensure_ascii=True) + "\n")
    return root, folder


def load_naming_gate():
    spec = importlib.util.spec_from_file_location("naming_gate_r30", os.path.join(REPO, ".tools", "naming-gate.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git_bash():
    from git_bash_resolver import git_bash as gb  # type: ignore
    return gb()


def main():
    fx = load_fixture()
    names = sorted(fx)
    root, folder = build_root(fx)

    # 1 load_entry reads one function file
    one = olm.load_entry(names[0], root=root)
    arm("load_entry_one", one == fx[names[0]], "name=%s" % names[0])

    # 2 load_entry raises on a missing file
    try:
        olm.load_entry("no-such-function", root=root)
        raised = False
    except FileNotFoundError as e:
        raised = "no-such-function" in str(e)
    arm("load_entry_missing_raises", raised)

    # 3 load_all sorted and equal to the fixture
    got = olm.load_all(root=root)
    arm("load_all_equal_sorted", list(got.keys()) == names and got == fx,
        "keys=%d sorted=%s" % (len(got), list(got.keys()) == names))

    # 4 empty folder raises
    empty_root = tempfile.mkdtemp(prefix="fm-empty-")
    os.makedirs(os.path.join(empty_root, FOLDER_REL))
    try:
        olm.load_all(root=empty_root)
        raised = False
    except ValueError:
        raised = True
    arm("load_all_empty_folder_raises", raised)

    # 5 absent folder raises
    absent_root = tempfile.mkdtemp(prefix="fm-absent-")
    try:
        olm.load_all(root=absent_root)
        raised = False
    except FileNotFoundError:
        raised = True
    arm("load_all_absent_folder_raises", raised)

    # 6 load_all writes nothing
    before = sorted(os.listdir(folder))
    olm.load_all(root=root)
    arm("load_all_never_writes", sorted(os.listdir(folder)) == before)

    # 7 reader module ASCII
    with open(os.path.join(REPO, "lib", "opal_lambda_map.py"), "rb") as f:
        arm("reader_ascii", all(b < 128 for b in f.read()))

    # 8 fixture holds exactly 5 entries
    arm("fixture_five_entries", len(fx) == 5, "n=%d" % len(fx))

    ng = load_naming_gate()
    # 9 missing folder reported
    missing = os.path.join(tempfile.mkdtemp(prefix="fm-ng-"), "no-folder")
    p9 = ng.function_map_problem(missing)
    arm("naming_gate_missing_folder_fails_loud", p9 is not None and "missing" in p9, "problem=%s" % (p9 or "none"))

    # 10 empty folder reported
    empty_dir = tempfile.mkdtemp(prefix="fm-ng-empty-")
    p10 = ng.function_map_problem(empty_dir)
    arm("naming_gate_empty_folder_fails_loud", p10 is not None and "empty" in p10, "problem=%s" % (p10 or "none"))

    # 11 the real folder is accepted when it exists in this tree
    real = os.path.join(REPO, FOLDER_REL)
    if os.path.isdir(real):
        p11 = ng.function_map_problem(real)
        arm("naming_gate_real_folder_accepted", p11 is None, "problem=%s" % (p11 or "none"))
    else:
        arm("naming_gate_real_folder_accepted", False, "the real function-map folder is absent in this tree")

    # 12 parity gate with a planted missing folder fails loud
    bash = git_bash()
    env = dict(os.environ)
    env["PARITY_FUNCTION_MAP"] = missing
    r = subprocess.run([bash, os.path.join(REPO, ".tools", "parity-gates.sh"), "lambda-sourcemap"],
                       cwd=REPO, env=env, capture_output=True, timeout=120)
    out = (r.stdout + r.stderr).decode("utf-8", "replace")
    arm("parity_gate_missing_folder_fails_loud", r.returncode != 0 and "ERROR" in out,
        "rc=%d line=%s" % (r.returncode, [ln for ln in out.splitlines() if "ERROR" in ln][:1]))

    # 13 this test file is ASCII
    with open(os.path.abspath(__file__), "rb") as f:
        arm("test_file_ascii", all(b < 128 for b in f.read()))

    k = sum(1 for _, c in ARMS if c)
    n = len(ARMS)
    print("FUNCTION-MAP arms=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())
