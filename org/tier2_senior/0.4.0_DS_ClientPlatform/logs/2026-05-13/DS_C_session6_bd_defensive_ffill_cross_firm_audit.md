# DS~C 2026-05-13 session 6 — BD cross-firm audit + defensive ffill ship

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~17:15Z → ~17:35Z 2026-05-13 (~20 min)
**Trigger:** Session 5 closed with INF NNA-oscillation fix shipped (`14c54aec2`); RD greenlit cross-firm BD audit for the same `cumsum + dict-lookup` pattern in BD's analog publisher Lambda or gold script.

## TL;DR

BD audit finding: **no visible bug, structural parallel.** BD's `D_02.advisor_client_detail._build_advisor_timeseries` (NOT the Lambda — gold script that D_04 pass-throughs to platinum) has the same `canonical_lookup` cumsum + dict-lookup pattern. **But BD canonical_nna upstream is daily-dense** (zero-padded on no-activity days), so the lookup never misses and the bug doesn't manifest. Shipped defensive `reindex+ffill` fix anyway (`74593520a`) — idempotent on dense input, prevents regression if BD upstream ever optimizes to sparse. Cost trivial, risk zero.

Also drafted complementary memory: `feedback_cross_firm_publisher_audit_pattern.md` (DS-angle on the methodology). RD already saved `feedback_alternating_pattern_fingerprint.md` (RD-angle on the diagnostic fingerprint). Linked via `[[name]]`.

## Cross-firm parity findings

| Pipeline | Canonical NNA upstream | canonical_lookup density | Bug visible? |
|---|---|---|---|
| INF | `gold/canonical/canonical_nna_{date}.parquet` — SPARSE (only activity-day rows) | Sparse | YES — visible oscillation in Patrick's chart, fixed `14c54aec2` |
| BD | `gold/canonical/nna/{date}.parquet` — DENSE (one row per account per date, zero-padded; ~99% rows have nna_txn=0) | Dense | NO — sampled 19 BD advisors, 0 of 19 show oscillation pattern |

Same Lambda/script code shape; different upstream density → different empirical surface.

## Ship roster

| Commit | Scope | Lines | S3 SHA-MATCH |
|---|---|---|---|
| `74593520a` | BD D_02 `_build_advisor_timeseries` `canonical_lookup` defensive ffill (mirrors INF `14c54aec2`) | +28/-2 | ✓ |

Memory entries:
- `feedback_cross_firm_publisher_audit_pattern.md` (NEW, DS-angle on methodology)
- `feedback_alternating_pattern_fingerprint.md` (RD-angle, already saved; my duplicate `feedback_sparse_cumsum_alternating_pattern.md` deleted)
- `MEMORY.md` index entry added

## Empirical audit evidence

Sampled 19 BD advisors at `platinum/advisors/{key}/timeseries.json`:
- 0 of 19 with oscillation pattern (>= 3 transitions zero ↔ non-zero at quarter ends)
- 1 of 19 (`august_vordenbaum`) with early-zero-then-monotonic (pre-firm-launch days zero, post-launch monotonic — correct behavior, not a bug)

Deep-dive on `abby_horton`:
- 742 daily rows
- 140 (18.9%) with `nna_canonical=0` — ALL in early period pre-first-activity
- 2025-03 through 2026-05 (15 consecutive months): 0% zero rate, 0% NaN
- Quarter-end values monotonic; DoD jumps tied to actual transactions

Cross-check of BD canonical_nna density:
- `gold/canonical/nna/2024-01-15.parquet`: 3236 rows, 3235 have nna_txn=0 (99.97% zero-padded)
- `gold/canonical/nna/2024-12-15.parquet`: 7075 rows, 7062 have nna_txn=0
- Confirmed: BD upstream is structurally dense → canonical_lookup is dense → lookup never misses → no flicker

## Defensive fix shape

```python
# Pre-compute per-advisor daily date map from acct (avoids 150x filtering)
_adv_daily_dates = (
    acct.groupby('architect')['date']
    .apply(lambda s: pd.DatetimeIndex(sorted(s.unique())))
    if 'architect' in acct.columns and 'date' in acct.columns
    else pd.Series(dtype=object)
)
for adv_name, adv_df in total_agg.groupby('advisor_name', sort=False):
    adv_sorted = adv_df.sort_values('date')
    cum_nna = adv_sorted['nna_txn_sum'].cumsum().values
    cum_inf = adv_sorted['inflow_sum'].cumsum().values
    cum_out = adv_sorted['outflow_sum'].cumsum().values
    if adv_name in _adv_daily_dates.index:
        cum_df = pd.DataFrame({'nna':cum_nna,'inf':cum_inf,'out':cum_out},
                              index=pd.DatetimeIndex(adv_sorted['date'].values))
        cum_df = cum_df.reindex(_adv_daily_dates[adv_name]).ffill().fillna(0.0)
        for d, row in cum_df.iterrows():
            canonical_lookup[(d, adv_name)] = (row['nna'], row['inf'], row['out'])
    else:
        # fallback to pre-fix sparse-build (shouldn't fire post-fix)
        for d, nna_v, inf_v, out_v in zip(adv_sorted['date'], cum_nna, cum_inf, cum_out):
            canonical_lookup[(d, adv_name)] = (nna_v, inf_v, out_v)
```

