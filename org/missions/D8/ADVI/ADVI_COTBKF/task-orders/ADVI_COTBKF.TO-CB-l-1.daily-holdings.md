# TO ADVI_COTBKF.TO-CB-l-1 -- round 12 CB-l-1: daily holdings per account rebuilt from the transactions, checked against the snapshot

<to_id>ADVI_COTBKF.TO-CB-l-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~28</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-l-1` (`decompositions/ADVI_COTBKF_DECOMP.round12.md`) |
**outcome_ref:** FWD-3 (C-DAILY step 1) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-l-1`, FWD-3: an analyst will read each Cottonwood account's returns day by day back to 2013. Daily returns are derived, not delivered:
step 1 of four is **daily holdings** -- for every account, on every trading day of its history, the quantity held of each security,
rebuilt from the transactions. No price is involved in this step.

Inputs (read from S3 by `lib/opal_naming.address("commonwealth", <the cottonwood scope via opal_naming.lookup>, "silver", <table>,
"date=2026-06-23")`): `transactions` (1,416,497 rows, 1,533 accounts, 2013-04-03 to 2026-06-22; EVERY delivered record is a row -- two
identical lines are two real events, so never de-duplicate) and `positions` (one snapshot dated 2026-06-23: 469 rows, 83 accounts; columns
`AccountNumber`, `Cusip`, `Quantity`).

**Reuse, never copy:** `data/assets/scripts/silver/commonwealth_crosswalk.py` already holds the signed-quantity rules -- `SIGN` (transaction
type to +1/-1), `_signed`, `rebuild_holdings`, `position_holdings`, `rebuild_check` (tolerance `QTY_TOL`, 0.001) -- and its REBUILD-CHECK
already compares rebuilt END holdings with the snapshot. Import them. Your new work is the DAILY dimension.

Build `data/assets/scripts/silver/commonwealth_daily_holdings.py`, read-only, which:
1. For each account, from its first to its last trade date, on each NYSE trading day (`lib/trading_calendar.py`), carries the running
   signed quantity per security (cumulative sum of the day's signed quantities in trade-date order). Store only days and securities where
   the quantity is non-zero (a compact long table: account, date, cusip, quantity).
2. Compares each snapshot account's rebuilt quantity on 2026-06-23 (its last held state) with the snapshot, non-cash securities only, and
   writes EVERY difference as a row (account, cusip, rebuilt, snapshot, delta) to a differences file -- the CTO asked for them by account
   and security.
3. Writes `daily_holdings.parquet`, `snapshot_differences.csv` and a short `.md` to `--out`, and prints as its LAST line exactly:
   `DAILY-HOLDINGS accounts=<a> account_days=<d> holding_rows=<h> snapshot_accounts=83 snapshot_pairs=<p> snapshot_equal=<e> snapshot_diffs=<x>`.

**Tests** `data/assets/scripts/silver/tests/test_commonwealth_daily_holdings.py` (stubs, no AWS): a stub account with a buy, a partial sell,
a transfer in, a transfer out and two identical same-day buys rebuilds the expected quantity on each trading day (the identical pair counts
twice); dropping one transaction moves the result (the control); a stub snapshot with one mismatched pair prints `snapshot_diffs=1` and
writes that row.

### ACCEPTANCE

<criterion id="CB12l1-AC1" cell_refs="CB-l-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_daily_holdings.py</invocation><expect>passed</expect></criterion>
`CB12l1-AC1` -- the daily rebuild on stubs, with the dropped-transaction control and the repeat-pair arm.

<criterion id="CB12l1-AC2" cell_refs="CB-l-1"><invocation>python data/assets/scripts/silver/commonwealth_daily_holdings.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~28</invocation><expect>DAILY-HOLDINGS accounts=1533</expect></criterion>
`CB12l1-AC2` -- the real tables; account_days, holding_rows and the snapshot counts on the same line are recorded, not presumed, and every
difference is in the CSV.

<criterion id="CB12l1-AC3" cell_refs="CB-l-1" judgment="true"/>
`CB12l1-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: one account's daily holdings read across its span against its transactions.

<expected_criteria>CB12l1-AC1,CB12l1-AC2,CB12l1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only.** No S3 write, no vendor call, no download of any kind, no bun. The `daily_holdings.parquet` in your deliverables folder is
  a local output; if it exceeds 50 MB, keep it in `.scratch/` and commit only its row count and a sha256 in the `.md`.
- **Do not edit `commonwealth_crosswalk.py`** -- import from it.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W28-S<k>`, `"fabric": "dell2"`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_daily_holdings.py
data/assets/scripts/silver/tests/test_commonwealth_daily_holdings.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round12.md</decomp_doc> (round 12), cell `CB-l-1`.
<owned_cells>CB-l-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB12l1-AC1, CB12l1-AC2, CB12l1-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never
PASS or FAIL). Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~28/ADVI_COTBKF.TO-CB-l-1.daily-holdings.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB12l1-AC1,CB12l1-AC2,CB12l1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the DAILY-HOLDINGS line, the snapshot differences summarized (how many accounts and pairs, the largest five), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time build.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets; denominator 1 bucket; BLIND: none needed.
comp-adversary: RUN -- signed-quantity rules reused by import, never copied; C-SILVER repeats counted twice (tested); every snapshot difference written, not only counted; BLIND: corporate actions the transactions do not record.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-11 ADDENDUM 1 @e74f8eeb8e (msg 677); PRD C-DAILY (`prd/ADVI_COTBKF_PRD.md:113`); FWD-3.
