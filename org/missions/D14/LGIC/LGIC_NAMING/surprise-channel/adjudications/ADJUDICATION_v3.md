# LGIC_NAMING round 2: CVO adjudication (L8 compile + L9)

Round 2 of `LGIC_NAMING`, compiled and adjudicated by `3.0.0_SA_CVO` on 2.0.0_SA_COO~G's drain-end read (96792). The issuance is @b9ea6f3686 (8 orders, decomposition v4 @32795c348c s.0c). This document carries the 7 rows that were carrier-less at L8 (S16, W1-S6, W2-S5, W3-S4, W4-S1, W4-S2, W6-S4), this seat's FWD-1 observation, and the one judgment grade. S14 and S15 were carried at round 1 by C-S11 and C-S12 (ADJUDICATION_v2.md). Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND2_L8_L9_20260915.md`.

```json
[
 {
  "id": "LGIC_NAMING-C-S13",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T01:07:23Z",
  "one_line": "ROUND-2 L9 GRADE RECORD: the one JUDGMENT criterion, F1R-J1, is PASS with a named qualification. Outcomes: FWD-1 NOT REALIZED (14 of 17 independent items identical, i15 identical under disclosure), FWD-2 NOT REALIZED on its reading limb (16 of 18) and REALIZED on its one-referent limb, FWD-3 REALIZED on canonical forms, and FWD-4 REALIZED on its reading limb (6 of 6).",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: a JUDGMENT criterion is graded by the CVO against the specification that issued it, never self-graded; its verdict lives in `grades`. Outcomes are graded against the PRD's DONE WHEN / ACCEPT text (LGIC_NAMING_PRD.md v1.6 :34-76).",
  "world_is": "Census: 8 orders, 26 criteria, 1 judgment (F1R-J1). this seat re-ran all 25 machine criteria of the 8 round-2 orders with check_ln_r2.py on the SHARED tree (cwd = workspace root, HEAD 4fdc86a76c, core.autocrlf=true), a different checkout from every writing worktree: 23 printed their expected VERDICT, and 2 did not -- E3R-AC1 'VERDICT: FAIL-DIFFERENT' and E5R-AC1 'VERDICT: FAIL-MISREAD', each equal to its instance's status. proof-of-spec-check.py read VALID (rc=0) on 8 of 8 instances, each run BOUND with --governing-order to its own order. FWD-1: namer A wrote the ruled name on 18 of 18 and namer B on 15 of 18. On the basis C-S12 committed, the 17 items other than i15 agree on 14. i15 agrees too, but its answer is spelled in the briefing, and i05 counts as the output of the bucket rule (C-S14). FWD-2: 16 of 18 marks correct, 0 clashes across 18 names, and the canary read blind (C-S15). FWD-3: F1R-AC1..AC5 PASS on the re-run; 68 attributed, 0 excluded, 1 raise (68 + 0 + 1 = 69). The four patterns catch 68 of 68 canonical forms, and 12 of 68 live names today, because the renames are LGIC_ENFORCE's. FWD-4: L3R-AC1 6 of 6 conforming addresses read right, including a3 (the code tier, round 1's miss), and L3R-AC2 flags the control. Its 'older descriptions say they are replaced' limb was served by round 1's LN-l-1 and is not re-graded here.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~4/LGIC_NAMING.TO-LN-f-1-r2.firm-patterns.proof_of_spec.json@a4480344e3",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md@a4480344e3",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n4-firm-patterns.md@d9ccd9babd",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@51b0952d71 :148-150 (R1.e-f)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-compare.md@ba8250b32a",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-reader-score.md@4c0866f468",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n5-reader-score.md@b9834f3b37",
    "org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@2706014705 :34-76",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND2_L8_L9_20260915.md (same commit series)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade record: it adjudicates no item and opens nothing. Each qualification is carried by the graduated row it names (C-S14, W6-S4 via C-S15, W4-S1 and W4-S2 via C-S17) and reaches 1.0.0_SA_CTO in the round-2 slug.",
  "hazard_standing": "INERT",
  "grades": [
   {
    "criterion": "F1R-J1",
    "instance": "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~4/LGIC_NAMING.TO-LN-f-1-r2.firm-patterns.proof_of_spec.json@a4480344e3",
    "verdict": "PASS",
    "reason": "MET WITH A NAMED QUALIFICATION. This seat compared the round-2 record's JSON with round 1's by its own script: 68 of 68 attributions are identical in firm and canonical form. Round 1's were graded F1-J1 PASS after this seat re-derived 12 of 69 by hand (C-S3). Six of those twelve were re-read in round 2's JSON and carry the same values, for example bd-allocation-checker-lambda-role -> {system}-49f-allocation-checker-lambda-role, opal-assets-mirror-cot-scheduler-role -> opal-cot-assets-mirror-scheduler-role and inf-api-eclipse-role -> eclipse-inf-api-role. The one change is the third disposition. wp5-49f-feeder-scheduler-role sits under raise with step R1.f, which GRADING_RULE.md :150 states: 'Any other t1 is in no vocabulary. RAISE: a token no registry row resolves.' The raise names its step, and excluded is empty, so no exclusion reason is owed. QUALIFICATIONS: (1) the forms follow GRADING_RULE.md, which the criterion names, and 31 of 68 carry a kind word inside the name that NAMING_SCHEMA v1.6's FN1 forbids (row W4-S2, recounted by this seat); (2) the face's bd paraphrase reads differently from R3, and the record follows R3 (row W4-S1; 12 of 20 bd roles recounted); (3) 48 of 68 forms carry {system} (PH1, LGIC_ENFORCE's registry)."
   }
  ]
 },
 {
  "id": "LGIC_NAMING-C-S14",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T01:07:23Z",
  "one_line": "ROUND-2 L9, FWD-1, GRADUATED -- CVO OBSERVATION: all three namer differences (i03, i10, i11) are one reading of FN1's noun-phrase clause. Namer B wrote the phrase as named, vendor token included, although that token already sits in the system slot. The clause's text admits it, and its own example 'the Orion ingest' is item i03. So the split is the schema's.",
  "class": "BLOCKING",
  "spec_asserts": "PRD FWD-1 ACCEPT: two people 'each writes down the identical name'. NAMING_SCHEMA.json:59 (FN1, v1.5): 'Where the item NAMES the process or subject as a noun phrase (the SmartX platform export, the Orion ingest, ...), the function is that phrase as named, kebab-case, ONE token'.",
  "world_is": "E3R-AC1 prints 'VERDICT: FAIL-DIFFERENT' (this seat's re-run on the shared tree) with 15 of 18 identical, and 14 of the 17 independent items. The three differing strings, read by this seat from the answer files: i03 A=orion-inf-ingest-daily B=orion-inf-orion-ingest-daily; i10 A=smartx-49f-platform-export-weekly B=smartx-49f-smartx-platform-export-weekly; i11 A=pathfinder-etfs-ingest-task B=pathfinder-etfs-pathfinder-ingest-task. Namer A matches the ruled table on 18 of 18; the table applies an unwritten subtraction (analysis s.2 rows i03, i10 and i11, 'FN1 (noun: the Orion ingest)'). FN1 has no clause that drops a phrase token already written in the system slot, so namer B's reading is the clause taken literally. Each of the three is a vendor-as-system item whose noun phrase begins with that vendor. E3R-AC2 prints 'VERDICT: PASS-NAMERS-UNCONFERRED' (one prompt, two sessions, two folders), so the three differences are the schema's, not collusion. No worker row carries this FAIL, so this row does.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-namer-a.tsv@eaafb46486",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-namer-b.tsv@59f68115a4",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-compare.md@ba8250b32a",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~6/LGIC_NAMING.TO-LN-e-3-r2.namer-comparison.proof_of_spec.json@ba8250b32a",
    "org/standards/NAMING_SCHEMA.json@2706014705 :59 resource.function (FN1)",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md@2706014705 s.2 table rows i03, i10, i11"
   ]
  },
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S15",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T01:07:23Z",
  "one_line": "ROUND-2 L9, FWD-2, GRADUATED: the blind reader (canary proved blind) marked the firm or none right on 16 of 18 names. Both misses fall on a token whose class a newcomer cannot see: 'demo', a tenant class the doctrine does not define, read as no firm; and the vendor 'pathfinder' in the system slot, read as the firm. The one-referent limb is REALIZED: 0 clashes.",
  "class": "BLOCKING",
  "spec_asserts": "PRD FWD-2 DONE WHEN: 'someone new to the estate has read names and pointed at the firm in each, unaided'; ACCEPT: '... and the same letters never mean two different things'.",
  "world_is": "E4R-AC1..AC3 PASS on the re-run, so the seat was clean, the canary read blind and every name was marked, and FWD-2 is measurable in this fabric (the round-1 C-S6 question, answered). E5R-AC1 prints 'VERDICT: FAIL-MISREAD' on the re-run: i09 marked none where N3_KEY_R2 reads demo, and i11 marked pathfinder where the key reads none (RULING Q changed i11 from etfs to none). E5R-AC2 prints 'VERDICT: PASS-ONE-REFERENT-EACH'. The spine lists demo as 'a tenant class the doctrine does not define' (infra/logic/05_IDENTITY_SPINE.md@a4cc0cb681 :69). A vendor in the system slot has the same shape as a firm to a reader who is told nothing about position, and FWD-2's own header says 'from position alone'.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W6-S4",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~6/LGIC_NAMING.TO-LN-e-5-r2.reader-scoring.proof_of_spec.json@4c0866f468",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-reader.tsv@9096ea3c49",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-reader-score.md@4c0866f468",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~5/LGIC_NAMING.TO-LN-e-4-r2.reader.proof_of_spec.json@9096ea3c49"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W6-S4"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S16",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T01:07:23Z",
  "one_line": "ROUND-2 L9: the three line-ending rows (W1-S6, W2-S5, W3-S4) and their disarm S16 are DISMISSED_WITH_REASON. The fix @ca44748a44 pins the seat records byte-exact, and this seat's re-run on the shared tree proves it.",
  "class": "OBSERVATION",
  "spec_asserts": "Decomposition v4 s.0c: the checker 're-derives the prompt with the same builder and re-parses the verbatim reply, which the seat record hashes'. A clean seat grades PASS wherever the checker runs.",
  "world_is": "The root .gitattributes at HEAD carries 'org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/seats/** binary' (S16's fix). This seat re-ran all 8 seat criteria, E1R-AC1/AC2, E2R-AC1/AC2, E4R-AC1/AC2 and L2R-AC1/AC2, on the shared tree, where core.autocrlf=true and no seat file was written. Each printed its expected PASS-CLEAN-SEAT or PASS-CANARY-BLIND, 8 of 8. The exposure the three rows named would have printed FAIL-SEAT-NOT-PROVED / FAIL-NO-CANARY there.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W1-S6",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W2-S5",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W3-S4",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-S16",
    ".gitattributes@ca44748a44"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W1-S6",
   "LGIC_NAMING-W2-S5",
   "LGIC_NAMING-W3-S4",
   "LGIC_NAMING-S16"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Closed in the artifact named. The three ARMED rows were disarmed by their disarm owner's fix, recorded as S16, and the disarm is EXERCISED here, not taken on the row's word. S16 is the disarm record itself. No remediation is owed.",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S17",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T01:07:23Z",
  "one_line": "ROUND-2 L9, FWD-3, GRADUATED: LN-f-1-r2 names two authorities that part in two places. Its face paraphrases GRADING_RULE R3's bd step as position where the rule tests adjacency (W4-S1). And GRADING_RULE.md, a v1.4-vintage rule, keeps a kind word in the function slot that NAMING_SCHEMA v1.6's FN1 forbids, in 31 of 68 canonical forms (W4-S2). Neither moves an attribution or a pattern catch.",
  "class": "OBSERVATION",
  "spec_asserts": "TO-LN-f-1-r2 face: 'Grade each by ... GRADING_RULE.md' and 're-grade under NAMING_SCHEMA.json v1.6'; F1R-J1: 'each attribution and canonical form follows GRADING_RULE.md'.",
  "world_is": "Recounted by this seat. W4-S1: over LIVE_NAMES.json IAM_ROLE (240 roles), 20 carry bd, and 12 of them have no adjacent firm token, all 12 with bd first. R3 reads those 12 as the FIRM, and the face's position paraphrase would not. W4-S2: with the 20 kind words of NAMING_SCHEMA kind.by_type, 31 of 68 canonical forms carry a kind word inside the name. Firm, scope, attribution and pattern catch are the same under both readings, because each pattern reads only the firm token.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W4-S1",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W4-S2",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@51b0952d71 :160-163 (R3), :173-181 (R5, R6)",
    "org/standards/NAMING_SCHEMA.json@2706014705 :59 (FN1)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md@a4480344e3"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W4-S1",
   "LGIC_NAMING-W4-S2"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 }
]
```
