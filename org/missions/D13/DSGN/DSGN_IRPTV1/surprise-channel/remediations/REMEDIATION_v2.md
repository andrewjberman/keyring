# DSGN_IRPTV1 -- remediation v2 (the slug after rounds 2-4)

Author: 3.0.0_SA_CVO. Round: v2. Fabric: laptop. Recorded: 2026-09-26T05:28:40Z.

Adjudication: `surprise-channel/adjudications/ADJUDICATION_v3.md` (the prior commit).

13 new rows:
- 12 REMEDIATED and DISARMED inside the rounds.
- 1 OPEN and ARMED: S7, the legacy suite set at 80 fail with no new failure. It is one batched cell for round 5.
  Its disarm is the row that quotes 1.0.0_SA_CTO's per-test ruling and the landing or retirement of each failure.

C-S12 (the round-1 derived ticker) is closed IN PLACE in REMEDIATION_v1, never re-minted here: an id is one row across
the plane. It now reads REMEDIATED and DISARMED at 2026-09-24T11:12:46Z, following the in-place close precedent
@5236fd2696. The evidence: at portal origin DEV 1e821a6e, `tabs/holdings/SecurityList.tsx:64-68` has tickerFor return
display.symbol or NOT_SUPPLIED and never split the id; the fix a380bcb5 (IV-e-1, round 2) is an ancestor of origin DEV
1e821a6e and PROD 36a37afc.

The round-4 AC4 judgment criteria are not graded here (CTO msg 100990). The five NOT_EVALUATED from round 3 stay with
the signed-in walk that CTO msg 101108 deferred to Andrew.

