# Session log — 0.4.0_DS_ClientPlatform~A (2026-04-16)

**TO:** `ADVI_ROLLUP.T1d.ds-orphan-advisor-slug-classification.md` (self-authored per COO 2026-04-16T12:54Z GO)
**Session goal:** Classify the 20 orphan advisor slug prefixes surfaced during B4 sweep; choose path (a bug patch) vs (b doc-only) vs (c accept-as-is).

## TL;DR

Path (b) memo-only close. **2 stale-rename, 0 producer gap, 18 legitimate orphan.** Zero consumer impact. No D_02 code change.

Memo: `docs/analysis/2026-04-16_t1d_orphan_advisor_slug_classification.md`.

## Root cause (1 sentence)

`build_advisor_books` (D_02 L1047) scopes to latest-snap advisors (163); `build_advisor_timeseries` (L1503) scopes to full history (larger); stale-cleanup (L2745-2775) runs between them — so orphan `timeseries.json` gets re-created after cleanup deletes the prior book prefix. Working-as-designed for each function in isolation; the combined artifact surface is cosmetic bit-rot.

## Classification (see memo for full detail)

| Bucket | Count | Slugs |
|--------|-------|-------|
| (a) rename | 2 | `david_ferrell`→`david_farrell`; `olivia_shin`→`liv_shin` |
| (b) gap | 0 | — |
| (c) orphan | 18 | `49_solutions`, `49f_house`, `alex_barnes`, `chad_crabill`, `connor_stiscak`, `ellie_shank`, `griffin_rea`, `jacob_villarreal`, `joshua_studebaker`, `kyle_kevorkian`, `luke_blackmon`, `maxwell_meyers`, `meredith_lipps`, `michael_wuest`, `mike_defrees`, `quinn_davis`, `ryan_fidler`, `ryan_witte` |

Rename evidence (quantitative): `david_ferrell` last 2026-01-19 $356K vs `david_farrell` 2026-04-13 $111.77M; `olivia_shin` last 2026-01-19 $219K vs `liv_shin` 2026-04-13 $54.27M. Both orphans tail off on 2026-01-19 (suggests a BD source rename push on ~2026-01-20).

## Consumer impact

ZERO.
- `comp-platinum reverse gold/entities/advisors` → no components found in dataflow index.
- `platinum/firm/leaderboard.json`: 157 unique advisor IDs across QTD(152) + YTD(155) + MAX(155) windows — **0/20 orphan hits**.
- `comp-pipescript consumers D_02` → D_04 reads `client_detail.json` only (not advisor book/timeseries).
- Platinum `advisors/{orphan}/*`: mostly empty; `49f_house` has stale 2026-04-09 artifacts (pre-current run).

## Compiler Tools

| Phase | Tool | Command | Observed | Pass/Fail |
|-------|------|---------|----------|-----------|
| 1 | `comp-pipescript io` | `comp-pipescript io D_02` | READS include `advisor_book_key` + `advisor_timeseries_key` as FUNC refs (indexer ambiguity: lists as READ rather than WRITE — minor extractor gap, noting for future `comp-build` fix). WRITES (4): IMPLEMENTOR_LEADERBOARD, advisor_mix_timeseries_key, canonical_role_aua_key, client_detail_key. | PASS (extractor gap not blocking) |
| 1 | `comp-platinum reverse` | `comp-platinum reverse gold/entities/advisors` | SERVED VIA `/api/scoped/advisor-intelligence/entities/advisors` (CF→APIGateway-portal); **CONSUMED BY: no components found** | PASS (no live consumer for orphan prefixes) |
| 1 | `comp-pipescript consumers` | `comp-pipescript consumers D_02` | D_04 reads `client_detail_key` only | PASS |
| 1 | `aws s3 ls` orphan prefixes × 20 | per-slug prefix listing | All 20 have `timeseries.json` only, 2026-04-15 15:14 timestamps, no book/mix/composition | PASS |
| 1 | `aws s3 cp timeseries.json` × 20 + python analyze | first/last date, last_aua, name | Table populated in memo | PASS |
| 1 | token match orphan vs active slugs | python Jaccard-like on name tokens | 2 rename candidates surfaced (ferrell/farrell, shin/shin) | PASS |
| 1 | `aws s3 cp platinum/firm/leaderboard.json` + scan | token-match 20 orphan slugs vs 157 leaderboard IDs | 0 hits | PASS |
| 2 | classification reconciliation | 20 slugs bucketed (a)/(b)/(c) | 2 + 0 + 18 = 20 | PASS |

## Files Modified

| File | Change |
|------|--------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.T1d.ds-orphan-advisor-slug-classification.md` | NEW — self-authored TO, `<status>=complete`, `<validation_result>` cites memo + session log |
| `docs/analysis/2026-04-16_t1d_orphan_advisor_slug_classification.md` | NEW — classification memo, 20-row taxonomy table, producer RCA, consumer impact audit, optional future hygiene options |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-16/t1d_orphan_advisor_slug_classification.md` | NEW — this log |

## What I did NOT do

- Did NOT modify `D_02.advisor_client_detail.py` (path b: no producer code change).
- Did NOT push or upload to S3 (no script changes).
- Did NOT trigger a gold rerun (not required).
- Did NOT author a follow-up TO for the producer hygiene note (optional future work, not scoped).
- Did NOT claim austin_bost D02-T2 (~B's lane per `<issued_to>=~B`).

## MCP traffic (this slice)

| Time (Z) | Direction | Party | Subject |
|----------|-----------|-------|---------|
| 12:50 | OUT | 2.0.0_SA_COO | B4 SWEEP COMPLETE — 100% tgp coverage |
| 12:51 | IN  | 2.0.0_SA_COO | ACK B4 COMPLETE |
| 12:52 | OUT | 2.0.0_SA_COO | CLARIFY — austin_bost D02-T2 is ~B lane; requesting next |
| 12:54 | IN  | 2.0.0_SA_COO | GO — option (c) T1d advisor count gap reconciliation |
| 12:54 | (heartbeat) | — | starting T1d |
| (next) | OUT | 2.0.0_SA_COO | T1d COMPLETE — path (b) memo-only, 2+0+18 classification |

## Next

- MCP COMPLETE to 2.0.0_SA_COO with classification table + consumer-impact summary (this turn).
- Stand by for post-nightly (04:00 UTC, ~14 hrs out): B3 parent closeout re-validation + B1.fix2 triage.
- Producer hygiene note parked — flag available to ~B / ~D when next D_02 touch-up lands.
