#!/usr/bin/env python3
"""test_round19_hygiene.py -- NFRA_CTLPLN round 19, CT-ai-5 (one hygiene batch).

Flags (one or more; each prints one final line `HYGIENE-<ITEM> <detail> ok=<True|False>`):
  --tsx      a staged portal .tsx file makes BOTH commit-gate.sh and the safe-commit.sh risk reflex print
             "not graded: <N> .tsx" (N = 1); a commit with no .tsx prints no such line. The real two scripts run
             from copies of the worktree's sparse set inside a temporary repository.
  --org-ref  a worktree cut by .tools/wk-provision.sh holds org/ref/ (the fixture repository of
             test_wk_sparse_provision.py, provisioned by the real script).
  --cleanup  running .tools/tests/test_round18_batch.py leaves no new r18_batch_* folder in the Temp folder
             (before and after counts; nothing is removed by this test).

Standard library only; temporary repositories and folders only; no AWS, no network, no push.
Usage: python .tools/tests/test_round19_hygiene.py --tsx | --org-ref | --cleanup
"""
from __future__ import annotations

import importlib.util
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .tools/tests
TOOLS = HERE.parent                              # .tools
ROOT = TOOLS.parent                              # the worktree root
sys.path.insert(0, str(TOOLS))
from git_bash_resolver import git_bash  # noqa: E402  (absolute Git Bash; never a bare bash, which is WSL here)

SERIAL = os.environ.get("OPAL_AGENT_SERIAL") or "0.9.0_WK_NFRA_CTLPLN~110"
AUTHOR = f"{SERIAL} <{SERIAL}@opal.agent>"
# the wk-provision.sh base set a worker holds, plus the two root files the commit gate reads
SPARSE_SET = [".tools", "lib", "org/modules/graph", "org/devices", "infra/logic/registry", "org/standards", "org/ref"]
ROOT_FILES = ["comp-constants.config.yaml", ".owned-paths.yaml"]
NOT_GRADED_RX = re.compile(r"not graded: (\d+) \.tsx")


