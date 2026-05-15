#!/usr/bin/env python3
"""vectorize_audit_cli.py — comp-perf vectorize-audit backend: pandas vectorization opportunity detection."""
from __future__ import annotations

import ast
import argparse
import re
import subprocess
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent
_GOLD_ROOT = _WORKSPACE / 'data' / 'orion' / 'scripts' / 'gold'
_VECTORIZE_DIR = _WORKSPACE / 'org' / 'modules' / 'graph' / 'vectorize-audit'


def _resolve_gold_script(script_id: str) -> Path | None:
    """Resolve script_id (e.g. INF_D_06.cash_drag) to full Path."""
    # Direct match
    p = _GOLD_ROOT / f'{script_id}.py'
    if p.exists():
        return p
    # Glob with prefix
    stem = script_id.split('.')[0] if '.' in script_id else script_id
    matches = list(_GOLD_ROOT.glob(f'{stem}*.py'))
    if matches:
        return matches[0]
    # Try full glob
    matches = list(_GOLD_ROOT.glob(f'{script_id}*.py'))
    return matches[0] if matches else None


class _VectorizeVisitor(ast.NodeVisitor):
    """AST visitor that detects pandas vectorization opportunities."""

    def __init__(self, source_lines: list[str]):
        self.findings: list[dict] = []
        self.source_lines = source_lines
        self._current_fn: str | None = None
        self._in_loop_depth = 0
        self._in_submit_fn: set[str] = set()

    def _src_line(self, lineno: int) -> str:
        if 1 <= lineno <= len(self.source_lines):
            return self.source_lines[lineno - 1].strip()
        return ''

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        old = self._current_fn
        self._current_fn = node.name
        self.generic_visit(node)
        self._current_fn = old

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_For(self, node: ast.For) -> None:
        self._in_loop_depth += 1
        self.generic_visit(node)
        self._in_loop_depth -= 1

    def visit_While(self, node: ast.While) -> None:
        self._in_loop_depth += 1
        self.generic_visit(node)
        self._in_loop_depth -= 1

    def visit_Call(self, node: ast.Call) -> None:
        src = ast.unparse(node) if hasattr(ast, 'unparse') else ''

        # Rule 1: groupby(...).apply(lambda...) — per-partition grouped apply
        if self._is_groupby_apply_lambda(node):
            context = 'inside loop' if self._in_loop_depth > 0 else 'top-level (may be vectorizable)'
            sketch = self._make_sketch_groupby_apply(node)
            self.findings.append({
                'rule': 'GROUPBY-APPLY-LAMBDA',
                'line': node.lineno,
                'fn': self._current_fn or '<module>',
                'snippet': self._src_line(node.lineno),
                'context': context,
                'severity': 'WARN' if self._in_loop_depth > 0 else 'INFO',
                'refactor_sketch': sketch,
                'detail': 'groupby().apply(lambda) creates Python-speed per-group loop; replace with named agg or vectorized ops',
            })

        # Rule 2: ThreadPoolExecutor.submit with per-partition functions
        if self._is_pool_submit(node):
            self.findings.append({
                'rule': 'THREADPOOL-PER-PARTITION',
                'line': node.lineno,
                'fn': self._current_fn or '<module>',
                'snippet': self._src_line(node.lineno),
                'context': 'parallel per-partition loop',
                'severity': 'INFO',
                'refactor_sketch': 'Consider: load all partitions via list comp → pd.concat → single vectorized groupby.agg',
                'detail': 'ThreadPoolExecutor.submit per partition is I/O parallel but CPU still serial-per-partition',
            })

        self.generic_visit(node)

    def _is_groupby_apply_lambda(self, node: ast.Call) -> bool:
        """Detect df.groupby(...).apply(lambda ...) pattern."""
        if not isinstance(node.func, ast.Attribute):
            return False
        if node.func.attr != 'apply':
            return False
        # Check there's a lambda argument
        if not node.args:
            return False
        first_arg = node.args[0]
        if not isinstance(first_arg, ast.Lambda):
            return False
        # Check the value being called is itself a .groupby() call
        obj = node.func.value
        if isinstance(obj, ast.Call):
            if isinstance(obj.func, ast.Attribute) and obj.func.attr == 'groupby':
                return True
        # Also match chained: (df.groupby(...)\n  .apply(lambda...))
        return False

    def _is_pool_submit(self, node: ast.Call) -> bool:
        """Detect pool.submit(fn, partition_arg) inside a for/futures dict comp."""
        if not isinstance(node.func, ast.Attribute):
            return False
        return node.func.attr == 'submit' and self._in_loop_depth > 0

    def _make_sketch_groupby_apply(self, node: ast.Call) -> str:
        # Try to extract column names from lambda body
        if node.args and isinstance(node.args[0], ast.Lambda):
            lam = node.args[0]
            body = ast.unparse(lam.body) if hasattr(ast, 'unparse') else '<lambda body>'
            if 'pd.Series' in body or 'Series' in body:
                return (
                    'Replace groupby().apply(lambda g: pd.Series({...})) with '
                    'groupby().agg(col=("src_col", "sum")) or named aggregation. '
                    'If multi-partition: concat all frames first, then single groupby on (partition_key, group_key).'
                )
        return 'Replace groupby().apply(lambda) with groupby().agg() or transform(). Vectorizes CPU-bound per-group Python.'


