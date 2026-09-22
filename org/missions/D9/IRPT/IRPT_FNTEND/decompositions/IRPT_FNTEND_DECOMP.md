# IRPT_FNTEND -- L5 decomposition -- rounds 1 through 11 -- v0.11

```json
{
 "project": "IRPT_FNTEND",
 "directive": "D9",
 "fabric": "laptop",
 "round": 11,
 "decomp_version": "v0.11",
 "round_1_header_retained_below": true,
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@5fd2dc9ab5",
 "prd_version": "v0.9",
 "brief_ref": "docs/briefs/investor-reporting-ir-fe-brief-20260910.md@2acf23d8fd",
 "endpoint_outcomes": ["FWD-1", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-8", "FWD-11", "FWD-12"],
 "cells": 9,
 "cell_id_shape": "FE-s-<n>",
 "code_repo": "portal (nested git repo, gitlink in the workspace; branch DEV @243089eb)",
 "record_repo": "workspace (branch CLOUD, this round's issuance commit)"
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


---
---

# ROUND 2 -- v0.2 -- the recut on the CTO's ROUND-2 ANALYSIS

```json
{
 "round": 2,
 "decomp_version": "v0.2",
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@d1479bc5f0",
 "prd_version": "v0.6",
 "analysis_ref": "org/missions/D9/IRPT/IRPT_FNTEND/ledger/ROUND_ANALYSIS.round1.md@0d57ceb2f9",
 "slug_ref": "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v1.md@27e67fa6a5",
 "round1_cells": "FE-s-1..FE-s-11, all COMPLETE (11 terminal task orders, 11 VALID instances; portal DEV edab15b5, workspace 2e50d2e129)",
 "cells": 7,
 "cell_id_shape": "FE-s-<n> continuing from 12",
 "code_repo": "portal (nested git repo, gitlink in the workspace; branch DEV @edab15b5)",
 "record_repo": "workspace (branch CLOUD)",
 "producer_pins": {
  "routes": "infra/aws/terraform/investor-reporting/api/routes.json@bef9b459f3 (11 DECLARED + 1 NO-HANDLER-AT-HEAD = 12)",
  "schemas": "infra/aws/lambda/investor-reporting/_contracts/*.schema.json@33351469c2 (11) with fixtures/*.valid.json",
  "backend_prd": "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md@e6ba5d9878 (CONTRACTS: BK owns identity, economic meaning, units, dates and wire compatibility)",
  "ui_contract": "docs/research/investor_reporting_ycharts_variants_20260911/UI_CONTRACT.md@72acd16e66 (S10, the Generate request half)"
 }
}
```

Round 1 delivered the parts (analysis section 2: shell, header, tabs, package, export, Global, census; 322 tests). The seam between the parts and the backend does not exist, no partner firm can reach the route, the export flow is unmounted, the composer is at v0.4's shape, the fonts are absent and DEV is red under tsc. Round 2 is those seven things, in the order the analysis ruled, as ONE issuance. The round-1 rectangle above is unchanged and its cells stay COMPLETE; the round-2 cells are additive (a re-decomposition of the affected surfaces, recorded here as the COO's choice per spine L10 "the recut").

## R2.1 THE RECTANGLE -- seven cells, the analysis's seven rulings

| cell | ruling | write surface (portal unless stated) | serves | slug rows | wave | slot |
|---|---|---|---|---|---|---|
| `FE-s-12` | 1 DEV green first | `src/pages/InvestorReporting/__tests__/fe-s-11/` | every outcome (the shared branch) | S17 | A | ~1 |
| `FE-s-13` | 2 the seam | `src/api/endpoints/investor-reporting.ts`; `src/pages/InvestorReporting/contracts/` (+ `wire/`); `.../fixtures/` (wire, requests, smoke); `.../__tests__/fe-s-1/`, `__tests__/fe-s-13/` | FWD-1, FWD-6 (and the data half of every crossing outcome) | C-S42, W3-S2 (the wire half), W2-S2 | B | ~1 |
| `FE-s-14` | 3 the route reachable by a partner firm | `src/lib/firmAccess.ts` (three entries); `.../global/`; `.../header/`; `.../__tests__/fe-s-14/`; smoke fixtures `fe-s-14-*.json` | FWD-1, FWD-11 | W1-S10 | C | ~2 |
| `FE-s-15` | 5 the Generate composer (F5 at v0.6, S10) | `.../tabs/analysis/`; `.../__tests__/fe-s-15/`; smoke fixtures `fe-s-15-*.json` | FWD-4 | W3-S2 (the meaning half), C-S43 (clean/correction) | C | ~1 |
| `FE-s-16` | 6 mount the export flow; narrative meaning | `.../export/`; `.../render/narrative/`; `.../index.tsx` (the two ExportAnchorSlot mounts only); `.../__tests__/fe-s-16/`; smoke fixtures `fe-s-16-*.json` | FWD-8, FWD-4 | W1-S11, W2-S6 | C | ~3 |
| `FE-s-17` | 4 Lato is a packaging input | `.../render/assets/fonts/`; `.../render/print.css`; `.../render/manifest.ts`; `.../__tests__/fe-s-17/` | FWD-8, FWD-12, FWD-3 | W2-S3 | B | ~2 |
| `FE-s-18` | 7 evidence rules; mobile | layout-only edits under `.../tabs/`, `.../header/`, `.../export/`, `.../global/`, `.../render/`; `.../__tests__/fe-s-18/`; smoke fixtures `fe-s-18-*.json`; the deliverables folder | FWD-3, FWD-5, FWD-8, FWD-11, FWD-12 (the NOT_EVALUATED surfaces) | C-S43, W3-S1, W4-S1, W1-S12 (the retained one-firm control) | D | ~1 |

**Coverage by subtraction, three domains.** (1) The analysis's seven rulings (denominator 7) minus the seven cells above = 0 uncovered. (2) The slug's OPEN rows (denominator 8: W2-S3, W2-S6, W3-S2, W1-S10, W1-S11, S17, C-S42, C-S43) minus the rows the table names = 0 uncovered. (3) The PRD header's outcomes (denominator 8) minus the outcomes the cells serve: FWD-1 {13,14}, FWD-3 {17,18}, FWD-4 {15,16}, FWD-5 {18}, FWD-6 {13}, FWD-8 {16,17,18}, FWD-11 {14,18}, FWD-12 {17,18} = 0 uncovered. Open items OUTSIDE the recut stay where the analysis put them (Lato 700 and the pushes at Andrew; ui-smoke query-string at the smoke-tool owner; R3 runtime at the COO runtime owner; the WAF diff at CloudOps) and no cell here writes into them.

## R2.2 BOUNDS -- ALL ROUND-2 CELLS (in addition to round 1's, which stand)

```
producer    routes.json@bef9b459f3 is the method/path authority; _contracts/*.schema.json@33351469c2
            are the shapes; where a field's MEANING differs, the backend PRD's definition wins and
            the frontend changes. No casing translator without economic meaning: a wire->view adapter
            RENAMES and RESTRUCTURES, never derives, averages, infers or defaults a value.
no-route    an operation with no DECLARED route does not exist on the live client; the view renders
            the envelope state UNAVAILABLE with public reason code no-declared-route and a surprise
            row names the route for the counterpart. The one NO-HANDLER-AT-HEAD route (holdings) is
            typed and marked not-yet-exercisable; its adapter path is fixture-only.
resolved    the browser never sends and never receives the server-only resolved envelope; a test in
            every cell that composes a request prints RESOLVED-KEY LEAKS: 0.
typecheck   EVERY order carries `cd <WS>/portal && timeout 180 bun run typecheck; echo rc=$?` -> rc=0.
evidence    every smoke criterion keys on a printed discriminator (CLICKED: <name>, DID NOT LAND,
            CONSOLE[log]: REFS RESOLVED: n of n via --console) and never on rc alone; every <expect> is
            a plain token with no regex metacharacter; a fixture map names the WHOLE page's needs
            (resolve-scope, the default Reporting tab's performance-report, the tab under test); a
            capture claim names a unique file recorded with its sha256 in the order's captures
            manifest; paired screen/preview/print views come from ONE frozen report fixture.
channel     round-2 rows go to surprise-channel/investigations/INVESTIGATION_v2.md (created by the
            first row; the row gate refuses an empty file); ids continue each slot's sequence
            (W1 from S15, W2 from S7, W3 from S3).
gitlink     never stage `portal` in the workspace repo.
```

## R2.3 THE CELLS

### `FE-s-12` -- DEV green first
```
ACT       Clear the eight TypeScript errors under __tests__/fe-s-11/ (test.each, toMatch, statSync,
          four implicit any) by editing those two test files only: loop instead of test.each,
          a regex test instead of toMatch, an existing shim member instead of statSync, typed
          parameters. The ambient shims are not edited; strictness is not lowered; no file is
          excluded from tsc.
SERVES    every outcome (the shared branch is never pushed red).   SLUG  S17.
DEPENDS   none (READY ROOT).
PROOF     bun run typecheck rc 0; bun test __tests__/fe-s-11 0 fail; whole set 0 fail; files
          changed outside the folder = 0.
```

### `FE-s-13` -- the seam: producer defines, consumer conforms
```
ACT       contracts/wire/: one TypeScript type per producer schema (11), generated from
          _contracts/*.schema.json by a script under __tests__/fe-s-13/ (committed output, the
          generator's input pinned by sha256 in the output header). The client's operation table
          becomes routes.json: every DECLARED route is exactly one operation with its method, path
          template and parameter binding (GET with path params and query; POST with a JSON body);
          LiveClient sends exactly that; the holdings route is typed and marked
          not-yet-exercisable; analysis-requests (no list route) and export-preview (no route) are
          RETIRED from the live client under the no-route bound -- the preview is composed
          client-side from the selected options and report refs into the wire ExportBundle and
          submitted through POST export. contracts/adapt.ts: wire -> view adapters for the ten
          consumed contracts and view -> wire for the two produced request shapes, each field of
          the view type mapped from a named wire path in an exported FIELD_MAP (view field <-
          wire path, kind RENAME | RESTRUCTURE | CARRIED-AS-IS); no arithmetic. fixtures/wire/:
          the eleven producer .valid.json copied byte-for-byte with their source sha256;
          fixtures/wire/requests/: one request record per DECLARED route (method, path with the
          fixture's own ids bound, query, body) -- the corpus the counterpart's paired test
          replays into its real handlers; fixtures/smoke/: re-based so the page's whole needs
          are served at the declared paths in wire shape (fe-s-13-wire.json). FixtureAdapter
          serves the wire fixtures through the same adapters the live client uses.
SERVES    FWD-1, FWD-6; the data half of FWD-3/4/5/8/11.   SLUG  C-S42, W2-S2, W3-S2 (wire half).
CROSSES   the counterpart publishes the contract as one versioned artifact (its ruling 1); if that
          lands before this cell is seated the face pins it instead of the two raw pins.
DEPENDS   FE-s-12.
PROOF     routes parity 11 of 11 declared (test reads routes.json); producer fixtures adapted 11
          of 11; request corpus 11 of 11 with RESOLVED-KEY LEAKS 0; field map N of N view fields
          mapped, 0 derived; the fe-s-1 negatives (stale dropped, revocation clears) still pass;
          smoke of the page with fe-s-13-wire.json reaches Holdings (CLICKED: Holdings);
          typecheck; whole set.
```

### `FE-s-14` -- the route reachable by a partner firm; the Global proof recut
```
ACT       portal/src/lib/firmAccess.ts: add '/investor-reporting' to the 49financial, inflection
          and cottonwood sets and nothing else (demo unchanged; no other path). The F10 proof
          recut: a firm session (ui-smoke --firm <id>) reaches /investor-reporting and renders the
          Holdings tab; it sees only its own scope (the wire resolve-scope fixture for that firm
          carries one permitted firm; the dropdown is absent; ?firm=global, a persisted 'global'
          and a forced selector value each resolve to that firm); a non-registry firm id is still
          refused (DID NOT LAND, /market). Global with two firms still renders.
SERVES    FWD-1, FWD-11.   SLUG  W1-S10.
DEPENDS   FE-s-13 (the wire smoke fixtures).
PROOF     allowlist test 3 of 3 registry firms admitted, demo and an unknown id refused; smoke
          --firm 49financial CLICKED: Holdings (repeat for inflection, cottonwood); smoke --firm
          nonregistry DID NOT LAND; GLOBAL PATH: absent printed by the one-firm header test;
          two-firm Global smoke CLICKED: Holdings; typecheck; whole set; judgment: the firm sees
          only its own scope (PNGs at 1440 for the three firms).
```

### `FE-s-15` -- the Generate composer (F5 at v0.6, S10)
```
ACT       tabs/analysis/: the composer produces AnalysisRequest's browser request half, in this
          order and nothing else: client from the header's selection; account(s) with a
          confirmable default, shown as labels; the holdings snapshot preselected WITH its as-of
          (an immutable snapshot_id from the wire HoldingsSnapshot; never re-fetched mid-job); 0-5
          ORDERED comparisons by opaque catalog keys; optional title; prepared-for/by prefilled
          from the profile fields the wire scope carries, overrides only where the wire policy
          allows; the variant resolved by count and DISPLAYED (0 Overview, 1 Comparison, 2-5
          Multi-Comp), variant 'auto' sent unless picked, an inconsistent explicit pick refused
          client-side; request_id a stable per-click idempotency key preserved across transport
          retries; changed inputs = a new request_id. Submit through POST analysis; job states
          queued / preparing / generating / ready / needs attention polled from GET status/{jobId}
          (the Opal job record); a WAF-refresh or reconciliation state renders needs attention
          with the request preserved. W3-S2: revision identity and section support are read from
          the wire fields the schemas name (AnalysisRequest.identity / corrections / stage;
          AnalysisReport.extraction_validation / release); parity.ts's local derivation is
          removed. Sections and the native/PDF preview render as round 1 built them, from the
          wire report through the adapter.
SERVES    FWD-4.   SLUG  W3-S2, C-S43 (clean/correction).
DEPENDS   FE-s-13.
PROOF     composer test: request body keys exactly the seven S10 keys; RESOLVED-KEY LEAKS 0;
          variant by count 0/1/2/5 and refusals (inconsistent pick; 6 comparisons); request_id
          stable across a retry (call log 2 sends, 1 id) and new on changed inputs; job-state test
          5 of 5 states rendered from status fixtures, needs-attention preserves the request;
          REVISION IDENTITY: preserved on a clean request and its correction; smoke Analysis
          clean and needs-correction at 390 (CLICKED: Analysis); typecheck; whole set; judgment.
```

### `FE-s-16` -- mount the export flow; the narrative's meaning is the backend's
```
ACT       export/: AppliedBranding and ReceiptPanel mounted inside ExportModal's dark Panel and
          wired to the composed wire ExportBundle and the ExportReceipt / StatusEnvelope the
          typed client returns; the ExportAnchorSlot mounts in index.tsx pass the tab's real
          report refs and revision (the two mount lines only). Five states proven on the MOUNTED
          flow: no-assets, approved-assets, running, failed, ready/download (the download route
          the receipt carries). render/narrative/: the page reads NarrativePacket's wire fields
          (events, cited_evidence, prose, coverage) through the adapter; absent history renders
          MISSING HISTORY naming coverage's cutoff; the placeholder is gone.
SERVES    FWD-8, FWD-4.   SLUG  W1-S11, W2-S6.
DEPENDS   FE-s-13.
PROOF     STATES RENDERED: 5 of 5 on the mounted modal; colour-law 0 fail; MARKERS: 2 and MISSING
          HISTORY: rendered from wire narrative fixtures; smoke Export at 1440 and 390 (CLICKED:
          Export); print narrative-on smoke REFS RESOLVED: 1 of 1; typecheck; whole set; judgment.
```

### `FE-s-17` -- Lato is a packaging input
```
ACT       Copy the three OFL 1.1 files from .runtime/codex-seats/4.0.0_SA_CRO/performance-export-
          recon/fonts/ into render/assets/fonts/ (Lato-Regular.ttf d636e468..., Lato-Light.ttf
          cf2a7745..., Lato-SemiBold.ttf 71b8b7de...) beside the FONT_LICENSE.txt already there,
          with fonts.manifest.json recording name, bytes, sha256, weight, licence and the stand-in
          rule; print.css declares faces 300, 400 and 700 with 700 served by Lato-SemiBold (600)
          and a comment naming the stand-in; no italic face (none is on the box); every url() is
          local. manifest.ts declares the packaged fonts and the stand-in. No new source is
          fetched; the 700 weight stays Andrew's carried call.
SERVES    FWD-8, FWD-12, FWD-3.   SLUG  W2-S3.
DEPENDS   FE-s-12.
PROOF     FONTS: 3 of 3 hashes match the manifest; EXTERNAL FONT HOSTS: 0 in print.css; STAND-IN
          DECLARED: 700<-600 in manifest.ts; a smoke of the print route with --netlog shows the
          local ttf requests served and EXTERNAL: 0; LICENCE: OFL-1.1 present; typecheck; whole
          set; print performance recaptured at 1440 with the font (REFS RESOLVED: 1 of 1).
```

### `FE-s-18` -- evidence rules; mobile clipping fixed and captured
```
ACT       Layout-only edits (class and structure, no behaviour, no data) so the page, the three
          tabs, the export modal and the print route do not clip or overlap at 390: the Holdings
          summary card and firm attribution, the slice table (horizontal scroll container), the
          Reporting period columns, the header actions. Captures under the evidence rules: paired
          screen / preview / print from ONE frozen performance report (fe-s-18-frozen.json, one
          revision served to the tab, the modal preview and the print route); the four
          NOT_EVALUATED surfaces on the mounted views -- Analysis clean and needs-correction,
          Holdings observed / target / missing-attribution, print narrative-on and pre-history;
          Global at 1440; every PNG named uniquely and recorded with sha256 in
          captures.manifest.json. Census and colour-law re-run on the round-2 tree.
SERVES    FWD-3, FWD-5, FWD-8, FWD-11, FWD-12.   SLUG  C-S43, W3-S1, W4-S1, W1-S12 (control).
DEPENDS   FE-s-14, FE-s-15, FE-s-16, FE-s-17.
PROOF     PAIRED: 1 report, 3 views (one performance-report body hash across the three fixture
          maps); UNIQUE FILES: n of n in the manifest; each capture's smoke prints its
          discriminator (CLICKED: Reporting / Analysis / Holdings / Export; REFS RESOLVED: 1 of 1);
          COMPONENTS: N re-censused; colour-law 0 fail; typecheck; whole set; judgment: no clipping
          at 390 and one Opal product (L9, from the manifest's PNGs).
```

## R2.4 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-12 <- (none)                         READY ROOT
  FE-s-13 <- FE-s-12
  FE-s-17 <- FE-s-12
  FE-s-14 <- FE-s-13
  FE-s-15 <- FE-s-13
  FE-s-16 <- FE-s-13
  FE-s-18 <- FE-s-14, FE-s-15, FE-s-16, FE-s-17

  weakly connected components:  M = 1      ready roots at issuance: R = 1
  waves by depth:  A={12}  B={13,17}  C={14,15,16}  D={18}     max concurrent width: 3 (wave C)

  ~1  FE-s-12 -> FE-s-13 -> FE-s-15 -> FE-s-18
  ~2  FE-s-17 -> FE-s-14        (17 seated when 12 is terminal; 14 when 13 is terminal)
  ~3  FE-s-16                   (seated when 13 is terminal)
```

**Fan-out: `1 of 1 ready root at issuance, 3 slots, cap 8`.** All seven orders are issued in the one issuance; six carry `blocked` until their dependency is terminal.

## R2.5 RULE 24 RECORD (round 2)

| postulate | how |
|---|---|
| (i) MECE | three domains by subtraction in R2.1: rulings 7-7=0; slug OPEN rows 8-8=0; outcomes 8-8=0. Cells partition the write surfaces: FE-s-13 owns contracts/, the client and fixtures; FE-s-14 firmAccess.ts, global/, header/; FE-s-15 tabs/analysis/; FE-s-16 export/, render/narrative/, the two mount lines; FE-s-17 render/assets/fonts/, print.css, manifest.ts; FE-s-18 layout-only edits across tabs/header/export/global/render AFTER every other cell is terminal, so no write surface is shared concurrently; FE-s-12 the fe-s-11 test folder. |
| (ii) same grain | (write region, ruling) per cell; FE-s-18 is the record-and-layout grain, stated. |
| (iii) intent | one axis: the frontend conforms to the producer and proves it on mounted, reachable views. No cell carries a backend intent; the counterpart's half of the seam is its own cell. |
| (iv) state | moves FWD-1/6 toward APPLIED on the real seam and every crossing outcome's view half to EXERCISABLE on a reachable route. Does NOT move: any grade to REALIZED (the CTO's read on the exercised artifact); the backend's routes, handlers, renderer or contract artifact; the 700 weight; the pushes. |

## R2.6 BATTERY DISPOSITION (round 2)

| lens | disposition | denominator / reason |
|---|---|---|
| comp-schedule / comp-iam | DECLARED-NOT-APPLICABLE | no scheduled producer, no IAM resource written; firmAccess.ts is a client-side allow-list read by ProtectedRoute |
| comp-adversary | RUN at L4 on v0.6 (both halves SIGNED, ADMITTED under v3.15 per 95828/95889) | carried; no new complement source |
| producer pins | RUN | routes.json@bef9b459f3 resolves (12 routes: 11 DECLARED, 1 NO-HANDLER); 11 of 11 schemas and 11 of 11 .valid.json fixtures exist at 33351469c2; required-field sets read (all `additionalProperties: false`) |
| fonts on box | RUN | 3 of 3 ttf present with sha256 equal to sources.json; OFL.txt 4407 bytes; FONT_LICENSE.txt already under render/assets/fonts/ |
| typecheck at the base | RUN | DEV @edab15b5: rc=2, 8 errors, all under __tests__/fe-s-11/ (FE-s-12's whole input); tests 322 pass 0 fail |
| firm matrix | RUN | FIRM_ALLOWED_PATHS: 4 entries (49financial, inflection, cottonwood, demo); /investor-reporting in 0 of 4 |
| instrument | RUN | ui-smoke prints CLICKED:/CLICK-FAIL:/DID NOT LAND/CONSOLE[type]: (--console)/--netlog; proof-of-spec-check grades expect as a regex (S16) |

## R2.7 REFUSES TO ASSUME (round 2)

1. That a wire->view adapter may compute. It renames and restructures; a value the wire does not carry renders as the envelope's unknown, never a default.
2. That the counterpart's versioned contract artifact exists at this cut. It does not; the two raw pins are the authority until it lands, and a face pins it when it does.
3. That an operation without a declared route may keep a client method. It may not (no-route bound); the view says UNAVAILABLE and a row names the route.
4. That rc=0 from an instrument proves a render. Every smoke bar is a printed discriminator.
5. That a fixture map cut for one tab serves the page. Every map names the whole page's needs.
6. That the 700 weight can be fetched. It cannot without Andrew's word; 600 stands in and says so.
7. That a partner-firm session's reachability is anyone else's cell. The CTO ruled firmAccess.ts in scope for FE-s-14 (three entries, nothing else).

## R2.8 HOLDS
None. The typecheck cell is the ready root; nothing waits on a push.

---

# ROUND 3 -- v0.3 -- the recut on the CTO's ROUND-2 ANALYSIS

```json
{
 "round": 3,
 "decomp_version": "v0.3",
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@d1479bc5f0",
 "prd_version": "v0.6 -- UNCHANGED; 1.0.0_SA_CTO ruled the PRD deliberately not amended (96062), so round 3 carries no PRD event and the L4-R halves stay closed",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND2_20260912.md@f819d7cb7d",
 "slug_ref": "ABSENT -- see R3.8; round 2 produced NO REMEDIATION_v2 and the analysis answered the COO's drain-end read instead",
 "round2_cells": "FE-s-12..FE-s-17 COMPLETE and drained; FE-s-18 NON-TERMINAL and CARRIED (ruling 1)",
 "cells": 6,
 "cell_id_shape": "FE-s-<n> continuing from 19",
 "code_repo": "portal (nested git repo, gitlink in the workspace; branch DEV @f0443ba8)",
 "record_repo": "workspace (branch CLOUD @922d6fd570)",
 "producer_pins": {
  "contract": "docs/contracts/investor-reporting/v1/@58e387b454 -- RECORDED AS DATA, NOT AS A BAR (ruling 3). Four moves in round 2 (S20, S21, S28, S33); the fourth landed 14 minutes INSIDE a worker's pass.",
  "backend_prd": "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md@b8e98d5a4d (v0.14: StatusEnvelope.business_date state-conditional)"
 }
}
```

Round 2 delivered the seam, the composer, the mounted export flow, the packaged font and the evidence -- and the evidence FAILED, which is what it was for. `W1-S33` / `S30`: on portal DEV the Reporting and Holdings tab bodies cannot mount from any network response, and 420 of 422 tests pass over it because every test that exercises a tab body SEEDS its envelope. Round 3 is the six things the analysis ruled, as ONE issuance. Rounds 1 and 2 above are unchanged and their cells keep their statuses; the round-3 cells are additive.

## R3.1 THE RECTANGLE -- six cells, the analysis's seven rulings

| cell | ruling | write surface (portal unless stated) | serves | rows | wave | slot |
|---|---|---|---|---|---|---|
| `FE-s-19` | 2 the envelope-to-view seam | `contracts/adapt.ts`; `contracts/envelope.ts`; `src/api/endpoints/investor-reporting.ts`; `tabs/TabShell.tsx`; `state/status.ts`; `__tests__/fe-s-19/` | FWD-1, FWD-5, FWD-6 | W1-S33, S30, W2-S11 | A | ~1 |
| `FE-s-20` | 3 pin by CONTENT; retire the byte pin | `contracts/wire/`; `fixtures/wire/`; `__tests__/fe-s-13/` | FWD-1, FWD-6 | S20, S21, S28, S33, S35, W2-S10 | A | ~2 |
| `FE-s-23` | 5(a) the invocation-comparison limb | **workspace** `.tools/proof-of-spec-check.py`; `.tools/tests/` | the fabric's own record integrity | S31 | A | ~3 |
| `FE-s-24` | -- `RENDER_PACKAGE.fonts` names 3 of 4 | `render/manifest.ts`; `__tests__/fe-s-4/`; `__tests__/fe-s-17/` | FWD-8, FWD-12 | W1-S28 | A | ~4 |
| `FE-s-21` | 6 F7 renders a legitimately absent source date | `state/status.ts`; `tabs/StatusPanel.tsx`; `tabs/reporting/`; `__tests__/fe-s-21/` | FWD-5 | S29 | B | ~1 |
| `FE-s-22` | 4 the scoped capture-hash rule; W1-S36 | `scripts/ui-smoke.mjs`; `__tests__/fe-s-22/` | FWD-3, FWD-5 (the evidence plane) | W1-S36, S33 | B | ~2 |

**CARRIED, NOT RE-CUT:** `FE-s-18` stays OPEN at `<status>pending</status>` with `F18-AC3` and `F18-AC17` UNTOUCHED (ruling 1). It is re-run, never re-issued, once `FE-s-19` and `FE-s-20` are terminal and drained. No round-3 cell writes `__tests__/fe-s-18/`.

**Coverage by subtraction, three domains.**
(1) The analysis's rulings (denominator 7) MINUS what the cells serve: ruling 1 = FE-s-18 carried (no cell, by the ruling itself); 2 = FE-s-19; 3 = FE-s-20; 4 = FE-s-22; 5(a) = FE-s-22 (the prompt/record rule, a BOUND on every face) and 5(b) = FE-s-23 (the checker limb); 6 = FE-s-21; 7 = the thirteen C-S* rows stay armed and are 3.0.0_SA_CVO's, by the ruling = **0 uncovered**.
(2) The analysis's consolidated round-3 inputs (denominator 9: seam cell, content pinning, capture-hash rule, checker limb, W1-S28, F7, W1-S36, W2-S10, W2-S11) MINUS the cells: seam=19, pinning=20, hash=22, limb=23, W1-S28=24, F7=21, W1-S36=22, W2-S10=20, W2-S11=19 = **0 uncovered**.
(3) The PRD header's outcomes (denominator 8) MINUS those round 3 moves: FWD-1 {19,20}, FWD-3 {22}, FWD-5 {19,21,22}, FWD-6 {19,20}, FWD-8 {24}, FWD-12 {24} = **2 NOT MOVED, and named**: FWD-4 and FWD-11 were served to EXERCISABLE in round 2 and no round-3 ruling touches them; they wait on the L9 grade, not on a cell.

## R3.2 BOUNDS -- ALL ROUND-3 CELLS (rounds 1 and 2 bounds stand)

```
network     ⛔ BINDING, ruling 2. Every criterion of FE-s-19 DRIVES FROM A NETWORK RESPONSE. A criterion
            satisfiable by seeding `initialEnvelope` / `initialHoldingsEnvelope` / `initialReport` /
            `initialSnapshot` IS REFUSED AT THE CUT. The 420-of-422 blindness is exactly this shape.
negcontrol  ⛔ BINDING, ruling 2. Every NEW seam criterion is shown RED against today's bytes BEFORE it
            goes green against the fix, and the instance records BOTH runs. A seam criterion that has
            never failed is a seeded test wearing different clothes.
pinning     ⛔ ruling 3. A consumer cell pins the CONTENT it consumes -- route keys, required field
            sets, operation ids -- and records the producer vintage as DATA. A byte/sha pin on a
            producer artifact is REFUSED at the cut for a consumer cell. NON-APPLICATION: a cell whose
            subject IS the producer's bytes.
captures    ⛔ ruling 4, SCOPED not blanket. Where two fixtures differ in a field THAT CAPTURE CLAIMS TO
            RENDER, distinct hashes are ASSERTED. Where the differing field is not claimed, the set
            SAYS SO and identical hashes are ADMITTED. The blanket form is wrong.
face/prompt ⛔ ruling 5(a). Placeholder substitution (`<WS>`, `<PORT>`) is the ONLY edit permitted
            between this file's worker face and the spawned prompt. ANY other change lands in the FILE
            FIRST. S31 is the proof.
messages    ⛔ ruling 5(b). An issuer's continue message carries ACTS and MEASURED FACTS only. An
            unruled recommendation is omitted or marked NOT BINDING ON THIS ORDER. S32 is the proof:
            to a worker whose entire context is what the issuer sends, EVERY SENTENCE FROM THE ISSUER
            IS SPEC -- a property of the worker-face design, not a lapse by any worker.
refusal     every face instructs its worker to REFUSE a criterion it cannot satisfy as written and to
            report the refusal with its measurement. Three of round 2's six cut defects were caught
            this way and by nothing else.
typecheck   EVERY order carries `cd <WS>/portal && timeout 180 bun run typecheck; echo rc=$?` -> rc=0.
seating     ⛔ S28 as amended by S33: measure the target tree at SEATING time AND accept that the
            window is the worker's WHOLE PASS. A producer move mid-pass is a ROW, never a re-pin
            inside the round.
flip        the seating `<status>` flip is COMMITTED BEFORE the worktree is cut (S26).
channel     round-3 rows go to INVESTIGATION_v2.md; ids continue each slot's sequence (W1 from S36,
            W2 from S14, W3 from S12, W4 from S1).
gitlink     never stage `portal` in the workspace repo. PORTAL IS FROZEN: local DEV commits only, no
            push, no gitlink bump.
```

## R3.3 THE CELLS

### `FE-s-19` -- the envelope-to-view seam

The v1 envelope's state is parsed and then discarded, so every network-sourced response reaches the tabs as `UNCERTAIN` and the Reporting and Holdings bodies never mount. `envelope.ts` already builds `state: status?.state ?? 'READY'`; `api/endpoints/investor-reporting.ts:932` returns `parsed.data` on the non-status branch (the sibling `:930` returns `parsed.status`, so the parsed state EXISTS and is dropped); `adapt.ts:157` then fills `state: parts.state ?? EXPLICIT_UNKNOWN_STATE` with `EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN'` (`:103`); `TabShell.tsx:133`, `:148`, `:150` gate on `envelopeFromAvailability(<x>.availability)`. **The design question is this cell's to answer** -- what the view's state derives from once the envelope carries it, and whether `availability` remains the carrier -- and it must be answered here rather than in an evidence cell. Also carries `W2-S11`: `LiveClient` still ACCEPTS a pre-envelope body carrying none of `contract_version` / `operation` / `firm_id`, so the strict parser has a bypass on the same plane.

### `FE-s-20` -- pin by content; retire the byte pin

`contracts/wire/index.ts:48`'s `WIRE_SCHEMA_PINS` is a sha-per-schema table and `__tests__/fe-s-13/producer-fixtures.test.ts:104` asserts every live digest equals its pin. Four producer moves in one round reddened it; the fourth (`58e387b454`) changed ONE file and left `WIRE SCHEMA PINS FRESH: 10 of 11`. Replace the byte table with the CONTENT the consumer actually depends on -- the operation ids it calls, the route keys, the required field sets it reads -- and record the producer vintage as a DATA field the test PRINTS and never asserts. Also carries `W2-S10`: re-basing `fixtures/smoke/default.json` to v1 DECLARED paths broke two pins on the counterpart's replay corpus.

### `FE-s-23` -- the checker cannot see a prompt/record divergence (WORKSPACE cell)

`proof-of-spec-check.py` returned VALID over an instance whose recorded invocations were not the invocations its task order carried (`S31`). Add the limb: each recorded invocation is compared to its criterion's invocation in the governing TO, modulo the declared placeholders, and a mismatch is a violation naming both strings. **This is the only cell writing the workspace repo and it touches no portal path.** It carries its own negative control: a seeded divergence must make the checker REFUSE, and the checker must still pass the round-2 instances that are honestly aligned.

### `FE-s-24` -- `RENDER_PACKAGE.fonts` names three of four packaged faces

`render/manifest.ts:114`'s `RENDER_PACKAGE.fonts` is a flat array naming 3 files while four are packaged; `__tests__/fe-s-4/manifest.test.ts` asserts a length no round-2 grant could change, and `__tests__/fe-s-17/fonts.test.ts:294` reads the flat array. FE-s-18 correctly named it and left it (`W1-S28`). Make the array name all four and move the length assertion to a DERIVED denominator rather than a literal.

### `FE-s-21` -- F7 renders a legitimately absent source date

Under IRPT_BCKEND v0.14 `business_date` is state-conditional: REQUIRED on the five answer-bearing states, and legitimately ABSENT (never null) on QUEUED, RUNNING, UNAVAILABLE, FAILED. `state/status.ts:170`'s `formatSourceAge` and the panels that consume it must render "no source age yet" on those four, never an error and never a missing-data defect. Shares `state/status.ts` with FE-s-19 and is therefore SEQUENCED BEHIND IT -- never concurrent.

### `FE-s-22` -- the evidence plane's two instruments

(a) The scoped capture-hash rule as a REUSABLE assertion under `__tests__/fe-s-22/`: fixtures differing in a CLAIMED field assert distinct hashes; a differing UNCLAIMED field is declared and identical hashes admitted. It does NOT touch `__tests__/fe-s-18/` -- FE-s-18's own literal arm stays as cut. (b) `W1-S36`: `scripts/ui-smoke.mjs:341` compares `window.location.pathname` against the full route STRING, so `DID NOT LAND` prints on EVERY query-bearing route and is EQUALLY UNABLE to report a genuine failure on one -- a detector that always fires is the mirror of one that never can. Five of twelve round-2 captures carry the noise. Fix is one line (`new URL(ORIGIN + route).pathname`); the cell proves BOTH directions (a landing query route prints no DID NOT LAND; a genuinely bad route still does).

## R3.4 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-19 <- (none)                       READY ROOT
  FE-s-20 <- (none)                       READY ROOT
  FE-s-23 <- (none)                       READY ROOT   (workspace repo; no portal path)
  FE-s-24 <- (none)                       READY ROOT
  FE-s-21 <- FE-s-19                      (shares state/status.ts -- never concurrent)
  FE-s-22 <- FE-s-19                      (its captures must be taken on the fixed seam)
  FE-s-18 <- FE-s-19, FE-s-20             CARRIED, re-run only; not part of this issuance

  weakly connected components:  M = 3     ready roots at issuance: R = 4
  waves by depth:  A={19,20,23,24}   B={21,22}   then the FE-s-18 re-run
  max concurrent width: 4 (wave A)

  ~1  FE-s-19 -> FE-s-21
  ~2  FE-s-20 -> FE-s-22        (22 is seated when 19 is terminal, not when 20 is)
  ~3  FE-s-23
  ~4  FE-s-24
```

**Fan-out: `4 of 4 ready roots at issuance, 4 slots, cap 8, reason: four disjoint write surfaces with no shared file`.** All six orders are issued in the one issuance; FE-s-21 and FE-s-22 carry `blocked` until FE-s-19 is terminal.

## R3.5 RULE 24 RECORD (round 3)

| postulate | how |
|---|---|
| (i) MECE | three domains by subtraction in R3.1: rulings 7-7=0; consolidated inputs 9-9=0; outcomes 8-6=2 NOT MOVED AND NAMED (FWD-4, FWD-11 wait on the L9 grade, not on a cell). Cells partition by FILE, not by directory: `contracts/` is SPLIT -- FE-s-19 owns `adapt.ts` and `envelope.ts`, FE-s-20 owns `wire/`. `state/status.ts` is shared by FE-s-19 and FE-s-21 and is sequenced, never concurrent. `__tests__/fe-s-18/` is written by NO round-3 cell. |
| (ii) same grain | (write region, ruling) per cell, as rounds 1 and 2. FE-s-23 is the one cell at the FABRIC grain (workspace `.tools/`) and is stated as such rather than folded into a portal cell. |
| (iii) intent | one axis: the consumer's state comes from the wire and is proven on the path a browser actually takes. FE-s-23's intent is the record's integrity, not the product's -- a different axis, which is why it is its own cell and not a limb of another. |
| (iv) state | moves FWD-1/5/6 toward EXERCISABLE on a MOUNTED, NETWORK-DRIVEN view. Does NOT move: any grade to REALIZED (the CTO's read); FWD-4 and FWD-11 (round 2 moved them; they wait on L9); the backend's routes, handlers or contract artifact; the portal freeze; S27 (the CVO's L9 judgment); the thirteen armed C-S* rows (3.0.0_SA_CVO's, ruling 7). |

## R3.6 BATTERY DISPOSITION (round 3)

| lens | disposition | denominator / reason |
|---|---|---|
| comp-schedule / comp-iam | DECLARED-NOT-APPLICABLE | no scheduled producer and no IAM-gated resource among these six write surfaces; FE-s-23 writes a repo-local checker |
| comp-adversary | RUN at L4 on v0.6 (both halves SIGNED, ADMITTED) | carried; PRD unchanged this round (96062), so no new complement source |
| the defect itself | RUN | source read at the pin by the issuer: `investor-reporting.ts:932`, `TabShell.tsx:133/:148/:150`, `adapt.ts:103/:157`, `envelope.ts` -- and a comp-find census of `envelopeFromAvailability`, 34 hits across 305 files, DEF=3 |
| the blindness | RUN | every tab-body test seeds its envelope: fe-s-5/controls, fe-s-5/fields, fe-s-5/states, fe-s-10/parity (`initialEnvelope:`), fe-s-10/tabs-mounted (`initialHoldingsEnvelope:`). 0 of them traverse the network path |
| producer vintage | RUN, AS DATA | `docs/contracts/investor-reporting/v1/@58e387b454`; 4 moves during round 2; `WIRE SCHEMA PINS FRESH: 10 of 11` at this cut |
| tree at the cut | RUN | portal DEV f0443ba8: typecheck rc=0; `bun test src/pages/InvestorReporting` 419 pass / 1 skip / 2 fail, both fails named (F18-AC3's collision; the one stale pin) |
| instrument | RUN, WITH A KNOWN DEFECT | `ui-smoke.mjs:341` prints `DID NOT LAND` on every query-bearing route (W1-S36) -- FE-s-22's own subject, so every OTHER cell's smoke criteria key on `CONSOLE[log]:` discriminators and never on that line |

## R3.7 REFUSES TO ASSUME (round 3)

1. That a test which mounts a component exercises the path a browser takes. Round 2's suite mounted every tab body and traversed the network path zero times.
2. That a criterion which passes has been shown capable of failing. Ruling 2's negative control exists because it had not been.
3. That a producer artifact can be pinned by bytes while the producer is moving. Four instances in one round, the fourth INSIDE a worker's pass.
4. That an issuer's message is context. To a worker it is spec (S32).
5. That the worker face in this file is the face the worker received. It was not, once (S31), and no gate compared them.
6. That a capture that renders is a capture that DISCRIMINATES. Three fixtures produced one byte-identical image and every criterion over them passed.
7. That a round-2 row is adjudicated. It is not -- see R3.8.

## R3.8 HOLDS

**None blocking.** One deviation, named because a successor must not read it as complete:

⚠ **ROUND 2 PRODUCED NO CVO SLUG.** `surprise-channel/remediations/` holds `REMEDIATION_v1.md` only, and `3.0.0_SA_CVO` states "No L9 grade, no slug: IB-rt-2 open, FE-s-18 non-terminal." The spine's L10 is the CVO's slug to the CTO; what actually happened is that the CTO answered the COO's DRAIN-END READ and issued the round-2 analysis from it. `ADJUDICATION_v2.md` exists and the CVO's watermark is current (v2 at 54 of 57), so the rows ARE compiled -- they are not ADJUDICATED, and no round-2 judgment criterion (`F15-AC12`, `F16-AC10`, `F18-AC18`) has been graded.

**So round 3 is cut on the CTO's analysis, not on an adjudicated slug, and its cells inherit no L9 disposition.** This is legible and was ruled by the CTO; it is recorded here rather than in prose elsewhere because the next reader of this rectangle needs to know that the row set behind it is compiled and un-graded. The L9 grades and the slug remain owed for round 2 and are `3.0.0_SA_CVO`'s; they are not a precondition of this issuance and no cell here waits on them.

---

# ROUND 4 -- v0.4 -- the recut on the CTO's ROUND-3 ANALYSIS

```json
{
 "round": 4,
 "decomp_version": "v0.4",
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@d1479bc5f0",
 "prd_version": "v0.6 -- UNCHANGED; no round-4 ruling touches the PRD, so the L4-R halves stay closed",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND3_20260912.md@b453306a65",
 "slug_ref": "ABSENT -- rounds 2 and 3 both produced NO REMEDIATION; the CTO answered the COO's drain-end read each time. See R4.8.",
 "round3_cells": "FE-s-19..FE-s-24 ALL COMPLETE and drained; FE-s-18 NON-TERMINAL and CARRIED for a SECOND consecutive round (ruling B)",
 "cells": 4,
 "cell_id_shape": "FE-s-<n> continuing from 25",
 "code_repo": "portal (gitlink in the workspace; branch DEV @237a9027)",
 "record_repo": "workspace (branch CLOUD @c968d44558)",
 "producer_pins": {
  "contract": "docs/contracts/investor-reporting/v1/@58e387b454 -- RECORDED AS DATA, NEVER AS A BAR (round-3 ruling 3, and the consumer's byte pin is retired)",
  "backend_prd": "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md@b8e98d5a4d (v0.14) -- SOUND AS PRODUCER LAW and NOT re-cut (ruling A)"
 }
}
```

Round 3 fixed the seam and proved it on the path that could not fake it. Round 4 is what round 3's own evidence exposed: **the v0.14 amendment is sound as producer law and its semantics do not survive the consumer boundary** (`3.0.0_SA_CVO` C-S50, four independent measurements), plus the three mechanism rulings round 3 earned. Rounds 1-3 above are unchanged and keep their statuses; round-4 cells are additive.

## R4.1 THE RECTANGLE -- four cells, seven rulings

| cell | ruling | write surface (portal unless stated) | serves | rows | wave | slot |
|---|---|---|---|---|---|---|
| `FE-s-25` | A the consumer boundary | `contracts/adapt.ts`; `contracts/index.ts`; `state/status.ts`; `__tests__/fe-s-13/gen-wire.ts`; `contracts/wire/`; `__tests__/fe-s-25/` | FWD-1, FWD-5, FWD-6 | W1-S26, W1-S41, W1-S42, W1-S43, C-S50 | A | ~1 |
| `FE-s-26` | B the fixture cell | `fixtures/smoke/` (the three Holdings maps); `__tests__/fe-s-26/` | FWD-3, FWD-5 | S44, W1-S33 (residual), C-S46 | A | ~2 |
| `FE-s-27` | C environmental preconditions | `__tests__/fe-s-19/`; `__tests__/fe-s-27/` | the evidence plane | W1-S45, S48 | A | ~3 |
| `FE-s-28` | D the opt-in becomes mandatory | **workspace** `.tools/to-pipeline-gate.py`; `.tools/tests/` | the fabric's record integrity | S38, S31, S43 | A | ~4 |

**CARRIED, NOT RE-CUT, FOR THE SECOND ROUND:** `FE-s-18` stays OPEN at `<status>pending</status>` with `F18-AC3` and `F18-AC17` UNTOUCHED (ruling B: "Not amended, not re-scoped, not passed with a caveat"). It is RE-RUN once `FE-s-26` is terminal and drained. **No round-4 cell writes `__tests__/fe-s-18/` or the deliverables folder it captures into.**

**RULED ELSEWHERE, DELIBERATELY NOT CELLS HERE:** ruling E (the third limb) is ADOPTED as a BOUND below -- `FE-s-22` already built it and no code change is owed. Ruling F (read the face at the named commit) is a BOUND, not a cell. Ruling G (`W2-S15`, the producer-side byte pin) is **`1.0.0_SA_CTO`'s to route into IRPT_BCKEND and is NOT round 4's** -- it is another project's surface and this seat may not cut into it.

**Coverage by subtraction, three domains.**
(1) The analysis's rulings (denominator 7) MINUS what covers each: A=FE-s-25; B=FE-s-26 plus the FE-s-18 re-run; C=FE-s-27; D=FE-s-28; E=R4.2 BOUND (no code owed); F=R4.2 BOUND; G=the CTO's, by the ruling = **0 uncovered**.
(2) C-S50's rows (denominator 4: W1-S26, W1-S41, W1-S42, W1-S43) MINUS FE-s-25's criteria = **0 uncovered**, with W1-S43 first by the ruling.
(3) The PRD header's outcomes (denominator 8) MINUS those round 4 moves: FWD-1 {25}, FWD-3 {26}, FWD-5 {25,26}, FWD-6 {25} = **4 NOT MOVED AND NAMED** -- FWD-4, FWD-8, FWD-11, FWD-12 were served in rounds 2-3 and wait on the L9 grade, not on a cell.

## R4.2 BOUNDS -- ALL ROUND-4 CELLS (rounds 1-3 bounds stand)

```
precond    ⛔ RULING C, AND IT BINDS EVERY CRITERION IN THIS ISSUANCE. A criterion with an
           ENVIRONMENTAL precondition -- a dev server, a port, a network, a browser -- DECLARES it in
           its own text, and an absent precondition renders SKIPPED or BLOCKED, NEVER FAILED. Measured
           cause: at ONE commit the suite read 452/1/3 with no server on 5181 and 454/1/1 with one, so
           a down server rendered as a code defect. ⛔ AND NO CRITERION IN THIS ROUND CARRIES A BARE
           WHOLE-SUITE `N fail` BAR: if a cell needs one, it names the precondition beside it and
           prints the failing test NAMES, never a count alone. A count is a property of the
           ENVIRONMENT as much as of the CUT.
survives   ⛔ RULING A. A criterion about a contract distinction asserts THE DISTINCTION SURVIVES AT
           THE VIEW, never that the producer emits it. ADMITTED means the text was reviewed; it does
           NOT mean the described behaviour exists -- 3.0.0_SA_CVO's C-S50, adopted verbatim by the CTO.
           `?? null` is REFUSED as a pattern wherever the contract distinguishes ABSENT from null.
domain     ⛔ RULE 24, as it landed on the CTO in W1-S41: a subtraction's DOMAIN must be the CLAIM's
           population, and choosing the domain is itself a claim. The producer's nine-state enum and
           the view's closed `EnvelopeState` are DIFFERENT NINES. Any cell partitioning states names
           WHICH PLANE it partitions and proves the image lands in the other.
faceread   ⛔ RULING F. Placeholder substitution is the ONLY edit between this file's worker face and
           a spawned prompt, anything else lands in the FILE first -- AND an amendment NAMES ITS
           COMMIT, with the worker reading the face at that commit via `git show <commit>:<path>`
           beside a POSITIVE CONTROL. An amendment made after a cut is READABLE and NOT CARRIED.
captures   ⛔ RULING E, third limb: a fixture that does NOT carry the claimed field is a DEFECTIVE
           FIXTURE, not an admitted collision. Already built by FE-s-22; no code is owed, and any
           capture set in this round uses it rather than re-deriving it.
messages   an issuer's continue message carries ACTS and MEASURED FACTS only; an unruled
           recommendation is omitted or marked NOT BINDING (S32).
append     ⛔ WHEN AN ACT'S INTENT IS AN APPEND, READ THE DIFFSTAT (S47/W1-S48). A channel append
           whose diff touches lines it did not write is doing something else; every gate over that
           file is a CONTENT check and none of them sees a line-ending rewrite. Write the channel
           with `newline='\n'`.
refusal    every face instructs its worker to REFUSE a criterion it cannot satisfy as written and
           report the refusal with its measurement. Every round so far: the refusals were right.
typecheck  EVERY order carries `cd <WS>/portal && timeout 180 bun run typecheck; echo rc=$?` -> rc=0.
channel    round-4 rows go to INVESTIGATION_v2.md; READ THE WHOLE PLANE (v1 AND v2) before minting an
           id -- the gate allocates across both documents and a number named in a face was wrong once
           (S36). No face in this round names a starting number.
gitlink    never stage `portal` in the workspace repo. PORTAL IS FROZEN: local DEV commits only.
```

## R4.3 THE CELLS

### `FE-s-25` -- the consumer boundary: the distinction has to survive arrival

The v0.14 amendment is SOUND as producer law (ruling A) and four independent measurements say its semantics do not reach the view. All four are this cell's, `W1-S43` first:

- **`W1-S43`, the one that bites hardest.** `contracts/adapt.ts:376` reads `const asOf = wire.source_dates.as_of ?? null` inside `adaptStatusEnvelope` (`:375`). The `?? null` COLLAPSES ABSENT AND NULL -- the exact distinction the amendment was written to create, and whose reason the CTO put into the schema's own `$comment`. The contract says ABSENT, never null; the consumer erases the difference on arrival.
- **`W1-S42`.** The clause governs `business_date`; the age surface computes from `source_dates.as_of` (`adapt.ts:376`) while `state/status.ts:343`'s `sourceDateFact` reads `sourceDates.business_date`. So a READY envelope carrying the REQUIRED `business_date` renders "Source time unknown".
- **`W1-S41`.** `contracts/adapt.ts:222`'s `STATE_FOR_WIRE` maps the producer's nine onto the view's closed `EnvelopeState` (`contracts/index.ts:68`), and QUEUED/RUNNING collapse onto LOADING -- so a queued job renders the label "Loading" and only `IR-JOB-QUEUED` distinguishes it from a browser that has not answered.
- **`W1-S26`.** `__tests__/fe-s-13/gen-wire.ts` tests `allOf` BEFORE `type`/`properties`, so regenerating StatusEnvelope at v0.14 emitted `export interface StatusEnvelopeWire unknown` and dropped all seven properties. The CONTRACT is sound and the GENERATOR degrades on a valid conditional.

⛔ **EVERY CRITERION ASSERTS THE DISTINCTION SURVIVES AT THE VIEW.** A test that proves the producer emits the right bytes proves nothing this cell is for.

### `FE-s-26` -- the fixture cell: three maps that can actually differ

`F18-AC3` has failed for two rounds and cannot pass until the three Holdings smoke maps carry DISTINCT `status` members. Measured twice independently (issuer 84 envelopes / 36 maps / 3 with `status`; worker 62/16/3): `fe-s-18-holdings-{observed,target,missing-attribution}.json` read **envelopes=9, with_status=0 EACH**. `status` is the only wire carrier of a state, so under the correct seam those three render identical panels BY THE CONTRACT.

Give each map a `status` that makes its basis visible at the view, using FE-s-22's third limb to prove the set is no longer DEFECTIVE. ⛔ **This cell does NOT re-take a capture and does NOT touch `__tests__/fe-s-18/`** -- FE-s-18 is carried untouched and re-runs itself afterwards.

### `FE-s-27` -- a precondition that is declared, and an absence that is not a failure

At ONE commit: 452/1/3 with no dev server on 5181, 454/1/1 with one. `__tests__/fe-s-19/mounted-from-wire.test.ts` hard-codes `PORT = '5181'` and declares a precondition no runner sees, so a DOWN SERVER RENDERS AS A CODE DEFECT and a worker on any other slot's port cannot pass those two tests at all. The test's own note covers the harmless direction (a down server can never read as a pass) and not the dangerous one.

Make the precondition explicit and make its absence render SKIPPED or BLOCKED, never FAILED; take the port from the environment rather than a literal. ⭐ **The cell's own proof is the two-way measurement**: the same command, at one commit, with and without the precondition.

### `FE-s-28` -- an integrity check the checked party may decline to arm is not an enforcement (WORKSPACE cell)

`FE-s-23` shipped the invocation-comparison limb with ENFORCE gated on a `<placeholders>` declaration in the task order, because at default-ENFORCE the two constraints it was given were arithmetically unsatisfiable (318 divergent rows across 874 comparable). That was the right call at the time and the CTO has now ruled it out (ruling D): **the declaration becomes MANDATORY at the L6 gate**, so an issuance cannot be cut without it. NON-APPLICATION: none -- an opt-in integrity check has no honest scope.

This is the only cell writing the workspace repo and it touches no portal path.

## R4.4 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-25 <- (none)     READY ROOT   contracts/, state/, gen-wire
  FE-s-26 <- (none)     READY ROOT   fixtures/smoke/ only
  FE-s-27 <- (none)     READY ROOT   __tests__/fe-s-19/ only
  FE-s-28 <- (none)     READY ROOT   workspace .tools/ only
  FE-s-18 <- FE-s-26    CARRIED, re-run only; NOT part of this issuance

  weakly connected components:  M = 4      ready roots at issuance: R = 4
  waves by depth:  A={25,26,27,28}   then the FE-s-18 re-run
  max concurrent width: 4

  ~1 FE-s-25   ~2 FE-s-26   ~3 FE-s-27   ~4 FE-s-28
```

**Fan-out: `4 of 4 chains, cap 8, reason: four disjoint write surfaces, no shared file in any pair`.** All four are ready roots; nothing carries `blocked`.

## R4.5 RULE 24 RECORD (round 4)

| postulate | how |
|---|---|
| (i) MECE | three domains by subtraction in R4.1: rulings 7-7=0; C-S50's rows 4-4=0; outcomes 8-4=4 NOT MOVED AND NAMED. Cells partition by FILE: `contracts/` is FE-s-25's entirely this round (FE-s-20 is terminal); `fixtures/smoke/` is FE-s-26's; `__tests__/fe-s-19/` is FE-s-27's; `.tools/` is FE-s-28's. `__tests__/fe-s-18/` is written by NO cell. |
| (ii) same grain | (write region, ruling) per cell; FE-s-28 is at the FABRIC grain and is stated as such rather than folded into a portal cell, as FE-s-23 was in round 3. |
| (iii) intent | one axis: what the contract distinguishes must still be distinguishable at the view, and what a criterion depends on must be declared. FE-s-28's intent is the record's integrity -- a different axis, its own cell. |
| (iv) state | moves FWD-1/5/6 toward EXERCISABLE on a consumer that preserves the producer's distinctions. Does NOT move: any grade to REALIZED; FWD-4/8/11/12 (served in rounds 2-3, waiting on L9); the producer's contract (ruling A: it STANDS); W2-S15 (the CTO's, ruling G); the portal freeze. |

## R4.6 BATTERY DISPOSITION (round 4)

| lens | disposition | denominator / reason |
|---|---|---|
| comp-schedule / comp-iam | DECLARED-NOT-APPLICABLE | no scheduled producer, no IAM-gated resource among these four surfaces |
| comp-adversary | RUN at L4 on v0.6 (both halves SIGNED, ADMITTED) | carried; PRD unchanged, and ruling A explicitly does NOT re-cut the producer contract |
| the four defects | RUN by the issuer at the pin | `adaptStatusEnvelope` adapt.ts:375 with `as_of ?? null` at :376; `STATE_FOR_WIRE` adapt.ts:222 against `ENVELOPE_STATES` contracts/index.ts:68; `sourceDateFact` state/status.ts:343 reading `business_date`; the generator at `__tests__/fe-s-13/gen-wire.ts` (comp-find: 1 of 325 files) |
| the fixture gap | RUN | 84 v1 envelopes across 36 smoke maps, 3 carrying `status`; the three Holdings maps at 0 of 9 each |
| the precondition | RUN, TWO WAYS AT ONE COMMIT | portal DEV 237a9027: no server 452/1/3, server on 5181 454/1/1. The delta is exactly F19-AC4 and F19-AC5 |
| tree at the cut | RUN | portal DEV 237a9027 typecheck rc=0; the one real failure is F18-AC3's collision |
| instrument | RUN, WITH KNOWN DEFECTS NAMED | `ui-smoke.mjs`'s DID-NOT-LAND defect is FIXED (FE-s-22, one line, both arms proven); `--help` does not exist on proof-of-spec-check and returns rc=2 (S36); the checker's own limb is live and ENFORCE is opt-in until FE-s-28 lands |

## R4.7 REFUSES TO ASSUME (round 4)

1. That a signed-off PRD half means the described behaviour exists. It means the TEXT was reviewed -- C-S50, adopted by the CTO against its own signature.
2. That a subtraction with a printed denominator is over the right domain. W1-S41 is Rule 24 landing on the seat that wrote the ruling.
3. That a failure count is a property of the code. It is equally a property of the environment (W1-S45).
4. That an integrity check the checked party may decline to arm is an enforcement (ruling D).
5. That a fixture which varies a claimed field can exercise it. It must also be REACHABLE at the view (ruling E's third limb).
6. That "the file is authority" identifies a file. It does not name WHICH commit (ruling F).
7. That a gate over a file sees everything about that file. Three gates over the channel are all CONTENT checks and none saw a whole-file line-ending rewrite (S47).

## R4.8 HOLDS

**None blocking.** Two deviations recorded rather than buried, both unchanged from round 3 and now in their second and third rounds:

⚠ **NO CVO SLUG HAS BEEN CUT FOR ROUNDS 2 OR 3.** `surprise-channel/remediations/` holds `REMEDIATION_v1.md` only. Both round-2 and round-3 analyses answered the COO's DRAIN-END READ instead, which the spine's L10 does not describe. `ADJUDICATION_v2.md` exists, the CVO's watermark is CURRENT (v2 at 91 of 93) and it has dispositioned every row it owns -- so the rows ARE compiled and adjudicated in substance, and no round-2 or round-3 JUDGMENT criterion (`F15-AC12`, `F16-AC10`, `F18-AC18`, `F19-AC10`, `F20-AC9`, `F21-AC8`, `F22-AC9`, `F23-AC7`) has been GRADED. Round 4 inherits no L9 disposition and no cell waits on one.

⚠ **`FE-s-18` IS NOW CARRIED INTO ITS THIRD ROUND.** Cut in round 2, non-terminal at the round-2 close, non-terminal at the round-3 close, and its blocker is `FE-s-26` in this one. Recorded so that the length of the carry is visible as a fact rather than as an accident.

---

# ROUND 5 -- v0.5 -- the recut on the CTO's ROUND-4 ANALYSIS

```json
{
 "round": 5,
 "decomp_version": "v0.5",
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@d1479bc5f0",
 "prd_version": "v0.6 -- UNCHANGED; every round-5 ruling applies ratified PRD text (analysis s.2, s.7), so no L4-R half re-opens",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND4_20260913.md@4f6c7abc7b (s.5 inputs 1-7; s.7 addendum items 6, 8-11; s.7 answer to 96406)",
 "slug_ref": "3.0.0_SA_CVO msg 96386, record org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND4_L8_L9_20260913.md@be3b6849a9 -- the FIRST IRPT_FNTEND round to reach L10 in spine order; late rounds 2-3 slug msg 96389 @49ef1fd1b1",
 "andrew_direct": "card 6, ~18:4xZ 2026-09-13, recs approved @e2210bf34c -- gate (viii) grades a MODIFICATION of an order that already declares the element",
 "round4_cells": "FE-s-25..FE-s-28 ALL COMPLETE and drained; FE-s-18 COMPLETE and drained after three rounds carried",
 "cells": 8,
 "cell_id_shape": "FE-s-<n> continuing from 29",
 "code_repo": "portal (gitlink in the workspace; branch DEV @c2eb8eb4, measured)",
 "record_repo": "workspace (branch CLOUD)"
}
```

Round 4's finding, one layer further in than round 2's: **round 3 fixed the seam, and the gate behind it withholds what the seam now delivers.** HoldingsTab mounts its body on READY only (`HoldingsTab.tsx:90`), ReportingTab only where `isCompleteState` admits READY and STALE (a designed, tested choice), and PrintEntry checks no report state at all. The PRD already rules the direction: FWD-3 (a PARTIAL result, and the PDF carries the same values), FWD-5 (missing attribution stays VISIBLE), FWD-6 (incomplete never shown as complete). Rounds 1-4 above are unchanged and keep their statuses; round-5 cells are additive.

## R5.1 THE RECTANGLE -- eight cells, and the checker limbs first

| cell | ruling | write surface (portal unless stated) | serves | rows | wave | slot |
|---|---|---|---|---|---|---|
| `FE-s-29` | M(i), M(ii), Q, card 6 -- the checker limbs | **workspace** `.tools/to-pipeline-gate.py`; `.tools/proof-of-spec-check.py`; `.tools/tests/` | the evidence plane | S53, S56, W4-S7, S42 (substrate half), C-S67 | A | ~4 |
| `FE-s-30` | H -- one availability gate, and Reporting under it | `state/availability.ts` (NEW); `tabs/reporting/`; `__tests__/fe-s-5/states.test.ts`; `__tests__/fe-s-30/` | FWD-3, FWD-6 | C-S57, S30 (class) | B | ~1 |
| `FE-s-33` | the fixture cell | three smoke maps + the Holdings maps + `__tests__/fe-s-18/gen-fixtures.ts`; `__tests__/fe-s-33/` | FWD-3, FWD-5, FWD-11 (evidence) | W1-S51, W1-S52, W1-S53 | B | ~2 |
| `FE-s-34` | K + O -- the relabel | `state/status.ts`; `tabs/analysis/StageDisplay.tsx`; `tabs/analysis/VariantSelector.tsx`; `__tests__/fe-s-34/` | FWD-4, FWD-6 | F25-AC12, W1-S46, C-S65 | B | ~3 |
| `FE-s-35` | P + W1-S20 -- the wire boundary | `src/api/endpoints/investor-reporting.ts`; `contracts/envelope.ts`; `contracts/adapt.ts` (report_title only); `tabs/analysis/composer.ts` (report_title only); `__tests__/fe-s-1/`; `__tests__/fe-s-13/`; `__tests__/fe-s-19/pre-envelope.test.ts`; `__tests__/fe-s-35/` | FWD-1, FWD-4, FWD-6 | W1-S39, W2-S11, C-S65, W1-S20 | B | ~5 |
| `FE-s-36` | N -- the output-vocabulary limb at L6 | **workspace** `.tools/to-pipeline-gate.py`; `.tools/tests/` | the evidence plane | S55, C-S58 | B | ~4 |
| `FE-s-31` | H (export) + J + W2-S12/W3-S5 | `render/PrintEntry.tsx`; `render/Page.tsx`; `render/performance/PerformanceDocument.tsx`; `render/analysis/AnalysisDocument.tsx`; `export/Preview.tsx`; `export/ExportButton.tsx`; `export/submit.ts`; `__tests__/fe-s-31/` | FWD-3, FWD-4, FWD-6, FWD-8 | C-S57, S27, C-S68, W2-S12, W3-S5 | C | ~1 |
| `FE-s-32` | I -- Holdings under the gate, (a) as its check | `tabs/holdings/`; `__tests__/fe-s-26/renders-differently.test.ts`; `__tests__/fe-s-22/capture-hash.test.ts` (DISTINCTION verdict only); `__tests__/fe-s-32/` | FWD-5, FWD-6 | W2-S21, W1-S35, C-S57 | C | ~2 |

**Coverage by subtraction, three domains.**
(1) The round-5 inputs (denominator 13: s.5 items 1-7; s.7 items 8, 9, 10a, 10b, 11; card 6; the FE-s-18 bound-5 DISTINCTION freeze) MINUS what covers each: 1=FE-s-29; 2=FE-s-30+FE-s-31; 3=FE-s-32; 4=FE-s-33; 5=FE-s-31; 6 (K widened by O)=FE-s-34; 7=FE-s-36; 8=FE-s-35; 9=FE-s-29; 10a (`export/submit.ts:87`)=FE-s-31; 10b (`report_title`)=FE-s-35; card 6=FE-s-29; the DISTINCTION freeze=FE-s-32; **11 = WITHDRAWN, already fixed** (`scripts/ui-smoke.mjs:341` changed at portal `25062fce` by FE-s-22, both arms proven by F22-AC6/AC7; measured by this seat, confirmed by 1.0.0_SA_CTO @4f6c7abc7b) = **0 uncovered**.
(2) The PRD header's outcomes (denominator 8: FWD-1, 3, 4, 5, 6, 8, 11, 12) MINUS those round 5 moves: FWD-1 {35}, FWD-3 {30,31,33}, FWD-4 {31,34,35}, FWD-5 {32,33}, FWD-6 {30,31,32,34,35}, FWD-8 {31}, FWD-11 {33} = **1 NOT MOVED AND NAMED**: FWD-12 (design conformity), served in rounds 2-3.
(3) The rows the analysis routes here MINUS their carrying cell: W2-S21 -> FE-s-32 (ruling I is its disposition); W1-S51/S52/S53 -> FE-s-33; W1-S35 -> FE-s-32; W1-S39 + W2-S11 -> FE-s-35; W1-S46 -> FE-s-34; W2-S12 + W3-S5 -> FE-s-31; W1-S20 -> FE-s-35; S53 + S56 + W4-S7 -> FE-s-29; S42's substrate half -> FE-s-29 (ruling Q's route); S55 -> FE-s-36; C-S68 -> FE-s-31; W1-S36 -> none, WITHDRAWN = **0 uncovered**.

**NOT ROUND 5's:** ruling L (the target-basis UNCERTAIN rule belongs in the producer's contract -- IRPT_BCKEND's L4, carried by 1.0.0_SA_CTO); the producer side of the smoke-map seam (IRPT_BCKEND-S51); C-S71's seven INERT wire gaps; W2-S16.

## R5.2 BOUNDS -- ALL ROUND-5 CELLS (rounds 1-4 bounds stand)

```
checker    ⛔ RULING M's SEQUENCING. FE-s-29 lands before any other round-5 cell's proof is checked, so
first      no round-5 grade moves under it: every wave-B and wave-C worktree is cut AFTER FE-s-29 is
           drained, so the checker a worker validates with is the new one. Until then the hand-read of
           every count bar's deciding line stands.
anchors    ⛔ every count bar is LEFT-anchored `(?<![0-9])` and every bound RIGHT-anchored `(?![0-9])`,
           NEVER `\b` -- a `\b`-anchored bar false-FAILS coloured output (1.0.0_SA_CTO 96370, tested with
           the grader's own call). Measured at the cut: proof-of-spec-check grades <expect> with
           re.search(expect, output_evidence, S|M) (`:106`).
evidence   `output_evidence` carries the DECIDING invocation's output and nothing else; earlier runs and
           BEFORE notes go in `status_reason` (96370). No anchor closes shape (b); hygiene does.
drives     ⛔ 1.0.0_SA_CTO @4f6c7abc7b: EVERY round-5 criterion declares `drives="network"` or
           `drives="none"`. A criterion whose proof requires a response to travel the real network path
           or a real browser is `network`; everything else is `none`. An explicit `none` is enforcement,
           not a waiver. FE-s-29 builds the limb; these faces declare ahead of it.
plane      ⛔ RULING H PARTITIONS ON THE PRODUCER PLANE (confirmed 96408). A body with NO wire state falls
           back to `EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN'` (`contracts/adapt.ts:103`) -- the SAME view state
           as a producer's UNCERTAIN -- and must NEVER render as an answer. Gate on
           `Availability.producerState` (`contracts/index.ts:127`), never on the view's EnvelopeState
           alone. F19-AC5 ("UNCERTAIN WITHOUT A WIRE STATE: 2 of 2") stays green.
overturn   ⛔ A test that asserts the behaviour a ruling OVERTURNS is granted to the cell that overturns it,
           with a bound: change only the claim the ruling changes, cite the ruling, show it both ways.
           Measured at the cut (S55 control 2): fe-s-5/states.test.ts asserts PARTIAL -> StatusPanel
           (its own docstring) -> FE-s-30; fe-s-26/renders-differently.test.ts classifies Holdings
           panels -> FE-s-32. fe-s-3's `isCompleteState('PARTIAL') === false` STAYS (ruling H keeps that
           predicate for "shown complete"); fe-s-10's Holdings negative control is LOADING and stays a
           panel. No test asserts "Updated" or "account(s) in scope" literally.
grant      a grant is a <paths> entry, never prose (96381); a retraction is a <paths> removal before the
           cut. Every face names its surfaces by FILE where a directory would reach another cell's.
instrument `scripts/ui-smoke.mjs` is granted to NO round-5 cell (item 11 withdrawn). Browser criteria
           drive the page under NODE (chromium under bun fails on this box -- S42) and read their port
           through FE-s-27's declared-precondition helper; an absent server reports SKIPPED, never FAILED.
refusal    every face instructs its worker to REFUSE a criterion it cannot satisfy as written and report
           the refusal with its measurement. Round 4: every refusal was right (S55 counts five).
typecheck  EVERY portal order carries `bun run typecheck; echo rc=$?` -> rc=0.
channel    round-5 rows go to INVESTIGATION_v2.md; READ THE WHOLE PLANE (v1 AND v2) before minting; write
           with `newline='\n'` and READ THE DIFFSTAT of the commit (S36, S47).
gitlink    never stage `portal` in the workspace repo. PORTAL IS FROZEN: local DEV commits only.
```

## R5.3 THE CELLS

### `FE-s-29` -- the checker limbs, at the head (WORKSPACE cell)
Four limbs, one cell, because M(i) must change BOTH readers in one change and the other three live in the same two files. (i) The `<placeholders>` reader line-anchored in `to-pipeline-gate.py` and `proof-of-spec-check.py` together -- S53 measured the shipped reader false-admitting on two branches and the line-anchored one closing both with zero regressions. (ii) `proof-of-spec-check` refuses a count-bar PASS whose evidence carries a contradicting nonzero count for the bar's noun: REFUSE new instances, ANNOUNCE legacy (S56). (iii) Ruling Q with the CTO's condition: the discriminator reads the invoked TEST FILE (a seeded criterion and a browser criterion both invoke `bun test <file>`), and the `drives=` declaration is MANDATORY for new IRPT_FNTEND criteria. (iv) Card 6: gate (viii) also grades a MODIFICATION of an order that already declares `<placeholders>`; nothing is back-filled.

### `FE-s-30` -- one availability gate, on the report, and Reporting under it
The predicate lives in ONE new module over ONE object: the REPORT's availability, partitioned on the producer plane. The five answer-bearing states (READY, PARTIAL, STALE, NEEDS_CORRECTION, UNCERTAIN) render the body with state, reason and `business_date` visible and never styled complete; the four no-answer states render the panel; a body with no wire state renders the panel. `isCompleteState` stays the predicate for "shown complete" and stops being the predicate for "rendered at all". The body-mount claims are browser criteria of necessity (S42: no DOM environment here, so mounting and seeding are indistinguishable under `renderToStaticMarkup`).

### `FE-s-33` -- the fixture cell: maps that can actually show what is claimed
W1-S51: `fe-s-18-frozen.json` carries a status on 0 of its 9 envelopes (measured), so the frozen report's screen view is a StatusPanel. W1-S52: `gen-fixtures.ts:143` emits `parent_node_id: null` for every node, so the READY Holdings tree is parentless and its donut and table render empty. W1-S53: `fe-s-14-global.json` carries 2 keys and no holdings key (measured), so Global's Holdings reads Failed. ⛔ **The Holdings maps carry FE-s-26's hand-authored statuses that the generator does not emit** -- regenerating them from a fixed generator must not silently strip FE-s-26's repair.

### `FE-s-34` -- the relabel
`formatSourceAge` labels its figure "Updated N ago" (`state/status.ts:280-287`) while it now measures a business-date age. And 2 of its 3 call sites (`StageDisplay.tsx:51`, `VariantSelector.tsx:61`) still age `envelope.sourceAsOf`, the `as_of` instant, not the `business_date` the clause governs (measured; the CTO's census). One cell: both analysis panels render through `formatSourceAgeForState` and carry the corrected label.

### `FE-s-35` -- the wire boundary
Ruling P: a body carrying none of `contract_version` / `operation` / `firm_id` is REFUSED. Today `investor-reporting.ts:907` admits only envelope-shaped bodies and everything else takes `:936-943` -- counted, adapted, returned as a view (measured). The fix refuses there with `EnvelopeMismatch` naming `body`, rendered as a state through `envelopeFromRefusal`. Round-1 suites that serve bare bodies are re-based (measured: 2 of the 6 `LiveClient` suites carry no `contract_version`, `fe-s-1/adapter` and `fe-s-13/no-route`; `fe-s-19/network-state` builds v1 envelopes and is safe). W1-S20 rides here: `contracts/adapt.ts` types `report_title` as `string` while `tabs/analysis/composer.ts` sends `string | null` -- two builders of one body.

### `FE-s-36` -- the output-vocabulary limb at L6 (WORKSPACE cell)
S55's control (1), installed: at issuance, a criterion whose `<expect>` its named tool can never print is refused. Real positive control: F28-AC6 as issued (`0 fail` against a battery that prints only `BATTERY PASS` / `BATTERY FAILED`). Prospective -- it grades newly added orders only, so it cannot grade round 5 and runs in wave B, not at the head (confirmed 96408).

### `FE-s-31` -- the export under the gate, and the print scope line
The export gates on the BUNDLE today: the bundle's own envelope is the composer's hard-coded READY (`export/resolveBundle.ts:137`) while PrintEntry checks no report state (measured). Feasible without a producer change: the report view carries `availability` (`contracts/index.ts:222`) and `resolveBundle` fetches it through the typed client. Answer-bearing states export with state, reason and `business_date` on every page -- the chrome renders in exactly three places, `render/Page.tsx` plus the two documents that feed it (measured; the narrative page builds no Page of its own). No-answer states refuse to produce a document. Ruling J: `PerformanceDocument.tsx:45` prints `{accountIds.length} account(s) in scope`, an absent field printed as zero. W2-S12/W3-S5: `submitExport` is typed to the StatusEnvelope ack (`export/submit.ts:87`) instead of the ExportReceipt the producer answers.

### `FE-s-32` -- Holdings under the gate, with (a) as its check
Ruling I: none of W2-S21's (a)/(b)/(c) is the fix; the gate is. PARTIAL renders the holdings with the classification gap visible as unknown; UNCERTAIN renders the weights with the unnamed model revision stated; (a) is then the check, read from a REAL render. (b) is REJECTED (it ratifies a FWD-5 violation) -- the claims model is not edited. (c) holds for no-answer states only. W1-S35 rides here: the pie labels clip at `DrillTree.tsx:194` (`outerRadius={100}`), a prop the round-2 layout bound excluded. And the FE-s-18 bound-5 DISTINCTION verdict, still reading live digests, is frozen to one map here -- this is the next cell that changes those digests.

## R5.4 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-29 <- (none)              READY ROOT   workspace .tools/ (both checker files)
  FE-s-30 <- FE-s-29             wave B       the predicate + tabs/reporting/
  FE-s-33 <- FE-s-29             wave B       fixtures + the generator
  FE-s-34 <- FE-s-29             wave B       state/status.ts + two analysis panels
  FE-s-35 <- FE-s-29             wave B       the endpoint + round-1 suites
  FE-s-36 <- FE-s-29             wave B       workspace .tools/to-pipeline-gate.py (same file as FE-s-29)
  FE-s-31 <- FE-s-30             wave C       consumes the predicate
  FE-s-32 <- FE-s-30, FE-s-33    wave C       consumes the predicate and the parented tree

  weakly connected components: M = 1     ready roots at issuance: R = 1
  waves by depth: A={29}  B={30,33,34,35,36}  C={31,32}      max concurrent width: 5
  ~1 FE-s-30 then FE-s-31   ~2 FE-s-33 then FE-s-32   ~3 FE-s-34   ~4 FE-s-29 then FE-s-36   ~5 FE-s-35
```

Every wave-B edge on FE-s-29 is a SEQUENCING edge, not a data edge: ruling M requires the new checker in every later worktree. FE-s-36's edge is also a FILE edge (to-pipeline-gate.py). Wave-B pairs are disjoint by FILE: FE-s-30 writes a NEW module and never `state/status.ts` (FE-s-34's); FE-s-34 writes `StageDisplay.tsx` and `VariantSelector.tsx` and FE-s-35 writes `composer.ts` -- three files under `tabs/analysis/`, granted by file.

**Fan-out: `1 of 1 ready roots at issuance, widening to 5 of 5 at wave B and 2 of 2 at wave C, cap 8, reason: ruling M puts the checker limbs ahead of every other proof, and the wave-B surfaces are disjoint by file`.**

## R5.5 RULE 24 RECORD (round 5)

| postulate | how |
|---|---|
| (i) MECE | three domains by subtraction in R5.1: inputs 13-13=0 (item 11 WITHDRAWN with evidence, not dropped); outcomes 8-7=1 NOT MOVED AND NAMED (FWD-12); routed rows 0 uncovered. Cells partition by FILE; the two `.tools` cells share `to-pipeline-gate.py` and are SERIALIZED (FE-s-36 after FE-s-29), never concurrent. |
| (ii) same grain | (write region, ruling) per cell; FE-s-29 and FE-s-36 are at the FABRIC grain and stated as such. |
| (iii) intent | one axis for the product cells: a qualified answer is SHOWN, qualified, and never hidden or styled complete -- on screen and in the export alike. The fabric cells' axis is the record's integrity. The fixture cell's axis is the evidence's reach. |
| (iv) state | moves FWD-3/4/5/6/8/11 and FWD-1 toward EXERCISABLE. Does NOT move: any grade to REALIZED (the evidence stays fixture-bound; seven of eight outcomes cross IRPT_BCKEND for their EXERCISED proof); FWD-12; the producer's contract (ruling L is IRPT_BCKEND's); the claims model (ruling I rejects (b)); `isCompleteState` (kept for "shown complete"); the portal freeze. |

**The DOMAIN claims this record rests on were each measured at portal DEV c2eb8eb4, not inherited:** the gate's plane (producer, `contracts/index.ts:127`) against the view's `EXPLICIT_UNKNOWN_STATE` (`adapt.ts:103`); the chrome's three render sites; the 6 `LiveClient` suites; the 6 seeded suites; the 3 `formatSourceAge(` call sites.

## R5.6 BATTERY DISPOSITION (round 5)

| lens | disposition | denominator / reason |
|---|---|---|
| comp-schedule / comp-iam | DECLARED-NOT-APPLICABLE | no scheduled producer, no IAM-gated resource among these surfaces |
| comp-adversary | RUN at L4 on v0.6 (both halves SIGNED) | carried; PRD unchanged -- every ruling applies ratified text |
| the gate's plane | RUN | `HoldingsTab.tsx:90` READY-only; `ReportingTab.tsx:175` via `isCompleteState` (`status.ts:144`); PrintEntry: three phases, no report-state check; `EXPLICIT_UNKNOWN_STATE='UNCERTAIN'` at `adapt.ts:103` |
| export feasibility | RUN | report view carries `availability` (`contracts/index.ts:222`); `resolveBundle.ts:137` hard-codes the bundle's own READY; chrome at `Page.tsx` + two documents; narrative page builds no Page |
| overturned-behaviour tests | RUN, 19 files by census, then read | fe-s-5/states (granted to FE-s-30); fe-s-26/renders-differently (granted to FE-s-32); fe-s-3, fe-s-10, fe-s-19 safe as measured |
| the fixture gaps | RUN | frozen map 9 envelopes / 0 status; Global map 2 keys / 0 holdings; generator `parent_node_id: null` at `:143` |
| the wire | RUN | `investor-reporting.ts:907` / `:936-943`; 6 LiveClient suites, 2 bare; `pre-envelope.test.ts` prints `PRE-ENVELOPE BODIES REFUSED: 3 of 3` and `CONTROL: ... ACCEPTED` at DEV |
| item 11 | RUN -- WITHDRAWN | `ui-smoke.mjs:341` pickaxe -> `25062fce`; F22-AC6/AC7 both arms |
| instruments at the cut | RUN | proof-of-spec-check --self-test `RESULT: 18 of 18 arm(s) behaved`; to-pipeline-gate --self-test `RESULT: 0 arm(s) failed of 51`; alignment battery `BATTERY PASS`; placeholders battery green |

## R5.7 REFUSES TO ASSUME (round 5)

1. That a view state names a producer state. `UNCERTAIN` is both the producer's answer and the consumer's "no state at all" (ruling H, confirmed 96408).
2. That a carried row describes the code it names. C-S72 re-described W1-S36 a day after the line was fixed; the CTO put it into round 5 on that grounding (item 11, withdrawn).
3. That a ruling an issuer must remember is a control. Ruling Q's declaration is MANDATORY (96408).
4. That a generator and the maps it once emitted agree. FE-s-26 hand-repaired the Holdings maps the generator does not know about.
5. That the evidence a round certified still stands after the next repair. Two tests read the live artifact a later cell was ordered to overwrite, twice in round 4.
6. That a positive control proves a detector fires. It must be built from the real shape (S52); a control that passes on a commit after the retirement proves nothing (the WIRE_SCHEMA_PINS control, rerun at 774c595b).

## R5.8 HOLDS

**None blocking.** One owed act, recorded so it is not lost: when FE-s-29 lands card 6, CLAUDE.md Rule 27's "widening it is HIS call and is carded" and the gate's own docstring go stale, so a LAW EDIT is owed at FE-s-29's drain (1.0.0_SA_CTO 96394). FE-s-29 updates the gate's docstring inside its grant; the CLAUDE.md edit is this seat's at the drain, as a three-surface law edit.

---

# ROUND 6 -- v0.6 -- the recut on the CTO's ROUND-5 ANALYSIS

```json
{
 "round": 6,
 "decomp_version": "v0.6",
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@d1479bc5f0",
 "prd_version": "v0.6 -- UNCHANGED; the analysis owes no addendum (s.1), so no L4-R half re-opens",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND5_20260914.md@942e4ff992 (one citation corrected @727c4e7c2b); s.5 RULINGS S, U, V, T (renderer half), W",
 "slug_ref": "3.0.0_SA_CVO msg 96576, record org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND5_L8_L9_20260914.md@366a0b4103 -- 8 judgment criteria graded, 7 MET (6 qualified), F29-AC15 NOT MET on clause 3",
 "round5_cells": "FE-s-29..FE-s-36 ALL COMPLETE and drained (last: FE-s-31 @6462e98cc6, portal DEV 741bb54b)",
 "cells": 5,
 "cell_id_shape": "FE-s-<n> continuing from 37",
 "code_repo": "portal (gitlink in the workspace; branch DEV @741bb54b, measured)",
 "record_repo": "workspace (branch CLOUD)"
}
```

Round 5's finding, in the CTO's words: **the checker can be steered by the party it grades.** Limbs 2 and 3 of
proof-of-spec-check read their NEW/LEGACY boundary from the governing order, and the governing order came from
`decomp_ref.to_ref`, a field the worker writes; the flip gate passed the checker neither the flipped order nor a
criterion list (row S61, F29-AC15 NOT MET). Round 6 binds that first, then closes the environment, business-date,
window and fixture gaps the slug graduated. The header of this document reads v0.6 from this recut (analysis s.1:
it read v0.4 through round 5).

## R6.1 THE RECTANGLE -- five cells, the checker binding first

| cell | ruling | write surface (portal unless stated) | serves | rows | wave | slot |
|---|---|---|---|---|---|---|
| `FE-s-37` | S -- the governing order is the order being flipped | **workspace** `.tools/to-pipeline-gate.py`; `.tools/proof-of-spec-check.py`; `.tools/tests/` | the evidence plane | S61, C-S84 | A | ~4 |
| `FE-s-38` | U -- one server per worktree, every browser verdict names it | `vite.config.ts`; `tsconfig.app.json`; `tsconfig.node.json`; `.gitignore`; `__tests__/fe-s-27/`; `__tests__/fe-s-38/` | FWD-1, FWD-6 (evidence) | C-S81, W1-S56, W1-S57, W5-S1, W5-S4, F35-AC6's browser arm | B | ~1 |
| `FE-s-39` | V + W's W2-S29 -- the adapter never substitutes a value the document did not state | `contracts/adapt.ts`; `contracts/index.ts`; `state/status.ts` (wording); `tabs/holdings/`; `__tests__/fe-s-21/source-age.test.ts`; `__tests__/fe-s-39/` | FWD-5, FWD-6 | C-S83 (W3-S22, W3-S25, W3-S26), W2-S29 | B | ~3 |
| `FE-s-40` | T (renderer half) + W's W2-S31 -- the window by trading day, the band's code as the contract names it | `render/performance/MethodsAndSources.tsx`; `tabs/reporting/PeriodControls.tsx`; `tabs/reporting/AnswerStatus.tsx`; `render/Page.tsx`; `tabs/StatusPanel.tsx`; `state/tradingCalendar.ts` (NEW); `__tests__/fe-s-40/` | FWD-3, FWD-6, FWD-8, FWD-12 | S62, W2-S31 | B | ~2 |
| `FE-s-41` | W -- one writer per fixture map, the narrative bound to its own revision | `__tests__/fe-s-14/gen-maps.ts`; `__tests__/fe-s-33/gen-global-holdings.ts`; `__tests__/fe-s-18/gen-fixtures.ts`; `fixtures/smoke/fe-s-14-global.json`; `fixtures/smoke/fe-s-18-frozen.json`; the three `fixtures/smoke/fe-s-18-holdings-*.json`; `__tests__/fe-s-41/` | FWD-3, FWD-11 (evidence) | W2-S24, W2-S27 | B | ~5 |

**Coverage by subtraction, three domains.**
(1) The analysis's round-6 inputs, s.5, taken to their sub-items (denominator 17): S {binding}; U {helper refuses
a default, cacheDir in the worktree, tsbuildinfo in the worktree, every browser run records port and worktree,
F35-AC6's browser arm carried}; V {W3-S22, W3-S25, W3-S26}; T {trading-day comparator, the calendar named and 01-01
proved, an unnamed code verbatim and flagged}; W {W2-S24, W2-S27, W2-S31, W2-S29}; and the header bump. MINUS the
cells: S=37; U=38 (5 of 5); V=39 (W3-S25 is ALREADY MET at portal DEV 741bb54b, `state/availability.ts:108` keys on
producerState since FE-s-34 amendment 3 @c6ee044e, so FE-s-39 carries only its guarding test); T=40 (3 of 3);
W2-S24 and W2-S27=41; W2-S31=40 (the band is FE-s-40's file); W2-S29=39 (the mapping is in `contracts/adapt.ts`,
FE-s-39's file); the header bump = this L5 commit. **0 uncovered.**
(2) The PRD header's outcomes (denominator 8: FWD-1, 3, 4, 5, 6, 8, 11, 12) MINUS those round 6 moves: FWD-1 {38},
FWD-3 {40, 41}, FWD-5 {39}, FWD-6 {38, 39, 40}, FWD-8 {40}, FWD-11 {41}, FWD-12 {40 -- W2-S31, the band at 390} =
**1 NOT MOVED AND NAMED: FWD-4** (its cells landed in round 5; nothing this round's rulings name touches the
analysis tab's own surfaces).
(3) The rows the analysis routes to round 6 MINUS their carrying cell: S61 -> 37; C-S81 (with W1-S56, W1-S57,
W5-S1, W5-S4) -> 38; C-S83 (W3-S22, W3-S25, W3-S26) -> 39; S62 (renderer half) -> 40; C-S82's frontend rows W2-S24,
W2-S27 -> 41, W2-S31 -> 40, W2-S29 -> 39 = **0 uncovered.**

**NOT ROUND 6's (analysis s.5, s.6):** the five contract gaps -- window reason codes, report_title and the
analysis-POST schema (W5-S2), scope node_kind (W2-S25), Global's second firm (W2-S23), the ADVISORY enum -- carried by
row IRPT_BCKEND-S52 @d4fe023415; W4-S12 (AMGT_RESAPP's issuer); W4-S9 (fixed by 1.0.0_SA_CTO @727c4e7c2b).

## R6.2 BOUNDS -- ALL ROUND-6 CELLS (rounds 1-5 bounds stand)

```
checker    RULING S's SEQUENCING. FE-s-37 lands before any other round-6 proof is checked: every wave-B
first      worktree is cut AFTER FE-s-37 drains, so the checker a worker validates with is the bound one.
           Until it drains, 3.0.0_SA_CVO reads each instance's to_ref against its own order at L9 (the
           analysis's interim control), and no order the checker grades flips on the unbound checker.
census     THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD (W4-S11, adopted by 1.0.0_SA_CTO in the analysis
           s.3): every cell that changes behaviour runs the whole affected suite ONCE with its change applied
           (the InvestorReporting suite for portal cells; every .tools battery that calls either tool for
           FE-s-37), IRPT_FE_DEV_PORT exported to a measured-closed port. A failure OUTSIDE the grant is a
           BLOCKING row with the list, never an edit. A grep can seed a grant; it cannot close it.
servers    Until FE-s-38 drains, every browser criterion in a wave-B cell other than FE-s-38 runs vite on a
           worktree-local cache through a `.mjs` override LOADED at runtime inside the cell's own __tests__
           folder (rows W1-S59, W2-S28: a `.ts` under src/ breaks the portal typecheck), and exports
           IRPT_FE_DEV_PORT on EVERY bun test run -- never unset (W1-S57, W5-S1). Kill the server before the
           report.
drives     every criterion declares drives="network" or drives="none" (the checker refuses a new instance
           otherwise); a drives="network" PASS must not be satisfied by seeding initial* props.
anchors    count bars left `(?<![0-9])`, right `(?![0-9])`, never `\b`; one line per bar with `[^\n]*` where a
           bar spans words; output_evidence carries the deciding run only (the count-bar limb refuses a
           contradicting count).
rows       round-6 rows go to INVESTIGATION_v2.md; read the WHOLE plane (v1 and v2) before minting; an INERT
           row OMITS the disarm_owner key (a null is refused by the corpus pass); write with newline='\n'
           and read the diffstat.
gitlink    never stage `portal` in the workspace repo. PORTAL IS FROZEN: local DEV commits only.
```

## R6.3 THE CELLS

### `FE-s-37` -- the governing order is the order being flipped (WORKSPACE cell)
`check_complete_flip` (`.tools/to-pipeline-gate.py:2469` at CLOUD) runs `subprocess.run(["python", chk, inst])` --
the instance and nothing else. The checker resolves its governing order from `decomp_ref.to_ref` when present
(`.tools/proof-of-spec-check.py:614-641`, "An explicit decomp_ref.to_ref wins when present"; `_governing_rel`
`:1300`). RULING S: the gate hands the checker the flipped order's path, the checker takes THAT as the governing
order, and an instance whose `to_ref` names a different order is refused before any limb runs, by a violation naming
both paths; `to_ref` is a cross-check only. The battery doctors `to_ref` to a real round-4 order through the gate's
own flip path, keeps FE-s-29's committed instance VALID, and reads limb 1's frame on the doctored arm.

### `FE-s-38` -- one server per worktree
The fe-s-27 helper defaults to port `'5181'` (`__tests__/fe-s-27/_dev-server.ts:40`), and its own
`precondition.test.ts` pins that default (`:40`, `:216`, `:251`). vite sets no cacheDir (`vite.config.ts`), so its
cache is `node_modules/.vite` -- through the junction, the main checkout's; `.gitignore:17` already ignores `.vite`.
Both tsconfigs write `tsBuildInfoFile` to `./node_modules/.tmp/` (`tsconfig.app.json:3`, `tsconfig.node.json:3`),
through the same junction. RULING U: the helper refuses without IRPT_FE_DEV_PORT or a worktree-derived port;
cacheDir and tsbuildinfo live inside the worktree by CONFIG; every browser run's precondition line names its port
AND its worktree. F35-AC6's browser arm is carried here and re-run on this worktree's own server (its round-5
deciding run met no server and SKIPPED F19-AC4/AC5 by name).

### `FE-s-39` -- the adapter never substitutes a value the document did not state
One axis for three findings. W3-S26: `readingFromValue(null)` returns fact NULL (`contracts/adapt.ts:161`), and
`carryDocumentReading` (`:316`) applies it to VIEW documents, where the view contract defines a null
`businessAsOf` as "no clock" (`contracts/index.ts:147`), so 3 of 134 view documents (all in
`smoke/fe-s-3-loading.json`) read "Source date malformed" (`state/status.ts:332`, `:476`); on the WIRE plane a null
stays a producer defect. W3-S22: `__tests__/fe-s-21/source-age.test.ts` builds its envelope from the status's
`sourceAsOf` (`panelFor`, `:77-81`) and grades that instant under the business-date label (`:171`). W2-S29:
`ADVISORY_FOR_WIRE[...] ?? 'unknown'` (`contracts/adapt.ts:558`, `:865`) maps an out-of-enum `advisory_status`
(`'ADVISORY'`, emitted by `__tests__/fe-s-18/gen-fixtures.ts:317`) to "unknown" -- on the READY observed answer, 3
of 3 rows, with nothing qualifying it (F32-AC9's qualification). RULING W: shown verbatim and flagged. W3-S25 is
already met at DEV (above); this cell guards it with a test.

### `FE-s-40` -- the window by trading day, the band's code as the contract names it
`MethodsAndSources.tsx:58` decides "the same window" by calendar strings; `tabs/reporting/PeriodControls.tsx` prints
the same sentence on screen. So the frozen READY print (fe-s-31_print_frozen-as-committed_1440.png) says "a different
window" on page 3 -- a request starting 2026-01-01, a market holiday, answered from 2026-01-02 -- while its band says
REQUESTED_WINDOW_ANSWERED (row S62). The portal has no trading calendar (a census of `src/`: `ModelPortfolios.tsx`
keeps a render-axis holiday list that names `lib/trading_calendar.py` as the canonical one; `BenchmarkHeatmap.tsx`
counts weekdays). RULING T: compare by trading day, name the calendar, prove 01-01; the table is DERIVED from the
estate's one frontier, `lib/trading_calendar.py`, never hand-typed. REQUESTED_WINDOW_ANSWERED is defined nowhere
(0 hits in `docs/contracts/investor-reporting/v1`), so until the contract names its codes a code it does not name is
shown verbatim and flagged, on the band surfaces this cell owns (`AnswerStatus.tsx`, which Holdings also uses;
`render/Page.tsx`; `tabs/StatusPanel.tsx`; `MethodsAndSources.tsx`). W2-S31: the band fits its reason code at 390.

### `FE-s-41` -- one writer per fixture map
`fe-s-14-global.json` has two writers: `__tests__/fe-s-14/gen-maps.ts:94` rewrites it whole with no holdings, and
`__tests__/fe-s-33/gen-global-holdings.ts:57` adds them; run alone, the first strips the second's envelopes (W2-S24;
S59 disarmed it by detection only, which the CTO calls the defect). W2-S27: the frozen map's narrative names `perf-9`
while the frozen report is `rev-49f-000091`. RULING W: one writer; the narrative re-bound to its own performance
fixture. The three Holdings maps are generated from the frozen map (`gen-fixtures.ts`, W2-S26), so the narrative's
re-binding reaches them through the one generator.

## R6.4 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-37 <- (none)          READY ROOT   workspace .tools/
  FE-s-38 <- FE-s-37         wave B       portal root config + fe-s-27/
  FE-s-39 <- FE-s-37         wave B       contracts/adapt.ts, contracts/index.ts, tabs/holdings/, fe-s-21 test
  FE-s-40 <- FE-s-37         wave B       the band surfaces, the window comparator, the calendar
  FE-s-41 <- FE-s-37         wave B       the generators and the maps they write

  weakly connected components: M = 1     ready roots at issuance: R = 1
  waves: A={37}  B={38,39,40,41}      max concurrent width: 4
  ~4 FE-s-37   ~1 FE-s-38   ~3 FE-s-39   ~2 FE-s-40   ~5 FE-s-41
```

Every wave-B edge on FE-s-37 is a SEQUENCING edge (RULING S: nothing the checker grades flips on the unbound
checker). Wave B is disjoint by FILE: FE-s-39 holds `contracts/adapt.ts` (both its V half and the advisory mapping);
FE-s-40 holds every band surface, including `AnswerStatus.tsx`, which Holdings renders; FE-s-41 holds the generators
and the maps; FE-s-38 holds the portal root config and the fe-s-27 helper. Cells READ each other's surfaces at their
base (FE-s-39 and FE-s-40 read the Holdings maps FE-s-41 regenerates; the rows those two assert on do not move).

**Fan-out: `1 of 1 chains, cap 8, reason: RULING S puts the checker binding ahead of every other round-6 proof, so
the graph is one component with one ready root; it widens to 4 of 4 at wave B, disjoint by file`.**

## R6.5 RULE 24 RECORD (round 6)

| postulate | how |
|---|---|
| (i) MECE | three domains by subtraction in R6.1: inputs 17-17=0 (W3-S25 already met, guarded not rebuilt); outcomes 8-7=1 NOT MOVED AND NAMED (FWD-4); routed rows 0 uncovered. Cells partition by FILE; no two wave-B cells share a written path. |
| (ii) same grain | (write region, ruling) per cell; FE-s-37 at the FABRIC grain, stated as such. |
| (iii) intent | FE-s-37: the grader cannot be steered by the graded. FE-s-38: a verdict names the server it hit. FE-s-39: the adapter never substitutes a value the document did not state. FE-s-40: the page never contradicts itself about its window or presents an undefined code as a known one. FE-s-41: one writer per map. |
| (iv) state | moves FWD-1/3/5/6/8/11/12 toward EXERCISABLE. Does NOT move: any grade to REALIZED (fixture-bound evidence; seven outcomes need IRPT_BCKEND); FWD-4; FWD-11's second firm (W2-S23, the producer's); the contract's code list and enums (IRPT_BCKEND-S52); the portal freeze. |

## R6.6 BATTERY DISPOSITION (round 6)

| lens | disposition | denominator / reason |
|---|---|---|
| comp-schedule / comp-iam | DECLARED-NOT-APPLICABLE | no scheduled producer, no IAM-gated resource |
| comp-adversary | RUN at L4 on v0.6 (both halves SIGNED) | carried; PRD unchanged (analysis s.1) |
| the checker's governing order | RUN | `check_complete_flip` passes only the instance (`subprocess.run(["python", chk, inst])`); `to_ref` wins at `proof-of-spec-check.py:614-641`; 3 of 63 `.tools/tests` files reference `to_ref` (count-bar, alignment, seeded) |
| the dev-server environment | RUN | helper default `'5181'` (`:40`) pinned by its own test (`:40`, `:216`, `:251`); vite cacheDir absent; `.gitignore:17` `.vite`; tsBuildInfoFile `./node_modules/.tmp/` in both tsconfigs |
| the business-date plane | RUN | `availability.ts:108` keys on producerState at DEV (W3-S25 met); `readingFromValue(null)` NULL at `adapt.ts:161`; `fe-s-21` `panelFor` `:77-81`, `:171` |
| the advisory mapping | RUN | `adapt.ts:558`, `:865` `?? 'unknown'`; `'ADVISORY'` at `gen-fixtures.ts:317` |
| the window and the codes | RUN | `MethodsAndSources.tsx:58` calendar-string comparator; no trading calendar in `src/` (3 files mention holidays; none is the canonical one); reason codes render in `AnswerStatus.tsx`, `render/Page.tsx`, `tabs/StatusPanel.tsx`, `MethodsAndSources.tsx` |
| the fixture writers | RUN | `gen-maps.ts:94` and `gen-global-holdings.ts:57` both write `fe-s-14-global.json`; `perf-9` 1 and `rev-49f-000091` 1 in the frozen map |
| instruments at the cut | RUN | to-pipeline-gate --self-test 0 of 70 failed; proof-of-spec-check --self-test 32 of 32 (CLOUD 6462e98cc6) |

## R6.7 REFUSES TO ASSUME (round 6)

1. That a boundary the grader reads is the grader's. S61: the graded party wrote the field that decided ENFORCE or LEGACY, and every battery was green.
2. That a census by grep closes a grant. Three misses on one cell in round 5; the whole-suite run is the census of record.
3. That a verdict names the server it graded. W5-S1: another project's page answered on the default port and was graded.
4. That a null means the same thing on two planes. The view contract's null is "no clock"; the wire's is a producer defect.
5. That two calendar strings that differ are two windows. 2026-01-01 is not a trading day.
6. That detection is a disarm. S59 made the two-writer map loud; RULING W removes the second writer.

## R6.8 HOLDS

**None blocking.** Interim control while FE-s-37 runs, stated so nobody reads it as a gap: every round-6 wave-B cut
waits on FE-s-37's drain, and 3.0.0_SA_CVO reads each instance's to_ref against its own order at L9.

# ROUND 7 -- v0.7 -- the recut on the CTO's ROUND-6 ANALYSIS

```json
{
 "round": 7,
 "decomp_version": "v0.7",
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@d1479bc5f0",
 "prd_version": "v0.6 -- UNCHANGED; the analysis owes no addendum (s.1), so no L4-R half re-opens",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND6_20260914.md@4713211d87 (msg 96739); s.3 RULINGS X, Y, Z, AA, AB, AC and RULING U's residuals",
 "slug_ref": "3.0.0_SA_CVO msg 96737, record org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND6_L8_L9_20260914.md@3d8fda2d73, carriers C-S87..C-S92 @158e88fbac, remediation rows @74d8d21a09 -- 5 judgment criteria graded, 4 MET (3 qualified), F39-AC10 NOT MET",
 "round6_cells": "FE-s-37..FE-s-41 ALL COMPLETE and drained (last: FE-s-41 amendment 2 @999f08609b, portal DEV 35797660)",
 "cells": 4,
 "cell_id_shape": "FE-s-<n> continuing from 42",
 "code_repo": "portal (gitlink in the workspace; branch DEV @35797660, measured)",
 "record_repo": "workspace (branch CLOUD @edac45e48c, measured)"
}
```

Round 6's lesson, in the CTO's words: **the cut's reach is a subtraction, never a recall.** Twice running, tests and
fixtures carrying a ruling's removed behaviour sat outside the cut (W3-S27, W3-S28, W5-S5), and an issuer's re-run in
the worker's own worktree let a checkout-dependent red into DEV (S64). RULINGS X, Y and AC make those remedies bounds on
this cut (R7.2). The four cells close the ten rows the slug graduated: RULING W reaching every site it names, the
receiving route's binding, the red battery, and RULING U's residuals.

## R7.1 THE RECTANGLE -- four cells, one wave, disjoint by file

| cell | ruling | write surface | serves | rows | slot |
|---|---|---|---|---|---|
| `FE-s-42` | Z -- RULING W at every site it names | portal `contracts/adapt.ts` (`:585`); `contracts/index.ts` (`CohortValue`); `contracts/validate.ts`; `header/ScopeSummary.tsx`; `export/ReceiptPanel.tsx`; the capture writers `__tests__/fe-s-32/{holdings-in-a-browser.test.ts,holdings-driver.mjs}` and `__tests__/fe-s-40/{band-at-390.test.ts,band-driver.mjs}`; the census-named tests `__tests__/fe-s-1/fixtures.test.ts`, `__tests__/fe-s-9/receipt.test.ts`, `__tests__/fe-s-16/mounted-states.test.ts`; `__tests__/fe-s-42/` | FWD-5, FWD-6 | C-S92 (W3-S29 = F39-AC10, W3-S30, W2-S33, W3-S31) | ~3 |
| `FE-s-43` | AA -- the L7->L8 receiving route binds the order | workspace `.tools/receiving-check.py`; `.tools/tests/test_receiving_binding.py` (NEW) | the evidence plane | C-S90 (W4-S14) | ~4 |
| `FE-s-44` | AB -- the red battery diagnosed, not inherited | workspace `org/standards/test_artifact_coverage_both_grammars.py`; `.tools/proof-of-spec-check.py` ONLY if the checker is the wrong side | the evidence plane | C-S90 (W4-S15) | ~6 |
| `FE-s-45` | U's residuals + AC's instance | portal `package.json` (the `dev` line only); `__tests__/fe-s-19/mounted-from-wire.test.ts` (`:56`); the four overrides `__tests__/fe-s-{31,39,40}/vite.worktree.config.mjs` and `__tests__/fe-s-32/vite.worktree.config.ts` (retired); `__tests__/fe-s-41/one-writer.test.ts` (F41-AC5's read); `__tests__/fe-s-45/` | FWD-1, FWD-11 (evidence) | C-S91 (W1-S63, W1-S64, W1-S65), C-S90 (W5-S7) | ~1 |

**Coverage by subtraction, three domains.**
(1) The analysis's round-7 inputs, s.3 (denominator 7: X, Y, Z, AA, AB, AC, U's residuals) MINUS where each lands:
X, Y and AC are bounds on the cut and on the issuer (R7.2); Z = 42; AA = 43; AB = 44; U's residuals and AC's instance
W5-S7 = 45. **0 uncovered.**
(2) The rows the slug graduated (denominator 10: C-S90's W4-S14, W4-S15, W5-S7; C-S91's W1-S63, W1-S64, W1-S65;
C-S92's W3-S29, W3-S30, W2-S33, W3-S31) MINUS their carrying cell: W3-S29, W3-S30, W2-S33, W3-S31 -> 42; W4-S14 -> 43;
W4-S15 -> 44; W1-S63, W1-S64, W1-S65, W5-S7 -> 45. **0 uncovered.** The 11 dismissed rows (C-S88, C-S89) are closed and
not re-cut.
(3) The PRD header's outcomes (denominator 8: FWD-1, 3, 4, 5, 6, 8, 11, 12) MINUS those round 7 moves: FWD-5 and FWD-6
{42}; FWD-1 and FWD-11 {45, evidence}. **4 NOT MOVED AND NAMED: FWD-3, FWD-4, FWD-8, FWD-12.** Nothing in this round's
rulings touches their surfaces, and no FWD is uncovered (analysis s.1).

**RULING X's census, run at this cut over the corpus, not a folder** (portal DEV 35797660, workspace CLOUD edac45e48c):
- `CohortFact` values outside `__tests__/`: 2 consumers, `validate.ts:164-171` and `ScopeSummary.tsx:79`. Both are in
  42's surface.
- "cohort" under `__tests__/`: 2 files, a netlog and `fe-s-32/holdings-no-answer.json`. Neither asserts the directory
  advisory, so no existing test is turned red by 42's directory change.
- Tests importing `validate`: 1, `fe-s-1/fixtures.test.ts`.
- Tests rendering ReceiptPanel: 2, `fe-s-9/receipt.test.ts` and `fe-s-16/mounted-states.test.ts`.
- Tests naming a deliverables folder: 6. Minus the 2 writer pairs (fe-s-32, fe-s-40) = 4 readers, which are not
  granted.
- `cacheDir` under `__tests__/`: 6 files. Minus FE-s-38's 2 readers = **4 overrides, not the row's 2**.
- `receiving-check` across `.tools/`, `.claude/` and 3.0.0_SA_CVO's folder: the tool, one mention in
  `prd-manifest-gate.py`, the canonical-flow skill's documented call, and historical records. **0 batteries.**
- The battery: a script, invoked `python <file>`. Under pytest it collects zero.

Every census-named test is granted BY NAME for the ruling's claims only. The whole-suite run stays each cell's census of
record, because a read census seeds a grant and the run closes it.

## R7.2 BOUNDS -- ALL ROUND-7 CELLS (rounds 1-6 bounds stand)

```
X  reach     the cut's reach is a subtraction over the corpus (R7.1's census); every test, fixture and map a
             ruling's change turns red is granted BY NAME; the domain is the corpus, never a folder.
Y  re-run    the issuer never re-runs a worker's bars in the worker's worktree: a branch synced with DEV or an
             untouched pair (workspace + nested portal, so cross-repo paths resolve), with `git ls-files --eol`
             printed beside any byte-compare.
AC reads     a criterion that reads a file reads `git cat-file blob HEAD:<path>` (or the committed tree), or its
             bound says why it reads the working copy (42's AC7/AC8 and 45's AC2 do, by design).
census       the whole-suite run is the census of record for every behaviour-changing cell (the InvestorReporting
             suite for 42 and 45; FE-s-37's .tools census battery for 43 and 44).
servers      FE-s-38 has drained: vite caches inside the worktree by config; `bun run dev --port <p> --strictPort`
             directly; IRPT_FE_DEV_PORT on EVERY bun test run; 42 on 5263, 45 on 5261.
drives       every criterion declares drives="network" or drives="none".
anchors      count bars left `(?<![0-9])`, right `(?![0-9])`, never `\b`.
rows         round-7 rows go to INVESTIGATION_v2.md; read the WHOLE plane (v1 and v2) before minting; an INERT row
             OMITS disarm_owner. Row starts at the cut: W3-S33, W4-S16, W6-S1, W1-S67.
gitlink      never stage `portal` in the workspace repo. PORTAL IS FROZEN: local DEV commits only.
```

## R7.3 THE CELLS

### `FE-s-42` -- RULING W at every site it names (RULING Z)
The directory cohort renames an out-of-enum advisory onto 'unknown' (`adapt.ts:585`), and the Holdings path does not
(`:464-466`). `CohortValue` is shared by three axes, and its two consumers are validate and ScopeSummary. validate pins
three values (`:448`). ReceiptPanel prints an unnamed code bare (`:47`), beside FE-s-40's one rule in `render/Page.tsx`
(`:95`), which is imported and never copied. Two browser tests write committed captures on every run. The bar:
verbatim and flagged at every use site, F39-AC10's clause re-graded at the directory site, and captures outside every
committed deliverables folder by default.

### `FE-s-43` -- the receiving route binds the governing order (RULING AA)
`receiving-check.py:71` builds `[instance]`. The checker already takes `--governing-order` (FE-s-37). The route
passes the order the receiving seat is handed; an unbound instance reads NOT-BOUND, never ACCEPT; the other five routes
keep their current behaviour. The canonical-flow skill documents the call; the change it needs is named for its owner,
not edited.

### `FE-s-44` -- the red battery, diagnosed (RULING AB)
3/6 at the cut: A, B and E are refused where rc=0 is owed, and C, D and F "pass" only as blanket refusals. The worker
diagnoses which limb refuses and which side is wrong before fixing, keeps every correct limb, and proves with a mutant
that the controls can fail again.

### `FE-s-45` -- RULING U's residuals and AC's instance
The dev script loads the config without writing through the junction (W1-S63); fe-s-19's comment follows the helper
(W1-S64); four overrides are retired (W1-S65, a census of 4); F41-AC5 reads the committed blob (W5-S7).

## R7.4 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-42 <- (none)   READY ROOT   portal: contracts, header, ReceiptPanel, the two capture writers
  FE-s-43 <- (none)   READY ROOT   workspace: .tools/receiving-check.py + its new battery
  FE-s-44 <- (none)   READY ROOT   workspace: the org/standards battery (+ the checker only if wrong)
  FE-s-45 <- (none)   READY ROOT   portal: package.json dev line, fe-s-19 comment, four overrides, fe-s-41 AC5

  weakly connected components: M = 4     ready roots at issuance: R = 4
  waves: A={42,43,44,45}      max concurrent width: 4
  ~3 FE-s-42   ~4 FE-s-43   ~6 FE-s-44   ~1 FE-s-45
```

The cells are disjoint by FILE. 42 and 45 share folders, but no file: 42 writes fe-s-32's and fe-s-40's tests and
drivers, and 45 deletes their `vite.worktree.config` files. 43 and 44 share `.tools/`, but no file: 43 writes
`receiving-check.py` and a new battery; 44 writes the org/standards battery and, only if it is the wrong side, the
checker. 43 CALLS the checker and never edits it. So if 44 changes the checker, 43's branch is synced with CLOUD before
43 drains.

**Fan-out: `4 of 4 chains, cap 8, reason: the round-6 analysis's four cells have no dependency edge between them and
no shared file, so each is its own chain and its own ready root`.**

## R7.5 RULE 24 RECORD (round 7)

| postulate | how |
|---|---|
| (i) MECE | three domains by subtraction in R7.1: inputs 7-7=0; graduated rows 10-10=0; outcomes 8-4=4 NOT MOVED AND NAMED. RULING X's census is itself a subtraction over the corpus, with denominators printed (R7.1). Cells partition by FILE. |
| (ii) same grain | (write region, ruling) per cell; 43 and 44 are at the FABRIC grain, stated as such. |
| (iii) intent | 42: the adapter and every surface state what the document states, and no test rewrites committed evidence. 43: the receiver grades against the order it was handed. 44: a battery that cannot fail is repaired so it can. 45: one server per worktree leaves nothing behind, and a committed read reads what is committed. |
| (iv) state | moves FWD-5, FWD-6, and FWD-1/FWD-11 (evidence) toward EXERCISABLE, and the evidence plane. Does NOT move: any grade to REALIZED (fixture-bound evidence; the EXERCISED proofs need IRPT_BCKEND, last in SEQUENCE.yaml); FWD-3, 4, 8 and 12; FWD-11's second firm (W2-S23); the contract's reason-code list (W2-S32, IRPT_BCKEND's); 3.0.0_SA_CVO's own intake scripts (that seat binds its own); the portal freeze. |

## R7.6 BATTERY DISPOSITION (round 7)

| lens | disposition | denominator / reason |
|---|---|---|
| comp-schedule / comp-iam | DECLARED-NOT-APPLICABLE | no scheduled producer, no IAM-gated resource |
| comp-adversary | RUN at L4 on v0.6 (both halves SIGNED) | carried; PRD unchanged (analysis s.1) |
| the advisory sites | RUN | `adapt.ts:585`, `:464-466`; `CohortValue` at `index.ts:310`; `validate.ts:448`, `:164-171`; `ScopeSummary.tsx:79`; `ReceiptPanel.tsx:47`; `render/Page.tsx:95` |
| RULING X's census | RUN | R7.1: the cohort consumers 2; "cohort" in tests 2; validate importers 1; ReceiptPanel renderers 2; deliverables-naming tests 6 (2 writer pairs); cacheDir files 6 (4 overrides) |
| the receiving route | RUN | `receiving-check.py:71` `[instance]`; `--governing-order` in the checker since 13a3e28b95; 0 batteries call receiving-check |
| the battery | RUN | 3/6 rc=1 at 8f4106a7f2; a script (`sys.exit` at `:128`) |
| the dev script and the drain | RUN | `package.json:13` `"dev": "vite"`; the main portal checkout's uncommitted overrides-block edit (+2/-1, another seat's) |
| instruments at the cut | RUN | to-pipeline-gate --self-test 0 of 72 failed; proof-of-spec-check --self-test 42 of 42 (CLOUD edac45e48c) |

## R7.7 REFUSES TO ASSUME (round 7)

1. That a folder is the corpus. W4-S15 sat red in `org/standards/`, where no folder-scoped census of the checker's batteries looked.
2. That a row's own count is the population. W1-S65 named two overrides and there are four, and W3-S31 named one capture writer and there are two.
3. That a re-run in the worker's tree corroborates the worker. S64 was green there, and red on every fresh checkout.
4. That a battery whose controls pass is discriminating. W4-S15's controls pass because everything is refused.
5. That the working copy is the committed state. W5-S7 and S64 read the working copy; the bars now read the blob.
6. That a drain touching a file another seat has modified will merge. git refuses, cleanly, and the owner is a seat, not a tool.

## R7.8 HOLDS

- **FE-s-45's PORTAL DRAIN** waits on the main portal checkout's uncommitted `package.json` edit, which is another
  seat's. git refuses a merge that touches a locally modified file. If the edit still stands when FE-s-45 is ready, the
  drain is surfaced to 0.0.0_AB_MSTR to find the edit's owner; this seat never touches it. Everything else in round 7
  drains without it.
- **The seat question is at Andrew, not ruled** (analysis s.5). The CTO's rec is to free this seat after round 7
  drains. Until he answers, round 7 proceeds.

# ROUND 8 -- v0.8 -- the recut on the CTO's ROUND-7 ANALYSIS

```json
{
 "round": 8,
 "decomp_version": "v0.8",
 "prd_ref": "org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md@d1479bc5f0",
 "prd_version": "v0.6 -- UNCHANGED; the analysis owes no addendum, so no L4-R half re-opens",
 "analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_IRPT_FNTEND_ROUND7_20260915.md (msg 96865; the CTO commits it when the shared index frees and said 'do not wait for the hash')",
 "slug_ref": "3.0.0_SA_CVO msg 96838, record org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND7_L8_L9_20260915.md@ac41c29ce1, carriers C-S93..C-S98 @aba71991f0, REMEDIATION_v3.md @2d42ebd1b0 -- 4 judgment criteria graded PASS (3 qualified), 5 rows graduated",
 "round7_cells": "FE-s-42..FE-s-45 ALL COMPLETE and drained (last: FE-s-45 @32855486f0, portal DEV 1f3ce9f0)",
 "cells": 3,
 "cell_id_shape": "FE-s-<n> continuing from 46",
 "code_repo": "portal (gitlink in the workspace; branch DEV @1f3ce9f0, measured)",
 "record_repo": "workspace (branch CLOUD, measured at this commit)",
 "seat": "Andrew-direct ~03:2xZ 'both recs approved' (@9e0ee4b49c): 2.0.0_SA_COO~F holds IRPT_FNTEND through round 8, then the seat frees"
}
```

Round 7's lesson, from the CTO's own W1-S69: **a bar that names a reading must name one that DIFFERS in the world it
rules out.** Round 8 closes the slug's three cuttable items as three small cells: timeouts sized to measured cost, the
adapter's reason on the no-status path, and "withheld" for a cohort the producer does not assert. The CTO fixed W6-S1
and W4-S16 in its own surfaces, landing with its analysis commit, so no cell is cut for them.

## R8.1 THE RECTANGLE -- three cells, one wave, disjoint by file

| cell | ruling | write surface | serves | rows | slot |
|---|---|---|---|---|---|
| `FE-s-46` | W3-S33 -- per-test timeouts sized to measured cost | portal `__tests__/fe-s-40/window.test.ts` and `__tests__/fe-s-41/one-writer.test.ts` (timeout arguments ONLY); `__tests__/fe-s-46/` | FWD-1, FWD-11 (evidence) | C-S96 (W3-S33) | ~1 |
| `FE-s-47` | W3-S35 -- the ADAPTER supplies the reason; validate unchanged | portal `contracts/adapt.ts` (the explicit-unknown sites + one constant); `__tests__/fe-s-47/` | FWD-5, FWD-6 | C-S97 (W3-S35) | ~3 |
| `FE-s-48` | F42-AC10's qualification -- a non-authoritative cohort reads "withheld" | portal `header/ScopeSummary.tsx` (the withheld word and its comment); `__tests__/fe-s-48/` | FWD-5, FWD-6 | C-S93 (F42-AC10 qualified) | ~4 |

**Coverage by subtraction, three domains.**
(1) The analysis's items (denominator 7: W1-S69, W1-S70, W6-S1, W4-S16, W3-S35, F42-AC10, W3-S33) MINUS where each lands:
W1-S69 is a bound on every criterion cut from now on (R8.2 "runtime"); W1-S70 is taken with no cell, because RULING (B)
stands on its other two reasons; W6-S1 and W4-S16 are fixed by 1.0.0_SA_CTO in its own surfaces; W3-S35 = 47;
F42-AC10 = 48; W3-S33 = 46. **0 uncovered.**
(2) REMEDIATION_v3's OPEN rows (denominator 5: W1-S69, W3-S33, W6-S1, W3-S35, W4-S16) MINUS their disposition: W3-S33 -> 46;
W3-S35 -> 47; W1-S69 -> bound R8.2; W6-S1 and W4-S16 -> 1.0.0_SA_CTO's own fixes. **0 uncovered.** The 5 dismissed rows
(C-S94, C-S95) are closed and not re-cut.
(3) The PRD header's outcomes (denominator 8: FWD-1, 3, 4, 5, 6, 8, 11, 12) MINUS those round 8 moves: FWD-5 and FWD-6
{47, 48}; FWD-1 and FWD-11 {46, evidence}. **4 NOT MOVED AND NAMED: FWD-3, FWD-4, FWD-8, FWD-12.** No FWD is uncovered.

**RULING X's census, run at this cut BY WHOLE-SUITE PROBE, not by grep.** It used a detached probe pair: workspace at
CLOUD HEAD and portal at DEV 1f3ce9f0, with its own junction. Each ruling's minimal change was applied alone, the
InvestorReporting suite was run on a measured-closed port, and the change was reverted:
- **Run A, "withheld" at `ScopeSummary.tsx:118`: 559 pass, 18 skip, 1 fail of 578.**
- **Run B, the carry supplying a reason when no status or no stated state arrived (`adapt.ts:292`): 559 pass, 18 skip,
  1 fail of 578.**
- **The 1 fail is the SAME test both times, and it is caused by neither change.** It is F41-AC5's control
  (`fe-s-41/one-writer.test.ts:791`, added by FE-s-45 in round 7), timing out at 5859 ms and 5812 ms under load.
  - That makes it a THIRD member of W3-S33's class, which the row did not name, and it goes into FE-s-46 by name.
  - So 47's and 48's changes each turn **0** existing tests red, and neither needs a census-named test grant.
- A read census of `partialReason`, `: unknown` and `not asserted` under `__tests__/` finds 84 hits in 44 files. The run,
  not the read, closes the grant; the read is too wide to grant from.
- `EXPLICIT_UNKNOWN_STATE` into an Availability: `adapt.ts:228` (`wireEnvelope`) and `:290` (`carryAvailabilityFromStatus`,
  whose `:292` carries the DOCUMENT's partialReason). `envelope.ts:233` is `IrParsedEnvelope.state`, which is not an
  Availability.
- Status-optional operations: 11 of 12 (`contracts/wire/responses.ts:236-249`). `envelope.ts:231` says ten, which is stale by
  one and named in 47, not edited.
- `partialReason` renderers: `render/Page.tsx:160`, `tabs/reporting/AnswerStatus.tsx:56`,
  `render/performance/MethodsAndSources.tsx:173` and `:242`. The reason reaches the screen with no UI grant.
- `CohortFact` render sites: `ScopeSummary.tsx` only; `validate.ts:164-171` checks and does not render (round 7's census).

The whole-suite run stays each cell's census of record, because a probe seeds a grant and the worker's run closes it.

## R8.2 BOUNDS -- ALL ROUND-8 CELLS (rounds 1-7 bounds stand)

```
X  reach     the cut's reach is a subtraction over the corpus; R8.1's whole-suite probe is this cut's census; every
             test a ruling's change turns red is granted BY NAME (0 this round).
Y  re-run    the issuer never re-runs a worker's bars in the worker's worktree: an untouched detached pair (workspace
             + nested portal + junction), with `git ls-files --eol` printed beside any byte-compare.
AC reads     a criterion that reads a file reads the committed blob or tree, or its bound says why it reads the
             working copy (46's load runs do, by design).
runtime      (W1-S69) a criterion that names a runtime names a reading that DIFFERS under the other runtime: the
             listener's image name, and process.versions.bun absent. Never process.release.name alone. No round-8
             criterion names a runtime.
census       the whole-suite run is the census of record for every cell; F41-AC5's control timing out under load is
             46's row, so 47 and 48 report it and re-run, never edit it.
servers      no dev server this round; IRPT_FE_DEV_PORT on EVERY bun test run to a measured-closed port: 46 on 5261,
             47 on 5263, 48 on 5265.
timeouts     per-test only; no bunfig.toml or global timeout, because a global value would hide every other slow test.
drives       every criterion declares drives="network" or drives="none" (all "none" this round).
anchors      count bars left `(?<![0-9])`, right `(?![0-9])`, never `\b`.
rows         round-8 rows go to INVESTIGATION_v2.md; read the WHOLE plane (v1 and v2) before minting; an INERT row
             OMITS disarm_owner. Row starts at the cut: W1-S71, W3-S36, W4-S18.
gitlink      never stage `portal` in the workspace repo. PORTAL IS FROZEN: local DEV commits only.
```

## R8.3 THE CELLS

### `FE-s-46` -- timeouts sized to measured cost (W3-S33)
Three tests pass on their content, but their loaded cost (5172 to 5875 ms) is past bun's 5000 ms default while their
unloaded cost is under it. So a later cell's census reads red for a reason that cell cannot fix. Each test in the two
files that can reach the default gets its own third `test()` argument, at least 3 times its highest recorded cost and
at most 60000 ms. A seeded 1 ms timeout shows bun honours the argument.

### `FE-s-47` -- a response with no status says why its state is unknown (W3-S35; the CTO's RULING)
With no status, `carryAvailabilityFromStatus` leaves the document UNCERTAIN with no reason. validate refuses that, and
the screen shows UNCERTAIN with nothing to explain it. The adapter supplies ONE named reason on that path only. A
stated state never carries it (the `:292` hazard), and validate is unchanged. The class runs over every status-optional
operation that carries an availability, not the one instance.

### `FE-s-48` -- a non-authoritative cohort reads "withheld" (F42-AC10's qualification; the CTO's RULING)
`ScopeSummary.tsx:118` renders every withheld axis as `<axis>: unknown`. It becomes `<axis>: withheld`, and the comment
follows. The assertable path, including a producer's own UNKNOWN token, is unchanged. Text only, so no contrast
surface moves.

## R8.4 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-46 <- (none)   READY ROOT   portal: fe-s-40/window.test.ts + fe-s-41/one-writer.test.ts (timeouts only)
  FE-s-47 <- (none)   READY ROOT   portal: contracts/adapt.ts (explicit-unknown sites + one constant)
  FE-s-48 <- (none)   READY ROOT   portal: header/ScopeSummary.tsx (the withheld word + comment)

  weakly connected components: M = 3     ready roots at issuance: R = 3
  waves: A={46,47,48}      max concurrent width: 3
  ~1 FE-s-46   ~3 FE-s-47   ~4 FE-s-48
```

The cells are disjoint by FILE: no two cells write the same file, and each new test folder is its cell's own. 47's
tests read `ScopeSummary`'s neighbours only through the adapter, and 48's tests read no adapter file 47 writes. The
three drain in any order.

**Fan-out: `3 of 3 chains, cap 8, reason: the round-7 analysis's three cells have no dependency edge between them and
no shared file, so each is its own chain and its own ready root`.**

## R8.5 RULE 24 RECORD (round 8)

| postulate | how |
|---|---|
| (i) MECE | three domains by subtraction in R8.1: analysis items 7-7=0; open remediation rows 5-5=0; outcomes 8-4=4 NOT MOVED AND NAMED. RULING X's census is a whole-suite probe per ruling, with its denominators printed (578 tests, 102 files). Cells partition by FILE. |
| (ii) same grain | (write region, ruling) per cell; all three are portal cells at the file grain. |
| (iii) intent | 46: a test's pass depends on its content, never on the box's load. 47: a state the wire did not send carries the reason it is unknown. 48: a value the panel declines to assert says so. |
| (iv) state | moves FWD-5 and FWD-6 toward EXERCISABLE, and the evidence plane. Does NOT move: any grade to REALIZED (fixture-bound evidence; the EXERCISED proofs need IRPT_BCKEND, last in SEQUENCE.yaml); FWD-3, 4, 8 and 12; the `.tools` census bound (W6-S1, the CTO's); the canonical-flow skill (W4-S16, the CTO's); 3.0.0_SA_CVO's backfill question (at Andrew); the portal freeze. |

## R8.6 BATTERY DISPOSITION (round 8)

| lens | disposition | denominator / reason |
|---|---|---|
| comp-schedule / comp-iam | DECLARED-NOT-APPLICABLE | no scheduled producer, no IAM-gated resource |
| comp-adversary | RUN at L4 on v0.6 (both halves SIGNED) | carried; PRD unchanged (no addendum) |
| the slow tests | RUN | `window.test.ts:253`, `one-writer.test.ts:424` and `:791`, no timeout argument; unloaded file totals 2.20 s and 7.19 s (3 of 3 runs green); loaded 5172, 5735, 5875, 5859 and 5812 ms |
| the no-status path | RUN | `validate.ts:95-96`; `adapt.ts:167`, `:228`, `:290`, `:292`; `envelope.ts:219`, `:233`; `responses.ts:236-249` (11 of 12 optional); the reason renderers (4 sites) |
| the withheld site | RUN | `ScopeSummary.tsx:67-68`, `:117-119`, `:9-12`; `fixtures/directory.unknown-cohort.json` |
| RULING X's census | RUN | two whole-suite probe runs, 559/18/1 of 578 each, the 1 fail the same unrelated timeout |

## R8.7 REFUSES TO ASSUME (round 8)

1. That a row's own list is the population. W3-S33 named two slow tests; the probe found a third, in the same file.
2. That a grep of a word sizes a grant. 84 hits in 44 files; the whole-suite probe says 0 tests turn red.
3. That a fix to one site is safe at the seam. `:292` carries the document's reason forward, so a reason placed in
   `wireEnvelope` would ride onto a stated state; 47's control arm reads it.
4. That a named reading discriminates. W1-S69: `process.release.name` reads "node" under bun too.
5. That a comment's count is the count. `envelope.ts:231` says ten status-optional operations; the table holds 11.

## R8.8 HOLDS

- **The seat.** Andrew-direct ~03:2xZ, "both recs approved" (@9e0ee4b49c): this seat holds IRPT_FNTEND through round 8,
  then frees. His ~18:2xZ word, relayed, gives the next freed seat to LGIC_CANON.
- **PORTAL FROZEN:** local DEV commits only. No CLOUD push and no SITEZ merge until Andrew's word (0.0.0_AB_MSTR's).

## R8.9 THE ADDED CELL -- round 8's one added order (1.0.0_SA_CTO rulings, msgs 96904, 96915 and 96924)

| cell | ruling | write surface | serves | rows | slot |
|---|---|---|---|---|---|
| `FE-s-49` | the Opal-admin gate: role admin AND firmId opal-capital (Andrew's prod-deploy condition 2) | portal `src/App.tsx` (the two `/investor-reporting` route lines and the nav item line, made byte-identical to 2.0.0_SA_COO~D's rendering); `src/lib/firmAccess.ts` (`'/investor-reporting'` out of 3 partner sets, only if the suite stays green); `__tests__/fe-s-49/` | FWD-1, FWD-12 (PRD F1: route, page identity, navigation entry) | S66 | ~2 |

**Why mid-round.**
- Andrew-direct ~04:4xZ, relayed by 0.0.0_AB_MSTR (msg 96903): *"Investor Reporting must remain Opal Admin gated, no
  clients are allowed to see that."* This is a condition of his full /prod-deploy.
- To 2.0.0_SA_COO~D (msg 96914): *"that page needs to be listed for Opal Admins only in the tsx for that page."*
- 1.0.0_SA_CTO ruled it into round 8 as its ONE added order (96904), with the stricter predicate (96915).
- It then ruled this seat's recommendation (96924): copy 2.0.0_SA_COO~D's rendering byte-for-byte, so identical edits on
  both branches merge clean, and take the partner allowlist entries out.
- Andrew confirmed: "we need those admin guards" (96906).

**The issuer's census at portal DEV 1f3ce9f0** (`git show` at the ref):
- `App.tsx:421` and `:573` wrap the page in `<ProtectedRoute>` with no `requireAdmin` or `requireInternal`, and the nav item at
  `:94` carries no `requiresAdmin` or `requiresTier`.
- `ProtectedRoute.tsx`:
  - `:39-40` `requireAdmin` tests role only;
  - `:44-45` `requireInternal` tests `firmId === 'opal-capital'`;
  - `:57` applies the firm allowlist.
- `firmAccess.ts` `FIRM_ALLOWED_PATHS` lists `/investor-reporting` for **three partner firms**: 49financial, inflection and
  cottonwood.
- `hasAccess('internal')` = `firmId === 'opal-capital'` (`AuthContext.tsx:758-760`).
- `origin/PROD` has 0 investor-reporting route lines, against 3 at DEV.
- 2.0.0_SA_COO~D's feature working copy carries the exact three target lines, quoted in FE-s-49's cell. Its commit hash
  follows, and the issuer byte-compares the drain against it.
- The whole-suite probe of the admin-only change: 559/18/1 of 578, and the 1 fail is the same unrelated load timeout
  (FE-s-46's). Every browser driver signs in as role admin with firmId opal-capital. So 0 tests turn red; the allowlist
  change is decided by the worker's own whole-suite run, as the CTO ruled.

**Coverage by subtraction, the added input:**
- the CTO's cell 4 (denominator 1) -> 49;
- row S66 -> 49;
- **0 uncovered.**

**Disjoint by FILE:** `App.tsx` and `firmAccess.ts` are none of 46's, 47's or 48's.

**Fan-out now:** `4 of 4 chains, cap 8, reason: the added cell has no dependency edge with 46, 47 or 48 and no shared file,
so it is its own chain and ready root`. Max width 4.

**Rule 24 (iv):**
- Moves: the page's access plane toward EXERCISABLE.
- Does NOT move: the backend's own admin gating (read-only census in F49-AC9); the d13 branch (2.0.0_SA_COO~D's own
  commit, identical lines); every other `FIRM_ALLOWED_PATHS` entry; the portal freeze.

## R9 -- ROUND 9: THE CTO'S NAMED SEVEN + THE PRD'S NEW CROSS-CUTTING OBLIGATION

**Two inputs, folded into ONE issuance (COO's own choice, spine v3.0 L10: re-decomposition, not a bare re-issue,
because the PRD moved past what round 8's analysis answered).**

1. `ROUND_ANALYSIS_IRPT_FNTEND_ROUND8_20260915.md` (`1.0.0_SA_CTO`, @unrecorded commit, read at HEAD 2026-09-21),
   section "Round 9 -- ONE issuance of seven small cells" (cells A-G below).
2. PRD addenda v0.7 (`unprojected_grant`, envelope-level field), v0.8 (the two-shape branch: response-envelope
   PRESENT-AT-ZERO vs. refusal ABSENT-BY-DESIGN) and v0.9 (the `irpt-holdings` fork carve-out, owner
   `1.0.0_SA_CTO`, un-park condition `IRPT_BCKEND.TO-IB-rtf-8`) -- landed since round 8's analysis and never
   folded into a decomposition. Reaches PRD cells F2, F4, F5, F6, F7, F8, F10, F11, F12 (PRD `CONTRACTS` section,
   the `unprojected_grant` paragraph).

### R9.1 THE RECTANGLE -- eleven new cells

**MECE by subtraction:** round 8 answered 7 named items (A-G) + the CTO's own round-8 lint addendum already
folded into round 8's cell C's scope; the PRD's `unprojected_grant` paragraph names 9 PRD cells it reaches
(F2,F4,F5,F6,F7,F8,F10,F11,F12) minus F9 (the RenderPackage itself is not named) and minus F12 read as the
PARSING layer (its own cell, not a "reach" target) = 8 reachable VIEW surfaces. Of those 8, F4/F5/F6/F7/F8
already share ONE render surface (`tabs/StatusPanel.tsx`, confirmed by source read: it is imported by
`ReportingTab.tsx`, `AnalysisTab.tsx`, `HoldingsTab.tsx`, `ExportModal.tsx`, `ReceiptPanel.tsx`, `TabShell.tsx`,
`index.tsx` and `render/Page.tsx` -- 8 of 8 grep hits, portal DEV be8cf21874), so ONE cell wired there closes
five PRD cells at once; F11 (Global) reuses the SAME tab bodies per its own PRD row ("uses all three tabs and
export"), so it is CLOSED BY VERIFICATION under that cell, not a separate cut (checked, not assumed --
FE-s-58's own acceptance exercises Global mode). F2 (`header/ScopeSummary.tsx`) and F10
(`render/narrative/PeriodInContextPage.tsx`) each read their contract's `.availability` directly, outside
`TabEnvelope`, so each needs its own cell. **8 reachable surfaces - 5 (closed by the shared cell) - 1 (F11,
closed by verification, not a cut) = 2 cells (F2, F10) plus the shared cell plus the parsing root = 4 cells
for the whole obligation.**

| cell | write surface | serves | source of the fix | wave | slot |
|---|---|---|---|---|---|
| `FE-s-50` | `portal/src/pages/InvestorReporting/__tests__/fe-s-1/gen-wire.test.ts` (new); `contracts/gen-wire.ts` if it exists as a script, else the generator it names | FWD-1, FWD-11 (evidence) | round-8 analysis item 6 (S68): `gen-wire.ts` CRLF-normalizes before hashing | A | ~1 |
| `FE-s-51` | a verification-only test under `__tests__/` naming the ancestry check | FWD-12 (evidence) | round-8 analysis item 9 (F49-AC8): the carried-hunks arm keyed to `c29a8b86` ancestry | A | ~2 |
| `FE-s-52` | `__tests__/fe-s-5/alias-probe.test.ts`; `__tests__/fe-s-19/pre-envelope.test.ts`; `export/ExportButton.tsx`; `src/components/market-performance/SentimentGauge.tsx` (DSGN_REBRND's file, carried under round-8's ruling) | FWD-12 (portal DEV CI green) | round-8 analysis item 8 + ADDENDUM 12:3xZ (0.0.0_AB_MSTR 97061): five lint errors | A | ~3 |
| `FE-s-53` | `contracts/adapt.ts` (`adaptStatusEnvelope`, `wireEnvelope`'s `NO_STATUS_REASON` path) | FWD-6 | round-8 analysis item 2 (W3-S37): the reason travels with the explicit unknown on every path the grant excluded | A | ~4 |
| `FE-s-54` | `contracts/adapt.ts` (`adaptStatusEnvelope`'s `status-summary`/`status-job` handling) | FWD-6 | round-8 analysis item 3 (W3-S38): a stated PARTIAL at the top level is the response's stated state; first act is the read 3.0.0_SA_CVO did not make (which production components render those two operations' state) | A | ~5 |
| `FE-s-55` | `tabs/holdings/slices.ts:100-102` | FWD-5 | round-8 analysis item 5 (W4-S19): a non-authoritative Holdings partition reads "withheld", not "unknown" | A | ~6 |
| `FE-s-56` | `__tests__/fe-s-14/` (the control's git-form re-point); `fixtures/index.ts:77` | FWD-12 (evidence prose) | round-8 analysis items 6-7 (W2-S35, W4-S20): `2.0.0_SA_COO~F`'s two rows, one cell | A | ~7 |
| `FE-s-57` | `contracts/index.ts` (`Availability`, new `UnprojectedGrant` type); `contracts/adapt.ts` (`wireEnvelope`, new `carryUnprojectedGrant`); `contracts/envelope.ts` (`parseIrEnvelope`) | FWD-3, FWD-4, FWD-5, FWD-6, FWD-8, FWD-11 (the carrying half; no rendering yet) | PRD v0.7/v0.8/v0.9 `unprojected_grant` paragraph | A (ROOT) | ~8 |
| `FE-s-58` | `state/status.ts` (`AvailabilityLike`, `TabEnvelope`, `envelopeFromAvailability`, `envelopeFromRefusal`); `tabs/StatusPanel.tsx` | FWD-3, FWD-4, FWD-5, FWD-6, FWD-8 (rendering half); FWD-11 (verified, not cut) | PRD v0.7/v0.8/v0.9, closes F4/F5/F6/F7/F8 via the shared panel | B (dep FE-s-57) | ~1 |
| `FE-s-59` | `header/ScopeSummary.tsx` | FWD-1, FWD-11 | PRD v0.7/v0.8/v0.9, closes F2 | B (dep FE-s-57) | ~2 |
| `FE-s-60` | `render/narrative/PeriodInContextPage.tsx` (+ `compose.ts` if the packet's field needs surfacing there first) | FWD-8 | PRD v0.7/v0.8/v0.9, closes F10 | B (dep FE-s-57) | ~3 |

**11 of 11 evaluated, 0 NOT-EVALUATED. Coverage by subtraction: round-8's 7 named items - 7 cut (A-G) = 0
uncovered; the PRD's 9-cell reach - 5 (shared panel) - 1 (F11, verified) - 2 (F2, F10, own cells) - 1 (F12, the
root itself) = 0 uncovered.**

### R9.2 THE CELLS

**FE-s-50 through FE-s-56** carry the CTO's own diagnosis verbatim (round-8 analysis items 1-9 quoted above);
each worker's task order inlines the exact file, line and remedy the analysis already named, so no further
design judgment is exercised at L5 for these seven -- the cut is the analysis restated as a cell boundary.

**FE-s-57 (the root).** `contracts/index.ts:110-134`'s `Availability` gains one new member,
`unprojectedGrant: UnprojectedGrant | null`, and a new exported type `UnprojectedGrant { readonly count:
number; readonly denominator: number; readonly kinds: readonly string[] }`, disjoint from every existing
member. `contracts/adapt.ts`'s `wireEnvelope()` (`:220-258`) gains an optional part `unprojectedGrant?:
UnprojectedGrant | null`, defaulted to `null` (the explicit unknown for "not yet attached" -- every existing
adapter call site is UNCHANGED, since the parameter is optional and every one of the ten document adapters
already flows through `wireEnvelope`). A NEW function, `carryUnprojectedGrant<T>(view: T, grant:
UnprojectedGrant | null): T`, mirrors `carryAvailabilityFromStatus`'s array/object recursion exactly (same
shape, same null-safety, stamping `view.availability.unprojectedGrant = grant` and nothing else).
`contracts/envelope.ts`'s `parseIrEnvelope()` (`:180-237`): on the REFUSED branch (`:195-208`), no change --
absence is by design and the function already returns `data: null`. On the non-refused branch, after `const
data = carryAvailabilityFromStatus(...)` (`:219`), read `body.unprojected_grant`; if it is not
`{count: number, denominator: number, kinds: string[]}`-shaped, throw `EnvelopeMismatch('unprojected_grant',
operation)` (mirroring the file's own established idiom -- ⛔ the `irpt-holdings` route's fork bug still SENDS
the key, always `{count: 0, ...}` per the PRD's v0.9 paragraph, so this throw fires only on a route that omits
the key entirely, which the PRD calls a genuine backend defect, never on holdings); else call
`carryUnprojectedGrant(data, grant)` before returning. `IrEnvelopeField` (`:69`) gains `'unprojected_grant'`.
**Bound: this cell renders NOTHING.** It is the carrying half only; FE-s-58/59/60 are the rendering half, and
the split exists so the parsing contract can be graded (12 of 12 `RESPONSE_OPERATIONS`, present-at-zero on
every non-refused response) independently of any pixel.

**FE-s-58.** `state/status.ts`'s `AvailabilityLike` (`:204-212`) and `TabEnvelope` (`:77-89`) each gain
`unprojectedGrant?: UnprojectedGrant | null`; `envelopeFromAvailability` (`:215-230`) copies
`availability.unprojectedGrant` across; `envelopeFromRefusal` (`:258-267`) sets it to `null` explicitly (a
refusal's `publicReasonCode` -- `UNPROJECTED_GRANT` included -- already renders verbatim via the EXISTING
`reason-code` slot at `StatusPanel.tsx:70-79`, confirmed by source read: no new code needed for the refusal
branch). `tabs/StatusPanel.tsx` gains a new slot, `data-slot="partial-disclosure"`, rendered when
`envelope.unprojectedGrant && envelope.unprojectedGrant.count > 0`, showing the count, denominator and kinds
list in the panel's existing visual idiom (a `<p>` beside the reason-code slot, same text sizing, navy ink on
the white panel per portal `CLAUDE.md`'s color law -- never a light-on-light badge). **Acceptance must exercise
Global mode** (`global/useFirmContext.ts` + the shared tab bodies) to CONFIRM F11's coverage is inherited, not
assumed -- a positive control render under a cross-firm selection, count>0, badge visible.

**FE-s-59.** `header/ScopeSummary.tsx` takes `scope: ResolvedScope | null` directly (`:41`); render the same
badge idiom reading `scope?.availability.unprojectedGrant`, placed beside the existing `Fact` grid (`:72-86`),
never inside the cohort blocks (a different concern, not to be conflated per this file's own withheld/unknown
distinction).

**FE-s-60.** `render/narrative/PeriodInContextPage.tsx` composes from `NarrativePacket` (`:51`); render the
same badge reading `packet.availability.unprojectedGrant`, on the page itself (this IS the exported-PDF path,
so the badge must appear in BOTH the on-screen preview and the printed PDF -- one render, both consumers, no
second copy).

### R9.3 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-50 <- (none)   READY ROOT   wave A
  FE-s-51 <- (none)   READY ROOT   wave A
  FE-s-52 <- (none)   READY ROOT   wave A
  FE-s-53 <- (none)   READY ROOT   wave A
  FE-s-54 <- (none)   READY ROOT   wave A
  FE-s-55 <- (none)   READY ROOT   wave A
  FE-s-56 <- (none)   READY ROOT   wave A
  FE-s-57 <- (none)   READY ROOT   wave A
  FE-s-58 <- FE-s-57  wave B, seated on FE-s-57's drain
  FE-s-59 <- FE-s-57  wave B, seated on FE-s-57's drain
  FE-s-60 <- FE-s-57  wave B, seated on FE-s-57's drain

  weakly connected components: 8   ready roots at issuance: 8
  wave A = {50,51,52,53,54,55,56,57}   max concurrent width: 8
  wave B = {58,59,60}   max concurrent width: 3, seated only after 57 merges
```

Disjoint by FILE within wave A: `gen-wire.ts`/tests (50), a new verification test (51), the five lint files
(52), `contracts/adapt.ts` for TWO disjoint functions -- `adaptStatusEnvelope`'s no-status branch (53) and its
status-summary/status-job branch (54) -- **same file, two cells: SERIALIZED, not concurrent** (see below),
`tabs/holdings/slices.ts` (55), `__tests__/fe-s-14/` + `fixtures/index.ts` (56), and the three `contracts/*`
files (57, none shared with 50-56). **53 and 54 share `contracts/adapt.ts` and are NOT disjoint by file --
seated in the SAME wave-A slot sequence (~4 then ~5), never concurrently, same worker or a hand-off commit
between them; this is the one exception to "wave A is 8 concurrent" and is stated here rather than silently
assumed.**

**Fan-out: `8 of 8 chains, cap 8, reason: seven independent items from the CTO's round-8 analysis with no
shared file (save 53/54, sequenced within the same chain) plus one new root for the PRD's carrying half; the
rendering half (58, 59, 60) has no ready root until 57 drains, so it seats in wave B, width 3`.**

### R9.4 RULE 24 RECORD (round 9)

| postulate | how |
|---|---|
| (i) MECE | round-8's 7 named items: 7-7=0 uncovered (R9.1). The PRD's 9-cell reach: 9-5(shared panel)-1(F11, verified not cut)-2(F2,F10)-1(F12 root)=0 uncovered. |
| (ii) same grain | every wave-A cell is a (file, named defect) pair at the FILE grain; wave-B cells are (file, new-field-consumption) pairs at the same grain. |
| (iii) intent | 50-56: each restates ONE ruling from round 8's analysis, one axis each (hashing, ancestry, lint, reason-carriage x2, withheld-text, control re-point). 57: parse and carry, never render. 58-60: render only, never re-derive the count. |
| (iv) state | Moves: FWD-1,3,4,5,6,8,11,12 toward EXERCISABLE evidence (fixture-bound; EXERCISED proofs still wait on IRPT_BCKEND per SEQUENCE.yaml, unchanged from round 8). Does NOT move: the `irpt-holdings` route's own fork bug (CTO-owned, `IB-rtf-8`, PARKED); the portal freeze; any grade to REALIZED; 3.0.0_SA_CVO's backfill question (at Andrew); S66 the backend admin wall (still at Andrew per round-8 item 1, unanswered as of this cut). |

### R9.5 HOLDS

- **PORTAL FROZEN:** local DEV commits only. No CLOUD push and no SITEZ merge until Andrew's word.
- **The seat.** Re-seated on IRPT_FNTEND as this session's sole focus, Andrew-direct 2026-09-21 ~12:37Z
  (`org/tier1_exec/2.0.0_SA_COO~F/deliverables/ANDREW_DIRECT_20260921_1237Z_COOF_SOLE_FOCUS_IRPT_FNTEND_CANONICAL_FLOW_THEN_DRIVE.md`),
  superseding the 2026-09-15 free-after-round-8 plan.
- **S66 (the backend admin wall) stays at Andrew**, unadjudicated by this cut; it names no cell here.


---

## R10 -- ROUND 10: FWD-12'S CLOSING PASS, THE ONE CARD THAT DOES NOT CROSS TO IRPT_BCKEND

**Source.** `1.0.0_SA_CTO`'s grades on this project's round-9 completion report
(`ledger/COMPLETION_GRADES.round9.json` @4030dac, msg 99254): 8 of 8 outcomes `NOT_EVALUATED`, none `NOT_REALIZED`, so no L5
recut and no SCOPE_CHANGE. Every cited proof is fixture-bound (303 criteria across 19 proofs, 0 reaching a live route). Seven cards
(FWD-1, 3, 4, 5, 6, 8, 11) CROSS to IRPT_BCKEND and their closing passes wait on its half. **FWD-12 is the one card whose PRD row
says `IRPT_BCKEND is NOT ENGAGED`, so its closing pass is cuttable now.** The grader's spec: *"the real route, all three tabs plus
the export, read against DESIGN.md at the CURRENT vintage."* One finding bears on it: FE-s-11's recorded `CANVAS` is
`rgb(195, 202, 218)`, the silver ground the 2026-09-11 ruling retired; `portal/CLAUDE.md` now requires `rgb(244, 246, 250)`. The same
pass answers round 9's open `F60-AC6` color-law question.

**A correction to this seat's own round-9 read.** This seat told the CTO "no PRD-endpoint gap to cut a cell for." That was true on the
COVERAGE axis and this seat over-extended it to "nothing left to build." The REALIZATION axis, read against the exercised artifact,
found a cuttable gap. The two axes are separate documents for exactly this reason.

### R10.1 THE RECTANGLE -- four cells

**MECE by subtraction.** The surfaces FWD-12's DONE WHEN names (an advisor uses all three tabs and the export) are five: the header
(scope and search), the Reporting tab, the Analysis tab, the Holdings tab, the export (modal, preview, print page). 5 named surfaces
- 5 assigned = 0 uncovered. The census cell is not a sixth surface: it is the PRD's own FWD-12 PROOF limb ("a census of EVERY
component the page uses ... denominator printed"), refreshed at the current vintage.

| cell | write surface | serves | source | wave | slot |
|---|---|---|---|---|---|
| `FE-s-61` | evidence: `deliverables/0.9.0_WK_IRPT_FNTEND~11/`; portal: `header/` and `tabs/reporting/` only | FWD-12 | the grade's spec: the real route, header and Reporting tab, read against DESIGN.md at the current vintage | A | ~1 |
| `FE-s-62` | evidence: `deliverables/0.9.0_WK_IRPT_FNTEND~12/`; portal: `tabs/analysis/` and `tabs/holdings/` only | FWD-12 | the same, Analysis and Holdings tabs | A | ~2 |
| `FE-s-63` | evidence: `deliverables/0.9.0_WK_IRPT_FNTEND~13/`; portal: `export/` and `render/` only | FWD-12 | the same, the export modal, the preview and the print page; also round 9's open `F60-AC6` | A | ~3 |
| `FE-s-64` | evidence ONLY: `deliverables/0.9.0_WK_IRPT_FNTEND~14/`; NO portal write | FWD-12 | the PRD's FWD-12 PROOF limb: the component census and the colour-law scan, at the current vintage | A | ~4 |

**Not cut, and why.** FWD-1, 3, 4, 5, 6, 8, 11: each card names what IRPT_BCKEND supplies and the PRD says a frontend mock cannot close
that half. `IB-rth-2` (the export submit controller) is still pending in IRPT_BCKEND round 8, and FWD-5 is also bound by PRD v0.9's
`irpt-holdings` count-0 exemption until `IB-rtf-8`. Cutting a fixture-fed pass for them would repeat exactly what the grades found
insufficient. They wait, named here so the wait is a record and not an omission.

### R10.2 BOUNDS -- ALL ROUND-10 CELLS (rounds 1-9 bounds stand)

```
  what a closing pass is  EXERCISE the real route with the round's fixtures fed at the network layer (ui-smoke --fixtures), READ every
                          capture, and record what it shows against DESIGN.md at the CURRENT vintage. It is evidence first.
  fixture-fed, said so    these passes do not reach a live route (none can: IRPT_BCKEND is not serving). Each result file says so in
                          its first paragraph; FWD-12's DONE WHEN limb (familiarity on the real route) needs no counterpart half, which
                          is why fixture-fed evidence is the correct kind HERE and insufficient for the other seven.
  canvas                  every capture's `CANVAS:` line must read rgb(244, 246, 250). The FE-s-11 capture recorded rgb(195, 202, 218);
                          both values are quoted side by side in the result, so the check has an arm that can fail.
  fixes                   a defect a capture in THIS pass demonstrates, on the cell's OWN surface (its portal write surface above), may be
                          fixed by the cell, with a BEFORE capture kept and an AFTER capture beside it, one fix per finding. A defect
                          whose fix needs any other file (StatusPanel.tsx, state/, src/index.css, App.tsx, any file outside
                          InvestorReporting/, or another cell's surface) is ONE ROW and the cell keeps going. Never widen your own grant.
  dev server              start your worktree's own vite dev server on its own derived port (export IRPT_FE_DEV_PORT), and STOP IT before
                          the whole-suite criterion; verify the port is closed. A live server makes the browser-gated suites run instead
                          of skip, which is a different measurement (measured this round: rows W8-S1, W9-S1).
  judgment                the last criterion of each order is a JUDGMENT criterion: RECORD the evidence, give NO verdict. It is graded
                          by the CVO at L9 and is never self-graded.
```

### R10.3 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-61 <- (none)   READY ROOT   wave A
  FE-s-62 <- (none)   READY ROOT   wave A
  FE-s-63 <- (none)   READY ROOT   wave A
  FE-s-64 <- (none)   READY ROOT   wave A

  weakly connected components: 4   ready roots at issuance: 4   max concurrent width: 4
```

Disjoint by FILE: portal write surfaces are `header/`+`tabs/reporting/` (61), `tabs/analysis/`+`tabs/holdings/` (62), `export/`+`render/` (63),
none (64). Every shared file (`tabs/StatusPanel.tsx`, `state/`, `contracts/`, `src/index.css`, `src/App.tsx`) is read-only to all four. The
one shared write is the append-only `INVESTIGATION_v2.md`, which conflicts at every concurrent drain and is resolved as union.

**Fan-out: `4 of 4 chains, cap 8, reason: four independent surfaces of one card with no shared write file; the count is the number of
surfaces FWD-12's DONE WHEN names plus its census limb, not a cap-fill`.**

### R10.4 RULE 24 RECORD (round 10)

| postulate | how |
|---|---|
| (i) MECE | FWD-12's named surfaces: 5 - 5 assigned = 0 uncovered; the census is the PROOF limb, not a surface. The other seven cards: 7 - 0 cut = 7 deliberately not cut, each with its counterpart dependency named. |
| (ii) same grain | every cell is a (surface, closing-pass) pair at the surface grain. |
| (iii) intent | one axis per cell: what the real route SHOWS at the current vintage (61-63), and what the tree CONTAINS at the current vintage (64). |
| (iv) state | Moves: FWD-12 from `APPLIED` toward `EXERCISED` on the real route. Does NOT move: FWD-1, 3, 4, 5, 6, 8, 11 (counterpart-dependent); any grade to `REALIZED` (the CTO's, on the exercised artifact); the portal freeze; `W3-S41` (no cell reaches `proof-of-spec-check.py`). |

### R10.5 HOLDS

- **PORTAL FROZEN:** local DEV commits only. No CLOUD push, no SITEZ merge, until Andrew's word.
- **`COMPLETION_REPORT.round1.json`** is ungraded history, superseded by round 9 (CTO, msg 99254). Left as it is.
- **The CVO seat for this project is `3.0.0_SA_CVO~F`** (Andrew-direct 2026-09-21; identity resolved to the Codex seat, PID 28148).


---

## R11 -- ROUND 11 (decomposition v0.11): the FWD-12 remediation pass

**Source.** `3.0.0_SA_CVO~F`'s round-10 L10 slug (`surprise-channel/remediations/REMEDIATION_v7.md` @`e1fbcf38d0`, 14 rows) and `1.0.0_SA_CTO`'s round-10 analysis
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_10_20260921.md` @`3020f2a580`, msg 99318; shape accepted with one condition in msg 99324).
Round 10 closed with FWD-12 `NOT_REALIZED`: grounded C3, C8 and C12 violations remain on shipped surfaces and the Reporting tab's answer-bearing state was never rendered.
The other seven outcomes stay `NOT_EVALUATED` on the IRPT_BCKEND crossing and are NOT re-cut here (they wait, named so the wait is a record).

### R11.1 THE RECTANGLE -- nine cells

| cell | write surface | serves | wave | slot | depends_on |
|---|---|---|---|---|---|
| `FE-s-65` | evidence: `deliverables/0.9.0_WK_IRPT_FNTEND~15/`; portal: `scripts/ui-smoke.mjs` (additive) and its own `__tests__/fe-s-65/` | the instrument (a1) | 1 | 1 | none -- READY ROOT, every other visual cell depends on this |
| `FE-s-66` | `fixtures/smoke/` and `__tests__/fe-s-66/` | fixture classification + answer-bearing pair (a2) | 1 | 2 | none -- READY ROOT |
| `FE-s-73` | evidence: `deliverables/0.9.0_WK_IRPT_FNTEND~23/`; `__tests__/fe-s-73/`; NO component edit | census reasons (g) | 1 | 9 | none -- READY ROOT |
| `FE-s-67` | `index.tsx`, `tabs/StatusPanel.tsx`, `tabs/analysis/GenerateComposer.tsx`, `tabs/holdings/DrillTree.tsx`, `__tests__/fe-s-67/` | shared C12 error presentation (b) | 2 | 3 | FE-s-65 |
| `FE-s-68` | `tabs/reporting/`, `header/ScopeSummary.tsx`, the fe-s-42/48/59 pins, `__tests__/fe-s-68/` | Reporting answer-bearing + scope strip (c) | 2 | 4 | FE-s-65, FE-s-66 |
| `FE-s-69` | `components/ui/PageSurfaceControl.tsx` (additive), `header/FirmDropdown.tsx`, `pages/ModelPortfolios.tsx` (dropdown className only), `__tests__/fe-s-3/`, `__tests__/fe-s-69/` | shared dropdown class token (d) | 2 | 5 | FE-s-65 |
| `FE-s-71` | `export/` (whole folder), `__tests__/fe-s-16/mounted-states.test.ts` (one assertion), `__tests__/fe-s-71/` | export modal chrome + receipt flow state (e) | 2 | 7 | FE-s-65 |
| `FE-s-72` | evidence: `__tests__/fe-s-72/` only, NO source write | Holdings withheld + reachable Analysis states (f) | 2 | 8 | FE-s-65 |
| `FE-s-70` | `components/CategoryViewTree.tsx`, `tabs/holdings/DrillTree.tsx` (one line), `__tests__/fe-s-70/` | CategoryViewTree light variant (d2) | 3 | 6 | FE-s-65, FE-s-69 |


**Why the instrument is a cell of its own (FE-s-65).** The CTO's criterion rule (a)-(d) is unmeetable with `scripts/ui-smoke.mjs` as it stands: its `TEXT:` line is
`document.body.innerText.slice(0, 160)` and its `CANVAS:` line is `getComputedStyle(document.body)`, the page field. Rule (b) needs content asserted by selector or text and rule (d)
needs the ground of a route's own container. The instrument is additive, its grammar is fixed in FE-s-65's order, and every other visual cell is cut against that exact grammar.

**Where the write paths were partitioned (the CTO left B/D to this decomposition).** Two workers never share a write path:
- `tabs/holdings/DrillTree.tsx` belongs to B WHOLLY (its C12 error text AND its purple breadcrumb, the C8 half of W12-S2). D2 edits the shared `CategoryViewTree` container only.
- `header/ScopeSummary.tsx` belongs to C (the scope strip's partial-disclosure fact is captured there, so the strip's own style residuals travel with it: W11-S4's ScopeSummary part). D keeps only the dropdown part of W11-S4.
- `export/` belongs to E WHOLLY: C-S130 (chrome) and S69 (receipt states) both live in `ExportModal.tsx` and `ReceiptPanel.tsx`, so they are ONE cell rather than a chain.
- F and G write no source at all (evidence and deliverables only), so they conflict with nothing.
- The instrument (FE-s-65) is the only cell that writes `portal/scripts/`; the fixtures (FE-s-66) are the only cell that writes `fixtures/smoke/`.

**Not cut.** `PageSurfaceControl`'s own `surfaceBase` (`font-medium`, C1): six production importers, four of them AdvisorIntelligence partner dashboards outside the product. Ruled out of IRPT's
scope and parked by `1.0.0_SA_CTO` (msg 99324); row `IRPT_FNTEND-S70` (commit `117c3dac03`) carries the six-file census. No round-11 cell touches it.

### R11.2 BOUNDS -- ALL ROUND-11 CELLS (rounds 1-10 bounds stand)

```
  the criterion rule     every VISUAL criterion carries (a) wire match (`FIXTURES-MATCH: matched N of N`), (b) named content by selector or text, (c) a wrong-state negative
                         control that must FAIL (`ASSERT-CONTENT: 0 of N met`), and (d) the ground measured on the actual route container with a wrong-ground control
                         (`--inject-css` silver; the same assertion prints FAIL rgb(196, 203, 219)). A criterion missing any of the four is refused at the cut. The PNG is
                         still read, but it is a JUDGMENT input, never the pass/fail line.
  a control is a claim   a control that passes proves the assertion cannot tell the states apart: the worker says so and fixes the assertion, never reports it as met.
  instrument first       every visual cell depends on FE-s-65's flags; a worktree whose `ui-smoke.mjs` refuses `--expect` has the wrong base and stops.
  fixes                  a defect on the cell's OWN surface may be fixed with a BEFORE capture kept and an AFTER beside it; a fix needing another cell's file is ONE ROW.
                         A test inside the cell's grant that pins the OLD behaviour is updated in the same commit and named in the result. A shared component's fix names
                         EVERY consumer's exact-class test and carries before/after captures of each consumer (the CTO's rule for D and D2).
  dev servers            each worker's own server on its own port block (5900-5989, outside the derived range 5400-5899 the browser-gated tests use), set as an INLINE
                         PREFIX on the server command and never exported; stopped, and the port verified closed, before the whole-suite criterion.
  judgment               the last criterion of each order is JUDGMENT: record the evidence, no verdict; the CVO grades it at L9.
  context                a worker keeps its context small (a prior worker stalled twice on an oversized one): at most the PNGs its criteria need, long output to files.
```

### R11.3 DEPENDENCY EDGES, SLOTS, FAN-OUT

```
  FE-s-65 <- (none)               READY ROOT   wave 1
  FE-s-66 <- (none)               READY ROOT   wave 1
  FE-s-73 <- (none)               READY ROOT   wave 1
  FE-s-67 <- FE-s-65                            wave 2
  FE-s-68 <- FE-s-65, FE-s-66                   wave 2
  FE-s-69 <- FE-s-65                            wave 2
  FE-s-71 <- FE-s-65                            wave 2
  FE-s-72 <- FE-s-65                            wave 2
  FE-s-70 <- FE-s-65, FE-s-69                   wave 3

  weakly connected components: 1 (every cell traces to FE-s-65 or is itself a root)
  ready roots at issuance: 3 (FE-s-65, FE-s-66, FE-s-73)
  max concurrent width: 5 (wave 2, once wave 1 drains)

```

**Fan-out: `3 of 9 cells cut ready NOW (wave 1), 5 more gated on FE-s-65 (wave 2), 1 gated on FE-s-65 AND FE-s-69 (wave 3), cap 8`.**
The count is 9 because the CTO's round-10 analysis named 9 surfaces (the instrument, the fixtures, 5 defect families, the census, and the container-variant split of one of them); it is not a cap-fill. Two workers never share a write path: `DrillTree.tsx` is split between B (its C12 text and breadcrumb) and D2 (one line passing a new prop), and each order's `<paths>` says so explicitly.

### R11.4 RULE 24 RECORD (round 11)

| postulate | how |
|---|---|
| (i) MECE by subtraction | The slug carries 14 rows. Subtract the two REMEDIATED (`W13-S1`, `W13-S3`) and `W13-S2` (its class hazard is carried by the criterion rule's (d); its local fix landed at portal `8894e765`): 11 rows remain, each assigned to at least one cell. `W11-S1`,`W12-S1` -> FE-s-66; `W11-S2` -> FE-s-68 (its precondition, the answer-bearing fixture, is FE-s-66); `W11-S3`,`W12-S3` -> FE-s-67; `W11-S4` -> FE-s-68 (ScopeSummary) AND FE-s-69 (dropdown), one row split across two cells on purpose; `W12-S2` -> FE-s-70 (container) AND FE-s-67 (the breadcrumb, C8); `W14-S2` -> FE-s-73; `S69`,`C-S130` -> FE-s-71; `C-S129` -> FE-s-72. 11 assigned - 11 = 0 uncovered. `S70` is deliberately unassigned (parked, ruled out of scope). |
| (ii) same grain | each cell is one surface family with one write-path set; the two split rows are split BY FILE, not by intent |
| (iii) intent coherence | every cell is a fix-with-proof of one clause family (C12 error presentation; C3/C8 shared style; the answer-bearing state; the instrument; the fixtures; the receipt state; the reachable states; the census reasons) |
| (iv) state coherence | what a cell does NOT move is named in its order: FE-s-69 does not touch `surfaceBase`; FE-s-70 keeps canonical data colours; FE-s-72 builds no request-list route (C-S129 ruling); FE-s-73 edits no component |

**The older open rows a cell touches** (the CTO asked the issuance to name them, no bulk close). By the latest row per id across `REMEDIATION_v1..v7`, MY count is
67 older open rows against the CTO's 65; the two instruments differ (I read each id's latest `remediation.state`) and I have not reconciled them. The list below is a
NAME MATCH (the row's text names a file a cell edits), not a reading of each row: each cell's order carries its list, tells the worker to read them, and to say in its result which
its change resolves. Nothing is closed here; the CVO dispositions.

| cell | older open rows it may touch |
|---|---|
| `FE-s-65` | W1-S51, W1-S52, W2-S23, W3-S26 |
| `FE-s-66` | W1-S51, W1-S53, W2-S27, W2-S29, W5-S7 |
| `FE-s-67` | W1-S19, W1-S35, W1-S46, W1-S51, W2-S21, W2-S23, W2-S33, W3-S6 |
| `FE-s-68` | W2-S33, W3-S29, W3-S30, W3-S31, W3-S6 |
| `FE-s-69` | (none named) |
| `FE-s-70` | (none named) |
| `FE-s-71` | W1-S11, W2-S27, W2-S33, W3-S29, W3-S30, W3-S31 |
| `FE-s-72` | W1-S46, W2-S21, W2-S33 |
| `FE-s-73` | C-S43, S42, W1-S11, W1-S46, W1-S57, W3-S26, W3-S33, W3-S37, W4-S11, W4-S15, W6-S1, W8-S2 |


### R11.5 HOLDS

- **PORTAL FROZEN:** local DEV commits only. No CLOUD push, no SITEZ merge, until Andrew's word. (`0.0.0_AB_MSTR` pushes.)
- **C-S129:** the Analysis request LIST has no declared backend route; FNTEND does not invent one. If an FWD's DONE WHEN needs the list it is an IRPT_BCKEND dependency, routed to `2.0.0_SA_COO~B` as information (CTO ruling).
- **W13-S2** disarms when a round-11 criterion exercises (d) with a wrong-ground control: FE-s-65 builds that control and the visual cells use it.
- **The CVO seat for this project is `3.0.0_SA_CVO~F`** (the Codex seat).
