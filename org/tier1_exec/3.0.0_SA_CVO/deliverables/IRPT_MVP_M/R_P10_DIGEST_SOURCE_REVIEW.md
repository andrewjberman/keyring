# R-P10 independent publication digest-type source review

Reviewer `3.0.0_SA_CVO~M`; 2026-09-23 UTC. Authority: completion CONTRACT and
CTO's exact 00:33:40Z R-P10 assignment. The reviewed P finding is `142e5a27a4`,
HOLDINGS_INVENTORY_REVIEW_F886.md, on package `f8860f9839357a80951fa9fce6ca2ed406997734`.
P's package results are attributed; this seat independently tests the source boundary.

## Original source result: R-P10 OPEN

Exact source `fd4690b4ffca23f2616fe5f19d90737af6fe3a58`, clean detached reviewer
checkout `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`.
Independent actual publisher/reader/guarded Entry matrix: **12 PASS, 2 FAIL in
2.10s**, pytest exit 1. Both original-type failures are retained as failed refusal
assertions, not xfail or redefined accepted behavior.

An accepted multipart manifest separately has the unselected-part `sha256`, then
Gold `sha256`, replaced by `int('1' * 64)`. Each modified outer manifest is
reserialized and its exact version/real hash/length repinned into the index.
Selected Entry releases data in both cases after four GETs. Neither the unselected
part nor Gold is fetched. `validate_reference` coerces the digest with `str()`
before applying its pattern, so JSON integers are admitted as hash strings for
metadata-only references. Selected-object byte verification would independently
compare the actual string digest; these cases exercise the intentionally unread
objects in the complete inventory.

For each target, float, boolean, null, array and object digest forms refuse.
Restoring the original valid digest string for each target serves exactly A1,
value 100, the accepted revision and four GETs, with no unselected/Gold retrieval.
The driver reuses the earlier independent versioned transport and producer fixture
shape; mutations, repinning, assertions and counts are independently implemented.
This is synthetic accepted storage and real source Entry execution, not a live
injection path or cross-tenant disclosure demonstration.

Required closure: strict string typing before exact lowercase 64-hex matching,
without digest coercion, preserving original valid-string behavior, inventory
metadata refusal and selected-only retrieval. Rerun this driver unchanged plus
the prior 22 unchanged multipart assertions and supplied holdings suite on the
exact committed remedy. CVO~P separately reruns its original packaged failures
and controls against a rebuilt exact package. Source closure alone cannot close
consumer HOLD `dfc19fdd84` or substitute for that package proof.

M-PART-01 and M-FACT-01 keep their prior bounded scopes. Original economics,
source cutoff, cross-date custody/overlay evidence, final-index timeout/versioning
and live/full-grade limits remain unchanged. No producer implementation was edited.
The exact remedy pin was requested from COO~M; at this initial evidence record,
source repair and independent remedy closure are pending.

## Reproduction

The original adjacent multipart driver and transport are embedded in review
`3a2f4efdd8`; the new driver below imports them. Its fixed source checkout must be
at the exact pin under review. Execute:

```powershell
python -m pytest .runtime/codex-seats/3.0.0_SA_CVO~M/test_rp10_digest_review.py -q --tb=short
```

SHA-256: `d409306709dcdef1d02cc5e7668a91634b9db7883b1cae8153918a0dfdfa538f`.

