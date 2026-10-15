#!/usr/bin/env python3
"""NFRA_CTLPLN round 22, cell CT-al-3 (hygiene batch): the danger map's age, its one rebuild, and the sparse rule.

Run: python .tools/tests/test_round22_hygiene.py --map-age
     (LAST line: HYGIENE-MAPAGE inside_time=<True|False> mtime_ignored=<True|False> rebuild_once=<True|False> ok=<True|False>)
     Temporary copies of a map only. An aged embedded built_utc (mtime fresh) must read STALE from inside the file,
     and the rebuild stub must be called exactly once; a fresh embedded built_utc with an OLD mtime must read FRESH
     with no rebuild; a map with no built_utc must read STALE and be rebuilt once.

Run: python .tools/tests/test_round22_hygiene.py --sparse
     (LAST line: HYGIENE-SPARSE builds=<n> reads_main_or_blind=<True|False> ok=<True|False>)
     A linked worktree made sparse (core.sparseCheckout true) in a TEMPORARY repository, without a map. The reflex
     must never build there (builds = child builds started by the reflex + map files a direct build attempt
     writes; both must be 0), and must read the main tree's map, or report BLIND when the main tree has none.
     A linked sparse worktree holding its own fresh map reads that map and builds nothing.

Nothing in the real tree is written: every map lives under a temporary folder.
"""
import datetime as dt
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
ROOT = TOOLS.parent
SCRIPT = ROOT / "org" / "modules" / "graph" / "comp_pulse.py"
GRAPH_FILES = ("nerves_lexical.py", "nerves_resolve.py")
MAP_REL = os.path.join("org", "modules", "graph", "nerves-risk-edges.json")


