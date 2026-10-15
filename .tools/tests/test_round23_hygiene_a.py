#!/usr/bin/env python3
"""test_round23_hygiene_a.py -- NFRA_CTLPLN round 23, CT-am-2 (the round-22 hygiene batch, cell A).

  --guard   HYGIENE-GUARD arms=<k>/<n> ok=<True|False>
            The danger-map build guard (org/modules/graph/nerves_lexical.py build) refuses a linked worktree, a
            sparse tree and a tree whose portal/ holds no tracked content; admits a full main tree with portal;
            writes the header fields (built_from_head, portal_sha, edge_count); and the reflex's refresh
            (comp_pulse.rebuild_risk_map) refuses through the same guard without spawning a build. Every arm runs
            in temporary repositories, never in this tree.
  --check8  HYGIENE-CHECK8 awaiting=<True|False> release_refused=<True|False> ok=<True|False>
            A check 8 whose signature file does not exist is recorded as 'awaiting' (not 'failed') and the release
            refuses with the reason 'check 8 awaits the signature'. A synthetic batch in a temporary intake root.
  --legacy  HYGIENE-LEGACY device=laptop requests=<n> files=<k> attributed_by=batch unattributed=0 ok=<True|False>
            The downloads reader counts the real 20261008 fetch records for laptop, attributed by the batch's
            DEVICE_OF_BATCH.txt. The expectation is counted here, independently, from the record JSON.

Stdlib only, ASCII. Exit 0 when ok, else 1.
"""
import argparse
import io
import importlib.util
import json
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
BUILDER_REL = "org/modules/graph/nerves_lexical.py"
SUPPORT_REL = "org/modules/graph/nerves_resolve.py"
MAP_REL = "org/modules/graph/nerves-risk-edges.json"
COMP_PULSE_REL = "org/modules/graph/comp_pulse.py"
INTAKE_DIR = ROOT / "org" / "devices" / "intake"
RECORDS_DIR = INTAKE_DIR / "records"
DEVICE_OF_BATCH = "DEVICE_OF_BATCH.txt"
REAL_DAY = "20261008"
CORPUS = {
    "CLAUDE.md": "# corpus stub\nNEVER edit the frozen stub.\n",
    "org/critical_paths/HOLD.md": "# hold\nFROZEN until the CTO rules: org/modules/graph/nerves_lexical.py is frozen.\n",
    "org/tier0/ledger/LD-1.md": "# decision\nDO NOT remove the ledger entry.\n",
    "docs/doctrine/DOC.md": "# doctrine\nNEVER skip the gate.\n",
    "docs/references/REF.md": "# reference\nHELD for review.\n",
}


def _rm(path):
    def _onerror(func, p, _exc):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except OSError:
            pass
    shutil.rmtree(str(path), onerror=_onerror)


def _git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), "-c", "user.name=hygiene-test",
                           "-c", "user.email=hygiene-test@example.invalid", *args],
                          capture_output=True, text=True, timeout=120)


def _git_head(cwd):
    out = subprocess.run(["git", "-C", str(cwd), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=60)
    return out.stdout.strip()


def _make_main(base, with_portal=True):
    """A full main repository: the builder and its resolver, the corpus folders, and (optionally) a portal/ that is
    its own checkout, added to the main tree as a gitlink exactly as the real submodule is."""
    main = base / "main"
    for rel in (BUILDER_REL, SUPPORT_REL):
        dst = main / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(ROOT / rel), str(dst))
    for rel, text in CORPUS.items():
        dst = main / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="ascii")
    _git(main, "init", "-q")
    if with_portal:
        portal = main / "portal"
        (portal / "src").mkdir(parents=True)
        (portal / "src" / "App.tsx").write_text("export const App = () => null;\n", encoding="ascii")
        _git(portal, "init", "-q")
        _git(portal, "add", "-A")
        _git(portal, "commit", "-q", "-m", "portal stub")
    _git(main, "add", "-A")
    _git(main, "commit", "-q", "-m", "main stub")
    return main


