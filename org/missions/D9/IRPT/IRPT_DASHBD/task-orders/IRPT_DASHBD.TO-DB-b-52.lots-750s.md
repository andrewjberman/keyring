# TO IRPT_DASHBD.TO-DB-b-52 -- E3 (W27-S2): the lots stage's full run over 7,604 accounts at or under 750 s; the chosen batch size set as the producer's default

<to_id>IRPT_DASHBD.TO-DB-b-52</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~31</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-28 analysis @e9b17e6e75
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_28_20261008.md` section 2, item E3; row W27-S2) |
**Decomp cell:** `DB-b-52` (decomposition section 31) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-48 (complete, merged @24d088b96e).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-31`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~31/`.

**The cell (`DB-b-52`).** Round 28 (DB-b-48, record `deliverables/0.9.0_WK_IRPT_DASHBD~27/BATCHED_E2.json`, runner `batched_e2_run.py`
beside it) batched the lots stage of the extended reporting-gold handler (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`,
`--local` mode, `--batch-size`; producer `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`, `DEFAULT_BATCH_SIZE = 1000`
at line 1138). Over 7,604 accounts for 2026-10-06 it measured: batch 250, lots 684.61 s, total 905.67 s (over the 900 s limit); batch
1,000, lots 495.54 s, total 768.91 s. The lots peak was flat at about 1.7 GB. The target is a full run (all three stages, `total`) at
**<= 750 s**.

1. Re-run the extended handler's `--local` mode over the handler's own population for 2026-10-06, one process per run, at batch sizes
   above 1,000 (for example 2,000 and 4,000; 0 means one batch, and may be one of them). Reuse round 28's runner by import or by
   invocation; do not restate it. Per run record: `batch_size`, `lots` {wall_seconds, peak_mb}, `total` {wall_seconds, peak_mb}.
   Stop a run that passes 3,600 s and record it.
2. Choose the batch size whose `total` is <= 750 s with the lowest lots `peak_mb`; write it as `chosen_batch_size`. Set the producer's
   `DEFAULT_BATCH_SIZE` to it; keep the line's form `DEFAULT_BATCH_SIZE = <int>`. The producer's tests must still pass
   (`python -m pytest -q data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py`).
3. Run once more with NO `--batch-size` argument (the new default) and record it as `default_run` {batch_size_arg: null, total
   {wall_seconds, peak_mb}, lots {wall_seconds, peak_mb}, lots_stage_completed}.
4. Write `LOTS_750_E3.json`: `population_count`, `accounts_run`, `lots_stage_completed`, `runs`, `chosen_batch_size`, `default_run`,
   `limits` {target_s: 750, timeout_s: 900, memory_mb: 2048}, `handler_sha256` and `producer_sha256` (sha256 of the files' bytes at your
   final commit), and the machine (cores, RAM, workers, pandas, python). Write `LOTS_750_E3.md`, COUNTS ONLY.
   If no batch size reaches 750 s, do not lower the bar: record every run, leave the default unchanged, and file a row.

<criterion id="DB29-3-AC1" cell_refs="DB-b-52"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . DB29-3-AC1</invocation><expect>DB29-3-AC1 PASS</expect></criterion>
`DB29-3-AC1` -- the full population; a run at the chosen batch size whose total is <= 750 s, with the lots peak printed. Base: FAIL.

<criterion id="DB29-3-AC2" cell_refs="DB-b-52"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r29/p29_round29.py" . DB29-3-AC2</invocation><expect>DB29-3-AC2 PASS</expect></criterion>
`DB29-3-AC2` -- the producer's DEFAULT_BATCH_SIZE equals the chosen size; the default run (no argument) reads <= 750 s; the recorded sha256s equal HEAD's bytes. Base: FAIL.

<expected_criteria>DB29-3-AC1,DB29-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The handler and round 28's runner are read, never edited.
- **AWS:** S3 reads only. No S3 write, no Lambda invoke, no deploy, no vendor call, no bun, no download of any package, script or program.
- **Refusal clause.** An S3 write, a deploy, a memory or timeout change in any infrastructure file, a relaxed refusal for true duplicates,
  a target other than 750 s, or a client figure in a committed `.md` is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~31/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-52.lots-750s.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 31 (round 29), cell `DB-b-52`.
<owned_cells>DB-b-52</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB29-3-AC1, DB29-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~31/IRPT_DASHBD.TO-DB-b-52.lots-750s.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB29-3-AC1,DB29-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, every run's timings and peaks, the chosen size, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a local re-run and one constant in the producer; nothing is deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB29-3-AC1 and AC2 base FAIL (no record) at base 62a01a0c61; DEFAULT_BATCH_SIZE = 1000 at HEAD.
lane: the <paths> block IS the grant.
</preflight>
