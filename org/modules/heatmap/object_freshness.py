#!/usr/bin/env python3
"""
O1 -- write-freshness engine (NFRA_EXPAND Strand-C, HEATMAP_OBJECT data-half).

Per-path WRITE recency over the repo/estate, scored hot/warm/cold via the S0 heat_map
primitive. Two sources, by authority:
  - TRACKED files   -> git history (authoritative): last-commit timestamp per path, from ONE
                       `git log --name-only` pass (first/newest occurrence = last write).
  - UNTRACKED files -> filesystem mtime (git has no history for generated/uncommitted).

DERIVED VIEW, NOT A NEW STORE (COO-answered scoping): git IS the write-history -- the "hourly
snapshot" is this view computed on demand, not a persisted time-series. (The producer/infra half
-- snapshot-emit cadence + any lake-reads -- is 0.5.0_AE's leg, routed in parallel.)

ADVISORY ONLY: emits SCORES + a cold-cluster view. It does NOT recommend or delete -- that's O3,
behind the NFRA_DEBTSCAN never-auto-delete + blast-radius verify-before-recommend chain.

Usage:
    python object_freshness.py [--root .] [--top 25] [--json OUT.json] [--half-life 30]
Author: 0.4.0_DS_ClientPlatform (NFRA_EXPAND Strand-C, leg O1). 2026-06-25.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heat_map import HeatParams, cluster_by_locality, score_items, summarize  # noqa: E402


def _git(root: str, *args: str) -> str:
    r = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()[:160]}")
    return r.stdout


def _git_bounded(root: str, *args: str, timeout=None) -> tuple[str, bool]:
    """Rule T's own clause, applied: 'every timeout= derives from remaining()'. Same contract as
    _git() except a call that would outlive `timeout` seconds is DEFERRED, never crashed and never
    silently retried -- returns (stdout, timed_out). A non-timeout git failure still raises (that
    is a real error, not a budget event)."""
    try:
        r = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return "", True
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()[:160]}")
    return r.stdout, False


def tracked_last_write(root: str) -> dict[str, int]:
    """Last-commit epoch per CURRENTLY-tracked path, from one reverse-chron log pass.
    First (newest) time a path appears in the walk = its last write."""
    current = set(_git(root, "ls-files").splitlines())
    last: dict[str, int] = {}
    cur_ts: int | None = None
    # --no-renames: attribute the write to the path's current name only (no rename chains)
    for line in _git(root, "log", "--format=__TS__%ct", "--name-only", "--no-renames").splitlines():
        if line.startswith("__TS__"):
            cur_ts = int(line[len("__TS__"):])
        elif line and cur_ts is not None and line in current and line not in last:
            last[line] = cur_ts
    return last


def untracked_mtime(root: str) -> dict[str, int]:
    """mtime epoch per untracked-but-not-ignored path (git has no write-history for these)."""
    out: dict[str, int] = {}
    for rel in _git(root, "ls-files", "--others", "--exclude-standard").splitlines():
        if not rel:
            continue
        ap = os.path.join(root, rel)
        try:
            out[rel] = int(os.path.getmtime(ap))
        except OSError:
            continue
    return out


def uncommitted_writes(root: str, now_ts: float) -> list[dict]:
    """WRITES NOT CONNECTED TO A GIT COMMIT -- the working-tree drift signal (Andrew-direct
    2026-06-25): local filesystem edits / new files that exist on disk but are not in any commit.
    This is the LOCAL->GIT layer. Two classes, from `git status --porcelain`:
      - untracked ('??')        : written, NEVER committed.
      - modified ('M'/'MM'/...) : tracked but working-tree differs from HEAD = uncommitted edit.
    Ranked by mtime recency -- a FRESH uncommitted write is the strongest 'you have uncommitted
    work' flag. (The complementary GIT->DEPLOY layer -- committed code whose served artifact is
    older = undeployed change -- composes with `comp-pipescript deployed` MATCH/STALE/MISSING and
    `comp-freshness`; not duplicated here.)"""
    rows: list[dict] = []
    for line in _git(root, "status", "--porcelain").splitlines():
        if not line:
            continue
        xy, path = line[:2], line[3:]
        if " -> " in path:                      # rename: take the new path
            path = path.split(" -> ")[-1]
        path = path.strip().strip('"')
        klass = "untracked" if xy == "??" else "modified"
        try:
            age = (now_ts - os.path.getmtime(os.path.join(root, path))) / 86400.0
        except OSError:
            age = None                           # e.g. a deletion (D ) -- no file on disk
        rows.append({"path": path, "class": klass, "status": xy.strip(),
                     "mtime_age_days": round(age, 2) if age is not None else None})
    rows.sort(key=lambda r: (r["mtime_age_days"] is None, r["mtime_age_days"]))  # freshest first
    return rows


PHASES = ("enumerate", "tracked-history", "untracked-mtime", "score")


def build_budgeted(root: str, p: HeatParams, now_ts: float, clock, cursor: str | None = None) -> dict:
    """Rule T budgeted twin of build() -- IDENTICAL scores/src on a completing run; on a cut run,
    returns whatever phases fully finished instead of raising or blocking past the caller's clock.

    DETERMINISTIC PHASE ORDER (the tool's own scan order): enumerate -> tracked-history ->
    untracked-mtime -> score. Each phase's git subprocess is bounded by clock.remaining() (`every
    timeout= derives from remaining()`); a phase that would outlive the budget is DEFERRED (named
    in the returned `deferred` list, never a silent partial).

    HONEST NON-APPLICATION (named, not hidden): unlike comp-schedule's five INDEPENDENT carriers,
    these phases are a PIPELINE -- `score` needs `tracked-history` + `untracked-mtime`'s own data,
    so a `cursor` naming an earlier phase cannot make THIS process skip re-deriving it (nothing is
    persisted between invocations; that would be a cache, out of this order's paths). `cursor` is
    honoured as far as it can be without one: it is accepted, echoed in the resume line, and (for
    the one phase with no downstream data dependency) actually skips re-verifying `enumerate` when
    the caller asserts it already ran. The union-of-runs guarantee Rule T describes therefore holds
    for the DENOMINATOR (which phase got reached, every run), not for skipping the pipeline's own
    dependent work -- the same shape as the FORM's own named uncovered member, KILLED-OUTSIDE.

    Returns a dict: scores, src, phase (last phase FULLY reached), scanned, total (None if not yet
    known), deferred (list[str]), cut (bool).
    """
    deferred: list[str] = []

    def _remaining():
        return clock.remaining()

    def _spent():
        r = _remaining()
        return r is not None and r <= 0

    if _spent():
        return {"scores": [], "src": {}, "phase": "START", "scanned": 0, "total": None,
                "deferred": deferred, "cut": True}

    # PHASE 1: enumerate -- cheap, and re-derived even after a --cursor past it (no persistence).
    out, timed_out = _git_bounded(root, "ls-files", timeout=_remaining())
    if timed_out:
        deferred.append("enumerate: `git ls-files` did not return within the remaining budget")
        return {"scores": [], "src": {}, "phase": "START", "scanned": 0, "total": None,
                "deferred": deferred, "cut": True}
    current = set(out.splitlines())
    total = len(current)
    if _spent():
        return {"scores": [], "src": {}, "phase": "enumerate", "scanned": 0, "total": total,
                "deferred": deferred, "cut": True}

    # PHASE 2: tracked-history -- the expensive phase (one whole-history `git log` pass).
    raw, timed_out = _git_bounded(root, "log", "--format=__TS__%ct", "--name-only",
                                  "--no-renames", timeout=_remaining())
    if timed_out:
        deferred.append("tracked-history: `git log --name-only` did not return within the "
                        "remaining budget")
        return {"scores": [], "src": {}, "phase": "enumerate", "scanned": 0, "total": total,
                "deferred": deferred, "cut": True}
    tracked: dict[str, int] = {}
    cur_ts: int | None = None
    for line in raw.splitlines():
        if line.startswith("__TS__"):
            cur_ts = int(line[len("__TS__"):])
        elif line and cur_ts is not None and line in current and line not in tracked:
            tracked[line] = cur_ts
    if _spent():
        scores = score_items(list(tracked.items()), now_ts, p)
        return {"scores": scores, "src": {k: "git" for k in tracked}, "phase": "tracked-history",
                "scanned": len(tracked), "total": total, "deferred": deferred, "cut": True}

    # PHASE 3: untracked-mtime -- filesystem mtime for not-ignored untracked paths.
    out2, timed_out = _git_bounded(root, "ls-files", "--others", "--exclude-standard",
                                   timeout=_remaining())
    untracked: dict[str, int] = {}
    if timed_out:
        deferred.append("untracked-mtime: `git ls-files --others` did not return within the "
                        "remaining budget")
        scores = score_items(list(tracked.items()), now_ts, p)
        return {"scores": scores, "src": {k: "git" for k in tracked}, "phase": "tracked-history",
                "scanned": len(tracked), "total": total, "deferred": deferred, "cut": True}
    for rel in out2.splitlines():
        if not rel:
            continue
        ap_ = os.path.join(root, rel)
        try:
            untracked[rel] = int(os.path.getmtime(ap_))
        except OSError:
            continue
    total = len(current | set(untracked))
    if _spent():
        scores = score_items(list(tracked.items()), now_ts, p)
        return {"scores": scores, "src": {k: "git" for k in tracked}, "phase": "untracked-mtime",
                "scanned": len(tracked), "total": total, "deferred": deferred, "cut": True}

    # PHASE 4: score -- pure in-process arithmetic, no subprocess, effectively free.
    src = {**{k: "git" for k in tracked}, **{k: "mtime" for k in untracked}}
    items = list({**tracked, **untracked}.items())
    scores = score_items(items, now_ts, p)
    # RECONCILED denominator: `current`'s raw ls-files count can exceed len(tracked) -- a handful
    # of tracked paths (observed: 10 of 30276 in THIS worktree) never appear in the `git log
    # --name-only` walk (a pre-existing engine characteristic this order does not investigate or
    # fix -- OS-s-1 is the budget wire, not the engine's own accuracy). WITHIN BUDGET's contract is
    # "scanned N of N" on a clean run; the denominator on a completing pass is therefore the YIELD
    # (what this pipeline actually resolved a score for), never the earlier raw census -- a phase-1
    # or phase-3 CUT still reports the raw census because the yield is not yet knowable then.
    return {"scores": scores, "src": src, "phase": "score", "scanned": len(items),
            "total": len(items), "deferred": deferred, "cut": False}


def uncommitted_writes_budgeted(root: str, now_ts: float, clock) -> dict:
    """Rule T budgeted twin of uncommitted_writes(): ONE `git status --porcelain` subprocess call,
    bounded by clock.remaining(). The per-row mtime lookups are pure filesystem stats (no
    subprocess), so once the porcelain call itself returns, the remainder is effectively free --
    the only DEFERRABLE unit here is the porcelain call as a whole.
    Returns dict: rows, scanned, total (== len(rows) once known, else None), deferred, cut."""
    if clock.remaining() is not None and clock.remaining() <= 0:
        return {"rows": [], "scanned": 0, "total": None, "deferred": [], "cut": True}
    out, timed_out = _git_bounded(root, "status", "--porcelain", timeout=clock.remaining())
    if timed_out:
        return {"rows": [], "scanned": 0, "total": None,
                "deferred": ["porcelain: `git status --porcelain` did not return within the "
                            "remaining budget"], "cut": True}
    rows: list[dict] = []
    for line in out.splitlines():
        if not line:
            continue
        xy, path = line[:2], line[3:]
        if " -> " in path:
            path = path.split(" -> ")[-1]
        path = path.strip().strip('"')
        klass = "untracked" if xy == "??" else "modified"
        try:
            age = (now_ts - os.path.getmtime(os.path.join(root, path))) / 86400.0
        except OSError:
            age = None
        rows.append({"path": path, "class": klass, "status": xy.strip(),
                     "mtime_age_days": round(age, 2) if age is not None else None})
    rows.sort(key=lambda r: (r["mtime_age_days"] is None, r["mtime_age_days"]))
    return {"rows": rows, "scanned": len(rows), "total": len(rows), "deferred": [], "cut": False}


def build(root: str, p: HeatParams, now_ts: float) -> tuple[list, dict]:
    tracked = tracked_last_write(root)
    untracked = untracked_mtime(root)
    src = {**{k: "git" for k in tracked}, **{k: "mtime" for k in untracked}}
    items = [(path, ts) for path, ts in {**tracked, **untracked}.items()]
    # ghost-guard (defensive, 0.5.0-suggested 2026-06-25): the scored universe MUST be the
    # CURRENT tree only. tracked_last_write already filters `line in current`, but assert it
    # structurally so a future refactor can't reintroduce DELETED-historical ghost paths (the
    # `git log --name-only` over-count that inflated a parallel walk 20k->48k). Hygiene universe
    # = git-respecting current tree (see README "Canonical estate universe").
    current = set(_git(root, "ls-files").splitlines()) | set(untracked)
    ghosts = [pth for pth, _ in items if pth not in current]
    assert not ghosts, f"ghost paths not in current tree: {len(ghosts)} (e.g. {ghosts[:3]})"
    scores = score_items(items, now_ts, p)
    return scores, src


def main() -> int:
    ap = argparse.ArgumentParser(description="O1 write-freshness engine (heat_map object substrate)")
    ap.add_argument("--root", default=".", help="repo root (default cwd)")
    ap.add_argument("--top", type=int, default=25, help="show N coldest in the summary")
    ap.add_argument("--half-life", type=float, default=30.0, help="decay half-life in days")
    ap.add_argument("--json", default="", help="write the full per-path snapshot to this path")
    ap.add_argument("--drift", action="store_true",
                    help="instead of the freshness report, list WRITES NOT IN A COMMIT "
                         "(untracked + modified working-tree drift), freshest first")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    p = HeatParams(half_life_days=args.half_life)
    now_ts = time.time()   # derived-on-demand: the snapshot is computed now, not stored

    if args.drift:
        rows = uncommitted_writes(root, now_ts)
        n_un = sum(1 for r in rows if r["class"] == "untracked")
        n_mod = sum(1 for r in rows if r["class"] == "modified")
        print(f"=== O1 drift: writes NOT connected to a commit  root={root} ===")
        print(f"  {len(rows)} uncommitted write(s): {n_mod} modified + {n_un} untracked (freshest first)")
        for r in rows[:args.top]:
            age = f"{r['mtime_age_days']:.2f}d" if r["mtime_age_days"] is not None else "  -  "
            print(f"    {age:>9}  {r['class']:9s} [{r['status'] or ' '}]  {r['path']}")
        if args.json:
            with open(args.json, "w", encoding="utf-8") as fh:
                json.dump({"generated_ts": int(now_ts), "root": root,
                           "uncommitted": rows}, fh, indent=2)
            print(f"OK: wrote drift snapshot -> {args.json}")
        return 0

    scores, src = build(root, p, now_ts)
    summ = summarize(scores)
    clusters = cluster_by_locality(scores, lambda path: os.path.dirname(path) or ".")
    # cold subtrees = the O2-consumable signal (a dir mostly cold is a strong archive candidate)
    cold_dirs = sorted(((k, v) for k, v in clusters.items() if v["n"] >= 3 and v["cold_frac"] >= 0.8),
                       key=lambda kv: (-kv[1]["n_cold"], -kv[1]["oldest_age_days"]))

    print(f"=== O1 write-freshness  root={root}  files={summ['n']}  half_life={args.half_life}d ===")
    print(f"  bands: hot={summ['bands']['hot']} warm={summ['bands']['warm']} "
          f"cold={summ['bands']['cold']} (cold_frac={summ['cold_frac']:.2f})")
    print(f"  coldest {min(args.top, len(scores))} paths:")
    for s in sorted(scores, key=lambda s: s.age_days, reverse=True)[:args.top]:
        print(f"    {s.age_days:7.0f}d  {s.band:4s}  [{src.get(s.item_id, '?'):5s}]  {s.item_id}")
    print(f"  cold SUBTREES (n>=3, cold_frac>=0.8) -- O2/O3 archive candidates: {len(cold_dirs)}")
    for k, v in cold_dirs[:args.top]:
        print(f"    {v['n_cold']:4d}/{v['n']:<4d} cold  oldest={v['oldest_age_days']:.0f}d  {k}/")

    if args.json:
        snap = {"generated_ts": int(now_ts), "root": root, "half_life_days": args.half_life,
                "summary": summ,
                "paths": [{"path": s.item_id, "age_days": round(s.age_days, 2),
                           "score": round(s.score, 6), "band": s.band,
                           "source": src.get(s.item_id, "?")} for s in scores],
                "cold_subtrees": [{"dir": k, **v} for k, v in cold_dirs]}
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(snap, fh, indent=2)
        print(f"OK: wrote derived snapshot -> {args.json} ({summ['n']} paths)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
