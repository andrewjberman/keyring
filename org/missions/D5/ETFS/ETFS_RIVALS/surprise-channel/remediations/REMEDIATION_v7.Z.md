# ETFS_RIVALS -- round 7 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-03 ~00:35Z. Graduated at round 7's L9 (`adjudications/ADJUDICATION_v7.Z.md`, parts A and B).

Round 7 is drained and applied:
- 8 of 8 orders are terminal;
- the apply ran at 75ad1e4d2e;
- the ledger is CLOSED 6/6.

This slug covers the whole project and carries no sweep watermark. One item graduates, P2. The slug goes to `1.0.0_SA_CTO~Z` with
the review `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R7_REVIEW_20261003.md`. C-S24 (REMEDIATION_v6) stays OPEN until
its organic proof on 2026-10-05.

```json
[
  {
    "id": "ETFS_RIVALS-Z-W1-S46",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The sweep's AI step stops starting vendor calls at its deadline (at most remaining - sweep.MARGIN_MS = 150 s), but it cannot interrupt a call already in flight, and ai_client.TIMEOUT_S is 120 s. A call started just inside the deadline therefore leaves about 30 s for the republish that follows. This seat measured republishes on the daily Lambda at 87.8 s (RequestId 1e8592c2) and 89.3 s in round 6. In that worst case the 900 s ceiling cuts the republish, while the morning marker-driven page stays served.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W1-S46 (0.9.0_WK_ETFS_RIVALS~1)",
      "data/etfs/scripts/rivalfunds/sweep.py:75 MARGIN_MS = 150_000, :78 AI_DEADLINE_S = 600.0, :526 _ai_deadline_s; ai_client.py:22 TIMEOUT_S = 120 at CLOUD a714df4d7f",
      "CloudWatch REPORT 1e8592c2-8627-4ed0-90b8-6770f7aea4ac Duration 87794.60 ms (round-6 republish of 2026-10-02)"
    ],
    "remedy": "Make the worst case fit. Either the vendor call's timeout is deadline-aware (min(TIMEOUT_S, time left to the deadline)), or the margin covers one vendor timeout plus the measured republish p95 (about 120 s + 100 s). Proof: a test with a stubbed vendor call that returns at TIMEOUT_S just after the deadline shows the republish still has its measured time.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v7"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV
