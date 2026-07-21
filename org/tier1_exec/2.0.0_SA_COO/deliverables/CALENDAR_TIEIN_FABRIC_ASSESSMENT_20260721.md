# Fabric-Wide Trading-Calendar / Ingestion Tie-In Assessment — 2026-07-21

**Author:** 2.0.0_SA_COO (coordination lane) · **Status:** read-only assessment complete → seeds OPAL_CONSOLIDATION workstream
**Co-owners:** 1.0.0_SA_CTO (architecture/gate) · governance boundary: 0.0.0_AB_MSTR

## Trigger (Andrew-direct, verbatim, 2026-07-21 ~14:40Z ET, via 0.4.0_DS_ClientPlatform~A)

> "today is 07/21/2026, yesterday was Monday 07/20/2026. Let's make sure we're managing expectations
> around weekends and trading holidays properly; we should have a calendar in a lib somewhere to this end.
> We want to assess ingestion schedule with that regard first of all, are we adequately tied into that so
> that we roll forward properly so that we dont have spikes to zero on non-trading days? Does the raw data
> already account for non-trading days?"

Coordination convergence (CTO+COO): assessment-first, read-only, per-pipeline; run as the discovery step
INSIDE OPAL_CONSOLIDATION (no new PRD); MDPF stays P0; convergence dispatches wait BEHIND the N=3 loop.
Governance boundary (MSTR): PRODUCER calendar-convergence = correctness/consolidation, CLEAR of the 07-17
suspend-new-alerts order; any NEW freshness/absence-twin ALARM off this = the suspended class → DEFER.

**Andrew refinement (2026-07-21 ~15:2xZ, via ~A, VERBATIM):** "It's not necessary to ffill every day, if it
currently is only trading days that is fine." => The standardization TARGET is the canonical trading-day
AXIS + frontier definition consumed universally, NOT a producer ffill-to-calendar-days mandate; roll-forward
is a SERVING-LAYER (FE-on-render) concern. This RATIFIES the assessment headline (trading-days-only is safe,
no zero-spike) and re-reads F-2 (bd/cot ffill) + the smartx forward-fill candidate as AXIS/FRONTIER adoption
targets, not ffill convergence — existing producer ffill is now PERMISSIVE (may stay), not mandated. The
`bdate_range` holiday-blindness finding STANDS (that is an AXIS-correctness defect, exactly what canonical-
axis adoption fixes). CTO owns how this binds the UNIVERSAL_TRADING_CALENDAR PRD framing.

## Method + coverage denominator (Verification Law #10)

Read-only comp-grep/comp-glob over LIVE producers (`data/*/scripts/{gold,silver}`, `black_diamond/archive/`
EXCLUDED) + targeted source reads. **Grounding = CODE-MECHANISM (producer roll-forward posture read from
source), NOT served-artifact-exercised.** The empirical served-artifact zero-spike check across the
2026-07-18/19 weekend is the ACCEPTANCE TEST at each convergence dispatch, not run in this read-only pass —
except MDPF, whose no-current-zero-spike is already CTO/DS~A-confirmed.
Pipelines grounded: bd, cot, inf, mdpf, assets/49F, etfs. orion + eclipse classified as source FEEDS (no
standalone served-gold producer dir).

## Canonical mechanism (exists, per CLAUDE.md NEVER#1)

`lib/trading_calendar.py` — the ONE NYSE frontier definition. API: `is_trading_day`, `prev_trading_day`,
`expected_last_trading_day`, `trading_days_behind`, `trading_days_between`, `trading_days_mtd/ytd`,
`total_trading_days_in_window`, `calendar_source`. Already consumed (vendored) by the 3 freshness ALARM
lambdas (bd-served-vintage-alarm, opal-assets-absence-check, schwab-bronze-freshness) — the ALARM side is
tied in and working. Andrew's question is about the PRODUCER side.

## Answer to Andrew's two questions

**Q1 — Does raw account for non-trading days?** No, and that is CORRECT. Every raw/bronze feed is
trading-days-only — there is nothing to record on a weekend/holiday. This is right by construction, not a
defect. (Uniform across bd/cot/inf/etfs/orion/eclipse.)

