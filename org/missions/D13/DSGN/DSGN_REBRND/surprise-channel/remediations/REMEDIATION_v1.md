# DSGN_REBRND -- round 1 remediation slug

Author: 3.0.0_SA_CVO. Round: v1. Fabric: laptop. Recorded: 2026-09-14T18:50:08Z. Branch: `feature/d13-visual-elevation` (LOCAL; not on CLOUD by Andrew's 2026-09-11 confinement), channel read at a1d0a7451c.

One row per GRADUATED item: 33 graduated investigation items (C-S5 to C-S10) plus this seat's own four (C-S11 to C-S14). Every row is OPEN. The eight DECOMP_INVALIDATING items (C-S4, the page inversion) carry no remediation row: their remedy is a new cell, and the re-decomposition is the COO's call at the recut.

Reader: **1.0.0_SA_CTO only**, one slug for this project. No row carries `route` or `loop_target`. The round-2 priority Andrew set at ~18:1xZ (msg 96669) is card/panel texture first, the light-mode inversion's state rule second (C-S4), the five indigo accents third, tooltips fourth; it grades nothing here.

```json
[
  {
    "id": "DSGN_REBRND-W3-S4",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Under a forced failure (every data request answered 503), the live 401, or held requests, seven routes draw data, EMPTY or LOADING where C12 requires ERROR: /market's Global RSI bars and Fear & Greed dial show a reading (50, 'Neutral', stamped with the current time; the RSI tooltip reads 'Now 50.0, 90D ago 50.0, Neutral'); /positioning and /advisor-intelligence render EMPTY sentences; /attribution holds its skeleton and renders EMPTY; /portfolio-management renders 0.00 metrics and an EMPTY sentence identically in default, empty, loading and error; /ticket-center shows its error line above 'No open tickets.'; /data-refresh History says 'No History Yet' on a 401.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W3-S4",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S5)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Every panel on the seven named routes renders ERROR, never a reading, EMPTY or LOADING, when its request fails; the /market Fear & Greed dial and Global RSI bars draw no value without data. Grade by a forced-failure render of each route.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W3-S1",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "No route or panel in portal/src renders an observable NO-PERMISSION state today -- every access denial found (route-level requireAdmin/requireInternal/firm-allowlist, a panel-level element hide, and one transient toast) is non-rendering, so this inventory cannot cite a fixture or a render for that state anywhere.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W3-S1",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S5)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Wire NO-PERMISSION to the access denials the inventory found (route guards, the panel-level hide), or record in the contract which denial renders it; FWD-11 requires four designed states and one is built but reachable nowhere.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W3-S5",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Beyond the four designed components, the read renders show a dozen further state treatments and developer text on client surfaces: bare spinners or a plain 'Loading...' line (/valuations, /correlations, /portfolios, /advisor-intelligence, /security-scanner, /data-refresh, /investor-reporting, /login); red text on the bare canvas plus a raw code IR-REQUEST-FAILED (/investor-reporting); an amber warning inside the band (/data-refresh); a red-on-pink banner (/positioning ETFs); the same ERROR sentence twice on one page (/factor-tilts); three error idioms across four auth pages, two of them light red-400 on pink; a tab that renders nothing (/philosophy Views); raw JSON response bodies in Cause lines; a CORS/S3 developer note (/portfolios); and 'silver page bg' contrast copy (/dev/page-surface-control).",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W3-S5",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S5)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Census every non-designed state treatment in portal/src (bare spinners, 'Loading...', red text on the bare canvas, raw codes) and move each onto one of the four C12 states.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W3-S3",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "23 of the inventory's 96 render obligations could not be rendered in their named state, yet rb13-coverage-check.py reads COVERED 96 of 96, because it checks that a mapped PNG exists and not what it shows: 12 data routes' DEFAULT rows render the route's ERROR (the live dev plane refuses the inert ui-smoke token with 401 and no ui-smoke fixture exists for them), 10 EMPTY rows render the app error boundary or an ERROR under the only empty shape constructible without a fixture, and /valuations|toggled-panel has no control to toggle while its data is refused.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W3-S3",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S5)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Re-render the 23 NO rows in their named state with consumable fixtures, and make rb13-coverage-check read what a render shows (a state marker), not that a PNG exists.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W3-S6",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 58 keyboard walks (1,379 stops, every one focus-visible with a painted ring) found what a ring cannot show: the file drop zones on /data-refresh and /trade-submission never take focus, so each page's upload is unreachable from the keyboard; /portfolios puts two stops on invisible chart internals (an empty svg and a bare g); and one of five loads of /attribution with its fixture fell to the app error boundary on mount. The read renders add two visual defects: the top '90D' marker on /market's Global RSI is clipped at the plot's upper edge, and /trade-submission's form fields paint a mid-grey fill inside the #0A1733 band.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W3-S6",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S5)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Make the /data-refresh and /trade-submission drop zones keyboard-focusable and operable, take the chart internals on /portfolios out of the tab order, and bring the out-of-order focusables on /investor-reporting and /trade-submission into it.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S20",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two of the three routes have NO persistent primary action to put the accent on: every accent fill on /positioning and /market was a state control. The third route's one primary action (Upload Portfolio) sits inside a #0A1733 band, where DESIGN.md C8 says no primary action goes.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S20",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Rule how FWD-4's 'one primary action per view' reads on a view with no action (/positioning, /market), and move /portfolio-management's Upload Portfolio out of the band C8 keeps actions out of.",
    "owner": "1.0.0_SA_CTO (the per-view rule), then 2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO (the per-view rule), then 2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-S3",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Global RSI bars on /market still render a lime/chartreuse gradient -- an ORDERED quantity on the token file's data.performance family, which no cell ramped -- and RB5-AC5's judgment evidence never renders /market, so the grader cannot see the route where 'no off-palette colour is the loudest thing on any page' is most at issue.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-S3",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Ramp the Global RSI value-band colours onto one hue (RSIBars.tsx:140-155 and RSIModal.tsx getRSIColor), which RB-s-4's census missed, then re-read RB5-AC5R's loudest-colour clause on /market.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W2-S11",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The asset-class legend on /positioning paints Fixed Income #10B981 and Equities #3B82F6, the reverse of the token file's data.assetClass (equity #10B981, fixedIncome #3B82F6), so the two carriers disagree on which colour means which asset class.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W2-S11",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Make the /positioning asset-class legend and the token file's data.assetClass agree on which colour means which class, from one writer.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W1-S37",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 270 +/- performance figures on /market paint #2DCE89 (147 text nodes) and #F5365C (123). Neither value matches any of the 4 --status-* or 23 --data-* tokens on the page's :root, so the busiest route's rendered gain/loss colour sits outside both token families.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S37",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Route /market's gain/loss figure colours (147 #2DCE89 and 123 #F5365C text nodes) through the status or data token family; today they match neither.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S4",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two parallel model-portfolio colour systems disagree: the legacy --model-* CSS custom properties (now relocated to data.model / data.chart, values preserved) do not match portal/src/lib/modelPortfolioColors.ts's per-model hex for the same named models.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S4",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Give model-portfolio colours one writer: the relocated --model-* properties and modelPortfolioColors.ts disagree for the same named models.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S14",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ONE ordered encoding -- the duration ladder -- had FOUR independent writers, and fixing the first three moved nothing on screen; only reading the DOM after each edit found the fourth.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S14",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Collapse the duration ladder's four writers to one source, so an edit cannot move three and miss the fourth.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W1-S16",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Model-name holdouts, recorded for L10 as the order directs: getModelColor() in aum.ts still keys the five models by their EARLIER names, and this order fixed only their colours and the UST shadowing, not the names.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S16",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Rename the five model keys in aum.ts getModelColor() to the current model names, as the order recorded for L10.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S8",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The product's BOLD weight is not a Bold: the cell orders Lato 400 and 700, a real Lato Bold is not on this box, and font-weight 700 is served by the SemiBold face (OS/2 usWeightClass 600) on the issuer's instruction.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S8",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "A real Lato Bold 700 needs Andrew's per-use word for the fetch or a supplied file; until then weight 700 is the SemiBold face, disclosed. Andrew may instead accept 600 as the product's bold.",
    "owner": "Andrew's word; otherwise 2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "Andrew's word; otherwise 2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "Andrew's word; otherwise 2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W2-S9",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The token file carries no typography, spacing, radius or grid block, so the non-colour values the cell itself requires the contract to resolve have no token-file counterpart to be byte-equal to.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W2-S9",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S7)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Add typography, spacing, radius and grid blocks to portal/design/brands/opal-capital.json so every value DESIGN.md names has a byte-equal token (FWD-6 PROOF).",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S3",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "portal/design/themes/opal-capital.css was not reproducible by running its own generator against the JSON before this cell, and still is not for the pre-existing Semantic block -- relevant to R3 (canvas and surfaces), which owns collapsing that structure.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S3",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S7)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Make portal/design/themes/opal-capital.css reproducible from its generator and the JSON, the Semantic block included, with light and dark split there.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S25",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The band ring renders rgb(230, 234, 244), #E6EAF4, not DESIGN.md's #E8ECF5, because the generated --palette-white is the rounded HSL '222 38% 93%'.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S25",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S7)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Carry #E8ECF5 as an exact hex, not a rounded HSL, so the rendered band ring equals DESIGN.md's value.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S22",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The order says to build the ring from 'the ring token RB-s-1 defines', but RB-s-1 defined no ring token. The only ring definition is portal/DESIGN.md C11, a two-layer ring, not the site's single 2px ring the face quotes.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S22",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S7)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Define the ring token, and either match the site's single 2px ring (FWD-5: 'with the ring the website ships') or record C11's two-layer ring as a deliberate difference with its reason.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S29",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "portal/DESIGN.md defines no page terminator, so 'the contract's designed terminator' that RB-s-9 asks every page to end on has no clause to point at.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S29",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S7)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Add a page-terminator clause to DESIGN.md and apply it, so a sparse page can end on it (FWD-10; RB9-AC5 FAILS on its absence).",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S36",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The shadows dimension no longer agrees. The brief records shadows as the one agreement, but at portal a65b939a painting box-shadows sit on 5, 1 and 2 elements of /market, /positioning and /portfolio-management: a shadow-lg on the navigation rail on all three, one on the Optimization Report panel, and four red 12px glows on /market markers.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S36",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S8)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Remove the painting box-shadows (the nav rail's shadow-lg on every route, the Optimization Report panel, four red glows on /market) or record each as a deliberate difference; the contract says no drop shadows.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S34",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The side-by-side render pair has no site half. No render of opalinvest.com is on record: design/brand holds only the .md and .json of the 2026-09-11 capture. A new capture of the site is egress this order carries no word for. So the pair was produced as the three portal renders plus a sheet drawn from the two JSON files.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S34",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S8)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "FWD-1's walk and its site half need a render of opalinvest.com: Andrew's per-use word for the capture, or a re-cut of FWD-1's proof onto an act a seat can take on demand (Rule 27: no FWD is a wait).",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W2-S15",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Three auto-read portal/src carriers outside this order's grant still state the 2026-07-15 silver-canvas law as current: panels/README.md, TicketCenter.tsx and designTokens.ts. The running theme contradicts all three.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W2-S15",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S8)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Rewrite panels/README.md, TicketCenter.tsx and designTokens.ts onto the 2026-09-11 law under a cell that grants them (FWD-1 CONSTRAINT: rewritten in place, never left standing).",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W1-S24",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A fifth comment, outside the four the order names, still states the superseded canvas: TicketCenter.tsx:174 (:171 at base) calls the page 'the silver canvas'. Not edited.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S24",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S8)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Rewrite TicketCenter.tsx:174's 'silver canvas' comment under the same grant as W2-S15.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W2-S2",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "portal/vite.config.ts's build.rollupOptions.manualChunks still names 'vendor-apexcharts':['apexcharts'] and 'vendor-nivo':['@nivo/core','@nivo/radar'] after this cell retired both from package.json and from every .tsx importer; the file sits outside RB-s-11's <paths> grant so it was not edited.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W2-S2",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S8)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Drop the vendor-apexcharts and vendor-nivo manualChunks entries from portal/vite.config.ts under a cell that grants it.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W2-S1",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TopicCloud.tsx's @visx/wordcloud spiral layout has no recharts equivalent -- migrating it would replace a spatial word-size/position cloud with a categorical chart type, changing WHAT the chart shows, so RB11-AC2/AC3 stay MULTI-RENDERER/STILL-DECLARED by the order's own rule.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W2-S1",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S8)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Rule whether TopicCloud's word cloud stays on @visx as a named exception to FWD-8's one charting library or is replaced by a chart that shows the same thing; FWD-8's constraint makes this row the carrier.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-10-01T10:20Z"
    }
  },
  {
    "id": "DSGN_REBRND-W2-S8",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Three of the five locked canon hexes measure below the 3:1 SC 1.4.11 floor against the white panel, and the lock forbids moving them.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W2-S8",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S9)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Three locked canon hexes measure below the SC 1.4.11 3:1 floor on the white panel Option A makes the default ground; the canon lock and the contrast bar cannot both hold as written. Andrew rules: keep the canon and add a non-colour cue, or allow a darker step for small marks.",
    "owner": "1.0.0_SA_CTO (to put to Andrew)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO (to put to Andrew)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO (to put to Andrew)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W1-S11",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "In the selected dark mode NO accent colour of any hue can satisfy both of the roles the product gives it -- white-on-accent and accent-on-band both at 4.5:1 -- because the two luminance bounds do not overlap; this is arithmetic, not a tuning miss.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S11",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S9)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "No accent hue meets 4.5:1 both as white-on-accent and as accent-on-band in the selected dark mode (the luminance bounds do not overlap). A ruling, not tuning: which role the dark-mode accent drops.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S6",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RB2-AC4's own invocation ('ls public/fonts/ | head -20; echo rc=$?') prints rc=0 even when public/fonts/ does not exist at all -- the pipeline's exit status is head's, not ls's, so the check cannot discriminate present from absent.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S6",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Re-cut any criterion that pipes into head so its rc is the listing's, not head's; test file presence directly.",
    "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W1-S12",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "RB3-AC5's own pattern has a wildcard that crosses newlines, so any radius-token USAGE in index.css makes it read past the usage and grade the NEXT declaration's value as an off-band radius -- it printed MID-RANGE twice while all five radius tokens were in band.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S12",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Anchor such patterns per line so a token usage is never graded as a declaration.",
    "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W1-S17",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "rb4-canon-check.py ARM A cannot see the five CANONICAL entries of MODEL_PORTFOLIO_COLORS -- their name and primary sit on different lines -- so on the pre-revert tree it flagged only the eight aliases while all five primaries were navy.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S17",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Let rb4-canon-check.py ARM A resolve a rung from its enclosing key so the five canonical entries are visible, with the pre-revert tree as its positive control.",
    "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "round": "v1"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "at": null
    }
  },
  {
    "id": "DSGN_REBRND-W1-S18",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RB5-AC4 already printed VERDICT: RETIRED before this cell changed anything: RB-s-4 had removed the #ADFF2F literal from index.css, so this criterion cannot tell this cell's work from no work.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S18",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Run every checker on its base tree at the cut; one that already reads its target verdict there cannot tell work from no work and is re-cut.",
    "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S35",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RB14-AC1 counts the file's top-level keys, not its routes. A file in the website file's shape carries at least 12 keys, so it reads MEASURED however many routes it covers. A bare {a, b, c} object also reads 'ROUTES-MEASURED: 3 / VERDICT: MEASURED'.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S35",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Re-cut RB14-AC1 to count measured routes, not top-level keys.",
    "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S21",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The worker face this worker was handed carries a BOUNDS bullet, 'THE CANON LOCK', that the task order file does not carry. So the face and its record disagree by one clause.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S21",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Cut the worker face from the order file, never edit it beside the file; the two must carry the same clauses.",
    "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-W1-S23",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The order cites row DSGN_REBRND-W2-S15 as the source of the comment fold and its census, but no such row exists in the channel, so 'the same census the row used' cannot be re-run.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c#DSGN_REBRND-W1-S23",
      "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/adjudications/ADJUDICATION_v1.md (carrier C-S10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 2"
    ],
    "remedy": "Resolve every row id an order cites against the channel at the cut.",
    "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-C-S11",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Fear & Greed gauge colours its state label with the accent token, outside the five identity sites C8 and FWD-4 allow.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/rb-s-5r_market_1440.png@a1d0a7451c",
      "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/rb-s-10_market_error_1440.png@a1d0a7451c",
      "2.0.0_SA_COO~D drain-end msg 96663 item 5 (untracked inbox carrier)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 4"
    ],
    "remedy": "Paint the Fear & Greed state label in ink or a ramp step, not the accent, and re-read RB5-AC5R's 'AND NOWHERE ELSE' on /market.",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-C-S12",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "RB-s-7 wrote the contract's front matter without the class field the CONTRACTS clause names, so no value in it carries its claim.",
    "evidence": [
      "portal/DESIGN.md @portal 086371dd (feature/d13-visual-elevation), read by this seat",
      "2.0.0_SA_COO~D drain-end msg 96663 item 5 (untracked inbox carrier)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 4"
    ],
    "remedy": "Label every token value in DESIGN.md's front matter with its class and write each derived value's rule beside it (the admitted PRD v0.5 classes the identity role and the selection highlight DERIVED).",
    "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut)",
      "round": "v1"
    }
  },
  {
    "id": "DSGN_REBRND-C-S13",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The branch was confined off CLOUD on 2026-09-11 and the PRD amendments v0.3-v0.5 landed on CLOUD only, so the two carriers of the spec diverged.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@a1d0a7451c (v0.2)",
      "org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@01378b0a5b on CLOUD (v0.5)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 4"
    ],
    "remedy": "Bring the admitted PRD (v0.5 @01378b0a5b) onto feature/d13-visual-elevation, or have the round-2 issuance name v0.5 on CLOUD as the governing text.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-10-01T10:20Z"
    }
  },
  {
    "id": "DSGN_REBRND-C-S14",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The grades carrier's criterion pattern admits only <X>-AC<n>, while the estate's amendment convention mints <X>-AC<n>R for a retired-and-replaced criterion (RB5-AC5R here; RB4-AC4R, RB10-AC2R, RB13-AC2R on mechanical rows), so an amended JUDGMENT criterion has no legal grade carrier.",
    "evidence": [
      "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json@ed2aaccf85",
      "org/surprise_channel/schemas/investigation_item.schema.json properties.grades.items.criterion.pattern",
      "org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-5.accent-controls.md@a1d0a7451c <expected_criteria>",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 4"
    ],
    "remedy": "Widen the grades criterion pattern to admit the amendment suffix (for example '^[A-Za-z0-9]+-AC[0-9]+R?$') and any judgment id shape the estate mints (a J-shaped id was refused on another project the same evening), then move RB5-AC5R's verdict into a grades entry.",
    "owner": "1.0.0_SA_CTO (schema owner)",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO (schema owner)",
      "round": "v1"
    }
  }
]
```
