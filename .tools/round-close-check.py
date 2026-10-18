#!/usr/bin/env python3
"""round-close-check.py -- may this round be counted finished on this box? (NFRA_CTLPLN workstream SEATS, cell CT-s-8;
contract C-SEATS clause 7; FWD-23.)

Andrew's word (2026-10-07 ~16:3xZ): "CVO is dedicated reviewer in those drive processes so mandatory spawn on any fabric.
If there are multiple projects attached to one macro on a fabric, it is best practice to spawn a CVO specific to that
macro, e.g. CVO~NFRA."  FWD-23: a piece of work is not counted finished until a seat that did none of it has graded it, on
the box where it was done.

    python .tools/round-close-check.py --project <CODE> [--round <n>] [--workstream <WS>] [--device <d>] [--deep]
    python .tools/round-close-check.py --reviewer-only [--device <d>]       (a remote job: no project, no round)
    python .tools/round-close-check.py --project <CODE> --staged            (read the project's files from the git index)
    python .tools/round-close-check.py --selftest

--round <n> SCOPES an order by the roundN of the decomposition its <decomp_doc> names (file ...roundN.md); an order that names
no decomposition, or whose decomposition file name carries no roundN, is scoped by its <round> tag. The TREE line after the
ORDERS line prints how many tree orders were scoped by their decomposition (CT-af-2).

THREE LIMBS, each printed with its evidence:
  REVIEWER-ON-BOX  a CVO-kind seat (kind through lib/seat_roles.py, via .tools/seat-list.py's own resolver) is LIVE on the
                   box where the work was done. This box: org/mcp/liveness.json, read by .tools/seat-list.py's reader (LIVE =
                   seen within its STALE_SECONDS). Another box: that box's org/devices/state/<device>/seats.json, with its AGE;
                   an absent, unreadable or older-than --max-age-minutes file is UNREAD, never present. A CVO lane named for
                   the project's macro (3.0.0_SA_CVO~NFRA) satisfies it and is printed as the macro reviewer.
  GRADED           every task order of the round whose status is `complete` has a proof instance that passes. DEFAULT is a
                   STRUCTURAL read (JSON parses, names the order, carries one acceptance row per criterion, no FAIL row); --deep
                   additionally runs .tools/proof-of-spec-check.py on each instance (about 5 s each, so it is not the default
                   and not what the commit hook runs). Every `judgment="true"` criterion of those orders needs a row in the
                   project's adjudication file(s) authored by a CVO-kind serial that names the criterion id, or the same kind of
                   row in the investigation file; each is listed with its grading row or UNGRADED.
  NOT-BY-A-DOER    a grading row whose author is the order's issuer or assignee (or another lane of either base serial) is not a
                   grade; it is counted self_graded and the criterion stays ungraded.
  HEADER GRADES   a grade written only in a markdown header, outside the fenced rows ("**RIV-wc-1 J1 MET.**"), is read from the
                  file's `Author:` line and grades by a verdict word (MET, NOT MET, PASS, FAIL, PARTIAL); HELD, NOT MEASURED and
                  UNVERIFIABLE name none. A fenced row grades only by a verdict word within fourteen tokens after the
                  criterion, same clause, or by a `grades` entry {criterion, verdict}: a mention without a verdict is not a
                  grade (the default, CTO~DELL1 msg 4566). --loose-grades restores the mention reading and the report prints
                  LOOSE-GRADES IN USE; every run counts bare mentions. ETFS_RIVALS D1-S15, CTO~DELL1 msg 4559.
BLIND (stated): whether a grade is a GOOD grade. This tool sees that a different CVO-kind seat wrote a row naming the
criterion (with a verdict word, under --strict-grades or in a header), not what the row says. Orders not yet `complete` are listed and do not enter the verdict (a round with an open
order is the issuer's to close, not this tool's to read).

LAST line (always):
  ROUND-CLOSE project=<CODE> device=<d> reviewer=<present|ABSENT|UNREAD> orders=<n> judgment=<j> graded=<g> not_met=<k> ungraded=<u> self_graded=<s> verdict=<MAY-CLOSE|REFUSED>
  not_met=<k> counts, among the GRADED judgment criteria, those whose grade of record reads NOT MET (the verdict word the
  grade of record already carries, read by the same reading). It is information for the round analysis: it changes no
  verdict (NFRA_CTLPLN round 30, CT-cb-1; the CVO's ruling C-S103: a NOT MET grade does not refuse a round close).
--staged: every repository file the check reads for the project (task orders, proof instances, adjudication and
investigation files, project.json) comes from the index git resolves (GIT_INDEX_FILE, GIT_DIR), enumerated with
`git ls-files` and read with `git cat-file --batch`; a file absent from the index is absent even if the working tree has
it. The liveness/reviewer read is runtime state and is unchanged. Without --staged the working tree is read, as before.
It READS and flips nothing. Exit 0 when a verdict was printed (the verdict is the LAST line, as the commit hook reads it),
2 on a usage or read error. Selftest LAST line: ROUND-CLOSE-SELFTEST cases=<k>/<n> ok=<True|False>.
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
DEFAULT_MAX_AGE_MIN = 120
LANE = re.compile(r"~([A-Za-z0-9]+)$")
FENCE = re.compile(r"```json\s*\n(.*?)```", re.S)
CRIT_TAG = re.compile(r"<criterion\b([^>]*?)/?>")
ATTR = re.compile(r'([A-Za-z_]+)="([^"]*)"')
# CT-af-2 (NFRA_CTLPLN round 16, CTO round-15 ruling 4): an order's <round> tag holds its WORKSTREAM's round, so --round is
# matched against the issuance round its decomposition names (<decomp_doc> ...roundN.md) when there is one.
DECOMP_DOC = re.compile(r"<decomp_doc>\s*([^<]*?)\s*</decomp_doc>")
DECOMP_ROUND = re.compile(r"\.round(\d+)\.md$")
# A grade needs a VERDICT (ETFS_RIVALS D1-S15, CTO~DELL1 msg 4559). Words that REACH a verdict, and words that name none.
# Census of the 1056 criterion-then-word matches in 779 tracked adjudication files: MET 324, PASS 314, FAIL 94, NOT MET 68,
# PASSES 20, NOT MEASURED 15, HELD 6, PARTIAL 4, UNGRADED 4. Upper case only: a grader writes the verdict in capitals.
VERDICT_NONE = ("NOT[ _]MEASURED", "NOT[ _]EVALUATED", "UNVERIFIABLE(?:-BY-INSTRUMENT)?", "UNCOMPUTABLE", "UNGRADED", "HELD", "VOID")
VERDICT_GRADED = ("NOT[ _]MET", "MET", "PASS(?:ES|ED)?", "FAIL(?:S|ED)?", "PARTIAL(?:LY[ _]MET)?")
VERDICT_WORD = re.compile(r"(?<![A-Za-z0-9_])(%s)(?![A-Za-z0-9_])" % "|".join(VERDICT_NONE + VERDICT_GRADED))
VERDICT_NONE_RE = re.compile(r"^(?:%s)$" % "|".join(VERDICT_NONE))
AUTHOR_LINE = re.compile(r"^Author:\s*(\d+\.\d+\.\d+_[A-Za-z]+_[A-Za-z0-9]+(?:~[A-Za-z0-9]+)?)", re.M)


class Usage(Exception):
    pass


def load_mod(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def base_of(serial: str) -> str:
    return LANE.sub("", str(serial).strip())


def lane_of(serial: str) -> str:
    m = LANE.search(str(serial).strip())
    return m.group(1) if m else ""


# ---------------------------------------------------------------- where repository files are read from

def pj(*parts: str) -> str:
    """Join with '/', which both a Windows glob and a git pathspec accept."""
    segs = [str(x).replace("\\", "/") for x in parts]
    return "/".join([segs[0].rstrip("/")] + [x.strip("/") for x in segs[1:]])


class WorkTree:
    """Reads the working tree (the default, unchanged)."""

    def __init__(self, root: str):
        self.root = root

    def project_dir(self, code: str) -> str:
        hits = glob.glob(os.path.join(self.root, "org", "missions", "D*", "*", code, "project.json"))
        if len(hits) != 1:
            raise Usage("project %s: %d project.json found under org/missions/D*/*/ (want exactly 1)" % (code, len(hits)))
        return os.path.dirname(hits[0])

    def glob(self, pattern: str) -> list:
        return sorted(glob.glob(pattern))

    def read(self, path: str) -> str:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()

    def local(self, path: str) -> str:
        return path

    def close(self) -> None:
        pass


class Staged:
    """Reads the index git resolves (GIT_INDEX_FILE / GIT_DIR from the environment): `git ls-files -s` to enumerate,
    `git cat-file --batch` to read. A path the index lacks is absent; the working tree is never opened."""

    def __init__(self, root: str, env=None):
        self.root = root
        self.env = env if env is not None else os.environ.copy()
        self._blobs = {}   # path -> sha
        self._text = {}
        self._tmp = None

    def _git(self, args: list, data=None) -> bytes:
        r = subprocess.run(["git", "-C", self.root] + args, input=data, capture_output=True, env=self.env)
        if r.returncode != 0:
            raise Usage("git %s failed rc=%d: %s" % (" ".join(args[:2]), r.returncode, r.stderr.decode("utf-8", "replace").strip()))
        return r.stdout

    def _entries(self, pathspec: str) -> list:
        out = self._git(["ls-files", "-s", "-z", "--", pathspec]).decode("utf-8", "replace")
        rows = []
        for rec in out.split("\0"):
            if not rec:
                continue
            meta, _tab, path = rec.partition("\t")
            parts = meta.split()
            if len(parts) == 3 and parts[2] == "0":
                rows.append((path, parts[1]))
        return rows

    def _load(self, paths: list) -> None:
        want = [p for p in paths if p in self._blobs and p not in self._text]
        if not want:
            return
        raw = self._git(["cat-file", "--batch"], "".join("%s\n" % self._blobs[p] for p in want).encode("ascii"))
        pos = 0
        for p in want:
            nl = raw.index(b"\n", pos)
            head = raw[pos:nl].split()
            if len(head) != 3 or head[1] != b"blob":
                raise Usage("index entry %s is not a readable blob (%s)" % (p, raw[pos:nl].decode("ascii", "replace")))
            size = int(head[2])
            self._text[p] = raw[nl + 1:nl + 1 + size].decode("utf-8", "replace")
            pos = nl + 1 + size + 1

    def project_dir(self, code: str) -> str:
        hits = self.glob("org/missions/D*/*/%s/project.json" % code)
        hits = [p for p in hits if re.match(r"^org/missions/D(?:0|[1-9][0-9]?)/", p)]
        if len(hits) != 1:
            raise Usage("project %s: %d project.json in the index under org/missions/D*/*/ (want exactly 1)" % (code, len(hits)))
        return hits[0].rsplit("/", 1)[0]

    def glob(self, pattern: str) -> list:
        """git's pathspec `*` crosses '/', so the hits are filtered back to one-segment wildcards."""
        rx = re.compile("^" + "/".join(re.escape(sg).replace(r"\*", "[^/]*") for sg in pattern.split("/")) + "$")
        ent = [(p, s) for p, s in self._entries(pattern) if rx.match(p)]
        for p, s in ent:
            self._blobs[p] = s
        self._load([p for p, _s in ent])
        return sorted(p for p, _s in ent)

    def read(self, path: str) -> str:
        if path not in self._text:
            if path not in self._blobs:
                ent = dict(self._entries(path))
                if path not in ent:
                    raise OSError("%s is not in the index" % path)
                self._blobs[path] = ent[path]
            self._load([path])
        return self._text[path]

    def local(self, path: str) -> str:
        """A real file holding the staged bytes (for a tool that opens a path, e.g. --deep)."""
        if self._tmp is None:
            # proof-of-spec-check refuses an instance outside the tree it lives in, so the copy goes under the root.
            scratch = os.path.join(self.root, ".scratch")
            os.makedirs(scratch, exist_ok=True)
            self._tmp = tempfile.mkdtemp(prefix="rcc_staged_", dir=scratch)
        dest = os.path.join(self._tmp, path.replace("/", "__"))
        with open(dest, "w", encoding="utf-8", newline="") as fh:
            fh.write(self.read(path))
        return dest

    def close(self) -> None:
        if self._tmp:
            shutil.rmtree(self._tmp, ignore_errors=True)


