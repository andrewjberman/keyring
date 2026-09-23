# Independent bounded accepted-publication review

**archetype:** VALIDATE

Reviewer `3.0.0_SA_CVO~M`; 2026-09-22. **Bounded PASS** for candidate `62139c3a1a9792b41e02a8b66b612ad4571c6ab8` at the exercised versioned publication / accepted reader / guarded Entry boundary. No full M4/M7, S2/S7, deployed storage, source-census or product PASS. Final index transport ambiguity and changing versioning configuration remain explicit limitations, not rollback guarantees.

Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`. Exact COO~M request `20260922T230629Z_2.0.0_SA_COO_M_IRPT_M_bounded_publication_review__62139.md`; ACK delivered before review. Producer evidence read completely: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/PUBLICATION_EVIDENCE.md` at the candidate.

## Isolation and actual instruments

The reviewer checkout `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review` was tracked/untracked clean before switching and after verification, detached at the exact candidate. No implementation changes, source integration, vendor call, AWS operation, deployment or push. Source diff and actual publication.py, snapshot reader, Gold land/run entry and supplied tests were read. The generated `firm_bucket_map` function AST is equal to its parent; its generator stamp changed. This verifies mapping equality, not a new naming-owner integration grant.

| Command/instrument | Result |
|---|---|
| `python -m pytest infra/aws/lambda/investor-reporting/holdings/tests -q` | 80 passed in 1.73s |
| `python -m pytest data/assets/scripts/gold/investor_reporting/tests -q` | 85 passed in 5.73s |
| Independent driver below: `python -m pytest <runtime>/test_publication_621_review.py -q -rA` | 26 passed in 1.68s after correcting reviewer exception identity; no candidate change |
| Candidate vs parent generated map AST | Equal |

The supplied suites include 19 publication/transport cases using actual Parquet and real land -> versioned reader -> guarded Entry. These cover malformed/different Gold nodes, validation/reconciliation rejection, immutable correction history, conditional conflicts, private destinations, exact versions/hashes, bounds and revocation. Rerunning those suites repeats producer instruments; independent corroboration is the separate transport and fault schedules embedded below.

The reviewer driver uses a separately implemented in-memory version store with opaque ETags and read/write logs, actual candidate Gold land and publication code, real Parquet, accepted snapshot loader and actual guarded holdings Entry. It reuses the producer's synthetic payload and Entry fixture: directory/grant/retained-selection dependencies are controlled, not real DynamoDB/IAM. This is a 49financial fixture; no three-firm actual-data census is claimed.

## Independent exercised cases: 26 of 26

| Cases | Observed boundary |
|---|---|
| 9: Gold, Platinum and manifest each crossed with pre-write timeout, corrupt readback bytes and wrong returned version | Publication refuses; prior captured index unchanged; guarded Entry still serves only selected A1=$100 with the prior accepted revision. |
| 2: stale competing publisher, with and without an existing index | Conditional index race refuses loser; guarded Entry serves winner's accepted revision. Serial deterministic interleavings, not live concurrent S3 clients. |
| 1: same-day correction | New content revision accepted; every earlier stored version preserved byte-for-byte. |
| 1: later unaccepted versions written to Gold/Platinum keys | Reader uses previously pinned versions; newer mutable heads cannot substitute their bytes. |
| 5: accepted manifest's Platinum reference mutated by bucket, key, missing version, hash and Boolean byte length | Guarded Entry returns NOT_READY with no data. Read log shows no foreign bucket or legacy-prefix fallback. Manifest/index hashes were adjusted to reach the downstream reference validation rather than failing only the outer hash. |
| 1: QA-only publication plus legacy mutable payload | PROD reader does not fall back; NOT_READY. |
| 1: requested date absent while latest exists | No latest substitution; NOT_READY. |
| 3: final index PUT before-persistence timeout, after-persistence timeout, suspended versioning | Outcomes below reproduced explicitly. |
| 3: grant revocation, directory revision change, retained-selection deletion after versioned read | Actual guarded Entry returns OBJECT_NOT_COVERED and no data. |

## Final index outcome limits

