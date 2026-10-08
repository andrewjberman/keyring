"""Test for .tools/remote-job.py's reviewer step: the grade, the brief file and the reviewer-aware bid.

Run as a plain script: python .tools/tests/test_remote_job_review.py
Nothing is sent: the LDO runtime is a fake, the lock and the liveness file live in a temporary directory, and the
device and CPU/memory reads are replaced. LAST line: REMOTE-JOB-REVIEW-TEST ok=<True|False> cases=<passed>/<total>
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("remote_job", os.path.join(HERE, "..", "remote-job.py"))
rj = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rj)

COO = "2.0.0_SA_COO~R"
CVO = "3.0.0_SA_CVO"
MSTR = "0.0.0_AB_MSTR"


class FakeRuntime:
    def __init__(self):
        self.sent = []

    def send(self, object_id, kind, payload=None, event_id=None):
        self.sent.append({"object_id": object_id, "kind": kind, "payload": payload, "event_id": event_id})
        return event_id


RESULTS = []


def case(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print("%s: %s %s" % ("PASS" if cond else "FAIL", name, "" if cond else detail))


def run(argv):
    """(rc, printed text) of rj.main(argv)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = rj.main(argv)
    return rc, buf.getvalue()


def write_liveness(path, entries):
    now = time.time()
    doc = {serial: {"last_seen_epoch": now - age} for serial, age in entries.items()}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh)


