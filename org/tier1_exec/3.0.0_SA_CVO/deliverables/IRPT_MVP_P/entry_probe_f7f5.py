"""Pinned actual entry review; real Enforcer/selection with offline dependencies."""
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

PIN = "f7f5d22a76e7e760c3e74f03ff85b85b2372bb47"
PACKAGE = "infra/aws/lambda/investor-reporting"


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix="cvo-p-entry-f7f5-" )).resolve()
    archive = subprocess.check_output([
        "git", "archive", "--format=zip", PIN, PACKAGE,
        "docs/contracts/investor-reporting/v1", "data/firm_registry.json"], cwd=root)
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for member in bundle.infolist():
            target = (snapshot / member.filename).resolve()
            if not target.is_relative_to(snapshot):
                raise ValueError("snapshot path outside temporary root")
            if member.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(bundle.read(member))
    tests = snapshot / PACKAGE / "performance/tests"
    added = here.with_name("entry_independent_cases.py").read_bytes()
    (tests / "test_independent_review.py").write_bytes(added)
    environment = dict(os.environ)
    environment["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    evidence = {}
    for label, name in (("supplied_suite", "test_entry_selection.py"),
                        ("independent_suite", "test_independent_review.py")):
        command = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(tests / name)]
        result = subprocess.run(command, cwd=snapshot, env=environment,
                                capture_output=True, text=True, timeout=90)
        evidence[label] = {"command": command, "exit_code": result.returncode,
                           "stdout": result.stdout, "stderr": result.stderr}
    paths = ["performance/entry.py", "performance/tests/test_entry_selection.py",
             "_authz/served.py", "_authz/enforce.py", "_scope/selection.py", "_scope/selection_store.py"]
    evidence.update({"seat": "3.0.0_SA_CVO~P", "candidate": PIN,
                     "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                     "snapshot": str(snapshot), "git_archive_sha256": hashlib.sha256(archive).hexdigest(),
                     "source_sha256": {name: hashlib.sha256((snapshot / PACKAGE / name).read_bytes()).hexdigest() for name in paths},
                     "reviewer_cases_sha256": hashlib.sha256(added).hexdigest(),
                     "limits": "Actual entry/Enforcer/M resolver. Synthetic storage, provider argument recorder. No deployed zip, browser, real provider, IAM evaluation, report persistence/export, vendor or cloud calls."})
    here.with_suffix(".json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    return 0 if all(evidence[key]["exit_code"] == 0 for key in ("supplied_suite", "independent_suite")) else 1


if __name__ == "__main__":
    raise SystemExit(main())
