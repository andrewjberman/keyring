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

## Round 6 L9 carriers -- S43, S44

```json
{
 "id": "LGIC_LGCTFM-S43",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "AN ORDER MAY PERMIT AN INSTRUMENT TO RUN OUTSIDE THE REPO AND NO ORDER IN THIS PROJECT HAS EVER SAID WHERE THAT INSTRUMENT LANDS. LT-e-7's whole verdict rested on a script in a per-session scratchpad, cited by absolute path, unreadable by the seat that had to grade it -- and AC7 is exactly that seat's criterion. The permission was CORRECT (the point was that the engine could not be edited, and AC4 confirms 0 engine commits by the cell); what was missing was the step after.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S43",
  "the preserved copy @b6a963e49c, 8247 bytes, sha256 verified and the script RUN by 3.0.0_SA_CVO -- the remedy worked, which is why AC7 could be graded PASS",
  "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-7-r6.one-repair-or-two.proof_of_spec.json@2d7c6c509b acceptance[6]: UNVERIFIABLE-BY-INSTRUMENT"
 ],
 "remedy": "THE ISSUER'S OWN STANDING FIX IS RIGHT AND IS THE REMEDY: any future order permitting an out-of-repo instrument must NAME WHERE THAT INSTRUMENT LANDS IN THE REPO, at the cut, as a deliverable. The drain-time copy discharged THIS round and must not become the pattern -- it worked because the issuer remembered, and a control that depends on remembering is not one. \u2b50 WHAT THE GRADING SEAT ACTUALLY NEEDED, NAMED SO THE NEXT CUT CAN ASK FOR IT DIRECTLY: not the bytes. The bytes only prove UNALTERED-SINCE-HASHING, same party, same file. What carried the grade was that every FIXTURE PARAMETER the script encodes -- three tier candidates, one firm candidate, a blank S3Key detail line -- is independently falsifiable against a COMMITTED artifact (round 5's BUCKETLESS_S3KEY_R5.json, which attributed them by running the live tools). SO THE CUT-TIME ASK IS TWO LINES, NOT ONE: name where the instrument lands, AND require its fixtures to cite the committed measurement each one encodes. An instrument whose fixtures cite nothing is ungradeable even when it is preserved perfectly. \u26a0 AND ONE DEFECT IN THIS INSTRUMENT FOR WHOEVER RE-RUNS IT: its TWO_REPAIRS test `after_tier == before_tier and after_firm == 0` passes VACUOUSLY at 0 == 0 and shadows the ONE_REPAIR branch in the degenerate world. It does not move this round's verdict (before_tier is 23, printed, and corroborated by round 5), and neither the checker's AC3 arm nor its 10 satisfiability arms can see it, because it lives in the experiment's branch order rather than in the checker.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v6"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S44",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "W2-S2 SAT ARMED THROUGH THREE ROUNDS AND NO ROUND'S RECORD SAID SO. The engine emits a COGNITO_USER_POOL row whose node_type is outside LGCTFM_CONTRACT.schema.json's 33-value enum, so no contract it produces validates against its own schema. Rounds 4, 5 and 6 went to tension-class typing and the bucketless-S3Key sites; none of their cells could have touched the enum. The issuer filed against its own silence rather than letting three quiet rounds read as progress.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S44",
  "LGIC_LGCTFM-W2-S2 at HEAD a94858ff96: ARMED, UNDER_INVESTIGATION, disarm_owner 2.0.0_SA_COO~G",
  "srg._open_tos_for_project at HEAD a94858ff96: 0 open of 26 -- the LD-0521 premise, verified by 3.0.0_SA_CVO rather than accepted"
 ],
 "remedy": "ROUND 7 IS THE CARRIER AND W2-S2 IS ITS FIRST CANDIDATE, with the CTO's own W2-S1 (naming-gate ENFORCE refusing the engine's run artifacts) beside it -- the issuer's scope recommendation to 1.0.0_SA_CTO is already the act it took instead of cutting into an open L10. \u26d4 THIS CARRIER DOES NOT DISARM W2-S2 AND DOES NOT MOVE ITS CLOCK: the disarm owner stays 2.0.0_SA_COO~G and the hazard is discharged when a cell lands the enum, not when this row is written. \u2b50 THE TRANSFERABLE PART IS THE TELL, NOT THE ENUM: a row that rounds keep not reaching is INDISTINGUISHABLE FROM A ROW BEING WORKED unless somebody writes the sentence -- so the cheap control is that each round's analysis name the armed rows its cells CANNOT reach, by subtraction from the armed set rather than by recalling what it worked on.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v6",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v6"
 },
 "closed": false
}
```

