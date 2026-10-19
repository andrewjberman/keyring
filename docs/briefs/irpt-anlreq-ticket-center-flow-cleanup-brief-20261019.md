# BRIEF (midstream) -- IRPT_ANLREQ: the Ticket Center analysis request, walked by Andrew, cleaned to what the flow needs

Author `4.0.0_SA_CRO~TCKT` (dell2), 2026-10-19. Mode: `--midstream`. Consumer: `1.0.0_SA_CTO~DELL2`, `/endpoint --forward`, as a
PRD addendum to `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (v0.22).

Authority (verbatim records, same folder):
- `org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/ANDREW_DIRECT_20261019_165xZ_TCKT_ANALYSIS_REQUEST_FLOW_BREAKS.md` @018f22da23
- `org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/ANDREW_DIRECT_20261019_18xxZ_TCKT_NO_ADVISOR_EMAIL_COMMENTARY_DEFAULT_ON.md` @c15be009b2

Evidence (gap ids G1-G10 cited below): `org/tier1_exec/4.0.0_SA_CRO~TCKT/deliverables/TCKT_ANLREQ_FLOW_GAPS_20261019.md` @c15be009b2.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

- Not read: the project's task-order files, its `phase` / `blocking` fields, its decompositions.
- Read: the PRD's ENDPOINT, CONTRACTS, section 1 and addenda v0.6, v0.9, v0.10 (purpose and acceptance); the served code at portal
  `origin/DEV` and in `infra/aws/lambda/investor-reporting/`; live AWS reads of one ticket (TCK-20261017-5af976ff), its request
  record and run.json, and the upload function's logs for Andrew's 2026-10-19 16:38-16:39Z attempts.
- **Where it bent.** The research subagents ran `git log` on the touched files, so cell ids reached this brief as provenance:
  AR-y-275 (added the report-type dropdown, portal `80d7c70a`), AR-y-378 (added the advisor-email field), AR-y-404 (`4050bbd629`,
  drops builder-only cards). Each is cited only as WHY a defect exists, never as a reason to keep it. The ratifying risk sits exactly
  there: AR-y-275 and AR-y-378 were deliberate, and this brief reverses both on Andrew's word of 2026-10-19.
- **"Unchanged" finding.** FWD-1's direction is unchanged: one request, form to four attachments on the open ticket, nobody in between.
  It has not been realized: zero package outcomes 2026-10-10 to 2026-10-19 (G7). The failure is mostly in execution and accretion,
  not direction. What Andrew's word CHANGES in the ratified text is listed in Part V.

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1, unchanged in shape):** an Opal staff user signed in on DEV files one Analysis Request for 49 Financial: one
holdings XLSX, two Opal models plus one other ETF (Multi-Comp variant 3 by count), no other inputs; the still-open ticket ends with the
four attachments. Andrew's 2026-10-19 sample (screenshot 1) is that thread.

### O1 -- An Opal staff member files for any partner firm without being stopped
The person signed in is the filer. No typed email, no advisor lookup, no firm-list readiness gate, no `allowedFirmIds` membership
check stands between an Opal user and Submit for any firm. Today: G1 (NOT_AUTHORIZED from the advisor lookup), G2 (firm list holds
Submit), G9 (typed advisor email). The firm still binds every downstream hop (C-FIRM's binding half is untouched).

### O2 -- The filer answers only what the system cannot infer
No report-type dropdown: zero comparables is an Overview (variant 1), one a Comparison, two or more a Multi-Comp (variant 3). No
"Add commentary" checkbox: every request gets commentary. The filer cannot file a request whose type disagrees with its picks,
because there is no type to disagree. Today: G3, G10.

### O3 -- The Opal models are on the form the moment it opens, in text a person reads at a glance
The five Opal model choices need no connection: they render at first paint, large. Today they wait on a four-step chain (firm list,
firm choice, a 400 ms pause, a catalogue fetch) and are never retried on failure (G4); the "form as filled" attachment re-fetches the
same list per package only to print names (G5).

### O4 -- Nothing on the form waits on a connection whose answer is static or unused
A sweep outcome: every wait in the form and the ticket page either gates something the person needs from the network at that moment,
or is gone. Only the free-text "Other ETFs" check legitimately needs the served catalogue. G4 and G5 are the known instances; the
sweep is the outcome, so instances found later are in scope.

### O5 -- An Opal person opens the still-open ticket and finds the four attachments
The original upload, the form as filed, the Opal report PDF, the commentary PDF marked DRAFT, each its own attachment, opened from
the ticket. A commentary failure does not withhold the other three: they attach when the report is complete, the commentary when it
is drafted (and the ticket says which step failed, per FWD-4). Today: the packager is reached only when `commentary_requested` is
True (`resident_worker.py:254`); TCK-20261017-5af976ff holds a COMPLETE 61-page PDF and its upload, neither attached; the board cannot
open the PDF at all (G7). Report link written two days after acceptance (G8).

### O6 -- "Open report" shows the report, not its construction log
A person who opens a report reads the report. Today "Open report" renders every element of the PDF layout map as a card: 427 for
REQ-d6231c013ae90519c67d18e9, 3 with values; the green SUPPORTED badge is the report's, not the card's (G6). The element trace may
stay behind "Technical details" for an Opal operator; it is never the default view.

### O7 -- A Multi-Comp report shows each chosen comparable against the portfolio
The comparison figures are present for every comparable picked. Today the Multi-Comp run's `calls` is `[]` and 144 vendor-sourced
elements read not available (G8; that the PDF's comparison figures are empty is INFERRED, not opened). This is FWD-7's territory;
it is listed so the walk's evidence is not lost, not as a new endpoint.

## PART II -- WHERE THE BOUNDARY SITS

- **IRPT_ANLREQ owns** (C-ABSORB): the Ticket Center Analysis Request parts (`portal/src/pages/TicketCenter/`), the upload door
  (`intake/uploads.py`), the Opal engine and resident (`ycharts/generate/*`, `ycharts/research/*`), the packager, the commentary.
- **IRPT_BCKEND (`~P2`) owns** auth and routes: the O1 owner fallback lives in `_authz/served.py` (`_create_owner`, `_advisor_owner`,
  lines 1069-1111), so O1's backend half is a cross-project write the CTO must place (cell in IRPT_BCKEND, or a C-ABSORB amendment).
- **TCKT_VNEXT owns** the ticket service; `report_type` stays a stored field from its fixed enum
  (`ticket_center/lambda_function.py:78, 119-121`), derived by the client from the count (O2) with no service change.
- **InvestorReporting render** (`NativeSections.tsx`) is shared with the Analysis tab (FWD-6); O6 changes what the TICKET opens, and
  must not regress the Analysis tab's manual path.
- Out: the partner-firm UI path (parked by v0.6 until the Ticket Center is shown to client users). O1 is about Opal users only.

## PART III -- THE QUALITATIVE BAR

- Andrew, signed in as himself, files his own 2026-10-19 sample (49 Financial, the Skudlarick XLSX, two models plus SPYM) and is not
  refused, and is never asked for an email or a report type.
- The model checkboxes are readable before he reaches them; he never sees "The Opal model list is not loaded."
- He opens the ticket and finds four files he can open, not a list of hundreds of cards he cannot interpret.
- A seat demonstrating any of this with a synthetic advisor or a pre-seeded directory row has not met the bar: the point of O1 is that
  the real staff path works with nothing seeded.

## PART IV -- THE SUBSTRATE (findings, measured)

- F1. Backend already derives the variant from the count and accepts `variant: "auto"` (`ycharts/generate/submission.py:72-74`,
  `recipe.py:138-163`). O2 needs no backend change.
- F2. Staff are already authorized by `authorize_current` (`_scope/interactive_access.py:115-116`); the refusal is in owner
  resolution, not authorization. `access.prospect_owner()` exists as the staff owner (I: fallback untested).
- F3. The five Opal models are a static `templates.json` in the backend (`comparison_catalogue.py:127-149`); the portal already holds
  the five names (`getAllModelColors()`).
- F4. The four-attachment reader exists on the board (`AnalysisRequestParts.tsx` package list); it renders only when the ticket
  carries `package`, which no ticket has had since 2026-10-10.
- F5. AR-y-404 removes 280 builder-only cards from new reports; stored reports are not rewritten; deployment not read.
- F6. ADDENDUM v0.6 (2026-10-14) already records Andrew: "Opal staff should not be 'held' from filing". O1 restates and widens it: the
  served path still holds them five days later, through a different gate.

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The ratified ENDPOINT text moves: FWD-1's "The form carries the variant chosen (Overview, Comparison, Multi-Comp)" and FWD-2's
  "the form offers the analysis types" become count-derived; FWD-1 gains commentary-always; C-FIRM's "the choice must be in its
  explicit `allowedFirmIds`" conflicts with O1 ("on behalf of any firm") and needs the CTO's restatement. Both halves re-open.
- O1's backend half and O1's portal half (removing the email field) must land together: the field alone makes staff hit
  `served.py:1089-1091` ("must name the firm advisor").
- O5 needs the packager's trigger to stop depending on commentary; O2's commentary-always makes it reachable meanwhile.
- Portal pages touched are the Ticket Center (internal-only per v0.6): Opal-internal class for the approval route.

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-19, 16:38Z-18:xxZ:
- Upload refusal: `irpt-ycharts-generate` logs 16:38:54Z, 16:39:17Z: INTERNAL caller admitted, `ProspectOwnershipRefused`,
  NOT_AUTHORIZED. `opal-partner-49financial` 11 rows, no dawson.moses; `opal-users-v2` 86 rows, none.
- TCK-20261017-5af976ff: `add_commentary: false`, no `package`; run.json COMPLETE, PDF ART-1630441c (290,707 bytes);
  `report_ref` written 2026-10-19 13:42Z for a request accepted 2026-10-17 05:14:30Z.
- Package outcomes 2026-10-10 to 2026-10-19: zero (the `~IB2` resolve-live notes and `A_RESIDENT_PACKAGER.txt`).
- Portal citations are `origin/DEV`; the dell2 `portal/` checkout is 141 commits behind.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It did not open the 61-page PDF; O7's "comparison figures empty" is inferred from `calls: []` and element status.
- It did not test the `prospect_owner()` fallback, nor read whether AR-y-404 is deployed.
- O4's sweep covered the form and its catalogue chain; the ticket page's status reads and the board's refresh were read only where
  they touch the form (the per-ticket status read was judged legitimate). A wider sweep is O4's work, not this brief's.
- It does not say whether the 2026-10-16 date field on the form (screenshot 1) is a needed-by date or a residual price-date input
  (v0.16 retired price-date selection); a reader should check it under O4.
- It does not decompose or sequence.

## REFS

```
  BRIEF PATH        docs/briefs/irpt-anlreq-ticket-center-flow-cleanup-brief-20261019.md
  PROJECT           IRPT_ANLREQ (D9/IRPT, fabric dell2)
  EXISTING PRD      org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md (v0.22)
  SIBLING PROJECTS  IRPT_BCKEND (auth/routes, served.py), TCKT_VNEXT (ticket service), IRPT_DASHBD (TWR engine, FWD-7 overlays)
  PRIOR ART         F1-F5 above; G1-G10 in TCKT_ANLREQ_FLOW_GAPS_20261019.md
  MEASURED AT       2026-10-19 16:38Z-18:xxZ (Part VI)
```
