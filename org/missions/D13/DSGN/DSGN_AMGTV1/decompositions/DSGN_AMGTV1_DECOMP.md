# DSGN_AMGTV1 -- DECOMPOSITION (L5) -- ROUND 1, THE THREAD (PRD v0.2)

```json
{
 "project": "DSGN_AMGTV1",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "site-z",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md@a4cfe729e8 (v0.2, ADMITTED)",
 "prd_half_hashes": {"ratified-text": "SIGNED by 3.0.0_SA_CVO~Z, current (prd-signoff status 2026-09-29 ~03:0xZ)", "brief": "ADMITTED (auto: the CRO wrote the brief)"},
 "order_ref": "1.0.0_SA_CTO~Z msg 26416 (L5 is yours: decompose and issue round 1 in ONE issuance over THE THREAD, hops 1-6)",
 "author": "2.0.0_SA_COO~D",
 "round": 1,
 "rectangle": "THE THREAD (FWD-1), one cell per hop adapter to build: lead-panel row (hops 2-3), header (hop 4), thesis (hops 5-6); hop 1 (real login) is served and has no cell",
 "cells": 3,
 "chains": 3,
 "join_cells": 0,
 "portal_base": "site-Z local DEV 8fa7abde (3 ahead / 141 behind origin DEV 50eb1d56, fetch read 2026-09-29 ~03:1xZ; the 3 are AMGT uu-2, uu-3 and HVST-y-3, which carry the page's current state)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~D` (site Z). **Input:** PRD v0.2 THE THREAD (:159-176), CONTRACTS (:125-157), PATHS (:187-194),
the register `docs/briefs/dsgn-amgtv1-findings-20260928.json` (42 findings), and three payloads captured from the scoped
API's own adapter at the cut (`deliverables/2.0.0_SA_COO~D/round1/fixtures/`, read-only Opal reads, no vendor call):
`rankings.TRENDING_PRICE.json` (generation 2026-09-25, 32 rows, VLO US rank 3, `security_key` VLO_US_Equity, no name
field on any row), `overlay.VLO_US_Equity.json` (18 header figures incl. `NAME` "VALERO ENERGY CORP", each carrying its
own `currency`; no volatility or trend mnemonic), `thesisBundle.VLO_US_Equity.json` (drafting SERVED from the 10-K filed
2026-02-25; investment_thesis 5 sentences / 5 passages, risks 3 / 4, recommendation 5 / 6). **Frozen at the cut.**

