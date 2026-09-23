"""Offline independent review of a pinned Y foundation; no live service calls."""
import argparse
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
from unittest.mock import Mock
import zipfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", default="6dc4e888e23c9cf08f591c57456233d855cf5cc7")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(["git", "rev-parse", "--verify", args.pin + "^{commit}"],
                                  cwd=root, text=True).strip()
    snapshot = root / ".runtime/codex-seats/3.0.0_SA_CVO~Y/foundation-review" / pin
    snapshot.mkdir(parents=True, exist_ok=True)
    archive = subprocess.check_output([
        "git", "archive", "--format=zip", pin,
        "infra/aws/lambda/investor-reporting", "docs/contracts/investor-reporting",
        "data/firm_registry.json"], cwd=root)
    hashes = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for member in bundle.infolist():
            destination = (snapshot / member.filename).resolve()
            if not destination.is_relative_to(snapshot.resolve()):
                raise ValueError("archive escapes exact-seat snapshot")
            if member.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
                continue
            data = bundle.read(member)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            hashes[member.filename] = hashlib.sha256(data).hexdigest()
    os.environ["IRPT_FIRM_REGISTRY"] = str(snapshot / "data/firm_registry.json")
    suites = []
    for directory, pattern in (
            ("intake/tests", "test_portfolio.py"),
            ("ycharts/generate/tests", "test_submission.py")):
        command = [sys.executable, "-m", "unittest", "discover", "-s",
                   "infra/aws/lambda/investor-reporting/" + directory, "-p", pattern, "-v"]
        result = subprocess.run(command, cwd=snapshot, text=True, capture_output=True, check=False)
        suites.append({"pattern": pattern, "exit_code": result.returncode,
                       "stdout": result.stdout, "stderr": result.stderr})

    test_path = snapshot / "infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_submission.py"
    spec = importlib.util.spec_from_file_location("foundation_subject_tests", test_path)
    tests = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests)
    wire = tests.DynamoAdapterTests()
    wire.setUp()
    sender = Mock()
    prior = {"identity": {"tenant_id": tests.OWNER["firm_id"], "request_id": wire.rid,
                           "revision": "1"}, "owner": tests.OWNER,
             "browser_sha256": tests.digest(tests.browser()), "composition_ref": tests.REF}
    try:
        wire.read(prior)  # Retry lookup is durable and already accepted.
        wire.read(prior)  # Dispatch reads the same accepted request.
        wire.stub.add_client_error("update_item", "ConditionalCheckFailedException",
            expected_params={"TableName": "irpt-jobs", "Key": tests.ANY,
                             "UpdateExpression": tests.ANY, "ConditionExpression": tests.ANY,
                             "ExpressionAttributeValues": tests.ANY})
        resolve_inputs, artifacts = Mock(), Mock()
        service = tests.SubmissionService(
            acceptance=wire.store, artifacts=artifacts,
            resolve_owner=lambda *args: ("verified-principal", tests.OWNER),
            authorize_current=lambda *args: True, resolve_inputs=resolve_inputs,
            settings={"management_fee": 0}, recipe_version="v1", ingestion_revision="v1",
            destination_revision="v1", send=sender, queue_url="offline")
        outcome = service.submit(tests.browser(), None, {}, {}, None)
        # Repeat at actual submit compute to record the user-visible status text.
        wire.read(prior)
        wire.read(prior)
        wire.stub.add_client_error("update_item", "ConditionalCheckFailedException",
            expected_params={"TableName": "irpt-jobs", "Key": tests.ANY,
                             "UpdateExpression": tests.ANY, "ConditionExpression": tests.ANY,
                             "ExpressionAttributeValues": tests.ANY})
        response = tests.entry.submit_analysis(
            None, {}, {"body": json.dumps(tests.browser())}, None, service)
        wire.stub.assert_no_pending_responses()
        case = {"control": "ConditionalCheckFailedException acquiring dispatch claim",
                "outcome": outcome, "response": response,
                "sender_calls": sender.call_count, "resolve_inputs_calls": resolve_inputs.call_count,
                "artifact_put_calls": artifacts.put.call_count,
                "expected": "Do not assert dispatched without distinguishing SENT from another active claim",
                "observed": {"dispatch_pending": outcome["dispatch_pending"],
                             "description": response["_status"]["actions"][0]["description"]}}
    finally:
        wire.doCleanups()
    evidence = {"candidate_pin": pin, "snapshot_file_sha256": hashes,
                "supplied_suites": suites, "dispatch_claim_control": case,
                "limits": ["No AWS or vendor calls; boto3 Stubber wire boundary",
                           "No persistent service, HTTP guard, worker or browser/export proof",
                           "Conditional error is injected; no claim about server expression evaluation"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in evidence.items()
                      if key != "snapshot_file_sha256"}, indent=2))


if __name__ == "__main__":
    main()
