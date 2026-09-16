# POSN_ASTTAX -- CLOSE-OUT BREAKDOWN (for Andrew's alignment, BEFORE any worker)

**Author:** `1.0.0_SA_CTO~Z` (L2/L4 owner) - **Date:** 2026-09-14, v0.5 ~17:5xZ
**On:** Andrew-direct ~16:5xZ, record `ANDREW_DIRECT_20260914_165xZ_SITEZ_POSN_ASTTAX_ONLY_BREAKDOWN_BEFORE_WORKERS.md` @`f529179076`
**Built from:** `4.0.0_SA_CRO~Z` brief (v0.1 @`ee4b7e5539`, v0.2 @`f846dd72da`, v0.3 @`727b82e8d2`; row `Z-S65`); round-4
packet `ledger/ROUND4_PACKET.md`; worker results U1 (`~15`), U3 (`~16`), U4 (`~17`); PRD v0.6 @`ded02d9a9c`; portal pin `e85f6eb84f`.
**Status:** **v0.5 -- ALIGNED BY ANDREW ~17:3xZ** at the `4.0.0_SA_CRO~Z` terminal (msg 22861; record
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260914_173xZ_POSN_ASTTAX_BREAKDOWN_ALIGNED_ALL_RECS_APPROVED_ATTRIBUTION_UNTOUCHED.md`),
VERBATIM: *"All recs approved. Keep in mind that attribution, for now at least, is staying to just Equities and Fixed
Income on asset classes, because those are the only ones Yang uses, and we stick to his layout. Eventually that may
change, but need to keep in mind that the work we're doing here is very much contained to "Positioning", we do not
touch "Attribution""*. **The worker gate is RELEASED on the eight cells below.** v0.4 folded `2.0.0_SA_COO~Z`'s
review (22857 / 22860). v0.2 folded `4.0.0_SA_CRO~Z`'s flags N1-N4 (msg 22839). **v0.3 folds Andrew's six rulings
at the `4.0.0_SA_CRO~Z` terminal ~17:2xZ** (msg 22842; record
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260914_172xZ_POSN_ASTTAX_SIX_CARDS_RULED.md` @`727b82e8d2`)
and the card-4 routing (msgs 22850, 22852, 22855).
Nothing here is cut, signed, deployed or ruled by this seat. Andrew's gate: no worker until he aligns.

---

## 1. WHAT "DONE" MEANS, NARROWED TO THE POSITIONING PAGE

On the Positioning page, in all three modes (Models, ETFs, Satellites):
- every holding sits in exactly one of the five classes, in the one order, in the one colour;
- the Satellites mode shows the TOTAL of each ticker the satellite holds -- e.g. total GLD as asset class Commodities,
  sub-asset Metals; total VXX as Structured, sub-asset Hedge -- with weighted characteristics for the satellite;
- class and sub-asset labels come from ETFClassifier's served table, so changing a row there changes the page with no
  portal edit;
