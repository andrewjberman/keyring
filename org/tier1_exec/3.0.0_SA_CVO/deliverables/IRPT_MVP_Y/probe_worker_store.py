"""Pinned Dynamo worker-store wire review; no server or process-loss simulation."""
import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import unittest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", default="2acea1aeca400c19bfdfcbd94fba01f121ac67ee")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(["git", "rev-parse", "--verify", args.pin + "^{commit}"],
                                  cwd=root, text=True).strip()
    snapshot = root / ".runtime/codex-seats/3.0.0_SA_CVO~Y/worker-review" / pin
    files = ["infra/aws/lambda/investor-reporting/ycharts/generate/" + name for name in (
        "durable_job.py", "submission.py", "tests/test_durable_job.py")]
    hashes = {}
    for name in files:
        data = subprocess.check_output(["git", "show", pin + ":" + name], cwd=root)
        path = snapshot / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    spec = importlib.util.spec_from_file_location("worker_review_tests", snapshot / files[2])
    tests = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests)
    log = io.StringIO()
    suite = unittest.TextTestRunner(stream=log, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromModule(tests))
    controls = []

    def run_case(name, arrange, act, expected):
        case = tests.DurableJobTests()
        case.setUp()
        try:
            arrange(case)
            try:
                act(case)
                observed = "RETURNED"
            except tests.LeaseRefused as exc:
                observed = str(exc)
            case.stub.assert_no_pending_responses()
            controls.append({"case": name, "expected_refusal": expected,
                             "observed": observed, "passed": observed == expected,
                             "update_calls": case.calls})
        finally:
            case.doCleanups()

    run_case("wrong composition on retained read",
             lambda c: c.read(dict(c.row, composition_sha256={"S": "c" * 64})),
             lambda c: c.store.get_state(c.store.request_id), "ACCEPTED_COMPOSITION_MISMATCH")

    def exact_expiry(c):
        c.claim()
        c.clock = 220
        c.read(c.row)

    run_case("assert_current refuses exact expiry equality", exact_expiry,
             lambda c: c.store.assert_current(), "LEASE_LOST")
    run_case("foreign job write refuses before wire", lambda c: None,
             lambda c: c.store.put_state("REQ-" + "c" * 24, "FAILED"), "JOB_IDENTITY_MISMATCH")

    def release(c):
        c.claim()
        c.update()
        c.store.release()
        if c.calls[-1]["UpdateExpression"] != "REMOVE lease_owner, lease_expires_at":
            raise AssertionError("release wire mutates more than lease fields")
        if c.store.fence is not None:
            raise AssertionError("local fence not cleared")

    run_case("release requires new claim before renewal", release,
             lambda c: c.store.renew(), "LEASE_REQUIRED")
    evidence = {"candidate_pin": pin, "file_sha256": hashes,
                "supplied_suite": {"tests_run": suite.testsRun, "failures": len(suite.failures),
                                   "errors": len(suite.errors), "skipped": len(suite.skipped),
                                   "passed": suite.wasSuccessful(), "log": log.getvalue()},
                "independent_controls": controls,
                "limits": ["Actual boto3 adapter; Stubber responses and controlled clock",
                           "No DynamoDB server expression evaluation or process loss",
                           "No orchestrator, publisher, vendor or full S4/E2E proof"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in evidence.items() if key != "file_sha256"}, indent=2))


if __name__ == "__main__":
    main()
