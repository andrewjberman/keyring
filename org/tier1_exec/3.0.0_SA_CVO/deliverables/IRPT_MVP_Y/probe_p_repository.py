"""Pinned P repository review, including boto3 DynamoDB numeric round trips.

Zero network: imports real candidate repository/adapters and uses its test doubles
plus the installed boto3 serializer/deserializer. Does not claim deployed proof.
"""
import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import unittest

from boto3.dynamodb.types import TypeDeserializer, TypeSerializer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", default="70598ece96498d639b0fb12104ffe9fd4b0d5718")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(
        ["git", "rev-parse", "--verify", args.pin + "^{commit}"], cwd=root,
        text=True).strip()
    snapshot = root / ".runtime/codex-seats/3.0.0_SA_CVO~Y/repository-review" / pin
    files = [
        "infra/aws/lambda/investor-reporting/reports/repository.py",
        "infra/aws/lambda/investor-reporting/reports/tests/test_repository.py",
        "docs/contracts/investor-reporting/v1/AnalysisReport.schema.json",
    ]
    hashes = {}
    for name in files:
        data = subprocess.check_output(["git", "show", pin + ":" + name], cwd=root)
        target = snapshot / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    spec = importlib.util.spec_from_file_location("p_candidate_tests", snapshot / files[1])
    tests = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests)
    suite_log = io.StringIO()
    result = unittest.TextTestRunner(stream=suite_log, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromModule(tests))

    serializer, deserializer = TypeSerializer(), TypeDeserializer()

    def dynamo_roundtrip(value):
        return deserializer.deserialize(serializer.serialize(value))

    class DynamoDecodedTable(tests.Table):
        def get_item(self, **kwargs):
            return dynamo_roundtrip(super().get_item(**kwargs))

        def query(self, **kwargs):
            return dynamo_roundtrip(super().query(**kwargs))

    case = tests.ArtifactTests()
    case.setUp()
    case.table = DynamoDecodedTable()
    case.artifacts = case.new_repository()
    operations = []
    for label in ("initial_put", "identical_retry"):
        try:
            receipt = case.put()
            operations.append({"operation": label, "result": "RETURNED", "ref": receipt})
        except Exception as exc:
            operations.append({"operation": label, "result": "RAISED",
                               "exception": type(exc).__name__, "message": str(exc)})
    stored = next(iter(case.table.rows.values()))
    artifact_id = stored["ref"]["artifact_id"]
    for label, action in (
            ("get", lambda: case.artifacts.get(case.principal, artifact_id)),
            ("head", lambda: case.artifacts.head(case.principal, artifact_id))):
        try:
            action()
            operations.append({"operation": label, "result": "RETURNED"})
        except Exception as exc:
            operations.append({"operation": label, "result": "RAISED",
                               "exception": type(exc).__name__, "message": str(exc)})
    decoded = case.table.get_item(
        Key={"tenant": stored["tenant"], "request_revision": stored["request_revision"]},
        ConsistentRead=True)["Item"]
    evidence = {
        "candidate_pin": pin, "file_sha256": hashes,
        "supplied_suite": {"tests_run": result.testsRun, "failures": len(result.failures),
                           "errors": len(result.errors), "skipped": len(result.skipped),
                           "passed": result.wasSuccessful(), "log": suite_log.getvalue()},
        "numeric_control": {"input_value": 7,
                            "decoded_type": type(dynamo_roundtrip(7)).__name__},
        "artifact_byte_length_type": type(decoded["ref"]["byte_length"]).__name__,
        "artifact_operations": operations,
        "published_rows": len(case.table.rows), "blob_puts": case.s3.put_count,
        "limits": ["No AWS or vendor network calls", "Actual candidate adapter classes",
                   "Actual boto3 numeric serialization; synthetic table and S3",
                   "No full S4, deployed, worker-restart or product E2E grade"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in evidence.items() if k != "file_sha256"}, indent=2))


if __name__ == "__main__":
    main()
