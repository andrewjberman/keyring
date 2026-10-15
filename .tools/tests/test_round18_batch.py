#!/usr/bin/env python3
"""test_round18_batch.py -- CT-ah-1 (round 18 batch): the in-use scan does not read the path the tool was GIVEN as a
use (S9126); a directory junction or symlink in a dirty merged worktree is preserved AS THE LINK, never followed
(W103-S2); safe-commit.sh runs green in a real sparse worktree cut by wk-provision.sh (CTO round-17 rulings 1-3).

Arms:
  (a) an absolute, a relative and a trailing-slash path read the same verdict and none reads SKIP IN USE; --go --only
      removes the tree given by an absolute and by a trailing-slash path
  (b) a worktree whose path is named in a RUNNING process's command line still reads SKIP IN USE
  (c) a directory junction to a folder outside the worktree is preserved as a 120000 entry; the target's files are not
      in the preserve commit and survive the removal
  (d) the same for a symbolic link; SKIPPED with its WinError when the link cannot be created on this box
  (e) --real only: a sparse worktree cut by .tools/wk-provision.sh takes one throwaway commit through
      .tools/safe-commit.sh on a throwaway branch; the worktree and the branch are removed in a finally

Standard library; temporary repositories only; no AWS, no network, no push. The real-process read is NOT stubbed:
arms (a), (b), (c) and (d) run the tool as a child process with a real process table.

Final lines:
  ROUND18-BATCH arms=<k>/<n> skipped=<s> ok=<True|False>           (k = passed, n = arms run; arm e only with --real)
  SAFE-COMMIT-SPARSE exit=<rc> tip_moved=<True|False> folders=<n> green=<True|False>   (--real only, printed last)
"""
from __future__ import annotations

import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .tools/tests
TOOLS = HERE.parent                              # .tools
ROOT = TOOLS.parent                              # the worktree root
TOOL = TOOLS / "worktree_gc.py"
SERIAL = os.environ.get("OPAL_AGENT_SERIAL") or "0.9.0_WK_NFRA_CTLPLN~105"
CODE = "NFRA_CTLPLN"
NUM = "9105"                                     # the throwaway sparse worktree's n: branch wk-NFRA_CTLPLN-9105
# the probe sits in the SERIAL's own deliverables folder: owned-paths-validate permits deliverables/<SERIAL>/** only
PROBE_REL = f"org/missions/D0/NFRA/{CODE}/deliverables/{SERIAL}/r18-sparse-probe/probe.txt"
FREE_FLOOR = 12 * 1024 ** 3                      # arm e needs C: above 12 GB free
PRESERVED_RX = re.compile(r"^PRESERVED (\S+) -> (preserve/\S+) ([0-9a-f]{40}) \((\d+) path\(s\)\)$", re.M)

sys.path.insert(0, str(TOOLS))
from git_bash_resolver import git_bash  # noqa: E402  (absolute Git Bash; never a bare bash, which is WSL here)


