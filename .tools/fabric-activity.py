#!/usr/bin/env python3
"""fabric-activity -- which box is working on which part of the estate, read from one shared store.

Andrew-direct 2026-10-08 ~16:5xZ (org/tier1_exec/4.0.0_SA_CRO/deliverables/
ANDREW_DIRECT_20261008_165xZ_CRO_LEADS_GRAPH_COHERENCE_BUILD_NO_CANONICAL_REGISTRATION.md): any box asks "who else is
working on this?" and gets the answer; Andrew gets an overlap map on request; the Dells write their own activity.

THE RECORD (schema fabric-activity/1): one JSON object per commit, written BY THE BOX THAT MADE IT, to
  s3://opal-313476888478-globgrph/fabric/activity/v1/dt=<YYYY-MM-DD>/box=<box>/<YYYYMMDDTHHMMSSZ>_<sha12>.json
  fields: when, box, box_claim (measured | inferred | absent), seat, committer, sha, branch, worktree, subject,
          verb (EDITS), files (capped), file_count, surfaces [{key, cls}], projects
The store sits in the graph's bucket OUTSIDE warehouse/ (the Iceberg tables and the head marker), so a record never
touches the served graph's build. It is an extension of the existing globgrph store (LGIC rule 30 non-application:
an existing pipeline's store; R19).

SUBCOMMANDS
  emit [--commit SHA]           write the record for one commit (the post-commit hook runs this, backgrounded)
  flush                         retry records spooled locally after a failed put
  who TARGET [--hours N]        who touched a surface or path, from every box (TARGET: a repo path or a surface key)
  overlap [--hours N] [--all]   surfaces with two or more boxes on them, ranked; --all keeps append-only surfaces
  boxes [--hours N]             per-box figures: commits, seats, surfaces, and how many another box is also on
  backfill --since ISO          write records for past non-merge commits on this branch, box INFERRED from serials
  surface PATH...               print the surface a path rolls up to (no network)

Never blocks a commit: emit has hard network timeouts, spools on any failure and exits 0. Read-only apart from its
own S3 prefix and its local state dir (.comp-graph/fabric-activity/, gitignored).
"""
import argparse
import concurrent.futures
import datetime as dt
import json
import os
import re
import subprocess
import sys

BUCKET = "opal-313476888478-globgrph"
PREFIX = "fabric/activity/v1"
SCHEMA = "fabric-activity/1"
FILE_CAP = 400

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or os.getcwd()
STATE = os.path.join(ROOT, ".comp-graph", "fabric-activity")
SPOOL = os.path.join(STATE, "spool")
CACHE = os.path.join(STATE, "cache")
LOG = os.path.join(STATE, "emit.log")

# Surface classes, highest stakes first. APPEND is built to take many writers and is left out of the overlap map.
CLS_RANK = {"INFRA": 0, "CODE": 1, "REGISTRY": 2, "TOOL": 3, "RECORD": 4, "APPEND": 9}

_APPEND_RE = re.compile(
    r"(/surprise[-_]channel/|/logs?/|/handoffs/|/inbox/|^org/mcp/|telemetry|audit[^/]*\.log$|\.log$|\.jsonl$"
    r"|/change_management/|/\.open_deploys/|agent-spawn-audit|/deliverables/ANDREW_DIRECT_)")


