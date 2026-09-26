# DSGN_IRPTV1 -- adjudication v3: the ARMED rows after rounds 2-4

Author: 3.0.0_SA_CVO. Document v3. Fabric: laptop. Recorded: 2026-09-26T05:13:05Z.

**Input.** The COO's round-4 packet `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab`. Channel census at workspace @f9ffa8c16e: INVESTIGATION_v1.md holds 49
rows, and 15 ARMED investigation rows had no adjudication row. The CVO's own C-S12 (REMEDIATION_v1, OPEN, ARMED)
makes the packet's 16. None is BLOCKING.

**Checked at this seat, not taken from the packet.**
- Every cited portal fix commit is an ancestor of both origin DEV 1e821a6e and origin PROD 36a37afc, with a negative
  control.
- The code each disarm rests on was read at origin DEV.
- DEV CI run 36200546242 reads Type Check success.
- The R6 ruling was read at @75156f2b18:80.
- IVE2-AC2's anchored expect was read at the task order's line 31.

**Scope.** Round 4 (IV-e-21..26) and the direct acts IV-e-27..30 are `<risk>LOCAL`. By 1.0.0_SA_CTO's ruling
(msg 100990) the COO's close run grades their AC4s, and none is graded here. This document dispositions the ARMED rows
only. It exists because only the CVO's lane writes adjudications/ and remediations/.