def _load_fixtures():
    """Reuse the round-17 fixtures (base_repo, add_worktree, own_and_merge, write, git) by file path."""
    spec = importlib.util.spec_from_file_location("r18_gc_fixtures", HERE / "test_worktree_gc_preserve.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


FX = _load_fixtures()
LINKS: list[Path] = []                           # every junction or symlink this run created, removed first


def tool(cwd: Path, *args: str, timeout: int = 200) -> tuple[int, str]:
    """Run worktree_gc.py as a child process (a real process table, real command lines)."""
    res = subprocess.run([sys.executable, str(TOOL), *args], cwd=str(cwd), capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=timeout)
    return res.returncode, res.stdout + res.stderr


def verdict_line(out: str) -> str:
    lines = [ln for ln in out.splitlines() if ln.startswith(("REMOVABLE", "NOT-REMOVABLE", "ERROR"))]
    return lines[-1] if lines else "(no verdict line)"


def tail(text: str, n: int = 12) -> str:
    return "\n".join(text.strip().splitlines()[-n:])


def arm_a(base: Path, facts: dict) -> tuple[str, str]:
    d = base / "a"
    main = FX.base_repo(d)
    wt = FX.add_worktree(main, d, "a")
    FX.own_and_merge(main, wt, "a")
    forms = {"absolute": str(wt.resolve()), "relative": "wk-a", "trailing-slash": str(wt.resolve()) + "/"}
    seen = {}
    for name, arg in forms.items():  # cwd is the folder holding both trees, so "wk-a" is a true relative path
        rc, out = tool(d, "--repo", str(main), "--check-removable", arg)
        seen[name] = (rc, verdict_line(out), "SKIP IN USE" in out)
    classes = {" ".join(v[1].split()[:2]) for v in seen.values()}  # the class tokens, not own= or the idle text
    verdicts_ok = all(v[0] == 0 and not v[2] for v in seen.values()) and classes == {"REMOVABLE CLEAN"}
    rc_abs, out_abs = tool(d, "--repo", str(main), "--go", "--only", str(wt.resolve()), "--clean-hours", "0")
    go_abs = rc_abs == 0 and "removed=1 failed=0" in out_abs and not wt.exists() and "SKIP IN USE" not in out_abs
    wt2 = FX.add_worktree(main, d, "a2")
    FX.own_and_merge(main, wt2, "a2")
    rc_tr, out_tr = tool(d, "--repo", str(main), "--go", "--only", "wk-a2/", "--clean-hours", "0")
    go_tr = rc_tr == 0 and "removed=1 failed=0" in out_tr and not wt2.exists() and "SKIP IN USE" not in out_tr
    shown = ", ".join(f"{k}={v[1].split(';')[0]} rc={v[0]}" for k, v in seen.items())
    detail = f"verdicts {shown}; go-abs removed={go_abs}; go-trailing-slash removed={go_tr}"
    return ("PASS" if verdicts_ok and go_abs and go_tr else "FAIL"), detail


def arm_b(base: Path, facts: dict) -> tuple[str, str]:
    d = base / "b"
    main = FX.base_repo(d)
    wt = FX.add_worktree(main, d, "b")
    FX.own_and_merge(main, wt, "b")
    sleeper = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)", str(wt.resolve())])
    try:
        time.sleep(0.5)  # the command line exists from process creation; the pause only lets the child start
        rc, out = tool(d, "--repo", str(main), "--check-removable", str(wt.resolve()))
        rc2, out2 = tool(d, "--repo", str(main), "--go", "--only", str(wt.resolve()), "--clean-hours", "0")
    finally:
        sleeper.kill()
        sleeper.wait()
    v = verdict_line(out)
    ok = (rc == 1 and v.startswith("NOT-REMOVABLE SKIP") and "SKIP IN USE" in out and rc2 == 0
          and "removed=0 failed=0" in out2 and wt.is_dir())
    return ("PASS" if ok else "FAIL"), f"verdict={v}; go removed=0: {'removed=0 failed=0' in out2}; kept={wt.is_dir()}"


def _link_arm(base: Path, kind: str) -> tuple[str, str]:
    d = base / kind
    main = FX.base_repo(d)
    wt = FX.add_worktree(main, d, kind)
    FX.own_and_merge(main, wt, kind)
    FX.write(wt / "dirty.txt", "u\n")
    outside = d / "outside"                      # the link's target: a folder OUTSIDE the worktree
    FX.write(outside / "inner.txt", "outside\n")
    link = wt / ("junc" if kind == "junction" else "lnk")
    if kind == "junction":
        if sys.platform != "win32":
            return "SKIP", "junction arm SKIPPED: not Windows"
        mk = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(outside)], capture_output=True, text=True)
        if mk.returncode != 0 or not os.path.isjunction(str(link)):
            return "FAIL", f"mklink /J rc={mk.returncode}: {(mk.stdout + mk.stderr).strip()[:200]}"
    else:
        try:
            os.symlink(str(outside), str(link), target_is_directory=True)
        except OSError as exc:
            code = getattr(exc, "winerror", None)
            if code == 1314:
                return "SKIP", f"symlink arm SKIPPED: WinError {code} (privilege not held on this box): {exc}"
            return "FAIL", f"symlink creation failed: {exc}"
    LINKS.append(link)
    rc, out = tool(d, "--repo", str(main), "--check-removable", str(wt.resolve()))
    v = verdict_line(out)
    rc2, out2 = tool(d, "--repo", str(main), "--go", "--only", str(wt.resolve()), "--clean-hours", "0")
    m = PRESERVED_RX.search(out2)
    if not m:
        return "FAIL", f"no PRESERVED line; verdict={v}; go out={tail(out2, 6)}"
    sha = m.group(3)
    entry = FX.git(main, "ls-tree", sha, link.name).strip()
    names = FX.git(main, "ls-tree", "-r", "--name-only", sha).split()
    under_link = [n for n in names if n.startswith(link.name + "/")]
    intact = (outside / "inner.txt").is_file() and (outside / "inner.txt").read_bytes() == b"outside\n"
    ok = (rc == 0 and v.startswith("REMOVABLE-AFTER-PRESERVE") and rc2 == 0 and m.group(4) == "2"
          and entry.startswith("120000 blob") and not under_link and intact)
    detail = (f"verdict={v.split(';')[0]}; preserved {m.group(4)} path(s); ls-tree: {entry.split()[0] if entry else '-'} "
              f"{entry.split()[1] if entry else '-'} {link.name}; target files in commit={len(under_link)}; "
              f"target intact after removal={intact}")
    return ("PASS" if ok else "FAIL"), detail


