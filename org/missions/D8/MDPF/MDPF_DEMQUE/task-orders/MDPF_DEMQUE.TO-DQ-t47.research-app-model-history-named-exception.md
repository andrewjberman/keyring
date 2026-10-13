# TO MDPF_DEMQUE.TO-DQ-t47 -- round 9 DQ-t-47: the research-app model block keeps its 2016 history as a NAMED exception to the 365-day non-client rule
<to_id>MDPF_DEMQUE.TO-DQ-t47</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~39</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>MODELEXC</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-47` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 12) |
**outcome_ref:** C-QUOTE, C-PRIORITY, FWD-4 | **depends_on:** DQ-t-44 (merged @900406e221)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-13 (relayed by CTO msg 4931; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`, section A4): "I also agree with
model data depth on financials back to 2016." The research app's model block (`model_block_pull.py`, `HIST_START` 2016-01-01) is a **named exception** to the 365-day
non-client rule: a company model needs several fiscal years; the pull is one-time per newly covered company (ABNB is 989 cells). The queue's refusal (DQ-t-44,
`bbg_quote._validate`) currently rejects it. This cell lets the refusal admit it **with that reason and no other**. **No Bloomberg call, nothing drawn.**

**Build** (read `data/mdpf/scripts/demque/bbg_quote.py` `_validate` and its need-class rule first):
1. **The named exception.** A request may carry `window_exception` with the exact value `"research_app_model_history_2016"`. The 365-day-before-need-date check is waived
   ONLY when ALL of: `window_exception` equals that value; `need_class` is `non_client`; the channel is `model_block`; and `window_start` is on or after `2016-01-01`. Every other
   rule stands: the 2012-01-01 floor, `start` not before `window_start`, `need_date` present for a non-client history window, and the refusal naming the request id. A request
   with any other `window_exception` value, or the right value on another channel or class, or with a start before 2016-01-01, is refused as before, with a message that names
   the exception it did not qualify for.
2. **Declare it.** In `org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json` add exactly `"window_exception": "research_app_model_history_2016"`
   and change nothing else (it already declares `need_class` `non_client`, `need_date` 2026-10-09 and `window_start` 2016-01-01).
3. NEW `test_demque_window_exception.py` (pytest; stubs, no network) with exactly these names:
   `test_a_model_block_with_the_named_research_app_exception_is_admitted_from_2016_and_no_earlier`,
   `test_the_exception_is_refused_on_another_channel_another_class_or_an_unnamed_reason`,
   `test_the_rule_still_refuses_an_undeclared_exception_and_a_start_before_2012`.
   Existing demque tests keep passing; if one pins that the ABNB request is refused, change only that assertion.

### ACCEPTANCE

<criterion id="DQ9-t47-AC1" cell_refs="DQ-t-47"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t47_tests.py</invocation><expect>EXC-OK</expect></criterion>
<criterion id="DQ9-t47-AC2" cell_refs="DQ-t-47"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t47_real.py</invocation><expect>EXC-REAL-OK</expect></criterion>
`DQ9-t47-AC1` -- the three named tests. `DQ9-t47-AC2` -- on the REAL request files: every Bloomberg request is accepted (none refused), the ABNB file declares the named
exception from 2016-01-01, and its quote reads 989 model-block cells. Report the whole folder `pytest data/mdpf/scripts/demque` once (164 passed at the t-45 merge, plus these 3).

<expected_criteria>DQ9-t47-AC1,DQ9-t47-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `EXC-BAD no file ...`; `EXC-REAL-BAD arm1 {"accepted": 7, "checked": 8, "refused": [{"request_id": "AMGT_RESAPP-107a-ABNB-MODEL-BLOCK", ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: no Bloomberg call, no Yahoo call, no write to S3, the ledger, the queue or any pacer state; no AWS write, no deploy, no timer. `standing_drawer.py --apply` and
  `bbg_backfill.py --apply` are never run.** Do not add any other exception, and do not widen this one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W39-S<k>`, `fabric` `dell1`,
  `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check or the rule. Rows are APPEND-ONLY. Merge
  `box/dell1` into your branch (a merge, never a rebase) before you append rows.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/test_demque_window_exception.py
data/mdpf/scripts/demque/test_demque_need_class.py
org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-47`.
<owned_cells>DQ-t-47</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t47-AC1, DQ9-t47-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~39/MDPF_DEMQUE.TO-DQ-t47.research-app-model-history-named-exception.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t47-AC1,DQ9-t47-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, each real-check arm's line verbatim, the refusal messages for the three refused shapes, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a validation exception and one declaration; nothing draws or serves.
risk: LOCAL -- code, tests and one declaration. The draw is a site-Z act under the queue's budget and the Terminal sign-in (Andrew's).
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-13 via CTO msg 4931 (form section A4); DQ-t-44 merged @900406e221; decomposition round 9.
