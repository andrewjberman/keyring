# IRPT_YCDGEN -- ROUND-2 ANALYSIS (L10) and the round-3 enrichment list

Author `1.0.0_SA_CTO`, 2026-10-05 ~00:3xZ. On `3.0.0_SA_CVO`'s slug (msg 105050), grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND2_L9_GRADE_20261005.md` @bf98bfc1fb (3 of 3 orders terminal; ADJUDICATION_v2,
REMEDIATION_v2: S2 dismissed; S3, W3-S2 and W3-S3 OPEN for `~Y`; 0 ARMED). Issuing lane `2.0.0_SA_COO~Y`. PRD v0.1, unchanged.

## 1. Where round 2 landed

- **The Overview map is complete (m-2.AC4 PASS):** 17 of 17 charts, the four vector-drawn ones included; 158 of 158 numbers; all 14
  physical tables; both small gaps fixed.
- **No client figure in git (c-2.AC3 PASS):** 705 numeric tokens checked, 0 figure values, every match structural.
- **The coverage table answers round 1's question.** Of the 176 elements with no live answer (`overview_coverage.json`, this seat's
  count):
  - **167 HELD_DATA:** computable from security-level answers weighted by the portfolio's holdings, which Opal holds.
  - **7 OTHER_ENDPOINT:** both probe routes now answer 200 for a model portfolio (scatter POST with the documented metric ids;
    `general_data` with `xAxis=metrics`).
  - **2 BUILDER_ONLY.**

  **An Opal-branded Overview can carry all but 2 of its 253 elements, each traced to a kept answer or to a stated computation over
  held data.**
- **FWD-1:** the fresh link was printed to Andrew at ~22:1xZ; his opening it is not on record. It is approved (his card 1, ~22:0xZ).
- **FWD-2:** the false arm is live (run B against run A). The true arm is pinned only by tests.
- **Carried defect (no row yet):** the keeper labels the scatter answer IDENTIFIERS although it carries `data.series`.

## 2. The round-3 enrichment list (ONE issuance, `~Y`)

| # | item | outcome | risk |
|---|---|---|---|
| E1 | **Build the 167 HELD_DATA elements** into the Overview layout. Each is computed from kept security-level answers weighted by the portfolio's holdings, and the run record states the method beside the element, with its inputs' kept keys (C-BUILDERONLY: "rebuilt from data Opal holds"). Never imitated. Where a weight or an answer is missing, the element reads not available with the reason | FWD-1, FWD-3 | LOCAL (build) |
| E2 | **Wire the 7 OTHER_ENDPOINT elements** through the two probed calls, kept and labelled like every call (C-KEEP), one at a time inside the lease | FWD-1, FWD-3 | WORLD (vendor reads under `~Y`'s word) |
| E3 | **The keeper's shape rule recognizes `data.series` as DATA,** with a test on the scatter answer. Re-label the round-2 kept objects by a new run, never by rewriting kept bytes | FWD-2 | LOCAL |
| E4 | **The three open rows S3, W3-S2 and W3-S3,** in the order the channel gives them | as each row names | by row |
| E5 | **FWD-2's true arm, live.** The round-3 close run on a new trading day records `changed_since_previous: true` for every price-bearing call against the round-2 run, and `false` for any static one. Prices move day over day, so this is the ordinary next run, not an engineered change. It is not a wait: the close runs when the build lands | FWD-2 | WORLD |
| E6 | **The Comparison and Multi maps,** by the same method as the Overview (m-1/m-2) over the retained certified PDFs: Multi from Y-3, Comparison from REQ-e4b7f5ab or REQ-7ea49c2d. These are maps only; their layouts come in round 4 from these maps' coverage | FWD-3, FWD-4 | LOCAL |

Each build cell carries at most three mechanical criteria (spine v3.18). The round-3 close run builds the fuller Overview (E1 + E2) and
puts a fresh link to Andrew if he has not yet opened the run-3 report; FWD-1 realizes on whichever report he opens.

## 3. Acts only Andrew can do (this project)

- **Open the Opal-branded Overview** (approved, card 1; not yet on record).

-- 1.0.0_SA_CTO
