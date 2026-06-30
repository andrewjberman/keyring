# Refactor SPEC-3: Inflection — GOLD layer (unified analytics) + portal-feed addendum

**Author:** 3.0.0_SA_CVO (Andrew-direct refactor planning, ADVI_BREAKS unified-flow) | **Date:** 2026-06-30
**As-is reference:** `inflection-gold.md` (audit). **Upstream:** SPEC-1 bronze, SPEC-2 silver. **Status:** DRAFT → CTO PRD.

---

## 0. Governing principles (Andrew-locked, this layer)

1. **Gold SCRIPTS are fine as-is — do NOT rewrite the gold logic.** [Andrew 2026-06-30] The refactor here is the **CHAIN COMPOSITION + a partition-freshness contract**, not the A/B/C/D scripts. Everything served today is orion-api; that does not change.
2. **Gold is the ONLY place the two source domains join.** orion-api flows through gold today; **eclipse-api gold is PENDING — no approach yet** (deferred; §5). The cross-domain join lives here, nowhere upstream.
3. **TWO flows: full + incremental.** Full = historical rebuild (backfill/recompute). Incremental = the daily scheduled run.
4. **The incremental flow MUST refresh current-day holdings.** [Andrew-locked — the break-fix as design] Incremental runs `INF_B_00` (and the current-day B/C chain) for the **current date only** (single-date incremental, NOT a full historical recompute, NOT skipped). The fresh per-day snapshot must propagate through gold to the served header every run.
5. **Served value must tie the custodian to the cent** (inherits the no-tolerance value-parity gate): served AUA == current-day gold holdings == `positions_mv` == Orion.

## 1. The two flows (exact composition)

```
 FULL (manual / backfill / recompute):
   pull → silver → A_00..A_04 → B_00..B_03 → C_00..C_09 → D_*   (all dates / full history)

 INCREMENTAL (the scheduled nightly) — REVISED:
   pull → silver → [A_* cached*] → B_00..B_03 --date={today} → C_00..C_09 --date={today} → D_*
                                    ▲ current-day single-date build (CHEAP — per-day snapshot pass-through)
   *A_* (slowly-changing dims: accounts/advisors/fee/client) may stay full-cadence or cached — see §2 DECISION.
```

The change vs today: today's `CHAIN_INCREMENTAL` is `pull → silver → D_*` (skips A/B/C). **Revised incremental inserts the current-day B + C chain** so `gold/canonical/holdings_{today}.parquet` is built every run and `INF_D_04.load_latest_holdings()` reads fresh.

## 2. Why incremental must include current-day B_00 (the finding, as design)

`INF_B_00` is the bridge silver `positions_mv` → `gold/canonical/holdings_{date}.parquet`; `INF_D_04` serves `total.aua = load_latest_holdings().market_value.sum()` from that GOLD partition. Today's incremental refreshes `positions_mv` SILVER but **skips B_00**, so the gold partition isn't rebuilt and D_04 reads the stale T-1 partition (the +$1.72M). The incremental design isn't wrong — it just refreshed the wrong layer for D_04. Fix = build the current-day gold holdings every incremental run.

