# DS~C Session 1 — INFGRO.004 NaN cleanup at JSON write boundary

**Date:** 2026-05-14
**Agent:** 0.4.0_DS_ClientPlatform~C
**Authorization:** DS~A + DS~B both ACKed ownership (00:13Z ping pre-session; replies received this session). Non-urgent; DE FE NaN-strip `e60ebf1a` was the partner-demo unblocker — this is the gold-side correctness-hardening fix.
**TO:** ADVI_INFGRO.004 (formally `pending`; per DS~B's 2026-05-12 audit, the leaderboard rollup body was already shipped by DS-base on 2026-05-13; this session covers the residual NaN-emit cleanup carved out as scope refinement post-chain.)
**Commit:** `de2286d67`
**Wall time:** ~25 min startup → ship → log

## TL;DR

`_aggregate_perf_per_advisor` (INF_D_00c.py:526-538) + `_aggregate_perf_firm` (lines 556-568) call pandas `.mean()`/`.median()` on filtered Series for 7 stat fields each (twr/drawdown/std_dev/r_squared/sharpe/sortino). When an advisor has zero non-null `twr_value` rows, pandas returns NaN; `float(NaN) * 100 = NaN`; `round(NaN, 4) = NaN`; `json.dumps` emits the literal token `NaN`, which is invalid JSON and breaks portal parse (currently masked by DE's FE NaN-strip `e60ebf1a`).

Picked Option B per COO routing: single-site defensive `_strip_nan()` recursive helper applied at `_write_json_s3` (line 128) + `allow_nan=False` tripwire on the `json.dumps` call. Catches all 14 specific NaN-leak sites in `_aggregate_perf_*` plus any future leaker from elsewhere in the script — defense-in-depth at the JSON boundary. ADHC_GOLDNAN candidate for cross-script audit.

## Why Option B over Option A

COO routed two options:
- **A:** `safe_aua_weighted()` (or `safe_mean()` / `safe_median()`) helper at the 14 emit sites in `_aggregate_perf_*`
- **B:** `_strip_nan` recursive dict-walk at `_write_json_s3` + `allow_nan=False` tripwire

Chose **B**:

1. **Single touch site** — 1 helper + 1 line modified in `_write_json_s3`, instead of touching 14 specific call sites across two functions.
2. **Defense-in-depth at the boundary** — catches NaN leakers from anywhere upstream, not just from `_aggregate_perf_*`. If a future field added to `_aggregate_gro_per_advisor_window` or any other producer leaks a NaN, the strip catches it without a per-site patch.
3. **Tripwire** — `allow_nan=False` raises `ValueError` if any non-finite slips past the strip (e.g. via a future code path that bypasses the helper or emits Inf instead of NaN). Fail-loud beats silent bad JSON.
4. **ADHC_GOLDNAN candidate** — single helper can be lifted into a shared utility (`data/orion/scripts/gold/_lib/json_safe.py` or similar) for the cross-script audit COO flagged. Option A's pattern would force 14 sites × N scripts.
5. **Misnomer-resistant naming** — the COO message's "`safe_aua_weighted()`" framing didn't quite match the actual code at lines 526-538/556-568, which use simple `.mean()`/`.median()`, not AUA-weighting. Option B sidesteps the naming ambiguity entirely.

## Code shape

Added at line 65: `import math`.

Added at lines 128-147 (just above `_write_json_s3`):

```python
def _strip_nan(obj):
    """Recursively replace non-finite floats (NaN, +Inf, -Inf) with None.

    Why: pandas .mean()/.median() on an all-null Series returns NaN, which
    json.dumps emits as the literal token `NaN` (invalid JSON, breaks portal).
    Surfaced 2026-05-14 via _aggregate_perf_per_advisor / _aggregate_perf_firm
    when an advisor had zero non-null twr_value rows. Defense-in-depth at the
    write boundary catches future leakers regardless of producer.

    Pairs with allow_nan=False on json.dumps as a tripwire — if any non-finite
    float slips past the strip, the write fails loud instead of emitting bad JSON.
    """
    if isinstance(obj, dict):
        return {k: _strip_nan(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_strip_nan(v) for v in obj]
    if isinstance(obj, float) and not math.isfinite(obj):
        return None
    return obj
```

Modified `_write_json_s3` (line 150-151):

```python
def _write_json_s3(obj, key):
    body = json.dumps(_strip_nan(obj), default=str, separators=(',', ':'), allow_nan=False)
```

Both writes (`LEADERBOARD_KEY` line 1224 + `GOLD_ARTIFACTS_LEADERBOARD_KEY` line 1226) route through `_write_json_s3`, so single edit covers both. The diagnostic `json.dumps` at line 1219 (size-logging only) and line 1230 (dry-run print) intentionally NOT touched — they use default `allow_nan=True`, are not the actual write, and their NaN-passthrough is harmless to logs.

## Sanity tests run pre-commit

| Case | Input | Output | Note |
|---|---|---|---|
| Leaf NaN | `{'avg_twr_pct': nan, 'median_twr_pct': 5.0}` | `{"avg_twr_pct": null, "median_twr_pct": 5.0}` | NaN → null |
| Nested NaN + Inf | leaderboard-shaped dict with nested dicts/lists, NaN + Inf at various depths | all NaN/Inf → null at every depth | Recurse over dicts, lists, tuples |
| Negative test | `json.dumps({'x': float('nan')}, allow_nan=False)` | `ValueError: Out of range float values are not JSON compliant: nan` | Tripwire confirmed live |

## Files Modified

| File | Change | Commit |
|---|---|---|
| `data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py` | +23/-1: `import math`; new `_strip_nan` recursive helper above `_write_json_s3`; `_write_json_s3` body computes `json.dumps(_strip_nan(obj), ..., allow_nan=False)` | `de2286d67` |

## Deploy Evidence

| Step | Result |
|---|---|
| `.tools/ds-commit-gate.sh` | `All checks passed!` — py_compile + AST undefined-name + ruff py39 |
| `git status data/orion/scripts/gold/` | Only target file dirty; clean to commit |
| Author | `0.4.0_DS_ClientPlatform~C <0.4.0_DS_ClientPlatform_C@opal.agent>` |
| Commit | `de2286d67` |
| Push | `2920719f8..de2286d67` — 5-commit advance (carried fcb36f20f / 7f0e664be / ec85f1a56 / 9574c6476 forward from local + mine) |
| safe-deploy.sh (pre-push) | `DEPLOYED [inf] data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py` PASS |
| S3 path | `s3://opal-data-inf/code/gold/INF_D_00c.portal_leaderboard.py` |
| S3 ETag | `b57a6258df2949ad911a20198d67816c` |
| S3 LastModified | 2026-05-14T14:02:05Z |
| S3 ContentLength | 57,059 bytes |
| SHA-MATCH structural verify | S3 file contains `import math` (line 65), `_strip_nan` defn (line 129), `allow_nan=False` (line 151) |

No merge conflict with DS~A's `fd11a33c2` (touches lines 615-628 in `_aggregate_gro_per_advisor_window`; mine touches line 65 import + lines 128-151 around `_write_json_s3` — disjoint).

## Compiler Tools

| Tool | Result |
|---|---|
| `grep -n "_write_json\|json.dump\|nan\|NaN"` | Located all NaN-relevant sites and the write boundary in one pass — preferred over `comp-pipescript` which (per DS~A 2026-05-14 log) has both a name-match bug and a bucket-scope gap for INF scripts |
| `.tools/ds-commit-gate.sh` | PASS — py_compile + AST + ruff py39 |
| `.tools/safe-commit.sh` | Clean commit, no index contamination this round |
| `.tools/safe-deploy.sh` (pre-push hook) | DEPLOYED [inf] PASS |
| Direct python sanity test | 3 cases (leaf NaN, nested NaN+Inf, negative test) all green pre-commit |

**Reaffirms surfaced bugs from DS~A 2026-05-14 log:**
- `comp-pipescript io <script>` returns the input as a "did you mean" suggestion (normalization-vs-matching mismatch)
- `comp-pipescript deployed <script>` only enumerates `opal-data-bd/code/{gold,silver}/` — INF scripts in `opal-data-inf` not covered

Both filed under known compiler-tools-maintainer queue per DS~A's log; no new bug surfaced this session.

## RAVC posture

This was a self-initiated cleanup carved out of INFGRO.004 post-ship, not a fresh RAVC-1 from COO. The 00:13Z ping by ~C asking who owns the scope received parallel ACKs from ~A (13:00:25Z) + ~B (13:06:26Z) routing it to me. Per RAVC §4, evidence-bearing close-out to COO + DE + ~A + ~B is the standard close.

## MCPs Sent (planned this turn after log commit)

| To | Subject |
|---|---|
| 2.0.0_SA_COO | RAVC2 — INFGRO.004 NaN cleanup shipped — de2286d67 — strip+tripwire pattern |
| 0.4.0_DS_ClientPlatform~A | Stand-down ACK — NaN side shipped, defense-in-depth chosen, no conflict with fd11a33c2 |
| 0.4.0_DS_ClientPlatform~B | Stand-down ACK — option B chosen, ADHC_GOLDNAN candidate per your suggestion |
| 0.4.0_DE_ClientPlatform | FYI — gold-side strip live; e60ebf1a FE strip becomes defense-in-depth (your call on rollback timing) |

## MCPs Received

| From | Subject | Disposition |
|---|---|---|
| 0.4.0_DS_ClientPlatform~A (13:00:25Z) | "NaN cleanup is YOURS" + Option A/B framing | Confirmed; chose B with rationale above |
| 0.4.0_DS_ClientPlatform~B (13:06:26Z) | "yes, please take it" + scope clarification (account_id-keyed not household_id-keyed) | Confirmed; scope matches code reading |

## Next Steps

| Recipient | Item |
|---|---|
| **Self — passive** | Strip materializes on next INF chain run. No fresh trigger needed from me; if AE 0.6.1's chain #30 hasn't completed yet, this lands in chain #30's output naturally. If chain #30 already terminal at de2286d67-precursor (`fd11a33c2`), the strip lands in chain #31 / next scheduled run. |
| **DE 0.4** | Defense-in-depth: gold-side strip + FE strip (`e60ebf1a`) now both live. FE strip can be rolled back at your discretion (no urgency — keep both is fine; gold tripwire `allow_nan=False` becomes the canary, FE strip becomes the safety net). |
| **CTO** | ADHC_GOLDNAN candidate: workspace-wide audit for `sum(...) / sum(...)` divide-by-zero patterns and pandas `.mean()`/`.median()` into JSON across `data/*/scripts/gold/*.py`. Single `_strip_nan` helper could be lifted into a shared utility. Not blocking; opportunistic per Andrew "annoys me to no end" rule-of-thumb posture (silver-no-slim 2026-05-13 precedent). |
| **AE 0.6.1** | No action needed from me. If chain #30 already terminal: next scheduled run picks up de2286d67. If chain #30 in-flight: lands automatically. |

## Decision Notes

1. **Option B beats Option A by 14× in touch count.** 1 helper + 1 line at the boundary vs 14 calls at producers. Plus the tripwire makes it self-policing: future regressions raise instead of leak. Cost: ~20 lines of code total, including the docstring.

2. **`allow_nan=False` was free.** It comes with the json.dumps signature. Combined with `_strip_nan`, the strip is the actual fix; `allow_nan=False` is a tripwire that asserts the strip caught everything. If it ever raises, that's a signal to extend `_strip_nan` (e.g. handle a new non-finite type).

3. **`math.isfinite()` covers NaN + Inf + -Inf in one call.** Simpler than `math.isnan(obj) or math.isinf(obj)`. The naming `_strip_nan` is slightly off (it also strips Inf) but that's idiomatic — Inf in JSON has the same invalid-token problem and the same null-substitution is correct.

4. **No merge conflict by design.** ~A touched `_aggregate_gro_per_advisor_window` (line 615-628, household_id dtype cast). I touched `_write_json_s3` (line 128 area) + import section (line 65). Disjoint blocks. Confirmed by reading the file post-pull.

5. **Carry-forward push.** My local had 4 unpushed prior commits from other agents (`fcb36f20f` SHARED.003 submodule bump, `7f0e664be` INFINC scaffolding, `ec85f1a56` DE log, `9574c6476` SHARED.002 submodule bump). Push range `2920719f8..de2286d67` carried all 5 forward. Standard behavior when local has accumulated others' commits without push — not a contamination issue (safe-commit.sh `--only` already scoped MY commit to just the one file).

## Session Telemetry

- Wall time: ~25 min (Step 1b startup → final session-log commit pending)
- 1 substantive commit (de2286d67)
- 1 file modified (+23/-1)
- 4 MCPs planned post-log
- 2 inbox-watch launches (1 exited mid-session post-broker-redelivery, relaunched)
- 0 escalations (clean defense-in-depth ship)
- safe-deploy gate PASS on first try
- Sanity tests: 3/3 green pre-commit
