#!/usr/bin/env python3
"""comp-missions -- attribute commits to mission sub-groups and report ACTIVITY.

OWNER 0.0.0_AB_MSTR. Index: org/tier0/missions.yaml. Prose register: org/tier0/MISSIONS.md.

    >> COMMIT ACTIVITY IS NOT PROGRESS. <<

This tool reports what was TOUCHED. It can never report whether a thing WORKS -- that needs an
exercised run, which a commit scanner structurally cannot see. So it writes ACTIVITY only and
never touches a DECIDED/BUILT/SERVING stance, a FRONTIER, or a BLOCKED-ON.

Attribution precedence: DECLARED trailer (authoritative) -> DERIVED path globs (advisory) ->
UNMAPPED (first-class, always printed). A commit deriving to >1 sub-group is AMBIGUOUS and is
reported as such rather than tie-broken -- inventing a winner would manufacture precision the
evidence does not carry.

OUTPUT CONTRACT (INFRASTRUCTURE.TOOLS.O2, C1-C4): every count prints its denominator in-band; bounded
output says so with a visible token; an EMPTY result is distinguishable from a FAILED one.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import hashlib
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
INDEX = REPO / "org" / "tier0" / "missions.yaml"


def _run(args: list[str]) -> str:
    r = subprocess.run(args, cwd=str(REPO), capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit("comp-missions: git failed: %s\n%s" % (" ".join(args), r.stderr.strip()))
    return r.stdout


def load_index() -> dict:
    if not INDEX.exists():
        raise SystemExit("comp-missions: missing index %s" % INDEX)
    try:
        import yaml  # type: ignore
    except ImportError:
        raise SystemExit("comp-missions: pyyaml not available; cannot parse the index")
    return yaml.safe_load(INDEX.read_text(encoding="utf-8"))


def subgroups(idx: dict) -> dict:
    out = {}
    for gname, g in (idx.get("groups") or {}).items():
        for sid, sg in (g.get("subgroups") or {}).items():
            sg = dict(sg or {})
            sg["group"] = gname
            out[sid] = sg
    return out


def classify(path: str, rules: dict) -> str | None:
    for kind in ("code", "doc"):
        for pref in rules.get(kind, []):
            if path.startswith(pref):
                return kind
    return None


def commits(since: str, until: str | None) -> list[dict]:
    # SENTINEL (\x02) closes the metadata block. %b is MULTI-LINE, so partitioning the chunk at
    # its first newline lands INSIDE the body and silently drops the commit. That bug returned
    # "1 commit" against a true 85 on first run -- caught only by a positive control, and it is
    # the same broken-retrieval class this tool reports on. Do not "simplify" this away.
    # rec goes FIRST, not last: --name-only prints the file list AFTER the format string, so a
    # trailing separator pushes every commit's files into the NEXT record. That produced a clean,
    # confident 100%-unmapped table -- a wrong answer with no error, which is worse than a crash.
    sep, rec, end = "\x1f", "\x1e", "\x02"
    fmt = rec + sep.join(["%H", "%h", "%aI", "%an", "%s", "%b"]) + end
    # RANGE SELECTION. A sha range is preferred over --since for the incremental path because
    # AUTHOR-DATE IS NOT MONOTONIC ACROSS MERGES: a commit merged in from another branch can carry
    # an author-date older than the watermark and would be silently skipped by a time filter.
    # `<sha>..HEAD` walks the commit DAG and cannot miss an ancestor. Same class as the
    # timestamp traps this estate already has laws about.
    if since.startswith("RANGE:"):
        rng = [since[6:]]
    elif since.startswith("REF:"):
        rng = [since[4:] + "..HEAD"]
    else:
        rng = ["--since", since]
    raw = _run(["git", "log", "--no-merges", "--pretty=format:" + fmt, "--name-only"] + rng)
    out = []
    for chunk in raw.split(rec):
        if not chunk.strip():
            continue
        meta, _, files = chunk.partition(end)
        parts = meta.split(sep)
        if len(parts) < 6:
            continue
        sha, short, iso, author, subject, body = parts[:6]
        sha = sha.lstrip("\n")
        paths = [f.strip() for f in files.splitlines() if f.strip()]
        if until and iso > until:
            continue
        out.append({"sha": sha, "short": short, "iso": iso, "author": author.strip(),
                    "subject": subject, "body": body, "paths": paths})
    return out


def is_meta(c: dict, metas: list) -> bool:
    if not c["paths"]:
        return False
    for p in c["paths"]:
        hit = any(fnmatch.fnmatch(p, m) or (m.endswith("/**") and p.startswith(m[:-3] + "/"))
                  for m in metas)
        if not hit:
            return False
    return True


def attribute(c: dict, sgs: dict) -> tuple[list[str], str]:
    for line in (c["body"] or "").splitlines():
        if line.lower().startswith("mission:"):
            tag = line.split(":", 1)[1].strip()
            if tag in sgs:
                return [tag], "declared"
    hits = set()
    for sid, sg in sgs.items():
        for pat in sg.get("paths") or []:
            for p in c["paths"]:
                if fnmatch.fnmatch(p, pat) or (pat.endswith("/**") and p.startswith(pat[:-3] + "/")):
                    hits.add(sid)
                    break
            if sid in hits:
                break
    if not hits:
        return [], "unmapped"
    return sorted(hits), ("derived" if len(hits) == 1 else "ambiguous")


def scan(since: str, until: str | None) -> dict:
    idx = load_index()
    sgs = subgroups(idx)
    rules = idx.get("classify") or {}
    metas = idx.get("meta_paths") or []
    cs = commits(since, until)
    per = defaultdict(lambda: {"commits": 0, "code": 0, "doc": 0,
                               "authors": Counter(), "declared": 0, "derived": 0,
                               "newest": None, "newest_sha": None})
    modes = Counter()
    unmapped, ambiguous = [], []
    for c in cs:
        ids, mode = attribute(c, sgs)
        if mode == "unmapped" and is_meta(c, metas):
            mode = "governance"
        modes[mode] += 1
        if mode in ("unmapped", "governance"):
            if mode == "unmapped":
                unmapped.append(c)
            continue
        if mode == "ambiguous":
            ambiguous.append((c, ids))
        for sid in ids:
            e = per[sid]
            e["commits"] += 1
            e["authors"][c["author"]] += 1
            e[mode if mode in ("declared", "derived") else "derived"] += 1
            for p in c["paths"]:
                k = classify(p, rules)
                if k:
                    e[k] += 1
            if e["newest"] is None or c["iso"] > e["newest"]:
                e["newest"], e["newest_sha"] = c["iso"], c["short"]
    head = _run(["git", "log", "-1", "--pretty=format:%h\x1f%aI\x1f%an\x1f%s"]).split("\x1f")
    return {"total": len(cs), "per": {k: dict(v, authors=dict(v["authors"])) for k, v in per.items()},
            "modes": dict(modes), "unmapped": unmapped, "ambiguous": ambiguous,
            "subgroups": sgs, "since": since,
            "head": {"short": head[0], "iso": head[1], "author": head[2], "subject": head[3]}}


def fmt_report(r: dict, limit: int) -> str:
    L = []
    h = r["head"]
    L.append("comp-missions ACTIVITY -- window since %s" % r["since"])
    L.append("ANCHOR (HEAD at scan time): %s  %s  %s" % (h["short"], h["iso"], h["author"]))
    L.append("            %s" % h["subject"][:96])
    L.append("")
    tot = r["total"]
    L.append("COMMITS IN WINDOW: %d   attribution: %s" % (
        tot, ", ".join("%s=%d" % (k, v) for k, v in sorted(r["modes"].items())) or "none"))
    un = r["modes"].get("unmapped", 0)
    gov = r["modes"].get("governance", 0)
    mapped = tot - un - gov
    denom = tot - gov
    pct = (100.0 * un / denom) if denom else 0.0
    L.append("MISSION-ATTRIBUTABLE DENOMINATOR: %d of %d  (%d governance/meta EXCLUDED -- register"
             " upkeep, ledger, law, comms: correctly unattributed, NOT a blind spot)" % (denom, tot, gov))
    L.append("MAPPED %d of %d   UNMAPPED %d (%.0f%% of the attributable denominator)"
             "  <- unmapped is a first-class outcome, not a rounding error" % (mapped, denom, un, pct))
    L.append("")
    L.append("%-30s %7s %6s %5s  %-26s %s" % ("SUB-GROUP", "COMMITS", "code", "doc", "NEWEST", "TOP AUTHOR"))
    L.append("-" * 110)
    rows = sorted(r["per"].items(), key=lambda kv: -kv[1]["commits"])
    for sid, e in rows:
        top = max(e["authors"].items(), key=lambda kv: kv[1])[0] if e["authors"] else "-"
        L.append("%-30s %7d %6d %5d  %-26s %s" % (
            sid, e["commits"], e["code"], e["doc"],
            (e["newest"] or "")[:19] + " " + (e["newest_sha"] or ""), top))
    for sid in r["subgroups"]:
        if sid not in r["per"]:
            L.append("%-30s %7d %6d %5d  %-26s %s" % (sid, 0, 0, 0, "-- NO ACTIVITY --", "-"))
    if r["ambiguous"]:
        L.append("")
        L.append("AMBIGUOUS (%d) -- derived to >1 sub-group; REPORTED, never tie-broken:" % len(r["ambiguous"]))
        for c, ids in r["ambiguous"][:limit]:
            L.append("  %s  %-28s %s" % (c["short"], ",".join(ids), c["subject"][:60]))
        if len(r["ambiguous"]) > limit:
            L.append("  ... showing %d of %d (bounded)" % (limit, len(r["ambiguous"])))
    if r["unmapped"]:
        L.append("")
        L.append("UNMAPPED (%d of %d) -- no trailer, no path match. These are the register's blind spot:"
                 % (len(r["unmapped"]), tot))
        for c in r["unmapped"][:limit]:
            L.append("  %s  %-22s %s" % (c["short"], c["author"][:22], c["subject"][:64]))
        if len(r["unmapped"]) > limit:
            L.append("  ... showing %d of %d (bounded)" % (limit, len(r["unmapped"])))
    return "\n".join(L)



WATERMARK = REPO / "org" / "missions" / ".watermark.json"


def config_fingerprint(idx: dict) -> str:
    """Hash ONLY the parts of the index that can change a commit's attribution.

    THE POINT: a commit is immutable (no rebase -- gate-enforced), but its ATTRIBUTION is a
    function of (commit x index). Edit a path glob, add a sub-group, change meta_paths, and rows
    already written may now belong somewhere else. Incremental append would never revisit them and
    the file would silently disagree with its own index. So the fingerprint FORCES a rebuild when
    the rules move -- the caller does not get to forget.

    Deliberately EXCLUDES attach/holes/title/notes: those are prose about a sub-group, not inputs
    to attribution, and hashing them would trigger pointless full rebuilds on every edit.
    """
    material = {}
    for sid, sg in subgroups(idx).items():
        material[sid] = sorted(sg.get("paths") or [])
    material["__meta_paths__"] = sorted(idx.get("meta_paths") or [])
    material["__trailer__"] = (idx.get("attribution") or {}).get("declared_trailer", "")
    blob = json.dumps(material, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def read_watermark() -> dict:
    if not WATERMARK.exists():
        return {}
    try:
        return json.loads(WATERMARK.read_text(encoding="utf-8"))
    except Exception:
        return {}


def load_existing(d) -> tuple[list, set]:
    f = d / "commits.jsonl"
    if not f.exists():
        return [], set()
    rows, seen = [], set()
    for ln in f.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        try:
            r = json.loads(ln)
        except Exception:
            continue          # a corrupt line is dropped, and the count difference shows in the report
        if r.get("sha") in seen:
            continue          # dedupe: re-emitting the same range must be idempotent
        seen.add(r.get("sha"))
        rows.append(r)
    return rows, seen


# ---------------------------------------------------------------------------
# emit -- write the org/missions/ tree.
#
# LAYOUT: org/missions/{GROUP}/{SUB_GROUP}/
#     commits.jsonl   MACHINE-OWNED, append-only. One JSON record per attributed commit.
#                     Rewritten wholesale each emit from git, which IS the source of truth --
#                     so it can never drift from the repo. Never hand-edit.
#     state.yaml      HUMAN/AGENT-OWNED. Stance, frontier, blocked-on, attach, holes.
#                     emit CREATES it if absent and NEVER overwrites it. The machine has no
#                     business writing a stance: BUILT anchors on an exercised run, which a
#                     commit scanner structurally cannot see.
#     execsum.yaml    MSTR-OWNED prose + the commit it was written against.
#                     emit refreshes only `anchor_*` and `activity`; `prose` is left alone and
#                     flagged STALE when the anchor moves.
# ---------------------------------------------------------------------------

MISSIONS_DIR = REPO / "org" / "missions"


def _yaml_str(v: str) -> str:
    return json.dumps(v, ensure_ascii=False)


def emit(since: str, until: str | None, rebuild: bool = False) -> str:
    idx = load_index()
    sgs = subgroups(idx)
    fp = config_fingerprint(idx)
    wm = read_watermark()
    prior_sha, prior_fp = wm.get("last_sha"), wm.get("config_fingerprint")

    if rebuild:
        mode, reason = "FULL", "--rebuild requested"
    elif not prior_sha:
        mode, reason = "FULL", "no watermark (first emit)"
    elif prior_fp != fp:
        mode, reason = "FULL", ("attribution rules CHANGED (%s -> %s) -- every prior row may re-map"
                                % (prior_fp or "none", fp))
    else:
        mode, reason = "INCREMENTAL", "watermark %s..HEAD" % prior_sha[:10]

    # A FULL rebuild MUST scan ALL history, never the caller's --since. Otherwise a rules-change
    # rebuild silently TRUNCATES commits.jsonl to whatever window happened to be on the command
    # line -- measured: a forced rebuild with the default --since cut 162 rows to 27 and 472 to 63,
    # with no error. The repair path destroying the data it was repairing is the worst shape there
    # is, so FULL ignores --since by construction rather than by discipline.
    scan_since = "RANGE:HEAD" if mode == "FULL" else ("RANGE:%s..HEAD" % prior_sha)
    r = scan(scan_since, until)
    cs = commits(scan_since, until)
    by_sg = defaultdict(list)
    for c in cs:
        # NOTE `amode` not `mode`: `mode` is the FULL/INCREMENTAL flag decided above. Rebinding it
        # here silently sent FULL down the incremental branch and printed "MODE: unmapped".
        # Caught only because the header prints the mode in-band -- a mode that is never displayed
        # is a mode nobody can see is wrong.
        ids, amode = attribute(c, sgs)
        for sid in ids:
            by_sg[sid].append((c, amode))

    out = []
    for sid, sg in sgs.items():
        group, sub = sid.split(".", 1)
        d = MISSIONS_DIR / group / sub
        d.mkdir(parents=True, exist_ok=True)

        # commits.jsonl -- machine-owned. INCREMENTAL: prior rows are immutable (no rebase) and are
        # kept as-is; only new commits are added, deduped by sha. FULL: rewritten from git.
        prior_rows, seen = ([], set()) if mode == "FULL" else load_existing(d)
        recs = [json.dumps(x, ensure_ascii=False) for x in prior_rows]
        added = 0
        for c, amode in sorted(by_sg.get(sid, []), key=lambda x: x[0]["iso"], reverse=True):
            if c["sha"] in seen:
                continue
            seen.add(c["sha"])
            added += 1
            recs.insert(0, json.dumps({
                "sha": c["sha"], "short": c["short"], "time": c["iso"],
                "author": c["author"], "subject": c["subject"],
                "attribution": amode, "files": len(c["paths"]),
                "paths": c["paths"][:40],
                "paths_truncated": max(0, len(c["paths"]) - 40),
            }, ensure_ascii=False))
        (d / "commits.jsonl").write_text(
            ("\n".join(recs) + "\n") if recs else "", encoding="utf-8")

        # state.yaml -- created once, never overwritten
        sp = d / "state.yaml"
        if not sp.exists():
            lines = [
                "# state.yaml -- HUMAN/AGENT-OWNED. `comp-missions emit` never overwrites this file.",
                "# The machine cannot write a stance: BUILT anchors on an EXERCISED RUN, and a commit",
                "# scanner cannot see a run. Anything below requiring judgment stays here.",
                "sub_group: %s" % sid,
                "title: %s" % _yaml_str(sg.get("title") or sub),
                "version: v1.0",
                "stance:",
                "  decided: UNASSESSED   # NO | PARTIAL | YES | UNASSESSED   (+ anchor)",
                "  built: UNASSESSED",
                "  serving: UNASSESSED",
                "  anchors: []",
                "frontier: \"\"        # the ONE next thing. Not a plan.",
                "blocked_on: \"\"       # a named owner, a named sovereign call, or empty",
                "attach: %s" % json.dumps(sg.get("attach") or [], ensure_ascii=False),
                "holes: %s" % json.dumps(sg.get("holes") or [], ensure_ascii=False),
                "grounded: \"\"        # date + what it was re-derived against",
            ]
            sp.write_text("\n".join(lines) + "\n", encoding="utf-8")

        # execsum.yaml -- anchor + activity machine-refreshed; prose preserved
        e = r["per"].get(sid, {})
        prose, prose_anchor = "", ""
        ep = d / "execsum.yaml"
        if ep.exists():
            txt = ep.read_text(encoding="utf-8")
            for ln in txt.splitlines():
                if ln.startswith("prose_written_against:"):
                    prose_anchor = ln.split(":", 1)[1].strip()
            if "prose: |" in txt:
                prose = txt.split("prose: |", 1)[1]
        h = r["head"]
        stale = bool(prose.strip()) and prose_anchor and prose_anchor != h["short"]
        body = [
            "# execsum.yaml -- MSTR-owned. `anchor_*` and `activity` are machine-refreshed by",
            "# `comp-missions emit`; `prose` is written by MSTR and is NEVER machine-generated.",
            "sub_group: %s" % sid,
            "anchor_commit: %s" % h["short"],
            "anchor_time: %s        # author-time of that commit, NOT a wall clock" % h["iso"],
            "anchor_author: %s" % h["author"],
            "activity:",
            "  commits: %d" % (e.get("commits", 0)),
            "  code_files: %d" % (e.get("code", 0)),
            "  doc_files: %d" % (e.get("doc", 0)),
            "  newest_commit: %s" % (e.get("newest_sha") or "null"),
            "  newest_time: %s" % (e.get("newest") or "null"),
            "  contributors: %s" % json.dumps(e.get("authors") or {}, ensure_ascii=False),
            "prose_written_against: %s" % (prose_anchor or "null"),
            "prose_stale: %s   # true = a commit landed after the prose was written" % ("true" if stale else "false"),
            "prose: |",
        ]
        body.append((prose.rstrip("\n") if prose.strip() else "  (not yet written)"))
        ep.write_text("\n".join(body) + "\n", encoding="utf-8")
        out.append("%-32s total=%-5d +%-4d this emit" % (sid, len(recs), added))
    head_sha = _run(["git", "rev-parse", "HEAD"]).strip()
    WATERMARK.parent.mkdir(parents=True, exist_ok=True)
    WATERMARK.write_text(json.dumps({
        "last_sha": head_sha,
        "last_emit_anchor": r["head"]["short"],
        "last_emit_time": r["head"]["iso"],
        "config_fingerprint": fp,
        "mode": mode,
        "scanned_commits": r["total"],
    }, indent=2) + "\n", encoding="utf-8")

    hdr = ["comp-missions emit -> %s" % MISSIONS_DIR,
           "MODE: %s  (%s)" % (mode, reason),
           "anchor %s @ %s" % (r["head"]["short"], r["head"]["iso"]),
           "scanned %d commit(s) this pass; config fingerprint %s" % (r["total"], fp),
           "state.yaml preserved; execsum prose preserved",
           ""]
    return "\n".join(hdr + out)


# ---------------------------------------------------------------------------
# compile -- generate org/missions/MISSIONS.md from the tree.
#
# MISSIONS.md IS A BUILD ARTIFACT. It is an AGGREGATION of the per-sub-group execsum.yaml +
# state.yaml, ordered by ACTIVITY INTENSITY, and it is regenerated rather than edited. Andrew-direct:
# "compiled as much as possible rather than hand-written so that it does not go stale."
#
# Nothing here is authored at compile time. Every sentence in the output already exists in a
# state.yaml or an execsum.yaml written deliberately by MSTR. The compiler ORDERS and SELECTS; it
# never composes -- because a compiler that writes prose is a compiler that can invent a stance.
# ---------------------------------------------------------------------------

_BOOL_BACK = {True: "YES", False: "NO", "true": "YES", "false": "NO"}


def _stance(v):
    """YAML 1.1 coerces bare YES/NO to booleans. A stance that silently becomes True/False is a
    corrupted stance, so normalise on READ as well as quoting on write -- belt and braces, because
    the write-side fix depends on nobody hand-editing the file back."""
    if isinstance(v, bool):
        return _BOOL_BACK[v]
    if v is None:
        return "?"
    return _BOOL_BACK.get(str(v).lower(), str(v))


def _load_yaml(path):
    try:
        import yaml
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}


def compile_md(recent_days: int = 14) -> str:
    import datetime
    idx = load_index()
    sgs = subgroups(idx)
    head = _run(["git", "log", "-1", "--pretty=format:%h\x1f%aI\x1f%an\x1f%s"]).split("\x1f")

    # cutoff for the RECENT window, derived from the newest commit in the tree (never a wall clock)
    newest = None
    per = {}
    for sid in sgs:
        grp, sub = sid.split(".", 1)
        d = MISSIONS_DIR / grp / sub
        rows = []
        f = d / "commits.jsonl"
        if f.exists():
            for ln in f.read_text(encoding="utf-8").splitlines():
                ln = ln.strip()
                if ln:
                    try:
                        rows.append(json.loads(ln))
                    except Exception:
                        pass
        st = _load_yaml(d / "state.yaml")
        ex = _load_yaml(d / "execsum.yaml")
        times = sorted((r.get("time") or "") for r in rows if r.get("time"))
        if times and (newest is None or times[-1] > newest):
            newest = times[-1]
        per[sid] = {"rows": rows, "state": st, "exec": ex, "newest": times[-1] if times else None}

    cutoff = ""
    if newest:
        try:
            cutoff = (datetime.datetime.fromisoformat(newest)
                      - datetime.timedelta(days=recent_days)).isoformat()
        except Exception:
            cutoff = ""

    for sid, e in per.items():
        e["recent"] = sum(1 for r in e["rows"] if cutoff and (r.get("time") or "") >= cutoff)
        e["total"] = len(e["rows"])
        e["authors"] = len({r.get("author") for r in e["rows"] if r.get("author")})

    order = sorted(per.items(), key=lambda kv: (-kv[1]["recent"], -kv[1]["total"], kv[0]))

    L = []
    L.append("# MISSIONS — Opal mission register")
    L.append("")
    L.append("    GENERATED ARTIFACT -- do NOT edit. `comp-missions compile` regenerates this file.")
    L.append("    Every sentence below is SELECTED from a state.yaml or execsum.yaml, never composed")
    L.append("    here: a compiler that writes prose is a compiler that can invent a stance.")
    L.append("")
    L.append("    ANCHOR COMMIT   %s" % head[0])
    L.append("    ANCHOR TIME     %s   (author-time, not a wall clock)" % head[1])
    L.append("    ANCHOR AUTHOR   %s" % head[2])
    L.append("    ORDERING        activity intensity -- commits in the last %d days, then total" % recent_days)
    L.append("    SOURCE          org/missions/{GROUP}/{SUB_GROUP}/{state,execsum}.yaml")
    L.append("")
    L.append("> **If the anchor is not HEAD, this file is history rather than state.** Re-run "
             "`comp-missions emit && comp-missions compile`.")
    L.append("")
    root = _load_yaml(MISSIONS_DIR / "GOALS.yaml")
    if root.get("root_goal"):
        rs = str(root.get("root_goal_status") or "PROPOSED")
        L.append("## ROOT GOAL")
        L.append("")
        if rs == "APPROVED":
            L.append("*approved %s by %s, %s*" % (root.get("root_goal_version") or "v1",
                                                  root.get("root_goal_approved_by") or "?",
                                                  root.get("root_goal_approved_at") or "?"))
        else:
            L.append("**%s — DRAFT, NOT sovereign intent**" % rs)
        L.append("")
        L.append("> %s" % " ".join(str(root["root_goal"]).split()))
        L.append("")
        L.append("---")
        L.append("")
    L.append("## Priority board — ordered by activity intensity")
    L.append("")
    L.append("| # | sub-group | recent | total | authors | DECIDED | BUILT | SERVING | blocked on |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for i, (sid, e) in enumerate(order, 1):
        st = e["state"].get("stance") or {}
        L.append("| %d | `%s` | **%d** | %d | %d | %s | %s | %s | %s |" % (
            i, sid, e["recent"], e["total"], e["authors"],
            _stance(st.get("decided")), _stance(st.get("built")), _stance(st.get("serving")),
            (e["state"].get("blocked_on") or "—")[:44] or "—"))
    L.append("")
    stale = [sid for sid, e in per.items() if str(e["exec"].get("prose_stale")).lower() == "true"]
    if stale:
        L.append("**PROSE STALE (a commit landed after the summary was written):** %s"
                 % ", ".join("`%s`" % x for x in stale))
    else:
        L.append("**All sub-group summaries are current to the anchor.**")
    L.append("")
    L.append("---")
    L.append("")

    for sid, e in order:
        st, ex = e["state"], e["exec"]
        stance = st.get("stance") or {}
        L.append("## %s — %s" % (sid, st.get("title") or sgs.get(sid, {}).get("title", "")))
        L.append("")
        if st.get("goal"):
            status = str(st.get("goal_status") or "PROPOSED")
            if status == "APPROVED":
                L.append("**GOAL** — *approved %s by %s, %s*" % (
                    st.get("goal_version") or "v1",
                    st.get("goal_approved_by") or "?", st.get("goal_approved_at") or "?"))
            else:
                L.append("**GOAL (%s — DRAFT, NOT sovereign intent)** — *%s*" % (
                    status, st.get("goal_version") or "v1"))
            L.append("")
            L.append("> %s" % " ".join(str(st["goal"]).split()))
            L.append("")
        L.append("    activity   %d commit(s) in the last %d days · %d total · %d author(s)"
                 % (e["recent"], recent_days, e["total"], e["authors"]))
        L.append("    newest     %s" % (e["newest"] or "— no activity —"))
        L.append("    stance     DECIDED %s · BUILT %s · SERVING %s"
                 % (_stance(stance.get("decided")), _stance(stance.get("built")), _stance(stance.get("serving"))))
        if st.get("version"):
            L.append("    version    %s" % st["version"])
        if st.get("priority"):
            L.append("    priority   %s" % " ".join(str(st["priority"]).split()))
        L.append("")
        if st.get("frontier"):
            L.append("**FRONTIER —** %s" % " ".join(str(st["frontier"]).split()))
            L.append("")
        if st.get("blocked_on"):
            L.append("**BLOCKED ON —** %s" % " ".join(str(st["blocked_on"]).split()))
            L.append("")
        prose = (ex.get("prose") or "").rstrip()
        if prose and "(not yet written)" not in prose:
            L.append(prose)
            L.append("")
        holes = st.get("holes") or []
        if holes:
            L.append("**HOLES — live work no project code covers (%d):**" % len(holes))
            for hh in holes:
                L.append("- %s" % " ".join(str(hh).split()))
            L.append("")
        if st.get("grounded"):
            L.append("*grounded: %s*" % " ".join(str(st["grounded"]).split()))
            L.append("")
        L.append("---")
        L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-missions")
    ap.add_argument("cmd", choices=["scan", "json", "emit", "compile"], nargs="?", default="scan")
    ap.add_argument("--since", default="midnight")
    ap.add_argument("--until", default=None)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--rebuild", action="store_true",
                    help="force a FULL rebuild of commits.jsonl (also forced automatically when the "
                         "attribution rules in missions.yaml change)")
    a = ap.parse_args()
    r = scan(a.since, a.until)
    if a.cmd == "compile":
        out = compile_md()
        (MISSIONS_DIR / "MISSIONS.md").write_text(out + "\n", encoding="utf-8")
        print("comp-missions compile -> %s  (%d lines)" % (MISSIONS_DIR / "MISSIONS.md",
                                                           out.count("\n") + 1))
        return 0
    if a.cmd == "emit":
        print(emit(a.since, a.until, a.rebuild))
        return 0
    if a.cmd == "json":
        r2 = dict(r)
        r2["unmapped"] = [{k: c[k] for k in ("short", "author", "subject", "iso")} for c in r["unmapped"]]
        r2["ambiguous"] = [{"short": c["short"], "ids": ids, "subject": c["subject"]} for c, ids in r["ambiguous"]]
        r2.pop("subgroups", None)
        print(json.dumps(r2, indent=2))
    else:
        print(fmt_report(r, a.limit))
    return 0


if __name__ == "__main__":
    sys.exit(main())
