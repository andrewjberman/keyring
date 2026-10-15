# MDPF_SECHIST SH-t-25 AC4 evidence -- the Positioning frontier label, looked at (2.0.0_SA_COO~H1, 2026-10-15 ~02:5xZ)

For `3.0.0_SA_CVO`'s L9 grade of `SH6-t25-AC4` (a judgment criterion: the reading of the labelled cells and the note). This file records what was run and what the issuer READ on the
screenshots; it is not a grade.

## How it was made (read only; nothing written to the app, S3 or the portal)

- Instrument: `portal/scripts/ui-smoke.mjs` against the dev server already listening on port 5174 (DEV head `e0b033253b`, which contains the feature commit `c77f23624d`; read
  `git merge-base --is-ancestor c77f23624d HEAD` = yes), auth-stubbed, `--click "ETFs"` and, for the performance views, `--click "Performance"`.
- Data: the `--fixtures` file maps `/api/general/etfs/positioning_data.json` to the order's own fixture `portal/src/pages/Positioning/__harness__/frontierFixture.json`
  (`ui_fixtures_carry.json` here; `FIXTURES-MATCH: matched 1 of 1`). The baseline uses the same fixture with `returns_frontier` and `returns_frontier_holdings` removed
  (`ui_fixtures_nocarry.json`). The served page does not carry the keys yet (the producer's first run after the apply is 2026-10-15 13:00Z), so a fixture is the only way to see the label today.
- Book shown: DIVZ (fixture `data_as_of` 2026-10-12), holdings AAPL (ordinary) and SALXX (carried from 2026-10-09).

## Files

| file | view |
|---|---|
| `positioning_etf_characteristics_with_carry.png` | Characteristics view, with carry: the note under the table |
| `positioning_etf_performance_with_carry.png` | Performance view, with carry: `as of 10-09` under each SALXX cell, the note under the table |
| `positioning_etf_performance_no_carry_baseline.png` | Performance view, same fixture without the two keys: no mark, no note (arm c) |

## What the issuer read (stated as read, not graded)

1. Arms (a) and (b) show: each SALXX cell carries `as of 10-09` in small secondary ink under the number; AAPL's cells carry nothing; the note `Returns for SALXX are as of SALXX 2026-10-09 (no vendor day on the book date).` sits under the table.
2. Arm (c) shows: the baseline has no mark and no note; its table rows are the same as the carry view's minus the mark line.
3. Three things for the grader to weigh, none a defect of the build against its order:
   - The note repeats the ticker (`are as of SALXX 2026-10-09`); the order specified that text. A reader may find `Returns for SALXX are as of 2026-10-09` cleaner.
   - The mark also sits under the BLANK windows of a carried holding (WTD, 1M, QTD, 1Q, 1Y render a dash with `as of 10-09` beneath). The order specified both branches; a dash labelled with a date is arguably accurate (blank as of that day) and arguably noise.
   - The ticker cell reads `SAL...` in the Performance view; the baseline shows the same truncation, so it predates this feature.
4. Contrast: the mark and note use the table's existing secondary ink (`--palette-mediumGray`) on the band-valued table ground (the Holdings panel is a band-valued panel today, the known divergence in `portal/CLAUDE.md`). The issuer did not run the `--state-table` contrast grade; the mark is `text-[10px]`, which the grader may want measured.
