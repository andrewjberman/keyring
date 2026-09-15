# POSN_ASTTAX -- L5 DECOMPOSITION (round 6) -- DRAFT, NOT CUT

**archetype:** IMPLEMENT (the Satellites mode completed: each holding's measures served and attached; only the classes a view holds; the summary's own date and copy)
**Owner (L5-L6):** `2.0.0_SA_COO~Z` - **Date:** 2026-09-15 ~03:2xZ - **Directive:** D4 - **Macro:** POSN - **Fabric:** site-z
**PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.10** @`59113e257a` (s.0 ADDENDUM v0.9: FWD-7 + C-HOLDING-MEASURES, C-PRESENT-CLASSES,
C-SUMMARY-COPY, C-B4-SCHEDULE; s.0 ADDENDUM v0.10: FWD-6 DONE WHEN = the presence rule, FWD-7's blank clause per measure, the GLD returns
rule and its landed backfill, the B6 import guidance, the BRIEF COVERAGE map), read in full at drafting and re-read at v0.10. **Gate at draft time:** `prd-signoff.py status POSN_ASTTAX` -> v0.10 @59113e257a
WITHHELD, both halves STALE and owed by the routed `~W` lanes (`3.0.0_SA_CVO~W` ratified-text, `4.0.0_SA_CRO~W` brief; msg 22980 --
the `~Z` lanes do not stamp). v0.10 adopts the two `~W` lane refusals (`3.0.0_SA_CVO~W` @27a54b7550: the provenance line leaves ENDPOINT, FWD-6's DONE WHEN carries the presence rule, FWD-7's
blank clause reconciled; `4.0.0_SA_CRO~W` @a397859526: a six-heading BRIEF COVERAGE map) and the Andrew-direct ~03:0xZ vendor
change (@365580f244: GLD/VXX Bloomberg return history BACKFILLED -- ledger `posn-bbg-gld-vxx-return-history-backfill` CLOSED @d3d2ffc4a5,
1429 rows each, 8 of 8 windows computed; B6 takes GLD's returns from the ETF gold returns rule, imported from its home). **Re-pinned to
v0.10 ~03:3xZ; the three cells are unchanged in shape (22970, 22980).**
**Answers:** `1.0.0_SA_CTO~Z`'s round-5 analysis `ledger/ROUND_ANALYSIS.round5.md` @`8eabf98d81`, which answers `3.0.0_SA_CVO~Z`'s
round-5 slug `surprise-channel/remediations/REMEDIATION_v5.Z.md` @`1edf35dbc3` (L9 `ADJUDICATION_v7.Z.md`, C-S142/C-S143/C-S144).
**Andrew's word for the round:** ~02:1xZ (@65410eedaf) and ~02:3xZ (@0553548fe2, *"just fix it completely, we're not waiting for the
next day"*). C-DONE binds as in round 5: backend deployed and driven; frontend built and committed behind the freeze; no promote,
no DEV/PROD push, no gitlink move.

> **STATUS OF THIS FILE: THREE CELLS, PINNED TO v0.10 @59113e257a, HELD FOR ITS TWO SIGNED HALVES (LIMB 6).** The cut is ONE issuance
> (`TO-W1-1` B6, `TO-W2-1` F4, `TO-W3-1` F5) the moment `prd-signoff.py status` reads both halves SIGNED at v0.10's bytes.

---

## 0. WHY THIS ROUND EXISTS -- the subtraction, re-read at source (the CTO's s.1, re-run by this seat at the cut)

```
DENOMINATOR   28 task orders under POSN_ASTTAX (24 complete, 2 superseded, 2 cancelled; 0 open at HEAD e53147ebe0)
DECLARED       7 (FWD-1..FWD-7, v0.9 header endpoint_outcomes)
COVERED        6 (FWD-1..FWD-6 each named by >= 1 order)
UNCOVERED = declared MINUS covered = { FWD-7 }     <- appended at v0.9; B6 and F4 name it
REALIZED       0 of 7 (the freeze is Andrew's expressly qualified wait for FWD-3/4/6; FWD-1/2/5 realized on the Yang plane and,
               since R2 03:02Z, on the Satellites plane too -- graded at L9, not here)
```
Round 5 built and deployed its nine cells; Andrew then read the page and ruled three things round 5 never specified (analysis s.0).
Round 6 serves them: the per-holding measures (FWD-7), the presence rule (C-PRESENT-CLASSES, graded into FWD-6), the summary's own
copy and date (C-SUMMARY-COPY), and B4's schedule after its input (C-B4-SCHEDULE).

## 1. THE CONSTRAINTS THAT SHAPE EVERY CELL -- from PRD v0.9 s.0, stated first

- **C-HOLDING-MEASURES** (FWD-7; disarm route for `Z-S132`, `C-S144`) -- B4's `characteristics.json` ALSO publishes, once per artifact,
  a `tickers` block keyed by ticker for every ticker any satellite holds: `fee, aum, active, yield, duration, credit, beta, returns,
  source`. Precedence is B4's existing per-ticker rule, unchanged (Yang's `current_holdings` row, else the Bloomberg partition, else
  none). Every existing field of the artifact is unchanged for the same inputs. The adapter attaches each row's served values to that
  row -- no arithmetic, no borrowing. Measured basis (the CTO, ~02:5xZ): 25 distinct tickers; 23 priced by Yang; GLD by Bloomberg only;
  CASH by neither; on the 5 shared tickers Yang's `aum` == `FUND_TOTAL_ASSETS` and `fee` == `FUND_EXPENSE_RATIO` (5 of 5), so the
  Bloomberg fallback maps `aum <- FUND_TOTAL_ASSETS` in the same unit; `active`/`credit` NULL for a Bloomberg-sourced ticker.
  **v0.10 @59113e257a:** GLD's returns come from the estate's ONE returns rule, `etf_positioning_gold.compute_returns` over
  `load_history` (daily `history_topup` partitions + the `bbg-testpull/tickers/{TICKER}/history.csv` backfill, LANDED for GLD and VXX
  @d3d2ffc4a5); the method difference from Yang's windows (start-inclusive, 1Q 91 vs 90 days) is disclosed in the PRD, not reconciled in
  code; the producer IMPORTS the two functions from their home and packages that module at its mirrored path.
