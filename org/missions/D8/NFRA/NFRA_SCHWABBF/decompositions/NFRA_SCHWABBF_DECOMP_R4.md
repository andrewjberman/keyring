# NFRA_SCHWABBF decomposition -- ROUND 4 (2026-10-20, issuer 2.0.0_SA_COO~SB): the silver tier on the firm form, 08403355 and the Cottonwood masters

Cut on the CTO's go (msg 109961, replying to the round-3 slug `ROUND3_L10_SLUG_TO_CTO.md` @b53e6a3eaf) and PRD v0.9 C-TIERS (ADMITTED; the CVO's v0.8 refusal and the CTO's v0.9 fix are in the PRD log). Andrew-direct ~17:0xZ, verbatim:
"a, yes. this needs to go through the same full bronze/silver process that the other masters go through" (silver, meta and `_ops` move with bronze), and ~16:3xZ: "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
**Scope of this round (CTO msg 109961): SILVER only.** Meta and `_ops` are round 5, cut once `4.0.0_SA_CRO` adds the `meta` and `_ops` tiers to the naming registry (the builder refuses them today). **The cutover is ONE act across every tier: no data moves until rounds 4 and 5 are both merged and the gateway edit is ready.**

## The silver contract (fixed here; every cell builds against it)

- For a FIRM-FORM master M (08403355 under `49financial`; 08719286, 08134043, 08165601, 08480305 under `cottonwood`), firm F, silver table T, business date D: the silver object is `schwab/{F}/silver/{T}/date={D}/{M}.parquet` = `address('schwab', F, 'silver', T, 'date=D')` without `s3://opal-data-assets/`, plus `/` plus `{M}.parquet`. It replaces `data.parquet`; every other byte of the converter's output is unchanged (PRD v0.9).
- For 08242234 and 08335338 (and any master outside the five): TODAY's `schwab/{M}/silver/{T}/date={D}/data.parquet`, byte for byte.
- 08403355's silver today (measured ~16:5xZ): 18 tables (`dim_asset`, `dim_balance`, `dim_position`, `dim_transaction` and 14 `fact_*`), one `data.parquet` per date, e.g. `schwab/08403355/silver/dim_balance/date=2026-10-16/data.parquet` (15,807 bytes).
- The silver event: none. Silver is written by the converter on a bronze event and is not itself an event source (the event rules match `schwab/<firm or master>/bronze/` with suffix `.zip`).
- `silver_registry.py` is shared with the other source families' Lambdas (each vendors a copy). It is NOT edited by this round; the Schwab override is applied in the Schwab-only modules.

## The rectangle (round 4)

| cell | item | PRD rows | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `BF-s-4` | the converter family writes, reads back, lists and checks silver on the firm form for firm-form masters (code, five vendored twins, tests) | C-TIERS | FWD-1, FWD-5 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing deployed) | worker | -- |
| `BF-m-4` | the move tool gains the silver tier for 08403355 (copy with rename `data.parquet` -> `08403355.parquet`, sha-verified) | C-TIERS, C-MOVE | FWD-4 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `BF-e-4` | the equality tool captures old-form silver before and reads firm-form silver after | C-EQUAL, C-TIERS | FWD-5 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `BF-t-4` | the trace reads and checks silver on both forms | FWD-1 DONE WHEN, FWD-4 | FWD-1 | NOT-EVALUATED | laptop | LOCAL | worker | -- |
| `BF-i-4` | the converter role may write the firm silver prefixes, enumerated per master (Terraform text only) | C-TIERS, C-ALONGSIDE (IAM shape) | FWD-1, FWD-8 | NOT-EVALUATED | laptop | WORLD (`infra/` floor; nothing applied) | worker | -- |

