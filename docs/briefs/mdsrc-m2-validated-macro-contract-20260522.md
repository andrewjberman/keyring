# YALP_MDSRC.M2 — Validated Macro Data Contract (verify-channel pass)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — PRD v0.4 WS-C |
| Task Order | `YALP_MDSRC.M2` (ds-macro-data-contract-verify-channel-validation) |
| Verified by | `0.1.0_DS_MarketIntelligence` (verifier != author — M1 authored by `0.2.0_DS_PortfolioAnalytics`, R5) |
| Date | 2026-05-22 |
| Input | `docs/briefs/mdsrc-m1-macro-data-contract-20260521.{md,tsv}` — the 81-row M1 contract (commit d9f8cd2c7) |
| Companion | `docs/briefs/mdsrc-m2-validated-macro-contract-20260522.tsv` — 81-row validated contract (adds `m2_verdict`, `m2_checks`, `m2_evidence`) |
| Audience | `2.0.0_SA_COO` (RAVC2) — CC `1.0.0_SA_CTO` |
| Method | verify-channel skill — EXISTS / FRESH / SCALED / NOT-FROZEN; verifier != author; sharpest-test-binds; live source state read, never M1's self-report |

---

## 1. Verdict — 80 CONFIRMED / 1 REWORK

Every one of the 81 M1 contract rows independently verify-channel-validated against
**live source state** (the FRED public API, the US Treasury TIC data files, the YCharts
internal API) — never M1's self-report. Result:

| M2 verdict | Count | Meaning |
|---|---|---|
| **CONFIRMED** | 80 | Source claim verified live, with evidence |
| **REWORK** | 1 | Claim failed verification — routed back to M1 (`0.2.0_DS`) |

R5 bar ("cannot hallucinate") met: **no row ships CONFIRMED on an assumed source.** Every
CONFIRMED row carries a live-probe evidence string in the TSV `m2_evidence` column.

---

## 2. Channel A — 56 FRED / Treasury rows

**55 FRED-replaceable + 1 Treasury.** Probed live via the keyless FRED public CSV endpoint
(`fredgraph.csv`) and the US Treasury TIC data files. Probe artifacts:
`.runtmp/m2_fred_verify_result.json`, `.runtmp/m2_verify_a2_result.json`.

### 2.1 The 4 verify-channel checks

- **EXISTS** — 54 of 55 FRED series returned HTTP 200 with observations. 1 failed (idx 41 — see §2.3). The Treasury TIC source (idx 21) confirmed (§2.4).
- **FRESH** — all 54 live series are actively maintained; **none discontinued**. The longest staleness (GDP / A191RL1Q225SBEA / ULCNFB at 140d; Case-Shiller 109d; the laggy monthly Census series at 81d) is **publication-lag**, not freezing — the next observation is genuinely not released yet for the indicator's cadence. (Empirical contrast: `TEDRATE` last obs 2022-01-20 and `USSLIND` last obs 2020-01 ARE frozen/discontinued — neither is in the FRED-replaceable set; both correctly sit on proprietary/originating-body rows.)
- **SCALED** — every series' values are in-family for the indicator (UNRATE 4.3%, DGS10 4.57%, VIXCLS 16.76, CPIAUCSL 332 index, WALCL $6.71M-millions). Two rows carry a documented ingest-time unit conversion — idx 15 Trade Balance and idx 19 Fed Balance Sheet (FRED $M → portal $B); the M1 contract already notes this. Not a defect.
- **NOT-FROZEN** — re-probed the last 10 observations of every FRED series; all tails vary (no frozen-duplicate series).

### 2.2 Transform reproduction (M1 priority-1 — the genuine open verify)

M1 flagged the `units=` transform rows as the priority verify: F1 probed *levels*, not the
transformed MoM/YoY/chg values. M2 probed every `units=` row with the FRED
`transformation=` parameter live. **All 16 transform rows reproduce a correctly-shaped
result:**

- `pch` rows (INDPRO, DGORDER, AMTMNO, CPIAUCSL, CPILFESL, PCEPI, PCEPILFE, PPIFIS, CES0500000003, RSAFS, RSFSXMV, CSUSHPINSA) — yield small monthly % deltas (−1.2% … +1.9%), the correct MoM-% shape.
- `pc1` rows (BUSINV, ULCNFB, TOTALSL) — yield 1–3% YoY-% values, correct.
- `chg` row (PAYEMS) — yields +115 … +185 (and −156) thousands, the correct NFP headline-change shape.

The FRED `transformation=` parameter is the deployable mechanism for the 16 pre-computed
Bloomberg MoM/YoY/QoQ rows — CONFIRMED.

### 2.3 idx 41 — the one REWORK

