"""Pinned actual guarded upload producer to browser parser, no deployed route."""
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

BACKEND = "5add22ca9fb36545d4ed0b857e17217644d10c98"
PORTAL = "cb62721c6095c0d51e1e4ec52be9c44a88002a48"
PACKAGE = "infra/aws/lambda/investor-reporting"
CAPTURE = '''import json, sys
from pathlib import Path
root = Path.cwd()
sys.path.insert(0, str(root / "infra/aws/lambda/investor-reporting/_contracts"))
import test_upload_contract as contract
result = {}
for label, csv in (("normalized", None), ("correction", "Ticker,Dollars\\nAAPL,10\\n")):
    case = contract.test_uploads.UploadIntegrationTests()
    case.setUp()
    request = contract.test_uploads.payload() if csv is None else contract.test_uploads.payload(csv)
    response = contract.test_uploads.build_upload_entry(case.service).handle(
        {"routeKey": contract.test_uploads.ROUTE, "headers": case.headers, "body": json.dumps(request)})
    contract.validator("AnalysisUploadRequest.schema.json").validate(request)
    contract.validator("responses/analysis-input-upload.response.schema.json").validate(response)
    result[label] = {"request": request, "response": response}
from portfolio import canonical_bytes
import hashlib
data = result["normalized"]["response"]["data"]
sha = hashlib.sha256(canonical_bytes(data["portfolio"])).hexdigest()
assert data["input_id"] == "portfolio_" + sha
assert data["input_ref"]["content_sha256"] == data["input_ref"]["artifact_ref"]["sha256"] == sha
(root / "actual-upload.json").write_text(json.dumps(result, indent=2) + "\\n", encoding="utf-8")
print(json.dumps({"states": [result[k]["response"]["data"]["state"] for k in result], "input_sha256":sha}))
'''


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    portal = root / "portal"
    snapshot = Path(tempfile.mkdtemp(prefix="cvo-p-upload-cb62-"))
    hashes = {}
    backend_paths = [PACKAGE + "/" + name for name in ("intake", "reports", "_authz", "_scope", "_ids", "_keys", "_contracts")]
    backend_paths += ["docs/contracts/investor-reporting/v1", "data/firm_registry.json"]
    for repo, pin, paths in ((root, BACKEND, backend_paths), (portal, PORTAL, ["src", "package.json"])):
        archive = subprocess.check_output(["git", "archive", "--format=zip", pin, *paths], cwd=repo)
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            for name in bundle.namelist():
                target = (snapshot / name).resolve()
                assert target.is_relative_to(snapshot.resolve())
                if name.endswith("/"):
                    continue
                data = bundle.read(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                hashes[name] = hashlib.sha256(data).hexdigest()
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    f"New-Item -ItemType Junction -Path '{snapshot / 'node_modules'}' -Target '{portal / 'node_modules'}' | Out-Null"], check=True)
    independent = here.with_name("upload_receipt_cases.test.ts").read_bytes()
    (snapshot / "reviewer-upload.test.ts").write_bytes(independent)
    (snapshot / "capture.py").write_text(CAPTURE, encoding="utf-8")
    environment = dict(os.environ)
    environment.update(PYTEST_DISABLE_PLUGIN_AUTOLOAD="1", IRPT_CONTRACTS_DIR=str(snapshot / "docs/contracts/investor-reporting/v1"))
    evidence = {"seat": "3.0.0_SA_CVO~P", "backend_pin": BACKEND, "portal_pin": PORTAL,
                "snapshot": str(snapshot), "independent_sha256": hashlib.sha256(independent).hexdigest(), "runs": []}

    def run(label, command):
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, encoding="utf-8", errors="replace", timeout=60)
        evidence["runs"].append({"label": label, "command": command, "exit_code": result.returncode,
                                 "stdout": result.stdout, "stderr": result.stderr})
        return result.returncode

    run("actual-producer-schema", [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", PACKAGE + "/_contracts/test_upload_contract.py"])
    captured = run("independent-producer-capture", [sys.executable, "capture.py"]) == 0
    run("supplied-browser", ["bun", "test", "src/pages/InvestorReporting/__tests__/mvp-upload/upload.test.ts",
        "src/pages/InvestorReporting/__tests__/mvp-selection/selection.test.ts",
        "src/pages/InvestorReporting/__tests__/mvp-selection/coverage.test.ts",
        "src/pages/InvestorReporting/__tests__/fe-s-9/resolve.test.ts"])
    if captured:
        raw = (snapshot / "actual-upload.json").read_bytes()
        here.with_name("upload_actual_5add.json").write_bytes(raw)
        evidence["actual_capture_sha256"] = hashlib.sha256(raw).hexdigest()
        run("independent-browser", ["bun", "test", "reviewer-upload.test.ts"])
    evidence["source_sha256"] = {name: sha for name, sha in hashes.items() if name in [
        PACKAGE + "/intake/portfolio.py", PACKAGE + "/intake/uploads.py", PACKAGE + "/intake/upload_entry.py",
        "src/api/endpoints/investor-reporting.ts", "src/pages/InvestorReporting/contracts/envelope.ts"] or
        "AnalysisUpload" in name or name.endswith("analysis-input-upload.response.schema.json") or name.endswith("v1/routes.json")}
    evidence["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    evidence["limits"] = "Actual guarded producer with supplied owner/storage doubles and schema; actual browser parser with regenerated responses. Route unavailable; no live transport, mounted upload UI, retained runtime, queue, provider or full S7 proof."
    here.with_suffix(".json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    return int(any(row["exit_code"] for row in evidence["runs"]))


if __name__ == "__main__":
    raise SystemExit(main())
