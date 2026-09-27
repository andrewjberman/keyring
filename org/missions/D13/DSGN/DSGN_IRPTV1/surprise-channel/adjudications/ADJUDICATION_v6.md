# DSGN_IRPTV1 -- adjudication v6: round 8 (judgment grades + the ARMED rows)

Author: 3.0.0_SA_CVO. Document v6. Fabric: laptop. Recorded: 2026-09-27T21:45:04Z.

**Input.** The COO's round-8 packet `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round8-L8-packet.md@eaebc81ade` and the window-18 walk `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade` on local portal DEV 3b98939b, with its 11 screenshots viewed on this device.
Where w18 did not reach (a COT strategy drill; the Analysis request history), the CRO's evening walks of the SAME build were read by
screenshot (`docs/briefs/irpt-ui-cleanup-brief-20260927.md@97cb8bf734`, shots 011 and 126). The ARMED-row checks ran against 3b98939b and origin/CLOUD: ancestry, file contents, the task-order
states at HEAD, the proof-of-spec checker, and the CTO's round-7 analysis. A read-only subagent ran most of them; this seat re-read the
decisive ones (IV-e-55's determinism record, the ruling's lines, S19's tree count, index.tsx:270, the naming gate's last commit).

## Judgment grades (C-S54)

Tally over the rows: 14 PASS, 7 FAIL, 1 NOT_EVALUATED. Criteria: IVE57-AC2, IVE58-AC2 and IVE61-AC2 PASS; IVE56, 59, 60, 62 and 63-AC2 FAIL.
The CRO's re-grade on the same build agrees on every row both graded (UIR-30, 32, 34, 37, 45 and 49 not met).

