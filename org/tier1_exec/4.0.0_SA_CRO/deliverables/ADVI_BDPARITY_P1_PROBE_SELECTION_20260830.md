# ADVI_BDPARITY P1-PROBE -- rider-4 PROBE-ACCOUNT SELECTION (the C3 deliverable of 2.0.0_SA_COO 84206)

**Seat:** `4.0.0_SA_CRO` (base) | **Clock:** 2026-08-30T02:1xZ (read) | **Authority:** `2.0.0_SA_COO` 84206 on
`3.0.0_SA_CVO` verdict D2-T70-1 -- SELECTION ONLY (C1). The two methodology cells (SI anchor = BD
funding-inception with admissibility; basis = CUMULATIVE) are FROZEN INPUT @`f11fb765ad` + annotation 1
@`3fc9752c58` + annotation 2 @`30d51fcbac`; **nothing in this file rules, remarks on, or re-opens them.**
No PERFRP-subject content (C2 of 84206). No vendor call was made and none is made by this file.

**Inputs, read at source:** candidates table `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/
ADVI_BDPARITY_P1_COHORT_CANDIDATES_20260829.md` @`da93bcacfc` (selection read) and @`b29b9f849b` (the
annotation carrying the all-535 sweep); the P1-PROBE face `:15-20, :34` + issuer amendment A2/A3; the
convention pre-registration `org/tier1_exec/1.0.0_SA_CTO/deliverables/
ADVI_49F_PARITY_CONVENTION_PREREGISTRATION_20260819.md` @`c7bfcb2917` (rider 4, A1 C5, A3 item 4, A5);
the TaxSMA roster `s3://opal-data-assets/blackdiamond/49f/_ops/taxsma_roster.json` (5 entries, 3 active);
`0.4.0_DS_ClientPlatform~C` 84281 (535/535-partition first-appearance sweep); `3.0.0_SA_CVO` 84210, 84354.

---

## 1. THE SELECTION -- five accounts

Accounts are named by Schwab account id (the `twr_daily.account_id` space) and `bd_internal_id` (tier-1
xref, `dim_account_xref date=2026-08-28`, 6,201 rows; all five resolve `seed-xref`, `in_0833_universe=True`).
Window attributes: `twr_daily` 37 partitions 2026-07-01..2026-08-28; positions `canonical_positions
date=2026-08-28`; external events `flow_ledger` same window. **Denominators in section 5.**

| # | account | bd_internal_id / bd_account_id | PICKED FOR (attribute) | recency source | fee_days | flow_days (twr) / EXTERNAL ledger | n_pos | rate_bearing / rb_share | mv_total | days_ok/36 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `0022312917` | 13477111 / z0813477111 | **C5 income-bearing fixed-income specimen** (pre-registered A3 item 4; corroborated by a second instrument, table s.2) | n/a (not the recency member) | 2 | 0 / 0 | 2 | 1 / 0.8982 | 790,249.11 | 36 |
| 2 | `0038836097` | 18927251 / z0818927251 | **C3 multi-security + fixed income** AND the **FLOWS** member (4 EXTERNAL flow days) | n/a | 2 | 4 / 4 | 80 | 1 (+1 NULL) / 0.0694 | 22,913,948.45 | 36 |
| 3 | `0010083855` | 21089351 / z0821089351 | **C2 fee-bearing off-quarter, NO flows, ZERO rate-bearing** (the clean fee-timing specimen: no C3-FI or C5 confound) | n/a | 2 | 0 / 0 | 15 | 0 / 0.0000 | 172,732.71 | 36 |
| 4 | `0027265115` | **22596361** / z0822596361 | **INCEPTION-RECENT (REQUIRED member) -- the only account with a KNOWN BD inception PRE-PULL** | **MEASURED: BD-returned SI start 2026-03-16** (bronze, 84141); ours first-linkable 2026-03-17 (84281, 535/535); **ADMISSIBLE, zero truncation** (CVO annotation 2, 84354) | 1 | 1 / 1 (-0.79, 2026-07-01) | 362 | 0 / 0.0000 | 1,012,411.57 | 36 |
| 5 | `0076459710` | **23221671** / z0823221671 | **INCEPTION-RECENT (most recent on our plane)** + in-kind external event (P2-5 in-kind class exercised) | **MEASURED: first present 2026-07-01, first linkable 2026-07-09, 37 days** (84281, 535/535); roster trade_start 2026-08-05 (NOT an inception -- 84281); BD inception UNKNOWN until the pull returns it | 1 | 0 / 2 (both `signed_amount=0.0`, `is_in_kind=True`, 2026-07-29) | 325 | 0 / 0.0000 | 1,256,691.02 | 31 (4 UNCOMPUTABLE-ZERO-BMV + 1 NO-PRIOR-BALANCE-ACCOUNT-ABSENT at the open) |

