# ANDREW-DIRECT 2026-08-24 -- NO BQL. Wire the issuer channels. HANDOFF BRIEF -> `1.0.0_SA_CTO~Z`

**From:** `0.0.0_AB_MSTR~Z` (site Z) · **To:** `1.0.0_SA_CTO~Z` · **Authority:** Andrew-direct, this terminal.
**This is the kickoff record for the PRD round.** CTO~Z drafts the PRD + registers the project;
MSTR~Z reads it back against these goals; then COO~Z and the executing seats spawn.

---

## 1. THE RULING, VERBATIM

> *"No we're not doing BQL which means we have to wire up the rest and just work to design the
> structure in a manner that renders a consistent output shape. All that work needs to be managed
> in the opal-data-etfs bucket. I want you to hand this off to CTO~Z and have them draft PRDs and
> register the project to do so in line with the directives.yaml and your knowledge on what needs
> to be accomplished here. When they are done with their PRD, you need to read it and make sure
> its accurate to the relevant goals. At that point, we can have COO~Z and the relevant agents and
> ~Z spawned to take this project through completion. The premise is that it should cover all
> ingestion and pipeline mechanics, threading it all the way to the frontend daily publish."*

**THE BQL OPTION IS CLOSED.** Do not re-propose it, do not design a "when we get BQL" branch as a
live path, and do not leave a dormant BQL leg in the build. The one thing that survives is the
**honest per-run refusal record** already in `etf_constituents_pull.py` leg 1b -- keep it as
evidence, not as a waiting room.

---

## 2. THE FOUR MEASURED FACTS THE DESIGN RESTS ON

Every one re-derivable; each names its control.

1. **Bloomberg SERVES a derived layer today, no entitlement needed.** Plain `ReferenceDataRequest`
   on the ETF ticker: `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT`, `FUND_PCT_TOP_TEN_HOLD`,
   `HB_INDUSTRY_SECTOR_ALLOCATION` (GICS-style sector weights), `HB_GEO_CNTRY_ALLOC`.
   Measured 2026-08-24 for all four funds, SPY as in-request control. **Landing already live** at
   `s3://opal-data-etfs/bbg/{as-of}/constituents/`.
2. **Bloomberg will NOT enumerate constituents without BQL, and there is no other Bloomberg route.**
   Field-dictionary census: the only constituent-enumerating family is `INDX_*`, which serves an
   INDEX. **All four funds are `ACTIVELY_MANAGED = Y` with no underlying index** (SPY control:
   `N` / `SPXT`). `FUND_BENCHMARK_PRIM` is a BENCHMARK, not a portfolio (PFDE/PFOE -> `SPX`).
3. **THE DERIVED LAYER IS CURRENT-DAY-ONLY.** `HistoricalDataRequest` returns ZERO rows for those
   fields while `PX_LAST` returns a full series in the SAME call. **No backfill exists or ever will.
   Every uncaptured day is permanently lost.** This is the only clock in the project.
4. **Both issuers publish a DAILY holdings CSV.** Measured 2026-08-24, HTTP 200, dated same-day.

---

## 3. THE TWO ISSUER CHANNELS -- current state, and they are NOT symmetric

| | Pathfinder (PFDE, PFOE) | TrueShares (DIVZ, IDVZ) |
|---|---|---|
| source | `pathfinderetfs.com` filepoint | Google Sheets export, linked from the fund page |
| raw lands today | `s3://opal-data-assets/pathfinder/filepoint/bronze/holdings/{YYYYMMDD}/ETF_Holdings.csv` | **nothing -- holdings are NOT captured** |
| what IS captured | holdings + dailynav | `trueshares/{DIVZ,IDVZ}/bronze/netassets/` -- **netassets only** |
| reaches silver | YES -- `opal-data-etfs/silver/holdings/` | **NO** |
| built? | YES, daily ~18:00 | **NO -- this is the gap** |