Idempotent on dense input: `reindex(target_dates).ffill()` where `target_dates ⊇ source_dates` is a no-op because every reindex target hits an existing source row (no NaN to ffill from).

## Known latent vulnerabilities NOT covered

Same code shape at 2 other build sites in `_build_advisor_timeseries`:
- `role_canonical_lookup` (L1874-1880) — per (date, advisor, role)
- `canonical_fee_lookup` + `canonical_nofee_lookup` (via `_build_bucket_lookup` L1900-1917) — per (date, advisor) fee bucket

These have the same latent vulnerability. Out of scope for this defensive ship — current BD data is dense so they all work; if BD ever ships sparse canonical_nna, all 3 need the same `reindex+ffill` treatment.

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| Live S3 BD audit — 19 advisors sampled + abby_horton deep dive + canonical_nna density check | 1× | 0 of 19 visible oscillation; BD upstream confirmed dense (97-99% zero-padded rows) |
| `ds-commit-gate.sh D_02.advisor_client_detail.py` | 1× | PASS — py_compile + ds-precommit + ruff py39 clean |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 1× | Clean first-try |
| `safe-deploy.sh` pre-push hook | 1× | DEPLOYED + SHA-MATCH `s3://opal-data-bd/code/gold/D_02.advisor_client_detail.py` |

## Files Modified

| File | Change | Commit |
|---|---|---|
| `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` | `_build_advisor_timeseries` canonical_lookup defensive ffill (idempotent on dense input) | `74593520a` (+28/-2) |
| `memory/feedback_cross_firm_publisher_audit_pattern.md` | NEW — cross-firm audit methodology entry | (memory write) |
| `MEMORY.md` | Add index entry for the new memory | (memory write) |

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **RD 0.4.2** | RAVC2 sent 17:34Z with commit hash + memory citations. Cross-firm audit closed. |
| **AE 0.6.0 (BD-side AE)** | FYI — defensive BD fix is `74593520a` on origin/CLOUD + S3-deployed. Picks up on next BD gold-d chain (04:00Z nightly unless triggered earlier). No urgency — no visible bug being fixed. |
| **AE 0.6.1 (INF-side AE)** | Standing position unchanged on v1.7.54 bundle. |
| **COO 2.0.0_SA_COO** | Hardening-pass proposal for `inf-portal-advisor-publisher` (3 bugs in one Lambda this session) — parked as follow-up post-v1.7.54. Will write proposal doc when greenlit. |
| **DS~C self** | Idle. /loop cron `526cad1f` checking inbox every 5 min. |

## Decision notes (worth keeping)

1. **"Same code, different data shape" is a real cross-firm gotcha.** When you find a bug in one tenant's code path, your first instinct is "the code is broken, same code in the other tenant must be broken too." But empirical data wasn't broken in BD — same code, dense upstream, no flicker. The structural reason matters: knowing WHY BD doesn't have the bug is what tells you whether a defensive fix is warranted.

2. **Pre-computing per-advisor daily date map once beats per-advisor acct filter.** Naive defensive fix: `acct[acct['architect'] == adv_name]['date'].unique()` inside the per-advisor loop. BD has 150 advisors → 150 full-acct filters → slow on large data. Pre-computing `acct.groupby('architect')['date'].apply(unique)` once gives the map for all advisors in a single pass.

3. **Idempotent defensive patterns are cheap insurance.** `reindex(target).ffill()` where `target ⊇ source` is a no-op. Adding it to currently-dense code paths costs zero correctness risk and prevents future regressions if upstream density changes. The pattern is worth applying whenever you encounter a "this works because of structural assumptions" code path.

4. **Out-of-scope latent vulnerabilities deserve commit-message citation.** I fixed only `canonical_lookup` (main one). 2 others (`role_canonical_lookup` + fee/nofee buckets) have same code shape. Documented in commit message as "known latent vulnerabilities NOT covered" so future maintainers know they exist + when to extend the fix.

5. **Cross-firm parity audit is a reusable methodology.** Today's 2 wins (display_label + sparse-cumsum) use the same audit pattern. Worth a separate memory entry so future investigators apply it routinely. Captured at `feedback_cross_firm_publisher_audit_pattern.md`.

## Pacing

20 min from RD GO to ship + memory + RAVC2. Quick audit (~10 min) + defensive fix (~5 min) + memory + handoff (~5 min). Cumulative session today: ~1.5 hr (sessions 1-6 covering 4 distinct INF brief responses + 1 BD cross-firm parity + 5 commits + 2 memory entries).
