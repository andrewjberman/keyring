"""
In: Interpret -- AST Structure Extractor (D-mode).

Parses source files into ASTs and extracts structural metadata.
Eliminates the common LLM pattern of "read this file and tell me
what functions it has."

Supports: Python (ast), JSON (json), YAML (yaml), Markdown (regex).

Spec: ONT.CORE.KF_ACCELERATION Section 2.1
"""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .. import ModuleOutput
from ..perceive.filesystem_scanner import FileMetadata


@dataclass
class ASTStructure:
    """Structural skeleton of a source file."""
    path: str
    language: str                    # python, json, yaml, markdown, unknown
    functions: list[dict] = field(default_factory=list)   # {name, args, returns, line, decorators}
    classes: list[dict] = field(default_factory=list)      # {name, bases, methods, line}
    imports: list[dict] = field(default_factory=list)      # {from, names}
    exports: list[str] = field(default_factory=list)       # __all__ entries
    constants: list[dict] = field(default_factory=list)    # {name, line}
    schema_shape: dict = field(default_factory=dict)       # For JSON/YAML: key structure
    headings: list[dict] = field(default_factory=list)     # For Markdown: {level, text, line}
    loc: int = 0                     # Lines of code
    has_docstring: bool = False


# ---------------------------------------------------------------------------
# Python AST extraction
# ---------------------------------------------------------------------------

def _extract_python(path: Path, content: str) -> ASTStructure:
    """Extract structure from a Python file using the ast module."""
    result = ASTStructure(path=str(path), language="python", loc=content.count("\n") + 1)

    try:
        tree = ast.parse(content)
    except SyntaxError:
        return result

    # Module-level docstring
    if (tree.body and isinstance(tree.body[0], ast.Expr)
            and isinstance(tree.body[0].value, (ast.Constant, ast.Str))):
        result.has_docstring = True

    for node in ast.walk(tree):
        # Functions
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = [a.arg for a in node.args.args]
            returns = ""
            if node.returns:
                try:
                    returns = ast.unparse(node.returns)
                except Exception:
                    returns = "..."
            decorators = []
            for d in node.decorator_list:
                try:
                    decorators.append(ast.unparse(d))
                except Exception:
                    decorators.append("...")
            result.functions.append({
                "name": node.name,
                "args": args,
                "returns": returns,
                "line": node.lineno,
                "decorators": decorators,
            })

        # Classes
        elif isinstance(node, ast.ClassDef):
            bases = []
            for b in node.bases:
                try:
                    bases.append(ast.unparse(b))
                except Exception:
                    bases.append("...")
            methods = [
                n.name for n in node.body
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
            ]
            result.classes.append({
                "name": node.name,
                "bases": bases,
                "methods": methods,
                "line": node.lineno,
            })

        # Imports
        elif isinstance(node, ast.ImportFrom):
            names = [alias.name for alias in node.names]
            result.imports.append({
                "from": node.module or "",
                "names": names,
            })
        elif isinstance(node, ast.Import):
            for alias in node.names:
                result.imports.append({
                    "from": "",
                    "names": [alias.name],
                })

    # __all__
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        result.exports = [
                            elt.value for elt in node.value.elts
                            if isinstance(elt, ast.Constant) and isinstance(elt.value, str)
                        ]

    return result


# ---------------------------------------------------------------------------
# JSON/YAML schema extraction
# ---------------------------------------------------------------------------

def _extract_schema_shape(data: Any, depth: int = 0, max_depth: int = 3) -> dict:
    """Extract the shape (key names + value types) of a JSON/YAML structure."""
    if depth >= max_depth:
        return {"_type": type(data).__name__}

    if isinstance(data, dict):
        shape = {}
        for k, v in list(data.items())[:20]:  # Cap at 20 keys
            shape[k] = _extract_schema_shape(v, depth + 1, max_depth)
        return shape
    elif isinstance(data, list):
        if data:
            return {"_type": "list", "_length": len(data),
                    "_item": _extract_schema_shape(data[0], depth + 1, max_depth)}
        return {"_type": "list", "_length": 0}
    else:
        return {"_type": type(data).__name__}


def _extract_json(path: Path, content: str) -> ASTStructure:
    """Extract schema shape from a JSON file."""
    result = ASTStructure(path=str(path), language="json", loc=content.count("\n") + 1)
    try:
        data = json.loads(content)
        result.schema_shape = _extract_schema_shape(data)
    except json.JSONDecodeError:
        pass
    return result


def _extract_yaml(path: Path, content: str) -> ASTStructure:
    """Extract schema shape from a YAML file."""
    result = ASTStructure(path=str(path), language="yaml", loc=content.count("\n") + 1)
    try:
        import yaml
        data = yaml.safe_load(content)
        if isinstance(data, (dict, list)):
            result.schema_shape = _extract_schema_shape(data)
    except Exception:
        pass
    return result


