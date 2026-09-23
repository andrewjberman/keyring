# Independent multipart review and original failure replay

Reviewer: `3.0.0_SA_CVO~M`. Authority: completion `CONTRACT.md` v1.2 and
IRPT-M-BASIS-01 (`b8de4c3899`). Review date: 2026-09-22 UTC.

## Disposition

**HOLD complete-inventory acceptance at `9e5739773094a69313a8ae8339bf8490443383f4`.**
The selected-data, count/byte-bound and release-authorization controls below pass,
but M-PART-01 remains open. No source-economic, normalized custody-port, live,
deployed, full-product or S7 acceptance is granted. The original economic failures
were independently reproduced without changing their assertions or analysis.

The review used a clean detached full checkout at
`C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`, first `554fc37e998554736ad98ccbfd872d400a9153ff`
and then the exact count-limit endpoint above. No implementation was edited.

## M-PART-01: incomplete unselected reference inventory is accepted

The actual guarded holdings Entry returns selected A1 data successfully when an
unselected v2 partition has either (a) no `object` member or (b) a reference with
foreign bucket, arbitrary key, null version, invalid hash and negative byte length.
The account memberships remain intact. The test rewrites the enclosing manifest
and index with valid exact-version/hash/length references, so it reaches semantic
inventory validation rather than merely failing the outer hash.

`HoldingsPublication._load_parts` checks every partition's account membership,
then validates object references only for selected partitions via `read_exact`.
Consequently the admitted manifest does not necessarily contain a complete pinned
inventory as specified in INTERFACES.md and IRPT-M-BASIS-01. This is a bounded
inventory-validation defect; it does **not** demonstrate a foreign-data read,
a permission bypass, or partial selected-account economics. The publisher's
normal output includes these references; the negative test exercises reader
acceptance of semantically invalid but byte-consistent accepted metadata.

Required closure: validate the presence, type, canonical destination/ordinal,
non-null version, digest and bounded integer length for **every** inventory
reference before selection. This does not require GETs of unselected parts and
must preserve selected-only retrieval and request bounds. Rerun both unchanged
negative assertions along with existing selected-part, census and count controls.

## Exercised evidence

- At `554fc37e99`: supplied holdings **85 PASS** (3.31s); Gold **85 PASS** (10.78s).
- At `9e57397730`: supplied holdings **89 PASS** (4.02s). Its delta changes
  publication count/request limits, associated holdings tests and INTERFACES only;
  no economic repair is represented. Gold caller tests were not claimed repaired.
- Independent final invocation: **20 PASS, 2 FAIL** (4.02s), pytest exit 1.
  The two failures are M-PART-01's expected whole-refusal assertions, retained as
  failures rather than xfail or redefined successful behavior.
- Passed missing selected version; bad selected hash/version/revision/account-tree
  census; bad header hash; duplicate and incomplete membership inventories;
  revocation, changed directory and deleted retained selection at release;
  exact one-part request allowance (4 application GETs), zero-part refusal
  (index/manifest/header only); reader account/part/byte caps before part GET;
  later unaccepted object heads cannot replace captured versions;
  interrupted header/part publication and corrupt part readback preserve the old
  accepted Entry revision; an index change during part retrieval does not mix
  accepted revisions.
- Tests use a reviewer-written in-memory versioned transport with opaque ETags,
  real candidate publisher/reader/guarded Entry, producer synthetic fixture data,
  and mocked authorization dependencies/selection store. They do not prove AWS
  IAM, deployed packaging, distributed atomic authorization, or live economics.
- Small JSON limits force multipart paths. These are controlled boundary tests,
  not an assertion that the real publication should use those reduced limits.
- Two earlier harness-only attempts each failed 18 setup checks: the route loader
  removes/reloads flat modules, first removing `publication` from `sys.modules`,
  then causing a stale module cap patch to leave the writer at v1. The final
  harness imports the current module after fixture setup and asserts its exact
  checked-out file path. No candidate code or tested refusal assertion changed.
- The shell command displaying the saved final pytest output returned 0 because
  it ended with Get-Content; the saved pytest result is explicitly **exit 1**.

