# GLDINC P1 — `load_flows` watermark plumbing-proof — design brief

**Author:** 0.6.0_AE_PartnerETL (GLDINC LEAD) · **Date:** 2026-06-08
**Status:** ENDORSED by CTO 2026-06-08 with one required correction now folded in (cache grain = PER-EVENT, not daily — §3/§4); COO endorsement pending. Build on COO GO.
**PRD anchor:** `docs/architecture/ADHC_GLDINC_PRD.md` §5 (hidden full-scan), §5a (unifying primitive), §4b (parity machine), §6 P1 row
**Predecessors:** P0 CHECKPOINT (`f815db45e`, validated-live 6/6–6/7) · NFRA W2a telemetry (`a4062e09c`, RAVC-closed)

---

## 1. What P1 is (and is not)

P1 is the **plumbing-proof**: it proves the **watermark + shadow + parity-scorecard machinery** end-to-end on the **lowest-risk** script, where the incremental output is **identical to the oracle by construction** so the diff is trivial. It is the FIRST shadow/parity phase → it **activates the GLDINC daily-watch obligation** (COO `/drive` attests `gold/_parity/load_flows/{run_date}/scorecard.json` daily through 2026-07-05).

It is **NOT** a production cutover. The oracle (the existing full-scan) **serves throughout**. P1 ships a SHADOW that runs **after** the oracle on the existing nightly runner (§4b P1 — no new EC2; the unchanged memory profile still needs the big box), writes to a non-served `_parity` prefix, and emits a numeric scorecard. Cutover is a **separate, Andrew-gated** step after **≥5 consecutive clean-night scorecards** (all §4b targets met).

## 2. The target (verified anchor)

`lib/nna_flows.py:87 load_flows_from_transactions(max_workers=128)` paginates the **entire** `silver/transactions/` prefix every call (lines 100–105) and reads every `.parquet` in parallel — a genuine engineering full-scan with **no date arg**. Consumers (each a fresh full-scan, no inter-script cache):

| Script | Call sites |
|---|---|
| `C_01.canonical_nna.py` | :783, :861 (×2) |
| `C_02.client_performance.py` | :269 |
| `C_03.account_performance.py` | :156 |

→ **~4 full-scans of `silver/transactions/` per nightly.** P1's win is a pure I/O cut shared across all three scripts.

## 3. The one real correctness subtlety (must be designed for, not glossed)

`load_flows_from_transactions()` is **NOT** a pure per-partition map. After loading + static exclusions + flow classification, it applies an **AUA-dependent garbage filter** (`_load_latest_silver_aua()` → per-event `|market_value| > 10× account's CURRENT silver AUA` ⇒ excluded; `nna_flows.py:248+`). The full-scan re-evaluates **every historical event against TODAY's silver AUA each night**. A naïve "cache old days' final flows + append new days" design would **freeze** old days against stale AUA → **divergence** whenever an account's AUA crosses a garbage threshold relative to a historical event. Same caveat for `load_nna_transaction_exclusions()` (a current-state (account,date) blocklist).

**Resolution — cache at the AUA-invariant PER-EVENT boundary (CTO correction 2026-06-08).** The garbage filter is **per-event** (`nna_flows.py:250` `_event_mv = max(daily_inflow,daily_outflow)` → `:257-259` mask → `:280` drop), applied BEFORE the daily `groupby` at `:285`. Caching at the daily-aggregated grain is therefore **NOT byte-identical** — a day of several sub-threshold events vs one over-threshold event of the same daily sum are treated oppositely by the oracle, and a daily aggregate cannot reproduce that. The cache grain must match the filter grain = **per-event**. Two further per-event/whole-set operations are likewise state- or cross-partition-sensitive and must run over the union, not be baked into the cache: the **composite dedup** (`:145-149`, keyed `account_id,trade_date,type_col,_mv_abs` — a duplicate whose twin straddles the watermark by FILE date but shares a trade_date would survive a cache-side dedup) and the **(account,date) txn-date exclusions** (`:227-242`, a CURRENT-state blocklist). Cleanest fully-correct boundary: cache the **minimal RAW per-event columns** for `date ≤ watermark` and re-run the entire cheap CPU pipeline over the union each night.

