"""Generate the SERVED-PREFIX REGISTRY -- the coverage denominator for S3Key graph ingest.

STEP 1 of the comp-opalbizcluster reroute (Andrew-direct 2026-07-28). This declares WHAT THE
S3Key PRODUCER MUST COVER. It is a denominator declaration, not a producer.

DEMAND-ANCHORED, NOT SUPPLY-ANCHORED. Scoping to "everything under json/" would ingest 958 keys --
4x the estate's entire current S3Key population (232) -- and 722 of those are a json/sentiment/
article dump against only 5 served sentiment endpoints. A registry that ingests a dump as a served
artifact is a denominator nobody can reason about.

TWO SCOPE MODES, and the rule that picks between them is measured, not chosen:
  PREFIX  -- declare the prefix. ROBUST TO KEY MOVES, which is the defect that caused this work
             (the 2026-07-23 mdpf platinum->json move). Used where the prefix is a served set.
  KEYSET  -- declare the served keys explicitly. Used where a prefix is a high-cardinality DUMP,
             i.e. key_count / served_endpoints exceeds DUMP_RATIO.

URL != KEY, MEASURED: ServedURL /api/general/mdpf/aggregate-aua-timeseries.json coexists with BOTH
json/mdpf/aggregate-aua-timeseries.json AND json/mdpf/global/aggregate-aua-timeseries.json. A naive
URL->key string transform resolves to the BARE key -- not the global/ one the incident was about.
So the registry NEVER derives a key from a URL; it declares prefixes and lets the producer observe.
"""
import datetime as dt
import os
import re
import subprocess
import sys

import boto3
import yaml

OUT = '.tools/served_prefix_registry.yaml'
SERVING_BUCKET = 'opal-data-portal-v2'
MONOLITH = 'opal-data-assets'
DUMP_RATIO = 10          # keys-per-served-endpoint above which a prefix is a DUMP, not a served set
KUZU = '.tools/comp-kuzu'


class EmptyDenominator(RuntimeError):
    """A zero on either side is a BROKEN RETRIEVAL until proven otherwise. Never write on it."""


def served_urls():
    """DEMAND side: the ServedURL nodes the portal actually reads (canonical graph).

    NEVER a bare `bash` from Python -- CLAUDE.md: a python-spawned bare bash Windows-resolves to
    the System32 WSL stub and fails LOUD or, worse, SILENTLY. This function returned 0 URLs on its
    first run for exactly that reason, and the caller wrote a registry declaring zero coverage.
    """
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from git_bash_resolver import git_bash
    q = "MATCH (n:CloudNode) WHERE n.node_type='ServedURL' RETURN n.node_id"
    r = subprocess.run([git_bash(), KUZU, '--limit', '200', q],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=280)
    urls = [m.group(1).strip() for m in re.finditer(r'endpointurl:(\S+)', r.stdout or '')]
    if not urls:
        raise EmptyDenominator(
            'DEMAND SIDE RETURNED ZERO ServedURL nodes. That is a broken retrieval, not an empty '
            'estate -- the graph is known to hold 45. Refusing to write a registry that would '
            'declare zero coverage.\n  rc=%s\n  stderr=%s' % (r.returncode, (r.stderr or '')[:400]))
    return urls


def live_prefix_counts(bucket, prefix):
    """Per-sub-prefix key count AND newest write.

    The newest write is the DISCRIMINATOR for a prefix with no ServedURL. Without it, "nothing
    serves this" and "the graph does not model what serves this" are indistinguishable -- I flagged
    exactly that as unresolvable in v0.1 and it is resolvable: A PREFIX STILL BEING WRITTEN IS BEING
    PRODUCED FOR SOMEONE. Absence of a consumer edge on a live producer is a GRAPH GAP, not dead code.
    """
    s3 = boto3.client('s3')
    subs, out = [], {}
    r = s3.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter='/')
    for p in r.get('CommonPrefixes', []):
        subs.append(p['Prefix'])
    for sub in subs:
        n, newest = 0, None
        for pg in s3.get_paginator('list_objects_v2').paginate(Bucket=bucket, Prefix=sub):
            for o in pg.get('Contents', []):
                n += 1
                if newest is None or o['LastModified'] > newest:
                    newest = o['LastModified']
        out[sub] = {'keys': n, 'newest': newest}
    return out


# write-age bands for a prefix carrying NO ServedURL edge
ALIVE_DAYS = 7
DORMANT_DAYS = 90


def liveness(newest, now):
    if newest is None:
        return 'EMPTY'
    age = (now - newest).days
    if age <= ALIVE_DAYS:
        return 'ALIVE'
    if age <= DORMANT_DAYS:
        return 'DORMANT'
    return 'STALE'