def _run_build(tree):
    p = subprocess.run([sys.executable, str(tree / BUILDER_REL), "build"], cwd=str(tree),
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def _guard_arms():
    base = pathlib.Path(tempfile.mkdtemp(prefix="hygiene_guard_"))
    arms = []
    try:
        # arm 1: a linked worktree of the main tree is refused
        main = _make_main(base)
        linked = base / "linked"
        _git(main, "worktree", "add", "-q", "--detach", str(linked))
        rc, out = _run_build(linked)
        arms.append(("linked_worktree_refused", rc != 0 and "linked worktree" in out
                     and not (linked / MAP_REL).exists(), out.strip().splitlines()[-1:] if out.strip() else []))

        # arm 2: a sparse tree is refused
        sparse = _make_main(base / "s")
        _git(sparse, "config", "core.sparseCheckout", "true")
        rc, out = _run_build(sparse)
        arms.append(("sparse_refused", rc != 0 and "sparse worktree" in out and not (sparse / MAP_REL).exists(),
                     out.strip().splitlines()[-1:] if out.strip() else []))

        # arm 3: a tree without portal content is refused
        noportal = _make_main(base / "n", with_portal=False)
        rc, out = _run_build(noportal)
        arms.append(("no_portal_refused", rc != 0 and "portal/ absent" in out and not (noportal / MAP_REL).exists(),
                     out.strip().splitlines()[-1:] if out.strip() else []))

        # arm 4: a full main tree with portal is admitted and writes the map
        full = _make_main(base / "f")
        rc, out = _run_build(full)
        written = (full / MAP_REL).is_file()
        arms.append(("full_main_admitted", rc == 0 and "nodes carry claims" in out and written,
                     out.strip().splitlines()[-1:] if out.strip() else []))

        # arm 5: the header names its inputs, equal to the git values of the tree that built it
        header_ok, detail = False, "map absent"
        if written:
            doc = json.loads((full / MAP_REL).read_text(encoding="utf-8"))
            head = _git_head(full)
            portal_head = _git_head(full / "portal")
            edges = doc.get("edges") or []
            header_ok = (doc.get("built_from_head") == head and doc.get("portal_sha") == portal_head
                         and isinstance(doc.get("edge_count"), int) and doc.get("edge_count") == len(edges)
                         and bool(doc.get("built_utc")))
            detail = "built_from_head=%s portal_sha=%s edge_count=%s len_edges=%d" % (
                str(doc.get("built_from_head"))[:12], str(doc.get("portal_sha"))[:12], doc.get("edge_count"), len(edges))
        arms.append(("header_names_inputs", header_ok, [detail]))

        # arm 6: the reflex's refresh refuses through the same guard and spawns no build
        spec = importlib.util.spec_from_file_location("comp_pulse_hygiene_probe", str(ROOT / COMP_PULSE_REL))
        cp = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cp)
        before = cp.BUILD_SPAWNS
        ok_rb, why = cp.rebuild_risk_map(str(linked / MAP_REL))
        refresh_ok = (ok_rb is False and why.startswith(
            "NOT-DECIDABLE: danger map STALE and the build guard refused: linked worktree")
            and cp.BUILD_SPAWNS == before)
        arms.append(("refresh_refused_no_spawn", refresh_ok, [why]))
    finally:
        _rm(base)
    k = sum(1 for _n, good, _d in arms if good)
    for name, good, detail in arms:
        print("HYGIENE-GUARD-ARM %s ok=%s %s" % (name, good, " | ".join(str(x) for x in detail)))
    print("HYGIENE-GUARD arms=%d/%d ok=%s" % (k, len(arms), k == len(arms)))
    return k == len(arms)


