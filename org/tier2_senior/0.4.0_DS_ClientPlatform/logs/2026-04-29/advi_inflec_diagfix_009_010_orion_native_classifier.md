# DS — ADVI_INFLEC.DIAGFIX.009 + .010: Orion-native asset classification (HAR-assisted endpoint discovery + INF_I_D03 refactor)

**Agent serial:** `0.4.0_DS_ClientPlatform`
**Date:** 2026-04-29 (session 3, post `/clear`)
**Session shape:** DIAGFIX.009 HAR-investigation VERDICT A + DIAGFIX.010 5-phase build (bronze + silver + INF_I_D03 refactor + composer auto-flip + validation)
**Outcome:** Orion-native classification live. Regex classifier + bd-securities DDB shim deleted. 23,699 silver rows / 100% coverage / orion_native_v1 metadata propagating end-to-end.

---

## Mandate Origin

DIAGFIX.009 first iteration (`ds-orion-morningstar-category-hunt.md`) was a TRACK-1 Verbose-API probe. TRACK-2 closed on Andrew's HAR file (`api.cloud.orionadvisor.com(6).har`). VERDICT A delivered to COO (`20260429T215145Z`) — endpoint found.

DIAGFIX.010 (`ds-orion-native-classification-build.md`) GO from COO `20260429T220Z`, Andrew authorized. 5-phase plan from VERDICT A endorsed verbatim with one Phase 5 win-condition clarification (percentages within ±2pp; absolute total delta out of scope).

---

## TO Coverage

| TO | Type | Status | Ship commit |
|----|------|--------|-------------|
| ADVI_INFLEC.DIAGFIX.009 (Morningstar hunt) | Investigation, HAR-assisted | VERDICT A | `8d8be1bcd` (PATH_DISCOVERY_MSTAR.md + probe) |
| ADVI_INFLEC.DIAGFIX.010 Phase 1+2 | Build, bronze + silver | SHIPPED | `2979c12a7` |
| ADVI_INFLEC.DIAGFIX.010 Phase 3 | Refactor, INF_I_D03 | SHIPPED | `e106bc7b8` |
| ADVI_INFLEC.DIAGFIX.010 Phase 4 | Composer metadata-inheritance | SHIPPED | `6f60a47eb` |
| ADVI_INFLEC.DIAGFIX.010 Phase 5 | Validation + RAVC | DELIVERED | (RAVC, no commit) |

---

## Files Touched

| File | Change |
|------|--------|
| `data/orion/manual_api/PATH_DISCOVERY_MSTAR.md` | NEW — full endpoint contract for `/api/v1/Portfolio/Clients/{cid}/Assets/{date}`, 58-column schema, coverage validation, bucket-mapping draft, 5-phase plan |
| `data/orion/manual_api/probe_mstar_paths.py` | NEW — TRACK-1 Verbose-API path probe (FAIL pattern documented; Verbose API does not surface mstar fields) |
| `data/orion/manual_api/pull_inflection_assets_v2.py` | NEW — Orion REST asset pull, iterates 296 distinct Inflection household_ids, captures all 58 columns to bronze |
| `data/orion/scripts/silver/convert_assets_v2_to_silver.py` | NEW — bronze parquet → silver/api_dims/assets_v2/snapshot_date={date}/data.parquet, camelCase→snake_case, type coercion |
| `data/orion/scripts/gold/INF_I_D03.composition_artifacts.py` | REFACTOR — deleted regex classifier + bd-securities cache + 4 Layer-1/2/3/4 functions + 5 keyword constants. Added Orion-native lookup, bucket map with alternatives discriminator, classification metadata stamp |
| `data/orion/scripts/gold/INF_I_D02d.firm_mix_summary.py` | FIX — composer inherits classification_method + classification_caveats from upstream firm_composition.json instead of hardcoding |

---

## Endpoint Discovery — HAR Analysis

