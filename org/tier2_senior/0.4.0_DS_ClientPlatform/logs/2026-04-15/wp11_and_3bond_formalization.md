# Session log — WP-11 + 3-bond scoped-exceptions formalization

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-15
**Task orders:**
- `3-bond-phantom-scoped-exceptions.md` (pending; thawed 2026-04-15)
- `BDPL_CNPRCS.WP-11.ds-scoped-price-overrides.md` (pending; thawed 2026-04-15)

## Summary

Thaw lifted by Andrew 2026-04-15. COO GO'd both TOs to ~D for a single paired commit. The tactical `scoped_price_exceptions.json` was already shipped on 2026-04-14 and is on S3 at `s3://opal-data-bd/code/silver/scoped_price_exceptions.json`. WP-11 formalizes the three phantom-bond entries into the permanent `_SCOPED_PRICE_OVERRIDES` list in `bd_price_update.py` and the matching `_INCEPTION_DATES` map in `inject_scoped_overrides.py`, so the BNP / WFC / NEWMONT fix survives independently of the JSON blocklist.

Path correction vs TO wording: both target scripts live under `data/black_diamond/scripts/silver/`, not `gold/` as the WP-11 TO states. Same files, same S3 deploy path (`code/silver/`).

## Edits

**`data/black_diamond/scripts/silver/bd_price_update.py`** — `_SCOPED_PRICE_OVERRIDES`:
- BNP PARIBAS SA: `ticker` BNP_STRUCT_DEP → `BOND_BNP_05613L3H2`; `price` 0.75 → 1.0188 (matches tactical JSON derived per-unit NAV).
- Added WELLS FARGO & CO 4.15% 01/24/2029: `BOND_WFC_415_2029`, 0.9804.
- Added NEWMONT CORP 2.8% 10/01/2029: `BOND_NEM_28_2029`, 0.9037.

**`data/black_diamond/scripts/silver/inject_scoped_overrides.py`** — `_INCEPTION_DATES`:
- BNP PARIBAS SA: 2024-12-06 → 2024-10-15 (aligned with tactical JSON).
- Added WELLS FARGO & CO 4.15% 01/24/2029: 2024-01-24.
- Added NEWMONT CORP 2.8% 10/01/2029: 2024-04-01.

## Compiler Tools

| Run | Expect | Observed | Pass/Fail |
|---|---|---|---|
| `comp-pipescript postdeps build_canonical_prices` | BLOCKING post-step `inject_scoped_overrides.py`; reason cites 2026-04-06 BNP incident | Exactly that — `[BLOCKING] Must run: inject_scoped_overrides.py`, reason `"rebuild wipes ALL scoped price overrides (BNP, MBS, DAF bonds)"`, incident `"2026-04-06 BNP PARIBAS SA override wiped, +$22M phantom value in Delaney account"` | **PASS** |
| `grep -n '_SCOPED_PRICE_OVERRIDES\|_INCEPTION_DATES' ...` (Phase 1 step 1) | Existing constants present | Found `_SCOPED_PRICE_OVERRIDES` at `bd_price_update.py:86`; `_INCEPTION_DATES` at `inject_scoped_overrides.py:84`. No matches in `gold/` — TO paths corrected to `silver/`. | **PASS** |
| `python -m py_compile bd_price_update.py inject_scoped_overrides.py` (Phase 2) | Exit 0 | Exit 0 | **PASS** |
| `comp-pipescript deployed bd_price_update.py` (pre-edit) | Tells me current S3 MATCH vs local | Output says "checks s3://opal-data-bd/code/gold/" — silver scripts aren't in the gold manifest; script coverage gap. Verified deployment path via `aws s3 ls s3://opal-data-bd/code/silver/` — both files present, will re-upload post-commit. | **PASS (with note)** |
| `comp-validate canonical_prices --artifact /tmp/canonical_prices.parquet` (Phase 2 step 2) | Exit 0 on regenerated artifact | **Deferred** — requires regenerated artifact from EC2 gold-runner. Will run after bd_price_update + inject_scoped_overrides daily cycle completes (4:51 PM ET today). | **DEFERRED** |
| `comp-blast canonical_prices` (Phase 3) | Consumer set unchanged | **Deferred to post-commit** per phase gating. | **DEFERRED** |

### Note on comp-pipescript deployed coverage

`comp-pipescript deployed` only checks `s3://opal-data-bd/code/gold/`. Silver-layer scripts like `bd_price_update.py` and `inject_scoped_overrides.py` are deployed to `s3://opal-data-bd/code/silver/` but not tracked by this tool. Flagging to COO/CTO as a compiler coverage gap — the silver-layer scripts that daily-enforce canonical prices should be in the deployed-status check surface.

## Deploy plan

