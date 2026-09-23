"""Bounded engineering probe: 12 GET /thesis Lambda requests plus a 401 control.

Uses authorized IAM InvokeFunction access, not a browser/JWT login. The x-firm-id
value matches the repository's engineering test fixture. No producer, refresh,
model, deployment or write route is invoked. Response prose is retained as hashes.
"""

from __future__ import annotations

import ast
import base64
import hashlib
import io
import json
from pathlib import Path
import urllib.request
import zipfile

import boto3
from botocore.config import Config


FUNCTION = "opal-amgt-scoped-api"


def main():
    home = Path(__file__).parent
    census = json.loads((home / "HELD_CENSUS.json").read_bytes())
    if not census["historical_denominator_recovered"] or len(census["objects"]) != 12:
        raise ValueError("the exact historical population must be recovered first")
    client = boto3.client("lambda", region_name="us-east-1", config=Config(
        retries={"total_max_attempts": 1}, connect_timeout=5, read_timeout=60,
    ))
    info = client.get_function(FunctionName=FUNCTION)
    raw = urllib.request.urlopen(info["Code"]["Location"], timeout=30).read()
    expected = info["Configuration"]["CodeSha256"]
    if base64.b64encode(hashlib.sha256(raw).digest()).decode() != expected:
        raise ValueError("downloaded deployed package hash mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        api = archive.read("lib/research/api/scoped_amgt.py")
        schema = archive.read("lib/research/drafting/schema.json")
        pipeline = archive.read("lib/research/drafting/pipeline.py")
    tree = ast.parse(api)
    functions = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in (
            "_validate_drafting_document", "read_drafted_sections", "read_thesis_bundle",
        ):
            functions[node.name] = {
                "start_line": node.lineno, "end_line": node.end_lineno,
                "calls": sorted({ast.unparse(n.func) for n in ast.walk(node) if isinstance(n, ast.Call)}),
                "source": ast.get_source_segment(api.decode(), node),
            }
    if len(functions) != 3:
        raise ValueError("expected all three serving functions in deployed artifact")
    result = {
        "evidence_level": "actual deployed Lambda GET engineering probe; not authenticated browser",
        "function": FUNCTION, "code_sha256_base64": expected,
        "last_modified": info["Configuration"]["LastModified"],
        "deployed_api_sha256": hashlib.sha256(api).hexdigest(),
        "deployed_schema_sha256": hashlib.sha256(schema).hexdigest(),
        "deployed_pipeline_sha256": hashlib.sha256(pipeline).hexdigest(),
        "source_functions": functions, "cases": [],
    }

    def invoke(security, authenticated):
        event = {
            "rawPath": f"/api/scoped/amgt/security/{security}/thesis",
            "headers": {"x-firm-id": "bd"} if authenticated else {},
            "requestContext": {"http": {"method": "GET"}},
        }
        response = client.invoke(FunctionName=FUNCTION, InvocationType="RequestResponse",
                                 Payload=json.dumps(event).encode())
        payload = response["Payload"].read()
        parsed = json.loads(payload)
        return response, parsed, hashlib.sha256(payload).hexdigest()

    _, control, control_hash = invoke(census["objects"][0]["security_key"], False)
    result["no_firm_header_control"] = {"statusCode": control.get("statusCode"), "response_sha256": control_hash}
    if control.get("statusCode") != 401:
        raise ValueError("missing-firm negative control did not refuse with 401")
    for obj in census["objects"]:
        security = obj["security_key"]
        response, parsed, digest = invoke(security, True)
        body = json.loads(parsed.get("body", "{}"))
        sections = body.get("drafted_sections", [])
        sentences = [s for section in sections for s in section.get("sentences", [])]
        unanchored = [s for s in sentences if not s.get("quoted_spans")]
        hashes = [hashlib.sha256((s.get("text") or "").encode()).hexdigest() for s in unanchored]
        historical_hashes = [case["text_sha256"] for case in obj["cases"]]
        row = {
            "security_key": security, "statusCode": parsed.get("statusCode"),
            "function_error": response.get("FunctionError"), "executed_version": response.get("ExecutedVersion"),
            "response_sha256": digest, "drafting_status": body.get("drafting_status"),
            "drafting_source": body.get("drafting_source"), "served_sentences": len(sentences),
            "served_no_span": len(unanchored), "no_span_text_hashes": hashes,
            "exact_historical_no_span_texts": sorted(hashes) == sorted(historical_hashes),
        }
        result["cases"].append(row)
        print(security, row["statusCode"], row["drafting_status"], len(sentences), len(unanchored), flush=True)
    after = client.get_function_configuration(FunctionName=FUNCTION)
    result["package_unchanged_through_probe"] = after["CodeSha256"] == expected
    result["documents_requested"] = len(result["cases"])
    result["documents_with_served_no_span"] = sum(row["served_no_span"] > 0 for row in result["cases"])
    result["served_sentences"] = sum(row["served_sentences"] for row in result["cases"])
    result["served_no_span"] = sum(row["served_no_span"] for row in result["cases"])
    result["historical_text_sets_matched"] = sum(row["exact_historical_no_span_texts"] for row in result["cases"])
    (home / "SERVED_CENSUS.json").write_bytes((json.dumps(result, indent=2) + "\n").encode())
    print(json.dumps({k: v for k, v in result.items() if k not in ("cases", "source_functions")}, indent=2))


if __name__ == "__main__":
    main()