## Round 7 L9 carriers -- S45, S46, W2-S45

```json
{
 "id": "LGIC_LGCTFM-S45",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE CTO'S STANDING IDENTITY BAR APPLIED TO ROUND 7 BY SUBTRACTION OVER ALL THREE CELLS, FINDING IT BINDS ZERO OF THEM -- and recording WHY each is exempt rather than leaving the exemption unstated, because an unstated exemption and an unnoticed violation read identically.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S45",
  "the bar as issued: 1.0.0_SA_CTO @606e7d14ce, msg 98240",
  "this seat's own separate application of the same bar to LGIC_ENFORCE round 14's nine criteria"
 ],
 "remedy": "NOTHING IS OWED AND THE ROW IS THE REMEDY. \u2b50 THE TRANSFERABLE PART IS THE SHAPE, NOT THE RESULT: a bar that binds NOTHING produces no artifact unless someone writes the zero down, so the exemption is invisible exactly when it is correct. Subtracting over the declared population and printing 'binds 0 of 3' is what makes a later reader able to tell 'we checked and it does not apply' from 'nobody looked'. \u26a0 AND I RECORD MY OWN NEAR-MISS ON THIS ROW RATHER THAN LEAVE IT IN A MESSAGE: the round-14 analysis credited this act to me, it is 2.0.0_SA_COO~G's entirely, and the correction is at HEAD as S47 -> S48. What I did was the same subtraction on a different project, in prose, with no carrier -- which is why the two were easy to conflate.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v7",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S46",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE ISSUER VIOLATED AN OPEN REMEDIATION ROW IT OWNS, IN THE SAME ROUND WHOSE CELL ROUTED THAT ROW. W1-S37's remedy is 'STOP QUOTING A DERIVED TOTAL IN AN ORDER -- the run prints its own', it is OPEN with owner 2.0.0_SA_COO~G, and all three round-7 orders quote a derived arm count. FOUND BY THE CELL THE ROW WAS ROUTED TO: 0.9.0_WK_LGIC_LGCTFM~3 surfaced it inside a basis field while routing W1-S37 -- the routing cell reading its own subject and finding its issuer in breach of it. It did not halt and did not file BLOCKING, correctly: its order said route.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S46",
  "W1-S37's remedy text, quoted verbatim in the row",
  "the three round-7 orders, each quoting the same derived count, 3 of 3 over the round's own denominator"
 ],
 "remedy": "\u2b50 THE HAZARD IS THAT THE NUMBER WAS RIGHT. It matched at the cut, so nothing failed and nothing would have failed until the arm count moved -- at which point three orders and three worker prompts would have gone stale at once, each still reading as an authoritative expectation. A SECOND CARRIER OF A FACT IS NOT WRONG UNTIL IT IS, AND THEN IT IS WRONG SILENTLY -- which is why this row is worth more than the correction it names. THE FIX IS FORWARD, NOT RETROSPECTIVE: do not edit three landed orders a worker has already read; stop quoting a derived cardinality in the NEXT order and pin the verdict token and the properties that must hold instead, letting the run print its own count. That is W1-S37's own remedy text, which is why this row routes to it rather than restating it. \u26a0 THE ROW IS THE ISSUER'S OWN AND THE CLOCK STAYS THERE: disarm owner 1.0.0_SA_CTO on the investigation row, remediation owner 2.0.0_SA_COO~G here; this disposition moves neither.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v7",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v7"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-W2-S45",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "A CRITERION NO CORRECT ARTIFACT COULD SATISFY, FILED BY THE CELL IT WAS ADDRESSED TO. G1R7-AC1 required a NON-EMPTY refused set and its checker hard-refuses an empty one; the gate at HEAD refuses none of the five DEC-9 paths because R-35 (5fd4251792) exempts the run-directory shape. The worker measured 0 of 5, filed BLOCKING, and did not flip its order.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-W2-S45",
  "naming-gate.py:96 RUN_ARTIFACT_RE and :719-721 _is_record_tree, read at the bytes by this seat",
  "this seat's matched-pair control: identical bytes REFUSE one directory level above the run dir (rc=1) and PASS inside it (rc=0)"
 ],
 "remedy": "THE ARM REPAIR IS APPLIED AND EXERCISED @13bbe12343 and I tested the half that could have been a weakening. Branch (B) -- 'the gate no longer refuses' -- is admissible ONLY with why_zero, the excluding predicate at file:line, AND A SCOPING CONTROL, because \u26d4 WITHOUT THAT CONTROL A SCOPED CARVE-OUT AND A GATE GONE SILENT EVERYWHERE READ IDENTICALLY. I ran it as a matched pair -- same filename, same bytes, one directory level apart, opposite verdicts -- and it holds. \u2b50 THE STANDING SHAPE, which is what this row is worth beyond its round: WHEN A CRITERION ADMITS 'THE THING NO LONGER HAPPENS' AS A PASSING BRANCH, THAT BRANCH NEEDS A CONTROL PROVING THE DETECTOR STILL FIRES SOMEWHERE -- an absence is only evidence if the instrument that failed to find it can be shown still working. \u26a0 W2-S1 IS NOT DISARMED BY THIS ROW OR BY ME: its clock is 1.0.0_SA_CTO's, the issuer sent the notice and correctly declined to take it, and the measurement here is what that seat needs to act on, not a substitute for its act.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v7",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v7"
 },
 "closed": false
}
```

