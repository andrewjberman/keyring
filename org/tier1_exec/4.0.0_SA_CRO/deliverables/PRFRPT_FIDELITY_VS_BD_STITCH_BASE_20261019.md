# Cottonwood: Fidelity vs Black Diamond as the base for performance and for the Commonwealth stitch -- 2026-10-19

Author: 4.0.0_SA_CRO~PRFRPT (dell2). Order: `ANDREW_DIRECT_20261019_19xxZ_FIDELITY_SHAPE_VS_BD_AND_COMMONWEALTH_STITCH.md`.
Read-only. (M) measured today, (I) inferred, (H) hypothesis with its test. Counts only; no client values.
Builds on: `RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md` (4.0.0_SA_CRO~FIDELITY, dell1),
`PRFRPT_PERFORMANCE_REPORTING_HOLES_20261019.md`, `ADVI_COTBKF_PRD.md`, IRPT_DASHBD TO-DB-b-235 (key-map read, 10-15).

## 1. Recommendation

**Stitch the Commonwealth history to Fidelity, not to Black Diamond.** Use Black Diamond for two things only: a
one-time source for the account key (freeze it now) and the source for the roughly 31% of Cottonwood value that is not
at Fidelity, until each of those custodians has a feed of its own. The fix to the Black Diamond reader still lands,
because Black Diamond is what clients see today.

## 2. The key already exists, and it points at Fidelity (M)

Black Diamond Cottonwood `fact_allocations` (silver `date=2026-10-16`, 948 accounts) has a column
`NFS Account Number`, which holds the **old Commonwealth account number**. Its `Account Number` column holds the
current Fidelity number.

| Measure | Value |
|---|---|
| BD accounts whose `NFS Account Number` exactly equals a Commonwealth account | **550** (one-to-one; IRPT_DASHBD's read found a floor of 563 over more partitions) |
| ...of which agree with the ADVI_COTBKF crosswalk | 423 of 423 where both have a pair; **0 conflicts** |
| ...that the crosswalk left NOT_MATCHED | **127** (79 no positions, 22 AMBIGUOUS, 19 no security positions, 7 AWAITING_PERSON) |
| crosswalk pairs with no NFS value in BD (positions-only match) | 40 |
| Commonwealth accounts linked by the union | **590 of 1,533** (crosswalk alone: 471) |
| custodian of all 550 key-linked accounts | **Fidelity IWS, 550 of 550**, current number prefix `658` |

So every stitchable Commonwealth account sits at Fidelity today. The link is Commonwealth NFS number ->
BD `NFS Account Number` -> the same row's `Account Number` (Fidelity). That is one static attribute, so a frozen
snapshot is enough; no daily BD dependency is needed to keep it.

**Correction to the holes report, section 2 item 4:** Anna Thiessen's Commonwealth numbers come from this field and end in
7492 and 7491. The `0QF879237/0QF879238` guess was wrong. Both accounts are Fidelity IWS.

The 22 AMBIGUOUS and 7 AWAITING_PERSON accounts linked here may shrink or retire the 107-pair ask to Cottonwood
(ADVI_COTBKF `COTTONWOOD_MATCH_PACKET_COVER_20261016.md`). This is (I) until the ADVI_COTBKF seat re-grades the packet against this key.

## 3. Fidelity coverage of Cottonwood (M, BD custodian field, 10-16)

| Custodian (BD) | Accounts | Share of BD market value |
|---|---|---|
| Fidelity IWS | 643 | **69.1%** |
| Schwab (+ Charles Schwab) | 24 | 14.5% |
| Manual / Investor Manual | 59 | 8.6% |
| Alternative Investment | 55 | 3.8% |
| American Funds, annuities, retirement plans, banks, other (about 25 names) | 167 | 4.0% |

Fidelity replaces Black Diamond for 643 of 948 accounts and about 69% of value. The Schwab slice ($81M) could come from
the existing Schwab feed if Cottonwood's Schwab master is entitled. The remaining ~16% (manual entries,
alternatives, direct-at-fund and held-away accounts) has no custodian feed and stays on BD (or the BD successor that
IRPT_CUSTDY names for 2027-01-01).

## 4. Shape of the Alongside Fidelity data (from dell1's walk, summarized; not re-measured here)

- **One file set per day for the whole Alongside book** (4,959 open accounts, $1.56B, domain ALONGSIDE, LLC). Custom CSV
  profile scheduled all 7 days from 2026-10-19: `account.txt` (141 cols), `position.txt` (62), `balance.txt` (43),
  `prices.txt` (44), `security.txt` (45), `transact.txt` (66). Business date is the first field (T-1); file names carry
  no date. Retrieval is two calls (status list, download); the export calendar keeps 120 days.
