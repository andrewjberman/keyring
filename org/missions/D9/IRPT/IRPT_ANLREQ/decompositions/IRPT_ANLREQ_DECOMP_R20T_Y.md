# IRPT_ANLREQ -- decomposition, round 20 SUITE EXPECTATIONS, workstream YR round 10 (issuer 2.0.0_SA_COO~Y2)

**Input:** the status-rule rebase (`AR-y-212`, `AR-y-213`, drained @6703116dd4 and @97896cf32d) found three function suites whose expectations encode the pre-rule binding, and the CTO ruled (msg 6882): an internal caller with no users row, or a row whose status is not exactly `active`, is REFUSED; an active row binds as before; service subjects unchanged; the three suites' expectations move to that and nothing else in them. The directory-search and export-render suites import the trunk's `_authz/served.py`, which already carries the rule, so they are red at the trunk head today; narrative's staging was moved to the new pin by `AR-y-212`.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-216` | the failing expectations of the narrative, directory-search and export-render suites moved to the rule (test files only), no test removed, the failures that also fail with the original bytes left as they are | the three suites' test folders | WORLD |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent test-only cell over three folders.
