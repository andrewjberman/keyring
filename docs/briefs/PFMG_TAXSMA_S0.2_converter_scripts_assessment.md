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

## Step-5 convert_optimization.py -- NOT LOCATABLE -> route to Yang/UA (Rule 22, do NOT infer I/O)
- **Searched (this machine):** repo (absent), `C:\Users\AndrewBerman\{Downloads,Desktop,Documents}` (absent), `C:\Users\YangLiu` (**directory not present on this machine**). Not findable.
- Per the PRD S0.2 mandate + COO + Rule 22: **request the file from Yang via 0.0.1_UA_mstools** -- do NOT infer or reconstruct its I/O contract. It is the OPEN blocker for the step-5 half.
- Once the source lands: same-pattern S0.2 -- provenance-lock under `tools/tax_sma/canonical/`, pin its I/O contract from source, assess host (no verbatim directive yet for step-5, so a normal assessment -- but default to the same verbatim+parameterize posture unless told otherwise).

## Net assessment
- **convert_cost_basis:** done-grounded -- located, drift-verified, contract-pinned, shim trivial, HYBRID-hostable via the OneDrive-shared BASE. Cheaper than a port (Andrew #3).
- **convert_optimization:** BLOCKED on file delivery from Yang/UA. I/O both-directions = confirmed for step-3, UNKNOWN for step-5 pending the source.
- **Architecture input:** the OneDrive-shared BASE supports CTO's HYBRID lean -- the file legs ride the M365 gateway + S3; only Yang's Factset (step 4) is irreducibly local.
