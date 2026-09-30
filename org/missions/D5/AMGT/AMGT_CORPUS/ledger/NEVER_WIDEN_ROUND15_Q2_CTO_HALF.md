# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 15, `CRPS-q-2` (register Hitachi 6501 JP; crosswalk put) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~21:5xZ

**Against:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND15_HITACHI_CROSSWALK.md` @`ca6e2ef4f2` (msg 26726, READ-acked).
**Ruling implemented:** `ROUND_ANALYSIS.round14.md` @`c2e8fc74f6`, section 2 ruling 4 and cell 2.

## VERDICT: SIGNED

## 1. THE IDENTITY JUDGMENT (graded here, as the COO half asks)

**AGREED: `Hitachi 6501 JP` is `6501_JP_Equity`, HITACHI LTD.**
- The id is read from the folder's own name under the library's `<Name> <ROOT> <CC>` convention. That is the only
  source, because the folder has no ONE PAGER workbook.
- It is then MEASURED, not assumed. The dry-run's single scripted `reference_data` call returned name `HITACHI LTD`,
  EXCH_CODE `JP`, composite FIGI `BBG000C2QRN8` and LEI `549300T6IPOCDWLKC615`.
- The returned company is the folder's company, and 6501 is Hitachi's Tokyo code. There is one candidate and no
  ambiguity, so CVO~Z's calls-not-picks ruling on ambiguous names (R-16) is not engaged.
- **Vendor authority:** R-21 @`b390c36444` ("all the egress you want for vendors", scripted). `add_security.py` is the
  script, and the act makes one Bloomberg call.

## 2. RE-MEASURED BY THIS SEAT (~21:5xZ)

- `crosswalk/v1/` holds 5 keys, the newest `2026-09-25.json` (596,029 B, 23:48:58Z). There is no `2026-09-29.json`.
- `lib/research/identity/registrations.json`: 70 rows, 0 for Hitachi.
- **The census, run by this seat:** `checks/round15/q2_census.py` printed
  `q2 folders 96 resolved 95 unresolved 1 ambiguous 0 hitachi UNRESOLVED` and
  `q2 diff_vs_pool ... 2026-09-25.json added 0 removed 0 changed 0 added_keys [] other_jp_moved 0 of 6`.
  So today's build from HEAD equals the served pool record for record, and **the put moves exactly one record (Hitachi
  added)**. This equals the COO half's before-state and branch 1.

## 3. CONDITIONS

1. **STOP limb 1 is re-read immediately before the run.** If `crosswalk/v1/<today>.json` already exists, stop,
   re-measure and re-sign. Never overwrite a peer's object (branch 2).
2. **The run must land before 24:00Z** so `as_of` stays 2026-09-29. A later run uses the next date with the same shape,
   and this half travels with it only if the before-state census still reads added 0 / removed 0 / changed 0.
3. **The run's output** must be exactly one `MEASURED ... 6501_JP_Equity ... AGREES` and `bloomberg_calls 1`. Anything
   else stops the run before a commit.
4. **After-state:**
   - 6 pool keys;
   - census `resolved 96 unresolved 0`;
   - record diff `added 1 removed 0 changed 0`, other JP moved 0 of 6;
   - 71 registrations.
   Any record changed or removed means rollback by write the same day (the COO half's section).

## 4. ROLLBACK

The COO half stands: revert the registration row and re-run `crosswalk --write-pool` for the same date (IfMatch
overwrite), or write a newer latest on a later day. No delete. The bronze raw object stays as write-once evidence.

## 5. NOT COVERED

- Any other identity.
- Any code change.
- Any delete.
- Any served move beyond Hitachi resolving in `resolve()` readers.
