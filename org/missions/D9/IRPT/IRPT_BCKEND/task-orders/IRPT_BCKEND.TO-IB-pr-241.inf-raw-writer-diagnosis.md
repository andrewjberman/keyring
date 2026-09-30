# TO IRPT_BCKEND.TO-IB-pr-241 -- Name the Inflection RAW bronze writer and why it stopped after 2026-09-27

<to_id>IRPT_BCKEND.TO-IB-pr-241</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~81</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO 102951 + 102969 (S216 is ~P's; the July DOOR 5 hold is no
longer in force; diagnose before restarting anything) | **Decomp cell:** `IB-pr-241` (decomposition section 22) |
**outcome_ref:** FWD-3 (INF) | **depends_on:** none

---

## WORKER FACE

**The cell.** Inflection's RAW Orion files stopped landing after 2026-09-27. In bucket `opal-data-inf`:
- `bronze/positions/`, `bronze/transactions/` and `bronze/performance/` carry `<date>.jsonl.gz` through 2026-09-27 and
  none after.
- For positions, `bronze/positions/2026-09-28.parquet` and `2026-09-29.parquet` exist. Those are the COERCED copies,
  which Lambda `inf-api-positions` writes at about 11:25Z. Its CloudWatch log shows "S3:
  s3://opal-data-inf/bronze/positions/<date>.parquet".
- The raw `.jsonl.gz` files landed later each day (positions about 11:51Z, transactions about 11:41Z, performance about
  11:48Z), so a DIFFERENT writer produced them.
- Because only parquet exists, `opal-assets-ingest-mirror` refuses to mirror those days (Ruling 16: raw only;
  `COERCED_SUFFIXES = (".parquet",)`). No Inflection bronze or silver `fact_positions` exists in `opal-data-assets` after
  09-27, and the Inflection holdings producer and adapter switch are blocked (row IRPT_BCKEND-S216).

**Your work, diagnosis first (restart NOTHING):**
1. **Find the raw writer.** Name the Lambda, EC2 chain or SSM document that wrote `bronze/{positions,transactions,
   performance}/<date>.jsonl.gz` through 2026-09-27. Candidates to read first:
   - the `inf-ec2-*` Lambdas (`inf-ec2-retry-launch`, `inf-ec2-launch-monitor`) and their launched instance's logs;
   - `inf-bronze-trigger`;
   - any writer whose CloudWatch logs name those keys.
   Use S3 object metadata and CloudWatch logs (read-only).
2. **Establish why it stopped.** Find its last success (09-27) and what happened on 09-28 and 09-29: an error, no
   launch, a changed trigger, or a disabled schedule. Cite the log group and lines, and any commit that touched it.
   Fabric history:
   - raw was restarted 08-14 (commit 5fdbe38637, "RAW LANDED ... bronze hole healed");
   - INF-REDEPLOY closed 09-01 (69a15bf90e).
3. **Record it** in `C:/Users/AndrewBerman/Desktop/wk-irpt-p-81/org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~81/RAW_WRITER_DIAGNOSIS.json`
   with exactly these fields:
   - `raw_writer` as `{"kind": "lambda"|"launch_template"|"ssm_document"|"ec2_instance", "name": "..."}`;
   - `last_raw_date` as `YYYY-MM-DD`;
   - `stop_cause`, one sentence;
   - `evidence`, a list of at least 3 items, each naming a log group, S3 key or commit;
   - `restart_path`: what a restart or fix would change, and that it goes under a ledger with both halves.
4. **Correct the stale comment.** In
   `C:/Users/AndrewBerman/Desktop/wk-irpt-p-81/infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py`,
   replace the DOOR 5 paragraph's claim that restarting the raw producer is "NOT ruled, NOT recommended, NOT yours".
   Write that the July hold was lifted, citing 5fdbe38637 and 69a15bf90e, and 1.0.0_SA_CTO 102969. Keep Ruling 16 and
   everything else in the file byte-identical.

<criterion id="P24-1-AC1" cell_refs="IB-pr-241"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r24/p24_1_ac1_raw_writer_diagnosis.py" .</invocation><expect>P24-1-AC1 PASS</expect></criterion>
`P24-1-AC1` -- the record's fields are present; its `last_raw_date` equals the newest raw positions date in S3; and its
`raw_writer` exists (get_function / describe). Base: FAIL (record absent).

<criterion id="P24-1-AC2" cell_refs="IB-pr-241"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r24/p24_1_ac2_mirror_door5_comment.py" .</invocation><expect>P24-1-AC2 PASS</expect></criterion>
`P24-1-AC2` -- the stale sentence is gone, both commits are cited, Ruling 16 is unchanged, and the file compiles. Base:
FAIL.

<expected_criteria>P24-1-AC1,P24-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. The comment edit is the ONLY
  code change.
- **Read-only against AWS.** You may read S3, CloudWatch, Lambda, EC2, SSM and EventBridge configuration. You may NOT
  launch, invoke, redeploy, enable a schedule, write S3 or backfill. The restart is a later cell under both halves.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken a check.

<paths>
infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 22 (round 24, workstream ~P), cell `IB-pr-241`.
<owned_cells>IB-pr-241</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P24-1-AC1, P24-1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~81/IRPT_BCKEND.TO-IB-pr-241.inf-raw-writer-diagnosis.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P24-1-AC1,P24-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, each criterion's last line, the raw writer and stop cause in one line
each, and any surprise row id (`IRPT_BCKEND-W81-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order changes no schedule; reading the raw writer's trigger is part of the diagnosis itself, and nothing is enabled.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; the worker's AWS use is read-only.
comp-blast: RUN -- the only write is a comment in the ingest mirror's source (no deploy); the served INF path is untouched.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- P24-1-AC1 base FAIL (record absent); P24-1-AC2 base FAIL (the stale sentence present, no citations); the S3 read in AC1 prints the newest raw date (2026-09-27 at the cut).
lane: the <paths> block IS the grant. Why the CTO's inf-api-{positions,txn,performance}/** is not the grant: inf-api-positions writes the PARQUET copy (its own log), not the raw file, so the raw writer is unnamed until this cell names it; the fix cell will grant it.
</preflight>
