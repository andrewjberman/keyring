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

## Round 1 close-out -- the eight carrier-less rows disposed outside a round

```json
{
 "id": "LGIC_LGCTFM-C-S6",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T06:20Z",
 "one_line": "SIX EVIDENCE ROWS DISMISSED -- S13, S14, S15, S17, S19 and S20. Each is an owner's word or a repair record answering a row disposed elsewhere, and each is INERT. Disposed OUTSIDE a round, which is this seat's call and is settled on the merits rather than on what the gate allows.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "THE TIMING CALL, answered: DISPOSE NOW rather than carry to round 2's L9. Round 1 closed at L10 and all eight were filed after that close, so no L9 in flight can reach them; round 2 is not cut and nobody has said when it will be. Two of the eight are ARMED, and an item with no carrier does not wait -- it decays, while the measurements inside it are freshest now. The mechanical question was settled before the call reached this seat: _worker_carrier_violations is WORKER-scoped (it returns [] for any non-worker author) and GATE (iii) refuses a new ROUTE-CARRYING row, never a disposition, so nothing prevents disposing with no round open. THE SIX: S13 and S14 answer this seat's own S10 -- the branch-relative arms are repaired by binding to IDENTITY rather than POSITION, and S14's word rests on the row's own discriminator, that they PASS in the SHARED checkout. S15 answers S11: the convention exists as R-40 and is applied twice, and the row states its own honest limit rather than overclaiming. S17 answers S6: the correction reached the decision-maker BESIDE the card via the CTO's adjudication and the card's bytes were never rewritten, which is the exact shape S6's own condition required. S19 answers S16 and S12's underlying finding: the restated remedy is performed as CARD_SUBJECT_PIN.md. S20 answers W2-S3 under R-49 -- DEC-9 never admitted a prefix at all, so there was nothing to extend, which dissolves the question rather than deciding it. NONE carries `adjudicates` and none is ARMED, so R-21 does not reach them and dismissal is available.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md -- all six read in full",
   "2.0.0_SA_COO~G msg 97852 (the census) and 1.0.0_SA_CTO msg 97854 (the call, R-54 @eeaaf56cbe)",
   "VERIFIED BY THIS SEAT, not accepted from S14: check_lt_r1.py x1-r16 -> PASS-X1-MARK-COMMIT-PRINTS-TARGETS and x1-footprint -> PASS-X1-REPO-FOOTPRINT-BOUNDED, both run at HEAD on the SHARED checkout, which is the precise place S10 measured them reading FALSE FAIL",
   "VERIFIED BY THIS SEAT for S19: org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/CARD_SUBJECT_PIN.md pins run 20260918T011619Z-8db9eb1 and contract content hash 33204e29839de89af81fb293317cce3ccdf2266d, names git hash-object as its instrument, and states that a plain sha1 of the same bytes reads differently -- the instrument being part of the value. That hash matches this seat's own recomputation of the manifest during the round-1 L9."
  ]
 },
 "disposition": "DISMISSED_WITH_REASON",
 "hazard_standing": "INERT",
 "adjudicates": [
  "LGIC_LGCTFM-S13",
  "LGIC_LGCTFM-S14",
  "LGIC_LGCTFM-S15",
  "LGIC_LGCTFM-S17",
  "LGIC_LGCTFM-S19",
  "LGIC_LGCTFM-S20"
 ],
 "dismissal_reason": "Owner's-word and repair-record rows, each answering a row disposed elsewhere; all six INERT, none carrying `adjudicates`, no residue owed by any seat."
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S7",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T06:20Z",
 "one_line": "S16 and S18 GRADUATED. S16's restated remedy is PERFORMED, so it graduates with its clock already closed; S18 is a NEW finding this seat verified and it stays ARMED -- S10's class has FOUR members and the two nobody named fail SILENTLY.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "S16 is the RESTATEMENT of this seat's S12, and restating rather than disarming was the correct act by its owner: the remedy S12 named -- one line in ANDREW_CARD.md -- is one the issuer is MECHANICALLY FORBIDDEN to perform, because owned-paths clause 4 refuses an issuer's edit inside a worker's deliverables folder, measured on that exact file and reverted. The reason moved and the owed act moved with it, and S19 records that act performed as CARD_SUBJECT_PIN.md. So S16 graduates with a closed clock. WHAT REMAINS TRUE AND IS RECORDED RATHER THAN SWEPT: the card's OWN bytes still name no run, and no seat but a worker or the CTO can change that -- the hazard is now a KNOWN limitation carried in a durable hash-bound record with a negative control, which is what S12 existed to buy, rather than a silent one. S18 IS REAL AND THIS SEAT CONFIRMED IT INDEPENDENTLY rather than taking the row: x2-flag prints `commits on this branch touching org/mcp/naming-gate.enforce: ''` and PASSES, and x3-filed prints `OPENED tensions 0; ADVI_FIRMBKTS channel rows added on this branch 0 []` and PASSES -- both on an EMPTY window, so each would pass identically had the cell touched nothing at all. That is a VACUOUS PASS, which is the dangerous half of the class R-47 and R-48 name, and it is strictly worse than S10's FALSE FAIL: a false fail announces itself and gets investigated, a vacuous pass is indistinguishable from a real one. It stays ARMED. Its non-repair is correct and stated: these are fixed inputs of a CLOSED, GRADED round, their windows were non-empty on their own branches so the grades they fed are sound, and editing them now would move no grade while falsifying a frozen record (R-43's scope).",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md rows S16 and S18, read in full",
   "VERIFIED BY THIS SEAT at HEAD on the shared checkout: x2-flag -> PASS-X2-ESTATE-FLAG-UNTOUCHED on an empty commit window; x3-filed -> PASS-X3-OPENED-ROWS-FILED on 0 opened and 0 filed. Both passes are vacuous exactly as S18 states.",
   "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/CARD_SUBJECT_PIN.md, read by this seat for S16's performed remedy",
   "R-47 and R-48 @1582e48505 for the vacuous-pass class; R-43 for why a frozen graded input is not rewritten"
  ]
 },
 "disposition": "GRADUATED",
 "hazard_standing": "ARMED",
 "adjudicates": [
  "LGIC_LGCTFM-S16",
  "LGIC_LGCTFM-S18"
 ],
 "disarm_owner": "2.0.0_SA_COO~G on S18; S16 carries no live hazard, its clock closes with this write"
}
```

## Round 2 -- L8/L9: three judgment criteria graded, four rows dispositioned

```json
{
 "id": "LGIC_LGCTFM-C-S8",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T09:55Z",
 "one_line": "L9 GRADE RECORD, round 2: THREE judgment criteria, all PASS. The hand-off's prose says four and its own list names three -- the list is right, and the mechanical count is 11 rather than the 12 it states.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "THE SET, measured from the orders rather than inherited: three round-2 order files declare 14 criteria by a raw tag count (5 + 4 + 5) of which exactly THREE carry judgment=\"true\", one per order -- A2R2-AC5, N2R2-AC5, C2R2-AC4 -- and each order's <expected_criteria> matches its own declarations. So the mechanical remainder is 11, not the 12 the hand-off reports, and its 'four judgment criteria' is one over a list that is itself correct. BOTH FIGURES RUN ONE HIGH WHILE BOTH LISTS ARE RIGHT, which is the same shape this seat has now measured in four hand-offs tonight and is benign here only because the lists are what a grader acts on. No grade moves and nothing is asked of the issuer's re-runs. ALL THREE PASS, and in all three the finding outranks the pass exactly as the hand-off says. What I would carry out of this round is C2R2-AC4's: a worker CORRECTED ITS OWN ISSUER on a mechanism sentence that had reached four carriers by being COPIED rather than re-derived, where every published number was right and only the explanation was half -- the failure mode that fires on the first later seat who follows the recipe rather than the numbers.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "All three round-2 orders read for their bars verbatim and censused by raw <criterion tag count",
   "All three proof instances read in full",
   "VERIFIED BY THIS SEAT at HEAD: e2-reproduce, x3-diff and x3-nontrivial all FAIL from the shared checkout, and this seat's OWN run of e2-reproduce during round 1's L9 returned PASS -- the before and after of live-builder drift held by one seat",
   "VERIFIED BY THIS SEAT: git hash-object == git rev-parse HEAD:<path> == 33204e29839d...; plain sha1 9c5cdb873f00...; prefix-only sha1 d07bf29d245f...; 790871 - 24967 CRLF pairs == 765904 committed bytes"
  ]
 },
 "disposition": "DISMISSED_WITH_REASON",
 "hazard_standing": "INERT",
 "grades": [
  {
   "criterion": "A2R2-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-a-2-r2.re-derivation-record.proof_of_spec.json@cd58e124b7",
   "verdict": "PASS",
   "reason": "BOTH HALVES MET, and the first half I can corroborate from my OWN earlier run rather than from the record. ON 'GENUINELY RE-RUN': the record's strongest evidence is that three arms came back FAIL from the third position where they fed PASS grades in round 1, and I re-ran all three at HEAD on the shared checkout -- e2-reproduce FAIL-E2-DESIRED-EQUALS-BUILDER, x3-diff FAIL-X3-COMMITTED-DIFF-REPRODUCES, x3-nontrivial FAIL-X3-WAVE-MOVED-SOMETHING. I ALSO RAN e2-reproduce MYSELF DURING ROUND 1's L9 AND IT RETURNED PASS, so I hold the before and the after on one arm from one seat, which is as direct a demonstration of live-builder drift as this project can produce and is not available to the cell. A restatement of a round-1 instance cannot manufacture three FAILs. The two further artefacts of an actual run are the right kind: a probe that read ABSENT because its needle copied the CITATION's spelling rather than the file's, and a negative control that fired the wrong way first. ON 'MECHANISM CENSUS RATHER THAN THE HANDED LIST': the census is an AST call-graph closure over the checker's OWN SUBCOMMANDS table (67 arms, 165 functions), a DIFFERENT instrument from S18's grep of one helper name -- which is what makes its agreement on {x2-flag, x3-filed} corroboration rather than repetition -- and it went BEYOND the handed four in three directions. The part that earns the grade is that 11 flagged arms were then hand-inspected and FIVE WERE CLEARED: a list that only grows is not a census. The cell also declares its two judgment calls inside the classification so they can be refused, and names the class a static census cannot reach at all."
  },
  {
   "criterion": "N2R2-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-n-2-r2.number-pins.proof_of_spec.json@797a1c4026",
   "verdict": "PASS",
   "reason": "ON THE DENOMINATOR: 520 digit runs against 17 surviving numbers is 30x larger than what was pinned, so it cannot be a count of what the cell happened to pin -- which is the exact failure the bar names. It is built from an enumeration BY EXISTENCE (git ls-files over the project's proof instances) and the widest field set the rows offer, with the axis named so a reader can reject it, and the path from 520 to 17 is a printed ledger of declared classes that must close against its own denominator. The detail that shows the ledger is real rather than decorative: it REFUSED THE RUN four times on this cell's own work, three path-rule drafts that ate the verdict spread and a re-measure limb that read RAISE as 0 against a cited 5. A classifier that has never refused its author is not evidence. ON THE HASHES: each is computed by git hash-object and required to equal git rev-parse HEAD:<path>, and I verified that equality myself on the graded contract -- both read 33204e29839de89af81fb293317cce3ccdf2266d. Two agreements with values the cell did not read first are the load-bearing part, and I had independently computed BOTH earlier tonight during round 1's L9 when I recomputed all 8 entries of that run's R-40 manifest: the contract hash and plan.json's f26d46db87f3d8bcbf7b7ff13dafe708030c6d48. A copied hash could not produce them. The cell states plainly what it does not claim -- that its domain choice is right -- and excludes 6 tokens BY CLASS on a stated reading of R-40, which is the correct way to hand a domain decision to the grader."
  },
  {
   "criterion": "C2R2-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-c-2-r2.card-names-its-subject.proof_of_spec.json@64450fcdcc",
   "verdict": "PASS",
   "reason": "ON 'UNAMBIGUOUS TO A STRANGER': a run id and a hash are necessary and the cell is right that they are not sufficient. It answers the three questions a stranger would otherwise have to ask, ON THE FACE -- which file the hash is of, WHY two identifiers are needed (four other run directories share the same 'built 18:16 UTC' subject and one holds 180 tensions rather than 179, which is what makes the timestamp insufficient and the hash decisive), and how to re-derive it with a named producer plus a cross-check that returns the same value. I verified that cross-check: git hash-object and git rev-parse HEAD:<path> both return 33204e29839d... THE THIRD ELEMENT IS NOT DECORATION AND I RE-MEASURED IT IN FULL, because it is the mechanism a later seat would re-derive from: the plain sha1 of the checkout reads 9c5cdb873f00..., and the 'blob <len> NUL prefix' explanation ALONE returns d07bf29d245f... -- a third number in no record. The real cause is that git hash-object runs the EOL FILTER FIRST, and the arithmetic closes exactly: 790,871 checkout bytes minus 24,967 CRLF pairs equals the 765,904 committed bytes. Every published number was correct and only the stated mechanism was half, which is the kind of defect that fires on the FIRST later seat who follows the recipe. ON 'READS AS PART OF THE CARD': the addition continues the card's own section, voice and tense one paragraph after the sentence it completes, re-flows no heading or existing sentence, and is 22 insertions with 0 deletions. THE CELL'S ONE DECLARED OVERREACH IS ACCEPTED AND I SAY SO EXPLICITLY: the order required a pointer and the cell put S6's correction ('1 of 179, not two') on the card's face, attributed and NOT applied to the recommendation above it. It offers to cut back if I read the bound narrowly. I do not: S6's condition was that the correction not be SILENT, a reader reaching the ranking should not have to open a commit to learn the line above it is corrected, and the graded refusal to touch the ranking or the recommendation is what keeps this an addition rather than a rewrite."
  }
 ],
 "dismissal_reason": "This row grades three judgment criteria and adjudicates no investigation item; it is a grade record."
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S9",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T09:55Z",
 "one_line": "S23 and W2-S4 DISMISSED -- and they FALSIFY THIS SEAT'S OWN ROW S11, correctly. I verified the falsification myself before accepting it, because a seat correcting another's work gets the least scrutiny exactly when it has earned some.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "S11 WAS MINE AND BOTH ITS HALVES ARE WRONG. It said P1R1-AC6's 1626 packages and X1R1-AC6's 1074 'cannot both be true of one plan', and that E3R1-AC6's 271-tension population 'no longer exists anywhere'. MEASURED BY THIS SEAT with the unscoped census S11 should have run: 12 tracked files are named contract.json and the 271-tension population is present at HEAD in TWO BYTE-IDENTICAL files (deliverables/0.9.0_WK_LGIC_LGCTFM~1/walk/contract.json and ~2/plan_r1/contract.json, 271 tensions / 278 rows, one hash); and of 17 tracked plan.json, 1626 belongs to deliverables/~2/plan_r1/plan.json while 1074 belongs to the run-directory plans -- two different plans, both numbers true. THE SHAPE OF MY ERROR IS THE TRANSFERABLE PART AND IT IS WORSE THAN A STALE NUMBER. I scoped the census to the run directories under workflows/legacy_transform/ and then wrote the unscoped word 'ANYWHERE'. The population was in the DELIVERABLES tree the entire time. That is Rule 24's domain failure -- a subtraction over the wrong domain arrives with a printed denominator and so reads as measured -- and it is the same trap I caught myself on hours earlier when I censused quarantine keys in four firm buckets the writer never writes to. Catching it once did not stop me writing it again in a row. AND THE SECOND HALF: I inferred a CONTRADICTION from two numbers that were never about one object. Nothing established they described one plan; I supplied that premise myself. Both rows are INERT, carry no `adjudicates`, and are dismissed as the answers they are -- S11's clock was already closed at 06:20Z on a different ground (the convention existing), so no clock moves here; what this record adds is that S11's FINDING was wrong, so a later reader does not inherit it as established.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S23 and #LGIC_LGCTFM-W2-S4, both read in full",
   "VERIFIED BY THIS SEAT: git ls-files *contract.json -> 12 tracked, 271/278 present at HEAD in two byte-identical files; git ls-files *plan.json -> 17 tracked, 1626 and 1074 on two different plans",
   "The census S11 ran was scoped to workflows/legacy_transform/ run directories; the population it declared absent lives under org/missions/.../deliverables/"
  ]
 },
 "disposition": "DISMISSED_WITH_REASON",
 "hazard_standing": "INERT",
 "adjudicates": [
  "LGIC_LGCTFM-S23",
  "LGIC_LGCTFM-W2-S4"
 ],
 "dismissal_reason": "Both are evidence rows answering S11, both INERT, neither carrying `adjudicates`. Dismissed with the correction recorded: S11's premise is falsified and its clock was already closed on other grounds."
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S10",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T09:55Z",
 "one_line": "W1-S22 GRADUATED and DISARMED on its owner's own corrective act @ee4dbdf774; W1-S21 GRADUATED and STAYS ARMED -- round 1's non-re-derivable population has causes that are not positions, and live-builder drift is one I can demonstrate from my own two runs.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "W1-S22 is the row a worker filed against its own issuer, and its remedy is done by that issuer: commit ee4dbdf774 by 2.0.0_SA_COO~G corrects the live carrier, while the three frozen carriers stand under R-43 because rewriting a completed record falsifies history rather than repairing it. I re-measured every number before accepting the disarm and the mechanism closes arithmetically (790,871 checkout bytes - 24,967 CRLF pairs == 765,904 committed). The distinction the row draws is the valuable one: EVERY PUBLISHED NUMBER WAS CORRECT and only the stated CAUSE was half, so nothing downstream was wrong and yet the first later seat to follow the recipe would have produced d07bf29d... and concluded the PIN was wrong. W1-S21 STAYS ARMED and its non-repair is correct: R-43 scopes a frozen-history defect's remedy to one live-direction document, and editing check_lt_r1.py or any round-1 fixed input was refused by the order and not done. Its live-builder-drift limb is the one I can corroborate independently -- e2-reproduce returned PASS when I ran it during round 1's L9 and FAILs on the same shared checkout now, so an arm of a CLOSED cell whose mechanical criteria graded PASS is no longer reproducible, and that is a property of the arm's dependence on a live builder rather than of where it runs.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S21 and #LGIC_LGCTFM-W1-S22, both read in full",
   "git log ee4dbdf774 -- 2.0.0_SA_COO~G's own correction of the live carrier",
   "VERIFIED BY THIS SEAT at HEAD: the four hash numbers and the CRLF arithmetic; e2-reproduce FAIL now against this seat's own PASS during round 1's L9"
  ]
 },
 "disposition": "GRADUATED",
 "hazard_standing": "ARMED",
 "adjudicates": [
  "LGIC_LGCTFM-W1-S22",
  "LGIC_LGCTFM-W1-S21"
 ],
 "disarm_owner": "2.0.0_SA_COO~G on W1-S21, as the row names; W1-S22's clock closes with this write on that seat's own corrective act"
}
```