# ---------------------------------------------------------------- the reviewer limb

def reviewer_limb(sl, ctx, device: str, this_box: str, kind_of, macro: str, max_age_min: int) -> dict:
    """{state: present|ABSENT|UNREAD, who: [(serial, macro_flag)], source, note}."""
    out = {"state": "UNREAD", "who": [], "source": "", "note": ""}
    if device == this_box:
        out["source"] = "org/mcp/liveness.json (this box, read as .tools/seat-list.py reads it)"
        try:
            live = sl.read_liveness(ctx)
        except sl.BadFile as exc:
            out["note"] = str(exc)
            return out
        now = ctx.now()
        for serial in sorted(live):
            info = live[serial] if isinstance(live[serial], dict) else {}
            seen = info.get("last_seen_epoch")
            if kind_of(serial) == "CVO" and isinstance(seen, (int, float)) and now - int(seen) <= sl.STALE_SECONDS:
                out["who"].append((serial, bool(macro) and lane_of(serial).upper() == macro.upper()))
        out["state"] = "present" if out["who"] else "ABSENT"
        out["note"] = "%d registered seat(s) read" % len(live)
        return out
    try:
        path = sl.list_path(ctx, device)
        out["source"] = path.replace("\\", "/")
        doc = sl.read_list(ctx, device)
    except sl.BadFile as exc:
        out["note"] = "%s; an absent or unreadable list is never a present reviewer" % exc
        return out
    written = sl.stamp_epoch(doc.get("written_at"))
    if written is None:
        out["note"] = "written_at unreadable (%r)" % doc.get("written_at")
        return out
    age_min = max(0, (ctx.now() - written) // 60)
    out["note"] = "seats.json written_at %s, age %d min (limit %d)" % (doc["written_at"], age_min, max_age_min)
    if age_min > max_age_min:
        out["note"] += "; STALE, so UNREAD"
        return out
    for row in doc["rows"]:
        if kind_of(row["serial"]) == "CVO" and row["liveness"] == "LIVE":
            out["who"].append((row["serial"], bool(macro) and lane_of(row["serial"]).upper() == macro.upper()))
    out["state"] = "present" if out["who"] else "ABSENT"
    return out


# ---------------------------------------------------------------- orders and proofs

def tag(text: str, name: str):
    m = re.search(r"^<%s>(.*?)</%s>" % (name, name), text, re.M)
    return m.group(1).strip() if m else None


def decomp_round(text: str) -> str:
    """The issuance round the order's decomposition names: N from a <decomp_doc> whose file name ends .roundN.md; '' when
    the order names no decomposition or its file name carries no roundN (the caller then falls back to the <round> tag)."""
    m = DECOMP_DOC.search(text)
    if not m:
        return ""
    r = DECOMP_ROUND.search(os.path.basename(m.group(1).replace("\\", "/")))
    return r.group(1) if r else ""


# Source: .tools/seat-list.py STATUS_WORDS (used when seat-list.py imports; this copy is the fallback).
_STATUS_FALLBACK = {"complete", "superseded", "cancelled", "canceled", "withdrawn", "retired", "closed", "pending",
                    "staged", "open", "parked", "active", "in_progress", "in-progress", "blocked", "held", "draft",
                    "issued"}


def status_words() -> set:
    try:
        return set(load_mod("opal_seat_list_s", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                             "seat-list.py")).STATUS_WORDS)
    except Exception:  # noqa: BLE001 - a seat-list that does not import falls back to the local copy
        return set(_STATUS_FALLBACK)


