"""Pinned retained request composition and dispatch review; all transports offline."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess
import sys

from probe_recipe_decimal import deny_network


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-evidence", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    source = json.loads(args.source_evidence.read_text(encoding="utf-8"))
    pin = source["candidate_pin"]
    snapshot = root / ".runtime/codex-seats/3.0.0_SA_CVO~Y/upload-review" / pin
    for relative, expected in source["snapshot_file_sha256"].items():
        if hashlib.sha256((snapshot / relative).read_bytes()).hexdigest() != expected:
            raise ValueError("snapshot changed: " + relative)
    os.environ["IRPT_FIRM_REGISTRY"] = str(snapshot / "data/firm_registry.json")
    socket.socket.connect = deny_network
    socket.socket.connect_ex = deny_network
    socket.create_connection = deny_network
    code_root = snapshot / "infra/aws/lambda/investor-reporting"
    sys.path.insert(0, str(code_root / "intake/tests"))
    spec = importlib.util.spec_from_file_location("request_retention_subject",
        code_root / "intake/tests/test_retained_uploads.py")
    subject = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subject)
    controls = []

    def world():
        return subject.world.__wrapped__(subject.test_retention.world.__wrapped__())

    def record(name, passed, **observed):
        controls.append({"name": name, "passed": bool(passed), "observed": observed})

    def invoke(service, acceptance, body):
        before = acceptance.dispatch.call_count
        try:
            result = service.submit(body, None, {}, {}, None)
            return {"returned": result, "error_type": None, "reason": None,
                    "dispatch_calls": acceptance.dispatch.call_count - before}
        except Exception as exc:
            return {"returned": None, "error_type": type(exc).__name__, "reason": str(exc),
                    "dispatch_calls": acceptance.dispatch.call_count - before}

    w = world()
    first = w.case.create()
    deadline = subject.retained(w, first)["expires_at"]
    w.state.now += 20 * subject.DAY
    service, acceptance, body, _loaded = subject.submission(w, first)
    initial = invoke(service, acceptance, body)
    ref = copy.deepcopy(acceptance.accept.call_args.args[2])
    retained = w.stores.retention.require_live(w.case.principal, ref["retention_ref"])
    record("request_composition_inherits_exact_input_dependency_and_deadline",
           initial["returned"] is not None and initial["dispatch_calls"] == 1
           and retained["expires_at"] == deadline
           and retained["dependencies"] == [first["input_ref"]["artifact_ref"]["retention_ref"]],
           invocation=initial, composition_ref=ref, deadline=retained["expires_at"],
           dependencies=retained["dependencies"])
    acceptance.lookup.return_value = {"owner": acceptance.accept.call_args.args[0],
        "composition_ref": ref, "identity": initial["returned"]["identity"]}

    def forbidden(*args):
        raise AssertionError("semantic replay re-resolved provider input")

    service.resolve_inputs = forbidden
    before_puts = w.case.s3.put_count
    replay = invoke(service, acceptance, body)
    record("live_replay_preserves_result_without_provider_reread",
           replay["returned"] == initial["returned"] and w.case.s3.put_count == before_puts,
           invocation=replay, extra_blob_puts=w.case.s3.put_count - before_puts)
    w.state.now = deadline
    expired = invoke(service, acceptance, body)
    record("configured_retention_refuses_expired_replay",
           expired["error_type"] == "RetentionExpired" and expired["dispatch_calls"] == 0,
           invocation=expired)
    service.artifacts.retention = None
    missing_service = invoke(service, acceptance, body)
    record("expired_retained_replay_requires_retention_service",
           missing_service["error_type"] is not None and missing_service["dispatch_calls"] == 0,
           invocation=missing_service, retained_composition_ref_present="retention_ref" in ref,
           current_time=w.state.now, accepted_deadline=deadline,
           expected="Refuse missing retention service before dispatch for a known retained record")

    w = world()
    first = w.case.create()
    service, acceptance, body, loaded = subject.submission(w, first)
    service.artifacts.retention = None
    no_service_first = invoke(service, acceptance, body)
    accepted_ref = (acceptance.accept.call_args.args[2] if acceptance.accept.called else None)
    record("retained_input_requires_retention_service_on_first_submission",
           no_service_first["error_type"] is not None and no_service_first["dispatch_calls"] == 0
           and not acceptance.accept.called,
           invocation=no_service_first,
           input_has_retention="retention_ref" in loaded["input_ref"]["artifact_ref"],
           accepted_ref=accepted_ref,
           expected="Refuse retained-input downgrade before bare composition storage/acceptance/dispatch")

    w = world()
    first = w.case.create()
    service, acceptance, body, loaded = subject.submission(w, first)
    loaded["input_ref"]["artifact_ref"]["version_id"] = "changed-version"
    before_puts = w.case.s3.put_count
    altered = invoke(service, acceptance, body)
    record("changed_retained_input_receipt_refuses_before_storage",
           altered["reason"] == "RETAINED_INPUT_BINDING" and altered["dispatch_calls"] == 0
           and before_puts == w.case.s3.put_count and not acceptance.accept.called,
           invocation=altered, extra_blob_puts=w.case.s3.put_count - before_puts)

    for mode in ("expiry", "policy_pending"):
        w = world()
        first = w.case.create()
        service, acceptance, body, _loaded = subject.submission(w, first)
        deadline = subject.retained(w, first)["expires_at"]

        def after_accept(owner, browser, receipt, **kwargs):
            if mode == "expiry":
                w.case.s3.on_get = lambda: setattr(w.state, "now", deadline)
            else:
                w.registered["state"] = "PENDING_ENFORCEMENT"
            return {"owner": owner, "composition_ref": receipt, "identity": {"request_id": "REQ-offline"}}

        acceptance.accept.side_effect = after_accept
        result = invoke(service, acceptance, body)
        expected = "RetentionExpired" if mode == "expiry" else "RetentionRefused"
        record(mode + "_after_acceptance_refuses_dispatch",
               result["error_type"] == expected and result["dispatch_calls"] == 0,
               invocation=result)
    paths = ["intake/tests/test_uploads.py", "intake/tests/test_retained_uploads.py",
             "ycharts/generate/tests/test_submission.py", "reports/tests/test_retained_repository.py"]
    suite_code = ("import socket,pytest; "
        "deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError('NETWORK_FORBIDDEN')); "
        "socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; "
        "raise SystemExit(pytest.main(" + repr(["-q"] + [str(code_root / path) for path in paths]) + "))")
    suite = subprocess.run([sys.executable, "-c", suite_code], cwd=snapshot,
                           capture_output=True, text=True, check=False)
    evidence = {"candidate_pin": pin, "source_evidence": str(args.source_evidence),
                "source_evidence_sha256": hashlib.sha256(args.source_evidence.read_bytes()).hexdigest(),
                "verified_snapshot_files": len(source["snapshot_file_sha256"]),
                "supplied_suite": {"exit_code": suite.returncode, "stdout": suite.stdout, "stderr": suite.stderr},
                "controls": controls, "passed": sum(row["passed"] for row in controls), "total": len(controls),
                "limits": ["Actual Y SubmissionService and P retained artifacts/policy",
                           "Acceptance lookup/accept/dispatch are Mock; dispatch-call evidence, not real queue/vendor",
                           "Storage and clock doubles; no server concurrency/recovery/runtime assembly",
                           "Missing-service control models miscomposed/restarted service with existing retained records",
                           "No READY, live policy activation, full S4/S7 or integrated product proof"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    if evidence["passed"] != evidence["total"] or suite.returncode:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
