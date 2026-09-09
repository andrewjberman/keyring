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

# The suffix set norm_tool() strips, censused over BOTH population sides -- see norm_tool.
SUFFIXES_STRIPPED = ('.py', '.sh')

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


def population_from_map():
    """THE SOLE POPULATION AUTHORITY is comp-coverage-map.yaml (CTO ruling #1, reaffirmed 212335Z).

    This master is an ATTRIBUTE STORE and MUST NEVER be a population source -- a peer file that
    enumerates its own tool list becomes a 5th copy of the population and drifts. This estate has a
    MEASURED history of exactly that in exactly this domain (comp-tools.yaml: 28/29/~30/42/63/66).
    """
    cm = load(COVERAGE_MAP, {}) or {}
    pop = set()
    for section in ('tools', 'meta_tools'):
        for row in (cm.get(section) or []):
            if isinstance(row, dict) and row.get('tool'):
                pop.add(norm_tool(str(row['tool'])))
    return pop


def status_from_map():
    """TOOL-GRAIN LIFECYCLE from the SOLE authority (comp-coverage-map.yaml `status:`, declared in
    its schema.node_fields, NFRA_CLDGRPH CG-s-30).

    A tool that omits the key is `active` -- the DEFAULT is declared in the map's schema, and it is
    applied HERE rather than left as None so every generated row carries a value a consumer can
    reject on (A_VALUE_MUST_CARRY_ITS_CLAIM: an unpopulated provenance field drifts).

    THIS IS NOT A POPULATION READ. It is an ATTRIBUTE read over the same rows population_from_map()
    walks; the population still comes from that function alone.
    """
    cm = load(COVERAGE_MAP, {}) or {}
    out = {}
    for section in ('tools', 'meta_tools'):
        for row in (cm.get(section) or []):
            if isinstance(row, dict) and row.get('tool'):
                out[norm_tool(str(row['tool']))] = str(row.get('status') or 'active')
    return out


def norm_tool(name):
    """Canonical tool id. The map drops the file suffix; an on-disk listing keeps it.

    FIRST EXERCISE OF THE PARITY CHECK found both sides at EXACTLY 89 with 12 DIVERGENT MEMBERS --
    a count-equality check would have passed clean and said nothing. 5 of the 12 were this suffix
    convention alone. Normalising here is correct; hiding the divergence would not be.

    SUFFIX DOMAIN, CENSUSED (NFRA_CLDGRPH CG-s-28, 2026-09-09) -- a suffix set is a DECLARED
    DOMAIN, so it is measured on both sides rather than assumed:
      AUTHORITY org/modules/graph/comp-coverage-map.yaml -- 99 name(s), suffixes present: NONE.
      PROFILE   org/tier1_exec/.../tool_profile.json     -- 93 name(s), suffixes present: .py (6),
                .sh (1). No .cmd, no .ps1, no other suffix on either side.
    Stripping .py ALONE made comp-v5-composite-test.sh read as a FIFTH exclusion that is not a
    retirement (row NFRA_CLDGRPH-W2-S37): one tool spelled two ways, printed beside four real
    retirements. SUFFIXES_STRIPPED below is therefore MECE over the names that exist today; a NEW
    suffix is a RE-CENSUS of this constant, never a silent pass-through (an unstripped suffix does
    not lose a tool -- it splits one into two names and prints the second as an exclusion).
    """
    n = name.strip()
    for suffix in SUFFIXES_STRIPPED:
        if n.endswith(suffix):
            return n[:-len(suffix)]
    return n


class PopulationDivergence(RuntimeError):
    """Raised on ANY population divergence, either direction. Never a silent skip."""


