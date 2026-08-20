#!/usr/bin/env python3
"""directives-check.py -- the directives register DASHBOARD (live + retired partitions).

The /registry-check of org/missions/DIRECTIVES.yaml: one numbered row per LIVE directive with
the long cells parsed into scan-friendly fields, each member project's registry status beside
it, open task orders counted per directive, and per-row freshness from git blame; then the
RETIRED partition (DIRECTIVES_RETIRED.yaml, machine-cut by comp-directives) with each cut's
authority and frozen vintage. Read-only -- pure filesystem + git + yaml, no MCP, no writes.

Usage:
  directives-check.py              LIVE rows (the working board)
  directives-check.py --all        LIVE + RETIRED partitions
  directives-check.py --retired    RETIRED partition only
  directives-check.py --code D7    one directive, full cells
  directives-check.py --json       machine-readable rows (respects the scope flags)

Per live row:
  Where:   placement DEVICE (LAPTOP/SITEZ parsed from the placement cell's leading token) + PRD path
  Members: sub-groups, and every member PROJECT with its org/projects status [active|closed d]
  TOs:     open task orders summed over member projects (from to-check.py --all, same denominator)
  Stance:  the human stance cell, compacted
  Last:    newest commit touching ANY line of the row (git blame -- per-row, not per-file)
  Flags:   RETIRE-CANDIDATE? = every member project closed (>=1 member) and no open TOs -- a HINT
           for the register owner, never an act (the FACT is human-written per LD-0433);
           NO-MEMBERS = empty member set (honest where a plausible one is not); MALFORMED rows
           are SURFACED, never dropped.

Denominators print in the RESULT line: live / retired / ever_minted / malformed.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:  # the gate env always has it; be loud if not
    print("ERROR: PyYAML missing -- directives-check needs it (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or os.getcwd()
LIVE = os.path.join(ROOT, "org", "missions", "DIRECTIVES.yaml")
RETIRED = os.path.join(ROOT, "org", "missions", "DIRECTIVES_RETIRED.yaml")
PROJECTS = os.path.join(ROOT, "org", "projects")
TOCHECK = os.path.join(ROOT, ".tools", "to-check.py")
SEP = "-" * 78


def compact(s, n=220):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 3] + "..."


def device_of(placement):
    p = str(placement or "").strip().upper()
    for d in ("LAPTOP", "SITEZ"):
        if p.startswith(d):
            return d
    return "UNRULED"


def project_status(code):
    f = os.path.join(PROJECTS, f"{code}.json")
    if not os.path.exists(f):
        return "no-json"
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:  # surfaced, not dropped
        return f"MALFORMED({type(e).__name__})"
    st = str(d.get("status", "?")).lower()
    when = d.get("closed") or d.get("completed") or ""
    return f"{st} {str(when)[5:10]}".strip() if st in ("closed", "complete", "completed") and when else st


def open_tos():
    """project -> open-TO count, parsed from to-check.py --all (its denominator, not ours)."""
    out = {}
    if not os.path.exists(TOCHECK):
        return out
    try:
        txt = subprocess.run([sys.executable, TOCHECK, "--all"], capture_output=True, text=True, timeout=120).stdout
    except Exception:
        return out
    for m in re.finditer(r"^Project: (\S+)\s+\((.+?)\)", txt, re.M):
        n = sum(int(x) for x in re.findall(r"(\d+) (?:ACTIVE|PENDING|BLOCKED|UNKNOWN)", m.group(2)))
        out[m.group(1)] = n
    return out


def row_spans(path):
    """code -> (start_line, end_line) of each 'D{n}:' block under directives:, 1-based."""
    spans, lines = {}, open(path, encoding="utf-8").read().splitlines()
    starts = [(i + 1, re.match(r"^  (D\d+):\s*$", s).group(1)) for i, s in enumerate(lines) if re.match(r"^  D\d+:\s*$", s)]
    for k, (ln, code) in enumerate(starts):
        end = starts[k + 1][0] - 1 if k + 1 < len(starts) else len(lines)
        spans[code] = (ln, end)
    return spans


def blame_newest(path, start, end):
    try:
        out = subprocess.run(["git", "blame", "--line-porcelain", f"-L{start},{end}", path],
                             capture_output=True, text=True, cwd=ROOT).stdout
    except Exception:
        return None
    ts = [int(m.group(1)) for m in re.finditer(r"^committer-time (\d+)$", out, re.M)]
    return datetime.datetime.fromtimestamp(max(ts), datetime.UTC) if ts else None


def key_blame(path, span, key):
    """Newest commit over the lines of ONE top-level key (members:/stance:/...) inside a row span."""
    lines = open(path, encoding="utf-8").read().splitlines()
    start, end = span
    k_start = k_end = None
    for ln in range(start, end + 1):
        s = lines[ln - 1]
        if re.match(rf"^    {key}:", s):
            k_start = ln
            continue
        if k_start and re.match(r"^    [a-z_]+:", s):
            k_end = ln - 1
            break
    if k_start and not k_end:
        k_end = end
    return blame_newest(path, k_start, k_end) if k_start else None


def fmt_age(dt):
    if not dt:
        return "?"
    h = (datetime.datetime.now(datetime.UTC) - dt).total_seconds() / 3600
    return f"{dt:%m-%d %H:%MZ} ({h:.0f}h ago)" if h < 72 else f"{dt:%m-%d} ({h/24:.0f}d ago)"


def load_live():
    d = yaml.safe_load(open(LIVE, encoding="utf-8")) or {}
    rows, malformed = [], []
    spans = row_spans(LIVE)
    tos = open_tos()
    for code, r in (d.get("directives") or {}).items():
        if not isinstance(r, dict) or "title" not in r:
            malformed.append((code, "row is not a mapping with a title"))
            continue
        mem = r.get("members") or {}
        projects = list(mem.get("projects") or [])
        pstat = {p: project_status(p) for p in projects}
        n_to = sum(tos.get(p, 0) for p in projects)
        n_closed = sum(1 for s in pstat.values() if s.startswith(("closed", "complete")))
        all_closed = bool(projects) and n_closed == len(projects)
        flags = []
        if not projects and not (mem.get("subgroups") or []):
            flags.append("NO-MEMBERS")
        # MEMBERSHIP CURRENCY, not work completion: every recorded member closed + 0 TOs. A directive
        # whose scope outgrew its recorded members reads this way while its work is alive (measured
        # 2026-08-20 on D6 -- Andrew: "certainly not going to be any retiring of that for some time"),
        # so the basis prints beside the flag and the name no longer says "retire".
        if all_closed and n_to == 0:
            flags.append(f"MEMBERS-ALL-CLOSED ({n_closed}/{len(projects)} closed, 0 TOs) -- membership currency, NOT work completion")
        span = spans.get(code)
        # MEMBERS-STALE?: the stance moved after the member set last did -- the more useful signal when
        # scope outgrows recorded membership (per-key blame over the row's own line span).
        if span:
            mb, sb = key_blame(LIVE, span, "members"), key_blame(LIVE, span, "stance")
            if mb and sb and (sb - mb).days >= 1:
                flags.append(f"MEMBERS-STALE? (stance moved {sb:%m-%d}, members last {mb:%m-%d})")
        if r.get("retired"):
            flags.append("RETIRED-FACT-PRESENT (awaiting emit)")
        rows.append({
            "code": code, "title": r.get("title", ""), "directive": r.get("directive", ""),
            "prd_exists": os.path.exists(os.path.join(ROOT, str(r.get("directive", "")))),
            "device": device_of(r.get("placement")), "placement": compact(r.get("placement"), 160),
            "subgroups": list(mem.get("subgroups") or []), "projects": pstat, "open_tos": n_to,
            "stance": compact(r.get("stance"), 260), "flags": flags,
            "last": blame_newest(LIVE, *span) if span else None,
        })
    return d, rows, malformed


def load_retired():
    if not os.path.exists(RETIRED):
        return {}, []
    d = yaml.safe_load(open(RETIRED, encoding="utf-8")) or {}
    rows = []
    for code, r in (d.get("directives") or {}).items():
        frozen = {}
        try:
            frozen = (yaml.safe_load(r.get("frozen_row", "")) or {}).get(code, {}) or {}
        except Exception:
            pass
        ret = frozen.get("retired") or {}
        v = r.get("retired_vintage") or {}
        rows.append({"code": code, "title": frozen.get("title", ""), "at": ret.get("at", "?"), "by": ret.get("by", "?"),
                     "authority": compact(ret.get("authority"), 200), "cut_at": v.get("cut_at", "?"),
                     "stances_as_of": v.get("stances_as_of", "?"), "device": device_of(frozen.get("placement"))})
    return d, rows


def print_live(rows, full):
    for i, r in enumerate(rows, 1):
        pj = ", ".join(f"{p}[{s}]" for p, s in r["projects"].items()) or "-"
        flags = f"   <{' | '.join(r['flags'])}>" if r["flags"] else ""
        print(f"{i:>2}. {r['code']}  {r['title']}{flags}")
        print(f"     Where:   {r['device']} -- {r['directive'] or '-'}{'' if r['prd_exists'] else '  [PRD PATH MISSING]'}")
        print(f"     Members: subgroups {r['subgroups'] or '-'}; projects {pj}")
        print(f"     TOs:     {r['open_tos']} open across member projects")
        print(f"     Stance:  {r['stance'] if full else compact(r['stance'], 150) or '-'}")
        if full:
            print(f"     Placed:  {r['placement']}")
        print(f"     Last:    {fmt_age(r['last'])}")
        print(SEP)


def print_retired(d, rows):
    if not rows:
        print("  (no retired rows)")
        return
    for i, r in enumerate(rows, 1):
        print(f"{i:>2}. {r['code']}  {r['title']}   [RETIRED {r['at']} by {r['by']}]")
        print(f"     Authority: {r['authority']}")
        print(f"     Frozen:    cut {r['cut_at']}; stances as_of {r['stances_as_of']}; was {r['device']}")
        print(SEP)
    print(f"  ever_minted: {d.get('ever_minted')}   emits: {len(d.get('emit_log') or [])}   tripwire: {d.get('tripwire', '?')}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--retired", action="store_true")
    ap.add_argument("--code")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    live_doc, live, malformed = load_live()
    ret_doc, retired = load_retired()
    if a.code:
        live = [r for r in live if r["code"] == a.code]
        retired = [r for r in retired if r["code"] == a.code]
    show_live = not a.retired
    show_ret = a.all or a.retired or bool(a.code)

    if a.json:
        print(json.dumps({"live": live if show_live else [], "retired": retired if show_ret else [],
                          "malformed": malformed, "ever_minted": ret_doc.get("ever_minted")}, indent=2, default=str))
        return
    print(f"DIRECTIVES REGISTER -- live as_of {live_doc.get('as_of', '?')} (org/missions/DIRECTIVES.yaml)  "
          f"| {datetime.datetime.now(datetime.UTC):%Y-%m-%d %H:%MZ}")
    print("  (Last = newest commit on ANY line of the row; TOs = to-check --all over member projects; "
          "RETIRE-CANDIDATE? is a hint for the register owner, never an act)")
    if show_live:
        print(f"\n== LIVE ({len(live)}) ==\n{SEP}")
        print_live(live, full=bool(a.code))
    if show_ret:
        print(f"\n== RETIRED ({len(retired)}) -- org/missions/DIRECTIVES_RETIRED.yaml, machine-cut, byte-frozen ==\n{SEP}")
        print_retired(ret_doc, retired)
    if malformed:
        print(f"\nWARN: MALFORMED ROWS ({len(malformed)}) -- surfaced, fix these:")
        for c, e in malformed:
            print(f"   {c}: {e}")
    print(f"\nDIRECTIVES-CHECK-RESULT live={len(live)} retired={len(retired)} "
          f"ever_minted={len(ret_doc.get('ever_minted') or [])} malformed={len(malformed)}")


if __name__ == "__main__":
    main()