COMPLETE_WORDS = {"complete", "completed", "done", "closed"}
OTHER_TERMINAL_WORDS = {"superseded", "cancelled", "canceled", "withdrawn", "retired", "parked"}
# TERMINAL AND NOT CLEAN (row AMGT_RESAPP-D1-S55; 1.0.0_SA_CTO ruling
# org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_PARKED_BUS_ITEMS_20261017_1350Z.md item 2): the order ended with at
# least one criterion failed. Counted as orders_not_met, never as complete and never as proof_bad; it does not reopen.
NOT_MET_WORDS = {"not_met"}


def lead_word(text: str) -> str:
    """The order's own status word: the first token of the <status> text, lowercased, trailing punctuation stripped."""
    toks = text.strip().lower().split()
    return toks[0].rstrip(".,;:!-") if toks else ""


def last_status(text: str, words: set) -> str:
    """The LAST <status> tag whose LEADING word is a status word (CTO ruling msg 107528; R3: read the order, not a spelling)."""
    got = ""
    known = set(words) | COMPLETE_WORDS | OTHER_TERMINAL_WORDS | NOT_MET_WORDS
    # leading whitespace admitted: an applier's flat-folder order indents its <status> line (TCKT_VNEXT TV2 orders), and
    # a line-anchored read returned '' for a `complete` order, so it was never counted as done (D2-S23, second limb)
    for m in re.finditer(r"^[ \t]*<status>(.*?)</status>", text, re.M):
        w = lead_word(m.group(1))
        if w in known:
            got = w
    return got


def read_orders(src, proj_dir: str, rnd, ws) -> list:
    """The project's orders: the tree's task-orders/ PLUS every seat flat folder's <CODE>.TO-*.md (an applier's or a
    Tier-2 seat's own task_orders/, where a round's APPLY/RUN orders live -- TCKT_VNEXT-D2-S23: round 1 printed
    judgment=1 graded=1 MAY-CLOSE while SA-r-1b AC2 NOT MET sat in 0.7.0_AE_CloudOps~TV2/task_orders/, unread). One order
    per to_id: the tree copy wins over a flat copy of the same id. A flat order remembers its seat dir for proof_state."""
    out = []
    seen = set()
    words = status_words()
    code = os.path.basename(proj_dir.rstrip("/"))
    tree = [(p, None) for p in src.glob(pj(proj_dir, "task-orders", "*.md"))]
    # the local source globs from its root (an absolute pattern, like proj_dir's); the git source takes a repo pathspec
    flat_pat = pj("org", "tier*", "*", "task_orders", code + ".TO-*.md")
    if not hasattr(src, "_entries"):
        flat_pat = pj(src.root, flat_pat)
    flat = [(p, p.replace("\\", "/").rsplit("/task_orders/", 1)[0]) for p in src.glob(flat_pat)]
    for path, seat_dir in tree + flat:
        text = src.read(path)
        stem = os.path.basename(path)[:-3]
        # no <to_id>: the id is the stem's first two dot-segments, <CODE>.TO-<id>, the form every proof instance and
        # grading row names (a whole-stem fallback matched neither, so a flat order's AC2 read UNGRADED and PROOF-BAD)
        fallback = ".".join(stem.split(".", 2)[:2]) if stem.count(".") >= 2 and ".TO-" in stem else stem
        o = {"path": path, "stem": stem, "id": tag(text, "to_id") or fallback,
             "status": last_status(text, words), "round": tag(text, "round") or "",
             "workstream": tag(text, "workstream"), "issued_by": tag(text, "issued_by") or "",
             "issued_to": tag(text, "issued_to") or "", "criteria": [], "seat_dir": seat_dir}
        for m in CRIT_TAG.finditer(text):
            attrs = dict(ATTR.findall(m.group(1)))
            if "id" in attrs:
                o["criteria"].append({"id": attrs["id"], "judgment": attrs.get("judgment", "").lower() == "true"})
        # CT-af-2: the scoping round is the decomposition's roundN when the order names one, else its <round> tag (unchanged)
        dec = decomp_round(text)
        o["decomp_scoped"] = bool(dec)
        o["scope_round"] = dec or o["round"]
        if rnd is not None and str(o["scope_round"]) != str(rnd):
            # A flat-folder order with NO <round> tag cannot be scoped to any round (the TV2 APPLY/RUN orders carry
            # none). Dropping it silently is the D2-S23 hole; it is counted in every round's check and NAMED as
            # untagged, so its judgment criteria still gate the close and the issuer sees the missing tag.
            if not (seat_dir and not str(o["scope_round"]).strip()):
                continue
            o["untagged"] = True
        if ws is not None and str(o["workstream"]) != str(ws):
            continue
        if o["id"] in seen:
            continue
        seen.add(o["id"])
        out.append(o)
    return out


def _newest_instance_only(root: str, paths: list) -> list:
    """The instances proof_state grades. INERT unless armed (flag file org/mcp/proof-newest-instance.enforce, or
    PROOF_NEWEST_INSTANCE=1): unarmed, `paths` is returned unchanged and the first instance that passes still passes the order.
    Armed, with two or more, only the ONE newest is graded (.tools/proof_instance_select.py), so an older VALID instance can no
    longer mask a newer FAILING one."""
    helper = os.path.join(os.path.dirname(os.path.abspath(__file__)), "proof_instance_select.py")
    if not os.path.isfile(helper):
        return paths   # this script was copied away from .tools (a test, a mutant control): grade as before, never crash
    spec = importlib.util.spec_from_file_location("proof_instance_select", helper)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.select(root, paths)