- **C-PRESENT-CLASSES** (FWD-3, FWD-6; disarm route for `Z-S118`, `Z-S131`, `C-S142`) -- ONE presence set per render: the classes with a
  non-zero value in ANY column the current view draws; legend, Asset Class rows and the section count list exactly that set, in
  `ASSET_CLASSES` order and colours (keyed by class name, so hiding a class shifts no colour -- msg 22957 compatible). Per mode,
  never across modes. The zero-row design comment goes with the behaviour.
- **C-SUMMARY-COPY** (FWD-6; disarm route for `Z-S115`, `Z-S117`, `Z-S119`, `C-S143`) -- the third percent label rounds like its
  siblings; the Satellites mode's footer names `holdings.json`'s `as_of` and Black Diamond; the Satellites subtitle and the unresolved
  notice stop describing the removed blend. Models and ETFs copy unchanged.
- **C-B4-SCHEDULE** (FWD-7 on schedule; disarm route for `Z-S120`, `Z-S130`) -- `cron(30 12 * * ? *)` UTC, after the 07:00
  America/New_York pull in both DST states; never success-of-upstream; the deploy is followed by a DRIVEN run with an explicit
  `bbg_as_of` under its own never-widen halves; the scheduled fire is the organic leg.
- **Carried from v0.6-v0.8, still binding:** C-POSITIONING-ONLY (Attribution untouched), C-SATELLITE-SOURCE (one BD total per ticker;
  never renormalised; NULL disclosed), C-SUB-ASSET, C-COLOURS, the freeze (source writes YES on ONE drain ref; gitlink NO; promote NO).
