"""Independent refresh controls against a source-hashed offline upload snapshot."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path


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
    path = snapshot / "infra/aws/lambda/investor-reporting/intake/tests/test_uploads.py"
    spec = importlib.util.spec_from_file_location("refresh_review_subject", path)
    subject = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subject)
    case = subject.UploadIntegrationTests()
    case.setUp()
    controls = []

    def record(name, passed, **observed):
        controls.append({"name": name, "passed": bool(passed), "observed": observed})

    def refuses(name, call, error_type, reason):
        before = case.s3.put_count
        try:
            call()
            outcome, error, matches_type = "RETURNED", None, False
        except (subject.UploadRefused, PermissionError) as exc:
            outcome, error, matches_type = str(exc), type(exc).__name__, isinstance(exc, error_type)
        record(name, matches_type and reason in outcome
               and before == case.s3.put_count,
               outcome=outcome, error_type=error, additional_blob_puts=case.s3.put_count - before)

    def quote(price):
        return {"S:AAPL": {"security_id": "S:AAPL", "price": str(price), "currency": "USD",
                           "as_of": "2026-09-21", "source_revision": "independent-price-" + str(price)}}

    body = subject.payload("Ticker,Shares\nAAPL,2\n", price_date="2026-09-21")
    case.service.resolve_prices = lambda *args: quote(10)
    original = case.create(body)
    case.service.resolve_prices = lambda *args: quote(20)
    refresh_body = dict(body, upload_token="review-refresh-one", supersedes_input_id=original["input_id"])
    entry_response = subject.build_upload_entry(case.service).handle({
        "routeKey": subject.ROUTE, "headers": case.headers, "body": json.dumps(refresh_body)})
    refreshed = entry_response["data"]
    upload_row = case.service.index.get(case.owner["firm_id"], "UPLOAD#" + refreshed["upload_id"])
    record("actual_guarded_entry_refresh_preserves_parent_receipt",
           refreshed["portfolio"]["holdings"]["total_dollars"] == "40"
           and original["portfolio"]["holdings"]["total_dollars"] == "20"
           and refreshed["input_id"] != original["input_id"]
           and refreshed["portfolio"]["source"]["supersedes_input_ref"] == original["input_ref"]
           and upload_row["supersedes_input_ref"] == original["input_ref"],
           original=original["input_ref"], refreshed=refreshed["input_ref"],
           original_dollars=original["portfolio"]["holdings"]["total_dollars"],
           refreshed_dollars=refreshed["portfolio"]["holdings"]["total_dollars"])

    def forbidden(*args):
        raise AssertionError("accepted replay attempted dependency refresh")

    case.service = case.new_service()
    case.service.resolve_prices = forbidden
    case.service.resolve_security = forbidden
    case.service.parse_mapping = forbidden
    count = case.s3.put_count
    replay = case.create(refresh_body)
    old_replay = case.create(body)
    record("restart_replays_both_frozen_revisions_without_dependency_calls",
           replay == refreshed and old_replay == original and case.s3.put_count == count,
           refreshed_equal=replay == refreshed, original_equal=old_replay == original,
           additional_blob_puts=case.s3.put_count - count)

    case.service = case.new_service()
    case.service.resolve_prices = lambda *args: quote(30)
    third = case.create(dict(body, upload_token="review-refresh-two", supersedes_input_id=refreshed["input_id"]))
    documents = [case.service.read_input(case.principal, case.owner, row["input_id"])["document"]
                 for row in (original, refreshed, third)]
    totals = [document["holdings"]["total_dollars"] for document in documents]
    record("second_refresh_keeps_immediate_lineage_and_all_prior_values",
           totals == ["20", "40", "60"]
           and third["portfolio"]["source"]["supersedes_input_ref"] == refreshed["input_ref"],
           totals=totals, third_input=third["input_ref"],
           third_parent=third["portfolio"]["source"]["supersedes_input_ref"])

    def read_refresh():
        return case.service.read_input(case.principal, case.owner, refreshed["input_id"])

    parent_key = (case.owner["firm_id"], "INPUT#" + original["input_id"])
    parent_row = copy.deepcopy(case.table.rows[parent_key])
    case.table.rows[parent_key]["content_sha256"] = "0" * 64
    refuses("parent_content_hash_rebound_after_publication", read_refresh,
            subject.UploadRefused, "LINEAGE_BINDING")
    case.table.rows[parent_key] = copy.deepcopy(parent_row)
    case.table.rows[parent_key]["artifact_ref"]["version_id"] = "rebound-version"
    refuses("parent_artifact_receipt_rebound_after_publication", read_refresh,
            subject.UploadRefused, "LINEAGE_BINDING")
    case.table.rows[parent_key] = copy.deepcopy(parent_row)
    case.table.rows[parent_key]["owner"]["principal_id"] = "foreign@example.invalid"
    refuses("parent_owner_changed_after_publication", read_refresh,
            PermissionError, "INPUT_UNAVAILABLE")
    case.table.rows.pop(parent_key)
    refuses("parent_index_missing_after_publication", read_refresh,
            PermissionError, "INPUT_UNAVAILABLE")
    case.table.rows[parent_key] = copy.deepcopy(parent_row)

    real_get = case.service.artifacts.get

    def revoke_after_parent(principal, artifact_id):
        value = real_get(principal, artifact_id)
        if artifact_id == original["input_ref"]["artifact_ref"]["artifact_id"]:
            case.headers["x-user-email"] = "revoked@example.invalid"
        return value

    case.service.artifacts.get = revoke_after_parent
    refuses("access_revoked_after_parent_artifact_read", read_refresh, PermissionError, "")
    case.headers = subject.claims()
    case.service.artifacts.get = real_get
    loaded = read_refresh()
    record("unmodified_parent_restored_positive", loaded["document"] == refreshed["portfolio"],
           same_document=loaded["document"] == refreshed["portfolio"])

    evidence = {"candidate_pin": pin, "source_evidence": str(args.source_evidence),
                "source_evidence_sha256": hashlib.sha256(args.source_evidence.read_bytes()).hexdigest(),
                "verified_snapshot_files": len(source["snapshot_file_sha256"]),
                "controls": controls, "passed": sum(item["passed"] for item in controls),
                "total": len(controls),
                "limits": ["Actual M guarded entry, Y upload/normalization and P repository code",
                           "AWS-shaped conditional/version/Decimal-aware doubles; offline only",
                           "Revocation injected after real local repository read",
                           "Immediate prior receipt controls; no expiry/lifecycle/transitive-retention proof",
                           "No real browser, concurrent server, process crash or integrated acceptance"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    if evidence["passed"] != evidence["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
