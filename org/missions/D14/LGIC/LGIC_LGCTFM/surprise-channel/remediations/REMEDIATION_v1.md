# LGIC_LGCTFM -- remediation slug v1 (pre-issuance intake)

Author: `3.0.0_SA_CVO`. Round: v1. Fabric: laptop. Recorded: 2026-09-16T17:55Z.

Input: `INVESTIGATION_v1.md` (1 row). Adjudication: `ADJUDICATION_v1.md` (C-S1), same slug.

ONE ROW PER GRADUATED ITEM: **1**. `LGIC_LGCTFM-S1` is born DISARMED on `2.0.0_SA_COO~G`'s evidence (R-14) with this seat writing (R-15), and REMEDIATED -- the three carriers now agree through one. Owner is the artifact's owner, never the CVO (R-22). `closed` is false: closing is the CTO's.

```json
[
 {
  "id": "LGIC_LGCTFM-S1",
  "project": "LGIC_LGCTFM",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The fork fixture's positive-control count was carried in three places that disagreed: PRD v1.1's T4 said FOUR (a forward list never checked against a denominator), the brief's IV.5 enumerated FIVE, and the fixture took the enumerating carrier. A criterion cut from T4 would have failed an engine that correctly returned the fixture's number.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S1",
   "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_LGCTFM-C-S1",
   "ISSUER'S EVIDENCE (R-14): org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/FORK_CONTROLS.json v1.1 @a71aa2d833 -- FORK-5 withdrawn on measurement with a positive control (planted twin -> exactly 1 pair; real names alone -> 0)",
   "1.0.0_SA_CTO R-24 @53654598b0 clause 3 and PRD v1.4 @459b4a736d -- T4 restated BY REFERENCE, making the fixture the one carrier"
  ],
  "remedy": "RESOLVED, and resolved in the durable form rather than the convenient one. The count went four (recall) -> five (the enumerating carrier) -> four (measurement) inside an hour, and only the last is a claim that could have gone the other way -- the planted-twin control is what makes the zero-pairs finding an absence rather than a broken predicate. The remedy that matters is not the number but T4 moving to BY-REFERENCE: a PRD cell that types a count carries a number it does not measure, and the next measurement re-opens a signed half. Now the fixture is the one carrier and the cell reads it, so no future measurement re-opens the brief. THIS SEAT'S RATIFIED-TEXT HALF IS UNAFFECTED and was verified, not assumed: ENDPOINT + CONTRACTS are byte-identical between the signed commit e996f463bb and v1.4 (13,324 bytes both). WHAT WOULD RE-ARM IT: any cell that types the fork count instead of reading FORK_CONTROLS.json.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-16T17:55Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO

## Round 1 -- remediation plane

```json
{
 "id": "LGIC_LGCTFM-S3",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "LT-x-1's RUN DIRECTORY IS A COMPOSITE OF TWO DIFFERENT RUNS AND NOTHING INSIDE IT SAYS SO. contract.json, plan.json, PLANT.json and PLANT_UNTYPEABLE.json under workflows/legacy_transform/blackdiamond-49financial/20260917T202556Z-bb29248/ were ADDED by a LATER CELL's commit (LT-e-4, a5fca30175) and are byte-identical to that amendment's OWN default-off run 20260917T233115Z-a89fd61, while the directory's VINTAGE.json still declares run_id 20260917T202556Z-bb29248 at repo_head bb292483994d4e2c379d671e6512313864c0363c. So X1R1-AC1 -- the criterion that reads 'the run directory is complete and its contract validates' -- now grades an artifact LT-x-1's own run did not produce, and it reads PASS. MARK.json, the fifth file the naming gate refused, was never committed at all and the worktree that held it is gone, so X1R1-AC2's evidence no longer exists anywhere and re-running x1-marks at HEAD reads FAIL-X1-MARK-ROWS-IN-THE-THREE-REGISTRIES.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S3",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S2"
 ],
 "remedy": "The remedy chosen on this row -- re-hand LT-x-1 to produce ONE COHERENT RUN rather than disclose a substituted one -- is DONE and verified by 3.0.0_SA_CVO: run 20260918T011619Z-8db9eb1 carries its own VINTAGE.json, all six run files, a contract validating with 0 schema errors, MARK.json committed for the first time, and an R-40 HASHES.json whose 8 declared hashes recompute with 0 mismatches under the manifest's own instrument. The 20:25Z composite is deliberately untouched and stays as the historical record.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T02:05Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S1",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "LT-e-2's OWN GRADED CRITERION E2R1-AC1 (check_lt_r1.py e2-reproduce) NOW FAILS ON A RE-RUN AGAINST THIS ROUND'S WALK OUTPUT, THOUGH NOTHING IN LT-e-2's CELL CHANGED. This round (LT-e-3) plants a third resource whose node_type fits no type in NAMING_SCHEMA.json's 33-type vocabulary at all (COGNITO_USER_POOL, WORKER FACE's own requirement), and lib/opal_lgctfm.py now returns desired.verdict = NOT_COVERED for it per 11_LGCTFM_CONTRACT_SCHEMA_RECORD.md s.3.1's six-value verdict enum. check_lt_r1.py's core_reproduce (built for e2-reproduce, LT-e-2's own arm) treats ANY raising builder call as correct ONLY when desired.verdict == 'RAISE' -- it has no branch for NOT_COVERED, a verdict this round's own WORKER FACE mints. Re-running e2-reproduce now: 'rows with a builder call the checker can make: 278; reproduced: 277' and 'VERDICT: FAIL-E2-DESIRED-EQUALS-BUILDER'.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S1",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S2"
 ],
 "remedy": "The issuer's fixed input was the defective party and was REPAIRED rather than the criterion waived: check_lt_r1.py's core_reproduce gained a NOT_COVERED branch, plus two arms (e2-not-covered, e2-not-covered-wrong-raise) giving the branch a positive AND a negative control. Verified by 3.0.0_SA_CVO running selftest-arms: both PASS, each with a real RED condition stated.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T02:05Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-W2-S1",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "DEC-9's MARK COMMIT AND THE ENGINE'S OWN RUN ARTIFACTS ARE NOT COMMITTABLE AT DEC-12's RUN HOME: .tools/naming-gate.py (ENFORCE mode) REFUSES contract.json, plan.json, PLANT.json, PLANT_UNTYPEABLE.json and MARK.json wholesale (1719 REFUSE + 49 RAISE lines on the first real run) because workflows/legacy_transform/ is covered by none of the gate's three exemptions, and the walk's own MEASURED current-state values are exactly the legacy tokens (opal-data-bd, 49financial, 49f, blackdiamond/49f/session-trigger-mode.json, ...) the gate's carrier rule refuses as a NEW hand-kept literal. Never exercised before this cell: every prior graded round wrote to org/missions/.../deliverables/, which IS exempt.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W2-S1",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S2"
 ],
 "remedy": "1.0.0_SA_CTO's own RULING R-35 @5fd4251792: an engine's MEASURED RUN OUTPUT is a RECORD, so the naming gate's record-tree subtraction now reaches a minted run DIRECTORY and deliberately not the engine-code tree above it. Verified by 3.0.0_SA_CVO on the gate's own function: _is_record_tree returns True for the run directory's contract.json and MARK.json, False for workflows/legacy_transform/run_home.py, with a registry path as a negative control reading False.",
 "owner": "1.0.0_SA_CTO",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "1.0.0_SA_CTO",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "1.0.0_SA_CTO",
  "at": "2026-09-18T02:05Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-W2-S2",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "EVERY WALK EMITS A ROW WHOSE node_type (COGNITO_USER_POOL) IS OUTSIDE org/standards/LGCTFM_CONTRACT.schema.json's 33-value node_type ENUM, SO NO REAL CONTRACT lib/opal_lgctfm.py PRODUCES CAN EVER VALIDATE AGAINST ITS OWN SCHEMA. The row is LT-e-3's own unconditional plant (cmd_walk() always injects name 'opal-blackdiamond-49financial-legacy-user-pool', node_type COGNITO_USER_POOL, PLANT_UNTYPEABLE.json), built to prove the walk returns an untypeable resource NOT_COVERED rather than dropping it silently -- but the schema's resource_or_plane_row.node_type enum (record s.1.1, 'the 33 node types BY SUBTRACTION from NAMING_SCHEMA.json') has no 34th 'untypeable' value, so the plant row fails 'row' oneOf, and this run's X1R1-AC1 (`check_lt_r1.py x1-run-dir`) reads FAIL on schema errors: 1 for exactly this reason.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W2-S2",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S2"
 ],
 "remedy": "RULING R-36 fixed it at the ROOT rather than by widening the vocabulary: the untypeable plant became OPT-IN behind --plant-untypeable, off by default, its carry counted in PLANT_UNTYPEABLE.json and printed even at zero, and the schema's 33-value node_type enum was NOT extended to admit COGNITO_USER_POOL. Verified by 3.0.0_SA_CVO: the graded run's contract validates with 0 schema errors over 184 rows, carries no COGNITO_USER_POOL row, and the enum still reads 33 values without it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T02:05Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-S6",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "ANDREW_CARD.md's RECOMMENDATION -- the one line a decision-maker actually weighs -- SAID 'the two rows touching a live, client-facing surface' AND THERE IS EXACTLY ONE. Measured over all 179 tensions of the contract the card ranks: client_facing == true is 1 (T-0001, the opal-data-bd bucket), live == true is 1 (T-0001), both together 1, irreversible == true is 0. The card's TABLE is correct and its own analysis sentence is correct ('Rank 1 is the only irreversible-or-client-facing-or-live row in the top ten'), so the RANKING and the 179-row order are not impeached -- what was wrong is the summary written FOR the reader who decides without checking, which is exactly backwards from how a card is used.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S6",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S3"
 ],
 "remedy": "Correct the RECOMMENDATION line so it matches the card's own table -- ONE row (T-0001) touches a live, client-facing surface, not two -- and get the correction to Andrew BESIDE the card rather than as a silent rewrite of a document already in his hands. If the intent was that T-0001 and T-0003 both concern opal-data-bd, say that instead: T-0003's own factors are client_facing false and live not-measurable, so as written against the rule's factors it is not a second such row.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T06:20Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-W2-S3",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "The re-hand's fresh walk (run 20260918T011619Z-8db9eb1) carries 13 current-name rows under `opal-data-bd/silver/`, and `infra/logic/06_CONFORMANCE_LEDGER.md:72` already carries a DECIDED disposition for that whole prefix -- MIGRATE -> `opal-data-assets/blackdiamond/49financial/silver/` (R4), LIVE -- exactly the same shape (a DECIDED MIGRATE the registry did not yet carry) as the `gold/` prefix the first hand marked in 53d59778a1. This worker APPENDED `{kind: s3-prefix, bucket: opal-data-bd, prefix: silver/}` to `infra/logic/registry/remediations.json`'s ADVI_FIRMBKTS surfaces this hand, beside disclosing the already-present `gold/` entry, both recorded in this run's MARK.json.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W2-S3",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S3"
 ],
 "remedy": "Decide whether DEC-9's accepted evidentiary shape for the gold/ prefix EXTENDS to a second DECIDED-but-unmarked prefix on the same bucket (opal-data-bd/silver/, 06_CONFORMANCE_LEDGER.md:72, MIGRATE under R4, 13 live rows surfaced by this run's own walk). The worker appended it to the marks input on the precedent; only DEC-9's owner can say whether the precedent reaches it.",
 "owner": "1.0.0_SA_CTO",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "1.0.0_SA_CTO",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "1.0.0_SA_CTO",
  "at": "2026-09-18T06:20Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-S10",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "TWO OF LT-x-1's OWN ARMS ARE BRANCH-RELATIVE AND READ FALSE FAIL FOR ANY SEAT THAT RE-RUNS THEM OFF THE WORKER'S CHECKOUT. x1-r16 and x1-footprint measure a branch against its own merge base, so on the shared tree they print FAIL with 'paths changed on this branch: 0' and 'commits touching the three registries: 0' -- artifacts of WHERE they ran, not findings.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S10",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S3"
 ],
 "remedy": "Make an arm whose verdict depends on the checkout PRINT that dependence, or resolve its base from the run's own recorded base rather than from the ambient branch, so a grader can tell a finding from a location. Two arms are affected (x1-r16, x1-footprint); the other twelve re-run clean off-branch and need nothing.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T06:20Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-S11",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "THREE NUMBERS IN THIS ROUND'S JUDGMENT RECORDS NAME NO RUN, AND TWO OF THEM DISAGREE WITH EACH OTHER. P1R1-AC6 cites plan.json's 1626 packages; X1R1-AC6 cites 'its atomic package plan (1074 packages)'. E3R1-AC6 grades 271 tensions and 1084 factor cells, and the contract at HEAD carries 179 tensions -- that population no longer exists anywhere.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S11",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S3"
 ],
 "remedy": "A number a judgment record cites carries the run it was measured on, and per R-40 that run's content hash. Three instances this round: P1R1-AC6's 1626 packages against X1R1-AC6's 1074 (which cannot both be true of one plan), and E3R1-AC6's 271 tensions / 1084 cells against a contract that now carries 179. No grade moves -- each was checkable at its own vintage -- and nothing is owed to the cells; what is owed is the convention.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T06:20Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-S12",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "ANDREW_CARD.md NAMES NO RUN AT ALL. A regex for a run id over the card returns ZERO matches: it identifies its own subject only as 'graph built 2026-09-17 18:16 UTC'. The card is with Andrew now, and the one thing pinning it away from a DIFFERENT run in the same subject directory is that its order happens to be 179 rows long.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S12",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S3"
 ],
 "remedy": "One line in ANDREW_CARD.md naming the run id it ranks and that run's contract content hash. It matters more than usual because the artifact is with a decision-maker now and FWD-4 will be graded against his answer to it -- an answer recorded against an unidentified subject is hard to re-bind later. Five run directories exist under the subject and one of them carries a different tension count.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T06:20Z"
 }
}
```

## Round 1 close-out -- remediation plane

```json
{
 "id": "LGIC_LGCTFM-S16",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "RESTATED REASON, THIS SEAT'S OWN WORD AS DISARM OWNER, for LGIC_LGCTFM-S12 -- NOT a disarm. The row's named remedy ('one line in ANDREW_CARD.md naming the run id it ranks and that run's contract content hash') IS NOT AVAILABLE TO THIS SEAT: .tools/owned-paths-validate.py clause 4 (ADHC_OWNPTH.004) refuses an issuer's edit inside a worker's deliverables folder, and this seat MEASURED that refusal on this exact file and reverted. So the reason moves, from 'a line in the card' to 'the run id and the contract's content hash delivered in this seat's own record BESIDE the card' -- and the row's premise moved a second time when 1.0.0_SA_CTO adjudicated the card @662d53b793, so the decision it feeds is now recorded against a named adjudication and not against an unidentified subject alone.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S16",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S7"
 ],
 "remedy": "PERFORMED. The remedy moved with the reason: the pin could not go into ANDREW_CARD.md (owned-paths clause 4 refuses an issuer's edit inside a worker's deliverables folder, measured and reverted), so it landed in the issuer's own record beside the card as CARD_SUBJECT_PIN.md @a4f61daeb0 -- run id, contract content hash, its instrument named, and a negative control over the other candidate run. Recorded performed by row S19 and verified at the file by this seat.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T06:20Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-S18",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "S10'S CLASS HAS FOUR MEMBERS, NOT TWO, AND THE TWO NOBODY NAMED FAIL SILENTLY. An UNSCOPED read of `base_ref()` over check_lt_r1.py finds 2 callers remaining after S10's repair -- x2-flag and x3-filed -- and re-run in the shared checkout they do NOT read FALSE FAIL, they read VACUOUS PASS. x2-flag prints \"commits on this branch touching org/mcp/naming-gate.enforce: ''\" and PASSES because the off-branch window is EMPTY, so it would pass IDENTICALLY had the cell touched the flag. x3-filed prints 'OPENED tensions 0; ADVI_FIRMBKTS channel rows added on this branch 0 []' and PASSES on 0 >= 0. A FALSE FAIL GETS INVESTIGATED; A VACUOUS PASS GETS ACCEPTED.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S18",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_LGCTFM-C-S7"
 ],
 "remedy": "Give x2-flag and x3-filed a POSITIVE-SATISFIABILITY arm -- the mirror of a mutant: show each can PASS for the right reason on a non-empty window, so an empty window is distinguishable from a satisfied one. NOT a repair of the round-1 inputs themselves: their windows were non-empty on their own branches, the grades they fed are sound, and editing a frozen graded input would move no grade while falsifying a record (R-43). The act belongs to whichever round next touches that checker.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v1",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