def proof_state(src, order: dict, proj_dir: str, root: str, deep: bool) -> tuple:
    """(ok, reason). Structural by default; --deep adds proof-of-spec-check.py (rc 0 = VALID)."""
    paths = src.glob(pj(proj_dir, "deliverables", "*", order["stem"] + ".proof_of_spec.json"))
    if order.get("seat_dir"):
        # a flat-folder order's proof lives in its seat's own deliverables/ (directly, or one folder down)
        paths += src.glob(pj(order["seat_dir"], "deliverables", order["stem"] + ".proof_of_spec.json"))
        paths += src.glob(pj(order["seat_dir"], "deliverables", "*", order["stem"] + ".proof_of_spec.json"))
    if not paths:
        return False, "no proof instance named %s.proof_of_spec.json under deliverables/%s" % (
            order["stem"], " (project tree or the seat's own)" if order.get("seat_dir") else "")
    paths = _newest_instance_only(root, paths)
    reasons = []
    want = [c["id"] for c in order["criteria"]]
    for path in paths:
        try:
            inst = json.loads(src.read(path))
            rows = inst["acceptance"]
            have = {r.get("criterion_id") for r in rows}
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
            reasons.append("%s unreadable (%s)" % (os.path.basename(os.path.dirname(path)), exc))
            continue
        inst_id = str(inst.get("to_id", "")).strip()
        # a proof instance names the order by its <CODE>.TO-<id> form OR by its whole file stem (both are in use across
        # the appliers' folders); either names THIS order, a different id does not
        if inst_id not in (order["id"], order["stem"]) and not inst_id.startswith(order["id"] + "."):
            reasons.append("%s names to_id %r, not %r" % (os.path.basename(os.path.dirname(path)), inst.get("to_id"), order["id"]))
            continue
        miss = [c for c in want if c not in have]
        if miss:
            reasons.append("no acceptance row for %s" % ",".join(miss))
            continue
        bad = [r.get("criterion_id") for r in rows if str(r.get("status", "")).upper().startswith("FAIL")]
        if bad:
            reasons.append("FAIL row(s) %s" % ",".join(bad))
            continue
        if deep:
            checker = os.path.join(root, ".tools", "proof-of-spec-check.py")
            try:
                rc = subprocess.run([sys.executable, checker, src.local(path), ",".join(want)], capture_output=True, text=True,
                                    timeout=100, cwd=root).returncode
            except (OSError, subprocess.TimeoutExpired) as exc:
                reasons.append("proof-of-spec-check did not finish (%s)" % exc)
                continue
            if rc != 0:
                reasons.append("proof-of-spec-check rc=%d" % rc)
                continue
        return True, ("VALID by proof-of-spec-check" if deep else "structural") + " %s" % os.path.basename(os.path.dirname(path))
    return False, "; ".join(reasons)


# ---------------------------------------------------------------- the grading rows

def load_rows(src, files: list) -> tuple:
    """[(file, row dict)], count of fenced blocks that did not parse (printed, never silent)."""
    rows, bad = [], 0
    for path in files:
        text = src.read(path)
        for m in FENCE.finditer(text):
            try:
                doc = json.loads(m.group(1))
            except ValueError:
                bad += 1
                continue
            for row in (doc if isinstance(doc, list) else [doc]):
                if isinstance(row, dict):
                    rows.append((path, row))
    return rows, bad


def author_of(row: dict) -> str:
    for key in ("surfaced_by", "authored_by", "author"):
        if row.get(key):
            return str(row[key])
    return ""


def load_prose(src, files: list) -> list:
    """[(file, pseudo-row)]: each file's text OUTSIDE its fenced json blocks, authored by its `Author:` line. A grade written
    only in a header ("RIV-wc-1 J1 MET.") lives here; it grades by a verdict word and never by a bare mention."""
    out = []
    for path in files:
        text = src.read(path)
        m = AUTHOR_LINE.search(text)
        out.append((path, {"id": os.path.basename(path) + "#header", "author": m.group(1) if m else "",
                           "_prose": FENCE.sub("", text)}))
    return out


def _strings(value, out: list) -> None:
    if isinstance(value, str):
        out.append(value)
    elif isinstance(value, dict):
        for item in value.values():
            _strings(item, out)
    elif isinstance(value, list):
        for item in value:
            _strings(item, out)


def row_text(row: dict) -> str:
    """Every string in the row, one blank line between fields, so a verdict in the next field never reads as adjacent."""
    out: list = []
    _strings(row, out)
    return "\n\n".join(out)


def verdict_after(text: str, crit_pat, order_pat, span: int = 40) -> str:
    """The first verdict word within fourteen tokens after a mention of the criterion, in the same clause (no sentence
    break between, so a list "AC3, AC4 and AC5 MET" carries one verdict for all of it); '' when none. A
    generic id (order_pat set) must also have its order named in the `span` characters before it (the order's full id
    plus its "TO-" and a separator, so a long slugged id is not cut)."""
    for m in crit_pat.finditer(text):
        if order_pat and not order_pat.search(text[max(0, m.start() - span):m.start()]):
            continue
        tail = text[m.end():m.end() + 90]
        v = VERDICT_WORD.search(tail)
        if not v:
            continue
        gap = tail[:v.start()]
        if re.search(r"[.;]\s|\n\n", gap) or len(re.findall(r"[A-Za-z0-9_]+", gap)) > 14:
            continue
        return v.group(1)
    return ""


def structured_grade(row: dict, crit_id: str, order_pat) -> str:
    """The verdict of a `grades` entry ({criterion, verdict, instance}) that names this criterion; '' when none."""
    entries = row.get("grades")
    if not isinstance(entries, list):
        return ""
    for e in entries:
        if not isinstance(e, dict):
            continue
        named = str(e.get("criterion", ""))
        # A generic id (AC5) is written namespaced by a grader (RPs1-AC5); the entry's instance names the order.
        if named != crit_id and not (order_pat and named.endswith("-" + crit_id)):
            continue
        if order_pat and not order_pat.search(json.dumps(e)):
            continue
        v = VERDICT_WORD.match(str(e.get("verdict", "")).strip().upper())
        if v:
            return v.group(1)
    return ""


# NFRA_CTLPLN round 29 (CT-be-1, cross-box call XB-20261016T121809Z-95c2): a criterion is read from its GRADE OF RECORD.
# Real rows carry surfaced_at as minute-precision ISO 8601 with a Z ("2026-10-16T12:00Z"); seconds, a fraction and a
# numeric offset are admitted too.
SURFACED_AT = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2})(?::(\d{2})(?:\.\d+)?)?)?\s*(Z|[+-]\d{2}:?\d{2})?$",
                         re.I)


def surfaced_epoch(value):
    """Epoch seconds of a row's surfaced_at, or None when it is absent or does not parse (such a row sorts before every
    dated row). A time with no offset is UTC, the convention the adjudication rows use."""
    if not isinstance(value, str):
        return None
    m = SURFACED_AT.match(value.strip())
    if not m:
        return None
    y, mo, d, hh, mi, ss, tz = m.groups()
    try:
        stamp = datetime(int(y), int(mo), int(d), int(hh or 0), int(mi or 0), int(ss or 0),
                         tzinfo=timezone.utc).timestamp()
    except ValueError:
        return None
    if tz and tz.upper() != "Z":
        digits = tz[1:].replace(":", "")
        offset = int(digits[:2]) * 3600 + int(digits[2:]) * 60
        stamp -= offset if tz[0] == "+" else -offset
    return stamp


def _ids_named(value) -> set:
    """The row ids a `supersedes` or `adjudicates` value names: one string or a list of strings; anything else names none."""
    if isinstance(value, str):
        return {value.strip()}
    if isinstance(value, list):
        return {x.strip() for x in value if isinstance(x, str)}
    return set()


