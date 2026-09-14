# POSN_ASTTAX -- CLOSE-OUT BREAKDOWN (for Andrew's alignment, BEFORE any worker)

**Author:** `1.0.0_SA_CTO~Z` (L2/L4 owner) - **Date:** 2026-09-14 ~17:2xZ
**On:** Andrew-direct ~16:5xZ, record `ANDREW_DIRECT_20260914_165xZ_SITEZ_POSN_ASTTAX_ONLY_BREAKDOWN_BEFORE_WORKERS.md` @`f529179076`
**Built from:** `4.0.0_SA_CRO~Z` brief v0.1 @`ee4b7e5539` (+ row `Z-S65`); round-4 packet `ledger/ROUND4_PACKET.md`;
worker results U1 (`~15`), U3 (`~16`), U4 (`~17`); PRD v0.6 @`ded02d9a9c`; portal pin `e85f6eb84f`.
**Status:** PROPOSAL. Nothing here is cut, signed, deployed or ruled. Andrew's gate: no worker until he aligns.

---

## 1. WHAT "DONE" MEANS, NARROWED TO THE POSITIONING PAGE

On the Positioning page, in all three modes (Models, ETFs, Satellites):
- every holding sits in exactly one of the five classes, in the one order, in the one colour;
- the Satellites mode shows what Black Diamond actually holds -- GLD in its own Commodities bucket, VXX under
  Structured -- at the weights BD trades;
- the class labels come from ETFClassifier's served table, so changing one row there changes the page with no
  portal edit;