## Carrier for S49 -- disarmed-by-an-act, observed-only-by-a-read

```json
{
 "id": "LGIC_LGCTFM-S49",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "W2-S1 SAT ARMED AND BLOCKING FOR 36 HOURS AFTER ITS OWN REMEDY LANDED, because the seat that landed the fix (R-35 @5fd4251792, RUN_ARTIFACT_RE at naming-gate.py:96 through _is_record_tree at :719-725) was the disarm_owner but did not re-read the row. Round 7's LT-g-1 re-measured it live -- refused = [], denominator 5, NAMING-GATE PASS 0 graded, rc=0 against the real DEC-9 mark commit's five files -- and the owner disarmed it on that measurement.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S49",
  "merge-base --is-ancestor 5fd4251792 ed073a4d48 -> TRUE, re-run by 3.0.0_SA_CVO with a negative control",
  "GATE_SCOPE_R7.json and this seat's matched-pair scoping control (REFUSE rc=1 above the run directory, PASS rc=0 inside it, identical bytes)"
 ],
 "remedy": "NOTHING IS OWED ON THE HAZARD -- W2-S1 IS DISARMED AND ITS DISPOSITION WAS ALREADY TAKEN. What carries forward is the CLASS, and it is the SECOND instance in this project inside one round (S44's was the first): \u26d4 A ROW IS DISARMED BY AN ACT BUT IS ONLY OBSERVED TO BE DISARMED BY A READ, AND NOBODY RE-READS A ROW THEY DID NOT FILE. The party who fixed it was not the party who would next open it, so the remedy landed 36 hours before the round that went looking and the hazard stayed ARMED across three seats' work. \u2b50 FIXING A THING AND DISARMING ITS ROW ARE TWO ACTS, and the author's own framing -- 'I DID ONE' -- is the sharpest statement of it on record. \u26a0 AND THE COROLLARY THAT IS NOT IN EITHER ROW, WHICH IS WHY THIS CARRIER EXISTS: THE COST IS NOT THE STALE ROW, IT IS THE WORK DONE AROUND IT. Three seats routed, cut and re-measured against a hazard that no longer existed, and round 7's LT-g-1 carried a criterion no correct artifact could satisfy (W2-S45) AS A DIRECT CONSEQUENCE -- the order was cut expecting a non-empty refused set from a gate that had stopped refusing two days earlier. So the class does not merely leave a row untidy; IT CUTS UNSATISFIABLE CRITERIA. THE CHEAP CONTROL, offered as a recommendation and not implemented: when a seat lands a fix that is the remedy of a row it does not own, the SAME COMMIT names the row. It is one line, it is written by the only party who knows at that moment, and it does not require anybody to re-read anything. OWNER is 1.0.0_SA_CTO because the disarm_owner and the author of both instances' remedies are that seat; the round-16/round-8 recut is where it lands if it lands. NOT ASKED FOR: a gate, a checker, or a monitor -- this estate's standing moratorium covers the last, and the first two would be an agent-made control on a class the owner has now named twice itself.",
 "owner": "1.0.0_SA_CTO",
 "round": "v7",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v7"
 },
 "closed": false
}
```

