#!/usr/bin/env python3
"""seatgates_limbs_check.py -- MDPF_SECCLASS round 20 cell SC-e-89 (rows D1-S23, D1-S25): the three limbs of the cross-box deploy check
that drew false STOPs on one-key ships. Drives `.tools/crossbox-deploy-check.py` (imported by path) against throwaway git repos in a
temp directory; no repo of this workspace is read or written. Run from the repo root being graded.

Usage:  python seatgates_limbs_check.py <call|own|slug>

call : (limb a, a CONTROL at the cut) a live cross-box call whose body quotes the shared root token `data/black_diamond` and a second
       root `data/cot` but names no carried file draws 0 OPEN-CALL hits for a one-file ship; the same call naming the carried file's
       bare name draws exactly 1. Prints  LIMB-CALL ok=<bool> unrelated=<n> related=<n>
own  : (limb b) `resolve_serial("")` returns the acting seat from OPAL_AGENT_SERIAL (no session file or git name consulted first), and
       with that serial the deploy's OWN open ledger entry draws 0 OPEN-DEPLOY hits while another lane's open entry that names the
       carried file still draws exactly 1. Prints  LIMB-OWN ok=<bool> resolved=<serial|MISSING> own_hits=<n> other_hits=<n>
slug : (limb c) one slug whose sentinel reads two different statuses in two worktrees' HEADs counts ONCE.
       Prints  LIMB-SLUG ok=<bool> hits=<n>
"""
import datetime
import importlib.util
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path.cwd()
TOOL = ROOT / ".tools" / "crossbox-deploy-check.py"
CARRIED = "data/black_diamond/scripts/gold/D_04.client_portal_summary.py"
REL = "data/black_diamond"
ENV = dict(os.environ, GIT_AUTHOR_NAME="chk", GIT_AUTHOR_EMAIL="chk@example.invalid",
           GIT_COMMITTER_NAME="chk", GIT_COMMITTER_EMAIL="chk@example.invalid")


def _git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, env=ENV, timeout=60, check=True)


def _tool():
    spec = importlib.util.spec_from_file_location("cdc_under_test", str(TOOL))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _sentinel(path, slug, author, status):
    import json
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "slug": slug, "author": author, "status": status, "opened_at": "2026-10-11T00:00:00Z",
        "legs": [{"id": "L1", "target": "code/gold/ -- " + CARRIED, "proof": "shipped " + CARRIED}],
    }, indent=2), encoding="utf-8")


def _repo(td, sentinels):
    repo = Path(td) / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    for slug, author, status in sentinels:
        _sentinel(repo / "org/critical_paths/.open_deploys" / f"{slug}.json", slug, author, status)
    (repo / "README").write_text("x", encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "base")
    return repo


def limb_call():
    mod = _tool()
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0, tzinfo=None)
    counts = []
    for names_file in (False, True):
        with tempfile.TemporaryDirectory() as td:
            repo = _repo(td, [])
            body = repo / "body.md"
            body.write_text("ship data/black_diamond and data/cot soon" + (" incl D_04.client_portal_summary.py" if names_file else ""),
                            encoding="utf-8")
            cb = repo / "org/devices/crossbox"
            cb.mkdir(parents=True)
            (cb / "XB-test.json").write_text('{"state": "OPEN", "from_device": "a", "to_device": "b", "body_path": "body.md"}', encoding="utf-8")
            hits, _ = mod.measure_open_call(str(repo), REL, [], now, files=[CARRIED])
            counts.append(len(hits))
    ok = counts == [0, 1]
    print(f"LIMB-CALL ok={ok} unrelated={counts[0]} related={counts[1]}")
    return 0 if ok else 1


def limb_own():
    mod = _tool()
    own, other = "0.7.0_AE_CloudOps~SC1", "0.7.0_AE_CloudOps~RA1"
    resolved = "MISSING"
    saved = {k: os.environ.get(k) for k in ("OPAL_AGENT_SERIAL", "CLAUDE_CODE_SESSION_ID", "GIT_AUTHOR_NAME")}
    try:
        os.environ["OPAL_AGENT_SERIAL"] = own
        os.environ.pop("CLAUDE_CODE_SESSION_ID", None)
        os.environ["GIT_AUTHOR_NAME"] = "someone-else"
        fn = getattr(mod, "resolve_serial", None)
        if fn is not None:
            resolved = fn("")
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    own_hits = other_hits = -1
    with tempfile.TemporaryDirectory() as td:
        repo = _repo(td, [("own-entry", own, "OPEN")])
        own_hits = len(mod.measure_open_deploy(str(repo), REL, resolved if resolved != "MISSING" else "", files=[CARRIED])[0])
    with tempfile.TemporaryDirectory() as td:
        repo = _repo(td, [("other-entry", other, "OPEN")])
        other_hits = len(mod.measure_open_deploy(str(repo), REL, own, files=[CARRIED])[0])
    ok = resolved == own and own_hits == 0 and other_hits == 1
    print(f"LIMB-OWN ok={ok} resolved={resolved} own_hits={own_hits} other_hits={other_hits}")
    return 0 if ok else 1


def limb_slug():
    mod = _tool()
    with tempfile.TemporaryDirectory() as td:
        repo = _repo(td, [("one-slug", "0.7.0_AE_CloudOps~SC1", "OPEN")])
        wt = Path(td) / "wt"
        _git(repo, "worktree", "add", "-q", "-b", "held", str(wt))
        _sentinel(wt / "org/critical_paths/.open_deploys/one-slug.json", "one-slug", "0.7.0_AE_CloudOps~SC1", "HELD-SOVEREIGN-GATED")
        _git(wt, "add", "-A")
        _git(wt, "commit", "-q", "-m", "status moved")
        hits = len(mod.measure_open_deploy(str(repo), REL, "0.7.0_AE_CloudOps~RA1", files=[CARRIED])[0])
    ok = hits == 1
    print(f"LIMB-SLUG ok={ok} hits={hits}")
    return 0 if ok else 1


if __name__ == "__main__":
    fns = {"call": limb_call, "own": limb_own, "slug": limb_slug}
    if len(sys.argv) != 2 or sys.argv[1] not in fns:
        print("LIMB ok=False error=usage (call|own|slug)")
        sys.exit(2)
    sys.exit(fns[sys.argv[1]]())
