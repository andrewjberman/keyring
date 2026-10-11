# ADVI_FIRMBKTS task order -- `FB-g-10` -- REMOVE THE PENDING `eclipse_jwt_initial` SECRET-VERSION BLOCK FROM THE inf-pipeline ROOT (ROW D1-S19)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-10</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one Terraform resource block is deleted from repository source; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: RUN by the issuer -- 2 reads named (`secretsmanager:DescribeSecret` on `orion/eclipse_jwt/current`, metadata only, and the root's read-only plan) against the dell1 CloudOps identity, 2 of 2 expected; blind to a deny that only bites at plan refresh time; no grant is created and the secret VALUE is never read.
comp-adversary: RUN by the issuer -- at base the unscoped plan lists `aws_secretsmanager_secret_version.eclipse_jwt_initial` as a create (row D1-S19, laptop plan read 358 resource changes, 6 creates, one of them this) so AC1 and AC2 FAIL as expected; AC3 reads `UNREADABLE` at base because the before-record does not exist. Blindness: nothing here proves no OTHER root is affected; the grep over `infra/aws/terraform` found exactly one resource of this name (a comment in bd-pipeline/secrets.tf names it).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-10` (round 4, workstream `INFJWT`; the CTO's round-3 ADDENDUM 2, msg 3843)

`infra/aws/terraform/inf-pipeline/secrets.tf` lines 40-53 declare `aws_secretsmanager_secret_version.eclipse_jwt_initial` with
`secret_string = jsonencode({jwt = "", ...})` and `ignore_changes = [secret_string]`. The resource is in config and NOT in
state. `ignore_changes` guards only after create, so ANY unscoped apply of this root creates a new AWSCURRENT version of
`orion/eclipse_jwt/current` holding `jwt = ""` over the token the inf-jwt-trigger Lambda captured. The CTO ruled: **remove
the block** (it changes nothing in AWS, because state never held it; the value is placed out-of-band by design; import is
REFUSED because every later plan would propose blanking the token). **Never print or read the secret's value.**

### 1a. Steps

0. Work in `/c/dev/wk-firmbkts-31` (a linked worktree from the dell1 branch). Begin every shell call with `cd /c/dev/wk-firmbkts-31 &&`. Initialise the root
   once: `cd /c/dev/wk-firmbkts-31/infra/aws/terraform/inf-pipeline && terraform init -input=false -no-color` (backend and providers read; no infrastructure change).
1. **Before the edit**, record the live AWSCURRENT version id of `orion/eclipse_jwt/current` from the secret's METADATA:
   `aws secretsmanager describe-secret --secret-id orion/eclipse_jwt/current` and take the version id whose stages hold
   `AWSCURRENT` from `VersionIdsToStages`. Write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1/evidence/secret_version_before.json` as
   `{"awscurrent_version_id": "<that id>", "recorded_at": "<date -u +%FT%TZ>"}` (ASCII, LF). Do not call
   `get-secret-value`.
2. **The edit.** In `infra/aws/terraform/inf-pipeline/secrets.tf` delete the resource block `aws_secretsmanager_secret_version.eclipse_jwt_initial`
   (lines 40-53 at base) and put in its place a three-line comment: that the version resource was removed under
   ADVI_FIRMBKTS round-3 ADDENDUM 2 (row D1-S19), why (an unscoped apply would blank the live token), and that the value
   is placed out-of-band. Change nothing else in the file.
