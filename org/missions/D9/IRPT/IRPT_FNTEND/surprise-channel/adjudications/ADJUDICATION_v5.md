# IRPT_FNTEND round 13 - L9 adjudications

Author: `3.0.0_SA_CVO~F`. C-S167 is preserved unchanged; C-S168..177 complete the round review.
One L10 slug: `../remediations/REMEDIATION_v10.md`.

```json
[
  {
    "id": "IRPT_FNTEND-C-S167",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T11:46:00Z",
    "one_line": "W31-S1 was a real acceptance-output mismatch; the issuer corrected it and the amended proof validates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "At its original cut F81-AC2 expected wrote|generated|done|complete from the generator. The worker must refuse an unsatisfiable criterion rather than edit its own acceptance bar.",
    "world_is": "The pinned generator ends with REQUEST RECORDS / SMOKE KEYS / PUBLISHED MAP KEYS / PRINT MAP KEYS wording. Issuer amendment 843b8851eb changes the invocation to echo rc and the expectation to rc=0(?![0-9]). On the replacement proof's recorded output, independent regex controls yield original=false, amended=true, nonzero=false, missing-rc=false. Explicit five-ID proof-of-spec-check returns VALID with five acceptance rows and zero violations; both portal artifact paths resolve at 9d3d9ea8 in the nested repository. This is source and recorded-output verification, not a fresh generator or whole-suite execution by CVO. The original refusal stays a valid historical finding. The row's surfaced_at claims 21:40Z, later than this 11:46Z read; its committed pin, not that clock, anchors this disposition.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@e40eb6938d6eeabadf82440f70c023494bdb82e9#IRPT_FNTEND-W31-S1",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-81.fixture-generator-repair-survives-regeneration.md@843b8851eb223b7ddf6cd2d72b235c86b43e6407",
        "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~31/IRPT_FNTEND.TO-FE-s-81.fixture-generator-repair-survives-regeneration.proof_of_spec.json@708487538cc8765812c5638dcb850f62aea9fb99",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-corpus.ts@9d3d9ea85b5b76e104b2122446cb3a8404ecafc8",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260922_CVOF_CANONICAL_DRIVE_IRPT_FNTEND.md (co-committed; controls and limits)"
      ]
    },
    "adjudicates": [
      "IRPT_FNTEND-W31-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Corrected in-round by the named issuer at 843b8851eb, with replacement proof 708487538c independently checked. No remaining acceptance-mismatch remedy is owed. This closes W31-S1 only; it does not close the broader generator hazard W25-S1 or grade other round-13 criteria."
  },
  {
    "id": "IRPT_FNTEND-C-S168",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "W33-S1: the issuer corrected all three unexecutable or vacuous invocations.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F83-AC2 measures navy, AC3 exercises hover, AC4 is a genuine absent-selector control; the worker may not self-amend.",
    "world_is": "Amendment 6d3b2e4d92 changes AC2/AC4 to the real Investor Reporting route with/without Holdings, and AC3 to the hover driver. Current proof validates six rows with five invocation matches. The absent-control expectation remains UNMEASURABLE; it did not become a focus-ring criterion. Own browser exercise additionally confirms visible navy hover and keyboard underline and the white-gap/indigo ring.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "IRPT_FNTEND-W33-S1"
    ],
    "dismissal_reason": "The original refusal was correct. The issuer repaired targeting and mechanism; final amended output meets those local expectations. No remaining W33-S1 remedy; common five-part cut defects are separately C-S176."
  },
  {
    "id": "IRPT_FNTEND-C-S169",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "W32-S1: the issuer repaired breadcrumb depth and selector discrimination.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F82-AC2 must distinguish current=700 from an ancestor link !=700 on the same view.",
    "world_is": "Amendment 6e3d50ab44 adds a Models drill and tag-qualified selectors. Own browser at portal pin measures current Models 700 and ancestor A-0001 400, both navy on a white Holdings container. Six-row proof validates.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "IRPT_FNTEND-W32-S1"
    ],
    "dismissal_reason": "The unsatisfiable one-node comparison is corrected by the issuer. The original worker refusal remains historical evidence; no residual order mismatch."
  },
  {
    "id": "IRPT_FNTEND-C-S170",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "W32-S2: the disclosed React harness exercises the actual DrillTree conditional branch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The no-DOM cell requires actual DrillTree logic and its own refusal output, rather than constructing PanelError directly.",
    "world_is": "Read the test body and independently ran it: stale onRowClick yields two harness passes and the refusal/error content; fresh sibling yields two passes and navigation without refusal; baseline one pass has no refusal. It directly calls the real component function inside a server-rendered harness, so hooks belong to the harness fiber. This is bounded handler/conditional integration evidence, not a browser click, independent DrillTree fiber, effect lifecycle or DOM-event test.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "IRPT_FNTEND-W32-S2"
    ],
    "dismissal_reason": "The nonstandard mechanism is fully disclosed and meets the explicitly no-DOM branch-coverage objective. No invented wire field and no browser-reachability claim. Close the component-test gap only."
  },
  {
    "id": "IRPT_FNTEND-C-S171",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "W34-S1: the issuer corrected the nonexistent qualified-state fixture path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "F84-AC5 requires the actual qualified state and a non-amber-50 background; the literal fixture must exist.",
    "world_is": "Amendment 6e3d50ab44 names the committed reporting-qualified.json fixture. Seven-row proof validates with six invocation matches. Own qualified browser probe serves 3/3 fixtures and measures white background, navy ink and warning border rgb(211,124,23). The static fixture changes the producer state to PARTIAL; the local acceptance bar is preserved.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "IRPT_FNTEND-W34-S1"
    ],
    "dismissal_reason": "The path defect was repaired by the issuer and the qualified state is now actually exercised. Remaining typography is C-S175/C-S150, not this fixture-path defect."
  },
  {
    "id": "IRPT_FNTEND-C-S172",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "Round 13 has four judgment criteria: three bounded PASS and one FAIL.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CVO grades the exact committed criteria, never a summary that invents a fifth judgment on FE-s-81.",
    "world_is": "Five proofs carry 30 criteria: 26 mechanical and four judgment. FE-s-81 has five mechanical criteria and no judgment. The four grades below are independent and bounded. F78-AC7 remains historically NOT_EVALUATED at its old vintage; F84-AC7 supplies the new exercised-scroll evidence.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This is the grade carrier, not a new remediation clock. Failures and residuals are carried under their named mechanisms.",
    "grades": [
      {
        "criterion": "F80-AC6",
        "verdict": "FAIL",
        "reason": "Static-only suffix control remains invalid, but the actual production classifier accepts holdings/A-0001/not-a-declared-operation as valid 1/1 although consumed.ts declares only holdings/{accountSetId}. Prefix matching does not validate the complete template. Colour discrimination and reusable actual scrolling are supported; the classifier-correctness conjunction fails. Existing C-S147 remains OPEN.",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~30/IRPT_FNTEND.TO-FE-s-80.instrument-round-13-classifier-colour-scroll.proof_of_spec.json@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      },
      {
        "criterion": "F82-AC6",
        "verdict": "PASS",
        "reason": "Own live measurement is current=700, link=400. Independent test execution exercises the real DrillTree handler and conditional with stale/fresh/baseline arms. Scope is no-DOM component-body integration, not browser event or separate component-fiber coverage.",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~32/IRPT_FNTEND.TO-FE-s-82.breadcrumb-weight-700-and-mounted-revision-guard-test.proof_of_spec.json@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      },
      {
        "criterion": "F83-AC6",
        "verdict": "PASS",
        "reason": "Own browser shows navy rgb(22,51,114), none->underline->none across rest/hover/release and keyboard focus/blur, effective opacity 1 when focused, actual tile :focus-visible=true, white 2px gap and indigo 4px focus ring. This supplies the focus exercise missing from the worker hover-only driver.",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~33/IRPT_FNTEND.TO-FE-s-83.view-breakdown-link-navy-hover-focus-underline.proof_of_spec.json@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      },
      {
        "criterion": "F84-AC7",
        "verdict": "PASS",
        "reason": "Read committed 390px before/after pair: newly revealed chart dates July/August/September accompany the recorded actual 0->638 scroll and shared selector-parameterised driver. Named surface/navy/hairline/warning roles are used and unavailable values remain unavailable. Bounded requested colour/scroll grade; it does not certify all report typography, every intermediate scroll position, or FWD-12.",
        "instance": "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~34/IRPT_FNTEND.TO-FE-s-84.report-scroll-reevaluation-and-styling-residuals.proof_of_spec.json@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      }
    ]
  },
  {
    "id": "IRPT_FNTEND-C-S173",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "The FE-s-81 generator source landed, but two regenerated outputs did not.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "F81-AC3 requires 12/12, 9/9 and 2/2 entries after regeneration; the committed artifact must preserve the delivered repair.",
    "world_is": "At producer 9d3d9ea85b5b76e104b2122446cb3a8404ecafc8, drain 86ae054b, and portal HEAD 467354c9, git show counts 12/12, 0/9 and 0/2. Producer commit contains only generator and test changes. Own focused test run gives 18 pass/2 fail; whole suite gives 648 pass/27 skip/2 fail, exactly the two sibling fixtures. No generator was run by CVO to hide the committed-state defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "disarm_owner": "2.0.0_SA_COO~F",
    "dismissal_reason": "Supplemental evidence on existing W25-S1; keep its remediation OPEN rather than minting a duplicate clock. Source repair alone is insufficient."
  },
  {
    "id": "IRPT_FNTEND-C-S174",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "The classifier now falsely validates an undeclared trailing path.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "F80-AC6 requires correct parameterised-template widening; C-S147 asks for key validity against consumed routes.",
    "world_is": "Own probe evaluates the shipped functions, reading the real consumed.ts. holdings/A-0001 is valid 1/1; holdings/A-0001/not-a-declared-operation also returns valid 1/1, although no consumed route matches it. The real status/extra-junk is valid because status/{jobId} exists; a separate static-only synthetic control rejects it. The flaw is unbounded parameter-prefix matching, not static-route widening.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "disarm_owner": "2.0.0_SA_COO~F",
    "dismissal_reason": "Keep existing C-S147 OPEN with a complete-template remedy and explicit admitted-prefix semantics; no duplicate remediation clock."
  },
  {
    "id": "IRPT_FNTEND-C-S175",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "AnswerStatus still requests forbidden 600/500 typography.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "DESIGN.md C1 permits only Lato weights 400/700; bounded colour fixes do not waive it.",
    "world_is": "At the portal pin AnswerStatus keeps font-semibold on answer-state and font-medium on answer-qualifier. Own computed-style probe reads Ready=600, Partial=600, qualified-label=500; screenshots show both real states. The surrounding colours now use admitted roles. Three measured labels, two states, two noncanonical requested weights.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "disarm_owner": "2.0.0_SA_COO~F",
    "dismissal_reason": "Keep the existing report-conformity remediation C-S150 OPEN; this precise remaining C1 mechanism is not a separate duplicate clock."
  },
  {
    "id": "IRPT_FNTEND-C-S176",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "The mandatory five-part visual criterion contract is silently waived in the results.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "spec_asserts": "Each of the five round-13 orders declares wire fulfilment N/N, named-content assertions, wrong-state content control, actual-container ground plus wrong-ground control, and absent-selector control binding on every visual criterion.",
    "world_is": "FE-s-80 result explicitly calls ground control N/A because it measures foreground text; FE-s-84 does the same for AC4/AC5. That exemption is absent from the issued common rule. Recorded F80-AC3 fulfils 3/12 and F83 Holdings 3/9, although declared key validity is a different denominator. Formal checker validity therefore does not establish the five-part acceptance conjunction. The six narrow issuer amendments repair their named local bars but do not reconcile this broader contract.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~F"
  },
  {
    "id": "IRPT_FNTEND-C-S177",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~F",
    "surfaced_at": "2026-09-22T13:41:31Z",
    "one_line": "L8 packet wording is corrected against committed artifacts and delivery receipts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Compilation carries exact task-order criteria, row counts, amendment identity and observed delivery, rather than inferred equivalents.",
    "world_is": "Message 99484 calls F83-AC4 a focus-ring expectation and implies FE-s-81 has a judgment; neither is in the task files. Six faulty criterion cuts map to four defect investigations W31-S1/W33-S1/W32-S1/W34-S1; W32-S2 is a separate method disclosure. Message 99496 says the driver report was not sent, but canonical send delivered 20260922T120143Z_3.0.0_SA_CVO_F_ACK_99451_99454__drive_registration_succ.md to CTO. The L8 file remained unread on disk while this review ran and was archived after substantial action, explaining the queued observation without implying inactivity.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md (co-committed; independent measurements and limitations)",
        "portal@467354c947c1afebc77eb6839724c7243547f46f",
        "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@da9ac0dae9b8d426a4357e6d0921656d87a73125"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Corrected by this review and the L10 carrier; no additional remediation clock. The driver remains stopped under the separately reported runtime scope defect."
  }
]
```
