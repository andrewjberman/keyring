#!/usr/bin/env python3
"""worktree_gc.py -- the box's worktree garbage collector: remove what is safe, HOLD what has unlanded work.

Andrew-direct 2026-10-08 (records org/tier1_exec/4.0.0_SA_CRO/deliverables/
ANDREW_DIRECT_20261008_173xZ_GC_FOUR_CALLS_ANSWERED_WORKTREE_OWNER_MUST_ASSESS.md):
  "I agree with 24 hours but we dont want to lose uncommitted work ... The agent has to be online to assess"
  and "48 Hours is better".

THE RULE (one class per linked worktree):
  SKIP      the main worktree; a worktree locked with `git worktree lock` (the fence: never touched);
            a `drain-*` worktree; a CLEAN or MERGED worktree whose path a running process command line or a
            scheduled task's Execute / Arguments / WorkingDirectory names (IN USE; row AMGT_HARVST-Z-S111: git
            idleness cannot see a scheduled runner). If that read fails, every removal candidate is SKIP.
  ACTIVE    git activity (commit, checkout, or an edited file) within --clean-hours (24 h).
  CLEAN     HEAD is merged into the trunk and `git status --porcelain` is empty (dirt = porcelain lines only;
            gitignored paths are not dirt, CTO round-16 ruling 2), idle >= 24 h  ->  removed by --go
            (`git worktree remove`). Every committed byte is already in the trunk or a box branch.
  MERGED    HEAD is merged, but the porcelain lists modified or untracked files, idle >= 24 h  ->  --go FIRST
            preserves those files on a new branch preserve/<branch>-<stamp> (the sha is printed), THEN removes the
            worktree with `git worktree remove --force`. A failed preserve removes nothing (CTO round-16 ruling 1).
            Andrew-direct 2026-10-08 ~23:0xZ, VERBATIM: "Force-removing merged worktrees is mandatory, if that is
            already merged it should be gotten rid of" (record ANDREW_DIRECT_20261008_230xZ_SITEZ_AND_DELL2_OPEN_
            CALLS_ANSWERED.md @86d85ab4a5, 1.0.0_SA_CTO; relayed by 0.0.0_AB_MSTR msg 107453). A LOCKED worktree
            stays SKIP and an ACTIVE one stays ACTIVE: the force reaches only the merged and idle.
  HELD      unmerged commits (with or without uncommitted files), idle >= 24 h  ->  NEVER touched. It has an OWNER (the serial that authored its newest unlanded commit;
            else a serial named in its branch or path; else the box's MSTR). The owner is told at its next
            registration (--hook-notice, wired on register_agent) and assesses it while online.
  ESCALATE  HELD, idle >= --held-hours (48 h), and the owner is not live  ->  still never touched; the box's MSTR
            brings the owner online to assess it (/mstr-spawn with that one task), or assesses it itself if the seat
            is retired.
  PRUNABLE  the directory is gone; --go runs `git worktree prune` (admin data only).
  UNSTARTED a worktree whose branch carries NO commit of its own (own=0: HEAD is still the branch's creation point)
            or whose own count cannot be read (own=unknown: detached HEAD, a missing or empty branch reflog, any git
            error). Unstarted or in progress, never merged: --go NEVER removes it, clean or dirty (CTO round-15 ruling 1,
            CT-af-1). own = commits reachable from HEAD and not from the creation point, which is the new-value of the
            OLDEST entry of `git reflog show <branch>` (`git worktree add -b` writes `branch: Created from <sha>`).
            CLEAN and MERGED also require own >= 1. ACTIVE is decided first, so a recently active worktree reads ACTIVE.

Every REMOVED worktree, and every first sighting of a HELD or ESCALATE worktree, is one WORKTREE-GC line in
org/mcp/agent-spawn-audit.log. State lives in <git-common-dir>/opal-worktree-gc.json (per box, never committed).

Usage:
  python .tools/worktree_gc.py                 # dry run: the table, nothing changed
  python .tools/worktree_gc.py --go            # remove CLEAN, preserve then force-remove MERGED, prune PRUNABLE, log, write state
  python .tools/worktree_gc.py --go --only <path>   # the same for ONE linked worktree; every other one is untouched
                                                   # (exit 2 when <path> is not a linked worktree); no prune, no state write
  python .tools/worktree_gc.py --selftest      # temp repo: merged+dirty -> removed, unmerged+dirty -> kept
  python .tools/worktree_gc.py --check-removable <path>   # the drain's test on ONE worktree, idle window ignored;
                                                          # one line REMOVABLE / REMOVABLE-AFTER-PRESERVE / NOT-REMOVABLE;
                                                          # removes and preserves nothing
  python .tools/worktree_gc.py --held-for S    # held/escalated worktrees owned by serial S (reads state; fast)
  python .tools/worktree_gc.py --hook-notice   # PostToolUse(register_agent) hook: stdin JSON -> notice for that serial
"""
from __future__ import annotations

