# Custody basis and multipart independent review preparation

**archetype:** VALIDATE

Reviewer `3.0.0_SA_CVO~M`, 2026-09-22. Authority: completion `CONTRACT.md` and complete `IRPT-M-BASIS-01` ruling at `b8de4c3899`. This responds with exercised baseline evidence and concrete outstanding inputs, not an ACK-only reply or a remedy/whole-source PASS.

## Current state

The immutable reviewed baseline is `62139c3a1a9792b41e02a8b66b612ad4571c6ab8`, detached clean reviewer checkout `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`. Its bounded publication transport PASS `c462d8b4df` remains separate from source correctness. No candidate implementation was changed. Producer worktree currently contains changing staged/unstaged basis/source/multipart edits; they were not substituted for a frozen candidate.

Read complete ruling and canonical SmartX architecture section 7b at workspace `ec7ea9d951136b8adedb2ccf13c18c5f59f8cd1c`, `data/assets/docs/SMARTX_INGESTION_ARCHITECTURE.md`. Preserve gross AUM = longEquity + cash, vendor net equity and signed positions as distinct facts. The ownership root must use independently enumerated custody; neither a SmartX allocation total nor its canonical gross fact proves that custody population.

The producer's current `SOURCE_INPUT_EVIDENCE.md` and exact `.runtime/m-holdings-source-probe.json` in `ajb_irpt_m` were read as uncommitted diagnostic evidence. The 23:15:32Z probe reports all three firms REFUSED: 49F reconciliation; COT/INF canonical publication vs supplied firm-home mismatch. This is attributed evidence, not an independent replay or accepted source lineage. The ruling's 5,917-account/127,925-node/7,479-partition/~98.45 MB diagnostic is also attributed; the exact original replay and frozen source receipts were requested from COO~M at 23:36:43Z.

## Independently exercised baseline

Unchanged supplied test `test_holdings_snapshot.py::test_8_smartx_positions_never_summed_into_the_account_value` was rerun: **1 passed in 3.16s**. Its actual assertion expects equity1000 + cash50 =1050. That passing test encodes the prohibited basis; it cannot certify the new ruling. Preserve it as historical evidence and distinguish any deliberate corrected contract assertion from an unchanged regression rerun.

The embedded diagnostic runs the actual `build_49f` at baseline with seven synthetic input controls. It patches source reads only, creates no network/storage operation, and does not claim independent custody is available.

| Case | Named gross / supported net | Actual baseline account value | Observation |
|---|---|---|---|
| long100, cash10, equity110 | 110 / 110 | 120 | Cash counted again |
| long100, short-20, cash10, equity90 | 110 / 90 | 100 | Neither declared gross nor net |
| long0, short-20, cash10, equity-10 | 10 / -10 | 0 | Negative net hidden by extra cash |
| explicit all-zero | 0 / 0 | 0 | Valid zero preserved |
| missing cash | unresolved / unresolved | REFUSED | Explicit missing valuation refusal works |
| missing position value with zero valuation | 0 / unresolved | 0, SECURITY=0 | Missing position becomes an observed zero in builder output |
| identical duplicate allocation | 110 / 110 | 120, one root | Duplicate collapse works; basis remains wrong |

These are builder-boundary observations, not proof that erroneous data was published or served. Later reconciliation may refuse; it does not make the builder's invented zero a valid source fact. All four actual source read families in this diagnostic are SmartX allocation map, roster, positions and valuation. An informational directory lookup does not supply independent custody values. The remedy must not merely replace the account root with a different SmartX basis.

## Required next review evidence

COO~M owns implementation and must supply an exact candidate or frozen patch hash, the unchanged original failing replay, protected exact-version input receipts and the complete per-account/per-parent findings. No user approval round is requested. The existing legacy-read commit refusal remains in force pending MSTR's sanctioned tooling mechanism; no bypass or source-literal reshaping is permitted.

The independent remedy review will discriminate:

1. **Custody and lineage:** complete independently enumerated account/position census, exact versions/hashes/dates/units and mappings; accounts absent from overlay remain visible; missing/incompatible source facts remain explicit. Whole-book totals alone are insufficient.
2. **Basis and partitions:** original failures unchanged; named canonical gross and supported net facts; signed shorts, cash exactly once, zero/negative roots, missing values, duplicate allocations and every parent partition. No cash plug, rescaling, residual assignment or provider-return change.
3. **Source cutoffs:** historical cutoff and immutable receipt binding; exact unchanged authorized legacy file/read/purpose scope; no bucket/prefix/population widening.
4. **Multipart:** declared schema plus concrete byte/count/request limits, complete part inventory pinned by accepted revision/version/hash, missing/corrupt/mixed parts and interrupted publication, all selected pages on one revision, selected-only reads, current-access checks and bounded continuation or refusal for oversized sets. No silent truncation, partial acceptance or cap inflation.
5. **Consumer composition:** P loader/manifest package and IAM correspondence; Y custody/normalization basis agreement. Existing final-index timeout ambiguity and versioning-suspension limitations remain until an exact fix is tested. No new storage family, live write, deployment or B/F-cycle authorization.

