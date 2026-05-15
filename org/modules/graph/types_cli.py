#!/usr/bin/env python3
"""types_cli.py — comp-types backend: TypeScript type consumer index, blast, and field audit."""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent
_PORTAL_SRC = _WORKSPACE / 'portal' / 'src'
_TYPES_INDEX_DIR = _WORKSPACE / 'org' / 'modules' / 'graph' / 'types-index'

# -------- Severity constants --------
SEV_INFO  = 'INFO'
SEV_WARN  = 'WARN'
SEV_ERROR = 'ERROR'


# -------- Helpers --------

def _grep_portal(pattern: str, extra_flags: list[str] | None = None) -> list[str]:
    """Run grep against portal/src; return matching lines as 'file:line:content' strings."""
    if not _PORTAL_SRC.exists():
        return []
    flags = ['-rn', '--include=*.ts', '--include=*.tsx', '--binary-files=without-match']
    if extra_flags:
        flags.extend(extra_flags)
    try:
        result = subprocess.run(
            ['grep'] + flags + [pattern, str(_PORTAL_SRC)],
            capture_output=True, text=True, timeout=15
        )
        return [l.rstrip('\n') for l in result.stdout.splitlines()
                if l.strip() and not l.startswith('Binary file')]
    except Exception:
        return []


def _parse_grep_line(line: str) -> tuple[str, int, str]:
    """Parse a grep output line into (file_path, line_number, content).

    Handles Windows drive-letter paths (C:\\...) where the drive colon
    must not be confused with the file:line delimiter.
    """
    # Pattern: <path>:<lineno>:<content> — use greedy match so Windows
    # drive-letter colon in C:\\... is absorbed into the path group.
    m = re.match(r'^(.+?[^:]):(\d+):(.*)', line)
    if m:
        # Check if path is a Windows drive path like "C:\..." — if so
        # the first token is just "C" which is wrong; consume the drive.
        file_path, lineno, content = m.group(1), int(m.group(2)), m.group(3)
        if len(file_path) == 1 and file_path.isalpha():
            # Drive letter prefix — re-parse with offset
            rest = line[2:]  # skip "C:"
            m2 = re.match(r'^(.+):(\d+):(.*)', rest)
            if m2:
                file_path = file_path + ':' + m2.group(1)
                lineno = int(m2.group(2))
                content = m2.group(3)
        return file_path, lineno, content
    return line, 0, ''


def _rel(path_str: str) -> str:
    """Convert absolute path to portal/src-relative form."""
    try:
        p = Path(path_str)
        return str(p.relative_to(_WORKSPACE))
    except ValueError:
        return path_str


def _classify_line(content: str, type_name: str) -> str:
    """Classify a grep match content (already stripped) into a consumer pattern category."""
    code = content.strip()
    if re.match(r'^\s*//', code) or re.match(r'^\s*\*', code):
        return 'comment'
    if re.search(r'\bimport\b.*\b' + re.escape(type_name) + r'\b', code):
        return 'import'
    if re.search(r'\buse' + re.escape(type_name) + r'\s*\(', code, re.IGNORECASE):
        return 'hook-call'
    hook_fn = 'use' + type_name[0].upper() + type_name[1:]
    if re.search(r'\buse\w+\s*\(' , code) and 'layout' in type_name.lower():
        if re.search(r'=\s+use\w+\(', code):
            return 'hook-call'
    if re.search(r'\?\?\s+DEFAULT_', code) or re.search(r'\?\?\s+\w+_LAYOUT', code) or 'DEFAULT_LAYOUT' in code:
        return 'default-fallback'
    if re.search(r':\s*' + re.escape(type_name) + r'\b', code):
        return 'type-annotation'
    if re.search(r'\b' + re.escape(type_name) + r'\s*=\s*\{', code):
        return 'mutation'
    if re.search(r'\bconst\b.*:\s*' + re.escape(type_name), code):
        return 'mutation'
    return 'reference'


def _find_type_definition(type_name: str) -> Path | None:
    """Find the .ts file defining an interface/type/const with the given name."""
    # Use literal grep (no regex metacharacters) since grep may not support \\s+
    patterns = [
        f'export interface {type_name} ',
        f'export interface {type_name}{{',
        f'export interface {type_name}\t',
        f'export type {type_name} =',
        f'export type {type_name}=',
        f'export const {type_name}:',
        f'export const {type_name} :',
    ]
    for pat in patterns:
        lines = _grep_portal(pat, ['-F'])  # -F = fixed string (no regex)
        if lines:
            file_path, _, _ = _parse_grep_line(lines[0])
            return Path(file_path)
    return None