## Out-of-round disposition -- S24 (0 open orders, no carrier)

```json
{
 "id": "LGIC_LGCTFM-C-S11",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T13:20Z",
 "one_line": "S24 DISMISSED, AND IT IS RIGHT ON EVERY LIMB -- I verified it at the PRD's own bytes and the decisive evidence is a NEGATIVE with a denominator: `C6` occurs ZERO times in 397 lines of the PRD. The register's stated mechanism for FWD-6 is FALSE; the VERDICT (UNREACHABLE) is unchanged; and the corrected mechanism points at ADVI_FIRMBKTS, which is the same project R-75 names as the only queued one that unblocks D14.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "DISPOSED OUTSIDE A ROUND DELIBERATELY: LGIC_LGCTFM reads 0 open orders and this was its only undispositioned row, so it had NO CARRIER and would have decayed until some future round had a reason to look -- the exact condition this seat's own tick checks for. VERIFIED AT THE BYTES BEFORE ACCEPTING, because 2.0.0_SA_COO~G's row corrects that seat's OWN project register and a correcting seat gets the least scrutiny exactly when it has earned some. FWD-6's ACCEPT at PRD :119-120 reads 'the 49 Financial migration's decomposition starts from the run's plan instead of rebuilding the inventory from scratch' -- S24 quotes it correctly. The PLAN row at :177 names its consumer verbatim: 'consumed by the subject's migration project at L5 (`ADVI_FIRMBKTS` first)' -- also correct. AND THE DECISIVE ONE IS THE NEGATIVE, WITH ITS DENOMINATOR: the token `C6` occurs ZERO TIMES across all 397 lines of LGIC_LGCTFM_PRD.md, and while `LGIC_CANON` occurs on 4 lines, none of them is in FWD-6's region (:116-120). So the register's claim that FWD-6 'closes when a real migration's decomposition is cut from the plan -- WHICH IS LGIC_CANON's C6 PRACTICE WAVE' has no basis in the PRD at all, and under R-51 DONE resolves on the PRD's outcome array rather than on a register's gloss of it. S24's own discriminator is the stronger argument and it is empirical rather than textual: C6 ALREADY RAN at LGIC_CANON round 4 -- this seat graded C6R4-AC8 PASS itself, reached 12 + carded 4 -- AND FWD-6 DID NOT MOVE. If the register's mechanism were right, FWD-6 would have closed then. A stated mechanism that has already been exercised without producing its stated effect is falsified by its own best case. WHAT THIS CHANGES AND WHAT IT DOES NOT: the VERDICT does not move -- FWD-6 remains UNREACHABLE by any act of this fabric, exactly as R-75 classified it, so nothing about D14's stop-condition loosens. What moves is the ROUTE, and it matters: FWD-6 terminates at ADVI_FIRMBKTS, not at a sibling project's practice wave. R-75 measured that LGIC_CANON's FWD-5 also terminates at ADVI_FIRMBKTS (carded steps 10 and 16) and that ADVI_FIRMBKTS sits THIRD in the next-COO-slot queue while being the only one of the four that unblocks anything in D14. THIS ROW ADDS A SECOND, INDEPENDENT ROUTE TO THAT SAME CONCLUSION, reached from a different project's PRD by a different seat. Two of D14's four members now demonstrably bar on one unseated project, and one of the two was barring on it through a mechanism nobody had stated correctly until now -- which means the dependency was real while the written reason for it was wrong, and a reader trusting the register would have looked to LGIC_CANON to unblock it. That strengthens R-75's card 6 rather than changing it, and card 6 is Andrew's to answer; I am recording evidence, not re-ordering a sequence.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S24 -- 2.0.0_SA_COO~G's row, read in full",
   "VERIFIED BY THIS SEAT at the bytes: org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md :119-120 (FWD-6 ACCEPT) and :177 (the PLAN row naming ADVI_FIRMBKTS as L5 consumer)",
   "VERIFIED BY THIS SEAT, denominator printed: `C6` occurs 0 times across 397 lines of that PRD; `LGIC_CANON` occurs on 4 lines, none in :116-120",
   "This seat's own LGIC_CANON round-4 L9: C6R4-AC8 graded PASS, reached 12 + carded 4 == 16 of 16 -- C6 ran and FWD-6 did not move",
   "R-75 @f28bf76f81: LGIC_CANON and LGIC_LGCTFM both classified UNREACHABLE; ADVI_FIRMBKTS third in the next-COO-slot queue and the only one of four that unblocks D14"
  ]
 },
 "adjudicates": [
  "LGIC_LGCTFM-S24"
 ],
 "disposition": "DISMISSED_WITH_REASON",
 "hazard_standing": "INERT",
 "dismissal_reason": "An INERT evidence row carrying no `adjudicates` of its own, correcting a register's stated mechanism. Verified correct at the PRD's bytes on every limb, including a negative with its denominator. No residue is owed inside this project's engine -- the verdict it examines does not move -- and its substance is carried into the D14 stop-condition record as a second independent route to ADVI_FIRMBKTS."
}
```

## Out-of-round disposition -- S25 (0 open orders, no carrier)

```json
{
 "id": "LGIC_LGCTFM-C-S12",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-18T15:30Z",
 "one_line": "S25 DISMISSED and every cited fact verified at the bytes. ROUND 1's GRADE STANDS -- I graded it and a later AUTHORIZED deletion does not falsify a closed round. THE TRANSFERABLE HALF: A RE-RUN OF A CLOSED ROUND'S ARM THAT NOW FAILS IS NOT A DEFECT IN THAT ROUND, and this is the THIRD instance of that shape on this project alone.",
 "class": "OBSERVATION",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "DISPOSED OUTSIDE A ROUND DELIBERATELY: LGIC_LGCTFM reads 0 open orders and this was its only undispositioned row, so it had NO CARRIER and would have decayed -- the condition this seat's tick exists to catch, and the second time today on this same project. EVERY CITED FACT VERIFIED AT THE BYTES rather than accepted: the old path .claude/skills/lgctfm/SKILL.md is ABSENT from the worktree and the new .claude/skills/legacy-transform/SKILL.md is PRESENT; the deleting commit is e2aa0d51c8 by 0.4.0_DS_ClientPlatform~X; check_lt_r1.py:50 pins SKILL = \".claude/skills/lgctfm/SKILL.md\" verbatim; and :565-568 reads tag = \"E1-SKILL-INVOKES-ENGINE\" / t = read(SKILL) / if t is None: / return say(\"FAIL-\" + tag, \"absent: %s\" % SKILL). So the arm's FAIL branch is reachable and deterministic on the absence. I READ THAT BRANCH RATHER THAN RUNNING THE ROUND-1 CHECKER, and say so: the branch is unconditional on a None read and re-running a closed round's whole fixed input would be disproportionate, but that is a READ and not an EXERCISE. AND I HOLD ONE INSTRUMENT THE FILING SEAT COULD NOT: the live invocation frame `legacy-transform` APPEARS IN THIS SEAT'S OWN AVAILABLE-SKILLS LISTING THIS TURN, which confirms the replacement from the CONSUMER side rather than from the filesystem. That is corroboration on a genuinely different plane. ROUND 1's GRADE STANDS AND THE REASON IS NOT MERELY R-43. R-43 says frozen history is not falsified by a later authorized change, which is true and sufficient. The sharper statement is that a FAILING RE-RUN AND A WRONG GRADE ARE DIFFERENT CLAIMS: the arm asserted a file existed AT THE LT-e-1 VINTAGE and it did; it now reports absence because Andrew retired the file on 2026-09-18, verbatim 'get rid of the stale skill'. An arm that fails because its SUBJECT was authorizedly removed is measuring the present against a past bar, which is the instrument working correctly and reporting a true fact about today. THIS IS THE THIRD INSTANCE OF THAT SHAPE ON THIS PROJECT ALONE and they are worth reading together: W1-S21 (round-1 arms non-reproducible through LIVE-BUILDER DRIFT), R38-AC2 on IRPT (a criterion certifying a FUTURE state of a shared artifact, falsified 83 minutes later by an authorized re-mint), and now S25 (an arm's subject authorizedly deleted). In all three the cell was right, the record was right at its vintage, and a later legitimate act made the evidence non-reproducible. THE FIVE FROZEN SURFACES ARE CORRECTLY NOT REWRITTEN -- the PRD, the decomposition, the LT-e-1 order, that cell's proof instance and result, and the round-1 fixed input all still name the retired path, and rewriting any of them would falsify history to make a re-run green, which is precisely the move R-43 forbids. THE ONE RESIDUE, NAMED BECAUSE IT HAS NO OWNER: the two workflows/ README edits that would complete the house's two-way cross-reference are REFUSED TO THE FILING SEAT by the owned-paths lane gate (lane ANY_EXEC_OR_AE) and wait on a permitted seat. That is real, small, and currently carried by nobody -- this project has no round in flight to pick it up. It is named here so a permitted seat can take it rather than leaving it to be rediscovered.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S25 -- 0.4.0_DS_ClientPlatform~X's row, read in full",
   "VERIFIED BY THIS SEAT: old path ABSENT, new path PRESENT in the worktree; deleting commit e2aa0d51c8",
   "VERIFIED BY THIS SEAT at the bytes: check_lt_r1.py:50 pins the retired path; :565-568 returns FAIL-E1-SKILL-INVOKES-ENGINE on a None read",
   "VERIFIED ON AN INSTRUMENT UNIQUE TO THIS SEAT: `legacy-transform` is present in this seat's own available-skills listing at this turn -- the replacement confirmed from the consumer side",
   "Andrew-direct 2026-09-18, verbatim: 'get rid of the stale skill'",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S21 -- the live-builder-drift sibling of this shape"
  ]
 },
 "adjudicates": [
  "LGIC_LGCTFM-S25"
 ],
 "disposition": "DISMISSED_WITH_REASON",
 "hazard_standing": "INERT",
 "dismissal_reason": "An INERT record of an authorized retirement, carrying no `adjudicates` of its own and no hazard. Round 1's grade stands under R-43 and under the sharper reading that a failing re-run and a wrong grade are different claims. The five frozen surfaces are correctly left naming the retired path. One residue is named rather than closed: the two workflows/ README cross-reference edits are refused to the filing seat by lane ANY_EXEC_OR_AE and are carried by nobody, so a permitted seat should take them."
}
```

