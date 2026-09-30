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


## v5 -- ROUND 5 (issuer, 2026-09-29 ~20:xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the ENRICHMENT LIST of `1.0.0_SA_CTO~Z`'s round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` @177c576c80 (msg 26684)
section 4, items 1-6, one cell per item, with rulings 1 (the divergence tile's name) and 2 (whose Base case) folded into item 4's
cell; PLUS one issuer cell, `AV-v-7`: AMGT_RESAPP r48's ask (msg 26588 from `2.0.0_SA_COO~Z`: read the served `model.line_names` /
`formula_words`; let FWD-30's parity harness admit the export's case line in words), placed by v4 "for the first round after ww-1
lands" -- ww-1's NEVER-2 entry CLOSED 19:56:55Z (COO~Z msg 26689), so its dependency is met at this cut. **NOT cells:** "$1,234" in
INTU's drafted prose and every date inside served prose (C-PRESENTATION-ONLY); the two producer asks of ruling 5 (a served company
`name` on the rank-history series; officers from a second source) -- AMGT_RESAPP's round-49 list. **Walk condition:** the round's
one real run waits on ww-1's V1 leg -- CLOSED at 19:56:55Z, so the condition holds at the cut. **Portal base:** site-Z local DEV
`09bd04b1`. **Fixtures:** `deliverables/2.0.0_SA_COO~D/round5/fixtures/` = the round-4 set plus `thesisBundle.AMD_US_Equity.json`
(the `payload` of AMGT_RESAPP round48/captures/thesis_AMD_US_Equity_20260929T200344Z.json @8f50bcb837, extracted verbatim: the
served /thesis after ww-1, carrying `model.line_names` 25 entries and `formula_words`). **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-v-1` | 1 | Posture cites read as words: no passage id, preset code or status word in a cite line; a carried passage names its document + section from its served `source`, an uncarried one says so in words; every cite still rendered | FWD-10, FWD-11 | `SA/postureCites.ts`, `SA/tabs/PostureTab.tsx`, harnesses `posture`, `posturePattern` | ~18 | LOCAL |
| `AV-v-2` | 2 | The history view: 12 strokes at min CIE76 dE >= 25 (66 pairs), >= 24 px right of the last tick, and a walker step that presses one legend button ("-Chart-picked") | FWD-3 | `SA/components/RankedChart.tsx` (palette, margin), harness `chart`, `.claude/skills/ui-walk/walk.mjs`, `SKILL.md` | ~19 (1st) | LOCAL |
| `AV-v-3` | 3 | The generations line as one plain sentence (no status word, no generation id); the Lead Panel's `PanelFooter` (the second #0A1733 band, measured) gone, its caption moved into the body | FWD-11 | `SA/components/RankedChart.tsx` (`GenerationsLine`), `SA/components/LeadPanel.tsx`, harnesses `leadPanelPattern`, `errorEmpty`, `shell`, `tabs` | ~19 (2nd) | LOCAL |
| `AV-v-4` | 4 + rulings 1, 2 | The Model face says whose Base case each is (an unlabelled rule case reads "Opal's rule-based Base case"; a served label prints as served); the divergence tile reads "Divergence from consensus forecast" | FWD-6, FWD-11 | `SA/tabs/ModelTab.tsx`, harnesses `modelPattern`, `exportCompare` | ~20 (1st) | LOCAL |
| `AV-v-7` | issuer (RESAPP r48 ask) | The Model reads the served `line_names` / `formula_words` (local copies = fallback only); FWD-30's parity admits the export's case line in words | FWD-9, FWD-11 | `SA/tabs/ModelTab.tsx`, `SA/modelSheet.ts`, `SA/types.ts`, harnesses `exportCompare`, `modelPattern` | ~20 (2nd) | LOCAL |
| `AV-v-6` | 6 | The page's own dates in one form (the Thesis / Model panel headers' "Sep 29, 2026" -> ISO); the timeline legend's words on the band-scoped tokens (fills unchanged) | FWD-11 | `SA/tabs/ThesisTab.tsx`, `SA/tabs/ModelTab.tsx` (header date only), `SA/components/TimelinePanel.tsx`, harnesses `thesisLadder`, `timelineFourStates` | ~20 (3rd) | LOCAL |
| `AV-v-5` | 5 | Exec "Read detail" and the Bloomberg-fallback line without the served machine reason (it rides a data attribute) | FWD-7, FWD-11 | `SA/tabs/ExecManagementTab.tsx`, harnesses `execPattern`, `execText`, `execFallback` | ~21 | LOCAL |

**Edges and chains:** no data edge. Two write-set collisions resolved by queues (CUT BY WRITE SET): `RankedChart.tsx` (v-2, v-3) ->
slot ~19, v-2 then v-3; `ModelTab.tsx` (v-4, v-7, v-6) and `exportCompare.harness.cjs` / `modelPattern.harness.cjs` (v-4, v-7) ->
slot ~20, v-4 then v-7 then v-6 (item 6, the batch-ish cell, last on its colliding slot). M = 4 chains (v-1; v-2->v-3;
v-4->v-7->v-6; v-5), N = 4, cap 8. Every other surface is written by exactly one cell; `tabs.harness.cjs` is v-3's to re-anchor
(its PanelFooter stub reads the "Source:" text) and a read-only bound for v-4, v-5, v-6 and v-7; the surprise channel is shared
append-only.

**Checks (`round5/checks/`, dry-run at base 09bd04b1; `_load.cjs`, `bound.cjs` and `census.cjs` copied forward from round 4):**
posturecite.cjs 0 of 3; pick.cjs 1 of 3 (min dE 18.1 #f59e0b/#fb923c; 8 px); pickstep.cjs 1 of 3; gens.cjs 0 of 3; modelwords.cjs
1 of 3; servedwords.cjs 1 of 3; casewords.cjs 1 of 2; datecontrast.cjs 1 of 3; execdetail.cjs 2 of 3 -- every build check FAILS as
expected (each passing arm is a floor or control). Green arms fed (scratch overrides, never on a face): posturecite 3/3, pick 3/3
(scratch palette min dE 40.2), pickstep 3/3, gens 3/3, modelwords 3/3, servedwords 3/3, casewords 2/2, datecontrast 3/3, execdetail
3/3. Bounds at base PASS: V1 2/2, V2 3/3, V3 4/4, V4 2/2, V5 4/4, V6 4/4, V7 2/2; RESAPP vv-5.AC1 YES; walkvoid.sh YES (5174
serving, CTO~Z's walk build). `_load.cjs` also reads timelineFourStates' `"failures": []` verdict as green. `census.cjs` gains a
passage-id class and a preset-code class (both over the full visible text, drawers included) and two surfaces (`chart`, the
generations line; `posture-sap`): 34 tokens over 8 surfaces at base -- the CVO's instrument, graded by judgment.

**Battery:** comp-schedule, comp-iam DECLARED-NOT-APPLICABLE. comp-adversary: the checks above; blind spots -- static markup with the
estate chrome stubbed; recharts replaced by a prop-recording stub (colour and edge are graded by props; pixels are the walk's);
pickstep.cjs reads walk.mjs statically (the issuer's walk is its live run); gens.cjs's band arm counts the component tree, the
walk's design:bands check reads pixels; datecontrast.cjs grades the legend by token class. MEASURED at the cut: the served rule case
carries the label "Historical-multiple reference" on every fixture and on the current AMD capture, so v-4's ruling-2 head is the
unlabelled fallback (the round-4 walk's 19:15Z shape); 6 of the 7 SAP GY passage ids name passages the bundle does not carry, so
v-1 names document + section only where `source` is served.

**Rule 24:** (i) MECE over the analysis's six items plus the placed ask, by subtraction: 7 placed; the NOT-cells named with their
reason. (ii) One cell per intent; three shared files resolved by two queues. (iii) One intent per cell. (iv) No cell moves a served
value, a figure, a verdict, a cite, a pick or a count; v-2 changes colours and room, v-3 the words of a count it keeps, v-7 which
of two identical word sources the page reads.

## v6 -- ROUND 6 (issuer, 2026-09-29 ~22:xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the round-5 analysis's enrichment list, plus one issuer cell.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round5.md` @c918fa1fab (msg 26737) section 4, items 1-4, one cell per
  item. Section 2a's correction (CTO~Z msg 26748) is folded into cell 1: a PARTIAL day reads "Searched: ...", and the word
  "covered" is withdrawn.
- **Cell 4 widened:** it also carries AMGT_HARVST's FWD-5 and FWD-6 as named judgments on the same walk (CTO~Z msg 26751;
  AMGT_HARVST `ROUND_ANALYSIS.round19.md` ruling 5 @a251f02116).
- **Issuer cell `AV-u-5`:** AMGT_RESAPP r49's ask (msg 26753 from `2.0.0_SA_COO~Z`; rows Z-W173-S1..S4) -- one data attribute
  per fact FWD-30's grade reads, no visible change.
