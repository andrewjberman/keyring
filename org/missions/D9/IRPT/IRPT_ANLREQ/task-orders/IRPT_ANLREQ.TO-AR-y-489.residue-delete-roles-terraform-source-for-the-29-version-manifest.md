# TO IRPT_ANLREQ.TO-AR-y-489.residue-delete-roles-terraform-source-for-the-29-version-manifest -- WRITE AND PROVE OFFLINE the Terraform source of the throwaway delete roles for the 29-version synthetic residue manifest (3 roles, 12 + 12 + 5 versions); nothing is planned, applied or run

<to_id>IRPT_ANLREQ.TO-AR-y-489.residue-delete-roles-terraform-source-for-the-29-version-manifest</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~362</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ148</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-489` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** the clean close of round 43 (synthetic residue of runs 7e-7j removed) | **depends_on:** CTO ruling msg 11928 (IRPT_ANLREQ issues the residue pass, V2's R22 method, own pair; the two run-7J analysis_audit versions go in)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~362`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-362` (branch `wk-IRPT_ANLREQ-362`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~362 <0.9.0_WK_IRPT_ANLREQ~362@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W362-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR489-y-AC1,AR489-y-AC2,AR489-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID. The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it). Do not flip the order to complete before every later edit you intend to make is committed (a status of complete removes your path grant).

### THE CELL (`AR-y-489`, inlined)

*What and why.* The issuer's manifest `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/synthetic_residue_delete_list_supplement_runs7e_7j_20261021.json` (git blob `7963026db44e4760e34bb28f2b21dc141c7c3fac`; 29 `{bucket, key, version_id}` entries, all in `opal-data-irpt`, 27 `STATE_OBJECT` and 2 `AUDIT_RECORD_PLATINUM`) lists synthetic versions that the CloudOps principals cannot delete. The CTO ruled (msg 11928) the pass uses the same method as the TCKT_VNEXT round-22 pass (see `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R22_DELETE/R22_DELETE_PAIR.md` section 2, which succeeded on 42 entries): one throwaway IAM role per chunk of 12 manifest entries, each role allowing ONLY `s3:DeleteObjectVersion` on its chunk's exact object ARNs and ONLY for its chunk's version ids, assumable ONLY by `cloudops-dell2-agent-user`. 29 entries make 3 chunks (12, 12, 5).

*The change.* ONE new file `infra/aws/terraform/investor-reporting/ycharts/irpt_residue_delete_r35.tf` with EXACTLY this content (byte for byte, LF line ends, ASCII; the four explicit blocks of V2's precedent are three here; names are explicit per chunk because a templated name is refused by the naming gate):

```
variable "residue_manifest_path" {
  type = string
}

locals {
  residue = jsondecode(file(var.residue_manifest_path)).objects
  chunks  = chunklist(local.residue, 12)
}

resource "aws_iam_role" "irpt_residue_delete_0" {
  name                 = "irpt-residue-delete-0-role"
  max_session_duration = 3600
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Effect = "Allow", Action = "sts:AssumeRole",
                   Principal = { AWS = "arn:aws:iam::313476888478:user/cloudops-dell2-agent-user" } }]
  })
}

resource "aws_iam_role_policy" "irpt_residue_delete_0" {
  name = "irpt-residue-delete-0-policy"
  role = aws_iam_role.irpt_residue_delete_0.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = ["s3:DeleteObjectVersion"]
      Resource  = [for o in local.chunks[0] : "arn:aws:s3:::${o.bucket}/${o.key}"]
      Condition = { StringEquals = { "s3:VersionId" = [for o in local.chunks[0] : o.version_id] } }
    }]
  })
}

resource "aws_iam_role" "irpt_residue_delete_1" {
  name                 = "irpt-residue-delete-1-role"
  max_session_duration = 3600
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Effect = "Allow", Action = "sts:AssumeRole",
                   Principal = { AWS = "arn:aws:iam::313476888478:user/cloudops-dell2-agent-user" } }]
  })
}

resource "aws_iam_role_policy" "irpt_residue_delete_1" {
  name = "irpt-residue-delete-1-policy"
  role = aws_iam_role.irpt_residue_delete_1.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = ["s3:DeleteObjectVersion"]
      Resource  = [for o in local.chunks[1] : "arn:aws:s3:::${o.bucket}/${o.key}"]
      Condition = { StringEquals = { "s3:VersionId" = [for o in local.chunks[1] : o.version_id] } }
    }]
  })
}

resource "aws_iam_role" "irpt_residue_delete_2" {
  name                 = "irpt-residue-delete-2-role"
  max_session_duration = 3600
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Effect = "Allow", Action = "sts:AssumeRole",
                   Principal = { AWS = "arn:aws:iam::313476888478:user/cloudops-dell2-agent-user" } }]
  })
}

