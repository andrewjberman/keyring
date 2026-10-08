# TO IRPT_DASHBD.TO-DB-b-48 -- E2 (after DB-b-47): the lots stage processes accounts in bounded batches; the full 7,597-account day re-run at two batch sizes with the lots peak flat (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-48</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~27</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Risk WORLD:** its `<paths>` name the handler (the gate's floor); the analysis classes it LOCAL and the cell applies nothing. | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-27 analysis @7fa28c7d6d (msg 1222) item E2 ("the full 7,597-account day re-run prints the per-stage time and peak memory, with the lots peak flat across batch counts (two batch sizes shown)") | **Decomp cell:** `DB-b-48`
(decomposition section 29) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-47 (same worker, same queue: run it after DB-b-47 is complete; the stage must not refuse).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-27`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/`.

**The cell (`DB-b-48`).** Round 27 (DB-b-46, record `deliverables/0.9.0_WK_IRPT_DASHBD~26/SIZING_S31.json` and `REALIZED_ID_REPEAT_COUNTS.json`) ran the extended reporting-gold handler (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`) over all 7,597 49F accounts for 2026-10-06. The lots stage (`data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`) REFUSED in `realized_rows`: 87 realized lot ids repeat within the day's frame (175 rows, 36 accounts, 0 ids spanning accounts, 0 rows identical in every column), so they are distinct lots sharing an id. Its peak reached at least 2,759.5 MB against the served function's 2,048 MB. This cell bounds its memory.

1. Make the lots stage process accounts in BOUNDED BATCHES (a batch size the handler passes in, with a default), so its peak memory
   does not grow with the population. The tables written must be identical to an unbatched run's on the same accounts (show it on a
   small sample: sha256 of each table, batched vs unbatched). The returns and class stages do not change.
2. Re-run the extended handler's `--local` mode over the handler's own population for 2026-10-06, in one process per run, at TWO batch
   sizes (for example 250 and 1,000 accounts). Record per run: `batch_size`, `lots` {wall_seconds, peak_mb}, `total` {wall_seconds,
   peak_mb}. Write `BATCHED_E2.json`: `population_count`, `accounts_run`, `lots_stage_completed`, `runs`, `limits` {timeout_s: 900,
   memory_mb: 2048}, the sample identity check, `handler_sha256`, `producer_sha256`, and the machine. Stop a run that passes 3,600 s and
   record it. Write `BATCHED_E2.md`, COUNTS ONLY.
3. Change no memory or timeout setting. Whether the batched peak fits 2,048 MB on the served pandas 2.2.3 is graded later by the issuer.

<criterion id="DB28-2-AC1" cell_refs="DB-b-48"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r28/p28_key_batch.py" . DB28-2-AC1</invocation><expect>DB28-2-AC1 PASS</expect></criterion>
`DB28-2-AC1` -- the full population re-run at two batch sizes, lots completed, the lots peak flat (max/min <= 1.25). Base: FAIL.

<expected_criteria>DB28-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. `account_return_daily.py` is read, never edited.
- **AWS:** S3 reads only. No S3 write, no Lambda invoke, no deploy, no vendor call, no bun, no download of any package, script or program.
- **Refusal clause.** An S3 write, a deploy, a relaxed refusal for true duplicates, a memory or timeout change, or a client figure in a
  committed `.md` is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-48.lots-stage-batched.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 29 (round 28, workstream B), cell `DB-b-48`.
<owned_cells>DB-b-48</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB28-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/IRPT_DASHBD.TO-DB-b-48.lots-stage-batched.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB28-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what you changed, the numbers each criterion prints, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a batching change in a producer that serves nothing yet; the handler change is source only; no S3 write, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB28-2-AC1 base FAIL (no record), dry-run at base 7fa28c7d6d 2026-10-08 ~07:3xZ.
lane: the <paths> block IS the grant.
</preflight>
