# TO IRPT_BCKEND.TO-IB-m21-211 -- The cot login box's RUNNING script becomes its build input (row S166)

<to_id>IRPT_BCKEND.TO-IB-m21-211</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.6.2_AE_PartnerETL~S</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-211`
(`decompositions/IRPT_BCKEND_DECOMP_R21_M.md`) | **outcome_ref:** FWD-1 (COT Performance hop) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-211` -- row `IRPT_BCKEND-S166` (yours, filed on TO-IB-s158): the cot login box `i-0643a5bee8a8feabf` runs
`/opt/bd-cot-auto-login/bd_49f_auto_login.js` (md5 28dd27a054b826cc3a87f6b4498d3b5a, 35,049 B), but
`infra/aws/ec2/bd-cot-auto-login/` holds only `run-bd-auto-login.sh` and `secret-ids.env` -- no `.js`. A future
S3 -> box redeploy from that directory would not reproduce the running script. The CTO ruled (round-19 analysis
`org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round19.md` section 3): first commit the RUNNING bytes as the
build input, with no behaviour change.

### BUILD

1. Read the running file off the box (one read-only SSM command: `md5sum` and `wc -c` of
   `/opt/bd-cot-auto-login/bd_49f_auto_login.js`, then its bytes), and confirm md5 28dd27a0... / 35,049 B.
2. Write those exact bytes to `infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js` (byte-for-byte; no line-ending or
   encoding change -- compare the md5 after writing). If the S3 deploy source for `/opt/bd-cot-auto-login` also lacks
   the `.js`, record that in your report; do NOT upload anything in this order.
3. Write `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S166_RUNNING_VS_REPO_20260929.json` as
   `{"command_id": "<the SSM read's id>", "running_md5", "running_bytes", "repo_md5"}`. Commit both. The box is not
   changed.

### ACCEPTANCE

<criterion id="IBM21-211-AC1" cell_refs="IB-mr-211"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R21_CHECKS/r21_s166_build_input.py</invocation><expect>BUILD-INPUT followed by the first 12 hex of the running md5</expect></criterion>
`IBM21-211-AC1` -- the repo carries the running bytes, and an SSM read shows the box still runs them.

<expected_criteria>IBM21-211-AC1</expected_criteria>

Dry-run at the base 2026-09-29 04:3xZ: NO-BUILD-INPUT: the repo .js absent (FAIL as expected).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Read-only on the box and in S3.** One SSM read command; no upload, no box write, no service restart.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-S<next>` under your serial), and do not weaken the test to pass.

<paths>
infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js
org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S166_RUNNING_VS_REPO_20260929.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R21_M.md</decomp_doc> (round 21, workstream ~M), cell `IB-mr-211`.
<owned_cells>IB-mr-211</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM21-211-AC1. Instance at `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND.TO-IB-m21-211.cot-login-script-build-input.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM21-211-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~M`: the running md5/bytes, the repo md5, the SSM command id, the commit hash,
and whether the S3 deploy source carries the `.js`.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- scheduler cot-bd-session-daily-et (cron 07:30 America/New_York) fires the document that runs this script; this order changes neither.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change; one SSM read.
comp-adversary: RUN -- 1 directory listed (infra/aws/ec2/bd-cot-auto-login: 2 files, no .js) and 1 row read (S166: running md5 28dd27a0 vs 49F repo 15fd5ef9); BLIND: the S3 deploy source's contents were not listed at the cut (the order records them).
lane: the <paths> block IS the grant; issued to the seat the CTO named (analysis s.3).
</preflight>

Source: CTO round-19 analysis (@d797a87872) section 3 row S165/S166, section 6 item 2.