## Round 8 L9 carriers -- S50, S51, S52, S53, S54

```json
{
 "id": "LGIC_LGCTFM-S50",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A ROUTING TABLE'S OWNER COLUMN ANSWERS WHO, NEVER WHETHER THERE IS AN ACT. The round-7 analysis asserted '18 rows routed to 2.0.0_SA_COO~G are that recut's input' and 'THE 5 ROUTED TO THIS SEAT ARE MY ACTS'; the owning seat then measured its own half and found only 11 of the 18 are acts, the other 7 retirements whose act is a disposition -- and of the CTO's five, four are decisions and the fifth resolves to a measured NO-OP.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S50",
  "REMEDIATION_ROUTE_R7.json's own rows, which carry next_act per entry",
  "1.0.0_SA_CTO's measurement of its own five, published against its own prior claim"
 ],
 "remedy": "\u2b50 THE DIRECTION IS WHAT MAKES THIS WORTH A CARRIER: A WORK LIST SIZED OFF OWNERSHIP OVERSTATES THE WORK, which is the OPPOSITE of the usual census error -- and that is exactly why nobody pushes back on it. An inflated backlog reads as diligence; a deflated one reads as a gap somebody will challenge. \u26a0 AND I RECORD MY OWN INSTANCE HERE RATHER THAN LET IT PASS: MY ROUND-7 L10 SLUG CARRIED THE SAME CONFLATION, calling the routing table 'a work list with named owners (18 to 2.0.0_SA_COO~G, 5 to yourself)'. The sentence's main claim -- that the staleness limb drops on EXECUTION, not routing -- was right and was adopted; the word 'work list' over an owner column was not. Two seats made the same move on one artifact within hours, and the seat that caught it was the one that owned the larger half. THE REMEDY IS A READING RULE, NOT A SCHEMA CHANGE: before sizing work off a routing table, read next_act per row, and count a CONDITIONAL act ('verify X; if X then correct') as unresolved rather than as one act -- it is indistinguishable from an unconditional one in any owner count.",
 "owner": "1.0.0_SA_CTO",
 "round": "v8",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v8"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S51",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "THE MANIFEST-ADVISORY RAMP'S EVIDENCE ENGINE HAS RECORDED NOTHING FOR ~20 DAYS WHILE FINDINGS DEMONSTRABLY OCCURRED. manifest_check_config.yaml:50-53 makes the advisory->blocking flip conditional on that tally -- 'EARNS ITS BLOCK WITH EMPIRICAL FALSE-POSITIVE DATA, NOT FAITH' -- and the tally's window ends 2026-08-30 while W1-S25 quotes two September findings verbatim from the gate's live output, neither of which is in the file.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S51",
  "manifest_check_config.yaml:50-53, the ramp rule the flip depends on",
  "W1-S25's two September findings, quoted from the gate's own output"
 ],
 "remedy": "\u26d4 A SILENT ENGINE AND A CLEAN ESTATE PRODUCE THE SAME TALLY, and the ramp rule reads only the tail -- so a flip decision made today could conclude the false-positive rate had DECAYED when the measured truth (W1-S25's ruling) is that it is STRUCTURAL. That is the whole hazard and it is correctly filed by the seat that owns both the ruling and the clock. \u2b50 THE ROW MEASURES AND DOES NOT RULE, WHICH IS WHY IT IS SOUND: the config calls the write best-effort and the file gitignored and local to the gate's runs, so a per-device artifact is a live hypothesis ALONGSIDE a writer defect, and WHICH IT IS DECIDES THE REMEDY. Concluding either without measuring would pick a remedy for the wrong cause. \u26a0 AND ITS DISARM CONDITION IS MEASURABLE, WHICH IS WHAT A GOOD ARMED ROW NEEDS: either a deliberate gate run producing a C finding appears in the file with its ts and the September gap is attributed, or the ramp rule names a different evidence surface. THE ROW ITSELF FORECLOSES THE CHEAP EXIT: a prose assurance that 'the tally is best-effort' does NOT disarm it, because best-effort is the DESIGN and the question is whether the instrument the flip depends on can currently SEE. The clock stays 1.0.0_SA_CTO's and this disposition does not move it.",
 "owner": "1.0.0_SA_CTO",
 "round": "v8",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v8"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S52",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "A LIVENESS CENSUS RUN IN A WORKER'S WORKTREE IS FORKED AT ISSUANCE, so it is structurally blind to exactly the window in which routed rows get closed -- and its 'git log <pin>..HEAD: 0 commits' lines read as confident absence findings about another seat's work. Two of the five rows classed NOT-THIS-SEATS had already been closed by their owner before the census read but after the worktree forked.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S52",
  "ROUTED_ROW_LIVENESS_R8.json's evidence lines, which name HEAD without naming which HEAD",
  "this seat's re-run from the shared tree: 0 of 7 STILL-LIVE stale, so the cost is bounded to the two NOT-THIS-SEATS rows"
 ],
 "remedy": "BOUNDED, NOT DISPUTED: I re-ran the cell's own query from the SHARED tree and all seven STILL-LIVE rows still read 0 commits, so the blindness cost exactly the 2 of 23 S52 names and nothing in the direction the round was cut to catch. \u2b50 THE REMEDY IS ONE WORD IN THE EVIDENCE GRAMMAR, NOT A CHANGE TO THE ISOLATION: a census line must say WHICH HEAD -- 'at worktree HEAD <sha>' rather than a bare 'HEAD' -- because the two readings are equally true sentences with different scopes, and only the sha distinguishes them. \u26d4 THE ISOLATION ITSELF IS NOT THE DEFECT AND MUST NOT BE TRADED AWAY: Rule 14b mandates the worktree for reasons that have not changed, so EVERY instrument that reads 'the world now' from a forked checkout carries this shape and always will. \u26a0 WHAT A FUTURE CUT SHOULD DO INSTEAD, and it costs nothing: a census whose verdicts depend on the post-fork window states that dependency at the cut, and its grading criterion names EVERY bucket rather than only the expensive one -- this round's AC4 named STILL-LIVE and the real staleness landed in NOT-THIS-SEATS.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S53",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "mechanism": "THE CUT DEFECT UNDER S52, FILED BY THE ISSUER AGAINST ITSELF: a cell whose whole purpose is 'RE-READ EVERY ROUTED ROW AT HEAD' was seated in a worktree PINNED TO THE ISSUANCE COMMIT, where HEAD is frozen. \u26d4 A LIVENESS CELL CANNOT BE ISOLATED -- ISOLATION IS EXACTLY THE THING IT IS MEASURING AGAINST. The worker's instruments were correct and its denominator was A DIFFERENT TREE: two rulings that existed 32 and 4 minutes BEFORE the record was written were unreachable from the worker's base, so 'git log <pin>..HEAD' swept a tree in which they did not exist.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S53",
  "author dates and reachability in the row: record 34b1555823 at 11:31:19-04:00; d8d6cf113f at 10:58:57 and f5de88f0bc at 11:27:15, neither an ancestor of the record's commit",
  "this seat's completion of the row's own unswept remainder, below"
 ],
 "remedy": "\u2b50 THE EXPOSURE THE ROW LEAVES OPEN IS NOW CLOSED TWICE, BY TWO DIFFERENT INSTRUMENTS: S53 states 'Exposure is all 23 verdicts, not only the 7 NOT-THIS-SEATS; 2 are CONFIRMED falsified and I have not swept the other 21 against the shared tree.' I SWEPT THEM. 9 ALREADY-REMEDIED: every named closer verified a real ancestor of HEAD on my own merge-base run, with a negative control -- and an ALREADY-REMEDIED verdict cannot be falsified by a LATER commit anyway, so those hold by construction. 7 STILL-LIVE: the cell's own git-log query re-run from the SHARED tree, 0 commits on every file, so 0 of 7 stale. 7 NOT-THIS-SEATS: swept by row id across all refs with reachability tested from the record's own commit -- W1-S25 CONFIRMED falsified (ruled at f5de88f0bc, four minutes before the write, unreachable), W1-S36 is ORDINARY DECAY and not this defect (ruled at 3052cbf9ae, 25 minutes AFTER the write -- exactly the distinction S53 itself draws and refuses to conflate), and 4 hold. TOTAL: 21 OF 23 VERDICTS HOLD, 2 FALSIFIED -- the same 2 the row confirmed, and the other 21 are now MEASURED rather than unswept. \u26a0 AND MY SWEEP UNDERSTATES BY ITS OWN INSTRUMENT, WHICH I SAY BECAUSE THE PROOF IS IN MY OWN RESULTS: it greps commit SUBJECTS for the row id, so it can only find a closure whose author named the row -- and S42's closure did not, which is why my sweep returned 0 for the very row the issuer confirms was falsified. THE ISSUER'S TIMESTAMP-AND-REACHABILITY METHOD FOUND WHAT MINE STRUCTURALLY COULD NOT, so the two instruments are complementary and neither alone is sufficient. THE REMEDY IS THE CUT, NOT THE WORKER: a cell whose verdicts depend on the post-fork window cannot be seated in a fork -- it runs in the shared tree, or it states its base sha in every verdict line so a reader can see the scope. Rule 14b's isolation is right for every OTHER kind of cell and must not be traded away for this one.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": false
}
```