Each night:
1. Window-read only `silver/transactions/` partitions with `date > watermark` (the dominant I/O cost — re-reading + re-parsing ~1764 parquet files for `date ≤ watermark` is exactly what's saved).
2. Extract the minimal per-event columns from the new partitions at the **TRULY-RAW boundary — right after the sorted parallel-read concat (`:122-124`), BEFORE the `:128` transaction_id dedup and BEFORE the `:131-132` coercion+`dropna`**: `{account_id, trade_date (raw, uncoerced), transaction_id, transaction_type/action, action, market_value, description}` + a `source_order_key` (partition key + intra-file row index) for the order-stability re-sort. RAW because the oracle's `:128` dedup (`keep='last'`) runs BEFORE the `:132` dropna — a null-field row can WIN the dedup then be dropped, net-suppressing its non-null twin; a post-dropna cache has already lost that null winner → re-running dedup over the union would wrongly keep the twin (trap 4, DS 2026-06-08).
3. **Union** with the cached truly-raw per-event rows for `date ≤ watermark` (`preflt_events.parquet`), then **re-sort by `source_order_key`** to reproduce the oracle's global-sorted-key concat order before any dedup.
4. Run the **whole transform from `:128` over the full union** exactly as the oracle: transaction_id dedup → coercion+dropna → composite dedup → action/desc static exclusions → flow classification → txn-date exclusions → **per-event AUA garbage filter** (vs CURRENT silver AUA) → `groupby(trade_date,account_id).sum()` → return. All cheap CPU on the in-memory union.
5. Result = **byte-identical to the full-scan by construction**, because every cross-event, order-dependent, and state-dependent step (dedup, dropna, exclusions, AUA filter) runs over the complete RAW event set every night in the oracle's exact order. Dominant transaction-read I/O is cut for all dates `≤ watermark`.

This per-event grain is the substantive engineering of the plumbing-proof; the shadow scorecard **empirically confirms** the byte-identity and would catch any miss in this reasoning on night 1.

**Implementation gotcha — dedup order-stability (must handle at build).** Both dedups (`:128-129` transaction_id `keep='last'`; `:145-149` composite `keep='last'`) are **row-order-dependent**. The oracle concatenates partitions in **global sorted-key order** (`:100-105` `sorted(keys)` → `dfs[index]`). A naïve windowed union (cached-block ++ new-block) can present a different row order whenever a new partition's KEY sorts before a cached key (file naming not strictly monotonic with date — e.g. the `bd_transactions` bulk file vs daily partitions), making `keep='last'` retain a different duplicate → divergence. **Fix at build:** persist each cached event's source partition key, and re-sort the union by (source_key, intra-file row index) to reproduce the oracle's exact concat order before the dedups run. To guarantee the shared transform is byte-identical, **refactor the oracle's post-read transform (`:128-293`) into a single pure helper `_transform_events_to_daily(txns)` that BOTH the oracle and windowed paths call** — never duplicate the logic (drift = divergence). The shadow scorecard is the empirical backstop for exactly these order/dedup traps.

## 4. Watermark object + lifecycle

- **Object:** `s3://opal-data-bd/gold/_state/load_flows/watermark.json` — `{ "max_partition_date": "YYYY-MM-DD", "partition_fingerprint": {<key>: <LastModified ISO>}, "cache_key": "gold/_state/load_flows/preflt_events.parquet", "updated_at": ISO }`.
- **Cache:** `s3://opal-data-bd/gold/_state/load_flows/preflt_events.parquet` — the minimal **TRULY-RAW per-event** rows (`account_id, trade_date` raw/uncoerced, `transaction_id, transaction_type/action, action, market_value, description` + `source_order_key`) for all dates `≤ max_partition_date`, snapshotted **before `:128` dedup and before `:132` dropna**. PER-EVENT + PRE-DEDUP + PRE-DROPNA so every cross-event/order/state op (transaction_id dedup, dropna, composite dedup, exclusions, AUA filter) re-runs over the union and reproduces the oracle exactly (CTO per-event correction + DS trap-4 raw-boundary, 2026-06-08).
- **Restatement awareness (P1-scope = DETECT-and-fall-back, not yet incremental-repair):** `partition_fingerprint` records each processed partition's `LastModified`. If any partition for `date ≤ watermark` shows an advanced `LastModified` (a restatement, per the §5a unifying primitive), the windowed path **falls back to a full-scan for that run and rebuilds the cache** — guaranteeing correctness while the incremental-repair of restatement is deferred to its own phase (§5/§5a). The scorecard records fallback events. This keeps P1 strictly zero-correctness-risk.
- **Both paths use CURRENT-version metadata only** (R2-lifecycle-robust; no version history).

## 5. Shadow harness + scorecard (§4b P1)

- New `lib/nna_flows.py` gains `load_flows_from_transactions_windowed(watermark)` alongside the unchanged oracle entry point. The oracle is untouched and remains the served path.
- The shadow runs **after** the oracle in the nightly (existing runner), writes the incremental output to `s3://opal-data-bd/gold/_parity/load_flows/{run_date}/incremental.parquet` (**never a served key**), and diffs vs the oracle output.
- Emits `s3://opal-data-bd/gold/_parity/load_flows/{run_date}/scorecard.json` per §4b, per output artifact: `key_set_symmetric_diff` (→0), `row_count_delta` (→0), `exact_match_rate` (→100.000%), `within_epsilon_rate` + `max_abs_diff` + `max_rel_diff` (frozen epsilon; a max that must GROW = divergence signal, re-review never widen), `headline_metric_diffs` (total inflow/outflow/implied-NNA, account count — →0/within-epsilon), `clean_night_counter` (consecutive all-green nights, →≥5), plus a `restatement_fallback` flag.
- **Scorecard emission is the daily_watch deliverable** COO attests via `/drive` through 2026-07-05.

## 6. Acceptance + cutover gate

1. Scorecard `clean_night_counter ≥ 5` consecutive nights with ALL §4b targets met.
2. No unresolved `restatement_fallback`-masked divergence (a fallback night is clean by definition; a non-fallback night with diff ≠ 0 is a STOP).
3. Cutover (swap the 3 consumers to the windowed entry point) is a **separate Andrew-gated** step; oracle serves until then.
4. Top-of-month (2026-07-01) bracket T−3…T+3 is **not P1-gating** (load_flows has no freeze-baseline), but the daily scorecard keeps running across it as steady-state evidence.

## 7. P2 fold-in (per COO RAVC2 ruling 2026-06-08)

The **empirical byte-identical resume==fresh** check for P0 (deferred — a manufactured resume run = banned ad-hoc compute) is folded into **P2 as an explicit AC**: the P2 dedicated small auto-shutoff EC2 parity-machine runs a shadow anyway, so a resume-vs-fresh byte-identical comparison rides along at **zero marginal cost**. Captured opportunistically on a natural mid-chain death if one occurs before P2. → carried into the P2 staging TO.

## 8. Cost posture

Zero ad-hoc bd-gold runs. P1 shadow rides the **existing scheduled nightly** (sequenced after the oracle on the same runner). The added shadow read is windowed (cheap); the added compute is the diff + scorecard (trivial). Validated on scheduled nightlies only, per the standing NFRA cost-governance constraint.

## 9. Staging deliverables (this session)

- This brief.
- TO `ADHC_GLDINC.P1.ae-load-flows-watermark-plumbing-proof.md` (status `staged` — awaits COO/CTO endorsement GO, then build).
- On endorsement: implement `load_flows_from_transactions_windowed()` + watermark/cache lifecycle + shadow harness + scorecard emitter; deploy to `code/gold/` ahead of a nightly; validate the FIRST scorecard on the next scheduled nightly (zero ad-hoc).
