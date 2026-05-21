# MDPF_ASSETS.029 Phase 0 — v0.9 historical-backfill DRY-RUN findings

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**TO:** MDPF_ASSETS.029 (Phase 0 only — non-mutating dry-run + mechanism validation)
**Routed to:** 1.0.0_SA_CTO~B (direct) + 2.0.0_SA_COO~B (separate CC send)
**Predecessor:** .028 (v0.9 49F re-scope, COMPLETE, commit dd3cd4d22)
**Status:** Phase 0 COMPLETE. HARD STOP — Phase 1 (the historical partition rewrite) is Andrew-gated and does NOT execute on this GO.

---

## TL;DR

1. **CTO~B's identity question — RESOLVED: `aggregate_aua_timeseries.json` is NOT `aum-timeseries.json`.** They are three distinct artifacts in two buckets with two producers. The naming similarity is a trap.
2. **The .029 named target (`aggregate_aua_timeseries`) is NOT consumed by the portal at all** — a whole-tree grep of `portal/` for `aggregate_aua_timeseries` returns empty. The "Daily AUA Analysis" chart reads `aum-timeseries.json` + `non_model_assets.json` — neither is the .029 target.
3. **Therefore .029-as-scoped does not, by itself, bring the chart onto v0.9.** The chart's historical v0.9-correctness is delivered by **.030**, not .029.
4. **.029 and .030 are still correctly sequenced and .029 is still necessary** — because `build_legacy_compat_emit.py` (the .030 script) *reads* the `aggregate_aua/{date}.json` partitions that .029 re-materializes. .029 → .030 is a real data dependency, not just an ordering preference.
5. **Mechanism validated end-to-end.** A scratch re-materialization of the overlapping date (2026-05-20) via `mdpf_aggregate_aua.py --date 2026-05-20 --source s3 --out <scratch>` reproduced the live v0.9 partition **bit-identically** (full artifact equal except `generated_at`; headline $1,748,030,393.45 to the cent).
6. **The scope of the rewrite is small:** 97 partitions (2025-12-23 → 2026-05-19) on the dry-run; 2026-05-20 is already v0.9 (.028) — a no-op. Bucket is versioned → rollback is `list-object-versions`.
7. **One honest cost flag (per CTO~B's invitation):** re-materializing *older* dates is a per-date **WS-B + WS-E feeder-chain re-run**, not just an aggregator re-run — that is gold-runner (EC2) compute and belongs in Phase 1, not a ~1h Phase 0. The overlapping-date validation was free because today's feeder outputs already exist; older dates' feeder outputs are pre-v0.9 and must be refreshed first.

---

## (Scope amendment) Chart-backward artifact enumeration

CTO~B's amendment: trace BACKWARD from the Model Portfolios "Daily AUA Analysis"
stacked-area chart and enumerate every artifact it consumes.

**The chart** — `portal/src/pages/ModelPortfolios.tsx` lines ~1149-1293,
the "Daily AUA Analysis" stacked-area chart — consumes exactly **two** daily-series
artifacts:

| Chart layer | React data var | useQuery key | Fetched from |
|---|---|---|---|
| per-model stacked layers (1a / 1c / 2a) | `rawTimeSeriesData` → `filteredAggregate` / `filteredByModel` | `aum-timeseries` | `getAUMTimeSeries()` → `/api/general/portfolios/aum-timeseries.json` |
| Non-Model overlay (1b) | `nonModelData` → `getNonModelAumForDate(nonModelData.time_series, …)` | `non-model-assets` | `getNonModelAssets()` → `/api/general/portfolios/non_model_assets.json` |

(`portal/src/api/portal-proxy.ts:314` and `:388` are the two `apiRequest` calls.)

**The three timeseries artifacts — distinct, do not conflate:**

| Artifact | S3 key | Producer script | Portal-consumed? | v0.9-sensitive? |
|---|---|---|---|---|
| `aggregate_aua_timeseries.json` | `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json` | `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py` (pure rollup of the per-date partitions) | **NO** — whole-`portal/` grep empty | Yes — its per-date partitions carry the basis |
| `aum-timeseries.json` | `s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json` | `data/mdpf/scripts/backfill/build_legacy_compat_emit.py` (the **.030** script) | **YES** — chart model layers | Model side (1a/1c/2a) — v0.9 did **not** change the model basis |
| `non_model_assets.json` | `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json` | `data/mdpf/scripts/backfill/build_legacy_compat_emit.py` (the **.030** script) | **YES** — chart Non-Model/1b overlay | **YES** — 1b is the v0.9-changed residual |

**Resolution of "is `aggregate_aua_timeseries == aum-timeseries.json`":** No.
Different bucket prefix (`platinum/mdpf/` vs `json/portfolios/`), different producer,
different consumer. `aggregate_aua_timeseries.json` is the platinum-MDPF rollup;
`aum-timeseries.json` is a legacy Model-Portfolios-page file. The portal chart reads
the latter, never the former. `aggregate_aua_timeseries.json` has no portal consumer
at all — its only readers are `data/analysis/fy2025_aggregate_opal_return.py` and,
critically, `build_legacy_compat_emit.py` (which reads the per-date `aggregate_aua/{date}.json`
partitions as its 2026-01-17-onward 49F source — see "(b) blast radius" below).

---

## (a) Backfill mechanism

**What .029 re-materializes:** the per-date partitions
`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json`, then the rollup
`aggregate_aua_timeseries.json` that bundles them.

`build_aggregate_aua_timeseries.py` is a **pure rollup** — it lists every
`aggregate_aua/{date}.json` and concatenates the series columnar; it has no
methodology of its own. The v0.9 basis lives entirely in the per-date partitions,
which are written by the WS-A aggregator `mdpf_aggregate_aua.py`.

**Per-date mechanism (one date D):**
```
mdpf_aggregate_aua.py --date D --source s3 --upload   # writes aggregate_aua/D.json
```
The aggregator has a built-in `--dry-run` (build + print, no S3 write) and `--out <path>`
(write to a local/scratch path) — **so Phase 0 is non-mutating by construction**: every
dry-run in this brief used `--out <scratch> --dry-run`.

**Full backfill (Phase 1):**
1. For each historical date D in 2025-12-23 … 2026-05-19: ensure the WS-B (1a/1c) and
   WS-E v0.9 (1b residual) feeder outputs for D exist on the v0.9 basis (see the cost
   flag below), then `mdpf_aggregate_aua.py --date D --source s3 --upload`.
2. Re-run `build_aggregate_aua_timeseries.py --upload` once at the end to rebuild
   `aggregate_aua_timeseries.json` from the 98 now-v0.9 partitions.

**Inputs the aggregator consumes** (per `mdpf_aggregate_aua.py` docstring, lines 35-38):
`model_aua_positions` (WS-B, account grain), `non_model_aua` (WS-E, firm×date grain),
`etf_net_assets` (WS-D). The aggregator reads feeder *outputs* — it does not compute
1a/1b/1c itself.

**Cost flag — the feeder-chain dependency (per CTO~B's "flag if real cost"):**
The overlapping-date validation below was free because 2026-05-20's WS-B/WS-E feeder
outputs already exist (today's daily run). For *older* dates, the WS-E `non_model_aua`
rows are on the **pre-v0.9 basis** (v0.8 full-BD-book `certified_aua`, or `pre_ruling2`).
Re-materializing an older partition on v0.9 therefore requires re-running **WS-E v0.9
(1b = Schwab_49F_whole − 1a − 1c, off the .028 crosswalk source) + WS-B per date**
*before* the aggregator. That is gold-runner (EC2) batch compute — it is **Phase-1
work, not a ~1h Phase-0 step.** Recommendation: Phase 1 begins with a feeder-output
historical-coverage + basis probe, then a per-date feeder re-run for any date whose
row is missing or pre-v0.9.

**Date range:** 98 partitions live today, **2025-12-23 → 2026-05-20**
(`aggregate_aua_timeseries.json` reports `n_dates: 98`, same span). The .029 TO's
"target: full series to 2024" is **not currently reachable from the partitions** —
the earliest partition is 2025-12-23, and 2025-12-23 itself is partial
(`opal_aggregate_aua: null`, model_aua only). Extending before 2025-12-23 would be
new data sourcing, not a re-materialization. **Recommend Phase 1 scope the backfill
to the 97 existing pre-v0.9 partitions (2025-12-23 … 2026-05-19)** and treat
"to 2024" as a separate question for Andrew/CTO~B.

---

## (b) Partition-write plan + blast radius

**Partitions Phase 1 would write:**

| Partition set | Count | Current basis | Phase-1 action |
|---|---|---|---|
| `aggregate_aua/2025-12-23.json … 2026-05-19.json` | 97 | v0.8 `(none)` / `pre_ruling2` | overwrite-in-place, v0.9 |
| `aggregate_aua/2026-05-20.json` | 1 | **already v0_9** (.028) | no-op / skip |
| `aggregate_aua_timeseries.json` (rollup) | 1 | mixed (97×v0.8 + 1×v0.9) | rebuild after the 97 land |

**Write mode — recommend overwrite-in-place.** The `opal-data-portal-v2` bucket has
versioning enabled, so every overwrite is recoverable via `list-object-versions`
(this is the same recovery path `build_legacy_compat_emit.py` already relies on).
A side-by-side prefix (`aggregate_aua_v09/`) would orphan `build_aggregate_aua_timeseries.py`'s
hard-coded `PLATINUM_PREFIX` and every downstream reader — not worth it. Versioning
gives the rollback story without the prefix fork.

**Blast radius — consumers of the .029-rewritten artifacts:**

| Consumer | Reads | Impact of the rewrite |
|---|---|---|
| **`build_legacy_compat_emit.py`** (the .030 script) | per-date `aggregate_aua/{date}.json` partitions — its 2026-01-17-onward 49F source | **This is the key one.** .030's historical `non_model_assets.json` backfill DEPENDS on these partitions being v0.9. → .029 must land before .030's historical phase. |
| `build_aggregate_aua_timeseries.py` | all partitions → rollup | rebuild after .029 |
| `data/analysis/fy2025_aggregate_opal_return.py` | `aggregate_aua_timeseries.json` | analysis script — picks up v0.9 on next run; no live-page impact |
| **the portal** | — | **none.** `aggregate_aua_timeseries.json` has no portal consumer (grep-verified). The live "Daily AUA Analysis" chart is untouched by .029. |

**The chart-reaching path is .030, not .029.** The chart reads `aum-timeseries.json` +
`non_model_assets.json`, both produced by `build_legacy_compat_emit.py`. So bringing
the *chart's* historical 1b layer onto v0.9 is a **.030** deliverable. .030's TO
already carries a `<scope_pending>` block (authored by COO~B 2026-05-20) anticipating
exactly this — that .030 must grow from "legacy-emit v0.9 re-scope (daily-forward)"
to "+ historical `non_model_assets.json` time_series backfill." **This brief confirms
that scope_pending: .030 must include the historical `non_model_assets.json` backfill,
and it gates on .029's partitions.** (`aum-timeseries.json`'s model layers — 1a/1c/2a —
need no v0.9 re-backfill: v0.9 changed only the 1b basis. .030 Phase 0 should confirm
the legacy emitter does not co-write a basis-dependent field into `aum-timeseries.json`.)

---

## (c) Sample validation (non-mutating, scratch location)

All re-materializations written to `.runtmp/mdpf029_scratch/` — no S3 object touched.

**Overlapping-date cross-check (AC1) — PASS, bit-identical.**
`mdpf_aggregate_aua.py --date 2026-05-20 --source s3 --out .runtmp/mdpf029_scratch/scratch_2026-05-20.json --dry-run`,
diffed against the live `aggregate_aua/2026-05-20.json` (the .028 v0.9 daily-forward output):

| Field | Scratch re-mat | Live partition (.028) | Match |
|---|---|---|---|
| opal_aggregate_aua | 1,748,030,393.45 | 1,748,030,393.45 | ✓ |
| model_aua | 1,442,971,318.19 | 1,442,971,318.19 | ✓ |
| sma_aua | 24,929,683.38 | 24,929,683.38 | ✓ |
| non_model_aua | 386,383,756.96 | 386,383,756.96 | ✓ |
| methodology_version | v0_9 | v0_9 | ✓ |
| **full artifact (ex `generated_at`)** | — | — | **EQUAL** |

The mechanism reproduces the .028 daily-forward output **to the cent and bit-identically**
on the overlapping date — and $1,748,030,393.45 is the exact .028 RAVC2 reconciliation
headline. The per-date re-run mechanism is sound.

**Older-date basis characterization (read-only, plausibility):**

| Date | methodology_version | opal_aggregate_aua | Note |
|---|---|---|---|
| 2026-05-20 | v0_9 | $1,748,030,393.45 | .028 daily-forward |
| 2026-05-19 | (none) — v0.8 | $1,848,801,032.18 | full-BD-book `certified_aua` basis |
| 2026-02-17 | pre_ruling2 | $1,465,158,307.76 | older basis; `sma_aua: null` |
| 2025-12-23 | (none) | null | partial — earliest partition, model_aua only |

**The boundary skew is real and large:** 2026-05-19 (v0.8, $1.849B) → 2026-05-20
(v0.9, $1.748B) is a **−$100.8M overnight step that is pure methodology artifact**,
not market. This is precisely what the historical backfill removes — after Phase 1,
2026-05-19 re-materializes onto v0.9 (~$1.748B less one day of market drift) and the
series is smooth across the boundary. It also means: **until .029 + .030 land, any
chart that splices a v0.9 daily-forward tail onto a v0.8 history will show a ~$100M
cliff at the .028 cutover date.** That is the user-visible stake.

**Not done in Phase 0 (correctly deferred):** a scratch re-materialization of an
*older* date. That requires the WS-B+WS-E feeder chain re-run per date (the cost flag
in section (a)) — gold-runner compute, Phase-1 work. The overlapping-date bit-identical
result is sufficient to validate the *aggregator* mechanism; the feeder-chain re-run
is validated as Phase 1's first gated step.

---

## (d) Risk / blast radius / rollback

| Risk | Severity | Mitigation |
|---|---|---|
| A wrong rewrite corrupts the historical series | Med | Bucket versioning → `list-object-versions` + restore prior version per key. Pre-flight: copy all 97 partitions + the rollup to a local `.runtmp` backup before any write (mirrors `build_legacy_compat_emit.py`'s own pre-flight discipline). |
| Feeder outputs unavailable / pre-v0.9 for historical dates | **High — the real Phase-1 risk** | Phase 1 starts with a feeder-output coverage+basis probe; re-run WS-E v0.9 + WS-B per date as needed. Do NOT run the aggregator against stale v0.8 feeder rows — it would silently emit a v0.8 number stamped v0_9. |
| .030 reads partly-rewritten partitions mid-backfill | Med | Sequence: complete ALL 97 partition writes + the rollup rebuild, verify, THEN GO .030's historical phase. .029 and .030's historical phases must not interleave. |
| "to 2024" expectation vs 2025-12-23 partition floor | Low | Flagged above — recommend Phase 1 scope to the 97 existing partitions; "pre-2025-12-23" is a separate Andrew/CTO~B question. |
| Boundary skew persists if only one of .029/.030 ships | Med | The chart is fixed only when .030's historical `non_model_assets.json` backfill lands. .029 alone leaves the live chart on v0.8 history. Communicate .029+.030 as one user-visible deliverable. |

**Rollback story:** every Phase-1 write is to a versioned bucket; rollback = restore
the prior object version for each of the 98 keys (97 partitions + rollup). A local
pre-write backup of all 98 objects is the belt-and-suspenders. No partition is
deleted — only overwritten — so there is no destructive-op gate to clear.

---

## Recommendation to CTO~B (for the Andrew go/no-go)

1. **.029 is correctly scoped and necessary** — but its deliverable is the platinum
   `aggregate_aua/{date}.json` partitions + the rollup, which feed `build_legacy_compat_emit.py`,
   **not the portal directly**. Frame it to Andrew as the *upstream half* of a
   two-TO fix.
2. **Confirm .030's `<scope_pending>`** — .030 must grow to include the historical
   `non_model_assets.json` time_series backfill; that is the half that actually moves
   the live "Daily AUA Analysis" chart. .029 and .030 together = the chart on v0.9.
3. **Phase 1 mechanism is proven** for the aggregator step (bit-identical overlapping-date
   re-mat). The open Phase-1 cost is the **per-date WS-B+WS-E feeder-chain re-run** —
   recommend Phase 1's first step is a feeder-output coverage probe + a 3-date scratch
   batch before the full 97-date sweep.
4. **Scope the backfill to 2025-12-23 … 2026-05-19 (97 partitions).** "To 2024" is not
   reachable from the existing partitions — defer as a separate question.
5. **Non-destructive throughout** — versioned bucket, overwrite-in-place, local
   pre-write backup. No destructive-op gate. Consistent with Andrew's "be ginger."

**HARD STOP.** Phase 1 (the rewrite) does not execute on this GO. Awaiting CTO~B's
review + the Andrew go/no-go relay.
