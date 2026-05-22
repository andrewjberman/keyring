# YALP_MDSRC.V1B — 3-Band Bloomberg-Proxy YCharts Catalog Scan

| Field | Value |
|---|---|
| Project | `YALP_MDSRC` — V1A follow-on |
| Task Order | `YALP_MDSRC.V1B` (ds-3-band-bbg-proxy-ycharts-catalog-scan) |
| By | `0.1.0_DS_MarketIntelligence` |
| Date | 2026-05-22 |
| Ruling | Andrew 2026-05-22, verbatim: *"scan the available bloomberg indexes that are available on YCharts and find a BBG proxy on the same platform. It is not essential that we have the exact same index, as long as its representative of that duration concept and is BBG in origin."* ICE cross-vendor OUT; pkl OUT; ETF-proxy OUT. |
| Corrects | `docs/briefs/mdsrc-c2-pull-spec-prestage-20260521.csv` — the final 3 open bond rows (the V1A-escalated bands) |
| Audience | `2.0.0_SA_COO` (RAVC2) — CC `1.0.0_SA_CTO` |

---

## 1. Outcome — all 3 bands resolved to a Bloomberg-origin YCharts index

V1A escalated 3 bands because YCharts carries no Bloomberg maturity-*band* index for
them. V1B widened the scan to the **full** Bloomberg fixed-income catalog on YCharts and,
per Andrew's ruling, picked the most representative Bloomberg-origin index per band
(exact maturity band not required — representative of the duration/segment concept).

| Band | V1B resolution | Symbol |
|---|---|---|
| Bloomberg 0-5 Year High Yield | Bloomberg US Corporate High Yield | `^BBUSCOHYTR` |
| Bloomberg 0-5 Year TIPS | Bloomberg US TIPS (Series-L) | `^BBUTISTR` |
| Bloomberg 20+ Year Treasury | Bloomberg US Long Government/Credit | `^BBUSLGCRTR` |

All 3 are Bloomberg-origin, YCharts-carried, and depth-confirmed live. No band escalated.

## 2. The catalog scan

Scanned the YCharts Bloomberg fixed-income index catalog via `/search/suggest/main`
(13 family queries — High Yield, Corporate, TIPS, Inflation, Treasury, Long, Government,
Aggregate, Intermediate, Government/Credit). **75 Bloomberg index entities returned; 19
distinct base indices** after collapsing currency/hedged variants. The complete
Bloomberg fixed-income base catalog on YCharts:

- **High Yield:** Bloomberg US Corporate High Yield (`^BBUSCOHYTR`), Bloomberg Global High
  Yield (`^BGHYTR`), Bloomberg Municipal Bond High Yield (`^BMBHYTR`).
- **TIPS / inflation-linked:** Bloomberg US TIPS (Series-L) (`^BBUTISTR`) — the only one.
- **Treasury:** Bloomberg US Treasury (`^BBUSTTR`), Bloomberg US Treasury Bills 1-3 Month
  (`^BBUTB13MTR`).
- **Government/Credit:** 1-3 Year (`^BBUGCR13YT`), 1-5 Year (`^BBUGCR15YT`), Intermediate
  (`^BIUSGCRTR`), Intermediate A+ (`^BIAUSGCRTR`), Long (`^BBUSLGCRTR`).
- **Corporate:** Bloomberg US Corporate (`^BBUSCOTR`), Bloomberg Long US Corporate
  (`^BLUSCOTR`).
- **Aggregate:** Bloomberg US Aggregate (`^BBUSATR`). **Municipal:** Managed Money
  Intermediate / Short-Intermediate, Municipal Bond maturity bands.

This confirms the V1A finding structurally: YCharts carries **no** Bloomberg HY maturity
band, **no** Bloomberg TIPS maturity band, and **no** pure-Treasury intermediate/long
maturity band. The picks below are therefore the closest representative-of-concept
Bloomberg-origin indices the catalog offers — which is exactly what Andrew's ruling asked
for. Scan artifact: `.runtmp/v1b_catalog_result.json`.

## 3. Band-by-band

### 3.1 Bloomberg 0-5 Year High Yield → `Bloomberg US Corporate High Yield` (^BBUSCOHYTR)

- **Duration-concept mapping** — the target is short-dated US high yield. The broad
  Bloomberg US Corporate High Yield index is the canonical US-HY benchmark. HY as an
  asset class is structurally short-clustered (issuers favour shorter, callable paper),
  so the broad index's effective duration already sits in the low-single-digit-years
  range — materially closer to a 0-5yr concept than a broad IG or Treasury index would be.
- **Credit-quality match** — exact: US corporate high yield, same credit segment.
- **Residual** — full-maturity (not 0-5yr-banded); a 0-5yr cut would trim the longer HY
  tail. The duration gap is modest given HY's short clustering.
