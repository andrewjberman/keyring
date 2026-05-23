# MDPF Cohort 0 — 5/19 Re-fire Status + Structural Follow-ups Brief

**Author:** `0.4.0_DS_ClientPlatform` (Andrew-direct, sole-DS session 2026-05-19)
**Recipients:** `1.0.0_SA_CTO` + `2.0.0_SA_COO`
**Date:** 2026-05-19 ~17:00Z
**Status:** Live defect resolved. Three structural follow-ups identified — C-suite planning needed THIS SESSION.
**Predecessors:**
- Morning close-out log `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-19/MDPF_Global_v0_design_through_close.md`
- CEO methodology pivot log `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-19/MDPF_Global_v0_CEO_methodology_pivot.md`
- Spread-2 closure brief `docs/briefs/mdpf-aggregate-value-decomposition-spread2-closure-20260519.md`

---

## 1. Live state — incident resolved

Andrew flagged a visible Cohort 0 anomaly on the chart this afternoon (~16:30Z). Empirical investigation surfaced a chain-ordering race condition (NOT a formula bug). End-to-end re-fire executed at Andrew's direction.

### What was wrong

The MDPF daily chain ran at **11:02:59Z** today, ~100 seconds BEFORE the Eclipse 5/19 silver/gold partition finished uploading at **11:04:39Z**. The WS-A aggregator emitted `platinum/mdpf/aggregate_aua/2026-05-19.json` with only `49financial` in the `partners` array — Inflection was structurally absent because no Inflection feed existed for 5/19 at chain-start.

Downstream consequence: `etf_public_residual_total` = $109.11M (49F-side subtraction only) instead of $91.31M (with Inflection 2a-held Opal ETFs subtracted). The legacy emit `non_model_assets.json` inherited the over-stated Cohort 0 verbatim, which is what Andrew saw on the page.

### What got fixed (this session, ~16:48Z → 16:51Z)

| Step | Action | Result |
|---|---|---|
| 1 | `build_mdpf_wsc_inflection_feeder.py --date 2026-05-19 --bronze-date 2026-05-18` | 3 Inflection feeds written: model_aua_positions (399 rows), model_composition (168 rows), non_model_aua (1 row); 2a=$93.70M, 2b=$106.25M |
| 2 | `mdpf_aggregate_aua.py --date 2026-05-19 --source s3 --upload` | Platinum re-emitted; both partners present; `opal_aggregate_aua = $1,848,801,032.18`; reconciliation PASS |
| 3 | `build_legacy_compat_emit.py --upload` | Live `aum-timeseries.json` + `non_model_assets.json` refreshed; 80 rewrites |
| 4 | CF invalidation `EVTSA9VEHNZVH` paths `/json/portfolios/*` + `/api/general/portfolios/*` | Invalidation ID `ID6O4GASY5WSSF2EXUEQFYEQHA` InProgress |

### Final 5/19 state (live)

```
opal_aggregate_aua    : $1,848,801,032.18
49financial total_aua : $1,648,847,956.91   (1a $1,332.82M + 1c $24.96M + 1b $291.07M)
inflection total_aua  : $  199,953,075.27   (2a $93.70M + 2b $106.25M)
etf_public_residual   : $   91,310,278.05   (Cohort 0)

Per-ETF Cohort 0:
  DIVZ  $74,017,248.03   (NAV $241.85M - 49F $167.83M - Inf $0)
  IDVZ  $12,396,705.25   (NAV $158.66M - 49F $146.26M - Inf $0)
  PFDE  $ 2,078,795.98   (NAV $131.63M - 49F $119.77M - Inf $9.78M)
  PFOE  $ 2,817,528.79   (NAV $110.85M - 49F $100.01M - Inf $8.03M)
```

The $17.80M correction == Inflection's PFDE+PFOE allocation (target-weight × model_aua across 6 Inflection models). To-the-cent empirically reconciled.

---

## 2. The three structural follow-ups (C-suite focus)

These are the load-bearing concerns. The re-fire above is band-aid; absent these, the same defect recurs daily.

