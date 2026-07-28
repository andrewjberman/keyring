"""Structured profile of every comp-* tool across Andrew's five axes.

  1 UNIVERSE          what population it covers
  2 RETRIEVAL         how it gets it (+ freshness semantics: derived-on-demand vs persisted,
                      incremental-write vs full-rewrite surface)
  3 DEFINITIVE        what it definitively covers inside that universe, and how we know
  4 WALLCLOCK         mechanical runtime (measured for the safe subset; variance noted)
  5 RETURN            output format, size, truncation point, and whether truncation can cut
                      semantically meaningful results

STATIC pass covers all 93. TIMED pass covers a VERIFIED READ-ONLY subset only -- some comp-tools
write (comp-system regen), and timing must never mutate the estate.
"""
import collections
import json
import os
import re

TOOLS = sorted(t for t in os.listdir('.tools') if t.startswith('comp-'))
SLASH = '\\'


def read(p):
    try:
        return open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        return ''


PATH_RE = re.compile(r'(org/modules/[A-Za-z0-9_/]+\.py)')
JOIN_RE = re.compile(r'os\.path\.join\(([^)]*)\)')
SIB_RE = re.compile(r'dirname[^)]*\)[/"\s]*([A-Za-z0-9_.\-]+\.py)')


def engines_for(src):
    out = set()
    for m in PATH_RE.finditer(src):
        if os.path.isfile(m.group(1)):
            out.add(m.group(1))
    for m in JOIN_RE.finditer(src):
        parts = re.findall(r'"([^"]+)"', m.group(1))
        if parts:
            cand = '/'.join(parts)
            for base in ('', 'org/modules/graph/', 'org/modules/'):
                p = base + cand
                if p.endswith('.py') and os.path.isfile(p):
                    out.add(p.replace(SLASH, '/'))
    for m in SIB_RE.finditer(src):
        p = os.path.join('.tools', m.group(1)).replace(SLASH, '/')
        if os.path.isfile(p):
            out.add(p)
    return out


# --- axis 2: retrieval primitive + its FRESHNESS SEMANTICS -------------------------------
PRIM = [
    ('GIT',       re.compile(r'ls-files|--name-only|rev-parse|git log'),
     'derived-on-demand from git; NEVER stale (git IS the write history)'),
    ('FS-WALK',   re.compile(r'os\.walk|\.rglob\(|glob\.glob|\.iterdir\('),
     'derived-on-demand from the working tree; reflects UNCOMMITTED state'),
    ('FS-GLOB',   re.compile(r'fnmatch'),
     'derived-on-demand, pattern-matched over the tree'),
    ('AWS-API',   re.compile(r'boto3|get_paginator|list_objects|list_functions|describe_instances'),
     'LIVE plane; fresh by construction, cost is latency not staleness'),
    ('SIMULATE',  re.compile(r'simulate[-_]principal[-_]policy'),
     'LIVE exercise; the only primitive that PROVES reach rather than reading a declaration'),
    ('GRAPH-DB',  re.compile(r'kuzu|globgrph|MATCH\s*\('),
     'PERSISTED derived DB -- STALENESS IS REAL; auto-refresh on HEAD-advance, read the provenance header'),
    ('REGISTRY',  re.compile(r'yaml\.safe_load|graph-call-manifest|comp-coverage-map|tools_index'),
     'PERSISTED authored artifact -- stale iff the author did not update it; gate-enforced where a gate exists'),
    ('AST',       re.compile(r'ast\.(parse|walk|NodeVisitor)'),
     'derived-on-demand from source at the READ vintage'),
    ('SQL/TRINO', re.compile(r'trino|athena', re.I),
     'LIVE federation; in-VPC one-shot, ~3-4 min/call'),
    ('SUBPROC',   re.compile(r'subprocess[^\n]{0,60}comp-[a-z]'),
     'delegates -- inherits the freshness of the tool it calls'),
]

# --- axis 5: truncation / bounding defaults -------------------------------------------
TRUNC = [
    ('--top N',      re.compile(r'add_argument\(\s*["\']--top')),
    ('--limit N',    re.compile(r'add_argument\(\s*["\']--limit')),
    ('--max N',      re.compile(r'add_argument\(\s*["\']--max')),
    ('head slice',   re.compile(r'\[:\s*\d{1,4}\s*\]')),
    ('MaxKeys',      re.compile(r'MaxKeys\s*=\s*\d+')),
    ('max_results',  re.compile(r'max_results|MaxItems|max_items')),
    ('json out',     re.compile(r'--json|json\.dump')),
]
DENOM_DECL = re.compile(r'denominator|of\s+\{?\w*total|showing|swept:|scanned\s', re.I)

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
    prims = [(n, fr) for n, rx, fr in PRIM if rx.search(full)]
    trunc = [n for n, rx in TRUNC if rx.search(full)]
    rows.append({
        'tool': t,
        'engines': sorted(seen),
        'primitives': [p[0] for p in prims],
        'freshness': [p[1] for p in prims],
        'bounding': trunc,
        'declares_denominator': bool(DENOM_DECL.search(full)),
        'src_bytes': len(full),
    })

print("=== STATIC PROFILE -- DENOMINATOR %d comp-* tools ===" % len(rows))
noprim = [r['tool'] for r in rows if not r['primitives']]
print("  classified: %d | no-primitive: %d %s" % (len(rows) - len(noprim), len(noprim), noprim))
print("\n  AXIS 5 -- BOUNDING / TRUNCATION defaults:")
bc = collections.Counter(b for r in rows for b in r['bounding'])
for k, v in bc.most_common():
    print("    %-14s %3d tools" % (k, v))
nb = [r['tool'] for r in rows if not r['bounding']]
print("    %-14s %3d tools  <-- UNBOUNDED: no limit arg, no slice" % ('(none)', len(nb)))
dd = sum(1 for r in rows if r['declares_denominator'])
print("\n  AXIS 5 -- DENOMINATOR DECLARED IN OUTPUT: %d of %d (%.0f%%)"
      % (dd, len(rows), 100.0 * dd / len(rows)))
print("    >> the other %d bound their output WITHOUT saying what it is bounded FROM" % (len(rows) - dd))

out = os.path.join(os.environ.get('TEMP', '.'), 'tool_profile.json')
json.dump(rows, open(out, 'w'), indent=1)
print("\n  rows -> %s" % out)
