# ADVI_BDPLAT_RESTORE.TO-1: bd platinum publish leg -- B_00 re-point to the ADVI Schwab master 08335338 + D_02 NaT guards + A_01 root fix, deployed; backfill 07-24..08-04 done; 23:01Z schedule is the restore -- 0.4.0_DS_ClientPlatform

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE

**Date:** 2026-08-18
**Task Order:** ADVI_BDPLAT_RESTORE.TO-1 (P1 CLIENT-FACING; joint DS + 0.7.0_AE_CloudOps; issued 2.0.0_SA_COO @f6912f9f1c)
**Status:** IN PROGRESS -- DS script legs COMPLETE + DEPLOYED (f71e767d33); ad-hoc backfill COMPLETE; awaiting the 23:01Z scheduled chain_full (BP-4 as observed) + AE's BP-5/BP-6

---

## Objective

49 Financial advisors were served `opal-data-bd/platinum/firm/*` content as_of 2026-08-06 for 8 trading days. Two
independent stacked causes: M1 (D_02 merge_asof crash on 3 NaT `effective_date` rows -> PHASE_D3 halted -> the
platinum publisher D_04 never ran since 08-16) and M2 (B_00 reading the DORMANT legacy Schwab RPS home
`opal-data-bd/schwab/silver/rps/` whose last partition is date=20260723 -> "Schwab partitions loaded: 0, rc=0" daily
since ~07-24 -> gold/canonical/holdings frozen at 08-06). Fix both ON THE SCHEDULED PATH; no alarm/monitor.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which / comp-find | `comp-find --name B_00.canonical_holdings.py`; `--name D_02...`; `comp-find advisor_assignments_history data/black_diamond/scripts/gold` | PASS | located the bd tree (`data/black_diamond/scripts/gold/`, not `data/bd/`) and A_01 as the SCD writer (21 hits / 107 files) |
| comp-pipescript io | `io B_00.canonical_holdings --pipeline bd`; `io D_02.advisor_client_detail --pipeline bd` | PARTIAL | reads/writes + consumers correct (canonical_holdings -> B_02/B_03/D_04; ADVISOR_ASSIGNMENTS <- A_01) but the Schwab RPS PREFIX read (paginated list_objects_v2) is INVISIBLE to it -- the exact input of this TO |
| comp-pipescript deployed | `deployed {B_00,D_02,A_01} --pipeline bd` before + after | PASS | STALE x3 -> VERIFY OK x3 (safe-deploy); confirmed by an independent sha256 read of the S3 members |
| commit-gate | `.tools/commit-gate.sh <3 files>` | PASS | py_compile + ds-precommit + ruff clean x3 |
| safe-commit (risk-reflex) | `safe-commit.sh --author ... -F msg -- <3 files>` | PASS | risk-reflex CLEAN, 3 files / 1,817 danger nodes; commit f71e767d33 |
| safe-deploy | `safe-deploy.sh --author 0.4.0_DS_ClientPlatform <3 files>` | PASS | DEPLOYED x3, VERIFY OK x3, rc=0 |
| proof-of-spec-check | `proof-of-spec-check.py <instance> BP-1,...,BP-6` | PASS | VALID rc=0 after 3 iterations (phase enum, kind enum, artifact-coverage token rule) |

**What worked:** comp-find for locating the two-homes scripts; commit-gate/safe-commit/safe-deploy end to end; the proof
checker's artifact-coverage rule forced an honest declared exclusion (function-level vs end-to-end exercise).
**What failed:** `comp-pipescript io` does not list `SCHWAB_RPS_PREFIX` -- a paginated prefix read is invisible; the
all-trees `comp-pipescript deployed` sweep exceeded 300s (backgrounded; per-script form used instead).
**Gap found:** paginated-prefix reads in a gold script are not in the io manifest (routed by COO to CTO as a comp-tool
coverage gap, not chased here).

---

## Work Completed

### 1. Startup + mechanism verification at source (13:33-13:44Z)
- Registered (PID 30668), persistent inbox Monitor bsdsr33hz armed (TaskOutput running); serial file written;
  A.3 PATH 96 of 97 + EXERCISE ran; owned-paths hook wired; comp-to set to the TO.
- Read the TO + COO GO @f6912f9f1c; ACK sent 133419Z; mechanism read at source: B_00:73 prefix, `_read_s3` defaults
  to S3_BUCKET at both Schwab call sites, `list_schwab_dates` :357 slices `part[5:]` as YYYYMMDD; D_02 :233 + :296
  merge_asof on `effective_date`; A_01 :405-408 baseline branch reads a nonexistent `start_date`.
- Live shape: legacy home 634 partitions 2024-01-12..2026-07-23 (93,126 x 11, typed); live
  `opal-data-assets/schwab/08335338/silver/fact_rps/` 531 partitions 2024-07-08..2026-08-17 (94,637 x 63 on 07-23,
  ALL object dtype); 07-23 present in both = the overlap date.

