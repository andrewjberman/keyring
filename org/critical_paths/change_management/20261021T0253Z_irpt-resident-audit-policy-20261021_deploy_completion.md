# Deploy Completion Record
**Date opened:** 2026-10-21T02:53:45.410162+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-AUDITPOLICY (re-pinned pair, GO 11786): ONE new customer-managed IAM policy (Put-only WriteTheAnalysisAudit on three opal-data-irpt analysis_audit prefixes and a KMS statement narrowed to them) and its attachment to irpt-ycharts-runner-role; the earlier ledger irpt-resident-audit-policy-20261020 is CLOSED as refused by gate
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: five inline policies with sha256, attached list, the new policy absent, baseline simulations on a sample audit key | R0 baseline implicitDeny put on the audit key |  | OPEN |
| C | verify | scoped plan at trunk HEAD reads 2 to add 0 to change 0 to destroy with exactly the two audit statements and the one attachment | plan output and document read |  | OPEN |
| A | activation | safe-apply of the saved plan | Apply complete 2 added 0 changed 0 destroyed |  | OPEN |
| V | verify | after-reads G1 to G3: inline policies unchanged, new policy exact, simulations, replan No changes | G1 G2 G3 lines |  | OPEN |

## Log

- 20261021T025345Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