# ---------------------------------------------------------------------------
# Markdown structure extraction
# ---------------------------------------------------------------------------

_MD_HEADING = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)


def _extract_markdown(path: Path, content: str) -> ASTStructure:
    """Extract heading structure from a Markdown file."""
    result = ASTStructure(path=str(path), language="markdown", loc=content.count("\n") + 1)
    for i, line in enumerate(content.split("\n"), 1):
        m = _MD_HEADING.match(line)
        if m:
            result.headings.append({
                "level": len(m.group(1)),
                "text": m.group(2).strip(),
                "line": i,
            })
    return result


# ---------------------------------------------------------------------------
# HCL (Terraform) structure extraction
# ---------------------------------------------------------------------------

# resource "aws_lambda_function" "auth_handler" { ... }
_HCL_BLOCK = re.compile(
    r'^(resource|data|variable|output|locals|module|provider|terraform)\s+'
    r'(?:"([^"]+)"\s+)?(?:"([^"]+)"\s*)?\{',
    re.MULTILINE,
)

# var.enable_lambda_edge, local.account_id, aws_iam_role.lambda_edge.arn
_HCL_REF = re.compile(
    r'\b(?:'
    r'(var)\.(\w+)'                                          # var.name
    r'|(local)\.(\w+)'                                       # local.name
    r'|(data)\.(\w+)\.(\w+)'                                 # data.type.name
    r'|(\w+)\.(\w+)\.(\w+)'                                  # resource_type.name.attr
    r')'
)

# "portal-auth/auth-validator-edge.zip", "opal-data-bd", ARN patterns
_HCL_STRING_LITERAL = re.compile(r'"([^"]*)"')


def _extract_hcl(path: Path, content: str) -> ASTStructure:
    """Extract structure from a Terraform HCL file."""
    result = ASTStructure(path=str(path), language="hcl", loc=content.count("\n") + 1)

    blocks = []
    resources = []
    data_sources = []
    variables = []
    outputs = []
    refs_out = set()
    string_literals = set()

    for m in _HCL_BLOCK.finditer(content):
        block_type = m.group(1)
        type_label = m.group(2) or ""
        name_label = m.group(3) or ""
        line = content[:m.start()].count("\n") + 1

        entry = {
            "block_type": block_type,
            "type_label": type_label,
            "name_label": name_label,
            "line": line,
        }

        if block_type == "resource":
            resources.append(entry)
            result.classes.append({
                "name": f"{type_label}.{name_label}",
                "bases": [block_type],
                "methods": [],
                "line": line,
            })
        elif block_type == "data":
            data_sources.append(entry)
            result.classes.append({
                "name": f"data.{type_label}.{name_label}",
                "bases": [block_type],
                "methods": [],
                "line": line,
            })
        elif block_type == "variable":
            variables.append(entry)
            result.constants.append({"name": f"var.{type_label}", "line": line})
        elif block_type == "output":
            outputs.append(entry)
            result.exports.append(type_label)
        elif block_type == "locals":
            result.constants.append({"name": "locals", "line": line})

    # Extract all cross-resource references
    for m in _HCL_REF.finditer(content):
        if m.group(1):    # var.name
            refs_out.add(f"var.{m.group(2)}")
        elif m.group(3):  # local.name
            refs_out.add(f"local.{m.group(4)}")
        elif m.group(5):  # data.type.name
            refs_out.add(f"data.{m.group(6)}.{m.group(7)}")
        elif m.group(8):  # resource_type.name.attr
            # Filter noise: skip common non-resource patterns
            rtype = m.group(8)
            if rtype.startswith("aws_") or rtype in ("module", "each"):
                refs_out.add(f"{rtype}.{m.group(9)}")

    # Extract string literals for S3 keys, ARN patterns, bucket names
    for m in _HCL_STRING_LITERAL.finditer(content):
        val = m.group(1)
        if "/" in val or val.startswith("arn:") or val.startswith("opal-"):
            string_literals.add(val)

    result.imports = [{"from": "hcl_ref", "names": sorted(refs_out)}]

    result.schema_shape = {
        "resources": [f"{r['type_label']}.{r['name_label']}" for r in resources],
        "data_sources": [f"{d['type_label']}.{d['name_label']}" for d in data_sources],
        "variables": [v["type_label"] for v in variables],
        "outputs": [o["type_label"] for o in outputs],
        "string_literals": sorted(string_literals),
    }

    return result


# ---------------------------------------------------------------------------
# ESM (JavaScript/MJS) structure extraction
# ---------------------------------------------------------------------------

