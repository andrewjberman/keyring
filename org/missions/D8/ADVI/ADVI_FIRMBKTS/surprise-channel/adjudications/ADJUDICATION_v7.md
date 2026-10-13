# ADVI_FIRMBKTS -- round 6 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-13T08:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T08:20:00Z. L8 packet: 2.0.0_SA_COO~B1 msg 4701, `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round6/R6_CLOSE.md` @3739c12b01 (blob ddf67622c3).
2 orders, 2 complete. round-close-check --round 6: proof_ok 2, judgment 0, MAY-CLOSE.

**L9:** FWD-1 -- one fresh reader, one face, 150 of 150 equal to the key, reproduced: correctness MET; the PRD's agreement arm
('two people ... and they agree') still needs a second reader, so FWD-1 stays PARTIAL (D1-C-S45). FB-i-2 -- REGION_UNSET is an
inference the code supports; the cause is not measured (D1-C-S46).

**L10:** precondition met (D1-C-S47). **Rows:** 1 undispositioned since v6's watermark, D1-S44, graduated (D1-C-S48).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-C-S45",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T08:20:00Z",
    "one_line": "ROUND 6 L9, FWD-1 (packet org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round6/R6_CLOSE.md @3739c12b01, blob ddf67622c3, 5,917 bytes). FB-i-1 AC1 re-run: ROUND 6 READER 4 of 4. Reproduced from the reader's own C:/dev/wk-firmbkts-r6-reader/ANSWERS.json against round6/READING_KEY.json: reader 0.9.0_WK_ADVI_FIRMBKTS~67, 150 answers; system, firm, tier and table each equal the key 150 of 150, all four 150 of 150, unknown 0; the 150 are exactly round 4's canonical classes under fresh ids. Fresh: ~67 has 0 commits on any ref (it authored neither earlier read: ~27, ~28, ~61, ~62); its face is marked 'the WHOLE of the worker's context', says 'you have never seen these locations', and forbids reading any other reader's answers; the tree holds only .git, LOCATIONS.json and ANSWERS.json, git ls-files lists LOCATIONS.json alone, one commit 80ff50f2f5. It saw the table rule: the face states it (TO-FB-i-1 :49-52, 'the ONE path component immediately after the tier component'). The PRD's clause (ADVI_FIRMBKTS_PRD.md ENDPOINT FWD-1 ACCEPT): 'two people who have never worked together read the same list of storage locations and each says, for every one, which system made it, which firm it belongs to, how finished it is and what it holds -- and they agree'. Verdict. The single-face objection of round 5 is answered: one reader, one face, all 150, equal to the key. That MEETS correctness on all four fields for the 150. It does NOT meet the clause's agreement arm as the PRD writes it: the clause is two readers who each answer and agree with EACH OTHER; the key is not a second reader -- it is the mapping, written by the issuing seat, so equality to it is agreement with the table's author, not with a person who never worked with the first. Independence needs a second fresh reader under the same face over the same 150; built the same way, that pair would still be two subagents of one session on one model, which is the by-construction residual the CTO has accepted since round 3. FWD-1 stays PARTIAL on the agreement arm alone; correctness is MET. The step that closes it: a second fresh reader (authored no read) over the same 150 under the same face, its answers compared with ~67's -- or the CTO's ruling that one fresh reader equal to the key satisfies 'they agree'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ADVI_FIRMBKTS PRD FWD-1 ACCEPT: 'two people who have never worked together read the same list of storage locations and each says, for every one, which system made it, which firm it belongs to, how finished it is and what it holds -- and they agree'.",
    "world_is": "ROUND 6 L9, FWD-1 (packet org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round6/R6_CLOSE.md @3739c12b01, blob ddf67622c3, 5,917 bytes). FB-i-1 AC1 re-run: ROUND 6 READER 4 of 4. Reproduced from the reader's own C:/dev/wk-firmbkts-r6-reader/ANSWERS.json against round6/READING_KEY.json: reader 0.9.0_WK_ADVI_FIRMBKTS~67, 150 answers; system, firm, tier and table each equal the key 150 of 150, all four 150 of 150, unknown 0; the 150 are exactly round 4's canonical classes under fresh ids. Fresh: ~67 has 0 commits on any ref (it authored neither earlier read: ~27, ~28, ~61, ~62); its face is marked 'the WHOLE of the worker's context', says 'you have never seen these locations', and forbids reading any other reader's answers; the tree holds only .git, LOCATIONS.json and ANSWERS.json, git ls-files lists LOCATIONS.json alone, one commit 80ff50f2f5. It saw the table rule: the face states it (TO-FB-i-1 :49-52, 'the ONE path component immediately after the tier component'). The PRD's clause (ADVI_FIRMBKTS_PRD.md ENDPOINT FWD-1 ACCEPT): 'two people who have never worked together read the same list of storage locations and each says, for every one, which system made it, which firm it belongs to, how finished it is and what it holds -- and they agree'. Verdict. The single-face objection of round 5 is answered: one reader, one face, all 150, equal to the key. That MEETS correctness on all four fields for the 150. It does NOT meet the clause's agreement arm as the PRD writes it: the clause is two readers who each answer and agree with EACH OTHER; the key is not a second reader -- it is the mapping, written by the issuing seat, so equality to it is agreement with the table's author, not with a person who never worked with the first. Independence needs a second fresh reader under the same face over the same 150; built the same way, that pair would still be two subagents of one session on one model, which is the by-construction residual the CTO has accepted since round 3. FWD-1 stays PARTIAL on the agreement arm alone; correctness is MET. The step that closes it: a second fresh reader (authored no read) over the same 150 under the same face, its answers compared with ~67's -- or the CTO's ruling that one fresh reader equal to the key satisfies 'they agree'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO r6_fwd1.py reader --dir C:/dev/wk-firmbkts-r6-reader: ROUND 6 READER 4 of 4",
        "3.0.0_SA_CVO own count over ANSWERS.json and round6/READING_KEY.json; classes compared with round4/READING_KEY.json canonical arm",
        "3.0.0_SA_CVO git log --all --author='0.9.0_WK_ADVI_FIRMBKTS~67': 0 commits; ls -A, git ls-files, git log on the reader tree",
        "task-orders/ADVI_FIRMBKTS.TO-FB-i-1.reader-150.md :3, :29, :49-52, :56, :102-103",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md ENDPOINT FWD-1 ACCEPT"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record; the agreement arm is carried by REMEDIATION_v2 D1-S3 (OPEN)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S46",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T08:20:00Z",
    "one_line": "ROUND 6 L9, FB-i-2 (the emit path). AC1 re-run: RUNNER record ok calls=17 verdict=REGION_UNSET test_event_sent=False. Graded as an INFERENCE; the cause is NOT measured -- no record on the runner names the exception, and no probe was sent. The code supports the inference: data/black_diamond/scripts/gold/gold_dispatch.sh:850 runs 'aws events put-events --entries file://...' with no --region, its output piped to 'grep -q' (the CLI's error text is discarded, so the WARN at :853 is all that is logged); the dispatcher names no --region, AWS_DEFAULT_REGION, AWS_REGION or aws configure anywhere (0 matches), nor do the runner's boot files in the repository (bd-gold-layer-runner run-gold-layer.sh, setup-instance.sh, user-data.sh: 0 each); the regional put-metric-data calls (:1346, :1598, :1604) carry no region either, while the global cloudfront create-invalidation (:1479) needs none -- which is the control FB1 read (the global call prints OK on 4 of 4 chains; BD/GoldRunner holds 0 metrics). The CLI resolves a region from --region, the environment or ~/.aws/config; the first two are absent from every path read, and the third, the runner's own config file, was not read (SSM is barred on the runner, row D1-S44). So REGION_UNSET is the code-consistent reading, not a measurement.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "ROUND 6 L9, FB-i-2 (the emit path). AC1 re-run: RUNNER record ok calls=17 verdict=REGION_UNSET test_event_sent=False. Graded as an INFERENCE; the cause is NOT measured -- no record on the runner names the exception, and no probe was sent. The code supports the inference: data/black_diamond/scripts/gold/gold_dispatch.sh:850 runs 'aws events put-events --entries file://...' with no --region, its output piped to 'grep -q' (the CLI's error text is discarded, so the WARN at :853 is all that is logged); the dispatcher names no --region, AWS_DEFAULT_REGION, AWS_REGION or aws configure anywhere (0 matches), nor do the runner's boot files in the repository (bd-gold-layer-runner run-gold-layer.sh, setup-instance.sh, user-data.sh: 0 each); the regional put-metric-data calls (:1346, :1598, :1604) carry no region either, while the global cloudfront create-invalidation (:1479) needs none -- which is the control FB1 read (the global call prints OK on 4 of 4 chains; BD/GoldRunner holds 0 metrics). The CLI resolves a region from --region, the environment or ~/.aws/config; the first two are absent from every path read, and the third, the runner's own config file, was not read (SSM is barred on the runner, row D1-S44). So REGION_UNSET is the code-consistent reading, not a measurement.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO r6_checks.py runner --file deliverables/0.7.0_AE_CloudOps~FB1/RUNNER_EMIT_READ.json",
        "3.0.0_SA_CVO grep -n 'put-events|put-metric-data|create-invalidation|--region|AWS_DEFAULT_REGION|AWS_REGION|aws configure' gold_dispatch.sh",
        "3.0.0_SA_CVO grep -c region settings over infra/aws/ec2/*/run-gold-layer.sh, setup-instance.sh, user-data.sh: 0 each"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An inference record; the cause is carried by REMEDIATION_v6 D1-W65-S1 (ARMED) and D1-S44."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S47",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T08:20:00Z",
    "one_line": "L10 PRECONDITION MET. round-close-check --project ADVI_FIRMBKTS --round 6: 2 orders, 2 complete, proof_ok 2, judgment 0, MAY-CLOSE. Every BLOCKING and ARMED row is dispositioned: the packet's list (D1-W65-S1, D1-W66-S2, D1-S41, D1-S42) was dispositioned at ADJUDICATION_v6 and is unchanged (D1-W65-S1 and D1-W66-S2 stay ARMED with their owners; the round-7 emit fix is D1-W65-S1's disarm); D1-S44 is the one new row (C-S48).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L10 PRECONDITION MET. round-close-check --project ADVI_FIRMBKTS --round 6: 2 orders, 2 complete, proof_ok 2, judgment 0, MAY-CLOSE. Every BLOCKING and ARMED row is dispositioned: the packet's list (D1-W65-S1, D1-W66-S2, D1-S41, D1-S42) was dispositioned at ADJUDICATION_v6 and is unchanged (D1-W65-S1 and D1-W66-S2 stay ARMED with their owners; the round-7 emit fix is D1-W65-S1's disarm); D1-S44 is the one new row (C-S48).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/round-close-check.py --project ADVI_FIRMBKTS --round 6: MAY-CLOSE",
        "adjudications/ADJUDICATION_v6.md D1-C-S42, D1-C-S43"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The L10 record."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S48",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T08:20:00Z",
    "one_line": "GRADUATED to 1.0.0_SA_CTO~DELL1: D1-S44 (the emit's cause reads REGION_UNSET, inferred, no exception text in any record; the order's probe step collided with the runner's EC2_MANIFEST, which bars SSM commands; PutEvents's CloudTrail class was never controlled). It travels with D1-W65-S1 (REMEDIATION_v6, ARMED) into the round-7 fix cell under a never-widen pair; the fix regenerates up to 158 client-facing summaries and starts the BD/GoldRunner metrics, so it is a served change.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-S44"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to 1.0.0_SA_CTO~DELL1: D1-S44 (the emit's cause reads REGION_UNSET, inferred, no exception text in any record; the order's probe step collided with the runner's EC2_MANIFEST, which bars SSM commands; PutEvents's CloudTrail class was never controlled). It travels with D1-W65-S1 (REMEDIATION_v6, ARMED) into the round-7 fix cell under a never-widen pair; the fix regenerates up to 158 client-facing summaries and starts the BD/GoldRunner metrics, so it is a served change.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_FIRMBKTS-D1-S44",
        "row ADVI_FIRMBKTS-D1-C-S46",
        "R6_CLOSE.md 'What the fix touches'"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```
