# IRPT_ANLREQ -- decomposition, round 22 ANALYSIS REQUEST FORM (Andrew's smoke), workstream Y, the CTO's O1 issuance (issuer 2.0.0_SA_COO~Y2)

**Input:** Andrew's smoke on DEV (~18:2xZ), relayed by the CTO (msg 7151, "your next issuance, ahead of anything else"), recorded as rows `IRPT_ANLREQ-D2-S79` to `-S82` with his words verbatim: "we're missing the Opal Ultra Short-Term, also they should be arranged in canonical order with canonical color checkboxes that take that color when checked. Also the Advisory Fee doesn't need to be included ... These would largely be from prospects so we'd have no way of knowing their fees ... also add commentary checkbox doesnt do anything." The form is `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx` (read by this seat at portal DEV `cf52fdbf`). The CTO's rulings: (1) every Opal model in the catalogue is listed, Ultra Short-Term included -- read why it is missing; (2) canonical model order and each checkbox in its canonical color when checked, both reused from the estate's model palette; (3) remove the Advisory Fee field (reports are before advisory fees); (4) "Add commentary" sends `commentary_requested` (J1, the form half).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-261` | READ ONLY: why the Opal Ultra Short-Term model is missing from the served comparison catalogue, whose lane the fix is in, and the estate's one canonical order | one record | LOCAL |
| `AR-y-262` | the form lists the Opal models in the canonical order and each checkbox shows its canonical color when checked, both from the estate's own function and constant | a portal candidate branch (`src/` only) | LOCAL |
| `AR-y-263` | the form drops the Advisory Fee field and sends no fee, after the ticket service is read for what it does without one | a portal candidate branch (`src/` only) | LOCAL |
| `AR-y-264` | the "Add commentary" box reaches `commentary_requested`: a read of every hop from the checkbox to the packager, and the portal half of the fix if the break is in the portal | a portal candidate branch (`src/` only) | LOCAL |

## Edges and chains

- None between the cells. `AR-y-262` to `AR-y-264` edit one component in disjoint hunks (the checkbox list, the fee input and its state, the commentary checkbox and the answer builder) on three branches off the DEV tip, so the CTO lands them in any order and a one-line conflict near the fee and commentary inputs is possible. `AR-y-261` decides the server cell for the missing model, if the cause is on the server.

fanout: 4 of 4 chains, cap 8, reason: four independent items of one smoke, one read and three candidate branches.
