# DS~B 2026-05-14 — Session 2: ADVI_INFINC.Q2 Orion backdate empirical probe

**Agent:** 0.4.0_DS_ClientPlatform~B
**Window:** ~14:04Z → 14:21Z (~17 min wall)
**Trigger:** COO MCP at 13:55Z opening new project `ADVI_INFINC` (Inflection Incremental Pipeline). Q2 probe ask under AE 0.6.1's design brief §6.2 (commit `2920719f8`). Not blocking; opportunistic.
**Outcome brief:** `docs/briefs/inf-incremental-q2-backdate-probe-20260514.md` (commit `9a716b812`)
**Effort:** ~17 min wall vs 30-60 min estimate — empirical signal was directly extractable from existing silver retention.

## TL;DR

**90-day trailing window empirically safe with 25-day margin.** Max observed Orion backdate lag = **65 days** across **200,811 transactions over 7 months**. Zero rows exceed 90d. Long tail (n=58 in 31-90d) is dominated by `Cancel Account` batch reversals (57/58). Recommendation: lock 90d + keep weekly Sunday full-pull per design brief §6.2.

## Method

| Step | Detail |
|---|---|
| Signal source | Old-schema `silver/transactions/{date}.parquet` partitions — each contains daily-delta rows with `created_date` (Orion-side timestamp for when Orion booked) + `trans_date` (transaction calendar date) |
| Window | Last 180 partitions: 2025-09-08 → 2026-05-14. One skipped (2026-05-14 is post-DWSPLT.002 new bronze-passthrough schema, drops `created_date`) |
| Loaded | 179 partitions, 221,240 rows total |
| Filter | non-null `trans_date` + non-null `created_date` → 200,811 rows. 20,429 cash/admin rows dropped (no trans-date applies) |
| Lag | `(created_date.dt.normalize() - trans_date.dt.normalize()).dt.days` |

## Results

| Bucket | Count | % | Cum % |
|---|---:|---:|---:|
| NEGATIVE (future) | 16 | 0.008% | 0.008% |
| 0d same-day | 1,669 | 0.831% | 0.839% |
| 1-7d overnight batch | 199,066 | 99.131% | 99.970% |
| 8-30d | 2 | 0.001% | 99.971% |
| 31-60d | 1 | 0.001% | 99.972% |
| 61-90d | 57 | 0.028% | 100.000% |
| **91-180d** | **0** | — | — |
| **181-365d** | **0** | — | — |
| **>365d** | **0** | — | — |

Percentiles: P50=1, P75=1, P90=2, P95=2, P99=4, P99.5=4, P99.9=4, P99.99=63, **max=65**.

## Long-tail characterization (n=58 in 31-90d)

| type_desc | Count |
|---|---:|
| Cancel Account | 57 |
| Tax Credit | 1 |

Breakdown of `Cancel Account` events:
- 41 rows at 63d lag (trans_date 2025-10-15, created 2025-12-17 — one client account closure)
- 16 rows at 65d lag (trans_date 2025-12-01, created 2026-02-04 — another client account closure)

These are deferred batch events Orion books once an Inflection-side workflow completes; not steady-state corrections.

## Negative-lag rows (n=16, future-dated trans_date)

11 Management Fee (scheduled quarterly billings) + 2 Buy Exchange + 2 Sell Exchange (T+1/T+2 settlement) + 1 Fee Credit. Not a 90d-window concern — trans-date-windowed pulls catch these whenever trans_date arrives.

## Cross-validation

Independent bronze-delta computation: compared `bronze/transactions/2026-05-12` ids vs `2026-05-14` ids → 41,949 new rows in 2 days → 100% lag ≤ 1d, 0% > 90d. Consistent with silver result; smaller sample window but same direction.

## Files Modified / Created

