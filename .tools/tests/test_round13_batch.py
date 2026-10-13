#!/usr/bin/env python3
"""Round-13 batch repair (NFRA_CTLPLN TO-CT-ac-1, cell CT-ac-1): arms for the seven round-12 defects.

Arms: (1) crossbox-call.py merge carries a null bus_message_id, and a merge the validator refuses writes nothing;
(2) spawn-agent.ps1's serial pattern accepts an underscore project segment; (3) the three schemas' box lists equal
lib/devices.py placement_values() (a GUARD: a list that drifts fails here, it is never hand-edited), and the HELD entry
for to-pipeline-gate.py is gone; (4) crossbox-deploy-check.py's OPEN-CALL arm matches a structured project field and a
root by path or its roots field, never a bare token in free text; (6) derive_protected_functions.py with no source flag
reads the saved file and makes no AWS call; (7) no check in the three files gates on simulate_policy.
Item 5 (the origin dependency of test_crossbox_call.py) is covered by that suite itself.

Standard library and temporary directories only. No AWS call (a stub aws on PATH records any call and the arm fails on it),
no network, nothing pushed. Run: python .tools/tests/test_round13_batch.py
LAST line: ROUND13-BATCH arms=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import contextlib
import datetime as dt
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
REPO = TOOLS.parent
INFRA_TESTS = REPO / "infra" / "aws" / "terraform" / "nfra-ctlpln-identity" / "tests"
SCHEMAS = ["org/surprise_channel/schemas/investigation_item.schema.json",
           "org/surprise_channel/schemas/remediation_row.schema.json",
           "org/standards/PRD_HEADER.schema.json"]
RESULTS = []


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rm(path) -> None:
    """Remove a temporary tree; git object files are read-only on Windows, so the handler makes each one writable first."""
    shutil.rmtree(path, onerror=lambda f, p, _e: (os.chmod(p, 0o700), f(p)))


def arm(name, fn) -> None:
    try:
        ok, detail = fn()
    except Exception as exc:  # an arm that cannot run is a failed arm, never a skipped one
        ok, detail = False, "%s: %s" % (type(exc).__name__, exc)
    RESULTS.append((name, bool(ok), str(detail)[:200]))


# ---------------------------------------------------------------- item 1: crossbox-call.py merge

def merge_setup(tmp):
    cb = load("crossbox_call_r13", TOOLS / "crossbox-call.py")
    h = cb.Harness(tmp)
    lines = h.a.open("ORDER", h.b.device, cb.SEAT + cb.SEAT_LANE, "1.0.0_SA_CTO", "Round 13 merge arm", cb.BODY)
    cid = lines[0].split()[1]
    h.commit(h.a, h.a.rel(cid))
    h.push(h.a.root)                       # the fixture's own local origin: line() requires the commit on origin
    line = h.a.line(cid)[0]
    h.pull(h.b, h.a, ff=True)
    h.b.receive(line)
    return cb, h, cid


def arm_merge_null_bus_id():
    tmp = tempfile.mkdtemp(prefix="r13-merge-null-")
    try:
        cb, h, cid = merge_setup(tmp)
        h.b.ack(cid, cb.SEAT + cb.SEAT_LANE, at="2026-10-13T10:00:00Z")
        h.commit(h.b, h.b.rel(cid))
        h.pull(h.a, h.b, ff=False)
        out = h.a.merge(cid, "FETCH_HEAD")
        got = h.a.read(cid)
        want_ack = {"at": "2026-10-13T10:00:00Z", "by": cb.SEAT + cb.SEAT_LANE, "bus_message_id": None}
        ok = got["ack"] == want_ack and got["state"] == "ACKED"
        return ok, "ack=%s state=%s line=%s" % (got["ack"], got["state"], out[0][:60])
    finally:
        rm(tmp)


def arm_merge_refused_writes_nothing():
    tmp = tempfile.mkdtemp(prefix="r13-merge-refuse-")
    try:
        cb, h, cid = merge_setup(tmp)
        h.b.ack(cid, cb.SEAT + cb.SEAT_LANE, at="2026-10-13T10:00:00Z")
        h.commit(h.b, h.b.rel(cid))
        h.pull(h.a, h.b, ff=False)
        before = h.a.path(cid).read_bytes()
        real = cb.check_call

        def refusing(doc, where):
            # a validator that refuses the MERGED value (the merge's own validation step is the only one labelled "(merged from")
            if "(merged from" in where:
                raise cb.Refused("validator refuses the merged value (test arm)")
            return real(doc, where)

        cb.check_call = refusing
        try:
            refused = False
            try:
                h.a.merge(cid, "FETCH_HEAD")
            except cb.Refused as exc:
                refused = "test arm" in str(exc)
        finally:
            cb.check_call = real
        after = h.a.path(cid).read_bytes()
        return refused and before == after, "refused=%s byte-identical=%s" % (refused, before == after)
    finally:
        rm(tmp)


def arm_merge_conflict_writes_nothing():
    tmp = tempfile.mkdtemp(prefix="r13-merge-conflict-")
    try:
        cb, h, cid = merge_setup(tmp)
        h.b.ack(cid, cb.SEAT + cb.SEAT_LANE, at="2026-10-13T10:00:00Z")
        h.commit(h.b, h.b.rel(cid))
        mine = h.a.read(cid)
        mine["ack"] = {"at": "2026-10-13T11:00:00Z", "by": cb.SEAT + cb.SEAT_LANE, "bus_message_id": None}
        h.a.save(mine)                     # the sending box holds a different ack.at for the same call
        before = h.a.path(cid).read_bytes()
        h.pull(h.a, h.b, ff=False)
        refused = False
        try:
            h.a.merge(cid, "FETCH_HEAD")
        except cb.Refused as exc:
            refused = "different ack.at" in str(exc)
        after = h.a.path(cid).read_bytes()
        return refused and before == after, "refused=%s byte-identical=%s" % (refused, before == after)
    finally:
        rm(tmp)


# ---------------------------------------------------------------- item 2: spawn-agent.ps1 serial pattern

def arm_spawn_serial_pattern():
    text = (TOOLS / "spawn-agent.ps1").read_text(encoding="utf-8")
    m = re.search(r"if \(\$Serial -notmatch '([^']+)'\)", text)
    if not m:
        return False, "no serial -notmatch pattern found in spawn-agent.ps1"
    pat = m.group(1)
    accepts = re.search(pat, "0.9.0_WK_NFRA_CTLPLN~78") is not None
    keeps_old = re.search(pat, "0.4.0_DS_ClientPlatform") is not None
    refuses = re.search(pat, "0.9.0_WK_bad name") is None
    return accepts and keeps_old and refuses, "pattern=%s accepts_underscore=%s keeps_old=%s refuses_space=%s" % (
        pat, accepts, keeps_old, refuses)


# ---------------------------------------------------------------- item 3: box lists guard and HELD entry

def fabric_enums(node):
    if isinstance(node, dict):
        for key, val in node.items():
            if key == "fabric" and isinstance(val, dict) and isinstance(val.get("enum"), list):
                yield val["enum"]
            yield from fabric_enums(val)
    elif isinstance(node, list):
        for val in node:
            yield from fabric_enums(val)


def arm_schema_box_lists_equal_register():
    devices = load("lib_devices_r13", REPO / "lib" / "devices.py")
    want = sorted(devices.placement_values())
    report, bad = [], []
    for rel in SCHEMAS:
        enums = list(fabric_enums(json.loads((REPO / rel).read_text(encoding="utf-8"))))
        same = bool(enums) and all(sorted(e) == want for e in enums)
        report.append("%s enums=%d same=%s" % (Path(rel).name, len(enums), same))
        if not same:
            bad.append(rel)
    return not bad, "register=%s; %s" % (want, "; ".join(report))


def arm_held_entry_gone():
    mod = load("no_hand_listed_boxes_r13", TOOLS / "tests" / "test_no_hand_listed_boxes.py")
    return ".tools/to-pipeline-gate.py" not in mod.HELD, "HELD keys=%s" % sorted(mod.HELD)


# ---------------------------------------------------------------- item 4: OPEN-CALL matching in crossbox-deploy-check.py

def open_call_hits(doc, root_rel):
    dc = load("crossbox_deploy_check_r13", TOOLS / "crossbox-deploy-check.py")
    tmp = tempfile.mkdtemp(prefix="r13-open-call-")
    try:
        crossbox = Path(tmp) / "org" / "devices" / "crossbox"
        crossbox.mkdir(parents=True)
        base = {"id": "c1", "kind": "CALL", "from_device": "dell1", "to_device": "laptop", "from_serial": "a",
                "to_serial": "b", "body_path": "org/devices/crossbox/c1.body.md", "state": "OPEN"}
        base.update(doc)
        (crossbox / "c1.json").write_text(json.dumps(base), encoding="utf-8")
        (crossbox / "c1.body.md").write_text("nothing about paths\n", encoding="utf-8")
        hits, _ = dc.measure_open_call(tmp, root_rel, [("PA", "placed on laptop")], dt.datetime(2026, 10, 13, 12, 0, 0))
        return hits
    finally:
        rm(tmp)


def arm_project_field_not_subject():
    root = "infra/aws/terraform/rootx"
    hits = open_call_hits({"subject": "the PA project needs a word", "project": "PB"}, root)
    return not hits, "hits=%s" % hits


def arm_project_field_matches():
    root = "infra/aws/terraform/rootx"
    hits = open_call_hits({"subject": "a word for the project", "project": "PA"}, root)
    return bool(hits), "hits=%s" % hits


def arm_root_by_path_in_subject():
    root = "infra/aws/terraform/rootx"
    hits = open_call_hits({"subject": "hold " + root}, root)
    return bool(hits), "hits=%s" % hits


def arm_root_by_roots_field():
    root = "infra/aws/terraform/rootx"
    hits = open_call_hits({"subject": "a word", "roots": [root]}, root)
    return bool(hits), "hits=%s" % hits


def arm_bare_root_name_no_hit():
    root = "infra/aws/terraform/rootx"
    hits = open_call_hits({"subject": "the rootx needs a word"}, root)
    return not hits, "hits=%s" % hits


# ---------------------------------------------------------------- item 6: derive_protected_functions.py default source

def protected_module():
    return load("derive_protected_functions_r13", INFRA_TESTS / "derive_protected_functions.py")


def arm_protected_check_default_reads_file_no_aws():
    mod = protected_module()
    calls = []

    def live(*_a, **_k):
        calls.append("live_listing")
        raise RuntimeError("live census would call AWS")

    def aws(*_a, **_k):
        calls.append("aws")
        raise RuntimeError("aws would be called")

    real_live, real_aws = mod.live_listing, mod.aws
    mod.live_listing, mod.aws = live, aws
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            mod.main(["--check"])
            mod.main([])
    finally:
        mod.live_listing, mod.aws = real_live, real_aws
    first = out.getvalue().splitlines()[0] if out.getvalue() else ""
    return calls == [] and first.startswith("SOURCE file:"), "calls=%s first=%s" % (calls, first[:70])


def arm_protected_live_only_when_explicit():
    mod = protected_module()
    calls = []

    def live(*_a, **_k):
        calls.append("live_listing")
        raise RuntimeError("stop after the recorded call")

    real_live = mod.live_listing
    mod.live_listing = live
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            try:
                mod.main(["--live"])
            except RuntimeError:
                pass
    finally:
        mod.live_listing = real_live
    first = out.getvalue().splitlines()[0] if out.getvalue() else ""
    return calls == ["live_listing"] and first.startswith("SOURCE live:"), "calls=%s first=%s" % (calls, first[:70])


def arm_protected_subprocess_stub_on_path():
    tmp = tempfile.mkdtemp(prefix="r13-stub-aws-")
    try:
        log = Path(tmp) / "aws-calls.log"
        (Path(tmp) / "aws").write_text('#!/bin/sh\necho "$@" >> "%s"\nexit 99\n' % log.as_posix(), encoding="utf-8")
        (Path(tmp) / "aws.cmd").write_text('@echo %%* >> "%s"\r\n@exit /b 99\r\n' % str(log), encoding="utf-8")
        env = dict(os.environ)
        env["PATH"] = tmp + os.pathsep + env.get("PATH", "")
        script = INFRA_TESTS / "derive_protected_functions.py"
        proc = subprocess.run([sys.executable, str(script), "--check"], env=env, capture_output=True, text=True, timeout=120)
        first = proc.stdout.splitlines()[0] if proc.stdout.strip() else ""
        calls = log.read_text(encoding="utf-8") if log.exists() else ""
        return first.startswith("SOURCE file:") and calls == "", "rc=%s first=%s stub_calls=%r" % (proc.returncode, first[:60], calls)
    finally:
        rm(tmp)


# ---------------------------------------------------------------- item 7: no gate on simulate_policy

def arm_no_simulate_policy_gate():
    gated = []
    for name in ("render_routes_policy.py", "derive_plan_reads.py", "derive_protected_functions.py"):
        if "simulate_policy" in (INFRA_TESTS / name).read_text(encoding="utf-8"):
            gated.append(name)
    retired = not (INFRA_TESTS / "simulate_policy.py").exists()
    return not gated and retired, "files naming simulate_policy=%s simulator removed=%s" % (gated or "none", retired)


def main() -> int:
    arm("1a merge carries a null bus_message_id and folds the receiving ack", arm_merge_null_bus_id)
    arm("1b a merge the validator refuses writes nothing (byte-identical)", arm_merge_refused_writes_nothing)
    arm("1c a merge with conflicting values writes nothing (byte-identical)", arm_merge_conflict_writes_nothing)
    arm("2 spawn-agent.ps1 serial pattern accepts 0.9.0_WK_NFRA_CTLPLN~78", arm_spawn_serial_pattern)
    arm("3a the three schemas' box lists equal lib/devices.py placement_values()", arm_schema_box_lists_equal_register)
    arm("3b the HELD entry for to-pipeline-gate.py is gone", arm_held_entry_gone)
    arm("4a a subject naming a project with another project field does not hit", arm_project_field_not_subject)
    arm("4b a matching project field hits", arm_project_field_matches)
    arm("4c a root named by path in the subject hits", arm_root_by_path_in_subject)
    arm("4d a root named in the roots field hits", arm_root_by_roots_field)
    arm("4e a bare root name in free text does not hit", arm_bare_root_name_no_hit)
    arm("6a derive_protected_functions --check with no flag reads the file and makes no AWS call", arm_protected_check_default_reads_file_no_aws)
    arm("6b --live is the only path that reaches the live census", arm_protected_live_only_when_explicit)
    arm("6c subprocess --check with a stub aws on PATH: source file, no stub call", arm_protected_subprocess_stub_on_path)
    arm("7 none of the three files gates on simulate_policy", arm_no_simulate_policy_gate)
    for name, ok, detail in RESULTS:
        print("%s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok else "  -- " + detail))
    good = sum(1 for _, ok, _ in RESULTS if ok)
    print("ROUND13-BATCH arms=%d/%d ok=%s" % (good, len(RESULTS), bool(RESULTS) and good == len(RESULTS)))
    return 0 if RESULTS and good == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