**One-line rationale per account**
1. `0022312917` -- the C5 class is 38 accounts of 6,185 (table s.1); this one is already REGISTERED as the
   C5 specimen (A3 item 4, largest accrual $22.47K) and independently corroborated on composition (rb_share
   0.8982). Kept over the alternate `0079954642` on purpose -- see section 3(a).
2. `0038836097` -- 80 positions is the largest per-security decomposition in the table (C3's classifier is
   per-security concentration), it holds fixed income (rate-bearing MV $1.59M), and it is the only
   candidate with real EXTERNAL flows in-window (4 days), so it carries the flows axis without a sixth
   account.
3. `0010083855` -- fee events on 2 days, no flows, no rate-bearing holdings: a C2 sawtooth here has no C3/C5
   competitor. **Its C2 TEST is graded UNAVAILABLE until the corrected gross leg reaches the history**
   (C02-g-3; CVO 84210 s.3) -- selection stands, the cell waits; its r_net cells are unaffected.
4. `0027265115` (bd 22596361) -- the only account in the population whose SI anchor is known before any
   vendor call, so the SI limb of the frozen ruling is DECIDABLE at P1 rather than deferred to returned
   anchors; admissibility already ruled ADMISSIBLE on the first-linkable reading with the BMV-0 rule
   (84354). Present 121 days; a real (tiny) external flow in-window.
5. `0076459710` (bd 23221671) -- the most inception-recent account with a MEASURED recency (first present
   2026-07-01, 37 days) and a live TaxSMA roster member (bd id resolved tier-3 under Andrew's account-api
   word, 2026-08-27). Its BD inception is the returned-anchor case the ruling's two-pass SI design exists
   for. It also carries the P2-5 in-kind class (two zero-value in-kind EXTERNAL rows).

---

## 2. AXIS COVERAGE (what rider 4 / the 08-19 amendment / 84206 C3 asked for, and where each lands)

| axis | covered by | status |
|---|---|---|
| fee-bearing | #1 #2 #3 #4 #5 (fee_days 2/2/2/1/1) | COVERED |
| **non-fee** | -- | **NOT COVERED at P1 -- deliberate; section 3(c); named alternate in section 4** |
| flows | #2 (4 EXTERNAL days), #4 (1) | COVERED |
| no-flows | #1 #3 #5 (twr flow_days 0) | COVERED |
| inception-recent (REQUIRED, measured recency) | #4 (BD inception 2026-03-16, measured) and #5 (first present 2026-07-01, measured 535/535) | COVERED, twice, by different recency sources |
| income-bearing fixed income (C5, 08-19 amendment) | #1 (rb_share 0.8982) | COVERED |
| C2 fee-bearing off-quarter (rider 4) | #3 (and #1, #2 as fee-bearing) | COVERED; test UNAVAILABLE until gross-leg re-emission |
| C3 multi-security with fixed income (rider 4) | #2 (80 positions, FI present) | COVERED |
| C4 Mitch-Johnson-case account (rider 4, "if in the 49F population") | -- | **NOT IDENTIFIABLE from our gold** (table s.5 bound 1); needs the 49F-side contact. Not selected; not silently dropped. |
| SI limb of the frozen ruling: prediction "SI parity testable only on inception-recent accounts" | #4 (anchor known, ADMISSIBLE) and #5 (anchor returned by the pull) | the prediction is FALSIFIABLE with this cohort; without #4/#5 P2-1's SI denominator reads 0-of-N by construction (84206 C3) |

