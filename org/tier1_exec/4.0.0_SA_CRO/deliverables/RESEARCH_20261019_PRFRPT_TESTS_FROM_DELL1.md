# RESEARCH 2026-10-19 -- PRFRPT section 6 tests owed by 4.0.0_SA_CRO~FIDELITY (dell1)

**Answers:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/PRFRPT_FIDELITY_VS_BD_STITCH_BASE_20261019.md` section 6 (4.0.0_SA_CRO~PRFRPT, dell2,
commit 8477fe8571), relayed by 0.0.0_AB_MSTR~DELL1 msg 8493.
**Inputs:**
- Black Diamond Cottonwood silver: `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_allocations/date=2026-10-16/data.parquet`,
  1,600 rows, 946 distinct accounts.
- The Fidelity Standard Format A files `FI101626.*` held on dell1.

Counts only; no account numbers or client values. Account numbers were compared after normalising to `[A-Z0-9]`.

## Test 1 -- does the Fidelity number join? YES, 639 of 643 (measured)

| Measure | Value |
|---|---|
| BD distinct accounts with Custodian `Fidelity IWS` | 643 (642 all-digit, 1 letter-prefixed) |
| ...found in `FI101626.naa` (5,007 accounts, the Alongside book) | **639 of 643 (99.4%)** |
| ...misses | 4, all 9-digit; none match on the last 9 characters either |
| ...with positions in `FI101626.ipn` (4,873 accounts) | 623 |

- The 4 misses are not examined further. Candidates: accounts closed or opened between BD's 10-16 snapshot and the Fidelity export, or
  accounts under a G number outside this login.
- **Prior / transfer-from key:** the 554 BD `NFS Account Number` values (the Commonwealth numbers) appear **0 times** anywhere in the
  `.naa` text, including its one unique-per-account id field `[26:36]`. **Standard Format A does not carry the Commonwealth number, so the
  key stays BD's frozen attribute.**
- The custom `account.txt` (141 columns) has not been handed over, so whether IT carries a prior-account field is **unmeasured**.

## Test 2 -- the seam (2026-06-01 to 07-15 in-kind receipts): NOT RUN

This needs an on-demand transactions export over that range, which is Andrew's export click. Nothing was requested from Wealthscape.
Note that the standard `.trn` on hand spans 2026-05-26 to 2026-10-16 already: 47,024 rows in 2026-06 and 116,062 in 2026-07, across the
whole book. A follow-up can read the seam from it directly for the 639 joined accounts without a new export. That read was not done in
this turn.

## Test 3 -- dedup: PARTIAL

- **Standard `.trn` has no transaction-id field.** Its columns are account, code, trade date, security type, symbol, amount, cash/client,
  quantity, broker, commission, settle date and comment. Rows: 387,037 data rows (the 14,556 `;` comment rows excluded). **259 extra rows
  are exact duplicates (0.07%) across 208 groups.** So row identity is not unique, and a dedup rule cannot be "drop exact duplicates"
  without losing genuine same-day repeats. The two cannot be told apart from this file.
- **Custom `transact.txt` (66 columns): unmeasured.** It was not handed over.
- **Does a daily file repeat earlier days?** Unmeasurable until there are two scheduled daily files. The first recurring v1.0.1 run
  lands on 2026-10-20.

## Test 4 -- parity: not this seat's (IRPT_DASHBD, once files land)
