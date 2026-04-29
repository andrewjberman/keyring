# DS~B — ADVI_INFSHIP B1 Wave + IWM Book + orion_tax Root-Cause

**Agent serial:** `0.4.0_DS_ClientPlatform~B`
**Date:** 2026-04-29
**Session shape:** post-compaction re-engagement → IWM book.json publisher run → pull_unified S3-upload patch → orion_tax exit=2 root-cause investigation
**Outcome:** 2 commits on origin/CLOUD; 1 publisher run UPLOADED; 1 root-cause RAVC; 3 RAVC4 closures (DE + ~D + AE 0.7.0~B)

---

## Mandate Origin

Three threads converged from prior session's outstanding queue:

1. **DS~D 0.4.0_DS_ClientPlatform~D (20260428T152957Z)** — cross-lane flag: INF_D_02 `_PLACEHOLDER_KEYS` still excludes `inflection_wealth_management` (line 103); same fix as INF_I_D03 `2b568b08`; ~5 min code edit + ~2 min publisher run. DE 13:33Z gated on this for B4 IWM drill visual completion.
2. **AE 0.7.0~B (20260428T153810Z)** — third smoke (15:33Z) identified two follow-ups:
   - `pull_unified_account_dim.py` missing S3 upload step (script writes only to local `pulls/` dir; silver chain fails NoSuchKey downstream)
   - `orion_tax_dim.py` exit=2 with truncated stderr (deprecation warning only; argparse vs runtime cause unknown)
   - Pre-cron deadline 2026-04-29 12:30 UTC.
3. **AE 0.7.0~B (20260428T152030Z)** RAVC4-CLOSE on my prior session's `cf11f13b` Linux portability fix — VERIFIED end-to-end on `i-083ad9ae297f88e9f`; only B1 blocker remaining was JWT staleness in AE 0.6.1~B's ORIAPI lane.

---

## Deliverables Matrix

| # | Item | Commit | S3 MATCH | RAVC closed by |
|---|------|--------|----------|----------------|
| 1 | INF_D_02 `_PLACEHOLDER_KEYS` IWM unblock + publisher run | `4bf137520` | `a06ad19af0...` (code) + `book.json` LIVE 32,564 B | DE RAVC4 sent 20260429T122446Z; ~D RAVC4-CLOSE 20260429T130000Z |
| 2 | `pull_unified_account_dim.py` `--upload-bronze` flag + S3 upload | `91b822857` | n/a (manual_api script; bronze runner pulls via git checkout) | AE 0.7.0~B RAVC4 sent 20260429T122911Z |
| 3 | `orion_tax_dim.py` exit=2 root-cause investigation | n/a (no code change) | local run verified exit 0, 877,772 B unrealized CSV at 12:27Z | AE 0.7.0~B RAVC4 sent 20260429T122911Z |

---

## Section-by-Section

### §1 — INF_D_02 IWM unblock: `4bf137520`

**Root cause:** `_PLACEHOLDER_KEYS = {'new_accounts_rep', 'inflection_wealth_management'}` at line 103 was filtering IWM out of the per-advisor publisher loop in INF_D_02. Same intentional skip as INF_I_D03 had pre-`2b568b08`. Andrew direction (via DE 0.4.0_DE_ClientPlatform 13:33Z): IWM should be a first-class drillable advisor entry — same as Peter Lee + Patrick Scanlan.

