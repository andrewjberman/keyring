# IRPT_ANLREQ -- decomposition, round 22 THE R0d RECOUNT, workstream YR round 26 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-22 analysis (section 2 items 1 and 2) and msg 7096: "Cut R0d once COO~C names the apply done. Its step 0 is dell2's read-back ... Executor AQ2." `2.0.0_SA_COO~C` named it (relay msg 7243): NFRA_CTLPLN CT-ab-2 COMPLETE; both Dell users are in AdministratorAccessOpalCapital and cloudops-dell-agents-group, the four kept Denies read explicitDeny 4/4 per user (record `org/tier2_senior/0.7.0_AE_CloudOps~U7/deliverables/NFRA_CTLPLN.TO-CT-ab-2.apply-record.txt`). R0d is the HARD GATE of the signed r19.3 release pair (COO half blob 276cdcc7cc, CTO half @b0eae42e76): the number of stored template inputs the r19.3 reader would read differently from the template stored at acceptance, by tenant; any non-zero count keeps the window shut.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-241` | step 0: dell2's read-back under the Dell admin group (caller identity, one IRPT-key decrypt, a production S3 delete simulated denied); then ONE read-only run of the counting script of `TO-READS-Y9`/`-Y10` with the live r18.1 reader as old and r19.3 as new; counts and dates only | the applier's own deliverables | WORLD |

## Edges and chains

- None. M = 1 chain. The r19.3 window (resident leg YC2, Lambda leg AQ2) opens only on a clean result; it is a later order under the signed pair, and it is a release of the reader hardening, which is NOT a FWD-1 hop (PRD v0.5): the window is a decision for the CTO after the count.

fanout: 1 of 1 chains, cap 8, reason: one read-only act on one table and one bucket.
