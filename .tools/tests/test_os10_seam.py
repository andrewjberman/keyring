#!/usr/bin/env python3
"""NFRA_OUTSET.TO-OS-s-10 battery: THE CONSUMPTION SEAM -- one artifact per outset tool carrying
answer state, vintage and denominators, and a FAILED publish that reads FAILED, never absent.

Run at both required file grains:
  python .tools/tests/test_os10_seam.py
  python -m pytest -q .tools/tests/test_os10_seam.py

THE SEAM HAS TWO HALVES ON TWO HOSTS, AND THIS FILE IS THE CONTRACT BETWEEN THEM.
  producer  org/modules/heatmap/outset_seam.py      -- runs where the tools and their batteries run
  consumer  infra/aws/ec2/estate-report-runner/estate_report_runner.py
                                                    -- runs on a box that pulls ONE file and has no
                                                       estate workspace, so it cannot import the
                                                       producer half
Arm B is what keeps them agreeing: it asserts the producer's DECLARED_ANSWER_STATES and the
consumer's OUTSET_ANSWER_STATE_TO_STATUS cover each other EXACTLY, in both directions. A state added
on one side and forgotten on the other is a failing arm, not a silent default to OK.

NO AWS, NO NETWORK: every arm runs against a tempfile directory. The s3:// publish branch is
exercised with a STUB client (arm K) so the code path is proven without writing to a shared bucket.
"""
from __future__ import annotations

import datetime as _dt
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "org" / "modules" / "heatmap" / "outset_seam.py"
RUNNER = ROOT / "infra" / "aws" / "ec2" / "estate-report-runner" / "estate_report_runner.py"
TOOL = ROOT / ".tools" / "comp-heat"

# The runner reads six env vars AT IMPORT. Fake values: no arm makes an AWS call.
RUNNER_ENV = {
    "ESTATE_REPORT_BUCKET": "os10-battery-not-a-real-bucket",
    "ESTATE_GITHUB_SECRET_ID": "x", "ESTATE_KIMI_SECRET_ID": "x",
    "ESTATE_KIMI_URL": "http://127.0.0.1:1", "ESTATE_KIMI_MODEL": "x",
    "ESTATE_REPO_URL": "http://127.0.0.1:1/x.git",
}

# The mutation arm O10-AC1 names: a FAILED publish that reads ABSENT (a clean empty) instead of
# FAILED. The anchor is the consumer's ABSENT branch.
# RE-POINTED by NFRA_OUTSET OS-s-14, which added the `absent=True` FIELD to this very return
# so a caller choosing between seam sources can distinguish 'never published' from 'published
# and BROKEN' structurally instead of by grepping the error prose. The anchor's uniqueness
# assert refused the battery rather than mutating nothing -- the correct loud failure
# (NFRA_OUTSET-W2-S19, and W2-S17 for why a silently-no-op mutant is the thing to avoid).
# THE MUTANT'S INTENT IS UNCHANGED: an ABSENT artifact reads as a clean empty.
ABSENT_ANCHOR = (
    '    except FileNotFoundError:\n'
    '        return fail("artifact ABSENT at %s -- the publish FAILED or never ran. This is a FAILED "\n'
    '                    "stratum, never an omitted one." % source, absent=True)'
)
ABSENT_MUTANT = (
    '    except FileNotFoundError:\n'
    '        return {"status": "OK", "error": None, "rows": [], "vintage": "n/a",\n'
    '                "denominator": "n/a", "age_hours": None}  # RED MUTANT: absent reads as clean'
)

RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail) -> None:
    RESULTS.append((name, ok, str(detail).replace("\n", " ")[:300]))


