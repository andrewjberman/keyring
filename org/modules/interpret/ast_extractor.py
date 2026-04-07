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
# Module entry point
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TypeScript / JavaScript structure extraction (regex-based, no parser)
# ---------------------------------------------------------------------------

_TS_FUNC = re.compile(
    r"^(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*(?:<[^>]*>)?\s*\(([^)]*)\)",
    re.MULTILINE,
)
_TS_ARROW_EXPORT = re.compile(
    r"^export\s+(?:const|let)\s+(\w+)\s*(?::\s*\w+(?:<[^>]*>)?)?\s*=\s*(?:async\s+)?\(",
    re.MULTILINE,
)
_TS_INTERFACE = re.compile(r"^(?:export\s+)?interface\s+(\w+)", re.MULTILINE)
_TS_TYPE_ALIAS = re.compile(r"^(?:export\s+)?type\s+(\w+)\s*=", re.MULTILINE)
_TS_CLASS = re.compile(r"^(?:export\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?", re.MULTILINE)
_TS_IMPORT = re.compile(r"^import\s+.*?from\s+['\"]([^'\"]+)['\"]", re.MULTILINE)
_TS_EXPORT_DEFAULT = re.compile(r"^export\s+default\s+(?:function\s+)?(\w+)", re.MULTILINE)


def _extract_typescript(path: Path, content: str) -> ASTStructure:
    """Extract structure from TypeScript/JavaScript using regex."""
    result = ASTStructure(path=str(path), language="typescript", loc=content.count("\n") + 1)

    # Functions (named + arrow exports)
    for m in _TS_FUNC.finditer(content):
        args = [a.strip().split(":")[0].strip() for a in m.group(2).split(",") if a.strip()]
        result.functions.append({
            "name": m.group(1), "args": args, "returns": "",
            "line": content[:m.start()].count("\n") + 1, "decorators": [],
        })
    for m in _TS_ARROW_EXPORT.finditer(content):
        result.functions.append({
            "name": m.group(1), "args": [], "returns": "",
            "line": content[:m.start()].count("\n") + 1, "decorators": ["export"],
        })

    # Interfaces and type aliases -> classes list (structural types)
    for m in _TS_INTERFACE.finditer(content):
        result.classes.append({
            "name": m.group(1), "bases": ["interface"], "methods": [],
            "line": content[:m.start()].count("\n") + 1,
        })
    for m in _TS_TYPE_ALIAS.finditer(content):
        result.classes.append({
            "name": m.group(1), "bases": ["type"], "methods": [],
            "line": content[:m.start()].count("\n") + 1,
        })
    for m in _TS_CLASS.finditer(content):
        result.classes.append({
            "name": m.group(1), "bases": [m.group(2)] if m.group(2) else [], "methods": [],
            "line": content[:m.start()].count("\n") + 1,
        })

    # Imports
    for m in _TS_IMPORT.finditer(content):
        result.imports.append({"from": m.group(1), "names": []})

    # Exports
    for m in _TS_EXPORT_DEFAULT.finditer(content):
        result.exports.append(m.group(1))

    return result


# ---------------------------------------------------------------------------
# Terraform structure extraction
# ---------------------------------------------------------------------------

_TF_RESOURCE = re.compile(r'^resource\s+"(\w+)"\s+"(\w+)"', re.MULTILINE)
_TF_DATA = re.compile(r'^data\s+"(\w+)"\s+"(\w+)"', re.MULTILINE)
_TF_VARIABLE = re.compile(r'^variable\s+"(\w+)"', re.MULTILINE)
_TF_OUTPUT = re.compile(r'^output\s+"(\w+)"', re.MULTILINE)
_TF_LOCAL = re.compile(r'^locals\s*\{', re.MULTILINE)
_TF_MODULE = re.compile(r'^module\s+"(\w+)"', re.MULTILINE)


def _extract_terraform(path: Path, content: str) -> ASTStructure:
    """Extract structure from Terraform HCL files."""
    result = ASTStructure(path=str(path), language="terraform", loc=content.count("\n") + 1)

    # Resources -> functions (type.name as the "function")
    for m in _TF_RESOURCE.finditer(content):
        result.functions.append({
            "name": f"{m.group(1)}.{m.group(2)}", "args": [], "returns": "resource",
            "line": content[:m.start()].count("\n") + 1, "decorators": [],
        })
    for m in _TF_DATA.finditer(content):
        result.functions.append({
            "name": f"data.{m.group(1)}.{m.group(2)}", "args": [], "returns": "data",
            "line": content[:m.start()].count("\n") + 1, "decorators": [],
        })
    for m in _TF_MODULE.finditer(content):
        result.functions.append({
            "name": f"module.{m.group(1)}", "args": [], "returns": "module",
            "line": content[:m.start()].count("\n") + 1, "decorators": [],
        })

    # Variables -> imports (inputs to the module)
    for m in _TF_VARIABLE.finditer(content):
        result.imports.append({"from": "variable", "names": [m.group(1)]})

    # Outputs -> exports
    for m in _TF_OUTPUT.finditer(content):
        result.exports.append(m.group(1))

    return result


_EXTRACTORS = {
    ".py": _extract_python,
    ".json": _extract_json,
    ".yaml": _extract_yaml,
    ".yml": _extract_yaml,
    ".md": _extract_markdown,
    ".ts": _extract_typescript,
    ".tsx": _extract_typescript,
    ".js": _extract_typescript,
    ".mjs": _extract_typescript,
    ".jsx": _extract_typescript,
    ".tf": _extract_terraform,
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