## Round 3 L9 adjudication (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S13",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T00:20Z",
 "class": "OBSERVATION",
 "one_line": "LGIC_LGCTFM ROUND 3 L9 -- THE THREE JUDGMENT CRITERIA, ALL PASS, EACH ON AN INSTRUMENT THIS SEAT RAN ITSELF. The count was verified by subtraction rather than taken from the hand-off: 5 criteria carry judgment=\"true\" across the four round-3 orders, MINUS X4R3-AC5 whose order is superseded-never-spawned, MINUS none other -- leaves 3, and the hand-off named 3. That is the FOURTH consecutive hand-off from 2.0.0_SA_COO~G with no count running high, and X4R3-AC5 is named here rather than left to vanish with its cell.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "Graded at HEAD 7f48a0ff42 on the shared tree. For each criterion the instrument is named and is NOT the worker's: R2R3-AC4 by importing lib/lgctfm_render.py and rendering all 5 contracts; E5R3-AC5 by reading COVERAGE_EVIDENCE.json's per-node leg attribution and by comp-find --corpus aws on the live plane; P2R3-AC4 by two field-shaped censuses over git ls-files with printed denominators. Every number below is from those runs.",
 "grades": [
  {
   "criterion": "R2R3-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-r-2-r3.no-bare-none.proof_of_spec.json@295ae45768",
   "verdict": "PASS",
   "reason": "THE READER LEARNS IT, AND I READ THE BYTES THE RENDERER PRODUCES RATHER THAN THE WORKER'S QUOTATION OF THEM. Importing lib/lgctfm_render.py@d701235a50 and calling render_current() on all 5 contracts under workflows/legacy_transform/ gives, in 5 of 5, a COMPUTE section opening 'coverage: NOT MEASURED -- this contract carries no coverage block, so the rows below are what the walk rowed, not what the subject has; an empty or short COMPUTE column is the instrument's limit, not proof the subject has none' and closing 'no rows rendered in COMPUTE -- read the coverage line above before reading this as the subject has no compute'. THE CRITERION SAYS 'EMPTY OR SHORT', SO I TESTED BOTH AND THE THIRD BRANCH TOO: with a coverage block and involved > rows the column opens 'short by N, named below'; with the column absent from by_node_type it prints '0 row(s) of 0 involved node(s)' AND, on the next line, 'no node_type of this column was measured'. All three branches answer the question, so PASS. TWO QUALIFICATIONS, BOTH MINE AND BOTH FILED RATHER THAN LEFT IN PROSE: 'short by N, named below' can name nothing when not_covered is empty (row S33, unreachable on today's one coverage block, 0 of 19 node_types), and the third branch's FIRST line reads as a measured zero with the disclosure on its SECOND line. Neither defeats the criterion; both are things a reader of this grade should have."
  },
  {
   "criterion": "E5R3-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-5-r3.discovery-by-design.proof_of_spec.json@b736ee4fdf",
   "verdict": "PASS",
   "reason": "'INVOLVED' IS A REAL DEFINITION ON ALL THREE OF THE CRITERION'S SUB-QUESTIONS, EACH MEASURED SEPARATELY. (1) EVERY LEG IS EXERCISED AND NONE IS DECORATIVE -- over the 381 involved nodes, the count of nodes whose ONLY leg is that leg is token 210, iam_grant 92, trigger_target 33, source_text 7; delete any leg and named nodes leave the set. (2) THE EXCLUSION IS REAL, NOT A STRAWMAN, AND ITS OWN PREMISE HOLDS: all 9 excluded /aws/lambda/ log groups are live nodes at grade time (comp-find --corpus aws, vintage 2026-09-18 22:13:04 UTC), and the reason they are excluded -- 're-created when its function, which IS a row, migrates' -- is TRUE for 9 of 9, because each named function appears in the contract's 370 row names. (3) THE DECISIVE ONE: a Lambda reached only through trigger_target or iam_grant IS rowed -- 58 of 67 involved Lambdas carry NO token leg and 58 of 58 are present in the contract's rows, including exactly the four opal-assets-bd49f-* and -bd49finsurance functions the WORD-BOUNDED token rule provably cannot reach (each verified non-word-bounded for both 49f and 49financial). MY GRADE-TIME LIVE CENSUS READ 13 /aws/lambda/ log groups matching 49f against the walk's 9 EXCLUDED, AND I STATE THE INSTRUMENT DIFFERENCE RATHER THAN THE NUMBER: my pattern was a SUBSTRING and the walk's is WORD-BOUNDED, and the 4-node difference is exactly those four bd49f names -- which the walk reaches by other legs anyway."
  },
  {
   "criterion": "P2R3-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-p-2-r3.step-dependencies.proof_of_spec.json@df4753e185",
   "verdict": "PASS",
   "reason": "ONE STALE READER EXISTS, THE CELL FOUND IT, AND TWO INDEPENDENT ARMS OF MINE FIND NO SECOND. ARM 1 (key-access shape, over git ls-files minus npm/lock/node_modules): DENOMINATOR 38296 tracked files, 35890 readable, 25 files carrying a programmatic 'dependencies' key access or literal key -- every one of them a vendored numpy or pydantic file, an npm package.json reader, an ATOM package manifest, a frozen plan.json under R-43, check_lt_r3.py reading the OLD field on the OLD plan by design, or a record about this very rename. ARM 2 (list-membership shape, tracked .py minus vendored layers): DENOMINATOR 5074 files, 3 hits, of which exactly ONE is a genuine stale reader -- fixed_inputs/r1/check_lt_r1.py:84 PACKAGE_FIELDS, which is precisely what row W1-S31 names. I SAY WHERE MY OWN INSTRUMENT WAS BLIND: ARM 1 COULD NOT SEE THE ONE THAT MATTERS, because a bare list element does not match a key-access pattern; arm 2 was built to close that hole, and the cell's comp-find census found it without either. ARM 3 WAS THE WRONG INSTRUMENT AND IS REPORTED AS SUCH: the plain word over 19705 tracked .md files hits 1474 of them, because 'dependencies' is ambient English -- a printed denominator certifying a sweep that cannot discriminate the question."
  }
 ],
 "disposition": "DISMISSED_WITH_REASON",
 "dismissal_reason": "A GRADE RECORD. It disposes no investigation item -- 'adjudicates' is absent and the dispositions for this round are carried by C-S14 and C-S15 -- so the row takes the disposition the schema requires of it and claims nothing further.",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "3.0.0_SA_CVO's own runs at HEAD 7f48a0ff42: render_current() over 5 of 5 contracts; COVERAGE_EVIDENCE.json leg attribution over 381 involved nodes; comp-find --corpus aws (13 hits across 2590 nodes, vintage 2026-09-18 22:13:04 UTC); two field-shaped censuses (38296 and 5074 file denominators)",
   "check_lt_r3.py selftest-arms at HEAD: PASS-ARMS-DISCRIMINATE, 27 arms driven"
  ]
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S14",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T00:20Z",
 "class": "OBSERVATION",
 "one_line": "SEVEN GRADUATED, EACH WITH ITS REMEDIATION ROW MINTED IN THIS SAME COMMIT so no item leaves L9 without a carrier -- S21, S26, W1-S24, W1-S25, W1-S30 from the round, plus S32 and S33 which are this seat's own L9 findings and are graduated under the same bar as everyone else's.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "S21 (4.0.0_SA_CRO): the INF gold chain's completion marker last written 2026-09-05, the MDPF accelerator rule live and unfired for 13 days while the backstop schedule hides it. It is a LIVE-ESTATE finding belonging to no LGIC round, which is exactly why it decays without a row -- owner 1.0.0_SA_CTO to route. S26 (2.0.0_SA_COO~G): round 3 was cut 25 minutes before R-81 existed; its own drain test S30 read NON-CONFORMANT on both halves, so it STAYS ARMED, LT-x-4 is not spawned, and the conformance repair leads round 4 -- the only remediation row of this set that carries an ARMED clock, and it is the issuer's. W1-S24: comp-trigger has NO path that reads a Scheduler schedule's targets (23 of its 167 entries); the walk covered them through comp-kuzu, so nothing is blocked and the gap is in the tool. W1-S25: the commit gate's MANIFEST-ADVISORY flags two Cypher strings that ARE routed through comp-kuzu and says both 'would block in blocking mode' -- a CONFORMANT caller would be refused if the advisory ever became blocking. W1-S30: the order's third write site does not exist AND THAT HALF NEEDS NO ACT, as its disarm owner says in decomposition s.14; what is graduated is the OTHER half the same row measured -- plan.md renders no step relation under either spelling, so the machine artifact now carries step_dependencies and the human one carries nothing. S32 and S33 are mine, filed in this commit, and are stated at their own rows.",
 "adjudicates": [
  "LGIC_LGCTFM-S21",
  "LGIC_LGCTFM-S26",
  "LGIC_LGCTFM-W1-S24",
  "LGIC_LGCTFM-W1-S25",
  "LGIC_LGCTFM-W1-S30",
  "LGIC_LGCTFM-S32",
  "LGIC_LGCTFM-S33"
 ],
 "disposition": "GRADUATED",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- one row per id in this list, minted in the same commit",
   "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.14 -- the disarm owner's word on W1-S30 and W1-S31, read at the bytes"
  ]
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S15",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T00:20Z",
 "class": "OBSERVATION",
 "one_line": "FIVE DISMISSED, FOUR OF THEM 2.0.0_SA_COO~G NAMING ITS OWN DEFECTS -- and the one that matters most, W1-S23, is dismissed because I RE-RAN ITS ARM rather than because its issuer said it was fixed.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "W1-S23 (BLOCKING, the worker's): the arm could not read PASS for ANY correct record at the path the order mandated. DISMISSED BECAUSE IT IS RESOLVED AT ITS CAUSE AND I MEASURED THAT: running check_lt_r3.py e5-schema at HEAD prints 'lgctfm-contract-check (receiving-check does not ROUTE this path -- W1-S23) rc=0 ACCEPT' then 'VERDICT: PASS-E5-SCHEMA', rc 0 -- and it names which instrument answered, which is the part that makes the repair honest rather than a bypass. The worker refused to work around it and filed BLOCKING, which is what the order asked for. .tools/receiving-check.py is NOT defective here: it routes by path, contracts belong in the run home, and the order named the wrong path. S29: the issuer's own record of that repair; the defect and the fix are both its own and both are on the record, so nothing is owed. S27: the issuer told a live worker a false fact (comp-trigger --list carries targets); the correction is recorded, the worker measured the same thing independently at W1-S24, and the leg was built on the sources that do carry targets -- so the false premise propagated into no artifact. What survives from it is the TOOL gap, and that is carried by W1-S24's remediation row rather than duplicated here. S28: an R-82 PRE-SPAWN amendment, recorded before the spawn as R-82 requires, with no criterion, grant, expect or invocation changed; a record, correctly filed, needing no act. S30: S26's drain test. It is EVIDENCE, not a separate hazard -- its NON-CONFORMANT reading is precisely why S26 stays ARMED, and S26's remediation row is the carrier. Disposing it again would mint a second carrier for one remedy. S31: the issuer's close record; every substantive half it carries is dispositioned on its own row here. W1-S31: DISMISSED ON THE DISARM OWNER'S WORD PLUS MY OWN READ OF THE REMEDY, not on the word alone -- decomposition s.14.1 exists, is marked [HARD], states that every arm of a closed round's checker is frozen against that round's own artifacts and that a run against a later artifact is neither a regression nor evidence, and it names what would REOPEN it (a round that re-uses check_lt_r1.py as a live instrument). That is the R-43 remedy, and it is written.",
 "adjudicates": [
  "LGIC_LGCTFM-S27",
  "LGIC_LGCTFM-S28",
  "LGIC_LGCTFM-S29",
  "LGIC_LGCTFM-S30",
  "LGIC_LGCTFM-S31",
  "LGIC_LGCTFM-W1-S23",
  "LGIC_LGCTFM-W1-S31"
 ],
 "disposition": "DISMISSED_WITH_REASON",
 "dismissal_reason": "Each id's reason is stated at its own name in world_is. None of the seven leaves an act owed by anyone: two are resolved at their cause (W1-S23 by S29's repair, re-run PASS here), one is carried by another row's remedy (S30 by S26), one's surviving half is carried by W1-S24, two are records correctly filed (S28, S31), and one has its R-43 remedy written and read (W1-S31).",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "3.0.0_SA_CVO's run of check_lt_r3.py e5-schema at HEAD 7f48a0ff42: PASS-E5-SCHEMA rc 0",
   "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.14.1, read at the bytes",
   "fd02b24c51 -- the issuer's repair commit for S29 / W1-S23"
  ]
 }
}
```

## Round 3 L10 -- disposition of LGIC_LGCTFM-S34

```json
{
 "id": "LGIC_LGCTFM-C-S16",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T01:20Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "LGIC_LGCTFM-S34 GRADUATED. The round analysis is ACCEPTED in full and nothing here disputes it -- the bar's DIRECTION is right and its REMEDY is right. What is measured is its TRIGGER's price, and the measurement is the kind the bar's own author asked for by naming a command.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "I ran the discriminator the analysis names, over the backlog, before round 4 adopts it. It returns non-zero on 63 of 112 evaluable proofs, so 'usually returns zero' does not hold on this estate, and a bar that fires on the majority case will either be paid in full every round or quietly skipped -- and the second is how a bar becomes a convention. I ALSO STATE THE NARROWING I TRIED THAT FAILED: the round-match axis subtracted zero. This row does not propose a mechanism; choosing the trigger is the analysis author's, and the remediation row is addressed accordingly.",
 "adjudicates": [
  "LGIC_LGCTFM-S34"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md#LGIC_LGCTFM-S34 -- the carrier, minted in this same commit"
  ]
 }
}
```

## Round 4 L9 adjudication (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S17",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T05:55Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "LGIC_LGCTFM ROUND 4 L9 -- THE THREE JUDGMENT CRITERIA, ALL PASS, EACH WITH THE DECISIVE CHECK RUN BY THIS SEAT; TEN GRADUATED WITH A CARRIER EACH. The count is by subtraction: 3 criteria carry judgment=\"true\" across the three round-4 orders, nothing to subtract, and the hand-off named 3.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "Graded at HEAD b93693e3b7. FOUR OF THE ISSUER'S OWN ARMS GRADED THE WRONG OBJECT THIS ROUND AND EVERY ONE WAS FOUND BY THE WORKER IT WAS GRADING, each arriving as a BLOCKING row with its discriminator already measured and none worked around. That is the round's real result and it is why these rows graduate rather than being dismissed as issuer housekeeping: in every case A CORRECT RECORD COULD NOT PASS, so the cheapest satisfying move was to damage something -- fabricate a proof path, write a status the manifest forbids, delete Andrew's comp-tool ledger, or REVERT ANOTHER PROJECT'S COMMIT. W1-S39 is the worst of the four and the issuer says so itself: its cheapest green cost a seat not even in this round. TWO MORE OF THE SAME CLASS (W2-S36, W1-S38) are about a mid-round repair that cannot reach a live worker's worktree while the arm measures that worktree -- a structural fact about repairing fixed inputs mid-round, not a defect in either party.",
 "grades": [
  {
   "criterion": "M1R4-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-m-1-r4.canonical-inventory-entry.proof_of_spec.json@f25d5ff2f5",
   "verdict": "PASS",
   "reason": "THE ENTRY ENDS THE TIE, AND I RE-DERIVED THE RECORD'S OWN SIEVE RATHER THAN READING ITS SUMMARY. At HEAD the manifest holds 129 entries = 128 pre-existing + exactly 1 cloud.inventory.*, which is the entry, carrying status 'canonical'. Re-running the record's sieve over the 128 reproduces its arithmetic exactly: layer==cloud 39, tool==comp-find 1, keyword on the remainder 30, READ 70, UNREAD 58. \u2b50 AND I FALSIFIED THE GAP THE RECORD HONESTLY STATES AND NOBODY HAD TESTED: of the 58 unread entries, the number whose FULL TEXT mentions 'aws' or 'resource' anywhere is 0 OF 58. So no unread entry can be the neighbour a reader with an AWS-resource inventory question would land on, and the stated gap is measured closed rather than merely disclosed. THE TIE IS ENDED BY SPLITTING THE QUESTION, not by ranking tools -- each of R-81's six tied tools is placed and comp-estate is refused BY NAME with its reason -- and the near-duplicates are genuinely different use cases rather than a list assembled to look thorough, because the set was chosen by SUBTRACTION from a printed denominator and the claim's own population was falsified BEFORE the subtraction ran (0 pre-existing entries route this question by any spelling)."
  },
  {
   "criterion": "E6R4-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-6-r4.repoint-and-declare.proof_of_spec.json@5b65010f7b",
   "verdict": "PASS",
   "reason": "A REAL PLANE MOVE, AND THE DISCRIMINATOR IS ONE A RENAME CANNOT PRODUCE. Diffing the round-3 and round-4 coverage evidence myself: roles_read 210 -> 256 (the TF-parsed population replaced by the live one), roles_granting 35 -> 50, compute_reached_forward 85 -> 95, and the fields that only exist on a live read appear -- plane 'LIVE (R-81-assigned)', roles_with_unresolved_managed_statements 148, an enumerated granting_roles, an authorization_instrument with a census_path. \u2b50 THE SECOND-ORDER TELL HOLDS AT THE BYTES: granting_roles_not_in_the_live_graph goes ['opal-49f-value-parity'] -> [], and a declared-but-not-live granting role cannot appear in a live read BY CONSTRUCTION. THE INTERNAL CONTROL IS THE PART I WOULD KEEP: source_text, the leg that did NOT change plane, is byte-identical across both rounds (411 files, 216 functions, 31 naming, the same bd-client-detail residual) -- so the movement is localised to the leg that moved and is not a global re-measure artifact. ON THE DROPS: the record says there are none and scopes that to node_types (19 of 19 held or grew). I FOUND ONE IT DOES NOT NAME -- execution_roles_added 7 -> 5 -- AND CHECKED IT AT A GRAIN NEITHER THE RECORD NOR THE CRITERION SPECIFIES: node IDENTITIES. Round-3 involved nodes absent from round 4: 0 OF 381. Round-3 iam_grant IAM_ROLEs missing from round 4: none. So the sub-metric fall is an ORDERING ARTIFACT -- those roles now arrive via the live granting set before the reverse execution-role step runs, so fewer are newly 'added' AT THAT STEP -- and not a coverage loss. The record's narrowing risk (148 of 256 roles carrying an unresolved attached-managed statement) is disclosed, bounded by the HAS_POLICY sub-leg, and asserted by a DRIVEN arm so it flips when the census improves; and comp-iam simulate is refused ON THE RECORD for population work, which is this criterion's own hazard named and declined."
  },
  {
   "criterion": "X5R4-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-x-5-r4.coverage-run-on-the-repaired-engine.proof_of_spec.json@243c1efd39",
   "verdict": "PASS",
   "reason": "I PERFORMED THE TEST THE CRITERION WRITES RATHER THAN GRADING A DESCRIPTION OF IT: I am the person opening the 49 Financial migration, and I opened the contract and listed the four things FWD-1's ACCEPT names, from the contract alone and with no hand list -- SCHEDULE 10 (advi-49f-gold-floor, advi-49f-publisher, wsb-49f-model-aua-pull-daily, ...), EC2_INSTANCE 20 (bd-49f-auto-login, bd-allocations, ...), IAM_ROLE 57, S3_BUCKET 2 (opal-data-49financial, opal-data-bd), out of 404 rows across 18 node_types. The ACCEPT's sentence is satisfied. ONE GAP FOUND AT A GRAIN THE ACCEPT DOES NOT NAME AND FILED AS LGIC_LGCTFM-S41: 24 of 154 S3Key rows carry no resolvable bucket, so a reader can list the BUCKETS but cannot say which bucket 24 of the KEYS live in. It does not move this verdict -- the criterion asks about the four categories and they are all answerable -- and it is exactly the kind of thing a reader hits on the second question."
  }
 ],
 "adjudicates": [
  "LGIC_LGCTFM-W2-S35",
  "LGIC_LGCTFM-W2-S36",
  "LGIC_LGCTFM-W2-S37",
  "LGIC_LGCTFM-W1-S35",
  "LGIC_LGCTFM-W1-S36",
  "LGIC_LGCTFM-W1-S37",
  "LGIC_LGCTFM-W1-S38",
  "LGIC_LGCTFM-W1-S39",
  "LGIC_LGCTFM-S35",
  "LGIC_LGCTFM-S41"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- one row per id in this list, minted in the same commit",
   "3.0.0_SA_CVO's own runs at HEAD: the manifest sieve re-derived (129 = 128 + 1; 70 read / 58 unread; 0 of 58 mentioning aws or resource), the round3-vs-round4 coverage diff with a 0-of-381 node-identity loss check, and the contract read as FWD-1's reader"
  ]
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S18",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T05:55Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "FIVE DISMISSED, ALL OF THEM THE ISSUER'S OWN EVIDENCE ROWS -- and dismissing them is what keeps one remedy to one carrier.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "S36, S37, S38 and S39 are 2.0.0_SA_COO~G's disarm records for W2-S35, W1-S35, W1-S38 and W1-S39, and the issuer says of each that it is EVIDENCE, NOT A DISPOSITION, carries no `adjudicates`, and leaves the row to this seat. That is exactly right and it is why they are dismissed: each one's substance is carried by the remediation row of the hazard it disarms, and disposing the evidence separately would mint a second carrier for one remedy. S40 is the same shape one round older -- the issuer's long-owed word on W2-S2, which is already GRADUATED and already carries a remediation row, so the evidence attaches to that carrier rather than opening a new one. \u2b50 THE ISSUER FILING ITS OWN ARM DEFECTS AS ROWS, WITH THE DISCRIMINATOR MEASURED AND WITHOUT TOUCHING THE DISPOSITION, IS THE REASON THIS ROUND COULD BE GRADED AT ALL -- the alternative history is four silent repairs and a clean-looking round.",
 "adjudicates": [
  "LGIC_LGCTFM-S36",
  "LGIC_LGCTFM-S37",
  "LGIC_LGCTFM-S38",
  "LGIC_LGCTFM-S39",
  "LGIC_LGCTFM-S40"
 ],
 "disposition": "DISMISSED_WITH_REASON",
 "dismissal_reason": "Each is an issuer EVIDENCE row whose substance is carried by the remediation row of the hazard it concerns (W2-S35, W1-S35, W1-S38, W1-S39 in this round's set; W2-S2's existing carrier for S40). None leaves an act owed, and disposing them separately would mint a second carrier per remedy.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "the four disarm rows' own text, each stating 'evidence, not a disposition'",
   "3.0.0_SA_CVO's check at HEAD that LGIC_LGCTFM-W2-S2 is GRADUATED and carries a remediation row"
  ]
 }
}
```

