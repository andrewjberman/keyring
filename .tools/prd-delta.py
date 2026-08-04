#!/usr/bin/env python3
"""prd-delta.py -- mechanical evidence-gathering engine for the /prd-delta skill.

This script does ONLY data-gathering: find the PRD, the registry JSON, every TO
filed against a project, and every commit referencing it. It makes NO completeness
judgment -- that is the per-project agent's job in the /prd-delta Workflow fan-out.
Read-only.

Reuses the canonical engines so nothing drifts from the sibling lenses:
  - project scope + status  <- registry-check.py's stable `--json -all` contract
  - TO parsing              <- to-check.py's parse_to_file()/find_all_to_files()
    (imported via importlib, same pattern the render_*.py dashboards use elsewhere
    in this skill family)
  - commit resolution       <- the same `git log --all --grep=CODE` pattern
    registry-check.py's git_latest() uses (literal substring match, not the
    word-boundary-exact resolver activity-check.py uses for its dashboards --
    a broader net is fine here; the assessment agent reasons about relevance).

Usage:
  python .tools/prd-delta.py --list-scope                  # hot projects -> JSON array
  python .tools/prd-delta.py --list-scope --all             # hot + cold
  python .tools/prd-delta.py --list-scope --project CODE    # one code (existence-checked)
  python .tools/prd-delta.py --evidence CODE                 # full evidence bundle (JSON)
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
PRD_DIR = WORKSPACE / "docs" / "architecture"
PROJ_DIR = WORKSPACE / "org" / "projects"


def _load_to_check_module():
    spec = importlib.util.spec_from_file_location("to_check_engine", WORKSPACE / ".tools" / "to-check.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def registry_json(code: str):
    f = PROJ_DIR / f"{code}.json"
    if not f.exists():
        return None
    try:
        return json.loads(f.read_text(encoding="utf-8", errors="replace"))
    except Exception as e:
        return {"_parse_error": str(e)}


def find_prd_docs(code: str, reg: dict | None = None):
    """Every PRD-equivalent doc for a project, as a list of {path, label, date}.

    AUTHORITATIVE SOURCE FIRST: org/projects/{code}.json's own `prds` field, when
    present, is curated by the agents who wrote the project and is the ONLY
    correct source -- it already handles cases filename-guessing structurally
    cannot: a project covered by a PARENT's PRD (e.g. NFRA_PPLINF -> the shared
    NFRA_PIPELINE_PRD.md), a project with MULTIPLE PRD-relevant docs (e.g.
    COMP_LEARNS' 15-entry PRD history), or a spec that lives outside
    docs/architecture/ entirely (docs/briefs/, an exec's own deliverables dir).
    `prds` may be a list OR a single object depending on how the registry entry
    was authored -- normalize both.

    FILENAME FALLBACK, only when the registry has no `prds` field at all: try
    `{code}_PRD.md`, then a `{code}*_PRD.md` glob, then a BARE `{code}.md` (a
    second, older, still-widely-used naming convention in this codebase --
    66 of the 90 docs/architecture/*.md project docs use it, no `_PRD` suffix).
    A confirmed miss (0 candidates via every path) is itself a real finding, not
    a tool failure -- but filename-guessing is the LAST resort, not the first.
    """
    if reg is None:
        reg = registry_json(code)
    if reg and reg.get("prds"):
        raw = reg["prds"]
        entries = raw if isinstance(raw, list) else [raw]
        docs = []
        for e in entries:
            if not isinstance(e, dict) or not e.get("path"):
                continue
            p = WORKSPACE / e["path"]
            docs.append({"path": str(p), "label": e.get("label", ""),
                         "date": e.get("date", ""), "exists": p.exists()})
        if docs:
            return docs, "registry"

    exact = PRD_DIR / f"{code}_PRD.md"
    if exact.exists():
        return [{"path": str(exact), "label": "", "date": "", "exists": True}], "filename-exact"
    globbed = sorted(glob.glob(str(PRD_DIR / f"{code}*_PRD.md")))
    if len(globbed) == 1:
        return [{"path": globbed[0], "label": "", "date": "", "exists": True}], "filename-glob"
    bare = PRD_DIR / f"{code}.md"
    if bare.exists():
        return [{"path": str(bare), "label": "", "date": "", "exists": True}], "filename-bare"
    return [], "not-found" if not globbed else "filename-glob-ambiguous"


def project_tos(code: str, tc):
    tos = []
    for path in tc.find_all_to_files():
        d = tc.parse_to_file(path)
        if d.get("project_code", "").upper() == code.upper():
            tos.append(d)
    return tos


def project_commits(code: str, limit: int = 80):
    r = subprocess.run(
        ["git", "log", "--all", "-i", "--grep", code, f"-{limit}",
         "--pretty=format:%H\t%aI\t%an\t%s"],
        capture_output=True, text=True, cwd=str(WORKSPACE), errors="replace",
    )
    out = []
    for ln in r.stdout.splitlines():
        parts = ln.split("\t", 3)
        if len(parts) != 4:
            continue
        sha, iso, author, subj = parts
        out.append({"sha": sha[:9], "iso": iso, "author": author, "subject": subj})
    return out


def cmd_list_scope(args):
    eng = WORKSPACE / ".tools" / "registry-check.py"
    r = subprocess.run([sys.executable, str(eng), "--json", "-all"],
                        capture_output=True, text=True, cwd=str(WORKSPACE))
    if r.returncode != 0 or not r.stdout.strip():
        sys.stderr.write("ERROR: registry-check.py --json -all failed:\n" + (r.stderr or "")[:1000] + "\n")
        sys.exit(1)
    d = json.loads(r.stdout)
    rows = d.get("hot", []) + (d.get("cold", []) if args.all else [])

    if args.project:
        target = args.project.upper()
        rows = [x for x in rows if x["code"].upper() == target]
        if not rows:
            # Not in the not-closed registry -- still allow (e.g. a closed/archived
            # project the operator explicitly wants checked, per D-001 PHASE 2's
            # retroactive-sweep mandate). Surfaced, not silently refused.
            rows = [{"code": target, "status": "(not in not-closed registry -- "
                     "closed/archived/unregistered; PRD-delta can still run)"}]

    out = []
    for row in rows:
        code = row["code"]
        reg = registry_json(code)
        docs, source = find_prd_docs(code, reg)
        existing = [d for d in docs if d["exists"]]
        out.append({
            "code": code,
            "status": row.get("status"),
            "prd_found": bool(existing),
            "prd_count": len(existing),
            "prd_source": source,
            "prd_paths": [d["path"] for d in existing],
        })
    print(json.dumps(out, indent=2))


def cmd_evidence(args):
    code = args.project_evidence.upper()
    tc = _load_to_check_module()
    reg = registry_json(code)
    docs, source = find_prd_docs(code, reg)
    prd_docs = []
    for d in docs:
        text = None
        if d["exists"]:
            text = Path(d["path"]).read_text(encoding="utf-8", errors="replace")
        prd_docs.append({"path": d["path"], "label": d["label"], "date": d["date"],
                          "exists": d["exists"], "text": text})
    existing_docs = [d for d in prd_docs if d["exists"]]
    tos = project_tos(code, tc)
    commits = project_commits(code)
    bundle = {
        "code": code,
        "prd_found": bool(existing_docs),
        "prd_source": source,
        "prd_docs": prd_docs,
        "registry": reg,
        "to_count": len(tos),
        "tos": tos,
        "commit_count": len(commits),
        "commits": commits,
    }
    print(json.dumps(bundle, indent=2, default=str))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-scope", action="store_true")
    ap.add_argument("--evidence", dest="project_evidence", metavar="CODE")
    ap.add_argument("--all", action="store_true", help="hot + cold (list-scope only)")
    ap.add_argument("--project", metavar="CODE", help="scope to one project code")
    args = ap.parse_args()

    if args.project_evidence:
        cmd_evidence(args)
    elif args.list_scope:
        cmd_list_scope(args)
    else:
        ap.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()
