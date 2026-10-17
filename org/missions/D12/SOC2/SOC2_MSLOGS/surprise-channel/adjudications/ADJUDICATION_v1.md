# SOC2_MSLOGS -- round 1 L8/L9 (dell1)

<sweep_watermark>2026-10-17T06:08:31Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T06:08:31Z, on 2.0.0_SA_COO~S1 msgs 7178 and 7366 and 1.0.0_SA_CTO~DELL1 msg 7368 (org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_L8_DRAIN_END_PACKET_R1_20261017.md @f842ea3a7c).
Swept: 15 of 15 investigation rows dispositioned (11 dismissed, 4 graduated). SM1-r1-AC5 graded NOT MET. The watermark moves to now.

```json
[
  {
    "id": "SOC2_MSLOGS-D1-C-S1",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T06:08:31Z",
    "one_line": "ROUND 1 L9: JUDGMENT SOC2_MSLOGS.TO-SM-r1 AC5 NOT MET. AC5 says Andrew recognises the timeline. No record of his recognition exists. His first read through the door could not say who acted, and that is why the door was re-cut. The enriched read reached him at 02:37Z, and nothing records his reading of it. The machinery is in place and read live; one sentence from Andrew closes it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "SOC2_MSLOGS.TO-SM-r1 SM1-r1-AC5 (judgment): Andrew names one account and a window, reads that account's Microsoft 365 timeline in order through the door with his MFA session, from collection that is actually running, and recognises it (PRD FWD-1: 'recognises it as that person's real day').",
    "world_is": "The recognition is Andrew's, and this seat cannot supply it. READ BY THIS SEAT 2026-10-17 ~06:1xZ. Records: Glob org/tier1_exec/**/ANDREW_DIRECT_20261017_0[3-6]* finds 6 records, none about SOC2_MSLOGS. The SOC2_MSLOGS commits since 02:30Z (fed3acffd2, f842ea3a7c, 9a72d4c1d5, c2e2c22be4) record no reading by him. The packet's own account (section 2): his first CloudShell read (~02:1xZ, relayed by the laptop CTO) 'worked and was cut at 5,000 rows with six columns that could not say who acted'. That fails 'recognises it', since a timeline that cannot say who acted cannot be recognised as that person's day. The enriched block reached him by Taildrop at 02:37Z, and that is the last record. WHAT IS IN PLACE, read live by this seat: globgrph-trino-access-lambda alias member is version 5 (10240 MB, 600 s, LastModified 2026-10-17T02:36:19Z, CodeSha256 J9ejfNZdkXT0ueKK...), deployed after the detail amendment. The collection side reads R1-SWITCH-OK on the issuer's run (9,534 audit_records over 8 dates). CLOSE PATH: Andrew runs the 02:37Z block on one account and window and says in one line whether it reads as that person's real day. A record of that line, graded here, meets AC5 without another build.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_L8_DRAIN_END_PACKET_R1_20261017.md @f842ea3a7c section 2",
        "aws lambda get-function-configuration --function-name globgrph-trino-access-lambda --qualifier member (this seat)",
        "Glob org/tier1_exec/**/ANDREW_DIRECT_20261017_0[3-6]* (6 records, none on SOC2_MSLOGS)",
        "git log --since 2026-10-17T02:30Z over org/tier1_exec/2.0.0_SA_COO~S1 and org/missions/D12/SOC2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: AC5 NOT MET for want of Andrew's recognition; the enriched read is the close path."
  },
  {
    "id": "SOC2_MSLOGS-D1-C-S2",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T06:08:31Z",
    "one_line": "ROUND 1 L8: 15 rows dispositioned. The 6 ARMED or BLOCKING rows are resolved in code read by this seat or by the issuer's merges. 7 INERT rows are dismissed. 4 text and naming rows graduate to REMEDIATION_v1 for round 2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "SOC2_MSLOGS-D1-W1-S2",
      "SOC2_MSLOGS-D1-W2-S1",
      "SOC2_MSLOGS-D1-W2-S2",
      "SOC2_MSLOGS-D1-W2-S4",
      "SOC2_MSLOGS-D1-S1",
      "SOC2_MSLOGS-D1-W1-S3",
      "SOC2_MSLOGS-D1-W5-S2",
      "SOC2_MSLOGS-D1-W1-S4",
      "SOC2_MSLOGS-D1-W1-S5",
      "SOC2_MSLOGS-D1-W4-S1",
      "SOC2_MSLOGS-D1-W4-S2"
    ],
    "spec_asserts": "Spine L8/L10: every BLOCKING or ARMED row is dispositioned on grounded evidence before the slug.",
    "world_is": "READ BY THIS SEAT. W1-S2 (BLOCKING, ARMED; first_content.py raises on the raw era): 56af05ace6 deletes data/m365_metadata/scripts/silver/first_content.py and its test, and git ls-tree at HEAD holds 0 paths named first_content.py. W2-S2 (ARMED; write-once read any head exception as absent): b4f2f10bbb changes infra/aws/lambda/globgrph-trino-access/handler.py so that _head returns 'absent' only for codes 404, NoSuchKey and NotFound, and every other failure returns 'error', on which nothing is written. Tests are added for each branch, and e601e64560 adds a fail-closed arm to the cell check. The deployed member alias (version 5, 02:36:19Z) post-dates it. ON THE ISSUER'S EVIDENCE, NOT RE-READ: W2-S1 (ARMED; the silver columns exist in the merged builder, 56af05ace6, and the door reads live silver); W2-S4 (BLOCKING, ARMED; the lane gate after complete, resolved by reopening the order on the worker's branch, f3da4710d8, with the fix b4f2f10bbb landing); S1 (BLOCKING; the Terraform dependency cycle, fixed in release item 3a at ade21bee08, and the release plan ran). The packet records 'a1 tf' now refuses the cross-reference. INERT DISMISSED: W1-S3 and W5-S2 (the channel file absent from a sparse worktree); W1-S4 and W1-S5 (both readings match the TO-SM-c1 contract); W4-S1 (a citation time); W4-S2 (records absent from a sparse worktree). GRADUATED (C-S3): W2-S3, W1-S1, W5-S1, W7-S1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show --stat 56af05ace6; git ls-tree -r HEAD (0 first_content.py)",
        "git show b4f2f10bbb -- infra/aws/lambda/globgrph-trino-access/handler.py and tests/test_handler.py",
        "python .tools/round-close-check.py --project SOC2_MSLOGS --round 1 -> orders=6 judgment=1 ungraded=1 (before this row)",
        "org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_L8_DRAIN_END_PACKET_R1_20261017.md @f842ea3a7c section 4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each ARMED or BLOCKING row is resolved by a merged fix; the INERT rows are worktree and citation facts."
  },
  {
    "id": "SOC2_MSLOGS-D1-C-S3",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T06:08:31Z",
    "one_line": "Graduated to REMEDIATION_v1 (4), carried by the issuer to round 2. W2-S3: the door hand-types its bronze prefixes, which the naming gate WARNs on. W1-S1, W5-S1 and W7-S1: the README, RUNBOOK and main.tf text still describe eight accounts, filter.py and an unsubscribed sign-in feed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "SOC2_MSLOGS-D1-W2-S3",
      "SOC2_MSLOGS-D1-W1-S1",
      "SOC2_MSLOGS-D1-W5-S1",
      "SOC2_MSLOGS-D1-W7-S1"
    ],
    "spec_asserts": "Spine L10: an item that still bears on later work graduates with an owner and a close condition.",
    "world_is": "W2-S3 stays ARMED in the channel until its remedy lands (a WARN today; rule 30 says every S3 address is lib/opal_naming output). The three text rows are INERT. They matter because an operator reading the RUNBOOK would believe the old eight-account, sign-in-less design.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows SOC2_MSLOGS-D1-W2-S3, SOC2_MSLOGS-D1-W1-S1, SOC2_MSLOGS-D1-W5-S1, SOC2_MSLOGS-D1-W7-S1",
        "org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_L8_DRAIN_END_PACKET_R1_20261017.md @f842ea3a7c sections 4 and 5"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows in REMEDIATION_v1."
  }
]
```

-- 3.0.0_SA_CVO
