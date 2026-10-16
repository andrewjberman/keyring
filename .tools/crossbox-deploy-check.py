#!/usr/bin/env python3
"""crossbox-deploy-check.py -- the three measurements a box runs before it deploys its own work, plus the open-deploy read
(NFRA_CTLPLN workstream SEATS, cell CT-s-3). READ-ONLY: it changes nothing and builds no alert or monitor.

    python .tools/crossbox-deploy-check.py --root <dir> [--target <address> ...] [--notices <dir>] [--serial <serial>]
        [--now <UTC, e.g. 2026-10-08T05:00:00Z>] [--repo-root <dir>]
        [--files <path> ... | --files-from <file|-> | --files-vs-trunk]
    python .tools/crossbox-deploy-check.py --list-deployable [--commit-range <a..b>] [--files-from <file|->] [--repo-root <dir>]

Andrew's word: the laptop needs to know what goes on across the devices, but not every commit/deploy/decision comes from
the laptop -- only when there is an open call, a potential project overlap, or a deploy that could upset another device's work.

  OPEN-CALL    an unfinished cross-box call (org/devices/crossbox/*.json, state OPEN or ACKED) or an open_calls row
               (org/devices/state/*/open_calls.json) that names this root by its PATH (infra/aws/terraform/<root> or
               <root>/), by a root named in its own roots field, or a project whose write set covers the root. A bare
               name in free text is NOT a match (CTO ruling on D2-S32; cell CT-ab-5). An open_calls row of kind act (an act
               only Andrew can do) matches ONLY through the roots its own roots field names, so an act row with no roots matches
               none (CTO ruling on NFRA_CTLPLN D2-S3). Line: OPEN-CALL calls_scanned= matched=.
  OVERLAP      a live project placed on ANOTHER box (project.json `placement`, else its `fabric` box) whose write set shares
               a path with the root -- .tools/placement-check.py's own read_projects() and overlaps(), imported.
  UPSET        a live deploy notice (org/devices/deploy_notices/<id>.json) that names the root: rule "no-apply" hits any
               apply; "targeted-only-excluding" hits an UNTARGETED apply and a targeted one that names a listed resource;
               an empty `resources` list means the whole root. An expired notice is ignored and listed as expired.
  OPEN-DEPLOY  another seat's open deploy on the root: org/critical_paths/.open_deploys/*.json at HEAD of EVERY live
               worktree (git worktree list --porcelain, then ls-tree), the per-worktree denominator printed. A worktree
               whose HEAD is contained in the shared trunk HEAD is STALE-MERGED and its sentinels are not counted; the
               trunk checkout itself (HEAD equal to trunk) is the control and always counts. Line: OPEN-DEPLOY
               worktrees_scanned= open= stale_merged=.

FILES MODE (--files, --files-from, --files-vs-trunk; AMENDMENT 1 of the cell's task order): OVERLAP is judged on the files a
push or deploy actually carries against another box's write set, never on a shared root -- a project hits only if one of THOSE
files is inside its write set (an empty list reads clear: "no file carried"). --files-vs-trunk makes the list the Terraform
files of --root that differ from the merge base with the shared branch (committed, staged, unstaged or untracked); when that
list is empty OVERLAP reads clear with the reason "no file of this root differs", and when the merge base cannot be resolved the
tool says so and falls back to the root alone. The same rule narrows the OPEN-CALL project-code match and, for a NON-Terraform
root, the OPEN-CALL path match (a call or row hits only if it names a carried file; MDPF_SECCLASS row D1-S23) and the
OPEN-DEPLOY match (a sentinel hits only if its text names a carried file). For a Terraform root the OPEN-DEPLOY limb
keeps matching the root: an apply works on the state of the whole root, so another seat's open deploy of the same root collides
whatever files differ. Without any of the three flags the old root-wide reading stands (the criterion CTs3-AC2 invocation).
--list-deployable prints what safe-deploy.sh's own core (safe_deploy_core.py detect_script_files + detect_bundle_member_files,
called the way its main() calls them) will deploy for the explicit files or the commit range: one `DEPLOYABLE <path>` per file,
one `DEPLOY-ROOT <data/pipeline>` per root, LAST line `DEPLOYABLE-COUNT n=<k>`; it measures nothing else.

An ABSENT file or directory reads clear, said so ("none recorded"). A file that EXISTS but cannot be parsed, or carries a key
this reader does not know, is NOT clear: it reads hit with the reason.
LAST line: CROSSBOX-DEPLOY device=<d> root=<name> open_call=<clear|hit> overlap=<clear|hit> upset=<clear|hit>
           open_deploy=<clear|hit> verdict=<CLEAR|STOP>
SC-e-92 (OPEN-DEPLOY): a sentinel that trunk (the HEAD of --repo-root) deleted, read stale at a lagging worktree HEAD, is STALE and
draws no hit (one STALE line per slug, with the deleting commit); a registered worktree whose directory is gone is VANISHED in the
denominator (vanished=) and is read through its branch ref (else its detached HEAD sha) at --repo-root: clear only when that ref was
read, else a hit. A sentinel trunk never carried is a deploy open on a branch and still counts.
Exit: 0 CLEAR, 1 STOP, 2 a usage error. CLEAR means this box acts and tells the laptop; STOP names what it hit and routes a
cross-box call (cell CT-s-6's tool).
"""
from __future__ import annotations

