#!/usr/bin/env python3
"""round-close-check.py -- may this round be counted finished on this box? (NFRA_CTLPLN workstream SEATS, cell CT-s-8;
contract C-SEATS clause 7; FWD-23.)

Andrew's word (2026-10-07 ~16:3xZ): "CVO is dedicated reviewer in those drive processes so mandatory spawn on any fabric.
If there are multiple projects attached to one macro on a fabric, it is best practice to spawn a CVO specific to that
macro, e.g. CVO~NFRA."  FWD-23: a piece of work is not counted finished until a seat that did none of it has graded it, on
the box where it was done.

    python .tools/round-close-check.py --project <CODE> [--round <n>] [--workstream <WS>] [--device <d>] [--deep]
    python .tools/round-close-check.py --reviewer-only [--device <d>]       (a remote job: no project, no round)
    python .tools/round-close-check.py --selftest

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
BLIND (stated): whether a grade is a GOOD grade. This tool sees that a different CVO-kind seat wrote a row naming the
criterion, not what the row says. Orders not yet `complete` are listed and do not enter the verdict (a round with an open
order is the issuer's to close, not this tool's to read).

LAST line (always):
  ROUND-CLOSE project=<CODE> device=<d> reviewer=<present|ABSENT|UNREAD> orders=<n> judgment=<j> graded=<g> ungraded=<u> self_graded=<s> verdict=<MAY-CLOSE|REFUSED>
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

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
DEFAULT_MAX_AGE_MIN = 120
LANE = re.compile(r"~([A-Za-z0-9]+)$")
FENCE = re.compile(r"```json\s*\n(.*?)```", re.S)
CRIT_TAG = re.compile(r"<criterion\b([^>]*?)/?>")
ATTR = re.compile(r'([A-Za-z_]+)="([^"]*)"')


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


def last_status(text: str, words: set) -> str:
    """The LAST <status> tag whose word is a status word (CTO ruling msg 107528)."""
    got = ""
    for m in re.finditer(r"^<status>(.*?)</status>", text, re.M):
        w = m.group(1).strip().lower()
        if w in words:
            got = w
    return got


def read_orders(proj_dir: str, rnd, ws) -> list:
    out = []
    words = status_words()
    for path in sorted(glob.glob(os.path.join(proj_dir, "task-orders", "*.md"))):
        text = open(path, encoding="utf-8", errors="replace").read()
        o = {"path": path, "stem": os.path.basename(path)[:-3], "id": tag(text, "to_id") or os.path.basename(path)[:-3],
             "status": last_status(text, words), "round": tag(text, "round"),
             "workstream": tag(text, "workstream"), "issued_by": tag(text, "issued_by") or "",
             "issued_to": tag(text, "issued_to") or "", "criteria": []}
        for m in CRIT_TAG.finditer(text):
            attrs = dict(ATTR.findall(m.group(1)))
            if "id" in attrs:
                o["criteria"].append({"id": attrs["id"], "judgment": attrs.get("judgment", "").lower() == "true"})
        if rnd is not None and str(o["round"]) != str(rnd):
            continue
        if ws is not None and str(o["workstream"]) != str(ws):
            continue
        out.append(o)
    return out


def proof_state(order: dict, proj_dir: str, root: str, deep: bool) -> tuple:
    """(ok, reason). Structural by default; --deep adds proof-of-spec-check.py (rc 0 = VALID)."""
    paths = sorted(glob.glob(os.path.join(proj_dir, "deliverables", "*", order["stem"] + ".proof_of_spec.json")))
    if not paths:
        return False, "no proof instance named %s.proof_of_spec.json under deliverables/" % order["stem"]
    reasons = []
    want = [c["id"] for c in order["criteria"]]
    for path in paths:
        try:
            inst = json.load(open(path, encoding="utf-8"))
            rows = inst["acceptance"]
            have = {r.get("criterion_id") for r in rows}
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
            reasons.append("%s unreadable (%s)" % (os.path.basename(os.path.dirname(path)), exc))
            continue
        if str(inst.get("to_id", "")).strip() != order["id"]:
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
                rc = subprocess.run([sys.executable, checker, path, ",".join(want)], capture_output=True, text=True,
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

def load_rows(files: list) -> tuple:
    """[(file, row dict)], count of fenced blocks that did not parse (printed, never silent)."""
    rows, bad = [], 0
    for path in files:
        text = open(path, encoding="utf-8", errors="replace").read()
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


def grade_criterion(crit_id: str, order: dict, adj_rows: list, inv_rows: list, kind_of) -> tuple:
    """(state GRADED|SELF|UNGRADED, detail). Adjudication-file rows: a doer is a self-grade, a CVO-kind non-doer a grade.
    Investigation-file rows: only a CVO-kind author counts (a doer's own surprise rows name criteria all the time and are
    not grades); a CVO-kind doer is a self-grade."""
    pat = re.compile(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(crit_id))
    # A generic id (AC3) is a substring of every order's AC3 and of any check-script name (rl9.AC3.sh): the row must
    # also name THIS order (its to_id or the short id after "TO-"), or a stale row from another round grades it.
    short = order["id"].split(".TO-", 1)[-1]
    order_pat = None
    if re.fullmatch(r"AC\d+[a-z]?", crit_id):
        names = [re.escape(order["id"]), "TO-" + re.escape(short)] + ([re.escape(short)] if re.search(r"[A-Za-z]", short) else [])
        order_pat = re.compile(r"(?<![A-Za-z0-9])(?:%s)(?![A-Za-z0-9])" % "|".join(names))
    doers = {base_of(order["issued_by"]), base_of(order["issued_to"])} - {""}
    self_hit = None
    for source, rows in (("adjudication", adj_rows), ("investigation", inv_rows)):
        for _path, row in rows:
            text = json.dumps(row)
            if not pat.search(text) or (order_pat and not order_pat.search(text)):
                continue
            who = author_of(row)
            if not who:
                continue
            is_doer = base_of(who) in doers
            is_cvo = kind_of(who) == "CVO"
            if is_cvo and not is_doer:
                return "GRADED", "%s row %s by %s" % (source, row.get("id", "?"), who)
            if is_doer and (source == "adjudication" or is_cvo):
                self_hit = self_hit or "%s row %s by %s, the order's own %s" % (
                    source, row.get("id", "?"), who, "issuer" if base_of(who) == base_of(order["issued_by"]) else "assignee")
    if self_hit:
        return "SELF", self_hit
    return "UNGRADED", "no CVO-kind row names it"


# ---------------------------------------------------------------- the whole check

def find_project(root: str, code: str) -> str:
    hits = glob.glob(os.path.join(root, "org", "missions", "D*", "*", code, "project.json"))
    if len(hits) != 1:
        raise Usage("project %s: %d project.json found under org/missions/D*/*/ (want exactly 1)" % (code, len(hits)))
    return os.path.dirname(hits[0])


def check(root: str, sl, ctx, code, rnd, ws, device, this_box, kind_of, deep=False, max_age=DEFAULT_MAX_AGE_MIN,
          reviewer_only=False) -> tuple:
    """(lines, last_line)."""
    lines = []
    macro = ""
    proj_dir = None
    if not reviewer_only:
        proj_dir = find_project(root, code)
        try:
            macro = json.load(open(os.path.join(proj_dir, "project.json"), encoding="utf-8")).get("macro_code", "")
        except (OSError, ValueError):
            macro = ""
    rv = reviewer_limb(sl, ctx, device, this_box, kind_of, macro, max_age)
    who = ", ".join("%s%s" % (s, " (macro reviewer for %s)" % macro if m else "") for s, m in rv["who"]) or "none"
    lines.append("REVIEWER-ON-BOX device=%s state=%s reviewer seat(s)=%s" % (device, rv["state"], who))
    lines.append("  source: %s; %s" % (rv["source"], rv["note"]))
    n_orders = n_j = n_g = n_s = 0
    if reviewer_only:
        verdict = "MAY-CLOSE" if rv["state"] == "present" else "REFUSED"
        return lines, "ROUND-CLOSE project=- device=%s reviewer=%s orders=0 judgment=0 graded=0 ungraded=0 self_graded=0 verdict=%s" % (
            device, rv["state"], verdict)
    orders = read_orders(proj_dir, rnd, ws)
    n_orders = len(orders)
    done = [o for o in orders if o["status"] == "complete"]
    open_ = [o for o in orders if o["status"] not in ("complete", "superseded", "cancelled", "canceled", "withdrawn", "retired")]
    lines.append("ORDERS scope round=%s workstream=%s: %d order(s), %d complete, %d not complete and outside the verdict%s" % (
        rnd if rnd is not None else "all", ws if ws is not None else "all", n_orders, len(done), len(open_),
        (" (" + ", ".join(o["id"].split(".")[-1] for o in open_) + ")") if open_ else ""))
    bad_proofs = 0
    for o in done:
        ok, why = proof_state(o, proj_dir, root, deep)
        if not ok:
            bad_proofs += 1
            lines.append("  PROOF-BAD %s: %s" % (o["id"], why))
    lines.append("PROOFS mode=%s complete=%d proof_ok=%d proof_bad=%d" % ("deep" if deep else "structural", len(done),
                                                                         len(done) - bad_proofs, bad_proofs))
    adj_files = sorted(glob.glob(os.path.join(proj_dir, "surprise-channel", "adjudications", "ADJUDICATION_v*.md")))
    inv_files = sorted(glob.glob(os.path.join(proj_dir, "surprise-channel", "investigations", "INVESTIGATION_v*.md")))
    adj_rows, bad_a = load_rows(adj_files)
    inv_rows, bad_i = load_rows(inv_files)
    lines.append("GRADING-ROWS adjudication=%d row(s) in %d file(s), investigation=%d row(s) in %d file(s), %d json block(s) did not parse" % (
        len(adj_rows), len(adj_files), len(inv_rows), len(inv_files), bad_a + bad_i))
    for o in done:
        for c in o["criteria"]:
            if not c["judgment"]:
                continue
            n_j += 1
            state, why = grade_criterion(c["id"], o, adj_rows, inv_rows, kind_of)
            if state == "GRADED":
                n_g += 1
            if state == "SELF":
                n_s += 1
            lines.append("  JUDGMENT %s %s -> %s (%s)" % (o["id"].split(".")[-1], c["id"], state, why))
    n_u = n_j - n_g
    ok = rv["state"] == "present" and n_u == 0 and n_s == 0 and bad_proofs == 0
    return lines, "ROUND-CLOSE project=%s device=%s reviewer=%s orders=%d judgment=%d graded=%d ungraded=%d self_graded=%d verdict=%s" % (
        code, device, rv["state"], n_orders, n_j, n_g, n_u, n_s, "MAY-CLOSE" if ok else "REFUSED")


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
        row = {"id": "TEST_PROJ-C-S1", "surfaced_by": graded_by, "adjudicates": ["T1-AC2"]}
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
        stale["adjudicates"] = "TEST_PROJ.TO-1 AC2"
        w(base + "/surprise-channel/adjudications/ADJUDICATION_v1.md", "```json\n%s\n```\n" % json.dumps([stale]))
        case("a generic AC id with the order named grades", run(), "graded=1", "verdict=MAY-CLOSE")
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
                            reviewer_only=args.reviewer_only)
    except Usage as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 2
    for ln in lines:
        print(ln)
    print(last)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
