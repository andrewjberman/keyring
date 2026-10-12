#!/usr/bin/env python3
"""sc_r21_trunk_first.py -- MDPF_SECCLASS round 21 cell SC-e-92 (row D1-S28): the two limbs of the cross-box deploy check that STOP a
ship on stale or unreadable worktree state although nothing contends. Drives `.tools/crossbox-deploy-check.py` (imported by path)
against throwaway git repos in a temp directory; no repo of this workspace is read or written. Run from the repo root being graded.

Usage:  python sc_r21_trunk_first.py <lagging|vanished|planted>

TRUNK is the HEAD of the checkout the check runs in (the `repo_root` argument). A worktree is LAGGING when its HEAD has not taken the
commit that deleted a sentinel at trunk.

lagging  : (limb d) a slug whose sentinel was committed at trunk and then DELETED at trunk (the ledger closed there) but still reads
           HELD in a lagging worktree's HEAD draws 0 OPEN-DEPLOY hits.
           Prints  TRUNK-FIRST ok=<bool> case=lagging hits=<n>
vanished : (limb e) a registered worktree whose directory is gone (prunable) is classified VANISHED in the denominator line and draws
           0 hits.   Prints  TRUNK-FIRST ok=<bool> case=vanished hits=<n> vanished=<n>
planted  : (the CONTROL for both limbs) (a) a live sentinel at trunk HEAD, another author, naming the carried file, still draws exactly
           1 hit; (b) a sentinel that exists ONLY on a worker's branch (never at trunk: a deploy open on its branch until the drain)
           still draws exactly 1 hit.   Prints  TRUNK-FIRST ok=<bool> case=planted trunk_hits=<n> branch_only_hits=<n>
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path.cwd()
TOOL = ROOT / ".tools" / "crossbox-deploy-check.py"
CARRIED = "data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py"
REL = "data/black_diamond"
OWN, OTHER = "0.7.0_AE_CloudOps~SC1", "0.7.0_AE_CloudOps~RA1"
SENT_DIR = "org/critical_paths/.open_deploys"
ENV = dict(os.environ, GIT_AUTHOR_NAME="chk", GIT_AUTHOR_EMAIL="chk@example.invalid",
           GIT_COMMITTER_NAME="chk", GIT_COMMITTER_EMAIL="chk@example.invalid")


def _git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, env=ENV, timeout=60, check=True)


def _tool():
    spec = importlib.util.spec_from_file_location("cdc_r21_under_test", str(TOOL))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _sentinel(path, slug, author, status):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "slug": slug, "author": author, "status": status, "opened_at": "2026-10-12T00:00:00Z",
        "legs": [{"id": "L1", "target": "code/gold/ -- " + CARRIED, "proof": "shipped " + CARRIED}],
    }, indent=2), encoding="utf-8")


def _repo(td):
    repo = Path(td) / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    (repo / "README").write_text("x", encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "base")
    return repo


def _commit(repo, msg):
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", msg)


def case_lagging():
    mod = _tool()
    with tempfile.TemporaryDirectory() as td:
        repo = _repo(td)
        _sentinel(repo / SENT_DIR / "closed-at-trunk.json", "closed-at-trunk", OTHER, "HELD-SOVEREIGN-GATED")
        _commit(repo, "open the deploy")
        wt = Path(td) / "lagging"
        _git(repo, "worktree", "add", "-q", "-b", "lagging", str(wt))  # its HEAD carries the sentinel
        (repo / SENT_DIR / "closed-at-trunk.json").unlink()
        _commit(repo, "ledger closed at trunk: sentinel deleted")
        hits, _ = mod.measure_open_deploy(str(repo), REL, OWN, files=[CARRIED])
    ok = len(hits) == 0
    print(f"TRUNK-FIRST ok={ok} case=lagging hits={len(hits)}")
    return 0 if ok else 1


def case_vanished():
    mod = _tool()
    with tempfile.TemporaryDirectory() as td:
        repo = _repo(td)
        wt = Path(td) / "gone"
        _git(repo, "worktree", "add", "-q", "-b", "gone", str(wt))
        shutil.rmtree(wt, ignore_errors=True)  # the registration stays: prunable
        hits, lines = mod.measure_open_deploy(str(repo), REL, OWN, files=[CARRIED])
        denom = [ln for ln in lines if "denominator:" in ln]
    vanished = -1
    if denom:
        for part in denom[-1].replace(",", " ").split():
            if part.startswith("vanished="):
                vanished = int(part.split("=")[1])
    ok = len(hits) == 0 and vanished >= 1
    print(f"TRUNK-FIRST ok={ok} case=vanished hits={len(hits)} vanished={vanished}")
    return 0 if ok else 1


def case_planted():
    mod = _tool()
    with tempfile.TemporaryDirectory() as td:
        repo = _repo(td)
        _sentinel(repo / SENT_DIR / "live-at-trunk.json", "live-at-trunk", OTHER, "OPEN")
        _commit(repo, "open the deploy at trunk")
        trunk_hits = len(mod.measure_open_deploy(str(repo), REL, OWN, files=[CARRIED])[0])
    with tempfile.TemporaryDirectory() as td:
        repo = _repo(td)
        wt = Path(td) / "worker"
        _git(repo, "worktree", "add", "-q", "-b", "worker", str(wt))
        _sentinel(wt / SENT_DIR / "branch-only.json", "branch-only", OTHER, "OPEN")
        _commit(wt, "deploy open on the worker's branch until the drain")
        branch_hits = len(mod.measure_open_deploy(str(repo), REL, OWN, files=[CARRIED])[0])
    ok = trunk_hits == 1 and branch_hits == 1
    print(f"TRUNK-FIRST ok={ok} case=planted trunk_hits={trunk_hits} branch_only_hits={branch_hits}")
    return 0 if ok else 1


if __name__ == "__main__":
    fns = {"lagging": case_lagging, "vanished": case_vanished, "planted": case_planted}
    if len(sys.argv) != 2 or sys.argv[1] not in fns:
        print("TRUNK-FIRST ok=False error=usage (lagging|vanished|planted)")
        sys.exit(2)
    sys.exit(fns[sys.argv[1]]())