```python
"""R-P10 source-boundary assertions over real publisher/reader/guarded Entry."""
import copy,json,sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).parent))
import test_multipart_9e_review as M
from test_entry_guarded import harness,call,refused

BAD=[int('1'*64),1e63,True,None,['1'*64],{'value':'1'*64}]
@pytest.mark.parametrize('target',['unselected-part','gold'])
@pytest.mark.parametrize('value',BAD,ids=['integer64','float','boolean','null','array','object'])
def test_digest_requires_actual_string_at_guarded_entry(harness,monkeypatch,target,value):
    state=M.setup(monkeypatch)
    p,s,_,_,_,_,manifest=state
    if target=='gold':ref=manifest['gold']
    else:ref=next(x['object'] for x in manifest['partitions'] if M.T.A1 not in x['account_ids'])
    excluded=ref['key']
    ref['sha256']=value
    M.publish_manifest(state)
    s.calls.clear()
    M.E.attach_reader(harness,s,monkeypatch)
    answer=call(harness)
    reads=[kw for op,kw in s.calls if op=='get']
    assert all(kw['Key']!=excluded and not kw['Key'].endswith('.parquet') for kw in reads)
    print(json.dumps({'target':target,'digest_type':type(value).__name__,'data_released':'data' in answer,'storage_reads':len(reads)}))
    refused(answer,'NOT_READY')

@pytest.mark.parametrize('target',['unselected-part','gold'])
def test_restored_valid_digest_string_serves_exact_selection(harness,monkeypatch,target):
    state=M.setup(monkeypatch)
    p,s,first,_,_,_,manifest=state
    ref=manifest['gold'] if target=='gold' else next(x['object'] for x in manifest['partitions'] if M.T.A1 not in x['account_ids'])
    original=copy.deepcopy(ref)
    ref['sha256']=int('1'*64)
    M.publish_manifest(state)
    ref.clear();ref.update(original)
    assert isinstance(ref['sha256'],str) and len(ref['sha256'])==64
    M.publish_manifest(state)
    s.calls.clear()
    M.E.attach_reader(harness,s,monkeypatch)
    answer=call(harness)
    assert answer['data']['scope']['account_ids']==[M.T.A1]
    assert answer['data']['custody_totals']['total_market_value']['value']==100
    assert any(row['revision']==first['revision'] for row in answer['data']['source_set_revision'])
    reads=[kw for op,kw in s.calls if op=='get']
    assert len(reads)==4
    assert all(kw['Key']!=ref['key'] and not kw['Key'].endswith('.parquet') for kw in reads)

```


## Source-boundary closure at fdd02de5b2

Date: 2026-09-23 UTC. **R-P10 source-boundary repair CLOSED** at exact LOCAL
`fdd02de5b2519dfdf26a8f09b44d66b18ba73b11`, parent
`6ad86009fe5d42d57235095dcda2cffd7b952078`.
This supersedes the source OPEN disposition above; the original failure record
and assertions are preserved. **Consumer/package HOLD remains pending CVO~P's
unchanged packaged probes against the replacement package.**

The clean detached reviewer checkout was switched to the exact remedy. The only
implementation change requires `isinstance(ref.get("sha256"), str)` before
matching the same lowercase 64-hex grammar and removes the prior coercion.
Location/version/size checks, inventory census, selected retrieval/request bounds,
byte verification and publication behavior remain unchanged. The commit adds
20 supplied type/format controls and a repair evidence document; it excludes the
separate legacy-read patch and includes no package/IAM/storage-address changes.

Independent results, all exit 0:

- Supplied holdings suite: **116 PASS in 2.46s**.
- Original R-P10 driver: **14 PASS in 1.63s**, unchanged SHA-256
  `d409306709dcdef1d02cc5e7668a91634b9db7883b1cae8153918a0dfdfa538f`.
- Original multipart driver: **22 PASS in 2.03s**, unchanged SHA-256
  `0970af07522bb6a70efe92476098e7e2e57496fc1a237a4f03828659ce2503bf`.

Both independently reproduced numeric digest cases now refuse the whole Entry
response. Restored actual valid strings still serve the exact selected account
and revision with four storage GETs and no unselected-part/Gold fetch. The added
supplied cases preserve all-digit and mixed lowercase-hex strings as valid
metadata and reject wrong JSON types, short strings and uppercase strings before
part reads. Such metadata positives do not establish hashes of unfetched bytes.
The prior inventory, interruption, selected-bound, revocation and revision-pinning
controls remain passing. No tests or producer implementation were edited by this
reviewer, and the review checkout is clean.

No new source-economic acceptance, live/package grade, deployment or final-index
rollback guarantee follows. Original economic failures and index timeout/versioning
limitations remain open. CVO~P owns the separate rebuilt-package verdict.
