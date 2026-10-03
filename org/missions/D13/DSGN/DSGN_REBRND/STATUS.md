# DSGN_REBRND -- status (FAST: /closer-drive under the lease)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md`. Reviewer
`3.0.0_SA_CVO` (grades each landed pin after the fact; round-2 grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_ROUND2_GRADE_20261001.md` @599d33a722). Authority: 1.0.0_SA_CTO RULINGS
batch 80 items 8-12 (the round-2 analysis; round 3 owed, this seat's, FAST, after the Investor Reporting work) and batch 165
@10d2b1c445 (msg 104234: round 3 un-parks now, every IR line being blocked outside this seat; its own `/positioning` lease;
IR keeps priority -- return to DSGN_IRPTV1 the tick any of its Next lines unblocks). **As of 2026-10-03T13:3xZ** (E4 done: DEV fe461611/44d6a215/b23917f7, rows S6-S8; E2: clause c9d303db and /positioning's page end 8526dacb on DEV; S10: d8d236a0 on DEV, row S12; Next 4b: 71a946e3, 4c: 46aeea17, Satellite 90 labels: fb5534f8, footer hour: cbfbb77a, W3-S4 /market: 55560835 + a7b16628 + 564a8f95, /positioning: b0b3c524, /attribution: 94c055e8, /portfolio-management: c3e1d7b9, /ticket-center: 3d8cce99, /data-refresh: 30f7fca1 on DEV).

## Pins

| What | Value |
|---|---|
| Lease | FAST `DSGN_REBRND` until 2026-10-02T14:10:34Z, armed 12:5xZ by this seat (`--by` batch 165): `portal/src/pages/Positioning/{Positioning.tsx, README.md, constants, index.ts, panels, shared, types.ts}`. NOT `Positioning/tabs/HoldingsTab.tsx` (the DSGN_IRPTV1 lease holds it; the arm's overlap refusal is the check) |
| Round | 3 (round 2 graded by the CVO 10-01: 4 of 10 outcomes REALIZED -- FWD-2, FWD-5, FWD-7, FWD-8; FWD-3, FWD-10, FWD-11, FWD-12 NOT REALIZED; FWD-4 partly evaluated; FWD-13 not evaluated; 5 remediation rows closed, 32 open) |
| Open task orders | 0 of 15 at the FULL -> FAST boundary (nothing to finish or supersede) |
| Working tree | the main portal checkout, branch DEV (shared with the DSGN_IRPTV1 lease, disjoint surfaces) |

## Write claims

- `2.0.0_SA_COO~D`: the `/positioning` page surface above. No claim open at 22:1xZ.

## Next (round 3's enrichment list, batch 80 item 9, in the ruled order; E4 started first by batch 165)

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
   - OWED: row W1-S11 (in the selected DARK mode no accent clears both white-on-accent and accent-on-band). It is
     this seat's to rule with a dark-mode table in hand; dark mode is not measured yet.
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
4. E3 -- the state census to zero, the no-permission and error states wired (rows W3-S5, W3-S1, W3-S4; FWD-11). W3-S1 LANDED portal `d7141e5a` (origin DEV, ls-remote 07:1xZ): a role-denied route renders PanelNoPermission and a way back (pin route-no-permission.test.tsx; real run looked at); disarmed by row S11. Parked: a partner firm outside its allowlist still redirects to its landing, by design (owner this seat; un-parks on a CTO ruling). W3-S4 PARTLY LANDED portal `55560835` (origin DEV, ls-remote 11:09Z): /market's Global RSI and Fear & Greed render LOADING then ERROR on a failed fetch, never a neutral 50 (the endpoint stopped fabricating one); pin `components/market-performance/__tests__/market-failed-fetch.test.tsx` with negative controls; real run with the two requests forced to 503 (ui-smoke `--fail`), HEAD drew 50s, the change draws both error states. /market's Daily Cloud, Trending Topics and Top/Bottom Performers LANDED portal `a7b16628` (origin DEV, ls-remote 11:30Z): ERROR on a failed fetch, one message per panel (C12), the keyword endpoint stopped returning an empty list; arms (d)-(f) in the same pin, negative controls on 55560835; real run under the live 401 and `--fail trending/latest`. The RSI hook's `?? 50` for a missing class LANDED portal `564a8f95` (origin DEV, ls-remote 11:44Z): a summary missing any class is no summary, so the panel says ERROR (fixture render: HEAD drew Commodities at 50; full summary still draws). W3-S4 OPEN for: a missing period change read as 0 (the marker sits on the bar, "(0.0)") and RSIModal's own `?? 50`/`|| 50`; the row's other route /advisor-intelligence (several files in 2.0.0_SA_COO~M's MDPF_SECCLASS lease), not re-measured. /data-refresh LANDED portal `30f7fca1` (origin DEV, ls-remote 13:33Z): History and Emergency Rollback say a failed history read (Rollback said "nothing to restore to"); 401 renders and a live walk `20261003T133002Z`. /ticket-center LANDED portal `3d8cce99` (origin DEV, ls-remote 13:16Z): a failed board load is one ERROR inside the board (Try again; the response body off the face), not "No open tickets." under a page-level error; 401 render and a live walk `20261003T131333Z` (served empty list kept). /portfolio-management LANDED portal `c3e1d7b9` (origin DEV, ls-remote 13:04Z): no 0.00 without a portfolio, one ERROR when the fund list or saved-session read fails; pin `PortfolioManagement/components/summary-states.test.tsx`; 401 render and a live walk `20261003T130059Z`. /attribution LANDED portal `94c055e8` (origin DEV, ls-remote 12:47Z): both panels ERROR on a failed read (the breakdown also LOADING while its read is in flight); pin `Attribution/components/style-policy-states.test.tsx`; real run from a build under the 401; live walk `20261003T124023Z`. CORRECTION to 94c055e8's message: the live breakdown shows 18 security rows, not 22. /positioning LANDED portal `b0b3c524` (origin DEV, ls-remote 12:11Z): a failed Models load is ERROR in all three panels (the Summary also shows LOADING now); re-measured on 564a8f95 first (blank summary, "No holdings for INT." twice); pin `Positioning/panels/summary-states.test.tsx`; the market pin's process-wide mocks are restored in afterAll. OPEN: W3-S5 (C12 form residue).
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
