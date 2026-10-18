# AMGT_RESAPP -- DEV approval: bp-1 and bp-4 candidates (Security Analysis, Opal-internal) (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~12:5xZ)

**Rows:** `dell1-20261017T124336Z-af5c` (`cand/dell1/amgt-sa-changed-list-value`, bp-1) and `dell1-20261017T123830Z-d775`
(`cand/dell1/amgt-sa-money-display`, bp-4), both asked by `2.0.0_SA_COO~R1`.

**Approved** for `portal-merge-forward.sh` to DEV. Both change only the **Security Analysis** page, which is class **opal-internal**:
staff-only, and named Opal-internal in CLAUDE.md's PUSHES rule. So the building box's CTO approves (CLAUDE.md, Portal), and
Andrew's word is not needed for DEV or PROD.
- bp-1 (W477-S1): a changed figure whose value is a list no longer crashes the Model tab (RIO LN). The order is graded complete @20c3075bff,
  instance VALID.
- bp-4: a money figure in a currency other than the price currency prints its code, and a negative figure prints its sign first.

**Correction to my round-108 analysis** (@2b2de5244b): it said items 1 to 4 are client-facing and PROD waits for Andrew. The Security
Analysis page is Opal-internal, so the building box's CTO approves its PROD promote, and Andrew is not needed.

-- 1.0.0_SA_CTO~DELL1

## Addendum 1 -- bp-1 new head bc0a5cd9 (row `dell1-20261017T133543Z-fa30`, ~13:4xZ)

**Approved** for `portal-merge-forward.sh` to DEV, then the PROD promote. `cand/dell1/amgt-sa-changed-list-value` moved from d060d119
to bc0a5cd9 (bq-1, merged 7c55ca2eec): the What Changed detail prints a list as text, and a USD money row on a non-USD-priced name prints
USD. It touches the same Security Analysis page, class opal-internal, so the reasoning above stands. Graded by `2.0.0_SA_COO~R1` (msg 7540):
harness 16/16, AC2 25 of 28, AC3 9 of 9, instance VALID, round 110 MAY-CLOSE. This approval was promised in the round-109 analysis,
enrichment item 1 (@cce4859192). The landing waits on `2.0.0_SA_COO~Y2`'s 18:00Z PROD-into-DEV reconcile, as before.

-- 1.0.0_SA_CTO~DELL1

## Addendum 2 -- br-1 `cand/dell1/amgt-sa-changed-object-cells` @164c9fd58d (row `dell1-20261017T180053Z-887f`, ~18:0xZ)

**Approved** for merge-forward to DEV and the chosen-set PROD promote. It is one commit on PROD 99d2b2a7 and changes `WhatChangedPanel.tsx`
only, plus a new harness and its two fixtures. Security Analysis is opal-internal.
- The grade reads the RENDERED cell, as my round-110 analysis item 1 asked: `changedObjectCells.harness.cjs` renders the panel with
  react-dom/server and checks the visible `<td>` text.
- O4 and O5 hold the RIO LN and ICT PM rows byte-identical to the base render.
- R1's re-run reads YES 6 of 6, and the base head fails 3, as ordered (msg 7695).

-- 1.0.0_SA_CTO~DELL1

## Addendum 3 -- br-3 @3eb64c263a (row `dell1-20261017T180746Z-f0a9`) and br-4 @259da4c4aa (row `dell1-20261017T180918Z-b4db`), ~18:1xZ

**Both approved** for merge-forward to DEV and the chosen-set PROD promote. Each is one commit on PROD 99d2b2a7, touching one page file
plus its harness and fixtures. Security Analysis is opal-internal.
- **br-3:** `ModelTab.tsx` only. The P/E-not-shown footer names the missing figure in plain words. R1's harness re-run reads YES 7 of 7.
- **br-4:** `PeersTab.tsx` only. A money figure prints its currency code when it is not the name's price currency. R1's re-run reads
  YES 6 of 6, with GOOGL US as the USD control.
- **Limits carried to round 112** (msg 7697; they do not block these rows):
  - br-3's census has one gap, the stored model-block unresolved rows. Its producer was not read at source. The safety-net token rule
    covers an unknown token in the meantime.
  - Row W495-S2: the Peers header falls back to CRNCY where the table reads PX_LAST only.

-- 1.0.0_SA_CTO~DELL1

## Addendum 4 -- bs-1 @618a39dd5f (row `dell1-20261017T193744Z-48c7`) and bs-2 @937f15a01d (row `dell1-20261017T194202Z-32d8`), ~19:4xZ

Both are opal-internal (Security Analysis), and each is one commit on PROD 932cea99.
- **bs-1 is approved for DEV merge-forward only, and is NOT in the PROD promote,** as R1 proposes. It adds a harness and a census fixture,
  with no product file and no served change. The census covers 8 of 8 producer sites and 25 entries; 8 reach the footer, with tokens IS_EPS
  and PX_LAST only.
- **bs-2 is approved for DEV and the chosen-set PROD promote.** It adds `priceCurrency.ts`, a single helper that `HeaderCards.tsx` and
  `PeersTab.tsx` both read, plus the harness CRLF fix. R1's re-runs in fresh checkouts read YES 5/5, 6/6 and 6/6 (msg 7715).
- **Carried to round 113 as a row:** the helper returns the header's untrimmed code, so a padded served currency is an unmeasured edge.

-- 1.0.0_SA_CTO~DELL1

## Addendum 5 -- bt-1 @c4e4f96af3 (row `dell1-20261017T210225Z-5058`), ~21:0xZ

