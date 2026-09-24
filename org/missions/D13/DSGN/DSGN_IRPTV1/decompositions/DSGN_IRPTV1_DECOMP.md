# DSGN_IRPTV1 -- DECOMPOSITION (L5) -- ROUND 3, THE UI FINISH (PRD v0.6)

```json
{
 "project": "DSGN_IRPTV1",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v3",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md@4746617b10",
 "prd_half_hashes": {"ratified-text": "STALE -- OWED BY 3.0.0_SA_CVO (the ENDPOINT changed at v0.6; prd-signoff status 2026-09-24T22:1xZ: WITHHELD)", "brief": "ADMITTED (auto: the CRO wrote the brief, spine v3.19 L4-R)"},
 "round_analysis_ref": "none -- the first cut after the FAST interval (closer-drive FAST -> FULL, call 5); input = PRD v0.6 + org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md@3730d145b5",
 "order_ref": "1.0.0_SA_CTO 100904 (Andrew-direct via 4.0.0_SA_CRO 100892: finish the IRPT UI; back onto /canonical-drive)",
 "author": "2.0.0_SA_COO~D",
 "round": 3,
 "rectangle": "PRD v0.6 ENRICHMENT BACKLOG items 12-22 plus the still-open items 5, 9, 10, 11, each measured against the FAST interval's landed pins",
 "cells": 12,
 "chains": 4,
 "join_cells": 3,
 "portal_base": "DEV 13b5356f (the FAST interval's last landing; re-measured by fetch at the cut)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~D` (L5 is the COO's). **Input:** PRD v0.6 @`4746617b10` (ENDPOINT FWD-1..FWD-18; CELL CANDIDATES
C15-C24; ENRICHMENT BACKLOG 12-22) and the FAST interval's STATUS.md @`3730d145b5`, which names every pin landed on portal
DEV between 17:4xZ and 22:2xZ. There is no round-2 analysis: the FAST interval ran in its place, and the spine's call 5
cuts this round straight from the next-list. Round 2's decomposition (v2 @`2a26e433b3`) is spent (7 of 8 cells merged and
on DEV since `a3f4c860`; `IV-e-7` superseded by the FAST lease, drive-mode.log line 1). **Frozen at the cut.**

**Rulings reaching every cell:** Andrew's calls C1-C3 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_214xZ_IRPT_UI_CALLS_C1_C3_ANSWERED.md`): cash is green,
on Positioning too; progressive disclosure is portal law; the search box and the paged list are shared components.
Andrew-direct ~19:4xZ design notes (`org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260924_194xZ_IRPT_DESIGN_NOTES/`).
Andrew-direct ~18:3xZ: the build place is the main portal checkout on DEV. CTO 100865: a test re-scope inside this lease
surface is this seat's own call, cited to the ruling it serves. PRD CONTRACTS: the FE derives nothing; "not supplied",
never zero; ids never print; facts move to a disclosure, they do not vanish; the colour is the page's, keyed by code or
served class, never by a label substring or a guess. Spine L6 diet: a build cell carries at most THREE mechanical criteria;
repo-wide hygiene at the drain.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

The rectangle is PRD v0.6's backlog, every item not yet CLOSED, measured against DEV `13b5356f` (the main checkout,
2026-09-24 ~22:2xZ) and STATUS.md's acceptance table:

```
  item  outcome            landed in the FAST interval (pin)                       open remainder                         cell
  ----  -----------------  -----------------------------------------------------  -------------------------------------  --------
   5    FWD-11             footers (c75a0fc9, af66ed43); drill table (f338e693)    status band tokens; "Basis" chip; firm  IV-e-18
                                                                                   chip; "PERIOD:" labels; census
   9    FWD-9              --                                                      one page-level Export; per-tab gone     IV-e-16
  10    FWD-10             tab-bar scrollbar (93b28880)                            tab order P/H/A; print sheet off Perf   IV-e-16
  11    FWD-1 (spread)     --                                                      P's `spread` -- DEFERRED, not a cell    --
  12    FWD-12             drill pie by served model_code (13b5356f), label        shared lib by code; hero cards by code  IV-e-11
                           fallback (08a04fe2)
  13    FWD-13             map/table/dialog by served asset_class (13b5356f)       cash green in chartColors (Positioning) IV-e-12
  14    FWD-14             pie stops at models (9bb4c5da); full-width dialog        bars stop at models; map drill + the    IV-e-13
                           (721170ca)                                              Positioning hover card; legends scale
  15    FWD-15             drill table (f338e693); Analysis strings (68f46e18)     every other body label; fe-s-5 fields  IV-e-18
  16    FWD-16             --                                                      per tab + the DESIGN.md clause         IV-e-19
  17    FWD-3 (amended)    readable input under OS dark mode (93b28880)            shared search select + paginator        IV-e-9
  18    FWD-2 (amended)    header chips + id bubbles gone (93b28880)               account filter in Holdings + Perf       IV-e-10
  19    FWD-7/8 (amended)  request panels gone (68f46e18); upload lane (088386fe)  three cards; upload step; prospect card IV-e-14
  20    FWD-17             --                                                      the sample view                         IV-e-15
  21    FWD-18             footers; tab scrollbar                                   tooltip families; motifs; band census   IV-e-20
  22    FWD-10 tab order   --                                                      (with item 10)                          IV-e-16
  --    repair             upload bridge type (088386fe); gen-wire has no oneOf    gen-wire oneOf rule; regenerate; drop   IV-e-17
                           rule (UnrenderableSchemaError)                          the bridge + the members' casts
```

