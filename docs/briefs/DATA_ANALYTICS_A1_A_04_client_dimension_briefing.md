# A_04 — client_dimension — DATA_ANALYTICS layer briefing

**Script:** `data/black_diamond/scripts/gold/A_04.client_dimension.py`
**Output:** `gold/dimensions/client_dimension.parquet` (+ legacy dual-write `gold/client_dimension.parquet`)
**Layer / order:** Group A (dimensions); catalog line 83. Dispatched in PHASE_A2 (parallel with A_01). Reads `gold/dimensions/accounts_dimension_latest.parquet` (A_00 output) + a FULL scan of `silver/transactions/`.
**Essential status (Andrew's framework):** ESSENTIAL — `client_dimension` feeds D_01 / D_02 / D_03 / D_04 (the Group-D backward-closure → ADVI/MDPF portal). It is the household/relationship-grain dimension (A_00 = account grain; A_04 = the household roll-up).
**Author/project:** Data Scientist / 2026-02-19 (original); part of the bd gold dimension tier.
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-25 (Andrew-direct A1 layer-walk, resumed). Source-grounded (file:line) + deployed-verified (comp-pipescript deployed = MATCH) + consumer-census grounded (comp-pipescript io + comp-grep on D-tier reads).

---

## 1. What it does

Rolls **account-level** rows up to the **household (relationship) level** to produce the client/household dimension. One row per `relationship_id`. Per household it computes: total/active account counts, modal architect/implementor/city/state/country, tax-bucket flags (`has_taxable` / `has_tax_deferred` / `has_tax_exempt`), the comma-joined `account_types` set, `first_seen_date`, and display names.

- **first_seen_date** comes directly from `accounts_dimension.relationship_first_seen_date` (L238-261) — the txn-derived `groupby min(trade_date)` is only a *fallback* if that column is absent (L264-274).
- **active_accounts** = accounts with a transaction in the **last 90 days** of `max(trade_date)` (L276-287) — this is the ONLY thing the full `silver/transactions/` load is actually used for (given first_seen now comes from A_00).
- **Orphan handling** (L347-369): accounts with no `relationship_id` become synthetic single-account households keyed `acct_<account_id>` — so no account is dropped from the dimension.
- **Tax inference** (L149-183): vectorized keyword classifier on `account_type`/`account_owner_type` fills `tax_status` when silver lacks it (Roth→exempt; 401k/ira/sep/simple/pension→deferred; else taxable).

## 2. Architecture / data flow

1. **Load accounts** (L64-83): `accounts_dimension_latest.parquet` (A_00) — authoritative tax_status + relationship metadata, all accounts 2020-present incl. closed.
2. **Load transactions summary** (L86-142): FULL paginated scan of `silver/transactions/*.parquet`, narrow column set; deterministic total-order dedup on `transaction_id` (the ADHC_GLDINC CLASS-N oracle-fix pattern, mirrored verbatim from A_01's 73ec87a84 remedy — index-slot assembly + sort before `keep='last'`, so survivors don't depend on thread-completion order).
3. **Build** (`build_client_dimension`, L216-424): infer tax → derive first_seen + names → 90-day active flag → groupby-relationship agg (counts + tax flags) → modal architect/implementor/location via `modal_by_group` → orphan synthesis → merge names → metadata stamps → column order + sort.
4. **Save** (L431-453): write canonical `gold/dimensions/client_dimension.parquet`; **dual-write** the legacy `gold/client_dimension.parquet` via the `LEGACY` map.

## 3. Recompute posture — FULL EVERY NIGHT (the lone Group-A straggler post-A_01-flip)

- **Catalog = `A_04|A_04.client_dimension.py|--upload`** (line 83) — NO `--incremental`. And `INCREMENTAL_CAPABLE="A_00 A_02 C_06"` (line 909) — **A_04 is not incremental-capable; it has no incremental code path at all** (only `--dry-run` / `--upload`).
- The script **full-scans every `silver/transactions/` partition (2020-03→present, thousands of files)** on every nightly run — yet that load serves ONLY the 90-day `active_accounts` flag (first_seen_date now comes from A_00; the txn-derived first_seen is a near-dead fallback). **This is the dominant cost and an unnecessary full-history read for a recent-window-only signal.**
- After the A_01 full→incremental flip (deployed by AE, 316202d69), **A_04 is the lone remaining Group-A full-recompute offender.** It differs from A_01/A_02 in KIND: A_04 is a **full-rebuild dimension** (recomputes the whole household table each run), not an SCD-append — so the right "incremental" here is **scoping the transactions read to ~last 90-100 days** (the active-flag window), NOT change-point caching. A full *rebuild* of the dimension off the (small) accounts table is cheap; the transactions full-scan is the waste.
- Output rebuild is order-deterministic (final `sort_values('relationship_id')`, L415) — safe to window the transactions read without changing the survivor set.

## 4. Tech debt

- **FULL silver/transactions scan for a 90-day flag** (L86-142, L276-287): read only the recent partitions (`>= max_date − ~100d`, or a bounded tail of sorted keys) instead of 2020-present. Largest, safest optimization; turns A_04's runtime from O(all-history) to O(recent-window). The deterministic-dedup machinery (`_file_date`/`_intra_pos`) becomes trivially cheaper too.
- **DEAD CODE — `modal_value` (L186-192):** scalar mode helper, **def-only, zero call sites** (the live path is the vectorized `modal_by_group`, L195-209). Drop in A2.
- **Near-dead first_seen_date txn-fallback (L264-274):** only fires if `relationship_first_seen_date` is absent from A_00 — which it is not. If the transactions read is windowed (above), this fallback would silently degrade (a windowed min(trade_date) ≠ true first-seen) — so when windowing, **gate the fallback off / assert the A_00 column present** rather than letting a windowed read feed it.
- **`/tmp` staging write (L436):** writes `/tmp/client_dimension.parquet` then uploads — fine on the EC2 gold runner; would crash on a read-only Lambda fs (not the deploy target here, noted for parity with the banked Lambda-readonly-fs gotcha).

## 5. Drop-list TRAP — the dual-write is LOAD-BEARING (do NOT naive-drop)

- A_04 dual-writes: canonical `gold/dimensions/client_dimension.parquet` AND legacy `gold/client_dimension.parquet` (LEGACY map, s3_layout.py L313).
- **Consumers are SPLIT across the two paths** (comp-pipescript io + comp-grep on D-tier):
  - `D_02.advisor_client_detail.py` reads the **canonical** `gold/dimensions/client_dimension.parquet`.
  - `D_01.partner_analytics.py`, `D_03.composition_artifacts.py`, `D_04.client_portal_summary.py` read the **legacy** `gold/client_dimension.parquet`.
- **Therefore the legacy dual-write canNOT be dropped until D_01/D_03/D_04 are repointed to `gold/dimensions/`.** This is exactly the silent-LIVE-surface-degradation trap the A1 consumer-census exists to catch. Flag for A2: a coordinated repoint-then-drop (DS edits D_01/D_03/D_04 read paths; verify served; then remove the legacy write).

## 6. Bullshit / overfit
- None egregious. **No hardcoded single-entity hacks** (unlike A_01's `Olivia Shin`). The tax-keyword inference is a reasonable silver-gap backfill; the orphan synthesis is defensible (keeps every account representable). The denormalization here is honest household aggregation, not 49F-overfit.

## 7. What's GOOD (keep)
- **Deterministic dedup** (total-order sort before `keep='last'`) — the A_01 CLASS-N oracle-fix applied correctly here, so the full-rebuild is reproducible night-to-night.
- **first_seen sourced from A_00** (not re-derived) — the right dependency direction; A_00 owns relationship_first_seen_date.
- **Orphan accounts preserved** rather than dropped — no silent account loss into the household dimension.
- **Modal aggregation is vectorized** (`modal_by_group`) — no per-row `iterrows` (the kind of dead per-account builder A_02 still carries).

## 8. Actions

| When | Action | Owner |
|---|---|---|
| A2 / incremental sweep | Window the `silver/transactions/` read to ~last 100 days (the active-flag window) — kills the full-history scan; A_04 stops being a full-recompute offender | DS |
| A2 | DELETE dead `modal_value` (L186-192) | DS |
| A2 | When windowing the txn read, gate/assert-off the first_seen txn-fallback (L264-274) so a windowed min(trade_date) can never feed `first_seen_date` | DS |
| A2 (coordinated) | Repoint D_01/D_03/D_04 from legacy `gold/client_dimension.parquet` → canonical `gold/dimensions/client_dimension.parquet`, verify served, THEN drop A_04's legacy dual-write | DS (+ D-tier) |
| — | Essential tag: KEEP — Group-D closure, ADVI/MDPF portal | — |

## 9. Status / ledger row

- **Tag: ESSENTIAL** (Group-D backward-closure → ADVI/MDPF portal; the household-grain dimension complementing A_00's account grain).
- **Recompute: FULL-RECOMPUTE OFFENDER** — the lone Group-A straggler after the A_01 flip; fix = window the transactions read (NOT SCD-caching; A_04 is a full-rebuild dimension). Cheap, deterministic, safe.
- **Drop-list: NO drop** — dual-write is load-bearing (split consumers); legacy write retires only after a coordinated D_01/D_03/D_04 repoint.
- **Cleanliness: GOOD** — deterministic, no entity-overfit hacks; only real debt = the full-scan + dead `modal_value` + the split-path dual-write coupling.

### Ledger entry (for the A1 transformation-ledger)
| Script | Output | Consumers | Tag | Recompute | Notes |
|---|---|---|---|---|---|
| A_04.client_dimension | gold/dimensions/client_dimension.parquet (+legacy gold/client_dimension.parquet) | D_01, D_02, D_03, D_04 (Group-D → ADVI/MDPF) | ESSENTIAL | FULL (not incremental-capable; lone Group-A straggler) | window txn read; drop dead modal_value; split-path dual-write load-bearing (repoint before drop) |