- **The two lane refusals v0.10 adopts change NO cell shape** (22970, 22980): ENDPOINT loses a provenance line; FWD-6's DONE WHEN is
  the presence rule ("a mode shows a class only when a book in its view holds some of it"); FWD-7's blank clause is per measure ("a cell
  blank only where no source carries that measure for that holding"); the brief half gains the six-heading coverage map.
- **The issuer's ONE reading beyond the CTO's file list, recorded as row `Z-S136`:** C-SUMMARY-COPY's plain text ("the Satellites
  mode's footer") reaches the Holdings panels' two footers and two headers in that mode (`HoldingsTab.tsx:1085-1087, :1162, :1169-1171,
  :1811`, all on the models PKL clock); F4 owns that file and carries it (W2-AC8); Models and ETFs byte-identical. The CTO's L10 lists
  the Summary's footer only; the row is the carrier for the CTO to hold the narrower reading at L10, and the change stays either way.

## 2. THE RECTANGLE -- surfaces x cells, status vocabulary {NOT_EVALUATED, CUT, ISSUED, TERMINAL}

S1 the characteristics producer (FWD-7, C-B4-SCHEDULE); S3 the Positioning page's Satellites mode (FWD-7 attach, FWD-6 copy) and
its Positioning Summary across modes (C-PRESENT-CLASSES).

| cell | breakdown | serves (surface -> outcomes) | status | placement |
|---|---|---|---|---|
| `AT6-s-1` | **B6** the per-ticker block + the schedule | S1 -> FWD-7 (served), C-B4-SCHEDULE | DRAFTED | `TO-W1-1`, slot `~24`, wave 1 |
| `AT6-s-2` | **F4** the adapter attaches the served values | S3 -> FWD-7 (rendered) | DRAFTED | `TO-W2-1`, slot `~25`, wave 2 (after B6 DEPLOYED and served) |
| `AT6-s-3` | **F5** presence filter, rounding, footer, copy | S3 -> FWD-6 (through C-PRESENT-CLASSES, C-SUMMARY-COPY), FWD-3 | DRAFTED | `TO-W3-1`, slot `~26`, wave 1 |

## 3. THE CELLS -- what each settles, its write surface, its measured premise

### `AT6-s-1` -- B6: `characteristics.json` gains the `tickers` block; the rule moves to `cron(30 12 * * ? *)`; deployed, then DRIVEN

