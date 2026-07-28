"""Resolve the ENUMERATION PRIMITIVE of every comp-* tool.

A tool's coverage universe is determined by the call that produces the population it reasons
over. This classifies all 93 comp-* executables by that primitive, following the three wrapper
delegation shapes (python _ENGINE, bash org/modules path, sibling .tools/ file) plus one
transitive hop. Read-only. Output feeds the `excludes:` field mechanically.
"""
import collections
import json
import os
import re

WS = os.getcwd()
TOOLS = sorted(t for t in os.listdir('.tools') if t.startswith('comp-'))


def read(p):
    try:
        return open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        return ''


PATH_RE = re.compile(r'(org/modules/[A-Za-z0-9_/]+\.py)')
JOIN_RE = re.compile(r'os\.path\.join\(([^)]*)\)')
SLASH = '\\'


def norm(p):
    return p.replace(SLASH, '/')


def engines_for(src):
    out = set()
    for m in PATH_RE.finditer(src):
        if os.path.isfile(m.group(1)):
            out.add(m.group(1))
    for m in JOIN_RE.finditer(src):
        parts = re.findall(r'"([^"]+)"', m.group(1))
        if not parts:
            continue
        cand = '/'.join(parts)
        for base in ('', 'org/modules/graph/', 'org/modules/'):
            p = base + cand
            if p.endswith('.py') and os.path.isfile(p):
                out.add(norm(p))
    return out


PRIM = [
    ('GIT',        re.compile(r'ls-files|--name-only|rev-parse|["\']log["\']|git log')),
    ('FS-WALK',    re.compile(r'os\.walk|\.rglob\(|glob\.glob|\.iterdir\(')),
    ('AWS-API',    re.compile(r'boto3|get_paginator|list_objects|list_functions|describe_instances')),
    ('REGISTRY',   re.compile(r'yaml\.safe_load|graph-call-manifest|comp-coverage-map|tools_index')),
    ('GRAPH-DB',   re.compile(r'kuzu|globgrph|MATCH\s*\(')),
    ('AST',        re.compile(r'ast\.(parse|walk|NodeVisitor)')),
    ('SUBPROC',    re.compile(r'subprocess[^\n]{0,60}comp-[a-z]')),
    ('SQL/TRINO',  re.compile(r'trino|athena|SELECT .* FROM', re.I)),
]

rows = []
for t in TOOLS:
    src = read(os.path.join('.tools', t))
    full = src
    engs = engines_for(src)
    seen = set(engs)
    for e in list(engs):
        es = read(e)
        full += '\n' + es
        for e2 in engines_for(es) - seen:
            seen.add(e2)
            full += '\n' + read(e2)
    hits = [n for n, rx in PRIM if rx.search(full)]
    rows.append({'tool': t, 'engines': sorted(seen), 'prims': hits, 'bytes': len(full)})

res = [r for r in rows if r['prims']]
unres = [r for r in rows if not r['prims']]
print("=== ENUMERATION-PRIMITIVE RESOLUTION -- DENOMINATOR %d comp-* tools ===" % len(TOOLS))
print("  RESOLVED   %d  (%.0f%%)" % (len(res), 100.0 * len(res) / len(TOOLS)))
print("  UNRESOLVED %d  (%.0f%%)" % (len(unres), 100.0 * len(unres) / len(TOOLS)))
c = collections.Counter(p for r in res for p in r['prims'])
print("\n  primitive distribution (a tool may carry >1):")
for k, v in c.most_common():
    print("    %-12s %3d" % (k, v))
withE = sum(1 for r in rows if r['engines'])
print("\n  engine resolution: %d of %d tools delegate to a resolvable engine" % (withE, len(TOOLS)))
out = os.path.join(os.environ.get('TEMP', '.'), 'prim_rows.json')
json.dump(rows, open(out, 'w'), indent=0)
print("  rows -> %s" % out)
if unres:
    print("\n  STILL UNRESOLVED (%d):" % len(unres))
    for r in unres:
        print("    %-28s engines=%d src_bytes=%d" % (r['tool'], len(r['engines']), r['bytes']))
