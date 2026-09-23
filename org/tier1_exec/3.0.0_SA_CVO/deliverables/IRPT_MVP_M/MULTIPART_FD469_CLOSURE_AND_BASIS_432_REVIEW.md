# Multipart inventory closure and bounded valuation-source review

Reviewer: `3.0.0_SA_CVO~M`. Date: 2026-09-23 UTC.
Authority: completion CONTRACT v1.2 and IRPT-M-BASIS-01.

## M-PART-01: CLOSED at exact fd469 remedy

Exact endpoint: `fd4690b4ffca23f2616fe5f19d90737af6fe3a58` in the clean detached
reviewer checkout `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`.
The independent suite from review `3a2f4efdd8` ran **unchanged**, including both
negative assertions that failed at `9e57397730`: **22 PASS in 3.18s**.
Its SHA-256 remains
`0970af07522bb6a70efe92476098e7e2e57496fc1a237a4f03828659ce2503bf`.
Supplied holdings suite: **96 PASS in 3.32s**. Both pytest processes exited 0.

The repair factors reference-metadata validation out of `read_exact`, validates
Gold metadata at manifest admission and every partition reference before selected
retrieval. It checks object mapping type, exact canonical bucket/key/part ordinal,
non-null version, digest shape and bounded positive integer byte length. This
closes acceptance of absent/malformed unselected references while retaining
selected-only GETs. The seven new supplied controls separately cover missing
reference, bucket, key, version, hash, size and Gold metadata; they also assert
no GET of unselected parts or Gold. Byte/count/request limits and IAM did not
change in this repair. No implementation changes were made by the reviewer.

Closure is specific to complete inventory **metadata** acceptance. Unselected
physical object bytes are intentionally not fetched. The existing final-index
post-persist timeout ambiguity and suspended-versioning findings remain open.
The 7,479 original source reconciliation failures remain open. No economic,
normalized-custody, package, live, deployed or full S7 acceptance follows.

CVO~P's attributed addendum `dfc19fdd84` holds package/consumer approval pending
renewed package proof at the eventual reviewed endpoint. The earlier package
proof `198d9a29c8` tested absent unselected physical blobs with intact references;
it did not contradict M-PART-01. P must evaluate the repaired endpoint separately.

## New helper: bounded evidence and M-FACT-01 type finding

Reviewed helper source: `432d068c46` (unchanged by the fd469 remedy).
Supplied helper tests: **26 PASS in 0.13s** at that exact source pin.
Independent helper controls: **11 PASS, 1 FAIL in 0.32s**, exit 1.

Passing controls cover signed negative cash with separately retained long/short/
net/gross facts, no mutation of supplied evidence, exact lineage propagation,
blank/overlong scope, unsupported currency, invalid revision length/case,
fractional/negative/boolean population counts, integer/text symbol collisions,
and finite wire-number range.

**M-FACT-01 OPEN:** `allocation_facts(..., source_revision=int("1" * 64))`
passes its revision guard because it regex-matches `str(source_revision)`, then
emits the original integer in every fact. The agreed fact seam requires a
lowercase 64-hex **string**. This is a bounded type/lineage guard defect, not an
observed production economic error; the helper is not wired into the serving
builder. Require a string before validating the hash and rerun the unchanged
`test_receipt_revision_must_be_a_hash_string_not_integer` negative assertion.
COO~M received the exact reproduction before this review commit.

The helper's equations and signed-value handling pass the exercised valid inputs.
This does not certify the caller's scope/revision binding; the caller must supply
an actual opaque allocation reference and the digest of complete receipts.

## Independent nine-version source check

Using committed `BASIS_SOURCE_EVIDENCE.json`, this seat independently performed
nine **explicit VersionId** S3 GETs: six custody-chain objects and three original
SmartX mapping/valuation/position objects. Every response version, byte length
and SHA-256 matched its pinned receipt. No listing, latest-version substitution,
source write or publication occurred. Source rows stayed in memory; the retained
result contains only aggregate facts, clock metadata and object receipts.

