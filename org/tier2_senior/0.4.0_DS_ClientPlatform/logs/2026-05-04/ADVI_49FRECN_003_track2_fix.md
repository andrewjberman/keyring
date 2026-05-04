# Session Log — ADVI_49FRECN.003 — Track 2 Fix (D_04 Sidecar + AC#1-6)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-04
**Task Order:** ADVI_49FRECN.003
**Status:** HANDED OFF TO DS~C — Andrew directive 2026-05-04. DS~B fix commits (e66898a64 + 386456223 + 76a3a9418 + 76a3a9418) remain attributed to DS~B. DS~C owns RAVC4 + TO close. Chain QA re-dispatch to AE redirected to DS~C.

---

## Summary

ADVI_49FRECN.003 Track 2 fix execution. Formalizes already-shipped BFIX3 (9fde23538) and A_03
Option B (e09cb806b); adds c1_recovered_accounts.json sidecar to D_04 with TO-compliant schema
(AC#2); creates standing backlog doc (AC#6, pending CTO commit to CTO-owned docs/architecture/).
AQR filter confirmed absent in D_04 (AC#1); inclusion handled by A_03 e09cb806b. AC#5 C1c PARK
recommendation sent to CTO for ack. RAVC2 to AE 0.7 for QA dispatch sent.

---

## Compiler Tools

| Tool | Target | Result | Notes |
|------|--------|--------|-------|
| comp-pipescript io | D_04 | 25 reads, 22 writes — canonical_holdings_key now registered as read (added e66898a64) | Phase 1 mandate |
| comp-platinum reverse | c1_recovered_accounts.json | Zero consumers — forensic-only initial state | Phase 1 — expected |
| comp-platinum reverse | out_of_scope_accounts.json | Zero consumers — no FE wiring yet | Phase 1 — sister artifact, confirmed |
| grep AQR in D_04 | D_04.client_portal_summary.py | ZERO matches — chained to A_03 per Phase 1 mandate | AC#1: no filter in D_04 |
| grep AQR in A_03 | A_03.positions_cube.py | 'DELPHI' in _PAR_VALUED_PATTERNS (line 301) — PRICING RULE, not exclusion | AC#1 clarification |
| ds-commit-gate | D_04.client_portal_summary.py | PASS (e66898a64) — ruff F841 dim_cols fixed before commit | Phase 2 |
| ds-commit-gate | D_04.client_portal_summary.py | PASS (386456223) — ruff F841 open_date_str fixed before commit | Phase 2 schema revision |
| comp-pipescript deployed | D_04 | MATCH — both commits uploaded sequentially | Phase 2 |

---

## AC#1 — D_04 AQR Filter Removal

**Finding:** No AQR exclusion filter exists in D_04.client_portal_summary.py (grep zero matches).
Phase 1 mandate instruction followed: chased chain to A_03.

**Actual filter location:** `data/black_diamond/scripts/gold/A_03.positions_cube.py` line 301,
`_PAR_VALUED_PATTERNS = (..., 'DELPHI', ...)`. This is a **pricing rule** (forces $1.00/unit for
AQR TA DELPHI PLUS FUND LLC, a par-valued hedge fund), NOT an account exclusion.

**AQR inclusion mechanism:** AQR accounts were missing from gold because A_03 only ingested
TXN_DAILY, and AQR delivers positions via UNREALIZED_DAILY only. The already-shipped A_03 Option B
fix (e09cb806b) added the unrealized injection path, which now captures AQR accounts. No D_04
change needed for inclusion.

**Sidecar detection:** Added AQR_INCLUDED mechanism in build_c1_recovered_accounts() — detected
by 'DELPHI' substring in asset_names from canonical_holdings for the recovered account.

**AC#1 verdict:** Satisfied by e09cb806b. No D_04 filter to remove. Documented here.

---

## AC#2 — c1_recovered_accounts.json Sidecar Schema

Initial implementation (e66898a64) used preliminary schema. Revised to TO AC#2 spec in 386456223.

| Field | Status |
|-------|--------|
| total_recovered_count | Implemented (was total_count) |
| total_recovered_aua | Implemented |
| count_by_mechanism / aua_by_mechanism | Implemented |
| count_by_advisor / aua_by_advisor | Implemented |
| accounts[].account_id | Implemented |
| accounts[].advisor_id | null first ship (not in silver/allocations) |
| accounts[].advisor_name | Implemented (from architect field) |
| accounts[].household_id | Implemented (from accounts_dimension.relationship_id) |
| accounts[].recovery_mechanism | Implemented: B_00_BFIX3 / AQR_INCLUDED / A_03_OPTION_B |
| accounts[].aua | Implemented (was recovered_aua) |
| accounts[].first_seen_rps | null first ship (requires RPS history scan) |
| accounts[].first_txn_posted | null first ship (requires txn history scan) |
| accounts[].rps_lag_days | Proxy: (snapshot - account_open_date).days for BFIX3/AQR; null for A_03 |
| accounts[].rps_lag_flag | rps_lag_days > 7 where computed; null otherwise |

**Null-field plan (first ship):** first_seen_rps, first_txn_posted require loading RPS history
parquets not currently in D_04's read scope. rps_lag_days for A_03_OPTION_B also null for same
reason. All will be populated in a future TO when RPS history scan is added to D_04.

---

## AC#3 — B_00 BFIX3 Ratification (9fde23538)

Pre-fix state per .002.5 investigation:
- C1b-RECONCILE_DROP: 40 accounts, $38.5M (all positions bd_stale, zeroed out by reconcile)

Post-fix mechanism: BFIX3 detects all-stale alive accounts (alive_ids = silver/allocations
AUA >= $100), re-injects from BD bronze with source='bd_new_acct'. No time-based N-day window —
gate is AUA-based only.

Expected post-fix RECONCILE_DROP bucket: near-zero (these accounts now appear in canonical_holdings
with real positions). Verification will complete on QA run.

N-day bandaid note: BFIX3 has no N-day threshold. The bandaid is the AUA >= $100 alive gate.
Documented in docs/architecture/49FRECN_STANDING_BACKLOG.md (pending CTO commit).

---

## AC#4 — A_03 Option B Ratification (e09cb806b)

Pre-fix state per .002.5 investigation:
- C1b-AQR: 6 accounts, $11.8M (no TXN_DAILY; UNREALIZED_DAILY only)
- C1b-SMA-UNREALIZED: 2 accounts, $3.2M (large SMA, unrealized only)
- C1b-TXN_LAG: 10 accounts, $6.8M (unrealized + TXN exists, cube predates TXN)
- Combined: 18 accounts, ~$21.8M

Post-fix mechanism: rps_covered narrowed to covered_with_events (accounts with actual RPS events).
Accounts not in covered_with_events fall through to unrealized buy-injection path. AQR + SMA +
TXN_LAG accounts now enter positions_cube via unrealized injection.

Expected post-fix ingestion-gap residual: C1b-NEW 4 accounts ($4.1M) only (genuinely-new, no BD
coverage). Verification will complete on QA run.

---

## AC#5 — C1c Ship-or-Park Decision

**Decision: PARK** — Confirmed by both CTO (RAVC3, 20260504T~121226Z) and COO.

CTO rationale (from RAVC3):
- Mechanism detection requires first_seen_rps not in D_04 scope — emitting unclassified rows is noise with no operator-actionable attribution.
- Phase 1.5 sub-investigation (a093a4df4) already documents C1c volume in recon report; reference for residual exists.
- Small fraction (6.3% of C1) — deferring keeps first ship clean.

Trigger conditions to revisit (CTO ruling):
- C1c bucket grows beyond 20 accounts in a single run
- 49F headcount reconciliation residual exceeds 1% attributable to unclassified C1c
- first_seen_rps data becomes available in D_04 scope (RPS history step added to gold)

D_04 sidecar ships with empty C1c emit (no GENUINELY_NEW_C1C rows). CTO will add C1c as
Bandaid 3 in standing backlog if/when trigger fires.

---

## AC#6 — Standing Backlog File

**COMMITTED** by CTO as `33e1ccaa0` (CTO-owned path docs/architecture/; CTO author per owned-paths lane).
Authored "by 0.4.0_DS_ClientPlatform~B per ADVI_49FRECN.003 AC#6" in message body.

Content:
1. B_00 BFIX3 AUA gate bandaid + trigger conditions
2. 7-day TXN_LAG tolerance bandaid + trigger conditions
CTO will add C1c as Bandaid 3 if/when C1c trigger fires.

---

## Files Modified

| File | Change |
|------|--------|
| data/black_diamond/scripts/gold/D_04.client_portal_summary.py | Added canonical_holdings_key import; C1_RECOVERED_ARTIFACT_KEY + _RPS_LAG_FLAG_DAYS constants; build_c1_recovered_accounts() function (Step 17); wired into main(). Schema revised to TO AC#2 spec in follow-up commit. |
| docs/architecture/49FRECN_STANDING_BACKLOG.md | NEW — COMMITTED by CTO as 33e1ccaa0 (CTO-owned path, authored by DS~B per AC#6) |

---

## Deploy Cycle (CLAUDE.md Rule 13)

| Step | Result |
|------|--------|
| Pre-commit gate (e66898a64) | PASS — py_compile + AST + ruff (1 F841 fixed) |
| Commit 1 | e66898a64 — feat(D_04): sidecar initial implementation |
| Pre-commit gate (386456223) | PASS — py_compile + AST + ruff (1 F841 fixed) |
| Commit 2 | 386456223 — fix(D_04): schema revision to TO AC#2 spec |
| Push | origin/CLOUD — 02216bc67..386456223 |
| S3 upload | s3://opal-data-bd/code/gold/D_04.client_portal_summary.py (151.1 KiB) |
| comp-pipescript deployed | MATCH |
| RAVC2 to AE 0.7 | Sent 20260504T121244Z — QA dispatch pending |
| CTO RAVC3 received | 20260504T~121226Z — AC#5 PARK approved; AC#6 standing backlog committed 33e1ccaa0 |
| RAVC2 follow-up to AE 0.7 | Sent 20260504T121709Z — artifact not yet on S3; dispatcher follow-up |
| QA run 1 (single D_04) | CONDITIONAL_FAIL — total_recovered_count=2673 (40x over-expected); excluded_c1_count=58 (unchanged); two root causes identified |
| D_04 logic fix (76a3a9418) | Root cause 1: c1_universe intersect gold = entire firm; fixed with first-seen-in-gold >= 2026-05-01 filter; pre-commit PASS; S3 MATCH |
| Chain re-dispatch request | Sent 20260504T123241Z — --chain downstream from B_00 required; root cause 2: intermediate parquets don't have BFIX3/Option B applied |

---

## B_00 + A_03 Commit Reference

| Commit | Description | Ratification |
|--------|-------------|-------------|
| 9fde23538 | B_00 BFIX3 — rescue all-stale alive accounts | AC#3 ratified |
| e09cb806b | A_03 Option B — rps_covered narrowed to covered_with_events | AC#4 ratified |
| e66898a64 | D_04 sidecar initial | AC#2 initial |
| 386456223 | D_04 sidecar schema revision | AC#2 final |
| 33e1ccaa0 | docs/architecture/49FRECN_STANDING_BACKLOG.md — CTO author, DS~B content | AC#6 complete |
| 76a3a9418 | fix(D_04): scope c1_recovered to first-seen-in-gold >= fix_date | QA logic fix |

---

## Next Steps

[AE 0.7] Chain re-dispatch — bd-gold-qa-runner --chain downstream from B_00 (rebuilds canonical_holdings + positions_cube with BFIX3/Option B, then D_04)
  - Chain re-dispatch request sent 20260504T123241Z
  - Expected: total_recovered_count ~58-73, excluded_c1_count ~2-4
[DS~B] On QA PASS: RAVC4 to CTO + COO with:
  - D_04 commit refs (e66898a64 + 386456223) + B_00 (9fde23538) + A_03 (e09cb806b) + standing backlog (33e1ccaa0)
  - c1_recovered_accounts.json S3 ETag + total_recovered_count + total_recovered_aua
  - QA run-id
  - AUA recon (~$1,720M firm AUA expected)
[DS~B] Mark TO complete on RAVC4 sent
