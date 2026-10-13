# TO MDPF_DEMQUE.TO-DQ-t46 -- round 9 DQ-t-46: of the CARD-A P1 names, what Yahoo can price, what Black Diamond units and market value price exactly, and the residual Bloomberg-only set
<to_id>MDPF_DEMQUE.TO-DQ-t46</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~37</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>P1COVER</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-46` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 10) |
**outcome_ref:** C-QUOTE, C-PRIORITY, C-ONCE, FWD-4, FWD-6 | **depends_on:** DQ-t-43 (merged @b956c6307e)

---

## WORKER FACE

### THE CELL

CTO msg 4904 (Andrew-direct word: "I do not see us needing even more than 2 weeks of BBG daily quota if done correctly"): before ANY draw of the CARD-A P1
slice, read and print (1) how many of the P1 names Yahoo can price, (2) how many have Black Diamond positions with Units and market value on their held
dates, which gives an EXACT price (market value / units) with no vendor draw, and (3) the residual Bloomberg-only set and its cells. **This cell is a
measurement: NO vendor call (no Yahoo, no Bloomberg), no draw, no write to any store. It prints numbers and writes one JSON file.**

**Inputs you read** (read each first):
- The P1 slice: `data/mdpf/scripts/demque/card_a_slice.py` (merged; `--priority P1 --out PATH --quote` writes a request of `{cusip, start, end}` per priced name and
  prints `p1_names` 609, `priced_names` 607, the 2 FDIC placeholders unresolved, `cells`). Import and call its builder; do not copy its logic.
- Yahoo side: `price_store.index(price_store.s3_root())` (the landed names); `~/.opal/demque/unresolved.csv` (columns `cusip, symbol, reason, ...`: a name Yahoo
  was tried on and the lock rejected); every request file under `org/missions/D8/MDPF/MDPF_DEMQUE/requests/*.json` and the device queue
  `~/.opal/demque/queue/*.json` (a `securities` entry with `cusip` and `symbol` is a Yahoo symbol the queue knows).
- Black Diamond units and value, Cottonwood bucket `s3://opal-data-cot/` (S3 read only through the shim or boto3): `gold/canonical/holdings/YYYY-MM-DD.parquet`
  (daily files from 2026-04-22; read ONE file's schema first) and `silver/cot_holdings.parquet` (columns `market_value`, `units`, `cusip`, `symbol`, `ticker`,
  `account_id`, ...). List the prefixes `blackdiamond/`, `bronze/`, `forwardfill_v2/` and `silver/` for any other holdings-like table that carries units and
  market value per held date and reaches back before 2026-04-22; name every source you use with its date coverage, and use only a source whose rows carry
  BOTH units > 0 and market_value > 0 for a CUSIP on a date. Reference record of how the build values a fund from this snapshot:
  `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.md`.

**Build** `data/mdpf/scripts/demque/p1_coverage.py` (`--out PATH`) and a test file:
1. For each P1 PRICED name (607): classify into exactly ONE Yahoo class, in this order: `in_store` (its CUSIP is in the Yahoo price store index);
   `rejected` (it is in `unresolved.csv` with a REJECTED or FAILED reason); `symbol_known_untried` (a request or queue file carries a `symbol` for it and it is in
   neither of the first two); `no_symbol` (none of the above). The four sum to 607.
2. Black Diamond units and value: per CUSIP, the set of held dates (inside the name's own `[start, end]` window from the P1 request) on which some Black Diamond
   row has units > 0 and market_value > 0; the exact price of that date is the sum of market value over the sum of units across the rows of that CUSIP and
   date. Count `names` with at least one such date, `held_days` = the total (CUSIP, date) pairs, and list `sources`.
3. Residual: a name's NEEDED days = the trading days in its window (`lib/trading_calendar.trading_days_between`); a day is COVERED when the name is in the Yahoo
   `in_store` class (its stored `valid_from..valid_to` range) or a Black Diamond exact price exists for that day. `residual.cells` = the uncovered needed days
   (x 1 field PX_LAST) summed over names; `residual.names` = names with at least one uncovered day; `window_cells` = the P1 slice's total cells (882,024 at the
   merge, from `card_a_slice`).
4. Print ONE JSON line to stdout: `{"p1_names", "priced_names", "yahoo": {"in_store", "rejected", "symbol_known_untried", "no_symbol"}, "bd_units_value":
   {"names", "held_days", "sources": [...]}, "residual": {"names", "cells"}, "window_cells"}`. `--out` writes the same plus, per CUSIP, `{cusip, yahoo_class,
   bd_held_days, needed_days, uncovered_days}` in rank order. **CUSIPs and counts only: no account number or any key naming an account (client containment ruling
   @0e8209c33c).** Read account ids only to group; never print or write them.
5. NEW `test_demque_p1_coverage.py` (pytest; stub frames, no network, no S3) with exactly these names:
   `test_a_held_day_with_units_and_market_value_prices_exactly_at_value_over_units`,
   `test_the_three_classes_partition_the_priced_names_and_the_residual_counts_only_uncovered_days`,
   `test_the_coverage_output_carries_cusips_and_counts_and_never_an_account_key`.

### ACCEPTANCE

<criterion id="DQ9-t46-AC1" cell_refs="DQ-t-46"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t46_tests.py</invocation><expect>COVER-OK</expect></criterion>
<criterion id="DQ9-t46-AC2" cell_refs="DQ-t-46"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t46_real.py</invocation><expect>COVER-REAL-OK</expect></criterion>
`DQ9-t46-AC1` -- the three named tests. `DQ9-t46-AC2` -- on the REAL inputs: P1 609, priced 607, the four Yahoo classes sum to 607, the Black Diamond block names its
sources, the residual sits inside the window cells, and the written file has no account key. Report the whole folder `pytest data/mdpf/scripts/demque` once.

<expected_criteria>DQ9-t46-AC1,DQ9-t46-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `COVER-BAD no file ...`; `COVER-REAL-BAD no file data\mdpf\scripts\demque\p1_coverage.py`.


### AMENDED 2026-10-13 ~17:0xZ (issuer; no gate limb graded it, no new order added) -- rulings on rows D1-W37-S1 to S3, and the re-seated slot

Your first pass (commits `aa3b2100ee`, `9b43288850`, `e2366a6d56`) stands as inherited state. The grant now also names `card_a_slice.py` and its test. Rulings:
- **S3 (key name): the key is `blackdiamond_units_value`.** The naming gate is right; the check script's arm now reads that key (amended by the issuer). Nothing for you to rename.
- **S1 (CFNCASH): a name whose identifier is not 9 alphanumeric characters, or that starts with `FDIC`, is a cash identifier: UNRESOLVED, never priced, reason
  `cash_identifier`.** Put the rule in `card_a_slice.py` (so the P1 request never carries it) and cover it with a test in `test_demque_card_a_slice.py`; the
  expected P1 is 609 names, 606 priced, 3 unresolved (FDIC66606, FDIC66853, CFNCASH). Update the real check's expectations only where the issuer already did
  (priced 606).
- **Measure on the merged window.** DQ-t-44 merged @900406e221 (P1 window to the frontier, held rule on the Commonwealth sign table, 471,522 cells before this
  rule). MERGE `box/dell1` into your branch (a merge, never a rebase; the investigation file will conflict at its end because both sides append rows: keep every row of
  both sides, by id) and rerun `p1_coverage.py` so `window_cells` is the merged builder's own cell count, not 882,024.
- **S2:** stands (47 early gold files carry no cusip column; counted as read, not attributed).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO Yahoo call, NO Bloomberg call, no write to S3, the ledger, the queue or any pacer state, no AWS write, no deploy, no timer or background task.**
  The check's real arm has a 118 second limit: read the daily holdings files with one listing and bounded reads, and say in the report how many you read.
- **Account ids never enter a committed file or the output.**
- **Refusal clause.** If a criterion cannot be met as written (for example, no holdings source reaches the held dates, or the bucket read is refused), stop, write the
  reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W37-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or
  `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/p1_coverage.py
data/mdpf/scripts/demque/test_demque_p1_coverage.py
data/mdpf/scripts/demque/test_demque_card_a_slice.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-46`.
<owned_cells>DQ-t-46</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t46-AC1, DQ9-t46-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~37/MDPF_DEMQUE.TO-DQ-t46.p1-coverage-yahoo-black-diamond-residual.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t46-AC1,DQ9-t46-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the stdout line verbatim, the Black Diamond sources with their date coverage and how many files you read, the
residual by Yahoo class (counts), anything that stopped a count, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE a read of the Cottonwood bucket with the dell1 identity; no grant is requested or changed.
comp-adversary: DECLARED-NOT-APPLICABLE a read-only measurement; nothing is drawn, written or served.
risk: LOCAL -- code, tests and a printed measurement.
direct_act: false -- a worker order.
</preflight>

Source: CTO msg 4904 (Andrew-direct word); CARD-A P1 slice @b956c6307e; decomposition round 9.
