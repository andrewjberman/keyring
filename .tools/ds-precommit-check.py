#!/usr/bin/env python3
"""
DS pre-commit gate: AST-based undefined-name scanner (stdlib-only, Python 3.10+).

Catches Class A latent bugs: missing imports, typos, renamed-name-missed-caller.
Complements `python -m py_compile` (which catches syntax but not function-body
undefined names — e.g. 081223b5 B_00 defaultdict miss passed py_compile).

Scope: function bodies, lambda bodies, comprehension element/cond expressions,
class-body statements. Module-level statements are NOT scanned (covered by
py_compile + runtime import). Cross-file names are NOT resolved (Class B).

Usage:
  python .tools/ds-precommit-check.py file.py [more.py ...]
  python .tools/ds-precommit-check.py --verbose file.py
  python .tools/ds-precommit-check.py --strict file.py    # scan even star-imports

Exit 0 on clean; exit 1 with `{file}:{lineno}: undefined name '{name}'` per miss.
"""
from __future__ import annotations

import argparse
import ast
import builtins
import fnmatch
import sys
from pathlib import Path

# Paths that must carry `from __future__ import annotations` (ADHC_DSFLOW.004).
_FUTURE_ANNOT_PATTERNS = [
    'data/*/scripts/gold/*.py',
    'data/*/scripts/silver/*.py',
    'data/*/scripts/bronze/*.py',
]

# Silver canonical ID dtype enforcement (ADVI_INFNNA.ID-DTYPE-ENFORCEMENT).
_SILVER_BUILDER_PATTERNS = ['data/*/scripts/silver/*.py']
_COERCE_HELPER_NAMES = {'coerce_silver_ids'}


def _path_requires_future_annotations(filepath: str) -> bool:
    p = str(filepath).replace('\\', '/')
    return any(fnmatch.fnmatch(p, pat) for pat in _FUTURE_ANNOT_PATTERNS)


def _path_is_silver_builder(filepath: str) -> bool:
    p = str(filepath).replace('\\', '/')
    return any(fnmatch.fnmatch(p, pat) for pat in _SILVER_BUILDER_PATTERNS)


def _annotation_text(node: ast.expr | None) -> str:
    return ast.unparse(node) if node is not None else ''


def _annotation_is_dataframe(node: ast.expr | None) -> bool:
    return 'DataFrame' in _annotation_text(node)


def _annotation_excludes_dataframe(node: ast.expr | None) -> bool:
    """True only when annotation is present and clearly not a DataFrame type."""
    if node is None:
        return False
    text = _annotation_text(node)
    return bool(text) and 'DataFrame' not in text


def _has_future_annotations_at_module_level(tree: ast.Module) -> bool:
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module == '__future__':
            for alias in node.names:
                if alias.name == 'annotations':
                    return True
    return False


def check_future_annotations_source(source: str, filepath_hint: str) -> str | None:
    """Return an error string if filepath_hint requires the __future__ import but source lacks it.

    filepath_hint is used only for pattern-matching and error reporting;
    the caller supplies the already-read source text.
    """
    if not _path_requires_future_annotations(filepath_hint):
        return None
    tree = ast.parse(source)
    if not _has_future_annotations_at_module_level(tree):
        return (
            f"{filepath_hint}:1: BLOCKED: missing `from __future__ import annotations` "
            f"-- required for PEP-604 union-type syntax on Python 3.9 runners "
            f"(ADHC_DSFLOW.004). Add as first import statement after any docstring/shebang."
        )
    return None


MODULE_DUNDERS = {
    "__name__", "__file__", "__doc__", "__spec__", "__loader__",
    "__package__", "__path__", "__builtins__", "__all__", "__dict__",
    "__class__", "__module__", "__qualname__", "__annotations__",
}
BUILTINS = set(vars(builtins).keys()) | MODULE_DUNDERS


def _add_targets(node, out):
    """Recursively add Name targets from assign-like nodes (tuple/list unpack, starred)."""
    if isinstance(node, ast.Name):
        out.add(node.id)
    elif isinstance(node, (ast.Tuple, ast.List)):
        for elt in node.elts:
            _add_targets(elt, out)
    elif isinstance(node, ast.Starred):
        _add_targets(node.value, out)


