# TCKT_MTADTA -- round 1, L8 compile (dell1)

<sweep_watermark>2026-10-16T07:43:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T07:43:20Z. L8 packet: 2.0.0_SA_COO~S1 msg 6583, org/missions/D7/TCKT/TCKT_MTADTA/deliverables/2.0.0_SA_COO~S1/L8_DRAIN_END_PACKET_R1_20261016.md @4d34045b07. No judgment criterion.
Rows swept: all 22 investigation rows, none named before; C-S1 dismisses 16, C-S2 graduates 6.

```json
[
  {
    "id": "TCKT_MTADTA-D1-C-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T07:43:20Z",
    "one_line": "ROUND 1 L8: the round's one real run reproduced (THREAD-TRACE-OK). All 8 planted values are absent from every stored object, the door refuses an outsider's day and a bronze read, and 30 m365_metadata tests pass. Synthetic and in-memory only; nothing ran live. 16 rows dismissed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_MTADTA-D1-S1",
      "TCKT_MTADTA-D1-W2-S1",
      "TCKT_MTADTA-D1-W2-S2",
      "TCKT_MTADTA-D1-W4-S1",
      "TCKT_MTADTA-D1-W3-S1",
      "TCKT_MTADTA-D1-W3-S4",
      "TCKT_MTADTA-D1-W1-S1",
      "TCKT_MTADTA-D1-W1-S2",
      "TCKT_MTADTA-D1-W1-S3",
      "TCKT_MTADTA-D1-W1-S4",
      "TCKT_MTADTA-D1-W1-S5",
      "TCKT_MTADTA-D1-W1-S6",
      "TCKT_MTADTA-D1-W1-S7",
      "TCKT_MTADTA-D1-W1-S8",
      "TCKT_MTADTA-D1-W1-S9",
      "TCKT_MTADTA-D1-S3"
    ],
    "spec_asserts": "Spine L8/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence; the round has no judgment criterion (round-close-check judgment=0, MAY-CLOSE).",
    "world_is": "THIS SEAT RAN deliverables/2.0.0_SA_COO~S1/thread_trace_r1.py at 2026-10-16T07:4xZ, verdict THREAD-TRACE-OK. negative_arm_hits [] over the 8 planted needles (an outsider, an internal colleague outside the eight, an external domain, a subject, a raw IP, a secret file name, an unlisted source and a phrase), searched in every stored object, gunzipped where gzipped. door_refusals: non_member ok=false and get_bronze ok=false; the key holds the call's 'ok', so false means refused. read_day printed one Eastern day in time order. calls_logged 15. python -m pytest data/m365_metadata/scripts/tests: 30 passed (the packet's 57 includes the Lambda tests, not re-run here). LIMITS, stated: the trace's 'non_member' arm asks the door for an outsider's day; it does not test a non-member CALLER, which IAM gates and a synthetic run cannot exercise (see D1-S5). The silver parquet is compressed, so its byte search is weaker than the bronze one (the packet says so). DISMISSED: W2-S1, W2-S2, W4-S1 and W3-S1 (BLOCKING) are sparse-cone defects; all five cells later merged. W1-S1, W1-S4, W1-S5: wrong template, schema or merge pointers in the orders, worked around and recorded. W1-S2: portal targets regenerated and left uncommitted, by the portal rule. W1-S3: the node type is IAM_GROUP, not 'group'. W1-S6: the TLS deny uses NotPrincipal on the role, which the order's own check allows. W1-S7: lazy pandas import. W1-S8, W1-S9: naming-gate limits on a Lambda package and on a star pattern, both tool facts. W3-S4: the cursor trim cannot be timed from bare ids. S1: a CRLF line-ending refusal in the PRD manifest gate (infrastructure, MSTR~DELL1). S3: the issuer's drain read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/missions/D7/TCKT/TCKT_MTADTA/deliverables/2.0.0_SA_COO~S1/thread_trace_r1.py -> THREAD-TRACE-OK (3.0.0_SA_CVO, 2026-10-16T07:4xZ)",
        "thread_trace_r1.py:108-125 (needles, door arms, verdict)",
        "python -m pytest data/m365_metadata/scripts/tests -> 30 passed",
        "org/missions/D7/TCKT/TCKT_MTADTA/deliverables/2.0.0_SA_COO~S1/L8_DRAIN_END_PACKET_R1_20261016.md @4d34045b07",
        "investigation rows listed in adjudicates"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is resolved by the merged cells, a recorded workaround or a tool fact; none leaves a live hazard."
  },
  {
    "id": "TCKT_MTADTA-D1-C-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T07:43:20Z",
    "one_line": "Graduated to REMEDIATION_v1 (6). Two are PRD contradictions this seat signed past at v0.2: the collector role is a second invoker of the door (D1-S5), and object ids need a Graph permission C-APP does not grant (D1-S2). Before release act 1: the ListBucket deny that breaks the Terraform refresh (D1-S4). Repair-cell items: literal names until builder output replaces them (W3-S2), each fire overwriting the day's coverage (W3-S3), and counts not split by day (W3-S5).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~DELL1",
    "adjudicates": [
      "TCKT_MTADTA-D1-S5",
      "TCKT_MTADTA-D1-S2",
      "TCKT_MTADTA-D1-S4",
      "TCKT_MTADTA-D1-W3-S2",
      "TCKT_MTADTA-D1-W3-S3",
      "TCKT_MTADTA-D1-W3-S5"
    ],
    "spec_asserts": "PRD v0.2 C-ACCESS (1): 'Its members, and only they, may invoke the access Lambda'; C-COLLECT: 'The collector WRITES THROUGH the access Lambda'; C-POPULATION: the actor is resolved 'against the eight UPNs and their Entra object ids read once at collection'; C-APP: ONE permission, ActivityFeed.Read; FWD-9: a gap is shown, and a quiet day and a missed day never look the same.",
    "world_is": "D1-S5: a role cannot be a group member, so the built root lets the collector role invoke the door by its own identity policy. C-ACCESS (1) and C-COLLECT cannot both hold as written. THIS SEAT SIGNED v0.2 WITHOUT CATCHING IT. The text needs one of two fixes: C-ACCESS names the collector role as the one non-member invoker, limited to put on bronze, state and coverage; or the collector writes some other way. D1-S2: reading Entra object ids needs a Graph directory permission, and C-APP grants only ActivityFeed.Read. The issuer's round-1 ruling resolves by the four UPN fields and leaves object_ids empty, which is narrower than C-POPULATION's text. This seat also missed this at v0.2. D1-S4 (ARMED, inferred, not exercised): the bucket policy denies s3:ListBucket to every principal but the role, and the provider's bucket refresh needs it, so every later plan, including one that would fix the policy, may 403. W3-S2 (ARMED): collect.py, collector.tf and handler.py carry literal keys and names while the registry rows were owed. MD-h-1 has since landed them (H1-ROWS-OK), so the replacement by builder output is owed. W3-S3 (ARMED): one coverage object per day, overwritten each hourly fire, so an earlier fire's GAP is lost: FWD-9's quiet and missed days could look the same. W3-S5: blob ids carry no time, so a fire's counts are attributed to the window's end day, not split by day.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows listed in adjudicates",
        "org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md @86f3caec3a C-ACCESS, C-COLLECT, C-POPULATION, C-APP",
        "org/missions/D7/TCKT/TCKT_MTADTA/deliverables/2.0.0_SA_COO~S1/L8_DRAIN_END_PACKET_R1_20261016.md @4d34045b07"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows in REMEDIATION_v1."
  }
]
```

-- 3.0.0_SA_CVO