def _check8_arm():
    sys.path.insert(0, str(INTAKE_DIR))
    import intake_check as ic  # noqa: E402  (stdlib-only module beside the tests' target)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="hygiene_check8_"))
    try:
        site_dir = tmp / "site"
        ic.build_installed_fixture(site_dir)
        av = tmp / "av.json"
        av.write_text(json.dumps([{"displayName": "Synthetic Antivirus (stand-in)", "productState": 266240}]),
                      encoding="ascii")
        signer = tmp / "signer"
        signer.mkdir()
        cfg = ic.Cfg(root=tmp / "root", records=tmp / "records", av_json=str(av), sites=[site_dir], signer_dir=signer)
        batch = "hygiene-check8-batch"
        hold = cfg.holding(batch)
        hold.mkdir(parents=True)
        wheel = ic.build_synthetic_wheel(hold / ic.syn_file_name())
        ic.write_fetch_record(cfg, batch, wheel)
        approved = tmp / "approved.txt"
        approved.write_text("%s==%s\n" % (ic.SYN_NAME, ic.SYN_VERSION), encoding="ascii")
        missing = str(signer / "CHECK8_NOT_WRITTEN_YET.md")
        record, line = ic.run_check(cfg, batch, wheel.name, approved_by=str(approved), signed_by=missing,
                                    out=io.StringIO(), scan_wait=0)
        checks = record.get("checks") or []
        c8 = checks[7] if len(checks) == 8 else {}
        awaiting = c8.get("verdict") == "awaiting" and "c8=awaiting" in line
        buf = io.StringIO()
        rc = ic.run_release(cfg, batch, wheel.name, out=buf)
        text = buf.getvalue()
        release_refused = (rc == 1 and "reason=check 8 awaits the signature" in text and wheel.is_file()
                           and not cfg.release(batch).exists())
        ok = awaiting and release_refused
        print("HYGIENE-CHECK8-LINE %s" % line)
        print("HYGIENE-CHECK8-RELEASE rc=%d %s" % (rc, text.strip()))
    finally:
        _rm(tmp)
    print("HYGIENE-CHECK8 awaiting=%s release_refused=%s ok=%s" % (awaiting, release_refused, ok))
    return ok


def _day_of(d):
    return str(d.get("at") or "")[:10].replace("-", "")


def _declared_device(batch_dir):
    p = batch_dir / DEVICE_OF_BATCH
    if not p.is_file():
        return None
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            return line.strip()
    return None


def _legacy_arm():
    # the expectation, counted here from the record JSON and the declaration file alone
    recs = []
    for dp, _dn, fn in os.walk(str(RECORDS_DIR)):
        for f in fn:
            if f.endswith(".fetch.json"):
                p = pathlib.Path(dp) / f
                d = json.loads(p.read_text(encoding="utf-8"))
                if _day_of(d) == REAL_DAY:
                    recs.append((p, d))
    exp_files = exp_requests = exp_unattr = 0
    for p, d in recs:
        dev = d.get("device") if "device" in d else _declared_device(p.parent)
        if not dev:
            exp_unattr += 1
        elif dev == "laptop":
            exp_files += 1
            exp_requests += len(d.get("requests") or [])
    real_legacy = sum(1 for p, d in recs if "device" not in d and _declared_device(p.parent) == "laptop")
    # the reader's answer
    proc = subprocess.run([sys.executable, str(INTAKE_DIR / "intake_request.py"), "downloads", "--device", "laptop",
                           "--day", REAL_DAY], cwd=str(ROOT), capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=120)
    line = next((ln for ln in (proc.stdout or "").splitlines() if ln.startswith("DOWNLOADS-TODAY")), "")
    m = re.search(r"requests=(\d+) files=(\d+)( attributed_by=batch)? unattributed=(\d+)", line)
    requests = files = unattr = -1
    attributed = False
    if m:
        requests, files, unattr = int(m.group(1)), int(m.group(2)), int(m.group(4))
        attributed = bool(m.group(3))
    ok = (proc.returncode == 0 and m is not None and real_legacy == 2 and files == exp_files == 2
          and requests == exp_requests and unattr == exp_unattr == 0 and attributed)
    print("HYGIENE-LEGACY-READER rc=%d line=%s" % (proc.returncode, line))
    print("HYGIENE-LEGACY expected files=%d requests=%d unattributed=%d legacy_records=%d"
          % (exp_files, exp_requests, exp_unattr, real_legacy))
    print("HYGIENE-LEGACY device=laptop requests=%d files=%d attributed_by=%s unattributed=%d ok=%s"
          % (requests, files, "batch" if attributed else "none", unattr, ok))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(prog="test_round23_hygiene_a.py")
    ap.add_argument("--guard", action="store_true", help="the map build guard and its header (CT-am-2 ruling 3)")
    ap.add_argument("--check8", action="store_true", help="check 8 awaits the signature (W119-S1)")
    ap.add_argument("--legacy", action="store_true", help="legacy fetch records attributed by the batch (W111-S1)")
    a = ap.parse_args(argv)
    if not (a.guard or a.check8 or a.legacy):
        ap.print_usage()
        return 2
    rc = 0
    if a.guard and not _guard_arms():
        rc = 1
    if a.check8 and not _check8_arm():
        rc = 1
    if a.legacy and not _legacy_arm():
        rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
