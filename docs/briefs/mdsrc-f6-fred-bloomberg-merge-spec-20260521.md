# F6 Spec — FRED-vs-Bloomberg Residue Merge

| Field | Value |
|---|---|
| Task Order | YALP_MDSRC.F6 (dsa-fred-bloomberg-residue-merge-spec) |
| Project | YALP_MDSRC |
| Author | 0.2.0_DS_PortfolioAnalytics~A |
| Date | 2026-05-21 |
| Audience | CTO (v0.4 FRED-architecture section) / COO (RAVC) / the merge-implementation TO |
| Inputs | F1 audit (`mdsrc-fred-macro-sourcing-audit-20260520.md`), F4 build note (`mdsrc-f4-fred-ingestion-build-note-20260520.md`, `f42c2ab1a`) |
| Scope | SPEC ONLY — no production code authored (reference implementation optional, deferred — see §7) |

---

## 1. Problem

The Macroeconomics page reads one artifact — `json/macro/macro_data.json` — produced
today entirely by `yang-generate-macro` from the Bloomberg `data_pkl` (79 indicators,
12 groups). F4 built a FRED pull (`ingest_fred_macro.py`) that emits a **separate**
artifact `json/macro/macro_data_fred.json` (51 FRED indicators) — deliberately separate
to avoid a dual-writer on `macro_data.json`. F6 specs how the FRED artifact and the
Bloomberg residue combine into the one artifact the page consumes, with **exactly one
writer** of `macro_data.json` (Third-Party Data Integration Standard — no dual-writers).

### 1.1 The indicator split