def _clear_readonly(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def _git(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def _run(cwd: Path, argv: list[str]) -> subprocess.CompletedProcess:
    env = {**os.environ, "OPAL_AGENT_SERIAL": SERIAL}
    return subprocess.run(argv, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=280, env=env)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _build_repo(repo: Path) -> None:
    """A temporary repository holding copies of the worktree's sparse set, with one initial commit."""
    repo.mkdir(parents=True)
    _git(repo, "init", "-q", "-b", "main")
    for key, val in (("user.email", "r19-hygiene@invalid"), ("user.name", "r19-hygiene"),
                     ("core.autocrlf", "false")):
        _git(repo, "config", key, val)
    for rel in SPARSE_SET:
        src = ROOT / rel
        if src.is_dir():
            shutil.copytree(str(src), str(repo / rel), ignore=shutil.ignore_patterns("__pycache__"))
    for rel in ROOT_FILES:
        if (ROOT / rel).is_file():
            shutil.copy2(str(ROOT / rel), str(repo / rel))
    _write(repo / "notes.md", "fixture note\n")
    _git(repo, "add", "-A")
    init = _git(repo, "commit", "-q", "-m", "r19 hygiene fixture init")
    if init.returncode != 0:
        raise RuntimeError("fixture commit failed: " + init.stderr.strip()[:300])


def _tsx_hits(text: str) -> tuple[bool, bool]:
    """(gate_line, reflex_line): a "not graded: 1 .tsx" line from commit-gate.sh, and one printed bare by the reflex."""
    gate = reflex = False
    for ln in text.splitlines():
        m = NOT_GRADED_RX.search(ln)
        if not m or m.group(1) != "1":
            continue
        if "[commit-gate]" in ln:
            gate = True
        else:
            reflex = True
    return gate, reflex


def arm_tsx() -> tuple[bool, str]:
    bash = git_bash()
    if not bash:
        return False, "git bash not found (git_bash_resolver returned None)"
    base = Path(tempfile.mkdtemp(prefix="r19_tsx_")).resolve()
    try:
        repo = base / "repo"
        _build_repo(repo)
        # (1) one staged portal .tsx file: the real safe-commit.sh must print the line from BOTH hooks
        _write(repo / "portal" / "src" / "Probe.tsx", "export const probe = 1;\n")
        _git(repo, "add", "--", "portal/src/Probe.tsx")
        msg_a = base / "msg-a.txt"
        _write(msg_a, "r19 hygiene probe: one staged .tsx\n")
        a = _run(repo, [bash, ".tools/safe-commit.sh", "--author", AUTHOR, "-F", msg_a.as_posix(),
                        "--", "portal/src/Probe.tsx"])
        a_out = a.stdout + a.stderr
        a_gate, a_reflex = _tsx_hits(a_out)
        # the commit-gate's own line, run directly against the same staged file
        d_tsx = _run(repo, [bash, ".tools/commit-gate.sh", "portal/src/Probe.tsx"])
        d_tsx_gate = any(_tsx_hits(d_tsx.stdout + d_tsx.stderr))  # run directly, the gate's line is bare
        # (2) a commit with no .tsx: the line must not print, from the hooks or from the direct gate
        _write(repo / "notes.md", "fixture note, edited\n")
        _git(repo, "add", "--", "notes.md")
        msg_b = base / "msg-b.txt"
        _write(msg_b, "r19 hygiene probe: no .tsx\n")
        b = _run(repo, [bash, ".tools/safe-commit.sh", "--author", AUTHOR, "-F", msg_b.as_posix(), "--", "notes.md"])
        b_out = b.stdout + b.stderr
        b_gate, b_reflex = _tsx_hits(b_out)
        d_md = _run(repo, [bash, ".tools/commit-gate.sh", "notes.md"])
        d_md_hit = any(_tsx_hits(d_md.stdout + d_md.stderr))
        ok = (a.returncode == 0 and a_gate and a_reflex and d_tsx_gate
              and b.returncode == 0 and not (b_gate or b_reflex) and not d_md_hit)
        detail = (f"tsx-commit rc={a.returncode} reflex_line={a_reflex} commit-gate_line={a_gate} "
                  f"direct_gate_tsx_line={d_tsx_gate}; no-tsx-commit rc={b.returncode} "
                  f"line_printed={b_gate or b_reflex} direct_gate_no_tsx_line={d_md_hit}")
        return ok, detail
    finally:
        shutil.rmtree(str(base), onerror=_clear_readonly)


def _load_sparse_tests():
    spec = importlib.util.spec_from_file_location("r19_wk_sparse", HERE / "test_wk_sparse_provision.py")
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def arm_org_ref() -> tuple[bool, str]:
    mod = _load_sparse_tests()
    base = Path(tempfile.mkdtemp(prefix="r19_orgref_")).resolve()
    try:
        repo = mod.build_repo(base)
        wt = base / "wt"
        p = mod.bash(repo, "provision", mod.CODE, "org", "--path", str(wt))
        seat = wt / "org" / "ref" / "SEAT_ROLES.json"
        sparse = mod.git(wt, "sparse-checkout", "list").stdout.split()
        ok = p.returncode == 0 and seat.is_file() and "org/ref" in sparse
        return ok, (f"provision rc={p.returncode} org/ref/SEAT_ROLES.json present={seat.is_file()} "
                    f"sparse list has org/ref={'org/ref' in sparse}")
    finally:
        mod.rm_tree(base)


def _r18_folders() -> set[str]:
    return {p.name for p in Path(tempfile.gettempdir()).glob("r18_batch_*")}


def arm_cleanup() -> tuple[bool, str]:
    before = _r18_folders()
    p = subprocess.run([sys.executable, str(HERE / "test_round18_batch.py")], cwd=str(ROOT), capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=280)
    after = _r18_folders()
    new = sorted(after - before)
    summary = [ln for ln in p.stdout.splitlines() if ln.startswith("ROUND18-BATCH")]
    ok = p.returncode == 0 and not new and bool(summary)
    return ok, (f"r18_batch_* folders before={len(before)} after={len(after)} new={len(new)} "
                f"batch rc={p.returncode} summary={summary[-1] if summary else '(none)'}")


ITEMS = {"--tsx": ("TSX", arm_tsx), "--org-ref": ("ORG-REF", arm_org_ref), "--cleanup": ("CLEANUP", arm_cleanup)}


def main(argv: list[str]) -> int:
    if not argv or any(a not in ITEMS for a in argv):
        print("usage: test_round19_hygiene.py --tsx | --org-ref | --cleanup  (one or more)")
        return 2
    all_ok = True
    for flag in argv:
        name, fn = ITEMS[flag]
        try:
            ok, detail = fn()
        except Exception as exc:  # an arm that raises is a failed arm, reported with its cause
            ok, detail = False, f"exception: {exc!r}"
        all_ok = all_ok and ok
        print(f"HYGIENE-{name} {detail} ok={ok}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