## Round 2 -- remediation plane

```json
{
 "id": "LGIC_LGCTFM-W1-S22",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE PUBLISHED REASON FOR THE TWO HASHES IS HALF THE CAUSE, AND THE RECIPE AS WRITTEN YIELDS A THIRD NUMBER. Four carriers explain the gap between git hash-object's 33204e29839de89af81fb293317cce3ccdf2266d and a plain sha1's 9c5cdb873f00a599bb00166831a91646fea97990 for one contract.json as 'git prefixes blob <len> and a NUL byte'. Measured on this checkout, the prefix ALONE returns d07bf29d245fd358fa15859b09a35aa8a3a2d5c3, which matches nothing published: git hash-object also applies the end-of-line filter first, so the published hash is the id of the COMMITTED (LF) bytes while the plain sha1 is over the CHECKOUT (CRLF) bytes. Every number in the record is correct; the stated MECHANISM is not, and the mechanism is the half a later seat re-derives from.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S22",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md round 2 disposition rows"
 ],
 "remedy": "REMEDIATED by the row's own disarm owner at ee4dbdf774: the live carrier now states the real cause -- git hash-object runs the EOL filter before the blob header, so the published id is of the COMMITTED bytes -- and the three frozen carriers stand under R-43. Verified by 3.0.0_SA_CVO: hash-object and rev-parse agree at 33204e29839d, plain sha1 reads 9c5cdb873f00, the prefix-only recipe yields d07bf29d245f which appears in no record, and 790871 - 24967 == 765904.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v2",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2"
 },
 "closed": true,
 "disarm": {
  "state": "DISARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": "2026-09-18T09:55Z"
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S21",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "ROUND 1's NON-RE-DERIVABLE POPULATION IS NOT ONLY THE CHECKOUT-DEPENDENT ARMS -- THREE FURTHER CAUSES, EACH MEASURED FROM A THIRD POSITION, AND NONE OF THEM IS A POSITION. (1) LIVE-BUILDER DRIFT: e2-reproduce, an arm of a CLOSED cell whose mechanical criteria graded PASS, reads FAIL-E2-DESIRED-EQUALS-BUILDER here -- 273 of 278 rows reproduce and 5 diverge because lib/opal_naming.py grade() now returns 'advi-inf-accounts-v2-daily' where the frozen contract holds '{system}-inf-accounts-v2-daily'. A static census of the checker cannot see this: the moving part is the LIBRARY the arm imports, not the checkout it runs in. (2) A PIN WHOSE PATH PREDATES THE FILE: S2R1-AC8's evidence compares two tools against org/standards/LGCTFM_CONTRACT.schema.json@ef8197ed07, and that path does not exist in that commit -- ef8197ed07 is round 1's L6 ISSUANCE and the schema was added 24 minutes later by a DIFFERENT cell. (3) A QUOTED MEASUREMENT THAT WENT STALE INSIDE ITS OWN CELL: E2R1-AC5's evidence states 'grep of lib/opal_lgctfm.py for the literal string FORK_CONTROLS returns 0 hits'; the string entered that file in the CELL'S OWN BUILD COMMIT f73efe6113, 3m40s before its own proof commit, so the stated result was already false when it was written and no seat at any vintage from that commit forward",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S21",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/adjudications/ADJUDICATION_v1.md round 2 disposition rows"
 ],
 "remedy": "Not a repair of round 1's fixed inputs -- R-43 scopes a frozen-history defect to one live-direction document and the order refused the edit. What is owed is that the three further causes are carried where a later seat re-deriving a round-1 arm will meet them, so a FAIL from a fresh position is read as drift rather than as a defect in the cell. LIVE-BUILDER DRIFT is the one to state first: an arm can pass at its cut and fail later with nothing about the cell changed, because its subject is a builder that keeps moving.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v2",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

## Round 3 L9 -- one remediation row per GRADUATED item

```json
{
 "id": "LGIC_LGCTFM-S21",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A LIVE EventBridge rule can be ENABLED and DEAD at the same time when a backstop schedule fires the same target: opal-data-inf/gold/meta/pipeline-complete.json was last written 2026-09-05T12:52:20Z while gold/meta/pipeline-failed.json is written daily, so mdpf-feeder-accelerator (ENABLED, pattern on that key, target mdpf-feeder-trigger) has not fired for 13 days and nothing said so -- the Scheduler backstop mdpf-feeder-backstop-daily fires the same Lambda at 12:52Z and the Lambda's own pre-check reads the per-date sentinel instead.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S21",
  "4.0.0_SA_CRO's RCN-0010 s.2.1 and the brief's IV.3 -- the corrected reading of the binding dependency"
 ],
 "remedy": "ROUTE IT, DO NOT FIX IT FROM HERE. This is a live-estate finding belonging to no LGIC round and to no seat that saw it, which is exactly the shape that decays: the CRO filed it off-task, LGCTFM has no write on the MDPF or INF pipelines, and the standing moratorium forbids building a monitor for it. What is owed is a ROUTING decision by 1.0.0_SA_CTO -- whose finding the daily failed marker is, whether it is already known, and which project owns it -- and that decision closes this row. The row explicitly does NOT ask for an alert, a checker or a comparator.",
 "owner": "1.0.0_SA_CTO",
 "round": "v3",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v3"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S26",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "mechanism": "A RULING THAT ARRIVES AFTER AN ISSUANCE BINDS THE NEXT ROUND, NEVER THE FROZEN ONE: R-81 landed @4443e7308e, 25 minutes after round 3's issuance @6139990fe7 and after LT-e-5's worker was spawned. The round is frozen and a worker cannot be messaged, so the face stood as issued and this row carried R-81 to the drain. Its drain test (S30) read NON-CONFORMANT on BOTH halves -- one leg reads a Terraform-plane comp-iam subcommand outside R-81's permitted set, and lambda-source-map.json is neither comp-lambdamap-guarded nor DECLARED with date, owner and un-defer condition.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S26",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S30 -- the drain test, NON-CONFORMANT on both halves",
  "LGIC_LGCTFM.TO-LT-x-4-r3.coverage-run.md -- superseded, never spawned, reason on its own face"
 ],
 "remedy": "The conformance repair leads round 4 beside R-81's canonical manifest entry, and LT-x-4 is re-cut there. STAYS ARMED until both halves read conformant: the source_text leg's hand surface guarded or declared, and every instrument inside R-81's permitted set. The cell is not at fault and the row says so -- it could not have been built against a ruling that did not exist when it was dispatched. DISARM IS THE ISSUER'S, NOT THIS SEAT'S (R-19).",
 "owner": "2.0.0_SA_COO~G",
 "round": "v3",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v3"
 },
 "closed": false,
 "disarm": {
  "state": "ARMED",
  "owner": "2.0.0_SA_COO~G",
  "at": null
 }
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S24",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "comp-trigger CARRIES NO TARGETS IN ITS LIST MODE AND NO PATH AT ALL FOR SCHEDULER SCHEDULES. Measured on the tool's own JSON: 167 entries (144 rules + 23 schedules), key-set Counter {(arn, kind, name, pattern, schedule, state): 167}. Targets come only from QUERY mode and only for kind == events-rule (match_triggers, org/modules/graph/comp_trigger.py:350-367), each query paying list-targets-by-rule across all 144 rules at about 110 seconds. So 23 of 167 triggers have targets no comp-trigger path can read.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S24",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S27 -- the issuer's independent measurement of the same fact",
  "4.0.0_SA_CRO's RCN-0010 @ecf57e8806 -- the first surfacing"
 ],
 "remedy": "NOTHING IS BLOCKED AND THIS ROW DOES NOT ASK FOR A BUILD. The walk covered schedules through comp-kuzu TRIGGERS/EMITS_TO, so LGCTFM needs nothing. What is owed is that the comp-tool surface's owner decides whether comp-trigger should answer for Scheduler schedules at all, and that the answer is written where the next order that reaches for the tool will meet it -- the reason this row exists is that TWO separate parties wrote orders on the premise that --list carries targets.",
 "owner": "1.0.0_SA_CTO",
 "round": "v3",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v3"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S25",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE COMMIT GATE'S MANIFEST-ADVISORY READS A STRING'S PRESENCE, NOT ITS ROUTE: it flagged lib/opal_lgctfm.py:772 and :788 as 'embeds raw Cypher outside comp-kuzu ... Route graph queries through comp-kuzu' when both queries are argv handed TO .tools/comp-kuzu by kuzu_rows() -- exactly the route the advisory demands. The gate printed '2 graph-access finding(s) (2 would block in blocking mode). Advisory -- not blocking.' and rc 0.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S25",
  "lib/opal_lgctfm.py@b736ee4fdf discover_involved() -- kuzu_rows() -> _bash_tool(COMP_KUZU, [query, --json, ...])"
 ],
 "remedy": "A CONFORMANT CALLER WOULD BE REFUSED THE DAY THE ADVISORY BECOMES BLOCKING, and the gate itself says so in its own output -- which is the whole reason this is worth carrying rather than shrugging at. What is owed, from the gate's owner: either the detector distinguishes a Cypher string PASSED to comp-kuzu from one executed beside it, or the blocking-mode promise is withdrawn. No edit to lib/opal_lgctfm.py is owed -- the file is already conformant.",
 "owner": "1.0.0_SA_CTO",
 "round": "v3",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v3"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S30",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE MACHINE ARTIFACT GAINED THE STEP RELATION AND THE HUMAN ONE STILL HAS NONE. The rename landed in 2 of the 3 sites the order named; the third, render_plan_md(), has NEVER printed the field under either spelling -- its only per-package line is package_id, the never-widen flag and objective (lib/opal_lgctfm.py:1762-1796 @f08295cc8f). So plan.json now carries step_dependencies and plan.md shows a package list with no ordering information at all.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S30",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.14 -- the disarm owner's word that the order-defect half needs no act",
  "org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md FWD-6 and row T6 -- plan.json and plan.md are both FWD-6's artifacts"
 ],
 "remedy": "THE ORDER-DEFECT HALF NEEDS NO ACT AND IS NOT WHAT THIS ROW CARRIES -- the cell renamed the two sites that existed and refused to invent the third, which is the right behaviour and is why the gap is visible at all. What is owed is the RENDERING half, and it belongs to FWD-6 (T6, 'the migration's work plan comes out of the run, in the order the canon requires') in a round, never as a rider on unrelated work: plan.md should render each package's step relation now that plan.json carries it. Cost is one line in render_plan_md(); the reason it is a row and not a fix is that nobody's <paths> grant covered it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v3",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v3"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S32",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A PINNED PROOF IS NOT RE-GRADED WHEN A FIXED INPUT MOVES UNDER IT. LT-e-5's instance records E5R3-AC4 FAIL at b736ee4fdf (16:27:12 -0400); the issuer repaired check_lt_r3.py at fd02b24c51 (17:09:25 -0400), 42 minutes later, for its own row S29; the same arm reads PASS-E5-SCHEMA rc 0 at HEAD. Both readings are correct at their own vintage, and no gate, notifier or limb closes the gap between them.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S32",
  "3.0.0_SA_CVO's own run of check_lt_r3.py e5-schema at HEAD 7f48a0ff42"
 ],
 "remedy": "NO ARTIFACT CHANGES AND NO PROOF IS REWRITTEN -- a pinned proof is a record of a vintage and rewriting it would be the worse defect. What is owed is one sentence in round 4's issuance stating that E5R3-AC4 reads PASS at HEAD on the repaired checker, so the next reader of the instance is not left with a FAIL the estate has already answered. The transferable half, which is why this is a row rather than a footnote: WHEN AN ISSUER REPAIRS A FIXED INPUT MID-ROUND, THE PROOFS ALREADY PINNED AGAINST IT ARE STALE AND NOTHING SAYS SO -- the only instrument that catches it is re-running the arm at L9, which is not required by any limb today.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v3",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v3"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S33",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "_coverage_lines() emits 'short by N, named below' on the sole condition involved > rows, while the 'not covered' lines it points at are emitted per not_covered entry -- so a node_type that is short and carries no not_covered entries renders a promise with nothing after it.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S33",
  "lib/lgctfm_render.py@d701235a50 _coverage_lines",
  "3.0.0_SA_CVO's direct call of _coverage_lines() at HEAD on a synthetic short block"
 ],
 "remedy": "UNREACHABLE TODAY AND THE ROW SAYS SO FIRST: 0 of 19 node_types on the one live coverage block can enter the branch, because all 19 have rows == involved. It becomes reachable the first time a walk reports a shortfall it cannot name -- which is precisely the case the coverage block exists for. The fix is one condition (name the shortfall, or say it cannot be named) on LT-r-2's own surface, and it belongs in the round that next opens lib/lgctfm_render.py, never as a rider. R2R3-AC4 is PASS with or without it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v3",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v3"
 },
 "closed": false
}
```

## Round 3 L10 -- carrier for LGIC_LGCTFM-S34

```json
{
 "id": "LGIC_LGCTFM-S34",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A FILE-LEVEL TRIGGER STANDS IN FOR AN ARM-LEVEL QUESTION IT CANNOT ANSWER. 'git log --since=<round cut> -- <fixed-input path>' fires whenever the round's checker was touched, and on this estate the issuer keeps committing to the round's checker while workers pin proofs -- adding the later cells' arms, repairing one cell's route, draining. Measured: 63 of 112 evaluable proofs carry the signature; check_lt_r1.py grew 61 -> 67 subcommand keys across 6 commits with 0 removed, while 3 of those 6 changed lines without changing keys. Additive commits cannot move an earlier arm; edits to shared code can; the file's history cannot tell them apart.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S34",
  "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/1.0.0_SA_CTO/LGIC_LGCTFM_ROUND3_ANALYSIS.md@ba1dcf65e9",
  "3.0.0_SA_CVO's sweep at HEAD: 163 tracked instances, 112 evaluable, 63 hits, 0 subtracted by the round-match axis"
 ],
 "remedy": "THE BAR STANDS AND IS NOT WEAKENED BY THIS ROW -- what is owed is a PRICE, decided by the bar's author before round 4 carries it. The measurement says the trigger fires on the majority case, so the choice is explicit rather than incidental: either round 4 pays 63-ish arm re-runs as a known cost and says so, or the trigger selects the arms a commit can actually move rather than every arm in a touched file. NOTHING IS REWRITTEN AND NO PROOF IS RE-CUT; this row changes no verdict and re-opens no round. I do NOT propose the narrower trigger's mechanism, because a trigger is an enforcement surface and designing one from this seat would be an agent-made gate; the owner is named because the bar is the owner's.",
 "owner": "1.0.0_SA_CTO",
 "round": "v3",
 "remediation": {
  "state": "REMEDIATED",
  "owner": "1.0.0_SA_CTO",
  "round": "v3"
 },
 "closed": true
}
```

## Round 4 L9 -- one remediation row per GRADUATED item

```json
{
 "id": "LGIC_LGCTFM-W2-S35",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "AN ARM DEMANDED A VOCABULARY THE SUBJECT HAS NEVER ADMITTED: m1-entry required status in (active|current|live) while graph-call-manifest.yaml's own schema admits canonical|deprecated|planned|retired and 125 of its 128 pre-existing entries read 'canonical'. The intersection was ZERO of 127, so no correct entry could pass and the cheapest green was to write a status the manifest forbids.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W2-S35",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "Repaired at 1d4df2c115 to take the manifest's OWN vocabulary, and the entry now reads PASS at the merged tree. What is owed forward is the class, not the fix: AN ARM THAT GRADES A VALUE AGAINST A VOCABULARY IT INVENTED RATHER THAN AGAINST THE SUBJECT'S OWN IS UNSATISFIABLE BY CONSTRUCTION, and the tell is cheap -- intersect the arm's accepted set with the subject's admitted set before the cut and print both denominators.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W2-S36",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A MID-ROUND FIXED-INPUT REPAIR CANNOT REACH A LIVE WORKER'S WORKTREE, AND THE ARM IT REPAIRS MEASURES THAT WORKTREE. The issuer repaired r4-stale-proofs at 1df2481ca0, which is not an ancestor of the worker's branch, so the in-tree checker FAILED the honest record while the repaired bytes PASSED it on the same tree.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W2-S36",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "This is STRUCTURAL and is not anyone's defect -- it is the cost of repairing a fixed input while workers are live, and it is the other half of the S32 bar the estate has been building all night. What is owed is that a mid-round fixed-input repair is ANNOUNCED to the live workers with the instruction to re-run from the merged tree rather than their own, which the issuer did here by message; making that the standing shape rather than this round's good judgment is the remedy. \u26d4 NOT a proposal to stop repairing fixed inputs mid-round: the alternative is leaving an unsatisfiable arm in front of a worker.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W2-S37",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE RULE-BANK TWO-PHASE OVERRIDE IS UNDISCHARGEABLE BY A WORKER: committing one manifest entry trips comp-system's STALE-source block, whose own text names an audited override line as the legal path AND requires it to be discharged in-session by a recompile commit -- which is outside a worker's grant.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W2-S37",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "A gate whose only legal path requires an act the graded party cannot perform is the same class as the four arms above, one level out: the worker cannot comply and cannot refuse. What is owed is a routing decision -- either the recompile is part of the issuing seat's drain, or the block admits a worker-shaped discharge. The row does not choose; the surface is not this project's.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S35",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "core_sources() WAS A BARE SUBSTRING SEARCH OVER THE WHOLE METHOD NOTE, so it could not tell a tool NAMED AS A SOURCE from one NAMED AS NOT USED -- and all three residual hits were rows of the 78-row COMP-TOOL LEDGER whose verdict column literally reads NOT USED. The cheapest passing move was to DELETE AN ANDREW-DIRECT ARTIFACT.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S35",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "Repaired at 21a163f492 to read the DESIGN half of the method note only. The class is the sharpest of the four and worth stating once: A SUBSTRING SEARCH CANNOT READ A NEGATION, so an arm built on one grades the presence of a word and never the claim -- and when the word appears in a truthful disclosure, the arm pays the record for being honest. The worker refusing to delete the ledger and filing BLOCKING instead is the behaviour the order asked for and got.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S36",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "LGCTFM_CONTRACT.schema.json's $defs.coverage is CLOSED (additionalProperties false, exactly five keys), so a contract carrying R-81's hand-surface guard output inside its coverage block reads HAND BACK from the estate's own router. The guard therefore rides in a sidecar.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S36",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "A ROUTED ITEM, NOT A ROUND-4 DEFECT, and the row is right to say so -- the schema is outside every cell's grant. What is owed is the owner's decision on whether the coverage block admits the guard's output or the sidecar becomes the declared shape; until then the guard's output is real and is simply not inside the artifact the router validates. Owner is the CTO because the schema is an estate surface.",
 "owner": "1.0.0_SA_CTO",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S37",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE ORDER'S ARM COUNT IS A MOVING NUMBER, NOT A CONSTANT: the face names '21 arms, 8 positive-satisfiability' and selftest-arms drove 24 and 8, because four arms are minted per round-4 order rather than fixed.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S37",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "Identical to LGIC_ENFORCE-W1-S89 one project over, and the remedy is the same and already taken forward there: STOP QUOTING A DERIVED TOTAL IN AN ORDER -- the run prints its own. A number an order quotes about its own instrument is a SECOND carrier of a fact the instrument already reports, and a second carrier goes stale silently. Pin the verdict token and the properties that must hold (8 positive-satisfiability arms), never the cardinality of a set the run computes.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S38",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A PER-WORKTREE MEASUREMENT FED A SHARED EQUALITY BAR: core_stale() required the record's fixed_input_commits_since_cut to EQUAL a count re-measured live, but the worker measures it against ITS OWN branch, which does not carry the issuer's mid-round repair commit -- so an honest record goes stale at the drain through no act of the worker's.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S38",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "Repaired at 21a163f492: the count became informational and the SET of at-risk proofs became the bar. The class to carry forward is that A BAR KEYED ON A COUNT TAKEN IN A DIFFERENT CHECKOUT IS NOT A BAR ON THE RECORD, IT IS A BAR ON WHERE THE RECORD WAS WRITTEN -- and a set that is stable across checkouts is the right shape, which is what the repair chose.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W1-S39",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "x4-no-registry-move DIFFED THE WHOLE TREE, so an unrelated project's commit (845343f925, IRPT_BCKEND steps 2-3 by 4.0.0_SA_CRO, touching exemptions.json and scopes.json) FAILED this cell AT THE WORKER'S OWN HEAD, BEFORE ANY ACT OF THE WORKER'S. The cheapest passing move would have been to REVERT ANOTHER PROJECT'S WORK.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W1-S39",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "Repaired at d08be0b693 to grade the cell's own write surface. \u2b50 THIS IS THE WORST OF THE FOUR AND THE ONLY ONE WHOSE CHEAPEST GREEN COSTS A SEAT THAT IS NOT IN THE ROUND -- an arm scoped to the tree makes every other seat's concurrent work a source of failure for a cell that never touched it, and on a shared branch with five live seats that is not a rare case. The standing shape: AN ARM'S DIFF SCOPE IS THE CELL'S GRANT, never the tree, and the grant is already written in the order's own <paths>.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S35",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE ROUND-4 STALE-PROOF ARM COUNTED ITS OWN MINT AND PRICED THE HONEST ANSWER OUT: the window opens at the ANALYSIS pin, the commit CREATING the fixed-input directory lands after it, so git log returns 1 -- and the old rule demanded len(proofs_re_run) > 0 where the honest list is EMPTY, because no round-4 proof existed before the input did.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S35",
  "org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md s.15.4 -- the round-4 close"
 ],
 "remedy": "Repaired at 1df2481ca0 to SET EQUALITY against the proofs that existed at the parent of the earliest counted commit, with the two residuals the CTO's round-11 analysis named closed at eda1e967d0 -- the empty-set-on-instrument-failure and the unsorted per-path concatenation, the first with a LIVE positive control that hands the real function a bogus commit-ish and requires it to raise. THAT POSITIVE CONTROL IS THE PART WORTH KEEPING: it is the difference between a repair that is believed and one that is exercised. Nothing further is owed in this project; the sibling carrier in LGIC_ENFORCE is tracked by that project's own S90.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S41",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE CONTRACT NAMES THE FOUR CATEGORIES FWD-1's ACCEPT ASKS FOR AND CANNOT PLACE 24 OF ITS OWN KEYS: 24 of 154 S3Key rows carry a path with no bucket component (12 platinum/, 10 gold/, 1 silver/, 1 with a malformed single-colon 's3:' scheme), and the bucket appears in no other field of those rows -- arn_or_path, name and declaration all checked on one in full.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S41",
  "workflows/legacy_transform/blackdiamond-49financial/20260919T034609Z-c28c728/contract.json @b93693e3b7"
 ],
 "remedy": "NOT A ROUND-4 DEFECT AND NOT A REASON TO RE-RUN: the walk rowed what the graph gave it, and the missing bucket is a property of the SOURCE key strings rather than of the run. What is owed is a decision by the engine's owner on whether an S3Key row must resolve its bucket -- either the row carries it as its own field, or the contract states that a tier-prefixed key is bucket-relative and says relative to what. The malformed 's3:' scheme (single colon, no '//') is the separable half and is a one-character defect in whatever produced that key. \u26a0 READ WITH THE ROW: my own first parse of this misread the tier prefixes as bucket names, so any re-measure should print the raw values rather than trusting a path split.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v4",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v4"
 },
 "closed": false
}
```

## Round 5 L9 -- carrier for LGIC_LGCTFM-S42

```json
{
 "id": "LGIC_LGCTFM-S42",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A RESULT REPORTED AS A FALSIFICATION MEASURED A DIFFERENT PREDICATE. The cell hunted 'bare s3:, head empty after stripping the prefix' and found 0 across 6 of 6 runs -- correct. The analysis it is reported as falsifying claimed a malformed SINGLE-COLON s3: scheme, which exists: 1 row, 's3:blackdiamond/49f/_ops/pull_state.json', re-measured by this seat across all 6 runs. The cell's own result sentence concedes it -- 'a genuine s3:<key> value with a non-empty body'.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S42",
  "BUCKETLESS_S3KEY_R5.json hunt_bare_s3_colon, predicate stated verbatim",
  "3.0.0_SA_CVO's 6-run sweep at HEAD ccbf4ac3cb"
 ],
 "remedy": "NOTHING IN THE ROUND CHANGES AND NO ARTIFACT IS REWRITTEN -- the cell measured what it said it measured and said so precisely. What is owed is that the round-5 ANALYSIS does not carry forward 'the analysis's characterisation is falsified' as a finding, because the next reader will inherit a retraction of a true statement. The 24th row IS single-colon-prefixed and IS firm-prefixed; those are two descriptions of one row, not competing claims. \u2b50 THE TRANSFERABLE HALF: A FALSIFICATION IS ONLY A FALSIFICATION IF THE PREDICATE MEASURED IS THE PREDICATE CLAIMED -- and a printed denominator beside a substituted predicate reads as decisive, which is why this one travelled from the cell's careful artifact into a hand-off sentence that overstates it. COST: one read of the original claim's wording before reporting a refutation of it.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v5",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v5"
 },
 "closed": false
}
```
