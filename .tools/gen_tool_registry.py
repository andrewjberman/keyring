"""Build the tool registry: sources + overrides -> TOOL_MASTER.yaml -> tool_index.py

ARCHITECTURE (Andrew-direct 2026-07-28, framework C-for-authorship + B-for-delivery):

  DERIVE EVERYTHING a machine can infer; hand-author only what it cannot.
  Hand-authored surface is TWO fields -- `concern` and `canonical_call` -- in tool_overrides.yaml.
  Everything else (state, derived, denominator_construction, excludes, control, cost) is derived
  from source or measured.

  sources + overrides  ->  gen  ->  org/modules/graph/TOOL_MASTER.yaml   (HEAVY, everything)
                                ->  .tools/tool_index.py                 (LIGHT, importable, no parse)

WHY A COMPILED PYTHON MODULE AND NOT YAML: comp-which re-parses 133KB of YAML per call --
yaml.safe_load x10, ~97% of call time (0.8.0_AE_CloudComp~B, 2026-07-24, cProfile). Anything on the
hot path that parses YAML loses. An import costs ~ms.

STALENESS GUARD: tool_index.py embeds MASTER_SHA256 of the master it was compiled from. A reader
that cares must compare. The compiled index is PERSISTED+derived in our own taxonomy, so it gets the
same discipline we impose on everything else -- it must be able to know it is stale.
"""
import hashlib
import json
import os

import yaml

PROFILE = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/tool_profile.json'
CLASSIFICATION = '.tools/TOOL_CLASSIFICATION.yaml'
COVERAGE_MAP = 'org/modules/graph/comp-coverage-map.yaml'
MANIFEST = 'org/modules/graph/graph-call-manifest.yaml'
OVERRIDES = '.tools/tool_overrides.yaml'
MASTER = 'org/modules/graph/TOOL_MASTER.yaml'
INDEX = '.tools/tool_index.py'

COST_BANDS = [(1.0, 'SUB_SECOND'), (10.0, 'SECONDS'), (60.0, 'TENS_OF_SECONDS'), (1e9, 'MINUTES')]
# measured this session; others inherit their primitive's band
MEASURED = {'comp-coverage-check': 0.34, 'comp-which': 1.07, 'comp-grep': 1.45,
            'comp-glob': 1.63, 'comp-heat': 2.50, 'comp-clobber': 22.65, 'comp-fedobs': 3.41}
PRIM_BAND = {'REGISTRY': 'SUB_SECOND', 'GIT': 'SECONDS', 'FS-GLOB': 'SECONDS', 'AST': 'SECONDS',
             'AWS-API': 'SECONDS', 'GRAPH-DB': 'SECONDS', 'FS-WALK': 'TENS_OF_SECONDS',
             'SIMULATE': 'MINUTES', 'SQL/TRINO': 'MINUTES', 'SUBPROC': 'UNKNOWN'}


def load(p, default=None):
    if not os.path.isfile(p):
        return default
    with open(p, encoding='utf-8', errors='replace') as f:
        return yaml.safe_load(f) if p.endswith(('.yaml', '.yml')) else json.load(f)


def band_for(tool, prims):
    if tool in MEASURED:
        s = MEASURED[tool]
        return next(b for lim, b in COST_BANDS if s < lim)
    for p in ('SQL/TRINO', 'SIMULATE', 'FS-WALK', 'GRAPH-DB', 'AWS-API', 'GIT', 'REGISTRY'):
        if p in prims:
            return PRIM_BAND[p]
    return 'UNKNOWN'


def bootstrap_overrides(classification):
    """Seed the two human fields from EXISTING authored registries -- never invent them."""
    cm = load(COVERAGE_MAP, {}) or {}
    mf = load(MANIFEST, {}) or {}
    concern, call = {}, {}
    for section in ('tools', 'meta_tools'):
        for row in (cm.get(section) or []):
            if isinstance(row, dict) and row.get('tool'):
                if row.get('concern'):
                    concern[row['tool']] = row['concern']
    ents = mf.get('entries') or []
    if isinstance(ents, dict):
        ents = list(ents.values())
    for e in ents:
        if isinstance(e, dict) and e.get('tool') and e.get('canonical_call'):
            t = str(e['tool']).split()[0]
            call.setdefault(t, e['canonical_call'])
    out = {}
    for tool in classification:
        rec = {}
        if concern.get(tool):
            rec['concern'] = concern[tool]
        if call.get(tool):
            rec['canonical_call'] = call[tool]
        if rec:
            out[tool] = rec
    return out, len(concern), len(call)