**Premise, measured at HEAD (this seat, ~03:1xZ):** `data/assets/scripts/gold/build_satellites_characteristics.py` (499 lines):
`build()` :355-405 is PURE (docstring :357-362, the V4-AC4 difference control ran it twice); `resolve_ticker` :270-282 is the
per-ticker precedence (Yang row -> `positioning_data`; else bbg -> `bbg`; else `{}`, `none`), called once per holding at
`aggregate_satellite` :305; `yang_index` :204-232 captures ONLY `SCALAR_FIELDS` (:113 `fee, yield, duration, beta`) and `returns`
(:225-226) from a Yang `current_holdings` row -- **it drops `aum`, `active`, `credit`, which the row carries**
(`portal/src/api/portal-proxy.ts:1078-1084` at `dd1d33c6db`: `fee, aum (millions), active (0|1), yield, duration, credit, beta`);
`bbg_index` :234-257 maps `BBG_SCALAR_COLUMNS` :117-122 (`fee<-FUND_EXPENSE_RATIO, yield<-EQY_DVD_YLD_IND_NET,
duration<-HB_OAS_EFF_DURTN, beta<-BETA_ADJ_OVERRIDABLE`) and `BBG_RETURN_COLUMNS = {}` :125 (the pull carries no return column,
docstring :54-64); the artifact envelope :373-405 (`schema_version` 1 :110; `inputs` :377-386; `method` :387-399 incl.
`bbg_return_columns`, `return_windows`; `satellites` :404 -- per-satellite block :334-352 with `coverage`, `sources`, `contributors`);
`publish` :429-434 -> `opal-data-cot / platinum/satellites/characteristics.json` after `validate` :408-427 passes; `main` :452-495
takes `--as-of`, `--bbg-as-of`, `--dry-run`, `--out`; `resolve_bbg_as_of` :440-449 = `prev_trading_day(today)`. The handler
`infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py:72-96` forwards exactly two event keys:
`dry_run` (:80) and `bbg_as_of` (:82-83). `build_package.py` pins members by `--pin` (required, immutable; :105-136) at the
repo-mirroring layout (:93-102: `lambda_function.py`, the producer, `lib/trading_calendar.py`; BUILD_MANIFEST in-zip :199-201 and a
sidecar :207-213). Terraform `infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf`: rule :272-277
`cron(20 7 * * ? *)` ENABLED; target :279-283; permission :285-291; module :222-243 (`../modules/yang-lambda`, 512 MB, 120 s, layer
`pandas-pyarrow-requests-layer:1`); the module reads `s3_object_version` and `metadata["content-sha256"]` off the uploaded artifact
(`modules/yang-lambda/main.tf:17-20, :36-39` -- upload BEFORE plan); IAM policy :95-150 with Sids `ReadSatellitesHoldings` :103,
`ReadServedPositioningData` :109, `ReadBloombergEtfDaily` :119, `WriteSatellitesCharacteristics` :132; cross-firm deny :152-170.
**The returns rule (v0.10):** `data/etfs/scripts/gold/etf_positioning_gold.py` `load_history(as_of, bucket)` :731-830 (every
`bbg/<date>/history_topup.parquet` within `HISTORY_LOOKBACK_DAYS` 400 :320, listed by `list_objects_v2` on `bbg/` :746, plus the
backfill `_load_backfill_history` :675-729 listing `bbg-testpull/tickers/` :690-693 and reading each `history.csv`), then
`compute_returns(tkr, as_of, hist)` :855-921 over `RETURN_WINDOWS` :319 (`1D WTD MTD 1M QTD 1Q YTD 1Y`; frontier ON as_of, start
coverage, a NaN disqualifies). The module is import-safe for packaging: no module-level client (`_s3()` :361 is lazy), `sys.path`
inserts :77-78 resolve under the mirrored layout and the layer, stdlib + boto3 + pandas (:60). The served key today: VersionId
`rt61ogajZQy79meUlsY1X_mIdPngxJTZ` (2026-09-14T21:45:13Z, 54825 B), N = 1 writer.

**Write surface:** `data/assets/scripts/gold/build_satellites_characteristics.py`; the producer's `lambda_function.py` and
`build_package.py` (the new member `data/etfs/scripts/gold/etf_positioning_gold.py` at its repo path); the `.tf` (the rule's cron; the
IAM policy gains `s3:ListBucket` on `opal-data-etfs` conditioned to prefixes `bbg/` and `bbg-testpull/tickers/`, and `s3:GetObject` on
`bbg/*/history_topup.parquet` and `bbg-testpull/tickers/*/history.csv`; NO new write grant; the deny stays); `CHANGELOG.json`;
`lambda-source-map.json`; the ledger; deliverables `~24/`. **`etf_positioning_gold.py` is READ by pin, never edited** (its lane is ETFS).

**Schema, fixed in the order (additive; `schema_version` stays 1):** `tickers: {<TICKER>: {fee, aum, active, yield, duration,
credit, beta, returns: {<window>: value|null}, source: positioning_data|bbg|none}}` -- every ticker any satellite holds, ONCE; a Yang
row supplies all seven scalars and its `returns` verbatim; a bbg row supplies `fee, yield, duration, beta` from `BBG_SCALAR_COLUMNS`,
`aum` from `FUND_TOTAL_ASSETS`, `active`/`credit` NULL, and `returns` from `compute_returns(ticker, bbg_as_of, load_history(bbg_as_of))`
(NULL per window where the rule returns None); `none` -> all NULL. Provenance under ONE new key `method.tickers_block` (`bbg_aum_column`,
`returns_rule`, `returns_as_of`, `history_partitions_read`, `backfill_tickers_read`). **Nothing else in the artifact changes.**

