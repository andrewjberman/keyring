"""Tests for .tools/remote-job.py -- the device side of remote jobs
(org/tier1_exec/4.0.0_SA_CRO/deliverables/REMOTE_JOBS_PROTOCOL_20261002.md). No AWS, no psutil reads, no bash."""
import importlib.util
import json
import os
import time

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("remote_job", os.path.join(HERE, "..", "remote-job.py"))
rj = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rj)


class FakeRuntime:
    def __init__(self):
        self.sent = []

    def send(self, object_id, kind, payload=None, event_id=None):
        self.sent.append({"object_id": object_id, "kind": kind, "payload": payload, "event_id": event_id})
        return event_id


@pytest.fixture
def env(monkeypatch, tmp_path):
    rt = FakeRuntime()
    monkeypatch.setattr(rj, "LOCK", str(tmp_path / ".remote-job.json"))
    monkeypatch.setattr(rj, "device_name", lambda: "laptop")
    monkeypatch.setattr(rj, "measure", lambda: (12.5, 40.0))
    monkeypatch.setattr(rj, "make_runtime", lambda: rt)
    monkeypatch.delenv("OPAL_AGENT_SERIAL", raising=False)
    live = tmp_path / "liveness.json"                # a reviewer seat seen just now, so a bid can be available
    live.write_text(json.dumps({REVIEWER: {"last_seen_epoch": time.time()}}), encoding="utf-8")
    monkeypatch.setenv("OPAL_LIVENESS_FILE", str(live))
    return rt


REVIEWER = "3.0.0_SA_CVO"


def brief_file(tmp_path):
    path = tmp_path / "brief.md"
    path.write_text("Fix the CSV export on the Holdings page.\n", encoding="utf-8")
    return str(path)


def grade_pass(tmp_path, job="J042"):
    record = tmp_path / "grade.md"
    record.write_text("PASS: read the real artifact\n", encoding="utf-8")
    return rj.main(["grade", job, "--as", REVIEWER, "--verdict", "PASS", "--record", str(record)])


def test_bid_available_with_the_contract_payload(env):
    assert rj.main(["bid", "J042"]) == 0
    (ev,) = env.sent
    assert ev["object_id"] == "job:J042" and ev["kind"] == "job.bid" and ev["event_id"] == "bid-J042-laptop"
    p = ev["payload"]
    assert set(p) == {"device", "serial", "available", "reviewer", "cpu_pct", "mem_pct", "at"}
    assert p["device"] == "laptop" and p["serial"] == "0.0.0_AB_MSTR" and p["available"] is True
    assert (p["cpu_pct"], p["mem_pct"]) == (12.5, 40.0)
    assert p["reviewer"] == REVIEWER and "unavailable_reason" not in p


def test_bid_unavailable_while_another_job_is_open(env):
    rj.write_lock({"job": "J007", "coo": "2.0.0_SA_COO~R"})
    rj.main(["bid", "J042", "--serial", "0.0.0_AB_MSTR~Z"])
    assert env.sent[0]["payload"]["available"] is False and env.sent[0]["payload"]["serial"] == "0.0.0_AB_MSTR~Z"


def test_accept_locks_then_close_unlocks(env, tmp_path):
    brief = brief_file(tmp_path)
    digest = rj.sha256_file(brief)
    assert rj.main(["accept", "J042", "--coo", "2.0.0_SA_COO~R", "--brief-file", brief]) == 0
    ev = env.sent[-1]
    assert ev["kind"] == "job.accepted" and ev["event_id"] == "accept-J042"
    assert ev["payload"] == {"device": "laptop", "serial": "0.0.0_AB_MSTR", "coo": "2.0.0_SA_COO~R",
                             "brief_sha256": digest}
    assert rj.read_lock()["job"] == "J042" and rj.read_lock()["brief_sha256"] == digest
    rj.main(["bid", "J043"])
    assert env.sent[-1]["payload"]["available"] is False
    assert rj.main(["close", "J042"]) == 0 and rj.read_lock() is None


def test_accept_refused_while_another_job_is_open(env):
    rj.write_lock({"job": "J007", "coo": "x"})
    assert rj.main(["accept", "J042", "--coo", "2.0.0_SA_COO~R"]) == 2 and env.sent == []
    assert rj.read_lock()["job"] == "J007"