| Set | Count | Source after migration |
|---|---|---|
| FRED-replaceable (F1 DIRECT + TRANSFORM) | 50 | FRED (`macro_data_fred.json`) |
| S&P CoreLogic CS Home Price MoM (F1 Finding F1 — config'd but dropped; F4 restores via FRED) | +1 | FRED |
| **FRED total (F4 artifact)** | **51** | **FRED** |
| F1 FRED-PROXY (DXY, USD/CNH, 3 ICE-BofA credit spreads, TIC flows) | 6 | Bloomberg (residue) |
| F1 non-FRED residue (licensed survey / proprietary — Leading Indicator x8, Investor Sentiment x7, ISM, AAII, Conf Board, NAHB, etc.) | 23 | Bloomberg (residue) |
| **Bloomberg residue** | **29** | **Bloomberg** |

Served page today = 79 (50 FRED-of-79 + 29 residue). Post-merge = **80** — the 79 plus
the restored S&P CoreLogic. (The heatmap renders `groups[].indicators[]` dynamically, so
one extra row is **no frontend change** — see §4.)

### 1.2 The constraint that drives the design — cadence

`yang-generate-macro` runs **weekly** (on `data_pkl` upload). The FRED pull runs
**daily** — daily freshness is the entire point of the FRED migration. Therefore the
component that produces `macro_data.json` **cannot be `yang-generate-macro`**: if it
were, the FRED indicators in the served artifact would only refresh weekly, sitting
6-of-7-days stale. The merge producer must run on the **daily** (FRED) cadence.

---

## 2. PRODUCER (AC1)

### 2.1 Options evaluated

| Option | Producer of `macro_data.json` | Verdict |
|---|---|---|
| (a) `yang-generate-macro` reads `macro_data_fred.json` + residue, writes the merged artifact | `yang-generate-macro` | **Rejected** — `yang-generate-macro` is weekly; FRED data would be 6/7-days stale. Defeats the migration. |
| (b) A new small daily **merge step** reads two intermediates, writes `macro_data.json` | new merge component | **RECOMMENDED** |
| (c) The FRED pull writes the merged artifact directly | `ingest_fred_macro.py` | Rejected — overloads the FRED pull with a second responsibility (pull + merge) and makes the page-critical artifact a side-effect of the FRED Lambda; weaker separation, harder rollback. |

### 2.2 Recommended — Option (b): a dedicated daily merge step

Three components, each with one responsibility, and **`macro_data.json` has exactly
one writer** — the merge step.

```
yang-generate-macro   --(weekly, data_pkl)-->  json/macro/macro_data_bloomberg.json   [all 79 indicators]
ingest_fred_macro.py  --(daily, FRED API)--->  json/macro/macro_data_fred.json        [51 FRED indicators]
                                                        |
merge-macro-data      --(daily)------------->  json/macro/macro_data.json   <-- SOLE WRITER, page consumes this
   reads both intermediates above
```

**Why this avoids a dual-writer:** `macro_data.json` is written only by `merge-macro-data`.
`yang-generate-macro` writes only `macro_data_bloomberg.json`; `ingest_fred_macro.py`
writes only `macro_data_fred.json`. No key has two writers.

**Change to `yang-generate-macro`:** a **one-line** change — its `OUTPUT_KEY`
`json/macro/macro_data.json` becomes `json/macro/macro_data_bloomberg.json`. It keeps
emitting **all 79** indicators (not slimmed): the full Bloomberg set is the rollback
fallback and the parallel-run baseline (§5), and the merge step simply ignores the 50
Bloomberg rows it supersedes. Its legacy `macro/macro_data.json` write and its
CloudFront invalidation move out of `yang-generate-macro` — the merge step owns the
invalidation of the served key now. (Aside: F1 Finding F4 — `yang-generate-macro`'s
existing invalidation path `/api/public/macro/*` is already wrong vs the served
`/api/general/*`; the merge step should invalidate the correct path — see §4.3.)

**The merge step** (`merge-macro-data` — a small Lambda, ~120 lines, no pandas):
- Runs **daily**, after `ingest_fred_macro.py` (Step Functions chain, or an EventBridge
  schedule offset ~15 min after the FRED pull).
- Reads `macro_data_fred.json` and `macro_data_bloomberg.json` from S3.
- Emits the merged `json/macro/macro_data.json` and invalidates its CloudFront path.
- Stateless, deterministic, tiny — trivial to reason about and to roll back.

---

## 3. RECONCILIATION (AC2)

### 3.1 Which source wins, per indicator

- **Boundary encoding — by membership in `macro_data_fred.json`, not a duplicated
  static list.** For each indicator the page needs: if the indicator name is present
  in the FRED artifact, the FRED value wins; otherwise the Bloomberg value is used.
  The FRED artifact IS the source of truth for "which indicators are FRED" — a second
  hand-maintained list would drift. The merge step builds a set of FRED indicator names
  from `macro_data_fred.json` at run time.
- **Both-present:** an indicator in the FRED 51 is also in the Bloomberg 79 (the 50
  overlap). FRED wins for all 50; the Bloomberg copy is ignored. (S&P CoreLogic is in
  FRED only — added to the merged Housing group.)
- **Residue:** the 29 not in the FRED artifact pass through from `macro_data_bloomberg.json`
  byte-for-byte (value, percentile, thresholds — untouched).

### 3.2 Assembly

The merge step walks the 12-group structure and, per indicator, takes the **whole
indicator object** from the winning source (`values`, `thresholds`, `unit`, etc.).
It does NOT recompute percentiles or thresholds — each producer already computed them
over its own full history (`yang-generate-macro` and `ingest_fred_macro.py` use the
identical min-max + `np.percentile` method, F4 verified). Group order and the
`{category, count, indicators[]}` structure follow the Bloomberg artifact's group
order; S&P CoreLogic is appended to the Housing Market group (`count` incremented).

### 3.3 Graceful degradation (a merge-specific rule)

The page must always render. If `macro_data_fred.json` is **missing or stale** (older
than a configurable threshold, e.g. 3 days — FRED is daily, so >3d means the FRED pull
is broken), the merge step **falls back to Bloomberg for every indicator** and logs
loud (`ERROR: FRED artifact stale/missing -- merged artifact is all-Bloomberg`). This
is fail-*safe* for the page (never a blank artifact) while still fail-*loud* for ops.
It is the inverse of `ingest_fred_macro.py`'s contract-drift gate (which fail-*loud*
refuses to write a partial FRED artifact) — correct because the merge step's job is to
always produce a renderable page artifact, degrading source quality rather than
availability.