A timeout injected **before** index persistence leaves the prior index and guarded accepted answer unchanged. A timeout injected **after** index persistence throws to the publisher yet the new revision is accepted and served by the reader. This is an ambiguous caller outcome requiring reconciliation, not rollback. Injected versioning suspension persists a `null`-version index, then publication refuses; subsequent guarded reading is NOT_READY. The prior immutable artifacts still exist, but code did not undo the index write or restore service.

These are controlled transport outcomes, not evidence of actual cloud timeouts or bucket configuration. The code's conditional writes depend on actual S3 versioning and write-policy enforcement. It cannot itself prevent a privileged writer from disabling versioning, mutating acceptance metadata or deleting retained versions. No bucket policy, versioning configuration, IAM/KMS, package delivery, physical disposal or crash consistency across changing operational configuration is graded here.

## Harness correction and remaining work

Initial independent run was 19 pass / 7 fail because the guarded route loader reloads flat Python modules: the raised `publication.PublicationRefused` belonged to the current module, while the reviewer expected the initially imported class identity. Failure traces showed the intended refusal, not an accepted artifact. The reviewer expectation now recognizes both exact module class identities. Transport schedules and acceptance assertions are unchanged; rerun 26 pass. This correction is disclosed and not counted as an implementation repair.

Exact upstream object-version receipts, independent complete custody census/freshness, historical provider ownership, Y security/price/normalized-position inputs and fresh three-firm source-to-publication-to-browser proof remain open. P owns package/IAM composition, including publication.py, canonical naming runtime/registry/schema, versioned object read permissions and conditional writes. The new reader fails closed on old publications, so coordinated publisher/reader rollout and accepted canonical data remain required before live use. Browser header evidence remains separately pinned at `d4fca0e5692730e9f79c3fa013159ffa63ba5b6b`, reviewer `999ed596ea`; this candidate does not compose the browser HTTP path with the accepted publication reader.

Push state LOCAL, no push by this seat. Measured local remote-tracking `origin/CLOUD`: `b8136f26dca101d9f0f74818df109f25cae5354d`; no fetch implied. Compiler reads used bare comp-which/comp-read then exact source/diff/test instruments. Stale risk-map PARTIAL_OR_BLIND is not clearance; Markdown gates do not substitute these runtime tests. Return this bounded result to COO~M/CTO and P/Y consumers without widening it to full acceptance.

## Durable reproduction

Save the following as `test_publication_621_review.py`, keep its ROOT pinned to the isolated checkout above, and run the pytest command in the table. SHA256: `D0C7CE716B02DB41BFD8E6CB9DE07FDEB8538BAAAF9A4047E531FA1C860A1CCD`. Raw case output: `.runtime/codex-seats/3.0.0_SA_CVO~M/publication_621_review_results.txt`. The complete driver is embedded so the fault schedule does not depend on transient runtime files.

