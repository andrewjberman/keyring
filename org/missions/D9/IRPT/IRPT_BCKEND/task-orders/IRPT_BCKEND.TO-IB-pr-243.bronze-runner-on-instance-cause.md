# TO IRPT_BCKEND.TO-IB-pr-243 -- Why the recovered inf-bronze-runner wrote no raw file on 2026-09-28

<to_id>IRPT_BCKEND.TO-IB-pr-243</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~86</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** row S216 and WK~81's diagnosis (TO-IB-pr-241, drained @0b5cdb06f9);
1.0.0_SA_CTO 102969 | **Decomp cell:** `IB-pr-243` (decomposition section 23) | **outcome_ref:** FWD-3 (INF) |
**depends_on:** none

---

## WORKER FACE

**The cell.** EC2 instance `i-083ad9ae297f88e9f` (`inf-bronze-runner`) writes Inflection's raw Orion files
(`s3://opal-data-inf/bronze/{positions,transactions,performance}/<date>.jsonl.gz`). Its service `inf-bronze-fetch`
runs code the instance pulls from `s3://opal-data-inf/code/bronze-runner/`. The repo copies are in
`C:/Users/AndrewBerman/Desktop/wk-irpt-p-86/infra/aws/ec2/inf-bronze-runner/` (for example `inf-bronze-fetch.sh`) and
`C:/Users/AndrewBerman/Desktop/wk-irpt-p-86/data/inf/scripts/bronze/orchestrator.py`.

What happened:
- On 2026-09-28 the daily start failed (`Server.InternalError`).
- `inf-ec2-retry-launch` recovered the instance to `running` by 11:15:55Z (CloudWatch `/aws/lambda/inf-ec2-retry-launch`).
- Even so, NO raw file landed for 09-28. The raw pull scripts' `s3://opal-data-inf/orion/rate_limit_state_transactions.json`
  and `rate_limit_state_performance.json` stayed stamped 2026-09-27.
- The instance's journal is not shipped to CloudWatch.

**Your work (read-only):**
1. **Compare deployed against repo.** For each file the instance pulls, record the S3 sha256 against the repo file's
   sha256, with a verdict.
2. **Find the path.** Read the service script and the orchestrator for a path that reaches `running` yet writes no raw
   file. Candidates: a date or "already done" guard, a stale lock or state object, a sentinel it waits on, a dependency
   on the same-morning parquet, or an exit it takes when started late or twice.
3. **Read S3 side effects.** Look at any the service leaves (state files, markers, logs uploaded to S3, run manifests)
   around 09-27 and 09-28.
4. **Record** `C:/Users/AndrewBerman/Desktop/wk-irpt-p-86/org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~86/ON_INSTANCE_DIAGNOSIS.json`
   with these fields:
   - `deployed_vs_repo`: a list of `{s3_key, s3_sha256, repo_path, repo_sha256, verdict}`;
   - `evidence`: a list of at least 3 items, each naming an S3 key, a log group or a `file:line`;
   - EITHER `cause`, a paragraph with `file:line` citations of the code path;
   - OR `needs_instance_read: true` with `reason`, plus `ssm_commands` to run on the instance, including a
     `journalctl -u inf-bronze-fetch ...` read.
   A named "cannot be seen without the journal" is a legal answer; a guess is not.

<criterion id="P24-3-AC1" cell_refs="IB-pr-243"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r24/p24_3_ac1_on_instance_cause.py" .</invocation><expect>P24-3-AC1 PASS</expect></criterion>
`P24-3-AC1` -- the record's `deployed_vs_repo` sha256 is re-confirmed against S3 (an instrument control); the `cause`
citations exist in the worktree, or `needs_instance_read` names a journal command; and the record has at least 3
evidence items. Base: FAIL (record absent).

<expected_criteria>P24-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. No code change.
- **Read-only against AWS.** You may read S3, CloudWatch, EC2 and SSM configuration. You may NOT start or stop the
  instance, send an SSM command, invoke a Lambda, or write S3. Starting it to read the journal is the issuer's act,
  under a ledger and both halves.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the check.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 23 (round 25, workstream ~P), cell `IB-pr-243`.
<owned_cells>IB-pr-243</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P24-3-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~86/IRPT_BCKEND.TO-IB-pr-243.bronze-runner-on-instance-cause.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P24-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, the cause (or what the journal read must
show) in two lines, and any surprise row id (`IRPT_BCKEND-W86-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order changes no schedule; the trigger is read, not moved.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; read-only.
comp-blast: RUN -- no write of any kind outside the worker's deliverables folder.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- P24-3-AC1 base FAIL (record absent); the check re-reads one recorded S3 object's sha256 (instrument control) and verifies every cited file:line exists.
lane: the <paths> block IS the grant.
</preflight>
