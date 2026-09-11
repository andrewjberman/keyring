# IRPT_FNTEND — round 1 adjudication

Author: 3.0.0_SA_CVO. Round: v1. Fabric: laptop. Recorded: 2026-09-11T10:56:02Z.

Input snapshot: workspace `eb6f7068db3da5bc67bfb7567d5a13ccdb32447b`; portal `edab15b54f8fd2e2c3da2eaed87dd64a215785c9`. Investigation: `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525`. 41 of 41 original items CVO-checked; zero undispositioned. 11 of 11 instances structurally VALID. All 10 judgment criteria graded against their issued faces. These are L9 criterion grades, not CTO outcome grades.

Review and primary-source inventory: [IRPT_ROUND1_L8_REVIEW_20260911.md](/org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md); independent measurements: [IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json](/org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json). References marked “same commit” bind to this document’s commit. Original row citations bind to the channel pin above; worker prose such as “this commit” is never read as the reviewer’s current HEAD.

The original investigation channel is unchanged. Each original id appears exactly once in `adjudicates`; rows without `adjudicates` are CVO findings or the manual-grade record and are excluded from the original-item denominator.

```json
[
  {
    "id": "IRPT_FNTEND-C-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The ambient declaration was narrowed to an inline structural directory entry. Current IRPT tests pass; the later eight FE-s-11 type errors are a separate S17 finding.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-1 names tests under portal/src/pages/InvestorReporting/__tests__/fe-s-1/ 'runnable by bun test' (F1-AC2..F1-AC6) AND a portal typecheck at rc=0 (F1-AC1), and grants no path outside <paths> -- portal/tsconfig.app.json is not in the grant.",
    "world_is": "The ambient declaration was narrowed to an inline structural directory entry. Current IRPT tests pass; the later eight FE-s-11 type errors are a separate S17 finding.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-1.contracts-client-adapter-fixtures.proof_of_spec.json@314f8e1259ed0cbdf1238b8ce81cb42151dd0c5f"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S1"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The face counts 31 JSON fixtures, while index.ts and the directory listing add non-JSON entries. Preserve the file-kind denominator; no missing fixture is inferred from a literal all-files count.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-1: fixtures.test.ts 'lists fixtures/ and asserts 31 files, printing FIXTURES: 31 of 31'; the same cell also requires 'A fixtures/index.ts manifest' and 'a smoke map ... at fixtures/smoke/default.json', both inside fixtures/.",
    "world_is": "The face counts 31 JSON fixtures, while index.ts and the directory listing add non-JSON entries. Preserve the file-kind denominator; no missing fixture is inferred from a literal all-files count.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-1.contracts-client-adapter-fixtures.proof_of_spec.json@314f8e1259ed0cbdf1238b8ce81cb42151dd0c5f"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S2"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The face counts 31 JSON fixtures, while index.ts and the directory listing add non-JSON entries. Preserve the file-kind denominator; no missing fixture is inferred from a literal all-files count."
  },
  {
    "id": "IRPT_FNTEND-C-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The issuer assigned the declaration repair. W1-S1 now records its verified narrow closure; an assignment is not a separate product finding.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W1-S1: ARMED, disarm_owner 2.0.0_SA_COO~F; a later addition of @types/node to the tsconfig types array would break a green typecheck on an edit nobody would connect to the fe-s-1 folder.",
    "world_is": "The issuer assigned the declaration repair. W1-S1 now records its verified narrow closure; an assignment is not a separate product finding.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The issuer assigned the declaration repair. W1-S1 now records its verified narrow closure; an assignment is not a separate product finding."
  },
  {
    "id": "IRPT_FNTEND-C-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "PageThemeProvider was imported from its actual definition after the face named a module that did not export it. Current route tests render successfully; preserve the corrected source location.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-2 cell FE-s-2, Page shell: \"`PageThemeProvider` and `PageHeaderCleanBadge` from `portal/src/components/PageHeaderVariants.tsx`\".",
    "world_is": "PageThemeProvider was imported from its actual definition after the face named a module that did not export it. Current route tests render successfully; preserve the corrected source location.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-2.route-shell-header-search.proof_of_spec.json@62f80c26fb032223648994f9755cbe06f28ddbc5"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S3"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "PageThemeProvider was imported from its actual definition after the face named a module that did not export it. Current route tests render successfully; preserve the corrected source location."
  },
  {
    "id": "IRPT_FNTEND-C-S5",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The original white-on-silver dropdown and clipped mobile actions are visible in F2 captures. FE-s-3 now uses the admitted Model Portfolios control classes and a stacked mobile actions row; F3’s two named captures show both controls.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-2 requires the firm dropdown to be `PageSurfaceControl` with `as=\"dropdown\"`, lists PageSurfaceControl.tsx as IMPORTED, never edited, and binds the cell to the colour law: \"No light text (text-white*, text-{color}-300) or light button (bg-white/N) directly on the silver canvas\". F2-AC7 is graded at L9 on \"nothing light sits on the silver canvas\".",
    "world_is": "The original white-on-silver dropdown and clipped mobile actions are visible in F2 captures. FE-s-3 now uses the admitted Model Portfolios control classes and a stacked mobile actions row; F3’s two named captures show both controls.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S4",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-2.route-shell-header-search.proof_of_spec.json@62f80c26fb032223648994f9755cbe06f28ddbc5"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S4"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S6",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The ignored brand source was provisioned into the render package as brand.tokens.json and a logo asset; current tests check its tokens. Its ignored-at-cut origin remains part of artifact provenance, and it is distinct from the missing font binary.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-4 cell FE-s-4: 'brand.ts: tokens read from deck_generation/brand_spec/brand.json (copied verbatim into the package as brand.tokens.json with the source path recorded in a comment); the logo from deck_generation/brand/logo_package/.../Opal-Capital-Logo-Full-Color.svg copied into render/assets/'. Both are stated as repo-relative paths, and BOUNDS adds 'READ or COPIED into the package, never edited'.",
    "world_is": "The ignored brand source was provisioned into the render package as brand.tokens.json and a logo asset; current tests check its tokens. Its ignored-at-cut origin remains part of artifact provenance, and it is distinct from the missing font binary.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W2-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W2-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The ignored brand source was provisioned into the render package as brand.tokens.json and a logo asset; current tests check its tokens. Its ignored-at-cut origin remains part of artifact provenance, and it is distinct from the missing font binary."
  },
  {
    "id": "IRPT_FNTEND-C-S7",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The frontend reference resolver and payload-to-template assembly now exist and the reference tests pass. This closes local preview composition only; the independent backend schema/route mismatch is a new CVO finding.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-4: PrintEntry 'fetches the ExportBundle through the typed client's export-preview operation, calls assertSupported, and renders PerformanceDocument or AnalysisDocument by bundle.reportKind'; Summary.tsx renders 'beginning value, ending value, period return'; 'every field rendered from PerformanceReport as given'; Disclosures.tsx is part of the performance template; BOUNDS: 'The package renders what the bundle carries and computes nothing'.",
    "world_is": "The frontend reference resolver and payload-to-template assembly now exist and the reference tests pass. This closes local preview composition only; the independent backend schema/route mismatch is a new CVO finding.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W2-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W2-S2"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S8",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The pinned brand requires Lato, while the package/recorded captures use fallback fonts and carry no Lato binary. Typography therefore fails F4-AC9 even though both templates share other brand tokens.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-4: manifest fonts ['Lato-Regular','Lato-Bold','Lato-Italic']; 'print.css: ... @font-face for the packaged Lato files under render/assets/fonts/ with docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt copied beside them'; and F4-AC9 grades the two PNGs for 'Opal colours, logo clear space, Lato'.",
    "world_is": "The pinned brand requires Lato, while the package/recorded captures use fallback fonts and carry no Lato binary. Typography therefore fails F4-AC9 even though both templates share other brand tokens.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W2-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W2-S3"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S9",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "Recharts produces no chart under server-only static markup. The package now declares browser rendering and its recorded print captures contain charts; SSR is no longer asserted as the rendering contract.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-4: 'CumulativeReturnChart.tsx (recharts, from the daily cumulative series, endpoints labelled with the returned dates)'; the cell's opening line: 'Screen preview and server-side PDF both render THIS package'; tests use react-dom/server renderToStaticMarkup.",
    "world_is": "Recharts produces no chart under server-only static markup. The package now declares browser rendering and its recorded print captures contain charts; SSR is no longer asserted as the rendering contract.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W2-S4",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W2-S4"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S10",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The screenshot helper compares pathname to a query-bearing route string, producing a false navigation warning. This instrumentation defect belongs to the portal smoke-tool surface, opened in org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md#owning-surface-referrals. It does not excuse W1-S10’s independently reproduced firm-access redirect.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-4 F4-AC7/F4-AC8 pass a route with a query string ('investor-reporting/print?bundle=perf-fixture-1') and say 'record LOC'; the expectation is rc=0.",
    "world_is": "The screenshot helper compares pathname to a query-bearing route string, producing a false navigation warning. This instrumentation defect belongs to the portal smoke-tool surface, opened in org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md#owning-surface-referrals. It does not excuse W1-S10’s independently reproduced firm-access redirect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W2-S5",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W2-S5"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The screenshot helper compares pathname to a query-bearing route string, producing a false navigation warning. This instrumentation defect belongs to the portal smoke-tool surface, opened in org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md#owning-surface-referrals. It does not excuse W1-S10’s independently reproduced firm-access redirect."
  },
  {
    "id": "IRPT_FNTEND-C-S11",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The assignment is discharged by W1-S4’s measured IRPT control repair. The original F2-AC7 grade remains FAIL at its own image vintage.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W1-S4: ARMED, disarm_owner 2.0.0_SA_COO~F -- PageSurfaceControl as=dropdown renders white text on the silver canvas; the control is do-not-edit. IRPT_FNTEND-W1-S3 (INERT): the FE-s-2 face named the wrong export path for PageThemeProvider.",
    "world_is": "The assignment is discharged by W1-S4’s measured IRPT control repair. The original F2-AC7 grade remains FAIL at its own image vintage.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S2"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The assignment is discharged by W1-S4’s measured IRPT control repair. The original F2-AC7 grade remains FAIL at its own image vintage."
  },
  {
    "id": "IRPT_FNTEND-C-S12",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The resolver assignment is discharged by W2-S2’s local composition closure. It is not proof that frontend and backend wire representations agree.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W2-S2: ARMED -- a backend implementing export-preview to the contract as written is refused by the print entry while every FE test stays green.",
    "world_is": "The resolver assignment is discharged by W2-S2’s local composition closure. It is not proof that frontend and backend wire representations agree.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S3"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The resolver assignment is discharged by W2-S2’s local composition closure. It is not proof that frontend and backend wire representations agree."
  },
  {
    "id": "IRPT_FNTEND-C-S13",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The browser-render contract amendment is reflected in W2-S4. The separate cloud renderer remains an open backend product gap.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W2-S4: ARMED -- a PDF path built on server-side static markup ships chartless reports while every FE test stays green.",
    "world_is": "The browser-render contract amendment is reflected in W2-S4. The separate cloud renderer remains an open backend product gap.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S4",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S4"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The browser-render contract amendment is reflected in W2-S4. The separate cloud renderer remains an open backend product gap."
  },
  {
    "id": "IRPT_FNTEND-C-S14",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "This is the Lato input-authority carrier. The font absence remains open in W2-S3; neither absence nor egress caution creates permission to fetch a replacement.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W2-S3: ARMED, disarm_owner 2.0.0_SA_COO~F -- the packaged Lato faces the cell names could not be packaged.",
    "world_is": "This is the Lato input-authority carrier. The font absence remains open in W2-S3; neither absence nor egress caution creates permission to fetch a replacement.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S5",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S5"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This is the Lato input-authority carrier. The font absence remains open in W2-S3; neither absence nor egress caution creates permission to fetch a replacement."
  },
  {
    "id": "IRPT_FNTEND-C-S15",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The narrative component is now wired, but the cell’s expected annotations/topics/historyCutoff fields are absent from the shared payload. Mapping coveredWindow.start to a history cutoff is not demonstrated semantic equivalence; the original PNG still shows the placeholder.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-8 cell FE-s-8: the page draws 'the packet's events ... and the packet's annotations placed on the curve'; 'for each marked window, the trendingTopics and topicCloud terms ... with the other sentiment signals as supporting context using the visual vocabulary of MarketRegimeIndicator.tsx, SentimentGauge.tsx and SentimentPanel.tsx (imported presentation, no live data)'; 'footnotes and coverage from the packet (coverage, evidence citations...)'; the MISSING HISTORY state gates on 'packet.historyCutoff'; and the page fills 'the slot PerformanceDocument left'.",
    "world_is": "The narrative component is now wired, but the cell’s expected annotations/topics/historyCutoff fields are absent from the shared payload. Mapping coveredWindow.start to a history cutoff is not demonstrated semantic equivalence; the original PNG still shows the placeholder.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W2-S6",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-8.narrative-page.proof_of_spec.json@24c4b211b2b296e21a046d05353a852c5e40f8d8"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W2-S6"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S16",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The issuer split the wiring and contract halves. Credit the later wiring without closing the unresolved semantic mapping or the missing replacement narrative evidence in W2-S6.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W2-S6: ARMED -- the print route still shows the FE-s-4 placeholder on the period-in-context page; the cell text names packet fields the contract does not carry; the named market-performance components fetch live and do not resolve under bun test.",
    "world_is": "The issuer split the wiring and contract halves. Credit the later wiring without closing the unresolved semantic mapping or the missing replacement narrative evidence in W2-S6.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S6",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S6"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The issuer split the wiring and contract halves. Credit the later wiring without closing the unresolved semantic mapping or the missing replacement narrative evidence in W2-S6."
  },
  {
    "id": "IRPT_FNTEND-C-S17",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The root tsconfig now supplies @/* -> src/* and the real-import alias probe passes in the full IRPT test run.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-3 F3-AC7: `bun test .../dropdown-class.test.ts` renders FirmDropdown via `renderToStaticMarkup` and asserts its computed classes; BOUNDS names `PageSurfaceControl.tsx` as imported, never edited.",
    "world_is": "The root tsconfig now supplies @/* -> src/* and the real-import alias probe passes in the full IRPT test run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S5",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-3.tabs-selection-lifecycle.proof_of_spec.json@4664ba9bd2af0f52013fb2e0c044a84a8132adee"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S5"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S18",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The orphan Vite process was an actual earlier port collision. S8 records the owner’s sweep, and later captures were obtained. No parent-lifecycle guarantee is inferred; the repeat-prevention requirement is retained in the runtime owning-surface referral in org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md.",
    "class": "OBSERVATION",
    "spec_asserts": "This order's identity line fixes <PORT>=5181 and every ui-smoke invocation (F3-AC4, F3-AC5, F3-AC9) names --port <PORT> literally; the identity line also instructs 'Stop it (kill its pid) before your final report', implying the port is this worker's alone to bind.",
    "world_is": "The orphan Vite process was an actual earlier port collision. S8 records the owner’s sweep, and later captures were obtained. No parent-lifecycle guarantee is inferred; the repeat-prevention requirement is retained in the runtime owning-surface referral in org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S6",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-3.tabs-selection-lifecycle.proof_of_spec.json@4664ba9bd2af0f52013fb2e0c044a84a8132adee"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S6"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The orphan Vite process was an actual earlier port collision. S8 records the owner’s sweep, and later captures were obtained. No parent-lifecycle guarantee is inferred; the repeat-prevention requirement is retained in the runtime owning-surface referral in org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md."
  },
  {
    "id": "IRPT_FNTEND-C-S19",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "This alias-repair assignment is discharged under W1-S5. Its regression is evaluated separately under W1-S7 rather than erased by the repair intent.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W1-S5: ARMED -- every later cell whose tests import a portal module through @/ hits the same failure and works around it per file, and a workaround that mocks the module is a test that never exercises the real component.",
    "world_is": "This alias-repair assignment is discharged under W1-S5. Its regression is evaluated separately under W1-S7 rather than erased by the repair intent.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S7",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S7"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This alias-repair assignment is discharged under W1-S5. Its regression is evaluated separately under W1-S7 rather than erased by the repair intent."
  },
  {
    "id": "IRPT_FNTEND-C-S20",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The process sweep closes the recorded port collision, not the general possibility of orphan servers. Preserve that distinction in the owning-runtime referral; no additional CVO monitor was launched for it.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W1-S6: ARMED -- a stale server holds a slot's assigned port, vite bumps the next worker to another port, and a port-keyed instrument reads the wrong tree.",
    "world_is": "The process sweep closes the recorded port collision, not the general possibility of orphan servers. Preserve that distinction in the owning-runtime referral; no additional CVO monitor was launched for it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S8",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S8"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The process sweep closes the recorded port collision, not the general possibility of orphan servers. Preserve that distinction in the owning-runtime referral; no additional CVO monitor was launched for it."
  },
  {
    "id": "IRPT_FNTEND-C-S21",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "FE-s-10 mounts AnalysisTab and the FE-s-11 Analysis capture contains real modeled sections. Current tests pass. The original F6 screenshots still cannot demonstrate correction behavior.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-6's WORKER FACE: 'Tab at portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx, mounted in TabShell's analysis body.' F6-AC6/F6-AC7 invoke ui-smoke against the LIVE route investor-reporting with --click Analysis, expecting the screenshot to show this cell's rendered tab (variants, request list, input review, stage, sections) for L9's F6-AC8 judgment.",
    "world_is": "FE-s-10 mounts AnalysisTab and the FE-s-11 Analysis capture contains real modeled sections. Current tests pass. The original F6 screenshots still cannot demonstrate correction behavior.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W3-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-6.analysis-tab.proof_of_spec.json@854594d51a6ba1accb25d8d965b1c188ea3121dd"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W3-S1"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S22",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The cell named AnalysisRequest.inputRevision and ReportSection.parity.passed fields that its shared contract did not carry. A local derivation/optional fallback makes the component testable but does not establish producer semantics.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-6 WORKER FACE: 'submitCorrection sends a NEW input revision through the typed client (inputRevision = current + 1)' and 'a section shows SUPPORTED only when section.parity.passed === true, otherwise UNSUPPORTED with the reason', both stated as if reading existing contract fields.",
    "world_is": "The cell named AnalysisRequest.inputRevision and ReportSection.parity.passed fields that its shared contract did not carry. A local derivation/optional fallback makes the component testable but does not establish producer semantics.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W3-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-6.analysis-tab.proof_of_spec.json@854594d51a6ba1accb25d8d965b1c188ea3121dd"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W3-S2"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S23",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "FE-s-10 mounts HoldingsTab and the FE-s-11 SmartX capture contains the holdings hierarchy. The original two F7 captures only showed status panels.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-7's cell text: 'Tab at portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx, mounted in TabShell's holdings body.'",
    "world_is": "FE-s-10 mounts HoldingsTab and the FE-s-11 SmartX capture contains the holdings hierarchy. The original two F7 captures only showed status panels.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W4-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-7.holdings-tab.proof_of_spec.json@277a7199ac4cccc82977dd33dd07f3bedcf89076"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W4-S1"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S24",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "CategoryViewTree’s AUM contract cannot carry signed IRPT custody amounts without loss. The local drill tree preserves signed values and reuses the canonical model-color functions; the census documents the limited overview reuse. This does not prove the missing target/attribution screenshots, retained in the CVO visual finding.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-7's cell text: 'DrillTree.tsx: CategoryViewTree from portal/src/components/CategoryViewTree.tsx over the snapshot's node hierarchy (Models, SMAs, Client and every other category the hierarchy carries)' -- read plainly, CategoryViewTree renders the snapshot's hierarchy.",
    "world_is": "CategoryViewTree’s AUM contract cannot carry signed IRPT custody amounts without loss. The local drill tree preserves signed values and reuses the canonical model-color functions; the census documents the limited overview reuse. This does not prove the missing target/attribution screenshots, retained in the CVO visual finding.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W4-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-7.holdings-tab.proof_of_spec.json@277a7199ac4cccc82977dd33dd07f3bedcf89076"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W4-S2"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "CategoryViewTree’s AUM contract cannot carry signed IRPT custody amounts without loss. The local drill tree preserves signed values and reuses the canonical model-color functions; the census documents the limited overview reuse. This does not prove the missing target/attribution screenshots, retained in the CVO visual finding."
  },
  {
    "id": "IRPT_FNTEND-C-S25",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The per-file mock that leaked into the real alias import was removed. The dropdown test imports the real component and checks exact white-token absence with a positive control; the full IRPT suite passes.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W1-S7 (COO, prior row): adding compilerOptions.baseUrl/paths to portal/tsconfig.json 'changes nothing tsc -b compiles, and retires the per-file workaround class for every remaining cell' -- and this order's own text: 'Existing per-file mock.module workarounds in earlier test folders are left as they are.' Separately, THE CELL: 'renders ... MethodsAndSources from render/performance/ (imported, never copied)'; 'a benchmark section ... renders only when PerformanceReport.supported.benchmark ... is true'; 'StatusPanel from FE-s-3 for every non-READY envelope.'",
    "world_is": "The per-file mock that leaked into the real alias import was removed. The dropdown test imports the real component and checks exact white-token absence with a positive control; the full IRPT suite passes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S7",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-5.reporting-tab.proof_of_spec.json@3ab6275f9f9aba603571e87c573e3ed21fc1eb98"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S7"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S26",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The tab-mount assignment is discharged under W3-S1 and W4-S1 using later actual-content captures. Their original visual criteria remain bounded by their original evidence.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W3-S1 and W4-S1: ARMED -- AnalysisTab and HoldingsTab are not reachable from the running app; TO-FE-s-6 and TO-FE-s-7 said each mounts in the shell's body and neither grant included the shell.",
    "world_is": "The tab-mount assignment is discharged under W3-S1 and W4-S1 using later actual-content captures. Their original visual criteria remain bounded by their original evidence.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S9",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S9"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The tab-mount assignment is discharged under W3-S1 and W4-S1 using later actual-content captures. Their original visual criteria remain bounded by their original evidence."
  },
  {
    "id": "IRPT_FNTEND-C-S27",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The mock-regression assignment is discharged under W1-S7. No blanket typecheck success is inferred from the test-only repair.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W1-S7 (1): ARMED -- F5-AC9's required edit regresses the already-terminal F3-AC7; the DEV test set is red until one of them moves.",
    "world_is": "The mock-regression assignment is discharged under W1-S7. No blanket typecheck success is inferred from the test-only repair.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S10",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S10"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The mock-regression assignment is discharged under W1-S7. No blanket typecheck success is inferred from the test-only repair."
  },
  {
    "id": "IRPT_FNTEND-C-S28",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "PRD v0.5 added Generate inputs after earlier faces were cut. The current v0.6 endpoint must inform the next cut; the old input-review cell is not retrospectively graded as a full Generate flow.",
    "class": "OBSERVATION",
    "spec_asserts": "PRD v0.5 F5: the Analysis tab produces the browser request half of AnalysisRequest as the UI contract specifies, with the variant resolved by comparison count and job states from the Opal job record.",
    "world_is": "PRD v0.5 added Generate inputs after earlier faces were cut. The current v0.6 endpoint must inform the next cut; the old input-review cell is not retrospectively graded as a full Generate flow.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S11",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S11"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "PRD v0.5 added Generate inputs after earlier faces were cut. The current v0.6 endpoint must inform the next cut; the old input-review cell is not retrospectively graded as a full Generate flow."
  },
  {
    "id": "IRPT_FNTEND-C-S29",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The narrative opt-in amendment made the old positive-control fixture fail. FE-s-10 updates that control to set includeNarrative explicitly; both positive and negative narrative tests now pass.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-9 (narrative page wiring amendment): \"In PerformanceDocument.tsx, replace the slot placeholder with PeriodInContextPage rendered when the RenderBundle carries a NarrativePacket AND the export options carry includeNarrative: true ... default false\"; render/performance/PerformanceDocument.tsx is this order's own granted path and the Reuse bound names it as one of the files this amendment changes.",
    "world_is": "The narrative opt-in amendment made the old positive-control fixture fail. FE-s-10 updates that control to set includeNarrative explicitly; both positive and negative narrative tests now pass.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S8",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-9.export-options-preview.proof_of_spec.json@7db8bed41ba4ce4e9739d15ce3bc13e959848bad"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S8"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S30",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The positive-control assignment is discharged in W1-S8. The old row’s narrative condition is distinct from approved-logo provisioning, which remains part of export integration.",
    "class": "OBSERVATION",
    "spec_asserts": "IRPT_FNTEND-W1-S8 (2): ARMED -- an amendment this issuer wrote retires a behaviour a terminal cell's positive control asserts, and the DEV set is red by one until the control follows the behaviour.",
    "world_is": "The positive-control assignment is discharged in W1-S8. The old row’s narrative condition is distinct from approved-logo provisioning, which remains part of export integration.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S12",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S12"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The positive-control assignment is discharged in W1-S8. The old row’s narrative condition is distinct from approved-logo provisioning, which remains part of export integration."
  },
  {
    "id": "IRPT_FNTEND-C-S31",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The worker-local portal gitlink incident is a repository handoff defect, not product behavior. This review pins portal edab15b54f8fd2e2c3da2eaed87dd64a215785c9 explicitly and does not use an unqualified workspace HEAD as proof of portal bytes. Future drains must prove receiving-side object reachability.",
    "class": "OBSERVATION",
    "spec_asserts": "A worker's write grant is its <paths> block; the workspace gitlink `portal` is not in any grant, and the workspace push (MSTR's) does not carry the portal repo.",
    "world_is": "The worker-local portal gitlink incident is a repository handoff defect, not product behavior. This review pins portal edab15b54f8fd2e2c3da2eaed87dd64a215785c9 explicitly and does not use an unqualified workspace HEAD as proof of portal bytes. Future drains must prove receiving-side object reachability.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S13",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S13"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The worker-local portal gitlink incident is a repository handoff defect, not product behavior. This review pins portal edab15b54f8fd2e2c3da2eaed87dd64a215785c9 explicitly and does not use an unqualified workspace HEAD as proof of portal bytes. Future drains must prove receiving-side object reachability."
  },
  {
    "id": "IRPT_FNTEND-C-S32",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The server snapshot implementation now permits TabShell’s static-render check and the integrated tests pass. The issuer’s state-file grant covers the repair; no extra state API is inferred.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-10 BOUNDS: \"Edits inside header/, state/, tabs/*/ and export/ are limited to the named export seams; a needed change beyond them is a surprise row on the owning cell.\" The named state/ seam is exactly \"state/selection.ts gains switchFirm(next)\" -- state/hooks.ts is not named.",
    "world_is": "The server snapshot implementation now permits TabShell’s static-render check and the integrated tests pass. The issuer’s state-file grant covers the repair; no extra state API is inferred.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S9",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-10.global-view.proof_of_spec.json@e1314eb32b337a8e4602190fa30ce1ce88a0d316"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S9"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S33",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "All four partner-firm allowlists omit /investor-reporting; the 49financial screenshot lands on /market and matches zero IRPT fixtures. A rejected route is not evidence of the intended firm-scoped IRPT view.",
    "class": "OBSERVATION",
    "spec_asserts": "This order's WORKER FACE: \"the ui-smoke `--firm <id>` flag renders a PARTNER session\" and \"ui-smoke prints `DID NOT LAND` for a route carrying a query string while rc=0 and the PNG is the evidence (F10-AC8 carries `?firm=global`)\" -- framing the expected DID-NOT-LAND print as a query-string artifact of the instrument, implying the PNG would otherwise show Investor Reporting's firm-scoped view.",
    "world_is": "All four partner-firm allowlists omit /investor-reporting; the 49financial screenshot lands on /market and matches zero IRPT fixtures. A rejected route is not evidence of the intended firm-scoped IRPT view.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S10",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-10.global-view.proof_of_spec.json@e1314eb32b337a8e4602190fa30ce1ce88a0d316"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S10"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S34",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The FE-s-10 drain count and assignment are intake records. The firm-access defect remains open under W1-S10; eleven terminal orders later supersede this ten-order vintage.",
    "class": "OBSERVATION",
    "spec_asserts": "TO-FE-s-10 F10-AC8 face: the DID-NOT-LAND print is an artifact of a route carrying a query string; a firm-scoped session renders the Investor Reporting page with one firm and no dropdown.",
    "world_is": "The FE-s-10 drain count and assignment are intake records. The firm-access defect remains open under W1-S10; eleven terminal orders later supersede this ten-order vintage.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S14",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S14"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The FE-s-10 drain count and assignment are intake records. The firm-access defect remains open under W1-S10; eleven terminal orders later supersede this ten-order vintage."
  },
  {
    "id": "IRPT_FNTEND-C-S35",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The issuer’s first FE-s-11 repair amendment is an authorization carrier. W1-S12 is now disarmed by measured captures/tests; W1-S11 is only partially repaired and remains open because both components are unmounted.",
    "class": "OBSERVATION",
    "spec_asserts": "Issuer faces F11-AC5..AC8 (and F9's print-route coverage): rc=0 from ui-smoke is the mechanical bar for 'the <screen> at 390'. Spine mid-round: the sanctioned repair of a defect is an issuer amendment to a NON-TERMINAL order; an ARMED row disarms via its disarm_owner.",
    "world_is": "The issuer’s first FE-s-11 repair amendment is an authorization carrier. W1-S12 is now disarmed by measured captures/tests; W1-S11 is only partially repaired and remains open because both components are unmounted.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S15",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S15"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The issuer’s first FE-s-11 repair amendment is an authorization carrier. W1-S12 is now disarmed by measured captures/tests; W1-S11 is only partially repaired and remains open because both components are unmounted."
  },
  {
    "id": "IRPT_FNTEND-C-S36",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The second FE-s-11 amendment is discharged for the malformed fixture and regex gate in W1-S13/W1-S14. It does not fix S17’s eight full-portal TypeScript errors.",
    "class": "OBSERVATION",
    "spec_asserts": "Issuer face F11-AC8 (first amendment): the bar is the printed line `CONSOLE[log]: REFS RESOLVED: 1 of 1`. FE-s-7's fixture map serves what the Holdings tab needs; the default tab's needs were not part of FE-s-7's cut.",
    "world_is": "The second FE-s-11 amendment is discharged for the malformed fixture and regex gate in W1-S13/W1-S14. It does not fix S17’s eight full-portal TypeScript errors.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S16",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S16"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The second FE-s-11 amendment is discharged for the malformed fixture and regex gate in W1-S13/W1-S14. It does not fix S17’s eight full-portal TypeScript errors."
  },
  {
    "id": "IRPT_FNTEND-C-S37",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "AppliedBranding and ReceiptPanel now use dark light-surface text, but the census and import read still show both defined and unmounted. The unsafe-color half is disarmed; the whole finding is not remediated because applied branding and receipt state are absent from the live flow.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-12's CONSTRAINT: 'a new component requires a stated need the existing set cannot meet; matching appearance alone is not reuse' and its PROOF: 'a census of EVERY component the page uses... each is REUSED... or is NEW with a stated reason'; F11-AC3's colour law: 'no light-on-canvas class outside a dark container'. AppliedBranding.tsx's own header states its need (show what branding was ACTUALLY applied, from the preview bundle) but nothing in the tree ever renders it to meet that need.",
    "world_is": "AppliedBranding and ReceiptPanel now use dark light-surface text, but the census and import read still show both defined and unmounted. The unsafe-color half is disarmed; the whole finding is not remediated because applied branding and receipt state are absent from the live flow.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S11",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json@74f846345fe1e332d3050b5035a2f8ce44acd0fb"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S11"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S38",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "useFirmContext now returns early while scope is null, ending the one-firm default-effect ping-pong. All five FE-s-11 fresh captures reach real content and current tests pass. CVO disarm confirmed.",
    "class": "OBSERVATION",
    "spec_asserts": "This order's WORKER FACE names these exact invocations (fixture + --click) as producing 'the Analysis tab at 390' / 'the Holdings tab at 390' / 'the export modal at 390', with only rc=0 as the stated expectation.",
    "world_is": "useFirmContext now returns early while scope is null, ending the one-firm default-effect ping-pong. All five FE-s-11 fresh captures reach real content and current tests pass. CVO disarm confirmed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S12",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json@74f846345fe1e332d3050b5035a2f8ce44acd0fb"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S12"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S39",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The holdings fixture now supplies the full method object expected by MethodsAndSources; the current Holdings capture and integrated test run render it.",
    "class": "OBSERVATION",
    "spec_asserts": "F11-AC6 (AMENDED): 'the bar is the printed CLICKED: Holdings'; this order's grant (BOUNDS) names exactly three portal files for repair (global/useFirmContext.ts, export/AppliedBranding.tsx, fixtures/smoke/fe-s-11-print.json) and states 'any other defect found is a surprise row on its cell.'",
    "world_is": "The holdings fixture now supplies the full method object expected by MethodsAndSources; the current Holdings capture and integrated test run render it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S13",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json@74f846345fe1e332d3050b5035a2f8ce44acd0fb"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S13"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S40",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The amended log-pattern expression no longer treats literal [log] as a character class. The terminal instance passes its checker and the reference-resolution test passes. CVO disarm confirmed.",
    "class": "OBSERVATION",
    "spec_asserts": "F11-AC8 (AMENDED): '<expect>CONSOLE[log]: REFS RESOLVED: 1 of 1</expect>'; <proof_of_spec>: 'validated with python .tools/proof-of-spec-check.py <instance> F11-AC1..F11-AC10 BEFORE the complete flip'; the PROOF_OF_SPEC.schema.json's own field description: 'the PATTERN (Python regex, searched with DOTALL) the deciding output must match; the checker grades a mechanical criterion by this match, not by the worker.'",
    "world_is": "The amended log-pattern expression no longer treats literal [log] as a character class. The terminal instance passes its checker and the reference-resolution test passes. CVO disarm confirmed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-W1-S14",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json@74f846345fe1e332d3050b5035a2f8ce44acd0fb"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W1-S14"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S41",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The CVO independently reproduced exactly eight TypeScript errors in FE-s-11 tests: missing test.each/toMatch/statSync declarations and four implicit-any parameters. The process exit code is 2; Bun still passes 322 with one skipped.",
    "class": "OBSERVATION",
    "spec_asserts": "Portal DEV carries every drained cell with `bun run typecheck` rc=0 (F10-AC1's bar on the cell before this one, and the standing bar of every earlier order); the census order's product is the record and its tests run under bun.",
    "world_is": "The CVO independently reproduced exactly eight TypeScript errors in FE-s-11 tests: missing test.each/toMatch/statSync declarations and four implicit-any parameters. The process exit code is 2; Bun still passes 322 with one skipped.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md@2e50d2e12912bc1af9b9b2a8a077736c90532525#IRPT_FNTEND-S17",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit): independent checks and limits",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-S17"
    ],
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S42",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "The source-level join measures zero of eleven frontend method/path pairs in the declared backend route table. Ten of ten consumer payload fixtures fail their same-named backend schemas, with eleven backend controls passing. LiveClient returns the raw transport payload and applies no agreed shape translator.",
    "class": "OBSERVATION",
    "spec_asserts": "The frontend live adapter must speak the agreed backend HTTP and payload contract.",
    "world_is": "The source-level join measures zero of eleven frontend method/path pairs in the declared backend route table. Ten of ten consumer payload fixtures fail their same-named backend schemas, with eleven backend controls passing. LiveClient returns the raw transport payload and applies no agreed shape translator.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit)",
        "portal/src/api/endpoints/investor-reporting.ts@0322a04a4d144db9bf3211eca5c1bcd05f8099b9",
        "infra/aws/terraform/investor-reporting/api/routes.json@bef9b459f3962b228f6ac032c9c4cae5cb90efcc",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-1.contracts-client-adapter-fixtures.proof_of_spec.json@314f8e1259ed0cbdf1238b8ce81cb42151dd0c5f",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-18.the-foundation-contracts-homes-manifest-roots.proof_of_spec.json@c4214773c9d84fa11f5641d3a28f9f503e784692"
      ]
    },
    "disposition": "GRADUATED",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S43",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "Of ten manual criteria, five FAIL, four are NOT_EVALUATED and only the narrow F3 header criterion PASSes. All 24 images were read; missing correction/target/history views and mismatched screen/print data cannot be repaired by a unit-test count.",
    "class": "OBSERVATION",
    "spec_asserts": "Visual acceptance must be demonstrated on the mounted states and matching report inputs.",
    "world_is": "Of ten manual criteria, five FAIL, four are NOT_EVALUATED and only the narrow F3 header criterion PASSes. All 24 images were read; missing correction/target/history views and mismatched screen/print data cannot be repaired by a unit-test count.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_L8_REVIEW_20260911.md (same commit)",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-5.reporting-tab.proof_of_spec.json@3ab6275f9f9aba603571e87c573e3ed21fc1eb98",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-6.analysis-tab.proof_of_spec.json@854594d51a6ba1accb25d8d965b1c188ea3121dd",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-7.holdings-tab.proof_of_spec.json@277a7199ac4cccc82977dd33dd07f3bedcf89076",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-8.narrative-page.proof_of_spec.json@24c4b211b2b296e21a046d05353a852c5e40f8d8",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-9.export-options-preview.proof_of_spec.json@7db8bed41ba4ce4e9739d15ce3bc13e959848bad",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-10.global-view.proof_of_spec.json@e1314eb32b337a8e4602190fa30ce1ce88a0d316",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json@74f846345fe1e332d3050b5035a2f8ce44acd0fb"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "IRPT_FNTEND-C-S44",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-11T10:56:02Z",
    "one_line": "10 judgment criteria independently read and graded; structural VALID is not a truth or product-completion verdict.",
    "class": "OBSERVATION",
    "spec_asserts": "L9 grades every judgment criterion against its issued specification.",
    "world_is": "10 judgment criteria independently read and graded; structural VALID is not a truth or product-completion verdict.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-10.global-view.proof_of_spec.json@e1314eb32b337a8e4602190fa30ce1ce88a0d316",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json@74f846345fe1e332d3050b5035a2f8ce44acd0fb",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-2.route-shell-header-search.proof_of_spec.json@62f80c26fb032223648994f9755cbe06f28ddbc5",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-3.tabs-selection-lifecycle.proof_of_spec.json@4664ba9bd2af0f52013fb2e0c044a84a8132adee",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-5.reporting-tab.proof_of_spec.json@3ab6275f9f9aba603571e87c573e3ed21fc1eb98",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-6.analysis-tab.proof_of_spec.json@854594d51a6ba1accb25d8d965b1c188ea3121dd",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-7.holdings-tab.proof_of_spec.json@277a7199ac4cccc82977dd33dd07f3bedcf89076",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-8.narrative-page.proof_of_spec.json@24c4b211b2b296e21a046d05353a852c5e40f8d8",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-9.export-options-preview.proof_of_spec.json@7db8bed41ba4ce4e9739d15ce3bc13e959848bad",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json (same commit)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "F10-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-10.global-view.proof_of_spec.json@e1314eb32b337a8e4602190fa30ce1ce88a0d316",
        "verdict": "NOT_EVALUATED",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-10.global-view.md F10-AC9: The Global image shows the Model Portfolios-style dropdown and firm attribution. The required firm session is redirected to Market Overview, so the intended firm-scoped IRPT surface is unreachable. Refusal proves no Global path from that rejected route, but cannot establish the firm-view behavior the combined bar asks the reviewer to read."
      },
      {
        "criterion": "F11-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.proof_of_spec.json@74f846345fe1e332d3050b5035a2f8ce44acd0fb",
        "verdict": "FAIL",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-11.design-conformity-census.md F11-AC9: All 24 round PNGs were viewed, together with census and brand review. Earlier contrast failures persist in their images; Lato is absent; current 390 report/holdings content clips or overlaps; applied-branding/receipt components remain unused. The report claims six fresh captures but only five distinct FE-s-11 PNGs exist. A clean color-token scan does not establish the full one-product visual bar."
      },
      {
        "criterion": "F2-AC7",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-2.route-shell-header-search.proof_of_spec.json@62f80c26fb032223648994f9755cbe06f28ddbc5",
        "verdict": "FAIL",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-2.route-shell-header-search.md F2-AC7: At the required F2 image vintage the dropdown is white on silver; at 390 its control is clipped and search is offscreen. This violates both the control-placement and contrast bar. F3 repairs do not rewrite these PNGs."
      },
      {
        "criterion": "F3-AC10",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-3.tabs-selection-lifecycle.proof_of_spec.json@4664ba9bd2af0f52013fb2e0c044a84a8132adee",
        "verdict": "PASS",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-3.tabs-selection-lifecycle.md F3-AC10: The two named captures show the dark primary-color firm control and, at 390, both dropdown and search fully visible below the title. This is the narrow header bar, not a grade of later report tables."
      },
      {
        "criterion": "F4-AC9",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.proof_of_spec.json@73752f923887e071c8dc9dcf1d06306f80098257",
        "verdict": "FAIL",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-4.render-package-templates-print.md F4-AC9: The bar explicitly requires Lato as well as shared Opal brand. Both templates share colors/logo framing, but their recorded font is the fallback stack and no Lato binary is packaged. The pinned brand.tokens.json and primary brand_spec/brand.json both require Lato."
      },
      {
        "criterion": "F5-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-5.reporting-tab.proof_of_spec.json@3ab6275f9f9aba603571e87c573e3ed21fc1eb98",
        "verdict": "FAIL",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-5.reporting-tab.md F5-AC8: The screen and print captures do not use a shared payload: figures differ and the screen return is shown as a raw decimal without an explicit percentage unit. Mobile report columns are clipped. Same figures/labels/units and legible units are not established by sharing a conceptual report type."
      },
      {
        "criterion": "F6-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-6.analysis-tab.proof_of_spec.json@854594d51a6ba1accb25d8d965b1c188ea3121dd",
        "verdict": "NOT_EVALUATED",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-6.analysis-tab.md F6-AC8: The required two PNGs contain status panels, not AnalysisTab’s clean/correction input views or modeled sections. The substantive visual surface is unreachable in those artifacts. The later FE-s-11 ready view shows modeled content but supplies no paired clean/correction replacement for this bar."
      },
      {
        "criterion": "F7-AC7",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-7.holdings-tab.proof_of_spec.json@277a7199ac4cccc82977dd33dd07f3bedcf89076",
        "verdict": "NOT_EVALUATED",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-7.holdings-tab.md F7-AC7: Both required F7 PNGs contain status panels rather than the holdings hierarchy. The later SmartX view proves mounting only; no replacement target/blend/missing-attribution capture supplies the missing visual comparison. Field-level tests do not make that absent visual surface observable."
      },
      {
        "criterion": "F8-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-8.narrative-page.proof_of_spec.json@24c4b211b2b296e21a046d05353a852c5e40f8d8",
        "verdict": "NOT_EVALUATED",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-8.narrative-page.md F8-AC8: The required PNG shows the old FE-s-4 narrative placeholder rather than PeriodInContextPage, and shows no missing-history case. Later wiring tests pass but the fresh FE-s-11 print has narrative off. The required contemporaneity/absent-history visual surface remains unobserved."
      },
      {
        "criterion": "F9-AC8",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-9.export-options-preview.proof_of_spec.json@7db8bed41ba4ce4e9739d15ce3bc13e959848bad",
        "verdict": "FAIL",
        "reason": "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-9.export-options-preview.md F9-AC8: The options read as a portal modal and preview uses the shared template. Applied branding is not stated as an applied result: the Opal button is a requested option, while AppliedBranding remains unmounted. A selected option does not prove which approved assets the rendered bundle applied."
      }
    ]
  }
]
```
