# Brief — Schwab TRN NNA Enrichment (Authoritative NNA Source + BD Silver Back-Fill)
**Author:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21
**Priority:** P1
**Assignee:** 0.6.0_AE_PartnerETL
**Approver:** 1.0.0_SA_CTO
**Driver:** 49 Financial NNA reconciliation (Andrew, 2026-04-21). BD silver is systematically missing new-account funding events; Schwab TRN is the authoritative NNA source and must enrich gold-layer NNA.

---

## Problem Statement

Our canonical NNA pipeline (`C_01.canonical_nna.py`) consumes BD silver transactions as its only flow source. On the 49 Financial book, reconciliation against Schwab's Business Review PDF over the 13 months May 2024 - May 2025 shows:

| Source | NNA | Delta vs Schwab |
|--------|-----:|------:|
| Schwab PDF (authoritative) | +$354.7M | — |
| Our canonical NNA (BD silver only) | +$211.1M | **-$143.6M** |

Two distinct root causes, confirmed at transaction level via Jul-Dec 2024 account-level cross-reference between Schwab TRN files and our BD silver:

**1. Inflow undercount (~$91M, ~58% coverage):** Schwab credits TRN immediately on wire/ACAT receipt; BD's client master lags 2 days to 5 months before recognizing the new 49F account, then ingests only current holdings and never replays the original funding transaction. Documented examples:
- Acct `79128541` (Jessica Lindsey Short Trust): $20.10M WIRED FUNDS RECEIVED on 2024-12-31 in Schwab TRN. BD silver first sees the account on 2025-01-02 with zero inflow record. The wire is permanently absent from BD.
- Acct `33823043` (STONERIDGE ROAD GROUP HOLDINGS): $17.40M WIRED FUNDS RECEIVED on 2024-12-30. BD doesn't ingest until 2025-05-30 (5 months later); only records current holdings as ACAT-In rows summing $2.69M.
- 1,642 such Schwab-only (acct, date) pairs totalling $91.3M over Jul-Dec 2024.

**2. Outflow overcount (~$85M, Jun 2024 alone):** 210 MetLife Variable Annuity "ghost" accounts post bulk `EF Transfer Out` rows on 2024-06-28 ($84.99M). Schwab excludes variable-annuity held-away assets from NNA; our BD-sourced classifier counts them. Separate issue, separate fix (DS-lane `nna_flows.py` filter), NOT addressed by this brief.

**Schwab NNA definition (from their Business Review PDF):**
- Existing + New Client NNA combined = total firm NNA
- Includes: Cash, TOA, FDIC
- Excludes: clients moving between existing Schwab platforms (Retail <-> Advisor Services)

BD silver does not and cannot fill this gap with any classifier change — the transactions are absent upstream, not miscategorized. Schwab TRN is the only data source that covers them, and we already receive it.

---

## What We Already Have

Do not rebuild what already exists.

### Data paths (authoritative)

**Schwab bucket (`s3://opal-data-schwab`):**

| Prefix | Contents | Status |
|--------|----------|--------|
| `01_raw/CRS{YYYYMMDD}.TRN` | Raw Schwab TRN (pipe-delimited) | 568 TRN files landed 2024-01-16 to 2026-04-20 |
| `01_raw/CRS{YYYYMMDD}.RPS` | Raw position snapshots | Same directory, sibling files |
| `01_raw/CRS{YYYYMMDD}.ULN` | Raw unrealized gain/loss | Same directory, sibling files |
| `01_raw/CRS{YYYYMMDD}.ACC` | Raw account master | Same directory, sibling files |
| `02_anonymized/CRS{YYYYMMDD}.TRN` | Anon account IDs | Partial; overlaps `01_raw/` |
| `03_mappings/CRS{YYYYMMDD}.TRN.mapping.json` | Anon hash -> item_id | Partial; through 2025-11 |
| `silver/RPS/date={YYYYMMDD}/data.parquet` | RPS silver (position snapshots) | Backfilled |
| `silver/ULN/date={YYYYMMDD}/data.parquet` | ULN silver (unrealized open lots) | 349 STANDARD partitions backfilled 2026-04-17 |
| `bronze/rps/CRS{YYYYMMDD}.RPS` | RPS mirror (historical; superseded by `01_raw/`) | 63 files |
| `03_silver/TRN/date={YYYYMMDD}/data.parquet` | Parsed TRN silver | **EMPTY — Phase 2 target** |
| `03_silver/TRN_NNA/date={YYYYMMDD}/data.parquet` | NNA-classified TRN | **DOES NOT EXIST — Phase 3 target** |

