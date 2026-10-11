# TO ADVI_COTBKF.TO-CB-bx-4.trade-day-return -- round 76 CB-bx-4: the return on trade days across every account: measured account-days whose return changes by over 10 basis points when a trade is valued at what was paid

<to_id>ADVI_COTBKF.TO-CB-bx-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~141</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bx-4` (`decompositions/ADVI_COTBKF_DECOMP.round76.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT on local copies, by arithmetic on the served table. You change no code, build nothing, fetch nothing.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_76_20261011.md` sections 1, 2 and 3 item 4 ("The return, on trade days only, across every account: the account-days whose
daily return changes by more than 10 basis points when a trade is valued at what was paid; counts by band. No account id leaves the
worker's folder."); the round-75 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~132/PURCHASE_DAY.json` and its `.md` (the build's return formula; the shares-bought term; the 12
purchase days, on which that term is the whole change on two days of about 882 basis points and 75 to 76 percent of it on ten).

**The served close** is `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` (cusip, date, price, store): the close the served table
values a security at. **The custodian's rows** are `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/` (purchase type `by`, sale type `sl`; amount over quantity is the
price paid or received per unit). **The unadjusted vendor close** is `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` (per ticker: Close, Adj Close), read as it
sits. Nothing is fetched and no bucket is read. **The served returns** are `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` (account, date, value, flow, return,
blank_reason) with `account_day_value.parquet` beside them.

**Your item.**

1. **The quantity, stated before it is computed** (write it to a file in your scratch with a clock timestamp, and copy it into the
   record): under the build's formula a day's return is the day's value less its flow, over the value at the account's previous
   row. Valuing a trade at what was paid changes the day's value by the cash of the trade less the traded shares at the served
   close (for a sale, the other way round), and nothing else. So the change in that day's return is that difference over the
   previous value. State the formula in symbols, the sign for a sale, what is done when several funds trade in one account-day,
   and the floor below which a change is not counted. This is the TRADE term only: the holding carried at the served close is NOT
   revalued, and you say so in the headline.
2. **The control first:** on round 75's 12 purchase days your trade term reproduces that round's shares-bought term (within a stated
   tolerance, and against the unadjusted close there: say how the two differ in definition). If not, stop and say why.
3. **The population, with every denominator:** account-days with a purchase or sale row of a fund series (270) carrying an amount
   and a quantity and a served close; of those the account-days MEASURED in the served table (a return present on that day and a
   value at the previous row); distinct accounts as a COUNT at each step. The table is about 94 percent blank: say how many trade
   account-days fall on a blank day, by blank reason.
4. **The number:** measured trade account-days whose return changes by more than 10 basis points; bands: 10 to 50, 50 to 200, over
   200; the sign; by kind of row; by year; and by the row's price fit (the served close within 1 percent of the price paid; 1 to 5;
   5 to 20; over 20), so a change that comes from a fee-sized gap is told from one that comes from a quarter of the price. The
   largest change in basis points, with its date and fund and no account. The count of accounts and of funds the changes sit in.
5. **And on the blank days,** as a count only: the trade account-days on which the same term would exceed 10 basis points if the
   day were measured (the previous value present), so the reader sees what a wider measured set would hold.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~141/TRADE_DAY_RETURN.json` and a short `.md`; a `.csv` by fund (columns: cusip, ticker, trade_account_days, measured, over_10bp;
   CUSIPs only in the column named exactly `cusip`). Top-level keys, exactly: `quantity` (`{"text", "written_at", "floor"}`),
   `control` (`{"days", "reproduced"}`), `population` (`{"trade_account_days", "measured", "blank", "accounts",
   "accounts_measured"}`), `changed_over_10bp`, `bands` (`{"b10_50", "b50_200", "over_200"}`), `by_sign`, `by_kind`, `by_year`,
   `by_price_fit`, `largest_bp`, `accounts_changed`, `funds_changed`, `on_blank_days_if_measured`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB76bx4-AC1" cell_refs="CB-bx-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~141/TRADE_DAY_RETURN.json',encoding='utf-8'));c=d['control'];p=d['population'];b=d['bands'];print('TRADE-DAY-RETURN quantity_written=%s control=%d/%d trade_account_days=%d measured=%d blank=%d accounts=%d accounts_measured=%d changed_over_10bp=%d b10_50=%d b50_200=%d over_200=%d band_sum=%d accounts_changed=%d funds_changed=%d'%(bool(d['quantity']['written_at']),c['reproduced'],c['days'],p['trade_account_days'],p['measured'],p['blank'],p['accounts'],p['accounts_measured'],d['changed_over_10bp'],b['b10_50'],b['b50_200'],b['over_200'],b['b10_50']+b['b50_200']+b['over_200'],d['accounts_changed'],d['funds_changed']))"</invocation><expect>TRADE-DAY-RETURN quantity_written=True control=12/12</expect></criterion>
`CB76bx4-AC1` -- the quantity was written first; the control reproduces on 12 of 12; the measured trade account-days that change by
more than 10 basis points are counted in three bands (`band_sum` equals `changed_over_10bp`).

<criterion id="CB76bx4-AC2" cell_refs="CB-bx-4" judgment="true"/>
`CB76bx4-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the quantity is the trade term alone and is stated
as such, with the carried holding left out by name; the control is run before the count; the changes are split by the row's price
fit so a fee-sized gap is not read as the defect; the blank days are counted apart and not added; no account id or amount appears.

<expected_criteria>CB76bx4-AC1,CB76bx4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local: no S3 read, no network call, no build of the chain.
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
  `ADVI_COTBKF-D2-W141-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round76.md</decomp_doc> (round 76), cell `CB-bx-4`.
<owned_cells>CB-bx-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB76bx4-AC1, CB76bx4-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~141/ADVI_COTBKF.TO-CB-bx-4.trade-day-return.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB76bx4-AC1,CB76bx4-AC2` BEFORE the flip. Mechanical: CB76bx4-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the quantity as written before it was computed, with its timestamp; the control on the 12 purchase days and how its definition differs from round 75's term; the population with every denominator and the blank days by reason; the measured trade account-days over 10 basis points, in three bands, by sign, kind, year and price fit; the largest change; the accounts and funds as counts; what the blank days would hold, apart; the headline, saying it is the trade term only; the `TRADE-DAY-RETURN` line; the account-id scan's DENOMINATOR line; a statement that no account id or amount left the scratch; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the quantity is written before it is computed and is the trade term alone, the carried holding left out by name; round 75's 12 purchase days are the control; every change is split by the row's price fit, so a fee-sized gap is told from a quarter of the price; blank days are counted apart and never added; BLIND: a trade whose cash and shares sit on different days, and an account-day with no previous value.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-76 analysis @8ae9f87cf2 (msg 5996), section 3 item 4; `3.0.0_SA_CVO` round-75 grade file @0e95fc9cca.
