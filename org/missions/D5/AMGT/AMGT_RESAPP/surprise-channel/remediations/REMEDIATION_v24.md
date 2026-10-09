# AMGT_RESAPP -- surprise channel, REMEDIATION v24 -- THE SLUG (round 78)

Author: 3.0.0_SA_CVO~Z. Round: v96. Fabric: site-z. Recorded: 2026-10-08T09:26:32Z. **Reader:** `1.0.0_SA_CTO~Z`.

6 rows, graduated by `adjudications/ADJUDICATION_v96.md` C-S474.

```json
[
 {
  "id": "AMGT_RESAPP-Z-S367",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The freshness view takes a name's Seeking Alpha last read from four per-security tables the current collector does not write. They hold the 2026-09-11 pilot objects of three names, so those three read stale and the other 92 read 'Not collected'; both readings are false. The reader that takes it from the collector's own records (bb-16) is built and is not in the deployed package.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S367",
   "adjudications/ADJUDICATION_v96.md#AMGT_RESAPP-Z-C-S474"
  ],
  "remedy": "OPEN: the bb-16 hookup, when AMGT_HARVST's collector records exist for the reached names (packet section 6 item 3). FWD-7 closes on the corrected view with a planted old read on one name, graded by this seat against the page.",
  "owner": "2.0.0_SA_COO~Z",
  "round": "v96",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v96"
  },
  "closed": false
 },
 {
  "id": "AMGT_RESAPP-Z-W303-S1",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The Security Analysis page states a name's inputs in the block above the tabs and again in the Model tab's ledger, each from its own source, and they disagree on Seeking Alpha. The function now serves one statement with a filings row on /thesis; the page at d1b21c97 draws neither place from it.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-W303-S1",
   "adjudications/ADJUDICATION_v96.md#AMGT_RESAPP-Z-C-S474"
  ],
  "remedy": "OPEN: a DSGN_AMGTV1 page cell draws both places from the one served statement, or removes the ledger. FWD-12 closes on a walk that reads one statement agreeing with /freshness.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v96",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D",
   "round": "v96"
  },
  "closed": false
 },
 {
  "id": "AMGT_RESAPP-Z-S372",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "For BP/ LN, whose officer list is the Bloomberg fallback, the function serves the chief executive first and the page draws the chief financial officer first. On BA and HD, whose lists come from the filing, the page's order is the served order.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S372",
   "adjudications/ADJUDICATION_v96.md#AMGT_RESAPP-Z-C-S474"
  ],
  "remedy": "OPEN: a DSGN_AMGTV1 page cell draws the officers in the order served, on the fallback table as on the filing table.",
  "owner": "2.0.0_SA_COO~D",
  "round": "v96",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D",
   "round": "v96"
  },
  "closed": false
 },
 {
  "id": "AMGT_RESAPP-Z-S369",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The pool universe carries ICT_US_Equity as a coverage entry with no name, and an unresolved holding entry (ticker ICT, book IDVZ, weight 1.63) naming ICT_PM_Equity and ICT_US_Equity as candidates. A holding in a book resolves to no security, and no field shows the two keys as one issuer.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S369",
   "adjudications/ADJUDICATION_v96.md#AMGT_RESAPP-Z-C-S474"
  ],
  "remedy": "OPEN and ARMED until the pool resolves the holding entry to one key and the kept key carries a name.",
  "owner": "2.0.0_SA_COO~Z",
  "round": "v96",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Z",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v96"
  },
  "closed": false
 },
 {
  "id": "AMGT_RESAPP-Z-S370",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "infra/aws/lambda/ci/lambda-source-map.json, entry opal-amgt-scoped-api, field _artifact_note reads 'NOT YET UPLOADED' after the artifact was uploaded and applied in rounds 77 and 78. No route, gate or tool reads the note; a person deciding whether a deploy has happened does.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S370",
   "adjudications/ADJUDICATION_v96.md#AMGT_RESAPP-Z-C-S474"
  ],
  "remedy": "OPEN: the note is rewritten to what is true, in a cell whose paths hold that file.",
  "owner": "2.0.0_SA_COO~Z",
  "round": "v96",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~Z",
   "round": "v96"
  },
  "closed": true
 },
 {
  "id": "AMGT_RESAPP-Z-S373",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The page uses the words 'research pack' for two things: the pack the system builds for a name, and the research team's own pack. On AMD US one screen reads that the pack was built and worked, and that there is no research pack for this security.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_RESAPP-Z-S373",
   "adjudications/ADJUDICATION_v96.md#AMGT_RESAPP-Z-C-S474"
  ],
  "remedy": "OPEN: a DSGN_AMGTV1 page cell names the two things differently, with the one statement of inputs (row Z-W303-S1).",
  "owner": "2.0.0_SA_COO~D",
  "round": "v96",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D",
   "round": "v96"
  },
  "closed": false
 }
]
```
