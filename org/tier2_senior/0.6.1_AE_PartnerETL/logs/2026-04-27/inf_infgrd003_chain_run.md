# Session Log — ADVI_INFLEC INFGRD.003 Full Silver Rebuild + Gold Chain Run

**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-04-27
**Session period:** ~20:30–22:30 ET
**Triggered by:** DS~A RAVC2 — INFGRD.002 commit 7ecc140a (silver rep_id allowlist + D_04 NMEC lifecycle windowing)

---

## Summary

Executed INFGRD.003: full silver rebuild from DS~A commit 7ecc140a, followed by full 28-script gold
chain on i-0ed5afded2ebd4ed4. Chain completed exit 0 at 22:24:46Z. CloudFront invalidated.
Post-run artifact verification found 3 open flags — all sent to DS~A + COO via RAVC.
Instance stopped. AE idle-complete pending DS~A investigation.

---

## DS~A Commit 7ecc140a — Changes Deployed

| Script | Fix Class | Change |
|---|---|---|
| `convert_orion_to_silver.py` | INFGRD.002 | `_apply_scopefix()` rewrote with `INFLECTION_REP_IDS = {3, 11, 12}` allowlist; removes Keil contamination (rep_ids 1,4,5,9,13,14,15,18); adds Guards A/B/C diagnostic output; adds `advisor_firm` column to TRN/AUM/accounts_dim writes |
| `D_04.client_portal_summary.py` | INFGRD.002 | Added `_compute_hh_lifecycle()` (nmnc/nmec/existing windowed classification, BD D_01 pattern); `_build_radial_12m` NMEC no longer hardcoded 0; `_build_aua_view` up to 3 lifecycle segments in donut |

S3 uploads (DS~A uploaded per INFGRD.002):
- `s3://opal-data-inf/code/silver/convert_orion_to_silver.py` — ETag `8135ada3`, 30,081B, 20:34:56Z
- `s3://opal-data-inf/code/gold/D_04.client_portal_summary.py` — ETag `e6192697`, 45,088B, 20:35:00Z

---

## Silver Rebuild

| Step | Action | Result |
|---|---|---|
| Instance start | aws ec2 start-instances i-0ed5afded2ebd4ed4 | running |
| S3 verify | head-object convert_orion_to_silver.py | ETag 8135ada3 — MATCH |
| SSM silver run | `python3 /tmp/gold_layer_scripts/convert_orion_to_silver.py --upload --full` | SSM success |
| Guard A | rep_id allowlist filter | `inflection_wealth_management: 1,137,387 rows, rep_ids=[3, 11, 12]` |
| Guard B | Keil exclusion | `other: 3,365,122 rows, rep_ids=[1, 4, 5, 9, 13, 14, 15, 18]` |
| Guard C | advisor_firm column | present in TRN/AUM/accounts_dim writes |
| S3 verify | head-object on 2020-05-26.parquet | 21:01:59Z — fresh write confirmed |

Silver output: 1,137,387 Inflection-only rows. Guards A/B/C PASS.

---

## Full Gold Chain Run

**Dispatch command:** `bash /tmp/orion-gold-dispatch.sh --chain full --force --bg`

**CHAIN_FULL:** `A_00 A_01 A_02 A_03 A_04 B_00 B_01 B_01b B_02 B_03 C_00 C_01 C_01b C_02 C_03 C_04 C_05 C_06 C_07 C_08 I_D00 I_D00b D_00c D_02 I_D03 D_04 09`

### Run 1 — OOM Failure on C_01b

| Step | Script | Result | Notes |
|---|---|---|---|
| A_00–A_04 | dimensions/positions | Success | A_03 positions_cube: 8.47 GB RSS |
| B_00–B_03 | canonical holdings/prices | Success | — |
| C_00–C_01 | NNA | Success | — |
| C_01b | role_aua_backfill | SILENT FAIL | OOM — instance memory exhausted after A_03 8.47 GB |
| Chain exit | watchdog | Stopped instance | Chain log wiped from /tmp (tmpfs) |