def _collect_import_names(node, out):
    if isinstance(node, ast.Import):
        for alias in node.names:
            out.add(alias.asname or alias.name.split(".")[0])
    elif isinstance(node, ast.ImportFrom):
        for alias in node.names:
            if alias.name != "*":
                out.add(alias.asname or alias.name)


def _collect_module_defined(tree):
    """Names defined at module level. Walks top-level + If/Try branches for conditional imports."""
    defined = set()
    for node in ast.walk(tree):
        # Only count statements whose DEFINITION reaches module scope — skip those inside
        # function/class bodies by filtering using getattr-based nesting detection via ast.walk
        pass
    # Simpler: traverse module body explicitly; recurse into If/Try (not into Def/Class)
    def walk(stmts):
        for n in stmts:
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                _collect_import_names(n, defined)
            elif isinstance(n, ast.Assign):
                for t in n.targets:
                    _add_targets(t, defined)
            elif isinstance(n, (ast.AugAssign, ast.AnnAssign)):
                _add_targets(n.target, defined)
            elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                defined.add(n.name)
            elif isinstance(n, ast.If):
                walk(n.body)
                walk(n.orelse)
            elif isinstance(n, ast.Try):
                walk(n.body)
                walk(n.orelse)
                walk(n.finalbody)
                for h in n.handlers:
                    if h.name:
                        defined.add(h.name)
                    walk(h.body)
            elif isinstance(n, (ast.With, ast.AsyncWith)):
                for item in n.items:
                    if item.optional_vars:
                        _add_targets(item.optional_vars, defined)
                walk(n.body)
            elif isinstance(n, (ast.For, ast.AsyncFor)):
                _add_targets(n.target, defined)
                walk(n.body)
                walk(n.orelse)
    walk(tree.body)
    return defined


def _collect_function_locals(node):
    """Names bound in this function's scope (not recursing into nested functions/classes/comps)."""
    out = set()
    # args
    args = node.args
    for lst in (args.posonlyargs, args.args, args.kwonlyargs):
        for a in lst:
            out.add(a.arg)
    if args.vararg:
        out.add(args.vararg.arg)
    if args.kwarg:
        out.add(args.kwarg.arg)

    body = node.body if isinstance(node.body, list) else [node.body]

    def walk(stmts):
        for n in stmts:
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                out.add(n.name)
                continue  # do NOT descend
            if isinstance(n, (ast.Lambda, ast.ListComp, ast.SetComp,
                              ast.DictComp, ast.GeneratorExp)):
                continue  # own scope
            if isinstance(n, ast.Assign):
                for t in n.targets:
                    _add_targets(t, out)
            elif isinstance(n, (ast.AugAssign, ast.AnnAssign)):
                _add_targets(n.target, out)
            elif isinstance(n, ast.NamedExpr):  # walrus
                _add_targets(n.target, out)
            elif isinstance(n, (ast.For, ast.AsyncFor)):
                _add_targets(n.target, out)
            elif isinstance(n, (ast.With, ast.AsyncWith)):
                for item in n.items:
                    if item.optional_vars:
                        _add_targets(item.optional_vars, out)
            elif isinstance(n, ast.ExceptHandler):
                if n.name:
                    out.add(n.name)
            elif isinstance(n, (ast.Global, ast.Nonlocal)):
                for name in n.names:
                    out.add(name)
            elif isinstance(n, (ast.Import, ast.ImportFrom)):
                _collect_import_names(n, out)
            for child in ast.iter_child_nodes(n):
                walk([child])
    walk(body)
    return out