resource "aws_iam_role_policy" "irpt_residue_delete_2" {
  name = "irpt-residue-delete-2-policy"
  role = aws_iam_role.irpt_residue_delete_2.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Action    = ["s3:DeleteObjectVersion"]
      Resource  = [for o in local.chunks[2] : "arn:aws:s3:::${o.bucket}/${o.key}"]
      Condition = { StringEquals = { "s3:VersionId" = [for o in local.chunks[2] : o.version_id] } }
    }]
  })
}
```

Do not copy the manifest into the Terraform tree and do not add any other file or resource. Before committing, run the naming gate on the new file the way V2's pair records it (`python .tools/naming-gate.py --diff --enforce`, or the form the gate's own `--help` shows for a staged or working-tree diff; read `.tools/naming-gate.py --help` first) and print its verdict: the names `irpt-residue-delete-0-role` to `-2-role` and `-0-policy` to `-2-policy` must read CONFORMANT. If the gate REFUSES a name, STOP with a BLOCKING row naming the refused name and the gate's own reason, and do not invent a registry row or a different name.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~362/`: `check_residue_roles.py` (stdlib only, ruff clean, offline). It reads the manifest at its repository path and the new `.tf` file as TEXT (and `git hash-object` of each), and prints `RESIDUE-ROLES-OK entries=29 chunks=3 sizes=12,12,5 action=s3:DeleteObjectVersion only principal=cloudops-dell2-agent-user only no_wildcard=yes manifest_blob=7963026db4` only if: the manifest blob equals `7963026db44e4760e34bb28f2b21dc141c7c3fac`; the manifest has exactly 29 entries, every `bucket` is `opal-data-irpt`, every `key` starts `irpt/49financial/`, no key or version_id contains `*`, `?`, `[`, `]`, ends with `/` or is `null`, and no `(key, version_id)` pair repeats; the `.tf` text equals the exact content above (compare to the block in this order read from the order file: strip the fenced block from this order text and compare); the `.tf` has exactly 3 `aws_iam_role` and 3 `aws_iam_role_policy` resources; `Action` is only `s3:DeleteObjectVersion`; the only principal is the one user ARN; `chunklist(..., 12)` yields sizes 12, 12, 5 for the manifest; an in-Python re-evaluation of the HCL's `Resource` and `s3:VersionId` expressions (the same list comprehension over the manifest chunks) gives, per chunk, exactly the chunk's bucket/key ARNs and version ids, and the union over the three chunks equals the manifest's 29 entries with no entry twice and none missing; each rendered role-policy document is under 4000 characters. Else `RESIDUE-ROLES-BAD <why>` (rc 1). `--selftest` mutates in memory five ways (a fourth `Action` `s3:GetObject` added; a wildcard `*` put at the end of one key; the principal changed to `arn:aws:iam::313476888478:root`; one manifest entry dropped; one entry duplicated into another chunk) and prints `CONTROL-FIRES` only when ALL FIVE read BAD. Commit order: the `.tf` as ONE commit first, message citing AR-y-489; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR489-y-AC1" cell_refs="AR-y-489"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~362/check_residue_roles.py</invocation><expect>^RESIDUE-ROLES-OK entries=29 chunks=3 sizes=12,12,5 action=s3:DeleteObjectVersion only principal=cloudops-dell2-agent-user only no_wildcard=yes manifest_blob=7963026db4$</expect></criterion>
<criterion id="AR489-y-AC2" cell_refs="AR-y-489"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~362/check_residue_roles.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR489-y-AC3" cell_refs="AR-y-489"><invocation>git hash-object infra/aws/terraform/investor-reporting/ycharts/irpt_residue_delete_r35.tf</invocation><expect>^[0-9a-f]{40}$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~362/IRPT_ANLREQ.TO-AR-y-489.residue-delete-roles-terraform-source-for-the-29-version-manifest.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-489.residue-delete-roles-terraform-source-for-the-29-version-manifest`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR489-y-AC1,AR489-y-AC2,AR489-y-AC3"`; flip `<status>` to `complete` only when it prints VALID. In your report print the blob that AC3 prints: the issuer pins it in the never-widen pair.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-489</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/terraform/investor-reporting/ycharts/irpt_residue_delete_r35.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~362/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-489.residue-delete-roles-terraform-source-for-the-29-version-manifest.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one new Terraform file declaring six IAM resources; nothing is planned, applied or run against AWS; IB2 applies them under a never-widen pair after the CTO signs, and destroys them in the same act.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the manifest, V2's round-22 pair and the CTO's ruling against this cell; the lens: a role that allows more than DeleteObjectVersion, a resource wildcard or prefix, a version condition missing (any version of the key deletable), a chunk that drops or repeats a manifest entry, a principal wider than the one agent user, a hand-edited file that differs from the order's block by a character, a naming-gate refusal worked around, a control that cannot fire. NOT seen (blind): the live state of the 29 versions after this write; denominator: three criteria.
</preflight>