### Recovery — Standalone C_01b + Resume

| Step | Action | SSM | Result |
|---|---|---|---|
| Instance restart | aws ec2 start-instances | running | — |
| C_01b standalone | `--single C_01b` | 58b34e7d | Success — 1,881 partitions |
| Resume from C_02 | `--from C_02 --force --bg` | 1c3ce5b8 | PID 2699 |

### Run 2 — C_02 to end

**SSM:** 1c3ce5b8 / dispatch PID 2699
**Completed:** 2026-04-27T22:24:46Z
**Exit:** Success, chain exit 0

| Script range | Status |
|---|---|
| C_02–C_08 | Success |
| I_D00, I_D00b | Success |
| D_00c | Success |
| D_02 | Success — 10 books, 995 client details |
| I_D03 | Success |
| D_04 | Success |
| 09 | Success |

---

## CloudFront Invalidation

- Distribution: `EVTSA9VEHNZVH`
- Path: `/api/scoped/advisor-intelligence/*`
- Invalidation ID: `IEGF5BTDPQE0IC1KLJSJ4KUXNK`
- Status: completed

---

## Post-Chain Artifact Verification

| Artifact | Size | Timestamp | Status |
|---|---|---|---|
| platinum/firm/header_metrics.json | ~95 KB | 22:24Z | present |
| platinum/firm/leaderboard.json | ~15 KB | 22:24Z | present |
| platinum/firm/timeseries_overview.json | ~52.8 KB | 22:24Z | present |
| platinum/advisors/ | 7 books | 22:24Z | present (see FLAG 2) |

---

## Open Flags — Sent to DS~A + COO via RAVC (20260427T223029Z / 20260427T223051Z)

### FLAG 1: AUA $133.7M — below $140M COO threshold, below target $191-200M

```
header_metrics.total.aua = $133,677,346
```

- Pre-filter (prior runs): $429,371,223
- Post-filter target (3 Inflection advisors × estimated AUM): $191–200M
- Actual post-filter: $133.7M

Possible causes (for DS~A investigation):
1. B_00 canonical_holdings aggregation uses pre-filter holdings artifacts — not re-filtered by rep_id
2. Double-exclusion: SCOPEFIX filter may be removing valid Inflection rows alongside Keil rows
3. Andrew noted 2023 AUM was ~$112M — $133.7M may be roughly correct for current period (investigation deferred)

### FLAG 2: 7 Advisor Books Including Keil Names

platinum/advisors/ at 22:24Z contains:
- `dan_sinnen/book.json`
- `daria_zalewska/book.json`
- `jeremy_keil/book.json`
- `john_kurcz/book.json`
- `keil_financial_partners/book.json`
- `patrick_scanlan/book.json`
- `peter_lee/book.json`

Expected post-INFGRD.002: only `daria_zalewska`, `patrick_scanlan`, `peter_lee` (rep_ids 3, 11, 12).

Root cause hypothesis: C_07 `advisor_attribution.py` derives `advisor_key` from `rep_name` in
holdings/NNA tables, not from `rep_id`. INFGRD.002 filter operates on TRN/AUM layer; if C_07
reads from a pre-filter holdings artifact (B_00), Keil advisors' rep_names still flow into
account_team → D_02 emits their books.

DS~A: audit C_07 input artifacts (what S3 key does it read for advisor-to-account mapping?)
and whether `advisor_firm` column from silver propagates through to the advisor book generation path.

### FLAG 3: advisor_name=None in Leaderboard (All 9 QTD Entries)

```
leaderboard QTD entries: 9, all advisor_name=None
```

Root cause hypothesis: D_00c name lookup (`accounts_dim → advisor_name join`) broke after
accounts_dim schema change introduced `advisor_firm` column — join key mismatch or column
position shift in the post-f4cabe05 schema.

DS~A: audit D_00c name resolution logic. Likely a broken join on `advisor_key` after
accounts_dim was written with the new INFGRD.002 column layout.

---

## RAVC Delivered

