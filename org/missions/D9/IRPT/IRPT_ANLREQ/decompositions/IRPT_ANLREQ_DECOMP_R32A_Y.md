# IRPT_ANLREQ -- decomposition, round 32A: THE APPLY OF RELEASE 28, LEGS L2 AND L1 (irpt-status words, then the ticket service), workstream YW round 32 (issuer 2.0.0_SA_COO~Y2)

**Input:** the release-28 pair, signed by both halves (COO half blob `e9bb20d7fe2f6d610c88c4399e6a4387af5e7743`, CTO half @d3adae2fc8, CTO msg 7415). The window order is L2, L1, L4, L3. The two Lambda legs that open the window, `irpt-status` (three new finding-code words, words only) and `opal-ticket-api` (the SUBMIT-FORM, own-firm LIST and PACKAGE request-id changes: the authorization widening of section 4a), are applied by the Dell CloudOps lane `0.7.0_AE_CloudOps~AQ2`, which also re-runs the stored-input recount (step R0d) first. L4 (`~YC2`) waits on the message that L1 has closed; L3 (`~AQ2`) waits on L4.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-302` | the apply of L2 then L1: ledgers opened, R0a to R0d read, each unit rebuilt from its recorded inputs at the expected CodeSha256, uploaded, scoped plan, `safe-apply`, after-reads A1 to A3, the map record, ledgers closed | the two Lambdas' code attributes and two S3 object versions; the applier's output file and a map-record commit | WORLD |

## Edges and chains

- One chain, two units in order (L2 then L1). The next window orders (`TO-APPLY-R28b` resident, `TO-APPLY-R28c` Lambda `irpt-ycharts-generate`, `TO-EXERCISE-R28` the synthetic sitting) are cut after this order reports; `R28b` also waits on `AR-y-301` (the resident scripts).

fanout: 1 of 1 chains, cap 8, reason: two sequential applies in one lane under one signed pair; the order between the units is the pair's.