## Round 5 L9 adjudication (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S19",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T08:10Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "LGIC_LGCTFM ROUND 5 L9 -- M2R5-AC6 PASS. One cell, one judgment criterion, counted by subtraction over the round-5 family. The cell filed NO rows and stated why, which after a round where four of the issuer's criteria were unsatisfiable is evidence about the CUT and not only about the cell.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "Channel at my write time: 60 items, 0 held on either predicate before this row, 0 open orders of 25. The round's product is a measurement and it holds: 24 of 154 S3Key rows resolve to no bucket, two producers at named code sites, zero unattributed, both attributed by instruments RUN. I add one row of my own (LGIC_LGCTFM-S42) on the reported falsification, which is a predicate substitution rather than a contradiction -- the cell's artifact is precise and its own result text distinguishes the shapes correctly; the hand-off's summary is the part that overstates.",
 "grades": [
  {
   "criterion": "M2R5-AC6",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-m-2-r5.which-producer-writes-a-bucketless-key.proof_of_spec.json@a2b05d19c1",
   "verdict": "PASS",
   "reason": "THE CAUSES ARE GENUINELY DISTINGUISHED, NOT MADE TO AGREE, AND THE TWO-SITES-ONE-ROOT SENTENCE -- the one the issuer asked me to press on -- IS THE CAREFUL VERSION RATHER THAN THE TIDY ONE. It does not say 'one cause' and it does not say 'two independent causes': it says two distinct code sites WRITE the value, and both trace to one upstream input defect (portal-stitch S3Key ingestion leaving arn empty when it cannot resolve a single firm-writer bucket), with the SHAPE difference explained as a downstream branch on candidate count rather than as a second external cause. That distinction is load-bearing and the record draws it explicitly -- 'a repair that fixed the upstream ingestion could plausibly resolve both at once' -- which is the fact a premature single-remedy cell would have hidden, and it is why the CTO cut this as a MEASUREMENT cell. ON THE SECOND HALF, EVERY how_it_was_attributed NAMES AN INSTRUMENT THAT WAS RUN, not a reading of the path already on the page: comp-find --corpus aws on each of the 23 bare keys (three same-name candidates each), comp-kuzu MATCH with the Cypher printed, confirming source='portal-stitch' / origin_reason='ambiguous-across-firms' / arn='' for all 23; and for the single firm-prefixed row a comp-kuzu MATCH plus the code read at :929-930. Zero unattributed, with the escape unused and the reason stated. \u26a0 ONE FINDING, FILED AS LGIC_LGCTFM-S42 AND NOT MOVING THIS VERDICT: the round's reported FALSIFICATION of the analysis's 'malformed single-colon s3:' characterisation is a PREDICATE SUBSTITUTION. The cell measured 'bare s3:, head empty' (0 of 6 runs, correct) against an analysis claim about a SINGLE-COLON SCHEME (1 row, which I re-measured myself and which the cell's own text concedes as 'a genuine s3:<key> value'). The cell's artifact is precise; the hand-off's summary of it is stronger than the measurement supports."
  }
 ],
 "adjudicates": [
  "LGIC_LGCTFM-S42"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "3.0.0_SA_CVO's own sweep of all 6 run contracts and read of BUCKETLESS_S3KEY_R5.json at HEAD ccbf4ac3cb",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- the carrier, minted in this commit"
  ]
 }
}
```

## Round 6 L9 -- E7R6-AC7 graded, S43 and S44 disposed (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S20",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T11:05Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "L9 round 6: E7R6-AC7 PASS -- the ephemeral instrument's verdict is graded WITHOUT trusting its provenance, because every fixture parameter it encodes is a committed round-5 live measurement and the comfortable answer was reachable on-population. S43 GRADUATED: the preservation remedy worked, and the standing cut-time fix is the carrier.",
 "spec_asserts": "A judgment criterion is graded at L9 against evidence the grading seat can read.",
 "world_is": "PASS. The issuer handed me the crux verbatim -- the instrument that produced TWO_REPAIRS ran in a SESSION SCRATCHPAD no other seat can open -- so I graded the claims that are falsifiable WITHOUT trusting that provenance, and every one of them held. (1) THE PRESERVED BYTES ARE THE CLAIMED BYTES: 8247 bytes, sha256 d418b2706442df10e8146bc6c8c10ae8678c56645d3da9be04acef72337b5e5f -- matches the row's claim exactly, committed b6a963e49c, worktree clean. That proves UNALTERED SINCE HASHING, not WHAT RAN, so it is where the grade starts and not where it ends. (2) THE TWO COPIED CODE SITES ARE VERBATIM AT THE CITED VINTAGE: I printed lib/opal_lgctfm.py at 21ca7eb0802b14ff7194553a526078bc4ce36b7d and compared. Site A (:923-933, the kuzu ingestion loop) and site B (:956-964, resolve()) are byte-identical to the script's ingest() and make_resolve() except for one cosmetic variable-init collapse and one dropped inline comment; no executable token differs. (3) SITE C IS NOT A COPY AND THE RECORD DOES NOT SAY SO -- this is the one place the experiment substitutes a PREMISE for code. cf_node_for() HARDCODES arn_or_path to the bare name, asserting comp-find's S3Key band prints no detail line; the real parser at :372-380 fills arn_or_path from the NEXT line and falls back to the name only when that line is absent. The script assumes the antecedent. THE VERDICT TURNS ENTIRELY ON THAT PREMISE: if S3Key rows carried a detail line, by_arn would hit and the answer would be ONE_REPAIR. (4) SO I FALSIFIED THE PREMISE INDEPENDENTLY, AND IT IS A ROUND-5 LIVE MEASUREMENT, NOT AN ASSUMPTION: BUCKETLESS_S3KEY_R5.json (committed, cell LT-m-2, _about says MEASUREMENT) records 154 S3Key rows, 24 bucketless, split 23 tier / 1 firm, and attributes them by RUNNING THE TOOLS -- 'RAN .tools/comp-find --corpus aws <bare-key> for each row's key: every one returns exactly THREE S3Key candidate nodes' and 'RAN .tools/comp-kuzu MATCH for the row's key: exactly ONE candidate node'. All THREE fixture parameters the experiment encodes -- three tier candidates, one firm candidate, blank S3Key detail line -- are each a committed round-5 live measurement. The production docstring at :358-360 names S3Key by name as a blank-detail type too, but that is the author's claim and I did not rest on it. (5) I RAN THE PRESERVED SCRIPT MYSELF, from this seat, and it reproduces 23/1 -> 23/0 and TWO_REPAIRS. (6) AND I TESTED REFUSABILITY BY MUTATION rather than accepting the checker's 23 self-test arms, which grade the CHECKER's functions and never the experiment's own branches: mutating only the AFTER arm so the repair DOES reach the tier class makes the same code print 'tier_prefixed 23 -> 0' and VERDICT: ONE_REPAIR. The comfortable answer was reachable on-population and the cell did not take it. THE PATH IS EXERCISED, NOT SKIPPED: resolve() is genuinely called 23 times in both arms and runs the full by_arn -> by_tn -> synthetic chain; the AFTER arm really does change an input (portal_arn_tier from empty to a bucketed arn) and the count really does not move -- which is the discriminating observation, not an absence of one. ONE DEFECT FOUND IN THE INSTRUMENT, DISCLOSED HERE BECAUSE IT DOES NOT MOVE THE VERDICT AND A SEPARATE HELD ROW WOULD DEADLOCK THIS L10 FOR NOTHING (LD-0521). The experiment's TWO_REPAIRS test is `after_tier == before_tier and after_firm == 0`, and 0 == 0 SATISFIES IT VACUOUSLY -- so the predicate cannot distinguish 'the repair never reached the tier class' from 'the tier class was never broken', and in the degenerate world it SHADOWS the ONE_REPAIR branch beneath it. I found this by running the WRONG mutation first: I inverted site C in BOTH arms, which drove before_tier to 0 as well, and the script still printed TWO_REPAIRS. That mutation was off-population -- round 5 MEASURED 23 broken -- so I re-cut it to move only the AFTER arm, and that is the run that proved ONE_REPAIR reachable. I am reporting the wrong mutation as well as the right one because a reader who repeats only the published one learns the wrong lesson about what the falsifier tested. WHY IT DOES NOT MOVE THE GRADE: before_tier is 23, it is PRINTED beside the verdict, and it is independently corroborated by a committed round-5 artifact, so the degenerate world cannot occur on this population. Neither the checker's AC3 arm (it reads the record's verdict STRING) nor its 10 positive-satisfiability arms (they drive the CHECKER's functions) can see this -- it lives in the experiment's own branch order.",
 "adjudicates": [
  "LGIC_LGCTFM-S43"
 ],
 "disposition": "GRADUATED",
 "grades": [
  {
   "criterion": "E7R6-AC7",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-7-r6.one-repair-or-two.proof_of_spec.json@2d7c6c509b",
   "verdict": "PASS",
   "reason": "PASS. The issuer handed me the crux verbatim -- the instrument that produced TWO_REPAIRS ran in a SESSION SCRATCHPAD no other seat can open -- so I graded the claims that are falsifiable WITHOUT trusting that provenance, and every one of them held. (1) THE PRESERVED BYTES ARE THE CLAIMED BYTES: 8247 bytes, sha256 d418b2706442df10e8146bc6c8c10ae8678c56645d3da9be04acef72337b5e5f -- matches the row's claim exactly, committed b6a963e49c, worktree clean. That proves UNALTERED SINCE HASHING, not WHAT RAN, so it is where the grade starts and not where it ends. (2) THE TWO COPIED CODE SITES ARE VERBATIM AT THE CITED VINTAGE: I printed lib/opal_lgctfm.py at 21ca7eb0802b14ff7194553a526078bc4ce36b7d and compared. Site A (:923-933, the kuzu ingestion loop) and site B (:956-964, resolve()) are byte-identical to the script's ingest() and make_resolve() except for one cosmetic variable-init collapse and one dropped inline comment; no executable token differs. (3) SITE C IS NOT A COPY AND THE RECORD DOES NOT SAY SO -- this is the one place the experiment substitutes a PREMISE for code. cf_node_for() HARDCODES arn_or_path to the bare name, asserting comp-find's S3Key band prints no detail line; the real parser at :372-380 fills arn_or_path from the NEXT line and falls back to the name only when that line is absent. The script assumes the antecedent. THE VERDICT TURNS ENTIRELY ON THAT PREMISE: if S3Key rows carried a detail line, by_arn would hit and the answer would be ONE_REPAIR. (4) SO I FALSIFIED THE PREMISE INDEPENDENTLY, AND IT IS A ROUND-5 LIVE MEASUREMENT, NOT AN ASSUMPTION: BUCKETLESS_S3KEY_R5.json (committed, cell LT-m-2, _about says MEASUREMENT) records 154 S3Key rows, 24 bucketless, split 23 tier / 1 firm, and attributes them by RUNNING THE TOOLS -- 'RAN .tools/comp-find --corpus aws <bare-key> for each row's key: every one returns exactly THREE S3Key candidate nodes' and 'RAN .tools/comp-kuzu MATCH for the row's key: exactly ONE candidate node'. All THREE fixture parameters the experiment encodes -- three tier candidates, one firm candidate, blank S3Key detail line -- are each a committed round-5 live measurement. The production docstring at :358-360 names S3Key by name as a blank-detail type too, but that is the author's claim and I did not rest on it. (5) I RAN THE PRESERVED SCRIPT MYSELF, from this seat, and it reproduces 23/1 -> 23/0 and TWO_REPAIRS. (6) AND I TESTED REFUSABILITY BY MUTATION rather than accepting the checker's 23 self-test arms, which grade the CHECKER's functions and never the experiment's own branches: mutating only the AFTER arm so the repair DOES reach the tier class makes the same code print 'tier_prefixed 23 -> 0' and VERDICT: ONE_REPAIR. The comfortable answer was reachable on-population and the cell did not take it. THE PATH IS EXERCISED, NOT SKIPPED: resolve() is genuinely called 23 times in both arms and runs the full by_arn -> by_tn -> synthetic chain; the AFTER arm really does change an input (portal_arn_tier from empty to a bucketed arn) and the count really does not move -- which is the discriminating observation, not an absence of one."
  }
 ],
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S43",
   "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-7-r6.one-repair-or-two.proof_of_spec.json@2d7c6c509b -- acceptance[6] E7R6-AC7, judgment=true, status UNVERIFIABLE-BY-INSTRUMENT naming 3.0.0_SA_CVO as the substitute oracle",
   "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/preserved_evidence/r6/experiment.py.preserved.txt @b6a963e49c -- 8247 bytes, sha256 d418b270...b5e5f verified by this seat, and RUN by this seat",
   "lib/opal_lgctfm.py@21ca7eb0802b14ff7194553a526078bc4ce36b7d :923-933, :956-964, :372-380 -- the three cited sites printed at the cited vintage and compared token by token",
   "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/BUCKETLESS_S3KEY_R5.json -- the round-5 MEASUREMENT (154 rows, 24 bucketless, 23 tier / 1 firm) whose live tool runs independently establish all three fixture parameters",
   "this seat's on-population mutation: AFTER arm only -> 'tier_prefixed 23 -> 0', ONE_REPAIR"
  ]
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S21",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T11:05Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "S44 GRADUATED: the issuer filed its own three-round silence on W2-S2 rather than letting it read as progress, and declined to cut round 7 into an open L10 for the reason LD-0521 names. Both halves are correct and the row is a transfer, not a closure -- W2-S2 stays ARMED and round 7 is its carrier.",
 "spec_asserts": "An armed blocking row is driven by the rounds that follow it.",
 "world_is": "VERIFIED AT MY OWN INSTRUMENTS RATHER THAN ACCEPTED. The open-order census the row cites reads 0 of 26 from the gate's own resolver at HEAD a94858ff96, so the LD-0521 reasoning rests on a true premise: a round-7 issuance cut before this slug would have flipped the count off zero and deadlocked the very L10 I am writing. \u2b50 THE ROW'S REAL MERIT IS THE HALF NOBODY IS OBLIGED TO WRITE: three rounds passed without touching W2-S2 and NOTHING IN THOSE ROUNDS' RECORDS SAID SO -- silence and work read identically from outside, and the issuer filed against itself to break that tie. I GRADUATE IT RATHER THAN DISMISS IT because the hazard is live: W2-S2 remains ARMED with the COGNITO_USER_POOL node_type outside LGCTFM_CONTRACT.schema.json's 33-value enum, so no contract the engine emits can validate against its own schema. \u26a0 AND THE CLOCK DOES NOT MOVE HERE: the disarm owner stays 2.0.0_SA_COO~G and the remedy is round 7 covering W2-S2, not this disposition. What graduating changes is that the row stops being a held item with no carrier and becomes a named obligation on the recut.",
 "adjudicates": [
  "LGIC_LGCTFM-S44"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S44",
   "srg._open_tos_for_project at HEAD a94858ff96: 0 open of 26, census note empty",
   "srg._latest_dispositions at HEAD a94858ff96: LGIC_LGCTFM-W2-S2 still UNDER_INVESTIGATION and ARMED",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- the carrier, minted in this commit"
  ]
 }
}
```

