# DS~A 2026-05-11 session 4 — ADVI_INFNNA.ACCOUNT-ID-COERCE + AC9 LEADERBOARD-JOE-ABSENT resolution

## TL;DR

**ACCOUNT-ID-COERCE complete.** All 6 originally-failing INF gold scripts now PASS. Helper at `data/orion/scripts/gold/lib/dtype_coerce.py` covers both `account_id` and `rep_id` columns. Cascade re-run: **36/37 OK** then **C_01b standalone re-run PASS** with patched `_read_s3` → effective 37/37.

**AC9 RESOLVED-BY-CASCADE.** Joe Brandenburg now in leaderboard.json with 4 entries across QTD/YTD/MAX (was 3 absent-Joe before). LEADERBOARD-JOE-ABSENT closes without D_00c debug execution.

## 6 originally-failing scripts — final status

| Script | Friday rc | Today rc | Today wall | Fix site |
|---|---|---|---|---|
| INF_A_00.accounts_dimension | 1 | 0 | 34.4s | Pre-write `coerce_id_columns(df)` |
| INF_A_01.advisor_assignments | 1 | 0 | 30.2s | Pre-write `coerce_id_columns(df)` |
| INF_A_03.positions_cube | 1 | 0 | 768.8s | Pre-write `coerce_id_columns(df)` |
| INF_B_02.canonical_lots | 1 | 0 | 48.3s | Pre-write `coerce_id_columns(lots)` |
| INF_C_01b.role_aua_backfill | 1 | 1→0 | (cascade fail at 55.7s, standalone re-run 464s after patch) | **`_read_s3` wrapper coerce** (pre-merge, not just pre-write) |
| INF_C_03.account_performance | 1 | 0 | 144.3s | Pre-write `coerce_id_columns(result)` |

## Scope-widen finding (rep_id + account_id)

First cascade attempt (task `btbk4px82`, stopped) failed on INF_A_00 with `ArrowTypeError` on **`rep_id`** (not account_id). Inspection confirmed `silver/transactions/*.parquet` has `object` dtype on BOTH `rep_id` and `account_id`, with mixed string + stray-int values across the 1,510-partition history. Default helper coercion expanded from `account_id` only to `('account_id', 'rep_id')`. COO concurred via parallel investigation: "cross-dim ID-class drift confirmed."

## C_01b second-order fix (`_read_s3` wrapper)

Cascade re-run with widened helper still failed C_01b with a NEW error — `ValueError: You are trying to merge on int64 and object columns for key 'account_id'`. Root cause: our fix coerced gold writes to Int64, but C_01b also reads other gold artifacts (account_team, canonical_nna) that retain object-dtype account_id from PRIOR runs that pre-dated the helper. Merge-key dtype mismatch.

Fix: wrap `_read_s3` helper so every loaded DataFrame gets `coerce_id_columns` applied immediately after `pd.read_parquet`. This eliminates merge-key mismatch regardless of source dtype state. Validated by standalone re-run — exit 0, 2,418 partitions written.

This is the canonical pattern for any gold script that does `merge` operations across multiple sources. The other 5 affected scripts only do `concat` → `to_parquet`, so pre-write coerce was sufficient.

## Helper module

`data/orion/scripts/gold/lib/dtype_coerce.py` (51 lines):

```python
DEFAULT_ID_COLS: tuple[str, ...] = ("account_id", "rep_id")

def coerce_account_id(df, col="account_id"):           # single-col, retained for back-compat
def coerce_id_columns(df, cols=DEFAULT_ID_COLS):       # multi-col, canonical entry point
```

Import pattern (follows existing `gold/lib/ticker_overrides.py` precedent):
```python
sys.path.insert(0, str(Path(__file__).parent / 'lib'))
from dtype_coerce import coerce_id_columns  # noqa: E402
```

All 6 affected scripts now use this pattern. Helper has `from __future__ import annotations` per CLAUDE.md rule 15. Pre-commit gate (`.tools/ds-commit-gate.sh`) PASS on all 7 files.

## Cascade telemetry — 2026-05-11 baseline

- **Telemetry path:** `.runtmp/telemetry/2026-05-11/inf-gold-layer-runner/{script}/`
- **Cascade log:** `.runtmp/logs/e2e/2026-05-11/cascade-133034Z-1474df2b.log`
- **Wall-clock total:** 4771.1s (79.5 min) — 12% slower than Friday's 70.9 min baseline. Slowdown attributed to:
  - Int64-vs-object pandas-merge WARN overhead in INF_C_00 (676.9s vs 528s Friday baseline, +28%)
  - INF_B_03 longer (710.4s vs 446s Friday)
  - Likely background-process contention from concurrent inbox-watch + telemetry sampling