class Scanner(ast.NodeVisitor):
    def __init__(self, filepath, module_defined):
        self.filepath = filepath
        self.scopes = [module_defined]  # innermost last
        self.misses = []

    def _in_scope(self, name):
        if name in BUILTINS:
            return True
        for sc in self.scopes:
            if name in sc:
                return True
        return False

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load) and not self._in_scope(node.id):
            self.misses.append((self.filepath, node.lineno, node.id))

    def _visit_function(self, node):
        # Decorators, default values, annotations evaluate in ENCLOSING scope
        for d in node.decorator_list:
            self.visit(d)
        for d in node.args.defaults:
            self.visit(d)
        for d in node.args.kw_defaults:
            if d is not None:
                self.visit(d)
        for lst in (node.args.posonlyargs, node.args.args, node.args.kwonlyargs):
            for a in lst:
                if a.annotation:
                    self.visit(a.annotation)
        if node.args.vararg and node.args.vararg.annotation:
            self.visit(node.args.vararg.annotation)
        if node.args.kwarg and node.args.kwarg.annotation:
            self.visit(node.args.kwarg.annotation)
        if getattr(node, "returns", None):
            self.visit(node.returns)
        # Body in new scope
        self.scopes.append(_collect_function_locals(node))
        for stmt in node.body:
            self.visit(stmt)
        self.scopes.pop()

    def visit_FunctionDef(self, node):
        self._visit_function(node)

    def visit_AsyncFunctionDef(self, node):
        self._visit_function(node)

    def visit_Lambda(self, node):
        for d in node.args.defaults:
            self.visit(d)
        for d in node.args.kw_defaults:
            if d is not None:
                self.visit(d)
        self.scopes.append(_collect_function_locals(node))
        self.visit(node.body)
        self.scopes.pop()

    def visit_ClassDef(self, node):
        for d in node.decorator_list:
            self.visit(d)
        for b in node.bases:
            self.visit(b)
        for k in node.keywords:
            self.visit(k.value)
        # Class body scope: class-level names visible in class body, NOT in methods
        class_defined = set()
        for n in node.body:
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                class_defined.add(n.name)
            elif isinstance(n, ast.Assign):
                for t in n.targets:
                    _add_targets(t, class_defined)
            elif isinstance(n, ast.AnnAssign):
                _add_targets(n.target, class_defined)
        self.scopes.append(class_defined)
        for n in node.body:
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # methods don't see class-body scope — pop, visit, restore
                self.scopes.pop()
                self._visit_function(n)
                self.scopes.append(class_defined)
            elif isinstance(n, ast.ClassDef):
                self.scopes.pop()
                self.visit_ClassDef(n)
                self.scopes.append(class_defined)
            else:
                self.visit(n)
        self.scopes.pop()

    def _visit_comprehension(self, node, exprs):
        # First generator's iter evaluates in ENCLOSING scope
        # Subsequent iters + all ifs + element expressions evaluate in COMP scope
        comp_local = set()
        for gen in node.generators:
            _add_targets(gen.target, comp_local)
        self.visit(node.generators[0].iter)
        self.scopes.append(comp_local)
        for i, gen in enumerate(node.generators):
            if i > 0:
                self.visit(gen.iter)
            for cond in gen.ifs:
                self.visit(cond)
        for e in exprs:
            self.visit(e)
        self.scopes.pop()

    def visit_ListComp(self, node):
        self._visit_comprehension(node, [node.elt])

    def visit_SetComp(self, node):
        self._visit_comprehension(node, [node.elt])

    def visit_GeneratorExp(self, node):
        self._visit_comprehension(node, [node.elt])

    def visit_DictComp(self, node):
        self._visit_comprehension(node, [node.key, node.value])


