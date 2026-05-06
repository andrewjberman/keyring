# AE 0.7.0 Session Log — 2026-05-06
## D4 Chain Dispatch + ADVI_LDRBRD.001 Bug A/C Verification

**Session scope:** Dispatch D4 `--from INF_D_00c` on inf-gold-layer-runner after DS~D RAVC3 (Bug A+C fix commit `0755a2330`). Verify Bug A + Bug C in chain output. Send RAVC3 to COO + DS~C.

**Secondary scope:** INFREL.001 secondary role — EventBridge + S3 audit for silver-chain staleness root cause classification (class a/b/c).

---

## Timeline

| Time (UTC) | Event |
|---|---|
| ~13:10Z | Received DS~D RAVC3: Bug A+C fixes in commit `0755a2330` |
| 13:14:56Z | D4 chain dispatched via SSM `dbf14149-e0e2-4ec1-ba6a-2d68918d5bc9` |
| 13:15:05Z | INF_D_00c started on runner |
| 13:15:13Z | `accounts_v2_dim` loaded: 849 rows (2026-04-29 snapshot) |
| 13:15:18Z | Bug A WARN fired: `no holdings snapshot on or before 2000-01-01 -- using earliest available: holdings_2019-09-17.parquet` |
| 13:15:18Z | Bug C2 WARNs: `lifecycle split failed for peter_lee/patrick_scanlan/joe_brandenburg/firm: int64 vs object for key 'account_id'` |
| 13:15:19Z | INF_D_00c complete; leaderboard 10.4 KB written |
| 13:15:19Z | `gold/artifacts/employee_leaderboard.json` written (precursor copy) |
| 13:17:20Z | CHAIN COMPLETE (INF_D_00c through INF_D_08) |
| 13:29Z | RAVC3 to COO + DS~C sent |

---

## D4 Chain Evidence

- **SSM command ID:** `dbf14149-e0e2-4ec1-ba6a-2d68918d5bc9`
- **Chain log:** `s3://opal-data-inf/gold/logs/from_INF_D_00c_20260506_131456.log` (244,809 bytes)
- **Scripts run:** INF_D_00c INF_D_02 INF_I_D02b INF_I_D03 INF_I_D02d INF_D_04 INF_09 INF_D_05 INF_D_06 INF_D_07 INF_D_08
- **Duration:** ~2.5 minutes

### Fresh Artifacts
- `gold/artifacts/employee_leaderboard.json` — 2026-05-06T13:16:13Z
- `gold/artifacts/summary/header_metrics.json` — 2026-05-06T13:16:45Z
- `gold/artifacts/firm_mix_views.json` — 2026-05-06T13:15:48Z
- `/firm/leaderboard.json` — 10,631 bytes — 2026-05-06T13:15:18Z
- `/firm/dashboard.json` — 306 bytes — 2026-05-06T13:16:44Z
- `/advisors/inflection_wealth_management/`, `/advisors/joe_brandenburg/`, `/advisors/patrick_scanlan/`, `/advisors/peter_lee/` — 4 files each (book.json, composition.json, summary.json, top_holdings.json)
- `/firm/` — 16 files total

---

## Bug A Verification — CONFIRMED FIXED

**Evidence:** Chain log at 13:15:18Z:
```
WARN: no holdings snapshot on or before 2000-01-01 -- using earliest available: holdings_2019-09-17.parquet
```
DS~D's fallback code (`keys[0]` when `best_key is None`) executed correctly for MAX window. `period_start_aua=None` for MAX/YTD in leaderboard output is expected behavior (no valid AUA snapshot at window start date; NNA computed via fallback).

---

## Bug C Verification — PARTIAL (Bug C2 surfaced)

**DS~D fix confirmed deployed:** `accounts_v2_dim` loaded 849 rows and passed into lifecycle computation path. This confirms the code fix (forwarding accounts_v2_dim to `_compute_hh_lifecycle()`) is deployed.

**New runtime failure — Bug C2:** All lifecycle splits fail with dtype mismatch:
```
WARN: lifecycle split failed for peter_lee: You are trying to merge on int64 and object columns for key 'account_id'
WARN: lifecycle split failed for patrick_scanlan: [same]
WARN: lifecycle split failed for joe_brandenburg: [same]
WARN: firm lifecycle split failed: [same]
```
Appears across all 3 windows (QTD, YTD, MAX) — 8 total occurrences.

**Root cause:** `accounts_v2_dim.account_id` is int64; the join-side column in the lifecycle merge is object dtype. `pd.merge` rejects the mixed-type join.

