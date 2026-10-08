#!/usr/bin/env python3
"""worktree_gc.py -- the box's worktree garbage collector: remove what is safe, HOLD what has unlanded work.

Andrew-direct 2026-10-08 (records org/tier1_exec/4.0.0_SA_CRO/deliverables/
ANDREW_DIRECT_20261008_173xZ_GC_FOUR_CALLS_ANSWERED_WORKTREE_OWNER_MUST_ASSESS.md):
  "I agree with 24 hours but we dont want to lose uncommitted work ... The agent has to be online to assess"
  and "48 Hours is better".

THE RULE (one class per linked worktree):
  SKIP      the main worktree; a worktree locked with `git worktree lock` (the fence: never touched);
            a `drain-*` worktree.
  ACTIVE    git activity (commit, checkout, or an edited file) within --clean-hours (24 h).
  CLEAN     HEAD is merged into the trunk, nothing modified or untracked, no ignored files beyond build caches,
            idle >= 24 h  ->  removed by --go (`git worktree remove`, never --force). Nothing is lost: every
            committed byte is already in the trunk.
  HELD      anything with unlanded work (modified, untracked, unmerged commits, or non-cache ignored files),
            idle >= 24 h  ->  NEVER touched. It has an OWNER (the serial that authored its newest unlanded commit;
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
  python .tools/worktree_gc.py --go            # remove CLEAN, prune PRUNABLE, log, write state
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
    merged = git(["merge-base", "--is-ancestor", head, trunk], cwd=path).returncode == 0
    unmerged = 0 if merged else int((git(["rev-list", "--count", f"{trunk}..{head}"], cwd=path).stdout.strip() or "0"))
    row.update({"idle_h": idle_h, "dirty": len(dirty), "unmerged": unmerged})
    if idle_raw < clean_h:
        row.update({"class": "ACTIVE", "reason": "a modified file was edited within the clean window"})
        return row
    if merged and not dirty and not ignored:
        row.update({"class": "CLEAN", "reason": f"merged into {trunk}, nothing uncommitted, idle {idle_h} h"})
        return row
    # HELD: find the owner
    owner = ""
    if not merged:
        author = git(["log", "-1", "--format=%an", f"{trunk}..{head}"], cwd=path).stdout.strip()
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


def load_state() -> dict:
    try:
        return json.loads(state_path().read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def run(args: argparse.Namespace) -> int:
    now = time.time()
    live = live_serials()
    rows = [classify(w, args.trunk, args.clean_hours, args.held_hours, live, now) for w in worktrees()[1:]]
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
            if r["class"] == "CLEAN":
                res = git(["worktree", "remove", r["path"]], cwd=str(ws_root()))
                if res.returncode == 0:
                    removed += 1
                    audit(f"REMOVED  path={r['path']}  branch={r['branch']}  reason={r['reason']}")
                else:
                    failed += 1
                    print(f"  WARN: git worktree remove refused {r['path']}: {res.stderr.strip()[:200]}")
        if any(r["class"] == "PRUNABLE" for r in rows):
            git(["worktree", "prune"], cwd=str(ws_root()))
        try:
            state_path().write_text(json.dumps({"written": now, "held": held_out}, indent=1), encoding="utf-8")
        except OSError as exc:
            print(f"WARN: state write failed: {exc}", file=sys.stderr)
    counts = {c: sum(1 for r in rows if r["class"] == c) for c in ("CLEAN", "HELD", "ESCALATE", "ACTIVE", "SKIP", "PRUNABLE")}
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--go", action="store_true", help="remove CLEAN worktrees, prune, log, write state")
    ap.add_argument("--trunk", default="CLOUD")
    ap.add_argument("--clean-hours", type=float, default=24.0)
    ap.add_argument("--held-hours", type=float, default=48.0)
    ap.add_argument("--held-for", default="")
    ap.add_argument("--hook-notice", action="store_true")
    ap.add_argument("--repo", default="", help="operate on this repository (exercise); default: the one holding this script")
    args = ap.parse_args()
    global _REPO
    _REPO = args.repo or None
    if args.hook_notice:
        return hook_notice()
    if args.held_for:
        for r in held_for(args.held_for):
            print(f"{r['class']}: {r['path']} [{r['branch']}] {r['reason']}")
        return 0
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