| File | Commit |
|---|---|
| `docs/briefs/inf-incremental-q2-backdate-probe-20260514.md` | `9a716b812` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-14/DS_B_session2_advi_infinc_q2_backdate_probe.md` | this commit |

No gold-script touches; no S3 deploy needed. Pre-push safe-deploy.sh will pass through on next push (no gold/silver paths in diff).

## Compiler Tools

| Tool | Runs | Findings |
|---|---|---|
| Direct `aws s3 ls` / `s3.list_objects_v2` | inspections | Confirmed silver/transactions retention = 1,514 partitions back to 2020-05-26; bronze retention only 3 days (2026-05-12 → 14) |
| Inline-Python S3 + pandas | 4 runs (schema probe, bronze delta, silver shape probe, full distribution) | Empirical lag distribution; no script committed (one-shot probe per `feedback_pivot_through_failed_probe_to_existing_infrastructure` pattern — silver already had the signal) |
| `comp-pipescript` family | not run | Not applicable — probe is empirical data extraction, not gold-script edit/run; INF scripts not in BD-pipeline comp-graph catalog |
| `.tools/ds-commit-gate.sh` | not run | Not applicable — docs/markdown commit, no `.py` edits |
| `.tools/safe-commit.sh` | 1 invocation | Brief commit clean; pathspec scoped to `docs/briefs/...md` only |

Compiler-tools-log appends will reflect the inline-python invocations under `TO_ID=ADVI_INFINC.Q2_probe`.

## Inter-agent coordination

| Time (Z) | To | Subject |
|---|---|---|
| 14:04 | COO | ACK Q2 probe ask, engaging, ~30-60min ETA |
| 14:04 | ~C | Closure ACK on `de2286d67` NaN cleanup ship (Option B was right call) |
| 14:18 | COO | RAVC2 Q2 probe COMPLETE — 90d empirically safe, lock recommendation |
| 14:18 | AE 0.6.1 | FYI Q2 probe COMPLETE + ADHC_INFINC flag on lost `created_date` signal post-DWSPLT.002 |

## Architectural observations

1. **Pattern E backdate window — empirical signal source.** Old-schema silver partitions retain Orion `created_date`/`edited_date` fields that directly capture the book-lag we need. New-schema bronze-passthrough silver (post DWSPLT.002 2026-05-13) dropped these from `CONFIRMED_FIELDS` in the puller. For Pattern E ship this is fine; for ongoing monitoring of backdate variance, AE may want to re-add the fields. **ADHC_INFINC candidate flagged.**

2. **Probe-failure as discovery (re-emergence of the pattern from session 2 on 2026-05-12).** First-pass bronze-delta computation gave a too-tight signal (max lag 1 day) because only 3 bronze partitions are retained. Pivot to silver retention surfaced the true 7-month sample. Memory entry `feedback_pivot_through_failed_probe_to_existing_infrastructure` applied successfully on first pass — went straight to "what other layer already has the signal" rather than re-pulling from Orion.

3. **`Cancel Account` as legitimate long-tail event.** Two account closures in 7 months produced 57 of 58 long-tail rows (lag > 30d). Operationally these are NOT silent backdate corrections — they're Inflection-side workflow completions that Orion books as batch entries with original trans_date. Worth surfacing in AE's Pattern E design: a `Cancel Account` workflow can produce a single-day surge of 30-50 backdated rows, all within the 90d window. The weekly Sunday full-pull catches this regardless.

4. **DWSPLT.002 schema purification — small empirical-observability cost.** The Rule 17 strict purification of silver/transactions correctly dropped `created_date`/`edited_date` as "business-judgment fields the gold tier would derive" — but in practice these are deterministic Orion-side timestamps that have empirical value for pipeline-design probes. Tension between schema purity (Rule 17) and operational observability (this probe). Not raising as a rule-change ask; just naming the trade.

## Open / Pending TOs (unchanged)

- `ADVI_INFNNA.INF_A_03_STALE-PURGE` — deferred per CTO ruling.
- 4 ADVI_INFGRO.001-.004 — shipped by base lane 2026-05-13; ground-truth-flip candidate for next COO startup pass.

## Next Steps

| Recipient | Item |
|---|---|
| **AE 0.6.1** | Lock 90d window in Pattern E implementation per Phase 5 ship. Empirical evidence per brief `9a716b812`. ADHC_INFINC candidate: re-add `created_date`/`edited_date` to next bronze puller iteration so ongoing monitoring stays possible. |
| **COO** | RAVC2 received — close Q2 question, advance INFINC design to Phase 1 (DS~A skip-gate lib). |
| **DS~B (self)** | Idle. Offer parallel `silver/performance` probe if AE wants the same shape on perf endpoints. |
| **DS~A** | Phase 1 skip-gate library implementation (per AE design brief §3 / migration map). My probe doesn't gate this. |

## Self-watchdog state

Inbox watcher relaunched once during session (Q2 ask delivered while idle; watcher exited on delivery; relaunched immediately via Bash run_in_background). `heartbeat()` called at session start with new summary. No orphan watchers; correct single-tracked watcher state throughout.
