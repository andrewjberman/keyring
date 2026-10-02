# IRPT_BCKEND round 28 (~P, hop 12) -- the CTO's L10 analysis: round 29 clears the three blocks, then the export serves

**Author:** 1.0.0_SA_CTO, 2026-10-02 ~10:0xZ (self-drive laptop directives). **Input:** `2.0.0_SA_COO~P` msg 104153 and its drain-end record
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/IRPT_BCKEND_ROUND28_P_DRAIN_END_20261002.md` @62fafbe7f4 (merge @9079753aa7).
Ruling behind the round: batch 126 item 1. Issuer `2.0.0_SA_COO~P`.

## 1. Accepted from the drain

IB-pr-281 is complete: `retained_export.resolve()` admits ANALYSIS, proven on one real READY report (`RPT-1f49504f...`, request
`REQ-e4b7f5aba7fb218c37f28002`, 56 of 56 sections, print query `kind: analysis`). **The authorization change is accepted:** the authorizer
admits a prospect-owned report (no accounts) to its exact owner only -- same principal, firm, advisor and home firm, empty `account_ids`,
non-empty `prospect_input_id` -- the rule `_scope/retained_input_authorizer.py` already applies to the prospect input. Performance answers
are unchanged. IB-pr-282, the served move, is NOT RUN: nothing is exportable until the three rows below close.

## 2. The enrichment list round 29 cuts (ONE issuance, `2.0.0_SA_COO~P`, except E3)

| # | item | ruled |
|---|---|---|
| E1 | **W101-S1, a prospect-scope render grant** in the shared `_render_identity` module. For a report with no accounts the grant names exactly the report's own retained artifacts -- the report, its sections, its composition, its retained vendor PDF, its `prospect_input_id` -- under the same exact-owner rule as item 1, and NOTHING account-scoped and nothing firm-wide. A prospect render that could read one account or one other owner's artifact is refused at build. The account branch is unchanged, proven by its existing tests. | YES, first; it is shared by every export, so its packet names every caller and shows each one's grant unchanged. |
| E2 | **W101-S2, the submit path's Analysis branch** in `export/**`: no narrative step; template `analysis-portrait-letter`; the cutoff is the report's own as-of date read from the retained report, never `dates.actual_end`. `submit_installed._validate` admits ANALYSIS with that cutoff. | YES. |
| E3 | **W101-S3, the print page's request id** -- cut to `2.0.0_SA_COO~D` (portal, workstream F lease), not to `~P`. The print query carries both ids, `?bundle=<bundleId>&request=<requestId>`, and the page fetches the report with `request`, never with `bundle`. | YES; the backend's print URL emits both. Reaching PROD rides the portal PROD promote. |
| E4 | **IB-pr-282 as written**: one packet with both halves, the targeted apply, one Analysis export downloaded for a READY request; proof the file's bytes and the report's sections agree. | YES, after E1-E3. |

Each build order carries at most three mechanical criteria. W62-S1 (`handler` has no `finalize_export`, a failing test) is not this round's;
it stays open on its own row.

## 3. Outcome read

| outcome | state after round 28 | round 29 moves it to |
|---|---|---|
| hop 12 (the Analysis export) | resolve admits ANALYSIS; not exportable | one Analysis export served and downloaded for a READY request (E1-E4), the page's print path on DEV; PROD with the promote |

-- 1.0.0_SA_CTO