class _SilverIdCoerceChecker(ast.NodeVisitor):
    """Detect build_* functions in silver scripts that return DataFrame without coerce_silver_ids."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.blocks: list[str] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if node.name.startswith('build_'):
            self._check(node)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        if node.name.startswith('build_'):
            self._check(node)
        self.generic_visit(node)

    def _check(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        # Skip functions whose annotation proves they don't return a DataFrame.
        if _annotation_excludes_dataframe(node.returns):
            return
        # Skip unannotated functions that appear void (no non-None return expr).
        if not _annotation_is_dataframe(node.returns) and not self._has_df_return(node):
            return
        if not self._calls_coerce(node):
            self.blocks.append(
                f"{self.filepath}:{node.lineno}: BLOCKED: build function '{node.name}' "
                f"returns DataFrame but missing coerce_silver_ids() call -- "
                f"required by ADVI_INFNNA.SILVER-ID-DTYPE-UNIFY Int64 convention. "
                f"Add `df = coerce_silver_ids(df)` before return."
            )

    @staticmethod
    def _calls_coerce(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                func = child.func
                if isinstance(func, ast.Name) and func.id in _COERCE_HELPER_NAMES:
                    return True
                if isinstance(func, ast.Attribute) and func.attr in _COERCE_HELPER_NAMES:
                    return True
        return False

    @staticmethod
    def _has_df_return(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
        for child in ast.walk(node):
            if isinstance(child, ast.Return) and child.value is not None:
                if isinstance(child.value, ast.Constant) and child.value.value is None:
                    continue
                return True
        return False


def _check_silver_id_astype_regression(source: str, filepath_hint: str) -> list[str]:
    """Return WARN strings for *_id columns cast via .astype('str'/'str')."""
    warns: list[str] = []
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not (isinstance(func, ast.Attribute) and func.attr == 'astype'):
            continue
        if not node.args:
            continue
        arg = node.args[0]
        is_str_cast = (
            (isinstance(arg, ast.Name) and arg.id == 'str') or
            (isinstance(arg, ast.Constant) and arg.value == 'str')
        )
        if not is_str_cast:
            continue
        obj = func.value
        if not isinstance(obj, ast.Subscript):
            continue
        slice_node = obj.slice
        key: str | None = None
        if isinstance(slice_node, ast.Constant):
            key = slice_node.value
        elif isinstance(slice_node, ast.Index) and isinstance(slice_node.value, ast.Constant):  # type: ignore[attr-defined]
            key = slice_node.value.value  # type: ignore[attr-defined]
        if key and isinstance(key, str) and key.endswith('_id'):
            warns.append(
                f"{filepath_hint}:{node.lineno}: WARN: '{key}' cast via .astype(str) -- "
                f"canonical dtype is Int64 (nullable); use coerce_silver_ids() instead. "
                f"(ADVI_INFNNA.SILVER-ID-DTYPE-UNIFY regression check)"
            )
    return warns


def check_silver_id_dtype(
    source: str, tree: ast.Module, filepath_hint: str
) -> tuple[list[str], list[str]]:
    """Return (blocks, warns) for silver canonical ID dtype checks.

    blocks cause exit 1; warns are informational only.
    Only fires for files matching _SILVER_BUILDER_PATTERNS.
    """
    if not _path_is_silver_builder(filepath_hint):
        return [], []
    checker = _SilverIdCoerceChecker(filepath_hint)
    checker.visit(tree)
    warns = _check_silver_id_astype_regression(source, filepath_hint)
    return checker.blocks, warns


def scan_file(filepath, verbose=False, strict=False):
    path = Path(filepath)
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))

    rc = 0

    # PEP-604 / future-annotations gate (ADHC_DSFLOW.004)
    err = check_future_annotations_source(source, str(filepath))
    if err:
        print(err, file=sys.stderr)
        rc = 1

    # Silver canonical ID dtype gate (ADVI_INFNNA.ID-DTYPE-ENFORCEMENT)
    blocks, warns = check_silver_id_dtype(source, tree, str(filepath))
    for msg in blocks:
        print(msg, file=sys.stderr)
    for msg in warns:
        print(msg, file=sys.stderr)
    if blocks:
        rc = 1

    has_star = any(
        isinstance(n, ast.ImportFrom) and any(a.name == "*" for a in n.names)
        for n in ast.walk(tree)
    )
    if has_star and not strict:
        if verbose:
            print(f"{filepath}: skipped (star import; use --strict to scan)", file=sys.stderr)
        return rc

    module_defined = _collect_module_defined(tree)
    if verbose:
        print(f"{filepath}: {len(module_defined)} module names", file=sys.stderr)

    scanner = Scanner(str(filepath), module_defined)
    scanner.visit(tree)
    for fp, lineno, name in scanner.misses:
        print(f"{fp}:{lineno}: undefined name '{name}'", file=sys.stderr)
    return max(rc, 1 if scanner.misses else 0)


def main():
    ap = argparse.ArgumentParser(description="DS pre-commit AST undefined-name scanner (stdlib-only).")
    ap.add_argument("files", nargs="+", help="Python files to scan")
    ap.add_argument("--verbose", action="store_true", help="Print defined-set size per file")
    ap.add_argument("--strict", action="store_true", help="Scan even files with star imports")
    args = ap.parse_args()
    rc = 0
    for f in args.files:
        rc = max(rc, scan_file(f, verbose=args.verbose, strict=args.strict))
    sys.exit(rc)


if __name__ == "__main__":
    main()
