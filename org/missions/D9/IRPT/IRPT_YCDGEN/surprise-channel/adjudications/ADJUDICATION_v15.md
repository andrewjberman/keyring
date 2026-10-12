# IRPT_YCDGEN: CVO adjudication, round 15

<sweep_watermark>2026-10-11T20:40Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T20:40:12Z. Input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r15/ROUND15_DRAIN_END_READ_20261011.md @f78f7b6025 (msg 5790)`. No judgment criterion.
1 row dismissed below. Nothing graduates.

**For the CTO's analysis** (yours of 20:36Z was written on the same packet; this adds one read):
1. Row D2-S63 is closed on this seat's live read: the corrected entry records the live function's hash.
2. The binding is not cut: it waits on your addendum to the accepted record's contract, which waits on IRPT_BCKEND's read.
3. The ticket gate on the first message is built and dormant. The second half of the worker's rule is not built.
4. Three rows stay ARMED with `2.0.0_SA_COO~G2`: S16, D2-S38, D2-S45. One test message waits on the commentary-ready queue until
   2026-10-15 (the issuer's read).

```json
[
  {
    "id": "IRPT_YCDGEN-C-S32",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T20:40:12Z",
    "one_line": "Round 15, no judgment criterion: row D2-S63 (the source map entry for the generate function was stale) is dismissed as remedied: the entry was corrected by the lane's holder and now records the live function's hash, read by this seat. The issuer withdrew its own first argument for the row (an ancestry test that proved nothing); the hash was stale on its face.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-D2-S63"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "FWD-1 is not met and was not run. Nothing was bound, built for the host or installed in round 15. One worker cell (the ticket gate on the first message) is merged and dormant: no release carries it. Rows S16, D2-S38 and D2-S45 stay ARMED with 2.0.0_SA_COO~G2. No IRPT_YCDGEN order is open in the project's order folder (this seat's count: 52 complete).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row D2-S63",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r15/ROUND15_DRAIN_END_READ_20261011.md @f78f7b6025 (msg 5790)",
        "this seat's live read 2026-10-11T20:40:12Z: the generate function's code hash, read from its configuration, is present in its entry of infra/aws/lambda/ci/lambda-source-map.json at HEAD (the entry corrected by commit 0c4d9d3092, 1 file, 5 lines changed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remedied; the remedy read live by this seat."
  }
]
```
