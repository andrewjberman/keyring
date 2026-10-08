# TO MDPF_HEALGAP.TO-HG-t3 -- round 2 HG-t-3: every run records which of the day's three feeds arrived, and a partial day never reads as a success
<to_id>MDPF_HEALGAP.TO-HG-t3</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~3</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-3` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 2) |
**outcome_ref:** FWD-2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-3`. FWD-2: anyone reading a run's result can tell whether every part of that day's data arrived, without looking at logs; a run
missing any part never reads as a success.

**The estate, read at the base.** `infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py`: `ingest(now_iso, date, force=False, induce=None)` (:403) lands three feeds
for `date` -- `rebalancer_models`, `rebalancer_accounts` (paginated, `_land_paginated_type` :249) and `rebalancer_model_detail`
(`_land_model_details` :300) -- then the count reconcile, then writes the complete-stamp `meta/<date>-complete.json` LAST (`_stamp_key`
:207) and prints/returns a `{"verdict": "BRONZE-COMPLETE", ...}` summary (:469). `_already_landed` (:211) skips a complete date by LISTING
the stamp. `META_PREFIX` (:70). `induce="auth-lapse"` (:408-412) raises a 401 after the guard. Tests: `test_healgap_guard.py` (round 1),
`test_lambda_function.py` (original); copy their stubbing style (no network, S3 stubbed).

**Build:**
1. A per-date run result at `META_PREFIX + "<date>-result.json"`, written on EVERY run that gets past the guard (success or not):
   `{"as_of", "run_at", "feeds": {<feed>: {"status": "arrived"|"missing", "landed_at": <iso>|null, "healed_at": <iso>|null}}, "verdict":
   "COMPLETE"|"PARTIAL"}`. A feed is `arrived` when its keys for the date exist after the run (read by listing, the way the guard does).
   When an earlier result marked a feed `missing` and this run lands it, set `healed_at` (keep the earlier result's other fields).
2. `verdict` is `COMPLETE` only when all three arrived. On `PARTIAL`: write the result, do NOT write the complete-stamp, and RAISE (a
   clear `RuntimeError` naming the missing feeds), so the async engine never treats it as a success and `on_success` does not fire.
3. `induce="drop-feed:<feed>"` (feed one of the three names) skips landing exactly that feed for this run; any other induce value still
   raises the existing `ValueError`. It must not touch the login.
4. Tests in NEW `test_healgap_result.py` with these exact names (each must PASS): `test_result_all_three_arrived_is_complete`,
   `test_result_missing_feed_is_partial_and_raises_without_stamp`, `test_induce_drop_feed_skips_exactly_that_feed`,
   `test_reattempt_records_healed_at_for_the_filled_feed`, `test_result_readable_without_logs` (the result object alone names the missing
   feed and day).

### ACCEPTANCE

<criterion id="HG2-t3-AC1" cell_refs="HG-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_t3_tests.py</invocation><expect>RESULT-OK</expect></criterion>
`HG2-t3-AC1` -- the five named tests in `test_healgap_result.py` pass: complete day, partial day raises without a stamp, drop-feed induce, healed_at on a re-attempt, result readable alone.

<criterion id="HG2-t3-AC2" cell_refs="HG-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_t3_legacy.py</invocation><expect>LEGACY-OK</expect></criterion>
`HG2-t3-AC2` -- the runner's existing tests (`test_healgap_guard.py`, `test_lambda_function.py`) still pass.

<expected_criteria>HG2-t3-AC1 HG2-t3-AC2</expected_criteria>

Run each invocation from the worktree root. AC1 FAILS at the base (2026-10-08 ~14:5xZ): `RESULT-BAD no file ...`. AC2 is a regression guard and reads `LEGACY-OK` at the base.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** Every deploy and apply is the
  issuer's, at the drain. Read-only AWS reads are allowed where a criterion names them.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your
  report with its state at your close.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-W3-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation
  file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row.

<paths>
infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py
infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/test_healgap_result.py
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 2, the enrichment), cell `HG-t-3`.
<owned_cells>HG-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG2-t3-AC1, HG2-t3-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~3/MDPF_HEALGAP.TO-HG-t3.per-feed-run-result.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG2-t3-AC1 HG2-t3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule change.
comp-iam: RUN at L5 (decomposition ROUND 2 battery): the result key sits under blackdiamond/cottonwood/meta/, inside the runner's existing PutObject grant (cot_rebalancer_runner.tf:73-112); no role change.
comp-adversary: RUN at L5 (decomposition ROUND 2 battery): the raise on PARTIAL makes the async engine retry twice and skip on_success; the tests pin healed_at and no double-landed feed (C-IDEMPOTENT).
risk: WORLD -- runner code the issuer deploys at the drain under a change-management entry.
direct_act: false -- the class is WORLD.
</preflight>

Source: PRD v0.2 ENDPOINT FWD-2; CTO round-1 analysis @475c742f71 section 3; decomposition round 2.
