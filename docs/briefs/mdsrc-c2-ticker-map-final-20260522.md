# YALP_MDSRC.C2 WS-1 — Finalized 71-Entity Ticker Map (AC2)

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — C2 WS-1 (0.1.0_DS) |
| Task Order | `YALP_MDSRC.C2` — AC2 deliverable (WS1-DDB-01 ticker map) |
| By | `0.1.0_DS_MarketIntelligence` |
| Date | 2026-05-22 |
| Companion data | `mdsrc-c2-ticker-map-final-20260522.csv` — the 71-row machine-readable map |
| Audience | `2.0.0_SA_COO` (RAVC2 — within the C2 TO) |

---

## 1. Deliverable

The WS1-DDB-01 ticker map — every one of the 71 portal entities (the DynamoDB
daily-price backbone) mapped to its YCharts pull symbol. Built by merging:

- the **dc01d4b8a crosswalk** (`mdsrc-ycharts-ticker-map-20260520.csv`) —
  `portal_name -> bbg_ticker` + the per-entity portal-1Y fidelity columns;
- the **V1B-finalized C2 pull-spec** (`mdsrc-c2-pull-spec-prestage-20260521.csv`)
  — `portal_name -> resolved ycharts_symbol + yc_kind`, keyed on `portal_name`.

Map columns: `entity_type, portal_name, bbg_ticker, ycharts_symbol, yc_kind,
fidelity, portal_1Y_pct, ycharts_1Y_pct, pin_status, note`.

## 2. Result — 71 of 71 PINNED

| pin_status | Count |
|---|---|
| PINNED — `ycharts_symbol` resolved | **71** |
| SEAT-FROZEN — symbol unresolved | 0 |
| NO-PULLSPEC-ROW | 0 |

**The A3 P4 ~10-case symbol-discovery residue is closed.** The C2 TO referenced
"~10 remaining symbol-discovery cases" as a defined C2 sub-task — that residue
was the *pre-V1* state. The V1 76-entity history verification, V1A (the 4
maturity-band bonds), and V1B (the 3-band Bloomberg-proxy resolution) closed
every case. All 71 backbone entities now carry a resolved, V1-verified YCharts
symbol; no symbol discovery remains for the WS-1 backbone.

Notable resolutions carried in: the 4 maturity-band bonds resolved by V1A/V1B —
0-1Yr Treasury -> `^BBUTB13MTR`, 0-5Yr HY -> `^BBUSCOHYTR`, 0-5Yr TIPS ->
`^BBUTISTR`, 20+Yr Treasury -> `^BBUSLGCRTR` (representative Bloomberg indices,
per Andrew's ruling; each labelled `meets-via-representative-Bloomberg-index`).

## 3. Freeze-aware scope — the fidelity column

`ycharts_1Y_pct` is left blank in the map: a live per-symbol 1-year fidelity
check (portal-1Y vs ycharts-1Y) requires a live YCharts pull, which is frozen
until the dedicated seat lands. The map delivers the **symbol identity mapping**
(AC2 — what each portal entity pulls from on YCharts); the per-symbol numeric
fidelity check is a first-live-run verification step, flagged here, not claimed.
`portal_1Y_pct` (the Bloomberg-pkl side) is carried from the dc01d4b8a crosswalk
as the comparison baseline for that future check.

## 4. Acceptance

`AC2 — the 71-entity ticker->YCharts-symbol map (WS1-DDB-01) delivered` — MET.
71/71 entities pinned to a V1-verified YCharts symbol; companion CSV committed.

The map is consumed by `ws1_surface_pull.pull_ddb_backbone` (the WS1-DDB-01
pull) — the `ycharts_symbol` column is the symbol list passed to the pull.
