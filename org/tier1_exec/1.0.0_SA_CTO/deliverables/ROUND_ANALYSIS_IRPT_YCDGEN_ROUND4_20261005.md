# IRPT_YCDGEN -- ROUND-4 ANALYSIS (L10) and the round-5 enrichment list

Author `1.0.0_SA_CTO`, 2026-10-05 ~09:4xZ. Answers `3.0.0_SA_CVO`'s slug (msg 105226) and grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND4_L9_GRADE_20261005.md` @d6f334c003.
- 4 of 4 orders terminal.
- REMEDIATION_v4: W3-S6 and S7 OPEN. S4 REMEDIATED. W4-S4, W2-S4 and S6 stay OPEN.

Issuing lane `2.0.0_SA_COO~Y`. PRD v0.1, unchanged.

## 1. Where round 4 landed

- **The maps list every value row and chart:** Comparison 178 of 178, Multi 221 of 221, with 0 figure values. m-4.AC3 FAILS only on
  residuals:
  - R1: Multi p9's "No data available" row is unlisted;
  - R2: seven placeholder labels read "row".
- **The keeper reads the live scatter answer as DATA** (S4 REMEDIATED).
- **The six statistics are built but not wired.** The map's p7 elements still carry statistic null, p7.e08's ids do not parse, and
  `compute_all` gets no benchmark or risk-free series (W2-S4, W3-S6).
- **The feed answered 400 on all 6 requests** (S8). The 158 HELD_DATA elements are still unfed.
- **FWD-2's true arm is NOT realized.** Runs F and G changed the request (5 years against all of history), not the answer. With the
  request held fixed, the answer is byte-identical. The flag cannot yet tell a changed request from a changed answer (S7).
- **The finding that reshapes the project: FWD-6.**
  - The measured budget is 6 requests per window, with 660 s or more between windows (no challenge in 5 windows).
  - The Overview map at HEAD plans **129 requests: 22 windows, about 3 h 51 min.**
  - Andrew's bar is "It has no need to take 15-20 minutes", in FWD-6's ACCEPT: he has the report "in the same sitting".
  - At 660 s, that fits **at most 2 windows (12 requests).**

## 2. Rulings

1. **FWD-6 is binding on the plan, and the plan is cut to fit it.**
   - An Overview run sends at most 12 YCharts requests (2 windows).
   - The runner prints the planned request count and window count before the first call, and refuses a plan over budget.
   - An element that cannot be fed inside the budget reads "not available", with the reason "outside the run's time budget".
     FWD-1's ACCEPT allows this: "Every number in it can be traced to one of those answers, or is marked as not available".
   - No answer kept from an earlier run stands in for a call in this run. FWD-1 requires "answers it asked for live".
2. **HELD_DATA comes from data Opal already holds, first.** Per-holding YCharts expand calls cannot fit 12 requests for 99
   holdings. Each HELD_DATA element group is sourced from data Opal holds for the portfolio's holdings, or it reads not available
   with its reason.
3. **FWD-2's true arm.**
   - **The flag keys on the call name AND its request parameters** (a request hash beside the flag), so a changed request can
     never read as a changed answer (S7's remedy).
   - **The deliberate driver:** two runs of one byte-identical request, a window or more apart during US market hours (13:30Z to
     20:00Z today), on a call whose answer moves intraday, if the map has one.
   - **The organic case:** the first byte-identical request after today's close reaches YCharts, against the morning's indexed
     run. Its kept series' last date must have advanced.
   - Either closes the mechanism today. A multi-day wait is not cut.
   - FWD-2 realizes when a person looks one up with the one-command lookup.
4. **R1 and R2 close W4-S4.**
   - R1: list the "No data available" row as an element reading not available.
   - R2: each "row" label takes the name the PDF prints on the line above.

## 3. The round-5 enrichment list (ONE issuance, `~Y`)

| # | item | outcome | risk |
|---|---|---|---|
| E1 | **The budgeted plan** (ruling 1). The runner prints requests and windows and refuses over 12. The Overview's portfolio calls are deduplicated to those an element actually reads. The rest of the elements read not available with the budget reason | FWD-6, FWD-1 | LOCAL |
| E2 | **The Opal-held census for HELD_DATA** (ruling 2). Per element group, the field each needs, against the data Opal holds for Y-5's 99 holdings (security tables, prices, classifications), each group named FED or NOT HELD. Wire the FED groups through the layout's computed path, with the method beside each element | FWD-1, FWD-3 | LOCAL (reads) |
| E3 | **The six statistics wired** (W2-S4, W3-S6). Set each p7 element's statistic id. Fix p7.e08's VaR id to 4.3's form. Pass a benchmark series (inside E1's budget) and the risk-free series Opal holds into `compute_all`. Where either is missing, the element names it | FWD-3 | LOCAL |
| E4 | **FWD-2's true arm** (ruling 3), with the request hash. Deliberate intraday pair during market hours if such a call exists; else the first identical request after today's close. Plus the one-command lookup | FWD-2 | WORLD |
| E5 | **R1 and R2** (W4-S4) | FWD-3, FWD-4 | LOCAL |
| E6 | **The budgeted Overview, live.** One run inside 2 windows, rendered, with its timing record split into YCharts time and Opal waiting. A fresh link goes to Andrew. FWD-1 and FWD-6 realize on his one sitting with it | FWD-1, FWD-6 | WORLD |

Each build cell carries at most three mechanical criteria (spine v3.18). E1 and E2 come before E6. E4 runs today, inside market
hours or after the close.

## 4. Acts only Andrew can do (this project)

None by citation. FWD-1's open and FWD-6's sitting are the person the outcomes are for, doing the journey. The loop does not wait
on them.

-- 1.0.0_SA_CTO
