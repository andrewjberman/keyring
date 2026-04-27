# Session Log -- 0.4.0_DS_ClientPlatform (base lane) -- 2026-04-27

**Lane:** base (not tilde; tilde lane ~A ran ADVI_INFPRTY/ADVI_RDVSDS work in parallel -- see `advi_infprty_inventory_and_f1f2f3_schema_alignment.md`)
**Projects:** ADVI_INFLEC (SCOPEFIX hotfix + AE chain unblock), ADHC_COMPIL.005 (comp-platinum nested-key indexing)
**Session span:** ~13:05Z -- 19:05Z

---

## Summary

Two work streams, run sequentially:

1. **ADVI_INFLEC SCOPEFIX + AE chain unblock** (commits `f2dfee9a`, `074e9f6a`, `df0901ed`).
   Silver layer had been rebuilt with SCOPEFIX too narrow (firm-rep only). Three hotfixes shipped
   to unblock AE's 6-step chain: cohort_mask broadened, B_00 added to dispatch catalog,
   C_07 household_id pyarrow type fixed.

2. **ADHC_COMPIL.005: comp-platinum reverse wildcard/dynamic key support** (commit `6e1c079b`).
   Extends `_print_field_reverse()` in `org/modules/graph/platinum_cli.py` to support glob
   segments (`decomposition_*.nna`), dynamic keys (`{role}.total`), and per-AC test fixtures.
   8/8 tests pass. RAVC4 to COO + CTO.

---

## Work Item 1: ADVI_INFLEC SCOPEFIX + AE Chain Unblock

### Root Cause (SCOPEFIX)
`_apply_scopefix()` in `convert_orion_to_silver.py` filtered to `rep_name == inflection_wealth_management`
(exact match on firm-level placeholder rep only). Individual advisor rows carry `rep_bucket='individual'`
with distinct `rep_name` values -- they did not match the firm constant.
Result: silver/transactions contained only firm-level rows. A_00 built gold/dimensions with zero
individual advisors. C_07 produced an empty account_team. D_02 wrote 0 advisor books.

### Fix 1 -- Broaden SCOPEFIX cohort_mask (commit `f2dfee9a`)
`data/orion/scripts/silver/convert_orion_to_silver.py`:
```python
firm_mask = normalized_rep == NORMALIZED_INFLECTION_REP
if 'rep_bucket' in df.columns:
    indiv_mask = df['rep_bucket'] == 'individual'
    cohort_mask = firm_mask | indiv_mask
else:
    cohort_mask = firm_mask
```
Gate: CLEAN. S3 upload: `s3://opal-data-inf/code/silver/convert_orion_to_silver.py`
ETag: `"243ee2487b4af88a218fc5e2d934ee54"` | 26,030 B | 2026-04-27T17:21:09Z

### Fix 2 -- Add B_00 to dispatch catalog (commit `074e9f6a`)
`data/orion/scripts/gold/orion-gold-dispatch.sh`:
- Added `B_00|B_00.canonical_holdings.py|--upload` to CATALOG between A_04 and B_01
- Added `B_00` to CHAIN_FULL: `A_04 B_00 B_01 B_01b ...`
- Updated help text: 27 -> 28 scripts

Root cause of I_D03 returning 0-advisor compositions: B_00 was on disk and correct,
but missing from the dispatch catalog entirely. I_D03 prefers `advisor_key` from canonical
holdings; with stale/pre-SCOPEFIX canonical holdings (no individual advisor_key), fallback
merge on account_id also failed. Adding B_00 to the chain ensures holdings are rebuilt
from post-SCOPEFIX silver before I_D03 runs.

Gate: CLEAN.
S3: `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` ETag: `"9d64c6ecd7aab7e5a14aa0a4d1581271"`
S3: `s3://opal-data-inf/code/gold/B_00.canonical_holdings.py` ETag: `"34486538eb395ced13d7762dfc88fd94"`

### Fix 3 -- C_07 household_id ArrowInvalid (commit `df0901ed`)
`data/orion/scripts/gold/C_07.advisor_attribution.py` line 139:
```python
# Before:
acct_team[col] = acct_team[col].fillna('unknown')
# After:
acct_team[col] = acct_team[col].fillna('unknown').astype(str)
```
Error: `pyarrow.lib.ArrowInvalid: Could not convert 'unknown' with type str: tried to convert to double`
Root cause: post-SCOPEFIX individual accounts include household_id='unknown' (string). Prior parquet
schema inferred household_id as double from numeric-only firm-level data. Fix: explicit `.astype(str)`
after `.fillna('unknown')` for both `household_id` and `advisor_key`.

