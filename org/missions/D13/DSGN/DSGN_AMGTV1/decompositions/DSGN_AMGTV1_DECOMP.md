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

## v13 -- ROUND 13 (issuer, 2026-09-30 ~15:xZ), over PRD v0.5 @bf3a6f5614 (ADMITTED)

**Rectangle:** the round-12 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round12.md` @81907cfe5f section 4, items 1-6, with rulings 1 (the page reads
  the served per-field dossier reason; the live no-dossier regression is DSGN's), 2 (FWD-13 binds the Model tab's fiscal cells), 3 (the
  three C14 blocks and FWD-11's raw tokens), 4 (a strip inside a band is that band) and 5 (the no-permission lever).
- **Cell ids:** `AV-l-1`..`AV-l-6`. Letters e, m, n, o, p, q, r, s, t, u, v, w are on disk, so round 13 takes `l`.
- **NOT cells:** `publishers_found_codes` on the page (AMGT_RESAPP ac-3 serves it; round 12's found branch goes live then, msg 27194).
- **The issuer's placements:**
  - (a) **Cell 1 leads and spans four readers.** The pack claim sat on the Thesis pillars AND the header's fund line
    (SecurityOverlay.tsx), Posture's fund line and Exec's management line; one cell fixes every per-field reader. It also refreshes the
    ui-contract fixture set from the live shapes (the CTO put the refresh in cells 1 and 4; it rides cell 1, which owns the file), by
    the issuer's `round13/grants/refresh_fixtures.py`.
  - (b) **Cells 1 and 3 share PostureTab.tsx and ExecManagementTab.tsx**, so they are one chain on slot ~49: l-1 then l-3.
  - (c) **Ruling 3's "derived before C-MODEL-WINDOW-AND-ROWS (5)" rides cell 2**, which owns ModelTab.tsx. Cell 3 adds the issuer's
    same-class Peers words seen on walk L ("R-1", "CSC").
  - (d) **Cells 4, 5 and 6 share portal/scripts**, so they are one chain on slot ~51: l-4, l-5, l-6.
  - (e) **The leadPanelPattern harness re-anchor rides cell 1:** the refreshed rankings are not a dated read (the page is right), so
    three of its checks read a dated variant; the diff was tested on the green arm (15 of 15) and is staged as
    `round13/grants/leadPanelPattern.reanchor.diff`.
- **Portal base:** site-Z local DEV `ba62e945` (clean). The portal DEV push (Andrew-direct @e1b5fd6d8c card 1, `0.0.0_AB_MSTR~Z`) waits
  on cell 1's drain; the issuer signals it with the harness invocations.
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round13/fixtures/` = the round-12 set plus 15 SERVED read-only captures at the cut
  (`round13/capture_r13.py`; `opal-amgt-scoped-api` CodeSha256 `nKWCfQRQ3/lL6cJxgYG3dZr0tcVdOBheeMMNaoWQE+w=`, LastModified
  2026-09-30T11:43:22Z -- redeployed since round 12): /thesis for 6501 JP (every dossier field ABSENT, "no research dossier exists for
  this name"), BA US, IMB LN, VLO US, 992 HK; BA /overlay, /peers, /versions, /compare, /ledger, /timeline; 6501 /overlay; /watchlist;
  the trending-chatter rankings and timeseries. Builds for the instrument cells: `C:/tmp/dsgn-r13-dist/dev` (DEV ba62e945) and
  `C:/tmp/dsgn-r13-dist/pre` (8fa7abde). Static pages `round13/checks/dists/{planted,clean,blank,inband,outstrip}`.
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-l-1` | 1 + ruling 1 | every dossier-field reader reads the per-field served reason; a failed read a designed sentence; "none are stated in the research team's pack" only where a dossier states none; the contract fixtures refreshed from the live shapes; the leadPanelPattern re-anchor | FWD-11, CORPUS no-dossier outcomes | `SA/tabs/ThesisTab.tsx`, `SA/components/SecurityOverlay.tsx`, `SA/tabs/PostureTab.tsx`, `SA/tabs/ExecManagementTab.tsx`, `SA/types.ts`, `SA/__harness__/tests/uiContractFixtures.json`, `SA/__harness__/leadPanelPattern.harness.cjs` | ~49 | LOCAL |
| `AV-l-2` | 2 + ruling 2 (+ the C-MODEL token) | each fiscal cell tabular with the header's tooltip (mnemonic + full value); each row its unit in words; no contract code on the Model tab | FWD-13, FWD-15 | `SA/tabs/ModelTab.tsx`, `SA/components/StatTile.tsx` | ~50 | LOCAL |
| `AV-l-3` | 3 + ruling 3 | an ABSENT description one plain sentence; Exec's CEO profile one sentence; Posture's evidence counts folded; Peers' as-of in long form, no R-1 / CSC; no passage id on the driver chart | FWD-11, FWD-20 (C14) | `SA/components/HeaderBrief.tsx`, `SA/components/ThesisCards.tsx`, `SA/components/ThesisDriverChart.tsx`, `SA/tabs/ExecManagementTab.tsx`, `SA/tabs/PostureTab.tsx`, `SA/tabs/PeersTab.tsx` | ~49 (after l-1) | LOCAL |
| `AV-l-4` | 4 + ruling 4 | darkContainers counts a strip inside a band as that band; a separate container still FAILS | FWD-20, FWD-12 | `portal/scripts/ui-contract-check.mjs`, `ui-measure.mjs`, `ui-smoke.mjs`, `ui-dist.mjs` | ~51 | LOCAL |
| `AV-l-5` | 5 + ruling 5 | `--states-sweep` folds the four designed states into the graded run's fourStates; no-permission standalone and labelled | FWD-19, FWD-20 | the same four scripts | ~51 (after l-4) | LOCAL |
| `AV-l-6` | 6 | FWD-14..19 clauses in grades.json, each with its value; never a PASS on nothing | FWD-14..19 | the same four scripts | ~51 (after l-5) | LOCAL |

**Edges and chains:** no data edge. Write sets: l-1 -> l-3 the dossier readers, fixtures and C14 files (share PostureTab and
ExecManagementTab); l-2 ModelTab + StatTile; l-4 -> l-5 -> l-6 portal/scripts. Pairwise disjoint across chains. M = 3 chains, N = 3 now,
K = 0 queued (l-3, l-5, l-6 follow on their own slots), cap 8. The surprise channel is shared append-only.

**Checks (`round13/checks/`, dry-run at base DEV ba62e945; `_load.cjs` (repointed at round13/fixtures), `bound.cjs`, `bytes.cjs`,
`census.cjs`, `surfaces.cjs`, `walkvoid.sh` and round 12's `dists/` copied forward; round 12's `rendercontrol.cjs` carried as a bound,
repointed at `C:/tmp/dsgn-r13-dist`):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| dossier.cjs | 0 of 3 (6501 and BA read "none are stated in the research team's pack"; all 10 fixture routes differ from the live shapes) | 3 of 3 (r13-green-a @3a9f4c25) |
| fiscal.cjs | 0 of 3 (no fiscal-cell tooltip; 32 of 35 rows without a unit; the planted C-MODEL token visible) | 3 of 3 (r13-green-b @49771e9c) |
| c14.cjs | 0 of 3 ("Description: ABSENT -- ..."; "unreadable object -- status=ABSENT ..."; raw ISO / R-1 / CSC on Peers; passage ids; the count block at rest) | 3 of 3 (r13-green-a @3f79ec94, over l-1) |
| strip.cjs | 1 of 3 (DEV list and the inband page read band 1 + strip 1; the negative arm passes at base by design) | 3 of 3 (r13-green-c @19420ece) |
| sweep.cjs | 2 of 3 (the lever arm FAILS: the sweep is a separate mode; labelling and the blank negative are controls) | 3 of 3 (r13-green-c @cc2705d1) |
| fwd1419.cjs | 1 of 3 (no FWD-14..19 clause; arm 3 vacuous at base) | 3 of 3 (r13-green-c @9ce993d3) |

- **Green arms** (issuer-spawned helpers, scratch roots `C:/tmp/dsgn-r13-green-{a,b,c}`): tsc rc=0 and bytes 3/3 on the page arms;
  ALL 16 of 16 harnesses on r13-green-b; 15 of 16 on r13-green-a before the granted leadPanelPattern re-anchor (tested 15/15);
  rendercontrol 3/3 and the ui-measure self-test OK after every instrument cell.
- **What the instrument arm measured on DEV (for the analysis):** darkContainers PASS in all six states; fourStates PASS (no-permission
  standalone); fwd14..fwd18 PASS; fwd19 FAIL -- Peers has no designed empty state. On the pre-redesign build fwd14, fwd15 and fwd17 FAIL.
- **Issuer check notes:** c14's long-form as-of clause also matches the identity line's date (the raw-ISO clause grades the Peers
  as-of); fiscal.cjs strips tooltip markup with a pattern that holds on the stubbed DataTooltip; dossier.cjs's header says "top-level
  `dossier.status`" meaning `dossier_fields.status`.
- **Ruled at the cut:** BA's per-field served reasons are shown verbatim as ruling 1 asks; they carry producer words ("RECOMMENDATION
  line", "(IDVZ|PFOE|DIVZ)", "class A") -- a round-14 input (readable reasons from AMGT_RESAPP, or a page fallback), not a cell here.

**Cut rules applied:** (a) queue-aware bases: no check compares against a base snapshot; the chained orders follow on their own slots.
(b) Every necessary harness break is granted with its exact change (leadPanelPattern, l-1). The worktree removal Andrew approved
(@e1b5fd6d8c card 2) ran during the cut: every junction link removed first, targets verified intact, branches kept.

**Battery:** comp-schedule and comp-iam DECLARED-NOT-APPLICABLE. comp-adversary: the checks above plus bytes.cjs on every page cell.
Blind spots: static markup (hover, overflow and layout are the walk's); the instrument reads fixture-fed builds (the live page is the
walk's). **The issuer's close:** the signed-out control; the walk (6501 JP's four surfaces for l-1; BA's Model for l-2; BA's header, Exec,
Peers, Posture and Thesis for l-3); the instrument's `--states-sweep` run on a build of the drain state, its PNGs read.

**Rule 24:** (i) MECE over the six items by subtraction: 6 cells, the NOT-cell named. (ii) One write set per chain. (iii) One intent per
cell. (iv) No cell moves a served value, figure, verdict, count or order: l-1 reads served reasons (and refreshes test fixtures); l-2
labels served units and adds tooltips; l-3 changes words and folds a block; l-4..l-6 change an instrument.

## v14 -- ROUND 14 (issuer, 2026-09-30 ~21:xZ), over PRD v0.5 @bf3a6f5614 (ADMITTED)

**Rectangle:** the round-13 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round13.md` @1e7d4bac11 section 4, items 1-7, with rulings 1 (machine tokens in
  served reasons fixed at the page by the caseAbsenceWords pattern), 2 (ERROR says what failed and what to do; the body never on the
  face), 3 (NO-PERMISSION names this page's object), 4 (Peers EMPTY), 5 (Exec's empty sentence from the served reason), 6 (an ABSENT model
  vs its history), 7 (Posture's settled footer) and 8 (the instrument arms: the opened-fold PNG; sizes and radii against C1/C11).
- **Cell ids:** `AV-k-1`..`AV-k-7`. Letters e, l, m, n, o, p, q, r, s, t, u, v, w are on disk, so round 14 takes `k`.
- **NOT cells:** the portal PROD promotion (Andrew's act, analysis s.5); the `radii` clause's blindness to C11's "pill for status dots and
  avatars only" (a helper finding, an instrument input for a later round -- ruling 8 fixes the page, not the instrument).
- **The issuer's placements:**
  - (a) **Chains are drawn from the MEASURED write sets** of seven issuer-spawned helpers' green arms (one per cell, each on its own
    scratch root off DEV 118cd005), not from the analysis's table: the table read "all 7 independent", but cells 1, 2 and 4 all write
    ExecManagementTab.tsx and PostureTab.tsx (and 1 and 2 write ThesisTab.tsx and SecurityOverlay.tsx), and cells 2, 3 and 7 all write
    portal/scripts/ui-contract-check.mjs.
  - (b) **Chain ~52: k-1 -> k-4 -> k-2.** k-1 leads (the shared reason-word mapping k-4 reads through); k-2 last (its error-site edits span
    the four tabs and SecurityOverlay). Stacked in the issuer's scratch root (k-1 + k-4 + k-2 merged clean): reasonwords, execfooter,
    states and bytes 3 of 3 each, all 16 harnesses green, tsc rc=0.
  - (c) **Chain ~53: k-7 -> k-3** (both write ui-contract-check.mjs). k-7 leads (instrument only). Stacked in the issuer's scratch root:
    see the checks table.
  - (d) **Chain ~54: k-5** (ModelTab.tsx; no other round-14 cell writes it). **Chain ~55: k-6** (TimelinePanel.tsx, ThesisCards.tsx; the
    analysis named Exec's 12 dots too, but the helper measured the clause -- it rejects only 1px -- and C11 -- status dots may be pills --
    so ExecManagementTab.tsx is not in k-6).
  - (e) **Cross-chain overlap, ruled by the issuer:** k-2 (~52) and chain ~53 both write PeersTab.tsx (k-2: one `causeAt` line on the error
    branch; k-3: the ABSENT branch) and ui-contract-check.mjs (k-2: the standalone no-permission block; k-7: the posture fold capture;
    k-3: the peers empty patch). Region-disjoint; `git merge-tree` over the green arms reads 0 conflicts (k-7+k-3; the ~52 stack with
    each of k-7 and k-3). The issuer merges both at the drain; serialising the two chains would have made the round one five-deep chain.
  - (f) **k-2's no-permission, measured against the analysis's premise:** no page under src/ renders PanelNoPermission; the "advisor book"
    default's only user is the render script's standalone capture. Ruling 3's "the shared default is untouched" is kept as byte-equal
    defaults (states.cjs arm 3); the page's own sentence lives in a new ResearchNoPermission component the capture renders.
  - (g) **Granted harness changes** (each tested on its green arm, staged as `round14/grants/*.diff`): k-1 adds one loader line to
    drafting, execFallback and execText (they load only named modules, so the new reasonWords module needs naming -- the claim is
    unchanged); k-3 moves one check each in peersReadFailed and peersPattern from the visible "(read ABSENT)" to
    `data-peers-read-status="ABSENT"` (the same fact).
- **Portal base:** site-Z local DEV `118cd005` (clean; LOCAL -- origin/DEV 29bfec2d does not contain ccca64ef; the DEV push is held for
  Andrew's word via 0.0.0_AB_MSTR~Z).
- **Fixtures:** `deliverables/2.0.0_SA_COO~D/round14/fixtures/` = round 13's set carried forward unchanged (no new capture: every cell is
  presentation over shapes already captured). Builds: the base page build `C:/tmp/dsgn-r13-dist/final` (= the page bytes of 118cd005) and
  the base close run `C:/tmp/dsgn-r13-close-render` are INPUTS to peersempty, styles and foldopen and are held through round 14.
- **Frozen at the cut.**

| cell | item | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-k-1` | 1 + ruling 1 | one shared reason-word mapping (the caseAbsenceWords pattern); every face that prints a served dossier reason reads it in words, the whole reason in a data attribute; a new token family worded too | FWD-11 | `SA/reasonWords.ts` (new), `SA/components/SecurityOverlay.tsx`, `SA/tabs/ExecManagementTab.tsx`, `SA/tabs/PostureTab.tsx`, `SA/tabs/ThesisTab.tsx`, `SA/__harness__/{drafting,execFallback,execText}.harness.cjs` (granted) | ~52 | LOCAL |
| `AV-k-4` | 4 + rulings 5, 7 | Exec's empty sentence from the served reason (no static 10-K); the source line names a 10-K only when served; Posture's settled footer states the comparable outcome | FWD-11, FWD-19 | `SA/tabs/ExecManagementTab.tsx`, `SA/tabs/PostureTab.tsx` | ~52 (after k-1) | LOCAL |
| `AV-k-2` | 2 + rulings 2, 3 | PanelError carries the cause in a data attribute on this page (default unchanged); what failed + what to do; this page's no-permission sentence; the capture renders it | FWD-19, FWD-11 | `src/ui/components/states/PanelStates.tsx`, `SA/components/ResearchNoPermission.tsx` (new), `SA/tabs/{ThesisTab,PostureTab,PeersTab,ExecManagementTab}.tsx`, `SA/components/{RankedList,SecurityOverlay}.tsx`, `portal/scripts/ui-contract-check.mjs` | ~52 (after k-4) | LOCAL |
| `AV-k-7` | 7 + ruling 8 | the render run writes posture-cites-open.png and a sidecar whose visible counts equal fwd17's; never silent on a blind read | FWD-17, FWD-20 | `portal/scripts/ui-contract-check.mjs`, `portal/scripts/ui-measure.mjs` | ~53 | LOCAL |
| `AV-k-3` | 3 + ruling 4 | Peers' designed EMPTY state on a served ABSENT read; the sweep's peers empty patch from a served absent shape | FWD-19 | `SA/tabs/PeersTab.tsx`, `portal/scripts/ui-contract-check.mjs`, `SA/__harness__/{peersReadFailed,peersPattern}.harness.cjs` (granted) | ~53 (after k-7) | LOCAL |
| `AV-k-5` | 5 + ruling 6 | with the latest model ABSENT, the compare block is headed as history (not hidden) | FWD-15, FWD-19 | `SA/tabs/ModelTab.tsx` | ~54 | LOCAL |
| `AV-k-6` | 6 + ruling 8 | the timeline's Y-axis ticks at 11px, its legend swatches and the MACHINE chip at 2px (C1, C11) | FWD-20 | `SA/components/TimelinePanel.tsx`, `SA/components/ThesisCards.tsx` | ~55 | LOCAL |

**Edges and chains:** no data edge. M = 4 chains (~52 k-1 -> k-4 -> k-2; ~53 k-7 -> k-3; ~54 k-5; ~55 k-6), N = 4 now, K = 0 queued (k-4,
k-2 and k-3 follow on their own slots), cap 8. Write sets pairwise disjoint across chains EXCEPT placement (e). The surprise channel is
shared append-only.

**Checks (`round14/checks/`, dry-run at base DEV 118cd005 from the shared root; `_load.cjs` repointed at round14/fixtures; `bound.cjs`,
`bytes.cjs`, `census.cjs`, `surfaces.cjs`, `walkvoid.sh`, `dists/` and `rendercontrol.cjs` carried from round 13):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| reasonwords.cjs | 1 of 3 (BA: 4 token faults over 4 faces; a planted new family verbatim; arm 3 control) -- issuer re-run | 3 of 3 (r14-green-a @f2258ff0) |
| states.cjs | 1 of 3 (7 of 7 surfaces error on a forced 503, six print the body's braces; no page no-permission; arm 3 control) -- issuer re-run | 3 of 3 (r14-green-b @8b1ee539) |
| peersempty.cjs | 1 of 3 (fwd19 FAIL, peers/empty unreachable; no PanelEmpty on an ABSENT read; arm 3 control), 866 s | 3 of 3 (r14-green-c @b7931ed3), 928 s |
| execfooter.cjs | 0 of 3 (6501's static 10-K; BA's footer "still loading" on a retrying read; the fallback names a 10-K) -- issuer re-run | 3 of 3 (r14-green-d @d7d29dd5) |
| modelhistory.cjs | 2 of 3 (the compare headed "What moved between two versions" beside the ABSENT sentence; arms 2-3 controls) -- issuer re-run | 3 of 3 (r14-green-e @2a9ef6a4) |
| styles.cjs | 1 of 3 (sizes FAIL [10] and radii FAIL in five states; ticks 10px, swatches 1px; arm 3 control), 608 s | 3 of 3 (r14-green-f @88205f47), 630 s |
| foldopen.cjs | 1 of 3 (no opened-fold PNG, no visible count; blank silent; arm 2 control) | 3 of 3 (r14-green-g @bce8e785) |

- **Green arms** (issuer-spawned helpers, scratch roots `C:/tmp/dsgn-r14-green-{a..g}`, portal branches `r14-green-{a..g}` off 118cd005):
  tsc rc=0, bytes 3/3 and ALL 16 of 16 harnesses on every arm (k-1 and k-3 with their granted harness lines).
- **Stacks (issuer):** `C:/tmp/dsgn-r14-green-h` = k-1 + k-4 + k-2 (chain ~52): reasonwords, execfooter, states, bytes 3 of 3; 16 of 16;
  tsc 0. `C:/tmp/dsgn-r14-green-i` = k-7 + k-3 (chain ~53): foldopen and peersempty running at the issuance (merge-tree 0 conflicts); their result goes to the issuer's drive log, and k-3's worker keeps foldopen 3 of 3 as a stated condition.
- **Issuer amendment at the cut -- foldopen.cjs arm 2:** the helper's control compared every grades.json VALUE with the round-13 close run;
  k-2's and k-3's instrument changes move values by design once drained, so the arm now compares SHAPE (every base cell present and graded,
  no new cell, the same number of graded cells). Re-run by the issuer after the amendment: base 1 of 3 (arms 1 and 3 FAIL, arm 2 the control PASS: 72 cells present and graded, no new cell), 705 s; green r14-green-g 3 of 3, 707 s.
- **Issuer check notes:** execfooter arm 1 matches the served reason's plain words of 4+ letters (the chain words them through k-1's
  mapping; stacked, 3 of 3); peersempty arm 1 needs a full fwd19 PASS (another panel's regression fails it too); styles and peersempty
  build the page from the worktree (vite) and take 10-15 minutes; round 13's frozen dossier.cjs arm 2 will read FAIL after k-1 (it
  expects BA's verbatim reason; a round-13 check, not a round-14 bound).

**Cut rules applied:** (a) queue-aware bases: no check compares values against a base snapshot (foldopen amended); the chained orders
follow on their own slots. (b) Every necessary harness break is granted with its exact change. (c) At most three mechanical criteria per
order (the cell's check, its harness bound, bytes -- or, for the instrument cell, rendercontrol and the self-test).

**Battery:** comp-schedule and comp-iam DECLARED-NOT-APPLICABLE. comp-adversary: the checks above plus bytes.cjs on every page cell.
Blind spots are named per order. **The issuer's close:** the signed-out control; the signed-in walk (BA's header, Exec, Posture, Thesis
for k-1; 6501's Exec and BA's Posture for k-4; the Model tab for k-5); the instrument's `--states-sweep` run on a build of the drain
state (every error PNG and the standalone no-permission for k-2, peers-empty.png for k-3, model-empty.png for k-5, sizes/radii for k-6,
posture-cites-open.png for k-7), its PNGs read.

**Rule 24:** (i) MECE over the seven items by subtraction: 7 cells, the two NOT-cells named. (ii) One write set per chain, the one
cross-chain overlap ruled (e). (iii) One intent per cell. (iv) No cell moves a served value, figure, verdict, count or order: k-1, k-4 and
k-2 change words and where a served reason sits; k-3 and k-5 frame a served absence or history; k-6 changes type size and radius; k-7
changes an instrument.


## v15 -- ROUND 15, THE FRIDAY ROUND (issuer, 2026-10-01 ~05:5xZ), over PRD v0.6 @bc4f634248 (ADMITTED)

**Rectangle:** the round-14 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round14.md` @950ae4bb4f section 3, rows 1-5, rulings 1-4, as amended by the CTO's
  msg 27547 (CONTRACT amendment 1 @c7f9fa44fa: `tabs/ModelTab.tsx` is AMGT_CORPUS's through the Friday freeze; row 5 is narrowed to the
  BA pack sentences on Thesis and Exec; k-5's Model-face half moved to CORPUS round 28). Plus row `DSGN_AMGTV1-Z-S9` (a repair, batched
  into row 4's cell). The shared Friday CONTRACT `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` binds.
- **Cell ids:** `AV-f-1`..`AV-f-6`. Letters e, k-w are on disk, so round 15 takes `f`.
- **NOT cells:** the Model-face contradiction (k-5 PARTIAL, moved to AMGT_CORPUS by msg 27547; the ModelTab pack lines were routed to
  `2.0.0_SA_COO~X`, the writer); Posture's served "ABSENT" (ruling 3, AMGT_RESAPP's); the PROD promote (Andrew's act); row Z-W4-S1
  (exportCompare vs the page, an export surface not on the demo).
- **The issuer's placements:**
  - (a) **Row 3 is split into two orders:** `AV-f-6` (extract the /philosophy card face into `src/ui/components/graphic/GraphicCard.tsx`;
    the four selected-name header cards render through it) and `AV-f-3` (the Lead Panel header through it). The extraction touches no
    LeadPanel file, so it runs beside the bars; the panel half chains after it.
  - (b) **Chains from the MEASURED write sets** of four issuer-spawned helpers' green arms (scratch roots `C:/tmp/dsgn-r15-green-{a..d}`,
    portal branches `r15-green-{a..d}` off b336b141), and `git merge-tree` over them: a x b conflicts on `LeadPanel.tsx` and
    `leadPanelPattern.harness.cjs` (both on chain ~56, serial); a x c conflicted only on `types.ts`; b x c clean.
  - (c) **Issuer DIRECT-ACT before the cut:** portal DEV `a41cf763` types the served Friday fields once (AMGT_RESAPP af-2's names per its
    COO's msg 27543 and the CONTRACT s.1-4 shapes): `places_moved(_reason)` on ranking rows; `return_30d_pct`, `score_pct`,
    `pct_jump_pct` on price rows; the `CollectedChatter*` payload; `as_of_date`, `requested_as_of`, `dated`, `stale_trading_days`,
    `absent_reason` on an axis read. Additive, tsc -b rc=0, 13 of 13 page harnesses green. This removes the a x c conflict.
  - (d) **Chain ~56: f-1 -> f-2 -> f-3** (all write `LeadPanel.tsx`). f-3 ALSO waits for chain ~57 to drain (it imports `GraphicCard`):
    the issuer merges ~57 into CLOUD/DEV and into the ~56 branches before handing f-3 over. **Chain ~57: f-6.** **Chain ~58: f-4 -> f-5**
    (both write `reasonWords.ts`).
  - (e) **Cross-chain overlap, ruled by the issuer:** the harness files `errorEmpty`, `tabs`, `shell` are granted to chains ~56 (re-anchors),
    ~57 (a `GraphicCard` stub) and ~58 (`shell`'s `axis_footnote` re-anchor): region-disjoint; merge-tree auto-merged a x b on all three.
    The issuer merges at the drain.
  - (f) **The chatter route:** AV-f-2 adds the client call to the already-mounted template
    `/lead-panel/timeseries/collected/chatter` now (CONTRACT s.1 names it mounted), so no separate wiring cell is needed when AMGT_RESAPP
    serves it; until then the face is the designed empty state, never fixture data. The header's fields (AV-f-4) are af-2's served names;
    the price bars read `return_30d_pct` on the existing trending price route. When RESAPP lands them on DEV the issuer re-runs the
    checks on live captures (a fixture refresh, no shape change).
  - (g) **Width:** analysis cap 3 (placement s.2, the box runs 8 COO lanes). M = 3 chains, N = 3 now, K = 3 queued (f-2, f-3, f-5 follow on
    their own slots).
- **Portal base:** site-Z local DEV `a41cf763` (on top of b336b141 = origin/DEV at the cut; a41cf763 is LOCAL).
- **Fixtures:** `round15/fixtures/` -- `r15a.*` (the trending price ranking with `return_30d_pct`; the CONTRACT s.1 monthly payload), `r15c.*`
  (BA, VLO, 6501 overlays in the af-2 shape, renamed by the issuer; 6501's live /thesis capture with the M-1 reason), grant diffs
  `r15{a,b,c}.grant.*`. `round15/checks/_load.cjs` reads round15/fixtures first, then round 14's.
- **Frozen at the cut.**

| cell | row | what it builds | serves | writes (SA/ = portal/src/pages/SecurityAnalysis/) | slot | risk |
|---|---|---|---|---|---|---|
| `AV-f-1` | 1 | price as ranked horizontal bars of the served `return_30d_pct`, |value| order, sign by colour; the List/Chart toggle, the line chart, the Movement control and the price list removed; the whole universe read | FWD-22, 18, 2 | `SA/components/{PriceBars (new),LeadPanel}.tsx`, `SA/hooks/useLeadPanelApi.ts`, `SA/constants.ts`, 4 granted harnesses | ~56 | LOCAL |
| `AV-f-2` | 2 | chatter as one bubble per security, area ~ the month's `collected`, a month cursor, "articles collected"; the client call to the mounted template | FWD-21 | `SA/components/{ChatterBubbles (new),LeadPanel}.tsx`, `SA/hooks/useLeadPanelApi.ts`, `portal/src/api/endpoints/amgt-lead-panel.ts`, `SA/constants.ts`, the same 4 harnesses | ~56 (after f-1) | LOCAL |
| `AV-f-6` | 3 (header half) | the /philosophy card face extracted (byte-identical /philosophy); the four header cards through it | FWD-23 | `src/ui/components/graphic/GraphicCard.tsx` (new), `pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx`, `SA/components/HeaderCards.tsx`, 4 granted harness stubs | ~57 | LOCAL |
| `AV-f-3` | 3 (panel half) | the Lead Panel header through the card face, no internal name, Starred a Segmented, 0 hex in the panel's chart files | FWD-23 | `SA/components/{LeadPanel,PriceBars,ChatterBubbles}.tsx`, `leadPanelPattern.harness.cjs` (granted) | ~56 (after f-2 AND ~57's drain) | LOCAL |
| `AV-f-4` | 4 + Z-S9 | the header prints the served `as_of_date`, "Breakout (price)" reads the breakout row, places moved, `absent_reason`; the reason mapping drops interface codes | FWD-24, 11 | `SA/components/SecurityOverlay.tsx`, `SA/reasonWords.ts`, `shell.harness.cjs` (granted) | ~58 | LOCAL |
| `AV-f-5` | 5 (narrowed) | Thesis and Exec pack sentences read their own served reason (no presupposed pack) | FWD-11 | `SA/reasonWords.ts`, `SA/components/ThesisCards.tsx`, `SA/tabs/ExecManagementTab.tsx` | ~58 (after f-4) | LOCAL |

**Edges and chains:** one data edge (f-3 imports f-6's module). M = 3 chains (~56 f-1 -> f-2 -> f-3; ~57 f-6; ~58 f-4 -> f-5), N = 3 now,
K = 3 queued, cap 3. Write sets pairwise disjoint across chains EXCEPT placement (e). The surprise channel is shared append-only.

**Checks (`round15/checks/`, dry-run by the issuer at base DEV a41cf763 from the shared root):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| pricebars.cjs | 2 of 3 (0 bars for 32 served rows; View toggle, Movement control, list table on the price face; arms 2-3 controls) | 3 of 3 (r15-green-a @7cb92a05) |
| bubbles.cjs | 2 of 3 (no ChatterBubbles.tsx, no bubbles in LeadPanel; arms 2-3 controls) | 3 of 3 (r15-green-a @7cb92a05) |
| cardface.cjs | 0 of 3 (no shared module; 4 of 4 cards not through the face; no module to mutate) | 3 of 3 (r15-green-b @69653d85) |
| panelhead.cjs | 2 of 3 (title "Lead Panel", no card-face header, hand-built Starred; arms 2-3 controls) | 3 of 3 (r15-green-b @69653d85) |
| headerread.cjs | 2 of 3 (15 faults: Breakout reads Trending, places moved, "today", no served day, M-1; arms 2-3 controls) | 3 of 3 (r15-green-c @993d933c, issuer-renamed to af-2 names) |
| packwords.cjs | 1 of 3 (BA, VLO, 992 HK Exec presuppose a pack the served reason says is missing; arm 3 control; served reasons agree 6 of 6) | 3 of 3 (r15-green-d @86944155) |

- Every green arm: tsc -b rc=0; the harnesses each loads green with its grants; round-14 reasonwords, execfooter, modelhistory 3 of 3
  where touched. posture.harness.cjs reads S3 live and is unstable in scratch roots: excluded from every bound (its stub grant still
  applies). assembled and exportCompare need arguments: red at base, not bounds.
- **Issuer check notes:** every check renders statically (seconds, not the 15-minute builds of round 14); the negative arms extract the
  b336b141 sources with git into a temp dir; hooks are stubbed, so the live read limit and the cursor click are carried by the cell
  text and the close walk, not the checks.

**Cut rules applied:** (a) queue-aware bases: no check compares values against a base snapshot. (b) Every harness break is granted with
its exact diff (`git apply --check` OK on a41cf763 for all 10). (c) At most three mechanical criteria per order.

**Battery:** comp-schedule and comp-iam DECLARED-NOT-APPLICABLE. comp-adversary: the checks above plus round 14's bytes.cjs. Blind spots
are named per order. **The issuer's close:** the signed-out control; a signed-in walk on the drained DEV build (the price bars, the
chatter bubbles stepped two months, the panel header beside /philosophy, BA, VLO and 6501's headers, BA's Thesis and Exec); the render
run's PNGs read. **The Friday close walk** (CRO~Z `/ui-walk`, 18:00-21:00 ET) follows the freeze.

**Rule 24:** (i) MECE over the analysis's five rows by subtraction: 6 orders (row 3 split in two), Z-S9 batched into row 4, the four
NOT-cells named. (ii) One write set per chain, the cross-chain harness overlap ruled (e). (iii) One intent per order. (iv) No order moves
a served value: f-1 orders served bars by a served value (CONTRACT s.2) and prints it as served; f-2 sizes by a served count; f-4 prints
served fields where the page printed the wrong one; f-3, f-5 and f-6 change chrome and words.


## v16 -- ROUND 16 (issuer, 2026-10-01 ~08:3xZ), over PRD v0.6 @bc4f634248 (ADMITTED)

**Rectangle:** the round-15 analysis's enrichment list.
- **Source:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round15.md` @68e34e1e97 section 4, rows 1-5, rulings 1-5 (cells 1-3 first);
  the CTO's walker rule (msg 27641: ARM / DISARMED posts to 0.0.0_AB_MSTR~Z until the lease lands). Freeze 22:00Z.
- **Cell ids:** `AV-g-1`..`AV-g-5` (letter g; e, f, k-w are on disk).
- **NOT cells:** ModelTab's "Lead Panel" (AMGT_CORPUS's file; fixed by that writer at portal 54f3a252); the live price face's empty
  ranking and the chatter route's 400 (AMGT_RESAPP af-2 / round 57 deploys -- server-side); `format:money` and the timeline findings
  of walk 20261001T073050Z (carried to the round-16 analysis); the posture harness's S3 instability.
- **The issuer's placements:**
  - (a) **g-1 carries a second item:** the walker's lead-panel steps (walk.mjs still walks Trending/Breakout x List/Chart --
    `walker:control-missing` x4 on walk 073050Z); the same file as the lease, so the same order.
  - (b) **Ruling on row AMGT_RESAPP-Z-W200-S1:** the Thesis pillars "no research pack" stays -- the designed worded form of the
    served "class A report" (CTO round-13 ruling 1, k-1 MET; round-14 reasonwords and round-15 packwords grade it; AV-f-5 made Exec
    agree). nolabel.cjs carries the clause gated off (PILLARS_GRADED). Correction sent to 2.0.0_SA_COO~Z.
  - (c) **Chains from the green arms' write sets:** ~59 g-1 -> g-5 (file-disjoint: `.claude/skills/ui-walk/*` then the tabs and
    SecurityOverlay -- chained only for throughput under cap 3); ~60 g-2 -> g-4 (both `LeadPanel.tsx`); ~61 g-3 (the instrument).
  - (d) **Cross-chain overlap, ruled:** g-3 may re-anchor `errorEmpty`/`leadPanelPattern`/`tabs` harness claims; g-4 may re-anchor
    `errorEmpty`/`tabs`; g-3 may add `data-chatter-denominator` to `ChatterBubbles.tsx` (an attribute) while g-4 may touch the same
    file's unserved branch. Region-disjoint; the issuer merges at the drain and re-runs every check on the merged DEV.
  - (e) **Checks at the cut:** every check dry-run at base DEV 209678ff (the negative arms pin f4adf790 or the pre-round walker
    files). g-3's and g-4's helper green arm (r16-green-g) was in progress at the cut; g-3 and g-4 are QUEUED behind g-2/the slot
    opening, and the issuer reads that green arm 3 of 3 before handing either over (or amends with the gate limb named).
  - (f) **Width:** cap 3. M = 3 chains, N = 3 now (g-1, g-2, g-3 -- g-3 handed when its green proof reads), K = 2 queued (g-4, g-5).
- **Portal base:** site-Z local DEV `209678ff` (f4adf790 + AMGT_CORPUS round 28's ModelTab/modelSheet commits). LOCAL.
- **Fixtures:** `round16/fixtures/r16g.collected.chatter.json` (+ its builder) -- the CONTRACT s.1 live shape (95 rows, 73 empty).
- **Frozen at the cut.**

| cell | row | what it builds | serves | writes | slot | risk |
|---|---|---|---|---|---|---|
| `AV-g-1` | 1 (+a) | the walker lease (conditional DDB lease before SSM; holder-only disarm); walk.mjs walks the Friday faces | FWD-20, FWD-1 | `.claude/skills/ui-walk/{ui_walker_account.py,walk.mjs,SKILL.md}` | ~59 | LOCAL |
| `AV-g-2` | 2 | header cards fill their grid at equal widths; eyebrows >= 11px with passing contrast | FWD-23, 20 | `SA/components/{HeaderCards,LeadPanel}.tsx` | ~60 | LOCAL |
| `AV-g-3` | 3 | the render instrument: live-shape chatter fixture, price- and chatter-face captures, fwd18/band/fwd19 re-anchored | FWD-20, 21, 22 | `portal/scripts/{ui-contract-check,ui-measure}.mjs`, `uiContractFixtures.json`, `ChatterBubbles.tsx` (attribute), 3 harnesses (re-anchor) | ~61 | LOCAL |
| `AV-g-4` | 4 | the chatter face's designed unavailable sentence until the route is served | FWD-21, 19 | `SA/components/{LeadPanel,ChatterBubbles}.tsx`, 2 harnesses (re-anchor) | ~60 (after g-2) | LOCAL |
| `AV-g-5` | 5 | no "Lead Panel" on any DSGN face; the identity block through GraphicCard | FWD-23, 11 | `SA/tabs/{Thesis,Peers,Posture,ExecManagement}Tab.tsx`, `SA/components/SecurityOverlay.tsx` | ~59 (after g-1) | LOCAL |

**Checks (`round16/checks/`, dry-run at base DEV 209678ff):**

| check | base (FAIL as expected) | green arm |
|---|---|---|
| walkerlease.py | 1 of 3 (arm 1 0 of 6; arm 3 vacuous on the base module) | 3 of 3 (r16-green-f @49bf677ac4) |
| walksteps.cjs (issuer) | 2 of 3 (7 faults: List/Chart/Breakout, no bars/bubbles/cursor, data-row-lead) | -- (static; the next close walk) |
| headerchrome.cjs | 2 of 3 (sizes 10px and lowContrast in 6 of 6 states; widths 137/195/86/169; arm 3 /philosophy control), ~10 min | 3 of 3 (r16-green-e @ea7b0a9b) |
| instrument.cjs | 2 of 3 (8 faults: no chatter fixture, no price/chatter captures, fwd18, band, fwd19; arm 3 5 of 5 planted caught), 303 s | in progress (r16-green-g) |
| unavailable.cjs | 2 of 3 ("Read failure" + the SourceCaption under the unserved chatter face) | in progress (r16-green-g) |
| nolabel.cjs | 2 of 3 (9 faults: 4 tabs "Lead Panel"; identity block off the card face) | 3 of 3 (r16-green-h @2f48ad29) |

**Cut rules applied:** at most three mechanical criteria per order; no check compares values against a base snapshot; harness changes
are re-anchors only. **Battery:** comp-schedule and comp-iam DECLARED-NOT-APPLICABLE (walkerlease stubs every AWS call). **The issuer's
close:** a signed-in walk with the NEW walker (ARM/DISARMED posted to MSTR~Z), the render run with g-3's instrument, PNGs read.

**Rule 24:** (i) the analysis's five rows by subtraction: 5 orders (+ the walker steps in g-1), the NOT-cells named. (ii) One write set
per chain, overlaps ruled (d). (iii) One intent per order. (iv) No order moves a served value: g-1 changes a tool; g-2 chrome; g-3 an
instrument; g-4 the words of an unserved state; g-5 words and chrome.


## v17 -- ROUND 17 (issuer, 2026-10-01 ~09:5xZ), over PRD v0.6 @bc4f634248 (ADMITTED) -- TWO DIRECT ACTS

**Rectangle:** the round-16 analysis @ce875b7bc1 section 3, rows 1-2 (rulings 1-4). Freeze 22:00Z.
- **Cell ids:** `AV-h-1`, `AV-h-2` (letter h).
- **Both cells take the DIRECT-ACT path** (`/dispatch`: one cell, small, `<risk>LOCAL</risk>`; `<direct_act>true</direct_act>`; no
  L2/L4-R/L8-L10; the close is the issuer's one real run).
- **Placement (a):** row 1 is a walk plus a walker change. A worker cannot post ARM/DISARM to 0.0.0_AB_MSTR~Z, so the build half
  (walk.mjs waits >= 30 s for `[data-price-bar]`, records a no-bars finding with the route body, flags raw-key bubble labels) is
  AV-h-1, and the walk itself is the issuer's close act (ruling 1: bars render -> proven; no bar after the wait -> the route body and
  component state captured and root-caused this round). After AMGT_RESAPP ah-2 deploys, the close walk re-reads the chatter labels
  (ruling 3).
- **Placement (b):** AV-h-2 is SecurityOverlay.tsx only (the identity card's panel background), disjoint from AV-h-1.
- **Chains:** ~62 AV-h-1; ~63 AV-h-2. M = 2, N = 2, cap 3.
- **Checks:** `round17/checks/pricewait.cjs` (issuer; base 2 of 3: no wait, no raw-key flag); `round16/checks/headerchrome.cjs` (base 2 of
  3 on DEV 03311745: lowContrast 5 in each Security state).
- **Portal base:** DEV 03311745 (LOCAL). **Frozen at the cut.**
- **Rule 24:** two rows, two orders; one write set each; no served value moves (a walker change; a panel colour).


## v18 -- ROUND 18 (issuer, 2026-10-01 ~10:4xZ) -- TWO DIRECT ACTS

**Rectangle:** the CTO's ruling msg 27760 (CONTRACT amendment 3 @b9d096f6dd) on the acceptance walk's one defect (round-17 close
@4b0135afec): the price bars printed the served `return_30d_pct` at full float precision and clipped. **Cell:** `AV-i-1` (letter i),
DIRECT ACT, `<risk>LOCAL</risk>`, `PriceBars.tsx` only: one decimal printed with sign and "%", the whole value in `data-price-value`.
**Check:** `round18/checks/precision.cjs` (issuer): base portal DEV c6aacc68 2 of 3 (128 faults). **Chain:** ~64 alone.
**Close:** the issuer's live walk (ARM/DISARMED to 0.0.0_AB_MSTR~Z) reads the price PNG for one-decimal values inside the panel.
**Second cell (CTO msg 27762, from AMGT_CORPUS ADJUDICATION_v36):** `AV-i-2`, DIRECT ACT, `SecurityOverlay.tsx` + `GenerationCaption.tsx`:
the header's readings line reads the monthly route ("<k> of <n> covered names collected this month") in place of the legacy chatter
ranking caption, and "1 name" never "1 names". Check `round18/checks/headerline.cjs` (issuer): base 2 of 3. Chain ~65 alone.
**Width:** M = 2 chains (~64, ~65), N = 2, cap 3.
**Rule 24:** two rows, two orders, file-disjoint; no served value moves (display rounding; a caption reading a served route).


## v19 -- ROUND 19 (issuer, 2026-10-01 ~11:1xZ) -- ONE DIRECT ACT

**Rectangle:** the CTO's ruling msg 27768 on the round-18 close: the selected-name header's chatter cell reads the legacy ranking point
("TRENDING (CHATTER) #1 | 0/100"). **Cell:** `AV-j-1` (letter j), DIRECT ACT, `<risk>LOCAL</risk>`, `SecurityOverlay.tsx`: the cell
(`data-header-reading="chatter"`) shows the name's collected count for the latest month from `useCollectedChatter`, or a designed absent
sentence; no "#", "/100" or "Trending". **Check:** `round19/checks/chattercell.cjs` (issuer): base portal DEV 4c02f293 2 of 3.
**Retired:** round15 `headerread.cjs`'s chatter-cell clause (it grades the legacy rank and score this ruling removes); its breakout clause
is read on the live walk. **New cut rule applied:** the order carries `tsc -b` in AC3. **Chain:** ~66 alone. **Close:** the issuer's live
walk; then DEV is DSGN's freeze candidate (ruling 27768).
**Rule 24:** one row, one order; no served value moves (a cell now reads a served count instead of a dead ranking point).


## v20 -- ROUND 20 (issuer, 2026-10-01 ~14:4xZ) -- ONE DIRECT ACT

**Rectangle:** the CTO's ruling msg 27874 (on COO~Z 27871: the overlay serves top-level `display_name` for all 94 names). **Cell:**
`AV-x-1` (letter x; e-w are on disk), DIRECT ACT, `<risk>LOCAL</risk>`, `SecurityOverlay.tsx` (+ the optional fields in `types.ts`): the
served company name above the ticker in `data-identity-name`; the ticker only when none is served, never a placeholder. **Check:**
`round20/checks/namecard.cjs` (issuer): base portal DEV f73cd009 2 of 3. AC3 carries `tsc -b`. **Chain:** ~67 alone. **Deadline:** land by
21:30Z with the walk evidence; otherwise f73cd009 stays the freeze candidate. **Rule 24:** one order; no served value moves.


## v21 -- ROUND 21 (issuer, 2026-10-01 ~15:4xZ) -- ONE DIRECT ACT

**Rectangle:** the CTO's ruling msg 27914 (on the round-20 walk's shot 009). **Cell:** `AV-y-1` (letter y), DIRECT ACT,
`<risk>LOCAL</risk>`, `StatTile.tsx` (+ `HeaderCards.tsx` if the flip needs it): the figure tooltip stays inside its pop-up, and its face
shows the plain label, definition and full value, never the Bloomberg code. **FWD-13 reconciliation (issuer):** FWD-13's "its tooltip
carries the mnemonic" is kept by `data-mnemonic` in the markup; the CTO may amend FWD-13's text instead. **Check:**
`round21/checks/tipface.cjs` (issuer, with a DataTooltip stub that renders the real component's text): base portal DEV da0b3bd7 2 of 3.
AC3 carries `tsc -b` and all 14 harnesses (ModelTab inherits the face; ModelTab.tsx itself is not edited). **Chain:** ~68 alone.
**Deadline:** walk clean by 21:30Z, otherwise drop; da0b3bd7 stays the candidate. **Rule 24:** one order; no served value moves.


## v22 -- ROUND 22 (issuer, 2026-10-02 ~06:5xZ), over PRD v0.7 @9ef3af2bee (ADMITTED)

**Rectangle:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round21.md` @e14de1769c section 3A, rows A1-A4 (rulings 1-5; msg 28252,
which supersedes the hold ruling 28223). Deadline: drained by **11:30Z**, or the cell drops and PROD stays on `b3a1d8a6`.
- **Cell ids:** `AV-z-1` (A1), `AV-z-2` (A2), `AV-z-3` (A3), `AV-z-4` (A4) (letter z; e-y are on disk).
- **The issuer's placements:**
  - (a) **A3 takes no order.** At the cut, `PriceBars.tsx:116-120` already labels a bar with the served `name` (or
    `classification.name`), the ticker only when none is served, and `ChatterBubbles.tsx:96` prints the served `display_name`.
    The 24 unnamed bars are a served gap (RESAPP round 61 cell B1). A3 is graded at the close as the issuer's real-run read after B1
    deploys: 0 bars whose label equals a `security_key` when the served row carries a name. No cell is cut for coverage alone.
  - (b) **"ABSENT" in Posture reason 2 is located: it is SERVED.** It is the thesis bundle's `posture.basis[1].claim` ("Both names' fit
    scores are ABSENT rather than low ..."), printed verbatim by `PostureTab.tsx`. Its producer fix is not in RESAPP B2's list. It is
    routed to `1.0.0_SA_CTO~Z` (one line), and A1's page guard covers it until the producer words it.
  - (c) **Chains from write sets.** A1 and A2 both write `PeersTab.tsx` and may both re-anchor the peers harnesses, so they are ONE
    chain on one worker: ~69 AV-z-1 -> AV-z-2. AV-z-4 writes only `errorEmpty.harness.cjs`: ~70 alone. A1 does not touch
    `errorEmpty.harness.cjs`, and AV-z-4 touches nothing else.
  - (d) **A4, issuer reading at the cut:** `unresolved_row_navigates`, `a_click_sent_a_ticker` and `error_claims_no_daily_row` read
    the RankedList click tree and the failed_request render (`ranked_row_click_handlers_found` true), so they are exercised and stay.
    The vacuous claim is the starred pair (`starred_successful_empty`, `starred_failed_request` ->
    `starred_error_differs_from_starred_empty`), met by the ranking footers since StarredList left LeadPanel.
  - (e) **Width:** M = 2 chains, N = 2, cap 3. The queued order on ~69 (AV-z-2) is handed by continuing the worker.
- **Portal base:** origin DEV `3ca6c53a` (fetched 06:4xZ; it contains site-Z DEV `24646bca`, and `src/pages/SecurityAnalysis` is
  identical between them). The checks' negative arms pin `24646bca`.
- **Frozen at the cut.**

| cell | row | what it builds | serves | writes | slot | risk |
|---|---|---|---|---|---|---|
| `AV-z-1` | A1 | one page guard: a served or page-written string carrying a code-shaped token prints a plain generic reason (the string rides a data- attribute); Exec Lusha line, Posture claims, Peers absent-column list and column-head tips, `cscTable.ts`'s own reason text | FWD-11 | `SA/tabs/{ExecManagement,Posture,Peers}Tab.tsx`, `SA/{cscTable,reasonWords,postureCites}.ts`, 9 harnesses (re-anchor) | ~69 | LOCAL |
| `AV-z-2` | A2 | the Peers subject row's Price and EV read the header's served PX_LAST and CURR_ENTP_VAL, in the column's own format | FWD-8 | `SA/tabs/PeersTab.tsx`, peers harnesses (stub re-anchor) | ~69 (after z-1) | LOCAL |
| `AV-z-3` | A3 | no order: the issuer's close read after RESAPP B1 deploys | FWD-2 | -- | issuer | -- |
| `AV-z-4` | A4 | errorEmpty's starred pair retired, or re-pointed at the price face's starred state | instrument (Z-W56-S4) | `SA/__harness__/errorEmpty.harness.cjs` | ~70 | LOCAL |

**Checks (`round22/checks/`, dry-run at base DEV 24646bca = 3ca6c53a for these paths):**

| check | base (as expected) |
|---|---|
| codeface.cjs (AV-z-1) | FAIL 2 of 3: exec 2 tokens (`_Equity`, `.json`), posture 1 (`ABSENT`), peers 20 (`ey_ntm`, `cash_mv`, `ABSENT` ...) |
| subjectrow.cjs (AV-z-2) | FAIL 2 of 3: Price "--" (want "204.80"), EV "--" (want "193,511") |
| starredclaims.cjs (AV-z-4) | FAIL 2 of 3: the starred cases remain with no starred-face anchor |
| round15 bound.cjs ALL 14 harnesses | PASS 14 of 14 (control) |

**Cut rules applied:** at most three mechanical criteria per order; no check compares values against a base snapshot; harness
changes are re-anchors only. **Battery:** comp-schedule and comp-iam DECLARED-NOT-APPLICABLE (static renders over fixtures). **The
issuer's close:** the merged DEV served on 5174, a signed-in read of BA, VLO and AMD on the Exec, Posture and Peers faces (the
analysis's census set), and the A3 read after B1.

**Rule 24:** (i) the analysis's four rows by subtraction: 3 orders + A3 placed (a) + the Posture source located (b). (ii) One write
set per chain. (iii) One intent per order. (iv) No order moves a served value: z-1 words, z-2 presents a served header value in a
second place, z-4 an instrument.


## v23 -- ROUND 23 (issuer, 2026-10-02 ~08:2xZ), over PRD v0.8 @7912f7aee2 (ADMITTED)

**Rectangle:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round22.md` @eee9380be7 section 3, rows 1-4 (rulings 1-6; msg 28303).
Deadline: drained by **11:30Z** and merged onto remote DEV, like `419ef41d`, so ONE candidate goes to Andrew; otherwise `419ef41d`
stays the candidate.
- **Cell ids:** `AV-zb-1` (row 1), `AV-zb-2` (row 2), `AV-zb-3` (row 3), `AV-zb-4` (row 4).
- **The issuer's placements:**
  - (a) **Row 3 is SERVED, so `AV-zb-3` drops.** The sentence "no declared IR domain for this name: a SERP not scoped to the
    company's own domain is not the contract's search" is written by `lib/research/management/enrich.py:536` (the CEO public
    profile `basis`, AMGT_RESAPP's lane). It is routed to `1.0.0_SA_CTO~Z` for RESAPP round 61 on B2's terms (ruling 3).
  - (b) **Row 1, the reader words are page-composed.** The absent reasons are served (`peers.csc_columns.absent[].reason`, R-1's
    words); the page's own words are the state phrase and the counts line. Under ruling 1 and round-21 ruling 1 (no page-side
    rewrite of a served string), the item reads one plain clause the PAGE composes from the column's label (e.g. "Shares
    outstanding is not reported for these peers"). The served reason rides `data-absent-column-reason` (kept by AV-z-1). The
    counts line and the column-head tips lose "comparison map", "registry" and "R-1" too.
  - (c) **Row 2, the served form and date** are the thesis bundle's `drafting_provenance` {accession, form, filing_date}, used only
    when its accession equals `management.source_accession`. Otherwise the page names the filing without a form or date it was
    not served for that filing.
  - (d) **Row 4:** `posture.harness.cjs` does its own read-only S3 fetch of the two posture objects (rl-7, Opal infra), so that
    order's bounds admit exactly that read. The plant knob (`POSTURE_HARNESS_PLANT=1`) is the harness's own, so it "grades
    something".
  - (e) **Chains from write sets:** ~71 `AV-zb-1` (Peers files + peers harnesses); ~72 `AV-zb-2` (`ExecManagementTab.tsx` + exec
    harnesses); ~73 `AV-zb-4` (`posture.harness.cjs`). They are file-disjoint. M = 3, N = 3, cap 3.
- **Portal base:** `419ef41d` (the round-22 candidate on remote DEV c4e0d744; src/pages/SecurityAnalysis is identical to DEV a730d8ce,
  where the checks were dry-run).
- **Frozen at the cut.**

| cell | row | what it builds | serves | writes | slot | risk |
|---|---|---|---|---|---|---|
| `AV-zb-1` | 1 | Peers absent-column items in reader words composed from the column label; the counts line and the tips without system terms | FWD-8 | `SA/tabs/PeersTab.tsx`, `SA/cscTable.ts`, peers harnesses (re-anchor) | ~71 | LOCAL |
| `AV-zb-2` | 2 | the Exec filing line names the form and filing date; the accession only in a data- attribute | FWD-11 | `SA/tabs/ExecManagementTab.tsx`, exec harnesses (re-anchor) | ~72 | LOCAL |
| `AV-zb-3` | 3 | dropped: served (placement a) | FWD-11 | -- | -- | -- |
| `AV-zb-4` | 4 | posture.harness repaired (current hook stubs) plus the plant knob | instrument (Z-W69-S1) | `SA/__harness__/posture.harness.cjs` | ~73 | LOCAL |

**Checks (`round23/checks/`, dry-run at DEV a730d8ce = 419ef41d for these paths):**

| check | base (as expected) |
|---|---|
| peerwords.cjs (AV-zb-1) | FAIL 2 of 3: per fixture, 19 terms (comparison map, factor code, row field, registry); RATIOS and THREE in reasons |
| accession.cjs (AV-zb-2) | FAIL 1 of 3: the accession is on the face; no 10-K or date; no attribute on the served branch |
| postureharness.cjs (AV-zb-4) | FAIL 0 of 3: TypeError useCollectedChatter; no CHECK lines |
| round15 bound.cjs ALL 14 + tsc | PASS (round-22 drain, and again on 419ef41d) |

**Rule 24:** (i) four rows by subtraction: 3 orders + row 3 placed (a). (ii) One write set per chain. (iii) One intent per order.
(iv) No order moves a served value: zb-1 and zb-2 are page words over served fields; zb-4 is an instrument.


## v24 -- ROUND 24 (issuer, 2026-10-02 ~09:1xZ) -- ONE DIRECT ACT

**Rectangle:** the CTO's ruling msg 28350 on row Z-S14 (review @dc22572ab2): "when the served Lusha reason is code-free, print it alone,
as one sentence." It folds in only if it is re-merged and walked by 11:30Z, and then the new hash goes to the CTO. Otherwise
41eeda55 ships as is. **Cell:** `AV-zc-1` (letter zc), DIRECT ACT, `<risk>LOCAL</risk>`, `ExecManagementTab.tsx` only: a code-free
served SKIPPED reason prints alone; a coded one keeps AV-z-1's plain sentence; the reason rides `data-lusha-reason` either way.
**Check:** `round24/checks/lushaline.cjs` (issuer): at base portal 41eeda55 it reads 2 of 3. **Chain:** ~74 alone, portal_ref 41eeda55.
**Close:** the issuer's merge onto the candidate branch, the battery, and one walk of VLO Exec. **Rule 24:** one row, one order; no
served value moves (the page prints a served string it already carries, without its own lead-in).


## v25 -- ROUND 25 (issuer, 2026-10-02 ~09:2xZ) -- the round-23 analysis's enrichment list, rows 1 and 3

**Rectangle:** `1.0.0_SA_CTO~Z`'s `ledger/ROUND_ANALYSIS.round23.md` @876dfcadb8 section 3 (msg 28356), rows 1-3. Row 2 (Z-S14) is
`AV-zc-1`, issued as round 24 @1549ca8bcc before the analysis landed. ONE ISSUER PER ROUND is keyed to the round
(to-pipeline-gate refused a second issuance into round 24), so rows 1 and 3 are round 25's one issuance. Deadline: re-merged onto the candidate and walked by 11:30Z, else the promote candidate stays `41eeda55`.
- **Cells:** `AV-zc-2` (row 1), `AV-zc-3` (row 3). Ruling 4 (the `surfaced_at` placeholders on W71-S1/S2) is the issuer's
  correction row Z-S16, because the row gate forbids an in-place edit. It carries no cell.
- **Placement (a), row 1:** R-1's served absent reasons are ONE global map: 11 distinct reasons over 12 columns, identical in all
  five fixtures. The page keeps a reader-words class table keyed by that reason (the column is a tie-break). Each item carries
  `data-absent-reason-class`; an unknown served reason renders `unmapped` with a generic plain clause.
- **Placement (b), row 3:** the "unfixed path" is the pre-AV-zb-4 predicate, which the harness keeps selectable
  (`POSTURE_HARNESS_LEGACY_PREDICATE=1`). The zero plant is `POSTURE_HARNESS_PLANT=zero`.
- **Chains:** ~75 `AV-zc-2` (PeersTab.tsx + peers harnesses); ~76 `AV-zc-3` (posture.harness.cjs). They are disjoint from each other
  and from ~74 (ExecManagementTab.tsx). Width: M = 3, N = 3, cap 3; portal_ref `41eeda55`.

| cell | row | what it builds | serves | writes | slot | risk |
|---|---|---|---|---|---|---|
| `AV-zc-2` | 1 | each absent column's reason in reader words, one clause per reason class, 0 unmapped | FWD-16, FWD-8 | `SA/tabs/PeersTab.tsx`, `SA/reasonWords.ts`, peers harnesses (re-anchor) | ~75 | LOCAL |
| `AV-zc-3` | 3 | the BABA check renamed to what it grades; zero plant + legacy predicate | instrument (v21) | `SA/__harness__/posture.harness.cjs` | ~76 | LOCAL |

**Checks (`round24/checks/`, written before the relabel; dry-run at base 41eeda55):** reasonclass.cjs FAIL 1 of 3 (the bare "not available" x60, no class
attribute); posturezero.cjs FAIL 0 of 3 (the old name printed, no zero plant, no legacy predicate).


## v26 -- ROUND 26 (issuer, 2026-10-02 ~09:5xZ) -- ONE DIRECT ACT

**Rectangle:** the issuer's own round-25 close walk 20261002T094604Z (VLO Peers): 5 of 12 absent columns read the generic `unmapped`
clause. RESAPP AMGT-ak-3 (B2, `lib/research/peers/csc_plain_reasons.py`) now SERVES the Cash, P/E 2027, Debt/Equity, 5-yr growth
EBIT and 5-yr growth FCF reasons with registry labels in place of codes, and AV-zc-2's table keys the old strings. This is a defect
in the round's own cell (the CTO's round-23 row 1 criterion is "0 classes left unmapped"), so the issuer repairs it inside its
decomposition. **Cell:** `AV-zd-1` (letter zd), DIRECT ACT, `<risk>LOCAL</risk>`, `reasonWords.ts` only: the five live strings join
the class table at their predecessors' classes. **Check:** `round26/checks/liveclass.cjs` (issuer): at base 7889655a it reads 1 of 3.
**Chain:** ~77 alone, portal_ref 7889655a. **Close:** the re-merge onto remote DEV 06bc6f85 (CTO msg 28379), the battery, and one walk
of VLO Peers. **Rule 24:** one row, one order; no served value moves.


## v27 -- ROUND 27 (issuer, 2026-10-02 ~14:3xZ) -- ONE DIRECT ACT

**Rectangle:** `1.0.0_SA_CTO~Z`'s `ledger/COMPLETION_GRADES.round26.json` @0c4c6d6368. FWD-2 is NOT_REALIZED, "A PAGE cell (DSGN)", on
CVO~Z ADJUDICATION_v26 @07446385f1 (spine: a NOT_REALIZED is the CTO's own round-N analysis for the next drain). FWD-7's NOT_REALIZED
is a PRODUCER cell (RESAPP management), not this decomposition's. The 11 NOT_EVALUATED rows are reads (CVO~Z v26 :40), not cells.
**Cell:** `AV-ze-1` (letter ze), DIRECT ACT, `<risk>LOCAL</risk>`, `PriceBars.tsx` + `ChatterBubbles.tsx` (+ `types.ts` for optional
chatter-row fields): every bar and bubble carries its SERVED identity one hover away (a native hover title). That means name, ticker,
asset class, sub-asset class, sector, the period figure and places moved, with a field not served said in words, never invented.
**Placement (a):** the served price rows carry every field. The served collected-chatter rows carry only `display_name`, so a
bubble prints what its row serves and says the rest is not served. Serving ticker, classification and places_moved on chatter rows
is a PRODUCER item (RESAPP), routed to the CTO. **Check:** `round27/checks/identity.cjs` (issuer): at base portal fa529337 (PROD's
tree) it reads 1 of 3. **Chain:** ~78 alone. **Rule 24:** one row, one order; no served value moves.


## v28 -- ROUND 28 (issuer, 2026-10-02 ~15:2xZ) -- ONE INSTRUMENT REPAIR CELL

**Rectangle:** `1.0.0_SA_CTO~Z` msg 28537 and the re-grade @6fe6735934 (16 REALIZED / 2 NOT_REALIZED / 5 NOT_EVALUATED / 1 RETIRED). It
names three instrument items: (i) the two stale clauses CVO~Z ADJUDICATION_v27 section 2 tables (fwd15 counts the consensus `th`;
fwd16 demands the served reason verbatim on the face); (ii) a contract fixture with an ABSENT model row, so FWD-15's footnote half
is read; (iii) the contract fixture's collected-chatter names (72 of 95 raw keys, the list.png rejection). The CTO asked for these as
an amendment to round 27. They are cut as round 28 because round 27 is issued, drained and closed (@8fba1b2e33), and
to-pipeline-gate refuses a second issuance into a round. The substance is unchanged.
**Cell:** `AV-zf-1`, DIRECT ACT, `<risk>LOCAL</risk>`, batch repair (`worker-light`). Files: `portal/scripts/ui-measure.mjs`,
`portal/scripts/ui-contract-check.mjs`, and the fixture `portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json`.
It touches no product file.
**Served input:** `round28/fixtures/served-names.collected-chatter.json`, made by the issuer with the served route's own resolver
(`monthly_chatter._display_names`), 95 of 95 resolved: 48 crosswalk, 25 model block header, 12 classification, 10 ticker; 0 raw keys.
**Checks (issuer), dry-run at portal 415f50db:** `round28/checks/render.cjs` 0 of 3 (fwd15 FAIL on spans with footnotes 0; fwd16
FAIL "12 listed column(s) carry no reason"; the planted predicate flags a healthy column) and `round28/checks/fixture.cjs` 1 of 3.
**Chain:** ~79 alone; base portal 415f50db (remote DEV), independent of round 27's df019dba. **Rule 24:** one row, one order.
FWD-20's PASS limb and FWD-15 are graded by CVO~Z at L9 on the amended instrument.


## v29 -- ROUND 29 (issuer, 2026-10-02 ~19:3xZ) -- THE UI/UX WALK FOLD (PRD v0.10 @175e4081b1)

**Rectangle:** PRD v0.10. The L4 notifier delivered it (CTO msg 28682). The ratified-text half is SIGNED by CVO~Z (current) and the brief half
is auto-accepted. The fold is CTO record `CTO_FOLD_SECURITY_ANALYSIS_UIUX_20261002.md` (rulings 1-10). Inputs: the 29 COO~D rows of the SAUX
register (`docs/briefs/amgt-security-analysis-ui-findings-20261002.json`); FWD-5, 12 and 22 amended; FWD-25 and 27 new. FWD-21 is cut for its
layout and fill limbs only.
**Base:** portal DEV ec65c5d6. Its SecurityAnalysis tree equals PROD dcdc89b1 (portal-v2.1.195).
**Write surfaces (disjoint; `types.ts` is owned by NO cell this round -- a cell extends a served row type locally by intersection):**

| cell | outcome(s) | SAUX rows | owned files (`portal/src/pages/SecurityAnalysis/` unless absolute) |
|---|---|---|---|
| `AV-zg-1` TIMELINE | FWD-5, FWD-27 (its lines) | 06, 07, 08, 09, 11, 13, 14; 30 ("day(s) rendered (no gap)"); 31 ("Social: no source measured", "MOST-DISCUSSED: NOT MEASURED") | `components/TimelinePanel.tsx`, `components/HeaderBrief.tsx`, new `components/timeline/**` |
| `AV-zg-2` OVERLAY HEADER | FWD-12 (header), FWD-27 (header) | 02, 03, 04, 05, 15; 30 ("Back to universe", "Export rich text (.md)"); 31 (card empty lines); 33/34 on the header | `components/SecurityOverlay.tsx`, `components/HeaderCards.tsx`, `components/IdentityLine.tsx`, `components/StatTile.tsx`, `components/PrintExportAction.tsx`, `constants.ts` |
| `AV-zg-3` LEAD PANEL + PRICE | FWD-12 (panel), FWD-22, FWD-26 (the price caption only), FWD-27 | 01, 20, 21, 36; 30 (page subtitle) | `components/LeadPanel.tsx`, `components/PriceBars.tsx`, `components/GenerationCaption.tsx`, `SecurityAnalysis.tsx` |
| `AV-zg-4` CHATTER COLLAGE | FWD-21 (collage, labels, fill) | 16, 17, 18 | `components/ChatterBubbles.tsx`, new `portal/src/lib/sentimentColor.ts`, `portal/src/components/market-performance/TopicCloud.tsx` (extraction: the import swap only) |
| `AV-zg-5` MODEL | FWD-25, FWD-27 (Model) | 23, 24, 26; 34 (the Model what-changed cap) | `tabs/ModelTab.tsx`, `modelSheet.ts`, `dateWords.ts`, new `components/model/**` |
| `AV-zg-6` TABS + ACCOUNT MENU | FWD-27 (tabs) | 32; 31 ("No profile (no match found)"); 30 ("in a union of", "no served drafted sentence ...", "held back uncited"); 33/34 on Peers; 35 | `tabs/ExecManagementTab.tsx`, `tabs/ThesisTab.tsx`, `components/ThesisDriverChart.tsx`, `tabs/PeersTab.tsx`, `portal/src/App.tsx` (the account menu: every page reads it) |

**Issuer rulings inside the decomposition:**
- (a) ONE money format: `<served currency code> <figure>` (e.g. "USD 196.80", "USD 187B"), never a `$` sign.
- (b) Every time prints in ET through `dateWords.ts` (owned by `AV-zg-5`); other cells call its helpers and do not format times.
- (c) A cell's read of a field not yet served (tone, voters, timeline markers of kind earnings_release) renders the designed empty state in words.
- (d) The sentiment ramp is TopicCloud's own `getSentimentColor`, extracted unchanged. TopicCloud's render is byte-equal before and after.

**FWD-26 presets: NOT cut** (EVENT-GATED: AMGT_RESAPP FWD-36 serving `?days=30|90|365`). The page cannot draw a rolling window from
calendar-month counts and never computes one (C-PRESENTATION-ONLY). The month cursor stays until the route serves windows; then a
round-30 cell cuts the presets. FWD-26's price caption is cut now, in `AV-zg-3` from the served `window_days`.
**Fan-out:** 6 chains, all independent (disjoint files), cap 8. **Risk:** LOCAL, all six. **Classes:** worker, all six.
**Battery ownership (issuer rulings at the cut, from the six check agents' reference runs):**
- Each portal harness clause pinning a pre-round-29 face is re-anchored by exactly ONE cell:
  - `shell` (5 clauses; both band counts become FWD-20 v0.9's `<= 1`): `AV-zg-2`;
  - `leadPanelPattern` (3 limbs) and `tabs` (`generation_captions_present`, `header_posture_line_matches_payload`): `AV-zg-3`;
  - `execPattern` (`absent_profile_cells`) and `drafting` (`held_uncited_line_present`): `AV-zg-6`;
  - `timelineFourStates` (the fill clause; not in the battery): `AV-zg-1`.
- AC3 is `round29/checks/battery29.sh`, the round 20-26 battery with a per-cell skip list naming items re-anchored by a sibling:
  `AV-zg-3` skips `shell`; `AV-zg-1` skips `tabs` and `namecard`. The issuer runs it with NO skip on the merged candidate.
- **Frozen shared exports:** StatTile's `FigureTooltip` / `formatStatValue` / `figureTooltipRows`; `constants.ts`'s `HEADER_CARD_DEFS` /
  `STAT_TILE_DEFS` / `IDENTITY_CURRENCY_MNEMONIC` / `StatTileFormat`; `dateWords`' `longDate` / `longStamp` / `chartTick` (`etStamp` added).
  `HeaderCards`' `HeaderCardDetail` stays exported.
- **Land together:** `AV-zg-1` and `AV-zg-2` (one timeline: HeaderBrief stops mounting it, and SecurityOverlay mounts it). The chatter
  ink goes navy (`AV-zg-4`) because the panel goes white (`AV-zg-3`).
- **Folded at the cut:** CTO msg 28729 (row Z-C-S41), the Exec caption naming only the served source, goes into `AV-zg-6`.
- **Checks:** 12 issuer checks (2 per cell), every one dry-run at portal dcdc89b1. Each FAILS at base (1-2 of 3-4 arms; PLANTED/CONTROL
  arms pass by design) and each reached full marks on its agent's scratch reference via `CHECK_SRC_OVERRIDE`.


## v30 -- ROUND 30 (issuer, 2026-10-03 ~01:0xZ) -- ONE UNIVERSE PER FACE + REPAIRS (PRD v0.13 @e398ee2294, ADMITTED)

**Rectangle:** round 29's close (@5e413e9b76) plus these sources:
- the CTO's round-29 review, msg 28820 (FWD-23, the hard-coded no-tone fill);
- RESAPP row Z-W208-S1 (CTO msg 28772; one universe per face);
- rows Z-W81-S1 and S3;
- COO~Z msg 28802 (feed url null);
- CTO msg 28833 (from CVO~Z v33): SAUX-15's first viewport, the "(movement is measured)" line, and What-changed rounding.
The "$2.9 billion" money item is ruled (b) by CTO msg 28836: served drafted prose stays as served, so no cell.
**Base:** portal e370eb7c, the CTO-approved round-29 candidate (review @a43b54dfee). Its DEV push waits on Andrew's word at MSTR~Z.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zh-1` ONE UNIVERSE | Z-W208-S1; FWD-27 (movement-basis words) | `components/LeadPanel.tsx`, `hooks/useLeadPanelApi.ts` | ~86 |
| `AV-zh-2` REPAIRS (batched) | FWD-23 token; Z-W81-S1 canonical Refresh; Z-W81-S3 render-check back control; Z-W212-S2 feed url null; FWD-27 rounding; SAUX-15 first viewport | `portal/src/lib/chartColors.ts` (one additive export), `components/ChatterBubbles.tsx`, `components/SecurityOverlay.tsx`, `__rendercheck__/renderCheck.tsx`, `components/HeaderBrief.tsx`, `components/model/WhatChangedPanel.tsx`, `components/TimelinePanel.tsx` | ~87 |

**Checks** (issuer, each FAILING at base e370eb7c):
- `round30/checks/universe/universe.cjs` 2/4 and `resolutionwords.cjs` 2/3;
- `round30/checks/repairs/chrome.cjs` 1/4 and `served.cjs` 1/3.
AC3 = `round29/checks/battery29.sh` with no skip.
**Issuer amendments to round-29 checks, landed with this issuance** (each 4/4 at base and FAILING its plants):
- `header/face.cjs`: a primary button's ink is judged against its own fill, and white ink is caught in every spelling;
- `timeline/dayopen.cjs`: an href only where a url is served.
**FWD-26 presets: NOT cut.** The deployed API ignores `?days=` (30/90/365 payloads are byte-identical; round30/fixtures/windows.*.json),
and RESAPP an-7 is signed @e1c310a414 but not deployed. The presets cut when COO~Z reports c9/c10 YES on deployed (CTO msg 28825).
**Fan-out:** 2 of 2 chains, disjoint files. **Risk:** LOCAL. **Rule 24:** one row per cell.

## v31 -- ROUND 31 (issuer, 2026-10-03 16:39Z) -- ROLLING WINDOWS + ONE NEWS ITEM AT REST (PRD v0.13 @e398ee2294, ADMITTED)

**Rectangle:** the round-30 close's open list (ROUND30_CLOSE.md section 4, @19b4ced775):
- FWD-26 presets. The routes now serve every window on the deployed opal-amgt-scoped-api (code KQSA62c3, COO~Z msgs 28860 and
  28874). Chatter `?days=30|90|365` serves window_days, window_start and window_end (plus window_note on 365). Trending/price
  `?days=30` serves 94 rows; `?days=90|365` serve 0 rows with window_reason.
- SAUX-15 first viewport: one news item at rest. The round-30 close walk measured the underline at y=917 (the served feed grew from 1
  to 69 items; CTO msg 28869).
**Base:** portal 2defab11, the round-30 candidate (it carries round 29). Its DEV push waits on Andrew's word at MSTR~Z.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zi-1` ROLLING WINDOWS | FWD-26 (SAUX-21, 27, 28); FWD-21 and FWD-22 read through the window | `api/endpoints/amgt-lead-panel.ts`, `hooks/useLeadPanelApi.ts`, `constants.ts`, `types.ts` (additive), `components/LeadPanel.tsx`, `components/ChatterBubbles.tsx`, `components/PriceBars.tsx`, two harnesses (follow-only) | ~88 |
| `AV-zi-2` ONE NEWS ITEM AT REST | SAUX-15 / FWD-12 / FWD-27 first viewport | `components/HeaderBrief.tsx` | ~89 |

**Checks** (issuer). Each FAILS at base 2defab11, and each PLANTED arm passes:
- `round31/checks/presets/presets.cjs` reads 1/4 and `windowread.cjs` reads 1/4 at base.
- `round31/checks/viewport/feedrest.cjs` reads 3/4 at base. A green arm with `FEED_OPEN_AT_REST = 1` planted through CHECK_SRC_OVERRIDE
  reads 4/4.
AC3 of each order is `round29/checks/battery29.sh` with no skip.
**Issuer amendment to a round-29 check, landed with this issuance:** `leadprice/leadface.cjs` AMENDMENT 1. FWD-26 retires the month
cursor, so the Chatter face hands ChatterBubbles no onMonthChange, and the face reads the served 30-day window fixture. At base the
amended check reads 2/3, failing only on the cursor clause.
**Kept on purpose:** ChatterBubbles keeps drawing a served month, with its cursor, for a caller that hands it `month` and
`onMonthChange`, because round-29 `collage.cjs` and `tone.cjs` and round-30 `chrome.cjs` render it that way. The page no longer does.
A later round may retire month mode together with those checks.
**Fan-out:** 2 of 2 chains, disjoint files. **Risk:** LOCAL. **Rule 24:** one row per cell.
**Workers:** the account hit its weekly model limit (resets 17:00Z), so the round-31 check agent died before writing. This session
made no call from ~01:57Z to ~16:2xZ. The issuer wrote the checks, and the two workers run on the Sonnet model override.
(Stamp correction: the issuance commit 812179b412 says "~02:2xZ" and this section first said "~03:0xZ". Both were
written without reading the clock; the issuance landed at 16:39Z.)

## v32 -- ROUND 32 (issuer, 2026-10-03 17:36Z) -- ONE DIRECT ACT: THE LEAD PANEL'S WORDS AT EVERY WINDOW (PRD v0.13 @e398ee2294)

**Rectangle:** the round-31 close's enrichment list (ROUND31_CLOSE.md section 4, @b742fd0687). The base is portal 76a15c1b, which the
CTO APPROVED (msg 28898, ledger @f722662a3f).

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zj-1` REPAIRS (batched, direct act) | FWD-27 one date format, no system words; FWD-26's faces | `components/LeadPanel.tsx`, `components/ChatterBubbles.tsx`, `components/GenerationCaption.tsx` | ~90 |

**What it repairs:**
- the Chatter footer prints `as_of` in words;
- an unserved Price window draws no "Source: ... payload" line;
- "this period" becomes "in this window";
- the stale `ground="band"` comment goes (row Z-W88-S1).

**Check:** `round32/checks/repairs/words32.cjs` reads 1/4 at base 76a15c1b (its arms 1-3 fail as expected; the 4 KEEP checks exit 0
there). AC2 = `round29/checks/battery29.sh` with no skip.
**Not cut:**
- Printing the served `window_note` (CTO note, msg 28898, not blocking): the note carries ISO dates, and FWD-27 wants words. The
  caption's composed "since <date>" says the same thing.
- A bubble hover's served `places_moved_reason` ISO date stays as served (C-PRESENTATION-ONLY, CTO ruling (b)).
**Fan-out:** 1 of 1. **Risk:** LOCAL. **Direct act:** one small cell (/dispatch Step 2).

## v32-A -- STEP 5 ON THE PRD AT d5bbef0fb6 (issuer, 2026-10-03 20:01Z; v0.13, CVO re-signed @e082e847ee, notifier msg 28980)

**What changed:** under the Andrew-direct 2026-10-03 ~18:xxZ deletion, the PRD lost the v0.12 clause on FWD-5's word-cloud limb
(record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261003_18xxZ_DELETE_AGENT_TOS_CONTEXT_AND_UNAUTHORIZED_GATES.md`).
FWD-5's ACCEPT still names "a word cloud from its own coverage".
**Ruling: no cell is cut this step.**
- The limb has no served input. 0 of 437 captured payloads (every round fixture and the 10-02 served re-read) carry a word-cloud or
  term-count field. The only `terms` field is the thesis pillars' labels.
- The input would come from an upstream producer: HARVST/RESAPP processing harvested coverage text into term counts. Andrew's
  standing word (2026-10-03 ~17:xxZ, record `ANDREW_DIRECT_20261003_17xxZ_RELEASE_ALL_QUARANTINE_NO_DATA_OPS_CHANGES_WITHOUT_DIRECTIVE.md`)
  is that agents do not adjust data-engineering operations without his explicit directive, and that further data collection is
  discussed internally after review.
- Separately, the CTO's grading ruling (@5cd2d798d8) cuts no round 33 before f9c6fa73 lands.
A DSGN cell for the word cloud is cut when a route serves the term counts.

## v32-B -- STEP 5 ON PRD v0.14 @548a6971fe (issuer, 2026-10-03 20:20Z; CVO re-signed @b66b480942, notifier msg 28993)

v0.14 names FWD-5's word-cloud input: `word_cloud` on the timeline payload, from AMGT_RESAPP FWD-39 (RESAPP v0.36). It is sized by the
served count, and an empty served list renders its served reason. The page counts nothing. **Ruling: no cell is cut this step.**
RESAPP FWD-39 is a QUALIFIED WAIT on Andrew's explicit word (CTO msg 28991), so no route serves `word_cloud` yet, and round 33 stays
held on the f9c6fa73 landing (@5cd2d798d8). The cell is cut, against the served shape, when a route serves the field (v32-A).

## v33 -- ROUND 33 (issuer, 2026-10-03 20:51Z) -- ONE DIRECT ACT: DEV CI GREEN AGAIN (PRD v0.14 @548a6971fe)

**Rectangle:** portal DEV 49c6e94a0f, the rounds 29-32 landing, is RED in CI ("Build & Validate" 37152260084, step "Run ESLint", 1
error: WhatChangedPanel.tsx:395 `@typescript-eslint/no-empty-object-type` on `export interface WhatChangedPanelProps extends
PairContext {}`, from round 29 AV-zg-5, MSTR~Z msg 29015). The CTO asks for the fix as a candidate (msg 29017). A red DEV blocks the
next PROD promote, and the round-32 grades wait for a green deploy.
**Base:** portal DEV 49c6e94a0f.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zk-1` ESLINT GREEN (direct act) | CI green on DEV; FWD-25 (What changed) unchanged in behaviour | `components/model/WhatChangedPanel.tsx` (one line) | ~91 |

**Check:** `round29/checks/battery29.sh` AMENDMENT 1 (this issuance) adds the CI's ESLint step, errors only, over this project's
paths. It reads FAIL at base 49c6e94a0f (eslint rc=1, 1 error). Green arm: the one-line fix piped to eslint --stdin reads rc=0.
AC2 = round29 model/whatchanged.cjs and model/etwords.cjs (they read WhatChangedPanel.tsx).
**Gate fix (MSTR~Z msg 29018, the issuer's call: adopted):** battery29 now runs ESLint, so "ALL PASS" includes the CI lint gate.
**Fan-out:** 1 of 1. **Risk:** LOCAL. **Direct act.**

## v34 -- ROUND 34 (issuer, 2026-10-04 00:48Z) -- THE GAP WALK + ONE REPAIR CELL (PRD v0.15 @237d5d742f, ADMITTED)

**Rectangle:** the CTO's round-33 analysis section 3 (`ledger/ROUND_ANALYSIS.round33.md` @ff31355b93), and the round-32 grades on PROD
dbd29c6320: 10 REALIZED, 3 NOT_REALIZED (FWD-5, 21, 27), 13 NOT_EVALUATED, 1 RETIRED.
**Base:** portal PROD dbd29c6320, the served build.

**1. The gap walk: the issuer's real run, not a cell.** `round34/walk/gapread.mjs` is an issuer instrument built on
`served-reread-20261002/servedread.mjs`, using the walk.mjs lease. It ran on a worktree build of PROD dbd29c6320 at 5174 against the
live API: read-20261004T001928Z, 00:19-00:30Z, DISARMED with login REFUSED afterwards. Result: 20 reads, **16 PASS, 3 FAIL, 1 ERROR**
(`round34/walk/GAP_READ.md`).
- PASS:
  - tabs on BA, VLO and AMD with the day dialog closed (5 of 5 each);
  - ROG SW's CHF header;
  - ASML NA's officers (filing empty, 7 served from the Bloomberg fallback);
  - the overlay census, 0 "not served" on 19 carried fields per name;
  - hovers: full names on every shortened label at 30/90/365, "no clear tone", the timeline tooltip, and bubble/bar identity;
  - Escape closing the account menu.
- FAIL: the display-name census. The Peers subject row prints the served `peers.subject.name` ("BOEING CO/THE") while every other
  surface prints `display_name`.
- ERROR: FWD-24's positive control. None of the 3 names lacks a checked field; owed on a sparser name.
The six-state ui-smoke capture (FWD-19/20) is not yet run; it is owed.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zl-1` REPAIRS (batched) | FWD-21 labels; FWD-27: header move window, What-changed precision, axis ink, one display name in Peers | `components/ChatterBubbles.tsx`, `components/SecurityOverlay.tsx`, `components/model/WhatChangedPanel.tsx`, `components/TimelinePanel.tsx`, `cscTable.ts`, `tabs/PeersTab.tsx` | ~93 |

**Checks** (each FAILS at base dbd29c6320 with its PLANTED arm passing; each green arm reads N of N through CHECK_SRC_OVERRIDE):
- `round34/checks/collage/labels34.cjs` reads 2/4. At base it finds 34 collisions over 30/90/365, and 30 shortened labels without a
  reachable `<title>`.
- `round34/checks/repairs/repairs34.cjs` reads 1/4: the move has no window, 11 of 13 changes print at raw precision, and the axis is
  #A8B0C0 at 2.18:1.
- `round34/checks/names/peername34.cjs` reads 3/4. Its fixtures are `round34/fixtures/{overlay,peers}.{BA,VLO}_US_Equity.json`,
  captured read-only on code FcVBPafw.
AC3 = `round29/checks/battery29.sh` with no skip (it now runs the CI ESLint step).
**Issuer ruling inside this decomposition:** the Peers subject name joins the repair cell. The CTO's analysis expected RESAPP's
title-case deploy to settle the name limb, but today's served `peers.subject.name` is still the raw vendor form. Which served name
the page prints for its own subject is a presentation choice; nothing is rewritten.
**Not cut:**
- FWD-5's word cloud: when RESAPP ap-4 serves FWD-39.
- SAUX-25 provenance lines: RESAPP FWD-38(d), at COO~Z.
- Officers for the 84 of 95 names whose M-1 management object has not landed (RESAPP upstream; observation sent to the CTO).
**Fan-out:** 1 of 1. **Risk:** LOCAL.

## v35 -- ROUND 35 (issuer, 2026-10-04 ~20:5xZ) -- THREE CELLS: WHAT CHANGED IN WORDS, NO SYSTEM WORD, THE WORD CLOUD (PRD v0.15 @237d5d742f, ADMITTED)

**Rectangle:** the round-34 enrichment list, `round34/ROUND34_CLOSE.md` section 4 (@a408efb24a), as the CTO's resume order names it
(`1.0.0_SA_CTO~Z` msg 29179: "2.0.0_SA_COO~D: round 35"). The CTO's review of 055ba370 (@720f78e6f6) reopens FWD-12, 18, 21, 23, 25,
26 and 27 for grading on the served build; that grading waits on the 055ba370 DEV push (Andrew's word, MSTR~Z's act).
**Base:** portal 055ba370 (the CTO-approved round-34 candidate, branch `dsgn-r34-onto-dev`, LOCAL). Round 35 stacks on it. Origin
DEV is now 7b053135 (7 laptop commits outside SecurityAnalysis, MSTR~Z msg 29215), and it is merged at the close.
**Restart note:** the site-Z crash (18:58Z) lost this round's first cut; its two authoring agents left nothing on disk. Everything
here was re-made after the relaunch.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zm-1` WHAT CHANGED IN WORDS | FWD-25, FWD-27 | `components/model/WhatChangedPanel.tsx` | ~94 |
| `AV-zm-2` NO SYSTEM WORD ON THE FACE | FWD-27 (and FWD-24's designed empty state) | `components/{GenerationCaption,LeadPanel,SecurityOverlay,StatTile,ThesisCards}.tsx`, `tabs/{ExecManagement,Posture,Thesis}Tab.tsx`, `readCompleteness.ts` | ~95 (worker-light) |
| `AV-zm-3` THE TIMELINE'S WORD CLOUD | FWD-5 (v0.14) | `components/TimelinePanel.tsx`, NEW `components/TimelineWordCloud.tsx` | ~96 |

**Served input:** RESAPP AMGT-ap-4 deployed `word_cloud` on the timeline range route (FcVBPafw, closed ~00:5xZ). The issuer's
read-only capture at this cut, `round35/fixtures/capture_timeline.py`, reads 40 terms on 6 of 6 names (BA, VLO, AMD, MSFT, ASML NA,
ROG SW; window 2026-01-01..2026-10-03). No name serves an empty list, so the empty and absent arms plant the producer's own reasons
(`lib/research/api/scoped_amgt.py` `_word_cloud_block`). The What-changed fixtures `round35/fixtures/{compare,thesis,versions}.BA_US_Equity.json`
were captured read-only on FcVBPafw at 03:08Z.

**Checks** (each dry-run by the issuer at base 055ba370; each FAILS with its PLANTED arm passing, and each green arm reads N of N
through CHECK_SRC_OVERRIDE with a scratch reference fix outside the repo):
- `round35/checks/changed/changed35.cjs` reads 2/5: 32 of 37 BA rows unnamed (all consensus forecasts); 11 mnemonics share the fixed
  phrase; 6 equal-print rows print a move ("0.0%" -> "0.0%" prints "-100.0%").
- `round35/checks/words/payload35.cjs` reads 2/4: 0 of 18 empty-state renders clean; 14 visible literals say "payload" in 40 files.
  Its census sets aside a `data-*` attribute value (`RankedChart.tsx:156` `NO_PAYLOAD`, a machine hook never seen). **Issuer ruling:
  accepted.** The rule is about text a person reads.
- `round35/checks/cloud/cloud35.cjs` reads 2/5: no `[data-word-cloud]` on BA, VLO or AMD. The negative control (TimelinePanel
  overridden without the new component) reads 1/5.
AC2 of every cell = `round29/checks/battery29.sh` with no skip (ESLint included).

**Not cut this round:**
- **FWD-20 instrument re-anchor** (enrichment item 1: the light-family band clause `bandContainersTopLevel <= 1` plus
  `lightOnDark == 0`, the price face's top-10 rest count, the windowed chatter fixture). Its check
  (`round35/checks/instrument/instrument35.cjs`, which builds and drives the instrument) has no base reading yet. A cell is never
  cut against an undry-run check, and a round has ONE issuance. It is cut as round 36 when its check reads at base.
- SAUX-25's provenance lines: RESAPP FWD-38(d), at COO~Z.
- Officers for the names with no M-1 management object (RESAPP upstream).
**Chain:** three independent chains, each from 055ba370, with disjoint file sets. **Fan-out:** 3 of 3 chains, cap 8. **Risk:** LOCAL.
**Rule 24:** one row, one order per cell.

## v36 -- ROUND 36 (issuer, 2026-10-04 ~22:3xZ) -- TWO CELLS: THE RENDER INSTRUMENT GRADES THE REDESIGN; THE BATCHED REPAIR (PRD v0.15 @237d5d742f, ADMITTED)

**Rectangle:** `round35/ROUND35_CLOSE.md` section 4, which the CTO's review of d60a0f90 confirms (@98209ce86a, msg 29256 condition 4:
"Your round-36 list stands"). **Base:** portal 35a723bf, now on DEV (MSTR~Z on Andrew's word, CI 37237977735 success, msg 29263/29269).

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zn-1` INSTRUMENT RE-ANCHOR | FWD-20 | `portal/scripts/ui-contract-check.mjs`, `portal/scripts/ui-measure.mjs`, `portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json` | ~97 |
| `AV-zn-2` REPAIRS (batched) | FWD-20 (list-state sizes and radii), FWD-5 (tooltip headline while loading), FWD-27 (no zero move) | `components/ChatterBubbles.tsx`, `components/TimelinePanel.tsx`, `components/model/WhatChangedPanel.tsx` | ~98 |

**Check, AV-zn-2:** `round36/checks/repairs/repairs36.cjs` (+ `_render36.cjs`). At base 35a723bf it reads 2 of 5: Chatter 30/90/365D carry
39/47/51 page-owned SVG label sizes 8-10.5 px and one 5px legend radius (ChatterBubbles.tsx :264-269, :359, :401, :653); while the day
read is pending, BA 09-28/09-29/09-08 print the coverage event's lead headline under "Strongest headline"; 3 rows print "-0.00%" /
"+0.00%". KEEP 6 of 6, PLANTED 9 of 9. Green 5 of 5 through CHECK_SRC_OVERRIDE (issuer re-run). Shared `PanelContent.tsx`
`rounded-b-lg` is reported, not graded; RankedChart.tsx's 10px ticks are not mounted on the list state (census only, not cut).
**Check, AV-zn-1:** `round35/checks/instrument/instrument35.cjs` (committed @9e5820652c). At base 35a723bf it reads 0 of 4 in 948 s: arm 1 finds
no re-anchored band clause and 0 chatter bubbles on the monthly fixture; arm 2 finds 8fa7abde fails no re-anchored clause; arm 3 tells
no plant apart; arm 4 counts 12 stale darkContainers/bandIsIdentityHeader FAILs. Green arm: 4 of 4 on a scratch reference re-anchor at
the round-35 cut. AC2 = battery29 with no skip. It touches no product file.
**Sequencing (CTO msg 29279):** AMGT_CORPUS round 36 has a candidate on `tabs/ModelTab.tsx` and `modelSheet.ts`. Neither cell
touches either file (checked against both `<paths>` lists).
**Fan-out:** 2 of 2 chains, cap 8 (disjoint files; both from 35a723bf). **Risk:** LOCAL.

## v37 -- ROUND 37 (issuer, 2026-10-05 ~04:3xZ) -- ONE BATCHED REPAIR CELL + THE READS (PRD v0.15 @237d5d742f, ADMITTED)

**Rectangle:** the CTO's ENRICHMENT LIST @9b2ed08fe2 (`ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND36.md`, msg 29466): (1) FWD-21 365D
edge labels inside the plot with no collision; (2) FWD-8 no cross-currency average ever, a mixed group says so; (3) FWD-10 the no-call
state carries its as-of date; (4) reads of FWD-5/11/19 on the served build. Grades @c706123ec2, countersigned @d0fd16fba5.
**Base:** portal DEV 56b71adb (carries AMGT_CORPUS's ModelTab.tsx/modelSheet.ts; this round touches neither).

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zo-1` REPAIRS (batched) | FWD-21, FWD-8, FWD-10 | `components/ChatterBubbles.tsx`, `cscTable.ts`, `tabs/PeersTab.tsx`, `components/LeadPanel.tsx`, `components/SecurityOverlay.tsx`, `tabs/PostureTab.tsx` | ~99 |

**Check:** `round37/checks/repairs/repairs37.cjs` (+ `_render37.cjs`, `_collage37.cjs`), fixtures `round37/fixtures/` captured read-only on
the deployed scoped API (`capture_r37.py`: chatter 30/90/365; MSFT and AMD peers/overlay/thesis). At base 56b71adb it reads 2 of 5: the
static render reproduces the live 365D offenders ("Kim...", "Synopsys Inc") plus 90D "IDEXX Laboratories Inc" -- each straddles its OWN
bubble's outline, the case labels34 skipped; 18 currency faults (MSFT "Average 158,633 (n=12)"); 9 undated no-call renders. KEEP 8/8,
PLANTED pass. Green 5 of 5 (issuer re-run).
**Issuer ruling inside the decomposition (FWD-8):** the served peers carry no member price currency (`cap_currency` only). The page reads
"never a cross-currency average" as no Price summary until a currency is served; the producer gap goes to the CTO for RESAPP at the close.
**Item 4 is not a cell:** the reads of FWD-5/11/19 are the issuer's real run at the close, `round37/walk/reads37.mjs` (FWD-5 marker press
and day dialog; FWD-11 side-by-side captures of /market, /positioning, /philosophy; FWD-19 loading/error on the timeline, header and
What changed by intercepting one GET, and PanelNoPermission on its real route).
**Fan-out:** 1 of 1 chains, cap 8. **Risk:** LOCAL.

## v38 -- ROUND 38 (issuer, 2026-10-05 ~07:3xZ) -- ONE BATCHED CELL: THE SHARED FOOTERS, THE END LINE, WHAT CHANGED'S STATES (PRD v0.15 @237d5d742f, ADMITTED)

**Rectangle:** the CTO's list @0a865d7e8f (`ledger/CTO_LIST_ROUND38.md`, msg 29501): (1) FWD-19 What changed uses PanelLoading and
PanelError; (2) FWD-11 every card ends in the shared time|source footer from served fields only, and the page ends with the shared
"End of Security Analysis. Data as of <served date>." line; (3) the FWD-11 re-read on the served candidate. FWD-11 was judged NOT_REALIZED
for the footers and the end line, not for the card family (FWD-12 governs that).
**Base:** portal 85e24287, the CTO-approved round-37 candidate (7f679aee on DEV 3e1aa46f); its DEV push is held for Andrew's word, so
round 38 stacks on it as round 35 did on 055ba370.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zp-1` FOOTERS + END LINE + STATES (batched) | FWD-11, FWD-19 | `SecurityAnalysis.tsx`, NEW `components/CardFooter.tsx`, `components/model/WhatChangedPanel.tsx`, `components/SecurityOverlay.tsx`, `components/LeadPanel.tsx`, `tabs/{Thesis,ExecManagement,Peers,Posture,Model}Tab.tsx`, `src/ui/components/panels/PanelFooter.tsx` | ~100 |

Items 1 and 2 share What changed (its card needs the footer too), so they are one cell.
**Check:** `round38/checks/repairs/repairs38.cjs` (+ `_render38.cjs`, `_cards38.cjs`; served fixtures from rounds 35 and 37). At base
85e24287 it reads 2 of 5 (issuer re-run): What changed shows no designed states and a skeleton on a 500 (incl. the remount path); 14
cards carry no footer and the Lead Panel prints a hand-rolled "date | Source" line; PageEnd renders 0 times. KEEP 9/9, PLANTED 17/17.
Green 5 of 5 through CHECK_SRC_OVERRIDE. A per-card census of served time/source fields is in the check (`_cards38.cjs`); a card with
neither prints no footer line (the timeline serves no source).
**Issuer rulings inside the decomposition:**
- `tabs/ModelTab.tsx`: one import + one footer line inside its own Panel. AMGT_CORPUS's ModelTab candidate has landed on DEV, and
  COO~X confirms nothing is in flight (msg 29519).
- `src/ui/components/panels/PanelFooter.tsx` (shared estate): ONE optional prop (a light ground), default unchanged, so every other page
  is unchanged. It is needed because the band-painted footer fails the light-card checks. Flagged to the CTO in the issuance; the CTO
  reviews the product-file candidate.
**Item 3 is not a cell:** the FWD-11 re-read is the issuer's real run at the close (round37/walk/reads37.mjs fwd11-side-by-side).
**Fan-out:** 1 of 1 chains, cap 8. **Risk:** LOCAL.

## v39 -- ROUND 39 (issuer, 2026-10-05 ~13:4xZ) -- ONE DIRECT ACT: AN UNKNOWN SOURCE READS THE FIXED PHRASE (PRD v0.15)

**Rectangle:** the CTO's review of round 38 (@2e225582da, msg 29549): APPROVED pending ONE required fix -- `CardFooter.tsx:95` prints a
de-punctuated raw code for an unknown source; it must return `UNNAMED_SOURCE_WORDS`, with one repairs38 arm on an unknown long source.
Andrew's word for the round 37+38 DEV push follows this fix (record 121b7b016e, msg 29560).
**Base:** portal `dsgn-r38-zp1` (75f9f477, the round-38 cell branch); the candidate is rebuilt at the close on current DEV.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zq-1` UNKNOWN SOURCE (direct act) | FWD-11 | `components/CardFooter.tsx` (one line) | ~101 (worker-light) |

**Check:** `round38/checks/repairs/repairs38.cjs` AMENDMENT 2 (arm 4, "AN UNKNOWN SOURCE READS THE FIXED PHRASE"; renders the real
CardFooter through `_render38.cjs`'s new footer mode). At the round-38 candidate 5fe58e89 it reads 5 of 6 (arm 4 FAIL); with the one-line
reference fix, 6 of 6. AC2 = battery29 with no skip.
**Not cut (the CTO's next list):** row S3 (the end line's "5:00p ET" after a bare served day) and reads37's What-changed scope selector.
**Fan-out:** 1 of 1. **Risk:** LOCAL. **Direct act.**

## v40 -- ROUND 40 (issuer, 2026-10-05 ~15:1xZ) -- ONE DIRECT ACT: SECURITY ANALYSIS OPEN TO EVERY OPAL EMPLOYEE

**Rectangle:** Andrew-direct 2026-10-05 ~15:0xZ at this seat (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261005_150xZ_SECURITY_ANALYSIS_ALL_OPAL_EMPLOYEES_REQUIREINTERNAL_LEADPANEL_LOAD_TO_COO_Z.md`):
"It should be visible for all Opal Employees" / "should not require admin access to see" / "requireInternal is the correct approac".
**Base:** portal DEV 71097b53 (r39 pushed first, MSTR~Z msg 29616 answered (a), msg 29619).

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zr-1` ACCESS (direct act) | the page gate (Andrew-direct) | `portal/src/App.tsx` (nav entry + 2 routes + their comments) | ~102 (worker-light) |

**Check:** `round40/checks/access/access40.cjs` (static read of App.tsx, ProtectedRoute.tsx, firmAccess.ts). At 71097b53 it reads 2 of 4: nav
requiresDev + requiresAdmin with no internal tier; both routes requireDev requireAdmin. KEEP (Investor Reporting unchanged; requireInternal is
firmId === 'opal-capital'; no partner allowlist names the path) and PLANTED pass. Green 4 of 4 on a scratch copy with the edit.
**Backend, measured:** the scoped AMGT API admits on the edge-injected firm identity only (scoped_amgt.py `_firm_id`); no Dev/admin role
check, so no backend change. **Not cut:** the Lead Panel's slow load (Andrew: to COO~Z; message sent 15:03Z).
**Fan-out:** 1 of 1. **Risk:** LOCAL. **Direct act.**

## v41 -- ROUND 41 (issuer, 2026-10-05 ~15:4xZ) -- ONE ISSUER ACT: THE COMPLETION GRADING WALK ON DEV e6ab82ad

**Rectangle:** `ledger/CTO_LIST_ROUND41.md` @9a476b6ee0 (msg 29654): (1) grade FWD-1..27 on DEV e6ab82ad against RESAPP GS//XHnV, each on
its DONE WHEN, into `COMPLETION_GRADES.round41.json` for the CTO's countersign; (2) re-read FWD-4 (ROG SW + a US name), FWD-7 (AMD, ASML),
FWD-8 (a mixed-currency name) where the producer moved. **Base:** portal DEV e6ab82ad (CI 37332239294 success).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zs-G` GRADING (issuer act, no product file) | FWD-1..27 | `deliverables/2.0.0_SA_COO~D/round41/` | 2.0.0_SA_COO~D (as round 36, per CTO ruling msg 29406) |

**Instruments, unchanged and already proven able to fail:** `round35/walk/closewalk35.mjs --no-officer "ASML NA" --names "BA US,VLO US,AMD
US,MSFT US"` (FWD-2/4/5/6-11/21/24/27, ROG SW non-USD header, ASML no-filing roster, AMD and MSFT tabs); `round37/walk/reads37.mjs
--names "BA US,AMD US"` (FWD-5 markers + own-first, FWD-11 side-by-side, FWD-19 panels; its no-permission arm RETIRED in round 40);
`round35/checks/instrument/instrument35.cjs` (FWD-12..20 states sweep). Live: localhost:5174 = C:/tmp/wk-dsgn-amgtv1-92/portal at e6ab82ad
(dev:live, live API). Walker ARM/DISARMED through MSTR~Z.
**Fan-out:** 0 worker chains (no product change). **Risk:** SERVED read (no write). **Not cut:** the Lead Panel load (COO~Z).

## v42 -- ROUND 42 (issuer, 2026-10-05 ~16:4xZ) -- ONE BATCHED REPAIR CELL + ONE ISSUER READ

**Rectangle:** `ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND41.md` @f5d6919117, ROUND 42 items 1-3 (page), and item 4 as Andrew re-set it
(record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261005_163xZ_SECURITY_ANALYSIS_NO_NO_PERMISSION_SCREEN_SIDEBAR_INVISIBLE_FOR_NON_OPAL.md`;
CTO msgs 29703, 29704): no "no permission" screen; ONE read that a non-Opal viewer sees no Security Analysis sidebar item; no route,
redirect or backend work. **Base:** portal DEV e6ab82ad. **Parity hold** (MSTR~Z 29688): cut on branch `wk-DSGN_AMGTV1-r42-issue`.

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zt-1` REPAIRS (batched) | FWD-4 (served reason in place), FWD-13 (full value in the tooltip), FWD-27 (Exec plain words) | `components/HeaderCards.tsx`, `tabs/ExecManagementTab.tsx` (+ a harness line only if it asserts the old Exec text) | ~103 (worker-light) |
| `AV-zt-R` SIDEBAR READ (issuer act) | FWD-19 limb as re-set by Andrew | none (a walk read on the candidate) | 2.0.0_SA_COO~D |

**Check, AV-zt-1:** `round42/checks/r42/r42.cjs` (the REAL HeaderCards rendered through round15/_load.cjs; ExecManagementTab read as source).
At base e6ab82ad it reads 2 of 5: ROG SW-shaped bundle 3 tiles with none of the 4 served reasons; the tooltip lacks the full values; the Exec
"yet:" run-on. KEEP and PLANTED pass. Green 5 of 5 on scratch reference edits (CHECK_SRC_OVERRIDE, issuer run).
**Fan-out:** 1 of 1 worker chains, cap 8. **Risk:** LOCAL. **Then:** candidate -> CTO review -> DEV push on Andrew's word; PROD held.

## v43 -- ROUND 43 (issuer, 2026-10-06 ~03:5xZ, by hand, no loop) -- ONE BATCHED REPAIR: PEER TICKERS + PLAIN NAMES

**Rectangle:** CTO countersign + list @0bcdb77515 (msg 29884): FWD-8 and FWD-27 NOT_REALIZED page-side. The producer (deployed
2lUlZomo) serves `display_name`, `security_key` and `ticker_reason`, and the page reads none of them (census
`round42/fwd8-27-census/` @662434b2cf). **Base:** portal DEV 4fa0312e (no SecurityAnalysis change since PROD ce6f0721).

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zu-1` REPAIRS (batched) | FWD-8 (no bare number as a peer ticker), FWD-27 (display_name at every served-name site) | `cscTable.ts`, `components/PriceBars.tsx`, `components/RankedList.tsx`, `postureCites.ts` (+ `types.ts` declarations) | ~104 (worker-light) |

**Check:** `round43/checks/r43/r43.cjs` on fixtures captured from the deployed API (`round43/fixtures/`). At base it reads 2 of 5 (bare
numbers 688910/677172/677381/645026; SYNOPSYS INC, ADOBE INC and CADENCE DESIGN SYS on the price face; three name-first sites). KEEP and
PLANTED pass. Green 5 of 5 on scratch reference edits (CHECK_SRC_OVERRIDE, issuer run).
**Fan-out:** 1 of 1. **Risk:** LOCAL. **Then:** a :5174 walk, CTO review, and the DEV push and PROD on Andrew's word.

## v44 -- ROUND 44 (issuer, 2026-10-06 ~06:1xZ, by hand, no loop) -- ONE CELL: DRIVER PASSAGE + SEGMENT BREAKDOWN

**Rectangle:** AMGT_RESAPP `ledger/ROUND_ANALYSIS.round73.md` @cf0d03deb2 item 1 (msg 29921): (a) FWD-18, a driver-chart click opens the
served `passage_text` with its cite; (b) FWD-1, the served `segment_breakdown` drawn with its cites, or its reason. **Base:** the round-43
candidate (portal c123c5a0), so rounds 43 and 44 reach Andrew as ONE DEV push.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zv-1` | FWD-18 (a), FWD-1 (b) | `components/ThesisDriverChart.tsx`, NEW `components/SegmentBreakdown.tsx`, `tabs/ThesisTab.tsx`, `types.ts` | ~105 (worker) |

**Check:** `round44/checks/r44/r44.cjs` on fixtures captured from deployed satkY3HX (`round44/fixtures/thesis.{BA,MSFT}`). At base DEV
b0051830 it reads 1 of 5: BA's point prints "not shown on this page"; there is no SegmentBreakdown; ThesisTab mounts none. PLANTED passes.
Green 5 of 5 on scratch reference edits.
**Fan-out:** 1 of 1. **Risk:** LOCAL. **Then:** a :5174 walk, CTO review, and ONE DEV push (43 + 44) on Andrew's word.

## v45 -- ROUND 45 (issuer, 2026-10-07 ~02:0xZ, by hand, no loop) -- TWO CELLS: THE TOP BAND + INPUT PROVENANCE; THE FWD-18 PAGE REPAIRS

**Rectangle:** AMGT_RESAPP `ledger/ROUND_ANALYSIS.round75.md` @326aea63b3 rulings 2-3 (the "DSGN round 45" line: the top-of-page band and the
provenance panel, drawn from round 76's served fields), `ROUND_ANALYSIS.round76.md` @c8bbeeac10 ruling 6 (the FWD-18 page repairs) and its
ADDENDUM 1 item 4 @a7b2c3e0ba (CTO msg 30491: round 45 carries the repairs and the removal of the /refresh control). **Base:** portal DEV
34803ef6 (= PROD v2.1.202 ab3191d0's content), with RESAPP round 76 deployed as OVpDhfwD.

| cell | serves | owned files | worker |
|---|---|---|---|
| `AV-zw-1` | RESAPP FWD-16 (news half), FWD-12 (provenance half), PRD v0.41 (no re-run button) | NEW `components/TopBand.tsx`, NEW `components/InputProvenance.tsx`, NEW `topBandTypes.ts`, `SecurityAnalysis.tsx`, `hooks/useLeadPanelApi.ts`, `components/SecurityOverlay.tsx`, `__harness__/posture.harness.cjs` | ~106 (worker) |
| `AV-zw-2` | RESAPP FWD-18 and FWD-1 on the page (ruling 6) | `components/ThesisDriverChart.tsx`, NEW `components/PassageTable.tsx`, `components/SegmentBreakdown.tsx`, `types.ts`, the `__harness__/` files naming `data-driver-chart` or `data-segment` | ~107 (worker) |

**Chains:** 2, with no shared product file (`AV-zw-1` declares its types in `topBandTypes.ts` because `AV-zw-2` owns `types.ts`), so both
cells run at once. **Not in this round:** `portal/src/api/endpoints/amgt-lead-panel.ts` and `pages/Freshness/` (RESAPP ba-4 writes them,
COO~Z msg 30485); row DSGN_AMGTV1-Z-S21 (case value and currency attributes on `ModelTab.tsx`) waits for the next cut.

**Checks:** `round45/checks/r45/r45.cjs` on fixtures captured from deployed OVpDhfwD (`round45/fixtures/overlay.{BA,MSFT}`): 1 of 5 at base
DEV 34803ef6, 5 of 5 on scratch reference components. Its item arm PLANTS two items, because 0 of 95 covered names served a news item at
the cut. `AV-zw-2` is graded by `2.0.0_SA_COO~Z`'s `round77/checks/r77_ba5.py` (@7daf7c5677): AC1, AC2 and AC3 read NO at base, controls passing.
**Fan-out:** 2 of 2 (`fanout: 2`). **Risk:** LOCAL. **Then:** battery29 on the combined candidate, a :5174 walk, CTO review from the
renders, and ONE DEV push on Andrew's word.

## v46 -- ROUND 46 (issuer, 2026-10-07 ~09:3xZ) -- ONE ISSUER ACT: THE COMPLETION GRADING WALK ON DEV 8ddfe409

**Rectangle:** the CTO's ruling msg 30749 (2026-10-07 09:22Z, answering msg 30748): no round-46 list exists; the newest is
`ledger/CTO_LIST_ROUND41.md`, and rounds 42 to 45 moved grades nobody has re-measured. Round 46 is ONE issuer act, the completion
grading walk over FWD-1..27 on portal DEV, round-41 pattern. `3.0.0_SA_CVO~Z` grades it; the CTO countersigns as in
`ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND41.md` and cuts the round-47 list from every FWD that does not grade REALIZED.
**Base:** portal DEV 8ddfe409 (ls-remote read 09:2xZ; PROD b06863fe = v2.1.203).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zx-G` GRADING WALK (issuer act, no product file) | FWD-1..27 | `deliverables/2.0.0_SA_COO~D/round46/` and the `read-<stamp>/` folders the instruments write beside themselves | 2.0.0_SA_COO~D |

**Instruments, unchanged:** `round35/walk/closewalk35.mjs --no-officer "ASML NA" --names "BA US,VLO US,AMD US,MSFT US"`;
`round37/walk/reads37.mjs --names "BA US,AMD US"`; `round42/walk/reads42.mjs` (the sidebar read); `round44/walk/reads44.mjs` and
`round45/walk/reads45.mjs` (FWD-18, FWD-1 segments, the top band, input provenance); `round35/checks/instrument/instrument35.cjs`.
Live: localhost:5174 = `C:/tmp/wk-dsgn-amgtv1-92/portal` detached at 8ddfe409 (`dev:live`, live API). Walker ARM and DISARMED
through MSTR~Z.
**Output:** `round46/COMPLETION_GRADES.round46.json` carrying the issuer's READINGS per FWD (what each instrument printed); the
verdict column is the CVO's to grade.
**Fan-out:** 0 worker chains (no product change). **Risk:** SERVED read (no write).

## v47 -- ROUND 47 (issuer, 2026-10-07 ~10:5xZ) -- ONE BATCHED REPAIR CELL ON THE MODEL TAB; ONE ISSUER READ; ONE CELL HELD

**Rectangle:** `ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md` @43d2e5eb3c, ROUND 47 items 1-4 (msg 30797). **Base:** portal DEV
8ddfe409 (= PROD b06863fe content).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zy-1` BATCHED REPAIR (items 1 and 2) | FWD-20 (10 px text), FWD-27 (the Model tab's foot) | `tabs/ModelTab.tsx`, `modelSheet.ts`, the `__harness__/` files that assert the changed words | ~108 (worker-light) |
| `AV-zy-R` READ (item 4, no build) | FWD-21 | `deliverables/2.0.0_SA_COO~D/round47/FWD21_READ.md` | 2.0.0_SA_COO~D |
| `AV-zy-I` INSTRUMENT CLAUSE (item 3) | FWD-18, FWD-20 | `portal/scripts/ui-contract-check.mjs` and its fixtures | NOT CUT -- waits on PRD v0.16's ratified-text half |

**Item 2, read first as the list orders:** all three foot lines are PAGE text. "Company short name" is `modelSheet.ts`
`V3_HEADER_LABELS.SHORT_NAME`; "N of M inputs have run." is `ModelTab.tsx` (`data-input-ledger-count`); "a source this page has no
name for yet" is `ModelTab.tsx` `ledgerSourceWords`' fallback. The news class's source is SERVED as "harvested news (the overlay feed,
gold article_security_mention)" (`lib/research/api/scoped_amgt.py`); the page has no word for it. Named for AMGT_RESAPP in the close:
that served string carries storage words.
**Check:** `round47/checks/r47/r47.cjs`, the REAL `ModelTab.tsx` rendered on round-11 fixtures. At base 8ddfe409 it reads 1 of 4 (34
rendered 10 px nodes; the short-name line; the ledger wording); PLANTED passes. Green 4 of 4 on scratch reference edits of the two files.
`round11/checks/ledger.cjs` reads 2 of 3 at the base and after (its re-run sentence arm, stale since round 45); it is not in battery29.
**Item 4:** read from the round-46 walk, 10 of 10 (`round47/FWD21_READ.md`); hover only, focus not read.
**Chains:** 1. **Fan-out:** 1 of 1 (`fanout: 1`). **Risk:** LOCAL. **Gate:** `.tools/to-pipeline-gate.py` LIMB 6 refuses a new order while
`prd-signoff status` reads WITHHELD (CTO msg 30802); the order is added the tick it reads ADMITTED.
**Then:** battery29 on the candidate, the render instrument's Model state, CTO review from the render, and ONE DEV push on Andrew's word.

**v47 ADDENDUM (issuer, 2026-10-07 ~11:0xZ) -- item 5 added before the issuance; TWO cells go out in ONE issuance.** The CTO's CORRECTION
(`ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md` @50e71b5b8d, msg 30810): MSFT US is not a covered name, FWD-4 returns to REALIZED
(board 21 / 4 / 1 / 1), and round 47 gains item 5.

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zy-2` (item 5) | FWD-4, FWD-27 (an uncovered name says so once) | `components/HeaderCards.tsx`, the `__harness__/` files that assert seven tiles for an all-absent row | ~109 (worker-light) |

**Item 5, read first:** MSFT US draws 7 tiles, each reading "We hold no stored company data for this name yet."; the served payload carries
no coverage marker, so the page rule is keyed on the served shape (no figure with a value, one reason shared by all). The marker is a
producer item, named in the close. **Check:** `round47/checks/r47b/r47b.cjs`: 2 of 3 at base 8ddfe409, 3 of 3 on a scratch reference
edit, with `round42/checks/r42/r42.cjs` still 5 of 5.
**Chains:** 2, with no shared product file (`AV-zy-1`: `tabs/ModelTab.tsx`, `modelSheet.ts`; `AV-zy-2`: `components/HeaderCards.tsx`), so
both run at once. **Fan-out:** 2 of 2 (`fanout: 2`). PRD v0.17 @8730d6c042 reads ADMITTED. `AV-zy-I` stays NOT CUT: its clause text is
the CTO's to send (msg 30797: "I send its hash"). **The round-47 grading walk** reads FWD-4, 7 and 8 on covered names and one uncovered
name only for its designed state.

## v48 -- ROUND 48 (issuer, 2026-10-07 ~11:3xZ) -- ONE CELL: THE RENDER CHECK'S PURPLE-FILL CLAUSE

**Rectangle:** round 47's item 3 (`ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md` ruling 3), named `AV-zy-I` in v47 and held there
for the PRD addendum. Cut now on the CTO's word (msg 30831: "cut AV-zy-I now, PRD v0.17 @8730d6c042 is ADMITTED"). It is its own round
because the issuance gate admits ONE issuance per round and round 47's is @de235b1e7c; the cell is renamed `AV-zz-1` to fit the cell-id
grammar. **Base:** portal ec9f9a0e, the round-47 candidate, APPROVED for DEV @07ff6ebe34 (the push is Andrew's word).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zz-1` | FWD-18 (the amended DONE WHEN), FWD-20 (the render check passes) | `portal/scripts/ui-contract-check.mjs` | ~110 (worker-light) |

**Check:** `round47/checks/r47i/r47i.cjs` lifts the `purpleFills` predicate and `gradeFwd18` out of the script's text and evaluates them:
1 of 4 at base ec9f9a0e, 4 of 4 on a scratch reference edit. The order also runs the instrument once and reads 0 FAIL cells in its
candidate grades (10 today, all this clause). The candidate becomes ec9f9a0e + 1 commit touching no product file.
**Fan-out:** 1 of 1 (`fanout: 1`). **Risk:** LOCAL.

## v49 -- ROUND 49 (issuer, 2026-10-07 ~12:2xZ) -- TWO CELLS: THE MODEL FOOT'S MONEY FORMAT; A PLANTED PAIR FOR EVERY RENDER-CHECK CLAUSE

**Rectangle:** the CTO's rulings msg 30859 (FWD-20: "each clause" means every clause) and msg 30869 (FWD-27: three grounds; the
money format is a page cell), on `3.0.0_SA_CVO~Z`'s files `DSGN_AMGTV1_ROUND48_FWD18_FWD20_REGRADE_20261007.md` @4a94e19089 and
`DSGN_AMGTV1_FWD20_CLAUSE_COUNT_AND_FWD27_REGRADE_20261007.md` @7ca923a956. Board 21 / 4 / 1 / 1 (FWD-7, 8, 20, 27 NOT_REALIZED).
**Base:** portal 97598dc3 (the round-48 candidate; ONE DEV push on Andrew's word, CTO msg 30851).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zza-1` | FWD-27 (one money format on the Model foot) | `tabs/ModelTab.tsx` | ~111 (worker-light) |
| `AV-zza-2` PLANTS (issuer act, test files only, no product file) | FWD-20 (the check FAILS a planted page on each clause, beside a clean control) | `deliverables/2.0.0_SA_COO~D/round49/checks/plants49/` | 2.0.0_SA_COO~D |

**`AV-zza-1`, read first as the CVO asked:** both foot figures are PAGE-formatted (`ModelTab.tsx` `v3FactValue`); the header's short form
is `components/StatTile.tsx` `formatStatValue`. **Check:** `round49/checks/r49/r49.cjs` computes its expected strings by calling that
formatter, so it grades "the foot uses the header's formatter": 2 of 3 at base 97598dc3 ("USD 152,320 million" against "USD 152B"),
3 of 3 on a scratch reference edit, `r47.cjs` still 4 of 4.
**`AV-zza-2`:** `plants49.cjs` plants one violation per clause on the Thesis state beside one clean control, and runs the portal's own
`scripts/ui-contract-check.mjs`. It covers the five the CVO counted as lacking a pair (fonts, weights, radii, shadows, the designed
states) and four more it plants anyway so no clause rests on history (sizes, lowContrastChars, purpleFills, tabPanelsWhite). The
designed-states pair is two FULL sweep runs: a page whose error-state marker is stripped, and an untouched control.
**Chains:** 2, no shared file. **Fan-out:** 1 of 1 worker chain (`fanout: 1`); the second cell is the issuer's. **Risk:** LOCAL.
**Not this round:** the country's capitals and the Filings ledger row (the producer's, routed to `2.0.0_SA_COO~Z` by msg 30869); the
What-changed row labelled in the vendor's words (not read; named in the close); row Z-S21.

## v50 -- ROUND 50 (issuer, 2026-10-07 ~13:0xZ) -- ONE CELL: THE RENDER CHECK REQUIRES THREE DESIGNED STATES, NOT FOUR

**Rectangle:** CTO msg 30918 ("the four-against-three count in the instrument is one script-only cell for the next issuance, whatever
the grade"), on the finding in `round49/ROUND49_CLOSE.md` @5e36b6ca82. PRD v0.17 FWD-19 names three designed states and FWD-20 reads
"the three states of FWD-19 present"; `portal/scripts/ui-contract-check.mjs` still requires a no-permission state in its run cell and
the standalone no-permission capture in `gradeFwd19`. **Base:** portal b3440392 (CTO-APPROVED for the one DEV push @add38b2768).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zzb-1` | FWD-19, FWD-20 (the check grades the amended text) | `portal/scripts/ui-contract-check.mjs` | ~112 (worker-light) |

**Check:** `round50/checks/r50/r50.cjs` lifts `gradeFwd19` and the run-cell block out of the script's text and evaluates them with
planted inputs: 2 of 4 at base b3440392 (both cells FAIL on a missing no-permission), 4 of 4 on a scratch reference edit, `r47i.cjs`
still 4 of 4. The order's third criterion is the real run: the designed-states pair of `round49/checks/plants49/plants49.cjs` on the
edited instrument (an untouched full sweep still PASSES; the stripped-error page still FAILS).
**Fan-out:** 1 of 1 (`fanout: 1`). **Risk:** LOCAL. The candidate becomes b3440392 + 1 commit touching no product file.
**Not this round:** renaming the `fourStates` key (other files read it); removing the standalone capture itself.

## v51 -- ROUND 51 (issuer, 2026-10-08 ~11:0xZ) -- TWO CELLS: ONE STATEMENT OF INPUTS + THE COVERAGE SENTENCE; OFFICERS AS SERVED + TWO PACK PHRASES

**Rectangle:** PRD v0.18 @9a07662460, rows SAUX-37 to SAUX-40 (CTO msg 31675: "take rows 37 to 40 into the next issuance"), on the
AMGT_RESAPP round-78 analysis R3 (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round78.md` @1a67e26433). **Base:** portal DEV
d1b21c97. The hold of CTO msg 31019 is met: the redeploy bb-18 is live since 2026-10-08T07:19:32Z (that analysis, section 1).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zzc-1` (SAUX-37, SAUX-39) | FWD-12 (one statement of inputs), FWD-27 (a served absence sentence is drawn) | `SecurityAnalysis.tsx`, `components/InputProvenance.tsx`, `components/CoverageNote.tsx` (new), `tabs/ModelTab.tsx`, `topBandTypes.ts`, `types.ts` | ~113 (worker-light) |
| `AV-zzc-2` (SAUX-38, SAUX-40) | FWD-27 (officers in the served order; two packs, two phrases) | `tabs/ExecManagementTab.tsx`, `reasonWords.ts`, `tabs/ThesisTab.tsx` | ~114 (worker-light) |

**Read first, per row:**
- SAUX-37: the block above the tabs is fed from `/overlay` (4 rows, no filings row); the Model tab's ledger is a second statement from
  another read. The function serves ONE statement on `/thesis` (`lib/research/api/inputs_statement.py`, in the deployed pin fbb643923e by
  content): five rows, the filings row carrying `form`, `filing_date`, `used_for`. **L5 decision:** the one statement is the block above
  the tabs, fed from `/thesis`; the Model tab's ledger is removed.
- SAUX-39: `research_coverage` is served on `/overlay` and `/thesis` (`coverage_marker.py`, in the pin; live on MSFT in the round-78
  walk's `overlay_MSFT.json`); the page draws it nowhere. It is drawn once under the identity header.
- SAUX-38: `ExecManagementTab.tsx` `orderedOfficers` re-sorts the served list (round 29, SAUX-32); the function now ranks it. The sort
  is removed.
- SAUX-40: "research pack" is the SERVED name of the pack the system builds, and also the page's own word for the research team's
  document (`reasonWords.ts`). **L5 decision:** the served name keeps the phrase; the research team's document reads "research-team
  report" / "the research team's report".

**Checks:** `round51/checks/r51a/r51a.cjs` reads 1 of 4 at the base (PLANTED passes); on a scratch reference edit its render arms
pass, and its two source-read lines were not exercised green. `round51/checks/r51b/r51b.cjs` reads 1 of 3 at the base and 3 of 3 on a
scratch reference edit. `round29/checks/battery29.sh` at the base: ALL PASS (0 skipped). Each order carries two criteria: its check and
the battery.
**Chains:** 2, with no shared product file, so both run at once; both may touch `__harness__/`, merged in order at the drain.
**Fan-out:** 2 of 2 (`fanout: 2`). **Risk:** LOCAL. PRD v0.18 reads ADMITTED (`prd-signoff status`, read at 10:3xZ).
**Not cut:** SAUX-41 and SAUX-42 wait on AMGT_RESAPP round 79 serving the value first (PRD v0.18).
**Superseded by this round:** `round47/checks/r47/r47.cjs` (the Model ledger's wording) and `round29/checks/tabs/tabwords.cjs` arm 1 (the
page's own officer sort). Neither is in battery29.
**Then:** the drain, battery29 with no skip on the combined candidate, the close walk on a local build against the live function (BA,
AMD, BP/ LN, MSFT), CTO review, and ONE DEV push on Andrew's word.

## v52 -- ROUND 52 (issuer, 2026-10-08 ~12:5xZ) -- ONE DIRECT ACT: THE RESEARCH TEAM'S DOCUMENT READS "THE RESEARCH TEAM'S PACK" EVERYWHERE

**Rectangle:** CTO msg 31721 (REVIEW + RULING on `round51/ROUND51_CLOSE.md` @24f8e4384c): SAUX-37, 38 and 39 accepted on the walk;
finding F1 ruled; candidate bfba701f RETURNED "for that one cell", the wording. **The ruling:** the team names its own file "Research
Pack", so the words belong to the team's document alone; on the page it is "the research team's pack" everywhere; "research-team
report" is withdrawn (`reasonWords.ts` and `tabs/ThesisTab.tsx`). The BUILT thing loses the word at the producer (AMGT_RESAPP round
79, cc-6: its source is served as "the analysis built for this name"). This supersedes v51's L5 decision on SAUX-40.

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zzd-1` DIRECT ACT (under the size floor, `<risk>LOCAL</risk>`; no task order) | FWD-27 (SAUX-40) | `reasonWords.ts`, `tabs/ThesisTab.tsx` | 2.0.0_SA_COO~D |

**The act:** portal `dbeb6764` = bfba701f + two commits (`655994d2`, `dbeb6764`), two files, +9 -4. The first commit's rule was
wrong: CTO msg 31737 asked for the doubling case, and "no class A report is on file" read "... is not on file is on file"; two more
served shapes garbled ("the most recent class A report ...", "no class-A or class-B report was picked"). The second commit gives each
served sentence shape its own form. The shapes were read from `lib/research/corpus/continuation.py` and `dossier.py`.
**Check:** `round52/checks/r52/r52.cjs` (r51b.cjs with arm 2 re-pointed to the ruling, plus six served sentence shapes printed and
graded for doubled words and stacked articles): 2 of 3 at the base (the ~114 tree at 060d0025) and at 655994d2; 3 of 3 on dbeb6764.
`r51a.cjs` still 4 of 4. `r51b.cjs` arm 2 is superseded.
**Real run:** `round51/walk/walk51.mjs` on dbeb6764 against the live function, BA US and BP/ LN: 8 of 8 reads PASS
(`round51/walk/read-20261008T123449Z/`); every drawn line naming the team's pack is printed in `round52/ROUND52_CLOSE.md`.
**Fan-out:** 0 orders (`fanout: 0`, one direct act).

## v53 -- ROUND 53 (issuer, 2026-10-08 ~21:4xZ) -- THREE CELLS: THE SEEKING ALPHA STATES; THE SEGMENT TABLE + THE FIVE NOTE SECTIONS; THE BUILT ANALYSIS'S NAME IN THE POSTURE CITES

**Rectangle:** PRD v0.18 @9a07662460 rows SAUX-41 (FWD-27), SAUX-42 and SAUX-43 (FWD-4), each "after COO~Z serves it (AMGT_RESAPP round
79)", plus the carried rename of decomposition v52 (the CTO's ruling msg 31721: the built thing is "the analysis built for this name").
**The hold is met, measured by this seat:** AMGT_RESAPP cc-7 redeploy @42700562a4 (2026-10-08 20:16Z); `r79_deployed.py` against the
deployed function ~21:1xZ: "R79 DEPLOYED: YES 1 of 1". Live bodies captured by `round53/capture_served.py` into `round53/served/`:
`/freshness?view=page` 95 covered rows, Seeking Alpha read 13 / checked 15 / no_record 67 (snapshot 2026-10-08T18:08Z); `/thesis` for AMD
(table 6x5, sections 0/5), ASML (12x5, 5/5), NU (none, 3/5), 8766 JP (6x5, 1/5), HD (none, 0/5). **Base:** portal DEV 38cc0ecf (origin,
ls-remote read ~21:1xZ).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zze-1` (SAUX-41) | FWD-27 (the Seeking Alpha column draws read / checked / no record apart, in the served words) | `api/endpoints/amgt-lead-panel.ts`, `pages/Freshness/freshnessRows.ts`, `pages/Freshness/Freshness.tsx`, `pages/Freshness/Freshness.test.tsx` | ~115 (worker-light) |
| `AV-zze-2` (SAUX-42, SAUX-43) | FWD-4 (the segment table with its periods and citation; the five research-note sections with their openers or reasons) | `SecurityAnalysis/components/SegmentTable.tsx` (new), `SecurityAnalysis/components/DossierSections.tsx` (new), `SecurityAnalysis/tabs/ThesisTab.tsx`, `SecurityAnalysis/types.ts` | ~116 (worker) |
| `AV-zze-3` DIRECT ACT (SAUX-40 carried) | FWD-27 (two packs, two phrases) | `SecurityAnalysis/postureCites.ts` | ~117 (worker-light) |

**L5 decisions:**
- SAUX-41: the cell prints the served `seeking_alpha.sentence` verbatim and carries `data-sa-state`; the stale rule stays the server's.
- SAUX-42: the five sections sit together on the Thesis tab directly under the research team's pillars, one block "The research team's
  notes", each under its served heading with the pillars' opener; an absent one prints its served reason.
- SAUX-43: the table sits on the Thesis tab directly above the filing's segment prose; a served reason is drawn in its place. Both draw
  whatever the drafting state is.
- The rename: "names" becomes "calls" in two sentences, so none reads "the analysis built for this name names".

**Checks** (each dry-run at the base, then green on a scratch reference edit; the tree was not left edited):
- `round53/checks/r53a.cjs`: base 2 of 3 (arm 1 FAIL as expected); reference edit 3 of 3.
- `round53/checks/r53b.cjs`: base 1 of 4 (arms 1-3 FAIL as expected; arm 4 PLANTED passes); reference components 4 of 4.
- `round53/checks/r53c.cjs`: base 2 of 3 (arm 1 FAIL as expected); scratch edit 3 of 3, reverted.
- `round29/checks/battery29.sh` at the base (slot ~116 tree): ALL PASS (0 skipped).
Each order carries two criteria: its check and the battery.
**Chains:** 3, no edge and no shared product file (zze-2 and zze-3 may both touch `__harness__/`; merged in order at the drain).
**Fan-out:** 3 of 3 (`fanout: 3`). **Risk:** LOCAL.
**Then:** the drain, battery29 with no skip on the combined candidate, `bun test` of the Freshness page, the one real run on a local build
against the live function (AMD and ASML Thesis tab; /freshness on BA, a checked row and a no-record row), CTO review, and ONE DEV push on
Andrew's word.

## v54 -- ROUND 54 (issuer, 2026-10-08 ~22:5xZ) -- ONE BATCHED REPAIR CELL ON THE FRESHNESS PAGE (DIRECT ACT)

**Rectangle:** the CTO's round-53 verdict (msg 32088) and the rows it routed to this round. This is the round-54 list in
`round53/ROUND53_CLOSE.md` @4a5b10aaf3:
- the finding: a no_record Seeking Alpha cell carries data-state "collected";
- DSGN_AMGTV1-Z-S25: the day cells wrap;
- DSGN_AMGTV1-Z-S26: the head "Research pack" names the built analysis.

**Base:** the round-53 candidate portal 84e13d0f, CTO-approved for DEV. Its DEV push waits on Andrew's word.

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zzf-1` DIRECT ACT (three repairs batched; under the size floor; `<risk>LOCAL</risk>`) | FWD-27 (the cell carries the served state; a day on one line; two packs, two phrases) | `pages/Freshness/Freshness.tsx`, `pages/Freshness/freshnessRows.ts`, `pages/Freshness/Freshness.test.tsx` | ~118 (worker-light) |

**L5 ruling (S26):** the column head is "Built analysis". This is the head form of "the analysis built for this name".
**Check:** `round54/checks/r54.cjs`. At the base 84e13d0f it reads 1 of 4: arms 1-3 FAIL as expected, PLANTED passes. On a scratch
reference edit it reads 4 of 4, and `round53/checks/r53a.cjs` still reads 3 of 3 there.
**Chains:** 1. **Fan-out:** 1 of 1 (`fanout: 1`). **Risk:** LOCAL.
**Then:** the drain, battery29 and the Freshness bun test on the stacked candidate, a /freshness real run, and CTO review.
**CANCELLED before spawn (issuer, ~23:1xZ):** Andrew-direct ~22:5xZ/~23:0xZ moves DSGN_AMGTV1 to DELL1 after the CURRENT round closes.
The record is `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_225xZ_AMGT_DSGN_RIVALS_TO_DELL1_AFTER_ROUND_CLOSE_AND_BBG_CENSUS.md`
@b7361ceb2a. The relay is 1.0.0_SA_CTO~Z msg 32100: "start no new round". AV-zzf-1 is `cancelled` with that pointer, and no worker
took it. This round's list and `round54/checks/r54.cjs` are the next DSGN_AMGTV1 round's list on DELL1.

## v55 -- ROUND 55 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-09 ~00:4xZ) -- ROUND 54's LIST, RE-CUT ON DELL1 (DIRECT ACT)

**Rectangle:** v54's list, unchanged. Site Z cancelled `AV-zzf-1` before spawn on the move (v54, above), and the CTO~Z hand-over
(`deliverables/1.0.0_SA_CTO~Z/HANDOVER_TO_DELL1_20261009.md`) names it the next round's input on DELL1.

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zzg-1` DIRECT ACT (= v54 `AV-zzf-1`: three repairs batched; under the size floor; `<risk>LOCAL</risk>`) | FWD-27 | `pages/Freshness/Freshness.tsx`, `pages/Freshness/freshnessRows.ts`, `pages/Freshness/Freshness.test.tsx` | ~119 (worker-light) |

**Base:** portal 84e13d0f (origin DEV HEAD at the cut). **Dry-run at the base on DELL1** (nested worktree, worker-shaped): `round54/checks/r54.cjs`
1 of 4 (arms 1-3 FAIL as expected, PLANTED passes); `round53/checks/r53a.cjs` 3 of 3; `round29/checks/battery29.sh` ALL PASS (0 skipped).
**Chains:** 1. **Fan-out:** 1 of 1. **Risk:** LOCAL. **Rows:** a dell1 row reads `DSGN_AMGTV1-D1-W119-S<k>`.
**Then:** the drain, battery29 and the Freshness bun test on the candidate, a /freshness real run, and CTO review.

## v56 -- ROUND 56 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-09 ~02:1xZ) -- ONE DATE FORM ON /freshness (DIRECT ACT)

**Rectangle:** the round-55 analysis's enrichment list (`ledger/ROUND_ANALYSIS.round55.md`, msg 1391):
1. R1, one date form across `/freshness` -> cell `AV-zzh-1`. The house form is the long date: `PageEnd` through `formatPanelTimestamp`,
   and Security Analysis round-9 ruling 1 (`dateWords.ts` `longDate`, AV-o-1). The page-drawn days take it, and the ISO day moves to
   `data-day`.
2. R2, Lenovo 992 HK -> not a cell. The row `AMGT_HARVST-D1-S2` is written, but the HARVST channel refuses every plain commit on the
   pre-existing duplicate `Z-S106`. The row is parked at `deliverables/2.0.0_SA_COO~D1/round56/HARVST_ROW_D1-S2_PARKED.json`, to land
   when the laptop CTO's gate fix admits it (1.0.0_SA_CTO~DELL1 msg 1426).
3. Round-54 items AV-zzg-1 did not serve -> NONE. The hand-over's list was the CTO finding, Z-S25 and Z-S26, and all three were served
   (round 55 MET). Z-S24 travels with AMGT_RESAPP.
R1 residual: the served sentences hold ISO days, printed verbatim -> row `AMGT_RESAPP-D1-S1` @76a7a2fc8a (producer ask).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zzh-1` DIRECT ACT (under the size floor; `<risk>LOCAL</risk>`) | FWD-27 (one date format) | `pages/Freshness/Freshness.tsx`, `pages/Freshness/freshnessRows.ts`, `pages/Freshness/Freshness.test.tsx` | ~120 (worker-light) |

**Base:** portal 8d2a08a9. **Check:** `deliverables/2.0.0_SA_COO~D1/round56/checks/r56.cjs`. At the base it reads 2 of 5 (arms 1-3 FAIL
as expected; CONTROLS and PLANTED pass). On a scratch reference edit it reads 5 of 5. The filtered bun test matches 0 tests at the
base (exit=1).
**Chains:** 1. **Fan-out:** 1 of 1. **Risk:** LOCAL. **Rows:** `DSGN_AMGTV1-D1-W120-S<k>`.
**Then:** the drain, tsc and eslint on the Freshness files, a signed-in /freshness real run, and CTO review.

## v57 -- ROUND 57 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-09 ~04:xxZ) -- TWO CELLS ON /security-analysis (DIRECT ACTS)

**Rectangle:** the round-56 analysis's enrichment list (`ledger/ROUND_ANALYSIS.round56.md`, msgs 1570/1593), read against the two walks
(`deliverables/2.0.0_SA_COO~D1/round56/WALK_SECURITY_ANALYSIS_DEV_0008ddd3.md`) and a code map of portal 0008ddd3:
1. R1 -> half (b), the honest not-found -> cell `AV-zzi-1`. Half (a), Enter resolves a typed name, is NOT cut: the page has no suggestions
   and no resolve call, and a page-side name lookup breaks C-PRESENTATION-ONLY. It goes back to 1.0.0_SA_CTO~DELL1 as a producer/contract
   question.
2. R2 money -> NOT cut: the "$" is in quoted news headlines, and the page's own money is one form (USD). R3 dates -> cell `AV-zzi-2` (served
   reason text on the Model card, using the page's own precedent `SecurityOverlay.tsx:96`).
3. R4 contrast -> NOT cut: the HeroDialog header on the navy band, a walker false positive. R5 -> cell `AV-zzi-2` (the two truncated Price
   labels: full text on focus; the title already serves hover). The "clipped element" is an empty chart `tspan`, so it is not cut.
4. R6 -> NOT cut: the month cursor was removed on purpose (AV-zi-1) for the 30D/90D/365D windows. This goes back to the CTO with that
   record.

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zzi-1` DIRECT ACT (LOCAL) | FWD-27, FWD-11 | `SA/notFound.ts` (new), `SA/SecurityAnalysis.tsx`, `SA/__tests__/notFound.test.tsx` (new); `SA/__harness__/` (re-anchor only) | ~121 (worker) |
| `AV-zzi-2` DIRECT ACT, repairs batched (LOCAL) | FWD-27 | `SA/components/PriceBars.tsx`, `SA/dateWords.ts`, `SA/components/model/WhatChangedPanel.tsx`, `SA/tabs/ModelTab.tsx` | ~122 (worker-light) |

**Write sets disjoint. Chains:** 2 (no edge). **Fan-out:** 2 of 2, cap 8. **Base:** portal 0008ddd3.
**Checks:** `deliverables/2.0.0_SA_COO~D1/round57/checks/r57a.cjs`: base 1 of 4, scratch reference 4 of 4. `r57b.cjs`: base 1 of 4, scratch
reference 4 of 4. `battery29`: base ALL PASS; on the scratch, every harness green.
**Rows:** `DSGN_AMGTV1-D1-W121-S<k>`, `-D1-W122-S<k>`. **Then:** the drain (tsc, eslint, battery29 on the combined candidate), a signed-in
/security-analysis walk, and CTO review.

## v58 -- ROUND 58 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-09 ~05:2xZ) -- THE FILING PANEL BESIDE A DRAWN TABLE (DIRECT ACT)

**Rectangle:** `ledger/ROUND_ANALYSIS.round57.md` (msg 1757) section 4: item 1 -> cell `AV-zzj-1`; item 2 (the PROD promote) is not a
cell (a `/prod-deploy` act under its pair, waiting on cross-box XB-20261009T052023Z-bf16).

| cell | serves | owned files | actor |
|---|---|---|---|
| `AV-zzj-1` DIRECT ACT (LOCAL) | FWD-27 | `SA/components/SegmentBreakdown.tsx`, `SA/tabs/ThesisTab.tsx` | ~123 (worker-light) |

**Base:** portal 2d42e9b7. **Check:** `deliverables/2.0.0_SA_COO~D1/round58/checks/r58a.cjs`: base 2 of 4, scratch reference 4 of 4. battery29
base ALL PASS. **Chains:** 1. **Fan-out:** 1 of 1.
**Beside it:** Andrew-direct ~05:0xZ-05:1xZ (record @1725deb826) -- a deep signed-in walk of /security-analysis feeds a register and a brief
(the news spine, the news presentation, the disclaimers) for the next rounds.

## v59 -- ROUND 59 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-09 ~06:3xZ) -- ANDREW'S WALK: SPINE, NEWS, DISCLAIMERS, LAYOUT (SIX CELLS)

**Rectangle:** `ledger/ROUND_ANALYSIS.round58.md` @23fec8836a: cells A-F as `deliverables/2.0.0_SA_COO~D1/round59/ROUND59_CUT_PLAN.md`
@f37fb3dc95, with R2 (IdentityLine YES, cell C removes the tab mounts), R3 (each absence once; served reasons folded, not reworded), R4
(spine) and R5 (one news surface) applied. Scope: the walk register SAW-01..23 (Andrew-direct ~05:0xZ-05:1xZ, record @1725deb826).

| cell | SAW | owned files (`SA/`) | actor |
|---|---|---|---|
| `AV-zzk-1` | 01, 02, 03, 04, 08 | `components/TimelinePanel.tsx`, `components/TimelineWordCloud.tsx` | ~124 (worker) |
| `AV-zzk-2` | 05, 07, 09 | `components/HeaderBrief.tsx`, `components/TopBand.tsx` | ~125 (worker) |
| `AV-zzk-3` | 11 (fold), 12, 14, 20, 21 | `SecurityAnalysis.tsx`, `components/SecurityOverlay.tsx`, `components/InputProvenance.tsx`, `components/CoverageNote.tsx`, `constants.ts`, `types.ts` (tab id), new `tabs/NewsTab.tsx`; the `IdentityLine` mount line in the five tabs (R2) | ~126 (worker) |
| `AV-zzk-4` | 10, 11 (tab), 18, 21 (tab subtitles) | `tabs/ThesisTab.tsx`, `components/DossierSections.tsx`, `tabs/PostureTab.tsx`, `components/SegmentTable.tsx` | ~127 (worker) |
| `AV-zzk-5` | 15, 16 | `tabs/ExecManagementTab.tsx`, `tabs/PeersTab.tsx`, `cscTable.ts` | ~128 (worker-light) |
| `AV-zzk-6` | 17, 19 (title), 22 | `tabs/ModelTab.tsx`, `components/model/WhatChangedPanel.tsx`, `modelSheet.ts`, `components/HeaderCards.tsx`, `components/StatTile.tsx`, `components/PrintExportAction.tsx` | ~129 (worker) |

**Overlap by ruling (R2):** cell C edits ONE line (the `IdentityLine` mount) in five tab files that D, E and F own. Hunks are disjoint, and
the merge reads them. **Not cut here:**
- SAW-06: feed relevance is a RESAPP ask (R6).
- SAW-13: the footers, cut after A-F merge.
- SAW-23: already ruled.
- The battery29 harness re-anchor: one batched repair cell after the merge.
**Checks:** `round59/checks/r59.cjs <cell>` is a source-level floor. At base `c0c6f570` every build arm FAILS, and every PLANTED arm PASSES
(each grader refuses the base form and admits a clean form). `round59/checks/hyg59.sh` (tsc + eslint) PASSES at the base. AC3 per cell is
JUDGMENT, graded on the close walk against the register. **Chains:** 6, with no data edge. **Fan-out:** 6 of 6, cap 8.

## v60 -- ROUND 60 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-09 ~07:3xZ) -- THE ROUND-59 REPAIRS (ONE BATCHED CELL)

**Rectangle:** `ledger/ROUND_ANALYSIS.round59.md` @3ce363b8b2 section 3, items 1-7:
- the battery29 re-anchor;
- one as-of per card;
- the description line;
- the mixed-currency line;
- display units in What changed;
- ten news items at rest;
- the spine's search bookkeeping out of the day detail.

The PROD promote of rounds 58-60 follows under a pair.

| cell | serves | owned files (`SA/` unless noted) | actor |
|---|---|---|---|
| `AV-zzl-1` repairs batched (LOCAL) | FWD-27, layout | `components/TimelinePanel.tsx`, `components/HeaderBrief.tsx`, `components/SecurityOverlay.tsx`, `tabs/PeersTab.tsx`, `components/model/WhatChangedPanel.tsx`, `__harness__/`, and `2.0.0_SA_COO~D/round24/checks/posturezero.cjs`, `round23/checks/postureharness.cjs`, `round20/checks/namecard.cjs` | ~130 (worker) |

**Base:** portal 3ea5d0f9. **Checks:**
- `deliverables/2.0.0_SA_COO~D1/round60/checks/r60.cjs`: base 1 of 7 (the build arms FAIL, PLANTED passes).
- battery29: base FAIL (7 of 14 harnesses; three checks red). The re-anchor is this cell's last item.

**Fan-out:** 1 of 1.

## v61 -- ROUND 61 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-09 ~09:3xZ) -- THE CARRIED REPAIRS, THE SPINE PRICE LINE, THE RANKED NEWS

**Rectangle:** `ledger/ROUND_ANALYSIS.round60.md` @0b03adc339 section 3, items 1-4. Items 1-2 (the Peers UNSTATED line, the caption-arm
rename) are repairs, batched into one cell; items 3 and 4 consume AMGT_RESAPP round 82's served `price_series` and feed `mentions`.

| cell | serves | owned files (`SA/`) | actor |
|---|---|---|---|
| `AV-zzm-1` repairs batched (LOCAL) | FWD-27, layout | `tabs/PeersTab.tsx`, `__harness__/` | ~131 (worker-light) |
| `AV-zzm-2` spine price line (LOCAL) | FWD-27 | `components/TimelinePanel.tsx`, `components/timelinePrices.ts` (new) | ~132 (worker) |
| `AV-zzm-3` news ranked by mentions (LOCAL) | FWD-27 | `components/HeaderBrief.tsx`, `types.ts` | ~133 (worker-light) |

**Base:** portal e6fb269c. **Checks** (`deliverables/2.0.0_SA_COO~D1/round61/checks/`): r61.cjs base 1 of 3; r61b.cjs base 1 of 3
(positive control: a clean `timelinePrices.ts` passes arm 1); r61c.cjs base 2 of 3. battery29 ALL PASS at the base.

**Fan-out:** 3 of 3 chains (disjoint write surfaces), cap 8.
