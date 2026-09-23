# Historical cutoff and source receipts: bounded independent review

Reviewer: `3.0.0_SA_CVO~M`, 2026-09-23 UTC.
Authority: completion CONTRACT M1/M4/M5 reviewer mandate; LEGACY-READ-01 final
`15157a666c0f1cd0f720e2c3f678cc9f71c05715` and CTO coordination notice
`20260923T023019Z`. Trigger: exact COO~M `20260923T024500Z` candidate handoff.

## Verdict and pins

**BOUNDED SOURCE PASS** for the implemented cutoff, version-receipt capture and
canonical publication destination changes at
`55a65d3bdb52c66b106ccfc5c50e8e745356fb6b`.
No new failure was reproduced within that scope. This does not certify a complete
historical source/account population, all-source fail-closed orchestration,
economic reconciliation, fresh real-source output, publication atomicity, live
runtime or full M/E2E. Two existing limits were positively reproduced below.

Clean detached review checkout:
`C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`.
Six changed paths only: holdings_snapshot.py, new source_inputs.py, three test
files and M SOURCE_INPUT_EVIDENCE.md. Read the complete candidate diff and source
reader, affected runner/plumbing/publication functions, full supplied new tests,
source evidence document and final exact-case authority. Producer worktree was
not used for tests.

Independently verified candidate ancestry of `bb3f3ecd04`, mechanism
`5de3df146f`, protection `9a07a90f6e`, authority `15157a666c`, and separately
committed carrier `0a7810c772`. The authorized runner is exactly Git blob
`8a2011533d1b8ef173d2fcc0cb39bb07cfc58a7d`, LF SHA256
`5f310f5c26f66fbe66d62598253afbe8b8781fd4d4f86441086863147478190f`.
The actual `_latest_date_partition` AST SHA256 is
`158c11ac7c272b3a3ef64720b85652d9449b1ddcc4f9e655d79306480243b1b4`, matching
the authority's measurement. No gate override, extension of the authority,
source repoint or source-commit reconstruction was performed. Its recorded
expiry remains 2026-09-24T00:00:00Z; this review does not renew it or measure push.

## Evidence

All runs at the exact detached candidate, exit 0:

| Command | Result |
| --- | --- |
| `python -m pytest data/assets/scripts/gold/investor_reporting/tests -q` | 121 passed, 7.98s |
| `python -m pytest infra/aws/lambda/investor-reporting/holdings/tests -q` | 119 passed, 3.18s |
| `python -m pytest <independent driver below> -q` | 42 passed, 1.08s: 40 functional controls plus two limitation characterizations |

The independent driver imports the actual candidate runner, source adapter and
publisher. It constructs its own in-memory versioned transport with opaque ETags
and new listing/source fixtures. Publication controls reuse only the existing
synthetic snapshot fixture. All I/O is local or in-memory; no AWS/vendor request,
deployment, live write or real-source build occurred.

Driver runtime path:
`C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/test_source_55a_review.py`.
SHA256:
`e978f147a58a1f3ef4767455d76b69adc5eea43279c1da360da65d91ccb16b4c`.
Complete driver is embedded below.

## Measured behavior

The date selector processes multiple pages, rejects noncanonical/calendar-invalid
partition dates, admits the inclusive cutoff, and never chooses a later dated
partition. Leap-day and empty eligible-set controls pass. Actual 49F, Cottonwood
and Inflection builder functions were invoked with instrumented Parquet reads:
the exact old bucket/prefix read inventory remains, all named date selectors
receive the cutoff, and future-only listings fall back to the requested as-of
path rather than reading the future partition. This is read routing evidence,
not meaningful empty-fixture economics or a historical ownership census.

The adapter returns bytes only after recording a nonempty string VersionId and
confirming the first bytes through an exact-version read. Missing/null/non-string
versions, changed exact-read bytes or version, empty/oversized bytes, missing
exact version and explicit mid-build version switches refuse without a new
receipt. A current-version change between the first and confirming read preserves
the original observed version; later reads remain pinned. Repeat pinned-byte
changes refuse. Receipts are sorted, distinguish bucket/key identities, preserve
exact SHA256/length/version and are detached from caller mutations. The per-object
256 MiB rule was exercised with a smaller injected limit at zero, one, exact
limit and limit-plus-one; this is not an aggregate-memory bound.

