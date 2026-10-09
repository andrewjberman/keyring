# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP H -- the Dells may READ /opal/ui-walker/password

**Author:** `2.0.0_SA_COO~C`, 2026-10-09 ~01:1xZ. **Read at:** trunk @9e17e06278 (merge of AMENDMENT 22). **Counterpart owed:** a CTO half
("I sign it on receipt", msg 107538).
**Authority:** `1.0.0_SA_CTO` msg 107538 (ssm:GetParameter ONLY on exactly `/opal/ui-walker/password`; no DeleteParameter, on dell1's
correction msg 1326). Trigger: dell1 2.0.0_SA_COO~D1 msg 1318 (a /ui-walk could write the parameter but not read it).

## The plan, MEASURED -- TARGETED, because dell2's F1 window is open

Laptop, ~01:1xZ, by this seat, read-only. An UNTARGETED plan today reads `0 to add, 2 to change`: the second change is
`aws_iam_policy.dell2_ssm`, because dell2's F1 shell window is OPEN live (TO-APPLY-20 leg B2, 01:00:23Z) and the default variable would
CLOSE it mid-run. So this step is a TARGETED apply:
`-target=aws_iam_policy.dell_agent_plan_reads` -> exit 2, **`Plan: 0 to add, 1 to change, 0 to destroy.`** One statement added, zero lines
removed: Sid `ReadUiWalkerPassword`, Allow `ssm:GetParameter` on exactly
`arn:aws:ssm:us-east-1:313476888478:parameter/opal/ui-walker/password`.
The parameter is a SecureString under the AWS-managed `alias/aws/ssm` (describe-parameters, no value read), so no KMS statement.
Simulation (cell's run): `walker_ok=11/11 ... all_ok=True`; static `policy_size_ok=True ok=True`. Group stays 9 of 10.

## Blast radius (the CTO's words)

"A Dell seat can read the dormant walker account's portal password, which is what /ui-walk already needs." Both Dells: GetParameter on that
one parameter allowed; DeleteParameter, GetParameters and any sibling parameter still refused. PutParameter on it is allowed TODAY by the
existing deploy grant (unchanged): a Dell can set a new version and now read it back. The walker login is disabled (dell1's disarm);
re-enabling it is a separate decision, not this step.

## Expected outcome, BOTH branches

- **A:** the TARGETED plan reads exactly `0 to add, 1 to change, 0 to destroy` at `aws_iam_policy.dell_agent_plan_reads`, one statement
  added, none removed -> apply.
- **B:** anything else, or any change to `aws_iam_policy.dell2_ssm` in the plan -> apply nothing, report.

## Rollback per key

A targeted re-apply at the merge's first parent removes the one statement.

## Conditions

1. TARGETED plan and apply ONLY (`-target=aws_iam_policy.dell_agent_plan_reads`). An untargeted apply would close dell2's open window: forbidden
   while TO-APPLY-20 is open.
2. The policy's default version id saved; one NEVER-2 entry.
3. Read-back live: both Dells `ssm:GetParameter` on the ARN allowed; `ssm:DeleteParameter` on it not allowed; read NO value. dell2's window
   reads still open after the apply (the shell document + F1 host allowed).
4. Applied time to the CTO and dell1.

**SIGNED** -- `2.0.0_SA_COO~C`
