# POSN_ASTTAX - ADJUDICATION v4, round 3, site Z

L8 review of all 24 new original investigation items is recorded below; 49 original items exist across both roots. Of the 24 newly reviewed items: {'DISMISSED_WITH_REASON': 6, 'GRADUATED': 17, 'UNDER_INVESTIGATION': 1}. W14-S1 remains formally pending; the CVO's own missing-repair-cell proposal C-S64 is also pending. L9 is therefore not fully disposition-complete and no L10 slug is issued.

Whole-project terminality: 15 orders, 11 terminal, four staged (S2-1, S3-1, T6-1, T7-1). Five new proof instances are freshly structurally VALID against their issued criterion IDs; six earlier proof instances retain their prior reviewed grades. No order status is changed. CTO 21814's T6 hold remains; the named round-2 exception is not generalized. The gate source at check_file explicitly subjects new DECOMP_INVALIDATING rows to L10 preconditions.

Evidence: `org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json` (intake row/proof snapshot) and `org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json` (new offline controls and source reads). Source pin 3ce0c0e372; portal object pin e85f6eb84f; seed source pin 8adab5748d2b58091bb0a19ebf16e15e27846e47. Evidence records worker proof commit IDs rather than accepting their PENDING-THIS-COMMIT placeholder as a hash. No downloaded pickle is executed. No live AWS call, retag, deployment, portal build or DOM exercise is performed by these CVO controls.

Basis: graduation requires an attributed mechanism, denominator and remedy holder; dismissal requires a stated counterexample, bounded non-defect or resolved instance. Severity and sender identity do not determine disposition. A missing read/grant in an existing cell does not itself invalidate the decomposition. A genuinely absent repair/deployment act is a separate proposed DI and remains pending while the repository gate bars it. C-S60 explicitly corrects the old W4-S2 category without rewriting its history.

C-S61 holds the five judgment grades. A scoped code-output PASS is not a served-system safety PASS. The bar remains NO-GO on the reproduced deployed-code exception, regardless of the rejected overclaims in W14-S8 and the matrix. Eleven tested candidate targets are not eleven approved membership decisions. No FWD is claimed REALIZED.

