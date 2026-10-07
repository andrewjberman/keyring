# MDPF_SECHIST -- surprise channel, INVESTIGATION v1 (round 1)

**Id grammar:** a worker's row is `MDPF_SECHIST-W<n>-S<k>`. **Append-only during the round.**

```json
[
  {
    "id": "MDPF_SECHIST-W1-S1",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_SECHIST~1",
    "surfaced_at": "2026-10-07T07:34:43Z",
    "one_line": "The cell's need rule (earliest stored date later than asof-365d) never converges for a security whose real history is shorter than a year: 2602335D (no vendor series), PFDE and PFOE (stored from about 2025-12-31) are re-planned and re-requested on every run, and consume cap slots.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "plan_only() live read 2026-10-07 on dell1: backfill plan names 2602335D end=2026-10-06 (nothing stored), PFDE and PFOE end=2025-12-30 (earliest stored 2025-12-31), i.e. after one backfill they would still read earliest > asof-365 and be planned again",
        "integrations/bloomberg/pipeline/etf_daily_pull.py history_backfill_plan (this branch): need = held is None or held > asof-365d; no record of a request that returned nothing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A ticker needs depth when nothing is stored or its earliest stored date is later than asof - 365 days; the plan is bounded by cap=50.",
    "world_is": "A security whose true first trading day is inside the last year (or which has no vendor series) satisfies the need rule forever, so each run spends one request and one cap slot on it for zero new rows. At 15 needing of 172 today it is cheap; it would only crowd out real work if more than 50 such securities accumulate. Built exactly as ordered; a bound (e.g. a manifest-recorded 'requested, nothing older exists' memory) is a round-2 enrichment for the CTO to read."
  }
]
```
