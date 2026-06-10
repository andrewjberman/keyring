# NFRA_DTAFLP TO-1b — cot gold tree `opal-data-bd` reference classification

**archetype:** TRACE
**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-10 · **TO:** NFRA_DTAFLP.TO-1b (LD-0177)
**Scope:** classification only (read-only). Retarget WRITES are gated post-GLDINC-night-4 + post-TO-1. No `.py` edited by this deliverable.

---

## Headline

- **Actual count: 73 `opal-data-bd` references** across 45 files in `data/cot/scripts/gold/` (the PRD's "~46" was an estimate; rigorous grep = 73).
- **Only 7 refs are LIVE firm-local S3 operations that MUST retarget** to keep the forked cot pipeline working under the already-deployed `opal-data-cot` IAM cross-bucket Deny.
- **Schwab shared-custodian set = 4 refs (2 live defaults + 2 comments) in A_03 + B_01.** **Ground-truthed recommendation: cot has ZERO Schwab dependency — default `SCHWAB_S3_BUCKET` to `opal-data-cot` on fork; the injection no-ops cleanly. Route ruling to CTO (below).**
- **45 refs are DEAD / non-production** (diagnostics, incident one-offs, migration-rollback toolset) — recommend they do NOT carry into the firm-native cot fork.

| Class | Refs | Disposition |
|---|---|---|
| (b-LIVE) firm-local, executable S3 op | **7** | **MUST retarget** `opal-data-bd`→`opal-data-cot` (IAM Deny hard-fails otherwise) |
| (b-TEXT) firm-local, comment/docstring/echo | 17 | Cosmetic retarget for provenance; no runtime effect |
| (c) shared-custodian Schwab | 4 | Route to CTO; recommend default→`opal-data-cot` (no-op for cot) |
| (a) dead / non-production | 45 | Prune from firm-native fork (or retarget if retained) |
| **Total** | **73** | |

---

## Class (b-LIVE) — firm-local executable refs · MUST retarget (7)

These set the runtime bucket for live `boto3` reads/writes against the firm's own data bucket. The forked cot scripts run under the cot IAM role, which carries a **live cross-bucket Deny on `opal-data-bd`** (`97e40bd14` / `20617a347`). Left unchanged, each of these throws `AccessDenied` at runtime. **Highest priority for the gated retarget write.**

| File:line | Ref | Note |
|---|---|---|
| `gold_dispatch.sh:62` | `BD_S3_BUCKET="${BD_S3_BUCKET:-opal-data-bd}"` | **Master nightly orchestrator default** — drives every script's bucket env |
| `build_canonical_prices_v2.py:56` | `os.environ.get('BD_S3_BUCKET', 'opal-data-bd')` | Core pricing build |
| `C_01c.role_aua_flow_join.py:50` | `os.environ.get('BD_S3_BUCKET', 'opal-data-bd')` | Role-AUA flow join |
| `B_01b.classify_new_securities.py:40` | `DATA_BUCKET = 'opal-data-bd'` | Hardcoded (no env fallback) |
| `_lib/watermark.py:39` | `S3_BUCKET = "opal-data-bd"` | Incremental-watermark store (used by incremental scripts; 14-day lookback) |
| `validate_sl_nightly_gate.py:31` | `S3_BUCKET = "opal-data-bd"` | Silver nightly gate |
| `validate_platinum_consistency.py:39` | `DEFAULT_BUCKET = 'opal-data-bd'` | Platinum consistency validator |

Retarget approach (gated): prefer env-driven defaults flipping to `opal-data-cot`; the two hardcodes (`B_01b:40`, `_lib/watermark.py:39`, plus `validate_*`) become literal `opal-data-cot`. Rule 14 gate (`.tools/ds-commit-gate.sh`) on every edited `.py`; Rule 13 deploy cycle to `opal-data-cot/code/gold/`.

## Class (b-TEXT) — firm-local comments/docstrings/echoes (17)

No runtime effect; retarget only for provenance accuracy (do in the same gated write as b-LIVE for hygiene, but they cannot cause a failure):

`C_04.validate_aua.py:25` · `D_01.partner_analytics.py:9,10,11,17` · `D_03.composition_artifacts.py:6,7` · `gold_dispatch.sh:36,815,1231,1271,1273` · `validate_platinum_consistency.py:5` · `validate_sl_nightly_gate.py:175` · `_lib/watermark.py:6` · `README_BUILD_SEQUENCE.md:117,133`

---

## Class (c) — shared-custodian Schwab · ROUTE TO CTO (4)

| File:line | Ref |
|---|---|
| `A_03.positions_cube.py:267` | `# Canonical layout: opal-data-bd/schwab/silver/rps/` (comment) |
| `A_03.positions_cube.py:268` | `S3_SCHWAB_BUCKET = os.environ.get('SCHWAB_S3_BUCKET', 'opal-data-bd')` |
| `B_01.holdings_lots.py:151` | `# Canonical layout: opal-data-bd/schwab/silver/rps/` (comment) |
| `B_01.holdings_lots.py:152` | `S3_SCHWAB_BUCKET = os.environ.get('SCHWAB_S3_BUCKET', 'opal-data-bd')` |

### Mechanism
The Schwab RPS (Retirement Plan Services) injection (`A_03._load_rps_injection_events`, mirrored in `B_01`) is **fully gated** by `gold/dimensions/schwab_bd_account_mapping.parquet` (read from the firm's *own* bucket, `S3_BUCKET`). The flow:
1. Read the Schwab→BD account mapping from the firm bucket. If absent → graceful `try/except` WARN, injection skipped.
2. If a mapping exists, list/get `schwab/silver/rps/` from `S3_SCHWAB_BUCKET` (default `opal-data-bd`), inject mapped accounts' positions, and extend the phantom-exclusion alive-set (`A_03:1509-1529`, also try/except WARN).

So the injection is a **no-op for any firm with no Schwab-mapped accounts** — it degrades silently and safely.

### Ground truth (read-only S3 census, 2026-06-10)
- `s3://opal-data-cot/schwab/` → **EMPTY** (no Schwab custodian feed for cot).
- `s3://opal-data-cot/gold/dimensions/` → `accounts_dimension_latest`, `advisor_assignments_history`, `client_dimension` only — **no `schwab_bd_account_mapping.parquet`**.
- Schwab RPS is a 49 Financial-specific custodian capability; Cottonwood onboarded to Black Diamond 2026-04-22 and its data is sourced entirely from BD.

### Recommendation to CTO
1. **On fork, default `SCHWAB_S3_BUCKET` to `opal-data-cot`** (not `opal-data-bd`). Rationale: (a) cot has no Schwab mapping → injection no-ops regardless; (b) keeping the `opal-data-bd` default would hard-fail under the live cot IAM cross-bucket Deny the moment a mapping ever appeared; (c) zero structural cross-firm read is the whole point of full separation. **No IAM Deny carve-out for cot→bd Schwab is needed or wanted.**
2. **Do NOT build a cot Schwab feed now** — there is no Cottonwood Schwab RPS data to route.
3. **Conditional follow-on (flagged, not blocking):** *if* Cottonwood is later found to custody retirement-plan assets at Schwab RPS, full separation means a **cot-own** custodian feed — Schwab RPS ingested to `opal-data-cot/schwab/silver/rps/` + a cot `schwab_bd_account_mapping.parquet`. That is an **AE/DT ingest task**, not a gold-script change.

---

## Class (a) — dead / non-production · prune from fork (45)

Not in the scheduled nightly cot gold chain (`gold_dispatch.sh`). Zero served-surface impact. Recommend they are NOT carried into the firm-native cot fork (cot is a recent, lean onboard; these are 49F-incident-specific artifacts). If any are retained for parity, they must be retargeted too (same IAM Deny applies on execution).

- **AUA-gap incident runners (9):** `auagap002_cascade.sh:10,17,22,23,34,35` · `adhoc/auagap002_option_a_cascade.sh:21,63,64`
- **Diagnostics (3):** `diag_gold_silver_recon.py:10,36` · `diag_sleeve_fix.py:12`
- **E_* exploratory/diagnostic family (19):** `E_02:27` `E_03:22` `E_04:21` `E_05:29` `E_06:26` `E_07:27` `E_08:23` `E_09:26` `E_10:25` `E_11:24` `E_12:8` `E_13:28` `E_14:28` `E_15:25` `E_16:25` · `E_17:5,15` · `E_19:23` · `E_25:273`
- **gldrst migration-rollback toolset (6):** `verify_migration.py:28,287` · `preflight_snapshot.py:10,26` · `restore_old_keys.py:11,30`
- **One-off run_* incident runners (6):** `run_c01c_rap1c.py:9` · `run_b03_auagap002.py:9` · `run_c00_auagap002.py:9` · `run_b00_auagap002.py:10` · `run_c03_auagap002.py:9` · `run_c02_auagap002.py:8`
- **Partial-chain helper (2):** `_partial_chain_b01.sh:15,21` (live log writes to `opal-data-bd/gold/logs/` — retarget if retained)

---

## Gating / next steps

- **Classification (this deliverable): COMPLETE, read-only.** RAVC2 to COO + MSTR + CTO.
- **Retarget WRITE: HELD** until GLDINC night-4 clears (LD-0176 morning review) AND TO-1 is confirmed landed (`6b0be4337`). Rule 13 (deploy cycle to `opal-data-cot/code/gold/`) + Rule 14 (`ds-commit-gate.sh` on every edited `.py`) apply.
- **TO-4 (FIRM_ID drop): HELD** pending Andrew DTAFLP go (read-only prep only).
- **Schwab (c) set: CTO ruling requested** on the default-bucket recommendation above.