def surface(path):
    """(key, cls) for a repo path: the coarsest unit that still names one thing."""
    p = path.replace("\\", "/")
    while p.startswith("./"):
        p = p[2:]
    parts = p.split("/")
    if _APPEND_RE.search(p):
        return "append:" + (os.path.dirname(p) or p), "APPEND"
    if p.startswith("infra/aws/terraform/") and len(parts) >= 4:
        return "tf:" + parts[3], "INFRA"
    if p.startswith("infra/aws/lambda/") and len(parts) >= 4:
        return "lambda-src:" + parts[3], "CODE"
    if p.startswith("infra/aws/") and len(parts) > 3:
        return "infra:" + parts[2], "CODE"
    m = re.match(r"data/([^/]+)/scripts/([^/]+)/([^/]+)\.py$", p)
    if m:
        return "pipeline:%s:%s:%s" % m.groups(), "CODE"
    if p.startswith("data/") and len(parts) > 2:
        return "data:" + "/".join(parts[1:3]), "CODE"
    if p.startswith("infra/logic/registry/") or p == "org/standards/NAMING_SCHEMA.json":
        return "registry:" + parts[-1], "REGISTRY"
    if p.startswith("lib/"):
        return "lib:" + parts[1], "CODE"
    if p.startswith(".tools/git-hooks/"):
        return "tool:git-hooks/" + parts[2], "TOOL"
    if p.startswith(".tools/"):
        return "tool:" + parts[1], "TOOL"
    if p.startswith(".claude/skills/") and len(parts) > 3:
        return "skill:" + parts[2], "TOOL"
    if p.startswith(".claude/"):
        return "claude:" + parts[-1], "TOOL"
    if p.startswith("portal/") or p == "portal":
        return "portal:" + "/".join(parts[1:4]), "CODE"
    m = re.match(r"org/missions/(D\d+)/([^/]+)/([^/]+)/", p)
    if m:
        return "project:" + m.group(3), "RECORD"
    if p in ("CLAUDE.md", "org/XXX.md") or p.startswith("docs/doctrine/"):
        return "law:" + p, "RECORD"
    return "path:" + "/".join(parts[:3] if len(parts) > 3 else parts[:-1] or parts), "RECORD"


def projects_of(files):
    out = set()
    for f in files:
        m = re.match(r"org/missions/D\d+/[^/]+/([^/]+)/", f)
        if m:
            out.add(m.group(1))
    return sorted(out)


def git(*args):
    r = subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return r.stdout


def this_box():
    sys.path.insert(0, os.path.join(ROOT, "lib"))
    try:
        import devices  # noqa: E402
        name, _basis = devices.this_device()
        return (name, "measured") if name else ("unresolved", "absent")
    except Exception:
        return "unresolved", "absent"


INFER_REV = 2
_PLACEMENT = None


def _placement():
    """project code -> box, from each project.json's `placement` (else `fabric`), resolved by the device register."""
    global _PLACEMENT
    if _PLACEMENT is None:
        _PLACEMENT = {}
        sys.path.insert(0, os.path.join(ROOT, "lib"))
        try:
            import devices  # noqa: E402
            import glob
            for f in glob.glob(os.path.join(ROOT, "org", "missions", "D*", "*", "*", "project.json")):
                try:
                    d = json.load(open(f, encoding="utf-8"))
                except Exception:
                    continue
                code = d.get("project_code") or os.path.basename(os.path.dirname(f))
                box = devices.resolve(str(d.get("placement") or ""), None) or devices.resolve(str(d.get("fabric") or ""), None)
                if box:
                    _PLACEMENT[code] = box
        except Exception:
            pass
    return _PLACEMENT


def _register_boxes():
    """The register's rows for boxes that are NOT the default-lane box, with each one's lane letters and trailing row digits
    (D1 -> "1"): the only things a serial or a committer name can say about a box. [] when the register cannot be read."""
    sys.path.insert(0, os.path.join(ROOT, "lib"))
    try:
        import devices  # noqa: E402
        rows = devices.devices()
    except Exception:
        return []
    out = []
    for d in rows:
        if d.get("lane_letters_default"):
            continue
        m = re.search(r"(\d+)$", d.get("row_coordinate") or "")
        out.append((d["name"], [x.upper() for x in d.get("lane_letters") or []], m.group(1) if m else ""))
    return out