- **No performance in the files.** Fidelity's TWR, time-series and risk endpoints exist, but only per account as UI JSON.
  For 4,959 accounts that is a scraping job behind Akamai bot management. **Daily performance should be computed by Opal
  from positions + transactions + balances**, the way 49 Financial's working chain does from Schwab. Fidelity's TWR is
  used on a sample as a parity check.
- **Blocker to an unattended daily schedule:** login needs an SMS code each day (no remember-device step seen); the session lasts
  about 10 h. NFRA_FIDUPL owns it. Andrew authorized the automated sign-in (CTO record 190xZ). The firm split of the book is by
  G number, assessed on dell1.
- **Nothing has landed yet:** `s3://opal-data-assets/fidelity/` holds no objects, and `opal-data-alongside` does not exist (M).

## 5. Stitch comparison

| Factor | Stitch to Black Diamond | Stitch to Fidelity |
|---|---|---|
| Account key | same frozen key (section 2) | same key, one more column on the same row |
| The seam 2026-06-23 to 07-09 | **cannot be bridged**: BD allocations are empty 06-22 to 07-09 (IRPT_DASHBD r120), so first return is 07-10 | (H) bridgeable: an on-demand `transact.txt` / `.trn` export takes any date range (the standard one ran 05-26 to 10-16), and the in-kind receipt rows from the Commonwealth NFS account should date the seam and give opening positions. Test below. |
| Same plumbing as Commonwealth | no: BD re-labels into its own taxonomy and ids (z-ids) | yes (I): Commonwealth cleared through NFS, and Fidelity IWS is NFS (`.trn` broker field `NFSC`), so CUSIPs and transaction semantics should line up |
| Daily data quality | rolling 14-day re-exports duplicate flows; partial days; whole days re-sent 22-87 days late | one dated book-wide set per day, T-1; dedup rule still to be proven (H: does `transact.txt` carry a unique transaction id?) |
| Lifetime | BD is scheduled to be replaced by 2027-01-01 (IRPT_CUSTDY), so stitching to it is work that gets thrown away | the custodian of record; survives BD's retirement |
| Ready today | yes (with the reader fix) | no: nothing landed, SMS login unsolved, history before 10-19 needs on-demand exports |

## 5a. Test results from dell1 (4.0.0_SA_CRO~FIDELITY, `RESEARCH_20261019_PRFRPT_TESTS_FROM_DELL1.md` @abc6fcdbd7; relayed, not re-measured here)

- **Test 1 passed:** 639 of 643 BD Fidelity IWS accounts are in the Alongside `.naa`. The standard `.naa` never carries the
  Commonwealth number, so **the key stays BD's attribute, frozen once**. Whether the custom `account.txt` carries it is unmeasured.
- **Test 2, the seam is datable from Fidelity:** transfer comments on 145 accounts cluster in ISO weeks 26-28 (about 06-22 to 07-17).
  For **106 accounts** the comments name the Commonwealth number, which gives Fidelity its own key for part of the book. **But the
  flagged rows are cash journals ("CONVERSION TRANS:REORG ACTIVITY"), not security receipts.** So the opening positions are not
  given as in-kind rows. They have to come from the entitled `Historical Prices and Positions Export` as of about 06-23, or by
  rolling the current `.ipn` back through `.trn`. The second is the cheaper read and is still to be tested.
- **Test 3, partial:** the standard `.trn` has no transaction id, and 259 exact-duplicate rows (0.07%) cannot be told apart from
  genuine repeats. The custom `transact.txt` (66 columns) is still unseen. The first two scheduled daily files (from 10-20) will show
  whether days repeat. **Until those answer, a Fidelity reader must not union overlapping files**, which is the Black Diamond bug again.

The recommendation in section 1 stands. The new fact is that the seam's opening positions need one extra read, a
historical-positions export or a roll-back.

## 6. Tests that decide it (each one cheap; owners named)

1. **The Fidelity number joins:** the 643 BD `Fidelity IWS` account numbers against `FI101626.naa` / `account.txt` on
   dell1. Expect about 643 hits. Also check whether `account.txt` carries a prior or transfer-from account number, which would
   make the key Fidelity's own. Owner: 4.0.0_SA_CRO~FIDELITY (dell1), where the files are.
2. **The seam:** one on-demand transactions export over 2026-06-01 to 2026-07-15 for the 550 linked accounts. Are there in-kind
   receipt rows naming or matching the Commonwealth positions, and on which dates? Owner: the same, on Andrew's export click.
3. **Dedup:** does `transact.txt` (66 columns) have a unique transaction id, and does a daily file repeat earlier days?
   Owner: the same.
4. **Parity:** compute daily TWR from Fidelity files for about 20 accounts and compare with Fidelity's own
   `performance-measurement/returns` for the same accounts. Owner: IRPT_DASHBD once files land.
