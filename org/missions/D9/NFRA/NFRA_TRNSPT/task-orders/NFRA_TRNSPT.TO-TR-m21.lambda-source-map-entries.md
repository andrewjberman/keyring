# TO NFRA_TRNSPT.TO-TR-m21 -- source-map entries for the transcripts root's Lambdas (row D2-S12)

<to_id>NFRA_TRNSPT.TO-TR-m21</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-m-21` (`decompositions/NFRA_TRNSPT_DECOMP_R21.md`) | **outcome_ref:** D2-S12 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-m-21` (CTO ADDENDUM 12 item 1): deployment rule 4 wants every Lambda in `infra/aws/lambda/ci/lambda-source-map.json`. None of the
transcripts root's Lambdas is there (row `NFRA_TRNSPT-D2-S12`). The root `infra/aws/terraform/transcripts/` declares 3 `aws_lambda_function`
resources at base: `mail_pull` (mail_pull.tf), `pull` (pull.tf), `commentary` (commentary.tf).

**Build:** one entry under `functions` per resource, keyed by the function's real name, which you read from the terraform locals (never typed
from memory). Copy the shape of an existing entry (for example `mdpf-gold-lambda`):
1. `source_dir`, `files`, `tf_file` (the .tf path), `tf_resource` (`aws_lambda_function.<name>`), `iam_role` (from the same .tf).
2. For a LIVE function (`mail_pull`, `pull`): read it with `aws lambda get-function --function-name <name> --query Configuration.CodeSha256` and
   `aws lambda list-tags`, both read-only. Then set `artifact_sha256` (the 44-char CodeSha256), `last_deployed_at` (LastModified), and
   `last_deployed_commit`: the 40-hex pin named in the function's change ledger under `org/critical_paths/change_management/`. For `pull`
   that is the `nfra-trnspt-p18-teams-pull-first-apply-20261009` entry. Resolve the short pin with `git rev-parse`.
3. For `commentary` (not yet applied; IRPT_ANLREQ.TO-APPLY-t1 holds it): no live fields; `_artifact_note` reads
   `not yet applied (IRPT_ANLREQ.TO-APPLY-t1)`.
4. Bump the file's `_updated` line to name this order. Change no other entry.

If a live Lambda the root owns is NOT an `aws_lambda_function` resource (a module, a data source), or a ledger names no pin, file a surprise row
(`NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`) and keep going.

### ACCEPTANCE

<criterion id="TR21-m21-AC1" cell_refs="TR-m-21"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R21_CHECKS/r21_checks.py m21</invocation><expect>R21-M21-OK</expect></criterion>
`TR21-m21-AC1` -- every `aws_lambda_function` in the root is mapped once; live ones carry the sha and commit; commentary carries its note.

<expected_criteria>TR21-m21-AC1</expected_criteria>

Dry-run at the base (box/dell2 37ad2cddeb): `R21-M21-FAIL ... entries=0` for all 3 -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **Read-only AWS.** `get-function`, `get-function-configuration`, `list-tags` only. No plan, apply, update, tag or invoke. No transcript,
  email or client content anywhere.
- **Refusal clause.** A builder refusal for a name: add nothing typed; file a row and stop that piece.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R21.md</decomp_doc> (round 21), cell `TR-m-21`.
<owned_cells>TR-m-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR21-m21-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-m21.lambda-source-map-entries.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR21-m21-AC1` BEFORE the flip. Commit the map first, then pin.
</proof_of_spec>

**REPORT:** the 3 keys added, each live field with the command that read it, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a build-input record, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only get/list on two functions; no grant change.
comp-adversary: RUN -- sources: CTO ADDENDUM 12 @85498539a5, row D2-S12, the three .tf files, the change ledgers; BLIND to any Lambda the root owns outside an aws_lambda_function resource (the face routes that to a row). Traps: a typed name, a sha read from a ledger instead of the function, an edit to another entry; the check and the face fix each.
lane: the paths block.
</preflight>

Source: CTO msg 3211 (ADDENDUM 12); decomposition round 21 cell TR-m-21.
