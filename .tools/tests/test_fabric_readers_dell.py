#!/usr/bin/env python
"""NFRA_CTLPLN.TO-CT-d-6 (AMENDMENT 1): the two fabric readers handle a Dell.

ID arm (9): the surprise-row gate's id-to-fabric derivation (`_fabric_of_id` / `_fabric_identity_violations` in
.tools/surprise-row-gate.py) run against a TEMPORARY COPY of the device register (OPAL_DEVICE_REGISTER), eight id cases
and one case with the register path pointing nowhere:
  bare -> laptop | Z- -> site-z | D1- -> dell1 | D2- -> dell2 | D1-W3-S2 -> dell1 | -D3- -> refused (unregistered
  coordinate) | a D1- id whose row says dell2 -> refused | a bare id whose row says dell1 -> refused | no register -> refused.
Row-schema arm (12): whole row objects through the gate's OWN schema limb (`_check_row`, which runs the Draft-07 validator and the
closed-enum walk) against the two row schemas in org/surprise_channel/schemas/: investigation D1/dell1, D2-W3/dell2, Z/site-z,
bare/laptop and W9/laptop admitted; fabric dell3 refused; a lower-case coordinate id refused; a remediation row with a D1- id
admitted; then the REFERENCE positions (AMENDMENT 3): an investigation row whose `adjudicates` names a D1- id admitted and a
lower-case one refused, a remediation row whose `disarms` names a D2-W3- id admitted and a malformed one refused. A verdict reads
only the complaints the schema limb raises (schema violation / ratified enum), because the gate's other
limbs (register agreement, owner, worker suffix) are graded by the id arm and by the gate's own --self-test.
Readers arm (9, AMENDMENTS 4-5): the three LAST id readers run through their OWN code -- `.tools/proof-of-spec-check.py` SURPRISE_ID_RE
(imported as compiled) and `org/surprise_channel/surprise-watch.sh` ID_RE (the line is read out of the script and run through
`grep -E`, the tool the script evaluates it with): X_PRJ-D1-S1, -D2-W3-S2, -Z-S4, -W9-S1 accepted by both; -d1-S1 and -W-S1 refused
by both. AMENDMENT 5 adds the third reader, IRPT_YCDGEN's `file_stop_row.py` ID_PATTERN (the compiled pattern imported from the file
by path), on three of the six ids (-D2-W3-S2, -Z-S4, -d1-S1): three more cases. A BRUTE-FORCE equivalence table (every id built from
two infix slots drawn from 20 tokens) compares the checker, the watcher, file_stop_row and the gate's ID_RE, and must agree on every id. Sweep (AMENDMENT 4): `ID-GRAMMAR-SWEEP` over every tracked file for the old
grammar's signature and for a hand-written row-id pattern; `old_grammar_left` is the count of live readers outside the grant.
Schema arm (5): one PRD header instance per fabric value validated against org/standards/PRD_HEADER.schema.json
(4 admitted) and one with dell3 (refused). Enum arm: the schema's fabric enum equals the gate's FABRIC_ENUM (register-derived
since NFRA_CTLPLN.TO-CT-ab-8; the gate source must still assign it, AST). Gate arm: `python .tools/surprise-row-gate.py --self-test` result line.

LAST line: FABRIC-READERS ids_ok=<a>/9 schema_ok=<b>/5 rowschema_ok=<c>/12 readers_ok=<r>/9 old_grammar_left=<d> enum_equal=<True|False>
           gate_selftest=<ok|fail> ok=<True|False>
"""
import ast
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE = os.path.join(ROOT, ".tools", "surprise-row-gate.py")
TOGATE = os.path.join(ROOT, ".tools", "to-pipeline-gate.py")
REGISTER = os.path.join(ROOT, "org", "devices", "DEVICES.json")
SCHEMA = os.path.join(ROOT, "org", "standards", "PRD_HEADER.schema.json")
ROW_SCHEMAS = os.path.join(ROOT, "org", "surprise_channel", "schemas")
CHECKER = os.path.join(ROOT, ".tools", "proof-of-spec-check.py")
WATCHER = os.path.join(ROOT, "org", "surprise_channel", "surprise-watch.sh")
STOPROW = os.path.join(ROOT, "infra", "aws", "lambda", "investor-reporting", "ycharts", "research", "file_stop_row.py")