## Round 7 L9 -- three judgment grades, three rows disposed (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S22",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T14:20Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "L9 round 7: ALL THREE judgment criteria PASS. N3R7-AC4 -- I recomputed the emitted set off the run's own 575 rows and got the record's 18 exactly, where the enum would have given 33. G1R7-AC4 -- I built a MATCHED-PAIR control the record did not have and ran both arms. R3R7-AC4 -- re-derived, and my own first arithmetic check was repetition. S45 and S46 GRADUATED.",
 "spec_asserts": "Judgment criteria are graded at L9 and never self-graded.",
 "world_is": "N3R7-AC4: PASS. The criterion's sharpest question is whether the EMITTED set was read off the RUN or assembled from the enum, and that is decidable at the bytes, so I decided it there rather than reading the record's assurance. I opened the run's own walk_r7/contract.json and computed sorted(set(r['node_type'] for r in rows)) MYSELF over its 575 rows: 18 members, and the record's emitted set EQUALS MINE EXACTLY. \u2b50 THE DISCRIMINATION IS BUILT INTO THE TWO NUMBERS: a set assembled from the schema would have been 33, not 18. 18 is what 575 real rows actually produced, and the gap is the answer. The run's own independent cells corroborate from a second direction -- contract.json's untypeable reads 0 and its coverage block's not_covered reads 0, both MEASURED by the walk rather than asserted by the cell. So emitted_minus_declared = 0 is a GENUINE ZERO: not a cell that found nothing, but a walk that emitted 18 types every one of which the enum declares. \u2b50 AND THIS IS THE CASE THE POSITIVE ARM EXISTED FOR. W2-S2's round-2 premise was that an unconditional COGNITO_USER_POOL plant put a node type outside the enum; the plant now fires only behind --plant-untypeable, off by default, and is never written into rows. A bar that could only pass ON A VIOLATION would have pressed this cell to manufacture one. It did not have to, and that is the arm working rather than the round being lucky. || G1R7-AC4: PASS, and I did not merely re-run the cell's control -- I BUILT A TIGHTER ONE AND RAN BOTH ARMS SEPARATELY. The whole of branch (B) rests on one claim: that the exemption is a SCOPED run-directory carve-out and not a gate that has gone silent on workflows/legacy_transform/ wholesale. The record's scoping control demonstrates it with a different path from the admitted set. \u2b50 MINE IS A MATCHED PAIR -- IDENTICAL CONTENT, IDENTICAL BASENAME, DIFFERING ONLY IN WHETHER THE PATH SITS INSIDE A MINTED RUN DIRECTORY: (A) workflows/legacy_transform/blackdiamond-49financial/scratch-probe.json carrying {\"bucket\": \"opal-data-bd\"} -> NAMING REFUSE ... opal-data-bd -> opal-data-49financial, '1 seen', rc=1; (B) the SAME filename and the SAME bytes at workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/scratch-probe.json -> NAMING-GATE: PASS 0 graded, '0 seen', rc=0. One directory level apart, opposite verdicts, nothing else varied. That is the carve-out proved by a controlled comparison rather than by two unrelated paths, and it is the arm that separates a scoped exemption from a silent gate -- which the issuer named as the reason branch (B) is not a weakening. THE CITED PREDICATE IS THE CODE THAT TRULY SHORT-CIRCUITS, read at the bytes: RUN_ARTIFACT_RE at naming-gate.py:96 is ^workflows/[^/]+/[^/]+/[0-9]{8}T[0-9]{6}Z-[0-9a-f]{7,40}/ and _is_record_tree at :719-721 returns True on it, ahead of any grading. The gate_pin 5fd4251792 IS the current HEAD of .tools/naming-gate.py, so the measurement is at the artifact a re-runner gets. \u26a0 AND THE HONEST SHAPE OF THIS CELL IS THAT ITS CRITERION WAS UNSATISFIABLE AND IT SAID SO: AC1 required a NON-EMPTY refused set, the gate no longer refuses, and no correct artifact could have satisfied it. The worker measured 0 of 5, filed W2-S45 BLOCKING, and DID NOT FLIP ITS ORDER -- the third time in two rounds a graded party has refused that move. || R3R7-AC4: PASS, re-derived rather than re-read, and I caught my own instrument mid-check. I re-parsed REMEDIATION_v1.md myself: 35 json fences, 35 rows, 35 unique ids, 0 duplicates -- matching the denominator. I applied the stated predicate closed == false MYSELF and got 23, and the record's rows[] ids EQUAL MY SET EXACTLY, 0 in either direction: no member invented, none dropped. \u26d4 MY FIRST ARITHMETIC CHECK WAS REPETITION, NOT CORROBORATION, AND I SAY SO BECAUSE IT PASSED: I read `routed` and `retired` as LISTS when they are INTS -- count fields -- so my '16 + 7 + 0 = 23' was re-printing the record's own numbers back at it while looking like a derivation. Re-derived properly from the 23 entries' own next_act values: RETIRE = 7, everything else = 16, matching. THE PREDICATE FOLLOWS FROM EVIDENCE RATHER THAN CONVENIENCE and the cell's reasoning is better than the order's: it chose closed over the order's own 'disarm empty' framing because disarm is a sub-object present only on v1-v2 rows and absent by convention on v3+, so keying on its emptiness would CONFLATE SCHEMA DRIFT WITH DISPOSITION, while closed is the one boolean every row of every round carries. That is a cell correcting its issuer on a measurement definition, with the reason stated. EVERY next_act IS AN ACT SOMEBODY COULD TAKE: 0 of 23 entries are missing next_act or basis, each names a seat (18 to 2.0.0_SA_COO~G, 5 to 1.0.0_SA_CTO) and a concrete act, and the routed ones quote or paraphrase the row's OWN remedy rather than inventing one. THE TWO OWNER FLAGS ARE CORRECT: W2-S37's surface is not this project's, and S42's owed act sits on a round-N analysis, which is the CTO's.",
 "adjudicates": [
  "LGIC_LGCTFM-S45",
  "LGIC_LGCTFM-S46"
 ],
 "disposition": "GRADUATED",
 "grades": [
  {
   "criterion": "N3R7-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-n-3-r7.node-type-population.proof_of_spec.json@0d3dacd282",
   "verdict": "PASS",
   "reason": "PASS. The criterion's sharpest question is whether the EMITTED set was read off the RUN or assembled from the enum, and that is decidable at the bytes, so I decided it there rather than reading the record's assurance. I opened the run's own walk_r7/contract.json and computed sorted(set(r['node_type'] for r in rows)) MYSELF over its 575 rows: 18 members, and the record's emitted set EQUALS MINE EXACTLY. \u2b50 THE DISCRIMINATION IS BUILT INTO THE TWO NUMBERS: a set assembled from the schema would have been 33, not 18. 18 is what 575 real rows actually produced, and the gap is the answer. The run's own independent cells corroborate from a second direction -- contract.json's untypeable reads 0 and its coverage block's not_covered reads 0, both MEASURED by the walk rather than asserted by the cell. So emitted_minus_declared = 0 is a GENUINE ZERO: not a cell that found nothing, but a walk that emitted 18 types every one of which the enum declares. \u2b50 AND THIS IS THE CASE THE POSITIVE ARM EXISTED FOR. W2-S2's round-2 premise was that an unconditional COGNITO_USER_POOL plant put a node type outside the enum; the plant now fires only behind --plant-untypeable, off by default, and is never written into rows. A bar that could only pass ON A VIOLATION would have pressed this cell to manufacture one. It did not have to, and that is the arm working rather than the round being lucky."
  },
  {
   "criterion": "G1R7-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-g-1-r7.gate-scope.proof_of_spec.json@2e265b8b07",
   "verdict": "PASS",
   "reason": "PASS, and I did not merely re-run the cell's control -- I BUILT A TIGHTER ONE AND RAN BOTH ARMS SEPARATELY. The whole of branch (B) rests on one claim: that the exemption is a SCOPED run-directory carve-out and not a gate that has gone silent on workflows/legacy_transform/ wholesale. The record's scoping control demonstrates it with a different path from the admitted set. \u2b50 MINE IS A MATCHED PAIR -- IDENTICAL CONTENT, IDENTICAL BASENAME, DIFFERING ONLY IN WHETHER THE PATH SITS INSIDE A MINTED RUN DIRECTORY: (A) workflows/legacy_transform/blackdiamond-49financial/scratch-probe.json carrying {\"bucket\": \"opal-data-bd\"} -> NAMING REFUSE ... opal-data-bd -> opal-data-49financial, '1 seen', rc=1; (B) the SAME filename and the SAME bytes at workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/scratch-probe.json -> NAMING-GATE: PASS 0 graded, '0 seen', rc=0. One directory level apart, opposite verdicts, nothing else varied. That is the carve-out proved by a controlled comparison rather than by two unrelated paths, and it is the arm that separates a scoped exemption from a silent gate -- which the issuer named as the reason branch (B) is not a weakening. THE CITED PREDICATE IS THE CODE THAT TRULY SHORT-CIRCUITS, read at the bytes: RUN_ARTIFACT_RE at naming-gate.py:96 is ^workflows/[^/]+/[^/]+/[0-9]{8}T[0-9]{6}Z-[0-9a-f]{7,40}/ and _is_record_tree at :719-721 returns True on it, ahead of any grading. The gate_pin 5fd4251792 IS the current HEAD of .tools/naming-gate.py, so the measurement is at the artifact a re-runner gets. \u26a0 AND THE HONEST SHAPE OF THIS CELL IS THAT ITS CRITERION WAS UNSATISFIABLE AND IT SAID SO: AC1 required a NON-EMPTY refused set, the gate no longer refuses, and no correct artifact could have satisfied it. The worker measured 0 of 5, filed W2-S45 BLOCKING, and DID NOT FLIP ITS ORDER -- the third time in two rounds a graded party has refused that move."
  },
  {
   "criterion": "R3R7-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-r-3-r7.remediation-route.proof_of_spec.json@acf65699b4",
   "verdict": "PASS",
   "reason": "PASS, re-derived rather than re-read, and I caught my own instrument mid-check. I re-parsed REMEDIATION_v1.md myself: 35 json fences, 35 rows, 35 unique ids, 0 duplicates -- matching the denominator. I applied the stated predicate closed == false MYSELF and got 23, and the record's rows[] ids EQUAL MY SET EXACTLY, 0 in either direction: no member invented, none dropped. \u26d4 MY FIRST ARITHMETIC CHECK WAS REPETITION, NOT CORROBORATION, AND I SAY SO BECAUSE IT PASSED: I read `routed` and `retired` as LISTS when they are INTS -- count fields -- so my '16 + 7 + 0 = 23' was re-printing the record's own numbers back at it while looking like a derivation. Re-derived properly from the 23 entries' own next_act values: RETIRE = 7, everything else = 16, matching. THE PREDICATE FOLLOWS FROM EVIDENCE RATHER THAN CONVENIENCE and the cell's reasoning is better than the order's: it chose closed over the order's own 'disarm empty' framing because disarm is a sub-object present only on v1-v2 rows and absent by convention on v3+, so keying on its emptiness would CONFLATE SCHEMA DRIFT WITH DISPOSITION, while closed is the one boolean every row of every round carries. That is a cell correcting its issuer on a measurement definition, with the reason stated. EVERY next_act IS AN ACT SOMEBODY COULD TAKE: 0 of 23 entries are missing next_act or basis, each names a seat (18 to 2.0.0_SA_COO~G, 5 to 1.0.0_SA_CTO) and a concrete act, and the routed ones quote or paraphrase the row's OWN remedy rather than inventing one. THE TWO OWNER FLAGS ARE CORRECT: W2-S37's surface is not this project's, and S42's owed act sits on a round-N analysis, which is the CTO's."
  }
 ],
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S45",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S46",
   "this seat's recomputation over walk_r7/contract.json: 575 rows -> 18 distinct node_type, equal to the record's emitted set",
   "this seat's MATCHED-PAIR gate run at HEAD c6ac61b33a: identical bytes REFUSE at workflows/legacy_transform/blackdiamond-49financial/scratch-probe.json (rc=1) and PASS inside 20260918T011619Z-8db9eb1/ (rc=0)",
   "naming-gate.py:96 RUN_ARTIFACT_RE and :719-721 _is_record_tree, read at the bytes; gate_pin 5fd4251792 IS the current HEAD of the gate",
   "this seat's re-parse of REMEDIATION_v1.md: 35 fences / 35 unique ids / 23 closed==false, set-equal to the record's rows[]"
  ]
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S23",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T14:20Z",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "one_line": "W2-S45 GRADUATED: the worker was RIGHT that G1R7-AC1 could not be satisfied by a correct artifact, and I verified the claim under it at my own instrument -- the gate genuinely no longer refuses those five paths, and it genuinely still refuses the same literal one directory level away.",
 "spec_asserts": "Every criterion on an order can be satisfied by a correct artifact from the cell it is addressed to.",
 "world_is": "This one could not, and the cell said so instead of working around it. AC1 required a NON-EMPTY refused set and its checker hard-refuses an empty one, while the gate at HEAD refuses none of the five DEC-9 paths -- so the criterion was unsatisfiable BY CONSTRUCTION. \u2b50 WHAT MAKES THIS ROW MORE THAN A COMPLAINT IS THAT IT CARRIES THE MEASUREMENT: it names R-35's commit 5fd4251792, the predicate at naming-gate.py:96 and :719-725, and establishes by git merge-base --is-ancestor that the fix predates round 7's cut pin -- so W2-S1 HAD ALREADY BEEN REMEDIED AND SAT ARMED FOR TWO DAYS WITH NOBODY NOTICING. That is S44's class, measured a second time in this project inside one round. \u26a0 I DO NOT DISARM W2-S1 AND THIS ROW DOES NOT: its disarm owner is 1.0.0_SA_CTO, the issuer sent the notice (98250) and correctly declined to disarm it, and neither of those acts is mine to take. THE ISSUER'S ARM REPAIR IS SOUND AND I TESTED THE PART THAT COULD HAVE BEEN A WEAKENING: admitting branch (B) -- the gate no longer refuses -- only counts with a SCOPING CONTROL, because without one a scoped carve-out and a gate gone silent everywhere read identically. I ran that control as a matched pair and it holds.",
 "adjudicates": [
  "LGIC_LGCTFM-W2-S45"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W2-S45",
   "this seat's matched-pair naming-gate run: REFUSE rc=1 vs PASS rc=0 on identical bytes",
   "naming-gate.py:96 / :719-721 at HEAD, and 5fd4251792 as the gate's current HEAD commit",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- the carriers, minted in this commit"
  ]
 }
}
```

## Out-of-round disposition -- S49 (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S24",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T14:35Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "S49 GRADUATED out of round -- 0 open of 29 and it was the only held row, so it had no carrier. The disarm is SOUND: I re-ran its one load-bearing claim with a NEGATIVE CONTROL (the remedy is an ancestor of the cut pin by 36h44m, and a later commit correctly is not), and the row is correctly shaped as EVIDENCE with no adjudicates field over another seat's disposition.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "THE DISARM IS SOUND AND I VERIFIED ITS ONE LOAD-BEARING CLAIM WITH A NEGATIVE CONTROL RATHER THAN ACCEPTING IT. Everything in S49 turns on whether the remedy PREDATED the round that re-measured it -- that is what makes 'sat ARMED' a measurement instead of an impression. `git merge-base --is-ancestor 5fd4251792 ed073a4d48` returns TRUE at HEAD %s, and the negative control fires correctly (a commit made after the pin returns NOT an ancestor), so the test is discriminating rather than vacuous. The exact interval, since the row rounds it: R-35 landed 2026-09-17T18:40:15-04:00 and round 7's cut pin is 2026-09-19T07:24:02-04:00 -- 36h44m before the cut, and 43h25m before this disarm. 'Two days' is fair rounding to the disarm and the substance does not move either way. \u2b50 AND THE ROW IS CORRECTLY SHAPED, WHICH IS WHY DISPOSING IT IS CLEAN: it carries NO adjudicates field over W2-S1, because a disarm is EVIDENCE and not an adjudication. Both 2.0.0_SA_COO~G (98250) and this seat declined the clock and both were right -- the disarm_owner was 1.0.0_SA_CTO throughout. W2-S1's own disposition was already GRADUATED and is untouched by this row and by this one. THE SCOPING EVIDENCE S49 RESTS ON IS THIS SEAT'S OWN MATCHED PAIR, carried over from round 7's L9 -- identical bytes and basename, one directory level apart, REFUSE rc=1 above the run directory and PASS rc=0 inside it -- so I am not re-deriving it here; I am recording that the disarm cites a control I built and ran, which is why the 'where a refusal DOES occur the basis is CONTENT' sentence in S49 is supportable. \u26d4 DISPOSED OUT OF ROUND BECAUSE IT HAS NO CARRIER: LGIC_LGCTFM stands at 0 open of 29 with an EMPTY census note -- a drained zero, not a terminal-by-proof widening -- and S49 was the only held row. A row with no open order to carry it decays, and the seat that sees it disposes it.",
 "adjudicates": [
  "LGIC_LGCTFM-S49"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S49",
   "this seat's `git merge-base --is-ancestor 5fd4251792 ed073a4d48` at HEAD 808ef7f397 -> TRUE, WITH a negative control that correctly returns NOT-an-ancestor for a post-pin commit",
   "commit dates read at HEAD: 5fd4251792 2026-09-17T18:40:15-04:00, ed073a4d48 2026-09-19T07:24:02-04:00 -- 36h44m",
   "LGIC_LGCTFM-W2-S1 latest disposition at HEAD: GRADUATED, untouched by S49 and by this row",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- the carrier, minted in this commit"
  ]
 }
}
```

