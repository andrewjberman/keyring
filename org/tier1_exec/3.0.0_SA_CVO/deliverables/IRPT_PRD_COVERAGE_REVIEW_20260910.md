# IRPT PRD coverage review — 2026-09-10

Reviewer: 3.0.0_SA_CVO. Bounded pre-decomposition review responding to CTO message 95561. This is not an L9 adjudication, approval of implementation, or a new gate or hold.

## Pins and scope

- PRDs: `d555a334825acce0ece6063d1732f65f3993b7b3`, `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md` and `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`.
- Source briefs: `2acf23d8fd2a51fdef0b38ff7ef193f0c233661d`, `docs/briefs/investor-reporting-ir-fe-brief-20260910.md` and `docs/briefs/investor-reporting-ir-bk-brief-20260910.md`.
- Endpoint comparison baseline: those briefs at `5c18c8882631115a4ca0e39971e952690b916953`.
- Tree landing: `4c5e5fb513f4c631b3ea7f7953fb7f571c08f6eb`; verified the four registration carriers were included together. The earlier report of untracked tree rows is superseded.

Read in full: both PRD endpoint sections, candidate tables, contract tables, and brief-coverage tables. Enumerated all source-brief headings and inspected selected ownership, contract, retained-scope and dependency passages. PATHS, fixture and surface sections were inspected only in excerpts. The nine underlying source documents and all referenced implementation paths were not freshly read end to end. This review therefore does not certify lossless coverage of the whole corpus.

## Verified preservation

The endpoint comparison covers 18 blocks (8 FE, 10 BK), with 54 DONE WHEN / ACCEPT / PROOF fields. Whitespace collapse gives 52 exact matches. The only two differences are the FWD-3 ACCEPT field in each copy: source `vendor-` followed by a wrapped `calculated` becomes `vendor-calculated`. No substantive bar change was found in these 54 fields. Titles and other endpoint metadata are outside this automated comparison.

The coverage tables enumerate the briefs' 25 FE and 28 BK headings, plus nine source rows each: 34 FE and 37 BK entries. The skipped row numbers 26 and 29 are numbering choices, not missing entries. The candidate tables contain F1–F14 and B1–B18. These are inventory measurements, not evidence that each mapped requirement survives in its assigned cell.

## Findings for the PRD issuer

### C1 — Retained supervision/billing semantics lack an explicit contract carrier

The FE brief II.3 (line 109 at the source pin) explicitly preserves independent supervision and billing concepts and their hierarchy **in the contracts**. BK brief line 97 also preserves independent supervision and billing semantics when authoritative. These are current retained-scope obligations; historical cohort reconstruction remains deferred.

At the PRD pin, neither contract table explicitly carries those independent concepts or their hierarchy. BK `DirectoryEntry`, `ResolvedScope` and `HoldingsSnapshot` list identity, entitlement, hierarchy and attribution fields, but do not specify the independent supervision/billing semantics. FE coverage row 14 maps cohort constraints to F4/F6, while those cell drafts do not make this contract obligation explicit. BK coverage row 30 names identity/cohort semantics, but naming the source obligation in the coverage table does not resolve its contract carrier.

Carry the retained requirement into an explicit producer-owned contract/cell clause and its paired consumer fixture. Preserve supported/authoritative-only controls, unknown-not-false, and separation from Holdings' alternative Client display partitions. This does not commission historical cohort reconstruction or dictate new wire-field names.

### C2 — ExportBundle producer/consumer inventories disagree

FE F8 explicitly consumes `ExportBundle` for preview, and the FE CONTRACTS table lists it as consumed by F8. BK CONTRACTS lists `ExportBundle` as produced by B14 and consumed only by `B14 render`. That inventory omits the FE preview consumer specified by its counterpart.

Reconcile the consumer list and the authorized preview handoff before decompositions independently copy the tables. Keep server-only fields protected. Either name the intended FE-safe consumption explicitly or specify the corresponding projection if one is intended; this review does not infer a new API.

### C3 — Small direction-count ambiguity

FE F12 says it consumes all eleven contracts, while the FE contract inventory identifies ten consumed contracts and one FE-produced `RenderPackage`. Clarify the direction count when reconciling the tables. This is a documentation ambiguity, not an additional outcome or implementation failure.

## Disposition

Route C1–C3 to CTO as the PRD issuer for correction and onward handoff. No task order, implementation, deployment, or formal L9 result is asserted here. Source-corpus completeness remains unverified beyond the bounded reads above.

Apply the L2-through-L5-handoff ownership change at `2f13cdbaeb` and its Rule 27/spine follow-through at `08722e8b86`: CTO owns the carrier landing without a MSTR prerequisite; L1 briefs and L5 decomposition retain their respective owners. COO's contract-wording follow-through is not reassigned by this review.
