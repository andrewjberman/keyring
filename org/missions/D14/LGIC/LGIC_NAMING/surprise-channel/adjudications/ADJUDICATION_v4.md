# LGIC_NAMING round 3: CVO adjudication (L8 compile + L9)

Round 3 of `LGIC_NAMING`, compiled and adjudicated by `3.0.0_SA_CVO`. The L8 input is 2.0.0_SA_COO~G's LATE hand-off, msg 97122 (14:54:19Z). The drain-end read it repeats, msg 97005 (09:11Z), was addressed to 1.0.0_SA_CTO only, so this seat's L8 began about 5 h 45 min after the drain. The issuance is @60350c4a04 (6 orders, decomposition v5 @2f8cc63b8e s.0d, PRD v1.7). This document carries the 6 rows that were carrier-less at L8 (S17, W1-S7, W2-S6, W3-S5, W3-S6, S18), the one judgment grade, and this seat's read of the prior rounds' OPEN remediation rows. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND3_L8_L9_20260915.md`.

```json
[
 {
  "id": "LGIC_NAMING-C-S18",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T15:10:15Z",
  "one_line": "ROUND-3 L9 GRADE RECORD: the one JUDGMENT criterion, G1T-J1, is PASS with two named qualifications (W3-S5, W3-S6). Outcomes: FWD-1 REALIZED (18 of 18 identical, every name the ruled name; i05 disclosed), FWD-2 REALIZED (18 of 18 correct, 0 clashes, seat clean, canary blind), FWD-3 REALIZED on canonical forms, with the rule at v1.7 for R5 only (0 of 68 forms change).",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: a JUDGMENT criterion is graded by the CVO against the specification that issued it, never self-graded. Outcomes are graded against LGIC_NAMING_PRD.md v1.7 FWD-1..FWD-3 DONE WHEN / ACCEPT (:34-60 @02f08322af).",
  "world_is": "Census: 6 orders, 17 machine criteria and 1 judgment (G1T-J1). This seat re-ran all 17 machine criteria with check_ln_r3.py on the SHARED tree (cwd = workspace root, core.autocrlf=true), a different checkout from every writing worktree: 17 of 17 printed their expected VERDICT. proof-of-spec-check.py read VALID (rc=0) on 6 of 6 round-3 instances, each BOUND with --governing-order to its own order. FWD-1, by this seat's own read of r3/n3-namer-a.tsv and r3/n3-namer-b.tsv: 18 of 18 identical, and each of the 18 equals the first cell of its row in the round-1 analysis s.2 ruled table, the grade the LN-e-3 worker left for L9. E3T-AC2 prints PASS-NAMERS-UNCONFERRED (one prompt sha 5dbd2548..., two sessions). i05's bucket still appears in the registry seed (row S15), so the independent count is 17 of 17. i15's worked example is gone from NAMING_SCHEMA.json at HEAD (RULING EX1). FWD-2, by this seat's own read of r3/n3-reader.tsv against r2/N3_KEY_R2.json, by item id through the s.2 names: 18 of 18 marks equal the key. E5T-AC2 reads 0 tokens as two referents. Under RULINGS DM and POS the reader may be told what each position holds. FWD-3, by this seat's own recount of FN1b and FN1c over the 68 attributed canonical forms of r2/n4-firm-patterns.md @a4480344e3 (all IAM_ROLE, own kind role, firms 49financial, cottonwood, demo and inflection): 0 of 68 change, equal to the rule's printed line and the checker's recount. W6-S1 (disarmed by S12's disclosure): round 3's three blind seats (e1, e2, e4) print PASS-CLEAN-SEAT and PASS-CANARY-BLIND, 6 of 6, on this seat's re-run (SEAT CONDITIONS 10, HELD 10, each), so the un-blinded worker context W6-S1 measured is absent from round 3's blind cells.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py@60350c4a04 (17 sub-commands re-run on the shared tree)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/n3-namer-a.tsv and n3-namer-b.tsv at HEAD (merged @2386471252, @59f8e34905)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/n3-reader.tsv at HEAD (merged @d47aac6c8b)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/N3_KEY_R2.json (unchanged in round 3)",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md s.2 table rows i01..i18",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md@02f08322af s.2 (RULINGS FN1b, FN1c, DM, POS, EX1)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md@a4480344e3 (attributed, 68 forms)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@3cc090827f (diff against 6705066c68)",
    "org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md@02f08322af :34-60"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade record: it adjudicates no item and opens nothing. Each qualification is carried by the graduated row it names (W3-S5 by C-S21, W3-S6 by C-S22) and reaches 1.0.0_SA_CTO in the round-3 slug.",
  "hazard_standing": "INERT",
  "grades": [
   {
    "criterion": "G1T-J1",
    "instance": "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~3/LGIC_NAMING.TO-LN-g-1-r3.grading-rule.proof_of_spec.json@a945caca96",
    "verdict": "PASS",
    "reason": "MET WITH TWO NAMED QUALIFICATIONS. Read from git diff 6705066c68..HEAD of GRADING_RULE.md, a single commit @3cc090827f. R5 states FN1b's subtraction as R5.a, with the RAISE on an emptied function. It states the own-kind bar as R5.b. And it states why a function's words are kept: FN1's word-choice clauses bind the namer only, and a grade has no item description. R3 gains one sentence: the test is adjacency to a V4 firm token, never position. R3's readings are unchanged. The only other hunks are the header, the FORMS CHANGED line with its re-grade paragraph, and two gap entries naming W3-S5 and W3-S6. No other step's text moved. QUALIFICATIONS: (1) R5.b can empty a function, and v1.7 names no output then (W3-S5; 0 of 68 forms and 0 worked cases reach it). (2) The header names v1.7 for R5 only. G2 (GRADING_RULE.md:58-64) still RAISES names v1.7 aws_fixed excludes, and V-2 (:334) lists {tier} and {entity}, which v1.7 grade.placeholder does not allow (W3-S6)."
   }
  ]
 },
 {
  "id": "LGIC_NAMING-C-S19",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T15:10:15Z",
  "one_line": "ROUND-3 L9, GRADUATED and REMEDIATED IN THE ROUND: S17's LIMB 6 refusal in a linked worktree was the S14 reader following a commit hook's GIT_DIR. Its owner 1.0.0_SA_CTO fixed it @0801a7d48c during round 3. This seat EXERCISED the fix in a linked worktree under the hook's variables: the pre-fix reader returns no signoff, and the HEAD reader returns all three.",
  "class": "OBSERVATION",
  "spec_asserts": "1.0.0_SA_CTO's 96826: at an issuance commit the gate reads the signatures committed before it, never a file staged or left on disk (prd_signoff_lib.read_signoff_files, @3e8cf9e288).",
  "world_is": "Exercised by this seat with a different instrument from the author's self-test, which builds a temporary repository. The COO's retained linked worktree .worktrees/wk-lgic-naming-3-6 (HEAD cd86d91a55) has 3.0.0_SA_CVO.json, 4.0.0_SA_CRO.json and 4.0.0_SA_CRO~D.json committed in LGIC_NAMING's signoff dir. read_signoff_files was called on that dir with GIT_DIR and GIT_INDEX_FILE set to the worktree's own gitdir, as a commit hook sets them. The pre-fix lib (0801a7d48c^) returned [], which reproduces S17; the HEAD lib returned all 3 files. Without the hook variables, both returned all 3. On this seat's own fixture the HEAD lib admits a committed signoff file and ignores an uncommitted one beside it (S14's doctored pair). All four callers read through read_signoff_files at HEAD: prd-signoff.py:86, to-pipeline-gate.py:2204, prd-header-notify.py:131 and prd-stamp.py:339.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-S17",
    ".tools/prd_signoff_lib.py@0801a7d48c :286-345 (read_signoff_files; the git location variables removed for its reads)",
    ".tools/prd_signoff_lib.py@0801a7d48c^ (the pre-fix reader, the negative arm)",
    ".worktrees/wk-lgic-naming-3-6 at cd86d91a55: org/missions/D14/LGIC/LGIC_NAMING/prd/signoff/ (3 committed files)"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-S17"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT",
  "notes": "The same fix completes S14's remedy (HEAD read for all four callers, proved on a doctored pair). REMEDIATION_v2's S14 row therefore advances OPEN -> REMEDIATED in this round's slug (C-S23)."
 },
 {
  "id": "LGIC_NAMING-C-S20",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T15:10:15Z",
  "one_line": "ROUND-3 L9, GRADUATED to 2.0.0_SA_COO~G: 5 of 6 round-3 result files overwrite round 2's result for the same slot (S18; W1-S7 and W2-S6 are two of them). Nothing is lost: all 5 round-2 records resolve at their proofs' commits, and all 5 round-2 proofs re-run VALID. The cost is that a HEAD reader of a slot folder sees only the latest round.",
  "class": "OBSERVATION",
  "spec_asserts": "Each round-3 order's proof_of_spec: 'Result file `<stem>.result.md` beside it', in deliverables/<issued_to>/. The order says nothing about a file already at that path.",
  "world_is": "Checked with git objects, not only the checker's verdict. For each of the 5 overwritten paths, the HEAD blob's first line names round 3's order, and the blob at the round-2 instance's pin names round 2's. Two pins are explicit: namer-a @eaafb46486 and namer-b @59f68115a4. Three are PENDING-THIS-COMMIT, which the checker resolves to the instance's own commit: namer-comparison @ba8250b32a, reader @9096ea3c49 and reader-scoring @4c0866f468. Each of those carries round 2's text. proof-of-spec-check, bound to each order, reads VALID on all 5 round-2 instances (TO-LN-e-1-r2..TO-LN-e-5-r2). The three PENDING resolutions hold only while no later commit touches those instances. 2.0.0_SA_COO~G's LGIC_ENFORCE drain-end read (97047) names that one-shot class biting a later commit. LN-g-1 alone was free, because it ran in slot ~3 while round 1's ran in ~1.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-S18",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-W1-S7",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-W2-S6",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~6/LGIC_NAMING.TO-LN-e-3-r2.namer-comparison.proof_of_spec.json (PENDING co-committed @ba8250b32a)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~5/LGIC_NAMING.TO-LN-e-4-r2.reader.proof_of_spec.json (PENDING co-committed @9096ea3c49)",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~6/LGIC_NAMING.TO-LN-e-5-r2.reader-scoring.proof_of_spec.json (PENDING co-committed @4c0866f468)"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-S18",
   "LGIC_NAMING-W1-S7",
   "LGIC_NAMING-W2-S6"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S21",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T15:10:15Z",
  "one_line": "ROUND-3 L9, GRADUATED to 1.0.0_SA_CTO: the own-kind bar (FN1c, R5.b) can empty a function slot, as in mdpf-lambda-lambda, and v1.7 names a RAISE for FN1b's subtraction only. The grading rule says so rather than choosing. Because the result depends on step order, the ruling must name the order too.",
  "class": "OBSERVATION",
  "spec_asserts": "NAMING_SCHEMA.json v1.7 resource.function: 'a subtraction that leaves no function token RAISES (grade.unplaceable) (FN1b, v1.7)', then FN1c, the own-kind bar, with no empty-function clause.",
  "world_is": "Read at HEAD: GRADING_RULE.md R5.b (@3cc090827f) reads 'If this step leaves no function token, v1.7 does not say what follows (row LGIC_NAMING-W3-S5)'. v1.7 grade.unplaceable RAISES 'a name the tokeniser cannot place', which could be read to cover the case, but the function clause does not say so. Reach: 0 of 68 round-2 attributed forms (this seat's recount) and 0 of the rule's worked cases. LIVE_NAMES.json is NOT EVALUATED for it, by the worker or by this seat. The worker's hand case shows the order matters: FN1b then FN1c empties [orion, lambda] with no RAISE, while the reverse order RAISES.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-W3-S5",
    "org/standards/NAMING_SCHEMA.json v1.7 at HEAD: resource.function, grade.unplaceable",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@3cc090827f R5.b"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W3-S5"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S22",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T15:10:15Z",
  "one_line": "ROUND-3 L9, GRADUATED to 1.0.0_SA_CTO: the grading rule grades against v1.7 for R5 only. G2 still RAISES the AWS-fixed names that v1.7 aws_fixed puts outside the grade, and V-2 lists two placeholders that v1.7 grade.placeholder refuses. The header discloses the split. The G2 half is round 1's W1-S4, whose remediation row stays OPEN.",
  "class": "OBSERVATION",
  "spec_asserts": "TO-LN-g-1-r3 step 5: 'The header names NAMING_SCHEMA.json v1.7 as the version the rule grades against'; and 'No other step moves.'",
  "world_is": "Read at HEAD. GRADING_RULE.md:58-64 (G2) RAISES the VPC default SECURITY_GROUP, IAM_POLICY and IAM_ROLE names beginning AWS or Amazon, and AWS-fixed LOG_GROUPs. NAMING_SCHEMA.json v1.7 aws_fixed (AW1, v1.5) puts such names OUTSIDE the grade's domain: 'excluded, never a fourth verdict', SECURITY_GROUP ['default'] by name, and an AWS-managed IAM_POLICY read from its ARN. GRADING_RULE.md:334 (V-2) lists {system}, {source}, {scope}, {tier}, {cadence} and {entity}; v1.7 grade.placeholder (PH1) admits only {system}, {source}, {scope} and {cadence}. The worker's field diff finds 15 changed fields between v1.4 and v1.7; only G2 and V-2 were read against the rule. REMEDIATION_v1's W1-S4 asks for 'exclude AWS-issued names in the data file'. That half landed at v1.5; the rule half did not.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-W3-S6",
    "org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md at HEAD :58-64 (G2), :334 (V-2), header",
    "org/standards/NAMING_SCHEMA.json v1.7 at HEAD: aws_fixed, grade.placeholder",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/remediations/REMEDIATION_v1.md row LGIC_NAMING-W1-S4 (OPEN)"
   ]
  },
  "adjudicates": [
   "LGIC_NAMING-W3-S6"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_NAMING-C-S23",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-15T15:10:15Z",
  "one_line": "ROUND-3 L9, the prior rounds' OPEN remediation rows read against this round's evidence. Five of round 2's six are REMEDIATED and advance in place: C-S14, W6-S4, W4-S2, S14 and S15. W4-S1 stays OPEN, because LN-f-1's face was not re-cut. Round 1's W6-S1, S12 and W1-S4 stay OPEN. Separately, the standing census found S3, graduated at C-S2, with no remediation row, and REMEDIATION_v3 backfills it.",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: 'A graduated row whose remedy was executed ... carries REMEDIATED'. Gate _monotone_advance: a remediation row's remediation.state may move OPEN -> REMEDIATED and closed false -> true in place, and nothing else may change.",
  "world_is": "Each advance is read against its row's own remedy text. C-S14: FN1b is ruled (v1.7) and LN-e-1..LN-e-3 re-ran, and E3T is 18 of 18 identical by this seat's own read. W6-S4: demo is ruled FIRM (DM), the reader may know positions (POS), the key is unchanged, and LN-e-4/LN-e-5 re-ran to 18 of 18 correct by this seat's own read. W4-S2: RULING FN1c. GRADING_RULE.md gains the step, and the forms change 0 of 68 by this seat's recount. S14: all four callers read at HEAD, and the doctored pair is proved (C-S19). S15: the worked example is replaced, and 'orion-inf-build-gold-profile' is absent from NAMING_SCHEMA.json at HEAD. Stays OPEN: W4-S1, whose remedy names LN-f-1's face at a re-cut, and LN-f-1 was not re-cut (R3's adjacency sentence serves the rule, not the face). W6-S1 and S12: of their three remedy parts, the clean seat and the jointly satisfiable re-cut are EXERCISED, but the row-id path for blind cells is not measured here. W1-S4: C-S22. S3: latest disposition GRADUATED at C-S2 (ADJUDICATION_v1), and 0 remediation rows name it across REMEDIATION_v1 and REMEDIATION_v2.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/remediations/REMEDIATION_v2.md@ab8d584c0f (6 rows, all OPEN before this slug)",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/remediations/REMEDIATION_v1.md@9129bf0be3 (W6-S1, S12, W1-S4)",
    "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_NAMING-C-S2 (S3 GRADUATED)",
    ".tools/surprise-row-gate.py _monotone_advance (the in-place advance limb)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A state read. It adjudicates no new item: the five advances land on their own rows as the gate's monotone advance, S3's backfill lands as its own remediation row, and the rows left OPEN are named with the part of their remedy still owed.",
  "hazard_standing": "INERT"
 }
]
```
