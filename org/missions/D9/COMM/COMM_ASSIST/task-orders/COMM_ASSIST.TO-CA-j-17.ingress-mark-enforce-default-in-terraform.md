# TO COMM_ASSIST.TO-CA-j-17 -- round 18 CA-j-17: the Terraform file's default for INGRESS_MARK_MODE becomes enforce (the edit only; the apply is CA-j-5)

<to_id>COMM_ASSIST.TO-CA-j-17</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~26</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>ENFORCETF</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-17` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 9) | **outcome_ref:** FWD-7 |
**depends_on:** CA-j-10 (CLOSED @0a79b22d2a), CA-j-8 (CLOSED @df7f6f6c55); the observation read `check_j5_obs.py` (CLEAN at 13:50Z)

---

## WORKER FACE

### THE CELL

The assistant's two Lambdas (LDO-001, `module "ldo_001"` in `infra/aws/terraform/transcripts/chat_assist.tf`) mark every event they make for Andrew's texts and check the mark in the handler, in the mode the environment variable `INGRESS_MARK_MODE` gives. The Terraform variable `chat_assist_ingress_mark_mode` sets it and defaults to `record` (the handler counts a missing or bad mark and acts anyway). The observation window has read CLEAN: the handler accepted 8 marked events and refused none, and the key is narrowed to the execution role. This cell changes ONE line: the variable's default becomes `enforce` (the handler refuses an unmarked, tampered, stale or replayed event). You edit the file and run NOTHING against AWS: no init, no plan, no apply, no AWS call; only `terraform fmt`. The apply that makes it live is cell CA-j-5, by the CloudOps seat under its own never-widen set, and NOTHING happens in AWS until then.

### BUILD

1. In `chat_assist.tf`, in `variable "chat_assist_ingress_mark_mode"`, change `default = "record"` to `default = "enforce"`. Change the variable's `description` only if it names the old default (it describes the three modes; leave it if it does not).
2. Run `terraform fmt` on that one file. Edit nothing else: no other variable, resource, module call or file. No non-ASCII.

### RULES

- Edit nothing but the files in `<paths>`. No `terraform init`, `plan`, `apply` or any AWS call; only `terraform fmt`.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj17-AC1" cell_refs="CA-j-17"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j5_tf.py"</invocation><expect>J5-TF ok=True arms=2 of 2</expect></criterion>
`CAj17-AC1` -- the issuer's check (read it; do not edit it): the file equals the record-mode file of the pin `3af44d523b` with that ONE default changed to `"enforce"` and nothing else (LF-normalised), and `terraform fmt -check` passes. It prints ok=False at the base (1 of 2).

<criterion id="CAj17-AC2" cell_refs="CA-j-17"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j7_tf.py"</invocation><expect>J7-TF ok=True arms=6 of 6</expect></criterion>
`CAj17-AC2` -- the bound, a control that PASSES at the base and must still pass: the narrowed-key policy, the secret shell, the read grant, the mode variable and the environment key from CA-j-2 and CA-j-7 are untouched (that check re-runs the CA-j-2 check, whose mode arm now accepts a default of `record` or `enforce` and still fails any other value).
</proof_of_spec>

<expected_criteria>CAj17-AC1,CAj17-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Commit the edit FIRST (`.tools/safe-commit.sh` as your serial; the message file is written with the Write tool). Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~26/COMM_ASSIST.TO-CA-j-17.ingress-mark-enforce-default-in-terraform.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~22/COMM_ASSIST.TO-CA-j-7.ingress-mark-key-resource-policy-in-terraform.proof_of_spec.json`, recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning the `chat_assist.tf` artifact row to the commit that carried the edit (a row left as pending-this-commit goes INVALID the moment a later commit lands). Flip `<status>` to `complete` only when both pass. Validate by running the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAj17-AC1,CAj17-AC2`, and read the LAST line: it must be `VALID (rc=0)` at the final head. Your final report names the one line you changed. Your surprise rows are `COMM_ASSIST-W26-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-17</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/transcripts/chat_assist.tf
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-17.ingress-mark-enforce-default-in-terraform.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~26/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing and applies nothing.
comp-iam: DECLARED-NOT-APPLICABLE no policy moves and no AWS call is made; the apply is cell CA-j-5.
comp-adversary: RUN -- the mode going live before the sign-offs (refused: this cell edits a default and applies nothing; the file reaches AWS only through CA-j-5's targeted apply under three halves); a second edit riding the file (refused: AC1 compares the file to the pin's with exactly one line changed); the CA-j-2 and CA-j-7 pieces disturbed (refused: AC2). A stale `enforce` default sitting in the trunk flipping the mode on ANOTHER seat's apply of this module (refused by sequence: the issuer does NOT merge this edit into `box/laptop` until CA-j-5 has applied and closed; the pair and the deploy pin the worker's commit on its own branch `wk-COMM_ASSIST-26`, which the CloudOps seat reads from a detached worktree, and the trunk's file stays `record` meanwhile). BLIND: that Terraform accepts the file and plans exactly the environment change is read by CA-j-5's plan, not here.
naming: no name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1). Declared WORLD because the gate infers that floor from an infrastructure path; the act itself is an edit with no apply, so its close is the file and its check.
</preflight>

Base: CAj17-AC1 base: FAIL as expected (1 of 2: the formatting holds, the default does not read enforce). CAj17-AC2 base: PASS as expected (control, 6 of 6). AC1 green arm: PASS as expected (2 of 2) against a scratch copy of the pin's file with the one default changed; negative controls: an extra edit and a wrong value (`off`) each read FAIL. The CA-j-2 check was amended to accept `record` or `enforce` and still fails `off` (6 of 7), so it reads 7 of 7 on both the record and the enforce tree.
Source: the observation read `check_j5_obs.py` (CLEAN at 13:50Z: 8 marked events accepted on 8 objects between 13:01:23Z and 13:01:46Z, 0 refusals, 0 unmarked; 0 `AccessDenied` or error in either function log since 11:36Z); the CTO and CVO halves of CA-j-3, CA-j-8 and CA-j-10 (the enforce pair reads marks_seen against unmarked_seen); round-18 decomposition AMENDMENTS 3, 5, 6.
