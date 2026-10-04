# NFRA_OPLGTW task order -- `OG-o-5` -- runbook section 7: the rollback text tells the truth about the schwab flag

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-o-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~21</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a runbook text change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE -- the remedy is the CVO's (OGO2-J1, ADJUDICATION_v4.Z.md @d4c58bd8ef), accepted by the CTO as R7 (ROUND_ANALYSIS.round14.md section 6 @2f46788988).
EGRESS CLASS, declared: NONE -- local text; one read of the live host's HEALTH output if you choose to verify the 7.3 command, through Opal's own gateway.
</preflight>

## 1. THE CELL -- `OG-o-5` (decomposition addendum R3-T.9, item 3; drafted under R3-T.8.1)

The CVO graded OGO2-J1 FAIL, narrowed to `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md` section 7, with
two defects:

- **7.1.** Its on-box disable (remove `schwab` from `ENABLED_INTEGRATIONS` in the host `.env`) is undone by the next
  deploy. `deploy-to-ec2.sh` re-renders `.env` from its fixed template, and every recorded release lists `schwab`.
- **7.2.** Step 2's rollback targets fail that step's own test: every recorded release renders `schwab`.

Make the text-only remedy the CTO accepted, as exactly these edits. Each carries the anchor the check reads, written
verbatim:

1. **7.1:** add a sentence beginning `The deploy template re-renders \`schwab\`` (with the backticks). It says that the
   deploy template writes `ENABLED_INTEGRATIONS` with `schwab` at EVERY deploy, so this disable lasts only until the
   next release, and that after any deploy the operator re-applies 7.1 and re-confirms `integration_enabled`.
2. **7.2 step 2:** replace the test that no target can pass with a true one. Every recorded release renders `schwab`,
   so immediately after any restore the operator must `re-apply 7.1` and confirm `` `integration_enabled=false` `` on
   HEALTH before the restore counts as done. Keep R-56's two target conditions as they are.
3. **7.3:** add a line beginning `Read command:` naming the exact read-only command that shows
   `HEALTH.checks.integration_enabled` (the section-5 status command, written out). No secret appears in it.

Change nothing else in the runbook; sections 0-6 and 8 passed J1. Keep `rb.AC1`-`rb.AC3` passing.

## AMENDMENT A1 (2026-10-03 ~23:1xZ, issuer; CTO msg 29057 on the CVO's L9 re-grade, ADJUDICATION_v6.Z.md)

OGO2-J1 re-graded FAIL, narrowed to 7.3. 7.1 and 7.2 now PASS. The defect is this order's own: item 3 said "name the
exact read-only command that shows `HEALTH.checks.integration_enabled`" for 7.3. But 7.3 is the A15 SOURCE-BUCKET
readback, and that command reads no bucket setting. Replace item 3 with:

3'. **Move** the `Read command:` line (`cd infra/aws/ec2/opal-gateway && python ops/schwab_status.py`, `--json` for the
    machine copy) out of 7.3 and into **7.1 step 3**, where HEALTH is read. 7.2 step 2 refers to it.
3''. **7.3** names the four read-only bucket reads, each with `--bucket opal-data-assets`, as one line beginning `Bucket
    reads:`:
    - `aws s3api get-bucket-versioning`
    - `aws s3api get-bucket-encryption`
    - `aws s3api get-public-access-block`
    - `aws s3api get-bucket-policy-status`
    **Delete** the sentence "This runbook does not run the AWS read itself ..." (it now contradicts the line). The
    baseline values and the pass/fail rule stay as they are.

The check `r15/checks/o5.AC1.sh` is amended to grade A1:
- 7.1 carries `schwab_status.py`;
- 7.3 carries `Bucket reads:` and all four reads with `--bucket opal-data-assets`;
- 7.3 carries neither `schwab_status.py` nor "does not run the AWS read".
Every other anchor and `rb.AC1`-`AC3` stay.

## 2. BOUNDS

- **Edit ONLY** the runbook.
- **No:** deploy, `.env` change, flag change, or code change. The host-side flag is a LATER release, ruled not to be cut
  before G-E.
- **Never:** push, merge, rebase, stash, `checkout --` or `clean`; override a gate.
- Commit with `.tools/safe-commit.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W21-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-o-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r15/checks/o5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)7.1 re-render anchor True; 7.2 re-apply \+ integration_enabled=false anchors True; 7.1 status read True; 7.3 four bucket reads True; 7.3 no HEALTH read and no "does not run" True.*rb.AC1-AC3 passing 3 of 3.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three anchors landed in their sections, and the runbook's existing checks still pass.
- `J1` (judgment, NOT self-graded): OGO2-J1 re-run at L9 by `3.0.0_SA_CVO~O` on the new section 7. Record it as
  `UNVERIFIABLE-BY-INSTRUMENT`, reserved to the CVO.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/NFRA_OPLGTW.TO-OG-o-5.runbook-section7-remedy.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If AC1 PASSes, edit this order's ONE `<status>complete</status>
<round>16</round>
<slot>~21</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
