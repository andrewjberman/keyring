# DSGN_REBRND -- status (FAST: /closer-drive under the lease)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md`. Reviewer
`3.0.0_SA_CVO` (grades each landed pin after the fact; round-2 grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND2_GRADE_20261001.md` @599d33a722). Authority: 1.0.0_SA_CTO RULINGS
batch 80 items 8-12 (the round-2 analysis; round 3 owed, this seat's, FAST, after the Investor Reporting work) and batch 165
@10d2b1c445 (msg 104234: round 3 un-parks now, every IR line being blocked outside this seat; its own `/positioning` lease;
IR keeps priority -- return to DSGN_IRPTV1 the tick any of its Next lines unblocks). **As of 2026-10-03T15:1xZ** (E4 done: DEV fe461611/44d6a215/b23917f7, rows S6-S8; E2: clause c9d303db and /positioning's page end 8526dacb on DEV; S10: d8d236a0 on DEV, row S12; Next 4b: 71a946e3, 4c: 46aeea17, Satellite 90 labels: fb5534f8, footer hour: cbfbb77a, W3-S4 /market: 55560835 + a7b16628 + 564a8f95, /positioning: b0b3c524, /attribution: 94c055e8, /portfolio-management: c3e1d7b9, /ticket-center: 3d8cce99, /data-refresh: 30f7fca1, /advisor-intelligence Advisors tab: 075d33fa, Data Source: 10fca02d, RSI period change: 1754d9c1, RSI modal: 4a40a0ff, /positioning notices: 6e31c220, Assets Overview: 1b8fccfd on DEV; row S14 disarms W3-S4; gate tests: e2563c17, 2da1eaaf, row S15 disarms S13).

## Pins

| What | Value |
|---|---|
| Lease | FAST `DSGN_REBRND` until 2026-10-02T14:10:34Z, armed 12:5xZ by this seat (`--by` batch 165): `portal/src/pages/Positioning/{Positioning.tsx, README.md, constants, index.ts, panels, shared, types.ts}`. NOT `Positioning/tabs/HoldingsTab.tsx` (the DSGN_IRPTV1 lease holds it; the arm's overlap refusal is the check) |
| Round | 3 (round 2 graded by the CVO 10-01: 4 of 10 outcomes REALIZED -- FWD-2, FWD-5, FWD-7, FWD-8; FWD-3, FWD-10, FWD-11, FWD-12 NOT REALIZED; FWD-4 partly evaluated; FWD-13 not evaluated; 5 remediation rows closed, 32 open) |
| Open task orders | 0 of 15 at the FULL -> FAST boundary (nothing to finish or supersede) |
| Working tree | the main portal checkout, branch DEV (shared with the DSGN_IRPTV1 lease, disjoint surfaces) |

## Write claims

- `2.0.0_SA_COO~D`: the `/positioning` page surface above. No claim open at 22:1xZ.

## Next -- ROUND 4 (1.0.0_SA_CTO round-3 analysis `ROUND_ANALYSIS_DSGN_REBRND_ROUND3_20261004.md` section 4 @cb2a26e675; PRD v0.14 @15576da1ee ADMITTED: both halves signed, the brief half by this seat at a322aef3fb, and the CTO's PRD LANDED notice was acked (msg 105014). v0.14's FWD-3 names the Global RSI bars only. Cut under the FAST lease, in this order)

R4-1. **FWD-11, PROD.** The ten DEV-only state fixes (`fb73cb1c`..`504e5379`) and StatusPanel `be349181` reach PROD on the next portal promote (0.0.0_AB_MSTR's, on Andrew's word; whole-bundle attribution). Asked of MSTR 2026-10-04 19:3xZ. The remaining bare spinners LANDED 2026-10-04 20:0xZ, portal DEV `7b053135` (ls-remote): App.tsx's route fallback and AdvisorPublicProfile's donut are PanelLoading; pin r4-1-remaining-spinners (census + ClientsTab control, DEV fails); ui-smoke --dist with /valuations' page chunk held, looked at; pin handed to the CVO. `AdvisorBookView.tsx:897` parked with 2.0.0_SA_COO~M (MDPF_SECCLASS surface). PROD half DONE: portal PROD c69b4747 (v2.1.199, a merge of DEV c7bc52c8; Deploy to Production 37231846084 success; 0.0.0_AB_MSTR 104959), so the ten state fixes and be349181 are on PROD for the CVO's outcome grade. 7b053135 (the last spinners) waits for the next promote.
R4-2. **FWD-10.** The page-end marker onto the remaining 24 routes; density measured with real data on each.
   - Batch 1 LANDED 2026-10-04 20:5xZ, portal DEV `97b7a6f2` (ls-remote): PageEnd shared (`ui/components/PageEnd.tsx`, /positioning re-exports it); /valuations and /correlations end on it with their own as-of. Census 3 of 25 routes. Pin page-end-batch1 (DEV fails); ui-smoke --dist with minimal fixtures, looked at. Density not yet measured.
   - Batch 2 LANDED 2026-10-04 21:3xZ, portal DEV `aa373a83` (ls-remote; 6142ae34 merged onto site Z's round-34 DEV): /attribution, /philosophy, /factor-tilts and /macro end on it, each naming its header title with its own as-of. Census 7 of 25. Pin page-end-batch2 (DEV fails); /attribution and /macro rendered, looked at.
   - Batch 3 LANDED 2026-10-04 22:0xZ, portal DEV `1b9f553d` (ls-remote; 57ac37d6 merged onto site Z's round-35 DEV): /market (with its as-of), /security-scanner, /data-refresh and /ticket-center end on it. Census 11 of 25. Pin page-end-batch3 (DEV fails); /market and /data-refresh rendered, looked at.
   - Batch 4 LANDED 2026-10-04 23:2xZ, portal DEV `3173c186` (ls-remote; 21e1aed7 merged onto site Z's 75efe9d6): /investor-reporting (dated by the accepted client's business date, undated with no client) and /advisor-intelligence (no page-level as-of) end on it. Census 13 of 25. Pin page-end-batch4 (DEV fails (a), (b), (c)); both rendered from dist, looked at.
   - Batch 5 LANDED 2026-10-05 00:0xZ, portal DEV `6936e92b` (ls-remote; 94f20376 merged onto site Z's c66d08f3): /portfolio-management (dated by the optimization in hand, YYYYMMDD or YYYY-MM-DD) and /trade-submission (no as-of) end on it. Census 15 of 25. Pin page-end-batch5 (DEV fails (a)-(d)); batches 2-4's control moved to /portfolios; both rendered from dist, looked at.
   - Left: /portfolios (parked: the MDPF_TAXSMA lease, 4.0.0_SA_CRO's; un-parks when that lease lapses or the CRO grants the one-line page end) and /security-analysis (parked: site Z, DSGN_AMGTV1; un-parks on site Z's word).
   - RULING (this seat, issuer, 2026-10-05 00:1xZ): the population. C10 binds "every page ... after its last panel", with only `<main>`'s bottom padding below it. App.tsx's 25 route paths (excluding "/" and "*") hold 18 content pages inside the shell's `<main>`. The other 7 are outside C10's population:
     - /login, /forgot-password, /reset-password and /change-password render outside `<main>` (App.tsx:596-602), and the PRD's Part II boundary leaves auth out of the commission;
     - /investor-reporting/print renders outside `<main>` (App.tsx:611); it is a printed document with its own footer, and Andrew's bundle-reference question is open on it;
     - /cma is a Navigate redirect and renders nothing (App.tsx:467);
     - /dev/page-surface-control is a component test fixture (`components/ui/__tests__/PageSurfaceControl.demo.tsx`), not a product page.

     The census is therefore 15 of 18, and the 3 left are the two parked routes above (/security-analysis has two paths).
   - Density part 1 LANDED 2026-10-05 01:4xZ, portal DEV `e2315890` (ls-remote; a3dc8427 + e2315890), pin page-end-spacing. The new `scripts/ui-smoke.mjs --density` line found:
     - /market's page end at 0px, outside its column (batch 3's defect);
     - eleven `space-y-6` columns, 24px;
     - /valuations and /correlations drawing no page end on a failed read.

     After: 15 of 15 page ends at 20px; failed and empty pages end too (never while loading); batches 3-5 census at least one page end.
   - Density part 2 LANDED 2026-10-05 03:3xZ, portal DEV `3e1aa46f` (ls-remote). The FWD-10 PROOF record is `deliverables/2.0.0_SA_COO~D/FWD10_PROOF_20261005.md`:
     - before (fb6f5023) vs after on /market, /positioning and /portfolio-management with the named populated fixtures (new: `r4-2-portfolio-management.json`), plus the rb-s-9-sparse control;
     - before: 24 inside = 24 between, and no end state; after: 30 inside, 20 between, and a 20px dated page end on all four;
     - fixed in this part: /positioning's pt-6 panel top and /portfolio-management's header mb-6;
     - pin density-part2 (DEV fails).
   - R4-2 remaining: /portfolios and /security-analysis page ends (parked with their holders); the CVO's FWD-10 grade.
   - Next: R4-3 (FWD-13).
R4-3 part 1 LANDED 2026-10-05 06:0xZ, portal DEV `99c6ae08`.
   - Instrument `ui-smoke.mjs --state-table`. As-is: 63 declared pairs, 13 below the bar: every disabled state, and the dark hover/selected rung under navy on light. The white-overlay hover is invisible on light.
   - To-be `src/ui/tokens/state-table.json`: 54 declared, 0 below the bar.
   - Eight opaque `--state-*` rungs in index.css. Controls' disabled state is off opacity, and `rowStateClass(world)` (rowState.ts) serves rows.
   - Census instrument `scripts/state-census.mjs` (590 files; state tokens 0). Pin state-table.test.ts.
R4-3 part 2 LANDED 2026-10-05 07:1xZ, portal DEV `0edab95f` (ls-remote).
   - Instrument `ui-smoke.mjs --hover-walk`: rest and hover pairs per distinct clickable element; image grounds are counted, not graded.
   - Before: 54 elements over 15 routes, 4 below 4.5:1 (/market Expand 3.62; PM AlphaTab headers 3.77; TS Reset 3.13 / 2.83 on hover).
   - After: danger state rungs in the shared Button; band secondary ink `--palette-mediumGray` replacing text-white/40 in ExecutiveSummary, FearGreedModal and AlphaTab.
   - Re-walk: 0 below; table 63 declared, 0 below. Pin state-part2.
   - The semantic-hover light-world FAIL in the as-is table is LATENT: all 17 sites sit on band grounds, and the 3 shared constants in ui/styles/interactive.ts have no importer.
   - Next, R4-3 part 3: the translucent state GROUNDS. Every rendered pair now passes contrast, but FWD-13's constraint requires an opaque rung: hover:bg-white/N is about 215 occurrences (white/10 121, /5 54, /20 22, /15 13, /8 5), and there are 140 ternary grounds. They move onto --state-hover-band / --state-selected-band / rowStateClass, by file, worst first, each re-censused and re-walked.
   - Still owed for the PROOF: a hover render per delivered page. That starts with the 17 `semantic-background-hover` sites on light grounds and the white-overlay hovers that land on light panels, each page re-censused, with a highlighted element walked on the band and on a light panel. The three IV.9 routes (/market, /positioning, /portfolio-management) are rendered at 1440x900 with the named populated fixtures: `.frontend-dev/testing/rb-s-9-market.json`, `rb-s-9-attribution.json` (it carries positioning data), and a new /portfolio-management fixture. For each, print the viewport share below the last content before and after, plus C10's 30px inside / 20px between measured on the render. `rb-s-9-sparse.json` is the negative control.
R4-3. **FWD-13.** One per-role state table (rest, hover, selected, focused, disabled); walk light panels, not dark only; close row S9 (the OS dark-mode setting) on PROD.
R4-4. **FWD-12.** A layer table covering light and dark; the layer values into the one token file and the contract.
R4-5. **FWD-6.** The contract gains value labels, the layer table (R4-4) and the state clause; then one page rejected by clause, its author agreeing.
R4-6. **FWD-3.** A census of every ordered scale in `portal/src/`, denominator printed, the three named exceptions listed (RULING R carries Global RSI).
R4-7. **FWD-4.** The accent's pixel share measured and the counterexample walk; close the accent "Neutral" label row.
R4-8. **FWD-1.** The site-to-portal walk by someone new to the portal: needs a person; this seat names who when it is reached.
R4-9. **FWD-9.** Andrew's side-by-side with an institutional competitor: his act, listed for him, not built.
Housekeeping (not cut): 3.0.0_SA_CVO compiles the closing rows (S6-S8, S11, S12, S14, S15, with S9, S10, S13) and grades 207728cced and 91c6cbb6d2 at the next L8. Closure is Andrew's word.

## Round 3 (done; kept for its record)


00. **W3-S5 /philosophy Views (2026-10-03 21:3xZ):** BUILT `fb73cb1c` in worktree `portal-coo-d-holdings`.
    - A failed views read is ERROR, a pending one LOADING, and no views is EMPTY; before, a failed read spun forever.
    - Pin views-states; DEV's page fails it.
    - Real run on a build with views.json forced to fail, looked at.
    - LANDED portal DEV `822ce891` (ls-remote 22:0xZ) with cbf41e6e and 3e526a44, after PROMOTED (104785).
000. **W3-S5 raw JSON bodies in Cause lines (2026-10-03 21:5xZ):** BUILT `3e526a44` in worktree
    `portal-coo-d-holdings`.
    - `innermostCause` (the one helper behind every designed ERROR state's Cause line) replaces an interpolated JSON
      body with its `error`, `message` or `detail` words; other text comes back unchanged.
    - Pin raw-cause (the helper plus the real /market page); DEV's cause.ts fails it.
    - Real run: /valuations with its data read forced to a 503 JSON body reads "... - ui-smoke forced failure"; the
      same render of a DEV-cause build reads `... - {"error":"ui-smoke forced failure"}`.
    - LANDED portal DEV `822ce891` (ls-remote 22:0xZ), after PROMOTED (104785). The CVO was handed the pins (23:08Z).
0. **The CVO's census after S14 (grade b296ae47c1): the remaining `?? 50` sites.** LANDED 2026-10-03 18:4xZ:
   portal `7b265fc4` (origin DEV, push output 2f326afc..7b265fc4), after B2 was PROMOTED (PROD 98a98e70fb, 104690).
   It carries 3a842221, a6a77e31, 6cb31b54 and cc1d7cc6; the CVO was handed the pins. BUILT 16:3xZ.
   - Commit `3a842221` on the local branch `coo-d-regime-readings`, worktree `C:/Users/AndrewBerman/Desktop/portal-coo-d-regime`.
   - Covers MarketRegimeIndicator, MarketRegimeModal and FearGreedModal: a missing reading says "Not published", never
     50. Pin regime-no-reading, with four negative controls.
   - Real run: a build served with gap and control fixtures, looked at.
   - HELD off DEV until B2 (the P-2 window's PROD promote, CTO 104632) is measured: B2 carries DEV head, and this
     change is not graded yet. It lands on DEV after B2.
   - The same grade's untested wiring is BUILT on the same branch, `a6a77e31`:
     - Positioning `loadFailed` and HoldingsTab's fetch failure, through the pages (wiring-states);
     - MarketPerformance `failed`, through the page (failed-wiring).
     Each arm fails on its mutant. Held with the branch.
   - W3-S5's auth item is BUILT on the same branch, `6cb31b54`.
     - The six auth form errors (login, change/forgot/reset password, both MFA steps) are one compact PanelError.
     - The invalid reset link's pink circle is gone.
     - Pin auth/error-state: the DEV files fail every arm.
     - Real run on a build: a forced forgot-password failure and the invalid link, looked at.
     - Held with the branch.
   - W3-S5's /factor-tilts item is BUILT on the same branch, `cc1d7cc6`.
     - A failed or empty load is said once, by the overview; the tabs are not drawn under it.
     - Pin one-state: the DEV page fails it, with each sentence twice under the tabs.
     - Real run on a build under the 401, looked at.
     - Held with the branch.

1. **E4 -- the page pass for FWD-12 and FWD-13 on `/positioning`** (first by batch 165). SURFACE HALF (FWD-12) LANDED:
   - portal fb5d6116: the Positioning Summary's six translucent fills on opaque rungs (bar tracks, placeholder and
     inputs: tile; the blend strip: body; the Collapse button: tile, hover rung on hover);
   - portal fe461611: the Holdings Breakdown's subtotal rows on the tile rung and grand-total rows on the selected rung,
     in the shared table and HoldingsTab's extra cells.
   Origin DEV fe461611, ls-remote 22:1xZ. After-walks: `tmp/ui-walk/20261002T214636Z` and `20261002T220333Z` against
   baseline `20261002T130259Z` (local). Hairlines are enumerated in fb5d6116's message and left as the band's light rule
   idiom.
   FWD-13 HALF LANDED for /positioning (portal DEV 44d6a215, ls-remote 00:0xZ):
   - The instrument is the walker's `--contrast-table`. Walk 20261003T000242Z graded 316 interactive text pairs (Models
     Portfolio and Custom, ETFs, Satellites), 0 under their bar.
   - Fixes (portal 661e49b3 + 44d6a215):
     - the AGG chip takes indigo400;
     - a highlighted book name keeps its colour and takes the band as its own ground;
     - the satellite ramp blends in OKLab (same stops and order; Models and ETFs unchanged).
   - RULING on row W2-S8 (this seat, CORRECTED in 44d6a215 after 661e49b3 removed the hover colour against Andrew's
     2026-09-15 word): the locked canon hex stays the hover ink, and the hover state supplies a ground (the band)
     on which every canon hex clears 4.5:1.
   - RULED: row W1-S11 (in the selected DARK mode no accent clears both white-on-accent and accent-on-band), by row
     DSGN_REBRND-S7 (this seat, 2026-10-03 00:25Z): the conflict is latent, since no code path selects dark mode, and
     splitting the accent into a fill token and an ink token is the precondition of shipping a dark-mode toggle. A
     dark-mode table cannot be read until such a toggle exists. Re-read 2026-10-04 03:1xZ: the walker has no dark-mode
     switch and the portal source still selects none. E4 is complete.
   The original text follows: every surface on the page resolves to a
   role of the one named-layer table (page, section strip, panel body, tile, inset, hover, selected, tooltip) with an opaque
   rung in both worlds; every interactive role's (ground, ink) state pairs clear the contrast bar in the state it is actually
   in. Measure first (the page rendered on 5174 and read), then fix in the surface. The two contrast rulings that bound
   FWD-13 (rows W2-S8, W1-S11) are this seat's, made with the contrast table in hand (batch 80 item 10).
2. ~~E1 -- the Global RSI bands onto one hue (row S3; FWD-3)~~ CLOSED: 1.0.0_SA_CTO RULED NO (batch 215, msg 104568). Andrew's 2026-09-14 word on the sibling Fear & Greed gauge ("Blue Gradient, that is not necessary") governs the RSI bars. Row S3 is superseded; the built patch stays archived at `deliverables/2.0.0_SA_COO~D/e1/` and is never applied. The 06:18Z card was dropped by the CTO's word. Parked, outside E1: the 70D/90D marker labels overlap the Global RSI bars (owner 2.0.0_SA_COO~D DSGN_REBRND; un-parks with a /market layout item).
3. ~~E2 -- the page-terminator clause in `portal/DESIGN.md` (row W1-S29; FWD-10)~~ WRITTEN: DESIGN.md C10 gains the PAGE END
   (portal c9d303db on DEV after PROMOTED 104493; lease re-armed with portal/DESIGN.md). /positioning ADOPTED it (portal 8526dacb,
   origin DEV): shared/PageEnd.tsx after the Holdings section. Signed-in walk 20261003T013711Z reads "End of Positioning. Data as
   of October 1st, 2026, 5:00p ET.", the footers' own format, with no format:dates finding. The clause names `typography.footnote`.
   Other routes adopt it in their own cells.
4. E3 -- the state census to zero, the no-permission and error states wired (rows W3-S5, W3-S1, W3-S4; FWD-11). W3-S1 LANDED portal `d7141e5a` (origin DEV, ls-remote 07:1xZ): a role-denied route renders PanelNoPermission and a way back (pin route-no-permission.test.tsx; real run looked at); disarmed by row S11. Parked: a partner firm outside its allowlist still redirects to its landing, by design (owner this seat; un-parks on a CTO ruling). W3-S4 PARTLY LANDED portal `55560835` (origin DEV, ls-remote 11:09Z): /market's Global RSI and Fear & Greed render LOADING then ERROR on a failed fetch, never a neutral 50 (the endpoint stopped fabricating one); pin `components/market-performance/__tests__/market-failed-fetch.test.tsx` with negative controls; real run with the two requests forced to 503 (ui-smoke `--fail`), HEAD drew 50s, the change draws both error states. /market's Daily Cloud, Trending Topics and Top/Bottom Performers LANDED portal `a7b16628` (origin DEV, ls-remote 11:30Z): ERROR on a failed fetch, one message per panel (C12), the keyword endpoint stopped returning an empty list; arms (d)-(f) in the same pin, negative controls on 55560835; real run under the live 401 and `--fail trending/latest`. The RSI hook's `?? 50` for a missing class LANDED portal `564a8f95` (origin DEV, ls-remote 11:44Z): a summary missing any class is no summary, so the panel says ERROR (fixture render: HEAD drew Commodities at 50; full summary still draws). A missing period change read as 0 LANDED portal `1754d9c1` (origin DEV, ls-remote 14:06Z): null, so no marker and "not published" in the tooltip (fixture render before/after). RSIModal's own `?? 50`/`|| 50` LANDED portal `4a40a0ff` (origin DEV, ls-remote 14:29Z): a missing reading is "Not published", a real 0 stays 0 (driver render before/after). W3-S4 on /market: none open; Row S13 (3.0.0_SA_CVO: d7141e5a broke F49-AC4) DISARMED by row S15: portal `e2563c17` + `2da1eaaf` (origin DEV, ls-remote 15:09Z), the second fixing F47-AC6, which this seat's b618efc9 had broken; the seven committed-blob suites 45 of 45 after commit. W3-S4 DISARMED by row S14 (every named route; Assets Overview LANDED portal `1b8fccfd`, origin DEV, ls-remote 14:51Z, the file released by 2.0.0_SA_COO~M). /advisor-intelligence: Advisors tab LANDED portal `075d33fa` (origin DEV, ls-remote 13:46Z), one ERROR for a failed leaderboard read; OPEN there: Assets Overview's EMPTY words on a failed read (`_shared/components/PartnerAnalytics.tsx:1153`, released by 2.0.0_SA_COO~M at 14:34Z (104623); ~M 104617: this seat takes it, landing once that lease reads FULL -- it read FAST to 14:27Z at 13:57Z). The Data Source panel's static "Connected" LANDED portal `10fca02d` (origin DEV, ls-remote 13:57Z): claimed only once data arrived, all four partner pages (49 Financial rendered both ways; the rest by typecheck). /data-refresh LANDED portal `30f7fca1` (origin DEV, ls-remote 13:33Z): History and Emergency Rollback say a failed history read (Rollback said "nothing to restore to"); 401 renders and a live walk `20261003T133002Z`. /ticket-center LANDED portal `3d8cce99` (origin DEV, ls-remote 13:16Z): a failed board load is one ERROR inside the board (Try again; the response body off the face), not "No open tickets." under a page-level error; 401 render and a live walk `20261003T131333Z` (served empty list kept). /portfolio-management LANDED portal `c3e1d7b9` (origin DEV, ls-remote 13:04Z): no 0.00 without a portfolio, one ERROR when the fund list or saved-session read fails; pin `PortfolioManagement/components/summary-states.test.tsx`; 401 render and a live walk `20261003T130059Z`. /attribution LANDED portal `94c055e8` (origin DEV, ls-remote 12:47Z): both panels ERROR on a failed read (the breakdown also LOADING while its read is in flight); pin `Attribution/components/style-policy-states.test.tsx`; real run from a build under the 401; live walk `20261003T124023Z`. CORRECTION to 94c055e8's message: the live breakdown shows 18 security rows, not 22. /positioning LANDED portal `b0b3c524` (origin DEV, ls-remote 12:11Z): a failed Models load is ERROR in all three panels (the Summary also shows LOADING now); re-measured on 564a8f95 first (blank summary, "No holdings for INT." twice); pin `Positioning/panels/summary-states.test.tsx`; the market pin's process-wide mocks are restored in afterAll. W3-S5 (C12 form residue) PARTLY LANDED portal `6e31c220` (origin DEV, ls-remote 14:40Z): /positioning's six tinted notices (the row's "red-on-pink banner (/positioning ETFs)") are PanelError / PanelEmpty; 401 renders of ETFs and Satellites. W3-S5 ON THIS SEAT'S SURFACE: DONE 2026-10-04 03:0xZ (the demo page's silver copy was already gone, portal `201bfe69`; DEV source holds no "silver page"). PARKED, each with its owner: /portfolios' spinners and CORS note (MDPF_TAXSMA's lease); /advisor-intelligence's ClientsTab and AdvisorBookView (MDPF_SECCLASS, 2.0.0_SA_COO~M); StatusPanel's verbatim reason code LANDED 2026-10-04 18:5xZ under CTO batch 238 (ruling T reconciled), portal DEV `be349181` (ls-remote), pin status-panel-reason-code, signed-in real run looked at. Was: bare spinners and plain "Loading..." lines on /portfolios (parked under MDPF_TAXSMA's lease); /login LANDED 2026-10-04 02:3xZ, portal DEV `504e5379` (ls-remote): LoadingOverlay (the sign-in check on /login and every protected page) is PanelLoading on a panel, pin sign-in-check-loading (DEV fails), ui-smoke --dist with auth/refresh held, looked at; the auth pages' button spinners are busy indicators and stay; /advisor-intelligence's ClientsTab (4) and AdvisorBookView sit under MDPF_SECCLASS's surface (parked, owner 2.0.0_SA_COO~M, un-parks when that surface is released). LANDED 2026-10-04 02:2xZ, portal DEV `d8b81b65` (ls-remote): /advisor-intelligence's partner pages, Advisors, Assets Overview (panel and chart) and Distribution's four chart loads are PanelLoading; pin advisor-loading-states (render arms + census, DEV fails); ui-smoke --dist with the advisor reads held, looked at; pin handed to the CVO. LANDED 2026-10-04 01:5xZ, portal DEV `a9b7427e` (ls-remote): /security-scanner's Factor Bank, Universe Scanner and Universe Data tabs load as PanelLoading (each drew a grey "Loading ... data..." line on navy); pin scanner-loading-states (DEV fails all three arms); ui-smoke --dist with the factor read held, looked at; pin handed to the CVO. LANDED 2026-10-04 01:3xZ, portal DEV `a403f466` (ls-remote): /data-refresh's amber band (Current Portal State's failed read) is PanelError with a retry, and that panel and Upload History load as PanelLoading; pin data-refresh-states (DEV fails every arm); ui-smoke --dist with manifest.json forced to a 503, looked at; pin handed to the CVO. LANDED 2026-10-04 01:1xZ, portal DEV `c35c66db` (ls-remote): /investor-reporting's request list and export preview (`8071b59b`, pin request-list-states, signed-in walk `20261004T010454Z` shows the list's LOADING); /valuations' page loading and Risk Premium failure (`e2f89bd9`) and its Range panel's developer text (`7a12098c`), pin valuation-states; /correlations' loading and its one-ticker dead end (`c35c66db`, the selectors lived in the panel the notice replaced), pin correlation-states; real runs via ui-smoke --dist (held reads, forced failures, minimal fixtures), looked at; pins handed to the CVO. IR-REQUEST-FAILED on /investor-reporting NARROWED 2026-10-04 00:2xZ: the named render (scope read failed) now draws one designed error panel and no code (ui-smoke --dist --fail directory/resolve, looked at); the residue is StatusPanel printing any reason code verbatim on a tab read that does not complete, which is CTO ruling T (FE-s-40) -- PARKED, owner 1.0.0_SA_CTO, un-parks on a ruling that reconciles T with AD-09/AD-15 (codes behind Technical details); /factor-tilts' repeated error; the auth pages' three idioms; /philosophy Views blank; raw JSON Cause lines; the /portfolios CORS note; the demo page's silver copy.
4a. Rows S9 and S10 (3.0.0_SA_CVO 2026-10-03T01:30Z, owner this seat). ~~S10~~ LANDED portal `d8d236a0` (origin DEV, ls-remote 09:11Z), disarmed by row S12: `chartColors.getAssetClassInkOnDark` gives Equity blue400 (5.89:1) and Structured pink400 (5.65:1) as text on the body rung; the bars keep the class colour; pin `Positioning/panels/class-label-ink.test.ts`. The walk's `--contrast-table` now also grades non-interactive text at rest (CLOUD `.claude/skills/ui-walk/walk.mjs`, state `text`, grouped, hints only). OPEN: S9, Tailwind's `dark:` variant follows prefers-color-scheme in 23 catalyst files (declare `@custom-variant dark` on the app's own switch, or render and grade the modals).
4b. ~~The widened limb's first read of /positioning~~ LANDED portal `71a946e3` (origin DEV, ls-remote 09:48Z). The probe
   (walk `20261003T092442Z`, location hints) placed the four groups: the panel footer's source words (TEXT.metadata
   white/40, 3.78:1) and separator (white/30, 2.65:1) on the band; the page's white/40 labels (3.63:1) on the body rung; and
   46 treemap tile labels read at 1.18:1 only because the limb took the panel behind an SVG tile as their ground (an
   instrument fault: the walker now reads a foreignObject's sibling `rect` fill, and skips clipped text). Fix: the band
   secondary ink `--palette-mediumGray` in `ui/components/panels/PanelFooter.tsx` (8.14:1, every page's footer) and the
   eight white/40 sites on /positioning (6.87:1 body, 5.65:1 tile); pin `Positioning/panels/secondary-ink.test.tsx`.
   After-walk `20261003T094015Z`: 105 pairs, 0 under their bar. The lease gained `PanelFooter.tsx` and dropped
   `AdvisorIntelligence/_shared/AdvisorBookView.tsx` (2.0.0_SA_COO~M's MDPF_SECCLASS lease holds it). NOT walked yet with
   the widened limb: the expanded details, the other routes (ETFs and Satellites: 4c).
4c. ~~The ETFs and Satellites views with the widened limb~~ WALKED and LANDED portal `46aeea17` (origin DEV, ls-remote
   10:10Z). Walk `20261003T095441Z`: ETFs 86 pairs and Satellites 112 pairs, 0 under their bar. One `format:dates`
   finding: the Satellites footers wrote "holdings as of 2026-10-03" beside the page end's long form; both now go
   through formatPanelTimestamp (pin `Positioning/panels/footer-date-format.test.ts`; after-walk `20261003T100559Z` has
   no date finding). The walker's older `design:contrast` check had the same SVG-tile blind spot (32-60 false hits per
   view); fixed in walk.mjs. Parked from this walk, owner this seat:
   - ~~the footer hour depends on the viewer's zone~~ LANDED portal `cbfbb77a` (origin DEV, ls-remote 10:46Z):
     `dateUtils.create5pmETDate` asks America/New_York (through Intl) whether the date is under EDT. Pin
     `lib/__tests__/create5pm-et.test.ts` (UTC runner; summer, winter, both changeover days; fails on HEAD). Real run in a
     UTC browser (walker `--tz UTC`): the page end read "6:00p ET" under a "5:00p ET" footer before (walk
     `20261003T104156Z`), both "5:00p ET" after (`20261003T104339Z`). The lease gained `src/lib/dateUtils.ts` and the pin;
   - ~~Satellite 90's percentage labels run past the Summary's right edge at 1440px~~ LANDED portal `fb5534f8` (origin
     DEV, ls-remote 10:31Z): in the compact layout (>= 6 books) the labels sit in flow beside the bar in a fixed slot;
     the five-book arm is byte-identical. The walker's new `layout:clipped` check measured 3 labels cut by 9px on the
     HEAD layout (walk `20261003T101902Z`) and none after (`20261003T102244Z`); pin `compact-labels.test.ts`. Not
     measured under 1440px: eight books fit from about 1200px of panel width, and scroll sideways below that;
   - the walker's old contrast check reads a CSS gradient/background-image header (the satellite dialog) as white: 4
     false hits per dialog. Un-parks with the next walker edit.
5. ~~E5 -- the two project checkers that read red on the accepted tree (the grade's Q2)~~ LANDED 06:5xZ (CLOUD, LOCAL). `task-orders/rb4-ramp-check.py` grades the portal-wide sentiment tokens and prints the /market `[data-sentiment-original]` block as EXCEPTED (Andrew-direct 2026-09-14; CTO batch 215): ONE-HUE-RAMPED on the accepted tree, and RAINBOW-REMAINS on a control with one rainbow token put back portal-wide. `rb7-contract-check.py` run bare grades both arms: CONTRACT-CARRIED; CONTRACT-MISSING on an absent file.
6. ~~E6 -- the old law in the `/frontend-dev` skill and the "silver" mentions (Q4, rows W2-S15, W1-S24)~~ LANDED: the skill at CLOUD 91c6cbb6d2 (LOCAL); the canvas comments in 28 portal files at portal `201bfe69` (origin DEV, ls-remote 06:4xZ). Left by reading each: the data tier, the Silver commodity, the brand palette's named silver, and Panel.tsx's history. Parked: renaming the `PRIMARY_ON_SILVER_DROPDOWN_CLASS` export (a code change across its importers and tests; owner 2.0.0_SA_COO~D, un-parks with any edit to PageSurfaceControl).

Each of E1-E3, E5 and E6 needs its own surface in the lease (a re-arm), outside today's `/positioning` arm.

## Open at Andrew

- FWD-9 (Andrew's own side-by-side) and FWD-1 (a walk by a person new to the portal) are person acts, unchanged.
- PRD v0.11 (batch 80 item 11: FWD-3's PROOF sentence against Andrew's 09-11 word that the ladder's five hues are canon) is an
  ENDPOINT change, both halves re-signed; it rides the round's FULL cut, not this FAST lease.

## Limits

- FAST never lowers a `<risk>` class; this lease touches the portal bundle only (DEV; PROD is Andrew's promote).
- Investor Reporting keeps priority (batch 165): a DSGN_IRPTV1 Next line that unblocks pre-empts this round.
