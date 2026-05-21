# YALP_MDSRC — Master Index (start here)

**Project:** YALP_MDSRC — Portal Market-Data Sourcing Strategy (YCharts vs Bloomberg-PKL vs SmartX)
**Index author:** 0.1.0_DS_MarketIntelligence · **Index date:** 2026-05-20
**Canonical PRD:** `docs/architecture/YALP_MDSRC.md` (v0.3.1 — implementation charter)

This is the definitive "start here" for YALP_MDSRC — every committed artifact, the consolidated current findings, and what is still open. All artifacts are committed on `origin/CLOUD`. This index is navigational; where it summarizes a brief, that brief is the authority.

---

## 1. What the project is

Andrew directive (2026-05-20): determine, surface by surface, which portal market-data surfaces — today fed by the manual Bloomberg `.pkl` yang-pipeline — can move to a daily automated YCharts pull, and which must stay manual. End state is an explicit hybrid. Also: where is model-portfolio performance best sourced (YCharts / yang `model.pkl` / SmartX).

**Status:** Phase-0 audit COMPLETE; PRD v0.3.1 is the implementation charter; Phase-2 implementation decomposed into 5 TOs (§4), gated on Andrew's Q1 call.

---

## 2. Consolidated headline findings

1. **YCharts touches 17 of 32 portal surfaces** — 7 fully YCharts-replaceable + 10 hybrid (data inputs migrate, Opal computation stays). The Bloomberg `data_pkl` dependency can be retired for all 17; the manual pkl shrinks to `model_pkl` + the Excel workbooks. 6 surfaces → SmartX, 7 proprietary, 2 already on FRED.
2. **YCharts data is high-fidelity vs the portal's Bloomberg-pkl values** — 44 of 53 mapped tickers match within ~1-3 pt. A source-swap is data-equivalent.
3. **The variant-mapping unlock** — the portal→YCharts ticker map was the #1 risk; the authority was found in S3: Yang's `data_pkl` carries a `bbg_ticker` column giving the exact Bloomberg ticker for all 71 entities. The map is now a deterministic crosswalk, no Yang consult needed.
4. **MSCI country indices are local-currency** — the systematic root cause of the wide-variance residue: the portal's MSCI `MX**` country indices are local-currency; mapping to YCharts `^MS**L` (LOC) variants collapses 6 of 7 wide cases to under 2 pt.
5. **The official YCharts API has no index client** — the `pycharts` SDK exposes Company / MutualFund / Indicator clients only. Indices are the core of the YCharts-replaceable set, so the official-API-as-primary recommendation is contingent on confirmed index coverage (Q1 sub-question).
6. **Session-scrape works but is fragile** — single-concurrent-session (F1: a human login evicts the integration), and can fail *partially* (some endpoints 403 while others 200). Officially-API path eliminates all of it. CTO recommendation: pursue the official API as primary, scrape as fallback.
7. **Open flag — Communication Services** — portal `S5COMM` 1Y +68.6% matches no YCharts S&P Communication-Services index (all ~43-44%); a possible portal-side data-integrity issue, independent of the migration.

---

## 3. Artifact index (all committed on origin/CLOUD)

### Reconnaissance + scoping
| Artifact | Commit | What it is |
|---|---|---|
| `ycharts-bloomberg-portal-data-sourcing-audit-20260520.md` | `3987616d8` | Phase-0 scoping brief — HAR recon; the project's founding doc |
| `mdsrc-ycharts-master-reconnaissance-20260520.md` | `1fd7650f4` | 26-endpoint YCharts capability catalog + coverage map + fidelity + official-API research |

