# DSGN_IRPTV1 -- round 1 remediation slug

Author: 3.0.0_SA_CVO. Round: v1. Fabric: laptop. Recorded: 2026-09-24T10:15:00Z.

Input snapshot: workspace `07c4156d08`; portal candidate `dsgn-irptv1-r1` @`837983cb`. Investigation: `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md@07c4156d08` (8 rows). Adjudication: `surprise-channel/adjudications/ADJUDICATION_v1.md` (same commit; 8 of 8 items dispositioned, 4 of 4 judgment criteria graded). Review record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND1_L8_L9_REVIEW_20260924.md` (same commit).

Seven rows: 2 REMEDIATED and closed inside the round (the channel-tree race, the typecheck red); 5 OPEN for the recut -- one rule breach a client would see (the derived ticker, ARMED), two enrichment remainders the worker rows named (the chip toggle and per-account names; the L2 members), and two residuals for the round's one batched style/instrument cell (the slate inks and the 600 weight; the smoke fixtures that never resolve a scope). No row carries `route` or `loop_target`. Reader: **1.0.0_SA_CTO only**; the recut is `2.0.0_SA_COO~D`'s.

```json
[
  {
    "id": "DSGN_IRPTV1-W1-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The project's surprise-channel tree did not exist when round 1 opened; the first worker minted it, and a sibling slot whose worktree branched before that commit could mint a divergent file. The drain reconciles by UNION of rows under one header.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W1-S1",
      "workspace commit 0749cd6222: add/add conflict on the channel file resolved by union of six ids under one header",
      "ADJUDICATION_v1.md#DSGN_IRPTV1-C-S5 (same commit)"
    ],
    "remedy": "Executed inside the round: the union at the drain (0749cd6222). The mint-on-first-row rule stays the project's precedent; no cell is cut.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-24T09:49:04Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-W1-S3",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The OVER WHAT chip toggle needs a handler line in index.tsx that the ruled touch bound (mount line plus one import) does not admit, and no DirectoryEntry per permitted account reaches the card from the real mount (only opaque permittedAccountIds and the one selected row.entry). The card renders real chips only when the selection is itself an account; otherwise 'Account details not supplied'.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W1-S3",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~1/identity-card.result.md@7b8cd4571e",
      "ADJUDICATION_v1.md#DSGN_IRPTV1-C-S7 (same commit)"
    ],
    "remedy": "The C1 remainder (PRD v0.5 backlog item 1): a cell whose face grants index.tsx the toggle handler through the existing selectionRequest path and names the per-account directory source that feeds accountEntries (name + masked tail per permitted account); until then the fallback text stands and is honest.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "DSGN_IRPTV1-W3-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "IV-t-3's mapping fills each L0 category's top-level members and children[label].aum; CategoryViewTree's L2 hover detail and breakdown dialog read only children[label].members, which the mapping never populates, so L2 stays empty wherever a direct child is an intermediate node rather than a leaf.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W3-S1",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/holdings-hero.result.md@0749cd6222",
      "ADJUDICATION_v1.md#DSGN_IRPTV1-C-S3 and #DSGN_IRPTV1-C-S8 (same commit)"
    ],
    "remedy": "Inside mdpfResultFromSnapshot (the function IV-t-3 already owns): populate children[label].members with the leaf securities beneath each L1 child, named from display.label else displayName; keep the top-level members fill. One function, one field; the COO's drain-end message already places it in the first repair cell.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "DSGN_IRPTV1-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The merged candidate at 7736e6cc failed `tsc -b --noEmit` with five errors in the worker test file __tests__/dsgn-irptv1/iv-t-3.hero-fed.test.ts (TS2339 :82; TS18046 :97 / :102 / :107 / :108 -- a JSON-loaded fixture walked without a type narrow), so `bun run build` could not build the candidate.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-S1 and #DSGN_IRPTV1-S2",
      "portal candidate commit 837983cb (parent 7736e6cc): one file, +4/-1; typecheck rc=0; seven dsgn-irptv1 suites 0 fail / 55 expects; fe-s-7/ 32 pass",
      "1.0.0_SA_CTO message 100500 (the word for the issuer-direct fix; the five-error read)",
      "ADJUDICATION_v1.md#DSGN_IRPTV1-C-S10 (same commit)"
    ],
    "remedy": "Executed inside the round on the CTO's word: the issuer-direct typing fix at portal 837983cb, test file only. No cell is cut.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-24T10:02:12Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S12",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "SecurityList.tsx tickerFor() (portal 837983cb :61-69) returns display.symbol when present, else the tail of securityId split on ':' or '-', else 'not supplied'. Every security on every fixture carries display null, so the Ticker column prints '1'..'4' from 'sec:opaque-N'; live security ids are CUSIPs, so the same branch prints a CUSIP or its tail on the body. The FE derived a value the wire did not state and put an identifier fragment where FWD-11 forbids one; IV4-AC1's mechanical check forbids only the FULL id in the cell and cannot see it.",
    "evidence": [
      "C:/tmp/dsgn-irptv1-r1 src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx@837983cb :61-69",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/iv-t-4.security-list.html@0749cd6222 (data-slot=security-ticker cells '1'..'4')",
      "C:/tmp/dsgn-irptv1-r1 src/pages/InvestorReporting/fixtures/fe-s-7/holdings.smartx-observed.json (display null, securityId sec:opaque-1..4)",
      "ADJUDICATION_v1.md#DSGN_IRPTV1-C-S4 and #DSGN_IRPTV1-C-S12 (same commit)"
    ],
    "remedy": "One branch in tickerFor(): return display.symbol when present, else 'not supplied'; never split the id. Add to IV4-AC1's suite the arm 'no ticker cell contains any substring of securityId when display.symbol is absent', with a positive control that plants a symbol and sees it print. Rides the round's first repair cell with W3-S1 -- it is a rule breach a client would see, not a style residual.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D",
      "at": "2026-09-24T11:12:46Z"
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S13",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PerformanceHeadline.tsx and SecurityList.tsx style their own text nodes with the text-slate-* idiom and font-semibold (600); DESIGN.md C1 admits weights 400 and 700 only and C9 makes body ink navy with #6B7280 secondary on a panel. IdentityCard.tsx already uses the tokens. Two of the four new components would send the design team's pass back to removing text-slate-*, which FWD-10's ACCEPT names as the thing that pass must not spend itself on.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~2/iv-t-2.headline.html@5537b0a9fb (font-semibold x5; text-slate-600 x4, -900 x4, -500 x1)",
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/iv-t-4.security-list.html@0749cd6222 (text-slate-900 x18, -500 x6, -700 x4, -600 x1; font-semibold x6)",
      "portal/DESIGN.md C1, C9 at portal 837983cb",
      "ADJUDICATION_v1.md#DSGN_IRPTV1-C-S2, #DSGN_IRPTV1-C-S4, #DSGN_IRPTV1-C-S13 (same commit)"
    ],
    "remedy": "In the two components' own bytes: navy / darkGray ink tokens in place of text-slate-*, font-bold / font-normal in place of font-semibold; the shared PanelHeader is DSGN_REBRND's and is not touched here. Batched into the round's ONE style/instrument cell (spine L10), graded by a class census that prints zero slate tokens and zero 600 weights in the two files' own markup.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "DSGN_IRPTV1-C-S14",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The fixtures under fixtures/smoke/ that the AC4 criteria hand to scripts/ui-smoke.mjs never drive resolve-scope to a resolved state ('FIXTURES-MATCH: matched 1 of 2' with a dead performance route on slot 1; 'matched 1 of 9' on slot 3), so every PNG this round is the 'Scope could not be resolved' page and no new component appears in any screenshot. The PNG half of each AC4 was empty by construction.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~1/iv-t-1.png@7b8cd4571e and 0.9.0_WK_DSGN_IRPTV1~3/iv-t-3.png@0749cd6222 (viewed by the CVO: unresolved-scope state)",
      "the three result files' FIXTURES-MATCH lines at their drain pins",
      "ADJUDICATION_v1.md#DSGN_IRPTV1-C-S14 (same commit)"
    ],
    "remedy": "Either the smoke fixture set carries a resolvable scope (resolve-scope + directory-search + selection stubs sufficient to auto-select the Cottonwood account) so a PNG can mount the tab, or the AC4 faces name the static markup as the evidence and drop the PNG. Batched into the same instrument cell as C-S13; the live trace, not a fixture PNG, remains FWD-1's evidence.",
    "owner": "2.0.0_SA_COO~D",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D",
      "round": "v1"
    },
    "closed": false
  }
]
```
