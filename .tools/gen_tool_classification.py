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

import yaml

PROFILE = 'org/tier1_exec/3.0.0_SA_CVO/deliverables/tool_profile.json'
OUT = '.tools/TOOL_CLASSIFICATION.yaml'

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
REFRESH = {
    'GRAPH-DB': {'refresh_mechanism': 'auto-refresh on HEAD-advance; provenance header printed per call',
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
tools = {}
unclassified = []
for r in rows:
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