Existing findings from review `c462d8b4df` remain open: a timeout after the final
index persists can leave a newly accepted publication despite caller failure;
suspended versioning can mutate the index then produce NOT_READY. No atomic
rollback promise follows from the successful pre-index interruption controls.

## Exact source replay

COO~M's frozen evidence bundle is
`C:/Users/AndrewBerman/Desktop/ajb_irpt_m/.runtime/basis-original-20260922/evidence.json`.
All six listed frozen files, the original snapshot and source-receipts file
matched their supplied SHA-256 values. The review independently fetched all six
S3 objects using the **explicit receipt VersionId**, verifying returned version,
byte length and digest. No live listing, source write or publication occurred.

The unchanged diagnostic and cash-probe scripts ran against the frozen original
runner and source_inputs.py. Their transport was replaced by a read-only cache of
those six verified exact versions; partition discovery was synthesized exclusively
from the pinned receipt inventory. Subsequent script reads used that cache, not
new network requests. Dependency/schema resolution used the reviewer checkout;
the endpoint's added publication limits do not change the failing build_49f.
The original script file bytes were not edited. This preserves the original
analysis while replacing mutable discovery with the required exact replay.

Both generated diagnostic reports equal the originals structurally and in every
reported value. The whole rebuilt snapshot equals the original after replacing
only `clocks.as_of_timestamp` with the original build time. No other field was
normalized. There are 5,917 accounts, 127,925 nodes, 7,479 failing parent/basis
partitions; schema validation passes while reconciliation returns false even
though the two top-level totals are both 1,506,694,007.25. The original cash probe
counts 7,501 position totals differing from equity and 8 matching to the cent.
These are failure-reproduction facts, not an accepted reconciliation tolerance.

The six receipts comprise four SmartX Silver families plus the directory pointer
and directory document. They do **not** supply independently enumerated custody
roots. The source repair must still preserve distinct longEquity, shortEquity,
cash and equity lineage and the ruled gross/net bases; the historical test's
`equity + cash` expectation is not economic acceptance. This replay grants no
permission to plug, rescale, or substitute provider totals for custody.

Applying only the candidate's pure packing plan to the failed snapshot confirms
98,451,490 canonical public JSON bytes, a 185,159-byte header, 95 parts with a
maximum 1,048,576 bytes each, and all 5,917 root memberships. This exercises shape
only and writes nothing. It does not make the failed economics publishable.

### Replay verification

```json
{
  "frozen_files_verified": [
    "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py",
    "data/assets/scripts/gold/investor_reporting/source_inputs.py",
    ".runtime/m-49f-diagnostic.py",
    ".runtime/m-49f-cash-probe.py",
    ".runtime/m-49f-reconcile.json",
    ".runtime/m-49f-cash-probe.json"
  ],
  "source_versions_fetched_verified": 6,
  "live_listing_requests": 0,
  "write_requests": 0,
  "replay_cache_gets": 13,
  "original_reports_equal": {
    "m-49f-reconcile.json": true,
    "m-49f-cash-probe.json": true
  },
  "snapshot_equal_after_only_as_of_timestamp_normalization": true,
  "original_timestamp": "2026-09-22T23:22:15Z",
  "replay_timestamp": "2026-09-22T23:56:26Z",
  "nodes": 127925,
  "accounts": 5917,
  "mismatched_partitions": 7479
}
```

### Shape and aggregate failure evidence

```json
{
  "canonical_bytes": 98451490,
  "header_bytes": 185159,
  "parts": 95,
  "max_part_bytes": 1048576,
  "inventory_accounts": 5917,
  "writes": 0,
  "economics_accepted": false,
  "m-49f-reconcile.json": {
    "reconciliation": [
      false,
      1506694007.25,
      1506694007.25
    ],
    "schema": [
      true,
      []
    ],
    "nodes": 127925,
    "accounts": 5917,
    "source_receipts": 6,
    "mismatched_partitions": 7479
  },
  "m-49f-cash-probe.json": {
    "full_snapshot_canonical_bytes": 98453882,
    "counts": {
      "positions_differ_from_equity": 7501,
      "positions_match_equity_to_cent": 8
    }
  }
}
```