```
  backlog items 5, 9-22 (the open population) ............................................... 15
  minus 11 (P's `spread`: a producer act, consumed when served; no page work until then) ..... -1
  minus 22 (the same act as 10: one cell carries both) ........................................ -1
  plus the repair (a gap the FAST interval exposed: the generator cannot render oneOf) ........ +1
  ------------------------------------------------------------------------------------------------
  CELLS IN ROUND 3 ............................................................................. 12   (IV-e-9 .. IV-e-20, no gaps)
```

**The unscoped control.** Read from the PRD's CELL CANDIDATES C15-C24 rather than the backlog: C15 -> IV-e-9, C16 ->
IV-e-10 (+ IV-e-14 for the Analysis input), C17 -> IV-e-11, C18 -> IV-e-12, C19 -> IV-e-13, C20 -> IV-e-18, C21 ->
IV-e-19, C22 -> IV-e-14, C23 -> IV-e-15, C24 -> IV-e-20 (+ IV-e-13 for the hover card); C12, C13 -> IV-e-16; C14 ->
IV-e-18. Every candidate lands in a cell; no cell serves a candidate outside the PRD. Read from STATUS.md's parked table:
the asset-class data for non-Opal securities, the "withheld" supervision/advisory, the credential manager and the leftover
folders are not page work and stay parked with their owners.

**Status vocabulary** -- `MEASURED` (evidence in hand, instrument named) - `DECLARED` - `NOT-EVALUATED` - `N/A`.

---

## 2. THE CELLS -- 12 (round 3)

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1: prefix `IV`, axis `e`, numbering continued from round 2.
Paths portal-relative; `IR/` = `src/pages/InvestorReporting/`.