```json
[
  {
    "id": "POSN_ASTTAX-Z-C-S36",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "This is the closure report for S7, not a second implementation defect. Its doc/cron/retraction claims are attributed to the CTO record. A commit subject containing the fence is not proof that tick-25 ran the fence; no independent CVO runtime reenactment is claimed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-S36",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "POSN_ASTTAX-Z-S7 asserts that the false belief is ACTIVELY PROPAGATING across three carriers -- CLAUDE.md's law text, a live 10m cron body, and three delivered messages -- and that the next COO to re-cut an order mid-round will inherit it.",
    "world_is": "This is the closure report for S7, not a second implementation defect. Its doc/cron/retraction claims are attributed to the CTO record. A commit subject containing the fence is not proof that tick-25 ran the fence; no independent CVO runtime reenactment is claimed.",
    "notes": "S7 receives the grounded disposition; duplicate closure information needs no new remedy.",
    "dismissal_reason": "S7 receives the grounded disposition; duplicate closure information needs no new remedy.",
    "adjudicates": [
      "POSN_ASTTAX-Z-S36"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S37",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The old one-artifact safety boundary omitted the frontend and sibling consumers. The later four-clause bar widens the named boundary, resolving this specification instance; actual UI and producer defects remain separate findings. The current code read confirms allocation-summary READS holdings_attribution_data.json and writes allocation_summary.json: do not propagate the reversed producer attribution in earlier prose.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-S6",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "PRD v0.5 s.4 step (2), as re-founded @49ddcc481d, states the retag's gate as a CONDITION read FROM THE SERVED ARTIFACT, and the round-3 decomposition makes AT3-s-5 that gate: AT3-s-6 fires on its GO.",
    "world_is": "The old one-artifact safety boundary omitted the frontend and sibling consumers. The later four-clause bar widens the named boundary, resolving this specification instance; actual UI and producer defects remain separate findings. The current code read confirms allocation-summary READS holdings_attribution_data.json and writes allocation_summary.json: do not propagate the reversed producer attribution in earlier prose.",
    "notes": "Existing C-RETAG-SAFETY scope correction; preserve historical source vintages. No retag is admitted by the document change.",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-S6"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S38",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The old claimed LIMB-6 fence did not cover M-only changes. The row reports two recuts and zero evaluator calls, not an observed unsigned issuance. The subsequent CLAUDE.md amendment ab642b92e5 relocates the mandatory signoff read; S36 supplies the owner closure record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-S7",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "CLAUDE.md Rule 27 states without qualification that .tools/to-pipeline-gate.py LIMB 6 REFUSES a task order against a PRD with a half not SIGNED -- which reads as a standing mechanical backstop protecting every task order from a stale or unsigned PRD half.",
    "world_is": "The old claimed LIMB-6 fence did not cover M-only changes. The row reports two recuts and zero evaluator calls, not an observed unsigned issuance. The subsequent CLAUDE.md amendment ab642b92e5 relocates the mandatory signoff read; S36 supplies the owner closure record.",
    "notes": "The current law carrier was repaired inside the round. Keep the historical assertion and its correction distinct; do not credit the old hook with coverage it lacked.",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-S7"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S39",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The staged T6 binds an obsolete brief and assumes fresh generation where the downloaded deployed bytes raise on all 11 candidate targets. The current artifact could remain stale; absence of a fresh write is not measured blank UI. CTO 21814 explicitly forbids repinning, recutting or spawning T6 ahead of deployment/scope resolution.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-S8",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "PRD v0.5 C-RETAG-SAFETY at f9458a7e43 states that the KeyError/page-blank mechanism is LIVE AT THE SERVED PLANE and that the silent-zeroing text describes THE MECHANISM AT HEAD, POST-DEPLOY. Step (3) retags only after step (2)'s bar is MET.",
    "world_is": "The staged T6 binds an obsolete brief and assumes fresh generation where the downloaded deployed bytes raise on all 11 candidate targets. The current artifact could remain stale; absence of a fresh write is not measured blank UI. CTO 21814 explicitly forbids repinning, recutting or spawning T6 ahead of deployment/scope resolution.",
    "notes": "Existing T6 instrument and prerequisites need correction at an authorized recut. No pending order is changed. A fail-closed freshness criterion is possible; it cannot substitute for the missing deployment act.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-S8"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S40",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "At the issued source base 651ffd4f16, the raw allocation already carried 2.5 while the five-class label was Unknown and the class delta/spread were absent. This falsifies the no-else/source-zero mechanism at that pin. It does NOT make the deployed KeyError historical: T5 and CVO separately reproduce the exception on downloaded deployed bytes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W10-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "PRD s.4 C-RETAG-SAFETY, this order's worker face and decomp cell AT3-s-1 all state the LIVE mechanism as: the allocation if/elif chain has NO else, so a Commodities or Structured value renders as the literal 'Unknown' AND its weight accumulates to 0.000. The PRD marks only the 17/3/14 RATIO as historical and states the mechanism itself as current and measured.",
    "world_is": "At the issued source base 651ffd4f16, the raw allocation already carried 2.5 while the five-class label was Unknown and the class delta/spread were absent. This falsifies the no-else/source-zero mechanism at that pin. It does NOT make the deployed KeyError historical: T5 and CVO separately reproduce the exception on downloaded deployed bytes.",
    "notes": "The brief was corrected within the round at f9458a7e43; preserve separate source-code and deployed-code vintages. Code-before and registry-before are different controls.",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W10-S1"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S41",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The source benchmark ETF map covers cash, fixed_income and equity; those are not three independent ratified classes because cash/fixed income share one top-level class. Structured, Commodities and Alternatives lack an explicit benchmark choice. Available-only selection and cash fallback are source mechanisms, but a small current VXX weight does not prove universal safety.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W10-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "Cell AT3-s-1 orders every hop where an asset_class value is mapped, branched, bucketed or rendered on the served path to carry all five ratified classes, so that a correctly-tagged ticker renders under its own label with its weight intact.",
    "world_is": "The source benchmark ETF map covers cash, fixed_income and equity; those are not three independent ratified classes because cash/fixed income share one top-level class. Structured, Commodities and Alternatives lack an explicit benchmark choice. Available-only selection and cash fallback are source mechanisms, but a small current VXX weight does not prove universal safety.",
    "notes": "Settle the benchmark policy and unknown-class behavior at the existing generator comparison contract. CVO does not invent ETFs or declare zero benchmark weights wrong without that contract.",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W10-S2"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S42",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The new generator normalizes case, spaces, hyphens and several aliases, while the staged registry writer has no settled raw spelling. The ratified labels are fixed; raw encoding is a distinct contract. Seven CVO source controls preserve the six recognized spellings/classes and expose an unknown-class warning control.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W10-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "The order's act is to make every hop carry the five ratified classes so a correctly-tagged ticker renders under its own label, and its BOUNDS forbid retagging any registry row and minting a sixth class. It names the five by LABEL and leaves the raw registry spelling unspecified.",
    "world_is": "The new generator normalizes case, spaces, hyphens and several aliases, while the staged registry writer has no settled raw spelling. The ratified labels are fixed; raw encoding is a distinct contract. Seven CVO source controls preserve the six recognized spellings/classes and expose an unknown-class warning control.",
    "notes": "The existing retag issuance must bind raw values to the generator contract, without minting a sixth ratified class or duplicating independent alias vocabularies.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W10-S3"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S43",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The superproject gitlink cannot be read as portal source and a sparse cone cannot supply absent files. T2 recovered through the portal object store at e85f6eb84f. CVO independently read the same consumer and both category callers there.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W11-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "TO-T2-1 BOUNDS: 'portal/ is outside your sparse cone. If you need to read it, widen your OWN worktree's cone (`git sparse-checkout add portal`) or read blobs via `git show HEAD:<path>`', and criteria T2-AC1/T2-AC3 name `comp-find ... --all --files` as the invocation that produces 'the PORTAL subset named explicitly'.",
    "world_is": "The superproject gitlink cannot be read as portal source and a sparse cone cannot supply absent files. T2 recovered through the portal object store at e85f6eb84f. CVO independently read the same consumer and both category callers there.",
    "notes": "Correct the existing measurement order instrumentation and exact repository/pin. Current read gap recovered; no portal write authorization follows.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W11-S1"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S44",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The 14-commit portal vintage difference is disclosed and the subject files reportedly have no diff between the compared pins. A moving branch is not a defect once evidence is explicitly bound to e85f6eb84f.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W11-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "TO-T2-1 treats 'portal' as a single readable object -- 'the PORTAL subset named explicitly' -- and names no commit at which the portal bytes are to be read.",
    "world_is": "The 14-commit portal vintage difference is disclosed and the subject files reportedly have no diff between the compared pins. A moving branch is not a defect once evidence is explicitly bound to e85f6eb84f.",
    "notes": "No remaining repair is demonstrated by this vintage observation. It is not evidence about the deployed bundle.",
    "dismissal_reason": "No remaining repair is demonstrated by this vintage observation. It is not evidence about the deployed bundle.",
    "adjudicates": [
      "POSN_ASTTAX-Z-W11-S2"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S45",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "T2 reports 1201 tree entries: 1200 blobs and one nested archive/dashboard gitlink; 1113 text reads and 87 binary exclusions. The unread nested repository and binaries limit a whole-estate claim, but this row does not establish an omitted active frontend consumer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W11-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "T2-AC1 <expect>: 'a stated count of files READ versus files UNREADABLE. If anything is unreadable, say so and say why -- an unreadable file is not an absent consumer.'",
    "world_is": "T2 reports 1201 tree entries: 1200 blobs and one nested archive/dashboard gitlink; 1113 text reads and 87 binary exclusions. The unread nested repository and binaries limit a whole-estate claim, but this row does not establish an omitted active frontend consumer.",
    "notes": "Accept the bounded source read and its exclusions. No all-runtime or transitive-repository closure is inferred.",
    "dismissal_reason": "Accept the bounded source read and its exclusions. No all-runtime or transitive-repository closure is inferred.",
    "adjudicates": [
      "POSN_ASTTAX-Z-W11-S3"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S46",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The 93 occurrences on 67 lines and 49 occurrences on 32 lines are different units at the same source vintage, not evidence that the issuer read stale files.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W12-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "TO-T3-1's cell (inheriting TO-S7-1) asserts the two sibling consumers carry 67 and 32 asset_class HITS respectively.",
    "world_is": "The 93 occurrences on 67 lines and 49 occurrences on 32 lines are different units at the same source vintage, not evidence that the issuer read stale files.",
    "notes": "Retain occurrence-versus-line denominators. No code or scope change follows.",
    "dismissal_reason": "Retain occurrence-versus-line denominators. No code or scope change follows.",
    "adjudicates": [
      "POSN_ASTTAX-Z-W12-S1"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S47",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The sibling source passes an unfamiliar class through despite the stale folds-to-Equity comment. Its fixed benchmark map defaults the missing class policy weight to zero, so a 10.0 style weight produces a 10.0 bet. This is a measured fallback and a missing explicit policy, not proof that every zero benchmark is financially wrong.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W12-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "The cell AT3-s-3 asks whether either sibling 'buckets asset_class into its own fixed-key structure' such that a retag 'silently zeroes or mislabels there too'. yang-generate-allocation-summary's own comment at :44 asserts Commodities is folded into Equity.",
    "world_is": "The sibling source passes an unfamiliar class through despite the stale folds-to-Equity comment. Its fixed benchmark map defaults the missing class policy weight to zero, so a 10.0 style weight produces a 10.0 bet. This is a measured fallback and a missing explicit policy, not proof that every zero benchmark is financially wrong.",
    "notes": "Recut the existing sibling measurement to bind and discriminate the benchmark policy; actual implementation repair outside this read-only cell is part of the pending missing-cell finding C-S64.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W12-S2"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S48",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The two-class assumption survives in four different mechanisms: the len==2 tilt guard, two-name ordering, two-row fallback and a normalization gap assigned to the largest row. The worker reports 88 exercised hop-lines (80 five-class plus 8 control/error cases), not 88 independent production surfaces.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W12-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "The cell frames the risk as a consumer that 'silently zeroes or mislabels' a retagged value, and asks per hop whether Commodities SURVIVES, RAISES or is SILENTLY DROPPED.",
    "world_is": "The two-class assumption survives in four different mechanisms: the len==2 tilt guard, two-name ordering, two-row fallback and a normalization gap assigned to the largest row. The worker reports 88 exercised hop-lines (80 five-class plus 8 control/error cases), not 88 independent production surfaces.",
    "notes": "Give each mechanism its own acceptance obligation within the sibling assessment; avoid replacing them with a blanket two-class claim. Missing repair acts are assessed separately in C-S64.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W12-S3"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S49",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The instruction to measure uncommitted seed-etf-constituents edits named shared SITEZ state that was absent from the worker linked checkout. The preserved patch is a separate artifact, not those checkout bytes. Its cash canonicalization and empty-index-key repairs must not be inferred present from a clean git status.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W13-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "TO-T4-1 BOUNDS: 'MEASURE THE WORKTREE, NOT JUST HEAD. seed-etf-constituents.py carries UNCOMMITTED bytes preserved at 5c9e329a21 (13 insertions / 6 deletions, another seat's, reviewed by nobody) ... the difference is invisible unless you look. Do not apply or commit those bytes; read, and say what you read.'",
    "world_is": "The instruction to measure uncommitted seed-etf-constituents edits named shared SITEZ state that was absent from the worker linked checkout. The preserved patch is a separate artifact, not those checkout bytes. Its cash canonicalization and empty-index-key repairs must not be inferred present from a clean git status.",
    "notes": "Bind the existing durability cell to the exact preserved patch/carrier and assess it before any later seeder act; preserve the other owner worktree.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W13-S1"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S50",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The historical producer encounters 16 empty sub_asset_class values in 136 tickers, with ACSG in the first batch; the worker measured the table index constraint and a paired conditional-request control. The new merge drops empty fields and preserves curated fields together. CVO normal/conflict/scan-denied controls confirm the new source paths, but do not repeat the live-table probe.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W13-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "TO-T4-1 THE CELL: 'seed-etf-classifications.py does an unconditional full-item put over the whole ticker universe ... So a seed run rewrites management_style back to \"unknown\" on exactly the six rows AT2-s-5 corrected', and 'A deliberate manual run still reverts everything.'",
    "world_is": "The historical producer encounters 16 empty sub_asset_class values in 136 tickers, with ACSG in the first batch; the worker measured the table index constraint and a paired conditional-request control. The new merge drops empty fields and preserves curated fields together. CVO normal/conflict/scan-denied controls confirm the new source paths, but do not repeat the live-table probe.",
    "notes": "The named seeder crash is repaired in the worker commit. Closing that crash alone on old overwrite code would arm a revert. The sibling patch and concurrent-curation risk remain separate.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W13-S2"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S51",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The worker removed one unused import and three extraneous f-string prefixes within the granted script. These pre-existing lint defects were corrected in the delivered change.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W13-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "CLAUDE.md Rule 14: 'Every `.py` edit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39). Universal.' TO-T4-1 CLOSING OUT names one commit via safe-commit.sh and grants exactly five paths; it names no lint remediation.",
    "world_is": "The worker removed one unused import and three extraneous f-string prefixes within the granted script. These pre-existing lint defects were corrected in the delivered change.",
    "notes": "No remaining separate remediation is demonstrated; no claim is made that earlier historical commits passed the current linter.",
    "dismissal_reason": "No remaining separate remediation is demonstrated; no claim is made that earlier historical commits passed the current linter.",
    "adjudicates": [
      "POSN_ASTTAX-Z-W13-S3"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S52",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The downloaded Lambda source has 94164 bytes and md5 cc79aff7506f8c39e17453f386c69551. CVO independently reproduced 11/11 candidate AFTER exceptions against 11/11 successful repaired-source AFTER arms. This establishes an unsafe generation precondition; it does not demonstrate live page blanking or a performed retag. All seven decomposition cells were read; none deploys the repaired source.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W14-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "PRD s.4 C-RETAG-SAFETY states the KeyError/page-blank mechanism is HISTORY and no longer operative, and that the live mechanism is silent zeroing at a page that still renders. Round 3's chain A (AT3-s-1 -> AT3-s-5 -> AT3-s-6) treats AT3-s-1's commit as the act that 'makes the bar meetable'.",
    "world_is": "The downloaded Lambda source has 94164 bytes and md5 cc79aff7506f8c39e17453f386c69551. CVO independently reproduced 11/11 candidate AFTER exceptions against 11/11 successful repaired-source AFTER arms. This establishes an unsafe generation precondition; it does not demonstrate live page blanking or a performed retag. All seven decomposition cells were read; none deploys the repaired source.",
    "notes": "PROPOSED DECOMP_INVALIDATING: a deployment/effective-artifact verification act is absent. Formal disposition waits the measured L10 terminality gate: S2/S3/T6/T7 are staged. Round-2 exception is not reused. CTO 21814 holds T6; no deployment is performed.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W14-S1"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S53",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The worker full-table subtraction is 285 minus 274 = 11 CANDIDATES, not eleven approved semantic decisions. The inherited seven-member hedge set omits UVXY, QBER and PDBC plus the separately named VXX. QBER/PDBC remain membership calls under C-MEMBERSHIP-AT-L5. The attribution artifact contains 31 rows for four candidates, so Models-only held status is not the whole blast radius.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W14-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "PRD s.4 C-VOL-HEDGE-STRUCTURED states the retag population as 'SEVEN tickers: SIX commodities (DBC, GLD, GSG, IAU, SLV, USO) and ONE volatility (VIXY)', plus VXX named separately as 'currently mis-served equity'. TO-T5-1's T5-AC1 invocation enumerates exactly eight keys and invites a differing set to be stated.",
    "world_is": "The worker full-table subtraction is 285 minus 274 = 11 CANDIDATES, not eleven approved semantic decisions. The inherited seven-member hedge set omits UVXY, QBER and PDBC plus the separately named VXX. QBER/PDBC remain membership calls under C-MEMBERSHIP-AT-L5. The attribution artifact contains 31 rows for four candidates, so Models-only held status is not the whole blast radius.",
    "notes": "Settle and bind the candidate set in the existing retag cell before issuance. No candidate target in the CVO control is a new classification authorization.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W14-S2"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S54",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "CVO parsed all 57 CANONICAL_SECURITIES and verified the --upload --yang update_item path: four candidates intersect (QBER, UVXY, VXX, PDBC). Its SET asset_class replaces that field even though unrelated attributes are preserved. The named T4 seeder guard cannot govern this second writer. Automatic scheduling was not measured; the evidenced trigger is deliberate invocation.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W14-S3",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "Decomp round 3 cell AT3-s-4 frames registry durability as a property of ONE producer -- 'seed-etf-classifications.py does an unconditional full-item put ... Make the registry hold its values against a re-seed' -- and TO-T4-1 closed on that file. PRD s.4 step (3) requires the retag to land in BOTH stores and cites AT3-s-4's refusal as the mechanism that makes it durable.",
    "world_is": "CVO parsed all 57 CANONICAL_SECURITIES and verified the --upload --yang update_item path: four candidates intersect (QBER, UVXY, VXX, PDBC). Its SET asset_class replaces that field even though unrelated attributes are preserved. The named T4 seeder guard cannot govern this second writer. Automatic scheduling was not measured; the evidenced trigger is deliberate invocation.",
    "notes": "The existing registry-durability cell must include the second writer in its coverage/permission assessment. Do not run it or silently retag these four. Implementation across another owning surface needs the CTO scope decision.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W14-S3"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S55",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The additional ETF publisher is a positive counterexample to the closed two-sibling set. It copies gold holding class values and emits a four-key book allocation at source lines 469-472. The live artifact had 189 rows over four books and zero candidate members; its current bytes do not exercise post-retag loss for those absent members.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W14-S4",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "PRD s.4 C-RETAG-SAFETY names the surfaces a retagged value reaches as positioning_data.json (the Models artifact), a portal tab, and the yang-generate-allocation-summary sibling writing holdings_attribution_data.json, and the worker quote it adopts is 'Data reaches three lambdas; the code hardening reaches one.'",
    "world_is": "The additional ETF publisher is a positive counterexample to the closed two-sibling set. It copies gold holding class values and emits a four-key book allocation at source lines 469-472. The live artifact had 189 rows over four books and zero candidate members; its current bytes do not exercise post-retag loss for those absent members.",
    "notes": "The CTO must settle this existing owning surface coverage at the project boundary. No POSN worker is authorized to rewrite another project publisher; candidate reach is distinguished from a currently held row and from classifier use for non-class fields.",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W14-S4"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S56",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "Code-before means new class on old source; registry-before means old class on a chosen source. Under the latter comparison CVO reproduced 0-to-weight movement in the raw target allocation on repaired source. This does not make a raw allocation interchangeable with the requested label-grouped weight or prove the rendering loop includes the group.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W14-S5",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "PRD s.4 and TO-T5-1 both assert, in bold, that the allocation-dict entry 'reads IDENTICALLY in the healthy world and the broken one' and that '(b) evidence that does not move between BEFORE and AFTER is the wrong column'.",
    "world_is": "Code-before means new class on old source; registry-before means old class on a chosen source. Under the latter comparison CVO reproduced 0-to-weight movement in the raw target allocation on repaired source. This does not make a raw allocation interchangeable with the requested label-grouped weight or prove the rendering loop includes the group.",
    "notes": "Name both comparisons and their units in the existing bar. The earlier equal 2.5/2.5 example remains valid only for its code-change control.",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W14-S5"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S57",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The worker comp-find invocation disclosed 29824 unreadable files alongside 3655 scanned files. Its later object-store census read 33514 blobs plus two named gitlinks in 33516 entries. These are distinct domains/instruments. Printed token counts alone do not establish dataflow reach; the later exclusion of 118 code files on absent registry tokens is also not a proof of unreachable consumers.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W14-S6",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "T5-AC2 names comp-find as the invocation that yields the printed denominator and full file list from which the surface set is to be derived by subtraction, and the cell's own star clause says the surface set is 'THE PART WITH NO PRIOR ART'.",
    "world_is": "The worker comp-find invocation disclosed 29824 unreadable files alongside 3655 scanned files. Its later object-store census read 33514 blobs plus two named gitlinks in 33516 entries. These are distinct domains/instruments. Printed token counts alone do not establish dataflow reach; the later exclusion of 118 code files on absent registry tokens is also not a proof of unreachable consumers.",
    "notes": "Repair the existing census criterion for sparse checkout and indirect reach. The tool disclosed its limit; the mistake is treating that limit as an exhaustive surface universe.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W14-S6"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S58",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "At the reported Models artifact only VXX of 11 candidates is held; ten have zero rows. NONZERO and equal to zero cannot both hold there. Attribution instead has four held candidates. A synthetic 0.025 control answers survival if held, not current live weight preservation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W14-S7",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "Step (2) states clause (b) as a conjunction that must hold for EVERY ticker in the retag set on EVERY served surface.",
    "world_is": "At the reported Models artifact only VXX of 11 candidates is held; ten have zero rows. NONZERO and equal to zero cannot both hold there. Attribution instead has four held candidates. A synthetic 0.025 control answers survival if held, not current live weight preservation.",
    "notes": "Make the existing bar surface- and held-status-specific. CVO does not adopt the suggested requirement to fabricate zero-weight rows for every absent ticker; that is an additional product decision.",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W14-S7"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S59",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The headline top-level-class override is falsified at e85f6eb84f. Full src search finds two getETFCategory callers; both consume category.segment as a sub-asset-class fallback, not category.assetClass. HoldingsTab groups by holding.asset_class from the artifact. Four stale map values and type unions therefore do not establish four live top-level overrides.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json#POSN_ASTTAX-Z-W14-S8",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json"
      ]
    },
    "spec_asserts": "C-ONE-SOURCE: 'the classification originates in ONE place and flows to every surface; no surface re-implements it', SETTLED at v0.4 to mean the served TABLE is the one place. The known frontend collapse site is recorded as the hardcoded assetClassOrder at HoldingsTab.tsx:1392-1394.",
    "world_is": "The headline top-level-class override is falsified at e85f6eb84f. Full src search finds two getETFCategory callers; both consume category.segment as a sub-asset-class fallback, not category.assetClass. HoldingsTab groups by holding.asset_class from the artifact. Four stale map values and type unions therefore do not establish four live top-level overrides.",
    "notes": "Dismiss that causal claim. The independent two-class rendering loop and missing class/color coverage are real and remain in T2/T5 evidence and C-S64; widening the loop is not claimed to fix all UI behavior. No deployed DOM was exercised.",
    "dismissal_reason": "Dismiss that causal claim. The independent two-class rendering loop and missing class/color coverage are real and remain in T2/T5 evidence and C-S64; widening the loop is not claimed to fix all UI behavior. No deployed DOM was exercised.",
    "adjudicates": [
      "POSN_ASTTAX-Z-W14-S8"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S60",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "Correction to C-S18/C-S31: W4-S2 proved an incomplete read of an already specified frontend contract, not a missing decomposition cell. The S7 order explicitly names that hop in THE ACT lines 31-34. The correct category is a grounded measurement/instrument failure in the existing cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S7-1.verify-the-five-class-chain.md:31",
        "org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/adjudications/ADJUDICATION_v3.md#POSN_ASTTAX-Z-C-S31"
      ]
    },
    "spec_asserts": "DECOMP_INVALIDATING requires a remedy needing a cell the decomposition does not contain.",
    "world_is": "Correction to C-S18/C-S31: W4-S2 proved an incomplete read of an already specified frontend contract, not a missing decomposition cell. The S7 order explicitly names that hop in THE ACT lines 31-34. The correct category is a grounded measurement/instrument failure in the existing cell.",
    "notes": "Supersedes only the W4-S2 DI category by a new citing row, preserving the old record. Round-3 T2 has now recovered the source read; it has not fixed or exercised the deployed frontend. A new read-only cell was a COO workflow choice, not proof that the original decomposition lacked this obligation.",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "adjudicates": [
      "POSN_ASTTAX-Z-W4-S2"
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S61",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "Five round-3 judgment grades: two scoped PASS, two FAIL, one NOT_EVALUATED. Retag remains NO-GO.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_INTAKE_20260912_Z.json"
      ]
    },
    "spec_asserts": "L9 grades each judgment against the specification that issued it, separately from structural proof validity.",
    "world_is": "Five round-3 judgment grades: two scoped PASS, two FAIL, one NOT_EVALUATED. Retag remains NO-GO.",
    "notes": "Grade carrier; the mechanical checker is not the truth grader. Six older proof instances retain their prior CVO grades; five new instances are freshly structure-checked against criterion IDs read from the issued orders. No historical source result is promoted to a current deployed claim.",
    "dismissal_reason": "Grade carrier; the mechanical checker is not the truth grader. Six older proof instances retain their prior CVO grades; five new instances are freshly structure-checked against criterion IDs read from the issued orders. No historical source result is promoted to a current deployed claim.",
    "grades": [
      {
        "criterion": "T1-AC6",
        "instance": "org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~10/POSN_ASTTAX.TO-T1-1.carry-five-classes-through-the-generator.proof_of_spec.json@07c046fa63f4558a67c27e7026f1d07923bd2b32",
        "verdict": "PASS",
        "reason": "Within the issued SOURCE CHANGE ONLY boundary, the real generator output carries all five classes, including cash/fixed-income spellings, with populated labels, weights and class delta/spread. CVO independently exercised six recognized raw classes and an unknown control, plus 11 candidate before/after inputs. This passes the generator output contract only; it does not pass deployment, benchmarks not specified by the order, sibling consumers or DOM safety."
      },
      {
        "criterion": "T2-AC5",
        "instance": "org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~11/POSN_ASTTAX.TO-T2-1.measure-the-frontend-hop.proof_of_spec.json@bab2cf66a2fcfcbe3886989a881f92f0369f29dd",
        "verdict": "PASS",
        "reason": "The specific unread frontend-contract gap is now closed at SOURCE-AT-PIN: 42/42 reported frontend consumer files read, 1113 text blobs plus 87 binary exclusions and one named nested gitlink. CVO checked the actual grouping loop and category call sites. The result is a demonstrated source collapse, not a successful UI. No all-runtime closure, portal change, deployment or DOM exercise is passed."
      },
      {
        "criterion": "T3-AC4",
        "instance": "org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~12/POSN_ASTTAX.TO-T3-1.hop-test-the-two-sibling-consumers.proof_of_spec.json@5899484453a8c5e152ca8f9c2d8adfa9be810a15",
        "verdict": "FAIL",
        "reason": "The two measured siblings are not the whole producer set. The data/etfs positioning publisher is a positive additional consumer/producer identified by W14-S4; its distinct served artifact and four-key payload were read. A 290-file/20-token-carrier sweep that classifies only two does not close the remainder. The local two-function measurements remain useful."
      },
      {
        "criterion": "T4-AC5",
        "instance": "org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~13/POSN_ASTTAX.TO-T4-1.registry-durability-the-re-seed-revert.proof_of_spec.json@8adab5748d2b58091bb0a19ebf16e15e27846e47",
        "verdict": "FAIL",
        "reason": "The default named seeder improves: CVO normal arm writes 136 rows, conflict arm refuses with rc3/0 writes and Scan-denied arm fails closed rc2/0 writes. But a CVO controlled curation between the scan and batch put is lost (curator_note B becomes old A, rc0); the snapshot merge is not concurrent durability. The 57-entry second writer overlaps four candidates, and explicit override flags also bypass preservation. No live concurrent edit is claimed."
      },
      {
        "criterion": "T5-AC8",
        "instance": "org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~14/POSN_ASTTAX.TO-T5-1.the-bar-step-2-measured-against-the-served-artifact.proof_of_spec.json@063312e4f33e36095ae751f0abcf5970cb5f88cc",
        "verdict": "NOT_EVALUATED",
        "reason": "The universal surface-set claim is not established: absent registry tokens exclude 118 code files without proving transitive dataflow absence, runtime/deployed consumers remain unread, and 132/836 reported cells are NOT-MEASURABLE-HERE. A4 has zero candidate members; R5/R6 claim a class override their call sites do not perform. The concrete generator counterexample nevertheless supports safety NO-GO. Completion of this measurement does not pass its universal property or all its table entries."
      }
    ]
  },
  {
    "id": "POSN_ASTTAX-Z-C-S62",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The T5 836-cell table repeats some source inferences as per-member exercised failures. A4-b/d are marked MEASURED-EXERCISED for 11 candidates despite zero candidate rows in that live artifact. R5/R6 assign top-level override failures even though the only callers read segment. Its 473 FAIL count is not an independently verified count of post-retag regressions.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json",
        "org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~14/t5_bar_table.py"
      ]
    },
    "spec_asserts": "A cell labeled exercised must carry a control that actually exercises the stated member, surface and clause.",
    "world_is": "The T5 836-cell table repeats some source inferences as per-member exercised failures. A4-b/d are marked MEASURED-EXERCISED for 11 candidates despite zero candidate rows in that live artifact. R5/R6 assign top-level override failures even though the only callers read segment. Its 473 FAIL count is not an independently verified count of post-retag regressions.",
    "notes": "Repair the existing bar instrument and evidence-grain labels. Preserve the valid NO-GO counterexample. The table mixes source files, stores and rendered surfaces; summing its rows is not a count of independent product surfaces. No DOM result is claimed.",
    "disarm_owner": "2.0.0_SA_COO~Z"
  },
  {
    "id": "POSN_ASTTAX-Z-C-S63",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The repaired seed_table scans a snapshot and later performs full-item batch puts without comparing the current item. In a paired actual-function control, normal preserves curator_note A; concurrent curation to B after scan is overwritten back to A, rc0 and 136 writes. Conflict and Scan-denied controls correctly refuse before writing.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json#reseed_controls",
        "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py@8adab5748d2b58091bb0a19ebf16e15e27846e47"
      ]
    },
    "spec_asserts": "AT3-s-4 asks whether the registry survives a re-seed rather than only the simulation supplied.",
    "world_is": "The repaired seed_table scans a snapshot and later performs full-item batch puts without comparing the current item. In a paired actual-function control, normal preserves curator_note A; concurrent curation to B after scan is overwritten back to A, rc0 and 136 writes. Conflict and Scan-denied controls correctly refuse before writing.",
    "notes": "Existing registry-durability cell: measure and bind the concurrent-update contract, then prevent lost curation or explicitly enforce an exclusive writer window. This is a controlled possibility, not a report of live concurrent activity. No additional permissions or production write was used.",
    "disarm_owner": "2.0.0_SA_COO~Z"
  },
  {
    "id": "POSN_ASTTAX-Z-C-S64",
    "project": "POSN_ASTTAX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-12T00:23:09Z",
    "one_line": "The seven-cell round-3 cut repairs generator source and one seeder, measures frontend/sibling/bar paths, then retags/reconciles. It contains no frontend repair or sibling implementation repair act, while actual HoldingsTab source groups only Fixed Income/Equity and omits a new class from orderedGroups but includes it in grandTotal. The frontend measurement cell is present; the distinct repair act is absent.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/POSN_ASTTAX_ROUND3_CVO_EVIDENCE_20260912_Z.json#portal_snippets",
        "org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md"
      ]
    },
    "spec_asserts": "The declared decomposition domain is everything needed to make step (2) true, before the retag; measurement and repair are distinct acts.",
    "world_is": "The seven-cell round-3 cut repairs generator source and one seeder, measures frontend/sibling/bar paths, then retags/reconciles. It contains no frontend repair or sibling implementation repair act, while actual HoldingsTab source groups only Fixed Income/Equity and omits a new class from orderedGroups but includes it in grandTotal. The frontend measurement cell is present; the distinct repair act is absent.",
    "notes": "PROPOSED DECOMP_INVALIDATING, pending the L10 terminality gate, separate from the corrected historical W4-S2 misclassification. Scope/freeze decisions belong to CTO/Andrew; the COO recut follows the authorized L10 route. Do not edit portal or expand another owner project. Deployment is separately pending on the original W14-S1.",
    "disarm_owner": "2.0.0_SA_COO~Z"
  }
]
```
