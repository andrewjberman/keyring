"""Generate .tools/TOOL_CLASSIFICATION.yaml -- the standardized-constants registry.

Populated MECHANICALLY from the enumeration-primitive census, so the classification is derived
from source rather than hand-asserted. Re-runnable: re-run to regenerate after tools change.

CONSTANTS (Andrew-direct 2026-07-28):
  state       LIVE | PERSISTED        -- "derived is a qualifier, not a state"
  derived     true | false            -- the qualifier: computed, vs read/authored directly
  denominator_construction ENUMERATED|MATCHED|TRAVERSED|EXERCISED -- how the population is built
  control     POSITIVE | NEGATIVE | NONE -- strongest control the tool can concretely establish
"""
import collections
import json
import os
import sys

import yaml

PROFILE = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/tool_profile.json'
OUT = '.tools/TOOL_CLASSIFICATION.yaml'
COVERAGE_MAP = 'org/modules/graph/comp-coverage-map.yaml'
MANIFEST = 'org/modules/graph/graph-call-manifest.yaml'

# ---- THE POPULATION COMES FROM THE AUTHORITY, NEVER FROM THIS FILE'S OWN INPUT ------------------
# NFRA_CLDGRPH CG-s-17 pass 2 (2026-09-09, the issuer's amendment). PROFILE above is an ATTRIBUTE
# source and was ALSO being used as the POPULATION -- exactly the "peer file that enumerates its own
# tool list becomes a 5th copy of the population and drifts" that CTO ruling 20260728T212335Z
# forbids, with org/modules/graph/comp-coverage-map.yaml named as the SOLE authority.
# MEASURED CONSEQUENCE, not a tidiness argument: the profile still lists retired tools, they landed
# in TOOL_CLASSIFICATION.yaml, and gen_tool_registry.py -- which builds its master FROM this file
# and asserts parity against the authority -- REFUSED with PopulationDivergence, so TOOL_MASTER.yaml
# and .tools/tool_index.py could not be regenerated AT ALL. A stale help text in a generated index
# then has no repair path, which is how an instruction plane outlives the thing it points at.
#
# THE AUTHORITY IS READ THROUGH gen_tool_registry's OWN READER, IMPORTED, NEVER COPIED. A second
# implementation of population_from_map() here would be a second reader of one population -- the
# very defect this fix removes, one file over. It FAILS CLOSED AND LOUD if the import or the read
# does not work: a local fallback copy IS the drift.


def authority():
    """(population, norm_tool) from the SOLE authority, via the registry generator's own reader."""
    try:
        import gen_tool_registry as reg
    except ImportError:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        try:
            import gen_tool_registry as reg
        except ImportError as exc:
            raise SystemExit(
                'BLOCKED: .tools/gen_tool_registry.py is not importable (%s), so the population\n'
                '  authority cannot be read the way its own consumer reads it. This generator does\n'
                '  NOT carry a fallback copy of population_from_map() on purpose: a second reader\n'
                '  of one population is the drift (CTO ruling 20260728T212335Z).' % exc)
    pop = reg.population_from_map()
    if not pop:
        raise SystemExit(
            'BLOCKED: the population authority %s yielded 0 tool(s). An empty authority would\n'
            '  EXCLUDE EVERY profile row and write an empty classification -- a vacuous pass that\n'
            '  reads as clean. Refusing.' % COVERAGE_MAP)
    return pop, reg.norm_tool


def declared_retired():
    """The manifest's closed set of retired comp-* NAMES -- read, never hardcoded here."""
    if not os.path.isfile(MANIFEST):
        return set()
    with open(MANIFEST, encoding='utf-8', errors='replace') as f:
        doc = yaml.safe_load(f) or {}
    return set((doc.get('retired_aliases') or {}).keys())

# HOW THE DENOMINATOR IS CONSTRUCTED -- the archetype. Replaces a bounded/unbounded boolean that
# measured VACUOUS (True for 89/89): a field that cannot vary is not a classification.
#   ENUMERATED  listed from an authoritative source -- you get the WHOLE set, N is knowable up front
#   MATCHED     discovered by pattern/search -- you get HITS, never the set; N is NOT knowable
#   TRAVERSED   walked from a seed -- depth-dependent; N depends on where you started
#   EXERCISED   probed candidate-by-candidate against the live plane -- N == candidates you supplied
DENOM_CONSTRUCTION = {
    'GIT': 'ENUMERATED', 'AWS-API': 'ENUMERATED', 'REGISTRY': 'ENUMERATED',
    'FS-WALK': 'ENUMERATED', 'FS-GLOB': 'MATCHED', 'AST': 'MATCHED',
    'GRAPH-DB': 'TRAVERSED', 'SIMULATE': 'EXERCISED', 'SQL/TRINO': 'ENUMERATED',
    'SUBPROC': 'INHERITED',
}
# N is knowable up front only when the population is listed or explicitly supplied
DENOM_KNOWABLE = {'ENUMERATED': True, 'EXERCISED': True,
                  'MATCHED': False, 'TRAVERSED': False, 'INHERITED': False}

