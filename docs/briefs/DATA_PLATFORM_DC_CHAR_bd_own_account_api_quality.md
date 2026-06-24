# DATA_PLATFORM DC-CHAR — BD own-account API-quality characterization (the partner-quality signal)

**TO:** DATA_PLATFORM.DC-CHAR (per-vendor; this = the BD supplant-side slice) · **Lane:** 0.4.0_DS_ClientPlatform~B · **Lead/integrator:** 0.4.0_DS_ClientPlatform (validate-fold)
**Date:** 2026-06-24 · **Status:** BD-char COMPLETE (Orion-char next, sequential; Eclipse-char GATED). RAVC2 base-DS+COO+CTO; CVO ROE-verifies.
**ROE:** OPTION-B compliant — and STRONGER: this characterization generated **ZERO BD-vendor traffic** (pure analysis of already-delivered exports in our S3 + S3 object metadata; no BD endpoint hit). our-data-only / read-never-scan / polite (no traffic) / authorized — the HARD-EXCLUDED tier (fuzz/brute/auth-test/out-of-account) is untouched.
**Method:** RECON-RIGOR evidence-schema per dimension -> feeds the 6-dim partner-scoring (API-maturity + operational-maturity) -> BD supplant cost-to-work-around.

---

## INTERFACE MODEL (the framing that bounds the other dims)
- **Observation:** BD's "API" to us is a **batch FILE-EXPORT delivery** (DataMining `*.xlsx` landing in `forwardfill_v2/{allocations,assets,transactions,realized,unrealized}` via SSM `opal-bd-*-download` on schedule), NOT a queryable/paginated programmatic API we session into.
- **Evidence:** advi-bd thread (5 EventBridge-cron SSM download jobs -> EC2 -> silver parquet); the 5 forwardfill_v2 delivery prefixes; no BD query-API in the estate.
- **Inference:** pagination/cursor/rate-limit/throttle semantics are **N/A by delivery model** — there is no request/response API surface to characterize; the operative dims are export schema/freshness/completeness/identifier.
- **CONFIDENCE:** HIGH (source-confirmed from the pipeline graph). **ALTERNATIVE:** BD *does* expose a live API (Advent APX/BD REST) we simply don't use — possible, but out of our own-account ROE scope (we hold the file feed). **Business-significance:** BD's value to us is a managed data-DELIVERY + firm-config HOSTING, not a sophisticated API — directly lowers the supplant cost (replicating a file feed << replicating a rich API).

## Dim 1 — SCHEMA-CONSISTENCY (API-maturity)
- **Observation:** export column-sets are STABLE day-to-day (allocations 92 / assets 31 / transactions 73 cols), no drift across 6 consecutive partitions (2026-06-11..06-18). BUT the schema carries **~10 duplicate-suffixed column pairs** in allocations (basis_points/_1, flat_fee/_1, fee_schedule_level/_1, fee_schedule_rate_type/_1, fee_schedule_type/_1, fee_schedule_description/_1, upper_range/_1, lower_range/_1, history_start_date/_1, reporting_target_description/_1).
- **Evidence:** multi-date column-set diff (STABLE); the 92-col allocations dump (chunk-2).
- **Inference:** schema is STABLE (good — no breaking drift) but LOW-HYGIENE (the `_1` pairs flatten two grains into one row, forcing the consumer to know which suffix is which).
- **CONFIDENCE:** HIGH (own-data, multi-date). **ALTERNATIVE:** the `_1` pairs are INTENTIONAL account-level vs portfolio-level duplicates of the same field family (fee schedule + ranges at both account & portfolio grain), not debt — plausible given the fee fields; either way it's a flatness/clarity tax on the consumer. **Business-significance:** stable schema = low ongoing-maintenance cost to consume; the denormalization = a minor parse-clarity tax, not a barrier.

## Dim 2 — FRESHNESS / DATA-LAG (operational-maturity)
- **Observation:** predictable **T+1 business-day** delivery (data-date D -> S3 delivery D+1), weekend-extended to 3d (Fri data delivered Mon). Daily batch; no intraday.
- **Evidence:** partition-date vs S3 LastModified, 6 recent allocations (lag 1d typical; one 3d over a weekend).
- **Inference:** freshness is predictable and adequate for a daily-cadence analytics platform; no real-time capability.
- **CONFIDENCE:** HIGH. **ALTERNATIVE:** occasional multi-day gaps could occur on BD-side delays (not observed in-window). **Business-significance:** T+1 is a reproducible SLA — a supplant feed (Schwab-direct) can match or beat it (Schwab files land same/next-day).

