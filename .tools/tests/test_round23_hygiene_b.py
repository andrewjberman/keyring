#!/usr/bin/env python3
"""Round-23 hygiene batch B (NFRA_CTLPLN, cell CT-am-3): two checks that the crossbox tools hold.

Run from the worktree root:
  python .tools/tests/test_round23_hygiene_b.py --merge
      the merge arms of .tools/crossbox-call.py (S9121): a null bus_message_id merges; a refused merge writes nothing.
      LAST line: HYGIENE-MERGE arms=<k>/<n> ok=<True|False>
  python .tools/tests/test_round23_hygiene_b.py --sparse
      cuts a temporary SPARSE worktree with .tools/wk-provision.sh (outside the ajb_wk checkouts), runs
      .tools/tests/test_crossbox_call.py in it, then removes the worktree, its portal and its temporary branch in a finally.
      LAST line: HYGIENE-SPARSE crossbox_cases=<pass>/<total> ok=<True|False>
      pass counts the cases that PASS; a case skipped with a printed reason (its folder is absent from the sparse set) is
      listed on a SKIP line before the last line and is not a failure. ok needs no failing case and a zero exit code.
Nothing is pushed, sent or deployed. Every experiment runs in temporary folders or repositories.
"""
from __future__ import annotations

import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import git_bash_resolver  # noqa: E402  the estate's canonical Git Bash, never a bare `bash` (the WSL stub)

# the sparse set this worktree was cut with (the folders the worker face names), mirrored for the temporary worktree
SPARSE_FOLDERS = ["infra/logic/registry", "lib", "org/devices", "org/modules/graph", "org/ref", "org/standards"]
TASK_ORDER_GLOB = "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-am-3.*.md"
SUITE_LAST = re.compile(r"CROSSBOX-TEST cases=(\d+)/(\d+) ok=(True|False)$")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cb = load("crossbox_call_hygiene_b", TOOLS / "crossbox-call.py")


def run_merge() -> int:
    tmp = tempfile.mkdtemp(prefix="hygiene-b-merge-")
    arms = []
    try:
        arms = cb.merge_cases(tmp)
    except Exception as exc:   # a harness that cannot run is a failed arm, never a pass
        print("FAIL the merge arms could not run -- %s: %s" % (type(exc).__name__, exc))
    finally:
        cb.rmtree_force(tmp)
    for name, ok, detail in arms:
        print("%s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok or not detail else "  -- " + detail))
    good = sum(1 for _, ok, _ in arms if ok)
    print("HYGIENE-MERGE arms=%d/%d ok=%s" % (good, len(arms), bool(arms) and good == len(arms)))
    return 0 if arms and good == len(arms) else 1


def provision(wt: Path, n: str, order_rel: list) -> subprocess.CompletedProcess:
    argv = git_bash_resolver.bash_argv(".tools/wk-provision.sh", "provision", "NFRA_CTLPLN", n, "--path", str(wt),
                                       "--node-modules", "none")
    for folder in SPARSE_FOLDERS:
        argv += ["--sparse-add", folder]
    for rel in order_rel:
        argv += ["--order", rel]
    return subprocess.run(argv, cwd=str(REPO), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=150)


def remove(wt: Path, branch: str) -> list:
    notes = []
    rm = subprocess.run(git_bash_resolver.bash_argv(".tools/wk-provision.sh", "remove", str(wt)), cwd=str(REPO),
                        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    notes.append("remove rc=%d" % rm.returncode)
    for name in (branch, branch + "-portal"):
        if name == "wk-NFRA_CTLPLN-125" or not name.startswith("wk-NFRA_CTLPLN-125s"):
            notes.append("REFUSED to delete %s (not this test's temporary branch)" % name)
            continue
        dl = subprocess.run(["git", "-C", str(REPO), "branch", "-D", name], capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=60)
        notes.append("branch -D %s rc=%d" % (name, dl.returncode))
    return notes


def run_sparse() -> int:
    root = Path(tempfile.mkdtemp(prefix="hygiene-b-sparse-"))   # the system temp folder, outside C:/Users/AndrewBerman/Desktop/ajb_wk/
    n = "125s%d" % os.getpid()
    branch = "wk-NFRA_CTLPLN-%s" % n
    wt = root / "wt"
    passed = failed = skipped = 0
    total = 0
    suite_total = None
    suite_ok = False
    try:
        order_rel = sorted(p.relative_to(REPO).as_posix() for p in REPO.glob(TASK_ORDER_GLOB))
        prov = provision(wt, n, order_rel)
        if prov.returncode != 0:
            print("HYGIENE-SPARSE-PROVISION rc=%d %s" % (prov.returncode, (prov.stderr or prov.stdout).strip()[-300:]))
        else:
            print("HYGIENE-SPARSE-PROVISION rc=0 worktree=%s branch=%s folders=%s order=%s" % (
                wt, branch, ", ".join(SPARSE_FOLDERS), ", ".join(order_rel) or "none"))
            print("HYGIENE-SPARSE-SET org/mcp present=%s" % (wt / "org" / "mcp").is_dir())
            run = subprocess.run([sys.executable, ".tools/tests/test_crossbox_call.py"], cwd=str(wt), capture_output=True,
                                 text=True, encoding="utf-8", errors="replace", timeout=200)
            lines = run.stdout.splitlines()
            for line in lines:
                if line.startswith("FAIL ") or line.startswith("skip ") or line.startswith("CROSSBOX-TEST"):
                    print(line)
            passed = sum(1 for line in lines if line.startswith("ok  "))
            failed = sum(1 for line in lines if line.startswith("FAIL "))
            skipped = sum(1 for line in lines if line.startswith("skip "))
            total = passed + failed + skipped
            last = lines[-1] if lines else ""
            m = SUITE_LAST.search(last)
            if m:
                suite_total = int(m.group(2))
                suite_ok = run.returncode == 0 and failed == 0 and total == suite_total and m.group(3) == "True"
            else:
                suite_ok = False
            if run.returncode != 0 and not m:
                print("HYGIENE-SPARSE-RUN rc=%d no CROSSBOX-TEST last line: %s" % (run.returncode, (run.stderr or "").strip()[-300:]))
    except Exception as exc:   # a provisioning or run error is a failed check, never a pass
        print("HYGIENE-SPARSE-ERROR %s: %s" % (type(exc).__name__, exc))
        suite_ok = False
    finally:
        for note in remove(wt, branch):
            print("HYGIENE-SPARSE-CLEANUP " + note)
        shutil.rmtree(root, ignore_errors=True)
    ok = bool(suite_ok) and total > 0 and failed == 0
    print("HYGIENE-SPARSE crossbox_cases=%d/%d ok=%s" % (passed, total, ok))
    return 0 if ok else 1


def main(argv: list) -> int:
    if "--merge" in argv:
        return run_merge()
    if "--sparse" in argv:
        return run_sparse()
    print("usage: test_round23_hygiene_b.py --merge | --sparse", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
