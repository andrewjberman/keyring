# TO MDPF_DEMQUE.TO-DQ-t50 -- round 9 DQ-t-50: surface B1 -- the Cottonwood client history request at option C depth, on the client-income basis
<to_id>MDPF_DEMQUE.TO-DQ-t50</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~42</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>B1REQUEST</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-50` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 14) |
**outcome_ref:** C-QUOTE, C-PRIORITY, C-PRICES, FWD-4, FWD-6 | **depends_on:** DQ-t-43, DQ-t-44, DQ-t-46 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-13 ("Go with your rec"; CTO msg 4964; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`, the section "Go with your rec" and the standing
rules above it; read it). **Surface B1, the Cottonwood client history, is ONE Bloomberg request at option C depth:**
1. **Depth:** the dates money moved (a name's own transaction dates, moved to the next trading day when they fall on a non-trading day) plus month-ends, **daily from 2026-04-22**
   (where Black Diamond has data); the floor is `max(first held date, 2012-01-01)`; the window end is the merged P1 builder's (frontier when held, last trade when not).
2. **Basis:** `PX_LAST` for every priced name, with the client's own recorded income (the dated interest and dividend rows in the transactions) supplying the distributions; the 11
   long-held Fixed Income names with no income row in their window ALSO get `TOT_RETURN_INDEX_GROSS_DVDS` (2,492 cells, 0.9 day, `2.0.0_SA_COO~Q1` @3be5467b33).
3. **$1.00 money market funds skip Bloomberg:** each cash equivalent is checked against its fund type; a fund whose price is fixed at $1.00 is priced at $1.00 with that reason on
   the value and is NOT pulled; a name whose fund type is UNREAD is pulled.
4. **The 8 mutual funds Yahoo rejected JOIN B1:** ABNFX, AGTHX, BALCX, MEIIX, NFFFX, PRILX, VEIRX, VGHAX, from their first held date (the 15-fund fill starts 2020-07-06, so a window
   starts on the later of that date and the fund's first trade), at the same depth, on the same basis.

**This cell BUILDS the request and prices it. It makes NO vendor call and draws nothing (the draw waits on Andrew's form: surfaces E, C and D are still open).**

**Build** (NEW `data/mdpf/scripts/demque/b1_request.py` and edits to `bbg_quote.py`; read `card_a_slice.py` (`build`, `trade_windows`, the merged windows and the cash-identifier
rule), `p1_coverage.py`, `bbg_quote.py` `_validate` / `quote`, `rank.py` `load_transactions`, `lock.py` `_load_transactions` (it carries `Asset_Type`), and the held snapshot `s3://opal-data-cot/silver/cot_holdings.parquet`
(columns `cusip`, `asset_name`, `asset_display_name`, `cash_equivalent`) first; import, do not copy):
1. **`bbg_quote.py`: two entry shapes (backward compatible; existing tests pass unedited).** A history `securities` entry may carry `"dates": ["YYYY-MM-DD", ...]` (cells = the entry's
   trading-day dates inside `[window_start, request end]` x its fields; a non-trading date or a date before 2012-01-01 is a loud `ValueError` naming the cusip) and/or
   `"fields": [...]` overriding the request's fields for that entry (cells = days x len(its fields)). The need-class rule applies to every date.
2. **`b1_request.py --build --out PATH`** (S3 read only): the 606 priced P1 names from `card_a_slice.build("P1", ...)` (priced = after the cash-identifier rule). For each name: entries =
   (a) one `{"cusip", "dates": [...]}` entry of the flow dates and month-ends strictly before 2026-04-22 (inside its window), and (b) one `{"cusip", "start": max(window start, 2026-04-22),
   "end": window end}` daily entry when its window reaches 2026-04-22. The 11 names with no income row in their window (Fixed Income, held over 365 days, from the transactions) carry
   `"fields": ["PX_LAST", "TOT_RETURN_INDEX_GROSS_DVDS"]` on their entries.
   - **$1.00 skip:** for names with `Asset_Type` `Cash Equivalent`, read the held snapshot's name text and `cash_equivalent` flag; a name whose text contains `MONEY MARKET` (case blind) and
     whose flag is true is SKIPPED into the request's `"skipped"` list as `{"cusip", "price": 1.0, "reason": "money market fund priced at $1.00"}`; every other cash equivalent, including a
     CUSIP absent from the snapshot (UNREAD), is pulled. Count and print both.
   - **The 8 funds:** their CUSIPs and symbols come from `requests/ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012.json` (the 8 symbols above); their entries carry `"symbol"` as well, start no
     earlier than 2020-07-06 and no earlier than their first trade, and use the same sampling and basis.
   - The request: `{"request_id": "MDPF_SECHIST-CARD-A-B1-OPTION-C", "channel": "history", "vendor": "bloomberg", "tier": 2, "need_class": "client", "window_start": <earliest start>, "page":
     "client performance (Cottonwood), via MDPF_SECHIST's one series per security", "fields": ["PX_LAST"], "securities": [...], "skipped": [...]}`, CUSIPs, symbols (funds only) and dates only,
     no account number, deterministic (two runs byte-identical), valid under `bbg_quote._validate`.
   - Prints ONE JSON line `{"securities", "priced_names", "skipped_one_dollar", "unread_pulled", "total_return_names", "funds_joined", "cells", "days_to_finish", "finish_date", "claim",
     "window_start"}`; `cells`, `days_to_finish`, `finish_date` and `claim` come from `bbg_quote.quote` with today's history allowance (the CLI's own read), as `card_a_slice --quote` does.
3. NEW `test_demque_b1_request.py` (pytest; stub frames, no network, no S3) with exactly these names:
   `test_option_c_dates_are_flow_dates_and_month_ends_before_2026_04_22_and_every_trading_day_after_with_the_2012_floor`,
   `test_a_security_with_a_total_return_override_prices_two_fields_and_a_dates_entry_prices_its_trading_days_only`,
   `test_a_fixed_one_dollar_money_market_fund_is_skipped_with_its_reason_and_an_unread_type_is_pulled`.

### ACCEPTANCE

<criterion id="DQ9-t50-AC1" cell_refs="DQ-t-50"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t50_tests.py</invocation><expect>B1-OK</expect></criterion>
<criterion id="DQ9-t50-AC2" cell_refs="DQ-t-50"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t50_real.py</invocation><expect>B1-REAL-OK</expect></criterion>
`DQ9-t50-AC1` -- the three named tests. `DQ9-t50-AC2` -- on the REAL inputs: 606 priced, the 11 total-return names, the 8 funds joined from 2020-07-06 on, the cells between 15,000
and 45,000, a request that validates, is deterministic and carries no account key. The real check allows 55 seconds a run: read the transactions once. Report the whole folder
`pytest data/mdpf/scripts/demque` once.

<expected_criteria>DQ9-t50-AC1,DQ9-t50-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `B1-BAD no file ...`; `B1-REAL-BAD no file ...b1_request.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO Yahoo call, NO Bloomberg call, no write to S3, the ledger, the queue or any pacer state, no AWS write, no deploy, no timer.** `standing_drawer.py --apply` is never run.
- **Account ids never enter a committed file or the output** (read them only to group by CUSIP).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W42-S<k>`, `fabric` `dell1`, `surfaced_at` =
  `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY. Merge `box/dell1` into your branch (a merge,
  never a rebase) before you append rows.

<paths>
data/mdpf/scripts/demque/b1_request.py
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/test_demque_b1_request.py
data/mdpf/scripts/demque/test_demque_bbg.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit; the committed B1 request file and its quote are the issuer's to write on your report.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-50`.
<owned_cells>DQ-t-50</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t50-AC1, DQ9-t50-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~42/MDPF_DEMQUE.TO-DQ-t50.b1-cottonwood-depth-option-c-request.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t50-AC1,DQ9-t50-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--build` line verbatim, the skipped list's count and how each skip was decided (the text rule), UNREAD names pulled, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE a read of the Cottonwood bucket with the dell1 identity; no grant is requested or changed.
comp-adversary: DECLARED-NOT-APPLICABLE a request builder and its pricing; nothing is drawn or served.
risk: LOCAL -- code, tests and a priced request. The draw is a site-Z act under the queue's budget and the Terminal sign-in (Andrew's), after his form is complete.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-13 "Go with your rec" via CTO msg 4964; P1 depth cuts @86abd8733d; income rows @54a77c0e82; decomposition round 9.
