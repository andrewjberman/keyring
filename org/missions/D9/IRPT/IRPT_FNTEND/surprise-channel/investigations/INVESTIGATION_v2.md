# IRPT_FNTEND -- surprise channel, INVESTIGATION v2 (round 2, laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "IRPT_FNTEND-W1-S15",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T09:12:00Z",
    "one_line": "TO-FE-s-12's <proof_of_spec> block specifies `phase BUILD`, but org/standards/PROOF_OF_SPEC.schema.json's `phase` enum carries no `BUILD` member -- proof-of-spec-check.py refuses the ordered value outright, so no instance written exactly as this order specifies it can ever validate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.md @d45d2760f2, <proof_of_spec> block: \"(phase `BUILD`, firm `FABRIC`, spec_ref.group `OTHER`)\" -- the same three-value parenthetical is repeated verbatim in this worker's WORKER FACE.",
        "org/standards/PROOF_OF_SPEC.schema.json @d45d2760f2, properties.phase.enum, read directly: ['P1-SCRIPTS', 'P2-TIMING', 'P3-REPOINTS', 'P4-PUBLISHERS', 'P5-DECOMMISSION', 'BUILD-GENERAL', 'INVESTIGATION', 'NON-BUILD-OTHER'] -- 8 members, denominator printed, and `BUILD` is not one of them.",
        "MEASURED, not inferred from the enum: the instance was authored with the ORDERED value and run through the gate first -- `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.proof_of_spec.json F12-AC1,F12-AC2,F12-AC3,F12-AC4,F12-AC5` returned `VIOLATION: schema: phase: 'BUILD' is not one of ['P1-SCRIPTS', 'P2-TIMING', 'P3-REPOINTS', 'P4-PUBLISHERS', 'P5-DECOMMISSION', 'BUILD-GENERAL', 'INVESTIGATION', 'NON-BUILD-OTHER']` and INVALID (rc=1). checker-vintage 709b9556a3 2026-09-10T14:37:30Z.",
        "The other two round-1 sibling instances in this deliverables folder that were written against the same schema (IRPT_FNTEND.TO-FE-s-11 and TO-FE-s-9 .proof_of_spec.json) both carry phase `INVESTIGATION`, a declared enum member -- so this is the first instance in this project ordered to a value the schema does not hold, not a long-standing tolerated deviation.",
        "Scope of the claim, stated: this row asserts ONLY that the literal token `BUILD` is refused by the phase enum. It does NOT assert that `BUILD-GENERAL` is the phase the issuer INTENDED -- that is the issuer's call; `BUILD-GENERAL` was chosen here as the nearest and only build-flavoured member, and the substitution is disclosed in the instance's own `surprises` array so a grader sees it without reading this row."
      ]
    },
    "spec_asserts": "This order's <proof_of_spec> block: the instance is to be written with `phase BUILD` and validated with `python .tools/proof-of-spec-check.py <instance> F12-AC1,..,F12-AC5` BEFORE the `complete` flip, and the flip happens only when the checker passes.",
    "world_is": "Those two instructions cannot both be satisfied as written: `phase: \"BUILD\"` is a hard schema violation and the checker returns INVALID (rc=1) on it, so the instance was carried as `BUILD-GENERAL` -- the nearest enum member -- and the deviation from the ordered literal is disclosed both here and in the instance's `surprises` array. hazard_standing INERT: the substitution is a metadata-field value on a proof instance, it moves no criterion, no artifact and no graded outcome (all five criteria are a typecheck, two bun test runs and two git diffs, each PASS by its own output either way), and the gate itself is the thing that catches the ordered value, so the failure mode is a loud refusal rather than a silent wrong record. No disarm_owner: nothing is armed. The standing question for the issuer -- whether future IRPT task orders should specify `BUILD-GENERAL`, or whether `BUILD` should be added to the ratified enum -- is a schema/issuance decision above this worker's lane and is left open, not decided here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S18",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T12:35:00Z",
    "one_line": "Round 2 opened: decomposition v0.2 @430c5fcb4a (seven additive cells on the CTO's seven rulings), ONE issuance @75d2e353a8, COMPLETION_REPORT.round1.json (8 of 8 COVERED). FE-s-12 (the typecheck repair) is terminal and drained in both repos: portal DEV 32a744dc reads `bun run typecheck` rc=0 by the issuer's own run and 322 pass, 1 skip, 0 fail; four lines changed in the two fe-s-11 test files, shims and tsconfig untouched (OUTSIDE-GRANT: 0, SHIMS-EDITED: 0). DEV is green under tsc: the analysis's ruling 1 precondition for a DEV push is met at 32a744dc. One issuer face defect carried by the worker (W1-S15): every round-2 BUILD order named proof phase `BUILD`, a value the PROOF_OF_SPEC schema's phase enum does not hold (P1..P5, BUILD-GENERAL, INVESTIGATION, NON-BUILD-OTHER); the five non-terminal orders FE-s-13..17 are amended to BUILD-GENERAL in one commit; FE-s-18 is INVESTIGATION. The worker also recorded, ungraded: colour-law.test.ts's positive control asserts only scannedFiles > 0, so a scan that collapses to one file still passes -- carried to FE-s-18's face reading as a control to tighten.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DEV @32a744dc, issuer's run: `bun run typecheck` rc=0; `bun test src/pages/InvestorReporting` 322 pass, 1 skip, 0 fail, 48 files",
        "workspace @69aa29687c -- proof-of-spec-check on the FE-s-12 instance: VALID rc=0, 5 acceptance rows; git show --format= --name-only on each of the 3 worker commits -- portal: 0 lines (no gitlink)",
        "org/standards/PROOF_OF_SPEC.schema.json @HEAD -- phase enum: P1-SCRIPTS, P2-TIMING, P3-REPOINTS, P4-PUBLISHERS, P5-DECOMMISSION, BUILD-GENERAL, INVESTIGATION, NON-BUILD-OTHER (read by the issuer after row W1-S15)",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-1[3-7].*.md -- 5 of 5 carried `phase BUILD` at 75d2e353a8; amended this turn"
      ]
    },
    "spec_asserts": "Issuer faces FE-s-12..17: proof instance phase `BUILD`. Analysis ruling 1: no DEV push before the typecheck repair lands.",
    "world_is": "The enum has no BUILD; the checker refuses the instance and the worker substituted the nearest member and rowed it. The repair landed; DEV is green; the push precondition is met and the push itself is 0.0.0_AB_MSTR's on Andrew's word, with this lane's gitlink bump after it.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S16",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T13:36:43Z",
    "one_line": "FE-s-13's face orders the two no-route operations RETIRED from InvestorReportingApi (previewExportBundle removed) and says only __tests__/fe-s-1/ needs updating -- but SEVEN test files in FIVE folders OUTSIDE this order's grant bind those exact members and the round-1 path literals, so retiring them as written makes F13-AC1 and F13-AC10 unreachable without writing outside the grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal @32a744dc, comp-find over src/pages/InvestorReporting/__tests__ for the eleven round-1 slugs plus previewExportBundle|IR_OPERATIONS|irRoute: DENOMINATOR 36 hits across 55 files scanned. Outside fe-s-1 and fe-s-13 the binding hits are: fe-s-6/_load.ts:33-34 (adapter.useFixture('analysis-requests', ...) then adapter.listAnalysisRequests(...)), fe-s-6/variants.test.ts:28 (adapter.fixtureFor('analysis-requests')), fe-s-9/no-refetch.test.ts:32,66,72,89 (useFixture('export-preview', ...), calls.some(url => url.includes('export-preview')), includes('performance-report')), fe-s-9/resolve.test.ts:85 (an api stub literal carrying previewExportBundle), fe-s-2/search.test.ts:14-15,156 (imports IR_OPERATIONS/irRoute, compares call-log urls to irRoute('directory-search')).",
        "Two further foreign suites assert the ROUND-1 PATH LITERAL on the FixtureAdapter's call log: fe-s-3/selection.test.ts:98 and fe-s-10/switch.test.ts:50 both expect(adapter.callLog[0].url.endsWith('performance-report')), and fe-s-6/correction.test.ts:58 filters on entry.url.endsWith('/submit-correction'). None of those literals is a declared path in routes.json @bef9b459f3.",
        "This order's <paths> block names portal/src/pages/InvestorReporting/__tests__/fe-s-1/ and .../__tests__/fe-s-13/ and no other test folder, so fe-s-2, fe-s-3, fe-s-6, fe-s-9 and fe-s-10 are outside the write grant.",
        "MEASURED baseline before any edit, from this worktree: bun test src/pages/InvestorReporting = 322 pass, 1 skip, 0 fail across 48 files. MEASURED after this cell: 344 pass, 1 skip, 0 fail across 53 files, and bun run typecheck rc=0. POSITIVE CONTROL on that rc: a planted const zzControl: number = 'not a number' in contracts/adapt.ts made the same command exit 2 with TS2322 at adapt.ts(1144,7), so the rc=0 is a real pass and not a stale incremental no-op."
      ]
    },
    "spec_asserts": "FE-s-13 item 2: analysis-requests and export-preview are RETIRED from InvestorReportingApi, previewExportBundle is removed, and IR_OPERATIONS/irRoute/IR_METHOD_VERB are REPLACED by the routes.json-derived table. Item 5: the existing tests under __tests__/fe-s-1/ are updated where the shapes changed (no other test folder is named). F13-AC10: the whole Investor Reporting set is green.",
    "world_is": "Removing the two members from the interface, or repointing the FixtureAdapter's call-log urls onto the declared paths, breaks seven test files in five folders this order does not grant. What was built instead, and is disclosed here rather than assumed: (1) the LIVE plane speaks ONLY the new table -- IR_ROUTE_TABLE (12 rows = routes.json's 11 DECLARED plus 1 NO-HANDLER-AT-HEAD), irBuildRequest binds each path, and LiveClient.listAnalysisRequests/previewExportBundle reject with the typed NoDeclaredRoute while getHoldingsSnapshot rejects with NotYetExercisable (F13-AC2 prints ROUTES MATCHED: 11 of 11 and NOT-YET-EXERCISABLE: 1; F13-AC8 prints NO-DECLARED-ROUTE: 2 with REQUESTS ISSUED: 0); (2) the two members REMAIN on the interface as RETIRED members that only the FIXTURE plane answers, and the legacy slug vocabulary (IR_OPERATIONS, irRoute, IR_METHOD_VERB, IR_FIXTURE_PLAN) is kept as the FixtureAdapter's own fixture-plane vocabulary rather than deleted. COST, stated plainly: an assertion on the FixtureAdapter's call-log URL no longer proves anything about the live path -- the declared-path claim lives on F13-AC2 (the table against routes.json) and F13-AC9 (the browser run against the declared paths), not on the adapter's log. hazard_standing INERT: nothing is armed, nothing served moves, and both planes are exercised by tests in this round. The decision this worker did NOT take: whether the foreign suites should be re-pointed onto the declared paths in a later cell (which would let the two members be deleted outright) is the issuer's, and the lane gate is exactly why it is not taken here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S17",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T13:37:10Z",
    "one_line": "Five places where the producer's contract and the consumer's view type do not map 1:1 -- three closed vocabularies lose a value on the way in, one view field could only be filled from a SERVER-ONLY storage key (so it is filled with null), and the producer's benchmark fact is an unstructured object the view's BenchmarkFact cannot be built from. Each is carried as an explicit unknown and named in FIELD_MAP; none is guessed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PIN AUTHORITY, checked first: docs/contracts/investor-reporting/v1/ does NOT exist in this worktree (ls docs/contracts -> No such file or directory at 6ecffd5b15), so per this order's BOUNDS the two RAW pins are the authority -- routes.json @bef9b459f3 and _contracts/ @33351469c2 -- and WIRE_SCHEMA_PINS carries the sha256 of each of the eleven schema FILES as read from infra/ (producer-fixtures.test.ts re-digests them and compares, printing WIRE SCHEMA PINS FRESH: 11 of 11).",
        "(a) DirectoryEntry.access.entitled: the wire enum is GRANTED|DENIED|UNKNOWN (DirectoryEntry.schema.json properties.access.properties.entitled), the view's AccessFacts.entitled is a BOOLEAN (contracts/index.ts:211). UNKNOWN cannot be represented; it adapts to the NON-ASSERTING false. The producer's own account-only fixture instance (instance_account_only) carries exactly entitled: UNKNOWN, so the case is real and not hypothetical.",
        "(b) DirectoryEntry.permitted_capabilities: the wire vocabulary is DIRECTORY_READ|PERFORMANCE_READ|HOLDINGS_READ|ANALYSIS_REQUEST|EXPORT_REQUEST; the view's Capability union is view-performance|view-holdings|view-analysis|submit-correction|export|view-narrative. DIRECTORY_READ has no view member (dropped); submit-correction and view-narrative have no wire member (never populated). The schema's own words for the field are 'a capability absent from the list is not permitted', so the view's withheldCapabilities could only be a COMPLEMENT this adapter refuses to compute -- it carries [].",
        "(c) AnalysisRequest.stage: the wire has 8 members (RECEIVED, PARSED, NEEDS_CORRECTION, READY, SUBMITTING, GENERATED, RELEASED, FAILED), the view's AnalysisStage has 7; SUBMITTING and GENERATED both land on 'generating'. The mapping is therefore lossy in that one direction, which matters only if a later cell ever maps a view stage back to the wire.",
        "(d) AnalysisReport.release.protected_pdf_ref carries {storage_key, sha256, server_only: true} -- a SERVER LOCATION. The view's ProtectedArtifactRef REQUIRES downloadRoute, 'Authorized route the browser may request', and the wire carries no route at all. adaptAnalysisReport yields protectedArtifact: null rather than renaming a storage key into a route; the consequence is that VendorPdfPreview renders nothing on the live plane until the producer carries a route.",
        "(e) PerformanceReport.optional_facts.benchmark is typed object|null with no properties (PerformanceReport.schema.json), so the view's BenchmarkFact[] (benchmarkId, displayName, periodReturns) cannot be built from it without inventing a shape; benchmarks adapts to []. Two smaller ones of the same family, listed for completeness: the ResolvedScope firm catalogue carries only {firm_id, selected} so PermittedFirm.displayName shows the OPAQUE ID (never a name invented here), and NarrativePacket carries cited_evidence at the PACKET level while the view hangs evidence off each EVENT, so events[].evidence is [] rather than one packet's evidence duplicated onto every event."
      ]
    },
    "spec_asserts": "FE-s-13 item 3: each adapter RENAMES and RESTRUCTURES only; a view field the wire does not carry is dropped from the view type or filled with the envelope's explicit unknown -- never a default, never arithmetic, never an inference; FIELD_MAP names every field of every view type with the wire path it comes from and its kind admits no derived value.",
    "world_is": "Held exactly, and the five gaps above are where holding it COSTS something visible on screen. Every one is filled with that field's own explicit unknown (null, 'unknown', [], or the non-asserting false) and named in FIELD_MAP with WIRE_ABSENT plus the reason; F13-AC6 prints FIELD MAP: 150 of 150 view fields mapped and DERIVED FIELDS: 0 over a denominator taken by reflection over the adapted producer fixtures, not from the map. hazard_standing INERT: no hazard is armed -- the failure mode of each gap is a screen showing 'unknown' or an empty section, never a wrong number, and the alternative (computing the complement, promoting a storage key to a route, inventing a benchmark shape) is what the cell's own bound forbids. For the counterpart, (d) is the one with a product consequence: a protected artifact the browser is meant to be able to download has no authorized route on the contract.",
    "disposition": "UNDER_INVESTIGATION"
  }
]
```
