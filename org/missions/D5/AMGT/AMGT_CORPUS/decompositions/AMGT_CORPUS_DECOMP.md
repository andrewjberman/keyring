# AMGT_CORPUS -- L5 decomposition v46.0 -- ROUND 46 (the round-45 analysis's enrichment list: the row-class reader and its render, the served acts that carry them, FWD-15/16/21/11 reads, the rendered re-read)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-11 ~13:0xZ.

**Source:** `1.0.0_SA_CTO~DELL1` round-45 analysis `ledger/ROUND_ANALYSIS.round45.md` @0d399ece09 (msg 3835) and its ADDENDUM 1 (msg 3846), over
`3.0.0_SA_CVO` ADJUDICATION_v57..v60. REALIZED 16 of 22; open FWD-11, 12, 15, 16, 20, 21. PRD v0.9, no ENDPOINT change. Round 45's
decomposition kept as `AMGT_CORPUS_DECOMP.round45.md`.

## 0. What this round IS

| # | item (analysis s.2) | cell | path | risk |
|---|---|---|---|---|
| 1 | the row-class reader: every counted row of a team sheet is FIGURE / HEADING / CONTROL, read from the sheet; a FIGURE row carries the team's own period values VERBATIM, cited; `rows` unchanged; METHOD /12 | `CRPS-av-1` | worker `~1`: `lib/research/corpus/team_sheet.py` (+ `dossier.py` METHOD literal and the six tests that pin it) | LOCAL |
| 2 | the render: HEADING renders as a heading with no value, CONTROL is not a row but is counted, FIGURE takes Bloomberg first, else the team's value labelled "team model" with its cite, else a PM-worded why; `unmapped` is 0 by construction | `CRPS-av-2` | worker `~2`: portal `modelSheet.ts`, `tabs/ModelTab.tsx`, `types.ts`, built against the shape this decomposition fixes (parallel to av-1) | LOCAL |
| 3 | the /12 dossier write over the served names, measured name by name (FIGURE rows by source) | `CRPS-av-3` | the issuer's paired served act, after av-1 drains; own never-widen pair | SERVED |
| 4 | the API redeploy that picks /12 (and carries av-1's closure), admitted by blob over the build's closure | `CRPS-av-4` | `AMGT_RESAPP`'s redeploy window (`2.0.0_SA_COO~R1` / `0.7.0_AE_CloudOps~RA1`): this seat asks for the leg and supplies blobs and its pair half after av-1 drains | WORLD |
| 5 | the portal build lands on DEV under the push law (a product file: the candidate goes to the CTO first) | `CRPS-av-5` | the issuer's candidate after av-2 drains | LOCAL (DEV only) |
| 6 | FWD-11: the officer comparison on SAP GY and BABA US against the persisted filing roster, on the LIVE function | `CRPS-av-6` | the issuer's read: `checks/round46/av6_roster_compare_live.py` (READ at the cut: `unchanged 2/2`, `evidence/r46_av6_roster_compare_live_20261011.txt`) | LOCAL (read) |
| 7 | FWD-15's two missing reads: the header posture line, and the verdict-unchanged read | `CRPS-av-7` | the issuer's read on the live payloads and the real components | LOCAL (read) |
| 8 | FWD-16's missing read: one PDF-only name rendered end to end (pillars, management, cases) | `CRPS-av-8` | the issuer's `/ui-walk` of a PDF-only name | LOCAL (read) |
| 9 | FWD-21's two missing reads: the UNVGY page, and the history-unchanged read | `CRPS-av-9` | the issuer's read on the live payloads and the real `modelSheet.ts` | LOCAL (read) |
| 10 | the rendered re-read over every served name: shown by source (Bloomberg / team / why), refused, absent, unmapped 0 over FIGURE rows, the three class counts summing to the sheet per name, the denominator printed; grades FWD-12 and FWD-20 | `CRPS-av-10` | the issuer's read after av-3, av-4 and av-5 are served | LOCAL (read) |
| 11 | the graded-reads packet for L9: FWD-11, 12, 15, 16, 20, 21 | `CRPS-av-11` | the issuer's packet to `3.0.0_SA_CVO` (depends on av-6..av-10) | -- |

**Chains:** `av-1 -> av-3 -> av-4 -> av-10`; `av-2 -> av-5 -> av-10`; `av-6`; `av-7`; `av-8`; `av-9`; `av-6..av-10 -> av-11`.
`fanout: 2 of 2 worker chains (av-1, av-2), cap 8`; the rest are issuer acts, the AMGT_RESAPP window, or the CVO.

## 1. The served shape (fixed here so av-1 and av-2 build in parallel)

`read_thesis_bundle(key)["model"]["team_sheet"]` keeps every round-44 key (`class`, `workbook_key`, `sheet`, `rows`, `model_rows_beside`,
`reason`) and gains, aligned with `rows`:

```
row_classes   ["FIGURE" | "HEADING" | "CONTROL", ...]
row_numbers   [<1-based sheet row>, ...]
row_values    [null | [<cell as the workbook saved it> per period, ...], ...]     (non-null only for a FIGURE row)
periods       [{"label": "2016", "column": "E"}, ...]                              (from the period header; [] when none is found)
row_counts    {"FIGURE": n, "HEADING": n, "CONTROL": n}                            (sums to len(rows))
```

A cell is carried verbatim: a number as a number, a text such as `#VALUE!` as that text, a blank as null. `master_absent` carries the same
keys empty. The API serves the stored field as stored (`scoped_amgt._team_sheet_from_dossier`), so no API code changes; what the redeploy
carries is the `dossier.py` METHOD literal, so that the reader picks the /12 objects.

## 2. The rule (the issuer's reading of ADDENDUM 1, measured on the 32 own workbooks; the worker builds it exactly)

- **Period header:** the first counted row whose numeric cells are ALL integers in 1990..2100, at least 3, strictly increasing. Its
  numeric columns are the period columns; its numbers are the period labels. None found: every counted row is FIGURE, `periods` is `[]`,
  `row_values` entries are null (the page then says why).
- **Above the header** (the info panel): CONTROL when the label is an upper-case identifier with an underscore
  (`^[A-Z][A-Z0-9]*(_[A-Z0-9]+)+$`), else HEADING.
- **The header row, and any later row whose numeric cells are all increasing years:** HEADING.
- **Below the header:** FIGURE when the row holds a numeric value in a period column; else CONTROL (identifier form) or HEADING (words).
- **Measured at the cut** (prototype over the 32): 3759 rows = FIGURE 3353, HEADING 344, CONTROL 62; a period header in 32 of 32; the
  reader's `rows` equal the counted labels on 32 of 32. 2856 FIGURE rows name no field the page reads: they take the team's value.
- **Panel labels read HEADING** ("Ticker:", "Currency:") and render as headings in the sheet's order. That is the CTO's word ("words, no
  numeric value in any period column ... renders as a heading in the sheet's order"); whether it reads well on the page is for av-10.

## 3. The cells (every check dry-run at the base before the cut)

**CRPS-av-1** `checks/round46/av1_check.py` (an in-memory workbook, no network). Base: `av1 build 0/4 control 2/2`; green arm (a reference
implementation, not shipped): `build 4/4 control 2/2`.
**CRPS-av-2** `checks/round46/av2_check.cjs` (the REAL `modelSheet.ts` in a vm) on portal DEV `00989b8b`: base `av2 build 0/5 control 2/2`;
green arm (a throwaway reference patch, not shipped): `build 5/5 control 2/2`. Snapshot `av2_base_snapshot.json`.
**CRPS-av-3 .. av-11** issuer reads and paired acts; their instruments are named in the packet that carries each read.

## 4. Not in round 46: the 10 files in 6 unresolved folders (each folder's identity is its own cell, cut when named and owned);
vocabulary growth (ruling F); anything that changes the 13:00Z fire's call, field list or address; the PROD promote of the portal.