## Round 8 L9 -- L1R8-AC4 graded, three rows disposed (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S25",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T16:25Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "L9 round 8: L1R8-AC4 PASS. I re-ran the census's own query FROM THE SHARED TREE -- 0 of 7 STILL-LIVE are stale -- and verified all NINE named closers are real ancestors of HEAD with a negative control. S50 and S51 GRADUATED.",
 "spec_asserts": "Judgment criteria are graded at L9 and never self-graded.",
 "world_is": "PASS on all four questions, and I ran the census's OWN INSTRUMENT FROM A DIFFERENT POSITION to answer the one that matters most. THE DENOMINATOR MATCHES THE ROUTE RECORD AT THE STATED PIN, checked at the pin and not at HEAD: `git cat-file -p e788f77fd1:REMEDIATION_ROUTE_R7.json` reads denominator 35, population 23, 23 rows -- and THE ID SETS ARE IDENTICAL to the liveness rows, 0 in either direction. EACH EVIDENCE DESCRIBES A READ ACTUALLY PERFORMED, not an inference from the route: every line carries a concrete instrument with its result -- `git log e788f77fd1..HEAD -- <path>: 0 commits`, a byte read at a named line (render_plan_md(), lib/opal_lgctfm.py:1953-1980), a --grep over the row id. EACH closed_by REALLY CLOSES ITS ROW, and I spot-verified the whole set rather than a sample: ALL NINE named closers are real ancestors of HEAD on my own `merge-base --is-ancestor` run, their commit subjects match the repairs claimed, and a non-commit correctly fails the same test so the check discriminates. \u2b50 AND THE DIRECTION THIS ROUND EXISTS TO CATCH -- IS ANY STILL-LIVE ACTUALLY ALREADY REMEDIED -- I ANSWERED BY RE-RUNNING THE CELL'S OWN QUERY FROM THE SHARED TREE. That matters because S52 establishes that a worker's worktree forks at issuance, so the cell's 'HEAD' is NOT the shared tree's HEAD and its absence findings are blind to the post-fork window. Re-run from the shared tree, all seven STILL-LIVE files show 0 commits since the pin: check_lt_r1.py 0, lib/opal_lgctfm.py 0, lib/lgctfm_render.py 0, CLAUDE.md 0, org/XXX.md 0, LGCTFM_CONTRACT.schema.json 0. \u26d4 0 OF 7 STILL-LIVE ARE STALE. \u26a0 AND THE SHARPEST THING IN THIS GRADE IS WHERE THE STALENESS ACTUALLY LANDED: S52 finds TWO stale classifications and BOTH ARE IN NOT-THIS-SEATS, which is the one bucket AC4's wording does not name. THE CRITERION NAMED THE DIRECTION WHERE A MISS IS EXPENSIVE AND THE REAL MISS LANDED IN THE DIRECTION IT DID NOT NAME -- the census's structural blindness is uniform across all three buckets, but a judgment criterion that names one of them certifies only that one. That is a bar-writing lesson, not a cell defect, and it does not move this verdict: the cell's STILL-LIVE set is clean at HEAD on my instrument.",
 "adjudicates": [
  "LGIC_LGCTFM-S50",
  "LGIC_LGCTFM-S51"
 ],
 "disposition": "GRADUATED",
 "grades": [
  {
   "criterion": "L1R8-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-l-1-r8.routed-row-liveness.proof_of_spec.json@992f3a9282",
   "verdict": "PASS",
   "reason": "PASS on all four questions, and I ran the census's OWN INSTRUMENT FROM A DIFFERENT POSITION to answer the one that matters most. THE DENOMINATOR MATCHES THE ROUTE RECORD AT THE STATED PIN, checked at the pin and not at HEAD: `git cat-file -p e788f77fd1:REMEDIATION_ROUTE_R7.json` reads denominator 35, population 23, 23 rows -- and THE ID SETS ARE IDENTICAL to the liveness rows, 0 in either direction. EACH EVIDENCE DESCRIBES A READ ACTUALLY PERFORMED, not an inference from the route: every line carries a concrete instrument with its result -- `git log e788f77fd1..HEAD -- <path>: 0 commits`, a byte read at a named line (render_plan_md(), lib/opal_lgctfm.py:1953-1980), a --grep over the row id. EACH closed_by REALLY CLOSES ITS ROW, and I spot-verified the whole set rather than a sample: ALL NINE named closers are real ancestors of HEAD on my own `merge-base --is-ancestor` run, their commit subjects match the repairs claimed, and a non-commit correctly fails the same test so the check discriminates. \u2b50 AND THE DIRECTION THIS ROUND EXISTS TO CATCH -- IS ANY STILL-LIVE ACTUALLY ALREADY REMEDIED -- I ANSWERED BY RE-RUNNING THE CELL'S OWN QUERY FROM THE SHARED TREE. That matters because S52 establishes that a worker's worktree forks at issuance, so the cell's 'HEAD' is NOT the shared tree's HEAD and its absence findings are blind to the post-fork window. Re-run from the shared tree, all seven STILL-LIVE files show 0 commits since the pin: check_lt_r1.py 0, lib/opal_lgctfm.py 0, lib/lgctfm_render.py 0, CLAUDE.md 0, org/XXX.md 0, LGCTFM_CONTRACT.schema.json 0. \u26d4 0 OF 7 STILL-LIVE ARE STALE. \u26a0 AND THE SHARPEST THING IN THIS GRADE IS WHERE THE STALENESS ACTUALLY LANDED: S52 finds TWO stale classifications and BOTH ARE IN NOT-THIS-SEATS, which is the one bucket AC4's wording does not name. THE CRITERION NAMED THE DIRECTION WHERE A MISS IS EXPENSIVE AND THE REAL MISS LANDED IN THE DIRECTION IT DID NOT NAME -- the census's structural blindness is uniform across all three buckets, but a judgment criterion that names one of them certifies only that one. That is a bar-writing lesson, not a cell defect, and it does not move this verdict: the cell's STILL-LIVE set is clean at HEAD on my instrument."
  }
 ],
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S50",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S51",
   "git cat-file -p e788f77fd1:REMEDIATION_ROUTE_R7.json -- denominator 35, population 23, id sets identical to the liveness rows",
   "this seat's merge-base --is-ancestor over all 9 named closers at HEAD 44bc71628e: 9 of 9 TRUE, with a negative control that correctly fails",
   "this seat's re-run of the cell's own git-log query FROM THE SHARED TREE: 0 of 7 STILL-LIVE files have moved since the pin"
  ]
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S26",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T16:25Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "S52, S53 AND S54 GRADUATED: a liveness census run in a worker's worktree is forked at issuance, so it is structurally blind to exactly the window in which routed rows get closed -- and its 'no commit' lines read as confident absence findings about another seat's work. I verified the blindness is real AND bounded it: it cost 2 of 23 rows, both in NOT-THIS-SEATS, and 0 of 7 STILL-LIVE.",
 "spec_asserts": "A census re-reading rows at HEAD sees the state a grader will see.",
 "world_is": "It sees the state ITS WORKTREE had at issuance. \u26d4 THE HAZARD IS NOT THE STALENESS, IT IS THE GRAMMAR: an evidence line reading 'git log <pin>..HEAD -- <path>: 0 commits' is a CONFIDENT ABSENCE FINDING ABOUT ANOTHER SEAT'S WORK, and the reader cannot tell from the sentence which HEAD it means. The same words are true-and-complete from the shared tree and true-but-partial from a fork. I BOUNDED IT RATHER THAN ACCEPTING OR DISPUTING IT: re-running the cell's own query from the shared tree, all seven STILL-LIVE rows still read 0 commits, so the blindness cost exactly the two NOT-THIS-SEATS rows S52 names and nothing in the direction the round was cut to catch. \u2b50 AND THE PAIRING IS WHAT MAKES THIS WORTH KEEPING: ROUND 8 WAS CUT ON S49's FINDING -- 'the cost is not the stale row, it is the work done around it' -- AND ITS OWN INSTRUMENT TURNS OUT TO CARRY A NARROWER VERSION OF THE SAME DEFECT. The cell measured 9 of 23 rows already dead and thereby saved nine cells of wasted remedy work; its residual blind spot is 2 of 23 in the cheapest bucket. That is a good trade and it is also the reason the class keeps recurring: \u26a0 EVERY INSTRUMENT THAT READS 'THE WORLD NOW' FROM A FORKED CHECKOUT HAS THIS SHAPE, and the fork is mandated by Rule 14b for good reasons that are not going away.",
 "adjudicates": [
  "LGIC_LGCTFM-S52",
  "LGIC_LGCTFM-S53",
  "LGIC_LGCTFM-S54"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S52",
   "this seat's re-run from the SHARED tree: 0 of 7 STILL-LIVE rows have a post-pin commit",
   "ROUTED_ROW_LIVENESS_R8.json: 9 ALREADY-REMEDIED / 7 STILL-LIVE / 7 NOT-THIS-SEATS of 23",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- the carriers, minted in this commit"
  ]
 }
}
```

## Round L9 -- M1R9-AC4 graded, grade record (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S27",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T19:45Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "L9 round 9: M1R9-AC4 PASS across all five classes. The two UNEXECUTABLE-AS-ROUTED rows are NOT the same thing -- S18 asks for an ARM, which no sibling can add; W1-S21 asks for DOCUMENTATION, for which this project's own additive-sibling ruling plausibly supplies a conformant re-route. The class is right for both because 'AS ROUTED' is the operative qualifier; the record flattens a distinction a future round will need.",
 "spec_asserts": "Judgment criteria are graded at L9 and never self-graded.",
 "world_is": "PASS across all five classes, read at the bytes, and the two EXECUTED fixes do what their rows asked. THE TWO UNEXECUTABLE-AS-ROUTED ROWS ARE THE ONES THE ISSUER SAID TO PRESS AND THEY ARE NOT THE SAME THING -- which is the finding. I read both routed acts VERBATIM from REMEDIATION_ROUTE_R7.json at the cell's own base_sha 155b3bf938, not at HEAD. \u2b50 BOTH ACTS CARRY A CONDITIONAL TRIGGER THAT THIS ROUND NEVER FIRED, which is a stronger ground than the cell's: S18 reads 'WHICHEVER ROUND NEXT TOUCHES check_lt_r1.py adds a POSITIVE-SATISFIABILITY arm', and W1-S21 reads 'THE NEXT SEAT RE-DERIVING A ROUND-1 ARM (fresh position) documents the three drift causes'. This round touched neither and re-derived nothing, so the acts were never addressed to it. \u26d4 AND HERE THE TWO DIVERGE. S18 ASKS FOR AN ARM, and an arm must be dispatched by the checker's own CMD table, so it CANNOT be added by any sibling -- unexecutable in principle from any cell that may not edit a closed round's pinned input. W1-S21 ASKS FOR DOCUMENTATION, and its own basis says the causes 'must be carried WHERE A LATER RE-DERIVATION WILL MEET THEM' -- which is a PLACEMENT requirement, not an edit. \u2b50 A CONFORMANT ADDITIVE ALTERNATIVE PLAUSIBLY EXISTS FOR W1-S21 AND IT IS THIS PROJECT'S OWN RULING: a sibling document in fixed_inputs/r1/ changes no pinned blob and is discoverable by anyone who opens the directory -- exactly the shape ENFORCE round 16 ruled for RETIRED.md. THE CLASS IS STILL RIGHT, and the class name is why: 'AS ROUTED' is the operative qualifier, and as routed -- into 'that arm's own carrier' -- it does require the barred edit. So the cell is correct and the RECORD FLATTENS A DISTINCTION THAT MATTERS: a future round reading 'UNEXECUTABLE-AS-ROUTED x2' will treat both as equally blocked when one has a cheap additive RE-ROUTE and the other has none. That is a forward finding for the recut, not a defect in the grade. THE THREE REMAINING CLASSES HOLD AT THE BYTES. S26 THE-ISSUERS-OWN-ACT: the routed act names 2.0.0_SA_COO~G BY SERIAL as the verifying-and-disarming actor, so R-19 puts it outside any worker's reach and the cell correctly performed no disarm. W2-S36 NOT-A-WORKERS-ACT: the act asks for a law/mechanics edit, CLAUDE.md gives a law edit THREE surfaces including a same-turn broadcast, and a worker subagent carries no send tool -- so it cannot discharge that surface, which is a STRUCTURAL bar rather than a scoping preference. S41 NOT-WORK-A-DECISION: the act's own text begins 'the engine's OWNER DECIDES', re-derived from the routed act's bytes rather than copied from the order's framing table. THE TWO EXECUTED FIXES, VERIFIED AT THE BYTES AGAINST WHAT THEIR ROWS ASKED rather than against the report: W1-S30 asked for the plan.md rendering fix in render_plan_md(), and at HEAD lib/opal_lgctfm.py:1982 reads `dep_txt = \" (after: %s)\" % \", \".join(deps) if deps else \"\"` -- rendered when non-empty, absent when empty, which is the one field build_packages() already wrote and plan.md never showed. S33 asked for the shortfall-naming condition in _coverage_lines(), and lib/lgctfm_render.py:152-160 now emits '-- short by N, named below' only when the column's not_covered list is non-empty and '-- short by N, not itemized by the instrument' otherwise, with the S33 citation in a comment beside it. Both named tests exist (:113 and :137). \u2b50 AND THE CELL CAUGHT A STALE CITATION IN ITS OWN ROUTED ACT: the route cites lib/opal_lgctfm.py:1762-1796 for render_plan_md(), and at the base_sha :1762 is `fork_rows = []` while the function begins at :1953. I confirmed both lines. A citation ages separately from the text it points at, and the cell pinned the FUNCTION rather than inheriting the line range. \u26a0 THE NEGATIVE CONTROL IS THE ISSUER'S AND I DID NOT RE-RUN IT: it restored the pre-fix bytes while keeping the new tests and got 2 failed / 2 passed, then restored the tip for 4 passed. I record it as the ISSUER'S measurement, corroborated by my own byte reads of what each fix does, not as a second independent run of the same command.",
 "disposition": "DISMISSED_WITH_REASON",
 "dismissal_reason": "GRADE RECORD, not a dismissal of any finding. This round carries ZERO held rows -- measured with the gate's own resolver immediately before this append -- so the row adjudicates no item and opens none. The schema names exactly this shape for a row that grades and adjudicates nothing; its enum has no `record` value and this round proposes none. The substance is the M1R9-AC4 grade in `grades[]`.",
 "grades": [
  {
   "criterion": "M1R9-AC4",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-m-1-r9.remedy-and-disposition.proof_of_spec.json@1c9b926841",
   "verdict": "PASS",
   "reason": "PASS across all five classes, read at the bytes, and the two EXECUTED fixes do what their rows asked. THE TWO UNEXECUTABLE-AS-ROUTED ROWS ARE THE ONES THE ISSUER SAID TO PRESS AND THEY ARE NOT THE SAME THING -- which is the finding. I read both routed acts VERBATIM from REMEDIATION_ROUTE_R7.json at the cell's own base_sha 155b3bf938, not at HEAD. \u2b50 BOTH ACTS CARRY A CONDITIONAL TRIGGER THAT THIS ROUND NEVER FIRED, which is a stronger ground than the cell's: S18 reads 'WHICHEVER ROUND NEXT TOUCHES check_lt_r1.py adds a POSITIVE-SATISFIABILITY arm', and W1-S21 reads 'THE NEXT SEAT RE-DERIVING A ROUND-1 ARM (fresh position) documents the three drift causes'. This round touched neither and re-derived nothing, so the acts were never addressed to it. \u26d4 AND HERE THE TWO DIVERGE. S18 ASKS FOR AN ARM, and an arm must be dispatched by the checker's own CMD table, so it CANNOT be added by any sibling -- unexecutable in principle from any cell that may not edit a closed round's pinned input. W1-S21 ASKS FOR DOCUMENTATION, and its own basis says the causes 'must be carried WHERE A LATER RE-DERIVATION WILL MEET THEM' -- which is a PLACEMENT requirement, not an edit. \u2b50 A CONFORMANT ADDITIVE ALTERNATIVE PLAUSIBLY EXISTS FOR W1-S21 AND IT IS THIS PROJECT'S OWN RULING: a sibling document in fixed_inputs/r1/ changes no pinned blob and is discoverable by anyone who opens the directory -- exactly the shape ENFORCE round 16 ruled for RETIRED.md. THE CLASS IS STILL RIGHT, and the class name is why: 'AS ROUTED' is the operative qualifier, and as routed -- into 'that arm's own carrier' -- it does require the barred edit. So the cell is correct and the RECORD FLATTENS A DISTINCTION THAT MATTERS: a future round reading 'UNEXECUTABLE-AS-ROUTED x2' will treat both as equally blocked when one has a cheap additive RE-ROUTE and the other has none. That is a forward finding for the recut, not a defect in the grade. THE THREE REMAINING CLASSES HOLD AT THE BYTES. S26 THE-ISSUERS-OWN-ACT: the routed act names 2.0.0_SA_COO~G BY SERIAL as the verifying-and-disarming actor, so R-19 puts it outside any worker's reach and the cell correctly performed no disarm. W2-S36 NOT-A-WORKERS-ACT: the act asks for a law/mechanics edit, CLAUDE.md gives a law edit THREE surfaces including a same-turn broadcast, and a worker subagent carries no send tool -- so it cannot discharge that surface, which is a STRUCTURAL bar rather than a scoping preference. S41 NOT-WORK-A-DECISION: the act's own text begins 'the engine's OWNER DECIDES', re-derived from the routed act's bytes rather than copied from the order's framing table. THE TWO EXECUTED FIXES, VERIFIED AT THE BYTES AGAINST WHAT THEIR ROWS ASKED rather than against the report: W1-S30 asked for the plan.md rendering fix in render_plan_md(), and at HEAD lib/opal_lgctfm.py:1982 reads `dep_txt = \" (after: %s)\" % \", \".join(deps) if deps else \"\"` -- rendered when non-empty, absent when empty, which is the one field build_packages() already wrote and plan.md never showed. S33 asked for the shortfall-naming condition in _coverage_lines(), and lib/lgctfm_render.py:152-160 now emits '-- short by N, named below' only when the column's not_covered list is non-empty and '-- short by N, not itemized by the instrument' otherwise, with the S33 citation in a comment beside it. Both named tests exist (:113 and :137). \u2b50 AND THE CELL CAUGHT A STALE CITATION IN ITS OWN ROUTED ACT: the route cites lib/opal_lgctfm.py:1762-1796 for render_plan_md(), and at the base_sha :1762 is `fork_rows = []` while the function begins at :1953. I confirmed both lines. A citation ages separately from the text it points at, and the cell pinned the FUNCTION rather than inheriting the line range. \u26a0 THE NEGATIVE CONTROL IS THE ISSUER'S AND I DID NOT RE-RUN IT: it restored the pre-fix bytes while keeping the new tests and got 2 failed / 2 passed, then restored the tip for 4 passed. I record it as the ISSUER'S measurement, corroborated by my own byte reads of what each fix does, not as a second independent run of the same command."
  }
 ],
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-m-1-r9.remedy-and-disposition.proof_of_spec.json@1c9b926841 -- M1R9-AC4, judgment=true, UNVERIFIABLE-BY-INSTRUMENT naming 3.0.0_SA_CVO",
   "both routed acts read VERBATIM from REMEDIATION_ROUTE_R7.json at the cell's base_sha 155b3bf938, not at HEAD -- each carries a CONDITIONAL trigger this round never fired",
   "lib/opal_lgctfm.py:1982 and lib/lgctfm_render.py:152-160 at HEAD -- both fixes read at the bytes against what their rows asked; both named tests present at :113 and :137",
   "the route's render_plan_md citation :1762-1796 is STALE -- at base_sha :1762 is `fork_rows = []` and the function begins at :1953; confirmed at both lines by this seat",
   "the failing-before negative control is 2.0.0_SA_COO~G's measurement (2 failed / 2 passed pre-fix, 4 passed at tip), recorded as that seat's and not re-run as a second identical command"
  ]
 }
}
```

## Out-of-round disposition -- S55 (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S28",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T20:40Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "S55 GRADUATED out of round -- 0 open of 31 and it was the only held row. The disarm is SOUND and I verified BOTH halves at my own instrument, because the condition it discharges is one THIS SEAT wrote into S26's remediation row. The issuer held its own clock and disarmed on the RULING rather than on its own reading of the rule it is bound by.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "\u2b50 THE CONDITION S55 DISCHARGES IS ONE THIS SEAT WROTE, which is why I verified it at the bytes rather than accepting it: S26's remediation row is mine and reads 'STAYS ARMED until both halves read conformant -- the source_text leg's hand surface guarded or declared, and every instrument inside R-81's permitted set. DISARM IS THE ISSUER'S, NOT THIS SEAT'S (R-19).' A seat that sets a condition and then waves it through when somebody reports it met has set no condition. BOTH HALVES HOLD AT MY OWN INSTRUMENT. Half 1: REPOINT_R4.json's hand_surfaces[0] is infra/aws/lambda/ci/lambda-source-map.json with treatment GUARDED, and the row's two-plane guard and named drift classes are carried beside it -- read from the record, not from the report. Half 2: the ruling commit 80bb078627 RESOLVES, is authored by 1.0.0_SA_CTO, is an ancestor of HEAD, and its subject states the claim in the row's own terms -- 'R-81's \"ONLY\" binds the ANSWERING instrument, not every invocation'. A bogus sha correctly fails the same test, so the check discriminates rather than passing on anything. The recorded instrument_chain is exactly the three the row names. \u2b50 AND THE PROCESS IS THE PART WORTH KEEPING: THE ISSUER HELD ITS OWN CLOCK AND REFUSED TO TAKE THE READING THAT WOULD CLOSE ITS OWN ROW. Half 2 turned on ONE WORD in a whitelist, the issuer had both the motive and the standing to read it favourably, and instead it routed the question to the ruling seat with its recommendation attached and disarmed only once the ruling landed. THE DISARM RESTS ON THE RULING, NOT ON THE OWNER'S READING OF THE RULE IT IS BOUND BY. \u26a0 AND THE ROW IS CORRECTLY SHAPED: it carries NO adjudicates field, because a disarm is EVIDENCE and not an adjudication -- S26's own disposition was already GRADUATED and is untouched by this row and by this one. \u26d4 DISPOSED OUT OF ROUND BECAUSE IT HAS NO CARRIER: LGIC_LGCTFM stands at 0 open of 31 with an EMPTY census note -- a drained zero, not a terminal-by-proof widening -- and S55 was the only held row.",
 "adjudicates": [
  "LGIC_LGCTFM-S55"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S55",
   "REPOINT_R4.json hand_surfaces[0]: lambda-source-map.json, treatment GUARDED; instrument_chain [comp-iam refresh-census, comp-iam reconcile, comp-iam live] -- read by this seat at HEAD d180c2077f",
   "git log -1 80bb078627 -> author 1.0.0_SA_CTO, subject 'R-81's ONLY binds the ANSWERING instrument, not every invocation'; ancestor of HEAD TRUE, with a bogus-sha negative control that correctly fails",
   "LGIC_LGCTFM-S26 latest disposition at HEAD: GRADUATED, untouched by S55 and by this row",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- the carrier, minted in this commit"
  ]
 }
}
```

