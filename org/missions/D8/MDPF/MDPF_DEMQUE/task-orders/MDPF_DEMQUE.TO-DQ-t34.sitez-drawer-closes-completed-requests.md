# TO MDPF_DEMQUE.TO-DQ-t34 -- round 9 DQ-t-34: the standing drawer closes a request whose every security reached its end date
<to_id>MDPF_DEMQUE.TO-DQ-t34</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.7.0_AE_CloudOps~MDPF1</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-11 ~18:0xZ (rows MDPF_DEMQUE-Z-S4 and MDPF_DEMQUE-Z-S5, BLOCKING; issuer defects; no criterion change):** (1) `dq_t33_real.py`, the start oracle, was once-only: it read the real folder after the issuer had already made its chained re-freeze, so its `supersedes_new` arm demanded a transition that had happened. It now restores its input from the superseded copy and prints QR-REAL-OK on the real tree (committed with this amendment); `bbg_quote.record_actual` accepting `COMPLETE` is exercised, as you measured. (2) Build items 3 and 4 could not both hold: `test_demque_standing_drawer.py`'s own fixture completes BOTH its requests on day 2 and asserts every actuals line is DRAWN (:111 and :135). GRANTED: `data/mdpf/scripts/demque/test_demque_standing_drawer.py` for exactly those two assertions: the day-2 run outcome and every actuals line of that test accept `DRAWN` or `COMPLETE`, and the lines of the day on which a request completes must read `COMPLETE` while every earlier line reads `DRAWN`. No other assertion in that file changes; its three tests keep passing. Land the candidate you preserved at `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T34` once that file is amended. This supersedes build item 4's word "unedited" for those two lines only.
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-17 ~14:5xZ (site Z row MDPF_DEMQUE-Z-S7, `0.7.0_AE_CloudOps~MDPF1`):** the 14:00Z fire drew the TR request's last 1,004 cells but recorded it STOPPED, because a later surface-B request stopped the run and the drawer decided every request's outcome from the run's stop reason; a complete request is skipped by later runs, so the COMPLETE line this order's AC2 reads can never appear. AC2 grades the same property (the request is closed; nothing 0-cell follows completion). `dq_t34_close.py` now also passes when no COMPLETE row exists and `standing_drawer.py --plan --request` reads `remaining_cells` 0 at the last drawing day with no later row; run it at site Z, where the stored rows are. The drawer defect itself is `TO-DQ-t74` (outcome per request). The criterion text below keeps its original wording.
**CARRIER (issuer, 2026-10-11 ~18:2xZ, answering site Z's manager via MSTR~DELL1 msg 4055):** crossbox ORDER XB-20261011T175203Z-1e74 is THIS order as amended and SUPERSEDES XB-20261011T154015Z-5c6f (the same order before this amendment). There is ONE live order, this file at its head; the issuer closed 5c6f's from-side.
**Directive:** D8 | **Fabric:** dell1 (placement site Z) | **Decomp cell:** `DQ-t-34` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT) |
**outcome_ref:** FWD-3 | **depends_on:** DQ-t-33 (`COMPLETE` in `bbg_quote.record_actual`)

---

## WORKER FACE

### THE CELL

