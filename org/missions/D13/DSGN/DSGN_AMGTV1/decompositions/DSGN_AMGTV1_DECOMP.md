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

## ADDENDUM 1 (issuer, 2026-09-29 ~05:0xZ) -- ruling on row DSGN_AMGTV1-Z-W3-S1 (ARMED, disarm owner this seat)

The issuer rules inside its own decomposition (/canonical-drive obligation 7). Round 1's three cells merged into site-Z
local portal DEV 5fac7a37; every build check passes there, and `tsc -b` reads 0 errors (a planted error reads 1). One
bound regressed: `SA/__harness__/tabs.harness.cjs` (20 of 20 at the base) dies at load with MODULE_NOT_FOUND, because it
stubs no `@/ui/components/graphic/HeroGraphic` and the page now reaches it through `ThesisCards.tsx` (AV-t-3) --
`HeaderCards.tsx` (AV-t-2) avoided it only by loading the dialog lazily (row W2-S2). One DIRECT-ACT repair cell, on slot
~3's continued worker (its context holds the harness shape):

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `AV-t-4` | DIRECT-ACT: `tabs.harness.cjs` stubs `@/ui/components/graphic/HeroGraphic` (a `HeroDialog` that renders its children only when `open`, a `DialogStamp` that renders nothing, the file's other exports as inert stubs) so the harness loads the merged page again and reads CHECKS-OK 20 of 20 with every check's claim unchanged | FWD-1 (the round's bound) | `SA/__harness__/tabs.harness.cjs` | `SA/components/ThesisCards.tsx`, `SA/components/HeaderCards.tsx`, `src/ui/components/graphic/HeroGraphic.tsx` | LOCAL |

Chain: one cell, slot ~3, after AV-t-3 drains. Base (merged DEV 5fac7a37): AC1's bound reads 3 of 4 (tabs rc=1; errorEmpty, drafting, thesisLadder green).

## 7. FINDINGS AT THE CUT (for the drain-end read)

- The overlay's header figures already carry `currency` per figure (e.g. PX_LAST `USD`), which the PRD's C-ASKS table
  reads "open" for "every money figure carries its currency". Measured on VLO only; FWD-4's round reads the census.
- Rows carry no company name and no classification (32 of 32 on the 2026-09-25 generation); the overlay carries `NAME` in
  vendor all-caps. The page does not join one into the other (C-PRESENTATION-ONLY).

---

## v2 -- ROUND 2 (issuer, 2026-09-29 ~07:4xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the ENRICHMENT LIST of `1.0.0_SA_CTO~Z`'s round-1 analysis `ledger/ROUND_ANALYSIS.round1.md` @80dc63c5d2
(msg 26481) section 5, items 1-6, one cell per item. Item 2's Model half comes from the CTO's Base-case anchor decision to
this seat ("(1) is the Model tab's and Recommendation's order"; `CTO_RULING_RESAPP_BASE_CASE_ANCHOR_20260929.md`): the
Recommendation half is `AV-e-2`, the Model half rides `AV-e-4` (same write set as the Model line names). NOT cells: hop 3's
served name (AMGT_RESAPP round 48); the white-ground panel variants (DSGN_REBRND). **Portal base:** site-Z local DEV
`f1a90a9b` (carries AMGT_RESAPP vv-1/vv-3/vv-5 on this page). **Fixtures:** `deliverables/2.0.0_SA_COO~D/round2/fixtures/`,
captured from the adapter at the cut (read-only): Valero and INTU /thesis (INTU's `model.team_cases` all SERVED, currency null
"not stated in the pack"; Valero's all ABSENT), Valero /overlay, the 2026-09-25 Trending x Price payload, the two peer sets
and WMB's /thesis (Valero's posture comparable). **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | reads | risk |
|---|---|---|---|---|---|---|
| `AV-e-1` | 1 | No raw code on the Thesis panel or the header: the chart card's absent reason, the held-uncited line and the Thesis header read as plain sentences; the header description's source line reads in words; the Thesis panel stops spending a second band | FWD-11 | `SA/tabs/ThesisTab.tsx`, `SA/components/ThesisDriverChart.tsx`, `SA/components/HeaderBrief.tsx`, `SA/__harness__/drafting.harness.cjs`, `SA/__harness__/thesisLadder.harness.cjs` | `SA/components/ThesisCards.tsx` | LOCAL |
| `AV-e-2` | 2 | The Recommendation window leads with the research team's case where served (`model.team_cases`): the team's table as written, its pack citation in words, "as written in the team's pack", labelled the team's; where not served, one sentence saying so; the machine draft follows. `types.ts` gains the team-case types | FWD-1 hop 6, FWD-6 | `SA/components/ThesisCards.tsx`, `SA/types.ts` | -- | LOCAL |
| `AV-e-3` | 3 | Every money figure in the header cards and windows prints one way: its own served currency code, then the amount; no currency served -> "currency not stated" | FWD-4 | `SA/components/HeaderCards.tsx`, `SA/components/StatTile.tsx` | `SA/constants.ts` | LOCAL |
| `AV-e-4` | 4 (+ item 2's Model half) | Model lines named in words (no vendor mnemonic on the face); each refused line says in one sentence whether the data is missing or the page cannot yet show it; the team's Base leads the cases where served | FWD-9, FWD-6 | `SA/tabs/ModelTab.tsx`, `SA/modelSheet.ts` | `SA/types.ts` (AV-e-2's team-case types) | LOCAL |
| `AV-e-5` | 5 | The lead panel's captions, resolution note and empty states read in words (no partition name); a Bloomberg ticker's literal slash never reaches the face (`BP/ LN` -> `BP LN`); `ResolutionNote` exported | FWD-2 | `SA/components/LeadPanel.tsx`, `SA/components/RankedList.tsx`, `SA/components/GenerationCaption.tsx` | -- | LOCAL |
| `AV-e-6` | 6 | The Posture tab's storage paths, read-failure codes and project codes read as words | FWD-10 | `SA/tabs/PostureTab.tsx`, `SA/postureCites.ts` | -- | LOCAL |

**Edges and chains:** one real data dependency -- `AV-e-4` consumes `AV-e-2`'s team-case types in `types.ts`, so they are one
chain on one worker's queue (e-2 then e-4). Every other write set is disjoint and consumes nothing. M = 5 chains
(e-2->e-4, e-1, e-3, e-5, e-6), N = 5, cap 8. No shared-file hookup: every new export is imported by its own cell's file.

**Checks (files under `round2/checks/`, dry-run at base f1a90a9b):** `raw.cjs <surface>` thesis 5 / header 1 / model 64 /
posture 20 hits (FAIL as expected; its pattern controls: positive TRENDING_PRICE, CIE_DES, a .json path and an s3 key hit,
plain prose reads 0); e-2.AC1 1 of 3, e-2.AC2 1 of 3, e-3.AC1 0 of 3, e-4.AC2 1 of 3, e-5.AC1 3 hits + ResolutionNote not
exported, e-5.AC2 1 of 3 (all FAIL as expected); bounds E1-E6 PASS (floor control posture 33 RED). No scratch green arm
was fed this round (round 1's were); a check that cannot pass surfaces as a worker row.

**Battery:** comp-schedule, comp-iam: DECLARED-NOT-APPLICABLE (no cadence; no AWS call; fixtures read by the issuer).
comp-adversary: the checks above; blind spots -- static markup with estate chrome stubbed (bands, contrast and layout are the
walk's); the raw-code census reads visible text only; `exportCompare` (FWD-30's page/export parity) errors at the base
(rc=2) and bounds no cell -- a Model line renamed on the page and not in the export is the walk's and the CVO's to see.

**Rule 24:** (i) MECE over the declared domain, the analysis's six items, by subtraction: 6 placed, 0 unplaced; item 2 split
by write set (Recommendation / Model) per the CTO decision. (ii) One cell per write set. (iii) One intent per cell, except
`AV-e-4`, which carries two presentation intents on one file set (named). (iv) State coherence: no cell moves a served
value, the click, row order, the verdict face, or any figure's number.

**Finding at the cut (row DSGN_AMGTV1-Z-S1):** Valero's team cases are all ABSENT (as are PBR, BA, HD, NU; INTU's are
SERVED), so FWD-1's hop 6 cannot show the team's position on the thread's own name even after `vv-4` lands.

**v2 ADDENDUM 2 (issuer, 2026-09-29 ~08:3xZ) -- a harness anchor AV-e-3 staled; the issuer's cut defect.** At the round's
close census (DEV 1a1e8162) `shell.harness.cjs` (10 of 10 at the round base f1a90a9b) reads 9 of 10:
`card_window_carries_provenance` is anchored on the literal `>$162B<`, and AV-e-3 correctly prints every money figure as
its served currency code then the amount. AV-e-3's bound did not name the shell harness (red at round 1's base, green again
at this round's) -- the cut's omission, not the worker's. One DIRECT-ACT cell, on slot ~6's continued worker:

| cell | what it builds | serves | writes | reads | risk |
|---|---|---|---|---|---|
| `AV-e-7` | DIRECT-ACT: `shell.harness.cjs`'s `card_window_carries_provenance` re-anchored onto the money form the page now prints (the market cap as its served currency code then the amount, e.g. `>USD 162B<`, or the amount and "currency not stated" when the fixture's figure carries no currency); its claim (the price window carries the mnemonic in an attribute and the value formatted for reading) kept; nothing else moves | FWD-4 (the round's bound) | `SA/__harness__/shell.harness.cjs` | `SA/components/HeaderCards.tsx`, `SA/components/StatTile.tsx` | LOCAL |

Base (DEV 1a1e8162): SHELL bound 2 of 3 (shell 9 of 10, RED).

---

## v3 -- ROUND 3 (issuer, 2026-09-29 ~10:0xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the ENRICHMENT LIST of `1.0.0_SA_CTO~Z`'s round-2 analysis `ledger/ROUND_ANALYSIS.round2.md` @172d3d9600 (msg 26551)
section 4, items 1-5, one cell per item, with the CTO ruling @06d51bce50 (W4-S1 (a) is item 3). NOT cells: the served name and
the export's wording from one source (AMGT_RESAPP round 48). **Portal base:** site-Z local DEV `670f29e4`. **Fixtures:**
`deliverables/2.0.0_SA_COO~D/round3/fixtures/` (adapter at the cut; `team_cases` now served): Valero (base ABSENT, the dossier's
reason "no BASE CASE section in class A missing or class B missing"), INTU (base SERVED; management ABSENT ZERO_OFFICERS),
SAP GY (EUR listing, base SERVED, team unit "$" as written -- the walk's non-USD name), WMB, peer sets, the ranking.
**Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | risk |
|---|---|---|---|---|---|
| `AV-r-1` | 1 | Every machine string the CVO named off the face -- "(S13)", "crosswalk/v1", "generation: none ...", the lead source line (generation id, state, blp_client 127.0.0.1:8194), "WMB_US_Equity", "claude-opus-5", "BLOOMBERG SESSION: NOT REPORTED" -- into words or behind a details affordance a PM opens on purpose; the Posture panel header white (one band) | FWD-11, FWD-2, FWD-10 | `SA/components/SecurityOverlay.tsx`, `HeaderBrief.tsx`, `GenerationCaption.tsx`, `LeadPanel.tsx`, `IdentityLine.tsx`, `SA/tabs/PostureTab.tsx`, `SA/postureCites.ts`, harnesses `tabs`, `shell`, `errorEmpty`, `leadPanelPattern`, `posture`, `posturePattern` | LOCAL |
| `AV-r-2` | 2 | The team-case absence names the gap the page can see: field not carried -> "not served on this page yet"; served ABSENT -> "not in the pack" with the dossier's reason carried on the element; INTU renders the served case -- in the Recommendation window and the Model tab | FWD-6, FWD-1 hop 6 | `SA/components/ThesisCards.tsx`, `SA/tabs/ModelTab.tsx` (the team-case element only) | LOCAL |
| `AV-r-3` | 3 | FWD-30's page/export parity harness keys on the data the page carries (`data-model-line-refusal`, `data-model-case-formula`, the line identity) and reads the cites inside the card windows; a real figure, cite or absence difference still fails it | FWD-30 parity (W4-S1 (a); closes AMGT_RESAPP Z-S297) | `SA/__harness__/exportCompare.harness.cjs` | LOCAL |
| `AV-r-4` | 4 | Exec Management's absence reads as a sentence saying where the officer list was looked for; the codes ride attributes | FWD-7 | `SA/tabs/ExecManagementTab.tsx`, harness `execPattern` | LOCAL |
| `AV-r-5` | 5 (batch, last) | The Model panel header white (one band); no page-side formatter prints a "$" it was not served (StatTile's legacy path); the Thesis chart caption names its line in words | FWD-11, FWD-4 | `SA/tabs/ModelTab.tsx` (the header), `SA/components/StatTile.tsx`, `SA/components/ThesisDriverChart.tsx`, harness `modelPattern` | LOCAL |

**Edges and chains:** AV-r-5 re-touches `ModelTab.tsx` after AV-r-2 (a batch cell runs last): one chain, one worker queue (r-2
then r-5). The rest are disjoint and consume nothing. M = 4 chains (r-2->r-5, r-1, r-3, r-4), N = 4, cap 8.

**Checks (`round3/checks/`, dry-run at base 670f29e4):** named.cjs 14 hits over 4 surfaces (FAIL); band.cjs posture and model
1 estate band header each (FAIL; thesis PASS, the control); team.cjs window 1 of 3, model 1 of 3 (FAIL); exec.cjs 2 of 3
(FAIL); money.cjs 2 of 3 (FAIL); RESAPP's vv-5.AC1.sh "NO" (FAIL: ABSENCES page 7 vs export 17); parity-ctl.sh YES (control:
deleting one counted export absence moves the export's count 17 -> 16 and the harness fails); bounds R1 6/6, R2 3/3, R4 2/2,
R5 3/3 (PASS); floor control (execPattern floor 10) RED. `census.cjs` is the CVO's instrument (decision 2): it prints every
visible non-prose token per surface for judgment and grades nothing; at base 40 tokens over six surfaces.

**Battery:** comp-schedule, comp-iam DECLARED-NOT-APPLICABLE. comp-adversary: the checks above; blind spots -- static markup,
estate chrome stubbed; no served fixture carries a Thesis chart, so AV-r-5's caption is graded by the walk only; the bound's
harness pattern cannot read `execText`/`execFallback` (they exit 0 with non-standard output), so they bound no cell.

**Rule 24:** (i) MECE over the analysis's five items, by subtraction: 5 placed. (ii) One cell per write set. (iii) One intent per
cell except AV-r-5, the named batch. (iv) No cell moves a served value, a figure, a verdict, a cite or the click.

## v4 -- ROUND 4 (issuer, 2026-09-29 ~14:xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the ENRICHMENT LIST of `1.0.0_SA_CTO~Z`'s round-3 analysis `ledger/ROUND_ANALYSIS.round3.md` @46d28c6c4c (msg 26587)
section 4, items 1-6, one cell per item; decisions 1 (`Z-S3`) and 2 (tickers as written, round-1 ruling 3 reversed) are cells 1
and 2. **NOT cells:** "$1,234" in INTU's drafted prose and the chart caption (the analysis's own list); AMGT_RESAPP r48's ask
(msg 26588 from `2.0.0_SA_COO~Z`: read `model.line_names` / `formula_words` from the payload, and let the export print words):
its dependency is unmet at the cut -- `AMGT_RESAPP.TO-AMGT-ww-1` (the redeploy) reads `pending` and 0 of 4 captured /thesis
payloads carry either field -- so it is placed for the first round after ww-1 lands, never a fixture. **Portal base:** site-Z
local DEV `a93071b8`. **Fixtures:** `deliverables/2.0.0_SA_COO~D/round4/fixtures/` (adapter at the cut): the round-3 set plus
`rankSeries.TRENDING_PRICE.12.json` (`read_rank_series` over the list's head 12 names, 5 landed dates, read complete 60 of 60
keys). **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | risk |
|---|---|---|---|---|---|
| `AV-w-1` | 1 | The walk harness FAILS when any step lands on the sign-in page ("WALK VOID: step <label> landed on the sign-in page", non-zero exit); a `--no-login` run is the positive control; the detector is a pure exported function | the round's instrument (`Z-S3`) | `.claude/skills/ui-walk/walk.mjs`, `signin_detect.mjs` (new), `SKILL.md` | LOCAL |
| `AV-w-2` | 2 | The lead list prints each ticker as Bloomberg writes it ("BP/ LN", "WALMEX* MM", "NG/ LN"); round 2's slash strip reverted | FWD-2 | `SA/components/RankedList.tsx`, harness `leadPanelPattern` | LOCAL |
| `AV-w-3` | 3 | The Model face carries no status word ("REFUSED --" x18, "ABSENT --", "SERVED --", "not read", "Peers V" / "Divergence D"): plain sentences; every refusal stays on its element | FWD-11 | `SA/tabs/ModelTab.tsx`, harnesses `modelPattern`, `assembled`, `exportCompare` (re-anchor only) | LOCAL |
| `AV-w-4` | 4 | Exec Management: the panel header white (the last second band); the "Read detail" drawer and the Bloomberg-fallback line read as words (no `roster_status`, `source_accession`, UNRESOLVED-SOURCE, upper-case ABSENT) | FWD-7, FWD-11 | `SA/tabs/ExecManagementTab.tsx`, harnesses `execPattern`, `execText`, `execFallback` | LOCAL |
| `AV-w-5` | 5 | Posture evidence: the comparable's missing sources said once; figure cites read as words (no `OPER_MARGIN FY2025 ... PERCENT`) | FWD-10 | `SA/tabs/PostureTab.tsx`, `SA/postureCites.ts`, harnesses `posture`, `posturePattern` | LOCAL |
| `AV-w-6` | 6 | The history view with ten or more names: the list's head 12 requested; one legend of per-name buttons; a picked name drawn full and the rest muted; 12 distinct strokes; dates thinned so they do not overlap; each line labelled by the served name when the series carries one, else the ticker as written | FWD-3 (first cut) | `SA/components/RankedChart.tsx`, `SA/constants.ts` (`RANK_SERIES_TOP_N`), harness `leadPanelPattern` | LOCAL |

**Edges and chains:** no data edge. `AV-w-2` and `AV-w-6` both may re-anchor `leadPanelPattern.harness.cjs` (it loads the list and
the chart): one worker queue, w-2 then w-6. M = 5 chains (w-1, w-2->w-6, w-3, w-4, w-5), N = 5, cap 8. `tabs.harness.cjs` is
read-only for every cell (a bound only); a red there is a row, never an edit.

**Checks (`round4/checks/`, dry-run at base a93071b8):** walkvoid.sh NO (the walker refuses the unknown `--no-login` and prints no
WALK VOID line); detect.mjs 0 of 6 (module absent); ticker.cjs 2 of 5; status.cjs 1 of 3 (29 hits per surface); exec.cjs 0 of 3;
posture.cjs 1 of 3; history.cjs 0 of 5 -- every build check FAILS as expected. Bounds at base PASS: leadPanelPattern 15, shell 10,
modelPattern 12, tabs 20, execPattern 9, execText 5/5, execFallback 5/5, posture 32, posturePattern 13, errorEmpty 12,
chart.harness rc 0; RESAPP vv-5.AC1 YES (4 of 4 sets exact). Green arms fed (scratch overrides, never on a face): ticker.cjs 5 of
5; history.cjs 4 of 5 (arm 1 reads the real constants file). `census.cjs` gains a status-word class and admits a ticker's own
"/" or "*": 35 tokens at base, 29 of them status words -- the CVO's instrument, graded by judgment.

**Battery:** comp-schedule, comp-iam DECLARED-NOT-APPLICABLE. comp-adversary: the checks above; blind spots -- static markup with
the estate chrome stubbed and recharts replaced by a prop-serialising stub (history.cjs reads props, not pixels: tick overlap is
graded by the walk); walkvoid.sh needs the 5174 build serving and reads only the signed-out branch; no served series carries a
company name today, so AV-w-6's name label is exercised on its ticker fallback only (the series name is an ask to AMGT_RESAPP,
the same boundary as hop 3).

**Rule 24:** (i) MECE over the analysis's six items, by subtraction: 6 placed; the three NOT-cells named with their reason.
(ii) One cell per write set, the one shared harness resolved by a queue. (iii) One intent per cell. (iv) No cell moves a served
value, a figure, a verdict, a cite or the click; AV-w-6 changes how many of the producer's already-ordered head rows the chart
requests (5 -> 12), never which or in what order.
