# NFRA_TRNSPT -- round 2 L8/L9 adjudication

<sweep_watermark>2026-10-01T00:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01 ~07:0xZ. L8 packet: 2.0.0_SA_COO~T 103412 (org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_DRAIN_END_PACKET_20261001.md @881af50a86). Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R2_REVIEW_20261001.md (co-committed). 6 undispositioned rows (S11, S12, S13, S14, W1-S6, W1-S7): 2 dismissed by the rows below, 4 graduated in remediations/REMEDIATION_v2.md. Closed IN PLACE in remediations/REMEDIATION_v1.md by their clocks alone: S6, S7, S8, S10. Left OPEN there, on purpose: S9 (the lander no longer crashes, but no admitted real message is landed) and W4-S8 (the limits are stated; the held-out rate on real rows is unmeasured). Carried unchanged: S2, S3, W4-S10.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S6",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T07:00:00Z",
    "one_line": "W1-S6 (round 1's test asserted the retired tables label and failed on the ruled one) was repaired by TO-TR-x2; the file passes at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-W1-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "data/transcripts/scripts/tests/test_outlook_bronze.py and test_outlook_envelope.py pass together at HEAD (18 passed), and the whole tests directory in one process reads SUITE-GREEN passed=133 failed=0 in a fresh worktree.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest test_outlook_bronze.py test_outlook_envelope.py (this seat, fresh worktree at 34ae583549, ~06:5xZ): 18 passed",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_CHECKS/r2_suite_check.py (this seat, same worktree): SUITE-GREEN passed=133 failed=0",
        "investigation row NFRA_TRNSPT-W1-S6 (0.9.0_WK_NFRA_TRNSPT~1)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R2_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The failing assertion was repaired inside round 2 and the file is green at HEAD."
  },
  {
    "id": "NFRA_TRNSPT-C-S7",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T07:00:00Z",
    "one_line": "W1-S7 (TO-TR-x2's re-materialise command could not work as written, and the handler's fake lives in teams/pull.py) records two acts taken inside the grant in place of the order's; both outcomes hold in a fresh checkout.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-W1-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "In a worktree created today, git ls-files --eol over data/transcripts/assets and data/transcripts/scripts/tests/fixtures reads 39 files i/lf w/lf and 1 file -text; .gitattributes scopes eol=lf to those two directories; the suite is green there, so the listing method added to pull._MemS3 and the test FakeS3 carries the seam.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-files --eol in the fresh worktree (this seat): 39 i/lf w/lf, 1 i/-text w/-text",
        ".gitattributes at HEAD: data/transcripts/assets/** text eol=lf and data/transcripts/scripts/tests/fixtures/** text eol=lf",
        "r2_suite_check.py in the same worktree: SUITE-GREEN passed=133 failed=0",
        "investigation row NFRA_TRNSPT-W1-S7 (0.9.0_WK_NFRA_TRNSPT~1)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R2_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The order's command was unworkable and the worker reached the order's outcome by a non-destructive act; the outcome is reproduced on a checkout the worker never touched."
  }
]
```
