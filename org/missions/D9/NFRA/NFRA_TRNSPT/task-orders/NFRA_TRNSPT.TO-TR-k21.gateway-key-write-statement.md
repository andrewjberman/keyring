# TO NFRA_TRNSPT.TO-TR-k21 -- a transcripts-key WRITE statement for the gateway role (FWD-6 un-park), plan-only

<to_id>NFRA_TRNSPT.TO-TR-k21</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>keys</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-k-21` (`decompositions/NFRA_TRNSPT_DECOMP_R21.md`, AMENDMENT 3) | **outcome_ref:** FWD-6 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-k-21`: site Z's gateway will copy a market-update deck (.pptx) into `opal-data-transcripts`, which is encrypted under the transcripts key
`aws_kms_key.transcripts` (`infra/aws/terraform/transcripts/main.tf`). The key policy gives use only to named principals. The gateway's role,
`opal-gateway-role`, needs to WRITE: `kms:GenerateDataKey` and `kms:Encrypt`. The model is the existing statement `DellAgentUsersGenerateDataKey`
(read it in main.tf), conditioned to S3 in us-east-1 and to this bucket's ARN as the encryption context (the bucket has a Bucket Key).

**Build (plan-only; you apply nothing):**
1. In `infra/aws/terraform/transcripts/main.tf`, resolve the gateway role through a `data "aws_iam_role"` block. Take its name from a
   source the estate already has, in this order: a NAMES/registry entry, or an output/local of the opal-gateway root, under
   `infra/aws/terraform/opal-gateway/`. Read how that root names it. If the only way is a bare literal and the commit-time naming gate refuses
   it, add nothing typed: file a surprise row (`NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under `surprise-channel/`) and stop.
2. Add ONE key-policy statement `GatewayWritesTranscripts`: Effect Allow, Principal = that role's ARN, Action
   `["kms:GenerateDataKey", "kms:Encrypt"]`, Resource `*`, Condition StringEquals `kms:ViaService` = `s3.us-east-1.amazonaws.com` and
   `kms:EncryptionContext:aws:s3:arn` = `aws_s3_bucket.transcripts.arn`. Change NO other statement.
3. New `data/transcripts/scripts/tests/test_gateway_key_write.py`. It parses the .tf text: no AWS, no terraform.
   - `test_gateway_write_statement_shape`: exactly that Sid, those two actions, the principal from the data source.
   - `test_gateway_write_scoped_to_s3_and_bucket`: both conditions are present.
   - `test_no_other_key_statement_changed`: every other Sid in the key policy is byte-identical to `git show HEAD~0:` of the base commit
     named below. Read the base text from a fixture you write from that commit.

### ACCEPTANCE

<criterion id="TR21-k21-AC1" cell_refs="TR-k-21"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R21_CHECKS/r21_checks.py k21</invocation><expect>R21-K21-OK</expect></criterion>
`TR21-k21-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR21-k21-AC1</expected_criteria>

Dry-run at the base (box/dell2 at issuance): `R21-K21-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **Plan-only.** No `terraform plan` against live state, no apply, no AWS call. `terraform fmt` / `validate` are allowed if the binary exists.
- No transcript, email or client content anywhere.

<paths>
infra/aws/terraform/transcripts/main.tf
data/transcripts/scripts/tests/test_gateway_key_write.py
data/transcripts/scripts/tests/fixtures/
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R21.md</decomp_doc> (round 21, AMENDMENT 3), cell `TR-k-21`.
<owned_cells>TR-k-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR21-k21-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-k21.gateway-key-write-statement.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR21-k21-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** where the role name comes from, the statement as written, the test names, the check line, commits, any row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: RUN -- a NEW writer principal on the transcripts key (GenerateDataKey + Encrypt, via S3 to this bucket only); the gateway's S3 PutObject grant is site Z's role policy; applied later under a never-widen pair at the laptop (key admin).
comp-adversary: RUN -- sources: site Z ruling @14cbf27dec (msg 3560), main.tf key policy; BLIND to live state. Traps: a typed ARN or name, a missing ViaService/context condition (would let the role encrypt anything), an edit to another statement (a18/s21/Dell statements must stay byte-identical); the three tests fix each.
lane: the paths block.
</preflight>

Source: MSTR~DELL2 msg 3560 relaying 1.0.0_SA_CTO~Z @14cbf27dec; decomposition round 21 AMENDMENT 3, cell TR-k-21.
