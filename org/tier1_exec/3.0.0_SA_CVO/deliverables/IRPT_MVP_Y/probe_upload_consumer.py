"""Pinned offline upload consumer review; actual M/Y/P modules, synthetic storage."""
import argparse
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import unittest
import zipfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", default="bf50e40359358d301d99278784afedeec8a50559")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[5]
    pin = subprocess.check_output(["git", "rev-parse", "--verify", args.pin + "^{commit}"],
                                  cwd=root, text=True).strip()
    snapshot = root / ".runtime/codex-seats/3.0.0_SA_CVO~Y/upload-review" / pin
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
                raise ValueError("snapshot path escape")
            if member.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
                continue
            data = bundle.read(member)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            hashes[member.filename] = hashlib.sha256(data).hexdigest()
    os.environ["IRPT_FIRM_REGISTRY"] = str(snapshot / "data/firm_registry.json")
    path = snapshot / "infra/aws/lambda/investor-reporting/intake/tests/test_uploads.py"
    spec = importlib.util.spec_from_file_location("upload_review_tests", path)
    tests = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tests)
    log = io.StringIO()
    result = unittest.TextTestRunner(stream=log, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromModule(tests))
    case = tests.UploadIntegrationTests()
    case.setUp()
    browser = tests.payload()
    first = case.create(browser)
    old_resolver = case.service.resolve_security

    def revised_resolver(identifier, namespace):
        resolved = old_resolver(identifier, namespace)
        return dict(resolved, resolution_revision="offline-catalog-v2") if resolved else None

    case.service = case.new_service()  # Same durable doubles, new service instance.
    case.service.resolve_security = revised_resolver
    retry = case.create(browser)
    original_read = case.service.read_input(case.principal, case.owner, first["input_id"])
    retry_control = {
        "browser_payload_unchanged": True,
        "changed_dependency": "security resolution_revision only, v1 to v2",
        "first_upload_id": first["upload_id"], "retry_upload_id": retry["upload_id"],
        "first_input_id": first["input_id"], "retry_input_id": retry["input_id"],
        "same_input_id": first["input_id"] == retry["input_id"],
        "same_holdings": first["portfolio"]["holdings"] == retry["portfolio"]["holdings"],
        "first_input_still_retrievable": original_read["document"] == first["portfolio"],
        "blob_puts": case.s3.put_count,
        "input_rows": sum(key.startswith("INPUT#") for _, key in case.table.rows),
    }
    # Positive control: an explicit valuation correction must remain separately frozen.
    correction = tests.UploadIntegrationTests()
    correction.setUp()
    weight_body = tests.payload("Ticker,Weight\nAAPL,100%\n", reference_notional="100")
    before = correction.create(weight_body)
    after = correction.create(dict(weight_body, reference_notional="200"))
    correction_control = {
        "same_upload_id": before["upload_id"] == after["upload_id"],
        "different_input_id": before["input_id"] != after["input_id"],
        "before_dollars": before["portfolio"]["holdings"]["total_dollars"],
        "after_dollars": after["portfolio"]["holdings"]["total_dollars"],
        "old_input_retrievable": correction.service.read_input(
            correction.principal, correction.owner, before["input_id"])["document"] == before["portfolio"],
    }
    shares = tests.UploadIntegrationTests()
    shares.setUp()
    shares_body = tests.payload("Ticker,Shares\nAAPL,2\n", price_date="2026-09-21")
    quote = {"security_id": "S:AAPL", "price": "10", "currency": "USD",
             "as_of": "2026-09-21", "source_revision": "price-v1"}
    shares.service.resolve_prices = lambda *args: {"S:AAPL": quote}
    shares_first = shares.create(shares_body)
    shares.service = shares.new_service()
    shares.service.resolve_prices = lambda *args: {
        "S:AAPL": dict(quote, price="20", source_revision="price-v2")}
    shares_retry = shares.create(shares_body)
    price_control = {"browser_payload_unchanged": True,
                     "price_date_unchanged": shares_body["price_date"],
                     "first_dollars": shares_first["portfolio"]["holdings"]["total_dollars"],
                     "retry_dollars": shares_retry["portfolio"]["holdings"]["total_dollars"],
                     "same_upload_id": shares_first["upload_id"] == shares_retry["upload_id"],
                     "same_input_id": shares_first["input_id"] == shares_retry["input_id"],
                     "first_input_still_retrievable": shares.service.read_input(
                         shares.principal, shares.owner, shares_first["input_id"])["document"]
                         == shares_first["portfolio"]}
    evidence = {"candidate_pin": pin, "snapshot_file_sha256": hashes,
                "supplied_suite": {"tests_run": result.testsRun, "failures": len(result.failures),
                                   "errors": len(result.errors), "skipped": len(result.skipped),
                                   "passed": result.wasSuccessful(), "log": log.getvalue()},
                "same_request_dependency_change": retry_control,
                "explicit_correction_control": correction_control,
                "same_request_price_change": price_control,
                "limits": ["Actual M owner/Entry, Y upload/parser/normalizer, P repository modules",
                           "Conditional/version/Decimal-aware storage doubles; no live AWS",
                           "Guarded analysis acceptance remains Mock in supplied suite",
                           "No runtime factory, browser, worker, retention or full E2E proof"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in evidence.items() if k != "snapshot_file_sha256"}, indent=2))


if __name__ == "__main__":
    main()
