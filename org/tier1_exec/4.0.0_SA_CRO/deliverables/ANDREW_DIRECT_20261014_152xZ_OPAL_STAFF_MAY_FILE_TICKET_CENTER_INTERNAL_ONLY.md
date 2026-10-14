# ANDREW DIRECT -- Opal staff may file in the Ticket Center (for testing); the Ticket Center is for Opal users only for now (2026-10-14 ~15:2xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. He was answering the first slice of the /closer trace
of the analysis-request workflow. The slice found that partner advisors cannot reach `/ticket-center` on any deployed build: the
partner reach is a vite-dev-only flag, `isPartnerDevReach`, at `portal/src/lib/firmAccess.ts:141-153`@6a5926fc. It also found that the
form holds an internal user's submit ("Choose the firm this request is filed under", `analysisRequest.ts:227`, `filingFirm` returns
`''` for internal users, `AnalysisRequestParts.tsx:100-104`).

**Verbatim:**

> Opal staff should not be "held" from filing, they can file they just realistically won't, but we should have that available for testing. Ticket Center does not need to be displayed for client users at this time, only opal users need to see it, so that part is accurate.

## What it sets (surfaced, not adjudicated)

- **Opal staff CAN file an Analysis Request in the Ticket Center.** The internal-user submit hold is a defect against this word. Filing
  by staff exists for testing.
- **The Ticket Center is shown to Opal users only, for now.** A partner-firm advisor not reaching `/ticket-center` on a deployed build
  is correct today, not a defect.

## What it touches (for the owners to rule; this seat does not widen or narrow it)

- Pivot direction `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md`, O1 and section 6.
  Those make the synthetic partner-firm advisor FWD-1's driven arm, and they say "Do not design for an Opal staff member filing in the
  Ticket Center". This later word allows staff filing for testing and keeps the Ticket Center internal for now.
- IRPT_ANLREQ PRD v0.5 FWD-1 and ADDENDUM v0.5: the filer and the driven arm. The partner-reach cells AR-y-282 and AR-y-283 are also
  touched.

-- recorded by 4.0.0_SA_CRO~DELL2
