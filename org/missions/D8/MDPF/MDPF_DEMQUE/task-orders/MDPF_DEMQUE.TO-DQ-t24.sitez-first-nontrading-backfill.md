# TO MDPF_DEMQUE.TO-DQ-t24 -- round 7 DQ-t-24: the first non-trading-day history backfill at site Z, drawn and read against its quote
<to_id>MDPF_DEMQUE.TO-DQ-t24</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.7.0_AE_CloudOps~ZQ</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~14:5xZ (row MDPF_DEMQUE-Z-W1-S4, refusal `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T24_REVIEW.md`; issuer defect):** the order required stopping on a vendor limit warning and recording the stop, but the client hides `fieldExceptions` and the recorder always writes DRAWN. GRANTED, both OPT-IN with defaults that leave every existing caller byte-for-byte unchanged: (1) `integrations/bloomberg/mcp/blp_client.py`: `historical_data(..., diagnostics=None)` -- when a list is passed, each `securityData.fieldExceptions` entry and any response warning is appended to it (security, field, category, message); nothing else changes. (2) `data/mdpf/scripts/demque/bbg_quote.py`: `record_actual(..., outcome="DRAWN", stop_reason=None)` and CLI `--outcome` / `--stop-reason`; a stop line carries `outcome: "STOPPED"` and its reason. `bbg_backfill.py` passes a diagnostics list, stops at the first entry, and records the stop. The client change runs under `1.0.0_SA_CTO~Z`'s half with the draw. No criterion changes.
**Directive:** D8 | **Fabric:** dell1 (placement site Z) | **Decomp cell:** `DQ-t-24` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 7 -- CUT) |
**outcome_ref:** FWD-3 | **depends_on:** DQ-t-22

---

## WORKER FACE

### THE CELL

`DQ-t-24` (FWD-3, FWD-4; CTO round-6 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round6.md` R1, read it). A history
backfill draws only on NON-trading days, at most the measured 5,858 history cells a day, and a vendor limit warning or refused request
stops it. The request is `org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json` (KO, JNJ, T, VZ, MO, XOM;
`PX_LAST` and `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`; 2021-10-01..2026-10-08; 15,720 cells; research use). DQ-t-22 (on box/dell1, reaching
site Z through the integrate) makes `bbg_quote.py --quote <request> --today 2026-10-10` print `allowance_today` 5858 and `finish_date`
2026-10-17. **Start only after that commit is in your tree** (`dq_t22_quote.py` prints NTDQ-OK there).

**Build:**
1. NEW `data/mdpf/scripts/demque/bbg_backfill.py`: `run(request_path, today, client)` quotes the request with `bbg_quote.quote` for
   `today`, draws nothing when `allowance_today` is 0, else draws the request's history in chunks (security x date range) through the
   site's existing Bloomberg client (read `integrations/bloomberg/READ_HERE.md` first and use its budgeted sign-in; never a new auth
   path) until the cells drawn would pass `allowance_today`, and STOPS at the first vendor limit warning or refused request, recording
   the stop. It writes the fetched rows to your deliverables folder (parquet), records each draw with `bbg_budget.record(mode=
   "demque-backfill", rows, batch_id)`, and appends ONE actuals line per run with `bbg_quote.py --record
   org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl --request <request> --drawer 0.7.0_AE_CloudOps~ZQ --cells <n>` (outcome
   `DRAWN`, or the stop named). It never draws on a trading day.
2. `bbg_ledger_upload.py`: mode `demque-backfill` converts rows to cells at 2 fields a row (the request's two fields), claim held,
   basis this order.
3. NEW `data/mdpf/scripts/demque/test_demque_bbg_backfill.py` (pytest; a stub client, no network) with exactly these names:
   `test_backfill_stops_at_the_days_allowance`, `test_backfill_stops_on_a_vendor_limit_warning`, `test_trading_day_backfill_draws_nothing`.
4. **The site-Z act (a pair; `1.0.0_SA_CTO~Z` signs the site-Z half):** run `bbg_backfill.py` ONCE on Saturday 2026-10-10 (a non-trading
   day), inside a change-management entry. A one-shot Windows task for that run is allowed (its name from `lib/opal_naming.py` `name()`),
   removed after the run. Then run AC2 and report the drawn count against the quoted 5,858.

### ACCEPTANCE

<criterion id="DQ7-t24-AC1" cell_refs="DQ-t-24"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R7_CHECKS/dq_t24_tests.py</invocation><expect>BKF-OK</expect></criterion>
<criterion id="DQ7-t24-AC2" cell_refs="DQ-t-24"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R7_CHECKS/dq_t24_draw.py</invocation><expect>DRAW-OK</expect></criterion>
`DQ7-t24-AC1` -- the three named tests. `DQ7-t24-AC2` -- at site Z after the 2026-10-10 run: an actuals row for that day with cells
drawn > 0 and <= 5,858, read against the quote by `quote_vs_actual.py`.

<expected_criteria>DQ7-t24-AC1,DQ7-t24-AC2</expected_criteria>

Run each invocation from the worktree root at site Z. At the base: `BKF-BAD no file ...`, `DRAW-BAD drawn=0 rows=0`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **One Bloomberg draw run, on 2026-10-10 only, inside its quoted allowance;** stop on any limit warning or refusal; no second run.
  No notebook, producer or auth path is changed. No S3 write beyond the uploader's existing daily ledger object.
- **You arm no timer, background task or OS task** except the one-shot task named in build item 4.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-Z-W1-S<k>`, `fabric` `site-z`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_backfill.py
data/mdpf/scripts/demque/test_demque_bbg_backfill.py
data/mdpf/scripts/demque/bbg_ledger_upload.py
data/mdpf/scripts/demque/bbg_quote.py
integrations/bloomberg/mcp/blp_client.py
org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl
org/critical_paths/change_management/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 7), cell `DQ-t-24`.
<owned_cells>DQ-t-24</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ7-t24-AC1, DQ7-t24-AC2. Instance at `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE.TO-DQ-t24.sitez-first-nontrading-backfill.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ7-t24-AC1,DQ7-t24-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the drawn count vs 5,858, any stop, the change-management entry, commits and push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at the cut: a one-shot task on 2026-10-10 only, removed after its run; the seat reads comp-schedule at site Z before registering it.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the uploader's existing PutObject is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE one budgeted Bloomberg run inside its quoted allowance, stopping on any vendor warning; reviewed under the site-Z half.
risk: WORLD -- a Bloomberg history draw at site Z through the queue, under a pair (CTO~Z signs the site-Z half).
direct_act: false -- a seat order to the site-Z per-project lane.
</preflight>

Source: CTO round-6 analysis @4f7ded8845 R1; row D1-W17-S1; decomposition round 7. Codex lanes run this mission-tree order directly
(site Z AGENTS.md @a55888e3a2).