**Q2 — Tied in for roll-forward, no spikes to zero on non-trading days?** No live zero-spike mechanism
found. Every daily served time-series either forward-fills across non-trading days (bd, cot, mdpf,
assets/49F) or emits trading-days-only points with NO full-calendar zero-injection (inf). The zero-spike
failure mode (reindex to full calendar days WITHOUT forward-fill → weekend rows become 0/NaN) was NOT found
in any live producer. **The real gap is STANDARDIZATION, not a live break:** the roll-forward + frontier
logic in bd/cot is AD-HOC per-producer `ffill`/carry-forward, not converged onto the one canonical lib.

## Per-pipeline table

| Pipeline | Cadence | Roll-forward posture (source-grounded) | Canonical-lib tie-in | Zero-spike risk |
|---|---|---|---|---|
| **bd** (black_diamond) | daily | `ffill`/carry-forward: `silver/bd_price_update.py` (source=carry_forward), `gold/build_canonical_prices_v2.py`, `gold/D_02` reindex+ffill (anti-flicker) | AD-HOC; `D_03` tie-in is a tracked fast-follow (B_01), not yet | none found — forward-fills; STANDARDIZE |
| **cot** (cottonwood) | daily | mirror of bd (same `build_canonical_prices_v2`, `D_02` reindex+ffill) | AD-HOC | none found; STANDARDIZE |
| **inf** (infinity) | daily | series built from `client_performance` points (trading-day cadence); `INF_D_00d` `date_range` is descriptive METADATA, not a calendar reindex; no zero-fill | none direct; `INF_E_00` processes eclipse | none found — trading-days-only, no full-cal zero-inject |
| **mdpf** | daily | explicit `ffill` NAMED-delta (`dim_mdpf_non_model_assets`: "weekend/holiday rows are ffill of a prior trading day … NAMED structural delta"); aggregate on `canonical_trading_axis` | CANONICAL (base aggregate) + 1 stale local copy (GAP-A) | none (CTO/DS~A-confirmed no live zero-spike); 1-module convergence in flight |
| **assets/49F** | daily | `runners_49f/a00_dim_account` uses vendored `trading_calendar as tc` ("the ONE frontier definition"); `c00_account_gains` reindex | CANONICAL (vendored `lib/trading_calendar`) | none |
| **etf** (`data/etfs`) | **MONTHLY** | `avgcap_monthly_average` / `avgcap_bd_rps_recon` — monthly avg-cap recon; ETF netassets is an mdpf-fed feeder | n/a | n/a — monthly cadence, no non-trading-day risk |
| **orion** | source FEED | custody deep-history feed; roll-forward inherited by consumers (mdpf/assets) | via consumer | covered by consumer |
| **eclipse** | source FEED | model feed, processed in `inf/INF_E_00`; feeds mdpf model; roll-forward inherited by consumers | via consumer | covered by consumer |

## Findings — seed OPAL_CONSOLIDATION workstream

- **F-1 (GAP-A, IN FLIGHT):** `data/mdpf/scripts/gold/_trading_day_calendar.py` is a divergent stale copy
  (missing 2027 + frontier fns; docstring falsely claims a clean rename). Converge to a re-export of
  `lib/trading_calendar`. Low-risk 1-module fix, CTO-gated, DS proceeding now, non-blocking to N=3.
- **F-2 (convergence — BEHIND P0):** bd + cot roll forward via AD-HOC per-producer `ffill`/carry-forward,
  not the canonical lib. No live zero-spike, but the frontier + roll-forward definitions are un-converged →
  converge onto `lib/trading_calendar`.
- **F-3 (convergence — BEHIND P0):** bd `D_03` calendar tie-in is a comment-tracked fast-follow (B_01) →
  fold into the F-2 convergence.
- **GAP-B WITHDRAWN:** the MDPF aggregate is ALREADY calendar-tied (`canonical_trading_axis`) — CTO/~A
  re-grounded 2026-07-21.

## WS-3 Consumer Census — full runtime enumeration (for UNIVERSAL_TRADING_CALENDAR, PRD-seed @30bef2f85)

Andrew elevated the disposition (~14:59Z, direct to CTO): the calendar must be UNIVERSAL — every cloud
runtime imports it (Lambda Layer + EC2 S3-pull + drift-guard), not just gold-runners. CTO: "your assessment
IS WS-3 (consumer enumeration)." Extending the producer scan to all runtimes:

