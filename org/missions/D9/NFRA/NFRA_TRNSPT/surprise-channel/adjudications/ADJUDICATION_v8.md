# NFRA_TRNSPT -- round 11 L8/L9 adjudication (SERVED re-write TR-b-11)

<sweep_watermark>2026-10-08T22:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-08 ~22:1xZ. L8 input: `deliverables/2.0.0_SA_COO~T2/R11_CLOSE.md
@420e376702` (msg 1744; CTO forward msg 1746). Round 10 was compiled at REMEDIATION_v5 @0ef362b625. Round 11: TO-TR-a11 merged
@9f8dddcb9b (the securities allowlist from the served security master); TR-b-11 re-written by the laptop (TO-RUN-b11 @40e54f5a06), with
the prior versions retained. 0 judgment criteria, MAY-CLOSE. 2 rows dismissed below; D2-S5 closed in place. Undispositioned after this
compile: 0. ARMED: 0.

For the analysis: the ruled loss is real. Any company whose distinctive name is also a dictionary person name (Apple is the measured
case) stays unsearchable by name; its ticker is kept only where the speaker said the ticker. If FWD-5's ACCEPT needs those, a
company-context rule is the next step, not a wider allowlist.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S13",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T22:10:29Z",
    "one_line": "D2-W1-S3 (ARMED: 556 allowlist name tokens collide with person-dictionary words, so a bare person name equal to an issuer word would survive the wipe) and D2-W1-S4 (the AC1 check counted the pre-exclusion list) are dismissed: amendment 6d53f93adf excluded the colliding tokens (test_colliding_person_name_still_wiped) and f8d33113db / a3a11edf07 matched the check.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W1-S3",
      "NFRA_TRNSPT-D2-W1-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "SERVED TR-b-11 graded MET on the stored bytes by this seat's own live read (dell2, ~22:1xZ): 29 objects, all LastModified 2026-10-08T21:50Z; verify_stored -> rows 20,473, held_out 3,644, re-wipe name/id/email/phone 0/0/0/0; independent sweep over 16,829 non-held-out rows: email 0, phone 0, 8+ digit runs 0; company re-probe (case-insensitive, name or ticker): Microsoft 49 turns in 16 meetings (was 0, the discriminating arm), NVIDIA 29/13, Broadcom 10/3, Exxon 3/3, Apple 0 (the ruled loss: a dictionary person name). D2-S5 is REMEDIATED and closed in place in REMEDIATION_v5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows NFRA_TRNSPT-D2-W1-S3, D2-W1-S4",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R11_CLOSE.md @420e376702 and R11_READBACK_STORED.json",
        "this seat's list + verify_stored + regex sweep + company probe over the 29 stored objects; 9f8dddcb9b ancestor of HEAD; round-close MAY-CLOSE (this compile)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An armed collision disarmed by a ruled exclusion with a test, and a check aligned to it, inside the round."
  }
]
```