---

## 3. THE THREE JUDGMENT CALLS, stated so they can be rejected

**(a) C5 specimen: `0022312917` KEPT; `0079954642` NOT substituted.** The table's argument for the
alternate (20 rate-bearing positions -> an accrual delta decomposes across holdings) is a real property,
but it cuts the other way for SIGNATURE SEPARATION, which is what rider 4 selects for: C3's signature is
per-security and sign-mixed, C5's is uniform-positive and (per A5) EXACT-form against qt1 `Accrual`. A
21-position, 20-bond account is precisely where C3 and C5 can be confused; a 2-position account with one
bond is where they cannot. The registered specimen is also a pre-registration commitment (rider 5:
amendments are addenda, never edits) and now carries two non-shared-input corroborations. The alternate
stays ranked first for P2, where decomposition across holdings is the point.

**(b) TWO inception-recent members, not one.** They are different tests. #4's anchor is KNOWN, so its SI
cell decides admissibility NOW and exercises annotation 2's BMV-0 rule on the one account it was stated
from. #5's anchor is RETURNED, so it exercises the two-pass design (pass 1 the pull, pass 2 offline
linking) on an account whose first-present date on our side (2026-07-01) predicts a BD inception; if BD
returns an inception EARLIER than our first linkable (2026-07-09), the cell must read
`UNAVAILABLE-NO-COVERAGE` -- that is the ruling's prediction landing as a measured outcome, not a
defect. One member cannot exercise both branches.

**(c) NON-FEE deliberately not covered at P1.** The cap is five; the binding axes are C5 (38 of 6,185
accounts) and measured inception-recency (3 accounts in the whole population have one). A non-fee account
is the C2 NEGATIVE control (gross == net identically), and the C2 test itself is UNAVAILABLE at P1 until
the gross leg is re-emitted -- a control for a cell that cannot run buys nothing at P1. Non-fee accounts
are 1,248 of 7,441 in-window and are covered by P2 by construction. **If the issuer wants the axis at P1
anyway, the swap rule is in section 4 and costs no re-measurement.**

---

## 4. RANKED ALTERNATES and the swap rules (all measured, all zero-egress, all `seed-xref` resolvable)

| rank | account | bd_internal_id | role | measured attributes | swap rule |
|---|---|---|---|---|---|
| A1 | `0035153269` | 12887581 (z0812887581) | **NON-FEE / NO-FLOW** control | fee_days 0, flow_days 0, days_ok 36, 19 positions, rb 0, mv $184,007.29 -- the median-MV member of the 9 accounts meeting (non-fee AND no-flow AND days_ok 36 AND rb 0 AND >=5 positions AND MV 100K-2M); the unfiltered non-fee/no-flow/days_ok-36 class is 101 | swap IN for #3 if non-fee is wanted at P1 (the C2 test is unavailable at P1 either way) |
| A2 | `0079954642` | 14052861 | C5 alternate (20 rate-bearing positions, rb_share 0.9402) | table s.3 | swap IN for #1 only on a ruling that decomposition-across-holdings outranks signature separation at P1; FIRST pick for a P2 C5 sub-cohort |
| A3 | `0084073310` | 22659431 | inception-recent alternate | first present 2026-03-13, first linkable 2026-03-20, 112 days (84281); fee_days 1; two zero-value in-kind EXTERNAL rows 2026-07-29; 324 positions, rb 0, mv $978,837.68 | swap IN for #5 if a longer linkable history is preferred over recency |

Withheld and NOT ranked: `0099965452`, `0065688849`, `0097064646` -- present in `twr_daily`, absent from
`canonical_positions` on 08-28 (table s.3); cohort membership is UNKNOWN, not zero.

---

## 5. MEASUREMENTS BEHIND THE TABLE (denominators, controls, instruments)