Method: whole-estate comp-grep for `trading_calendar` imports/vendors (23 files) + candidate patterns
(`business_day`, `bdate_range`, `weekday()`, `holiday`, `is_weekend`); vendored 3rd-party `dateutil` in
`layers/pyiceberg-nessie-deps` EXCLUDED; comp-tools/tests separated from runtime.

### A. Current consumers (already import/vendor the calendar)
| Consumer | Runtime | How | Drift note |
|---|---|---|---|
| `lib/served_vintage.py` | shared lib | imports canonical | shared-module nucleus already exists |
| `assets/49F a00_dim_account` | gold producer | vendored `trading_calendar as tc` | vendored |
| `mdpf dim_mdpf_aggregate_aua_timeseries` / `dim_mdpf_non_model_assets` | gold producers | `canonical_trading_axis` / ffill named-delta | base tied |
| `bd D_03.composition_artifacts` | gold producer | planned (fast-follow comment) | not-yet |
| `bd-served-vintage-alarm` (lambda_function + served_vintage) | Lambda | **VENDORED copy** | copy #1 |
| `opal-assets-absence-check` | Lambda | **VENDORED copy** | copy #2 |
| `schwab-bronze-freshness` | Lambda | **VENDORED copy** | copy #3 |
| `m365-mcp-gateway` (ssavail_contract, tools) | **EC2** | imports | EC2 consumer (SSAvail tax dates) |
| `mdpf/_trading_day_calendar.py` | gold producer | **DIVERGENT STALE copy** | copy #4 = GAP-A / F-1 |

=> FOUR vendored copies + one stale divergent copy = the drift surface the universal shared module +
drift-guard eliminate. (This is the mechanistic case FOR Andrew's elevation.)

### B. Candidate consumers — ad-hoc business/trading-day logic NOT on the canonical lib (migration targets; HYPOTHESES, per-consumer source-verify at migration time)
| Candidate | Runtime | Pattern | Why a candidate |
|---|---|---|---|
| `smartx_ingestion_pipeline/forward_fill_missing_dates.py` | Lambda | business_day forward-fill | roll-forward OFF-lib — directly in Andrew's roll-forward scope |
| `opal-assets/opal-assets-bd49f-daily-pull` | Lambda | business_day | producer-lambda business-day logic off-lib |
| inf silver: `_orion_api_silver_lib`, `convert_performance_to_silver`, `convert_transactions_to_silver` | silver | pandas `bdate_range` (Mon-Fri) | HOLIDAY-BLIND: `bdate_range` counts NYSE holidays as business days — verify usage (hypothesis, NOT a confirmed defect) |
| `inf silver/_orion_vendor_asof` | silver | `weekday()` as-of | off-lib as-of |
| `cot/cot_bronze_ingest` | bronze | business_day | off-lib |
| `infra/aws/compdiff/freeze_monitor` | monitor | business_day + weekday | off-lib — **MONITOR: classify vs the 07-17 suspend-new-alerts boundary at PRD time (migrate-existing vs new-twin)** |

### C. Excluded / non-runtime
3rd-party `dateutil` (layers) = vendored dep, not ours. comp-tools/tests (comp_freshness, comp_debris,
comp_pydeps, dup_scan, passcraft, registry-check, freshness_manifest_gen) consume the calendar for
tooling/analysis — migrate opportunistically, not runtime-critical.

Coverage denominator: whole-estate `trading_calendar` grep (23 files) + 5 candidate-pattern greps. Section-B
entries are grep-identified HYPOTHESES — each needs a per-consumer source read at migration time to confirm
it genuinely needs frontier/roll-forward semantics vs. a benign local date op.

## Bottom line

No live "spike to zero on non-trading days" defect exists anywhere assessed. Raw-is-trading-days-only is
correct. The producer roll-forward is real but AD-HOC (bd/cot) rather than converged on the single canonical
lib — a CONSOLIDATION/correctness standardization opportunity (OPAL_CONSOLIDATION WS), dispatched behind the
MDPF_REVAMP P0. No new alarms/twins (07-17 suspend order honored).