def main():
    tmp = tempfile.mkdtemp(prefix="rj-review-")
    rt = FakeRuntime()
    rj.LOCK = os.path.join(tmp, ".remote-job.json")
    rj.device_name = lambda: "laptop"
    rj.measure = lambda: (12.5, 40.0)
    rj.make_runtime = lambda: rt
    os.environ.pop("OPAL_AGENT_SERIAL", None)
    live = os.path.join(tmp, "liveness.json")
    os.environ["OPAL_LIVENESS_FILE"] = live

    brief = os.path.join(tmp, "brief.md")
    with open(brief, "w", encoding="utf-8") as fh:
        fh.write("# Remote job J042\n\nFix the CSV export.\n")
    empty = os.path.join(tmp, "empty.md")
    open(empty, "w").close()
    record = os.path.join(tmp, "grade-record.md")
    with open(record, "w", encoding="utf-8") as fh:
        fh.write("PASS: read the real artifact\n")

    def reset():
        if os.path.exists(rj.LOCK):
            os.remove(rj.LOCK)
        del rt.sent[:]

    def accepted():
        reset()
        rc, _ = run(["accept", "J042", "--coo", COO, "--brief-file", brief])
        return rc

    # -- accept ---------------------------------------------------------------------------------------------------
    reset()
    rc, text = run(["accept", "J042", "--coo", COO])
    case("accept without --brief-file refuses, no lock, nothing sent",
         rc == 2 and text.startswith("ERROR:") and rj.read_lock() is None and rt.sent == [], (rc, text))
    rc, text = run(["accept", "J042", "--coo", COO, "--brief-file", os.path.join(tmp, "nope.md")])
    case("accept with a missing brief file refuses, no lock, nothing sent",
         rc == 2 and text.startswith("ERROR:") and rj.read_lock() is None and rt.sent == [], (rc, text))
    rc, text = run(["accept", "J042", "--coo", COO, "--brief-file", empty])
    case("accept with an empty brief file refuses, no lock, nothing sent",
         rc == 2 and text.startswith("ERROR:") and rj.read_lock() is None and rt.sent == [], (rc, text))
    rc, text = run(["accept", "J042", "--coo", MSTR, "--brief-file", brief])
    case("accept with a --coo that is not a 2.0.0_SA_COO~lane serial refuses",
         rc == 2 and text.startswith("ERROR:") and rj.read_lock() is None and rt.sent == [], (rc, text))
    want = hashlib.sha256(open(brief, "rb").read()).hexdigest()
    rc = accepted()
    lock = rj.read_lock() or {}
    case("accept with a real brief file locks and carries its SHA-256 (lock and payload)",
         rc == 0 and lock.get("brief_sha256") == want and len(rt.sent) == 1
         and rt.sent[0]["payload"].get("brief_sha256") == want and rt.sent[0]["kind"] == "job.accepted",
         (rc, lock, rt.sent))

    # -- complete / grade -----------------------------------------------------------------------------------------
    refusal = "ERROR: J042 has no passing reviewer grade on this box; nothing sent"
    accepted()
    del rt.sent[:]
    rc, text = run(["complete", "J042", "--summary", "done"])
    case("complete with no grade refuses with the exact line and sends nothing",
         rc == 2 and text.strip() == refusal and rt.sent == [], (rc, text, rt.sent))

    rc, text = run(["grade", "J042", "--as", CVO, "--verdict", "FAIL", "--record", record])
    case("a FAIL grade is written (OK line, nothing sent)",
         rc == 0 and text.strip() == "OK: J042 graded FAIL by %s" % CVO and rt.sent == []
         and (rj.read_lock() or {}).get("grade", {}).get("verdict") == "FAIL", (rc, text))
    rc, text = run(["complete", "J042", "--summary", "done"])
    case("after a FAIL grade, complete still refuses and sends nothing",
         rc == 2 and text.strip() == refusal and rt.sent == [], (rc, text, rt.sent))

    rc, text = run(["grade", "J042", "--as", COO, "--verdict", "PASS", "--record", record])
    case("grade --as the job's own operations seat refuses",
         rc == 2 and text.startswith("ERROR:") and (rj.read_lock() or {}).get("grade", {}).get("verdict") == "FAIL",
         (rc, text))
    rc, text = run(["grade", "J042", "--as", MSTR, "--verdict", "PASS", "--record", record])
    case("grade --as a manager serial refuses",
         rc == 2 and text.startswith("ERROR:") and (rj.read_lock() or {}).get("grade", {}).get("verdict") == "FAIL",
         (rc, text))
    rc, text = run(["grade", "J042", "--as", CVO, "--verdict", "PASS", "--record", os.path.join(tmp, "none.md")])
    case("grade with a missing record file refuses",
         rc == 2 and text.startswith("ERROR:") and (rj.read_lock() or {}).get("grade", {}).get("verdict") == "FAIL",
         (rc, text))
    rc, text = run(["grade", "J043", "--as", CVO, "--verdict", "PASS", "--record", record])
    case("grade for a job the lock does not name refuses",
         rc == 2 and text.startswith("ERROR:") and (rj.read_lock() or {}).get("grade", {}).get("verdict") == "FAIL",
         (rc, text))
    os.environ["OPAL_AGENT_SERIAL"] = "3.0.0_SA_CVO~X"
    rc, text = run(["grade", "J042", "--as", CVO, "--verdict", "PASS", "--record", record])
    os.environ.pop("OPAL_AGENT_SERIAL", None)
    case("grade with OPAL_AGENT_SERIAL set to another serial refuses",
         rc == 2 and text.startswith("ERROR:") and (rj.read_lock() or {}).get("grade", {}).get("verdict") == "FAIL",
         (rc, text))

    # the difference control: the same completion, refused above, built after a PASS by the reviewer
    rc, text = run(["grade", "J042", "--as", CVO, "--verdict", "PASS", "--record", record])
    case("a PASS grade by 3.0.0_SA_CVO is written", rc == 0 and text.strip() == "OK: J042 graded PASS by %s" % CVO
         and rt.sent == [], (rc, text))
    rc, text = run(["complete", "J042", "--summary", "done", "--dry-run"])
    env_line = [ln for ln in text.splitlines() if ln.startswith("DRY-RUN: would send ")]
    envelope = json.loads(env_line[0][len("DRY-RUN: would send "):]) if env_line else {}
    p = envelope.get("payload", {})
    case("after the PASS grade the same complete builds an envelope carrying coo and grade (dry run, nothing sent)",
         rc == 0 and envelope.get("kind") == "job.complete" and p.get("coo") == COO
         and p.get("grade", {}).get("by") == CVO and p.get("grade", {}).get("verdict") == "PASS"
         and p.get("grade", {}).get("record") == record and p.get("grade", {}).get("at") and rt.sent == [],
         (rc, text))
    rc, text = run(["complete", "J042", "--summary", "done"])
    case("after the PASS grade a real-path complete reaches the (fake) sender with the same payload",
         rc == 0 and len(rt.sent) == 1 and rt.sent[0]["payload"].get("grade", {}).get("verdict") == "PASS"
         and rt.sent[0]["payload"].get("coo") == COO, (rc, text, rt.sent))

    # a grade whose `by` equals the lock's coo (a tampered lock) is not a passing grade
    lock = rj.read_lock()
    lock["grade"]["by"] = COO
    rj.write_lock(lock)
    del rt.sent[:]
    rc, text = run(["complete", "J042", "--summary", "done"])
    case("complete re-checks that the grade is not by the operations seat",
         rc == 2 and text.strip() == refusal and rt.sent == [], (rc, text))

    # complete with no lock at all (the old warn-and-send path is gone)
    reset()
    rc, text = run(["complete", "J042", "--summary", "done"])
    case("complete with no lock refuses and sends nothing",
         rc == 2 and text.strip() == refusal and rt.sent == [], (rc, text))

    # -- bid --------------------------------------------------------------------------------------------------------
    reset()
    write_liveness(live, {MSTR: 5, COO: 5})
    rc, text = run(["bid", "J042"])
    p = rt.sent[-1]["payload"] if rt.sent else {}
    case("bid with no reviewer in the liveness file: available false, reason no_reviewer, a WARN line",
         rc == 0 and p.get("available") is False and p.get("unavailable_reason") == "no_reviewer"
         and p.get("reviewer") is None and "WARN:" in text, (rc, text, p))
    write_liveness(live, {MSTR: 5, CVO: 30})
    del rt.sent[:]
    rc, text = run(["bid", "J042"])
    p = rt.sent[-1]["payload"] if rt.sent else {}
    case("bid with a reviewer seen 30 seconds ago: available true and the reviewer named",
         rc == 0 and p.get("available") is True and p.get("reviewer") == CVO and "unavailable_reason" not in p, p)
    write_liveness(live, {MSTR: 5, CVO + "~Z": 600})
    del rt.sent[:]
    rc, text = run(["bid", "J042"])
    p = rt.sent[-1]["payload"] if rt.sent else {}
    case("bid with a reviewer seen 10 minutes ago: available false",
         rc == 0 and p.get("available") is False and p.get("unavailable_reason") == "no_reviewer"
         and p.get("reviewer") is None, p)
    write_liveness(live, {CVO + "~Z": 10})
    accepted()
    del rt.sent[:]
    rc, text = run(["bid", "J043"])
    p = rt.sent[-1]["payload"] if rt.sent else {}
    case("bid while a job is open keeps job_open even with a live reviewer",
         p.get("available") is False and p.get("unavailable_reason") == "job_open" and p.get("reviewer") == CVO + "~Z", p)
    os.environ["OPAL_LIVENESS_FILE"] = os.path.join(tmp, "absent.json")
    reset()
    rc, text = run(["bid", "J042", "--dry-run"])
    case("bid with no liveness file reads as no reviewer, and a dry run sends nothing",
         rc == 0 and rt.sent == [] and '"no_reviewer"' in text, text)

    passed = sum(1 for _, ok in RESULTS if ok)
    ok = passed == len(RESULTS)
    print("REMOTE-JOB-REVIEW-TEST ok=%s cases=%d/%d" % (ok, passed, len(RESULTS)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
