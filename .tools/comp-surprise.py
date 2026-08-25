#!/usr/bin/env python3
"""comp-surprise.py -- the SURPRISE CHANNEL rollup: every open item across every project, in ONE list.

THE GAP THIS CLOSES: the protocol writes ONE INVESTIGATION_v{N}.md PER PROJECT, and nothing read them
together. CVO could see a project; nobody could see the CHANNEL. An item filed into a per-project file
that no aggregate view reads is filed and invisible -- which is why the investigate -> graduate ->
remediate cycle stalls at "filed".

Read-only: pure filesystem + json over artifacts CVO already writes. It REPORTS. It does not file,
graduate, dismiss, or edit anything -- the channel is CVO's surface (CLAUDE.md Rule 27).

Usage:
  comp-surprise                 the board: open items grouped by disposition, denominators printed
  comp-surprise --armed         ARMED items only (the ones that can cause harm while unattended)
  comp-surprise --project CODE  one project in full
  comp-surprise --all           include GRADUATED / DISMISSED (closed) items
  comp-surprise --json          machine rows
"""
from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re
import subprocess

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True).stdout.strip() or os.getcwd()
CHANNEL = os.path.join(ROOT, "org", "surprise_channel")
SEP = "-" * 78
OPEN_DISPOSITIONS = {"UNDER_INVESTIGATION", "DECOMP_INVALIDATING"}


def _blocks(path):
    """Every fenced json block in a file. Malformed blocks are SURFACED, never dropped."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    out, bad = [], []
    for m in re.finditer(r"```json\s*(.*?)```", txt, re.S):
        try:
            out.append(json.loads(m.group(1)))
        except Exception as e:
            bad.append("%s: %s" % (os.path.relpath(path, ROOT), type(e).__name__))
    return out, bad


def load():
    items, malformed, files = [], [], 0
    if not os.path.isdir(CHANNEL):
        return items, malformed, 0, 0
    pats = [os.path.join(CHANNEL, "*", "INVESTIGATION_v*.md"),
            os.path.join(CHANNEL, "*", "REMEDIATION_v*.md")]
    paths = sorted({p for pat in pats for p in glob.glob(pat)})
    for p in paths:
        files += 1
        project = os.path.basename(os.path.dirname(p))
        kind = "REMEDIATION" if "REMEDIATION" in os.path.basename(p) else "INVESTIGATION"
        blocks, bad = _blocks(p)
        malformed.extend(bad)
        for b in blocks:
            rows = b if isinstance(b, list) else b.get("items", [b]) if isinstance(b, dict) else []
            for r in rows:
                if not isinstance(r, dict) or "id" not in r:
                    continue
                r = dict(r)
                r["_project"] = project
                r["_kind"] = kind
                r["_file"] = os.path.relpath(p, ROOT)
                items.append(r)
    return items, malformed, files, len(paths)


def age_days(s):
    if not s:
        return None
    m = re.search(r"(20\d\d-\d\d-\d\d)", str(s))
    if not m:
        return None
    d = datetime.datetime.fromisoformat(m.group(1)).replace(tzinfo=datetime.UTC)
    return (datetime.datetime.now(datetime.UTC) - d).total_seconds() / 86400


def defects(items):
    """Schema-encoded obligations that are UNMET. The schema's conditionals ARE the law."""
    out = []
    for r in items:
        d = r.get("disposition")
        # ARMED requires a NAMED disarm owner -- an armed hazard with nobody on it is the
        # one state the channel exists to make impossible.
        if r.get("hazard_standing") == "ARMED" and not str(r.get("disarm_owner") or "").strip():
            out.append((r, "ARMED with NO disarm_owner"))
        if d == "GRADUATED" and str((r.get("grounding") or {}).get("status", "")).upper() != "GROUNDED":
            out.append((r, "GRADUATED without GROUNDED grounding"))
        if d == "DISMISSED_WITH_REASON" and not str(r.get("dismissal_reason") or "").strip():
            out.append((r, "DISMISSED with no dismissal_reason"))
    return out


