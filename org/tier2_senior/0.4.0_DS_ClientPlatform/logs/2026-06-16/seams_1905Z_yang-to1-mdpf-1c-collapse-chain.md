# SEAM: build_aggregate_aua_timeseries.py -> served json/mdpf -> ModelPortfolios.tsx (YANG_SITTW.TO-1 chain) (scale: MACRO)
**archetype:** VALIDATE
**secondary_archetypes:** TRACE

Independent /seams pass on this session's YANG_SITTW.TO-1 work (Andrew-directed). Decomposed the macro chain into 3 constituent seams; grounded every axis against LIVE/DEPLOYED/SERVED artifacts (re-pulled, not session memory).

## Seam definition
- **S1 producer->served:** `build_aggregate_aua_timeseries.py` (the 1c/SMA fold, deployed) -> served `json/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries.json` (opal-data-portal-v2).
- **S2 runner-code->nightly (durability):** `s3://opal-data-mdpf/code/scripts/backfill/build_aggregate_aua_timeseries.py` -> daily-chain Stage-4 (RUNBOOK_AE_mdpf_daily_chain).
- **S3 served->FE:** served slices -> `ModelPortfolios.tsx` via `getMdpfAggregateAUATimeSeriesByFirm` + leg-b SI extension (portal DEV a447712b).
- **Expected contract:** sma_aua collapsed into non_model_aua (1b'=Schwab_total-1a); total + combined band never-widen; FE consumes value-preservingly + extends Global to 2024-11-01 with estimate-tail demarcation.

## Axis verdicts

### S1 producer->served
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | Live served global (ETag 4139302361, mtime 18:37:13Z): top keys lack `sma_aua` data field; as_of_first=2024-11-01, n_dates=413. The fold landed on the served object. |
| DECLARATIVE | PASS | data_contract.xml `<mdpf_global_timeseries>` + served `meta` both state the collapse; match the served shape. |
| SEMANTIC | PASS | non_model_aua first(2024-11-01)=$570.6M = old nm $550.9M + old sma $19.67M (fold exact); never-widen $0 verified all 413d x3 slices (leg-a Phase-3, COO-independently-confirmed). |

### S2 runner-code->nightly (durability)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | Deployed runner code at the backfill code-prefix: `_fold_sma_into_nonmodel` count=3 AND byte-identical to committed HEAD (diff empty). The chain's Stage-4 code IS my collapse. |
| DECLARATIVE | PASS | RUNBOOK_AE_mdpf_daily_chain Stage-4 = `build_aggregate_aua_timeseries.py --upload`; runner pulls from this code-prefix (recovery-procedure-evidenced). |
| SEMANTIC | UNVERIFIED (residual) | Code placed + correct, but the SCHEDULED nightly has NOT run since the upload -> the durable fold-emit is proven only on the 6/17 nightly (exercise-or-evidence: not yet exercised). Expected PASS; review on 6/17 artifacts. |

### S3 served->FE (leg b a447712b)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | sma_aua?: optional on all 3 portal-proxy types (matches absent field); SI extension `isGlobalSI`-gated to 2024-11-01; per-firm keeps rolling-1y. tsc clean (DE). |
| DECLARATIVE | PASS-with-NOTE | The per-firm fold-removal (L831/L893) is value-preserving (old `+sma_aua`=+0 since field absent; render identical). NOTE: the GLOBAL view's rendered Non-Model band is sourced from `non_model_assets.json` via `getNonModelAumForDate` (= total-model), NOT my `globalMdpfData.non_model_aua` (1b'); they differ by `cohort_2b_audit` (~$82M last). My collapse is invisible to Global rendering (correct) + value-preserving for per-firm. |
| SEMANTIC | PASS-with-FINDING | SI Global band IS populated to 2024-11-01 (non_model_assets.json = 438 entries from 2024-11-01; roll-forward returns 0 only pre-all-data, none). Stack (model bars + band) == opal_aggregate EXACTLY from 2026-01-15 on. **FINDING:** in the estimate-basis deep tail (< 2026-01-16) the stack OVERSHOOTS the true enterprise total -- $22.4M (~2.9%) at the 2024-11-01 floor, declining to $0 at 2026-01-15 -- because the non_model_assets band is uncalibrated estimate there and doesn't reconcile with my artifact's (total-model). MITIGATED by DE's estimate-basis demarcation (the region is shaded "estimated history, not calibrated"). |

## Knowledge-parity delta
- BELIEVED (FE comment L606-608): "model bars + Non-Model band total to opal_aggregate_aua." TRUE in the measured region (>=2026-01-15); FALSE in the estimate-basis deep tail the leg-b SI extension now renders (overshoot up to 2.9% at the floor). The leg-b demarcation footnote ("estimate-basis ... not yet calibrated") is the honest mitigation, but the stack-sums-to-total invariant is not universal across the new SI range. Recorded here; routed to COO+DE for an explicit accept-vs-refine call (not unilaterally changed -- non_model_assets.json is a separate producer + the deep tail is correctly demarcated).
- BELIEVED: "the never-widen gate protects the Global view's rendered band." Actually the Global view's band comes from non_model_assets.json (untouched by my change), so the Global RENDER was never at risk from the collapse -- the never-widen evidence correctly scoped to the served json/mdpf fields (which the per-firm views consume). Parity now on record.

## Verdict
- **S1 producer->served: SOUND** (all 3 PASS) -- my leg-a collapse is correct + deployed + never-widen.
- **S2 runner-code->nightly: SOUND-on-placement; SEMANTIC UNVERIFIED until the 6/17 nightly exercises it** (residual, expected PASS).
- **S3 served->FE: SOUND mechanically + value-preserving**, with a recorded SEMANTIC FINDING (deep-tail estimate-basis band overshoot, demarcation-mitigated) routed to COO+DE.
- **Chain (weakest-seam-binds): SOUND for the leg-a data contract; one open semantic decision (deep-tail Global band reconciliation in the estimate region) + one time-gated residual (6/17 nightly).** No BROKEN seam; the collapse connects correctly end to end.

## Residual / unknowns
- 6/17 nightly: confirm Stage-4 runs the new runner code + the auto-emitted served artifact stays sma_aua-free (durability proof).
- Deep-tail Global band: COO/DE/Andrew decision -- accept the demarcated ~<=2.9% estimate-region overshoot, or re-source the SI deep-tail band from globalMdpfData (opal_aggregate-model, sums exactly by construction).
- Visual render smoke (Global renders from 2024-11-01 + demarcation visible) -- deferred to DT-promote/Andrew.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| aws s3 cp/head-object (served global + non_model_assets + runner code) | yes | live re-ground: served sma_aua-free 2024-11-01..2026-06-16; runner==HEAD; nma 438 entries from 2024-11-01 |
| git -C portal show a447712b | yes | leg-b diff read: value-preserving fold removal + isGlobalSI extension + ReferenceArea demarcation @2026-01-16 |
| custom stack-vs-aggregate reconcile (python) | yes | sum==opal_aggregate from 2026-01-15; deep-tail overshoot $22.4M->$0 (the FINDING) |
| comp-* | no | seam is a multi-artifact reconcile + deployed-code diff; comp-pipescript io is mdpf-unsupported (leg-a GAP). Ground-truthed via direct S3/deployed-code/served reads per /seams discipline. |