def grade_of_record(cands: list) -> tuple:
    """(payload of the grade of record, candidate count). cands are (key, row, payload) for the CVO-kind non-doer rows that
    grade one criterion, key = (dated, epoch, position): a row with no parseable surfaced_at sorts first, and a tie keeps
    file order so the later file/row wins. The record is the greatest key, except a row that a LATER candidate names in its
    `supersedes` or `adjudicates` key. The greatest key is never named by a later row, so one candidate always remains."""
    ranked = sorted(cands, key=lambda c: c[0])
    live = []
    for i, (_key, row, payload) in enumerate(ranked):
        rid = str(row.get("id", ""))
        named = any(rid and rid in (_ids_named(later.get("supersedes")) | _ids_named(later.get("adjudicates")))
                    for _k, later, _p in ranked[i + 1:])
        if not named:
            live.append(payload)
    return live[-1], len(cands)


def grade_criterion(crit_id: str, order: dict, adj_rows: list, inv_rows: list, kind_of, strict: bool = False) -> tuple:
    """(state GRADED|SELF|UNGRADED, detail, word): word is the verdict word of the grade of record ('' when none is read).
    Adjudication-file rows: a doer is a self-grade, a CVO-kind non-doer a grade.
    Investigation-file rows: only a CVO-kind author counts (a doer's own surprise rows name criteria all the time and are
    not grades); a CVO-kind doer is a self-grade.
    A header-only grade (a `_prose` pseudo-row) and every row under strict=True needs a VERDICT word after the criterion
    (or a `grades` entry with one); a mention without a verdict is not a grade. strict=False keeps the older reading for
    a fenced row: any mention of the criterion by a CVO-kind non-doer grades.
    THE GRADE OF RECORD (CT-be-1): every qualifying CVO-kind non-doer row is collected and the one read is the grade of
    record (grade_of_record: the latest surfaced_at), not the first row in file order. The verdict in the detail is the
    verdict of that row. A self-grade reads SELF only when no CVO-kind non-doer row grades the criterion.
    SOURCE PRIORITY (CT-bf-1, round 29, AMENDMENT 2): an ADJUDICATION-file grade outranks an INVESTIGATION-file grade, whatever
    their dates; the grade of record is taken within the winning source. A row that only reports a grade does not grade."""
    pat = re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(crit_id))
    # A generic id (AC3, J2) is a substring of every order's AC3/J2 and of any check-script name (rl9.AC3.sh): the row must
    # also name THIS order (its to_id or the short id after "TO-"), or a stale row from another round grades it.
    short = order["id"].split(".TO-", 1)[-1]
    order_pat = None
    if re.fullmatch(r"(?:AC|J)\d+[a-z]?", crit_id):
        names = [re.escape(order["id"]), "TO-" + re.escape(short)] + ([re.escape(short)] if re.search(r"[A-Za-z]", short) else [])
        order_pat = re.compile(r"(?<![A-Za-z0-9])(?:%s)(?![A-Za-z0-9])" % "|".join(names))
    doers = {base_of(order["issued_by"]), base_of(order["issued_to"])} - {""}
    self_hit = None
    cands = []      # (key, row, payload): every CVO-kind non-doer row that grades the criterion
    position = 0
    for source, rows in (("adjudication", adj_rows), ("investigation", inv_rows)):
        for _path, row in rows:
            position += 1
            via = ""
            if strict or row.get("_prose"):
                v = structured_grade(row, crit_id, order_pat) or verdict_after(
                    row_text(row), pat, order_pat, max(40, len(order["id"]) + 16))
                if not v or VERDICT_NONE_RE.match(v):
                    continue
                via = " (verdict %s)" % v
            else:
                text = json.dumps(row)
                if not pat.search(text) or (order_pat and not order_pat.search(text)):
                    continue
            who = author_of(row)
            if not who:
                continue
            is_doer = base_of(who) in doers
            is_cvo = kind_of(who) == "CVO"
            if is_cvo and not is_doer:
                epoch = surfaced_epoch(row.get("surfaced_at"))
                key = (0, 0.0, position) if epoch is None else (1, epoch, position)
                cands.append((key, row, (source, row, who, via)))
            elif is_doer and (source == "adjudication" or is_cvo):
                self_hit = self_hit or "%s row %s by %s, the order's own %s" % (
                    source, row.get("id", "?"), who, "issuer" if base_of(who) == base_of(order["issued_by"]) else "assignee")
    if cands:
        # NFRA_CTLPLN round 29 (CT-bf-1 AMENDMENT 2, SOURCE PRIORITY): the candidates are the rows that already grade (the tests
        # above, unchanged, strict or loose, prose or structured). An ADJUDICATION-file grade ALWAYS outranks an INVESTIGATION-file
        # grade, whatever their dates; within one source the grade of record is the latest surfaced_at (grade_of_record). An
        # investigation grade is read only when no adjudication row grades the criterion. No prose is read differently.
        adj_c = [c for c in cands if c[2][0] == "adjudication"]
        inv_c = [c for c in cands if c[2][0] == "investigation"]
        pool = adj_c or inv_c
        (source, row, who, via), _n = grade_of_record(pool)
        # NFRA_CTLPLN round 30 (CT-cb-1): the verdict word of the grade of record, read by the SAME two readings the candidate
        # test above uses (a `grades` entry, else the verdict after the criterion). It feeds not_met= only; the detail is unchanged.
        word = structured_grade(row, crit_id, order_pat) or verdict_after(
            row_text(row), pat, order_pat, max(40, len(order["id"]) + 16))
        n = len(cands)
        detail = "%s row %s by %s%s" % (source, row.get("id", "?"), who, via)
        if n > 1:
            detail += "; grade of record among %d CVO-kind rows (latest surfaced_at wins)" % n
        return "GRADED", detail, word
    if self_hit:
        return "SELF", self_hit, ""
    return "UNGRADED", "no CVO-kind row names it", ""


# ---------------------------------------------------------------- the whole check

def check(root: str, sl, ctx, code, rnd, ws, device, this_box, kind_of, deep=False, max_age=DEFAULT_MAX_AGE_MIN,
          reviewer_only=False, staged=False, env=None, strict_grades=True) -> tuple:
    """(lines, last_line). staged=True reads the project's repository files from the git index (see Staged)."""
    src = Staged(root, env) if staged else WorkTree(root)
    try:
        return _check(src, root, sl, ctx, code, rnd, ws, device, this_box, kind_of, deep, max_age, reviewer_only, strict_grades)
    finally:
        src.close()