**BD bucket (`s3://opal-data-bd`) — reference paths consumed by this workstream:**

| Path | Contents |
|------|----------|
| `silver/transactions/{YYYY-MM-DD}.parquet` | BD daily transactions (source for `nna_flows.py`) |
| `gold/canonical/nna/{YYYY-MM-DD}.parquet` | Canonical NNA (output of `C_01.canonical_nna.py`) |
| `platinum/firm/timeseries_overview.json` | Firm-level monthly/quarterly/annual NNA timeseries (consumer) |
| `platinum/firm/partner_analytics_monthly.json` | Per-period partner analytics (consumer) |
| `platinum/49financial/ownership_map.json` | 49F ownership map |

**OneDrive source (manual Schwab delivery):**

- Path: `C:\Users\AndrewBerman\OneDrive - Opal Capital\Documents\Schwab Data Delivery\08242234\` (master account 08242234 = 49 WEALTH MANAGEMENT LLC)
- Filename pattern: `CRS{YYYYMMDD}.{ext}` where ext in {TRN, RPS, ULN, ACC, RLD, RLU, RLW, RLY, RTU, RTY, SEC, TCF, TCFX, TNN, UPN, UPT}
- As of 2026-04-21: 1,232 total CRS files (all extensions); 496 TRN files

### Schwab master-account identifier

- `0008242234` — 49 WEALTH MANAGEMENT LLC (the only firm TRN files we currently receive). Appears as `master_account` in the TRN H1 header and stays constant across all 568 TRN files.

**Converter:** `data/black_diamond/scripts/bronze/convert_schwab_trn_to_parquet.py` — already authored by this agent under ADHC_HISTRY (project re-scoped; output was never backfilled). Reads H2 header positionally, resolves key columns by pattern match, writes to `03_silver/TRN/`. ProcessPool, idempotent, same shape as the live ULN and RPS converters.

**Pattern precedent:** `convert_schwab_uln_to_silver.py` (deployed 2026-04-17, 349 STANDARD partitions live) is the reference implementation. Follow it verbatim.

---

## Source Data — TRN

**Format:** Pipe-delimited ASCII. Record types (each line prefixed with 2-char record code + pipe):
- `H1|` — file header (master account `0008242234`, firm name `49 WEALTH MANAGEMENT LLC`, date)
- `H2|` — compressed column names (115 columns, contains duplicates — e.g. `Tran` appears at positions 35 and 42)
- `H3|` — column-name extension row (type codes / sub-labels — not data)
- `D1|` — data rows
- `T1|` — trailer (row counts)

Safe row filter: `line.startswith('D1|')`. The existing converter uses this; any line-index-based filter will misfire on rare files with varying header counts.

**Data-row columns (key fields for NNA):**

| Field | H2 position | Example |
|-------|:-----------:|---------|
| Account ID | 4 | `0010066510` |
| Transaction | 34 | `Deposits and Withdrawals` |
| Tran (code) | 35 | `TOA`, `PDEFT`, `DPINS`, `CHE`, `BKSWP`, `BRSWP`, `DIV`, `TRADE` |
| Transaction Source | 36 | `*DEPOSIT`, `WIRED FUNDS IN`, `MONEYLINK TRANSFER`, `TRANSFER ACCOUNT`, `FUNDS PAID`, `AUTO BANK SWEEP` |
| Transaction Detail Description | 37 | `TOA ACAT 0062 CASH`, `IRA ROLLOVER CONT`, `Tfr BANK OF AMERICA, CLIENT NAME` |
| Trade Date | 40 (duplicate-col `Trade__1` if de-duped) | `20241231` |
| Settlement Date | 10 | `20241231` |
| Quantity | 44 | `+0000000006.000000` |
| Price | 45 | `+00000000070.7599` |
| Gross Amount | 46 | `+0000000000424.56` |
| Net Amount | 48 | `+0000000000000.00` |

**Numeric parsing:** `+0000000000583.00` signed-prefix, 16-char fixed-width. Strip whitespace, `float()` works directly (Python parses the `+` prefix). Zero-padded leading zeros are fine.

**Direction convention:** Gross Amount is unsigned (`+` prefix always). Direction is inferred from `Transaction Source` + sub-pattern on `Transaction Detail Description`. See classifier below.

**Coverage as of 2026-04-21:**
- S3 `01_raw/`: 568 files (2024-01-16 through 2026-04-20)
- OneDrive (local, user-managed): 245 files. User confirmed 2026-04-21 plans to upload all of 2025.
- Expected S3 total after 2025 backfill lands: ~630 files.

---

## Required Output — Two Silver Layers

### Layer A: `03_silver/TRN/date={YYYYMMDD}/data.parquet`

Raw parsed TRN — one row per TRN data line. Schema mirrors the existing converter's output.

```
account_id_schwab       string     -- 10-digit Schwab Account ID, zero-stripped (the join key, call it acct10)
account_id_padded       string     -- 10-char zero-padded original (kept for traceability)
trade_date              date       -- parsed from Trade Date col
settlement_date         date
transaction             string     -- Transaction col (category)
tran_code               string     -- Tran col (short code)
transaction_source      string     -- stripped, upper
transaction_detail      string     -- description
ticker                  string
cusip                   string
quantity                float64
price                   float64
gross_amount            float64
net_amount              float64
commission              float64
file_date               date       -- partition date
master_account          string     -- 0008242234 (firm scoping)
firm_name               string     -- 49 WEALTH MANAGEMENT LLC
```

**Partition:** `03_silver/TRN/date={YYYYMMDD}/data.parquet`, one per file.

### Layer B: `03_silver/TRN_NNA/date={YYYYMMDD}/data.parquet`

NNA-classified derivative of Layer A. One row per TRN event that is NNA-eligible (inflow or outflow). Excluded rows (sweeps, dividends, trades, internal journals) do NOT appear here — keeps downstream consumers simple.

```
acct10                  string      -- zero-stripped Schwab Account ID (join key)
trade_date              date
direction               enum        -- 'inflow' | 'outflow'
sub_category            enum        -- 'WIRE' | 'MONEYLINK' | 'TOA' | 'DEPOSIT' | 'CHECK' | 'IRS_WH' | 'OTHER'
gross_amount            float64     -- always positive; direction is the sign carrier
tran_code               string
transaction_source      string
transaction_detail      string
schwab_txn_key          string      -- synthetic hash of (acct10, trade_date, tran_code, gross_amount, detail) for dedup
firm_master_account     string      -- 0008242234
source_file_date        date        -- when TRN was issued; for lag tracking
```

**Partition:** `03_silver/TRN_NNA/date={YYYYMMDD}/data.parquet`.

### Classifier (empirically validated against Schwab PDF to within 85-90% on monthly NNA totals)

```python
INFLOW_SOURCES_DEFAULT_IN  = {'*DEPOSIT', 'DEPOSIT', 'WIRED FUNDS IN'}
BOTH_DIRECTION_SOURCES     = {'TRANSFER ACCOUNT', 'MONEYLINK TRANSFER'}  # direction from detail regex
OUTFLOW_SOURCES_DEFAULT    = {'FUNDS PAID', 'WIRED FUNDS OUT', 'IRS WITHHOLDING'}
EXCLUDE_TRAN_CODES         = {'BKSWP', 'BRSWP', 'DIV', 'QDV', 'TRADE', '$JNL', '$TYPE',
                              'RID', 'DFR', 'INT', 'TPFEE', 'SMFEE', 'MGFEE', 'RDM', 'STOP'}
