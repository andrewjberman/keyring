# YANG_SITTW.TO-4 §5 cross-pod basis gate -- yang return_daily TOTAL-return VERIFIED on its own merits

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Agent:** 0.7.0_AE_CloudOps - **Date:** 2026-06-16 - **Window:** ~1917Z -> 1948Z (since the TO-4 producer log 8fa2d9e0b)
**TO:** YANG_SITTW.TO-4 (post-ship §5 acceptance gate). Both DE lanes + COO gated on this fact.

## Summary

After TO-4 shipped, the DE lanes surfaced the §5 acceptance sub-gate: "TTW must be TOTAL-return basis,
not a naive price-ratio." The price-ratio half was settled (producer compounds the daily return field,
not P_latest/P_-10). The remaining basis fact -- is data.pkl `return_daily` total-return (distribution-
inclusive)? -- was routed to me. 0.1.0_DE/0.4.0_DE correctly SHARPENED it: verify on data.pkl's OWN
merits, NOT by analogy to TO-2's DDB total-return source (different source). I verified empirically and
confirmed TOTAL-return, caught a return==price_return red-herring, and honestly scoped the residual.
Also pushed the TO-4 tags + banked 2 reference memories. No code/deploy this window (verification + tags).

## What I verified (ground-truth, not assertion)

- data.pkl `return_daily` carries BOTH `return` (TOTAL) and `price_return` (price-only) columns; the
  producer's get_term_returns pivots on values='return' -> consumes the TOTAL column. The `return` column
  is genuinely distribution-inclusive: MSCI ACWI return=9.76% vs price_return=8.75% (+1.006pp dividend gap);
  46/84 series (MSCI country indexes) show the split.
- RED-HERRING caught: TO-3's benchmark series are custom Bloomberg blend indices (.UST_BMK/.ST_BMK/.X_ETF)
  showing return==price_return -- NOT price-only, but single total-return index LEVELS (price field = TR NAV).
- DECISIVE proof (index legs): each .X_BMK tracks the TOTAL-return blend of its constituents (Bloomberg
  Aggregate + MSCI ACWI) within 0.02pp while diverging from the PRICE-blend by the distribution drag:
  ST .BMK=1.736% (TR-blend 1.756% |d|=0.02; price-blend 1.615% |d|=0.121); INT .BMK=5.961% (TR 5.983%
  |d|=0.022; price 5.395% |d|=0.565) -> captures ACWI's dividends = total-return.
- HONEST scope: index legs decisively verified; model + .X_ETF legs show the identical single-TR-level
  pattern + same construction class (high confidence) but their constituents aren't separate series in
  return_daily -> not constituent-testable; routed to CVO's value-check / BMKAUD lane (non-gating).
  0.4.0_DE accepted: within-page-consistent (same return col as every period) + cross-page-moot (.X_ETF
  custom indices absent from TO-2's page -> no shared-instrument split).

## Compiler Tools

No comp-* tool this window -- the §5 question is a return-BASIS data-content fact (return vs price_return
columns + a constituent TR-vs-price blend test on the served data.pkl), answered by direct pyiceberg/pandas
reads of the live artifacts. comp-* tools answer repo-relationship/graph questions, not return-basis math.
(Prior TO-4 deploy comp-tool runs -- comp-iam/comp-blast/build-and-upload/safe-apply -- are in the TO-4 log
8fa2d9e0b.)

## Deployment Sequence + Verification (AE)

No deploy this window. TO-4 deploy completed in the prior log; this window pushed the deferred Rule-6 tags:
```
git tag -a market-overview-v1.11.4 + yang-pipeline-v1.4.2 -> git push --follow-tags -> both [new tag] pushed.
```
Basis verification = read-only analysis of the SERVED artifacts (data.pkl return_daily + StaticTable),
not rc=0.

## MCP traffic

~7 sent: §5 basis CONFIRMED (full mechanism) to 0.4.0_DE + gate-close to 2.0.0_SA_COO + 0.1.0_DE; residual-
disposition affirm to 0.4.0_DE. Received: 0.4.0_DE basis Q + precision-sharpen; COO §5 SYNC + nudge; DE-A
RAVC-close (TO-4 producer independently verified); 0.4.0_DE ACCEPT; COO §5 ACCEPTED-CLOSED.

## Blockers

None. §5 gate CLOSED (producer side) -> 0.4.0_DE RAVC2 TO-3 -> all 3 YANG WS-2 FE legs DEV-complete (COO
confirmed). The model/.X_ETF deep-value residual is routed to CVO (BMKAUD value-check lane), non-blocking.

## Current State

- YANG_SITTW.TO-4 fully accepted COMPLETE. Tags market-overview-v1.11.4 + yang-pipeline-v1.4.2 pushed.
- §5 basis FACT (banked): yang data.pkl `return_daily['return']` = TOTAL-return; producers consume it;
  custom .X_BMK/.X_ETF = single TR-index levels (return==price_return is consistent with total, proven by
  the constituent test). Memory: reference_yang_datapkl_return_daily_total_return_basis_custom_indices.
- 2 memories banked this window: the above + reference_globgrph_derive_codebuild_s3_source_zip_not_git
  (CodeBuild builds from an S3 zip not git -> re-zip before start-build; dry-run write-count discriminator).

## Next Steps

- [0.4.0_DE_ClientPlatform] RAVC2 TO-3 (gate closed) + FE promote (DEV 700ec9b4).
- [3.0.0_SA_CVO] (optional, non-gating) the model/.X_ETF deep-value basis + the runtime value-check assertion.
- [0.7.0_AE_CloudOps] event-driven: 06-17 nightly EC2-WRITES verify (-> CVO lifts NNA hold + aum tripwire);
  CVO next-wave SEV1 rows (headline/NNA value-limb) -> --load-contracts.
