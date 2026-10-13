# IRPT_ANLREQ -- decomposition, round 21 EXERCISE REQUEST-ID READ, workstream YR round 16 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's ruling on the exercise run (msg 7039, 2026-10-13 ~15:44Z): PASS with row `IRPT_ANLREQ-D2-S74` recorded, no re-run, on one condition -- the record shows the Lambda RequestId of the `disabled` request on its one `row_non_active` line, and that the 3 extra `row_present/admitted` lines of the same sub-window carry OTHER RequestIds; and each identity got exactly one token across the two phases (a second token is a deviation row, not a re-run). The applier's record (`org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r21/`, commit `3596a4a3f5`) carries counts per sub-window and no RequestId.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-230` | a READ of the log group `/aws/lambda/irpt-directory-search` for the sitting window with the RequestId of every invocation and which class lines each carries; a statement of the tokens minted per identity from the applier's own two trace files | one record file, one ledger-free read (no write to any AWS resource) | WORLD |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one read-only act on one log group.
