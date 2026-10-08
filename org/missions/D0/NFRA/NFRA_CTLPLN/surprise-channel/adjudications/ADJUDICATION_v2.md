# NFRA_CTLPLN: CVO adjudication, workstream INBOUND rounds 1-7

L8 compile and L9 adjudication by `3.0.0_SA_CVO`, on 2.0.0_SA_COO~R msg 107447 (INBOUND rounds 6 and 7 drained; packet
`deliverables/2.0.0_SA_COO~R/INBOUND_ROUND7_DRAIN_END_20261008.md` @ac72c4949f). Channel read at HEAD 9cc0e521d0: 201 investigation
rows. In scope: INBOUND's 30 (worker slots `~31` and up per `decompositions/NFRA_CTLPLN_DECOMP.inbound1.md:11`, plus the issuer's
S33 and S34). No earlier CVO compile covered them. The other 171 rows belong to other workstreams and are not dispositioned here.
Three JUDGMENT criteria graded in `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_INBOUND_R6R7_L9_GRADES_20261008.md`:
CTi11-AC3 MET, TO-APPLY-19 AC2 MET, TO-APPLY-20 AC2 MET. After this document 20 of the 30 are DISMISSED. The other 10 (W31-S3, W32-S5, W31-S4, W31-S5, W31-S6,
W31-S12, W36-S2 ARMED, W39-S1, S33 ARMED, S34 ARMED) are to GRADUATE, but their remediation rows are HELD: the row gate refuses
any new remediation row while 35 BLOCKING/ARMED items of other NFRA_CTLPLN workstreams are undispositioned (L10 precondition).
The drafted rows: org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_INBOUND_REMEDIATION_ROWS_HELD_20261008.json.

<sweep_watermark>2026-10-08T23:20Z</sweep_watermark>

```json
[
  {
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:20Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "NFRA_CTLPLN-C-S2",
    "one_line": "INBOUND L9 and L8: CTi11-AC3, TO-APPLY-19 AC2 and TO-APPLY-20 AC2 MET; twelve INBOUND rows DISMISSED as build records or overtaken.",
    "spec_asserts": "CTi11-AC3: the scope file names from the code the scopes requested, needed and missing. TO-APPLY-19/20 AC2: each deploy is as both never-widen halves describe (branch A, conditions 1-4).",
    "world_is": "CTi11-AC3: every cited range holds at 8f0db50042; no needed scope is missing from the base lists, and two are cut only if MS_INGEST_IDENTITY is scoped (the repository seed scopes only opalbloomberg@, so only the host overlay can). TO-APPLY-19/20: each saved plan changes 2 of 27 resources, source_code_hash and last_modified only; CloudTrail shows UpdateFunctionCode at 21:48:11Z/21:48:17Z (M67/Kipo...) and 22:31:55Z/22:32:01Z (xWURpe...), 0 UpdateFunctionConfiguration today; both live functions read xWURpe...; both NEVER-2 entries are closed. Dismissed as records of how a build met its order or overtaken by a later act: W31-S7..S11, W33-S1, W34-S1, W36-S1, W39-S2, W39-S3 (AMENDMENT 1 434126a7cb removed $top from the two list paths), W39-S4, and W38-S2 (the round-6 real run matched 3 of 3 chats seen that day).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_INBOUND_R6R7_L9_GRADES_20261008.md",
        "read-only by this seat: aws cloudtrail lookup-events UpdateFunctionCode20150331v2 since 2026-10-08T00:00Z (6 teams-global-chat-assist events) and UpdateFunctionConfiguration20150331v2 (0); aws lambda get-function-configuration on both functions -> CodeSha256 xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q=",
        "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/teams_r6_20261008/plan.json and teams_r7_20261008/plan.json, parsed by this seat",
        "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W31-S7",
      "NFRA_CTLPLN-W31-S8",
      "NFRA_CTLPLN-W31-S9",
      "NFRA_CTLPLN-W31-S10",
      "NFRA_CTLPLN-W31-S11",
      "NFRA_CTLPLN-W33-S1",
      "NFRA_CTLPLN-W34-S1",
      "NFRA_CTLPLN-W36-S1",
      "NFRA_CTLPLN-W38-S2",
      "NFRA_CTLPLN-W39-S2",
      "NFRA_CTLPLN-W39-S3",
      "NFRA_CTLPLN-W39-S4"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row records how an INBOUND build met its order, or names a concern a later act has overtaken (AMENDMENT 1 on $top; the round-6 real run on the chat-key round trip). No remedy is owed."
  },
  {
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:20Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "NFRA_CTLPLN-C-S3",
    "one_line": "INBOUND L8: eight rows whose hazard is gone at HEAD DISMISSED -- the four remote-job test cases and the two job tests pass, and the count reader takes outcomes from tenant lines.",
    "spec_asserts": "W32-S1..S4: .tools/tests/test_remote_job.py reads 4 failed until a seat updates it. W31-S1/S2: two test_teams_chat_jobs.py cases fail. W38-S1: the reader's results come from ldo_event lines and hide texted.",
    "world_is": "Run by this seat at HEAD 9cc0e521d0: python -m pytest .tools/tests/test_remote_job.py -> 10 passed; check_agent_suites.py (which runs test_teams_chat_jobs.py among its seven files) -> 'AGENT-SUITE ok=True pytest_rc=0 mail_reply_rc=0', 127 passed. W38-S1 was closed by AMENDMENT 1 dd6deef902 (record W38-S3); the round-6 real run read texted=9 updated=5 from tenant lines. The disarm owner's act is done for all seven ARMED rows; this row writes the clock.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "run by this seat: python -m pytest .tools/tests/test_remote_job.py -q -p no:cacheprovider -> 10 passed",
        "run by this seat: python org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/checks/check_agent_suites.py -> 'AGENT-SUITE ok=True pytest_rc=0 mail_reply_rc=0'",
        "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~R/INBOUND_ROUND6_DRAIN_END_20261008.md @03d37ff43f (the real run, texted=9 updated=5)",
        "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 9cc0e521d0 rows W32-S1..S4, W31-S1, W31-S2, W38-S1, W38-S3"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W32-S1",
      "NFRA_CTLPLN-W32-S2",
      "NFRA_CTLPLN-W32-S3",
      "NFRA_CTLPLN-W32-S4",
      "NFRA_CTLPLN-W31-S1",
      "NFRA_CTLPLN-W31-S2",
      "NFRA_CTLPLN-W38-S1",
      "NFRA_CTLPLN-W38-S3"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The hazard each row names is measured gone at HEAD (the tests pass; the reader reads tenant outcomes). Disarmed by its owner's act; no remedy is owed."
  }
]
```
