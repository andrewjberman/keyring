# /work cycle — 0.4.0_DS_ClientPlatform — 2026-06-02T1906Z

## Tick class: TO-COMPLETE (verify-only, no data change)

## Dispatch
SENIOR_DISPATCH from 2.0.0_SA_COO (off-hold, Andrew-direct 2026-06-02):
TO `BDPL_CNPRCS.WP-11b` — VERIFY-RELEVANCE-FIRST then (if still valid) re-run the
stranded 49F-cohort scoped-price-override AUA delta (~$24.3M); else recommend close.
Capacity-fill, NOT Inflection-critical-path.

## STEP 1 — Verify-relevance (the gate)

**Question:** Is the WP-11 scoped-price-override 49F re-run + its ~$24.3M AUA delta
still live/wanted/un-superseded? Is override commit 864b6d7a still in the live
canonical_prices path? Does the $24.3M delta still apply on the current basis?

### Evidence gathered
1. **Override logic intact in live scripts** — `_SCOPED_PRICE_OVERRIDES` (bd_price_update.py)
   + `_INCEPTION_DATES` (inject_scoped_overrides.py) still carry all 3 bonds. Only 2
   commits touched these files since WP-11 (864b6d7a): `a5ac27a27` (ADHC_DSFLOW.004
   future-annotations/ruff sweep) + `64b6b9d65` (a log commit) — both mechanical, neither
   superseded the override logic.
2. **Postdep is BLOCKING** — `comp-pipescript postdeps build_canonical_prices`:
   inject_scoped_overrides.py is a `[BLOCKING]` post-step ("rebuild wipes ALL scoped
   price overrides; inject must re-pin them immediately after every canonical_prices
   rebuild"; born from the 2026-04-06 BNP wipe / +$22M phantom incident). So the override
   is structurally re-applied on EVERY rebuild.
3. **Deployed MATCH** — `comp-pipescript deployed inject_scoped_overrides.py` → SILVER MATCH
   on s3://opal-data-bd. No drift.
4. **Live served artifact confirms continuous application** — pulled live
   `s3://opal-data-bd/silver/prices/canonical_prices.parquet` (rebuilt 2026-06-02 00:03,
   11,217,843 rows). All 3 override bonds pinned through 2026-06-02 at exactly the WP-11
   inception prices, single-source `bd_txn_price`, zero equity-price contamination:

   | Bond | ticker | rows | range | latest price | source |
   |---|---|---|---|---|---|
   | BNP PARIBAS SA | CUSIP_05613L3H2 | 426 | 2024-10-15..2026-06-02 | 1.0188 | bd_txn_price |
   | WELLS FARGO 4.15% 2029 | CUSIP_95000U2D4 | 615 | 2024-01-24..2026-06-02 | 0.9804 | bd_txn_price |
   | NEWMONT 2.8% 2029 | CUSIP_651639AX4 | 567 | 2024-04-01..2026-06-02 | 0.9037 | bd_txn_price |

   Equity siblings (BNPQF ADR / WFC common / NEM common) are SEPARATE asset_names at
   correct yahoo equity prices — no double-count, no phantom leak.

## STEP 2 — Branch: SUPERSEDED/MOOT → do NOT re-run

The override has been **continuously applied since 2026-04-15** (BLOCKING postdep
re-pins every rebuild). Therefore the ~$24.3M phantom correction is already permanently
baked into the current 49F basis and every downstream AUA computation built from it. A
re-run today would net **~$0 incremental delta, NOT a fresh $24.3M** — the drop is
already in the served numbers. The re-run-to-realize-delta task is moot/already-effectively-done.

- WP-11b TO → `complete` (verify-only; phantom in_progress cleared).
- WP-11 parent TO → `CLOSE-RECOMMENDED` (pending COO/registry project-level flip).
- No data change landed → no CTO/CVO CC required (per dispatch: CC only if a re-run lands a data change).

### Optional low-pri follow-up (NOT done — bundled with the moot re-run branch)
A dedicated override-presence regression sentinel in `gold_validate_config.yaml`. Structurally
redundant given the BLOCKING postdep + the existing `B_00` hybrid_price_fill pricing-coverage
validator; a cheap belt-and-suspenders if COO/CVO want it as a separate micro-TO.

## Verify discipline note
Followed `feedback_verify_against_served_artifact_not_partial_proxy`: traced to the actual
served canonical_prices artifact (live S3 pull + per-CUSIP latest-date read), not a partial
proxy (script-grep alone or a single partition). Single-source check ruled out a duplicate
phantom row leaking alongside the override.

## RAVC2 → COO: close-recommendation (verdict above).
