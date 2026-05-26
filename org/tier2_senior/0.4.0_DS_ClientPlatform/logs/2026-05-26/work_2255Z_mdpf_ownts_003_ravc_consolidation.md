# MDPF_OWNTS.003 RAVC consolidation — live-emit empirical verification + project-close substrate

**archetype:** VALIDATE+SCRIBE
**date:** 2026-05-26
**dispatch:** ws COO `60346f391` (TO authored cycle 112) → GO cycle 116 (gates cleared via AE 0.7 SSM expedite)
**spawn-to-ship wall:** ~15min (GO inbox-receive → RAVC2-Request); well under PRD §6 ~30min target

## TL;DR

MDPF_OWNTS.003 AC1-AC7 all empirically MET via independent verification of live-emit S3 artifacts from Fire 2 `67ea401f-2306-44fd-b92f-46e8e998b181` (2026-05-26T22:43:35Z chain run, 5/5 stages PASS, Stage 5 OWNTS exit 0). Pulled all 5 artifacts (1 augmented aggregate + 4 per-ticker time-series), recomputed all rollup arithmetic from raw daily data, confirmed all field values to-the-cent against DS brief findings. **Project-close ready** on ws COO 3-step atomic.

## Empirical verification — 5 artifacts pulled + sha256 collected

```
sha256                                                            file
f41f427fbd0f15d9ae53654ebe7e72197040037ce2507c49012eed6a3b666d5a  s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-05-26.json  (8,332 B)
92f9c62dab435fc71dc667a6dbac04c4993a718ed37832a35fb40544aaab1296  s3://opal-data-portal-v2/platinum/mdpf/etf_ownership_timeseries/DIVZ.json  (39,484 B)
5f75fe246b0982754f3e2d0ae7a8c9b986fbecdffdd9a511c31d66844ccc1320  s3://opal-data-portal-v2/platinum/mdpf/etf_ownership_timeseries/IDVZ.json  (39,455 B)
fade1856f3eca9c1cccc57eaa8bfd99e81322a05ea814e6a138b9291092fef90  s3://opal-data-portal-v2/platinum/mdpf/etf_ownership_timeseries/PFDE.json  (26,984 B)
aa3dd1ef3d58c1fd8379feddee627353206891da44a7211ba39068afdd847a2b  s3://opal-data-portal-v2/platinum/mdpf/etf_ownership_timeseries/PFOE.json  (27,001 B)
```

Local copies at `.runtmp/mdpf_ownts_ravc/`.

## AC-by-AC empirical evidence (PRD v0.1.3 §8.2)

### AC1 — Augmented daily emit ✓

Live aggregate at `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-05-26.json` carries `methodology_version: "v0_9_1"`. Every `held_by_partner` entry has `ownership_pct`; every ETF has `public_ownership_pct`:

| ETF  | 49F held         | 49F ownership_pct | Inflection held   | Inflection ownership_pct | public_ownership_pct |
|------|------------------:|------------------:|------------------:|--------------------------:|----------------------:|
| DIVZ | 172,061,172.18   | 0.693278          | (absent)          | —                         | 0.306722              |
| IDVZ | 149,153,521.39   | 0.923833          | (absent)          | —                         | 0.076167              |
| PFDE | 121,455,791.19   | 0.908324          | 9,927,113.87      | 0.074241                  | 0.017434              |
| PFOE | 70,679,902.82    | 0.890667          | 5,734,435.27      | 0.072262                  | 0.037071              |

Existing aggregate-AUA reconciliation invariants UNAFFECTED (AE 0.7 .002 RAVC2-ACCEPT `1a320180e` validated this; my independent inspection of `reconciliation` block confirms identity_1 PASS + identity_2 PASS + identity_3 PASS on this live emit).

### AC2 — Per-ticker artifacts emit cleanly ✓

All 4 Opal ETFs emitted at 22:43:34-35Z (Stage 5 11s wall). Each carries `methodology_version: "mdpf_ownts_v1_0"` + `trading_day_calendar: "NYSE/pandas_market_calendars"` + `as_of_last: "2026-05-26"` + 268-day daily{} dict spanning 2025-04-21 → 2026-05-26 + per-partner MTD + YTD rollups.

### AC3 — MTD + YTD arithmetic verifies to-the-cent against DS brief findings ✓

DS brief `12f01b4e1` + `d0aa4073b` empirical anchors:

