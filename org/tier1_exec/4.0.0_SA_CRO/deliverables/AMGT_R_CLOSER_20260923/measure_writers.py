"""Read deployed ZIP and candidate source; enumerate drafting output edges."""

import ast
import base64
import hashlib
import io
import json
from pathlib import Path
import urllib.request
import zipfile

import boto3


TOKENS = ("drafted_sections", "read_drafted_sections", "_read_drafting_document",
          "read_description", "read_thesis_bundle", "drafting/v1/")


def scan(sources):
    result = {"python_files": len(sources), "matching_files": [], "definitions": [],
              "calls": [], "literal_output_keys": [], "parse_failures": []}
    for name, raw in sources.items():
        source = raw.decode("utf-8-sig")
        if not any(token in source for token in TOKENS):
            continue
        result["matching_files"].append({"path": name, "sha256": hashlib.sha256(raw).hexdigest()})
        try:
            tree = ast.parse(source)
        except SyntaxError as exc:
            result["parse_failures"].append({"path": name, "reason": str(exc)})
            continue
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name in TOKENS or node.name in ("_drafting_block", "_print_pack", "read_posture"):
                result["definitions"].append({"path": name, "name": node.name,
                                              "line": node.lineno,
                                              "source": ast.get_source_segment(source, node)})
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    called = ast.unparse(child.func)
                    if called in TOKENS or called in ("_drafting_block", "read_security_overlay", "_print_pack"):
                        result["calls"].append({"path": name, "caller": node.name,
                                               "callee": called, "line": child.lineno,
                                               "expression": ast.unparse(child)})
                if isinstance(child, ast.Dict):
                    for key in child.keys:
                        if isinstance(key, ast.Constant) and key.value == "drafted_sections":
                            result["literal_output_keys"].append({"path": name, "function": node.name,
                                                                  "line": child.lineno})
    return result


def main():
    home = Path(__file__).parent
    client = boto3.client("lambda", region_name="us-east-1")
    info = client.get_function(FunctionName="opal-amgt-scoped-api")
    raw = urllib.request.urlopen(info["Code"]["Location"], timeout=30).read()
    digest = base64.b64encode(hashlib.sha256(raw).digest()).decode()
    assert digest == info["Configuration"]["CodeSha256"]
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        sources = {n: archive.read(n) for n in archive.namelist() if n.endswith(".py")}
    result = {"deployed_package_sha256_base64": digest, "deployed": scan(sources)}
    paths = list(Path("lib").rglob("*.py")) + list(Path("infra").rglob("*.py"))
    paths = [p for p in paths if not any(part in ("site-packages", "vendor", "__pycache__", ".venv") for part in p.parts)]
    result["candidate"] = scan({p.as_posix(): p.read_bytes() for p in paths})
    env = info["Configuration"].get("Environment", {}).get("Variables", {})
    result["drafting_location_overrides"] = {k: env.get(k) for k in (
        "AMGT_DRAFTING_PREFIX", "AMGT_DRAFTING_ROOT", "AMGT_DRAFTING_BUCKET")}
    result["limitations"] = [
        "Static syntax census; dynamic string construction is not proven absent by token matches alone.",
        "Handler branches, print renderer, posture output shape and all matching first-party call sites manually reviewed separately.",
        "Tests accepting injected drafting blocks are not production callers.",
    ]
    (home / "WRITER_CENSUS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for plane in ("deployed", "candidate"):
        print(plane, "python_files", result[plane]["python_files"], "matching_files", len(result[plane]["matching_files"]),
              "parse_failures", len(result[plane]["parse_failures"]))
        for call in result[plane]["calls"]:
            if "/tests/" not in call["path"] and not Path(call["path"]).name.startswith("test_"):
                print(json.dumps(call))


if __name__ == "__main__":
    main()
