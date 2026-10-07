# IRPT_CUSTDY -- surprise channel, INVESTIGATION v1 (dell2 placement)

**Opened by:** `2.0.0_SA_COO~K2` at the round-1 issuance. **Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py`
validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A seat's row is
`IRPT_CUSTDY-S<k>`; a worker's is `IRPT_CUSTDY-W<n>-S<k>`. **Append-only during the round.** Never edit an existing row.

## IRPT_CUSTDY-S1 -- the render path's input is a portal export request; whether it renders a client-report document is unmeasured

```json
{
  "id": "IRPT_CUSTDY-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~K2",
  "surfaced_at": "2026-10-07T08:12:00Z",
  "one_line": "The PRD's S07 marks the render on irpt-export-render as held, but that path renders portal pages through a minted token, and whether it can render a client-report document is unmeasured.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_CUSTDY/prd/IRPT_CUSTDY_PRD.md v0.2 @c2bc15f427 section 6 row S07: claim 'held', verb 'wire'",
      "infra/aws/terraform/investor-reporting/export/b2_render.tf lines 1-17 at dell2 HEAD: submit-export mints a render token into SSM /irpt/render-token/<ATT-id> and dispatches a render host that renders the read functions' render ports",
      "aws lambda get-function irpt-export-render, 2026-10-07 ~07:5xZ: Active, LastModified 2026-10-06T01:35:28Z"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.2 S07: the render on the IRPT_BCKEND export path is held; round 1 wires the template to it.",
  "world_is": "The path exists and is live, but its input is a portal export request, not a document. Cell CU-a-4 reads the path's input contract from source and reports accepts_document; a gap is routed by the issuer to IRPT_BCKEND's COO at the drain, never written into IRPT_BCKEND's paths."
}
```

## IRPT_CUSTDY-W2-S1 -- CU-a-2 chose one reading of five open figure rules

```json
{
  "id": "IRPT_CUSTDY-W2-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_IRPT_CUSTDY~2",
  "surfaced_at": "2026-10-07T08:29:35Z",
  "one_line": "The client-report contract leaves five figure rules open; CU-a-2 chose one reading of each and states it in the module docstring.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/irpt_custody/client_report_figures.py module docstring, THE RULES THIS BUILD STATES (this worker's branch wk-IRPT_CUSTDY-2)",
      "data/assets/scripts/gold/runners_49f/parity_period_returns.py:link -- SI with no anchor returns UNAVAILABLE-NO-ANCHOR, a window that is undefined",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py:247 COLUMNS -- the gold carries total_return_daily and market_value_eod, not the linker's r_net/r_gross"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Decomposition contract: statuses OK|NO_DATA|WINDOW_NOT_RULED; household_returns by the same linking; account 'last 4 only in any printed output'; fees = Schwab fee rows labelled SCHWAB_TXN_FEE_ROWS; SI window per the linker.",
  "world_is": "Readings taken where the contract is silent. (1) SI with no inception anchor maps to WINDOW_NOT_RULED (window null), every other UNAVAILABLE-* to NO_DATA; SI anchor = accounts-file inception, else the gold manifest first_data_date. (2) The gold's total_return_daily feeds the linker as r_net and r_gross (it is gross of advisory fees). (3) A household return links a daily series weighted by prior-day market_value_eod and is OK only when every member account is OK. (4) The document's account field carries the last 4 only, not just the printed lines. (5) Fee amount is the signed sum of fee-class rows (a charge is negative) and is null when a QTD trading day has no fact_trn partition. The issuer or CTO may overrule any of the five; each is one function in the module.",
  "notes": "Real-neighbour read: --coverage on masters 08335338 and 08242234 at as_of 2026-09-30 both read_ok=True, as_of_covered=True (latest 2026-10-05). The worker ran no --apply and wrote no S3 object."
}
```
