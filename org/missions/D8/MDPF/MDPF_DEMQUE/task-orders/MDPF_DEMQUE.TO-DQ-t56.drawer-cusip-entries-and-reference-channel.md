# TO MDPF_DEMQUE.TO-DQ-t56 -- round 9 DQ-t-56: the site Z drawer draws CUSIP entries with per-entry dates and fields, and the reference channel, so B1, the porting test and the fund-type check all draw through the one queue
<to_id>MDPF_DEMQUE.TO-DQ-t56</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~48</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>DRAWERENTRIES</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-56` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 19) |
**outcome_ref:** C-QUOTE, C-PRIORITY, C-SITES, FWD-3, FWD-4 | **depends_on:** DQ-t-44, DQ-t-50, DQ-t-52, DQ-t-54 (merged)

---

## WORKER FACE

### THE CELL

CTO msg 5174 (the queue form is complete and the draw hold is lifted): **one drawer, one queue; Bloomberg only through it.** The standing drawer (`data/mdpf/scripts/demque/standing_drawer.py`) draws only
requests whose every security carries a `bloomberg` ticker and a start-to-end window, on the `history` channel. The issuer measured that it returns ONE open request today (the TR comparison). The
requests Andrew has just approved are NOT drawable by it:
- **B1** (`MDPF_SECHIST-CARD-A-B1-OPTION-C`, 613 CUSIPs, 803 entries): each entry carries a `cusip`, most carry a `dates` list (sparse flow dates and month-ends), some carry a per-entry `fields`
  override, and none carries a ticker.
- **The porting test** (`MDPF_SECHIST-CARD-A-PORTING-TEST`, 326 CUSIPs, 3,195 single-day entries) carries a `cusip` and a one-day window per entry.
- **The fund-type check** (`MDPF_SECHIST-CARD-A-B1-FUND-TYPE`, 227 CUSIPs x `FUND_TYP`) is a `reference`-channel request; the drawer draws `history` only.
This cell teaches the drawer all three. **It makes NO Bloomberg call (tests use a stub client) and arms nothing.**

**Build** (read `standing_drawer.py` in full, `bbg_quote.py` `_own_window` / `_validate` / the `dates` and per-entry `fields` handling merged in t-50, `priority_gate.py`,
`integrations/bloomberg/mcp/blp_client.py` `reference_data` / `historical_data`, and the three request files above; import, do not copy):
1. **Identifier.** `bloomberg_id(security) -> (identifier, form)`: the entry's `bloomberg` ticker when present (form `"ticker"`), else `"/cusip/<CUSIP>"` (form `"/cusip/"`). `_is_drawable` accepts an entry that has either.
   Because the `/cusip/` form is the issuer's reading of the Bloomberg API and is UNVERIFIED on the site client, **the first draw of any `/cusip/` entry in a run is a ONE-ROW PROBE**: one security, one
   trading day, one field. If the response is empty, errors or returns a different identifier, the run records a refusal for that request, stops it (no further cells spent on it), and the
   receipt says `identifier_form: "/cusip/ UNVERIFIED"`; if it returns the row, the receipt says `VERIFIED` and the draw continues. The result is cached for the rest of the run only.
2. **`dates` entries.** For an entry with a `dates` list, the days to draw are those dates not already stored (by identity: (identifier, date)); `undrawn_runs` returns maximal runs of
   CONSECUTIVE trading days among them, so each isolated date is one single-day request and a consecutive stretch is one request. Cells = days x the entry's fields. A non-trading date is a loud error.
3. **Per-entry `fields`.** An entry's `fields` (when present) replaces the request's `fields` for that entry: `_draw_request`'s `per_row` and `remaining_cells` use the entry's own list. Stored output carries
   one column per field asked.
4. **The reference channel.** A request with `channel: "reference"` and a list of securities is drawable: ONE call per chunk of at most `CHUNK_ROWS` securities through the client's `reference_data(securities, fields)`;
   cells = securities x fields; the output is written as `reference-<day>.parquet` (columns `security`, one per field) beside the history output; identity = (security, field), never re-asked once stored.
   The `model_block` channel stays NOT drawable (its own producer).
5. **The priority gate.** The drawer skips (no vendor call, counted in the receipt as `skipped_excluded`) a security of a `need_class: client` request that `priority_gate.excluded` returns, and REFUSES
   the request (fail closed) when the crosswalk or transactions cannot be read. A `non_client` request is never gated.
6. **Open list and plan.** `standing_drawer.py --open` prints ONE JSON line `{"open": [ids in draw order], "not_drawable": [{"request_id", "why"}]}`: the order is the existing demand_queue order (tier, then rank, then
   file order); every request file in `requests/` that is not drawable carries a plain reason (`model_block: its own producer`, `no securities list`, `already complete`). `--plan --request ID` works for a request
   with no request-level `start`/`end` (it prints `window_start` from the request's declared `window_start`), plus `channel`, `securities`, `remaining_cells` (identity-based) and `identifier_forms`
   (a dict form -> count).
7. NEW `test_demque_drawer_cusip_entries.py` (pytest; a stub client, stub stored frames, no network) with exactly these names:
   `test_a_cusip_entry_resolves_to_a_bloomberg_identifier_and_the_first_draw_of_an_unverified_form_is_a_one_row_probe`,
   `test_a_dates_entry_draws_only_its_undrawn_trading_days_by_identity_one_request_per_consecutive_run`,
   `test_a_per_entry_fields_override_draws_that_entrys_fields_and_a_reference_request_draws_securities_by_fields`,
   `test_the_drawer_skips_a_client_request_security_the_priority_gate_excludes_and_fails_closed`.
   The existing drawer tests (`test_demque_standing_drawer.py`, `test_demque_standing_drawer_close.py`, `test_demque_carry_over.py`) keep passing; one that pins "a security without a ticker is not drawable" changes that
   assertion and nothing else.

### ACCEPTANCE

<criterion id="DQ9-t56-AC1" cell_refs="DQ-t-56"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t56_tests.py</invocation><expect>DRAWER-OK</expect></criterion>
<criterion id="DQ9-t56-AC2" cell_refs="DQ-t-56"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t56_real.py</invocation><expect>DRAWER-REAL-OK</expect></criterion>
`DQ9-t56-AC1` -- the four named tests. `DQ9-t56-AC2` -- on the REAL request files, read only: the drawer lists B1, the porting test, the fund-type check and the TR comparison as open (B1 and the porting test before
the TR comparison), every not-drawable request has a reason, and each plan's remaining cells equal what `bbg_quote.py --quote` prices for the same file. Report the whole folder
`pytest data/mdpf/scripts/demque` once, and the `--open` line verbatim.

<expected_criteria>DQ9-t56-AC1,DQ9-t56-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `DRAWER-BAD no file ...`; `DRAWER-REAL-BAD arm1 ... (standing_drawer.py: error: unrecognized arguments: --open)`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO Bloomberg call, NO Yahoo call, no write to S3, the real budget ledger, the actuals ledger, the queue or any pacer state, no AWS write, no deploy, no timer. `standing_drawer.py --apply` is NEVER run
  by you, and the stub client in your tests never reaches the network.** Build no alarm, monitor or notification (standing moratorium).
- **Account ids never enter a committed file.**
- **Refusal clause.** If a criterion cannot be met as written (for example the site client has no `reference_data`), stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W48-S<k>`,
  `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, appended at the end of your own branch's copy. Do NOT merge `box/dell1` (it is blocked by a
  foreign row); the issuer unions the investigation file at the drain.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/test_demque_drawer_cusip_entries.py
data/mdpf/scripts/demque/test_demque_standing_drawer.py
data/mdpf/scripts/demque/test_demque_standing_drawer_close.py
data/mdpf/scripts/demque/test_demque_carry_over.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit; a change to `blp_client.py` or any site Z file is a surprise row asking for the grant, not an edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-56`.
<owned_cells>DQ-t-56</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t56-AC1, DQ9-t56-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~48/MDPF_DEMQUE.TO-DQ-t56.drawer-cusip-entries-and-reference-channel.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t56-AC1,DQ9-t56-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--open` line verbatim, each plan line, how the probe works and what the receipt prints for it, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the standing drawer's existing task at site Z runs the merged code at its next non-trading-day fire (2026-10-17), under the draw rules and ~ZQ's task.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a request-shape extension; the draw still stops on the first vendor limit warning or refusal, and the unverified identifier form is probed with one row first.
risk: LOCAL -- code and tests. The first live use is the 2026-10-17 fire at site Z (WORLD: a vendor call), under the issuer's hold-lift and the 585-cell/day surface E reserve; the issuer reads the receipt.
direct_act: false -- a worker order.
</preflight>

Source: CTO msgs 5165, 5169, 5174; the queue form; decomposition round 9.