All 10,061 valuation rows and all 120,639 positions pass the new helper with
same-owner and same-calendar-date checks, declared position counts, distinct
symbol identities, signed positions plus cash equaling vendor net, and long plus
signed short plus cash equaling vendor net. The reviewer also checked valuation
owner uniqueness and that no position owner is absent from the valuation table.
The six aggregate fact sums match the producer diagnostic (comparison tolerance
0.0001 only for whole-source floating summation); the helper's per-allocation
reconciliation tolerance remains 0.01. These whole-source sums are not custody
root values. The diagnostic scope is explicitly NON_SERVING.

The pinned canonical valuation has 7,522 distinct account roots with no duplicate
root rows; its account set equals the independently loaded IN_CLIENT_BOOK
boundary. The overlay map has 5,917 accounts: 1,622 custody-only and 17 overlay-only.
The historical account dimension has 8,799 accounts; 1,277 lack current custody
valuation, including 1,176 marked open. Canonical positions contain 106,370 rows
across 6,315 accounts. There are five negative and 884 zero custody root values.

Custody business date is 2026-09-21 while both SmartX fact sources have actual
as-of timestamps on 2026-09-22. The displayed calendar-date rollup below is for
readability; the retained runtime result contains the distinct original source
timestamps. This cross-date coverage diagnostic cannot justify economic splicing,
residual allocation or historical membership inference. The enumerated custody
set proves only the measured canonical/Schwab-master chain and boundary, not all
possible 49F custody sources. Original build_49f remains invalid and unwired.

### Aggregate result

```json
{
  "source_versions_fetched_verified": 9,
  "live_listings": 0,
  "writes": 0,
  "helper_allocations_reconciled": 10061,
  "position_rows": 120639,
  "negative_net": 529,
  "zero_net": 2045,
  "empty_reported_positions": 2070,
  "helper_fact_totals": {
    "SMARTX_GROSS_AUM": 1494048625.227404,
    "SMARTX_NET_EQUITY": 1444544908.6874025,
    "SMARTX_LONG_EQUITY": 1479507971.53,
    "SMARTX_SHORT_EQUITY": -49503716.540000014,
    "SMARTX_CASH": 14540653.697399994,
    "SMARTX_SIGNED_POSITIONS": 1430004254.9899988
  },
  "custody_unique_roots": 7522,
  "custody_matches_in_client_book": true,
  "overlay_accounts": 5917,
  "custody_without_overlay": 1622,
  "overlay_without_custody": 17,
  "historical_accounts": 8799,
  "historical_without_current_custody": 1277,
  "open_historical_without_current_custody": 1176,
  "custody_position_rows": 106370,
  "custody_position_accounts": 6315,
  "custody_negative_roots": 5,
  "custody_zero_roots": 884,
  "custody_dates": [
    "2026-09-21"
  ],
  "valuation_dates": [
    "2026-09-22"
  ],
  "position_dates": [
    "2026-09-22"
  ],
  "source_economics_accepted": false,
  "custody_dates_distinct_timestamps": 1,
  "valuation_dates_distinct_timestamps": 10056,
  "position_dates_distinct_timestamps": 7987
}
```

## Reproduction

The unchanged multipart driver is embedded in the prior review `3a2f4efdd8`; use it and its adjacent transport dependency against the exact fd469 reviewer checkout.

```powershell
python -m pytest infra/aws/lambda/investor-reporting/holdings/tests -q
python -m pytest C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M/test_multipart_9e_review.py -q
```

### test_valuation_432_review.py

SHA-256: `f445cfca3971b5a8ced6bf5ffed0afd82f8916346ab331649d7be579fe454741`.