# primitive -> (state, derived, denominator_bounded, universe, excludes, control)
PRIM_MAP = {
    'GIT': ('LIVE', True, True,
            'git-tracked files + commit history at call time',
            ['gitignored paths', 'submodule contents (gitlink only)', 'anything not in the repo'],
            'POSITIVE'),
    'FS-WALK': ('LIVE', True, True,
                'working tree under declared roots, filtered by extension',
                ['paths outside the declared roots', 'unlisted extensions', 'non-filesystem stores'],
                'POSITIVE'),
    'FS-GLOB': ('LIVE', True, True,
                'working tree matched by glob pattern',
                ['paths outside the pattern', 'non-filesystem stores'],
                'POSITIVE'),
    'AST': ('LIVE', True, True,
            'parsed Python source at the read vintage',
            ['non-Python lanes', 'runtime/dynamic construction'],
            'POSITIVE'),
    'AWS-API': ('LIVE', False, True,
                'the live AWS control plane for the queried service',
                ['other regions', 'other accounts', 'resource types not queried'],
                'POSITIVE'),
    'SIMULATE': ('LIVE', False, True,
                 'actual reach, established by exercising each enumerated candidate',
                 ['candidates not enumerated for simulation'],
                 'NEGATIVE'),
    'SQL/TRINO': ('LIVE', False, True,
                  'the Trino federation by physical catalog',
                  ['catalogs not federated', 'in-VPC only; ~3-4 min/call'],
                  'POSITIVE'),
    'GRAPH-DB': ('PERSISTED', True, True,
                 'the derived globgrph (kuzu) nodes and edges',
                 ['anything not yet ingested into the graph',
                  'anything the SERVED projection has not picked up yet -- read the VINTAGE line'],
                 'POSITIVE'),
    'REGISTRY': ('PERSISTED', False, True,
                 'an authored ledger (coverage-map / manifest / project JSON)',
                 ['anything unregistered -- THE PHANTOM CLASS'],
                 'POSITIVE'),
    'SUBPROC': ('LIVE', True, False,
                'inherits the universe of the tool it delegates to',
                ['inherits the callee blind spots'],
                'NONE'),
}
# NFRA_CLDGRPH CG-s-28 (2026-09-09): the HEAD-advance auto-refresh string this constant used to
# carry described the LOCAL Kuzu projection, retired at CG-s-8 (@173a1d8c90). It is CITED, not
# repeated, so a census of the retired phrase does not hit this tombstone (the W2-S38 convention).
# Nothing refreshes on a HEAD-advance any more and no
# CALL refreshes anything: the SERVED projection is refreshed by the marker-driven cloud worker
# (CG-s-2/3) off a real S3 marker, and every seat READS it through the thin client, which prints the
# VINTAGE line per call. refresh_is_incremental stays True on the MEASURED behaviour of that worker
# -- infra/aws/globgrph/kuzu_incremental_refresh.py is incremental with a FULL-RELOAD FALLBACK on a
# large delta (:53-56 FALLBACK_MIN_ABS/FALLBACK_FRACTION), so the mechanism is incremental-first and
# the fallback is the exception, not the rule.
REFRESH = {
    'GRAPH-DB': {'refresh_mechanism': 'served projection; refreshed by the marker-driven cloud '
                                      'worker (NFRA_CLDGRPH CG-s-2/3), never by a call; provenance '
                                      'header (VINTAGE) printed per call',
                 'refresh_is_incremental': True},
    'REGISTRY': {'refresh_mechanism': 'gate-enforced at registration (comp-coverage-check)',
                 'refresh_is_incremental': True},
}


def classify(prims):
    if not prims:
        return None
    # state: PERSISTED dominates -- if ANY read is from a store, staleness is a live question
    order = ['GRAPH-DB', 'REGISTRY', 'SIMULATE', 'AWS-API', 'SQL/TRINO', 'GIT', 'FS-WALK', 'AST',
             'FS-GLOB', 'SUBPROC']
    primary = next((p for p in order if p in prims), prims[0])
    st, der, bnd, uni, exc, ctl = PRIM_MAP[primary]
    state = 'PERSISTED' if any(p in ('GRAPH-DB', 'REGISTRY') for p in prims) else st
    excludes = []
    for p in prims:
        for e in PRIM_MAP.get(p, (None,) * 6)[4] or []:
            if e not in excludes:
                excludes.append(e)
    # strongest control across primitives
    ctl = 'NEGATIVE' if 'SIMULATE' in prims else ('POSITIVE' if any(
        PRIM_MAP.get(p, (None,) * 6)[5] == 'POSITIVE' for p in prims) else 'NONE')
    constr = DENOM_CONSTRUCTION.get(primary, 'INHERITED')
    rec = {
        'primitives': prims,
        'state': state,
        'derived': bool(der),
        'denominator_construction': constr,
        'denominator_knowable_up_front': DENOM_KNOWABLE[constr],
        'universe': uni,
        'excludes': excludes,
        'control_established': ctl,
    }
    for p in prims:
        if p in REFRESH:
            rec.update(REFRESH[p])
    return rec


