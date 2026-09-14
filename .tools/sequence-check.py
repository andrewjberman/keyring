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

A VIEWER, NOT A CHECKER: findings never change the exit code (the monitor moratorium; Andrew ~01:xxZ card 1 chose
TRACK). Exit 0 rendered; 1 nothing rendered (the sequence file unreadable); 2 rendered with >=1 UNREADABLE source.

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
TOP_KEYS = {"version", "owners", "enforcement", "stages", "projects", "parked", "pending_placement", "supersedes",
            "change_log"}
PROJECT_KEYS = {"fabric", "stage", "waits_on", "hold", "why", "notes"}
GATE_FORMS = ("prd_admitted", "dep_stage_at_least", "status", "manual")


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

    now = datetime.datetime(2026, 9, 20, tzinfo=datetime.timezone.utc)
    rows = {
        "A": {"dep_stage": "PRD", "status": "active", "fabric": "laptop", "_act": "abc 2026-09-19T00:00:00+00:00"},
        "B": {"dep_stage": "EXECUTING", "status": "active", "fabric": "laptop", "_act": "abc 2026-09-19T00:00:00+00:00"},
        "C": {"dep_stage": "REGISTERED", "status": "active", "fabric": "laptop", "_act": "abc 2026-09-01T00:00:00+00:00"},
        "D": {"dep_stage": "REGISTERED", "status": "active", "fabric": "site-z", "_act": "abc 2026-09-19T00:00:00+00:00"},
    }
    prd = {"A": True}
    doc = {"stages": [{"id": 1, "name": "s"}], "projects": {
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
    got = {r["project"]: set(r["flags"]) for r in evaluate(doc, Fake(rows, prd), now=now)}
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
    rows = evaluate(doc, Reader(ROOT))
    if a.project:
        rows = [x for x in rows if x["project"] in set(a.project)]
    if a.json:
        print(json.dumps({"sequence": SEQ_REL, "file_last_commit": r.stdout.strip() or None, "rows": rows}, indent=1))
    else:
        print("sequence-check | %s | file last commit: %s | enforcement: %s | projects: %d | stage enum: %s" % (
            SEQ_REL, r.stdout.strip() or "UNCOMMITTED", doc.get("enforcement"), len(rows),
            "OK" if enum_ok else "MISMATCH (" + enum_note + ")"))
        render(doc, rows, only_flags=a.flags)
        counts = {}
        for x in rows:
            for f in x["flags"]:
                counts[f] = counts.get(f, 0) + 1
        print("\nFLAGS (denominator %d projects): %s" % (len(rows), ", ".join("%s=%d" % kv for kv in sorted(counts.items())) or "none"))
    unreadable = any("UNREADABLE" in x["flags"] for x in rows) or not enum_ok
    return 2 if unreadable else 0


if __name__ == "__main__":
    sys.exit(main())
