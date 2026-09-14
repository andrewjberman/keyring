#!/usr/bin/env python3
"""sequence-check.py -- THE SEQUENCE viewer. VIEW-TIME COMPILED, like schedule-check.py.

Reads org/missions/SEQUENCE.yaml -- the order of the projects that must run in sequence across both fabrics, and the
gates between them -- and joins it, at the moment you run it, to the register: each project's dep_stage and status
(org/projects/<CODE>.json), its PRD sign-off (.tools/prd_signoff_lib.py evaluate(), the one rule, never re-derived
here), and its last activity (git). SEQUENCE.yaml carries no status and nothing here is cached, so nothing can go stale.

AUTHORITY: Andrew-direct 2026-09-14 ~01:xxZ, record org/tier1_exec/1.0.0_SA_CTO/deliverables/
ANDREW_DIRECT_20260914_01xxZ_LAPTOP_SEQUENCE_DOCUMENT_APPROVED.md @cc79b6191a.

WHAT IT FLAGS, per project:
  OUT-OF-SEQUENCE  past its hold's max_dep_stage while a gate of that hold is unmet
  WAITING          a waits_on gate is unmet: it may not start yet (not a violation)
  HELD             a hold gate is unmet and it sits at or below its cap (not a violation)
  READY-IDLE       every gate met, not complete, and no commit under its home for IDLE_DAYS
  DRIFT            the file and the repo disagree (a code the register lacks, a fabric the register contradicts)
  UNMEASURED       a manual gate with no `confirmed` line: no tool can check it
  UNREADABLE       a source that could not be read -- never rendered as a pass
  NEEDS-SLOT       its PRD is admitted and its next step is a COO's (L5), but its tree row names no coo_lane. While the
                   box is at its COO cap it waits for a slot, and slots go in the file's order (not a violation)

CAPACITY (Andrew-direct 2026-09-14 ~07:0xZ, "We can only have 3 COOs running their respective projects/subagents at
any one time"): the live COO lanes on THIS box, read from the broker's org/mcp/liveness.json (a 2.0.0_SA_COO lane seen
within LIVE_SECONDS, the broker's own LIVE threshold), set beside the file's per-fabric cap. The box's fabric comes
from the checked-out branch (CLOUD -> laptop, SITEZ -> sitez). A liveness row is the broker's claim, not process
truth, and the line says which instrument it read.

A VIEWER, NOT A CHECKER: findings never change the exit code (the monitor moratorium; Andrew ~01:xxZ card 1 chose
TRACK). Exit 0 rendered; 1 nothing rendered (the sequence file unreadable); 2 rendered with >=1 UNREADABLE source;
3 a --project code resolves to NOTHING -- neither the sequence nor the register holds it, which is almost always a
typo, and a typo must never read as a clean pass (1.0.0_SA_CTO~Z msg 22541: a mistyped ADVI_FIRMBKTS read
"FLAGS: none", rc=0, and a seat would have walked past its HOLD). Every --project code is resolved and named:
PLACED, PARKED, PENDING-PLACEMENT, UNPLACED (a register project the file does not list) or UNKNOWN.

Usage:
  sequence-check.py              the sequence, stage by stage, with live status and flags
  sequence-check.py --flags      only projects carrying a flag
  sequence-check.py --project X  one project (repeatable)
  sequence-check.py --json       machine-readable
  sequence-check.py --self-test  the evaluator against planted cases (no repo read)
"""
from __future__ import annotations

import argparse
import ast
import datetime
import difflib
import glob
import importlib.util
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEQ_REL = "org/missions/SEQUENCE.yaml"
IDLE_DAYS = 7
STAGES = ("REGISTERED", "PRD", "DECOMP", "EXECUTING", "ROUND_CLOSE", "CLOSED")
TOP_KEYS = {"version", "owners", "enforcement", "capacity", "stages", "projects", "parked", "pending_placement",
            "supersedes", "change_log"}
PROJECT_KEYS = {"fabric", "stage", "waits_on", "hold", "why", "notes"}
GATE_FORMS = ("prd_admitted", "dep_stage_at_least", "status", "manual")
LIVE_SECONDS = 120          # org/mcp/server.py STALE_THRESHOLD: a registration older than this is not LIVE
COO_BASE = "2.0.0_SA_COO"
BRANCH_FABRIC = {"CLOUD": "laptop", "SITEZ": "sitez"}


