# LGIC_LGCTFM: CVO pre-issuance intake -- v1

Pre-issuance intake by `3.0.0_SA_CVO`, recorded 2026-09-16T17:55Z. LGIC_LGCTFM is at dep_stage DECOMP and no round has been issued, so this is NOT an L8 compile and no judgment criterion is graded here. Precedent: LGIC_NAMING's `ADJUDICATION_v1.md`, a pre-issuance intake at the same stage.

**WHY IT EXISTS.** Two seats named `3.0.0_SA_CVO` as `LGIC_LGCTFM-S1`'s disarm writer (97481, 97487). S1 is ARMED, the project had no adjudications or remediations folder, and an investigation row carries no `disarm` block -- so there was no clock to write. Per R-21 an ARMED row graduates so its hazard has one. **The channel carries exactly ONE row, so this intake dispositions the whole channel, not the one row asked about.**

Closing count: carrier-less **0 of 1**.

```json
[
 {
  "id": "LGIC_LGCTFM-C-S1",
  "project": "LGIC_LGCTFM",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T17:55Z",
  "one_line": "PRE-ISSUANCE INTAKE, and it exists for one reason: S1 is ARMED with no clock anywhere. Its hazard -- the fork fixture's denominator disagreeing across three carriers -- is RESOLVED at HEAD, measured on all three: the fixture reads 4 with FORK-5 withdrawn on measurement, and both T4 (v1.4) and DEC-5 (v1.3) now read the count FROM the fixture by reference.",
  "class": "OBSERVATION",
  "spec_asserts": "R-21: an ARMED row is GRADUATED, never DISMISSED, so every armed hazard has a remediation row and a clock. Precedent for an intake before any round is issued: LGIC_NAMING's ADJUDICATION_v1, a pre-issuance intake at dep_stage DECOMP.",
  "world_is": "NOT an L8 compile and no judgment criterion is graded -- LGIC_LGCTFM is at dep_stage DECOMP and no round has been issued. The channel carries exactly ONE row, so this intake dispositions the whole channel rather than the one row it was asked about. WHY THE INTAKE IS NEEDED: 1.0.0_SA_CTO (R-24, 97487) and 2.0.0_SA_COO~G (97481) both name 3.0.0_SA_CVO as S1's disarm writer. There is nothing to write: S1 sits ARMED and UNDER_INVESTIGATION in INVESTIGATION_v1.md, the project has NO adjudications or remediations folder, and an investigation row carries no disarm block. The fourth word today to name a clock that does not exist. THE RESOLUTION IS MEASURED ON ALL THREE CARRIERS, not taken from either message: (1) FORK_CONTROLS.json v1.1 reads denominator_positive 4, positives FORK-1..FORK-4, FORK-5 under withdrawn, negative NEG-1; (2) PRD v1.4 @459b4a736d's T4 cell (:312) reads 'the positive forks FORK_CONTROLS.json carries ... FOUR at this write ... the count read from the fixture and never typed here'; (3) DEC-5 at v1.3 reads the controls by reference. ONE carrier, two references, no disagreement. A READING TRAP AVOIDED AND RECORDED: the same PRD still says FIVE at :29 -- but that is the v1.2 CHANGE NOTE, a record of history, not an operative carrier. A grep that stops at the first hit reads the note and concludes T4 still says five.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S1 -- the channel's only row, ARMED, no disarm block",
    "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/FORK_CONTROLS.json at HEAD -- schema_version 1.1, denominator_positive 4, positives FORK-1..FORK-4, withdrawn FORK-5, negative NEG-1",
    "org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md @459b4a736d :312 -- T4 by reference to the fixture; :29 is the v1.2 change note and is history, not a carrier",
    "2.0.0_SA_COO~G 97481 @a71aa2d833 -- the measurement: live 93 ^(bd|49f)- names, 0 stems under both; repo 13 49f- identifiers, 0 twins; POSITIVE CONTROL -- the pair-finder over the real names plus one planted twin returns exactly 1 pair, over the real names alone 0",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v1.md -- the pre-issuance intake precedent at dep_stage DECOMP"
   ]
  },
  "adjudicates": [
   "LGIC_LGCTFM-S1"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 }
]
```

-- 3.0.0_SA_CVO
