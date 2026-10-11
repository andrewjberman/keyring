# TO MDPF_DEMQUE.TO-DQ-t33 -- round 9 DQ-t-33: a re-quote prices the remaining cells, history is priced on trading days, and a completed request closes
<to_id>MDPF_DEMQUE.TO-DQ-t33</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~26</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-33` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-33` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` section 1 "Z-S2 and Z-S3" and round 7's R2: grade
against ONE quote frozen under the rule in force; a request whose every security reached its end date is CLOSED; rows `MDPF_DEMQUE-Z-S2`,
`MDPF_DEMQUE-Z-S3`). Two defects. (Z-S2) `bbg_quote.quote()` prices the FULL request from today's fire days and never subtracts cells already
drawn, so a mid-draw re-quote of the TR request reads 2026-10-18 against the frozen 2026-10-17: a reader sees a slip that is not one. (Z-S3) A
history request is priced on every weekday (1,310 per security, 15,720 cells for the TR request) while the vendor returns trading days (1,260
per security), so drawn is always below quoted: the request never closes and a fire after completion would append 0-cell lines.

**Build** (under `data/mdpf/scripts/demque/`; the site-Z drawer's own closing is the next order, DQ-t-34, and needs your `COMPLETE`):
1. `bbg_quote.py`:
   - A `history` request is priced on TRADING days: `cells` = trading days in `[start, end]` (`lib/trading_calendar.py` `trading_days_between`,
     the repo root on `sys.path` as `_calendar()` does) x fields x securities. `bql` stays on weekdays. A window the calendar cannot cover raises
     `ValueError` naming the calendar (a quote refuses; it never guesses). The `model_block` history component is unchanged.
   - `quote(request, allowance, drawn_today, today, producer_path=None, fire_days=None, drawn_to_date=0)`: `drawn_to_date` is the cells of THIS
     request already drawn up to and including `today`. The walk and finish date use `cells - drawn_to_date` (never below 0; when 0 remain,
     `finish_date` is None and `allowance_gap` is `"request fully drawn"`). Add
     `cells_remaining` and `label` to the output: `label` is `"remaining-cells quote: <drawn_to_date> of <cells> already drawn"` when
     `drawn_to_date` > 0 and `"full-request quote"` otherwise. `cells` still carries the FULL request.
   - CLI `--quote FILE --today D [--actuals PATH]`: with `--actuals`, `drawn_to_date` is the sum of `cells_drawn` over that file's lines whose
     `job` equals the request id and whose `date` <= `today`, and `drawn_today` is the sum of `cells_drawn` of every `channel` history line
     dated `today`; without it both are 0 as today.
   - `record_actual(...)`: `outcome` may also be `"COMPLETE"` (no `stop_reason` needed); `--outcome` gains `COMPLETE`.
2. `quote_vs_actual.py`: a line of the request with outcome `COMPLETE` sets `drawn_date` to its date (even when the cells never reach the
   quoted figure) and the verdict is `ON_TIME` / `LATE` against the finish date as for a covered request; otherwise unchanged. `--all` still must
   not read a superseded file.
3. `refreeze.py`: a re-freeze of a quote that already carries `supersedes` is allowed when the `reason` differs from the one it carries (the same
   reason and `as_of` stays `ALREADY_REFROZEN`): the current `<id>.quote.json` is copied to the next free `<id>.quote.superseded-<date>[-n].json`
   (with `superseded_reason`, `superseded_on`, `superseded_by`), the earlier superseded files are never touched, and the new quote's `supersedes`
   names the file just written. `quote_vs_actual` already prints every superseded file.
4. `test_demque_bbg.py`: any assertion that counted weekdays for a HISTORY request over a week with an NYSE holiday is amended to the trading-day
   count; no other assertion changes. Every other `test_demque_*.py` keeps passing unedited (run the folder with
   `pytest data/mdpf/scripts/demque`; it collects now) and a failure outside your paths is a surprise row, not an edit.
5. NEW `test_demque_quote_remaining.py` (pytest; `tmp_path`, no network) with exactly these names:
   `test_requote_of_a_partly_drawn_request_prices_the_remaining_cells` (a 1,000-cell request, ceiling 100, 400 drawn to date: finish moves
   earlier by the cells drawn; the label names the 400),
   `test_history_cells_are_priced_on_trading_days` (a request over a week containing 2026-11-26 counts 4 days, not 5),
   `test_complete_row_closes_the_request_and_sets_the_drawn_date` and
   `test_refreeze_chains_a_second_superseded_quote` (three quotes in the chain; the first superseded file is byte-identical afterwards).

### ACCEPTANCE

<criterion id="DQ9-t33-AC1" cell_refs="DQ-t-33"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t33_tests.py</invocation><expect>QR-OK</expect></criterion>
<criterion id="DQ9-t33-AC2" cell_refs="DQ-t-33"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t33_real.py</invocation><expect>QR-REAL-OK</expect></criterion>
`DQ9-t33-AC1` -- the four named tests. `DQ9-t33-AC2` -- the REAL TR request in scratch copies: re-quoted at 2026-10-11 with the ledger through that
day it prices the full request on trading days, reports `cells_remaining` = cells minus 11,716 drawn, finishes 2026-10-17 and carries the label;
a chained re-freeze writes a second superseded file and `quote_vs_actual` prints both superseded finishes (OPEN).

<expected_criteria>DQ9-t33-AC1,DQ9-t33-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `QR-BAD no file ...`; `bbg_quote.py: error: unrecognized arguments: --actuals ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **You never write the real requests folder or the real ledger.** Tests and AC2 use scratch copies; the real re-freeze is the issuer's act.
- **No AWS write, no Bloomberg call, no deploy.**
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W26-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/quote_vs_actual.py
data/mdpf/scripts/demque/refreeze.py
data/mdpf/scripts/demque/test_demque_bbg.py
data/mdpf/scripts/demque/test_demque_quote_remaining.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-33`.
<owned_cells>DQ-t-33</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t33-AC1, DQ9-t33-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~26/MDPF_DEMQUE.TO-DQ-t33.remaining-cells-trading-days-complete.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t33-AC1,DQ9-t33-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the re-quote line verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL quote and record tools over scratch files.
risk: LOCAL -- code, tests and records.
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis @92a9b27704 section 1 (Z-S2, Z-S3) and round 7 R2; rows Z-S2, Z-S3 (REMEDIATION_v7); decomposition round 9.
