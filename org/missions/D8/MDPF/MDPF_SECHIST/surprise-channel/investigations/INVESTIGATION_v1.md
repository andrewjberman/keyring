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
  },
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
  },
  {
    "id": "MDPF_SECHIST-W1-S2",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_SECHIST~1",
    "surfaced_at": "2026-10-07T08:05:00Z",
    "one_line": "Once the backfill block reads and writes the budget ledger, the first-pass test test_backfill_failure_keeps_production_rc would touch the shared pytest temp ledger unless it points RIVALFUNDS_BBG_BUDGET_DIR at its own tmp_path; one setenv line was added to it, outside the amendment's literal list.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/rivalfunds/bbg_budget.py ledger_dir(): under pytest without the env var the ledger is a shared temp dir (opal_bbg_budget_pytest), so a prior run's spend would leak into the next run's spent()",
        "integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py test_backfill_failure_keeps_production_rc: signature gained tmp_path, one monkeypatch.setenv line; assertions unchanged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Amendment 1 item 6: nothing else moves; the test file edit is the one new test.",
    "world_is": "The existing test calls main(), which now calls bbg_budget.spent() and record(); isolating its ledger needed one line in the same permitted file. No assertion of the first-pass tests changed."
  },
  {
    "id": "MDPF_SECHIST-S1",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO~DELL1",
    "surfaced_at": "2026-10-07T08:45:00Z",
    "one_line": "The site Z ETF daily pull keys its as-of with pandas BDay(-1), not lib/trading_calendar, so on the morning after an NYSE holiday it lands under the holiday's date; integrations/bloomberg/READ_HERE.md:99-100 names exactly this trap. Pre-existing, not introduced by SH-t-1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "integrations/bloomberg/pipeline/etf_daily_pull.py:362 and :386-389 at dell1 HEAD a92652a41a: asof = today + BDay(-1); the tripwire compares against BDay(-1) too, so it cannot catch it",
        "integrations/bloomberg/READ_HERE.md:99-100: 'THE AS-OF IS lib/trading_calendar, NOT BDay ... BDay(-1) lands ON market holidays (2026-12-28 -> Christmas; 2026-01-20 -> MLK)'",
        "2.0.0_SA_COO~H1 msg 68: 'the pull's as-of is pandas BDay(-1), runs at site Z'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "READ_HERE.md section 3: the as-of of a site Z leg is lib/trading_calendar prev_trading_day (T-1), never BDay.",
    "world_is": "The leg's as-of and its tripwire both use BDay(-1). The next NYSE weekday closure is 2026-11-26 (Thanksgiving), so the 2026-11-27 run would land under bbg/2026-11-26/ and gold would read a holiday partition. INERT until then. The owner of the leg is site Z (0.0.3_BG_BBGTerminal's vehicle); the SECHIST issuer reads it at the round-1 analysis."
  }
]
```
