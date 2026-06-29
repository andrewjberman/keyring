# PFMG_TAXSMA S0.2 -- converter scripts: LOCATE + assessment (read-only discovery)

**Author:** 0.4.0_DS_ClientPlatform, 2026-06-26. **Project:** PFMG_TAXSMA (renamed from ADVI_TAXSMA, COO reg 6906a0b25). **PRD:** docs/architecture/ADVI_TAXSMA_PRD.md (being renamed). **Gate:** S0 discovery -> RAVC COO + CTO. Read-only; no execution surface (hard guardrail: system GENERATES, human executes; no creds in code).

## Step-3 convert_cost_basis.py -- LOCATED, provenance-locked, drift-VERIFIED
- **Located:** in-repo `tools/tax_sma/canonical/convert_cost_basis.py` (landed by CTO 2026-06-26, 86b87d06d). Origin `C:\Users\AndrewBerman\Downloads\convert_cost_basis.py` (still present, 218 lines).
- **Drift check (repo vs Downloads original, I ran it -- not trusting the README self-report):** exactly **4 comment-separator lines** changed -- box-drawing `U+2500` -> ASCII `--` on the `# -- helpers/load SMA accounts/process each cost-basis CSV/write Excel summary` section headers. **ZERO logic/code/formatting change** -- conversion body is byte-for-byte Yang's. (RECORD NOTE: the canonical README says "3 comment-separator lines"; it is actually **4**. Immaterial -- all cosmetic ASCII-compliance -- but flag for accuracy.)
- **I/O contract (source-confirmed, matches PRD §3):**
  - IN: `{BASE}\Tax Lot\{YYYYMMDD}\CostBasis_Acct_*.csv` (Schwab exports, data line 8, utf-8-sig; cols [0]symbol [2]date [3]qty [4]market_value [6]cost_per_share) + `{BASE}\Tax SMA Accounts.xlsx` (acct key = digits-only).
  - OUT: `{BASE}\Initial Holding\{YYYYMMDD}\` -> `{index}_{account}.txt`, `{index}_{account}_ex_divest.txt`, `summary.xlsx`.
- **Host / shim effort (Andrew decision #3: VERBATIM + parameterize {BASE}+{date} ONLY -- not a port):**
  - Hardcodes (source lines 21-24): `BASE = Path(r"c:\Users\YangLiu\Opal Capital\Shared - Documents\TAX")`; `TODAY/TODAY_DATE/_biz` = `date.today()`-derived. All I/O (lines 28-31) derive from `BASE`+`TODAY`.
  - Shim = inject `BASE` + a `date` arg (replace the 4 module-level constants), body untouched. **TRIVIAL** (thin wrapper / env). Deps: `pandas`, `openpyxl`.
  - **HOST INSIGHT (feeds Andrew's UI=HYBRID call):** `BASE` is a **OneDrive SHARED library** path ("Opal Capital\Shared - Documents\TAX"), NOT machine-local-only -> reachable via the **M365 gateway** -> cloud-stageable. So step-3 hosts cleanly HYBRID: M365/OneDrive intake of the Tax Lot CSVs -> run the parameterized converter (S3-side or a thin local runner) -> write `Initial Holding` back to OneDrive. No hard machine-local dependency for step-3.

## Step-5 convert_optimization.py -- LOCATED + provenance-locked + contract-pinned (UPDATED 2026-06-29)
**STATUS CHANGE:** the file LANDED after the original brief was authored (the Yang/UA request worked). It is
now in-repo + committed -- the original "NOT LOCATABLE" status is SUPERSEDED.
- **Located + locked:** `tools/tax_sma/canonical/convert_optimization.py` (committed bfa81d9da, "capture canonical
  step-5 converter + Yang source-spec"). Origin `C:\Users\AndrewBerman\Downloads\convert_optimization.py` (118 lines).
- **Byte-fidelity (verified 2026-06-29):** the committed canonical copy is **BYTE-IDENTICAL** to Yang's Downloads
  source (`diff` clean; 4004 bytes both). Landed VERBATIM (still carries the 3 box-drawing `U+2500` comment
  separators -- a cosmetic ASCII-compliance deviation to optionally normalize like step-3's, ZERO logic impact).
- **I/O contract (source-confirmed from the 118-line actual source):**
  - IN: `{BASE}\optimization\{YYYYMMDD}\Acct-N.xlsx` (Axioma optimization output, one per account; reads the
    **"Trade List"** sheet, header row = first cell == "Symbol", uses cols `Ticker` / `Trade Type` / `Traded Shares`)
    + `{BASE}\Tax SMA Accounts.xlsx` (maps `Index` col -> `Account Number`, digits-only key).
  - OUT: `{BASE}\Trade\{YYYYMMDD}\schwab_upload_{YYYYMMDD}.csv` -- **NO header**, rows `AccountNumber,Action,Quantity,Ticker`.
    Action map: BUY->`B`, SELLSHORT/SHORT->`SS`, SELLLONG/LONG->`SL`, else->`S`. Qty = `abs(round(Traded Shares))` int.
    Ticker `.`->`/`. Skips CASH_USD / zero-qty / blank-ticker / Total rows.
- **HARD-GUARDRAIL CONFIRMED (load-bearing finding):** the script's terminal action is `OUTPUT_FILE.write_text(...)`
  (line 115) -- it **GENERATES the trade CSV and STOPS. No Schwab upload, no trade execution, no API/browser post.**
  So the PRD's non-negotiable guardrail (system generates, HUMAN reviews+executes) is satisfied by Yang's own code
  at step-5; the automation just needs to surface the generated file for a human to upload.
- **Host / shim effort (same posture as step-3):** hardcodes `BASE` (same OneDrive shared TAX dir) + `TODAY =
  date.today()` (lines 21-26). Shim = inject `{BASE}` + `{date}`, body untouched -- TRIVIAL. Deps: `pandas` (+ openpyxl
  for `read_excel`). HYBRID-hostable via the OneDrive-shared BASE, same as step-3.

## Net assessment (UPDATED 2026-06-29 -- S0.2 now COMPLETE, both converters locked)
- **convert_cost_basis (step-3):** located, drift-verified, contract-pinned, shim trivial, HYBRID-hostable via the OneDrive-shared BASE. Cheaper than a port (Andrew #3).
- **convert_optimization (step-5):** **NO LONGER BLOCKED** -- located + committed (bfa81d9da, byte-identical to Yang's source), I/O contract pinned from the 118-line source (both directions), shim trivial, HYBRID-hostable. **Hard-guardrail confirmed in-code** (generates the CSV, never executes/uploads).
- **S0.2 verdict:** BOTH converters are provenance-locked + contract-pinned + verbatim-faithful + trivially shimmable. S0.2 is COMPLETE. Remaining S0 gates = S0.1 (the Schwab-lot cost-basis audit -- the step-2 lookup-vs-pull lever) + S0.3 (the email PRELIM/final disambiguation rule).
- **Architecture input:** both converters' OneDrive-shared BASE supports CTO's HYBRID lean -- the file legs ride the M365 gateway + S3; only Yang's Factset (step 4) is irreducibly local. The step-5 generate-not-execute property means the trade-file leg needs only a "file ready for human upload" surface, no execution-credential design.