**Contracts reaching every cell:** C-PRESENTATION-ONLY (the page derives nothing; a missing field renders a designed
empty state naming in plain words what is missing and which team fills it, never a project code, serial or path);
C-ESTATE-FIXTURES (HeroDialog + DialogStamp for windows, the estate's panels and states; nothing forked); DESIGN.md C1-C14.
Spine L6 diet: at most THREE mechanical criteria per build cell; typecheck and repo hygiene at the drain.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: the six hops of THE THREAD. Hop 1 (real login -> portal session) is served by the portal's sign-in and
touches no page file -> no cell. Hop 2 (`/security-analysis` -> the Trending x Price list) and hop 3 (the row reads
Valero by company name) are one write set, the list row -> `AV-t-1`. Hop 4 (four header cards, Financials opening its
window) -> `AV-t-2`. Hop 5 (Thesis: three cards under the principal chart) and hop 6 (the Recommendation card's window:
whose view, each citation's document) are one write set, the Thesis tab -> `AV-t-3`. Remainder: zero hops unplaced.

What the thread cannot pass on this round, stated at the cut (both are the PRD's own named outcomes, never fixtures):
- hop 3: the served rows carry no company name (the C-ASKS row "rows carry the company name", AMGT_RESAPP, open). `AV-t-1`
  builds the consumer of the served name; until it is served the row leads with its served ticker and FWD-1 does not pass
  on a ticker (PRD :167-168).
- hop 6: the research team's recommendation is not served (the dossier route, AMGT_CORPUS, open). `AV-t-3`'s card says whose
  view the served text is (a machine draft of the 10-K) and that the team's position is not there; FWD-1 stays NOT_REALIZED
  on that hop and the route is round 2's first enrichment input (PRD :171-173).

## 2. THE CELLS -- 3 (round 1)

Paths portal-relative; `SA/` = `src/pages/SecurityAnalysis/`.

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `AV-t-1` | Each lead-panel row leads with the company name the ROW carries (`row.name`, else `row.classification.name`), its served ticker beside it; a row carrying neither leads with its served ticker. The row states which (`data-row-name-state` SERVED / NOT_SERVED). The canonical key never prints. `RankingRowBase` gains the two optional fields, typed as the ask will serve them. | FWD-1 hops 2-3 (FWD-2 later) | `SA/components/RankedList.tsx`, `SA/types.ts` (the two optional fields only) | `SA/components/LeadPanel.tsx`, `SA/components/StarredList.tsx` | LOCAL |
| `AV-t-2` | The seven stat tiles become FOUR CARDS -- Price (price; market cap, average volume), Financials (enterprise value; net debt), Market features (beta; volatility), Trading technicals (trend; average volume, short interest) -- each a button leading with its first carried figure and opening a HeroDialog window listing every figure of the card, a figure the payload does not carry named in plain words. New `SA/components/HeaderCards.tsx` exports the cards and the window body `HeaderCardDetail`. | FWD-1 hop 4 (FWD-4 later) | `SA/components/SecurityOverlay.tsx`, `SA/components/HeaderCards.tsx` (new), `SA/constants.ts` (the card definitions; `STAT_TILE_DEFS` retired or kept unused) | `SA/components/StatTile.tsx` (`formatStatValue`), `src/ui/components/graphic/HeroGraphic.tsx`, `src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx` (the pattern) | LOCAL |
| `AV-t-3` | The Thesis tab at rest is the principal chart, then THREE CARDS (Investment thesis, Risks, Recommendation), each opening a HeroDialog window with its sentences, each sentence's passages and verdict face, and every citation's document named in words from the bundle's `drafting_provenance` (form + filing date), never an accession number. The Recommendation window says whose view it is: a machine draft of the filing, and the research team's own position is not in the pack yet. New `SA/components/ThesisCards.tsx` exports the cards and the window body `ThesisCardDetail`. The two page harnesses that walk the Thesis evidence are re-scoped onto the windows with every check's claim kept. | FWD-1 hops 5-6 (FWD-6 later) | `SA/tabs/ThesisTab.tsx`, `SA/components/ThesisCards.tsx` (new), `SA/__harness__/drafting.harness.cjs`, `SA/__harness__/thesisLadder.harness.cjs` | `SA/components/ThesisDriverChart.tsx`, `SA/components/CheckFaceBadge.tsx`, `src/ui/components/graphic/HeroGraphic.tsx`; every named export of `ThesisTab.tsx` another file imports stays | LOCAL |

Status vocabulary (every cell): NOT_EVALUATED at the cut -> PASS / FAIL per criterion at the drain. All three: NOT_EVALUATED.

## 3. PLACEMENT AND BASE

Fabric site-z, every cell. Each cell is a portal cell on a worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_AMGTV1 <n> --path <abs> --portal-ref 8fa7abde`. The drain merges each chain's portal
branch into site Z's local portal DEV and runs the round's one real run: the signed-in FWD-1 walk on `localhost:5174`
(`/ui-walk --route /security-analysis --security VLO_US_Equity`, screenshots read), which grades every JUDGMENT criterion
(the CVO at L9, on the PNGs). The local-vs-origin DEV divergence (3 / 141) is the integrator's; nothing in this round
pushes.

## 4. DEPENDENCY EDGES AND CHAINS

No edge: the three write sets are pairwise disjoint (section 2 `writes`) and no cell consumes another's output (`AV-t-2`
and `AV-t-3` both READ HeroGraphic, which none writes). M = 3 chains of one cell each; N = 3; cap 8. No shared-file hookup is
needed: each new module is imported by a file its own cell writes.

## 5. BATTERY DISPOSITION

- comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence in any cell.
- comp-iam: DECLARED-NOT-APPLICABLE -- the thread touches no IAM surface; the fixtures were read by the issuer at the cut and
  no cell makes an AWS call.
- comp-adversary: RUN by the issuer at the cut, on the checks rather than the cells (each build check fed a scratch GREEN
  arm and the base): t-1.AC1 base 1 of 4 / green 4 of 4; t-2.AC1 base 1 of 3 / green 3 of 3; t-2.AC2 base 0 of 5 / green
  5 of 5; t-3.AC1 base 0 of 3 / green 3 of 3; t-3.AC2 base 0 of 8 / green 8 of 8. Bounds PASS at base (RANKEDLIST 3 of 3,
  HEADER 2 of 2, THESIS 2 of 2), and a floor control (drafting floor 9) reads RED. Blind spots, stated: the checks render
  static markup with the estate chrome stubbed, so they cannot see a dialog opening, contrast or layout -- those are the
  walk's; they read one name (Valero) plus constructed arms.
- Base harness census (19 page harnesses at 8fa7abde): 14 green; 5 already red and NOT touched by this round's bounds --
  `assembled` (needs args), `exportCompare`, `leadPanelPattern` (3 checks wrong way: source_caption_wraps,
  disclosure_own_line, caption_facts_unchanged), `posture`, `shell` (a require-stack failure). Carried to the drain-end read.

## 6. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over the declared domain, the six thread hops, by subtraction (section 1): every hop placed or served. (ii) Same
grain: one cell per hop write set. (iii) One intent per cell. (iv) State coherence: `AV-t-2` does not move the header
description, posture line, feed, timeline or axis footnote (HeaderBrief and GenerationCaption are untouched); `AV-t-3` does
not move the Thesis tab's held-uncited line, subtitle or any named export other tabs import; `AV-t-1` does not move row
order, the star toggle, the click (it still sends `security_key`) or any empty/refused state.

## 7. FINDINGS AT THE CUT (for the drain-end read)

- The overlay's header figures already carry `currency` per figure (e.g. PX_LAST `USD`), which the PRD's C-ASKS table
  reads "open" for "every money figure carries its currency". Measured on VLO only; FWD-4's round reads the census.
- Rows carry no company name and no classification (32 of 32 on the 2026-09-25 generation); the overlay carries `NAME` in
  vendor all-caps. The page does not join one into the other (C-PRESENTATION-ONLY).