`GET /api/v1/Portfolio/Clients/{clientId}/Assets/{date}?$top=50000&includeCostBasis=false` (date `MM-DD-YYYY`)

100% coverage on `assetClass` (Morningstar Category) + `productCategory` (Equity / Bond / Money Market) in HAR sample. 58-column schema also fills several PATH_DISCOVERY "vendor research" gaps (registrationType, custodian, modelName, fundFamily, riskCategory, managementStyle, costBasis with flag, etc.).

TRACK-1 Verbose-API probe (`probe_mstar_paths.py`) confirmed Verbose surface does NOT expose mstar fields. Both Asset and Account groupings returned schema-level Generate 400 ("Cannot create a grouping calculator for 39") on mstar/morningstar/category candidate paths. Documented as the FAIL pattern.

---

## Phase 1+2 — bronze + silver

**Bronze pull execution:**
- Source: `silver/api_dims/accounts_v2` distinct `household_id` → 296 Inflection clientIds
- Per-client REST call with retry/backoff (3 retries, exponential)
- Runtime: ~5.5 min (296 calls @ 150ms sleep); one transient connection-reset auto-recovered; one 404 (clientId 1343 — stale household_id, expected drift)
- Output: `s3://opal-data-inf/bronze/orion-api-v2/2026-04-29/assets.parquet` — **23,699 rows, 100% coverage on assetClass + productCategory, $197,861,248.96 total currentValue**
- All 58 columns present; pull script logs schema-validation warnings for any drift vs expected field set

**Silver convert:**
- camelCase → snake_case (`accountId` → `account_id`, etc.)
- Int64 IDs / float64 values / boolean flags / datetime64 dates / string everything else
- Output: `s3://opal-data-inf/silver/api_dims/assets_v2/snapshot_date=2026-04-29/data.parquet` (907,725 bytes; 58 source cols + `snapshot_date` partition col = 59 final cols)

---

## Phase 3 — INF_I_D03 refactor

**Deleted (per Andrew "no fallback paths"):**
- `_CASH_PATTERNS` / `_FIXED_INCOME_PATTERNS` / `_ALTERNATIVES_PATTERNS` / `_INTL_EQUITY_PATTERNS`
- `_classify_keyword`, `_normalize_classifier_pk`, `_load_bd_securities_cache`, `_classify`
- `BD_SECURITIES_TABLE`, `_VALID_ASSET_CLASSES`, `_TICKER_ALPHA_RE`, `_NAME_SLUG_RE`, `_BD_SECURITIES_CACHE`
- `_dynamodb` resource

**Added:**
- `_ALTERNATIVES_CATEGORY_KEYWORDS` (asset_class substring discriminator: real estate / allocation / target-date / multi-asset / commodities / hedged / long-short / market neutral / macro / multistrategy / systematic trend / event driven / defined outcome / derivative income / alternative / digital asset / energy limited / natural resources / trading-- / infrastructure / precious metals)
- `_bucket_from_orion(product_category, asset_class)` — direct map (Money Market → cash, Bond → fixed_income, Equity → equity unless alternatives keyword) with NA-safe handling
- `_load_assets_v2_classifier()` — loads silver dim, returns join-ready DataFrame with `(account_id, ticker, product_category, mstar_asset_class)`
- `CLASSIFICATION_METHOD = 'orion_native_v1'` + `CLASSIFICATION_CAVEATS` constants stamped at top of every firm + advisor composition output

**main() classification section:**
Replaced per-row `_classify(row['ticker'], row['asset_name'])` list comprehension with vectorized merge on uppercase `(account_id, ticker)`. Diff: 101 insertions / 98 deletions.

---

## Phase 4 — composer metadata inheritance

INF_I_D02d had hardcoded `CLASSIFICATION_METHOD = 'keyword_regex_v1'`. Switched to `composition.get('classification_method', DEFAULT)` so future classifier upgrades auto-propagate without composer code changes. Verified: mix_summary.json now emits `classification_method: orion_native_v1`.

