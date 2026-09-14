# POSN_ASTTAX -- L5 DECOMPOSITION (round 5) -- DRAFT, NOT CUT

**archetype:** IMPLEMENT (the first issuance that writes the code, data and frontend the six bars read)
**Owner (L5-L6):** `2.0.0_SA_COO~Z` - **Date:** 2026-09-14 ~17:5xZ - **Directive:** D4 - **Macro:** POSN - **Fabric:** site-z
**PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075` (s.0 ADDENDUM v0.7 + ENDPOINT FWD-6 narrowed), read IN FULL at
the moment of drafting. **Gate at draft time:** `prd-signoff.py status POSN_ASTTAX` -> **ADMITTED**, ratified-text SIGNED
`3.0.0_SA_CVO~Z` current, brief SIGNED `4.0.0_SA_CRO~Z` current (read by this seat, not taken from 22880).
**Answers:** `1.0.0_SA_CTO~Z`'s round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` @`221ed89911`, which answers
`3.0.0_SA_CVO~Z`'s round-4 slug `surprise-channel/remediations/REMEDIATION_v4.Z.md` @`ae66872ce5`.
**Cell-level authority:** the close-out breakdown
`org/tier1_exec/1.0.0_SA_CTO/deliverables/POSN_ASTTAX_CLOSEOUT_BREAKDOWN_20260914_Z.md` **v0.5** @`0949f2d53d`, ALIGNED by
Andrew ~17:3xZ (*"All recs approved ... we do not touch Attribution"*, record by `4.0.0_SA_CRO~Z` @`727b82e8d2` family).

> **STATUS OF THIS FILE: DRAFT.** Eight cells are aligned. A NINTH (`AT5-s-9`, the edge-router leaf allowlist) is
> **PROPOSED-PENDING-ANDREW**: accepted at L4 by `1.0.0_SA_CTO~Z` (msg 22884) as essential, put to Andrew because it
> deviates from breakdown s.3 (s.4 step 4). **Nothing is cut until his word lands and both never-widen halves are
> committed and cited** (s.4 step 3b). The decomposition freezes at the cut; this draft may still move.

---

## 0. WHY THIS ROUND EXISTS -- the subtraction, re-read at source

```
DENOMINATOR   19 task orders under POSN_ASTTAX (15 complete, 2 superseded @93135eb5b9, 2 cancelled @9e6e72ea8b)
DECLARED       6 (FWD-1..FWD-6, PRD v0.7 header endpoint_outcomes)
NAMED          6      <- every outcome is NAMED by at least one order (round-4 analysis s.1)
REALIZED       0      <- no outcome is SERVED: rounds 1-4 measured, hardened and priced; none deployed or rendered
```
Naming is not serving (PRD s.7 qualifier, v0.6). **Round 5 is the first issuance that writes what the bars read:**
the deployed backend (B1, B2, B4, B5), the durability guard (B3), the Positioning frontend built and committed behind
the freeze (F1-F3), and the retag itself, last (R1). C-DONE binds the finish line; the promote is Andrew's separate word.

## 1. THE CONSTRAINTS THAT SHAPE EVERY CELL -- from PRD v0.7 s.0, stated first

- **C-POSITIONING-ONLY** -- the surfaces are the 14 Positioning files at portal pin `e85f6eb84f` plus `src/lib/chartColors.ts`.
  **The Attribution page is not touched. F4 is OUT** (Andrew ~17:3xZ). Accepted consequence, not a defect: after R1, VXX drops
  out of Attribution's per-class groups while its weight stays in its totals; a worker who sees it files nothing.
- **C-SATELLITE-SOURCE** -- Satellites mode shows ONE total weight per ticker from Black Diamond, summed across the satellite's
  sleeves; **Yang's copy is never added** (LT VXX: BD 1.87, not 1.87 + 1.50); labels from the served ETFClassifier table;
  weighted characteristics by an ADDITIONAL lambda (server-side, NULL disclosed, never renormalised). Models mode unchanged.
- **C-SUB-ASSET** -- Metals = GLD, IAU, SLV; Hedge = VXX, VIXY, UVXY, QBER; Real Estate = VNQ; DBC, GSG, USO, PDBC keep theirs.
  `Hedge` is a `sub_asset_class` value under `Structured`; the top-level `hedge` dissolves; every write names its level.
- **C-RETAG-SET** -- TWELVE, BOTH stores, LAST. **C-COLOURS** -- a NEW yellow token for Commodities, pink for Structured.
- **C-BENCHMARK** -- labelled zero for the three new classes in BOTH generator functions under ONE sign-off.
- **C-CUTS** -- `is_hedge()` and `bd-securities` reconciliation are out; only the seeder guard (B3) stays.
- **The freeze, its corrected cause (`C-S105`):** it never barred portal SOURCE writes. Write source YES; commit inside the
  submodule YES on ONE drain ref `refs/drains/posn-5-portal` cut from `e85f6eb84f`, recorded in `ledger/PORTAL_REFS.md` at the
  first portal commit; **MOVE THE GITLINK NO; promote / DEV / PROD push NO.** Shared checkout measured AT the pin 2026-09-14
  ~17:2xZ (is-ancestor TRUE both ways); every portal worker verifies its OWN clone the same way before writing (`C-S106`).