def main():
    cls_doc = load(CLASSIFICATION) or {}
    classification = cls_doc.get('tools') or {}
    profile = {r['tool']: r for r in (load(PROFILE) or [])}

    ov = load(OVERRIDES)
    seeded = False
    if ov is None:
        ov, nc, ncall = bootstrap_overrides(classification)
        with open(OVERRIDES, 'w', encoding='utf-8') as f:
            yaml.safe_dump({
                'doc': 'THE ONLY HAND-AUTHORED TOOL FIELDS. Everything else is derived by '
                       'gen_tool_registry.py. Seeded from comp-coverage-map (concern) and '
                       'graph-call-manifest (canonical_call) -- never invented.',
                'tools': ov}, f, sort_keys=False, width=100)
        seeded = True
        print('SEEDED %s from existing registries: %d concern, %d canonical_call' % (OVERRIDES, nc, ncall))
    else:
        ov = ov.get('tools') or {}

    master_tools = {}
    for tool, c in classification.items():
        p = profile.get(tool, {})
        o = ov.get(tool, {}) if isinstance(ov, dict) else {}
        prims = c.get('primitives', [])
        master_tools[tool] = {
            'concern': o.get('concern'),
            'canonical_call': o.get('canonical_call'),
            'state': c.get('state'),
            'derived': c.get('derived'),
            'refresh_mechanism': c.get('refresh_mechanism'),
            'refresh_is_incremental': c.get('refresh_is_incremental'),
            'denominator_construction': c.get('denominator_construction'),
            'knows_own_denominator': c.get('denominator_knowable_up_front'),
            'declares_denominator_in_output': c.get('declares_denominator_in_output'),
            'control_established': c.get('control_established'),
            'universe': c.get('universe'),
            'excludes': c.get('excludes', []),
            'cost_band': band_for(tool, prims),
            'primitives': prims,
            'engines': p.get('engines', []),
            'bounding': c.get('bounding', []),
        }

    master = {
        'schema_version': '1.0',
        'authority': 'Andrew-direct 2026-07-28 -- one heavy master, one light compiled index',
        'generated_by': '.tools/gen_tool_registry.py -- DO NOT HAND-EDIT',
        'hand_authored_surface': 'ONLY .tools/tool_overrides.yaml (concern + canonical_call). '
                                 'Every other field is derived from source or measured.',
        'inventory_source_of_truth': 'org/modules/graph/comp-coverage-map.yaml (CTO ruling #1) -- '
                                     'this master does not supersede it, it composes with it.',
        'counts': {'tools': len(master_tools)},
        'tools': dict(sorted(master_tools.items())),
    }
    with open(MASTER, 'w', encoding='utf-8') as f:
        yaml.safe_dump(master, f, sort_keys=False, width=100, default_flow_style=False)
    master_sha = hashlib.sha256(open(MASTER, 'rb').read()).hexdigest()

    # ---- compile the LIGHT card: 8 decision fields, importable, no parse ----
    CARD = ('concern', 'canonical_call', 'state', 'denominator_construction',
            'control_established', 'excludes', 'cost_band', 'knows_own_denominator')
    cards = {t: {k: v[k] for k in CARD if v.get(k) is not None} for t, v in master_tools.items()}
    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write('"""GENERATED by .tools/gen_tool_registry.py -- DO NOT EDIT.\n\n'
                'The LIGHT card: the 8 fields an agent needs to DECIDE. Import, never parse --\n'
                'comp-which re-parsing 133KB of YAML per call was ~97%% of its runtime.\n'
                'Full detail lives in org/modules/graph/TOOL_MASTER.yaml.\n\n'
                'STALENESS: MASTER_SHA256 is the master this was compiled from. A reader that cares\n'
                'MUST compare against the live master -- this file is PERSISTED+derived and must be\n'
                'able to know it is stale.\n"""\n')
        f.write('MASTER_PATH = %r\n' % MASTER)
        f.write('MASTER_SHA256 = %r\n\n' % master_sha)
        # repr(), NOT json.dumps() -- json emits `true`/`false`, which are not Python literals and
        # produce a file that WRITES fine and FAILS ON IMPORT. Caught by importing it, not by reading it.
        import pprint
        f.write('TOOLS = ')
        f.write(pprint.pformat(cards, width=118, sort_dicts=True))
        f.write('\n\n\ndef is_stale():\n')
        f.write('    """True if TOOL_MASTER.yaml has changed since this index was compiled."""\n')
        f.write('    import hashlib as _h\n')
        f.write('    import os as _o\n')
        f.write('    if not _o.path.isfile(MASTER_PATH):\n        return True\n')
        f.write('    with open(MASTER_PATH, "rb") as fh:\n')
        f.write('        return _h.sha256(fh.read()).hexdigest() != MASTER_SHA256\n')

    print('WROTE %s  (%d tools)' % (MASTER, len(master_tools)))
    print('WROTE %s  (card = %d fields)' % (INDEX, len(CARD)))
    print('  master sha256 : %s' % master_sha[:16])
    print('  master bytes  : %d' % os.path.getsize(MASTER))
    print('  index  bytes  : %d  (%.0f%% of master)'
          % (os.path.getsize(INDEX), 100.0 * os.path.getsize(INDEX) / os.path.getsize(MASTER)))
    if seeded:
        print('  NOTE: overrides seeded this run -- review .tools/tool_overrides.yaml')


if __name__ == '__main__':
    main()
