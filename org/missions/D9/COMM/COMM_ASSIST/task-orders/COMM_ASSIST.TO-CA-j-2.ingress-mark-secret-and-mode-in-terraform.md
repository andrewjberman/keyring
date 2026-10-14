# TO COMM_ASSIST.TO-CA-j-2 -- round 18 CA-j-2: the Terraform file declares the ingress-mark secret, lets the two functions read it, and sets INGRESS_MARK_MODE to record (the edit only; the apply is CA-j-3)

<to_id>COMM_ASSIST.TO-CA-j-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~21</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>INGRESSTF</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-2` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 1) | **outcome_ref:** FWD-7 |
**depends_on:** CA-j-1 (merged @0ca94ce0b6)

---

## WORKER FACE

### THE CELL

The assistant (LDO-001, two Lambdas from `module "ldo_001"` in `infra/aws/terraform/transcripts/chat_assist.tf`) now marks every event it makes for Andrew's texts and checks the mark in the handler (cell CA-j-1). The mark is an HMAC keyed by a secret
named by the `NAMES.json` row `secrets.ingress_mark`, and the check runs in the mode the environment variable `INGRESS_MARK_MODE` gives (`off` when unset). This cell puts three things in the Terraform file so the deploy that follows (cell CA-j-3, a separate act by a
CloudOps seat) can set them: the secret SHELL (a name and a description, never a value), the two functions' permission to read it, and the mode variable defaulting to `record`. You edit the file and run NOTHING against AWS: no init, no plan, no apply.

### BUILD

1. Beside the other secret resources, add `resource "aws_secretsmanager_secret" "ca_ingress_mark"` with `name = local.ca_names.secrets.ingress_mark` and a one-sentence `description` (the HMAC key for the ingress mark on LDO-001's text-driven events; its value is put out of band and never enters state). The same shape as `ca_gateway_bearer`. No `aws_secretsmanager_secret_version`, no `secret_string`: a value never enters this file.
2. In `module "ldo_001"`'s `secret_arns = concat([...], ...)`, add `aws_secretsmanager_secret.ca_ingress_mark.arn` to the list beside the other three secret ARNs. Leave the mail-bearer conditional exactly as it is.
3. Beside the other `chat_assist_*` variables add `variable "chat_assist_ingress_mark_mode"`: `type = string`, `default = "record"`, and a one-sentence `description` (how the handler treats an event without a valid mark: off, record or enforce; record checks and counts and acts anyway; enforce refuses). In `local.ca_env` add `INGRESS_MARK_MODE = var.chat_assist_ingress_mark_mode` to the plain map beside `MUSE_ANSWER_PUBKEY`. Leave the `MAIL_BEARER_SECRET` join and every other entry exactly as they are.
4. Format with `terraform fmt` on that one file only. Edit nothing else. No other variable, resource, module call or file changes. No non-ASCII.

### RULES

- Edit nothing but the files in `<paths>`. No `terraform init`, `plan`, `apply` or any AWS call; only `terraform fmt`.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj2-AC1" cell_refs="CA-j-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j2_tf.py"</invocation><expect>J2-TF ok=True arms=7 of 7</expect></criterion>
`CAj2-AC1` -- the issuer's check (read it; do not edit it): the `NAMES.json` row is present; the secret resource reads that row; it is in `secret_arns`; the variable defaults to `record` and the environment carries `INGRESS_MARK_MODE`; no secret value or version is in the file; the existing joins and secrets are untouched; `terraform fmt -check` passes. It prints ok=False at the base (4 of 7).

<criterion id="CAj2-AC2" cell_refs="CA-j-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i4a_tf.py"</invocation><expect>I4A-TF ok=True</expect></criterion>
`CAj2-AC2` -- the bound, a control that PASSES at the base and must still pass: muse's key pin and the mail-bearer join are unchanged and the file is formatted.
</proof_of_spec>

<expected_criteria>CAj2-AC1,CAj2-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~21/COMM_ASSIST.TO-CA-j-2.ingress-mark-secret-and-mode-in-terraform.proof_of_spec.json`, validate it by running the
WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAj2-AC1,CAj2-AC2`, and flip `<status>` to `complete` only when both pass and the
instance is VALID. Your final report names the lines you added. Your surprise rows are `COMM_ASSIST-W21-S<k>`; append only to the investigation file and keep its existing line endings;
`surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-2</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/transcripts/chat_assist.tf
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-2.ingress-mark-secret-and-mode-in-terraform.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~21/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing and applies nothing.
comp-iam: DECLARED-NOT-APPLICABLE no policy is applied here; the secret ARN joins the module's `secret_arns` list, which the module turns into a read grant for the two functions at the CA-j-3 apply, and that plan is read there. BLIND: that the grant covers the new ARN is read by the CA-j-3 plan and the live read, not here.
comp-adversary: RUN -- a secret value in the file (refused: AC1 `value` arm rejects `secret_string` and any secret version); a mode default of `enforce` (refused: AC1 pins `record`); the existing joins disturbed (refused: AC1 `keep` arm pins six exact strings and AC2 pins the muse key and mail join); a second edit riding the file (refused: THE CELL; the CA-j-3 plan will show any); the secret named by a typed string (refused: AC1 `shell` arm requires `local.ca_names.secrets.ingress_mark`). BLIND: that Terraform accepts the file is read by the plan in CA-j-3, not here.
naming: the secret name comes from the `NAMES.json` row `secrets.ingress_mark` (CONFORMANT, graded at CA-j-1's commit); no name is typed here (CLAUDE.md rule 30).
lane: the <paths> block IS the grant (worker RULING 1). Declared WORLD because the gate infers that floor from an infrastructure path; the act itself is an edit with no apply, so its close is the file and its check. The apply is cell CA-j-3 with its own pair.
</preflight>

Base: CAj2-AC1 base: FAIL as expected (4 of 7; the NAMES row is present since CA-j-1, the shell, the read and the mode are not). CAj2-AC2 base: PASS as expected (control). AC1 green arm: PASS as expected (7 of 7) against a scratch copy carrying the intended edit, `terraform fmt` applied.
Source: round-18 decomposition cell CA-j-2; CTO round-17 analysis item 1 (`ledger/ROUND_ANALYSIS.round17.md`); CA-j-1 contract (`ingress_mark.py`, `tenant.py` `_mark_mode`).