def infer_box(author, committer):
    """Best guess of the box from serials (box_claim=inferred), by the device register: a box's name in the author or
    committer, or a lane ending in its row digits -> that box; a lane starting with one of its lane letters -> that box;
    a worker 0.9.0_WK_<CODE>~n -> its project's placement; any other agent serial -> the default-lane box (laptop); a human
    name -> unplaced (the laptop and site Z both commit under it)."""
    s = "%s|%s" % (author, committer)
    boxes = _register_boxes()
    for name, _letters, _digits in boxes:
        if re.search(re.escape(name), s, re.I) or committer.strip().lower() == name.lower():
            return name
    m = re.match(r"0\.9\.0_WK_([A-Z0-9_]+)~", author)
    if m:
        return _placement().get(m.group(1), "unplaced")
    m = re.match(r"\d+\.\d+\.\d+_[A-Z]{2}_[A-Za-z0-9]+(?:~([A-Za-z]*)(\d*))?$", author.strip())
    if m:
        letters, digit = m.group(1) or "", m.group(2) or ""
        for name, lane_letters, _digits in boxes:
            if any(letters.upper().startswith(x) for x in lane_letters):
                return name
        for name, _letters, digits in sorted(boxes, key=lambda b: -len(b[2])):
            if digits and digit.endswith(digits):
                return name
        return _default_box()
    return "unplaced"


def _default_box():
    """The register's default-lane box: the one that runs every lane no other box claims."""
    sys.path.insert(0, os.path.join(ROOT, "lib"))
    try:
        import devices  # noqa: E402
        for d in devices.devices():
            if d.get("lane_letters_default"):
                return d["name"]
    except Exception:
        pass
    return "unplaced"


def build_record(sha, box, claim):
    fmt = "%H%x1f%an%x1f%cn%x1f%aI%x1f%P%x1f%s"
    head = git("show", "-s", "--format=" + fmt, sha).strip().split("\x1f")
    if len(head) < 6:
        return None
    full, author, committer, when, parents, subject = head[:6]
    if len(parents.split()) > 1:
        return None  # merges carry other commits' files; MERGED is a later verb
    files = [f for f in git("diff-tree", "--no-commit-id", "--name-only", "-r", "--root", full).splitlines() if f]
    when_utc = dt.datetime.fromisoformat(when).astimezone(dt.timezone.utc)
    surf = {}
    for f in files:
        k, c = surface(f)
        surf[k] = c
    return {
        "schema": SCHEMA,
        "when": when_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "box": box,
        "box_claim": claim,
        "seat": author,
        "committer": committer,
        "sha": full,
        "branch": git("rev-parse", "--abbrev-ref", "HEAD").strip(),
        "worktree": os.path.basename(ROOT),
        "subject": subject[:200],
        "verb": "EDITS",
        "infer_rev": INFER_REV if claim == "inferred" else None,
        "file_count": len(files),
        "files": files[:FILE_CAP],
        "surfaces": [{"key": k, "cls": c} for k, c in sorted(surf.items())],
        "projects": projects_of(files),
    }


def key_for(rec):
    t = rec["when"]
    return "%s/dt=%s/box=%s/%s_%s.json" % (PREFIX, t[:10], rec["box"], t.replace("-", "").replace(":", ""),
                                           rec["sha"][:12])


def s3():
    import boto3
    from botocore.config import Config
    return boto3.client("s3", config=Config(connect_timeout=5, read_timeout=10, retries={"max_attempts": 2}))


def log(line):
    os.makedirs(STATE, exist_ok=True)
    with open(LOG, "a", encoding="ascii", errors="replace") as fh:
        fh.write("%s %s\n" % (dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), line))


def put(client, rec):
    body = json.dumps(rec, ensure_ascii=True, separators=(",", ":")).encode("ascii")
    client.put_object(Bucket=BUCKET, Key=key_for(rec), Body=body, ContentType="application/json")


def spool(rec):
    os.makedirs(SPOOL, exist_ok=True)
    with open(os.path.join(SPOOL, rec["sha"][:12] + ".json"), "w", encoding="ascii") as fh:
        json.dump(rec, fh, ensure_ascii=True)


