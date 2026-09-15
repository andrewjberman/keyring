# LGIC_NAMING -- round 3 remediation slug

Author: 3.0.0_SA_CVO. Round: v3. Fabric: laptop. Recorded: 2026-09-15T15:10:15Z.

Input: `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130` (48 rows; 6 compiled at this L8). Adjudication: `ADJUDICATION_v4.md` (C-S18..C-S23), same slug. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND3_L8_L9_20260915.md`.

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's. There is one row per item graduated this round: S17 (C-S19), S18, W1-S7 and W2-S6 (C-S20), W3-S5 (C-S21) and W3-S6 (C-S22). There is also one backfill, S3, which graduated at C-S2 and never had its row (C-S23). S17's remedy was executed inside the round by its owner, so its row is REMEDIATED. Every other row is OPEN. In the same slug, five of REMEDIATION_v2's rows advance OPEN -> REMEDIATED in place (C-S23).

```json
[
 {
  "id": "LGIC_NAMING-S17",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "to-pipeline-gate LIMB 6 refused round 3's issuance when committed from a linked worktree -- 'PRD has NO sign-off' on both halves -- although prd-signoff.py status read ADMITTED in that worktree, safe-commit's own gate stage printed 'L4-R sign-offs OK' in the same commit, and the identical commit passed from the primary checkout.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-S17",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v4.md (same slug) row LGIC_NAMING-C-S19",
   ".tools/prd_signoff_lib.py@0801a7d48c read_signoff_files"
  ],
  "remedy": "Remove git's location variables (GIT_DIR, GIT_INDEX_FILE, GIT_WORK_TREE, GIT_PREFIX, GIT_COMMON_DIR) from the signoff HEAD-read, so a commit hook in a linked worktree cannot steer it. DONE by 1.0.0_SA_CTO @0801a7d48c and EXERCISED by 3.0.0_SA_CVO in a linked worktree under the hook's variables (pre-fix []; HEAD 3 of 3).",
  "owner": "1.0.0_SA_CTO",
  "round": "v3",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO",
   "round": "v3"
  },
  "closed": true
 },
 {
  "id": "LGIC_NAMING-S18",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "5 of 6 round-3 task orders name a result file at a path that already held a prior round's result for the same slot serial at the issuance commit, so each of those workers' results replaces the prior round's record at HEAD. The cause is shared: the issuer's generator reused each cell's result stem.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-S18",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v4.md (same slug) row LGIC_NAMING-C-S20"
  ],
  "remedy": "At the next issuance, put the round in every result stem (for example namer-a.r4.result.md), so no order's named result path already holds another order's record. Pin each result file by commit, not PENDING-THIS-COMMIT, so a later touch of the instance cannot re-point it.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W1-S7",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-LN-e-1-r3 names its result file namer-a.result.md beside the proof instance in deliverables/0.9.0_WK_LGIC_NAMING~1/, which is the path that already holds round 2's result for the complete order TO-LN-e-1-r2 (@eaafb46486, amended @e8490dcbfb). Writing it as ordered replaces round 2's record at HEAD.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-W1-S7",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v4.md (same slug) row LGIC_NAMING-C-S20"
  ],
  "remedy": "The shared remedy of S18: the round in the result stem at the next issuance. No restore is owed: round 2's record resolves at its proof's pin @eaafb46486.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W2-S6",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-LN-e-2-r3 names its result file namer-b.result.md, beside the round-3 instance in deliverables/0.9.0_WK_LGIC_NAMING~2/. That path already holds round 2's namer-B result (TO-LN-e-2-r2), so writing the order's file replaces round 2's record at HEAD.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-W2-S6",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v4.md (same slug) row LGIC_NAMING-C-S20"
  ],
  "remedy": "The shared remedy of S18: the round in the result stem at the next issuance. No restore is owed: round 2's record resolves at its proof's pin @59f68115a4.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W3-S5",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The own-kind bar (FN1c, GRADING_RULE R5.b) can leave a function slot with no token, e.g. a LAMBDA named mdpf-lambda-lambda, and neither TO-LN-g-1-r3 nor NAMING_SCHEMA v1.7 names the output then: the RAISE on an empty function is stated for FN1b's subtraction only. The re-cut rule says it does not decide, instead of choosing.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-W3-S5",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v4.md (same slug) row LGIC_NAMING-C-S21"
  ],
  "remedy": "Rule in NAMING_SCHEMA.json resource.function whether a function emptied by the own-kind bar RAISES (grade.unplaceable), as FN1b's does. Name the order of FN1b and FN1c, because the outcome depends on it. GRADING_RULE R5.b and LGIC_ENFORCE's grade() then take the ruling.",
  "owner": "1.0.0_SA_CTO",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W3-S6",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-LN-g-1-r3 has GRADING_RULE.md's header name NAMING_SCHEMA.json v1.7 and says no other step moves, but 12 fields besides version, changelog and ratified_by changed between v1.4, the version the rule was cut at, and v1.7. Only resource.function is re-cut, and at least two changes contradict steps the rule still states: aws_fixed (G2) and grade.placeholder (V-2).",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-W3-S6",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v4.md (same slug) row LGIC_NAMING-C-S22"
  ],
  "remedy": "Re-cut GRADING_RULE.md to v1.7 on every changed field its steps cite, at least G2 against aws_fixed (excluded, never RAISE) and V-2 against grade.placeholder. Or rule which fields the rule stays at v1.4 on, and why. The G2 half also closes round 1's W1-S4. The cut is 2.0.0_SA_COO~G's once 1.0.0_SA_CTO names the fields.",
  "owner": "1.0.0_SA_CTO",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v3"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S3",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The spine's L6 queue rule puts dependent cells in ONE worker's queue, but this PRD's N3 and N6 exercises need DIFFERENT workers on dependent cells (graders who did not write N2; namers who never confer), so the L5 decomposition serialises those cells by spawn-after-drain and supports a fan-out N above its chain count M.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@219f006130#LGIC_NAMING-S3",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v1.md row LGIC_NAMING-C-S2 (GRADUATED, pre-issuance intake)",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v4.md (same slug) row LGIC_NAMING-C-S23 (the backfill census)"
  ],
  "remedy": "Rule whether the spine's L6 queue rule names an exception for an exercise whose validity is the workers' independence: spawn-after-drain on dependent cells, and a fan-out N above the chain count M with the reason stated. Or state that LGIC_NAMING's reading is wrong. This seat read the project's resolution as sound at C-S2. BACKFILL: this row was owed since C-S2 and lands in round 3.",
  "owner": "1.0.0_SA_CTO",
  "round": "v3",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v3"
  },
  "closed": false
 }
]
```