def utc(hours_ago: float) -> str:
    return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=hours_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_reflex():
    spec = importlib.util.spec_from_file_location("comp_pulse_under_test", str(SCRIPT))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write_map(path: Path, built_utc=None, mtime_days_ago=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = {"_README": "temporary test map", "stats": {}, "edges": []}
    if built_utc is not None:
        doc["built_utc"] = built_utc
    path.write_text(json.dumps(doc), encoding="utf-8")
    if mtime_days_ago is not None:
        past = dt.datetime.now().timestamp() - mtime_days_ago * 86400
        os.utime(str(path), (past, past))


class Stub:
    """The rebuild stub: counts its calls and writes a fresh built_utc, as nerves_lexical build would."""

    def __init__(self):
        self.calls = 0

    def __call__(self, map_path):
        self.calls += 1
        doc = json.loads(Path(map_path).read_text(encoding="utf-8"))
        doc["built_utc"] = utc(0)
        Path(map_path).write_text(json.dumps(doc), encoding="utf-8")
        return True, "stub rebuild"


def map_arm(mod, work: Path):
    mod.is_sparse_tree = lambda tree: False   # the age arm is about the embedded time; no git query on a temp tree
    tree = work / "tree"
    # (a) aged embedded time, fresh mtime: the age must come from inside the file.
    a_map = tree / "a" / "nerves-risk-edges.json"
    write_map(a_map, built_utc=utc(100), mtime_days_ago=0)
    a_pre = mod.RiskSource(str(a_map))
    a_stub = Stub()
    a_src, _note, _blind = mod.resolve_risk_map(str(tree / "a"), str(a_map), rebuild=a_stub)
    inside_time = (a_pre.stale and a_pre.age_h is not None and 99.0 < a_pre.age_h < 101.0
                   and a_stub.calls == 1 and not a_src.stale)
    # (b) fresh embedded time, OLD mtime (30 days): mtime must be ignored.
    b_map = tree / "b" / "nerves-risk-edges.json"
    write_map(b_map, built_utc=utc(1), mtime_days_ago=30)
    b_stub = Stub()
    b_src, _note, _blind = mod.resolve_risk_map(str(tree / "b"), str(b_map), rebuild=b_stub)
    mtime_ignored = (not b_src.stale and b_src.age_h is not None and 0.5 < b_src.age_h < 1.5
                     and b_stub.calls == 0)
    # (c) no embedded time: unknown age, STALE, rebuilt once.
    c_map = tree / "c" / "nerves-risk-edges.json"
    write_map(c_map, built_utc=None, mtime_days_ago=0)
    c_pre = mod.RiskSource(str(c_map))
    c_stub = Stub()
    c_src, _note, _blind = mod.resolve_risk_map(str(tree / "c"), str(c_map), rebuild=c_stub)
    no_field_stale = c_pre.stale and c_pre.age_h is None and c_stub.calls == 1 and not c_src.stale
    rebuild_once = a_stub.calls == 1 and b_stub.calls == 0 and c_stub.calls == 1
    ok = inside_time and mtime_ignored and rebuild_once and no_field_stale
    print("  map-age: aged embedded=%.1fh mtime-fresh stale=%s rebuilds=%d | fresh embedded=%.1fh mtime-30d "
          "stale=%s rebuilds=%d | no field stale=%s rebuilds=%d"
          % (a_pre.age_h or -1, a_pre.stale, a_stub.calls, b_src.age_h or -1, b_src.stale, b_stub.calls,
             c_pre.stale, c_stub.calls))
    print("HYGIENE-MAPAGE inside_time=%s mtime_ignored=%s rebuild_once=%s ok=%s"
          % (inside_time, mtime_ignored, rebuild_once, ok))
    return 0 if ok else 1


def git(repo, *args):
    p = subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", str(repo), *args],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    if p.returncode != 0:
        raise RuntimeError("git %s rc=%d: %s" % (" ".join(args), p.returncode, p.stderr.strip()))
    return p.stdout


def sparse_arm(mod, work: Path):
    main = work / "main"
    wt = work / "wt"
    main_map = main / MAP_REL
    wt_map = wt / MAP_REL
    main.mkdir()
    git(main, "init", "-q", "-b", "CLOUD", ".")
    git(main, "config", "extensions.worktreeConfig", "true")
    (main / "README.txt").write_text("fixture\n", encoding="utf-8")
    git(main, "add", "--", "README.txt")
    git(main, "commit", "-q", "-m", "fixture")
    # The main tree holds a fresh map, UNTRACKED (the sparse worktree does not check it out).
    write_map(main_map, built_utc=utc(1), mtime_days_ago=0)
    git(main, "worktree", "add", "-q", str(wt), "-b", "wt-sparse")
    git(wt, "config", "--worktree", "core.sparseCheckout", "true")
    graph_src = ROOT / "org" / "modules" / "graph"
    (wt / "org" / "modules" / "graph").mkdir(parents=True, exist_ok=True)
    for name in GRAPH_FILES:   # the real builder is present in the sparse tree; the guard must still refuse it
        shutil.copy2(str(graph_src / name), str(wt / "org" / "modules" / "graph" / name))

    # (1) sparse, no own map: the reflex reads the MAIN map and builds nothing.
    spawns0 = mod.BUILD_SPAWNS
    src1, note1, blind1 = mod.resolve_risk_map(str(wt), str(wt_map), rebuild=mod.rebuild_risk_map)
    reads_main = (not blind1 and src1.exists and os.path.samefile(src1.path, str(main_map)))
    # (2) a direct build attempt in the sparse tree: refused, and no map file written.
    p = subprocess.run([sys.executable, str(wt / "org" / "modules" / "graph" / "nerves_lexical.py"), "build"],
                       cwd=str(wt), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    direct_refused = p.returncode == 2 and "BLOCKED" in (p.stdout + p.stderr)
    direct_wrote = wt_map.exists()
    # (3) main map removed: sparse, no map anywhere: BLIND.
    parked = main_map.with_name(main_map.name + ".parked")
    os.replace(str(main_map), str(parked))
    try:
        _src3, note3, blind3 = mod.resolve_risk_map(str(wt), str(wt_map), rebuild=mod.rebuild_risk_map)
    finally:
        os.replace(str(parked), str(main_map))
    reads_main_or_blind = reads_main and blind3
    builds = (mod.BUILD_SPAWNS - spawns0) + (1 if direct_wrote else 0)
    # (4) informational + graded: a sparse worktree holding its OWN fresh map reads it, builds nothing.
    write_map(wt_map, built_utc=utc(1), mtime_days_ago=0)
    spawns1 = mod.BUILD_SPAWNS
    src4, _note4, blind4 = mod.resolve_risk_map(str(wt), str(wt_map), rebuild=mod.rebuild_risk_map)
    own_fresh_ok = (not blind4 and os.path.samefile(src4.path, str(wt_map)) and not src4.stale
                    and mod.BUILD_SPAWNS == spawns1)
    print("  sparse: (1) own absent -> main map read=%s note=%s" % (reads_main, note1))
    print("  sparse: (2) direct build rc=%d refused=%s wrote_map=%s" % (p.returncode, direct_refused, direct_wrote))
    print("  sparse: (3) main map absent -> blind=%s note=%s" % (blind3, note3))
    print("  sparse: (4) own fresh map read=%s builds=%d" % (own_fresh_ok, mod.BUILD_SPAWNS - spawns1))
    ok = builds == 0 and reads_main_or_blind and direct_refused and not direct_wrote and own_fresh_ok
    print("HYGIENE-SPARSE builds=%d reads_main_or_blind=%s ok=%s" % (builds, reads_main_or_blind, ok))
    return 0 if ok else 1


def main(argv) -> int:
    if "--map-age" not in argv and "--sparse" not in argv:
        print("usage: python .tools/tests/test_round22_hygiene.py --map-age | --sparse")
        return 2
    if not SCRIPT.is_file():
        print("ERROR: missing %s" % SCRIPT)
        return 2
    mod = load_reflex()
    work = Path(tempfile.mkdtemp(prefix="hygiene_r22_"))
    try:
        if "--map-age" in argv:
            return map_arm(mod, work)
        return sparse_arm(mod, work)
    finally:
        shutil.rmtree(str(work), ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
