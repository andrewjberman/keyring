#!/usr/bin/env python3
"""test_worktree_gc_preserve.py -- CT-ag-1: --go preserves a merged worktree's dirt before it removes the worktree
(CTO round-16 ruling 1), gitignored paths are not dirt (ruling 2), and --only restricts one worktree (build item 5).

Arms (a)-(h) of the cell, plus arm (i): a sparse checkout's out-of-cone file is preserved as HEAD content, never
recorded as deleted.

Standard library; temporary repositories only; no AWS, no network. The running-process read is stubbed in-process
(in_use_text), so no real process names a fixture. Every --go runs with --only and --repo pointing at a temporary
repository; the real repository's worktrees are never named.

Final line: WORKTREE-GC-PRESERVE arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

TOOL = Path(__file__).resolve().parent.parent / "worktree_gc.py"
N_ARMS = 9
PRESERVED_RX = re.compile(r"^PRESERVED (\S+) -> (preserve/\S+-(\d{8}T\d{6}Z)) ([0-9a-f]{40}) \((\d+) path\(s\)\)$",
                          re.M)


def load_tool():
    spec = importlib.util.spec_from_file_location("worktree_gc_preserve_under_test", TOOL)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    mod.in_use_text = lambda: ""  # stub: no running process or scheduled task names a fixture
    return mod


def gitout(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=str(repo),
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def git(repo: Path, *args: str) -> str:
    res = gitout(repo, *args)
    if res.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed in {repo}: {res.stderr.strip()}")
    return res.stdout


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


def go_only(mod, path: Path, repo: Path) -> tuple[int, str]:
    return call(mod, "--repo", str(repo), "--go", "--only", str(path), "--clean-hours", "0")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("ascii"))


def base_repo(parent: Path) -> Path:
    """Trunk CLOUD: one commit with a .gitignore that ignores *.local, a tracked f.txt and the audit folder."""
    main = parent / "main"
    main.mkdir(parents=True)
    git(main, "init", "-q", "-b", "CLOUD")
    (main / "org" / "mcp").mkdir(parents=True)  # the audit line lands in the temporary repository
    write(main / ".gitignore", "*.local\n")
    write(main / "f.txt", "x\n")
    git(main, "add", ".gitignore", "f.txt")
    git(main, "commit", "-q", "-m", "c0")
    return main


def add_worktree(main: Path, parent: Path, key: str) -> Path:
    path = parent / f"wk-{key}"
    git(main, "worktree", "add", "-q", "-b", f"wk-{key}", str(path), "CLOUD")
    return path


def own_and_merge(main: Path, tree: Path, key: str) -> None:
    """One own commit on the worktree's branch, merged into the trunk (the MERGED / CLEAN precondition)."""
    write(tree / f"{key}.txt", "z\n")
    git(tree, "add", f"{key}.txt")
    git(tree, "commit", "-q", "-m", f"own {key}")
    git(main, "merge", "-q", "--no-ff", "--no-edit", f"wk-{key}")


def own_only(tree: Path, key: str) -> None:
    """One own commit on the worktree's branch, NOT merged into the trunk."""
    write(tree / f"{key}.txt", "z\n")
    git(tree, "add", f"{key}.txt")
    git(tree, "commit", "-q", "-m", f"own {key}")


def preserve_refs(main: Path, prefix: str = "") -> list[str]:
    return [ln for ln in git(main, "for-each-ref", "--format=%(refname)", f"refs/heads/preserve/{prefix}").split()]


def arm_a(mod, base: Path) -> bool:
    main = base_repo(base / "a")
    wt = add_worktree(main, base / "a", "a")
    own_and_merge(main, wt, "a")
    write(wt / "f.txt", "dirty tracked\n")       # modified tracked file
    write(wt / "new.txt", "untracked\n")         # new untracked file
    write(wt / "secret.local", "ignored\n")      # ignored: not dirt, not preserved
    v_rc, v_line = verdict(mod, wt, main)
    rc, out = go_only(mod, wt, main)
    m = PRESERVED_RX.search(out)
    if not m or m.group(1) != "wk-a" or m.group(5) != "2":
        print(f"      detail: no PRESERVED line for wk-a with 2 paths; out={out.strip()[:300]}")
        return False
    ref_short, stamp, sha = m.group(2), m.group(3), m.group(4)
    ref_sha = git(main, "rev-parse", "--verify", f"refs/heads/{ref_short}").strip()
    tracked = git(main, "show", f"{sha}:f.txt").replace("\r", "")
    untracked = git(main, "show", f"{sha}:new.txt").replace("\r", "")
    tree_names = git(main, "ls-tree", "-r", "--name-only", sha).split()
    audit_ok = sha in (main / "org" / "mcp" / "agent-spawn-audit.log").read_text(encoding="ascii")
    print(f"      verdict rc={v_rc} {v_line}")
    print(f"      go rc={rc} ref={ref_short} sha={sha[:12]} stamp={stamp} ref_sha={ref_sha[:12]}")
    return (v_rc == 0 and v_line.startswith("REMOVABLE-AFTER-PRESERVE MERGED") and rc == 0
            and not (wt).exists() and ref_sha == sha and tracked == "dirty tracked\n"
            and untracked == "untracked\n" and "secret.local" not in tree_names and audit_ok)