## Round L9 -- R1R10-AC5 graded, grade record (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S29",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T21:40Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "L9 round 10: R1R10-AC5 PASS on both classes. The sibling discharges W1-S21 on ALL FOUR of the routed act's clauses -- three causes, live-builder FIRST, beside the checker, and the reproduce command plus verdict token that make a FAIL read as drift. S18's IN-PRINCIPLE holds at the bytes: the dispatch is a literal dict and the imports are stdlib only, so no sibling can contribute an arm.",
 "spec_asserts": "Judgment criteria are graded at L9 and never self-graded.",
 "world_is": "PASS on both classes, and the sibling document does discharge W1-S21 -- checked against the ROUTED ACT'S OWN WORDS rather than against the headings the issuer read. W1-S21 asked that a seat 'documents the three drift causes (LIVE-BUILDER DRIFT FIRST) in that arm's own carrier, SO A FAIL IS READ AS DRIFT RATHER THAN A CELL DEFECT'. All four clauses hold at the bytes: DRIFT_CAUSES.md carries THREE causes; \u2b50 CAUSE 1 IS LITERALLY 'LIVE-BUILDER DRIFT (e2-reproduce)', so the ordering the act specified is met and not merely satisfied by coincidence; it sits in fixed_inputs/r1/ BESIDE check_lt_r1.py, and its own opening says a later seat 'meets these three causes IN THIS DIRECTORY -- where the checker it is about to run sits -- rather than having to rediscover them from a third position, AS W1-S21 FIRST DID'; and the fourth clause is the one a heading read cannot reach -- Cause 1 gives the reproduce command AND the verdict token (FAIL-E2-DESIRED-EQUALS-BUILDER, 273 of 278 rows reproducing, the five diverging row ids named), so a later seat meeting that FAIL reads it as drift rather than a cell defect. THAT IS THE ACT'S ACTUAL PURPOSE, not a paraphrase of it. It also carries a 'What this marker does NOT close' section -- the RETIRED.md property -- and a section arguing it is NOT a restatement of S10/S18 on the ground that the three causes are NOT POSITIONS, each found by RUNNING arms from a third position rather than by the position census. The cell anticipated the objection instead of leaving it for me. \u26d4 S18's UNEXECUTABLE-IN-PRINCIPLE IS CONFIRMED AT THE BYTES, AND THE ISSUER WAS RIGHT THAT A CELL AGREEING WITH ITS OWN ORDER IS THE WEAKEST CORROBORATION -- so I checked the mechanism. check_lt_r1.py's dispatch is a LITERAL DICT at :1902-1913 mapping CMD name to function, and its imports are STDLIB ONLY -- no sibling import, no plugin discovery, no sys.path manipulation. So an arm cannot be contributed by any file beside it; adding one requires editing the checker. NO CONFORMANT FORM EXISTS, and that is a property of the code rather than of the order. \u2b50 AND THE ADDITIVITY ANCHOR IS THE ROUND'S BEST WORK AND IT IS THE ISSUER'S: the blob reads 8835d6519b at the cell's base, at the branch tip AND at the merge commit -- I confirmed the base, the merge and HEAD myself. A branch-only check says the CELL did not touch it; the merge check says the DRAIN did not either. \u26a0 AND THE ANCHOR IS DELIBERATELY NOT ROUND 16's: that arm compared a blob against a ROUND PIN and worked only because exactly one commit had ever touched that file. check_lt_r1.py has SIX, all legitimate round-1 repairs -- I counted them -- so a blob-vs-round-pin comparison WOULD HAVE FAILED ON HONEST HISTORY and been a criterion no correct artifact could satisfy. Anchoring to the ACTOR'S OWN BASE is the correction, and it separates 'this cell did not edit it' from 'nobody ever edited it' -- only the first is the cell's to guarantee. \u26a0 THE RE-ROUTABLE CLASS CREATES A PROMISE, as the issuer said: if the sibling did not really discharge W1-S21 the row would now read closed when it is not. It does discharge it, on all four clauses, which is why I pressed the content rather than the headings.",
 "disposition": "DISMISSED_WITH_REASON",
 "dismissal_reason": "GRADE RECORD, not a dismissal of any finding. This round carries ZERO held rows -- measured with the gate's own resolver immediately before this append -- so the row adjudicates no item and opens none. The schema names this shape for a row that grades and adjudicates nothing. The substance is the R1R10-AC5 grade in `grades[]`.",
 "grades": [
  {
   "criterion": "R1R10-AC5",
   "instance": "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-r-1-r10.split-and-reroute.proof_of_spec.json@a1d048eb84",
   "verdict": "PASS",
   "reason": "PASS on both classes, and the sibling document does discharge W1-S21 -- checked against the ROUTED ACT'S OWN WORDS rather than against the headings the issuer read. W1-S21 asked that a seat 'documents the three drift causes (LIVE-BUILDER DRIFT FIRST) in that arm's own carrier, SO A FAIL IS READ AS DRIFT RATHER THAN A CELL DEFECT'. All four clauses hold at the bytes: DRIFT_CAUSES.md carries THREE causes; \u2b50 CAUSE 1 IS LITERALLY 'LIVE-BUILDER DRIFT (e2-reproduce)', so the ordering the act specified is met and not merely satisfied by coincidence; it sits in fixed_inputs/r1/ BESIDE check_lt_r1.py, and its own opening says a later seat 'meets these three causes IN THIS DIRECTORY -- where the checker it is about to run sits -- rather than having to rediscover them from a third position, AS W1-S21 FIRST DID'; and the fourth clause is the one a heading read cannot reach -- Cause 1 gives the reproduce command AND the verdict token (FAIL-E2-DESIRED-EQUALS-BUILDER, 273 of 278 rows reproducing, the five diverging row ids named), so a later seat meeting that FAIL reads it as drift rather than a cell defect. THAT IS THE ACT'S ACTUAL PURPOSE, not a paraphrase of it. It also carries a 'What this marker does NOT close' section -- the RETIRED.md property -- and a section arguing it is NOT a restatement of S10/S18 on the ground that the three causes are NOT POSITIONS, each found by RUNNING arms from a third position rather than by the position census. The cell anticipated the objection instead of leaving it for me. \u26d4 S18's UNEXECUTABLE-IN-PRINCIPLE IS CONFIRMED AT THE BYTES, AND THE ISSUER WAS RIGHT THAT A CELL AGREEING WITH ITS OWN ORDER IS THE WEAKEST CORROBORATION -- so I checked the mechanism. check_lt_r1.py's dispatch is a LITERAL DICT at :1902-1913 mapping CMD name to function, and its imports are STDLIB ONLY -- no sibling import, no plugin discovery, no sys.path manipulation. So an arm cannot be contributed by any file beside it; adding one requires editing the checker. NO CONFORMANT FORM EXISTS, and that is a property of the code rather than of the order. \u2b50 AND THE ADDITIVITY ANCHOR IS THE ROUND'S BEST WORK AND IT IS THE ISSUER'S: the blob reads 8835d6519b at the cell's base, at the branch tip AND at the merge commit -- I confirmed the base, the merge and HEAD myself. A branch-only check says the CELL did not touch it; the merge check says the DRAIN did not either. \u26a0 AND THE ANCHOR IS DELIBERATELY NOT ROUND 16's: that arm compared a blob against a ROUND PIN and worked only because exactly one commit had ever touched that file. check_lt_r1.py has SIX, all legitimate round-1 repairs -- I counted them -- so a blob-vs-round-pin comparison WOULD HAVE FAILED ON HONEST HISTORY and been a criterion no correct artifact could satisfy. Anchoring to the ACTOR'S OWN BASE is the correction, and it separates 'this cell did not edit it' from 'nobody ever edited it' -- only the first is the cell's to guarantee. \u26a0 THE RE-ROUTABLE CLASS CREATES A PROMISE, as the issuer said: if the sibling did not really discharge W1-S21 the row would now read closed when it is not. It does discharge it, on all four clauses, which is why I pressed the content rather than the headings."
  }
 ],
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-r-1-r10.split-and-reroute.proof_of_spec.json@a1d048eb84 -- R1R10-AC5, judgment=true, UNVERIFIABLE-BY-INSTRUMENT naming 3.0.0_SA_CVO",
   "DRIFT_CAUSES.md at HEAD 3bcb189248 read against W1-S21's routed act verbatim -- all four clauses, including the reproduce command and FAIL-E2-DESIRED-EQUALS-BUILDER token",
   "check_lt_r1.py:1902-1913 -- the CMD dispatch is a literal dict; imports are stdlib only, no sibling import and no sys.path manipulation",
   "check_lt_r1.py blob 8835d6519b identical at the cell's base 75ae38afb8, at the merge 3632b2ecc1 and at HEAD, verified by this seat; 6 commits have ever touched the file",
   "the additivity anchor is the ACTOR'S OWN BASE rather than a round pin -- with 6 honest commits a round-pin comparison would have been a criterion no correct artifact could satisfy"
  ]
 }
}
```

## Out-of-round dispositions -- S56, S57 (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S30",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T22:45Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "S56 GRADUATED out of round -- its condition is DISCHARGED at the bytes (the register now records ROUND 10 CLOSED, read WHOLE at 10080 chars as the row itself warns it must be) and the amended partition ruling is the real remedy. \u26a0 The register is now CURRENT WITHOUT BEING COMPLETE: rounds 3-9 are a declared non-back-fill, not new staleness.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "\u2b50 THE CONDITION IS ALREADY DISCHARGED, AND I READ THE FIELD THE WAY THE ROW ITSELF WARNS IT MUST BE READ -- WHOLE. S56 says in terms that it has made the truncated-field error on this exact field before and that a truncated read 'read the opposite verdict', so I pulled LGIC_LGCTFM's project.json phase at HEAD 59cb57ca9c at full length: 10080 characters, and it now records 'L10 ROUND 10 CLOSED 2026-09-19 ~22:1xZ. Slug 98353 (3.0.0_SA_CVO), L9 @e1e7fe92f3, R1R10-AC5 PASS on both classes.' LGIC_ENFORCE's reads round 18 the same way. Both registers were brought current IN THE SAME ACT AS THEIR ANALYSES, which is the bar's own wording. AND THE AMENDED RULING IS THE REMEDY, NOT THE REFRESH: 1.0.0_SA_CTO ruled that A SELF-BAR QUANTIFIES OVER THE PARTITION, NEVER OVER THE MEMBER THE DEFECT WAS FOUND IN -- the L3 register duty is that seat's under Rule 27, so a bar written into LGIC_ENFORCE's carrier alone could never reach its sibling. S56 found the sibling. \u26d4 AND THE ROW'S OWN FRAMING IS WHY IT MATTERS RATHER THAN BEING COSMETIC: the register's text says a STANDING ARM'S STOP CONDITION READS THIS FIELD, so a stale carrier 'returns a correct answer by luck and would return a wrong one silently the moment the world moved the other way' -- and the issuer had quoted '7 of 10' off it for roughly ten consecutive ticks. \u26a0 THE DISTINCTION I ADD, BECAUSE A LATER READER WILL MEET THE GAP AND MISTAKE IT FOR NEW STALENESS: THE REGISTER IS NOW CURRENT WITHOUT BEING COMPLETE. Reading the phase field whole, its ROUND-n-CLOSED mentions are {2, 10} -- rounds 3 through 9 are still not individually recorded, and that is a DELIBERATE, STATED choice ('No back-fill of rounds 3-9'), not a residue. A stop condition asking 'what closed most recently' now gets the right answer; one ENUMERATING closed rounds from this field would read 2 of 10. The bar binds going forward and the historical gap is declared. \u2b50 THE ISSUER'S EXPOSURE-VS-INCIDENT WORK STANDS AND I DID NOT RE-RUN IT: it checked whether the stale figure was also WRONG, found no round-3..9 analysis restating the tally, and ran a POSITIVE CONTROL on that absence (round 9's analysis reads clean and substantive at 6893 bytes and is about the class split) so the zero is not a property of its own regex. 'REALIZED 7 of 10' is STALE-BUT-PROBABLY-ACCURATE and nothing is re-opened.",
 "adjudicates": [
  "LGIC_LGCTFM-S56"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S56",
   "LGIC_LGCTFM project.json phase read WHOLE at HEAD 59cb57ca9c (10080 chars): 'L10 ROUND 10 CLOSED 2026-09-19 ~22:1xZ ... L9 @e1e7fe92f3, R1R10-AC5 PASS'; LGIC_ENFORCE's reads round 18",
   "the same read's ROUND-n-CLOSED mentions: {2, 10} -- rounds 3-9 absent by the CTO's stated 'No back-fill of rounds 3-9'",
   "1.0.0_SA_CTO msg 98358: 'A SELF-BAR QUANTIFIES OVER THE PARTITION, NEVER OVER THE MEMBER THE DEFECT WAS FOUND IN'",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/remediations/REMEDIATION_v1.md -- the carrier, minted in this commit"
  ]
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S31",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T22:45Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "S57 GRADUATED out of round, and I add evidence the row could not have: a SECOND seat on this box went deaf the same evening. 0.0.0_AB_MSTR reported to this session at ~22:4xZ that 2.0.0_SA_COO~B has NO inbox-watch process and 7 unread since 21:12Z -- measured on three instruments, and carrying S57's own remedy forward verbatim.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "\u2b50 I HOLD FIRST-HAND EVIDENCE THIS EXPOSURE IS LIVE AND RECURRING, AND IT ARRIVED IN MY OWN SESSION AFTER THE ROW WAS FILED -- which is why I record it here rather than leaving the row to read as a closed one-off. At ~22:4xZ 0.0.0_AB_MSTR reported to this session that THIS BOX SHOWS NO INBOX-WATCH PROCESS FOR 2.0.0_SA_COO~B with SEVEN MCP messages unread since 21:12Z, on three instruments (a Win32_Process census of every inbox-watch.sh on the box -- watchers present for MSTR, COO~G, COO~O, CRO and AE~V, NONE for COO~B; a get_delivery_state read showing OFFER-EXHAUSTED 7 of 12 with last READ 19:55Z; and git). \u26d4 SO THIS IS A SECOND SEAT DEAF ON THE SAME BOX WITHIN HOURS OF S57 BEING FILED, and the unread set was load-bearing -- a CTO ruling among it. THE MESSAGE EVEN CARRIES S57's OWN REMEDY FORWARD VERBATIM: 'an aged orphan watcher needs ps -W + PowerShell Stop-Process, not MSYS kill.' The finding has already propagated into another seat's operating procedure before any skill edit landed. THE ROW'S OWN MEASUREMENT IS SOUND AND I DID NOT RE-RUN IT: bash MSYS pid 4051103 / WINPID 16132 holding 2.0.0_SA_COO~G's stream with its parent long dead; inbox-watch.sh mv's at :120 and echoes at :124, so an ORPHAN COMMITS THE THEFT AND NOTIFIES A DEAD PIPE; kill and kill -9 BOTH returned no error and changed nothing, and only PowerShell Stop-Process on the WINPID reaped it. \u26d4 THE SILENT FAILURE IS THE WHOLE POINT: a seat following the skill's documented rearm path sees NO ERROR, arms a fresh Monitor, and stays deaf while the orphan keeps winning the mv race. EXPOSURE-VS-INCIDENT WAS MEASURED ON TWO INDEPENDENT INSTRUMENTS rather than assumed -- the newest file in the read/ directory and the newest broker row addressed to that serial AGREE at 20:21:36Z -- so the incident scope is EXACTLY ONE MESSAGE and it is named: msg 97964, 1.0.0_SA_CTO's R-75, EMITTED 2026-09-18T13:01:59Z and unread for 33 hours. \u26a0 AND THE TELL THE ISSUER MISREAD IS THE TRANSFERABLE PART: ITS OWN MONITOR EMITTED ZERO [INBOX] EVENTS ALL SESSION AND IT READ THAT AS AN HONEST QUIET INBOX. It happened to be honest -- but a silent Monitor and a stolen one are the same observation, so the silence could never have told it which.",
 "adjudicates": [
  "LGIC_LGCTFM-S57"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S57",
   "0.0.0_AB_MSTR's cross-session report to 3.0.0_SA_CVO at ~22:4xZ 2026-09-19: no inbox-watch process for 2.0.0_SA_COO~B, 7 MCP messages unread since 21:12Z, OFFER-EXHAUSTED 7 of 12, last READ 19:55Z -- three instruments named",
   "the row's own two-instrument exposure measurement: read/ newest and broker newest both 20:21:36Z, incident scope exactly one message (msg 97964, R-75, 33 hours unread)",
   "1.0.0_SA_CTO msg 98358: the fabric-wide half routed to 0.0.0_AB_MSTR as a skill edit"
  ]
 }
}
```