- To DS~A 0.4.0_DS_ClientPlatform~A: 20260427T223051Z
- To COO 2.0.0_SA_COO: 20260427T223029Z

DS~A to investigate 3 flags, fix, commit, and send RAVC2 to AE for INFGRD.004 re-dispatch.

---

## Andrew Note (2026-04-27)

"in 2023 aum was more like 112m or so depending on what month you look in, lets just get it done
and we'll get into the analytics later"

FLAG 1 AUA investigation deferred per Andrew. $133.7M may be directionally correct for current
period — full forensic audit is DS~A scope, not blocking RD smoke.

---

## Files Changed

| File | Action | Why |
|---|---|---|
| `org/tier2_senior/0.6.1_AE_PartnerETL/logs/2026-04-27/inf_infgrd003_chain_run.md` | created | This file |

---

## DS~A RAVC2 (20260427T223846Z) — Root Cause Identified

Root cause (all flags): stale silver partition sweep gap in `build_trn_silver()`.

For dates where ALL transactions were Keil-rep (e.g., 2024-06-15: rep_ids [5,15] only),
post-filter combined has ZERO rows → `groupby('trade_date')` skips that date → no new file
written → old pre-filter parquet (rep_ids [5,15], 33 cols, no advisor_firm) remains on S3.

A_00 reads ALL silver/transactions/ partitions → sees Keil rep_ids → accounts_dim 8 advisor_keys
→ C_07 → account_team inherits Keil → D_00c + D_02 emit Keil books.

Evidence: `silver/transactions/2024-06-15.parquet` — 4 rows, rep_id [5,15], 33 cols (PRE-rebuild).

Fix options:
- Option A: `_clear_silver_partitions_in_range()` sweep in `build_trn_silver()` before writes
  (destructive S3 delete — requires COO auth)
- Option B: per-gold-script `advisor_firm` filter on read in A_00, C_07, B_00
  (non-destructive, multiple edits)

DS~A recommendation: Option A. Pending COO authorization.
DO NOT redispatch chain until silver fix committed + COO auth confirmed.

---

## RAVC Delivered (complete)

| Agent | Timestamp | Subject |
|---|---|---|
| 2.0.0_SA_COO | 20260427T224201Z | INFGRD.003 COMPLETE + DS~A RAVC2 triage + HOLD INFGRD.004 |
| 0.4.0_DS_ClientPlatform~A | 20260427T224214Z | ACK RAVC2 — triage confirmed, AE holding |
| 0.4.2_RD_AdvisorIntelligence | 20260427T224224Z | HOLD Option C smoke — 4 flags open |

---

## CloudFront Invalidations

| ID | Paths | Status | Timestamp |
|---|---|---|---|
| IEGF5BTDPQE0IC1KLJSJ4KUXNK | /api/scoped/advisor-intelligence/* | Completed | 22:29:55Z |
| I5YEY69YS16FMJNB8LI3GEXPXQ | /platinum/firm/*, /platinum/advisors/* | InProgress | 22:41:03Z |

---

## Current State

- INFGRD.003 full chain: COMPLETE (22:24:46Z)
- Instance i-0ed5afded2ebd4ed4: stopped
- CloudFront: 2 invalidations filed (see above)
- Root cause: DS~A identified + triage sent to COO + AE + RD
- AE: idle-complete, HOLDING redispatch until COO auth + DS~A INFGRD.004 fix commit

## Outstanding Items

1. COO: authorize Option A silver sweep (destructive S3 delete) or select Option B
2. DS~A: implement authorized fix, commit, send INFGRD.004 RAVC2 to AE
3. AE (on DS~A RAVC2): silver sweep + full chain rerun (INFGRD.004)
4. DS~A: unknown/ PLACEHOLDER exclusion in D_02 `_PLACEHOLDER_KEYS`
5. DS~A (separate TO): leaderboard field rename advisor_name vs name (post-Keil-cleanup)
6. AE (post-W5): Terraform aws CLI -s shebang fix (AMI update)
7. DS/future TO: orion-gold-dispatch.sh catalog I_ prefix normalization