## Related X10 handoff boundary

COO~G message 99608 attributes bounded builder-owner PASS at LOCAL `136624e660`,
with two stale-stamp drain refusals and a carrier fork. These are G's measurements,
not reruns by this review. CTO's full IRPT-X10-INTEGRATION-01 ruling at
`f6a8721a5970f7964b75c18080853bdd7d88e680` was read: option A is builder/test/two
registry files only; M may separately regenerate its two owned source stamps
from the actual reconciled tree, preserving all current CTO rulings. CVO~M's
fresh integration review awaits M's exact candidate and staged gate/non-IRPT
proof. No carrier-copy, harvest/fmt rider, activation, deployment or broad drain
is inferred. This does not change the earlier bounded registry review.

## Reproduction scripts

Run the embedded files with these names in the exact seat runtime directory;
the multipart suite imports the adjacent prior reviewer transport module.
Commands from `ajb_workspace`:

```powershell
python .runtime/codex-seats/3.0.0_SA_CVO~M/replay_original_pinned.py
python .runtime/codex-seats/3.0.0_SA_CVO~M/review_original_shape.py
python -m pytest .runtime/codex-seats/3.0.0_SA_CVO~M/test_multipart_9e_review.py -q --tb=short
```

Replay needs existing read-only access to the six pinned source versions. Raw
customer rows remain in the ignored seat runtime; only aggregate evidence and
reproducible scripts are retained here. The source bundle's frozen originals and
receipt inventory must remain available; their hashes are checked before replay.

### replay_original_pinned.py

SHA-256: `12882c2a5ff4af65823d8e3e5b5ef9c50d5a041e1978a6b592eeda686838e65c`.

```python
import contextlib, hashlib, importlib.util, io, json, os, runpy, sys
from pathlib import Path
import boto3
BASE=Path(r'C:/Users/AndrewBerman/Desktop/ajb_irpt_m/.runtime/basis-original-20260922')
REVIEW=Path(r'C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
OUT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/original-pinned-replay')
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'.runtime').mkdir(exist_ok=True)
evidence=json.loads((BASE/'evidence.json').read_text())
verified=[]
for item in evidence['files']:
    raw=Path(item['frozen_path']).read_bytes()
    assert len(raw)==item['byte_length'] and hashlib.sha256(raw).hexdigest()==item['sha256'], item['original_path']
    verified.append(item['original_path'])
raw=Path(evidence['snapshot_path']).read_bytes()
assert hashlib.sha256(raw).hexdigest()==evidence['snapshot_sha256']
original=json.loads(raw)
receipts_raw=(BASE/'source-receipts.json').read_bytes()
assert hashlib.sha256(receipts_raw).hexdigest()==evidence['input_receipts_sha256']
receipts=json.loads(receipts_raw)
client=boto3.client('s3',region_name='us-east-1')
cache={}
for ref in receipts:
    result=client.get_object(Bucket=ref['bucket'],Key=ref['key'],VersionId=ref['version_id'])
    raw=result['Body'].read(ref['byte_length']+1)
    assert result.get('VersionId')==ref['version_id'] and len(raw)==ref['byte_length'] and hashlib.sha256(raw).hexdigest()==ref['sha256']
    cache[(ref['bucket'],ref['key'])]=(ref,raw)
print('Verified six frozen files, original snapshot and receipts; fetched and verified six exact S3 versions.',flush=True)
class Pinned:
    exceptions=client.exceptions
    calls=[]
    def get_object(self,**kw):
        ref,raw=cache[(kw['Bucket'],kw['Key'])]
        assert kw.get('VersionId',ref['version_id'])==ref['version_id']
        self.calls.append({**kw,'VersionId':ref['version_id']})
        return {'Body':io.BytesIO(raw),'VersionId':ref['version_id']}
    def get_paginator(self,name):
        assert name=='list_objects_v2'
        return self
    def paginate(self,**kw):
        assert kw['Delimiter']=='/'
        prefix=kw['Prefix']
        keys=[key for bucket,key in cache if bucket==kw['Bucket'] and key.startswith(prefix)]
        assert keys, 'Listing outside frozen inventory'
        yield {'CommonPrefixes':[{'Prefix':p} for p in sorted({prefix+key[len(prefix):].split('/')[0]+'/' for key in keys})]}
pinned=Pinned()
def load(name,path,logical=None):
    spec=importlib.util.spec_from_file_location(name,logical or path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    exec(compile(path.read_bytes(),str(path),'exec'),mod.__dict__)
    return mod
load('source_inputs',BASE/'source_inputs.py')
load('holdings_snapshot',BASE/'holdings_snapshot.py',REVIEW/'data/assets/scripts/gold/investor_reporting/holdings_snapshot.py')
boto3.client=lambda service,**kw: pinned if service=='s3' else (_ for _ in ()).throw(AssertionError(service))
os.chdir(OUT)
for name in ['m-49f-diagnostic.py','m-49f-cash-probe.py']:
    with (OUT/(name+'.stdout.txt')).open('w',encoding='utf-8') as stdout,contextlib.redirect_stdout(stdout):
        runpy.run_path(str(BASE/name),run_name='__main__')
    print('Completed unchanged '+name,flush=True)
comparison={}
for name in ['m-49f-reconcile.json','m-49f-cash-probe.json']:
    result=json.loads((OUT/'.runtime'/name).read_text())
    expected=json.loads((BASE/name).read_text())
    comparison[name]=result==expected
result=json.loads((OUT/'.runtime/m-49f-built.json').read_text())
oldclock=original['clocks'].get('as_of_timestamp')
newclock=result['clocks'].get('as_of_timestamp')
result['clocks']['as_of_timestamp']=oldclock
summary={'frozen_files_verified':verified,'source_versions_fetched_verified':len(cache),'live_listing_requests':0,'write_requests':0,'replay_cache_gets':len(pinned.calls),'original_reports_equal':comparison,'snapshot_equal_after_only_as_of_timestamp_normalization':result==original,'original_timestamp':oldclock,'replay_timestamp':newclock,'nodes':len(result['nodes']),'accounts':result['custody_totals']['unique_account_count'],'mismatched_partitions':json.loads((OUT/'.runtime/m-49f-reconcile.json').read_text())['mismatched_partitions']}
(OUT/'verification.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2),flush=True)

```