**Bar (the discriminators):** (1) purity -- HEAD's module and the cell's module run `build()` over the SAME inputs; the outputs minus
`tickers` and `method.tickers_block` parse IDENTICAL (the difference control, both arms printed); (2) the local dry run prints the
tickers block: 25 tickers each once; sources 23 / 1 / 1; the five shared tickers' `aum` equal between sources 5 of 5; GLD `active` and
`credit` NULL; GLD `returns` per window -- computed where the backfill and the `bbg_as_of` frontier exist at the run, else NULL with the
rule's reason (frontier absent / start coverage) printed -- BOTH branches are the measured act; (3) deploy: `commit-gate`, `build_package
--pin <COMMITTED_HASH>`, `s3api put-object` with `content-sha256` metadata read back, `comp-iam gaps`, targeted plan (the module, the
policy, the rule) N change / 0 add / 0 destroy, `safe-apply`, unscoped 0-diff; (4) DRIVEN: `lambda invoke --payload '{"bbg_as_of":
"<NEWEST_BBG_PARTITION>"}'` (the newest `bbg/<date>/characteristics.parquet` present at the run, listed and printed) -> `characteristics.json`
VersionId moved, the served `tickers` block equals the dry run's over the same inputs, the `satellites` block equals the pre-deploy served
block when the `inputs` triple is unchanged (else the dry-run arm at the same inputs); (5) `describe-rule` -> `cron(30 12 * * ? *)`
ENABLED, the target the function; L8 = its first fire (2026-09-15 12:30Z) recorded by the COO, not waited on; (6) the record.
**never-widen:** BOTH halves cited by path -- `ledger/NEVER_WIDEN_ROUND6_COO_HALF.md` (this seat, drafted with this file) and
`ledger/NEVER_WIDEN_ROUND6_CTO_HALF.md` (owed by `1.0.0_SA_CTO~Z`); the worker REFUSES the deploy leg without both at HEAD.

### `AT6-s-2` -- F4: the Satellites adapter attaches each row's served values; NO arithmetic