**Current disposition:** baseline basis/missing-position defects exercised; remedy, unchanged full-source replay and multipart acceptance NOT_EVALUATED pending exact candidate/input handoff. No broad product grade. Return this exact evidence to COO~M/CTO while implementation proceeds.

Compiler record: contextual bare comp-read inspected exact files after comp-which. One overbroad comp-which fallback search reached its 90-second budget without a result; it was not treated as absence. Routed bare comp-find scoped to docs found zero of1,354files, then data found the architecture file among1,167files. UTF-8 stdout correction was needed to print section7b completely. No tooling change was made.

## Reproducible baseline diagnostic

Run `python <saved-script>` with ROOT pointing to the exact baseline checkout above. Script SHA256 `454172ED500E5953CC9878A3E30F56564B6F923C226BBA770922B43B13CCD7F4`. Local output `.runtime/codex-seats/3.0.0_SA_CVO~M/basis_621_baseline.json`. The script returns measurements; exit0 is diagnostic completion, not acceptance PASS.

```python
"""Read-only synthetic diagnostic at the immutable pre-remedy basis baseline."""
import json
import sys
from pathlib import Path
from unittest.mock import patch
import pandas as pd

ROOT=Path('C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review')
sys.path.insert(0,str(ROOT/'data/assets/scripts/gold/investor_reporting'))
import holdings_snapshot as H

def exercise(name, long, short, cash, equity, positions, duplicate=False):
    date='2026-09-21'
    prefix='smartx/platform/silver/'
    mapping={'model_id':'model-test','allocation_id':'allocation-test','account_number':'12345678'}
    frames={
      'fact_allocation_account_map':pd.DataFrame([mapping]*(2 if duplicate else 1)),
      'fact_model_allocation_roster':pd.DataFrame([{'allocation_id':'allocation-test','status':'ACTIVE'}]),
      'fact_allocation_valuation':pd.DataFrame([{'owner_id':'allocation-test','longEquity':long,
        'shortEquity':short,'cash':cash,'equity':equity}]),
      'fact_allocation_positions':pd.DataFrame([{'owner_id':'allocation-test','market_value':v,
        'ticker':'TEST'+str(i),'symbol_id':str(i)} for i,v in enumerate(positions)]),
    }
    reads=[]
    def read(s3,bucket,key):
        reads.append(key)
        family=key[len(prefix):].split('/')[0]
        return frames[family].copy(deep=True)
    result={'case':name,'input':{'long_equity':long,'short_equity':short,'cash':cash,'equity':equity,
      'positions':positions},'expected_named_gross':None if cash is None else long+cash,
      'expected_named_net':None if cash is None or any(v is None for v in positions) else sum(positions)+cash}
    with patch.object(H,'_read_parquet',read), patch.object(H,'_latest_date_partition',return_value=date), \
         patch.object(H,'_directory_account_ids',return_value=None):
        try:
            nodes,extra=H.build_49f(object(),date)
            result.update(status='RETURNED',account_values=[n['amount']['value'] for n in nodes if n['node_kind']=='ACCOUNT'],
                security_values=[n['amount']['value'] for n in nodes if n['node_kind']=='SECURITY'],
                model_values=[n['amount']['value'] for n in nodes if n['node_kind']=='MODEL_LEAF'],
                manifest_total=extra['manifest']['total_market_value'])
        except Exception as exc:
            result.update(status='REFUSED',error_type=type(exc).__name__,reason=str(exc))
    result['read_families']=[s[len(prefix):].split('/')[0] for s in reads]
    return result

cases=[
 exercise('long_and_cash',100,0,10,110,[100]),
 exercise('signed_short_and_cash',100,-20,10,90,[100,-20]),
 exercise('negative_net',0,-20,10,-10,[-20]),
 exercise('zero_control',0,0,0,0,[0]),
 exercise('missing_cash',100,0,None,100,[100]),
 exercise('missing_position_at_zero',0,0,0,0,[None]),
 exercise('identical_duplicate_allocation',100,0,10,110,[100],duplicate=True),
]
print(json.dumps({'candidate':'62139c3a1a9792b41e02a8b66b612ad4571c6ab8',
    'ruling':'b8de4c3899','kind':'synthetic baseline diagnostic, not source-backed acceptance',
    'cases':cases},indent=2,allow_nan=False))

```
