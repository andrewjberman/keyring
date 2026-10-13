# TO COMM_ASSIST.TO-CA-i-9 -- round 17 CA-i-9: the Terraform file pins muse's public key into the assistant's environment (the edit only; the apply is CA-i-4)

<to_id>COMM_ASSIST.TO-CA-i-9</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~15</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>TFPIN</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-i-9` (`decompositions/COMM_ASSIST_DECOMP.round17.md`, AMENDMENT 3) | **outcome_ref:** FWD-7 |
**depends_on:** CA-i-2 (merged @eac776ff43)

---

## WORKER FACE

### THE CELL

The assistant (LDO-001, two Lambdas from `module "ldo_001"` in `infra/aws/terraform/transcripts/chat_assist.tf`) now verifies muse's signed answers against a public key read at call
time from the environment variable `MUSE_ANSWER_PUBKEY` (cell CA-i-2; with the variable unset every muse answer is refused). This cell puts that key into the Terraform file, so the
deploy that follows (cell CA-i-4, a separate act by a CloudOps seat) sets it. You edit the file and run NOTHING against AWS: no init, no plan, no apply.

### BUILD

1. In `chat_assist.tf` add, beside the other `chat_assist_*` variables, `variable "chat_assist_muse_answer_pubkey"`: `type = string`, a one-sentence `description` (muse's public key, one ssh-ed25519 line, not a
   secret; the assistant acts on a muse answer only when its signature verifies against it; empty means every muse answer is refused), and this EXACT default (a public key, the one
   `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/MUSE_KEY_RECORD.md` names by fingerprint):

   `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBiHPazucl0mQ1FIq3VQ1mLIcIvRtdFvS9OnIZgS+rDj muse`

2. In `local.ca_env` (the `merge({...})` block) add `MUSE_ANSWER_PUBKEY = var.chat_assist_muse_answer_pubkey` to the plain map beside `GATEWAY_BASE`, `SMS_ORIGINATION` and `IGNORE_NAMES`. Leave the
   `MAIL_BEARER_SECRET` join exactly as it is. Both Lambdas already take `local.ca_env`, so both get it.
3. Add one comment line above the variable saying that a change to this key is a change-managed deploy (PRD v0.7's stated limit) and that the record is `MUSE_KEY_RECORD.md`.
4. Format with `terraform fmt` on that one file only. Edit nothing else. No other variable, resource, module call or file changes. No non-ASCII.

### RULES

- Edit nothing but the files in `<paths>`. No `terraform init`, `plan`, `apply` or any AWS call; only `terraform fmt`.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAi9-AC1" cell_refs="CA-i-9"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i4a_tf.py"</invocation><expect>I4A-TF ok=True</expect></criterion>
`CAi9-AC1` -- the issuer's check (read it; do not edit it): the variable carries the key whose `ssh-keygen -lf` fingerprint is the record's, the environment joins `MUSE_ANSWER_PUBKEY`, the mail-bearer join is unchanged, and `terraform fmt -check` passes. It prints ok=False at the base.
</proof_of_spec>

<expected_criteria>CAi9-AC1</expected_criteria>

Run the invocation from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~15/COMM_ASSIST.TO-CA-i-9.pin-muse-key-in-the-assistant-environment.proof_of_spec.json`, validate it by running the
WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree: `python .tools/proof-of-spec-check.py <instance> CAi9-AC1`, and flip `<status>` to `complete` only when it passes and the
instance is VALID. Your final report names the lines you added. Your surprise rows are `COMM_ASSIST-W15-S<k>`; append only to the investigation file and keep its existing line endings;
`surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round17.md</decomp_doc>
<owned_cells>CA-i-9</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/transcripts/chat_assist.tf
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-i-9.pin-muse-key-in-the-assistant-environment.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~15/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing and applies nothing.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves; a public key joins an environment map. The apply, and its plan read, are cell CA-i-4.
comp-adversary: RUN -- the wrong key pinned (refused: AC1 compares the fingerprint to the record); the mail-bearer join disturbed (refused: AC1 pins its exact text); a second edit riding the file (refused: THE CELL; the deploy plan will show any); a secret in the file (the pinned value is a public key by construction, fingerprint-checked). BLIND: that Terraform accepts the file is read by the plan in CA-i-4, not here.
naming: no resource or name is created; an environment variable key joins a map (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1). Declared WORLD because the gate infers that floor from an infrastructure path; the act itself is an edit with no apply, so its close is the file and its check. The apply is cell CA-i-4 with its own pair.
</preflight>

Base: CAi9-AC1 base: FAIL as expected (variable not declared). AC1 green arm: PASS as expected against a scratch copy carrying the intended edit (fingerprint SHA256:oq0Wq... equal to the record).
Source: MUSE_KEY_RECORD.md; CTO round-16 analysis @6e9e2fc1ff section 3 item 2 and its ruling (the key rotates by the same change-managed path); `tenant.py` `MUSE_PUBKEY_ENV`; the live Lambdas' environment read 2026-10-13 (no MUSE_ANSWER_PUBKEY).
