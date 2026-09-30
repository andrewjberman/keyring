# DSGN_IRPTV1 -- status (FAST: /closer-drive under the lease, presence-extended)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.18
@5d44d0fa62. Reviewer `3.0.0_SA_CVO` (grades each landed pin after the fact). Authority: Andrew-direct 17:3xZ record
@229b3fd184; CTO placement @1d443e50db (msg 102388); LIVE_ARMS row `/canonical-drive 10m`, the FAST lease routing each
tick here; post-crash relaunch 2026-09-30 13:0xZ (`org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAUNCH_BRIEF_20260930_130xZ_POST_CRASH.md`).
**As of 2026-09-30T15:2xZ.** Lease read FAST (until 14:23Z, extended by presence stamps). The 07:52Z reboot ended the
previous session mid-wait (DEV 44fd5f42 at Andrew's re-smoke); no worker, worktree, deploy entry or index lock of this
lane survived it (measured 13:1xZ: 84 of 84 task orders terminal, no `.open_deploys/` entry names this seat, no
`index.lock`). 5174 restarted 13:5xZ from the main portal checkout (`bun run dev:live --port 5174`).

## Pins

| What | Value |
|---|---|
| Lease | FAST DSGN_IRPTV1, surface `portal/src/pages/InvestorReporting`, `Positioning/tabs/HoldingsTab.tsx`, `components/holdings`, `components/CategoryViewTree.tsx`, `lib/chartColors.ts`; last ARM line 2026-09-30T01:40:50Z (Andrew-direct rapid design feedback), presence-extended since |
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal candidate pin | DEV `1bcda74c` (item 39, W2-19b) on `775c4261` (item 38, W2-19) on `1d7b8feb` (item 37, lint) on `a20b5a60` (item 36, W2-07) on `44fd5f42` (AF-2, Andrew smoke feedback #2) on `5c7eead8` (AF-1, Andrew design feedback #1) on `b66c31d3` (walk-2 batch 2) on `5068973b` (item 32) on `2da4f470` on `3e2233de` (item 31, PROD v2.1.191) on `a528392f` (item 30) on `18899c96` (item 29) on `27eae57a` (item 28) on `7689c526` / `7b4f4f83` (round 10) on `29b33ef1` (item 27) on `037657da` (26) ... `a47d3a75` (item 1) on `28f5118c` (round 9 drained). The full item 1-35 chain with CI run ids is in git at STATUS.md @a7a6d286f2 and earlier. |
| Portal origin | origin DEV `1bcda74c` (pushed by this seat under the lease, VALGATE pre-push passed; ls-remote read 15:20:12Z `1bcda74cf242`). PROD `ba8e971f` (tag portal-v2.1.191). DEV CI: run 36725618787 (a20b5a60) FAILURE at Run ESLint, as every DEV push since 620ea953 -- row S41 (HeaderBrief.tsx 0x08 bytes, DSGN_AMGTV1's); item 37 removed this lane's four lint errors, the run for 1d7b8feb is read at the next tick |
| Suite on 775c4261 | IR scope 949 pass / 27 skip / 18 fail = the known five + row S40's 13 (967 tests; iv-e-117 green; iv-e-45 and iv-e-63 re-goldened green alone and in the run). Earlier on a20b5a60 | IR scope 920 pass / 27 skip / 18 fail = the known five + row S40's 13 (GET /analysis/comparisons, IRPT_BCKEND ~Y); iv-e-116 green in the suite run and alone. A suite run REGENERATES `contracts/wire/*` onto disk (gen-wire tests): 23 files EOL-only churn, `index.ts` + `responses.ts` gain the ComparisonCatalogue wire (row S40's portal half, ~Y's) -- restored to HEAD after each run, never committed by this lane |
| Screen | `localhost:5174` (dev-live from the main checkout, log `portal/.runtmp/vite-smoke.log`) |
| Workspace push state | CLOUD LOCAL; the push is 0.0.0_AB_MSTR's |

## Live thread

State: LIVE END TO END on DEV for Holdings, Performance and Analysis. Last real run: item 36's fixture-plane
Generate journey on 5174 @a20b5a60 working tree (`deliverables/2.0.0_SA_COO~D/item36/w2-07.fast-run.png`). The
live press stays Andrew's (walk-2 write guard).

## Write claims

- `2.0.0_SA_COO~D`: `portal/src/pages/InvestorReporting/tabs/analysis/*` (W2 analysis items), `tabs/holdings/*`,
  `tabs/reporting/*` (W2-01 residue), `src/components/holdings`, `src/components/CategoryViewTree.tsx`, `src/lib/chartColors.ts`.
- Next claim: W2-01 front residue (`tabs/reporting/ReportingTab.tsx:260-263,467-484`, `tabs/holdings/AccountFilter.tsx:136-141`).

## Landed under FAST since STATUS @a7a6d286f2 (items 1-35 recorded there; graded by the CVO after the fact)

| Item | Pin | Rows / brief | Check |
|---|---|---|---|
| AF-1 | portal `5c7eead8` (origin DEV) | Andrew-direct design feedback 2026-09-30 ~01:4xZ: pie contrast, Client grey, top-10 map with multi-select chips, account picker removed, name without ticker | tsc 0; IR suite 920/18 (known 5 + S40 13); Andrew smoked 5174 |
| AF-2 | portal `44fd5f42` (origin DEV) | Andrew smoke feedback ~05:0xZ: Securities table folded per Sleeve/Account view (his word = the F7-AC4 exception), map tooltip name-only + 'Other Securities' + Client chip, cash-first class order, account dialog sleeves by value with collapsible buckets | tsc 0; IR suite 920/18; vite served the six modules 200 |
| 36 | portal `a20b5a60` (origin DEV, ls-remote 13:58Z) | W2-07: after Generate the ISSUED request opens in the page's own dialog (status in words, Technical details behind one control, report sections when READY) and "Your analysis requests" re-lists from the first page; `requestToOpenAfterSubmit` in composer.ts, `onSubmitted` on GenerateComposer, `openRequest` on OwnedRequestHistory, wired in AnalysisTab | iv-e-116 GENERATE-JOURNEY-OK (pre-fix press branch as the negative control); tsc -b 0; eslint 0 errors; real run on 5174, fixture plane (no live write): VERDICT GENERATE-JOURNEY-REAL-OK -- POST /analysis once, dialog on REQ-0123...4567 "Job status: Ready" + one section, row listed, /analysis/requests re-read; shot `deliverables/2.0.0_SA_COO~D/item36/w2-07.fast-run.png` |
| 37 | portal `1d7b8feb` (origin DEV, ls-remote 14:19Z) | Lint hygiene in surface: iv-e-106's non-ASCII check is a code-point count (no-control-regex), iv-e-116's two wiring regexes use `{2}` / `{4}` (no-regex-spaces); the two remaining repo lint errors are HeaderBrief.tsx:47-48's literal 0x08 bytes (row S41, DSGN_AMGTV1's) | eslint rc=0 on both files; both tests green; `bun run lint` 6 -> 2 errors (the two out of surface) |
| 38 | portal `775c4261` (origin DEV, ls-remote 14:57Z) | W2-19 (absorbs UIC-14): `holdingsFooterSource(snapshot, vendorWords)` prints the snapshot's `sourceVendorKeys` as words through an injected registry vendor view, else the one fallback string; `provenance.sourceCoordinate` (a producer function name) never reaches the face (help tip only); DrillTree hands the card `source={holdingsFooterSource(snapshot)}` so card, map and table footers are one string | iv-e-117 FOOTER-SOURCE-WORDS-OK (pre-fix body as the negative control); iv-e-45 UIR-45d + iv-e-63 IVE63-2b re-goldened; tsc -b 0; eslint 0 errors; real run on 5174 (fixture plane): three "Source:" lines on the Holdings tab, one distinct string, 0 function-named -- VERDICT FOOTER-SOURCE-REAL-OK, shot `deliverables/2.0.0_SA_COO~D/item38/w2-19.fast-run.png` read (card line, map footer, table footer identical) |
| 39 | portal `1bcda74c` (origin DEV, ls-remote 15:2xZ) | W2-19b: PerformanceHeadline's footer reads `PERFORMANCE_FOOTER_SOURCE_WORDS`, never `lineage.sourceCoordinate` (kept in the header help tip); the report wire carries no vendor keys, so the face reads the one attribution string until a vendor view + served keys exist | iv-e-117 ARM (d) OK; iv-e-63 IVE63-2a re-goldened; tsc -b 0; eslint 0 errors; real run on 5174 (fixture plane, Performance tab): 0 function-named, 0 served coordinates on the face; the panel footer reads the words (shot `deliverables/2.0.0_SA_COO~D/item39/w2-19b.performance.fast-run.png` read); the source-age line inside Report details reads "Black Diamond, as of ..." (already words) |

## Next (in order; the enrichment backlog from the walk-2 state table @f80d019a6c, front-end-only and unblocked first)

0. **IRPT_DASHBD workstream F, round-1 cell = FWD-1 hop 5, CUT HERE as a closer-drive item** (CTO 103252 + 103261: L4-R ADMITTED, CVO half @9914eab4f4, review `org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_REVIEW_IRPT_DASHBD_v0.1_20260930.md`; PRD v0.1 @2cb022f549, C-LEASE + ruling 6.7). Review condition carried: today's lease surface covers the whole `portal/src/pages/InvestorReporting` tree, so the NEXT DSGN_IRPTV1 lease arm (the CTO's) excludes `tabs/reporting/` + `dashboard/` or holds; under FAST this seat builds F's items itself either way. Under this live FAST
   lease the Performance chart reading `series` (honest label "Total return, before advisory fees" + method version, C-HONESTY
   coverage sentences) is built HERE as a closer-drive item reading FWD-1 and C-SEAM. PARKED until workstream B
   (`2.0.0_SA_COO~P`) lands `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` and a served `series.json.gz` (measured 14:1xZ:
   no contract file, no `dashboard/` dir, no IRPT_DASHBD task order, CVO half of the PRD unsigned); "any hop fed by a fixture
   fails the outcome", so nothing is built against an invented shape. Write surface when it un-parks:
   `tabs/reporting/` and the new `dashboard/` only.
1. **W2-19 words half** (this lane's reader is ready; the VIEW is the LGIC lane's): a `VENDOR_DISPLAY_NAMES` generated
   view in `lib/opal_naming.py` (the `FIRM_DISPLAY_NAMES` mechanism) over `infra/logic/registry/systems.json` VENDOR
   rows, which today carry only slugs (`blackdiamond`, `wall-street-journal`) and no display words -- a registry field
   to add, never a hand-typed page map (UIC-14, CTO 102443). Asked of `1.0.0_SA_CTO` 15:0xZ. When it lands: import it
   in `slices.ts` callers and re-golden iv-e-117 ARM (c).
2. **W2-01 front residue** (P0 front half): the refusal names the missing upstream day; the picker's 'pending' word
   settled -- `tabs/reporting/ReportingTab.tsx:260-263,467-484`, `tabs/holdings/AccountFilter.tsx:136-141`. The
   figure itself is ~P's (S173).
3. **W2-22 remainder** (P1): the card's selection drives the map and the table on every axis (batch 2 landed the
   account axis only) -- `HoldingsTab.tsx`, `HoldingsTreemap.tsx:420`, `SecurityList.tsx:192-207`.