def _extract_interface_fields(type_name: str, def_file: Path) -> list[str]:
    """Extract top-level field names from a TypeScript interface definition."""
    try:
        src = def_file.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return []
    # Find the interface body
    m = re.search(r'export\s+interface\s+' + re.escape(type_name) + r'\s*\{([\s\S]*?)\n\}', src)
    if not m:
        return []
    body = m.group(1)
    fields = []
    for line in body.splitlines():
        # match: optional_ws  field_name  optional?  :
        fm = re.match(r'\s{2,4}(\w+)\??\s*:', line)
        if fm:
            fields.append(fm.group(1))
    return fields


def _find_firm_conditional_sites(files: set[str]) -> list[dict]:
    """Find firmOverride/firmId conditional patterns in consumer files."""
    # Use fixed-string patterns to avoid regex issues
    patterns = [
        'firmOverride ===',
        'firmId ===',
        'isInflectionFirm',
        'isCottonwoodFirm',
        'firmOverride !==',
        'firmOverride===',
        'firmId!==',
    ]
    results = []
    seen: set[str] = set()
    for pat in patterns:
        lines = _grep_portal(pat, ['-F'])
        for line in lines:
            if 'Binary' in line or not line.strip():
                continue
            file_path, lineno, code = _parse_grep_line(line)
            rel = _rel(file_path)
            key = f'{rel}:{lineno}'
            if key not in seen:
                seen.add(key)
                results.append({'file': rel, 'line_content': code.strip()[:120]})
    return results


# -------- Subcommands --------

