# TO MDPF_DEMQUE.TO-DQ-t15 -- round 5 DQ-t-15: every live Bloomberg request kind prices to a finish day (per-kind ceilings)
<to_id>MDPF_DEMQUE.TO-DQ-t15</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~13</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-15` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 5 -- CUT) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-15` (FWD-4; C-RESERVE; CTO round-4 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round4.md` item 1). The quote
`data/mdpf/scripts/demque/bbg_quote.py` (read it) gives a finish day only when a channel's ceiling AND reserve are present in
`data/mdpf/scripts/demque/bbg_allowance.json`. Today `reference.ceiling`, `history.ceiling`, `history.reserve` and both `model_block`
figures are absent, so three live requests get no finish day. C-RESERVE (PRD `prd/MDPF_DEMQUE_PRD.md`): the CEILING is "seeded from the
measured floor on capacity and re-measured from the ledger"; the RESERVE is the tier-1 production draw plus a stated margin.

**Build:**
1. NEW `data/mdpf/scripts/demque/ceiling_from_ledger.py`. It reads the SERVED demand ledger read-only: every object under the builder
   home `lib.opal_naming.address("bloomberg","global","bronze","demand_ledger","dt=<day>")` (list the `dt=` partitions; boto3 read
   only). Each line carries `channel`, `cells`, `claim`. Per channel, the floor = the largest single-day sum of `cells` (rows whose
   `cells` is null are left out and counted in a `skipped` figure). `--print` prints ONE JSON line `{channel: {"value", "day",
   "claim": "held", "basis", "skipped"}}`. `--write` sets `<channel>.ceiling` in `bbg_allowance.json` to `{"value", "claim": "held",
   "basis"}` ONLY where the channel's ceiling is absent or lower; a measured or higher ceiling is never lowered (bql's 2,920,000 stays).
   The basis names the ledger day and the object read, and says the figure is a floor (a day drawn with no refusal), not a capacity.
2. `reserve_estimate.py`: add the `history` channel the way `bql` and `reference` are done -- the tier-1 producers of
   `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` read AS TEXT, names x fields x rows per name for their daily history legs,
   claim held, margin stated, gaps named. Then `--write` it. Never import a producer; never guess a number.
3. `bbg_quote.py`: a `model_block` request is priced on its component channels. The breakdown's `header` and `forecast` groups draw the
   `reference` channel and its `history` group draws `history` (read `integrations/bloomberg/research/model_block_pull.py` to confirm
   which request type each group sends; if a group is neither, name it in a row). `finish_date` = the LATER of the two channels' finish
   days; `finish_date_claim` = held if any figure used is held; `allowance_gap` names a missing component figure. The `model_block`
   allowance entries stay as they are (unused).
4. NEW `data/mdpf/scripts/demque/test_demque_ceiling.py` (pytest; stub ledger rows, no S3) with exactly these names:
   `test_ceiling_is_largest_ledger_day_per_channel_never_lowered`, `test_ceiling_carries_claim_held_and_basis`,
   `test_model_block_finish_is_later_of_its_component_channels`. Keep `test_demque_bbg.py` and `test_demque_reserve.py` passing.

### ACCEPTANCE

<criterion id="DQ5-t15-AC1" cell_refs="DQ-t-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R5_CHECKS/dq_t15_tests.py</invocation><expect>CEIL-OK</expect></criterion>
<criterion id="DQ5-t15-AC2" cell_refs="DQ-t-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R5_CHECKS/dq_t15_quotes.py</invocation><expect>QFIN-OK</expect></criterion>
`DQ5-t15-AC1` -- the three named tests. `DQ5-t15-AC2` -- three REAL requests (reference, model_block, history) each quoted with a finish
day and its claim, from the committed `bbg_allowance.json` after your `--write` runs.

<expected_criteria>DQ5-t15-AC1,DQ5-t15-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `CEIL-BAD no file ...`; `QFIN-BAD ... reference.ceiling absent | ...
model_block.ceiling absent ... | ... history.ceiling absent; history.reserve absent`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No Bloomberg call, no import of any `integrations/bloomberg/` or `data/etfs/` module, no AWS write, no deploy.** The demand ledger is
  read only (S3 `GetObject` / `ListObjectsV2`). Producer files are read as text.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written (for example a history reserve no producer's code states), stop, write the
  reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W13-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class
  `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/bbg_allowance.json
data/mdpf/scripts/demque/reserve_estimate.py
data/mdpf/scripts/demque/ceiling_from_ledger.py
data/mdpf/scripts/demque/test_demque_ceiling.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 5), cell `DQ-t-15`.
<owned_cells>DQ-t-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ5-t15-AC1, DQ5-t15-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~13/MDPF_DEMQUE.TO-DQ-t15.per-kind-ceilings.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ5-t15-AC1,DQ5-t15-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the three quotes' finish days and claims, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; the ledger read uses the seat's existing S3 read.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code and a config file.
risk: LOCAL -- code, config and tests; the served ledger is read only.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.3 FWD-4, C-RESERVE, C-QUOTE; CTO round-4 analysis @91f3ee9da6 item 1; decomposition round 5.
