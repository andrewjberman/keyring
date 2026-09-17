# DSGN_REBRND: CVO adjudication

Round 1 L8 compile and L9 adjudication by `3.0.0_SA_CVO`, on 2.0.0_SA_COO~D's drain-end (msg 96663) and 1.0.0_SA_CTO's routing (msg 96664 item 2): the channel lives on `feature/d13-visual-elevation`, and these documents land beside it. Channel read at a1d0a7451c: 67 rows, 67 new since the issuance 845cb2b6ac (the channel did not exist there), 0 lost, 67 carrier-less before this document. Every row below was read against the artifact that closes it or grounds it. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md`.

```json
[
  {
    "id": "DSGN_REBRND-C-S1",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1 L9 GRADE RECORD: the twenty-two JUDGMENT verdicts bound to each proof instance at its commit -- 10 PASS (8 with a named qualification), 9 FAIL, 3 NOT_EVALUATED. 21 ride `grades` here; RB5-AC5R (FAIL) rides C-S14 because the schema pattern refuses its amended id. Graded against PRD v0.5 @01378b0a5b (ADMITTED); the branch's own PRD copy is v0.2 (C-S13).",
    "class": "OBSERVATION",
    "spec_asserts": "Spine v3 L9: a JUDGMENT criterion is graded by the CVO and never self-graded; its verdict lives in `grades`, one entry per criterion, on a row of the CVO's.",
    "world_is": "22 of 22 judgment rows across 15 governing instances read UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming this seat. RB5-AC5 on the superseded original RB-s-5 instance (0.9.0_WK_DSGN_REBRND~1) is not graded: the reopened order retired it for RB5-AC5R, and that instance reads INVALID only against the amended expected set. Evidence read: the instances, 11 renders, the inventory JSON, DESIGN.md, RSIBars.tsx and two rewritten law files; record org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-1.token-spine.proof_of_spec.json@cc480cc723",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-10.four-states.proof_of_spec.json@bccea536d0",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-14.boundary-parity.proof_of_spec.json@1df06e9112",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-15.andrew-pack.proof_of_spec.json@1fb309e862",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-2.typography-lato.proof_of_spec.json@cf406a823c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-3.canvas-surfaces.proof_of_spec.json@cf5a65f497",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-4.ordered-scales.proof_of_spec.json@5072b24fad",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-6.focus-visible.proof_of_spec.json@7a7364907b",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json@38f1c57663",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-11.one-renderer.proof_of_spec.json@46495a26a9",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json@ed2aaccf85",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json@1794c79aef",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-8.archetype-rewrites.proof_of_spec.json@76afb991e3",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/DSGN_REBRND.TO-RB-s-12.surface-inventory.proof_of_spec.json@80dfead12e",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/DSGN_REBRND.TO-RB-s-13.render-coverage.proof_of_spec.json@7333b9c5a1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND1_L8_L9_20260914.md section 3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: it adjudicates no item and opens nothing. Every FAIL's defect is a graduated or DECOMP_INVALIDATING row (C-S4 to C-S13); every qualification travels to 1.0.0_SA_CTO in the round-1 slug.",
    "hazard_standing": "INERT",
    "grades": [
      {
        "criterion": "RB1-AC6",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-1.token-spine.proof_of_spec.json@cc480cc723",
        "verdict": "FAIL",
        "reason": "TO RB-s-1: 'the dark theme is a complete, selectable alternative with its own values in the same file, not a residue'. Complete in the JSON (darkMode palette 11 of 11, semantic 5 of 5 categories): MET. Selectable: NOT MET. The instance records ThemeProvider/ThemeSwitcher unmounted (0 of 2), and at branch HEAD (portal 086371dd) this seat finds 0 mounted theme toggles in portal/src (ThemeSwitcher, toggleTheme, setTheme, portal-theme: 0 hits; html.dark-mode appears only as CSS selectors at index.css:272 and :330). A user cannot select the dark mode; RB3-AC7 reached it by setting the class. The generated CSS was not a light/dark split at this cell's vintage (W1-S3)."
      },
      {
        "criterion": "RB2-AC6",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-2.typography-lato.proof_of_spec.json@cf406a823c",
        "verdict": "NOT_EVALUATED",
        "reason": "Typeface clause MET by measurement: 6 of 6 sampled figures compute Lato with tabular-nums, 2 of 2 same-origin faces load (portal/public/fonts holds lato-regular-400 and lato-semibold-600 plus OFL.txt), a negative control excluded FontFaceSet.check, and rb-s-2_market_1440 shows Lato figures. Alignment clause ('no worse than before') is UNREADABLE: 0 pre-font captures exist, and the graded route renders no populated figure column (every data panel is empty or failing, unfixtured). The bold is the SemiBold face (W1-S8, at Andrew)."
      },
      {
        "criterion": "RB3-AC6",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-3.canvas-surfaces.proof_of_spec.json@cf5a65f497",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION. Canvas #F4F6FA measured by ui-smoke and read as one near-white field around the panels in rb-s-3_market_1440; navy #163372 fills nothing; three navy tiers retired to one container level; 449 of 449 bands enumerated with one stated reason. Qualifications: the bands are a GRANT LIMIT, not deliberate inversions (band pixel share 73.9/45.6/48.3% against the site's 20-31%, RB14-AC4's evidence), carried DECOMP_INVALIDATING in C-S4; the native select on /portfolio-management was not render-verified by this cell (the RB-s-15 AFTER render shows the Fund select styled)."
      },
      {
        "criterion": "RB3-AC7",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-3.canvas-surfaces.proof_of_spec.json@cf5a65f497",
        "verdict": "FAIL",
        "reason": "'every text/background pair on the canvas, on the inverted bands AND in the selected dark mode meets WCAG 2.1 SC 1.4.3 / 1.4.11, denominator printed': 33 of 40 pairs pass (light 17 of 18, dark 16 of 22). Failures: #FFFFFF on #10B981 at 2.54:1 (the INT chip, both modes); three dark-mode accent pairs at 4.27-4.39:1 (structural, W1-S11); the background-token ink idiom at 1:1 in dark (120 sites, W1-S10). SC 1.4.11 was not computed: 0 of 40 pairs are boundary pairs, and the hairline #C4CBDB on #FFFFFF is 1.47:1."
      },
      {
        "criterion": "RB4-AC5",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-4.ordered-scales.proof_of_spec.json@5072b24fad",
        "verdict": "FAIL",
        "reason": "'each ordered quantity uses ONE hue ramped light to dark': the Global RSI bars colour an ordered 0-100 quantity by value band through four hue families (RSIBars.tsx:140-155 @portal 086371dd: perf-weak-neg, perf-strong-pos, perf-neutral, perf-weak-pos), rendering lime-to-yellow in rb-s-4_market_1440 and rb-s-5r_market_1440 (row S3). MET: the Fear & Greed arc is one navy-blue ramp; unordered series keep their colour; the canon duration ladder is exempt under Amendment 1's canon lock."
      },
      {
        "criterion": "RB5-AC6",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json@ed2aaccf85",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION: focus and selection moved the persistent ACTION count by 0 on 3 of 3 routes, with the five identity sites listed separately as Amendment 1 directs. The counterexample's precondition (a primary visible) holds on 1 of 3 routes: on /portfolio-management the count 1 stays 1. On /portfolio-management and /market the focused control sat in a band, so no accent ring appeared beside the action; the accent transient is shown on /positioning only."
      },
      {
        "criterion": "RB6-AC5",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-6.focus-visible.proof_of_spec.json@7a7364907b",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION: 462 of 462 Tab stops ring-painted at the full 4px (107 on the three routes, 355 on 18 inventory routes); the base control at 845833fb paints 0 rings; 15 of 15 mouse clicks on non-text controls paint no ring. Qualifications: 7 of 7 clicks into text fields paint the ring, which is the platform's :focus-visible rule for text entry and is accepted (W1-S28, C-S3); the #0A1733 sidebar paints the light-ground ring (W1-S27); focusables outside the tab order on /investor-reporting and /trade-submission and the unreachable drop zones (W3-S6, C-S5) never take focus, so they cannot show a ring."
      },
      {
        "criterion": "RB6-AC6",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-6.focus-visible.proof_of_spec.json@7a7364907b",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION against brief III.9 ('The visual system survives a reader who has raised their browser's default font size'): at a 24px default (positive control ROOT-FONT 24px) 107 of 107 stops ring, there is no horizontal overflow at 1440, and the sidebar list scrolls. Qualification: panel headers, segmented labels and table text stay at 16px-root sizes, so most data type ignores the reader's raised default (rb-s-6_font24_positioning_full read)."
      },
      {
        "criterion": "RB7-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json@1794c79aef",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION: a fresh builder whose sole design input was the contract built rb7-ac4-page, read at 1440: light canvas, white hairline panels, one #0A1733 band, one accent action, navy ink, a 40/60 split (546.6/819.9 px), 0 shadows at rest, canon model hues, a ring on 3 of 3 controls. Qualifications: it rendered in Arial (Lato absent in the capture, vendoring forbidden by the brief), and its build record lists 32 questions the contract did not answer, evidence against FWD-6's 'the contract resolves typeface, colour role, spacing, shape, elevation, focus and layout split' (C-S7)."
      },
      {
        "criterion": "RB7-AC5",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json@1794c79aef",
        "verdict": "FAIL",
        "reason": "'the rejection record carries the author's agreement that the clause was violated': /positioning is rejected by clause C3 with C8, C4, C6 and C12 in support, but 0 of 5 author agreements are recorded; the agreement is owed (2.0.0_SA_COO~D drain-end 96663, item 4)."
      },
      {
        "criterion": "RB8-AC5",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-8.archetype-rewrites.proof_of_spec.json@76afb991e3",
        "verdict": "PASS",
        "reason": "MET: 5 of 5 rewritten law and skill files carry a dated, directional supersession ('Andrew's 2026-09-11 ruling supersedes the 2026-07-15 archetype'), read by this seat at design/brand/COLOR_ARCHETYPES.md:7 and design/process/UI_VERIFICATION.md:6 on the branch; the old-value census reads 0 across the edited files. Out-of-grant carriers that still state the retired law (W2-S15, W1-S24) are outside this criterion's population and are graduated in C-S8."
      },
      {
        "criterion": "RB9-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json@38f1c57663",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION: on the populated renders the work runs past the fold; the share of the viewport below the last content element is 0.036 before and after on /market and /attribution (the main element's 32px padding). Nothing moved because the brief's empty lower third came from unfixtured captures (W1-S30)."
      },
      {
        "criterion": "RB9-AC5",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json@38f1c57663",
        "verdict": "FAIL",
        "reason": "'the page ends with the contract's designed terminator': rb-s-9_positioning_sparse_1440 ends on the Holdings Breakdown source line, the terminator probe reads present:false, and portal/DESIGN.md defines no terminator clause (W1-S29). The no-filler, no-stretched-row and no-added-panel clauses are met."
      },
      {
        "criterion": "RB9-AC6",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json@38f1c57663",
        "verdict": "PASS",
        "reason": "MET: between-section gaps 20px (7 of 7) against panel inner padding 30px (6 of 6), matching DESIGN.md C10 (spacing.sm 20 between, spacing.md 30 inside)."
      },
      {
        "criterion": "RB10-AC5",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-10.four-states.proof_of_spec.json@bccea536d0",
        "verdict": "FAIL",
        "reason": "'every panel with nothing to show uses exactly ONE of the four states ... no error is painted on the bare canvas': 119 designed-state uses, but under a forced failure seven routes draw data, EMPTY or LOADING where ERROR is owed. In rb-s-10_market_error_1440 the Fear & Greed dial reads '50 Neutral' and the RSI bars draw a reading while every request fails (W3-S4); a dozen further treatments include red text on the bare canvas with a raw code on /investor-reporting (W3-S5); NO-PERMISSION is built but wired to no surface (W3-S1)."
      },
      {
        "criterion": "RB11-AC6",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-11.one-renderer.proof_of_spec.json@46495a26a9",
        "verdict": "NOT_EVALUATED",
        "reason": "The graded render (rb-s-11_market_1440) carries none of the cell's migrated charts, and the one render showing a migrated chart (.scratch/verify_factortilts5.png) is worktree-only and not on record, so no two migrated charts on one screen can be read."
      },
      {
        "criterion": "RB12-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/DSGN_REBRND.TO-RB-s-12.surface-inventory.proof_of_spec.json@80dfead12e",
        "verdict": "PASS",
        "reason": "MET: design/brand/portal-surface-inventory.json holds 99 rows over 24 distinct routes, equal to its route_count (read by this seat); fixed_comparison_set is /market, /positioning and /portfolio-management; related_fixtures appear beside rows as sources, never in place of a render."
      },
      {
        "criterion": "RB13-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/DSGN_REBRND.TO-RB-s-13.render-coverage.proof_of_spec.json@7333b9c5a1",
        "verdict": "FAIL",
        "reason": "'every touched surface in the inventory has a read render on record': 96 of 96 PNGs exist and 58 of 58 walks completed, but only 65 of 96 renders show the named state (6 show no visible difference, 23 do not, 2 are not renderable): 12 DEFAULT rows render the route's ERROR under a live 401 and 10 EMPTY rows render the error boundary (W3-S3). A render of another state is not a read render of the named surface."
      },
      {
        "criterion": "RB14-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-14.boundary-parity.proof_of_spec.json@1df06e9112",
        "verdict": "FAIL",
        "reason": "'every dimension of the brief's IV.3 table reads the same on both sides, or the difference is an enumerated inverted band with its reason': 11 of 11 dimensions compared, and several differences are not bands: typeface (34 Inter elements on /market), radius (8px on 47/27/23 elements, 7/1/1 of them off the band), shadows (5/1/2 painting, the nav rail on 3 of 3, W1-S36), the loudest colour on 2 of 3 routes, and the focus ring's added 2px white gap."
      },
      {
        "criterion": "RB14-AC5",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-14.boundary-parity.proof_of_spec.json@1df06e9112",
        "verdict": "NOT_EVALUATED",
        "reason": "The walk was not performed and the site half of the pair is absent: 0 of 1 site renders, because a new capture of opalinvest.com is egress this order carries no word for (W1-S34). There is nothing to grade."
      },
      {
        "criterion": "RB15-AC5",
        "instance": "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-15.andrew-pack.proof_of_spec.json@1fb309e862",
        "verdict": "PASS",
        "reason": "MET WITH A NAMED QUALIFICATION: 3 of 3 routes paired at 1440 with no fixtures on either side, one self-contained HTML page (0 non-file requests) plus a composite, and a first screen stating what the pack does not show (rb-s-15_pack_composite read). Qualifications: 'same fixtures' holds as none on both sides, so neither half shows data; the /market BEFORE body is capture-timing-dependent and disclosed (W1-S38); the AFTER /portfolio-management file is named _pm_. The grade of FWD-9 itself is Andrew's and is not taken here."
      }
    ]
  },
  {
    "id": "DSGN_REBRND-C-S2",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1 L9: eighteen rows CLOSED inside the round -- by an amendment, a drain, an in-grant fix or a ruling (W2-S19 by Andrew's word, KEEP) -- each read against the artifact that closes it.",
    "class": "OBSERVATION",
    "spec_asserts": "Each row names what would close it: a collision measured gone (S1, W1-S31), a channel union at the drains (W1-S1, W2-S4, W2-S17), fonts shipped (W1-S5), a same-turn fix (W1-S7), a retired-and-replaced criterion (W1-S13, W1-S32), a fresh builder (W2-S10), canon restored (W1-S15), the identity set (W1-S19), Andrew's word on the rail edge (W2-S19: 'extended only by his word'), in-grant rewrites (W2-S13, W2-S14, W2-S16), a re-pin (W2-S12) and a tool fix (S4).",
    "world_is": "S1, W1-S31: RB9-AC7 PASS, 8 of 8 label/ornament pairs, 0 overlapping. W1-S1, W2-S4, W2-S17: the channel at a1d0a7451c parses 67 rows, 67 unique ids, duplicate_ids 0 (comp-surprise); W2-S12 and W2-S16 stand as distinct ids. W1-S5: portal/public/fonts holds lato-regular-400.woff2, lato-semibold-600.woff2 and OFL.txt, and RB2-AC6 measured both faces load same-origin (the 700 residual is W1-S8). W1-S7: fixed in its own commit; every later render parses the CSS. W1-S13, W1-S32: RB4-AC4 and RB10-AC2 retired for RB4-AC4R and RB10-AC2R by Amendment 1 (the TOs' expected sets carry the R ids). W2-S10: RB7-AC4 built by a fresh builder under Amendment 2. W1-S15: the ReturnVolatilityScatter benchmark colours restored to canon by Amendment 2 (RB4-AC5 evidence item 4). W1-S19: the sidebar active item and the avatar are identity sites by Andrew's word (PRD v0.5 FWD-4); RB5-AC5R counts them as such. W2-S19: RULED KEEP by Andrew-direct ~18:3xZ at the 2.0.0_SA_COO~D terminal (msg 96682, record org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_183xZ_DSGN_REBRND_ROUND2_DECISIONS_NAMED_LAYERS_STATE_RULE_PAGE_BY_PAGE_MARKET_FIRST.md @0e0e97f75a on CLOUD), item 4 verbatim: 'I like faint indigo edge on the sidebar, I honestly think that the original sidebar coloring/setup (on DEV Branch) was fine, will see what the current version looks like in the interim and make a call later if we keep it as is or just revert to the DEV branch implementation.' The rail's faint indigo edge extends FWD-4's closed identity set by one member by his word; the ratified v0.5 does not list it yet and the round-2 PRD addendum owes it (1.0.0_SA_CTO). The larger question he names -- keep the current sidebar or revert to the DEV implementation -- is OPEN at him and is not ruled here. W2-S13, W2-S14, W2-S16: rewritten in grant; RB8-AC5 5 of 5 supersessions, old-value census 0. W2-S12: the RB-s-7 instance reads VALID rc=0. S4: fixed @ed78c9c6c6 and @f7fe05777f, both on CLOUD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json@38f1c57663",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-2.typography-lato.proof_of_spec.json@cf406a823c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json@1794c79aef",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-8.archetype-rewrites.proof_of_spec.json@76afb991e3",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-4.ordered-scales.proof_of_spec.json@5072b24fad",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json@ed2aaccf85",
        "portal/public/fonts @portal 086371dd",
        "ed78c9c6c6 and f7fe05777f (CLOUD)"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-S1",
      "DSGN_REBRND-W1-S31",
      "DSGN_REBRND-W1-S1",
      "DSGN_REBRND-W2-S4",
      "DSGN_REBRND-W2-S17",
      "DSGN_REBRND-W1-S5",
      "DSGN_REBRND-W1-S7",
      "DSGN_REBRND-W1-S13",
      "DSGN_REBRND-W1-S32",
      "DSGN_REBRND-W2-S10",
      "DSGN_REBRND-W1-S15",
      "DSGN_REBRND-W1-S19",
      "DSGN_REBRND-W2-S19",
      "DSGN_REBRND-W2-S13",
      "DSGN_REBRND-W2-S14",
      "DSGN_REBRND-W2-S16",
      "DSGN_REBRND-W2-S12",
      "DSGN_REBRND-S4"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is closed in the artifact named above: measured, merged, amended or ruled inside the round. The ARMED rows among them (S1, W1-S1, W2-S4, W2-S17, W1-S5, W1-S7, W1-S13, W1-S32, W2-S10, W1-S15, W1-S19, W2-S19) stand INERT from this row. The one residual of W1-S5 (the SemiBold bold) is W1-S8, graduated in C-S6. W2-S19 is closed by Andrew's KEEP; what it leaves owed is the PRD addendum naming the sixth identity carrier (1.0.0_SA_CTO), and his open sidebar keep-or-revert call is not a remedy of this row.",
    "hazard_standing": "INERT"
  },
  {
    "id": "DSGN_REBRND-C-S3",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1 L9: eight rows that are RECORDS or accepted readings -- corrected premises, disclosed limits and one behaviour that is the platform's -- needing no remedy.",
    "class": "OBSERVATION",
    "spec_asserts": "Each row states a premise the world contradicted or a judgement call inside the grant: a count (W1-S2, W3-S2), a README mistaken for code (W2-S3), a wider edit than named (W1-S26), a ring on text-field clicks (W1-S28), an absent empty third (W1-S30), a timing-dependent BEFORE (W1-S38) and a retired rule still in the brief (W2-S18).",
    "world_is": "W1-S2, W3-S2: miscounted premises; the cells used the measured counts (22 literals; 24 routes, and RB12-AC4 PASSES on 24). W2-S3: zero code imported phosphor-react; RB11's census is unaffected. W1-S26: four changed lines in App.tsx inside the grant, needed to make the active item bold. W1-S28: 7 of 7 clicks into text fields paint the ring because browsers match :focus-visible on fields that take typing; that is correct platform behaviour, not a defect of the ring. W1-S30: populated routes run past the fold before and after (RB9-AC4). W1-S38: the pack discloses both captures. W2-S18: 1.0.0_SA_CTO's half is discharged by PRD v0.4 @4ebd24684b (FWD-4's SOURCE cites Andrew's word); the brief's O4 is 4.0.0_SA_CRO's L1 record of what was briefed, and the governing carrier of the budget is the PRD; the 6 in-grant sentences were updated.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/DSGN_REBRND.TO-RB-s-12.surface-inventory.proof_of_spec.json@80dfead12e",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-6.focus-visible.proof_of_spec.json@7a7364907b",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json@38f1c57663",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-15.andrew-pack.proof_of_spec.json@1fb309e862",
        "org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@4ebd24684b (CLOUD)",
        "1.0.0_SA_CTO msg 96664 item 3 (untracked inbox carrier)"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-W1-S2",
      "DSGN_REBRND-W2-S3",
      "DSGN_REBRND-W3-S2",
      "DSGN_REBRND-W1-S26",
      "DSGN_REBRND-W1-S28",
      "DSGN_REBRND-W1-S30",
      "DSGN_REBRND-W1-S38",
      "DSGN_REBRND-W2-S18"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Records and accepted readings: each is closed as stated above, and none names a remedy the next round needs. W2-S18's ARMED standing ends here: the PRD, not the brief, governs the accent budget, and the brief records what was briefed.",
    "hazard_standing": "INERT"
  },
  {
    "id": "DSGN_REBRND-C-S4",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1 L9, DECOMP_INVALIDATING: Option A's page inversion -- panels go light, one deliberate #0A1733 band per page -- is in the contract and applied to no page. Its remedy needs a cell granted portal/src/pages/**, which decomposition v1 does not contain.",
    "class": "BLOCKING",
    "spec_asserts": "Andrew's Option A (DESIGN.md C3; S2): every panel white with #0A1733 as one deliberate band per page; the committed inversion rule (design/brand/inversion-rule.json) and a per-role semantic re-derivation turn the light-on-dark idioms over.",
    "world_is": "4,887 light-on-dark idioms in 171 page files outside every round-1 grant (W1-S9), so 449 band instances stay dark and the band holds 73.9/45.6/48.3% of the pixels on /market, /positioning and /portfolio-management (RB14-AC4 evidence) against the site's 20-31%; 120 background-token ink sites in 20 page files render at 1:1 in dark (W1-S10); the token file still resolves contentPanel to the dark field (W2-S5); the inversion rule's worked examples sit on #101828, not #0A1733 (W2-S6); status tokens miss their contrast floors on the white panel the inversion makes the default ground (W2-S7); the #0A1733 sidebar is not marked .dark-band (W1-S27); C12 state wells paint white inside dark host panels (W1-S33). The pack's first screen says it: 'no cell of this round inverted the pages'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-3.canvas-surfaces.proof_of_spec.json@cf5a65f497",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-14.boundary-parity.proof_of_spec.json@1df06e9112",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/rb-s-15_pack_composite.png@a1d0a7451c",
        "Andrew-direct ~18:1xZ, msg 96669, org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_181xZ_DSGN_REBRND_CARD_TEXTURE_VARIANTS_AND_LIGHT_MODE_INVERSION_ARE_THE_TWO_CRUCIAL_WORKS.md@e7051143e2 (CLOUD)"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-S2",
      "DSGN_REBRND-W1-S9",
      "DSGN_REBRND-W1-S10",
      "DSGN_REBRND-W2-S5",
      "DSGN_REBRND-W2-S6",
      "DSGN_REBRND-W2-S7",
      "DSGN_REBRND-W1-S27",
      "DSGN_REBRND-W1-S33"
    ],
    "disposition": "DECOMP_INVALIDATING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO, the seat that re-decomposes DSGN_REBRND for round 2: DISARMS when a cell granted portal/src/pages/** applies the committed inversion rule and the per-role semantic re-derivation. Andrew-direct ~18:1xZ (msg 96669, record @e7051143e2 on CLOUD) names the light-mode inversion's state rule CRUCIAL, priority 2 of 4."
  },
  {
    "id": "DSGN_REBRND-C-S5",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1, GRADUATED: the four designed states do not yet cover the product -- failures drawn as data (W3-S4), NO-PERMISSION unwired (W3-S1), a dozen stray treatments (W3-S5) -- and the render record shows 23 of 96 surfaces in another state than named (W3-S3); upload drop zones are unreachable by keyboard (W3-S6).",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-11: empty, loading, error and no-permission are four designed states and every panel uses one; never an error on the bare page. FWD-5: tabbing through any route, the advisor always sees which element is focused.",
    "world_is": "RB10-AC5, RB13-AC4 FAIL (C-S1). W3-S4: under 503, a live 401 or held requests, seven routes draw data, EMPTY or LOADING where C12 requires ERROR; rb-s-10_market_error_1440 shows '50 Neutral' and RSI bars with every request failing. W3-S1: every access denial found is non-rendering. W3-S5: bare spinners, 'Loading...' lines, red text on the canvas with raw codes on eight routes. W3-S3: 65 of 96 renders show their named state; rb13-coverage-check reads COVERED 96 of 96 because it checks that a PNG exists. W3-S6: drop zones on /data-refresh and /trade-submission never take focus.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-10.four-states.proof_of_spec.json@bccea536d0",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~3/DSGN_REBRND.TO-RB-s-13.render-coverage.proof_of_spec.json@7333b9c5a1",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/rb-s-10_market_error_1440.png@a1d0a7451c"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-W3-S4",
      "DSGN_REBRND-W3-S1",
      "DSGN_REBRND-W3-S5",
      "DSGN_REBRND-W3-S3",
      "DSGN_REBRND-W3-S6"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1): DISARMS when a forced-failure render of each of the seven W3-S4 routes shows ERROR where data is absent; until then /market shows a '50 Neutral' reading during an outage."
  },
  {
    "id": "DSGN_REBRND-C-S6",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1, GRADUATED: the accent budget and colour roles as rendered -- no primary action on 2 of 3 routes (W1-S20), the RSI bars an ordered scale in four hues and the loudest colour on /market (S3), a reversed legend (W2-S11), off-token gain/loss colours (W1-S37), multi-writer colour families (W1-S4, W1-S14), stale model names (W1-S16) and a SemiBold bold (W1-S8, at Andrew).",
    "class": "OBSERVATION",
    "spec_asserts": "PRD v0.5 FWD-4 (one persistent primary action plus the closed identity set, 'extended only by his word'); FWD-3 (every ordered quantity one hue ramped); FWD-7 (status and data colour two token systems); FWD-6 (one writer); FWD-2 (Lato at the weights the website ships, 400/700).",
    "world_is": "RB5-AC5R (C-S14) and RB4-AC5 (C-S1) FAIL. Persistent actions 0/1/0 (W1-S20). RSIBars.tsx:140-155 colours RSI by value band through four hue families (S3). Legend vs data.assetClass reversed (W2-S11). 270 figure nodes in #2DCE89/#F5365C, in no token family (W1-S37). --model-* vs modelPortfolioColors.ts disagree (W1-S4); four writers of the ladder (W1-S14); aum.ts keys the earlier model names (W1-S16). Weight 700 served by the SemiBold face (W1-S8).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json@ed2aaccf85",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-4.ordered-scales.proof_of_spec.json@5072b24fad",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-2.typography-lato.proof_of_spec.json@cf406a823c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-14.boundary-parity.proof_of_spec.json@1df06e9112",
        "portal/src/components/market-performance/RSIBars.tsx:140-155 @portal 086371dd"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-W1-S20",
      "DSGN_REBRND-S3",
      "DSGN_REBRND-W2-S11",
      "DSGN_REBRND-W1-S37",
      "DSGN_REBRND-W1-S4",
      "DSGN_REBRND-W1-S14",
      "DSGN_REBRND-W1-S16",
      "DSGN_REBRND-W1-S8"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1): DISARMS W1-S14 and W1-S4 when each colour family has one writer; W1-S8's bold is Andrew's word (a fetch) or a supplied file."
  },
  {
    "id": "DSGN_REBRND-C-S7",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1, GRADUATED: the contract and its token chain are not yet one byte-equal system -- no non-colour token blocks (W2-S9), an unreproducible generated CSS (W1-S3), a rounded band-ring value (W1-S25), no ring token and a ring unlike the site's (W1-S22), and no page-terminator clause (W1-S29).",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-6 PROOF: the contract and the token files it governs agree byte-for-byte on every value the contract names; the three token writers are one. FWD-5: the ring the website ships. FWD-10: a short page ends with a designed statement that it has ended.",
    "world_is": "The token file has no typography, spacing, radius or grid block (W2-S9); opal-capital.css does not reproduce from its generator (W1-S3); the band ring renders #E6EAF4 against DESIGN.md's #E8ECF5 (W1-S25); C11 defines a two-layer ring and no ring token exists (W1-S22); DESIGN.md has 0 terminator clauses and RB9-AC5 FAILS on it (W1-S29). RB7-AC4's build record lists 32 questions the contract did not answer (C-S1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json@1794c79aef",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-9.density.proof_of_spec.json@38f1c57663",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-6.focus-visible.proof_of_spec.json@7a7364907b",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-1.token-spine.proof_of_spec.json@cc480cc723"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-W2-S9",
      "DSGN_REBRND-W1-S3",
      "DSGN_REBRND-W1-S25",
      "DSGN_REBRND-W1-S22",
      "DSGN_REBRND-W1-S29"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "INERT"
  },
  {
    "id": "DSGN_REBRND-C-S8",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1, GRADUATED: boundary parity and stale carriers -- painting shadows the contract forbids (W1-S36), FWD-1's walk with no site half (W1-S34, egress), the retired silver law still in four auto-read carriers (W2-S15, W1-S24), retired chart libraries in vite.config (W2-S2) and TopicCloud as FWD-8's unruled exception (W2-S1).",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-1 (one system across the boundary; the archetype documents rewritten in place, never left standing); FWD-8 (one charting library; a chart that cannot migrate is a surprise row, not a quiet exception).",
    "world_is": "RB14-AC4 FAIL and RB14-AC5 NOT_EVALUATED (C-S1). Shadows paint on 5/1/2 elements (W1-S36). 0 of 1 site renders; a capture is egress (W1-S34). panels/README.md, TicketCenter.tsx, designTokens.ts and TicketCenter.tsx:174 state the 2026-07-15 law (W2-S15, W1-S24). manualChunks names vendor-apexcharts and vendor-nivo (W2-S2). TopicCloud keeps @visx (W2-S1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-14.boundary-parity.proof_of_spec.json@1df06e9112",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-8.archetype-rewrites.proof_of_spec.json@76afb991e3",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-11.one-renderer.proof_of_spec.json@46495a26a9"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-W1-S36",
      "DSGN_REBRND-W1-S34",
      "DSGN_REBRND-W2-S15",
      "DSGN_REBRND-W1-S24",
      "DSGN_REBRND-W2-S2",
      "DSGN_REBRND-W2-S1"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO (DSGN_REBRND round-2 cut; 2.0.0_SA_COO~D held round 1) for W2-S15 and W1-S24 (the retired law still stated in auto-read carriers) when a cell that grants them rewrites them; 1.0.0_SA_CTO for W2-S1's FWD-8 ruling."
  },
  {
    "id": "DSGN_REBRND-C-S9",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1, GRADUATED to rulings: two standing words cannot both hold as written -- three locked canon hexes are below 3:1 on the white panel (W2-S8), and no accent hue satisfies both of the dark mode's accent roles at 4.5:1 (W1-S11). Arithmetic, not tuning.",
    "class": "OBSERVATION",
    "spec_asserts": "The canon lock ('no act of this order may move' the five); the WCAG 2.1 SC 1.4.3 / 1.4.11 bar the PRD pins independently of the contract.",
    "world_is": "W2-S8: three of five canon hexes measure below 3:1 against #FFFFFF. W1-S11: white-on-accent needs relative luminance <= 0.1833 and accent-on-band needs >= 0.2002; an exhaustive search over hue 240-265, saturation 40-100%, lightness 30-85% returns 0 values. RB3-AC7 FAILS on the three dark-mode accent pairs (C-S1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-3.canvas-surfaces.proof_of_spec.json@cf5a65f497",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-7.the-contract.proof_of_spec.json@1794c79aef"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-W2-S8",
      "DSGN_REBRND-W1-S11"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO, putting both to Andrew: DISARMS when he rules the canon-lock versus contrast-bar conflict (W2-S8) and which role the dark-mode accent drops (W1-S11)."
  },
  {
    "id": "DSGN_REBRND-C-S10",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "ROUND-1, GRADUATED: the issuer's cut-defect class -- a check whose domain differs from its claim, or a face that differs from its order: a pipeline rc that is head's (W1-S6), a pattern that crosses lines (W1-S12), a canon checker blind to the canon (W1-S17), a criterion already green at the base (W1-S18), a key count read as a route count (W1-S35), a face with a clause its order lacks (W1-S21) and a cited row that does not exist (W1-S23).",
    "class": "OBSERVATION",
    "spec_asserts": "Spine L7: the worker face is the worker's whole context, one clause per criterion with its invocation and expectation; a criterion must be able to fail on the defect it names.",
    "world_is": "Seven rows, each measured by the worker that met it; each checker's miss is stated with its arm. The same shape recurs on MODIFIED orders (RB4-AC4, RB5-AC4, RB10-AC2, RB13-AC2, per the drain-end's item 4), which no gate grades because LIMB 6 and the other limbs read NEWLY-ADDED orders only (CLAUDE.md Rule 27).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/investigations/INVESTIGATION_v1.md@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-2.typography-lato.proof_of_spec.json@cf406a823c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-3.canvas-surfaces.proof_of_spec.json@cf5a65f497",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-4.ordered-scales.proof_of_spec.json@5072b24fad",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json@ed2aaccf85",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/DSGN_REBRND.TO-RB-s-14.boundary-parity.proof_of_spec.json@1df06e9112"
      ]
    },
    "adjudicates": [
      "DSGN_REBRND-W1-S6",
      "DSGN_REBRND-W1-S12",
      "DSGN_REBRND-W1-S17",
      "DSGN_REBRND-W1-S18",
      "DSGN_REBRND-W1-S35",
      "DSGN_REBRND-W1-S21",
      "DSGN_REBRND-W1-S23"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D (issuer of the round-1 faces and checkers): DISARMS when each named checker reads its failing verdict on its base tree at the cut; the three ARMED rows (W1-S6, W1-S12, W1-S17) are checkers a re-cut would otherwise reuse."
  },
  {
    "id": "DSGN_REBRND-C-S11",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "CVO OBSERVATION: the Fear & Greed state label ('Neutral') on /market is painted in the accent #5F3BE3 -- an accent carrier outside FWD-4's closed identity set that no row names; the issuer's drain-end item 5 raised it as a lead and this seat confirmed it on the render.",
    "class": "OBSERVATION",
    "spec_asserts": "PRD v0.5 FWD-4 (@01378b0a5b) and RB5-AC5R: the accent is spent on ONE persistent primary action plus the five named identity sites AND NOWHERE ELSE.",
    "world_is": "rb-s-5r_market_1440.png (0.9.0_WK_DSGN_REBRND~2, the reopen's final /market render) shows the Fear & Greed value '50' with its state label 'Neutral' in the indigo accent beneath it; the same label renders in the accent in rb-s-10_market_error_1440. It is neither an action nor one of the five sites.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/rb-s-5r_market_1440.png@a1d0a7451c",
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~1/rb-s-10_market_error_1440.png@a1d0a7451c",
        "2.0.0_SA_COO~D drain-end msg 96663 item 5 (untracked inbox carrier)"
      ]
    },
    "disposition": "GRADUATED",
    "hazard_standing": "INERT"
  },
  {
    "id": "DSGN_REBRND-C-S12",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "CVO OBSERVATION: portal/DESIGN.md's front matter names token values with NO class label -- 0 'class:' keys, 0 'derived', 0 'preserved' -- where the CONTRACTS clause requires every value named WITH ITS CLASS (fixed / measured / preserved / derived) and every derived value's rule beside it.",
    "class": "OBSERVATION",
    "spec_asserts": "PRD CONTRACTS, DesignContract row: 'YAML front matter naming every token value WITH ITS CLASS (fixed / measured / preserved / derived)'; the preamble: 'A derived value is never labelled captured: its derivation rule is written beside it in the contract'.",
    "world_is": "portal/DESIGN.md @portal 086371dd: 454 lines; the front matter's colors block lists 15 palette values as bare hex with comments; word counts over the whole file: fixed 1, measured 7, preserved 0, derived 0; 'class:' keys 0. The issuer's drain-end item 5 raised it (from RB-s-7).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/DESIGN.md @portal 086371dd (feature/d13-visual-elevation), read by this seat",
        "2.0.0_SA_COO~D drain-end msg 96663 item 5 (untracked inbox carrier)"
      ]
    },
    "disposition": "GRADUATED",
    "hazard_standing": "INERT"
  },
  {
    "id": "DSGN_REBRND-C-S13",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "CVO OBSERVATION: feature/d13-visual-elevation carries the PRD at v0.2 while the ADMITTED text is v0.5 on CLOUD (@01378b0a5b); this round was graded against v0.5, and a round-2 cut read from the branch would grade FWD-4 against the one-accent text Andrew replaced.",
    "class": "OBSERVATION",
    "spec_asserts": "2.0.0_SA_COO~D drain-end 96663 item 1: 'PRD v0.5 is ADMITTED'; the spine's L10 recut reads the PRD the CTO holds.",
    "world_is": "On the branch at a1d0a7451c, org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md reads prd_version v0.2 and FWD-4 names one persistent primary action only; on CLOUD @01378b0a5b it reads v0.5 with the closed identity set and the DERIVED classes. The two texts differ in FWD-4 and the CONTRACTS preamble.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@a1d0a7451c (v0.2)",
        "org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@01378b0a5b on CLOUD (v0.5)"
      ]
    },
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO: DISARMS when the round-2 issuance names the governing PRD text (v0.5 on CLOUD) or the admitted PRD is brought onto the branch."
  },
  {
    "id": "DSGN_REBRND-C-S14",
    "project": "DSGN_REBRND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T18:50:08Z",
    "one_line": "CVO OBSERVATION, AND THE CARRIER OF ONE GRADE: RB5-AC5R -- FAIL. The investigation schema's grades[].criterion pattern '^[A-Za-z0-9]+-AC[0-9]+$' refuses an amended criterion id, so this verdict cannot ride C-S1's `grades`; it is stated here, and the id is not renamed to fit.",
    "class": "OBSERVATION",
    "spec_asserts": "org/surprise_channel/schemas/investigation_item.schema.json grades.items.criterion: 'the criterion id as the task order names it ... the same string the proof-of-spec instance's acceptance row carries, so the grade and the row it grades resolve to one id', pattern '^[A-Za-z0-9]+-AC[0-9]+$'.",
    "world_is": "DSGN_REBRND's reopened RB-s-5 (Amendment 1, @3b45dfb5e3) retired RB5-AC5 for RB5-AC5R, and the governing instance carries RB5-AC5R; 21 of 22 judgment ids in this round match the pattern and RB5-AC5R does not. Renaming it would grade an id no instance row carries. THE VERDICT, FAIL: Against Andrew's budget (PRD v0.5 FWD-4 @01378b0a5b). (1) Exactly ONE persistent primary ACTION per route: NOT MET, 0/1/0 on /positioning, /portfolio-management, /market, and PM's sits in a band (W1-S20). (2) Identity accents at the five sites AND NOWHERE ELSE: NOT MET. Sites 4/5/5 (/positioning has no tabs), and the Fear & Greed 'Neutral' label is painted in the accent in rb-s-5r_market_1440 (C-S11), a carrier outside the set. NAMED QUALIFICATION, not counted as a violation: the rail's faint accent border-image on 3 of 3 routes (W2-S19) is a sixth persistent identity carrier, admitted by Andrew's word at ~18:3xZ (msg 96682, record @0e0e97f75a on CLOUD: 'I like faint indigo edge on the sidebar'); ratified v0.5 does not list it yet, and the round-2 PRD addendum owes it (1.0.0_SA_CTO's). (3) No filled accent chip per option: MET. Sidebar active item legible with its fill ignored: MET (App.tsx:192). Favicon an indigo sphere with the white mark: MET (rb-s-5r_favicon_32_x8 read). (4) No off-palette colour loudest on any page: NOT MET on /market, the lime RSI bars. Instance: org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json@ed2aaccf85.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_REBRND/deliverables/0.9.0_WK_DSGN_REBRND~2/DSGN_REBRND.TO-RB-s-5.accent-controls.proof_of_spec.json@ed2aaccf85",
        "org/surprise_channel/schemas/investigation_item.schema.json properties.grades.items.criterion.pattern",
        "org/missions/D13/DSGN/DSGN_REBRND/task-orders/DSGN_REBRND.TO-RB-s-5.accent-controls.md@a1d0a7451c <expected_criteria>"
      ]
    },
    "disposition": "GRADUATED",
    "hazard_standing": "INERT"
  }
]
```
