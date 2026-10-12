# TO ADVI_COTBKF.TO-CB-bx-1.purchase-rows-off -- round 76 CB-bx-1: the 26 percent: the purchase rows that miss the unadjusted close, each given a cause from a closed list written first, under two orders

<to_id>ADVI_COTBKF.TO-CB-bx-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~138</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bx-1` (`decompositions/ADVI_COTBKF_DECOMP.round76.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT on local copies. You change no code. Nothing is fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_76_20261011.md` sections 1, 3 item 1 and 4 ("The 26 percent, first, because it bounds everything after it"; "It is not
written before the 26 percent has causes: a rule that a quarter of the rows contradict is not a rule yet."); the round-75 record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~132/PURCHASE_DAY.json` and its `.md`, key `cash_against_shares` (over all accounts, 936 purchase rows of the 19 moved funds with a close: the
unadjusted close over the price paid has a median of 0.997 and 73.7 percent within 1 percent; 183 more purchase rows have no close
on the row's day).

**The served close** is `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` (cusip, date, price, store): the close the served table
values a security at. **The custodian's rows** are `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/` (purchase type `by`, sale type `sl`; amount over quantity is the
price paid or received per unit). **The unadjusted vendor close** is `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` (per ticker: Close, Adj Close), read as it
sits. Nothing is fetched and no bucket is read.

**Your item.**

1. **Reproduce first:** the 1,119 purchase rows of the 19 funds, the 936 with an unadjusted close on the row's effective day, the
   share within 1 percent (73.7), and so the count that is off. State the day convention exactly as round 75 had it.
2. **THE CLOSED LIST FIRST.** Before any off row is looked at, write to a file in your scratch (with a clock timestamp) and copy
   into the record: the causes, the TEST for each, the ORDER they are tried in (a row takes the first that fits), and ONE ALTERNATIVE
   ORDER you will also run. From the analysis: `fee_inside_amount` (a sales charge or fee: the price paid sits ABOVE the close by a
   share that is one of a small set of load rates, or the same account and fund show a constant excess; state the test without
   reading it off the rows); `prior_day_close` and `next_day_close` (the price paid equals, within 1 percent, the close of the
   previous or the next trading day); `reinvestment_or_exchange_recorded_as_purchase` (the same account has a distribution,
   reinvestment or exchange row in that fund or its sibling within a stated window, or the row's own codes say so); `another_share_class`
   (the price paid equals, within 1 percent, the close that day of a different share class of the same fund on disk);
   `none_found`. You may add causes with tests ONLY in this file, before you start (for instance: a price paid equal to the ADJUSTED
   close; a quantity too small for its three decimals to carry the price). Then keep it.
3. **Each off row given its cause,** under the stated order and under the alternative: counts per cause both ways, and how many rows
   change cause with the order. Per cause: the median of close over price paid, and how many funds and accounts (as COUNTS) it
   spreads over. `none_found` with its count and what was looked at.
4. **What it bounds.** After the causes that are NOT a wrong close (a fee, a neighbouring day, a different instrument) are set
   aside, the share of purchase rows on which the unadjusted close reproduces the price paid; and the same for the SALE rows of
   the 19 funds (a sale carries no front load), stated beside it as a check.
5. **The rows with no close that day (183):** why (before the cache window; a non-trading day; no bar), counts.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~138/PURCHASE_ROWS_OFF.json` and a short `.md`. Top-level keys, exactly: `reproduced` (`{"purchase_rows", "with_a_close",
   "within_1pct", "off"}`), `closed_list` (`{"text", "written_at", "causes", "order", "alternative_order"}`), `causes` (an object:
   cause to `{"rows", "median_ratio", "funds", "accounts"}`), `alternative` (the same object under the other order),
   `rows_that_change_cause_with_the_order`, `none_found`, `fit_after_benign_causes` (`{"purchases", "sales"}`), `no_close_that_day`,
   `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB76bx1-AC1" cell_refs="CB-bx-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~138/PURCHASE_ROWS_OFF.json',encoding='utf-8'));r=d['reproduced'];c=d['causes'];a=d['alternative'];print('PURCHASE-ROWS-OFF list_written=%s reproduced=%d/%d/%d off=%d given=%d given_alt=%d none_found=%d change_with_order=%d by_cause=%s'%(bool(d['closed_list']['written_at']),r['purchase_rows'],r['with_a_close'],r['within_1pct'],r['off'],sum(v['rows'] for v in c.values()),sum(v['rows'] for v in a.values()),c.get('none_found',{}).get('rows',0),d['rows_that_change_cause_with_the_order'],json.dumps({k:v['rows'] for k,v in c.items()},sort_keys=True)))"</invocation><expect>PURCHASE-ROWS-OFF list_written=True reproduced=1119/936</expect></criterion>
`CB76bx1-AC1` -- the closed list was written first; round 75's rows are reproduced; every off row carries a cause under the stated
order and under the alternative (`given` and `given_alt` equal `off`); the issuer reads how many change with the order.

<criterion id="CB76bx1-AC2" cell_refs="CB-bx-1" judgment="true"/>
`CB76bx1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the list, its tests and both orders precede the look
and were not widened after; a fee is named by a test stated beforehand and not read off the rows; `none_found` is used where no
test fits; the sale rows are reported as they came out; no account id or amount appears.

<expected_criteria>CB76bx1-AC1,CB76bx1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local: no S3 read, no network call.
- **Accounts.** Inside your own scratch you work with account ids as the tables hold them. NOTHING you commit, print in your report
  or write to the channel carries an account id, or an account's value, flow, quantity, balance, amount or return. Counts, ratios,
  basis points without an account, tickers and dates only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W138-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round76.md</decomp_doc> (round 76), cell `CB-bx-1`.
<owned_cells>CB-bx-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB76bx1-AC1, CB76bx1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~138/ADVI_COTBKF.TO-CB-bx-1.purchase-rows-off.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB76bx1-AC1,CB76bx1-AC2` BEFORE the flip. Mechanical: CB76bx1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** round 75's rows as reproduced, with the day convention; the closed list, its tests, its order and the alternative order as written before the look, with the timestamp; the off rows by cause under each order, with the median ratio and the spread per cause; how many change cause with the order; `none_found` with its count and what was looked at; the fit after the benign causes, for purchases and for sales; the rows with no close that day and why; the headline; the `PURCHASE-ROWS-OFF` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the list, each test and both orders are written before any off row is looked at; a fee is named by a test stated beforehand; the alternative order is run because order decided nine days last round, and the rows that change are counted; sales, which carry no front load, are the check on the fee cause; none-found is a legal answer; BLIND: a fee schedule is not on disk, so a fee is inferred from the shape of the excess and never read from a document.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-76 analysis @8ae9f87cf2 (msg 5996), section 3 item 1; `3.0.0_SA_CVO` round-75 grade file @0e95fc9cca.
