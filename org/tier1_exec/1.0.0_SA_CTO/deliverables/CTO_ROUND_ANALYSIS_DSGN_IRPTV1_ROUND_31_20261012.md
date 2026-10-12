# CTO ROUND-31 ANALYSIS -- DSGN_IRPTV1 -- answering the rounds 24-30 L10 slug (2026-10-12 ~22:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2 (bound widened by fc10 addendum 2 @696d21d55b). **Answers:**
`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v10.md` @1c481315bb (3.0.0_SA_CVO msg 6619): 8 rows
OPEN, 2 BLOCKING, ARMED 0. **No PRD addendum.** Nothing here was re-measured by this seat; every fact is the CVO's or a worker's.

## 1. Rulings

| row | ruling |
|---|---|
| **D2-W65-S1** (BLOCKING; portal wire lacks `commentary_requested`, two whole-scope tests fail at the DEV head) | **Regenerate the portal wire from the contract, first in the round.** Types only: the form still does not SEND `commentary_requested` (IRPT_ANLREQ PRD v0.4 list item 5 keeps it parked behind IRPT_BCKEND's release), so no request changes. Every later order's "no new failure" bar rests on this base. Same fix serves IRPT_BCKEND row D2-W338-S1. |
| **D2-W62-S2** (BLOCKING; React colgroup warning in shared `HoldingsBreakdownTable.tsx:294-298`) | **Grant ONE cell on that file**, render-only markup fix, on two conditions: `owned-paths-validate` finds no other live order naming the file; and every page that mounts the component (a census from the build's module graph, denominator printed) is rendered before and after with no visible change but the warning's absence. |
| **D2-W60-S1** (Total Assets base drawn by shared `CategoryViewTree.tsx`) | **Grant ONE cell on that file**, the same two conditions, because moving the base inside the card changes every page that mounts the tree. A page the census finds that a partner-firm login opens is listed in the cell's record; its PROD rides Andrew's held promote. |
| **D2-W61-S2** (print-route closure holds four changed files; WAITS_ON_ANDREW) | **Folded into Andrew's held portal promote `dell1-e7f2`** ("No for now, I would need to visual smoke that + want a breakdown"), as call 29b7 was (`CTO_RULING_DELL2_29B7_..._20261012.md`). The printed report is the client's, so the breakdown names the print route's four files. No separate ask. |
| **D2-W63-S1** (producer contract fixtures send a section the extractor cannot send; owner this seat) | **Routed to IRPT_BCKEND ~P** (`2.0.0_SA_COO~P2`) as a fixture-only cell: the producer's fixtures carry only what the extractor sends; the page's fixtures are re-derived after. No served value moves. |
| **D2-S24** (Account select ignores the header's picked account on a served answer) | A page cell, proven on a RENDERED page with an account row picked, never a test alone. |
| **D2-S22** (UNAVAILABLE/FIRM_BINDING answers say nothing on the face) | A page cell: an unavailable answer states that it is unavailable and its reason code on its face. |
| **D2-S21** (vendor report face has no validation or source line) | A page cell: the face carries the validation line and the source line from the four validation keys already on the wire. |

## 2. ENRICHMENT LIST for round 31 (ONE issuance; each build order at most three mechanical criteria)

1. The wire regeneration (W65-S1). It merges first; items 2 to 6 cut from its merge.
2. `HoldingsBreakdownTable.tsx` colgroup fix under the grant (W62-S2).
3. `CategoryViewTree.tsx` Total Assets base inside the card under the grant (W60-S1).
4. Account select from the header's pick, rendered (S24).
5. The unavailable answer's face (S22).
6. The vendor report's validation and source line (S21).

Every candidate lands on portal DEV through the CTO review lane; PROD for all of them rides `e7f2`.

## 3. Acts only Andrew can do

None new. The portal PROD promote (`dell1-e7f2`) stays his, with this project's print-route files added to its breakdown.

-- 1.0.0_SA_CTO~DELL2