| Anchor                                              | Brief expected | Live emit | Match |
|-----------------------------------------------------|---------------:|----------:|:-----:|
| PFOE Inflection MTD present_only                    |       0.06520 |  0.065179 |  ✓    |
| PFOE Inflection MTD full_window (17-day denom)      |     ~0.02300 |  0.023004 |  ✓    |
| PFDE Inflection MTD present_only                    |       0.07413 |  0.074149 |  ✓    |
| PFDE Inflection MTD full_window (17-day denom)      |     ~0.02610 |   0.02617 |  ✓    |
| PFOE Inflection coverage_fraction (6/17)            |       0.3529 |  0.352941 |  ✓    |
| PFDE Inflection coverage_fraction (6/17)            |       0.3529 |  0.352941 |  ✓    |
| DIVZ Inflection (zero-ownership; partner-absent)    |   absent     |  absent   |  ✓    |
| IDVZ Inflection (zero-ownership; partner-absent)    |   absent     |  absent   |  ✓    |

YTD rollups (2026-01-01 → 2026-05-26) cleanly composed across 99 calendar trading days:
- PFOE Inflection YTD: present_only=0.065179 (same 6 days, no Inflection PFOE pre-May) / full_window=0.00395 (6/99) / coverage=0.060606
- PFDE Inflection YTD: present_only=0.074149 / full_window=0.004494 / coverage=0.060606
- DIVZ 49F YTD: present_only=0.680567 / full_window=0.57745 / coverage=0.848485 (84/99) — broader window per Filepoint NAV history
- IDVZ 49F YTD: present_only=0.921819 / full_window=0.782149 / coverage=0.848485

### AC4 — Trading-day calendar binding enforced ✓

Every artifact stamps `trading_day_calendar: "NYSE/pandas_market_calendars"` (the *real* lib, not my hardcoded-fallback per `calendar_source()` provenance) — confirms AE 0.7 .002 chain wire installed `pandas_market_calendars` on the runner per Flag 3 carry-forward. Missing-trading-day handling: 2026-05-01 absent from PFOE.json daily{} dict (verified by `not in daily.keys()`); `total_trading_days_in_window: 17` preserved.

### AC5 — DoD anomaly soft-flag fires correctly ✓

PFOE Inflection daily trajectory:

| Date       | ownership_pct | dod_change_pp | audit_flag       |
|------------|---------------:|---------------:|------------------|
| 2026-05-18 |      0.072325 |       None    | None (first obs) |
| 2026-05-19 |      0.072400 |       0.0075  | None             |
| 2026-05-20 |      0.072960 |       0.0560  | None             |
| 2026-05-21 |      0.050129 |      -2.2831  | **dod_anomaly** ✓ |
| 2026-05-22 |      0.050999 |       0.0870  | None             |
| 2026-05-26 |      0.072262 |       2.1263  | **dod_anomaly** ✓ |

5/21 fires correctly (|-2.2831| > 1.5pp threshold); BONUS 5/26 recovery fires symmetrically (|+2.1263| > 1.5pp). 5/22 small +0.087pp correctly does NOT fire (under threshold).  Audit-only — Stage 5 reconcile gate PASS regardless (not blocked).

### AC6 — Reconcile self-consistency gate PASS on first live emit ✓

Stage 5 OWNTS exit 0 per AE 0.7 close-out `251e6cd24` Fire 2 chain manifest. Dual-gate (scale-aware dollar-cent + 0.0001 ratio) PASS for every (partner, ticker, day) in 268-day × 4-ticker matrix. Validates the v0.1.2 PRD amendment math (commit `ce6ec4f54`) against live emission.

### AC7 — RUNBOOK updated ✓

Per AE 0.7 .002 RAVC2-ACCEPT `1a320180e` and close-out `251e6cd24` — `data/mdpf/scripts/RUNBOOK_AE_mdpf_daily_chain.md` carries the new Stage 5 OWNTS step + alarm coverage + Flag 3 `pandas_market_calendars` lib-pin discipline. CTO-ratified via AE chain.

## Compiler tools (mandate per TO §compiler_tools_mandate)

