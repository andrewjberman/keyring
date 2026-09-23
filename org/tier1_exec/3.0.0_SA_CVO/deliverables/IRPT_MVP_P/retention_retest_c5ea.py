"""Exact-pin R-P07 retest with unchanged original assertions and receipt boundaries."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

PIN = "c5eace08c76176c6d9ebb78dd31ced3b0e57ea2d"
PACKAGE = "infra/aws/lambda/investor-reporting/reports"


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix="cvo-p-retention-c5ea-"))
    registry = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", PIN, "infra/logic/registry"], cwd=root,
        text=True).splitlines()
    sources = [PACKAGE + "/" + name for name in
               ("retention.py", "repository.py", "tests/test_retention.py")]
    sources += ["lib/opal_naming.py", "org/standards/NAMING_SCHEMA.json"] + registry
    hashes = {}
    for source in sources:
        data = subprocess.check_output(["git", "show", PIN + ":" + source], cwd=root)
        target = snapshot / source
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        hashes[source] = hashlib.sha256(data).hexdigest()
    reviewers = {}
    for source, target in (("retention_independent_cases.py", "test_original_review.py"),
                           ("retention_receipt_cases.py", "test_receipt_review.py")):
        data = here.with_name(source).read_bytes()
        (snapshot / PACKAGE / "tests" / target).write_bytes(data)
        reviewers[source] = hashlib.sha256(data).hexdigest()
    environment = dict(os.environ)
    environment["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    evidence = {"seat": "3.0.0_SA_CVO~P", "candidate": PIN, "source_sha256": hashes,
                "reviewer_sha256": reviewers, "snapshot": str(snapshot)}
    for label, name in (("supplied_suite", "test_retention.py"),
                        ("unchanged_independent_suite", "test_original_review.py"),
                        ("receipt_boundary_suite", "test_receipt_review.py")):
        command = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                   str(snapshot / PACKAGE / "tests" / name)]
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, timeout=60)
        evidence[label] = {"command": command, "exit_code": result.returncode,
                           "stdout": result.stdout, "stderr": result.stderr}
    evidence["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    evidence["limits"] = "Pinned modules/accessor/registry. Synthetic server clock, owner, transport and ACTIVE policy; actual boto3 serialization and supplied Stubber. Controlled interleavings, not live concurrency. No lifecycle composition, cleanup, cloud, browser, or full S7 acceptance."
    here.with_suffix(".json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    return int(any(evidence[k]["exit_code"] for k in
                   ("supplied_suite", "unchanged_independent_suite", "receipt_boundary_suite")))


if __name__ == "__main__":
    raise SystemExit(main())