| cell | what it builds (the remainder only) | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `IV-e-9` | C15: a shared searchable dropdown (the `PageSurfaceControl` look, suggestions as you type, no clipping) and a shared paginator under `src/components/ui/`; `IR/header/ClientSearch.tsx` and `IR/header/BrowseDrawer.tsx` adopt them; the Catalyst combobox's `dark:` classes leave `src/ui/components/catalyst/combobox.tsx` with every other reader named and read before/after | FWD-3 | `src/components/ui/SearchSelect.tsx` (new), `src/components/ui/Paginator.tsx` (new), `src/ui/components/catalyst/combobox.tsx`, `IR/header/ClientSearch.tsx`, `IR/header/BrowseDrawer.tsx`, `IR/__tests__/dsgn-irptv1/iv-e-9.*` | `components/ui/PageSurfaceControl.tsx`, `pages/ModelPortfolios.tsx` (the dropdown reference) | LOCAL |
| `IV-e-10` | C16: an account filter next to the Holdings drill and the Performance accounts table (name + masked tail from the directory, never an id); the Analysis input's account choice rides `IV-e-14` | FWD-2 | `IR/tabs/holdings/HoldingsTab.tsx` (one filter mount, ruled), `IR/tabs/reporting/AccountsTable.tsx`, `IR/__tests__/dsgn-irptv1/iv-e-10.*` | `IR/header/IdentityCard.tsx` (`fetchIdentityCardData`, `overWhatFor`), `IR/header/search.ts` | LOCAL |
| `IV-e-11` | C17: `getModelColor` resolves through `canonicalModelCode`, never a label substring (the "Opal Ultra Long Term" -> Long Term blue defect); the hero cards colour by code; `IR/tabs/holdings/DrillTree.tsx`'s label fallback retired where a code exists | FWD-12 | `src/lib/modelPortfolioColors.ts`, `IR/tabs/holdings/DrillTree.tsx`, `IR/__tests__/dsgn-irptv1/iv-e-11.*` | readers of the lib: Model Portfolios, Positioning, Attribution -- a before/after read of each is the criterion | LOCAL |
| `IV-e-12` | C18 remainder: `ASSET_CLASS.cash` moves to green in `src/lib/chartColors.ts` (Andrew's C1), Positioning named and read before/after; the legend and hover say "Unclassified" for an unclassified security | FWD-13 | `src/lib/chartColors.ts`, `IR/tabs/holdings/assetClass.ts`, `IR/__tests__/dsgn-irptv1/iv-e-12.*` | `pages/Positioning/tabs/HoldingsTab.tsx` (reader; never edited) | LOCAL |
| `IV-e-13` | C19 remainder: the allocation bars stop at the model level; the Securities map carries the model-to-securities drill with the Positioning hover card pattern on `DataTooltip` (copied, never imported from the Positioning page); a legend with many entries stays readable | FWD-14, FWD-18 | `IR/tabs/holdings/AllocationBars.tsx`, `IR/tabs/holdings/HoldingsTreemap.tsx`, `IR/tabs/holdings/DrillTree.tsx` (legend only), `IR/__tests__/dsgn-irptv1/iv-e-13.*` | `pages/Positioning/tabs/HoldingsTab.tsx` (`HoldingsTreemapTooltip`, read only), `components/DataTooltip.tsx` | LOCAL |
| `IV-e-14` | C22 + FWD-8: the three variant cards (the portfolio alone / vs one Opal model / vs several) in the Philosophy card style on `HeroGraphic`; the upload as a designed step with a place and a state; the Analysis input's account choice (C16's third view); a prospect card in the header when no client is chosen; the comparison-key input in advisor words | FWD-7, FWD-8, FWD-2 | `IR/tabs/analysis/AnalysisTab.tsx`, `IR/tabs/analysis/ProspectComposer.tsx`, `IR/tabs/analysis/GenerateComposer.tsx`, `IR/tabs/analysis/VariantCards.tsx` (new), `IR/header/IdentityCard.tsx` (the prospect card), `IR/__tests__/dsgn-irptv1/iv-e-14.*` | `pages/Philosophy/**` (`PhilosophyPillars`, read only), `components/HeroGraphic.tsx`, `IR/tabs/analysis/composer.ts` | LOCAL |
| `IV-e-15` | C23: Performance and Holdings with no client show sample components marked as a sample, and one prompt to choose a client; no sample figure is real client data | FWD-17 | `IR/tabs/TabShell.tsx` (the selection-required branch), `IR/tabs/SampleView.tsx` (new), `IR/__tests__/dsgn-irptv1/iv-e-15.*` | the smoke fixtures (the sample's shape, never its values) | LOCAL |
| `IV-e-16` | C12 + C13: one page-level Export on the header exporting the active tab at the revision on screen; the per-tab disabled buttons retired (fe-s-5 controls re-scoped, CTO 100865); the tabs read Performance, Holdings, Analysis; the Performance tab off `render/print.css` / `.ir-page` onto screen layout | FWD-9, FWD-10 | `IR/index.tsx` (the header action, ruled), `IR/tabs/TabShell.tsx` (TABS order), `IR/tabs/reporting/ReportingTab.tsx` (the `.ir-page` wrapper and Export mount, ruled), `IR/__tests__/fe-s-5/controls.test.ts` (re-scope), `IR/__tests__/dsgn-irptv1/iv-e-16.*` | `IR/export/**` (the existing submit/receipt path, consumed unchanged), `render/**` (never written) | LOCAL |
| `IV-e-17` | REPAIR: `IR/__tests__/fe-s-13/gen-wire.ts` renders a oneOf of object alternatives; the wire types are regenerated from CLOUD's v1 (AnalysisUpload request/result, PerformanceReport provider `OPAL_ENGINE`, the HoldingsSnapshot members); the bridge type in `IR/tabs/analysis/prospect.ts` and the members' casts are dropped | FWD-7, FWD-5, FWD-13 | `IR/__tests__/fe-s-13/gen-wire.ts`, `IR/contracts/wire/**` (regenerated output: a RULED touch on P's surface, asked by P 100861 / 100893), `IR/tabs/analysis/prospect.ts`, `IR/__tests__/dsgn-irptv1/iv-e-17.*` | `docs/contracts/investor-reporting/v1/**` (workspace, read) | LOCAL |
| `IV-e-18` | JOIN 1 -- C20 + C14: client language on every body -- the status band's state and reason code, the "Basis:" chip, the firm-attribution chip, the accounts table's "PERIOD:" labels move to disclosures; fe-s-5/fields re-scoped to the PRD (CTO 100865); a DOM census over the three bodies printing zero state tokens, reason codes, revisions, `sel_`/`acc_` ids, with the disclosures as the positive control | FWD-15, FWD-11 | `IR/tabs/reporting/*`, `IR/tabs/holdings/HoldingsTab.tsx`, `IR/global/FirmAttribution.tsx` (ruled), `IR/__tests__/fe-s-5/fields.test.ts` (re-scope), `IR/__tests__/dsgn-irptv1/iv-e-18.*` | `IR/tabs/reporting/AnswerStatus.tsx` (P-written: wrapped at the mount, never edited) | LOCAL |
| `IV-e-19` | JOIN 2 -- C21: at rest each tab shows its headline and one main picture; everything else opens from a toggle, a tile, a dialog or a help tip; the portal-law clause lands in `portal/DESIGN.md` under the DSGN_REBRND lane in its own commit (Andrew's C2) | FWD-16 | `IR/tabs/**` (the at-rest composition), `portal/DESIGN.md` (one clause, DSGN_REBRND), `IR/__tests__/dsgn-irptv1/iv-e-19.*` | `DESIGN.md` C1-C12 | LOCAL |
| `IV-e-20` | JOIN 3 -- C24: `DataTooltip` for every chart figure and `HelperTip` for help (the drill pie's default recharts tooltip replaced); a stray-scrollbar census at 1440 and 390; the website motifs (numbered cards, the process band, the short-to-long model spectrum) where they help; a dark-band census against C3 (one band per page) | FWD-18 | `IR/tabs/**`, `IR/header/**` (presentation only), `IR/__tests__/dsgn-irptv1/iv-e-20.*` | `design/brand/opalinvest.com.md`, `pages/ModelPortfolios.tsx`, `pages/Philosophy/**` | LOCAL |

**Risk, stated:** every cell is `LOCAL` -- a worker builds and proves on fixtures in its own worktree and never pushes. The
round's DEV landing is the COO's drain act and is `SERVED` (DEV CI deploys the portal to its DEV host); the COO runs each
outcome once there at the close. PROD stays gated.

**Ruled touches on files this project does not own, named for the CTO before the issuance:** `IR/index.tsx` (IV-e-16, the
header action), `IR/tabs/reporting/ReportingTab.tsx` (IV-e-16, IV-e-18), `IR/tabs/holdings/HoldingsTab.tsx` (IV-e-10,
IV-e-18), `IR/global/FirmAttribution.tsx` (IV-e-18), `IR/contracts/wire/**` (IV-e-17, generated output), and the shared
files `src/lib/modelPortfolioColors.ts`, `src/lib/chartColors.ts`, `src/ui/components/catalyst/combobox.tsx`, `portal/DESIGN.md`.

---

## 3. PLACEMENT AND BASE

**Every cell executes on LAPTOP**, served by `0.9.0_WK_DSGN_IRPTV1~<n>` in a worktree pair
(`.tools/wk-provision.sh provision DSGN_IRPTV1 <n> --path <abs> --portal-ref <portal_ref>`), slots numbered from ~7 so a
row id never collides with rounds 1-2. **Base:** `portal_ref` = portal DEV HEAD at the cut (`13b5356f` at this write,
re-fetched at the issuance and written into the `fanout:` data). The drain merges into DEV in the main portal checkout
(Andrew-direct ~18:3xZ) and pushes under the normal rule; a JOIN cell is provisioned off DEV's tip once the chains it
waits on have landed, so it reads the surfaces as they will stand.

---

## 4. DEPENDENCY EDGES AND CHAINS

Edges keyed to write collision (two worktrees on one file conflict at the drain) and to observed completion.

```
  IV-e-9  --> IV-e-10                 chain A (header + accounts): ClientSearch, BrowseDrawer, the lib combobox; HoldingsTab
                                       filter, AccountsTable
  IV-e-11 --> IV-e-12 --> IV-e-13     chain B (colour + drill): modelPortfolioColors, chartColors, assetClass.ts, DrillTree,
                                       AllocationBars, HoldingsTreemap
  IV-e-14 --> IV-e-17                 chain C (analysis + wire): the analysis files, IdentityCard (prospect), prospect.ts, wire
  IV-e-15 --> IV-e-16                 chain D (shell): TabShell (sample, tab order), index.tsx, ReportingTab
  {A, B, C, D} --> IV-e-18 --> IV-e-19 --> IV-e-20   the JOIN chain: each reads every body the chains moved
```

**CHAINS: M = 4 at the cut** (A, B, C, D pairwise disjoint in write surface); the JOIN chain runs after all four land.
**Fan-out: N = 4 of M = 4 chains, cap 8; join_cells: 3 (IV-e-18, IV-e-19, IV-e-20, serial).** Queue order is the arrow.

---

## 5. BATTERY DISPOSITION

- **`comp-adversary` -- RUN** (`comp-adversary compose org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md`,
  2026-09-24 ~22:3xZ, rc=0): cited commits 10 attempted / 10 VERIFIED; cited paths 12 attempted / 11 stable / 1 flagged --
  `portal/src/components/catalyst/combobox.tsx` GONE (finding F1 below); uncited neighbourhood 1,494 siblings, cap declared.
- **`comp-schedule` -- the gate register this round creates:** (1) FWD-1's signed-in trace -- Andrew's walk on DEV;
  (2) P's `spread` -- consumed when served; (3) M's emission of the classification members per firm under the CTO's GO --
  the map reads Unclassified until then, and the drain reads the served snapshot; (4) the CVO's ratified-text signature at
  v0.6 -- LIMB 6 refuses the issuance until it lands.
- **`comp-iam` -- DECLARED-NOT-APPLICABLE:** no cell writes an AWS surface; the deployed functions are consumed unchanged.
- **The drain's hygiene (every chain, before its DEV landing):** `tsc -b` 0; `eslint` 0 errors on the touched files;
  `bun test src/pages/InvestorReporting` with its failing set diffed against DEV's (0 new); `bun run build`; one real run
  per cell on `localhost:5174` served from the main checkout, the screenshot read; the shared-lib cells add the named
  readers' before/after screenshots.

---

## 6. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE.** Section 1: fifteen open items minus two plus one = twelve cells; falsified from the PRD's C15-C24 (all
inside) and STATUS.md's parked table (all outside by owner). Touch is not exclusive (`DrillTree.tsx`: IV-e-11, IV-e-13;
`HoldingsTab.tsx`: IV-e-10, IV-e-18; `ReportingTab.tsx`: IV-e-16, IV-e-18); section 4 serialises every shared file.

**(ii) SAME GRAIN.** Each cell is one advisor-facing capability, graded by its built behaviour on a fixture, a control
(a planted value, a before/after reader read, a census with its positive control), and the ruled-touch bound.

**(iii) INTENT COHERENCE.** One axis: finishing the advisor-facing render to PRD v0.6. Not the producers, not `spread`,
not the print package, not PROD, not the design team's pass.

**(iv) STATE COHERENCE -- what each remedy does NOT move.** IV-e-9 moves how a client is found, not the selection request
or the entitlement. IV-e-10 moves where accounts are chosen, not who may see them. IV-e-11/12 move colours, not a figure,
a class or a model's identity. IV-e-13 moves the drill's depth and hover, not a weight. IV-e-14 moves the Analysis
composition, not the request the server receives. IV-e-15 adds a sample that no real figure feeds. IV-e-16 moves the
Export's place and the tab order, not what an export produces. IV-e-17 moves generated types, not a wire byte. IV-e-18/19/20
move where facts print and how the page looks; every fact is retained one click down.

---

## 7. FINDINGS FOR THE CTO (at the cut)

- **F1** -- PRD v0.6 PATHS and SURFACE MANIFEST name `portal/src/components/catalyst/combobox.tsx`; the file is
  `portal/src/ui/components/catalyst/combobox.tsx` (comp-adversary: GONE at read-vintage). IV-e-9 writes the real path.
- **F2** -- the Positioning hover card `HoldingsTreemapTooltip` is defined inside `pages/Positioning/tabs/HoldingsTab.tsx`,
  a reference page this project never edits: IV-e-13 copies the pattern onto `DataTooltip`; it does not import it.
- **F3** -- the FAST interval touched P's contract surface twice on its owners' asks (`contracts/envelope.ts` on Y's spec
  edit 2 @088386fe; `contracts/wire/consumed.ts` regenerated on P 100861 @9902bf25) and once on the CTO's step-2 routing
  (`contracts/adapt.ts` + `contracts/index.ts` @13b5356f, CTO 100905). PRD SURFACE MANIFEST says NEVER for
  `contracts/**`; IV-e-17 carries one more such touch (generated output). A ruling that these consumer-side acceptances
  are this seat's under the frontend-integrator word (Andrew ~15:31Z) closes it.
- **F4** -- this seat's interim classifier lookup (86561aef) guessed a class from the Positioning ETF table; 13b5356f
  retired it for the served member, so a fixture or firm without the member reads Unclassified until M emits.
