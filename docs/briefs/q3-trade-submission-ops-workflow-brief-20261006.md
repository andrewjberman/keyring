# L1 BRIEF -- Q-3: trade submission through Opal, led by the operations lead's own workflow

- **Author:** `4.0.0_SA_CRO` (L1), 2026-10-06 ~19:4xZ (3:4x PM Eastern). **Mode:** NEW (research-and-requirements
  phase; Andrew: "begin to understand the requirements").
- **Order:** Andrew-direct 2026-10-06, two records:
  - the goal (voice transcript, ~18:3xZ):
    `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md`:
    "we need to look into and begin to understand the requirements for a trade submission flow that is viable to run
    through opal i believe what this looks like is a ticketing system workflow [...] something that we do need to figure
    out or at least have an inkling on figuring out come january 1st if not have built out the entire pipeline";
  - the direction (~19:2xZ), verbatim in
    `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_192xZ_DELLS_SECHIST_LIFT_PUSH_RHYTHM_RESEARCH_EGRESS_Q3_OPS_WORKFLOW.md`:

    > He doesn't use software he manages everything in Excel and calls the custodians personally; this is where we need
    > to build in, which is why OPLGTW and graphapi ops to MS sharepoint will be essential, using the dashboard at least
    > for ingestion of trade requests. I suspect the fastest way to integrate with him will be getting the MCP server
    > active so his claude ai can at least have freeflowing easy access to the relevant data in aws. we may need to
    > develop additional tooling/integrations for his workflow, but it will lead with his workflow and I think we
    > spearhead frictionless systems for him via the MCP
- **Consumer:** `1.0.0_SA_CTO`, `/endpoint --forward` at L2.

---

## PART I -- THE OUTCOME TERRITORY

### The candidate thread

**One trade request, from an advisor to the operations lead, with nothing re-typed.** An advisor submits a trade request
through Opal's dashboard; it lands where the operations lead works (his Excel workbook in SharePoint) and is visible to
his Claude through the Opal MCP server with the account's data beside it; he calls the custodian as he does today; the
request's status is recorded back in Opal. Every later outcome widens this one.

### O1 -- The operations lead asks his Claude about any account and gets the answer from Opal's data

Positions, cash, recent activity, the model an account follows: available to him in Claude through the Opal MCP server,
scoped to his firm, without a login to another system. Andrew calls this the fastest integration.

### O2 -- An advisor submits a trade request in Opal and the operations lead sees it in the workbook he already uses

Requests come in through the dashboard (Andrew: "using the dashboard at least for ingestion of trade requests") and
appear as rows in his SharePoint Excel workbook, so his way of working does not change.

### O3 -- The operations lead's workbook stays the record he trusts, and Opal reads it without his re-entry

What he marks in his workbook (sent to the custodian, filled, rejected) is read back by Opal through Microsoft Graph, so
the advisor sees the status and Opal keeps the trail.

### O4 -- Anyone can trace a trade from the advisor's request to the custodian's confirmation

Who asked, when, what the operations lead did, and what the custodian confirmed: one trail per request.

### O5 -- The YCharts upload runs as the ticketing system's first workflow

Andrew's first ticketing workflow: an advisor uploads holdings, the in-house report runs (IRPT_YCDGEN), AI investor
commentary follows (NFRA_TRNSPT). The same ticket shape later carries trade requests.

### O6 -- Andrew knows, before January 1, what the full trade-submission pipeline would take

Even if not built by January 1, the requirements are written down: what the operations lead does today step by step,
what each custodian accepts, where Opal fits, and what stays manual.

---

## PART II -- WHERE THE BOUNDARY SITS

**This project owns:** the operations lead's workflow map; the request-to-workbook-to-status loop; the MCP access scope
for him; the trade trail; the requirements document for the full pipeline.

**It relies on, and does not own (MEASURED by name today):**
- **NFRA_OPLGTW** (site Z, executing): Opal Gateway, "authorized Schwab questions and CSV downloads in Claude".
- **The Opal MCP family** on site Z: NFRA_OPALAI (the Opal Analyst, awaiting Andrew's launch), NFRA_MCPINDEX (the tool
  index), NFRA_MCPMSP (the partner-firm analyst, held), NFRA_MCPORTAL (operator console, parked).
