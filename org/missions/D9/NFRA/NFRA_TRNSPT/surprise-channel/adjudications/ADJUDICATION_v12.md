# NFRA_TRNSPT -- round 21 L8 adjudication

<sweep_watermark>2026-10-09T17:29Z</sweep_watermark>

L8 compile by 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~17:3xZ. L8 input: `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R21_CLOSE.md @bbaa367ce5 (msg 3793); landing evidence R21_FIRST_SCHEDULED_LANDING.json @7cdd125f18`. MAY-CLOSE; no judgment criterion.
4 rows dismissed below; D2-S11 and D2-S12 closed in place in REMEDIATION_v9. Nothing graduates. ARMED: 0.

**For the analysis (FWD-1/2/3):** one scheduled fire (16:00Z) landed one meeting end to end, with 436 rows, 98 held out, residual re-wipe 0, and the
planted control discriminating. The 17:00Z fire landed nothing new (no re-land). Wall-clock is 'absent' (interim, site Z's metadata route). The research
meeting is the one excluded case.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S17",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T17:29:05Z",
    "one_line": "Round 21 compiled. Dismissed: D2-W1-S9 (the naming gate refused a 'pipeline' field; dropped, no effect), D2-W2-S10 (ARMED: held-out Research text readable by a silver-only role) -- disarmed by D2-S13, the reader's grant carries an explicit Deny on teams/transcripts/silver/research_meeting/ and the issuer's live proof reads that prefix AccessDenied; D2-S13 and D2-S14 (disposition records). Closed in place, clocks only: D2-S11 (the gateway host's allowlist now admits 3 of 4 meetings; the 16:00Z scheduled fire landed a monday_meeting bronze -> silver) and D2-S12 (source-map entries + transcripts-v1.0.0 on origin). The research meeting's refusal remains the organizer-grant person act (laptop S11, Andrew).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W1-S9",
      "NFRA_TRNSPT-D2-W2-S10",
      "NFRA_TRNSPT-D2-S13",
      "NFRA_TRNSPT-D2-S14"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~17:3xZ: git ls-remote origin refs/tags/transcripts-v1.0.0 -> fe3e0aad38 (peeled 4e29ac38d5); 4e29ac38d5 adds 39 lines to infra/aws/lambda/ci/lambda-source-map.json; round-close-check round 21 MAY-CLOSE (orders=3, judgment=0). Held-out Research text is still unblanked at the writer; the Deny is the guard, so a later grant widening must not drop it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows NFRA_TRNSPT-D2-W1-S9, NFRA_TRNSPT-D2-W2-S10, NFRA_TRNSPT-D2-S13, NFRA_TRNSPT-D2-S14",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R21_CLOSE.md @bbaa367ce5 (msg 3793); landing evidence R21_FIRST_SCHEDULED_LANDING.json @7cdd125f18",
        "this seat's reads ~17:3xZ: git ls-remote origin refs/tags/transcripts-v1.0.0 -> fe3e0aad38 (peeled 4e29ac38d5); 4e29ac38d5 adds 39 lines to infra/aws/lambda/ci/lambda-source-map.json; round-close-check round 21 MAY-CLOSE (orders=3, judgment=0)",
        "R21_SILVER_READER_PROOF.json @f8a19f80e4 (silver 200, bronze AccessDenied, research AccessDenied)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A dropped field, an ARMED row disarmed by an applied Deny, and two disposition records."
  }
]
```