- the Models mode is NOT changed (Andrew ~17:2xZ: *"models do not get updated because they are not changing"*);
- backend deployed; frontend **built and committed behind the freeze** (Andrew 2026-09-14 05:31Z: *"the frontend
  being done is defined as built and committed behind the freeze"*). The portal promote stays his separate word.

**The Positioning page is 14 files at the pin** (`git ls-tree e85f6eb84f -- src/pages/Positioning`): one tab
(`HoldingsTab.tsx`), one summary panel (`PositioningSummary.tsx`), mode adapters (`etfAdapter.ts`,
`satelliteAdapter.ts`, `bookSet.ts`), `types.ts`, and the shared colour registry `src/lib/chartColors.ts` it imports.

## 2. THE PREMISE AND THE DESIGN, AS RULED

**Measured by `4.0.0_SA_CRO~Z` (81 rebalancer files, 2026-09-14):** every Opal Satellite has 0 securities at its root;
GLD/VXX sit inside Black Diamond's copy of each model. Yang's copy -- which the portal blends to build satellites --
carries no GLD and less VXX. Today's Satellites mode is wrong on gold for 7 of 9 satellites and on VXX for 6 of 9.

**Andrew ~17:2xZ, VERBATIM:** *"Call 1, they should be summed because the goal is not to see what's yangs models versus
what's external residuual in the satellite; it is to see total GLD listed as Commodity Asset, Metals Sub-Asset, and to
see Total VXX (or whatever hedge securities) as Structured Asset, Hedge Sub-Asset. Call 2 Yes. Call 3, mint some yellow
color, yes. Call 4 Yes. Call 5 Yes. Call 6, definitely B, models do not get updated because they are not changing,
Satellites simply need to have an additional lambda to do weighted characteristics aggregates ."*

**So the design is:** Satellites mode shows, per satellite, ONE total weight per ticker taken from Black Diamond,
summed across the satellite's sleeves; each ticker labelled (class + sub-asset) from ETFClassifier; weighted
characteristics computed server-side by an additional lambda. No Yang-vs-residual column. Models mode untouched.
WARN: "summed" must not add Yang's copy of a model on top of BD's -- BD's per-sleeve figure already includes what sits
inside the model (LT VXX: BD 1.87; adding Yang's 1.50 would read 3.37). Open item A in s.5 until he confirms.

## 3. THE WORK -- round 5, one issuance, 8 cells (F4 removed by Andrew's "we do not touch Attribution")

| cell | what | where | depends on |
|---|---|---|---|
| **B1** | Deploy the already-committed hardened positioning generator (running bytes are 2026-08-18 and crash on a retag); set the three new classes' benchmark rows to an explicit, labelled zero (ruled yes) | TWO functions, TWO served artifacts: `yang-generate-positioning` (the deploy Andrew approved 2026-09-13) **and** `yang-generate-allocation-summary` `BENCHMARK_ALLOCATIONS` (new code). ONE never-widen sign-off (CTO+COO) naming both functions and both artifacts, writer census printed | -- |
| **B2** | Satellite holdings: emit `holdings.json` beside `registry.json` -- per satellite, one total weight per ticker (BD components summed across sleeves), the per-sleeve breakdown, `asset_class` + `sub_asset_class` from ETFClassifier. No Yang comparison | `cot-satellites-registry-producer` + its IAM in `infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf` (second pinned PutObject key; DynamoDB read on `etf-classifications`); deploy | -- |
| **B3** | Seeder guard: apply the round-4 preserve-don't-clobber patch (+57/-2, `git apply --check` rc=0) so a re-seed cannot revert the retag (measured: it reverts 4 of 4) | `data/black_diamond/scripts/classification/seed_canonical_securities.py` (lane POD4) | -- |
| **B4** | **The additional lambda (ruled):** per satellite, weighted aggregates of fee / yield / duration / beta / returns = `holdings.json` weights x per-ticker characteristics (from Yang's `positioning_data.json` `current_holdings` where a Yang book holds the ticker; from the Bloomberg daily pull once GLD/VXX land there; NULL otherwise -- the null-weight share printed as coverage, never silently renormalised); writes one characteristics artifact beside `holdings.json`. A separate function, per his word "an additional lambda" | new function + Terraform + IAM (read `holdings.json`, read the positioning JSON on `opal-data-portal-v2`, read the ETF pull output, write one pinned key); its OWN EventBridge schedule offset after B2's, never success-of-upstream as the only trigger; no monitor. New key only, so never-widen is a stated non-application; ledger entry, `safe-apply`, `comp-iam gaps`. The cross-firm gate enumeration (`.tools/ds-precommit-check.py`) is read at the cut -- if it refuses the portal-bucket read, that comes back to Andrew before issuance | B2 schema fixed in the order |
| **F1** | Colour registry: `structured` (pink) and `commodities` (a NEW **yellow** token, ruled; not amber, which is Cash); fix `'Commodities'` currently a shade of equity blue (`:308`); sub-asset colours for `Metals` and `Hedge` | `portal/src/lib/chartColors.ts` | -- |
| **F2** | Positioning renders five classes: order literal `HoldingsTab.tsx:1392`, colour map `:215`, drop the Hedge->Equity fold `:1381-1383`; one row per class `PositioningSummary.tsx:545-546`; allocation type widened to five keys | `portal/src/pages/Positioning/` | F1 token names fixed in the order |
| **F3** | Satellites mode reads `holdings.json` (totals + labels) and B4's characteristics artifact and renders them; no computation in the adapter; the satellite's as-of is BD's partition date; Models and ETFs modes untouched | `portal/src/pages/Positioning/shared/satelliteAdapter.ts` (+ `src/api/endpoints/satelliteRegistry.ts`) | B2 + B4 schemas fixed in the order |
| **R1** | THE RETAG, last: the 12 tickers' `asset_class` AND the ruled `sub_asset_class` values (Metals / Hedge, item B) in BOTH stores (DynamoDB `etf-classifications` + `ETF_CLASSIFICATIONS`); every write level-explicit; VNQ `management_style` fixed; then the bar on the local build over all 9 satellites and both other modes: served labels right, weight unchanged, served rows = rendered rows, class subtotals = total. FWD-5 graded on the retag itself (rows changed in the one place, every mode reflecting it with no portal edit) | both stores; local build | B1, B2, B4 deployed; B3 landed; F1-F3 built |

**Sequencing (three waves, max concurrency 4):** B1, B2, B3, F1 in parallel; B4, F2, F3 in parallel once their orders
fix the token names and the two artifact schemas up front; orders carry full paths at the pin; **R1 strictly last** -- a retag into a two-class page hides the row while its weight stays
in the total (the Cash defect PROD v2.1.167 already shipped once).

**Encoding ruled here at L4 (this seat's call, per 22842/22849):** `Hedge` is a `sub_asset_class` value under
`Structured`. The legacy TOP-level `asset_class` value `hedge` is dissolved by R1. The two never share a field, and
every R1 write names its level.

## 4. BEFORE THE ISSUANCE -- seat steps, no workers

1. `2.0.0_SA_COO~Z` closes the four carried round-2/3 orders: `TO-S2-1`/`TO-S3-1` superseded by `TO-T6-1`/`TO-T7-1`
   (their own headers say so) -- **DONE @`93135eb5b9`**; `TO-T6-1` cancelled as written, re-cut as R1; `TO-T7-1` cancelled (item E). Until
   these four are terminal, the round-4 slug is refused (open orders count per project).
2. `3.0.0_SA_CVO~Z` adjudicates round 4 (`ROUND4_PACKET.md`) and cuts the slug. **In progress.**
3. `1.0.0_SA_CTO~Z` writes `ROUND_ANALYSIS.round4` and PRD v0.7 carrying the rulings: FWD-6 narrowed to the Positioning
   page (ENDPOINT change -> `3.0.0_SA_CVO~Z` re-signs); `C-TWO-SURFACES` replaced; `C-SATELLITE-SOURCE` (one total per
   ticker from BD, labelled, characteristics by the additional lambda) and surface row S4; the sub-asset encoding;
   the retag set; the scope-outs in s.6; disarms `Z-S65`, settles `Z-W15-S2` / `Z-W17-S3`, and dispositions `Z-W1-S1` / `Z-C-S1` (the `is_hedge` row, served
   by no cell once item E cuts it). `4.0.0_SA_CRO~Z` re-signs the
   brief half.
3b. The deploy preconditions land BEFORE the issuance (a worker cannot wait on a sign-off): CTO+COO never-widen halves
   for B1 (both functions, both served artifacts, writer census N printed) and B2 (the re-deployed registry producer
   plus the new key), cited in the orders; B4's non-application stated in its order.
4. `2.0.0_SA_COO~Z` decomposes round 5 to s.3's eight cells. **Any deviation from s.3 comes back to Andrew before the
   issuance.** Portal commits land on ONE drain ref, `refs/drains/posn-5-portal`, cut from `e85f6eb84f` and recorded in
   `ledger/PORTAL_REFS.md`; the gitlink does not move.

**Card 4 (GLD + VXX into the Bloomberg daily pull) is NOT a round-5 cell.** It is a two-string edit to
`integrations/bloomberg/pipeline/etf_daily_pull.py:45` `FUNDS`, lane `ANY_EXEC_OR_AE`. On this device the scheduled
tasks run the working tree, so the edit is a production deploy the moment it lands: `1.0.0_SA_CTO~Z` gates it and
names the lander, with a change-management ledger entry opened first, after reading what `FUNDS` feeds.
`0.0.3_BG_BBGTerminal` cannot perform it (its write fence) and `0.0.0_AB_MSTR~Z` does not work projects. Today's
scheduled pull already ran (07:00 ET), so a landed edit first captures on 2026-09-15; capturing 2026-09-14 needs a
same-day ad-hoc Bloomberg pull -- **Andrew's trade** (open item H).

## 5. DECISIONS

**RULED by Andrew ~17:2xZ (CRO~Z card numbers):** 1 one total per ticker, Metals/Hedge sub-assets; 2 FWD-6 narrowed to
the Positioning page; 3 a new yellow token; 4 GLD + VXX into the Bloomberg daily pull; 5 labelled-zero benchmark rows;
6 models untouched, an additional lambda for weighted characteristics.

**A-G APPROVED by Andrew ~17:3xZ ("All recs approved"), with D overridden to OUT. H below is being confirmed:**
- **A. "Summed" = BD's total across the satellite's sleeves, NOT Yang's number added on top.** **REC: yes** (adding
  Yang's copy double-counts: LT VXX would read 3.37 instead of 1.87). Also put by `4.0.0_SA_CRO~Z` at its terminal.
- **B. Sub-asset mapping for the rest of the 12.** **APPROVED:** Metals = GLD, IAU, SLV; Hedge = VXX, VIXY, UVXY, QBER;
  DBC, GSG, USO, PDBC keep their current sub-asset (broad commodity index / oil); **VNQ -> Real Estate**.
- **C. Retag set = the 12:** Commodities -- DBC, GLD, GSG, IAU, SLV, USO, PDBC; Structured -- VXX, VIXY, UVXY, QBER;
  Alternatives -- VNQ; BIPC stays Equity. **REC: yes.**
- **D. F4 -- OUT.** Andrew: *"we do not touch Attribution"*; Attribution stays two-class on Yang's layout. ACCEPTED
  CONSEQUENCE, not a defect to file: after R1, VXX (and any retagged ticker Yang's models hold) drops out of
  Attribution's per-class groups while its weight stays in the totals.
- **E. Cut from this close-out:** the dormant `is_hedge()` helper and reconciling the second table `bd-securities`
  (9,631 rows; disagrees on 13 of 13). Keep only B3. **REC: yes.**
- **F. Done = backend deployed + frontend built and committed behind the freeze; promote on your separate word; the
  "yes" to labelled-zero benchmarks widens the 2026-09-13 deploy approval to `yang-generate-allocation-summary`.**
  **REC: yes.**
- **G. RELEASED.** `2.0.0_SA_COO~Z` issues the eight cells after the round-4 slug, `ROUND_ANALYSIS.round4` and PRD v0.7
  signed (s.4).
- **H. Bloomberg pull "today":** land the edit today and take 2026-09-15 as the first captured day, or ALSO run a
  same-day ad-hoc pull to capture 2026-09-14 (a download-class Bloomberg act, your per-use word). **REC: land today;
  the ad-hoc pull only if the 2026-09-14 characteristics matter to you** -- B4 renders NULL until data exists either way.

## 6. OUT OF SCOPE -- named so no worker picks them up

- Changes to the Models mode or Yang's model data (ruled); any Yang-vs-BD comparison column (ruled).
- CMA/Philosophy frontend (Yang's sheet, later); AdvisorIntelligence readers; **the Attribution page, entirely** (ruled).
- `bd-securities` reconciliation; retiring the 136-entry seed dict (only the 12 rows change in it).
- The Yang-vs-BD model drift beyond GLD/VXX (ICSH, BIV) -- a Yang/Andrew reconciliation, not a defect.
- The SPYM duplicate row, VXX beta anomaly, the `opal-partners-data` ETF publisher.
- BIPC's class; any new monitor, alert or parallel pipeline.

## 7. FOUND ON THE WAY -- surfaced, not acted on

- `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py` carries an UNCOMMITTED 13+/6- change in the
  shared tree (mtime 2026-09-11 01:47 ET: the canonical CASH line and a drop of empty values DynamoDB rejects on an
  index key). Not a POSN surface; owner to land or discard.
- Brief v0.1 listed `SelectionTab.tsx` / `holdings-shared.tsx` as Positioning; both are Attribution at the pin
  (corrected in brief v0.2).