EXCLUDE_SOURCES            = {'AUTO BANK SWEEP', 'JOURNAL', 'ORD DIV - CASH',
                              'QUALIFIED DIV', 'REINVEST DIVIDEND', 'ORD INC DIV REINV.',
                              'CREDIT INT', 'ADVISOR FEE', 'REDEMP/CONVERSION'}
# Also exclude any description containing 'TRF BTWN SCH' (intra-Schwab, per Schwab NNA def)

# For BOTH_DIRECTION_SOURCES, direction is inferred from the description:
#   detail contains ' TO '   -> outflow
#   otherwise                -> inflow
```

`sub_category` mapping:
- `WIRE`: source `WIRED FUNDS IN`/`WIRED FUNDS OUT`
- `MONEYLINK`: source `MONEYLINK TRANSFER`
- `TOA`: source `TRANSFER ACCOUNT`
- `DEPOSIT`: source `*DEPOSIT`/`DEPOSIT`
- `CHECK`: source `FUNDS PAID`
- `IRS_WH`: source `IRS WITHHOLDING`
- `OTHER`: anything else (should be rare — audit these)

---

## Reconciliation / Enrichment Into canonical_nna

This is the new addition. The existing `C_01.canonical_nna.py` becomes the merge point.

### New input: `03_silver/TRN_NNA/`

Loaded once per run via a thin helper (mirror of `lib/nna_flows.load_flows_from_transactions`), aggregated to `(acct10, trade_date, direction)` grain.

### Merge algorithm (per `trade_date`)

| Schwab-NNA row | BD-silver row | Rule | Tag |
|---|---|---|---|
| present | matching ±2% tolerance same day | use BD (keeps `architect`, `relationship_id`) | `source=bd` |
| present | matching ±2% within ±7d | use BD, log a `lag_days` | `source=bd_lagged` |
| present | matching ±2% within ±180d | use BD, log `lag_days`, flag > 30d for DS review | `source=bd_delayed` |
| present | no BD match anywhere in window | impute from Schwab | `source=schwab_imputed` |
| present | BD amount differs >2% | KEEP BD, ALSO emit Schwab-only delta to diff table | `source=bd_diff_flagged` |
| not present | present | keep BD | `source=bd_only` |

**Anti-double-count guard:** Imputation is idempotent across re-runs. The same `schwab_txn_key` will always resolve to the same output (imputed or superseded by a later-found BD match). When BD does eventually catch up on a previously-imputed event, the re-run supersedes the imputed row and retains only BD. Implementation: the imputed-row emitter takes `{BD history up to run_date}` as input, not `{BD history at time of Schwab event}` — so a BD row posted Mar 2025 for a Schwab event on Dec 2024 will cause the Dec 2024 imputed row to vanish on the next run.

### Output: canonical_nna gets one new column

Extend the existing canonical_nna schema with:

```
source_system   string   -- 'bd' | 'bd_lagged' | 'bd_delayed' | 'schwab_imputed' | 'bd_diff_flagged' | 'bd_only'
```

Everything else stays identical. Downstream D_04 monthly/quarterly/annual rollup, partner_analytics, platinum artifacts — no schema changes required. Optional enhancement: expose `imputed_pct_of_period_nna` in partner_analytics so UI can surface data-quality on periods that lean heavily on imputation.

### Advisor attribution for imputed rows

Schwab TRN does not carry advisor/architect information. Three options; recommending **(a)**:

- **(a) Most-recent BD lookup — RECOMMENDED.** For a Schwab-imputed row on `acct10 = 79128541`, look up BD silver for the earliest `architect` ever recorded for that account and attribute to them. This works for 9 of the 10 worst-gap accounts from the Dec 2024 investigation (all have BD-side architect assigned within 5 months). For accounts that never get assigned, fall back to `Unassigned` and tag as such.
- (b) Synthetic `Onboarding` advisor bucket. Clean but distorts firm view.
- (c) Firm-only attribution, skip advisor dimension for imputed rows. Safest but breaks advisor leaderboards for newly-onboarded books.

Implement (a). Escalate to CTO if the "never-assigned" rate in production >5% of imputed dollar value — would indicate upstream BD relationship mapping is further broken than assumed.

---

## Ingestion Pipeline

Three execution phases. Each runs independently; each is idempotent against its output prefix.

**Phase 1: Bronze sync (on-demand / future Lambda).**
- `data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py` already handles OneDrive -> `01_raw/`. Extend to cover TRN (confirm TRN is already included — if not, 1-line add).
- Future Lambda-on-schedule can replace manual sync once Schwab SFTP delivery is automated. Out of scope for this brief.

**Phase 2: TRN -> Layer A silver (`03_silver/TRN/`).**
- `convert_schwab_trn_to_parquet.py` — already written, never backfilled. Uses `D1|` record-type filter, so header variants (H1/H2/H3) are correctly skipped. No known bug; validation required before backfill.
- Validation step: dry-run on one file, compare `D1|` count to output row count, schema sanity check (all 12 `KEY_FIELD_PATTERNS` resolve to a column; numerics parse cleanly with `+`/`-` prefix handling).
- Backfill all existing `01_raw/CRS*.TRN` (568 files). ThreadPoolExecutor(8) per existing script pattern, idempotent (skips dates already in `03_silver/TRN/`).

**Phase 3: Layer A -> Layer B NNA-classified silver (`03_silver/TRN_NNA/`).**
- New script: `data/black_diamond/scripts/bronze/convert_schwab_trn_to_nna_silver.py`.
- Reads `03_silver/TRN/date=*/`, applies classifier, writes `03_silver/TRN_NNA/date=*/`.
- Runs after Phase 2 each day.
- Backfill all dates on first run.

**Phase 4: canonical_nna enrichment (DS lane, not AE).**
- DS `0.4.0_DS_ClientPlatform` owns `C_01.canonical_nna.py` modifications. AE delivers Phase 1-3 and publishes the schema contract.
- Separate TO after this brief's Phase 1-3 land.

---

## Acceptance Criteria

1. `03_silver/TRN/date={YYYYMMDD}/data.parquet` exists for every `01_raw/CRS*.TRN` file present (backfill complete; gap reports emitted for any STANDARD-tier file that fails).
2. `03_silver/TRN_NNA/date={YYYYMMDD}/data.parquet` exists for every Layer-A partition (Layer-B backfill complete).
3. **NNA parity test:** For each of the six months Jul-Dec 2024, the sum of `gross_amount` from `03_silver/TRN_NNA/` (grouped by `direction`) must be within +/- 15% of the Schwab PDF stated figure for 49 Financial. Jul 2024 target: inflow $43.4M, outflow $15.1M.
4. **Imputation-rate metric:** for each month in the 13-month window May 2024 - May 2025, publish `(inflow_imputed_schwab / total_inflow)` and `(outflow_imputed_schwab / total_outflow)`. Expected inflow imputation rates: ~10-20% typical months, 50%+ in Jun 2024 and Dec 2024. Out-of-band values are the diagnostic.
5. Anti-double-count invariant: running the canonical_nna pipeline twice on the same input produces byte-identical output.
6. Schema contract doc at `docs/data/schwab_trn_nna_contract.md` — column definitions, classifier rules, direction rules, sub_category taxonomy. DS consumes this.
7. pipeline_inventory.xml and data_contract.xml both updated to reference the new silver layers.

---

## Phasing

| Phase | Owner | Deliverable | Dependencies |
|---|---|---|---|
| 0 | 0.6.0_AE | CTO approval of this brief + TO issuance | — |
| 1 | 0.6.0_AE | Confirm OneDrive -> `01_raw/` sync covers all 2025 TRN once user uploads | User uploads |
| 2 | 0.6.0_AE | Fix TRN converter line-3 skip, backfill `03_silver/TRN/` (568 files) | Phase 1 |
| 3 | 0.6.0_AE | New converter `03_silver/TRN_NNA/`, backfill all dates | Phase 2 |
| 4 | 0.6.0_AE | NNA parity test script; run for Jul-Dec 2024 against PDF | Phase 3 |
| 5 | 0.6.0_AE | Publish schema contract doc + update `pipeline_inventory.xml` | Phase 3 |
| 6 | 0.4.0_DS | `C_01.canonical_nna.py` enrichment (separate TO) | Phase 5 |
| 7 | 0.4.0_DE | Surface `imputed_pct` in partner_analytics + portal indicator (separate TO) | Phase 6 |

AE scope ends at Phase 5. Downstream consumer integration is DS + DE lanes.

---

## Out of Scope

- Classifier change for MetLife VA overcount (Jun 2024 ghost accounts). Separate DS fix inside `nna_flows.py`.
- Snowflake / data warehouse export of the new silver layers. Existing bronze/silver on S3 is sufficient for current gold-layer consumers.
- Multi-firm generalization. This brief is scoped to 49 Financial (single TRN master account `0008242234`). Structure generalizes trivially — add a firm dimension to Layer B — but no second firm is in TRN delivery today.
- Schwab SFTP automation (replacing OneDrive manual delivery with scheduled ingest). Follow-up TO.
- Consumer-side portal changes. DE lane after DS integrates.

---

## Open Design Questions — Flag at TO Draft

1. **Attribution fallback precedence.** The brief proposes BD-most-recent-architect for imputed rows. Acceptable as-is, or should CTO approve a different fallback (e.g., attribute to the advisor whose book contains the earliest correlated deposit in a ±30d window)?
2. **Diff-flag threshold.** 2% tolerance on matched rows — reasonable for wire rounding but may swamp DS review queue if MoneyLink amounts vary by fee. Alternate: absolute $100 floor combined with 2% ratio.
3. **Layer B materialization cost.** Full backfill of 568 dates x average ~11K rows = ~6M rows in `03_silver/TRN_NNA/`. Parquet-compressed, ~200 MB. Acceptable per ULN precedent (212K rows / day) but worth a plan check.
4. **DS -> AE contract on merge semantics.** This brief proposes the merge runs inside `C_01.canonical_nna.py` (DS-owned). Alternative: AE publishes a pre-merged `03_silver/NNA_reconciled/` layer and C_01 consumes it directly. The latter keeps DS out of Schwab-specific classifier logic. Flag to CTO.

---

## Related

### Work trace leading to this brief
- **Investigation session log:** `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-21/schwab_trn_nna_enrichment_investigation.md` — full phase-by-phase trace, findings, and TRN sync status
- Investigation memory: `memory/project_schwab_trn_nna_enrichment.md` (agent-scoped persistent memory)

### PoC scripts (saved to prevent wheel-reinvention during TO execution)
- `data/schwab/analysis/README.md` — index + status
- `data/schwab/analysis/trn_nna_classify_poc.py` — PoC TRN parser + NNA classifier (85-90% parity vs Schwab PDF on monthly totals)
- `data/schwab/analysis/reconcile_schwab_bd_nna.py` — PoC account-level cross-reference Schwab TRN vs BD silver with delay-matching

### Existing infrastructure (reused, do not reinvent)
- `data/black_diamond/scripts/bronze/sync_schwab_onedrive_to_s3.py` — OneDrive -> S3 uploader (0.4.0_DS, 2026-04-14)
- `data/black_diamond/scripts/bronze/convert_schwab_trn_to_parquet.py` — existing TRN parser, written but never backfilled (0.6.0_AE, ADHC_HISTRY)
- `data/black_diamond/scripts/bronze/convert_schwab_uln_to_silver.py` — ULN silver producer; pattern precedent for Layer B (0.6.0_AE, 2026-04-17)
- `data/black_diamond/scripts/bronze/convert_schwab_rps_to_silver.py` — RPS silver producer (0.6.0_AE)
- `data/black_diamond/scripts/gold/lib/nna_flows.py` — BD-side NNA classifier; reference for semantic parity (0.4.0_DS)
- `data/black_diamond/scripts/gold/C_01.canonical_nna.py` — gold-layer consumer, will become the merge point per Phase 6 (0.4.0_DS)
- `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` `_build_nna_by_period` — downstream rollup (0.4.0_DS)

### Reference docs
- Reference ULN brief (same shape, prior workstream): `docs/briefs/ae-brief-schwab-uln-silver-ingestion.md`
- Prior ULN AE session log (backfill precedent): `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-17/schwab_uln_silver_ingestion.md`
- Schwab 49 Financial Business Review PDF: `C:\Users\AndrewBerman\Downloads\49 Financial Business Review Dashboard May 2025 1.pdf` (NNA parity ground truth)
- Prior Schwab SoT cross-reference (manual PDF ingestion, March 2026): `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-04/REQ_schwab_sot_cross_reference.md`