- **Window attribute read:** 37 of 37 `twr_daily` partitions 2026-07-01..2026-08-28 (535 in history),
  columns `account_id, business_date, r_net, r_gross, status, bmv, cf_net, cf_gross`; `fee_day` =
  `cf_gross != cf_net`, `flow_day` = `cf_net != 0`, `days_ok` = `r_net` non-null. **POSITIVE CONTROL: the
  three table rows re-read with these definitions reproduce the table exactly -- `0022312917` (2/0/36),
  `0038836097` (2/4/36), `0010083855` (2/0/36), 3 of 3.** So the roster accounts' attributes are on the
  table's own definitions, not a look-alike.
- **Positions:** `canonical_positions date=2026-08-28`, 103,351 rows, 6,185 accounts (matches the table's
  denominator). `0038836097` carries one `rate_bearing` NULL row (an unknown, counted as neither).
- **External events:** `flow_ledger` window, `final_class == EXTERNAL`, joined per (account,
  business_date) to `twr_daily`. The roster accounts' EXTERNAL rows are `signed_amount 0.0, is_in_kind
  True` (2026-07-29, two each on `0076459710` / `0084073310`) and one `-0.79` (2026-07-01,
  `0027265115`); that is why twr `flow_days` reads 0 while the ledger reads 2 -- an in-kind zero-value
  event is not a cash flow. Attribute, not defect.
- **Population denominators (this read, same window):** accounts in `twr_daily` 7,441; fee-bearing 6,193;
  NON-fee 1,248; flow-bearing 1,510; no-flows 5,931 -- **identical to table s.4, re-derived, same
  instrument class (pyarrow over the same parquet), different code path.** Rate-bearing 38 of 6,185 (table
  s.1, not re-derived here).
- **Recency:** NOT re-derived here. Cited: `0.4.0_DS_ClientPlatform~C` 84281 / annotation @`b29b9f849b`
  (535/535 partitions, 156s) for first-present / first-linkable; 84141 for the BD-returned SI start
  2026-03-16 with BMV 0.0; `3.0.0_SA_CVO` 84354 for the admissibility verdict. Roster `trade_start_date`
  (2026-04-08 / 2026-08-05 / 2026-08-05) is printed only to show it is NOT the recency source.
- **Instrument note (a second reading of a known partition):** `twr_daily date=2026-08-18` carries only
  10 of the 14 columns -- `bmv`, `cf_net`, `cf_gross`, `emv` are ABSENT from its schema, not null-typed.
  DS~C's BP1-4 @`fa82a129d8` recorded `r_net`/`r_gross` as `null`-typed on that date; this read adds that
  four cash/valuation columns are missing outright. Read schema-tolerantly; one line to the surprise
  channel, not chased.

---

## 6. WHAT THIS FILE DOES NOT DO

- It does not answer table s.6 items 1-2, 83415 items 1-2, or 84281's admissibility question -- all
  FROZEN / ruled by `3.0.0_SA_CVO` (@`f11fb765ad`, @`3fc9752c58`, @`30d51fcbac`). Any future
  methodology remark from this seat is a P3-3 proposal through `1.0.0_SA_CTO`'s convention gate.
- It fires nothing. The pull is `0.4.0_DS_ClientPlatform~C`'s, within Andrew's 21:23Z scope (ruled
  QTD/YTD/1Y/SI, 3-5 accounts, no schedule, `ytd_mode="custom"`), on GATE 1 (vendor egress, Andrew).
- It is graded on C3 by `3.0.0_SA_CVO` regardless of who made it (84206 C4). If Andrew answers D2-T69-R2
  YES, this seat is released and the file stays as the record of a selection made under the face's
  routing.

## 7. SURPRISE CHANNEL (OBSERVATION, INERT -- one line each, to `3.0.0_SA_CVO` cc issuer; nothing chased)

1. `twr_daily date=2026-08-18` schema is 10 columns, missing `bmv/emv/cf_net/cf_gross` entirely (section 5).
2. `dim_account_xref date=2026-08-28`: `account_is_open` is NULL for `0027265115` (the other five picks read True).
3. `canonical_positions date=2026-08-28`: `0038836097` carries one `rate_bearing` NULL position (of 80).