rows = json.load(open(PROFILE, encoding='utf-8'))

# THE SPLIT, PRINTED BEFORE ANYTHING IS WRITTEN. A profile row whose tool is not in the authority is
# EXCLUDED and NAMED -- never silently dropped, because a population that shrinks quietly is the
# failure this whole chain is built against. An excluded name that is ALSO a declared retired alias
# is expected bookkeeping; one that is NOT is a finding, and it is printed as such rather than
# absorbed into the exclusion count.
AUTHORITY, NORM = authority()
RETIRED_NAMES = declared_retired()
kept, excluded, undeclared = [], [], []
for r in rows:
    if NORM(str(r['tool'])) in AUTHORITY:
        kept.append(r)
    else:
        excluded.append(str(r['tool']))
        if NORM(str(r['tool'])) not in RETIRED_NAMES:
            undeclared.append(str(r['tool']))
orphan_authority = sorted(AUTHORITY - {NORM(str(r['tool'])) for r in rows})

print('POPULATION AUTHORITY: %s -- %d tool(s) (read via gen_tool_registry.population_from_map)'
      % (COVERAGE_MAP, len(AUTHORITY)))
print('PROFILE (attributes only): %s -- %d row(s)' % (PROFILE, len(rows)))
print('EXCLUDED_NOT_IN_AUTHORITY=%d of %d: %s'
      % (len(excluded), len(rows), ', '.join(sorted(excluded)) or 'none'))
print('  of those, DECLARED RETIRED ALIASES (expected)=%d of %d: %s'
      % (len(excluded) - len(undeclared), len(excluded),
         ', '.join(sorted(set(excluded) - set(undeclared))) or 'none'))
print('  NOT DECLARED RETIRED -- A FINDING, NOT AN EXCLUSION=%d of %d: %s'
      % (len(undeclared), len(excluded), ', '.join(sorted(undeclared)) or 'none'))
print('AUTHORITY_WITHOUT_A_PROFILE_ROW=%d of %d: %s'
      % (len(orphan_authority), len(AUTHORITY), ', '.join(orphan_authority) or 'none'))
print('  (these are NOT dropped: gen_tool_registry emits each one with an explicit'
      ' UNCLASSIFIED marker, per CTO ruling 212335Z "no silent skip".)')

tools = {}
unclassified = []
for r in kept:
    c = classify(r['primitives'])
    if c is None:
        unclassified.append(r['tool'])
        continue
    c['bounding'] = r['bounding'] or ['NONE -- unbounded output']
    c['declares_denominator_in_output'] = r['declares_denominator']
    tools[r['tool']] = c

