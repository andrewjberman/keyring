# DSGN_IRPTV1 -- remediation v5 (the FAST interval backlog)

<sweep_watermark>2026-10-02T03:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO. Round: v5. Fabric: laptop. Recorded: 2026-10-02T03:10:00Z.

Adjudication: `ADJUDICATION_v7.md` (C-S61 to C-S68, same commit).

**13 rows.** REMEDIATED, DISARMED and closed, each read at portal origin DEV 24646bca: S28, S29, S30, W36-S3, W38-S4. DISARMED with remediation OPEN: S27 (no page export observed at READY yet). OPEN and ARMED: W39-S2 (1.0.0_SA_CTO: the request list labels every request with the selected client). OPEN and INERT: S34, S37, S38, W40-S1 (2.0.0_SA_COO~D), S40 (2.0.0_SA_COO~Y), S12 (1.0.0_SA_CTO). No row carries `route` or `loop_target`.

```json
[
  {
    "id": "DSGN_IRPTV1-S27",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The export receipt read answered a pending export as UNAVAILABLE/NOT_READY, and the page went silently idle after one read. Two parts: the seam (a pending receipt must read as pending) and the page (a refused poll must be named).",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S27",
      "24646bca:src/pages/InvestorReporting/export/submit.ts:277-300: pollExportReceipt keeps polling through a data-less read within its bound (e5e96606, 2026-09-29T04:56:38Z, in DEV's history); :327-341 describeExportReceiptFailure names a refused read by its publicReasonCode (c34692a2, TO-IV-e-78 complete)",
      "w21-part-p-walk-20260929.md@bc3a514122 K8 arm 2: the served receipt read now answers RUNNING / EXPORT_BUILDING with no data (the seam's backend half), the shape the fix polls through",
      "No record read by this seat shows an export reaching READY or FAILED on the page: K8 arms 3-4 were not observable at W21"
    ],
    "remedy": "Both parts are in the code. Closes on ONE page walk where an export reaches READY with a download offered, or FAILED with its reason named on the panel.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-29T04:56:38Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-S28",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The live irpt-status answered HTTP 500 for one READY request (REQ-67e12718) on every page read, and the opened-request read dropped selected_tenant.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S28",
      "w21-part-p-walk-20260929.md@bc3a514122 K10 (2026-09-29 03:47Z-04:08Z): REQ-67e12718 opened with GET /analysis/requests 200, /sections 200 and /status 200 READY",
      "CloudWatch Logs /aws/lambda/irpt-status, filter-log-events over 4 days to 2026-10-02 03:0xZ (this seat): 646 START lines; 0 lines matching Traceback or 'Internal Server Error' or statusCode 500; 8 ERROR/Exception lines, each a handled irpt_internal refusal; 0 lines name REQ-67e12718 (the request was not read in the window)",
      "24646bca:src/api/endpoints/investor-reporting.ts:1060-1073 and :1169: the opened request, report and status reads send selected_tenant (TO-IV-e-66 a5107226, complete)"
    ],
    "remedy": "Remedied on both halves: the 500 did not recur on the W21 walk and no unhandled 500 appears in four days of the function's log; the tenant omission is fixed in the code.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-29T04:08:00Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-S29",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "UIC-09 was closed as 'already holds' while the page printed 'No source age yet' on loading and refused panels.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S29",
      "24646bca:src/pages/InvestorReporting/state/status.ts:506-512: sourceAgeWordsForPanel returns null for a no-source-age-yet state; StatusPanel.tsx:73 renders that value",
      "portal 528acdcd (FAST item 2, 2026-09-28T19:31:39Z) is an ancestor of 24646bca; control: 24646bca is not an ancestor of 528acdcd",
      "24646bca:__tests__/dsgn-irptv1/iv-e-69.performance-finished.test.tsx:325-346: the UIC-09 arm re-goldened to 'no words before a source exists', with an answered-state control"
    ],
    "remedy": "Executed under FAST (item 2); graded PASS on its source-age half by this seat on 2026-09-28 (row S34's notes).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-28T19:31:39Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-S30",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Holdings accounts pie drew nothing for an eleven-account client; recharts draws nothing once the signed sum is not above zero, and a negative account made it so.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S30",
      "24646bca:src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:134-139: partitionPieRows draws amount > 0 only and lists negatives apart",
      "portal a47d3a75 (FAST item 1, 2026-09-28T18:33:12Z) is an ancestor of 24646bca",
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S31: the owner's disarm record (real run on the cowdin client: 10 positive wedges, the negative account as a labelled line)"
    ],
    "remedy": "Executed under FAST (item 1): a negative account is a labelled line, never a wedge, so the drawn feed always sums above zero.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-28T18:33:12Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W36-S3",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TO-IV-e-73 made FirmAttribution render nothing by default, which flipped five pinned tests outside its grant that asserted the old visible chip.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W36-S3",
      "portal 6521cb09 (TO-IV-e-79, 2026-09-28T13:48:33Z, merged ac9e628d) re-goldens iv-e-23.firm-chip, iv-e-38.header-identity, iv-e-56.firm-display and fe-s-10/parity; iv-e-23.parity-kept was not changed",
      "bun test at the main portal checkout, whose bytes for these files and FirmAttribution.tsx equal 24646bca (git diff --stat empty), this seat 03:0xZ: the five files plus the two W38-S4 files, 13 pass, 0 fail across 7 files"
    ],
    "remedy": "Executed by TO-IV-e-79 (complete): the five assertions now read the show-gated default.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-28T14:30:29Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W38-S4",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IV-e-70 moved ASSET_CLASS.fixedIncome to green700, which broke two ratified AdvisorIntelligence tests (commodities green900 at dE00 14.0 < 20).",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W38-S4",
      "24646bca:src/lib/chartColors.ts:198 fixedIncome PALETTE.green500 and :226 commodities PALETTE.yellow500, after 3e2233de (Andrew-direct 2026-09-29, colours back on standard hues); both iv-e-49.commodities-distance and iv-e-51.commodities-chromatic were last changed in 3e2233de",
      "bun test (this seat, 03:0xZ, bytes equal 24646bca): both files pass within the 13 of 13 run; the run prints INFO dE00(commodities #eab308, Short Term #f59e0b) = 9.8943 < 20 'rule superseded, not a failure'"
    ],
    "remedy": "Overtaken by Andrew's standard-hues direction (3e2233de); the two tests were re-goldened in the same commit and pass.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-29T18:06:36Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W39-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The served owned-request wire carries no client field, and the history list is owner-scoped, not client-scoped. The page labels every listed request with the header's selected client, so the same requests show under any selected client, each with that client's name.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W39-S2",
      "docs/contracts/investor-reporting/v1/OwnedAnalysisRequest.schema.json at HEAD (last 8c4398e32a, E7): 11 property paths, none naming a client, account, selection or name",
      "24646bca:src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx:237 clientName = header?.row?.displayName, printed at :365; investor-reporting.ts:1045-1049 listOwnedAnalysisRequests sends no client filter",
      "org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md (2aed13d096) Parked: 'The Analysis request list shows the same requests under any selected client, each labelled with that client's name (REAL_RUNS_20261001.md section 2): owner IRPT_BCKEND'"
    ],
    "remedy": "1.0.0_SA_CTO places the contract call: a served client field on the owned request, or a client-scoped history route (IRPT_BCKEND). Then 2.0.0_SA_COO~D prints the served client. Disarmed when a walk shows each request under its own client only.",
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
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "DSGN_IRPTV1-S12",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "/dispatch Step 5 says hand a slot's next order by continuing the same worker subagent; in the session that filed the row a completed worker could not be continued ('No transcript found'), so each handoff was a fresh worker on the same worktree.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S12",
      ".claude/skills/dispatch/SKILL.md:435-436 at HEAD still reads 'Hand the next task order by CONTINUING the same subagent ... No respawn, no cold start'; the harness behaviour itself is not re-measured here"
    ],
    "remedy": "The /dispatch skill's owner re-measures continuation of a completed worker in the current harness and either keeps Step 5 or adds the respawn-on-the-same-worktree path. Outside this project's paths; it moves to ESTATE_GOVERNANCE at this project's close if still open.",
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
    "id": "DSGN_IRPTV1-S34",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A raw public reason code reaches the Analysis face: the stage line appends '(CODE)' on every state that carries one, and the Holdings-snapshot line on a refusal does the same. The served envelope carries the codes on every loading state (S35).",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S34",
      "24646bca:src/pages/InvestorReporting/tabs/analysis/StageDisplay.tsx:62: {envelope.publicReasonCode ? ' (' + code + ')' : null}",
      "24646bca:src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx:469: the snapshot line appends the code",
      "24646bca:OwnedRequestHistory.tsx:93: the history row now words the code (the third surface of S36 is fixed)"
    ],
    "remedy": "One page change covers both remaining surfaces: the code moves behind the Technical details control, as FAST item 14 did for Performance under CTO ruling 102453.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "DSGN_IRPTV1-S37",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A pick in the Holdings tab's first dropdown was walk-observed to clear the client selection and return the page to Performance with sample placeholders; which pick, and whether the page or the walker causes it, is not isolated.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S37",
      "comp-find over the DSGN_IRPTV1 deliverables, STATUS.md and this seat's FAST grade file (this seat, 03:0xZ): 5 hits, all in DSGN_IRPTV1_FAST_PIN_GRADES_20260928.md, the last (:223) still listing it as a walk constraint; no record closes or reproduces it"
    ],
    "remedy": "One manual pick of each option of that select with a client selected, on the current DEV build; a reset found is a page fix, none found closes the row.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "DSGN_IRPTV1-S38",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "After a Comparison or Multi-Comp card is picked, the composer's Variant line reads the label for the COUNT of chosen comparisons, so it says 'Overview (0 comparisons)' until comparisons are chosen, against the picked card.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S38",
      "24646bca:src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx:386-390: the Variant line renders variantLabelForCount(count); the card pick is held in variantChoice (:331) and not read there"
    ],
    "remedy": "The Variant line reads the picked card when one is picked (or states that comparisons are still to be chosen). A design call if the count rule is intended; owner to confirm.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "DSGN_IRPTV1-S40",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The workspace contract carries GET /analysis/comparisons and its ComparisonCatalogue schema; the portal carries no operation entry, wire type or fixture for it, so 13 IR tests fail beyond the known five.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S40",
      "git grep -c 'analysis/comparisons|ComparisonCatalogue' 24646bca -- src/ (this seat, 03:0xZ): 0 files",
      "24 schemas in docs/contracts/investor-reporting/v1 against 23 entries in the portal generator's WIRE_CONTRACTS; the missing one is ComparisonCatalogue",
      "org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md Parked: owner 2.0.0_SA_COO~Y; un-parks when ~Y lands the portal half or the CTO re-homes it"
    ],
    "remedy": "The portal half of the comparison-catalogue cell (IRPT_BCKEND ~Y): the operation entry, the generated wire type and a fixture; the 13 tests then pass.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "DSGN_IRPTV1-W40-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-IV-e-63 named two Performance exceptions; only the first (the answer ends before the page date) is built. The second (the series starts after the requested start) was left out because the reference fixtures carry tail-only daily samples.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W40-S1",
      "git grep -i 'series starts|starts late' 24646bca -- src/pages/InvestorReporting (non-test): 0 hits"
    ],
    "remedy": "Confirm dailyCumulative's served population (full series or tail sample) from a served report; if full, build the second exception with its control.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v5"
    },
    "closed": false
  }
]
```
