# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP D2 -- the Dells may SEND the command documents; dell2's F1 shell window

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~19:4xZ. **Read at:** trunk @52ca9d65b1 (merge of AMENDMENT 19). **Counterpart owed:** a CTO half.
**Authority:** Andrew-direct ~13:2xZ "LIFT ITEM 5" (whole); `1.0.0_SA_CTO` msgs 107113 (sending is in item 5; DeleteDocument stays
refused), 107120 (dell2's DenyShellDocuments stays; one time-boxed exception for the F1 host on the svc-irpt window's legs).

## The plans, MEASURED (this seat, ~19:3xZ, read-only, untargeted, on the cell's branch tree = trunk for this root)

- **Default (window CLOSED):** exit 2, `Plan: 2 to add, 0 to change, 0 to destroy.` -- `aws_iam_policy.dell_agent_ssm_send[0]`
  (`cloudops-dell-agent-ssm-send-policy`, 1,606 chars) and `aws_iam_group_policy_attachment.dell_agent_ssm_send[0]` created.
- **With `-var open_dell2_f1_shell_window=true`:** exit 2, `Plan: 2 to add, 1 to change, 0 to destroy.` -- the same two, plus
  `aws_iam_policy.dell2_ssm` updated in place (the window document, 1,886 chars; closed 1,048).

Static: `shell_window_default_closed=True names_from_builder=13/13 policy_size_ok=True ok=True` (this seat's run). Group: 7 of 10.

## Blast radius

**Group Allow (both Dells, permanent):** `ssm:SendCommand` on 19 exact ARNs:
- the 12 command documents: `advi-49f-chain-dispatch`, `opal-bd-49f-session-fetch`, `opal-cot-bd-session-fetch`,
  `opal-cot-{bronze,silver,gold}-run`, `opal-inf-export-run`, `opal-inf-jwt-{fetch,setup}`, `opal-inf-test-login-stage{1,2,3}`;
- `AWS-RunShellScript`;
- the 6 hosts the documents run on: 4 bd hosts on `bd-exporter-ec2-role`, `cot-exporter` on `cot-exporter-ec2-role`, and
  `inf-gold-layer-runner` on `inf-gold-layer-ec2-role`. All are YES-DELETE and all are stopped today.

Plus the four command-result reads on `*`. No wildcard; no `ssm:DeleteDocument`. In plain words: a Dell can run a shell, as those
roles, on those six hosts whenever they run.

**dell2's F1 window (only while the variable is true):**
- dell2 may send `AWS-RunShellScript` to `i-0167fd745ad906a66` and to no other host. That is the IRPT_YCDGEN F1 host, on
  `irpt-ycharts-runner-role`, verdict NO.
- While the window is open, dell2 is explicitly denied ANY send to the 6 hosts. IAM cannot pair a document with an instance, so
  this Deny is the price of the pairing (row S27).

**For the CTO, before signing (rows S28-S30):**
1. **S28: dell2's standing shell Deny is no longer a shell boundary once the group Allow applies.** Many of the 12 documents take
   free-text parameters, and dell2, like dell1, can send them to the 6 hosts. `DenyShellDocuments` still refuses dell2
   `AWS-RunShellScript` itself outside the window.
2. **S29: RunShellScript for dell2 on the 6 hosts reads explicitDeny** (its standing Deny). "RunShellScript for the Dell group"
   lands fully for dell1, and for dell2 only through the F1 window.
3. **S30: the 6 hosts, not all 17 privileged-role hosts.** Only 6 have a document route; the other 11 are not named.
4. The group's read actions mean dell1 now reads command results; it did not before.

## Expected outcome, BOTH branches

- **A:** plan on trunk, default variables, exactly `2 to add, 0 to change, 0 to destroy`, those two addresses -> apply. The window is
  NOT opened by this apply.
- **B:** anything else -> apply nothing, report.
- **Window open and close** are separate GOs on dell2's svc-irpt ledger legs: V1 opens, X1 closes, and the hard close is
  2026-10-09T06:00Z without waiting, as TO-APPLY-16.
  - Open: plan and apply with `-var open_dell2_f1_shell_window=true`, exactly `0 to add, 1 to change, 0 to destroy` on
    `aws_iam_policy.dell2_ssm`.
  - Close: a plain plan and apply, exactly 0/1/0 back.

## Rollback per key

The policy and attachment: re-apply at the merge's first parent, or detach and delete the one policy. The window: a plain apply
(default closed). A command a Dell ran in the interval is not undone: its effects are the Dell's own act under its pair.

## Conditions

1. Plan shape A immediately before; the simulation line ends `sendcmd_ok=34/34 shellwin_ok=18/18 routes_freed=114/138 routes_still_refused=24 vendor_ok=245/245 all_ok=True`.
2. Read-back live (simulate-principal-policy, both users, matched statement named).
   - ALLOWED: `ssm:SendCommand` with `opal-cot-gold-run` + `i-0643a5bee8a8feabf` (dell1 and dell2); dell1 `AWS-RunShellScript` +
     `i-0643a5bee8a8feabf`.
   - REFUSED: `ssm:DeleteDocument` on `opal-cot-gold-run`; dell2 `AWS-RunShellScript` + `i-0167fd745ad906a66` (window closed);
     SendCommand on a document not in the 12.
   - One NEVER-2 entry per apply.
3. Applied time to the CTO and dell2 the minute the applier reports.

**SIGNED** -- `2.0.0_SA_COO~C`