### review_original_shape.py

SHA-256: `4fb94ccf9292dabb75ab79162274809ea5a85dc6bbcfc7552ba6baa0b507c980`.

```python
import hashlib,json,sys
from pathlib import Path
root=Path(r'C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
sys.path.insert(0,str(root/'infra/aws/lambda/investor-reporting/holdings'))
import publication as p
base=Path(r'C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/original-pinned-replay')
doc=json.loads((base/'.runtime/m-49f-built.json').read_text())
doc={k:v for k,v in doc.items() if not k.startswith('_')}
body=p.canonical_bytes(doc)
header,parts=p._platinum_plan(doc,p.digest(body))
summary={'canonical_bytes':len(body),'header_bytes':len(header),'parts':len(parts),'max_part_bytes':max(len(body) for ids,body in parts),'inventory_accounts':sum(len(ids) for ids,body in parts),'writes':0,'economics_accepted':False}
for name in ['m-49f-reconcile.json','m-49f-cash-probe.json']:
    raw=json.loads((base/'.runtime'/name).read_text())
    summary[name]={k:v for k,v in raw.items() if k!='examples'}
(base/'shape-summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))

```

### test_multipart_9e_review.py

SHA-256: `0970af07522bb6a70efe92476098e7e2e57496fc1a237a4f03828659ce2503bf`.

