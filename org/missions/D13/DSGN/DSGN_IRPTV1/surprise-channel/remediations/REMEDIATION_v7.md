# DSGN_IRPTV1: remediations, rounds 11 and 12

<sweep_watermark>2026-10-11T07:05Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T07:05:06Z. Inputs: msgs 4273, 4276 and 4335. Grades: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND_11_L9_GRADE_20261011.md`; the round 12 answer: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND_12_L9_ANSWER_20261011.md`.
Graduated, round label v13: 10 rows, OPEN, INERT. Still ARMED from earlier files: S7 and W21-S2.

**Three things for the CTO's analysis:**
1. **An API-runner trace with no rendered page does not meet FWD-1.** The draft pair defaults its page step to not run; as drafted it
   authorizes a run that grades nothing.
2. **The 14 KNOWN-LEGACY suite rulings are not accepted as labelled.** None cites a ruling that retires the assertion. S7 and W21-S2
   stay ARMED until each of the 43 failing ids is a regression with an owner or an assertion retired by ruling.
3. **The press test stays the only test on React's private dispatcher** until the CTO decides how the portal presses things.

```json
[
 {
  "id": "DSGN_IRPTV1-D2-W43-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Eighteen suite failures come from the contract files being ahead of the portal half (custody-report routes, 22 against 21 operations, unprojected_grant, download_route). The suite's identity is a pair of commits, not the portal tip alone.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W43-S2",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/SUITE_SAMPLE.json"
  ],
  "remedy": "The portal half catches up to the contract (routes table, envelopes, content pins), or the CTO rules which side moves. The sample then names both commits.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W43-S3",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Five failures at the DEV tip are named in no earlier row. Two need an early look: F40-AC5 (the portal calendar disagrees with lib/trading_calendar.py, fallback years 2010 against 2024) and F47-AC6, which was recorded fixed on 2026-10-03 and is red again.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W43-S3",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/SUITE_SAMPLE.json",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND_11_L9_GRADE_20261011.md"
  ],
  "remedy": "Each of the five gets a ruling or a fix. F40-AC5 first: a calendar that disagrees with the trading calendar can mislabel a day on a served page.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W43-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Six tests spawn bun at a hardcoded path under another user's profile, so they fail on any other box whatever the product does.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W43-S1",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/SUITE_SAMPLE.json"
  ],
  "remedy": "The tests resolve bun from the environment (the workspace law: derive, do not hardcode).",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W46-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The served upload-review row carries no display symbol for the corrected security; the page matches the row's uploaded symbol against disclosures.corrections[].from_value to find it. Two rows with the same uploaded symbol, or a correction with no disclosure, would not be told apart.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W46-S1",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/S61_FIX.json"
  ],
  "remedy": "IRPT_BCKEND serves the corrected display symbol on the row, and the page reads it there. A contract call for the CTO.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S3",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The upload review's disclosure sentence reads '<from> is analysed as <to>, a proxy you named.' for every served correction. For an accepted spelling suggestion the advisor named no proxy, so the sentence is false for that kind.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-S3",
   "the screenshot review_region_crop_1cd1cf25.png, read by this seat"
  ],
  "remedy": "The sentence states the kind it has (a correction you accepted, or a proxy you named), from a served kind field; or one wording true of both.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W46-S5",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The upload review's two dollar columns are left-aligned, where DESIGN.md C2 says figures right-align in a column. The numerals are tabular.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W46-S5",
   "portal/DESIGN.md C2 (:220-223); the screenshot review_region_crop_1cd1cf25.png"
  ],
  "remedy": "The two cells take the right-align class, in the next cell that touches the table.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W47-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "GET /performance/{accountSetId} is a read-through store: a miss computes and persists a report, and for the named client's firm the fresh path is the vendor branch, which spends a single-use vendor authorization if an approved plan is installed. A trace called read-only can write and can spend.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W47-S2",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/FWD1_TRACE_READONLY_PAIR.md"
  ],
  "remedy": "The FWD-1 pair names this branch in its blast radius and states what holds it (a warm store read first, or the vendor branch refused), in both halves, before either signs.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W47-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The ruled bound 'every request a GET but the sign-in' does not describe the page: POST /selections writes one immutable item and POST /directory/resolve only reads.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W47-S1",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/FWD1_TRACE_HOPS.json"
  ],
  "remedy": "The pair restates the bound as the request list it is (22 requests, 4 non-GET, each named), and the ruling's wording follows.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W47-S3",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The portal signs its page in by a refresh cookie, so a minted token cannot open the page; a signed-in browser also posts analytics events and prefetches five 49financial files for an internal-tier claim.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W47-S3",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/FWD1_TRACE_READONLY_PAIR.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND_12_L9_ANSWER_20261011.md"
  ],
  "remedy": "The pair's page step uses a real sign-in and lists those extra requests in its blast radius. FWD-1 is graded on that step (this seat's answer, org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND_12_L9_ANSWER_20261011.md).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v13"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S5",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The upload review's single wording for a correction is honest only while the served correction carries no kind. IRPT_YCDGEN FWD-20 will serve the kind.",
  "evidence": [
   "investigation rows DSGN_IRPTV1-D2-S5 and DSGN_IRPTV1-D2-S3"
  ],
  "remedy": "When FWD-20's cell serves the kind, the Holding cell and its disclosure line follow it. This closes with row D2-S3.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v13",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v13"
  },
  "closed": false
 }
]
```
