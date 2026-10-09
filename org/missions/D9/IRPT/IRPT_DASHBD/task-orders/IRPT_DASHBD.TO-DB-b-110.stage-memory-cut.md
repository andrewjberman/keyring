# TO IRPT_DASHBD.TO-DB-b-110 -- E2: measure the gold Lambda's peak memory per stage on the heaviest kit day, then cut the largest stage's peak in the producer, with a test -- ships in the gold release with DB-b-97/104 under that pair

<to_id>IRPT_DASHBD.TO-DB-b-110</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~85</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>55</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 20 and ADDENDUM 19 item 2, enrichment item E2 | **Decomp cell:** `DB-b-110` (decomposition section 57) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-107 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-85`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~85/`.

**THE CLIENT-DATA RULE (binding):** evidence carrying account numbers or client figures is written OUTSIDE the repo, under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/<your serial>/`. The repo carries counts, sha256 and reason codes only, and account tokens in the
`acct#<sha256("49financial:<account>")[:8]>` form. Never print an account number in a commit message, a record, a row or a report.

**The cell (`DB-b-110`).** The CTO ruled (ADDENDUM 18, ADDENDUM 20 item 2) that the producer fix is owed and preferred: measure, then cut the largest
stage's peak. The live run reads 1,685 MB of 2048 on 2026-10-08.

In `C:/dev/wk-irpt-dashbd-85`:
1. **Measure.** Run the handler's stages locally on the 2026-10-08 kit, as `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~50/kit_run_day.py` does (S3 GETs only).
   Record each stage's peak memory: returns, class, lots realized, lots unrealized, activity, and the status write. Use RSS or tracemalloc, and say
   which. Name the largest.
2. **Cut it** in its producer:
   - `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`;
   - `account_return_daily.py`, `account_class_daily.py`;
   - or `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`;

   whichever owns the stage. Examples of a cut: streaming or chunking, dropping columns early, freeing frames between stages, narrower dtypes. The
   rows must be byte-equal: hash the stage's output before and after on the kit day.
3. **Test** that the cut stage's output is unchanged on a fixture, and keep every existing test passing.
4. Record `STAGE_MEMORY.json` {method, stages: [{stage, peak_mb}], largest_stage, before: {largest_stage_peak_mb}, after: {largest_stage_peak_mb},
   output_hash_equal: true, tests: {passed, failed, new_test}}. It holds no account number.

No deploy: this ships in the gold release with DB-b-97/104 (R45) under that pair.

<criterion id="DB55-2-AC1" cell_refs="DB-b-110"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r55/p55_round55.py" . DB55-2-AC1</invocation><expect>DB55-2-AC1 PASS</expect></criterion>
`DB55-2-AC1` -- per-stage peaks are measured on a kit day and the largest stage's peak falls after the cut, tested. Base: FAIL.

<expected_criteria>DB55-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** S3 GETs for the kit day; you edit the producer or handler that owns the largest stage, and its tests. No deploy.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~85/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~85/
data/assets/scripts/gold/irpt_reporting/
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-110.stage-memory-cut.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 57 (round 55), cell `DB-b-110`.
<owned_cells>DB-b-110</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB55-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~85/IRPT_DASHBD.TO-DB-b-110.stage-memory-cut.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB55-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the per-stage peaks, the largest, the cut and its byte-equality, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the producer stage with the largest memory peak; ships later in the R45 gold release under its pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 GETs only; no write, no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB55-2-AC1 FAIL at base (no record). CTO ADDENDUM 18, ADDENDUM 20 item 2.
lane: the <paths> block IS the grant.
</preflight>