def arm_b(mod, base: Path) -> bool:
    main = base_repo(base / "b")
    wt = add_worktree(main, base / "b", "b")
    own_and_merge(main, wt, "b")
    v_rc, v_line = verdict(mod, wt, main)
    rc, out = go_only(mod, wt, main)
    return (v_rc == 0 and v_line.startswith("REMOVABLE CLEAN") and rc == 0 and not wt.exists()
            and preserve_refs(main) == [] and "PRESERVED" not in out)


def arm_c(mod, base: Path) -> bool:
    main = base_repo(base / "c")
    wt = add_worktree(main, base / "c", "c")
    own_and_merge(main, wt, "c")
    write(wt / "secret.local", "ignored only\n")  # ignored-only: porcelain empty, so CLEAN
    v_rc, v_line = verdict(mod, wt, main)
    rc, out = go_only(mod, wt, main)
    return (v_rc == 0 and v_line.startswith("REMOVABLE CLEAN") and rc == 0 and not wt.exists()
            and preserve_refs(main) == [] and "PRESERVED" not in out)


def arm_d(mod, base: Path) -> bool:
    main = base_repo(base / "d")
    wt = add_worktree(main, base / "d", "d")   # NEGATIVE CONTROL: branch at its issuance commit, dirty
    write(wt / "dirty.txt", "u\n")
    v_rc, v_line = verdict(mod, wt, main)
    rc, out = go_only(mod, wt, main)
    return (v_rc == 1 and v_line.startswith("NOT-REMOVABLE UNSTARTED") and wt.is_dir()
            and (wt / "dirty.txt").is_file() and preserve_refs(main) == [] and "PRESERVED" not in out)


def arm_e(mod, base: Path) -> bool:
    main = base_repo(base / "e")
    wt = add_worktree(main, base / "e", "e")
    own_only(wt, "e")                            # one own commit NOT in the trunk
    write(wt / "dirty.txt", "u\n")
    v_rc, v_line = verdict(mod, wt, main)
    rc, out = go_only(mod, wt, main)
    return (v_rc == 1 and v_line.startswith("NOT-REMOVABLE HELD") and wt.is_dir()
            and (wt / "dirty.txt").is_file() and preserve_refs(main) == [] and "PRESERVED" not in out)


def arm_f(mod, base: Path) -> bool:
    main = base_repo(base / "f")
    wt = add_worktree(main, base / "f", "f")
    own_and_merge(main, wt, "f")
    write(wt / "f.txt", "dirty before a failed preserve\n")
    # inject the failure: a plain ref named preserve blocks every refs/heads/preserve/<name> (directory/file clash)
    git(main, "update-ref", "refs/heads/preserve", git(main, "rev-parse", "CLOUD").strip())
    v_rc, v_line = verdict(mod, wt, main)
    rc, out = go_only(mod, wt, main)
    kept = (wt / "f.txt").read_bytes() == b"dirty before a failed preserve\n"
    print(f"      go out: {out.strip()[:200]!r}")
    return (v_rc == 0 and v_line.startswith("REMOVABLE-AFTER-PRESERVE") and "PRESERVE-FAILED" in out
            and "PRESERVED " not in out and wt.is_dir() and kept and preserve_refs(main, "wk-f-") == [])


def arm_g(mod, base: Path) -> bool:
    main = base_repo(base / "g")
    dirty = add_worktree(main, base / "g", "ga")
    clean = add_worktree(main, base / "g", "gb")
    own_and_merge(main, dirty, "ga")
    own_and_merge(main, clean, "gb")
    write(dirty / "f.txt", "dirty A\n")
    rc, out = go_only(mod, dirty, main)
    return (rc == 0 and "PRESERVED wk-ga" in out and "SUMMARY --only" in out and not dirty.exists()
            and clean.is_dir() and "wk-gb" not in out)


