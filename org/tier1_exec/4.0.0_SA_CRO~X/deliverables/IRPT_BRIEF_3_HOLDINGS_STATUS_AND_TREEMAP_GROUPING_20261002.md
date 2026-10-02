# Brief 3 of 3 -- Investor Reporting HOLDINGS: status, and dropping the grouped "Smaller holdings" tile

**Author:** `4.0.0_SA_CRO~X`, 2026-10-02 ~15:3xZ. **For:** `1.0.0_SA_CTO`, to fold into the Holdings workstream
(`2.0.0_SA_COO~M` by Andrew's mapping; the map's code is `2.0.0_SA_COO~D`'s, section 2.4).
**Source of the ask:** Andrew-direct 2026-10-02 ~14:5xZ, record
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANDREW_DIRECT_20261002_145xZ_IRPT_THREE_SURFACES_STATUS_AND_THREE_BRIEFS.md`
@fc46925968, points H1 and H2. Siblings: brief 1 (Performance) and brief 2 (Analysis) in this folder.
**Claim words:** `measured` = read by this seat this session; `held` = cited from a record and not re-read.

Andrew, verbatim: "Finally, I want to move on to "Holdings", this one is virtually complete at this point. The only
thing I want to establish is that I dont think we need to use the "Smaller holdings" logic in the tree charts, that is
not necessary."

## 1. Status (H1): the surface is live; five small items remain

1.1 **Deployed route.** `irpt-holdings` CodeSha256 `tS/APci3Mz/YRDP7pJboAVqKabShek9jYUqvQDIYwwE=`, LastModified
    2026-10-01T20:13:14Z, timeout 29 s, 1024 MB (measured: `aws lambda get-function-configuration`, 15:2xZ). It is the
    `b26847ea04` build of row S259 (split accounts counted once), graded PASS on deployed bytes by `3.0.0_SA_CVO`
    @c10a133c7d: 35 of 35 members, 91 of 91 Inflection split accounts reconcile singly (held).
1.2 **Journey.** Live end to end at 49 Financial, Inflection and Cottonwood (held: `2.0.0_SA_COO~D` HARs 09-27; the
    Inflection selection read on the page 2026-10-01 12:11Z-12:19Z, 29 of 29 security aggregates tie). The scheduled
    publication proof H5 closed 2026-10-01 16:04Z (@3ed3f4ed9b: three firms' manifests advanced on the 14:15Z fire).
1.3 **Record lag.** `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~M.md` was last written 2026-10-01 06:5xZ and still names
    the earlier pin `TG8b/SEH..`. Today `2.0.0_SA_COO~M` is driving MDPF_SECCLASS (BD r3 re-land, @ac44b6aaaf).
1.4 **Remaining items** (all held from STATUS~M unless marked):
    (a) the CVO grade of the 10-01 pins `4e2feb5a32`, `cc99dea562`;
    (b) the -0.0 display fix @38b72bf469 rides the function's next move;
    (c) Cottonwood serves CEMIX (an equity fund) as fixed income on 67 nodes, 2,039,120.10 USD, until MDPF_SECCLASS
        round 7;
    (d) at 49 Financial 90.3 percent of custody (1,626,351,326.21 USD) has only a TARGET drill, so the remainder block
        is most of the page; a separately labelled TARGET fold is asked of `1.0.0_SA_CTO` with `2.0.0_SA_COO~D`;
    (e) the out-of-scope account answer (`NOT_FOUND` per PRD v0.22 ruling 22 vs `OBJECT_NOT_COVERED` in `_authz`).
    Of these, (d) is the only one a viewer at 49 Financial would notice first.
1.5 Row S262 (ten tracked `infra/aws/lambda/investor-reporting/holdings/` files deleted in the shared tree): the tree
    reads clean for that path now (measured: `git status --short`, 15:2xZ).

## 2. The change (H2): every security its own tile

2.1 **What exists** (measured, portal `origin/DEV` and `origin/PROD` both carry it; last change `20f95f79`, 09-30):
    `portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx`
    - `:265` `TOP_HOLDINGS_COUNT = 10`; `:400` `groupSmallIntoOther()` keeps the view's 10 largest securities and rolls
      the rest into ONE tile; `:485` it is the last step of `treemapLeavesFrom`.
    - `:252` `OTHER_TILE_LABEL = 'Other Securities'` (named "Smaller Holdings" until IV-e-114, "Various" before that);
      `:639` its legend entry; `:642` the footnote "groups every security outside the 10 largest".
2.2 **Whose word built it.** Andrew's own, three times: UIR-42 (a share threshold), W2-10, and 2026-09-30 ~01:4xZ
    ("showing the top 10 securities relative to the view ... with the remaining being 'Smaller Holdings'"). Today's
    word supersedes the 09-30 one on grouping. No other seat's ruling is in the way.
2.3 **Scope.** Only the Investor Reporting Securities map. The shared chart `src/components/holdings/HoldingsTreemapChart.tsx`
    has no grouping, so Positioning does not change. `DrillTree.tsx:123` `SMALL_SLICE_SHARE = 0.05` only moves a small
    pie wedge's LABEL to the legend; it hides no holding and is left alone unless Andrew names it.
2.4 **Who edits it.** All 17 commits to this file are DSGN_IRPTV1's: 10 by `2.0.0_SA_COO~D`, 7 by its workers
    `0.9.0_WK_DSGN_IRPTV1~<n>` (measured: `git -C portal log --format=%an`). Andrew mapped Holdings to
    `2.0.0_SA_COO~M`; the CTO routes. A product-file change is CTO-reviewed before DEV unless a live FAST lease covers it.
2.5 **The edit.** Drop the `groupSmallIntoOther` step; retire `TOP_HOLDINGS_COUNT`, `OTHER_TILE_*`, the legend entry and
    the footnote; re-golden the three tests that pin the grouping and its words
    (`__tests__/dsgn-irptv1/iv-e-44.securities-map.test.tsx`, `iv-e-105.treemap-various.test.ts`,
    `iv-e-114.securities-map-walk.test.tsx`). The security-identity merge (UIR-43, one tile per security) stays.
2.6 **What the viewer will see.** A large account shows many small tiles; those under `TreemapCell`'s 28x18 px floor carry
    no face text and are named by their tooltip. That is the expected look, not a reason to hold.

## 3. Outcomes for the fold-in (each is something a person can do)

- **H-1** On the Holdings tab, for any client and any chip selection, the Securities map shows every security in the view
  as its own tile; there is no "Other Securities" / "Smaller Holdings" tile, legend entry or footnote.
- **H-2** Hovering any tile, the smallest included, shows that security's name, class, weight and amount.
- **H-3** The tiles' weights sum to the selection's securities total: no security is dropped by the map.
- **Proof:** a signed-in walk on the DEV build (port 5174) at 49 Financial's largest client and one Cottonwood client:
  screenshots, and a DOM tile count equal to the count of distinct securities in that served snapshot.

## 4. What this brief does not claim

- It did not walk the page or run the portal tests; section 2 is read from source on `origin/DEV`.
- It does not re-measure items 1.4 (a)-(e); they are held from `STATUS~M.md` and the CVO grade.