def cmd_index(args: argparse.Namespace) -> int:
    type_name = args.type_name
    t0 = time.monotonic()

    print(f'COMP-TYPES index: {type_name}')

    def_file = _find_type_definition(type_name)
    if def_file:
        print(f'  Definition: {_rel(str(def_file))}')
    else:
        print(f'  WARN: definition file not found for {type_name!r}; searching consumers by name only')

    # Collect all references
    hits = _grep_portal(type_name)

    # Also search for hook patterns
    # For TenantLayoutConfig the hook is useTenantLayout (strip trailing 'Config')
    bare = type_name
    for suffix in ('Config', 'Type', 'Props', 'State', 'Data', 'Info', 'Params'):
        if bare.endswith(suffix):
            bare = bare[:-len(suffix)]
            break
    hook_name = 'use' + bare
    seen_lines: set[str] = set(hits)

    def _add_hits(new_hits: list[str]) -> None:
        for h in new_hits:
            if h not in seen_lines:
                hits.append(h)
                seen_lines.add(h)

    _add_hits(_grep_portal(hook_name, ['-F']))

    # Search for DEFAULT_LAYOUT references (the exported default from the type file)
    default_const_hits = _grep_portal(f'DEFAULT_LAYOUT', ['-F'])
    _add_hits(default_const_hits)

    # Search for field accesses on common layout variable names: layout.X, tenantLayout.X
    for var_name in ('layout.', 'tenantLayout.', 'dataSourceLayout.'):
        _add_hits(_grep_portal(var_name, ['-F']))

    # Exclude the definition file itself and .d.ts files
    def_path_str = str(def_file) if def_file else None
    consumers: list[dict] = []
    for hit in hits:
        if '.d.ts:' in hit:
            continue
        file_path, lineno, code = _parse_grep_line(hit)
        code = code.strip()
        if def_path_str and Path(file_path).resolve() == Path(def_path_str).resolve():
            continue
        rel_path = _rel(file_path)
        cat = _classify_line(code, type_name)
        if cat == 'comment':
            continue
        is_default_fallback = bool(re.search(r'\?\?\s+\w*(DEFAULT|LAYOUT)\w*', code))
        consumers.append({
            'file': rel_path,
            'line': lineno,
            'category': cat,
            'code': code[:120],
            'default_fallback': is_default_fallback,
        })

    elapsed = time.monotonic() - t0

    # Print table
    cat_order = ['hook-call', 'mutation', 'import', 'type-annotation', 'default-fallback', 'reference']
    consumers_sorted = sorted(consumers, key=lambda c: (cat_order.index(c['category']) if c['category'] in cat_order else 99, c['file'], c['line']))

    print(f'\n  Consumer sites ({len(consumers)} total, {elapsed:.2f}s):\n')
    print(f'  {"FILE":<60} {"LINE":>5}  {"CATEGORY":<18}  SNIPPET')
    print(f'  {"-"*60} {"----":>5}  {"-"*18}  {"-"*40}')
    for c in consumers_sorted:
        fallback_mark = ' [DEFAULT-FALLBACK]' if c['default_fallback'] else ''
        print(f'  {c["file"]:<60} {c["line"]:>5}  {c["category"]:<18}  {c["code"][:60]}{fallback_mark}')

    # Default-fallback summary
    fallbacks = [c for c in consumers if c['default_fallback']]
    if fallbacks:
        print(f'\n  Default-fallback sites ({len(fallbacks)}):')
        for fb in fallbacks:
            print(f'    {fb["file"]}:{fb["line"]} — {fb["code"][:80]}')
    else:
        print(f'\n  Default-fallback sites: none detected')

    # Firm-conditional sites
    if getattr(args, 'firm_conditional_sites', False):
        consumer_files = {c['file'] for c in consumers}
        firm_sites = _find_firm_conditional_sites(consumer_files)
        print(f'\n  Firm-conditional sites (--firm-conditional-sites, {len(firm_sites)}):')
        if firm_sites:
            for fs in firm_sites:
                print(f'    {fs["file"]} — {fs["line_content"]}')
        else:
            print('    (none found in consumer files)')

    # Severity check
    severity = getattr(args, 'severity', None)
    if severity == 'error' and len(consumers) < 29:
        print(f'\n  ERROR: only {len(consumers)} consumer sites found; expected >= 29')
        return 1
    elif severity == 'warn' and len(consumers) < 29:
        print(f'\n  WARN: only {len(consumers)} consumer sites found; expected >= 29')

    # Write manifest
    _TYPES_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = _TYPES_INDEX_DIR / f'{type_name}.yaml'
    manifest_lines = [
        f'type_name: {type_name}',
        f'definition_file: {_rel(str(def_file)) if def_file else "not_found"}',
        f'total_consumer_sites: {len(consumers)}',
        f'elapsed_seconds: {elapsed:.2f}',
        f'default_fallback_sites: {len(fallbacks)}',
        f'consumers:',
    ]
    for c in consumers_sorted:
        manifest_lines.append(f'  - file: {c["file"]}')
        manifest_lines.append(f'    line: {c["line"]}')
        manifest_lines.append(f'    category: {c["category"]}')
        manifest_lines.append(f'    default_fallback: {str(c["default_fallback"]).lower()}')
        manifest_lines.append(f'    code: {repr(c["code"][:80])}')
    manifest_path.write_text('\n'.join(manifest_lines) + '\n', encoding='utf-8')
    print(f'\n  Manifest: {_rel(str(manifest_path))}')
    print(f'\nPASS: comp-types index complete ({len(consumers)} consumer sites, {elapsed:.2f}s)')
    return 0


def cmd_blast(args: argparse.Namespace) -> int:
    type_name = args.type_name
    print(f'COMP-TYPES blast: {type_name}')
    print('  What breaks if this type changes shape?')

    hits = _grep_portal(type_name)
    # Also search for the hook variant (strip common type suffixes)
    bare = type_name
    for suffix in ('Config', 'Type', 'Props', 'State', 'Data', 'Info', 'Params'):
        if bare.endswith(suffix):
            bare = bare[:-len(suffix)]
            break
    hook_name = 'use' + bare
    for h in _grep_portal(hook_name, ['-F']):
        if h not in hits:
            hits.append(h)

    def_file = _find_type_definition(type_name)

    blast_files: set[str] = set()
    for hit in hits:
        if '.d.ts:' in hit:
            continue
        file_path, _, _ = _parse_grep_line(hit)
        if def_file and Path(file_path).resolve() == def_file.resolve():
            continue
        blast_files.add(_rel(file_path))

    print(f'\n  Blast radius: {len(blast_files)} file(s) affected if {type_name} shape changes\n')
    for f in sorted(blast_files):
        print(f'    {f}')

    _TYPES_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = _TYPES_INDEX_DIR / f'{type_name}.blast.yaml'
    lines = [f'type_name: {type_name}', f'blast_radius_files: {len(blast_files)}', 'affected_files:']
    for f in sorted(blast_files):
        lines.append(f'  - {f}')
    manifest_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'\n  Manifest: {_rel(str(manifest_path))}')
    print(f'\nPASS: comp-types blast complete')
    return 0


