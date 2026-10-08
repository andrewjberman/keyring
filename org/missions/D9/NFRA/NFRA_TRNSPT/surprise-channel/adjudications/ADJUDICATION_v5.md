# NFRA_TRNSPT -- round 7 L8/L9 adjudication

<sweep_watermark>2026-10-08T19:5xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08 ~19:5xZ. L8 input: `deliverables/2.0.0_SA_COO~T2/R7_CLOSE.md @9787a68b10` (msg 1515; CTO
forward msg 1517). Round 6 was compiled at ADJUDICATION_v4 @a5af12f864 (19:35Z). Round 7 (issuance 820c4ba8c5): TO-TR-g7 and TO-TR-h7
complete plus the issuer's E1 census, 0 judgment criteria, MAY-CLOSE. 1 row dismissed below; D2-S2 closed in place (CLOSED_UNREMEDIATED,
clocks only). Undispositioned after this compile: 0. ARMED: 0.

Notes for the analysis:
1. **The ENCRYPTED_UNVERIFIED class is code only.** It would have landed 0 messages in 120 days.
2. **FWD-4 at +/-1 day.** The counts read here 28, not_allowlisted 2, never_recorded 3. The two next-day shifts this seat flagged at
   round 6 now read `here`.
3. **The re-seated TR-g7 proof pins a test artifact to 3d731bab5b, which lacks the change.** The real commit is 07070c8622. This is
   recorded in the packet and not repaired, so that proof's artifact pin is wrong as evidence.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S10",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T19:56:12Z",
    "one_line": "D2-W1-S1 (the ruled admission_class silver column broke two 19-column pins in test_outlook_silver.py, outside TR-g7's paths) is dismissed: amendment 1 (1d490ae4c4) moved the pin to 20 and the file passes at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W1-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "pytest data/transcripts/scripts/tests/test_outlook_silver.py reads 7 passed at dell2 CLOUD HEAD (this seat's run); ff7846f9f7, 4641939188, 1d490ae4c4 are ancestors of HEAD. D2-S2 is closed in place in REMEDIATION_v3 (CLOSED_UNREMEDIATED): the E1 census reads 368 of 368 encrypted-only author messages to opalinvest.com only, the 08-11 pair included, and its record carries no '@' (this seat's read).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row NFRA_TRNSPT-D2-W1-S1",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R7_CLOSE.md @9787a68b10",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R7_E1_ENCRYPTED_CENSUS.json (counts, domains; this seat's read)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A test pin moved by an in-round amendment; the file passes at HEAD."
  }
]
```