### Follow-up #1 — WS-C feeder is out-of-chain (root cause)

**The bug:** `build_mdpf_wsc_inflection_feeder.py` is NOT part of `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`. The chain runs:
```
Stage 1: WS-B (49F SmartX) + WS-D.1 (ETF NAV) + WS-D.2 (49F RPS) -- parallel
Stage 2: WS-E (49F 1b)
Stage 3: WS-A (aggregate)
Stage 4: ROLLUP (timeseries)
```
WS-C (Inflection) sits on its own cadence — invoked separately, today produced only the 5/18 partition at 10:02Z. When the chain ran at 11:02Z reading from `mdpf/feeds/*/inflection/`, the latest available partition was 5/18 and the aggregator's date-filter (`as_of_date == 2026-05-19`) returned empty → no Inflection in partners.

**Why this matters:** Inflection's 2a Opal-ETF holdings (~$17.8M today on PFDE+PFOE) are part of the Cohort 0 subtraction. If WS-C is missing for the run-date, Cohort 0 is silently over-stated by exactly that amount. The reconciliation gate (§7 identity_1) PASSES because aggregator-vs-partner-sum holds; the defect is in the absolute scale, which the gate is structurally insensitive to (sister to `feedback_identity1_masks_absolute_value_class.md` anchor class — destructive defect-detector class #6).

**Two architectural options:**

| Option | Mechanism | Properties |
|---|---|---|
| **A. Pull WS-C into the chain** | Add WS-C to Stage 1 parallel feeders (`wsc_inflection.py --date $RUN_DATE`). Stage 1 already has WS-B/D.1/D.2 in parallel; WS-C joins them. Chain blocks if any Stage 1 feeder fails. | Single dispatch boundary. Eclipse-availability becomes a Stage 1 dependency. If Eclipse isn't ready, WS-C fails → entire chain fails → ChainFailed=1 alarm. Recovery = retry chain after Eclipse lands. |
| **B. Gate WS-A on per-firm presence** | Keep WS-C separate. WS-A loops/sleeps waiting for both `49financial` and `inflection` partitions on `RUN_DATE` before emitting (with timeout + alarm). | Decouples cadences. WS-A becomes the chokepoint. Tolerant of WS-C running on its own schedule. Riskier: a stuck wait propagates timeouts; alarming + escalation needed. |

**Recommendation:** Option A. The chain is the architectural authority for daily run-state; WS-C belongs in it. Side benefit: single CloudWatch alarm covers all Stage 1 feeder failures. Estimated diff: ~5 lines in `mdpf-daily-dispatch.sh` + WS-C `--upload` flag confirmation + chain runbook update.

**Dependency:** Eclipse silver/gold cadence. Today the Orion-bronze upstream uploaded 2026-05-19 09:01Z (silver/assets_v2) and Eclipse silver itself at 09:01Z, with gold/eclipse/{date}/ at 11:04Z. Chain currently fires at ~11:02Z (cron hour-aligned). Pulling WS-C into the chain means either (a) chain shifts to ~11:30Z or (b) chain accepts a transient WS-C failure on early-fire days with retry. Both are operationally tractable; CTO call on which.

### Follow-up #2 — Strict Cohort 0 formula (Andrew-direct CEO directive refinement)

**Andrew verbatim 2026-05-19:** "cohort 0 is etf assets minus Opal ETF (IDVZ DIVZ PFDE PFOE) in 1a - 1c - 2a."

**Current implementation:**
```
Cohort 0 = etf_total_nav 
         - 49F_RPS_partner_held_etf   (sum of ALL 49F Schwab RPS positions in Opal ETFs; includes 1a + 1c + 1b)
         - inflection_target_weight_estimate (model_aua × is_opal_etf target_weight; 2a only)
```

The 49F-side subtraction is RPS-total — captures any 49F-account holding the Opal ETF regardless of whether the account is 1a/1b/1c. The strict formula wants only 1a + 1c subtracted from the 49F side.

