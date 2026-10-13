# L4-R review, ADVI_BDPRCE PRD v1.0, ratified-text half -- REFUSE, one ground (3.0.0_SA_CVO, dell1, 2026-10-13 ~12:5xZ)

**Delivery:** `1.0.0_SA_CTO~DELL1` msgs 4809 and 4810 (pin f9627a75e2), re-pinned on msg 4815: FWD-6 was edited before this stamp.
**Bytes reviewed:** `org/missions/D8/ADVI/ADVI_BDPRCE/prd/ADVI_BDPRCE_PRD.md` @4d158f4c40, equal to HEAD.
- ratified-text half_hash 572b4c811e06125617b2fc7628d182505766de742c86778c0392c2c2147798d7.
- The f9627a75e2 hash 619490f42681 is stale.
**Read whole:** the header, ENDPOINT, CONTRACTS and THE DECISIONS (DEC-6, DEC-7) at HEAD, plus:
- brief PART VIII at f2171cae6c (and at 18cbc90139 and f5256ca81e);
- `ENDPOINT_FORWARD_ADVI_BDPRCE_20261013.md` at HEAD;
- Andrew's records `ANDREW_DIRECT_20261013_121xZ_*` and `ANDREW_DIRECT_20261013_122xZ_CAPPED_LOTS_*`;
- CRO msg 4813.

## Verdict: REFUSE -- one ground, cheap to cure

**Ground: FWD-3's DONE WHEN names a value the PRD does not hold.**
- FWD-3 reads: "for a sample spanning every price source (override, trade median, interpolation, vendor) ... the sample size is set in the PRD".
- The PRD sets no sample size. `grep -n -i sample` over the file returns only that line (:48-49) and :146, which is unrelated (the exec-summary slots).
- With no size stated, the outcome cannot be graded as written: a one-row-per-source sample would pass it.
- Cure: state the size in the PRD (a DEC, brief half, is fine, since the ENDPOINT line already points there). Give a minimum per price source and the total, how the rows are drawn (seeded random, or every row of a named date), and which T-1 object. Nothing else needs to change.

## What holds (read and checked, not grounds)

1. **Andrew's four DONE WHEN lines are carried, and were not changed after he confirmed them.** Brief PART VIII lines 1-4 are byte-identical at 18cbc90139
   (before his ~12:1xZ "Yes as written"), at f5256ca81e and at f2171cae6c. Each maps to one outcome, by its SOURCE line:
   - line 1 "a rule written down in one place" -> FWD-2;
   - line 2 "trace any served price to that rule and its inputs" -> FWD-3;
   - line 3 "moved under a fix Andrew saw before it moved" -> FWD-7;
   - line 4 "on the basis Andrew chose for capped lots" -> FWD-8.
   FWD-2, FWD-3, FWD-7 and FWD-8 are measurable renderings of those four lines, and none narrows its line.
2. **The PRD's ENDPOINT block is byte-equal to the endpoint record at HEAD** (4,807 bytes each, compared programmatically).
3. **FWD-6's edit (4d158f4c40) is not a change to Andrew's confirmed text.** FWD-6 comes from O4, not from PART VIII.
   - Old: "the reading (instant or strict) is RULED at L4 ... each served reader keys on that reading".
   - New: "each served reader keys on trade_date, not the transactions file day (DEC-6)".
   - DEC-6 is defined in THE DECISIONS (:133). It rules trade date from FWD-6's own ACCEPT ("built from the trades OF THAT DATE") and names the three readers.
   - CRO msg 4813 says instant and strict were FB-h-7's measurement windows, not keying choices. One correction: the brief's own PART V item 6 lists "trade date,
     the strict day after, or the instant reading" as choices. Either way, the new line is the decided form, and it removes a DONE WHEN that waited on a ruling.
4. **The no-estimation constraint and the capped-lots ruling are carried.**
   - FWD-8: a capped lot's value and gain read UNVERIFIED, "never an estimate", until FWD-9.
   - The lot record contract: `market_value` and `accrued_gain` are absent, with the status, never scaled.
   - The account totals contract: totals stay BD's own account value, never a sum of lots. That matches "Account totals stay exact" (~12:2xZ).
   - FWD-9: FIFO-only lots read UNVERIFIED, and "no served lot's units or cost is a reconstruction".
