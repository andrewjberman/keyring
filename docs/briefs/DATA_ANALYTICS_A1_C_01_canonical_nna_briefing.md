# C_01 -- canonical_nna -- DATA_ANALYTICS layer briefing

**Script:** `data/black_diamond/scripts/gold/C_01.canonical_nna.py`
**Output:** `gold/canonical/nna/{date}.parquet` (+ `nna_atomic/` -> C_01c, + `nna_validation/{date}.json` diagnostic)
**Layer / order:** Group C, order 201; catalog line 90. Reads account_gains (B_03), accounts_dimension (A_00), client_performance (C_02, cross-val), silver/transactions (via lib/nna_flows.py).
**Essential status:** ESSENTIAL -- AGNOSTIC-core. The SINGLE SOURCE OF TRUTH for NNA -> D_00/D_00b/D_00c/D_01/D_02, C_08 read daily_inflow/daily_outflow from here -> served NNA/flows surfaces.
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-25 (Andrew-direct A1 layer-walk, C-tier; patch-register-aware per Andrew 2026-06-25 canonize-the-gold-process directive). Source-grounded.

---

## 1. What it does
Produces per-account canonical NNA with BOTH: (a) the **accounting residual** `aua_residual = AUA_change - growth` (from B_03), AND (b) the **transaction-classified real NNA** (`daily_inflow`, `daily_outflow`, `nna_txn`) via `lib/nna_flows.py`. Enriches with dimensions + a `nna_clean` flag; cross-validates the residual vs legacy script-05 NNA. The canonical NNA other scripts trust (they never call nna_flows independently).

## 2. Recompute posture -- watermark-incremental (--start-date); HEALTHY. Lightweight (arithmetic + the flow classification).

## 3. PATCH-REGISTER findings (Andrew's canonize-the-gold directive) -- distinguishing GOOD labeling from inappropriate patches

C_01 is where the **NNA-vs-dirty-data tension lives**, so it's a key patch-register node -- but the flags here are a MIX, and the distinction is the whole point of Andrew's directive:

- **`nna_clean` (L219) = `(components & NNA_CLEAN_MASK) == NNA_CLEAN_MASK`** -- a **completeness-PROVENANCE flag** (is the residual NNA trustworthy because all gain-components were present?). This is the GOOD pattern -- honest labeling of when a residual is reliable. KEEP (it is exactly the kind of honest-provenance the clean rebuild WANTS, not a patch to excise). NOTE: it is the *residual* that is unreliable when inputs are incomplete -- which is the B_03 "NNA = residual, Growth-completeness-bounded" doctrine surfacing here.
- **`is_ghost` (L551)** -- the **FIFO-ghost flag** (positions B_00 marked bd_stale because the custodian doesn't confirm them). This IS a patch in the Andrew sense: it exists only because BD's FIFO reconstruction invents positions the custodian denies. It **dissolves entirely** under the custodian-direct lot re-sourcing (see B_02 brief) -- an excise-the-root candidate (remove the bad FIFO source, not flag its ghosts).
- **`is_excluded` (L550)** -- account-exclusion flag (defaults False here, set upstream). Needs an upstream trace to classify (legit business exclusion vs a dirty-data dodge) -- flagged for the register's follow-up.
- **The `how='left'` bugfix (L231-241, Andrew 2026-04-14)** -- a genuine CORRECTNESS fix (newly-opened accounts with real flows but no gains-row were silently dropped), NOT an overfit patch. Different category -- keep; it is the kind of root-correctness fix the rebuild preserves.

**Register doctrine this layer establishes:** the patch register must split findings into (i) INAPPROPRIATE PATCHES = excise-at-source candidates (the 90-day flag; is_ghost via FIFO; aberration-dodging exclusions), vs (ii) LEGITIMATE PROVENANCE/CORRECTNESS = keep (nna_clean completeness labeling; the how='left' bugfix). Lumping them together would wrongly strip honest labeling. The NNA residual's sensitivity to dirty data (a $4B-withdrawal aberration would blow up aua_residual) is the strongest argument for Andrew's excise-at-source thesis: clean the aberrant transactions once, and the residual NNA becomes trustworthy without defensive flagging.

## 4. Status / ledger row
- **Tag: ESSENTIAL / AGNOSTIC-core** (NNA single-source-of-truth -> served flows).
- **Recompute: HEALTHY** (watermark-incremental, lightweight).
- **Patch-register: MIXED node** -- is_ghost (excise via FIFO re-source) + is_excluded (trace) = patch candidates; nna_clean + the how='left' fix = legitimate, keep.

### Ledger entry (C-tier)
| Script | Output | Consumers | Tag | Recompute | Notes |
|---|---|---|---|---|---|
| C_01.canonical_nna | gold/canonical/nna/{date} (+atomic,+validation) | C_01c, D_00/b/c, D_01, D_02, C_08 | ESSENTIAL / AGNOSTIC-core | watermark-incremental (HEALTHY) | NNA single-source (residual + txn-classified). PATCH-REGISTER: is_ghost (FIFO-dissolve) + is_excluded (trace) = excise candidates; nna_clean (completeness provenance) + how='left' fix = KEEP. Residual's dirty-data sensitivity = the case for excise-at-source. |
