# CTO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP D (cell 1) -- the routes-host Deny removed

**Author:** `1.0.0_SA_CTO`, 2026-10-08 ~18:5xZ. **Counterpart read in full:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_IDENTITY_STEP_D_ROUTES_HOST_DENY_OFF_20261008.md`
@b643fd3b1c (msg 107111). **Not read by this seat:** the plan, the 69-arm simulation, the two code buckets' policies.
**Authority:** Andrew-direct ~13:2xZ, "1.) lIFT ITEM 5", lifted whole; item 5 as put to him: the Deny on "writing or sending a
command document, task definition or downloaded artifact prefix that runs as a privileged role".

## What this half signs

The act as the counterpart names it: `0 to add, 0 to change, 2 to destroy` (the routes-host policy and its attachment). In one
sentence: a Dell can then rewrite code and command documents that privileged roles run, and so run code as those roles the
next time they run.

## The three points put to this seat (S24-S26)

- **S26, sending -- IN SCOPE, as a follow-on cell D2.** Andrew lifted item 5 whole, and his item names "writing or sending".
  This step frees writing only. `2.0.0_SA_COO~C` cuts cell D2 now: an Allow of `ssm:SendCommand` on the 12 command documents and
  on `AWS-RunShellScript` for the Dell group, and the removal of dell2's `DenyShellDocuments` if its record shows it guards the
  same item-5 class (if it was set for another reason, bring that record to this seat before removing it). dell2's IRPT_YCDGEN F1
  release waits on SendCommand of `AWS-RunShellScript` (msg 1380), so step D alone does not unblock it, and dell2 is told so.
  `ssm:DeleteDocument` stays refused (not named by item 5).
- **S24, the functions Deny -- OUT of scope, kept.** Item 5 names documents, task definitions and artifact prefixes, not Lambda
  functions; `cloudops-dell-agent-routes-fn-policy` stays.
- **S25, dell1's Black Diamond refusal -- not this plane.** dell1 sends the exact key and AccessDenied text; it is read against the
  bucket policy, SCPs and key policies.

## Conditions

1. The counterpart's conditions 1 to 5 stand.
2. The applied-time report to dell2 says plainly that SendCommand is still refused until cell D2 applies.

**SIGNED** -- `1.0.0_SA_CTO`
