"""Independent fenced report-index controls on actual boto wire, without a server."""
import argparse
import contextlib
import copy
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys

from probe_recipe_decimal import deny_network, snapshot, SOURCE_ROOT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", default="6cacc80887")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin, folder, hashes = snapshot(root, args.pin)
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    path = folder / SOURCE_ROOT / "tests/test_report_index.py"
    spec = importlib.util.spec_from_file_location("independent_index_subject", path)
    subject = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subject)
    boundary = contextlib.contextmanager(subject.boundary.__wrapped__)
    controls = []

    def record(name, expected, call, calls, **details):
        try:
            result, error = call(), None
            outcome = "RETURNED"
        except Exception as exc:
            result, error = None, type(exc).__name__
            outcome = getattr(exc, "response", {}).get("Error", {}).get("Code", str(exc))
        controls.append({"name": name, "passed": outcome == expected,
                         "outcome": outcome, "error_type": error, "result": result,
                         "transaction_calls": len(calls), **details})

    with boundary() as (adapter, index, item, _stub, read, calls):
        read(composition_sha256={"S": "e" * 64})
        record("composition_changed_before_publish", "ACCEPTED_COMPOSITION_MISMATCH",
               lambda: adapter.publish(item), calls)
        index.get.assert_not_called()
    with boundary() as (adapter, index, item, _stub, read, calls):
        read(lease_expires_at={"N": "100"})
        record("exact_lease_expiry_before_publish", "LEASE_LOST", lambda: adapter.publish(item), calls)
        index.get.assert_not_called()
    with boundary() as (adapter, _index, item, stub, read, calls):
        read()
        stub.add_response("transact_write_items", {})
        read(fence_token={"N": "8"})
        record("fence_lost_after_successful_transaction_response", "LEASE_LOST",
               lambda: adapter.publish(item), calls,
               limit="Refused acknowledgement; does not roll back the already successful transaction")
    with boundary() as (adapter, index, item, _stub, read, calls):
        read()
        read(lease_owner={"S": "replacement-worker"})
        index.page.return_value = {"items": [item], "next": None}
        record("page_rechecks_lease_after_lookup", "LEASE_LOST",
               lambda: adapter.page(item["tenant"], None, 10), calls)
    with boundary() as (adapter, index, item, stub, read, calls):
        read()
        stub.add_client_error("transact_write_items", "TransactionInProgressException")
        read()
        read()
        retained = copy.deepcopy(item)
        retained["blob"]["version_id"] = "retained-prior-version"
        index.get.return_value = retained
        result = adapter.publish(item)
        controls.append({"name": "in_progress_duplicate_returns_original_receipt",
                         "passed": result == retained, "result": result,
                         "transaction_calls": len(calls)})
    with boundary() as (adapter, index, item, stub, read, calls):
        read()
        stub.add_client_error("transact_write_items", "ProvisionedThroughputExceededException")
        record("throughput_error_propagates_without_duplicate_lookup", "ProvisionedThroughputExceededException",
               lambda: adapter.publish(item), calls)
        index.get.assert_not_called()
    with boundary() as (adapter, index, item, stub, read, calls):
        read()
        stub.add_client_error("transact_write_items", "TransactionCanceledException")
        read()
        read()
        index.get.return_value = None
        record("canceled_transaction_without_prior_row_propagates", "TransactionCanceledException",
               lambda: adapter.publish(item), calls)
    with boundary() as (adapter, _index, item, _stub, _read, calls):
        changed = copy.deepcopy(item)
        changed["ref"]["immutable"] = False
        record("mutable_report_rejected_before_wire", "REPORT_INDEX_BINDING",
               lambda: adapter.publish(changed), calls)
    suite_code = ("import socket,pytest; "
                  "deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError('NETWORK_FORBIDDEN')); "
                  "socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; "
                  "raise SystemExit(pytest.main(['-q','" + SOURCE_ROOT + "/tests/test_report_index.py','"
                  + SOURCE_ROOT + "/tests/test_durable_job.py']))")
    suite = subprocess.run([sys.executable, "-c", suite_code], cwd=folder,
                           capture_output=True, text=True, check=False)
    evidence = {"candidate_pin": pin, "file_sha256": hashes,
                "supplied_suite": {"exit_code": suite.returncode, "stdout": suite.stdout, "stderr": suite.stderr},
                "controls": controls, "passed": sum(row["passed"] for row in controls), "total": len(controls),
                "limits": ["Actual boto client/Stubber and real Y adapters; underlying P index is Mock",
                           "No Dynamo server expression evaluation, simultaneous clients or delay/clock proof",
                           "Post-response lease refusal does not undo a successful index transaction",
                           "No actual P retained repository composition, blob/schema/authorization/expiry proof",
                           "No live network, publication integration or READY/E2E claim"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in evidence.items() if key != "file_sha256"}, indent=2))
    if evidence["passed"] != evidence["total"] or suite.returncode:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
