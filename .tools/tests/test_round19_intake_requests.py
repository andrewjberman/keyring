#!/usr/bin/env python3
"""Round-19 intake request arms (CT-ai-6): file, decide, status, show, and downloads-today.

Default arms run org/devices/intake/intake_request.py in a temporary folder; every tool call is a
separate process. --downloads runs the downloads-today reader over a fixture folder.
Last line: INTAKE-REQUESTS arms=<k>/<n> ok=<True|False>, or INTAKE-DOWNLOADS arms=<k>/<n> ok=<True|False>.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
TOOL = os.path.join(REPO, "org", "devices", "intake", "intake_request.py")
SERIAL = "0.9.0_WK_NFRA_CTLPLN~111"
DECIDER_APPROVE = "1.0.0_SA_CTO"
DECIDER_REFUSE = "4.0.0_SA_CRO"
REASON_APPROVE = "the brief needs pkgapproved 2.1.0 for the record reader"
REASON_REFUSE = "2.1.0 is the wrong major for the brief"


def run(args, device_env=None):
    env = dict(os.environ)
    if device_env:
        env["AGENTBUS_DEVICE"] = device_env
    p = subprocess.run([sys.executable, TOOL] + args, capture_output=True, text=True,
                       env=env, timeout=120)
    return p.returncode, p.stdout, p.stderr


def last_line(out):
    lines = [x for x in out.splitlines() if x.strip()]
    return lines[-1] if lines else ""


def write(path, text):
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        fh.write(text)


def request_files(root):
    d = os.path.join(root, "requests")
    if not os.path.isdir(d):
        return []
    return sorted(f for f in os.listdir(d) if f.startswith("REQ-") and f.endswith(".json"))


def read_request(root, rid):
    with open(os.path.join(root, "requests", rid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def default_arms(tmp):
    root = os.path.join(tmp, "intake")
    os.makedirs(root)
    reqs = os.path.join(tmp, "requirements.txt")
    write(reqs, "# test requirements\npinned-here==1.0.0  # test pin\n")
    ev_a = os.path.join(tmp, "evidence_approve.md")
    ev_r = os.path.join(tmp, "evidence_refuse.md")
    ev_missing = os.path.join(tmp, "no_such_evidence.md")
    write(ev_a, "approval evidence A\n")
    write(ev_r, "refusal evidence R\n")
    common = ["--root", root]
    needs = ["--needed-by", "lane NFRA_CTLPLN", "--why-no-approved",
             "no approved version reads the brief", "--by", SERIAL]
    results = []

    def arm(label, ok):
        results.append(bool(ok))
        print("ARM %-2d %s %s" % (len(results), "PASS" if ok else "FAIL", label))

    rc_a, out_a, _ = run(["file", "--name", "pkgapproved", "--version", "2.1.0"] + common + needs)
    id_a = (re.search(r"id=(REQ-\S+)", out_a) or [None, None])[1]
    arm("file approved-candidate (rc 0, FILED id, decisions empty)",
        rc_a == 0 and id_a and read_request(root, id_a)["decisions"] == [])
    rc_r, out_r, _ = run(["file", "--name", "pkgrefused", "--version", "3.0.0"] + common + needs)
    id_r = (re.search(r"id=(REQ-\S+)", out_r) or [None, None])[1]
    arm("file refused-candidate (rc 0)", rc_r == 0 and id_r)
    rc_q, out_q, _ = run(["file", "--name", "pkgrequested", "--version", "0.5.0"] + common + needs)
    id_q = (re.search(r"id=(REQ-\S+)", out_q) or [None, None])[1]
    arm("file still-requested (rc 0)", rc_q == 0 and id_q)
    arm("request folder holds exactly the three filed requests", len(request_files(root)) == 3)

    rc, out, _ = run(["decide", "--id", id_a, "--verdict", "APPROVED", "--by", DECIDER_APPROVE,
                      "--reason", REASON_APPROVE, "--evidence", ev_a] + common)
    arm("decide APPROVED on the approved-candidate (rc 0)", rc == 0)
    rc, out, _ = run(["decide", "--id", id_r, "--verdict", "REFUSED", "--by", DECIDER_REFUSE,
                      "--reason", REASON_REFUSE, "--evidence", ev_r] + common)
    arm("decide REFUSED on the refused-candidate (rc 0)", rc == 0)

    st = ["status", "--name", "pkgapproved", "--version", "2.1.0"] + common + ["--requirements", reqs]
    rc1, o1, _ = run(st + ["--device", "laptop"])
    rc2, o2, _ = run(st + ["--device", "dell1"], device_env="dell1")
    arm("status approved: identical across two devices, APPROVED by the CTO",
        rc1 == 0 and rc2 == 0 and o1 == o2 and " APPROVED by=%s " % DECIDER_APPROVE in o1)
    st = ["status", "--name", "pkgrefused", "--version", "3.0.0"] + common + ["--requirements", reqs]
    rc1, o1, _ = run(st + ["--device", "laptop"])
    rc2, o2, _ = run(st + ["--device", "dell1"], device_env="dell1")
    arm("status refused: identical across two devices, REFUSED by the CRO",
        rc1 == 0 and rc2 == 0 and o1 == o2 and " REFUSED by=%s " % DECIDER_REFUSE in o1)
    st = ["status", "--name", "pkgrequested", "--version", "0.5.0"] + common + ["--requirements", reqs]
    rc1, o1, _ = run(st + ["--device", "laptop"])
    rc2, o2, _ = run(st + ["--device", "dell1"], device_env="dell1")
    arm("status still-requested: identical across two devices, REQUESTED",
        rc1 == 0 and rc2 == 0 and o1 == o2 and " REQUESTED by=- " in o1)
    st = ["status", "--name", "pkgnever", "--version", "9.9.9"] + common + ["--requirements", reqs]
    rc1, o1, _ = run(st + ["--device", "laptop"])
    rc2, o2, _ = run(st + ["--device", "dell1"], device_env="dell1")
    arm("status unknown: identical across two devices, UNKNOWN",
        rc1 == 0 and rc2 == 0 and o1 == o2 and " UNKNOWN by=- " in o1)
    rc, out, _ = run(["status", "--name", "pinned_here", "--version", "1.0.0"] + common
                     + ["--requirements", reqs])
    arm("status pinned in requirements.txt reads APPROVED by=requirements.txt",
        rc == 0 and " APPROVED by=requirements.txt " in out)

    rc, out, _ = run(["show", "--id", id_a] + common)
    arm("show approved, read back by a second process (decision, who, why, evidence)",
        rc == 0 and "DECISION: APPROVED" in out and DECIDER_APPROVE in out
        and REASON_APPROVE in out and "exact version: 2.1.0" in out)
    rc, out, _ = run(["show", "--id", id_r] + common)
    arm("show refused, read back by a second process (REFUSED, who, why)",
        rc == 0 and "DECISION: REFUSED" in out and DECIDER_REFUSE in out
        and REASON_REFUSE in out)

    rc, out, _ = run(["decide", "--id", id_a, "--verdict", "REFUSED", "--by", DECIDER_REFUSE,
                      "--reason", "second opinion", "--evidence", ev_r] + common)
    arm("second decision on the same request refused (rc != 0, one decision kept)",
        rc != 0 and "REFUSED" in out and len(read_request(root, id_a)["decisions"]) == 1)
    rc, out, _ = run(["decide", "--id", id_q, "--verdict", "APPROVED", "--by", DECIDER_APPROVE,
                      "--reason", "no evidence", "--evidence", ev_missing] + common)
    arm("decide with a missing evidence file refused (rc != 0, no decision written)",
        rc != 0 and "REFUSED" in out and read_request(root, id_q)["decisions"] == [])
    return results


def fetch_fixture(root):
    rdir = os.path.join(root, "records", "intake-20261015-a")
    os.makedirs(rdir)
    recs = {
        "one.whl.fetch.json": {"schema": "intake-fetch/1", "device": "laptop",
                               "at": "2026-10-15T09:00:00Z",
                               "requests": [{"url": "u1"}, {"url": "u2"}]},
        "two.whl.fetch.json": {"schema": "intake-fetch/1", "device": "laptop",
                               "at": "2026-10-15T10:30:00Z",
                               "requests": [{"url": "u3"}, {"url": "u4"}, {"url": "u5"}]},
        "old.whl.fetch.json": {"schema": "intake-fetch/1", "device": "laptop",
                               "at": "2026-10-14T23:59:00Z",
                               "requests": [{"url": "u6"}]},
    }
    for name, rec in recs.items():
        write(os.path.join(rdir, name), json.dumps(rec, indent=2) + "\n")


def downloads_arms(tmp):
    root = os.path.join(tmp, "intake_fx")
    os.makedirs(root)
    fetch_fixture(root)
    results = []

    def arm(label, ok):
        results.append(bool(ok))
        print("ARM %-2d %s %s" % (len(results), "PASS" if ok else "FAIL", label))

    rc, out, err = run(["downloads", "--device", "laptop", "--day", "20261015", "--root", root])
    arm("downloads laptop 20261015: two records counted, requests 2+3, one other day excluded",
        rc == 0 and last_line(out) == "DOWNLOADS-TODAY device=laptop day=20261015 requests=5 files=2 unattributed=0")
    rc, out, err = run(["downloads", "--device", "laptop", "--day", "20261016", "--root", root])
    arm("downloads on a day with no records: zero, read from the record folder (rc 0)",
        rc == 0 and last_line(out) == "DOWNLOADS-TODAY device=laptop day=20261016 requests=0 files=0 unattributed=0")
    rc, out, err = run(["downloads", "--device", "dell1", "--day", "20261015", "--root", root])
    arm("downloads for another device: records of laptop not counted",
        rc == 0 and last_line(out) == "DOWNLOADS-TODAY device=dell1 day=20261015 requests=0 files=0 unattributed=0")
    rc, out, err = run(["downloads", "--device", "laptop", "--day", "20261015",
                        "--root", os.path.join(tmp, "no_such_folder")])
    arm("missing intake folder REFUSED (rc != 0)", rc != 0 and "REFUSED" in out)
    empty = os.path.join(tmp, "intake_empty")
    os.makedirs(empty)
    rc, out, err = run(["downloads", "--device", "laptop", "--day", "20261015", "--root", empty])
    arm("missing record folder under an existing intake folder REFUSED (rc != 0)",
        rc != 0 and "REFUSED" in out)
    return results


def main():
    mode = "--downloads" in sys.argv[1:]
    tmp = tempfile.mkdtemp(prefix="intake_round19_")
    try:
        results = downloads_arms(tmp) if mode else default_arms(tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    k, n = sum(results), len(results)
    tag = "INTAKE-DOWNLOADS" if mode else "INTAKE-REQUESTS"
    print("%s arms=%d/%d ok=%s" % (tag, k, n, k == n))
    return 0 if k == n else 1


if __name__ == "__main__":
    sys.exit(main())
