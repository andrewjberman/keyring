# ADVI_FIRMBKTS -- round 5 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-13T07:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T07:40:00Z. L8 packet: 2.0.0_SA_COO~B1 msg 4682, `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/R5_CLOSE.md` @03fd62aa85 (blob 5a0743fc39).
8 orders: 7 complete, FB-h-5 parked by the CTO's ruling. round-close-check --round 5: proof_ok 7, judgment 0, MAY-CLOSE.

**L9:** 14 of 14 criteria match on this seat's runs; act 2 and the validator read live (D1-C-S38). FWD-1: 11 of 11 reproduced, but
150 of 150 only as a composite of two faces -- PARTIAL (D1-C-S39). S32 re-computed EQUAL (D1-C-S41). FWD-4 PARTIAL (live half).

**L10:** precondition met (D1-C-S40).

**Rows:** 20 undispositioned since v5's watermark: 9 dismissed, 11 graduated to `remediations/REMEDIATION_v6.md` (6 to
1.0.0_SA_CTO~DELL1, 2 to 2.0.0_SA_COO~B1, 3 to 0.0.0_AB_MSTR; D1-W65-S1 and D1-W66-S2 stay ARMED). REMEDIATION_v5: D1-C-S33,
D1-S28 and D1-S40 REMEDIATED (D1-C-S44).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-C-S38",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T07:40:00Z",
    "one_line": "ROUND 5 L9 (packet org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/R5_CLOSE.md @03fd62aa85, blob 5a0743fc39, 10,086 bytes). Every criterion of the 7 complete orders re-run by this seat, 14 of 14 matching: 7 at the merged HEAD (FB-h-3 AC2, FB-h-4 AC1 and AC2, FB-h-6 AC1, FB-h-7 AC1, FB-h-8 AC1 and AC2); FB-h-1 and FB-h-2 4 of 4 each in their reader directories; FB-h-3 AC1's replay on ownership maps this seat fetched fresh from S3 (legacy 2026-10-12T05:22:13Z, canonical 2026-10-13T05:24:07Z, 474,841 B each, equal except generated_at): REPLAY pairs=2127 mismatches=0 control_mismatches=1 accounts=1501 relationships=626; the four write-surface arms (FB-h-3 AC3, FB-h-4 AC3, FB-h-6 AC2, FB-h-7 AC2) OK over each worker's own commits. FB-h-5 is parked (D1-C-S40). Applied state read live: act 2 -- NEW HOME 11 of 11 classes written since 2026-10-13T03:30Z, OLD HOME QUIET 0 keys since MOVE_TS; the validator v23 census over 7 of 17 regions since 2026-10-12T15:15:10Z, this seat's own read at 07:25Z: 9,136 lines, 17 on the accounts or relationship paths, all tier=internal, 0 non-admin, the last at 01:25:51Z -- FB-h-5's un-park condition is unmet. auth-validator-edge's spec reads 7 pass 0 fail at HEAD; the fence instrument runs to its last line (no traceback) and reads ok=False (D1-S43). Round 5 wrote nothing to AWS. FWD-4 stays PARTIAL: the offline half holds on this seat's replay; the live half (a non-admin line) is not exercised.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "ROUND 5 L9 (packet org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/R5_CLOSE.md @03fd62aa85, blob 5a0743fc39, 10,086 bytes). Every criterion of the 7 complete orders re-run by this seat, 14 of 14 matching: 7 at the merged HEAD (FB-h-3 AC2, FB-h-4 AC1 and AC2, FB-h-6 AC1, FB-h-7 AC1, FB-h-8 AC1 and AC2); FB-h-1 and FB-h-2 4 of 4 each in their reader directories; FB-h-3 AC1's replay on ownership maps this seat fetched fresh from S3 (legacy 2026-10-12T05:22:13Z, canonical 2026-10-13T05:24:07Z, 474,841 B each, equal except generated_at): REPLAY pairs=2127 mismatches=0 control_mismatches=1 accounts=1501 relationships=626; the four write-surface arms (FB-h-3 AC3, FB-h-4 AC3, FB-h-6 AC2, FB-h-7 AC2) OK over each worker's own commits. FB-h-5 is parked (D1-C-S40). Applied state read live: act 2 -- NEW HOME 11 of 11 classes written since 2026-10-13T03:30Z, OLD HOME QUIET 0 keys since MOVE_TS; the validator v23 census over 7 of 17 regions since 2026-10-12T15:15:10Z, this seat's own read at 07:25Z: 9,136 lines, 17 on the accounts or relationship paths, all tier=internal, 0 non-admin, the last at 01:25:51Z -- FB-h-5's un-park condition is unmet. auth-validator-edge's spec reads 7 pass 0 fail at HEAD; the fence instrument runs to its last line (no traceback) and reads ok=False (D1-S43). Round 5 wrote nothing to AWS. FWD-4 stays PARTIAL: the offline half holds on this seat's replay; the live half (a non-admin line) is not exercised.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO runall5.py at HEAD; r5_fwd1.py reader --reader A|B in the reader directories; bun replay_harness.mjs on maps fetched fresh (s3api get-object x2, deleted after); scope over each worker's authored commits (~63: b39d4a70f6..f46adfdeb0, ~64: b39d4a70f6..b5d6fc5208, ~65: ecfb64dcf4..400a39417a, ~66: ecfb64dcf4..0786e05f9a)",
        "3.0.0_SA_CVO r3_act2_reads.py new-home --since 2026-10-13T03:30:00Z and old-home --since 2026-10-12T06:22:08Z",
        "3.0.0_SA_CVO vlines.py: describe-log-groups x17 regions, filter-log-events /aws/lambda/us-east-1.auth-validator-edge since 2026-10-12T15:15:10Z, 2026-10-13T07:25Z",
        "3.0.0_SA_CVO bun test auth-validator-edge at HEAD: 7 pass 0 fail; python check_fence_scoped_rows.py: runs to its last line, ok=False"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record; FWD-4's live half is carried by D1-S41 (graduated) and D1-C-S37."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S39",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T07:40:00Z",
    "one_line": "FWD-1 re-read. This seat's own count over C:/dev/wk-firmbkts-r5-reader-{a,b}/ANSWERS_{A,B}.json and round5/READING_KEY.json (readers 0.9.0_WK_ADVI_FIRMBKTS~61 and ~62, 22 locations): the 11 round-4 disagreements (all 11 r4 ids covered) agree on all four fields and both equal the key, 11 of 11; the 11 controls 11 of 11. Both trees hold only .git, LOCATIONS.json and the answers file, git ls-files lists LOCATIONS.json alone, one commit 110cfbe34b. Does this move FWD-1 from 139 of 150 to 150 of 150? ONLY AS A COMPOSITE of two reads under two faces: 139 under the round-4 face and 11 under the round-5 face, which now STATES the table rule. No single blind read of the 150 under one face exists, and 128 of the 139 were not re-read under the new face (the 11 controls show no regression on a sample only). The issuer's own text says the fix makes agreement hold by construction for a reader that obeys the stated rule, which shows the rule is learnable, not that two readers reach it unprompted. Independence is unchanged: by construction, subagents of the issuing session on one model. FWD-1 stays PARTIAL; D1-S3 stays OPEN. The step that would close the agreement limb: one blind read of all 150 under the stated face.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ADVI_FIRMBKTS PRD FWD-1 ACCEPT.",
    "world_is": "FWD-1 re-read. This seat's own count over C:/dev/wk-firmbkts-r5-reader-{a,b}/ANSWERS_{A,B}.json and round5/READING_KEY.json (readers 0.9.0_WK_ADVI_FIRMBKTS~61 and ~62, 22 locations): the 11 round-4 disagreements (all 11 r4 ids covered) agree on all four fields and both equal the key, 11 of 11; the 11 controls 11 of 11. Both trees hold only .git, LOCATIONS.json and the answers file, git ls-files lists LOCATIONS.json alone, one commit 110cfbe34b. Does this move FWD-1 from 139 of 150 to 150 of 150? ONLY AS A COMPOSITE of two reads under two faces: 139 under the round-4 face and 11 under the round-5 face, which now STATES the table rule. No single blind read of the 150 under one face exists, and 128 of the 139 were not re-read under the new face (the 11 controls show no regression on a sample only). The issuer's own text says the fix makes agreement hold by construction for a reader that obeys the stated rule, which shows the rule is learnable, not that two readers reach it unprompted. Independence is unchanged: by construction, subagents of the issuing session on one model. FWD-1 stays PARTIAL; D1-S3 stays OPEN. The step that would close the agreement limb: one blind read of all 150 under the stated face.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO own count over the round-5 answers, key and FWD1_R4_DISAGREEMENTS.json (11 of 11 r4 ids)",
        "3.0.0_SA_CVO ls -A / git ls-files / git log on C:/dev/wk-firmbkts-r5-reader-a and -b",
        "deliverables/2.0.0_SA_COO~B1/round5/RULING_FWD1_R5.md; R5_CLOSE.md 'FWD-1, stated for the CVO'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A re-read record; D1-S3 stays OPEN."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S40",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T07:40:00Z",
    "one_line": "FB-h-5's park is a CTO ruling and is outside the verdict. ROUND_ANALYSIS.round4.md ADDENDUM 1 item 2 (1.0.0_SA_CTO~DELL1) directs it: if the walker's request does not give the non-admin read, 'the order parks with owner 1.0.0_SA_CTO~DELL1 and the un-park condition the first organic non-admin validator line on those paths'. The record face :98 parks it on exactly that branch (the walker reads role=admin, userType=Dev, row D1-S42); <status>parked</status> is outside the round under the CTO's standing ruling (ROUND4_5_ANALYSIS_MDPF_SECCLASS_20260930.md:20-21) and is a terminal word in both gates. round-close-check --round 5: 8 orders, 7 complete, proof_ok 7, judgment 0, MAY-CLOSE. Residual: the ruling's premise reads 'byte-equal maps'; they are equal except generated_at, and the replay shows equal decisions regardless.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "FB-h-5's park is a CTO ruling and is outside the verdict. ROUND_ANALYSIS.round4.md ADDENDUM 1 item 2 (1.0.0_SA_CTO~DELL1) directs it: if the walker's request does not give the non-admin read, 'the order parks with owner 1.0.0_SA_CTO~DELL1 and the un-park condition the first organic non-admin validator line on those paths'. The record face :98 parks it on exactly that branch (the walker reads role=admin, userType=Dev, row D1-S42); <status>parked</status> is outside the round under the CTO's standing ruling (ROUND4_5_ANALYSIS_MDPF_SECCLASS_20260930.md:20-21) and is a terminal word in both gates. round-close-check --round 5: 8 orders, 7 complete, proof_ok 7, judgment 0, MAY-CLOSE. Residual: the ruling's premise reads 'byte-equal maps'; they are equal except generated_at, and the replay shows equal decisions regardless.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round4.md:63-80 (ADDENDUM 1)",
        "task-orders/ADVI_FIRMBKTS.TO-FB-h-5.validator-live-read.md:98-100",
        "python .tools/round-close-check.py --project ADVI_FIRMBKTS --round 5: MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The L10 record: the precondition holds."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S41",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T07:40:00Z",
    "one_line": "S32 re-computed by this seat with its own code (extract_t1_prices as written at bd_price_update.py:327-345, then again after drop_duplicates on transaction_id; a move counts when |delta| > 1e-6), over the 20 weekday partitions of s3://opal-data-bd/silver/transactions/ 2026-09-16..2026-10-13 fetched fresh (LastModified 2026-09-27T00:13Z..2026-10-13T00:14Z; 740,698 rows; 2 zero-row partitions): asset-days 5,366, medians that move 830, assets 450, max delta 753.5. EQUAL to the record (PRICING_QUANT.json S32). The price x quantity amount is still not computed. The fetched files were deleted after the count.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "S32 re-computed by this seat with its own code (extract_t1_prices as written at bd_price_update.py:327-345, then again after drop_duplicates on transaction_id; a move counts when |delta| > 1e-6), over the 20 weekday partitions of s3://opal-data-bd/silver/transactions/ 2026-09-16..2026-10-13 fetched fresh (LastModified 2026-09-27T00:13Z..2026-10-13T00:14Z; 740,698 rows; 2 zero-row partitions): asset-days 5,366, medians that move 830, assets 450, max delta 753.5. EQUAL to the record (PRICING_QUANT.json S32). The price x quantity amount is still not computed. The fetched files were deleted after the count.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO s32.py (own code; 20 get-object reads, files deleted after)",
        "deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.json S32",
        "data/black_diamond/scripts/silver/bd_price_update.py:59, :327-345"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A re-computation record: S32 equals the record. D1-S32..S34 stay OPEN (the CRO brief)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S42",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T07:40:00Z",
    "one_line": "DISMISSED (9): D1-S42 (BLOCKING: the walker is an admin-bypass identity) is the ruling's second branch, applied, and is absorbed by D1-S41's remedy; D1-W63-S4 and D1-W66-S8 (BLOCKING: AC paths named in the base checkout) -- both criteria match at the merged HEAD on this seat's run (FB-h-3 AC2, FB-h-7 AC1); the class (an invocation that names the wrong tree) stays carried by REMEDIATION_v3 D1-W9-S2; D1-W64-S1 (mockadv shares the 49financial bucket; the spec was written to the registry); D1-W63-S2 (absorbed by W63-S1); D1-W63-S3 (the harness steps the 60 s cache); D1-W65-S2 (the 17-region sweep, read-only); D1-W66-S1 (the order's path; the file is under silver/); D1-W66-S4 (the account_gains versions rewritten 2026-09-27, recorded).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-S42",
      "ADVI_FIRMBKTS-D1-W63-S4",
      "ADVI_FIRMBKTS-D1-W66-S8",
      "ADVI_FIRMBKTS-D1-W64-S1",
      "ADVI_FIRMBKTS-D1-W63-S2",
      "ADVI_FIRMBKTS-D1-W63-S3",
      "ADVI_FIRMBKTS-D1-W65-S2",
      "ADVI_FIRMBKTS-D1-W66-S1",
      "ADVI_FIRMBKTS-D1-W66-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED (9): D1-S42 (BLOCKING: the walker is an admin-bypass identity) is the ruling's second branch, applied, and is absorbed by D1-S41's remedy; D1-W63-S4 and D1-W66-S8 (BLOCKING: AC paths named in the base checkout) -- both criteria match at the merged HEAD on this seat's run (FB-h-3 AC2, FB-h-7 AC1); the class (an invocation that names the wrong tree) stays carried by REMEDIATION_v3 D1-W9-S2; D1-W64-S1 (mockadv shares the 49financial bucket; the spec was written to the registry); D1-W63-S2 (absorbed by W63-S1); D1-W63-S3 (the harness steps the 60 s cache); D1-W65-S2 (the 17-region sweep, read-only); D1-W66-S1 (the order's path; the file is under silver/); D1-W66-S4 (the account_gains versions rewritten 2026-09-27, recorded).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row ADVI_FIRMBKTS-D1-C-S38 (the re-run record)",
        "investigation rows as listed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "DISMISSED (9): D1-S42 (BLOCKING: the walker is an admin-bypass identity) is the ruling's second branch, applied, and is absorbed by D1-S41's remedy; D1-W63-S4 and D1-W66-S8 (BLOCKING: AC paths named in the base checkout) -- both criteria match at the merged HEAD on this seat's run (FB-h-3 AC2, FB-h-7 AC1); the class (an invocation that names the wrong tree) stays carried by REMEDIATION_v3 D1-W9-S2; D1-W64-S1 (mockadv shares the 49financial bucket; the spec was written to the registry); D1-W63-S2 (absorbed by W63-S1); D1-W63-S3 (the harness steps the 60 s cache); D1-W65-S2 (the 17-region sweep, read-only); D1-W66-S1 (the order's path; the file is under silver/); D1-W66-S4 (the account_gains versions rewritten 2026-09-27, recorded)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S43",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T07:40:00Z",
    "one_line": "GRADUATED (11). To 1.0.0_SA_CTO~DELL1: D1-S41 (BLOCKING, INERT: FWD-4's live half, FB-h-5's un-park condition, 0 non-admin lines at 07:25Z); D1-W65-S1 (ARMED, stays ARMED: no PutEvents in CloudTrail in 17 regions over 90 days -- the exec summaries have been stale since 2026-05-04 and the cause is INDETERMINATE; the next act is a write that waits on the CTO) with D1-W65-S3 (the SCP read is denied); and the pricing evidence for the CRO brief, D1-W66-S3 (served transaction_observed prices differ from the current median on 603 of 1,610 rows), W66-S5 (no INFO step lines logged), W66-S6 (weekend partitions and two zero-row recent weekdays). To 2.0.0_SA_COO~B1: D1-W66-S2 (ARMED, stays ARMED, its named disarm owner: the B_01 same-date tie-break; inferred as of 10-09, 3,906 of 11,108 alternatives differ) and D1-W63-S1 (a worker probe reached the render-key Secrets Manager read outside its bound; the harness mock must cover that branch). To 0.0.0_AB_MSTR: D1-S43 (BLOCKING, INERT: the fence instrument's four re-baseline causes, routed to NFRA_CTLPLN by CTO msg 4674), D1-W64-S2 (the client-data check absent on this device, with D1-W35-S1) and D1-W66-S7 (the aws shim's WARN in a worktree).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-S41",
      "ADVI_FIRMBKTS-D1-W65-S1",
      "ADVI_FIRMBKTS-D1-W65-S3",
      "ADVI_FIRMBKTS-D1-W66-S3",
      "ADVI_FIRMBKTS-D1-W66-S5",
      "ADVI_FIRMBKTS-D1-W66-S6",
      "ADVI_FIRMBKTS-D1-W66-S2",
      "ADVI_FIRMBKTS-D1-W63-S1",
      "ADVI_FIRMBKTS-D1-S43",
      "ADVI_FIRMBKTS-D1-W64-S2",
      "ADVI_FIRMBKTS-D1-W66-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED (11). To 1.0.0_SA_CTO~DELL1: D1-S41 (BLOCKING, INERT: FWD-4's live half, FB-h-5's un-park condition, 0 non-admin lines at 07:25Z); D1-W65-S1 (ARMED, stays ARMED: no PutEvents in CloudTrail in 17 regions over 90 days -- the exec summaries have been stale since 2026-05-04 and the cause is INDETERMINATE; the next act is a write that waits on the CTO) with D1-W65-S3 (the SCP read is denied); and the pricing evidence for the CRO brief, D1-W66-S3 (served transaction_observed prices differ from the current median on 603 of 1,610 rows), W66-S5 (no INFO step lines logged), W66-S6 (weekend partitions and two zero-row recent weekdays). To 2.0.0_SA_COO~B1: D1-W66-S2 (ARMED, stays ARMED, its named disarm owner: the B_01 same-date tie-break; inferred as of 10-09, 3,906 of 11,108 alternatives differ) and D1-W63-S1 (a worker probe reached the render-key Secrets Manager read outside its bound; the harness mock must cover that branch). To 0.0.0_AB_MSTR: D1-S43 (BLOCKING, INERT: the fence instrument's four re-baseline causes, routed to NFRA_CTLPLN by CTO msg 4674), D1-W64-S2 (the client-data check absent on this device, with D1-W35-S1) and D1-W66-S7 (the aws shim's WARN in a worktree).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows as listed",
        "row ADVI_FIRMBKTS-D1-C-S38 (validator census)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S44",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T07:40:00Z",
    "one_line": "Remediations re-read. REMEDIATED in place (REMEDIATION_v5): D1-C-S33 (auth-validator-edge's spec reads 7 pass 0 fail at HEAD; FB-h-4 merged a579ab8193), D1-S28 (the fence instrument's cp1252 crash fixed at 38f8179f10 on the CTO's ruling; it runs to its last line), D1-S40 (the round-5 cut FB-h-6 names it; the diagnosis is INDETERMINATE and its cause is carried by D1-W65-S1). STAY OPEN: D1-C-S37 and REMEDIATION_v4 D1-S17 (the live non-admin read); D1-S32..S34 (the CRO brief); D1-C-S21 and D1-C-S34 (TO-FB-f-8 still carries 4 placeholder lines); D1-W60-S3; the tooling rows with 0.0.0_AB_MSTR; REMEDIATION_v3 D1-S7, D1-S10, D1-W9-S2, D1-W9-S5, D1-W4-S7; REMEDIATION_v2 D1-S1, D1-S2, D1-S3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-C-S33",
      "ADVI_FIRMBKTS-D1-S28",
      "ADVI_FIRMBKTS-D1-S40"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Remediations re-read. REMEDIATED in place (REMEDIATION_v5): D1-C-S33 (auth-validator-edge's spec reads 7 pass 0 fail at HEAD; FB-h-4 merged a579ab8193), D1-S28 (the fence instrument's cp1252 crash fixed at 38f8179f10 on the CTO's ruling; it runs to its last line), D1-S40 (the round-5 cut FB-h-6 names it; the diagnosis is INDETERMINATE and its cause is carried by D1-W65-S1). STAY OPEN: D1-C-S37 and REMEDIATION_v4 D1-S17 (the live non-admin read); D1-S32..S34 (the CRO brief); D1-C-S21 and D1-C-S34 (TO-FB-f-8 still carries 4 placeholder lines); D1-W60-S3; the tooling rows with 0.0.0_AB_MSTR; REMEDIATION_v3 D1-S7, D1-S10, D1-W9-S2, D1-W9-S5, D1-W4-S7; REMEDIATION_v2 D1-S1, D1-S2, D1-S3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO bun test (auth-validator-edge) and check_fence_scoped_rows.py at HEAD",
        "task-orders/ADVI_FIRMBKTS.TO-FB-h-6.exec-summary-diagnosis.md (names D1-S40)",
        "3.0.0_SA_CVO grep -c '<ROUTER_VERSION>|<ROUTER_SHA256>|<WAF_ACL_NAME>' TO-FB-f-8: 4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Close conditions met as stated; the three rows advance in place by remediation.state and closed only."
  }
]
```
