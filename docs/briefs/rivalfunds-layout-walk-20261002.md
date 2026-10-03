# /rivalfunds and Model Portfolios -- the layout walk of 2026-10-02 and its line items

**Author:** `4.0.0_SA_CRO~RV`. **Order:** Andrew-direct ~17:0xZ, recorded verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_17xxZ_RIVALFUNDS_LAYOUT_WALK_AND_BUILD.md`: walk the page,
list the line items, check whether a 2.0.0_SA_COO~RV agent already carries each one, and build the rest.

**Walked:**
- /rivalfunds, rendered READ-ONLY from S3 at the code under test (writes captured in memory, never sent), served on
  localhost:5180 and screenshotted, with each dialog opened;
- the portal's /portfolios (Model Portfolios) through `/ui-walk` on localhost:5174, with a hover step.

## Line items

| # | Andrew's ask | Who carries it | State |
|---|---|---|---|
| L1 | The header figures as nested cards with a hover explanation | not in round 6 (ui-1 only counts once) | built by CRO~RV: 4 cards, tooltip in the portal's indigo look, header no longer clips it |
| L2 | Peers and Period rows aligned and easy to read | not in round 6 | built by CRO~RV: one row per peer group plus the period row, fixed label column, 15px text |
| L3 | Default to YTD | ui-2 said "shortest period that ranks" | built by CRO~RV: YTD first and selected; COO~RV confirmed it supersedes ui-2 (msg 28598) |
| L4 | The buying trend's "By month" redesigned, labelled, readable at a glance | ui-3 made it a small unlabelled sparkline | built by CRO~RV: the face is holding / net with a bar / "Tilt, N trades"; the months move into the holding dialog, labelled Jan..Dec with bought / sold / no trade |
| L5 | A large popup on clicking a holding | not in round 6 | built by CRO~RV: one near-full-screen dialog per holding of the YTD rankings and the trend (contribution by period with its rank, the year's net buying, the labelled months) |
| L6 | AI analysis at the top, under the group card | not in round 6 (ui-4 kept it last) | built by CRO~RV |
| L7 | AI analysis easier to read, with a popup for full detail and citations | ui-4 put sources behind a details element | built by CRO~RV: the face is the badge plus two sentences at 16.5px; one dialog per account holds the full text, Observed, Inferred, the invalidation and the citations |
| L8 | Bigger text, progressive disclosure throughout | partly ui-1..ui-5 | built by CRO~RV: 15px base, larger captions and tags; the method, definitions and month record sit behind hovers and dialogs |
| L9 | Model Portfolios: the Models / SMAs / Client cards explain themselves on hover | no COO~RV cell (portal, outside ETFS_RIVALS) | built by CRO~RV on portal branch `cro-rv-mp-explain` (ac766035, 5a42f2df); landing waits on the CTO's product-file review |

## Evidence

- **rivalfunds** (CLOUD branch `cro-rv-layout2` @95af466e67, on CLOUD ae0d4e7082): the package suite reads 532 passed,
  3 skipped, 0 failed. The page for 2026-10-02 is 1,905,952 B against the 2 MiB gateway cap, with 387 holding dialogs and
  24 AI dialogs. `render_page` leaves the holding dialogs out above 1,950,000 B so a large day still publishes. There is no
  script on the page: dialogs use the native `popover`, hovers use CSS.
- **portal**: `bun run typecheck` (tsc -b) rc=0, with a mutant control rc=2. The ui-walk hover over the three cards shows
  the explanation with no occlusion. Investor Reporting is byte-identical: the prop is opt-in and only ModelPortfolios.tsx
  passes it.

## Found on the way (not Andrew's asks)

- **st-1 hid every AI account** (a second `A1_TABLES` at publish_page.py:252 shadowed :240). This was reported to COO~RV
  (msg at 17:40Z); it is fixed in CLOUD as `A1_PRODUCED`.
- **Five portal Investor Reporting guard tests fail on DEV already** (iv-e-109, iv-e-110, iv-e-111, iv-e-112 and iv-e-25).
  They pin ModelPortfolios.tsx to commits 72fe8393 / 8242412d, and the file changed after both (370d2fe8, MDPF_TAXSMA
  TX-c-3).
- **Weakest-sector ranks start at 2 on today's served tables** (Unclassified still holds rank 1 there). COO~RV's sx-1
  producer change removes it at the next deploy.

## Not done here

- **Deploy:** the page changes reach /rivalfunds at 2.0.0_SA_COO~RV's next Lambda deploy (Andrew-direct ~17:0xZ, item 1).
- **Walker option:** the walker's `--hover` option waits until 0.0.0_AB_MSTR~Z drains the laptop's walk.mjs change; the
  patch is held by this seat.