3. **The plan, read-only.** Run the root's FULL, unscoped `terraform plan` (the command of AC1) once; keep its output
   under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1/evidence/` uncommitted. It must not list `eclipse_jwt_initial` and must add nothing new (`Plan: 0 to add`, or `No
   changes`). If it lists another resource for its own reasons, name each in your report and stop for the issuer.
4. `terraform fmt` the file. Commit with `.tools/safe-commit.sh` under your own serial. **Do NOT apply**: no apply is
   needed or ordered. Scoped applies only in this root until this lands.

## 2. BOUNDS

1. One file changes: `infra/aws/terraform/inf-pipeline/secrets.tf`; plus your evidence folder. No other Terraform file, no variable, no state
   operation (no `import`, no `state rm`), no `apply`, no AWS write.
2. The secret's value is never read, printed, logged or committed; only the metadata call of step 1.
3. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/terraform/inf-pipeline/secrets.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1/evidence/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1/ADVI_FIRMBKTS.TO-FB-g-10.inf-jwt-initial-removal.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-10"><invocation>cd /c/dev/wk-firmbkts-31/infra/aws/terraform/inf-pipeline &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color 2&gt;&amp;1 | grep -cE "^\s*# aws_secretsmanager_secret_version\.eclipse_jwt_initial (will|must)"</invocation><expect>^0$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-10"><invocation>cd /c/dev/wk-firmbkts-31/infra/aws/terraform/inf-pipeline &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color 2&gt;&amp;1 | grep -E "^(Plan:|No changes)"</invocation><expect>Plan: 0 to add|No changes</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-10"><invocation>cd /c/dev/wk-firmbkts-31 &amp;&amp; timeout 70 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_secretver.py --before org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1/evidence/secret_version_before.json; echo "exit=$?"</invocation><expect>SECRET VERSION: UNCHANGED</expect></criterion>
  <criterion id="AC4" cell_refs="FB-g-10"><invocation>cd /c/dev/wk-firmbkts-31 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-31 --allow infra/aws/terraform/inf-pipeline/secrets.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1/evidence/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/inf-pipeline/secrets.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 and AC2 are one plan read twice for two clauses of the ruling (the resource is gone; nothing new is added). AC3
reads that the live AWSCURRENT version is the one recorded before the edit. A fourth criterion, AC4, is the write-surface
bound (a one-file Terraform edit beside a secret is the case where a stray change matters; it fails for any path
outside the allowance). Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-10.inf-jwt-initial-removal.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1`. Commit the file and
the before-record, then the instance second; flip this order's `<status>` to `complete` in the SAME commit as the instance
only when AC1 to AC4 pass. Row ids: `ADVI_FIRMBKTS-D1-DELL1-S<k>` from the next unused number, `surfaced_at` from
`date -u +%FT%TZ`. Report once to `2.0.0_SA_COO~B1`: AC1 to AC4 outputs, any other resource the plan lists, and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's round-3 ADDENDUM 2 (msg 3843); a third workstream (`INFJWT`) of round 4, added to the
frozen decomposition by amendment 1 (cells 10, chains 9). The CTO calls it a LOCAL cell; a Terraform path carries the WORLD
floor under the gate, so the order carries WORLD with nothing applied. Closes row D1-S19's hazard (ARMED to disarmed at
merge).

**AMENDMENT 1 (2.0.0_SA_COO~B1, after the seat's report msg 3855, row D1-S23):** the dell1 CloudOps identity is denied two
reads the full plan needs (`sms-voice:DescribeSpendLimits`, `ssm:GetParameter` on the inf gold last-trigger-mode parameter), so
the plan reads no Plan line on this box; the issuer will not widen the identity. AC1 and AC2 are therefore graded from the
LAPTOP lane (`0.7.0_AE_CloudOps~FBL`, the identity that took the untargeted plan on 2026-10-11) at the seat's commit, by a
crossbox ORDER; AC3 and AC4 stay the seat's own. AC1's invocation counted the plan's refresh lines as well as a change
line (the laptop's `plan_untargeted.out` lists the name in a refresh line), so it now counts only a `# <address> will be`
or `must be` change header. Gate limb: GATE viii reads `<placeholders>` at HEAD (`NONE`) and the amended invocation
carries no token.

<status>complete</status>
<round>4</round>
<workstream>INFJWT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-10</to_id>
<slot>~DELL1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