```python
"""Independent fault schedules over real publisher/reader/Entry; no network."""
import copy
import hashlib
import io
import json
import sys
from pathlib import Path
import pytest
from botocore.exceptions import ClientError

ROOT = Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
TESTS = ROOT / 'infra/aws/lambda/investor-reporting/holdings/tests'
sys.path.insert(0, str(TESTS))
sys.path.insert(0, str(ROOT / 'lib'))
import test_publication_entry as E
from test_entry_guarded import harness, call, refused
import publication as P
import test_snapshot as T


class Transport:
    """Separate version store, opaque ETags, logs and injected fault boundaries."""
    def __init__(self):
        self.head = {}
        self.versions = {}
        self.calls = []
        self.counter = 0
        self.fault = None

    @staticmethod
    def stage(key):
        if key.endswith('/current/manifest.json'): return 'index'
        if key.endswith('.parquet'): return 'gold'
        if key.endswith('.manifest.json'): return 'manifest'
        return 'platinum'

    def matches(self, operation, kw):
        return self.fault and self.fault[:2] == (operation, self.stage(kw['Key']))

    def put_object(self, **kw):
        self.calls.append(('put', dict(kw)))
        key = (kw['Bucket'], kw['Key'])
        old = self.head.get(key)
        if (kw.get('IfNoneMatch') == '*' and old is not None or
            'IfMatch' in kw and (old is None or self.versions[key + (old,)][1] != kw['IfMatch'])):
            raise ClientError({'Error': {'Code': 'PreconditionFailed'}}, 'PutObject')
        fault = self.fault[2] if self.matches('put', kw) else None
        if fault == 'before': raise TimeoutError('injected before persistence')
        self.counter += 1
        version = 'null' if fault == 'suspended' else 'version-' + str(self.counter)
        etag = '"opaque-' + str(self.counter) + '"'
        self.versions[key + (version,)] = (bytes(kw['Body']), etag)
        self.head[key] = version
        if fault == 'after': raise TimeoutError('injected after persistence')
        return {'VersionId': version, 'ETag': etag}

    def get_object(self, **kw):
        self.calls.append(('get', dict(kw)))
        key = (kw['Bucket'], kw['Key'])
        version = kw.get('VersionId', self.head.get(key))
        item = self.versions.get(key + (version,))
        if item is None: raise ClientError({'Error': {'Code': 'NoSuchKey'}}, 'GetObject')
        body, etag = item
        if self.matches('get', kw):
            if self.fault[2] == 'bytes': body += b'corruption'
            if self.fault[2] == 'version': version = 'other-version'
        return {'VersionId': version, 'ETag': etag, 'Body': io.BytesIO(body)}


def doc(revision='one'):
    payload = E.payload()
    payload['source_set_revision'][0]['revision'] = revision
    return payload


def land(s3, revision='one', date=T.CUSTODY, expected=None, qa=False):
    publisher = P.HoldingsPublication(s3, T.FIRM, qa=qa)
    return E.writer.land('opal-data-49financial', E.writer.QA_PREFIX if qa else E.writer.PROD_PREFIX,
        date, doc(revision), True, None, s3_client=s3,
        expected=publisher.begin() if expected is None else expected)


def assert_selected(harness, s3, monkeypatch, revision):
    E.attach_reader(harness, s3, monkeypatch)
    answer = call(harness)
    assert answer['data']['scope']['account_ids'] == [T.A1]
    assert answer['data']['custody_totals']['total_market_value']['value'] == 100
    assert any(row['revision'] == revision for row in answer['data']['source_set_revision'])
    assert '_accepted_publication' not in answer['data']


@pytest.mark.parametrize('stage', ['gold', 'platinum', 'manifest'])
@pytest.mark.parametrize('fault', [('put', 'before'), ('get', 'bytes'), ('get', 'version')])
def test_each_artifact_failure_preserves_guarded_accepted_revision(harness, monkeypatch, stage, fault):
    s3 = Transport()
    first = land(s3)
    store = P.HoldingsPublication(s3, T.FIRM)
    prior = copy.deepcopy(store.begin())
    s3.fault = (fault[0], stage, fault[1])
    # The guarded route loader reloads flat modules; use its current exception
    # identity as well as the initially imported reader's identity.
    with pytest.raises((P.PublicationRefused, sys.modules['publication'].PublicationRefused, TimeoutError)):
        land(s3, 'failed-correction', expected=prior)
    s3.fault = None
    assert store.begin() == prior
    assert_selected(harness, s3, monkeypatch, first['revision'])


@pytest.mark.parametrize('initial', [False, True])
def test_stale_publisher_loses_to_competing_conditional_index(harness, monkeypatch, initial):
    s3 = Transport()
    store = P.HoldingsPublication(s3, T.FIRM)
    if initial: land(s3)
    stale = store.begin()
    winner = land(s3, 'winner', expected=stale)
    with pytest.raises(ClientError): land(s3, 'loser', expected=stale)
    assert_selected(harness, s3, monkeypatch, winner['revision'])


def test_same_day_correction_retains_original_exact_version(harness, monkeypatch):
    s3 = Transport()
    first = land(s3)
    old_versions = copy.deepcopy(s3.versions)
    second = land(s3, 'same-day-correction')
    assert first['revision'] != second['revision']
    assert all(s3.versions[key] == value for key, value in old_versions.items())
    assert_selected(harness, s3, monkeypatch, second['revision'])


def test_unconditional_later_blob_version_cannot_substitute_pinned_version(harness, monkeypatch):
    s3 = Transport()
    first = land(s3)
    accepted = E.REAL_LOAD(T.FIRM, s3_client=s3)
    for family in ['platinum', 'gold']:
        ref = accepted['_accepted_publication'][family]
        s3.put_object(Bucket=ref['bucket'], Key=ref['key'], Body=b'new unaccepted version')
    assert_selected(harness, s3, monkeypatch, first['revision'])


@pytest.mark.parametrize('target', ['bucket', 'key', 'version_id', 'sha256', 'byte_length'])
def test_referenced_platinum_fault_refuses_without_legacy_fallback(harness, monkeypatch, target):
    s3 = Transport()
    first = land(s3)
    store = P.HoldingsPublication(s3, T.FIRM)
    index = store.begin()['document']
    ref = first['accepted']['manifest']
    manifest = json.loads(s3.versions[(ref['bucket'], ref['key'], ref['version_id'])][0])
    replacements = {'bucket':'opal-data-cottonwood', 'key':'investor-reporting/holdings/latest.json',
                    'version_id':'missing', 'sha256':'0'*64, 'byte_length':True}
    manifest['platinum'][target] = replacements[target]
    body = P.canonical_bytes(manifest)
    receipt = s3.put_object(Bucket=ref['bucket'], Key=ref['key'], Body=body)
    index['dates'][T.CUSTODY]['manifest'] = dict(ref, version_id=receipt['VersionId'],
        sha256=P.digest(body), byte_length=len(body))
    bucket, key = store.location('platinum', 'current', 'manifest.json')
    s3.put_object(Bucket=bucket, Key=key, Body=P.canonical_bytes(index))
    start = len(s3.calls)
    E.attach_reader(harness, s3, monkeypatch)
    refused(call(harness), 'NOT_READY')
    reads = [kw for op, kw in s3.calls[start:] if op == 'get']
    assert all(kw['Bucket']=='opal-data-49financial' for kw in reads)
    assert all(not kw['Key'].startswith('investor-reporting/') for kw in reads)


def test_qa_and_legacy_objects_never_become_prod_fallback(harness, monkeypatch):
    s3 = Transport()
    land(s3, qa=True)
    s3.put_object(Bucket='opal-data-49financial', Key='investor-reporting/holdings/latest.json',
                  Body=P.canonical_bytes(doc()))
    E.attach_reader(harness, s3, monkeypatch)
    refused(call(harness), 'NOT_READY')


def test_requested_missing_date_does_not_fall_back_to_latest(harness, monkeypatch):
    s3 = Transport()
    land(s3)
    harness['event']['queryStringParameters'] = {'as_of':'2026-09-09'}
    E.attach_reader(harness, s3, monkeypatch)
    refused(call(harness), 'NOT_READY')


@pytest.mark.parametrize('mode', ['before', 'after', 'suspended'])
def test_final_index_outcomes_are_not_a_rollback_promise(harness, monkeypatch, mode):
    s3 = Transport()
    first = land(s3)
    store = P.HoldingsPublication(s3, T.FIRM)
    prior = copy.deepcopy(store.begin())
    s3.fault = ('put', 'index', mode)
    with pytest.raises((TimeoutError, P.PublicationRefused, sys.modules['publication'].PublicationRefused)):
        land(s3, 'final-index', expected=prior)
    s3.fault = None
    if mode == 'before':
        assert store.begin() == prior
        assert_selected(harness, s3, monkeypatch, first['revision'])
    elif mode == 'after':
        current = store.begin()
        assert current != prior
        revision = current['document']['dates'][T.CUSTODY]['revision']
        assert revision != first['revision']
        assert_selected(harness, s3, monkeypatch, revision)
    else:
        key = store.location('platinum', 'current', 'manifest.json')
        assert s3.head[key] == 'null'
        E.attach_reader(harness, s3, monkeypatch)
        refused(call(harness), 'NOT_READY')


@pytest.mark.parametrize('change', ['revoke','directory','selection'])
def test_post_versioned_read_current_access_refuses(harness, monkeypatch, change):
    s3 = Transport()
    land(s3)
    def mutate():
        if change=='revoke': harness['accounts']=[T.A2,T.A3]
        elif change=='directory': harness['directory']['revision']='changed'
        else: harness['rows'].clear()
    E.attach_reader(harness, s3, monkeypatch, after_read=mutate)
    refused(call(harness), 'OBJECT_NOT_COVERED')

```
