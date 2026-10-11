# DSGN_IRPTV1: remediations, rounds 14 to 16

<sweep_watermark>2026-10-11T10:08Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T10:08:26Z. Inputs: msgs 4490, 4551, 4666. Reads: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_14_15_L9_GRADE_20261011.md`.
Graduated, round label v17: 14 rows, OPEN, INERT. Still ARMED from earlier files: S7 and W21-S2 (2 of 10 retirements unruled).

**Four things for the CTO's analysis:**
1. **FWD-1 is NOT MET on the rendered walk** (rows D2-S7, D2-S11). Two hops hold it: Performance (the release was rolled back) and
   the reporting-read firm map, which holds one firm.
2. **Two tests on DEV are weaker than the ones they replaced** (row D2-W49-S9): pin the three excused routes by name.
3. **Five ids wait on IRPT_BCKEND's schemas** (row D2-W49-S7).
4. The suite reads 9 failing of 1,159 on DEV (the issuer's run), against 43 at the baseline.

```json
[
 {
  "id": "DSGN_IRPTV1-D2-S7",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "FWD-1's rendered walk on DEV breaks at the Performance hop: the reporting-read function's firm map holds one firm (49financial, measured live), so a Cottonwood client's year-to-date return and spread are refused FIRM_BINDING. The category split is one layer in (PARTIAL).",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-S7",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_14_15_L9_GRADE_20261011.md",
   "this seat's live read 2026-10-11T08:32:48Z: get-function-configuration irpt-49f-reporting-read-lambda, IRPT_DIRECTORY_BUCKET_MAP holds 1 key, 49financial -- the record's inferred live state, now measured",
   "org/tier1_exec/4.0.0_SA_CRO/deliverables/UI_WALK_DSGN_IRPTV1_FWD1_20261011T0730Z.md"
  ],
  "remedy": "IRPT_DASHBD builds FWD-11 for the reporting read (the CTO's read-only cell comes first, msg 4459). On the page: the Holdings face opens on the picked account's category split. Then FWD-1 is walked again, rendered.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W50-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Three failing ids come from the contract-ahead-of-portal drift and sit outside the repair cell's 18, so that cell's criterion will not see them.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W50-S1",
   "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~50/FAILING_ID_TABLE.json"
  ],
  "remedy": "The repair cell's list takes the three, or each gets its own owner in the table.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W49-S9",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two re-derived test equalities (fe-s-14 envelope, fe-s-57 carry) excuse any DECLARED route with no response schema, and the number excused is not pinned. A route that loses its schema no longer fails them.",
  "evidence": [
   "investigation rows DSGN_IRPTV1-D2-W49-S9 and DSGN_IRPTV1-D2-S10",
   "this seat's read of portal commits 3e654e4e and 8a14511d and of candidate 7e8fa4fd: fe-s-13/routes.test.ts and fe-s-14/header.test.ts now compare to routes.json _denominator.total; fe-s-14/envelope.test.ts:166-223 and fe-s-57/carry.test.ts:152-242 set declared = routes with a response schema, declaredNoSchema = DECLARED routes with none, and assert their sum equals the DECLARED count",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_14_15_L9_GRADE_20261011.md",
   "this seat's reads 2026-10-11T10:08:26Z: portal origin/DEV is 3bf0d731; on it fe-s-14/envelope.test.ts:221-223 and fe-s-57/carry.test.ts:239-241 still assert declared.length + declaredNoSchema.length equal to the DECLARED count, with the three excused routes named in a comment only; irpt-performance-adapter live CodeSha256 is 9kYLdR64..., LastModified 2026-10-11T10:03:25Z, no longer the release's OF+8j4uc... this seat read at 09:41Z"
  ],
  "remedy": "Assert the excused set by name (custody-report-read, custody-report-persist, analysis-request-original). The tests are on portal DEV unpinned (read at 3bf0d731).",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W49-S6",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The calendar fix on DEV (733986d7) broke fe-s-46's bounds test; its repair is in the contract catch-up candidate, which is not on DEV.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W49-S6",
   "msg 4551 (round 14 fully drained @b97b6ac14a)"
  ],
  "remedy": "The candidate lands, or the repair is cut out and landed alone. DEV reads red on that id until then.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W49-S7",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two v1 response schemas (comparison-catalogue, analysis-request-pdf) do not declare the envelope member unprojected_grant that the producer always sends and the portal's parser requires. Five ids stay red on it.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W49-S7",
   "msg 4551 (round 14 fully drained @b97b6ac14a)"
  ],
  "remedy": "IRPT_BCKEND's schemas declare the member. The CTO places it; it is the producer's contract.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W49-S8",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "One test needs the smoke map at 22 keys while two others pin the same file at 12; two of the ten missing routes have no producer fixture.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W49-S8",
   "msg 4551 (round 14 fully drained @b97b6ac14a)"
  ],
  "remedy": "One ruling on the smoke map's size, then the three tests agree.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W49-S5",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The one new dev dependency resolved a transitive package (happy-dom 20.14.6) published three days before the work, by a caret range.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W49-S5",
   "msg 4551 (round 14 fully drained @b97b6ac14a)"
  ],
  "remedy": "The lock pins the version the CTO approved, or the CTO accepts the newer one by name.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W49-S3",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A plain add of one dev dependency re-resolved five other packages and pruned 57 lock entries, because the committed lock was stale against one plugin family.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W49-S3",
   "msg 4551 (round 14 fully drained @b97b6ac14a)"
  ],
  "remedy": "The lock is refreshed once, on purpose, in its own commit, so the next add moves one package.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W49-S4",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A lock-faithful install lacks playwright-core, which the shared node_modules holds and neither package.json nor the lock declares. Two tests pass only on the shared tree.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W49-S4",
   "msg 4551 (round 14 fully drained @b97b6ac14a)"
  ],
  "remedy": "The package is declared, or the two tests state their skip path as the expected one.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W49-S1",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The regenerated portal calendar's provenance line depends on the box's python: without pandas_market_calendars it names a hardcoded fallback.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W49-S1",
   "msg 4551 (round 14 fully drained @b97b6ac14a)"
  ],
  "remedy": "The generator refuses to regenerate from the fallback, or records the fallback as a claim a reader can reject on.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S11",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The FWD-1 re-walk read the Performance hop PARTIAL on a release the CTO then ruled against the ratified ENDPOINT and rolled back. That hop is not evidence for FWD-1 and is unavailable again.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-S11",
   "msg 4666 (round 16 drained @3b1d197935; record deliverables/0.9.0_WK_DSGN_IRPTV1~52/REPAIRS.json)"
  ],
  "remedy": "FWD-1 is graded on a walk whose Performance hop is served by a release the ENDPOINT admits. The CTO's analysis names that release.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W52-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "adapt.ts site 1360 (facts.frozen_as_of ?? null) is STOPPED: the contract types the member string, optional, never null, but iv-e-162 ARM(a) CONTROL pins a receipt without it as null on the view, and that assertion is not retired.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W52-S2",
   "msg 4666 (round 16 drained @3b1d197935; record deliverables/0.9.0_WK_DSGN_IRPTV1~52/REPAIRS.json)"
  ],
  "remedy": "One ruling: the contract admits null for frozen_as_of, or the pinned assertion is retired. The CTO's ruling on portal 3bf0d731 records it as an exception in the scan; the coalesce itself is still there.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W52-S3",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "iv-e-116 ARM(b) locates the press branch by a regex anchored on LF line ends; this device checks GenerateComposer.tsx out CRLF (index LF), so the pin could not match here even when the literal was right.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W52-S3",
   "msg 4666 (round 16 drained @3b1d197935; record deliverables/0.9.0_WK_DSGN_IRPTV1~52/REPAIRS.json)"
  ],
  "remedy": "The pin's regex accepts either line ending, or the file's checkout is fixed by attribute.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S9",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The portal's published-map entry for the export-download answer borrows its four signed-link members from the producer's AnalysisRequestPdf.valid.json fixture, because no producer fixture exists for the download answer itself; it is to be replaced when IRPT_BCKEND publishes one.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-S9",
   "msg 4666 (round 16 drained @3b1d197935; record deliverables/0.9.0_WK_DSGN_IRPTV1~52/REPAIRS.json)"
  ],
  "remedy": "The export-download answer gets its own published schema entry.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v17"
  },
  "closed": false
 }
]
```
