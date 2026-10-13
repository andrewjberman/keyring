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
  CLEAN     HEAD is merged into the trunk, nothing modified or untracked, no ignored files beyond build caches,
            idle >= 24 h  ->  removed by --go (`git worktree remove`). Nothing is lost: every committed byte is
            already in the trunk.
  MERGED    HEAD is merged, but the tree holds modified, untracked or non-cache ignored files, idle >= 24 h  ->
            removed by --go with `git worktree remove --force`; the discarded counts are written to the audit line.
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

Every REMOVED worktree, and every first sighting of a HELD or ESCALATE worktree, is one WORKTREE-GC line in
org/mcp/agent-spawn-audit.log. State lives in <git-common-dir>/opal-worktree-gc.json (per box, never committed).

Usage:
  python .tools/worktree_gc.py                 # dry run: the table, nothing changed
  python .tools/worktree_gc.py --go            # remove CLEAN, force-remove MERGED, prune PRUNABLE, log, write state
  python .tools/worktree_gc.py --selftest      # temp repo: merged+dirty -> removed, unmerged+dirty -> kept
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
import subprocess
import sys
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


def classify(wt: dict, trunk: str, clean_h: float, held_h: float, live: set[str], now: float) -> dict:
    path = wt.get("worktree", "")
    branch = str(wt.get("branch", "")).replace("refs/heads/", "") or "(detached)"
    row = {"path": path, "branch": branch, "class": "", "reason": "", "owner": "", "idle_h": None,
           "dirty": 0, "unmerged": 0}
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
    # stale by git activity: now read the working tree
    st = git(["status", "--porcelain", "--untracked-files=all", "--ignored=matching"], cwd=path).stdout.splitlines()
    dirty = [ln[3:] for ln in st if not ln.startswith("!!")]
    ignored = [ln[3:] for ln in st if ln.startswith("!!") and not CACHE_RX.search(ln[3:].replace("\\", "/"))]
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
    row.update({"idle_h": idle_h, "dirty": len(dirty), "unmerged": unmerged})
    if idle_raw < clean_h:
        row.update({"class": "ACTIVE", "reason": "a modified file was edited within the clean window"})
        return row
    if merged and not dirty and not ignored:
        row.update({"class": "CLEAN", "reason": f"merged into {holders[0]}, nothing uncommitted, idle {idle_h} h"})
        return row
    if merged:
        row.update({"class": "MERGED", "reason": f"merged into {holders[0]}; --force discards {len(dirty)} "
                    f"uncommitted/untracked and {len(ignored)} ignored non-cache path(s); idle {idle_h} h"})
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
    if ignored:
        why.append(f"{len(ignored)} ignored non-cache path(s)")
    row["owner"] = owner or "box MSTR (owner unknown)"
    owner_live = bool(owner) and owner in live
    if idle_raw >= held_h and not owner_live:
        row.update({"class": "ESCALATE", "reason": "; ".join(why) + f"; idle {idle_h} h, owner not live"})
    else:
        row.update({"class": "HELD", "reason": "; ".join(why) + f"; idle {idle_h} h"})
    return row


_IN_USE_PS = (
    "$ErrorActionPreference='Stop';"
    "Get-CimInstance Win32_Process | ForEach-Object { $_.CommandLine };"
    "Get-ScheduledTask | ForEach-Object { $_.Actions } | ForEach-Object { $_.Execute; $_.Arguments; $_.WorkingDirectory }"
)


def in_use_text() -> str | None:
    """Every running process command line and scheduled-task action, lowercased with forward slashes.
    None when the read failed: the caller then removes nothing."""
    if sys.platform != "win32":
        res = subprocess.run(["ps", "-eo", "args"], capture_output=True, text=True, errors="replace")
    else:
        res = subprocess.run(["powershell", "-NoProfile", "-Command", _IN_USE_PS], capture_output=True, text=True,
                             encoding="utf-8", errors="replace")
    if res.returncode != 0 or not res.stdout.strip():
        return None
    return res.stdout.replace("\\", "/").lower()


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
    rows = [classify(w, args.trunk, args.clean_hours, args.held_hours, live, now) for w in worktrees()[1:]]
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
    print(f"=== worktree_gc {'GO' if args.go else 'DRY-RUN'} -- trunk {args.trunk}, clean {args.clean_hours} h, "
          f"held {args.held_hours} h, {len(rows)} linked worktree(s), {len(live)} live serial(s) ===")
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
            if r["class"] in ("CLEAN", "MERGED"):
                force = ["--force"] if r["class"] == "MERGED" else []
                res = git(["worktree", "remove", *force, r["path"]], cwd=str(ws_root()))
                if res.returncode == 0:
                    removed += 1
                    audit(f"REMOVED{'-FORCE' if force else ''}  path={r['path']}  branch={r['branch']}  reason={r['reason']}")
                else:
                    failed += 1
                    print(f"  WARN: git worktree remove refused {r['path']}: {res.stderr.strip()[:200]}")
        if any(r["class"] == "PRUNABLE" for r in rows):
            git(["worktree", "prune"], cwd=str(ws_root()))
        try:
            state_path().write_text(json.dumps({"written": now, "held": held_out}, indent=1), encoding="utf-8")
        except OSError as exc:
            print(f"WARN: state write failed: {exc}", file=sys.stderr)
    counts = {c: sum(1 for r in rows if r["class"] == c)
              for c in ("CLEAN", "MERGED", "HELD", "ESCALATE", "ACTIVE", "SKIP", "PRUNABLE")}
    print("SUMMARY: " + "  ".join(f"{k}={v}" for k, v in counts.items())
          + (f"  removed={removed} failed={failed}" if args.go else "  (dry run: nothing removed)"))
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
        (wb / "g.txt").write_text("y\n", encoding="ascii")
        g("add", "g.txt", cwd=wb)
        g("commit", "-q", "-m", "unlanded", cwd=wb)
        for t in (wa, wb):   # uncommitted edits in both
            (t / "f.txt").write_text("edited\n", encoding="ascii")
            (t / "scratch.tmp").write_text("u\n", encoding="ascii")
        _REPO = str(main_tree)
        ns = argparse.Namespace(go=True, trunk="CLOUD", clean_hours=0.0, held_hours=48.0)
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
    ap.add_argument("--repo", default="", help="operate on this repository (exercise); default: the one holding this script")
    args = ap.parse_args()
    global _REPO
    _REPO = args.repo or None
    if args.selftest:
        return selftest()
    if args.hook_notice:
        return hook_notice()
    if args.held_for:
        for r in held_for(args.held_for):
            print(f"{r['class']}: {r['path']} [{r['branch']}] {r['reason']}")
        return 0
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