5. **NO FWD IS A WAIT.** FWD-7 is the one wait, and it is qualified: its reason, its discharging act (Andrew's review of each fix's named diff), per fix,
   with no other FWD waiting on it. Andrew's word for it is line 3 itself. FWD-9 rests on an act a seat can take (the template switch, cell 1, reversible).
6. **Rule 30.** The one new address, `unrealized_lots`, is builder output. This seat ran `lib/opal_naming.py address("blackdiamond", "49financial", "silver",
   "unrealized_lots", "date=YYYY-MM-DD")` and got `s3://opal-data-assets/blackdiamond/49financial/silver/unrealized_lots/date=YYYY-MM-DD`, equal to the PRD.
   The template's S3 path is an existing object, not a new name.
7. **CONTRACTS have no counterpart PRD to contradict.** comp-find for `silver/unrealized|unrealized_lots|exec.summary|capped` over the ADVI_FIRMBKTS and MDPF_SECCLASS PRD
   folders returns 1 hit across 6 files, and it is unrelated (MDPF_SECCLASS's three-year lookback). The consumers named (B_01, account-level readers, IRPT and
   the BD Mix in DEC-7) are code and other projects' readers, carried in FWD-7's blast radius.

## Carried notes (not grounds; for the re-sign)

- **Estimated prices in the precedence.** The price-rule contract keeps `linear_interpolation` (rank 2) and `carry_forward` (rank 3) as served price sources. Andrew's
  words ("any 'estimation' is highly risky for performance reporting that needs to be exact") were said about capped lots, and both records apply them there.
  They read on interpolated and carried prices too. Those prices are traceable under FWD-3, but the PRD does not say whether a reader sees that a price is interpolated
  or carried. One DEC line would close it: say whether the source label is served on the row, or put the question to Andrew.
- **Status figures inside DONE WHEN lines.** FWD-4 ("830 of 5,366 asset-days moved at measurement") and FWD-8 ("64,629 capped lots (13 pct, at measurement)") carry
  measurements that age. They are context, not criteria; a grade reads the live count.

-- 3.0.0_SA_CVO

## ADDENDUM 1 (2026-10-13 ~13:0xZ) -- SIGN: the ground is cured

**Delivery:** `1.0.0_SA_CTO~DELL1` msg 4818. **Bytes reviewed:** the PRD @96028a9e53, equal to HEAD.
- ratified-text half_hash d5ab58f8d868fa4e76e0b2a79efe160c3c55a2020d78335e8e38f8ec6ca0373b.
- The refused hash 572b4c811e06 is superseded.
- `git diff 4d158f4c40 HEAD` on the PRD, read whole, has two hunks and nothing else. ENDPOINT and CONTRACTS are otherwise unchanged:
  1. FWD-3's DONE WHEN tail "the sample size is set in the PRD" became "the sample is set in DEC-10".
  2. DEC-10 was added in THE DECISIONS (brief half).

**The cure holds.**
- DEC-10 makes FWD-3 gradeable:
  - five dates (the latest frontier and four earlier trading dates, each read from `lib/trading_calendar.py`, so a weekend never counts);
  - at least 30 per price source (override, trade median, interpolation, vendor), with all of a source taken and the shortfall printed if it has fewer;
  - at least 150 in total;
  - a deterministic draw (rows ordered by `sha256(asset_id|date|"ADVI_BDPRCE-FWD3")`, so any seat reproduces it);
  - plus every price of the FWD-1 thread.
- The pass rule fits Andrew's "estimation is highly risky": 100 pct, every recompute equal to the cent, and a miss keeps FWD-3 NOT REALIZED.
- Andrew's confirmed line is unchanged. PART VIII line 2 reads the same at f2171cae6c and at HEAD: "an analyst can trace any served price to that rule and
  its inputs". FWD-3's change only points to where the sample is set. That is a cure, not a re-word.

**Note, not a ground: the endpoint record and the PRD now differ by a few words in that pointer.**
- The endpoint record reads "the sample is set in the PRD (DEC-10)"; the PRD reads "the sample is set in DEC-10".
- The meaning and the referent are the same, so this is a wording drift and not a change of substance. Make the two match byte for byte.

**Carried forward from the review (not grounds):** whether a reader sees that a price is interpolated or carried forward, and the status figures that age inside
the FWD-4 and FWD-8 lines.

-- 3.0.0_SA_CVO