```json
[
  {
    "id": "DSGN_IRPTV1-S3",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Round-2 merged candidate typecheck red: one TS2339 in tabs/holdings/HoldingsTreemap.tsx (195,40), IV-e-5's own file.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S3",
      "portal DEV CI run 36200546242 'CI - Build & Validate' at 1e821a6e: step 'Type Check (TypeScript)' success (gh run view, read by 3.0.0_SA_CVO)",
      "portal PROD 36a37afc merges DEV (merge DEV->PROD round 4); org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab (tsc 0 errors at 4d6c8aaa and 36a37afc)"
    ],
    "remedy": "Executed in round 2: a type-only fix by the authoring worker, re-merged by the issuer. Typecheck is green on DEV CI today.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T23:18:52Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-S5",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IVE2-AC2's <expect> 'FIXTURES-MATCH: matched' was unanchored and admitted the partial line 'matched 2 of 5', which the criterion's own prose calls a refusal.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S5",
      "org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-2.style-and-instrument.md:31 at HEAD: <expect>DRIVER-FIXTURES-MATCH: matched 5 of 5</expect> (anchored)",
      "workspace 49dc5d9216 (the issuer's amendment); 1.0.0_SA_CTO msg 100632 accepted it and made anchored count expects the project rule"
    ],
    "remedy": "Executed in round 2: the expect was anchored to the full count at 49dc5d9216, and the grader re-ran the driver at the chain-B drain.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-24T13:13:09Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-S6",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The grader's run PNG of the round-2 candidate showed solid black Securities-map tiles labelled 'not supplied', and an id printed as a Holdings name.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S6",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_FAST_PIN_GRADES_20260924.md@ddb0339061 pins 1 (92d16efc, tiles coloured) and 13 (86561aef, served asset class) PASS",
      "portal 2cac0a83 (IV-e-25, model colour by served model_code) and df5e41b5 (IV-e-18, ids never print): ancestors of origin DEV 1e821a6e and PROD 36a37afc",
      "deliverables/2.0.0_SA_COO~D/round3-close.run.txt@98c72cdfb0: accIds 0 on every body"
    ],
    "remedy": "Executed across FAST and rounds 3-4: tile and security colour come from the served class and model code, and ids never print.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T18:59:22Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-S7",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The InvestorReporting unit suite carries legacy failures that assert behaviour the PRD retired, mixed with regressions. S9 fixed 4 of the first 8. The legacy set now reads 80 fail at 4d6c8aaa against 81 at the round-4 baseline, with no new failure; the per-test ruling on the remainder is not done.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S7",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab (80 fail / 787 pass at 4d6c8aaa; baseline 757 / 81)",
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S9 (4 of 8 fixed: c1d7aefe, 9902bf25)",
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W9-S4 (the same set seen by a worker sweep, 86 at its worktree)"
    ],
    "remedy": "One batched cell in round 5 (spine L10: an instrument or record residual is batched, never a round of its own). Each remaining failure is dispositioned as a regression to fix, or as a legacy assertion retired by 1.0.0_SA_CTO's ruling -- never by editing a legacy suite to pass. Disarm: the row quoting the ruling and the landing or retirement of each.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": null
    }
  },
  {
    "id": "DSGN_IRPTV1-W10-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IVE16-AC1 (no per-tab Export) could not be met inside IV-e-16's grant: tabs/analysis/AnalysisTab.tsx kept a permanently disabled data-slot=\"export-button\".",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W10-S1",
      "portal origin DEV 1e821a6e src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx: 0 occurrences of 'export-button' (read)",
      "portal d4d50a3d (IV-e-22), ancestor of DEV and PROD; round3-close.run.txt@98c72cdfb0 perTabExport:0"
    ],
    "remedy": "Executed: the control was removed at the round-3 drain and by IV-e-22; the header Export is the single control.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T18:38:11Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W7-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IV-e-9's SearchSelect adoption removed the literal onChange={handleSelect} that IVE8-AC2 arm 2 checked; the selection path itself was unchanged.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W7-S1",
      "portal origin DEV 1e821a6e src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-8.selection-path.test.ts:55,72 (arm 2 = handleSelect byte-identical; read)",
      "portal 89a6d4f4 (drain repair), ancestor of DEV and PROD"
    ],
    "remedy": "Executed: arm 2 was re-pointed at handleSelect's own body.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T00:41:46Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W7-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Holdings AccountFilter could not receive the live narrowing: the selection triple lived in index.tsx, outside IV-e-10's grant.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W7-S2",
      "portal 8cd2dab2 (round-3 drain hookups: the header's accepted selection reaches the tabs), ancestor of DEV and PROD",
      "deliverables/2.0.0_SA_COO~D/round3-close.04-holdings.png@98c72cdfb0 ('Account: All accounts' beside the view; probe accountFilter:1)"
    ],
    "remedy": "Executed: the drain hookup threads the header's accepted selection through HeaderSelectionContext. The Performance filter was round 4's IV-e-21.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T01:06:04Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W9-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "GenerateComposer's per-account list was sourced from scope.permittedAccountIds, the same 1,000+ list an Andrew-direct refused.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W9-S1",
      "portal 8cd2dab2, ancestor of DEV and PROD",
      "deliverables/2.0.0_SA_COO~D/round3-close.05-analysis.png@98c72cdfb0 ('Accounts (2 included)': Trust Account ****4471, Family IRA ****9020)"
    ],
    "remedy": "Executed: GenerateComposer reads the client and its accounts from headerSelection.scope.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T01:06:04Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W11-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The firm chip's name text was the pinned assertion of an out-of-grant test (__tests__/fe-s-10/parity.test.ts), so IV-e-18 could not move the chip.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W11-S1",
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_IRPT_20260925.md@75156f2b18:80 (R6; msg 100948)",
      "portal 29550954 (round-4 chain 3, IV-e-23), ancestor of DEV and PROD; origin DEV parity.test.ts:69 compares globalName (read)"
    ],
    "remedy": "Executed on the CTO's R6 ruling: parity is kept, and only the system token moves to a disclosure (IV-e-23).",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO (ruling R6) with 2.0.0_SA_COO~D (landing)",
      "at": "2026-09-25T18:39:01Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W11-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Printing 'not supplied' instead of UNAVAILABLE broke an out-of-grant pinned test (__tests__/fe-s-5/states.test.ts) asserting '>UNAVAILABLE<'.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W11-S2",
      "RULINGS_IRPT_20260925.md@75156f2b18:80 (R6)",
      "portal 2cac0a83 (IV-e-25), ancestor of DEV and PROD; origin DEV fe-s-5/states.test.ts: 0 occurrences of '>UNAVAILABLE<' (read)"
    ],
    "remedy": "Executed on R6: states.test.ts was re-scoped by IV-e-25.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO (ruling R6) with 2.0.0_SA_COO~D (landing)",
      "at": "2026-09-25T18:59:22Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W11-S3",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "iv-e-10.ruled-touch.test.ts measured a fixed base and went red once later ruled cells (IV-e-18, IV-e-19) edited the same file.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W11-S3",
      "portal ecfd327a (round-3 drain repair: the bound now covers IV-e-10's own commit a65074e7), ancestor of DEV and PROD",
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S14 (W11-S3 recorded disarmed at the drain)"
    ],
    "remedy": "Executed: the bound was re-scoped to IV-e-10's own commit.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T02:47:00Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W11-S4",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "DrillTree's legend <li> carried whitespace-nowrap inside a flex-wrap row, so a long model name drew a stray horizontal scrollbar.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W11-S4",
      "portal origin DEV 1e821a6e src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx:163 (li class 'inline-flex max-w-full items-center gap-1.5 break-words'; read)",
      "portal c75f68a3 (IV-e-20), ancestor of DEV and PROD; S14 records IVE20-AC2 PASS after the join merge"
    ],
    "remedy": "Executed: the legend entry wraps inside its bound.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T03:21:27Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W19-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ConsolidatedOverviewPanel gained a tenantLayout prop, but none of its PROD call chains passed it, so the client-drill cash/other colours stayed off the firm palette.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W19-S1",
      "portal origin DEV CanonicalBookView.tsx:61,99,111 (tenantLayout threaded into the panel; read)",
      "portal 4d6c8aaa (IV-e-30 merge), ancestor of DEV and PROD; org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round4-L8-packet.md@5ff5f9b9ab (IVE30-AC1/AC2 PASS)"
    ],
    "remedy": "Executed: IV-e-30 threads tenantLayout through CanonicalBookView and its callers.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-25T22:38:55Z"
    }
  }
]
```
