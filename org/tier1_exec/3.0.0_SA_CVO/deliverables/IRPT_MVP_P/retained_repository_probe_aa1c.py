"""Pinned retained repository composition and unchanged receipt regression checks."""
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

PIN = "aa1cfaea6b063acac5fc974d397d6a278daa17a0"
PACKAGE = "infra/aws/lambda/investor-reporting/reports"


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix="cvo-p-retained-aa1c-"))
    archive = subprocess.check_output(["git", "archive", "--format=zip", PIN, PACKAGE,
        "lib/opal_naming.py", "org/standards/NAMING_SCHEMA.json", "infra/logic/registry",
        "docs/contracts/investor-reporting/v1"], cwd=root)
    hashes = {}
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
    reviewer_hashes = {}
    for source, target in (("retention_independent_cases.py", "test_original_review.py"),
                           ("retention_receipt_cases.py", "test_receipt_review.py"),
                           ("retained_repository_cases.py", "test_composition_review.py")):
        data = here.with_name(source).read_bytes()
        (snapshot / PACKAGE / "tests" / target).write_bytes(data)
        reviewer_hashes[source] = hashlib.sha256(data).hexdigest()
    environment = dict(os.environ)
    environment["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    evidence = {"seat": "3.0.0_SA_CVO~P", "candidate": PIN, "snapshot": str(snapshot),
                "source_sha256": {name: sha for name, sha in hashes.items() if name.startswith(PACKAGE)},
                "reviewer_sha256": reviewer_hashes, "runs": []}
    for label, files in (("supplied", ["test_repository.py", "test_retention.py", "test_retained_repository.py"]),
                         ("unchanged_regressions", ["test_original_review.py", "test_receipt_review.py"]),
                         ("independent_composition", ["test_composition_review.py"])):
        command = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"]
        command += [str(snapshot / PACKAGE / "tests" / name) for name in files]
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, timeout=60)
        evidence["runs"].append({"label": label, "command": command, "exit_code": result.returncode,
                                 "stdout": result.stdout, "stderr": result.stderr})
    evidence["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    evidence["limits"] = "Exact repository/retention/composition modules; synthetic ACTIVE policy/destination/clock/access and serialized/versioned storage doubles. No live services, runtime factories, IAM, disposal or full S7 acceptance."
    here.with_suffix(".json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    return int(any(row["exit_code"] for row in evidence["runs"]))


if __name__ == "__main__":
    raise SystemExit(main())
