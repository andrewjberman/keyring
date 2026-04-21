# Schwab TRN — 1st/2nd Order Transaction Enrichment Feasibility

**Author:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-21
**Driver:** Andrew, 2026-04-21: "priority is the most complete transactions history as possible,
so if we can enrich 1st and 2nd order transactions tables, thereby enriching gold, that is
what we want to assess feasibility and implementation" — focus is 49 Financial NNA, not
Schwab PDF parity.
**Supersedes:** `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md` Phase 6 scope
(expands from gold-only merge into upstream silver enrichment).

---

## TL;DR

**Feasibility: HIGH.** The join key already exists for free — BD
`original_account_number` equals the Schwab 8-digit account number (zero-stripped). 84% of
BD accounts already overlap with Schwab's account master. A new silver layer
`silver/transactions_enriched/` can union BD + Schwab-imputed rows with explicit
`source_system` tagging. Downstream gold scripts cut over by changing one read path.

Concrete scope (Jul-Dec 2024): 1,642 Schwab-only (acct, date) pairs totaling $91.3M of
inflows BD misses today. Jessica Lindsey SHORT TRUST (Schwab acct `79128541`, $20.1M wire
2024-12-31) has zero BD records — ever. This is exactly the hole to fill.

---

## Cross-reference evidence

### Account-ID mapping is already present

BD silver/transactions `original_account_number` is an 8-character zero-stripped Schwab
account number:

| BD column `original_account_number` | Schwab ACC `account_id` (padded) | Schwab TRN `acct10` |
|-------------------------------------|----------------------------------|---------------------|
| `79128541` | `0079128541` | `79128541` |
| `33823043` | `0033823043` | `33823043` |
| `38836097` | `0038836097` | `38836097` |

**Overlap test on Dec 2024 BD silver (3,991 unique BD accounts):**

- BD `original_account_number` ∩ Schwab `acct10` = **3,366 accounts (84%)**
- Remaining 16% of BD accounts are either non-Schwab custody (held-away) or format variants
- Reverse direction (Schwab ACC 6,753 accounts): ~50% present in BD on any given day
  (expected — Schwab ACC holds all 49F accounts across time; BD holds active book)

### Schwab ACC gives us cross-reference attribution

`silver/ACC/date={YYYYMMDD}/data.parquet` per-date snapshot has:
- `account_id` (padded), `master_account_number` (`0008242234` = 49F)
- `account_title_1/2/3` — client name/account name/cohort
- `taxpayer_first_name`, `taxpayer_last_name`, `ssn_tin` — identity join
- `manager` — Schwab's view of the managing advisor
- `state` — client state

### Worked example — Jessica Lindsey recovery

- **Schwab ACC 2026-04-20:** acct `0079128541` / `JESSICA A LINDSEY TTEE` / `JESSICA A. LINDSEY 2019 RESTAT`
- **Schwab TRN 2024-12-31:** `DPWRF` inflow $20.1M (WIRED FUNDS RECEIVED)
- **BD silver for `original_account_number=79128541`:** 0 rows, any date
- **BD only has:** account `38836097` (`Lindsey, Jessica - Long Trust brokerage`) — a DIFFERENT account

BD literally doesn't see the SHORT TRUST at all. Enrichment synthesizes BD-schema rows for
this account tagged `source_system='schwab_imputed'` with attribution inherited from the
other Jessica Lindsey account we do have.

---

## Proposed Architecture

Four layers, all additive. No destructive writes to existing BD or Schwab silver.

```
Schwab silver/ACC          -- existing, per-date master
Schwab silver/TRN          -- existing, Layer A (bea387a9)
Schwab silver/TRN_NNA      -- existing, Layer B (bea387a9)

NEW Schwab silver/account_xref   -- [Phase 1]
NEW BD silver/transactions_enriched   -- [Phase 2]
```

### Phase 1 — `schwab_bd_account_xref` (1st-order key layer)

**Purpose:** one-row-per-account cross-reference with attribution fallbacks.

