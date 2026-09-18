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

## Round 1 -- L8/L9: 12 rows dispositioned, four disarmed on their owners' own acts, fourteen judgment criteria graded

```json
{
 "id": "LGIC_LGCTFM-C-S2",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T02:05Z",
 "one_line": "FOUR ROWS GRADUATED AND DISARMED -- S3, W1-S1, W2-S1 and W2-S2. Every one disarms on its OWN OWNER'S act, and this seat re-derived all four rather than accepting the evidence rows that assert them.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "R-19: the CVO holds the pen and is never the word. Each of these four has an owner who ACTED, which is stronger than a word, and each act was checked here. S3 (the composite run directory): its own finding first -- the 20:25Z directory's contract.json, plan.json, PLANT.json and PLANT_UNTYPEABLE.json are byte-identical to the LATER run 20260917T233115Z-a89fd61 while its VINTAGE.json still declares the 20:25Z run, confirmed by hashing all five with the re-handed run as a control that correctly DIFFERS. Its cure (evidence row S8) is real: the re-handed run 20260918T011619Z-8db9eb1 carries an R-40 HASHES.json whose 8 declared hashes this seat RECOMPUTED under the manifest's own instrument (git hash-object) -- 8 of 8 match, 0 missing -- with MARK.json on disk AND tracked in git for the first time, and the directory self-consistent. W2-S2 (no contract could validate against its own schema): the graded run's contract VALIDATES with 0 schema errors over 184 rows and carries no COGNITO_USER_POOL row, and the schema's node_type enum is still 33 values WITHOUT that type -- so the fix was made at the root (R-36 made the plant opt-in) and the vocabulary was correctly NOT widened to admit an untypeable member. W1-S1 (a graded criterion failing a re-run nothing in its cell changed): the two arms its evidence row S5 claims -- e2-not-covered and e2-not-covered-wrong-raise -- exist and PASS, each carrying a real RED condition ('NOT_COVERED carrying a form must FAIL', 'NOT_COVERED on a non-coverage raise must FAIL'), so the branch has a positive and a negative control rather than an assertion. W2-S1 (the naming gate refusing the engine's own run artifacts) disarms on 1.0.0_SA_CTO's OWN act, its ruling R-35 @5fd4251792, and the cure is verified on the gate's own function: _is_record_tree returns True for the run directory's contract.json and MARK.json, False for workflows/legacy_transform/run_home.py -- the exemption reaches the minted run directory and deliberately NOT the engine-code tree above it -- with a registry path as a negative control reading False.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md, rows S3, S4, S5, S8, W1-S1, W2-S1, W2-S2 -- all read in full",
   "3.0.0_SA_CVO's own recomputation of all 8 hashes in 20260918T011619Z-8db9eb1/HASHES.json under git hash-object: 0 mismatches, 0 missing; MARK.json tracked (git ls-files) in the re-handed run and absent from the composite",
   "3.0.0_SA_CVO's own byte comparison: the composite's contract/plan/PLANT/PLANT_UNTYPEABLE are sha256-identical to 20260917T233115Z-a89fd61's, its VINTAGE.json is not, and the graded run differs from both -- the control that makes the comparison discriminate",
   "3.0.0_SA_CVO's own jsonschema validation of the graded contract against org/standards/LGCTFM_CONTRACT.schema.json: 0 errors, 184 rows, COGNITO_USER_POOL absent; enum measured at 33 values not containing it",
   "3.0.0_SA_CVO's own run of check_lt_r1.py selftest-arms: e2-not-covered and e2-not-covered-wrong-raise both PASS with stated RED conditions; VERDICT PASS-ARMS-DISCRIMINATE",
   "1.0.0_SA_CTO, RULING R-35 @5fd4251792, verified by calling naming-gate.py's own _is_record_tree on the run files, the engine-code tree and a registry path"
  ]
 },
 "disposition": "GRADUATED",
 "hazard_standing": "INERT",
 "adjudicates": [
  "LGIC_LGCTFM-S3",
  "LGIC_LGCTFM-W1-S1",
  "LGIC_LGCTFM-W2-S1",
  "LGIC_LGCTFM-W2-S2"
 ]
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S3",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T02:05Z",
 "one_line": "FIVE ROWS GRADUATED AND STILL ARMED: S6 and W2-S3 from the round, plus this seat's own S10, S11 and S12. None has an owner's word and each names an act nobody has taken.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "S6 -- ANDREW_CARD.md's RECOMMENDATION says 'the two rows touching a live, client-facing surface' and there is exactly ONE. This seat measured it independently across all five run directories at the nested factor path: four runs read client_facing 1 / live 1 / irreversible 0 over 179 tensions, one reads 180 with live 2, and BOTH-together is 1 everywhere. The card's TABLE and its analysis sentence are correct; only the line a decision-maker actually weighs overstates, which is the half that matters. It stays ARMED because the card is in Andrew's hands and the correction has to reach him BESIDE it rather than as a silent rewrite. W2-S3 -- a second DECIDED-but-unmarked prefix (opal-data-bd/silver/, 06_CONFORMANCE_LEDGER.md:72, MIGRATE under R4) on the same bucket and the same evidentiary shape DEC-9 already accepted for gold/; the worker appended it to the marks input, and whether DEC-9's acceptance EXTENDS to a second prefix is a decision no one has made. S10, S11 and S12 are this seat's own findings from the L9 read, graduated in the round they were raised so they carry clocks rather than prose: two branch-relative arms that read FALSE FAIL for any seat re-running them off the worker's checkout; three unpinned numbers in judgment records, two of which disagree with each other; and a card that names no run at all while sitting with a decision-maker.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md rows S6 and W2-S3, read in full",
   "3.0.0_SA_CVO's own factor census across all five run directories, read at factors.<name>.value, with the top-level read kept as a control (it returns a confident 0 for client_facing and live on every run)",
   "infra/logic/06_CONFORMANCE_LEDGER.md:72 for W2-S3's silver/ disposition",
   "Rows S10, S11 and S12 carry this seat's own measurements in their own grounding"
  ]
 },
 "disposition": "GRADUATED",
 "hazard_standing": "ARMED",
 "adjudicates": [
  "LGIC_LGCTFM-S6",
  "LGIC_LGCTFM-W2-S3",
  "LGIC_LGCTFM-S10",
  "LGIC_LGCTFM-S11",
  "LGIC_LGCTFM-S12"
 ],
 "disarm_owner": "per-row: 2.0.0_SA_COO~G on S6, S10, S11 and S12; W2-S3's extension decision rides to 1.0.0_SA_CTO at L10 because DEC-9 is a ratified decision and only its owner can say whether it reaches a second prefix"
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S4",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T02:05Z",
 "one_line": "SIX ROWS DISMISSED: two records and four rows that are themselves the disarm evidence for rows disarmed in C-S2. Graduating an answer row would mint a clock for work already done.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "S2 records that the round-1 cut has four writers of lib/opal_lgctfm.py where decomposition v1's constraint counted three -- found at the L6 cut before any order existed, sequenced by the existing edge LT-e-3 -> LT-p-1, and recorded in v1.1 s.10. Nothing is owed. S7 records that x1-fwd10 was still resolving its subject by POSITION (subject_runs()[0]) after graded_run() was added to the other two arms, so on the re-hand it graded the FIRST hand's FWD10.json -- self-reported by the worker rather than left to stand, and repaired: this seat verified graded_run() is now called at three sites including the x1-fwd10 arm, whose own docstring records the miss. S4, S5, S8 and S9 are the issuer's disarm-evidence rows for W2-S2, W1-S1, S3 and S1 respectively; each is INERT, each is itself an answer, and the rows they answer carry the dispositions. All six are INERT, so R-21 does not reach them.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md, all six rows read in full; hazard_standing verified INERT on each",
   "3.0.0_SA_CVO's own enumerate over check_lt_r1.py: graded_run() called at :1244, :1337 and :1375, the last being the x1-fwd10 arm; remaining subject_runs() uses are enumeration, which is its correct use",
   "The four evidence rows' claims are not dismissed on their own say-so -- each was re-derived in C-S2 before the row it answers was disarmed"
  ]
 },
 "disposition": "DISMISSED_WITH_REASON",
 "hazard_standing": "INERT",
 "adjudicates": [
  "LGIC_LGCTFM-S2",
  "LGIC_LGCTFM-S4",
  "LGIC_LGCTFM-S5",
  "LGIC_LGCTFM-S7",
  "LGIC_LGCTFM-S8",
  "LGIC_LGCTFM-S9"
 ],
 "dismissal_reason": "Records and answer rows. Two record a fact already carried by the decomposition or already repaired and self-disclosed; four ARE the disarm evidence for rows disposed in C-S2. All six INERT, no residue owed."
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S5",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T02:05Z",
 "one_line": "L9 GRADE RECORD, round 1: FOURTEEN judgment criteria, ALL PASS -- and the hand-off's census is the first tonight that reconciles exactly (84 criteria declared across 14 orders, 14 carrying judgment=\"true\", one per order, every <expected_criteria> matching its declarations).",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- a grade record.",
 "world_is": "THE SET WAS RE-MEASURED BEFORE ANYTHING WAS GRADED AGAINST IT, because two hand-offs earlier tonight named judgment sets that did not match their orders -- one naming a criterion that exists in no file, one claiming thirteen where there were twelve. This one is right: 14 order files, 84 criteria declared, exactly 14 carrying judgment=\"true\", no order missing one and none with two, and all 14 status words reading complete. ALL FOURTEEN PASS, which is not a soft result but a reflection of how this round was worked: cell after cell HANDS ITS JUDGMENT OVER rather than self-grading (D1, H1, R1, S1, S2 each state in their own evidence which question is the CVO's), several answer the hard half of their bar with a NEGATIVE that cannot be faked (E2's zero-hit search proving the engine never opens the control file; E1's plant shown outside both instruments by quoting each instrument's own text; X2's mutant that still refuses but stops naming the project), and the one cell whose bar degenerated this round said so instead of claiming the win (V1's single builder fn). E4 is the cleanest against its own bar and X2 carries the strongest argument. THREE THINGS GRADED AROUND RATHER THAN THROUGH, each filed as its own row instead of being folded into a verdict: E3's graded population (271 tensions, 1084 cells) no longer exists anywhere -- the contract at HEAD carries 179 -- so its numbers are unreproducible, and this seat will not grade a cell against R-40, which was issued after it ran (S11). Two of LT-x-1's arms are branch-relative and read FALSE FAIL for any seat re-running them off the worker's checkout, which is the inverse of the known repetition trap: the arm can only be made to pass where passing proves nothing (S10). And ANDREW_CARD.md names no run at all while sitting in a decision-maker's hands (S12). NOT GRADED HERE: RT6-AC1-style mechanical siblings (70 of 70 PASS across the fourteen instances, the issuer's to report), and outcome coverage, which is 1.0.0_SA_CTO's L10 read.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "All 14 order files' <criterion> declarations read for the census; IB-rt-9-style miscounts specifically looked for and not found here",
   "All 14 proof-of-spec instances read; the judgment row of each read in full",
   "3.0.0_SA_CVO's own runs at HEAD on the shared checkout: check_lt_r1.py selftest-arms (PASS-ARMS-DISCRIMINATE), v1-reproduced / v1-order / v1-card / v1-not-author, x1-run-dir / x1-marks / x1-fwd10 / x1-hashes, x2-adding / x2-removing / x2-flag",
   "3.0.0_SA_CVO's own verification of the four disarms recorded in C-S2, including recomputing 8 of 8 declared hashes and calling naming-gate.py's _is_record_tree with a negative control",
   "3.0.0_SA_CVO's own factor census across all five run directories at the nested path, with the top-level read kept as a wrong-reader control"
  ]
 },
 "disposition": "DISMISSED_WITH_REASON",
 "hazard_standing": "INERT",
 "grades": [
  {
   "criterion": "D1R1-AC3",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-d-1-r1.determinism.proof_of_spec.json@cd058652cd",
   "verdict": "PASS",
   "reason": "Both clauses met with the argument shown rather than asserted. The removed sort is named to the line -- lib/opal_lgctfm.py:878 `distinct = sorted(set(members))`, feeding a FORK row's members at :914-921 -- with the reasoning that json.dump(sort_keys=True) orders dict KEYS and never list ELEMENTS, so this is the only site where list order reaches contract.json for that row. QUALIFIED, and the cell qualifies it itself rather than leaving it to be found: the pinned input runs in :leaf mode, which by the code's own docstring skips the live S3 listing, and the claim that the grouping site under test does not read it is an argument from the call graph rather than a measurement. This seat grades that sufficient because the bar asks whether the input is one the engine GENUINELY WALKS rather than a stub that bypasses the walk -- a leaf-mode input is walked by the engine, with one source narrowed -- and because the cell handed the question over instead of resolving it in its own favour."
  },
  {
   "criterion": "E1R1-AC9",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-1-r1.walk.proof_of_spec.json@f64d815ef5",
   "verdict": "PASS",
   "reason": "The third clause is the strong one and it is genuinely established: the plant (opal-data-bd-s3-notify-planted-test-queue) is shown outside BOTH instruments' scope by quoting each instrument's OWN text -- comp-trigger's --list output ('S3 bucket notifications NOT scanned (v1 scope, by design)') and comp_trigger.py's help -- so neither could produce it by name, which is what 'genuinely outside every instrument's scope rather than hidden from one' asks. GAP NAMED: 'each row's declared blind spot is true of its instrument' is established by CONSTRUCTION -- the same five blind-spot strings are written into every cell -- rather than by per-row verification that a given string fits the instrument that produced that row. The construction is over-inclusive rather than wrong (the five are the union across instruments), so no cell carries a FALSE blind spot; what it cannot show is that each cell carries the RIGHT one. Graded PASS on that reading, with the distinction recorded so a later round does not read 'five blind spots per cell' as five per-row measurements."
  },
  {
   "criterion": "E2R1-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-2-r1.desired-and-forks.proof_of_spec.json@a565fbdf4a",
   "verdict": "PASS",
   "reason": "The best discriminator of the fourteen, and it is a negative one: a search of lib/opal_lgctfm.py for the literal FORK_CONTROLS returns ZERO hits, so the engine never opens the control file at all -- which settles 'the seeds name storage locations and not the control pairs' by construction rather than by comparing lists. SEEDS.json carries 7 {bucket, prefix, mode} entries, none matching a control member verbatim. DEC-5's resolution order is coded once in cmd_forks() and applied per fork WITH THE STEP NAMED: FORK-2 and FORK-4 resolve at step 2 (ledger RETIRE), FORK-1 and FORK-3 at step 3 (RULING-OWED, because the ledger disposes MIGRATE rather than a two-member RETIRE split). The cell declines to guess past the ledger, which is the correct stop."
  },
  {
   "criterion": "E3R1-AC6",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-3-r1.tensions.proof_of_spec.json@4bc03940c1",
   "verdict": "PASS",
   "reason": "Graded PASS AT ITS OWN VINTAGE, and the qualification is not decoration. `irreversible` is read from the canon's words as the bar requires -- 02_DOCTRINE.md R1/N5 ('renames authorized: NONE ... moves no live name') and s.5's state-coherence table, with the reasoning that R9's parquet-under-bronze is the canon's own IRREVERSIBLE example and this round's tensions never cite R9. Two rows inspected by hand against their named instruments, 1084 cells swept by the mechanical sibling. THE GRADED POPULATION NO LONGER EXISTS: the evidence reads 271 tensions and 1084 of 1084, and the contract at HEAD carries 179 -- E3 ran before LT-e-4 made the untypeable plant opt-in, which is what moved it. A later reader can neither confirm nor refute those numbers against any current artifact, and the sentence carries no run id. That is R-40's exact subject, R-40 was issued AFTER this cell ran, and this seat will not grade a cell against a rule that did not exist when it ran -- the gap is filed as LGIC_LGCTFM-S11 instead. TWO FACTORS DISCRIMINATE NOTHING THIS ROUND and the cell says so: rules_colliding is 1 for every tension (TENSION_DECIDING_RULES = ['R1'], declared as an exclusion), and client_facing is a static False for every non-S3_BUCKET node type."
  },
  {
   "criterion": "E4R1-AC9",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-e-4-r1.untypeable-opt-in.proof_of_spec.json@b33eaf9840",
   "verdict": "PASS",
   "reason": "The cleanest of the fourteen against its own bar. 'Genuinely OFF rather than defaulted-on-with-a-name' is settled by quoting the declarations -- action='store_true', default=False on both p_walk and p_run -- plus getattr(args, 'plant_untypeable', False), so an absent flag also reads False. The count-equality clause is answered STRUCTURALLY in a way that is better than the measurement the bar would have accepted: contract['untypeable'].value and PLANT_UNTYPEABLE.json's count are written from the SAME Python list in the SAME function call, so a reader checks the equality by reading one function rather than by trusting two independently-computed numbers to agree. Branch-specific blind-spot text for the OFF and ON paths rather than one string covering both. This seat independently confirmed the fix's shape: the graded contract validates with 0 errors and the schema's 33-value node_type enum was NOT widened to admit the untypeable type -- the defect was cured at its root rather than by making the vocabulary accept it."
  },
  {
   "criterion": "H1R1-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-h-1-r1.run-home-diff.proof_of_spec.json@0406a6fa71",
   "verdict": "PASS",
   "reason": "Both clauses met. 'Compiled from the tree, no wall clock in its bytes' is established from the code path: cmd_manifest calls _iter_runs() -> os.listdir(), opening each VINTAGE.json fresh with no state carried from a prior MANIFEST.md -- compile-on-view, which is the property the bar names. The README carries both required statements including the identity key verbatim ('<row_id>|<axis>|<kind>|<deciding_rules sorted, comma-joined> -- never prose'). QUALIFIED: the no-wall-clock claim is a code reading rather than a byte-level diff of two compiles at different times. This seat grades the code reading decisive here, because a wall clock in the bytes would have to appear in that function and it does not."
  },
  {
   "criterion": "P1R1-AC6",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-p-1-r1.plan.proof_of_spec.json@f88d0f9c39",
   "verdict": "PASS",
   "reason": "All three fields are traced to the code that produces them (_build_one_package(): arn = _cv(cur.get('arn_or_path')) or row_id), with the argument that no package writes a row_id absent from the rows_by_id map, and ONE package hand-checked end to end -- R-0221-PORT, reading the real CloudFront ARN EVTSA9VEHNZVH, writing R-0221, with an acceptance_proof citing grade() on that row's own fields. GAPS NAMED, both real: one package of 1626 was sampled by hand and the rest rest on the code argument; and the bar's actual subject -- COULD a COO lane cut a decomposition from this without re-deriving the inventory -- is not testable by the cell that wrote the plan, since no lane tried. This seat grades PASS because the clause the cell CAN reach ('each package's reads, writes and acceptance proof name real rows') is evidenced, and the untestable half is honestly left as what it is rather than claimed. The package count (1626) disagrees with X1R1-AC6's (1074) and neither is pinned to a run -- filed as LGIC_LGCTFM-S11, not held against either grade."
  },
  {
   "criterion": "R1R1-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-r-1-r1.renderer.proof_of_spec.json@105fea6b5b",
   "verdict": "PASS",
   "reason": "The operative half is met: the pictures show what fires what (a concrete fired edge, R-0002 --R-0001--> TRIGGERS), what writes where and what serves it, in DEC-7's column order (TRIGGERS, COMPUTE, TIERS, SERVING), with a FORKS section showing two rows resolving to one desired form. THE HOUSE-STYLE HALF IS A DEPARTURE AND THE CELL DECLARED IT rather than letting it pass: no box-drawing glyphs, no query-plane walkthrough, and one mandatory analogy table reused verbatim on both files, all recorded in the result file's exclusions with the judgment handed to this seat. Graded PASS: a departure that is declared, reasoned and recorded is this estate's DECLARED-EXCEPTION shape, and the bar's substance travels without the glyphs. ONE ITEM NAMED FOR THE NEXT ROUND rather than graded down: an analogy table reused VERBATIM across two different pictures is doing explanatory work on at most one of them -- a mandatory element satisfied by duplication is satisfied in form. If the element is worth requiring, it is worth requiring per-picture."
  },
  {
   "criterion": "S1R1-AC7",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-s-1-r1.contract-schema.proof_of_spec.json@a8fa9e1f8d",
   "verdict": "PASS",
   "reason": "The uncovered-member hunt is done the right way round and that is what earns the grade: it is a RE-DERIVATION against the live file at this commit rather than a copy of the record's printed numbers, and it lands at 0 uncovered, matching s.1.1 independently. Every schema enum value traces to a carrier the record names -- row_kind/RESOURCE/PLANE minted by the record with FORK the one mint, cell_status adopted from ssot_establishment.schema.json, axis from 02_DOCTRINE.md s.2, tension_kind from 06_CONFORMANCE_LEDGER.md s.7, edge_type from evidence-model.md. The cell hands over whether its reading of s.5's remedy table is itself correct, which is the right thing to hand over and does not weaken what it measured."
  },
  {
   "criterion": "S2R1-AC8",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-s-2-r1.receiving-check.proof_of_spec.json@07cf1aca7a",
   "verdict": "PASS",
   "reason": "'Re-implements no rule the schema already carries' is evidenced rather than asserted: each doctored fixture produces BOTH a named-token line AND a schema: line at the same commit, which shows the tool NARRATES the schema's own required-property and type rules in the contract's vocabulary instead of encoding a second independent rule. Route disjointness is argued by enumeration against self_test()'s case table, and the new route is placed FIRST in ROUTES so a later broader pattern cannot silently pre-empt it -- a defensive choice, not an accident. DECLARED LIMIT, correctly: the disjointness check covers EXISTING routes and cannot bound a route nobody has written yet. That is inherent to the question and the cell says so instead of implying coverage it does not have."
  },
  {
   "criterion": "V1R1-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-v-1-r1.reviewer-reproduction.proof_of_spec.json@2ba4c3d4ad",
   "verdict": "PASS",
   "reason": "FWD-3's clause is met as far as it CAN be and the cell names why it degenerates: this run's contract exposes one builder fn ('grade') across all 184 callable rows, so 'spans the builder kinds present' reduces to spanning the five desired.verdict kinds the grade() calls produce, which the sample does (5/4/1/5/5, none of the 184 excluded from eligibility). The reproduction claims behind it are RE-RUNNABLE and were re-run rather than read: v1-reproduced reports 184 callable rows, 20 required, 20 sampled, 20 reproduced by call; v1-order reports 179 tensions with reviewer order == rule order and contract order == rule order both True; v1-card confirms the card carries the contract's ranking_rule verbatim with 10 of 10 top tensions shown; v1-not-author confirms the reviewer (~3) is not among lib/opal_lgctfm.py's authors (~1, ~2). FWD-4's clause is correctly NOT claimed: Andrew's read is not reachable from a worker's instrument, the bar's own APPLIED-with-the-named-actor branch is taken, and the card was recorded for his read rather than a substitute oracle being invented. TWO DEFECTS BESIDE THE GRADE, neither changing it: the card's RECOMMENDATION line overstates the top-priority population by one (row S6), and the card names no run id at all (row S12)."
  },
  {
   "criterion": "X1R1-AC6",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-x-1-r1.first-run-and-mark.proof_of_spec.json@fc273d0bc0",
   "verdict": "PASS",
   "reason": "FWD-10's live-plane clause is met with real instrument discipline: both AWS reads used the identical comp-find --corpus aws pattern before the run verb and after the mark commit, both served-plane reads used projection_client.py against the same live distribution EVTSA9VEHNZVH, and the cell ran a genuine NEGATIVE CONTROL ON INSTRUMENT TARGETING by confirming against E1DHJH4Y1W8YC2, which serves opalinvest.com and is not the portal. delta_outside_run is empty, DRIFT bands are identical, and no AWS write call was made at any point. The S3/S7/S8 history behind this cell resolves cleanly and this seat verified it: graded_run() selects the run CARRYING AN R-40 HASHES.json -- 1 of 5 -- which is identity rather than position, x1-hashes reads 8 declared and 0 mismatches, x1-marks reproduces PASS now that MARK.json is committed for the first time, and x1-run-dir reports 0 missing run files and 0 schema errors on the graded contract. GAP NAMED: FWD-1's half -- that the contract lets the migration's opener learn what the pipeline is made of without listing it by hand -- is asserted from the artifact's shape, because no opener tried it. Also 1074 packages here against P1R1-AC6's 1626, neither pinned (row S11)."
  },
  {
   "criterion": "X2R1-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-x-2-r1.planted-refusal.proof_of_spec.json@1b45fb4d55",
   "verdict": "PASS",
   "reason": "The strongest ARGUMENT of the fourteen, on the hardest clause to evidence. The plant is shown to be a genuine hand-kept use rather than a gate-tripping string by its own shape: a second freshness watch on the SAME A_00 gate artifact the file already watches, with the same fields and naming convention as every entry in a 437-line file, for a named consuming script with a tighter threshold -- and the file's own comment documents exactly that pattern ('Monthly/annual variants share this vintage (trivially-addable siblings)'). The cell anticipates the obvious objection and answers it: reusing the existing artifact's exact s3_key_prefix 'is what a second watch on the SAME artifact means -- the literal being unchanged is what makes the addition genuine'. The mutant control closes it: a fabricated suffix still refuses but STOPS NAMING ADVI_FIRMBKTS, which is the opposite of what a shaped-to-trip string would need. The discriminating pair re-runs clean off-branch (x2-adding REFUSE 2 graded, x2-removing PASS 0 graded, estate flag untouched). CARRIAGE DEFECT, not a grade: this is the one instance of the fourteen whose judgment row carries no `judgment` field (judgment: None where the other thirteen read true). The checker passes it regardless, so the flag is unenforced -- the second instance of that exact class this seat has measured tonight across two projects."
  },
  {
   "criterion": "X3R1-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-x-3-r1.second-run-diff.proof_of_spec.json@aa18cf366e",
   "verdict": "PASS",
   "reason": "Both clauses met, and the first is met in the way that actually matters: DIFF.md ALONE states CLOSED: 0, OPENED: 1 with the single identity string R-0185|A3|GRAMMAR|R1, and UNCHANGED: 179 with every identity listed -- so a reader who opens neither run learns what closed, opened and stayed from that file and nothing else. The result file names the one change the practice wave made, verbatim and singular: one added --seed-loc (opal-data-49financial:_campaign/), one previously-unwalked live S3 prefix surfaced, one new PLANE row whose S3Key grade() call RAISEs at K1. The arithmetic is self-consistent against the 180-tension run it diffs (179 unchanged + 1 opened)."
  }
 ],
 "dismissal_reason": "This row grades fourteen judgment criteria and adjudicates no investigation item; it is a grade record, per the schema's own note for this shape."
}
```
