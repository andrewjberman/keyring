"""Pinned offline retention review; exact module and declared AWS test boundary."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

PIN = "bd7c9f1b2c23737566f90a519634f904ff89f201"
PACKAGE = "infra/aws/lambda/investor-reporting/reports"


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    snapshot = Path(tempfile.mkdtemp(prefix="cvo-p-retention-bd7c-"))
    hashes = {}
    for name in ("retention.py", "repository.py", "tests/test_retention.py"):
        source = PACKAGE + "/" + name
        data = subprocess.check_output(["git", "show", PIN + ":" + source], cwd=root)
        target = snapshot / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        hashes[source] = hashlib.sha256(data).hexdigest()
    reviewer = here.with_name("retention_independent_cases.py").read_bytes()
    (snapshot / "tests/test_independent_review.py").write_bytes(reviewer)
    environment = dict(os.environ)
    environment["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    evidence = {"seat": "3.0.0_SA_CVO~P", "candidate": PIN, "source_sha256": hashes,
                "reviewer_sha256": hashlib.sha256(reviewer).hexdigest(), "snapshot": str(snapshot)}
    for label, name in (("supplied_suite", "test_retention.py"),
                        ("independent_suite", "test_independent_review.py")):
        command = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(snapshot / "tests" / name)]
        result = subprocess.run(command, cwd=snapshot, env=environment, capture_output=True,
                                text=True, timeout=60)
        evidence[label] = {"command": command, "exit_code": result.returncode,
                           "stdout": result.stdout, "stderr": result.stderr}
    evidence["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    evidence["limits"] = "Exact retention/repository modules; synthetic policy/owner/clock/transport and actual boto3 serialization/Stubber. No repository lifecycle composition, concurrent workers, physical cleanup, live AWS or vendor execution."
    here.with_suffix(".json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    return 0 if all(evidence[k]["exit_code"] == 0 for k in ("supplied_suite", "independent_suite")) else 1


if __name__ == "__main__":
    raise SystemExit(main())
