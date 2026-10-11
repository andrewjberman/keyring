# AMGT_CORPUS -- L5 decomposition v47.1 -- ROUND 47 (the round-46 analysis's enrichment list: field-code rows read in words, the team's own number format, the portal render, and the master template)

**Issuer:** `2.0.0_SA_COO~C1` (dell1), 2026-10-11 ~16:0xZ.

**Source:** `1.0.0_SA_CTO~DELL1` round-46 analysis `ledger/ROUND_ANALYSIS.round46.md` (msg 3965) and its ADDENDUM 1 (msg 3972), over
`3.0.0_SA_CVO` slug msg 3960 (ADJUDICATION_v61 @80f1356183). REALIZED 19 of 22 (FWD-15 makes 20 on the CVO's re-sign); open FWD-12 (master
arm) and FWD-20 (labels and formats). PRD v0.10 (ADDENDUM E, FWD-15 to the Posture tab). Round 46's decomposition kept as
`AMGT_CORPUS_DECOMP.round46.md`.

## 0. What this round IS

| # | item (analysis s.3, ADDENDUM 1) | cell | executor | risk |
|---|---|---|---|---|
| 1 | the label of every field-code row, in words: Bloomberg's description as stored, cited; a FactSet data item takes FactSet's published description with its cite, else the label "FactSet line" (code and why in the title); `*_OVERRIDE` and `EQY_FUND_YEAR` are CONTROL by name; each team cell's own Excel number format is captured; METHOD /13 | `CRPS-aw-1` | worker `~1`: `lib/research/corpus/` | LOCAL |
| 2 | the render: a code-labelled row prints the served label, never the code; a FactSet row's cell says "FactSet, via team model"; a team value prints by its own number format with the full value in the title | `CRPS-aw-2` | worker `~2`: `portal/src/pages/SecurityAnalysis/` | LOCAL |
| 3 | the /13 dossier write over the served names (each name's `row_labels` split by source, the class census re-printed and summing per workbook) | `CRPS-aw-3` | the issuer's paired served act after aw-1 drains; own never-widen pair | SERVED |
| 4 | the API redeploy that picks /13 (carries aw-1's closure), admitted by blob | `CRPS-aw-4` | `AMGT_RESAPP`'s window (`2.0.0_SA_COO~R1` / `0.7.0_AE_CloudOps~RA1`) | SERVED |
| 5 | the portal candidate reviewed by the CTO before DEV; DEV landing under the push law; the PROD release waits on Andrew's `e7f2` | `CRPS-aw-5` | the issuer's candidate after aw-2 drains | LOCAL (DEV only) |
| 6 | FWD-20's served read on DEV: 0 raw codes visible over the FIGURE rows split by source with the fallback count printed; 0 team cells beyond their format's decimals; percents as percents; the class census | `CRPS-aw-6` | the issuer's read on the live payloads and the real `modelSheet.ts` | LOCAL (read) |
| 7 | FWD-12's master arm: locate `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx` across the research SharePoint (site-wide file search, denominator printed); found, ingest under the harvest path; nowhere, the team's file to supply (analysis s.4) | `CRPS-aw-7` | the issuer's read (the gateway's SharePoint tools; a worker holds none) | LOCAL (read) |
| 8 | the graded-reads packet for L9: FWD-12 and FWD-20 | `CRPS-aw-8` | the issuer's packet to `3.0.0_SA_CVO` (depends on aw-6, aw-10) | -- |
| 9 | (AMENDMENT 1, after the CTO's ADDENDA 2 and 3, msgs 3994 and 4001) the master template is its own bronze table `research_template` (partition `template=<SharePoint item id>`, the address builder as it prints today); the master-arm reader reads that table; the team's own labels of the code rows are MEASURED from the workbook (column-B metric name, single-row pass-through), cited, claim measured, the count printed | `CRPS-aw-9` | worker `~1` (FOLDED INTO the `CRPS-aw-1` order as its AMENDMENT 2: GATE (x) refuses a second order into round 47, and the files are the same): `lib/research/corpus/` | LOCAL |
| 10 | the template's one write-once put into `research_template` at site Z (the library is synced there only), under its own never-widen pair and a ledger entry opened before the act; the stored object re-opened and compared | `CRPS-aw-10` | the issuer's paired served act, executed by `0.7.0_AE_CloudOps~ZC` under its own order in workstream `TEMPLATE` of round 47 (a disjoint write surface and lane, Rule 27) | SERVED |
| 11 | the render of `claim: measured` (the label text, the title naming the cite, the census `measured` count) | `CRPS-aw-11` | worker `~2` (FOLDED INTO the `CRPS-aw-2` order as its AMENDMENT 1): `portal/src/pages/SecurityAnalysis/` | LOCAL |

**Chains:** `aw-1 -> aw-9 -> aw-10 -> aw-3 -> aw-4 -> aw-6`; `aw-2 -> aw-11 -> aw-5 -> aw-6`; `aw-7` (DONE: found, evidence
`r47_aw7_master_template_search_20261011.md`); `aw-6, aw-10 -> aw-8`.
`fanout: 2 of 2 worker chains (aw-1, aw-2); aw-9 and aw-11 are amendments to those two orders (queue rule: same files, same chain; GATE (x)
refuses a second issuance into the round and adds no file)`; the rest are issuer acts, the AMGT_RESAPP window, or the CVO. The /13 write
(aw-3) waits for aw-9 and aw-10 so the page is written once.

## 1. The served shape (fixed here so aw-1 and aw-2 build in parallel)

`read_thesis_bundle(key)["model"]["team_sheet"]` keeps every round-46 key (`class`, `workbook_key`, `sheet`, `rows`, `model_rows_beside`,
`reason`, `row_classes`, `row_numbers`, `row_values`, `periods`, `row_counts`) and gains, aligned with `rows`:

```
row_labels   [null | {"text", "source": "bloomberg"|"factset", "claim": "held"|"absent", "cite": <repo path>|null, "code", "why": <words>|null}, ...]
row_formats  [null | [<the period cell's Excel number format string, or null where the sheet carries no cell> per period, ...], ...]   (non-null only for a FIGURE row)
```

`row_labels[i]` is null unless the sheet label has the identifier form (`^[A-Z][A-Z0-9]*(_[A-Z0-9]+)+$`). An identifier label whose code is a mnemonic of
`integrations/bloomberg/research/field_map.json` takes that field's `basis.definition` AS STORED (`source bloomberg`, `claim held`, `cite` the field
map's path). A code starting `FF_`, `FFI_`, `FG_`, `FE_` or `P_` is a FactSet data item: `lib/research/corpus/factset_descriptions.json` is read first
(`{"entries": {"<code>": {"text", "cite"}}}`, FactSet's own published description and where it was published; `claim held`); with no entry the label is
"FactSet line", `claim absent`, `why` says no published FactSet description was found and the meaning is not inferred from the name. Any other
identifier the field map does not carry is "Bloomberg line", `claim absent`, `why` says the estate's field metadata does not describe it.
The API serves the stored field as stored, so no API code changes; what the redeploy carries is the `dossier.py` METHOD literal, so that the reader picks
the /13 objects.

## 2. The rules (CTO ADDENDUM 1, msg 3972; the issuer's reading is stated where it adds)

- **CONTROL by name:** a counted row whose label is `*_OVERRIDE` (`^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*_OVERRIDE$`) or is `EQY_FUND_YEAR` is CONTROL
  wherever it sits and whatever its cells hold. It is counted, never rendered, and never the period header. Cite: the estate's own use of
  `BEST_FPERIOD_OVERRIDE` as the request parameter (`integrations/bloomberg/research/model_block_pull.py` `FORECAST_OVERRIDE_FIELD`) and
  `EQY_FUND_YEAR` as the fund-year key (`FIELD_BASIS`), and Bloomberg's `_OVERRIDE` naming convention.
- **Label by source, claim held:** nothing is inferred from the letters of a code.
- **Number format:** the saved value is carried unchanged (`row_values` stays verbatim); the render prints it by the cell's own format and the full
  value rides the title. `General` prints at most 4 decimals with trailing zeros trimmed (the issuer's reading of "0 cells beyond the format's decimals");
  a percent format prints as a percent.
- **Measured at the cut (the live /12 team_sheet over the 32 own workbooks):** 1348 FIGURE rows carry a code label: 646 on 56 Bloomberg mnemonics
  the field map describes, 702 on 50 codes it does not (FactSet data items and 4 Bloomberg names). The by-name rule moves 29 FIGURE and 32 HEADING
  rows to CONTROL; the /13 write's census re-prints the classes.
- **AMENDMENT 1 -- the period header (issuer, ~17:1xZ).** Round 46's header test (all numeric cells of the row are years) took the
  `EQY_FUND_YEAR` row as the header on CLX, ML FP and BABA and classed ~190 of their model rows HEADING (row D1-S7). A YEAR ROW is now a counted
  row with at least 3 strictly increasing integer-year cells that make up at least 80% of its numeric cells; the period columns are those
  cells' columns; a named CONTROL row is never the header. The /13 write carries the corrected classes. Amends the aw-1 order face
  (@93aceffa31).
- **AMENDMENT 1 -- measured labels (CTO ADDENDA 2 and 3).** Precedence for a code row's label: the Bloomberg field map's description (held);
  an entry of `factset_descriptions.json` (held); the team's own label MEASURED from the workbook (column-B metric name, else the one label of
  the single labelled row that passes the code row through in a period column), cited `<sheet>!<cell>`; else the fallback line (claim absent).
- **Searched for FactSet's published descriptions (2026-10-11, 2 web searches and 2 fetches of the vendor's developer pages): no source found.** The
  search was bounded, not exhaustive; `factset_descriptions.json` ships with no entries, so all 50 codes read "FactSet line" until an entry with its
  cite is added, and the mechanism needs no code change for that.
- **Four Bloomberg names the field map does not carry** (`BS_TIER1_COM_EQUITY_RATIO`, `BS_TOT_LOAN`, `CF_DECR_CAP_STOCK`, `CF_INCR_CAP_STOCK`): the
  ruling names only FactSet codes. The issuer reads "Bloomberg line" with the code and why in the title; stated to the CTO.

## 3. The cells (every check dry-run at the base before the cut)

**CRPS-aw-1** `checks/round47/aw1_check.py` (an in-memory workbook, no network). Base: `aw1 build 0/4 control 2/2`; green arm (a reference
implementation, not shipped): `build 4/4 control 2/2`.
**CRPS-aw-2** `checks/round47/aw2_check.cjs` (the REAL `modelSheet.ts` in a vm) on portal DEV `cb76f857`: base `aw2 build 0/4 control 2/2`; green arm
(a throwaway reference patch, not shipped): `build 4/4 control 2/2`. Snapshot `aw2_base_snapshot.json`.
**CRPS-aw-3 .. aw-8** issuer reads and paired acts; their instruments are named in the packet that carries each read.

## 4. Not in round 47: the 10 files in 6 unresolved folders (each folder's identity is its own cell, cut when named and owned); vocabulary growth
(ruling F); the 4 Bloomberg codes' descriptions (a Bloomberg field-description pull goes only through the Bloomberg queue);
anything that changes the 13:00Z fire's call, field list or address; the PROD promote of the portal (Andrew's `e7f2`).