_ESM_IMPORT = re.compile(
    r'^import\s+(?:(\{[^}]+\})|(\w+))\s+from\s+["\']([^"\']+)["\']',
    re.MULTILINE,
)
_ESM_EXPORT_FUNC = re.compile(
    r'^export\s+(?:const|function|async\s+function)\s+(\w+)',
    re.MULTILINE,
)
_ESM_CONST = re.compile(
    r'^\s*(?:export\s+)?const\s+(\w+)\s*=',
    re.MULTILINE,
)
_ESM_STRING_LITERAL = re.compile(r'["\']([^"\']{2,})["\']')
_ESM_ARROW_FUNC = re.compile(
    r'(?:^|\s)(?:export\s+)?(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\(',
    re.MULTILINE,
)


def _extract_esm(path: Path, content: str) -> ASTStructure:
    """Extract structure from an ES module (.mjs/.js) file."""
    result = ASTStructure(path=str(path), language="esm", loc=content.count("\n") + 1)

    # Imports
    for m in _ESM_IMPORT.finditer(content):
        named = m.group(1)  # { Foo, Bar }
        default = m.group(2)  # Foo
        source = m.group(3)
        names = []
        if named:
            names = [n.strip() for n in named.strip("{}").split(",") if n.strip()]
        elif default:
            names = [default]
        result.imports.append({"from": source, "names": names})

    # Exported functions
    for m in _ESM_EXPORT_FUNC.finditer(content):
        line = content[:m.start()].count("\n") + 1
        result.functions.append({
            "name": m.group(1),
            "args": [],
            "returns": "",
            "line": line,
            "decorators": ["export"],
        })

    # Arrow functions assigned to const (e.g., export const handler = async (event) => {})
    for m in _ESM_ARROW_FUNC.finditer(content):
        name = m.group(1)
        line = content[:m.start()].count("\n") + 1
        # Skip if already captured as export function
        if not any(f["name"] == name for f in result.functions):
            result.functions.append({
                "name": name,
                "args": [],
                "returns": "",
                "line": line,
                "decorators": [],
            })

    # Regular (non-exported) function declarations
    for m in re.finditer(r'^function\s+(\w+)\s*\(', content, re.MULTILINE):
        name = m.group(1)
        line = content[:m.start()].count("\n") + 1
        if not any(f["name"] == name for f in result.functions):
            result.functions.append({
                "name": name,
                "args": [],
                "returns": "",
                "line": line,
                "decorators": [],
            })

    # String literals (paths, ARNs, S3 references) — only short, clean values
    interesting = set()
    for m in _ESM_STRING_LITERAL.finditer(content):
        val = m.group(1)
        if len(val) > 120 or "\n" in val:
            continue
        if (val.startswith("/") or val.startswith("opal") or
                val.startswith("arn:") or "s3" in val.lower()):
            interesting.add(val)

    result.schema_shape = {
        "path_patterns": sorted(p for p in interesting if p.startswith("/")),
        "aws_references": sorted(p for p in interesting if "aws" in p.lower() or p.startswith("arn:")),
        "s3_references": sorted(p for p in interesting if "s3" in p.lower() or p.startswith("opal")),
    }

    # Module docstring (JSDoc comment at top)
    if content.lstrip().startswith("/**"):
        result.has_docstring = True

    return result


# ---------------------------------------------------------------------------
# Module entry point
# ---------------------------------------------------------------------------

_EXTRACTORS = {
    ".py": _extract_python,
    ".json": _extract_json,
    ".yaml": _extract_yaml,
    ".yml": _extract_yaml,
    ".md": _extract_markdown,
    ".tf": _extract_hcl,
    ".mjs": _extract_esm,
    ".js": _extract_esm,
}


def extract_ast(file_path: Path) -> ASTStructure:
    """Extract AST/structure from a single file."""
    ext = file_path.suffix.lower()
    extractor = _EXTRACTORS.get(ext)
    if not extractor:
        return ASTStructure(path=str(file_path), language="unknown")

    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ASTStructure(path=str(file_path), language="unknown")

    return extractor(file_path, content)


def execute(inputs: dict, config: dict) -> ModuleOutput:
    """Extract AST structures for all files from Pe stage.

    Inputs:
        pe_output: list[FileMetadata]
    """
    pe_output: list[FileMetadata] = inputs.get("pe_output", [])

    structures = []
    for meta in pe_output:
        s = extract_ast(Path(meta.path))
        structures.append(s)

    # Stats
    by_lang: dict[str, int] = {}
    total_funcs = 0
    total_classes = 0
    for s in structures:
        by_lang[s.language] = by_lang.get(s.language, 0) + 1
        total_funcs += len(s.functions)
        total_classes += len(s.classes)

    return ModuleOutput(
        data=structures,
        confident=structures,
        ambiguous=[],
        mode="D",
        stage="In",
        stats={
            "total_files": len(structures),
            "by_language": by_lang,
            "total_functions": total_funcs,
            "total_classes": total_classes,
        },
    )