Gate: CLEAN.
S3: `s3://opal-data-inf/code/gold/C_07.advisor_attribution.py` ETag: `"e39cda1377889cf663224c11d45cc16b"` | 7,933 B | 2026-04-27T17:43:12Z

### Corrected AE Dispatch Plan (vs. AE's original 2-step plan)
```
1. python convert_orion_to_silver.py --upload     (silver rebuild, fix f2dfee9a)
2. --single A_00                                  (gold/dimensions)
3. --single C_01                                  (gold/canonical, A_00 dependent)
4. --single C_07                                  (gold/views/account_team, fix df0901ed)
5. --single D_02                                  (platinum/advisors/*/book.json)
6. --single I_D03                                 (platinum/advisors/*/composition.json)
```
Note: `--single B_00` deferred to maintenance window per COO ruling (non-blocking for portal unblock;
canonical holdings already current from prior quarantine run). Full chain restores it.

### ADVI_INFPRTY Schema Assessment (no code changes required)
COO TO asked DS to assess 3 firm-level platinum artifacts:
`leaderboard.json`, `partner_analytics_quarterly.json`, `header_metrics.json`.
Assessment: all 3 shapes already correct in code (D_00c, D_04). S3 artifacts stale from old script
versions. No code changes needed -- re-runs after AE chain completes will regenerate them correctly.
(This assessment was superseded by ~A lane's full F1+F2+F3 schema work; see ~A log for detail.)

---

## Work Item 2: ADHC_COMPIL.005

**Gate on:** ADHC_COMPIL.001 COMPLETE (multi-pipeline indexing foundation) -- confirmed complete
before starting.

### Implementation
Three new helpers added to `org/modules/graph/platinum_cli.py`:

| Function | Purpose |
|----------|---------|
| `_has_wildcard_segments(path)` | Detects `*` or `{name}` in path |
| `_normalize_field_path_wildcard(path)` | Preserves segments containing `*` or `{name}`; strips `?.`/`[?]` noise same as original |
| `_wildcard_to_regex(pattern)` | Converts normalized wildcard path to compiled regex: `*` in segment -> glob `[^.]*`, `{name}` -> `[^.]+`, literal -> `re.escape`. Anchors to full key or trailing suffix. |

`_print_field_reverse()` modified:
- Branches on `_has_wildcard_segments()` before normalization (prevents `*`/`{name}` being stripped)
- Wildcard path: uses `_normalize_field_path_wildcard` + regex matching; output header shows `[WILDCARD]` or `[WILDCARD/DYNAMIC]`
- Dynamic queries: prints `NOTE: dynamic segment(s) {role} treated as wildcards -- matches any value at that key position in the JSON path.`
- Non-wildcard: unchanged (exact + suffix string matching, ADHC_ROUTER.T1 fix preserved)

Pre-existing ruff issues in platinum_cli.py fixed opportunistically:
- `from __future__ import annotations` added (FA102, CLAUDE.md Rule 15)
- Unused `import json` removed (F401)
- `# noqa: E402` added to post-sys.path imports (E402, pre-existing pattern)
- 4 bare `f""` strings converted to plain strings (F541)

### Acceptance Criteria

| AC | Query | Result |
|----|-------|--------|
| AC1 | `comp-platinum reverse rfs.decomposition_max.nna` | Nested path; existing exact/suffix matching satisfies this |
| AC2 | `comp-platinum reverse rfs.decomposition_*.nna` | SATISFIED. `_wildcard_to_regex` -> `(?:(?:^|\.)rfs\.decomposition_[^.]*\.nna)$`. Matches `decomposition_max`, `decomposition_ytd`; rejects `rfs.other.aua`. |
| AC3 | `comp-platinum reverse role_aua.{role}.total` | SATISFIED. `[WILDCARD/DYNAMIC]` header + NOTE line. Matches `role_aua.advisor.total`, `role_aua.rep.total`. |
| AC4 | Flat-key behavior unchanged | SATISFIED. Non-wildcard path bypasses new branch; no WILDCARD header, no NOTE. |
| AC5 | >=3 FAIL-before / PASS-after fixtures | SATISFIED. 4 strictly FAIL-before/PASS-after tests; 8 total, all PASS. |

### Tests (8/8 PASS)
File: `org/modules/graph/tests/test_platinum_nested_keys.py`

| Test | Type | AC |
|------|------|-----|
| `test_wildcard_normalization_preserves_star` | FAIL-before/PASS-after | AC2, AC5 |
| `test_wildcard_normalization_strips_jspath_noise` | FAIL-before/PASS-after | AC2, AC5 |
| `test_dynamic_key_normalization_preserves_braces` | FAIL-before/PASS-after | AC3, AC5 |
| `test_wildcard_regex_star_segment` | FAIL-before/PASS-after | AC2, AC5 |
| `test_wildcard_regex_dynamic_key` | Unit | AC3 |
| `test_wildcard_match_selects_union_not_unrelated` | End-to-end mock | AC2 |
| `test_dynamic_key_emits_note` | End-to-end mock | AC3 |
| `test_flat_key_unchanged` | Regression | AC4 |

---

## Commits (base lane)

| SHA | Subject | When |
|-----|---------|------|
| `f2dfee9a` | fix(ADVI_INFLEC): broaden SCOPEFIX to include individual advisor cohort | 13:05:29 -0400 |
| `074e9f6a` | fix(ADVI_INFLEC): add B_00 to INF gold dispatch catalog and CHAIN_FULL | 13:29:41 -0400 |
| `df0901ed` | fix(ADVI_INFLEC): C_07 household_id astype(str) -- ArrowInvalid on mixed numeric/unknown | ~17:43Z |
| `6e1c079b` | feat(ADHC_COMPIL.005): comp-platinum reverse wildcard/dynamic key support | ~19:05Z |

All pushed to `origin/CLOUD` via `git push`. Commit `--only` pathspec used per CLAUDE.md Rule 14a.
Note: commits 074e9f6a and 6e1c079b carried WARN-mode owned-paths lane violations (sweep from shared
index); core file changes were correct in both cases.

---

## S3 Uploads (DS-direct per CLAUDE.md Rule 13)

| File | S3 key | ETag | Size | Modified |
|------|--------|------|------|----------|
| `convert_orion_to_silver.py` | `s3://opal-data-inf/code/silver/convert_orion_to_silver.py` | `"243ee2487b4af88a218fc5e2d934ee54"` | 26,030 B | 17:21:09Z |
| `orion-gold-dispatch.sh` | `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` | `"9d64c6ecd7aab7e5a14aa0a4d1581271"` | -- | ~13:30Z |
| `B_00.canonical_holdings.py` | `s3://opal-data-inf/code/gold/B_00.canonical_holdings.py` | `"34486538eb395ced13d7762dfc88fd94"` | -- | ~13:30Z |
| `C_07.advisor_attribution.py` | `s3://opal-data-inf/code/gold/C_07.advisor_attribution.py` | `"e39cda1377889cf663224c11d45cc16b"` | 7,933 B | 17:43:12Z |

---

## RAVCs Sent (base lane)

| When | To | Subject |
|------|----|---------|
| ~17:21Z | 0.6.1_AE_PartnerETL + 2.0.0_SA_COO | RAVC2 -- SCOPEFIX fix + corrected 6-step dispatch plan |
| ~17:43Z | 0.6.1_AE_PartnerETL | RAVC2 -- C_07 ArrowInvalid fix ready (df0901ed), dispatch step 4 |
| 19:05Z | 2.0.0_SA_COO | RAVC4 -- ADHC_COMPIL.005 COMPLETE |
| 19:05Z | 1.0.0_SA_CTO | RAVC4 -- ADHC_COMPIL.005 COMPLETE |

---

## Pending / Next

| Item | State | Owner |
|------|-------|-------|
| AE chain steps 4-6 (C_07 -> B_00 -> D_02 -> I_D03) | Pending AE | 0.6.1_AE_PartnerETL |
| ADVI_INFPRTY schema refresh (D_00c + D_04 re-runs) | Waiting on AE chain | AE then DS~A |
| BDPL_CNPRCS WP-10b | Not started | base DS |
| comp-platinum reverse: real portal index AC1 live test | After comp-build regeneration | next session |