- **The Opal gateway's Microsoft 365 tools** already reach SharePoint (site file listing, workbook reads, text upload are
  among its tools in this session).
- **The existing trade pipeline:** `infra/aws/terraform/trade-pipeline` and the portal's `TradeSubmission` page;
  project TRSB_LEDGER (executor authorization and audit trail) was near-complete on 2026-05-18, 11 of 12 task orders
  shipped, now inactive.
- **The existing ticket center:** `infra/aws/terraform/ticket-center` and the portal's `TicketCenter` page; project
  OPAL_TICKET_VNEXT (attachments, chat, notifications) has a PRD and no decomposition.
- **IRPT_YCDGEN and NFRA_TRNSPT** (the first workflow, O5).

**It does not own:** any custodian's systems, the operations lead's phone calls, or a client-facing release.

---

## PART III -- THE QUALITATIVE BAR

1. The operations lead keeps working in Excel and finds his day shorter, not different.
2. No trade request is typed twice by anyone.
3. An advisor never has to call or email to ask where a request stands.
4. Asked "who approved this trade?", anyone answers from one trail.
5. Nothing reaches a custodian that the operations lead did not send himself.

---

## PART IV -- THE SUBSTRATE: what exists, measured

- **F1. A trade pipeline and a trade-submission page already exist** (TRSB_LEDGER, trade-pipeline v1.17.0, portal
  `TradeSubmission`; the CVO graded `/trade-submission` page pins this week). Whether they fit the operations lead's
  workflow is unexamined.
- **F2. A ticket center exists** (`ticket-center`, portal `TicketCenter`), with a vNext PRD at
  `docs/architecture/D7_TICKET_VNEXT_PRD.md` and no decomposition.
- **F3. The gateway already reads and writes SharePoint** through Microsoft Graph (its M365 tool set).
- **F4. The MCP family is mostly built** and partly held or parked (census section 3.2).
- **F5. The operations lead uses no trade software;** Excel and phone calls to custodians (Andrew, ~19:2xZ).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **The operations lead's own description** of his day, his workbook's layout, and which custodians he calls. Andrew
  will work with him; this brief cannot be completed without that sitting.
- **Firm scoping:** his MCP access sees only his firm's data (the cross-firm law).
- **No automatic custodian submission** without Andrew's word: the trail records what the operations lead did; it does
  not send trades.
- **The held MCP pieces** (NFRA_MCPMSP held, NFRA_MCPORTAL parked, NFRA_OPALAI awaiting launch) are released by their own
  owners or Andrew, not by this brief.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-06 ~19:3xZ. No project is registered for Q-3. Phase: research and requirements.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- The operations lead was not consulted; his workflow is described only by Andrew's two sentences.
- Which firm he works for, and which custodians he calls, are not stated here.
- The trade pipeline's and ticket center's fit was not read beyond their register rows and folder names.
- Public web research on custodian trade-submission paths (approved today) has not been done yet.

## REFS

```
  BRIEF PATH        docs/briefs/q3-trade-submission-ops-workflow-brief-20261006.md
  PROJECT           NONE-YET
  ANDREW'S WORDS    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_183xZ_FOUR_BOX_ACCELERATION_PROJECT_CENSUS_AND_Q4_GOALS.md
                    org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_192xZ_DELLS_SECHIST_LIFT_PUSH_RHYTHM_RESEARCH_EGRESS_Q3_OPS_WORKFLOW.md
  RELIES ON         NFRA_OPLGTW; NFRA_OPALAI, NFRA_MCPINDEX, NFRA_MCPMSP, NFRA_MCPORTAL; trade-pipeline + TRSB_LEDGER;
                    ticket-center + OPAL_TICKET_VNEXT (docs/architecture/D7_TICKET_VNEXT_PRD.md); IRPT_YCDGEN; NFRA_TRNSPT
  MEASURED AT       2026-10-06 ~19:3xZ
```
