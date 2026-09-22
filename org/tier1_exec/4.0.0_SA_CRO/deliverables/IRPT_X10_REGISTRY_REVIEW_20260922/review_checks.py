from pathlib import Path
import subprocess
import sys
import json
import hashlib
import os
import re
import importlib.util
import copy
import difflib

ROOT = Path(__file__).resolve().parent
SOURCE = Path(r"C:\Users\AndrewBerman\Desktop\ajb_irpt_m")
SHARED = Path(r"C:\Users\AndrewBerman\Desktop\ajb_workspace")
ENV = dict(
    os.environ,
    PYTHONDONTWRITEBYTECODE="1",
    PYTHONIOENCODING="utf-8",
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="1",
)
PINS = {
    "baseline": "78a4859664",
    "candidate": "587e782bc6",
    "generated_evidence": "3c14153eeb",
    "x10": "705dae3202",
    "ruling": "3c55f37800",
    "order": "8529764a5d",
    "grant": "820f35ec69",
}
BASE = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/"


def git(*args, repo=SOURCE):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def put(path, data):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return target


def run(tag, args, cwd=ROOT):
    q = subprocess.run(
        args, cwd=cwd, env=ENV, capture_output=True, encoding="utf-8", errors="replace"
    )
    put(Path("evidence") / (tag + ".txt"), (q.stdout + q.stderr).encode())
    print(
        tag, "rc=" + str(q.returncode), (q.stdout + q.stderr).strip().splitlines()[-1:]
    )
    return {"rc": q.returncode, "command": args, "output": q.stdout + q.stderr}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    sys.dont_write_bytecode = True
    pins = {
        k: git("rev-parse", v + "^{commit}").decode().strip() for k, v in PINS.items()
    }
    records = []
    inv = json.loads(
        git(
            "show",
            pins["generated_evidence"]
            + ":"
            + BASE
            + "GENERATED_CARRIER_INVENTORY.json",
        )
    )
    for name in [
        "REGISTRY_CANDIDATE.md",
        "REGISTRY_EVIDENCE.json",
        "GENERATED_CARRIER_INVENTORY.json",
        "GENERATED_CARRIER_DIFFS.md",
    ]:
        pin = (
            pins["generated_evidence"]
            if name.startswith("GENERATED")
            else pins["candidate"]
        )
        put(Path("evidence/producer") / name, git("show", pin + ":" + BASE + name))
    for label in ["baseline", "candidate"]:
        pin = pins[label]
        files = (
            git("ls-tree", "-r", "--name-only", pin, "--", "infra/logic/registry")
            .decode()
            .splitlines()
        )
        files += [
            "lib/opal_naming.py",
            "lib/tests/test_opal_naming.py",
            "org/standards/NAMING_SCHEMA.json",
            "org/missions/DIRECTIVES.yaml",
            "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md",
            "org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json",
        ] + [x["path"] for x in inv["paths"]]
        if label == "candidate":
            files += ["lib/tests/test_irpt_destination.py"]
        for path in sorted(set(files)):
            data = git("show", pin + ":" + path)
            put(Path("snapshots") / label / path, data)
            records.append(
                {
                    "snapshot": label,
                    "pin": pin,
                    "path": path,
                    "sha256": hashlib.sha256(data).hexdigest(),
                }
            )
    for key, path in [
        ("x10", "infra/logic/06_CONFORMANCE_LEDGER.md"),
        (
            "ruling",
            "org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md",
        ),
        (
            "order",
            "org/tier1_exec/4.0.0_SA_CRO/task_orders/IRPT-X10_REGISTRY_REVIEW_20260922.md",
        ),
    ]:
        put(
            Path("evidence/authority") / (key + ".md"),
            git("show", pins[key] + ":" + path),
        )
    put(
        Path("evidence/source_diff.patch"),
        git(
            "diff",
            pins["baseline"],
            pins["candidate"],
            "--",
            "lib/opal_naming.py",
            "lib/tests/test_irpt_destination.py",
            "infra/logic/registry",
        ),
    )
    put(
        Path("evidence/input_manifest.json"),
        json.dumps({"pins": pins, "files": records}, indent=2).encode(),
    )
    (ROOT / "test_tmp").mkdir(exist_ok=True)
    results = {"pins": pins, "generation": {}, "naming_tests": {}}
    for label in ["baseline", "candidate"]:
        snap = ROOT / "snapshots" / label
        results["generation"][label] = run(
            label + "_generation",
            [
                sys.executable,
                "-B",
                str(snap / "lib/opal_naming.py"),
                "generate",
                "--out",
                str(ROOT / "generated" / label),
            ],
        )
        results["naming_tests"][label] = run(
            label + "_naming_tests",
            [
                sys.executable,
                "-B",
                "-m",
                "pytest",
                "-q",
                "-p",
                "no:cacheprovider",
                "--basetemp",
                str(ROOT / "test_tmp" / label),
                "-k",
                "not targets_report and not lambda_plane_consumers and not terraform_plane_consumers and not hash_pinned_census and not cmd_targets",
                str(snap / "lib/tests/test_opal_naming.py"),
            ],
            cwd=snap,
        )
    snap = ROOT / "snapshots/candidate"
    results["targeted_tests"] = run(
        "candidate_targeted_tests",
        [
            sys.executable,
            "-B",
            "-m",
            "pytest",
            "-q",
            "-p",
            "no:cacheprovider",
            "--basetemp",
            str(ROOT / "test_tmp/targeted"),
            str(snap / "lib/tests/test_irpt_destination.py"),
        ],
        cwd=snap,
    )
    results["validation"] = run(
        "candidate_validation",
        [sys.executable, "-B", str(snap / "lib/opal_naming.py"), "validate"],
    )
    generated = []

    def clean(t):
        return re.sub(r"(registry@)[0-9a-f]{16}", r"\1<STAMP>", t)

    for item in inv["paths"]:
        path = item["path"]
        source = (ROOT / "snapshots/baseline" / path).read_text(encoding="utf-8")
        b = (ROOT / "generated/baseline" / path).read_text(encoding="utf-8")
        c = (ROOT / "generated/candidate" / path).read_text(encoding="utf-8")
        record = {
            "path": path,
            "baseline_sha256": hashlib.sha256(
                (ROOT / "generated/baseline" / path).read_bytes()
            ).hexdigest(),
            "candidate_sha256": hashlib.sha256(
                (ROOT / "generated/candidate" / path).read_bytes()
            ).hexdigest(),
            "inherited_drift": source != b,
            "inherited_nonstamp": clean(source) != clean(b),
            "irpt_stamp_only": clean(b) == clean(c),
            "candidate_carrier_unchanged": git("show", pins["baseline"] + ":" + path)
            == git("show", pins["candidate"] + ":" + path),
        }
        record["producer_hashes_reproduced"] = (
            record["baseline_sha256"] == item["baseline_generated_sha256"]
            and record["candidate_sha256"] == item["candidate_generated_sha256"]
        )
        generated.append(record)
        diff = (
            "".join(
                difflib.unified_diff(
                    source.splitlines(True),
                    b.splitlines(True),
                    fromfile="baseline-source",
                    tofile="baseline-generated",
                )
            )
            + "\n"
            + "".join(
                difflib.unified_diff(
                    b.splitlines(True),
                    c.splitlines(True),
                    fromfile="baseline-generated",
                    tofile="candidate-generated",
                )
            )
        )
        put(
            Path("evidence/generated_diffs") / (path.replace("/", "__") + ".diff"),
            diff.encode(),
        )
    results["generated_carriers"] = generated
    bs = json.loads(
        (ROOT / "snapshots/baseline/infra/logic/registry/scopes.json").read_text()
    )
    cs = json.loads((snap / "infra/logic/registry/scopes.json").read_text())
    # scopes document root remains unchanged except its scopes row list.
    scopekey = next(
        k
        for k, v in bs.items()
        if isinstance(v, list) and v and isinstance(v[0], dict) and "key" in v[0]
    )
    results["scope_list_key"] = scopekey
    reduced = copy.deepcopy(cs)
    reduced[scopekey] = [x for x in reduced[scopekey] if x["key"] != "irpt"]
    results["non_irpt_scopes_equal"] = reduced == bs
    results["other_registry_blobs_equal"] = {
        p.name: (
            p.read_bytes() == (snap / "infra/logic/registry" / p.name).read_bytes()
        )
        for p in (ROOT / "snapshots/baseline/infra/logic/registry").glob("*.json")
        if p.name != "scopes.json"
    }
    # Full existing function bodies must be identical except the explicitly changed loader/validator.
    import ast

    def funcs(path):
        return {
            n.name: ast.dump(n, include_attributes=False)
            for n in ast.parse(path.read_text()).body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        }

    bf = funcs(ROOT / "snapshots/baseline/lib/opal_naming.py")
    cf = funcs(snap / "lib/opal_naming.py")
    results["changed_existing_functions"] = [k for k in bf if bf[k] != cf.get(k)]
    results["new_functions"] = sorted(set(cf) - set(bf))
    for group in ["generation", "naming_tests"]:
        results[group] = {
            k: {a: b for a, b in v.items() if a != "output"}
            for k, v in results[group].items()
        }
    for group in ["targeted_tests", "validation"]:
        results[group].pop("output")
    put(Path("evidence/reproduction.json"), json.dumps(results, indent=2).encode())
    print(
        json.dumps(
            {
                k: v
                for k, v in results.items()
                if k not in ["pins", "generation", "naming_tests"]
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
