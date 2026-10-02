# DSGN_IRPTV1 -- adjudication v7: the FAST interval backlog (72 rows)

<sweep_watermark>2026-10-02T03:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO. Document v7. Fabric: laptop. Recorded: 2026-10-02T03:10:00Z.

**Input.** No drain-end packet: the project has run FAST since 2026-09-28 and its 84 orders read 75 complete, 9 superseded, 0 open. Census by the row gate's own resolver (`.tools/surprise-row-gate.py` `_latest_dispositions`) at HEAD: 130 investigation items, 72 UNDER_INVESTIGATION (65 INERT, 7 ARMED), 40 GRADUATED, 18 DISMISSED_WITH_REASON. A json-only parse reads 81 undispositioned: the 9 more (S31, S32, S33, W22-S4, W25-S1, W34-S2, W36-S4, W36-S5, W38-S5) carry DISMISSED_WITH_REASON in their own rows, which the resolver counts. They are not re-adjudicated here. The last item was surfaced 2026-10-01T00:10Z (S42).

**Checked at this seat, not taken from a record.** Code reads at portal origin DEV 24646bca (git show / git grep / ancestry with a control); one bun test run of 7 files whose bytes equal 24646bca (13 pass, 0 fail); one read-only CloudWatch Logs read of irpt-status (4 days). The full IR suite is not run: it regenerates contracts/wire/* in the shared checkout.

**Tally: 72 of 72.** 59 dismissed by C-S61 to C-S67; 13 graduated by C-S68 into REMEDIATION_v5.md (7 ARMED: 5 REMEDIATED and closed, S27 DISARMED with its remediation OPEN, W39-S2 still ARMED; 6 INERT OPEN). Carried unchanged: every open row of REMEDIATION_v1 to v4, including the S7 family (S7, W21-S2, W23-S1, W29-S10, W34-S1) and W35-S1, W35-S2.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S61",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:10:00Z",
    "one_line": "Ten rows are records of other rows' disarms or of a round's close (S4, S8, S10, S11, S13, S14, S15, S21, W29-S5, W41-S1); none carries a hazard of its own.",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S4",
      "DSGN_IRPTV1-S8",
      "DSGN_IRPTV1-S10",
      "DSGN_IRPTV1-S11",
      "DSGN_IRPTV1-S13",
      "DSGN_IRPTV1-S14",
      "DSGN_IRPTV1-S15",
      "DSGN_IRPTV1-S21",
      "DSGN_IRPTV1-W29-S5",
      "DSGN_IRPTV1-W41-S1"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an ARMED item only on a read showing it disarmed.",
    "world_is": "Every item these rows point at is dispositioned at HEAD by the row gate's resolver: S3 GRADUATED, S6 GRADUATED, S19 GRADUATED, W29-S2 GRADUATED, W29-S3 GRADUATED, S5 GRADUATED, S7 GRADUATED, S9 DISMISSED_WITH_REASON. S10's five items were carried to TO-IV-e-13 and TO-IV-e-18, both complete. W41-S1 disarmed itself in its own commit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/surprise-row-gate.py _latest_dispositions(root, 'DSGN_IRPTV1') at HEAD (this seat, 2026-10-02 03:0xZ): 130 items, 72 UNDER_INVESTIGATION, 40 GRADUATED, 18 DISMISSED_WITH_REASON; the values above read from it",
        "task-orders <status> at HEAD: TO-IV-e-13 complete, TO-IV-e-18 complete; the project's 84 orders read 75 complete, 9 superseded, 0 open",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md rows S4, S8, S10, S11, S13, S14, S15, S21, W29-S5, W41-S1 (each names the row it disarms or the round it closes)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Evidence and round records: each points at an item already dispositioned or an order already complete; no hazard remains on any of the ten."
  },
  {
    "id": "DSGN_IRPTV1-C-S62",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:10:00Z",
    "one_line": "The export and owned-request chain rows S18, S20, S22, S23, S24, S25 and S26 are remedied in the code at portal DEV: each named order is complete and its commit is in DEV's history, and the item and report reads carry selected_tenant.",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S18",
      "DSGN_IRPTV1-S20",
      "DSGN_IRPTV1-S22",
      "DSGN_IRPTV1-S23",
      "DSGN_IRPTV1-S24",
      "DSGN_IRPTV1-S25",
      "DSGN_IRPTV1-S26"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an ARMED item only on a read showing it disarmed.",
    "world_is": "At portal origin DEV 24646bca: listOwnedAnalysisRequests exists (investor-reporting.ts:1045, comment cites S18); getOwnedAnalysisRequest and getOwnedAnalysisReport send selected_tenant (investor-reporting.ts:1060-1073, comment cites S25); the submit and preview carry the tenant; a data-less QUEUED submit starts the receipt poll. No page export has yet been observed to reach READY: that residual is carried on S27 (REMEDIATION_v5).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log 24646bca --grep TO-<id> (this seat, 03:0xZ): IV-e-62 ab107147, IV-e-53 cad4d979, IV-e-64 55bbdd71, IV-e-65 21ec94d8, IV-e-66 a5107226, IV-e-67 8808eeb6, each in DEV's history; the seven orders read complete at HEAD",
        "git grep -n selected_tenant 24646bca -- src/api/endpoints/investor-reporting.ts: lines 1037-1073 and 1087-1169 (item, report, selection, directory, performance and status reads)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w21-part-p-walk-20260929.md@bc3a514122: POST /export?selected_tenant=49financial 200 QUEUED; the opened READY request read 200 on all three reads"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remedied by orders that completed and are in DEV's history, read in the code; the export journey's last step (a READY receipt on the page) is carried on S27, not here."
  },
  {
    "id": "DSGN_IRPTV1-C-S63",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:10:00Z",
    "one_line": "Nine rows count or describe Investor Reporting suite failures outside their cells (W4-S2, W13-S1, W16-S1, W21-S3, W21-S4, W27-S2, W29-S4, W35-S3, W36-S1). The S7 family of rows already carries that hazard, OPEN and ARMED.",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W4-S2",
      "DSGN_IRPTV1-W13-S1",
      "DSGN_IRPTV1-W16-S1",
      "DSGN_IRPTV1-W21-S3",
      "DSGN_IRPTV1-W21-S4",
      "DSGN_IRPTV1-W27-S2",
      "DSGN_IRPTV1-W29-S4",
      "DSGN_IRPTV1-W35-S3",
      "DSGN_IRPTV1-W36-S1"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an ARMED item only on a read showing it disarmed.",
    "world_is": "STATUS.md records the IR scope at 775c4261 as 949 pass, 27 skip, 18 fail: the known five plus row S40's 13. The known five are the fixture smoke map, source bounds (W21-S4's ycharts token), F25-AC2 twice and F25-AC3 (W35-S3's fe-s-25 file). The run-to-run instability (W21-S3, W36-S1) is W29-S10's subject. S7 (REMEDIATION_v2), W21-S2, W23-S1 and W29-S10 (REMEDIATION_v3) and W34-S1 (REMEDIATION_v4) are OPEN and ARMED at HEAD; their remedy order TO-IV-e-50 reads superseded.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md (2aed13d096) Pins row 'Suite on 775c4261'",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~42/DSGN_IRPTV1.TO-IV-e-81.search-only.proof_of_spec.json:63: 'exactly the known five fail (fixture set smoke map, source bounds, F25-AC2 x2, F25-AC3)'",
        "remediation rows read at HEAD (this seat, 03:0xZ): S7 OPEN ARMED; W21-S2, W23-S1, W29-S10 OPEN ARMED; W34-S1 OPEN ARMED; TO-IV-e-50 <status> superseded"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Duplicates of the open S7 family. The suite is not re-run here: a full IR run regenerates contracts/wire/* in the shared checkout (STATUS.md), which this seat does not write."
  },
  {
    "id": "DSGN_IRPTV1-C-S64",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:10:00Z",
    "one_line": "S35, S36 and S39 widen or re-measure S34 (a raw public reason code on the Analysis face). S34 is graduated as their one carrier.",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S35",
      "DSGN_IRPTV1-S36",
      "DSGN_IRPTV1-S39"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an ARMED item only on a read showing it disarmed.",
    "world_is": "At portal origin DEV 24646bca two of the three surfaces still print the code: StageDisplay.tsx:62 '({envelope.publicReasonCode})' and GenerateComposer.tsx:469 the Holdings-snapshot line. The request-history row now words it (OwnedRequestHistory.tsx:93). S35 shows the served envelope carries the codes, so live traffic reaches the face.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 24646bca:src/pages/InvestorReporting/tabs/analysis/StageDisplay.tsx line 62; git grep publicReasonCode 24646bca -- tabs/analysis: GenerateComposer.tsx:469",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md rows S34, S35, S36, S39"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "One hazard, one carrier: S34 in REMEDIATION_v5 holds both surfaces still live."
  },
  {
    "id": "DSGN_IRPTV1-C-S65",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:10:00Z",
    "one_line": "Nineteen worker rows record how a cell read or resolved its own text, inside its own grant, with every criterion passing (W4-S1, W5-S1, W5-S2, W5-S3, W5-S4, W6-S1, W6-S2, W8-S1, W9-S2, W9-S3, W14-S1, W15-S1, W18-S2, W25-S2, W25-S3, W25-S4, W27-S1, W38-S2, W39-S1). None leaves a hazard.",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W4-S1",
      "DSGN_IRPTV1-W5-S1",
      "DSGN_IRPTV1-W5-S2",
      "DSGN_IRPTV1-W5-S3",
      "DSGN_IRPTV1-W5-S4",
      "DSGN_IRPTV1-W6-S1",
      "DSGN_IRPTV1-W6-S2",
      "DSGN_IRPTV1-W8-S1",
      "DSGN_IRPTV1-W9-S2",
      "DSGN_IRPTV1-W9-S3",
      "DSGN_IRPTV1-W14-S1",
      "DSGN_IRPTV1-W15-S1",
      "DSGN_IRPTV1-W18-S2",
      "DSGN_IRPTV1-W25-S2",
      "DSGN_IRPTV1-W25-S3",
      "DSGN_IRPTV1-W25-S4",
      "DSGN_IRPTV1-W27-S1",
      "DSGN_IRPTV1-W38-S2",
      "DSGN_IRPTV1-W39-S1"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an ARMED item only on a read showing it disarmed.",
    "world_is": "Each row says not blocking and names its criteria passing. Two were re-read here. W5-S4: adapt.ts:790 still sets displayName to account_id, and AccountsTable.tsx's detector (lines 10-15, NOT_SUPPLIED at 45) prints 'not supplied', never the id. W9-S2's open question is answered: 24 contract schemas in docs/contracts/investor-reporting/v1 against 23 generator entries, and the one missing is ComparisonCatalogue, which is row S40.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 24646bca:src/pages/InvestorReporting/contracts/adapt.ts lines 790-791; git grep 'not supplied' 24646bca -- tabs/reporting/AccountsTable.tsx",
        "ls docs/contracts/investor-reporting/v1/*.schema.json (24) against WIRE_CONTRACTS in 24646bca:src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts (23): missing ComparisonCatalogue only",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md rows as listed (each with its 'Not blocking' note)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Method and scoping notes of completed cells; W4-S1's comp-pulse basename collision is advisory (the commit proceeded) and belongs to the comp-pulse owner, not to this project."
  },
  {
    "id": "DSGN_IRPTV1-C-S66",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:10:00Z",
    "one_line": "W4-S3, W26-S1, W26-S2 and W41-S2 document test-harness traps on this box (CRLF against git-show blobs, renderToStaticMarkup entity-encoding an apostrophe, EOL-only churn from the wire generator). Each was handled in its cell and nothing was committed past a grant.",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W4-S3",
      "DSGN_IRPTV1-W26-S1",
      "DSGN_IRPTV1-W26-S2",
      "DSGN_IRPTV1-W41-S2"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an ARMED item only on a read showing it disarmed.",
    "world_is": "The churn is still produced by a full IR run (23 contracts/wire files EOL-only, STATUS.md) and is restored to HEAD after each run, never committed. No served byte depends on it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md (2aed13d096) Pins row 'Suite on 775c4261': 'A suite run REGENERATES contracts/wire/* onto disk ... restored to HEAD after each run, never committed by this lane'",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md rows W4-S3, W26-S1, W26-S2, W41-S2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Instrument notes with no product hazard; kept as rows for the next author who meets the trap."
  },
  {
    "id": "DSGN_IRPTV1-C-S67",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:10:00Z",
    "one_line": "Seven rows are remedied or moot in the world: W18-S1 (the legend now lists 'other'), W30-S2, W30-S4 and W38-S3 (the colour changes they describe were reverted to standard hues), W30-S3 (the missing test file is now on DEV), S41 (no 0x08 byte left in HeaderBrief.tsx) and S42 (the dev-server cache is present).",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W18-S1",
      "DSGN_IRPTV1-W30-S2",
      "DSGN_IRPTV1-W30-S3",
      "DSGN_IRPTV1-W30-S4",
      "DSGN_IRPTV1-W38-S3",
      "DSGN_IRPTV1-S41",
      "DSGN_IRPTV1-S42"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an ARMED item only on a read showing it disarmed.",
    "world_is": "At portal origin DEV 24646bca: ConsolidatedOverviewPanel.tsx:391 lists ['cash','fixed_income','equity','alternatives','other']; ASSET_CLASS.commodities is PALETTE.yellow500 (chartColors.ts:226) after 3e2233de (Andrew-direct 2026-09-29, standard hues), so green900 carries one meaning again and the yellow500 notes W30-S2 called stale are current; assetClass.ts carries no blue500/blue600 comment; iv-e-48 is in __tests__/dsgn-irptv1 (1 file); HeaderBrief.tsx holds 0 bytes 0x08 of 8,905; portal/.vite/deps exists with 10 deps_temp_* directories beside it. One stale note remains: chartColors.ts:161-178 still narrates commodities as green900 (comment only, no behaviour).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git grep / git show at 24646bca (this seat, 03:0xZ): the six reads above",
        "git show 24646bca:src/pages/SecurityAnalysis/components/HeaderBrief.tsx | count of b'\\x08': 0 of 8905 bytes",
        "ls -d portal/.vite/deps (present); ls -d portal/.vite/deps_temp_* : 10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remedied or overtaken in the world, each read here. S42's cause stays unidentified; it re-opens as a new row if the cache vanishes again."
  },
  {
    "id": "DSGN_IRPTV1-C-S68",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T03:10:00Z",
    "one_line": "Thirteen rows GRADUATE to REMEDIATION_v5: the seven ARMED rows (S27, S28, S29, S30, W36-S3, W38-S4, W39-S2) and six INERT rows still true in the world (S12, S34, S37, S38, S40, W40-S1). Five ARMED rows arrive remediated and closed; S27 arrives disarmed with its remediation open; W39-S2 stays ARMED.",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S27",
      "DSGN_IRPTV1-S28",
      "DSGN_IRPTV1-S29",
      "DSGN_IRPTV1-S30",
      "DSGN_IRPTV1-W36-S3",
      "DSGN_IRPTV1-W38-S4",
      "DSGN_IRPTV1-W39-S2",
      "DSGN_IRPTV1-S12",
      "DSGN_IRPTV1-S34",
      "DSGN_IRPTV1-S37",
      "DSGN_IRPTV1-S38",
      "DSGN_IRPTV1-S40",
      "DSGN_IRPTV1-W40-S1"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every investigation item is dispositioned on grounded evidence; an ARMED item only on a read showing it disarmed.",
    "world_is": "Each row's read is in its own evidence in REMEDIATION_v5.md.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v5.md (same commit)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```
