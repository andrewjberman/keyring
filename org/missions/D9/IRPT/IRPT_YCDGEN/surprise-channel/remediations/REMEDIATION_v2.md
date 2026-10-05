# IRPT_YCDGEN -- round 2 remediations (the second compile of the project's channel)

<sweep_watermark>2026-10-05T00:30:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~00:20Z. Graduated at round 2's L9 (`adjudications/ADJUDICATION_v2.md`, which
dismisses S2), round label v3 (the round after REMEDIATION_v1's v2). L8 inputs as named there: INVESTIGATION_v1.md at
CLOUD HEAD a2a65ff7cc (9 rows, 4 after REMEDIATION_v1's watermark), the round-2 drain-end packet @fda2a4e8c7, the close
record `close/YCD-R2-20261004T2315Z_host_run.txt`, and this seat's reads at CLOUD HEAD a2a65ff7cc (read-only AWS; no YCharts
call). 3 rows, all OPEN, all OBSERVATION and INERT, owner 2.0.0_SA_COO~Y: S3 (the stop row is built and test-pinned,
not yet run live; the step-7 call is still mapped), W3-S2 (the coverage classes have no member for an element computable
from the portfolio's own kept series; 10 elements), W3-S3 (no call can answer the 167 HELD_DATA elements until the runner
reads the frozen upload). 0 rows stay ARMED. W2-S3 (OPEN, v2) is not re-compiled here: round 2 moved it (c-2 classified
all 176 unanswered elements; both OTHER_ENDPOINT probes answered 200), and it stays OPEN until the HELD_DATA build
(W3-S3's remedy) and the OTHER_ENDPOINT re-pointing (packet section 5 item 2) answer its elements.

Clock note (the rows are not edited): W3-S2 and W3-S3 carry `surfaced_at` 2026-10-05T00:30:00Z, which was ahead of the
wall clock when they were filed and at this compile's read (2026-10-05T00:20Z). The worker reports the true filing time as
~2026-10-04T22:52Z, and the commit that added both rows (c41213cc7f, 0.9.0_WK_IRPT_YCDGEN~3) is authored
2026-10-04T22:52:25Z. This compile's watermark is therefore 2026-10-05T00:30:00Z, the latest surfaced_at compiled, so that both rows
sit at or before it; a row surfaced between this read and 2026-10-05T00:30:00Z falls inside it, so this compile owes its
disposition (the stricter reading).

```json
[
  {
    "id": "IRPT_YCDGEN-S3",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C-SESSION says a firewall challenge STOPS research and files a row. The round-1 runner stopped close runs 2 and 3 at step 7 (a 202 with x-amzn-waf-action, WAF_REFRESH_REQUIRED) and released the lease, but it had no row-filing path, so neither stop was filed until this seat's row S3. Round 2's cell YCD-r-2 added the path: on any STOP the runner writes a surprise-row-shaped stop_row.json beside run.json after the lease is released, and file_stop_row.py prints the channel section for the issuer to file. The path is pinned by tests and has not run live (neither round-2 run stopped), and the step-7 call that draws the challenge is still in the Overview map.",
    "evidence": [
      "investigation row IRPT_YCDGEN-S3",
      "infra/aws/lambda/investor-reporting/ycharts/research/runner.py:141-143, :212-216 and :223-234 at CLOUD HEAD a2a65ff7cc: on a STOP the run writes stop_row(...) through `stops` after the lease is released, and a failed write is noted in stop_reason (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)",
      "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner.py at CLOUD HEAD a2a65ff7cc: test_a_challenged_call_writes_a_stop_row_naming_the_step_and_decision_and_the_lease_is_released, test_stop_row_for_a_lease_refusal_and_a_release_failure_but_not_for_a_complete_run_or_a_plain_failure, test_stop_row_that_cannot_be_written_is_noted_in_the_stop_reason_and_the_run_record_is_still_written; tests/test_file_stop_row.py holds 4 tests (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)",
      "drain 6c252f2efe (2.0.0_SA_COO~Y): TO-YCD-r-2 complete, merged 988a62c350; r-2.AC2 PASS (4 + 4) on the merged tree",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R2-20261004T2315Z_host_run.txt:6 and :13: both round-2 runs COMPLETE with stop_reason None; boto3 list_objects_v2 of ycharts_runs/request=YCD-R2-20261004T2315Z-A/ and -B/: run.json only, no stop_row.json (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json calls 4-12 at CLOUD HEAD a2a65ff7cc: GET /indices/table_data with indices={security_id}; step 7 is portfolio_equity_exposure, the call run 3 stopped on (run.json stop_reason WAF_REFRESH_REQUIRED at step 7, status 202) (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/DRAIN_END_PACKET.md section 5 item 5: retire the table_data indices=P: calls (steps 04-12); they answer 400/404, and step 7 draws the firewall's challenge every time"
    ],
    "remedy": "Exercise the stop row once on the resident host by driving a STOP that needs no vendor call (a lease refusal), read stop_row.json back from the run's prefix, and file it through file_stop_row.py; and retire the Overview map's table_data indices=P: calls (steps 04-12), so that no run sends the step-7 call that draws the challenge. Close on: a filed stop row whose world_is names the step and decision, and a map whose calls no longer include those steps.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "IRPT_YCDGEN-W3-S2",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The coverage classes of decomposition 2.7 (HELD_DATA, OTHER_ENDPOINT, BUILDER_ONLY) have no member for an element computable from the portfolio's own kept answer. Run 3's step 02 kept a 200 level series for the portfolio itself (shape DATA), from which periodic and annual returns, drawdowns and the risk statistics are computable, and that answer is neither security-level nor a probe. Cell YCD-c-2 placed the 10 such elements under HELD_DATA, through the holdings' fund_data series with the step-02 series named as a cross-check, so the table does not record that those 10 need no per-holding call.",
    "evidence": [
      "investigation row IRPT_YCDGEN-W3-S2",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json at CLOUD HEAD a2a65ff7cc: 176 elements, 167 HELD_DATA (157 via /indices/table_data, 10 via /charts/fund_data.json), 7 OTHER_ENDPOINT, 2 BUILDER_ONLY; the 10 fund_data rows name the kept step-02 portfolio level series as the cross-check: p2.e08, p2.e13, p6.e22, p7.e02, p7.e03, p7.e05, p7.e06, p7.e07, p7.e08, p12.e04 (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ, no figure value)",
      "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R1-20261004T1944Z/run.json: step 2 portfolio_level_series status 200, shape DATA (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ, no figure value)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round2/checks/c-2.AC1.py:34: CLASSES = {HELD_DATA, OTHER_ENDPOINT, BUILDER_ONLY}, so a fourth class fails the check until the check changes"
    ],
    "remedy": "Carry the gap to the CTO's round-2 analysis for a decision on a fourth coverage class (computable from the portfolio's own kept answer), and record the decision in the decomposition and check c-2.AC1. Either way, have the round-3 build answer the 10 elements from the kept step-02 portfolio level series before it plans any per-holding call, with the coverage table naming that path for each of them. Close on: a coverage table whose classes cover the 10 elements by the decided rule, and a run whose kept step-02 answer is the traced source of each.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "IRPT_YCDGEN-W3-S3",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The probe map's calls are planned by runner.plan_calls, whose only placeholders are {security_id}, {start} and {end}. So the map can hold neither a dashboard module route (/dashboard/*_module_data/{n} needs a dashboard id the run does not hold) nor a per-holding call (the HELD_DATA route needs holding tickers from the frozen upload). It holds two portfolio-level probes, and both answered 200 at the round-2 close. The 167 HELD_DATA elements therefore have no call that can answer them until the runner reads the frozen upload.",
    "evidence": [
      "investigation row IRPT_YCDGEN-W3-S3",
      "infra/aws/lambda/investor-reporting/ycharts/research/runner.py:34, :37 and :62 at CLOUD HEAD a2a65ff7cc: READ_ONLY_POSTS holds the scatter path only; _PLACEHOLDERS = security_id, start, end; plan_calls (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/coverage_probe_map.json at CLOUD HEAD a2a65ff7cc: 2 calls (portfolio_scatter_documented_ids POST /charts/scatter_plot_data.json; portfolio_snapshot_metrics GET /charts/general_data.json), elements empty (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R2-20261004T2315Z_host_run.txt:6-9 and :13-16; s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R2-20261004T2315Z-A/run.json and -B/run.json: both probes answered 200 in both runs (scatter shape IDENTIFIERS, snapshot DATA); run B reads changed_since_previous false for both (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ, no figure value)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_coverage.json at CLOUD HEAD a2a65ff7cc: every one of the 167 HELD_DATA rows names a per-holding call over the frozen upload's rows in via.per (this compile's read, 2026-10-04 ~23:3xZ to 2026-10-05 ~00:1xZ)"
    ],
    "remedy": "Cut a runner step that reads the frozen upload's normalized holdings (identifier and quantity) and calls the security-level routes one holding at a time inside the lease (/indices/table_data with real tickers, /charts/fund_data.json per holding), keeping each answer under C-KEEP, so the layout computes the 167 HELD_DATA elements by the weighting each coverage row states; the dashboard module routes stay out of scope until a run holds a dashboard id. Close on: a run whose kept answers carry a 200 DATA answer per holding behind every HELD_DATA element.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v3"
    },
    "closed": false
  }
]
```