- **Depth-confirmed live:** HTTP 200, 6,973 daily points, 1998-08-10 → 2026-05-21, median
  gap 1.0 day (~28yr).

### 3.2 Bloomberg 0-5 Year TIPS → `Bloomberg US TIPS (Series-L)` (^BBUTISTR)

- **Duration-concept mapping** — the target is short-dated TIPS. `Bloomberg US TIPS
  (Series-L)` is the canonical Bloomberg TIPS index; it is the **only** Bloomberg
  inflation-linked index YCharts carries (no maturity-banded TIPS variant exists on the
  platform).
- **Credit-quality match** — exact: US Treasury inflation-protected securities, identical
  asset class.
- **Residual** — full-maturity (average maturity ~7-8yr) vs the 0-5yr target; the chosen
  index runs longer in duration than a 0-5yr cut.
- **Depth-confirmed live:** HTTP 200, 7,057 daily points, 1998-04-20 → 2026-05-21, median
  gap 1.0 day (~28yr).

### 3.3 Bloomberg 20+ Year Treasury → `Bloomberg US Long Government/Credit` (^BBUSLGCRTR)

- **Duration-concept mapping** — the defining attribute of "20+ Year Treasury" is the
  **long-duration** (long-end rate-sensitivity) concept. `Bloomberg US Long
  Government/Credit` is the only Bloomberg-origin long-duration fixed-income index YCharts
  carries — the Bloomberg Treasury family on YCharts is broad-only (`^BBUSTTR`,
  ~mid-duration) and the Government/Credit maturity bands top out at 1-5yr. Of the catalog,
  `^BBUSLGCRTR` is the single index that captures the long-end concept.
- **Credit-quality match** — partial: it is Government **+** investment-grade Credit, not
  pure Treasury. A substantial Government component remains, but the index carries some
  IG corporate-credit-spread exposure a pure 20+yr Treasury does not.
- **Residual** — (a) the IG-credit component above; (b) effective duration somewhat short
  of a pure 20+yr Treasury (the "Long" family spans ~10yr+, not strictly 20+).
- **Why not the broad `Bloomberg US Treasury` (^BBUSTTR)?** It is pure Treasury but
  all-maturity (~mid-duration) — it does **not** represent the long-end duration concept,
  which Andrew's ruling makes the priority attribute. A mid-duration index would not track
  the long-bond rate sensitivity the portal entity exists to show. `^BBUSLGCRTR` trades a
  modest credit residual for the correct duration concept — the right call under the
  ruling.
- **Depth-confirmed live:** HTTP 200, 8,092 daily points, 1994-02-28 → 2026-05-21, median
  gap 1.0 day (~32yr).

## 4. Honest labeling

All 3 carry a representative-index disclosure into the corrected C2 pull-spec rows: the
portal series must note it is a *representative* Bloomberg index, not the exact requested
maturity band, with the residual stated. None is presented as the exact 0-5yr/20+yr index.

## 5. Pull-spec correction (AC4)

`docs/briefs/mdsrc-c2-pull-spec-prestage-20260521.csv` — the 3 rows (0-5Yr HY, 0-5Yr
TIPS, 20+Yr Treasury) corrected from the V1A `BLOCKED -- escalation` state to
`meets-via-representative-Bloomberg-index (V1B 2026-05-22)` + `READY`, each with the
chosen symbol, `calcs=id:level`, depth evidence, and the representative-index
honest-labeling note. With V1A (band 1) + V1B (bands 2-4), **all 76 C2 pull-spec rows are
now resolved** — the pull-spec is complete.

## 6. Compiler Tools

V1B is a YCharts-entity sourcing task — no gold/portal/route/IAM/schema change; no comp-*
graph tool applies (per the TO note). Empirical self-checks: Phase-1 — all 3 chosen
indices depth-confirmed live (HTTP 200, daily gap 1.0d, 28-32yr history — PASS). Phase-2 —
all 3 are Bloomberg-origin, YCharts-carried, each with a documented representativeness
basis (duration-concept mapping + credit match + residual) — PASS; zero bands escalated.
`.comp-graph/.agent_context` TO_ID set to `YALP_MDSRC.V1B`.

## 7. Acceptance criteria

| AC | Status |
|---|---|
| AC1 — each of the 3 bands resolved to a representative Bloomberg-origin index YCharts carries | MET — ^BBUSCOHYTR / ^BBUTISTR / ^BBUSLGCRTR |
| AC2 — per band: representativeness basis documented (duration-concept mapping, credit match, residual) | MET — §3 |
| AC3 — each chosen index depth-confirmed live (HTTP 200, daily, adequate history) | MET — 6,973 / 7,057 / 8,092 daily pts, all 1994-1998 → 2026, gap 1.0d |
| AC4 — the 3 C2 pull-spec rows corrected; brief committed; RAVC2 to COO + CC CTO | this brief + the pull-spec correction committed; RAVC2 on commit |