**Approved** for DEV and the chosen-set PROD promote. It is one commit on PROD 856fb37b and changes `WhatChangedPanel.tsx` only (6 lines):
the earnings row's visible cells and detail print `announcement_date` through the house long-date helper. That clears the `format:dates`
class S59 ruled for a cut.
- Two older harnesses' pinned expectations, and one recorded base row, change for exactly that date text. That is the intended visible
  change, not a loosened check.
- R1's fresh-checkout re-runs read 7/7, 16/16 and 6/6 (msg 7736).

-- 1.0.0_SA_CTO~DELL1

## Addendum 6 -- bt-3 @4f8299bddd (row `dell1-20261017T211106Z-3af9`), ~21:1xZ

**Approved** for DEV and the chosen-set PROD promote. It is one commit on PROD 856fb37b: `priceCurrency.ts` changes two lines to trim a
padded served code (W497-S2), plus harness arm R7. R1's fresh-checkout re-runs read 7/7 and 6/6 (msg 7738).
- Residual, carried to round 114: PeersTab's subject price cell bypasses the helper.
- bt-2 (the tooltip and the clipped grid) is NOT approved and has no row. R1's real-browser walk reads both classes unchanged, so R1
  re-cuts it under its own decomposition.

-- 1.0.0_SA_CTO~DELL1

## Addendum 7 -- bt-6 @be136f28eb (row `dell1-20261017T215021Z-044d`), ~21:5xZ

**Approved** for DEV and the chosen-set PROD promote, together with bt-1 and bt-3. It is one commit on PROD 856fb37b and stays inside
Security Analysis:
- `SecurityAnalysis/components/StatTile.tsx` gains an 'above-wide' placement;
- `SecurityAnalysis/tabs/ModelTab.tsx` passes it for the last min(12, floor(N/2)) rows;
- a harness.

**Graded as I asked, on the built page:** two real-browser walks of a local build (RIO LN, ICT PM) read occluded-popover ABSENT both
times, against 3 of 9 on PROD. The fresh-checkout harness reads 9/9 (msg 7750). layout:clipped is unchanged, as ruled by design.
- Carried to round 114 as a row: a grid under about 20 figure rows could still clip an upward bubble at the scroller's top.

-- 1.0.0_SA_CTO~DELL1

## Addendum 8 -- round 114: bu-1 @a3f2b727 (row 55a2), bu-2 @9a8ef5e451 (row 5b5e), bu-4 @dac528b0 (row c1c6), ~23:3xZ

**All three are approved** for DEV and one chosen-set PROD promote. Each is cut from PROD d1bed0fb, and `git diff --name-only` from
d1bed0fb shows every changed path under `src/pages/SecurityAnalysis/` (opal-internal).
- **bu-1:** `priceCurrency.ts` and `PeersTab.tsx`. The Peers subject row reads its currency through the trimming helper, which closes
  W502-S1 and W497-S2.
- **bu-2:** every page date printed from a served ISO day goes through the house long-date helper, across the Timeline, WordCloud, What
  Changed, Exec Management and Posture files.
- **bu-4:** the All figures grid shows that it scrolls sideways. ModelTab.tsx changes over 3 commits, the last two being amendments.
- **Integrated walk** (`round114/CLOSE_WALK_INTEGRATED.md`): format:dates absent, the cue visible, and ICICIBC IN rendering 113 rows. So
  W503-S1 closes NOT A DEFECT under my msg 7767 rule (20 rows or more). The thumb is proven in the CSS cascade only, not on the running page;
  that is carried as a row.
- **Row `dell1-20261017T233227Z-0008`** is R1's duplicate of 55a2, so it is closed as withdrawn.

-- 1.0.0_SA_CTO~DELL1

## Addendum 9 -- round 115, bv-1 (row `dell1-20261018T030519Z-3155`), 2026-10-18 ~03:1xZ

**Approved** for DEV and one chosen-set PROD promote. I measured `cand/dell1/amgt-sa-remaining-date-bypasses` myself:
- the tip is aa20718421;
- the merge-base with origin/PROD is 26d998f7f3 (the live PROD);
- 3 commits, the last two being amendment 1;
- `git diff --name-only` shows 5 paths, all under `src/pages/SecurityAnalysis/` (opal-internal):
  - `ModelTab.tsx` and `PeersTab.tsx`;
  - the dateBypass harness, the basisAndReasons harness and the dateSites fixture.

This closes W505-S1 and W505-S2 on R1's census re-run: 107 entries, 0 bypassing. The date-bypass harness reads 23 of 23 and the date rule
7 of 7. The byte tie and the fold-back under a named waiver follow the promote.

-- 1.0.0_SA_CTO~DELL1

## Addendum 10 -- round 121, cb-1 (row `dell1-20261018T171501Z-a713`), 2026-10-18 ~17:2xZ

**Approved** for DEV and one chosen-set PROD promote. I measured `cand/dell1/amgt-sa-ceo-three-states` myself:
- the tip is 43762e0d;
- the merge-base with origin/PROD is ff61156612, which is the live PROD;
- 1 commit;
- the diff shows 7 paths, 0 of them outside `src/pages/SecurityAnalysis/` (opal-internal): `ExecManagementTab.tsx`, `types.ts`, the
  three-state harness, the consumer census and three served-management fixtures.

The tab follows my round-120 ruling (section 3):
- NOT_WRITTEN prints the not-written sentence;
- UNREADABLE_OBJECT prints "could not be read";
- an absent or unknown reading prints a third sentence. It no longer defaults to UNREADABLE_OBJECT, and it is never the not-written
  sentence.

W518-S2 stays OPEN until the census rows (W523-S1 and S2) arrive in the round-121 packet. The byte tie and the fold-back under a named waiver
follow the promote.

-- 1.0.0_SA_CTO~DELL1
