"""Independent retained upload dependency/clock controls with actual Y/P composition."""
import argparse
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
    source_root = snapshot / "infra/aws/lambda/investor-reporting"
    sys.path.insert(0, str(source_root / "intake/tests"))
    spec = importlib.util.spec_from_file_location("retained_upload_subject",
        source_root / "intake/tests/test_retained_uploads.py")
    subject = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subject)
    controls = []

    def world():
        return subject.world.__wrapped__(subject.test_retention.world.__wrapped__())

    def record(name, passed, **observed):
        controls.append({"name": name, "passed": bool(passed), "observed": observed})

    def capture(call, expected):
        try:
            call()
            return {"refused": False, "type": None, "reason": "RETURNED"}
        except Exception as exc:
            return {"refused": isinstance(exc, expected), "type": type(exc).__name__, "reason": str(exc)}

    def read(w, result):
        return w.case.service.read_input(w.case.principal, w.case.owner, result["input_id"])

    def input_rows(w):
        return sum(key[1].startswith("INPUT#") for key in w.table.rows)

    w = world()
    first = w.case.create()
    deadline = subject.retained(w, first)["expires_at"]
    w.state.now += 10 * subject.DAY
    second = w.case.create(subject.upload_tests.payload(upload_token="dag-refresh-second",
                              supersedes_input_id=first["input_id"]))
    w.state.now += 10 * subject.DAY
    third_body = subject.upload_tests.payload(upload_token="dag-refresh-third",
                                              supersedes_input_id=second["input_id"])
    third = w.case.create(third_body)
    graph = []
    for result in (first, second, third):
        for ref in (subject.original_ref(w, result), result["input_ref"]["artifact_ref"]["retention_ref"]):
            row = w.stores.retention.require_live(w.case.principal, ref)
            graph.append({key: row[key] for key in ("ref", "family", "created_at", "expires_at", "dependencies")})
    expected_dependencies = [[], [graph[0]["ref"]], [graph[1]["ref"]], [graph[2]["ref"]],
                             [graph[3]["ref"]], [graph[4]["ref"]]]
    record("three_revision_dependency_graph_keeps_oldest_deadline",
           all(row["expires_at"] == deadline for row in graph)
           and [row["dependencies"] for row in graph] == expected_dependencies,
           deadline=deadline, graph=graph)
    w.state.now = deadline - 1
    w.stores = subject.build_retained_repositories(w.table, w.case.s3, w.case.authorize,
        lambda *args: None, reporting_policy=w.policy.reporting_policy,
        reporting_destination=lambda firm, family, identity, sha, **kwargs:
            ("offline-private", "/".join((firm, family, identity, sha))), clock=lambda: w.state.now)
    w.case.service = w.case.new_service()
    w.case.service.artifacts = w.stores.artifacts

    def must_not_refresh(*args):
        raise AssertionError("retained replay refreshed a dependency")

    w.case.service.resolve_security = must_not_refresh
    w.case.service.resolve_prices = must_not_refresh
    w.case.service.parse_mapping = must_not_refresh
    puts = w.case.s3.put_count
    replay = w.case.create(third_body)
    live = subject.retained(w, third)
    record("repository_recomposition_retry_at_last_live_second",
           replay == third and live["expires_at"] == deadline and puts == w.case.s3.put_count,
           same_result=replay == third, deadline=live["expires_at"], extra_blob_puts=w.case.s3.put_count - puts)
    root_key = (w.case.owner["firm_id"], "RETENTION#" + graph[0]["ref"]["retention_id"])
    root_row = w.table.rows.pop(root_key)
    result = capture(lambda: read(w, third), subject.RetentionExpired)
    record("missing_oldest_retention_record_refuses_descendant", result["refused"], **result)
    w.table.rows[root_key] = root_row
    w.state.now = deadline
    read_expired = capture(lambda: read(w, third), subject.RetentionExpired)
    refresh_expired = capture(lambda: w.case.create(subject.upload_tests.payload(
        upload_token="expired-dag-refresh", supersedes_input_id=third["input_id"])), subject.RetentionExpired)
    record("exact_oldest_deadline_refuses_descendant_read_and_refresh",
           read_expired["refused"] and refresh_expired["refused"] and puts == w.case.s3.put_count,
           read=read_expired, refresh=refresh_expired, extra_blob_puts=w.case.s3.put_count - puts)

    w = world()
    first = w.case.create()
    w.case.s3.on_get = lambda: w.registered.update(state="PENDING_ENFORCEMENT")
    result = capture(lambda: read(w, first), subject.RetentionRefused)
    record("policy_becomes_pending_during_blob_read", result["refused"], **result)

    w = world()
    first = w.case.create()
    deadline = subject.retained(w, first)["expires_at"]
    real_put = w.case.s3.put_object

    def delayed_refresh_put(**kwargs):
        receipt = real_put(**kwargs)
        w.state.now = deadline
        return receipt

    w.case.s3.put_object = delayed_refresh_put
    puts, inputs = w.case.s3.put_count, input_rows(w)
    result = capture(lambda: w.case.create(subject.upload_tests.payload(
        upload_token="late-original-refresh", supersedes_input_id=first["input_id"])), subject.RetentionExpired)
    record("expiry_during_refreshed_original_blob_write",
           result["refused"] and input_rows(w) == inputs,
           **result, extra_blob_puts=w.case.s3.put_count - puts, extra_input_rows=input_rows(w) - inputs)

    w = world()
    deadline = w.state.now + 30 * subject.DAY
    real_put = w.case.s3.put_object

    def delayed_normalized_put(**kwargs):
        receipt = real_put(**kwargs)
        if w.case.s3.put_count == 2:
            w.state.now = deadline
        return receipt

    w.case.s3.put_object = delayed_normalized_put
    result = capture(lambda: w.case.create(), subject.RetentionExpired)
    record("expiry_during_normalized_blob_write", result["refused"] and input_rows(w) == 0,
           **result, blob_puts=w.case.s3.put_count, input_rows=input_rows(w))

    w = world()
    first = w.case.create()
    w.case.s3.on_get = lambda: w.case.headers.update({"x-user-email": "revoked@example.invalid"})
    result = capture(lambda: read(w, first), PermissionError)
    record("current_owner_revoked_during_blob_read", result["refused"], **result)

    w = world()
    first = w.case.create()
    w.case.service.artifacts.retention = None
    result = capture(lambda: read(w, first), sys.modules["repository"].ReportRefused)
    record("retained_input_cannot_use_repository_without_retention_service", result["refused"], **result)

    paths = ["intake/tests/test_uploads.py", "intake/tests/test_retained_uploads.py",
             "reports/tests/test_retained_repository.py"]
    suite_code = ("import socket,pytest; "
        "deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError('NETWORK_FORBIDDEN')); "
        "socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; "
        "raise SystemExit(pytest.main(" + repr(["-q"] + [str(source_root / p) for p in paths]) + "))")
    suite = subprocess.run([sys.executable, "-c", suite_code], cwd=snapshot,
                           capture_output=True, text=True, check=False)
    evidence = {"candidate_pin": pin, "source_evidence": str(args.source_evidence),
                "source_evidence_sha256": hashlib.sha256(args.source_evidence.read_bytes()).hexdigest(),
                "verified_snapshot_files": len(source["snapshot_file_sha256"]),
                "supplied_suite": {"exit_code": suite.returncode, "stdout": suite.stdout, "stderr": suite.stderr},
                "controls": controls, "passed": sum(row["passed"] for row in controls), "total": len(controls),
                "limits": ["Actual Y upload + P retained repository/policy; storage and clocks are doubles",
                           "Isolated ACTIVE policy fixture; canonical policy not activated",
                           "Late successful blob writes can remain stored; no physical cleanup proof",
                           "No concurrent server, real process crash, report promotion, runtime/browser or READY proof",
                           "R-P08 history metadata is outside these upload controls; see separately pinned peer review"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    if evidence["passed"] != evidence["total"] or suite.returncode:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