- **NOT cells:**
  - the team pack's unit (ruling 3);
  - the Historical-multiple owner label (an AMGT_RESAPP ask, ruling 4);
  - "$1,234" in drafted prose;
  - the rank-series `name` (AMGT_RESAPP xx-2, merged, not deployed; the page's label path already reads it);
  - officers from a second source (AMGT_RESAPP xx-3);
  - an event-span layer on the timeline (not in any round-6 item; the walk records its absence for AMGT_HARVST FWD-6).
- **A not-reached count is NOT served:** `/timeline` carries `publishers_covered` (the searched count) and its codes, with no
  pool denominator, so cell 1 states only what is served.
- **Portal base:** site-Z local DEV `4f927ad0`.
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round6/fixtures/` is the round-5 set plus these:
  - **SERVED, captured at the cut** by a read-only invoke of `opal-amgt-scoped-api` (CodeSha256 uv0oTSMa...Ng=, LastModified
    2026-09-29T21:57:59Z):
    - `timeline.992_HK_Equity.json`: 272 days, 1 PARTIAL, searched wsj, 0 articles, 3 events;
    - `timeline.ASML_NA_Equity.json`: 74 PARTIAL, searched sa;
    - `timelineDay.992_HK_Equity.2026-09-23.json` and `timelineDay.ASML_NA_Equity.2026-07-15.json`.
  - **ISSUER VARIANT, labelled in the file:** `rankSeries.TRENDING_PRICE.12.named.VARIANT.json`, which adds a `name` per series
    to exercise the label path only.
  - **Snapshot:** `attrs.visible.base.json`, the base visible text of the six surfaces `AV-u-5` touches.
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-u-1` | 1 + 2a | Timeline panel: a failed call's visible error in words (raw cause on a data attribute; the designed ERROR state already renders -- walk D shot 059); a PARTIAL day reads "Searched: <publishers in words> -- nothing found / N found" in the tooltip and the exported DayDissection (fixed display map, no "covered", no raw code, no field name, no not-reached count); legend words >= 4.5:1 on the body and tile rungs (fills unchanged) | FWD-5, FWD-11 | `SA/components/TimelinePanel.tsx`, harness `timelineFourStates` | ~22 | LOCAL |
| `AV-u-2` | 2 | Posture's last machine phrasing: comparability measures via a fixed named display map, the footer's two counts in words; no "the object", "comparable selection", "rung", "log cap", "cite(s)", "bundles this page reads", "on this name's peer set", "validated N of N" | FWD-10 | `SA/postureCites.ts`, `SA/tabs/PostureTab.tsx` (cites, footer), harnesses `posture`, `posturePattern` | ~23 (1st) | LOCAL |
| `AV-u-5` | issuer (RESAPP r49) | Seven data attributes carrying served values/reasons (figure value + year, served case value + currency, identity sector/country/currency, description-absence reason, driver-chart series, peers absent-column reason, posture no-call reason); no visible change | FWD-11, RESAPP FWD-30 | `SA/tabs/ModelTab.tsx`, `SA/components/SecurityOverlay.tsx`, `SA/components/HeaderBrief.tsx`, `SA/components/ThesisDriverChart.tsx`, `SA/tabs/PeersTab.tsx`, `SA/tabs/PostureTab.tsx` (verdict attribute) | ~23 (2nd, last) | LOCAL |
| `AV-u-3` | 3 | History view: an unpicked line's dots mute with it (the picked line and the no-pick view full); the served-name label path kept (proven on the labelled variant) | FWD-3 | `SA/components/RankedChart.tsx`, harness `chart` | ~24 | LOCAL |
| `AV-u-4` | 4 + HARVST r19 ruling 5 | The walker grades by name: `--thread "<company name>"` walks FWD-1's five hops, picking the row by `[data-row-lead]` name; the four List views written to `lead-lists.json`; per opened name a timeline day pressed and an event span opened, or `timeline:no-event-element` recorded | FWD-1, FWD-2, FWD-11; HARVST FWD-5, FWD-6 | `.claude/skills/ui-walk/walk.mjs`, `SKILL.md` | ~25 | LOCAL |

**Edges and chains:**
- No data edge.
- One write-set collision is resolved by a queue: `PostureTab.tsx` is written by `AV-u-2` (cites and footer) and `AV-u-5` (the
  verdict attribute), so slot ~23 runs u-2 then u-5. u-5 is last because its six files span surfaces no other round-6 cell
  writes except that one.
- M = 4 chains (u-1; u-2 -> u-5; u-3; u-4), N = 4, cap 8.
- Every other surface is written by exactly one cell. `tabs.harness.cjs` is a read-only bound for u-1 and u-5. The surprise
  channel is shared append-only.

**Checks (`round6/checks/`, dry-run at base 4f927ad0):** `_load.cjs`, `bound.cjs`, `census.cjs` and `walkvoid.sh` were copied
forward from round 5.

| check | base | green arm (scratch overrides, never on a face) |
|---|---|---|
| timeline.cjs | 0 of 3 | 3 of 3 |
| posturewords.cjs | 1 of 3 | 3 of 3 |
| dots.cjs | 2 of 3 | 3 of 3 |
| walkthread.cjs | 0 of 3 | 3 of 3 |
| attrs.cjs | 0 of 3 | 3 of 3, visible text unchanged |

- **Every build check FAILS at base, as expected.** Each arm that passes at base is a control.
- **Bounds at base PASS:** U1 2/2, U2 2/2, U3 3/3, U5 7/7; RESAPP vv-5.AC1 YES; walkvoid.sh YES (5174 serving).
- **`census.cjs`:** gains a machine-phrase class ("the object", "comparable selection", "rung", "log cap", "cite(s)", "bundles
  this page reads", "on this name's peer set", "validated N of N", "covered", `mention_score`). It reads 30 tokens over 8
  surfaces at base. It is the CVO's instrument, graded by judgment.
- **AMGT_RESAPP's own FWD-30 grade:** `round45/checks/sweep.py` @525e045932 reads AWS (lambda invoke), so it is not an offline
  criterion; the issuer runs it at the drain.

**Battery:** comp-schedule and comp-iam are DECLARED-NOT-APPLICABLE. comp-adversary is the checks above. Blind spots:
- The markup is static, with the estate chrome stubbed.
- react-query and recharts are stubs. The timeline tooltip is rendered through recharts' `content` prop, and pixels are the walk's.
- walkthread.cjs reads walk.mjs statically; the issuer's signed-in round-6 walk is its live run.
- The legend contrast is computed from `index.css`'s layer tokens, not pixels; the walk's `design:contrast` is the pixel read.

**Measured at the cut:**
- The INTU "skeleton" on walk D shot 054 was the in-flight LOADING state; the designed ERROR state rendered on shot 059. The
  issuer's round-5 drain-end read, item 1, mis-read it, and cell 1 is recast onto the error's words.
- Every served PARTIAL day opened serves 0 articles.
- No served fixture carries an ABSENT description or a no-call posture, so `AV-u-5` exercises both on labelled in-memory variants.

**Rule 24:**
- **(i) MECE:** over the analysis's four items plus the placed ask, by subtraction: 5 placed. The NOT-cells are named with their
  reason.
- **(ii) Write sets:** one cell per intent; the one shared file is resolved by a queue.
- **(iii) Intent:** one intent per cell.
- **(iv) What no cell moves:** a served value, a figure, a verdict, a cite, a count or a pick. u-1 changes the words around served
  counts and codes. u-3 changes dot opacity. u-5 adds attributes whose values are the served values.

## v7 -- ROUND 7 (issuer, 2026-09-30 ~00:xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the round-6 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round6.md` @378fd0c04b (msg 26790) section 4, items 1-4, one cell per item,
  with rulings 1 (no-call posture), 2 (footer form), 4 (DENIED = not searched), 5 (FWD-2 columns: measure, then build) and 6 (the
  PASS badge) folded into their cells as the analysis places them.
- **Cell ids:** `AV-s-1`..`AV-s-4`. The letter `t` is round 1's (`AV-t-1`..`AV-t-4`, still on disk), so round 7 takes `s`.
- **NOT cells:**
  - ruling 3 (the reference pages' band / contrast defects -- their owners);
  - ruling 7 and the producer asks to AMGT_RESAPP (posture reason in words, crosswalk-name fallback, places moved, the thesis
    driver's series);
  - "$1,234" in drafted prose (carried).
- **Portal base:** site-Z local DEV `fd4deb75`.
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round7/fixtures/` = the round-6 set plus these, SERVED, captured at the cut by
  read-only invokes of `opal-amgt-scoped-api` (each file's `_capture` / `_capture_note` names the route, CodeSha256 and time):
  - `thesisBundle.992_HK_Equity.json`, `overlay.992_HK_Equity.json` (posture SERVED, verdict absent, comparable null, the
    producer's machine reason -- cell 1's positive control);
  - `timelineDay.992_HK_Equity.2026-08-13.json` (DENIED, 2 articles); `timeline.VLO_US_Equity.json` (272 DENIED, 0 articles);
  - `rankings.{TRENDING,BREAKOUT}_{CHATTER,PRICE}.json` (the four lead lists, as served).
  - ISSUER VARIANTS are built in memory inside the checks, each labelled there (an ABSENT posture with a planted reason;
    date-only vintages; an all-quiet ASML; a served sector; a REFUSE sentence).
- **FWD-2 served-column census (measured at the cut, ruling 5):** asset class and sub-asset class 30 of 32 on each price list and
  2 of 2 on Trending x Chatter; sector 0 on every list; NO places-moved field on any row; Breakout x Chatter serves 0 rows. So
  cell 4 renders asset / sub-asset class, names sector and places moved as not served, and "places moved" is a RESAPP ask.
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-s-1` | 1 + ruling 1 | A no-call posture (status ABSENT, or SERVED verdict absent) reads "No call on this name yet" + one reason class from the served status (`data-posture-reason-class`: not-drafted / no-comparable / no-call-made) on the tab and both header-line copies; the served reason only on `data-posture-reason` | FWD-11 | `SA/tabs/PostureTab.tsx`, `SA/components/SecurityOverlay.tsx`, `SA/components/LeadPanel.tsx`, harnesses `posture` (re-anchor absent_arm_explicit), `exportCompare` (re-anchor the ABSENT-state key) | ~26 | LOCAL |
| `AV-s-2` | 2 + ruling 2 | Both window footers (header cards, Thesis) stamp through the estate's `formatPanelTimestamp`: a time prints whole, a bare date prints the long date with no invented clock and says it is a date; each source begins "Source: "; `headerCardStamp` / `thesisWindowStamp` exported | FWD-11 | `SA/components/HeaderCards.tsx`, `SA/components/ThesisCards.tsx`, harness `drafting` (one loader line) | ~27 (1st) | LOCAL |
| `AV-s-3` | 3 + ruling 4 | DENIED reads "Not searched on this day" (dissection, tooltip, legend); the all-quiet caption says an unsearched range was not searched, with served counts, never "honest zero"; each served event marked `[data-timeline-event]` with its headline; the walker's `--day "<sec>=<date>"` opens a day by date and writes `timeline-days.json` | HARVST FWD-5, FWD-6 | `SA/components/TimelinePanel.tsx`, `.claude/skills/ui-walk/walk.mjs`, `SKILL.md` | ~28 | LOCAL |
| `AV-s-4` | 4 + rulings 5, 6 | The lead lists show the served asset / sub-asset class (and sector where served) as aligned columns under a header row, the unserved columns named once, nothing computed; the PASS badge leaves the face (`data-verbatim-check`), a refusal keeps its badge | FWD-2, FWD-11 | `SA/components/RankedList.tsx`, `SA/components/ThesisCards.tsx`, harnesses `drafting` (re-anchor verbatim_badge), `thesisLadder` (re-anchor pass_faces_kept) | ~27 (2nd) | LOCAL |

**Edges and chains:**
- There is no data edge.
- Write sets: `ThesisCards.tsx` and `drafting.harness.cjs` are written by `AV-s-2` and `AV-s-4`, so slot ~27 runs s-2 then s-4.
  Every other surface is written by exactly one cell.
- M = 3 chains (s-1; s-2 -> s-4; s-3), N = 3, cap 8.
- The surprise channel is shared append-only.

**Checks (`round7/checks/`, dry-run at base fd4deb75; `_load.cjs`, `bound.cjs`, `census.cjs`, `walkvoid.sh` copied forward):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| absent.cjs | 1 of 3 (the 992 HK header prints the producer's reason verbatim; the VLO control passes) | 3 of 3 |
| footer.cjs | 0 of 3 (builders unexported; base stamps ISO / "Pack read") | 3 of 3 |
| timeline7.cjs | 0 of 3 | 3 of 3 |
| walkday.cjs | 0 of 3 | 3 of 3 |
| columns.cjs | 0 of 3 | 3 of 3 |

- **Bounds PASS at base AND on the green arm:** U1 8 of 8, U2 5 of 5, U3 3 of 3, U4 5 of 5. RESAPP vv-5.AC1 YES at base; on the
  green arm the four parity sets are exact. walkvoid.sh YES.
- **census.cjs** now covers EVERY walked name (header-/posture- for VLO, INTU, SAP GY, 992 HK) plus a planted-reason arm. It reads
  40 tokens at base (header-HK alone 7: the file name, AMGT-s-1, F2/G-24 ...; planted 12, 4 of them [planted]) and 20 on the green
  arm (planted 1).

**Cut rules applied (round 6's two cut defects):**
- **(a) No base comparisons.** No check compares against a base snapshot, count or diff; each check grades the worker's own tree,
  so slot ~27's second order has no pre-queue base to drift from.
- **(b) Bounds run against a green build.** Every bound was run against a GREEN BUILD of all four cells: a scratch detached portal
  worktree at fd4deb75 with the cells built. That run found every harness a required change NECESSARILY breaks:
  - `posture` and `exportCompare` for s-1;
  - `drafting` for s-2 (its loader cannot resolve a new import);
  - `drafting` and `thesisLadder` for s-4.
  Each is granted in its cell's `<paths>`, with the exact re-anchor named on the face and proven green on the green arm.
- **Two build constraints the green run found, stated on the faces:**
  - `errorEmpty`'s loader cannot resolve a NEW sibling module, so s-1 restates its helper per file.
  - The loaders cannot resolve an unknown `@/` module, so s-2 imports `dateUtils` relatively.

**Battery:**
- comp-schedule and comp-iam: DECLARED-NOT-APPLICABLE.
- comp-adversary: the checks above.
- Blind spots:
  - static markup with the estate chrome stubbed;
  - the header window is lazy-loaded, so footer.cjs reads the exported builders;
  - react-query and recharts are stubbed in timeline7.cjs, so pixels are the walk's;
  - walkday.cjs reads walk.mjs statically; the issuer's walk (`--thread "Valero"`, `--day "992 HK=2026-08-13"`, the four names,
    /market /positioning /philosophy) is its live run.

**Rule 24:**
- (i) MECE over the analysis's four items by subtraction: 4 placed; the NOT-cells named with their reasons.
- (ii) One cell per write set; two shared files resolved by one queue.
- (iii) One intent per cell.
- (iv) No cell moves a served value, a figure, a verdict, a cite, a count or an article order. s-1 and s-4 move visible words
  onto attributes; s-2 moves only the stamp's format; s-3 moves a status word to its meaning and draws served events it never
  drew.

## v8 -- ROUND 8 (issuer, 2026-09-30 ~02:xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the round-7 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round7.md` @0c498ee766 section 4, items 1-3, one cell per item, with
  rulings 1 (the walker waits for state), 3 (FWD-6's last clause graded on the same re-walk), 4 (the lead source line, date only)
  and 5 (labels per Positioning; the finer field by its grain) folded into their cells as the analysis places them.
- **Cell ids:** `AV-q-1`..`AV-q-3`. Letters e, r, s, t, u, v, w are on disk, so round 8 takes `q`.
- **NOT cells:**
  - ruling 2 (the `/timeline/day` ~5.5 s latency) -- AMGT_HARVST's round-24 input, routed by the CTO; this project grades the page
    on whatever the route returns;
  - the AMGT_RESAPP standing asks (names for the other 15 rows, places moved, the thesis driver's series).
- **Portal base:** site-Z local DEV `ab7e1e49` (clean). **Walker base:** `.claude/skills/ui-walk/walk.mjs` @4a0628755b.
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round8/fixtures/` = the round-7 set, carried unchanged (25 files; each keeps its
  `_capture` note). No new capture: no cell reads a payload round 7 did not. ISSUER VARIANTS are built in memory inside the checks,
  each labelled there (a dateless list; a served finer field; a held day route on a stub page).
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-q-1` | 1 + rulings 1, 3 | `waitForDayState(page, date)` polls the panel's served state attributes (rows / empty / failed) under `[data-timeline-selected-day]`, ceiling `DAY_STATE_CEILING_MS` >= 15 s, a held route records "ceiling"; the --day step, the newest-day press and the event open each wait before the shot (no `settle(page, 1500)`); every opened day recorded with `via`, `state`, `waited_ms`; `timeline-days.json` written whenever non-empty | HARVST FWD-5, FWD-6 | `.claude/skills/ui-walk/walk.mjs`, `SKILL.md` | ~29 | LOCAL |
| `AV-q-2` | 2 + ruling 4 | The lead source line reads "Dated <long date> \| Source: ..." through `formatPanelTimestamp` with its clock stripped (date only, never an invented time); the requested day, when it differs, as "; requested for <long date>"; no ISO | FWD-11 | `SA/components/LeadPanel.tsx`, harnesses `errorEmpty` (one loader line), `leadPanelPattern` (re-anchor source_footer, caption_facts_unchanged) | ~30 | LOCAL |
| `AV-q-3` | 3 + ruling 5 | The lead-list columns take Positioning's labels per key ("Asset Class", "Sub Asset", read from `HoldingsBreakdownTable.tsx`); `sector` is named by its grain ("Industry group (finer than Sub Asset)"), never "Sector"; the unserved note uses the same labels; keys unchanged | FWD-2 | `SA/components/RankedList.tsx` | ~31 | LOCAL |

**Edges and chains:**
- There is no data edge.
- Write sets are disjoint: q-1 writes the walker only; q-2 writes `LeadPanel.tsx` and two harnesses; q-3 writes `RankedList.tsx`
  only (measured on the green arm: no bound harness reads its labels, so it needs no harness grant and shares no file with q-2).
- M = 3 chains (q-1; q-2; q-3), N = 3, K = 0 queued, cap 8.
- The surprise channel is shared append-only.

**Checks (`round8/checks/`, dry-run at base ab7e1e49 / walk.mjs @4a0628755b; `_load.cjs`, `bound.cjs`, `census.cjs`,
`walkvoid.sh` copied forward):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| daystate.cjs | 0 of 3 (no wait; every day and event shot follows settle 1500; timeline-days.json only under --day) | 3 of 3 (ceiling 20000; held route -> "ceiling") |
| sourceline.cjs | 0 of 3 (ISO inside the source; census 14 of 18) | 3 of 3 (census 18 of 18) |
| labels.cjs | 0 of 3 ("Asset class" / "Sub-asset class" / "Sector" against "Asset Class" / "Sub Asset") | 3 of 3 |

- **Bounds PASS at base AND on the green arm:** walkerbound 3 of 3 (round5 pickstep, round6 walkthread, round7 walkday); Q2 5 of 5;
  Q3 5 of 5; round-7 columns.cjs 3 of 3. walkvoid.sh YES at base (5174 serving); not run on the green arm (the green change touches no
  sign-in or void path -- named blind spot). Portal `tsc -b --noEmit` rc=0 on the green arm (q-2 + q-3).
- **Census:** sourceline.cjs prints every footer on the page (4 lead lines, 12 header card windows over VLO / SAP GY / 992 HK, 2 Thesis
  windows); labels.cjs prints each key's page label beside Positioning's.

**Cut rules applied:**
- **(a) Queue-aware bases.** No check compares against a base snapshot, count or diff; there is no queue this round.
- **(b) Bounds run against a green build.** A scratch detached portal worktree at ab7e1e49 (`C:/tmp/cood-r8-root/portal`) with q-2
  and q-3 built, and a scratch walk.mjs fed by the issuer-only `CHECK_SRC_OVERRIDE`. That run found every harness a required change
  NECESSARILY breaks: `errorEmpty` (its loader cannot resolve the new relative `dateUtils` import) and `leadPanelPattern`
  (`source_footer`, `caption_facts_unchanged` anchored on the ISO line) for q-2. Each is granted in q-2's `<paths>` with the exact
  re-anchor named on the face and proven green (Q2 5 of 5). q-1 and q-3 break none.

**Battery:**
- comp-schedule and comp-iam: DECLARED-NOT-APPLICABLE.
- comp-adversary: the checks above.
- Blind spots:
  - daystate.cjs runs the extracted wait on a stub page and fake clock; the live latency is the issuer's walk;
  - static markup with the estate chrome stubbed (sourceline, labels); column widths and wrap are the walk's;
  - walkvoid.sh not re-run on the green arm.
- The issuer's close walk: signed-out control first; then `--day "992 HK=2026-08-13"` plus one event open (HARVST FWD-5 / FWD-6),
  the lead panel beside a header card window and a Market / Positioning window (FWD-11), a lead list beside the Positioning
  breakdown (FWD-2).

**Rule 24:**
- (i) MECE over the analysis's three items by subtraction: 3 placed; the NOT-cells named with their reasons.
- (ii) One cell per write set; no shared file.
- (iii) One intent per cell.
- (iv) No cell moves a served value, a figure, a verdict, a count or an article order. q-1 moves only when the walker shoots and
  what it records; q-2 moves only the line's date format; q-3 moves only the words that name three columns.

## v9 -- ROUND 9 (issuer, 2026-09-30 ~03:xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the round-8 analysis's enrichment list, plus one Andrew-direct item.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round8.md` @2c63f69a09 section 4, items 1-3, with rulings 1 (the heading follows
  the grain, "Sector"; display case; no truncation), 2 (the day's rows show their strength) and 3 (the FWD-11 residuals).
- **Andrew-direct**, to 2.0.0_SA_COO~D on 2026-09-30 ~03:1xZ, verbatim: *"By the way, for your referece, the Security Analysis
  icon in the portal sidebar is in the wrong location. It is a tool, so it shoudl actually sit beneath the Security Scanner icon
  in the tools section."* It becomes cell `AV-p-4`, on the DIRECT-ACT path (one line moved, LOCAL). The scope is verbatim: the
  entry moves, and nothing else about the sidebar changes.
- **Cell ids:** `AV-p-1`..`AV-p-4`. Letters e, q, r, s, t, u, v, w are on disk, so round 9 takes `p`.
- **The issuer's mapping differs from the analysis's in one place.** Ruling 3's first residual, the article time's raw ISO and
  "(instant)", is placed in `AV-p-2`, not in the residuals cell. The time and the strength words sit in the one article-row
  component (`TimelinePanel.tsx` `ArticleRow`), so one cell owns that row, and the write sets stay disjoint (fan-out 4, no chain).
  The residuals cell `AV-p-3` keeps "Dated" and the system-voice line (`LeadPanel.tsx`).
- **NOT cells:**
  - the Positioning model window's missing source (ruling 3: the reference page's gap);
  - names on 22 of 22 rows and the driver series (AMGT_RESAPP r51 cells 5-6);
  - the `/timeline/day` latency (AMGT_HARVST).
- **Seen at the cut, NOT cut (round-10 inputs):**
  - the Thesis window source for VLO reads "machine draft from VLO US's 10-K, filed 2026-02-25", an ISO date inside a source;
  - `HeaderCards.tsx` `footerTime` and `ThesisCards.tsx` `thesisWindowStamp` still print "Dated <long date>" for a bare-date
    vintage. No served fixture reaches that path, and the census reads 18 of 18 in the one form on the served payloads.
- **Portal base:** site-Z local DEV `29c8226a` (clean). **Walker base:** `.claude/skills/ui-walk/walk.mjs` @ac0fdbfc16 (unchanged
  this round).
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round9/fixtures/` = the round-8 set, carried unchanged (25 files; each keeps its
  `_capture` note). No new capture: `mention_count` and `published_precision` are already in the served
  `timelineDay.992_HK_Equity.2026-08-13.json`. ISSUER VARIANTS are built in memory inside the checks, each labelled there.
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-p-1` | 1 + ruling 1 | `sub_asset_class` headed "Sector"; `sector` "Industry group (finer than Sector)" in its header and the unserved note; the asset-class value in display case ("Equity"), its data attribute unchanged; no truncating class on a classification value | FWD-2 | `SA/components/RankedList.tsx` | ~32 | LOCAL |
| `AV-p-2` | 2 + ruling 2, ruling 3's first residual | each article row shows "named N times" from `mention_count` ("named once", "not counted"), and its time through `formatPanelTimestamp` ("instant") or as the long date (any other precision), with no ISO and no precision word; the served order untouched | HARVST FWD-5, FWD-11 | `SA/components/TimelinePanel.tsx`, harness `timelineFourStates` (one loader line) | ~33 | LOCAL |
| `AV-p-3` | 3 + ruling 3 | the lead source line drops "Dated" ("<long date> \| Source: ..."); the older-list line reads "This list is from <long date>, the newest available." | FWD-11 | `SA/components/LeadPanel.tsx`, harness `leadPanelPattern` (re-anchor source_footer, stale_dated_said) | ~34 | LOCAL |
| `AV-p-4` | Andrew-direct | the `/security-analysis` sidebar entry moves from Analysis to Tools, directly beneath Security Scanner; its label, icon, gate and comment are kept | Andrew's word (no FWD) | `portal/src/App.tsx` | ~35 | LOCAL, DIRECT-ACT |

**Edges and chains:**
- There is no data edge.
- Write sets are disjoint: p-1 `RankedList.tsx`; p-2 `TimelinePanel.tsx` + `timelineFourStates`; p-3 `LeadPanel.tsx` +
  `leadPanelPattern`; p-4 `App.tsx`.
- M = 4 chains, N = 4, K = 0 queued, cap 8.
- The surprise channel is shared append-only.

**Checks (`round9/checks/`, dry-run at base 29c8226a; `_load.cjs`, `bound.cjs`, `census.cjs`, `walkvoid.sh` copied forward):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| grain.cjs | 0 of 3 ("Sub Asset" over sector names; "Industry group (finer than Sub Asset)"; "equity" and `truncate`) | 3 of 3 |
| strength.cjs | 1 of 3 (no "named N times"; raw ISO + "(instant)"; the order arm passes at base by design) | 3 of 3 |
| oneform.cjs | 0 of 3 ("Dated" leads 4 lead lines; the system-voice line; census 14 of 18) | 3 of 3 (census 18 of 18) |
| sidebar.cjs | 1 of 3 (the entry in Analysis; the gate arm passes at base by design) | 3 of 3 |

- **Bounds:** all 18 SecurityAnalysis harnesses were run at base and on the green arm.
  - 16 are green at base. `assembled` and `exportCompare` are RED at base (rc=2) and stay out of the bound.
  - On the green arm without re-anchors, exactly two turn red:
    - `timelineFourStates`: its loader cannot resolve p-2's new `../../../lib/dateUtils` import;
    - `leadPanelPattern`: `source_footer` and `stale_dated_said` are anchored on "Dated" and on the old line.
  - With the named re-anchors, 16 of 16 are green.
  - `admin-gate.test.ts` (bun; reads `App.tsx`) is 10 of 10 at base. On the green scratch root it is 9 of 10, and its F49-AC8
    App.tsx gate-hunk test passes. The one fail is F49-AC10's `git rev-parse` at the outer root, which the scratch root does not
    have (named, environmental); p-4's worker runs it in a real worktree.
  - Portal `tsc -b --noEmit` rc=0 on the green arm (all four cells). A planted type error in `RankedList.tsx` is caught (rc=2).
- **Earlier checks this round supersedes by ruling (not bounds):**
  - round-8 `labels.cjs` ("Sub Asset" is replaced by "Sector", ruling 1);
  - round-8 `sourceline.cjs` arm 1 (it expects "Dated");
  - round-7 `columns.cjs` arm 1, value for value on asset_class. The display case is ruling 1; grain.cjs arm 3 checks the served
    attribute unchanged and the shown value by the case rule.
  - Round-7 `timeline7.cjs` and `footer.cjs` read 3 of 3 on the green arm.

**Cut rules applied:**
- **(a) Queue-aware bases.** No check compares against a base snapshot, count or diff; there is no queue.
- **(b) Bounds run against a green build.** A scratch detached portal worktree at 29c8226a (`C:/tmp/cood-r9-root/portal`)
  with all four cells built found every harness a required change NECESSARILY breaks. Each is granted in that cell's `<paths>`
  with the exact re-anchor named on the face and proven green.

**Battery:**
- comp-schedule and comp-iam: DECLARED-NOT-APPLICABLE.
- comp-adversary: the checks above.
- Blind spots:
  - static markup with the estate chrome stubbed, so column widths, wrap and the sidebar's drawn position are the walk's;
  - `precision` values other than "instant" are reached only by the labelled variant (the served day carries "instant" only).
- The issuer's close walk:
  - signed-out control first;
  - then a lead list beside the Positioning breakdown (FWD-2) and `--day "992 HK=2026-08-13"` plus one event (the strength and
    time on each row);
  - the lead panel footer beside a header card window (FWD-11);
  - the sidebar in any shot (p-4).

**Rule 24:**
- (i) MECE over the analysis's three items plus Andrew's one item by subtraction: 4 placed; the NOT-cells named with their reasons.
- (ii) One cell per write set; no shared file.
- (iii) One intent per cell.
- (iv) No cell moves a served value, a figure, a verdict, a count or an order:
  - p-1 moves the words that head two columns and the case of one shown value;
  - p-2 adds a served count's words and changes a time's format;
  - p-3 changes two lines' words;
  - p-4 moves one sidebar entry.

## v10 -- ROUND 10 (issuer, 2026-09-30 ~05:xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the round-9 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round9.md` @d229d699f3 section 4, items 1-4, one cell per item, with rulings 1
  (the house date form, covering the whole page), 2 (CORPUS's six outcomes: `dossier_fields`; the team's cases, with Opal's rule
  cases labelled) and 3 (no K/M/B/T on an UNRESOLVED unit).
- **Cell ids:** `AV-o-1`..`AV-o-4`. Letters e, p, q, r, s, t, u, v, w are on disk, so round 10 takes `o`.
- **NOT cells:**
  - the names on 22 of 22 rows and the driver series (AMGT_RESAPP r51 cells 5-6);
  - the `/timeline/day` latency (RESAPP r51 `zz-8` as HARVST `n-6`);
  - 6501's empty dossier block's per-field reasons (CORPUS ruling 2: AMGT_RESAPP's producer ask). The page shows the one served
    reason.
- **The issuer's placements:**
  - (a) The header "posture line" (ruling 2) reads the `/overlay`, which does not carry `dossier_fields`. o-2 reads it through the
    page's existing `useThesisBundle` hook, the same `/thesis` query the tabs already make; this is no new route.
  - (b) Cells 2 and 3 have disjoint write sets, so they get separate workers (the analysis left the call to the COO).
  - (c) o-1 writes every page file o-2, o-3 and o-4 write, so it is a QUEUED chain. It starts on the post-drain DEV (cut rule
    (a)).
- **Portal base:** site-Z local DEV `b6634ba0` (clean). **Walker:** unchanged.
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round10/fixtures/` = the round-9 set, carried unchanged (25 files), plus 12 SERVED
  captures made at the cut by `round10/capture_r10.py`.
  - The captures are read-only `lambda:Invoke`s of `opal-amgt-scoped-api`, CodeSha256 `pVa+sgzj8XNZ9uvJqCOwRNCJn0IZhUklnWZh6JbO7B0=`,
    LastModified 2026-09-30T01:46:54Z. Each file carries a `_capture_note`.
  - `/thesis` for IMB LN, AZN LN, 6501 JP and TSM US; `/overlay` for IMB, AZN, 6501, 9433, 8316, 8035, 8766 JP and TSM US.
  - Four more `/thesis` captures (9433, 8316, 8035, 8766) were read and not kept, since no check reads them.
  - ISSUER VARIANTS are built in memory inside the checks, each labelled there.
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-o-2` | 2 + ruling 2 | `dossier_fields` rendered: the pillars (in order, with terms and the report's file name) on the Thesis tab, or the empty block's reason; the management passage on Exec Management; fund of record + last stated position on the Posture tab and the header posture line; no storage path on the face; types in `types.ts` TYPES ONLY, components INLINE | CORPUS FWD-10, 11, 15, 16, 18 | `SA/types.ts`, `SA/tabs/ThesisTab.tsx`, `SA/tabs/ExecManagementTab.tsx`, `SA/tabs/PostureTab.tsx`, `SA/components/SecurityOverlay.tsx` | ~36 | LOCAL |
| `AV-o-3` | 3 + ruling 2 | the team's Base, Upside and Downside each rendered as written, or one plain sentence; every rule-case line headed "Opal's ..." (the served label, prefixed where it lacks it, or "Opal's rule-based <case>"); no bare "<Name> case:" and no "not in the pack yet" | CORPUS FWD-12 | `SA/tabs/ModelTab.tsx` | ~37 | LOCAL |
| `AV-o-4` | 4 + ruling 3 | `formatStatValue(value, format, currency, unit)`: an UNRESOLVED unit shows unscaled, grouped, "(unit not resolved)"; a measured unit unchanged; `HeaderCards` passes the unit and exports `headerCardFigureDisplay` | RESAPP FWD-30 | `SA/components/StatTile.tsx`, `SA/components/HeaderCards.tsx` | ~38 | LOCAL |
| `AV-o-1` | 1 + ruling 1 | ONE helper `dateWords.ts` (`longDate`, `longStamp`, over `formatPanelTimestamp`); every date a person reads in the long form, the ISO on a `data-` attribute; the bare-date "Dated" paths drop "Dated" | FWD-11 | `SA/dateWords.ts` (new), `postureCites.ts`, 12 components, 5 tabs, 6 harnesses (loader lines; one re-anchor) | ~39 QUEUED | LOCAL |

**Edges and chains:**
- There is no data edge.
- Write sets:
  - o-2, o-3 and o-4 are pairwise disjoint.
  - o-1 overlaps all three (`types.ts` excepted), so it runs on its own chain after o-2, o-3 and o-4 drain.
- M = 4 chains, N = 3 now, K = 1 queued (o-1), cap 8.
- The surprise channel is shared append-only.

**Checks (`round10/checks/`, dry-run at base b6634ba0; `_load.cjs`, `bound.cjs`, `census.cjs`, `walkvoid.sh` copied forward;
`surfaces.cjs` renders every walked surface: lead lists + footers, the lead chart, 8 headers, the timeline + 992 HK's day, and 4 tabs
x 8 names = 45 surfaces):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| dates.cjs | 1 of 3 (224 visible ISO dates on 44 of 45 surfaces; the long-form arm fails; the data- control passes at base by design) | 3 of 3 (0 over 45; 162 data- attributes keep the ISO) |
| dossier.cjs | 0 of 4 (no consumer of `dossier_fields`) | 4 of 4 (13 pillars in order with their reports) |
| cases.cjs | 0 of 3 (AZN's team Upside / Downside unrendered; "Upside case: not in the pack yet") | 3 of 3 (60 team table cells; 9 rule lines "Opal's ...") |
| units.cjs | 0 of 3 (the unresolved EV scaled; no display helper) | 3 of 3 (6 unresolved figures unscaled; 50 measured unchanged) |

- **Green arms:**
  - Scratch `C:/tmp/cood-r10a-root/portal` branch `r10-green-a` carries o-2, o-3 and o-4 (issuer).
  - Scratch `C:/tmp/cood-r10b-root/portal` branch `r10-green-b` carries o-1, built by an issuer-spawned helper agent to this check.
  - `r10-green-b` was merged over `r10-green-a` (3 import-line conflicts resolved) = the drain state.
  - On it: dates 3/3, dossier 4/4, cases 3/3, units 3/3; round-9 grain / strength / oneform / sidebar 3/3 each; ALL 16 of 16
    harnesses; portal `tsc -b` rc=0.
- **Bounds, base and green:**
  - Q2 (o-2) 8 of 8, Q3 (o-3) 3 of 3, Q4 (o-4) 3 of 3, Q1 (o-1) 16 of 16, each green at base and on the green arm.
  - o-2's first green arm put its blocks in a new shared module and exported value helpers from `types.ts`. That turned drafting,
    execFallback, execText and execPattern RED: their loaders resolve only the modules they name, and `../types` for type positions
    only.
  - Rebuilt INLINE with types-only `types.ts`, 16 of 16 were green with no harness grant; the face says so.
  - o-1 NECESSARILY breaks six harnesses: five cannot resolve `../dateWords` or its `../../lib/dateUtils` import, and tabs'
    `peers_csc_table_absent_marked` is anchored on the ISO universe vintage. Each is granted with its exact lines.

**Cut rules applied:**
- **(a) Queue-aware bases.** No check compares against a base snapshot. o-1 is queued: its slot is provisioned on the post-drain
  DEV, and its face says so (BOUNDS 4).
- **(b) Bounds run against a green build.** Every harness a required change NECESSARILY breaks is granted with its exact change
  on that cell's face (o-1 only), and was proven green on the combined drain state.

**Battery:**
- comp-schedule and comp-iam: DECLARED-NOT-APPLICABLE (no AWS in the cells; the cut's captures were read-only invokes by the
  issuer).
- comp-adversary: the checks above.
- Blind spots:
  - static markup with the estate chrome stubbed, so layout, chart ticks and tooltips and the lazily opened card windows are the
    walk's (o-4's window rows are graded through `headerCardFigureDisplay`);
  - a `precision` / date shape the fixtures do not carry is reached only by labelled variants.
- The issuer's close walk:
  - signed-out control first;
  - then the usual four names plus IMB LN, AZN LN and one planted JP name (6501);
  - IMB's Thesis / Exec Management / Posture tabs and header (o-2), AZN's Model tab (o-3), 6501's and IMB's header cards (o-4), and
    every date on the walked surfaces (o-1).

**Rule 24:**
- (i) MECE over the analysis's four items by subtraction: 4 placed; the NOT-cells named with their reasons.
- (ii) One cell per write set; o-1 queued behind the three it overlaps.
- (iii) One intent per cell.
- (iv) No cell moves a served value, a figure, a verdict, a count or an order:
  - o-1 moves only how a date reads;
  - o-2 adds served text;
  - o-3 adds served tables and changes the rule lines' heads;
  - o-4 stops a scale the unit never claimed and leaves every measured figure byte-identical.

### v10 AMENDMENT 1 (issuer, 2026-09-30 ~06:2xZ) -- `AV-o-3` re-opened for a byte repair, after walk I

- **Why:** walk I (`tmp/ui-walk/20260930T055658Z`, shot 192) showed AZN's Model tab reading "Opal's opal's historical-multiple
  reference". A byte scan of `portal/src/pages/SecurityAnalysis/` found three literal BACKSPACE bytes (0x08) where regexes meant
  `\b`: `tabs/ModelTab.tsx:295` (o-3, cb14d218) and `components/HeaderBrief.tsx:48-49` (since 2515f456, round 1; no description
  source has ever read "Company description from Bloomberg"). tsc and all 16 harnesses pass them. Row `DSGN_AMGTV1-Z-S5`.
- **Cell:** `AV-o-3` re-opened -- its own `ModelTab.tsx` byte, with `HeaderBrief.tsx` granted (same class). It replaces the three
  bytes with `\b` and nothing else, on DEV 5810586a; new criterion AC4 = bytes.cjs. A new order file (`AV-o-5`) was refused by
  to-pipeline-gate LIMB 6 (one issuance per round; a re-cut modifies its orders), so the repair rides the order that introduced one
  of the bytes. Worker slot ~37 (a fresh worker at the same serial), on its existing worktree brought to DEV.
- **Check:** `round10/checks/bytes.cjs` -- 0 control bytes in the page's source; AZN's rule label read once (plus an unprefixed
  variant); `descriptionSourceWords` reads Bloomberg / drafted / plain. Base 0 of 3; green 3 of 3; ALL 16 of 16 and Q5 4 of 4 at
  base and on green; tsc rc=0.
- **A check blind spot, named:** cases.cjs arm 2 asks only that a rule line START with "Opal's", which "Opal's opal's ..." does.
  bytes.cjs arm 2 closes it.
- **Walk:** 6501 JP never opened on walk I (only `/security/6501%20JP/peers` was requested; every 6501 shot is a loading
  skeleton), so o-4's planted face is re-walked on TSM US (a planted name) at the re-walk.
- **Gate limb that graded this amendment:** none graded the modification of `AV-o-3` (LIMB 6 fires on newly-added orders only;
  GATE (viii) reads its `<placeholders>NONE`). The surprise row is graded by `.tools/surprise-row-gate.py`.

## v11 -- ROUND 11 (issuer, 2026-09-30 ~07:xZ), over PRD v0.3 @abfad1355c (ADMITTED)

**Rectangle:** the round-10 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round10.md` @afad83a02f section 4, items 1-6, one cell per item, with rulings 1
  (the qualifier leads an unresolved figure), 3 (the evidence names which evidence), 4 (a DENIED day with articles) and s.2 (o-2's
  unexercised no-dossier arm; RESAPP round-51's routed page asks).
- **Cell ids:** `AV-n-1`..`AV-n-6`. Letters e, o, p, q, r, s, t, u, v, w are on disk, so round 11 takes `n`.
- **NOT cells:**
  - ruling 2 (quoted document titles are names, not page dates: nothing to build);
  - the names on 22 of 22 rows and the driver series (AMGT_RESAPP r51);
  - RESAPP FWD-12's re-run half, which has no served per-input re-run route (the page says so; a round-12 input for AMGT_RESAPP);
  - 6501's per-field dossier reasons (AMGT_RESAPP round-52 cell 2).
- **The issuer's placements:**
  - (a) Cell 4 is a WALKER cell. An issuer-spawned read-only research agent measured why 6501 JP never opened on walk I: the walker
    typed and submitted it correctly, and the page issued `/overlay`, but walk.mjs waits a FIXED settle (3000 ms after the pick,
    2500 ms per tab) and moved on while that first read was pending ("Loading identity header" on all seven 6501 steps). n-4 makes
    the walker wait for the page's panel state (`data-panel-state`) and record it, so the no-dossier arm is walked.
  - (b) Cells 5 and 6 share their write set (ModelTab, types, constants, the hooks, the endpoint file), so they are one chain on
    slot ~44: n-5 then n-6.
- **Portal base:** site-Z local DEV `2bb60cc3` (clean). **Walker base:** walk.mjs at CLOUD HEAD.
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round11/fixtures/` = the round-10 set, carried unchanged (37 files), plus 14 SERVED
  read-only captures at the cut (`round11/capture_r11.py`, committed, plus two one-off capture scripts in the issuer's scratchpad,
  not committed: each fixture's `_capture_note` names the route, query, CodeSha256 and time). The captures are `opal-amgt-scoped-api`,
  CodeSha256 `zHpr7FhS+irmKofIuKNqTkQm2hj7x2fvS1rrX1ohkfQ=`, LastModified 2026-09-30T05:20:04Z:
  - `/ledger`, `/versions` and `/compare` for BA, VLO, IMB and AZN;
  - `/compare?from=<oldest>&to=<newest>` for BA (212 added / 0 removed / 7 changed / 172 unchanged; every default compare of the
    two newest stamps is 0 changed);
  - `/thesis` for BA.
  ISSUER VARIANTS are built in memory inside the checks, each labelled there.
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-n-1` | 1 + ruling 1 | an UNRESOLVED unit reads "unit not resolved -- raw figure <digits> (<CUR>)": the qualifier first, the digits labelled raw; measured units unchanged | RESAPP FWD-30, FWD-11 | `SA/components/StatTile.tsx` | ~40 | LOCAL |
| `AV-n-2` | 2 + ruling 3 | the Posture tab's evidence section and footer name the FILING evidence (never "pack"); no "on this object", no raw key; an absent side says no filing evidence is carried | FWD-11 | `SA/tabs/PostureTab.tsx`, `SA/postureCites.ts` | ~41 | LOCAL |
| `AV-n-3` | 3 + ruling 4 | a DENIED day with N served articles reads "not searched for this company directly -- N articles found in other searches" (heading and tooltip); a 0-article day unchanged | HARVST FWD-5, FWD-11 | `SA/components/TimelinePanel.tsx` | ~42 | LOCAL |
| `AV-n-4` | 4 (s.2) | walk.mjs `waitForLoaded(page)` on `data-panel-state` (ceiling >= 30 s) after the pick and each tab, replacing the fixed settles; `load-states.json` | CORPUS FWD-10/11/15/16/18 (the no-dossier arm) | `.claude/skills/ui-walk/walk.mjs` | ~43 | LOCAL |
| `AV-n-5` | 5 (RESAPP r51) | `useModelVersions` / `useModelCompare` + client calls; the Model tab's versions (newest first, dated) and compare (oldest -> newest by default, served counts, the earlier version named, each change's line name and from/to); no raw mnemonic on the tab | RESAPP FWD-6 | the endpoint file, `SA/constants.ts`, `SA/types.ts`, `SA/hooks/useLeadPanelApi.ts`, `SA/tabs/ModelTab.tsx`, 2 harness stubs | ~44 | LOCAL |
| `AV-n-6` | 6 (RESAPP r51) | `useInputLedger` + client call; the Model tab's input ledger (6 classes in words, source, last run dated, worked/failed/skipped or not run yet; "1 of 6"; re-run said unavailable; no storage path) | RESAPP FWD-12 | the same five files + the same 2 harness stubs | ~44 (after n-5) | LOCAL |

**Edges and chains:**
- There is no data edge.
- Write sets: n-1 StatTile; n-2 PostureTab + postureCites; n-3 TimelinePanel; n-4 walk.mjs; n-5 -> n-6 the Model-tab set. They are
  pairwise disjoint across chains.
- M = 5 chains, N = 5 now, K = 0 queued (n-6 follows n-5 on its own slot), cap 8.
- The surprise channel is shared append-only.

**Checks (`round11/checks/`, dry-run at base 2bb60cc3 / walk.mjs at HEAD; `_load.cjs`, `bound.cjs`, `census.cjs`, `walkvoid.sh`,
`surfaces.cjs` and `bytes.cjs` copied forward):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| unitlead.cjs | 1 of 3 (amount first: "TWD 71,993,494.73 (unit not resolved)"; the measured control passes at base by design) | 3 of 3 |
| evidence.cjs | 1 of 3 ("pack" / "research pack" in the evidence section; "carried in packs on this object"; control passes at base) | 3 of 3 |
| denied.cjs | 1 of 3 ("Not searched on this day" above 2 served articles; "1 found anyway"; control passes at base) | 3 of 3 |
| loadstate.cjs | 0 of 3 (no waitForLoaded; fixed settles; nothing recorded) | 3 of 3 (scratch walk.mjs, CHECK_SRC_OVERRIDE) |
| versions.cjs | 0 of 3 (no surface, no caller) | 3 of 3 |
| ledger.cjs | 0 of 3 (no surface, no caller) | 3 of 3 |

- **Green arms:**
  - Scratch `C:/tmp/cood-r11a-root/portal` `r11-green-a` carries n-1..n-3 (an issuer-spawned helper agent).
  - Scratch `C:/tmp/cood-r11b-root/portal` `r11-green-b` carries n-5 and n-6 (another helper).
  - `r11-green-b` merged cleanly over `r11-green-a` = the drain state.
  - On it: all five portal checks 3/3, bytes 3/3, ALL 16 of 16 harnesses, and portal `tsc -b` rc=0. The round-10 checks read dates
    3/3, dossier 4/4, cases 3/3 and units 3/3.
  - n-4's green arm is a scratch walk.mjs: loadstate 3/3; round-8 daystate 3/3 and walkerbound 3/3.
- **Harness breaks, NECESSARY, granted:**
  - n-5 / n-6 break `modelPattern.harness.cjs` and `tabs.harness.cjs`. Their stubs of `hooks/useLeadPanelApi` name only the hooks
    they use ("useModelVersions is not a function").
  - Each is granted one stub line per new hook, split by the hooks each cell adds. n-1..n-4 break none.
- **Found by the green arms and folded into the faces:**
  - n-2's absent-source clause is `postureCites.ts` `FILLED_BY` (granted);
  - n-5: BA's served base-case reason carries `BEST_EPS` on the Model tab face, so `caseAbsenceWords` strips mnemonics with the
    page's `formulaInWords`.

**An issuer check defect, found at this cut:**
- `census.cjs` (carried forward since round 6) has had nine literal 0x08 bytes where its MACHINE_PHRASES regex meant `\b`. So
  "the object", "rung", "log cap", "cite(s)" and "covered" were never counted in rounds 6-10's non-prose census; the other phrases
  were.
- Fixed in `round11/checks/census.cjs` only. The earlier rounds' copies stay as their history.
- It is the same class as row Z-S5. The census is an instrument for the CVO's judgment, not a criterion.

**Cut rules applied:**
- (a) Queue-aware bases: no check compares against a base snapshot; n-6 is chained on n-5's slot, not queued on another.
- (b) Every necessary harness break is granted with its exact line and proven green on the combined drain state.

**Battery:**
- comp-schedule and comp-iam: DECLARED-NOT-APPLICABLE (no AWS in the cells; the cut's captures were read-only invokes by the issuer).
- comp-adversary: the checks above, plus `bytes.cjs` on every portal cell (round 10's 0x08 class).
- Blind spots:
  - static markup with the estate chrome stubbed, so layout, selects, hover tooltips and the lazily opened card windows are the
    walk's;
  - loadstate's live latency is the walk's.
- The issuer's close walk:
  - signed-out control first;
  - then VLO, INTU, SAP GY, 992 HK, IMB LN, AZN LN, TSM US, 6501 JP (0 dossier objects of 287) and BA US;
  - TSM's header (n-1); IMB's Posture tab (n-2); 992 HK's opened days (n-3); 6501's Thesis tab loaded, with `load-states.json`
    (n-4); BA's Model tab versions / compare and input ledger (n-5, n-6).

**Rule 24:**
- (i) MECE over the analysis's six items by subtraction: 6 placed; ruling 2 and the NOT-cells named with their reasons.
- (ii) One write set per chain.
- (iii) One intent per cell.
- (iv) No cell moves a served value, a figure, a verdict, a count or an order:
  - n-1 reorders words around an unscaled figure;
  - n-2 and n-3 change words;
  - n-4 changes only when the walker shoots;
  - n-5 and n-6 add read-only surfaces over served routes.

## v12 -- ROUND 12 (issuer, 2026-09-30 ~11:xZ), over PRD v0.5 @bf3a6f5614 (ADMITTED)

**Rectangle:** the round-11 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round11.md` @8e46a89f9f section 4, items 1-6, with rulings 1 (covered vs
  found publishers), 2 (version labels carry the time), 3 (FWD-13 binds every rendered figure) and 5 (FWD-20 first).
- **Cell ids:** `AV-m-1`..`AV-m-5`. Letters e, n, o, p, q, r, s, t, u, v, w are on disk, so round 12 takes `m`.
- **NOT cells:** FWD-14..19, which are graded by FWD-20's instrument once it lands; the driver series (RESAPP ab-6); the names on
  ranked rows (RESAPP). Ruling 4 (the coverage-rule ask) is ruled by the CTO: nothing to route.
- **The issuer's placements:**
  - (a) **Item 6 (FWD-12, one dark band) folds into AV-m-1.** At the cut the estate instrument `ui-contract-check.mjs` read
    bandContainersTopLevel 1, fonts {Lato} and purpleFills 0 (list) / 1 (Security states) on all six states of 5174 @4e4307be
    (DEV 846ecc6c): a build cell's check could not FAIL at base. Its clauses (the band is the identity header; the tab panels are
    white hairline panels; ONE dark container) ride AV-m-1's instrument, which the close grades.
  - (b) **FWD-20's negative control, measured.** The cut's helper read the pre-redesign build (portal 8fa7abde, this project's
    round-1 base) as PASSING the band, fonts, weights, sizes, radii, shadows, lowContrast and purple clauses in all six states
    (AMGT_RESAPP rounds 37-38 fixed that chrome first); only its navy title strips (stripContainers 1 in thesis, exec, model,
    posture; DEV 0) separate it. AV-m-1's AC therefore proves CAN-FAIL on the real page for darkContainers (band + strip) and on a
    planted page for each style clause, beside a clean control. Asked `1.0.0_SA_CTO~Z` (msg 27092); the ENDPOINT was amended to
    this form, PRD v0.5 @bf3a6f5614 (msg 27097).
  - (c) **Cells 2 and 3 share ModelTab.tsx**, so they are one chain on slot ~46: m-2 then m-3.
  - (d) **Item 5's never-collected timeline sentence rides AV-m-4**, which owns TimelinePanel.tsx; m-5 keeps the Posture half.
  - (e) **AV-m-4 takes an import-free `components/publisherNames.ts`.** The green arm first put the name map in TimelinePanel.tsx and
    turned shell.harness.cjs RED (three harnesses stub TimelinePanel with only its component); the shared module needs no harness
    edit (measured by the same helper).
  - (f) `portal/scripts/` is outside PRD PATHS' owned list; FWD-20 names `portal/scripts/ui-smoke.mjs` as its instrument.
- **Portal base:** site-Z local DEV `846ecc6c` (clean).
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round12/fixtures/` = the round-11 set plus 13 SERVED read-only captures at the cut
  (`round12/capture_r12.py`; `opal-amgt-scoped-api` CodeSha256 `zHpr7FhS+irmKofIuKNqTkQm2hj7x2fvS1rrX1ohkfQ=`, LastModified
  2026-09-30T05:20:04Z): `/versions` for BA (15 stamps: four on 20260910, no two in one minute), VLO, IMB, AZN; BA `/thesis`,
  `/overlay`, `/compare` oldest -> newest (7 changed header figures); IMB `/thesis`; 992 HK `/timeline` and `/timeline/day/2026-08-13`
  (now PARTIAL, covered [bbg], articles from wsj and sa); BA `/timeline` and `/timeline/day/2026-09-08` (DENIED, 5 articles); 6501 JP
  `/timeline` (series [] -- never collected). Two local builds for AV-m-1: `C:/tmp/dsgn-r12-dist/pre` (8fa7abde) and
  `C:/tmp/dsgn-r12-dist/dev` (846ecc6c); and three issuer pages `round12/checks/dists/{planted,clean,blank}/index.html`.
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-m-1` | 1 + 6, ruling 5 | the render instrument: `--dist` (a build from disk, no server), `grades.json` over ten clauses per state (darkContainers, bandIsIdentityHeader, tabPanelsWhite + the style clauses), NOT_EXERCISED on a blind page, fourStates, the three harnesses by the estate runner | FWD-20, FWD-12 | `portal/scripts/ui-contract-check.mjs`, `ui-measure.mjs`, `ui-smoke.mjs`, `ui-dist.mjs` (new) | ~45 | LOCAL |
| `AV-m-2` | 2 + ruling 2 | every version labelled with its long date and UTC time (seconds where two stamps share a minute): the list, both pickers, the what-moved sentence | RESAPP FWD-6 page half | `SA/tabs/ModelTab.tsx`, `SA/dateWords.ts` | ~46 | LOCAL |
| `AV-m-3` | 3 + ruling 3 | header-card figures tabular with a tooltip of mnemonic + full value; what-moved lines readable (no >4 fractional digits, no ungrouped 5+ digits), each with its tooltip, named from served fields; no raw float on the Model tab | FWD-13 | `SA/components/HeaderCards.tsx`, `SA/components/StatTile.tsx`, `SA/tabs/ModelTab.tsx`, `SA/constants.ts`, 1 harness stub | ~46 (after m-2) | LOCAL |
| `AV-m-4` | 4 + ruling 1 (+ item 5's timeline sentence) | every served publisher code named (shared import-free map); "Searched:" never credits found articles; "found, listing not run" for a found-only publisher; the absent found set said in words; the never-collected timeline in words | FWD-11, HARVST FWD-5 | `SA/components/publisherNames.ts` (new), `SA/components/TimelinePanel.tsx`, `SA/components/HeaderBrief.tsx` | ~47 | LOCAL |
| `AV-m-5` | 5 (Posture half) | the comparable's side as a sentence when none is identified (never "this name"); the zero-citation footer in words | FWD-11 | `SA/tabs/PostureTab.tsx`, `SA/postureCites.ts` | ~48 | LOCAL |

**Edges and chains:**
- There is no data edge.
- Write sets: m-1 portal/scripts; m-2 -> m-3 ModelTab + dateWords + HeaderCards + StatTile + constants + modelPattern harness;
  m-4 publisherNames + TimelinePanel + HeaderBrief; m-5 PostureTab + postureCites. Pairwise disjoint across chains.
- M = 4 chains, N = 4 now, K = 0 queued (m-3 follows m-2 on its own slot), cap 8.
- The surprise channel is shared append-only.

**Checks (`round12/checks/`, dry-run at base DEV 846ecc6c; `_load.cjs` (repointed at round12/fixtures), `bound.cjs`, `bytes.cjs`,
`census.cjs`, `surfaces.cjs` and `walkvoid.sh` copied forward):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| rendercontrol.cjs | 0 of 3 (no --dist, no grades.json) | 3 of 3 (r12-green-a @75baeecc; a helper run over the fixed clean page) |
| versiontime.cjs | 0 of 3 (four identical "September 10th, 2026" labels; pickers repeat; days only) | 3 of 3 (r12-green-b @1e87ce6c) |
| figures.cjs | 0 of 3 (no card tooltip; "193510.78009600003"; "a line this page has no name for yet"; 10 raw floats on the Model tab) | 3 of 3 (r12-green-b @e19a38e2, over m-2) |
| publishers.cjs | 0 of 3 (ft / bbg / barrons unnamed; "Searched: ... -- 2 found" credits Bloomberg; raw codes in rows and news; "No chatter_daily rows exist for this security_key yet") | 3 of 3 (r12-green-c @1227560a) |
| zerowords.cjs | 1 of 3 ("... has not identified (comparable): ... for this name yet"; "0 of the 0 citations"; the VLO control passes at base by design) | 3 of 3 (r12-green-d @244593b7) |

- **AV-m-1's green arm, measured (r12-green-a @75baeecc, 395+/36- over DEV):** pre-redesign darkContainers FAIL in list (1+2),
  thesis, exec, model, posture (1+1 each), PASS in peers; DEV PASS (1+0) in the five Security states and FAIL in list (1+1: the Lead
  Panel band plus one navy strip); every other clause PASS in both; harnesses drafting 8/8, tabs 20/20, posture 32/32; fourStates
  FAIL in both (DEV: loading 2, error 5, empty 1, no-permission 0). So FWD-20 is NOT green on DEV yet (Universe-mode strip;
  fourStates needs FWD-19's levers) -- the instrument says so, which is its job. The planted page FAILS all eight style clauses; the
  blank page reads NOT_EXERCISED on all ten and exits 1. **An issuer page defect, found by that arm:** the clean control's button
  computed Arial (Chromium's form-control font; the static page lacked the portal reset's `font-family: inherit`); fixed in
  `dists/clean/index.html` before issuance, and the helper's run over the fixed copy read 3 of 3. Two FWD-12 clauses
  (bandIsIdentityHeader, tabPanelsWhite) do not discriminate old from new; arm 1's real-page "can fail" rests on darkContainers.
  The harness clause grades the source tree the instrument sits in, not the --dist build. A full rendercontrol run takes ~6 min.
- **Harnesses:** in the helpers' scratch roots posture, posturePattern and tabs read RED at base because those harnesses run
  `lib/research/api/scoped_amgt.py` from the workspace root and the roots lacked `lib/research`. With it junctioned in, the issuer
  re-ran posture 32/32, posturePattern 13/13, tabs 20/20, shell 10/10, modelPattern 12/12 and errorEmpty 12/12 on r12-green-b and
  r12-green-d. `assembled` and `exportCompare` need file arguments and are never in a bound list.
- **Harness break, NECESSARY, granted:** m-3 brings `@/components/DataTooltip` into `modelPattern.harness.cjs` (no stub: "Cannot find
  module"); one STUBS line is granted. m-1, m-2, m-4 (in the publisherNames.ts form) and m-5 break none.
- **Found by the green arms and folded into the faces:** m-4's name map as an import-free module (placement (e)); m-1's harness runner
  must be the estate runner (`_load.cjs` runHarness) -- another invocation crashed posture on its module paths; the helpers'
  0x08 discipline held (bytes 3/3 on every arm), and one issuer check edit made through a heredoc put a 0x08 into zerowords.cjs,
  repaired byte-level before the dry-run and scanned for over all round12 checks (0).

**Cut rules applied:**
- (a) Queue-aware bases: no check compares against a base snapshot; m-3 is chained on m-2's slot, not queued on another.
- (b) Every necessary harness break is granted with its exact line.

**Battery:**
- comp-schedule and comp-iam: DECLARED-NOT-APPLICABLE (no AWS in the cells; the cut's captures were read-only invokes by the issuer).
- comp-adversary: the checks above, plus `bytes.cjs` on every page cell.
- Blind spots:
  - static markup with the estate chrome stubbed, so hover tooltips, the native select popup and layout are the walk's;
  - figures.cjs reads served figures from /overlay while the what-moved lines read the /thesis bundle's copy (they agree today);
  - publishers.cjs does not render the day tooltip (it shares the sentence function);
  - AV-m-1's fourStates is counted, not forced.
- **The issuer's close:** the signed-out control; the walk of VLO, INTU, SAP GY, 992 HK, IMB LN, AZN LN, TSM US, 6501 JP and BA US
  (BA's Model tab versions and figures, m-2/m-3; 992 HK's and BA's opened days and the news list, m-4; 6501's timeline, m-4; IMB's
  Posture, m-5); and AV-m-1's instrument run on the drain state's build, its six PNGs read by the issuer and handed to the CVO.

**Rule 24:**
- (i) MECE over the analysis's six items by subtraction: 5 cells + item 6 folded (placement (a)); the NOT-cells named with reasons.
- (ii) One write set per chain.
- (iii) One intent per cell.
- (iv) No cell moves a served value, a figure, a verdict, a count or an order: m-1 changes an instrument; m-2 and m-5 change words;
  m-3 formats served figures for display and keeps each full value verbatim one hover away; m-4 names served codes and states which
  served set a publisher is in.