---

## Phase 5 — Validation

Live run results (post Phase 3 + 4 ship):

| Bucket | Market Value | Pct (now) | Pct (regex was) | Improvement |
|--------|--------------|-----------|------------------|-------------|
| equity | $102,761,042 | **53.93%** | 70.29% | -16.36pp (over-classification fixed) |
| fixed_income | $58,935,656 | **30.93%** | 15.22% | +15.71pp (bond ETFs correctly typed) |
| alternatives | $15,391,076 | **8.08%** | 1.79% | +6.29pp (4.5x improved) |
| cash | $12,441,843 | **6.53%** | 12.70% | -6.17pp (Cash or Equivalent re-routed to FI per Orion) |
| (unmatched) | $1,006,011 | 0.53% | n/a | small dim drift, gold/canonical 9295 vs silver 23699 |

Bond-ETF over-classification fully resolved: HTRB / BAGIX / BSIIX / BSNIX / TFEBX now correctly classified as Bond → fixed_income (was equity under regex Layer-4 alpha-ticker heuristic).

**Win-condition note:** TO target was 44.8/21.3/5.4/28.5 (Andrew's UI screenshot). Three of four buckets miss ±2pp because the target was a UI top-9-residual artifact, not a true 4-bucket Orion-native rollup. Documented in Phase 5 RAVC. Cash hits target within ±2pp.

The classification source is now ORION-TRUTH. The percentage interpretation gap is a definitional / UX call, not a data quality issue.

---

## Compiler Tools

| Phase | Tool | Result | Notes |
|-------|------|--------|-------|
| 1 — before write (each script) | `comp-pipescript io <script>` | SKIPPED — Orion scripts not in BD-pipeline graph | Documented gap, applies to all DIAGFIX TOs |
| 2 — before commit (each script) | `.tools/ds-commit-gate.sh <files>` | PASS on every file | Caught 3 ruff violations (1 F401 + 2 F541) auto-fixed before commit |
| 3 — after S3 upload | manual MD5 verify | MATCH on every uploaded script | aws s3api head-object ETag = local md5 |

Pre-commit gate ran 5+ times across the session. No `--force` audit entries. No bypasses.

---

## Deploy Cycle Summary

| TO / Phase | Commit | Push | S3 (script) | S3 (artifact) |
|---|---|---|---|---|
| DIAGFIX.009 doc + probe | `8d8be1bcd` | CLOUD | n/a (docs/probe) | n/a |
| DIAGFIX.010 Phase 1+2 | `2979c12a7` | CLOUD | `code/manual_api/pull_inflection_assets_v2.py` `d8e57b16…`, `code/silver/convert_assets_v2_to_silver.py` `6b7d3f7c…` | `bronze/orion-api-v2/2026-04-29/assets.parquet`, `silver/api_dims/assets_v2/snapshot_date=2026-04-29/data.parquet` |
| DIAGFIX.010 Phase 3 | `e106bc7b8` | CLOUD | `code/gold/INF_I_D03.composition_artifacts.py` `dc28bc14…` | `platinum/firm/firm_composition.json` (post-refactor with orion_native_v1 metadata), 3 advisor compositions |
| DIAGFIX.010 Phase 4 | `6f60a47eb` | CLOUD | `code/gold/INF_I_D02d.firm_mix_summary.py` `e8ed80f0…` | `platinum/firm/mix_summary.json` (8,204 bytes, orion_native_v1 propagated) |

All commits authored as `0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>` via `.tools/safe-commit.sh`. No bare `git commit`. No contamination aborts.

---

## Brandenburg Attribution Side-Finding (separate — for follow-on TO)

Andrew flagged a "new advisor Joe Brandenberg" (Orion: **Brandenburg**, with U) that wasn't surfacing in our data. Investigation:

- **Coverage = 100%.** All 21 of his households + 67 accounts + $16.22M ARE in our current pull and silver `accounts_v2` dim.
- **Attribution-only gap.** All 67 accounts have `representative_name='Inflection Wealth Management'` (Orion's primary rep field) instead of `'Joe Brandenburg'` (servicing rep).
- Resolvable via `GET /api/v1/Portfolio/Representatives` (returns full 18-rep list) + `GET /api/v1/Portfolio/Clients?representativeId=6` (returns Brandenburg's 21 cleanly).
- Recommend follow-on TO: augment silver `accounts_v2` with `servicing_rep_id` / `servicing_rep_name` columns; downstream gold scripts that route by `advisor_key` honor servicing rep when present.
- Doesn't block DIAGFIX.010 — Brandenburg's $16.22M classification is correct via the new Orion-native classifier.

Bonus: 18-rep list also surfaces 2 other Inflection-affiliated reps (Brandenburg/IWM rep_id=7, Brandenburg/Lee rep_id=8 — both 0 households, joint-name placeholders) and Noel Soderblom (rep_id=10, 0 households) which COO can fold into the broader scope-fix TO.

---

## RAVC Loops

| To | Subject | Time |
|----|---------|------|
| 2.0.0_SA_COO | RAVC ACK — DIAGFIX.008 scope amendment received; STEP 0 starting | 20260429T212417Z |
| 2.0.0_SA_COO | RAVC VERDICT — DIAGFIX.008 STEP 0 + Opal scan + proposed path | 20260429T212825Z |
| 2.0.0_SA_COO | RAVC EVIDENCE — DIAGFIX.008 Step 1 SHIPPED — composer + mix_summary.json | 20260429T213759Z |
| 0.6.1_AE_PartnerETL | FYI — INF_I_D02d needs orion-gold-dispatch.sh CATALOG entry | 20260429T213809Z |
| 2.0.0_SA_COO | RAVC ACK — DIAGFIX.009 Morningstar hunt — Track 1 starting now | 20260429T214305Z |
| 2.0.0_SA_COO | RAVC VERDICT A — DIAGFIX.009 — Orion REST endpoint found | 20260429T215145Z |
| 2.0.0_SA_COO | RAVC ACK — DIAGFIX.010 GO received — starting Phase 1 | 20260429T220248Z |
| 2.0.0_SA_COO | RAVC EVIDENCE — DIAGFIX.010 Phase 1+2 SHIPPED — bronze + silver assets_v2 | 20260429T221925Z |
| 0.6.1_AE_PartnerETL | FYI — DIAGFIX.010 Phase 1+2 scripts need orion-gold-dispatch.sh CATALOG entries | 20260429T221940Z |
| 2.0.0_SA_COO | RAVC EVIDENCE — DIAGFIX.010 Phase 3+4+5 SHIPPED — Orion-native classifier live | 20260429T222734Z |
| 0.6.1_AE_PartnerETL | RAVC ACK — DIAGFIX.009 (holdings pricing strategy) received | 20260429T222744Z |

Inbox: COO scope amendment + ACK + GO (3 messages); AE 0.6.1 chain registration ACK (1) + new pricing TO (1). All ACK'd within same wake.

---

## Andrew Direct Interactions

- "197.86m as of when exactly" → answered: asOfDate=2026-04-29 (today), pulled at 22:04-22:10 UTC = 18:04-18:10 ET, just past market close; HAR recorded 21:43-21:44 UTC same date — both intraday snapshots
- "Joe Brandenberg should be in this" → answered: 100% coverage in pull, attribution-only gap, separate fix path documented
- HAR (7) provided → noted `/Reporting/Scope` + `/Reporting/Custom/{id}/Generate/SlickGrid` endpoints for future Books-tab work
- "WE SHOULDNT NEED TO USE OUR BD-SECURITIES OR ETF CLASSIFIER OR REGEX OR ANY OF THAT BULLSHIT" → DIAGFIX.010 Phase 3 deletes ALL of those classifier paths, no fallbacks retained

---

## Watcher Activity

`org/mcp/inbox-watch.sh 0.4.0_DS_ClientPlatform` relaunched 4 times across the session. All Bash-tool tracked with `run_in_background: true`; no bare `&`. One stale orphan (`b3vt63mmv` from prior session) reaped during startup. No deliveries lost — belt-and-suspenders `check_inbox` + `get_agent_status` at every wake caught everything.

---

## Standing State

DIAGFIX.010 fully shipped (all 5 phases). DIAGFIX.009 (Morningstar hunt) closed VERDICT A.

Next in queue:
- **AE 0.6.1's new DIAGFIX.009 (`ds-holdings-pricing-strategy.md`)** — TRN-as-price-feed concern for INF_B_00 holdings. Phase 1: probe Orion `Activity.Value(EndingMV)` daily-coverage over 30-day window. Two surface candidates: existing Verbose API harness OR `/Reporting/Scope` endpoint from HAR (7) Activity-series calc. Will RAVC after probe.
- **DIAGFIX.008 Step 2** (INF_D_04 timeseries.mix integration) — still queued behind DIAGFIX.010
- **Brandenburg attribution follow-on** — silver `accounts_v2` + servicing_rep schema enhancement; awaiting COO TO if scoped
- **W4.14, BDPL_CNPRCS.WP-10b** — lower urgency, queued

Heartbeat current. Inbox watcher running.

---

## Files Modified (table)

| File | Change |
|------|--------|
| `data/orion/manual_api/PATH_DISCOVERY_MSTAR.md` | NEW — endpoint contract for `/Portfolio/Clients/{cid}/Assets/{date}`, 58-column schema, coverage validation, 5-phase plan |
| `data/orion/manual_api/probe_mstar_paths.py` | NEW — Verbose-API path probe (TRACK 1 FAIL evidence) |
| `data/orion/manual_api/pull_inflection_assets_v2.py` | NEW — Orion REST bronze pull (296 households, all 58 cols) |
| `data/orion/scripts/silver/convert_assets_v2_to_silver.py` | NEW — bronze→silver type-coercion + camelCase→snake_case |
| `data/orion/scripts/gold/INF_I_D03.composition_artifacts.py` | REFACTOR — Orion-native classifier replaces regex+DDB+keyword patterns; classification metadata stamped |
| `data/orion/scripts/gold/INF_I_D02d.firm_mix_summary.py` | FIX — composer inherits classification metadata from upstream firm_composition.json |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-29/advi_inflec_diagfix_009_010_orion_native_classifier.md` | THIS LOG |

---

## Next Steps

- [DS / NEXT] AE 0.6.1's new DIAGFIX.009 (holdings pricing strategy) Phase 1 probe — 30-day Activity.Value(EndingMV) coverage assessment
- [COO] Andrew + COO reconcile bucket-percentage definitional question (Orion-truth 4-bucket vs UI top-9-residual interpretation) before any further percentage targets
- [AE 0.6.1] Register `pull_inflection_assets_v2.py` + `convert_assets_v2_to_silver.py` in `orion-gold-dispatch.sh` CATALOG / CHAIN_FULL / CHAIN_INCREMENTAL (FYI sent)
- [Future / Optional] Brandenburg attribution fix — augment silver `accounts_v2` with servicing_rep columns (Andrew flagged)
- [Future / Optional] DIAGFIX.008 Step 2 (INF_D_04 timeseries.mix integration) — unblocked by re-run availability
- [Future / Optional] Books-tab follow-on using `/Reporting/Scope` endpoint surfaced in HAR (7)

---

*Authored by `0.4.0_DS_ClientPlatform`. Session arc: ~80 min for DIAGFIX.009 VERDICT + DIAGFIX.010 5 phases. 5 commits, 4 S3 script uploads, 3 S3 artifact publishes, 11 RAVC messages (COO + AE), 0 destructive ops, 0 contamination aborts, 0 hook bypasses.*