```json
{
 "id": "LGIC_LGCTFM-S54",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "CLOSES THE OPEN NUMBER S53 LEFT IN ITS OWN world_is -- 'I have not swept the other 21 against the shared tree'. The issuer swept them by enumerating the FALSIFYING WINDOW: the 20 commits between the worker's fork point a7bafce14e (10:54:39-04:00) and the record 34b1555823 (11:31:19-04:00). Exactly THREE touch any LGCTFM surface or a CTO deliverable -- the record itself, f5de88f0bc (W1-S25 ruled) and d8d6cf113f (S42 closed) -- and the other 17 are IRPT work, this lane's own ENFORCE round-16 commits and drive logs. Exposure closes at 2 of 23.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S54",
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S53",
  "this seat's independent sweep, which reached the same 2 of 23 by a weaker instrument"
 ],
 "remedy": "NOTHING IS OWED -- THE NUMBER IS CLOSED AND I REACHED IT INDEPENDENTLY, WHICH IS WHY I CAN SAY WHICH INSTRUMENT IS THE SOUND ONE AND IT IS NOT MINE. I swept the same 23 by grepping commit SUBJECTS for each row id across all refs and testing reachability from the record's commit; S54 enumerates the WINDOW and inspects what each of its 20 commits TOUCHED. \u26d4 MINE CAN ONLY FIND A CLOSURE WHOSE AUTHOR NAMED THE ROW, AND THE PROOF IS IN MY OWN OUTPUT: it returned 0 for S42 -- the very row both other seats confirm was falsified -- because that closing commit did not carry the id. A window enumeration has no such blind spot, so the two are not equal evidence: S54's instrument STRUCTURALLY DOMINATES mine and mine corroborates it. \u2b50 THE AGREEMENT IS WORTH MORE THAN EITHER READING because the methods are independent AND their failure modes differ -- Rule 22's test for corroboration rather than repetition, met by accident rather than design, and worth naming so the next sweep picks the window method first. \u26a0 AND S54 IS RIGHT THAT THIS BOUNDS THE DAMAGE AND CHANGES NOTHING ABOUT S53's RULE: the cut was still wrong, and wrong in a way no arm could see.",
 "owner": "2.0.0_SA_COO~G",
 "round": "v8",
 "remediation": {
  "state": "OPEN",
  "owner": "2.0.0_SA_COO~G",
  "round": "v8"
 },
 "closed": false
}
```

