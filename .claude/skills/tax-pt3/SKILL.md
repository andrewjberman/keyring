---
name: tax-pt3
description: OPAL_TAXSMA part 3, the FactSet conversion: take pt2's lot-level CSVs and Yang's roster and run his convert_cost_basis.py verbatim (tools/tax_sma/run_converter.py, fail-loud on drift) to produce the FactSet Initial Holding files into SharePoint TAX/Initial Holding/{YYYYMMDD}/. `/tax-pt3 {YYYYMMDD}` (default: the newest date with pt2 CSVs). Generates files only -- never a trade or an upload.
---

# /tax-pt3 {YYYYMMDD} — Schwab lots -> FactSet "Initial Holding" format (OPAL_TAXSMA part 3)

**What it is:** Yang's step 3. pt2 produced the lot-level cost-basis CSVs; pt3 converts them to the
FactSet input format Yang optimizes against (step 4, MANUAL). This is a **verbatim-Yang conversion** —
`tools/tax_sma/canonical/convert_cost_basis.py` runs unchanged; the runner only injects `BASE`+`date`.

**Commissioning:** Andrew-direct family finalize 2026-07-21 (0.5.0_AE_OpalETL~A). The converter core +
injection wrapper were already CTO-blessed (`run_converter.py`, CTO(B) 210145Z); this skill is the
SharePoint I/O orchestration around them. Mechanics exercised end-to-end on synthetic Schwab-shape data
(divest cross-ref, CASH_USD substitution, `/`->`.` rewrite, lot numbering) — see `tools/tax_sma/pt3_stage.py`
`selftest`. LIVE validation runs on the next fresh `TAX/Tax Lot/{date}/` pt2 output.

**Mechanism (do NOT reimplement — these are the source-of-record):**
- `tools/tax_sma/canonical/convert_cost_basis.py` — Yang's verbatim step-3 converter (provenance-locked).
- `tools/tax_sma/run_converter.py` — loads the canonical, overrides ONLY `BASE`+the date pins (fail-loud
  `ConfigPinMismatch` on any drift/re-delivery), execs an in-memory copy. Canonical on disk NEVER modified.
- `tools/tax_sma/pt3_stage.py` — the I/O glue: `build-roster` (rebuild `Tax SMA Accounts.xlsx` from a
  `read_site_workbook` grid), `report` (render summary.xlsx as markdown). Holds NO MCP; the agent holds those.

**I/O contract (pinned):**
- IN  `TAX/Tax Lot/{YYYYMMDD}/CostBasis_Acct_*.csv`  (pt2's output — the canonical globs this exact name)
- IN  `TAX/Tax SMA Accounts.xlsx`  (Yang's roster: cols `Account Number`, `Name`, `Index`, `Divest Securities`)
- OUT `TAX/Initial Holding/{YYYYMMDD}/{index}_{account}.txt`            (all lots: SYMBOL,Qty(.2f),CostPerShare,YYYY/MM/DD,LotNumber)
- OUT `TAX/Initial Holding/{YYYYMMDD}/{index}_{account}_ex_divest.txt`  (divest tickers removed + renumbered; leading `CASH_USD` row if divest MV)
- OUT `TAX/Initial Holding/{YYYYMMDD}/taxpt3-report.md`                 (per-account MV breakdown, row counts, sha of inputs; the local `summary.xlsx` stays for audit — upload is text-only)

**Never:** modify the canonical converter (verbatim Yang); overwrite an existing SharePoint artifact
(`conflictBehavior=fail` — a collision means it already ran); treat pt3 output as a trade file or upload
anything to Schwab; run with credentials in code. **pt3 GENERATES; a human (Yang) reviews + optimizes.**

## Steps (agent-run, Phase A)

0. **Resolve inputs.** `{YYYYMMDD}` = the arg, else the NEWEST `TAX/Tax Lot/{date}/` folder that
   contains `CostBasis_Acct_*.csv` (a fresh pt2 run). Pick a local `BASE` = a scratch dir
   (e.g. the session scratchpad `.../scratchpad/tax_pt3/{YYYYMMDD}`).

1. **Locate the site.** `find_sharepoint_site` for the TAX documents site (same site pt1/pt2 write to);
   note `site_id`. `list_site_files(site_id, "TAX/Tax Lot/{YYYYMMDD}")` -> the `CostBasis_Acct_*.csv`
   item_ids. `list_site_files(site_id, "TAX")` -> the `Tax SMA Accounts.xlsx` item_id.

2. **Download the inputs.**
   - Each CostBasis CSV: `read_site_file(site_id, item_id)` -> write the text to
     `{BASE}/Tax Lot/{YYYYMMDD}/{filename}` (keep the exact `CostBasis_Acct_*.csv` name).
   - The roster: `read_site_workbook(site_id, roster_item_id)` -> save the returned grid to
     `{BASE}/roster_grid.json`, then
     `python tools/tax_sma/pt3_stage.py build-roster --base {BASE} --roster-json {BASE}/roster_grid.json`
     (fail-loud if `Divest Securities`/`Account Number`/`Name`/`Index` is absent).

3. **Convert (verbatim).**
   `python tools/tax_sma/run_converter.py convert_cost_basis.py {BASE} {YYYYMMDD}`
   A `ConfigPinMismatch` here = the canonical drifted (a Yang re-delivery moved a config line) -> STOP,
   re-provenance the canonical, never run a stale path.

4. **Collect + upload the outputs** to `TAX/Initial Holding/{YYYYMMDD}/`:
   - each `{BASE}/Initial Holding/{YYYYMMDD}/*.txt` -> `upload_text_to_site(site_id, "TAX/Initial Holding/{YYYYMMDD}", name, text)`.
   - `python tools/tax_sma/pt3_stage.py report --base {BASE} --date {YYYYMMDD}` -> upload as `taxpt3-report.md`
     (include: per-account lot counts, the MV breakdown table, and each input CSV's sha256 for the audit tie).
   - `conflictBehavior=fail` is built into `upload_text_to_site`; a collision = already-ran, STOP and report.

5. **Verify + report.** `list_site_files(site_id, "TAX/Initial Holding/{YYYYMMDD}")` — listing-based
   acceptance (name + size for every expected `{index}_{account}.txt` / `_ex_divest.txt`). Report to chat +
   broker; on any failure MCP a note to `0.5.0_AE_OpalETL` (project lane).

## Phases

- **Phase A (NOW):** a workspace agent runs this skill (SharePoint reads/writes ride the m365 gateway;
  the converter runs as a local python subprocess). Operator: Andrew or any workspace agent on his word.
- **Phase B (future, gateway-packaged):** Alyssa-operable from her laptop. The converter is a local
  python (pandas/openpyxl) step, so Phase B needs it packaged behind the gateway (a `taxsma_convert`
  tool or a small Lambda) — deferred; scope it with pt2's Phase-B gateway leg, not before.

## Open / notes

- **Roster source:** currently `Tax SMA Accounts.xlsx` in SharePoint TAX (Yang maintains it; the
  `Divest Securities` column drives the ex-divest file). When OPAL_TAXSMA_REGISTRY lands, the registry
  becomes the account source-of-truth for the ETL — but pt3's divest input stays Yang's xlsx (a
  per-run business input, not an account-membership fact).
- **step-5** (`convert_optimization.py` -> Schwab trade file) is DESCOPED for now but the canonical is
  landed + parameterized the same way (`run_converter.py convert_optimization.py {BASE} {date}`); a
  `/tax-pt5` would wrap it identically, with the **generated-not-executed** guardrail hard-enforced.
