# IRPT_YCDGEN -- round 4 remediations (the fourth compile of the project's channel)

<sweep_watermark>2026-10-05T06:43:17Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~09:15Z. Graduated at round 4's L9 (`adjudications/ADJUDICATION_v4.md`, which dismisses
W3-S5, W2-S6, W4-S5, W4-S6 and S8), round label v5 (the round after REMEDIATION_v3's v4). L8 inputs as named there:
INVESTIGATION_v1.md at CLOUD HEAD 742b4665df (27 rows, 7 after REMEDIATION_v3's watermark), the round-4 drain-end packet
@742b4665df, the round-4 close records, and this seat's reads at CLOUD HEAD 742b4665df (read-only AWS; no YCharts call).
2 rows, both OPEN, OBSERVATION and INERT, owner 2.0.0_SA_COO~Y: W3-S6 (the benchmark and risk-free inputs never reach
the computation) and S7 (FWD-2's true arm is exercised only on a changed request; the flag cannot tell a changed request
from a changed answer). 0 rows stay ARMED. In-place clock advances on REMEDIATION_v3 (S4 REMEDIATED; W4-S4 stays OPEN, m-4.AC3 FAIL on eight label and row items) are listed in ADJUDICATION_v4's header. The watermark is the latest surfaced_at compiled
(S7 and S8), behind the wall clock at this compile's read (2026-10-05T09:15Z).

```json
[
  {
    "id": "IRPT_YCDGEN-W3-S6",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Contract 4.3 builds alpha, beta, Sharpe and Sortino from a benchmark series kept by the run and a risk-free series Opal holds, but names neither the series' form nor how they reach the computation. YCD-l-4 took both as optional level series passed as benchmark= and risk_free= to statistic_of, compute_element and compute_all, and the issuer confirmed those conventions and ruled that a held yield is converted by the wiring cell. At CLOUD HEAD 742b4665df both render paths call compute_all(run_doc, kept, map_doc) with no benchmark and no risk-free series, the Overview map's 14 non-holdings calls keep no benchmark series, and no held risk-free series is named, so on a live run every alpha, beta, Sharpe and Sortino element reads INPUT_MISSING.",
    "evidence": [
      "investigation row IRPT_YCDGEN-W3-S6",
      "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-l-4.layout-six-statistics.md record face, DRAIN (2.0.0_SA_COO~Y): W3-S6 conventions CONFIRMED; a held yield is converted by the wiring cell",
      "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py:703 and :811 at CLOUD HEAD 742b4665df: compute_all called without benchmark or risk_free (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json at CLOUD HEAD 742b4665df: 36 calls, the 14 without expand all portfolio_* (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R4.md contract 4.3 (inputs: a benchmark series kept by the run, a risk-free series Opal holds)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round4/DRAIN_END_PACKET.md @742b4665df section 4 item 2 (wire a benchmark series kept by the run and a risk-free series Opal holds, per element)"
    ],
    "remedy": "Wire the two inputs: add a kept benchmark series to the Overview's run inside the call budget, name the risk-free series Opal holds and convert it to a level series where it is a yield, and pass both into compute_all from the render path. Close on: a layout test that renders the Overview map's alpha, beta, Sharpe and Sortino elements from a run fixture carrying a kept benchmark and the held risk-free series, and one live run whose run.json traces each of those elements to a value or to a reason other than INPUT_MISSING:benchmark or INPUT_MISSING:risk_free.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "IRPT_YCDGEN-S7",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C-KEEP computes changed_since_previous from the same call's previous kept sha256 for the same portfolio, and the runner keys that previous sha256 by call name alone (runner._previous_hashes). /charts/fund_data.json returns the whole level series whatever startDate and endDate say, so a different --end cannot change an answer: runs A and B (zoom=max, --end 2026-09-30 and 2026-10-02) kept byte-identical answers, as did D and E (no zoom). The issuer then produced a true reading with runs F and G, which send one call name with zoom=5y and then zoom=max; G reads true against F. That true reports a changed request, not a changed answer to the same request: G's zoom=max answer is byte-identical to run A's of 05:56Z. FWD-2's true arm on an unchanged request has not been exercised, and the flag as built cannot tell the two apart.",
    "evidence": [
      "investigation row IRPT_YCDGEN-S7",
      "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R4-20261005T0552Z-A, -B, YCD-R4-20261005T0620Z-D, -E, YCD-R4-20261005T0700Z-F and -G run.json: level-series sha256 539579bbaee2.. in A, B and G, 04f9de536ee8.. in F, ef306d6162e1.. in D and E; changed_since_previous false in B and E, no_previous in F, true in G (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ, no figure value)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/e5_zoom_5y_map_r4.json and e5_zoom_max_map_r4.json: the same two call names and parameters except zoom (5y, max)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R4-20261005T0700Z_host_run.txt: runs F and G COMPLETE, 2 calls each, 07:07:48Z and 07:08:09Z",
      "infra/aws/lambda/investor-reporting/ycharts/research/runner.py:155-158 at CLOUD HEAD 742b4665df: _previous_hashes maps call name to sha256 (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md FWD-2 ACCEPT ('... and whether it changed since the previous run') and C-KEEP ('computed from the same call's previous kept sha256 for the same portfolio')"
    ],
    "remedy": "Exercise FWD-2's true arm on an unchanged request: run the byte-identical level-series request (same call name, same parameters, same portfolio) again after a new trading day's close has reached YCharts, against an indexed run whose answer ends on the prior close, and read changed_since_previous true with the kept series' last date advanced. Make the flag tell a changed request from a changed answer, either by keying the previous sha256 on the call name and its request parameters or by recording a request hash beside the flag. Close on: that run's run.json, read by this seat, showing true on the unchanged request, and a runner test in which a changed parameter under one call name does not read as a changed answer.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v5"
    },
    "closed": false
  }
]
```
