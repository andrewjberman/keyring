# ETFS Status Brief -- for COO (wrap decisively in 2 days; then CVO /verify the pipeline)

**Author:** 3.0.0_SA_CVO | **Date:** 2026-06-25 | **Requested by:** Andrew-direct ("status of ETFS -- did we sort out assets/average-owned? needs done in 2 days; brief COO -> /allocation to wrap -> I /verify seams+molecules")
**Audit basis:** PRDs (ETFS_SETUP.md, ETFS_AVGCAP.md) + project JSONs + the 8 ETFS TOs + commits since 06-15 + SERVED ground-truth (opal-data-etfs).

## TL;DR
ETFS is ~75% done and the remaining ~25% is a **single coherent gap: the 49F leg + the cross-partner monthly rollup.** Two of three partners are fully live and CVO-certed; the 49F producer was never built because its assignee (0.5.0_AE_OpalETL) got preempted onto the MDPF P0 (now CLOSED, so 0.5.0 is freed). The 49F data is a manual monthly batch (06-09), so the gap is a **build + compute** task, NOT blocked on new data -- **2 days is achievable.**

## Definition of done (per PRD)
Per Opal ETF (DIVZ/IDVZ/PFDE/PFOE), per partner (**49F, Inflection, Cottonwood**), the **monthly AVERAGE ownership value** (AUM each partner placed in Opal's funds), built on per-partner DAILY ownership producers (ETFS_SETUP write-out model -> opal-data-etfs) feeding the monthly-average metric (ETFS_AVGCAP). DONE = all 3 partners have a daily producer AND a monthly average shipped.

## DONE (verified)
| Piece | State | Evidence |
|---|---|---|
| Infra: opal-data-etfs bucket, IAM, ETF-universe config, daily-artifact schema | COMPLETE | ETFS_NETAST closed; W1 IAM ledger closed |
| ETFS_SECIDX (securities index / the "assets" dimension) | COMPLETE | 3/3 TOs; 102 securities / 138 tickers / 97.1% coverage |
| ETFS_NETAST (ETF net-assets daily) | COMPLETE | closed 2026-05-22 |
| **Inflection** daily producer | COMPLETE | 41 slices served (05-15..06-24); W1 ledger closed |
| **Inflection** monthly average | COMPLETE | monthly/{2026-05 $24.29M, 2026-06 $76.21M}; **CVO-certed serve-GO** (AC#1/#2/#3) |
| **Cottonwood** daily producer (W3) | COMPLETE | 10 slices served (06-08..06-22); **CVO-certed VERIFIED/GO**; ledger closed |
| DS fact_asset (asset value time-series, the broader "assets" build) | BUILT 06-25 | 2060 assets @06-18, firm-MV $1.63B (parallel canonical) |

## OUTSTANDING -- the 2-day wrap (one coherent gap)
1. **ETFS_SETUP W2 -- 49F daily/monthly ETF-ownership producer.** NOT BUILT: `opal-data-etfs/daily/49financial/` = **0 slices**. The 49F silver/RPS substrate EXISTS (RPS partitions present -- the "B1 empty" note in the TO is now stale), so the converter prerequisite is largely met; the missing piece is the **producer** (read 49F RPS -> filter 4 ETFs -> sum market_value -> write daily/49financial/{date}.json per the W1 contract). Constraint: 49F Schwab is a **manual monthly batch** (latest 06-09, next ~early-July) -> the slice is monthly-granular; build+prove on the 06-09 batch now (do NOT overstate daily-ness). Assignee 0.5.0_AE_OpalETL (49F/Schwab role-fit) -- **was preempted by the MDPF P0, now freed.**
2. **ETFS_AVGCAP cross-partner monthly rollup.** monthly/{YYYY-MM}.json is currently **Inflection-only**. Need: the **Cottonwood** monthly average (daily slices exist; rollup was "dispatched" 06-25 a04e070d1 -- confirm it ships) + the **49F** monthly average (gated on the W2 producer landing -> May full + June-MTD from the 06-09 batch). The averaging engine (avgcap_monthly_average.py) is built + CVO-certed and is multi-partner by construction -- it just needs the 49F + Cottonwood daily series present, then a re-run.

## Status drift to correct (cheap, do at allocation)
- **W3 TO `<status>pending</status>` is STALE** -- W3 is DONE (deployed cot-pipeline-v0.4.4, CVO-certed, ledger closed). Flip -> complete.
- **ETFS_SETUP + ETFS_AVGCAP project JSONs say "PHASE 0 -- PRD AUTHORED"** -- stale; both are mid-build (W1/W3 + AVGCAP-W1 done). Update the phase narrative.
- ETFS_AVGCAP has only a W1 (Inflection) TO -- the Cottonwood + 49F average legs need TOs (or a single wrap-TO).

## Recommendation (for /allocation)
A **decisive wrap is ~1.5 lanes of work, 2 days realistic:**
- **0.5.0_AE_OpalETL** (now freed from MDPF; 49F/Schwab role-fit, already the W2 assignee) -> build the **49F producer (W2)** on the 06-09 batch + land daily/49financial slices. (DS consult on the daily-slice contract; CVO verify.)
- **0.4.0_DS_ClientPlatform** (owns avgcap_monthly_average.py) -> on the 49F + Cottonwood daily series, run the **AVGCAP rollup** so monthly/*.json carries all 3 partners (the engine's done; it's a re-run + the cottonwood-dispatch confirm).
- Cut the missing **AVGCAP Cottonwood + 49F TOs** (or one wrap-TO) + correct the 3 status-drifts.
This closes the macro: all-3-partners daily producers + all-3-partners monthly averages. The 49F monthly-batch cadence is the one honest caveat (49F refreshes ~early-July), but May + June-MTD are deliverable NOW from 06-09.

## Then: CVO /verify (post-wrap, Andrew-directed)
Once allocated + landed, I run the full verification -- **seams + molecules + the whole pipeline**: each partner producer (read-own-firm -> write-out, firm-sep no-cross-read), the daily-artifact contract (schema/source_as_of fidelity), the AVGCAP engine (the certed methodology) over the now-complete 3-partner series, the monthly rollups (per-partner / per-ETF / all-partner), and served parity. Surface-level (does it deliver) + project-level (closeout adequacy). That's the close-gate on the macro.