- backend deployed; frontend **built and committed behind the freeze** (Andrew 2026-09-14 05:31Z: *"the frontend
  being done is defined as built and committed behind the freeze"*). The portal promote stays his separate word.

**The Positioning page is 14 files at the pin** (`git ls-tree e85f6eb84f -- src/pages/Positioning`): one tab
(`HoldingsTab.tsx`), one summary panel (`PositioningSummary.tsx`), mode adapters (`etfAdapter.ts`,
`satelliteAdapter.ts`, `bookSet.ts`), `types.ts`, and the shared colour registry `src/lib/chartColors.ts` it imports.

## 2. THE ONE PREMISE TO ALIGN ON FIRST

Andrew's framing (~16:34Z): GLD/VXX live in the Satellite *outside* its model constituents. **Measured by
`4.0.0_SA_CRO~Z` today (81 rebalancer files): every Opal Satellite has 0 securities at its root; GLD/VXX sit
inside Black Diamond's copy of each model.** Yang's copy of the same models -- which the portal blends to build
satellites -- carries no GLD and less VXX. So the loss happens because the portal blends the wrong version of the
models, not because anything sits outside them. Today's Satellites mode is wrong on gold for 7 of 9 satellites
and on VXX for 6 of 9.

**Consequence for the design (CRO R1-R4):** Satellites mode reads BD's holdings, flattened and summed by ticker;
Models mode stays on Yang; the gap between them is shown per ticker, never added together; every ticker is
labelled from ETFClassifier. One existing producer extended, one adapter changed, no new pipeline.

## 3. THE WORK -- round 5, one issuance, 8 cells

| cell | what | where | depends on |
|---|---|---|---|
| **B1** | Deploy the already-committed hardened positioning generator (running bytes are 2026-08-18 and crash on a retag); set the three new classes' benchmark rows to an explicit, labelled zero | `yang-generate-positioning` (+ `BENCHMARK_ALLOCATIONS` in `yang-generate-allocation-summary`); never-widen halves CTO+COO with the writer census printed | -- |
| **B2** | Satellite holdings: emit `holdings.json` beside `registry.json` -- per satellite, BD components summed by ticker, `weight` / `weight_models_blend` / `overlay`, class labels from ETFClassifier | `cot-satellites-registry-producer`, `s3://opal-data-cot/platinum/satellites/`; deploy | -- |
| **B3** | Seeder guard: apply the round-4 preserve-don't-clobber patch (+57/-2, `git apply --check` rc=0) so a re-seed cannot revert the retag (measured: it reverts 4 of 4) | `data/black_diamond/scripts/classification/seed_canonical_securities.py` (lane POD4) | -- |
| **F1** | Colour registry: add `structured` (pink) and `commodities` (a NEW gold token); fix `'Commodities'` currently a shade of equity blue (`:308`) | `portal/src/lib/chartColors.ts` | -- |
| **F2** | Positioning renders five classes: order literal `HoldingsTab.tsx:1392`, colour map `:215`, drop the Hedge->Equity fold `:1381-1383`; one row per class `PositioningSummary.tsx:545-546`; allocation type widened to five keys | `portal/src/pages/Positioning/` | F1 token name fixed in the order |
| **F3** | Satellites mode reads B2's `holdings.json`; Models and ETFs modes untouched | `portal/src/pages/Positioning/shared/satelliteAdapter.ts` (+ endpoint) | B2 schema fixed in the order |
| **F4** | No-regression guard, Attribution page: the same two-class literal in three files, extended to five -- ONLY so the retag does not silently drop rows there (card 2) | `SelectionTab.tsx:321`, `AssetAllocationSummary.tsx:92`, `StylePolicyComparison.tsx:156` | card 2 |
| **R1** | THE RETAG, last: the 12 tickers in BOTH stores (DynamoDB `etf-classifications` + `ETF_CLASSIFICATIONS`), VNQ `management_style` fixed; then the bar on the local build over all 9 satellites and both other modes: served label right, weight unchanged, served rows = rendered rows, class subtotals = total; plus one boundary flip (PDBC) proving FWD-5 with no portal edit | both stores; local build | B1 deployed, B3 landed, F1-F3 built |

**Sequencing:** B1, B2, B3, F1, F4 run in parallel; F2 and F3 in parallel once their order fixes the token name and
the `holdings.json` schema up front; **R1 strictly last** -- a retag into a two-class page hides the row while its
weight stays in the total (the Cash defect PROD v2.1.167 already shipped once).

**The 12 (round-4 U4, subtraction over all 285 table rows):** Commodities -- DBC, GLD, GSG, IAU, SLV, USO, PDBC;
Structured -- VXX, VIXY, UVXY, QBER; Alternatives -- VNQ. BIPC stays Equity.

## 4. BEFORE THE ISSUANCE -- seat steps, no workers

1. `2.0.0_SA_COO~Z` closes the four carried round-2/3 orders: `TO-S2-1`/`TO-S3-1` superseded by `TO-T6-1`/`TO-T7-1`
   (their own headers say so); `TO-T6-1` cancelled as written, re-cut as R1; `TO-T7-1` cancelled (card 6). Until
   these four are terminal, the round-4 slug is refused (open orders count per project).
2. `3.0.0_SA_CVO~Z` adjudicates round 4 (`ROUND4_PACKET.md`, owed since 2026-09-13T07:54Z) and cuts the slug.
3. `1.0.0_SA_CTO~Z` writes `ROUND_ANALYSIS.round4` and PRD v0.7: FWD-6 narrowed to the Positioning page's three
   modes (ENDPOINT change -> `3.0.0_SA_CVO~Z` re-signs); `C-TWO-SURFACES` replaced; new `C-SATELLITE-SOURCE` (R1-R4)
   and surface row S4; retag set = 12; the scope-outs in s.6; disarms `Z-S65` and settles `Z-W15-S2` / `Z-W17-S3`.
   `4.0.0_SA_CRO~Z` re-signs the brief half.
4. `2.0.0_SA_COO~Z` decomposes round 5 to s.3's eight cells. **Any deviation from s.3 comes back to Andrew before the
   issuance.** Portal commits land on ONE named POSN drain ref cut from `e85f6eb84f`; the gitlink does not move.

## 5. CARDS -- decisions for Andrew, each with the recommendation

1. **Source rule:** Satellites = BD as traded, summed by ticker; Models = Yang; the gap shown, never added.
   **REC: yes** -- the only rule under which the Satellites column is true.
2. **Scope = the Positioning page only**, plus F4's three one-line guards on Attribution. CMA/Philosophy,
   AdvisorIntelligence and the rest of Attribution are out. **REC: yes, with F4** -- without it the retag makes
   Attribution silently drop commodity rows while keeping their weight in the total.
3. **Retag set = the 12 above; BIPC stays Equity.** **REC: yes.**
4. **Gold colour:** no gold token exists and amber already means Cash. **REC: mint a new gold token.**
5. **Benchmark rows for Structured / Commodities / Alternatives:** today a 10% position reads as a 10% bet against
   an implicit zero. **REC: explicit zero, labelled "no benchmark".**
6. **Cut from this close-out:** reconciling the dormant `is_hedge()` helper (no live caller) and reconciling the
   second classification table `bd-securities` (9,631 rows, disagrees on 13 of 13 retag tickers). Keep only B3,
   which stops that seeder undoing the retag. **REC: yes** -- neither changes what the Positioning page shows.
7. **Done = backend deployed + frontend built and committed behind the freeze; promote on your separate word.**
   **REC: yes** -- matches your 05:31Z definition.
8. **Add GLD and VXX to the Bloomberg daily pull** (`0.0.3_BG_BBGTerminal`, two strings; those fields have no
   backfill; until then fee/yield/duration show blank for GLD). **REC: yes, now** -- it serves this page and costs nothing.

## 6. OUT OF SCOPE -- named so no worker picks them up

- CMA/Philosophy frontend (Yang's sheet, later); AdvisorIntelligence readers; Attribution beyond F4.
- `bd-securities` reconciliation; retiring the 136-entry seed dict (only the 12 rows change in it).
- The Yang-vs-BD model drift beyond GLD/VXX (ICSH, BIV) -- a Yang/Andrew reconciliation, not a defect.
- The SPYM duplicate row, VXX beta anomaly, the `opal-partners-data` ETF publisher.
- BIPC's class; any new monitor, alert or parallel pipeline.

## 7. FOUND ON THE WAY -- surfaced, not acted on

- `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py` carries an UNCOMMITTED 13+/6- change in the
  shared tree (mtime 2026-09-11 01:47 ET: the canonical CASH line and a drop of empty values DynamoDB rejects on an
  index key). Not a POSN surface; owner to land or discard.
- `4.0.0_SA_CRO~Z` brief s.3/s.4 list `SelectionTab.tsx` and `holdings-shared.tsx` as Positioning; both are
  Attribution files at the pin. s.3 above reflects the pin.
