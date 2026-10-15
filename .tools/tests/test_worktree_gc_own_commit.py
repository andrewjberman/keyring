#!/usr/bin/env python3
"""test_worktree_gc_own_commit.py -- CT-af-1: a worktree is MERGED or CLEAN only when its branch carries a commit of
its own, every one of them in the trunk (CTO round-15 ruling 1). Arms (a)-(h) of the cell.

Standard library; temporary repositories only; no AWS, no network. The running-process read is stubbed in-process
(in_use_text), so no real process names a fixture; every --go and --check-removable runs with --repo pointing at a
temporary repository, never at the real repository's worktrees.

Final line: WORKTREE-GC-OWN-COMMIT arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "worktree_gc.py"
N_ARMS = 8


def load_tool():
    spec = importlib.util.spec_from_file_location("worktree_gc_under_test", TOOL)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    mod.in_use_text = lambda: ""  # stub: no running process or scheduled task names a fixture
    return mod


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=str(repo), check=True,
                   capture_output=True, text=True)


def call(mod, *argv: str) -> tuple[int, str]:
    """Run the tool's main() in-process with argv; return (rc, captured stdout)."""
    buf = io.StringIO()
    saved = sys.argv
    sys.argv = ["worktree_gc.py", *argv]
    try:
        with contextlib.redirect_stdout(buf):
            rc = mod.main()
    finally:
        sys.argv = saved
    return rc, buf.getvalue()


def verdict(mod, path: Path, repo: Path) -> tuple[int, str]:
    rc, out = call(mod, "--repo", str(repo), "--check-removable", str(path))
    lines = [ln for ln in out.splitlines() if ln.startswith(("REMOVABLE", "NOT-REMOVABLE", "ERROR"))]
    return rc, (lines[-1] if lines else "(no verdict line)")


def own_commit(tree: Path, name: str) -> None:
    (tree / name).write_text("z\n", encoding="ascii")
    git(tree, "add", name)
    git(tree, "commit", "-q", "-m", f"own {name}")


def build(base: Path) -> dict[str, Path]:
    """Trunk CLOUD with one commit; linked worktrees each made by `git worktree add -b`, one detached."""
    main = base / "main"
    main.mkdir()
    git(main, "init", "-q", "-b", "CLOUD")
    (main / "org" / "mcp").mkdir(parents=True)  # the audit line lands in the temporary repository
    (main / "f.txt").write_text("x\n", encoding="ascii")
    git(main, "add", "f.txt")
    git(main, "commit", "-q", "-m", "c0")
    t = {"main": main}
    for key in ("a", "b", "c", "d", "e", "g"):
        t[key] = base / f"wk-{key}"
        git(main, "worktree", "add", "-q", "-b", f"wk-{key}", str(t[key]), "CLOUD")
    t["f"] = base / "wk-f"
    git(main, "worktree", "add", "-q", "--detach", str(t["f"]), "CLOUD")
    # (a) and (b): branches at their issuance commit; (b) carries one uncommitted file
    (t["b"] / "dirty.txt").write_text("u\n", encoding="ascii")
    # (c), (d), (g): one own commit each, merged into the trunk; (d) then carries one uncommitted file
    for key in ("c", "d", "g"):
        own_commit(t[key], f"{key}.txt")
        git(main, "merge", "-q", "--no-ff", "--no-edit", f"wk-{key}")
    (t["d"] / "dirty.txt").write_text("u\n", encoding="ascii")
    # (e): one own commit NOT in the trunk
    own_commit(t["e"], "e.txt")
    # (g): the branch's reflog file deleted (fail closed)
    reflog = main / ".git" / "logs" / "refs" / "heads" / "wk-g"
    assert reflog.is_file(), "fixture precondition: wk-g must have a reflog before it is deleted"
    reflog.unlink()
    return t


def run_arms(mod, base: Path) -> list[tuple[str, bool]]:
    t = build(base)
    main = t["main"]
    v = {}
    for key in ("a", "b", "c", "d", "e", "f", "g"):
        v[key] = verdict(mod, t[key], main)
    v["h"] = verdict(mod, base / "not-a-worktree", main)
    # one --go against the temporary repository, after every verdict (MERGED wk-d is force-removed by design)
    go_rc, _ = call(mod, "--repo", str(main), "--go", "--clean-hours", "0")
    alive = {k: t[k].is_dir() for k in ("a", "b", "c", "d", "e", "f", "g")}
    return [
        ("(a) issuance commit, clean: NOT-REMOVABLE UNSTARTED, rc 1; --go keeps the directory",
         v["a"][0] == 1 and v["a"][1].startswith("NOT-REMOVABLE UNSTARTED") and alive["a"]),
        ("(b) issuance commit, dirty: NOT-REMOVABLE UNSTARTED; --go keeps the directory and the file",
         v["b"][0] == 1 and v["b"][1].startswith("NOT-REMOVABLE UNSTARTED") and alive["b"]
         and (t["b"] / "dirty.txt").is_file()),
        ("(c) one own commit merged, clean: REMOVABLE CLEAN rc 0; --go removes the directory",
         v["c"][0] == 0 and v["c"][1].startswith("REMOVABLE CLEAN") and go_rc == 0 and not alive["c"]),
        ("(d) one own commit merged, dirty: REMOVABLE-AFTER-PRESERVE rc 0 (CT-ag-1: --go preserves the dirt first)",
         v["d"][0] == 0 and v["d"][1].startswith("REMOVABLE-AFTER-PRESERVE MERGED")
         and "1 path(s) would be preserved" in v["d"][1]),
        ("(e) one own commit NOT in the trunk, clean: NOT-REMOVABLE HELD rc 1; --go keeps the directory",
         v["e"][0] == 1 and v["e"][1].startswith("NOT-REMOVABLE HELD") and alive["e"]),
        ("(f) detached HEAD at a trunk commit: NOT-REMOVABLE UNSTARTED own=unknown rc 1; --go keeps it",
         v["f"][0] == 1 and v["f"][1].startswith("NOT-REMOVABLE UNSTARTED own=unknown") and alive["f"]),
        ("(g) branch reflog file deleted: NOT-REMOVABLE UNSTARTED own=unknown rc 1 (fail closed); --go keeps it",
         v["g"][0] == 1 and v["g"][1].startswith("NOT-REMOVABLE UNSTARTED own=unknown") and alive["g"]),
        ("(h) a path that is not a worktree: rc 2",
         v["h"][0] == 2 and v["h"][1].startswith("ERROR")),
    ]


def _clear_readonly(func, path, _exc):
    """git object files are read-only on Windows; clear the bit and retry so the temporary tree is removed."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def main() -> int:
    base = Path(tempfile.mkdtemp(prefix="wtgc_own_")).resolve()
    mod = load_tool()
    try:
        arms = run_arms(mod, base)
    finally:
        shutil.rmtree(base, onerror=_clear_readonly)
    for name, ok in arms:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    passed = sum(1 for _, ok in arms if ok)
    print(f"WORKTREE-GC-OWN-COMMIT arms={passed}/{len(arms)} ok={passed == len(arms) == N_ARMS}")
    return 0 if passed == len(arms) == N_ARMS else 1


if __name__ == "__main__":
    sys.exit(main())