def cmd_flush(client=None, limit=50):
    if not os.path.isdir(SPOOL):
        return 0
    names = sorted(os.listdir(SPOOL))[:limit]
    if not names:
        return 0
    client = client or s3()
    sent = 0
    for n in names:
        path = os.path.join(SPOOL, n)
        try:
            with open(path, encoding="ascii") as fh:
                put(client, json.load(fh))
            os.remove(path)
            sent += 1
        except Exception as exc:  # stays spooled; next emit retries
            log("FLUSH-FAIL %s %s" % (n, type(exc).__name__))
            break
    if sent:
        log("FLUSHED %d" % sent)
    return sent


def cmd_emit(args):
    box, claim = this_box()
    rec = build_record(args.commit, box, claim)
    if rec is None:
        log("SKIP %s (merge or unreadable)" % args.commit)
        return 0
    try:
        client = s3()
        put(client, rec)
        log("OK %s %s files=%d" % (rec["sha"][:12], box, rec["file_count"]))
        cmd_flush(client)
    except Exception as exc:
        spool(rec)
        log("SPOOLED %s %s" % (rec["sha"][:12], type(exc).__name__))
    return 0


def cmd_backfill(args):
    shas = sorted(set(git("log", "--no-merges", "--format=%H", "--since=" + args.since, *args.rev).split()))
    client = s3()

    def one(sha):
        head = git("show", "-s", "--format=%an%x1f%cn", sha).strip().split("\x1f")
        rec = build_record(sha, infer_box(head[0], head[1] if len(head) > 1 else ""), "inferred")
        if rec:
            put(client, rec)
            return 1
        return 0

    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        n = sum(ex.map(one, shas))
    print("OK: backfilled %d of %d non-merge commits since %s (box_claim=inferred)" % (n, len(shas), args.since))
    return 0