def render(r, wide=False):
    a = age_days(r.get("surfaced_at"))
    age = ("%5.1fd" % a) if a is not None else "    ?"
    haz = r.get("hazard_standing") or "-"
    cls = (r.get("class") or "?")[:11]
    line = "   %-13s %s  %-11s %-6s %-22s %s" % (
        r["_project"][:13], age, cls, haz, str(r.get("id"))[:22],
        re.sub(r"\s+", " ", str(r.get("one_line") or ""))[:0 if wide else 60])
    print(line)
    if wide:
        print("        %s" % re.sub(r"\s+", " ", str(r.get("one_line") or ""))[:150])
        print("        by %s  disp=%s  owner=%s  file=%s"
              % (r.get("surfaced_by", "?"), r.get("disposition", "?"),
                 r.get("disarm_owner") or "-", r["_file"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--armed", action="store_true")
    ap.add_argument("--project")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    items, malformed, files, paths = load()
    if a.project:
        items = [r for r in items if r["_project"].upper() == a.project.upper()]

    openi = [r for r in items if r.get("disposition") in OPEN_DISPOSITIONS]
    armed = [r for r in items if r.get("hazard_standing") == "ARMED"]
    shown = armed if a.armed else (items if a.all else openi)
    dfx = defects(items)

    if a.json:
        print(json.dumps({"items": items, "open": openi, "armed": armed,
                          "defects": [{"id": r.get("id"), "project": r["_project"], "why": w}
                                      for r, w in dfx],
                          "malformed": malformed,
                          "denominators": {"items": len(items), "open": len(openi),
                                           "armed": len(armed), "files": files}},
                         indent=2, default=str))
        return

    print("SURPRISE CHANNEL -- %s  | %s"
          % (os.path.relpath(CHANNEL, ROOT), datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%MZ")))
    print("  (read-only rollup over the per-project files CVO writes; it REPORTS, it never files or graduates)")
    projects = sorted({r["_project"] for r in items})
    print("\n== DENOMINATORS ==")
    print("  %d item(s) across %d project(s), from %d file(s)" % (len(items), len(projects), files))
    print("  OPEN (UNDER_INVESTIGATION / DECOMP_INVALIDATING): %d" % len(openi))
    print("  ARMED (can cause harm while unattended):          %d" % len(armed))
    for d in ("GRADUATED", "DISMISSED_WITH_REASON"):
        print("  %-48s %d" % (d + ":", len([r for r in items if r.get("disposition") == d])))

    if dfx:
        print("\n== SCHEMA OBLIGATIONS UNMET (%d) -- the schema's conditionals ARE the law ==\n%s" % (len(dfx), SEP))
        for r, why in dfx:
            print("   %-13s %-22s %s" % (r["_project"][:13], str(r.get("id"))[:22], why))

    title = "ARMED" if a.armed else ("ALL" if a.all else "OPEN")
    print("\n== %s ITEMS (%d) ==\n%s" % (title, len(shown), SEP))
    print("   %-13s %6s  %-11s %-6s %-22s %s" % ("PROJECT", "AGE", "CLASS", "HAZ", "ID", "ONE-LINE"))
    if not shown:
        print("   (none)")
    for r in sorted(shown, key=lambda x: -(age_days(x.get("surfaced_at")) or 0)):
        render(r, wide=bool(a.project))

    if malformed:
        print("\nWARN: MALFORMED JSON BLOCKS (%d) -- surfaced, fix these:" % len(malformed))
        for m in malformed:
            print("   %s" % m)

    print("\nCOMP-SURPRISE-RESULT items=%d open=%d armed=%d projects=%d files=%d defects=%d malformed=%d"
          % (len(items), len(openi), len(armed), len(projects), files, len(dfx), len(malformed)))


if __name__ == "__main__":
    main()
