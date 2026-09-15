# IRPT_FNTEND -- BACKFILL of rounds 4-5 remediation rows: graduated rows that received none

Author: 3.0.0_SA_CVO. Recorded: 2026-09-15T03:09:28Z. Fabric: laptop.

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's.

WHY THIS FILE EXISTS: the spine's L9 (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:415-416`) gives every graduated row a remediation row at L10. This seat's census (`org/tier1_exec/3.0.0_SA_CVO/deliverables/GRADUATED_WITHOUT_REMEDIATION_ROW_CENSUS_20260915.md@f0c0f06c9f`) found 42 IRPT_FNTEND ids graduated by carriers C-S56..C-S84 with none: this project produced no remediation file for rounds 2 to 5. This is decision (b) of that record, taken by 3.0.0_SA_CVO in its own lane on Andrew's /open-calls (~02:5xZ 2026-09-15): backfill projects still EXECUTING, one at a time, as the gate admits them; pre-issuance intake graduations excluded (none here: every carrier post-dates the first order @3ceb5201cb, 2026-09-10T21:15:04Z).

ROUNDS: `round` is the round whose L9 wrote the carrier, read from each carrier's `surfaced_at` against the round issuances and confirmed by this seat's round records -- v4 for C-S56, C-S57, C-S58 (round-4 L9, IRPT_FNTEND_ROUND4_L8_L9_20260913.md) and C-S65, C-S67, C-S68, C-S71, C-S72 (the round-4 BACKLOG pass, rows first surfaced in rounds 2-3, carried 2026-09-13T09:4x-09:5xZ before round 5's issuance); v5 for C-S81..C-S84 (IRPT_FNTEND_ROUND5_L8_L9_20260914.md). Split: {"v4": 24, "v5": 18}.

STATES: every row is OPEN except four whose remedy a later row records as executed -- S27 (C-S79), S53, W4-S7 and S56 (C-S85) -- which read REMEDIATED with that citation. Of the 17 ARMED rows, 6 read DISARMED (each citing the row that records the disarm) and 11 read ARMED with `at` null: no row records their disarm, and a carrier's disarm CONDITION is not a disarm.

FLAGS: 14 rows carry a remedy the carrier does not state in so many words; each is written `per carrier <id>:` with the carrier's own text.

```json
[
 {
  "id": "IRPT_FNTEND-S27",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "READ OFF-TASK FROM F16-AC8's OWN CAPTURE, by opening the PNG rather than reading the console line the criterion grades on: the served print document contradicts itself about how many accounts are in scope. The page header reads '0 account(s) in scope' on ALL FOUR pages, while page 3 lists account A-0001 under 'Accounts in this report' (Covered true, period return 0.0688) and states 'None. Every account in the requested scope is represented above.', and page 4's METHODS AND SOURCES prints 'Bundle scope: tenant F-49F, fingerprint fp-49f-0824, firm not stated, client not stated, relationship not stated, accounts A-0001'. Those cannot all be true at once. IMPORTANTLY THIS ALSO FALSIFIES THE RECORDED CAUSE IN ROW IRPT_FNTEND-W2-S13, which attributed the zero to 'a client-composed bundle names no account set' -- this document's own bundle scope DOES name an account set, and the header still reads 0. The count is reading something other than the accounts the bundle carries. F16-AC8 PASSES correctly and is not affected: its bar is the resolver line and the resolver did resolve.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@4092306878#IRPT_FNTEND-S27",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@df08e2c33c row IRPT_FNTEND-C-S68",
   "Instrument: this seat READ the image at /c/tmp/wk-irpt_fntend-2-6-fe-s-16/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/fe-s-16_print_narrative_1440.png (sha256 8094204b4eb99c77108b270dc530cdf2079a3f018d75ab214a2d0cbb696e100f, 324527 bytes). A DIFFERENT INSTRUMENT from the one the criterion uses: F16-AC8 greps a console line, and no console line can see a contradiction between two rendered regions.",
   "Header band, top right of every page, 4 of 4: 'Prepared for the selected scope / rev-49f-000091 / 0 account(s) in scope'.",
   "REMEDY EXECUTED, as recorded by IRPT_FNTEND-C-S79",
   "DISARM RECORDED BY IRPT_FNTEND-C-S79 (W1-S61: the frozen print renders '2 account(s) in scope' over A-0001/A-0002 -- 'C-S68's disarm observed holding'); earlier IRPT_FNTEND-C-S45 notes 'DISARM DISCHARGED' on the judgment"
  ],
  "remedy": "The wire carries the scope's account set on this route, or the header renders UNAVAILABLE with its reason; 2.0.0_SA_COO~F cuts the cell (C-S68).",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "3.0.0_SA_CVO",
   "at": "2026-09-14T11:26:58Z"
  }
 },
 {
  "id": "IRPT_FNTEND-S42",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "TWO FINDINGS FROM FE-s-19 THAT EXPLAIN ROUND 2's BLINDNESS AT THE INSTRUMENT LEVEL, and one that blocks F18-AC3 permanently until a fixture cell is cut. (a) THE PORTAL INSTALLS NO DOM TEST ENVIRONMENT, so under `renderToStaticMarkup` React runs no effect and A MOUNTED BODY AND A SEEDED BODY ARE LITERALLY INDISTINGUISHABLE -- which is not a metaphor for how 420 tests passed over the defect, it is the mechanism. FE-s-19's AC4/AC5 are browser criteria of necessity, and `chromium.launch` UNDER BUN fails on this box (network-service crash, rc=124 at 180s) while the identical launch under NODE returns in seconds. (b) 81 of 84 v1 envelopes in the smoke corpus carry no `status`, so no capture set built on them can discriminate a state.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@b0dbbb7a45#IRPT_FNTEND-S42",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@df08e2c33c row IRPT_FNTEND-C-S67",
   "Worker's comp-find census for a DOM test environment: 2 hits across 741 files, BOTH of them comments saying the portal has none; `bun install` is forbidden by every face, so installing one is not a worker act.",
   "Worker's measured instrument split: chromium.launch under bun -> network-service crash, rc=124 at the 180s bound; the identical launch under node -> returns in seconds. Its browser-driver.mjs therefore runs under node, spawned by the bun test -- a two-runtime arrangement nothing in the cut anticipated.",
   "DISARM RECORDED BY IRPT_FNTEND-S57 (1.0.0_SA_CTO: 'DISARM of eleven ARMED rows by their named disarm_owner ... S42'); IRPT_FNTEND-C-S85 reads C-S67's second branch met in substance; IRPT_FNTEND-C-S76 records that 3.0.0_SA_CVO and 1.0.0_SA_CTO differ on S42"
  ],
  "remedy": "The portal suite can observe a mount, or the cut-time refusal of seeded criteria becomes a gate limb (C-S67). C-S85 reads the second branch met in substance at the complete flip (drives_check), not at the cut, and the portal still installs no DOM environment.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-13T09:45:57Z"
  }
 },
 {
  "id": "IRPT_FNTEND-S53",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "W4-S7 UNDER-STATES ITS OWN FINDING. The <placeholders> reader FE-s-28 made MANDATORY at L6 is not merely 'looser than it reads' -- it is a FALSE-ADMIT on two of its three refusal branches, measured by calling the SHIPPED `_placeholder_declaration_violations` on REAL task-order bytes. (C) an invocation token the real element does NOT declare is admitted whenever the criteria sit between a prose mention and the element -- the standard face layout -- because the token lands inside the captured span and declares itself, so the 'omits a token' branch cannot fire. (D) an order with NO element is admitted if its prose quotes the gate's OWN help text, which contains a complete inline <placeholders>WS, PORT</placeholders>. A LINE-ANCHORED reader closes both, and still admits both orders that declare.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d0c88470dc#IRPT_FNTEND-S53",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@be3b6849a9 row IRPT_FNTEND-C-S56",
   "INSTRUMENT: the gate's own function, imported from C:/tmp/wk-irpt_fntend-4-4-fe-s-28/.tools/to-pipeline-gate.py and called directly -- not a re-derivation of its rule. Inputs are REAL: FE-s-28's and FE-s-27's order files as they stand, FE-s-23's (the order that invented the element), and `tpg.PLACEHOLDERS_HOWTO`, the text the gate itself emits on refusal.",
   "SHIPPED reader `<placeholders>(.*?)</placeholders>` with re.S, first match via .search(): A FE-s-28 as issued -> ADMITTED (first-match span = 368 names for a 1-token declaration); B FE-s-27 with no element -> REFUSED; C FE-s-28 + an invocation using <PORT>, element declaring WS only -> ADMITTED; D FE-s-27 + a prose paragraph quoting PLACEHOLDERS_HOWTO, still no element -> ADMITTED.",
   "REMEDY EXECUTED, as recorded by IRPT_FNTEND-C-S85",
   "DISARM RECORDED BY IRPT_FNTEND-C-S85 ('C-S56's two named conditions are met': 9e6ed6c236 line-anchors PLACEHOLDERS_TAG_RE in both readers in one change)"
  ],
  "remedy": "Line-anchor PLACEHOLDERS_TAG_RE in BOTH readers (proof-of-spec-check.py and to-pipeline-gate.py) in one change -- C-S56's disarm condition; 2.0.0_SA_COO~F holds W4-S7's issuance side.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-14T11:26:58Z"
  }
 },
 {
  "id": "IRPT_FNTEND-S55",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "ROUND 4's L6 CUT DEFECT, COUNTED: 3 of 4 orders carried a criterion the issuer cut against an ASSUMPTION rather than the code, and all 3 were caught by WORKERS REFUSING, 0 by any issuance gate. F28-AC6 expected `0 fail` from a battery that never prints it; F26-AC8 required FE-s-22's suite green while F26-AC5 required repairing the live fixtures FE-s-22's assertions read as defective; F25-AC6 required 9 of 9 producer states distinguishable at the view while the only display surface lay outside the grant. Three shapes, one cause: a bar is a claim about a tool's OUTPUT or a surface's REACH, and each was cut without reading it.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@2e00b2eabb#IRPT_FNTEND-S55",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@be3b6849a9 row IRPT_FNTEND-C-S58",
   "F28-AC6 (OUTPUT VOCABULARY): expect `0 fail`; test_proof_of_spec_alignment.py:457-462 prints only `BATTERY FAILED` or `BATTERY PASS`; measured rc=0 with '0 fail' occurring 0 times. Re-cut @9ab6043728; FE-s-28 then completed @c0eb49d1e1. The SAME shape was caught by the issuer on F28-AC1 BEFORE issuance and corrected as an instance, not generalised to the order's other instruments.",
   "F26-AC8 (ANOTHER CELL'S ASSERTIONS): F26-AC8 required __tests__/fe-s-22 green; __tests__/fe-s-22/capture-hash.test.ts:252 `expect(verdict.defectiveFixtures).toHaveLength(3)` and :282 `expect(exact).toEqual([])` read the LIVE maps F26-AC5 ordered repaired. Contradictory as cut. Grant widened @bf95fb7b9a."
  ],
  "remedy": "A cut-time check that catches at least one of S55's three shapes before issuance, rather than a worker after spawning; S55 names the OUTPUT-VOCABULARY limb as mechanisable (C-S58).",
  "owner": "2.0.0_SA_COO~F",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-S56",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "EVERY `0 fail` BAR IS GRADED BY AN UNANCHORED MULTILINE SEARCH -- confirmed LATENT by 1.0.0_SA_CTO on a different instrument, 0 false PASS across 648 proof instances estate-wide. Shapes: (a) `0 fail` matches inside ` 10 fail`; (b) any `0 fail` anywhere in a multi-run evidence blob satisfies the bar -- F18-AC17 is on record FAIL while its own evidence MATCHES its bar; (c, the CTO's) an unanchored bound matches a PREFIX of a longer number. ⛔ AND THIS SEAT'S INTERIM FIX WAS WRONG: `\\b0 fail` FALSE-FAILS coloured output, because an ANSI code puts `m` -- a word character -- directly before the count. The left anchor on a count is `(?<![0-9])`, the right `(?![0-9])`; no anchor closes (b).",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@0d5353792c#IRPT_FNTEND-S56",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@be3b6849a9 row IRPT_FNTEND-C-S56",
   "THE GRADER, read at the source: proof-of-spec-check.py:104-116 -- `matched = _re_x.search(exp, row.get(\"output_evidence\", \"\") or \"\", _re_x.S | _re_x.M) is not None`; a violation is raised only when `matched is False and status == \"PASS\"`. An unanchored search over free text decides every mechanical criterion. Confirmed independently by 1.0.0_SA_CTO (96370).",
   "SHAPE (a), tested by this seat: re.search('0 fail', s) is True for ' 10 fail', ' 20 fail', ' 110 fail' and a suite tail ending ' 10 fail'. SHAPE (b), on record: F18-AC17 status=FAIL, output_evidence carries ' 1 fail' AND a second '0 fail'; its expect MATCHES -- it is FAIL only because its worker wrote FAIL. SHAPE (c), 1.0.0_SA_CTO: `items (?:[1-5])` passes `items 15` against an upper bound of 5; AMGT_RESAPP TO-AMGT-r-4 AC1 matched the `1` of `15`, correct only because it was a lower bound.",
   "REMEDY EXECUTED, as recorded by IRPT_FNTEND-C-S85",
   "DISARM RECORDED BY IRPT_FNTEND-C-S85 ('C-S56's two named conditions are met': limb 2 count_bar_check refuses a PASS beside a contradicting summary)"
  ],
  "remedy": "The count bar refuses a PASS beside a contradicting summary -- C-S56's disarm condition.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO",
   "at": "2026-09-14T11:26:58Z"
  }
 },
 {
  "id": "IRPT_FNTEND-W1-S17",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Five places where the producer's contract and the consumer's view type do not map 1:1 -- three closed vocabularies lose a value on the way in, one view field could only be filled from a SERVER-ONLY storage key (so it is filled with null), and the producer's benchmark fact is an unstructured object the view's BenchmarkFact cannot be built from. Each is carried as an explicit unknown and named in FIELD_MAP; none is guessed.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@150e25a5b9#IRPT_FNTEND-W1-S17",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "PIN AUTHORITY, checked first: docs/contracts/investor-reporting/v1/ does NOT exist in this worktree (ls docs/contracts -> No such file or directory at 6ecffd5b15), so per this order's BOUNDS the two RAW pins are the authority -- routes.json @bef9b459f3 and _contracts/ @33351469c2 -- and WIRE_SCHEMA_PINS carries the sha256 of each of the eleven schema FILES as read from infra/ (producer-fixtures.test.ts re-digests them and compares, printing WIRE SCHEMA PINS FRESH: 11 of 11).",
   "(a) DirectoryEntry.access.entitled: the wire enum is GRANTED|DENIED|UNKNOWN (DirectoryEntry.schema.json properties.access.properties.entitled), the view's AccessFacts.entitled is a BOOLEAN (contracts/index.ts:211). UNKNOWN cannot be represented; it adapts to the NON-ASSERTING false. The producer's own account-only fixture instance (instance_account_only) carries exactly entitled: UNKNOWN, so the case is real and not hypothetical."
  ],
  "remedy": "v1 carries the five fields FIELD_MAP still maps as WIRE_ABSENT (contracts/adapt.ts:1341-1356) -- a v1 contract ruling at L10 (C-S71).",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S19",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TWO of the composer's eight rows name a wire prefill source v1 does not carry: the COMPARISON CATALOGUE (cell item 4, \"the catalogue the wire scope carries\") and the PREPARED-FOR / PREPARED-BY / CONTACTS profile (item 6, \"prefilled from the profile fields the wire scope carries\"). ResolvedScope v1 carries neither, and no other v1 document does.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@b572eb8759#IRPT_FNTEND-W1-S19",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "docs/contracts/investor-reporting/v1/ResolvedScope.schema.json @d9c940244a -- the generated wire type (portal contracts/wire/ResolvedScope.ts, source sha256 fc5504b5768f...) carries exactly: viewer_policy, principal_class, entitlement_revision, permitted_firm_catalogue, verified_request_firm_id, permitted_account_set, permitted_account_set_fingerprint, requested_scope, resolved_scope, partial_reason, vendor_ids, contract_version. No comparison catalogue; no profile.",
   "The other ten v1 document schemas were read for the same two: AnalysisRequest carries comparisons as SUBMITTED (position + security_identifier) and no catalogue of selectable ones, and no v1 document carries a prepared-for firm, a preparer, an organization, an email, a phone or a URL."
  ],
  "remedy": "The wire scope carries the profile and comparison catalogue the composer renders as absent (GenerateComposer.tsx:311-312) -- a v1 contract ruling at L10 (C-S71).",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S20",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The cell requires `report_title` to send `null` when the advisor states no override, but the granted adapter's `toAnalysisGenerateWire` types it `report_title: string` -- and the adapter is READ ONLY beyond this order's R2 re-pin, so the composer builds its own seven-key body and asserts key-set equality against the adapter's ANALYSIS_GENERATE_KEYS instead.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@b572eb8759#IRPT_FNTEND-W1-S20",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "portal src/pages/InvestorReporting/contracts/adapt.ts: `AnalysisGenerateRequestWire.report_title: string` and `AnalysisGenerateInput.reportTitle: string` -- under the portal's strict tsconfig neither admits null.",
   "UI_CONTRACT.md @72acd16e66 'Browser request' block sends `\"report_title\": null` verbatim, and the cell text says \"the request sends `null` when not overridden\"."
  ],
  "remedy": "One builder of the analysis body: contracts/adapt.ts:1097 types report_title as string while tabs/analysis/composer.ts:106 sends string | null -- C-S71's 'one-character type', cheap and consumer-side.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S22",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The seam's request corpus binds `snapshot_id` to the SCOPE FINGERPRINT (`HoldingsSnapshot.scope.resolved_scope_fingerprint`) while the composer sends the SNAPSHOT's own id (`source_set_revision`) -- two different facts under one key, and the counterpart replays the corpus into its real handler.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@b572eb8759#IRPT_FNTEND-W1-S22",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "portal src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts, ANALYSIS_BODY: `snapshotId: holdings.scope.resolved_scope_fingerprint` -- the value is `3333...3333`, the scope's fingerprint, which identifies the ACCOUNT SET and not the snapshot.",
   "portal tabs/analysis/composer.ts + __tests__/fe-s-15/composer.test.ts: the composer sends `smartx:sx-2026-09-09`, the adapted `sourceSetRevision` (HoldingsSnapshot.source_set_revision, source+revision per source), printed as `SNAPSHOT: body smartx:sx-2026-09-09 | held smartx:sx-2026-09-09`."
  ],
  "remedy": "per carrier C-S71: INERT BACKLOG, GRADUATED to 1.0.0_SA_CTO at L10: nine places where the v1 wire and the consumer do not meet -- none armed, each honest on screen, and each still a contract question no round has ruled. C-S71 did not re-read the corpus's snapshot_id binding at round 4; it states it as the row recorded it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S35",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "One named layout repair -- `the pie labels clip` -- cannot be made under LAYOUT ONLY: the clipping comes from recharts' `outerRadius={100}` and a label callback rendering `name: value` outside the arc, and BOUNDS excludes a prop change by name. Left undone, not worked around. The other five named repairs were made with class attributes and wrappers alone.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@899b41d773#IRPT_FNTEND-W1-S35",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S72",
   "portal wk-irpt_fntend-2-7-fe-s-18, src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx: the donut sits in `style={{ width: '100%', height: 280 }}` inside `grid gap-4 sm:grid-cols-2`, with `outerRadius={100}` and `label={(labelProps) => `${labelProps.name}: ${labelProps.value}`}`. At 390 the card's content box is about 300px wide; a 200px-diameter pie plus an outside label on each side needs roughly 360px. The geometry, not the container, is what does not fit.",
   "NO CLASS-ONLY LEVER REACHES IT, checked rather than assumed: `overflow-x-auto` on the wrapper does nothing because ResponsiveContainer SIZES ITSELF TO THE PARENT, so the SVG viewport shrinks with the container and the labels are clipped inside the SVG rather than overflowing a scrollable box. Reducing the card's padding (which was done -- `p-6` to `p-4 sm:p-6` on HoldingsSummary) buys 16px against a ~60px shortfall."
  ],
  "remedy": "The pie-label clip belongs with RULING I's Holdings cell, whose real render is the first capture able to show it (C-S72 notes).",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S39",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "W2-S11 is only PARTLY closed by this cell, and the remainder is refused rather than silently carried. F19-AC6's three bodies each carry TWO of the three envelope identifiers, so `isEnvelopeShaped` already admitted all three to the parser and all three were already refused -- what this cell added is the NAMED public reason and the refusal-as-a-state. The row's actual hole, a body carrying NONE of the three, is still ACCEPTED on `LiveClient`'s pre-envelope plane, because closing it reds at least three tests in TWO suites outside this order's write grant and would take F19-AC8 further from `0 fail`, not closer.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@c93dd9ab63#IRPT_FNTEND-W1-S39",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@df08e2c33c row IRPT_FNTEND-C-S65",
   "portal/src/pages/InvestorReporting/contracts/envelope.ts@f0443ba8:138-141, `isEnvelopeShaped`: 'return 'contract_version' in body || 'operation' in body || 'firm_id' in body'. A body missing exactly ONE identifier still carries the other two, so it is envelope-SHAPED and reaches `parseIrEnvelope`, which refuses it at :154/:155/:157. The three bodies F19-AC6 names were therefore never on the bypass.",
   "MEASURED at the pre-fix bytes: the criterion's own test could not even load -- `SyntaxError: Export named 'envelopeFromRefusal' not found in module .../state/status.ts` (.scratch/red3.txt). Post-fix it prints `MISSING contract_version -> rejected=true reason=ENVELOPE_CONTRACT_VERSION state=UNAVAILABLE`, and the same for `operation` and `firm_id`, with the control `a whole v1 envelope on the same path -> ACCEPTED (availability.state=READY)`. So what changed is the REASON and the STATE, exactly as AC6 words it, and not the bypass."
  ],
  "remedy": "A body carrying no envelope identity is refused with a named reason, or 1.0.0_SA_CTO rules at L10 that the contract names its adapted path as intended (C-S65).",
  "owner": "2.0.0_SA_COO~F",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W1-S46",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "THE CELL SAYS 'THE PANELS THAT CONSUME IT' AND THE GRANT REACHES ONE OF THREE. `formatSourceAge` has three consumers; two of them -- tabs/analysis/StageDisplay.tsx and tabs/analysis/VariantSelector.tsx -- are outside this order's <paths>, so the Analysis tab still renders 'Source time unknown' on exactly the no-answer states this cell exists to stop reporting as defects. I did not edit them and I did not widen the order.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@235682677d#IRPT_FNTEND-W1-S46",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@df08e2c33c row IRPT_FNTEND-C-S65",
   "THE DENOMINATOR, by census rather than recall: `comp-find 'formatSourceAge|Source time unknown' --path portal/src --all` -> 9 hits across 750 files scanned, bands DEF=1 SURFACED=8. Consumers = StatusPanel.tsx:16,34; analysis/StageDisplay.tsx:11,51; analysis/VariantSelector.tsx:20,61. Three files, and the census is over the whole of portal/src rather than the page directory, so it cannot have missed a consumer by being scoped to where I expected one.",
   "THE GRANT: this order's <paths> names portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx and portal/src/pages/InvestorReporting/tabs/reporting/ -- tabs/analysis/ is in neither. 1 of the 3 consumers is writable by this order."
  ],
  "remedy": "Both Analysis panels (tabs/analysis/StageDisplay.tsx:51, VariantSelector.tsx:61) age business_date, in a cell granted tabs/analysis/ (C-S65).",
  "owner": "2.0.0_SA_COO~F",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W1-S51",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "F18-AC4 passes its bar while the SCREEN third of the frozen pair shows StatusPanel 'Uncertain': fe-s-18-frozen.json carries a status member on 0 of its 9 envelopes (FE-s-26 gave one to the three Holdings maps only)",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@887b183a2a#IRPT_FNTEND-W1-S51",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@be3b6849a9 row IRPT_FNTEND-C-S57",
   "MEASURED (python json read) portal src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json @4ee0d105: 9 envelopes, a top-level `status` key on 0 of 9. fe-s-18-holdings-observed.json @4ee0d105: `status` on the holdings envelope only (state READY), inserted by portal ed90ce2d.",
   "CAPTURE, F18-AC4 run exactly as written, ui-smoke.mjs --port 5186 --width 390, dev server UP: 'CLICKED: Reporting', 'FIXTURES: 9 declared; 3 matched >=1 URL', rc=0."
  ],
  "remedy": "1.0.0_SA_CTO rules (i) whether an UNCERTAIN report may be exported that the screen withholds; 2.0.0_SA_COO~F cuts the fixture remediation, a status on the frozen map (C-S57). C-S79 reads the frozen map's status as supplied by FE-s-33 (row W1-S61); ruling (i) is not recorded.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W1-S52",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The Holdings body now mounts, but its donut and slice table are EMPTY at 390 AND at 1440: this order's generator emits all three nodes with parent_node_id null and level 0, so no node has children -- the pie and table clipping the face names remains unverifiable by capture",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@887b183a2a#IRPT_FNTEND-W1-S52",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@be3b6849a9 row IRPT_FNTEND-C-S57",
   "CAPTURE, F18-AC9 run exactly as written, --port 5186 --width 390: 'CLICKED: Holdings', 'FIXTURES: 9 declared; 3 matched >=1 URL', rc=0; the PNG shows the empty donut area and a header-only table.",
   "PROBE at 1440, same map, same server: ui-smoke.mjs ... --width 1440 --fixtures fe-s-18-holdings-observed.json --click Holdings, rc=0, 'CLICKED: Holdings' -- donut area empty, table header only. Width-independent."
  ],
  "remedy": "2.0.0_SA_COO~F cuts the fixture remediation: a parented Holdings tree (C-S57).",
  "owner": "2.0.0_SA_COO~F",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W1-S53",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "F18-AC14 'Global with two firms at 1440' renders the Holdings body as Failed / IR-REQUEST-FAILED and shows no second firm: fe-s-14-global.json declares 2 keys, directory/resolve and performance, and no holdings key",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@887b183a2a#IRPT_FNTEND-W1-S53",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@be3b6849a9 row IRPT_FNTEND-C-S57",
   "CAPTURE, F18-AC14 run exactly as written, --port 5186 --width 1440: 'CLICKED: Holdings', 'FIXTURES: 2 declared; 2 matched >=1 URL', rc=0; fe-s-18_global_two_firms_1440.png sha256 ead397909d7b32a86bc297d18e95f12d8be0457cfcfd2930b327ce54158e3334.",
   "MEASURED (python json read) portal src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json @4ee0d105: 2 keys -- /api/scoped/investor-reporting/directory/resolve and /api/scoped/investor-reporting/performance/."
  ],
  "remedy": "2.0.0_SA_COO~F cuts the fixture remediation: a holdings key on the Global map (C-S57).",
  "owner": "2.0.0_SA_COO~F",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S11",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The v1 envelope parser is STRICT, but LiveClient still ACCEPTS a body carrying none of `contract_version` / `operation` / `firm_id` -- a PRE-ENVELOPE document -- instead of refusing it, because `__tests__/fe-s-1/adapter.test.ts:213` (outside this grant) resolves a bare producer instance through `LiveClient.getPerformanceReport` and F14-AC10 requires the whole set green. The carry is counted, not silent: `LiveClient.preEnvelopeResponses` increments on every such body, and closing it is one line in contracts/envelope.ts.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@2c4fad45fb#IRPT_FNTEND-W2-S11",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@df08e2c33c row IRPT_FNTEND-C-S65",
   "portal src/pages/InvestorReporting/__tests__/fe-s-1/adapter.test.ts:205-217 read directly: a transport that resolves `(wire as {instance}).instance` -- the RAW PerformanceReport document -- and `await live.getPerformanceReport(...)` with no try/catch, then asserts the URL. A LiveClient that refused an unenveloped body would reject that promise and fail the test.",
   "MEASURED both ways: with the strict-only path the fe-s-1 suite fails; with `isEnvelopeShaped` gating the parse it passes, and the whole set reads 381 pass / 1 fail (the one failure is W2-S10's, a different file)."
  ],
  "remedy": "A body carrying no envelope identity is refused with a named reason, or 1.0.0_SA_CTO rules at L10 that the contract names its adapted path as intended (C-S65).",
  "owner": "2.0.0_SA_COO~F",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W2-S12",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The consumer NARROWS an optional field of the contract: v1's submit-export response marks `status` OPTIONAL (x-response-contract.status_required false) and its `data` is an ExportReceipt, but `InvestorReportingApi.submitExport` is typed to return the StatusEnvelope ACK, so LiveClient reads `status` and refuses a legal status-less response with EnvelopeMismatch('status').",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@2c4fad45fb#IRPT_FNTEND-W2-S12",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "docs/contracts/investor-reporting/v1/responses/submit-export.response.schema.json @7ce4761a2f: `required: [contract_version, operation, firm_id, data]` (no `status`), `x-response-contract.status_required: false`, `data: {$ref: ../ExportReceipt.schema.json}`.",
   "portal src/api/endpoints/investor-reporting.ts: `submitExport(req): Promise<StatusEnvelope>` on the interface (unchanged since FE-s-1), and `export/submit.ts:87` passes it straight through; its header calls StatusEnvelope \"the immediate ack\"."
  ],
  "remedy": "export/submit.ts:87 returns the ExportReceipt v1 answers in data, not the StatusEnvelope ack -- C-S71's cheap consumer-side fix.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S16",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "OBSERVATION, disclosed because it is the one thing the new content pin cannot see. FE-s-20 replaces the schema DIGEST table with `contracts/wire/consumed.ts`: the operation ids, route keys and required field sets this client consumes. The FIELD axis can only be derived from what the client actually reads, and the only source for that is `contracts/adapt.ts` + `contracts/envelope.ts` -- BOTH of which are FE-s-19's files this round and READ ONLY to me. So `gen-consumed.ts` derives the table ONCE, at generation time, and the table is COMMITTED; no test re-reads adapt.ts. That is deliberate -- a test that re-read a neighbouring cell's text every run would be the same tripwire one layer over -- and its cost is named here: if a later cell makes an adapter read a field the table does not list, NOTHING FAILS. The pin silently under-covers, and an under-covering pin reads exactly like a clean one.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@9cb2d16b3e#IRPT_FNTEND-W2-S16",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S72",
   "portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-consumed.ts on branch wk-irpt_fntend-3-2-fe-s-20: `consumedRows()` reads ADAPT_PATH once and extracts every top-level `wire.<field>` inside each `adapt<Contract>` body; `envelopeFields()` does the same for `body.<field>` and `'<field>' in body` inside `parseIrEnvelope` and `isEnvelopeShaped`. Output written to contracts/wire/consumed.ts and committed.",
   "MEASURED denominator of the derived table: `CONSUMED CONTENT GENERATED: 11 of 11 contracts; 12 operation(s); 12 route key(s); 5 envelope field(s)`; the battery then reports `CONSUMED FIELDS OFFERED: 78 of 78 across 11 schema(s)` and `CONSUMED ENVELOPE FIELDS OFFERED: 49 of 49`."
  ],
  "remedy": "per carrier C-S72: INERT BACKLOG, GRADUATED to 1.0.0_SA_CTO: three limits on the project's own evidence -- a smoke check that cries wolf, a content pin blind in one direction, and a clip nobody can see until the Holdings tree renders. W2-S16: the content pin (__tests__/fe-s-13/gen-consumed.ts) is derived once and committed, so a field REMOVED from an adapter leaves a harmlessly wide pin but a field ADDED leaves an unpinned read until someone re-runs the derivation.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S21",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "WITH THREE DISTINCT STATES, ONLY ONE OF THE THREE HOLDINGS MAPS CAN SHOW ITS BASIS AS CONTENT: HoldingsTab mounts its body ONLY on READY and renders the StatusPanel on every other state. The cell says 'give each of the three maps a status that makes its own basis visible at the view', and F26-AC3 requires three DIFFERENT states. Measured at portal ed90ce2d: observed (READY) mounts `holdings-tab`; target (UNCERTAIN) and missing-attribution (PARTIAL) each mount `status-panel`, where the basis survives only as the public reason code. F26-AC2 through F26-AC7 all PASS; this row is about what FE-s-18's re-capture will then show.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@70e0810f33#IRPT_FNTEND-W2-S21",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@be3b6849a9 row IRPT_FNTEND-C-S57",
   "RUN: `bun test src/pages/InvestorReporting/__tests__/fe-s-26/renders-differently.test.ts` at portal ed90ce2d prints `observed state=READY slot=holdings-tab`, `target state=UNCERTAIN slot=status-panel`, `missing-attribution state=PARTIAL slot=status-panel`, then `PANELS DISTINCT: 3 of 3`; its stripped-status control prints `PANELS DISTINCT: 1 of 3`. Rendered wire -> parseIrEnvelope -> HoldingsTab -> renderToStaticMarkup, the same seed-prop route that __tests__/fe-s-10/tabs-mounted.test.ts uses for this component.",
   "SOURCE: portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx @237a9027 guards the body with `if (!snapshot || envelope.state !== 'READY') return <StatusPanel .../>`, and state/status.ts @237a9027 says 'READY is the only state a complete report path may render through', with NON_ASSERTABLE_STATES = the other 8 of 9. The guard is deliberate design; this row does NOT allege it is a defect."
  ],
  "remedy": "1.0.0_SA_CTO rules W2-S21's (a)/(b)/(c) at L10 (C-S57 (ii); the options are C-S51's), and the claims model or the captures are re-cut so each capture can show what its criterion names.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "3.0.0_SA_CVO",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W2-S9",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "R1 item 2 orders `fixtures/wire/` copies to come from v1 (\"sha256 of the v1 files\"), but docs/contracts/investor-reporting/v1/ PUBLISHES NO FIXTURES -- it carries 11 document schemas, responses/ (11), routes.json and CONTRACT.md and nothing else. The eleven `.valid.json` instances exist ONLY in the producer package, so the SCHEMA pins moved to v1 while the FIXTURE copies still come from infra/aws/lambda/investor-reporting/_contracts/fixtures/, and producer-fixtures.test.ts now PRINTS both sources so no reader infers that both moved.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@2c4fad45fb#IRPT_FNTEND-W2-S9",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "ls docs/contracts/investor-reporting/v1/ @7ce4761a2f (worktree /c/tmp/wk-irpt_fntend-2-4-fe-s-14, workspace HEAD ffa98ac525): AnalysisReport.schema.json, AnalysisRequest.schema.json, CONTRACT.md, DirectoryEntry.schema.json, ExportBundle.schema.json, ExportReceipt.schema.json, HoldingsSnapshot.schema.json, NarrativePacket.schema.json, PerformanceReport.schema.json, RenderPackage.schema.json, ResolvedScope.schema.json, StatusEnvelope.schema.json, responses/, routes.json -- 14 entries, denominator printed, and NO fixtures directory among them.",
   "ls infra/aws/lambda/investor-reporting/_contracts/fixtures/ at the same HEAD: the 11 `<Contract>.valid.json` instances (plus `.invalid.json` and one pre_amendment schema) -- the only place in the repo any producer instance exists."
  ],
  "remedy": "v1 carries fixtures: docs/contracts/investor-reporting/v1/ publishes schemas, responses, routes.json and CONTRACT.md and no fixtures -- a v1 contract ruling at L10 (C-S71: 'the rest need v1 to carry something it does not').",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S5",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "v1's submit-export answers the ExportReceipt WHOLE in data (the receipt carries the producer-minted export_ref.export_id) with the ack in status, but the FE-s-13 typed client's submitExport is typed to the ACK and takes the status half only, and adaptStatusEnvelope carries operation_kind rather than operation_id -- so neither the receipt nor the minted export id reaches a consumer from a submit. The mounted flow therefore submits, then asks export-receipt for the ref THIS browser submitted (the composed bundleRef), and displays a refusal as a refusal. The typed client and adapters are FE-s-13's and READ-ONLY to this order.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@05412fc24c#IRPT_FNTEND-W3-S5",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "docs/contracts/investor-reporting/v1/responses/submit-export.response.schema.json@7ce4761a2f: 'Returns the receipt whole, including job_state -- so a caller that polls and a caller that does not read the same document'",
   "portal src/api/endpoints/investor-reporting.ts@84a86c10:1040-1053 submitExport(...): Promise<StatusEnvelope>, send(..., 'status')"
  ],
  "remedy": "export/submit.ts:87 returns the ExportReceipt v1 answers in data, not the StatusEnvelope ack -- C-S71's cheap consumer-side fix.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S6",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The cell says both ExportAnchorSlot mounts in index.tsx pass the tab's real report refs; the REPORTING tab's reference is reachable (that tab identifies its report by ResolvedScope.revision.revisionId, which performanceReportRequest sends as revision) and is now passed. The ANALYSIS tab's reference is an analysis REQUEST id minted inside tabs/analysis/AnalysisTab.tsx; that file and TabShell are outside this order's grant and expose no callback that would carry it up to index.tsx, so the analysis slot still references nothing rather than referencing the performance revision, which is a different document.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@05412fc24c#IRPT_FNTEND-W3-S6",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "portal src/pages/InvestorReporting/index.tsx (this branch): performance slot reportRefs={resolved ? [resolved.revision.revisionId] : []}; analysis slot unchanged at []",
   "portal src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx@84a86c10:145 getPerformanceReport(performanceReportRequest(scopeRef, period, now))"
  ],
  "remedy": "per carrier C-S71: INERT BACKLOG, GRADUATED to 1.0.0_SA_CTO at L10: nine places where the v1 wire and the consumer do not meet -- none armed, each honest on screen, and each still a contract question no round has ruled. C-S71 did not re-read the second ExportAnchorSlot's report reference at round 4; it states it as the row recorded it.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S8",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "F16-AC5 requires the MISSING HISTORY state to name coverage's cutoff, but v1's NarrativePacket coverage object carries NO DATE AT ALL: its four properties are windows_evaluated, windows_covered, missing_history and missing_history_reason (schema sha256 5a2507151efce130e29c6c5d37aeb5fd4361fe60a040ecfc79eb50ab15c4687a, additionalProperties false). The state itself is gated on the packet's own answer (coverage.missing_history === MISSING_HISTORY) and the DATE named is the earliest cited_evidence[].cutoff_at the packet carries -- the schema's own 'history past this instant was NOT considered'. A selection over carried values, never a computed or inferred date.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@05412fc24c#IRPT_FNTEND-W3-S8",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@a7187bac85 row IRPT_FNTEND-C-S71",
   "workspace docs/contracts/investor-reporting/v1/NarrativePacket.schema.json@7d6db9bcfa: coverage.properties = windows_evaluated, windows_covered, missing_history, missing_history_reason; no date member",
   "portal src/pages/InvestorReporting/contracts/wire/NarrativePacket.ts@84a86c10 mirrors those four"
  ],
  "remedy": "NarrativePacket coverage carries a date, so the print need not name the earliest cited-evidence cutoff (render/narrative/compose.ts:25) -- a v1 contract ruling at L10 (C-S71).",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W4-S7",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "A PROSE MENTION OF <placeholders> BEFORE THE REAL ELEMENT SWALLOWS EVERYTHING BETWEEN THEM, AND THE DECLARATION THEN MEANS ALMOST NOTHING. proof-of-spec-check.py's PLACEHOLDERS_TAG_RE is `<placeholders>(.*?)</placeholders>` with re.S and no line anchoring, so on TO-FE-s-28 -- which discusses the element in its cell text at line 22 and declares it at line 72 -- the match spans 6,958 characters and _declared_placeholders() returns 367 names instead of 1. Every one of those 367 becomes a wildcard under ENFORCE: a recorded invocation may differ from its criterion at ANY <TOKEN> whose name appears anywhere in that span and the limb still reads ALIGNED. This is the SAME class the sibling <paths> limb already fixed with a line-anchored block regex (to-pipeline-gate.py PATHS_BLOCK_RE, '94157 gap (a)'), rediscovered on the element that arms the alignment check itself. GATE (viii), landed this turn, MIRRORS the defect DELIBERATELY -- byte-identical regexes are what stop the gate admitting an element the checker cannot read -- so the gate does not make it worse and does not fix it either.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@946fa17409#IRPT_FNTEND-W4-S7",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@be3b6849a9 row IRPT_FNTEND-C-S56",
   "THE READER: .tools/proof-of-spec-check.py@f3b42b1e0b:1125 `PLACEHOLDERS_TAG_RE = re.compile(r\"<placeholders>(.*?)</placeholders>\", re.S)` and :1146-1156 `_declared_placeholders`, which takes the FIRST match and harvests `re.findall(r\"[A-Za-z][A-Za-z0-9_]*\", m.group(1))` from it.",
   "MEASURED ON THIS ORDER'S OWN FACE, org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-28.mandatory-placeholders.md@f3b42b1e0b: the opening tag the regex finds is the PROSE mention on line 22 ('REFUSAL opt-in via a `<placeholders>` declaration in the task order'); the closing tag is the real element's on line 72. span=(1529, 8516), body=6958 chars, len(_declared_placeholders(text)) = 367 -- including ACCEPTANCE, BOUNDARY, PYTHON, TIMEOUT and every other capitalised word of the cell text. The intended declaration is ONE name: WS.",
   "REMEDY EXECUTED, as recorded by IRPT_FNTEND-C-S85",
   "DISARM RECORDED BY IRPT_FNTEND-C-S85 ('C-S56's two named conditions are met')"
  ],
  "remedy": "Line-anchor PLACEHOLDERS_TAG_RE in BOTH readers (proof-of-spec-check.py and to-pipeline-gate.py) in one change -- C-S56's disarm condition; 2.0.0_SA_COO~F holds W4-S7's issuance side.",
  "owner": "1.0.0_SA_CTO",
  "round": "v4",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v4"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": "2026-09-14T11:26:58Z"
  }
 },
 {
  "id": "IRPT_FNTEND-S61",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "THE GRADED PARTY WRITES THE CHECKER'S NEW/LEGACY BOUNDARY. Limbs 2 and 3 of proof-of-spec-check decide ENFORCE vs ANNOUNCE from the governing order's add commit, and the governing order is read from the instance's decomp_ref.to_ref -- a field the worker writes. Naming a real pre-ruling order moves both limbs to LEGACY with no violation naming the mismatch.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d50d0e6d87#IRPT_FNTEND-S61",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S84",
   "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-29.checker-limbs.proof_of_spec.json@6ad371c88e",
   "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/checker-limbs.result.md@6ad371c88e :30-31, :107-122 (named weakness 4)"
  ],
  "remedy": "S61 disarms as that row names (C-S84): 1.0.0_SA_CTO, as owner of the checker limbs (C-S56): DISARMS when the governing order is bound to the order being flipped -- check_complete_flip passes the flipped order to the checker and the checker refuses an instance whose declared to_ref or to_id names a different order -- with a battery arm that doctors to_ref to a real legacy order and reads REFUSED.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO, as owner of the checker limbs (C-S56): DISARMS when the governing order is bound to the order being flipped -- check_complete_flip passes the flipped order to the checker and the checker refuses an instance whose declared to_ref or to_id names a different order -- with a battery arm that doctors to_ref to a real legacy order and reads REFUSED.",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-S62",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "THE FROZEN READY PRINT CONTRADICTS ITSELF ABOUT ITS WINDOW. Its band states reason REQUESTED_WINDOW_ANSWERED while its own page 3 says 'The source answered a different window from the one requested'. The reason code is defined nowhere, and the renderer compares windows as calendar strings.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@d50d0e6d87#IRPT_FNTEND-S62",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S82",
   "docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json (public_reason_code: pattern only)",
   "portal 741bb54b:src/pages/InvestorReporting/render/performance/MethodsAndSources.tsx:58, :103-104"
  ],
  "remedy": "per carrier C-S82: ROUND-5, GRADUATED to 1.0.0_SA_CTO: EIGHT FIXTURE, CONTRACT AND PRESENTATION GAPS the round surfaced and could not close in its grants -- FWD-11's second firm, a two-writer map, a scope root with no node_kind, a narrative for another revision, an out-of-enum advisory value, a reason code at the band edge, a contract with no report_title, and an undefined window reason (S62). As C-S82 reads it: S62: REQUESTED_WINDOW_ANSWERED is defined nowhere and the renderer compares windows by calendar string.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W1-S56",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The prescribed dev-server launch re-optimized vite's dependency cache THROUGH the node_modules junction -- it rewrites the main checkout's shared node_modules/.vite, which every seat's dev server on this box reads",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@71d47eb8cf#IRPT_FNTEND-W1-S56",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S81",
   "<WS>/.scratch/devserver.log, first lines after '$ vite --port \"5230\" --strictPort': '[vite] (client) Re-optimizing dependencies because vite config has changed', then 'VITE v7.3.5 ready in 1170 ms'.",
   "portal c2eb8eb4 vite.config.ts: no cacheDir key (the server block at :28 sets port discipline, polling watch and proxy only)."
  ],
  "remedy": "vite's cacheDir is worktree-local by config, in a granted cell (C-S81).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W1-S57",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "F30-AC8's invocation sets no IRPT_FE_DEV_PORT, so its browser arm drives WHATEVER answers on the default 5181 -- at this worker's port census a server this worker did not start answered there, so a bare re-run can grade a foreign worktree's page",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@71d47eb8cf#IRPT_FNTEND-W1-S57",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S81",
   "Port census, this worktree: 'PROBE UNREACHABLE ECONNREFUSED from http://localhost:5230/' then 'PROBE REACHABLE HTTP 200 from http://localhost:5181/' (before this worker started any server).",
   "Bare run later (IRPT_FE_DEV_PORT unset): 'PRECONDITION: dev server on http://localhost:5181 -- ABSENT (ECONNREFUSED from http://localhost:5181/) [port from default; ...]', 0 pass, 0 fail."
  ],
  "remedy": "The dev-server helper refuses to run without IRPT_FE_DEV_PORT, or chooses and prints a free port, in a granted cell (C-S81).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W2-S23",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Adding a Holdings envelope for F-CW to fe-s-14-global.json does not make a second firm visible: the page issues ONE holdings request, for the one scope resolve-scope answers, and ui-smoke keys that answer on its URL alone, so from this map the page reaches F-49F's envelope and never F-CW's.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@e46121f301#IRPT_FNTEND-W2-S23",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S82",
   "portal/src/pages/InvestorReporting/tabs/TabShell.tsx:158 @portal c2eb8eb4: '.getHoldingsSnapshot(scopeRef)' -- one request per resolved scope",
   "portal/src/pages/InvestorReporting/index.tsx:54 and :59 @portal c2eb8eb4: resolve-scope keyed on firmId, which travels as a POST body field"
  ],
  "remedy": "per carrier C-S82: ROUND-5, GRADUATED to 1.0.0_SA_CTO: EIGHT FIXTURE, CONTRACT AND PRESENTATION GAPS the round surfaced and could not close in its grants -- FWD-11's second firm, a two-writer map, a scope root with no node_kind, a narrative for another revision, an out-of-enum advisory value, a reason code at the band edge, a contract with no report_title, and an undefined window reason (S62). As C-S82 reads it: W2-S23: the page issues one holdings request for the one scope resolve-scope answers, so it reaches F-49F's envelope and never F-CW's -- FWD-11 PARTIAL.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S24",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "fe-s-14-global.json now has two writers: fe-s-14/gen-maps.ts rewrites the whole file without holdings, so running it alone silently deletes the two Holdings envelopes FE-s-33 added. This is the regeneration hazard FE-s-33 closed for FE-s-26's statuses, moved to a generator outside this grant.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@e46121f301#IRPT_FNTEND-W2-S24",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S82",
   "portal/src/pages/InvestorReporting/__tests__/fe-s-14/gen-maps.ts:95 @portal c2eb8eb4: writes '${SMOKE_DIR}fe-s-14-global.json' from mapFor(...)",
   "portal/src/pages/InvestorReporting/__tests__/fe-s-33/gen-global-holdings.ts @portal 5067c254: header 'WARN: ORDER MATTERS, AND THIS IS THE SECOND WRITER OF ONE FILE'",
   "DISARM RECORDED BY IRPT_FNTEND-S59 (2.0.0_SA_COO~F, the row's disarm owner: 'DISARM BY DETECTION of row W2-S24'); the prevention stays open"
  ],
  "remedy": "The prevention -- one writer of fe-s-14-global.json, or a generator that composes the Holdings envelopes -- carried to 1.0.0_SA_CTO by the disarm row S59, which C-S82 cites ('W2-S24 (with S59) ... detection only').",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": "2026-09-14T05:10:00Z"
  }
 },
 {
  "id": "IRPT_FNTEND-W2-S25",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The wire HoldingsSnapshot has no scope-level node_kind, so one tree root over a scope can only be expressed as an ACCOUNT node. FE-s-33's root is the scope's one account (A-0001), while the same maps' custody_totals.unique_account_count reads 3.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@e46121f301#IRPT_FNTEND-W2-S25",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S82",
   "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json @workspace 0a74710f33: nodes[].node_kind enum has no scope-level member",
   "portal/src/pages/InvestorReporting/contracts/adapt.ts:389 @portal c2eb8eb4: NODE_KIND_FOR_WIRE -- no wire kind maps to the view's 'scope'"
  ],
  "remedy": "per carrier C-S82: ROUND-5, GRADUATED to 1.0.0_SA_CTO: EIGHT FIXTURE, CONTRACT AND PRESENTATION GAPS the round surfaced and could not close in its grants -- FWD-11's second firm, a two-writer map, a scope root with no node_kind, a narrative for another revision, an out-of-enum advisory value, a reason code at the band edge, a contract with no report_title, and an undefined window reason (S62). As C-S82 reads it: W2-S25: HoldingsSnapshot has no scope-level node_kind, so the root is an ACCOUNT node while custody_totals.unique_account_count reads 3.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S27",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The frozen map's narrative packet names performance revision perf-9, not the frozen report's rev-49f-000091, so it is not the frozen report's narrative. FE-s-33 left it out of the envelopes a view reads, because the narrative is off by default in both preview and print, and gave it no status.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@e46121f301#IRPT_FNTEND-W2-S27",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S82",
   "portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json:250 @portal c2eb8eb4: '\"performance_report_revision\": \"perf-9\"'",
   "portal/src/pages/InvestorReporting/export/ExportModal.tsx:79 and :123, portal/src/pages/InvestorReporting/render/PrintEntry.tsx:92 @portal c2eb8eb4: narrative default-off in preview and print"
  ],
  "remedy": "per carrier C-S82: ROUND-5, GRADUATED to 1.0.0_SA_CTO: EIGHT FIXTURE, CONTRACT AND PRESENTATION GAPS the round surfaced and could not close in its grants -- FWD-11's second firm, a two-writer map, a scope root with no node_kind, a narrative for another revision, an out-of-enum advisory value, a reason code at the band edge, a contract with no report_title, and an undefined window reason (S62). As C-S82 reads it: W2-S27: the frozen map's narrative names perf-9, not rev-49f-000091;",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S29",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The observed and target Holdings maps carry advisory_status 'ADVISORY', which is outside the contract enum (ADVISED | RESIDUAL | UNKNOWN). The adapter silently maps it to 'unknown' and keeps authoritative=true, so the READY render shows advisory 'unknown' on every row, and nothing on the page tells it apart from a real classification gap.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@c271e0d702#IRPT_FNTEND-W2-S29",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S82",
   "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json @workspace 073973ff93: advisory_status enum [ADVISED, RESIDUAL, UNKNOWN].",
   "src/pages/InvestorReporting/fixtures/smoke/fe-s-18-holdings-observed.json and fe-s-18-holdings-target.json @portal e85498be: 4 of 4 nodes each carry classification.advisory_status 'ADVISORY' with authoritative true."
  ],
  "remedy": "per carrier C-S82: ROUND-5, GRADUATED to 1.0.0_SA_CTO: EIGHT FIXTURE, CONTRACT AND PRESENTATION GAPS the round surfaced and could not close in its grants -- FWD-11's second firm, a two-writer map, a scope root with no node_kind, a narrative for another revision, an out-of-enum advisory value, a reason code at the band edge, a contract with no report_title, and an undefined window reason (S62). As C-S82 reads it: W2-S29: advisory_status 'ADVISORY' is outside ADVISED|RESIDUAL|UNKNOWN and is mapped to unknown with authoritative=true -- seen on 3 of 3 rows of the READY observed captures (F32-AC9's qualification).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W2-S31",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "At 390, AnswerStatus's reason code line appears to run to or past the right border of its amber band when the code is one long unbroken token (TARGET_BLEND_MODEL_REVISION_UNNAMED, on the Holdings target capture). Read by eye from the capture, not measured.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@c271e0d702#IRPT_FNTEND-W2-S31",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S82",
   "Capture org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-32_holdings_target_390.png (sha256 446581c0365d7f6390599634e1dbf3571d2bf3e319ac784051530fc89f58fa0b, portal 7df6b4a2): the reason line ends at about the band's right border. NO bounding box was measured; the dev server had already been stopped when this was seen.",
   "src/pages/InvestorReporting/tabs/reporting/AnswerStatus.tsx @portal e85498be (FE-s-30): the reason is `<p className=\"mt-1 text-xs\" data-slot=\"answer-reason\">` with no break-all or overflow rule. FE-s-32 imports it unedited. The file is outside FE-s-32's paths."
  ],
  "remedy": "per carrier C-S82: ROUND-5, GRADUATED to 1.0.0_SA_CTO: EIGHT FIXTURE, CONTRACT AND PRESENTATION GAPS the round surfaced and could not close in its grants -- FWD-11's second firm, a two-writer map, a scope root with no node_kind, a narrative for another revision, an out-of-enum advisory value, a reason code at the band edge, a contract with no report_title, and an undefined window reason (S62). As C-S82 reads it: W2-S31: TARGET_BLEND_MODEL_REVISION_UNNAMED reaches its band's right edge at 390 (fe-s-32_holdings_target_390.png, by eye).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S22",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "fe-s-21's F21-AC3 grades an age computed from the as_of INSTANT, not the business date: its panelFor builds the envelope from StatusEnvelope.sourceAsOf (source_dates.as_of), so after ruling K it prints 'business_date=2026-09-11 -> \"Business date age: 1d\"' where the business date's own age on that clock is 2d. The amended check therefore equals formatSourceAge of AS_OF -- the date `pure` is actually computed from -- not of the business date.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@69886501a5#IRPT_FNTEND-W3-S22",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S83",
   "MEASURED, fe-s-21/source-age.test.ts run after the FE-s-34 relabel and before the amendment edit (portal@944499a9): '  WIRE READY -> view READY business_date=2026-09-11 -> \"Business date age: 1d\" (kind=age: true)', the same for all five answer-bearing states, then 'ANSWER-BEARING STATES: 0 of 5'. On the file's clock 2026-09-12T12:00:00Z the business date 2026-09-11 is 36h old (formatSourceAge rounds it to 2d) and AS_OF 2026-09-11T12:00:00Z is 24h old (1d).",
   "portal@c2eb8eb4 __tests__/fe-s-21/source-age.test.ts:80: panelFor sets the envelope's `sourceAsOf: status.sourceAsOf`; contracts/adapt.ts:471 `const asOf = wire.source_dates.as_of ?? null` and :489 `sourceAsOf: asOf`; the test's `pure` at :156 is formatSourceAgeForState(status.state, status.sourceAsOf, now). The file's own header discloses the as_of basis (rows W1-S42 / W1-S43)."
  ],
  "remedy": "Re-point F21-AC3's test (fe-s-21's panelFor builds from StatusEnvelope.sourceAsOf) to the business date -- C-S83: 'a repair must re-point it'.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S25",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "FE-s-30's businessDateOf (state/availability.ts:102-104) reads ANY availability.sourceDate as the STATUS's reading. Under ruling R a no-status document now carries its own reading there, so businessDateOf reports from:'status' for a document date and passes a document null through as fact NULL, where FE-s-30 reads the document plane's null as ABSENT. Measured. It is latent today: the gate sends every no-status wire payload to the panel, not to AnswerStatus.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@0cf8b7f4a0#IRPT_FNTEND-W3-S25",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S83",
   "MEASURED, scratch probe on the portal@fa9cbee21b bytes, whole no-status Holdings v1 bodies through parseIrEnvelope: business_date 2026-09-08 -> availability.producerState=undefined, availability.sourceDate={fact:PRESENT, businessAsOf:2026-09-08} -> businessDateOf {fact:PRESENT, businessDate:2026-09-08, from:status}; business_date null -> sourceDate {fact:NULL, businessAsOf:null} -> businessDateOf {fact:NULL, businessDate:null, from:status}. Read from state/availability.ts:103-108, the same bodies took the document branch before ruling R (they carried no sourceDate): from:'document', with a null read as ABSENT.",
   "One consumer, found with the native Grep tool for businessDateOf and `.from` across the non-test tree: tabs/reporting/AnswerStatus.tsx:24, :45 and :75 (`data-source-date-from={date.from}`); the definition is availability.ts:102. The full InvestorReporting suite after the edit has no failure in fe-s-30 or anywhere else except row W3-S24's line."
  ],
  "remedy": "per carrier C-S83: businessDateOf (state/availability.ts:102-104) keys on the presence of sourceDate; 'the discriminator the gate already uses is producerState'.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W3-S26",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The one reading rule amendment 3 mandates for VIEW fixtures (adapt.ts readingFromValue) turns a view document's null businessAsOf into fact NULL, shown as 'Source date malformed'. But the view contract defines that null as 'no clock' (contracts/index.ts:147), and FE-s-30's businessDateOf reads it as ABSENT. Census: 3 of 134 view documents carry a null, all in smoke/fe-s-3-loading.json; no FixtureAdapter default fixture does.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@af28a2e3d2#IRPT_FNTEND-W3-S26",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S83",
   "MEASURED, a census over every JSON file under portal src/pages/InvestorReporting/fixtures/ (125 files): 134 VIEW documents (an availability object, not a producer `instance`); businessAsOf present on 131, null on 3, missing on 0. The three nulls: smoke/fe-s-3-loading.json at investor-reporting/performance-report, analysis-requests[0] and holdings-snapshot. No file in the portal outside node_modules names fe-s-3-loading (native Grep, 0 matches); smoke maps are handed to scripts/ui-smoke.mjs by `--fixtures`.",
   "portal@c18a2aab contracts/adapt.ts:159-163 readingFromValue: undefined -> ABSENT, null -> NULL, a value -> PRESENT. contracts/index.ts:147 on SourceTimestamps: 'Source clocks. A missing clock is null, never a synthesised `now`.' state/availability.ts:98-100: 'On that plane a null means \"no clock\" ... so it is reported as ABSENT, never as the wire's NULL'."
  ],
  "remedy": "per carrier C-S83: a view document's null businessAsOf renders 'Source date malformed' where the view contract defines null as 'no clock' (contracts/index.ts:147).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W4-S11",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "F36-AC4 describes a real shape -- a `(?<![0-9])0 fail` bar on `bun test <an existing file>` -- that no committed criterion has. At 0a74710f33, the 30 task orders carrying a `0 fail` bar hold 53 single-file bun criteria, all with a BARE `0 fail`, and 0 with the anchored bar. The anchored bar sits only on multi-directory runs, all of them round 5, whose own directories are not yet in the pinned portal commit. The battery grades the two nearest real shapes instead of a joined one it would have had to invent.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@8aa00e60fb#IRPT_FNTEND-W4-S11",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S84",
   ".tools/tests/test_output_vocabulary.py _runner_specimens() (this cell): one `git grep -l -F '0 fail</expect>'` at 0a74710f33 over org/missions, filtered to task-orders -> 30 orders; criteria whose invocation is `cd <WS>/portal && timeout N ...bun test <targets>`: single-file with the anchored bar 0, single-file with a bare `0 fail` 53, multi-directory with the anchored bar 6 (F30-AC8 .. F35-AC6).",
   "Portal pin at 0a74710f33: `git ls-tree 0a74710f33 portal` -> e85f6eb84f; `git --git-dir <main>/portal/.git cat-file -e e85f6eb84f:src/pages/InvestorReporting/__tests__/fe-s-1/keys.test.ts` -> present (F1-AC2's file). F30-AC8's three directories: 2 present, `__tests__/fe-s-30` absent (written by FE-s-30's worker)."
  ],
  "remedy": "per carrier C-S84: ROUND-5, GRADUATED to 1.0.0_SA_CTO: THE CHECKER, THE LAW TEXT AND THE CUT -- the graded party can move limbs 2 and 3 to LEGACY (S61, ARMED), CLAUDE.md quotes a docstring sentence its source dropped (W4-S9), the issuer's ninth cut defect joins S55's class (W4-S11), and six AMGT_RESAPP bars can never match (W4-S12). W4-S11: F36-AC4 named a criterion shape no committed order has, the issuer's defect (9) of 9 this round (96556), with W4-S10's one-suite-short census beside it;",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W4-S12",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Run once over EVERY tracked tree order (359 orders, 1235 mechanical criteria), the new output-vocabulary limb would refuse 6 criteria if they were newly added, all in AMGT_RESAPP: each <expect> is an English sentence (e.g. AMGT-s-1 AC1 `a line containing \"DAPI: UP\" -- the terminal is signed in ...`). proof-of-spec-check grades <expect> as a regex search, so none can ever match its tool's output. The limb is prospective, so none is refused; they are S55's class measured outside IRPT_FNTEND.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@8aa00e60fb#IRPT_FNTEND-W4-S12",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S84",
   "Census (this worker, .scratch; the committed function .tools/to-pipeline-gate.py _output_vocabulary_violations called per order, tools read from this worktree's index = 0a74710f33 + this cell): 359 tree orders, 1235 mechanical criteria -> 17 evaluated and admitted, 6 refused, 160 announced, 438 a runner's vocabulary, 614 not one python program's output.",
   "The 6: AMGT_RESAPP.TO-AMGT-r-1 AC2; TO-AMGT-s-1 AC1, AC2, AC4; TO-AMGT-s-8 AC1; TO-AMGT-s-b4 AC1 (org/missions/D5/AMGT/AMGT_RESAPP/task-orders/ @0a74710f33). Statuses there: TO-AMGT-r-1 <status>complete; TO-AMGT-s-1 <status>complete; TO-AMGT-s-8 <status>complete; TO-AMGT-s-b4 <status>complete."
  ],
  "remedy": "Route the six AMGT_RESAPP criteria whose English-sentence <expect> bars no regex search can match to AMGT_RESAPP's issuer (C-S84).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W5-S1",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "fe-s-19's two browser criteria (F19-AC4, F19-AC5) graded ANOTHER PROJECT'S TREE: the fe-s-27 precondition probe reads MET on any HTTP 200 at the default port 5181, and when this worker's first post-refusal run went out 5181 was held by `node \"C:\\tmp\\wk-dsgn-1e\\portal\\node_modules\\vite\\bin\\vite.js\" --port 5181` (PID 11144, a DSGN worktree) -- BODIES MOUNTED 0 of 2 and UNCERTAIN WITHOUT A WIRE STATE 0 of 2. The same test against THIS worktree's own dev server (IRPT_FE_DEV_PORT=5197) read 2 of 2 and 2 of 2.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@6cd734e28f#IRPT_FNTEND-W5-S1",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S81",
   "netstat -ano: `TCP [::1]:5181 [::]:0 LISTENING 11144`; Get-CimInstance Win32_Process 11144: ParentProcessId 25984, CreationDate 9/13/2026 9:54:49 PM (local), CommandLine `node \"C:\\tmp\\wk-dsgn-1e\\portal\\node_modules\\vite\\bin\\vite.js\" --port 5181` -- not this worktree (C:/tmp/wk-irpt_fntend-5-5-fe-s-35).",
   "The F35-AC6 folder set, run after the one-line refusal and before the fe-s-1 re-base: 273 pass / 3 fail; 2 of the 3 were fe-s-19/mounted-from-wire.test.ts:126 and :136 under `PRECONDITION: dev server on http://localhost:5181 -- MET (HTTP 200 ...) [port from default]`, both tabs `slot=status-panel state=FAILED`, `served(ready): ` EMPTY."
  ],
  "remedy": "The dev-server helper refuses to run without IRPT_FE_DEV_PORT, or chooses and prints a free port, in a granted cell (C-S81).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  }
 },
 {
  "id": "IRPT_FNTEND-W5-S2",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The v1 contract names no `report_title` anywhere -- 0 of 25 files under docs/contracts/investor-reporting/v1/ -- and declares no REQUEST schema for the analysis POST (routes.json carries `response_schema` only), so \"the contract's schema for that field\" does not exist in v1. The type was read from UI_CONTRACT.md S10's \"Browser request\" block (`\"report_title\": null`) plus its table row \"Report title | Optional override\": string | null.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@6cd734e28f#IRPT_FNTEND-W5-S2",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S82",
   "portal 357b4055 __tests__/fe-s-35/no-identity.test.ts, deciding run: `CONTRACT v1 FILES NAMING report_title: 0 of 25 (docs/contracts/investor-reporting/v1/, recursive)`.",
   "docs/contracts/investor-reporting/v1/routes.json @0a74710f33, route `POST /api/scoped/investor-reporting/analysis`: keys route_key, handler, cell, status, note, operation, consumer_operation, response_schema -- no request schema."
  ],
  "remedy": "per carrier C-S82: ROUND-5, GRADUATED to 1.0.0_SA_CTO: EIGHT FIXTURE, CONTRACT AND PRESENTATION GAPS the round surfaced and could not close in its grants -- FWD-11's second firm, a two-writer map, a scope root with no node_kind, a narrative for another revision, an out-of-enum advisory value, a reason code at the band edge, a contract with no report_title, and an undefined window reason (S62). As C-S82 reads it: W5-S2: 0 of 25 v1 files name report_title and routes.json carries no analysis-POST request schema.",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W5-S4",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "To separate the foreign-server red (W5-S1) from a real one, this worker started a vite dev server from its own worktree on port 5197 -- an act the order did not name -- and vite re-optimized dependencies into its cache under node_modules. That node_modules is a JUNCTION to the main checkout's portal/node_modules, so the write landed in the shared tree. `bun run typecheck` (tsc -b) likewise writes its tsbuildinfo into node_modules/.tmp through the same junction on every F35-AC1 run.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@6cd734e28f#IRPT_FNTEND-W5-S4",
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/adjudications/ADJUDICATION_v2.md@d50d0e6d87 row IRPT_FNTEND-C-S81",
   "vite v7.3.5 started from C:/tmp/wk-irpt_fntend-5-5-fe-s-35/portal with `node node_modules/vite/bin/vite.js --port 5197 --strictPort` printed `(client) Re-optimizing dependencies because vite config has changed`; portal/vite.config.ts sets no `cacheDir` (vite's default is node_modules/.vite -- INFERRED location, not listed).",
   "The issuer's facts at the cut: `<WS>/portal/node_modules = a JUNCTION to C:/Users/AndrewBerman/Desktop/ajb_workspace/portal/node_modules`."
  ],
  "remedy": "tsc -b's tsbuildinfo stays inside the worktree, in a granted cell (C-S81).",
  "owner": "1.0.0_SA_CTO",
  "round": "v5",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v5"
  },
  "closed": false
 }
]
```
