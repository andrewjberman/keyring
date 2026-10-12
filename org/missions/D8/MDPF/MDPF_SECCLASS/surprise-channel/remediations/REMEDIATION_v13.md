# MDPF_SECCLASS -- round 23 remediations (dell1)

<sweep_watermark>2026-10-12T14:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T14:30:00Z. Graduated at ADJUDICATION_v21: 1 row, ARMED (the SC-e-97 pair's firm-total gap).

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S17",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The SC-e-97 pair's blast radius names no firm-total or AUA move, yet the window restatement can change them: the half request says the total_aua and cube totals for the window days are 'not in the record and are not measured', and its own orphan columns show relationships in the current partition but not stored (18..205 a day; 172..205 on 09-26..09-28) and stored relationships absent from the partition (up to 15 a day, which branch 3 removes). This seat's proxy, the current partition's market_value sum, equals the served firm total to the cent only on 2026-10-09 and sits $5,203.59 to $270,086,670.20 ABOVE it on the other 14 window dates. The proxy is not the rebuild (it disagrees with round 22's re-derived byte drift of -$1.35M..-$1.93M on 10-06..08), so the size of the firm-total move is NOT established; that it is not zero is likely. The advisor map also drops advisors with no window day (W86-S4, carried by D1-W80-S3), which is a served change the pair does not name either.",
    "evidence": [
      "3.0.0_SA_CVO pyarrow sum of market_value over the CURRENT gold/canonical/holdings/<date>.parquet vs the served firm[date].total: equal to the cent on 2026-10-09 only (2,015,391,646.72); above served by 32,079,997.98 (09-25), 224,041,973.12 (09-26), 223,812,108.95 (09-27), 270,086,670.20 (09-28), 179,758,545.96 (09-29), 172,345,196.98 (09-30), 173,097,836.54 (10-01), 28,215,020.75 (10-02), 5,203.59 (10-03), 48,507.12 (10-04), 21,236,498.17 (10-05), 21,798,230.14 (10-06), 21,542,619.84 (10-07), 21,045,481.88 (10-08)",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md :28 and the per-date table's orphan columns",
      "adjudication row MDPF_SECCLASS-D1-C-S17"
    ],
    "remedy": "Before the SC-e-97 ship's GO: measure, from the build's own dry run, the per-date REBUILT firm total and each advisor's total for the 15 window days beside the served totals, and write them into the half request's blast radius with both branches (a day whose total moves, a day whose total holds) and the advisors the map would drop; the CTO half signs on that radius. Close when: the half request names the per-date firm-total move (or measures it zero), and the first post-ship read finds each window day's served total equal to the stated rebuilt total within the pair's tolerance.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v23",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v23"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": "2026-10-12T14:05:00Z"
    },
    "closed": false
  }
]
```
