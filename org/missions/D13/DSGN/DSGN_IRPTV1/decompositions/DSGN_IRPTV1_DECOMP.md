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