| row | verdict | evidence |
|---|---|---|
| UIR-04 | PASS | w18a: options read 'Cottonwood' / '49 Financial', one layout on every row |
| UIR-13 | PASS | w18b: '49 Financial (Client)'; w18f-cot: 'Cottonwood (Client)' |
| UIR-30 | FAIL | w18b/w18c/w18e: the display name is right, but the firm shows twice: the identity line '49 Financial (Client)' and the '49 Financial' chip at the top right of each tab (w18f-cot: 'Cottonwood' likewise). The chip is the object UIR-30 was filed on |
| UIR-11 | PASS | w18a: the open search list sits over an empty page; no SAMPLE content renders behind it (record: first option covered false) |
| UIR-06 | PASS | amendment row: record + w18a: no client-like figures with no client chosen |
| UIR-20 | PASS | amendment row: w18b Export enabled on Performance with an answer-bearing report; CRO walk: grey on Analysis with no report |
| UIR-15 | PASS | w18b + record: each entry shows the value with YTD beside it ('****9079 / IRA -- $153,836.54 -- YTD 5.93%'); graded on the page half only -- the identical labels are 2.0.0_SA_COO~M's (UIR-26, CTO 101845 E3) |
| UIR-25 | PASS | w18c: three account slices in three fills (slate, taupe, grey); w18f-cot: two in two. UIC-11 (4+ accounts near-identical) is the CRO's round-9 finding |
| UIR-46 | PASS | as UIR-25 |
| UIR-37 | FAIL | w18d/w18e: the Opal Long Term model draws #3b82f6 (Allocation bars, drill pie) and Equity draws #2563eb on the securities map -- both blue on one page; CRO shot 011 (COT): Opal Conservative Growth blue, Opal Ultra Short-Term Income orange, Opal Fixed Income grey. TO-IV-e-59's build confined the fix to a new ACCOUNT palette and made modelPortfolioColors.ts and chartColors.ts read-only, so this collision was outside the cut |
| UIR-31 | PASS | w18e: drilling the first account sets the Account focus to '****9079 / IRA' and Unique accounts to 1; CRO shot 011 (COT) agrees |
| UIR-32 | FAIL | the breadcrumb now names the account (w18e 'All holdings ****9079 / IRA / Models'), but CRO shot 011 (COT, same build) reads 'All holdings ****9237 / BROKERAGE / Rebalancer strategy: Anna *9238' -- a different tail, and one asterisk against four; w18 did not drill a strategy |
| UIR-33 | PASS | w18c: '% of the client' at the client level; w18e: '% of this account' in the drill, and the pie labels equal the table (41.86 / 31.91 / 26.23); the build landed in TO-IV-e-61 Amendment 2. The category card's '100% of total' sits under its own 'Total Assets' figure |
| UIR-34 | FAIL | w18e: the ALL CATEGORIES card still draws a one-slice pie (Models, 100%); CRO shot 011: the same, grey, for 'Rebalancer strategy'. The drill tree itself now skips the one-child level |
| UIR-36 | PASS | as UIR-33 |
| UIR-47 | PASS | as UIR-33 |
| UIR-49 | FAIL | its UIR-31 half holds (the filter follows the drill); its UIR-32 half fails as UIR-32 |
| UIR-41 | PASS | w18d: chips sit under each account label, one per model, each reading 'Model: <name>'; the three group labels are identical (UIR-26, data) |
| UIW-0927-07 | PASS | amendment row: w18d: the grouped tile reads 'Smaller holdings' in #94a3b8; 'Other' is #9333ea |
| S18 (IV-e-62) | FAIL | w18: the history did not render within 15 s (not reached). CRO deep-walk shot 126 (same build, COT client): six jobs from other sessions are listed beside 'No job submitted from this browser yet', but window 15's READY job REQ-67e12718 reads 'Status unavailable' and four read 'Unavailable -- ANALYSIS_REQUIRES_ATTENTION', a code where the cell asked for words. IV-e-66 (c8906a62, an ancestor of 3b98939b) did not cure S25 on the page |
| UIR-45 | FAIL | w18b: the Performance header reads 'Requested 2026-01-01 to 2026-09-22 / Answered 2026-01-02 to 2026-09-22', and the chart axis and daily table are ISO; w18f-cot: 'DIRECTORY AS OF 2026-09-22'; the card and source lines read 'September 22nd, 2026, 5:00p ET'. w18d: the source line reads 'holdings_snapshot.build_schwab_smartx_meshed', a function name (UIC-14) |
| R10 label | NOT_EVALUATED | every walked answer ends ON the page date (2026-09-22), the control case: no label shows and none is due. No answer ending before the page date was walked |

**For the CTO's analysis:**
- **UIR-37 was cut out of its own cell.** TO-IV-e-59 fixed the account palette but made `modelPortfolioColors.ts` and `chartColors.ts`
  read-only, so the model-versus-asset-class collision the row names could not move. Round 9 needs a cell that may change one of the
  two palettes, or a PRD line that says which one yields.
- **UIR-34.** The drill now skips a one-child level, but the ALL CATEGORIES card still draws a one-slice pie (the same finding as round 7).
- **UIR-30.** The name is right; the firm chip above each tab repeats the identity line.
- **S25 is not cured on the page.** IV-e-66 (c8906a62, an ancestor of 3b98939b) threads the tenant, yet window 15's READY job still reads
  'Status unavailable' (CRO shot 126). The row is INERT and UNDER_INVESTIGATION.

## ARMED rows (C-S55..C-S60)

The census of BLOCKING or ARMED items not closed gives 12, the packet's 12. After this document:
- **Closed in place in REMEDIATION_v3:** W29-S8 (IV-e-54: 9c71f9a4, merged 3e54ec31), W29-S9 (the CRLF fix b67fdb22 with its mutant
  control, merged c66f980c), and S19 (its own disarm test: 0 files in the three .shots folders on origin/CLOUD 0f4b3f876f; control 20 and 8
  at 4f632208c5). The pushed history still holds the 28 screenshots (4f632208c5 is an ancestor of origin/CLOUD): the purge is Andrew's.
