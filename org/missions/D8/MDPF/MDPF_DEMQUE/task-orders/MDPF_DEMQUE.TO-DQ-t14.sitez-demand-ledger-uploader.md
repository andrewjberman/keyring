# TO MDPF_DEMQUE.TO-DQ-t14 -- round 4 DQ-t-14: site Z's recorded Bloomberg draws land as cell rows on the builder ledger home
<to_id>MDPF_DEMQUE.TO-DQ-t14</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.7.0_AE_CloudOps~ZQ</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-09 ~03:5xZ:** issued_to `0.7.0_AE_CloudOps~Z` -> `0.7.0_AE_CloudOps~ZQ`, the per-project site-Z lane (site Z CTO msg 32331; Andrew-direct ~03:5xZ relayed msg 1589: only site-bound acts go to site Z, on per-project lanes). The uploader is site-bound: it reads site Z's `bbg_budget` files. Clears gate2's one-project-per-seat finding on `~Z`.
**REVERTED by the issuer, 2026-10-09 ~04:0xZ (CTO msg 1611, site Z CTO msg 32344):** the four `~Z*` lanes hold no act until Andrew answers site Z's question on site-bound acts; site-bound orders stay as issued. issued_to is back to `0.7.0_AE_CloudOps~Z`; the gate2 seating finding on `~Z` stands open with that question.
**RE-ADDRESSED by the issuer, 2026-10-09 ~04:1xZ (msg 1644: site Z LIFTED its hold; the dell1 CTO's table):** issued_to `0.7.0_AE_CloudOps~ZQ` (LIVE). Clears the seating finding on `~Z`.
**STANDING CONDITION added by the issuer, 2026-10-09 ~08:0xZ (0.0.0_AB_MSTR~DELL1 msg 2082; LGIC_BLANKFIX switch-on @4d2bfc6dfd):** naming-place enforcement is live -- a NEW infra name the canon cannot place BLOCKS commit and apply. Any new name this order mints (the site-Z schedule's task name; any S3 key outside the queue's existing ledger address) comes from `lib/opal_naming.py` `name()`/`address()`; a builder refusal is a missing registry row to report, never a hand-typed name. No criterion changes.
**Directive:** D8 | **Fabric:** dell1 (placement site Z) | **Decomp cell:** `DQ-t-14` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 4) |
**outcome_ref:** FWD-2, FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-14` (site Z ruling 1.0.0_SA_CTO~Z msg 32309; dell1 CTO msg 1536 item 6). You are `0.7.0_AE_CloudOps~ZQ`, the site-Z Codex lane seated for MDPF_DEMQUE.
Site Z already records every Bloomberg draw: `data/etfs/scripts/rivalfunds/bbg_budget.py` `record()` (:73-76) appends to
`%LOCALAPPDATA%\opal_bbg_budget\bbg_budget_<UTC day>.jsonl` lines `{"at","mode","rows","batch_id"}`, called by `etf_daily_pull.py`,
`model_block_pull.py` (CORPUS induction), `collector_bloomberg.py` and `enrichment_bloomberg.py`. **Edit no producer.**

**Build** NEW `data/mdpf/scripts/demque/bbg_ledger_upload.py` (it runs at site Z):
1. `rows_for_day(day) -> list`: reads that day's jsonl via `bbg_budget.ledger_dir()` (importing `bbg_budget` is allowed: it does not sign
   in; never import a Bloomberg producer) and, per line, emits `{date, vendor "bloomberg", channel, mode, batch_id, rows, cells, claim}`.
   `cells = rows x cells_per_row[mode]` from a stated table in the module, each entry with its claim and basis: rivalfunds BQL holdings 16
   (site Z's reconstruction `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/BBG_CELL_TRACKING_RECONSTRUCTION_20261005_BLOCK_20261008.md` :84);
   a refdata mode = its producer's field count read from the producer's file as text; a mode not in the table: `cells` null, `claim`
   "absent" -- never defaulted. `channel` per mode (bql / reference / history).
2. `upload(day, dry_run=True)`: target `lib.opal_naming.address("bloomberg","global","bronze","demand_ledger","dt=<day>")` + `/ledger.jsonl`
   (builder output, never typed); writes the day's rows (overwriting the same day: idempotent) only when `dry_run` is False; a dry run
   prints the target and the rows.
3. CLI `python bbg_ledger_upload.py --day YYYY-MM-DD [--apply]`.
4. NEW `data/mdpf/scripts/demque/test_demque_bbg_ledger_upload.py` (fixture jsonl files in a temp dir; S3 stubbed) with exactly these names:
   `test_reads_record_lines_and_converts_rows_to_cells_per_mode`, `test_unknown_mode_is_written_with_claim_absent_not_defaulted`,
   `test_target_is_the_builder_address_for_the_utc_day`, `test_dry_run_writes_nothing`, `test_rerun_of_a_day_is_idempotent`.
5. **The site-Z acts (a pair; `1.0.0_SA_CTO~Z` signs the site-Z half):** read your user's PutObject on the bloomberg ledger prefix; run
   `--apply` once for the latest UTC day that has a `bbg_budget_<day>.jsonl` file; then run AC2 with that day; then schedule the uploader
   daily at site Z after the 07:00 ET pull (read with `comp-schedule`) and name it in your report with its state. If OPAL_BBGTML's
   notebook pull does not call `record()`, name it in the report as a gap (claim held); editing it is not this order.

### ACCEPTANCE

<criterion id="DQ4-t14-AC1" cell_refs="DQ-t-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R4_CHECKS/dq_t14_tests.py</invocation><expect>UPL-OK</expect></criterion>
<criterion id="DQ4-t14-AC2" cell_refs="DQ-t-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R4_CHECKS/dq_t14_ledger.py</invocation><expect>LEDGER-OK</expect></criterion>
`DQ4-t14-AC1` -- the five named tests. `DQ4-t14-AC2` -- after the first --apply at site Z: rows exist under the builder ledger home for that day, each with its claim.

<expected_criteria>DQ4-t14-AC1,DQ4-t14-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `UPL-BAD no file ...`; `LEDGER-BAD 0 rows ...` (the ledger home is empty at the cut).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **The uploader never calls Bloomberg;** it reads files `record()` already wrote.
- **The S3 write and the site-Z schedule are this order's WORLD acts,** under the pair and a change-management entry opened at start and closed at completion (CLAUDE.md NEVER-2).
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-Z-W1-S<k>`, `fabric` `site-z`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/bbg_ledger_upload.py
data/mdpf/scripts/demque/test_demque_bbg_ledger_upload.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 4), cell `DQ-t-14`.
<owned_cells>DQ-t-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ4-t14-AC1, DQ4-t14-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.7.0_AE_CloudOps~ZQ/MDPF_DEMQUE.TO-DQ-t14.sitez-demand-ledger-uploader.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ4-t14-AC1,DQ4-t14-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE at the cut: no schedule exists yet; the seat reads comp-schedule at site Z when it schedules the uploader (step 5) and names it in the report.
comp-iam: DECLARED-NOT-APPLICABLE at the cut: the writer is a site-Z user, unreadable from dell1; the seat reads its PutObject on the bloomberg demand_ledger prefix at site Z before the first write (step 5).
comp-adversary: DECLARED-NOT-APPLICABLE the uploader writes a new, additive prefix nothing serves.
risk: WORLD -- a site-Z S3 write and a scheduled job, under a pair (CTO~Z signs the site-Z half).
direct_act: false -- a seat order, one issuer (dell1 MDPF_DEMQUE COO), per site Z ruling 32309.
</preflight>

Source: PRD v0.3 FWD-2, FWD-3, C-CELL, C-METER, C-RESERVE, C-SITES; site Z ruling 32309 (msg 1532); CTO msg 1536 item 6; decomposition round 4.
