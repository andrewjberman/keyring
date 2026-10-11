# ADVI_FIRMBKTS task order -- `FB-e-4` -- F4: WHOM THE TWO FIRM BUCKETS' FENCE ADMITS, AND WHOM IT REFUSES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R2.md</decomp_doc>
<owned_cells>FB-e-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~7</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- 0 of 9 `*-cot-*` roles are assumable by user/cloudops-dell1-agent-user and iam:SimulatePrincipalPolicy / SimulateCustomPolicy are refused to it (denominators printed in L5_FACTS section 2). No IAM object is created or changed; the negative arm uses the one existing trust path (role/irpt-ycharts-runner-role -> irpt-cot-ycharts-research-role). ssm:SendCommand on the runner is INFERRED, not measured: a refusal is a BLOCKING row.
comp-adversary: RUN by the issuer -- r2_f4.py positive arm 3 of 3 live at base (a control); negative arm 0 of 4 at base (evidence absent), 4 of 4 on a reference record, 3 of 4 on each of three mutants (no deny text; own firm also refused; caller is not a cot role). Blindness: the lens cannot see the runner's installed CLI or the instance role's identity policy.
EGRESS CLASS, declared: NONE (one read-only SSM command inside the account; no vendor call).
</preflight>

## 1. THE CELL -- `FB-e-4` (round 2, enrichment item 3; PRD F4's acceptance)

`opal-data-inflection` and `opal-data-cottonwood` exist and carry a scope-derived fence (the bucket policy statement
`DenyForeignFirmPrincipals`). F4's acceptance does not ask whether a fence exists; it asks whom it ADMITS and whom it
REFUSES, EXERCISED rather than read from the policy text:
- the POSITIVE arm: an identity this estate holds performs named acts on each bucket and succeeds. This is
  `user/cloudops-dell1-agent-user` and it is a live read-only control: it passes today.
- the NEGATIVE arm: a `role/*-cot-*` principal's own read of `opal-data-inflection` is REFUSED by the resource-based
  deny, while the same principal's read of `opal-data-cottonwood` is not refused by it (the difference control).

You exercise both with the issuer's two instruments below. You do not interpret, extend or repair either.

### 1a. The steps, in order

1. **AC1:** run its invocation (section 4). It must read `3 of 3 arms`. A different count is your final report.
2. **The one send.** `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f4_send.py
   --out org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~7/F4_NEGARM_EVIDENCE.json`
   - It sends ONE `AWS-RunShellScript` command to ONE instance (`i-0167fd745ad906a66`, `irpt-ycharts-runner`). The
     instance, the role and both buckets are constants in that file; it takes no argument that changes them. First run
     `r2_f4_send.py --print` and read the command: it assumes `irpt-cot-ycharts-research-role`, prints that session's STS
     ARN, makes one `ListObjectsV2 MaxKeys=1` on each bucket and prints each result or error text. It prints no credential.
   - If the output says `Status=InProgress` or the file shows no `StandardOutputContent`, fetch the SAME command once:
     `r2_f4_send.py --collect <command_id> --out <same file>`. Never send a second command.
   - If `send_command` is REFUSED (AccessDenied or similar), or the runner reports the AWS CLI absent, that is a BLOCKING
     row with the exact error text, and your final report. Do not try another instance, another role, another service or
     another route.
3. **AC2:** run its invocation (section 4) over the evidence file. It must read `4 of 4 arms`.

## 2. BOUNDS

1. Exactly one `send_command`, to exactly one instance, running exactly the command `r2_f4_send.py` builds. Read-only on
   the buckets; nothing written to AWS; no delete; no IAM or SSM document change.
2. Never print, save or commit a credential. The evidence file holds the command's output text only.
3. Only the files in section 3 change. Never edit the checks.
4. No non-ASCII; LF line endings. If an item cannot be met within your paths, file a surprise row and stop on that
   criterion.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~7/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the issuer's checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/`
(`r2_f4.py`, `r2_f4_send.py`; never edit them), the PRD.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~7/ADVI_FIRMBKTS.TO-FB-e-4.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-e-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 100 python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f4.py" --arms positive; echo "exit=$?"</invocation><expect>ROUND 2 F4 POSITIVE: 3 of 3 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-e-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f4.py" --arms negative --evidence "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~7/F4_NEGARM_EVIDENCE.json"; echo "exit=$?"</invocation><expect>ROUND 2 F4 NEGATIVE: 4 of 4 arms</expect></criterion>
</proof_of_spec>

AC1 is a control: it passes at the base, so it is not evidence that this cell built anything; it is the positive arm
recorded. AC2 is the cell: it fails at the base because no evidence exists, and it grades the evidence file only (no
AWS call), so it terminates at once.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~7/ADVI_FIRMBKTS.TO-FB-e-4.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance and the evidence file**, only when
AC1 and AC2 both pass. A row id on this project carries the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W7-S<k>`, with
`surfaced_at` from `date -u +%FT%TZ`. Report once: the caller ARN printed by AC1, the command id, the `INF:` and `COT:`
lines of the evidence verbatim (first 200 characters each), the output lines of AC1 and AC2, the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's item 3 asked a `*-cot-*` role to be refused by an exercised GET. L5 measured that no held
identity can be one (L5_FACTS section 2) and that both IAM simulators are refused to the dell1 user, so the arm runs
through the one existing principal route. The class is LOCAL by the gate's floor (no infrastructure path, no deploy verb);
it is a read-only act on a running production runner, bounded by the sender's constants, and the CTO is told in the
issuance message. The claim the negative arm carries is `exercised` only if N1-N4 all read PASS; a refusal of the send is
reported as `absent`, never as `inferred`. If the send is refused the cell is a BLOCKING row, not a recut.

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's. Every other limb passed in the issuer's dry run.
<status>complete</status>
<round>2</round>
<to_id>ADVI_FIRMBKTS.TO-FB-e-4</to_id>
<slot>~7</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