4. **W2-16** (P2): only if the Next-button clip reproduces at a narrower viewport (not reproduced at 1440).
5. **W2-20 front residue**: retire the 'Rebalancer strategy:' label path (`slices.ts:473-475`) once ~M's re-mint is
   the served shape (parked until then; retiring it early would blank a still-served node).

Blocked on another seat (not cut here): W2-04 / W2-05 (a served catalog read, `2.0.0_SA_COO~Y`); W2-13 industry
sub-line (served field); W2-12 / W2-14 (the narrowed class release under CTO 103168, `2.0.0_SA_COO~M`); W2-15 class
totals (a served per-class total, or a CTO ruling on F7-AC4); W2-06 correction words (CTO decision on the seat);
W2-07's other half (why a job needs attention, IRPT_BCKEND); row S40's portal half of GET /analysis/comparisons
(`2.0.0_SA_COO~Y`).

## Open at Andrew

- Re-smoke DEV `1bcda74c` on `localhost:5174` (his last re-smoke target was 44fd5f42; items 36-39 sit on top of it).
- PROD promote call (DEV carries AF-1, AF-2, items 36-39 and walk-2 batches 1-2 above PROD v2.1.191).
- FCASH fold scope (whether FCASH folds into the Cash row).

## Parked (one line each, owner + the condition that un-parks it)

- Suite-run wire regeneration leaves `contracts/wire/index.ts` + `responses.ts` carrying the ComparisonCatalogue
  wire on disk: `2.0.0_SA_COO~Y` (row S40); un-parks when ~Y lands the portal half or the CTO re-homes it.
- DEV CI red at ESLint on every push since 620ea953: row DSGN_IRPTV1-S41 -- `src/pages/SecurityAnalysis/components/HeaderBrief.tsx:47-48`
  carry a literal 0x08 byte in two regexes (DSGN_AMGTV1, site-Z `2.0.0_SA_COO~D`); un-parks when that seat lands the two-byte fix.
  This lane's four in-surface lint errors are gone at 1d7b8feb (item 37).
- 5174's process is detached from this session (PowerShell Start-Process, pid in the drive log); the next reboot
  kills it: this lane restarts it at the next tick that finds `/` unreachable.

## Limits

- The Generate press was exercised on the FIXTURE plane only (the walk-2 write guard); Andrew's live press is the
  acceptance. The history re-list after a press is one bounded read; a producer list that lags the issue shows the
  row on the next read.
- The CVO's grades of AF-1, AF-2 and item 36 are owed after the fact; nothing here waits on them.