def arm_c(base: Path, facts: dict) -> tuple[str, str]:
    return _link_arm(base, "junction")


def arm_d(base: Path, facts: dict) -> tuple[str, str]:
    return _link_arm(base, "symlink")


def _main_worktree() -> Path:
    out = subprocess.run(["git", "worktree", "list", "--porcelain"], cwd=str(ROOT), capture_output=True, text=True,
                         encoding="utf-8", errors="replace").stdout
    first = out.splitlines()[0]
    return Path(first[len("worktree "):])


def arm_e(base: Path, facts: dict) -> tuple[str, str]:
    free = shutil.disk_usage(os.path.splitdrive(str(base))[0] + "\\").free
    facts.update({"exit": None, "tip_moved": False, "folders": 0, "green": False})
    if free < FREE_FLOOR:
        return "SKIP", f"arm e SKIPPED: C: free {free / 1024 ** 3:.1f} GiB is below 12 GiB"
    bash = git_bash()
    if not bash:
        return "FAIL", "git bash not found (git_bash_resolver returned None)"
    main = _main_worktree()
    nested = main / "portal"
    wt = base / "sparse-wt"
    branch = f"wk-{CODE}-{NUM}"
    try:
        pr = subprocess.run([bash, ".tools/wk-provision.sh", "provision", CODE, NUM, "--path", wt.as_posix(),
                             "--node-modules", "none"], cwd=str(ROOT), capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=280)
        if pr.returncode != 0:
            return "FAIL", f"provision rc={pr.returncode}: {tail(pr.stdout + pr.stderr)}"
        folders = [ln for ln in FX.git(wt, "sparse-checkout", "list").splitlines() if ln.strip()]
        facts["folders"] = len(folders)
        FX.write(wt / PROBE_REL, "round-18 sparse probe (throwaway branch)\n")
        msg = base / "probe-msg.txt"
        FX.write(msg, "r18 sparse probe: throwaway commit on a throwaway branch, removed by the test\n")
        tip0 = FX.git(wt, "rev-parse", f"refs/heads/{branch}").strip()
        env = {**os.environ, "OPAL_AGENT_SERIAL": SERIAL}
        sc = subprocess.run([bash, ".tools/safe-commit.sh", "--author", f"{SERIAL} <{SERIAL}@opal.agent>",
                             "-F", msg.as_posix(), "--", PROBE_REL], cwd=str(wt), env=env, capture_output=True,
                            text=True, encoding="utf-8", errors="replace", timeout=280)
        tip1 = FX.git(wt, "rev-parse", f"refs/heads/{branch}").strip()
        facts["exit"] = sc.returncode
        facts["tip_moved"] = tip1 != tip0 and bool(tip1)
        facts["green"] = sc.returncode == 0 and facts["tip_moved"]
        gate = [ln for ln in (sc.stdout + sc.stderr).splitlines() if "[naming-gate]" in ln or "WARN:" in ln]
        print(f"      safe-commit gate lines: {len(gate)}")
        for ln in gate[:6]:
            print(f"        {ln[:200]}")
        return ("PASS" if facts["green"] else "FAIL"), (f"safe-commit rc={sc.returncode} tip_moved={facts['tip_moved']} "
                                                       f"folders={len(folders)}; tail: {tail(sc.stdout + sc.stderr, 3)}")
    finally:
        _remove_sparse(main, nested, wt, branch)