def _check(src, root: str, sl, ctx, code, rnd, ws, device, this_box, kind_of, deep, max_age, reviewer_only,
           strict_grades=True) -> tuple:
    lines = []
    macro = ""
    proj_dir = None
    if not reviewer_only:
        proj_dir = src.project_dir(code)
        try:
            macro = json.loads(src.read(pj(proj_dir, "project.json"))).get("macro_code", "")
        except (OSError, ValueError):
            macro = ""
    rv = reviewer_limb(sl, ctx, device, this_box, kind_of, macro, max_age)
    who = ", ".join("%s%s" % (s, " (macro reviewer for %s)" % macro if m else "") for s, m in rv["who"]) or "none"
    lines.append("REVIEWER-ON-BOX device=%s state=%s reviewer seat(s)=%s" % (device, rv["state"], who))
    lines.append("  source: %s; %s" % (rv["source"], rv["note"]))
    n_orders = n_j = n_g = n_s = n_nm = 0
    if reviewer_only:
        verdict = "MAY-CLOSE" if rv["state"] == "present" else "REFUSED"
        return lines, "ROUND-CLOSE project=- device=%s reviewer=%s orders=0 judgment=0 graded=0 not_met=0 ungraded=0 self_graded=0 verdict=%s" % (
            device, rv["state"], verdict)
    orders = read_orders(src, proj_dir, rnd, ws)
    # IRPT_BCKEND-D2-S76 (2026-10-12): an untagged seat-folder order (no <round>) is counted in every round's
    # check so its issuer sees the missing tag (D2-S23). With no --workstream that counted ANOTHER lane's
    # untagged orders into this issuer's close. Now an untagged order GATES the verdict only when its
    # <issued_by> is one of the round's own issuers (read from the round's tagged orders); another lane's
    # untagged order is NAMED below and left out of the counts. No tagged orders in scope: unchanged, all count.
    round_issuers = {o["issued_by"] for o in orders if not o.get("untagged") and o["issued_by"]}
    foreign_untagged = [o for o in orders if o.get("untagged") and round_issuers
                        and o["issued_by"] and o["issued_by"] not in round_issuers]
    if foreign_untagged:
        orders = [o for o in orders if o not in foreign_untagged]
        lines.append("  SEAT-FOLDER orders NAMED, not counted (no <round> tag, issued by a lane outside this round's "
                     "issuers %s): %s" % (",".join(sorted(round_issuers)),
                                          ", ".join("%s<-%s" % (o["id"].split(".")[-1], o["issued_by"]) for o in foreign_untagged)))
    n_orders = len(orders)
    done = [o for o in orders if o["status"] in COMPLETE_WORDS]
    not_met_orders = [o for o in orders if o["status"] in NOT_MET_WORDS]
    open_ = [o for o in orders if o["status"] not in COMPLETE_WORDS and o["status"] not in OTHER_TERMINAL_WORDS
             and o["status"] not in NOT_MET_WORDS]
    lines.append("ORDERS scope round=%s workstream=%s: %d order(s), %d complete, %d not complete and outside the verdict%s" % (
        rnd if rnd is not None else "all", ws if ws is not None else "all", n_orders, len(done), len(open_),
        (" (" + ", ".join(o["id"].split(".")[-1] for o in open_) + ")") if open_ else ""))
    if not_met_orders:
        lines.append("  NOT-MET orders (terminal, NOT clean; outside the proof count): %d (%s)" % (
            len(not_met_orders), ", ".join(o["id"].split(".")[-1] for o in not_met_orders)))
    tree_dec = [o for o in orders if o.get("decomp_scoped") and not o.get("seat_dir")]
    lines.append("  TREE orders counted by decomposition round: %d (%s)" % (
        len(tree_dec), ", ".join(o["id"].split(".")[-1] for o in tree_dec)))
    flat = [o for o in orders if o.get("seat_dir")]
    untagged = [o for o in flat if o.get("untagged")]
    if flat:
        lines.append("  SEAT-FOLDER orders counted: %d (%s)%s" % (
            len(flat), ", ".join(o["id"].split(".")[-1] for o in flat),
            ("; %d carry NO <round> tag and are counted in EVERY round's check until the issuer tags them: %s" % (
                len(untagged), ", ".join(o["id"].split(".")[-1] for o in untagged))) if untagged else ""))
    bad_proofs = 0
    for o in done:
        ok, why = proof_state(src, o, proj_dir, root, deep)
        if not ok:
            bad_proofs += 1
            lines.append("  PROOF-BAD %s: %s" % (o["id"], why))
    lines.append("PROOFS mode=%s complete=%d proof_ok=%d proof_bad=%d" % ("deep" if deep else "structural", len(done),
                                                                         len(done) - bad_proofs, bad_proofs))
    adj_files = src.glob(pj(proj_dir, "surprise-channel", "adjudications", "ADJUDICATION_v*.md"))
    inv_files = src.glob(pj(proj_dir, "surprise-channel", "investigations", "INVESTIGATION_v*.md"))
    adj_rows, bad_a = load_rows(src, adj_files)
    inv_rows, bad_i = load_rows(src, inv_files)
    lines.append("GRADING-ROWS adjudication=%d row(s) in %d file(s), investigation=%d row(s) in %d file(s), %d json block(s) did not parse" % (
        len(adj_rows), len(adj_files), len(inv_rows), len(inv_files), bad_a + bad_i))
    adj_all = adj_rows + load_prose(src, adj_files)
    inv_all = inv_rows + load_prose(src, inv_files)
    bare = strict_n = 0
    for o in done:
        for c in o["criteria"]:
            if not c["judgment"]:
                continue
            n_j += 1
            state, why, word = grade_criterion(c["id"], o, adj_all, inv_all, kind_of, strict=strict_grades)
            s_state = state if strict_grades else grade_criterion(c["id"], o, adj_all, inv_all, kind_of, strict=True)[0]
            strict_n += s_state == "GRADED"
            if state == "GRADED" and s_state != "GRADED":
                bare += 1
                why += " -- BARE MENTION: no verdict word after the criterion"
            if state == "GRADED":
                n_g += 1
                if word.replace("_", " ") == "NOT MET":
                    n_nm += 1
            if state == "SELF":
                n_s += 1
            lines.append("  JUDGMENT %s %s -> %s (%s)" % (o["id"].split(".")[-1], c["id"], state, why))
    if strict_grades:
        lines.append("STRICT-GRADES mode=verdict graded_with_a_verdict_word=%d bare_mention=%d of judgment=%d (a mention "
                     "without a verdict word is not a grade; --loose-grades restores the older mention reading)" % (
                         strict_n, bare, n_j))
    else:
        lines.append("LOOSE-GRADES IN USE (--loose-grades): a fenced row grades by any mention of the criterion; "
                     "graded_with_a_verdict_word=%d bare_mention=%d of judgment=%d" % (strict_n, bare, n_j))
    n_u = n_j - n_g
    ok = rv["state"] == "present" and n_u == 0 and n_s == 0 and bad_proofs == 0
    return lines, "ROUND-CLOSE project=%s device=%s reviewer=%s orders=%d judgment=%d graded=%d not_met=%d ungraded=%d self_graded=%d verdict=%s" % (
        code, device, rv["state"], n_orders, n_j, n_g, n_nm, n_u, n_s, "MAY-CLOSE" if ok else "REFUSED")


def make_kind_of(root: str):
    """kind_of through lib/seat_roles.py; the same minimal local fallback .tools/seat-list.py carries."""
    sl_path = os.path.join(root, ".tools", "seat-list.py")
    if os.path.isfile(sl_path):
        return load_mod("opal_seat_list_k", sl_path).kind_resolver()
    return lambda serial: "UNKNOWN"


