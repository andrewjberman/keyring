# AMGT_RESAPP v0.6: ratified-text review

Reviewer: `3.0.0_SA_CVO~W`. Verdict: **REFUSED**.

Reviewed PRD: `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md@2f3b65d8b842847bd31eefc63766593bcc235b42`.
Reviewed half: `f52bb3078727d373990d8df005f7db3c1c58b396aa74aa01bb714a12c9a36c3e`.
Deliveries: 23047 and 23049, the same pin and half; 23052 confirms one review is owed.

## Result and corrections by pinned line

The new page direction is present, and the fifteen earlier outcome cards are unchanged. These bytes cannot receive the ratified-text signature because ENDPOINT contains newly added history and contradictory outcome counts. The four new cards also lack a demonstrated verbatim ratified-card carrier in the cited sources. Corrections belong to the L4 author; this review edits no PRD or task order.

| Finding | PRD lines at the reviewed pin | Required correction |
|---|---|---|
| R1: version history inside ENDPOINT | 341-343 | Move the parenthetical starting `v0.6: FWD-16..FWD-19 added` and its claim about the earlier bars into the preamble or addendum. The section runs from line 137 to the next top-level heading at 351; being outside the code fence does not exempt this text from L4-R's prohibition on annotation and history inside ENDPOINT. Retain the operative bar rule. |
| R2: the outcome denominator contradicts itself | 341 and 345-346 | The cards contain nineteen outcomes, eighteen EXERCISED and one APPLIED. The adjacent operative sentence still says `Fourteen outcomes cannot be closed by any build`. Correct it to eighteen or an equivalent count-free rule that covers every EXERCISED outcome. Do not change any card's bar to repair the count. |
| R3: the verbatim ratified-card comparison is not established for the additions | 286-338, with provenance at 973-984 | Identify the pinned ratified endpoint carrier for the new DONE WHEN/ACCEPT text, or explicitly document the governing L2 ratification of these newly authored cards. The cited Andrew-direct records contain the product directions, not these four card texts. Directional agreement is supported; a verbatim comparison to a ratified card cannot be claimed from those records. Preserve the distinction in the provenance outside ENDPOINT. |

R1 and R2 independently prevent a signature. R3 is a bounded provenance finding about the sources actually cited and read, not a claim that Andrew did not authorize the new product direction. The ~05:04Z record explicitly assigns the outcome and its DONE WHEN/ACCEPT to the L2/L4 owner. This review does not require a new user approval merely because the author must repair its carrier.

## What was checked

- The canonical `prd_signoff_lib.half_hashes` over the pinned PRD yields the exact delivered full hash above. The other half is `90b966c9b31051c680ad9c5efc2a8cb4d495895682ff1627deeb02aff1e1b3ad`; it is not this seat's signature.
- A separate card extraction, anchored on each `FWD-n`, compared v0.6 with its parent. All fifteen existing cards match, including their DONE WHEN and ACCEPT text. There are four additions, no removed/reused IDs, eighteen EXERCISED bars, one APPLIED bar, and no PROOF fields in the endpoint cards.
- The initial endpoint source `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_ENDPOINT_20260910.md@3bc8f5f2c4` carries FWD-1 through FWD-14. The prior accepted FWD-15 is unchanged in this delta. No prior outcome is regraded here.
- The brief at `docs/briefs/amgt-resapp-security-analysis-20260910.md@19ce7d5b4d` supplies the existing outcome territory, qualification rules, raw-before-derived, independent reruns, source quotation gate, failure marking and identity constraints. The existing constraint sections are unchanged by this PRD commit. FWD-9's APPLIED marking/evidence rule remains operative in the new filings contract.
- The two primary new-direction records were read at their pins: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_051xZ_SECURITY_ANALYSIS_HEADER_PANEL_FOUR_TABS_FILINGS_ANALYZER.md@a5c6a066de` and `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_055xZ_TRANSCRIPT_SECURITY_ANALYSIS_PANELS_DRILL_DOWN.md@fbd5d91431`. They support the header, five surfaces, whole C-suite and comparative tenure, one company-specific chart, Bloomberg model, the shared similarity ranker and symmetric Posture over both four-tab packs.
- The ~05:04Z record was read at `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/ANDREW_DIRECT_20260915_0504Z_EXECUTIVE_MANAGERS_LUSHA_AND_THE_HARVEST_POOL.md@7cf62a165f`. It supports executive managers, Lusha enrichment and the harvest pool as the system of record, and expressly leaves outcome formation to L2/L4.
- The three substrate cards were read at `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/SUBSTRATE_CARDS.md@5007337353`. They support the citation-shape caveat, filing-first officer identity/tenure, Lusha's limited role, and reuse of the workbook/scanner shapes. They are measurements and proposed design consequences, not a ratified endpoint card carrier.

## Contracts: bounded comparison

There are **eight** new named contracts, despite the addendum's prose saying seven: C-PAGE-LAYOUT, C-ONE-STORE, C-ETF-PLANE-READ, C-UNION-UNIVERSE, C-SIMILARITY-RANKER, C-POSTURE, C-FILINGS-ANALYZER and C-EXEC-MANAGEMENT. The count correction at line 970 is an author note outside this half's body; it does not independently drive this verdict.

Their substantive direction is consistent with the records above: one header plus five tabs; one article pool with readers repointed; read-only ETF membership at a snapshot vintage; coverage union holdings; one ranker shared by Peers and Posture; two comparable evidence packs; cited, marked machine prose; confirmed officer identities before profile enrichment. No production behavior is certified by this text review.

C-ETF-PLANE-READ names the POSN_ASTTAX / ETFS_* ownership boundary. The limited counterpart inspection of `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md@ab2ee8052a7660af407a49b444979e42ee286781` found no CONTRACTS section and no occurrence of AMGT_RESAPP, opal-data-etfs, snapshot_ or 22:00. Therefore this read does **not** demonstrate a matching reciprocal producer contract for the four ETF paths and daily schedule asserted at AMGT lines 376-380. The AMGT register lists related projects, not an explicit paired PRD for that seam. Cite the actual producer contract/pin when asserting counterpart agreement; absence of those strings alone does not prove a producer conflict. No POSN review or signature is issued.

The transcript record at fbd5d91431:79-80 names `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_PAGE_V2_DESIGN_20260915_W.md` as a drafted design carrier. That exact file was absent when inspected. This is a repository provenance defect, not permission to invent a replacement. It limits the evidence for R3; it does not invalidate the transcript itself.

## Scope and next act

Authority: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`, L4-R, lines 162-167: pinned source comparison, all operative constraints, no history/annotation inside ENDPOINT, and counterpart agreement. The same section requires a pinned review and canonical sign/refuse stamp. The stamp must use `--expect-half-hash` with the full reviewed hash to avoid certifying concurrent edits.

CTO answers this refusal with a focused correction and a newly delivered current half. The round-10 judgments, remediation slug and L8/L9/L10 stamps remain the completed prior-round record. S100/S101 announced in message 23052 belong to the next compilation; this review does not advance their remediation clocks. The existing portal/push holds and harvest ownership boundary remain in force. No vendor call, deployment, worker contact or new task order was made by this review.
