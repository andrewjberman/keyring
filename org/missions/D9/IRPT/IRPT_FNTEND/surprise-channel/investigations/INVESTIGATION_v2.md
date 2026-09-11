# IRPT_FNTEND -- surprise channel, INVESTIGATION v2 (round 2, laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "IRPT_FNTEND-W1-S15",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-11T09:12:00Z",
    "one_line": "TO-FE-s-12's <proof_of_spec> block specifies `phase BUILD`, but org/standards/PROOF_OF_SPEC.schema.json's `phase` enum carries no `BUILD` member -- proof-of-spec-check.py refuses the ordered value outright, so no instance written exactly as this order specifies it can ever validate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.md @d45d2760f2, <proof_of_spec> block: \"(phase `BUILD`, firm `FABRIC`, spec_ref.group `OTHER`)\" -- the same three-value parenthetical is repeated verbatim in this worker's WORKER FACE.",
        "org/standards/PROOF_OF_SPEC.schema.json @d45d2760f2, properties.phase.enum, read directly: ['P1-SCRIPTS', 'P2-TIMING', 'P3-REPOINTS', 'P4-PUBLISHERS', 'P5-DECOMMISSION', 'BUILD-GENERAL', 'INVESTIGATION', 'NON-BUILD-OTHER'] -- 8 members, denominator printed, and `BUILD` is not one of them.",
        "MEASURED, not inferred from the enum: the instance was authored with the ORDERED value and run through the gate first -- `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-12.dev-green-typecheck.proof_of_spec.json F12-AC1,F12-AC2,F12-AC3,F12-AC4,F12-AC5` returned `VIOLATION: schema: phase: 'BUILD' is not one of ['P1-SCRIPTS', 'P2-TIMING', 'P3-REPOINTS', 'P4-PUBLISHERS', 'P5-DECOMMISSION', 'BUILD-GENERAL', 'INVESTIGATION', 'NON-BUILD-OTHER']` and INVALID (rc=1). checker-vintage 709b9556a3 2026-09-10T14:37:30Z.",
        "The other two round-1 sibling instances in this deliverables folder that were written against the same schema (IRPT_FNTEND.TO-FE-s-11 and TO-FE-s-9 .proof_of_spec.json) both carry phase `INVESTIGATION`, a declared enum member -- so this is the first instance in this project ordered to a value the schema does not hold, not a long-standing tolerated deviation.",
        "Scope of the claim, stated: this row asserts ONLY that the literal token `BUILD` is refused by the phase enum. It does NOT assert that `BUILD-GENERAL` is the phase the issuer INTENDED -- that is the issuer's call; `BUILD-GENERAL` was chosen here as the nearest and only build-flavoured member, and the substitution is disclosed in the instance's own `surprises` array so a grader sees it without reading this row."
      ]
    },
    "spec_asserts": "This order's <proof_of_spec> block: the instance is to be written with `phase BUILD` and validated with `python .tools/proof-of-spec-check.py <instance> F12-AC1,..,F12-AC5` BEFORE the `complete` flip, and the flip happens only when the checker passes.",
    "world_is": "Those two instructions cannot both be satisfied as written: `phase: \"BUILD\"` is a hard schema violation and the checker returns INVALID (rc=1) on it, so the instance was carried as `BUILD-GENERAL` -- the nearest enum member -- and the deviation from the ordered literal is disclosed both here and in the instance's `surprises` array. hazard_standing INERT: the substitution is a metadata-field value on a proof instance, it moves no criterion, no artifact and no graded outcome (all five criteria are a typecheck, two bun test runs and two git diffs, each PASS by its own output either way), and the gate itself is the thing that catches the ordered value, so the failure mode is a loud refusal rather than a silent wrong record. No disarm_owner: nothing is armed. The standing question for the issuer -- whether future IRPT task orders should specify `BUILD-GENERAL`, or whether `BUILD` should be added to the ratified enum -- is a schema/issuance decision above this worker's lane and is left open, not decided here.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-S18",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~F",
    "surfaced_at": "2026-09-11T12:35:00Z",
    "one_line": "Round 2 opened: decomposition v0.2 @430c5fcb4a (seven additive cells on the CTO's seven rulings), ONE issuance @75d2e353a8, COMPLETION_REPORT.round1.json (8 of 8 COVERED). FE-s-12 (the typecheck repair) is terminal and drained in both repos: portal DEV 32a744dc reads `bun run typecheck` rc=0 by the issuer's own run and 322 pass, 1 skip, 0 fail; four lines changed in the two fe-s-11 test files, shims and tsconfig untouched (OUTSIDE-GRANT: 0, SHIMS-EDITED: 0). DEV is green under tsc: the analysis's ruling 1 precondition for a DEV push is met at 32a744dc. One issuer face defect carried by the worker (W1-S15): every round-2 BUILD order named proof phase `BUILD`, a value the PROOF_OF_SPEC schema's phase enum does not hold (P1..P5, BUILD-GENERAL, INVESTIGATION, NON-BUILD-OTHER); the five non-terminal orders FE-s-13..17 are amended to BUILD-GENERAL in one commit; FE-s-18 is INVESTIGATION. The worker also recorded, ungraded: colour-law.test.ts's positive control asserts only scannedFiles > 0, so a scan that collapses to one file still passes -- carried to FE-s-18's face reading as a control to tighten.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal DEV @32a744dc, issuer's run: `bun run typecheck` rc=0; `bun test src/pages/InvestorReporting` 322 pass, 1 skip, 0 fail, 48 files",
        "workspace @69aa29687c -- proof-of-spec-check on the FE-s-12 instance: VALID rc=0, 5 acceptance rows; git show --format= --name-only on each of the 3 worker commits -- portal: 0 lines (no gitlink)",
        "org/standards/PROOF_OF_SPEC.schema.json @HEAD -- phase enum: P1-SCRIPTS, P2-TIMING, P3-REPOINTS, P4-PUBLISHERS, P5-DECOMMISSION, BUILD-GENERAL, INVESTIGATION, NON-BUILD-OTHER (read by the issuer after row W1-S15)",
        "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-1[3-7].*.md -- 5 of 5 carried `phase BUILD` at 75d2e353a8; amended this turn"
      ]
    },
    "spec_asserts": "Issuer faces FE-s-12..17: proof instance phase `BUILD`. Analysis ruling 1: no DEV push before the typecheck repair lands.",
    "world_is": "The enum has no BUILD; the checker refuses the instance and the worker substituted the nearest member and rowed it. The repair landed; DEV is green; the push precondition is met and the push itself is 0.0.0_AB_MSTR's on Andrew's word, with this lane's gitlink bump after it.",
    "disposition": "UNDER_INVESTIGATION"
  }
]
```