1. Commit both files in a single `~D` commit.
2. `git push origin CLOUD`.
3. `aws s3 cp` both files to `s3://opal-data-bd/code/silver/`.
4. Next scheduled `bd-price-update` run (4:51 PM ET 2026-04-15) picks up the new `_SCOPED_PRICE_OVERRIDES` entries; enforces BNP / WFC / NEWMONT at the derived NAVs on every new daily canonical row.
5. Verify 49F pre/post AUA delta (~$24.3M drop) after the run completes; report to COO.

## Risk notes

- `_SCOPED_OVERRIDE_MAP` (line 167 of bd_price_update.py) rebuilds from `_SCOPED_PRICE_OVERRIDES` at import — new entries propagate automatically.
- `inject_scoped_overrides.py` `_build_base_overrides()` already iterates `_SCOPED_PRICE_OVERRIDES` and looks up `_INCEPTION_DATES` by `asset_name` — new entries wire in with zero additional code.
- JSON blocklist (`scoped_price_exceptions.json`) already supersedes same-`asset_name` entries from `_SCOPED_PRICE_OVERRIDES` (line 163). With WP-11 values matching the JSON, the blocklist and the formalization converge — no divergence risk.
- `build_canonical_prices_v2.py` rebuilds wipe scoped rows; the post-step `inject_scoped_overrides.py` re-pins them. BLOCKING dependency confirmed intact via `comp-pipescript postdeps`.

## Next

- Commit SHA + S3 etags recorded below after push+upload.
- Signal COO on commit + 49F delta confirmation after tonight's daily run.

## 15:22 ET addendum — canonical_prices gap remediation

Spot-check at 15:18 ET of `silver/prices/canonical_prices.parquet` (mtime 09:29 ET) found:
- BNP PARIBAS SA: price 1.0188 but `source=linear_interpolation`, ticker=None
- WELLS FARGO & CO 4.15% 01/24/2029: price **86.64** (Yahoo equity), `source=linear_interpolation`
- NEWMONT CORP 2.8% 10/01/2029: price **116.50** (Yahoo equity), `source=linear_interpolation`

Root cause: morning rebuild of canonical_prices (09:29 ET, downstream of someone's partial pipeline run — likely CN-P1/RA-P1 shadow-write testing) regenerated from scratch and did NOT fire `inject_scoped_overrides.py` as the required post-step. This is the Apr-06 $22M phantom incident pattern.

Remediation:
- `python inject_scoped_overrides.py --dry-run` — preview clean: +5,064 net rows, 9 assets get override-class rows, no duplicates.
- `python inject_scoped_overrides.py --upload` at 15:22 ET — uploaded 85.8 MB parquet to `s3://opal-data-bd/silver/prices/canonical_prices.parquet`.
- Post-upload spot-check: BNP 392 rows @ $1.0188 `src=bd_txn_price`; WFC 581 rows @ $0.9804 `src=bd_txn_price`; NEWMONT 533 rows @ $0.9037 `src=bd_txn_price`. All correct.
- `aws s3 cp ... /tmp/canonical_prices.parquet` then `comp-validate canonical_prices --artifact /tmp/canonical_prices.parquet` — exit 0; 1 SKIP for missing `canonical_prices` entry in `gold_validate_config.yaml` (flag to COO as tool coverage gap).

Deferred:
- 49F cohort AUA delta (~$24.3M expected drop) — requires downstream 49F re-run; nightly `bd-price-update` + downstream processing will surface it.
- `comp-blast canonical_prices` (Phase 3 post-commit step) — consumer set unchanged verification pending cohort run.

Escalation: COO should be aware the gold-runner orchestration needs to enforce `inject_scoped_overrides` as post-step of any `build_canonical_prices_v2` rebuild, including ad-hoc shadow-write test runs. Today a second phantom-price exposure window opened between 09:29 ET and 15:22 ET.

## Deployment record

## Deployment record

- Commit: `864b6d7a` (author `0.4.0_DS_ClientPlatform~D`)
- Pushed: origin/CLOUD `21c0637f..864b6d7a` at 2026-04-15 12:26 ET
- S3 uploads (2026-04-15 16:27 UTC / 12:27 ET):
  - `s3://opal-data-bd/code/silver/bd_price_update.py` — etag `72521f9a1dfefd8e0ea4708e561a27b2`
  - `s3://opal-data-bd/code/silver/inject_scoped_overrides.py` — etag `13915b2cee5fa7e809fbeb6751c10f28`
- Next natural trigger: `bd-price-update` daily run at 4:51 PM ET 2026-04-15. Will read the new `_SCOPED_PRICE_OVERRIDES` and emit `bd_txn_price`-sourced canonical rows for BNP / WFC / NEWMONT on the target date. 49F AUA delta measured post-run.
