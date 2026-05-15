# Session Log — DS~A — ADVI_INFLEC live-portal data-drift: investigation + fixes

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-15
**Trigger:** Andrew-flagged URGENT — Inflection live-portal data drift; co-investigation with DE 0.4.
**Projects/TOs:** ADVI_INFDRF.001 (INF_D_04 geo reconciliation, GO'd) + ADVI_INFDRF.003 (INF_C_02/C_03 append-gate fix, COO captured for the record).

---

## Summary

Three distinct defects surfaced behind one "the Inflection portal numbers are wrong" report:

1. **WA 685->744 / "Segment Analytics number changed"** — the 17:57Z full chain CORRECTED a defective 06:00 holdings build. 744 is right. Root cause = ADVI_INFDRF.002 (AE 0.6.1).
2. **$787K timeseries drift (the live "205M")** — `gold/timeseries/client_performance.parquet` froze at the defective 06:00 value because INF_C_02's append gate never recomputes the current day. FIXED — commit 2f580143f.
3. **Count slippage (state != sum-city, plotted != total, etc.)** — 4 pre-existing reconciliation defects in INF_D_04. A/B/C-geo/D FIXED — commits 7a1b57a2b + 9ad466d1d. C canonical-count designation held (CTO ruling, blocked on a dimension-freshness bug).

---

## Defect 1 — WA 685->744 (-> ADVI_INFDRF.002, AE)

S3 object-versions, `gold/canonical/holdings_2026-05-15.parquet`: 06:00 chain = 11,413 rows / 801 accts / mv $204,632,760; 17:57Z full chain = 29,552 rows / 865 accts / mv $203,845,242 (= canonical header total.aua exactly). The 06:00 holdings was defective-short; 744 (17:57Z) is CORRECT, 685 was the regression. INF_D_04 geo-emitter code unchanged since 2026-05-14.
Mechanism (AE 0.6.1 root-caused, supersedes my initial chain-mode read): the 06:00 cron runs `--chain full` and INF_B_00 DOES run — but `INF_B_00.canonical_holdings` reconciles against `bronze/orion-api/{date}/assets.csv`, which the legacy bronze runner does not write until ~12:54 UTC. The 06:00 gold chain runs ~6h before its bronze input exists -> pmv-only fallback -> short holdings. Fix = move the gold cron 06:00 -> 14:00 UTC (AE 0.6.1, ADVI_INFDRF.002).

## Defect 2 — $787K timeseries drift (FIXED — ADVI_INFDRF.003)

The 17:57Z full chain emitted firm AUA as two numbers: snapshot family (header_metrics / partner_analytics / geo donut) = $203,845,242.41 CORRECT; timeseries family (timeseries_overview.json, cumulative_chart.json current point) = $204,632,759.83 WRONG (+$787,517).

Root cause: both timeseries artifacts source the current AUA point from `gold/timeseries/client_performance.parquet`. Its 2026-05-15 row = $204,632,759.83; S3 has no version after 07:03Z — the 17:57Z full chain did not rewrite it. `INF_C_02.client_performance.py` "Pattern B append-only gate" filtered `dates = [d for d in dates if d > _existing_max_date]` (strictly greater). The 06:00 chain wrote max_date = 2026-05-15; the 17:57Z full-chain INF_C_02 found nothing strictly newer and SKIPPED (the 3-second telemetry entry vs INF_C_00's 427s). The current day was structurally write-once — no corrective rerun could fix it. INF_C_03 (account_performance) had the identical gate.

Fix (commit 2f580143f): `>= _existing_max_date` so the trailing date always recomputes; the existing append-concat `drop_duplicates(keep='last')` replaces the stale rows. Self-correcting regardless of chain mode. Committed, pushed origin/CLOUD, S3-deployed to opal-data-inf/code/gold — both INF_C_02 + INF_C_03 sha-verified MATCH.

## Defect 3 — INF_D_04 count reconciliation (ADVI_INFDRF.001)

Producer: `INF_D_04.client_portal_summary.py` — `_build_geo_view` + `_compute_histogram_block`. Code unchanged since 2026-05-14; pre-existing latent defects.

| Defect | Finding (account-level verified, 17:57Z artifact) | Fix |
|--------|---------------------------------------------------|-----|
| A | WA state account_count 744 != sum top-10 cities 515. NOT null-city (0 null-city accounts) — WA has 55 distinct city strings; the top-10 cap drops cities #11-55 (229 accounts). Also unnormalized city casing fragments cities. | Title-case+strip city before the groupby; emit an "Other Cities" city-grain remainder bucket -> state == sum(city) exactly. (7a1b57a2b) |
| B | Histogram $1K floor: firm 865 accounts -> 770 plotted, no excluded field. | `_compute_histogram_block` emits total_count/plotted_count/excluded_count; filter stays (Rule 17). (7a1b57a2b) |
| C | geo client_count 321 vs header 307: `_build_geo_view` did `household_id.fillna(account_id)` -> 14 phantom pseudo-households (accounts the stale household_dim failed to map). | Geo derivation: household_id off fresh accounts_v2, no account_id fallback; unmapped accounts stay NaN, not phantom. 321 -> 296 real households. (9ad466d1d) |
| D | radial_12m partial decomposition presented unlabeled (AUA sum short of total). | header emits `radial_12m_meta` {is_partial, classified_aua, total_aua, unclassified_aua}. (7a1b57a2b) |

**Defect C — the 14-household verification (CTO premise check):** the 321-307 delta = 14 accounts the geo view phantom-counted via `fillna(account_id)`. Mapped via fresh accounts_v2: 11 are new accounts of EXISTING households (already in 307 — confirm the original premise); 3 (households 1353/1366/1367, May-created) are GENUINELY NEW CLIENTS that `silver/accounts_dim/latest.parquet` is missing because that artifact is STALE (frozen 2026-04-29, 17 days). CTO ruling: "307 canonical" WITHDRAWN; geo derivation fix proceeds off accounts_v2 (done); canonical client_count designation BLOCKED on the dimension-freshness bug. `silver/api_dims/household/` is also frozen (04-28). Local repro of the C fix: geo distinct household 321 -> 296; 31 holdings accounts unmapped by accounts_v2 (kept NaN — candidate closed-account/inclusion-semantics signal, flagged for the post-freshness re-compare).

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `comp-pipescript io INF_C_02 / INF_C_03` | clean | confirmed client_performance.parquet consumers incl. INF_D_00d/D_04/D_00b/D_05a |
| `comp-pipescript io INF_D_04` | no COLUMN GAPS | edits add no new column reads |
| `ds-commit-gate.sh` (INF_C_02, INF_C_03, INF_D_04 x2) | PASS | py_compile + AST + ruff py39 all clean |
| `comp-pipescript deployed` | n/a for INF | BD-bucket scoped; INF deploys verified directly by sha vs committed ref |

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/INF_C_02.client_performance.py` | Append gate `>` -> `>=` (trailing-date recompute) — 2f580143f |
| `data/orion/scripts/gold/INF_C_03.account_performance.py` | Same append-gate fix — 2f580143f |
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | Defects A/B/D — 7a1b57a2b; Defect C geo-derivation — 9ad466d1d |

## Deploy Evidence

| Item | Result |
|------|--------|
| INF_C_02/C_03 commit | 2f580143f (author DS~A), pushed origin/CLOUD |
| INF_C_02/C_03 S3 | s3://opal-data-inf/code/gold/ — sha MATCH vs HEAD |
| INF_D_04 commits | 7a1b57a2b (A/B/D) + 9ad466d1d (C geo), pushed origin/CLOUD |
| INF_D_04 S3 | s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py — sha MATCH |
| Materialization | DONE — AE 0.7.0 `--from INF_C_02` rerun (SSM a0e77feb), complete 2026-05-15T20:56Z; 29 scripts |
| AC5 smoke-test | 7/7 PASS — `inf_infdrf_ac5_smoke.py` against artifacts generated 20:53-20:55Z |

## AC5 Smoke-Test Results (post-rerun, 7/7 PASS)

| Check | Result |
|-------|--------|
| Defect 2 — cumulative_chart geo.data[-1] sum | $203,845,242.41 EXACT (drift was $204,632,759.83) |
| Defect 2 — timeseries_overview aua.{m,q,a}.data[-1] | $203,845,242.41 all three; zero drift-value occurrences |
| Defect A — geo state account_count == sum(city) | all states reconcile; "Other Cities" bucket present |
| Defect B — histogram plotted + excluded == total | total=865, plotted=770, excluded=95 |
| Defect C — geo distribution.total.count de-inflated | 296 (was phantom-inflated 321) |
| Defect D — header.radial_12m_meta | present: is_partial=true, unclassified_aua=$2,246,329.81 |
| COO fold-in — dimension freshness | OUTCOME (b): silver/accounts_dim STILL 04-29, household STILL 04-28 — did NOT un-freeze; orphaned from chain, separate AE item |

## Next Steps

| Recipient | Item |
|-----------|------|
| **AE 0.7.0** | DONE — `--from INF_C_02` rerun complete 20:56Z; ADVI_INFDRF.002 also shipped (gold cron 06:00->14:00 UTC, inf-pipeline-v1.7.62). |
| **DS~A (self)** | DONE — AC5 smoke-test 7/7 PASS; RAVC2-close ADVI_INFDRF.001 + .003 sent to COO (CC CTO/DE/AE). |
| **COO 2.0.0** | Route the dimension-refresh-path freeze as a NEW item (ADVI_INFDRF.00x to AE): `silver/accounts_dim` + `silver/api_dims/household` have NO pull/build step in the chain — orphaned, frozen 04-29/04-28. Confirmed outcome (b) — not the append-gate. Defect C canonical client_count is blocked on this. |
| **CTO 1.0.0** | Defect C canonical client_count held for the post-freshness clean re-compare; will verify the accounts_v2-vs-accounts_dim inclusion-semantics (closed-account) hypothesis then. |
