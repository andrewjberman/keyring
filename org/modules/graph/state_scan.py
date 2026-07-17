#!/usr/bin/env python3
"""comp-state engine -- BM25 registry/TO/PRD state linter (Andrew-direct 2026-07-14 ~04:2xZ).

THE QUESTION IT ANSWERS: which governance records (REGISTRY rows, project JSONs, task-order
<status> lines, PRD Status: lines) are BEHIND the estate's actual state?

THE MECHANISM (Andrew's design, verbatim intent: "a bm25-style linter on git commits which you
use in tandem with the registry"): the corpus is the recent git commit log (subjects + bodies);
each record contributes a query (its code / TO id / title tokens); commits are ranked per record
by BM25 (engine REUSED from debtscan's dup_scan.py -- the proven implementation) plus a
DIRECT-HIT tier (the record's code appearing verbatim in a commit message). The drift rule:

    strong evidence NEWER than the record's last git touch  =>  the record is BEHIND state.

Verdicts per record (denominators always printed):
    BEHIND        evidence commits postdate the record's last touch -- update the record.
    POST-CLOSE    record is complete/closed but evidence postdates the close -- either scope
                  re-opened silently or activity is mis-attributed. Look.
    CURRENT       evidence exists; none newer than the record's last touch.
    QUIET         no evidence in the window. Context matters: QUIET+pending+old is a stall
                  smell; QUIET+complete is normal.

HONESTY CLAUSES (the night's doctrine, built in):
  - The verdict is ADVISORY and text-based: BM25 measures LEXICAL association, not truth.
    A BEHIND is a place to LOOK, never an auto-edit. A CURRENT is absence-of-lexical-evidence
    of drift, NOT a verified record (comp-state cannot read S3).
  - Record last-touch comes from GIT (last commit touching the file / the row's code string),
    never fs mtime (checkouts lie).
  - The instrument can fail and says so: --self-test plants a synthetic behind-record and a
    synthetic current-record and MUST verdict them BEHIND/CURRENT respectively, else exit 2.

Read-only. Never edits a record. ASCII-only output. Exit 0 = scanned (findings are advisory);
exit 2 = the instrument itself failed (self-test red / no corpus).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from typing import Optional

_HERE = os.path.dirname(os.path.abspath(__file__))            # org/modules/graph/
_WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))  # repo root
sys.path.insert(0, os.path.join(_HERE, "debtscan"))
from dup_scan import BM25  # noqa: E402  -- the proven engine, reused not reimplemented

# The ASCII-only output contract is enforced at the STREAM: scanned records carry arbitrary
# text (a status field's U+2192 killed the render under cp1252, truncating the report), and
# every print site inherits this instead of each sanitizing its own fields.
try:
    sys.stdout.reconfigure(encoding="ascii", errors="backslashreplace")
    sys.stderr.reconfigure(encoding="ascii", errors="backslashreplace")
except AttributeError:
    pass

TOKEN_RE = re.compile(r"[a-z0-9_]{2,}")


def _tok(s: str) -> list[str]:
    return TOKEN_RE.findall(s.lower())


def _git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=_WS, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


# ---- corpus: recent commits ---------------------------------------------------------------
def load_commits(max_n: int, days: Optional[int]) -> list[dict]:
    rng = ["--since", f"{days} days ago"] if days else ["-n", str(max_n)]
    raw = _git("log", *rng, "--no-merges", "--format=%H%x01%ct%x01%an%x01%s%x01%b%x02")
    out = []
    for chunk in raw.split("\x02"):
        chunk = chunk.strip()
        if not chunk:
            continue
        parts = chunk.split("\x01")
        if len(parts) < 5:
            continue
        sha, ct, an, subj, body = parts[0], parts[1], parts[2], parts[3], "\x01".join(parts[4:])
        try:
            ts = int(ct)
        except ValueError:
            continue
        out.append({"sha": sha[:9], "ts": ts, "author": an,
                    "subject": subj, "text": (subj + " " + body).lower(),
                    "doc": _tok(subj + " " + body)})
    return out


# ---- records ------------------------------------------------------------------------------
def _last_touch_file(path: str) -> int:
    """Per-file fallback ONLY. 277ms/call measured 2026-07-17 -- 2,080 records made this the
    entire 300-630s runtime (the 'comp-state hangs' Andrew reported). Bulk path is the map."""
    out = _git("log", "-1", "--format=%ct", "--", path).strip()
    return int(out) if out.isdigit() else 0


def build_last_touch_map() -> dict[str, int]:
    """ONE streaming history walk -> {path: last-commit-ts}. Replaces N per-record
    'git log -1 -- path' subprocesses (measured: 4.1s total vs 277ms EACH; validated
    5/5 exact-match against the per-file answers on 2026-07-17)."""
    raw = _git("log", "--format=%x01%ct", "--name-only")
    last: dict[str, int] = {}
    ts = 0
    for ln in raw.splitlines():
        if ln.startswith("\x01"):
            try:
                ts = int(ln[1:])
            except ValueError:
                ts = 0
        elif ln and ts:
            if ln not in last:          # log is newest-first: first seen = last touch
                last[ln] = ts
    return last


def build_registry_line_touch(rel: str) -> dict[int, int]:
    """ONE 'git blame --line-porcelain' -> {1-based line number: last-touch ts} for the
    working-tree REGISTRY. Replaces a 0.5s pickaxe (-S) subprocess PER active row.
    Uncommitted lines blame to sha 0*40 with ts=now -- correct here (the row was just touched,
    so no corpus commit can postdate it)."""
    raw = _git("blame", "--line-porcelain", "--", rel)
    out: dict[int, int] = {}
    cur_ts = 0
    cur_line = 0
    for ln in raw.splitlines():
        m = re.match(r"^[0-9a-f]{40} \d+ (\d+)", ln)
        if m:
            cur_line = int(m.group(1))
        elif ln.startswith("committer-time "):
            try:
                cur_ts = int(ln.split()[1])
            except (IndexError, ValueError):
                cur_ts = 0
            if cur_line:
                out[cur_line] = cur_ts
    return out


def load_records(only_code: Optional[str]) -> list[dict]:
    recs: list[dict] = []
    touch = build_last_touch_map()

    def _last(rel: str) -> int:
        return touch.get(rel) or _last_touch_file(rel)

    # (a) task orders -------------------------------------------------------------------
    to_glob = subprocess.run(
        ["git", "ls-files", "org/*/*/task_orders/*.md", "org/*/task_orders/*.md"],
        cwd=_WS, capture_output=True, text=True).stdout.splitlines()
    for rel in to_glob:
        stem = os.path.basename(rel)[:-3]
        try:
            body = open(os.path.join(_WS, rel), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        m = re.search(r"<status>([^<]{1,400})</status>", body, flags=re.S)
        status = (" ".join(m.group(1).split())[:120] if m else "?")
        parts_ = stem.split(".")
        code = parts_[0]
        tokey = ".".join(parts_[:2]).lower() if len(parts_) > 1 else stem.lower()
        comp = parts_[1].lower() if len(parts_) > 1 else ""
        recs.append({"kind": "TO", "id": stem, "code": code, "status": status,
                     "tokey": tokey, "comp": comp,
                     "path": rel, "last": _last(rel),
                     "query": _tok(stem.replace(".", " ").replace("-", " "))})
    # (b) project JSONs -----------------------------------------------------------------
    pj_dir = os.path.join(_WS, "org", "projects")
    for fn in sorted(os.listdir(pj_dir)):
        if not fn.endswith(".json"):
            continue
        rel = f"org/projects/{fn}"
        try:
            d = json.load(open(os.path.join(pj_dir, fn), encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            recs.append({"kind": "JSON", "id": fn, "code": fn[:-5], "status": "UNPARSEABLE",
                         "path": rel, "last": _last(rel), "query": _tok(fn)})
            continue
        code = fn[:-5]
        phase = str(d.get("phase", d.get("current_phase", "")))[:300]
        recs.append({"kind": "JSON", "id": fn, "code": code,
                     "status": str(d.get("status", "?")),
                     "path": rel, "last": _last(rel),
                     "query": _tok(code.replace("_", " ") + " " + phase)[:24]})
    # (c) REGISTRY rows (active table only: rows above the Completed/Archived heading) ---
    reg_rel = "org/projects/REGISTRY.md"
    try:
        reg = open(os.path.join(_WS, reg_rel), encoding="utf-8", errors="replace").read()
    except OSError:
        reg = ""
    active_part = re.split(r"^#+\s*(Completed|Archived)", reg, maxsplit=1, flags=re.M)[0]
    # Per-row last-touch from ONE blame call (was: one -S pickaxe subprocess per row).
    line_ts = build_registry_line_touch(reg_rel) if reg else {}
    for m in re.finditer(r"^\|\s*`([A-Z0-9_]{3,})`\s*\|(.+)$", active_part, flags=re.M):
        code, rest = m.group(1), m.group(2)
        line_no = active_part.count("\n", 0, m.start()) + 1
        recs.append({"kind": "REGROW", "id": f"REGISTRY:{code}", "code": code,
                     "status": "active-row",
                     "path": reg_rel, "last": line_ts.get(line_no, 0),
                     "query": _tok(code.replace("_", " ") + " " + rest[:200])[:24]})
    # (d) PRD Status: lines ----------------------------------------------------------------
    prd_list = subprocess.run(["git", "ls-files", "docs/architecture/*PRD*.md"],
                              cwd=_WS, capture_output=True, text=True).stdout.splitlines()
    for rel in prd_list:
        try:
            head = open(os.path.join(_WS, rel), encoding="utf-8", errors="replace").read(4000)
        except OSError:
            continue
        m = re.search(r"^\*{0,2}Status:?\*{0,2}\s*(.+)$", head, flags=re.M)
        if not m:
            continue
        stem = os.path.basename(rel)[:-3]
        recs.append({"kind": "PRD", "id": stem, "code": stem.replace("_PRD", ""),
                     "status": m.group(1).strip()[:100],
                     "path": rel, "last": _last(rel),
                     "query": _tok(stem.replace("_", " "))})
    if only_code:
        oc = only_code.lower()
        recs = [r for r in recs if oc in r["code"].lower() or oc in r["id"].lower()]
    return recs


# ---- verdicts ------------------------------------------------------------------------------
CLOSED_TOKENS = ("complete", "closed", "superseded", "cancelled", "done")


def assess(rec: dict, commits: list[dict], bm: BM25, floor: float, top_k: int = 4) -> dict:
    # DIRECT-HIT tier. For a TO the identifier is CODE.Cn (bare project code would match EVERY
    # project commit and drown the signal -- measured on the first live run, 33/34 false-BEHIND);
    # for JSON/REGROW/PRD records the bare code IS the right key.
    id_l, code_l = rec["id"].lower(), rec["code"].lower()
    if rec["kind"] == "TO":
        key = rec.get("tokey", id_l)
        direct = [c for c in commits if key in c["text"] or id_l in c["text"]]
    else:
        direct = [c for c in commits if id_l in c["text"] or
                  (len(code_l) >= 6 and code_l in c["text"])]
    # BM25 tier. For a TO, evidence must also CARRY THE COMPONENT TOKEN (c1/c10/...) --
    # shared project vocabulary otherwise cross-matches sibling TOs' commits.
    comp = rec.get("comp", "")
    scored = []
    for j, c in enumerate(commits):
        if rec["kind"] == "TO" and comp and comp not in c["doc"]:
            continue
        s = bm._score(rec["query"], j)
        if s >= floor:
            scored.append((s, c))
    scored.sort(key=lambda x: -x[0])
    ev = {c["sha"]: (s, c) for s, c in scored[:top_k * 3]}
    for c in direct:
        ev.setdefault(c["sha"], (999.0, c))          # direct hits always count
    evidence = sorted(ev.values(), key=lambda x: -x[1]["ts"])
    newest = evidence[0][1]["ts"] if evidence else 0
    closed = any(t in rec["status"].lower() for t in CLOSED_TOKENS)
    if not evidence:
        verdict = "QUIET"
    elif newest > rec["last"]:
        verdict = "POST-CLOSE" if closed else "BEHIND"
    else:
        verdict = "CURRENT"
    return {"verdict": verdict, "newest_ev": newest,
            "evidence": [{"sha": c["sha"], "ts": c["ts"], "score": round(s, 2),
                          "subject": c["subject"][:110]} for s, c in evidence[:top_k]]}


# ---- self-test: the instrument must be able to fail ----------------------------------------
def self_test() -> int:
    now = int(time.time())
    commits = [
        {"sha": "aaaaaaaaa", "ts": now - 100, "author": "t",
         "subject": "feat(FAKEPROJ_X9): the widget LANDED and verified",
         "text": "feat(fakeproj_x9): the widget landed and verified",
         "doc": _tok("feat FAKEPROJ_X9 the widget landed and verified")},
        {"sha": "bbbbbbbbb", "ts": now - 100, "author": "t",
         "subject": "chore: unrelated noise", "text": "chore: unrelated noise",
         "doc": _tok("chore unrelated noise")},
    ]
    bm = BM25([c["doc"] for c in commits])
    behind = {"kind": "TO", "id": "FAKEPROJ_X9.T1.widget", "code": "FAKEPROJ_X9",
              "status": "pending", "path": "x", "last": now - 999999,
              "query": _tok("FAKEPROJ_X9 T1 widget")}
    current = {"kind": "TO", "id": "FAKEPROJ_X9.T1.widget", "code": "FAKEPROJ_X9",
               "status": "pending", "path": "x", "last": now,  # touched AFTER the commit
               "query": _tok("FAKEPROJ_X9 T1 widget")}
    quiet = {"kind": "TO", "id": "OTHERPROJ_Z.T9.nothing", "code": "OTHERPROJ_Z",
             "status": "pending", "path": "x", "last": now - 999999,
             "query": _tok("OTHERPROJ_Z T9 zzz qqq")}
    v1 = assess(behind, commits, bm, floor=0.5)["verdict"]
    v2 = assess(current, commits, bm, floor=0.5)["verdict"]
    v3 = assess(quiet, commits, bm, floor=0.5)["verdict"]
    ok = (v1 == "BEHIND") and (v2 == "CURRENT") and (v3 == "QUIET")
    print(f"self-test: planted-behind={v1} planted-current={v2} planted-quiet={v3} "
          f"-> {'PASS (3/3 -- the instrument discriminates)' if ok else 'FAIL'}")
    return 0 if ok else 2


# ---- main ----------------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(
        description="comp-state -- BM25 registry/TO/PRD state linter (advisory, read-only)")
    ap.add_argument("--commits", type=int, default=400, help="corpus size (default 400)")
    ap.add_argument("--days", type=int, default=None, help="corpus window in days (overrides --commits)")
    ap.add_argument("--project", help="filter records to one code substring")
    ap.add_argument("--floor", type=float, default=6.0, help="BM25 evidence floor (default 6.0)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--all", action="store_true", help="show CURRENT/QUIET too (default: drift only)")
    ap.add_argument("--top", type=int, default=60,
                    help="max records rendered in the report (default 60; 0 = unlimited). "
                         "JSON output is never truncated.")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    # Stage timings go to stderr so a stall is diagnosable mid-run (the 2026-07-17 incident:
    # 2,080 serial git subprocesses = 300-630s with ZERO output, indistinguishable from a hang).
    t0 = time.time()
    commits = load_commits(args.commits, args.days)
    t1 = time.time()
    print(f"[stage] corpus: {len(commits)} commits in {t1 - t0:.1f}s", file=sys.stderr)
    if not commits:
        print("comp-state: EMPTY CORPUS -- git log returned nothing. That is an instrument "
              "failure, not a clean estate.", file=sys.stderr)
        return 2
    recs = load_records(args.project)
    t2 = time.time()
    print(f"[stage] records: {len(recs)} loaded (last-touch map + blame) in {t2 - t1:.1f}s",
          file=sys.stderr)
    bm = BM25([c["doc"] for c in commits])

    results = []
    for i, r in enumerate(recs):
        if i and i % 500 == 0:
            print(f"[stage] scoring: {i}/{len(recs)}", file=sys.stderr)
        a = assess(r, commits, bm, args.floor)
        results.append({**{k: r[k] for k in ("kind", "id", "code", "status", "path", "last")}, **a})
    t3 = time.time()
    print(f"[stage] scoring: {len(recs)} records x {len(commits)} commits in {t3 - t2:.1f}s "
          f"(total {t3 - t0:.1f}s)", file=sys.stderr)

    drift = [x for x in results if x["verdict"] in ("BEHIND", "POST-CLOSE")]
    if args.json:
        print(json.dumps({"scanned_commits": len(commits), "records": len(results),
                          "drift": drift,
                          "all": results if args.all else None}, indent=1, default=str))
        return 0

    win = f"{args.days}d" if args.days else f"last {len(commits)} commits"
    print("comp-state -- registry/TO/PRD state linter (ADVISORY; BM25 over git; read-only)")
    print(f"  corpus: {len(commits)} commits ({win}) | records: {len(results)} "
          f"(TO {sum(1 for r in results if r['kind']=='TO')} / JSON "
          f"{sum(1 for r in results if r['kind']=='JSON')} / REGROW "
          f"{sum(1 for r in results if r['kind']=='REGROW')} / PRD "
          f"{sum(1 for r in results if r['kind']=='PRD')})")
    print(f"  verdicts: BEHIND/POST-CLOSE {len(drift)} | "
          f"CURRENT {sum(1 for x in results if x['verdict']=='CURRENT')} | "
          f"QUIET {sum(1 for x in results if x['verdict']=='QUIET')}")
    print("  A BEHIND is a place to LOOK, never an auto-edit. CURRENT = no lexical drift "
          "evidence, NOT a verified record.")
    print()
    show = results if args.all else drift
    show = sorted(show, key=lambda z: (z["verdict"], -z["newest_ev"]))
    dropped = 0
    if args.top and len(show) > args.top:
        dropped = len(show) - args.top
        show = show[:args.top]
    for x in show:
        age_rec = time.strftime("%m-%d %H:%M", time.gmtime(x["last"])) if x["last"] else "never"
        print(f"[{x['verdict']}] {x['kind']:6s} {x['id']}")
        print(f"    status: {x['status'][:90]} | record last touched {age_rec}Z")
        for e in x["evidence"]:
            ets = time.strftime("%m-%d %H:%M", time.gmtime(e["ts"]))
            tag = "DIRECT" if e["score"] >= 999 else f"bm25={e['score']}"
            print(f"    ev {e['sha']} {ets}Z [{tag}] {e['subject']}")
        print()
    if dropped:
        print(f"  ... TRUNCATED: {dropped} more record(s) not shown (denominator above is the "
              f"true count; --top 0 for all, --json for machine-readable full set).")
    if not show:
        print("  no drift found in window (run --all for the full census).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