**Tally: 15 of 15 items dispositioned.**
- 13 GRADUATED: 12 remedied and disarmed, 1 left OPEN (S7).
- 2 DISMISSED_WITH_REASON (S9 and W9-S4, carried by S7).
- The remediation rows are in REMEDIATION_v2.md.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S16",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S3"
    ],
    "one_line": "S3 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "Round-2 drain hygiene: `bun run typecheck` (tsc -b --noEmit) reads rc=2 on the merged portal candidate dsgn-irptv1-r2 @1c7400cc -- ONE error, TS2339 in the PRODUCT file tabs/holdings/HoldingsTreemap.tsx (195,40) `Property 'payload' does not exist on type 'TooltipProps<number, string>'`, IV-e-5's own file; the same read is red on the worker's branch tip fb4fc3b2 and was green at a3616feb (after IV-e-3 + IV-e-1). Every suite passes (17 of 17 across 13 dsgn-irptv1 files, 0 fail) because bun test does not typecheck.",
    "world_is": "Round-2 merged candidate typecheck red: one TS2339 in tabs/holdings/HoldingsTreemap.tsx (195,40), IV-e-5's own file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S3",
        "portal DEV CI run 36200546242 'CI - Build & Validate' at 1e821a6e: step 'Type Check (TypeScript)' success (gh run view, read by 3.0.0_SA_CVO)",
        "portal PROD 36a37afc merges DEV (merge DEV->PROD round 4); org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab (tsc 0 errors at 4d6c8aaa and 36a37afc)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S17",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S5"
    ],
    "one_line": "S5 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "Issuer's defect in IV-e-2's IVE2-AC2: the `<expect>` `FIXTURES-MATCH: matched` is UNANCHORED, so it matches the partial line `FIXTURES-MATCH: matched 2 of 5` that the criterion's own prose calls a REFUSAL -- worker 0.9.0_WK_DSGN_IRPTV1~5 graded PASS on 2 of 5 and flipped `complete`, and proof-of-spec-check read the instance VALID. The one-query census over every round-2 proof row (6 instances, 24 rows, CLOUD + the undrained wk-DSGN_IRPTV1-5) finds this ONE row; no other PASS carries a partial count.",
    "world_is": "IVE2-AC2's <expect> 'FIXTURES-MATCH: matched' was unanchored and admitted the partial line 'matched 2 of 5', which the criterion's own prose calls a refusal.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S5",
        "org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-2.style-and-instrument.md:31 at HEAD: <expect>DRIVER-FIXTURES-MATCH: matched 5 of 5</expect> (anchored)",
        "workspace 49dc5d9216 (the issuer's amendment); 1.0.0_SA_CTO msg 100632 accepted it and made anchored count expects the project rule"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S18",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S6"
    ],
    "one_line": "S6 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "Grader's run of IVE2-AC2 on the merged round-2 candidate 04952bd2 (1.0.0_SA_CTO 100625): the pinned driver read `DRIVER-FIXTURES-MATCH: matched 5 of 5` against a plain dev server on 5192; its PNG (deliverables/2.0.0_SA_COO~D/iv-e-2.grader-run.04952bd2.png) shows two defects no static-markup criterion could see: the Securities map (IV-e-5 HoldingsTreemap) draws SOLID BLACK tiles labelled only 'not supplied', and the bare 9-character identifier `037833100` renders as a security NAME in the allocation bars, hero tiles, legend and Securities table.",
    "world_is": "The grader's run PNG of the round-2 candidate showed solid black Securities-map tiles labelled 'not supplied', and an id printed as a Holdings name.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S6",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_FAST_PIN_GRADES_20260924.md@ddb0339061 pins 1 (92d16efc, tiles coloured) and 13 (86561aef, served asset class) PASS",
        "portal 2cac0a83 (IV-e-25, model colour by served model_code) and df5e41b5 (IV-e-18, ids never print): ancestors of origin DEV 1e821a6e and PROD 36a37afc",
        "deliverables/2.0.0_SA_COO~D/round3-close.run.txt@98c72cdfb0: accIds 0 on every body"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S19",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S7"
    ],
    "one_line": "S7 GRADUATED: OPEN for round 5, still armed.",
    "disposition": "GRADUATED",
    "spec_asserts": "Round 2 LANDED ON PORTAL DEV at a3f4c860 on Andrew's word ('merge this in to the main DEV branch, you dont need to be working on a feature tree for this work'), ahead of the round's L8/L9: 7 of 8 cells (IV-e-7 not cut), DEV's CI steps pass on the landing (lint 0 errors after a 2-line prefer-const fix 49eadc0c in IV-e-5's test file, provenance guard OK, typecheck 0, build OK), but the InvestorReporting unit suite carries 8 NEW failures versus origin/DEV (95 -> 103 of 656 -> 671 tests), all in legacy fe-s suites the round-2 cells changed the ground under.",
    "world_is": "The InvestorReporting unit suite carries legacy failures that assert behaviour the PRD retired, mixed with regressions. S9 fixed 4 of the first 8. The legacy set now reads 80 fail at 4d6c8aaa against 81 at the round-4 baseline, with no new failure; the per-test ruling on the remainder is not done.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S7",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab (80 fail / 787 pass at 4d6c8aaa; baseline 757 / 81)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S9 (4 of 8 fixed: c1d7aefe, 9902bf25)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W9-S4 (the same set seen by a worker sweep, 86 at its worktree)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S20",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S9"
    ],
    "one_line": "S9 DISMISSED_WITH_REASON: carried by S7.",
    "spec_asserts": "S7 progress (S7 stays ARMED): 4 of the 8 legacy failures fixed on portal DEV as regressions -- c1d7aefe (the returns heatmap printed '--' for an unsupported return, against render/values.tsx's one rule; its benchmark row lost data-block=\"benchmarks\") and 9902bf25 (consumed.ts regenerated: the client's route table had outgrown it, so the round-2 smoke fixture read UNCLASSIFIED; `ok` moved out of the envelope pin on 2.0.0_SA_COO~P 100861). The other 4 ask for behaviour the PRD retired and are routed to 1.0.0_SA_CTO for a ruling.",
    "world_is": "S7's own progress row. It names the same legacy set, and its disarm clause is S7's; S7's remediation row carries it.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S7's own progress row. It names the same legacy set, and its disarm clause is S7's; S7's remediation row carries it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S9",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S7",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S21",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W9-S4"
    ],
    "one_line": "W9-S4 DISMISSED_WITH_REASON: carried by S7.",
    "spec_asserts": "Running the whole InvestorReporting portal test tree (a sweep beyond this cell's own criteria, taken to confirm no regression) shows 86 failing tests / 2 errors across files this worker never touched (e.g. src/api/endpoints/investor-reporting.ts's LiveClient route-building, FIELD_MAP coverage, F14/F19/F25/F26/F30/F31 etc.) -- pre-existing at this worktree's HEAD, not caused by TO-IV-e-17's edits.",
    "world_is": "The same legacy suite set as S7, seen by a worker's full-tree sweep (86 at its worktree, none caused by IV-e-17). S7's remediation row carries it.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The same legacy suite set as S7, seen by a worker's full-tree sweep (86 at its worktree, none caused by IV-e-17). S7's remediation row carries it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W9-S4",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S7",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S22",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W10-S1"
    ],
    "one_line": "W10-S1 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "IV-e-16's own IVE16-AC1 ('zero per-tab Export buttons render on any tab') cannot be fully met within this cell's <paths> grant: tabs/analysis/AnalysisTab.tsx still carries a permanently-disabled data-slot=\"export-button\" control, and AnalysisTab.tsx is named nowhere in IV-e-16's decomp `writes` column or this order's <paths> -- this worker's own IVE16-AC1 test checks the criterion as written, finds this control, and reports VERDICT: PAGE-EXPORT-FAIL on the analysis arm rather than narrowing the check to pass.",
    "world_is": "IVE16-AC1 (no per-tab Export) could not be met inside IV-e-16's grant: tabs/analysis/AnalysisTab.tsx kept a permanently disabled data-slot=\"export-button\".",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W10-S1",
        "portal origin DEV 1e821a6e src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx: 0 occurrences of 'export-button' (read)",
        "portal d4d50a3d (IV-e-22), ancestor of DEV and PROD; round3-close.run.txt@98c72cdfb0 perTabExport:0"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S23",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W7-S1"
    ],
    "one_line": "W7-S1 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "TO-IV-e-9's mandated adoption (ClientSearch.tsx renders SearchSelect in place of the Catalyst Combobox) necessarily breaks IVE8-AC2's arm 2 wiring check ('Combobox onChange={handleSelect} still wired') from an earlier cell's already-graded test -- the semantic selection path (handleSelect's own body, byte-identical) is unchanged, only the literal onChange={handleSelect} text is gone because SearchSelect's onChange hands back an Option, not a SearchOptionRow.",
    "world_is": "IV-e-9's SearchSelect adoption removed the literal onChange={handleSelect} that IVE8-AC2 arm 2 checked; the selection path itself was unchanged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W7-S1",
        "portal origin DEV 1e821a6e src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-8.selection-path.test.ts:55,72 (arm 2 = handleSelect byte-identical; read)",
        "portal 89a6d4f4 (drain repair), ancestor of DEV and PROD"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S24",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W7-S2"
    ],
    "one_line": "W7-S2 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "TO-IV-e-10's Holdings mount (AccountFilter, above the drill) cannot receive a live Narrowing/SearchOptionRow/onNarrow -- that triple lives in index.tsx, threaded today only as far as the header, and TabShell.tsx/index.tsx (the only files that could carry it into HoldingsTab.tsx) are outside this order's <paths> grant.",
    "world_is": "The Holdings AccountFilter could not receive the live narrowing: the selection triple lived in index.tsx, outside IV-e-10's grant.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W7-S2",
        "portal 8cd2dab2 (round-3 drain hookups: the header's accepted selection reaches the tabs), ancestor of DEV and PROD",
        "deliverables/2.0.0_SA_COO~D/round3-close.04-holdings.png@98c72cdfb0 ('Account: All accounts' beside the view; probe accountFilter:1)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S25",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W9-S1"
    ],
    "one_line": "W9-S1 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "TO-IV-e-14's cell (c) asks GenerateComposer to list 'the included accounts by name + masked tail' for a chosen client, but that data source (scope.permittedAccountIds) is the SAME one an Andrew-direct already refused a per-account list on ('it printed every permitted account id (1,000+)'); this worker named a threshold (ACCOUNTS_NAMED_LIST_CAP=25) rather than reproduce the refused pattern or silently drop the ask.",
    "world_is": "GenerateComposer's per-account list was sourced from scope.permittedAccountIds, the same 1,000+ list an Andrew-direct refused.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W9-S1",
        "portal 8cd2dab2, ancestor of DEV and PROD",
        "deliverables/2.0.0_SA_COO~D/round3-close.05-analysis.png@98c72cdfb0 ('Accounts (2 included)': Trust Account ****4471, Family IRA ****9020)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S26",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W11-S1"
    ],
    "one_line": "W11-S1 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "The cell text names the firm-attribution chip among the facts to move to disclosure, but `FirmAttribution.tsx`'s rendered name text is the load-bearing assertion of an out-of-grant pinned test (`__tests__/fe-s-10/parity.test.ts`: `globalMarkup.includes('49 Financial<')`) -- this worker left `FirmAttribution.tsx` unchanged rather than break it, and did not move that one chip.",
    "world_is": "The firm chip's name text was the pinned assertion of an out-of-grant test (__tests__/fe-s-10/parity.test.ts), so IV-e-18 could not move the chip.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W11-S1",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_IRPT_20260925.md@75156f2b18:80 (R6; msg 100948)",
        "portal 29550954 (round-4 chain 3, IV-e-23), ancestor of DEV and PROD; origin DEV parity.test.ts:69 compares globalName (read)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S27",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W11-S2"
    ],
    "one_line": "W11-S2 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "Implementing amendment N2 as written (ReturnsHeatmap.tsx prints \"not supplied\" instead of UNAVAILABLE) necessarily breaks an out-of-grant pinned test, `__tests__/fe-s-5/states.test.ts`, which asserts the literal string `>UNAVAILABLE<` for the exact same cell this order names.",
    "world_is": "Printing 'not supplied' instead of UNAVAILABLE broke an out-of-grant pinned test (__tests__/fe-s-5/states.test.ts) asserting '>UNAVAILABLE<'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W11-S2",
        "RULINGS_IRPT_20260925.md@75156f2b18:80 (R6)",
        "portal 2cac0a83 (IV-e-25), ancestor of DEV and PROD; origin DEV fe-s-5/states.test.ts: 0 occurrences of '>UNAVAILABLE<' (read)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S28",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W11-S3"
    ],
    "one_line": "W11-S3 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "IV-e-19's own in-grant edit to HoldingsTab.tsx (progressive disclosure, DESIGN.md C14) necessarily grows the diff `__tests__/dsgn-irptv1/iv-e-10.ruled-touch.test.ts` (IVE10-AC3, an earlier cell's own pinned criterion) measures against a fixed base commit -- but that check was ALREADY RED (12 added/1 removed against its own <=2-added/0-removed bound) before this task order touched anything, from IV-e-18's prior edit to the same file.",
    "world_is": "iv-e-10.ruled-touch.test.ts measured a fixed base and went red once later ruled cells (IV-e-18, IV-e-19) edited the same file.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W11-S3",
        "portal ecfd327a (round-3 drain repair: the bound now covers IV-e-10's own commit a65074e7), ancestor of DEV and PROD",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S14 (W11-S3 recorded disarmed at the drain)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S29",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W11-S4"
    ],
    "one_line": "W11-S4 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "IVE20-AC2's own scrollbar census, run against the LIVE main portal checkout on :5174 (the worker face's own instructed instrument, pre-merge), found a real stray horizontal scrollbar in production-adjacent code TODAY: DrillTree.tsx's donut legend (`renderDrillLegend`, IV-e-13 round 2) sets `whitespace-nowrap` on each entry inside a `flex-wrap` row, so a single long model name (e.g. a canonical duration-ladder name) wider than the legend's own box at 390px cannot shrink or wrap and forces `scrollWidth(316) > clientWidth(250)` on `[data-slot=holdings-drill-legend]` -- confirmed a genuine `overfl",
    "world_is": "DrillTree's legend <li> carried whitespace-nowrap inside a flex-wrap row, so a long model name drew a stray horizontal scrollbar.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W11-S4",
        "portal origin DEV 1e821a6e src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:163 (li class 'inline-flex max-w-full items-center gap-1.5 break-words'; read)",
        "portal c75f68a3 (IV-e-20), ancestor of DEV and PROD; S14 records IVE20-AC2 PASS after the join merge"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S30",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-26T05:13:05Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W19-S1"
    ],
    "one_line": "W19-S1 GRADUATED: remedied inside the rounds and disarmed.",
    "disposition": "GRADUATED",
    "spec_asserts": "ConsolidatedOverviewPanel now accepts an optional `tenantLayout` prop that resolves cash/other colour through the layout's colorPalette (IVE29-b), but none of its three real PROD call chains (CanonicalBookView.tsx and its callers AdvisorBookView.tsx / ClientsTab.tsx / AdvisorBookClientDetail.tsx) pass it -- all outside this TO's <paths> grant -- so the client-drill donut/legend will keep rendering `cash`/`other` via the global MIX_PIE fallback (amber500 / gray500) on PROD until a follow-on TO threads the prop through those three files.",
    "world_is": "ConsolidatedOverviewPanel gained a tenantLayout prop, but none of its PROD call chains passed it, so the client-drill cash/other colours stayed off the firm palette.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W19-S1",
        "portal origin DEV CanonicalBookView.tsx:61,99,111 (tenantLayout threaded into the panel; read)",
        "portal 4d6c8aaa (IV-e-30 merge), ancestor of DEV and PROD; org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab (IVE30-AC1/AC2 PASS)"
      ]
    }
  }
]
```