```python
"""Independent v2 faults using reviewer transport and real guarded Entry; synthetic data."""
import copy, io, json, sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).parent))
import test_publication_621_review as V
E,T=V.E,V.T
from test_entry_guarded import harness,call,refused

def setup(monkeypatch):
    p=__import__('publication')
    assert Path(p.__file__).resolve()==(V.ROOT/'infra/aws/lambda/investor-reporting/holdings/publication.py').resolve()
    monkeypatch.setattr(p,'MAX_JSON_BYTES',6000)
    s=V.Transport()
    receipt=E.land(s,E.large_payload())
    pub=p.HoldingsPublication(s,T.FIRM)
    index=pub.begin()['document']
    mref=receipt['accepted']['manifest']
    manifest=json.loads(s.versions[(mref['bucket'],mref['key'],mref['version_id'])][0])
    assert manifest['schema_version']=='irpt-holdings-manifest-v2'
    return p,s,receipt,pub,index,mref,manifest

def replace_ref(s,p,ref,body):
    response=s.put_object(Bucket=ref['bucket'],Key=ref['key'],Body=body)
    return dict(ref,version_id=response['VersionId'],sha256=p.digest(body),byte_length=len(body))

def publish_manifest(state):
    p,s,receipt,pub,index,mref,manifest=state
    index['dates'][T.CUSTODY]['manifest']=replace_ref(s,p,mref,p.canonical_bytes(manifest))
    bucket,key=pub.location('platinum','current','manifest.json')
    s.put_object(Bucket=bucket,Key=key,Body=p.canonical_bytes(index))

def selected(manifest):
    return next(x for x in manifest['partitions'] if T.A1 in x['account_ids'])

@pytest.mark.parametrize('fault',['missing','hash','version','revision','census','header','duplicate','inventory'])
def test_v2_selected_or_inventory_damage_refuses_entry(harness,monkeypatch,fault):
    state=setup(monkeypatch)
    p,s,_,_,_,_,m=state
    part=selected(m); ref=part['object']
    identity=(ref['bucket'],ref['key'],ref['version_id'])
    if fault=='missing': del s.versions[identity]
    elif fault=='hash': part['object']['sha256']='0'*64
    elif fault=='version': part['object']['version_id']='nonexistent-version'
    elif fault in ['revision','census']:
        body=json.loads(s.versions[identity][0])
        if fault=='revision': body['revision']='other-accepted-revision'
        else: body['nodes']=[n for n in body['nodes'] if n['node_id']!=T.A1]
        part['object']=replace_ref(s,p,ref,p.canonical_bytes(body))
    elif fault=='header': m['platinum_header']['sha256']='0'*64
    elif fault=='duplicate': m['partitions'].append(copy.deepcopy(part))
    else: m['partitions']=[part]
    publish_manifest(state)
    s.calls.clear()
    E.attach_reader(harness,s,monkeypatch)
    refused(call(harness),'NOT_READY')
    assert not any(op=='get' and kw['Key'].endswith('.parquet') for op,kw in s.calls)

@pytest.mark.parametrize('change',['revoke','directory','selection'])
def test_v2_release_rechecks_current_access(harness,monkeypatch,change):
    p,s,*_=setup(monkeypatch)
    def mutate():
        if change=='revoke': harness['accounts']=[T.A2,T.A3]
        elif change=='directory': harness['directory']['revision']='different'
        else: harness['rows'].clear()
    E.attach_reader(harness,s,monkeypatch,after_read=mutate)
    refused(call(harness),'OBJECT_NOT_COVERED')

def test_v2_request_limit_checks_before_parts_and_exact_limit_serves(harness,monkeypatch):
    p,s,_,pub,_,_,m=setup(monkeypatch)
    monkeypatch.setattr(p,'MAX_SELECTED_PART_READS',1)
    s.calls.clear()
    E.attach_reader(harness,s,monkeypatch)
    answer=call(harness)
    assert answer['data']['scope']['account_ids']==[T.A1]
    assert answer['data']['custody_totals']['total_market_value']['value']==100
    assert '_accepted_publication' not in answer['data']
    assert sum(op=='get' for op,kw in s.calls)==4
    monkeypatch.setattr(p,'MAX_SELECTED_PART_READS',0)
    s.calls.clear()
    refused(call(harness),'NOT_READY')
    assert sum(op=='get' for op,kw in s.calls)==3
    assert not any(op=='get' and '.part' in kw['Key'] for op,kw in s.calls)

@pytest.mark.parametrize('cap',['MAX_PUBLICATION_ACCOUNTS','MAX_PUBLICATION_PARTS','MAX_SELECTED_READ_BYTES'])
def test_v2_count_and_byte_limits_refuse_entry(harness,monkeypatch,cap):
    p,s,*_=setup(monkeypatch)
    monkeypatch.setattr(p,cap,1)
    s.calls.clear()
    E.attach_reader(harness,s,monkeypatch)
    refused(call(harness),'NOT_READY')
    assert not any(op=='get' and '.part' in kw['Key'] for op,kw in s.calls)

def test_v2_pins_survive_unaccepted_later_heads(harness,monkeypatch):
    p,s,receipt,_,_,_,m=setup(monkeypatch)
    for ref in [m['platinum_header']]+[x['object'] for x in m['partitions']]:
        s.put_object(Bucket=ref['bucket'],Key=ref['key'],Body=b'not accepted')
    E.attach_reader(harness,s,monkeypatch)
    answer=call(harness)
    assert answer['data']['scope']['account_ids']==[T.A1]
    assert any(row['revision']==receipt['revision'] for row in answer['data']['source_set_revision'])

@pytest.mark.parametrize('fault',['missing-reference','foreign-reference'])
def test_complete_inventory_requires_unselected_pinned_reference(harness,monkeypatch,fault):
    state=setup(monkeypatch)
    p,s,_,_,_,_,m=state
    other=next(x for x in m['partitions'] if T.A1 not in x['account_ids'])
    if fault=='missing-reference': del other['object']
    else: other['object']={'bucket':'other-firm','key':'arbitrary','version_id':'null','sha256':'invalid','byte_length':-1}
    publish_manifest(state)
    E.attach_reader(harness,s,monkeypatch)
    refused(call(harness),'NOT_READY')

@pytest.mark.parametrize('fault',['header-before','part-before','part-readback'])
def test_v2_interrupted_artifacts_keep_old_accepted_entry(harness,monkeypatch,fault):
    p=__import__('publication')
    monkeypatch.setattr(p,'MAX_JSON_BYTES',6000)
    class FaultTransport(V.Transport):
        enabled=False
        def put_object(self,**kw):
            if self.enabled and ((fault=='header-before' and kw['Key'].endswith('.header.json')) or (fault=='part-before' and '.part' in kw['Key'])):
                raise TimeoutError('before v2 artifact persistence')
            return super().put_object(**kw)
        def get_object(self,**kw):
            result=super().get_object(**kw)
            if self.enabled and fault=='part-readback' and '.part' in kw['Key']:
                result['Body']=io.BytesIO(result['Body'].read()+b'corrupt')
            return result
    s=FaultTransport()
    original=E.land(s,E.payload())
    pub=p.HoldingsPublication(s,T.FIRM)
    before=pub.begin()
    s.enabled=True
    with pytest.raises((TimeoutError,p.PublicationRefused)):
        E.land(s,E.large_payload())
    s.enabled=False
    assert pub.begin()==before
    E.attach_reader(harness,s,monkeypatch)
    answer=call(harness)
    assert any(row['revision']==original['revision'] for row in answer['data']['source_set_revision'])

def test_v2_index_change_mid_read_does_not_mix_revisions(harness,monkeypatch):
    p,s,first,pub,_,_,_=setup(monkeypatch)
    original_get=s.get_object
    switched=[]
    def get_object(**kw):
        if '.part' in kw['Key'] and not switched:
            switched.append(True)
            newer=E.large_payload()
            newer['source_set_revision'][0]['revision']='second-accepted-revision'
            E.land(s,newer)
        return original_get(**kw)
    monkeypatch.setattr(s,'get_object',get_object)
    E.attach_reader(harness,s,monkeypatch)
    answer=call(harness)
    assert switched
    assert any(row['revision']==first['revision'] for row in answer['data']['source_set_revision'])
    assert pub.begin()['document']['dates'][T.CUSTODY]['revision']!=first['revision']

```

### test_publication_621_review.py

SHA-256: `d0c7ce716b02db41bfd8e6cb9de07fdeb8538baaaf9a4047e531fa1c860a1ccd`.

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