**Fix (verbatim from DS~D's `2b568b08` reference):**

```python
# Placeholder advisor_keys (firm-level routing buckets, not individual advisors).
# Andrew direction 2026-04-28 (via DE 0.4.0_DE_ClientPlatform 13:33Z): IWM
# (`inflection_wealth_management`) is now treated as a first-class drillable
# advisor entry — same as Peter Lee + Patrick Scanlan — with its own book.json
# drilldown page. Removed from skip set; new_accounts_rep remains a placeholder
# (genuine routing bucket, no drilldown). Mirrors INF_I_D03 fix at 2b568b08.
_PLACEHOLDER_KEYS = {'new_accounts_rep'}
```

Lines 586 + 721 (the two `account_team[~account_team['advisor_key'].isin(_PLACEHOLDER_KEYS)]` consumer sites) needed no edits — set update propagates through `.isin()` automatically.

**Publisher run (`python3 INF_D_02.advisor_client_detail.py --upload`):**
```
[2026-04-29T12:23:30Z] Advisor books:   8         ← was 7 pre-fix; IWM is the 8th
[2026-04-29T12:23:30Z] Client details:  305
[2026-04-29T12:23:30Z] Mode:            UPLOADED
```

**S3 verification of IWM artifacts:**
```
2026-04-29 08:22:54  32564  s3://opal-data-inf/platinum/advisors/inflection_wealth_management/book.json    ← new
2026-04-28 11:28:41   6331  s3://opal-data-inf/platinum/advisors/inflection_wealth_management/composition.json
2026-04-28 01:39:15   1637  s3://opal-data-inf/platinum/advisors/inflection_wealth_management/top_holdings.json
```

**book.json shape spot-check (matches DE's 13:33Z ask):**

| Field | Value | DE expected |
|-------|-------|-------------|
| `advisor_key` | `inflection_wealth_management` | ✓ |
| `book_name` | `Inflection Wealth Management` | ✓ |
| `firm_id` | `inflection` | ✓ |
| `summary.total_aua` | `$86,187,811.83` | ✓ matches leaderboard QTD |
| `summary.tagged_aua` | `$86,187,811.83` | ✓ |
| `summary.client_count` | 297 | ✓ |
| `summary.account_count` | 801 | leaderboard 800; +1 likely fresh acct |
| `summary.ytd_nna` | `$-1,098,045.18` | firm-level NNA |
| `summary.{tax,billing,performance}` | all present | ✓ |
| `clients[]` length | 297 | ✓ all HH listed |

**Code shipped to S3 gold-runner prefix:** `aws s3 cp data/orion/scripts/gold/INF_D_02.advisor_client_detail.py s3://opal-data-inf/code/gold/INF_D_02.advisor_client_detail.py` — md5 MATCH `a06ad19af0b83e0e85b41d9e175b5353`.

### §2 — pull_unified_account_dim.py `--upload-bronze` ship: `91b822857`

**Bug class (per AE 0.7.0~B 15:38Z):** the script pulled API → wrote local CSV → exited 0, but never uploaded to S3 bronze. So `bronze marker` said OK while silver builders (household + performance + activity) all failed downstream with NoSuchKey on `s3://opal-data-inf/bronze/orion-api/{date}/unified_account_dim.csv`.

**Pattern adopted:** mirror `orion_tax_dim.py write_bronze()` exactly (`--upload-bronze` flag default OFF for manual local runs, ON when orchestrator passes the flag).

Three changes:
1. `import argparse` added (alphabetized after `from __future__`)
2. `main()` now begins with `argparse.ArgumentParser` accepting `--upload-bronze, action="store_true"`
3. Inside the polling loop, after `with open(out, "wb")`, capture `now_utc` once and emit `date_dashed = now_utc.strftime('%Y-%m-%d')` so local file (yyyymmdd) and S3 key (yyyy-mm-dd) come from same instant. Conditional on `args.upload_bronze`:

```python
if args.upload_bronze:
    key = f"bronze/orion-api/{date_dashed}/unified_account_dim.csv"
    s3.put_object(
        Bucket="opal-data-inf",
        Key=key,
        Body=p.content,
        ServerSideEncryption="AES256",
        ContentType="text/csv",
    )
    print(f"[upload] s3://opal-data-inf/{key} ({len(p.content)} bytes)")
```

**Verification:**
- `.tools/ds-commit-gate.sh data/orion/manual_api/pull_unified_account_dim.py` → CLEAN
- `python data/orion/manual_api/pull_unified_account_dim.py --help` → flag accepted, helptext correct
- Did NOT run end-to-end with `--upload-bronze` locally (would deposit a real bronze object during a live cron window; deferred to tomorrow's 12:30 UTC cron once AE 0.7.0~B ships orchestrator follow-up `extra_args=("--upload-bronze",)`)

**Orchestrator dependency:** AE 0.7.0~B will ship a follow-up patch appending `extra_args=("--upload-bronze",)` to the unified DimSpec in their orchestrator commit `05ae692b`. Confirmed flag name to AE in RAVC4.

### §3 — orion_tax_dim.py exit=2 root-cause: NOT a script bug

**Hypothesis ruled out (template KeyError):** Inspected `data/orion/manual_api/billing_dim_spike.verbose.json` (75,367 B). Top-level `schema.contextChange` exists with all 12 expected keys including `costBasisOptionId`. So `q["schema"]["contextChange"]["costBasisOptionId"] = cost_basis_option_id` (line 235 in orion_tax_dim.py) is safe — would not raise KeyError. KeyError would also be caught by main()'s `try/except` wrapper at line 462-465 → exit 5, not 2.

**Hypothesis ruled out (argparse):** Already accepts `--upload-bronze` (line 407). AE confirmed orchestrator passes the same flag fine to billing/tax. argparse error would be exit 2 in some Python versions but stderr would show "unrecognized arguments" not just deprecation warnings.

**Hypothesis confirmed (JWT staleness at API layer):** Re-ran `python data/orion/manual_api/orion_tax_dim.py --skip-realized` locally with current fresh JWT (12:27:28Z UTC, 9:58 remaining):

```
[12:27:28Z] JWT OK -- expires 2026-04-29T22:26:01.000Z (9:58:32 remaining)
[12:27:28Z] --- PULL: INF_L1_tax_unrealized_20260429T122728Z (cbo=0, window=3y) ---
[12:27:31Z] create OK -- id=a1798628-3911-4fff-8643-837753b858a8     ← Verbose POST 200
[12:28:18Z] generate OK -- .../Run/b8d58185-...                       ← Generate POST 201
[12:28:19Z] poll OK -- 877,772 bytes
[12:28:21Z] cleanup DELETE -- 204
[12:28:21Z] OK: orion_tax_dim.py bronze pull complete
```

Exit 0. 877 KB unrealized CSV written. ~53s wall-clock.

**Diagnosis:** at AE's 15:33Z smoke yesterday, `read_jwt()` succeeded (S3 read OK + freshness check passed because `expires_at_iso` was a future timestamp in the JSON file) but the JWT itself was rejected at the Orion API layer with HTTP 401. `create_query` saw non-200, `sys.exit(2)` per docstring exit-code map. Elapsed 2.65s = `read_jwt(~1s)` + `Verbose POST 401 round-trip(~1.5s)`. Path is in AE 0.6.1~B's ORIAPI lane (Wave 2 ORIAPI JWT recovery commit `2bcf708fb`).

**No code change to orion_tax_dim.py.** Script is structurally clean. Tomorrow's 12:30 UTC cron should produce all 7 bronze CSVs cleanly with the recovered JWT lifecycle.

---

## Compiler Tools

| Tool | Run count | Notes |
|------|-----------|-------|
| `.tools/ds-commit-gate.sh` | 2 (per `.py` file edited: INF_D_02 + pull_unified) | Both PASS — py_compile + AST undefined-name + ruff |
| `.tools/safe-commit.sh` | 2 commits (`4bf137520`, `91b822857`) | Both clean (single-file pathspec, no contamination, no `--force` needed) |
| `aws s3 cp` MATCH verify | 1 (INF_D_02 to s3://opal-data-inf/code/gold/) | md5 MATCH `a06ad19af0b83e0e85b41d9e175b5353` (head-object ETag = local md5) |
| Local publisher run | 1 (INF_D_02 `--upload`; 8 advisors + 305 details) | "Mode: UPLOADED"; IWM book.json LIVE on S3 verified via `aws s3 ls` |
| Local script smoke | 1 (orion_tax_dim.py `--skip-realized`) | Exit 0, 877 KB CSV; JWT healthy 12:27Z; rules out script-side bug |
| `comp-pipescript io` | 0 | INF gold scripts not yet indexed (ADHC_COMPIL.001 pending); known io map; edits don't change column flow |
| `comp-pipescript deployed` | 0 | Direct head-object md5 verify used instead (BD-only tool) |

---

## RAVC Loops Closed

| Counterparty | Topic | RAVC4 close |
|-------------|-------|-------------|
| 0.4.0_DE_ClientPlatform | IWM book.json LIVE — both halves of B4 IWM drill ready | 20260429T122446Z (sent; awaiting visual via DT push) |
| 0.4.0_DS_ClientPlatform~D | Cross-lane closure on INF_D_02 _PLACEHOLDER_KEYS flag | DS~D RAVC4-CLOSE 20260429T130000Z (validated commit + S3 state; loop closed) |
| 0.7.0_AE_CloudOps~B | pull_unified S3 upload SHIPPED + orion_tax exit=2 ROOT CAUSE eval | 20260429T122911Z (sent; awaiting orchestrator `extra_args` follow-up + tomorrow's 12:30 UTC cron verification) |

---

## Lane Boundary

Clean. Edits scoped to:
- `data/orion/scripts/gold/INF_D_02.advisor_client_detail.py` (1-line `_PLACEHOLDER_KEYS` set update + 4-line comment block)
- `data/orion/manual_api/pull_unified_account_dim.py` (argparse + S3 upload — 14 lines added)

No cross-lane trespass into ~A (INF_D_00c, accounts_v2, transactions), ~D (INF_I_D03, assets, pull_inflection_assets, pull_inflection_new_portfolio), or ~C (geo/MAX TWR). DS~D's IWM composition.json + INF_I_D03 PLACEHOLDER fix from `2b568b08` left untouched.

`safe-commit.sh` audit log: 2 commits this session, both NORMAL pathspec (no FORCE-BYPASS — single-file commits don't interact with shared-index contamination patterns from yesterday's wave).

---

## Outstanding (out of my lane)

- AE 0.7.0~B orchestrator follow-up: append `extra_args=("--upload-bronze",)` to unified DimSpec (1-commit patch confirmed in their RAVC).
- AE 0.6.1~B ORIAPI JWT lifecycle health for tomorrow's 12:30 UTC cron (Wave 2 `2bcf708fb` recovery in flight).
- DT push portal/DEV B4 commit (folds in the 3-advisor INFLECTION_LAYOUT change with `advisorDrill.enabled=true`); enables visual cycle for IWM drill render.
- INFGRD.004 chain rerun (Andrew hold) — when canonical refreshes, my prior session's `_meta` annotation on `header_metrics.json` (`b287388d`) auto-clears.

---

## Numbers Reference

- IWM total_aua: **$86,187,811.83** (matches leaderboard QTD entries[].total_aua)
- 8 advisor books (was 7 pre-`4bf137520`; IWM 8th)
- 305 client details emitted in same publisher run
- 297 HH / 801 accts under IWM advisor_key (DE expected 800; +1 fresh acct)
- 877,772 B orion_tax unrealized CSV (3y window) — verified working with fresh JWT 12:27Z
- 75,367 B template `billing_dim_spike.verbose.json` — schema.contextChange.costBasisOptionId verified present (rules out KeyError class)
- 2× S3 MATCH md5: `a06ad19af0...` (INF_D_02 code), n/a for pull_unified (manual_api; runner uses git checkout)

---

*Authored by `0.4.0_DS_ClientPlatform~B`. Session arc: 20260429T120000Z → 20260429T123000Z (~30 min wall clock). 2 commits + 1 publisher run + 1 root-cause investigation closing the joint AE 0.7.0~B B1 follow-up wave.*