### 2. Column map + tie-out (13:36-13:44Z) -- the two findings that changed the edit
- Legacy `quantity_settled` == live `quantity_settled_unsettled` EXACTLY (0 diffs / 93,097 shared keys); live
  `quantity_settled` differs on 591 rows (max 151,000). `market_value` == `market_value_settled_unsettled`,
  `quantity_{cash,margin,short}` == `*_settled`, `closing_price` exact, `ticker` == `ticker_symbol`.
- The legacy partition's `_source_file` = `schwab/08242234/bronze/rps/20260723/08242234.CRS20260723.RPS.zip`: the
  legacy home was fed from the MDPF master. Through B_00's own prepare path on 07-23: 08242234 fact_rps == legacy
  EXACTLY (83,878 agg rows, 0 diffs, identical sum); 08335338 ties exactly on all 83,878 legacy rows + adds 650 rows /
  17 mapped 49F BD accounts / 315,389 units. Masters share 5,993 of ~6,000 sub-accounts.
- Mechanism ACK with three additions sent 134424Z (COO), cc CTO 134437Z, MSTR 134449Z. RULED: COO 134509Z + CTO
  134513Z build to 08335338 (correct-master outranks content-identity; disclose the delta); MSTR 134541Z: quantify +
  classify the 17 BEFORE it lands, no hold.

### 3. Edits (13:45-13:53Z), commit f71e767d33, deploy 14:16Z
- **B_00**: `SCHWAB_RPS_BUCKET='opal-data-assets'`, `SCHWAB_RPS_PREFIX='schwab/08335338/silver/fact_rps/'`
  (full 8-digit), `SCHWAB_RPS_COLUMNS` map, `_read_s3(columns=)`, `_read_schwab_rps` (the one reader; coercion),
  `_parse_partition_date` (ISO + legacy via strptime, never a slice), denominator print on listing, two hard-fails
  (0 listed -> rc=2; listed-but-0-loaded -> rc=2), "Schwab partitions loaded: M (of K)" print.
- **D_02**: `_drop_null_scd_keys` at both merge_asof sites, count printed.
- **A_01**: baseline `effective_date` = `account_open_date` -> `first_transaction_date` -> NaT with WARN count.
- safe-deploy to `opal-data-bd/code/gold/`; independent sha256 MATCH x3 (31277c56e71db0b6 / 651dafbb1e65a3f1 /
  a6635d0c0cb25f0d, mtimes 14:16:06/09/12Z); COO re-hashed 142016Z. Push is integrator-only (LD-0367 gate fired
  correctly) -- MSTR moves f71e767d33 at the integration window.

### 4. Ad-hoc QA reads (13:49-14:32Z)
- B_00 `--date 2026-07-23 --dry-run`: "531 objects listed, 531 date partitions parsed, 0 unparseable"; "Schwab range
  2024-07-08 to 2026-08-17"; "Schwab partitions loaded: 1 (of 1)"; "Dates processed: 1".
- Delta quantification (delta_quant.py, worker path, one mapping/bridge for all legs): MASTER SWITCH +17,791,028.82 =
  +0.961% (07-23; 6,771 -> 6,778 accts, 7 net-new, 17 changed, all open + named advisors; per-account/per-advisor
  lists sent to MSTR 140642Z cc COO 140654Z); T-1 REFRESH 08-06 -> 08-14 = +132,550,278.91 = +7.35%; total
  1,803,550,848.72 -> 1,953,892,156.44 = +8.336%. Control residual vs the sealed 07-23 partition (+283 bd-only
  accounts / +$88.5M) attributed to the nightly cube rewrite after the 08-08 seal (silver allocations are WEEKLY, so
  the phantom filter is empty on weekdays in production too).
- D_02 guards on the LIVE parquet: WARN 3, merge completes; fee PIT with injected NaT: WARN 1. A_01: the 3 accounts
  -> effective_date 2026-08-11; negative control -> WARN 3 + NaT.
- Mutants: old slice on `date=2026-08-17` -> `'2026--0-8-'`; bogus prefix -> ERROR + SystemExit 2. Determinism: 07-23
  dry-run identical across two harnesses.

### 5. IAM + backfill (14:18-14:30Z)
- Deploy message 141842Z (COO) + AE GO 141854Z; AE applied @7b706eec4c 1419Z, BP-3 PASS 142154Z (note: the role
  already holds a separate 08242234 grant, so that is not a valid negative for THIS role -- AE substituted one).
- Started i-01003b035d2988dfb (stopped since 04:00Z), SSM AWS-RunShellScript with S3-staged code: first attempt
  3a7029aa failed at line 1 (`sh` rejects `set -o pipefail`; nothing ran); re-sent with `#!/bin/bash`
  = 66111816-7642-48f2-b27c-e13a70dc0797: `B_00 --upload --start-date 2026-07-24 --end-date 2026-08-04 --force`
  -> "loaded 8 (of 8)", "Forward-filled: 4 written, 0 skipped", "Dates processed: 12", "Sealed 12 new dates (total
  2,410)", rc=0; log uploaded `gold/logs/adhoc_B_00_backfill_0724_0804_20260818_142603.log`; runner self-halted
  (launcher-standard `sudo shutdown -h +2`; stopped 14:29Z). 12 canonical partitions rewritten 14:26Z with
  Schwab-reconciled content (07-24 MV 1,851,154,278.49); 08-05/06 left to the schedule's --force-recent-days 14.
