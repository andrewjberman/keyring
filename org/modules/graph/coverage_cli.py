#!/usr/bin/env python3
"""coverage_cli.py — comp-coverage backend: compiler-tools TO compliance audit."""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent
_COMP_LOG = _WORKSPACE / 'org' / 'compiler-tools-log.md'
_COVERAGE_DIR = _WORKSPACE / 'org' / 'modules' / 'graph' / 'coverage-report'

# Path glob patterns to classify TOs
# Each entry: (class_name, list of path fragment patterns)
_CLASSIFIERS = [
    ('FRONTEND', ['portal/', '.tsx', '.ts', 'frontend', 'component', 'portal/src']),
    ('GOLD',     ['scripts/gold/', 'scripts/silver/', 'scripts/bronze/', 'data/orion/', 'data/black_diamond/']),
    ('API',      ['infra/aws/lambda/', 'infra/aws/terraform/', 'lambda_function.py', '.tf']),
    ('DOC',      ['docs/', 'org/modules/', 'org/tier', 'org/threads/', '.md', 'CLAUDE.md']),
]

# TO status values that count as "completed" (searchable in log)
_COMPLETE_STATUSES = {'complete', 'done', 'closed'}

# Agents with gated TOs — classify any TO issued_to this agent as gated
_GATED_AGENTS = {
    '0.1.0_DE_MarketIntelligence', '0.4.0_DS_ClientPlatform', '0.4.2_RD_AdvisorIntelligence',
    '0.6.1_AE_PartnerETL', '0.7.0_AE_CloudOps', '1.0.0_SA_CTO', '2.0.0_SA_COO',
    '0.4.0_DE_DataEngineering', '0.4.1_RD_ModelPortfolios', '0.4.3_DE_DataEngineering',
    '0.5.0_DS_DataScience', '0.6.0_AE_Infrastructure',
}


def _classify_to(files_text: str, issued_to: str) -> str:
    """Classify a TO based on its <files> declarations."""
    if not files_text.strip():
        return 'EXEMPT'
    lower = files_text.lower()
    for class_name, patterns in _CLASSIFIERS:
        for pat in patterns:
            if pat.lower() in lower:
                return class_name
    # If no files declared or only org/doc files
    if all(pat.lower() in lower for pat in ['org/', 'docs/']):
        return 'EXEMPT'
    return 'DOC'


def _parse_to_files(xml_text: str) -> tuple[str, str, str, str, str]:
    """Parse TO XML for (id, status, issued_to, issued_by, files_block).

    Returns empty strings on parse failure.
    """
    def _tag(tag: str) -> str:
        m = re.search(rf'<{tag}>(.*?)</{tag}>', xml_text, re.DOTALL)
        return m.group(1).strip() if m else ''

    to_id = _tag('id')
    status = _tag('status')
    issued_to = _tag('issued_to')
    issued_by = _tag('issued_by')

    files_m = re.search(r'<files>(.*?)</files>', xml_text, re.DOTALL)
    files_text = files_m.group(1) if files_m else ''

    return to_id, status, issued_to, issued_by, files_text


def _load_comp_log_to_ids() -> set[str]:
    """Extract all TO IDs referenced in the compiler-tools log rows."""
    if not _COMP_LOG.exists():
        return set()
    ids: set[str] = set()
    for line in _COMP_LOG.read_text(encoding='utf-8', errors='ignore').splitlines():
        if not line.startswith('|'):
            continue
        parts = [p.strip() for p in line.split('|')]
        # Format: | DATE | AGENT | TO | TOOL | COMMAND | RESULT | NOTE |
        if len(parts) >= 5:
            to_field = parts[3]  # index 3 after leading empty from split
            if to_field and to_field != 'TO' and to_field != '-' and len(to_field) > 2:
                ids.add(to_field)
    return ids


