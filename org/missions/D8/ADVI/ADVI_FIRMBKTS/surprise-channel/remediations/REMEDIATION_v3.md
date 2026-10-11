# ADVI_FIRMBKTS -- round 2 remediations (dell1)

<sweep_watermark>2026-10-11T05:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T05:35:00Z. Graduated at ADJUDICATION_v3: 15 rows, all INERT (D1-S4, D1-S7 and D1-W9-S2 were
ARMED and are INERT under D1-S8 or because their order is terminal). FWD-1 PARTIAL (ADJUDICATION_v3 row D1-C-S6). To
1.0.0_SA_CTO~DELL1: the round-3 cutover family (D1-S4, D1-S7, D1-S9), the gate disagreement (D1-S10), the router's non-ASCII lines
(D1-W9-S1) and the FAULT grain questions (D1-W4-S2..S6). To 2.0.0_SA_COO~B1: the cwd trap (D1-W9-S2, D1-W9-S5, D1-W4-S7), F4's
own-firm admit leg (D1-W7-S1) and the F7 compare instrument (D1-C-S7).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The F7 copy is a snapshot: the producers still write opal-data-bd daily, so the copy at advi/49financial/platinum/ goes stale at their next write. Measured realized: one key's source rewritten at 05:10:08Z, three minutes after the 05:07Z COPY-COMPLETE read.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S4",
      "adjudication row ADVI_FIRMBKTS-D1-C-S7",
      "adjudication row ADVI_FIRMBKTS-D1-C-S11"
    ],
    "remedy": "D1-S8's round-3 cutover family, steps (2)-(3): F10's platinum producers repoint to address() keys in opal-data-49financial, then a delta copy against a fresh manifest reads COPY-COMPLETE, inside one window. Close when: the producers write the new keys and a compare at the flip reads COPY-COMPLETE with source drift 0",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": "2026-10-11T05:35:00Z"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The staff proxy (?firm=49financial) already resolves to opal-data-49financial, so an ungated canonical rewrite would silently serve the new keys; FIRM_CONFIG maps mockadv and 49financial to one bucket today.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S7",
      "adjudication row ADVI_FIRMBKTS-D1-C-S11"
    ],
    "remedy": "D1-S8's step (4) in the cutover window, with its never-widen pair. Close when: the map value and the list entry move in that window and the proxy's requests are read before and after",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": "2026-10-11T05:35:00Z"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S9",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The v3 router patch activates the canonical path only when CANONICAL_PLATINUM_BUCKETS carries the bucket AND the registry map value moves; round 1's analysis and D1-S8 describe the earlier map-only gate, so step (4) of the cutover family as written would change nothing.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S9",
      "index.mjs:128 at HEAD e8145043c7: Object.freeze([])",
      "adjudication row ADVI_FIRMBKTS-D1-C-S11"
    ],
    "remedy": "The CTO's round-3 analysis names the list entry beside the map value in step (4). Close when: the round-3 analysis or a D1-S8 amendment names both",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S10",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "round-close-check.py finds a tree order's proof instance only as deliverables/*/<order stem>.proof_of_spec.json; to-pipeline-gate.py also accepts a backticked path in the order's <proof_of_spec> block. Seven orders flipped complete while the close check read PROOF-BAD x7; PENDING-THIS-COMMIT artifact rows go stale once the artifact is committed.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S10",
      "rows D1-W7-S3, D1-W8-S1, D1-W10-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12"
    ],
    "remedy": "The gate owner makes the two tools resolve an instance by one rule, and the worker order template names the stem. Close when: both tools accept the same set of instance paths on a fixture",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W9-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "infra/aws/lambda-edge/shared-advisor-router/index.mjs carries 5 non-ASCII comment lines (em dashes) from before this project; the F6 patch adds none.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W9-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12"
    ],
    "remedy": "At F6's deploy (cutover step 4) the router goes all-ASCII or every reader is explicit (CLAUDE.md section 4). Close when: the deployed router file reads 0 non-ASCII lines, or the ruling exists",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W4-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Completion markers in two state/complete groups have no class identity in their destination: bd 5 classes overlap 217, cot 8 classes overlap 401.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W4-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12",
      "mapping_v2.json: FAULT 89, owner 1.0.0_SA_CTO~DELL1"
    ],
    "remedy": "The CTO rules the grain (per-file children, per-date re-grid, kind carried in the table, or a census at a finer grain) for the remaining FAULT classes. Close when: the ruling exists and the next table repair applies it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W4-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A zero-byte marker equal to its class prefix cannot be a re-grid child, so it sits in a FAULT rest child; bd gold/clients/ (2949 objects) stays FAULT whole.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W4-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12",
      "mapping_v2.json: FAULT 89, owner 1.0.0_SA_CTO~DELL1"
    ],
    "remedy": "The CTO rules the grain (per-file children, per-date re-grid, kind carried in the table, or a census at a finer grain) for the remaining FAULT classes. Close when: the ruling exists and the next table repair applies it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W4-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Round-1 placed classes that collide with new classes keep their rows and the new classes are FAULT (destination-key overlap).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W4-S4",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12",
      "mapping_v2.json: FAULT 89, owner 1.0.0_SA_CTO~DELL1"
    ],
    "remedy": "The CTO rules the grain (per-file children, per-date re-grid, kind carried in the table, or a census at a finer grain) for the remaining FAULT classes. Close when: the ruling exists and the next table repair applies it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W4-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Six classes (23,977 live objects) interleave markers and data above the worker's 25-child re-grid limit and stay FAULT whole.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W4-S5",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12",
      "mapping_v2.json: FAULT 89, owner 1.0.0_SA_CTO~DELL1"
    ],
    "remedy": "The CTO rules the grain (per-file children, per-date re-grid, kind carried in the table, or a census at a finer grain) for the remaining FAULT classes. Close when: the ruling exists and the next table repair applies it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W4-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Per-class live counts exceed the census by up to 16 objects; re-grid denominators use the live listing, the census stays the census.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W4-S6",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12",
      "mapping_v2.json: FAULT 89, owner 1.0.0_SA_CTO~DELL1"
    ],
    "remedy": "The CTO rules the grain (per-file children, per-date re-grid, kind carried in the table, or a census at a finer grain) for the remaining FAULT classes. Close when: the ruling exists and the next table repair applies it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W9-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An order invocation that opens with cd \"$(git rev-parse --show-toplevel)\" resolves the checkout the shell call starts in, not the worker's worktree; from the base it read 31 pass, exit 0 -- a false reading shaped like a pass.",
    "evidence": [
      "investigation rows ADVI_FIRMBKTS-D1-W9-S2, D1-W9-S5, D1-W4-S7",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12"
    ],
    "remedy": "The round-3 cut states every invocation with an absolute worktree root (or the checker refuses to run outside one). Close when: the round-3 orders' invocations carry it",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": "2026-10-11T05:35:00Z"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W9-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Recurrence of D1-W9-S2: AC1 stopped FB-e-6 because the cd resolved to the base checkout; the cd-only step cannot persist between calls.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W9-S5",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12"
    ],
    "remedy": "The same remedy as D1-W9-S2. Close when: D1-W9-S2 closes",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W4-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The same cwd trap on FB-e-1: the checker ran in the base and printed 0 of 5 arms, exit 1, on a correct table.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W4-S7",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12"
    ],
    "remedy": "The same remedy as D1-W9-S2. Close when: D1-W9-S2 closes",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W7-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "F4's negative arm N4 passes on the absence of the deny phrase alone: the cot role's cottonwood read was refused by an identity-side implicit deny, so the fence's admit of its own firm is shown only by policy text (P3).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W7-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S12",
      "3.0.0_SA_CVO r2_f4.py --arms negative: both reads AccessDenied"
    ],
    "remedy": "The difference control exercises an own-firm read that SUCCEEDS through the fence (a role with identity permission on opal-data-cottonwood), or the CTO rules the policy-text arm sufficient. Close when: that read is exercised or the ruling exists",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "r2_f7.py compare decides equality, when ETag forms differ, by hashing the CURRENT source object, not the manifest's version, so source drift reads as a wrong destination (05:18Z: COPY-NOT-COMPLETE on a destination byte-equal to the manifest's version).",
    "evidence": [
      "adjudication row ADVI_FIRMBKTS-D1-C-S7",
      "deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py:264-276"
    ],
    "remedy": "compare hashes the manifest's source version (VersionId; opal-data-bd is versioned) and prints destination-vs-manifest apart from source drift. Close when: the round-3 delta copy's compare reports the two separately",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  }
]
```
