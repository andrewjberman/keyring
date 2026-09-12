# IRPT_FNTEND round 2: CVO adjudication

Accumulating CVO review as round-two evidence arrives. This is NOT an L10 slug and no judgment criterion is graded here: round 2 is mid-flight, cells remain non-terminal, and no slug is cuttable on this project.

```json
[
  {
    "id": "IRPT_FNTEND-C-S45",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-12T02:05:00Z",
    "one_line": "DISARMING IRPT_FNTEND-S27, which named this seat its disarm_owner. The contradiction is REAL and the row's own framing UNDERSTATES it: the header's zero is not a count of the wrong field, it is an ABSENT field defaulted to empty and printed as a fact -- the performance wire payload carries no scope block at all, so there is no field on that route for the count to be pointed at.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "IRPT_FNTEND-S27 (2.0.0_SA_COO~F, ARMED, disarm_owner 3.0.0_SA_CVO): the served print document reads '0 account(s) in scope' on all four pages while page 3 lists account A-0001 and page 4's bundle scope names accounts A-0001; the row asks this seat for the L9 disposition and states the count 'is reading something other than the accounts the bundle carries'. The PRD's reporting contract: values print exactly as the source supplied them, and an absence renders as an explicit UNAVAILABLE with its reason, never as a silent zero.",
    "world_is": "CONFIRMED, and re-derived on a THIRD instrument -- S27 read the rendered PNG, F16-AC8 greps a console line, and this seat read the SOURCE and the FIXTURE. Three regions of one document have three different sources and nothing binds them: (1) portal/src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx:45 prints `{bundle.scope.accountIds.length} account(s) in scope`; (2) render/performance/AccountDetail.tsx:28 renders 'Accounts in this report' from a separate `accounts` prop, never from bundle.scope.accountIds; (3) page 4's bundle-scope line prints the client-composed bundle scope, which DOES name A-0001. THE DECISIVE READ, and it is what upgrades the row: the fixture the capture was taken against -- C:/tmp/wk-irpt_fntend-2-6-fe-s-16/portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-narrative.json -- is a route-keyed mock whose performance payload has keys ['dates','lineage','measurement_basis','optional_facts','returns'] and NO scope key; a recursive walk of the whole fixture finds `accountIds` ZERO times. The rendered account row comes from returns.account_detail = [{account_id: 'A-0001', level: 'Account', value: 0.0688}], which matches the PNG's A-0001 / 0.0688 exactly. So bundle.scope.accountIds is absent on the wire, is defaulted to an empty array before render, and [].length prints as the literal 0. THAT IS THE SILENT ZERO THE UNAVAILABLE CONVENTION EXISTS TO PREVENT, in its exact textbook form: an absent value rendering as a measured fact rather than as a stated absence. It also means the remedy is NOT 'point the count at the right field' -- on this route there is no such field to point it at, so a future cut must either carry scope on the wire or render UNAVAILABLE with its reason. NOT ASSERTED: how the count behaves on a server-issued bundle or a multi-account scope; neither was exercised and the denominator here is ONE document, ONE fixture, ONE scope, exactly as S27 stated its own limit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/render/performance/PerformanceDocument.tsx:45 -- `{bundle.scope.accountIds.length} account(s) in scope` (read at the workspace's portal gitlink, this seat's own read)",
        "portal/src/pages/InvestorReporting/render/performance/AccountDetail.tsx:28 -- 'Accounts in this report' rendered from an `accounts` prop, a different source from the header",
        "portal/src/pages/InvestorReporting/render/analysis/AnalysisDocument.tsx:179 -- the analysis document prints report.scope.accountIds.join(', '), a THIRD accounts source in the same render tree",
        "C:/tmp/wk-irpt_fntend-2-6-fe-s-16/portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-narrative.json -- performance payload data keys ['dates','lineage','measurement_basis','optional_facts','returns']; no scope key; recursive walk finds accountIds 0 times; returns.account_detail carries exactly one entry, account_id A-0001, value 0.0688",
        "IRPT_FNTEND-S27 @ the round-2 channel -- the originating row, its PNG pin 8094204b4eb99c77108b270dc530cdf2079a3f018d75ab214a2d0cbb696e100f and its stated denominator of 1",
        "NEGATIVE-CONTROL NOTE on the fixture read: the first open failed FileNotFoundError on the MSYS path /c/tmp/... under native Windows Python and succeeded on C:/tmp/... -- the absence was a path artefact and was resolved rather than reported as an absent fixture"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "DISARM DISCHARGED. S27's ARMED standing was waiting on this seat's judgment and nothing else; that judgment is recorded here, so the hazard is held rather than open. No repair is taken: the remediation lands in a cell nobody has been granted, this round's decomposition is FROZEN, and it is not a COO act -- exactly as S27 itself states. CARRIED TO L10, two items and they are separate: (1) the silent-zero defect above, with the remedy constrained by the fact that the wire carries no scope on this route; (2) S27's own observation that IRPT_FNTEND-W2-S13's recorded CAUSE is falsified -- W2-S13 attributed the zero to 'a client-composed bundle names no account set', and the page-4 bundle scope DOES name A-0001. ⭐ THE SECOND ITEM IS THE ONE THAT COSTS MONEY IF IT IS LOST: a wrong CAUSE sitting in the channel sends the next round's cut at the wrong surface, and it would have sent it at the bundle composer rather than at the wire contract. A correction row citing W2-S13 belongs in the next round's channel; this seat does not mutate W2-S13 in place, because corrections are NEW rows citing the old id. NO GRADE IS ASSERTED: F16-AC8 PASSES correctly on its own bar -- the resolver did resolve -- and nothing here touches it."
  }
]
```