Actual `run_firm -> land -> HoldingsPublication.publish/load` ran with synthetic
source bytes and a valid synthetic snapshot for each of three firms in both
production and QA namespaces. Only the canonical primary firm destination
received writes. The runner wraps the builder client, incorporates the receipt
bundle digest into public source_set_revision/content identity, and carries exact
receipts privately in the accepted manifest. Raw source_objects do not enter the
public snapshot. No-receipt and unversioned required-source controls stop before
any artifact write; a changed receipt with the old snapshot binding refuses
before the first PUT. Publisher receives the original output transport, not the
source-capture wrapper. This proves hash binding, not source completeness or
authority of caller-supplied receipts.

## Explicit limits and retained holds

1. **Eclipse still checks date shape and marker listing only.** Its cutoff skips
   future completion-marker probes and falls back across incomplete dates. It
   retains the old regex rather than calendar validation: a listed
   `2026-02-30` with a completion marker is selected under a `2026-03-01` cutoff.
   This was disclosed in the candidate and is not graded as valid-calendar proof.
   Marker listings themselves are not immutable content receipts or freshness.
2. **Optional directory cross-check still catches read exceptions.** Injecting
   SourceRefused for directory reads returns None after the existing fallbacks.
   Thus unversioned/corrupt source refusal is demonstrated at VersionedInputs and
   at uncaught required-source runner paths, not every caller. This directory
   result is informational, not the authorization join gate, and its existing
   production/QA latest pointers are not made historical by this patch. Their
   successful object reads are version-captured, but a failed read is not a
   receipt or proof of absence/completeness. No account widening was introduced
   by the reviewed diff; this does not prove global historical scope completeness.

Source reads/listings are not an atomic multi-object snapshot. Version capture
does not prove business-date compatibility, provider identity, independent
custody coverage, complete dated crosswalks, or correctness of the original
SmartX equity/cash economics. Empty/missing critical populations retain their
builder-specific requirements. The prior 7,479 reconciliation failures and
original source/custody observations are not regraded or freshly replayed here.

The existing final-index publication timeout/version ambiguity remains open.
These passing receipt/destination controls do not assert rollback, atomic
multi-object publication, real-source acceptance, vendor/render permission,
runtime package completeness or a full product grade. The maintained-source
resolver PASS at `e64d917252` is separate evidence and is not inherited here.
ADVI_FIRMBKTS, B/F cycle and existing live/deployment/economic holds remain as
specified by their governing records.

## Reproducible driver

Restore as a UTF-8 Python file; update ROOT only if the clean review checkout is
elsewhere, retain the exact source pin, then run the command above. The two named
characterization tests assert existing limits rather than claiming protective
refusal or fixing producer code.