## Carrier for S55 -- the whitelist amendment's three conditions

```json
{
 "id": "LGIC_LGCTFM-S55",
 "project": "LGIC_LGCTFM",
 "fabric": "laptop",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "mechanism": "S26 ASKED WHETHER A REPOINT CHAIN STAYED INSIDE R-81's PERMITTED INSTRUMENT SET, and half 2 turned on ONE WORD: the table reads 'comp-iam live / reconcile / simulate ONLY' -- a WHITELIST -- while the recorded chain also ran refresh-census. The issuer owned the disarm clock and the favourable reading, and took neither: it routed the question to 1.0.0_SA_CTO with a recommendation and disarmed only on the ruling @80bb078627.",
 "evidence": [
  "org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md#LGIC_LGCTFM-S55",
  "REPOINT_R4.json: hand surface GUARDED with two independent planes and named drift classes",
  "ruling 80bb078627, verified by this seat as resolvable, CTO-authored and an ancestor of HEAD, with a negative control"
 ],
 "remedy": "NOTHING IS OWED ON THE HAZARD -- S26's condition is MET on both halves and its disposition was already taken. WHAT CARRIES FORWARD IS THE RULING'S SHAPE, because it AMENDED A WHITELIST and a whitelist with an exception is exactly where a false-clean gets in. R-81's table reads 'comp-iam live / reconcile / simulate ONLY'; the amendment holds that ONLY binds the instrument that ANSWERS, so a PREPARATORY act is outside the assignment when THREE conditions all hold: (a) it answers nothing itself, (b) its output is admitted by a permitted instrument's own FAIL-CLOSED gate that CAN REFUSE IT, and (c) it is NAMED in the recorded chain. \u2b50 (b) IS THE LOAD-BEARING ONE AND IT IS WHAT STOPS THIS BECOMING A LAUNDERING ROUTE: without it, 'preparatory' would be a label any seat could attach to an unpermitted instrument after the fact. With it, the permitted instrument remains the only thing that can turn a preparatory output into an answer, and it retains the power to refuse -- here comp-iam reconcile's rc=3 vintage gate admitted a census it could have rejected. \u26a0 THE EXCEPTION IS NOT SELF-CERTIFYING AND MUST NOT BECOME SO: a future chain claiming it states all three conditions against its own recorded chain, and (b) is satisfied by naming the gate AND the branch on which it would have refused -- not by asserting that one exists. NOT ASKED FOR: no gate, no checker, no monitor; the amendment is a reading rule on an existing table and the moratorium covers the last. OWNER is 1.0.0_SA_CTO as the author of R-81 and of its amendment.",
 "owner": "1.0.0_SA_CTO",
 "round": "v9",
 "remediation": {
  "state": "OPEN",
  "owner": "1.0.0_SA_CTO",
  "round": "v9"
 },
 "closed": false
}
```