def arm_h(mod, base: Path) -> bool:
    main = base_repo(base / "h")
    rc1, out1 = go_only(mod, base / "h" / "not-a-worktree", main)
    rc2, out2 = go_only(mod, main, main)  # the main worktree is never a candidate
    return rc1 == 2 and out1.startswith("ERROR") and rc2 == 2 and out2.startswith("ERROR")


def arm_i(mod, base: Path) -> bool:
    """A sparse worktree: the file outside the cone is on no disk and in no dirt; --go preserves it as HEAD content."""
    sp = base / "i"
    main = base_repo(sp)
    write(main / "sub" / "a.txt", "a\n")
    write(main / "other" / "b.txt", "b\n")
    git(main, "add", "sub", "other")
    git(main, "commit", "-q", "-m", "c1")
    wt = add_worktree(main, sp, "i")
    own_only(wt, "sub/i")  # own commit inside the cone (sub/i.txt); merged into the trunk below
    git(main, "merge", "-q", "--no-ff", "--no-edit", "wk-i")
    git(wt, "sparse-checkout", "init", "--cone")
    git(wt, "sparse-checkout", "set", "sub")
    out_of_cone_on_disk = (wt / "other").exists()
    write(wt / "sub" / "a.txt", "dirty a\n")
    write(wt / "sub" / "new.txt", "new\n")
    v_rc, v_line = verdict(mod, wt, main)
    rc, out = go_only(mod, wt, main)
    m = PRESERVED_RX.search(out)
    if not m:
        print(f"      detail: no PRESERVED line; out={out.strip()[:300]}")
        return False
    sha = m.group(4)
    listed = git(main, "ls-tree", "-r", "--name-only", sha).split()
    other_b = git(main, "show", f"{sha}:other/b.txt").replace("\r", "")
    print(f"      precondition other/ on disk={out_of_cone_on_disk}; verdict {v_line}; preserved {m.group(5)} path(s)")
    return (not out_of_cone_on_disk and v_rc == 0 and rc == 0 and not wt.exists() and "other/b.txt" in listed
            and other_b == "b\n" and git(main, "show", f"{sha}:sub/a.txt").replace("\r", "") == "dirty a\n"
            and m.group(5) == "2")


def _clear_readonly(func, path, _exc):
    """git object files are read-only on Windows; clear the bit and retry so the temporary tree is removed."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def main() -> int:
    base = Path(tempfile.mkdtemp(prefix="wtgc_preserve_")).resolve()
    mod = load_tool()
    arms = [
        ("(a) merged, one modified tracked + one untracked + one ignored: REMOVABLE-AFTER-PRESERVE; --go --only "
         "PRESERVED with 2 paths, dir gone, ref at the sha, tracked and untracked content read back, ignored absent",
         arm_a),
        ("(b) clean merged: REMOVABLE CLEAN, removed, no preserve/ branch", arm_b),
        ("(c) ignored-only merged: REMOVABLE CLEAN, removed, no preserve/ branch", arm_c),
        ("(d) NEGATIVE CONTROL: dirty tree at its issuance commit: NOT-REMOVABLE UNSTARTED, kept, no preserve/ branch",
         arm_d),
        ("(e) dirty tree with an own commit NOT in the trunk: NOT-REMOVABLE HELD, kept, no preserve/ branch", arm_e),
        ("(f) preserve failure injected: PRESERVE-FAILED, worktree kept with its dirt, no preserve/ branch", arm_f),
        ("(g) --only A with two removable trees: only A is preserved and removed; B is not named", arm_g),
        ("(h) a path that is not a linked worktree (and the main worktree): rc 2 with ERROR", arm_h),
        ("(i) sparse worktree: out-of-cone file kept as HEAD content in the preserve commit, not recorded as deleted",
         arm_i),
    ]
    results: list[tuple[str, bool]] = []
    try:
        for name, fn in arms:
            try:
                ok = bool(fn(mod, base / fn.__name__))
            except Exception as exc:  # an arm that raises is a failed arm, reported with its cause
                print(f"      exception: {exc}")
                ok = False
            results.append((name, ok))
    finally:
        shutil.rmtree(base, onerror=_clear_readonly)
    for name, ok in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    passed = sum(1 for _, ok in results if ok)
    print(f"WORKTREE-GC-PRESERVE arms={passed}/{len(results)} ok={passed == len(results) == N_ARMS}")
    return 0 if passed == len(results) == N_ARMS else 1


if __name__ == "__main__":
    sys.exit(main())