doc = {
    'schema_version': '0.1',
    'authority': 'Andrew-direct 2026-07-28 -- standardized constants for tool classification',
    'generated_by': '.tools/gen_tool_classification.py (re-runnable; derived from source, not asserted)',
    'population_authority':
        'org/modules/graph/comp-coverage-map.yaml -- tools[] + meta_tools[] (CTO ruling '
        '20260728T212335Z, the SOLE population authority). READ through '
        'gen_tool_registry.population_from_map(), never re-implemented here. '
        'org/tier1_exec/3.0.0_SA_CVO/deliverables/tool_profile.json is the ATTRIBUTE source ONLY: a '
        'profile row whose tool is absent from the authority is EXCLUDED and NAMED on stdout, and '
        'an excluded name that is not a declared retired alias is reported as a finding. Before '
        'NFRA_CLDGRPH CG-s-17 (2026-09-09) the profile was also the population, and the four '
        'retired names it still carries made gen_tool_registry refuse outright.',
    'source_of_truth_note':
        'This file classifies HOW a tool retrieves and what it covers. Tool INVENTORY '
        '(which tools exist + their one home) remains org/modules/graph/comp-coverage-map.yaml '
        'per CTO ruling #1. This does NOT supersede it and must not duplicate its fields.',
    'constants': {
        'state': ['LIVE', 'PERSISTED'],
        'state_doc':
            'WHERE THE ANSWER COMES FROM. LIVE = established at call time. PERSISTED = read from a '
            'store built earlier. ONLY PERSISTED CAN BE STALE.',
        'derived': [True, False],
        'derived_doc':
            'A QUALIFIER ON state, NOT A STATE (Andrew-direct). derived=true means computed from a '
            'more primitive source; false means read/authored directly. PERSISTED+derived needs a '
            'REFRESH MECHANISM; PERSISTED+authored needs an AUTHORSHIP GATE.',
        'denominator_construction': ['ENUMERATED', 'MATCHED', 'TRAVERSED', 'EXERCISED', 'INHERITED'],
        'denominator_construction_doc':
            'HOW THE POPULATION IS BUILT. ENUMERATED = listed from an authoritative source, you get '
            'the whole set. MATCHED = discovered by pattern/search, you get HITS and never the set. '
            'TRAVERSED = walked from a seed, depth-dependent. EXERCISED = probed candidate-by-candidate '
            'against the live plane. NOTE: a bounded/unbounded BOOLEAN was tried first and measured '
            'VACUOUS (true for 89/89) -- a field that cannot vary is not a classification.',
        'denominator_knowable_up_front': [True, False],
        'denominator_knowable_doc':
            'Derived from construction: can the tool state N-of-M BEFORE it scans? ENUMERATED and '
            'EXERCISED yes; MATCHED and TRAVERSED no. THIS IS THE TRUNCATION-RISK AXIS -- a tool that '
            'cannot know its denominator cannot honestly report showing-N-of-M.',
        'control_established': ['POSITIVE', 'NEGATIVE', 'NONE'],
        'control_doc':
            'POSITIVE = can concretely show what IS covered. NEGATIVE = can also establish what is '
            'NOT there (only SIMULATE achieves this today -- it exercises rather than reads). '
            'NEGATIVE archetyping is the goal; POSITIVE is the floor and is enough to start.',
    },
    'known_limitations': {
        'universe_and_denominator_construction_are_PRECEDENCE_PICKED':
            'A tool matching MULTIPLE primitives gets `universe` and `denominator_construction` from '
            'the PRECEDENCE-WINNING primitive, which is NOT always its dominant behaviour. Worked '
            'defect: comp-heat matches [GIT, SQL/TRINO] and is labelled with the Trino universe, but '
            'its true universe is GIT (object_freshness.py:46 ls-files). '
            'MEASURED BLAST RADIUS: 67 of 89 tools (75%) are multi-primitive -- so treat `universe` '
            'as RELIABLE only for the 22 single-primitive tools. v0.2 fix: make `universe` and '
            '`denominator_construction` LISTS, one per primitive, since a multi-primitive tool '
            'genuinely has more than one universe.',
        'fields_NOT_affected':
            '`state` (PERSISTED dominates -- if ANY read is from a store, staleness is a real '
            'question), `excludes` (UNIONED across all primitives, so it accumulates conservatively '
            'in the SAFE direction), and `control_established` (strongest across primitives) are '
            'sound for multi-primitive tools.',
        'classification_is_DECLARED_from_source':
            'Derived by source-pattern match, NOT by execution. A primitive reached only on a rare '
            'code path may be mis-binned. Exercised for: comp-heat, comp-clobber, comp-coverage-check, '
            'comp-which, comp-grep, comp-glob.',
        'negative_control':
            'Only EXERCISED (SIMULATE) tools can establish absence. 8 of 89 today. For the other 81, '
            'POSITIVE control is the floor and is what is claimed -- per Andrew-direct, that is enough '
            'to start.',
    },
    'counts': {
        'classified': len(tools),
        'unclassified': len(unclassified),
        'unclassified_tools': unclassified,
        'profile_rows': len(rows),
        'excluded_not_in_authority': len(excluded),
        'excluded_not_in_authority_tools': sorted(excluded),
        'excluded_not_declared_retired': sorted(undeclared),
        'authority_without_a_profile_row': orphan_authority,
    },
    'tools': dict(sorted(tools.items())),
}
with open(OUT, 'w', encoding='utf-8') as f:
    yaml.safe_dump(doc, f, sort_keys=False, width=100, default_flow_style=False)

print('WROTE %s' % OUT)
print('  classified %d / unclassified %d %s' % (len(tools), len(unclassified), unclassified))
print('  state      :', dict(collections.Counter(t['state'] for t in tools.values())))
print('  derived    :', dict(collections.Counter(t['derived'] for t in tools.values())))
print('  denom-constr:', dict(collections.Counter(t['denominator_construction'] for t in tools.values())))
print('  N knowable :', dict(collections.Counter(t['denominator_knowable_up_front'] for t in tools.values())))
print('  control    :', dict(collections.Counter(t['control_established'] for t in tools.values())))
print('  declares denominator in output:',
      dict(collections.Counter(t['declares_denominator_in_output'] for t in tools.values())))