**Fix required (DS lane):** `.astype(str)` coercion on `account_id` on both sides before `pd.merge` in `_compute_hh_lifecycle()`. Assign to DS~D.

**Result:** `lifecycle_aua = {nmnc: 0.0, nmec: 0.0, existing: 0.0}` for all advisors, all windows.

---

## Leaderboard Values (D4 Run)

| Window | total_aua | total_nna | new_clients |
|---|---|---|---|
| QTD | $199,649,186.31 | -$1,358,124.82 | 9 |
| YTD | $199,649,186.31 | $115,117.15 | 18 |
| MAX | $199,649,186.31 | $13,874,710.43 | 309 |

**Dashboard.json (`/firm/dashboard.json`):**
- `headline.total_aua`: $182,552,380.96
- `account_count`: 794 | `client_count`: 307 | `advisor_count`: 3
- `ytd.nna`: $115,117.15

Note: $17M discrepancy between leaderboard ($199.6M) and dashboard ($182.5M) flagged to COO for DS review.

---

## INFREL.001 Secondary Audit (completed earlier this session)

**Scope:** AE 0.7 secondary — EventBridge `inf-silver-chain-bronze-complete` rule firing history + S3 sentinel audit.

**Findings:**
- Lambda invokes: 11 in 14 days, 0 errors — CW logs clean
- S3 sentinel: `_BRONZE_COMPLETE.json` found on all fresh-bronze dates checked
- EventBridge rule: firing correctly on sentinel creation
- **Classification: Class (c)** — Lambda invokes and succeeds, but per-dim conversion errors are silently suppressed. Silver dims appear stale because conversion fails quietly.

**RAVC3b sent to AE 0.6.1 LEAD** for Phase 0 RAVC3 incorporation. AE 0.6.1 LEAD confirmed receipt.

---

## SSM Dispatch Issue (carry-forward from prior session)

First SSM attempt (e6892232) failed — heredoc delimiter escaping issue caused the script body to be consumed as file content. Only `SHUTDOWN_CANCEL: issued` appeared in stdout. Fix: replaced `<<'EOF'` heredoc with `printf '...\n'` pattern. Second attempt (dbf14149) succeeded with all 4 steps confirmed.

---

## Open Items

1. ~~**Bug C2 fix**~~ — RESOLVED by D5 (see below).
2. **Dashboard vs leaderboard total_aua discrepancy** — $182.5M vs $199.6M. DS review item.
3. **Lambda INITIAL_RATE bump** — AE 0.6.1 coordination to bump TO-1/2/3 Lambdas from 1.0 → 30-50 RPS per CTO rate-empirical finding. Lower priority; post-INFREL.001 Phase 1 fix.
4. **OUTPUT_PREFIX double-slash paths** — Platinum artifacts land at `/firm/` and `/advisors/` (leading-slash S3 keys) instead of `platinum/firm/inflection/`. Functional but non-canonical path. Requires gold runner OUTPUT_PREFIX investigation.

---

## D5 Chain — Bug C2 Fix Verification

**Trigger:** DS~D RAVC2 at 13:35:31Z — Bug C2 fix shipped (commit 46d55bc51, S3 ETag eafd00520c5bcee7d0fdd4c7fc7800d7, 42,687 bytes, 13:33:56Z).
**Fix:** 3 `.astype(str)` coercions on `account_id` in `_compute_hh_lifecycle()` before all pd.merge calls.

**SSM:** f9dacdd0-080d-4352-83af-442b8cd5624f
**Chain log:** gold/logs/from_INF_D_00c_20260506_133647.log (240,255 bytes)
**Duration:** 13:36:47Z → 13:39:04Z (~2.3min)

**Bug C2 — CONFIRMED FIXED**

| Advisor | nmnc | nmec | existing |
|---|---|---|---|
| Peter Lee | $16,589,270 | $6,630,370 | $138,647,490 |
| Patrick Scanlan | $939,657 | $472,714 | $19,173,247 |
| Joe Brandenburg | $1,897,010 | $272,681 | $13,988,493 |
| Firm aggregate | $19,682,951 | $7,486,368 | $171,801,491 |

Identical lifecycle_aua values across QTD/YTD/MAX (snapshot-based computation).

**AC1 (MAX period_start_aua):** waived by COO — data-bounded, not a code defect.
**AC2 (lifecycle_aua non-zero):** PASS — all advisors, all windows.

Fresh artifact: gold/artifacts/employee_leaderboard.json generated_at 2026-05-06T13:38:01Z.
RAVC3 to COO + DS~D sent at 13:39:47Z / 13:39:52Z.