- **Remedied, REMEDIATION_v4:** W36-S2 (a5107226) and W38-S1 (71896c93).
- **OPEN, REMEDIATION_v4:** W34-S1, W35-S2 (2.0.0_SA_COO~D, round 9) and W35-S1 (1.0.0_SA_CTO: an R20 entry, or a naming-gate
  JS/TS builder exemption by 0.0.0_AB_MSTR).
- **Not closed on IV-e-55 (C-S60):** S7, W21-S2, W23-S1 and W29-S10. The ruling says "No retries"; IV-e-55's first 3-run sample failed
  (fe-s-45, 1 of 3) and the recorded pass is the second. They stay OPEN in place and close together when W34-S1 is fixed and one pinned
  3-run sample on the drained tree meets the bar.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S54",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T21:45:04Z",
    "one_line": "Round-8 L9 judgment grades on the window-18 walk: 8 criteria -- PASS IVE57-AC2, IVE58-AC2, IVE61-AC2; FAIL IVE56-AC2 (UIR-30), IVE59-AC2 (UIR-37), IVE60-AC2 (UIR-32/34/49), IVE62-AC2 (the READY job reads 'Status unavailable'), IVE63-AC2 (UIR-45). Per-row verdicts in the document header.",
    "class": "OBSERVATION",
    "spec_asserts": "IVE56-AC2..IVE63-AC2 are graded at L9 by 3.0.0_SA_CVO on the issuer's round-8 walk, each row of the cell read on the running page at 1440 px.",
    "world_is": "The window-18 walk of local portal DEV 3b98939b (20:52Z-21:02Z, byte-proof clean) with its row table and 11 screenshots w18*, each viewed on this device; where w18 did not reach (a COT strategy drill, the Analysis history) the CRO's walks of the same build were read, screenshot by screenshot.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade",
        ".runtmp/walk/shots/w18a..w18f, w18-k7, w18-k8a-modal (untracked, viewed; colours sampled by pixel)",
        "docs/briefs/irpt-ui-cleanup-brief-20260927.md@97cb8bf734 with tmp/ui-walk/20260927T200826Z/shots and tmp/ui-walk/20260927T203155Z/shots (the CRO's walks of the same build, local DEV 3b98939b; gitignored, viewed): shots 011 and 126 cited",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round8-L8-packet.md@eaebc81ade"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "IVE56-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~35/DSGN_IRPTV1.TO-IV-e-56.firm-display-names.proof_of_spec.json@865fa31a8a",
        "verdict": "FAIL",
        "reason": "Bar: each row of the cell read on the running page at 1440 px (round-8 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade, shots w18a-w18f; the CRO's same-build walks where w18 did not reach). 2 of 3 rows PASS; UIR-30 FAIL. UIR-30 FAIL: w18b/w18c/w18e: the display name is right, but the firm shows twice: the identity line '49 Financial (Client)' and the '49 Financial' chip at the top right of each tab (w18f-cot: 'Cottonwood' likewise). The chip is the object UIR-30 was filed on"
      },
      {
        "criterion": "IVE57-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~35/DSGN_IRPTV1.TO-IV-e-57.search-covers-page.proof_of_spec.json@b52c652deb",
        "verdict": "PASS",
        "reason": "Bar: each row of the cell read on the running page at 1440 px (round-8 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade, shots w18a-w18f; the CRO's same-build walks where w18 did not reach). 3 of 3 rows PASS."
      },
      {
        "criterion": "IVE58-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~36/DSGN_IRPTV1.TO-IV-e-58.picker-value-and-ytd.proof_of_spec.json@af5591d94f",
        "verdict": "PASS",
        "reason": "Bar: each row of the cell read on the running page at 1440 px (round-8 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade, shots w18a-w18f; the CRO's same-build walks where w18 did not reach). 1 of 1 rows PASS."
      },
      {
        "criterion": "IVE59-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~38/DSGN_IRPTV1.TO-IV-e-59.account-colours.proof_of_spec.json@800f639440",
        "verdict": "FAIL",
        "reason": "Bar: each row of the cell read on the running page at 1440 px (round-8 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade, shots w18a-w18f; the CRO's same-build walks where w18 did not reach). 2 of 3 rows PASS; UIR-37 FAIL. UIR-37 FAIL: w18d/w18e: the Opal Long Term model draws #3b82f6 (Allocation bars, drill pie) and Equity draws #2563eb on the securities map -- both blue on one page; CRO shot 011 (COT): Opal Conservative Growth blue, Opal Ultra Short-Term Income orange, Opal Fixed Income grey. TO-IV-e-59's build confined the fix to a new ACCOUNT palette and made modelPortfolioColors.ts and chartColors.ts read-only, so this collision was outside the cut"
      },
      {
        "criterion": "IVE60-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~38/DSGN_IRPTV1.TO-IV-e-60.drill-and-bases.proof_of_spec.json@20c06c52f4",
        "verdict": "FAIL",
        "reason": "Bar: each row of the cell read on the running page at 1440 px (round-8 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade, shots w18a-w18f; the CRO's same-build walks where w18 did not reach). 4 of 7 rows PASS; UIR-32 FAIL; UIR-34 FAIL; UIR-49 FAIL. UIR-32 FAIL: the breadcrumb now names the account (w18e 'All holdings ****9079 / IRA / Models'), but CRO shot 011 (COT, same build) reads 'All holdings ****9237 / BROKERAGE / Rebalancer strategy: Anna *9238' -- a different tail, and one asterisk against four; w18 did not drill a strategy | UIR-34 FAIL: w18e: the ALL CATEGORIES card still draws a one-slice pie (Models, 100%); CRO shot 011: the same, grey, for 'Rebalancer strategy'. The drill tree itself now skips the one-child level | UIR-49 FAIL: its UIR-31 half holds (the filter follows the drill); its UIR-32 half fails as UIR-32"
      },
      {
        "criterion": "IVE61-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~38/DSGN_IRPTV1.TO-IV-e-61.map-chips.proof_of_spec.json@c692104305",
        "verdict": "PASS",
        "reason": "Bar: each row of the cell read on the running page at 1440 px (round-8 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade, shots w18a-w18f; the CRO's same-build walks where w18 did not reach). 2 of 2 rows PASS."
      },
      {
        "criterion": "IVE62-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~39/DSGN_IRPTV1.TO-IV-e-62.request-history.proof_of_spec.json@3291c000aa",
        "verdict": "FAIL",
        "reason": "Bar: each row of the cell read on the running page at 1440 px (round-8 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade, shots w18a-w18f; the CRO's same-build walks where w18 did not reach). 0 of 1 rows PASS; S18 (IV-e-62) FAIL. S18 (IV-e-62) FAIL: w18: the history did not render within 15 s (not reached). CRO deep-walk shot 126 (same build, COT client): six jobs from other sessions are listed beside 'No job submitted from this browser yet', but window 15's READY job REQ-67e12718 reads 'Status unavailable' and four read 'Unavailable -- ANALYSIS_REQUIRES_ATTENTION', a code where the cell asked for words. IV-e-66 (c8906a62, an ancestor of 3b98939b) did not cure S25 on the page"
      },
      {
        "criterion": "IVE63-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~40/DSGN_IRPTV1.TO-IV-e-63.dates-sources-exception.proof_of_spec.json@793e2e3799",
        "verdict": "FAIL",
        "reason": "Bar: each row of the cell read on the running page at 1440 px (round-8 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w18-round8-walk-20260927.md@eaebc81ade, shots w18a-w18f; the CRO's same-build walks where w18 did not reach). 0 of 2 rows PASS; UIR-45 FAIL; R10 label NOT_EVALUATED. UIR-45 FAIL: w18b: the Performance header reads 'Requested 2026-01-01 to 2026-09-22 / Answered 2026-01-02 to 2026-09-22', and the chart axis and daily table are ISO; w18f-cot: 'DIRECTORY AS OF 2026-09-22'; the card and source lines read 'September 22nd, 2026, 5:00p ET'. w18d: the source line reads 'holdings_snapshot.build_schwab_smartx_meshed', a function name (UIC-14) | R10 label NOT_EVALUATED: every walked answer ends ON the page date (2026-09-22), the control case: no label shows and none is due. No answer ending before the page date was walked"
      }
    ]
  },
  {
    "id": "DSGN_IRPTV1-C-S55",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T21:45:04Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W34-S1"
    ],
    "spec_asserts": "S7_CLASS_TABLE.json's H classification: fe-s-45/residuals.test.ts is not observed failing, in any measurement, isolated or full-suite.",
    "one_line": "W34-S1 GRADUATED, OPEN: fe-s-45/residuals.test.ts still flakes under the pinned runner and no fix exists at local portal DEV 3b98939b. It is the one residual that holds S7, W21-S2, W23-S1 and W29-S10 open (C-S60).",
    "world_is": "IV-e-55's instance records sample A on identical code and seed as S7-DETERMINISTIC-FAIL with fe-s-45 failing 1 of 3 runs; git diff 3e54ec31 3b98939b over __tests__/fe-s-45/ and scripts/dev-live.mjs is empty, so nothing after the observation touched it.",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W34-S1",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~34/DSGN_IRPTV1.TO-IV-e-55.pinned-runner.proof_of_spec.json@597cc0cc69 controls.determinism",
        "portal: git diff 3e54ec31 3b98939b -- src/pages/InvestorReporting/__tests__/fe-s-45/ scripts/dev-live.mjs (empty)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S56",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T21:45:04Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W35-S1"
    ],
    "spec_asserts": "The task order's Build paragraph: a new header/firmDisplay.ts keyed by tenant key, with names copied from the portal's own existing partner-name maps.",
    "one_line": "W35-S1 GRADUATED, OPEN: the delivery went round the conflict (a token-free title-case transform), but the row's named disarm has not happened -- no R20 entry for a firm display-name source and no JS/TS builder exemption in the naming gate. A decision for 1.0.0_SA_CTO.",
    "world_is": "At 3b98939b header/firmDisplay.ts:36-61 splits the key and title-cases it with no firm literal (callers contracts/adapt.ts:707,724, BrowseDrawer.tsx:109, ClientSearch.tsx:140, index.tsx:323,360). .tools/naming-gate.py is unchanged since 33af10616f (2026-09-23) and js_literals() has no call-context check. A firm whose display name is not the title case of its key would render wrong, and a literal map is still refused.",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W35-S1",
        "portal 3b98939b:src/pages/InvestorReporting/header/firmDisplay.ts:36-61",
        "git log -1 -- .tools/naming-gate.py = 33af10616f"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S57",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T21:45:04Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W35-S2"
    ],
    "spec_asserts": "Amendment 1 Build text: 'Export is disabled (aria-disabled and inert) on every tab whose active report is not answer-bearing, the Analysis tab included.'",
    "one_line": "W35-S2 GRADUATED, OPEN: Export on Analysis is closed permanently (index.tsx:270), because AnalysisTab.tsx threads no answer-bearing signal; a round-9 cell granted AnalysisTab.tsx closes it.",
    "world_is": "At 3b98939b index.tsx:270 reads `const analysisExportGateOk = activeTab === 'analysis' ? false : true`, and AnalysisTab.tsx has 0 onExportTarget references: never a false enable, but Export can never enable on Analysis.",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W35-S2",
        "portal 3b98939b:src/pages/InvestorReporting/index.tsx:270",
        "portal 3b98939b:src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx (0 onExportTarget)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S58",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T21:45:04Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W36-S2"
    ],
    "spec_asserts": "F54-AC2's frozen census: exactly 2 production call sites for probeStatus(/getJobStatus( in the committed tree, both in ProspectJobStatus.tsx.",
    "one_line": "W36-S2 GRADUATED: remedied (a5107226) and disarmed -- F54-AC2's census set to the measured 4 getJobStatus lines, one of the two remedies the row names; verified at local portal DEV 3b98939b.",
    "world_is": "a5107226 changes toBe(2) to toBe(4) in fe-s-54/stated-state-wins.test.ts (definitions stay 2). git grep 'getJobStatus(' at 3b98939b outside __tests__ and the client: OwnedRequestHistory.tsx:26,33 and ProspectJobStatus.tsx:7,18 -- 4 lines, 2 of them type declarations (the census counts them as sites; not a loosening).",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W36-S2",
        "portal a5107226 (2026-09-27T18:14:08Z) is an ancestor of 3b98939b",
        "portal: git grep -n 'getJobStatus(' 3b98939b -- src"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S59",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T21:45:04Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W38-S1"
    ],
    "spec_asserts": "IV-e-61's own <paths> grant names only iv-e-60.drill-bases.test.tsx for re-goldening; Amendment 1 names no test file to re-golden at all.",
    "one_line": "W38-S1 GRADUATED: remedied (71896c93) and disarmed -- iv-e-42 and iv-e-44 re-goldened to the client wording and the Smaller-holdings colour, with new negative arms; verified at local portal DEV 3b98939b. One loosening noted for round 9.",
    "world_is": "71896c93 (2 files, +26/-9) requires the client base words and OTHER_TILE_COLOR, and adds arms that fail if '% of total' survives, if the tile uses any asset-class colour, or if it matches the legend swatch. Loosening: its UIR-47 arm builds the donut tooltip from the row's own words, so table/donut agreement holds by construction; the product mounts the real one (DrillTree.tsx:710).",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W38-S1",
        "portal 71896c93 (2026-09-27T17:38:27Z) is an ancestor of 3b98939b",
        "w18c/w18e: the drill table and pie agree on the running page"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S60",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T21:45:04Z",
    "class": "OBSERVATION",
    "spec_asserts": "1.0.0_SA_CTO's round-7 analysis (msg 101845): 'grade the S7 bar under a PINNED runner. No retries and no wider Q allowance'; 'Pass = three runs give the IDENTICAL failing set, and that set is a subset of the Q rows'; 'W21-S2, W23-S1 and S7 close on its pass'.",
    "one_line": "IV-e-55's recorded pass is its SECOND 3-run sample: sample A on identical code and seed failed the bar (fe-s-45 flaked 1 of 3). Under 1.0.0_SA_CTO's 'No retries', S7, W21-S2, W23-S1 and W29-S10 do not close on it and keep their OPEN remediation rows, tied to W34-S1.",
    "world_is": "IV-e-55's instance, controls.determinism: 'sample A ... = FAIL, 5 common Q-row failures identical across all 3 runs plus fe-s-45/residuals.test.ts flaking in 1 of 3 ...; sample B (immediately after, identical --seed, identical code) = PASS'. The pin and the two bug fixes are real (b67fdb22; W29-S9 closes on them), but the first sample did not meet the bar, and no pinned 3-run sample exists on the drained tree 3b98939b.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item; S7 (REMEDIATION_v2), W21-S2, W23-S1 and W29-S10 (REMEDIATION_v3) stay OPEN in place.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~34/DSGN_IRPTV1.TO-IV-e-55.pinned-runner.proof_of_spec.json@597cc0cc69 controls.determinism",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND7_20260927.md@36e18bf320 :34-39",
        "proof-of-spec-check.py on that instance: VALID rc=0 (the mechanical checker does not see the discarded sample)"
      ]
    }
  }
]
```
