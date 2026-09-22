"""Independent canonical-security normalization controls through retained uploads."""
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


def local(identifier, namespace):
    return {"security_key": "local-key-" + identifier,
            "canonical_identifier": identifier,
            "canonical_identifier_namespace": namespace,
            "resolution_revision": "independent-local-dimension-1"}


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
    spec = importlib.util.spec_from_file_location("local_identity_subject",
        code_root / "intake/tests/test_retained_uploads.py")
    subject = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subject)
    controls = []

    def world():
        w = subject.world.__wrapped__(subject.test_retention.world.__wrapped__())
        w.case.service.resolve_security = local
        return w

    def record(name, passed, **observed):
        controls.append({"name": name, "passed": bool(passed), "observed": observed})

    def no_vendor_id(document):
        return all("security_id" not in row for row in document["rows"] + document["holdings"]["rows"])

    w = world()
    body = subject.upload_tests.payload("Ticker,Market Value,Currency\nAAPL,9007199254740993.01,USD\n"
        "AAPL,0.10,USD\nAAPL,0.20,USD\n$:CASH,1.00,USD\n")
    result = w.case.create(body)
    doc = result["portfolio"]
    read = w.case.service.read_input(w.case.principal, w.case.owner, result["input_id"])
    record("local_duplicate_cash_large_cents_persist_and_read_exactly",
           result["state"] == "NORMALIZED" and doc["holdings"]["total_dollars"] == "9007199254740994.31"
           and len(doc["rows"]) == 4 and len(doc["holdings"]["rows"]) == 2
           and no_vendor_id(doc) and doc["holdings"]["identity_kind"] == "CANONICAL_SECURITY"
           and read["document"] == doc,
           holdings=doc["holdings"], source_rows=doc["rows"], input_ref=result["input_ref"],
           read_equal=read["document"] == doc)

    def forbidden(*args):
        raise AssertionError("unchanged local upload retry resolved current input")

    w.case.service.resolve_security = forbidden
    puts = w.case.s3.put_count
    retry = w.case.create(body)
    record("retained_local_retry_avoids_current_resolution", retry == result and w.case.s3.put_count == puts,
           same_result=retry == result, additional_blob_puts=w.case.s3.put_count - puts)

    w = world()
    w.case.service.resolve_security = lambda identifier, namespace: local("BRK.B", "TICKER")
    result = w.case.create(subject.upload_tests.payload(
        "Ticker,Market Value,Currency\nBRK.B,0.10,USD\nBRK-B,0.20,USD\n"))
    doc = result["portfolio"]
    record("two_source_aliases_same_canonical_identity_consolidate",
           doc["holdings"]["total_dollars"] == "0.30" and len(doc["holdings"]["rows"]) == 1
           and len(doc["rows"]) == 2 and no_vendor_id(doc),
           holdings=doc["holdings"], original_identifiers=[row["original"]["identifier"] for row in doc["rows"]])

    w = world()
    quote = {"security_key": "local-key-AAPL", "price": "12.35", "currency": "USD",
             "as_of": "2026-09-21", "source_revision": "independent-local-price-1"}
    w.case.service.resolve_prices = lambda *args: {"local-key-AAPL": quote}
    result = w.case.create(subject.upload_tests.payload("Ticker,Shares\nAAPL,2\n", price_date="2026-09-21"))
    doc = result["portfolio"]
    record("local_shares_use_exact_key_date_and_decimal_price",
           doc["holdings"]["total_dollars"] == "24.70" and no_vendor_id(doc)
           and doc["rows"][0]["price"]["security_key"] == "local-key-AAPL",
           holdings=doc["holdings"], price=doc["rows"][0]["price"])

    w = world()
    result = w.case.create(subject.upload_tests.payload(
        "Ticker,Weight\nAAPL,25%\nMSFT,75%\n", reference_notional="100.01"))
    doc = result["portfolio"]
    record("local_weights_preserve_explicit_notional_basis",
           doc["holdings"]["total_dollars"] == "100.0100" and no_vendor_id(doc)
           and doc["valuation_basis"] == "REFERENCE_NOTIONAL" and doc["reference_notional"] == "100.01",
           holdings=doc["holdings"], basis=doc["valuation_basis"], notional=doc["reference_notional"])

    failures = [
        ("same_alias_different_keys", "AMBIGUOUS_SECURITY_RESOLUTION",
         lambda identifier, namespace: dict(local("AAPL", "TICKER"), security_key="key-" + identifier)),
        ("same_key_different_identity", "AMBIGUOUS_SECURITY_RESOLUTION",
         lambda identifier, namespace: dict(local(identifier, namespace), security_key="shared-key")),
        ("mixed_local_and_vendor_rows", "MIXED_SECURITY_IDENTITY",
         lambda identifier, namespace: local(identifier, namespace) if identifier == "AAPL"
         else {"security_id": "S:MSFT", "resolution_revision": "legacy-fixture"}),
        ("cash_namespace_noncanonical_token", "CANONICAL_CASH_INVALID",
         lambda identifier, namespace: local("CASH", "CASH")),
    ]
    for name, reason, resolver in failures:
        w = world()
        w.case.service.resolve_security = resolver
        result = w.case.create(subject.upload_tests.payload(
            "Ticker,Market Value,Currency\nAAPL,10,USD\nMSFT,20,USD\n"))
        input_count = sum(key[1].startswith("INPUT#") for key in w.table.rows)
        record(name + "_holds_whole_input",
               result["state"] == "NEEDS_CORRECTION" and result["input_id"] is None
               and result["reason"] == reason and input_count == 0 and w.case.s3.put_count == 1,
               response=result, input_rows=input_count, blob_puts=w.case.s3.put_count)
    w = world()
    w.case.service.resolve_prices = lambda *args: {"local-key-AAPL": dict(quote, security_key="other-key")}
    result = w.case.create(subject.upload_tests.payload("Ticker,Shares\nAAPL,2\n", price_date="2026-09-21"))
    input_count = sum(key[1].startswith("INPUT#") for key in w.table.rows)
    record("wrong_local_price_key_holds_whole_input",
           result["state"] == "NEEDS_CORRECTION" and result["reason"] == "PRICE_INCOMPATIBLE"
           and input_count == 0 and w.case.s3.put_count == 1,
           response=result, input_rows=input_count, blob_puts=w.case.s3.put_count)

    paths = ["intake/tests/test_portfolio.py", "intake/tests/test_uploads.py",
             "intake/tests/test_retained_uploads.py"]
    suite_code = ("import socket,pytest; "
        "deny=lambda *a,**k: (_ for _ in ()).throw(AssertionError('NETWORK_FORBIDDEN')); "
        "socket.socket.connect=deny; socket.socket.connect_ex=deny; socket.create_connection=deny; "
        "raise SystemExit(pytest.main(" + repr(["-q"] + [str(code_root / p) for p in paths]) + "))")
    suite = subprocess.run([sys.executable, "-c", suite_code], cwd=snapshot,
                           capture_output=True, text=True, check=False)
    evidence = {"candidate_pin": pin, "source_evidence": str(args.source_evidence),
                "source_evidence_sha256": hashlib.sha256(args.source_evidence.read_bytes()).hexdigest(),
                "verified_snapshot_files": len(source["snapshot_file_sha256"]),
                "supplied_targeted_suite": {"exit_code": suite.returncode, "stdout": suite.stdout, "stderr": suite.stderr},
                "controls": controls, "passed": sum(row["passed"] for row in controls), "total": len(controls),
                "limits": ["Actual CSV parser/Y upload/local normalization/P retained repository code",
                           "Canonical resolver and prices are explicit local fixtures, not actual M source",
                           "Legacy S-prefixed supplied fixture tests are not runtime resolution evidence",
                           "Storage/clock/policy fixtures only; no activation, vendor lookup/upload/readback/create",
                           "Shared schema suite reported by producer not independently rerun here",
                           "No browser/runtime, real server concurrency or full Y2/S2/S3/S7 acceptance"]}
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_pin": pin, "suite": evidence["supplied_targeted_suite"],
                      "passed": evidence["passed"], "total": evidence["total"],
                      "controls": [{"name": c["name"], "passed": c["passed"]} for c in controls]}, indent=2))
    if evidence["passed"] != evidence["total"] or suite.returncode:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
