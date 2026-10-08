# NFRA_TRNSPT -- round 8 L8/L9 adjudication

<sweep_watermark>2026-10-08T20:1xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-08 ~20:1xZ. L8 input: `deliverables/2.0.0_SA_COO~T2/R8_CLOSE.md
@2e53d2f87c` (msg 1541; CTO forward msg 1543). Round 8: TO-TR-k8 (the class revert) and TO-TR-s8 (FWD-5's first slice, 29 Research
transcripts as structured speech, nothing written to S3) complete, 0 judgment criteria, MAY-CLOSE. 1 row dismissed below; undispositioned
after this compile: 0. ARMED: 0.

For the analysis: research_fold's 2,716 residual wipe flags are capitalised words it could not classify. Any silver home for these
rows must hold them out until resolved, as the mail silver does, and that home is still undecided (PRD :154). Store times are None
by design: they are derived, not observed.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S11",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T20:14:03Z",
    "one_line": "D2-W2-S2 (one utterance in RT-20260409-1029.json has a null speaker, which the file itself names UNATTRIBUTED; research_fold passes it through as None) is dismissed: the issuer ruled to keep None, so the row records a fact of the source, not a defect.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W2-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 8 at box/dell2 HEAD: 5eaeb0744c, a7c0019d76 and the revert 603cbf62e4 are ancestors; git diff 8394179dec..HEAD over data/transcripts/scripts/outlook/ and test_outlook_silver.py is empty, so the ENCRYPTED_UNVERIFIED class is fully reverted and was never deployed. research_fold.py is the only new tracked file in teams/ (no parquet committed). The issuer's read-back R8_READBACK_ONE_TRANSCRIPT.json carries counts only (339 bytes, 0 '@'): RT-20260803-1003, 207 rows, 2 speakers, 207 turns, 0 failures (this seat's reads).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row NFRA_TRNSPT-D2-W2-S2",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R8_CLOSE.md @2e53d2f87c",
        "git diff --stat 8394179dec HEAD (empty) and R8_READBACK_ONE_TRANSCRIPT.json (this compile)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A source fact passed through unchanged under the issuer's ruling."
  }
]
```