```python
"""CVO M offline source receipt/cutoff review at exact detached 55a65d3bdb."""
import copy
import hashlib
import io
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest
from botocore.exceptions import ClientError

ROOT = Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
sys.path.insert(0, str(ROOT / 'data/assets/scripts/gold/investor_reporting'))
import holdings_snapshot as hs
import source_inputs as si
import publication as pub
sys.path.insert(0, str(ROOT / 'infra/aws/lambda/investor-reporting/holdings/tests'))
import test_snapshot as fixture


class Store:
    """Versioned in-memory transport; opaque ETags; no SDK or network client."""
    exceptions = SimpleNamespace(NoSuchKey=type('NoSuchKey', (Exception,), {}))

    def __init__(self):
        self.objects = {}; self.current = {}; self.gets = []; self.puts = []
        self.filter = lambda kw, response: response

    def seed(self, bucket, key, body, version):
        self.objects[bucket, key, version] = bytes(body)
        self.current[bucket, key] = version

    def get_object(self, **kw):
        self.gets.append(dict(kw))
        identity = kw['Bucket'], kw['Key']
        version = kw.get('VersionId', self.current.get(identity))
        if (*identity, version) not in self.objects:
            raise ClientError({'Error': {'Code': 'NoSuchKey'}}, 'GetObject')
        return self.filter(kw, {'Body': io.BytesIO(self.objects[*identity, version]),
                                'VersionId': version, 'ETag': 'opaque-' + str(version)})

    def put_object(self, **kw):
        identity = kw['Bucket'], kw['Key']
        current = self.current.get(identity)
        if (kw.get('IfNoneMatch') == '*' and current is not None or
                'IfMatch' in kw and kw['IfMatch'] != 'opaque-' + str(current)):
            raise ClientError({'Error': {'Code': 'PreconditionFailed'}}, 'PutObject')
        version = 'out-' + str(len(self.puts) + 1)
        self.seed(*identity, kw['Body'], version)
        self.puts.append(dict(kw))
        return {'VersionId': version, 'ETag': 'opaque-' + version}


def source():
    s = Store(); s.seed('observed-bucket', 'source.parquet', b'original source bytes', 'source-v1')
    return s, si.VersionedInputs(s)


def read(reader, **extra):
    return reader.get_object(Bucket='observed-bucket', Key='source.parquet', **extra)['Body'].read()


@pytest.mark.parametrize('invalid', [None, '', 'null', True, 1, [], {}])
def test_invalid_response_version_refuses_without_receipt(invalid):
    s, reader = source()
    s.filter = lambda kw, response: {**response, 'VersionId': invalid}
    with pytest.raises(si.SourceRefused): read(reader)
    assert reader.receipts() == [] and not s.puts


@pytest.mark.parametrize('mutation', ['version', 'bytes', 'empty', 'missing'])
def test_failed_first_exact_readback_never_records_source(mutation):
    s, reader = source()
    def change(kw, response):
        if 'VersionId' not in kw: return response
        if mutation == 'version': response['VersionId'] = 'different'
        elif mutation == 'bytes': response['Body'] = io.BytesIO(b'changed source bytes')
        elif mutation == 'empty': response['Body'] = io.BytesIO(b'')
        else: raise ClientError({'Error': {'Code': 'NoSuchVersion'}}, 'GetObject')
        return response
    s.filter = change
    with pytest.raises((si.SourceRefused, ClientError)): read(reader)
    assert reader.receipts() == [] and not s.puts


def test_current_changes_between_first_get_and_exact_confirmation():
    s, reader = source()
    def change(kw, response):
        if 'VersionId' not in kw:
            s.seed('observed-bucket', 'source.parquet', b'later bytes', 'source-v2')
        return response
    s.filter = change
    assert read(reader) == b'original source bytes'
    assert read(reader) == b'original source bytes'
    assert [kw.get('VersionId') for kw in s.gets] == [None, 'source-v1', 'source-v1']
    assert reader.receipts()[0] == {'bucket': 'observed-bucket', 'key': 'source.parquet',
        'version_id': 'source-v1', 'byte_length': 21,
        'sha256': hashlib.sha256(b'original source bytes').hexdigest()}


@pytest.mark.parametrize('mutation', ['version', 'bytes', 'empty'])
def test_repeat_pinned_response_change_refuses(mutation):
    s, reader = source(); read(reader); before = reader.receipts()
    def change(kw, response):
        if mutation == 'version': response['VersionId'] = 'source-v2'
        elif mutation == 'bytes': response['Body'] = io.BytesIO(b'same size false bytes')
        else: response['Body'] = io.BytesIO(b'')
        return response
    s.filter = change
    with pytest.raises(si.SourceRefused): read(reader)
    assert reader.receipts() == before


def test_explicit_switch_refuses_before_additional_get():
    s, reader = source(); read(reader); count = len(s.gets)
    with pytest.raises(si.SourceRefused): read(reader, VersionId='source-v2')
    assert len(s.gets) == count


def test_explicit_first_wrong_returned_version_refuses():
    s, reader = source()
    s.filter = lambda kw, response: {**response, 'VersionId': 'different'}
    with pytest.raises(si.SourceRefused): read(reader, VersionId='source-v1')
    assert reader.receipts() == []


@pytest.mark.parametrize('length,success', [(0, False), (1, True), (8, True), (9, False)])
def test_exact_nonempty_byte_bound(monkeypatch, length, success):
    s, reader = source(); monkeypatch.setattr(si, 'MAX_SOURCE_BYTES', 8)
    s.seed('observed-bucket', 'source.parquet', b'x' * length, 'bounded')
    if success:
        assert read(reader) == b'x' * length
        assert reader.receipts()[0]['byte_length'] == length
    else:
        with pytest.raises(si.SourceRefused): read(reader)
        assert reader.receipts() == []


def test_receipts_are_sorted_detached_and_distinguish_buckets():
    s, reader = source()
    for bucket, key in [('z', 'same'), ('a', 'same'), ('a', 'earlier')]:
        s.seed(bucket, key, b'payload', 'v')
        reader.get_object(Bucket=bucket, Key=key)
    refs = reader.receipts()
    assert [(x['bucket'], x['key']) for x in refs] == [('a', 'earlier'), ('a', 'same'), ('z', 'same')]
    refs[0]['key'] = 'mutated'; refs.pop()
    assert len(reader.receipts()) == 3 and reader.receipts()[0]['key'] == 'earlier'


class Listing:
    def __init__(self, tails, complete=()):
        self.tails = tails; self.complete = set(complete); self.pages = []; self.markers = []
    def get_paginator(self, operation):
        assert operation == 'list_objects_v2'; return self
    def paginate(self, **kw):
        self.pages.append(dict(kw))
        yield {}
        for tail in self.tails:
            yield {'CommonPrefixes': [{'Prefix': kw['Prefix'] + tail + '/'}]}
    def list_objects_v2(self, **kw):
        self.markers.append(dict(kw))
        day = kw['Prefix'].split('/')[2]
        return {'KeyCount': int(day in self.complete)}


@pytest.mark.parametrize('prefix', ['date=', 'snapshot_date='])
def test_calendar_cutoff_pagination_inclusive_and_empty(prefix):
    s = Listing([prefix + d for d in ['2026-03-01', '2026-02-28', '2026-02-29',
        '2024-02-29', '2026-2-27', '20260227', 'latest', '2026-02-30']])
    assert hs._latest_date_partition(s, 'observed-bucket', 'unchanged/', prefix, as_of='2026-02-28') == '2026-02-28'
    assert hs._latest_date_partition(s, 'observed-bucket', 'unchanged/', prefix, as_of='2026-02-27') == '2024-02-29'
    assert hs._latest_date_partition(s, 'observed-bucket', 'unchanged/', prefix, as_of='2024-01-01') is None
    assert all(p == {'Bucket': 'observed-bucket', 'Prefix': 'unchanged/', 'Delimiter': '/'} for p in s.pages)


def test_eclipse_cutoff_skips_future_markers_and_incomplete_dates():
    s = Listing(['2026-09-24', '2026-09-22', '2026-09-21', 'not-a-date'], ['2026-09-21', '2026-09-24'])
    assert hs._latest_complete_eclipse_date(s, 'opal-data-inf', '2026-09-22') == '2026-09-21'
    assert [x['Prefix'] for x in s.markers] == [
        'silver/eclipse/2026-09-22/_meta/silver_complete.json',
        'silver/eclipse/2026-09-21/_meta/silver_complete.json']


def test_eclipse_retains_disclosed_shape_only_calendar_limit():
    s = Listing(['2026-02-30'], ['2026-02-30'])
    assert hs._latest_complete_eclipse_date(s, 'opal-data-inf', '2026-03-01') == '2026-02-30'


@pytest.mark.parametrize('firm', ['49financial', 'cottonwood', 'inflection'])
@pytest.mark.parametrize('future_only', [False, True])
def test_actual_builders_keep_buckets_prefixes_and_apply_cutoff(monkeypatch, firm, future_only):
    calls = []; listing_calls = []; cutoff = '2026-09-22'
    class BuilderListing(Listing):
        def paginate(self, **kw):
            listing_calls.append(kw)
            shape = '' if kw['Prefix'] == 'silver/eclipse/' else ('snapshot_date=' if 'accounts_v2' in kw['Prefix'] else 'date=')
            for day in (['2026-09-23'] if future_only else ['2026-09-23', '2026-09-21']):
                yield {'CommonPrefixes': [{'Prefix': kw['Prefix'] + shape + day + '/'}]}
    s = BuilderListing([], ['2026-09-21'])
    def parquet(client, bucket, key):
        calls.append((bucket, key)); return pd.DataFrame()
    monkeypatch.setattr(hs, '_read_parquet', parquet)
    monkeypatch.setattr(hs, '_directory_account_ids', lambda *_: None)
    hs.BUILDERS[firm](s, cutoff)
    day = cutoff if future_only else '2026-09-21'
    if firm == '49financial':
        names = ['account_map', 'model_allocation_roster', 'allocation_positions', 'allocation_valuation']
        expected = [('opal-data-assets', 'smartx/platform/silver/fact_' + ('allocation_account_map' if name == 'account_map' else name) + '/date=' + day + '/data.parquet') for name in names]
        expected_prefixes = ['smartx/platform/silver/fact_allocation_account_map/']
    elif firm == 'cottonwood':
        expected_prefixes = ['blackdiamond/cottonwood/silver/fact_' + n + '/' for n in ['model_assignment', 'model_blend', 'model_roster', 'holdings']]
        expected = [('opal-data-assets', prefix + 'date=' + day + '/data.parquet') for prefix in expected_prefixes]
    else:
        expected_prefixes = ['silver/eclipse/', 'silver/api_dims/accounts_v2/']
        expected = [('opal-data-inf', 'silver/eclipse/' + day + '/' + n + '.parquet') for n in ['portfolios_simple', 'portfolios_full']]
        expected.append(('opal-data-inf', 'silver/api_dims/accounts_v2/snapshot_date=' + day + '/data.parquet'))
    assert calls == expected
    assert [p['Prefix'] for p in listing_calls] == expected_prefixes
    assert {p['Bucket'] for p in listing_calls} == {x[0] for x in expected}


def payload(firm):
    doc = fixture.fixture_snapshot(); doc['scope']['firm_id'] = firm
    doc['_manifest'] = {'total_market_value': 147.0}
    doc['_clock_census'] = hs.assert_clocks_carried(doc)
    return doc


@pytest.mark.parametrize('firm', ['49financial', 'cottonwood', 'inflection'])
@pytest.mark.parametrize('qa', [False, True])
def test_actual_runner_publish_receipts_canonical_home_and_private_metadata(monkeypatch, firm, qa):
    s, _ = source(); captured = []
    def builder(actual_firm, reader, day):
        assert isinstance(reader, si.VersionedInputs) and actual_firm == firm
        assert read(reader) == b'original source bytes'
        doc = payload(firm); captured.append(doc); return doc
    monkeypatch.setattr(hs, 'build_snapshot', builder)
    result = hs.run_firm(firm, s, qa=qa, upload=True, local_out=None, as_of=fixture.CUSTODY)
    store = pub.HoldingsPublication(s, firm, qa=qa)
    document, manifest = store.load()
    expected_bucket = 'opal-data-' + firm
    assert result['landed']['bucket'] == expected_bucket and result['landed']['uploaded']
    assert {x['Bucket'] for x in s.puts} == {expected_bucket}
    assert all('/holdings_qa/' in x['Key'] if qa else '/holdings/' in x['Key'] for x in s.puts)
    refs = manifest['source_objects']
    assert refs == captured[0]['_source_objects']
    revision = pub.digest(pub.canonical_bytes(refs))
    assert any(r['source'] == 'irpt-source-objects' and r['revision'] == revision for r in document['source_set_revision'])
    assert '_source_objects' not in document and 'source_objects' not in document
    assert result['landed']['revision'] == pub.digest(pub.canonical_bytes(document))


@pytest.mark.parametrize('mode', ['no_reads', 'unversioned'])
def test_actual_runner_no_valid_receipts_refuses_before_writes(monkeypatch, mode):
    s, _ = source()
    if mode == 'unversioned': s.filter = lambda kw, r: {**r, 'VersionId': 'null'}
    def builder(firm, reader, day):
        if mode == 'unversioned': read(reader)
        return payload(firm)
    monkeypatch.setattr(hs, 'build_snapshot', builder)
    with pytest.raises(RuntimeError):
        hs.run_firm('49financial', s, qa=False, upload=True, local_out=None, as_of=fixture.CUSTODY)
    assert s.puts == []


def test_receipt_tamper_refuses_before_any_artifact_put(monkeypatch):
    s, reader = source(); read(reader); refs = reader.receipts()
    doc = payload('49financial'); doc['_source_objects'] = copy.deepcopy(refs)
    doc['source_set_revision'].append({'source': 'irpt-source-objects',
        'revision': pub.digest(pub.canonical_bytes(refs)), 'completion_date': fixture.CUSTODY})
    doc['_source_objects'][0]['version_id'] = 'changed'
    store = pub.HoldingsPublication(s, '49financial')
    with pytest.raises(pub.PublicationRefused, match='source receipts not bound'):
        hs.land('opal-data-49financial', hs.PROD_PREFIX, fixture.CUSTODY, doc, True, None,
                s3_client=s, expected=store.begin())
    assert s.puts == []


def test_directory_optional_crosscheck_still_swallows_source_failure():
    """Characterization of preexisting behavior, not a fail-closed success claim."""
    class BrokenDirectory:
        def get_object(self, **kw): raise si.SourceRefused('unversioned directory')
    assert hs._directory_account_ids(BrokenDirectory(), 'observed-bucket', '49financial') is None

```