import argparse
import ctypes
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

SERIAL_RX = re.compile(r"\b(\d+\.\d+\.\d+_[A-Z]{2}_[A-Za-z0-9]+(?:~[A-Za-z0-9]+)?)\b")
CACHE_RX = re.compile(r"(^|/)(__pycache__|node_modules|\.pytest_cache|\.ruff_cache|\.mypy_cache|\.terraform)(/|$)|\.pyc$")


def git(args: list[str], cwd: str | None = None, check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", check=check)


_REPO: str | None = None


def ws_root() -> Path:
    """The box's MAIN worktree (liveness.json, the audit log and the state live there), from any linked worktree."""
    base = _REPO or str(Path(__file__).resolve().parent.parent)
    out = subprocess.run(["git", "worktree", "list", "--porcelain"], cwd=base, capture_output=True, text=True,
                         encoding="utf-8", errors="replace").stdout
    for ln in out.splitlines():
        if ln.startswith("worktree "):
            return Path(ln[len("worktree "):])
    return Path(base)


def common_dir() -> Path:
    out = git(["rev-parse", "--git-common-dir"], cwd=str(ws_root())).stdout.strip()
    p = Path(out)
    return p if p.is_absolute() else (ws_root() / p).resolve()


def state_path() -> Path:
    return common_dir() / "opal-worktree-gc.json"


def audit(line: str) -> None:
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    text = f"{ts}  WORKTREE-GC  {line}".encode("ascii", "replace").decode("ascii")
    try:
        with open(ws_root() / "org" / "mcp" / "agent-spawn-audit.log", "a", encoding="ascii") as fh:
            fh.write(text + "\n")
    except OSError as exc:
        print(f"WARN: audit append failed: {exc}", file=sys.stderr)


def pid_alive(pid: int) -> bool:
    """True only for a process that exists AND has not exited (STILL_ACTIVE)."""
    if pid <= 0:
        return False
    if sys.platform != "win32":
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False
    k32 = ctypes.windll.kernel32
    h = k32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
    if not h:
        return False
    try:
        code = ctypes.c_ulong(0)
        if not k32.GetExitCodeProcess(h, ctypes.byref(code)):
            return True  # cannot read: never call a seat dead on a probe that cannot see it
        return code.value == 259  # STILL_ACTIVE
    finally:
        k32.CloseHandle(h)


def live_serials() -> set[str]:
    try:
        data = json.loads((ws_root() / "org" / "mcp" / "liveness.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    return {s for s, v in data.items() if isinstance(v, dict) and pid_alive(int(v.get("pid") or 0))}


def worktrees() -> list[dict]:
    out = git(["worktree", "list", "--porcelain"], cwd=str(ws_root())).stdout
    rows, cur = [], {}
    for ln in out.splitlines() + [""]:
        if not ln.strip():
            if cur:
                rows.append(cur)
            cur = {}
            continue
        key, _, val = ln.partition(" ")
        cur[key] = val if val else True
    return rows


SHA_RX = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")


def creation_point(branch: str, cwd: str) -> str | None:
    """The commit a branch was created at: the new-value of the OLDEST entry of its reflog. None when the branch is
    detached, its reflog is missing or empty, or git fails (fail closed). Forms this reads: `worktree add -b`,
    `git branch`, `checkout -b`, `worktree add <path> <existing-branch>`. An orphan branch reads its first commit
    as the creation point (own undercounts by one: safe, it can only refuse). An expired reflog reads a later
    entry (undercount: safe)."""
    if not branch or branch == "(detached)":
        return None
    res = git(["reflog", "show", "--format=%H", f"refs/heads/{branch}"], cwd=cwd)
    if res.returncode != 0:
        return None
    shas = [ln.strip() for ln in res.stdout.splitlines() if ln.strip()]
    if not shas or not SHA_RX.fullmatch(shas[-1]):
        return None
    return shas[-1]


def own_commits(path: str, branch: str, head: str) -> int | None:
    """Commits reachable from HEAD and not from the branch's creation point; None = unknown (fail closed)."""
    start = creation_point(branch, path)
    if start is None or not SHA_RX.fullmatch(head):
        return None
    res = git(["rev-list", "--count", f"{start}..{head}"], cwd=path)
    if res.returncode != 0 or not res.stdout.strip().isdigit():
        return None
    return int(res.stdout.strip())


def _gx(args: list[str], cwd: str, env: dict | None = None, stdin: str | None = None) -> subprocess.CompletedProcess:
    """git with an explicit environment and optional stdin; a git error is a return code, never an exception."""
    return subprocess.run(["git", *args], cwd=cwd, env=env, input=stdin, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def _is_link(p: str) -> bool:
    """A symbolic link or a directory junction (os.path.isjunction is Python 3.12+; absent => False)."""
    isj = getattr(os.path, "isjunction", None)
    return os.path.islink(p) or bool(isj is not None and isj(p))


def link_entries(path: str) -> tuple[list[tuple[str, str]] | None, str]:
    """Directory junctions and symbolic links in a worktree that git would walk into, as (worktree-relative path,
    link target); (None, reason) when git fails. Found through the untracked listing: git lists a junction's target
    files under the junction's path, so each listed path's components are tested, outermost first (only the
    OUTERMOST link on a path is kept). A link whose target holds no untracked, non-ignored file is not listed and is
    not recorded (the one known limit). The target is read from the link itself and never followed."""
    res = _gx(["ls-files", "-o", "--exclude-standard", "-z"], path)
    if res.returncode != 0:
        return None, f"ls-files -o failed: {res.stderr.strip()[:160]}"
    found: dict[str, str] = {}
    for rel in res.stdout.split("\0"):
        if not rel:
            continue
        comps = rel.split("/")
        for i in range(1, len(comps) + 1):
            d = "/".join(comps[:i])
            if d in found:
                break
            full = os.path.join(path, *comps[:i])
            if _is_link(full):
                try:
                    target = os.readlink(full)
                except OSError as exc:
                    return None, f"readlink failed for {d}: {exc}"
                found[d] = target[4:] if target.startswith("\\\\?\\") else target
                break
    return sorted(found.items()), ""


def preserve_dirt(path: str, branch: str, meta: dict | None = None) -> tuple[bool, str]:
    """Commit the worktree's porcelain dirt to a NEW branch preserve/<branch>-<stamp>; return (True, commit sha).

    Plumbing on a TEMPORARY index (GIT_INDEX_FILE): no hook runs, the worktree's own index is not written, and
    .gitignore is honoured, so ignored paths are not preserved. A sparse checkout's skip-worktree entries are copied
    into the temporary index first, so paths outside the cone are recorded as unchanged, never as deleted. FAILS
    CLOSED: any git error returns (False, reason) and the caller must not remove the worktree. meta, when given,
    receives ref (short name), n (paths preserved) and stamp.
    """
    meta = meta if meta is not None else {}
    if not branch or branch == "(detached)":
        return False, "detached HEAD: no branch to preserve under"
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    tmp = tempfile.mkdtemp(prefix="wtgc_preserve_")
    try:
        env = {**os.environ, "GIT_INDEX_FILE": os.path.join(tmp, "index")}
        head = _gx(["rev-parse", "--verify", "-q", "HEAD"], path)
        head_sha = head.stdout.strip()
        if head.returncode != 0 or not SHA_RX.fullmatch(head_sha):
            return False, "HEAD does not resolve"
        real = _gx(["ls-files", "-t", "-z"], path)  # read-only on the worktree's own index
        if real.returncode != 0:
            return False, f"ls-files failed: {real.stderr.strip()[:160]}"
        sparse = [e[2:] for e in real.stdout.split("\0") if e.startswith("S ")]
        r = _gx(["read-tree", "HEAD"], path, env)
        if r.returncode != 0:
            return False, f"read-tree failed: {r.stderr.strip()[:160]}"
        if sparse:
            r = _gx(["update-index", "--skip-worktree", "-z", "--stdin"], path, env, "".join(p + "\0" for p in sparse))
            if r.returncode != 0:
                return False, f"update-index --skip-worktree failed: {r.stderr.strip()[:160]}"
        # W103-S2 (CTO round-17 ruling 3): a directory junction or symlink is preserved AS THE LINK, never followed.
        # Each link becomes a 120000 entry (its target path as the blob), and `add -A` excludes the link's path so
        # git does not walk into the target and record the target's files under the link.
        links, why = link_entries(path)
        if links is None:
            return False, why
        for rel, target in links:
            h = _gx(["hash-object", "-w", "--stdin"], path, env, target)
            link_sha = h.stdout.strip()
            if h.returncode != 0 or not SHA_RX.fullmatch(link_sha):
                return False, f"hash-object failed for link {rel}: {h.stderr.strip()[:160]}"
            u = _gx(["update-index", "--add", "--cacheinfo", f"120000,{link_sha},{rel}"], path, env)
            if u.returncode != 0:
                return False, f"update-index failed for link {rel}: {u.stderr.strip()[:160]}"
        r = _gx(["add", "-A", "--", "."] + [f":(exclude){rel}" for rel, _ in links], path, env)
        if r.returncode != 0:
            return False, f"add -A failed: {r.stderr.strip()[:160]}"
        tree = _gx(["write-tree"], path, env)
        tree_sha = tree.stdout.strip()
        if tree.returncode != 0 or not SHA_RX.fullmatch(tree_sha):
            return False, f"write-tree failed: {tree.stderr.strip()[:160]}"
        names = _gx(["diff", "--cached", "--name-only", "-z", "HEAD"], path, env)
        if names.returncode != 0:
            return False, f"diff --cached failed: {names.stderr.strip()[:160]}"
        changed = [x for x in names.stdout.split("\0") if x]
        if not changed:
            return False, "no path differs from HEAD; no preserve branch written"
        msg = (f"preserve: worktree dirt of {branch} at {stamp}\n\nsource branch: {branch}\npath: {path}\n"
               f"stamp: {stamp}\npreserved paths: {len(changed)}\n")
        ct = _gx(["-c", "user.name=worktree_gc", "-c", "user.email=worktree_gc@opal.agent",
                  "-c", "commit.gpgsign=false", "commit-tree", tree_sha, "-p", head_sha, "-m", msg], path)
        commit = ct.stdout.strip()
        if ct.returncode != 0 or not SHA_RX.fullmatch(commit):
            return False, f"commit-tree failed: {ct.stderr.strip()[:160]}"
        ref = f"refs/heads/preserve/{branch}-{stamp}"
        k = 1
        while True:
            cand = ref if k == 1 else f"{ref}-{k}"  # a name already taken gets a numeric suffix
            if _gx(["check-ref-format", cand], path).returncode != 0:
                return False, f"invalid preserve ref name: {cand}"
            if _gx(["rev-parse", "--verify", "-q", cand], path).returncode != 0:
                break
            k += 1
            if k > 99:
                return False, "preserve ref names exhausted"
        u = _gx(["update-ref", cand, commit, "0" * len(commit)], path)  # old value zero: never overwrites
        if u.returncode != 0:
            return False, f"update-ref {cand} failed: {u.stderr.strip()[:160]}"
        meta.update({"ref": cand[len("refs/heads/"):], "n": len(changed), "stamp": stamp})
        return True, commit
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _same_path(wt: dict, want: Path) -> bool:
    try:
        return Path(str(wt.get("worktree", ""))).resolve() == want
    except OSError:
        return False


def classify(wt: dict, trunk: str, clean_h: float, held_h: float, live: set[str], now: float) -> dict:
    path = wt.get("worktree", "")
    branch = str(wt.get("branch", "")).replace("refs/heads/", "") or "(detached)"
    row = {"path": path, "branch": branch, "class": "", "reason": "", "owner": "", "idle_h": None,
           "dirty": 0, "unmerged": 0, "merged": False, "own": None}
    if wt.get("locked") is not None and "locked" in wt:
        row.update({"class": "SKIP", "reason": "locked (git worktree lock)"})
        return row
    if Path(path).name.startswith("drain-"):
        row.update({"class": "SKIP", "reason": "drain-* worktree"})
        return row
    if "prunable" in wt or not Path(path).is_dir():
        row.update({"class": "PRUNABLE", "reason": "directory missing"})
        return row
    head = str(wt.get("HEAD", ""))
    # idle: newest of HEAD commit time and this worktree's newest reflog entry (checkout/commit/reset)
    t_commit = git(["log", "-1", "--format=%ct", "HEAD"], cwd=path).stdout.strip()
    t_reflog = git(["reflog", "-1", "--date=unix", "--format=%gd", "HEAD"], cwd=path).stdout.strip()
    stamps = [int(t_commit)] if t_commit.isdigit() else []
    m = re.search(r"\{(\d+)\}", t_reflog)
    if m:
        stamps.append(int(m.group(1)))
    last = max(stamps) if stamps else 0
    if now - last < clean_h * 3600:
        row.update({"class": "ACTIVE", "reason": "git activity within the clean window",
                    "idle_h": round((now - last) / 3600, 1)})
        return row
    # stale by git activity: now read the working tree. DIRT = the porcelain lines only (tracked changes and untracked
    # non-ignored files); gitignored paths are not dirt (CTO round-16 ruling 2, W100-S2). A failed read is no answer.
    st_res = git(["status", "--porcelain", "--untracked-files=all"], cwd=path)
    if st_res.returncode != 0:
        row.update({"class": "SKIP", "reason": f"git status failed; not removed: {st_res.stderr.strip()[:160]}"})
        return row
    dirty = [ln[3:] for ln in st_res.stdout.splitlines() if ln.strip()]
    for f in dirty:  # an edited file counts as activity
        try:
            last = max(last, int((Path(path) / f.strip('"')).stat().st_mtime))
        except OSError:
            pass
    idle_raw = (now - last) / 3600
    idle_h = round(idle_raw, 2)
    # MERGED = HEAD is contained in the trunk (local or origin) OR in any box branch (local or origin) -- per-box
    # branches, CTO placement B5 (PER_BOX_BRANCH_BUILD_PLACEMENT_20261008.md): a commit already on a box branch is
    # safe in the repository, so its worktree holds nothing unique. One for-each-ref call answers all refs at once.
    holders = git(["for-each-ref", "--format=%(refname:short)", "--contains", head,
                   f"refs/heads/{trunk}", f"refs/remotes/origin/{trunk}", "refs/heads/box/", "refs/remotes/origin/box/"],
                  cwd=path).stdout.split()
    merged = bool(holders)
    # Count against origin's trunk: on a box branch nobody advances the local trunk ref, so it can sit thousands of
    # commits behind and inflate the unmerged count and the owner read (dell2 2.0.0_SA_COO~Y2, msg 6850).
    base = f"origin/{trunk}"
    unmerged = 0 if merged else int((git(["rev-list", "--count", f"{base}..{head}"], cwd=path).stdout.strip() or "0"))
    row.update({"idle_h": idle_h, "dirty": len(dirty), "unmerged": unmerged, "merged": merged})
    if idle_raw < clean_h:
        row.update({"class": "ACTIVE", "reason": "a modified file was edited within the clean window"})
        return row
    own = own_commits(path, branch, head)
    row["own"] = own
    if own is None or own < 1:  # CT-af-1: no commit of its own is not merged, whatever the trunk says
        row.update({"class": "UNSTARTED", "reason": f"own={'unknown' if own is None else '0'}: no commit of its own "
                    f"(unstarted or in progress); never removed; idle {idle_h} h"})
        return row
    if merged and not dirty:
        row.update({"class": "CLEAN", "reason": f"merged into {holders[0]}, porcelain empty, idle {idle_h} h"})
        return row
    if merged:
        row.update({"class": "MERGED", "reason": f"merged into {holders[0]}; {len(dirty)} uncommitted/untracked "
                    f"path(s) preserved to a preserve/ branch before the --force removal; idle {idle_h} h"})
        return row
    # HELD: find the owner
    owner = ""
    if not merged:
        author = git(["log", "-1", "--format=%an", f"{base}..{head}"], cwd=path).stdout.strip()
        mm = SERIAL_RX.search(author)
        owner = mm.group(1) if mm else ""
    if not owner:
        mm = SERIAL_RX.search(branch) or SERIAL_RX.search(path)
        owner = mm.group(1) if mm else ""
    why = []
    if dirty:
        why.append(f"{len(dirty)} uncommitted/untracked")
    if unmerged:
        why.append(f"{unmerged} unmerged commit(s)")
    row["owner"] = owner or "box MSTR (owner unknown)"
    owner_live = bool(owner) and owner in live
    if idle_raw >= held_h and not owner_live:
        row.update({"class": "ESCALATE", "reason": "; ".join(why) + f"; idle {idle_h} h, owner not live"})
    else:
        row.update({"class": "HELD", "reason": "; ".join(why) + f"; idle {idle_h} h"})
    return row


_IN_USE_PS = (
    "$ErrorActionPreference='Stop';"
    "$procs=@(Get-CimInstance Win32_Process | ForEach-Object { [pscustomobject]@{pid=[int]$_.ProcessId;"
    "ppid=[int]$_.ParentProcessId;cmd=[string]$_.CommandLine} });"
    "$tasks=@(Get-ScheduledTask | ForEach-Object { $_.Actions } | ForEach-Object { $_.Execute; $_.Arguments; "
    "$_.WorkingDirectory } | ForEach-Object { [string]$_ });"
    "[pscustomobject]@{procs=$procs;tasks=$tasks} | ConvertTo-Json -Compress -Depth 4"
)
SELF_CHAIN_DEPTH = 3  # the tool's own pid, then up to three ancestors (the shell and any wrapper such as timeout)


def _self_chain(procs: list[tuple[int, int, str]]) -> set[int]:
    """The tool's own pid and up to SELF_CHAIN_DEPTH ancestors. Their command lines name the path the tool was GIVEN
    (the shell or wrapper that ran it), which is a call, not a use: they never make a worktree IN USE (S9126)."""
    parent = {pid: ppid for pid, ppid, _ in procs}
    chain = {os.getpid()}
    cur = os.getpid()
    for _ in range(SELF_CHAIN_DEPTH):
        cur = parent.get(cur, 0)
        if cur <= 0 or cur in chain:
            break
        chain.add(cur)
    return chain


def in_use_text() -> str | None:
    """Every running process command line and scheduled-task action, lowercased with forward slashes, EXCEPT the
    tool's own process and its ancestor chain (_self_chain). None when the read failed: the caller then removes
    nothing."""
    tasks: list[str] = []
    if sys.platform != "win32":
        res = subprocess.run(["ps", "-eo", "pid=,ppid=,args="], capture_output=True, text=True, errors="replace")
        if res.returncode != 0 or not res.stdout.strip():
            return None
        procs: list[tuple[int, int, str]] = []
        for ln in res.stdout.splitlines():
            parts = ln.strip().split(None, 2)
            if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
                procs.append((int(parts[0]), int(parts[1]), parts[2] if len(parts) > 2 else ""))
    else:
        res = subprocess.run(["powershell", "-NoProfile", "-Command", _IN_USE_PS], capture_output=True, text=True,
                             encoding="utf-8", errors="replace")
        if res.returncode != 0 or not res.stdout.strip():
            return None
        try:
            data = json.loads(res.stdout)
            rows = data.get("procs") or []
            rows = [rows] if isinstance(rows, dict) else rows
            procs = [(int(p["pid"]), int(p["ppid"]), str(p.get("cmd") or "")) for p in rows]
            tasks = [str(t) for t in (data.get("tasks") or []) if t]
        except (ValueError, KeyError, TypeError, AttributeError):
            return None
    if not procs:
        return None
    skip = _self_chain(procs)
    lines = [cmd for pid, _, cmd in procs if pid not in skip and cmd] + tasks
    return "\n".join(lines).replace("\\", "/").lower()


def path_in_use(path: str, text: str) -> bool:
    """True when the worktree path, in Windows, MSYS or cygwin spelling, appears whole in text.
    An 8.3 spelling (C:/Users/ANDREW~1/...) is not matched."""
    p = path.replace("\\", "/").rstrip("/").lower()
    forms = {p}
    m = re.match(r"^([a-z]):/(.*)$", p)
    if m:
        forms |= {f"/{m.group(1)}/{m.group(2)}", f"/cygdrive/{m.group(1)}/{m.group(2)}"}
    return any(re.search(re.escape(f) + r"(?=$|[/\"'\s;,])", text, re.M) for f in forms)


def load_state() -> dict:
    try:
        return json.loads(state_path().read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def run(args: argparse.Namespace) -> int:
    now = time.time()
    live = live_serials()
    wts = worktrees()[1:]
    if args.only:  # ONE linked worktree: every other one is neither classified nor touched
        want = Path(args.only).resolve()
        wts = [w for w in wts if _same_path(w, want)]
        if not wts:
            print(f"ERROR: --only path is not a linked worktree of this repository: {args.only}")
            return 2
    rows = [classify(w, args.trunk, args.clean_hours, args.held_hours, live, now) for w in wts]
    if any(r["class"] in ("CLEAN", "MERGED") for r in rows):
        text = in_use_text()
        for r in rows:
            if r["class"] not in ("CLEAN", "MERGED"):
                continue
            if text is None:
                r.update({"class": "SKIP", "reason": "in-use read failed (process/scheduled-task list); not removed"})
            elif path_in_use(r["path"], text):
                r.update({"class": "SKIP", "reason": "IN USE: a running process or scheduled task names this path"})
    prev = load_state().get("held", {})
    held_out = {}
    print(f"=== worktree_gc {'GO' if args.go else 'DRY-RUN'}{' --only' if args.only else ''} -- trunk {args.trunk}, "
          f"clean {args.clean_hours} h, held {args.held_hours} h, {len(rows)} linked worktree(s), "
          f"{len(live)} live serial(s) ===")
    for r in sorted(rows, key=lambda x: (x["class"], x["path"])):
        print(f"  {r['class']:<9} {r['path']}  [{r['branch']}]  {r['reason']}"
              + (f"  owner={r['owner']}" if r["owner"] else ""))
        if r["class"] in ("HELD", "ESCALATE"):
            held_out[r["path"]] = r
            old = prev.get(r["path"], {})
            if args.go and old.get("class") != r["class"]:  # dry runs never write the record
                audit(f"{r['class']}  path={r['path']}  branch={r['branch']}  owner={r['owner']}  reason={r['reason']}")
    removed = failed = 0
    if args.go:
        for r in rows:
            if r["class"] not in ("CLEAN", "MERGED"):
                continue
            preserved = ""
            if r["class"] == "MERGED":  # the dirt is preserved FIRST; a failed preserve removes nothing
                meta: dict = {}
                ok, val = preserve_dirt(r["path"], r["branch"], meta)
                if not ok:
                    failed += 1
                    print(f"PRESERVE-FAILED {val}  path={r['path']}")
                    audit(f"PRESERVE-FAILED  path={r['path']}  branch={r['branch']}  reason={val}")
                    continue
                print(f"PRESERVED {r['branch']} -> {meta['ref']} {val} ({meta['n']} path(s))")
                preserved = f"  preserved={meta['ref']}@{val}"
            force = ["--force"] if r["class"] == "MERGED" else []
            res = git(["worktree", "remove", *force, r["path"]], cwd=str(ws_root()))
            if res.returncode == 0:
                removed += 1
                audit(f"REMOVED{'-FORCE' if force else ''}  path={r['path']}  branch={r['branch']}"
                      f"{preserved}  reason={r['reason']}")
            else:
                failed += 1
                print(f"  WARN: git worktree remove refused {r['path']}: {res.stderr.strip()[:200]}")
        if args.only:
            print("NOTE: --only: no prune and no state write (both are repository-wide)")
        else:
            if any(r["class"] == "PRUNABLE" for r in rows):
                git(["worktree", "prune"], cwd=str(ws_root()))
            try:
                state_path().write_text(json.dumps({"written": now, "held": held_out}, indent=1), encoding="utf-8")
            except OSError as exc:
                print(f"WARN: state write failed: {exc}", file=sys.stderr)
    counts = {c: sum(1 for r in rows if r["class"] == c)
              for c in ("CLEAN", "MERGED", "HELD", "ESCALATE", "ACTIVE", "SKIP", "PRUNABLE", "UNSTARTED")}
    print(("SUMMARY --only: " if args.only else "SUMMARY: ") + "  ".join(f"{k}={v}" for k, v in counts.items())
          + (f"  removed={removed} failed={failed}" if args.go else "  (dry run: nothing removed)"))
    return 0


def check_removable(args: argparse.Namespace) -> int:
    """--check-removable PATH: the drain's test on ONE linked worktree, the idle window ignored (the drain calls it the
    moment a merge lands). Prints one line and removes nothing. 0 = REMOVABLE or REMOVABLE-AFTER-PRESERVE, 1 =
    NOT-REMOVABLE, 2 = not a linked worktree of this repository. REMOVABLE only when own >= 1, HEAD is contained in
    the trunk or a box branch, the porcelain is empty, and the path is not locked, not drain-*, not named by a running
    process. A merged worktree with porcelain dirt reads REMOVABLE-AFTER-PRESERVE: --go preserves the dirt first."""
    want = Path(args.check_removable).resolve()
    match = None
    for w in worktrees()[1:]:  # [0] is the main worktree, never a candidate
        try:
            if Path(str(w.get("worktree", ""))).resolve() == want:
                match = w
        except OSError:
            pass
    if match is None:
        print(f"ERROR: not a linked worktree of this repository: {args.check_removable}")
        return 2

    def not_removable(cls: str, why: str) -> int:
        print(f"NOT-REMOVABLE {cls} {why}")
        return 1

    r = classify(match, args.trunk, 0.0, args.held_hours, live_serials(), time.time())
    if r["class"] in ("SKIP", "PRUNABLE"):
        return not_removable(r["class"], r["reason"])
    if r["own"] is None or r["own"] < 1:
        return not_removable("UNSTARTED", f"own={'unknown' if r['own'] is None else 0}; no commit of its own")
    if not r["merged"]:
        return not_removable(r["class"], f"own={r['own']}; HEAD is not in the trunk or a box branch; {r['reason']}")
    text = in_use_text()
    if text is None:
        return not_removable("SKIP", "in-use read failed (process/scheduled-task list); not removable")
    if path_in_use(r["path"], text):
        return not_removable("SKIP", "IN USE: a running process or scheduled task names this path")
    if r["dirty"]:  # the same verdict --go reaches: the dirt is preserved on a preserve/ branch before removal
        print(f"REMOVABLE-AFTER-PRESERVE MERGED own={r['own']}; {r['dirty']} path(s) would be preserved")
        return 0
    print(f"REMOVABLE CLEAN own={r['own']}; {r['reason']}")
    return 0


def held_for(serial: str) -> list[dict]:
    held = load_state().get("held", {})
    return [r for r in held.values() if r.get("owner") == serial]


def hook_notice() -> int:
    """PostToolUse(register_agent): tell the registering seat which held worktrees it owns. Never blocks."""
    try:
        payload = json.loads(sys.stdin.read() or "{}")
        serial = str((payload.get("tool_input") or {}).get("agent_serial") or "")
    except ValueError:
        return 0
    rows = held_for(serial) if serial else []
    if not rows:
        return 0
    lines = [f"WORKTREE-GC: {serial} holds {len(rows)} worktree(s) with UNLANDED work, idle past 24 h. Assess each now: "
             "land it (commit + merge) or discard it explicitly; nothing here is removed without you."]
    for r in rows:
        lines.append(f"  {r['class']}: {r['path']} [{r['branch']}] {r['reason']}")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "\n".join(lines)}}))
    return 0


def selftest() -> int:
    """A throwaway repo: one merged+dirty worktree (removed by --go) and one unmerged+dirty worktree (kept)."""
    import shutil
    import tempfile
    global _REPO
    base = Path(tempfile.mkdtemp(prefix="wtgc_")).resolve()   # long spelling, as git worktree list prints it
    main_tree, wa, wb = base / "main", base / "wk-merged", base / "wk-unmerged"
    wc = base / "wk-in-use"
    holder = None
    ok = []
    try:
        def g(*a, cwd=main_tree):
            git(["-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=str(cwd), check=True)
        main_tree.mkdir()
        g("init", "-q", "-b", "CLOUD")
        (main_tree / "org" / "mcp").mkdir(parents=True)   # the audit line lands in the temp repo
        (main_tree / "f.txt").write_text("x\n", encoding="ascii")
        g("add", "f.txt")
        g("commit", "-q", "-m", "c0")
        g("worktree", "add", "-q", "-b", "wk-a", str(wa), "CLOUD")
        g("worktree", "add", "-q", "-b", "wk-b", str(wb), "CLOUD")
        g("worktree", "add", "-q", "-b", "wk-c", str(wc), "CLOUD")
        # a live process whose command line names wk-in-use, as a scheduled runner's would
        holder = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(120)", str(wc)])
        # CT-af-1: a "merged" worktree carries one own commit and that commit lands in the trunk (a branch at its
        # creation point is UNSTARTED, never MERGED or CLEAN)
        for t, name in ((wa, "a.txt"), (wc, "c.txt")):
            (t / name).write_text("z\n", encoding="ascii")
            g("add", name, cwd=t)
            g("commit", "-q", "-m", "own", cwd=t)
        g("merge", "-q", "--no-ff", "--no-edit", "wk-a")
        g("merge", "-q", "--no-ff", "--no-edit", "wk-c")
        (wb / "g.txt").write_text("y\n", encoding="ascii")
        g("add", "g.txt", cwd=wb)
        g("commit", "-q", "-m", "unlanded", cwd=wb)
        for t in (wa, wb):   # uncommitted edits in both
            (t / "f.txt").write_text("edited\n", encoding="ascii")
            (t / "scratch.tmp").write_text("u\n", encoding="ascii")
        _REPO = str(main_tree)
        ns = argparse.Namespace(go=True, trunk="CLOUD", clean_hours=0.0, held_hours=48.0, only="")
        run(ns)
        ok.append(("merged+dirty -> removed", not wa.exists()))
        ok.append(("unmerged+dirty -> kept (HELD)", wb.is_dir() and (wb / "scratch.tmp").exists()))
        ok.append(("merged+clean but named by a live process -> kept (SKIP IN USE)", wc.is_dir()))
    finally:
        if holder is not None:
            holder.kill()
            holder.wait()
        _REPO = None
        shutil.rmtree(base, ignore_errors=True)
    for name, res in ok:
        print(f"  {'PASS' if res else 'FAIL'}  {name}")
    passed = sum(1 for _, r in ok if r)
    print(f"WORKTREE-GC-SELFTEST cases={passed}/{len(ok)} ok={passed == len(ok) == 3}")
    return 0 if passed == len(ok) == 3 else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--go", action="store_true", help="remove CLEAN worktrees, prune, log, write state")
    ap.add_argument("--trunk", default="CLOUD")
    ap.add_argument("--clean-hours", type=float, default=24.0)
    ap.add_argument("--held-hours", type=float, default=48.0)
    ap.add_argument("--held-for", default="")
    ap.add_argument("--hook-notice", action="store_true")
    ap.add_argument("--selftest", action="store_true", help="exercise MERGED (force-removed) and HELD (kept) on a temp repo")
    ap.add_argument("--check-removable", default="", metavar="PATH",
                    help="the drain's removable test on one linked worktree (idle window ignored); removes nothing")
    ap.add_argument("--only", default="", metavar="PATH",
                    help="restrict the dry run or --go to the ONE linked worktree at PATH (exit 2 if it is not one)")
    ap.add_argument("--repo", default="", help="operate on this repository (exercise); default: the one holding this script")
    args = ap.parse_args()
    global _REPO
    _REPO = args.repo or None
    if args.selftest:
        return selftest()
    if args.check_removable:
        return check_removable(args)
    if args.hook_notice:
        return hook_notice()
    if args.held_for:
        for r in held_for(args.held_for):
            print(f"{r['class']}: {r['path']} [{r['branch']}] {r['reason']}")
        return 0
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
