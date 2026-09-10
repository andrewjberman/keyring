# IRPT_FNTEND -- L5 decomposition -- round 1 -- v0.1

```json
{
 "project": "IRPT_FNTEND",
 "directive": "D9",
 "fabric": "laptop",
 "round": 1,
 "decomp_version": "v0.1",
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@62301f71e0",
 "prd_version": "v0.4",
 "brief_ref": "docs/briefs/investor-reporting-ir-fe-brief-20260910.md@2acf23d8fd",
 "endpoint_outcomes": ["FWD-1", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-8", "FWD-11", "FWD-12"],
 "cells": 11,
 "cell_id_shape": "FE-s-<n>",
 "code_repo": "portal (nested git repo, gitlink in the workspace; branch DEV @5907cbca)",
 "record_repo": "workspace (branch CLOUD @62301f71e0)"
}
```

The PRD's fourteen cell candidates are re-cut into eleven cells over three write surfaces. Every candidate maps to exactly one cell (section 3). The counterpart's routes do not exist at this cut; every cell builds and proves against a fixture adapter that implements the same typed interface the live client will, so a live route is a configuration change and never a code change.

---

## 1. THE RECTANGLE -- eleven cells over the PRD's surface manifest

**Cell status vocabulary** (adopted, not minted; the estate's decompositions already carry it and its four-postulate record):
`NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`. At this cut all eleven read `OPEN`; **11 of 11 evaluated, 0 NOT-EVALUATED.**

| cell | write surface | serves | PRD candidates | wave | slot |
|---|---|---|---|---|---|
| `FE-s-1` | `portal/src/api/endpoints/investor-reporting.ts`; `portal/src/pages/InvestorReporting/contracts/`; `portal/src/pages/InvestorReporting/fixtures/` | FWD-1, FWD-6 (contributes to FWD-2) | F12, F14 | A | ~1 |
| `FE-s-2` | `portal/src/App.tsx` (route + nav lines only); `portal/src/pages/InvestorReporting/index.tsx`; `.../header/` | FWD-1, FWD-11, FWD-12 | F1, F2 | B | ~1 |
| `FE-s-3` | `portal/src/pages/InvestorReporting/tabs/`; `.../state/` | FWD-1, FWD-6 | F3, F7 | C | ~1 |
| `FE-s-4` | `portal/src/pages/InvestorReporting/render/` (the RenderPackage); `portal/src/App.tsx` (print route line only) | FWD-3, FWD-4, FWD-8, FWD-12 | F9 | B | ~2 |
| `FE-s-5` | `portal/src/pages/InvestorReporting/tabs/reporting/` | FWD-3 | F4 | D | ~1 |
| `FE-s-6` | `portal/src/pages/InvestorReporting/tabs/analysis/` | FWD-4 | F5 | D | ~3 |
| `FE-s-7` | `portal/src/pages/InvestorReporting/tabs/holdings/` | FWD-5 | F6 | D | ~4 |
| `FE-s-8` | `portal/src/pages/InvestorReporting/render/narrative/` | FWD-8 | F10 | C | ~2 |
| `FE-s-9` | `portal/src/pages/InvestorReporting/export/` | FWD-8, FWD-4 | F8 | E | ~1 |
| `FE-s-10` | `portal/src/pages/InvestorReporting/global/`; edits inside `header/`, `tabs/`, `export/` | FWD-11 | F11 | F | ~1 |
| `FE-s-11` | `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/` (the census, the review, the screenshots); no portal write | FWD-12 | F13 | G | ~1 |

**Surface manifest coverage (PRD section SURFACE MANIFEST, 8 rows):** `pages/InvestorReporting/` -> cells 2-10; `api/endpoints/investor-reporting.ts` -> cell 1; the rendering package -> cells 4, 8; `App.tsx` edit -> cells 2, 4 (two line-scoped edits, no other change to that file); every IV.2 reuse path -> import-only in cells 2-10, read in cell 11; brand sources -> read in cells 4, 11; the counterpart's `/api/scoped/investor-reporting/` routes -> the typed client's target in cell 1, unreachable at this cut; the excluded row (no vendor session, cookie, model join, news retrieval, email parser) -> a bound on every cell. **8 of 8 rows covered.**

---

## 2. THE CELLS

Every cell inherits these bounds. They are stated once here and inlined into every worker face at L6.

```
BOUNDS -- ALL CELLS
  repo        code lands in the portal repo on a branch cut from DEV; records (proof-of-spec
              instance, result file, surprise rows) land in the workspace repo. Never PROD.
  data        the browser consumes the ten contracts through the typed client in FE-s-1 and
              nothing else: no vendor session, no vendor cookie, no model join, no news
              retrieval, no email parsing, no recalculation of any return, no parsing of a
              raw provider hierarchy, no inference of gain from ending minus beginning value,
              no averaging of account returns, no missing value rendered as zero.
  vendor      NO LIVE VENDOR CALL. Every fixture is a file under fixtures/.
  numbers     no latency target, TTL, retry count or width is an acceptance value; the two
              viewports named below are test setups taken from the sketch's evidence file.
  reuse       the IV.2 paths are imported, never edited; the ONLY edited shared file is
              portal/src/App.tsx, and only the route and nav lines named in FE-s-2 / FE-s-4.
  keys        every react-query key is namespaced ['investor-reporting', <op>, tenant,
              scopeFingerprint, revision, ...params]; a client name is never a key.
  states      LOADING READY STALE PARTIAL UNAVAILABLE RETRYABLE UNCERTAIN NEEDS-CORRECTION
              FAILED render from StatusEnvelope; an unknown classification is an explicit
              unknown, never false and never Client.
  a11y        every chart has a table equivalent; every control is keyboard reachable.
  colour law  no light text or light button directly on the silver canvas (portal/CLAUDE.md).
  tests       mechanical proof runs under `bun test` (bun 1.3.9, built-in runner; no vitest
              is installed and none is added) and `bun run typecheck`; renders are proven
              with `node scripts/ui-smoke.mjs <route> <png> --port <port> --fixtures <json>`
              at viewports 1440x1200 and 390x844.
  surprise    anything outside the cell is ONE ROW in
              org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v1.md
              and the cell keeps going.
```

### `FE-s-1` -- contracts, typed client, fixture adapter, consumer fixtures

```
ACT       Define the ten consumed contract types (DirectoryEntry, ResolvedScope,
          PerformanceReport, AnalysisRequest, AnalysisReport, HoldingsSnapshot,
          NarrativePacket, ExportBundle, ExportReceipt, StatusEnvelope) from the field sets in
          org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md CONTRACTS section @62301f71e0,
          each carrying schemaVersion, scope, revision, availability and source timestamps.
          Build the typed client at portal/src/api/endpoints/investor-reporting.ts on the
          conventions of portal/src/api/endpoints/market.ts and portal/src/api/portal-proxy.ts,
          targeting /api/scoped/investor-reporting/<op>, behind an interface
          InvestorReportingApi. Build a FixtureAdapter implementing the same interface over
          fixtures/*.json, selected by one configuration value. Build the consumer fixture set:
          for each of the ten contracts one success and one failure fixture, plus the named
          negatives: duplicate client names, account-only entry, multiple relationships,
          terminated-but-entitled client, partly authorized relationship, swapped ids, revoked
          grant against a warm cache, partial scope, differing returned dates, unavailable
          metric, unknown cohort. Build the query-key builder and the response-handling rules:
          a 401/403 or a revocation state clears every cached protected result for that scope;
          telemetry carries operation, revision and public reason code and never a client
          payload, cookie, raw provider id or infrastructure diagnostic.
SERVES    FWD-1 (permitted set, as-of, zero-vendor-request path), FWD-6 (states, as-of,
          revision); the refusal-handling half of FWD-2.
CROSSES   the producer fixtures and field meanings are the counterpart's; a contract change
          without a matching producer fixture is refused at this seam.
PROOF     bun test on: key builder (namespace, tenant, fingerprint, revision present; a
          client name absent); adapter parity (live client and fixture adapter satisfy one
          interface, checked by a type-level test); revocation clears protected cache;
          telemetry redaction (a fixture response containing a cookie header and a provider
          id yields telemetry containing neither). bun run typecheck rc 0. Fixture census:
          10 contracts x 2 = 20 base fixtures plus 11 named negatives = 31 files, denominator
          printed by a test that lists fixtures/.
```

### `FE-s-2` -- route, page shell, header, firm dropdown, client search

```
ACT       Add the lazy route /investor-reporting in portal/src/App.tsx beside /portfolios,
          following the existing lazy(() => import(...)) and <ProtectedRoute> lines, and its
          nav entry; distinct from /advisor-intelligence and /positioning. Build
          pages/InvestorReporting/index.tsx from PageHeaderCleanBadge
          (portal/src/components/PageHeaderVariants.tsx), PageSurfaceControl as="dropdown"
          (portal/src/components/ui/PageSurfaceControl.tsx) with the option shape
          portal/src/pages/ModelPortfolios.tsx uses ({ id: 'global', name: 'Global (All)' }
          plus the partner firms), the catalyst combobox
          (portal/src/ui/components/catalyst/combobox.tsx) with the option and virtual-list
          conventions of ClientListPanel.tsx for name/account search over DirectoryEntry, and
          the panels under portal/src/ui/components/panels/. The header shows: the selected
          client, relationship or account; the permitted account population with a useful
          discriminator; scope and directory as-of dates; a TERMINATED marker with actual
          available dates; an explicit capability gap for an unmapped client; cohort controls
          only when DirectoryEntry marks the classification authoritative. Account selection
          narrows the relationship. The firm dropdown renders only when
          ResolvedScope.permittedFirms has more than one entry; isInternal() is a rendering
          hint and never a permission.
SERVES    FWD-1, FWD-11 (the selector), FWD-12 (header, dropdown, search are the portal's own).
DEPENDS   FE-s-1.
PROOF     ui-smoke of investor-reporting at both viewports with the directory fixture: the
          header, dropdown and search render; LOC equals the route. bun test on: search over
          the duplicate-name fixture returns two distinct options with discriminators; an
          account-only entry resolves to its relationship with the account narrowed; a
          terminated entry renders TERMINATED with its dates; an unmapped entry renders with a
          capability gap and is not filtered out; the fixture adapter's request log during 25
          keystrokes shows 0 provider-shaped calls; the dropdown is absent when permittedFirms
          has one entry. bun run typecheck rc 0. The App.tsx diff touches only the import,
          route and nav lines (git diff --stat names one file; the hunks are enumerated).
```

### `FE-s-3` -- tabs, selection persistence, scope-switch clearing, lifecycle states

```
ACT       Mount TabNavigation + useTabNavigation (portal/src/components/TabNavigation.tsx,
          portal/src/hooks/useTabNavigation.ts) with tabs Reporting, Analysis, Holdings.
          Build state/selection.ts: the current selection is (firm, scope, revision); a
          response is applied only when its (scope, revision) equals the current selection at
          arrival; a scope switch clears the prior selection's protected content synchronously
          before any fetch starts and marks outstanding requests stale. Build
          tabs/StatusPanel.tsx rendering StatusEnvelope into the nine states with the source
          age, the safe next action and the public reason code; a failed Analysis job leaves
          Holdings and search usable; a stale model map keeps old assignments labelled with
          their as-of; an over-age directory or a revoked grant renders what the envelope says
          even when a cached result exists; an incomplete result never renders as a complete
          zero-valued report.
SERVES    FWD-1 (choice survives a tab switch), FWD-6.
DEPENDS   FE-s-2.
PROOF     bun test on: selection survives tab change; a late response for a previous
          selection is dropped (out-of-order fixture: response A arrives after selection
          moved to B; the store holds B's data and none of A's); scope switch clears
          protected content before the next fetch is issued (ordering asserted on the
          adapter's call log); each of the nine StatusEnvelope states maps to one distinct
          rendered label; an envelope with state FAILED on Analysis leaves the Holdings store
          untouched; an over-age envelope wins over a warm cache entry. ui-smoke of each tab
          in LOADING and FAILED with the failure fixtures at both viewports.
```

### `FE-s-4` -- the RenderPackage: templates, print styles, fonts, print entry point

```
ACT       Build pages/InvestorReporting/render/ as a versioned package: package.json-style
          manifest render/manifest.ts declaring supported contract and template versions;
          deterministic components for the performance report (summary of beginning value,
          ending value, period return; cumulative-return chart; period results; account
          detail; methods and sources; disclosures) and for the Analysis report (the
          certified section layout in its own orientation, same brand, never inheriting the
          performance narrative); a landscape-letter print stylesheet with page breaks,
          footnotes and embedded Lato from a locally packaged font set with its licence
          (source: docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt);
          brand tokens read from deck_generation/brand_spec/brand.json and the logo at
          deck_generation/brand/logo_package/Opal-Capital-Logo-Package/Full Logo/Full Color/
          Opal-Capital-Logo-Full-Color.svg; HEX kept as HEX, CSS pixels distinct from PDF
          points; the print entry point as the route /investor-reporting/print rendering an
          ExportBundle selected by ?bundle=<fixture id> (this round) with no network read;
          render fixtures under render/fixtures/. Determinism: no Date.now, no Math.random,
          no locale-dependent formatting without an explicit locale. The prototype at
          docs/research/investor_reporting_export_20260910/build_export_review.py and its PDF
          are the visual starting point and are not shipped.
SERVES    FWD-3 (the same result on screen and in the PDF), FWD-4 (the Analysis template),
          FWD-8 (the Opal template, preview-to-PDF parity), FWD-12 (one brand).
CROSSES   the counterpart executes this package in its export worker and returns the
          ExportReceipt; execution and the frozen bundle are its cells.
DEPENDS   FE-s-1.
PROOF     bun test on: rendering the same ExportBundle fixture twice yields byte-identical
          HTML; the manifest lists every contract version the components import; a bundle
          whose schemaVersion the manifest does not list is refused with a reason; the
          Analysis template renders with no narrative section present. ui-smoke of
          investor-reporting/print?bundle=<performance fixture> and ?bundle=<analysis fixture>
          at 1440x1200; fonts resolve locally (the page's font requests contain no external
          host). bun run typecheck rc 0.
```

### `FE-s-5` -- the Reporting tab

```
ACT       Build tabs/reporting/ mounting the package's performance components inside the
          tab: summary trio leads; cumulative-return chart; period results; compact account
          detail; the method labels TWR/MWR, net/gross, cumulative/annualized; currency;
          units; inception limitations; actual returned dates; UNAVAILABLE rendered as such;
          presets and custom dates with YTD as the proposed default; a benchmark or
          value-history section only when PerformanceReport marks it supported; PARTIAL or
          UNSUPPORTED rendered when the fixture says so; refresh and export are separate
          controls. Nothing in this cell computes a return.
SERVES    FWD-3.
CROSSES   canonical meaning, units, dates and the vendor-calculation-only rule are the
          counterpart's; this view is graded against its certified fixture.
DEPENDS   FE-s-3, FE-s-4.
PROOF     bun test on: for each of the three firm fixtures (49F BD, Cottonwood BD,
          Inflection Orion) the rendered labels, units, chart endpoints and account rows equal
          the fixture's fields (a field-by-field comparison, denominator = fields in the
          fixture); the partial-scope fixture renders PARTIAL; the unavailable-metric fixture
          renders UNAVAILABLE and never 0; the unsupported-benchmark fixture renders no
          benchmark section; a source grep of tabs/reporting/ for arithmetic on return fields
          returns 0 hits. ui-smoke of the tab with each firm fixture at both viewports.
```

### `FE-s-6` -- the Analysis tab

```
ACT       Build tabs/analysis/: variant selector (Overview, Comparison, Multi-Comp) with the
          primary portfolio, ordered comparison selections, holdings/input date, fee and
          settings (the 0.30% annual fee is a displayed setting from the contract, never a
          constant in this code) and generation state; the request list of email-ingested
          AnalysisRequests and released AnalysisReport revisions for the selected client;
          an input review showing inferred inputs with unresolved securities, account
          grouping, proposed substitutions and cover details each correctable, a correction
          submitting a NEW input revision through the typed client and never mutating the
          shown one; stage and release evidence rendered from StatusEnvelope and the request's
          stage fields with no percentage anywhere; native sections rendered from
          AnalysisReport.sections in Opal components with each section's dates, disclosures
          and units; a section rendered as SUPPORTED only when the fixture marks its
          paired-fixture comparison passed; an embedded vendor PDF rendered as a preview and
          labelled as such; MODELED analysis labelled modeled and never presented as actual
          performance.
SERVES    FWD-4.
CROSSES   the intake, mapping, generation, extraction and release state are the
          counterpart's; the three-variant PDF parity gap stays open until its fixtures exist.
DEPENDS   FE-s-3.
PROOF     bun test on: all three variants render from their fixtures; a correction produces a
          request with inputRevision = previous + 1 and the previous fixture is unchanged
          (deep-equal before and after); a source grep of tabs/analysis/ for '%' adjacent to a
          progress or stage word returns 0 hits; a section whose fixture lacks the
          parity-passed flag renders UNSUPPORTED; the fee shown equals the fixture's
          settings.annualFee and no literal 0.30 or 0.003 exists in tabs/analysis/.
          ui-smoke of the tab in READY, NEEDS-CORRECTION and UNCERTAIN at both viewports.
```

### `FE-s-7` -- the Holdings tab

```
ACT       Build tabs/holdings/: summary of current value, unique account count, source dates
          and model coverage; drilldowns through Models, SMAs, Client and the other categories
          the HoldingsSnapshot node hierarchy carries, using CategoryViewTree
          (portal/src/components/CategoryViewTree.tsx) for the tree and modelPortfolioColors
          (portal/src/lib/modelPortfolioColors.ts) for colour; donut charts with breadcrumbs
          and direct labels following the AdvisorIntelligence radial precedents in
          presentation only; a table equivalent beside every chart. Every slice states its
          value basis (observed custody, observed allocation, assigned-account, target) and
          its denominator; percent of parent and percent of total shown as two values;
          sleeve-held securities and model target constituents are different drill
          destinations; unassigned, unmapped and classification-unavailable amounts are
          distinct slices; partial allocations are never scaled to 100; negative and short
          positions keep their sign; a signed, zero or unknown denominator renders the
          alternative table state the contract names; classification partitions
          (Supervised/Unsupervised, Advised/Residual) are displayed from the snapshot and are
          never merged with the value basis axis; an unknown classification renders as
          unknown. No time series.
SERVES    FWD-5.
CROSSES   joins, reconciliation, denominators and revision-bound nodes are the counterpart's.
DEPENDS   FE-s-3.
PROOF     bun test on the seven model-overlay fixture cases (observed SmartX allocation,
          Eclipse assignment, Cottonwood target blend, cash remainder, unknown category,
          duplicated relationship membership, stale overlay): the sum of rendered slice values
          equals the fixture's stated total and never 100 when the fixture is partial; a
          negative position renders negative; the unknown-category fixture renders 'unknown'
          and never 'Client'; parent and total percentages differ where the fixture says they
          do; a source grep of tabs/holdings/ for Math.abs returns 0 hits; summary and drill
          carry the same (scope, revision). ui-smoke of the top level and one drill at both
          viewports.
```

### `FE-s-8` -- the narrative page

```
ACT       Build render/narrative/: a full-width period-in-context page inside the
          performance template, rendered only when selected and when NarrativePacket is
          present; the performance time series with the packet's peak, trough, recovery and
          movement markers and its dated annotations placed on the curve; the Trending Topic
          and Topic Cloud terms dated to each marked window; other sentiment signals as
          supporting context using the visual vocabulary of MarketRegimeIndicator,
          SentimentGauge and SentimentPanel (import only); every fact and reference from the
          packet's cited evidence and nothing else; a fixed statement that the page shows
          contemporaneous market context and does not explain the return; a window that
          predates the packet's history cutoff renders a MISSING HISTORY state naming the
          cutoff date, never an empty list; footnotes and coverage from the packet.
SERVES    FWD-8.
CROSSES   inflection selection, evidence dating and prose validity are the counterpart's.
DEPENDS   FE-s-4.
PROOF     bun test on: the pre-history fixture renders the MISSING HISTORY state and no topic
          element; the two-marker fixture renders exactly two markers at the packet's dates;
          the rendered text contains the contemporaneous-context statement and contains none
          of the words caused, because, drove, explains, due to (list enumerated in the test);
          every quoted term in the output exists in the packet's evidence array. ui-smoke of
          investor-reporting/print?bundle=<narrative fixture> at 1440x1200.
```

### `FE-s-9` -- export options, modals, preview, receipt

```
ACT       Build export/: the dashboard is the default view; Export is a separate control
          opening a modal with branding options (Opal, advisor, co-branded), the narrative
          page toggle, account detail, and the optional sections the bundle marks supported;
          approved scoped asset references only; the standard Opal template renders with no
          logo and the modal shows what branding was applied; a branding edit creates a new
          export revision without re-fetching performance (the request carries the same
          performance revision); the preview renders through the package from an ExportBundle
          and issues no vendor call and no performance fetch; export submission goes through
          the typed client; ExportReceipt and StatusEnvelope drive the job state and the
          authorized download route; an Analysis export binds the same input, configuration
          and artifact revision the tab shows.
SERVES    FWD-8, FWD-4 (the Analysis export).
CROSSES   the export API, the frozen bundle, the worker and the receipt are the counterpart's.
DEPENDS   FE-s-5, FE-s-8.
PROOF     bun test on: the initial render shows no export modal; a branding change produces a
          request whose performanceRevision equals the previous request's; the adapter call
          log during a preview contains no performance and no provider-shaped call; a missing
          advisor logo renders the Opal template and the applied-branding label reads Opal;
          the receipt fixture's download route is the one rendered. ui-smoke of the modal
          open and of the preview at both viewports.
```

### `FE-s-10` -- the Global view

```
ACT       Build global/ and the Global behaviours in header/, tabs/ and export/: with
          'global' selected and ResolvedScope granting a permitted-firm catalogue, client
          search spans every permitted firm, each result carries its firm, and every tab,
          review and export shows the firm attribution; selecting a firm from the dropdown
          clears the prior selection and all protected content before another response can
          display; a principal whose ResolvedScope has one permitted firm cannot enter Global
          by URL parameter, saved state or an altered selector value (the selector value is
          validated against the catalogue on every change and on load); the figures shown for
          a client in Global are the figures the firm-scoped fixture shows for the same client
          and revision; no blended or recomputed value exists; no email request is rebound to
          another firm from this view.
SERVES    FWD-11.
CROSSES   the entitlement class and the scoped routes are the counterpart's.
DEPENDS   FE-s-5, FE-s-6, FE-s-7, FE-s-9.
PROOF     bun test on: with the two-firm ResolvedScope fixture, search returns clients from
          both firms each carrying firm; a firm switch clears the store before the next
          request is issued; with the one-firm fixture, ?firm=global, a persisted 'global'
          selection and a forced selector value each resolve to the single permitted firm;
          the Global render of client X at revision R deep-equals the firm-scoped render of
          X at R. ui-smoke of Global with two firms at both viewports.
```

### `FE-s-11` -- design conformity: census, brand review, narrow viewport

```
ACT       Produce the component census: every import under pages/InvestorReporting/ that
          resolves to a React component, denominator printed, each row REUSED with its exact
          existing path or NEW with the reason the existing set could not meet; the
          denominator to subtract from is the PRD's PATHS table (11 reuse rows) plus the
          import graph. Review screen, modal, preview and print against
          deck_generation/brand_spec/brand.json and deck_generation/brand/
          opal_brand_guidelines.pdf: colours, logo clear space, Lato. Run ui-smoke at 390x844
          on the page, each tab, the export modal and the print route and read every PNG
          against the colour law. Confirm every chart has a table equivalent. Confirm the
          firm dropdown is PageSurfaceControl as="dropdown" and not a new component.
SERVES    FWD-12.
DEPENDS   FE-s-10.
PROOF     the census file lists N components with N printed and every row REUSED or NEW with
          a reason (a test parses the census and fails on a row with neither); a source grep
          of pages/InvestorReporting/ for text-white, text-[a-z]+-300 and bg-white/ outside a
          dark Panel returns 0 hits; the 390x844 PNG set exists for page, three tabs, modal
          and print; judgment: the screens and the export read as one Opal product to a
          reviewer who knows another portal page -- graded at L9, not by the worker.
```

---

## 3. RE-CUT MAP -- PRD candidates to cells

| candidate | cell | change |
|---|---|---|
| F1 route + page identity | `FE-s-2` | merged with F2: one shell, one App.tsx edit |
| F2 header, dropdown, autosuggest | `FE-s-2` | -- |
| F3 tabs, persistence, scope-switch clearing | `FE-s-3` | merged with F7: the selection/revision guard and the status renderer are one state layer |
| F4 Reporting tab | `FE-s-5` | mounts the package's components (F9) so screen and PDF share one renderer |
| F5 Analysis tab | `FE-s-6` | -- |
| F6 Holdings tab | `FE-s-7` | -- |
| F7 lifecycle states | `FE-s-3` | see F3 |
| F8 export options and modals | `FE-s-9` | -- |
| F9 RenderPackage | `FE-s-4` | the performance and Analysis layout components live here, not in the tabs |
| F10 narrative page | `FE-s-8` | -- |
| F11 Global view | `FE-s-10` | -- |
| F12 typed client and transport | `FE-s-1` | merged with F14 and made the root: every other cell consumes its types, adapter and fixtures |
| F13 design conformity | `FE-s-11` | -- |
| F14 consumer fixtures | `FE-s-1` | see F12 |

**14 of 14 candidates mapped; 0 dropped; 0 split across two cells.**

---

## 4. DEPENDENCY EDGES

```
  FE-s-1  <- (none)                       READY ROOT
  FE-s-2  <- FE-s-1
  FE-s-3  <- FE-s-2
  FE-s-4  <- FE-s-1
  FE-s-5  <- FE-s-3, FE-s-4
  FE-s-6  <- FE-s-3
  FE-s-7  <- FE-s-3
  FE-s-8  <- FE-s-4
  FE-s-9  <- FE-s-5, FE-s-8
  FE-s-10 <- FE-s-5, FE-s-6, FE-s-7, FE-s-9
  FE-s-11 <- FE-s-10

  weakly connected components:  M = 1
  ready roots at issuance:      R = 1
  waves by depth:               A={1}  B={2,4}  C={3,8}  D={5,6,7}  E={9}  F={10}  G={11}
  max concurrent width:         3  (wave D)
```

**Slots for L6, by the queue rule (two orders on one chain share one worker):**

```
  ~1  FE-s-1 -> FE-s-2 -> FE-s-3 -> FE-s-5 -> FE-s-9 -> FE-s-10 -> FE-s-11
  ~2  FE-s-4 -> FE-s-8                      seated when FE-s-1 is terminal
  ~3  FE-s-6                                seated when FE-s-3 is terminal
  ~4  FE-s-7                                seated when FE-s-3 is terminal
```

**Fan-out: `1 of 1 ready root at issuance, 4 slots, cap 8` (1 component, max width 3).** All eleven orders are issued in the one issuance; ten carry `blocked` until their dependency is terminal.

**The one assumption that could fail:** `FE-s-5` and `FE-s-8` assume the package in `FE-s-4` exposes the performance layout components and the template without changing shape once `FE-s-4` is terminal. If a tab needs a package change, that is a surprise row on `FE-s-4`, not an edit inside the tab.

---

## 5. RULE 24 RECORD

| postulate | how this rectangle satisfies it |
|---|---|
| (i) MECE over a declared domain | **Domain 1: the PRD's endpoint outcomes, denominator 8.** Forward: FWD-1 -> {1,2,3}; FWD-3 -> {4,5}; FWD-4 -> {4,6,9}; FWD-5 -> {7}; FWD-6 -> {1,3}; FWD-8 -> {4,8,9}; FWD-11 -> {2,10}; FWD-12 -> {2,4,11}. Backward: every cell serves at least one. **8 minus 8 = 0 uncovered.** **Domain 2: the PRD's cell candidates, denominator 14** (section 3): 14 minus 14 = 0. **Domain 3: the surface manifest, denominator 8** (section 1): 8 minus 8 = 0. Uncovered member hunted in each domain by subtraction; none found. |
| (ii) same grain | every cell is one region of one write surface serving named outcomes; the grain is (write region, outcome). `FE-s-11` writes a record surface rather than a code surface and is the one cell at a different grain, stated here: its product is the census and the review, not code. |
| (iii) intent coherence | one axis, one intent: the advisor-facing Investor Reporting product on the portal, reading normalized authorized contracts. No cell carries a backend intent; a cell that would need one is the counterpart's. |
| (iv) state coherence | the round moves every owned outcome from absent toward gradeable and the view half of the five crossing outcomes to APPLIED. **What it does not move:** no crossing outcome (FWD-3, 4, 5, 8, 11) to REALIZED, because their data, entitlement and execution halves are the counterpart's and are graded inside each outcome's adjudication; no EXERCISED bar to REALIZED, because a cell produces the artifact and its mechanical proof while the exercised reading is a person's act at L9; no live vendor call; no PROD promote; no counterpart route. |

---

## 6. BATTERY DISPOSITION -- run at this cut

| lens | disposition | denominator / reason |
|---|---|---|
| `comp-schedule` | DECLARED-NOT-APPLICABLE | no scheduled producer among the three write surfaces; the mailbox poll and the export worker are the counterpart's cells |
| `comp-iam` | DECLARED-NOT-APPLICABLE | no IAM-gated resource is written; entitlement is enforced on the counterpart's `/api/scoped/` routes; the browser writes no AWS resource |
| `comp-adversary compose` on the PRD | RUN | 5 complement sources run, 0 deferred, 4 declared-excluded; every pin read-vintage |
| `comp-cache collisions` | RUN | 415 files scanned; 0 existing keys under an `investor-reporting` namespace; binding in section 2 BOUNDS (`keys`) |
| `comp-blast` on the exact graph nodes | RUN, LOWER BOUND | `component:portal/src/App.tsx`, `.../PageSurfaceControl.tsx`, `.../TabNavigation.tsx`, `.../ModelPortfolios.tsx`: PRESENT_WITH_ZERO_RESULTS (extracted edges only; graph vintage 2026-09-10T12:24Z). `portal/src/components/CategoryViewTree.tsx`: SUBJECT_ABSENT_FROM_CORPUS while the file exists at portal `5907cbca` -- a graph blindness, stated; the cell imports it and never edits it |
| `comp-surprise --project IRPT_FNTEND` | RUN | 0 items over 56 files; the tree channel file does not exist and is created with the issuance |
| path existence at HEAD | RUN | 23 of 23 reuse paths and 16 of 16 fixture and brand artifacts EXIST (portal `5907cbca`, workspace `62301f71e0`); 2 of 2 new homes ABSENT, as required |
| instrument availability | RUN | `portal/scripts/ui-smoke.mjs` exists (21,677 bytes); bun 1.3.9 and `bun test` pass a smoke; `bun run typecheck` is `tsc -b --noEmit`; no vitest, no msw, no testing-library installed and none added |

---

## 7. WHAT THIS DECOMPOSITION REFUSES TO ASSUME

1. **That a fixture-backed render closes a crossing outcome.** The adapter proves the view half. The five crossing grades read the counterpart's producer fixtures and execution too; the consumer fixtures in `FE-s-1` are one half of a pair.
2. **That the counterpart's routes exist.** They do not at this cut. The typed client targets them and runs against the adapter; the switch is one configuration value.
3. **That `isInternal()` is a permission.** It is a rendering hint. Global is granted by `ResolvedScope.permittedFirms` and refused in `FE-s-10` against URL, saved state and altered selector.
4. **That the print entry point is a separate build.** In this round it is a portal route. Repackaging for the counterpart's worker follows the portal's build constraints and is measured when that worker exists.
5. **That any number in the brief is fixed.** The two viewports are test setups from the sketch's evidence file, not acceptance values.
6. **That a screenshot proves an EXERCISED bar.** A cell produces the artifact and its mechanical proof; the exercised reading is graded at L9.
7. **That a workspace worktree contains the portal.** The workspace tracks `portal/` as a gitlink; a linked worktree of the workspace carries an empty `portal/`. Each slot therefore receives two worktrees at L6: one of the workspace for its records and one of the portal repo, cut from `DEV`, for its code. The workspace's owned-paths hook never sees a portal commit, so the `<paths>` grant on portal paths binds by reading; the workspace paths bind mechanically.
8. **That the three-variant Analysis PDFs exist.** They do not; `FE-s-6` renders UNSUPPORTED where the fixture lacks parity, and the gap stays named.

---

## 8. HOLDS

None. Every cell is cuttable or dependency-blocked. No live vendor call is authorized. No PROD promote is in scope. The high-definition advisor logos are a pending input and never block a cell (`FE-s-9` renders the Opal template without them).
