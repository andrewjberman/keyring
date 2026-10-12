# DSGN_IRPTV1: remediations, rounds 24 to 30

<sweep_watermark>2026-10-12T22:00Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T22:00:00Z. Follows ADJUDICATION_v19. L8 input: msg 6600 and `org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261012T13Z_desktop-n8rjv0a.md lines 13-17`; the held compile of round 23
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_REMEDIATION_ROUND_23_HELD_20261011.md`, removed in this commit). No judgment criterion.
Graduated, round label v31: 8 rows, OPEN; BLOCKING 2 (D2-W62-S2 shared table warning; D2-W65-S1 portal wire drift); ARMED 0.
Owners: `2.0.0_SA_COO~D2` 7, `1.0.0_SA_CTO~DELL2` 1. Three need a grant on a shared component or Andrew's word: D2-W60-S1 and D2-W62-S2 (shared components),
D2-W61-S2 (a PROD push whose print closure changes).

```json
[
 {
  "id": "DSGN_IRPTV1-D2-W60-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-108: the Total Assets figure and its heading are drawn by portal/src/components/CategoryViewTree.tsx, outside the grant, so its base is a caption above the card, not a label inside it",
  "evidence": [
   "investigation row D2-W60-S1"
  ],
  "remedy": "The Total Assets base sits inside its card, which needs a grant on the shared portal/src/components/CategoryViewTree.tsx; the header's account-row case, held by a test only, is read on a rendered page.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v31",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v31"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S24",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Laptop walk XB-c5ce face 11: with an ACCOUNT row picked in the header's search, Performance's Account select does NOT start on the picked account on a served answer; IV-e-108 recorded hands_tabs true on a test alone",
  "evidence": [
   "investigation row D2-S24"
  ],
  "remedy": "On a served answer with an ACCOUNT row picked in the header's search, Performance's Account select starts on that account; proven on a rendered page, not a test alone (IV-e-108 recorded hands_tabs true on a test).",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v31",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v31"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W62-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-114: the React colgroup warning is reproduced in a development build and traced to portal/src/components/holdings/HoldingsBreakdownTable.tsx:294-298, a shared component outside this order's grant, so present_after false cannot be met by an edit this order permits",
  "evidence": [
   "investigation row D2-W62-S2"
  ],
  "remedy": "The React colgroup warning is in the shared portal/src/components/holdings/HoldingsBreakdownTable.tsx:294-298. A cell with a grant on that component removes it; until then present_after false cannot be met by this project's orders.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v31",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v31"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S21",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Laptop walk XB-c5ce: an opened vendor report on a SERVED answer shows section codes for titles, 'Unit: unknown' on every card, and no validation or source line on its face",
  "evidence": [
   "investigation row D2-S21",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/WALK_2_RESULT_READ_20261012.md"
  ],
  "remedy": "Narrowed by walk 2: titles and units are PROVEN fixed on a served vendor report (103 of 104 census titles, the chart token fixed by IV-e-118 on DEV; 0 of 104 'Unit: unknown'). Open: the face carries no validation line and no source line (answers 5a, 5b; UIR-45). One page cell; the validation object's four keys are on the wire.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v31",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v31"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S22",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Laptop walk XB-c5ce: three served answers came back UNAVAILABLE with FIRM_BINDING during the walk and nothing on any face says so",
  "evidence": [
   "investigation row D2-S22"
  ],
  "remedy": "Three served answers came back UNAVAILABLE with FIRM_BINDING and no face says so. The page states an unavailable answer and its reason code on its face.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v31",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v31"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W63-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-115: the producer's contract fixtures, and the page's copies and fixtures derived from them, send a vendor section with section_type annualized_return and units DECIMAL_FRACTION, which the producer's extractor cannot send",
  "evidence": [
   "investigation row D2-W63-S1"
  ],
  "remedy": "The producer's contract fixtures send section_type annualized_return and units DECIMAL_FRACTION, which the extractor cannot send, and the page's fixtures are derived from them. The fixtures' owner (the producer's project) aligns them with what the extractor sends; routed by the CTO.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v31",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v31"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W65-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-117: two whole-scope tests (iv-e-26 wire-regen, iv-e-98 generators-drift) FAIL at the base ad774c6f9e: the workspace contract AnalysisSubmissionRequest has commentary_requested that the portal wire file lacks; IV117-AC1 asks suite_after fail 0",
  "evidence": [
   "investigation row D2-W65-S1"
  ],
  "remedy": "The portal wire file lacks commentary_requested, which the workspace contract AnalysisSubmissionRequest carries, so iv-e-26 wire-regen and iv-e-98 generators-drift fail at the DEV head (the same two IRPT_BCKEND row D2-W338-S1 saw). Regenerate the portal wire from the contract; every later order's 'no new failure' bar rests on this base until then.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v31",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v31"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W61-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-111: the print route's import closure (106 source files from src/pages/InvestorReporting/render/PrintEntry.tsx, from the build's module graph) holds four of the candidate's changed files; the verdict is WAITS_ON_ANDREW",
  "evidence": [
   "investigation row D2-W61-S2"
  ],
  "remedy": "IV-e-111's print-route closure (106 files from PrintEntry.tsx) holds four of the candidate's changed files; the verdict is WAITS_ON_ANDREW. A PROD push of that candidate waits on Andrew's word. The Investor Reporting page is Opal-internal by its route, but the printed report is the client's.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v31",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v31"
  },
  "closed": false
 }
]
```
