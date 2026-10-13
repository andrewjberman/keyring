# TO MDPF_DEMQUE.TO-DQ-t43 -- round 9 DQ-t-43: the Bloomberg client-history need priced per security's own window, P1 living-client names first
<to_id>MDPF_DEMQUE.TO-DQ-t43</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~35</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>CARDASLICE</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-43` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 8) |
**outcome_ref:** C-QUOTE, C-PRIORITY, C-RESERVE, FWD-4, FWD-9 | **depends_on:** DQ-t-25 (merged)

---

## WORKER FACE

### THE CELL

`DQ-t-43` (CTO ruling msg 4875, 2026-10-13: "(1) Cut the per-security window cell: each name's own held window, so no cells outside it. (2) The P1
living-client slice goes first, then former clients last. (3) It takes only what that priority already gives current clients from today's
history allowance; no new spend. Print the P1 count, its cells and its days-to-finish before the first draw."). The Bloomberg client-history need
(request `MDPF_SECHIST-CARD-A-COT-BBG-HISTORY`, 1,319 securities) cannot be queued as filed: it lists its securities by a CSV pointer, and
`bbg_quote.quote` prices ONE date window per request while the need is a window per security. This cell makes the quote price each
security's own window and builds the P1 slice as a request the queue can price. **It makes NO Bloomberg call and arms nothing: a request file, a
quote, and the numbers.**

**Build** (read `data/mdpf/scripts/demque/bbg_quote.py` `quote` / `_validate` / `_trading_days`, `rank.py` `rank` / `load_crosswalk` /
`load_transactions`, and `org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.quote.json` first):
1. **Per-security windows in `bbg_quote.quote`.** A history request's `securities` entry may be a string (the request's own `start` / `end`, as
   today) OR a dict `{"cusip": ..., "start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}` carrying its own window. Cells = the sum over securities of
   (trading days inside that security's window) x fields. Every existing request shape keeps its exact old cells; the existing
   `test_demque_bbg.py` tests pass unedited. A dict entry with `end` before `start`, or a missing key, is a loud `ValueError` naming the cusip.
2. **`card_a_slice.py`** (NEW; `--priority P1 --out PATH [--quote]`):
   - The security set = the `ranked` list of the CARD-A quote file above (1,319 CUSIPs). The priority of each = `rank.rank(...)` over
     `load_crosswalk()` and `load_transactions()` (S3 read only), the same rule `rank.py --probe` uses. Keep the names of the requested priority,
     in rank order (score descending).
   - A name's window: `start` = the LATER of its first transaction `Trade_Date` in the silver transactions and the card's floor 2013-04-03
     (so never before 2013-04-03); `end` = 2026-06-23 (the need's end date). Nothing outside it.
   - A name is UNRESOLVED, never quoted, when it has no transaction in the need window, or its CUSIP is not a Bloomberg-priceable security (the two
     FDIC cash-sweep placeholders `FDIC66606` and `FDIC66853` are the known cases: a CUSIP shaped `FDIC` + digits). Each is listed with a one-word
     `reason`.
   - `--out` writes the request: `{"request_id": "MDPF_SECHIST-CARD-A-P1-SLICE", "channel": "history", "vendor": "bloomberg", "tier": 2,
     "page": "client performance (Cottonwood), via MDPF_SECHIST's one series per security", "fields": ["PX_LAST"], "securities": [{"cusip",
     "start", "end"}, ...]}` in rank order, CUSIPs and dates ONLY. It carries NO account number or account-derived field: client account ids
     never enter the repo (CTO containment ruling @0e8209c33c).
   - `--quote` prints ONE JSON line to stdout: `{"priority", "p1_names", "priced_names", "unresolved_names", "cells", "days_to_finish",
     "finish_date", "claim", "window_end", "unresolved": [{"cusip", "reason"}]}`. `cells`, `finish_date` and `claim` come from
     `bbg_quote.quote` on the written request with today's history allowance (the CLI's own allowance read, held claim stays held);
     `days_to_finish` = the whole number of trading days from today to `finish_date`.
3. NEW `test_demque_card_a_slice.py` (pytest; stub crosswalk and transactions frames, no network, no S3) with exactly these names:
   `test_a_security_carries_its_own_window_and_the_quote_sums_trading_days_inside_it`,
   `test_the_p1_slice_lists_priced_names_in_rank_order_and_every_window_ends_on_the_need_end_date`,
   `test_a_p1_name_with_no_trades_or_no_bloomberg_cusip_is_listed_unresolved_and_never_quoted`.

### ACCEPTANCE

<criterion id="DQ9-t43-AC1" cell_refs="DQ-t-43"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t43_tests.py</invocation><expect>SLICE-OK</expect></criterion>
<criterion id="DQ9-t43-AC2" cell_refs="DQ-t-43"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t43_real.py</invocation><expect>SLICE-REAL-OK</expect></criterion>
`DQ9-t43-AC1` -- the three named tests. `DQ9-t43-AC2` -- on the REAL silver transactions (S3 read only): the P1 slice has 500 to 700 names, priced
plus unresolved equals P1, both FDIC placeholders unresolved, every window ends 2026-06-23, a positive cell count and days-to-finish, and no
account key in the written request. Report the whole folder `pytest data/mdpf/scripts/demque` once (148 passed at the t-42 merge, plus these 3).

<expected_criteria>DQ9-t43-AC1,DQ9-t43-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `SLICE-BAD no file ...`; `SLICE-REAL-BAD no file data\mdpf\scripts\demque\card_a_slice.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: no Bloomberg call, no write to S3, the ledger, the queue or any pacer state, no AWS write, no deploy, no timer or background task.**
  The one file you write outside tests is the request at the `--out` path you are given.
- **Account ids never enter a committed file.** Print and commit CUSIPs, dates and counts only.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W35-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/card_a_slice.py
data/mdpf/scripts/demque/test_demque_card_a_slice.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The committed P1 request file is the issuer's to write on your report.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-43`.
<owned_cells>DQ-t-43</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t43-AC1, DQ9-t43-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~35/MDPF_DEMQUE.TO-DQ-t43.card-a-p1-slice-per-security-windows.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t43-AC1,DQ9-t43-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--quote` line verbatim (unresolved trimmed to the first 3 plus the count), how a first trade date maps
to `start`, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a quote and a request builder; nothing is drawn or served.
risk: LOCAL -- code, tests and a priced request. The draw itself is a site-Z act under the queue's budget and the Terminal sign-in (Andrew's).
direct_act: false -- a worker order.
</preflight>

Source: CTO msg 4875 (2026-10-13); CARD-A quote @2026-10-09; CTO containment ruling @0e8209c33c; decomposition round 9.