**Magnitude of the gap (empirical today):** Unknown but probably small (49F 1b non-model accounts holding Opal ETFs would be rare — 1b is typically cash/CDs/non-Opal positions). Could probe by joining BD silver/allocations account_grain × Schwab RPS by account_id, filtering on `account_type ∈ {Bank, Savings, ...}` exclusion set. Estimated 1-2 hour DS probe.

**Architectural implication:** Even the strict formula has a methodology choice in it — whether to subtract Inflection-side 2b (Inflection's non-model accounts that hold Opal ETFs). Andrew's wording says 1a/1c/2a only, so 2b stays IN Cohort 0 (alongside truly-public holdings). Current code already does this; just needs the 49F-side narrowed.

**Implementation path:** Phase 3 work under existing TO #27. Requires position-grain join of (BD allocations × Schwab RPS) at SmartX-decomposable account-set granularity for 49F. Position-grain BD freshness is the bigger gap — BD `daily_positions.parquet` is stale 2026-01-27 latest. Not a blocker for the strict-formula correction, but reduces precision until refreshed.

**COO sequencing question:** how urgent vs Phase 1B? Today's gap is well under 1% of headline ($91.31M vs strict ~$91M); audit-acceptable. Defer to Phase 3 alongside BD position-grain refresh.

### Follow-up #3 — Cohort 0 absolute-scale sentinel (detect-class extension)

The 5/19 defect demonstrated that §7 identity_1 PASSES on a partition that's missing an entire partner. Cohort 0 went UP $17.78M day-over-day on data that shouldn't have moved that much; no gate flagged it.

**Proposed sentinel (Phase 2.5 hardening, sibling to MDPF_ASSETS.017 day-1-zero guard):**

```
Day-over-day Cohort 0 plausibility check:
  if abs(cohort_0_today - cohort_0_prior_business_day) > 0.5 * cohort_0_prior:
    ERROR -- "Cohort 0 moved >50% day-over-day; partner-missing-from-partition candidate"
  elif partners_in_partition != expected_partners_for_date:
    ERROR -- "Partners array missing {missing_set}; aggregator may have run before feeder"
```

The second clause specifically catches the WS-C-out-of-chain class. `expected_partners_for_date` is configured per-firm from the Eclipse/SmartX cadence calendar (49F always expected; Inflection expected from first-appearance date onward).

**Why this matters as a third-line gate:** identity_1 is row-consistency. Day-over-day series-walk is the second line (catches absolute-scale drift). Partner-completeness is the third line — catches structural absence that even a series-walk could miss on a single-day re-fire. Three independent classes. Each catches a class the others structurally cannot.

**Implementation cost:** Small — ~20 lines in `mdpf_aggregate_aua.py` reconciliation block + config artifact for expected_partners per-date.

---

## 3. Proposed TO sequencing — for COO

Current open TOs related to this:
- #16 (pending): WS-C Inflection feeder full historical (legacy; orthogonal — production WS-C exists, this is for backfilling 2024/2025)
- #27 (pending): MDPF Phase 1B + Phase 3 (canonical methodology + BD daily_positions historical)
- #28 (pending): MDPF_ASSETS.017 day-1-zero guard

**Recommended additions (3 new TOs):**

| TO# | Title | Lane | Effort | Priority |
|---|---|---|---|---|
| MDPF_ASSETS.018 | Pull WS-C Inflection feeder into mdpf-daily-dispatch.sh chain | AE-owned (chain edit) + DS RAVC | ~1h | **High** — recurs daily until fixed |
| MDPF_ASSETS.019 | Cohort 0 absolute-scale sentinels (day-over-day + partners-present) | DS-owned (`mdpf_aggregate_aua.py` reconcile block) | ~2h | **Medium** — detection complement, deploy with .018 |
| MDPF_ASSETS.020 | Strict Cohort 0 formula — 49F-side 1a/1c-only via position-level decomposition | DS-owned (Phase 3 scope) | ~1d | **Low** — gap <1% of headline; ride Phase 3 |

**Dependency graph:**
- .018 + .019 ship together (one chain edit + one sentinel; both prevent recurrence + detect recurrence; structural cousins)
- .020 rides Phase 3 work under #27 (position-grain freshness is the bigger gap; isolate to one effort)
- .017 (day-1-zero guard) and .019 (Cohort 0 sentinel) are siblings under MDPF Phase 2.5 hardening umbrella — both add reconciliation-layer plausibility gates

**Lane discipline:** .018 touches `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh` — that's AE-lane (Rule 13: DS owns gold/silver/bronze script commit→QA-deploy; chain dispatch infrastructure is AE). DS proposes the WS-C invocation block + RAVC-Request to AE; AE owns the chain edit + push to s3://opal-data-mdpf/code/.

---

## 4. Decision points C-suite needs to resolve (today)

1. **Option A vs B on Follow-up #1** — pull WS-C into chain (Option A, recommended) vs gate WS-A on per-firm presence (Option B). My read: A is cleaner and matches the chain-as-source-of-truth pattern. Confirming with CTO.

2. **Chain fire time** — current ~11:02Z is too early for Eclipse 5/19's 11:04Z upload. Options:
   - (a) Shift chain to 11:30Z (operationally simple)
   - (b) Add retry-after-Eclipse-arrival logic (more robust but more complex)
   - (c) Accept transient early-fire failures with manual re-fire (today's pattern; not durable)

   My recommendation: (a). The chain doesn't need to be at 11:02Z specifically; 11:30Z gives Eclipse + every other upstream a comfortable buffer.

3. **TO sequencing** — MDPF_ASSETS.017 (already opened for tomorrow AM) + the three new TOs (.018, .019, .020). Is the proposed sequence + priority acceptable? COO confirmation needed for COO TO-authoring on .018/.019 (recommended together for next 24-48h window) + .020 deferred under #27.

4. **AE Opt C bridge** — AE 0.7's Lambda Opt C (Cohort 0 manual emit path) is in flight per yesterday's thread. Does .018 (chain integration) preempt Opt C or supplement it? My read: .018 makes Opt C structurally unnecessary for the WS-C-in-chain case, but Opt C may still be useful as the manual-override path for edge cases. Confirming with AE this thread.

---

## 5. Why this matters strategically

Today's empirical pattern: a partition that PASSED §7 identity_1 to-the-cent silently understated Cohort 0 by 19% of its value because an entire partner was missing from the partners array. This is structurally the same class as the four prior anchors in `feedback_identity1_masks_absolute_value_class.md` (PFOE over-attribution, Spread-2 vintage spread, SmartX day-1-zero, INFGRO Finding A/B). It's the SIXTH anchor in 24 hours.

The pattern is clear: **identity_1 + per-cohort series-walk + partner-presence completeness are three orthogonal classes of correctness gates.** Today's incident proves each catches a class the others structurally cannot. The strategic implication for MDPF: every Phase 2.5 hardening sprint needs to address all three independently, not collapse them into a single "reconciliation gate" because they have different blind spots.

Follow-ups #1, #2, #3 above are not band-aids — they're the structural buildout that closes the 6-anchor pattern. Andrew's "this is crucial to nail down this session" directive captures the urgency: the gap is operationally exploitable (one race condition silently mis-states a chart line by 19%), and the detect-and-prevent layers need to ship together so the production methodology pivot is durably correct, not just live-correct after a manual re-fire.

---

## Appendix — file references

- `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh` — 4-stage chain (WS-C absence)
- `data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py` — out-of-chain Inflection feeder
- `data/mdpf/scripts/gold/mdpf_aggregate_aua.py` — WS-A aggregator (reconciliation block lines 408+)
- `data/mdpf/scripts/backfill/build_legacy_compat_emit.py` — page-driving emit (inherits platinum etf_public_residual)
- `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-05-19.json` — re-fired partition
- `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json` — live legacy file (corrected)
- `memory/feedback_identity1_masks_absolute_value_class.md` — destructive defect-detector class with 5 anchors (this incident = anchor #6 candidate)

**Author commit identity:** `0.4.0_DS_ClientPlatform`
**Brief location:** `docs/briefs/mdpf-cohort-0-5-19-race-and-structural-followups-20260519.md` (uncommitted alongside session logs until next org sweep, consistent with prior briefs)