def cmd_report(args: argparse.Namespace) -> int:
    gated_only = getattr(args, 'gated_only', False)
    by_agent = getattr(args, 'by_agent', False)
    pipeline = getattr(args, 'pipeline', None)

    print('COMP-COVERAGE: scanning TO corpus...')

    # Load comp log TO IDs
    logged_ids = _load_comp_log_to_ids()
    print(f'  Comp-log TO IDs found: {len(logged_ids):,}')

    # Walk all TO files
    to_files = list(_WORKSPACE.glob('org/tier*/*/task_orders/*.md'))
    print(f'  TO files found: {len(to_files):,}')

    # Parse each TO
    records: list[dict] = []
    for to_path in sorted(to_files):
        try:
            text = to_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue

        # Filter out non-XML TOs (plain markdown)
        if '<task_order>' not in text and '<id>' not in text:
            # Try to extract id from filename
            fname = to_path.stem  # e.g. ADHC_DESIGN.026.de-tooltip
            parts = fname.split('.')
            to_id = parts[0] + '.' + parts[1] if len(parts) >= 2 else fname
            records.append({
                'id': to_id,
                'status': 'unknown',
                'issued_to': 'unknown',
                'issued_by': 'unknown',
                'to_class': 'DOC',
                'logged': to_id in logged_ids,
                'path': str(to_path),
            })
            continue

        to_id, status, issued_to, issued_by, files_text = _parse_to_files(text)
        if not to_id:
            continue

        to_class = _classify_to(files_text, issued_to)
        is_complete = status.lower() in _COMPLETE_STATUSES
        is_logged = to_id in logged_ids

        records.append({
            'id': to_id,
            'status': status,
            'issued_to': issued_to or 'unknown',
            'issued_by': issued_by or 'unknown',
            'to_class': to_class,
            'is_complete': is_complete,
            'logged': is_logged,
            'path': str(to_path),
        })

    # Filter
    if gated_only:
        records = [r for r in records if r['to_class'] not in ('EXEMPT', 'DOC')]
    if pipeline:
        records = [r for r in records if pipeline.lower() in r['id'].lower() or pipeline.lower() in r.get('path', '').lower()]

    completed = [r for r in records if r.get('is_complete')]
    logged_completed = [r for r in completed if r['logged']]

    raw_pct = (len(logged_completed) / len(completed) * 100) if completed else 0
    print(f'\n  Total TOs: {len(records):,}')
    print(f'  Completed TOs: {len(completed):,}')
    print(f'  Logged in comp-log: {len(logged_completed):,}')
    print(f'  Raw coverage: {raw_pct:.1f}%')

    # Per-class breakdown
    by_class: dict[str, dict] = defaultdict(lambda: {'total': 0, 'completed': 0, 'logged': 0})
    for r in records:
        cls = r['to_class']
        by_class[cls]['total'] += 1
        if r.get('is_complete'):
            by_class[cls]['completed'] += 1
        if r.get('is_complete') and r['logged']:
            by_class[cls]['logged'] += 1

    print(f'\n  {"CLASS":<12}  {"TOTAL":>6}  {"DONE":>6}  {"LOGGED":>7}  {"PCT":>6}')
    print(f'  {"-"*12}  {"-"*6}  {"-"*6}  {"-"*7}  {"-"*6}')
    for cls in ['FRONTEND', 'GOLD', 'API', 'DOC', 'EXEMPT']:
        d = by_class[cls]
        pct = (d['logged'] / d['completed'] * 100) if d['completed'] else 0
        print(f'  {cls:<12}  {d["total"]:>6}  {d["completed"]:>6}  {d["logged"]:>7}  {pct:>5.1f}%')

    # Outliers: completed gated TOs with 0 logged runs
    outliers = [r for r in completed if not r['logged'] and r['to_class'] not in ('EXEMPT', 'DOC')]
    if outliers:
        print(f'\n  Unlogged gated TOs ({len(outliers):,} outliers):')
        for r in sorted(outliers, key=lambda x: x['issued_to']):
            print(f'    {r["id"]:<40}  agent={r["issued_to"]:<30}  class={r["to_class"]}')

    # Per-agent compliance
    if by_agent:
        print(f'\n  PER-AGENT COMPLIANCE (completed gated TOs only):')
        by_agent_d: dict[str, dict] = defaultdict(lambda: {'done': 0, 'logged': 0})
        for r in completed:
            if r['to_class'] in ('EXEMPT', 'DOC'):
                continue
            agent = r['issued_to']
            by_agent_d[agent]['done'] += 1
            if r['logged']:
                by_agent_d[agent]['logged'] += 1
        ranked = sorted(by_agent_d.items(), key=lambda x: -(x[1]['logged'] / max(x[1]['done'], 1)))
        print(f'  {"AGENT":<40}  {"DONE":>5}  {"LOGGED":>7}  {"PCT":>6}')
        print(f'  {"-"*40}  {"-"*5}  {"-"*7}  {"-"*6}')
        for agent, d in ranked:
            pct = (d['logged'] / d['done'] * 100) if d['done'] else 0
            print(f'  {agent:<40}  {d["done"]:>5}  {d["logged"]:>7}  {pct:>5.1f}%')

    # Write REPORT.md
    _COVERAGE_DIR.mkdir(parents=True, exist_ok=True)
    report_path = _COVERAGE_DIR / 'REPORT.md'
    lines = [
        '# Compiler Tools Coverage Report',
        '',
        f'Generated: 2026-05-15 (AE 0.7, ADHC_COMPIL_V4.033)',
        '',
        f'## Summary',
        f'- Total TOs: {len(records):,}',
        f'- Completed: {len(completed):,}',
        f'- Logged in comp-log: {len(logged_completed):,}',
        f'- Raw coverage: {raw_pct:.1f}%',
        '',
        f'## By Class',
        '',
        f'| Class | Total | Done | Logged | % |',
        f'|-------|------:|-----:|-------:|--:|',
    ]
    for cls in ['FRONTEND', 'GOLD', 'API', 'DOC', 'EXEMPT']:
        d = by_class[cls]
        pct = (d['logged'] / d['completed'] * 100) if d['completed'] else 0
        lines.append(f'| {cls} | {d["total"]:,} | {d["completed"]:,} | {d["logged"]:,} | {pct:.1f}% |')

    if outliers:
        lines += ['', f'## Unlogged Gated TOs ({len(outliers):,})', '']
        for r in sorted(outliers, key=lambda x: x['issued_to']):
            lines.append(f'- `{r["id"]}` — {r["issued_to"]} ({r["to_class"]})')

    report_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    # Per-agent yamls
    per_agent_dir = _COVERAGE_DIR / 'per-agent'
    per_agent_dir.mkdir(exist_ok=True)
    by_agent_full: dict[str, list] = defaultdict(list)
    for r in completed:
        by_agent_full[r['issued_to']].append(r)
    for agent, agent_tos in by_agent_full.items():
        safe = re.sub(r'[^a-zA-Z0-9._-]', '_', agent)
        yaml_path = per_agent_dir / f'{safe}.yaml'
        gated = [r for r in agent_tos if r['to_class'] not in ('EXEMPT', 'DOC')]
        logged = [r for r in gated if r['logged']]
        pct = (len(logged) / len(gated) * 100) if gated else 0
        yaml_lines = [
            f'agent: {agent}',
            f'gated_done: {len(gated)}',
            f'gated_logged: {len(logged)}',
            f'compliance_pct: {pct:.1f}',
            f'unlogged:',
        ]
        for r in gated:
            if not r['logged']:
                yaml_lines.append(f'  - id: {r["id"]}')
                yaml_lines.append(f'    class: {r["to_class"]}')
        yaml_path.write_text('\n'.join(yaml_lines) + '\n', encoding='utf-8')

    print(f'\n  Report: {_COVERAGE_DIR.relative_to(_WORKSPACE)}/REPORT.md')
    print(f'  Per-agent: {len(by_agent_full)} manifests written')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='comp-coverage',
        description='Compiler-tools TO compliance audit'
    )
    sub = parser.add_subparsers(dest='subcmd')

    p_report = sub.add_parser('report', help='Generate compliance coverage report')
    p_report.add_argument('--by-agent', action='store_true', help='Show per-agent compliance ranking')
    p_report.add_argument('--gated-only', action='store_true', help='Only count gated-class TOs (drop EXEMPT/DOC)')
    p_report.add_argument('--pipeline', help='Filter by pipeline string in TO ID or path')

    args = parser.parse_args()
    if args.subcmd == 'report':
        return cmd_report(args)
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
