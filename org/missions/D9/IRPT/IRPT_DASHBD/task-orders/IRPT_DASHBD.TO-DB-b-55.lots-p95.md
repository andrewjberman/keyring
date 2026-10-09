# TO IRPT_DASHBD.TO-DB-b-55 -- E3 (W31-S2): the full run's p95 over >= 5 runs at the default batch size is <= 750 s, or the default is lowered until it is

<to_id>IRPT_DASHBD.TO-DB-b-55</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~33</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-29 analysis @72ae174b3c item
E3 (row W31-S2) | **Decomp cell:** `DB-b-55` (decomposition section 32) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-52 (merged
@50a0ebae91).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-33`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~33/`.

**The cell (`DB-b-55`).** Round 29 (DB-b-52, record `deliverables/0.9.0_WK_IRPT_DASHBD~31/LOTS_750_E3.json`, runner
`lots_750_run.py` beside it) set the lots producer's `DEFAULT_BATCH_SIZE = 2000`
(`data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`). The full extended reporting-gold run over 7,604 accounts for
2026-10-06 read 757.55, 692.81 and 666.98 s at that size: the 750 s bar sits inside run-to-run spread (row W31-S2). This cell measures
the spread.

1. Run the extended handler's `--local` full run with NO `--batch-size` argument (the producer's default), one process per run, at
   least FIVE times. Reuse round 29's runner (`lots_750_run.py`, its `default` mode) by import or by invocation; do not restate it. Per
   run record `batch_size` (the default in effect), `lots_stage_completed`, `lots` {wall_seconds, peak_mb}, `total` {wall_seconds,
   peak_mb}. Stop a run that passes 3,600 s and record it.
2. The bar is the p95 of the runs' `total` wall_seconds (linear interpolation) <= 750 s. If it is over, lower `DEFAULT_BATCH_SIZE`
   (keep the line's form `DEFAULT_BATCH_SIZE = <int>`) and repeat step 1 at the new default until the bar holds. The producer's tests
   must still pass (`python -m pytest -q data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py`). If it holds at
   2000, change nothing.
3. Write `LOTS_P95_E3.json` (`population_count`, `runs` -- every run, including any at an earlier default -- `p95_total_s`,
   `default_batch_size`, the machine and the other load present) and `LOTS_P95_E3.md`, COUNTS ONLY.

<criterion id="DB30-3-AC1" cell_refs="DB-b-55"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . DB30-3-AC1</invocation><expect>DB30-3-AC1 PASS</expect></criterion>
`DB30-3-AC1` -- at least 5 completed full runs over >= 7,000 accounts at the batch size equal to the producer's DEFAULT_BATCH_SIZE at HEAD. Base: FAIL.

<criterion id="DB30-3-AC2" cell_refs="DB-b-55"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . DB30-3-AC2</invocation><expect>DB30-3-AC2 PASS</expect></criterion>
`DB30-3-AC2` -- the p95 of those runs' total time, computed by the check, is <= 750 s. Base: FAIL.

<expected_criteria>DB30-3-AC1,DB30-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The handler and round 29's runner are read, never edited.
- **AWS:** S3 reads only. No S3 write, no Lambda invoke, no deploy, no vendor call, no bun, no download of any package, script or program.
- **Refusal clause.** An S3 write, a deploy, a memory or timeout change in any infrastructure file, a bar other than p95 <= 750 s over
  >= 5 runs, or a client figure in a committed `.md` is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~33/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-55.lots-p95.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 32 (round 30), cell `DB-b-55`.
<owned_cells>DB-b-55</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB30-3-AC1, DB30-3-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~33/IRPT_DASHBD.TO-DB-b-55.lots-p95.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB30-3-AC1,DB30-3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, every run's timings, the p95, the default in effect, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: local re-runs and at most one constant in the producer; nothing deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB30-3-AC1 and AC2 base FAIL (no record) at base 74730695dc; positive control on planted runs PASS (p95 718.0 s over 5).
lane: the <paths> block IS the grant.
</preflight>