## 2. THE RECTANGLE -- surfaces x cells, status vocabulary {NOT_EVALUATED, CUT, ISSUED, TERMINAL, PROPOSED-PENDING-ANDREW}

PRD v0.7 s.7 as amended: **S1** ETFClassifier + the satellite holdings producer + the characteristics lambda (FWD-1, FWD-2,
FWD-5); **S2** the class registry, order + colour (FWD-3, FWD-4); **S3** the Positioning page's three modes (FWD-6).

| cell | breakdown | serves (surface -> outcomes) | status | placement |
|---|---|---|---|---|
| `AT5-s-1` | **B1** deploy the hardened positioning generators + labelled-zero benchmarks | S1 -> FWD-1, FWD-2, FWD-5 (the served plane finally carries five classes) | NOT_EVALUATED | site-z |
| `AT5-s-2` | **B2** `holdings.json` beside `registry.json` | S1 -> FWD-1, FWD-2 on the Satellites mode | NOT_EVALUATED | site-z |
| `AT5-s-3` | **B3** seeder preserve-don't-clobber guard | S1 -> FWD-5 (durability: a re-seed cannot revert the retag) | NOT_EVALUATED | site-z |
| `AT5-s-4` | **B4** the additional characteristics lambda | S1 -> FWD-1, FWD-2 on the Satellites mode (characteristics) | NOT_EVALUATED | site-z |
| `AT5-s-5` | **F1** colour registry: pink, NEW yellow, Metals/Hedge sub-colours | S2 -> FWD-3, FWD-4 | NOT_EVALUATED | site-z |
| `AT5-s-6` | **F2** Positioning renders five classes (order, colour map, rows, five-key allocation) | S3 -> FWD-6; S2 -> FWD-3/FWD-4 applied | NOT_EVALUATED | site-z |
| `AT5-s-7` | **F3** Satellites mode reads `holdings.json` + characteristics; no computation | S3 -> FWD-6 on Satellites; S1 outcomes rendered | NOT_EVALUATED | site-z |
| `AT5-s-8` | **R1** THE RETAG, both stores, both levels, then the bar on the local build | S1 -> FWD-1, FWD-2, FWD-5 EXERCISED; S3 -> FWD-6 EXERCISED | NOT_EVALUATED | site-z |
| `AT5-s-9` | **B5** edge router leaf allowlist {registry, holdings, characteristics}.json + Lambda@Edge deploy | S3 -> the READ PATH for FWD-6 on Satellites (no outcome of its own) | **PROPOSED-PENDING-ANDREW** | site-z |

**Every cell is served by a worker at L7; no cell is owned by a seat.** The seat acts that precede the issuance (the halves,
s.4 step 3b) are not cells.

## 3. THE CELLS -- what each settles, its write surface, its measured premise

