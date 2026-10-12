# DSGN_IRPTV1 -- DECOMPOSITION (L5) -- ROUND 4, THE FAILS RE-CUT (PRD v0.8)

```json
{
 "project": "DSGN_IRPTV1",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v4",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md@31a61d0466 (v0.8, ADMITTED)",
 "prd_half_hashes": {"ratified-text": "SIGNED by 3.0.0_SA_CVO, current (prd-signoff status 2026-09-25)", "brief": "ADMITTED (auto: the CRO wrote the brief)"},
 "round_analysis_ref": "1.0.0_SA_CTO 100991 on ADJUDICATION_v2.md@7bf1522657 (C-S15: 2 PASS / 5 FAIL / 5 NOT_EVALUATED): re-cut each FAIL as an enrichment cell; the NOT_EVALUATED grade on the signed-in drain trace (CTO 100986)",
 "order_ref": "Andrew-direct 2026-09-25 ~17:2xZ (/canonical-drive on IRPT to completion); CTO 100991, 100986, 100953, R6 (RULINGS_IRPT_20260925.md@75156f2b18)",
 "author": "2.0.0_SA_COO~D",
 "round": 4,
 "rectangle": "the four FE-servable FAILs of C-S15 (IVE10, IVE14 + IVE19, IVE18), the repairs batched into one cell (R6, CTO 100953, rows S14 and W8-S1), and the export hop's consumer side on P's written specs (100960, 100987); IVE16 is parked on the producer",
 "cells": 5,
 "chains": 5,
 "join_cells": 0,
 "portal_base": "DEV 8242412d = origin DEV (ls-remote read 2026-09-25); PROD cb48eff8 carries round 3",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~D`. **Input:** the CTO's round-3 analysis 100991 over the CVO's grades
(`surprise-channel/adjudications/ADJUDICATION_v2.md@7bf1522657`), the CTO's notes 100953 (colour by the served
`model_code`; 2.0.0_SA_COO~M serves it since 23:2xZ) and 100986 (the signed-in FWD-1 trace is the drain act, not a cell),
ruling R6 (fe-s-10/parity kept; fe-s-5/states re-scoped this round), and 2.0.0_SA_COO~P's written interface specs 100960
(submit-export data optional while QUEUED/RUNNING, schema @f6fd60f4fd) and 100987 (the print URL, design card B2-URL
@bc3f70d22c). Round 3 (v3 @2af10e4cd0) is spent: 12 of 12 orders complete and on origin DEV 8242412d. **Frozen at the cut.**

