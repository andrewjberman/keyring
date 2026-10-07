# ADVI_COTBKF decomposition -- ROUND 5 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~08:5xZ)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-4 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_4_20261007.md`
@e363a194ed (msg 158; ENRICHMENT LIST E1-E5), on `3.0.0_SA_CVO`'s compile @2114a2a7a2 (ADJUDICATION_v3, REMEDIATION_v2, grade file
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_4_L9_GRADE_20261007.md`), and under laptop `1.0.0_SA_CTO`'s rulings of 08:5xZ
(`CTO_RULINGS_FOR_THE_DELLS_20261007_0850Z_TRADING_CALENDAR_AND_ROW_IDS.md`, relayed by `0.0.0_AB_MSTR~DELL2` msg 178): **RULING A, a HOLD
on dell2 producing, landing or grading anything dated before 2024-01-01 through `lib/trading_calendar.py` until RULING B's fix is on this
box.** Decomposition and code work continue.

**Rule 24.** Domain: the five enrichment items E1-E5. Subtraction, each against the world at the cut:
- **E1** (the three calendar readers refuse an uncovering calendar): one cell, `CB-e-1`. Code only; its check writes nothing that persists.
- **E2** (links and census on a covering calendar, then the links applied): **NOT CUT this round.** The analysis gates it on
  `lib/trading_calendar.py` covering 2013 onward on dell2, and RULING A holds every pre-2024 production here until RULING B's fix lands
  (an NFRA_CTLPLN round-4 cell, `2.0.0_SA_COO~C`). It is cut in the issuance that follows the fix. Rows S9 and W12-S1 stay ARMED until then.
- **E3** (the unique documents and the documents table applied): split by actor. The CODE half (every planned key checked against the
  C-RESTRICTED prefix, held back and counted) is cell `CB-e-3`. The APPLY half is the issuer's act at the drain (below). The documents
  script reads no calendar (0 imports of `trading_calendar`), so RULING A does not bind it.
- **E4** (the C-RESTRICTED apply write-in): one cell, `CB-e-4`, LOCAL: a request record and a note; no AWS act.
- **E5** (the round-4 crosswalk applied): no code; the issuer's act (below). The crosswalk script reads no calendar (0 imports).

Three cells, one intent each, disjoint writes. Chains: E1 then E2 (E2 uncut); E3, E4, E5 independent.

## Measured constraints (read at the base, dell2, 2026-10-07 ~08:4xZ-08:5xZ)

1. **Calendar:** `calendar_source()` = `NYSE/hardcoded-fallback-2024-2027`; `pandas_market_calendars`, `holidays`, `exchange_calendars`
   absent. `trading_calendar` imports: `commonwealth_account_links.py` 3, `commonwealth_price_census.py` 2, `commonwealth_price_need.py` 4;
   `commonwealth_crosswalk.py` 0, `commonwealth_documents.py` 0.
2. **Cause of S9:** measured twice -- `1.0.0_SA_CTO~DELL2` (analysis section 1) and this seat (row S10 @3dd25927f2, 1,450 of 1,450 rows equal
   under 127 rule-derived pre-2024 holidays).
3. **Documents plan at the base:** `DOCUMENTS-PLAN unique=11119 every_document_once=True sources_verified=11119 refused=0 keys_unique=True
   bytes=1795905639` (no held-back field).
4. **C-RESTRICTED** (merged @85d8b5f20f, NOT applied): `s3-lgic-firm-buckets.tf:177-275` -- statements DenyRestrictedReadExceptReaders,
   DenyRestrictedListExceptReaders, DenyRestrictedWriteExceptBreakglass on prefix `commonwealth/cottonwood/bronze/crm/`; role
   `cloudops-cot-restricted-breakglass-role` (module `opal_name_restricted_breakglass`), trust = console user only; inline policy
   `restricted-prefix-get-put-list`. Its check `tests/check_restricted_prefix.py` needs terraform (absent on dell2, row S7).
5. **Write-in tool:** `org/devices/role_request.py` (NFRA_CTLPLN CT-c-2 @003fc334e5); `write` records under
   `org/devices/role_requests/<device>/` and sends one bus line to the laptop; `validate` prints `ROLE-REQUEST-VALID <id> ok=<bool>`.

## The cells

| cell | what | serves | risk | chain / slot |
|---|---|---|---|---|
| `CB-e-1` | the three calendar readers exit non-zero with `CALENDAR-UNCOVERED <years>` when `calendar_source()` does not cover their table's dates | S9, W12-S1 (FWD-3, FWD-9) | LOCAL | A, `0.9.0_WK_ADVI_COTBKF~17` |
| `CB-e-3` | the documents script holds back and counts every planned key under the C-RESTRICTED prefix; the plan line prints `held_restricted=<n>` | FWD-5 | LOCAL | B, `0.9.0_WK_ADVI_COTBKF~18` |
| `CB-e-4` | the C-RESTRICTED apply write-in: one valid role request on dell2 and a note carrying the CB4d4-AC1 re-run | FWD-7, FWD-4, FWD-2; S7 | LOCAL | C, `0.9.0_WK_ADVI_COTBKF~19` |

## Write sets (disjoint)

- **CB-e-1:** `data/assets/scripts/silver/commonwealth_account_links.py`, `data/assets/scripts/analysis/commonwealth_price_census.py`,
  `data/assets/scripts/analysis/commonwealth_price_need.py`, `data/assets/scripts/silver/commonwealth_calendar_guard.py` (new),
  `data/assets/scripts/silver/tests/test_commonwealth_calendar_guard.py` (new).
- **CB-e-3:** `data/assets/scripts/silver/commonwealth_documents.py`, `data/assets/scripts/silver/tests/test_commonwealth_documents.py`.
- **CB-e-4:** `org/devices/role_requests/dell2/` (one new record), its deliverables folder.
- Each: its deliverables folder and the investigation file.

**Ordering and fan-out:** `fanout: 3 of 3 chains, cap 8` -- no cell consumes another's output this round.

## The issuer's acts (one change-management ledger entry, opened at the first apply)

1. **E5:** `commonwealth_crosswalk.py --apply` (silver `crosswalk`, date=2026-06-23, re-written: round 3's table is replaced by round 4's),
   read back matched 439 / not_matched 1,094, `near_matches_applied=0`. Moves served output: under a never-widen pair (`1.0.0_SA_CTO~DELL2`
   + this seat) naming the blast radius (one key prefix, rollback = round 3's objects re-written from the round-3 run).
2. **E3 apply, after CB-e-3 drains:** `commonwealth_documents.py --apply` (silver `documents`, about 11,119 objects, plus the documents
   table; first mint), count = plan less held-back; read back by count and a sample of SHA-256s; one statement and one tax form found
   by account and date and opened for the CVO (CB4d5-AC3).
3. **E4, after CB-e-4 drains:** the request record's path sent to `1.0.0_SA_CTO~DELL2`, which forwards it. The apply is the laptop's.
4. **RULING C rows:** this lane's dell2-made pre-2024-dated artifacts listed as rows (the round-4 census deliverable's day figures; the
   real-run outputs in `.scratch/`); none served, landed or graded REALIZED before the fix.