### `AT5-s-1` -- B1: deploy the two positioning generators, with labelled-zero benchmark rows (C-BENCHMARK)
**Premise, measured 2026-09-14 ~17:4xZ:** `yang-generate-positioning` live `CodeSha256 PRg64EGzQtLw7/HAhyN/jNP6rd01PrcLK4wKqCHAKfQ=`,
`LastModified 2026-08-18T18:34:43Z`; its PACKAGE carries FOUR commits since the last one before that build (`69b867c4eb`):
`7f247caae0` harden, `c34eab85dc` unknown-is-not-equity, `07c046fa63` five classes through the generator (all 2026-09-11), and
`b0e1f33471` (ETFS_INGEST TO-9-DS, 2026-08-28, display-name beautification in the vendored `etf_classifications_dynamodb.py` --
NOT a POSN commit; it ships with this deploy and is named in both halves). `yang-generate-allocation-summary` live
`LastModified 2026-08-04T22:17:48Z` with ZERO source commits since its build, so B1 ships exactly one change there; `BENCHMARK_ALLOCATIONS` at its `lambda_function.py:46` and `OUTPUT_KEY
json/positioning/allocation_summary.json` at `:34`. The positioning generator's `BENCHMARK_ETFS` (`:178`) holds THREE classes and
its `benchmark_etf_info` (`:186-203`) **falls back to `cash` with a WARN** for a class with no benchmark ETF -- a silent-wrong
that C-BENCHMARK's labelled zero replaces. `deploy.sh` in that directory is a BARE `aws lambda update-function-code` and is
**NEVER used** (CLAUDE.md NEVER: Terraform only); the sanctioned path is `infra/aws/lambda/ci/build-and-upload.sh yang-pipeline
<fn>` -> `safe-apply` scoped to `module.generate_positioning` + `module.generate_allocation_summary` (`lambdas.tf:162-184`) ->
0-diff re-plan -> `record-terraform-deploy.sh` -> the SFN regeneration and the served read (the 2026-08-18 ledger's leg shape).
**Write surface:** `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py` (the
labelled-zero benchmark for `structured`/`commodities`/`alternatives`, replacing the cash fallback), `.../yang-generate-allocation-
summary/lambda_function.py` (`BENCHMARK_ALLOCATIONS` labelled zeros), `infra/aws/lambda/ci/lambda-source-map.json` (written by the
builder), `infra/aws/terraform/yang-pipeline/` (plan/apply/record; CHANGELOG.json by the recorder), the change-management ledger
entry, the worker's deliverables dir. **Precondition, cited in the order:** `ledger/NEVER_WIDEN_ROUND5_COO_HALF.md` +
`NEVER_WIDEN_ROUND5_CTO_HALF.md` committed. **Bar:** deployed `CodeSha256` == the built zip's hash for BOTH functions; a 0-diff
re-plan; the regenerated `positioning_data.json` carries the five-class keys (`structured`, `commodities`, `alternatives` beside
`cash`, `fixed_income`, `equity`, per the generator's `:271-279`) for every model and its benchmark rows carry an EXPLICIT zero
labelled "no benchmark" for the three new classes; `allocation_summary.json` likewise; membership and every non-class payload
byte-identical to the pre-deploy read (the 2026-08-18 leg-7 shape). Rollback: the artifact bucket is versioned; prior
VersionIds are printed in the COO half.

### `AT5-s-2` -- B2: `holdings.json` beside `registry.json` (C-SATELLITE-SOURCE, totals + labels only)
**Premise, measured:** the trigger `infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py` (128 lines)
vendors the REAL producer `data/assets/scripts/gold/build_satellites_registry.py` (313 lines; `DETAIL_KEY` `:91`, `REGISTRY_KEY`
`:92`, `build_books` `:158-198`, `publish` `:223-234`) out of git at a REQUIRED `--pin` (`build_package.py`, repo-mirroring layout);
`satellites_registry.py` is a CONFORMANCE ORACLE and **must not be converted** (its own header). The `.tf` pins ONE PutObject key and
grants no DynamoDB read. `registry.json` served `LastModified 2026-09-14T07:00:19Z`, 2196 bytes; `holdings.json` **404 (absent)**.
**Write surface:** `data/assets/scripts/gold/build_satellites_registry.py` (or a sibling `build_satellites_holdings.py` -- the
build ladder says EXTEND; the cell decides and states why), the trigger, `build_package.py` (member list gains
`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` by pin, never a copy), `infra/aws/terraform/cot-pipeline/
satellites-registry-producer.tf` (second pinned PutObject key `platinum/satellites/holdings.json`; `dynamodb:GetItem`/
`BatchGetItem` on the `etf-classifications` table ARN; memory/timeout re-measured, not inherited), the ledger entry, the
deliverables dir. **Schema, fixed in the order:** `{as_of, source, claim: "measured", satellites: {<code>: {holdings:
[{ticker, weight, asset_class, sub_asset_class, sleeves: [{book, weight}]}], coverage: {labelled, unlabelled}}}}` -- weight = the
sum of `absoluteAllocation` across the satellite's sleeves (BD's figure; Yang never added); a ticker with no registry row carries
`asset_class: null` and is COUNTED in `coverage.unlabelled`, never guessed. **Bar:** the artifact published by the SCHEDULED
07:00Z fire (an ad-hoc run is QA, never the acceptance); for Sat 15 GLD reads 8.34 and Sat 30 GLD reads 7.25 (= ST 6.26 + INT
1.00, the CRO's measured example), with the sleeve breakdown printed; nine satellites, one row per ticker per satellite.

### `AT5-s-3` -- B3: the seeder guard (`C-S92`, `C-S93`)
**Premise, measured:** `u3_proposed_patch.diff` (+57/-2) at `deliverables/0.9.0_WK_POSN_ASTTAX~16/` still applies cleanly at HEAD
(`git apply --check` rc=0, 2026-09-14 ~17:4xZ). A re-seed reverts 4 of 4 carried members (U3-AC1). The worker grant is additive
to the POD4 lane rule (`owned-paths-validate.py:112-147`, self-test `:458-459`), so the cell is cuttable as a worker cell.
**Write surface:** `data/black_diamond/scripts/classification/seed_canonical_securities.py` ONLY (+ deliverables dir, channel).
**Bar:** the CHANGED `.py` passes `.tools/commit-gate.sh` (the criterion names the changed file -- `C-S93`); the pure-ASCII
check names an instrument that actually selects that path and carries a firing control (`C-S92`); a dry run against a SCRATCH
copy of the table shows REFUSED rc=1 on a disagreeing row and MINTS an absent row (U3's mutant control re-run on the applied
file); **no live table write** in this cell.

### `AT5-s-4` -- B4: the additional characteristics lambda (C-SATELLITE-SOURCE, "an additional lambda")
**Premise, measured:** the Bloomberg ETF pull writes `s3://opal-data-etfs/bbg/<asof>/characteristics.{csv,parquet}` + `run_manifest.json`
(`etf_daily_pull.py:37-38`, `:330-350`); GLD/VXX enter as `EXTRA_SECURITIES` @`ac3e03a317`, first captured by the 2026-09-15 07:00 ET
fire (ledger `posn-bbg-etf-pull-gld-vxx`). Yang's `positioning_data.json` `current_holdings` carries per-ticker characteristics for
the tickers a Yang book holds. `characteristics.json` **404 (absent)**. The cross-firm gate `.tools/ds-precommit-check.py:68-70`
keys on a script's HOME DIR (`data/cot/`, `data/black_diamond/`) and enumerates `opal-data-bd|inf|49financial` / `opal-data-cot`;
`opal-data-portal-v2` and `opal-data-etfs` are in NO foreign list, and neither `data/assets/` nor `infra/aws/lambda/cot-pipeline/`
matches a home dir -- **the gate does not fire on B4's reads; no gate edit is needed** (read at the cut, per s.4 item 4).
**Write surface (NEW):** `infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/{lambda_function.py, build_package.py}`,
`data/assets/scripts/gold/build_satellites_characteristics.py` (vendored by pin, the registry pattern), `infra/aws/terraform/
cot-pipeline/satellites-characteristics-producer.tf` (role: GetObject `opal-data-cot/platinum/satellites/holdings.json`, GetObject
`opal-data-portal-v2/json/positioning/positioning_data.json`, GetObject `opal-data-etfs/bbg/*/characteristics.parquet`; PutObject
`opal-data-cot/platinum/satellites/characteristics.json` ONLY; **its OWN EventBridge cron offset after B2's 07:00Z (proposed 07:20Z),
never success-of-upstream**; the cross-firm deny mirrored; no ListBucket -- the as-of is resolved from the clock and the trading
calendar as the registry producer does), `lambda-source-map.json`, the ledger entry, deliverables. **Schema, fixed in the order:**
`{as_of, inputs: {holdings_as_of, positioning_data_as_of, bbg_as_of}, satellites: {<code>: {fee, yield, duration, beta, returns:
{...}, coverage: {weight_with_value, weight_null}}}}` -- weighted by `holdings.json` weights; a ticker with no characteristic in
either source contributes NULL and its weight to `weight_null`; **never renormalised**. **Bar:** the artifact published by its
scheduled fire; for Sat 15, `coverage.weight_null` >= GLD's 8.34 until the 2026-09-15 pull lands, and the value moves when it does
(the difference control: the same satellite before and after the input exists). never-widen: NON-APPLICATION stated in the COO
half (new key, zero writers); ledger + `safe-apply` + `comp-iam gaps` bind.

### `AT5-s-5` -- F1: the colour registry (C-COLOURS)
**Premise, measured at the pin:** `src/lib/chartColors.ts:113-120` `ASSET_CLASS` = {fixedIncome green500, equity blue500, cash
amber500, alternatives orange500, realEstate orange500, other gray500} -- no `structured`, no `commodities`; `:308` `'Commodities':
PALETTE.blue950` (a shade of equity blue); PALETTE carries `pink500 '#ec4899'` (`:61`) and `yellow500 '#eab308'` (`:78`) already.
**Write surface:** `portal/src/lib/chartColors.ts` ONLY. **Act:** `structured: PALETTE.pink500`; `commodities: PALETTE.yellow500`
(a NEW semantic token bound to the existing electric-yellow palette entry, **never amber**); `SUB_ASSET` gains `'Metals'` and
`'Hedge'` and `'Commodities'` leaves the blue family. **Bar:** the exclusivity check -- no PALETTE value keyed to two ratified
classes in `ASSET_CLASS` (the pre-existing `alternatives`/`realEstate` pair is a class and its sub-asset, disclosed, unchanged);
`tsc -b` (never `--noEmit` against the root, which typechecks zero files -- AMGT rd-8 AC2's vacuity); the token NAMES are the
contract F2 binds, so they are fixed HERE and inlined into F2's face.

### `AT5-s-6` -- F2: the Positioning page renders five classes (C-POSITIONING-ONLY)
**Premise, measured at the pin:** `tabs/HoldingsTab.tsx:215-219` `ASSET_CLASS_COLORS` three keys; `:1381-1383` folds Cash->Fixed
Income (KEEP: one ratified class) and Hedge->Equity (DROP); `:1392` `assetClassOrder = ['Fixed Income', 'Equity']`;
`panels/PositioningSummary.tsx:545-546` two hardcoded rows, `:627-651` the two-bucket fold (`equity + hedge`), `:704-712` and
`:840-884` a `{fixedIncome, equity}` render type; `shared/etfAdapter.ts:105` `ZERO_ALLOCATION` four legacy keys; the served allocation
after B1 carries `cash, fixed_income, equity, structured, commodities, alternatives`; **the `PositioningAllocation` type is defined
at `src/api/portal-proxy.ts:969`, OUTSIDE the 14 files** -- in this cell's grant by name. **Write surface:** `portal/src/pages/
Positioning/tabs/HoldingsTab.tsx`, `panels/PositioningSummary.tsx`, `shared/etfAdapter.ts`, `types.ts`, `portal/src/api/
portal-proxy.ts` (the type only). **NOT in this cell:** `shared/satelliteAdapter.ts` (F3 owns it whole, so the two write surfaces
do not intersect). **Bar:** five classes in the canonical order on the Models and ETFs modes, one colour each from F1's tokens, the
class subtotals summing to the total, `tsc -b` clean, a headless render READ (the frontend-dev loop) on the local build against the
served plane. Depends on F1's token names (inlined) and, for the served five-class keys, on B1 DEPLOYED at the bar.

### `AT5-s-7` -- F3: the Satellites mode reads `holdings.json` + characteristics; no computation in the adapter
**Premise, measured at the pin:** `shared/satelliteAdapter.ts` (306 lines) blends Yang's books: B) the holding-weight union `:53-56`,
A) the measures blend, `:133-159` allocation/delta over `PositioningAllocation`; `src/api/endpoints/satelliteRegistry.ts` exports
ONE endpoint `/api/scoped/satellites/registry.json` and `getSatelliteRegistry()` (throws on malformed/empty-as_of, no fallback
beneath it, @`24a8435642`); `SatelliteBook {code, displayName, constituents}` at `shared/satelliteSet.ts:74-78`. **Write surface:**
`portal/src/pages/Positioning/shared/satelliteAdapter.ts` (whole), `portal/src/api/endpoints/satelliteRegistry.ts` (+
`getSatelliteHoldings()`, `getSatelliteCharacteristics()` with the SAME throw-on-malformed contract and the same
`?firm=<slug>` rule), `portal/src/pages/Positioning/shared/satelliteSet.ts` (the served-holdings contract type beside
`SatelliteBook`, never a hand copy of membership). **Act:** the Satellites mode's holdings come from `holdings.json` rows (one total
per ticker, labels served); its measures come from `characteristics.json`; its as-of is `holdings.json`'s BD date; Models and ETFs
modes untouched; a NULL characteristic renders as the page already renders VXX's null yield. **Bar:** on the local build, Sat 15
shows GLD 8.34 in its own Commodities bucket (sub Metals after R1) and Sat 80 shows VXX 1.87 under Structured; nine satellites,
served rows == rendered rows. **Depends on:** B2 + B4 schemas (inlined), **B5 DEPLOYED for the fetch to succeed at the bar** (the
router admits ONE leaf today -- s.9 below), and F2 (the five-key type lands first).

### `AT5-s-8` -- R1: THE RETAG, last (C-RETAG-SET, C-SUB-ASSET, C-RETAG-SAFETY; round-4 analysis s.4 item 1)
**Premise, measured 2026-09-14 ~17:5xZ by a filtered scan (Count 12 of ScannedCount 285, no LastEvaluatedKey):**
```
ticker  asset_class    sub_asset_class   management_style   ->  TARGET asset_class / sub_asset_class
DBC     hedge          Commodities       passive                Commodities / Commodities (keeps)
GLD     hedge          Gold              passive                Commodities / Metals
GSG     hedge          Commodities       passive                Commodities / Commodities (keeps)
IAU     hedge          Gold              passive                Commodities / Metals
SLV     hedge          Silver            passive                Commodities / Metals
USO     hedge          Oil               passive                Commodities / Oil (keeps)
PDBC    equity         Commodities       active                 Commodities / Commodities (keeps)
VXX     equity         Volatility        passive                Structured  / Hedge
VIXY    hedge          Volatility        passive                Structured  / Hedge
UVXY    equity         Volatility        passive                Structured  / Hedge
QBER    fixed_income   Volatility        active                 Structured  / Hedge
VNQ     equity         US Large Cap      unknown                Alternatives / Real Estate   + management_style fixed
```
The served vocabulary today is FOUR values (`hedge`, `equity`, `fixed_income`, + `cash` elsewhere); `hedge` dissolves. **Write
surface:** the served DynamoDB `etf-classifications` table (12 rows, both levels, VNQ's `management_style`), `infra/aws/lambda/
v2_portal/_shared/etf_classification.py` (`ETF_CLASSIFICATIONS`, the same 12 rows), the deliverables dir. **Bar, one clause each:**
(i) the denominator is a STORE ENUMERATION -- every row of `etf-classifications` read, count printed (`C-S84`); (ii) each of the
twelve compared to ITS TARGET per level, never "one of the five" -- `bd-securities` carries ratified `alternatives` on ten of the
twelve, so a membership check passes on wrong rows (analysis s.4 item 1); (iii) the prior values above printed BEFORE the write and
restorable by the one script the order names; (iv) `seed-etf-classifications.py` dry run reports 0 conflicts after (both stores
agree) and B3's guarded seeder dry run reports 0 PRESERVED against a scratch copy; (v) VNQ's `management_style` no longer `unknown`
(the one member that arms `C-RETAG-SAFETY`, `C-S85`); (vi) the bar on the LOCAL BUILD (vite proxies `/api/*` to the TF-managed
distribution `EVTSA9VEHNZVH`, i.e. the served plane) over all NINE satellites and BOTH other modes: served labels == target per level,
weight unchanged per satellite (sum before == after), served rows == rendered rows, class subtotals == total; (vii) FWD-5 graded on
the retag itself: twelve rows changed in ONE place, every Positioning mode reflecting it with NO portal edit. **Depends on:** B1,
B2, B4, **B5** DEPLOYED; B3 landed; F1-F3 built and drained to the drain ref.

### `AT5-s-9` -- B5: the edge router admits the two new leaves (PROPOSED-PENDING-ANDREW)
**Premise, measured 2026-09-14 ~17:4xZ:** `infra/aws/lambda-edge/shared-advisor-router/index.mjs:95-101` defines
`SATELLITES_PREFIX "/api/scoped/satellites/"`, `SATELLITES_REGISTRY_LEAF "registry.json"`, ONE key; `:340-357` refuses every other
leaf with 404 `unknown_satellites_resource` **by design**; `:358` rewrites the one leaf. The response-side edge special-cases nothing
by leaf (`shared-advisor-router-response/index.mjs`, 4 hits, all comments on the registry's 403/404 contract). **So B2's and B4's
keys are unreachable by the page without this cell.** Deploy shape = the TO-7-AE precedent (`org/critical_paths/change_management/
20260828T0228Z_etfs-satellites-to7-ae-scoped-route-portal-auth_deploy.md`): `build-nodejs-lambda.sh portal-auth
shared-advisor-router` -> artifact `portal-auth/shared-advisor-router.zip` (current `content-sha256 qrL3PFqRnq5RUyQ4SDJvZQWDreLnl7rmNWZ25IF8cx0=`,
VersionId `N3w_OHAikHzTkuf.iIGPCXPM8_4ygJlL`, 2026-08-28T02:25:36Z) -> plan shows `aws_lambda_function.shared_advisor_router[0]` +
the distribution (its `qualified_arn` pin was dropped @`1fb2ad4abb`/`573690efd6`, so the association follows) -> `safe-apply` ->
0-diff re-plan -> the literal probe on the NEW artifact (`bun build` mangles identifiers, so LITERALS only, with the negative control
on the previous artifact). **Write surface:** `infra/aws/lambda-edge/shared-advisor-router/index.mjs` (a leaf allowlist
`{registry.json, holdings.json, characteristics.json} -> platinum/satellites/<leaf>`, same prefix, same bucket resolution, same firm
assertion, refusal branch KEPT for every other leaf; its gate script's test count grows and is printed), `infra/aws/terraform/
portal-auth/lambda-edge.tf` (no change expected -- `source_code_hash` reads the S3 object; stated if a change is needed), the ledger
entry, deliverables. **Bar:** an authenticated fetch of each of the three leaves returns the served bytes (ETag == the S3 object);
a fourth, unlisted leaf still returns the 404 with `rule: satellites_unknown_leaf` (the refusal branch survives); the previous edge
version's ARN printed as the rollback. never-widen: a second pair of halves (radius: the `/api/scoped/satellites/*` path class only).
**The freeze reading on an API-plane edge deploy is Andrew's, surfaced by `1.0.0_SA_CTO~Z` in the same card.**

## 4. DEPENDENCY EDGES -- keyed to OBSERVED completion, never to a message

```
AT5-s-5 (F1) -> AT5-s-6 (F2)          token names; F2 starts from the drain ref carrying F1
AT5-s-6 (F2) -> AT5-s-7 (F3)          the five-key PositioningAllocation type lands first; F3 starts from the ref carrying F2
AT5-s-2 (B2) -> AT5-s-4 (B4)          holdings.json schema + the served key B4 reads
AT5-s-2, AT5-s-4 -> AT5-s-7 (F3)      schemas inlined; served keys at the bar
AT5-s-9 (B5) -> AT5-s-7 (F3)          the fetch path (DEPLOYED)
AT5-s-1, AT5-s-2, AT5-s-4, AT5-s-9 (DEPLOYED), AT5-s-3 (landed), AT5-s-6, AT5-s-7 (built+drained) -> AT5-s-8 (R1)
```
**Why F1 -> F2 -> F3 is ONE chain, sequential, and not three parallel portal cells:** F2 and F3 both touch the
`PositioningAllocation` consumers, the submodule has ONE HEAD, and the round MUST land on ONE drain ref. Three clones committing in
parallel onto one ref is the append-only-shared-file inversion (CLAUDE.md 14b) moved into git: a guaranteed conflict at the drain
for a few minutes of parallelism. One slot, three orders, each starting from the ref the previous one landed on. Write surfaces are
DISJOINT by construction: F1 = `chartColors.ts`; F2 = HoldingsTab, PositioningSummary, etfAdapter, types, the type at portal-proxy;
F3 = satelliteAdapter (whole), satelliteRegistry, satelliteSet.

**Chains (maximal paths, dependency-independent at their roots):** `[s-1 -> s-8]`, `[s-2 -> s-4 -> s-7 -> s-8]`, `[s-3 -> s-8]`,
`[s-5 -> s-6 -> s-7 -> s-8]`, `[s-9 -> s-7 -> s-8]`. **M = 5 chains (4 if B5 is refused).** s-7 and s-8 sit on several chains; each
is queued on ONE slot and handed over only when EVERY upstream edge reads complete at HEAD (the drain, not a message, is the
observation).

**Waves (the fan-out L6 derives; max concurrency 5, default cap 8):**
```
wave 1   s-1 (B1)   s-2 (B2)   s-3 (B3)   s-5 (F1)   s-9 (B5)
wave 2   s-4 (B4)   s-6 (F2)
wave 3   s-7 (F3)
wave 4   s-8 (R1)   -- strictly last; a retag into a two-class page hides the row while its weight stays in the total
```
**Slots (`C-S113`, allocated from CURRENT ownership; `~1..~18` are consumed, `~15`/`~16` explicitly):** `~19` s-1 then s-8;
`~20` s-2 then s-4; `~21` s-3; `~22` s-5 then s-6 then s-7; `~23` s-9. `fanout: 5 of 5 chains, cap 8, reason: five
dependency-independent roots; the portal chain is deliberately serial on one slot` (4 of 4 without B5). Surprise rows mint
`POSN_ASTTAX-Z-W<slot>-S<k>` with the site-Z coordinate (`C-S96`). Every order declares its proof instance at the FULL order-file
stem (`C-S83`, `C-S87`); every order that depends on another cell's output reads that dependency back into its own face (`C-S112`).

## 5. WHAT THIS ROUND DELIBERATELY DOES NOT CUT

- **Attribution -- nothing.** F4 is OUT by Andrew's word; the consequence is accepted and no worker files it.
- **Card 4 (GLD/VXX into the Bloomberg pull)** landed as a CTO-gated seat act @`ac3e03a317`; B4 READS its output and does not touch it.
- **`is_hedge()` / `bd-securities` reconciliation** -- C-CUTS. Rows `Z-W1-S1`/`Z-C-S1` and `Z-W17-S3` are dispositioned at L4.
- **The portal promote, DEV/PROD push, the gitlink move** -- Andrew's separate word; C-DONE ends at "built and committed behind
  the freeze".
- **Any monitor, alarm or freshness checker** -- the standing moratorium; the CloudWatch log and each artifact's `as_of` are the record.
- **A same-day ad-hoc Bloomberg pull** -- open item H, Andrew's; B4 renders NULL for GLD/VXX characteristics until a pull lands.

## 6. THE BATTERY -- three mandatory lenses, each RUN or DECLARED, with its denominator or blindness

| lens | disposition | what it read (denominator) | what it cannot see (stated) |
|---|---|---|---|
| `comp-schedule --drift` | **RUN** 2026-09-14 ~17:4xZ | GATES ARMED 2 (G-3 owner CTO, an inf never-widen sentinel; G-7 owner POD4, the BD calendar guard) -- **neither is a POSN gate**; carriers C1 23 sentinel lines -> 7, C2 **7 open deploy-ledger entries** (one is `posn-bbg-etf-pull-gld-vxx`, card 4, L2 owed to the 2026-09-15 fire), C3 **12 standing NEVER clauses** (they bind B1/B2/B4/B5: no monitor, safe-apply only, never-widen, no shadow pipeline), C4 21 scope guards, C5 334 blocking fields (a reading list) | project `blocking` prose is not counted as a gate; C4 scope guards are listed, never graded discharged |
| `comp-iam service cot-satellites-registry-producer` | **RUN** | DESIRED plane only (474 .tf files, 404 policy blocks attached, 26 NOT ATTACHED, deny overlay 2 unparsed); result: **"No AWS operations detected"** | **BLIND BY CONSTRUCTION**: the producer logic is VENDORED from `data/assets/...` by pin, so the trigger carries no boto3 call site; B2's and B4's IAM are graded by `comp-iam gaps` AFTER their `.tf` exists, inside the cell, and by the live `simulate-principal-policy` at the deploy leg -- DESIRED != APPLIED != EXERCISED |
| `comp-iam service yang-generate-positioning` | **RUN** | 7 calls across 13 statements: 1 GRANTED, **6 UNRESOLVABLE-RESOURCE** (bucket/key are runtime args) | the resource check cannot resolve `args.bucket`; the role is `local.lambda_role_arn` shared across the yang pipeline; B1 changes no grant, so the blindness is disclosed rather than remedied here |
| `comp-adversary compose <this file>` | **RUN after this draft is written; its declaration is appended in s.8** | -- | -- |
| lenses not in the core | `comp-blast`, `comp-routes`, `comp-cache` (the COO minimum for a PRD decomposition) | **DECLARED-NOT-APPLICABLE at L5, RUN at the cut**: the routes lens is what found B5 (read manually at `index.mjs:340-358`); `comp-routes behaviors` is run against the `/api/scoped/satellites/*` behavior before B5's order is cut and its output inlined into that face | a neighbourhood lens that reads the filesystem around a cited path, not the dependency chain, states that blindness in the face |

## 7. Four-postulate record (Rule 24)

- **(i) MECE by SUBTRACTION over a declared domain.** Domain = the PRD v0.7 endpoint outcomes, denominator 6; every outcome is
  named by at least one cell above (FWD-1/2/5 by s-1, s-2, s-4, s-8; FWD-3/4 by s-5, s-6; FWD-6 by s-6, s-7, s-8);
  uncovered = 6 MINUS 6 = **{ }**. And the SECOND domain, the one the v0.6 qualifier demands: cells that SERVE rather than name --
  every cell here writes code, data, a deploy or a render that a bar reads; none is measurement-only. The breakdown's eight cells
  MINUS this decomposition's cells = { } ; this decomposition's cells MINUS the breakdown's = **{ AT5-s-9 }**, the one deviation,
  named and pending Andrew rather than folded in silently.
- **(ii) SAME GRAIN.** Every cell is one artifact with one owner-worker and one bar; deploy cells carry their deploy leg shape
  (build -> plan -> safe-apply -> 0-diff -> record -> served read); build cells carry `tsc -b` + a read render; the retag carries
  the store enumeration and the per-level target comparison.
- **(iii) INTENT COHERENCE.** One axis: take the Positioning page to C-DONE -- backend deployed, frontend built and committed
  behind the freeze, the retag last. Nothing here reconciles Yang's models to BD, touches Attribution, or adds a monitor.
- **(iv) STATE COHERENCE -- what no cell here moves:** the portal gitlink (`e85f6eb84f`), any DEV/PROD branch, Yang's PKL or the
  Models mode's data, `bd-securities`, the Attribution page, the Bloomberg pull's FUNDS list, any served key outside the six named
  (`positioning_data.json`, `allocation_summary.json`, `registry.json`, `holdings.json`, `characteristics.json`, the edge router's
  version). `holdings_attribution_data.json` is READ (its class values already come from the registry at `:585`) and not rewritten
  by this round; its next scheduled fire carries the retag through unchanged code.

## 8. comp-adversary declaration -- RUN 2026-09-14 ~18:0xZ on this draft

`comp-adversary compose org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md` (v1 contract). What the
validator of this decomposition WAS shown: 12 comp-read digests (python-ast x9, whole-file x2, UNDECLARED x1; 24,369 bytes) over the
cited neighbourhood, the comp-state drift excerpt (400 commits / 2837 records, estate-wide and not POSN-specific), the PRD rows
cited; **complement sources: 5 run / 0 deferred / 4 DECLARED-EXCLUDED** -- toolgraph SHARES_SUBSTRATE independence, comp-axes
unexamined axes, comp-blast/comp-trace neighbourhood expansion (the neighbourhood is the DECOMPOSITION graph, never a blast radius),
comp-pulse warnings / comp-cochange diversity. **Every pin in the declaration is READ-VINTAGE**; trace-to-authority claims are
unanswerable from it. What the declaration therefore does NOT certify, stated rather than implied: (1) that the reader set of
`chartColors.ts` beyond the 14 Positioning files is closed (out of scope by C-POSITIONING-ONLY, not by measurement); (2) that
`build_satellites_registry.py`'s sibling oracle survives a holdings extension unchanged -- the cell proves it; (3) that the edge
router's response side admits the new leaves -- read manually (4 comment hits, no leaf branch), proved at B5's bar; (4) the digest
of the vendored registry oracle was TRUNCATED at 2,400 of 2,508 bytes by the per-file cap, so its tail (`assert_no_drift`,
`drift_report`) was not shown to the validator and is read in the cell.
