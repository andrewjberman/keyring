# Session Log — ADVI_INFINC.006 Cron Chain-Validation
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-18
**Directed by:** 2.0.0_SA_COO (GO 20260518T135007Z) — verification, not a build TO

## Summary

DIRECTED verification of DS~D's ADVI_INFINC.006 (Pattern E TXN account-level
windowed incremental pull + weekly backstop), which closed 2026-05-15 with the
note that it "rides the 2026-05-16 14:00Z cron" for chain-validation.

VERDICT: **DEFECT.** The INFINC.006 migration has NEVER executed in any chain
run. Both cron fires ran stale code or died upstream. Root cause: a filename
collision in `orion-gold-dispatch.sh sync_scripts()`.

## Evidence Chain

### The two cron fires since INFINC.006 deploy (5c1ea192d, 2026-05-15 16:46Z)

- **2026-05-16 (Saturday)** — `chain_full_20260516_130141` (13:01Z aggregator-
  primary) FAILED at step 2 `INF_API_SILVER_REPS` (exit=1, the --run-date catalog
  bug). `INF_API_PULL_TXN` is step 8 — never reached. No `chain_full_20260516_14*`
  telemetry exists; the 14:00 fallback cron produced no TXN run.
- **2026-05-17 (Sunday)** — `chain_full_20260517_140109` (14:01Z cron) COMPLETE,
  all 56 steps ok. `INF_API_PULL_TXN` ran 432s, wrote `bronze/transactions/2026-05-17.parquet`.

### The 05-17 run executed PRE-INFINC.006 code

Chain log `gold/logs/chain_full_20260517_140029.log` lines 291-325, the
`INF_API_PULL_TXN` section:
- `[14:01:22Z] pull_date=2026-05-17 cycle_id=... upload=True` — **no `mode=` field.**
  INFINC.006 code (lines 360-365) ALWAYS prints `mode=FULL-PULL/INCREMENTAL (...)`.
- `Loading client_ids from household_rep_mapping` / `household_rep_mapping: 312
  client_ids` / `Pulling 862 accounts across 312 clients` — INFINC.006 code loads
  account_ids from `accounts_v2` and prints no client grouping.
- `=== pull_inflection_transactions_rest.py COMPLETE ===` — INFINC.006 prints
  `=== ... FETCH COMPLETE ===`.

These log strings match commit `5c1ea192d~1` (= `f667b5d73`) verbatim
(`git show 5c1ea192d~1` lines 156/165/339). The 05-17 chain ran the
**pre-INFINC.006 version**.

### Root cause — `sync_scripts()` flat-dir filename collision

`data/orion/scripts/gold/orion-gold-dispatch.sh` lines 283-304: `sync_scripts()`
bulk-downloads four S3 prefixes into ONE flat `$SCRIPTS` dir keyed by basename:
```
prefixes = ['code/gold/', 'code/manual_api/', 'code/silver/', 'code/bronze/']
```
Processed in list order, last-write-wins. `pull_inflection_transactions_rest.py`
exists in THREE prefixes:

| S3 key | Size | LastModified | Content |
|--------|------|--------------|---------|
| code/gold/pull_inflection_transactions_rest.py | 15,792 | 2026-05-11 | pre-INFINC.006 |
| code/manual_api/pull_inflection_transactions_rest.py | 21,835 | 2026-05-15 | **INFINC.006 (5c1ea192d)** |
| code/bronze/pull_inflection_transactions_rest.py | 15,792 | 2026-04-30 | pre-INFINC.006 |

`code/bronze/` is LAST in the prefix list -> its stale 04-30 copy overwrites the
INFINC.006 `code/manual_api/` copy in the runner's flat dir. The chain ALWAYS
runs the old version. DS~D deployed INFINC.006 to `code/manual_api/` per the TO
Phase 4 spec — a structurally correct deploy, silently clobbered by the sync.

### Blast radius — systemic, not INFINC.006-only

Every script present in 2+ `code/` prefixes is subject to the collision. S3 scan:

| Script | Runner uses (bronze/silver wins) | Stale risk |
|--------|----------------------------------|-----------|
| pull_inflection_transactions_rest.py | code/bronze/ 15,792b 04-30 | **YES — INFINC.006 clobbered** |
| pull_inflection_assets_v2.py | code/bronze/ 17,530b 04-30 (vs manual_api 11,701b 04-29) | LIKELY — copies differ |
| pull_inflection_positions_daily.py | code/bronze/ 19,547b 04-30 (vs manual_api 16,376b) | LIKELY — copies differ |
| pull_inflection_performance_rest.py | code/bronze/ 12,962b | NO — all 3 copies byte-identical |
| pull_inflection_performance_dim.py | code/manual_api/ 13,965b 05-08 | NO — newest copy wins |
| pull_inflection_new_portfolio.py | code/gold/ = manual_api, identical | NO |
| _orion_api_silver_lib.py / build_assets_dim.py / __init__.py | silver/gold | benign |

## Impact Assessment

**No data regression.** The old code is a daily full per-account inception-to-date
pull — correctness-SAFE (every transaction re-pulled every day; no incremental
window gap, no backdated-correction exposure). It is exactly the "safe but slow"
baseline INFINC.006 set out to optimize. silver/transactions/2026-05-17.parquet =
1,300,879 rows / 48 cols, Custom-Report enrichment 88.33% — coherent, no
regression vs the TXNAMG.003 amalgamated writer.

**What is lost:** the INFINC.006 optimization is dead. AC5 (~7min/day -> <1min)
not realized — the 05-17 run still spent 432s. The incremental 7-day-window +
Sunday-backstop design is not in force (the chain runs full-pull every day,
which is why it stays correct).

## Recommended Fix (for COO's fix TO)

Two layers:
1. **Immediate unblock** — collapse the duplicates so one canonical copy exists.
   Either (a) delete the stale `code/gold/` + `code/bronze/` copies of
   `pull_inflection_transactions_rest.py` (S3 deletion — needs human OK per
   CLAUDE.md autonomy rules), or (b) re-deploy the INFINC.006 copy over
   `code/bronze/` + `code/gold/` so the winning copy is the correct one
   (no deletion; hack but immediate).
2. **Structural** — fix `sync_scripts()` in `orion-gold-dispatch.sh`: define an
   explicit prefix precedence and skip lower-priority overwrites, OR fail-loud on
   any basename collision, OR namespace the dest per prefix. Reordering the list
   alone is fragile. `orion-gold-dispatch.sh` is my lane (ADVI_INFLEC.W4.11) —
   route the fix TO to me.

Also scope into the fix: re-validate `pull_inflection_assets_v2.py` and
`pull_inflection_positions_daily.py` (bronze copy wins, differs from manual_api).

## Compiler Tools

- comp-pipescript deployed — N/A for this path: the catalog references the
  script by bare basename; the deployed-check tracks `code/gold/` MATCH/STALE but
  cannot see the cross-prefix collision (it would report `code/gold/` STALE,
  missing that `code/bronze/` is what actually wins the sync). The collision is a
  sync-mechanism defect below comp-pipescript's resolution — noted as a comp-tool
  gap. Root cause established by S3 listing + chain-log signature diff vs git.

## RAVC

Findings reported to COO (RAVC2); CC CTO + DS~D (0.4.0_DS_ClientPlatform~D — their
migration is deployed but not live).

## Status

INFINC.006 chain-validation COMPLETE — verdict DEFECT. Root cause + blast radius
+ recommended fix delivered to COO. Awaiting COO's fix-TO decision.