- **Feasibility (confirmed):** `INF_B_00 --date={today}` builds ONE snapshot date (the per-day Assets snapshot is a pass-through, not a reconstruction) — cheap, well within the incremental budget. Same for `B_01..B_03`, `C_00..C_09` single-date.
- `[DECISION]` **What incremental may still skip:** the A-stage slowly-changing dims (`accounts_dimension`, `advisor_assignments`, `fee_rate_history`, `client_dimension`). Candidate to cache / refresh on the full cadence rather than daily. CTO/DS confirm which A dims D_04 needs same-day vs which are safe to cache. (B + C are NOT skippable — they're daily-volatile.)

## 3. Partition-freshness contract (defense-in-depth)

- `load_latest_holdings()` must **assert `partition_date == data_as_of`** and **fail loud** if the current-day partition is missing — never silently serve T-1 (today's defect). [the precise change to `INF_D_04`; minimal, not a rewrite]
- This is the producer-side mirror of the TO-6 value-parity alarm (served vs `positions_mv`, exact-match): the chain produces fresh, the assert refuses stale, the alarm catches any residual.

## 4. Single-writer + shape gate (TO-2 — DONE, preserve)

`INF_D_04` is the sole writer of `platinum/firm/header_metrics.json` + has the shape gate (rejects thin payloads). `INF_D_00`'s stub emit is removed (`b0224d8cb`). Preserve — do not reintroduce a second writer of any served key.

## 4b. Price-source consolidation — REMOVE the yahoo thread (Andrew-locked 2026-06-30)

Orion's daily Assets snapshot self-prices the full active book every day, back to 2020-05-26 (CVO-confirmed; SPEC-2 §5.5). So the yahoo/interp `canonical_prices` history is redundant. **Repoint the 4 gold consumers off `canonical_prices` → `positions_mv` (Orion snapshot price):**
- `INF_B_00`, `INF_B_01`, `INF_B_01b`, `INF_D_07` — each currently reads `silver/prices/canonical_prices.parquet`; switch to the Orion `current_price`/`market_value` already in `positions_mv`.
- Retire the yahoo + interpolation legs of `INF_build_canonical_prices.py` (INF_S_00); retire `canonical_prices.parquet` + `historical_prices.parquet` + `backfill_yahoo_prices.py` (SPEC-2 §5.5).
- **Gating check per consumer (before delete):** confirm none needs a price for an asset on a date it was NOT held (outside `positions_mv`); for held-position valuation the snapshot covers it. **Posture:** remove now, reopen a 3rd-party price source only if a real gap surfaces.

## 5. eclipse-api gold — PENDING (no approach yet)

Deferred (Andrew). Eclipse data lands raw (`bronze/eclipse-api/`) + stubbed silver (`silver/eclipse-api/`); there is **no gold/analytics flow yet**. When designed, the cross-domain join lives HERE (account by `int()`-coercion, model by name; ~96.6% reconcile, ~3.4% valuation-lag — D3 §6). Stub section; do not build under this spec.

## 6. The break — current state (MECHANISM CORRECTED 2026-06-30, source-confirmed)

**CORRECTION (Rule 22):** my earlier premise "scheduled = incremental, skips INF_B_00" was an INFERENCE and is **REFUTED**. DS~A source-confirmed (eventbridge.tf:164 `mode="full"`; trigger:183/263; today's runner ps `--chain full`; B_00 wrote 06-20..28): **the scheduled nightly runs `--chain FULL` and DOES run B_00** every night. `CHAIN_INCREMENTAL` is MANUAL-only.
- **The real recurring root = the FULL chain HANGS on `pull_inflection_performance_rest.py`** — PERF pull sits BEFORE positions/B_00 in CHAIN_FULL (confirmed pos 1 vs 9/11), so the hang kills the chain before B_00 ever runs → no fresh holdings (AE ground-truthed the hang: 103min, 41min). **The deployed timeout-tolerate is the durable fix.**
- TO-2 (`b0224d8cb`) fixed only the dual-writer clobber; the stale-partition symptom is real and was OPEN, but its mechanism is the perf-hang, not an incremental-skip.
- RESIDUAL to confirm (the acceptance bar verifies it): does a NON-hanging full run build the **current-day** (T) holdings partition, or T-1? (06-29: B_00 ran but wrote through 06-28 only.) If T-1, there is a B_00 date-coverage gap atop the hang.

## 7. Retroactive / migration work

- **G-R1 — revise `CHAIN_INCREMENTAL`** (insert `INF_B_00..B_03 + C_00..C_09 --date={today}`): **PARKED for the nightly** (the nightly is `--chain full`, not incremental — §6 correction). Keep as the design contract for the MANUAL/future incremental path. The nightly's durable fix is the deployed **perf-hang timeout-tolerate** (so the full chain reaches B_00).
- **G-R2 — `load_latest_holdings` partition-date assert** (the §3 fail-loud) — minimal INF_D_04 edit.
- **G-R3 — `[DECISION]` A-stage cadence** — confirm which A dims incremental can cache vs must rebuild.
- **G-R4 — backfill** the missing current-day holdings until the fix lands (operational; the live 06-30 staleness).
- **Parity gate:** after the fix, served AUA == current-day `positions_mv` == Orion to the cent, several clean days (the no-tolerance value-parity bar) before calling inf GREEN.

## 8. Acceptance criteria (machine-checkable → PRD/TO)

- AC1: every incremental run produces `gold/canonical/holdings_{run_date}.parquet` (current-day partition exists).
- AC2: `INF_D_04.load_latest_holdings()` partition_date == served `data_as_of`; fail-loud on mismatch (no silent T-1).
- AC3: served `total.aua` == current-day `positions_mv` sum == Orion, to the cent (no tolerance).
- AC4: single-writer per served key preserved (D_04 sole; no D_00 stub regression).
- AC5: full flow rebuilds all stages; incremental flow includes current-day B+C (not skipped).
- AC6: orion-api only in gold; eclipse-api gold absent (pending) — no cross-domain join shipped under this spec.

---

## ADDENDUM — how gold artifacts feed the portal

```
 inf-gold-layer-runner EC2 (end of chain)
   → writes gold/meta/pipeline-complete.json
   → (S3 ObjectCreated) → inf-portal-publisher λ  (generates platinum/firm/*.json)
        └ async → inf-portal-advisor-publisher λ → platinum/advisors/{advisor_key}/*.json
 platinum/{firm,advisors,clients}/*.json
   → GET /api/scoped/advisor-intelligence/... → CloudFront EVTSA9VEHNZVH
   → shared-advisor-router (λ@Edge, FIRM_BUCKET_MAP inflection→opal-data-inf) → S3-direct read
   → shared-advisor-router-response (λ@Edge: Cache-Control 60s + JSON-error envelope)
   → portal/src/api/endpoints/advisor-intelligence.ts → AdvisorIntelligence components
       getHeaderMetrics()      → platinum/firm/header_metrics.json   (firm AUA / NNA / by-architect / radial)
       getTimeseriesOverview() → platinum/firm/timeseries_overview.json
       getPartnerAnalytics()   → platinum/firm/partner_analytics_{granularity}.json
       (+ advisors/{id}/* , clients/{id}/* drill-downs)
```
Serving path (CloudFront + 2 λ@Edge + FIRM_BUCKET_MAP) is shared across all 3 firms and is sound — no change. RESIDUAL to confirm (from the gold audit): whether the gold D-scripts AND `inf-portal-publisher` both write `platinum/firm/*` (a possible second writer of a served key) — verify disjoint before the PRD; if overlap, same single-writer hazard as TO-2.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| read orion-gold-dispatch.sh (CHAIN_FULL/INCREMENTAL) + inf-gold-trigger (mode default/VALID_MODES) | the two-flow composition + the B_00-skip | PASS (rail-checked) |
| read INF_B_00 (--date single-date) | incremental-B_00 feasibility | PASS |
| live S3 (holdings partitions, pipeline-complete, git show TO-2 scope) | break still-occurring + TO-2 did-not-fix | PASS |

— 3.0.0_SA_CVO
