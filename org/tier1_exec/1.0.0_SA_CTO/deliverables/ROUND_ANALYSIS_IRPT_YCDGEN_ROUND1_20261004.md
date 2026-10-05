# IRPT_YCDGEN -- ROUND-1 ANALYSIS (L10) and the round-2 enrichment list

Author `1.0.0_SA_CTO`, 2026-10-04 ~21:3xZ. On `3.0.0_SA_CVO`'s slug (msg 104979), grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND1_L9_GRADE_20261004.md` @2fd59da001 (4 of 4 orders terminal; ADJUDICATION_v1,
REMEDIATION_v1). Issuing lane `2.0.0_SA_COO~Y`. PRD `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` v0.1, unchanged by
this analysis.

## 1. Where round 1 landed

- **The thread ran live end to end except its last hop.** Run 3 (YCD-R1-20261004T1944Z) asked YCharts live inside the lease, kept 6
  answers on Cottonwood's research principal and built a 39-page Opal-branded Overview at its builder key. The 5 live values trace to
  their answer, and every other element carries a not-available line. **FWD-1 is NOT REALIZED only because Andrew has not opened
  the report.**
- **The round's measured finding (row W2-S3, OPEN):**
  - Of the map's 12 data calls, 2 answer with data for a model portfolio (`P:`-portfolio).
  - `table_data` and `scatter` refuse it.
  - So 176 of 249 elements have no live answer. The report is honest and thin.
- **The map misses 4 charts (m-1.AC2 FAIL):** p3 Stock Style Exposure, p3 Market Classification, p3 Region and p5 Stock Sector
  Exposure. They are drawn as vector shapes, not embedded images. Smaller gaps: p14.e03 lists 2 of 6 columns, and p13.e04 dropped a
  header word.
- **FWD-2:** every call reads `no_previous`, although run 2 kept the same calls. The previous-answer lookup is wrong.
- **FWD-6:** run 3 carries the three clocks, but there is no record of Andrew waiting.
- **New row S3:** the step-7 firewall stops filed no row, which C-SESSION requires.
- **Not yet exercised:** FWD-4 (Comparison and Multi), FWD-5 (the firm-private read) and FWD-7 (the side-by-side check).

## 2. The round-2 enrichment list (ONE issuance, `~Y`; order is the order to cut)

| # | item | outcome | risk |
|---|---|---|---|
| E1 | **The last hop of the thread.** Andrew opens the run-3 report from a fresh short-lived signed link, in `~Y`'s session, where he is. The run record notes whether he had it in the same sitting (FWD-6's evidence). The link is not stored and its query string is never logged (C-DELIVERY) | FWD-1, FWD-6 | his act |
| E2 | **The map's four missing charts and two small gaps.** Detect drawn charts as vector-shape elements, not only embedded images; list all of p14.e03's columns; restore p13.e04's header word. Re-grade m-1.AC2 | FWD-3 | LOCAL |
| E3 | **The coverage measurement for the 176 unanswered elements (W2-S3).** One read-only cell sorts every unanswered element into exactly one of three classes: (a) computable from security-level answers weighted by the portfolio's holdings, which Opal holds, under C-BUILDERONLY's "rebuilt from data Opal holds"; (b) served by a different YCharts endpoint that accepts a model portfolio, named; (c) BUILDER_ONLY. Calls are made only under `~Y`'s egress word, one at a time, inside the lease, with no extra generate call. The round-3 build is cut from this table | FWD-3, FWD-1 depth | WORLD (vendor reads) |
| E4 | **FWD-2's previous-answer lookup.** `changed_since_previous` compares a call with the same call of the previous run for the same portfolio. It reads `no_previous` only when no such run exists. A test pins the run-2 to run-3 case | FWD-2 | LOCAL |
| E5 | **Row S3.** A firewall stop files its row and releases the lease (C-SESSION), with a test | C-SESSION | LOCAL |

Each build cell carries at most three mechanical criteria (spine v3.18). Comparison and Multi (FWD-4, FWD-7) wait for E3's table, so
round 3 builds on a measured coverage map rather than on a guess.

## 3. Acts only Andrew can do (this project)

- **Open the Opal-branded Overview (E1).** FWD-1's DONE WHEN is "one live run, ending in Andrew opening the report". `~Y` puts the
  fresh link to him in its session.

-- 1.0.0_SA_CTO
