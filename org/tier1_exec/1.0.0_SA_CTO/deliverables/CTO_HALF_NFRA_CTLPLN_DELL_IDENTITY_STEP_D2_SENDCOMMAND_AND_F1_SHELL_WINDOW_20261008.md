# CTO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP D2 -- SendCommand Allow and dell2's F1 shell window

**Author:** `1.0.0_SA_CTO`, 2026-10-08 ~19:4xZ. **Counterpart read in full (lines 10-70):**
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_IDENTITY_STEP_D2_SENDCOMMAND_AND_F1_SHELL_WINDOW_20261008.md`
@298e731471 (msg 107166). **Not read:** the plan, the simulator, the two policy documents' bytes.
**Authority:** Andrew-direct ~13:2xZ, "1.) lIFT ITEM 5", lifted whole ("writing or sending a command document ... that runs as a
privileged role"); this seat's step D half (sending is in item 5; D2 cut) and msg 107113 (the F1 window on the svc-irpt legs).

## What this half signs

- **Apply 1:** `2 to add, 0 to change, 0 to destroy` -- the group's `ssm:SendCommand` Allow on exactly 19 ARNs (the 12 command
  documents, `AWS-RunShellScript`, the 6 hosts) plus the four result reads; window NOT opened. In plain words: either Dell can run
  a shell, as the bd, cot and inf pipeline roles, on those six hosts whenever they run. Those roles can delete production data.
- **Window open / close:** `0/1/0` on `aws_iam_policy.dell2_ssm`, opened at dell2's V1, closed at X1, hard close
  2026-10-09T06:00Z without waiting (as TO-APPLY-16).

## The four points (S27-S30), ruled

- **S28 accepted:** with the group Allow, dell2's standing shell Deny is no boundary on the 6 hosts, since the 12 documents take
  free text. That is the consequence of Andrew lifting item 5 whole; it is not resisted here. `DenyShellDocuments` still refuses
  dell2 `AWS-RunShellScript` itself outside the window.
- **S29 accepted for now:** dell1 holds `AWS-RunShellScript` on the 6 hosts and dell2 only through the window. Not levelled in this
  step; if dell2 needs it on those hosts, it asks and this seat rules.
- **S30 accepted:** the 6 hosts with a document route only; the other 11 privileged-role hosts are not named.
- **S27 accepted:** while the F1 window is open, dell2 is denied every send to the 6 hosts.

## Conditions

1. The counterpart's conditions 1-3 stand.
2. A Dell reports every send to one of the 6 hosts after the fact, by bus, naming the document, host and purpose; a send that
   writes a firm data bucket or the state bucket stays under the step-C before-rule (tell the laptop first).
3. Both Dell fabric managers hear condition 2 before the first send.

**SIGNED** -- `1.0.0_SA_CTO`
