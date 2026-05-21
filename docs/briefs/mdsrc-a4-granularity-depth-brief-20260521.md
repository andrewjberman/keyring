# BRIEF: YCharts Granularity + Depth — full 76-entity sweep (YALP_MDSRC.A4)

**Date:** 2026-05-21
**Author:** 0.1.0_DS_MarketIntelligence (deliverable lead) — capture side: 0.7.0_AE_CloudOps~A (paired AE)
**TO:** YALP_MDSRC.A4 (issued by 2.0.0_SA_COO, Andrew-direct; paired TO)
**Audience:** 2.0.0_SA_COO (RAVC2) — CC 1.0.0_SA_CTO
**Deliverable matrix:** `docs/briefs/mdsrc-a4-granularity-depth-matrix-20260521.csv` — 76 rows, one per portal-tracked entity.
**Reference:** Phase 0 universe `mdsrc-a4-entity-universe-20260521.csv`; A3 internal-API brief `mdsrc-ycharts-internal-api-20260520.md`.

> **Amendment 2026-05-21 (CTO/COO rulings):** the `general_data.json` 403 that deferred the 36 MSCI + Bloomberg-bond indices is — on the **working theory** (Andrew's read) — **F1 session eviction** (a concurrent login on the shared YCharts seat), not an entitlement gap; the conditional "36 permanently stay Bloomberg-pkl" is **retracted.** Per the CTO precision note, the brief holds the 36 at **working-theory / access-and-depth-unverified** (zero data points captured for any of the 36) — *not* "confirmed resident"; the recapture must verify depth, not just endpoint access. §1, §3.2, §5, §6, §8 reflect this; the 36 carry `verdict = pending-recapture`. Finding 2 (no date-bounded pull) is unaffected.

---

## 1. Summary + verdict

A4 verifies, per portal-tracked entity, the **granularity** and **depth** the YCharts internal API actually delivers — whether a YCharts pull can replace the Bloomberg `data_pkl` feed for that surface. A3 mapped the endpoints; the granularity/depth spot-probe was n=1 (S&P 500). A4 is the full sweep of all **76 entities** (53 INDEX + 11 BOND_INDEX + 7 COMMODITY + 5 ETF).

**Headline:** the sweep splits the universe cleanly.

| Verdict | Count | What it means |
|---|---|---|
| **meets** | 29 | Clean daily series, depth 12.2–96.4 yr — far exceeds the ~6yr daily backbone requirement. YCharts-replaceable. |
| **partial** | 2 | Bitcoin + Ethereum — clean daily, but only 1.8 yr deep (YCharts crypto coverage starts 2024-07). |
| **pending-recapture** | 36 | All 29 MSCI indices + all 7 Bloomberg-bond indices — served by `general_data.json`, not `fund_data.json`. The sweep could not capture them; **F1 session eviction (a concurrent login on the shared seat) is the working theory** (Andrew's read) — so the 36 are *not* a confirmed Bloomberg-pkl gap, but **access and depth remain unverified** (zero data points captured) pending a `general_data.json` recapture (see §6). |
| **blocked-pending-symbol** | 9 | Batch-0 entities with no YCharts symbol resolvable in one attempt — a C2 symbol-discovery task, not a data-availability gap. |

**Net:** for the 31 entities that ARE `fund_data.json` items, YCharts replacement is confirmed sound — 29 meet outright, 2 are shallow-but-daily. The other 36 (all MSCI + all Bloomberg-bond indices) were not captured — the **working theory** (Andrew's read) is F1 session eviction: a concurrent login evicted the capture session mid-sweep. On that theory the 36 are not an entitlement or Bloomberg-pkl gap, and C2 plans for them as in-scope-YCharts — **but it is a theory, not a measurement: zero data points were captured for any of the 36, so their access and depth remain unverified pending a recapture.** A dedicated YCharts seat (being acquired) removes the contention; the recapture then verifies the 36 to the same standard as the 31.

---

## 2. Method

- Phase 0 (DS): enumerated the 76-entity universe, resolved YCharts symbols (67 PROBE-READY, 9 RESOLVE-FIRST), A3/A2 corrections applied.
- Phase 1 (paired AE ~A, live YCharts session): one `fund_data.json` pull per PROBE-READY entity at `maxPoints=100000` (the calibration established this returns the full native daily series — see §4). Consolidated capture: `.runtmp/a4_capture/a4_sweep_capture.json`, keyed by YCharts symbol, each row carrying its exact request URL. Resample-boundary characterization: `a4_boundary.json`.
- Phase 2 (DS): per-entity granularity (median inter-point gap over the recent tail), depth (`last_ts − first_ts`), resample boundary, and the meets/partial/gap verdict against the portal requirement.
- Portal requirement applied: **~6yr of daily data** — the `opal-portal-market-data` DynamoDB backbone that feeds Market Overview, Correlation, and the ticker timeseries.

---

## 3. Results

### 3.1 The 31 captured (`fund_data.json` HTTP 200) — all clean daily

All 31 returned a clean daily/trading-day series (median inter-point gap 1.0 day). Depth, sorted:

- **Deepest:** Dow Jones 96.4yr (from 1930-01-02), S&P 500 76.4yr (1950), Russell 1000/2000 47.4yr (1978), Nasdaq 41.5yr (1984).
- **Mid:** the 10 older S&P 500 sectors 36.7yr (1989-09-11), Real Estate sector 24.6yr (2001 — the sector was carved out later), Russell 1000 Growth/Value 35.4yr (1990).
- **Shallower but still ample:** IVV 26.0yr, AGG 22.7yr, WTI 21.3yr, BIL 19.0yr, ACWI 18.2yr, VGSH 16.5yr, S&P GSCI 15.2yr, the 3 Russell Mid Cap indices 12.7yr, Gold 12.2yr.
- **Shallow — the 2 partials:** Bitcoin 1.8yr (2024-07-31), Ethereum 1.8yr (2024-07-23).

**29 `meets`:** every one is clean daily AND ≥12.2yr deep — comfortably past the ~6yr backbone. No granularity or depth shortfall.

**2 `partial` (BTC/ETH):** daily granularity meets; 1.8yr depth falls short of the ~6yr backbone. This is a YCharts coverage-start limit (its crypto series begin 2024-07), not a granularity defect. Whether it is a true gap depends on the portal's own crypto history depth — if the portal added crypto recently it may not predate 2024-07 materially either, making `partial` acceptable. **Flagged for the C2 / portal owner to confirm.**

### 3.2 The 36 not captured — all 29 MSCI + all 7 Bloomberg-bond indices

Every MSCI index and every Bloomberg-bond index returned `fund_data.json` HTTP 400 *"There are no valid items on this chart"* — on every calc tried (level/price/total_return/none). They are simply **not `fund_data.json` items**; their real time-series endpoint is `general_data.json` (the `/indices/^MSEM` detail page's own chart calls it). `general_data.json` returned **HTTP 403 "You are signed out"** during the sweep — the partial-failure signature of a disturbed YCharts session (the known F1 mode: some endpoints 403 while others still 200). **Working theory (Andrew's read, 2026-05-21): this 403 was F1 session eviction** — a concurrent human login on the shared YCharts account killed the capture session mid-sweep — **operational contention, not an entitlement gate.** On that theory the 36 are not a Bloomberg-pkl gap — but it is unverified: zero data points were captured for any of the 36, so neither their access nor their depth is established. They need a recapture on a non-contended session (see §6).

### 3.3 The 9 blocked-pending-symbol (Batch 0)

5 securities-search entities (MSCI USA Size, Silver, Crude Oil Brent, Natural Gas, Copper) + 4 Bloomberg maturity-band bonds (0-1 Yr Treasury, 0-5 Yr High Yield, 0-5 Yr TIPS, 20+ Yr Treasury). One thorough resolution attempt each (per the TO's one-attempt directive): the 5 need a browser-in-loop live securities-search (YCharts `/search/` is a client-rendered SPA shell with no locatable JSON XHR); the 4 maturity-band bonds are absent from YCharts' Bloomberg index set entirely — YCharts carries **ICE-vendor** maturity-band alternatives (`^ICEUT2YTR`, `^ICEUST13YT`, etc.), so a Bloomberg→ICE cross-vendor substitution is a C2 fidelity decision. Both are C2 symbol-discovery tasks, not A4 data-availability gaps.

---

## 4. AC5 — the canonical C2 time-series endpoint (resolved)

The ~A calibration on `^SPX` answered AC5 and corrected the A4 scoping assumptions:

- **`fund_data.json` is the canonical C2 time-series endpoint for the 31 entities it carries.** The 36 MSCI/Bloomberg-bond indices are not `fund_data.json` items — their endpoint is `general_data.json`, which 403'd during the sweep (§6 — working theory: F1 session eviction; its usability for C2 is pending the recapture, not assumed).
- **The calc parameter is entity-class-specific:** `calcs=id:level` for standard indices (`^SPX`, sectors, Russell, GSCI); `calcs=id:price` for securities/ETFs/crypto/commodity-securities (IVV, BTC, ETH, GOLD, WTI, the 5 ETFs). Using the wrong calc 400s.
- **`fund_data.json` ignores `startDate`/`endDate`** — date params are silently dropped. Granularity is controlled solely by `maxPoints` vs the entity's available daily-point count: `maxPoints ≥ daily-count` → full native daily; below it → auto-resampled (weekly/biweekly/monthly). Boundary samples confirm uniform behavior (`^SPX`: monthly at maxPoints=500, biweekly at 2000, daily at ≥20000 / 19,225 daily pts). `maxPoints=100000` is safely above every entity's daily count.

---

## 5. C2 implications

1. **C2 pulls full native history via `fund_data.json` + `maxPoints=100000` and bounds client-side.** There is no working date-bounded YCharts path on this account — design C2 accordingly.
2. **C2 must select the calc by entity-class** — `id:level` for `^`-prefixed indices, `id:price` for securities/ETFs/crypto. A per-entity `yc_kind` flag (already in the A4 universe CSV) drives this.
3. **The 36 MSCI + Bloomberg-bond indices are unverified pending recapture** (§6) — the working theory is F1 session contention, not a data gap, so C2 plans for them as in-scope-YCharts. But zero data points were captured: the recapture must verify access AND depth (a real `general_data.json` series, ACs mirroring AC2/AC3) before C2 relies on them. They are ~half the index universe and a large share of the DynamoDB backbone — this is C2 pre-build work, not a closed result.
4. **9 blocked-pending-symbol** — C2 closes these with a browser-in-loop securities-search (5) and a Bloomberg→ICE cross-vendor decision (4).
5. **BTC/ETH** — YCharts daily but only 1.8yr; if the portal needs a deeper crypto backbone it stays partly Bloomberg-pkl for the pre-2024 tail. C2 / portal-owner confirm.

---

## 6. The 36 MSCI + Bloomberg-bond indices — unverified; working theory = session contention (AC4)

During the sweep `general_data.json` 403'd while `fund_data.json`/`table_data` 200'd on the same run. A4 originally flagged this as a fork (degraded-session vs entitlement-gap). **The working theory (Andrew's read, 2026-05-21, plausible):** the 403 was **F1 session eviction** — a concurrent human login on the shared YCharts account, and YCharts' single-concurrent-session constraint (F1) killed the capture session mid-sweep. Andrew's directive: *"should not take these 403s as blocks, it's an operational issue not a permissions issue"* — and he is acquiring a **dedicated YCharts seat**.

**What this does and does not establish.** It retracts the "36 entities permanently stay on the manual Bloomberg feed" conditional — on the session-eviction theory the 36 are *not* an entitlement gap, so C2 plans for them as in-scope-YCharts (no Bloomberg-pkl carve-out to design around). But it is a **theory, not a measurement: zero data points have been captured for any of the 36.** Neither their access (does `general_data.json` open for them on a clean session) nor their depth/granularity is verified. This brief does **not** assert the 36 as "YCharts-resident / confirmed" — only as unverified-pending-recapture.

**The recapture verifies access AND depth.** A `general_data.json` 200-vs-403 check alone only proves the endpoint opens; it does not establish that the 36 carry a usable multi-year daily series. The recapture must pull each of the 36 via `general_data.json` at `maxPoints=100000` and record a real series — the same integrity check the 31 passed — with ACs mirroring A4 AC2/AC3 (finest granularity, depth, resample boundary, meets/partial/gap verdict). Their A4 matrix rows carry `verdict = pending-recapture` until then. This recapture folds into C2 pre-build (per COO) — confirmation work, not a blocker.

---

## 7. Compiler self-checks (TO `compiler_tools_mandate`)

A4 is a YCharts-internal-API investigation — no comp-* graph tool covers the YCharts backend.

- **Phase-0 step 1 (universe count):** observed 76 (53+11+7+5); ETF set concrete = 5. PASS.
- **Phase-0 step 2 (crosswalk corrections):** MSCI-country LOC variants + bond plain-USD symbols applied. PASS. (Moot for the 36 in the event — they 400 on `fund_data.json` regardless of variant; the variant question moves to C2 with the `general_data.json` path.)
- **Phase-2 step (matrix row-count):** matrix = 76 rows, one per Phase-0 entity; all 10 columns populated; the 9 blocked + 36 pending present as explicit rows (verdict = blocked / pending), none absent. PASS — `meets 29 + partial 2 + pending 36 + blocked 9 = 76`.

---

## 8. Acceptance criteria

- **AC1** — all 76 entities (INDEX/BOND_INDEX/COMMODITY/ETF) enumerated + probed; none skipped; 9 unresolved entities present as explicit blocked rows. **MET.**
- **AC2** — per captured entity: finest granularity, depth (earliest date + span), resample boundary recorded from the live pull. **MET** for the 31; the 36 unverified pending the §6 recapture (zero data points captured).
- **AC3** — per-entity meets/partial/gap verdict. **MET** — 29 meets, 2 partial, 36 `pending-recapture` (unverified, §6), 9 blocked.
- **AC4** — entities YCharts cannot serve at the required granularity/depth explicitly flagged stays-Bloomberg-pkl. **MET** — per the §6 ruling, no entity is a confirmed permanent stays-Bloomberg-pkl: the 36 are unverified-pending-recapture (working theory = session contention, not an entitlement gap), and the 9 blocked are symbol-discovery not data-availability. The only *measured* granularity/depth shortfall is BTC/ETH (daily but 1.8yr — a portal-owner call on whether YCharts' crypto depth suffices or the pre-2024 tail stays Bloomberg-pkl).
- **AC5** — canonical C2 time-series endpoint resolved. **MET** — §4: `fund_data.json` canonical for the 31 (entity-class calc, maxPoints-driven granularity, date params ignored); `general_data.json` is the 36's endpoint, 403'd in-sweep (§6, working theory: session eviction — recapture pending).
- **AC6** — committed machine-readable matrix + brief; compiler self-checks reproduced. **MET** (§7, this commit).
- **AC7** — RAVC2 to COO + CC CTO; C2 implications stated. **MET** (§5, this RAVC2).

**Follow-on (defined):** re-capture the 36 `pending-recapture` entities via `general_data.json` on a non-contended / the dedicated YCharts seat, and finalize their matrix rows (expected meets/partial). Per COO 2026-05-21 this folds into C2's pre-build step — no separate A4.1.
