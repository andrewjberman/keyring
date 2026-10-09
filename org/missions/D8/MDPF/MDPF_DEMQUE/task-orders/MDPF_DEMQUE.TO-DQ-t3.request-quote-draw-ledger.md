# TO MDPF_DEMQUE.TO-DQ-t3 -- round 1 DQ-t-3: a history request is priced in cells, drawn in priority order, and recorded on the ledger
<to_id>MDPF_DEMQUE.TO-DQ-t3</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~2</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `DQ-t-3` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-1 | **depends_on:** `MDPF_DEMQUE.TO-DQ-t2` (same slot; draws through its `pull()` and `Pacer`)

---

## WORKER FACE

### THE CELL

`DQ-t-3`, hop 4 of the FWD-1 thread: someone asks for history; the queue says what it costs in cells and the day it will finish before
anything runs, draws it in priority order without a person, and records what it actually drew beside the quote.

**Build** NEW `data/mdpf/scripts/demque/demand_queue.py` (it imports `yahoo_pull` from the same folder, built by your previous order) with:

1. A request is a JSON file: `request_id, tier (int 1-5), reason, page, securities [{cusip, symbol}], fields ["close"], start (YYYY-MM-DD),
   end (YYYY-MM-DD)`. Tiers are Andrew's order: 1 production daily pulls (incl. ETF Positioning); 2 current clients and new-client
   onboarding; 3 Rival Funds history; 4 research pages; 5 former clients.
2. `quote(request, queue_ahead_requests: int, daily_cap: int, today) -> dict` with `cells` (`{"yahoo": n}`; a cell is one row times one
   field: weekdays in `[start, end]` times `len(fields)`, summed over securities), `requests` (one per security), `finish_date` (the
   weekday on which this request's last security is drawn, counting `queue_ahead_requests` first at `daily_cap` per weekday from `today`).
3. `draw(queue_dir, ledger_path, pacer, today, fetch=None) -> list[dict]`: reads every request JSON in `queue_dir` not yet drawn, orders
   them by `tier` ascending then file order, pulls each security through `yahoo_pull.run`/`pull` under the given `Pacer`, and appends ONE
   ledger row per request to `ledger_path` (JSON lines): `date, vendor "yahoo", channel "history", job (request_id), page, cells_quoted,
   cells_drawn, outcome` (`DRAWN` / `PARTIAL` / `FAILED` / `DEFERRED` when the pacer stops). A failed security contributes 0 cells. A
   request is marked drawn only when all its securities are `OK`.
4. CLI `python demand_queue.py --quote FILE` prints the quote as one JSON line.
5. NEW `data/mdpf/scripts/demque/test_demque_queue.py` (pytest, stubbed fetch, `sleep` no-op, temp dirs) with exactly these names:
   `test_quote_counts_cells_as_rows_times_fields`, `test_quote_finish_date_from_daily_cap_and_queue_ahead`,
   `test_draw_takes_lower_tier_number_first`, `test_draw_writes_one_ledger_row_per_request_with_quote_beside_actual`,
   `test_failure_is_a_ledger_row_with_zero_cells`.

**And the ledger's home (CLAUDE.md rule 30):** every S3 address is `lib/opal_naming.py address()` output, and today
`address("yahoo", ...)` REFUSES ("source 'yahoo' is not a systems.json key"). A refusal is a missing registry row: add ONE row to the
`systems` list in `infra/logic/registry/systems.json`, following the existing `commonwealth` VENDOR row's shape exactly (read it; every
field it has), with `key` `yahoo`, `class` `VENDOR`, `long` `yahoo-finance`, owner directive `D8`, and an `owner_basis` citing
`org/missions/D8/MDPF/MDPF_DEMQUE/` and Andrew-direct record @489e1cd24c. Note: `yfinance` is a REFUSED generic noun in that file -- the
system key is `yahoo`. Edit nothing else in the file. This round writes the ledger locally; S3 upload is a later round.

### ACCEPTANCE

<criterion id="DQ1-t3-AC1" cell_refs="DQ-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t3_tests.py</invocation><expect>QUEUE-OK</expect></criterion>
<criterion id="DQ1-t3-AC2" cell_refs="DQ-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t3_home.py</invocation><expect>HOME-OK</expect></criterion>
`DQ1-t3-AC1` -- quote, ranked draw and ledger row, by the five named tests. `DQ1-t3-AC2` -- the builder names the Yahoo ledger home after
your registry row; its bloomberg control arm resolves on both sides.

<expected_criteria>DQ1-t3-AC1,DQ1-t3-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base: `QUEUE-BAD no file ...`, `HOME-BAD yahoo refused: ... (control ok: ...)`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call, no vendor call (tests stub the fetch), no deploy.**
- **You arm no timer, background task or OS task** -- scheduling the draw is the issuer's act.
- **Refusal clause.** If a criterion cannot be met as written (for example a registry gate refuses the row), stop, write the reason in your
  report and a surprise row (id `MDPF_DEMQUE-W2-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or
  `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/demand_queue.py
data/mdpf/scripts/demque/test_demque_queue.py
infra/logic/registry/systems.json
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 1, the thread), cell `DQ-t-3`.
<owned_cells>DQ-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ1-t3-AC1, DQ1-t3-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~2/MDPF_DEMQUE.TO-DQ-t3.request-quote-draw-ledger.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ1-t3-AC1,DQ1-t3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed (the daily draw's schedule is the issuer's drain act, read then).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE thread round.
risk: WORLD -- the L6 gate floors it there: <paths> names infra/logic/registry/systems.json (an infrastructure path). The cell writes code, tests and one registry row; no AWS or vendor write.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.2 FWD-1, FWD-4, C-CELL, C-QUOTE, C-PRIORITY, C-HOMES (open item 4); decomposition round 1.