```python
import copy,sys
from pathlib import Path
import pytest
ROOT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
sys.path.insert(0,str(ROOT/'data/assets/scripts/gold/investor_reporting'))
from smartx_valuation import allocation_facts,BasisRefused

def inputs():
    return dict(owner_id='a',as_of='2026-09-22',long_equity='125.25',short_equity='-25.25',cash='-10.50',equity='89.50',total_count=2),[dict(owner_id='a',as_of='2026-09-22',symbol_id=11,market_value='125.25'),dict(owner_id='a',as_of='2026-09-22',symbol_id=22,market_value='-25.25')]

def invoke(v,p,**kwargs):
    return allocation_facts(v,p,**dict(dict(source_scope='opaque:allocation:a',source_revision='a'*64,units='USD'),**kwargs))

def test_signed_cash_and_decimal_facts_preserve_sources_without_mutation():
    v,p=inputs(); before=copy.deepcopy((v,p))
    result=invoke(v,p)
    values={x['fact_kind']:x['value'] for x in result}
    assert values==dict(SMARTX_GROSS_AUM=114.75,SMARTX_NET_EQUITY=89.5,SMARTX_LONG_EQUITY=125.25,SMARTX_SHORT_EQUITY=-25.25,SMARTX_CASH=-10.5,SMARTX_SIGNED_POSITIONS=100.0)
    assert (v,p)==before
    assert all(x['source_scope']=='opaque:allocation:a' and x['source_revision']=='a'*64 and x['units']=='USD' and x['source_as_of']=='2026-09-22' for x in result)

@pytest.mark.parametrize('kwargs',[{'source_scope':' '},{'source_scope':'x'*201},{'units':'EUR'},{'source_revision':'A'*64},{'source_revision':'a'*63}])
def test_explicit_lineage_boundary_refuses(kwargs):
    with pytest.raises(BasisRefused): invoke(*inputs(),**kwargs)

@pytest.mark.parametrize('count',[1.5,-1,True])
def test_population_count_cannot_be_rounded_or_boolean(count):
    v,p=inputs(); v['total_count']=count
    with pytest.raises(BasisRefused): invoke(v,p)

def test_numeric_and_text_position_identity_collision_refuses():
    v,p=inputs(); p[1]['symbol_id']='11'
    with pytest.raises(BasisRefused): invoke(v,p)

def test_overflowed_wire_facts_refuse():
    v,p=inputs(); v.update(long_equity='1e310',short_equity='0',cash='0',equity='1e310'); p[0]['market_value']='1e310';p[1]['market_value']='0'
    with pytest.raises(BasisRefused): invoke(v,p)

def test_receipt_revision_must_be_a_hash_string_not_integer():
    with pytest.raises(BasisRefused): invoke(*inputs(),source_revision=int('1'*64))


```

### basis_432_exact_review.py

SHA-256: `d7c6effa779620582e0b43b0b927d8b5f8c687624d457f59985a99a53536dd39`.

