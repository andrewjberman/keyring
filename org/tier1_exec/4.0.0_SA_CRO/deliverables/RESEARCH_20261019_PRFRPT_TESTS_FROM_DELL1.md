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

## Test 2 -- the seam: READ FROM THE ON-HAND `.trn` (no new export needed), measured

The standard `.trn` already spans 2026-05-26 to 2026-10-16. Comment rows (`;`) were attached to the data row before them on the same
account.

| Measure (the 643 BD Fidelity IWS accounts) | Value |
|---|---|
| accounts with any `.trn` row | 642 (69,320 rows) |
| rows carrying a TRANSFER comment | 541 rows, on **186 accounts** |
| ...codes | `dp*` ca 415, `wd*` ca 120, `sl*` eu 5, `wd*` ex 1 (the `*` flag marks them) |
| ...by month | 2026-06: 66, 07: 262, 08: 90, 09: 73, 10: 50 |
| ...inside 2026-06-01 to 07-15 | **275 rows on 145 accounts**, ISO weeks 25: 1, 26: 57, 27: 101, 28: 96, 29: 20 (about 06-22 to 07-17) |
| accounts whose transfer comments **name their own Commonwealth number** (BD `NFS Account Number`) | **106 of 643** |

The comment phrasings are "CONVERSION TRANS:REORG ACTIVITY OR ACCT ..." (526 rows), "TRANSFERRED FROM VS <id> ACATS" (196), "TRANSFERRED
FROM VS <id>" (114), "TRANSFERRED TO VS <id>" (91), plus RGY and REDEM variants.

**Reading (I):**
- **The seam is datable from Fidelity's own file.** The transfers cluster in late June to mid July, matching BD's empty window of
  06-22 to 07-09.
- **For 106 accounts Fidelity's own transactions carry the Commonwealth number.** That is a Fidelity-side key for part of the book. The
  other 537 still need BD's frozen attribute.
- **The flagged transfer rows are cash journal entries (`ca`), not security receipts.** No `by` / `li` security rows with a transfer
  comment were found, so opening security positions are **not** shown as in-kind receipts in this file. Whether they are carried some
  other way, for example as the first positions after a conversion row, is unmeasured.

## Test 3 -- dedup: PARTIAL

- **Standard `.trn` has no transaction-id field.** Its columns are account, code, trade date, security type, symbol, amount, cash/client,
  quantity, broker, commission, settle date and comment. Rows: 387,037 data rows (the 14,556 `;` comment rows excluded). **259 extra rows
  are exact duplicates (0.07%) across 208 groups.** So row identity is not unique, and a dedup rule cannot be "drop exact duplicates"
  without losing genuine same-day repeats. The two cannot be told apart from this file.
- **Custom `transact.txt` (66 columns): unmeasured.** It was not handed over.
- **Does a daily file repeat earlier days?** Unmeasurable until there are two scheduled daily files. The first recurring v1.0.1 run
  lands on 2026-10-20.

## Test 4 -- parity: not this seat's (IRPT_DASHBD, once files land)
