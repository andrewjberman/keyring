# MDPF_SECHIST -- surprise channel, INVESTIGATION v1 (round 1)

Append-only. Worker rows `MDPF_SECHIST-W<n>-S<k>`.

```json
[
{
  "id": "MDPF_SECHIST-W2-S1",
  "project": "MDPF_SECHIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_MDPF_SECHIST~2",
  "surfaced_at": "2026-10-07T07:34:02Z",
  "one_line": "SH-t-2 says the sibling etf_positioning tests run bare from the gold folder, but test_etf_positioning_upgrade_forward.py and test_etf_positioning_per_fund_asof.py fail at import on a clean worktree: etf_positioning_publisher.py:66 imports etf_classifications_dynamodb, which lives only under infra/aws/lambda/v2_portal/_shared/ and is not on the path.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "cd data/etfs/scripts/gold && python test_etf_positioning_upgrade_forward.py -> rc=1 ModuleNotFoundError: No module named 'etf_classifications_dynamodb' (etf_positioning_publisher.py line 66); same for test_etf_positioning_per_fund_asof.py (2026-10-07, worktree wk-MDPF_SECHIST-2 at f8a41e7902; etf_positioning_gold.py unchanged by this cell)",
      "test_etf_positioning_industry_group.py and test_etf_positioning_sector_order_carriers.py run rc=0 from the same folder; git ls-files shows etf_classifications_dynamodb.py only under infra/aws/lambda/v2_portal/"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The sibling tests in the same folder import etf_positioning_gold bare, run offline with fixtures and pass from the folder (so they can serve as the keep-passing regression for any gold edit).",
  "world_is": "Two of the four siblings import the publisher, whose dependency is not on the bare path, and fail at import on a clean worktree before any gold code runs; they may pass on a box whose PYTHONPATH carries the _shared folder. No gold edit was made by this cell, so none of this affects SH1-t2-AC1."
}
]
```