def _remove_sparse(main: Path, nested: Path, wt: Path, branch: str) -> None:
    """Remove the throwaway sparse worktree, its nested portal worktree, and both throwaway branches (finally)."""
    portal_wt = wt / "portal"
    portal_branch = f"{branch}-portal"
    if portal_wt.exists() and nested.is_dir():
        subprocess.run(["git", "-C", str(nested), "worktree", "remove", "--force", str(portal_wt)],
                       capture_output=True, text=True)
    if nested.is_dir():
        subprocess.run(["git", "-C", str(nested), "branch", "-D", portal_branch], capture_output=True, text=True)
    if wt.exists():
        subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(wt)],
                       capture_output=True, text=True)
    if wt.exists():  # the worktree still on disk after git's removal: the temporary tree is ours, no links in it
        shutil.rmtree(wt, onerror=FX._clear_readonly)
    # no `git worktree prune` here: a prune is repository-wide and clears every unrelated prunable entry (the
    # round-17 cmd_remove comment forbids it); git worktree remove above already drops this worktree's own entry
    subprocess.run(["git", "-C", str(ROOT), "branch", "-D", branch], capture_output=True, text=True)


def _is_link_path(p: Path) -> bool:
    isj = getattr(os.path, "isjunction", None)
    return os.path.islink(str(p)) or bool(isj is not None and isj(str(p)))


def _drop_links() -> None:
    """Unlink every junction or symlink this run made. os.rmdir on a junction removes the link, never its target."""
    for link in LINKS:
        if os.path.lexists(str(link)) and _is_link_path(link):
            os.rmdir(str(link))


def main() -> int:
    extra = [a for a in sys.argv[1:] if a != "--real"]
    if extra:
        print(f"ERROR: unknown argument(s): {extra}")
        return 2
    real = "--real" in sys.argv[1:]
    base = Path(tempfile.mkdtemp(prefix="r18_batch_")).resolve()
    arms = [("a", "absolute, relative and trailing-slash paths; no SKIP IN USE", arm_a),
            ("b", "a worktree named by a running process still reads SKIP IN USE", arm_b),
            ("c", "junction preserved as a 120000 link; target not in commit; target intact", arm_c),
            ("d", "symlink preserved as a 120000 link (SKIPPED with WinError 1314 where it cannot be created)", arm_d)]
    if real:
        arms.append(("e", "--real: safe-commit.sh green in a real sparse worktree cut by wk-provision.sh", arm_e))
    facts: dict = {}
    results: list[tuple[str, str, str]] = []
    try:
        for name, title, fn in arms:
            try:
                status, detail = fn(base / name, facts)
            except Exception as exc:  # an arm that raises is a failed arm, reported with its cause
                status, detail = "FAIL", f"exception: {exc!r}"
            print(f"  {status:<4}  ({name}) {title}")
            print(f"        {detail}")
            results.append((name, title, status))
    finally:
        try:
            _drop_links()
        finally:
            try:  # the git object files are read-only on Windows: _clear_readonly clears the bit and retries
                shutil.rmtree(base, onerror=FX._clear_readonly)
            except OSError as exc:
                print(f"WARN: temporary fixture folder not fully removed: {base} ({exc})")
    n = len(results)
    passed = sum(1 for r in results if r[2] == "PASS")
    skipped = sum(1 for r in results if r[2] == "SKIP")
    ok = n > 0 and passed + skipped == n
    print(f"ROUND18-BATCH arms={passed}/{n} skipped={skipped} ok={ok}")
    if real:
        green = bool(facts.get("green"))
        print(f"SAFE-COMMIT-SPARSE exit={facts.get('exit')} tip_moved={bool(facts.get('tip_moved'))} "
              f"folders={facts.get('folders', 0)} green={green}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