def fetch(hours):
    """Every record in the window, all boxes; immutable objects are cached locally. One record per sha (measured wins)."""
    client = s3()
    now = dt.datetime.now(dt.timezone.utc)
    start = now - dt.timedelta(hours=hours)
    days = sorted({(start + dt.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((now - start).days + 2)})
    keys = []
    pag = client.get_paginator("list_objects_v2")
    for d in days:
        for page in pag.paginate(Bucket=BUCKET, Prefix="%s/dt=%s/" % (PREFIX, d)):
            for o in page.get("Contents", []):
                keys.append(o["Key"])
    os.makedirs(CACHE, exist_ok=True)

    def get(k):
        local = os.path.join(CACHE, k.replace("/", "__"))
        if os.path.exists(local):
            with open(local, encoding="ascii") as fh:
                return json.load(fh)
        body = client.get_object(Bucket=BUCKET, Key=k)["Body"].read()
        with open(local, "wb") as fh:
            fh.write(body)
        return json.loads(body)

    with concurrent.futures.ThreadPoolExecutor(16) as ex:
        recs = list(ex.map(get, keys))
    cutoff = start.strftime("%Y-%m-%dT%H:%M:%SZ")
    best = {}
    for r in recs:
        if r.get("when", "") < cutoff:
            continue
        prev = best.get(r["sha"])
        rank = (r.get("box_claim") == "measured", r.get("infer_rev") or 0)
        if prev is None or rank > (prev.get("box_claim") == "measured", prev.get("infer_rev") or 0):
            best[r["sha"]] = r
    since = "--since=" + (start - dt.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    trunk = set(git("rev-list", since, "origin/CLOUD").split())
    # per-box branches (PER_BOX_BRANCH_DESIGN_20261008, build row B4): every origin/box/* is read beside CLOUD
    boxrefs = [ln.strip() for ln in git("for-each-ref", "--format=%(refname)", "refs/remotes/origin/box/").splitlines()
               if ln.strip()]
    pushed = set(git("rev-list", since, *boxrefs).split()) if boxrefs else set()
    for r in best.values():
        # MERGED: on origin/CLOUD; PUSHED: on an origin/box/* branch, not yet integrated; else still only on its box
        r["merged"] = r["sha"] in trunk
        r["state"] = "MERGED" if r["merged"] else ("PUSHED" if r["sha"] in pushed else "on-box")
    return sorted(best.values(), key=lambda r: r["when"]), len(keys)


def trunk_age():
    t = git("log", "-1", "--format=%cI", "origin/CLOUD").strip()
    return t or "unknown"


_PATHS_RE = re.compile(r"^<paths>[ \t]*$(.*?)^</paths>[ \t]*$", re.S | re.M)
_STATUS_RE = re.compile(r"<status>\s*([^<\s]+)\s*</status>")
_ISSUED_RE = re.compile(r"<issued_to>\s*([^<]+?)\s*</issued_to>")
_TERMINAL_TO = {"complete", "superseded", "cancelled"}
_OPEN_DEPLOY_DONE = {"closed", "complete", "completed", "superseded", "rolled_back", "rolled-back", "cancelled"}


def _covers(declared, target, tkey):
    d = declared.strip().replace("\\", "/").rstrip("/").lstrip("./") if not declared.strip().startswith(".") else \
        declared.strip().replace("\\", "/").rstrip("/")
    if not d:
        return False
    t = target.rstrip("/")
    if d == t or t.startswith(d + "/") or d.startswith(t + "/"):
        return True
    return surface(d)[0] == tkey


def declares(target, tkey):
    """Open task orders whose <paths> cover the target (DECLARES), read from this box's tree."""
    import glob
    out = []
    place = _placement()
    for f in glob.glob(os.path.join(ROOT, "org", "missions", "D*", "*", "*", "task-orders", "*.md")):
        try:
            text = open(f, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        st = _STATUS_RE.search(text)
        if st and st.group(1).lower() in _TERMINAL_TO:
            continue
        hit = [ln.strip() for m in _PATHS_RE.finditer(text) for ln in m.group(1).splitlines()
               if ln.strip() and _covers(ln, target, tkey)]
        if hit:
            code = f.replace("\\", "/").split("/org/missions/")[1].split("/")[2]
            who = _ISSUED_RE.search(text)
            out.append((place.get(code, "unplaced"), code, os.path.basename(f), (who.group(1) if who else "?"),
                        (st.group(1) if st else "?"), hit[0]))
    return sorted(out)


def holds(target, tkey):
    """Open change-management entries whose title or leg targets name the target (HOLDS), this box's tree."""
    import glob
    needle = {target.rstrip("/"), tkey.split(":", 1)[-1]}
    out = []
    for f in glob.glob(os.path.join(ROOT, "org", "critical_paths", ".open_deploys", "*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if str(d.get("status", "")).lower() in _OPEN_DEPLOY_DONE:
            continue
        blob = " ".join([str(d.get("title", ""))] + [str(leg.get("target", "")) for leg in d.get("legs", [])])
        if any(n and n in blob for n in needle):
            out.append((d.get("author", "?"), d.get("slug", os.path.basename(f)), d.get("status", "?")))
    return out


def graph_context(tkey):
    """What the estate graph says the surface IS, through the served graph (needs the graph read token). One line per
    node kind with a count, plus the graph's own vintage line. Empty when the surface has no estate node."""
    if tkey.startswith("tf:"):
        q = ("MATCH (n:CloudNode) WHERE n.props CONTAINS '\"tf_module\": \"%s\"' "
             "RETURN n.node_type AS kind, count(*) AS n ORDER BY n DESC" % tkey[3:])
    elif tkey.startswith("pipeline:"):
        _, firm, tier, script = (tkey.split(":") + ["", "", ""])[:4]
        q = ("MATCH (n:CloudNode) WHERE n.node_id STARTS WITH 'pipeline:' AND n.node_id ENDS WITH ':%s' "
             "RETURN n.node_type AS kind, n.node_id AS id LIMIT 5" % script)
    elif tkey.startswith("portal:"):
        q = ("MATCH (n:CloudNode) WHERE n.node_id STARTS WITH 'module:%s' "
             "RETURN n.node_type AS kind, count(*) AS n" % tkey[len("portal:"):])
    elif tkey.startswith("lambda-src:"):
        q = ("MATCH (n:CloudNode) WHERE n.node_type = 'LAMBDA' AND n.name CONTAINS '%s' "
             "RETURN n.node_type AS kind, n.name AS id LIMIT 5" % tkey[len("lambda-src:"):])
    else:
        return []
    r = subprocess.run([sys.executable, os.path.join(ROOT, "infra", "aws", "globgrph", "kuzu_cli.py"), "--json", q],
                       capture_output=True, text=True, timeout=90)
    out = []
    vintage = [ln for ln in r.stderr.splitlines() if ln.startswith("VINTAGE")]
    try:
        rows = json.loads(r.stdout or "[]")
    except ValueError:
        rows = []
    for row in rows:
        out.append("  GRAPH  " + "  ".join("%s=%s" % kv for kv in row.items()))
    if not rows:
        out.append("  GRAPH  no estate node matched (or the graph is unreachable from this box: %s)"
                   % (r.stderr.strip().splitlines()[-1][:120] if r.stderr.strip() else "no output"))
    out += ["  " + v[:160] for v in vintage[:1]]
    return out


def cmd_who(args):
    t = args.target.replace("\\", "/")
    tkey = t if re.match(r"^[a-z-]+:", t) else surface(t)[0]
    recs, scanned = fetch(args.hours)
    hits = []
    for r in recs:
        files = [f for f in r.get("files", []) if f == t or f.startswith(t.rstrip("/") + "/")]
        if files or any(s["key"] == tkey for s in r.get("surfaces", [])):
            hits.append((r, files))
    boxes = sorted({r["box"] for r, _ in hits})
    onbox = sorted({r["box"] for r, _ in hits if not r.get("merged")})
    pushed = sorted({r["box"] for r, _ in hits if r.get("state") == "PUSHED"})
    print("WHO %s  (surface %s, last %dh)  %d commit(s) from %d box(es): %s   [records scanned %d]"
          % (t, tkey, args.hours, len(hits), len(boxes), ", ".join(boxes) or "-", scanned))
    print("  not yet on origin/CLOUD from: %s (of which pushed to a box branch: %s)   (origin/CLOUD as last fetched"
          " here: %s)" % (", ".join(onbox) or "none", ", ".join(pushed) or "none", trunk_age()))
    for r, files in hits[-args.limit:]:
        print("  %s  %-8s %-9s %-7s %-30s %s  %s" % (r["when"], r["box"], r["box_claim"],
                                                     r.get("state", "on-box"), r["seat"][:30],
                                                     r["sha"][:10], r["subject"][:64]))
    if len(hits) > args.limit:
        print("  ... %d earlier commit(s) not shown (--limit)" % (len(hits) - args.limit))
    dec = declares(t, tkey)
    print("  DECLARES  %d open task order(s) name it in <paths> (this box's tree)" % len(dec))
    for box, code, fname, who, st, path in dec[: args.limit]:
        print("    %-8s %-18s %-10s %-28s %s  (%s)" % (box, code[:18], st[:10], who[:28], fname[:60], path[:60]))
    hl = holds(t, tkey)
    print("  HOLDS     %d open deploy entr(ies) name it (this box's tree)" % len(hl))
    for author, slug, st in hl[: args.limit]:
        print("    %-28s %-22s %s" % (author[:28], st[:22], slug))
    if args.graph:
        for line in graph_context(tkey):
            print(line)
    return 0


def cmd_overlap(args):
    recs, scanned = fetch(args.hours)
    by = {}
    for r in recs:
        for s in r.get("surfaces", []):
            if s["cls"] in ("APPEND", "RECORD") and not args.all:
                continue
            e = by.setdefault(s["key"], {"cls": s["cls"], "boxes": {}, "last": ""})
            b = e["boxes"].setdefault(r["box"], {"n": 0, "seats": set(), "onbox": 0})
            b["n"] += 1
            b["onbox"] += 0 if r.get("merged") else 1
            b["seats"].add(r["seat"])
            e["last"] = max(e["last"], r["when"])
    rows = [(k, e) for k, e in by.items() if len([b for b in e["boxes"] if b != "unplaced"]) >= 2]
    rows.sort(key=lambda kv: (CLS_RANK.get(kv[1]["cls"], 5), -len(kv[1]["boxes"]), kv[1]["last"]), reverse=False)
    claims = {}
    for r in recs:
        claims[r["box_claim"]] = claims.get(r["box_claim"], 0) + 1
    print("OVERLAP last %dh: %d surface(s) with 2+ boxes, of %d surfaces touched; %d commits (%s) [records scanned %d]"
          % (args.hours, len(rows), len(by), len(recs), ", ".join("%s %d" % kv for kv in sorted(claims.items())),
             scanned))
    for k, e in rows[: args.limit]:
        parts = ["%s:%d%s" % (b, v["n"], ("(%d on-box)" % v["onbox"]) if v["onbox"] else "")
                 for b, v in sorted(e["boxes"].items())]
        print("  %-8s %-48s %s   last %s" % (e["cls"], k[:48], " ".join(parts), e["last"]))
    return 0


def cmd_boxes(args):
    """Per-box figures for the window: commits, seats, surfaces, and how many of its surfaces another box is also on."""
    recs, scanned = fetch(args.hours)
    per = {}
    surf_boxes = {}
    for r in recs:
        b = per.setdefault(r["box"], {"commits": 0, "seats": set(), "surfaces": set(), "last": "", "claims": set()})
        b["commits"] += 1
        b["seats"].add(r["seat"])
        b["last"] = max(b["last"], r["when"])
        b["claims"].add(r["box_claim"])
        for s in r.get("surfaces", []):
            if s["cls"] in ("APPEND", "RECORD"):
                continue
            b["surfaces"].add(s["key"])
            surf_boxes.setdefault(s["key"], set()).add(r["box"])
    print("BOXES last %dh: %d commits [records scanned %d]" % (args.hours, len(recs), scanned))
    print("  %-9s %8s %6s %9s %8s  %-20s %s" % ("box", "commits", "seats", "surfaces", "shared", "last", "claim"))
    for box, b in sorted(per.items(), key=lambda kv: -kv[1]["commits"]):
        shared = sum(1 for k in b["surfaces"] if len(surf_boxes.get(k, set()) - {"unplaced"}) >= 2)
        print("  %-9s %8d %6d %9d %8d  %-20s %s" % (box, b["commits"], len(b["seats"]), len(b["surfaces"]), shared,
                                                   b["last"], "+".join(sorted(b["claims"]))))
    return 0


def cmd_surface(args):
    for p in args.paths:
        k, c = surface(p)
        print("%-8s %s  <- %s" % (c, k, p))
    return 0


def main():
    ap = argparse.ArgumentParser(prog="fabric-activity", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("emit")
    e.add_argument("--commit", default="HEAD")
    sub.add_parser("flush")
    w = sub.add_parser("who")
    w.add_argument("target")
    w.add_argument("--hours", type=int, default=24)
    w.add_argument("--limit", type=int, default=40)
    w.add_argument("--graph", action="store_true", help="add what the estate graph says the surface is")
    o = sub.add_parser("overlap")
    o.add_argument("--hours", type=int, default=24)
    o.add_argument("--limit", type=int, default=40)
    o.add_argument("--all", action="store_true", help="include record folders and append-only files")
    x = sub.add_parser("boxes")
    x.add_argument("--hours", type=int, default=24)
    b = sub.add_parser("backfill")
    b.add_argument("--since", required=True)
    b.add_argument("--rev", nargs="*", default=["HEAD"])
    s = sub.add_parser("surface")
    s.add_argument("paths", nargs="+")
    a = ap.parse_args()
    return {"emit": cmd_emit, "flush": lambda _a: (cmd_flush(), 0)[1], "who": cmd_who, "overlap": cmd_overlap,
            "backfill": cmd_backfill, "surface": cmd_surface, "boxes": cmd_boxes}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