Not in this rectangle: meta and `_ops` (round 5, after the CRO's tier rows); the gateway side (`2.0.0_SA_COO~O` owns it, `0.7.0_AE_CloudOps~NFRA1` applies it in the cutover window; I owe the date); the Alongside box (`~SA`); the release acts, re-cut after round 5.

**Chains (M = 5; fan-out 5 of 5, cap 8).** S (slot ~1), M (~2), E (~3), T (~4), I (~5); no edges.

**Write sets (disjoint).**
- BF-s-4: `data/assets/scripts/silver/{schwab_conversion,conversion_manifest,schwab_projections,set_identity_guard,schwab_runtime}.py`; their five twins in `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`; `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json` (only if the vendored set changes); tests `data/assets/scripts/silver/tests/test_schwab_silver_firm_key.py` (new), `test_conversion_manifest.py`, `test_set_identity_guard.py`, `test_schwab_conversion.py`, `test_schwab_runtime.py`.
- BF-m-4: `data/canonical/schwab/keyform/move_bronze_key_form.py`, `data/canonical/schwab/tests/test_move_bronze_key_form.py`, `data/canonical/schwab/tests/fixtures/move_listing_silver.json` (new).
- BF-e-4: `data/canonical/schwab/keyform/equal_sample.py`, `data/canonical/schwab/tests/test_equal_sample.py`.
- BF-t-4: `data/canonical/schwab/keyform/thread_trace.py`, `data/canonical/schwab/tests/test_thread_trace.py`.
- BF-i-4: `infra/aws/terraform/opal-assets/silver.tf`, `data/canonical/schwab/tests/test_firm_prefix_grants.py`.

## Rule 24 record (the cell set is a schema)

- **MECE over a declared domain.** Domain: the silver-tier consumers and producers of PRD C-TIERS for the in-scope masters = the producer (converter family), the mover, the instrument that compares, the instrument that traces, the permission that lets the producer write = five members; the readers outside this repo's Schwab tree (the gateway) are `2.0.0_SA_COO~O`'s. By subtraction from the repo census of `08403355` in code (45 files, native Grep over `data/ infra/ lib/ .tools/ deck_generation/`, 2026-10-20 ~17:5xZ): gateway files (`infra/aws/ec2/opal-gateway/**`, `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf`) = COO~O; registry and naming files = generated or CRO; the converter family = BF-s-4; the key-form/move/trace/equality/IAM files = this project's tools; no gold reader in this repo reads 08403355 silver. Remainder: none.
- **Same grain. Intent coherence. State coherence.** One cell per write set; none writes to S3, applies Terraform, deletes, deploys, or contacts Schwab.

## Battery (round 4)

- `comp-schedule`: DECLARED-NOT-APPLICABLE. No schedule is touched.
- `comp-iam`: RUN. Denominator: `silver.tf` (the converter role: `silver_read_bronze` at ~561, the write grant over `silver_source_scopes` at ~395-417, my round-2 firm read at ~624-655) and `monolith-iam.tf`, 2 Terraform files; masters enumerated: 3 before round 2, 1 (08403355) + 4 Cottonwood for the firm silver write after this round. The converter's silver WRITE grant today is `schwab/<master>/silver/*` over `silver_source_scopes.schwab`, which does not cover `schwab/49financial/silver/`: a firm-form conversion would be refused at its first write. Blind: the live IAM plane (0 roles read).
- `comp-adversary`: DECLARED-NOT-APPLICABLE as a lens run. Findings inlined: (1) the converter builds the silver key in THREE places (`silver_registry.silver_key` shared; `schwab_projections.dim_key`; `conversion_manifest.canonical_object_key`) and walks it in two more (`set_identity_guard` walk; the closure verdict's partition check); a cell that changes one leaves the guard counting zero silver and reporting nothing; (2) a firm folder holds several masters' objects, so every walk and count filters by the `<master>.parquet` name; (3) `silver_registry.py` is vendored by the other families, so the override must live in Schwab-only code; (4) the equality read must compare the SAME figures across the rename (`data.parquet` vs `<master>.parquet`); (5) the pre-cutover silver partitions are `data.parquet` under the master folder and stay readable until the old keys are deleted.

## Not in round 4

Meta and `_ops` (round 5); the 0840 backfill and held-days record; the gateway edit; the release acts; silver, meta and `_ops` for Cottonwood beyond the key rule (the `~SA` lane writes them from their first day).