```python
import collections,hashlib,io,json,sys
from pathlib import Path
import boto3,pandas as pd
ROOT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
OUT=Path(r'C:/Users/AndrewBerman/Desktop/ajb_workspace/.runtime/codex-seats/3.0.0_SA_CVO~M')
sys.path.insert(0,str(ROOT/'data/assets/scripts/gold/investor_reporting'))
from smartx_valuation import allocation_facts
E=json.loads((ROOT/'org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/BASIS_SOURCE_EVIDENCE.json').read_text())
client=boto3.client('s3',region_name='us-east-1')
frames={}; receipts=[]
refs=E['custody_census']['receipts']+[x for x in E['original_source_receipts'] if any('/'+name+'/' in x['key'] for name in ['fact_allocation_account_map','fact_allocation_positions','fact_allocation_valuation'])]
for ref in refs:
    response=client.get_object(Bucket=ref['bucket'],Key=ref['key'],VersionId=ref['version_id'])
    raw=response['Body'].read(ref['byte_length']+1)
    assert response['VersionId']==ref['version_id'] and len(raw)==ref['byte_length'] and hashlib.sha256(raw).hexdigest()==ref['sha256']
    name=ref['key'].split('/')[-3]
    frames[name]=pd.read_parquet(io.BytesIO(raw))
    receipts.append(ref)
print('Verified nine exact source versions.',flush=True)
val=frames['fact_allocation_valuation'];pos=frames['fact_allocation_positions'];mapping=frames['fact_allocation_account_map']
assert not val['owner_id'].duplicated().any()
groups={owner:frame.to_dict('records') for owner,frame in pos.groupby('owner_id',dropna=False)}
assert set(groups)<=set(val['owner_id'])
source_revision=hashlib.sha256(json.dumps([r for r in refs if any('/'+n+'/' in r['key'] for n in ['fact_allocation_positions','fact_allocation_valuation'])],sort_keys=True,separators=(',',':')).encode()).hexdigest()
count=0; totals=collections.defaultdict(float)
for row in val.to_dict('records'):
    facts=allocation_facts(row,groups.get(row['owner_id'],[]),source_scope='DIAGNOSTIC_ONLY_NON_SERVING',source_revision=source_revision,units='USD')
    for fact in facts: totals[fact['fact_kind']]+=fact['value']
    count+=1

def ids(frame,column):
    series=frame[column]
    assert series.notna().all()
    return set(series.astype(str).str.strip().str.zfill(10))
cv=frames['canonical_valuation'];cp=frames['canonical_positions'];da=frames['dim_account'];db=frames['dim_boundary']
custody=ids(cv,'account_id');overlay=ids(mapping,'account_number');historical=ids(da,'account_id')
boundary=ids(db[db['boundary_class']=='IN_CLIENT_BOOK'],'account_id')
assert len(cv)==len(custody) and custody==boundary
missing=da[~da['account_id'].astype(str).str.strip().str.zfill(10).isin(custody)]
summary={'source_versions_fetched_verified':len(refs),'live_listings':0,'writes':0,'helper_allocations_reconciled':count,'position_rows':len(pos),'negative_net':int((val.equity<0).sum()),'zero_net':int((val.equity==0).sum()),'empty_reported_positions':int((val.total_count==0).sum()),'helper_fact_totals':dict(totals),'custody_unique_roots':len(custody),'custody_matches_in_client_book':custody==boundary,'overlay_accounts':len(overlay),'custody_without_overlay':len(custody-overlay),'overlay_without_custody':len(overlay-custody),'historical_accounts':len(historical),'historical_without_current_custody':len(historical-custody),'open_historical_without_current_custody':int(missing.account_is_open.sum()),'custody_position_rows':len(cp),'custody_position_accounts':len(ids(cp,'account_id')),'custody_negative_roots':int((cv.net_mv_plus_cash<0).sum()),'custody_zero_roots':int((cv.net_mv_plus_cash==0).sum()),'custody_dates':sorted(cv.business_date.astype(str).unique().tolist()),'valuation_dates':sorted(val.as_of.astype(str).unique().tolist()),'position_dates':sorted(pos.as_of.astype(str).unique().tolist()),'source_economics_accepted':False}
expected=E['custody_overlay_gap']
assert summary['custody_without_overlay']==expected['custody_without_overlay']
assert summary['overlay_without_custody']==expected['overlay_absent_custody']
assert count==E['basis_controls']['valuation_rows'] and len(pos)==E['basis_controls']['position_rows']
assert all(abs(totals[k]-v)<0.0001 for k,v in E['basis_controls']['reconciled_allocation_facts'].items())
(OUT/'basis_432_exact_review.json').write_text(json.dumps({'summary':summary,'verified_receipts':receipts},indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2),flush=True)


```


## M-FACT-01 closure at f7344d6

Date: 2026-09-23 UTC. **M-FACT-01 CLOSED**, bounded helper revision-type guard.
Exact independently tested endpoint:
`f7344d6e9a3833c7952b8f473a773634baea9dee`.
The clean detached reviewer checkout was switched to this endpoint; candidate
and review test files were not edited. The only helper implementation delta
requires `source_revision` to be a string before the unchanged exact lowercase
64-hex regex, and removes coercion through `str()`. The added supplied regression
requires refusal of the numeric 64-digit case.

Supplied focused suite: **27 PASS in 0.19s**, exit 0.
Original independent driver: **12 PASS in 0.09s**, exit 0, including unchanged
`test_receipt_revision_must_be_a_hash_string_not_integer`. Its file hash matches
the original driver embedded above: `f445cfca3971b5a8ced6bf5ffed0afd82f8916346ab331649d7be579fe454741`.
This supersedes only the M-FACT-01 OPEN disposition above, which remains as the
historical failure record. No new source fetch was needed for this type-only
change; the nine-version source checks and limits above retain their exact scope.

The helper remains unwired into the invalid holdings root. The original economic
failures, cross-date custody/overlay mismatch, package/live proof and final-index
timeout/versioning limitations remain open. M-PART-01's separate bounded closure
is unchanged. COO~M also supplied preliminary X10 candidate `ffbffcac50` on
`3978b247b4`, explicitly promising a durable proof/handoff to follow; that mention
is not an independently reviewed integration verdict.