def _gate_enum_matches():
    """The dep_stage order is the L6 gate's own enum, read by AST -- never a second copy that can drift."""
    try:
        tree = ast.parse(open(os.path.join(ROOT, ".tools", "to-pipeline-gate.py"), encoding="utf-8").read())
    except Exception as exc:  # noqa: BLE001
        return False, "to-pipeline-gate.py unreadable (%s)" % exc
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "DEP_STAGE_ENUM" for t in node.targets):
            val = tuple(ast.literal_eval(node.value))
            return val == STAGES, "DEP_STAGE_ENUM=%s" % (val,)
    return False, "DEP_STAGE_ENUM not found"


def _stage_index(s):
    return STAGES.index(s) if s in STAGES else None


class Reader:
    """Live reads. Every method returns (value, note); value None means UNREADABLE, never a zero."""

    def __init__(self, root):
        self.root = root
        self._lib = None

    def row(self, code):
        p = os.path.join(self.root, "org", "projects", code + ".json")
        if not os.path.isfile(p):
            return None, "no register row org/projects/%s.json" % code
        try:
            return json.load(open(p, encoding="utf-8")), "org/projects/%s.json" % code
        except Exception as exc:  # noqa: BLE001
            return None, "register row unreadable (%s)" % exc

    def _signoff_lib(self):
        if self._lib is None:
            spec = importlib.util.spec_from_file_location("prd_signoff_lib", os.path.join(self.root, ".tools", "prd_signoff_lib.py"))
            lib = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(lib)
            self._lib = lib
        return self._lib

    def prd_admitted(self, code, row):
        home = (row or {}).get("home")
        if not home:
            return None, "no tree home on the register row, so no PRD location to read"
        prd = os.path.join(self.root, home, "prd", code + "_PRD.md")
        if not os.path.isfile(prd):
            return False, "no PRD at %s/prd/%s_PRD.md" % (home, code)
        files = {}
        for f in sorted(glob.glob(os.path.join(self.root, home, "prd", "signoff", "*.json"))):
            try:
                files[os.path.basename(f)] = json.load(open(f, encoding="utf-8"))
            except Exception:  # noqa: BLE001
                files[os.path.basename(f)] = None
        try:
            res = self._signoff_lib().evaluate(open(prd, encoding="utf-8").read(), files)
        except Exception as exc:  # noqa: BLE001
            return None, "prd_signoff_lib.evaluate failed (%s)" % exc
        halves = ", ".join("%s %s" % (h, v["state"]) for h, v in sorted(res["halves"].items()) if not h.startswith("_"))
        return bool(res["admitted"]), "%s %s (%s)" % (res.get("prd_version") or "?", "ADMITTED" if res["admitted"] else "WITHHELD", halves)

    def tree_row(self, row):
        home = (row or {}).get("home")
        if not home:
            return None, "no tree home"
        p = os.path.join(self.root, home, "project.json")
        try:
            return json.load(open(p, encoding="utf-8")), "%s/project.json" % home
        except Exception as exc:  # noqa: BLE001
            return None, "tree row unreadable (%s)" % exc

    def coo_sessions(self):
        """Live COO lanes on THIS box, from the broker's liveness file. None means UNREADABLE, never zero."""
        p = os.path.join(self.root, "org", "mcp", "liveness.json")
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            return None, "org/mcp/liveness.json unreadable (%s)" % exc
        now = datetime.datetime.now(datetime.timezone.utc).timestamp()
        live = sorted(k for k, v in d.items() if isinstance(v, dict) and k.split("~")[0] == COO_BASE
                      and isinstance(v.get("last_seen_epoch"), (int, float)) and now - v["last_seen_epoch"] <= LIVE_SECONDS)
        return live, "org/mcp/liveness.json (%d registrations; LIVE = seen within %ds)" % (len(d), LIVE_SECONDS)

    def box_fabric(self):
        r = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=self.root, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        branch = r.stdout.strip()
        return BRANCH_FABRIC.get(branch), "branch %s" % (branch or "?")

    def last_activity(self, row):
        home = (row or {}).get("home")
        if not home:
            return None, "no tree home"
        r = subprocess.run(["git", "log", "-1", "--format=%h %aI", "--", home], cwd=self.root, capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        out = r.stdout.strip()
        if r.returncode != 0 or not out:
            return None, "git log returned nothing for %s" % home
        return out, home


def eval_gate(gate, reader, cache):
    """-> (state, text). state in MET, UNMET, UNMEASURED, UNREADABLE."""
    if not isinstance(gate, dict):
        return "UNREADABLE", "gate is not a mapping: %r" % (gate,)
    forms = [k for k in gate if k in GATE_FORMS]
    if len(forms) != 1 or (forms[0] != "manual" and "project" not in gate):
        return "UNREADABLE", "gate %r is not one of the four forms" % (gate,)
    form = forms[0]
    if form == "manual":
        if gate.get("confirmed"):
            return "MET", "manual, CONFIRMED: %s" % gate["confirmed"]
        return "UNMEASURED", "manual: %s" % gate["manual"]
    code = gate["project"]
    if code not in cache:
        cache[code] = reader.row(code)
    row, note = cache[code]
    if row is None:
        return "UNREADABLE", "%s: %s" % (code, note)
    if form == "prd_admitted":
        ok, why = reader.prd_admitted(code, row)
        if ok is None:
            return "UNREADABLE", "%s PRD: %s" % (code, why)
        return ("MET" if ok else "UNMET"), "%s PRD admitted? %s" % (code, why)
    if form == "dep_stage_at_least":
        want, have = _stage_index(gate["dep_stage_at_least"]), _stage_index(row.get("dep_stage"))
        if want is None:
            return "UNREADABLE", "unknown stage %r in the gate" % gate["dep_stage_at_least"]
        if have is None:
            return "UNMET", "%s dep_stage=%r, gate needs >= %s" % (code, row.get("dep_stage"), gate["dep_stage_at_least"])
        return ("MET" if have >= want else "UNMET"), "%s dep_stage=%s, gate needs >= %s" % (code, row.get("dep_stage"), gate["dep_stage_at_least"])
    want = gate["status"]
    return ("MET" if row.get("status") == want else "UNMET"), "%s status=%r, gate needs %r" % (code, row.get("status"), want)


def validate(doc):
    errs = []
    if not isinstance(doc, dict):
        return ["the file is not a mapping"]
    for k in doc:
        if k not in TOP_KEYS:
            errs.append("unknown top-level key %r" % k)
    stage_ids = {s.get("id") for s in doc.get("stages") or [] if isinstance(s, dict)}
    for code, p in (doc.get("projects") or {}).items():
        if not isinstance(p, dict):
            errs.append("%s: not a mapping" % code)
            continue
        for k in p:
            if k not in PROJECT_KEYS:
                errs.append("%s: unknown key %r" % (code, k))
        if p.get("stage") not in stage_ids:
            errs.append("%s: stage %r is not a declared stage" % (code, p.get("stage")))
        hold = p.get("hold")
        if hold is not None and _stage_index((hold or {}).get("max_dep_stage")) is None:
            errs.append("%s: hold.max_dep_stage %r is not a dep_stage" % (code, (hold or {}).get("max_dep_stage")))
    return errs


def evaluate(doc, reader, idle_days=IDLE_DAYS, now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    cache, rows = {}, []
    for code, p in (doc.get("projects") or {}).items():
        if code not in cache:
            cache[code] = reader.row(code)
        row, rnote = cache[code]
        flags, notes = [], []
        entry = {"project": code, "stage": p.get("stage"), "fabric": p.get("fabric"), "flags": flags, "notes": notes,
                 "gates": []}
        if row is None:
            flags.append("DRIFT" if "no register row" in rnote else "UNREADABLE")
            notes.append(rnote)
            rows.append(entry)
            continue
        entry.update({"dep_stage": row.get("dep_stage"), "status": row.get("status")})
        if row.get("fabric") and p.get("fabric") and str(row.get("fabric")).lower() != str(p.get("fabric")).lower():
            flags.append("DRIFT")
            notes.append("fabric: the file says %r, the register row says %r" % (p.get("fabric"), row.get("fabric")))
        ok, why = reader.prd_admitted(code, row)
        entry["prd"] = why if ok is not None else "UNREADABLE: " + why
        act, anote = reader.last_activity(row)
        entry["last_activity"] = act or ("UNREADABLE: " + anote)
        waits = [eval_gate(g, reader, cache) + ("waits_on",) for g in p.get("waits_on") or []]
        hold = p.get("hold") or {}
        holds = [eval_gate(g, reader, cache) + ("hold",) for g in hold.get("until") or []]
        entry["gates"] = [{"kind": k, "state": s, "detail": t} for s, t, k in waits + holds]
        states = [s for s, _, _ in waits + holds]
        if "UNREADABLE" in states:
            flags.append("UNREADABLE")
        if "UNMEASURED" in states:
            flags.append("UNMEASURED")
        if any(s != "MET" for s, _, _ in waits):
            flags.append("WAITING")
        hold_open = holds and any(s != "MET" for s, _, _ in holds)
        if hold_open:
            cap, have = _stage_index(hold.get("max_dep_stage")), _stage_index(row.get("dep_stage"))
            if have is not None and cap is not None and have > cap:
                flags.append("OUT-OF-SEQUENCE")
                notes.append("dep_stage %s is past the hold's cap %s while a hold gate is unmet" % (row.get("dep_stage"), hold.get("max_dep_stage")))
            else:
                flags.append("HELD")
        # NEEDS-SLOT: admitted, at PRD (so L5 is next, and L5 is a COO's), no lane seated, not waiting, and any open
        # hold still lets it reach DECOMP.
        if ok and row.get("dep_stage") == "PRD" and "WAITING" not in flags:
            cap_ok = not hold_open or (_stage_index(hold.get("max_dep_stage")) or 0) >= _stage_index("DECOMP")
            trow, tnote = reader.tree_row(row)
            if trow is None:
                notes.append("tree row: " + tnote)
            elif cap_ok and not trow.get("coo_lane"):
                flags.append("NEEDS-SLOT")
                notes.append("PRD admitted; L5 is next and is a COO's; no coo_lane on the tree row")
        all_met = all(s == "MET" for s in states)
        if all_met and row.get("status") != "complete" and act:
            try:
                when = datetime.datetime.fromisoformat(act.split(" ", 1)[1])
                if (now - when).days >= idle_days:
                    flags.append("READY-IDLE")
                    notes.append("every gate met; no commit under its home for %d days" % (now - when).days)
            except Exception:  # noqa: BLE001
                pass
        rows.append(entry)
    return rows


def _register_codes(root):
    return {os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(root, "org", "projects", "*.json"))}


def resolve_codes(doc, codes, register):
    """PURE. Each --project code -> (code, state, detail), state in PLACED / PARKED / PENDING-PLACEMENT / UNPLACED /
    UNKNOWN. A code the sequence places reads as before; one it does not is SAID so, never rendered as zero rows."""
    placed = doc.get("projects") or {}
    parked = doc.get("parked") or {}
    pending = {str(p.get("subject")) for p in doc.get("pending_placement") or [] if isinstance(p, dict)}
    known = sorted(set(placed) | set(parked) | set(register))
    out = []
    for code in codes:
        if code in placed:
            out.append((code, "PLACED", "stage %s of the sequence" % placed[code].get("stage")))
        elif code in parked:
            out.append((code, "PARKED", "not ordered; recorded so no driver takes it up ahead of the sequence"))
        elif code in pending:
            out.append((code, "PENDING-PLACEMENT", "a placement question is open in the file; not yet ordered"))
        elif code in register:
            out.append((code, "UNPLACED", "a register project the sequence does not list: not sequenced, so its own directive's rules govern it"))
        else:
            near = difflib.get_close_matches(code, known, n=3, cutoff=0.8)
            out.append((code, "UNKNOWN", "neither the sequence nor the register holds this code"
                        + ("; did you mean %s?" % " or ".join(near) if near else "")))
    return out


def capacity(doc, reader, rows):
    """The COO-capacity read. It never changes a flag and never refuses anything; it says what the slots are."""
    caps = {k: v for k, v in ((doc.get("capacity") or {}).get("coo_sessions") or {}).items() if isinstance(v, int)}
    live, note = reader.coo_sessions()
    fabric, fnote = reader.box_fabric()
    order = {code: i for i, code in enumerate((doc.get("projects") or {}))}
    queue = sorted((r for r in rows if "NEEDS-SLOT" in r["flags"]), key=lambda r: (r.get("stage") or 0, order.get(r["project"], 0)))
    cap = caps.get(fabric) if fabric else None
    return {"caps": caps, "box_fabric": fabric, "box_note": fnote, "cap": cap, "live": live, "note": note,
            "at_cap": (live is not None and cap is not None and len(live) >= cap),
            "queue": [r["project"] for r in queue]}


def render_capacity(c):
    caps = ", ".join("%s %d" % kv for kv in sorted(c["caps"].items())) or "none declared"
    if c["live"] is None:
        print("\nCAPACITY: COO lanes UNREADABLE (%s) | caps: %s" % (c["note"], caps))
    else:
        state = "AT CAP" if c["at_cap"] else ("no cap ruled for this box" if c["cap"] is None else "%d free" % (c["cap"] - len(c["live"])))
        print("\nCAPACITY: %d live COO lane(s) on this box (%s, %s): %s | cap %s | %s | source: %s" % (
            len(c["live"]), c["box_fabric"] or "fabric unknown", c["box_note"], ", ".join(c["live"]) or "-",
            c["cap"] if c["cap"] is not None else "-", state, c["note"]))
    if c["queue"]:
        print("  NEXT COO SLOT, in the sequence's order: %s" % " -> ".join(c["queue"]))


def render(doc, rows, only_flags=False):
    stages = {s["id"]: s for s in doc.get("stages") or [] if isinstance(s, dict)}
    for sid in sorted(stages):
        members = [r for r in rows if r["stage"] == sid and (r["flags"] or not only_flags)]
        if not members and only_flags:
            continue
        print("\nSTAGE %s -- %s" % (sid, stages[sid].get("name")))
        for r in members:
            print("  %-14s %-7s dep_stage=%-10s status=%-8s flags=%s" % (
                r["project"], r.get("fabric"), r.get("dep_stage"), r.get("status"), ",".join(r["flags"]) or "-"))
            print("      prd: %s" % r.get("prd", "-"))
            print("      last activity: %s" % r.get("last_activity", "-"))
            for g in r["gates"]:
                print("      %-8s %-10s %s" % (g["kind"], g["state"], g["detail"][:150]))
            for n in r["notes"]:
                print("      NOTE: %s" % n[:170])
    parked = doc.get("parked") or {}
    if parked and not only_flags:
        print("\nPARKED (%d): %s" % (len(parked), ", ".join(sorted(parked))))
    pend = doc.get("pending_placement") or []
    if pend and not only_flags:
        print("PENDING PLACEMENT (%d): %s" % (len(pend), "; ".join(str(p.get("subject")) for p in pend)))


def self_test():
    class Fake:
        def __init__(self, rows, prd):
            self.rows, self.prd = rows, prd

        def row(self, code):
            if code == "BROKEN":
                return None, "register row unreadable (planted)"
            return (self.rows[code], "fake") if code in self.rows else (None, "no register row org/projects/%s.json" % code)

        def prd_admitted(self, code, row):
            return self.prd.get(code, False), "fake"

        def last_activity(self, row):
            return row.get("_act"), "fake"

        def tree_row(self, row):
            return row.get("_tree", {}), "fake"

        def coo_sessions(self):
            return self.live, "fake"

        def box_fabric(self):
            return "laptop", "fake"

    now = datetime.datetime(2026, 9, 20, tzinfo=datetime.timezone.utc)
    rows = {
        "A": {"dep_stage": "PRD", "status": "active", "fabric": "laptop", "_act": "abc 2026-09-19T00:00:00+00:00",
              "_tree": {"coo_lane": "2.0.0_SA_COO~A"}},
        "G": {"dep_stage": "PRD", "status": "active", "fabric": "laptop", "_act": "abc 2026-09-19T00:00:00+00:00",
              "_tree": {"coo_lane": None}},
        "H": {"dep_stage": "PRD", "status": "active", "fabric": "laptop", "_act": "abc 2026-09-19T00:00:00+00:00",
              "_tree": {"coo_lane": "2.0.0_SA_COO~H"}},
        "B": {"dep_stage": "EXECUTING", "status": "active", "fabric": "laptop", "_act": "abc 2026-09-19T00:00:00+00:00"},
        "C": {"dep_stage": "REGISTERED", "status": "active", "fabric": "laptop", "_act": "abc 2026-09-01T00:00:00+00:00"},
        "D": {"dep_stage": "REGISTERED", "status": "active", "fabric": "site-z", "_act": "abc 2026-09-19T00:00:00+00:00"},
    }
    prd = {"A": True, "G": True, "H": True}
    doc = {"capacity": {"coo_sessions": {"laptop": 3}}, "stages": [{"id": 1, "name": "s"}], "projects": {
        "G": {"fabric": "laptop", "stage": 1, "waits_on": []},
        "H": {"fabric": "laptop", "stage": 1, "waits_on": []},
        "A": {"fabric": "laptop", "stage": 1, "waits_on": []},
        "B": {"fabric": "laptop", "stage": 1, "hold": {"max_dep_stage": "DECOMP", "until": [{"manual": "x"}]}},
        "B2": {"fabric": "laptop", "stage": 1},
        "C": {"fabric": "laptop", "stage": 1, "waits_on": [{"project": "A", "prd_admitted": True}]},
        "D": {"fabric": "laptop", "stage": 1, "hold": {"max_dep_stage": "PRD", "until": [{"project": "C", "dep_stage_at_least": "PRD"}]}},
        "E": {"fabric": "laptop", "stage": 1, "waits_on": [{"project": "BROKEN", "status": "complete"}]},
        "F": {"fabric": "laptop", "stage": 1, "waits_on": [{"project": "A", "bogus": 1}]},
    }}
    rows["E"] = {"dep_stage": "REGISTERED", "status": "active", "fabric": "laptop", "_act": None}
    rows["F"] = {"dep_stage": "REGISTERED", "status": "active", "fabric": "laptop", "_act": None}
    fake = Fake(rows, prd)
    fake.live = ["2.0.0_SA_COO~A", "2.0.0_SA_COO~H", "2.0.0_SA_COO~X"]
    evaluated = evaluate(doc, fake, now=now)
    got = {r["project"]: set(r["flags"]) for r in evaluated}
    cap = capacity(doc, fake, evaluated)
    rdoc = {"projects": {"LGIC_NAMING": {"stage": 1}}, "parked": {"NFRA_X": {}}, "pending_placement": [{"subject": "IRPT_BCKEND"}]}
    rreg = {"LGIC_NAMING", "AMGT_RESAPP", "IRPT_BCKEND"}
    _typo = resolve_codes(rdoc, ["LGIC_NAMNIG"], rreg)[0]
    cases = [
        ("A: no gates, active 1 day ago -> no flag", got["A"] == set()),
        ("B: manual hold unconfirmed, EXECUTING past cap DECOMP -> OUT-OF-SEQUENCE + UNMEASURED", {"OUT-OF-SEQUENCE", "UNMEASURED"} <= got["B"]),
        ("B2: code missing from the register -> DRIFT", got["B2"] == {"DRIFT"}),
        ("C: waits on A's PRD (admitted), idle 19 days -> READY-IDLE only", got["C"] == {"READY-IDLE"}),
        ("D: hold unmet at its cap -> HELD, not OUT-OF-SEQUENCE; fabric contradicts -> DRIFT", got["D"] == {"HELD", "DRIFT"}),
        ("E: gate on an unreadable row -> UNREADABLE + WAITING, never a pass", {"UNREADABLE", "WAITING"} <= got["E"]),
        ("F: gate not in the vocabulary -> UNREADABLE", "UNREADABLE" in got["F"]),
        ("the dep_stage order equals to-pipeline-gate.py's DEP_STAGE_ENUM (read by AST)", _gate_enum_matches()[0]),
        ("validate: an unknown top-level key is refused", validate({"stagez": 1, "projects": {}}) != []),
        ("G: PRD admitted, at PRD, no coo_lane -> NEEDS-SLOT only", got["G"] == {"NEEDS-SLOT"}),
        ("H: PRD admitted, at PRD, a coo_lane seated -> no flag", got["H"] == set()),
        ("capacity: 3 live against a laptop cap of 3 -> AT CAP, and the queue is [G]", cap["at_cap"] and cap["queue"] == ["G"]),
        ("validate: the capacity key is accepted", validate({"capacity": {"coo_sessions": {"laptop": 3}}, "projects": {}}) == []),
        ("resolve: a placed code -> PLACED", resolve_codes(rdoc, ["LGIC_NAMING"], rreg)[0][1] == "PLACED"),
        ("resolve: a one-letter TYPO -> UNKNOWN, with the placed code suggested", _typo[1] == "UNKNOWN" and "LGIC_NAMING" in _typo[2]),
        ("resolve: a register code the file does not list -> UNPLACED, never zero rows", resolve_codes(rdoc, ["AMGT_RESAPP"], rreg)[0][1] == "UNPLACED"),
        ("resolve: parked and pending-placement codes say which", [s for _, s, _ in resolve_codes(rdoc, ["NFRA_X", "IRPT_BCKEND"], rreg)] == ["PARKED", "PENDING-PLACEMENT"]),
    ]
    fails = 0
    for name, ok in cases:
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        fails += 0 if ok else 1
    print("sequence-check --self-test: %d/%d PASS" % (len(cases) - fails, len(cases)))
    return 0 if fails == 0 else 1


def main():
    ap = argparse.ArgumentParser(description="THE SEQUENCE viewer (view-time compiled; a viewer, never a gate)")
    ap.add_argument("--flags", action="store_true")
    ap.add_argument("--project", action="append")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    path = os.path.join(ROOT, SEQ_REL)
    try:
        import yaml
        doc = yaml.safe_load(open(path, encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print("ERROR: %s unreadable (%s) -- nothing rendered" % (SEQ_REL, exc))
        return 1
    errs = validate(doc)
    if errs:
        print("ERROR: %s does not validate -- nothing rendered:" % SEQ_REL)
        for e in errs:
            print("  " + e)
        return 1
    enum_ok, enum_note = _gate_enum_matches()
    r = subprocess.run(["git", "log", "-1", "--format=%h %aI %an", "--", SEQ_REL], cwd=ROOT, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    reader = Reader(ROOT)
    rows = evaluate(doc, reader)
    cap = capacity(doc, reader, rows)
    res = resolve_codes(doc, a.project, _register_codes(ROOT)) if a.project else []
    if a.project:
        rows = [x for x in rows if x["project"] in set(a.project)]
    if a.json:
        print(json.dumps({"sequence": SEQ_REL, "file_last_commit": r.stdout.strip() or None, "capacity": cap,
                          "resolution": [{"project": c, "state": s, "detail": d} for c, s, d in res], "rows": rows}, indent=1))
    else:
        print("sequence-check | %s | file last commit: %s | enforcement: %s | projects: %d | stage enum: %s" % (
            SEQ_REL, r.stdout.strip() or "UNCOMMITTED", doc.get("enforcement"), len(rows),
            "OK" if enum_ok else "MISMATCH (" + enum_note + ")"))
        for c, s, d in res:
            print("PROJECT %s: %s -- %s" % (c, s, d))
        render(doc, rows, only_flags=a.flags)
        render_capacity(cap)
        counts = {}
        for x in rows:
            for f in x["flags"]:
                counts[f] = counts.get(f, 0) + 1
        print("\nFLAGS (denominator %d projects): %s" % (len(rows), ", ".join("%s=%d" % kv for kv in sorted(counts.items())) or "none"))
    if any(s == "UNKNOWN" for _, s, _ in res):
        return 3
    unreadable = any("UNREADABLE" in x["flags"] for x in rows) or not enum_ok or cap["live"] is None
    return 2 if unreadable else 0


if __name__ == "__main__":
    sys.exit(main())
