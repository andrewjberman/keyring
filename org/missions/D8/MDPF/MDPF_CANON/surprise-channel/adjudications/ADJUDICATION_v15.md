# MDPF_CANON -- rounds 7 and 9 L9: five judgments read, 26 rows dispositioned (dell1)

<sweep_watermark>2026-10-15T14:12Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T14:20:00Z. Packet: 2.0.0_SA_COO~D1 msg 6032, `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/ROUND9_DRAIN_END.md @9b61aca787 (blob ade99b928959)`.

**L9:** CN-p-1 AC4 MET (D1-C-S81); CN-h-1 AC4 MET (D1-C-S82); CN-j-1 AC4 NOT MET (D1-C-S83, which also corrects v14); CN-p-2 AC4 HELD (D1-C-S84); CN-l-2 AC3 HELD (D1-C-S85). No slug: both rounds still hold one judgment each.
**Rows:** 26 of 26 since the 2026-10-14T16:05Z watermark: 3 graduated to REMEDIATION_v8 (D1-S27 closed), 23 dismissed.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S81",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:20:00Z",
    "one_line": "ROUND 9 L9: JUDGMENT MDPF_CANON.TO-CN-p-1 AC4 MET on the first scheduled gold run carrying the code (13:31Z, pin 8e2dd0fb36): Trend-groups readback 11 of 11 and seams 7 of 7, run by this seat.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-p-1 AC4 (judgment): /seams on the producer-to-served seam, grounded on the objects after the first scheduled run that carries the code -- MECHANICAL, DECLARATIVE, SEMANTIC as the order states.",
    "world_is": "ROUND 9 L9, JUDGMENT MDPF_CANON.TO-CN-p-1 AC4: MET. Packet org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/ROUND9_DRAIN_END.md @9b61aca787 (blob ade99b928959), msg 6032. This seat ran org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_trend_groups_readback.py read --pin 8e2dd0fb369043d5f23dca2d02dba7d51cfabd6f at ~14:05Z: 11 of 11. MECHANICAL: R1 Global carries the four keys aligned to 497 dates with carried_dates a sorted subset; R2 the three firm scopes all-None and []; R6 against the prior dated object only the four keys are added and none dropped, with one restated cell per array on four arrays (the newest shared date, within the order's five-cell tolerance). DECLARATIVE: R8 meta.trend_groups names the SMArtX partition read 2026-10-15, 1,285 dates and the 2026-05-18 boundary; R7 no scope's SMA > ALT Strategies lists 'Muni SMA'. SEMANTIC: the client-visible deltas are the four keys and Muni leaving ALT, the two the never-widen pair names (R6, R7, R10 disjoint from the CN-h-1 count fields); R9 the manifest errors are empty and the run's commit equals the pin. The fail-open the first pass built (D1-W26-S2) is closed: this seat's r9_cn_p_1.py seams reads S7 PASS (a loader raise leaves Global None and the other scopes kept, and the grader rejects the or-fallback wiring). Limit: R11 found the Dividend, Growth and SMA legs present on both rows, so the packet's candidate (a), a missing leg read as zero on a total-bearing row, was not exercised by this run; it stays a candidate for the CTO's analysis.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_trend_groups_readback.py read --pin 8e2dd0fb369043d5f23dca2d02dba7d51cfabd6f: R9 TREND-GROUPS READBACK: 11 of 11 arms",
        "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_1.py seams: CN-P-1 SEAMS: 7 of 7 arms (S7 PASS)",
        "task-orders/MDPF_CANON.TO-CN-p-1.producer-global-sma-clientsup-carried.md:221 (AC4 text)",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/ROUND9_DRAIN_END.md @9b61aca787 (blob ade99b928959)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: AC4 MET; not a hazard."
  },
  {
    "id": "MDPF_CANON-D1-C-S82",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:20:00Z",
    "one_line": "ROUND 7 L9: JUDGMENT MDPF_CANON.TO-CN-h-1 AC4 MET on the 2026-10-15 scheduled gold run: frontier readback 7 of 7, run by this seat; the staleness stamp reads FRESH where the order keeps one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-h-1 AC4 (judgment): /seams on the loader-to-served seam, grounded on the objects after the first scheduled run that carries the code -- MECHANICAL, DECLARATIVE, SEMANTIC as the order states.",
    "world_is": "ROUND 7 L9, JUDGMENT MDPF_CANON.TO-CN-h-1 AC4: MET. This seat ran org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_frontier_readback.py read at ~14:05Z on the 2026-10-14 objects against 2026-10-13: 7 of 7. MECHANICAL: F1 every overridden key equals the 2026-10-14 A4 map (Global 5 of 5 compared, 49 Financial 5 of 5, Inflection 7 of 7; none equal to staged and not A4); F2 Global account_count_total[-1] 8701 equals its composition (prior 8264, +437), 49 Financial 7488 (+344), Inflection 565 (+17). DECLARATIVE: F4 the 49 Financial stamp names as_of 2026-10-14 = the A4 period and reads FRESH; Global and Inflection carry no meta.frontier_count stamp, as before, and the order forbids adding one (order lines 64-65, 102), so that is the order's scope, not a miss. SEMANTIC: F3 22,005 other cells and F6 7,335 cells equal the prior object, so the client-visible deltas are the frontier counts and the rows that follow them; F5 the deployed loader names no staged key. The pair's predicted Global count (near 8695) is replaced by the read 8701; the difference is the A4 map's, not the loader's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_frontier_readback.py read: ROUND 7 READBACK: 7 of 7 arms",
        "task-orders/MDPF_CANON.TO-CN-h-1.frontier-counts-read-the-a4-distribution.md:132-135 (AC4 text), :64-65 and :102 (the stamp is not to change)",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/ROUND9_DRAIN_END.md @9b61aca787 (blob ade99b928959)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: AC4 MET; not a hazard."
  },
  {
    "id": "MDPF_CANON-D1-C-S83",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:20:00Z",
    "one_line": "ROUND 7 L9: JUDGMENT MDPF_CANON.TO-CN-j-1 AC4 NOT MET: the history leaf is served and correct (9 of 9), but no portal code reads it, so the Trend's Client chips draw on the as-of date only, not on the leaf's dates. Also corrects ADJUDICATION_v14.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-j-1 AC4 (judgment): /seams on the leaf-to-chip seam -- SEMANTIC: 'the Trend's Client chips draw on the leaf's dates and are absent, never zero, on every other date'.",
    "world_is": "ROUND 7 L9, JUDGMENT MDPF_CANON.TO-CN-j-1 AC4: NOT MET, on the SEMANTIC arm. MECHANICAL and DECLARATIVE hold: this seat's r7_history_readback.py read on the 13:50Z scheduled run (manifest 20261015T135048Z-5a1d60b7) reads 9 of 9 -- the four keys exist, each leaf equals its scope's dated nodes (198 cells, 0 mismatch), the 18 pair leaves equal gold, and the header, omitted dates and provenance keys are present. The session-holding GET through /api/general/mdpf/<scope>/category-views-history.json was not read by anyone (the deploy ledger's leg L5 read 401 without a session); edge v24 is live on 27 of 27 associations (this seat's get-distribution-config read). SEMANTIC FAILS: on portal origin/PROD c3b21a40e2 and origin/DEV ad7c100b5c, git grep finds no reader of category-views-history in src/ (0 hits in each); the only category-views reader is getCategoryViewsByFirm (src/api/endpoints/aum.ts:1029, the latest object). The chip rule on PROD is clientChipAt (src/lib/trendGrouping.ts:97-109): a chip carries its value only when the category-views as-of equals the period, so a chip draws on ONE date. It is absent, never zero, on every other date, but the leaf the order built has no consumer. Whether the chips still need the leaf after PRD v2.21 (b), which draws Client Supervised on Global from the CN-p-1 arrays, is the CTO's call at the round-N analysis; graded here against the criterion's text. CORRECTION to ADJUDICATION_v14 (row D1-C-S80): it said src/lib/trendGrouping.ts is absent on DEV and that the CN-i-2 Trend had not landed. Both are wrong. trendGrouping.ts is present on origin/DEV and origin/PROD, and the Trend landed through CN-p-2 (PROD c3b21a40e2; DEV merge e0b033253b, an ancestor of ad7c100b5c). Only the commit fd5433a3 itself is not an ancestor; v14 read the diff line count as an absence. v14's hold reasons (2) and (3) are replaced by this grade.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_history_readback.py read: ROUND 7 HISTORY READBACK: 9 of 9 arms",
        "portal: git grep -n -E 'category-views-history|categoryViewsHistory' origin/PROD -- src and origin/DEV -- src: 0 hits each (fetched ~14:05Z)",
        "portal origin/PROD:src/lib/trendGrouping.ts:97-109 clientChipAt; origin/PROD:src/api/endpoints/aum.ts:1029",
        "portal: git cat-file -e origin/DEV:src/lib/trendGrouping.ts succeeds (the v14 correction)",
        "aws cloudfront get-distribution-config --id EVTSA9VEHNZVH: auth-validator-edge:24 on 27 of 27 associations",
        "task-orders/MDPF_CANON.TO-CN-j-1.category-views-history-leaf.md:144-148 (AC4 text), :21-23 (the rule the leaf serves)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: AC4 NOT MET; the unconsumed leaf goes to the CTO's round-N analysis with the slug. Not a hazard: nothing wrong is served."
  },
  {
    "id": "MDPF_CANON-D1-C-S84",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:20:00Z",
    "one_line": "ROUND 9: MDPF_CANON.TO-CN-p-2 AC4 HELD. The criterion asks for a render of an internal session and of a demo-tenant claim set; only the internal one was made, and it was not kept anywhere this seat can read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-p-2 AC4 (judgment): the issuer renders the Global Trend at a STATED portal commit on bun run dev:live --port 5174 for an internal session and for a demo-tenant claim set, against the producer's deployed arrays and the spec's oracle.",
    "world_is": "ROUND 9, MDPF_CANON.TO-CN-p-2 AC4 HELD -- not graded. The packet's section 3 walked the internal session only and kept local screenshots, which this seat cannot read. It names the limit 'no partner or demo login exists', but the criterion asks for a demo-tenant CLAIM SET, not a login; the unit arms V1-V12 run on fixtures and AC2 already covers that ground, so they cannot stand in for the render. This seat read the PROD code (c3b21a40e2): src/pages/ModelPortfolios.tsx:385-389 sets trendMode from internal = isInternal() || isDev(), and :451-464 fetch the 49 Financial and Inflection series only when effectiveFirmId is 'global' and internal. So a non-internal session draws Variant 2 and never fetches a single-firm leaf -- the gate is right in code. The render is what the criterion grades, and the demo tenant is the audience this seat's v2.19 refusal turned on. To grade: render the Global Trend at a stated commit for an internal session and for a claim set with firmId 'demo' that is neither internal nor dev (isDev() would force Variant 1 on a dev build), and keep both renders as files at a path this seat can read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "packet section 3 (org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/ROUND9_DRAIN_END.md @9b61aca787 (blob ade99b928959))",
        "portal origin/PROD:src/pages/ModelPortfolios.tsx:385-389 and :451-464",
        "task-orders/MDPF_CANON.TO-CN-p-2.portal-variant1-trend-stitch-and-approved-edits.md:99 (AC4 text)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hold record: AC4 is graded on the two renders; not a hazard (the gate is right in code)."
  },
  {
    "id": "MDPF_CANON-D1-C-S85",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:20:00Z",
    "one_line": "ROUND 7: MDPF_CANON.TO-CN-l-2 AC3 HELD. No render of the Other Models card at a stated commit is in the packet; the served object reads the pool-present branch (no as_of key).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-l-2 AC3 (judgment): the issuer renders the Model Portfolios page on bun run dev:live --port 5174 at a STATED portal commit, and the CVO reads the Other Models card against the rule.",
    "world_is": "ROUND 7, MDPF_CANON.TO-CN-l-2 AC3 HELD -- not graded. The packet's section 4 reads the served Global aum-metrics Other Models row (account_count 211, aum $68.9M, no as_of key), the pool-present branch, and section 3's walk names the Trend only. On a pool-present day the rule is 'no extra line', which only a render shows. To grade: one render of the Other Models card at a stated portal commit, kept as a file this seat can read. The carried and no-pool branches stay graded by the offline arms, as the packet says.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "packet sections 3 and 4 (org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/ROUND9_DRAIN_END.md @9b61aca787 (blob ade99b928959))",
        "task-orders/MDPF_CANON.TO-CN-l-2.other-models-as-of-card.md:110-112 (AC3 text)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hold record: AC3 is graded on the render; not a hazard."
  },
  {
    "id": "MDPF_CANON-D1-C-S86",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:20:00Z",
    "one_line": "GRADUATED to REMEDIATION_v8: D1-S27 (edge firm scoping; REMEDIATED by CN-q-1, closed), D1-S25 (Client card vs drill-down, OPEN, 2.0.0_SA_COO~D1), D1-S26 (round-close-check first-verdict read, OPEN, 0.0.0_AB_MSTR~DELL1).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S27",
      "MDPF_CANON-D1-S25",
      "MDPF_CANON-D1-S26"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to REMEDIATION_v8. D1-S27 (ARMED): per-firm MDPF leaves were reachable by any login. CN-q-1's edge gate is live: this seat read auth-validator-edge:24 on 27 of 27 associations of EVTSA9VEHNZVH, and an unauthenticated GET of /api/general/mdpf/49financial/category-views-history.json answers 401. The order's record has the deployed-bundle replay at 14 of 14, with a v23 negative control that fails A5-A7, and an internal login reading a foreign-firm leaf 200. Limit, carried in the remediation: a live foreign-firm 403 is unproven, since no partner login exists. REMEDIATED, DISARMED, closed. D1-S25 (INERT, client-facing): the Client card reads $292.26M against a $341.10M drill-down. Not re-read on the CN-p-2 page; OPEN to 2.0.0_SA_COO~D1. D1-S26 (INERT): round-close-check returns the first CVO verdict in string-sorted files, so a re-grade cannot replace a NOT MET. OPEN to 0.0.0_AB_MSTR~DELL1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws cloudfront get-distribution-config --id EVTSA9VEHNZVH (~14:10Z): auth-validator-edge:24 x27, no other version",
        "curl https://opalinvest.dev/api/general/mdpf/49financial/category-views-history.json: 401",
        "packet section 2 (CN-q-1 ledger fac3025ca7)",
        "investigation rows MDPF_CANON-D1-S25, D1-S26, D1-S27"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "MDPF_CANON-D1-C-S87",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:20:00Z",
    "one_line": "DISMISSED: 13 rows of the superseded round-8 order CN-i-2/CN-i-3 (D1-W24-S1..S4, D1-W25-S1..S9). Its candidate 19494a76 never landed; the Trend landed through CN-p-2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W24-S1",
      "MDPF_CANON-D1-W24-S2",
      "MDPF_CANON-D1-W24-S3",
      "MDPF_CANON-D1-W24-S4",
      "MDPF_CANON-D1-W25-S1",
      "MDPF_CANON-D1-W25-S2",
      "MDPF_CANON-D1-W25-S3",
      "MDPF_CANON-D1-W25-S4",
      "MDPF_CANON-D1-W25-S5",
      "MDPF_CANON-D1-W25-S6",
      "MDPF_CANON-D1-W25-S7",
      "MDPF_CANON-D1-W25-S8",
      "MDPF_CANON-D1-W25-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED. TO-CN-i-2 reads status superseded (round 8). Portal 19494a76, the CN-i-3 candidate the W25 rows describe, is in neither origin/DEV nor origin/PROD (merge-base read ~14:12Z). The landed Trend is CN-p-2's (PROD c3b21a40e2, CI run 38667132776 success). The seven ARMED rows (W25-S1..S6 and S8) each name a site left unedited, or a stale order file, in a candidate that will not land. Their disarm condition, 'refuse portal 19494a76 as the CN-i-3 candidate', holds by supersession. W24-S3 (ARMED): the workspace commit gate reads no .ts/.tsx file. Portal files are graded by VALGATE on every push and by portal CI; the danger-map staleness it names is not this project's. W24-S1, S2, S4, W25-S7 and S9 are INERT face notes on the superseded order.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/MDPF_CANON.TO-CN-i-2.aua-trend-repair-colour-tooltip-note.md <status>superseded</status>",
        "portal: git merge-base --is-ancestor 19494a76 origin/DEV and origin/PROD: not an ancestor of either",
        "packet section 2 (CN-p-2 PROD promote)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The order is superseded and its candidate never landed; the portal file gap is covered by VALGATE and CI at push."
  },
  {
    "id": "MDPF_CANON-D1-C-S88",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-15T14:20:00Z",
    "one_line": "DISMISSED: 10 round-9 rows (D1-W26-S1..S4, D1-W27-S1..S4, D1-W28-S1, D1-S28). The one ARMED row, W26-S2 (fail-open), is closed by amendment 1, which this seat's S7 run proves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W26-S1",
      "MDPF_CANON-D1-W26-S2",
      "MDPF_CANON-D1-W26-S3",
      "MDPF_CANON-D1-W26-S4",
      "MDPF_CANON-D1-W27-S1",
      "MDPF_CANON-D1-W27-S2",
      "MDPF_CANON-D1-W27-S3",
      "MDPF_CANON-D1-W27-S4",
      "MDPF_CANON-D1-W28-S1",
      "MDPF_CANON-D1-S28"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED. W26-S2 (ARMED): a failed SMArtX read fell back to empty legs. AMENDMENT 1 closed it, and this seat's r9_cn_p_1.py seams reads S7 PASS: a loader raise leaves Global None, keeps the other scopes, and makes no apply call. The scheduled run is green (R9, errors []). W28-S1 (BLOCKING): the LGIC limb refused firm-name literals in mdpf_gate.mjs; the order was re-cut on the CRO's generator 1fc3358292 and merged at 643932fee0. S28: auth-validator-edge version 23 shows an unexplained LastModified, but its CodeSha256 equals the L1 print and CloudTrail lists no other write, so the rollback proof holds. INERT notes: W26-S1 and W26-S4 (an eight-line comment and LF endings, each handled as found); W27-S1 (the plottedKeys filter, fixed in the order, checked by W3); W27-S3 (Inflection's Custom series read as the cohort rule). Candidates for the CTO's round-N analysis, not defects of the merged code: W27-S2 (the composition footnote also shows on internal per-firm views) and the stale comments of W26-S3 and W27-S4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_1.py seams: S7 PASS",
        "packet sections 1, 2 and 5 (org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/ROUND9_DRAIN_END.md @9b61aca787 (blob ade99b928959))",
        "investigation rows D1-W26-S1..S4, D1-W27-S1..S4, D1-W28-S1, D1-S28"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is closed by the merged order or is a note with no served effect; W27-S2, W26-S3 and W27-S4 travel as enrichment candidates."
  }
]
```