**TrueShares daily holdings CSV (verified 2026-08-24, HTTP 200, dated same day):**
```
DIVZ  https://docs.google.com/spreadsheets/export?id=1csUjnC2fHqZQORGBccRy_ew0dgv-jpC_LOKdbjPwI9U&exportFormat=csv
IDVZ  https://docs.google.com/spreadsheets/export?id=1H8LXhhQBSbQLK37-y5TPTvJsaeKfE2HVmVcRVpQHKh8&exportFormat=csv
```
Schema: `Date, Account, Stock Ticker, CUSIP, Security Name, Shares, Price, Market Value, Weightings,
Net Assets` -- **identical to the repo's 2026-07-31 oracle CSVs**, which is where those came from.
DIVZ 29 rows / weights 99.80; IDVZ 44 rows / 99.51; both carry a `SALXX` cash line.

⚠ **THE LINK IS INJECTED CLIENT-SIDE.** A `curl` of the fund page HTML does NOT contain it; it
appears only once the page is RENDERED. Any fetcher must either hit the export URL directly (they
appear stable per fund) or render. **Do not design a fetcher that greps the saved HTML** -- that is
the exact wrong-plane error MSTR~Z made and corrected in `READ_HERE.md` section 5.

⚠ **`PATHFINDER_FUNDS = ("PFDE","PFOE")`** in `data/assets/scripts/silver/etf_schemas.py` is
hardcoded BY DESIGN -- it is a Pathfinder-specific converter, not a generic one. DIVZ/IDVZ were
never in its scope. **Do not "fix" it by widening the tuple**; the TrueShares fetch is a different
source with a different schema.

⚠ **UNRECONCILED, DO NOT SMOOTH IT:** Bloomberg's holdings COUNT sits **+1 (DIVZ)** and **+2 (IDVZ)**
above the issuer CSV row count. Small, unexplained, not a blocker. **The PRD should name who
reconciles it and against which source of truth**, rather than letting a later tie-out discover it.

---

## 4. WHAT THE PRD MUST COVER -- his words: "all ingestion and pipeline mechanics, threading it all the way to the frontend daily publish"

**(a) INGESTION** -- three sources on one daily cadence: Bloomberg derived layer (live today),
Pathfinder holdings CSV (live today, wrong bucket -- see (c)), TrueShares holdings CSV (**to build**).

