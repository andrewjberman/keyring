"""Independent pinned source-map equality, member hashes and flat-entry evidence."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

PIN = "051054cd3e52539ba6461b5359ec24d9431665d2"
BEFORE = "63c6b39af6574fda5e4ad6573258e188ddd21569"
MAP = "infra/aws/lambda/ci/lambda-source-map.json"
HELPER = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/verify_selection_packages.py"
CLOSURE = "infra/aws/lambda/ci/import-closure-check.py"
CONSUMERS = ["irpt-directory-search", "irpt-performance-adapter"]


def main():
    here = Path(__file__).resolve()
    root = here.parents[5]
    scratch = Path(tempfile.mkdtemp(prefix="cvo-p-package-0510-")).resolve()

    def blob(pin, path):
        return subprocess.check_output(["git", "show", pin + ":" + path], cwd=root)

    before_bytes, after_bytes = blob(BEFORE, MAP), blob(PIN, MAP)
    before, after = json.loads(before_bytes), json.loads(after_bytes)
    changed = sorted(name for name in set(before["functions"]) | set(after["functions"])
                     if before["functions"].get(name) != after["functions"].get(name))
    assert changed == CONSUMERS
    assert set(before["functions"]) == set(after["functions"])
    assert {k: v for k, v in before.items() if k != "functions"} == {
        k: v for k, v in after.items() if k != "functions"}
    for name in changed:
        old, new = before["functions"][name], after["functions"][name]
        assert all(old.get(key) == new.get(key) for key in set(old) | set(new)
                   if key not in {"files", "staged_from", "_staged_from_note", "_build_note"})
    helper_path = scratch / "supplied_verifier.py"
    helper_path.write_bytes(blob(PIN, HELPER))
    spec = importlib.util.spec_from_file_location("supplied_package_verifier", helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    closure = scratch / "import-closure-check.py"
    closure.write_bytes(blob(PIN, CLOSURE))
    environment = {k: v for k, v in os.environ.items() if not k.startswith("IRPT_") and k != "PYTHONPATH"}
    environment["AWS_EC2_METADATA_DISABLED"] = "true"
    evidence = {"seat": "3.0.0_SA_CVO~P", "candidate": PIN, "before": BEFORE,
                "changed_functions": changed, "total_functions": len(after["functions"]),
                "unchanged_non_irpt_count": sum(not name.startswith("irpt-") for name in after["functions"]),
                "all_other_function_objects_equal": True, "root_metadata_equal": True,
                "changed_function_noncomposition_metadata_equal": True,
                "map_before_sha256": hashlib.sha256(before_bytes).hexdigest(),
                "map_after_sha256": hashlib.sha256(after_bytes).hexdigest(),
                "canonical_closure_sha256": hashlib.sha256(closure.read_bytes()).hexdigest(),
                "supplied_probe_sha256": hashlib.sha256(helper_path.read_bytes()).hexdigest(),
                "members": {}, "runs": []}

    def run(label, argv, cwd):
        result = subprocess.run(argv, cwd=cwd, env=environment, capture_output=True,
                                text=True, encoding="utf-8", errors="replace", timeout=60)
        evidence["runs"].append({"label": label, "argv": argv, "exit_code": result.returncode,
                                 "stdout": result.stdout, "stderr": result.stderr})
        return result

    outcomes = []
    exchange = scratch / "synthetic-retained-selection.json"
    for name in CONSUMERS:
        item = after["functions"][name]
        flat = scratch / name
        flat.mkdir()
        stage = {row["packaged_as"]: row for row in item["staged_from"]}
        assert len(stage) == len(item["staged_from"])
        assert set(stage) <= set(item["files"]) and len(set(item["files"])) == len(item["files"])
        evidence["members"][name] = []
        for member in item["files"]:
            target = (flat / member).resolve()
            assert target.is_relative_to(flat.resolve())
            row = stage.get(member)
            source = row["repo_path"] if row else item["source_dir"] + "/" + member
            pin = row["pin"] if row else PIN
            data = blob(pin, source)
            digest = hashlib.sha256(data).hexdigest()
            if row:
                assert digest == row["sha256"]
            else:
                assert data == blob(BEFORE, source), source
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            evidence["members"][name].append({"member": member, "pin": pin, "source": source, "sha256": digest})
        result = run(name + ":canonical-closure", [sys.executable, str(closure), str(flat), *item["files"]], flat)
        outcomes.append(result.returncode == 0 and "OK: import-closure" in result.stdout)
        result = run(name + ":supplied-flat-probe", [sys.executable, "-I", "-c", helper.PROBE, str(flat), name], flat)
        outcomes.append(result.returncode == 0)
        result = run(name + ":independent-entry", [sys.executable, "-I", str(here.with_name("package_entry_cases.py")),
                                                   str(flat), name, str(exchange)], flat)
        outcomes.append(result.returncode == 0)
        # Copy a bounded synthetic test package with keys.py omitted. Keep original intact.
        missing = scratch / (name + "-missing-keys")
        missing.mkdir()
        for member in item["files"]:
            if member == "keys.py":
                continue
            target = (missing / member).resolve()
            assert target.is_relative_to(missing.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((flat / member).read_bytes())
        result = run(name + ":missing-member-negative", [sys.executable, "-I", "-c", helper.PROBE,
                                                         str(missing), name], missing)
        outcomes.append(result.returncode != 0 and "ModuleNotFoundError" in result.stderr)
    evidence["all_expected_outcomes"] = all(outcomes)
    evidence["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
    evidence["scratch"] = str(scratch)
    evidence["limits"] = "Offline materialized declared members; local interpreter site packages are not deployed Lambda-layer proof. Synthetic selection/provider/storage, no AWS/IAM/deploy/browser/export/vendor tests. Missing-member negatives expect process failure."
    here.with_suffix(".json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in evidence.items() if key != "members"}, indent=2))
    return 0 if all(outcomes) else 1


if __name__ == "__main__":
    raise SystemExit(main())