**Rulings reaching every cell:** PRD CONTRACTS (the FE derives nothing; "not supplied", never zero; ids never print; a fact
moves to a disclosure, it does not vanish; colour keyed by code or served class, never a label or a guess); Andrew's calls
C1-C3; CTO 100919 (contracts/** incl. wire is this project's consumer-side surface, landing on the owning seat's written
spec; P keeps portal/src/api/**); CTO 100991: in a LOCAL-only round the JUDGMENT criterion names the COO's close run (the
signed-in trace where reachable) or Andrew's once-over where the AC says so, never the CVO. Spine L6 diet: at most THREE
mechanical criteria per build cell; repo-wide hygiene at the drain.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: the 12 AC4 grades of C-S15. PASS 2 (IVE15, IVE17) -> no cell. NOT_EVALUATED 5 (IVE9, IVE11, IVE12, IVE13,
IVE20) -> graded on the round-4 drain's signed-in trace (CTO 100986, 100991), no cell. FAIL 5 -> IVE10 (`IV-e-21`), IVE14 and
IVE19's Analysis half (`IV-e-22`, one write set: the Analysis tab), IVE18 (`IV-e-23` for the chip and the card;
`IV-e-22` for the two Analysis strings, its write set), IVE16 (PARKED, section 7: the fix is a Holdings report kind the
export producer does not serve; an FE cell has nothing to build). Remainder after subtraction: zero FAILs unplaced.
Repairs outside the grades (R6, CTO 100953, row S14's next-round items, row W8-S1) -> `IV-e-25`. P's two consumer asks ->
`IV-e-26`.

## 2. THE CELLS -- 5 (round 4)

Ids continue from round 3. Paths portal-relative; `IR/` = `src/pages/InvestorReporting/`.

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `IV-e-21` | IVE10: Performance offers the account choice at rest -- the shared `AccountFilter` mounted above the Performance headline (reading `HeaderSelectionContext`), not only inside the collapsed accounts table | FWD-2 | `IR/tabs/reporting/ReportingTab.tsx` (one mount + one import), `IR/__tests__/dsgn-irptv1/iv-e-21.*` | `IR/tabs/holdings/AccountFilter.tsx`, `IR/header/HeaderSelectionContext.ts` | LOCAL |
| `IV-e-22` | IVE14 + IVE19 + IVE18's Analysis strings: with a client chosen the variant cards come first and the prospect upload sits behind one toggle; with no client the upload leads (FWD-8); the Generate form's secondary inputs open from a disclosure so Analysis at rest is the cards and one action; the report title placeholder is the client's name, never a code; the comparison input speaks "Opal model" with no "key" | FWD-7, FWD-8, FWD-16, FWD-15 | `IR/tabs/analysis/AnalysisTab.tsx`, `IR/tabs/analysis/ProspectComposer.tsx`, `IR/tabs/analysis/GenerateComposer.tsx`, `IR/tabs/analysis/VariantCards.tsx`, `IR/__tests__/dsgn-irptv1/iv-e-22.*` | `IR/tabs/analysis/composer.ts` | LOCAL |
| `IV-e-23` | IVE18's header half: the firm chip shows the firm's name (a firm name is client language, R6) with the firm token in a disclosure; the identity card's firm line reads the firm's name, never the token | FWD-15, FWD-2 | `IR/global/FirmAttribution.tsx`, `IR/header/IdentityCard.tsx`, `IR/__tests__/dsgn-irptv1/iv-e-23.*` | `IR/__tests__/fe-s-10/parity.test.ts` (kept, R6: must stay green) | LOCAL |
| `IV-e-25` | REPAIRS, one cell: (a) fe-s-5/states re-scoped per R6 (the heatmap cell reads "not supplied", the reason on hover; the two Summary-block sub-tests re-scoped or removed with the reason stated); (b) models coloured by the served `modelCode` only on the hero cards and the drill pie (CTO 100953, row W8-S1); (c) the drill pie colours a security by its served asset class, never the name hash (row S14 item 2); (d) `SearchSelect` gains combobox/listbox/option roles and arrow/Enter/Escape keys (row S14 item 1) | FWD-15, FWD-12, FWD-13, FWD-3 | `IR/__tests__/fe-s-5/states.test.ts`, `IR/tabs/holdings/DrillTree.tsx`, `src/components/CategoryViewTree.tsx` (additive props only), `src/components/ui/SearchSelect.tsx`, `IR/__tests__/dsgn-irptv1/iv-e-25.*` | `src/lib/modelPortfolioColors.ts`, `IR/tabs/holdings/assetClass.ts` | LOCAL |
| `IV-e-26` | THE EXPORT HOP, consumer side, on P's written specs: `contracts/wire/**` regenerated from the workspace contracts (submit-export `data` optional while QUEUED/RUNNING); `export/submit.ts` accepts that answer and reads the export id from `status.operation.revision`; `render/PrintEntry.tsx` reads `selection`, `start` and `end` from the print URL and `export/resolveBundle.ts` passes them to `getPerformanceReport`, refusing by name when one is missing | FWD-9 | `IR/contracts/wire/`, `IR/export/submit.ts`, `IR/export/resolveBundle.ts`, `IR/render/PrintEntry.tsx`, `IR/__tests__/dsgn-irptv1/iv-e-26.*` | `docs/contracts/investor-reporting/v1/**`, `IR/__tests__/fe-s-13/gen-wire.ts` (run, not edited) | LOCAL |

`IV-e-24` is reserved for IVE16 (section 7) and not cut.

**Addendum (issuer, 2026-09-25 ~19:5xZ; the issuer rules inside its own decomposition, /canonical-drive obligation 7):**
one DIRECT-ACT cell, on 2.0.0_SA_COO~M's written ask 101020 (Andrew-direct 2026-09-25 ~14:4xZ: personal and held-away
assets are the class `other`, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260925_144xZ_CLASSIFIER_OTHER_OPENAI_RUN_AND_DEV_PUSH.md`
@705be61575; the v1 contract admits it, ~P @3d5a590ad0). The CTO's sign-off @8214723353 holds M's bd-securities batch B
until the portal maps it, so it is cut now, not at round 5.

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `IV-e-27` | DIRECT-ACT: the served asset class `other` maps to its own class "Other" (never folded into Unclassified), with a label and a colour distinct from every other class and from Unclassified; an unknown class still reads Unclassified | FWD-13 | `IR/contracts/adapt.ts` (`ASSET_CLASS_FOR_WIRE`), `IR/contracts/index.ts` (the `assetClass` union), `IR/tabs/holdings/assetClass.ts`, `IR/__tests__/dsgn-irptv1/iv-e-27.*` | `src/lib/chartColors.ts` (READ ONLY: a PALETTE token no ASSET_CLASS entry uses) | LOCAL |

## 3. PLACEMENT AND BASE

Every cell is a portal cell on a worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 <n> --portal-ref
8242412d`. The drain lands on DEV in the main portal checkout; origin DEV through 1.0.0_SA_CTO's review and 0.0.0_AB_MSTR's
push. The signed-in FWD-1 trace runs at the drain on IRPT_BCKEND's bounded test principal (IB-rtf-3) if live, else one
signed-in walk by Andrew asked through 1.0.0_SA_CTO (CTO 100986); it grades the five NOT_EVALUATED criteria and every
round-4 JUDGMENT criterion.

## 4. DEPENDENCY EDGES AND CHAINS

No edge: the five write sets are pairwise disjoint (section 2 `writes`), and no cell consumes another's output. M = 5
chains of one cell each; N = 5; cap 8. The hookups a cell needs in a shared file are added at the merge (C10).

## 5. BATTERY DISPOSITION

comp-iam: not applicable (no AWS surface). comp-schedule: none of its four entries is owed. comp-adversary: each cell names
files measured at DEV 8242412d; `IR/tabs/holdings/HoldingsTab.tsx` is M-written and NOT in any write set this round
(`IV-e-21` mounts on the Performance side only).

## 6. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over the declared domain, the 12 C-S15 grades, by subtraction (section 1): every FAIL placed or parked with a
reason. (ii) Same grain: one cell per write set. (iii) One intent per cell, except `IV-e-25`, the spine's one batched repair
cell. (iv) State coherence: `IV-e-25` does not move the Positioning or Model Portfolios colours (their readers are named in
round 3's IV-e-11 and IV-e-12 criteria and stay unchanged).

## 7. FINDINGS FOR THE CTO (at the cut)

- **IVE16 (FWD-9, Export on Holdings): PARKED on the producer.** `render/manifest.ts` `ReportKind` is `'performance' |
  'analysis'`; `index.tsx` `EXPORT_KIND_BY_TAB.holdings = null`. The fix is a Holdings report kind the export producer
  (2.0.0_SA_COO~P) serves; the FE hookup is one map line at the merge once it exists. Routing asked of 1.0.0_SA_CTO.

**Addendum 2 (issuer, 2026-09-25 ~20:4xZ):** one DIRECT-ACT cell routed by 1.0.0_SA_CTO (101030) under
`SIGNOFF_COT_OTHER_20260925.md` @4fdc4284c9, act 2 precondition 3: the Advisor Intelligence Cottonwood views render `other`,
the reader of IV-e-27's class outside the IR page. The PROD promotion (Andrew allows a full /prod-deploy) is a separate act
after the drain; the proof is one real read of z09305589 on PROD after batch B.

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `IV-e-28` | DIRECT-ACT: an opt-in `other` class on the Advisor Intelligence mix (the `includesCash` pattern), ON for Cottonwood only, coloured PALETTE.purple600, labelled "Other"; 49financial and Inflection unchanged | FWD-13 (reader: Advisor Intelligence) | `src/pages/AdvisorIntelligence/_shared/lib/composition.ts`, `_shared/types/TenantLayoutConfig.ts`, `_shared/hooks/useTenantLayout.ts`, `_shared/AdvisorBookView.tsx`, `_shared/components/PartnerAnalytics.tsx`, `_partners/cottonwood/layout.ts`, `__tests__/cot-other/` | `src/lib/chartColors.ts` | LOCAL |

**Addendum 3 (issuer, 2026-09-25 ~22:0xZ):** one DIRECT-ACT cell routed by 1.0.0_SA_CTO (101039) under
`SIGNOFF_COT_CASH_S138_20260925.md` @d257eb67aa (render first: cash must show on PROD before M's C_06 cash deploy), plus row
W18-S1 (the client-drill legend in ConsolidatedOverviewPanel hardcodes its classes). Same PROD release as IV-e-28.

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `IV-e-29` | DIRECT-ACT: cash ON for Cottonwood in ASSET_CLASS.cash green beside `other`; the client-drill legend lists every served class incl. Other and Cash; 49financial and Inflection unchanged | FWD-13 (reader: Advisor Intelligence) | `src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts`, `_shared/panels/ConsolidatedOverviewPanel.tsx`, `_shared/lib/composition.ts`, `__tests__/cot-other/` | `src/lib/chartColors.ts` | LOCAL |

**Addendum 4 (issuer, 2026-09-25 ~23:0xZ):** one DIRECT-ACT cell disarming row W19-S1 (ARMED): IV-e-29's tenant-palette
prop on ConsolidatedOverviewPanel reaches no product caller, so Cottonwood's real client drill colours cash by the MIX_PIE
fallback. Same PROD release as IV-e-28 and IV-e-29.

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `IV-e-30` | DIRECT-ACT: CanonicalBookView and AdvisorBookClientDetail take an optional `tenantLayout` and forward it; every caller passes the viewed firm's layout, so the client drill colours cash and other by the tenant palette | FWD-13 (reader: Advisor Intelligence) | `_shared/panels/CanonicalBookView.tsx`, `_shared/AdvisorBookClientDetail.tsx`, `_shared/AdvisorBookView.tsx`, `_shared/tabs/ClientsTab.tsx`, `__tests__/cot-other/` | `_shared/panels/ConsolidatedOverviewPanel.tsx` | LOCAL |

## v5 -- round 5 (issuer, 2026-09-26 ~13:4xZ)

From 1.0.0_SA_CTO's ROUND_ANALYSIS.round4.md @61cd39d895 section 3 (the enrichment list); rounds 2-4 closed there. Of its six
items: (1) S7 and (2) the FWD-12 remainder are cut below; (3) SearchSelect accessibility is MET AT THE BASE and not cut --
`src/components/ui/SearchSelect.tsx` at 1e02be40 carries combobox/listbox/option roles and ArrowUp/ArrowDown handling (IV-e-25,
2cac0a83); its keyboard grade is the walk's (IVE25-AC4); (4) IVE16 waits on 2.0.0_SA_COO~P's `holdings` report kind (unmet
dependency, not cut); (5) the admin + Dev walk is the round's DRAIN ACT, not a cell; (6) the Monday PROD reads are parked
(STATUS.md). The AI drill 403 is surprise row S16 (filed by the issuer), not an IRPT cell.

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `IV-e-31` | a model slice coloured by its served model_code only; `ASSET_CLASS.other` when no code resolves; the label fallback retires for models | FWD-12 | `tabs/holdings/DrillTree.tsx`, `AllocationBars.tsx`, `SecurityList.tsx`, `__tests__/dsgn-irptv1/` | `src/lib/**` | LOCAL |
| `IV-e-32` | S7 by class (R/G/H/Q) over every failing IR test, the class table at `ledger/S7_CLASS_TABLE.json` | FWD-11, S7 | `src/pages/InvestorReporting/**`, the class table | the ENDPOINT, the PRD | LOCAL |

**Chains:** ONE -- IV-e-31 then IV-e-32 on slot ~21; the batch cell's grant covers the narrow cell's files, so it runs last.

## v6 -- round 6 (issuer, 2026-09-26 ~17:5xZ)

From PRD v0.11 @e13fed2413 (ADMITTED: the CVO's ratified-text half signed; CTO 101294/101298): ENRICHMENT BACKLOG item 23 / C25 (FWD-19, the
client context and per-account Performance route structure, spec'd by 4.0.0_SA_CRO's proposal @889160ce2c sections 2-5). C26 (FWD-20)
is the round after. Andrew pre-authorized the C25 DEV->PROD promote on 3.0.0_SA_CVO's PASS of the pinned candidate after its live DEV
walk (CTO 101383). Issued while round 5's batch cell IV-e-32 still runs on slot ~21 (issuer ruling: C25's files do not overlap IV-e-31's;
test conflicts with IV-e-32's re-scopes are resolved at round 5's drain).

| cell | what it builds | serves | writes | reads (never writes) | risk |
|---|---|---|---|---|---|
| `IV-e-33` | R0/R1: the client is the page unit (one selection, one shared snapshot, one account list keyed by drill_refs id); "Client" everywhere; clear empties the card | FWD-19, FWD-1, FWD-2 | `index.tsx`, `header/*` (IdentityCard, BrowseDrawer, ScopeSummary, HeaderSelectionContext, ClientSearch, search, selectionRequest), `state/selection.ts`, tests | the proposal, the PRD | LOCAL |
| `IV-e-34` | R2a/R3a: tab-local account focus; Performance always one account (largest preselected, chooser always shown); refusals in words; export follows the focused account | FWD-19, FWD-1, FWD-5, FWD-9 | `tabs/reporting/*`, `tabs/holdings/AccountFilter.tsx`, `HoldingsTab.tsx`, `TabShell.tsx`, `export/{ExportButton,resolveBundle,submit}`, plus the shared `IdentityCard`/`HeaderSelectionContext`/`index.tsx` after IV-e-33 | IV-e-33's account list | LOCAL |

**Chains:** ONE -- IV-e-33 then IV-e-34 on slot ~22 (IV-e-34 consumes IV-e-33's account list and re-touches its shared header files).

**v6 addendum 1 (issuer, 2026-09-26 ~19:2xZ):** `IV-e-35` -- the S7 residual carried by CTO 101449 (IV-e-32 landed with AC2 moved): the IR
suite fails only the class table's Q rows; public-status.ts stays producer-faithful. Writes `IR/__tests__/{fe-s-*, m-*, mvp-*,
submission-request}`, `IR/fixtures/`, `IR/render/fixtures/`, `iv-e-17.regenerated.test.ts`, `s7-table-check.ts`, the class table. Slot ~23, in
parallel with IV-e-34 (disjoint write sets). Serves FWD-11 and S7. LOCAL.

**v6 addendum 2 (issuer, 2026-09-26 ~21:0xZ):** `IV-e-36` -- row W22-S6 (surfaced by IV-e-34's worker): Export's PREVIEW fetches
Performance without the tab's focused account and window, so the rule "Performance is always one account" (PRD v0.12 R3/R3a) holds
for the tab and the submission but not the preview. Threads the account set id and window from ReportingTab's export target through
index.tsx and ExportButton into Preview's resolveBundle call. Writes `tabs/reporting/ReportingTab.tsx`, `index.tsx`,
`export/ExportButton.tsx`, `export/Preview.tsx` and two new tests. Slot ~24, in parallel with IV-e-35 (disjoint write sets). Serves
FWD-19 (C25). LOCAL, direct act.

## v7 -- round 7 (issuer, 2026-09-26 ~21:5xZ), over PRD v0.15 @f12fcbb16e (ADMITTED; v0.13 is Andrew's UI review, v0.14/v0.15 add UIR-50 and C34)

**Rectangle:** CTO 101505 -- round 7 cuts from v0.13 (Andrew's UI review, 49 UIR ids; backlog items 25-31 = C27-C33) with C26
(FWD-20, the round after C25, CTO 101294). C27 goes first. DSGN_IRPTV1 owns 45 of the 49 rows (UIR-03, 23, 26, 48 are IRPT_BCKEND ~M;
UIR-07's ranking is ~P's, its render half is here).

**Re-cut by write set.** A read-only map of C26-C33 at DEV fdccc6e6 found the PRD's cells overlap heavily (C29 shares files with six
of the other seven; DrillTree, AllocationBars, SliceTable, slices.ts and AccountFilter each sit in three or more). Cells are re-cut so
each parallel chain owns disjoint files; each cell names the PRD cell and the UIR rows it carries. Every DSGN_IRPTV1 row lands in
exactly one cell (45 rows + FWD-20):

| cell | PRD | rows | chain / slot | files (IR-relative unless src/) |
|---|---|---|---|---|
| IV-e-37 | C28 + UIR-04 | 01 02 04 06 07r 08 09 10 11 | S ~25, 1 of 2 | src/components/ui/SearchSelect.tsx, header/ClientSearch, header/search, header/BrowseDrawer, tabs/SampleView, tabs/TabShell |
| IV-e-38 | C29 header | 05 12 13 14 22 30 | S ~25, 2 of 2 | index.tsx (two named places), header/IdentityCard, header/FirmDropdown, global/FirmAttribution |
| IV-e-39 | C30 | 15 16 18 19 21 | P ~26, 1 of 2 | tabs/holdings/AccountFilter, tabs/reporting/ReportingTab, tabs/StatusPanel, tabs/reporting/PerformanceControls |
| IV-e-40 | C26 | FWD-20 | P ~26, 2 of 2 | AccountFilter, ReportingTab, tabs/reporting/accountFocus, tabs/reporting/period |
| IV-e-41 | C27 | 39 + rootNode census | H ~27, 1 of 2 | tabs/holdings/AllocationBars, slices, DrillTree, SecurityList |
| IV-e-42 | C31 + UIR-24 | 24 31 32 33 34 36 47 49 | H ~27, 2 of 2 | DrillTree, SliceTable, slices, AllocationBars, HoldingsTab |
| IV-e-44 | C33 | 41 42 43 | T ~28, 1 of 1 | tabs/holdings/HoldingsTreemap |
| IV-e-43 | C32 | 25 37 44 46 | Z ~29, 1 of 2 | DrillTree, AllocationBars, HoldingsTreemap, assetClass, palette (new) |
| IV-e-45 | C29 face + 17 + 20 (batch, last) | 17 20 27 28 29 35 38 40 45 | Z ~29, 2 of 2 | index, IdentityCard, HeaderSelectionContext, TabShell, ReportingTab, PerformanceHeadline, SliceTable, HoldingsSummary, AllocationBars, HoldingsTreemap, SecurityList, slices, format (new) |

**Edges (data or shared-file order, not contention inside a chain):** chain P starts after TO-IV-e-36 (direct act, ReportingTab)
drains; chain Z starts after chains S, P, H and T drain, because C32's colours and the batch rows re-touch every holdings file. Chains
S, H and T start now at fdccc6e6. IV-e-38 edits index.tsx at two named places while TO-IV-e-36 edits its export-target mount: the
issuer merges both. Every cell: LOCAL; one mechanical criterion (a test, one arm per row) and one judgment criterion graded by the CVO
on the issuer's live DEV walk. Shared portal libraries (src/lib, src/ui, src/components except SearchSelect) are read only.

**Parked, not in round 7:** C34 (v0.14), the portal mapping for UIR-50's new asset classes (label and colour), which the PRD
cuts once 2.0.0_SA_COO~M's producer half lands.

**v7 addendum 1 (issuer, 2026-09-26 ~23:1xZ):** `IV-e-46`, workstream AI-TAGS, outside the rounds (CTO 101579: "a single cell in its own
workstream, not a DSGN_IRPTV1 round"). Advisor Intelligence's composition and the four partner `ordered` lists admit UIR-50's
`structured` and `commodities` classes, labelled and coloured distinctly from the models, before 2.0.0_SA_COO~M writes any value.
Writes composition.ts, PartnerAnalytics.tsx, the four partner layout.ts files, new keys in src/lib/chartColors.ts, two new tests.
Slot ~30, direct act, LOCAL; the CTO reviews it before DEV. Disjoint from every round-7 chain.

**v7 addendum 2 (issuer, 2026-09-26 ~23:1xZ):** `IV-e-47`, UIR-07's Global merge (CTO 101590/101594, PRD v0.16): full-name matches
first by the server's predicate, in Global only, each firm's served order kept otherwise. Writes header/ClientSearch.tsx,
header/search.ts, one new test. Queued on slot ~25 after IV-e-38, on top of IV-e-37's ClientSearch changes. Direct act, LOCAL.

**v7 addendum 3 (issuer, 2026-09-26 ~23:2xZ):** `IV-e-48` = PRD C34, cut on its trigger: 2.0.0_SA_COO~P's contract enum admits
`structured` and `commodities` (CLOUD d3c5467ce1 + ae32ac98d7). The page maps both (regenerated wire, contracts union, adapt.ts,
assetClass.ts CLASS_FOR_SERVED) with their existing colours; ~M writes the values after it drains. Slot ~31, direct act, LOCAL;
disjoint from every running chain. Chain Z's TO-IV-e-43 (colours) runs after it on merged DEV.

**v7 addendum 4 (issuer, 2026-09-27 ~00:5xZ):** `IV-e-49`, the CTO's one change to IV-e-46 before DEV (101649): one commodities colour at
least CIEDE2000 dE 20 from every MIX_PIE, ASSET_CLASS and model primary, shared by MIX_PIE and ASSET_CLASS.commodities (UIR-44). Writes
src/lib/chartColors.ts, IV-e-46's reader-census test, one new test. Slot ~30 after IV-e-46, direct act, LOCAL. Round 7's harness cell
(CTO 101651, the deterministic suite) and chain Z (IV-e-43, IV-e-45) seat when C: allows a worktree.

**v7 addendum 5 (issuer, 2026-09-27 ~01:2xZ):** `IV-e-50`, the harness cell CTO 101651 names (disarms W23-S1): the IR suite is
deterministic (3 consecutive full runs, identical pass/fail sets; no retries, quarantine or raised Q cap), each flaky file named with its
shared-state source and fixed at the root, and the "only Q rows fail" bar moved here from IV-e-35. Tests, fixtures, the class table and
the channel only. Queued on slot ~29 after IV-e-45 (the last round-7 cell), direct act, LOCAL.

**v7 addendum 6 (issuer, 2026-09-27 ~01:4xZ):** `IV-e-51`, CTO 101681 ruling (b) on IV-e-49: commodities takes the chromatic PALETTE
token with the largest minimum dE00 (>= 20) against every mix, asset-class and model primary, used by no text/ink role, amber/gold
preferred; text contrast >= 4.5:1. Writes src/lib/chartColors.ts and the IV-e-46/49 tests plus one new test. Slot ~30 queue 3 of 3;
then IV-e-46+49+51 go to DEV with no second review.

**v7 addendum 7 (issuer, 2026-09-27 ~04:0xZ):** `IV-e-52`, the follow-on cell CTO 101768 orders for rows W29-S2 / W29-S3: UIR-29 (the
card's "$" format page-wide, one client total = the identity card's HOW MUCH, HoldingsSummary drops its total, non-USD shows its code)
and UIR-27 (the ordinary case one click away), re-goldening the pinned money sets, F39-AC7, and the two tests IV-e-45 broke (fe-s-30
F30-AC5, fe-s-55), each re-golden commit naming its UIR row. Slot ~29 before IV-e-50. Direct act, LOCAL.

**v7 addendum 8 (issuer, 2026-09-27 ~07:1xZ):** `IV-e-53`, the repair of IV-e-36's seam that rows S20 / S22 ground (window 10 K8;
2.0.0_SA_COO~P 101835): the Export preview's Performance request drops `selectedTenant`, which the tab's own request carries, so an
internal viewer gets UNAVAILABLE and resolveBundle throws MissingPayloadError. Thread the export target's `selectedTenant` through
index.tsx, ExportButton and PreviewRequestState into resolveBundle's deps and onto both getPerformanceReport request shapes; the print
path (render/PrintEntry.tsx) passes an optional `selected_tenant` URL parameter the same way. Additive; the analysis path and a call
without a tenant are unchanged. Same class as IV-e-36 (issuer repair of its own cell, row-driven). Slot ~33, direct act, LOCAL; it seats
when C: allows a worktree (0.0.0_AB_MSTR 101618). Thread-breaking (the export hop), so it precedes round 8.

## v8 -- round 8 (issuer, 2026-09-27 ~08:2xZ), over PRD v0.16 @f3026103f0 (ADMITTED; both halves signed)

**Rectangle:** the ENRICHMENT LIST of 1.0.0_SA_CTO's round-N analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND7_20260927.md` @36e18bf320 (msg 101845), E1-E11, one cell
per item; E10 splits into its two ruled cells. Each cell keeps its UIR rows' acceptance lines verbatim on its face. A read-only write-set
map at portal DEV 3f76cdb2 found five shared files (IdentityCard: E1/E3/E7; contracts/adapt.ts: E1/E10a; DrillTree: E4/E5; slices.ts:
E5/E7; HoldingsTreemap: E6/E7), so the chains are cut to keep every parallel write set disjoint:

| cell | item | rows | chain / slot | files (IR = portal/src/pages/InvestorReporting) |
|---|---|---|---|---|
| IV-e-54 | E10a | W29-S8 (F45-AC9, F57-AC2) | A ~34, 1 of 2 | scripts/dev-live.mjs, IR/contracts/adapt.ts, fe-s-45 test + driver, fe-s-57 test |
| IV-e-55 | E10b | W29-S10, W29-S9 (supersedes IV-e-50) | A ~34, 2 of 2 | s7-*.ts/json, iv-e-26 test, suite-complete-check.mjs, IR/__tests__ (test fixes), S7_CLASS_TABLE |
| IV-e-56 | E1 | UIR-04, 13, 30 | H ~35, 1 of 2 | header/firmDisplay (new), contracts/adapt.ts, header/search, ClientSearch, BrowseDrawer, IdentityCard, index.tsx, global/FirmAttribution |
| IV-e-57 | E2 | UIR-11 | H ~35, 2 of 2 | src/components/ui/SearchSelect, index.tsx, tabs/TabShell, tabs/SampleView, ClientSearch |
| IV-e-58 | E3 | UIR-15 (+FWD-20) | P ~36, 1 of 1 | tabs/holdings/AccountFilter, tabs/reporting/ReportingTab |
| IV-e-59 | E4 | UIR-25, 46, 37 | V ~38, 1 of 3 | tabs/holdings/DrillTree, palette |
| IV-e-60 | E5 | UIR-31, 32, 33, 34, 36, 47, 49 | V ~38, 2 of 3 | DrillTree, SliceTable, slices.ts |
| IV-e-61 | E6 | UIR-41 | V ~38, 3 of 3 | tabs/holdings/HoldingsTreemap |
| IV-e-62 | E9 | S18 | N ~39, 1 of 1 | src/api/endpoints/investor-reporting.ts (owned history only), tabs/analysis/AnalysisTab, RequestList, OwnedRequestHistory |
| IV-e-63 | E7 (batch, last) | UIR-45, R10 | Z ~40, 1 of 1 | PerformanceHeadline, MethodAndSources, IdentityCard, HoldingsSummary, slices.ts, SecurityList, AllocationBars, HoldingsTreemap, IR/format.ts |
| IV-e-53 | E11 | S20, S22 | X ~33 (direct act, cut @fd78957113) | export/resolveBundle, Preview, ExportButton, index.tsx, render/PrintEntry |

**E8 is not a cell:** it is the round-8 walk's scope (the issuer's one real run at close): OVER WHAT expansion (UIR-17), a refusal state
(UIR-18, UIR-19; a fixture or a named refused account, read-only) and "About this scope" (UIR-22); UIR-50 grades when 2.0.0_SA_COO~M's
values land.

**Edges:** chain A runs first (CTO: E10 first, so the round's mechanical grades are trustworthy); chain H seats after IV-e-54 drains
(contracts/adapt.ts). Chain Z seats after H, P and V drain (it re-touches IdentityCard, slices.ts and HoldingsTreemap). X (IV-e-53) and
IV-e-56/57 both edit index.tsx: X drains before H seats. Chains P, V, N and X have no unmet dependency. E9's route is served
(2.0.0_SA_COO~P 101849). TO-IV-e-50 is superseded by IV-e-55 (CTO 101845). Every cell is `<risk>LOCAL</risk>` (local portal DEV only).
Seating waits on C: above 15 GB (0.0.0_AB_MSTR 101618; 14 GB at the cut).

**v8 addendum 1 (issuer, 2026-09-27 ~14:0xZ):** `IV-e-64`, the repair of IV-e-53's seam that row S23 grounds (window 12 K8 on local DEV
1f149d69; 2.0.0_SA_COO~P 101906): the preview now resolves, but the export SUBMIT (submit.ts:64-78, ExportButton.tsx:213) omits
`selectedTenant`, so the one POST /export answered UNAVAILABLE/UNEXPECTED (BucketUnmapped). Thread it into the submit, every receipt/status
read of the flow, and the download href. Same class as IV-e-36 and IV-e-53 (row-driven issuer repair of its own seam). Slot ~41, direct
act, LOCAL; export/submit.ts, ExportButton.tsx, ReceiptPanel.tsx belong to no running round-8 cell. Thread-breaking (the export hop).

**v8 addendum 2 (issuer, 2026-09-27 ~15:2xZ):** `IV-e-65`, the next export-hop repair that row S24 grounds (window 14 K8 on local DEV
55bbdd71; 2.0.0_SA_COO~P 101933): the POST now carries selected_tenant (S23 holds), but the export target names the report by its
revision hash (ReportingTab.tsx:214-228), so the renderer refuses 'invalid report reference'. Name it by retainedReport {reportId,
revision}. Direct act, LOCAL, slot ~36; ReportingTab.tsx belongs to no running round-8 cell. Thread-breaking (the export hop).

**v8 addendum 3 (issuer, 2026-09-27 ~16:4xZ):** `IV-e-66`, the Analysis-hop repair row S25 grounds (window 15 K10 on local DEV
e8a00b23): the owner history (IV-e-62) lists the READY job, but the per-request and report reads omit selected_tenant, so every row reads
'Status unavailable' and opening fails (200 UNAVAILABLE/UNEXPECTED). Thread the tenant into getOwnedAnalysisRequest /
getOwnedAnalysisReport and OwnedRequestHistory's reads. Direct act, LOCAL, slot ~36; no running cell holds these files. Carried to round 9:
a prospect job (no client) is invisible until a client is chosen (the history mounts only with a client).

**v8 addendum 4 (issuer, 2026-09-27 ~21:4xZ):** `IV-e-67`, row S26 re-routed to the page by 1.0.0_SA_CTO 102138 (R2 makes `data`
optional for QUEUED/RUNNING): a data-less QUEUED submit answer yields the exr_ id and starts the existing receipt poll until READY or a named
FAILED. Files: contracts/envelope.ts (data rule for submit-export/export-receipt), investor-reporting.ts submitExport, export/submit.ts,
ExportButton.tsx, ReceiptPanel.tsx. Direct act, LOCAL, slot ~41. The K8 re-run waits for this pin and P's kms:Decrypt grant.

## v9 -- round 9 (issuer, 2026-09-27 ~22:3xZ), over PRD v0.18 @5d44d0fa62 (ADMITTED; both halves current)

**Rectangle:** the ENRICHMENT LIST of 1.0.0_SA_CTO's round-N analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND8_20260927.md` @071e09aa18 (msg 102160), E1-E12, one cell
per item; the v0.18 UI CLEANUP FINDINGS ride E3-E8. E11 is TO-IV-e-67 (direct act, in flight); E12 is the round-9 walk's scope (no cell).
Write sets from the prep map `deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md` @51ec23d744; chains keep parallel sets disjoint:

| cell | item | rows | chain / slot | key files (IR = portal/src/pages/InvestorReporting) |
|---|---|---|---|---|
| IV-e-68 | E9 | W34-S1 (-> S7, W21-S2, W23-S1, W29-S10) | A ~34, 1 of 1 | IR/__tests__/fe-s-45/, s7-*.ts/json, S7_CLASS_TABLE |
| IV-e-69 | E6 | UIC-01/02/04/05/07/08/09 | P ~35, 1 of 1 | tabs/reporting/* (Headline, Chart, AccountsTable, Heatmap, ReportingTab, period, AnswerStatus, MethodAndSources), AccountFilter, StatusPanel, state/status |
| IV-e-70 | E4 | UIR-37, UIC-11 | H ~38, 1 of 3 | src/lib/chartColors.ts, holdings/palette, DrillTree |
| IV-e-71 | E2 | UIR-32/34/49 | H ~38, 2 of 3 | DrillTree, slices, HoldingsTab, src/components/CategoryViewTree.tsx (additive prop) |
| IV-e-72 | E7 | UIC-10/12/13 | H ~38, 3 of 3 | DrillTree, slices, SliceTable, header/IdentityCard |
| IV-e-73 | E1 | UIR-30 | N ~36, 1 of 1 | global/FirmAttribution, export/Preview |
| IV-e-74 | E5 | S25 diagnosis, UIC-23 | X ~39, 1 of 2 | tabs/analysis/OwnedRequestHistory |
| IV-e-75 | E8 | UIC-18..22, W35-S2 | X ~39, 2 of 2 | tabs/analysis/*, TabShell, index.tsx, export/ExportButton + submit |
| IV-e-76 | E10 | W35-S1 (UIR-04/13/30 labels) | Z ~40, 1 of 2 | header/firmDisplay + callers, adapt.ts, a generated module from infra/logic/registry/scopes.json |
| IV-e-77 | E3 | UIR-45, UIC-14, UIC-17 | Z ~40, 2 of 2 | PerformanceControls, PerformanceChart, PerformanceHeadline, slices, ScopeSummary, adapt.ts, format.ts |

**Edges:** A runs first (CTO: E9 first). P, H and A start now (disk: ~15 GB free, one pair ~2 GB). N and X seat when IV-e-67 drains (slot 41
frees; X's IV-e-75 also needs IV-e-67's ExportButton/submit). Z seats last, after P, H, N and X drain (it re-touches index.tsx, IdentityCard,
FirmAttribution, PerformanceHeadline/Chart, slices, adapt.ts) and after 1.0.0_SA_CTO commits the registry view target. Every cell is LOCAL.


**v9 addendum 1 (issuer, 2026-09-27 ~23:3xZ):** `IV-e-78`, row S27 (window 19 K8: the first export-receipt read answered data-less
UNAVAILABLE/NOT_READY and the page went silently idle). 1.0.0_SA_CTO 102222 ruled (b): the backend answers RUNNING while pending (to
2.0.0_SA_COO~P), and the page shows any refused or non-pending receipt read BY NAME (FWD-11), with no poll-on-UNAVAILABLE. One LOCAL direct act
on export/ExportButton + submit (+ ReceiptPanel/ExportModal if the slot needs it). It seats on the first slot to free (net-zero reuse) and
drains BEFORE IV-e-75, which writes the same two files.

**v9 addendum 2 (issuer, 2026-09-28 ~00:0xZ):** `IV-e-79`, row W36-S3: IV-e-73 (UIR-30) correctly hides FirmAttribution by default and flips five
pinned tests that asserted the tab-body chip (iv-e-23 firm-chip and parity-kept, iv-e-38 header-identity, iv-e-56 firm-display, fe-s-10 parity).
Issuer ruling: re-golden each to the ruled design, keeping its claim and a control that bites; the KEPT parity test's "never edited" line is
superseded by this ruling. One LOCAL direct act, tests only, on slot ~36 as queue position 2 (net-zero disk); IV-e-73 and IV-e-79 drain together.


## v10 -- round 10 (issuer, 2026-09-29 ~07:5xZ), over PRD v0.18 @5d44d0fa62 + the master brief Part VI

**Rectangle:** 1.0.0_SA_CTO 102636 ("cut AD-10..13 from STATUS.md as your next round"; FAST lapsed on presence 07:11Z).
The master brief `docs/briefs/irpt-master-guidance-brief-20260928.md` AD-10..AD-13, filtered by its own Owners lines:

| cell | item | rows | chain / slot | key files (IR = portal/src/pages/InvestorReporting) |
|---|---|---|---|---|
| IV-e-80 | AD-13 | UIC-17, UIR-45 (identity) | I ~42, 1 of 2 | IR/header/IdentityCard.tsx (+ pinned tests that assert the disclosure) |
| IV-e-81 | AD-11 | UIR-01's "Browse stays the listing" clause (superseded) | I ~42, 2 of 2 | IR/header/ClientSearch.tsx, IR/header/BrowseDrawer.tsx (+ pinned tests) |

**Not cut, named:** AD-10 (one masked tail per account) -- the page half waits on 2.0.0_SA_COO~M serving distinct account labels
(row IRPT_BCKEND-S182; every COT account reads "****8774 / UTMA" / "****9237 / BROKERAGE" at the producer); it is cut the tick ~M
names the served revision. AD-12 (a client the search offers must open) is owned by 2.0.0_SA_COO~P and ~M per the brief; no ~D cell.

**Edges:** one chain, one slot (~42), IV-e-80 then IV-e-81: both re-touch the header test pins (iv-e-38 and neighbours), so they run in
series on one worktree. Both are DIRECT-ACT (one cell each, well under 300 product lines, LOCAL); the close is the issuer's real run
on 5174. fanout: 1 of 1 chains, cap 8.


## v11 -- round 11 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~05:2xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's round analysis @10d7d46e49

**Rectangle:** the analysis's section 4 ENRICHMENT LIST, five items, one cell each. The lane is 2.0.0_SA_COO~D2 (analysis section 2), lease FULL.
Portal base for every portal cell: DEV tip `7bb81fa89792067bf90531371bcf0031a05f878c` (ls-remote after a fetch, 2026-10-11 ~05:1xZ).

| cell | item | rows | risk | chain / slot | key files (IR = portal/src/pages/InvestorReporting) |
|---|---|---|---|---|---|
| IV-e-82 | 1: the pinned three-run suite sample | S7, W21-S2, W23-S1, W29-S10, W34-S1 | LOCAL | A ~43 | the IR test scope, read-only |
| IV-e-83 | 2: S61 the Holding cell names the corrected security | S61 | SERVED | B ~46, 1 of 2 | IR/tabs/analysis/ProspectComposer.tsx (+ pins) |
| IV-e-84 | 3: S60 a test that presses "Did you mean" | S60 | LOCAL | C ~44 | IR/__tests__/dsgn-irptv1/ (test only) |
| IV-e-85 | 4: W35-S2 Export on the Analysis tab | W35-S2 | SERVED | B ~46, 2 of 2 | IR/tabs/analysis/AnalysisTab.tsx, the page header's Export |
| IV-e-86 | 5: the per-outcome state table | (none; the next analysis's input) | LOCAL | D ~45 | the PRD, the reviewer's files, the old lane's records |

**Edges:** IV-e-82, IV-e-84 and IV-e-86 are independent and start at once (analysis section 4). IV-e-83 waits on IV-e-82's baseline, then IV-e-85
follows it on the same slot and worktree pair: both touch the analysis tab and its pins. The two SERVED cells produce CANDIDATE portal commits; the
CTO reviews each product-file candidate before DEV (analysis section 2). W39-S2's served half is IRPT_ANLREQ's (row IRPT_ANLREQ-D2-S21); its page
half is a later round's and is NOT cut here.

**Rule 24:** no new enum is introduced by this round. The three closed sets in the checks (the ruling of a failing test id, the Export finding, the
outcome state) are the CTO's own, quoted from the analysis sections 3 and 4.

fanout: 3 of 4 chains at the cut (A, C, D), chain B after A; cap 8.


## v12 -- round 12 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~06:4xZ), over PRD v0.18 (ADMITTED), on 1.0.0_SA_CTO~DELL2's ruling msg 4198

**Rectangle:** one item. FWD-1 reads APPLIED in the round-11 state table: no whole signed-in trace exists. The CTO ruled no closer and one
trace cell under a never-widen pair for a READ-ONLY synthetic identity.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-87 | the DRAFT pair for one signed-in FWD-1 trace: hops and requests from the portal at the DEV tip, the ruled identity bounds, radius, branches, halves UNSIGNED | (none) | WORLD | A ~47 | the PRD's FWD-1, the TCKT_VNEXT R2-tr-1 pair (precedent), the portal's Investor Reporting client (read-only) |

**Not cut, named:** the trace RUN (after both halves sign; its executor is named in the pair); the page halves of W39-S2 and W35-S2, which wait on
IRPT_ANLREQ's rows D2-S21 and D2-S24 going live.

**Rule 24:** the check's closed sets (`writes_server_side`: true / false / NOT_ESTABLISHED; `repo_carries`) are measurement vocabularies local to
this cell's record, not a served enum.

fanout: 1 of 1 chains, cap 8.


## v13 -- round 13 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~07:1xZ), over PRD v0.18 (ADMITTED), on 1.0.0_SA_CTO~DELL2's rulings msg 4336

**Rectangle:** one item. The draft FWD-1 trace pair (IV-e-87) found the journey is not GET-only; the CTO withdrew that bound and ruled four points:
the trace makes the calls the page makes, no others, each named in the radius.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-88 | the pair revised to the four rulings (v2) and the runner at a pin: a POST allow-list of two routes, a 30-minute token cap, cleanup after exp, offline tests | D2-W47-S1, S2, S3 | WORLD | A ~48 | the draft pair and hops (~47), the TCKT_VNEXT runner (precedent, read-only), the portal's Performance loader (read-only) |

**Not cut, named:** the live reads owed at signing and both halves (the issuer and the CTO); the RUN order to the executor seat; the rendered
walk, a second act asked of the laptop's /ui-walk once the hops read clean (ruling 4).

**Rule 24:** no served enum is introduced; the runner's per-hop record vocabulary is the draft's `repo_carries`.

fanout: 1 of 1 chains, cap 8.


## v14 -- round 14 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~07:3xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ROUND-13 ANALYSIS @72e8e2bb59

**Round 13 is void:** its one order, IV-e-88 (the trace runner and pair v2), was SUPERSEDED before any work landed. The CTO's analysis dropped the
API-runner trace (an API trace does not grade FWD-1; the reviewer's answer, accepted) and withdrew msgs 4198 and 4338. The analysis calls its list
"round 13"; it is cut here as round 14 so no round number carries two issuances.

**Rectangle:** the analysis's section 4, five items. Item 1 (the FWD-1 rendered walk) is an ASK the managers carry to the laptop's /ui-walk, not a
cell. Items 2 to 5 are one cell each. Portal base: DEV tip `1cd1cf252eae0eee0d67cba4bde31630a71f975c`.

| cell | item | rows | risk | chain / slot | key files (IR = portal/src/pages/InvestorReporting) |
|---|---|---|---|---|---|
| IV-e-89 | 2: F40-AC5, the calendar derived from the one frontier | D2-W43-S3 | SERVED | A ~49, 1 of 3 | the portal's calendar data and its generator; fe-s-40 |
| IV-e-90 | 3: the 43-id table, two dispositions only | S7, W21-S2 (stay ARMED until dispositioned), the 14 refused labels | LOCAL | B ~50 | the suite sample and its logs, read-only |
| IV-e-91 | 4: the portal half catches up to the contract (18 ids) | D2-W43-S2 | SERVED | A ~49, 3 of 3 | IR routes table, envelopes, content pins |
| IV-e-92 | 5: bun from the environment; the press test off the private dispatcher; F47-AC6 | D2-W43-S1, D2-W44 (press), D2-W43-S3 | LOCAL | A ~49, 2 of 3 | IR tests and helpers |

**Edges:** every portal-editing cell runs in series on ONE slot and worktree pair (chain A), in the order calendar, test hygiene, contract
catch-up, so the candidates form one linear history on the DEV tip and each later cell's suite run stands on the earlier fixes. The table
(chain B) is independent and starts at once. The analysis lists items 2, 3 and 5 as independent; they are, but two portal branches cut from one tip
cannot both fast-forward, so 5 follows 2 on the slot.

**Not cut, named:** the page halves waiting on served fields (W39-S2 on IRPT_ANLREQ D2-S21; Export on IRPT_ANLREQ D2-S24; the correction kind on
IRPT_YCDGEN FWD-20); right-aligning the two dollar columns (D2-W46-S5: "in the next cell that touches the table").

**Rule 24:** the two dispositions of the 43-id table are the CTO's, quoted from the analysis section 2 item 2; the check refuses any third word.

fanout: 2 of 2 chains, cap 8.


## v15 -- round 15 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~07:5xZ), over PRD v0.18 (ADMITTED), on 1.0.0_SA_CTO~DELL2 msgs 4407 and 4427

**Rectangle:** one read-only item. The FWD-1 rendered walk ran on the laptop (portal DEV @ab697ba1) and broke at Performance on two refusals
(row DSGN_IRPTV1-D2-S7). OBJECT_NOT_COVERED is placed and ruled elsewhere (IRPT_BCKEND, 2.0.0_SA_COO~P2). The CTO asked for this cell "first in
round 14"; the issuance gate admits one issuance per round, so it is round 15. Round 14's four orders run unchanged.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-93 | the FIRM_BINDING refusal of the reporting summary and manifest placed at its emitting line; whether Global (All) is the cause; what an Opal user sees by default; whose defect; hop 7's two sentences side by side | D2-S7 | LOCAL | A ~51 | infra/aws/lambda (the reporting-read handler, _authz), the portal's Performance loader at ab697ba1, the walk record; read-only |

**Rule 24:** the record's answer sets (YES / NO / NOT_ESTABLISHED; SERVICE / PAGE / BOTH / NOT_ESTABLISHED) are measurement vocabularies local to
this cell, not a served enum.

fanout: 1 of 1 chains, cap 8.

## v16 -- round 16 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~09:2xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's retirement rulings msg 4446 and msg 4554

**Rectangle:** the round's repairs batched into ONE cell, on the table `deliverables/0.9.0_WK_DSGN_IRPTV1~50/FAILING_ID_TABLE.json`. Rounds 14
and 15 are drained (@b97b6ac14a, @6d3bb93153). At portal 7e8fa4fd (the contract catch-up, approved for DEV by msg 4554) the Investor Reporting
scope fails 20 of 1159 ids, against 43 at the baseline. The cell takes the ids this project owns outright; three items wait on another owner
and are named as deferrals, not cut.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-94 | the five git-diff arms on ModelPortfolios.tsx retired with the behavioural arms kept; the ycharts forbidden token retired with its duty; the explicit-null business_date arm decided from the contract's line; IVE116 and IVE137 re-pinned; the five absent-to-null coalesces in contracts/adapt.ts settled | D2-W43 family; D2-W49-S7, S8 (deferred) | SERVED | A ~52 (the slot's existing worktree pair) | portal/src/pages/InvestorReporting/ |

**Deferred, with owners:** the wire generator on empty-schema members (IVE26-AC3; IRPT_BCKEND); the smoke map pinned at 12 keys by two other
tests (row D2-W49-S8; the CTO rules which pin stands); `unprojected_grant` on two response schemas (row D2-W49-S7; IRPT_BCKEND).

**Not in this round, unchanged:** the page halves that wait on a served producer (history row client claim, Export on Analysis, the
correction kind), and the FWD-1 re-walk, which waits on IRPT_BCKEND IB-pr-421 and is the laptop's act.

**Rule 24:** the record's outcome words (DONE / STOPPED / DEFERRED; NULL_ADMITTED_REGRESSION / NULL_FORBIDDEN_RETIRED; ABSENT_CARRIED /
CONTRACT_ADMITS_NULL; ADDED / NOT_NEEDED) are measurement vocabularies local to this cell, not a served enum.

fanout: 1 of 1 chains, cap 8.

## v17 -- round 17 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~10:2xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ROUND-17 ANALYSIS @e4345abd6e

**Rectangle:** the analysis's ENRICHMENT LIST, section 4, items 1 to 4. Item 5 is the list's own exclusion: NOTHING is cut for the Performance
hop. Its source is ruled to be IRPT_BCKEND FWD-3's holdings-basis figure on the current Cottonwood feed (CTO msg 4705); IRPT_DASHBD FWD-11 for
the reporting read stays deferred. Rounds 14, 15 and 16 are drained. On portal DEV 3bf0d731 the scope fails 9 of 1,159 ids (issuer's run).

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-95 | list items 1 and 3, batched with the test-only repairs: the excused set pinned by name; the smoke map at 22 with two named excuses; the IVE115 and IVE69 stale goldens; newline-anchored pins | D2-W49-S9, D2-W49-S8, D2-W52-S3 | LOCAL | A ~53, first | portal/src/pages/InvestorReporting/ (tests and fixtures only) |
| IV-e-96 | list item 2: the Holdings face opens on the PICKED account's Models / SMAs / Client split (product; screenshots; candidate to the CTO) | D2-S7 (second half) | SERVED | A ~53, second | portal/src/pages/InvestorReporting/ |
| IV-e-97 | list item 4: the lock refreshed once on purpose; playwright-core declared or its skip stated; the calendar's provenance refused or carried as a claim | D2-W49-S3, S4, S1 | LOCAL | A ~53, third | portal/package.json, portal/bun.lock, portal/scripts/ |

The four list items are independent in content; they run in SERIES because every portal-editing cell shares the one portal slot and its
candidates must stay one linear history onto DEV.

**Owners for the three ids of row D2-W50-S1 (the issuer's ruling inside its own decomposition):** IVE17-AC3 clears with the content-pins
ids, owner IRPT_BCKEND (2.0.0_SA_COO~P2, row D2-W49-S7, placed by the CTO); the fe-s-1 smoke map is cell IV-e-95; IVE26-AC3 (the wire
generator on empty-schema members) is this issuer's, cut after IRPT_BCKEND states what the `report_index` members are, the same placement.

**Not in this round, unchanged:** the page halves that wait on a served producer (history row client claim, Export on Analysis, the
correction kind). The producer's smoke-map pin (`test_seam_paired.py`) is IRPT_BCKEND's file and is placed with 2.0.0_SA_COO~P2.

**Rule 24:** the records' outcome words (DONE / STOPPED / PLACED; DECLARED / SKIP_STATED; REFUSES_FALLBACK / CARRIES_CLAIM) are measurement
vocabularies local to these cells, not a served enum.

fanout: 1 of 1 chains, cap 8, reason: every portal-editing cell runs in series on one slot.

## v18 -- round 18 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~11:2xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ruling msg 4798

**Rectangle:** one cell, handed to this project by ruling: the portal's generated wire folder is regenerated WITH its consumers. A sibling
workstream (IRPT_ANLREQ AR-y-42) regenerated the folder and stopped on 13 type errors and dropped hand-added exports; its portal branch
`wk-IRPT_ANLREQ-51-portal-r4` @890f1d0f3d is the input, and rows IRPT_ANLREQ-D2-W51-S6 (BLOCKING) and -S7 move here with it.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-98 | a generated folder holds generator output and nothing else: each hand-added export emitted by the generator or moved outside; one command runs gen-wire and gen-consumed; the drift test covers both; the consumers fixed at their cause; IVE26-AC3 | IRPT_ANLREQ-D2-W51-S6, S7; DSGN_IRPTV1-D2-W50-S1 (IVE26-AC3) | SERVED | A ~54, behind IV-e-96 | portal/src/pages/InvestorReporting/contracts/, portal/scripts/ |

**Order on the one portal slot (the issuer's ruling):** IV-e-96 (running) -> IV-e-95 part 2 under AMENDMENT 3 (the map at 16) -> IV-e-98 ->
IV-e-97. IV-e-98 goes before the tooling cell because the CTO placed it "behind the Holdings face" and IV-e-97's lock refresh is easier to
prove byte-equal on a settled tree.

**Also owned here now, not cut:** the portal readers that refuse five valid producer fixtures (row D2-W53-S4; record
`deliverables/2.0.0_SA_COO~D2/FIVE_FIXTURES_VS_CONTRACT_20261011.md`): cut on the CTO's word.

**Rule 24:** the record's outcome words (GENERATOR_EMITS / MOVED_OUTSIDE; FIXED / NOT_FIXED) are measurement vocabularies local to this
cell, not a served enum.

fanout: 1 of 1 chains, cap 8, reason: every portal-editing cell runs in series on one slot.

## v19 -- round 19 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~11:3xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ruling msg 4806

**Rectangle:** one cell, urgent. irpt-status release 5 is rolled back because the portal's history reader admits exactly two keys and the
release's answer carries a third; the release returns only after the reader admits the contract's members, on PROD.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-99 | the history reader admits BOTH answers the service can serve (two keys; the contract's answer with unreadable_rows and the per-item client_id / client_claim) and refuses anything else; members carried, nothing new rendered | D2-W53-S4 (history) | SERVED | B ~55, its OWN portal worktree | portal/src/pages/InvestorReporting/contracts/owned-requests.ts |

It runs BESIDE the portal slot's chain (IV-e-96 -> IV-e-95 part 2 -> IV-e-98 -> IV-e-97): it touches no file the Holdings change touches,
and it lands on DEV first; the slot's next candidate merges DEV under it as every candidate has. The other four refused readers (row
D2-W53-S4) are not cut: the CTO rules that cell after 2.0.0_SA_COO~P2 reads the live shapes.

**Rule 24:** the record's words are booleans and lists local to this cell; no enum is minted. `client_claim`'s enum is the contract's.

fanout: 2 of 2 chains, cap 8.

## v20 -- round 20 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~12:1xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ruling msg 4872

**Rectangle:** one read-only cell. Round 19's history reader is on portal DEV (8ed372cb) and waits on Andrew's word for PROD. Before the
service release returns, the CTO wants every portal reader of that service listed with how strictly it reads.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-100 | the census: every irpt-status route the portal reads -- reader (file:line), key policy per level (EXACT / TOLERANT), release 5's answer PASS or the refusing member, at portal PROD 37aa1247ee and at DEV's tip; the sections reader and the single-request reader included; the routes that join the PROD push | D2-W53-S4, D2-W55-S1; IRPT_YCDGEN-W2-S13, W6-S4 | LOCAL | B ~56, the second worktree pair, read-only | portal/src/pages/InvestorReporting/contracts/, infra/aws/lambda/investor-reporting/ |

**What it feeds:** a build cell per reader that refuses at PROD (the CTO's order of return: every such reader on PROD first, then the
service). The sections reader admitting the Opal form (IRPT_YCDGEN round-11 analysis, section 4 item 3) is expected to be one of them; it
is cut from this cell's rows, not before. Row IRPT_YCDGEN-W3-S21 (the suite leaves four tracked wire files modified) is taken into IV-e-98.

**Rule 24:** EXACT / TOLERANT is one axis (what an unknown key does at one level) with two values and no third; PASS / REFUSES /
NOT_ESTABLISHED is one axis (what the reader does with one answer). Both are measurement vocabularies local to this cell.

fanout: 2 of 2 chains, cap 8.

## v21 -- round 21 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~13:1xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's rulings msg 4924 and msg 4958

**Rectangle:** two page cells handed to this project by ruling, from IRPT_YCDGEN's journey read (hop 12). IRPT_YCDGEN's FWD-1 waits on
them; the CTO asks Andrew for the sitting when both are on DEV, and put them AHEAD of the wire-folder regeneration.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-101 | an Opal report opened on the page prints no vendor wording ("Vendor attribution", "Extraction validation"); a vendor report is unchanged | IRPT_YCDGEN-D2-W14-S1 (related W4-S8) | SERVED | B ~57, a second worktree pair, first | portal/src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx, NativeSections.tsx, contracts/adapt.ts |
| IV-e-102 | the report can be opened after a Prospect upload: a rendered read first, a fix only if the read says so | IRPT_YCDGEN-D2-W14-S2 (inferred) | SERVED | B ~57, second | portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx |

**"Ahead of" on a slot that is already running (the issuer's ruling):** IV-e-98 has been running on the one portal slot since ~12:40Z.
Stopping it mid-regeneration loses its work, so these two run in a SECOND portal worktree and land on DEV first; IV-e-98's candidate then
merges DEV under itself, as every candidate has. If the two touch a file the regeneration also touches, the merge is resolved in IV-e-98's
candidate, not here.

**Queued, not issued** (carrier: `deliverables/2.0.0_SA_COO~D2/SLOT_QUEUE_20261011.md`): the smoke map takes the two routes whose producer
fixtures 2.0.0_SA_COO~P2 corrected @d8fb17b6d5 (msg 4959), and the five ids that waited on `unprojected_grant` in four response schemas are
re-run (same commit); the 130% weight (row D2-W53-S7); the contract-exact history reader (after release 5 returns).

**Rule 24:** the records' words (FIXED / NOT_A_DEFECT / STOPPED; RENDERED) are measurement vocabularies local to these cells.

fanout: 2 of 2 chains, cap 8.

## v22 -- round 22 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~14:4xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2 msgs 5037, 4992, 4888 and 4864

**Rectangle:** what the CTO named for "your next issuance", with the repairs batched into ONE cell. All three run in series on the one
portal slot (worker ~58); IV-e-102 (round 21) runs beside them in the second worktree pair.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-105 | the print and export document of an Opal report prints no vendor wording; every print or export surface listed by subtraction; a vendor document unchanged | D2-W57-S2 | SERVED | A ~58, first (Andrew's sitting may export) | portal/src/pages/InvestorReporting/tabs/analysis/AnalysisDocument.tsx and the surfaces that import it |
| IV-e-104 | ONE batched repair cell: the smoke map takes the two routes whose producer fixtures were corrected; the five ids that waited on the response schemas re-run; IVE26-AC3's third arm derived, not a literal; IV-e-97's flip | D2-W53-S4, D2-W54-S1, D2-W53-S10 | LOCAL | A ~58, second | portal/src/pages/InvestorReporting/ (tests and fixtures only) |
| IV-e-103 | the 130% weight on a two-account client's unpicked Holdings view: a read first (the fixture or the page's denominator), a fix only if it is the page | D2-W53-S7 | SERVED | A ~58, third | portal/src/pages/InvestorReporting/tabs/holdings/ |

**Not cut, and why:** the portal's renderer set lacking the contract's new reason REPORT_TICKET_MISMATCH (test F40-AC7 red since trunk
@359da3005f) -- 2.0.0_SA_COO~Y2 lands its own regeneration of render/Page.tsx as a candidate (CTO msg 5135; Y2 msg 5138), and no deployed
function serves the code. The contract-exact history reader waits on release 5's return. The custody readers wait on a page that calls them.

**Rule 24:** the records' verdict words (PAGE_DEFECT / FIXTURE_DEFECT / NOT_ESTABLISHED; FIXED / NOT_FIXED; PASS / FAIL) are measurement
vocabularies local to these cells.

fanout: 1 of 1 chains on the slot, cap 8.

## v23 -- round 23 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~17:0xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ROUND-23 ANALYSIS @b417e9ee3c

**Rectangle:** the analysis's ENRICHMENT LIST, section 4, thread-breaking first. Three items are cells; item 2 is the issuer's own document.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-106 | item 1: ONE PROD candidate record, pushed by nobody -- the exact commit, every changed file assigned to a page with its class, the two missing irpt-status reads stated, and `retained_ref` carried by the sections reader | D2-W56-S3, D2-W56-S2 | SERVED | A ~59, first | portal/src/pages/InvestorReporting/contracts/adapt.ts |
| IV-e-108 | item 3: the Holdings face names the picked account and labels each total with its base; the header's picker hands the tabs the picked account | D2-S14, D2-W53-S5 | SERVED | B ~60 | portal/src/pages/InvestorReporting/tabs/holdings/, header/ |
| IV-e-109 | item 4: hygiene -- the raw NUL byte out of a test file; the smoke-map generator keeps the tracked request fixture's `_captured`; `scripts/ui-smoke.mjs` can pick a client | D2-W53-S2, D2-W53-S8, D2-W53-S6 | LOCAL | A ~59, second | portal test, generator and script files only |

**Item 2, no order:** the ask for the laptop's rendered walk of DEV is a document this seat writes
(`deliverables/2.0.0_SA_COO~D2/LAPTOP_WALK_ASK_20261011.md`) and hands to 0.0.0_AB_MSTR~DELL2 to carry MSTR to MSTR; it names the faces
and what each must show.

**Not cut, and why:** whether a served holdings answer can carry a sleeve with no security beneath it is IRPT_BCKEND's read (CTO msg
5374, row D2-S18); the page's sentence for unlisted sleeves, or the fixture's repair, follows its answer. The Opal wording on a served
report is read at Andrew's sitting (rows D2-S16, D2-W58-S4, D2-W57-S3). Row D2-W58-S3 is ruled kept as supplied.

**Rule 24:** `class` on a page takes two values over the declared domain "every page a changed file belongs to": CLIENT_FACING or
OPAL_INTERNAL, one grain (the page), one intent (who can open it), and unsure resolves to CLIENT_FACING, which the push law states. The
other verdict words (CARRIED / NOT_CARRIED; PASS / FAIL) are measurement vocabularies local to these cells.

fanout: 2 of 2 chains (slot A, slot B), cap 8.

## v24 -- round 24 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~17:2xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ruling msg 5447

The CTO placed this cell "in round 23, beside the Holdings labels". Round 23's one issuance was already made (@bc7b3f4544), so it is
issued as round 24 and runs on the same slot after IV-e-108.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-110 | when the listed securities sum to less than the total card, the Holdings table says in a sentence how much sits in sleeves it does not itemise, and names the producer's two reasons (cash only, or detail withheld); absent when the rows sum to the card | D2-S18 | SERVED | B ~60, after IV-e-108 | portal/src/pages/InvestorReporting/tabs/holdings/ |

The producer is not changed (withholding a drill is its rule). The fixture was honest: IRPT_BCKEND's read found the shape in a served
answer (2.0.0_SA_COO~P2 msg 5438, relayed in the ruling; not re-read by this seat).

fanout: 1 of 1 chains, cap 8.

## v25 -- round 25 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~17:5xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ruling msg 5494

IV-e-106's record showed the PROD-to-DEV range is not this project's alone (67 of 127 commits are other projects', on pages partner
firms can open), and that the Investor Reporting route on PROD is behind admin, the Opal firm and user type Dev while the print route
admits a render claim. The CTO ruled the whole range out and ordered ONE cut.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-111 | ONE candidate cut off portal PROD holding only what release 5's return needs: the history reader, the two missing irpt-status reads, `retained_ref`; every changed file under src/pages/InvestorReporting or the one endpoints file; none in the print route's import closure, shown from the build's chunk graph, or the candidate waits on Andrew | D2-W56-S2, D2-W56-S3, D2-W59-S2 | SERVED | C ~61 (a third worktree pair, its portal half at PROD with its own install) | portal/src/pages/InvestorReporting/contracts/, portal/src/api/endpoints/investor-reporting.ts |

"CI green" (the ruling's third condition) is read on the candidate's own branch after the worker returns; a worker cannot push. The
record `PROD_CANDIDATE.json` of IV-e-106 stands as the census of the whole range and is not re-pointed.

**Rule 24:** `verdict` takes CLEAR or WAITS_ON_ANDREW over the declared domain "candidates whose print closure was computed with a found
control": one grain (the candidate), one intent (may it go without his word), and the one remedy that moves it is removing the file from
the candidate or from the closure.

fanout: 1 of 1 chains, cap 8.

## v26 -- round 26 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~18:4xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ruling msg 5562

The laptop's rendered walk on a served answer (XB-c5ce) produced rows D2-S21, S22 and S23. The CTO ruled all three, S22 first.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-112 | the reads the walk saw refused with FIRM_BINDING: each traced to its reader and its face; every such face states the refusal in words | D2-S22 | SERVED | A ~62, first | portal/src/pages/InvestorReporting/dashboard/reportingRead.ts and the faces it feeds |
| IV-e-113 | an opened vendor report reads section codes for titles and "Unit: unknown": page or producer, traced through the contract, the producer's fixture and code, and the adapter; a read | D2-S21 | LOCAL | A ~62, second | portal/src/pages/InvestorReporting/contracts/adapt.ts (read only) |
| IV-e-114 | one hygiene cell on the Holdings tab: the React colgroup warning, the low-contrast eyebrow text, the navy bands counted against the design law's clause | D2-S23 | SERVED | A ~62, third | portal/src/pages/InvestorReporting/tabs/holdings/ |

**Not a cell:** which three reads were refused, as what user type and with which firm selected, is asked of the walker from its saved
evidence (carried by 0.0.0_AB_MSTR~DELL2, msg to it at ~18:3xZ); the CTO tells Andrew before he sits if an internal user with a firm
selected is refused.

**Rule 24:** `verdict` in IV-e-113 takes PAGE, PRODUCER, BOTH or NOT_ESTABLISHED over the declared domain "where a missing title or unit
originates": one grain (the member), one intent (who fixes it); BOTH is a member, not an escape, and NOT_ESTABLISHED names the missing read.

fanout: 1 of 1 chains on slot A, cap 8.

## v27 -- round 27 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~19:4xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2's ruling msg 5664

IV-e-113's read returned BOTH for row D2-S21: the vendor section's title never reaches the wire, and the page maps none of the 12 unit
tokens the producer sends. The CTO ruled both are the page's to fix now, with no schema change.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-115 | the page maps a vendor section's code to its census name (33 names copied from the pinned census, source recorded, a drift test) and maps the producer's 12 unit tokens; an unmapped code or token prints itself, never "unknown"; the page's fixtures send real tokens; an Opal report unchanged | D2-S21, D2-W62-S1 | SERVED | B ~63 | portal/src/pages/InvestorReporting/contracts/adapt.ts and a new names module |

Still open on row D2-S21 and not cut: the missing validation line and source line of a vendor report. A wire title is noted for the
producer's next release (IRPT_BCKEND's). 2.0.0_SA_COO~P2 is asked for one owner read confirming both on a served answer.

fanout: 1 of 1 chains, cap 8.

## v28 -- round 28 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~21:0xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2 msg 5782

IV-e-115 is on portal DEV (1bf9e1f3). Its screenshot showed several cards of one section reading the same title and the same Label
(row D2-W63-S2); the CTO named the next cell.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-116 | a vendor card whose Label equals its title prints the title once; a differing Label and an Opal card unchanged; and a READ (no product change) of whether the wire's section id carries a field slug the pinned census can name exactly | D2-W63-S2 | SERVED | B ~64 | portal/src/pages/InvestorReporting/contracts/adapt.ts, tabs/analysis/NativeSections.tsx |

The proof of IV-e-115 on a served vendor report is asked of the laptop's walker
(`deliverables/2.0.0_SA_COO~D2/LAPTOP_WALK_ASK_2_VENDOR_REPORT_20261011.md`, carried by 0.0.0_AB_MSTR~DELL2).

fanout: 1 of 1 chains, cap 8.

## v29 -- round 29 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~22:1xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2 msg 5852

IV-e-116 is on portal DEV (ad774c6f9e, CI success, 0.0.0_AB_MSTR~DELL2 receipt msg 5950). The CTO ruled row D2-W62-S3: a navy-filled
strip breaks C3; the shared components are not this project's to restyle; one cell is inside the grant.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-117 | the Holdings tab passes PanelFooter its light ground (the prop exists on the shared component, which is not changed), removing the navy footer strips; contrast measured; the three header strips stay and go to the design system's owner | D2-W62-S3 | SERVED | B ~65 | portal/src/pages/InvestorReporting/tabs/holdings/ |

fanout: 1 of 1 chains, cap 8.

## v30 -- round 30 (issuer 2.0.0_SA_COO~D2, 2026-10-12 ~02:3xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2 msg 6344

The proof walk of a served vendor report came back (laptop 4.0.0_SA_CRO, portal DEV 0a06280a; the issuer's read
`deliverables/2.0.0_SA_COO~D2/WALK_2_RESULT_READ_20261012.md` @7db8985b06). IV-e-115's names and units are proven on served data.
The CTO's list, in order, three items; the third is carried, not cut.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-118 | a page never prints an unmapped code as a title: where the census names nothing the card takes its section's name; the word for the chart row is proposed and lands in the census | none | SERVED | B ~66 | portal/src/pages/InvestorReporting/contracts/vendorSectionNames.ts; the census file |
| IV-e-119 | a READ, no build: for the 46 cards sharing one title, does section_id through the census give distinct names, and how many stay shared (all separate: the build is the page's; else the remainder is a wire member for 2.0.0_SA_COO~P2) | none | LOCAL | A ~67 | none edited |

Carried, not cut this round (CTO msg 6344 item 3): the validation line and the source line on the report's face.

fanout: 2 of 2 chains, cap 8.

## v31 -- round 31 (issuer 2.0.0_SA_COO~D2, 2026-10-12 ~22:2xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2 msg 6625

The CTO's round-31 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_31_20261012.md` @5f3be4e3da)
answers the rounds 24-30 slug (REMEDIATION_v10). Its list has six items; the issuer re-measured the base before cutting
(row `DSGN_IRPTV1-D2-S27`): items 1, 2 and 5 are already satisfied on portal DEV 183860bac055 and are not cut. Three cells remain.

| item | state at the base | cell |
|---|---|---|
| 1 wire regeneration (W65-S1) | satisfied: iv-e-98 and iv-e-26 pass, 0 of 28 wire files differ | not cut |
| 2 colgroup text nodes (W62-S2) | satisfied: portal eba86eaf (TO-IV-e-114) removed them | not cut |
| 3 Total Assets base inside the card (W60-S1) | open: the base is a caption above the card (HoldingsTab.tsx:436) | IV-e-120 |
| 4 Account select from the header's pick, rendered (S24) | open: no rendered walk of an ACCOUNT row | IV-e-121 |
| 5 the unavailable answer's face (S22) | satisfied for FIRM_BINDING: ReportingTab.tsx:438-462 (IV-e-112), read on a served Cottonwood client | not cut |
| 6 the vendor report's validation and source line (S21) | open: carried since round 30 | IV-e-122 |

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-120 | the Total Assets base sits inside the card, drawn by the shared CategoryViewTree (an optional prop; the caption above the card goes); every page that mounts the tree is rendered before and after (census from the module graph, denominator printed) with no visible change outside the Holdings tab | D2-W60-S1 | SERVED | A ~68 | portal/src/components/CategoryViewTree.tsx; tabs/holdings/ |
| IV-e-121 | an ACCOUNT row picked in the header starts Performance's Account select on that account and Holdings opens on it, proven on a RENDERED page; the record says which row kind the header yields for a last-four search | D2-S24 | SERVED | B ~69 | tabs/reporting/, header/ |
| IV-e-122 | the vendor report's face carries the validation line and the source line from the wire's extraction_validation (status, checks_run, checks_failed, notes); an Opal report unchanged | D2-S21 | SERVED | C ~70 | tabs/analysis/NativeSections.tsx and its reader |

The three write sets are disjoint (a shared hookup is the issuer's at the drain). The CTO's first condition on the shared file
was read: no live order's `<paths>` names `portal/src/components/CategoryViewTree.tsx` (MDPF_TAXSMA TO-TX-c-2 narrowed off it
at its Amendment 1; TO-TX-v-3 only reads it). The second condition, the census with a rendered before and after, is IV-e-120's
own criterion.

fanout: 3 of 3 chains, cap 8.

## v32 -- round 32 (issuer 2.0.0_SA_COO~D2, 2026-10-12 ~23:4xZ), over PRD v0.18 (ADMITTED; no addendum), on 1.0.0_SA_CTO~DELL2 msg 6671

The round-31 candidate landed on portal DEV as cf52fdbf00f2 (0.0.0_AB_MSTR~DELL2 receipt msg 6669, CI success); the CTO's round-32 analysis
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_32_20261012.md` @933fc4d8f7) answers the round-31 slug (REMEDIATION_v11).
Its list: items 1 and 2 below; item 3 (rows D2-W60-S1 and D2-S21 close when the candidate lands) is satisfied by that landing and needs no cell.
The vendor-name question (row D2-W70-S2) is held for Andrew; the view keeps adding no provider. The account-pick start (row D2-W69-S1) is the producer's entry kind,
routed to IRPT_BCKEND ~P.

| cell | item | rows | risk | chain / slot | key files |
|---|---|---|---|---|---|
| IV-e-123 | one read of the holdings producer: is an ACCOUNT node's id equal to the account id on every served path (denominator printed); where it is not, the page maps the node ref to the account id before the focus post (a product change only then) | D2-W69-S2 | SERVED | A ~72 | tabs/holdings/ (read: infra/aws/lambda/investor-reporting/holdings/) |
| IV-e-124 | the unsupported-card reason on an UNCERTIFIED vendor report is a plain sentence in the register of the face's one validation sentence, with no producer status word; an Opal report unchanged | D2-W70-S4 | SERVED | B ~73 | tabs/analysis/NativeSections.tsx |

The two write sets are disjoint (a shared hookup is the issuer's at the drain).

fanout: 2 of 2 chains, cap 8.
