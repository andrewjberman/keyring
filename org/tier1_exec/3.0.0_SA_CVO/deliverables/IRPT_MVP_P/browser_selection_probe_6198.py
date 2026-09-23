"""Pinned shared client/parser review, without mounted or live browser claims."""
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import zipfile

PORTAL_PIN = "61983ce9b7515d93ff391a94c68a6c6da23cfc10"
BACKEND_PIN = "c5eace08c76176c6d9ebb78dd31ced3b0e57ea2d"


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    portal = root / "portal"
    scratch = Path(tempfile.mkdtemp(prefix="cvo-p-browser-6198-"))
    hashes = {}
    for repo, pin, members in ((portal, PORTAL_PIN, ["src", "package.json"]),
                               (root, BACKEND_PIN, ["docs/contracts/investor-reporting/v1"])):
        data = subprocess.check_output(["git", "archive", "--format=zip", pin, *members], cwd=repo)
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            for name in archive.namelist():
                target = (scratch / name).resolve()
                assert target.is_relative_to(scratch.resolve())
                if name.endswith("/"):
                    continue
                content = archive.read(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
                hashes[name] = hashlib.sha256(content).hexdigest()
    junction = scratch / "node_modules"
    target = portal / "node_modules"
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    f"New-Item -ItemType Junction -Path '{junction}' -Target '{target}' | Out-Null"], check=True)
    independent = here.with_name("browser_selection_cases.test.ts").read_bytes()
    (scratch / "reviewer_selection.test.ts").write_bytes(independent)
    environment = dict(os.environ)
    environment["IRPT_CONTRACTS_DIR"] = str(scratch / "docs/contracts/investor-reporting/v1")
    evidence = {"seat": "3.0.0_SA_CVO~P", "portal_pin": PORTAL_PIN, "backend_pin": BACKEND_PIN,
                "snapshot": str(scratch), "bun_version": subprocess.check_output(["bun", "--version"], text=True).strip(),
                "independent_sha256": hashlib.sha256(independent).hexdigest(),
                "dependency_source": str(target), "runs": []}
    for label, path in (("supplied", "src/pages/InvestorReporting/__tests__/mvp-selection/selection.test.ts"),
                        ("independent", "reviewer_selection.test.ts")):
        command = ["bun", "test", path]
        run = subprocess.run(command, cwd=scratch, env=environment, capture_output=True,
                             text=True, encoding="utf-8", errors="replace", timeout=60)
        evidence["runs"].append({"label": label, "command": command, "exit_code": run.returncode,
                                 "stdout": run.stdout, "stderr": run.stderr})
    changed = subprocess.check_output(["git", "diff-tree", "--no-commit-id", "--name-only", "-r", PORTAL_PIN], cwd=portal, text=True).splitlines()
    evidence["changed_source_sha256"] = {name: hashes[name] for name in changed}
    evidence["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    evidence["limits"] = "Pinned client/parser and backend contract bytes; supplied captured producer fixture not independently regenerated. Synthetic transport; no mounted browser, HTTP guard composition, live routing, auth, provider, cache or deployment acceptance. Local existing dependencies, no installs."
    here.with_suffix(".json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    return int(any(run["exit_code"] for run in evidence["runs"]))


if __name__ == "__main__":
    raise SystemExit(main())
