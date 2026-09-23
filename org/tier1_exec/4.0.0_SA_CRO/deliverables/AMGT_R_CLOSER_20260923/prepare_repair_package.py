"""Prepare a two-function ZIP delta from the measured live artifact; never deploy."""

import ast
import base64
import copy
import hashlib
import io
import json
from pathlib import Path
import urllib.request
import zipfile

import boto3


def functions(source):
    return {n.name: n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)}


def main():
    home = Path(__file__).parent
    evidence = json.loads((home / "WRITER_CENSUS.json").read_bytes())
    client = boto3.client("lambda", region_name="us-east-1")
    info = client.get_function(FunctionName="opal-amgt-scoped-api")
    raw = urllib.request.urlopen(info["Code"]["Location"], timeout=30).read()
    before_hash = base64.b64encode(hashlib.sha256(raw).digest()).decode()
    assert before_hash == info["Configuration"]["CodeSha256"] == evidence["deployed_package_sha256_base64"]
    target = "lib/research/api/scoped_amgt.py"
    local = Path(target).read_text(encoding="utf-8")
    names = ("_drafting_block", "read_drafted_sections")
    staging = Path("C:/tmp/amgt-r-no-span-package-20260923")
    staging.mkdir(exist_ok=True)
    (staging / "rollback.zip").write_bytes(raw)
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        old_bytes = archive.read(target)
        old = old_bytes.decode("utf-8")
        old_functions, local_functions = functions(old), functions(local)
        lines = old.splitlines(keepends=True)
        for name in sorted(names, key=lambda name: old_functions[name].lineno, reverse=True):
            node = old_functions[name]
            replacement = ast.get_source_segment(local, local_functions[name]) + "\n"
            lines[node.lineno - 1:node.end_lineno] = [replacement]
        changed = "".join(lines)
        after_functions = functions(changed)
        assert set(old_functions) == set(after_functions)
        changed_functions = [name for name in old_functions if
                             ast.dump(old_functions[name]) != ast.dump(after_functions[name])]
        assert set(changed_functions) == set(names)
        before_tree, after_tree = ast.parse(old), ast.parse(changed)
        before_tree.body = [n for n in before_tree.body if not isinstance(n, ast.FunctionDef) or n.name not in names]
        after_tree.body = [n for n in after_tree.body if not isinstance(n, ast.FunctionDef) or n.name not in names]
        assert ast.dump(before_tree) == ast.dump(after_tree)
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as candidate:
            for member in archive.infolist():
                candidate.writestr(copy.copy(member), changed.encode() if member.filename == target else archive.read(member.filename))
        package = output.getvalue()
        with zipfile.ZipFile(io.BytesIO(package)) as candidate:
            differences = [name for name in archive.namelist() if archive.read(name) != candidate.read(name)]
            assert differences == [target]
            candidate.extractall(staging / "extracted")
        count = len(archive.namelist())
    (staging / "candidate.zip").write_bytes(package)
    result = {
        "function": "opal-amgt-scoped-api", "artifact_directory": staging.as_posix(),
        "deployed_revision_id_at_build": info["Configuration"]["RevisionId"],
        "before_code_sha256_base64": before_hash,
        "candidate_code_sha256_base64": base64.b64encode(hashlib.sha256(package).digest()).decode(),
        "candidate_code_sha256_hex": hashlib.sha256(package).hexdigest(),
        "before_api_sha256": hashlib.sha256(old_bytes).hexdigest(),
        "candidate_api_sha256": hashlib.sha256(changed.encode()).hexdigest(),
        "zip_members": count, "changed_members": differences,
        "changed_functions": changed_functions, "other_ast_nodes_identical": True,
        "deployment": "NOT EXECUTED; requires independent review and CTO+COO pair",
        "rollback_limitation": "Original ZIP restores known no-span serving defect; not a routine safe fallback.",
    }
    (home / "REPAIR_PACKAGE.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
