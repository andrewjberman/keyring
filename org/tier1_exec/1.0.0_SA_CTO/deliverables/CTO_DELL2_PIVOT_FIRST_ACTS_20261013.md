# CTO dell2 -- first acts under the pivot direction (2026-10-13 ~18:1xZ)

**Author:** `1.0.0_SA_CTO~DELL2`. **Order:** crossbox `XB-20261013T180328Z-d4a5` (ACKED 18:10:43Z), body
`org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` (ACCEPTED by Andrew ~17:4xZ). Sections 1 and 2
were read in full. The box priority from now: **O1 and O2 (the analysis-request workflow with four attachments on the open ticket) outrank
everything on dell2** for seats and budget.

## Act 2 -- call 1, the C-SWITCH allow-list addition for ticket-filed requests only: RULED, with one read first

The direction names `svc-irpt-analysis@opalinvest.com` (`IRPT_YCDGEN INVESTIGATION_v1.md:2307`) and asks this seat to confirm that
it is the principal a ticket-filed request reaches the producer as. **Not confirmed by any read here.** The one-step filing runs in the
advisor's browser (`fileAndRequestAnalysis`, `analysisRequest.ts:304-322`), so the request may arrive as the ADVISOR's principal. In
that case, adding a service principal changes nothing for ticket filings.

**Ruling:**
1. `2.0.0_SA_COO~G2` first reads which principal `producer_for` (`resident_worker.py:126-131`) receives for a ticket-filed request,
   from code (the route, the entry and the worker). It is one read cell.
2. **If it is a service principal:** add exactly that principal to `OPAL_PRODUCER_PRINCIPALS`, under a never-widen pair.
3. **If it is the advisor's own principal:** the release keys the Opal producer on the request carrying a `ticket_id` that the ticket
   table confirms is an `analysis_request` ticket. No human principal is added, and the list's comment ("No other principal goes on
   this list") stays true. The pair names that rule.
4. Either way the pair's blast radius is "ticket-filed requests only". A non-ticket request by a non-listed principal still takes
   the YCharts path. The negative arm proves this.
5. **Distinct from the IB-pr-456 word** (~17:0xZ): no agent principal is added for the BEFORE run. Andrew submits it via PROD himself.

## Act 3 -- call 2, the synthetic partner-firm advisor drives FWD-1: RULED

FWD-1's driven arm is an agent filing as a synthetic partner-firm advisor on portal DEV. The mint and the delete each happen under a
never-widen pair; precedents are TCKT_VNEXT R2-cw-1 and IRPT_ANLREQ round 21. Andrew's own filing and Alyssa's (`3cb1`) are the
organic arm, never the gate. **Open call `2e30` is CLOSED, SUPERSEDED** by
`ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md` call 2.

## Act 6 (part 1) -- the AdvisorBookFeePanel guard: ALREADY MET

The panel's mount was reverted on portal DEV at `f6ef1d25` (landed by MSTR 13:41Z, on dell1 CTO msg 4847 and Andrew's smoke). The
component file stays, unmounted. No second fee panel rides the promote. The round-4 enrichment list for ADVI_BILLING follows at its
next list; the project stays parked for seats.

## The open calls of direction section 3, put to Andrew as cards (dell2 list)

1. Call 7: which templates were "sent last week", and who approves the default report's template.
2. The commentary model: Kimi K3 as wired, or "Astra".
3. The portal PROD promote: the direction holds the ticket pages for PROD until O1 passes on DEV, but Andrew's card-9 word was
   "if that passes, yes we can promote". **The later accepted direction governs.** This seat asks him once whether the localhost smoke
   promote goes ahead now (the Ticket Center pages ship with it, because `/prod-deploy` ships DEV whole) or waits for O1.

## Next acts (direction section 8, items 4, 5, 7 and 9)

At each project's next round-N analysis:
- IRPT_ANLREQ: the FWD-1 four-item ENDPOINT addendum and the J1, J2, J3, J5 and J6 cells; reader rounds stop.
- IRPT_YCDGEN and NFRA_TRNSPT: the re-points.
- ADVI_COTBKF: round 82, the one active-set and reverse-match cell, then PARK.
- IRPT_DASHBD: after the 2026-10-14 ledger read, the default-report outcome.

-- 1.0.0_SA_CTO~DELL2
