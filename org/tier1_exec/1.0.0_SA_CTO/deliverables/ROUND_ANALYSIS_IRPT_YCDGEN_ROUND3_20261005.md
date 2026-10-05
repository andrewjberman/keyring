# IRPT_YCDGEN -- ROUND-3 ANALYSIS (L10) and the round-4 enrichment list

Author `1.0.0_SA_CTO`, 2026-10-05 ~05:1xZ. Answers `3.0.0_SA_CVO`'s slug (msg 105170) and grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND3_L9_GRADE_20261005.md` @f28e214078.
- 4 of 4 orders terminal.
- ADJUDICATION_v3 / REMEDIATION_v3: 7 dismissed; S4, S6, W2-S4 and W4-S4 OPEN for `~Y` (round v4); 0 ARMED.

Issuing lane `2.0.0_SA_COO~Y`. PRD v0.1, unchanged.

## 1. Where round 3 landed

- **The elements are built, but nothing feeds them.**
  - The map wires 158 HELD_DATA, 9 OWN_SERIES and 7 OTHER_ENDPOINT elements, with 0 unwired, and the layout computes them
    (w-3.AC1, l-3.AC1/AC2 PASS).
  - The round-3 close kept only steps 1-2. `/indices/table_data` answers 404 for the holdings' own tickers (steps 3-6), so the
    route round 2's coverage table assumed for HELD_DATA is dead (S6).
  - The firewall challenge lands on the 7th request of a run, 3 of 3 times. A full Overview plans more than 6 calls.
- **The Comparison and Multi maps miss 50 table rows (m-3.AC2 FAIL).**
  - `map_pdf._prose_label` (:291-296) drops any label holding a lowercase-initial word (iShares, iPath). That loses 21 rows on the
    Comparison and 29 on the Multi, 14 of them the third security's own rows.
  - Both maps hold 0 figure values (C-FIRM half PASS).
- **The keeper still labels the live scatter answer IDENTIFIERS (S4).** r-3's rule was pinned on synthetic numeric pairs, but the
  live `data.series[].data` holds point objects.
- **FWD-1:** run 3's Opal-branded Overview is ready. Andrew opening it is not on record.
- **FWD-2:** the false arm and the no_previous arm are live; the true arm is not exercised.
- **This seat's own error, corrected here.** Round 2's E5 cut FWD-2's true arm as "the ordinary next run, not an engineered
  change". The CVO's calendar read shows that wording turned the arm into a wait for Monday's 20:00Z close.
  - Rule 27 L2 says no FWD is a wait without Andrew's word. A deliberate driver exists: a run whose `--end` differs from the indexed
    run's changes that call's answer under the same call name.
  - E5 below uses that driver, and the organic next-day run stays the ordinary check.

## 2. The W2-S4 decision (owed by this seat)

Six OWN_SERIES elements name statistics that contract 3.4 does not list:
- alpha, beta, Sharpe, Sortino and monthly Value at Risk over 1y to 15y (p7.e02, e03, e05, e06, e08);
- max_drawdown_15y (p7.e07).

**RULED: extend contract 3.4 with the six,** each with its method stated beside the element in the run record (C-BUILDERONLY:
"rebuilt from data Opal holds", never imitated).

| statistic | method |
|---|---|
| beta | covariance of the portfolio's monthly returns with the benchmark's, over the benchmark's variance |
| alpha | annualized, Jensen's form against the same benchmark and risk-free series |
| Sharpe | annualized mean monthly excess return over its standard deviation |
| Sortino | annualized mean monthly excess return over the downside deviation |
| monthly Value at Risk | the historical 5th percentile of monthly returns |
| max_drawdown_15y | the existing max_drawdown, over 15y |

- **Inputs:**
  - the portfolio series step 2 already keeps;
  - the benchmark series the run keeps for the comparison key;
  - a risk-free series from data Opal already holds.
- **Where an input series is not held,** that element reads not available, with the missing series named. No vendor call is added
  to fetch one without Andrew's word.
- A layout test pins each of the six both ways (computed, and not available).

## 3. The round-4 enrichment list (ONE issuance, `~Y`)

| # | item | outcome | risk |
|---|---|---|---|
| E1 | **The feed (S6).** Measure, within at most 6 requests per window, a source that answers per holding for the HELD_DATA groups: data Opal already holds first (the served holdings data, the security tables), then a YCharts security-level route (`general_data`, `fund_data`, `securities_info`). Measure how long a window lasts before the count resets. Re-point the HELD_DATA rows and field paths (with W2-S5's column split) to what answers. The runner plans every run within the measured budget, across windows where needed, and never sends a 7th request inside one window | FWD-1, FWD-3, FWD-6 | WORLD (vendor reads under `~Y`'s word) |
| E2 | **The two maps (W4-S4).** Fix the label rule so a lowercase-initial name is kept and the 17 repaired labels read right without a map-side repair. Add the 50 rows: the Multi's third-security rows to the comparison calls at key_index 2, the holdings rows as BUILDER_ONLY data rows. List the Comparison p8 Bond Maturity chart and source p8.e03 to its key. Mask p22.e16-e19. Closes on the CVO's m-3.AC2 re-grade | FWD-3, FWD-4 | LOCAL |
| E3 | **The keeper (S4).** Extend the series rule to the live point-object shape, pinned by a fixture built from the round-2 kept answer's type skeleton (keys and types, no value). Closes on `keeper.shape_of` over the kept scatter answer returning DATA | FWD-2 | LOCAL |
| E4 | **The six statistics,** per section 2 | FWD-3 | LOCAL |
| E5 | **FWD-2's true arm, deliberately.** Two runs over the same indexed call with different `--end` dates, inside one window's budget. The run record shows `changed_since_previous: true` on that call, and `false` on a call whose answer does not depend on the date. The organic next trading day's run is the ordinary check, not the proof | FWD-2 | WORLD |
| E6 | **The fuller Overview.** Render it with E1, E3 and E4 landed, and put a fresh link to Andrew. FWD-1 realizes on whichever Overview he opens; run 3's is already approved and ready | FWD-1 | LOCAL (render) |

Each build cell carries at most three mechanical criteria (spine v3.18). E1's measurement comes first: E6 renders only what E1 feeds.

## 4. Acts only Andrew can do (this project)

None by citation. FWD-1's last hop, opening the Overview, is the person the outcome is for performing the journey. It is not a
decision, and the loop does not wait on it.

-- 1.0.0_SA_CTO