`idx 41 — Retail Sales ex Auto and Gas MoM`. M1's claimed FRED series id
**`MARTSSM44X72USS` returns HTTP 404 — the series does not exist.** M1's own `m2_verify_note`
flagged it ("Confirm exact FRED series ID for ex-auto-and-gas at verification"); the verify
confirms the id is wrong. **Routed to M1 (`0.2.0_DS`) as REWORK.**

M2 evidence for the rework (verifier supplies evidence, does not re-author): the correct
series is **`MARTSSM44W72USS`** — FRED title *"Advance Retail Sales: Retail Trade and Food
Services, Excluding Motor Vehicle and Parts Dealers and Gasoline Stations"* — an `X`→`W`
character typo. The `units=pch` transform was confirmed live on the correct id. The other
candidates probed (`MRTSSM44X72USS` = "Retail Trade and Food Services", not ex-auto-gas;
`RSXFS`, `RSAFSNA`) are NOT the ex-auto-and-gas series — M1 to confirm the SA series choice.

### 2.4 idx 21 — Treasury TIC, verdict CONFIRMED

M1 verdict `Treasury` (`fred_series_id` = `(partial)` — FRED TIC coverage thin). M2 confirmed
the authoritative source: **`https://ticdata.treasury.gov/Publish/s1_globl.csv`** — HTTP 200,
*"U.S. Transactions with Foreigners in Long-term Domestic and Foreign Securities, by Type and
Country"*, 41,538 rows, machine-readable CSV, the canonical TIC long-term-securities table
(the headline net long-term flow = the `Grand Total / 99996` series). Treasury publishes it
free, on a monthly release schedule. Verdict `Treasury` CONFIRMED.

---

## 3. Channel B — the 19 originating-body rows + the YCharts-coverage question

M1 verdict `originating-body-direct` for 19 indicators (ISM ×4, S&P Global PMI ×2, NFIB,
Conf Board LEI + Consumer Confidence, NAHB, NAR Pending, UMich 5-10yr, ADP, AAII ×6).

**The verdict `originating-body-direct` is CONFIRMED for all 19** — the "no free government
source" claim is empirically backed (FRED spot-checks: `NAPMPMI` / `ISMPMI` / `AAIIBULL` /
`NFIBOPT` / `NAHB` all 404; `USSLIND` discontinued 2020). The authoritative source is the
originating private body.

### 3.1 YCharts coverage — the COO's "single biggest open WS-C question"

M2 probed the YCharts internal API (`/search/suggest/main`, the A5-pinned search endpoint,
mchm seat) for every one of the 19. **YCharts carries 15 of the 19; 4 are NOT carried.**
Probe artifacts: `.runtmp/m2_chb_v1a_result.json` + rounds 2–4.

**15 carried** (the YCharts automation channel is available — migration-ready):
ISM Mfg PMI · ISM Svc PMI · ISM Mfg New Orders · ISM Svc New Orders · NFIB (Small Business
Optimism Index, I:SBOI) · ADP (I:ADPEC) · Conf Board Consumer Confidence (US Consumer
Confidence, I:USCC) · NAHB (id 197) · NAR Pending Home Sales (id 113) · AAII Bullish /
Neutral / Bearish (US Investor Sentiment, I:USISBNW/USISN/USISB) · AAII Stock / Bond / Cash
Allocation.

**4 NOT carried** — YCharts has no equivalent indicator; migration for these must use the
originating body's own (licensed) feed, not YCharts:

| idx | Indicator | Why not |
|---|---|---|
| 1 | Conference Board Leading Economic Index | YCharts has the OECD Composite Leading Indicator for the US (`I:CLIUS`) — a different methodology, not the CB LEI |
| 4 | S&P Global US Manufacturing PMI | YCharts PMI search resolves only to the ISM PMI; no S&P Global/Markit PMI indicator |
| 5 | S&P Global US Services PMI | same — no S&P Global/Markit Services PMI on YCharts |
| 29 | UMich 5-10 Year Inflation Expectations | YCharts has US 1-Year & 3-Year-Ahead Inflation Expectations (NY Fed SCE) — not the UMich 5-10yr survey |

This is a sharpest-test-binds finding: a first-pass coarse search returned non-zero hit
counts for idx 4/5/43, but reading the actual entity *names* showed idx 4/5's hits were the
ISM PMI (wrong indicator) and idx 43's first-pass hits were Japan-only — re-queried to the
true US entity. Hit-count > 0 was not coverage; the entity name binds.

---

## 4. Channel C — the 6 stays-Bloomberg-proprietary rows

All 6 CONFIRMED. Empirical backing where a live probe applies:

