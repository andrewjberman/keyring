"""Exercise the pinned real recorder in its existing offline throwaway fixture."""
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import zipfile

PIN = "0116b83bc0"
FILES = ["record-terraform-deploy.sh", "record-deploy-scope.py",
         "test_record_terraform_deploy_scope.py"]
PREFIX = "infra/aws/lambda/ci/"


def main():
    root = Path(tempfile.mkdtemp(prefix="irpt-cto-recorder-probe-"))
    archive = subprocess.check_output(
        ["git", "archive", "--format=zip", PIN] + [PREFIX + f for f in FILES])
    zipfile.ZipFile(io.BytesIO(archive)).extractall(root)
    test_path = root / PREFIX / FILES[2]
    spec = importlib.util.spec_from_file_location("recorder_fixture", test_path)
    fixture = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixture)
    script = (root / PREFIX / FILES[0]).read_text(encoding="utf-8")
    workspace = fixture.build_fixture(str(root), script)
    changelog = Path(workspace) / "infra/aws/terraform/investor-reporting/CHANGELOG.json"
    data = json.loads(changelog.read_text(encoding="utf-8"))
    data["entries"][0]["deployed_commit"] = fixture._git(workspace, "rev-parse", "HEAD")
    changelog.write_text(json.dumps(data), encoding="utf-8")
    result = fixture.run_recorder(workspace, ["--function", fixture.TARGET])
    observed = {k: result[k] for k in (
        "rc", "stamped", "changelog_functions", "changelog_artifacts",
        "reconcile_functions", "aws_called")}
    print(json.dumps(observed, indent=2))
    assert observed["stamped"] == [fixture.TARGET]
    assert observed["changelog_artifacts"] == [fixture.TARGET]
    assert observed["changelog_functions"] == []
    assert observed["reconcile_functions"] is None
    assert observed["rc"] == 0 and not observed["aws_called"]
    print("REPRODUCED: deployed target omitted from functions/reconcile; fixture:", workspace)


if __name__ == "__main__":
    main()
