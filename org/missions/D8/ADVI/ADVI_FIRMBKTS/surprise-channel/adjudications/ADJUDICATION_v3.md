# ADVI_FIRMBKTS -- round 2 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-11T05:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T05:35:00Z. L8 packet: 2.0.0_SA_COO~B1 msg 3509,
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/R2_CLOSE.md` @27bd0e5f9e (blob ea663dd0ba; the working tree holds an uncommitted F6-bullet edit, not graded).
7 of 7 orders complete. `round-close-check.py --project ADVI_FIRMBKTS --round 2 --deep`: proof_ok 7, judgment=0, MAY-CLOSE.

**L9:** no order carries a JUDGMENT criterion. This seat re-ran every criterion of the seven orders at HEAD e8145043c7 and graded
FWD-1 from the answer files on its own count: PARTIAL. Agreement 195 of 209 on all four fields, both readers right on all four
193 of 207; every disagreement is a grain choice. Contents: MET on this seat's read (0 date conflicts over 209; 36 of 36 sampled
pairs describe the same object). Independence: NOT MET (D1-S3 stays open). One re-run differs from the issuer's: F7's compare reads
COPY-NOT-COMPLETE at 05:18Z because a producer rewrote one source key at 05:10:08Z; the destination equals the manifest's version
(C-S7: D1-S4 realized, plus an instrument defect).

**Rows:** 24 open since v2 (7 BLOCKING, 4 ARMED; S2 stays as REMEDIATION_v1 left it). 10 dismissed (D1-S8 among them), 14 graduated INERT to
`remediations/REMEDIATION_v3.md` (9 to 1.0.0_SA_CTO~DELL1, 5 to 2.0.0_SA_COO~B1) plus the new C-S7 (to 2.0.0_SA_COO~B1).
REMEDIATION_v2: D1-W1-S2, D1-W1-S3 and S11 REMEDIATED; D1-S1, D1-S2, D1-S3 stay OPEN. No BLOCKING or ARMED row is open.

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-C-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:35:00Z",
    "one_line": "ROUND 2 L9: FWD-1 PARTIAL on this seat's own count. Agreement, canonical arm n=209: system 207, firm 209, tier 209, table 197, all four 195 (equal to the issuer's). Correctness against mapping_v2.json dest, truth joined for 207 of 209 (the two cot positions_cube classes are FAULT and have no dest): reader A right on all four fields 207 of 207; reader B system 205, table 195; both right on all four 193 of 207. Every one of the 14 canonical disagreements is a GRAIN choice, not a misreading: 9 times B names the partition below the table (state/parity/<x>, orion-rest/<x>, orion/trn) and 5 times B answers unknown. Contents clause MET on this seat's read: 0 date conflicts over 209 free-text pairs, and 36 of 36 pairs drawn at random (seeds 7 and 11) describe the same object; a word-level proxy (every word of the true table in both texts) reads 118 of 207 and is too strict to grade by (dim vs dimension, 'firm' tables named by their file). The legacy contrast holds: all four agree 47 of 209 and both right 32 of 207, system unreadable in 155. Independence NOT MET: readers 0.9.0_WK_ADVI_FIRMBKTS~5 and ~6 are subagents of one COO session on one model; nothing in the round makes them two people who never worked together (D1-S3 stays OPEN). Mechanical re-run at HEAD e8145043c7, 05:18Z: FB-e-1 structure 5 of 5, repair 4 of 4; FB-e-4 positive 3 of 3 (live), negative 4 of 4; FB-e-5 manifest --verify VERIFIED and residue UNCHANGED, but compare reads COPY-NOT-COMPLETE exit 1 (row D1-C-S7); FB-e-6 AC1 39 pass 0 fail, AC2 193 of 193 twice, AC3 20 of 20 and controls 10 of 10; FB-e-7 AC1 3 passed, AC2 naming gate PASS (0 graded), AC3 12 passed. round-close-check --deep: 7 of 7, proof_ok 7, judgment 0, MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ADVI_FIRMBKTS PRD FWD-1 ACCEPT: two people who have never worked together read the same list of storage locations and each says, for every one, which system made it, which firm it belongs to, how finished it is and what it holds -- and they agree. Spine L9: graded by a seat that did none of the work.",
    "world_is": "ROUND 2 L9: FWD-1 PARTIAL on this seat's own count. Agreement, canonical arm n=209: system 207, firm 209, tier 209, table 197, all four 195 (equal to the issuer's). Correctness against mapping_v2.json dest, truth joined for 207 of 209 (the two cot positions_cube classes are FAULT and have no dest): reader A right on all four fields 207 of 207; reader B system 205, table 195; both right on all four 193 of 207. Every one of the 14 canonical disagreements is a GRAIN choice, not a misreading: 9 times B names the partition below the table (state/parity/<x>, orion-rest/<x>, orion/trn) and 5 times B answers unknown. Contents clause MET on this seat's read: 0 date conflicts over 209 free-text pairs, and 36 of 36 pairs drawn at random (seeds 7 and 11) describe the same object; a word-level proxy (every word of the true table in both texts) reads 118 of 207 and is too strict to grade by (dim vs dimension, 'firm' tables named by their file). The legacy contrast holds: all four agree 47 of 209 and both right 32 of 207, system unreadable in 155. Independence NOT MET: readers 0.9.0_WK_ADVI_FIRMBKTS~5 and ~6 are subagents of one COO session on one model; nothing in the round makes them two people who never worked together (D1-S3 stays OPEN). Mechanical re-run at HEAD e8145043c7, 05:18Z: FB-e-1 structure 5 of 5, repair 4 of 4; FB-e-4 positive 3 of 3 (live), negative 4 of 4; FB-e-5 manifest --verify VERIFIED and residue UNCHANGED, but compare reads COPY-NOT-COMPLETE exit 1 (row D1-C-S7); FB-e-6 AC1 39 pass 0 fail, AC2 193 of 193 twice, AC3 20 of 20 and controls 10 of 10; FB-e-7 AC1 3 passed, AC2 naming gate PASS (0 graded), AC3 12 passed. round-close-check --deep: 7 of 7, proof_ok 7, judgment 0, MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO own script over org/tier1_exec/2.0.0_SA_COO~B1/round2/blind/{ANSWERS_A,ANSWERS_B,LOCATIONS}.json, READING_KEY.json and deliverables/mapping_v2.json (truth joined by bucket+class), 2026-10-11 ~05:2xZ: the counts above",
        "3.0.0_SA_CVO re-ran every criterion of TO-FB-e-1..7 as the orders state them, main checkout, HEAD e8145043c7, 2026-10-11T05:18Z",
        "python .tools/round-close-check.py --project ADVI_FIRMBKTS --round 2 --deep -> orders=7 proof_ok=7 judgment=0 verdict=MAY-CLOSE",
        "L8 packet org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/R2_CLOSE.md @27bd0e5f9e (blob ea663dd0ba); the working tree carries an UNCOMMITTED edit to its F6 bullet (blob 73657bd39d) -- this grade reads the pinned bytes"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard. The unmet independence clause is carried by D1-S3 (REMEDIATION_v2, OPEN)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:35:00Z",
    "one_line": "NEW: FB-e-5's compare re-run at 05:18Z reads COPY-NOT-COMPLETE (exit 1): DEST mismatch 1, SOURCE changed-since-manifest 1, key advi/49financial/platinum/views/client_tax_liability.parquet. The destination is CORRECT for its snapshot: its bytes equal the source version the manifest names (opal-data-bd gold/views/client_tax_liability.parquet version wefvwm7u.., 11,392,210 bytes, multipart ETag 8edee8b4..-2), sha256 7a22e8315a5afbce on both. A producer rewrote the source at 05:10:08Z (version LUlNN5O_.., 10,989,932 bytes), three minutes after the issuer's COPY-COMPLETE read at 05:07Z. Two things follow. (1) D1-S4 is REALIZED, measured: the copy went stale within minutes of the close. (2) An instrument defect: when ETags differ in form (multipart source, single-part copy) r2_f7.py compare (lines 264-276) decides equality by hashing the CURRENT source object, not the manifest's version, so source drift reads as a wrong destination. The source bucket is versioned, so the manifest's version is readable.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-S4"
    ],
    "spec_asserts": "TO-FB-e-5 AC2 expects COPY-COMPLETE: every manifest key present and equal. Row D1-S4: the copy is a snapshot and the producers still write the source.",
    "world_is": "NEW: FB-e-5's compare re-run at 05:18Z reads COPY-NOT-COMPLETE (exit 1): DEST mismatch 1, SOURCE changed-since-manifest 1, key advi/49financial/platinum/views/client_tax_liability.parquet. The destination is CORRECT for its snapshot: its bytes equal the source version the manifest names (opal-data-bd gold/views/client_tax_liability.parquet version wefvwm7u.., 11,392,210 bytes, multipart ETag 8edee8b4..-2), sha256 7a22e8315a5afbce on both. A producer rewrote the source at 05:10:08Z (version LUlNN5O_.., 10,989,932 bytes), three minutes after the issuer's COPY-COMPLETE read at 05:07Z. Two things follow. (1) D1-S4 is REALIZED, measured: the copy went stale within minutes of the close. (2) An instrument defect: when ETags differ in form (multipart source, single-part copy) r2_f7.py compare (lines 264-276) decides equality by hashing the CURRENT source object, not the manifest's version, so source drift reads as a wrong destination. The source bucket is versioned, so the manifest's version is readable.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO r2_f7.py compare --manifest deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/F7_MANIFEST.tsv.gz, 2026-10-11T05:18Z: COPY-NOT-COMPLETE, exit=1",
        "3.0.0_SA_CVO .tools/aws s3api list-object-versions opal-data-bd gold/views/client_tax_liability.parquet: latest LUlNN5O_ 05:10:08Z 10989932; prior wefvwm7u 00:10:57Z 11392210 8edee8b4..-2",
        "3.0.0_SA_CVO get-object of that prior version and of the destination key: sha256 7a22e8315a5afbce8dfc30ba19cb9fb7bdb0196650a8dd7e89ec36a224ed0c1b on both",
        "deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py:264-276 (the multipart tie-break hashes SRC_BUCKET/src as it is now)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S8",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:35:00Z",
    "one_line": "D1-W7-S3, D1-W8-S1 and D1-W10-S1 (BLOCKING; W10-S1 ARMED) dismissed, resolved: the issuer renamed the seven proof instances to the order stem (e60140c2d2), amended the order paths (6f71f434ac), merged baaa2bbc81. This seat reads all seven orders <status>complete</status> with exactly one deliverables/*/<stem>.proof_of_spec.json each, and round-close-check --deep proof_ok 7 of 7. The disagreement between the two tools is carried by D1-S10 (graduated, C-S12).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W7-S3",
      "ADVI_FIRMBKTS-D1-W8-S1",
      "ADVI_FIRMBKTS-D1-W10-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W7-S3, D1-W8-S1 and D1-W10-S1 (BLOCKING; W10-S1 ARMED) dismissed, resolved: the issuer renamed the seven proof instances to the order stem (e60140c2d2), amended the order paths (6f71f434ac), merged baaa2bbc81. This seat reads all seven orders <status>complete</status> with exactly one deliverables/*/<stem>.proof_of_spec.json each, and round-close-check --deep proof_ok 7 of 7. The disagreement between the two tools is carried by D1-S10 (graduated, C-S12).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ls deliverables/*/<stem>.proof_of_spec.json for the 7 FB-e orders: 1 each; <status> complete x7",
        "round-close-check --deep -> PROOFS complete=7 proof_ok=7 proof_bad=0",
        "commits e60140c2d2, 6f71f434ac, baaa2bbc81 (issuer)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W7-S3, D1-W8-S1 and D1-W10-S1 (BLOCKING; W10-S1 ARMED) dismissed, resolved: the issuer renamed the seven proof instances to the order stem (e60140c2d2), amended the order paths (6f71f434ac), merged baaa2bbc81. This seat reads all seven orders <status>complete</status> with exactly one deliverables/*/<stem>.proof_of_spec.json each, and round-close-check --deep proof_ok 7 of 7. The disagreement between the two tools is carried by D1-S10 (graduated, C-S12)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S9",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:35:00Z",
    "one_line": "D1-W9-S3, D1-W9-S4 (BLOCKING) and D1-W7-S2 dismissed. W9-S3: the FB-e-6 flip landed (issuer, ce7f83772e) and the order reads complete. W9-S4: the v1 patch's naming refusal is superseded by the v3 re-cut (D1-S9) committed at e4224d8fe5; naming-gate.py --diff --enforce over the router diff fda1c4f0cc..HEAD reads PASS (2 paths seen, 0 graded) and index.mjs:128 carries CANONICAL_PLATINUM_BUCKETS = Object.freeze([]). W7-S2: a newline-format difference between expect and output; this seat's re-run prints 3 of 3 and 4 of 4 with exit=0 and the order is complete.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W9-S3",
      "ADVI_FIRMBKTS-D1-W9-S4",
      "ADVI_FIRMBKTS-D1-W7-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W9-S3, D1-W9-S4 (BLOCKING) and D1-W7-S2 dismissed. W9-S3: the FB-e-6 flip landed (issuer, ce7f83772e) and the order reads complete. W9-S4: the v1 patch's naming refusal is superseded by the v3 re-cut (D1-S9) committed at e4224d8fe5; naming-gate.py --diff --enforce over the router diff fda1c4f0cc..HEAD reads PASS (2 paths seen, 0 graded) and index.mjs:128 carries CANONICAL_PLATINUM_BUCKETS = Object.freeze([]). W7-S2: a newline-format difference between expect and output; this seat's re-run prints 3 of 3 and 4 of 4 with exit=0 and the order is complete.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python .tools/naming-gate.py --diff <git diff fda1c4f0cc HEAD -- infra/aws/lambda-edge/shared-advisor-router/> --enforce -> NAMING-GATE: PASS 0 graded, rc=0",
        "infra/aws/lambda-edge/shared-advisor-router/index.mjs:128 at HEAD e8145043c7",
        "3.0.0_SA_CVO r2_f4.py --arms positive / --arms negative: 3 of 3, 4 of 4, exit=0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W9-S3, D1-W9-S4 (BLOCKING) and D1-W7-S2 dismissed. W9-S3: the FB-e-6 flip landed (issuer, ce7f83772e) and the order reads complete. W9-S4: the v1 patch's naming refusal is superseded by the v3 re-cut (D1-S9) committed at e4224d8fe5; naming-gate.py --diff --enforce over the router diff fda1c4f0cc..HEAD reads PASS (2 paths seen, 0 graded) and index.mjs:128 carries CANONICAL_PLATINUM_BUCKETS = Object.freeze([]). W7-S2: a newline-format difference between expect and output; this seat's re-run prints 3 of 3 and 4 of 4 with exit=0 and the order is complete."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S10",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:35:00Z",
    "one_line": "D1-W4-S1 (BLOCKING), D1-S5, D1-S6 and D1-S8 dismissed. D1-S8: the disarm owner's placement record for D1-S4 and D1-S7 (one round-3 cutover window); the family it orders is carried by their remediation rows (C-S11). W4-S1: both cot positions_cube rows in mapping_v2.json read FAULT, owner 1.0.0_SA_CTO~DELL1, reason 'destination-key overlap 342 of 342 keys' (issuer ruling 2ca0be7c81 applied in FB-e-1); repair arm P2 PASSES on this seat's run (28 of 28 collisions ruled). D1-S5: the SSM route it named was the one used; N1 and N2 pass on the saved record. D1-S6: the S11 cell is the tolerant load as the row says; FB-e-7 AC1-AC3 pass on this seat's run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W4-S1",
      "ADVI_FIRMBKTS-D1-S5",
      "ADVI_FIRMBKTS-D1-S6",
      "ADVI_FIRMBKTS-D1-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W4-S1 (BLOCKING), D1-S5, D1-S6 and D1-S8 dismissed. D1-S8: the disarm owner's placement record for D1-S4 and D1-S7 (one round-3 cutover window); the family it orders is carried by their remediation rows (C-S11). W4-S1: both cot positions_cube rows in mapping_v2.json read FAULT, owner 1.0.0_SA_CTO~DELL1, reason 'destination-key overlap 342 of 342 keys' (issuer ruling 2ca0be7c81 applied in FB-e-1); repair arm P2 PASSES on this seat's run (28 of 28 collisions ruled). D1-S5: the SSM route it named was the one used; N1 and N2 pass on the saved record. D1-S6: the S11 cell is the tolerant load as the row says; FB-e-7 AC1-AC3 pass on this seat's run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read of deliverables/mapping_v2.json rows (opal-data-cot, gold/positions_cube/) and (opal-data-cot, gold/timeseries/positions_cube/)",
        "3.0.0_SA_CVO r2_mapping.py --arms repair: P2 PASS, ROUND 2 MAPPING REPAIR: 4 of 4 arms",
        "3.0.0_SA_CVO FB-e-7 AC1 3 passed, AC2 S11 NAMING GATE PASS, AC3 12 passed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W4-S1 (BLOCKING), D1-S5, D1-S6 and D1-S8 dismissed. D1-S8: the disarm owner's placement record for D1-S4 and D1-S7 (one round-3 cutover window); the family it orders is carried by their remediation rows (C-S11). W4-S1: both cot positions_cube rows in mapping_v2.json read FAULT, owner 1.0.0_SA_CTO~DELL1, reason 'destination-key overlap 342 of 342 keys' (issuer ruling 2ca0be7c81 applied in FB-e-1); repair arm P2 PASSES on this seat's run (28 of 28 collisions ruled). D1-S5: the SSM route it named was the one used; N1 and N2 pass on the saved record. D1-S6: the S11 cell is the tolerant load as the row says; FB-e-7 AC1-AC3 pass on this seat's run."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S11",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:35:00Z",
    "one_line": "D1-S4 and D1-S7 (ARMED) move to INERT under the disarm owner's row D1-S8 and are GRADUATED to 1.0.0_SA_CTO~DELL1 as the round-3 cutover family (D1-S8 itself is dismissed in C-S10 as that ruling's record); D1-S9 graduates beside them. Read here: F6 is dormant at HEAD (empty CANONICAL_PLATINUM_BUCKETS), so a deploy alone changes no request. NOT read here: the deployed edge function's bytes, and whether anything reads advi/49financial/platinum/ (CTO half, condition 2). D1-S4 is now measured realized (C-S7). D1-S9 matters to the family: the v3 patch made activation need a list entry AND the map value, while D1-S8's step (4) names only the map value.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-S4",
      "ADVI_FIRMBKTS-D1-S7",
      "ADVI_FIRMBKTS-D1-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S4 and D1-S7 (ARMED) move to INERT under the disarm owner's row D1-S8 and are GRADUATED to 1.0.0_SA_CTO~DELL1 as the round-3 cutover family (D1-S8 itself is dismissed in C-S10 as that ruling's record); D1-S9 graduates beside them. Read here: F6 is dormant at HEAD (empty CANONICAL_PLATINUM_BUCKETS), so a deploy alone changes no request. NOT read here: the deployed edge function's bytes, and whether anything reads advi/49financial/platinum/ (CTO half, condition 2). D1-S4 is now measured realized (C-S7). D1-S9 matters to the family: the v3 patch made activation need a list entry AND the map value, while D1-S8's step (4) names only the map value.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D1-S4, D1-S7, D1-S8 (1.0.0_SA_CTO~DELL1, the disarm), D1-S9",
        "index.mjs:128 at HEAD e8145043c7: Object.freeze([])",
        "row ADVI_FIRMBKTS-D1-C-S7 (the copy stale at 05:10:08Z)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S12",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:35:00Z",
    "one_line": "GRADUATED INERT, by owner. To 2.0.0_SA_COO~B1 (the cut template): D1-W9-S2 (ARMED until now; INERT for this round because the order is terminal and the merged main checkout reads the worktree's 39 pass), D1-W9-S5 and D1-W4-S7, the same cwd trap: an invocation's cd \"$(git rev-parse --show-toplevel)\" resolves the call-start checkout, and the false reading looks like a pass; and D1-W7-S1: F4's difference control N4 passes on the absence of the deny phrase while the cottonwood read was refused anyway, by an identity-side implicit deny, so the fence's admit of its own firm is policy text only. To 1.0.0_SA_CTO~DELL1: D1-S10 (round-close-check and to-pipeline-gate find a proof instance by different rules; the gate owners are this fabric's CTO and 0.0.0_AB_MSTR~Z by last commit), D1-W9-S1 (5 non-ASCII comment lines pre-existing in the router, to be decided at F6's deploy), and D1-W4-S2..S6 (the grain questions behind the 89 FAULT classes, all owned by the CTO in mapping_v2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W9-S2",
      "ADVI_FIRMBKTS-D1-W9-S5",
      "ADVI_FIRMBKTS-D1-W4-S7",
      "ADVI_FIRMBKTS-D1-W7-S1",
      "ADVI_FIRMBKTS-D1-S10",
      "ADVI_FIRMBKTS-D1-W9-S1",
      "ADVI_FIRMBKTS-D1-W4-S2",
      "ADVI_FIRMBKTS-D1-W4-S3",
      "ADVI_FIRMBKTS-D1-W4-S4",
      "ADVI_FIRMBKTS-D1-W4-S5",
      "ADVI_FIRMBKTS-D1-W4-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED INERT, by owner. To 2.0.0_SA_COO~B1 (the cut template): D1-W9-S2 (ARMED until now; INERT for this round because the order is terminal and the merged main checkout reads the worktree's 39 pass), D1-W9-S5 and D1-W4-S7, the same cwd trap: an invocation's cd \"$(git rev-parse --show-toplevel)\" resolves the call-start checkout, and the false reading looks like a pass; and D1-W7-S1: F4's difference control N4 passes on the absence of the deny phrase while the cottonwood read was refused anyway, by an identity-side implicit deny, so the fence's admit of its own firm is policy text only. To 1.0.0_SA_CTO~DELL1: D1-S10 (round-close-check and to-pipeline-gate find a proof instance by different rules; the gate owners are this fabric's CTO and 0.0.0_AB_MSTR~Z by last commit), D1-W9-S1 (5 non-ASCII comment lines pre-existing in the router, to be decided at F6's deploy), and D1-W4-S2..S6 (the grain questions behind the 89 FAULT classes, all owned by the CTO in mapping_v2).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows as listed",
        "3.0.0_SA_CVO F6 AC1 from the main checkout at HEAD: 39 pass, 0 fail, 3 files (equal to the worktree reading)",
        "git log -1 .tools/round-close-check.py -> a163c61b93 0.0.0_AB_MSTR~Z; .tools/to-pipeline-gate.py -> 8fff05ca26 1.0.0_SA_CTO",
        "r2_mapping.py --arms repair: FAULT rows remaining=89 owners={1.0.0_SA_CTO~DELL1: 89}"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S13",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T05:35:00Z",
    "one_line": "Round-1 remediations re-read against their close conditions (REMEDIATION_v2). CLOSED: D1-W1-S2 (each of the 89 remaining FAULT rows carries a named owner, P1 PASS); D1-W1-S3 (0 unruled collisions, 28 of 28 ruled with a measured overlap of 0; the copy commit 7a8a5fc00b does NOT descend from the table commit bdb2413a64, so the check did not run before the copy, but the manifest's 11 classes re-verified against mapping_v2 at HEAD place 52,910 keys with 0 destination collisions, so nothing interleaved; round 3's delta copy reads the final table); S11 (FB-e-7 merged the tolerant load; the literal rename was already done by ADVI_COTBKF, D1-S6). STAY OPEN: D1-S3 (table agreement 197 of 209, not 209; independence not exercised); D1-S1 (the refusal is now EXERCISED, N3; the PRD's F4 wording is unamended at prd_version v1.3, the CTO's limb); D1-S2 (no addendum or ruling yet).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W1-S2",
      "ADVI_FIRMBKTS-D1-W1-S3",
      "ADVI_FIRMBKTS-S11"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Round-1 remediations re-read against their close conditions (REMEDIATION_v2). CLOSED: D1-W1-S2 (each of the 89 remaining FAULT rows carries a named owner, P1 PASS); D1-W1-S3 (0 unruled collisions, 28 of 28 ruled with a measured overlap of 0; the copy commit 7a8a5fc00b does NOT descend from the table commit bdb2413a64, so the check did not run before the copy, but the manifest's 11 classes re-verified against mapping_v2 at HEAD place 52,910 keys with 0 destination collisions, so nothing interleaved; round 3's delta copy reads the final table); S11 (FB-e-7 merged the tolerant load; the literal rename was already done by ADVI_COTBKF, D1-S6). STAY OPEN: D1-S3 (table agreement 197 of 209, not 209; independence not exercised); D1-S1 (the refusal is now EXERCISED, N3; the PRD's F4 wording is unamended at prd_version v1.3, the CTO's limb); D1-S2 (no addendum or ruling yet).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediations/REMEDIATION_v2.md remedies (close conditions) read in full",
        "3.0.0_SA_CVO git merge-base --is-ancestor bdb2413a64 7a8a5fc00b -> not an ancestor",
        "3.0.0_SA_CVO r2_f7.py manifest --verify: objects=52910 classes=11 placed=52910 destination-collisions=0, VERIFIED",
        "prd/ADVI_FIRMBKTS_PRD.md prd_version v1.3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Close conditions met as stated; the three entries are advanced in REMEDIATION_v2 by the in-place clock (remediation.state OPEN to REMEDIATED, closed false to true)."
  }
]
```
