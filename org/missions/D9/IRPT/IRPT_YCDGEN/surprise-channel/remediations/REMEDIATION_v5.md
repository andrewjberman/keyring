# IRPT_YCDGEN -- round 5 remediations (the fifth compile of the project's channel)

<sweep_watermark>2026-10-05T12:58:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~19:5xZ. Graduated at round 5's L9 (`adjudications/ADJUDICATION_v5.md`, which dismisses
W1-S2, W2-S7, W2-S8 and W3-S7), round label v6 (the round after REMEDIATION_v4's v5). L8 inputs as named there:
INVESTIGATION_v1.md at CLOUD HEAD 7acefc344b (33 rows, 6 after REMEDIATION_v4's watermark), the round-5 drain-end packet
@043a6cc2d1, the E4 leg 1 close record, and this seat's reads at CLOUD HEAD 7acefc344b (read-only AWS; no YCharts
call). 2 rows, both OPEN, OBSERVATION and INERT: W2-S9 (the risk statistics compute one window of the five the page
prints; owner 2.0.0_SA_COO~Y) and W2-S10 (a held value prints at any coverage; owner 1.0.0_SA_CTO, a decision). 0 rows
stay ARMED. In-place clock advances on REMEDIATION_v3 (W4-S4 REMEDIATED on m-5.AC3 PASS; W2-S4 REMEDIATED on the six
wired statistics) are listed in ADJUDICATION_v5's header. The watermark is the latest surfaced_at compiled (W2-S10),
behind the wall clock at this compile's read.

```json
[
  {
    "id": "IRPT_YCDGEN-W2-S9",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Contract 4.3 names alpha, beta, Sharpe and Sortino for 1y, 3y, 5y, 10y and 15y, and the source page prints five windows per statistic. YCD-p-5 wired each of the six p7 elements to one statistic id, its 1y window, because compute_element reads one `statistic` per element and the risk-free series the wiring names (the portal's FRED 3M Treasury yield object) is coded for a 2-year history, so a 3y or longer window would read SERIES_TOO_SHORT. Each p7 element therefore prints one value where the page prints five. Three other OWN_SERIES elements (p2.e08, p2.e13, p6.e22) still carry statistic null and read STATISTIC_UNKNOWN:None. The issuer accepted this for round 5 and carried a longer risk-free history and a per-column compute to its packet.",
    "evidence": [
      "investigation row IRPT_YCDGEN-W2-S9",
      "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-p-5.budgeted-overview-map-and-statistics-wired.md record face, DRAIN (2.0.0_SA_COO~Y): W2-S9 ACCEPTED -- only the 1y window computes; a per-column compute and a longer risk-free history are carried",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json at CLOUD HEAD 7acefc344b: p7.e02, e03, e05, e06, e07, e08 statistic alpha_1y, beta_1y, sharpe_1y, sortino_1y, max_drawdown_1y, var_monthly_1y (this compile's read, 2026-10-05 ~19:4xZ to ~19:5xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R4.md contract 4.3 (the statistic ids and their windows)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/DRAIN_END_PACKET.md @043a6cc2d1 section 5 item 1"
    ],
    "remedy": "Name a risk-free series whose history covers the longest window the page prints and whose last observation is current at the run date, and build a per-column compute so each p7 element returns one value per printed window. Decide the three statistic-null OWN_SERIES elements (p2.e08, p2.e13, p6.e22) the same way: a statistic id or a recorded not-available reason. Close on: a layout test in which each of the six p7 elements returns a value or a named reason for every window its columns list, and a run or render whose trace shows no STATISTIC_UNKNOWN:None for an Overview element.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v6"
    },
    "closed": false
  },
  {
    "id": "IRPT_YCDGEN-W2-S10",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Contract 3.5 makes a computed element NOT_AVAILABLE below 0.95 coverage. The issuer ruled at spawn and at the drain that the floor does not apply to an OPAL_HELD element: its value is renormalized over the holdings Opal holds a figure for, and the held-of count goes in the trace and on the page. The census (row W3-S7) measures those figures on at most 37 of Y-5's 99 holdings, all single stocks, so a sector or region share prints as the portfolio's while describing roughly a third of its holdings. PRD C-BUILDERONLY allows an element rebuilt from data Opal holds with its method stated, and forbids an element approximated to look like YCharts' figure. Which of the two a renormalized partial-coverage value is has not been decided by the PRD's author. No such value has been rendered yet: the loader's first live read is E6, which has not run.",
    "evidence": [
      "investigation rows IRPT_YCDGEN-W2-S10 and IRPT_YCDGEN-W3-S7",
      "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-w-5.opal-held-elements-wired.md record face, DRAIN (2.0.0_SA_COO~Y): W2-S10 ACCEPTED -- contract 3.5's 0.95 coverage floor does not apply to an OPAL_HELD element",
      "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-h-5.opal-held-census-and-module.md record face, DRAIN (2.0.0_SA_COO~Y): Opal holds the figures for at most 37 of Y-5's 99 holdings",
      "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md:115 C-BUILDERONLY: 'rebuilt from data Opal already holds, with its method stated in the run record, or left out with a line on the report saying it is not available. No element is approximated to look like YCharts' figure.' (this compile's read, 2026-10-05 ~19:4xZ to ~19:5xZ)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/DRAIN_END_PACKET.md @043a6cc2d1 section 1 (issuer rulings W2-S10, W3-S7)"
    ],
    "remedy": "Decide, in the endpoint revision or the round-5 analysis, whether an OPAL_HELD value on partial coverage is C-BUILDERONLY's 'rebuilt with its method stated' or its 'approximated': either set a coverage floor for held values (one constant in _compute_opal_held) below which the element reads not available with the held-of count as its reason, or record that any coverage prints with the count beside it. Close on: the decision recorded in the PRD or the decomposition, and a layout test that pins the decided behaviour for an OPAL_HELD element below and above the decided coverage.",
    "owner": "1.0.0_SA_CTO",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v6"
    },
    "closed": false
  }
]
```