**(b) THE CONSISTENT OUTPUT SHAPE** -- his central design ask. One constituent row shape that BOTH
providers normalise into, so downstream never branches on provider. Pathfinder and TrueShares CSVs
have DIFFERENT native schemas; the normalisation is the deliverable, not an afterthought. Name the
canonical columns, the cash-line convention (`SALXX` appears in both issuers' files), the
weight-units convention, and the identifier spine (CUSIP is present in both -- ticker is not
reliable for non-US lines in IDVZ).

**(c) THE BUCKET CONSOLIDATION -- HIS EXPLICIT CONSTRAINT, AND IT CARRIES A GATE.**
*"All that work needs to be managed in the opal-data-etfs bucket."* Today Pathfinder raw lands in
**`opal-data-assets`** and only the silver product reaches `opal-data-etfs`. ⛔ **`opal-data-assets/pathfinder/...`
HAS EXISTING CONSUMERS** (`data/assets/scripts/silver/etf_conversion.py`, the
`opal-assets-silver-etf` Lambda). **Moving or re-pointing served output is NEVER#3 and needs
never-widen sign-off (CTO+COO); a verified DELTA=0 deploy needs no hold.** The PRD must state
whether this is (i) new ETF ingestion lands in `opal-data-etfs` going forward while the existing
assets path stands, or (ii) a migration with the consumer census done first. **Do not begin a
migration inside the build.**

**(d) MEDALLION FORM (Rule 17b).** bronze raw vendor -> silver parquet queryable -> gold analytics,
all in `opal-data-etfs`; **platinum is the SERVING tier**. Rule 17a: **the issuer CSV lands as
BRONZE BYTE-FOR-BYTE; parquet is a SILVER act.** Do not convert at ingest.

**(e) THE FRONTEND DAILY PUBLISH** -- the thread he named explicitly. The Positioning page is the
consumer; the two book-level shells for DIVZ/IDVZ flip to full books once constituents land.
**AE's TO-5 (platinum producer schedule, `cron(0 13)` UTC) STANDS and CONSUMES this landing.**
His promote conditions from ~15:2xZ still gate the page: (i) the pipeline COMPLETE with the full
data structure for daily Bloomberg data for ALL ETFs; (ii) it DISPLAYS PROPERLY on the DEV build
with **GICS REPLACED BY SUB-CATEGORIES** on the frontend. **The promote word remains his.**

**(f) CADENCE + AS-OF.** One vehicle: the daily `/terminal-upload` schedule. `lib/trading_calendar`
is the ONE frontier (A2) -- `prev_trading_day` for a T-1 as-of; **`expected_last_trading_day()` is a
FRESHNESS FRONTIER, not a T-1 call.** Isolation per leg (L1-3 form). Capture-forward.

**(g) WHAT ALREADY EXISTS -- reuse, do not rebuild** (Build Ladder rung 2):
- `integrations/bloomberg/pipeline/etf_constituents_pull.py` -- legs 1a/1b/2/3 scaffolded; **leg 2
  is where the TrueShares fetch goes**; legs 2-TrueShares and 3 are declared `not-implemented`.
- `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` -- the vehicle, constituents leg wired
  (`RC_CONS`, exit 70-73, runs even if the ETF leg failed).
- `integrations/bloomberg/READ_HERE.md` -- the scenario playbook incl. both channels.
- `data/etfs/scripts/gold/etf_positioning_{gold,publisher}.py` -- the existing producer/publisher.

---

## 5. PROCESS -- Rule 27, and the two flags I am NOT adjudicating

**Rule 27 binds:** register -> purpose-level PRD -> **COO atom-decomp of the operative surfaces
BEFORE any TO exists** -> execute ON SPEC -> CVO surprise channel. Proof-of-spec derives from decomp
cells, aligned both directions with printed denominators. A value-enum/schema act (and **the
canonical constituent row shape IS one**) requires the Rule-24 four-postulate test at authoring.

**FLAG 1 -- D4's placement is `SITEZ -- TEMPORARY, TODAY ONLY`.** This project plainly outlives
today. The row's revert is `0.0.0_AB_MSTR` (base)'s act and reverts to LAPTOP-OWNED without a new
ruling. **A multi-week project cannot sit on a placement that expires tonight.** Andrew's word is
needed to extend or re-place it; MSTR~Z surfaces this and does not adjudicate it.

**FLAG 2 -- egress.** The TrueShares fetch is external egress. TrueShares egress was GRANTED
2026-08-21T20:45Z and Andrew pointed at the fund-documents page himself on 2026-08-24, so the
channel is authorized. **Google Sheets export is the delivery host for that same content** -- named
here explicitly so nobody has to make that call at a call site.

**NOT the source, recorded so it is not rediscovered:** the `Part F Schedule of Investments` on the
fund page is **SEMI-ANNUAL N-PORT** (DIVZ `03/31/2026`, `09/30/2025`; IDVZ `01/31/2026`,
`07/31/2025`), ~2 snapshots/year. Useful as an independent point-in-time CHECK, useless as a feed.

---

## 6. THE HANDOFF LOOP

1. **`1.0.0_SA_CTO~Z`** -- register the project + draft the PRD(s) against sections 2-5.
2. **`0.0.0_AB_MSTR~Z`** -- read the PRD back against these goals and confirm accuracy (Andrew's
   explicit instruction; this is a read-back, not a gate on CTO~Z's authorship).
3. **Andrew** -- the spawn word for COO~Z and the executing seats.
4. **`2.0.0_SA_COO~Z`** -- atom-decomp of the operative surfaces before any TO is cut.

**Records:** `laneZ_ANDREW_DIRECT_20260824_BLOOMBERG_ETF_CONSTITUENTS.md` (the constituent hunt) ·
`integrations/bloomberg/READ_HERE.md` §4-5 · `docs/architecture/ETFS_POSITIONING_DAILY_PULL_ORDER.md`
A4/A4.1 · session log `logs/2026-08-24/mstrz_session_close_1242-1355Z.md`.


---

## 7. AMENDMENT -- ANDREW-DIRECT, same day: FLAG (b) RESOLVED, and the canonical pattern already exists

**VERBATIM:** *"we can manage bronze ingestion for both channels in opal-data-assets and proceed
that way, I prefer that kind of structure actually, let CTO~Z know that, this gives us an
opportunity to develop a canonical format/pattern from the start for this work."*

**SECTION 4(c) IS SUPERSEDED.** Bronze for BOTH channels lives in `opal-data-assets`. **No
migration, no consumer census, no re-pointing** -- Pathfinder's raw stays where it is and its live
consumers are untouched. **The NEVER#3 never-widen tension is DISSOLVED, not managed.** His earlier
*"all that work needs to be managed in the opal-data-etfs bucket"* is thereby SCOPED rather than
contradicted: **raw vendor bytes -> `opal-data-assets`; the ETF pipeline PRODUCT -> `opal-data-etfs`.**
The PRD states that boundary explicitly rather than leaving it inferred.

**THE PATTERN HE WANTS TO "DEVELOP" ALREADY EXISTS AND BOTH SOURCES CONFORM** -- measured at S3 and
at source 2026-08-24, and very likely why he prefers the structure. Build-ladder rung 2: **extend
it, do not mint a second grammar beside it.**

```
{source}/{delivery_scope}/{bronze|silver|meta}/...
  pathfinder/filepoint/bronze/holdings/{d8}/ETF_Holdings.csv        80 objects
  pathfinder/PFDE/silver/  +  pathfinder/PFOE/silver/               80 + 80
  trueshares/{DIVZ,IDVZ}/bronze/netassets/{d8}/{fund}.html          40 each
  trueshares/{DIVZ,IDVZ}/silver/fact_netassets_page/date=.../       40 each
  {source}/{scope}/meta/{conversions,pulls,backfill-status.json}
```

- **Scope asymmetry is a FEATURE, do not "fix" it:** Pathfinder's bronze scope is `filepoint` (ONE
  file covering both funds) while its SILVER splits per fund; TrueShares is per-fund at both tiers.
  The grammar absorbs both because **scope is a field, not an assumption**.
- **Shared helper already used by both sources:** `_silver_key(source, scope, silver_feed, date)`
  -> `sr.silver_key(sr.BronzeObject(...))`, `data/assets/scripts/silver/etf_conversion.py:207`.
- **`convert_trueshares()` ALREADY EXISTS** (`:216`), converting `netassets_page` today.
  **Adding holdings is a NEW FEED in that converter, not a new converter.**
- **The bucket split he just endorsed is already architected:** `etfs-netassets-daily` carries a
  documented **C4** property -- `BRONZE_BUCKET` and `S3_BUCKET` resolve SEPARATELY, *"bronze lands
  in its OWN bucket."*

### ⛔ ONE OPEN QUESTION -- NAME IT IN THE PRD, DO NOT ASSUME IT

There appear to be **TWO silver surfaces** and I could not determine whether that is by design:
1. `opal-data-assets/{source}/{scope}/silver/fact_*` -- the converter's output, per source.
2. `opal-data-etfs/silver/holdings/{date}.parquet` -- **72 partitions, PFDE/PFOE only**, all-time
   2026-05-18..08-23; it is what the L1 leg reads to derive its universe.

**I could not find (ii)'s producer** in a repo sweep over 27,945 files. So: is (ii) the ETF-PRODUCT
silver tier fed from (i), or a parallel path? **The canonical row shape cannot be specified without
that answer**, because it decides whether the shape is authored at (i), at (ii), or once and shared.
⚠ **Treat (ii)'s producer as UNKNOWN-AT-MSTR~Z, NOT as absent** -- mine was a REPO sweep, and a
Lambda-only producer would not appear in it. *(The wrong-plane class: my sweep answered the question
its plane could answer.)*

**Relayed to `1.0.0_SA_CTO~Z` at 19:0xZ (msg 4829, DELIVERED).** Flag (a) -- D4's
`TEMPORARY, TODAY ONLY` placement -- **remains open at Andrew.**


---

## 8. AMENDMENT 2 -- ANDREW-DIRECT: D4 STAYS SITEZ UNTIL DONE, and THE FULL GROUND-UP CHAIN

**VERBATIM (both parts):**
> *"keep D4 on sitez until the project is done."*
> *"Furthermore, this is a good opportunity to build the ground-up, in pattern ingestion and
> processing (bronze and silver) layers for all relevant ETFs working from their idiosyncratic
> shapes, to unified parquet, to unified gold parquet format in opal-data-etfs/gold/ for platinum
> json serving in opal-data-portal-v2."*

**FLAG (a) IS CLOSED.** D4 placement is SITEZ until **the project is done** -- a COMPLETION
condition, not a date. That is a materially different row: a date-bounded placement expires silently
and correctly; a completion-bounded one **does not expire and must be reverted deliberately**, so the
row should name what "done" is. **The row edit is `0.0.0_AB_MSTR`'s act (register owner);
routed to them 2026-08-24 ~19:2xZ, not written from site Z.** Fifth placement on that row in six days.

**THE SCOPE IS NOW THE FULL MEDALLION CHAIN, ground-up and in pattern:**
```
issuer idiosyncratic shapes
  -> BRONZE   raw, per source, opal-data-assets, byte-for-byte (Rule 17a)
  -> SILVER   unified parquet
  -> GOLD     unified parquet, opal-data-etfs/gold/
  -> PLATINUM json serving, opal-data-portal-v2
```
*"Ground-up" AND "in pattern" together:* build the tiers properly rather than bolting constituents
onto what exists, **while conforming to the grammar both sources already use** (section 7).

### THREE TENSIONS -- surfaced, NOT resolved. The PRD must address each.

**(1) THE GOLD HOME CONTRADICTS CLAUDE.md RULE 17b AS AMENDED 2026-08-11.** He says
`opal-data-etfs/gold/`; the amendment says the product-gold home is
`opal-data-assets/portal/gold/{product}/{scope}/`. **His word is later and sovereign, so it binds** --
but the divergence must be RECORDED, because a future reader hitting law-says-X / estate-does-Y with
nothing between them will "correct" one of them. Either the PRD carries his ruling as a scoped
exception or it routes a Rule 17b amendment. **Measured: `opal-data-etfs/gold/` is EMPTY (0 objects)**
-- greenfield, which is precisely why "ground-up" is achievable here without touching anything.

**(2) PLATINUM ALREADY EXISTS IN TWO PLACES AND ONE IS LIVE-SERVED TODAY.**
`opal-data-etfs/platinum/etf_ownership_dashboard.json` was **written today 12:00:03Z**; monthly
`platinum/reports/{YYYY-MM}/etf_ownership.{html,pdf}` sit beside it; and
`opal-data-portal-v2/platinum/etfs/` already exists. His serving target is portal-v2, consistent with
Rule 17b -- **but it leaves the live `opal-data-etfs/platinum` artifact unaddressed.**
⛔ **Moving a served key is NEVER#3.** No move inside this build. The PRD states whether that artifact
stays, is superseded, or is out of scope, **and names who decides.**

**(3) "ALL RELEVANT ETFs" IS UNDEFINED -- A REAL SCOPE FORK, AND ANDREW'S TO SETTLE.**
`opal-data-etfs/config/etf_universe.json` declares exactly four tickers (DIVZ, IDVZ, PFDE, PFOE), is
**runtime-read** by the producers, and its own description says *"To add an ETF: append its ticker to
'tickers'; no redeploy."* So the universe is extensible **by design**, and the pipeline **must be
universe-driven, never hardcoded to four** -- that is the "in pattern" test.
**But TrueShares publishes well beyond ours** -- their own Part F filings name `spcz fldz rnwz lrnz
pvex oneh qber qbul paym payh onez` alongside `divz`/`idvz`. So "all relevant" may mean the four, or
a wider set. **Design so either answer costs nothing; put the question to him in the PRD.**

**RULE 24 NOW BINDS TWICE** -- once for the unified SILVER row shape, once for unified GOLD. They are
**different grains and may not share an axis**; the four-postulate test applies to each at authoring.

**And the two-silver-surfaces question (section 7) now matters MORE, not less**, because "unified
parquet" at silver is a named deliverable and cannot be specified while
`opal-data-etfs/silver/holdings/`'s producer is UNKNOWN-AT-MSTR~Z.

**Relayed to `1.0.0_SA_CTO~Z` msg 4830, DELIVERED (live seat).**


---

## 9. AMENDMENT 3 -- ANDREW-DIRECT: THE UNIVERSE IS FOUR. Tension (3) CLOSED.

**VERBATIM:** *"For our purposes at this stage and for the forseeable future, all relevant ETFs
means DIVZ IDVZ PFDE and PFOE."*

**SETTLED:** the universe is **four**. The wider TrueShares family (`spcz fldz rnwz lrnz pvex oneh
qber qbul paym payh onez`) is **OUT OF SCOPE**. Do not put the universe question to him in the PRD --
it is answered. Scope the decomp, the TOs and the acceptance to four tickers.

**NOT SETTLED INTO A HARDCODE, and the distinction is the point:** those four are **already the exact
contents of `opal-data-etfs/config/etf_universe.json`**, which is **runtime-read**. So reading the
config is **not speculative extensibility for a future he did not ask for -- it is the cheaper
implementation of the answer he gave**, and it is the estate's own rule (*"DERIVE FROM ONE DECLARED
AUTHORITY, NEVER RESTATE AT A CALL SITE"*). *"Foreseeable future" is not "never"*: a config read
costs nothing today; a restatement costs a silent divergence later.

### A LATENT DUPLICATE, FOUND WHILE CONFIRMING THIS -- and one of the two is MINE

**The sanctioned pattern is live in THREE production Lambdas**, each reading the config at runtime
with a `DEFAULT_UNIVERSE` fallback and a loud WARN when the config is unreadable:
`bd-49f-etf-ownership-daily-canonical:57` · `cot-etf-ownership-daily:72` · `inf-etf-ownership-daily:88`.

**Two pipeline scripts restate the universe in code instead:**
```
integrations/bloomberg/pipeline/etf_daily_pull.py:45         FUNDS = ["DIVZ","IDVZ","PFDE","PFOE"]
integrations/bloomberg/pipeline/etf_constituents_pull.py:62  FUNDS = ["DIVZ","IDVZ","PFDE","PFOE"]
```
**The second is MINE, written today.** I copied the shape of the first without checking whether the
estate already had a declared authority for it -- **the exact build-ladder rung-2 miss this brief
tells CTO~Z to avoid, committed in the same file it tells them to extend.**

**IT IS HARMLESS TODAY AND THAT IS WHY IT IS WORTH RECORDING.** All three lists agree right now, so
nothing misbehaves. **The moment the config changes, the three Lambdas follow and these two scripts
do not** -- a silent divergence with no error, found later by someone wondering why a fifth ticker
appears in ownership and not in the daily pull. Not urgent (his answer stabilises the config), and
**deliberately not fixed unilaterally mid-PRD-round**: it is precisely the *"ground-up, in pattern"*
tidy-up his instruction covers, so it belongs in the spec. Offered to CTO~Z as a one-line fix per
call site if they would rather have it now.

### RETRIEVAL NOTE -- it nearly became a false finding in this very brief

The first sweep for hardcoded tickers used `comp-find` with a filter and returned nothing. That was
**page 1 of 348 (8,688 hits)** -- an artifact of truncation, not a measurement -- and it would have
let this document assert *"nothing hardcodes the universe"* **while the file it was written in did.**
A direct `grep` found it in one call. **Never answer an ABSENCE question from a truncated result set.**

**Relayed to `1.0.0_SA_CTO~Z` msg 4831, DELIVERED.** Tensions (1) gold-home-vs-Rule-17b and
(2) the live platinum artifact remain OPEN and are CTO~Z's.
