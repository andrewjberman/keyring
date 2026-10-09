# TO MDPF_DEMQUE.TO-DQ-t9 -- round 3 DQ-t-9: a Bloomberg request is priced in cells per channel before it draws, and its actual draw is recorded beside the quote
<to_id>MDPF_DEMQUE.TO-DQ-t9</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~8</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `DQ-t-9` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 3) |
**outcome_ref:** FWD-3, FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-9`: every Bloomberg pull in the organisation now files a request on this queue (folder
`org/missions/D8/MDPF/MDPF_DEMQUE/requests/`), and none may draw until it is quoted. Build the quote and the actuals record. Bloomberg
itself is never called here: the Terminal is at site Z and site Z draws.

**A Bloomberg request** is a JSON file with `request_id, tier (1-5), reason, page, vendor ("bloomberg"), channel, securities [...],
fields [...], start, end` (start/end may be null for static fields). Read the two real ones first:
`requests/AMGT_RESAPP-493c-ICT-IDENTITY.json` (channel `reference`, 1 security, 4 fields, null window) and
`requests/AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json` (channel `model_block`, fields `["model_block"]`).

**Build** NEW `data/mdpf/scripts/demque/bbg_quote.py`:

1. `quote(request, allowance, drawn_today, today) -> dict` with `request_id`, `cells` = `{"bloomberg_<channel>": n}`, `finish_date`,
   `allowance_gap`, and for model_block a `breakdown` dict. Cells (one row times one field, PRD C-CELL):
   - `reference`: securities x fields (static fields, one row each).
   - `history` and `bql`: weekdays in `[start, end]` x fields x securities (start/end required).
   - `model_block`: the producer's own declared field groups in `integrations/bloomberg/research/model_block_pull.py` -- read its
     module-level lists (`HEADER_FIELDS`, `HIST_FIELDS`, `FORECAST_FIELDS`, and any other group its per-name pull spends, as the producer's
     code shows) with `ast` from the file's text; NEVER import that module (it signs in to Bloomberg). Cells per security = the sum over
     groups of (that group's fields x the rows the producer requests for it, as its code states); `breakdown` = the per-group counts, which
     must sum to the total. State in a docstring which lines you read each figure from.
   - any other channel or a malformed request: `ValueError` naming it.
2. **Allowance.** NEW `data/mdpf/scripts/demque/bbg_allowance.json`: per channel `ceiling`, `reserve`, each as `{"value": <int or null>,
   "claim": "measured" | "held" | "absent", "basis": "<source>"}`. Seed: `bql.ceiling` = 2920000, claim `measured`, basis "PRD C-RESERVE:
   the 2026-10-05 BQL block, a floor"; `bql.reserve` = null, claim `absent`, basis "tier-1 production draw not yet on the ledger (CTO msg
   1511)"; `reference`, `history`, `model_block`: ceiling and reserve null / `absent`. `quote()` computes `finish_date` only when the
   channel's ceiling and reserve are both non-null: allowance per day = ceiling - reserve; today's room = allowance - drawn_today; the
   finish date is the first weekday by which the cumulative room covers the request (today counts if a weekday). Otherwise `finish_date`
   is `null` and `allowance_gap` names exactly which figure is absent, e.g. `"bql.reserve absent"`. Never default a missing figure.
3. `record_actual(ledger_path, request_id, drawer, channel, cells_drawn, quote=None, day=None)`: appends one JSON line `date, vendor
   "bloomberg", channel, job, page (if known), drawer, cells_quoted (int or null), cells_drawn, outcome "DRAWN", label`; `label` is
   `"drawn before C-METER Bloomberg; no quote"` exactly when `quote` is None, else `"quoted"`.
4. CLI: `python bbg_quote.py --quote FILE` prints the quote as ONE JSON line (reads `bbg_allowance.json` beside the module; drawn_today
   0; today = the local date); `python bbg_quote.py --record LEDGER --request FILE --drawer SERIAL --cells N [--no-quote]` appends.
5. NEW `data/mdpf/scripts/demque/test_demque_bbg.py` (pytest; synthetic requests; a small synthetic producer file for the model_block
   test) with exactly these names: `test_reference_request_quotes_securities_times_fields`,
   `test_history_request_quotes_weekdays_times_fields_per_security`, `test_model_block_quote_reads_the_producers_declared_fields`,
   `test_allowance_unknown_gives_no_finish_date_and_names_the_gap`, `test_allowance_known_gives_finish_date_above_the_reserve`,
   `test_actual_recorded_beside_quote_and_unquoted_draw_is_labelled`.

Do NOT edit `demand_queue.py` or any other module; do NOT create `__init__.py`; do NOT type an S3 address.

### ACCEPTANCE

<criterion id="DQ3-t9-AC1" cell_refs="DQ-t-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R3_CHECKS/dq_t9_tests.py</invocation><expect>BBGQ-OK</expect></criterion>
<criterion id="DQ3-t9-AC2" cell_refs="DQ-t-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R3_CHECKS/dq_t9_seam.py</invocation><expect>BSEAM-OK</expect></criterion>
`DQ3-t9-AC1` -- the six named tests, and three round-1/2 queue tests still pass (regression arm). `DQ3-t9-AC2` -- the seam against the two
real filed requests and the real producer file: ICT quotes exactly 4 reference cells; ABNB quotes a positive model-block total whose
breakdown sums to it; each carries a finish date or a named allowance gap.

<expected_criteria>DQ3-t9-AC1,DQ3-t9-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base: `BBGQ-BAD`, `BSEAM-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No Bloomberg call, no import of any `integrations/bloomberg/` module, no AWS call, no deploy.** Read producer files as text only.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written (for example the producer's per-name rows cannot be read from its code),
  stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W8-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u
  +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/bbg_allowance.json
data/mdpf/scripts/demque/test_demque_bbg.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 3), cell `DQ-t-9`.
<owned_cells>DQ-t-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ3-t9-AC1, DQ3-t9-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~8/MDPF_DEMQUE.TO-DQ-t9.bloomberg-quote-and-actuals.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ3-t9-AC1,DQ3-t9-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code; the quote never calls the vendor.
risk: LOCAL -- code, a config file and tests.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.3 FWD-3, FWD-4, C-CELL, C-METER, C-RESERVE, C-QUOTE, C-SITES; CTO msgs 1466, 1502, 1511; decomposition round 3.