def assert_population_parity(authority, mine):
    """FAIL LOUD, both directions (CTO ruling 212335Z). No silent skip, no continue."""
    missing = sorted(authority - mine)   # in the authority, absent from this master
    extra = sorted(mine - authority)     # in this master, absent from the authority
    if missing or extra:
        raise PopulationDivergence(
            'POPULATION DIVERGENCE vs %s (the SOLE population authority).\n'
            '  authority=%d  master=%d\n'
            '  IN AUTHORITY, MISSING FROM MASTER (%d): %s\n'
            '  IN MASTER, ABSENT FROM AUTHORITY (%d): %s\n'
            '  This master is an ATTRIBUTE STORE and must never source its own population.'
            % (COVERAGE_MAP, len(authority), len(mine), len(missing), missing[:20],
               len(extra), extra[:20]))
    return len(authority)


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

    # POPULATION comes from the AUTHORITY, never from this file's own inputs (CTO ruling 212335Z).
    authority = population_from_map()
    # TOOL-GRAIN LIFECYCLE from the same authority (CG-s-30). Attribute, not population.
    tool_status = status_from_map()

    master_tools = {}
    for tool_raw, c in classification.items():
        tool = norm_tool(tool_raw)
        p = profile.get(tool_raw, {})
        o = ov.get(tool_raw, ov.get(tool, {})) if isinstance(ov, dict) else {}
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
            'status': tool_status.get(tool, 'active'),
        }

    # NO SILENT SKIP (CTO ruling 212335Z, explicit). A tool in the authority that this generator
    # could not classify is EMITTED WITH AN EXPLICIT MARKER, never dropped -- dropping it is how a
    # population quietly shrinks. First exercise found 3 such tools being `continue`d away.
    for tool in sorted(authority - set(master_tools)):
        o = ov.get(tool, {}) if isinstance(ov, dict) else {}
        master_tools[tool] = {
            'concern': o.get('concern'),
            'canonical_call': o.get('canonical_call'),
            'classification_status': 'UNCLASSIFIED -- present in the population authority, no '
                                     'enumeration primitive resolved. NOT a claim that it covers '
                                     'nothing; a claim that this generator could not determine it.',
            'state': None, 'derived': None, 'denominator_construction': None,
            'knows_own_denominator': None, 'control_established': None,
            'universe': None, 'excludes': [], 'cost_band': 'UNKNOWN',
            'primitives': [], 'engines': [], 'bounding': [],
            'status': tool_status.get(tool, 'active'),
        }

    n_pop = assert_population_parity(authority, set(master_tools))

    master = {
        'schema_version': '1.0',
        'authority': 'Andrew-direct 2026-07-28 -- one heavy master, one light compiled index',
        'generated_by': '.tools/gen_tool_registry.py -- DO NOT HAND-EDIT',
        'hand_authored_surface': 'ONLY .tools/tool_overrides.yaml (concern + canonical_call). '
                                 'Every other field is derived from source or measured.',
        'inventory_source_of_truth': 'org/modules/graph/comp-coverage-map.yaml (CTO ruling #1) -- '
                                     'this master does not supersede it, it composes with it.',
        'population_authority': 'org/modules/graph/comp-coverage-map.yaml -- tools[] + meta_tools[]. '
                                'THIS FILE IS AN ATTRIBUTE STORE AND IS NEVER A POPULATION SOURCE '
                                '(CTO ruling 20260728T212335Z). gen_tool_registry.py FAILS LOUD on any '
                                'population divergence in either direction -- no silent skip.',
        'counts': {'tools': len(master_tools), 'population_authority_count': n_pop},
        'tools': dict(sorted(master_tools.items())),
    }
    with open(MASTER, 'w', encoding='utf-8') as f:
        yaml.safe_dump(master, f, sort_keys=False, width=100, default_flow_style=False)
    master_sha = hashlib.sha256(open(MASTER, 'rb').read()).hexdigest()

    # ---- compile the LIGHT card: 8 decision fields, importable, no parse ----
    CARD = ('concern', 'canonical_call', 'state', 'denominator_construction',
            'control_established', 'excludes', 'cost_band', 'knows_own_denominator',
            # CG-s-30: the tool-grain lifecycle rides the LIGHT card too, so a consumer on the
            # import path (comp-which) can exclude a deprecated tool without parsing the map.
            'status')
    cards = {t: {k: v[k] for k in CARD if v.get(k) is not None} for t, v in master_tools.items()}

    # ---- compile the ROUTING CORPORA (comp-which wiring, CTO ruling #1 @212335Z) ----
    # comp-which's hot path iterates the manifest `entries:` corpus (fuzzy backstop) and the
    # coverage-map doc (surface-first routing) -- NOT the decision card. Embedding the docs is what
    # makes the index READABLE FOR ROUTING at all; without them "wire comp-which to the index" has
    # nothing to wire. Parsed here with the EXACT open+safe_load shape comp-which itself uses, so
    # the embedded structure is the structure comp-which would have parsed -- byte-identical
    # routing is then a matter of the sha guard, not of parser agreement.
    with open(MANIFEST, encoding='utf-8') as f:
        manifest_doc = yaml.safe_load(f)
    manifest_sha = hashlib.sha256(open(MANIFEST, 'rb').read()).hexdigest()
    with open(COVERAGE_MAP, encoding='utf-8') as f:
        ledger_doc = yaml.safe_load(f) or {}
    ledger_sha = hashlib.sha256(open(COVERAGE_MAP, 'rb').read()).hexdigest()

    # WRITE TO A SIBLING TEMP, IMPORT IT, COMPARE, THEN MOVE INTO PLACE. rc=0 on the write is
    # silent about the LOAD (banked 4x on 2026-07-28, incl. this generator's own first emit) --
    # so the emitted module must prove it imports AND round-trips equal BEFORE it replaces the
    # live index. A generator that verifies after writing has already shipped the broken file.
    import pprint
    tmp_index = INDEX + '.gen-verify.tmp.py'
    with open(tmp_index, 'w', encoding='utf-8') as f:
        f.write('"""GENERATED by .tools/gen_tool_registry.py -- DO NOT EDIT.\n\n'
                'The LIGHT card (TOOLS: the 8 fields an agent needs to DECIDE) plus the ROUTING\n'
                'CORPORA (MANIFEST_DOC / LEDGER_DOC: the parsed docs comp-which routes on).\n'
                'Import, never parse -- comp-which re-parsing 133KB of YAML per call was ~97%% of\n'
                'its runtime. Full detail lives in org/modules/graph/TOOL_MASTER.yaml.\n\n'
                'STALENESS: each *_SHA256 is the sha of the source file this was compiled from.\n'
                'A reader MUST compare against the live file and FALL BACK TO PARSING on mismatch\n'
                '-- a stale index is never wrong, only unused. This file is PERSISTED+derived and\n'
                'must be able to know it is stale.\n"""\n')
        f.write('MASTER_PATH = %r\n' % MASTER)
        f.write('MASTER_SHA256 = %r\n' % master_sha)
        f.write('MANIFEST_PATH = %r\n' % MANIFEST)
        f.write('MANIFEST_SHA256 = %r\n' % manifest_sha)
        f.write('LEDGER_PATH = %r\n' % COVERAGE_MAP)
        f.write('LEDGER_SHA256 = %r\n\n' % ledger_sha)
        # repr()/pformat, NOT json.dumps() -- json emits `true`/`false`, which are not Python
        # literals and produce a file that WRITES fine and FAILS ON IMPORT.
        f.write('TOOLS = ')
        f.write(pprint.pformat(cards, width=118, sort_dicts=True))
        f.write('\n\nMANIFEST_DOC = ')
        f.write(pprint.pformat(manifest_doc, width=118, sort_dicts=True))
        f.write('\n\nLEDGER_DOC = ')
        f.write(pprint.pformat(ledger_doc, width=118, sort_dicts=True))
        f.write('\n\n\ndef is_stale():\n')
        f.write('    """True if TOOL_MASTER.yaml has changed since this index was compiled."""\n')
        f.write('    import hashlib as _h\n')
        f.write('    import os as _o\n')
        f.write('    if not _o.path.isfile(MASTER_PATH):\n        return True\n')
        f.write('    with open(MASTER_PATH, "rb") as fh:\n')
        f.write('        return _h.sha256(fh.read()).hexdigest() != MASTER_SHA256\n')

    import importlib.util as _ilu
    spec = _ilu.spec_from_file_location('_tool_index_verify', tmp_index)
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)                       # raises loud on any emit defect
    for name, want in (('TOOLS', cards), ('MANIFEST_DOC', manifest_doc), ('LEDGER_DOC', ledger_doc)):
        got = getattr(mod, name)
        if got != want:
            os.remove(tmp_index)
            raise RuntimeError('EMIT ROUND-TRIP DIVERGENCE on %s: the imported literal does not '
                               'equal the parsed source. Refusing to replace the live index.' % name)
    os.replace(tmp_index, INDEX)

    print('WROTE %s  (%d tools)' % (MASTER, len(master_tools)))
    print('WROTE %s  (card = %d fields + MANIFEST_DOC + LEDGER_DOC, import-verified pre-replace)'
          % (INDEX, len(CARD)))
    print('  master sha256 : %s' % master_sha[:16])
    print('  master bytes  : %d' % os.path.getsize(MASTER))
    print('  index  bytes  : %d  (%.0f%% of master)'
          % (os.path.getsize(INDEX), 100.0 * os.path.getsize(INDEX) / os.path.getsize(MASTER)))
    if seeded:
        print('  NOTE: overrides seeded this run -- review .tools/tool_overrides.yaml')


if __name__ == '__main__':
    main()