## Dim 3 — EXPORT-COMPLETENESS / WINDOW (operational-maturity) — the STANDOUT
- **Observation:** the transaction-export DELIVERY WINDOW is **IRREGULAR/UNPREDICTABLE**: across consecutive deliveries the trade_date span + row count swing wildly — 4d/4,563 rows; 2d/59,236; **78d-span/5,119**; **17d-MTD/128,471**. (Allocations/assets are point-in-time per-date snapshots, stable; the IRREGULARITY is the transaction feed.)
- **Evidence:** per-delivery row-count + trade_date-span probe (silver/transactions, 06-12..06-18).
- **Inference:** BD's transaction export does NOT deliver a fixed window — the consumer cannot assume "today's file = today's txns" or any fixed lookback; it must **defensively dedup + accumulate**. (Confirmed structurally: the `bd-txn-consolidator` lambda + the dedup-on-(account_id,as_of_date) exist precisely for this.)
- **CONFIDENCE:** HIGH (own-data, multi-date, mechanism-confirmed). **ALTERNATIVE:** the swings track BD re-delivery/backfill events (the 78d-span = a catch-up redelivery) rather than a designed window — same operational consequence. **Business-significance:** this is the single biggest BD operational-maturity GAP + the clearest supplant argument — a replacement feed (Schwab TRN, single-day deterministic partitions) is MORE predictable. NOTE: this also retro-grounds the chunk-3 fresh-NNA-diff residual (the BD window isn't merely "trailing," it's irregular).

## Dim 4 — IDENTIFIER-STABILITY (API-maturity)
- **Observation:** stable z-prefixed BD `account_id` + `relationship_id`/`portfolioid`; cross-custodian joins require the `schwab_bd_account_mapping` translation (7,027 rows; 85.7% of BD accts map to a Schwab id — chunk-2).
- **Evidence:** the mapping artifact (bd_account_id<->schwab_account_id) + chunk-2 coverage.
- **Inference:** identifiers are STABLE within BD, but BD uses its OWN id-space (not custodian ids) -> an identifier-translation layer is mandatory to reconcile to custodian-raw.
- **CONFIDENCE:** HIGH. **ALTERNATIVE:** the 14.3% unmapped = held-away/other-custodian/new accts (chunk-2), not id-instability. **Business-significance:** the translation layer is a modest integration cost; the id-space is BD-proprietary but deterministic.

## Dim 5 — UI-vs-EXPORT PARITY
- **Observation/Inference:** COULD-NOT-VERIFY — no BD UI access within the own-account ROE scope here; cannot diff exported figures against BD's UI presentation.
- **CONFIDENCE:** N/A (honest gap, Rule-22). **Business-significance:** unverified; a future own-account UI spot-check (within ROE) could close it. Flagged, not assumed.

---

## 6-DIM PARTNER-SCORING CONTRIBUTION (BD)
- **API-maturity: LOW-MODERATE.** Batch file-export model (no query API/pagination/cursor); stable schema but denormalized; proprietary id-space needing translation. Stable + predictable, but unsophisticated.
- **Operational-maturity: MODERATE.** Predictable T+1 freshness (good); but the IRREGULAR transaction-export window is a real operational gap (forces defensive consolidation).
- **=> BD SUPPLANT cost-to-work-around: LOW-MODERATE.** BD's value-add to us is managed data-DELIVERY (custodian-derived) + firm-config HOSTING (T2-HOST, chunks 2/4) — NOT a sophisticated API or computed IP. Replicating the delivery is straightforward (we already hold Schwab-direct, which is MORE predictable than BD's irregular window); the only frictions (irregular-window handling, id-translation) are already solved in our medallion. **Consistent with + reinforces the chunks-2-4 supplant-feasible verdict** — BD's own API-quality profile (unsophisticated batch feed, irregular window, denormalized schema) is itself an argument FOR supplant.

## GROUNDING + RESIDUALS
- **ROE:** zero BD-vendor traffic (analysis of delivered exports + S3 metadata only); Option-B-compliant and then some. **comp-rail:** comp-which (route) + pipescript advi-bd (interface model) + boto3 own-data probes (schema/freshness/window/identifier).
- **Residuals (Rule-22):** (1) UI-vs-export parity = could-not-verify (no UI access in scope). (2) True API rate-limit/pagination = N/A by delivery model (no programmatic API consumed). (3) Window-irregularity characterized over a 6-delivery window — a longer baseline would quantify the distribution (low-risk). (4) Scope = BD/49F own-account; ORION-char is the next sequential unit (rides opal-data-inf/bronze/orion-api; base-DS feeding D3 context); ECLIPSE-char GATED (DC2 crawl, Andrew risk-call).
