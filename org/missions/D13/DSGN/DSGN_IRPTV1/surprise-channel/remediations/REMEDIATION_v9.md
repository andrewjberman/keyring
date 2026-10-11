# DSGN_IRPTV1: remediations, rounds 17 to 22

<sweep_watermark>2026-10-11T16:41Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T16:41:38Z. Inputs: msgs 4903, 5015, 5262, 5345, 5351. Reads:
`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_17_19_L9_READ_20261011.md`.
Graduated, round label v23: 12 rows, OPEN, INERT.

**For the CTO's analysis:**
1. **FWD-1 has no rendered walk on anything built in rounds 17 to 22.** The Holdings face, the Opal wording on the page and in print,
   and the report opener after a Prospect Generate are each on portal DEV and each read on synthetic data only.
2. **The Holdings face shows two totals with no label, and a securities table that does not add up to its card** (row D2-S14).
   The 130 percent weight was the driver's, not the page's. The missing share is a sleeve with no security beneath it, which the
   table omits without saying so (row D2-S18); whether a served answer can carry one is not established.
3. **The transitional history reader is on DEV, not PROD.** Its PROD push changes a client-facing page and waits on Andrew's word;
   the PROD portal also lacks two of the seven irpt-status reads (row D2-W56-S2).
4. **The Opal wording depends on the provider reaching the view.** A report with no provider prints the vendor words.

```json
[
 {
  "id": "DSGN_IRPTV1-D2-S14",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The Holdings face, opened on a picked account, shows two totals with no label between them (the Identity band's household figure over 2 accounts, and Total Assets for one account at half of it), names the picked account nowhere, and lists securities that sum to 80 percent of the total with no row and no sentence for the SMA 20 percent. Seen on one driver screenshot of a synthetic fixture; the 130 percent weight of row D2-W53-S7 is the same family.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-S14",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The Holdings face names the picked account and its base, and the securities table states what it leaves out. Checked on the rendered walk. Row D2-S18 explains the missing share on the fixture.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S18",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-103 follow-up (CTO msg 5359): the Holdings securities table's two rows sum to 750,000 against a total card of 1,000,000 because the synthetic fixture's two SMA SLEEVE nodes (150,000 and 100,000) are leaves with no SECURITY node beneath them, and the table lists SECURITY nodes only; the card and the table read the SAME total.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-S18",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The page states the amount a table leaves unlisted, or the producer always sends a sleeve's securities. First: whether a served answer can carry a sleeve with no security beneath it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-S16",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-101 (an Opal report opened on the page prints no vendor wording; portal 58e15f4c on DEV) is UNEXERCISED on a served Opal report: its evidence is a screenshot of synthetic data produced by a driver script, and a static-markup test.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-S16",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The first served Opal report opened on the page is read for the Opal wording.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W58-S4",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-105 is UNEXERCISED on a served Opal report and on a real export: the document was rendered from synthetic fixtures through the print route of a build, not from a backend-produced export.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W58-S4",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The Opal print and export are read on a backend-produced export.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W57-S3",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The fix mounts OwnedRequestHistory after an accepted Prospect Generate and reads it with selected_tenant = the tenant the submission used (the card's firm for an internal viewer); the page itself is reachable only by an Opal-internal admin Dev user",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W57-S3",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The report opener after a Prospect Generate is read on the rendered page by the identity that can reach it.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W56-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-100: the portal reads 7 of the 7 irpt-status routes at DEV but only 5 at PROD -- the PROD client has no method and no route-table row for analysis-request-pdf or -original, and PROD's parser has no adapter for -original",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W56-S2",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "A PROD push that carries the two missing reads, or a statement that PROD does not offer them, before irpt-status is re-released.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W56-S3",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-100: on the v1 plane the sections reader drops retained_ref (no member on AnalysisReportSliceView), and getAnalysisReport is typed AnalysisReport while the parser returns the slice view -- its adapter argument is unread",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W56-S3",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The sections reader carries retained_ref on the v1 plane, before the release that serves it.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W53-S5",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-96: the account picker the walks used is the Performance tab's own, whose choice was tab-local and unseen by Holdings; the header's picker hands the tabs no account",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W53-S5",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The header's picker hands the tabs the picked account, so Holdings and Performance read one choice.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W53-S6",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-96: scripts/ui-smoke.mjs cannot pick a client, so the order's named screenshot instrument stops before any client or account is chosen; screenshots came from a supplementary driver",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W53-S6",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "scripts/ui-smoke.mjs can pick a client, so the named screenshot instrument reaches an account.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W58-S3",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two things on the Opal document are not vendor WORDS and are left as they are: the Source column prints the wire page number of each value (2, 3, or not stated), and report-level disclosure text prints as the producer supplied it.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W58-S3",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The Opal document's Source column and disclosure text are ruled: kept as supplied, or worded for Opal.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W53-S8",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "IV-e-95 part 2: running fe-s-13/gen-corpus.ts (the one documented way to regenerate default.json) rewrote fixtures/wire/requests/comparison-catalogue.request.json without its `_captured` member; the worker restored the file from git and committed only the generator and default.json",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W53-S8",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The smoke-map generator leaves the tracked request fixture alone.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 },
 {
  "id": "DSGN_IRPTV1-D2-W53-S2",
  "project": "DSGN_IRPTV1",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "iv-e-69.performance-finished.test.tsx carries one raw NUL byte (offset 16025, in the fallback of formatPageDate(...) ?? '<NUL>'), so ripgrep and Grep report the file as binary and skip it.",
  "evidence": [
   "investigation row DSGN_IRPTV1-D2-W53-S2",
   "msgs 5345 and 5351 (IV-e-104 drained @9cc17c490e, portal DEV c3a03c24; IV-e-103 drained @5a150bf718; round 22 MAY-CLOSE)"
  ],
  "remedy": "The raw NUL byte is removed from the test file, so search tools read it.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v23",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v23"
  },
  "closed": false
 }
]
```