def load_gate():
    spec = importlib.util.spec_from_file_location("surprise_row_gate_under_test", GATE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["surprise_row_gate_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


def enum_from_source():
    """The gate's FABRIC_ENUM (NFRA_CTLPLN.TO-CT-ab-8: register-derived, so no literal is parsed). The gate's source must
    still assign it at module level (AST, fail closed to None); the value is the gate's runtime FABRIC_ENUM."""
    with open(TOGATE, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    assigned = any(isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "FABRIC_ENUM" for t in n.targets)
                   for n in tree.body)
    if not assigned:
        return None
    spec = importlib.util.spec_from_file_location("to_pipeline_gate_enum_read", TOGATE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return list(mod.FABRIC_ENUM)


def id_cases(gate, enum, reg_copy, missing):
    """(label, ok, detail) per case; the register is the temporary copy unless the case says otherwise."""
    results = []
    os.environ["OPAL_DEVICE_REGISTER"] = reg_copy
    dev = gate._fabric_of_id("X_PRJ-S1")[1]
    to_box = {f: dev.resolve(f) for f in enum}
    box_of = {v: k for k, v in to_box.items()}   # box name -> fabric value, from the enum + the register

    def derives(rid, want):
        box, _d, _r, why = gate._fabric_of_id(rid)
        fab = box_of.get(box)
        ok = fab == want and gate._fabric_identity_violations(rid, want) == []
        results.append(("%s -> %s" % (rid, want), ok, "got %r %s" % (fab, why)))

    def refused(label, rid, fabric, needles):
        v = gate._fabric_identity_violations(rid, fabric)
        ok = bool(v) and all(n in v[0] for n in needles)
        results.append((label, ok, (v[0][:200] if v else "ADMITTED")))

    derives("X_PRJ-S1", "laptop")
    derives("X_PRJ-Z-S1", "site-z")
    derives("X_PRJ-D1-S1", "dell1")
    derives("X_PRJ-D2-S1", "dell2")
    derives("X_PRJ-D1-W3-S2", "dell1")
    refused("X_PRJ-D3-S1 (unregistered coordinate) refused", "X_PRJ-D3-S1", "dell1", ["'D3'", "'D1'", "'D2'", "'Z'"])
    refused("X_PRJ-D1-S1 with fabric dell2 refused", "X_PRJ-D1-S1", "dell2", ["dell1", "dell2"])
    refused("bare X_PRJ-S1 with fabric dell1 refused, names the id form", "X_PRJ-S1", "dell1",
            ["<CODE>-D1-S<n>", "laptop", "site-z", "dell1", "dell2"])
    os.environ["OPAL_DEVICE_REGISTER"] = missing
    refused("register path pointing nowhere refused loudly", "X_PRJ-S1", "laptop", ["REFUSED", "cannot be read"])
    return results


def schema_cases(enum):
    import jsonschema
    with open(SCHEMA, encoding="utf-8") as fh:
        schema = json.load(fh)
    base = {"project": "X_PRJ", "directive": "D0", "prd_version": "v0.1", "step": 4,
            "brief_ref": "docs/briefs/x.md@a77b65337e", "endpoint_outcomes": ["FWD-1"], "status": "DRAFT"}
    out = []
    for fab, expect in [(f, True) for f in enum] + [("dell3", False)]:
        errs = [e.message[:80] for e in jsonschema.Draft7Validator(schema).iter_errors(dict(base, fabric=fab))]
        good = (not errs) if expect else (len(errs) == 1 and "is not one of" in errs[0])   # a refusal must be the fabric alone
        out.append(("PRD header fabric=%s" % fab, good, "ADMITTED" if not errs else "REFUSED " + errs[0]))
    return out, schema["properties"]["fabric"]["enum"]


def rowschema_cases(gate):
    """Twelve whole-row cases through gate._check_row; only the schema limb's complaints decide each verdict."""
    def load(name):
        with open(os.path.join(ROW_SCHEMAS, name), encoding="utf-8") as fh:
            return json.load(fh)
    inv, rem = load("investigation_item.schema.json"), load("remediation_row.schema.json")

    def inv_row(rid, fabric):
        return {"id": rid, "project": "X_PRJ", "fabric": fabric, "surfaced_by": "0.9.0_WK_X_PRJ~3",
                "surfaced_at": "2026-10-07T09:30:00Z", "one_line": "a well-formed test row for the schema arm",
                "class": "OBSERVATION", "hazard_standing": "INERT", "grounding": {"status": "INFERRED", "evidence": ["test evidence line"]},
                "disposition": "UNDER_INVESTIGATION", "spec_asserts": "the spec asserts a thing", "world_is": "the world is another thing"}

    def rem_row(rid, fabric):
        return {"id": rid, "project": "X_PRJ", "fabric": fabric, "class": "OBSERVATION", "hazard_standing": "INERT",
                "mechanism": "a well-formed test mechanism", "evidence": ["test evidence line"], "remedy": "a test remedy",
                "owner": "1.0.0_SA_CTO", "round": "v1", "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"}}

    def with_key(row, key, value):
        return dict(row, **{key: value})

    def disarming(refs):   # a row carrying `disarms` must carry the `disarm` block (the schema's allOf)
        return dict(rem_row("X_PRJ-S6", "laptop"), disarms=refs,
                    disarm={"state": "DISARMED", "owner": "1.0.0_SA_CTO", "at": "2026-10-07T09:30:00Z"})

    def schema_complaints(row, kind, schema):
        out = gate._check_row(row, kind, schema)
        return [c for c in out if "schema violation" in c or "ratified enum" in c]

    out = []
    for label, row, kind, schema, admit, where in [
        ("investigation X_PRJ-D1-S1 / dell1", inv_row("X_PRJ-D1-S1", "dell1"), "INVESTIGATION", inv, True, None),
        ("investigation X_PRJ-D2-W3-S2 / dell2", inv_row("X_PRJ-D2-W3-S2", "dell2"), "INVESTIGATION", inv, True, None),
        ("investigation X_PRJ-Z-S4 / site-z", inv_row("X_PRJ-Z-S4", "site-z"), "INVESTIGATION", inv, True, None),
        ("investigation X_PRJ-S5 / laptop", inv_row("X_PRJ-S5", "laptop"), "INVESTIGATION", inv, True, None),
        ("investigation X_PRJ-W9-S1 / laptop (worker form)", inv_row("X_PRJ-W9-S1", "laptop"), "INVESTIGATION", inv, True, None),
        ("investigation fabric dell3 refused", inv_row("X_PRJ-D1-S1", "dell3"), "INVESTIGATION", inv, False, "fabric"),
        ("investigation X_PRJ-d1-S1 (lower case) refused", inv_row("X_PRJ-d1-S1", "dell1"), "INVESTIGATION", inv, False, "id"),
        ("remediation X_PRJ-D1-S1 / dell1", rem_row("X_PRJ-D1-S1", "dell1"), "REMEDIATION", rem, True, None),
        ("investigation adjudicates X_PRJ-D1-S1", with_key(inv_row("X_PRJ-C-S1", "laptop"), "adjudicates", ["X_PRJ-D1-S1"]),
         "INVESTIGATION", inv, True, None),
        ("investigation adjudicates X_PRJ-d1-S1 (lower case) refused",
         with_key(inv_row("X_PRJ-C-S1", "laptop"), "adjudicates", ["X_PRJ-d1-S1"]), "INVESTIGATION", inv, False, "adjudicates"),
        ("remediation disarms X_PRJ-D2-W3-S2", disarming(["X_PRJ-D2-W3-S2"]),
         "REMEDIATION", rem, True, None),
        ("remediation disarms a malformed id refused", disarming(["X_PRJ-D1-S"]),
         "REMEDIATION", rem, False, "disarms"),
    ]:
        got = schema_complaints(row, kind, schema)
        if admit:
            good = not got
        else:   # a refusal must be the named field alone: a refusal for some other reason proves nothing
            good = bool(got) and all(("/" + where) in c or ("%s=" % where) in c for c in got)
        out.append((label, good, "ADMITTED" if not got else "REFUSED " + got[0][:150]))
    return out


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def watcher_regex():
    """The watcher's ID_RE exactly as the script assigns it (the single-quoted value), read out of the script."""
    with open(WATCHER, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("ID_RE='") and line.rstrip().endswith("'"):
                return line.rstrip()[len("ID_RE='"):-1]
    return None


def watcher_accepts(ids):
    """The set of ids the watcher's ID_RE counts, run through `grep -E` (the script's own evaluator), one row line per id."""
    grep = shutil.which("grep")
    rx = watcher_regex()
    if grep is None or rx is None:
        return None
    lines = "".join('  "id": "%s",\n' % i for i in ids)
    with tempfile.TemporaryDirectory() as tmp:   # the pattern travels in a file: a native-Windows argv mangles its double quotes
        pf = os.path.join(tmp, "id_re.txt")
        with open(pf, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(rx + "\n")
        cp = subprocess.run([grep, "-E", "-f", pf], input=lines, capture_output=True, text=True, timeout=60, encoding="utf-8")
    return {ln.split('"')[3] for ln in cp.stdout.splitlines() if ln.count('"') >= 4}


def readers_cases(gate):
    """Six named cases through the two readers' own code, three through file_stop_row's, then a brute-force equivalence of the
    three readers and the gate's ID_RE."""
    checker = load_module("proof_of_spec_check_under_test", CHECKER)
    stoprow = load_module("file_stop_row_under_test", STOPROW)

    def stoprow_accepts(rid):
        return bool(stoprow.ID_PATTERN.match(rid))

    def checker_accepts(rid):
        m = checker.SURPRISE_ID_RE.match(rid + ": a surprise entry")
        return bool(m) and m.group(1) == rid

    named = [("X_PRJ-D1-S1", True), ("X_PRJ-D2-W3-S2", True), ("X_PRJ-Z-S4", True), ("X_PRJ-W9-S1", True),
             ("X_PRJ-d1-S1", False), ("X_PRJ-W-S1", False)]
    got_w = watcher_accepts([i for i, _w in named])
    out = []
    for rid, want in named:
        c, w = checker_accepts(rid), (None if got_w is None else rid in got_w)
        out.append(("%s checker=%s watcher=%s (want %s)" % (rid, c, w, want), c == want and w == want, ""))
    for rid, want in [("X_PRJ-D2-W3-S2", True), ("X_PRJ-Z-S4", True), ("X_PRJ-d1-S1", False)]:
        got = stoprow_accepts(rid)
        out.append(("%s file_stop_row=%s (want %s)" % (rid, got, want), got == want, ""))
    # brute force: two infix slots over 20 tokens; the gate's ID_RE is the reference language
    toks = ["", "W-", "W1-", "W12-", "C-", "C1-", "D1-", "D2-", "D-", "D12-", "Z-", "Z9-", "X-", "d1-", "WW-", "1-", "W0-", "C0-",
            "B7-", "V-"]
    ids = sorted({"X_PRJ-%s%sS%s" % (a, b, k) for a in toks for b in toks for k in ("1", "12", "")}
                 | {"X_PRJ-W2S1", "X_PRJ-S1x", "X_PRJ-S5"})
    ref = {i for i in ids if gate.ID_RE.match(i)}
    chk = {i for i in ids if checker_accepts(i)}
    wat = watcher_accepts(ids)
    stp = {i for i in ids if stoprow_accepts(i)}
    agree = wat is not None and ref == chk == wat == stp
    print("equivalence: %d ids, gate ID_RE accepts %d, checker accepts %d, file_stop_row accepts %d, watcher (grep -E) accepts %s -> %s"
          % (len(ids), len(ref), len(chk), len(stp), "UNREADABLE" if wat is None else len(wat), "AGREE" if agree else "DISAGREE"))
    if not agree and wat is not None:
        print("  checker differs:", sorted(ref ^ chk)[:6], "watcher differs:", sorted(ref ^ wat)[:6],
              "file_stop_row differs:", sorted(ref ^ stp)[:6])
    return out, agree


RECORD_PREFIXES = ("org/missions/", "org/tier1_exec/", "org/tier2_senior/", "org/audit/", "daily_reports/", "docs/", "org/ref/",
                   "org/surprise_channel/ETFS_INGEST/")
RECORD_EXT = (".md", ".html", ".log", ".txt")
FIXED_HERE = {
    ".tools/proof-of-spec-check.py": "SURPRISE_ID_RE now the gate's grammar (this amendment)",
    "org/surprise_channel/surprise-watch.sh": "ID_RE now the gate's grammar by alternation, and the comment above it (this amendment)",
    "org/surprise_channel/schemas/investigation_item.schema.json": "id and adjudicates patterns at the gate's grammar (amendments 2-3)",
    "org/surprise_channel/schemas/remediation_row.schema.json": "id and disarms patterns at the gate's grammar (amendments 2-3)",
    "infra/aws/lambda/investor-reporting/ycharts/research/file_stop_row.py": "ID_PATTERN now the gate's grammar (amendment 5)",
    ".tools/tests/test_fabric_readers_dell.py": "this test: its signatures are composed, so only data in it can hit",
}
GATE_DERIVED = {".tools/surprise-row-gate.py": "the reference grammar's own file: decides by ID_RE (line 108); a hit is prose in a "
                                               "docstring or a refusal message"}


def sweep():
    """Every tracked text file (<= 2 MB) for the OLD grammar's literal signature and for a hand-written row-id regex holding the
    seat-number pattern beside the worker-number pattern. Prints each hit with its class; returns (last line, live count)."""
    sig_text = "(Z" + "-)" + "?"   # composed, so this file does not carry the signature on one line
    sig_old = re.compile(re.escape(sig_text))
    seat = re.compile(r"S(?:\[0-9\]|\\d)\+")
    worker = re.compile(r"W(?:\[0-9\]|\\d)\+")
    names = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, timeout=110).stdout.split(b"\0")
    scanned, hits = 0, []
    for raw in names:
        if not raw:
            continue
        rel = raw.decode("utf-8", "replace")
        try:
            if os.path.getsize(os.path.join(ROOT, rel)) > 2 * 1024 * 1024:
                continue
            with open(os.path.join(ROOT, rel), "rb") as fh:
                data = fh.read()
        except OSError:
            continue
        if b"\0" in data[:8192]:
            continue
        scanned += 1
        if sig_text.encode() not in data and b"[0-9]+" not in data and b"\\d+" not in data:
            continue   # cheap byte prefilter: no signature fragment anywhere in the file
        for n, ln in enumerate(data.decode("utf-8", "replace").splitlines(), 1):
            if sig_old.search(ln) or (seat.search(ln) and worker.search(ln)):
                hits.append((rel, n))
    cls = {"FIXED-HERE": 0, "GATE-DERIVED": 0, "RECORD": 0, "LIVE-READER-OUTSIDE-GRANT": 0}
    for rel, n in hits:
        if rel in FIXED_HERE:
            c, why = "FIXED-HERE", FIXED_HERE[rel]
        elif rel in GATE_DERIVED:
            c, why = "GATE-DERIVED", GATE_DERIVED[rel]
        elif rel.startswith(RECORD_PREFIXES) or rel.endswith(RECORD_EXT):
            c, why = "RECORD", "a document, log, deliverable, task order or archived channel file quoting the pattern as history"
        else:
            c, why = "LIVE-READER-OUTSIDE-GRANT", "code outside the grant still deciding on the old grammar"
        cls[c] += 1
        print("  hit %s:%d  %s  %s" % (rel, n, c, why))
    d = cls["LIVE-READER-OUTSIDE-GRANT"]
    last = ("ID-GRAMMAR-SWEEP files_scanned=%d hits=%d fixed_here=%d gate_derived=%d record=%d live_outside_grant=%d ok=%s"
            % (scanned, len(hits), cls["FIXED-HERE"], cls["GATE-DERIVED"], cls["RECORD"], d, d == 0))
    return last, d


def main():
    gate = load_gate()
    enum = enum_from_source()
    print("to-pipeline-gate FABRIC_ENUM (from source) = %r" % (enum,))
    with open(REGISTER, encoding="utf-8") as fh:
        reg = json.load(fh)
    with tempfile.TemporaryDirectory() as tmp:
        copy = os.path.join(tmp, "DEVICES.json")
        with open(copy, "w", encoding="utf-8") as fh:
            json.dump(reg, fh)
        ids = id_cases(gate, enum, copy, os.path.join(tmp, "no-such-register.json"))
    os.environ.pop("OPAL_DEVICE_REGISTER", None)
    for label, ok, detail in ids:
        print("%s  id: %s | %s" % ("PASS" if ok else "FAIL", label, detail))
    sch, sch_enum = schema_cases(enum)
    for label, ok, detail in sch:
        print("%s  schema: %s | %s" % ("PASS" if ok else "FAIL", label, detail))
    rows = rowschema_cases(gate)
    for label, ok, detail in rows:
        print("%s  rowschema: %s | %s" % ("PASS" if ok else "FAIL", label, detail))
    rd, rd_agree = readers_cases(gate)
    for label, ok, _detail in rd:
        print("%s  readers: %s" % ("PASS" if ok else "FAIL", label))
    sweep_last, left = sweep()
    print(sweep_last)
    enum_equal = enum is not None and sch_enum == enum
    print("schema enum %r == FABRIC_ENUM %r -> %s" % (sch_enum, enum, enum_equal))
    cp = subprocess.run([sys.executable, GATE, "--self-test"], cwd=ROOT, capture_output=True, text=True, timeout=110,
                        encoding="utf-8", errors="replace")
    line = [ln for ln in (cp.stdout + cp.stderr).splitlines() if ln.startswith("RESULT:")]
    selftest = "ok" if cp.returncode == 0 and line else "fail"
    print("surprise-row-gate --self-test -> %s | rc=%d %s" % (selftest, cp.returncode, line[-1] if line else "(no result line)"))
    a = sum(1 for _l, ok, _d in ids if ok)
    b = sum(1 for _l, ok, _d in sch if ok)
    c = sum(1 for _l, ok, _d in rows if ok)
    r = sum(1 for _l, ok, _d in rd if ok)
    ok = a == 9 and b == 5 and c == 12 and r == 9 and rd_agree and left == 0 and enum_equal and selftest == "ok"
    print("FABRIC-READERS ids_ok=%d/9 schema_ok=%d/5 rowschema_ok=%d/12 readers_ok=%d/9 old_grammar_left=%d enum_equal=%s "
          "gate_selftest=%s ok=%s" % (a, b, c, r, left, enum_equal, selftest, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