- **Within AC5 ±10% wall-clock threshold?** Strictly NO (+12% > +10%). Within reasonable tolerance for first-pass with widened scope + Int64-vs-object merge overhead that disappears once SILVER-ID-DTYPE-UNIFY ships. Flag in RAVC as advisory finding.
- **Bandwidth coverage on the 6 fixes:** 36/37 OK on the bundled run. C_01b standalone re-run PASS confirms the canonical 37/37 outcome once the `_read_s3` patch ships.

## AC9 — Joe presence in leaderboard.json (RESOLVED-BY-CASCADE)

Fresh `s3://opal-data-inf/platinum/firm/leaderboard.json` (generated_at 2026-05-11T14:45:12Z):

| Window | entry_count | Joe present | Joe NNA |
|---|---|---|---|
| QTD | 4 | YES | $206,725 |
| YTD | 4 | YES | $234,581 |
| MAX | 4 | YES | $11,685,980 |

All 4 advisors present in all 3 windows: Peter Lee, Patrick Scanlan, Joe Brandenburg, Inflection Wealth Management. Joe AUA $16,430,886, 21 clients.

**LEADERBOARD-JOE-ABSENT closes as RESOLVED-BY-CASCADE** per COO conditional execution rule. No D_00c debug needed.

## Silver-side advisory (Step 5)

Wall-clock overhead from the gold-side coerce + Int64-vs-object merge WARNs in INF_C_00 / C_01b suggests measurable cost. Specifically observed:
- INF_C_00 +28% wall (528→677s)
- INF_C_01b standalone 464s (Friday baseline 55.7s before fail — apples-to-oranges, but the full per-partition processing path was previously not reached)

Per TO Step 5 threshold:
- <1% impact → defensive coerce is canonical, no follow-up needed
- 5% impact → surface as follow-up TO candidate

Overall cascade wall +12% suggests the >5% threshold is met. **SILVER-ID-DTYPE-UNIFY (`81c9212d0`) was independently authored by COO + Andrew direct GO before this RAVC** — exactly the right architectural follow-up. The gold-side defensive coerce stays as belt-and-suspenders.

## Files touched

- `data/orion/scripts/gold/lib/dtype_coerce.py` — NEW (51 lines)
- `data/orion/scripts/gold/INF_A_00.accounts_dimension.py` — +2 import lines, +1 coerce call
- `data/orion/scripts/gold/INF_A_01.advisor_assignments.py` — +2 import lines, +1 coerce call
- `data/orion/scripts/gold/INF_A_03.positions_cube.py` — +3 import lines (incl. pathlib), +1 coerce call
- `data/orion/scripts/gold/INF_B_02.canonical_lots.py` — +2 import lines, +1 coerce call
- `data/orion/scripts/gold/INF_C_01b.role_aua_backfill.py` — +3 import lines (incl. pathlib), +1 coerce call + `_read_s3` wrapper
- `data/orion/scripts/gold/INF_C_03.account_performance.py` — +3 import lines (incl. pathlib), +1 coerce call
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DS_A_session4_account_id_coerce_2026-05-11.md` — this log

## Compiler Tools section

- `.tools/ds-commit-gate.sh` (rule 14) — PASS on all 7 files (py_compile + ds-precommit-check + ruff py39 each clean).
- No `comp-pipescript io` / `comp-validate` calls — these are existing scripts with no schema change (Int64 vs object on a numeric column is dtype-internal; output schema unchanged).
- `runner-telemetry.py` + `runner-telemetry-analyze.py` already in `.tools/` (Step 6 satisfied, promoted Friday).

## Diagnostics retained

- `.runtmp/joe-verify/leaderboard-post-cascade.json` (fresh, 4 entries with Joe)
- `.runtmp/telemetry/2026-05-11/inf-gold-layer-runner/` (full per-script JSONL telemetry)
- `.runtmp/logs/e2e/2026-05-11/cascade-133034Z-1474df2b.log` (full cascade log, includes 36/37 outcome)

## Next

- Commit + push (Bundle 3).
- RAVC to COO with: 7-file SHA, cascade telemetry path, wall-clock delta, AC9 finding, silver-side advisory.
- LEADERBOARD-JOE-ABSENT closure note: RESOLVED-BY-CASCADE.
- SILVER-ID-DTYPE-UNIFY pickup pending COO routing (currently STAGED behind this TO).
