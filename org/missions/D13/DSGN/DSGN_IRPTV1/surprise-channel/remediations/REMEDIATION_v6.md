# DSGN_IRPTV1: remediations, compile from watermark 2026-10-02T03:10Z

<sweep_watermark>2026-10-11T05:01Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T05:01:57Z, on msg 4114 (1.0.0_SA_CTO~DELL2, 2026-10-11T04:55:59Z): compile from watermark 2026-10-02T03:10Z; no COO packet. Read at portal origin DEV 26f621d5 (ls-remote read 2026-10-11T05:01:57Z). These are reads of code at the DEV tip; no page was
rendered and no suite was run.

## The 8 ARMED rows first

| row | hazard | live at the DEV tip? | disarm owner |
|---|---|---|---|
| W35-S1 | a firm whose shown name is not its key in title case renders wrong | **No. Fixed.** The name is read from the registry-generated view; the transform is deleted. Closed in place (REMEDIATION_v4) | closed |
| W39-S2 | a request is labelled with the header's selected client, whoever's it is | **The mislabel is gone** (no client is printed on a row). Still true: the history route is not client-scoped, so every request of the viewer lists under any selected client, unlabelled | `1.0.0_SA_CTO`: the contract call (a served client field, or a client-scoped route). Standing should read INERT |
| W35-S2 | Export on Analysis is permanently closed | **Yes.** AnalysisTab passes no export signal; the override is set on the reporting tab only. A missing capability, not a hazard to a served number: standing should read INERT | a seated lane, one cell |
| S7 | the unit suite mixes legacy failures with regressions | **Not measured here.** The last figure on record is 18 failing of 967 on 2026-10-02 (STATUS.md), a different set from the row's 80 | a seated lane |
| W21-S2 | the suite fails outside the class table's Q rows | **Not measured here** | a seated lane |
| W23-S1 | the suite is not deterministic across full runs | **Not measured here.** No three-run sample is on record since 2026-09-27 | a seated lane |
| W29-S10 | two three-run samples gave different failing sets | **Not measured here.** Waits on the same sample | `1.0.0_SA_CTO`: how the bar is graded |
| W34-S1 | fe-s-45 fails intermittently under the pinned runner | **Its cause has a fix on record** (row W34-S2: the fixed port range). The sample that proves it has not been taken | a seated lane |

**One act closes five of them:** one pinned three-run sample of the Investor Reporting suite at the DEV tip. An identical failing set
closes W23-S1, W29-S10 and W34-S1; that set, ruled test by test, closes S7 and W21-S2.

## Graduated this compile: 2 rows, OPEN, INERT

```json
[
 {
  "id": "DSGN_IRPTV1-S60",
  "project": "DSGN_IRPTV1",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The pin upload-accept-suggestion renders the 'Did you mean' row and its button and never presses it. A click handler that fills nothing, or fills another ticker, passes the pin. The fill and the re-post are correct at head by this seat's probe of 2026-10-04 and are pinned by no test.",
  "evidence": [
   "investigation row DSGN_IRPTV1-S60",
   "S60: git show origin/DEV:.../__tests__/dsgn-irptv1/upload-accept-suggestion.test.tsx holds no click, press or fireEvent line; no other test under __tests__ presses the suggestion button"
  ],
  "remedy": "One component test that presses the button and asserts the re-post's corrections. The owner places it on a seated lane.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-S61",
  "project": "DSGN_IRPTV1",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "On a corrected upload row the Holding cell shows the uploaded symbol while the dollars are the corrected security's. An advisor reads one ticker beside another security's dollars.",
  "evidence": [
   "investigation row DSGN_IRPTV1-S61",
   "S61: git show origin/DEV:.../tabs/analysis/ProspectComposer.tsx:563 -- the Holding cell reads original.symbol first; no line in the page source names a correction on that row"
  ],
  "remedy": "The Holding cell names the corrected security on a corrected row (and may show the uploaded symbol beside it as 'uploaded as'). The owner places it on a seated lane; it is a served-page wording fix.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v6"
  },
  "closed": false
 }
]
```
