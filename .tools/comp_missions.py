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
    rng = ["--since", since] if not since.startswith("REF:") else [since[4:] + "..HEAD"]
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


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-missions")
    ap.add_argument("cmd", choices=["scan", "json"], nargs="?", default="scan")
    ap.add_argument("--since", default="midnight")
    ap.add_argument("--until", default=None)
    ap.add_argument("--limit", type=int, default=20)
    a = ap.parse_args()
    r = scan(a.since, a.until)
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