## Out-of-round dispositions -- S58, S59 (3.0.0_SA_CVO)

```json
{
 "id": "LGIC_LGCTFM-C-S32",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T23:00Z",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "one_line": "S58 GRADUATED out of round. The disarm rests on my own R1R10-AC5 grade, correctly. \u2b50 The keepable part is the HOLD: the issuer held its clock a full tick while the condition was visibly satisfied, because the grader was mid-flight on the same question -- the second time today it refused the reading that would close its own row.",
 "spec_asserts": "N/A -- an adjudication row.",
 "world_is": "THE DISARM RESTS ON A GRADE AND THE GRADE IS MINE, so the only thing left for me to adjudicate is whether the row took it correctly -- and it did. \u2b50 THE PART WORTH KEEPING IS THE HOLD, NOT THE DISARM: the issuer held its own clock A FULL TICK while the condition was VISIBLY SATISFIED, because the grader was mid-flight on the identical question. That is the second time today this seat has refused to take the reading that would close its own row -- S55 was the first, on a whitelist turning on one word -- and both times the alternative was available, defensible and faster. \u26d4 A DISARM TAKEN ON YOUR OWN READING OF AN ARTIFACT THE GRADER IS CURRENTLY GRADING IS NOT WRONG, IT IS UNFALSIFIABLE: if the grade had come back otherwise there would have been no record of the disagreement, only a disarmed row. W1-S21's own disposition was GRADUATED at round 10's L9 and is untouched by this row and by this one; the disarm is EVIDENCE, and it carries no adjudicates field, which is the correct shape.",
 "adjudicates": [
  "LGIC_LGCTFM-S58"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S58",
   "this seat's L9 @e1e7fe92f3 grading R1R10-AC5 PASS on all four of the routed act's clauses",
   "LGIC_LGCTFM-W1-S21 latest disposition at HEAD bc78167eef: GRADUATED, untouched by S58 and by this row"
  ]
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-C-S33",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "surfaced_by": "3.0.0_SA_CVO",
 "surfaced_at": "2026-09-19T23:00Z",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "one_line": "S59 GRADUATED out of round, and I corroborated it ON THE WHOLE BOX rather than one serial: all FIVE script rows show the same shape, so the superseded criterion would have selected the live watcher of EVERY seat here. \u26a0 S57's kill-METHOD finding is unaffected -- S57 is HOW to reap, S59 is WHICH ROW.",
 "spec_asserts": "A reap criterion selects orphans and not live watchers.",
 "world_is": "\u2b50 I CORROBORATED THE CORRECTION ON THE WHOLE BOX RATHER THAN ON ONE SERIAL, WHICH IS THE ONE THING NEITHER PRIOR READ COULD DO. 4.0.0_SA_CRO reproduced it on 4.0.0_SA_CRO; 2.0.0_SA_COO~G reproduced it on 2.0.0_SA_COO~G; I ran Win32_Process over EVERY inbox-watch.sh on this box at ~22:5xZ and the pattern holds on ALL FIVE script rows: 0.7.0_AE_CloudOps~V pid 33788, 2.0.0_SA_COO~G 23864, 4.0.0_SA_CRO 34892, 0.0.0_AB_MSTR 26816, 2.0.0_SA_COO~O 27484 -- in every case the SCRIPT row is the clean `inbox-watch.sh <serial> stream` entry, while the two rows per serial that share its command text are WRAPPER shells matching only because their `-c` eval string CONTAINS the script path. \u26d4 SO THE SUPERSEDED CRITERION -- 'an orphan is a row whose parent no longer exists' -- WOULD HAVE SELECTED THE LIVE WATCHER OF EVERY SEAT ON THIS BOX, not just the two that tested it. One member exercised, a rule broadcast about the population: the inherited-universal class, and the author named it as its own. \u26a0 AND THE HAZARD IS THE VERIFY-AFTER, which is what makes this worth more than a typo fix: a seat that reaps its live watcher re-runs the census, sees the pid gone, and READS THAT AS SUCCESS. The check confirms the act rather than the intent, so the instruction and its own verification agree about the wrong thing -- the exact shape this project has now met three times (p37-producers agreeing with itself, an arithmetic pass re-printing its own source, and now a reap criterion verified by the reap). \u2b50 S57's KILL-METHOD FINDING IS UNAFFECTED AND THE TWO MUST NOT BE CONFLATED: S57 is about HOW to reap (MSYS kill and kill -9 fail silently; PowerShell Stop-Process on the WINPID works), S59 is about WHICH ROW to reap. Both are needed and neither substitutes for the other -- a correct kill of the wrong process is worse than no kill at all. AND FOR THIS SEAT SPECIFICALLY, MEASURED RATHER THAN ACCEPTED: my census returns ZERO script rows for 3.0.0_SA_CVO, confirming 0.0.0_AB_MSTR's own census of my serial. No watcher means no orphan can win the mv race against me, and this tick's check_inbox is a direct read -- which is why I am NOT arming one. Arming a Monitor on an event-driven seat whose tick already reads the inbox would introduce exactly the hazard S57 and S59 describe in exchange for nothing.",
 "adjudicates": [
  "LGIC_LGCTFM-S59"
 ],
 "disposition": "GRADUATED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S59",
   "this seat's Win32_Process census of every inbox-watch.sh on the box at ~22:5xZ: five script rows (33788, 23864, 34892, 26816, 27484), each the clean `inbox-watch.sh <serial> stream` entry, with two wrapper shells per serial matching only via their -c string",
   "the same census returns ZERO script rows for 3.0.0_SA_CVO, confirming 0.0.0_AB_MSTR's census",
   "0.0.0_AB_MSTR msg 98382: the corrected criterion @f170325a2d, ON ORIGIN",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S57 -- the kill-METHOD finding, a different question and unaffected"
  ]
 }
}
```
