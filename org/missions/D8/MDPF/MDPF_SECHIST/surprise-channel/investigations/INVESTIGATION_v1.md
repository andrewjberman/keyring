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
  },
  {
    "id": "MDPF_SECHIST-D1-W5-S1",
    "project": "MDPF_SECHIST",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_SECHIST~5",
    "surfaced_at": "2026-10-09T13:55:00Z",
    "one_line": "The R3 named-test check r3_named_tests.py grades PASSED by regex '::name PASSED' and reports GAP-TESTS-BAD on a passing suite when FORCE_COLOR=3 is set in the shell, because pytest then emits ANSI codes between the name and PASSED.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~H1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "worktree wk-mdpf_sechist-r3-6, shell env FORCE_COLOR=3: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py GAP data/etfs/scripts/silver/test_etf_history_gap_record.py <3 names> -> output 'test_absent_interior_day_listed \u001b[32mPASSED' and last line GAP-TESTS-BAD not-passed=<all 3>, rc=1 (4 passed in pytest's own summary)",
        "same command under 'env -u FORCE_COLOR' -> GAP-TESTS-OK passed=3/3, rc=0; the check (r3_named_tests.py:36) passes the parent environment to pytest and does not set NO_COLOR or --color=no"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order MDPF_SECHIST.TO-SH-t6 criterion SH3-t6-AC1: running the named invocation from the worktree root prints GAP-TESTS-OK once the three named tests pass.",
    "world_is": "On a shell that exports FORCE_COLOR (this seat's does: FORCE_COLOR=3), the same invocation prints GAP-TESTS-BAD for passing tests, so every R3 named-test criterion (GAP, BLANK, MMF, PULL, ENTRY, WRITER) is graded by environment, not by the code. I did not edit the check (order forbids it); the criterion was recorded with FORCE_COLOR unset. Armed for the other five R3 workers and the drain, whose shells may carry the same variable; the owner can add '--color=no' to the check's pytest argv."
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
  "id": "MDPF_SECHIST-D1-W8-S1",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_SECHIST~8",
  "surfaced_at": "2026-10-09T14:20:00Z",
  "one_line": "The R3 named-test check (r3_named_tests.py) reports TESTS-BAD on passing tests whenever FORCE_COLOR is set in the environment, because pytest colours the PASSED token and the check's regex expects 'name PASSED'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RUN (shell with FORCE_COLOR=3) python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_named_tests.py ENTRY data/mdpf/scripts/silver/test_security_entry_depth.py <3 names> -> pytest prints '5 passed' with '::test_each_source_depth \u001b[32mPASSED' and the last line is ENTRY-TESTS-BAD not-passed=<all three>, rc=1 (2026-10-09, worktree wk-mdpf_sechist-r3-9)",
      "RUN the same command under env -u FORCE_COLOR -> last line ENTRY-TESTS-OK passed=3/3, rc=0; the check at r3_named_tests.py line ~33 matches the text '::<name> PASSED' with no ANSI strip",
      "env | grep -i color in the dell1 worker shell -> FORCE_COLOR=3"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Each R3 criterion invocation, run from the worktree root, prints <LABEL>-TESTS-OK when the named tests pass (order MDPF_SECHIST.TO-SH-t9 ACCEPTANCE).",
  "world_is": "The invocation is environment-sensitive: with FORCE_COLOR set it fails on real passing tests, so a grader running in a coloured shell would read a false BAD for every R3 cell. I did not edit the check (barred by the order) and ran it with FORCE_COLOR unset for the recorded output."
}
```

```json
{
  "id": "MDPF_SECHIST-D1-W6-S1",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_SECHIST~6",
  "surfaced_at": "2026-10-09T14:40:00Z",
  "one_line": "Three of the five pre-existing offline gold suites in data/etfs/scripts/gold/ do not pass in a dell1 worker worktree at the base (rc=1 before any SH-t-7 edit): two cannot import the lambda-vendored etf_classifications_dynamodb, one reads portal/src files the worktree does not carry.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RUN at the base, from data/etfs/scripts/gold with PYTHONPATH=<worktree>;<worktree>/infra/aws/lambda/v2_portal/_shared: test_etf_positioning_per_fund_asof.py and test_etf_positioning_upgrade_forward.py -> rc=1 ModuleNotFoundError: No module named 'etf_classifications_dynamodb' (etf_positioning_publisher.py:66; the suite header itself says the module is vendored into the lambda package)",
      "RUN at the base: test_etf_positioning_sector_order_carriers.py -> rc=1, 12 PASS 8 FAIL, each FAIL reading 0 B from portal/src/pages/Positioning/shared/bookSet.ts (the portal submodule is not populated in the worktree)",
      "RUN after SH-t-7: the five suites' outputs are byte-identical to the base outputs (backfill_rows rc=0, industry_group rc=0 50/50, the other three rc=1 as above)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SH-t7 and its issuer: the existing gold tests in data/etfs/scripts/gold/ pass, and are run to show a security with no listed day reads as today.",
  "world_is": "Only two of the five pass in this worktree (backfill_rows, industry_group); the other three fail identically before and after the change for environment reasons, so they show nothing about SH-t-7 either way. SH-t-7's own proof of unchanged reading is its named tests plus the byte-identical outputs of the five suites."
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

```json
{
  "id": "MDPF_SECHIST-D1-W7-S1",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_SECHIST~7",
  "surfaced_at": "2026-10-09T14:45:00Z",
  "one_line": "TO-SH-t8 asks for ONE total-return level field and names none; the pull now requests TOT_RETURN_INDEX_GROSS_DVDS, a field name chosen from vendor knowledge and not confirmed on the terminal (no Bloomberg call is permitted this cell).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "FILE org/missions/D8/MDPF/MDPF_SECHIST/task-orders/MDPF_SECHIST.TO-SH-t8.pull-fill-and-total-return-field.md:29 says 'gains ONE total-return level field (route 2a)'; a search of org/missions/D8/MDPF for the field name found only DAY_TO_DAY_TOT_RETURN_GROSS_DVDS (the daily return, already pulled) and no level field.",
      "FILE integrations/bloomberg/pipeline/etf_daily_pull.py TOTAL_RETURN_LEVEL_FIELD = 'TOT_RETURN_INDEX_GROSS_DVDS' (one constant; HISTORY_FIELDS = PX_LAST, DAY_TO_DAY_TOT_RETURN_GROSS_DVDS, that constant).",
      "FILE integrations/bloomberg/mcp/blp_client.py:309-322 historical_data builds each row from the fields the response HAS (point.hasElement(f)); an invalid field name raises nothing at the default on_response_error='ignore', so a wrong name lands as an absent column, not a failed pull (rc stays 0)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order names the cell (a total-return level field, route 2a) and its test (test_history_request_carries_total_return_level); it does not name the Bloomberg mnemonic.",
  "world_is": "The mnemonic is a one-constant edit. Its first real confirmation is the first live history_topup carrying a non-null column of that name (the site-Z take is a separate WORLD act). If the terminal rejects the name, gold's C-MMF rule (TO-SH-t7) finds no level and blanks the day, which is its stated behaviour for a day with neither input."
}
```

```json
{
  "id": "MDPF_SECHIST-D1-W14-S1",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_SECHIST~14",
  "surfaced_at": "2026-10-09T16:10:00Z",
  "one_line": "TO-SH-t15 makes the scheduled gold Lambda write s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=<date>/gap_record.json; the write sits outside gold's _assert_write_boundary and needs an S3 PutObject grant on that prefix that no cell in this round adds.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~H1",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "FILE data/etfs/scripts/gold/etf_positioning_gold.py produce_gap_record() calls etf_history_gap_record.write_record, whose key is lib.opal_naming address('bloomberg','etfs','silver','history_gaps','as_of=<d>','gap_record.json') = bloomberg/etfs/silver/history_gaps/as_of=<d>/gap_record.json in bucket opal-data-etfs (printed by the builder for 2026-10-08).",
      "FILE etf_positioning_gold.py _assert_write_boundary admits only opal-data-etfs/gold/; the gap write does not pass through it (write_record is the silver module's own writer), so the boundary is not a gate on this key.",
      "NOT RUN: the Lambda role's policy was not read (comp-iam is declared not applicable to this cell); whether it already holds s3:PutObject on that prefix is unmeasured."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order says the Lambda write grant is checked at the deploy pair, not in this cell (preflight comp-iam).",
  "world_is": "Without s3:PutObject on bloomberg/etfs/silver/history_gaps/* for the gold Lambda role, every scheduled run logs 'gap record: WRITE FAILED' and continues: gold still blanks over the gap that day (in-memory record) but no record persists, so the next pull cannot re-request from it (FWD-4 degrades silently, FWD-5 holds). Read grant on bbg/ already exists (load_history lists and reads it)."
}
```

```json
{
  "id": "MDPF_SECHIST-D1-S1",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~H1",
  "surfaced_at": "2026-10-09T16:50:00Z",
  "one_line": "SH-t-19's depth bound marks a ticker exhausted for good when its backfill returns zero rows, and a per-security vendor error returned as an empty response also reads as zero rows, so one transient error removes that ticker from depth backfill permanently.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "FILE integrations/bloomberg/pipeline/etf_daily_pull.py @522aa18dc2 history_backfill_exhausted: a planned ticker with a stored date and rec rows == 0 joins the set; the set is the union with the prior manifest's list (never shrinks)",
      "FILE same, depth loop near :745-760: backfill_info[ticker] = {rows: _n} with _n = 0 when the returned row list is empty; a group that raises leaves its tickers absent (not marked)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SH-t19 repair (3): a ticker whose last backfill returned no row older than its earliest stored date is not planned again.",
  "world_is": "Zero rows from a per-security error and zero rows from a genuinely short history read the same, and nothing ever removes a ticker from the list. Issuer ruling (2.0.0_SA_COO~H1): accepted for round 5 -- no served value moves (depth only), the 2026-10-12 manifest's list is read at SH-t-20 and any ticker in it with known older vendor history is the trigger for a later expiry repair; owner 2.0.0_SA_COO~H1."
}
```

```json
{
  "id": "MDPF_SECHIST-D1-S2",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~H1",
  "surfaced_at": "2026-10-09T16:55:00Z",
  "one_line": "The gold Lambda package (etf-positioning-producer build_package.py PACKAGE) ships 3 members and none of the modules SH-t-7/SH-t-15 now import: etf_history_gap_record.py and lib/opal_naming.py with its registry inputs; gold's load_gap_record imports the gap module OUTSIDE its try, so a deploy as built raises ImportError on every scheduled run.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~H1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "FILE infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py:95-102 PACKAGE = etf_positioning_gold.py, etf_positioning_publisher.py, etf_classifications_dynamodb.py (3 members)",
      "FILE data/etfs/scripts/gold/etf_positioning_gold.py:836, :865, :931 'import etf_history_gap_record as _gr'; :836 load_gap_record imports before its try, and only NoSuchKey is tolerated",
      "FILE data/etfs/scripts/silver/etf_history_gap_record.py:49 record_address imports lib.opal_naming.address; lib/opal_naming.py reads infra/logic/registry/*.json relative to its own file",
      "FILE infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py:184-201 the pattern that works: lib/opal_naming.py as a real subpackage plus 7 registry files and org/standards/NAMING_SCHEMA.json at the same relative paths"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The gold deploy half: the package is built from git at a pin and the member list must include the silver module (a package edit in this act).",
  "world_is": "The member list needs more than the silver module: lib/opal_naming.py and its registry and schema inputs too. Not live: no gold deploy has been taken. Disarm ruling (2.0.0_SA_COO~H1): the gold deploy order to 0.7.0_AE_CloudOps~DELL1 adds to PACKAGE etf_history_gap_record.py, lib/opal_naming.py and its registry/schema inputs, on the mdpf-gold-lambda pattern; the build's own import-closure check (infra/aws/lambda/ci/import-closure-check.py) passes on the zip before apply; a post-apply invoke reading 'gap record:' in the log (not ImportError) is the acceptance's first line."
}
```

## MDPF_SECHIST-Z-S2 -- The SH-t-8 "site-Z take" had already landed in site Z's live tree, through box-sync 574fe5ce6b at 17:09Z, before its site-Z producer half was signed.

```json
{
  "id": "MDPF_SECHIST-Z-S2",
  "project": "MDPF_SECHIST",
  "fabric": "site-z",
  "surfaced_by": "1.0.0_SA_CTO~Z",
  "surfaced_at": "2026-10-09T17:52:00Z",
  "one_line": "The SH-t-8 take of etf_daily_pull.py at blob 75342a6958 was already in site Z's shared tree, which the OPAL_BBGTML_daily_pull task runs, via box-sync 574fe5ce6b (17:09Z), before the site-Z producer half or its ledger existed; the integration path is not gated on the pair.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~H1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git rev-parse HEAD:integrations/bloomberg/pipeline/etf_daily_pull.py = 75342a695857 = origin/box/dell1's blob; git hash-object on disk = the same; git status clean",
      "first-parent walk of box/sitez: 574fe5ce6b (box-sync, CLOUD @9fe42c43a5, 13:09:28 -0400) is the first commit carrying d2434ebc08",
      "Get-ScheduledTask OPAL_BBGTML_daily_pull: cmd.exe /c ajb_workspace/integrations/bloomberg/pipeline/scheduled_daily_pull.cmd (shared tree); :242 ETF_PULL=%REPO%/integrations/bloomberg/pipeline/etf_daily_pull.py; next run 2026-10-10 07:00 local",
      "python -m pytest integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py on the live tree: 13 passed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "XB-20261009T172645Z-2ed2 and the staged TO-DEPLOY-SH-T8-SITEZ-TAKE: site Z's tree takes ONE file at blob 75342a6958 replacing 73735f44d6, under a ledger opened by site Z's owner, outside 10:30Z-12:00Z.",
  "world_is": "There is nothing left to take: the replacement happened by integration. The site-Z half (1.0.0_SA_CTO~Z) is signed on that basis, and the executor's order becomes a VERIFY. Disarm: before the 2026-10-10 07:00 local run, a NEVER-2 ledger entry is opened that names the box-sync as the landing, records the blob read and the 13-pass test, and closes on the first scheduled run's acceptance (run_class scheduled, exit 0, both new manifest fields, exhausted list printed). Fixing the integration-path gap belongs to 0.0.0_AB_MSTR~Z and is a separate question from this disarm."
}
```

## MDPF_SECHIST-D1-S3 -- The dell1 cloudops agent user cannot call iam:SimulatePrincipalPolicy, so an AE seat on this box cannot run the cloud-ops live-primitive check on any role it grants.

```json
{
  "id": "MDPF_SECHIST-D1-S3",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~SH1",
  "surfaced_at": "2026-10-09T20:12:35Z",
  "one_line": "After the TO-DEPLOY-GOLD apply landed R1's one statement, the cloud-ops verification step for a new ARN (iam simulate-principal-policy on the live primitive) returned AccessDenied for cloudops-dell1-agent-user on iam:SimulatePrincipalPolicy, so this seat could prove the grant DESIRED and APPLIED but could not exercise it; the same gap applies to every role an AE seat on dell1 grants, not just this one.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::313476888478:role/etf-positioning-producer-role --action-names s3:PutObject --resource-arns arn:aws:s3:::opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-12/gap_record.json -> AccessDenied: User arn:aws:iam::313476888478:user/cloudops-dell1-agent-user is not authorized to perform iam:SimulatePrincipalPolicy (2026-10-09, 3 invocations, target plus 2 negative controls, all 3 identical)",
      "POSITIVE CONTROL that the credentials and the role both exist and are readable: aws iam get-role-policy --role-name etf-positioning-producer-role --policy-name s3-rw-etfs-gold-platinum rc=0 returning 9 statements, and aws s3api head-bucket --bucket opal-data-etfs rc=0 -- so the denial is the SimulatePrincipalPolicy permission, not a bad ARN, a bad role or absent credentials",
      "The act did not depend on it: the statement is proven APPLIED by the live get-role-policy read (8 prior statements carried byte-identical, 1 added) and by terraform plan -detailed-exitcode = 0 after the apply"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": ".claude/skills/cloud-ops/SKILL.md names aws iam simulate-principal-policy as the live-primitive verification an AE seat runs for a NEW bucket/table/ARN -- one --resource-arns per call, the positive control as a separate invocation, the ARN at the grain the action is authorized on, and the simulation run AFTER the resource exists. It reads as a step every AE seat can take on demand.",
  "world_is": "On dell1 that step is unreachable: the agent user holds no iam:SimulatePrincipalPolicy. The instrument the skill leans on for the EXERCISED rung is absent on this box, so an AE seat here can reach DESIRED and APPLIED and no further, and ABSENT is not EXERCISED-AGAINST. For THIS grant the EXERCISED rung arrives with L3, the first scheduled gold run, which writes the gap record as the role -- a real exercise rather than a simulation, and it is the issuer 2.0.0_SA_COO~H1's read. The open question is whose it is to decide whether the dell1 and dell2 agent users should carry iam:SimulatePrincipalPolicy (read-only, no mutation) so the skill's step is takeable, or whether the skill should state that on an agent box the live PutObject at L3 is the only exercise available. Not adjudicated here and it blocked nothing."
}
```

## MDPF_SECHIST-D1-S4 -- proof-of-spec-check cannot see <proof_genre>DEPLOY</proof_genre> in a CRLF-committed order, so a correct order's complete flip is blocked.

```json
{
  "id": "MDPF_SECHIST-D1-S4",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~SH1",
  "surfaced_at": "2026-10-09T20:45:55Z",
  "one_line": "proof-of-spec-check refuses the TO-DEPLOY-GOLD instance for lacking <proof_genre>DEPLOY</proof_genre> on its own line, but the marker IS on line 14 of the order: the order's blob is CRLF and PROOF_GENRE_ELEMENT_RE ends in [ \t]*$, which cannot cross the \r -- so the complete flip is blocked by an instrument that cannot read a correct order.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "FILE .tools/proof-of-spec-check.py:2106 PROOF_GENRE_ELEMENT_RE = re.compile(r\"^[ \t]*<proof_genre>\\s*([A-Za-z]+)\\s*</proof_genre>[ \t]*$\", re.M); :2110 _committed_order_text reads the order with `git show HEAD:<rel>` capture_output (bytes), so CRLF survives into the match",
      "CONTROL INSIDE THE SAME FILE: :2107 RISK_ELEMENT_RE = ^\\s*<risk>\\s*([A-Za-z]+)\\s*</risk> has NO trailing anchor and reads WORLD from the SAME bytes in the SAME run. One regex reads the order and the other does not; the only difference is the trailing [ \t]*$",
      "MEASURED on the order's blob at HEAD: 7264 bytes, 98 CRLF, 0 bare LF; genre regex -> None, risk regex -> WORLD. The SAME text with \r\n replaced by \n: genre regex -> DEPLOY. The marker is present at line 14, between <risk>WORLD</risk> and <placeholders>NONE</placeholders>",
      "SCOPE FALSIFIED rather than assumed -- this is NOT 'the gate is broken for everyone': the orders behind two working DEPLOY-genre instances read 0 CRLF / 116 LF (AMGT_RESAPP.TO-AMGT-ay-5) and 0 CRLF / 133 LF (AMGT_RESAPP.TO-AMGT-ax-5), both with the marker present. The defect bites an order COMMITTED WITH CRLF, which is what a Windows-box writer produces",
      "The instance is otherwise clean at commit e8fb4ce260: proof-of-spec-check reports structural=jsonschema valid, 6 of 6 named controls DISCRIMINATE with 0 DID-NOT-DISCRIMINATE, rollback named, alignment 5/5 criteria carrying a cell_ref and 1/1 declared cell reachable, surprises 1 of 1 resolving to a channel row, invocation-alignment 1/1 matching. violations=1, and it is this one"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "org/standards/PROOF_OF_SPEC.schema.json and 3.0.0_SA_CVO verdict 29306 condition 1: genre DEPLOY is admitted when the governing order carries the issuer's line-anchored <proof_genre>DEPLOY</proof_genre> beside <risk>SERVED|WORLD</risk>. MDPF_SECHIST.TO-DEPLOY-GOLD carries both, so a DEPLOY instance for it should be admitted and the assignee should be able to flip <status> to complete once its work is proven.",
  "world_is": "It is refused. The admission test is a line-anchored regex over bytes read straight from `git show`, and this order was committed CRLF, so the trailing [ \t]*$ never reaches the line end and the marker reads as absent. The work is unaffected -- L1 and L2 are closed with proof and the live state is verified -- but <status> stays `pending` and the order cannot be marked complete. NEITHER REMEDY IS THE ASSIGNEE'S: (a) normalise the order's line endings to LF, which is the ISSUER's file and the spec is frozen mid-round, or (b) widen the regex to tolerate a trailing \r (or normalise newlines in _committed_order_text), which is the GATE OWNER's instrument and fixes the whole class rather than this one order. (b) is recommended: (a) leaves the next CRLF-committed order to rediscover it. The audited `# pipeline-override:` escape was deliberately NOT taken -- its stated condition is that the TO stands outside the pipeline, which is false here, and a false reason in an audit log is worse than a blocked flip. Routed to 2.0.0_SA_COO~H1 with 1.0.0_SA_CTO~DELL1 copied as the decision."
}
```

## MDPF_SECHIST-D1-S5 -- The 2026-10-13 scheduled pull was stopped by its own precondition (DAPI down), so SH-t-21's gating event has not happened.

```json
{
  "id": "MDPF_SECHIST-D1-S5",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~H1",
  "surfaced_at": "2026-10-13T11:55:00Z",
  "one_line": "The 2026-10-13 07:00 ET scheduled pull started and was stopped by its own precondition (DAPI down, Terminal likely signed out), so no run_manifest exists for as_of 2026-10-12 and SH-t-21's gating event has not happened; the same condition holds for SH-t-22 behind it.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ s3://opal-data-etfs/bbg/2026-10-12/run_manifest.json at 2026-10-13T11:35Z by this seat: HeadObject 404; listing bbg/2026-10-12/ returned no key; newest bbg/ prefix 2026-10-09",
      "CONTROL in the same call set: HeadObject on bbg/2026-10-09/run_manifest.json read LastModified 2026-10-12T11:03:03Z, so the instrument returns a value for a present key",
      "RELAYED, not measured by this seat: 0.0.0_AB_MSTR~Z bus 042a6904 via 0.0.0_AB_MSTR~DELL1 msg 4788 (11:41Z): OPAL_BBGTML_daily_pull LastRunTime 2026-10-13T11:00:01Z, LastTaskResult 50, log bbg_tplus1_20261013_070001.log 108 lines; 0 matches for 'ETF LEG EXIT CODE' and 'run_class'; line 48 'PRECONDITION: FAILED -- DAPI DOWN and not self-healed. PULL NOT ATTEMPTED.'; blpapi connect IO_ERROR on 127.0.0.1:8194 at 07:03, 07:05, 07:06, 07:07 ET",
      "RELAYED same message: the 2026-10-12 log read PRECONDITION PASS and ETF LEG EXIT CODE 0, which matches this seat's own read of that run's manifest (11:03:03Z)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-SH-t21 depends_on: the scheduled pull for as-of 2026-10-12 and the publish that follows it; TO-SH-t22 depends_on SH-t-21 read OK and the next scheduled run (as-of 2026-10-13).",
  "world_is": "No pull wrote a manifest and nothing was written (RIVALFUNDS legs exit 93 and 97, 'nothing written'). This is not the organic case SH-t-21 names: that case reads a landed run where the vendor left no null, and no run landed. Issuer ruling (2.0.0_SA_COO~H1): SH-t-21 and SH-t-22 stay `issued`, no read is run against an absent manifest and nothing is graded BAD; the date is ruled when a scheduled run lands again, because the as_of 2026-10-12 key may then be written by a catch-up or may never be (the next run after recovery writes the then-current T-1), which is a dated re-point inside this decomposition and not an ENDPOINT change. Recovery is site Z's Terminal sign-in, which 0.0.0_AB_MSTR~Z reports it told 1.0.0_SA_CTO~Z and Andrew; this seat does not act there. Disarm/close: the first scheduled manifest after the sign-in, read by this seat."
}
```

## MDPF_SECHIST-D1-S6 -- The live characteristics producer package vendors the pre-MMF-rule etf_positioning_gold.py, so FWD-9's rule is not in the code that computes characteristics.json's windows.

```json
{
  "id": "MDPF_SECHIST-D1-S6",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~G1",
  "surfaced_at": "2026-10-13T15:22:49Z",
  "one_line": "The live cot-satellites-characteristics-producer package vendors etf_positioning_gold.py at 09408b19e5, four SECHIST commits behind HEAD, so the MMF rule (FWD-9) and the gap-record producer that the Positioning gold now runs are not in the code that computes characteristics.json's per-ticker return windows.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RELAYED then re-read by this seat: 2.0.0_SA_COO~G1 msg 4916 and record org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/HG_T16_PACKAGE_DRIFT_20261013.md (member sha256 table, live vs HEAD build at 34b7e3d62a)",
      "MEASURED here 2026-10-13 ~15:3xZ: git log -- data/etfs/scripts/gold/etf_positioning_gold.py lists ae567af9ef, d3c47c1896, ed0b1fc0d2, f9d959a290 (workers ~18, ~14, ~6, ~6, 2026-10-09) after 09408b19e5 (2026-08-28); git merge-base --is-ancestor of each of the four against 09408b19e5 is false; git diff --shortstat 09408b19e5 HEAD: 112 insertions, 6 deletions, matching the record",
      "FILE infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/build_package.py:35,42,119 vendors data/etfs/scripts/gold/etf_positioning_gold.py and says the producer imports it for a Bloomberg-sourced ticker's windows"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD v0.3 C-MMF / FWD-9: the money-market fund's return is carried by the pull's daily-return field and a null day is served blank; the Positioning page is the graded surface.",
  "world_is": "Not measured: whether characteristics.json carries a money-market ticker whose window the older rule computes differently, and by how much. Issuer ruling (2.0.0_SA_COO~H1): (B) in the G1 record is accepted from this seat's side -- the producer's apply ships the three vendored members at their live bytes, and nothing of this project's is shipped into that package inside an act whose signed half does not name it. Redeploying the MMF rule and the gap-record producer into this package is a separate act of this seat under its own never-widen pair; it is not decided and not scheduled. First act toward it: read characteristics.json for the money-market tickers and run the HEAD rule against the live rule on the same inputs, both branches printed, before any pair is asked for. Owner 2.0.0_SA_COO~H1."
}
```

## MDPF_SECHIST-D1-W23-S1 -- The gold folder cannot be collected by pytest: test_etf_positioning_sector_order_carriers.py calls sys.exit at module level.

```json
{
  "id": "MDPF_SECHIST-D1-W23-S1",
  "project": "MDPF_SECHIST",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_MDPF_SECHIST~23",
  "surfaced_at": "2026-10-14T13:33:45Z",
  "one_line": "python -m pytest data/etfs/scripts/gold -q aborts at collection (INTERNALERROR, SystemExit: 0, no test runs, rc=3) because test_etf_positioning_sector_order_carriers.py ends with a module-level sys.exit(0 if n_pass == n else 1) at line 296, which pytest imports as a test module; excluding that one file the folder runs 32 passed, rc=0.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RUN timeout 300 python -m pytest data/etfs/scripts/gold -q -p no:cacheprovider in worktree C:/dev/wk-MDPF_SECHIST-23 at HEAD 6c8dc6dc79 plus the SH-t-24 edits: 'INTERNALERROR> SystemExit: 0' raised from test_etf_positioning_sector_order_carriers.py line 296, 'no tests ran in 1.69s', rc=3",
      "RUN the same with --ignore=data/etfs/scripts/gold/test_etf_positioning_sector_order_carriers.py -> '32 passed in 2.49s', rc=0; git status on that file is clean (not touched by this cell)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The worker face's regression instruction: the existing gold suites must still pass, run once as python -m pytest data/etfs/scripts/gold -q.",
  "world_is": "The sector-carriers file is a script-style check that exits at import, so under pytest the whole folder collects as an INTERNALERROR and the regression run reads as a crash rather than as a result. It is outside this cell's paths and was not edited. The gold suites themselves are unaffected: 32 pass with that file excluded. Owner of the file is the seat that wrote it; the fix (a main() guard or a test_ function) is not this cell's to make."
}
```