def _audit_script(script_path: Path, source: str | None = None) -> list[dict]:
    """Run vectorize audit on a gold script source."""
    if source is None:
        source = script_path.read_text(encoding='utf-8', errors='ignore')
    lines = source.splitlines()

    try:
        tree = ast.parse(source, filename=str(script_path))
    except SyntaxError as e:
        return [{'rule': 'PARSE-ERROR', 'line': 0, 'fn': '', 'snippet': str(e),
                 'severity': 'ERROR', 'detail': 'Could not parse file', 'refactor_sketch': ''}]

    visitor = _VectorizeVisitor(lines)
    visitor.visit(tree)
    return visitor.findings


def cmd_audit(args: argparse.Namespace) -> int:
    script_id = args.script

    # Resolve script path
    script_path = _resolve_gold_script(script_id)
    if not script_path:
        print(f'ERROR: script {script_id!r} not found under {_GOLD_ROOT}')
        return 1

    print(f'COMP-PERF VECTORIZE-AUDIT: {script_id}')
    print(f'  Script: {script_path.relative_to(_WORKSPACE)}')

    findings = _audit_script(script_path)

    warns = [f for f in findings if f['severity'] == 'WARN']
    infos = [f for f in findings if f['severity'] == 'INFO']

    if not findings:
        print('  PASS: no vectorize opportunities detected')
    else:
        print(f'\n  Findings: {len(findings)} ({len(warns)} WARN, {len(infos)} INFO)\n')
        print(f'  {"LINE":>5}  {"SEV":<5}  {"RULE":<28}  {"FN"}')
        print(f'  {"-"*5}  {"-"*5}  {"-"*28}  {"-"*30}')
        for f in sorted(findings, key=lambda x: (x['severity'] != 'WARN', x['line'])):
            print(f'  {f["line"]:>5}  {f["severity"]:<5}  {f["rule"]:<28}  {f["fn"]}')
            print(f'         snippet: {f["snippet"][:90]}')
            print(f'         detail:  {f["detail"][:90]}')
            print(f'         sketch:  {f["refactor_sketch"][:100]}')
            print()

    # Write manifest
    _VECTORIZE_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = _VECTORIZE_DIR / f'{script_id}.yaml'
    yaml_lines = [
        f'script_id: {script_id}',
        f'script_path: {script_path.relative_to(_WORKSPACE)}',
        f'total_findings: {len(findings)}',
        f'warn_count: {len(warns)}',
        f'findings:',
    ]
    for f in findings:
        yaml_lines.append(f'  - rule: {f["rule"]}')
        yaml_lines.append(f'    line: {f["line"]}')
        yaml_lines.append(f'    fn: {f["fn"]}')
        yaml_lines.append(f'    severity: {f["severity"]}')
        yaml_lines.append(f'    detail: {repr(f["detail"][:120])}')
        yaml_lines.append(f'    refactor_sketch: {repr(f["refactor_sketch"][:150])}')
    manifest_path.write_text('\n'.join(yaml_lines) + '\n', encoding='utf-8')
    print(f'  Manifest: {manifest_path.relative_to(_WORKSPACE)}')

    return 1 if warns else 0