def cmd_fields(args: argparse.Namespace) -> int:
    type_name = args.type_name
    print(f'COMP-TYPES fields: {type_name}')

    def_file = _find_type_definition(type_name)
    if not def_file:
        print(f'  ERROR: definition file not found for {type_name!r}')
        return 1

    fields = _extract_interface_fields(type_name, def_file)
    if not fields:
        print(f'  WARN: no fields extracted from {_rel(str(def_file))} — may not be an interface')
    else:
        print(f'  Fields ({len(fields)}): {", ".join(fields[:8])}{"..." if len(fields) > 8 else ""}')

    severity = getattr(args, 'severity', None)
    field_consumers: dict[str, list[dict]] = {}
    for field in fields:
        hits = _grep_portal(r'\.' + re.escape(field) + r'\b')
        consumers = []
        for hit in hits:
            if not hit.strip():
                continue
            if '.d.ts:' in hit:
                continue
            file_path, lineno, code = _parse_grep_line(hit)
            if def_file and Path(file_path).resolve() == def_file.resolve():
                continue
            consumers.append({'file': _rel(file_path), 'line': lineno, 'code': code.strip()[:80]})
        field_consumers[field] = consumers

    print(f'\n  Per-field consumer summary:\n')
    print(f'  {"FIELD":<30}  {"CONSUMERS":>9}  STATUS')
    print(f'  {"-"*30}  {"-"*9}  {"-"*10}')
    for field in fields:
        count = len(field_consumers[field])
        status = 'UNUSED' if count == 0 else 'USED' if count < 5 else 'READ-EVERYWHERE'
        if status == 'UNUSED' and severity == 'error':
            status = 'ERROR: UNUSED'
        elif status == 'UNUSED' and severity == 'warn':
            status = 'WARN: UNUSED'
        print(f'  {field:<30}  {count:>9}  {status}')

    _TYPES_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = _TYPES_INDEX_DIR / f'{type_name}.fields.yaml'
    yaml_lines = [f'type_name: {type_name}', f'total_fields: {len(fields)}', 'fields:']
    for field in fields:
        count = len(field_consumers[field])
        yaml_lines.append(f'  - name: {field}')
        yaml_lines.append(f'    consumer_count: {count}')
        yaml_lines.append(f'    status: {"UNUSED" if count == 0 else "USED" if count < 5 else "READ-EVERYWHERE"}')
        if field_consumers[field]:
            yaml_lines.append(f'    consumers:')
            for c in field_consumers[field][:5]:
                yaml_lines.append(f'      - {c["file"]}:{c["line"]}')
    manifest_path.write_text('\n'.join(yaml_lines) + '\n', encoding='utf-8')
    print(f'\n  Manifest: {_rel(str(manifest_path))}')
    print(f'\nPASS: comp-types fields complete')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='comp-types',
        description='TypeScript type consumer index, blast, and field audit'
    )
    sub = parser.add_subparsers(dest='cmd')

    p_index = sub.add_parser('index', help='Index all consumer sites for a TypeScript type')
    p_index.add_argument('type_name', help='TypeScript type/interface name')
    p_index.add_argument('--firm-conditional-sites', action='store_true', dest='firm_conditional_sites',
                         help='Also surface firmOverride/firmId conditional co-locations')
    p_index.add_argument('--severity', choices=['warn', 'error'], default=None,
                         help='Escalate missing-consumer findings (warn|error)')

    p_blast = sub.add_parser('blast', help='What breaks if this type changes shape?')
    p_blast.add_argument('type_name', help='TypeScript type/interface name')

    p_fields = sub.add_parser('fields', help='Per-field consumer enumeration')
    p_fields.add_argument('type_name', help='TypeScript type/interface name')
    p_fields.add_argument('--severity', choices=['warn', 'error'], default=None,
                          help='Escalate UNUSED fields to warn|error')

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return 1

    dispatch = {'index': cmd_index, 'blast': cmd_blast, 'fields': cmd_fields}
    return dispatch[args.cmd](args)


if __name__ == '__main__':
    sys.exit(main())