**Location:** `s3://opal-data-schwab/03_silver/account_xref/date={YYYYMMDD}/data.parquet`
(daily refresh; `date=latest` symlink for convenience)

**Schema:**

| Column | Source | Notes |
|--------|--------|-------|
| `acct10` | Schwab ACC stripped | Primary key |
| `schwab_padded_id` | Schwab ACC `account_id` | `0079128541` form |
| `schwab_master_account` | Schwab ACC | `0008242234` = 49F |
| `schwab_account_title_1/2/3` | Schwab ACC | Client / account name |
| `schwab_taxpayer_name` | Schwab ACC | first + last |
| `schwab_manager` | Schwab ACC | Schwab's advisor label |
| `schwab_state` | Schwab ACC | |
| `bd_account_id` | BD silver LATEST | `z0818927251` form (BD's internal) |
| `bd_account_number` | BD silver LATEST | Maps to Schwab padded when BD has it |
| `bd_relationship_id` | BD silver LATEST | For architect attribution |
| `bd_architect` | BD silver LATEST | Most-recent non-null architect |
| `bd_client_name` | BD silver LATEST | For fuzzy fallback matching |
| `bd_first_seen_date` | BD silver | Earliest BD sighting (lifecycle indicator) |
| `bd_last_seen_date` | BD silver | Latest BD sighting |
| `status` | derived | `bd+schwab` / `schwab_only` / `bd_only` |
| `as_of` | current date | Refresh timestamp |

**Producer:** `data/black_diamond/scripts/bronze/build_schwab_bd_account_xref.py` (new).
Joins Schwab ACC (latest) + BD silver LATEST `original_account_number` unique values +
most-recent architect/relationship lookup. Runs nightly after BD silver refresh.

**Fallback strategy for `schwab_only` accounts (no BD record):** name-fuzzy-match to BD
via `taxpayer_name` ↔ `client_name` within the same `bd_relationship_id` family. If
match, inherit architect. If no match, tag architect as `Unassigned` for the imputed row.

### Phase 2 — `silver/transactions_enriched/` (1st-order enrichment)

**Location:** `s3://opal-data-bd/silver/transactions_enriched/date={YYYY-MM-DD}/data.parquet`

**Schema:** identical to `silver/transactions/` **plus** one column:

| Column | Values |
|--------|--------|
| `source_system` | `bd` \| `bd_lagged` \| `bd_delayed` \| `schwab_imputed` \| `bd_diff_flagged` \| `bd_only` |

**Producer:** `data/black_diamond/scripts/silver/enrich_transactions_with_schwab.py` (new).
Per date:

1. Read `silver/transactions/{date}.parquet` (authoritative BD)
2. Read `03_silver/TRN_NNA/date={date}/data.parquet` (Schwab classified)
3. Read `03_silver/account_xref/date=latest/data.parquet`
4. For each Schwab row, map `acct10` → BD account via xref; check for BD match:
   - ±2% amount AND same day → tag BD row `source_system='bd'`, drop Schwab (dedup)
   - ±2% amount within ±7d → tag BD row `bd_lagged`, drop Schwab
   - ±2% amount within ±180d → tag BD row `bd_delayed` + `lag_days` attribute, drop Schwab
   - > 2% amount diff on same day → tag BD `bd_diff_flagged`, emit Schwab delta as separate
     reference row
   - No BD match in ±180d → synthesize BD-schema row tagged `schwab_imputed`
5. All remaining BD rows with no Schwab counterpart → tag `bd_only`
6. Write union to enriched partition

**Synthesis rules for `schwab_imputed` rows** (mapping Schwab TRN_NNA → 79-col BD schema):

| BD column | Derivation |
|-----------|-----------|
| `transaction_id` | `SCHWAB_{schwab_txn_key}` (stable, deterministic) |
| `trade_date`, `settle_date` | From Schwab TRN |
| `action` | `Deposit` (inflow) / `Withdrawal` (outflow) |
| `transaction_type` | Map from `sub_category`: `Wire` / `ACH` / `Transfer of Assets` / `Check` |
| `transaction_sub_type` | sub_category |
| `external_flow` | `yes` |
| `description` | Schwab `transaction_source` + ` - ` + `transaction_detail[:64]` |
| `price`, `units` | From TRN (price only useful for cash-equivalent) |
| `market_value` | Schwab `gross_amount` |
| `account_id`, `account_number`, `original_account_number` | From xref |
| `account_name`, `client_name` | From xref Schwab ACC |
| `relationship_id`, `relationship_name` | From xref BD-latest (fallback `SCHWAB_IMPUTED`) |
| `architect` | From xref BD-latest (fallback `Unassigned`) |
| `manager`, `additional_advisor`, splits | From xref BD-latest or defaults |
| `is_nna`, `is_nna_inflow`, `is_nna_outflow` | Computed from TRN direction |
| `is_new_client` | True if BD-first-seen-date > trade_date (or acct is schwab_only) |
| `cusip`, `asset_id` | None (cash events don't have cusip; in-kind skipped for v1) |
| `_source_file` | `schwab:CRS{YYYYMMDD}.TRN` |
| `_ingested_at` | Run timestamp |
| All other 40+ cols | None / default |

**Idempotency:** deterministic `transaction_id` means reruns are byte-identical. If BD
catches up on a date later, the next run re-evaluates and demotes the Schwab row to
`bd_delayed` (replaced by real BD row).

### Phase 3 — 2nd-order gold enrichment (consumer cutover)

Gold scripts that read BD silver/transactions flip their read path:

| Gold script | Current source | New source | Owner |
|-------------|----------------|------------|-------|
| `C_01.canonical_nna.py` | `silver/transactions/` | `silver/transactions_enriched/` | 0.4.0_DS |
| `lib/nna_flows.py` (helper) | same | same | 0.4.0_DS |
| `C_02.canonical_flows.py` or similar | same | same | 0.4.0_DS |
| Any other transactions consumer | audit via `comp-blast` | same | varies |

Read path change is a 1-line swap with an environment-flag fallback for safe cutover:

```python
TX_SOURCE = os.environ.get('TX_SOURCE_LAYER', 'silver/transactions')  # migrate: 'silver/transactions_enriched'
```

**DS Phase 6 (per brief) moves UP into Phase 2.** Gold-layer merge becomes unnecessary —
the union happens in silver, so gold just sees one table with a `source_system` column.
Simpler DS code, one less merge point.

### Phase 4 — Ops

- **Daily cadence:** account_xref and transactions_enriched run after BD silver refresh
- **Backfill scope:** all dates 2024-04-12 onward (range of Schwab TRN_NNA silver)
- **Validation harness:** compare enriched vs plain silver — row count by source_system,
  total inflow/outflow dollar by month, schwab_imputed concentration (top-10 accts/month)
- **Regression gate:** `count(bd) + count(schwab_imputed) >= count(silver/transactions)`
  per partition; imputation rate ≤ 50% of any month's inflow (hard flag if exceeded)

---

## Anticipated Impact

### Transactions coverage

Enriched silver gets new rows where BD is blind:
- **Jul-Dec 2024 window:** 1,642 imputed (acct, date) events; ~$91M of inflow
- **Per-month imputation share:** 10-40% of inflow depending on month
- **Account coverage:** previously invisible accounts like Jessica Lindsey SHORT TRUST
  become visible in every downstream consumer

### Gold-layer impact

- `canonical_nna` monthly/quarterly/annual NNA figures shift upward by the imputed amount
- `positions_cube` and lifecycle tracking get earlier first-seen dates for new 49F accounts
- Architect leaderboards see rebalanced contribution if fallback attribution resolves to
  the correct architect
- Portal charts (Monthly NNA, Firm Overview) no longer undercount in onboarding-lag months

### Non-goals

- We do NOT try to match Schwab's position-delta NNA. That's Schwab's internal metric on
  their book, not 49 Financial's business reality (held-away accounts, non-Schwab
  custodians, etc.).
- In-kind ACAT valuation stays **out of scope for v1.** Cash + wire + ACH + check = 80% of
  the value. Price-join for in-kind securities introduces overcounting risk (see
  `ae-schwab-trn-nna-coverage-gap-methodology.md` for evidence). v2 candidate.

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| 16% of BD accounts don't map to Schwab 10-digit (probably held-away METVA_* or non-Schwab). | These are BD-only; unaffected by enrichment. `bd_only` tag preserves them. |
| Schwab-only accounts (closed/onboarded mid-window) need architect fallback | Xref Phase 1 fallback logic (taxpayer-name → BD relationship_id). Tag `Unassigned` if fallback fails. |
| Synthetic rows have None for ~40 columns → downstream scripts may break on null architect | Inventory null-sensitive scripts via `comp-blast` before cutover. Patch each to handle `source_system != 'bd'` gracefully. |
| 2% diff-flag threshold spams DS review queue | Tune after v1 backfill — absolute $100 floor alongside %. |
| Dual ingestion race: BD silver refreshes mid-enrichment run | Atomic write to `_tmp` key + S3 rename (standard pattern). Enricher locks on current silver partition list. |
| BD re-ingestion replaces a prior-imputed event with its own row — need re-run | Enricher is idempotent; next nightly re-run demotes imputed → `bd_delayed`. |

---

## Implementation Plan

| Phase | Deliverable | Owner | LOE |
|-------|-------------|-------|-----|
| 1 | `build_schwab_bd_account_xref.py` + daily `account_xref` partition + xref validation report | 0.6.0_AE | ~1 day |
| 2 | `enrich_transactions_with_schwab.py` + `transactions_enriched` layer + backfill 2024-04-12 onward | 0.6.0_AE | 2-3 days (schema map is the heavy part) |
| 3a | DS migrates `C_01.canonical_nna.py` to read enriched; replaces brief's Phase 6 merge | 0.4.0_DS | 1 day (simpler than original Phase 6) |
| 3b | Audit other gold consumers via `comp-blast silver/transactions`; migrate each | joint DS+DE | 2 days |
| 4 | Validation harness + nightly ops + cutover monitoring | 0.6.0_AE | 1 day |

**Total path to production:** ~1 week elapsed (parallelizable across DS + AE).

---

## Open Questions (flag to CTO)

1. **Enriched layer as read-through vs primary.** Do we eventually deprecate
   `silver/transactions` and have enriched be the only silver, or do we keep both forever
   with different consumers? Recommend: keep both, enriched is consumer-facing, plain is
   audit trail for BD-authoritative view.

2. **Architect fallback for Schwab-only accts.** Name-fuzzy-match (recommended) vs
   synthetic `SCHWAB_ONBOARDING` architect bucket vs skip-advisor-dimension? Impacts
   architect leaderboards for newly-onboarded books. Need decision before Phase 1 ships.

3. **Held-away / non-Schwab accounts.** Out of this scope entirely — they stay in BD
   silver as-is, tagged `source_system='bd_only'` in enriched. OK?

4. **Diff-flag threshold (2% vs 2%+$100 floor).** Tune post-v1 from actual volume.

5. **In-kind ACAT valuation follow-up.** v2 candidate: price-join against RPS with a
   "safe" tran_code whitelist (exclude intra-account journals). Separate TO.

---

## Related

- Coverage-gap methodology: `docs/briefs/ae-schwab-trn-nna-coverage-gap-methodology.md`
- Original enrichment brief: `docs/briefs/ae-brief-schwab-trn-nna-enrichment.md` (Phase 6
  supersession documented there on approval)
- Layer A/B contract: `docs/data/schwab_trn_nna_contract.md`
- Investigation trace: `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-21/schwab_trn_nna_enrichment_investigation.md`