**Premise, measured at `dd1d33c6db` (worktree `C:/tmp/portal-posn-view`):** the Holdings Breakdown row type is `CurrentHolding`
(`src/api/portal-proxy.ts:1062-1109`: `fee?, aum? (millions), active? (0|1), yield?, duration?, credit?, beta?, returns?{1D..SI}`);
the Satellites adapter's row literal `src/pages/Positioning/shared/satelliteAdapter.ts:262-282` carries EXACTLY FIVE keys (`ticker,
name, asset_class, sub_asset_class, weight`) -- every measure OMITTED; the book-level `characteristics` :314-320 IS served. The
table `src/pages/Positioning/tabs/HoldingsTab.tsx:1166-1812` draws 7 characteristic columns for satellites (`CHARACTERISTIC_FIELDS
.satellites = {fee, duration, credit}` at `shared/bookSet.ts:447-456`) and 8 performance windows; a missing scalar renders `-`
(:1551, :1557, :1569, :1576, :1583, :1590), a missing return renders an em dash (:1604), and a missing `active` renders **"NO"**
(:1561-1565) -- indistinguishable from a measured 0, which FWD-7's ACCEPT ("blank only where nothing prices that holding") forbids.
The read `src/api/endpoints/satelliteRegistry.ts:232-269` joins the three artifacts; `SatelliteCharacteristicsResponse` :168
carries no `tickers`; the contract types live in `shared/satelliteSet.ts` (:142-184).

**Write surface (DISJOINT from F5 by file):** `satelliteAdapter.ts` (the row literal attaches `served.characteristics.tickers[ticker]`
pass-through: `fee, aum, active, yield, duration, credit, beta, returns`, a non-finite or null served value -> `undefined`, unit as
served, NO arithmetic), `satelliteSet.ts` (the served `tickers` type), `satelliteRegistry.ts` (the response type), `HoldingsTab.tsx`
for the Active hunk at :1561-1565 (an `active` of null/undefined renders blank; `1` YES; `0` NO -- Models rows always carry 0|1,
unchanged) and the four Satellites-mode footer/header hunks (:1085-1087, :1162, :1169-1171, :1811 -- the mode's own clock, `Z-S136`).
**Bar:** `tsc -b` with a positive control; `diff --stat` exactly the four files; the render on fixtures built from the SERVED bytes
AFTER B6 (VersionIds printed; `--click 'Satellites'` then the satellite picked); the Holdings panels' footers and headers in the
Satellites mode read Black Diamond and `holdings.json`'s `as_of` (W2-AC8, the `Z-S136` reading), Models unchanged: for Opal Satellite 15 and 80, every Holdings Breakdown
row's 7 characteristic cells and 8 performance cells EQUAL the served `tickers` values under the renderer's own formatting (served vs
rendered printed per cell), CASH blank throughout, a NULL blank (never `NO`, never a raw float), GLD's returns blank iff served NULL;
the DISCRIMINATING PAIR: the same fixtures with the `tickers` block removed render the pre-F4 cells (`-`), so the equality is the
attachment and not the renderer's default. **Depends on B6 DEPLOYED AND SERVED** (read back at the bar, never assumed).

### `AT6-s-3` -- F5: one presence set per render; the label rounds; the Satellites footer, subtitle and notice are the mode's own

**Premise, measured at `dd1d33c6db`:** `src/pages/Positioning/panels/PositioningSummary.tsx` (1385 lines): `ASSET_CLASSES` :79-92
(five entries, `color: ASSET_CLASS.<key>` from `src/lib/chartColors.ts:115-126`, keyed by class name); enumeration sites -- rows
:578-582 (the zero-row comment :575-577), section count :850, bars :925-976, labels :988-1010, legend :1159-1170, the N/A rows :252;
the drawn columns -- `books` :627-629 (`resolveBooks`), portfolio values `getAllocationData` :660-681, benchmark :669, relative
:672-676, custom :230-242 (`'--'` on an invalid blend), gated by `caps` :623 and `viewSupported` :697-699; the raw label :1011
`{data[c.key]}%` beside :1004 `toFixed(1)` (relative, signed) and :989/:994 `Math.round` (the Custom pair); the footer :1382
`<SmartPanelFooter sourceKey="model_pkl" content="Source: Bloomberg." />` HARDCODED for every mode (the models PKL clock beside Black
Diamond numbers). `src/pages/Positioning/Positioning.tsx` (645 lines): `MODE_DESCRIPTIONS.satellites` :123-125 ("...each a weighted
blend of Opal model portfolios"); the unresolved notice :616-622 ("...blended over their remaining legs only"); the `models-unavailable`
notice copy :219-221 ("blended from") -- a third string describing the retired blend, in the same file, same defect; `dataAsOf` :481 =
`data_as_of` = `holdings_as_of` (satelliteAdapter.ts:336, :366-369); `REGISTERS_YANG_AS_OF.satellites = false` :491-495.

**Write surface (DISJOINT from F4 by file):** `PositioningSummary.tsx`, `Positioning.tsx`. **The presence set:** one pure helper,
exported, computed once per render from every column the current view draws (the `books` portfolio values; the benchmark values when
the Benchmark or Relative view is on; the custom column when the blend is valid), applied to the legend, the Asset Class rows, the
section count and the bars; `ASSET_CLASSES` order and colours untouched; sub-category rows untouched; the comment :575-577 removed.
**The label:** :1011 renders `Math.round(v)%` like the Custom pair (the issuer's reading of "like its two siblings": the single-bar
labels; the relative delta keeps its signed `toFixed(1)`) -- a worker who reads the constraint otherwise files a row, never a second
reading in code. **The footer:** in the Satellites mode `Source: Black Diamond, holdings as of <data_as_of>` with no manifest key
(`SmartPanelFooter.tsx:49-84` read for the props); Models and ETFs unchanged. **The copy:** the subtitle names Black Diamond
holdings, not a blend; the unresolved notice names a satellite with no served holdings; the models-unavailable notice likewise.
**Bar:** `tsc -b`; `diff --stat` exactly two files; the presence helper exercised by a node script over a constructed column set (a
class present only in the benchmark column is present; a class zero in every column is absent) -- a unit control on a pure
function, not a render fixture; the render on fixtures from the SERVED bytes (post-R2 `holdings.json` VersionId
`67GP52SdV1rw6QFVNPytU6ec4TvhwJh3`): Models lists 3 classes (Fixed Income, Equity, Structured) in the legend and the rows with the
section count `(3)`; Satellites lists 4 (Fixed Income, Equity, Structured, Commodities); ETFs printed (no class outside the five,
no zero row); the TEXT dump carries no label matching `[0-9]+\.[0-9]{2,}%`; the Satellites footer text carries `Black Diamond` and
`2026-09-14`; the subtitle and notices carry no `blend`. **Runs in parallel with B6 and F4** (disjoint files; the drain merges).

## 4. DEPENDENCY EDGES -- keyed to OBSERVED completion, never to a message

```
AT6-s-1 (B6, DEPLOYED and served) -> AT6-s-2 (F4)     the served tickers block is what F4 attaches and what its bar reads
AT6-s-3 (F5)                                          no upstream inside the round (reads the served keys as they are after R2)
```
**Chains (maximal paths, dependency-independent at their roots):** `[s-1 -> s-2]`, `[s-3]`. **M = 2.**
**Waves:** wave 1 `s-1 (B6)` + `s-3 (F5)`; wave 2 `s-2 (F4)` after `TO-W1-1` reads `complete` at HEAD AND `characteristics.json`'s served
bytes carry `tickers` (read back). **Slots (from current ownership, `~1..~23` consumed):** `~24` s-1; `~25` s-2; `~26` s-3.
`fanout: 2 of 2 chains, cap 8, reason: two dependency-independent roots; F4 and F5 are disjoint files on one drain ref and run in
parallel, merged at the drain`. **The portal ref:** `refs/drains/posn-6-portal` cut from `refs/drains/posn-5-portal` = `dd1d33c6db` at
hand-over and recorded in `ledger/PORTAL_REFS.md` at the first commit; branches `wk-posn-6-25-portal` (F4) and `wk-posn-6-26-portal`
(F5) each cut FROM the ref; the COO drains each by merge into the ref's worktree (disjoint files -> no conflict; a conflict is STOP and
a row); the gitlink `e85f6eb84f` does not move. Surprise rows mint `POSN_ASTTAX-Z-W<slot>-S<k>`; every order declares its proof instance
at the FULL order-file stem; F4 reads B6's served output back into its own face.

## 5. WHAT THIS ROUND DELIBERATELY DOES NOT CUT

- **The Bloomberg return-history backfill for GLD/VXX** -- a CTO-driven vendor act under its own ledger (Andrew ~03:0xZ @365580f244).
  B6 READS its output through the loader that already reads that contract; B6 does not land it and does not wait for it: the bar's
  returns clause carries both branches.
- **A second yellow for Metals** (`C-S139`), the MFA-capable authenticated probe (`C-S135`), the recorder's device defects (`C-S136`),
  the seeder docstring (`C-S138`) -- graduated by L9 to their owners, not round-6 cells.
- **The portal promote, DEV/PROD push, the gitlink move** -- Andrew's separate word. **Any monitor or alarm** -- the moratorium.
- **Attribution** -- C-POSITIONING-ONLY.

## 6. THE BATTERY -- three mandatory lenses, each RUN or DECLARED, with its denominator or blindness

| lens | disposition | what it read (denominator) | what it cannot see (stated) |
|---|---|---|---|
| `comp-schedule --drift` | RUN 2026-09-15 ~03:2xZ (output inlined at the cut, s.8) | the armed gates and the open deploy ledgers; `posn-round5-b4-satellites-characteristics` is OPEN at L8 by design (its organic arm), `posn-round5-b2-...` CLOSED 03:1xZ, `posn-bbg-etf-pull-gld-vxx` L2 owed to the 07:00 ET fire | project `blocking` prose is not a gate |
| `comp-iam service cot-satellites-characteristics-producer` | RUN (s.8) | the DESIRED plane; the producer's boto3 calls are VENDORED by pin so the trigger carries no call site | BLIND BY CONSTRUCTION -- B6's grant is graded by `comp-iam gaps` on the `.tf` inside the cell and by the live apply |
| `comp-adversary compose <this file>` | RUN after this draft (s.8) | -- | -- |
| reader census of `platinum/satellites/characteristics.json` | RUN (s.8) | every file naming the key -- the consumers of the changed artifact | a consumer that builds the key from parts |
| `comp-blast`, `comp-routes`, `comp-cache` | DECLARED-NOT-APPLICABLE at L5 | no new route (B5's `/api/scoped/satellites/*` already admits the leaf; the edge caches it under `opal-scoped-advisor-by-firm`, DefaultTTL 60 s -- stated in F4's face) | -- |

## 7. Four-postulate record (Rule 24)

(i) MECE over the declared domain: the domain is v0.9's four new constraints + FWD-7; the census by subtraction -- {C-HOLDING-MEASURES,
C-PRESENT-CLASSES, C-SUMMARY-COPY, C-B4-SCHEDULE, FWD-7} MINUS {served by s-1: C-HOLDING-MEASURES (the block), C-B4-SCHEDULE, FWD-7
(served)} MINUS {served by s-2: FWD-7 (rendered), C-HOLDING-MEASURES (the attach)} MINUS {served by s-3: C-PRESENT-CLASSES,
C-SUMMARY-COPY} = {} -- every member consumed, none twice at the same grain. (ii) SAME GRAIN: cells are write surfaces; s-2 and s-3
share a repo and a ref but no file. (iii) INTENT COHERENCE: one axis -- "the Satellites mode complete", per Andrew ~02:3xZ.
(iv) STATE COHERENCE: what no cell moves -- the gitlink, the promote, Attribution, the ETF publisher, the Yang pipeline, the Bloomberg
pull's own code, `registry.json` / `holdings.json` (READ by B6, never written).

## 8. Lens outputs and the comp-adversary declaration -- RUN 2026-09-15 ~03:2xZ on this draft

- `comp-schedule --drift`: WITHIN BUDGET, 5 of 5 carriers (C1=23 sentinel lines -> 7 gates; C2=9 open deploy ledgers -- among them
  `posn-round5-b4-satellites-characteristics` OPEN at L8 by design (superseded by B6's rescheduled first fire, closed in W1-AC14) and
  `posn-bbg-etf-pull-gld-vxx` L2 owed to the 07:00 ET fire; `posn-round5-b2-satellites-holdings` CLOSED 03:1xZ; C3=12 standing NEVER
  clauses; C4=21 scope guards; C5=334 blocking fields, a reading list). GATES ARMED 2 (G-3 CTO, G-7 POD4) -- neither is a POSN gate.
- `comp-iam service cot-satellites-characteristics-producer`: "No AWS operations detected" -- BLIND BY CONSTRUCTION (the producer's calls
  are vendored by pin; the trigger carries no call site); DENY-OVERLAY INCOMPLETE (2 for_each deny statements unparsed) -- silence is not
  allowed; B6's grant is graded by `comp-iam gaps` on the `.tf` (W1-AC8) and by the live apply (W1-AC10).
- reader census `comp-find 'satellites/characteristics\.json' --files`: hits in this project's orders, deliverables and docs only, plus
  the producer script and its `.tf` (the writer); the portal consumer lives in the submodule at `dd1d33c6db`
  (`satelliteRegistry.ts:107`) -- outside the workspace corpus, named here by hand. No second producer names the key.
- `comp-adversary compose <this file>`: 5 complement sources run / 0 deferred / 4 declared-excluded (toolgraph independence, comp-axes
  rows, code-graph blast expansion, comp-pulse -- v1 contract); 12 digests (python-ast); the NOT-covered items each cell's `<preflight>`
  states are this seat's own, not the tool's.