### 3.4 `data_as_of`

The merged artifact's top-level `data_as_of` = `max(FRED data_as_of, Bloomberg
data_as_of)`. Per-source freshness is already visible: the FRED indicator objects
carry the `fred_series`/`fred_units` provenance fields F4 added; the merge step may
additionally stamp a top-level `sources: {fred: <date>, bloomberg: <date>}` block
(additive, frontend ignores it) so the staleness of either leg is observable.

---

## 4. SHAPE (AC2) — no frontend change

### 4.1 The merged artifact matches `macro_data.json` exactly

`{data_as_of, year, groups: [{category, count, indicators: [{name, bbg_ticker, unit,
values: {Mon: {value, percentile}}, thresholds: {p10..p90}}]}]}` — the shape
`MacroHeatmap.tsx` and `MacroTimeSeriesModal.tsx` consume today (F1/F4 confirmed). The
FRED indicator objects carry two **additive** provenance fields (`fred_series`,
`fred_units`); extra JSON fields are ignored by the frontend — no FE change.

### 4.2 Two shape items to confirm at cutover (not blockers)

- **S&P CoreLogic restoration (80th indicator).** The heatmap renders groups/indicators
  dynamically — one extra Housing row needs no FE change. Its drill-down timeseries is
  a separate artifact (`macro/timeseries/*`) covered by F3/F7, not F6 — until F3/F7
  ships, clicking that row's modal 404s gracefully (handled). Flag, do not block.
- **Fed Balance Sheet unit (F4 Finding F4-3).** Today `macro_data.json` carries Fed
  Balance Sheet as raw `$M` (`6699950`) under unit label `B` — a pre-existing
  `yang-generate-macro` mislabel. The FRED artifact emits the correct `$B` (`6699.9`).
  When the merge swaps in the FRED value, the heatmap cell changes from `6699950` to
  `6699.9`. Confirm `formatValueWithUnit` renders `6699.9` with unit `B` acceptably
  (it should — it is a smaller, correct number). One-line FE check at cutover; not a
  blocker.

### 4.3 CloudFront invalidation

The merge step invalidates the **served** path on each write. Per `comp-routes`
behavior 16 the served path is `/api/general/*` -> S3 `opal-data-portal-v2` — so
invalidate `/api/general/macro/macro_data.json` (and `/json-tiered/macro/macro_data.json`
if that behavior is also live). This corrects F1 Finding F4 in passing — the old
`yang-generate-macro` invalidation targeted the wrong prefix (`/api/public/macro/*`).

---

## 5. CUTOVER (AC3)

A **3-stage** sequence with a parallel-run gate; **no transient dual-writer** at any
point — the write-path switch is atomic.

**Stage 1 — FRED pull live (F5, in flight).** `ingest_fred_macro.py` deployed, writing
`macro_data_fred.json` daily. No page impact (`macro_data.json` still pure-Bloomberg
from `yang-generate-macro`). Already covered by F5.

**Stage 2 — merge step in shadow.** Deploy `merge-macro-data` writing to a **staging
key** `json/macro/macro_data_merged_staging.json`. Its Bloomberg input in this stage is
the **live** `macro_data.json` (still pure-Bloomberg — `yang-generate-macro` unchanged).
`yang-generate-macro` is NOT touched in Stage 2 — it remains the sole writer of
`macro_data.json`. **Parallel-run gate:** for ~1 weekly `yang-generate-macro` cycle,
diff `macro_data_merged_staging.json` vs live `macro_data.json` per indicator:
- the **29 residue** must be byte-identical (they pass through);
- the **51 FRED** show the expected F4 fidelity deltas (45 EXACT / 4 CLOSE / 1
  unit-correction / S&P CoreLogic new) — no unexplained divergence;
- no indicator missing, no group miscount.

**Stage 3 — atomic cutover (one deploy).** In a single deploy / `terraform apply`,
flip three settings together:
1. `yang-generate-macro` `OUTPUT_KEY` -> `json/macro/macro_data_bloomberg.json`;
2. `merge-macro-data` Bloomberg input -> `macro_data_bloomberg.json` (was the live
   `macro_data.json`);
3. `merge-macro-data` `OUTPUT_KEY` -> `json/macro/macro_data.json` (was the staging key).

Before the deploy: `yang-generate-macro` is the sole writer of `macro_data.json`.
After: `merge-macro-data` is the sole writer. Because all three flip in one atomic
deploy, **at no instant do two components write `macro_data.json`** — the dual-writer
window is zero.

**Rollback (single revert).** Revert the Stage-3 deploy: `yang-generate-macro`
`OUTPUT_KEY` returns to `json/macro/macro_data.json` (sole writer again) and
`merge-macro-data` returns to the staging key (or is disabled). One revert, fully
restores the pre-migration state. Because `yang-generate-macro` kept emitting all 79
throughout, the rollback artifact is complete immediately.

**Per-indicator no-regression verification (at Stage 3 + each daily run for the first
week):** assert every one of the 80 expected indicators is present in the merged
artifact; the 29 residue match `macro_data_bloomberg.json` byte-for-byte; the 51 FRED
match `macro_data_fred.json`; all 12 group `count`s equal their `indicators` length.

---

## 6. The non-FRED residue (stays Bloomberg — producer unaffected)

The 29 residue indicators stay sourced from the Bloomberg `data_pkl` via
`yang-generate-macro` (now writing `macro_data_bloomberg.json`). They are, from F1:
the entire **Leading Indicator** group (8 — ISM/S&P PMI, Conf Board LEI, NFIB), the
entire **Investor Sentiment** group (7 — AAII x6, Fed NLP), plus Bloomberg FCI, ADP,
Conf Board Consumer Confidence, NAHB, NAR Pending Home Sales, UMich 5-10yr, Ted Spread,
Bloomberg Agg OAS, and the 6 F1 FRED-PROXY indicators (DXY, USD/CNH, AAA/IG/HY ICE-BofA
spreads, TIC flows) which F4 deliberately left on Bloomberg pending an explicit
proxy-acceptance decision (F1 recommendation 3). `yang-generate-macro`'s logic for
these is **unchanged** — only its output key changes. No residue producer is modified.

---

## 7. Reference implementation — deferred

A reference `merge-macro-data` Lambda is **optional** per the F6 TO and is **not
authored here** — the spec is the deliverable. The merge logic is small and fully
determined by §2-§5 (read two JSON artifacts, set-membership reconciliation, assemble
groups, graceful-degradation guard, write + invalidate). Recommend it be built as a
**follow-on TO**: DS-authored (the merge logic + `ds-commit-gate`), AE-deployed
(`infra/aws/lambda` is AE lane; the deploy mechanism rides the F2 IaC ruling, same as
F5). Estimated ~120 lines, no pandas, 256 MB / 60 s Lambda.

---

## 8. Compiler Tools

| Tool | Command | Result | vs expect |
|------|---------|--------|-----------|
| comp-routes | `comp-routes behaviors` | behavior 16 `/api/general/*` -> S3 `opal-data-portal-v2` (public-data-router + cache-control-injector) | MATCH — anchors the §4.3 invalidation path + the §2 served-key identity |
| comp-pipescript | `comp-pipescript io yang-generate-macro` | "Unknown script" — yang generators are not comp-graph nodes | MISMATCH handled per TO `<if_mismatch>` — source-read fallback (the F1/F4 reads of `yang-generate-macro` + `ingest_fred_macro.py` are the basis) |
| ds-commit-gate | n/a | no reference implementation `.py` authored — §7 defers it | per TO compiler mandate phase 2 = documented-N/A |

---

## 9. Deliverables / RAVC

- This spec — `docs/briefs/mdsrc-f6-fred-bloomberg-merge-spec-20260521.md` (committed,
  push-confirmed on origin/CLOUD).
- Session log with the Compiler Tools section.
- RAVC2 to `2.0.0_SA_COO`, CC `1.0.0_SA_CTO` — feeds the PRD v0.4 FRED-architecture
  section. The merge-implementation follow-on TO (§7) is recommended for COO to issue
  after F5 lands.