def _load(path, name, env=None):
    keep = {}
    for k, v in (env or {}).items():
        keep[k] = os.environ.get(k)
        os.environ[k] = v
    try:
        spec = importlib.util.spec_from_file_location(name, str(path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def _artifact(seam, **over):
    a = seam.build_artifact("t", "q?", ["argv"], 0, None, answer_state="OK",
                            denominators={"scanned": 5, "total": 5, "claim": "measured"},
                            rows=[{"path": "p"}])
    a.update(over)
    return a


def _write(d: Path, name: str, doc) -> str:
    p = d / name
    p.write_text(json.dumps(doc) if not isinstance(doc, str) else doc, encoding="utf-8")
    return str(p)


def _run_battery() -> None:                                                # noqa: C901
    if RESULTS:
        return
    seam = _load(PRODUCER, "os10_producer_%s" % uuid.uuid4().hex)
    runner = _load(RUNNER, "os10_runner_%s" % uuid.uuid4().hex, RUNNER_ENV)
    now = _dt.datetime.now(_dt.timezone.utc)

    # ---- ARM A: ONE ARTIFACT PER OUTSET TOOL, each carrying the three required fields ----
    # REAL producers, really run, really published. Not fixtures.
    tmp_a = tempfile.mkdtemp(prefix="os10-pub-")
    try:
        rc_a = subprocess.run([sys.executable, str(PRODUCER), "--tool", str(TOOL),
                               "--out-dir", tmp_a], cwd=str(ROOT), text=True,
                              capture_output=True, timeout=110)
        missing, checked = [], []
        for key, tool, _q, _tail in seam.SEAM_PRODUCERS:
            f = Path(tmp_a) / (key + ".json")
            if not f.exists():
                missing.append(key)
                continue
            doc = json.loads(f.read_text(encoding="utf-8"))
            has = (isinstance(doc.get("answer_state"), str) and doc.get("answer_state_claim")
                   and (doc.get("vintage") or {}).get("answer_produced_utc")
                   and isinstance(doc.get("denominators"), dict)
                   and doc["denominators"].get("claim") in ("measured", "absent"))
            checked.append((key, tool, doc.get("answer_state"), bool(has)))
            if not has:
                missing.append(key + "(field)")
        _record("A-ONE-ARTIFACT-PER-OUTSET-TOOL-WITH-STATE-VINTAGE-DENOMINATORS",
                rc_a.returncode == 0 and not missing and len(checked) == len(seam.SEAM_PRODUCERS)
                and len(checked) >= 2,
                "published %d of %d declared producer(s), each carrying answer_state(+claim), "
                "vintage.answer_produced_utc and a denominators object with its own claim: %s"
                % (len(checked), len(seam.SEAM_PRODUCERS),
                   [(k, s) for k, _t, s, _o in checked]))
    finally:
        shutil.rmtree(tmp_a, ignore_errors=True)

    # ---- ARM B: THE CROSS-HALF CONTRACT -- both directions, no silent default ----
    prod_states = set(seam.DECLARED_ANSWER_STATES)
    cons_states = set(runner.OUTSET_ANSWER_STATE_TO_STATUS)
    statuses = set(runner.OUTSET_ANSWER_STATE_TO_STATUS.values())
    legal = {"OK", "INSTRUMENT_FAILED", "INSTRUMENT_UNAVAILABLE"}
    _record("B-PRODUCER-AND-CONSUMER-DECLARE-THE-SAME-DOMAIN",
            prod_states == cons_states and statuses <= legal and seam.SEAM_TAG == runner.SEAM_TAG,
            "producer-only=%s ; consumer-only=%s ; %d state(s) map into %d runner status(es) all "
            "within the runner's own vocabulary=%s ; seam tag agrees=%s"
            % (sorted(prod_states - cons_states), sorted(cons_states - prod_states),
               len(cons_states), len(statuses), statuses <= legal,
               seam.SEAM_TAG == runner.SEAM_TAG))

    # ---- ARM C: THE RUNNER READS A REAL PUBLISHED ARTIFACT ----
    tmp = Path(tempfile.mkdtemp(prefix="os10-read-"))
    try:
        art = seam.run_and_build("comp-heat drift", "what is written but not committed?",
                                 [sys.executable, str(TOOL), "drift", "--budget", "60", "--json"],
                                 cwd=str(ROOT), timeout_s=90)
        receipt = seam.publish_artifact(art, str(tmp / "comp_heat_drift.json"))
        st = runner._stratum_propagation("PIN", prefix=str(tmp), now=now)
        _record("C-RUNNER-READS-A-REAL-PUBLISHED-ARTIFACT",
                receipt["published"] and st["status"] == "OK"
                and "comp-heat drift" in st["vintage"] and st["denominator"].strip()
                and "NO DENOMINATOR" not in st["denominator"]
                and st["row_count"] is not None,
                "published %d B -> stratum status=%s row_count=%s | vintage=%s | denominator=%s"
                % (receipt["bytes"], st["status"], st["row_count"], st["vintage"][:90],
                   st["denominator"][:110]))

        # ---- ARM D: A FAILED PUBLISH READS **FAILED**, NEVER ABSENT ----
        st_absent = runner._stratum_propagation("PIN", prefix=str(tmp / "nowhere"), now=now)
        rendered = runner.render_stratum(st_absent)
        _record("D-FAILED-PUBLISH-READS-FAILED-NEVER-ABSENT",
                st_absent["status"] == "INSTRUMENT_FAILED"
                and "artifact ABSENT" in (st_absent["instrument_error"] or "")
                and st_absent["row_count"] is None
                and "THIS STRATUM PRODUCED NO DATA" in rendered
                and "zero rows" not in rendered,
                "status=%s row_count=%r ; rendered LOUDLY=%s ; not rendered as a clean zero=%s"
                % (st_absent["status"], st_absent["row_count"],
                   "THIS STRATUM PRODUCED NO DATA" in rendered, "zero rows" not in rendered))

        # ---- ARM E: NOT CONFIGURED is a THIRD fact, not a failure ----
        st_unconf = runner._stratum_propagation("PIN", prefix=None, now=now)
        _record("E-NOT-CONFIGURED-IS-NOT-THE-SAME-AS-FAILED",
                st_unconf["status"] == "INSTRUMENT_UNAVAILABLE"
                and st_unconf["status"] != st_absent["status"]
                and "ESTATE_OUTSET_SEAM_PREFIX unset" in (st_unconf["instrument_error"] or ""),
                "unconfigured=%s vs absent-publish=%s -- three facts, three renderings"
                % (st_unconf["status"], st_absent["status"]))

        # ---- ARM F: STALE READS FAILED, with its measured age ----
        old = dict(art)
        old["vintage"] = dict(art["vintage"],
                              answer_produced_utc=(now - _dt.timedelta(hours=51)).strftime(
                                  "%Y-%m-%dT%H:%M:%SZ"))
        _write(tmp, "comp_heat_drift.json", old)
        st_stale = runner._stratum_propagation("PIN", prefix=str(tmp), now=now)
        _record("F-STALE-ARTIFACT-READS-FAILED-NOT-TODAYS-ANSWER",
                st_stale["status"] == "INSTRUMENT_FAILED"
                and "STALE" in (st_stale["instrument_error"] or "")
                and "51.0 h" in (st_stale["instrument_error"] or ""),
                (st_stale["instrument_error"] or "")[:190])

        # ---- ARM F2: A FUTURE-DATED ARTIFACT IS REFUSED (staleness is a ONE-SIDED control) ----
        ahead = dict(art)
        ahead["vintage"] = dict(art["vintage"],
                                answer_produced_utc=(now + _dt.timedelta(hours=9)).strftime(
                                    "%Y-%m-%dT%H:%M:%SZ"))
        _write(tmp, "comp_heat_drift.json", ahead)
        st_future = runner._stratum_propagation("PIN", prefix=str(tmp), now=now)
        _record("F2-FUTURE-DATED-ARTIFACT-IS-REFUSED-NOT-TRUSTED",
                st_future["status"] == "INSTRUMENT_FAILED"
                and "DATED IN THE FUTURE" in (st_future["instrument_error"] or ""),
                "a 9 h-ahead artifact would NEVER trip the staleness ceiling, so it is refused: %s"
                % (st_future["instrument_error"] or "")[:150])

        # ---- ARM G: AN UNMAPPED STATE IS REFUSED, NEVER DEFAULTED TO OK ----
        weird = dict(art, answer_state="SOMETHING_THE_SEAM_NEVER_DECLARED")
        _write(tmp, "comp_heat_drift.json", weird)
        st_weird = runner._stratum_propagation("PIN", prefix=str(tmp), now=now)
        _record("G-UNMAPPED-ANSWER-STATE-IS-REFUSED",
                st_weird["status"] == "INSTRUMENT_FAILED"
                and "outside the seam's declared domain" in (st_weird["instrument_error"] or ""),
                (st_weird["instrument_error"] or "")[:190])

        # ---- ARM H: A FAILING PRODUCER YIELDS A FAILED ARTIFACT, NOT NOTHING ----
        bad = seam.run_and_build("a-tool-that-is-not-there", "q?",
                                 [sys.executable, str(ROOT / "no_such_tool_os10.py")],
                                 cwd=str(ROOT), timeout_s=30)
        _write(tmp, "comp_heat_drift.json", bad)
        st_bad = runner._stratum_propagation("PIN", prefix=str(tmp), now=now)
        _record("H-A-FAILING-PRODUCER-PUBLISHES-FAILED-NOT-SILENCE",
                bad["answer_state"] == "FAILED" and bad["error"]
                and bad["denominators"]["claim"] == "absent"
                and st_bad["status"] == "INSTRUMENT_FAILED",
                "producer answer_state=%s (error: %s) -> stratum %s"
                % (bad["answer_state"], (bad["error"] or "")[:90], st_bad["status"]))

        # ---- ARM I: THE RED MUTANT O10-AC1 NAMES ----
        src = RUNNER.read_text(encoding="utf-8")
        if src.count(ABSENT_ANCHOR) != 1:
            raise AssertionError("mutation anchor count != 1: %d" % src.count(ABSENT_ANCHOR))
        mdir = tempfile.mkdtemp(prefix="os10-mutant-")
        try:
            mp = Path(mdir) / "estate_report_runner.py"
            mp.write_text(src.replace(ABSENT_ANCHOR, ABSENT_MUTANT, 1), encoding="utf-8")
            mrun = _load(mp, "os10_runner_mutant_%s" % uuid.uuid4().hex, RUNNER_ENV)
            st_mut = mrun._stratum_propagation("PIN", prefix=str(tmp / "nowhere"), now=now)
            mrendered = mrun.render_stratum(st_mut)
            _record("I-RED-MUTANT-FAILED-PUBLISH-READS-ABSENT-AND-IS-CAUGHT",
                    st_mut["status"] == "OK" and st_mut["row_count"] == 0
                    and "zero rows" in mrendered
                    and st_absent["status"] == "INSTRUMENT_FAILED",
                    "mutant: a MISSING artifact renders status=%s row_count=%s and the report says "
                    "'zero rows -- this is a RESULT' ; production on the SAME missing artifact: %s "
                    "-- the mutant is the exact defect this cell exists to prevent"
                    % (st_mut["status"], st_mut["row_count"], st_absent["status"]))
        finally:
            shutil.rmtree(mdir, ignore_errors=True)

        _record("J-MUTATION-ANCHOR-UNIQUE",
                RUNNER.read_text(encoding="utf-8").count(ABSENT_ANCHOR) == 1,
                "exactly one ABSENT branch expected in the consumer half")

        # ---- ARM K: the s3:// publish branch, exercised with a STUB (no bucket is written) ----
        class _StubS3:
            def __init__(self):
                self.calls = []

            def put_object(self, **kw):
                self.calls.append(kw)
                return {}

        stub = _StubS3()
        r_s3 = seam.publish_artifact(art, "s3://not-a-real-bucket/outset/comp_heat_drift.json",
                                     s3_client=stub)
        r_bad = seam.publish_artifact(art, "s3://bucket-with-no-key", s3_client=stub)
        _record("K-S3-PUBLISH-PATH-EXERCISED-WITHOUT-WRITING-A-BUCKET",
                r_s3["published"] and len(stub.calls) == 1
                and stub.calls[0]["Bucket"] == "not-a-real-bucket"
                and stub.calls[0]["Key"] == "outset/comp_heat_drift.json"
                and not r_bad["published"] and "key" in (r_bad["error"] or ""),
                "stub received Bucket=%r Key=%r ; a keyless s3 URI is REFUSED: %s"
                % (stub.calls[0]["Bucket"], stub.calls[0]["Key"], (r_bad["error"] or "")[:80]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _report() -> int:
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    print("OS10-SEAM BATTERY: %d/%d PASS (denominator %d; 0 AWS calls, 0 network)"
          % (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    assert not failed, "comp-heat OS10 seam battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
