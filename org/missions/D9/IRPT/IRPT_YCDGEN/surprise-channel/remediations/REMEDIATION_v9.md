# IRPT_YCDGEN: remediations, round 10 and the backlog

<sweep_watermark>2026-10-11T11:36Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T11:36:25Z. L8 input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)`.
Graduated, round label v11: 26 rows, OPEN. ARMED: 1 (D2-S45, the 8 dead letters). D2-S38 stays ARMED from an earlier file.
**22 of these rows are from rounds 6 to 9 and are graduated as filed.** Their present state was not re-read by this seat; an owner
who finds one already met closes it with the evidence.

**For the CTO's analysis:**
1. **FWD-1 is NOT MET and no run was made in round 10.** st30 is on the host and unexercised. A regenerated report waits on Andrew's
   word about a measuring identity (your msg 4669) or on his own sitting.
2. **A dead-lettered job still reads RECEIVED with no reason** (row D2-S49): 8 of 8. The redrive hazard (D2-S45) is ARMED.
3. **The published response schemas do not admit an Opal report** (rows W2-S13, W6-S4): they require a vendor-only member.
4. **The Opal path's research role exists for one firm** while the packaged policy row names three (row D2-S19).

```json
[
 {
  "id": "IRPT_YCDGEN-D2-S45",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The generation queue IS consumed today and reads 0 messages; 8 dead letters wait in irpt-generation-dlq, identity unknown: the hazard is a DLQ redrive, not a first binding",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S45",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The redrive of the 8 dead letters is decided on a read of what each is; no redrive before that read (the inventory read is with the laptop's executor).",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G2",
   "at": null
  }
 },
 {
  "id": "IRPT_YCDGEN-D2-S49",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A generation job can fail every delivery and be dead-lettered while its record still reads RECEIVED and holds no reason: 8 of 8 dead letters, none with a ticket_id",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S49",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "A dead-lettered job's record states its failure and its reason; the 8 existing ones are reconciled.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-S46",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The package gate fails a correct whole-tree build on the map member: it applies the recorded map source only in named-list mode; and two runs gave two tar hashes",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S46",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The package gate applies the recorded map source in whole-tree mode, and the two tar hashes are explained.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-S47",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "install_st30.sh carries an UNSUBSTITUTED placeholder VER=__ST30_SCRIPT_VERSION__: dead today because the fetch is by key, a hard failure the moment anyone restores the by-version fetch it is a leftover of",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S47",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The placeholder is removed or substituted in the install script.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-S9",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The held risk-free object (portal FRED Treasury yields) was last written 2026-08-05 and its last observation is 2026-08-04, so it is two months behind as well as two years short.",
  "evidence": [
   "investigation row IRPT_YCDGEN-S9",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The risk-free series is refreshed and its depth stated, or the sections that need it state the input missing.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W2-S12",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Contract R4 leaves the OPAL_ENGINE section's nullability, the inputs_as_of shape, the coverage type and the VALUE-branch reason open; the v2 schema fixes them one way that a consumer may need to confirm.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W2-S12",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The CTO confirms or changes the four choices the v2 schema made where contract R4 is silent.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W1-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "R2 states a closed reason set (COVERAGE_BELOW_0.95, STALE_INPUT, INPUT_MISSING:<name>, NOT_IN_THIS_VERSION); the module's existing paths still produce NOT_HELD:<reason>, SERIES_TOO_SHORT, OUTSIDE_TIME_BUDGET and others, and plain vendor-call elements carry no price marker.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W1-S4",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "Every reason the module can produce is a member of the closed set, or the set is widened by a rule-24 record.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W1-S8",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "layout_overview.py prints 'Not available from YCharts' data endpoints.' for builder-only elements, 'YCharts gave no answer' / 'outside the run's time budget' for vendor-call elements, and a 'Data: YCharts' footer on every page of the Opal report.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W1-S8",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The Opal layout prints no vendor wording and no vendor footer.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W1-S9",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The layout has no element list of its own for the three classified methods, the closed reason set excludes NOT_HELD:<r>, OUTSIDE_TIME_BUDGET and METHOD_UNKNOWN, and the v2 section value is number|string|null while the layout's table values are lists.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W1-S9",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The layout carries an element list for the three classified methods, and the v2 section value type matches what is written.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W1-S10",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "run.json inputs and the document's inputs_as_of carry the date the run read each input (as_of_basis READ_DATE), because the layout's held-row loaders return rows without the dated folder or the table's own date.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W1-S10",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "inputs_as_of carries each input's own date, or the READ_DATE basis is stated where a reader sees it.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W2-S13",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "OwnedAnalysisReader.sections now answers provider, request_ref, sections and computation_validation for an OPAL_ENGINE document, but the published response schema for the sections route requires extraction_validation and forbids any other member, so that answer is outside the published contract.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W2-S13",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The published sections response schema admits an OPAL_ENGINE report (computation_validation in place of extraction_validation).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W6-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "analysis-report.response.schema.json data requires request_ref, sections and extraction_validation; an OPAL_ENGINE report has no extraction_validation (it has computation_validation), so its sections slice does not validate against the response contract even though the sections pointer now accepts the OPAL section shape.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W6-S4",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The same contract change as W2-S13, on analysis-report.response.schema.json.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W3-S12",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Test_factory_returns_exactly_the_resident_shape_without_any_aws_call fails when test_resident_installed.py is run alone.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W3-S12",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The test passes when its file is run alone.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W3-S18",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "One test of a file under l-6's reports/tests/*.py fails identically before and after l-6: resident_worker.py:20 imports extract, which is not on that test's path.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W3-S18",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The test's import path is fixed, or the test has an owner.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W2-S14",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The Opal sections reach the Analysis tab only through the adapter's carried members; NativeSections and the typed contracts are outside the e-6 paths and still speak the v1 vendor wording.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W2-S14",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "NativeSections and the typed contracts speak the Opal form; placed with DSGN_IRPTV1 if it is a page change.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W4-S8",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The adapter does not set AnalysisReport.provider, so the tab tells the Opal form from its sections; an Opal report with an empty section list renders the v1 wording.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W4-S8",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The adapter sets the report's provider, so an Opal report with no sections does not render vendor wording.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W3-S13",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The Opal document is spilled to an artifact of the existing json family EXTRACTION_EVIDENCE, on every Opal checkpoint rather than only past the limit.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W3-S13",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The document is spilled only past the limit, or the every-checkpoint spill is stated as the design with its cost.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W3-S16",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "When the PDF is retained as an artifact, run.json's report.key (the layout's own key) names an S3 address nothing is written to; the retained location is artifact_ref.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W3-S16",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "run.json's report key names where the report is, or is absent when the report is retained as an artifact.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-S12",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "the Analysis tab lets an internal user submit with no firm selected; the intake function refuses it as BucketUnmapped, shown to the user as 'Needs attention' with no reason",
  "evidence": [
   "investigation row IRPT_YCDGEN-S12",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The Analysis tab does not submit with no firm selected, or the refusal reaches the user with its reason.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W2-S16",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "For a Global principal who picked a client, selectedScope.registryTenant and the global firm's tenant both hold the firm on the repo's served-wire fixture; the empty tenant comes from GenerateComposer reading and submitting with the bootstrap scopeRef, which carries none.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W2-S16",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The composer reads the firm from the selected scope for a Global principal who picked a client.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-S13",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "the picked-client Generate path sends a snapshot_id the browser builds from source_set_revision; the server needs the opaque cst_ id it minted, and no route returns it",
  "evidence": [
   "investigation row IRPT_YCDGEN-S13",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "A route returns the server-minted snapshot id, or the server accepts the id the browser can build.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-W3-S21",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "bun test src/pages/InvestorReporting leaves contracts/wire/{AnalysisReport,ExportBundle,index,responses}.ts modified (120 changed lines, 56 deleted from AnalysisReport.ts) in the portal worktree; the IVE17-AC2 regenerated-wire test is the likely writer.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W3-S21",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The portal test run leaves no tracked file modified.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-W7-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "build_brand_spec() output depends on the box: its logo.variants block is read from deck_generation/brand/logo_package (gitignored), which dell2 does not hold, so the packaged brand.json carries formats {} and preferred null for all 6 variants; the laptop would write relative paths.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-W7-S2",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The brand spec is built from tracked inputs, so the package is the same on every box.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-S4",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "No registered partner firm has a row E5 can resolve as FIRM_OPERATIONS (0 admin users at every firm), and cottonwood has no FIRM_ADVISOR-capable row either: an on-behalf upload for cottonwood is impossible on current data",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S4",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The CTO rules how an on-behalf upload is authorised for a firm with no operations row.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-S19",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "st28 F1 on 49financial: the Opal path cannot run for any firm but cottonwood -- the runner role may assume only irpt-cot-ycharts-research-role, and irpt-49f-ycharts-research-role does not exist",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S19",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The Opal path's research role exists for each firm the packaged policy row names, or the row names only the firms that have one.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v11"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-S25",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "updatedAt on an opal-users-v2 PROFILE row has a SECOND writer -- /auth/login stamps it -- so the served-read window's standing 'the before-updatedAt equals my own last write, therefore no third party touched this row' inference is not a sound no-third-party oracle; the tell is precision, 3-decimal ms from the login vs 6-decimal us from swap_svc_firm.py.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S25",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r10/ROUND10_DRAIN_END_READ_20261011.md @7219e6977e (msg 4827)"
  ],
  "remedy": "The served-read window stops inferring 'no third party touched the row' from updatedAt, which login also stamps.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v11",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v11"
  },
  "closed": false
 }
]
```
