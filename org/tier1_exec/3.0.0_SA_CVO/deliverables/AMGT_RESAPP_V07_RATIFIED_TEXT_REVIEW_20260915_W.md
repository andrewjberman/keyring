# AMGT_RESAPP v0.7: ratified-text re-review

Reviewer: `3.0.0_SA_CVO~W`. Verdict: **REFUSED -- one remaining placement correction**.

PRD: `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md@164ae74e06d02030ef70dc8fd1e76030e9713e6c`.
Reviewed half: `52243c2ae8fa0739fe9b9c50d7e688f0e9f71f98147b3b0fb9c9de9ee47b9751`.
Deliveries: 23057 and 23059; author summary 23062. Prior review: `AMGT_RESAPP_V06_RATIFIED_TEXT_REVIEW_20260915_W.md@01e640925c`.

## The one correction

**At the pinned PRD's lines 149-154, move the entire italic paragraph beginning `Carriers, for the verbatim comparison L4-R makes` outside ENDPOINT.** Place it in the existing preamble's `ENDPOINT provenance and history` block, before the first top-level section, or in the addendum. Preserve its paths and pins; do not remove the source evidence or alter an outcome card.

The paragraph is useful review provenance, but it is an annotation about L4-R and the comparison just performed. It is inside the section beginning at line 140 and ending before CONTRACTS at line 359. The code fence beginning at 156 is not the section boundary. Calling lines 149-154 the "ENDPOINT preamble" in the author summary does not place them in the PRD's actual preamble.

The governing instruction remains `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`, L4-R, lines 164-167: no annotation, history or seat name inside the ENDPOINT **section**, from heading to next heading. V0.7 correctly moved the old version-history parenthetical but introduced this replacement annotation. This is the same placement rule as v0.6 R1, not a new demand for approval or a change to the product direction.

## Corrections accepted and checks completed

| Item | Result |
|---|---|
| V0.6 R1's specific version-history parenthetical | Removed from ENDPOINT and retained at 9g. Accepted; the new carrier paragraph is the sole remaining blocker. |
| V0.6 R2's count | Corrected to Eighteen. Independently counted 19 outcome cards, 18 EXERCISED and 1 APPLIED. |
| V0.6 R3's source carrier | Resolved by `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_ENDPOINT_ADDENDUM_20260915.md@2285a23678`. Read the full carrier, including its explicit explanation of L2 formation from Andrew's direct sentences. Independently extracted FWD-16..19: all four match the PRD exactly after trimming only trailing inter-card whitespace. |
| Card preservation | All nineteen v0.7 cards match v0.6 using the same anchored extraction. The first fifteen remain the prior reviewed cards; no bar is lowered, no ID is removed or reused. |
| Missing design carrier | The exact `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_PAGE_V2_DESIGN_20260915_W.md` now exists at 2285a23678. The historical missing-file finding is closed. This existence check does not certify implementation of the design. |
| Contract count | Independently enumerated ten named contracts, matching the corrected addendum. |
| Pool-reader contract | C-ONE-STORE now names `published`, the stable article identity and digest, deduplication, distinct failure states and the isolated deployment-package requirement. Compared with the full connection brief at `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_POOL_READERS_20260915_W.md@0e7de170e3`. The new contract expressly incorporates its field-level contract and acceptance examples. |
| Identity contract | C-ONE-IDENTITY carries the canonical route-boundary identity, explicit crosswalk, exchange/share-class preservation, unresolved identities, full-universe dispositions and legacy-link transition. Compared with `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_IDENTITY_20260915_W.md@b90bfdd20d`. |
| Ranking contract | C-RANKING-GENERATION carries complete generations, distinguishable successful emptiness and failure, no readable mixed generation, run identity and payload hash. Compared with `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_RANKING_RETRIES_20260915_W.md@5ae6dd04b5`. |
| Filing evidence contract | C-FILINGS-ANALYZER now requires source/excerpt hashes, a passage map, evidence resolution before quotation checking, held uncited claims, and actual exercise of the chart-driver and role-start fields. Compared with `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_FILING_EVIDENCE_20260915_W.md@a65fe406c2`. Existing FWD-9 marking and adjacent-evidence obligations remain. |
| ETF counterpart limitation | Lines 431-435 now expressly say the producer-side contract is unestablished and the read is one-sided, require snapshot/schema vintage, and disclaim any POSN signature. This resolves the prior false implication of established counterpart agreement. The producer contract remains an explicit dependency, not a verified reciprocal agreement; no POSN review is performed. |
| Reviewed-byte guard | Canonical `prd_signoff_lib.half_hashes` gives the full hash above at the pinned commit and at HEAD during verification. The stamp uses `--expect-half-hash` so a concurrent amendment cannot inherit this verdict. |

## Scope and next act

This is the delta re-review of ENDPOINT and CONTRACTS under L4-R. The brief-half supersession/coverage map remains its assigned reviewer's work. The original brief and Andrew-direct records were read in the prior review; the four new connection briefs and endpoint carrier were read at their pins in this review. No live vendor or deployment check was run or claimed.

CTO's next correction is only relocation of lines 149-154 while retaining their source pins. The accepted checks above stand for unchanged bytes. The prior-round judgments and slug are unchanged; no outcome is marked REALIZED, no order is cut, and no harvest schedule or portal promotion is authorized by this review. All artifacts remain LOCAL under the push hold.