### Phase-0 domain audits (the four work-streams)
| Artifact | Commit | Work-stream / owner |
|---|---|---|
| `mdsrc-ws1-external-market-data-audit-20260520.md` + `mdsrc-ws1-matrix-slice-20260520.tsv` | `1baf13dfa` | WS-1 External Market Data — 0.1.0_DS |
| `mdsrc-ws2-portfolio-analytics-audit-20260520.md` + `mdsrc-ws2-matrix-slice-20260520.tsv` | `7de5d3b69` / `368510231` | WS-2 Portfolio Analytics — 0.2.0_DS |
| `mdsrc-ws3-client-facing-data-audit-20260520.md` + `mdsrc-ws3-matrix-slice-20260520.tsv` | `b7153c70c` / `678f02649` / `f963b8727` | WS-3 Client-Facing Data — 0.4.0_DS_ClientPlatform |
| `mdsrc-ws4-ycharts-operational-pattern-20260520.md` | `b88787708` / `5f7a3ae1e` | WS-4 Operational Pattern — 0.7.0_AE_CloudOps |

### Live test, ticker map, endpoint spec
| Artifact | Commit | What it is |
|---|---|---|
| `mdsrc-ycharts-live-session-test-20260520.md` | `391f1321f` | YALP_MDSRC.007 — live-session capability test (PASS 4/4, corrected) |
| `mdsrc-ycharts-ticker-map-and-fidelity-20260520.md` + `mdsrc-ycharts-ticker-map-20260520.csv` | `dc01d4b8a` (+`b0ab3557c`) | 71-row portal→YCharts crosswalk w/ `bbg_ticker` + universe-wide fidelity |
| `mdsrc-ycharts-endpoint-spec-20260520.md` | `cbd6f4ab8` | YALP_MDSRC.A2 — per-requirement endpoint spec (32 surfaces) + the 27-case alternatives hunt; the TO-C2 build spec |

### Synthesis + charter
| Artifact | Commit | What it is |
|---|---|---|
| `docs/architecture/YALP_MDSRC.md` (PRD v0.3.1) | `de7facf93` → `554992f2d` | WS-5 synthesis: 32-surface migration decision matrix + integration architecture + 4-phase implementation plan |

Session logs: `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-20/` (5 — scoping, WS-1, .007, master-recon, A2).

---

## 4. Phase-2 implementation (PRD §7) — 5 TOs

| TO | Scope | Owner | Gate |
|---|---|---|---|
| A1 | YCharts capture probe (WAF-clears-headless?) | 0.7.0_AE_CloudOps | Q1-independent — dispatched |
| B1 | Model-portfolio performance pull from SmartX REST | 0.4.0_DS lane | Q1-independent — dispatched |
| C1 | YCharts credential pipeline | 0.7.0_AE_CloudOps | Q1-gated |
| C2 | YCharts market-data pull (builds against the A2 endpoint spec) | 0.1.0_DS + 0.2.0_DS | Q1-gated |
| D1 | Per-surface yang-pipeline cutover + parallel-run diff gate | 0.5.0_AE_OpalETL + DS | Phase-2C-gated |

---

## 5. Open items / decisions pending

| # | Item | Owner |
|---|---|---|
| Q1 | Official YCharts API vs. session-scrape — incl. the sharpened sub-question: does the official API cover the index families? | Andrew + CTO |
| Q7 | ToS — is programmatic extraction from a YCharts seat contractually permitted? | Andrew |
| — | YCharts API quote + index-coverage confirmation (a vendor conversation) | Andrew |
| — | Communication Services `S5COMM` +68.6% anomaly — portal-side data check | CTO (tracked) |
| C2 | Pin the 5 still-unmapped tickers (Silver/Brent/NatGas/Copper/MSCI-USA-Size) via the YCharts securities-search; confirm the GSCI return-basis variant | TO-C2 |

---

## 6. Note on raw evidence

The committed briefs + the ticker-map CSV are the durable record and faithfully summarize the recon. The **raw probe artifacts** — the 26 endpoint captures, the 3 MB `all_calc_menu` catalog extract, the downloaded `data_pkl` — were transient (gitignored `.runtmp/`, throwaway per the TOs). The `bbg_ticker` crosswalk (the most reproduction-critical extract) IS persisted in the committed CSV. Re-deriving the rest would require re-probing the live YCharts seat.