def test_complete_payload_and_attempt_event_id(env, tmp_path):
    rj.main(["accept", "J042", "--coo", "2.0.0_SA_COO~R", "--brief-file", brief_file(tmp_path)])
    sent_before = len(env.sent)
    assert rj.main(["complete", "J042", "--summary", "export fixed"]) == 2    # no grade yet: refused, nothing sent
    assert len(env.sent) == sent_before
    assert grade_pass(tmp_path) == 0
    rj.main(["complete", "J042", "--summary", "export fixed", "--deployed", "--evidence", "commit abc"])
    ev = env.sent[-1]
    assert ev["kind"] == "job.complete" and ev["event_id"] == "complete-J042-1"
    grade = rj.read_lock()["grade"]
    assert grade["by"] == REVIEWER and grade["verdict"] == "PASS"
    assert ev["payload"] == {"device": "laptop", "serial": "0.0.0_AB_MSTR", "summary": "export fixed",
                             "deployed": True, "evidence": "commit abc", "coo": "2.0.0_SA_COO~R", "grade": grade}
    rj.main(["complete", "J042", "--summary", "again", "--attempt", "2"])
    assert env.sent[-1]["event_id"] == "complete-J042-2" and env.sent[-1]["payload"]["deployed"] is False
    assert rj.read_lock()["job"] == "J042"          # the lock stays until close


def test_fail_sends_and_clears_the_lock(env):
    rj.main(["accept", "J042", "--coo", "2.0.0_SA_COO~R"])
    rj.main(["fail", "J042", "--reason", "cannot reproduce"])
    ev = env.sent[-1]
    assert ev["kind"] == "job.failed" and ev["event_id"].startswith("fail-J042-")
    assert ev["payload"] == {"device": "laptop", "serial": "0.0.0_AB_MSTR", "reason": "cannot reproduce"}
    assert rj.read_lock() is None


def test_dry_run_sends_nothing_and_touches_no_lock(env, monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(rj, "make_runtime", lambda: (_ for _ in ()).throw(AssertionError("no send on a dry run")))
    rj.main(["bid", "J042", "--dry-run"])
    rj.main(["accept", "J042", "--coo", "2.0.0_SA_COO~R", "--brief-file", brief_file(tmp_path), "--dry-run"])
    assert rj.read_lock() is None
    rj.write_lock({"job": "J042", "coo": "x"})
    rj.main(["fail", "J042", "--reason", "r", "--dry-run"])
    assert rj.read_lock()["job"] == "J042"
    lines = capsys.readouterr().out.splitlines()
    assert sum(1 for ln in lines if ln.startswith("DRY-RUN: would send")) == 3


def test_device_resolution_refuses_unknown():
    assert rj.parse_device("device: sitez\n  basis: workspace path\n", 0) == "sitez"
    for text, rc in (("device: UNKNOWN\n", 2), ("device: laptop\n", 2), ("", 0), ("device: moon\n", 0)):
        with pytest.raises(SystemExit):
            rj.parse_device(text, rc)


def test_job_id_validation():
    assert rj.job_id(" j042 ") == "J042" and rj.job_id("#J100") == "J100"
    for bad in ("J42", "C042", "J0420", ""):
        with pytest.raises(SystemExit):
            rj.job_id(bad)


def test_show_writes_the_brief_from_a_listener_line(tmp_path):
    award = {"type": "award", "job": "J042", "ldo": "LDO-001", "sent_at": "2026-10-02T17:30:00Z",
             "brief": "Fix the CSV export on the Holdings page.", "requester": "Jane Doe", "chat_title": "Jane Doe"}
    captured = tmp_path / "listener.out"
    captured.write_text("[AGENTBUS -> laptop] REMOTE-JOB AWARD J042 -- yours.\nREMOTE-JOB-JSON %s\n"
                        % json.dumps(award), encoding="utf-8")
    assert rj.main(["show", "J042", "--from-file", str(captured), "--out-dir", str(tmp_path)]) == 0
    text = (tmp_path / "remote-job-J042-brief.md").read_text(encoding="utf-8")
    assert "Fix the CSV export" in text and "Requester: Jane Doe" in text
    assert rj.main(["show", "J043", "--json", "REMOTE-JOB-JSON %s" % json.dumps(award)]) == 2