def main():
    urls = served_urls()
    static = [u for u in urls if u.endswith('.json')]
    dynamic = [u for u in urls if not u.endswith('.json')]

    # map each static ServedURL to its bucket sub-prefix by its PENULTIMATE path segment
    # (/api/general/<group>/<file>.json -> json/<group>/). Never to a KEY -- see module docstring.
    demand = {}
    for u in static:
        parts = [p for p in u.split('/') if p]
        group = parts[-2] if len(parts) >= 2 else None
        if group:
            demand.setdefault('json/%s/' % group, []).append(u)

    counts = live_prefix_counts(SERVING_BUCKET, 'json/')
    if not counts:
        raise EmptyDenominator(
            'SUPPLY SIDE RETURNED ZERO prefixes under json/ on %s. Broken retrieval or wrong '
            'bucket -- refusing to write.' % SERVING_BUCKET)

    entries = []
    for pfx, endpoints in sorted(demand.items()):
        rec_ = counts.get(pfx)
        n_keys = rec_['keys'] if rec_ else None
        if n_keys is None:
            entries.append({'prefix': pfx, 'scope': 'ABSENT-ON-LIVE', 'served_endpoints': len(endpoints),
                            'live_keys': None,
                            'note': 'a ServedURL group with NO matching live prefix -- either the URL '
                                    'group does not map to a json/ sub-prefix, or the artifact moved. '
                                    'SURFACED, not dropped.'})
            continue
        ratio = n_keys / max(len(endpoints), 1)
        entries.append({
            'prefix': pfx,
            'scope': 'KEYSET' if ratio > DUMP_RATIO else 'PREFIX',
            'served_endpoints': len(endpoints),
            'live_keys': n_keys,
            'keys_per_endpoint': round(ratio, 1),
            'endpoints': sorted(endpoints),
        })

    covered = sum(e['live_keys'] or 0 for e in entries if e['scope'] == 'PREFIX')
    dumps = [e for e in entries if e['scope'] == 'KEYSET']
    unmatched_raw = sorted(set(counts) - set(demand))
    now = dt.datetime.now(dt.timezone.utc)
    unmatched = []
    for u in unmatched_raw:
        c = counts[u]
        lv = liveness(c['newest'], now)
        unmatched.append({
            'prefix': u, 'keys': c['keys'],
            'newest_write': c['newest'].strftime('%Y-%m-%dT%H%MZ') if c['newest'] else None,
            'age_days': (now - c['newest']).days if c['newest'] else None,
            'liveness': lv,
            'disposition': (
                'GRAPH GAP -- actively written with NO ServedURL edge. A live producer with no '
                'modelled consumer is a coverage defect, NOT dead code. MUST be resolved before '
                'this registry is complete.' if lv == 'ALIVE' else
                'MIGRATION REMNANT or dormant product surface -- written within 90d then stopped. '
                'Candidate debt; NOT a graph gap.' if lv == 'DORMANT' else
                'STALE -- no write in >90d. Almost certainly decommissioned; excluded from ingest '
                'scope, recorded so the exclusion is visible rather than silent.'),
        })

    doc = {
        'schema_version': '0.1',
        'purpose': 'THE COVERAGE DENOMINATOR for S3Key graph ingest. Declares what the S3Key '
                   'producer must cover so a served artifact can never be structurally invisible.',
        'authority': 'Andrew-direct 2026-07-28. Step 1 of the comp-opalbizcluster reroute.',
        'generated_by': '.tools/gen_served_prefix_registry.py -- re-runnable; DEMAND from the '
                        'canonical graph, SUPPLY from live S3. Nothing hand-listed.',
        'method': {
            'demand': 'ServedURL nodes in the canonical graph (what the portal actually reads)',
            'supply': 'live list_objects_v2 over %s' % SERVING_BUCKET,
            'url_is_not_key': 'MEASURED: /api/general/mdpf/aggregate-aua-timeseries.json coexists '
                              'with BOTH json/mdpf/aggregate-aua-timeseries.json AND '
                              'json/mdpf/global/aggregate-aua-timeseries.json. The registry NEVER '
                              'derives a key from a URL -- it declares prefixes and lets the '
                              'producer OBSERVE the keys.',
            'dump_rule': 'keys_per_endpoint > %d => KEYSET (a dump, declare served keys) '
                         'else PREFIX (a served set, declare the prefix -- robust to key moves)' % DUMP_RATIO,
        },
        'denominators': {
            'served_urls_total': len(urls),
            'static_json_served': len(static),
            'dynamic_api_routes': len(dynamic),
            'live_keys_under_json': sum(c['keys'] for c in counts.values()),
            'keys_in_PREFIX_scope': covered,
            'prefixes_declared': len(entries),
            'live_prefixes_with_NO_served_url': len(unmatched),
        },
        'dynamic_routes_out_of_scope': sorted(dynamic),
        'entries': entries,
        'live_prefixes_with_no_served_url': unmatched,
        'unmatched_liveness_summary': {k: sum(1 for u in unmatched if u['liveness'] == k) for k in ('ALIVE','DORMANT','STALE','EMPTY')},
        'monolith_note': 'opal-data-assets (the monolith) also serves. Its gold/ and json/ prefixes '
                         'need the same treatment; NOT enumerated here because its ServedURL edges '
                         'are not yet in the graph. STATED AS A GAP, not silently omitted.',
    }
    with open(OUT, 'w', encoding='utf-8') as f:
        yaml.safe_dump(doc, f, sort_keys=False, width=100, default_flow_style=False)

    print('WROTE %s' % OUT)
    d = doc['denominators']
    for k, v in d.items():
        print('  %-32s %s' % (k, v))
    print('\n  PREFIX-scope prefixes: %d' % len([e for e in entries if e['scope'] == 'PREFIX']))
    print('  KEYSET-scope (dumps)  : %d  %s' % (len(dumps), [e['prefix'] for e in dumps]))
    print('  ABSENT-ON-LIVE        : %d' % len([e for e in entries if e['scope'] == 'ABSENT-ON-LIVE']))


if __name__ == '__main__':
    main()
