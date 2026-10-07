# Two findings about `infra/aws/terraform/transcripts/`, filed from the LAPTOP for NFRA_TRNSPT's owner to mint

**Filed by:** `0.7.0_AE_CloudOps~E` (laptop), 2026-10-07 ~20:0xZ.
**Why this is a file and not two appended rows:** CTO never-widen half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_TRANSCRIPTS_KEY_DELL_DECRYPT_20261007.md` @`091b68b282`,
**condition 8**, verbatim: *"The root's untargeted drift (9 to add, 4 to change) and its backend record are filed as rows
on NFRA_TRNSPT's channel for its owner, as a file from the laptop, since a Dell mints that project's ids."*
**This seat mints NO `NFRA_TRNSPT-S<n>` id.** The channel's highest id at the time of writing is `NFRA_TRNSPT-S14`;
the owner assigns the next two and folds these into
`org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md`.

**Occasion:** `NFRA_CTLPLN.TO-APPLY-9` @`70eeb0005b`, one targeted apply of `aws_kms_key.transcripts` at the laptop
(the two Dell agent users admitted to `kms:Decrypt` and `kms:DescribeKey`). Both findings were measured in the course
of that apply. **Neither was acted on. Nothing of NFRA_TRNSPT's was applied, reverted or repaired.**

---

## CANDIDATE ROW 1 -- the root carries another project's unapplied work, so it cannot be applied untargeted

**`spec_asserts`:** a Terraform root at the trunk applies cleanly, so an `apply` of it lands only what its own commit
intends.

**`world_is`:** UNTARGETED, this root plans **`9 to add, 4 to change, 0 to destroy`** (measured read-only with
`-lock=false` at ~19:4xZ, applying nothing; re-read after the key apply as **`9 to add, 3 to change, 0 to destroy`**,
the one departed change being the key). The 9 creations and 3 of the 4 changes are **unapplied work that is not
NFRA_CTLPLN's**:

| resource | plan verb |
|---|---|
| `aws_lambda_function.pull` | created |
| `aws_iam_role.pull` | created |
| `aws_iam_policy.pull` | created |
| `aws_iam_role_policy_attachment.pull` | created |
| `aws_cloudwatch_event_rule.pull` | created |
| `aws_cloudwatch_event_target.pull` | created |
| `aws_cloudwatch_log_group.pull` | created |
| `aws_lambda_permission.pull_from_rule` | created |
| `aws_kms_grant.pull` | created |
| `aws_lambda_function.mail_pull` | updated in-place |
| `module.ldo_001.aws_lambda_function.handler` | updated in-place |
| `module.ldo_001.aws_lambda_function.ingress[0]` | updated in-place |

**Denominator:** 13 resource blocks in the untargeted plan, of which **1** was this act's (`aws_kms_key.transcripts`)
and **12** are the above. **0 destroys** anywhere in the plan, before or after.

**Why it matters to the owner:** anyone who runs a bare `apply` in this root lands a whole Lambda stack and a KMS
grant that nobody has signed for in this window. Under `NFRA_CTLPLN.TO-APPLY-9` both signed halves made an untargeted
apply a **void** of the sign-off, and the apply was targeted at one address for exactly this reason. **The three
in-place Lambda updates are the quieter half of the hazard:** they do not announce themselves as new infrastructure,
and `aws_kms_grant.pull` is an access change on the same key this seat just edited.

**Not established here:** whether that work is mid-review, abandoned, or simply awaiting its own window; and whether
the three in-place Lambda updates are code drift, configuration drift or both. This seat did not read the other
project's commits, and `local.pull_*` / `local.mail_*` names render only inside a plan (the naming gate printed ten
`unresolved before plan` lines for them during the apply, which is that gate reporting what it cannot grade, not a
defect).

**`disarm_owner`:** not ARMED by this seat -- nothing here is a live hazard that a laptop act created. It is a
standing condition of the root.

---

## CANDIDATE ROW 2 -- `terraform init` refuses in the shared tree, and the usual cause is NOT the cause

**`spec_asserts`:** `terraform init` in a root at the trunk either initialises against the backend the root's
`main.tf` declares, or names what differs.

**`world_is`:** in the shared tree `terraform init` fails **"Backend configuration changed"**. **The obvious
explanation is measured FALSE.** The root's own `.terraform/terraform.tfstate` records:

```
type   = s3
bucket = opal-313476888478-terraform-state
key    = transcripts/tfstate
region = us-east-1
```

and `main.tf:33-37` declares **the same bucket, the same key and the same region**. So the refusal is **not** a
bucket, key or region mismatch; it is some other field of the stored record. The same `init`, run with `TF_DATA_DIR`
pointed at a scratch directory outside every git tree, **succeeded** against that identical backend
(`Successfully configured the backend "s3"!`) **with no migrate prompt and no reconfigure prompt**.

**What this seat did NOT do, deliberately:** no `init -reconfigure`, no `init -migrate-state`, and no write of any
kind to the root's own `.terraform`. Both halves forbade it on the ground that this is another project's root and may
be mid-migration. **Proof it was left alone:** `.terraform/terraform.tfstate` is 1818 B,
`sha256 13b0ae8497536acf75c68d229041b22397cb43b1edabc1814a466ed328215383`, **identical before the init, after the
init, and after the apply.**

**Why it matters to the owner:** a seat working this root in the shared tree meets a refusal whose stated reason
points at the three fields that are in fact correct, so the natural next move is `-reconfigure` or `-migrate-state` --
either of which rewrites backend state in a root that may be mid-migration. The scratch-`TF_DATA_DIR` route is a
working way past it that touches nothing.

**Not established here:** which field of the record actually differs. Resolving that means diffing the stored record
against what Terraform computes for the current block, and that read belongs to whoever owns this root; this seat
stopped at proving the three obvious fields match.

**`disarm_owner`:** not ARMED. Nothing was changed; the condition pre-dates this act and survives it.

---

## WHAT THIS FILE DOES NOT CLAIM

- It does not claim either finding is new to NFRA_TRNSPT. Neither appears in `INVESTIGATION_v1.md` up to
  `NFRA_TRNSPT-S14` on a read of that file, but this seat did not read the project's adjudications or its PRD, so
  **"not already filed" is NOT asserted** -- if the owner already holds one of these, that id supersedes the
  candidate and this file is the duplicate.
- It does not touch NFRA_TRNSPT's served output, state, or any resource of its root.
- The counts are of DECLARED plan verbs from one read-only plan at one moment, not of live AWS state.
