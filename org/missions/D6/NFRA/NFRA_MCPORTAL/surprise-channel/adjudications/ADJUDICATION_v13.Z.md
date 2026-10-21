# NFRA_MCPORTAL -- OGW round 2 item 3 L9: three 26-day ARMED rows disarmed, worker rows W45-S1..S3 adjudicated (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v13. Fabric: site-z. Recorded: 2026-10-21 ~00:1xZ.

**Input:** `2.0.0_SA_COO~MP` packet `deliverables/2.0.0_SA_COO~MP/ogw/OGW_R2_ROWS_PACKET_20261020.md` @8ea7309729, read whole.
The evidence file `deliverables/0.9.0_WK_NFRA_MCPORTAL~45/row_evidence.json` was read for W3-S2 and W2-S8 and in part for
C-S3. `.tools/owned-paths-validate.py:407-418` was read at HEAD by this seat.

**Verdicts:**
- Z-C-S3, Z-W3-S2 and Z-C-S8 are DISARMED, two of them with a stated limit.
- Z-W45-S1, S2 and S3 are ACCEPTED, as corrections of premise, locus and wording.
- Z-W2-S8 stays ARMED, owner `2.0.0_SA_COO~O`, date 2026-10-21. It is not adjudicated here.

**For the batch16 window tonight (06:00Z), not a grade:** Z-W2-S8's hazard is live for EVERY gateway release, batch16
included.
- Any rollback through `safe-ec2-deploy.sh` first runs `.tools/halt-gate-check.sh`'s per-message scan (L456-475).
  HALT_ACK is read only at L515, after it.
- On 2026-09-25 that scan took about 12 minutes over 186 pending messages.
- So a "60 s /health" rollback trigger can leave the gateway down for minutes, not seconds.
- The applier should measure the scan once before the window, and the scan belongs to `0.0.0_AB_MSTR`'s lane.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S56",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T00:10Z",
    "one_line": "Z-C-S3 (BLOCKING, GRADUATED, 26 days) DISARMED and Z-W45-S1 ACCEPTED: owned-paths-validate.check_agent now returns the worker's task-order grant for an UNMAPPED path (lines 413-418, the ADHC_OWNPTH.005 reach) before any UNDEFINED refusal, so C-S3's 'UNDEFINED before the grant clause' premise no longer holds at HEAD.",
    "class": "OBSERVATION",
    "spec_asserts": "C-S3: a worker is admitted to exactly the paths its non-terminal order names, including a new top-level path (CLAUDE.md 14a; ADHC_OWNPTH.005).",
    "world_is": ".tools/owned-paths-validate.py:413-418 at HEAD: 'if lane_name is None: ... return _owns_task_order_paths(agent, path, grant, root, cache)' with the comment naming NFRA_MCPORTAL-Z-W1-S1. The packet records --self-test 28 arms rc 0 with the UNMAPPED admit arm and its mutant PASS.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-C-S3",
      "NFRA_MCPORTAL-Z-W45-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/owned-paths-validate.py:407-418 at HEAD (read by this seat)",
        "deliverables/2.0.0_SA_COO~MP/ogw/OGW_R2_ROWS_PACKET_20261020.md (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by the code at HEAD. Limit: proven on the tool's self-test with synthetic orders; no live order names an unmapped top-level path today, so the first real one is the served proof."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S57",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T00:10Z",
    "one_line": "Z-W3-S2 (BLOCKING, owner Andrew, G-OWNER-OID) DISARMED, bounded: the deployed grant writer carries MCPORTAL_OWNER_KEY and its claim (names read, no value), and a no-header invoke answers REFUSED NO-OWNER-HEADER, which the writer returns only after its owner-configuration check; that the key equals Andrew's oid is NOT measured, and a wrong key fails CLOSED behind the gateway's single-principal owner gate.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-t-3: the writer is configured with the owner's Entra object id from an existing record; W3-S2 recorded that no record named it.",
    "world_is": "row_evidence.json: get-function-configuration keys [MCPORTAL_OWNER_KEY, MCPORTAL_OWNER_KEY_CLAIM, MCPORTAL_CHANGES_TABLE] (names only); zo5.AC2.sh status=200 verdict_reason=[REFUSED NO-OWNER-HEADER] PASS; equality with Andrew's oid recorded ABSENT. The writer's route is reachable only through the gateway mount behind owner_gate.require_owner (andrew@ only, owner_gate.py:34; this seat's v0.10 W1' sign-off @314290bab3).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W3-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPORTAL~45/row_evidence.json, row Z-W3-S2 (read by this seat)",
        "infra/aws/ec2/opal-gateway/app/owner_gate.py:34 (read by this seat 2026-10-20)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The hazard W3-S2 named (a writer with no owner configured) is gone. Bound: a wrong key cannot widen, because a write needs both the gateway's owner gate (andrew@ only) and the writer's key; a wrong key only refuses Andrew. The close run's owner-header write (MP-zo-4) is the proof of equality and must record it."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S58",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T00:10Z",
    "one_line": "Z-C-S8 (BLOCKING, GRADUATED, 26 days) DISARMED and Z-W45-S3 ACCEPTED: the deployed zip's CodeSha256 equals the downloaded zip's, the zip carries app/ and ops/ at the mirrored path, and the handler answers from the built package; the check's '/var/task' wording overclaimed what its output prints and is corrected.",
    "class": "OBSERVATION",
    "spec_asserts": "C-S8 (W3-S3): the writer's parents[5] and gateway imports cannot resolve inside the zip its Terraform builds.",
    "world_is": "Packet: CodeSha256 deployed == downloaded; app/ and ops/ present at the mirrored path; a no-header invoke answers from the built package (REFUSED NO-OWNER-HEADER requires the handler to import and run). /var/task is inferred from the answer, not printed (W45-S3).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-C-S8",
      "NFRA_MCPORTAL-Z-W45-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MP/ogw/OGW_R2_ROWS_PACKET_20261020.md (read whole)",
        "investigations row Z-W45-S3 (read by this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed: a handler that answers a verdict has imported its modules from the deployed package, which is the thing C-S8 said could not happen. W45-S3 is right that the check's header claimed more than its output shows."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S59",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T00:10Z",
    "one_line": "Z-W45-S2 ACCEPTED (locus correction): the halt-gate per-message scan Z-W2-S8 blames is in .tools/halt-gate-check.sh L456-475, sourced by safe-ec2-deploy.sh L167-171, and HALT_ACK is read only at L515 after the scan; Z-W2-S8 itself stays ARMED with owner 2.0.0_SA_COO~O, date 2026-10-21, and the script is 0.0.0_AB_MSTR's lane.",
    "class": "OBSERVATION",
    "spec_asserts": "W2-S8: a named 90-second (now 60-second) rollback trigger must be meetable by the named rollback command.",
    "world_is": "row_evidence.json W2-S8: safe-ec2-deploy.sh L167-171 sources and calls halt_gate_check before the host step, no rollback flag skips it; halt-gate-check.sh L456-475 loops over pending messages before the verdicts, HALT_ACK read at L515. The 12 min 17 s over 186 messages is the row's 2026-09-25 run, not re-measured.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W45-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPORTAL~45/row_evidence.json, row Z-W2-S8 (read by this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Accepted as the correct locus. Not a disarm of W2-S8: its hazard applies to every gateway release's rollback, batch16 at 06:00Z included; the cheap act before the window is one timed halt-gate run."
  }
]
```

-- 3.0.0_SA_CVO~Z
