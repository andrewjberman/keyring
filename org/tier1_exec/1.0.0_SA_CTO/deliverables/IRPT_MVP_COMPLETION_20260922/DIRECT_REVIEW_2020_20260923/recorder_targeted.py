"""Two focused recorder regression cases on exact source, no live services."""
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import zipfile

PIN = "0b8784cea8e61c3f06b5aa8f5f77a0c1c47fa1e4"
PREFIX = "infra/aws/lambda/ci/"
FILES = ["record-terraform-deploy.sh", "record-deploy-scope.py",
         "test_record_terraform_deploy_scope.py"]
root = Path(tempfile.mkdtemp(prefix="irpt-cto-recorder-repair-"))
archive = subprocess.check_output(["git", "archive", "--format=zip", PIN]
                                  + [PREFIX + f for f in FILES])
zipfile.ZipFile(io.BytesIO(archive)).extractall(root)
spec = importlib.util.spec_from_file_location("fixture", root / PREFIX / FILES[2])
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)
source = (root / PREFIX / FILES[0]).read_text(encoding="utf-8")
results = []
for label, ref, args, expected, changed in [
    ("unchanged_single", "HEAD", ["--function", fixture.TARGET], [fixture.TARGET], []),
    ("mixed_all", "HEAD~2", ["--all"], fixture.ALL_FNS, [fixture.TARGET]),
]:
    case = root / label
    case.mkdir()
    ws = fixture.build_fixture(str(case), source)
    fixture.seed_changelog_at(ws, ref)
    result = fixture.run_recorder(ws, args)
    row = {k: result[k] for k in ["rc", "stamped", "changelog_functions",
           "changelog_artifacts", "reconcile_functions", "changelog_source_changes", "aws_called"]}
    row["case"] = label
    print(json.dumps(row))
    assert row["rc"] == 0 and not row["aws_called"]
    for key in ["stamped", "changelog_functions", "changelog_artifacts", "reconcile_functions"]:
        assert sorted(row[key]) == sorted(expected), (label, key, row)
    assert row["changelog_source_changes"] == changed
    results.append(row)
Path(__file__).with_name("recorder-results.json").write_text(
    json.dumps({"pin": PIN, "results": results, "limits": "offline bun branch; no plan E2E or live acceptance"}, indent=2), encoding="utf-8")
print("PASS: two targeted recorder cases; every consumer reached")