`DQ-t-34` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` section 1: "a request whose every security
reached its end date is CLOSED, with no 0-cell DRAWN lines after completion"; row `MDPF_DEMQUE-Z-S3`). Your DQ-t-27 standing drawer
(`data/mdpf/scripts/demque/standing_drawer.py`) treats a request as open while its drawn cells are fewer than its quoted cells. The TR request
was quoted on weekdays (15,720) and the vendor returns trading days (15,120 or so), so it would never read closed and every non-trading-day
fire after the last cell would append a 0-cell DRAWN line. DQ-t-33 now prices history on trading days and lets an actuals line carry outcome
`COMPLETE`. **Start only after DQ-t-33's commit is in your tree** (`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t33_real.py`
prints QR-REAL-OK there; `bbg_quote.record_actual` accepts `outcome="COMPLETE"`).

**Build** (`standing_drawer.py` and a NEW test file; every other behavior of the drawer stays):
1. **Reached its end:** a security has reached its end when no NYSE trading day (`lib/trading_calendar.py`) lies in `(its latest stored date, the
   request's end]`, counting the dates already stored by earlier runs (the same cursor the drawer already derives). A request is COMPLETE when
   every one of its securities has reached its end.
2. **Open requests** no longer means "drawn cells below quoted cells": a request is open only if it is not COMPLETE. A COMPLETE request is
   skipped at the start of a run, with no actuals line and no draw.
3. **The completing fire:** when a run's draws leave every security of a request at its end, that run records its ONE line for the request
   with `outcome` `COMPLETE` (`bbg_quote.record_actual(..., outcome="COMPLETE")`, `cells_drawn` the cells that run drew), not `DRAWN`. A request
   that is already COMPLETE at the start of a run records nothing, so no 0-cell `DRAWN` line follows completion.
4. NEW `test_demque_standing_drawer_close.py` (pytest; stub client, `tmp_path`, no network, no Terminal) with exactly these names:
   `test_request_whose_securities_all_reached_their_end_is_closed_and_skipped`,
   `test_the_completing_fire_records_complete_not_drawn` and
   `test_no_zero_cell_drawn_line_after_completion` (a later fire records nothing for the request and still draws the other open requests).
   The three existing `test_demque_standing_drawer.py` tests keep passing unedited.
5. **The site-Z act (a pair; `1.0.0_SA_CTO~Z` signs the site-Z half; the CTO half is the round-8 analysis section 1):** the standing task is
   unchanged and already registered (`mdpf-demque-drawer-daily`, daily 10:00 ET). Nothing is registered or re-registered; the task runs the
   updated file from the repository root. Open a change-management entry first and close it at the completing fire (the sentinel committed).

### ACCEPTANCE

<criterion id="DQ9-t34-AC1" cell_refs="DQ-t-34"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t34_tests.py</invocation><expect>CL-OK</expect></criterion>
<criterion id="DQ9-t34-AC2" cell_refs="DQ-t-34"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t34_close.py</invocation><expect>CLOSE-OK</expect></criterion>
`DQ9-t34-AC1` -- the three named tests. `DQ9-t34-AC2` -- the REAL ledger: exactly one `COMPLETE` row for the TR request, `cells_drawn` > 0, and no
row of the job after it (no 0-cell `DRAWN` line). AC2 is date-gated to the fire that completes the request (the TR request has about 3,400
cells left after 2026-10-11, so the next scheduled non-trading-day fire, 2026-10-17); the order stays open until it reads CLOSE-OK. A history
draw is barred on trading days (round-6 R1), so that fire has no on-demand act.

<expected_criteria>DQ9-t34-AC1,DQ9-t34-AC2</expected_criteria>

Run each invocation from the repository root at site Z. At the base: `CL-BAD no file ...`; `CLOSE-BAD no COMPLETE row yet`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Bloomberg draws only through the standing drawer, only on non-trading days, only inside the quoted day room;** stop on any limit warning or
  refusal; no manual draw; no auth path changed; no S3 write beyond the uploader's existing daily ledger object.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-Z-W3-S<k>`, `fabric` `site-z`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/standing_drawer.py
data/mdpf/scripts/demque/test_demque_standing_drawer_close.py
data/mdpf/scripts/demque/test_demque_standing_drawer.py
org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl
org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-34`.
<owned_cells>DQ-t-34</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t34-AC1, DQ9-t34-AC2. Instance at `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE.TO-DQ-t34.sitez-drawer-closes-completed-requests.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t34-AC1,DQ9-t34-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the completing fire's line, the change-management entry, commits and push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the registered task `mdpf-demque-drawer-daily` runs the updated file.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the uploader's existing PutObject is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE a narrowing change to an existing standing draw (it draws no more than before and stops after completion); reviewed under the site-Z half.
risk: WORLD -- the standing Bloomberg history draw at site Z through the queue, under a pair (CTO~Z signs the site-Z half).
direct_act: false -- a seat order to the site-Z per-project lane.
</preflight>

Source: CTO round-8 analysis @92a9b27704 section 1 (Z-S3); TO-DQ-t27 (the drawer this narrows); row Z-S3 (REMEDIATION_v7); decomposition round 9.
Codex lanes run this mission-tree order directly (site Z AGENTS.md @a55888e3a2).