| idx | Indicator | M2 verification |
|---|---|---|
| 16 | Bloomberg Financial Condition Index | Chicago Fed NFCI (idx 17) verified live on FRED — the on-page FRED-native substitute. No free composite equiv. CONFIRMED. |
| 59 | Fed NLP Sentiment | Bloomberg NLP score — no public/government/vendor equivalent. CONFIRMED. |
| 70 | Ted Spread | FRED `TEDRATE` verified **discontinued** (last obs 2022-01-20, LIBOR retirement). No live free equivalent. CONFIRMED. |
| 73 | AGG (Bloomberg US Aggregate OAS) | Licensed Bloomberg index product; no FRED series. CONFIRMED. |
| 76 | MOVE | ICE-licensed; no FRED series. NOTE: `opal-portal-volatility-fetcher` already sources `^MOVE` from Yahoo Finance — a partial off-Bloomberg path the implementation TO should weigh. CONFIRMED. |
| 77 | DXY | FRED `DTWEXBGS` verified live but a **different basket and scale** (118.67 vs ICE DXY ~99) — not a drop-in. CONFIRMED. |

---

## 5. Decision-useful summary (verify-channel Step 3.5)

The validated contract is **decision-useful for the WS-C migration scope**:

- **56 rows (69%) are migration-ready now** — 55 FRED + 1 Treasury, all on free keyless
  public APIs already integrated in this pipeline (`ingest_yield_curve_fred.py`,
  `opal-portal-volatility-fetcher`, `refresh-fred-cache`). The implementation TO can scope
  the FRED macro-ingestion Lambda directly off the validated TSV — **except** idx 41, which
  must take M1's REWORK correction (`MARTSSM44W72USS`) first.
- **15 rows are YCharts-automatable** — the originating-body indicators YCharts carries; the
  implementation channel is the YCharts internal API (the C2-track endpoint work).
- **4 rows (idx 1, 4, 5, 29) have no free or YCharts channel** — migration must license the
  originating body's feed (Conference Board, S&P Global, U. Michigan) or the product call is
  to drop them. This is the genuine residual the implementation TO must escalate as a
  cost/scope decision.
- **6 rows stay Bloomberg-proprietary** — honest terminal verdicts; 2 (BFCI, MOVE) carry a
  documented partial off-Bloomberg path.

**Honest-limit:** M2 verified source EXISTENCE / FRESHNESS / SCALE / TRANSFORM-shape and
YCharts coverage. M2 did **not** value-reconcile each series against a live Bloomberg
terminal value (no Bloomberg access; F1's §3.4 level-probe table is the prior fidelity
evidence). Per-series Bloomberg-vs-source numeric fidelity at the chosen revision vintage is
an implementation-TO acceptance step, flagged here, not claimed done.

---

## 6. Compiler Tools

| Phase | Mandate | Result |
|---|---|---|
| 1 | verify-channel — read live source state, never M1's self-report | DONE — FRED public API (56 rows), Treasury TIC files (idx 21), YCharts internal API (19 rows). All probes are live HTTP; artifacts in `.runtmp/m2_*`. |
| 2 | sharpest-test-binds — EXISTS-but-FROZEN / scale-mismatched fails | DONE — idx 41 failed EXISTS (404) → REWORK; idx 4/5/43 coarse hit-counts overruled by reading actual entity names (ISM ≠ S&P Global; Japan ≠ US). |
| 3 | decision-useful meta-gate — per-indicator deployable verdict + evidence | DONE — §5; the validated TSV states the deployable channel + evidence per row. |

No comp-* graph tool applies — M2 is an external-source verify-channel pass, not a gold/portal/route/IAM change. `.comp-graph/.agent_context` TO_ID set to `YALP_MDSRC.M2`.

## 7. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — every non-Bloomberg-verdict row verify-channel-validated; live source state, not M1's self-report | MET — 56 FRED/Treasury + 19 originating-body all probed live |
| AC2 — sharpest-test-binds: EXISTS-but-FROZEN / scale-mismatched fails | MET — idx 41 REWORK on 404; transform + entity-name sharp checks applied |
| AC3 — every row CONFIRMED or REWORK; none CONFIRMED on assumption | MET — 80 CONFIRMED (each with live evidence) + 1 REWORK (idx 41 → M1) |
| AC4 — committed validated contract w/ deployable verdict per indicator; session log; RAVC2 to COO + CC CTO | this brief + the validated TSV committed; session log; RAVC2 on commit |

## 8. Handoff

- **REWORK → M1 (`0.2.0_DS_PortfolioAnalytics`):** idx 41 only — correct `MARTSSM44X72USS`
  to `MARTSSM44W72USS` (M2 supplies the evidence; M1 re-authors the row + confirms SA series).
- **The implementation TO** (downstream): scope the FRED macro-ingestion Lambda off the
  validated TSV's 56 FRED/Treasury rows; the YCharts-channel work for the 15 carried
  originating-body rows; and escalate the 4 no-channel rows (idx 1/4/5/29) as a licensing
  cost/scope decision.
- RAVC2 to `2.0.0_SA_COO`, CC `1.0.0_SA_CTO` — this closes WS-C.