def cmd_chain(args: argparse.Namespace) -> int:
    """Chain-wide vectorize audit: all gold scripts, ranked by finding count."""
    print('COMP-PERF VECTORIZE-AUDIT --chain')
    scripts = sorted(_GOLD_ROOT.glob('*.py'))
    print(f'  Scanning {len(scripts)} gold scripts...')

    all_results: list[tuple[Path, list[dict]]] = []
    for sp in scripts:
        findings = _audit_script(sp)
        if findings:
            all_results.append((sp, findings))

    # Sort by WARN count descending
    all_results.sort(key=lambda x: -sum(1 for f in x[1] if f['severity'] == 'WARN'))

    total_warns = sum(sum(1 for f in fs if f['severity'] == 'WARN') for _, fs in all_results)
    print(f'  {len(all_results)} scripts with findings, {total_warns} total WARNs\n')

    if all_results:
        print(f'  {"SCRIPT":<40}  {"WARN":>5}  {"INFO":>5}')
        print(f'  {"-"*40}  {"-"*5}  {"-"*5}')
        for sp, findings in all_results[:20]:
            warns = sum(1 for f in findings if f['severity'] == 'WARN')
            infos = sum(1 for f in findings if f['severity'] == 'INFO')
            print(f'  {sp.stem:<40}  {warns:>5}  {infos:>5}')
        if len(all_results) > 20:
            print(f'  ... and {len(all_results) - 20} more')

    # Write chain manifest
    _VECTORIZE_DIR.mkdir(parents=True, exist_ok=True)
    chain_path = _VECTORIZE_DIR / '_chain_inf.yaml'
    yaml_lines = [
        'pipeline: inf',
        f'scripts_with_findings: {len(all_results)}',
        f'total_warn: {total_warns}',
        'ranked:',
    ]
    for sp, findings in all_results:
        warns = sum(1 for f in findings if f['severity'] == 'WARN')
        yaml_lines.append(f'  - script: {sp.stem}')
        yaml_lines.append(f'    warn: {warns}')
        yaml_lines.append(f'    info: {sum(1 for f in findings if f["severity"] == "INFO")}')
    chain_path.write_text('\n'.join(yaml_lines) + '\n', encoding='utf-8')
    print(f'\n  Chain manifest: {chain_path.relative_to(_WORKSPACE)}')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='comp-perf',
        description='Performance vectorization opportunity audit for gold scripts'
    )
    sub = parser.add_subparsers(dest='subcmd')

    p_audit = sub.add_parser('vectorize-audit', help='Audit a single gold script')
    p_audit.add_argument('script', help='Script ID (e.g. INF_D_06.cash_drag) or path')
    p_audit.add_argument('--severity', choices=['warn', 'error'], default=None)

    p_chain = sub.add_parser('chain', help='Chain-wide vectorize audit')
    p_chain.add_argument('--pipeline', choices=['inf', 'bd'], default='inf')

    args = parser.parse_args()
    if args.subcmd == 'vectorize-audit':
        return cmd_audit(args)
    elif args.subcmd == 'chain':
        return cmd_chain(args)
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