- Reported 143007Z (COO ACK 143039Z).

### 6. Proof-of-spec instance
- `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_BDPLAT_RESTORE.TO-1_PROOF_OF_SPEC.json` -- BP-1 PASS,
  BP-2 PASS, BP-3 PASS (AE's 142154Z transcribed; AE to confirm), BP-4/5/6 UNCOMPUTABLE with status_reason (await the
  schedule); checker VALID rc=0.

---

## Decisions Made

- **Home = 08335338 fact_rps** (COO 134509Z, CTO 134513Z ruled; MSTR concurred): the ADVI master; the legacy 08242234
  read was the two-buckets substitution; delta disclosed as a CORRECTION.
- **Table = fact_rps** (the FACT table; the IAM grant + TO name it; dim_position is a projection).
- **A_01 fixed at source + D_02 guards retained** (COO accepted; CTO: the shape they would have asked for).
- **Never a full --force**: the live home starts 2024-07-08; 2024-01-12..07-07 exists only in the dormant home
  (COO wrote a RETAIN marker at the legacy prefix 141010Z; migrate-or-write-off is a DATED DS-lane item).
- **Backfill range-bounded 07-24..08-04**, run via SSM with S3-staged code, self-halt mirrors the launcher.

---

## Files Modified

see commit message: f71e767d33 (B_00, D_02, A_01). Plus this log + the proof-of-spec JSON (this commit).

---

## Blockers

None. Waiting (not blocked) on the 23:01Z scheduled run; AE fills BP-5/BP-6 after it.

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| (none -- the proof-of-spec instance + MCP reports are the deliverables) | | |

---

## Current State

- **Deployed and running-tonight bytes:** `s3://opal-data-bd/code/gold/{B_00.canonical_holdings,D_02.advisor_client_detail,A_01.advisor_assignments}.py` == commit f71e767d33 (sha256 MATCH x3). Commit is on local CLOUD; NOT pushed (integrator-only push; MSTR moves it).
- **IAM:** `monolith-schwab-08335338-silver-read` on `bd-exporter-ec2-role` applied @7b706eec4c 1419Z (AE), BP-3 PASS.
- **Data:** `gold/canonical/holdings/2026-07-24..2026-08-04` rewritten 14:26Z (Schwab-reconciled, QA-class run); newest partition still 2026-08-06 (legacy, MV 1,803,550,848.72) until tonight; `account_performance.parquet` still 225,216,334 B; `gold/dimensions/advisor_assignments_history.parquet` still carries 3 NaT until PHASE_A2 tonight.
- **Runner** i-01003b035d2988dfb: stopped (self-halted 14:29Z); bd-gold-trigger starts it 23:01Z as every night.
- **Proof:** `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_BDPLAT_RESTORE.TO-1_PROOF_OF_SPEC.json` VALID; BP-4/5/6 open.
- **Disclosed deltas** (with MSTR + Andrew): master switch +$17.79M / +0.961%; T-1 refresh +$132.6M / +7.35% (08-06 -> 08-14 basis); total +8.336%.
- **Scratch (not committed):** `.../scratchpad/{tie3,qty_col,delta_quant,exercise_d02_a01,exercise_a01,mutant_b00}.py`, `delta_quant.out`.

---

## Next Steps

1. [0.4.0_DS_ClientPlatform] ~23:30Z: read `s3://opal-data-bd/gold/logs/chain_full_20260818_2301*.log` -- PHASE_A2 "A_01 done (rc=0)"; PHASE_B1 B_00 "Schwab range ... to <T-1>", "Schwab partitions loaded: M (of K)" M>0, "Dates processed: N" N>0, sealed-through AS OBSERVED; PHASE_D3 "D_02 done (rc=0)" (+ any WARN NaT count); PHASE_D4 "D_04 done (rc=0)". Rewrite BP-4 with observed values (newest canonical partition; account_performance.parquet size). Report to COO cc CTO/MSTR/AE. If PHASE_B1 reads rc=2/AccessDenied -> grant-did-not-land, escalate immediately.
2. [0.7.0_AE_CloudOps] BP-5 (served header_metrics as_of + before/after through the scoped route, the two named deltas separately) + BP-6 (chain log PHASE_D4) -> send evidence to DS to write into the joint instance, or edit under override.
3. [0.0.0_AB_MSTR] integration window: push f71e767d33 (+ this log commit).
4. [0.4.0_DS_ClientPlatform] DATED 08-19, after bd platinum closes: MDPF_PROVENANCE.T-B @8c25748037 (do not interleave).
5. [0.4.0_DS_ClientPlatform, DATED, not tonight] the 2024-01-12..2024-07-07 legacy-only Schwab tail: migrate into the 08335338 silver home or Andrew writes it off (COO RETAIN marker at the legacy prefix).
