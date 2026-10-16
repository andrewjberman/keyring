# IRPT_ANLREQ -- decomposition, round 58, workstream ~T (issuer 2.0.0_SA_COO~T2)

**Input:** `2.0.0_SA_COO~V2` msgs 9657 and 9665 (TCKT_VNEXT round 4 sitting 2; CTO rulings 9637 and 9651): the page read of a failed commentary hop needs a second drive of the SAME synthetic job row, now that the first drive (TO-APPLY-t55, complete) was read without words because the ticket has no report_ref. Arm B (a packaged ticket) has no job row and is a page-only read.

## Cells

| cell | outcome | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-tf-79` | FWD-4 | ONE direct refused-body invoke of the live commentary function on the synthetic row, the failure held until V2's page read, then one conditional removal | one attribute of one `irpt-jobs` row (applier) | WORLD (a live write; no deploy) |

## Edges and chains

- One chain (M = 1); follows AR-tf-78 (complete). V2's own order (fixture write, page read) chains behind leg A and is not this decomposition's.

fanout: 1 of 1 chains, cap 4, reason: one applier act, one cell