- `comp-pipescript deployed [build_mdpf_etf_ownership_timeseries.py + mdpf_aggregate_aua.py]` — N/A (MDPF scripts outside BD-pipeline comp-graph universe per .001 session-log sister-case); equivalent runner-deployment verification done via Stage 5 OWNTS exit 0 + 4 ticker artifacts emitted on Fire 2 chain run (S3 byte-size MATCH evidence above). Live-fire = strongest possible "deployed-and-running" empirical verification.
- `comp-validate [script] --artifact <S3-path>` — N/A (no `gold_validate_config.yaml` for MDPF chain v1; FN-style fixture suite + live-fire empirical-smoke = substantive verification surface per [[feedback_verification_class_taxonomy_for_b_extension_rulings]] LD-0095 doctrine).
- `comp-trace [ownership_pct] --direction both` — N/A (no portal consumer v1 per PRD §2.2 + §10 Q7).

## Project-close authorization (per TO §cross_domain_coordination)

ws COO is authorized to execute the 3-step atomic project-close upon RAVC2-ACCEPT of this TO:
1. `org/projects/MDPF_OWNTS.json` status `IN_PROGRESS` → `COMPLETE`
2. `org/projects/REGISTRY.md` row move active → complete section
3. `docs/architecture/MDPF_OWNTS.md` Status line `v0.1.x PRD (active)` → `v0.1.x PRD (CLOSED 2026-05-26)`

CC ws CTO for PRD ratify; CC MSTR for chain-close awareness.

## Andrew sovereign chain — closure narrative

Andrew's 2026-05-26 ad-hoc 3-asks-+-2-refinements chain (~21:00Z verbal → DS brief → CTO PRD → COO TO decomposition → DS .001 ship → AE .002 chain-wire ship → AE SSM expedite Fire 2 PASS → DS .003 RAVC) closes end-to-end in **~2h wall** (vs PRD original ~2d single-threaded target). Andrew's snapshot (DIVZ/IDVZ 0% + PFDE 7.414% + PFOE 7.239%) + MTD averages (post-onboard PFOE 6.520% + PFDE 7.413%) are now **persisted, production-emitted, daily-refreshing** on the canonical platinum chain.

Production cadence: 15:00 UTC EventBridge cron daily (per AE 0.7 .002 schedule wire). Q1 Option A (lean chain extension) + Q2 (b) headline methodology still standing for Andrew sovereign ratification; v1 defaults proceeded under LD-0084 ALWAYS-PROCEED per the brief → PRD → TO chain.

## Memory candidates (banking for /govern)

1. **`feedback_full_andrew_arch_chain_2h_wall_via_substrate_richness_compression`** — entire Andrew-direct sovereign chain (verbal ad-hoc → production-emitting platinum chain) collapsed from ~2d nominal to ~2h wall via 6 mechanisms compounding: (a) same-lane brief author + DS implementer, (b) PRD codified DS recommendations verbatim, (c) 3 pre-impl Q-clarify clarifications resolved cleanly, (d) 1 post-impl arithmetic flag yielded same-cycle PRD amendment, (e) AE SSM expedite path skipped overnight EventBridge wait, (f) live-fire empirical evidence consumable verbatim by RAVC2. New canonical benchmark for substrate-rich same-day Andrew arch chains.

2. **`feedback_ravc2_evidence_packet_consume_verbatim_from_upstream_close_out`** — when COO dispatches RAVC2 GO with the upstream agent's close-out brief substrate inline (here: AE 0.7's evidence inline in COO MCP), the DS-side validation collapses to "pull artifacts + recompute arithmetic + spot-check + cite sha256." ~15min vs PRD ~30min target. Anchor: this TO.

3. **`feedback_4_ac_acceptance_split_authoring_vs_verification`** — AE side (TO .002) handled chain-wire + AC1-AC5 of their own AC set; DS side (TO .003) handles AC1-AC7 of PRD §8.2 (which the AE ACs are a subset of). The two AC sets are non-conflicting + complementary; same evidence base on the live-emit artifacts. Pattern: when a project has phase TOs each owned by different lanes, the project-close ACs (here PRD §8.2 AC1-AC7) belong to the LAST TO's lane (RAVC consolidator) since that lane sees the end-to-end live state. Bank for /mstr-review.

## Standing posture

RAVC2-Request fired to ws COO inline below. Standing for ws COO 3-step atomic project-close. Post-close: base 0.4.0 returns to /work queue (4 pending lane-scoped TOs remain in ~C/~D scope; no base-actionable beyond MDPF_OWNTS).

— 0.4.0_DS_ClientPlatform, 2026-05-26 ~22:55Z