import datetime
import glob
import importlib.util
import json
import os
import re
import subprocess
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)
NOTICE_KEYS = {"id", "root", "resources", "rule", "until", "by", "reason", "record"}
NOTICE_RULES = ("no-apply", "targeted-only-excluding")
LIVE_CALL_STATES = {"OPEN", "ACKED"}
CLOSED_WORDS = {"CLOSED", "CLOSED-BOTH", "COMPLETE", "COMPLETED", "SUPERSEDED", "CANCELLED"}


def load_placement(repo_root: str):
    """placement-check.py is imported (its file name has a hyphen), never copied; ROOT is pointed at repo_root."""
    spec = importlib.util.spec_from_file_location("opal_placement_check", os.path.join(TOOLS, "placement-check.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.ROOT = repo_root
    return mod


def rel_root(root: str, repo_root: str) -> str:
    absolute = os.path.abspath(root if os.path.isabs(root) else os.path.join(os.getcwd(), root))
    try:
        rel = os.path.relpath(absolute, repo_root)
    except ValueError:
        rel = absolute
    if rel.startswith(".."):
        rel = root
    return rel.replace("\\", "/").strip("/")


def mention_patterns(rel: str) -> list:
    """Regexes that count as 'names this root' in FREE TEXT. A Terraform root is named by its full PATH only (a trailing '/'
    included): its bare name is a word, not the root (CTO ruling on D2-S32; a call that says 'rootx' is not about
    infra/aws/terraform/rootx). A non-Terraform root also keeps its last two components, as the data roots are named that way."""
    bounded = r"(?<![A-Za-z0-9_-])%s(?![A-Za-z0-9_-])"
    pats = [(bounded % re.escape(rel), rel)]
    parts = rel.split("/")
    if not rel.startswith("infra/aws/terraform/") and len(parts) >= 2:
        last = "/".join(parts[-2:])
        pats.append((bounded % re.escape(last), last))
    return pats


def roots_field_names(doc) -> list:
    """The root names a call or row carries in its OWN roots field (`roots` or `--roots`), normalised. Structured data, not text."""
    out = []
    if not isinstance(doc, dict):
        return out
    for key in ("roots", "--roots"):
        value = doc.get(key)
        if isinstance(value, list):
            items = value
        elif isinstance(value, str):
            items = re.split(r"[,\s]+", value)
        else:
            items = []
        out.extend(norm_file(str(x)).rstrip("/") for x in items if str(x).strip())
    return out


def roots_field_hit(doc, rel: str) -> str:
    """Non-empty when the doc's own roots field names this root: its full path (or a path under it), or for a Terraform root its name."""
    name = rel.split("/")[-1]
    tf = rel.startswith("infra/aws/terraform/")
    for entry in roots_field_names(doc):
        if entry == rel or entry.startswith(rel + "/") or (tf and entry == name):
            return "names the root in its roots field (%s)" % entry
    return ""


def project_field_hit(doc, codes) -> str:
    """Non-empty when the doc's own structured `project` field names one of the covering project codes. Structured data only:
    a project code in a subject or context is free text and does not count (CTO ruling on D2-S32)."""
    value = doc.get("project") if isinstance(doc, dict) else None
    if isinstance(value, str) and value.strip() in codes:
        return "names project %s in its project field, whose write set covers the root" % value.strip()
    return ""


def mentions(text: str, pats: list) -> str:
    """Free text names the root only by its path pattern (mention_patterns); a bare project code or a bare root name does not."""
    for pat, label in pats:
        if re.search(pat, text):
            return "names the root (token %s)" % label
    return ""


def parse_utc(text: str):
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%MZ"):
        try:
            return datetime.datetime.strptime(str(text).strip(), fmt)
        except ValueError:
            continue
    raise ValueError("not a UTC time like 2026-10-08T06:20:00Z: %r" % (text,))


def age_text(stamp, now) -> str:
    try:
        sec = int((now - parse_utc(str(stamp).replace("+00:00", "Z").split(".")[0].rstrip("Z") + "Z")).total_seconds())
    except Exception:
        return "age unknown (written_at %r)" % (stamp,)
    return "age %dh%02dm" % (sec // 3600, (sec % 3600) // 60)


def projects_covering(pc, dev, reg, rel: str, files=None) -> tuple:
    """([(code, placement_box, write_path, placement_field)], findings) for live projects whose write set overlaps rel --
    or, when files is a list (FILES MODE), overlaps one of THOSE files: the root alone no longer hits."""
    projects, findings = pc.read_projects(dev, reg)
    out = []
    for proj in projects:
        if files is None:
            hit = next((w for w in proj["writes"] if pc.overlaps(w, rel)), None)
        else:
            pair = next(((w, f) for w in proj["writes"] for f in files if pc.overlaps(w, f)), None)
            hit = "%s (carried file %s)" % pair if pair else None
        if not hit:
            continue
        field = None
        try:
            field = json.load(open(os.path.join(pc.ROOT, proj["home"], "project.json"), encoding="utf-8")).get("placement")
        except (OSError, ValueError):
            pass
        box = dev.resolve(str(field), reg) if field else None
        out.append((proj["code"], box or proj["box"], hit, field or "(no placement field; fabric %s)" % proj.get("fabric")))
    return out, findings


def cross_call_entries(repo_root) -> list:
    """(file name, call record, error) for every call under org/devices/crossbox, read by the one reader of the call files
    (.tools/crossbox-call.py, fold_dir). A crossbox/2 call is one entry: its from-side file with its answer file folded in."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crossbox-call.py")
    spec = importlib.util.spec_from_file_location("crossbox_call_reader_deploy", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.fold_dir(os.path.join(repo_root, "org", "devices", "crossbox"))


def is_act_row(row) -> bool:
    """An open_calls row of kind act (an act only Andrew can do), compared on the stripped, case-folded value. A row with no
    kind, or kind fork, is not one: it keeps every match rule."""
    return isinstance(row, dict) and str(row.get("kind", "")).strip().lower() == "act"


def measure_open_call(repo_root, rel, covering, now, files=None) -> tuple:
    """files None, or a Terraform root: a live call or row hits when its text names the root or a covering project. A
    non-Terraform root in FILES MODE: it hits only when it names a carried file or a project covering one, or (open_calls
    rows of any kind) its own roots field names the root (CTO ruling 3, NFRA_CTLPLN round 14). A crossbox call file keeps the
    files-only reading; the roots field is not read there (MDPF_SECCLASS row D1-S23: a one-key ship on data/black_diamond
    drew STOP hits from calls that named only the shared root token)."""
    narrow = files is not None and not rel.startswith("infra/aws/terraform/")
    pats = file_patterns(files) if narrow else mention_patterns(rel)
    codes = [c[0] for c in covering]
    lines, hits = [], []
    scanned = 0  # every call file read and every open_calls row read (closed or not): the denominator
    if narrow:
        lines.append("  files mode: a call hits only if it names one of the %d carried file(s) or a project covering one; a row "
                     "hits on those or on its own roots field, not the shared root" % len(files))
    # the calls are read by the ONE reader (.tools/crossbox-call.py fold_dir): a crossbox/2 call is its from-side file with
    # its answer file, one entry per call; a file the reader cannot read is an entry with an error, never a clear
    crossbox = cross_call_entries(repo_root)
    if not crossbox:
        lines.append("  org/devices/crossbox/*.json: none recorded (0 files) -- reads clear")
    for fname, call, err in crossbox:
        scanned += 1
        name = "org/devices/crossbox/%s" % fname
        if err is not None:
            hits.append("%s unreadable (%s): a file that exists and cannot be parsed is not clear" % (name, err))
            lines.append("  HIT %s" % hits[-1])
            continue
        try:
            state = str(call.get("state", "")).upper()
            if state not in LIVE_CALL_STATES:
                lines.append("  %s: state %s -- not live" % (name, state or "(none)"))
                continue
            body = ""
            if call.get("body_path"):
                try:
                    body = open(os.path.join(repo_root, call["body_path"]), encoding="utf-8", errors="replace").read()
                except OSError:
                    body = ""
            why = (roots_field_hit(call, rel) if not narrow else "") or project_field_hit(call, codes) \
                or mentions(json.dumps(call) + "\n" + body, pats)
        except Exception as exc:
            hits.append("%s unreadable (%s: %s): a file that exists and cannot be parsed is not clear" % (name, type(exc).__name__, exc))
            lines.append("  HIT %s" % hits[-1])
            continue
        if why:
            hits.append("%s (state %s, %s -> %s) %s" % (name, state, call.get("from_device"), call.get("to_device"), why))
            lines.append("  HIT %s" % hits[-1])
        else:
            lines.append("  %s: live (state %s) but does not name the root or its projects" % (name, state))
    states = sorted(glob.glob(os.path.join(repo_root, "org", "devices", "state", "*", "open_calls.json")))
    if not states:
        lines.append("  org/devices/state/*/open_calls.json: none recorded (0 files) -- reads clear")
    for path in states:
        name = os.path.relpath(path, repo_root).replace("\\", "/")
        try:
            doc = json.load(open(path, encoding="utf-8"))
            rows = doc.get("rows", [])
            age = age_text(doc.get("written_at"), now)
            lines.append("  %s: device=%s written_by=%s %s rows=%d" % (name, doc.get("device"), doc.get("written_by"), age, len(rows)))
            for row in rows:
                scanned += 1
                if str(row.get("state", "")).upper() in CLOSED_WORDS:
                    continue
                if is_act_row(row):
                    # CTO ruling (NFRA_CTLPLN D2-S3): an act row matches only through the roots its own roots field names.
                    hit = roots_field_hit(row, rel)
                    why = ("act row " + hit) if hit else ""
                else:
                    # files mode: a row of any kind matches through its own roots field too (CTO ruling 3, NFRA_CTLPLN round 14)
                    why = roots_field_hit(row, rel) or project_field_hit(row, codes) \
                        or mentions(json.dumps(row), pats)
                if why:
                    hits.append("%s row %s %s" % (name, row.get("id", "?"), why))
                    lines.append("  HIT %s" % hits[-1])
        except Exception as exc:
            hits.append("%s unreadable (%s: %s): not clear" % (name, type(exc).__name__, exc))
            lines.append("  HIT %s" % hits[-1])
    lines.append("OPEN-CALL calls_scanned=%d matched=%d" % (scanned, len(hits)))
    return hits, lines


def measure_overlap(dev_name, covering, findings, basis, files=None, files_note="") -> tuple:
    """files None = the old root-wide reading; a list = FILES MODE (an empty list has nothing to overlap: clear, with the reason)."""
    lines, hits = [], []
    if files is not None:
        lines.append("  files mode: %d file(s) carried (%s)" % (len(files), files_note))
        if not files:
            reason = files_note if files_note.startswith("no file") else "no file carried"
            return hits, lines + ["  %s -- reads clear" % reason]
    if dev_name is None:
        hits.append("this box is unresolved (%s): cannot say which placement is another box's" % basis)
        return hits, lines + ["  HIT %s" % hits[0]]
    for code, box, path, field in covering:
        if box and box != dev_name:
            hits.append("project %s is placed on %s (%s) and its write set names %s" % (code, box, field, path))
            lines.append("  HIT %s" % hits[-1])
        else:
            lines.append("  project %s placed on %s (%s) names %s -- this box or unplaced, not another box's" % (code, box, field, path))
    if not covering:
        what = "the root" if files is None else "the %d carried file(s)" % len(files)
        lines.append("  no live project's write set shares a path with %s (placement-check read_projects/overlaps)" % what)
    for finding in findings:
        lines.append("  placement finding: %s" % finding)
    return hits, lines


def target_hits(resources: list, targets: list) -> list:
    out = []
    for tgt in targets:
        bare = re.sub(r"\[[^\]]*\]$", "", tgt)
        for res in resources:
            if bare == res or bare.endswith("." + res) or res.endswith("." + bare) or tgt.startswith(res + "["):
                out.append((tgt, res))
    return out


def measure_upset(notices_dir, rel, targets, now) -> tuple:
    lines, hits = [], []
    files = sorted(glob.glob(os.path.join(notices_dir, "*.json")))
    if not files:
        lines.append("  %s: none recorded (0 notices) -- reads clear" % notices_dir.replace("\\", "/"))
    for path in files:
        name = os.path.basename(path)
        try:
            note = json.load(open(path, encoding="utf-8"))
            unknown = sorted(set(note) - NOTICE_KEYS)
            missing = sorted(NOTICE_KEYS - set(note))
            if unknown or missing:
                raise ValueError("keys unknown %s missing %s" % (unknown, missing))
            if note["rule"] not in NOTICE_RULES:
                raise ValueError("rule %r is not one of %s" % (note["rule"], list(NOTICE_RULES)))
            until = parse_utc(note["until"])
            if not isinstance(note["resources"], list):
                raise ValueError("resources is not a list")
        except Exception as exc:
            hits.append("notice %s unreadable (%s: %s): not clear" % (name, type(exc).__name__, exc))
            lines.append("  HIT %s" % hits[-1])
            continue
        if until <= now:
            lines.append("  notice %s EXPIRED at %s (now %s) -- ignored" % (note["id"], note["until"], now.strftime("%Y-%m-%dT%H:%M:%SZ")))
            continue
        nroot = str(note["root"]).replace("\\", "/").strip("/")
        if nroot != rel and not rel.startswith(nroot + "/") and not nroot.startswith(rel + "/"):
            lines.append("  notice %s live until %s names another root (%s) -- not this one" % (note["id"], note["until"], nroot))
            continue
        res = [str(r) for r in note["resources"]]
        base = "notice %s (by %s, until %s, rule %s) names root %s" % (note["id"], note["by"], note["until"], note["rule"], nroot)
        if note["rule"] == "no-apply" or not res:
            hits.append("%s%s: no apply of it is made until the notice expires" % (base, "" if res else " as a whole root"))
        elif not targets:
            hits.append("%s and this apply is UNTARGETED, so it would reach %s: it waits" % (base, ", ".join(res)))
        else:
            named = target_hits(res, targets)
            if named:
                hits.append("%s and this apply targets %s, which the notice excludes" % (base, "; ".join("%s (names %s)" % n for n in named)))
            else:
                lines.append("  notice %s live: this apply is TARGETED (%d target(s)) and names none of %s -- clear of it" % (note["id"], len(targets), ", ".join(res)))
                continue
        lines.append("  HIT %s" % hits[-1])
        lines.append("    reason: %s | record: %s" % (note["reason"], note["record"]))
    return hits, lines


def git_lines(repo_root, *args) -> tuple:
    proc = subprocess.run(["git", "-C", repo_root, *args], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    return proc.returncode, proc.stdout


def read_blobs(repo_root, shas) -> dict:
    """{sha: text or None} through ONE `git cat-file --batch` (the object store is shared by every worktree)."""
    out = {sha: None for sha in shas}
    if not shas:
        return out
    proc = subprocess.run(["git", "-C", repo_root, "cat-file", "--batch"], input=("\n".join(shas) + "\n").encode("ascii"),
                          capture_output=True, timeout=60)
    data, pos = proc.stdout, 0
    for sha in shas:
        end = data.find(b"\n", pos)
        if end < 0:
            break
        head = data[pos:end].split()
        if len(head) == 3 and head[1] == b"blob":
            size = int(head[2])
            out[sha] = data[end + 1:end + 1 + size].decode("utf-8", errors="replace")
            pos = end + 1 + size + 1
        else:
            pos = end + 1
    return out


def file_patterns(files: list) -> list:
    """Regexes that count as 'names a carried file': its full repo path, or its bare name (never __init__.py)."""
    pats = []
    for path in files:
        pats.append((re.escape(path), path))
        base = path.rsplit("/", 1)[-1]
        if base != "__init__.py" and len(base) >= 4:
            pats.append((r"(?<![A-Za-z0-9_/.-])%s(?![A-Za-z0-9_-])" % re.escape(base), base))
    return pats


def worktree_refs(porcelain: str) -> dict:
    """{worktree path: its branch ref (refs/heads/...), else its detached HEAD sha, else None} from `git worktree list --porcelain`."""
    refs, path = {}, None
    for ln in porcelain.splitlines():
        if not ln.strip():
            path = None
        elif ln.startswith("worktree "):
            path = ln[9:].strip()
            refs[path] = None
        elif path is not None and ln.startswith("branch "):
            refs[path] = ln[7:].strip()
        elif path is not None and ln.startswith("HEAD ") and refs.get(path) is None:
            refs[path] = ln[5:].strip()
    return refs


def listing_rows(listing: str) -> tuple:
    """(all rows, sentinel rows) of an ls-tree listing: a sentinel is a file whose name does not start with a dot."""
    entries = [ln.split(None, 3) for ln in listing.splitlines() if ln.strip()]
    return entries, [e for e in entries if len(e) == 4 and not os.path.basename(e[3].split("\t")[-1]).startswith(".")]


def worktree_heads(porcelain: str) -> dict:
    """{worktree path: its HEAD sha} from `git worktree list --porcelain` (a branch checkout or a detached one alike)."""
    heads, path = {}, None
    for ln in porcelain.splitlines():
        if not ln.strip():
            path = None
        elif ln.startswith("worktree "):
            path = ln[9:].strip()
        elif path is not None and ln.startswith("HEAD "):
            heads[path] = ln[5:].strip()
    return heads


def contained_in_trunk(repo_root, sha, trunk_sha) -> str:
    """'merged' when sha is an ancestor of trunk_sha (its checkout is contained in the shared trunk), 'open' when it is not, or when
    it IS the trunk (the shared tree's own sentinels are the control), 'error' when git cannot say (rc other than 0 or 1)."""
    if sha == trunk_sha:
        return "open"
    rc, _out = git_lines(repo_root, "merge-base", "--is-ancestor", sha, trunk_sha)
    return {0: "merged", 1: "open"}.get(rc, "error")


def measure_open_deploy(repo_root, rel, serial, files=None) -> tuple:
    """files None, or a Terraform root: a sentinel hits when its text names the root (the state of a whole root is what an apply
    works on). A non-Terraform root in FILES MODE: a sentinel hits only when its text names a carried file.
    A checkout whose HEAD is contained in the shared trunk HEAD is STALE-MERGED: its sentinels are printed and not counted."""
    narrow = files is not None and not rel.startswith("infra/aws/terraform/")
    pats = file_patterns(files) if narrow else mention_patterns(rel)
    lines, hits = [], []
    if narrow:
        lines.append("  files mode: a sentinel hits only if it names one of the %d carried file(s), not the shared root" % len(files))
    rc, out = git_lines(repo_root, "worktree", "list", "--porcelain")
    trees = [ln[9:].strip() for ln in out.splitlines() if ln.startswith("worktree ")] if rc == 0 else []
    refs = worktree_refs(out) if rc == 0 else {}
    heads = worktree_heads(out) if rc == 0 else {}
    if rc != 0 or not trees:
        hits.append("git worktree list failed (rc=%d): the open deploys of other seats cannot be read, so this is not clear" % rc)
        return hits, ["  HIT %s" % hits[0]]
    vanished = 0
    pending = []  # (tree, its HEAD sha, [(blob sha, path)] of its sentinels): the ancestry rule below decides which of them count
    for tree in trees:
        shown = tree.replace("\\", "/")
        gone = not os.path.isdir(tree)
        # SC-e-92 limb e, AMENDED (AMENDMENT 1, row D1-W81-S2): a registration whose directory is gone is read through its ref (branch,
        # else detached HEAD sha) at repo_root, exactly like a HEAD. A tree whose read fails is then RACE-CHECKED (below).
        ref = refs.get(tree) if gone else "HEAD"
        if ref:
            rc, listing = git_lines(repo_root if gone else tree, "ls-tree", "-r", ref, SENTINEL_DIR)
        else:
            rc, listing = 1, ""
        if rc != 0 or not ref:
            # The race between the list and this read (CLAUDE.md NEVER-2 names the per-tree read): a checkout removed in between is
            # VANISHED and not a hit; a checkout still listed (or whose path still exists) is unreadable, and that is a hit.
            why = ("ls-tree %s rc=%d" % (ref, rc)) if ref else "no branch or HEAD ref to read"
            rc2, out2 = git_lines(repo_root, "worktree", "list", "--porcelain")
            if rc2 != 0:
                hits.append("worktree %s: %s and the re-read of the worktree list failed (rc=%d): not clear" % (shown, why, rc2))
                lines.append("  HIT %s" % hits[-1])
                continue
            still = {ln[9:].strip() for ln in out2.splitlines() if ln.startswith("worktree ")}
            if tree not in still and not os.path.exists(tree):
                vanished += 1
                lines.append("  worktree %s: VANISHED during the read (listed, then removed)" % shown)
                continue
            hits.append("worktree %s: %s (not readable, not clear)" % (shown, why))
            lines.append("  HIT %s" % hits[-1])
            continue
        entries, sentinels = listing_rows(listing)
        if gone:
            vanished += 1
            lines.append("  worktree %s: VANISHED (registered, directory absent), read through %s: %d file(s), %d sentinel(s)" % (
                shown, ref, len(entries), len(sentinels)))
        else:
            lines.append("  worktree %s: %d file(s) at HEAD, %d sentinel(s) read" % (shown, len(entries), len(sentinels)))
        if sentinels:
            pending.append((tree, heads.get(tree), [(e[2], e[3].strip()) for e in sentinels]))
    # OPEN-DEPLOY ancestry (CTO ruling on D2-S32, cell CT-ab-5): a sentinel counts at a checkout only when that checkout's HEAD is NOT
    # contained in the shared trunk HEAD. A contained HEAD is STALE-MERGED and not counted. The trunk checkout (HEAD equal to trunk) is the
    # control and always counts. A HEAD that git cannot compare is not clear, so it counts.
    merged = []  # (tree, sha, rows) of every checkout whose HEAD is contained in trunk
    found = []  # (blob sha, path, tree) of the sentinel readings that are not excluded
    if pending:
        rc, trunk_out = git_lines(repo_root, "rev-parse", "--verify", "-q", "HEAD^{commit}")
        trunk_sha = trunk_out.strip() if rc == 0 else ""
        if not trunk_sha:
            hits.append("trunk HEAD does not resolve (rc=%d): a checkout contained in trunk cannot be told from an open one, so this is not clear" % rc)
            lines.append("  HIT %s" % hits[-1])
        for tree, sha, rows in pending:
            shown = tree.replace("\\", "/")
            verdict = contained_in_trunk(repo_root, sha, trunk_sha) if (sha and trunk_sha) else "open"
            if verdict == "error":
                hits.append("worktree %s: HEAD %s cannot be compared with trunk (merge-base): not clear" % (shown, (sha or "?")[:10]))
                lines.append("  HIT %s" % hits[-1])
                verdict = "open"
            if verdict == "merged":
                merged.append((tree, sha, rows))
                lines.append("  STALE-MERGED worktree %s: HEAD %s is contained in trunk %s; %d sentinel(s) not counted: %s" % (
                    shown, sha[:10], trunk_sha[:10], len(rows), ", ".join(path for _blob, path in rows)))
                continue
            found.extend((blob, path, tree) for blob, path in rows)
    open_checkouts = len(pending) - len(merged)
    # SC-e-92 limb d, TRUNK FIRST: the HEAD of repo_root is trunk. A sentinel that trunk does not carry, at a path trunk's history DOES
    # carry, was deleted at trunk: a worktree that has not taken the closing commit still reads it, so it is STALE and draws no hit.
    # A path trunk never carried is a deploy open on a worker's branch until the drain (CLAUDE.md NEVER-2) and counts as before. A
    # stale reading must also be a blob trunk once carried at that path: a sentinel re-opened on a branch under the same name carries
    # a blob trunk never had, so it stays a hit.
    stale_at = {}  # path -> (the trunk commit that deleted it, {blob shas trunk carried at that path})
    # The trunk listing is needed only when a sentinel was read: with none, there is nothing to call stale.
    rc, trunk = git_lines(repo_root, "ls-tree", "-r", "HEAD", SENTINEL_DIR) if found else (0, "")
    if rc != 0:
        hits.append("trunk HEAD ls-tree rc=%d: a stale sentinel cannot be told from a live one, so this is not clear" % rc)
        lines.append("  HIT %s" % hits[-1])
    else:
        at_trunk = {e[3].strip() for e in (ln.split(None, 3) for ln in trunk.splitlines() if ln.strip()) if len(e) == 4}
        for path in sorted({f[1] for f in found} - at_trunk):
            rc, log = git_lines(repo_root, "log", "-m", "--no-abbrev", "--raw", "--format=%H", "--", path)
            if rc != 0:
                hits.append("%s: git log at trunk HEAD rc=%d: not clear" % (path, rc))
                lines.append("  HIT %s" % hits[-1])
                continue
            commits, blobs_then = [], set()
            for ln in log.splitlines():
                if ln.startswith(":"):
                    blobs_then.update(ln[1:].split("\t")[0].split()[2:4])
                elif ln.strip():
                    commits.append(ln.strip())
            blobs_then.discard("0" * 40)
            if commits:
                stale_at[path] = (commits[0], blobs_then)
    blobs = read_blobs(repo_root, sorted({f[0] for f in found}))
    seen = set()
    readings = []  # one per distinct (path, blob) that parses: (slug, doc, why, path)
    stale = []  # (slug, path, deleting trunk commit, tree) for each stale reading
    for sha, path, tree in found:
        if (path, sha) in seen:
            continue
        seen.add((path, sha))
        text = blobs.get(sha)
        if path in stale_at and sha in stale_at[path][1]:
            stale.append((sentinel_slug(loaded_doc(text), path), path, stale_at[path][0], tree))
            continue
        if text is None:
            hits.append("%s (blob %s, first seen in %s) unreadable: not clear" % (path, sha[:10], tree))
            lines.append("  HIT %s" % hits[-1])
            continue
        try:
            doc = json.loads(text)
        except ValueError as exc:
            hits.append("%s is not JSON (%s): not clear" % (path, exc))
            lines.append("  HIT %s" % hits[-1])
            continue
        why = mentions(text, pats)
        if why and narrow:
            why = why.replace("names the root (token", "names a carried file (token")
        readings.append((sentinel_slug(doc, path), doc, why, path))
    # SC-e-89 limb c: one SLUG counts once however many statuses or worktrees it was read at. A slug is skipped when every
    # reading is closed, and its readings authored by the actor are skipped; otherwise it draws one hit iff a live reading of
    # another author names the carried file, built from the most recently opened such reading.
    by_slug, order = {}, []
    for slug, doc, why, path in readings:
        if slug not in by_slug:
            by_slug[slug] = []
            order.append(slug)
        by_slug[slug].append((doc, why, path))
    for slug in order:
        live = [r for r in by_slug[slug] if str(r[0].get("status", "")).upper() not in CLOSED_WORDS]
        if not live:
            continue
        named = [r for r in live if r[1] and not (serial and r[0].get("author") == serial)]
        if not named:
            continue
        doc, why, path = max(named, key=lambda r: str(r[0].get("opened_at") or ""))
        hits.append("open deploy %s (author %s, status %s, opened %s) %s" % (
            doc.get("slug", path), doc.get("author"), doc.get("status"), doc.get("opened_at"), why))
        lines.append("  HIT %s" % hits[-1])
    stale_by_slug, stale_count = {}, 0
    for slug, path, commit, tree in stale:
        stale_by_slug.setdefault(slug, []).append((path, commit, tree))
    for slug, rows in stale_by_slug.items():
        path, commit = rows[0][0], rows[0][1]
        if slug in by_slug:
            lines.append("  NOTE slug %s: a lagging HEAD reads %s, deleted at trunk by commit %s; the slug's other reading(s) are "
                         "judged as today, not counted as stale" % (slug, path, commit))
        else:
            stale_count += 1
            lines.append("  STALE slug %s: %s deleted at trunk by commit %s, read at HEAD of %d worktree(s): closed at trunk, "
                         "draws no hit" % (slug, path, commit, len({r[2] for r in rows})))
    reads = sum(len(rows) for _tree, _sha, rows in pending)
    lines.append("  denominator: %d worktree(s), %d sentinel read(s), %d distinct (path, blob), %d distinct slug(s), vanished=%d, "
                 "stale=%d" % (len(trees), reads, len(seen), len(order), vanished, stale_count))
    lines.append("OPEN-DEPLOY worktrees_scanned=%d open=%d stale_merged=%d" % (len(trees), open_checkouts, len(merged)))
    return hits, lines


def norm_file(path: str) -> str:
    path = path.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


TF_SUFFIXES = (".tf", ".tfvars", ".tf.json", ".hcl", ".tftpl")
SENTINEL_DIR = "org/critical_paths/.open_deploys/"


def trunk_files(repo_root, rel) -> tuple:
    """(files or None, note): the Terraform files of rel that differ from the merge base with the shared branch."""
    base = ""
    for cand in ("origin/CLOUD", "CLOUD", "origin/main", "main"):
        rc, out = git_lines(repo_root, "rev-parse", "--verify", "-q", cand + "^{commit}")
        if rc != 0:
            continue
        rc, out = git_lines(repo_root, "merge-base", "HEAD", cand)
        if rc == 0 and out.strip():
            base = out.strip().splitlines()[0]
            break
    if not base:
        return None, "the merge base with the shared branch cannot be resolved (origin/CLOUD, CLOUD, origin/main, main); the root alone is judged"
    rc1, changed = git_lines(repo_root, "diff", "--name-only", base, "--", rel)
    rc2, fresh = git_lines(repo_root, "ls-files", "--others", "--exclude-standard", "--", rel)
    if rc1 != 0 or rc2 != 0:
        return None, "git diff against the merge base failed (rc=%d/%d); the root alone is judged" % (rc1, rc2)
    names = sorted({norm_file(x) for x in (changed.splitlines() + fresh.splitlines()) if x.strip()})
    names = [n for n in names if n.endswith(TF_SUFFIXES)]
    if not names:
        return [], "no file of this root differs from the merge base %s with the shared branch" % base[:10]
    return names, "%d Terraform file(s) of this root differ from the merge base %s" % (len(names), base[:10])


def load_core(repo_root):
    """safe-deploy.sh's own core, imported (its functions decide what a deploy carries; this tool never re-implements them)."""
    spec = importlib.util.spec_from_file_location("opal_safe_deploy_core", os.path.join(repo_root, ".tools", "safe_deploy_core.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def list_deployable(repo_root, files, commit_range) -> int:
    try:
        core = load_core(repo_root)
        explicit = files if files else None
        scripts = core.detect_script_files(commit_range=commit_range, explicit_files=explicit)
        members = core.detect_bundle_member_files(commit_range=commit_range, explicit_files=explicit)
    except Exception as exc:
        print("ERROR: cannot read what the deploy core will deploy (%s: %s)" % (type(exc).__name__, exc), file=sys.stderr)
        return 2
    deploy = list(dict.fromkeys(norm_file(f) for f in list(scripts) + list(members)))
    roots = sorted({"/".join(f.split("/")[:2]) if f.startswith("data/") and f.count("/") >= 2 else os.path.dirname(f) for f in deploy})
    for path in deploy:
        print("DEPLOYABLE %s" % path)
    for root in roots:
        print("DEPLOY-ROOT %s" % root)
    print("DEPLOYABLE-COUNT n=%d" % len(deploy))
    return 0


def read_list(path: str) -> list:
    text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    return [norm_file(x) for x in text.splitlines() if x.strip()]


def resolve_serial(arg: str, repo_root: str = REPO) -> str:
    """The acting seat, in resolve-actor.sh's order (--serial, $OPAL_AGENT_SERIAL, the session serial file, $GIT_AUTHOR_NAME),
    but "" -- never UNKNOWN -- when nothing resolves, so an unresolved actor is never treated as an author (SC-e-89, limb b)."""
    if arg:
        return arg
    if os.environ.get("OPAL_AGENT_SERIAL"):
        return os.environ["OPAL_AGENT_SERIAL"]
    session = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
    if session:
        path = os.path.join(repo_root, "org", "mcp", "sessions", session + ".serial")
        if os.path.isfile(path):
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read().strip()
            if text:
                return text
    return os.environ.get("GIT_AUTHOR_NAME", "")


def loaded_doc(text) -> dict:
    """The sentinel's parsed JSON object, or {} when it does not parse (a stale reading needs only its slug)."""
    try:
        doc = json.loads(text) if text else {}
    except ValueError:
        return {}
    return doc if isinstance(doc, dict) else {}


def sentinel_slug(doc: dict, path: str) -> str:
    """The sentinel's slug, else its file name without .json (SC-e-89, limb c)."""
    if doc.get("slug"):
        return str(doc["slug"])
    base = os.path.basename(path)
    return base[:-len(".json")] if base.endswith(".json") else base


def run(argv: list) -> int:
    root, targets, notices, serial, now_arg, repo_root = "", [], "", "", "", REPO
    files, trunk, listing, commit_range = None, False, False, None
    i = 0
    try:
        while i < len(argv):
            arg = argv[i]
            if arg == "--root":
                root = argv[i + 1]
                i += 2
            elif arg == "--target":
                targets.append(argv[i + 1])
                i += 2
            elif arg == "--notices":
                notices = argv[i + 1]
                i += 2
            elif arg == "--serial":
                serial = argv[i + 1]
                i += 2
            elif arg == "--now":
                now_arg = argv[i + 1]
                i += 2
            elif arg == "--repo-root":
                repo_root = os.path.abspath(argv[i + 1])
                i += 2
            elif arg == "--files":
                files = [] if files is None else files
                i += 1
                while i < len(argv) and not argv[i].startswith("--"):
                    files.append(norm_file(argv[i]))
                    i += 1
            elif arg == "--files-from":
                files = (files or []) + read_list(argv[i + 1])
                i += 2
            elif arg == "--files-vs-trunk":
                trunk = True
                i += 1
            elif arg == "--list-deployable":
                listing = True
                i += 1
            elif arg == "--commit-range":
                commit_range = argv[i + 1]
                i += 2
            else:
                raise ValueError("unknown argument %r" % arg)
        if listing:
            return list_deployable(repo_root, files, commit_range)
        if not root:
            raise ValueError("--root is required")
        if trunk and files is not None:
            raise ValueError("--files-vs-trunk cannot be combined with --files or --files-from")
        now = parse_utc(now_arg) if now_arg else datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0, tzinfo=None)
    except (IndexError, ValueError, OSError) as exc:
        print("ERROR: %s\nusage: crossbox-deploy-check.py --root <dir> [--target <address> ...] [--notices <dir>] "
              "[--files <path> ... | --files-from <file|-> | --files-vs-trunk]" % exc, file=sys.stderr)
        return 2
    notices = notices or os.path.join(repo_root, "org", "devices", "deploy_notices")
    rel = rel_root(root, repo_root)
    name = rel.split("/")[-1]
    serial = resolve_serial(serial, repo_root)
    files_note = "the list the caller passed"
    if trunk:
        files, files_note = trunk_files(repo_root, rel)
    pc = load_placement(repo_root)
    dev = pc.devices_module()
    reg = dev.load()
    dev_name, basis = dev.this_device(reg)
    covering, findings = projects_covering(pc, dev, reg, rel, files)
    print("CROSSBOX-DEPLOY-CHECK device=%s (%s) root=%s targets=%d files=%s now=%s serial=%s" % (
        dev_name or "UNRESOLVED", basis, rel, len(targets), "root-only" if files is None else str(len(files)),
        now.strftime("%Y-%m-%dT%H:%M:%SZ"), serial or "UNRESOLVED"))
    if trunk and files is None:
        print("FILES-NOTE: %s" % files_note)
    sections = (
        ("OPEN-CALL", measure_open_call(repo_root, rel, covering, now, files)),
        ("OVERLAP", measure_overlap(dev_name, covering, findings, basis, files, files_note)),
        ("UPSET", measure_upset(notices, rel, targets, now)),
        ("OPEN-DEPLOY", measure_open_deploy(repo_root, rel, serial, files)),
    )
    verdicts, why = {}, []
    for label, (hits, lines) in sections:
        print("%s: %s" % (label, "hit (%d)" % len(hits) if hits else "clear"))
        for line in lines:
            print(line)
        verdicts[label] = "hit" if hits else "clear"
        why.extend("%s: %s" % (label, h) for h in hits)
    stop = any(v == "hit" for v in verdicts.values())
    if stop:
        print("STOP: %d hit(s) in %s -- first: %s" % (len(why), ", ".join(k for k, v in verdicts.items() if v == "hit"), why[0]))
        print("ROUTE: do not deploy this on the strength of this box alone; raise a cross-box call to the box that owns the "
              "work (cell CT-s-6's tool), or wait for the notice to expire.")
    else:
        print("CLEAR: this box acts and tells the laptop.")
    print("CROSSBOX-DEPLOY device=%s root=%s open_call=%s overlap=%s upset=%s open_deploy=%s verdict=%s" % (
        dev_name or "UNRESOLVED", name, verdicts["OPEN-CALL"], verdicts["OVERLAP"], verdicts["UPSET"],
        verdicts["OPEN-DEPLOY"], "STOP" if stop else "CLEAR"))
    return 1 if stop else 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