def resolve_this_box(root: str) -> str:
    dev = load_mod("opal_devices_rc", os.path.join(root, "lib", "devices.py"))
    name, basis = dev.this_device(dev.load())
    if name is None:
        raise Usage("this box is unresolved: %s (name it with --device, or set AGENTBUS_DEVICE)" % basis)
    return name


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    sl = load_mod("opal_seat_list_t", os.path.join(TOOLS, "seat-list.py"))
    dev = load_mod("opal_devices_t", os.path.join(ROOT, "lib", "devices.py"))
    names = dev.names(dev.load())
    this_box, other_box = names[0], names[1]
    kind_of = sl.kind_resolver()
    tmp = tempfile.mkdtemp(prefix="rcc_selftest_")
    results = []
    NOW = 2000000000

    def w(rel, text):
        p = os.path.join(tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)

    base = "org/missions/D0/TEST/TEST_PROJ"
    order = ('# TO\n<to_id>TEST_PROJ.TO-1</to_id>\n<issued_to>0.9.0_WK_TEST_PROJ~1</issued_to>\n<issued_by>2.0.0_SA_COO~C</issued_by>\n'
             '<status>complete</status>\n<round>1</round>\n'
             '<criterion id="T1-AC1" cell_refs="X"><invocation>x</invocation></criterion>\n'
             '<criterion id="T1-AC2" cell_refs="X" judgment="true"/>\n')

    def reset(reviewer="3.0.0_SA_CVO", graded_by="3.0.0_SA_CVO", where="adjudication", seen=NOW, proof=True):
        shutil.rmtree(tmp, ignore_errors=True)
        os.makedirs(tmp)
        w("now", str(NOW))
        w(base + "/project.json", '{"project_code": "TEST_PROJ", "macro_code": "TEST"}')
        w(base + "/task-orders/TEST_PROJ.TO-1.one.md", order)
        w(base + "/task-orders/TEST_PROJ.TO-2.two.md", order.replace("TO-1", "TO-2").replace("complete", "issued"))
        if proof:
            w(base + "/deliverables/0.9.0_WK_TEST_PROJ~1/TEST_PROJ.TO-1.one.proof_of_spec.json", json.dumps(
                {"to_id": "TEST_PROJ.TO-1", "acceptance": [
                    {"criterion_id": "T1-AC1", "status": "PASS"},
                    {"criterion_id": "T1-AC2", "status": "UNVERIFIABLE-BY-INSTRUMENT", "judgment": True}]}))
        row = {"id": "TEST_PROJ-C-S1", "surfaced_by": graded_by, "adjudicates": ["T1-AC2"],
               "one_line": "TEST_PROJ.TO-1 T1-AC2: MET on this seat's read."}
        if graded_by:
            fname = "adjudications/ADJUDICATION_v1.md" if where == "adjudication" else "investigations/INVESTIGATION_v1.md"
            w(base + "/surprise-channel/" + fname, "# rows\n\n```json\n%s\n```\n" % json.dumps([row], indent=1))
        w("org/mcp/liveness.json", json.dumps({
            "2.0.0_SA_COO~C": {"last_seen_epoch": NOW - 5, "summary": "x"},
            **({reviewer: {"last_seen_epoch": seen, "summary": "x"}} if reviewer else {})}))

    def run(device=None, **kw):
        ctx = sl.Ctx(tmp)
        return check(tmp, sl, ctx, "TEST_PROJ", kw.pop("rnd", None), None, device or this_box, this_box, kind_of, **kw)[1]

    def case(name, line, *want):
        ok = all(x in line for x in want)
        results.append(ok)
        print("%s  %s -> %s" % ("PASS" if ok else "FAIL", name, line if not ok else " ".join(want)))

    try:
        reset()
        w(base + "/task-orders/TEST_PROJ.TO-1.one.md", order.replace("<status>complete</status>", "<status>complete -- landed by someone. Note.</status>"))
        case("a `complete -- <note>` status reads complete with its judgment criterion", run(), "orders=2", "judgment=1", "ungraded=0", "verdict=MAY-CLOSE")
        reset(reviewer=None)
        case("no reviewer on the box is REFUSED", run(), "reviewer=ABSENT", "verdict=REFUSED")
        reset(graded_by="")
        case("an ungraded judgment criterion is REFUSED", run(), "reviewer=present", "ungraded=1", "verdict=REFUSED")
        reset(graded_by="2.0.0_SA_COO~C")
        case("a grade by the order's own issuer is REFUSED", run(), "self_graded=1", "ungraded=1", "verdict=REFUSED")
        reset(graded_by="0.9.0_WK_TEST_PROJ~1")
        case("a grade by the order's own assignee is REFUSED", run(), "self_graded=1", "verdict=REFUSED")
        reset(reviewer="3.0.0_SA_CVO~TEST")
        line = run()
        case("a macro reviewer satisfies", line, "reviewer=present", "graded=1", "verdict=MAY-CLOSE")
        reset()
        case("all present is MAY-CLOSE", run(), "orders=2", "judgment=1", "graded=1", "ungraded=0", "self_graded=0", "verdict=MAY-CLOSE")
        reset(where="investigation")
        case("a CVO-kind row in the investigation file grades", run(), "graded=1", "verdict=MAY-CLOSE")
        # D1-S15 (ETFS_RIVALS round 28): a header-only grade reads GRADED; a mention without a verdict reads UNGRADED.
        reset(graded_by="")
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md",
          "# round 1 L9\n\nAuthor: 3.0.0_SA_CVO, 2026-10-12.\n\n**TEST_PROJ.TO-1 T1-AC2 MET.** The grade is written in this header only.\n")
        case("a header-only grade by a CVO-kind author reads GRADED", run(), "graded=1", "ungraded=0", "verdict=MAY-CLOSE")
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md",
          "# round 1 L9\n\nAuthor: 3.0.0_SA_CVO, 2026-10-12.\n\n**TEST_PROJ.TO-1 T1-AC2 HELD:** no page is published yet.\n")
        case("a header that names the criterion HELD is not a grade", run(), "graded=0", "ungraded=1", "verdict=REFUSED")
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md",
          "# round 1 L9\n\nAuthor: 2.0.0_SA_COO~C, 2026-10-12.\n\n**TEST_PROJ.TO-1 T1-AC2 MET.**\n")
        case("a header grade by the order's own issuer is not a grade", run(), "graded=0", "verdict=REFUSED")
        reset()
        bare = {"id": "TEST_PROJ-C-S2", "surfaced_by": "3.0.0_SA_CVO", "one_line": "Read T1-AC2 and its instance beside the packet."}
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "```json\n%s\n```\n" % json.dumps([bare]))
        case("a mention without a verdict reads UNGRADED by default", run(), "graded=0", "ungraded=1", "verdict=REFUSED")
        case("--loose-grades keeps the older mention reading", run(strict_grades=False), "graded=1", "verdict=MAY-CLOSE")
        verdict_row = {"id": "TEST_PROJ-C-S3", "surfaced_by": "3.0.0_SA_CVO", "one_line": "TEST_PROJ.TO-1 T1-AC2: MET on this seat's read."}
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "```json\n%s\n```\n" % json.dumps([verdict_row]))
        case("a row with the verdict word grades under --strict-grades", run(strict_grades=True), "graded=1", "verdict=MAY-CLOSE")
        struct_row = {"id": "TEST_PROJ-C-S4", "surfaced_by": "3.0.0_SA_CVO",
                      "grades": [{"criterion": "T1-AC2", "instance": "x/TEST_PROJ.TO-1.one.proof_of_spec.json@abc", "verdict": "PASS"}]}
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "```json\n%s\n```\n" % json.dumps([struct_row]))
        case("a structured `grades` entry with a verdict grades under --strict-grades", run(strict_grades=True), "graded=1", "verdict=MAY-CLOSE")
        # A generic id (AC2): a CVO row naming AC2 only through another object (rl9.AC2.sh) must not grade this order.
        reset()
        w(base + "/task-orders/TEST_PROJ.TO-1.one.md", order.replace("T1-AC2", "AC2"))
        w(base + "/deliverables/0.9.0_WK_TEST_PROJ~1/TEST_PROJ.TO-1.one.proof_of_spec.json", json.dumps(
            {"to_id": "TEST_PROJ.TO-1", "acceptance": [
                {"criterion_id": "T1-AC1", "status": "PASS"},
                {"criterion_id": "AC2", "status": "UNVERIFIABLE-BY-INSTRUMENT", "judgment": True}]}))
        stale = {"id": "TEST_PROJ-C-S9", "surfaced_by": "3.0.0_SA_CVO", "evidence": ["checks/rl9.AC2.sh re-run: PASS"]}
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "```json\n%s\n```\n" % json.dumps([stale]))
        case("a generic AC id named only by another object does not grade", run(), "graded=0", "ungraded=1", "verdict=REFUSED")
        stale["adjudicates"] = "TEST_PROJ.TO-1 AC2 MET"
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "```json\n%s\n```\n" % json.dumps([stale]))
        case("a generic AC id with the order named grades", run(), "graded=1", "verdict=MAY-CLOSE")
        # A generic J id (J2) is scoped the same way: a CVO row from ANOTHER round's order must not grade this one.
        reset()
        w(base + "/task-orders/TEST_PROJ.TO-1.one.md", order.replace("T1-AC2", "J2"))
        w(base + "/deliverables/0.9.0_WK_TEST_PROJ~1/TEST_PROJ.TO-1.one.proof_of_spec.json", json.dumps(
            {"to_id": "TEST_PROJ.TO-1", "acceptance": [
                {"criterion_id": "T1-AC1", "status": "PASS"},
                {"criterion_id": "J2", "status": "UNVERIFIABLE-BY-INSTRUMENT", "judgment": True}]}))
        other = {"id": "TEST_PROJ-C-S8", "surfaced_by": "3.0.0_SA_CVO", "adjudicates": "TEST_PROJ.TO-9 J2"}
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "```json\n%s\n```\n" % json.dumps([other]))
        case("a generic J id graded on another round's order does not grade", run(), "graded=0", "ungraded=1", "verdict=REFUSED")
        other["adjudicates"] = "TEST_PROJ.TO-1 J2 MET"
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "```json\n%s\n```\n" % json.dumps([other]))
        case("a generic J id with the order named grades", run(), "graded=1", "verdict=MAY-CLOSE")
        reset(seen=NOW - 100000)
        case("a CVO seat gone stale is ABSENT", run(), "reviewer=ABSENT", "verdict=REFUSED")
        reset(proof=False)
        case("a complete order with no proof instance is REFUSED", run(), "verdict=REFUSED")
        reset()
        case("a round with no orders in it still needs the reviewer line", run(rnd=9), "orders=0", "judgment=0", "verdict=MAY-CLOSE")
        reset()
        case("another box with no seats.json reads UNREAD, never present", run(device=other_box), "reviewer=UNREAD", "verdict=REFUSED")
        doc = {"schema": sl.SCHEMA, "device": other_box, "written_at": sl.stamp(NOW - 600), "written_by": "x",
               "rows": [{"serial": "3.0.0_SA_CVO", "kind": "CVO", "liveness": "LIVE", "last_seen_minutes": 1, "summary": "",
                         "project": None, "drive": None, "drive_cite": None, "open_orders": None,
                         "last_commit_minutes": "NEVER", "doing": "IDLE"}]}
        w("org/devices/state/%s/seats.json" % other_box, json.dumps(doc))
        case("another box with a fresh seats.json naming a live CVO is present", run(device=other_box), "reviewer=present", "verdict=MAY-CLOSE")
        doc["written_at"] = sl.stamp(NOW - 100000)
        w("org/devices/state/%s/seats.json" % other_box, json.dumps(doc))
        case("another box's seats.json older than the limit is UNREAD", run(device=other_box), "reviewer=UNREAD", "verdict=REFUSED")
        reset()
        _lines, last = check(tmp, sl, sl.Ctx(tmp), None, None, None, this_box, this_box, kind_of, reviewer_only=True)
        case("--reviewer-only reads the first limb alone", last, "project=-", "reviewer=present", "verdict=MAY-CLOSE")
        # --staged reads the index, not the working tree: a proof the index lacks is absent though the file is on disk.
        reset()
        genv = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        inst_rel = base + "/deliverables/0.9.0_WK_TEST_PROJ~1/TEST_PROJ.TO-1.one.proof_of_spec.json"

        def g(*args):
            return subprocess.run(["git", "-C", tmp] + list(args), capture_output=True, env=genv).returncode

        def run_staged(**kw):
            return check(tmp, sl, sl.Ctx(tmp), "TEST_PROJ", None, None, this_box, this_box, kind_of, staged=True, env=genv, **kw)[1]

        git_ok = g("init", "-q") == 0 and g("add", "-A") == 0
        results.append(git_ok)
        print("%s  --staged selftest repo built" % ("PASS" if git_ok else "FAIL"))
        if git_ok:
            case("--staged with everything in the index is MAY-CLOSE", run_staged(), "orders=2", "graded=1", "verdict=MAY-CLOSE")
            rm_ok = g("rm", "--cached", "-q", "--", inst_rel) == 0
            case("--staged: a proof the index lacks is not graded as present", run_staged() if rm_ok else "git rm failed",
                 "verdict=REFUSED")
            case("without --staged the same working tree still reads the proof", run(), "verdict=MAY-CLOSE")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    ok = all(results)
    print("ROUND-CLOSE-SELFTEST cases=%d/%d ok=%s" % (sum(results), len(results), ok))
    return 0 if ok else 1


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(prog="round-close-check.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project")
    ap.add_argument("--round")
    ap.add_argument("--workstream")
    ap.add_argument("--device")
    ap.add_argument("--deep", action="store_true")
    ap.add_argument("--max-age-minutes", type=int, default=DEFAULT_MAX_AGE_MIN)
    ap.add_argument("--reviewer-only", action="store_true")
    ap.add_argument("--staged", action="store_true", help="read the project's files from the git index, not the working tree")
    ap.add_argument("--strict-grades", action="store_true",
                    help="the default: a judgment criterion is graded only by a verdict word (or a `grades` entry)")
    ap.add_argument("--loose-grades", action="store_true",
                    help="escape: a fenced row grades by any mention of the criterion (the report prints LOOSE-GRADES IN USE)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    try:
        if not args.project and not args.reviewer_only:
            raise Usage("--project <CODE> is required (or --reviewer-only for a job with no project)")
        sl = load_mod("opal_seat_list_m", os.path.join(TOOLS, "seat-list.py"))
        this_box = resolve_this_box(ROOT)
        lines, last = check(ROOT, sl, sl.Ctx(None), args.project, args.round, args.workstream, args.device or this_box,
                            this_box, sl.kind_resolver(), deep=args.deep, max_age=args.max_age_minutes,
                            reviewer_only=args.reviewer_only, staged=args.staged, strict_grades=not args.loose_grades)
    except Usage as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2
    for ln in lines:
        print(ln)
    print(last)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
