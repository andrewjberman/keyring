# TO ADVI_COTBKF.TO-CB-bx-2.price-paid -- round 76 CB-bx-2: the price-paid instrument over the whole table: the served close over amount per unit on every purchase and sale row of every fund, in four bands

<to_id>ADVI_COTBKF.TO-CB-bx-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~139</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bx-2` (`decompositions/ADVI_COTBKF_DECOMP.round76.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT on local copies. You change no code. Nothing is fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_76_20261011.md` sections 1, 2 and 3 item 2 ("The price paid on a trade reaches every fund that was ever bought or sold, in
every account, from the custodian's own rows and with no fetch"; "This is the first number that sizes the defect across all 377
holders."); the round-75 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~132/PURCHASE_DAY.json` (12 purchase days: the served close over the price paid has a median of 0.76 and is within
1 percent on 0 of 12; the unadjusted close on 12 of 12); the round-70 scan `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~113/CLOSE_VS_TRADE_SCAN_WIDE.json` and its `.md` (the close-against-trade scan
over every kind of security: its print admission and its classes; this cell is narrower in kind and wider in what it reports).

**The served close** is `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` (cusip, date, price, store): the close the served table
values a security at. **The custodian's rows** are `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/` (purchase type `by`, sale type `sl`; amount over quantity is the
price paid or received per unit). **The unadjusted vendor close** is `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` (per ticker: Close, Adj Close), read as it
sits. Nothing is fetched and no bucket is read.

**Your item.**

1. **The population, with every denominator printed:** the fund series in the served table (270: Mutual Fund and Mutual Fund (Closed
   End)); every purchase (`by`) and sale (`sl`) row of those funds in every account; of them the rows that carry BOTH an amount and a
   quantity (and a quantity large enough for its three decimals to carry a price: state the guard); of those the rows with a served
   close on the row's effective day (state the day convention and what is done on a non-trading day). Funds with at least one such
   row; distinct accounts as a COUNT.
2. **The control first:** on round 75's 12 purchase days you reproduce a median near 0.76 and 0 of 12 within 1 percent for the
   served close. If not, stop and say why.
3. **The instrument:** per row, the served close over amount per unit. Bands by the distance from 1: within 1 percent; 1 to 5; 5 to
   20; over 20. Over all rows, by kind of row (purchase, sale), by direction (the served close BELOW or ABOVE the price), and by
   year. The sale rows matter: a sale carries no front load, so a fee cannot explain a sale that is off.
4. **By group of fund:** the 19 moved in round 74; the 33 validated (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~128/VALIDATED_UNADJUSTED.csv`, reading `validated`); the 237 unreadable by
   reinvestment; and separately the 73 substituted with the unadjusted close (a control: they should be within 1 percent) against
   the 197 left on the store.
5. **By fund,** in a `.csv`: trade rows read, rows in each band, the median ratio, the first and last trade date, and the group.
   Counts and ratios only.
6. **What the instrument cannot see:** fund series with no purchase or sale row with a close (count them, by group), and holdings
   that arrived by transfer and were never traded.
7. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~139/PRICE_PAID.json`, the `.csv` (columns: cusip, ticker, group, substituted, trade_rows, within_1, b1_5, b5_20, over_20,
   median_ratio, first_trade, last_trade; CUSIPs only in the column named exactly `cusip`) and a short `.md`. Top-level keys,
   exactly: `population` (`{"fund_series", "trade_rows", "with_amount_and_quantity", "with_a_served_close", "funds_with_a_row",
   "accounts"}`), `control` (`{"days", "median", "within_1pct"}`), `bands` (`{"within_1", "b1_5", "b5_20", "over_20"}`), `by_kind`,
   `by_direction`, `by_year`, `by_group`, `not_reached` (`{"fund_series", "by_group"}`), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB76bx2-AC1" cell_refs="CB-bx-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~139/PRICE_PAID.json',encoding='utf-8'));p=d['population'];b=d['bands'];c=d['control'];print('PRICE-PAID control=%d/%d fund_series=%d trade_rows=%d with_amount_and_quantity=%d with_a_served_close=%d funds_with_a_row=%d accounts=%d within_1=%d b1_5=%d b5_20=%d over_20=%d band_sum=%d not_reached=%d'%(c['within_1pct'],c['days'],p['fund_series'],p['trade_rows'],p['with_amount_and_quantity'],p['with_a_served_close'],p['funds_with_a_row'],p['accounts'],b['within_1'],b['b1_5'],b['b5_20'],b['over_20'],b['within_1']+b['b1_5']+b['b5_20']+b['over_20'],d['not_reached']['fund_series']))"</invocation><expect>PRICE-PAID control=0/12 fund_series=270</expect></criterion>
`CB76bx2-AC1` -- the control reproduces; every denominator is printed; each trade row with a served close sits in one band
(`band_sum` equals `with_a_served_close`); the issuer reads the bands and the fund series not reached.

<criterion id="CB76bx2-AC2" cell_refs="CB-bx-2" judgment="true"/>
`CB76bx2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the denominators run from every trade row down to
the rows read, with what dropped at each step; the substituted funds are reported as a control whichever way they read; purchases
and sales are kept apart; the fund series the instrument cannot reach are counted; no account id or amount appears.

<expected_criteria>CB76bx2-AC1,CB76bx2-AC2</expected_criteria>

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
  `ADVI_COTBKF-D2-W139-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round76.md</decomp_doc> (round 76), cell `CB-bx-2`.
<owned_cells>CB-bx-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB76bx2-AC1, CB76bx2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~139/ADVI_COTBKF.TO-CB-bx-2.price-paid.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB76bx2-AC1,CB76bx2-AC2` BEFORE the flip. Mechanical: CB76bx2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the population with every denominator and what dropped at each step; the control on the 12 purchase days; the four bands over all rows, by kind, by direction and by year; by group of fund, the substituted control stated whichever way it reads; the fund series the instrument cannot reach, by group; the headline; the `PRICE-PAID` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- round 75's 12 purchase days are the positive control and must read 0 of 12; the funds already substituted with the unadjusted close are the negative control and are reported whichever way they read; purchases and sales are kept apart because a fee can explain one and not the other; the denominators run from every trade row to the rows read; BLIND: a fund held and never traded, and a row whose date is a day off its price.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-76 analysis @8ae9f87cf2 (msg 5996), section 3 item 2; `3.0.0_SA_CVO` round-75 grade file @0e95fc9cca.
