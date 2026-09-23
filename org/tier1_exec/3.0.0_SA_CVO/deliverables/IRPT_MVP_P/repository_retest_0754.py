"""Replay the original independent controls without replacing baseline evidence."""
import contextlib
from decimal import Decimal
import importlib.util
import io
import json
from pathlib import Path


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    here = Path(__file__).resolve()
    probe = load("original_review", here.with_name("repository_candidate_probe.py"))
    probe.PIN = "0754b10b6c6407da82021f8e475382634804870d"
    # Original runner writes beside __file__; retain its original JSON untouched.
    probe.__file__ = str(here)
    with contextlib.redirect_stdout(io.StringIO()):
        result = probe.main()
    target = here.with_suffix(".json")
    record = json.loads(target.read_text(encoding="utf-8"))
    tests = load("replacement_tests", Path(record["snapshot"]) / probe.TEST)
    fixture = tests.ArtifactTests()
    fixture.setUp()
    receipt = fixture.put()
    row = next(iter(fixture.table.rows.values()))
    raw = fixture.table.get_item(Key={"tenant": row["tenant"],
                                     "request_revision": row["request_revision"]},
                                 ConsistentRead=True)["Item"]
    assert type(raw["ref"]["byte_length"]) is Decimal
    loaded = fixture.artifacts.get(fixture.principal, receipt["artifact_id"])
    for ref in (receipt, fixture.put(), loaded["ref"],
                fixture.artifacts.head(fixture.principal, receipt["artifact_id"])):
        assert ref == receipt and type(ref["byte_length"]) is int
        assert json.loads(json.dumps(ref)) == receipt
    assert loaded["data"] == b"Ticker,Dollars\nAAPL,100\n"
    assert len(fixture.table.rows) == 1 and fixture.s3.put_count == 1
    record["additional_decimal_control"] = {
        "grade": "PASS", "raw_byte_length_type": "decimal.Decimal",
        "operations": ["initial put", "identical retry", "get", "head"],
        "public_byte_length_type": "int", "same_receipt_and_bytes": True,
        "published_rows": 1, "blob_put_count": 1,
        "limit": "Actual boto3 type roundtrip with synthetic Table/S3; Y retains its own Y-P01 retest verdict."}
    target.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
    return result


if __name__ == "__main__":
    raise SystemExit(main())
