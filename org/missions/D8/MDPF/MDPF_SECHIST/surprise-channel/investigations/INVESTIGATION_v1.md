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
  },
  {
    "id": "MDPF_SECHIST-S2",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~H1",
    "surfaced_at": "2026-10-07T12:40:00Z",
    "one_line": "FWD-1's acceptance needs class, sector and clean name on the Positioning page, but the served rows for CSCO, BX and LNVGY carry sub_asset_class None and industry_group None today; round 1 fills only the return windows, so the thread can read returns-complete and still fail on sector.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "issuer read 2026-10-07 ~12:4xZ of s3://opal-data-portal-v2/platinum/etfs/positioning_data.json (LastModified 2026-10-06T13:01:32Z) via R1_CHECKS/sh_fwd1_served_read.py: DIVZ CSCO 'Equity / None / None' windows 2/8; DIVZ BX 'Equity / None / None' 2/8; IDVZ LNVGY 'Equity / None / None' 2/8; control PFOE GEV 'Equity / Industrials / Capital Goods' 4/8",
        "PRD v0.1 C-TABLE: the row (class, sector, clean name) is MDPF_SECCLASS's (FWD-10 detector, FWD-12 sector and industry group served to the ETF view, FWD-14 clean names); this project never writes classification"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD section 2 THREAD: the row exists (MDPF_SECCLASS FWD-10) and the analyst reads the security's class, sector and clean name with its returns.",
    "world_is": "Three of the round's live negative cases have no sector on the served page. Not this project's to fix (C-TABLE); routed to the round-N analysis so the CTO can sequence it against MDPF_SECCLASS FWD-12. The FWD-1 real run will grade returns and classification separately."
  },
  {
    "id": "MDPF_SECHIST-S3",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~H1",
    "surfaced_at": "2026-10-07T21:35:00Z",
    "one_line": "Two corrections: (1) investigation row ids MDPF_SECHIST-S1 (1.0.0_SA_CTO~DELL1, 08:44Z) and MDPF_SECHIST-S2 (2.0.0_SA_COO~H1, 12:40Z) reuse the ids REMEDIATION_v1.md already gave its graduated rows at 08:33Z; (2) S2's evidence is stale: the 2026-10-07 13:01:37Z publish shows CSCO, BX and LNVGY with a sector and 4 of 8 windows.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "REMEDIATION_v1.md (a7010ab13e, 3.0.0_SA_CVO, 08:33Z) carries ids MDPF_SECHIST-S1 and MDPF_SECHIST-S2; INVESTIGATION_v1.md carries S1 (26d1a33719, 08:44Z) and S2 (676bb5a882, 12:40Z) with different content",
        "R1_CHECKS/sh_fwd1_served_read.py at 2026-10-07T21:2xZ against positioning_data.json LastModified 2026-10-07T13:01:37Z: DIVZ CSCO 'Equity / Information Technology / Technology Hardware & Equipment' 4/8; DIVZ BX 'Equity / Financials / Financial Services' 4/8; IDVZ LNVGY 'Equity / Information Technology / Technology Hardware & Equipment' 4/8. S2's read was of the 2026-10-06T13:01:32Z publish"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row ids are unique within a project's channel (surprise-row gate duplicate-id limb); S2 states the three securities show no sector on the served page.",
    "world_is": "Two id pairs collide across documents (the gate grades each new row in its own file, so it did not see the other document); and the sector gap S2 named closed on the 10-07 publish without any SECCLASS FWD-12 write (the table's legacy seed values now reach the page). The FWD-1 read on 2026-10-08 grades classification against the page as it stands then."
  }
]
```

```json
{
  "id": "MDPF_SECHIST-Z-S1",
  "project": "MDPF_SECHIST",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~Z",
  "surfaced_at": "2026-10-09T08:18:34Z",
  "one_line": "The SH-t-4 run-record reland is at HEAD but NOT in the vehicle that runs: this deploy's artifact is the WORKING TREE of etf_daily_pull.py, and the working tree is HEAD minus the 15-line SH-t-4 block, so the 2026-10-09 11:00Z scheduled fire will emit no 'history backfill budget' remainder line. The working-tree blob equals the blob leg L2 of ledger mdpf-sechist-sh-t1-sitez-etf-daily-pull-20261007 closed on, so L2 is intact and it is HEAD that moved past the vehicle.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~H1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RUN git rev-parse HEAD:integrations/bloomberg/pipeline/etf_daily_pull.py -> 73735f44d6b8e4a17c9ebf241a62b9bf4a334379; git hash-object on the working tree file -> 0e399c9523f60511107b8491b9894c892a6aeb60. The order's own context line pins leg L2 to 'working-tree blob 0e399c9523', so the vehicle's bytes ARE the closed leg's bytes.",
      "RUN git diff --stat HEAD -- that path -> '1 file changed, 15 deletions(-)'; the hunk is the SH-t-4 run record at main():610-624 that logs spent_after and the ledger remainder.",
      "RUN git log -S'history backfill budget: estimate' -- that path -> 19e50528d3 (2026-10-08 13:59Z, 2.0.0_SA_COO~H1) 'reland ... SH-t-4 run-record edit back into etf_daily_pull.py and its test, on Andrew's yes'. So the reland landed at HEAD on 10-08 and the vehicle never took it.",
      "RUN byte-level confirm: git show HEAD:<path> | grep -c 'history backfill budget: estimate' -> 1; the same grep on the working tree -> 0.",
      "FILE integrations/bloomberg/pipeline/scheduled_daily_pull.cmd: ETF_PULL is %REPO%\\integrations\\bloomberg\\pipeline\\etf_daily_pull.py -- the live checkout, not a built artifact. The ETFS_RIVALS leg's own comment in the same file states the vehicle 'runs the working tree'.",
      "RUN the L3 subject is NOT broken by this: grep -n '_bb.record(\"backfill\"' on the working tree -> line 609 present, and the etf_history_backfill_<asof> batch_id with it. The budget LINE will still be written; only the extra remainder LOG line is absent.",
      "LIVE Get-ScheduledTask OPAL_BBGTML_daily_pull -> State Ready, NextRunTime 2026-10-09 07:00:00 local (11:00Z), action cmd.exe /c scheduled_daily_pull.cmd, principal 'Opal Bloomberg' LogonType Interactive."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "SH-t-4 was relanded on Andrew's yes at 19e50528d3 and is at HEAD, so the scheduled pull records and logs the backfill draw beside the ledger remainder. Order MDPF_SECHIST.TO-READ-R2-L3 reads the 11:00Z fire for 'a backfill line in the day's bbg_budget ledger'.",
  "world_is": "HEAD carries SH-t-4; the running vehicle does not. The deploy's artifact for this cell is an UNCOMMITTED working-tree state, which makes the delta itself load-bearing: any routine 'git checkout --' , 'git stash', clean or merge on this tree would restore HEAD's hunk and MOVE the deployed bytes with nothing recorded, which is why this is filed ARMED rather than as a note. ARMED WITHOUT A LIVE OWNER, stated rather than hidden: 2.0.0_SA_COO~H1 reads NOT REGISTERED on the broker (lane never registered), so it cannot disarm same-turn and this row is the parked carrier. CONDITION THAT UN-PARKS IT: ~H1 registering, or any seat holding the mdpf-sechist-sh-t1 ledger ruling whether the vehicle should carry the reland before the next fire. I changed nothing: the order's rules forbid this seat editing anything under integrations/bloomberg/pipeline/, and restoring the hunk would move a producer's bytes hours before its scheduled fire with no sign-off. CONSEQUENCE FOR L3, bounded: the backfill ledger line and the manifest are unaffected, so L3's AC1 is not at risk from this; only SH-t-4's own remainder log line will be absent from the 11:00Z run. SEPARATELY and not caused by this: the 10-08 07:00 fire exited 50 (DAPI precondition failed, pull NOT attempted, fallback aborted at zero Bloomberg attempts per C:\\opal-elev\\bbg_fallback_ESCALATION.txt), and on the rc=50 path the .cmd jumps to :prune and SKIPS the ETF leg entirely -- so a repeat would leave L3's manifest ABSENT. Transport is UP as of 08:0xZ (bbcomm pid 36400 since 03:13 local, 127.0.0.1:8194 LISTENING with an ESTABLISHED link to the vendor), and 0.0.3_BG_BBGTerminal reports bloomberg_health ok:true, so entitlement is believed live; this seat did not test it, because an agent-turn Bloomberg call is barred by R-21."
}
```

```json
{
  "id": "MDPF_SECHIST-D1-W12-S1",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_SECHIST~12",
  "surfaced_at": "2026-10-09T14:00:00Z",
  "one_line": "r3_named_tests.py greps pytest -v output for '::<name> PASSED' but does not strip ANSI color, so with FORCE_COLOR=3 in the caller's environment (as in this worker shell) a fully passing file reports TESTS-BAD for every named test.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RUN (FORCE_COLOR=3 in env) python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py WRITER data/mdpf/scripts/silver/test_security_series_writer.py test_three_values_per_day test_cusip_key_namespace test_no_write_without_switch -> pytest '6 passed' but last line 'WRITER-TESTS-BAD not-passed=test_three_values_per_day,test_cusip_key_namespace,test_no_write_without_switch', rc=1; the output shows 'PASSED' wrapped in ESC[32m...ESC[0m.",
      "RUN same invocation under 'env -u FORCE_COLOR' -> '6 passed' and last line 'WRITER-TESTS-OK passed=3/3', rc=1 absent, rc=0.",
      "FILE r3_named_tests.py: regex r'::' + name + r'(\\[[^\\]]*\\])? PASSED' over subprocess stdout with no color strip or --color=no; the file was not edited by this worker."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The criterion invocation prints <LABEL>-TESTS-OK for a file whose named tests pass, in whatever shell the worker or drain runs it.",
  "world_is": "It prints OK only when FORCE_COLOR/PY_COLORS color forcing is absent from the environment; with FORCE_COLOR=3 it prints BAD on a passing file. The same holds for every round-3 criterion that uses r3_named_tests.py. The proof for SH3-t13-AC1 records the run with FORCE_COLOR unset."
}
```
