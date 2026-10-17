# ETFS_RIVALS -- DECOMPOSITION, ROUND 12 (ENRICHMENT): the audit trail comes off the page so the main page keeps every security dialog (Z-S47; ADDENDUM 4 steps 1-2); then, on the Bloomberg hold lifting, the enrichment session bound (ADDENDUM 2) and Bloomberg's own key for CUSIP/ISIN rows (ADDENDUM 1)

```json
{
 "project": "ETFS_RIVALS",
 "round": 12,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.17 @43a5542d11; ADMITTED)",
 "prd_version": "v0.17",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round10.md@56de423b4d (ADDENDUM 3 route B, re-sequenced by ADDENDUM 4: steps 1 and 2 are round 12)",
 "andrew_direct": [
  "org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261006_163xZ_RIVALFUNDS_SECURITY_LINKS_GONE_EVERY_TICKER_MENTION_LINKS.md@05c469e083",
  "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_164xZ_RIVALFUNDS_AUDIT_OFF_PAGE_LINKS_FIRST_AUDIT_ROUTE_AFTER.md@56de423b4d"
 ],
 "narrowed_v1_0": "ADDENDUM 4 steps 1-2 only. Step 3 (the gateway audit route, then the page link) follows after step 2 is graded; its draft order and check are parked at deliverables/2.0.0_SA_COO~RV/round13_prep/. pk-1 (@982e914b1d) and the RIV-e-1 retry bound (@b555e81836) stay HELD under the site-Z Bloomberg-priority word (MSTR~Z msg 30060 @f42219ebfe).",
 "author": "2.0.0_SA_COO~RV",
 "cells": 3,
 "chains": 2,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.5",
 "revision_1_5": "2026-10-07 ~06:2xZ: round 15 (main workstream) cells APPENDED below (pd-1, pd-2, pd-3, ps-1, tm-1, co-1, bf-1, rt-1, md-1); no earlier cell is replaced.",
 "revision_1_4": "2026-10-07 ~03:3xZ: round 14 (main workstream) cells APPENDED below (ab-1, as-1); no earlier cell is replaced.",
 "revision_1_3": "2026-10-06 ~19:4xZ: round 13 (main workstream) cells APPENDED below; no earlier cell is replaced (round-11 analysis ruling 4: an issued order's cells stay readable).",
 "revision_1_2": "2026-10-06 ~19:1xZ, issuer amendment on ADDENDUM 5 @a8fb9c1df1 (CTO~Z msg 30204/30218): RIV-al-1 is cut as ROUND 13 of workstream BBGLEG (round 12 BBGLEG already issued; ONE ISSUER PER ROUND per (round, workstream)). The main workstream's round 13 (ADDENDUM 4 step 3 + the Z-S50 rule) waits on J1.",
 "revision_1_1": "2026-10-06 ~17:5xZ (workstream BBGLEG: eb-1 + pk-1, the Bloomberg leg, disjoint write surface from au-1), issuer amendment on Andrew's word lifting the site-Z Bloomberg hold (MSTR~Z msg 30169, record @8555ce7e12): the two cells the v1.0 narrowing held (ADDENDUM 1 @982e914b1d pk-1; ADDENDUM 2 @b555e81836 eb-1) are added. RIV-au-1 is unchanged and complete (drained c34e0875e9, deployed 8c40451259).",
 "round11_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round11.md"
}
```

## Rectangle (ADDENDUM 4, steps 1-2)

| item | cell | chain | risk |
|---|---|---|---|
| step 1: the audit block off the served page; the audit trail still written as its own platinum object; no link yet | RIV-au-1 | ~1 | SERVED |
| step 2: every ticker mention links to its modal, every dialog on the page; the over-cap FAIL line | RIV-au-1 (same write set) | ~1 | SERVED |
| step 2 proof on the 10-06 data (headroom >= 20% under DIALOG_SOFT_CAP; mentions = buttons, 0 dead) | issuer's one real run at the drain | - | - |
| step 3: GET /rivalfunds/YYYY-MM-DD/audit (gateway release under a never-widen pair), then the page link | NEXT round, after step 2 is graded | - | WORLD |
| ADDENDUM 2: the enrichment bounds its Bloomberg session attempts; unreachable exits 1 | RIV-eb-1 | ~2 (1 of 2) | SERVED |
| ADDENDUM 1: PARSEKYABLE_DES on the existing G4 reference request; the one-key join reads it | RIV-pk-1 | ~2 (2 of 2) | SERVED |
| ADDENDUM 5: the three readers take pk-1's parsekey (BBGLEG round 13) | RIV-al-1 | ~3 | SERVED |

Edges: none of data. eb-1 and pk-1 both write `enrichment_bloomberg.py`, so they are ONE chain (`~2`, one worker queue: eb-1 then pk-1); au-1 (`~1`) is disjoint. Stated gap (ADDENDUM 4): between step 1 and step 3, FWD-5's trade log and FWD-18's holdings list are
written but not served.

## Cells

### `RIV-au-1` -- the audit trail comes off the main page into its own dated object; every security mention links in-document; the over-cap fallback is loud (row Z-S47)
- Measured 2026-10-06 (2.0.0_SA_COO~RV): the served 2026-10-05 and 2026-10-06 pages (1,798,995 B and 1,813,001 B) carry
  `data-holding-dialogs="off"`, 0 `data-sec-dialog`, 0 `data-sec`. `render.render_page` (render.py:1796-1803) re-renders the
  whole page without holding dialogs once the with-dialogs render crosses `DIALOG_SOFT_CAP` (1,950,000 B, set under the
  gateway's 2 MB refusal). The closed `<details id="audit">` block is 1,119,671 B of the 10-06 page (holdings 454,238 B across
  13 funds, trade log 370,517 B across 221 trade panels).
- Interface:
  - `render.render_page(ctx)` returns the MAIN page with no audit block and NO link to the audit trail (the link lands with the
    gateway route in a later round, never a 404);
  - `render.render_audit_page(ctx)` returns the AUDIT page: a whole self-contained document (same shell and theme, no script)
    carrying the trades, holdings, refused and status sections and its OWN `_sec_dialogs` for the securities it names; every
    `data-sec` button on either page resolves to a `data-sec-dialog` element in the SAME document;
  - `render.validate` grades the main page (components lead, self-contained, no audit block) and a validator for the audit page
    grades what the closed block graded before (trades and holdings once each, one trace per trade);
  - `publish_page` writes `homes.page(day, "audit.html")` with read-back beside `index.html`, keeps a changed prior audit.html
    under `revisions/<ts>/` as it does index.html, and the manifest carries `audit_uri`, `audit_sha256`, `audit_bytes`,
    `holding_dialogs` ("on" | "off");
  - over `DIALOG_SOFT_CAP` the day still publishes, but the manifest and the run result's `detail` read
    `holding_dialogs: "off"` and the stage prints `FAIL: holding dialogs off ...` to stdout.
- **Organic trigger:** the 07:00 ET marker publish (publish-page stage).

### `RIV-eb-1` -- the enrichment bounds its Bloomberg session attempts and exits "unreachable" (ADDENDUM 2 @b555e81836)
- Measured 2026-10-06: with the DAPI precondition already FAILED, `rivalfunds.enrichment_bloomberg` kept issuing one blp_client
  request per batch (each opens its own short-lived session; `no RESPONSE ... within 90s` per batch) until Task Scheduler's
  30-minute ExecutionTimeLimit killed the vehicle at 11:30:01Z (0x41306); the names stage and the D12 leg never ran. Offline at
  base: 300 securities, Bloomberg down -> 18 calls (6 dividend + 6 historical + 6 reference batches), exit 3.
- Interface: an exception whose class name is `BloombergError` (blp_client's session/connect-level error: session start, open
  service, no-RESPONSE timeout) is UNREACHABLE; `BlpResponseError` and per-security errors are not. `SESSION_ATTEMPTS` (module
  int, 2 or 3): after that many CONSECUTIVE unreachable failures in one run the run makes no further Bloomberg call (dividends,
  market, names), lands nothing, and returns status FAILED with `detail.unreachable` true and `detail.session_attempts`;
  `exit_code` maps it to 1 (the existing contract). eg-1's guard unchanged. `integrations/bloomberg/` is NOT touched (Andrew's
  no-modify order).
- **Organic trigger:** the vehicle's 07:00 ET enrichment step on a day Bloomberg is unreachable.

### `RIV-pk-1` -- Bloomberg's own key for CUSIP/ISIN-keyed securities rides the existing G4 request; the one-key join reads it (ADDENDUM 1 @982e914b1d, row Z-S43)
- Measured 2026-10-06 on G1 2026-10-01: GQGU reports Nebius CUSIP-only (security_id null, raw N97284108, cusip N97284108, isin
  NL0009805522); WCMG reports `NBIS_US_Equity` with NO CUSIP/ISIN. RIV-ok-1's CUSIP/ISIN join cannot meet them; a refresh publish
  at its code is byte-identical to the control (Nebius shows twice).
- Interface: `enrichment_bloomberg` mode `market`: the current-value reference request for an identifier-keyed security
  ('/cusip/..', '/isin/..') also asks `PARSEKYABLE_DES`; a Bloomberg-keyed security's request does not. The answer lands in G4
  column `security_parsekey` (null when not asked or not answered); the market result's detail carries the number of
  PARSEKYABLE_DES points asked (S24's daily budget). `gold_holding_contribution` and the trade schedule's position key (RIV-ok-1's
  `row_keys` / `stable_key`): a row keyed by a CUSIP/ISIN whose G4 row carries `security_parsekey` P takes the key
  `security_key(P)` when another row in the input window carries that key; otherwise it keeps its own key.
- **Organic trigger:** the vehicle's 07:00 ET market pull (G4), then the 07:00 ET marker publish (A1) and the batch chain (G5).

### `RIV-al-1` -- the three readers take pk-1's parsekey, so one security under two listings is one key on the whole page (ADDENDUM 5 @a8fb9c1df1)
- Measured 2026-10-06 (2.0.0_SA_COO~RV, AST census of `data/etfs/scripts/rivalfunds/` at CLOUD 325e20b091): 20 call sites of 10
  functions that take pk-1's parsekey (`pk` / `parsekeys`); 6 omit it -- gold_buying_trend.py:79 and :192 (identity_maps),
  gold_input_census.py:139 (identity_maps), :140 (_cross_sectors), :146 (_books), sweep.py:306 (held_funds). On a two-listing
  plant (GQGU Nebius CUSIP-only N97284108 + WCMG NBIS_US_Equity, G4 parsekey N97284108 -> "NBIS US Equity") the rankings bucket
  both under NBIS_US_Equity while the trend and the census name GQGU's by N97284108.
- Interface: each of the six sites passes the parsekey, taken from the G4 the reader already reads (`parsekey_map(g4)`) or, for
  the sweep's hold gate, from `gold_trade_schedule.load_parsekeys(s, canonical)`; `gold_buying_trend.build(..., g4)` derives it
  from its `g4` argument. A reader with no G4 passes an empty map (today's behaviour). No other site changes.
- **Organic trigger:** the 07:00 ET marker publish (A1: trend, census) and the 09:00 ET sweep (the hold gate).

---

## ROUND 13 (main workstream) -- APPENDED, the cells above stay for the orders that cite them

Source: `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round11.md` @3ae96d6bc7 section 3 (items 1, 2; item 3 is BBGLEG round
13 RIV-al-1, drained 2d78ef2151; item 4 is a surprise row against the gate). Author 2.0.0_SA_COO~RV; frozen; revision 1.3 of this
file. Edges: none of data. fe-1 and lk-1 both write `render.py`: ONE chain (`~2`: fe-1 then lk-1). gw-1 (`~1`) is disjoint.
Deploy order (record): gw-1's gateway release under its pair BEFORE the publisher Lambda carrying lk-1's link.

| item | cell | chain | risk |
|---|---|---|---|
| 1a the audit gateway route | RIV-gw-1 | ~1 | SERVED (build) / WORLD (release, issuer act) |
| 2 fund-engagement: C-S47 + Z-S50 + per-button section census + C-S36 names | RIV-fe-1 | ~2 (1 of 2) | SERVED |
| 1b the page link + citation lines to the audit page | RIV-lk-1 | ~2 (2 of 2) | SERVED |

### `RIV-gw-1` -- the gateway serves the day's audit page at GET /rivalfunds/YYYY-MM-DD/audit (ADDENDUM 4 step 3; round-11 analysis item 1)
- Measured 2026-10-06: `infra/aws/ec2/opal-gateway/app/rivalfunds_view.py` serves only `<key_prefix>date=<day>/index.html`
  (`object_key`, `_PAGE_NAME`); server.py mounts `/rivalfunds`, `/rivalfunds/`, `/rivalfunds/archive`, `/rivalfunds/{day}`. The
  publisher has written `audit.html` beside index.html every day since round 12 (10-06: 1,326,857 B). The read policy
  (`gen_rivalfunds_location.py` `policy_doc`) already grants GetObject on `<key_prefix>*`: no new grant.
- Interface: `audit_key(day)` = `<key_prefix>date=<day>/audit.html` from the generated location (never typed) and the handler
  `rivalfunds_audit(request)`: no viewer 401; a bad date 400; a missing object 404 naming the day's audit page with a link to the
  day's page; otherwise the bytes with `_HEADERS`, under the same 2 MB cap and TTL cache as the page. The server.py Route line is
  the issuer's hookup at the merge; the gateway release is the issuer's act under a never-widen pair, BEFORE lk-1's link deploys.
- **Organic trigger:** a signed-in viewer following the main page's audit link.

### `RIV-fe-1` -- every mention in fund F's panel opens a modal with F's engagement; the page counts it; the trend's ticker-named keys get names (round-11 analysis rulings 1, 2, 5: C-S47 + Z-S50 + C-S36)
- Measured on the served 10-06 page (CVO census, C-S47): 15 mentions (3 securities, 2 funds) open a modal with no section for the
  linking fund -- Nebius (two keys; pk-1 + al-1), Alphabet (a share-class name crossing to the other listing), SpaceX (a fresh
  GQGU entry with no contribution row and no YTD trend row, so `_sec_dialogs` writes no GQGU section). Four securities still read
  in ticker form (C-S36): 8053 JP, RBLX US (rankings / AI text), 9433 JP, 000270 KS (trend only) -- the names stage reads only
  holding_contribution keys.
- Interface: a name mention inside fund F's panel links to the key F holds or traded among the keys carrying that name (a name two
  listings share resolves by F's own holdings, Z-S50; when F holds none, the page-wide rule applies). `_sec_dialogs` writes a
  `section data-fund=<_fid(F)>` for EVERY fund F with a contribution row OR a trend row (any period) for that key -- a trend-only
  fund's section states its buying. `render.fund_section_census(html) -> {"buttons", "with_section", "missing"}` over every
  `data-sec` button inside a `data-fund-panel`; `publish_page` puts it in the manifest (`fund_sections`) and prints a line starting
  `FAIL: fund sections missing` when missing > 0. `security_names` asks for the ticker-named keys of the newest holding_contribution
  AND buying_trend objects.
- **Organic trigger:** the 07:00 ET marker publish; the names stage on the vehicle's daily run.

### `RIV-lk-1` -- the main page's one audit link; the AI citation lines move to the audit page (ADDENDUM 4 step 3; round-11 analysis ruling 3)
- Measured on the served 10-06 page (CVO): the AI modals carry 148 machine keys in 89 citation lines ("Cited rows: ..."), plain;
  the main page has no audit link (au-1, by design until the route serves).
- Interface: `render.render_page(ctx)` carries exactly one `<a href="/rivalfunds/<day>/audit">` worded as "one step away"; no AI modal
  on the main page carries a "Cited rows:" line (grade line, full text, Observed/Inferred, invalidation stay). `render_audit_page`
  carries a section `id="citations"` with, per fund and account, its "Cited rows:" line (and [web] reads when present), each block
  `data-cited-fund="<fund>"` `data-ai-kind="<kind>"`. Deploys only after RIV-gw-1's route serves (never a 404).
- **Organic trigger:** the 07:00 ET marker publish after the route serves.

---

## ROUND 14 (main workstream) -- APPENDED

Source: `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round13.md` @594d1be8f8 (section 4 item 1 = ruling 4; ADDENDUM 1 =
Z-S54) and Andrew-direct `cooRV_ANDREW_DIRECT_20261007_031xZ_RIVALFUNDS_AI_VARIANCE_DO_A_AND_C_NOT_B.md` @3e040ecbf2. Author
2.0.0_SA_COO~RV; frozen; revision 1.4 of this file. Section 4 item 2 ("whatever the morning pass returns") is NOT in this
issuance: the pass runs after the 2026-10-07 07:00 ET vehicle run and its rows go to the next round; Andrew's word on Z-S54 is
cut now. Edges: none of data. ab-1 and as-1 both write `render.py` and `publish_page.py`: ONE chain (`~1`: ab-1 then as-1).

| item | cell | chain | risk |
|---|---|---|---|
| Z-S54 (A) the sweep order + (C) the badge and its manifest count | RIV-ab-1 | ~1 (1 of 2) | SERVED |
| ruling 4: the audit page's own size rule | RIV-as-1 | ~1 (2 of 2) | SERVED |

### `RIV-ab-1` -- an AI account is written against the build the page serves, and its badge says so when it is not (row Z-S54; round-13 analysis ADDENDUM 1; Andrew: "not needed do a and c")
- Measured on the served 2026-10-06 page (2.0.0_SA_COO~RV): 22 of 26 accounts carry a figure that differs from the panel beside it;
  149 of 197 cited contribution figures moved (IDVZ direction verdict: "Petrobras ... +0.47%" against the rankings' +0.93%), each
  under a green "Grounded". The AI step ran at 13:00:20Z against the 11:03Z tables; `sweep.run_ai_step` (sweep.py ~589) runs
  `ai_stage.run_for_day` FIRST and only the republish after it (publish_page.produce_a1's stale rebuild) rebuilt
  holding_contribution and buying_trend, at 13:05-13:06Z. The only disclosure is a small "Written against earlier tables" line.
- Interface:
  - (A) `sweep.run_ai_step` calls `publish_page.produce_a1(<sink object>, <sink spec>, <date>)` BEFORE `ai_stage.run_for_day` and
    returns its result under `a1_refresh`; a refresh that raises is recorded and the AI step still runs; nothing is refreshed
    when the AI step does not apply. Each account already records the revision of every row it cites (`cited_rows[].revision`).
  - (C) the PASS badge is `<span class="rf-grounding-PASS" data-grade="PASS" data-build="served">Grounded</span>` when every
    revision the account's cited rows carry for a vintage table (holding_contribution, buying_trend) is a revision the page
    serves for that table, else `... data-build="earlier">Grounded on an earlier build</span>` -- the same element, place and
    weight. `render.grounding_census(html) -> {"served": n, "earlier": m}`; `publish_page` writes it into the manifest as
    `ai_grounding`. A FAIL badge is unchanged. NO account is re-run after a rebuild (Andrew: B is not needed).
- **Organic trigger:** the 09:00 ET sweep's AI step and its republish.

### `RIV-as-1` -- the audit page's own loud size rule (row Z-W1-S48; round-13 analysis ruling 4)
- Measured 2026-10-07: the served audit.html is 1,381,244 B against the gateway's 2,097,152 B read cap (34.1% under); the trade
  log grows every day; `publish_page` checks only index.html against MAX_PAGE_BYTES and writes audit.html unconditionally.
- Interface: `render.AUDIT_SOFT_CAP` (bytes, default 1_950_000). `render.render_audit_page(ctx)` returns a document of at most
  that size when a cut can achieve it: trade trace panels are dropped OLDEST first (by window end) until it fits, and the page
  then carries one element `data-audit-cut="<count left out>"` stating in plain words how many trades were left out and the
  oldest window end still shown; with nothing cut the attribute is absent. `publish_page`: the manifest carries
  `audit_trades_left_out` (0 when none) and, when it is > 0, the stage prints a line starting `FAIL: audit page over cap` (the
  day still publishes). The gateway never refuses the audit page silently.
- **Organic trigger:** the 07:00 ET marker publish.

---

## ROUND 15 (main workstream) -- APPENDED

Source: PRD v0.18 `FWD-22`, `FWD-23`, ADDENDUM F (F.1-F.7) @6e245cbebe; five Andrew-direct records of 2026-10-07 04:5xZ-05:2xZ
(modal @ad78eef973, periods @82bb78106e, backfill/page-only/MTD @96d0ab2f4b, calendar days @69c7f24b44, script @efc0acb127);
scoping facts `deliverables/2.0.0_SA_COO~RV/round15_prep/MODAL_PRICE_SERIES_AND_PERIODS_SCOPING_FACTS.md` @d773ddba61. Author
2.0.0_SA_COO~RV; frozen; revision 1.5 of this file. Every interface below is PRESCRIBED so that a consuming cell builds against
the interface with a fixture and never against a sibling's branch: the edges are of interface, not of files.

Shared vocabulary (binding on every cell):
- **Periods:** `R30`, `R90`, `R365` -- calendar days. `asof = prev_trading_day(page_day)` (the existing CALL 3 rule); a window's
  first day is `asof - N calendar days`, its last day `asof`. `MTD`, `QTD`, `YTD` keep computing and are never displayed.
- **Chart object:** one JSON per fund per page day at `homes.page(<day>, "charts/<FUND>.json")` (opal_naming output), shape
  `{"fund", "asof", "generated_at", "ranges": {"R30": <first day>, "R90": ..., "R365": ...}, "securities": {<security_key>:
  {"name", "source_words", "points": [[<YYYY-MM-DD>, <price>|null, <source code>], ...], "gaps": [{"start", "end", "reason"}],
  "markers": [{"side": "buy"|"sell", "start", "end", "span": bool, "usd", "bps", "r", "n_trades"}]}}}`. Source codes:
  `m` market close, `i` holding-implied. `points` ascend by date and cover `asof - 365d .. asof`.
- **Route:** `GET /rivalfunds/<YYYY-MM-DD>/chart/<FUND>` on the gateway, JSON, behind the same identity wall.

Chains (M = 5; file sets disjoint across chains):

| chain | cells in order | files | risk |
|---|---|---|---|
| ~1 | RIV-pd-1, RIV-pd-2, RIV-md-1 | gold_holding_contribution.py, gold_buying_trend.py; then render.py | SERVED |
| ~2 | RIV-ps-1, RIV-tm-1, RIV-co-1 | price_series.py (new), trade_markers.py (new); then publish_page.py | SERVED |
| ~3 | RIV-bf-1 | enrichment_bloomberg.py, bbg_budget.py | WORLD |
| ~4 | RIV-rt-1 | infra/aws/ec2/opal-gateway/app/rivalfunds_view.py, server.py, their tests | WORLD |
| ~5 | RIV-pd-3 | ai_accounts.py | SERVED |

### `RIV-pd-1` -- the gold tables compute 30d / 90d / 365d as calendar days (FWD-23; F.2, F.6)
- Today `gold_holding_contribution.PERIODS = ("MTD","QTD","YTD","R30")` with R30 = the 30th NYSE trading day ending on the day
  (`period_start`, :120-128); `gold_buying_trend.PERIODS = ("YTD","R30","MTD","QTD")`, R30 likewise (`_period_starts`, :123-136).
- Interface: both modules' `PERIODS` gain `R90` and `R365` and keep `MTD`, `QTD`, `YTD`. `gold_holding_contribution.period_start(p,
  day)` and `gold_buying_trend._period_starts(day)[p]` return, for `R30` / `R90` / `R365`, `date(day) - 30 / 90 / 365` calendar
  days (`day` here is the as-of the stage already passes). `earliest_start` follows. A fund whose history starts after the window's
  first day keeps the existing partial rule (`period_clipped`, `price_coverage`). Each table's stage detail states, for one fund,
  the old and the new R30 window (`r30_window_was`, `r30_window_is`).
- Rulings at the cut (issuer): ONE anchor for both tables. The pure functions stay pure on the day they are handed
  (`period_start(p, d)` and `_period_starts(d)[p]` return `d - N` calendar days); `gold_buying_trend.build` hands the three
  rolling periods `gold_holding_contribution.as_of(<event day>)`, exactly as holding_contribution already does, so both tables'
  R30 / R90 / R365 start on the same day. MTD / QTD / YTD keep their present anchors and starts. `r30_window_was` and
  `r30_window_is` sit in each stage's result `detail`, each `{"fund": <id>, "start": <ISO>, "end": <ISO>}` for the first fund
  built.
- **Organic trigger:** the 07:00 ET marker publish's stale-table rebuild (`publish_page.produce_a1`).

### `RIV-pd-2` -- every switch on the page offers 30d | 90d 365d and opens on 30d; no QTD, YTD or MTD is displayed (FWD-23)
- Today `render.PERIODS = ("R30","QTD","YTD")`, `PERIOD_LABEL` names them, `_dialog_keys` covers R30 and YTD (:753), the trend
  sentence says "this year" for YTD (:1750), `_sec_dialogs` prefers the YTD trend row (:1776).
- Interface: `render.PERIODS = ("R30","R90","R365")`; `PERIOD_LABEL = {"R30": "Last 30 days", "R90": "Last 90 days", "R365":
  "Last 365 days"}`; the switch reads 30d, the dividing line, then 90d and 365d, and opens on R30. No element of the rendered
  main page or audit page carries the visible text QTD, YTD, MTD, "Quarter to date", "Year to date" or "Month to date". The
  dialog keys cover R30 and R365; the security dialog's trend row prefers R365. A period that ranks nothing for the fund greys
  and says why (unchanged rule). Rows of MTD / QTD / YTD in the context are ignored, not an error.
- Rulings at the cut (issuer): the switch's own words are short -- `render.PERIOD_SHORT = {"R30": "30d", "R90": "90d", "R365":
  "365d"}` is what each period radio's label prints (Andrew: "30d, then | 90d and 365d"); `PERIOD_LABEL` (the long names) is
  for table headings and dialog rows. The clause "the dialog keys cover R30 and R365" is WITHDRAWN (`_dialog_keys` has no
  caller); the dialog lists the three periods and its buying line is the R365 trend row.
- **Organic trigger:** the 07:00 ET marker publish.

### `RIV-pd-3` -- the AI accounts are written on the same three periods (FWD-23; F.2 last bullet)
- Today `ai_accounts` builds its facts from `("R30",5),("MTD",3),("QTD",3),("YTD",3)` (:165) and the YTD trend rows (:176-183).
- Interface: the fact pack is built from `("R30",5),("R90",3),("R365",3)` and the R365 trend rows; fact keys read
  `<fund>|R90|<bucket>` / `<fund>|R365|<bucket>`; no fact label names MTD, QTD or YTD; the prompt text names the three periods
  in plain words (last 30 / 90 / 365 days). `ai_accounts.PACK_PERIODS = ("R30","R90","R365")` is the one constant.
  The "not shown as current" rule for an older account is render's (round 14's badge) and is not this cell's.
- Rulings at the cut (issuer): a "fact label" is the fact's id and its text. Periods are named to the model in words or digits
  ("last thirty days" / "last 30 days"), consistently with the SYSTEM prompt's own number rule. `P_DIRECTION`'s "the year's
  trend" becomes "the 365-day trend".
- **Organic trigger:** the 09:00 ET sweep's AI step.

### `RIV-ps-1` -- one price series per security: market close first, holding-implied second, a gap with its reason third (FWD-22; C-MODAL-PRICE-SOURCE)
- Measured: `gold/security_market` holds 4 day partitions; `trade_schedule` 504. No module assembles a per-security daily series.
- Interface: new `rivalfunds/price_series.py`. `series(g4: DataFrame, g1: DataFrame, keys, start: date, end: date) -> {key:
  {"points": [(date, price|None, "m"|"i"|None)], "gaps": [{"start","end","reason"}], "source_words": str}}`. For each NYSE
  trading day in `[start, end]`: the G4 `px_close` of that date when present and positive (`m`); else the price implied by any
  universe fund's G1 report of that date, `market_value / quantity` with quantity > 0 (`i`; when several funds report, the
  median); else `None`. Consecutive `None` days form one gap with reason `"no market close on file and no fund reported the
  holding"`. `source_words` names in plain words which sources the series uses. No vendor call, no S3 call: pure over frames.
  `load(s, keys, start, end)` reads the two tables through the sink for the publisher.
- Rulings at the cut (issuer): a G1 row maps to a key through `gold_holding_contribution.row_keys` (the page's own key rule,
  raw-identifier alias included), never `security_id` alone. Several lots of one security in one fund's report are summed
  (market value and quantity) before the ratio. A key in neither frame returns all-None points and one gap over the range.
  Point dates are ISO strings. `load(s, keys, start, end)` returns the same dict `series` returns.
- **Organic trigger:** the publisher's chart object (RIV-co-1).

### `RIV-tm-1` -- a fund's trades in a security as sized markers (FWD-22; C-TRADE-MARKER)
- Measured: `trade_schedule` (G5) carries `action`, `window_start`, `window_end`, `window_trading_days`, `est_notional`; no
  share-of-fund column for the trade itself.
- Interface: new `rivalfunds/trade_markers.py`. `markers(g5_rows, fund_mv_by_date: {date: float}) -> [{"side", "start", "end",
  "span", "usd", "bps", "r", "n_trades"}]` per (fund, security): `side` = `buy` for entry / add, `sell` for trim / exit; `usd`
  = abs(`est_notional`); `bps` = `usd / fund_mv_by_date[window_end] * 10000` (the fund's total reported market value on the
  window end; absent -> `bps` None and `r` = R_MIN); `r` = the marker radius: `R_MIN` (3.0) at 20 bps or less, `R_MAX` (12.0) at
  500 bps or more, linear in bps between; `span` = `window_trading_days > 1`; trades of one side sharing one window are ONE
  marker with `n_trades` counted and `usd` / `bps` summed. A REFUSED window yields no marker. `words(marker) -> str` reads
  "Bought" / "Sold", the date or "between <start> and <end>", the dollar value, the basis points of the fund, and the count.
- Rulings at the cut (issuer): `g5_rows` is a list of row dicts (or a DataFrame, converted); `fund_mv_by_date` is keyed by
  `datetime.date`. The fund's total reported market value includes its cash lines (it is the report's total). A refused window
  has no G5 rows, so "no marker" is: empty rows in, `[]` out. `words()` prints dollars as `$26,000` and dates as ISO.
- **Organic trigger:** the publisher's chart object (RIV-co-1).

### `RIV-co-1` -- the publisher writes one chart object per fund beside the page, with its size line (FWD-22; F.5 items 1 and 4)
- Interface: `publish_page` writes `homes.page(day, "charts/<FUND>.json")` for every fund of the page, in the shape of the shared
  vocabulary, covering exactly the securities whose dialog on the rendered page carries that fund's section
  (`publish_page.dialog_fund_keys(html) -> {fund: [security_key, ...]}`, exported by THIS cell from a regex over the rendered HTML:
  `data-sec-dialog="<key>"` blocks and their `<section data-fund=...>` children; no render.py edit). Built from
  `price_series.load` and `trade_markers.markers`. `CHART_MAX_BYTES = 1_900_000` per object: over it, the 365-day points are
  thinned to weekly (and the object says `"thinned": true`); still over -> the object is not written and the stage prints `FAIL:
  chart object over cap for <FUND>`. The manifest gains `charts: {<FUND>: {"uri", "bytes", "securities", "markers",
  "thinned"}}`. The day's page publishes whether or not a chart object fails. Write once per revision, like audit.html.
- Rulings at the cut (issuer): `dialog_fund_keys(html)` and `CHART_MAX_BYTES` live in `publish_page` (this cell's file) and the
  cap is read at call time. A fund of the page with no dialog section gets NO object and no manifest entry. In the manifest
  `securities` and `markers` are counts. Thinning keeps the last trading day of each ISO week and every day that carries a
  marker's start or end. A fund whose object is refused has the manifest entry `{"uri": null, "bytes": <over-cap bytes>,
  "refused": true}`. `fund_mv_by_date` is the sum of `market_value` over the fund's G1 report of that date.
- **Organic trigger:** the 07:00 ET marker publish.

### `RIV-bf-1` -- an ad hoc Bloomberg close-price backfill over a date range, on the existing market route, under a row budget (FWD-22; F.5 card 2 answer; WORLD)
- Andrew-direct @96d0ab2f4b: "Yes for the rivalfunds funds only ... an ad hoc backfill for the selected funds that uses the
  existing BBG route"; @69c7f24b44: about 365 calendar days. Existing route: `enrichment_bloomberg` mode `market` already sends a
  one-day `HistoricalDataRequest` for a past date (`_market_pull`, `_blp_historical_data`).
- Interface: new mode `market-range` of stage `pull-enrichment`: event `{"mode": "market-range", "start", "end", "securities":
  [...], "batch_id", "sink", "max_points": int, "dry_run": bool}`. It plans `len(securities) x trading days in [start, end]`
  points; `dry_run` returns the plan and spends nothing; if the plan exceeds `max_points`, or exceeds `bbg_budget`'s
  `ceiling - reserve - spent(today)`, it REFUSES before any request, naming the points left. Otherwise ONE historical request
  per batch of 50 securities over `[start, end]` for `px_close`'s field only; it writes one `gold/security_market/date=<D>`
  object per date that has rows (never overwriting an existing object of that date: a date already holding a `market-*.parquet`
  is skipped and counted), each row `as_of_source = "backfill"`; it records the points in the `bbg_budget` ledger with mode
  `market-range`; a tripped session stops the run with what landed stated. No file under `integrations/` changes. The live
  run is the ISSUER's act under a never-widen pair, after the day's 07:00 ET vehicle run; the worker makes NO Bloomberg call.
- Rulings at the cut (issuer): a refusal is `status == "REFUSED"` (the module's own word). The result carries `plan: {"points",
  "securities", "trading_days", "batches"}`; a refusal's detail names the planned points and the points left, where "left" is
  the smaller of `max_points` and the budget remainder. Skipped dates are returned as `skipped_dates` (a list). The ledger
  records the points REQUESTED (securities x trading days of the range), since that is what the vendor was asked for. The
  budget read is a new `bbg_budget.check_points(points, today=None) -> None | detail` beside `check_backfill` (unchanged).
  A tripped session returns `FAILED` naming the dates that landed.
- **Organic trigger:** none (ad hoc by Andrew's word); the negative arm is the daily `market` mode, unchanged.

### `RIV-rt-1` -- the gateway serves a fund's chart object (FWD-22; F.5 item 2; WORLD, released by NFRA_OPLGTW)
- Today `rivalfunds_view` serves `/rivalfunds/<day>` and `/rivalfunds/<day>/audit` (2 MB cap, audit log, identity wall).
- Interface: `rivalfunds_view.chart_key(day, fund)` (the page prefix + `date=<day>/charts/<FUND>.json`; `fund` must match
  `^[A-Z0-9]{1,8}$`) and handler `rivalfunds_chart` for `/rivalfunds/{day}/chart/{fund}`: 200 `application/json` with the
  object's bytes; bad day or bad fund -> 400; no object -> 404 JSON `{"error": "no chart for this fund and day"}`; over the cap
  -> the page's own over-cap refusal; every call audit-logged with `{"day", "fund", "route": "chart"}`. The route is declared
  in `ROUTE_CLASS` as `access-layer` and mounted in `server.py` by this cell.
- Rulings at the cut (issuer): CORRECTION -- the over-cap refusal is the page's own (502, `rivalfunds_view.py` `_serve_day`),
  not a 413. No viewer -> 401 as the other routes. The 200 and the 404 are audit-logged; a 400 and a 401 are not, as today.
  The `server.py` Route and the `ROUTE_CLASS` line are THIS cell's (the lane refuses the issuer's commit there: round 13
  AMENDMENT 1), so both files are in its paths.
- **Organic trigger:** a signed-in click on a security modal after RIV-md-1 is served.

### `RIV-md-1` -- the security modal draws the price curve with the fund's trade markers, by the page's ONE script (FWD-22; F.7)
- Interface: each `<section data-fund=...>` of a security dialog gains a chart frame `<div class=rf-chart data-chart-fund="<FUND>"
  data-chart-key="<security_key>">` holding a three-way range switch (30d first, then 90d, 365d), a words line (`data-chart-status`)
  and the fund's trade list in words (from the context's trades; present with or without the script). The page carries EXACTLY
  ONE inline `<script>` block with no `src`; `_BAD_CONSTRUCTS` admits that one block and still refuses every other script,
  `src=`, `<link`, `@import`, `url(`; `render.script_count(html) -> int`. The script: on a dialog opening, fetches
  `/rivalfunds/<page day>/chart/<FUND>` (same origin, once per fund, cached), draws an inline-SVG curve of the chosen range
  from `points`, breaks the line at gaps and prints each gap's reason, draws each marker as a hollow circle of radius `r` at
  its end date (green buy, red sell; a `span` marker also draws a bar over its window), shows price + date on pointing at any
  part of the curve and the marker's words on a marker, prints `source_words`. On a failed or missing object the status line
  reads "Chart could not load" and the trade list stays. `data-history=none` and HISTORY_NONE leave the dialog.
  The script lands on the SERVED page only after the chart route serves (issuer's sequencing at the deploy).
- Rulings at the cut (issuer): the script is emitted unconditionally by `render_page`; the route-before-script order is the
  issuer's deploy sequence, not a flag. The AUDIT page gets no chart frame and no script, and `validate_audit` /
  `validate_fund` still refuse any script. `data-chart-fund` carries the fund ticker exactly as the route takes it. The range
  switch is three buttons `<button data-chart-range="R30|R90|R365">` reading 30d, 90d, 365d, R30 marked current. The trade
  list is one line per trade from `trade_markers.words` when that module is importable, else the page's own trade words; a
  fund with no trade in the security lists none and says "No trades in the last 365 days".
- **Organic trigger:** opening a security modal from a fund's section on the live page.

## ROUND 16 (main workstream; the repair of round 15) -- APPENDED 2026-10-07, revision 1.6 of this file

One repair cell, on row ETFS_RIVALS-Z-S55 (the issuer's real run of round 15, record
`deliverables/2.0.0_SA_COO~RV/round15/real_run_2026-10-06.json`) and the ruling of 1.0.0_SA_CTO~Z msg 30787 (shape (a), four
terms). Author 2.0.0_SA_COO~RV. No earlier cell is replaced; RIV-ps-1, RIV-co-1 and RIV-md-1 stay for the orders that cite
them. Chain `~6`, one cell, files price_series.py, publish_page.py, render.py, risk SERVED.

### `RIV-pc-1` -- a holding-implied price is drawn only for a listing quoted in US dollars; the chart says the currency (FWD-22; row Z-S55; CTO ruling 30787)
- Measured (real run, day 2026-10-06, 13 chart objects, 695 fund-securities): 598 carry both source codes; the first market
  close over the last holding-implied price before it is above 3 or below 1/3 for 152 of 598 (JP 43/43, LN 54/54, HK 11/11,
  KS 9/9; US 0/238). The funds' holding reports are in US dollars; a Bloomberg close is in the listing's quote currency.
  G4 `security_market.currency` (Bloomberg `CRNCY`) is stored per security: on 2026-10-05, 0 of 578 priced rows carry none;
  values include `USD` 193, `EUR` 92, `JPY` 78, `GBp` 35 (London quotes in pence; 1 London listing is `USD`).
- Interface: `price_series.series` reads each key's quote currency from the G4 frame it is handed: the `currency` of the
  key's NEWEST G4 row that carries one (a row with no `px_close` still counts). The value is READ, never inferred from the
  exchange code. Exactly `"USD"` -> the series is built as today (`m`, then `i`, then a gap). Anything else, and a key
  with no stored currency, -> market closes only: a day with no positive close is `None` whatever the funds report, and
  its gap reason is `"no market close on file (the funds' holding reports are in US dollars and this listing is not quoted
  in US dollars)"`. Each key's result gains `"currency": <the stored string> | None`. `source_words` says in plain words
  which sources the series uses and, for a non-dollar listing, that the prices are in the listing's currency.
  The chart object's `securities[<key>]` gains `"currency"`. The page's one script shows the currency beside the price
  axis and in the hover's price words (`null` -> "currency not on file"). A trade marker is placed by its DATE on the
  curve and never by a dollar price; on a day with no price it keeps its date marker.
- Rulings at the cut (issuer): `load` reads G4 as it does today (the same window), so a key whose only G4 rows fall outside
  the window has no stored currency and is treated as non-dollar. The currency comparison is exact and case-sensitive
  (`GBp`, `ZAr`, `ILs`, `KWd` are not dollars). No new Bloomberg field is requested and nothing under `integrations/`
  changes. The fixtures of `round15/checks/co-1.AC1.py`, `co-1.AC2.py`, `md-1.AC1.py` and `md-1.AC2.py` hold no G4
  currency; the cell may plant G4 rows carrying `currency` `USD` (no `px_close`) for those fixtures' securities and add
  `"currency"` to an exact key set those checks compare, and may change nothing else in them.
- **Organic trigger:** opening a non-US security's modal on the live page; the issuer's real run re-measures the 598.

## ROUND 17 (main workstream) -- APPENDED 2026-10-07, revision 1.7 of this file

One cell, on the ruling of 1.0.0_SA_CTO~Z msg 30817 term 2 (answering the round-16 measurement,
`deliverables/2.0.0_SA_COO~RV/round16/currency_measure_2026-10-06.json`). Author 2.0.0_SA_COO~RV. No earlier cell is
replaced. Chain `~7`, one cell, files price_series.py and render.py, risk SERVED. Term 1 of that ruling (the backfill's
security list includes formerly-held keys, inside the existing Bloomberg budget ledger) is the issuer's act at the
backfill run and is not a cell.

### `RIV-nc-1` -- a holding with no stored currency draws no curve and says why (FWD-22; CTO ruling 30817 term 2)
- Measured (round-16 real run, day 2026-10-06): 96 of 695 fund-securities carry `"currency": null` in their chart object
  (no G4 row in the 365-day window); the script draws their frame as an empty chart with a shaded gap.
- Interface: `price_series.NO_HISTORY = "No price history is stored for this holding yet."`. For a key with no stored
  currency, `series` returns `source_words` equal to `NO_HISTORY` exactly (its points stay all `None`, its `currency`
  `None`, its gaps as today). The page's one script, for a security whose `currency` is `null`: draws NO chart (no
  `<svg>` in the frame, no axis, no shaded gap, no gap-reason list), sets the frame's status line to the object's
  `source_words` (so the sentence comes from the object, and the same sentence is in the script as its fallback when
  `source_words` is absent), and changes nothing else: the range buttons may stay, and the static trade list stays.
  A security WITH a stored currency is drawn exactly as today, whatever its number of priced points.
- Rulings at the cut (issuer): the test is `currency == null` in the object, never "no priced point" (a non-dollar listing
  with 0 closes in a range but a stored currency still draws its frame and gap reason). No change to the chart object's
  keys or to `publish_page.py`. The sentence is not shown on the audit page (it carries no script).
- **Organic trigger:** opening the dialog of a holding that left the funds before the market table began; the issuer's
  real run reads the 96 in a browser.

## ROUND 18 (main workstream) -- APPENDED 2026-10-07, revision 1.8 of this file

One repair cell, on row ETFS_RIVALS-Z-S56 (the issuer's round-17 real run, packet
`deliverables/2.0.0_SA_COO~RV/round17/DRAIN_END_PACKET.round17.md`). Author 2.0.0_SA_COO~RV; the issuer rules it inside
cell RIV-md-1's surface. No earlier cell is replaced. Chain `~8`, one cell, file render.py, risk SERVED.

### `RIV-tl-1` -- the dialog's trade list never says "No trades in the last 365 days" about a window it has not read (FWD-22, F.7; row Z-S56)
- Measured (round-17 real run, day 2026-10-06): 618 chart frames carry the static words "No trades in the last 365 days";
  542 of them belong to a fund-security whose chart object holds one or more markers; 77 more list fewer trades than the
  object holds markers. The static list is built from the trades in the page context; the markers from the fund's trades
  over 365 days.
- Interface: `render._trade_list(trades)` with no trade in the page context returns `<p data-chart-trades>` holding exactly
  `"The fund's trades over the last 365 days load with the chart."`; with context trades it lists them as today. The
  static page no longer prints "No trades in the last 365 days" anywhere. The page's one script gains a pure function
  `tradelines(markers)`, exposed as `window.rfChart.tradelines`: no marker -> `["No trades in the last 365 days"]`;
  otherwise one `words(m)` line per marker, NEWEST first by `end` (ties by `start`, newest first), at most 20 lines, and
  when there are more a last line `"and <N> earlier trades in the last 365 days."` (`"trade"` when N is 1). When a chart
  object loads, the script replaces the content of the frame's `[data-chart-trades]` element with those lines built from
  ALL of the security's markers in the object (not the chosen range), for a holding with or without a stored currency
  (so before the `nohist` return). On a failed or missing object the static element stays as rendered.
- Rulings at the cut (issuer): the list is written once per object load and is not redrawn on a range click. A line is
  text (`textContent`), never markup. The AUDIT page is untouched. `round15/checks/md-1.AC1.py` pins the static words
  "No trades in the last 365 days" for the fixture's IDVZ Apple frame; the cell may change that one expected sentence to
  the new static sentence (and the docstring line that quotes it), and nothing else in that file.
- **Organic trigger:** opening any security dialog on the live page; the issuer's real run re-measures the 618.

## ROUND 19 (main workstream) -- APPENDED 2026-10-07, revision 1.9 of this file

One repair cell, on row ETFS_RIVALS-Z-S58 (the issuer's round-18 real run, packet
`deliverables/2.0.0_SA_COO~RV/round18/DRAIN_END_PACKET.round18.md`). Author 2.0.0_SA_COO~RV; the issuer rules it inside
cell RIV-pd-2's surface. No earlier cell is replaced. Chain `~9`, one cell, file render.py, risk SERVED.

### `RIV-ml-1` -- the month-by-month buying strip labels each cell with the month it is (FWD-23; row Z-S58)
- Measured (round-18 real run, day 2026-10-06): the page holds 393 month strips, every one labelled January to December
  by cell position; gold buying_trend's `trend_mark` months run from the window start's month, oldest first, through the
  page day's month. 248 of 349 R365 rows carry 13 month tokens (the strip draws the first 12 and drops the newest); the
  R30 and R90 strips (2 and 4 cells) read "Jan, Feb" for September and October.
- Interface: `render._month_chart(mark, end=None)` and `render._month_words(mark, end=None)`. `end` is the trend row's
  `window_end` (ISO string or date). With `end`: the LAST token is `end`'s month and each earlier token one month before;
  at most the last 12 tokens are drawn or named; every cell carries its month as `data-m=<Jan..Dec>`. With `end` None:
  tokens are labelled from January, as before, and each cell still carries `data-m`. `render.MONTH_CSS` prints the label
  from the cell (`content:attr(data-m)`); the twelve positional rules go. Every call site passes the trend row's
  `window_end` (the dialog's buying section and the sector tag's hover words).
- Rulings at the cut (issuer): the month is counted back from `window_end`, never forward from `window_start` (a clipped
  window's start is not its mark's first month on every row). A row with no `window_end` gets the legacy labels. No
  year is printed: at most 12 cells, so a month name is unique in a strip. The audit page is untouched unless it draws
  the same strip through the same function.
- **Organic trigger:** any fund panel's trend and any security dialog on the live page; the issuer's real run reads the
  strips against the listed trades.

## ROUND 20 (main workstream) -- APPENDED 2026-10-07, revision 1.10 of this file

One repair cell, on rows ETFS_RIVALS-Z-S60 and ETFS_RIVALS-Z-S61 and the ruling of 1.0.0_SA_CTO~Z msg 30897 (shapes (a),
(b), (c), four terms). Author 2.0.0_SA_COO~RV. No earlier cell is replaced. Chain `~10`, one cell, files
gold_holding_contribution.py, gold_canonical_shape.py, enrichment_bloomberg.py, gold_buying_trend.py, risk WORLD (it
changes a Bloomberg-calling mode; no worker makes a call).

### `RIV-bk-1` -- backfill rows feed the price curve only, carry their currency, and a range can be finished on a later day; the trend's parsekey join reads its column (rows Z-S60, Z-S61; CTO ruling 30897)
- Measured (backfill preparation, read-only, `deliverables/2.0.0_SA_COO~RV/backfill_prep/`): 863 securities x 252 trading
  days = 217,476 points against a 120,000-point daily allowance. Read in code: `gold_holding_contribution._daily` prices
  a holding-day from two consecutive G4 closes before the holding-implied return, and a newer G4 object makes the next
  publish rebuild that table, so backfilled closes would move every fund's served rankings; `_market_range` writes rows
  with `px_close` only (currency NULL), marked `as_of_source == "backfill"`, and no reader filters on that mark;
  `gold_buying_trend.handler_entry` reads G4 as `("security_id", "date", "security_name")`, so `parsekey_map(g4)` is
  always `{}` there (morning pass 2026-10-07: holding_contribution MERGED 13, buying_trend SPLIT 7).
- Interface:
  1. `gold_holding_contribution.drop_backfill(g4) -> DataFrame` returns the frame without rows whose `as_of_source` is
     exactly `"backfill"` (a frame with no such column is returned unchanged). `handler_entry`'s own G4 read loads
     `as_of_source` and drops those rows before anything else uses the frame: a day's table is identical with and
     without backfill-marked rows present in G4.
  2. `gold_canonical_shape`: when it picks the G4 partition for a report date (`_g4_for`), a partition whose rows are
     all backfill-marked is never picked (it falls back to the nearest earlier partition holding a non-backfill row),
     and a backfill-marked row never fills GICS.
  3. `enrichment_bloomberg` mode `market-range`: every backfill row carries `currency`. A security's currency is its
     STORED one (the `currency` of its newest non-backfill G4 row, read through the sink); for a security with no stored
     currency the mode makes ONE reference request for the single field `CRNCY` for exactly those securities, through
     the client hook the mode already uses, with `bbg_budget.check_points` before and `bbg_budget.record` after (points =
     securities asked); a security with no answer gets `None`. A dry run's plan gains `"currency_lookups"`. The plan's
     `points` and the budget check count only the dates NOT already held, so a range is finished on a later day inside
     that day's allowance; the ceiling and the reserve are untouched.
  4. `gold_buying_trend.handler_entry`'s own G4 read loads `security_parsekey`.
- Rulings at the cut (issuer): `price_series` and the chart object keep reading backfill rows (that is what they are
  for). Nothing under `integrations/` changes and no field other than `CRNCY` is added. The daily market pull already
  asks `CRNCY` per security, so a currently-held security takes its stored currency and costs no lookup. A reference
  request that fails leaves the run FAILED with nothing landed, like a failed historical batch. No stage marker is
  written. Input-census and trade-schedule readers are untouched (a backfill row's name, sector and parsekey are NULL
  and those readers skip blanks). A held date is neither counted NOR asked: each batch's historical request is sent
  once per contiguous run of un-held trading days, and the ledger records exactly what is asked (securities x the days
  of that run). The stored-currency read lists G4 from the range's first day to the run date and no further back. When
  no partition holding a non-backfill row exists at or before a report date, `_g4_for` answers as it does today when no
  partition exists at all. The round-15 checks `bf-1.AC1.py` and `bf-1.AC2.py` pin the mode as first built (no reference
  request; one request per batch over the whole range; a held date counted in the plan and the ledger): the cell may
  change in those two files ONLY the figures, request shapes and the "no reference request" clause that these rulings
  change, and nothing else.
- **Organic trigger:** the issuer's backfill run (never a worker's), split over the days the ledger's room allows, each
  after that day's 07:00 America/New_York vehicle run; the issuer's DELTA 0 proof on the served rankings (ruling term 1).

## ROUND 21 (main workstream) -- APPENDED 2026-10-07, revision 1.11 of this file

One cell, on the L9 grades of 3.0.0_SA_CVO~RV for rounds 15 to 19 (`surprise-channel/adjudications/ADJUDICATION_v20.Z.md`
row ETFS_RIVALS-Z-C-S60 @0c69a8829e). Author 2.0.0_SA_COO~RV; the issuer rules these inside cells RIV-ml-1, RIV-tl-1 and
RIV-md-1's surfaces. No earlier cell is replaced. Chain `~11`, one cell, file render.py, risk SERVED.

### `RIV-pl-1` -- the month strip shows every month of its window, the trade list is headed by its window, and the chart's currency label clears the axis (FWD-22, FWD-23; CVO row Z-C-S60)
- Measured by the CVO on the round-19 real run: 56 of the 252 year strips have one or more markers in October 2025,
  inside the 365-day trade list and outside the 12-cell strip, whose first cell is November 2025; in 141 dialogs a
  30-day or 90-day buying section sits above the 365-day trade list, and the list carries no heading of its own; the
  "Price in <currency>" label is printed over the axis's top figure when that figure is long (TWD); the drawing uses
  about two thirds of the frame's width.
- Interface:
  1. `render._month_chart(mark, end)` draws EVERY token of the mark, at most 13. When the first and the last cell are
     the same calendar month (a 13-token mark), those two cells carry the month and a two-digit year (`data-m="Oct 25"`,
     `data-m="Oct 26"`); every other cell carries the bare month. A mark of 12 tokens or fewer is drawn as round 19
     drew it. `render._month_words(mark, end)` names the same months the same way.
  2. `render._trade_list(trades)` puts, immediately before the `[data-chart-trades]` element, the caption element
     `<p data-chart-trades-head>` holding exactly `Trades in the last 365 days`, with or without a context trade. The
     script leaves the caption alone when it rewrites the list.
  3. In the page's one script the "Price in <currency>" label is drawn where it cannot overlap an axis figure (right
     aligned at the plot's top right edge), and the chart is as wide as its frame.
- Rulings at the cut (issuer): the stylesheet's month cells must stay readable at 13 cells (the two year-carrying
  labels are five characters). `round15/checks/ml-1.AC1.py` pins round 19's rule that a 13-token mark draws 12 cells
  (its arm (a), and arm (e)'s "12 months at most"); the cell may change those two arms to this cell's rule and nothing
  else in that file. Items 1 and 2 are checked mechanically; item 3 is the CVO's to grade in a browser.
- **Organic trigger:** any security dialog on the live page; the issuer's real run.

## ROUND 22 (main workstream) -- APPENDED 2026-10-07, revision 1.12 of this file

One cell, the second display cell of ROUND_ANALYSIS.round20 @c9a9e27770 (rulings R2 items 2 and 4, R3) and of the R3 read
(`deliverables/2.0.0_SA_COO~RV/round21/READ_R3_S59_CAUSE.md` @ad9f13a0bb, causes A and C). Author 2.0.0_SA_COO~RV. No
earlier cell is replaced. Chain `~12`, one cell, files render.py, trade_markers.py, publish_page.py, risk SERVED.

### `RIV-pm-1` -- the oldest strip cell is marked as a part month; no curve is drawn where there is none; the markers run through the page day and a zero-dollar trade is not one (FWD-22, FWD-23; analysis R2, R3; row Z-S59)
- Measured: the 365-day window begins inside October 2025, so the 180 thirteen-cell strips' first cell is a part month,
  and a 90-day strip's first cell is July from the 8th (cause B: 3 strips read as disagreeing with their markers). One
  fund-security has a stored currency, 4 markers and 0 prices and draws nothing (BIDD 6475395Z GR); CGIC 2454 TT has 2
  prices and 126 markers riding the top edge. Two strips show an October trade whose window ends on the page day and has
  no marker (cause A); two securities carry trims at -0.0 dollars drawn as markers (cause C).
- Interface:
  1. `render._month_chart(mark, end=None, start=None)` and `render._month_words(mark, end=None, start=None)` take the
     trend row's `window_start`. When `start` is given, its day of month is after the 1st, and the strip's first cell is
     `start`'s own calendar month (same year and month), the FIRST cell carries the attribute `data-part` and no other
     cell does; `render.MONTH_CSS` gains a rule on `[data-part]` that shows the reader the month is partial;
     `_month_words` appends " (part month)" to that month. Otherwise no cell carries it. Both call sites pass the row's
     `window_start`. Everything round 21 built stays.
  2. In the page's one script: `nohist(s)` returns the no-history sentence also for a security with a stored currency and
     not one priced point (the plain sentence; the object's `source_words` only when the currency is null); a new pure
     function `window.rfChart.curve(pl)` answers true only when the range's plan holds two or more priced points, and for
     a range where it is false the script draws no svg and prints "Fewer than two prices on file in this range." when the
     range holds exactly one priced point (a range with none keeps "No price on file in this range."). Each sentence
     appears once in the script.
  3. `trade_markers.markers` skips a trade whose `est_notional` is zero (0.0 or -0.0) as it skips a null one. The chart
     object's markers run through the PAGE day: the trades handed to `trade_markers.markers` include one whose
     `window_end` is the page day. Prices (`points`, `ranges`, `asof`) still end at the as-of day.
  4. (Amendment 1, row ETFS_RIVALS-Z-C-S64; CTO ruling msg 31031.) The chart object's markers are keyed by the SAME
     one-key rule the trend and the rankings use: a fund's trade recorded in G5 under a CUSIP or ISIN key whose G4
     `security_parsekey` gives a Bloomberg key is gathered under that Bloomberg key, so a security the page shows
     under one key carries every trade the fund made in it. Measured on the round-21 real run: 7 GQGU securities
     folded into their Bloomberg keys by round 20 lost their 86 markers, because the publisher groups G5 rows by the
     recorded key. Reuse the join the trend stage applies to G5 rows (`gold_buying_trend.build`: `parsekey_map(g4)`
     and `identity_maps`); do not derive a second rule.
- Rulings at the cut (issuer): the fund market value read for the markers' basis points is widened through the page day
  too, so a page-day marker states its basis points. In the script a marker whose end is after the object's `asof` is
  kept by `plan` and drawn at the chart's right edge; it is in the trade list either way. The script builds its nodes
  with `createElement` / `createElementNS` as today, never `innerHTML`. No key is added to the chart object. The audit
  page is untouched. Cause D of the R3 read (a trade under another key) is item 4 where the other key is a CUSIP or
  ISIN with a parsekey; any other shape of cause D is not in this cell. Item 4 has no check file of its own: the cell
  adds a package test for it (a fund's trade under a CUSIP key with a G4 parsekey row appears as a marker under the
  Bloomberg key), and the proof is the issuer's real run: total markers per fund equal the run before the fold for
  all 13 funds, GQGU's 7 Bloomberg keys hold the 86, and 0 dialogs show a buying section above "No trades".
- **Organic trigger:** any security dialog on the live page; the issuer's real run re-reads the 11 strips of row Z-S59.

## ROUND 23 (main workstream) -- APPENDED 2026-10-07, revision 1.13 of this file

One cell, item 1 of the ENRICHMENT LIST of ROUND_ANALYSIS.round22 @f8a61834fd (rulings R1, R2). Items 2 to 4 of that list
are the issuer's reads and acts on 2026-10-08 (the two runs' REPORT lines, row Z-S62, the AI period-word count, the
deployed-stage read before the backfill, leg L3) and Andrew's look; they are not cells. Author 2.0.0_SA_COO~RV. No
earlier cell is replaced. Chain `~13`, one cell, file render.py, risk SERVED.

### `RIV-ks-1` -- a security named in an account's text never opens a dialog without the panel fund's section (rows Z-S65, Z-S66; analysis round 22 R1, R2)
- Measured: the served page of 2026-10-07 (rounds 15 to 22) reads `fund_sections` 2247 buttons, 4 missing: in GQGU's
  panel "META PLATFORMS INC" and "ASML HOLDING NV-NY REG SHS" target the dialogs `30303M102` and `N07059210`, which hold
  a name and no section; the full dialogs are `META_US_Equity` and `ASML_US_Equity`. Reproduced by `ks-1.AC1.py` with the
  served markup: the fund traded the security under a raw key (so `render._fund_keys` counts it), the raw key's page
  name differs from the tabled key's only in case, the account cites the raw key, and `_panel_page` / `_name_link` let
  the citation decide; `_sec_dialogs` builds sections from contribution and trend rows only. The count read 0 through
  round 16, 3 from round 17, 6 from round 21 on day 2026-10-06; the publisher prints a FAIL line and publishes.
- Interface:
  1. On the rendered page every `data-sec` button inside a fund panel targets a dialog that carries a section for that
     fund, or the mention is plain text. A name whose deciding key has no section for the panel's fund links to the key
     of the same security that has one (the page's one key), else reads as plain text with the written form kept in
     the text or a title. No dialog on the page has zero sections.
  2. Round 13's rule stays: inside fund F's panel a name several listings carry links to the listing F holds; the cited
     key breaks a tie between keys that each HAVE a section for F.
  3. `publish_page` already prints `FAIL: fund sections missing` and publishes. It keeps publishing (a day's page is
     not withheld for a link); the manifest's `fund_sections` stays the count. No change to the audit page's bytes
     beyond what item 1 causes.
- Rulings at the cut (issuer): the repair is in how a mention picks its key, not in adding sections for raw keys and
  not in rewriting stored account text. Reuse the page's existing name tables (`_NAME_ALL`, `_NAME_KEYS`) and the set of
  keys that will carry a section; do not read G4 or add a second key map to the renderer. Row Z-S57 (Meta in GQGU under
  two keys in buying_trend) is NOT this cause as far as the issuer has read: Z-S57 is a table bucket, this is a link;
  the worker says in its report whether its read agrees. Why the FAIL line reached no row for two rounds is the
  issuer's answer, not the cell's: the real-run record carried the count and the issuer's packets did not read it;
  from this round the issuer's real-run read prints `fund_sections.missing` in the packet.
- **Organic trigger:** GQGU's panel on the live page; the issuer's real run of the served day reads `fund_sections`
  missing 0 and 0 dialogs with no section.

## ROUND 24 (main workstream) -- APPENDED 2026-10-07, revision 1.14 of this file

One cell, item 1 of the ENRICHMENT LIST of ROUND_ANALYSIS.round22 ADDENDUM 2 @be5cb4f530 (the chart's UI: ADDENDUM 1,
Andrew-direct 2026-10-07 ~19:0xZ, record @f76452470f). Item 2 (row Z-S57) is withdrawn by CTO ruling msg 31341; items 3
to 5 are the issuer's reads and acts. Author 2.0.0_SA_COO~RV. No earlier cell is replaced. Chain `~14`, one cell, files
render.py and page_theme.py, risk SERVED.

### `RIV-cu-1` -- the dialog chart is framed, its x-axis is dated, its hover read-out is bold and focal, and a buy or sell marker has a dramatic tooltip (Andrew-direct 2026-10-07 ~19:0xZ; analysis round 22 ADDENDUM 1 and 2)
- Measured on the served page (rounds 15 to 23): the chart is a 600 x 200 svg with no border and no x-axis label; the
  hover read-out is one `<p class="rf-ch-read">` under the chart in the dialog's body type; a marker's hover text is the
  svg's own `<title>` (a small delayed browser tooltip). Andrew's words: the price/date read-out "should be much more focal,
  bold, and obvious"; the tooltip, "especially when hovering over a buy/sell moment, should be much more dramatic"; "a box
  around the chart element itself with clear dates on x-ticks, give it a little more space and make it more of an event".
  "The mechanics are all there": no change to the data.
- Interface (all in `render.py` -- `CHART_SCRIPT`, `CHART_CSS` -- and `page_theme.py`; one inline script as today):
  1. **Dated x-ticks.** A new pure function `window.rfChart.ticks(pl)` takes a plan (`rfChart.plan(s, from, to)`, whose
     `a` and `b` are the range's first and last day numbers) and returns an array of 4 to 7 objects `{x, label}`: `x` a day
     number with `pl.a <= x <= pl.b`, strictly increasing; `label` a date a reader can place: day and month ("8 Sep") for a
     range of 100 days or fewer, month and two-digit year ("Oct 25") for a longer one; no two labels equal. The script's
     draw writes one svg `text` per tick carrying the attribute `data-tick` with that label as its text, under the plot.
  2. **The frame and the room.** The chart's svg sits inside an element of class `rf-ch-frame`; `render.CHART_CSS` gives
     `.rf-ch-frame` a border of at least 1px solid, a border-radius, a padding of at least 10px and a background; the svg's
     viewBox height is at least 280 (today 200) with the same 600 width.
  3. **The read-out.** The read-out element (class `rf-ch-read`) is placed BEFORE the svg inside the frame, and
     `render.CHART_CSS` gives `.rf-ch-read` a `font-size` of at least 20px and a `font-weight` of at least 700 (the dialog's
     body is 17px, weight 400), stated as plain numbers in px. On a pointer move over the curve it shows the price with
     its currency and the date, as today; the price and the date are each in their own child element (`data-read="price"`,
     `data-read="date"`) so the price can be the larger.
  4. **The marker tooltip.** The script creates ONE element of class `rf-ch-tip` per chart (hidden by default: the
     attribute `hidden`), inside the frame. On `mouseover` (and `focus`) of a marker it is shown (no `hidden`), carries
     `data-side="buy"` or `"sell"`, and its text states the side in a word ("Bought" / "Sold"), the dollars, and the date
     or dates -- the content of `rfChart.words(m)` at least; on `mouseout` (and `blur`) it is hidden again. `CHART_CSS`
     gives `.rf-ch-tip` a `font-size` of at least 16px, a `font-weight` of at least 600, `position:absolute`, a padding and
     a coloured background or border that differs by `data-side` (green for buy, red for sell, the script's `G` and `X`
     colours). Each marker is focusable (`tabindex="0"`). The svg `<title>` of a marker stays.
- Rulings at the cut (issuer): nodes are built with `createElement` / `createElementNS`, never `innerHTML`. No key is
  added to the chart object and no gold table, price series, marker or window changes. The audit page is untouched (it
  has no script). The dialog's static trade list and month strip stay as they are. Everything rounds 15 to 23 built
  stays: every existing check file under `round15/checks/` still ends `PASS 0 failures`. The page stays under its
  1,950,000-byte cap; the script may grow by at most 3,000 bytes (today 7,369) and the frame adds no per-dialog markup
  to the static page (it is built by the script).
- Rulings on the check drafter's questions (issuer; the check files accept exactly these): a tick's label names the date
  its own `x` falls on; the 100-day boundary is `pl.b - pl.a`; the price child shows the stored currency code, not a
  sign; the date child names the same point as the price; the tooltip states "Bought" or "Sold" (never both), the
  dollars with thousands separators and the date or dates; the tooltip's colour by side is set by `CHART_CSS` rules on
  `[data-side=buy]` and `[data-side=sell]`, not by inline style; hidden means the attribute `hidden`; a marker is a
  circle with a `title` child and `data-m`, focusable with `tabindex="0"`; there is exactly one frame, one read-out and
  one tooltip per chart after every range switch; CSS lengths are in px and the frame's padding is at least 10px on
  every side; the static page carries no `rf-ch-frame` or `rf-ch-tip` markup.
- **Organic trigger:** any security dialog on the live page, pointer over the curve and over a buy or sell marker.

## ROUND 25 (main workstream) -- APPENDED 2026-10-07, revision 1.15 of this file

Two cells, by CTO ruling msg 31428 on row ETFS_RIVALS-Z-S69 (BLOCKING) and the round-24 analysis msg 31413: the readers'
grain of gold security_market (the disarm of Z-S69; PRD v0.19 C-OWED-GRAIN, rulings msgs 31416 and 31432) and the
marker read-out repair (CVO ADJUDICATION_v28). FWD-24's history-owed step and top-up writer are round 26. Author
2.0.0_SA_COO~RV. No earlier cell is replaced. Two chains with disjoint files: `~15` RIV-rg-1 (the readers), `~16`
RIV-mr-1 (render.py). Risk SERVED.

### `RIV-rg-1` -- a date's rows of gold security_market are the union of ALL its objects, one row per security and date by a stated rule (row ETFS_RIVALS-Z-S69, BLOCKING; PRD v0.19 C-OWED-GRAIN, G.4; CTO rulings msgs 31416, 31428)
- Measured (census `deliverables/2.0.0_SA_COO~RV/round25_prep/READER_CENSUS_SECURITY_MARKET_20261007.md` @33e8bbe318, and
  the live table): every reader of G4 rows takes ONE object per date, `revision.newest` of the date's uris. For
  2026-09-29 the partition holds a live pull `market-20260929-53bc393958bd.parquet` (434 securities, 430 with `px_close`,
  `source` `blp_client.reference_data`) and an import `market-20260929-afcd903ad844.parquet` (172 securities, 0 with
  `px_close`, 164 with a GICS sector, `source` `import:bbg/2026-09-29/characteristics.parquet`). Neither name carries a
  capture time and the readers hand `revision.newest` bare uris, so its "an import never outranks a live object" rule
  cannot apply and the NAME decides: the import wins and all 430 market closes of that day reach no stage (355
  fund-security chart entries of the served page then draw that day from the fund's own valuation). On 2026-10-02 three
  objects of 601 rows hold the same securities: the control.
- Interface (in `data/etfs/scripts/rivalfunds/`; no new module is required, one shared function is):
  1. ONE function, used by every reader below, returns a date's G4 rows as the union of ALL `.parquet` objects of that
     date's partition, ONE row per (`security_id`, `date`). Where several objects hold the same (`security_id`, `date`),
     the rows are ordered: (a) a row whose `as_of_source` is not `"backfill"` before a backfill row; (b) a row whose
     `source` does not start `import:` before an import row; (c) the later capture time in the object's name
     (`revision.capture_time`; a name with no time is oldest); (d) the later `as_of` of the row; (e) the object name,
     descending -- a last tie-break that decides only when (a) to (d) tie. From that order the merged row is built in
     TWO parts (CTO term, msg 31432). THE PRICE GROUP -- `px_close`, `total_return_index`, `currency`, `as_of`, `source`,
     `as_of_source` -- travels WHOLE from ONE row: the first row in the order whose `px_close` is not null (if none has
     a close, the first row in the order). A close is never combined with a currency, a price date or a price source
     from another object, even when its own currency is null. THE DESCRIPTIVE FIELDS -- every other column (the GICS
     columns, `security_bloomberg`, `security_parsekey`, a name) -- each take the first non-null value in the order. A
     column an older object lacks reads as null for its rows.
  2. Readers moved to it: `gold_holding_contribution._newest_by_date` + `_read` as used for G4 by
     `gold_holding_contribution.handler_entry`, `gold_buying_trend.handler_entry`, `gold_input_census.build`,
     `price_series.load` and `publish_page._chart_reads`; `gold_canonical_shape._g4_for` (still ONE date per report date,
     the greatest at or before it that holds a non-backfill row, but that date's rows are the union); and
     `gold_trade_schedule.load_parsekeys`. `_newest_by_date` keeps its one-object rule for every OTHER table (G1, G5 and
     the A1 tables are written whole per revision).
  3. For 2026-09-29 this keeps the live pull's close for every security it prices (430), the live pull's GICS where it
     has one and the import's where only the import has one. `drop_backfill` and every other row rule run AFTER the union.
  4. What a stage RECORDS as the date's G4 revision or location (for example the G4 revision inside a G1 revision in
     `gold_canonical_shape`, `location` in `gold_input_census`) stays the `revision.newest` object of the date, as today.
- Rulings at the cut (issuer): nothing is written to or deleted from `gold/security_market`; the writer
  (`enrichment_bloomberg.py`) is not in this cell. No change to `revision.py`'s ordering contract. The cost of opening
  every object of a date is accepted (8 objects over 5 dates today). `publish_page._a1_window` returning no window for
  buying_trend is NOT in this cell.
- Rulings on the check drafter's questions (issuer; the check files accept exactly these): the ONE shared function is
  `gold_holding_contribution.g4_rows(s, day)` -- `s` the sink, `day` a `YYYY-MM-DD` string -- returning a pandas
  DataFrame of that date's merged rows with every column any object of the date carries. It reads `source`, `as_of` and
  `as_of_source` to order the rows even when a caller's column filter leaves them out; a caller filters columns AFTER.
  A `px_close` of 0.0 is a close (not null). Backfill-marked rows are handled after the union exactly as today: the
  price series keeps a backfill-only row, `drop_backfill` drops it for the rankings, `_g4_for` leaves it out.
  `_newest_by_date(s, prefix, lo, hi)` keeps its signature and its one-object rule for G1, G5 and the A1 tables.
  Interface item 4 is narrowed: `_g4_for`'s recorded uri and revision stay the `revision.newest` object by its own
  provenance rule; what the input census records as a price's `location` and what the rankings manifest lists under
  `g4` may name the newest object or every object read -- say which in the report; neither is graded.
- **Organic trigger:** the next daily run and any republish; the issuer's real run prints, per fund, the rankings and
  the 30d / 90d / 365d tables before and after, each moved figure named, and the control on 2026-10-02 reads no change.

### `RIV-mr-1` -- while a marker is pointed at, the read-out names THAT marker's day and price, and the tooltip never covers the read-out (CVO ADJUDICATION_v28; CTO round-24 analysis msg 31413)
- Measured on the served page (round 24): pointing at a buy or sell marker shows the tooltip for the marker while the
  read-out above the chart keeps the price and date of the last curve position the pointer crossed, so the two can name
  different days; and a marker near the top of the plot flips its tooltip to a position that can cover the read-out.
- Interface (`render.py` `CHART_SCRIPT` / `CHART_CSS` only; one inline script as today):
  1. On `mouseover` or `focus` of a marker the read-out (`.rf-ch-read`) shows the marker's END date in its
     `data-read="date"` child and, in its `data-read="price"` child, the price of the priced point the marker is drawn
     on (the nearest priced point, as the marker's `cy` is computed today) with the stored currency code; a marker
     with no priced point in the range shows the date and no price. On `mouseout` or `blur` the read-out returns to its
     idle prompt until the pointer next moves over the curve. A `mousemove` whose target is a marker does not overwrite
     it (as today: the handler returns for `data-m`).
  2. The tooltip (`.rf-ch-tip`) is positioned only over the svg's own box: its top edge is never above the svg's top
     edge inside the frame, so it cannot overlap the read-out, which sits before the svg. It still flips below a marker
     when there is no room above, and stays inside the frame horizontally.
  3. Everything round 24 built stays: `cu-1.AC1.py`, `cu-1.AC2.py` and `cu-1.AC3.py` still end `PASS 0 failures`; the
     script grows by at most 600 bytes (today 9,348).
- Rulings at the cut (issuer): nodes by `createElement` / `createElementNS`, never `innerHTML`; no key is added to the
  chart object; no data change.
- **Organic trigger:** any dialog chart on the live page, pointer on a marker.

## ROUND 26 (main workstream) -- APPENDED 2026-10-08, revision 1.16 of this file

One cell, the re-cut of round 25's readers by CTO rulings msgs 31477 and 31480 on CVO ADJUDICATION_v30 (RIV-rg-1 J1 NOT
MET) and row ETFS_RIVALS-Z-S71. RIV-mr-1 of round 25 shipped alone (ledger `etfs-rivalfunds-r25-mr1`). FWD-24's history-owed
step and writer move to round 27. Author 2.0.0_SA_COO~RV. No earlier cell is replaced: RIV-rg-1 stays as built and this
cell narrows it. Chain `~17`, one cell, the shared reader, risk SERVED.

### `RIV-rg-2` -- the union reads only objects whose name carries a capture time; a date's untimed objects are read as before, one object (row ETFS_RIVALS-Z-S71, BLOCKING; CVO ADJUDICATION_v30, RIV-rg-1 J1 NOT MET; CTO rulings msgs 31477 and 31480)
- Measured (`deliverables/2.0.0_SA_COO~RV/round25/g4_date_offset_read_20261007.json`; row Z-S71): the live table's object
  `date=2026-09-29/market-20260929-53bc393958bd.parquet` holds the closes of 2026-09-30, a day early (48 of 58 comparable
  closes match the funds' 2026-09-30 valuations, 32 match only that day, 0 match only its own date). Its `as_of` column
  says 2026-09-29, so no column shows it. The four dates written since by the daily leg (names with a capture time,
  `market-20261002T111038Z-...`) match their own day. The served readers ignore the mis-dated object by a name
  tie-break; `g4_rows` / `g4_window` as merged in round 25 (RIV-rg-1) would read it. Round 25's readers are merged and
  NOT deployed.
- Interface (the shared reader in `gold_holding_contribution.py`, and nothing else unless a caller needs it):
  1. An object takes part in the union ONLY when `revision.capture_time` of its name is not None (a TIMED object). For a
     date whose partition holds NO timed object, the reader returns the rows of exactly ONE object, the
     `revision.newest` of the date's uris -- byte for byte what `_newest_by_date` + `_read` returned before round 25. For
     a date that holds timed AND untimed objects, the union is over the timed objects only; the untimed ones are not
     read.
     `gold_canonical_shape._g4_for` on a date with no timed object ALSO behaves exactly as before round 25: its own pick
     by provenance records (for 2026-09-29 the live object, from which it joins SECTORS, never closes), the rows of that
     one object, and that object's uri and revision recorded (`rg-1.AC3.py` arm b pins it).
  2. Everything else RIV-rg-1 built stands: the order (non-backfill, live over import, later capture time, later
     `as_of`, name), the price group travelling whole, the descriptive coalesce, one row per security and date,
     `_newest_by_date` unchanged for the other tables.
  3. The mis-dated object is NAMED, so the rule does not rest on a name's shape alone (CTO term 1): a package test
     plants `market-20260929-53bc393958bd.parquet` (closes) beside `market-20260929-afcd903ad844.parquet` (an import with
     no price) on 2026-09-29 and asserts that no reader returns a close for that date; its docstring says the object
     holds 2026-09-30's closes and cites row ETFS_RIVALS-Z-S71.
- Rulings at the cut (issuer): no object is written, moved, renamed or deleted in `gold/security_market`. On the live
  table this cell changes NO served figure: the only multi-object dates are 2026-09-29 (two untimed objects: read as
  before) and 2026-10-02 (three timed objects with the same rows: the union equals the newest). The term for future
  writers (every object a writer adds carries, per close, the trading date it belongs to, and the reader keeps a close
  only where that date equals the partition date; CTO term 2) is FWD-24's, round 27, and is NOT in this cell.
- **Organic trigger:** any republish; the issuer's real run reads 0 moved rows of holding_contribution and of
  buying_trend against the served tables, and chart objects equal to the served ones.

## ROUND 27 (main workstream) -- APPENDED 2026-10-08, revision 1.17 of this file

Three cells for FWD-24 (PRD v0.19 ADDENDUM G: the year of closes kept by the daily sequence), on the ENRICHMENT LIST of
ROUND_ANALYSIS.round22 ADDENDUM 4 ("FWD-24's owed step and writer under R13, the request off") and CTO rulings R13,
msgs 31402, 31480, 31514 and 31527. The standing Bloomberg request stays OFF: it waits on Andrew's recorded answer.
Author 2.0.0_SA_COO~RV. No earlier cell is replaced. Three chains with disjoint files: `~18` RIV-ho-1 (a new module),
`~19` RIV-tw-1 (enrichment_bloomberg.py), `~20` RIV-rk-1 (the shared reader). RIV-tw-1's checks stub the module of
RIV-ho-1, so no chain waits on another. Risk SERVED.

### `RIV-ho-1` -- the history-owed set: every (security, trading day) of the last 365 days with no stored close, computed from stored tables alone (FWD-24, PRD v0.19 C-HISTORY-OWED)
- Measured (the CRO's analysis behind ADDENDUM G; live read by the issuer 2026-10-08): gold `security_universe` holds
  1,051 securities with `first_seen`, `last_seen` and `funds` (a comma-joined list of fund tickers); gold
  `security_market` holds closes on 5 trading days. Nothing computes what is owed.
- Interface (a NEW module `data/etfs/scripts/rivalfunds/history_owed.py`; standard library, pandas and the package's own
  readers only; NO vendor import and no network call but the sink's):
  1. `history_owed.owed(s, day, window_days=365)` -> a pandas DataFrame, one row per owed unit, columns `security_id`,
     `security_bloomberg`, `date` (ISO string), `funds`. A unit is owed when: the security is in the newest
     `security_universe` object at or before `day` with a non-blank `security_bloomberg`; `date` is a trading day
     (`lib.trading_calendar`) with `day - window_days <= date <= as_of(day)` where `as_of(day)` is the previous trading
     day of `day`; `first_seen - window_days <= date` is NOT required (a security held at any time in the window is owed
     its whole window: the PRD's "every security a tracked fund held in the last 365 days has its year of closes"), but
     the security's `last_seen` is on or after `day - window_days`; and `hc.g4_window` over the window returns no row for
     (`security_id`, `date`) whose `px_close` is not null. Rows sorted by `date` descending, then `security_id`.
  2. `history_owed.summary(df)` -> a dict `{"securities": n, "units": n, "dates": n, "newest": iso, "oldest": iso}`
     (zeros and None for an empty frame).
  3. A unit whose only stored close sits in an object the shared reader does not read (an untimed object beside timed
     ones; the mis-dated 2026-09-29 object) IS owed: the set is defined by what the readers return, not by what S3 holds.
- Rulings at the cut (issuer): the unit of the budget is this row (one security on one day). Cash lines and securities
  with no Bloomberg key are not owed (there is nothing to ask). The function writes nothing.
- Rulings on the check drafter's questions (issuer): `first_seen` is no bound at all -- a security whose `last_seen` is on
  or after `day - window_days` (inclusive) is owed every trading day of the window through `as_of(day)`, before its
  `first_seen` and after its `last_seen` included; the window's first day is inclusive; "the newest universe object at
  or before `day`" includes one dated `day`; `day` is an ISO string and `s` the sink; a blank key includes a
  whitespace-only one (`hc._blank`); an empty result still carries the four columns; `date` is an ISO string.
- **Organic trigger:** the issuer's real read prints `summary(owed(s, day))` for the live tables.

### `RIV-tw-1` -- the daily leg asks for owed closes inside the budget and lands each date's top-up as its own object, each close carrying its trading date; the request is OFF by default (FWD-24, C-OWED-GRAIN, C-OWED-IN-THE-LEG, C-OWED-BUDGET; CTO ruling R13)
- Measured: `enrichment_bloomberg.py` mode `daily` asks for the securities held today and lands ONE object per date;
  mode `market-range` (the hand-run backfill) skips any date that already holds a `market-*` object
  (`_held_dates`), checks `bbg_budget.check_points` before any request and records every request sent. The vehicle runs
  `python -m rivalfunds.enrichment_bloomberg --mode daily` FROM THE WORKING TREE every day at 11:00Z (rows Z-S62, Z-S72):
  this file's merge is its deploy to that job.
- Interface (`enrichment_bloomberg.py` only, plus the module of RIV-ho-1 which it imports lazily):
  1. A switch, environment variable `RIVALFUNDS_HISTORY_OWED`, read once per run: unset, empty or `"0"` = OFF. With it
     OFF the `daily` run is byte-for-byte what it is today: it does not import `history_owed`, makes no additional sink
     list or get, sends no additional request, prints no additional line and returns the same result dict. `"print"` =
     compute the owed set after the daily pull lands and print one line `HISTORY OWED: owed <units> units, <securities>
     securities, <dates> dates; asked 0 (request off); carried <units>`, send nothing, write nothing. `"ask"` = compute,
     ask, land, print `HISTORY OWED: owed <o>; asked <a>; landed <l>; carried <c>`.
  2. With `"ask"`: the units to ask are the first `HISTORY_OWED_CAP` (a named module constant, 5,000) of the owed set in
     its own order (newest dates first); `bbg_budget.check_points(n)` is called BEFORE any request with the count to
     ask, and a refusal asks nothing and prints the refusal with `carried <all>`; every request sent is recorded with
     `bbg_budget.record("history-owed", <points requested>, batch_id)`; what is not asked is carried (counted, never
     stored: the next run recomputes the owed set).
  3. Landing: per date, ONE new object in that date's partition, named by `market_target_uri(date, revision)` with a
     revision that carries the capture time (as `_market_pull` builds it), never overwriting a name and never touching
     another object. Every row carries, beside the existing columns, **`price_date`**: the ISO trading date the vendor
     returned for that close. A returned close whose own date is not the partition's date is NOT written (and is
     counted in the printed line as `misdated <n>`). Rows are marked `as_of_source = "backfill"` and `source` as
     `market-range` marks them today.
  4. The result dict of the `daily` run gains a key `history_owed` only when the switch is not OFF.
  5. The Bloomberg client is reached only through the function `market-range` already uses for a history request; no
     file under `integrations/` is edited or imported in a new way.
- Rulings at the cut (issuer): NOTHING in this cell or its checks calls a vendor: every check and test stubs the client
  hook, as `bf-1.AC1.py` / `bf-1.AC2.py` do. The switch stays OFF in the repository and on the vehicle; turning it on is
  Andrew's recorded answer relayed by 1.0.0_SA_CTO~Z, never a merge. `market-range` and its `_held_dates` are left as
  they are.
- Rulings on the check drafter's questions (issuer): any value of the switch other than exactly `print` or `ask`
  (case-sensitive) is OFF. ONLY the top-up objects carry `price_date`: they are written with the market schema plus
  that one string column; the daily pull's object and `market-range`'s objects are written exactly as today.
  "Misdated" means: a close the vendor returns for a date that is NOT one of the units asked for that security; it is
  not written and is counted. A close is landed in the partition of its own returned date, with `price_date` equal to
  it, only when that (security, date) was asked. `landed` may count rows or objects. A refusal's line format is free
  beyond containing `HISTORY OWED:` and `carried <all>`. `tw-1.AC1.py` compares the switch-OFF run with the module as
  it is at commit 361b735308, read from git: the OFF path stays identical to that commit's behaviour.
- **Organic trigger:** none while the switch is OFF; the issuer's read is the 2026-10-08 and later vehicle logs showing
  the enrichment leg unchanged.

### `RIV-rk-1` -- the reader keeps a close only where its own trading date equals the partition date; an untimed date that gains a timed object keeps its sectors; a backfill close does not cost a security its sector (CTO ruling R13; CTO half @e081a672d4 note; worker row Z-W15-S2)
- Measured: `gold_holding_contribution.g4_objects` / `_g4_merge` (rounds 25, 26). No stored object carries a per-close
  date today, so nothing tells the reader that a close belongs to another day (row Z-S71). On a date with untimed
  objects only (2026-09-29) the reader returns one object, an import with sectors; the first timed top-up landed there
  would make the union "timed only" and drop those sectors. And a security whose live row has no close while a backfill
  row has one merges to a backfill-marked row, which `drop_backfill` then removes whole, sector and parsekey included.
- Interface (`gold_holding_contribution.py`; `gold_canonical_shape.py` only if `_g4_for` needs it):
  1. THE PRICE DATE. Where a row carries a non-null `price_date`, its price group (`px_close`, `total_return_index`,
     `currency`, `as_of`, `source`, `as_of_source`, `price_date`) takes part in the merge only when `price_date` equals
     the partition date; otherwise that row offers no price group (its descriptive fields still coalesce). A row with no
     `price_date` column, or a null one, is treated as today (every stored object).
  2. THE UNTIMED DATE THAT GAINS A TIMED OBJECT. On a date holding timed AND untimed objects, the ONE untimed object
     the pre-round-25 read picks (`revision.newest` of the date's untimed uris) contributes its DESCRIPTIVE fields to
     the merge, last in the order, and NEVER a price group. Other untimed objects are still not read.
  3. THE BACKFILL CLOSE. `drop_backfill` no longer removes a merged row whose price group came from a backfill row when
     any of its descriptive fields came from a non-backfill row: it returns the row with the price group nulled
     (so the rankings price it as they do today, from the fund's valuation) and the descriptive fields kept. A row
     whose every contributing object is a backfill object is still dropped. The price series (`price_series.load`)
     still receives the backfill close.
  4. Everything rounds 25 and 26 built stands; on the live table NOTHING read today changes (no stored object carries
     `price_date`; no date mixes timed and untimed objects; no backfill row exists).
- Rulings at the cut (issuer): the column is named `price_date` in both this cell and RIV-tw-1. No object is written,
  moved or deleted.
- Rulings on the check drafter's questions (issuer): `price_date` may arrive as an ISO string or a date; both compare
  to the partition date. In item 2 a security present ONLY in the picked untimed object, with no non-null descriptive
  field there, yields NO row (so `rg-2.AC1.py` arm c stands unchanged). Descriptive fields are every column outside
  the price group. Item 3 also binds `gold_canonical_shape._g4_for`: a merged row whose price group came from a
  backfill row while a descriptive field came from a non-backfill row stays in its sector join (today it filters the
  merged frame on `as_of_source`); `rk-1.AC1.py` does not grade that, so the cell's package test does. Item 4 is the
  issuer's own measurement of the live table on 2026-10-07 and 2026-10-08: 8 objects over 5 dates, the two untimed on
  2026-09-29 alone, no `price_date` column anywhere, `as_of_source` absent or `pull` on every row.
- **Organic trigger:** any republish; the issuer's real run reads 0 moved rows and identical charts.

## ROUND 28 (main workstream) -- APPENDED 2026-10-08, revision 1.18 of this file

Two cells on the ENRICHMENT LIST of ROUND_ANALYSIS.round22 ADDENDUM 6 (@8ea0b4a05a; CTO msg 31885: issue now): (1) the AI
accounts, CTO rulings R19 and R20; (2) the top-up writer before `ask`, CTO half C2 of round 27 and ruling R13. Not in the
round: anything that sets the switch `RIVALFUNDS_HISTORY_OWED`, and `HISTORY_OWED_CAP` (the CTO rules it with Andrew's
answer). Author 2.0.0_SA_COO~RV. No earlier cell is replaced. Two chains with disjoint files: `~21` RIV-aw-1
(ai_accounts.py), `~22` RIV-tc-1 (enrichment_bloomberg.py). RIV-tc-1's merge is a deploy to the 11:00Z vehicle and lands
only after RIV-tw-1's J1 is graded on the 2026-10-09 run. Risk SERVED.

### `RIV-aw-1` -- an AI account names its periods in words with the window's two dates, never by the system's codes, and cites a row for every dollar figure; one correction call when it does not (CTO rulings R19, R20; rows C-S83; ROUND_ANALYSIS.round22 ADDENDUM 6)
- Measured (served page 2026-10-08, 13:08Z): 26 account items over 13 funds. The codes `R30`, `R90` and `R365` reach the
  reader 240 times ("The top R30 contributor ..."): the SYSTEM prompt teaches the codes and the fact lines carry them.
  One item (TXUE, the 30-day account) is shown as grounding FAIL: it states "$1.2 million" and cites no row for it, and
  three uncited facts round to that amount, so `attach_uncited` cannot attach one
  (`deliverables/2.0.0_SA_COO~RV/round28_prep/R20_TXUE_GROUNDING_FAIL_READ_20261008.md`). Where exactly one uncited fact
  matches, `attach_uncited` attaches it silently and the item reads "Grounded".
- Interface (`data/etfs/scripts/rivalfunds/ai_accounts.py` only):
  1. **Words, not codes.** `PROMPT_VERSION` becomes `a1-chain/7`. The SYSTEM prompt and the TEXT of every fact line
     given to the model name a period as "the last 30 days", "the last 90 days" or "the last 365 days" and never contain
     the tokens `R30`, `R90`, `R365` (a fact's `id` and its `cited_row` keys keep the codes: they are keys, not prose).
     Each prompt names, once, the two end dates of each period it covers, as ISO dates, taken from the same window the
     fact pack is built on (the 30-day account: the 30-day window; the direction verdict: the 30-, 90- and 365-day
     windows), and tells the model to state the window's two dates once in `text`.
  2. **A wording check**, a new pure function `wording_check(text_fields, windows) -> list[str]` (empty = clean): it
     returns one reason per defect over the item's `text`, `observed`, `inferred` and `invalidation`: (a) a period code
     as a whole word, case-insensitive (`R30`, `R90`, `R365`; also `MTD`, `QTD`, `YTD`); (b) the item's own window
     dates not both present in `text` (the 30-day account: the 30-day window's two ISO dates; the direction verdict: the
     365-day window's two).
  3. **Cite every dollar figure.** The SYSTEM prompt requires the id of a fact in `cited` for EVERY figure written. A
     figure the item writes that no CITED row carries is a defect even when exactly one uncited fact matches it
     (today's silent attach).
  4. **One correction call per item.** When an item has a wording defect (2) or an uncited figure (3), the chain sends
     ONE more `client.chat` for that item: the item's own message history, the item's reply as the assistant turn, and
     one user message that lists each defect (for an uncited figure: the figure and the ids of the candidate facts;
     for a code: the code and the words to use; for missing dates: the two dates) and asks for the corrected JSON
     object. The corrected reply replaces the item and is graded once more by the same checks; there is no second
     correction. The direction verdict's own prompt is built on the FIRST reply of the 30-day account, as today: a
     correction of item 1 does not re-run item 2. At most 2 additional `chat` calls per fund per run.
  5. **What is stored.** An item still carrying a wording defect after its correction is stored with
     `grounding = "FAIL"` and the defect in `grounding_reason` (prefix `wording: `), beside any figure reasons. After the
     correction, `attach_uncited` still runs as today (an item is not failed for a figure a single fact explains), and
     the number of figures it attached is written as an integer `attached_figures` inside the row's `input_manifest`
     JSON, with `corrections` (0 or 1). No column is added to the stored table and no reader changes.
  6. `regrade_rows` / `regrade_day` re-grade stored items with the new checks and send NOTHING to a model.
- Rulings at the cut (issuer): the fix is where the words are made; nothing in `render.py` or `publish_page.py` replaces
  a code in a stored account. The page's own labels and data attributes that say R30 / R90 / R365 are not this cell's.
  NOTHING in this cell or its checks calls a model or the web: every check and test passes a stub client. The first
  real accounts under the new prompt are the 13:00Z sweep's after the deploy.
- Rulings on the check drafter's questions (issuer): a period's two dates are the `period_start` and `period_end` of
  that period's contribution rows in the fact pack (the dates the page's own period labels show), not the 30-trading-day
  trade window; `fact_pack` and `run_chain` keep today's signatures and the chain takes the windows from the facts (a
  fact may carry them). `wording_check(text_fields, windows)`: `text_fields` is a dict `{"text", "observed": [..],
  "inferred": [..], "invalidation"}`, `windows` a list of `(start_iso, end_iso)` pairs; a code's reason names the code.
  A correction is the item's history, then the item's reply byte for byte as the assistant turn, then ONE user message;
  for a figure it writes the figure as the reply wrote it and each candidate fact id as a whole token. `attached_figures`
  and `corrections` are integers in EVERY row's `input_manifest`. `regrade_rows` keeps its arguments and applies the
  wording rule and the cite-every-figure rule only to a row whose `prompt_version` is `a1-chain/7` or later (older
  stored accounts are re-graded as today). The two user-prompt templates outside the fact lines carry no code either
  (not graded by the checks: pin it in your package test). A fact id written into an item's prose counts as the code it
  contains.
- **Organic trigger:** the first 13:00Z sweep after the deploy; the issuer's read counts the codes in the 26 served
  account items (0 expected), the items stating their two dates (26 expected), the FAIL items and the sum of
  `attached_figures`.

### `RIV-tc-1` -- a top-up close is stored with a currency, and the owed window ends on the page day (CTO half C2 of round 27; ROUND_ANALYSIS.round22 ADDENDUM 6 item 2; CTO ruling R13)
- Measured (round 27 as built, `enrichment_bloomberg._history_owed`): a top-up row is written with `currency` NULL
  (`{"PX_LAST": px, "CRNCY": None}`), and a security that never had a daily pull would have closes and no stored
  currency (the chart draws no curve without one). The leg calls `history_owed.owed(s, date)` with the REPORT date, so
  the window ends one trading day before it and the report date itself is never owed for a security the daily pull
  did not ask (a formerly-held one). `market-range` already has the pattern: `_stored_currencies` first, then ONE
  `_blp_reference_data` request for the single field `CRNCY` for exactly the securities with none, counted in the
  budget before any request.
- Interface (`data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` only, inside the branch the switch opens):
  1. **The window's end.** The leg calls `history_owed.owed(s, page_day)` where `page_day` is the next trading day
     after the report date (`lib.trading_calendar`), so the report date is the newest date a unit can be owed for. In
     `print` and in `ask`.
  2. **Currency, in `ask` only.** For the securities among the units to ask: the stored currency
     (`_stored_currencies`, over the owed window) where one exists; for those with none, ONE `_blp_reference_data`
     request for the single field `CRNCY`, sent through `_blp_call`, BEFORE the history requests. Its points (one per
     security asked) are part of the count passed to `bbg_budget.check_points` (units to ask plus currency lookups) and
     are recorded with `bbg_budget.record("history-owed", <securities asked>, batch_id)`. A top-up row carries the
     currency found, NULL only when the lookup returned none for that security. If the currency request fails, no
     history request is sent, nothing lands, and the line reads `carried <all>` with the failure.
  3. **The printed line** in `ask` gains `; currency lookups <n>` after `asked <a>`; in `print` it gains
     `; currency lookups <n> (not sent)` computed from the stored currencies alone (no request).
  4. `price_date` on every top-up row stays as round 27 built it (the returned trading date; a close for a date not
     asked is not written).
  5. With the switch OFF nothing changes: `tw-1.AC1.py` still ends `PASS 0 failures` (it compares the OFF run with the
     module at commit 361b735308).
  6. **The cap (AMENDMENT 1, Andrew-direct ~17:1xZ via CTO msg 31926, ruling R24).** `HISTORY_OWED_CAP` becomes `20000`
     (an `int`): up to 20,000 units a run, each unit one security on one day, so at most 20,000 returned records. It is the
     only number that changes; `tw-1.AC1.py` arm (e), amended with this order, reads `20000`.
- Rulings at the cut (issuer): `HISTORY_OWED_CAP` is 20,000 by item 6 (ruling R24). Nothing here
  sets the switch: `ask` is set only after this cell is merged and RIV-tw-1's J1 is graded, where the vehicle reads it, in a pair. NOTHING in this cell or its checks calls a vendor: every check and test stubs the client hook and
  points the budget ledger at a temp directory. The cap counts history units only; the currency lookups are counted
  on top of it in the budget check.
- Rulings on the check drafter's questions (issuer): `_stored_currencies` is read from the window's first day THROUGH
  THE REPORT DATE, so a security the daily pull priced in this same run takes its currency from the object just written
  and is never looked up. The `currency lookups <n>` clause is OMITTED when n is 0, in `print` and in `ask` (as
  `misdated` and `failed` are): with both, round 27's `tw-1.AC2.py` still ends `PASS 0 failures` unchanged, and it must.
  The lookup is ONE reference request whose fields are exactly `["CRNCY"]`, recorded by its OWN `bbg_budget.record`
  call; a lookup that was sent and failed is recorded as spent, as `market-range` records it. After a failed lookup the
  line says `asked 0` and `carried <all>` and names the failure; the result dict's shape for that case is yours. Under
  the cap, lookups are counted over the securities of the capped units only. A security the lookup returned no currency
  for is looked up again on a later run (one point each time; stated for the cap's ruling). The read cost of
  `_stored_currencies` over the window is accepted in `ask` and in `print`.
- **Organic trigger:** none while the switch is OFF. THE VEHICLE RUNS THIS FILE FROM THE WORKING TREE: the merge is a
  deploy to the 11:00Z job, lands only after RIV-tw-1's J1 is graded on the 2026-10-09 run, and carries a pair.

## WORKSTREAM 2 (split-adjusted history; the dramatic-move lookup; the trade list scoped to the toggle) -- APPENDED 2026-10-09, revision 1.19 of this file

Issuer `2.0.0_SA_COO~V1` (dell1). Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md`
(1.0.0_SA_CTO~DELL1, msg 1762, @f26ff8fbbc), on Andrew-direct ~05:1xZ
(`deliverables/2.0.0_SA_COO~V1/ANDREW_DIRECT_20261009_051xZ_UI_COMMENTS_TKOMY_CLOSE_AND_TRADE_LIST_SCOPE.md` @9d08dd64d4).
A workstream, not a round: round 28 stays frozen on its three acts. Three cells, three chains, no edge: each cell owns a
disjoint write set and they meet only through two stated contracts (the corporate-action row shape; the chart object's
`adjustment` field). GUARDS on every cell: (1) no deploy and no served write before both round-28 J1 reads (tw-1 at the
2026-10-09 11:00Z vehicle run, aw-1 at the 13:00Z sweep); (2) no edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py`
(a cell that finds it must, files a row and stops); (3) every deploy or served write goes under its own never-widen pair.

### `RIV-wa-1` -- every price series the page draws is adjusted for stored splits, so a split leaves a continuous curve; a big move with no action on file is a gap (WS2-a)
- Measured: on the 2026-10-08 page, IDVZ's chart object holds `TKOMY_US_Equity` points `[2026-10-05, 49.59, m]`,
  `[2026-10-06, 50.5, m]`, `[2026-10-07, 3.33, m]`: Tokio Marine's 15-for-1 split took effect 2026-10-07 (Andrew), and the
  pre-split closes are drawn unadjusted. Gold corporate_actions stores splits as `event_type` `split`, `ratio` = new shares
  per old share (ANET 4.0, PANW 2.0), `ex_date`, `claim` `MEASURED`; `security_id` there is the Bloomberg form with spaces
  (`TKOMY US Equity`), while gold security_market's is underscored (`TKOMY_US_Equity`).
- Interface:
  1. `price_series.series(g4, g1, keys, start, end, actions=None)`: `actions` is a frame in the corporate_actions shape
     (at least `security_id`, `event_type`, `ratio`, `ex_date`, `claim`; `source_url` optional). For a key, every row
     with `event_type` `split` (a reverse split is a ratio below 1) and an `ex_date` inside `(start, end]` divides every
     price dated before the ex-date by its ratio (cumulative over several rows; market and holding-implied points alike).
     Keys match after mapping spaces to underscores. `cash_div` and other event types adjust nothing.
  2. Each key's result gains `"adjustment"`: a list of `{"event_type", "ratio", "ex_date", "claim", "source_url"}`, one per
     applied row, oldest first; `[]` when none. With `actions=None` the points equal today's output, except item 3.
  3. A drawn price more than 3x, or below one third of, the key's previous drawn price (after adjustment), with no applied
     row between them, is not drawn: point `(d, None, None)` and a gap with reason
     `"the price moved more than threefold in one day and no corporate action is on file"`.
  4. `price_series.load(s, keys, start, end)` also reads every object under gold `corporate_actions/date=<D>/` for the
     window's dates (ALL objects there, including WS2-b's `actions-inferred-*` objects) and passes them as `actions`.
  5. `publish_page._build_charts` copies each series' `adjustment` into the chart object's security entry (`"adjustment"`).
     WS2-c renders it; this cell writes no render code.
- Out of bounds: no S3 write, no deploy; `enrichment_bloomberg.py`, `render.py` and `dramatic_move.py` untouched.

### `RIV-wb-1` -- a dramatic move with no action on file is looked up on the web and, when found, stored as an INFERRED corporate-action row (WS2-b)
- Measured: gold corporate_actions date=2026-10-06 and date=2026-10-07 (160 rows each) carry no TKOMY or 8766 row, and no
  date=2026-10-08 object exists. Egress is open except Bloomberg (law 4d77a9c3ea). A SERP client exists:
  `lib/research/management/ceo_search.py` (Bright Data, `BRIGHT_DATA_API_KEY`, `BD_SERP_ZONE`).
- Interface, a new module `data/etfs/scripts/rivalfunds/dramatic_move.py`:
  1. `detect(g4, actions) -> list[dict]`: per security, consecutive stored closes (ascending dates) where the close is
     more than 3x or below one third of the previous one and no `split` or `merger` row of that security has an ex-date in
     `(prior_date, date]`. Each candidate: `security_id`, `date`, `prior_date`, `prior_close`, `close`, `security_name`
     when the frame has one. Keys match across the two forms by mapping spaces to underscores.
  2. `lookup(candidate, search=None) -> dict | None`: builds a query from the security name (or id) and the date (e.g.
     "Tokio Marine Holdings stock split October 2026"), calls `search(query)` -> list of `{title, url, snippet}`, and parses
     an explicit ratio ("15-for-1", "15:1", "1-for-10 reverse", a merger exchange ratio). Found: ONE row in the stored
     corporate_actions shape: `security_id` in the Bloomberg form, `event_type` `split` (or `merger`), `ratio` new-per-old as
     a float, `ex_date` the candidate's date unless the result names another, `claim` `INFERRED`, `source` `web_search`,
     `source_url` the result's URL, `status` `OK`, `row_kind` `event`. Nothing parseable: `None`, never a guessed ratio.
     `search=None` uses the Bright Data SERP the way `ceo_search.py` does (read it; do not edit it).
  3. `write_rows(s, rows, day)` writes one object `address("rivalfunds","etfs","gold","corporate_actions",f"date={day}",
     f"actions-inferred-{revision}.parquet")` through a sink. It is BUILT and tested on a memory sink only: running it
     against live S3 is a served write under guards 1 and 3, not this cell's act.
- Out of bounds: no live search in tests (inject `search`), no S3 write, no deploy, no hookup into the sweep (the issuer adds
  the hookup at the merge); `enrichment_bloomberg.py`, `price_series.py`, `render.py` untouched.

### `RIV-wc-1` -- the security dialog's trade list follows the selected window, behind a closed disclosure; an adjusted series says so (WS2-c)
- Measured: `render.py` writes a fixed heading `HEADP = "<p data-chart-trades-head>Trades in the last 365 days</p>"` and
  `_trade_list`; the page script's `putTrades` fills the list from every marker of the chart object and ignores the range
  toggle (`draw(f,o,rg)`, the `[data-chart-range]` click handler). Andrew: the 365-day list "was not ... asked for if
  you're looking at the 30d Toggle. That should at the very least be behind a dropdown, and it should be scoped for the
  toggle value".
- Interface (`render.py` only, plus its tests):
  1. The list sits inside `<details data-chart-trades-box>` with NO `open` attribute; its `<summary>` is the heading.
     No static text names 365 days.
  2. The page script exposes `window.rfChart.tradehead(rg)` -> `"Trades in the last 30 days"` / `"... 90 days"` /
     `"... 365 days"` for `R30` / `R90` / `R365`, and `window.rfChart.tradelines(markers, from)` -> the trade lines of the
     markers whose `end` is on or after `from` (the window's first day), oldest first, worded as today's `tradelines`.
  3. On every `draw` (first load and every toggle click) the heading and the list are rewritten for the selected window;
     an empty window says `"No trades in the last <n> days."`.
  4. When the chart object's security entry carries a non-empty `adjustment` (WS2-a's field), the dialog shows one muted
     line under the chart: `"Prices before <ex_date> are adjusted for a <ratio>-for-1 split"` (a reverse split as
     `"1-for-<1/ratio> reverse split"`), plus `" (found by web search)"` and the link when `claim` is `INFERRED`.
  5. Existing tests that pin the old heading (`test_r21pl1_strip_and_caption.py`, `test_r18tl1_trade_list_from_markers.py`)
     are updated to the new shape; every other test stays green.
- Out of bounds: no S3, no deploy, no other module.

## WORKSTREAM 3 (the audit's exclusion line; no trade below tolerance or on a repeat day; the header Period bar) -- APPENDED 2026-10-09, revision 1.20 of this file

Issuer `2.0.0_SA_COO~V1`. Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 1
(1.0.0_SA_CTO~DELL1 msg 1852, @a50caca634), on Andrew-direct comments 4-7 (record
`deliverables/2.0.0_SA_COO~V1/ANDREW_DIRECT_20261009_051xZ_UI_COMMENTS_TKOMY_CLOSE_AND_TRADE_LIST_SCOPE.md` @588865eef8).
Item 8 (the Direction Verdict prompt) is WS3's SECOND issuance, cut only after aw-1's J1 read at the 13:00Z sweep. WS3 carries
the three WS2 guards and takes no file a live WS2 order owns: `render.py` belongs to RIV-wc-1, so items 4 and 7 are
`RIV-wc-2`, the next order on wc-1's chain (same worker, after wc-1 is terminal). Two chains: `RIV-wd-1` alone; `RIV-wc-1 -> RIV-wc-2`.

### `RIV-wd-1` -- a share change is a trade only when the share count moved and the trade clears Andrew's 20 bps tolerance; no trade is read across a repeated report (WS3 items 5 and 6)
- Measured: `gold_trade_schedule._pair_rows` infers a holding's trade as `q1 - f * q0`, with `f` the median ratio over the
  window's untouched holdings (`FLOW_WINDOW_EPS` 0.001; `flow_adjusted` true past it). In a window with fund flows an
  UNCHANGED holding therefore reads as a trade. The CGIC audit (latest report 2026-10-06, revision 20261008T122342Z-6ea2fb54eece)
  shows 12 such rows, all "flow adjusted": MediaTek 2454_TT 428,000 -> 428,000 (-1,442; window 09-30 -> 10-02), Renault
  RNO_FP 277,771 -> 277,771 (-936; -2,361 in 09-29 -> 09-30), SMC 6273_JP 10,700 -> 10,700 (-36), Jentech 3653_TT 23,000 ->
  23,000 (-77), Taisei 1801_JP 56,900 -> 56,900 (-192), Aura AUGO_US 46,976 -> 46,976 (-158; -399), Grifols GRFS_US
  120,713 -> 120,713 (-407; -1,026), Tokyo Electron 8035_JP 205,000 -> 205,000 (-1,743). Andrew's tolerance (PRD v0.21
  FWD-10 SOURCE): "at a 20bps tolerance it's immediately clear who is discretionary and who is systematic"; today no code
  applies it. The holdings calendar (`gold_holdings_coverage`) marks 10-01, 10-02, 10-05 and 10-06 `repeat` ("report dated
  <d> re-published") while the 10-02 -> 10-05 and 10-05 -> 10-06 windows carry trades.
- Interface (`gold_trade_schedule.py`, and `gold_holdings_coverage.py` only if item 3 needs it; plus tests):
  1. **Unchanged count, no trade.** A holding whose share count is the same in both reports (`q1 == q0`, both > 0) is NEVER
     a trade, whatever the flow factor; it is not emitted as an add or trim.
  2. **The tolerance.** `TRADE_TOLERANCE_BPS = 20`: a candidate trade whose absolute estimated notional is below 20 bps of the
     fund's total (the later report's) market value is not a trade on the page or in the rankings. It is kept as a row with
     `action` `below_tolerance` (or an equivalent flag the readers skip), counted, so the audit can say how many and the
     numbers stay reconstructible. Entries and full exits are trades whatever their size.
  3. **No trade across a repeated report.** Where the later report of a window is a re-publication of the earlier one (the
     same actual report date, the coverage table's `repeat`), the window yields no trade; and the windows and the calendar
     read the same object, so a day the calendar marks `repeat` never carries a trade. Find which of the two is wrong today
     (state it in the report with the two objects read), and make them agree.
     This item is graded by J1 on the issuer's real run over CGIC's actual windows (no trade on a day the calendar marks
     `repeat`); the check's arm (c) is a control (a re-published report with identical counts yields no trade, at the
     base and after).
  4. Readers that count trades (rankings, buying trend, trade markers) skip the rows items 1-3 exclude; existing tests stay
     green except where they asserted an unchanged-count or sub-tolerance trade (each such change named in the report).
- Out of bounds: no S3 write, no deploy; `render.py`, `price_series.py`, `publish_page.py`, `dramatic_move.py`,
  `enrichment_bloomberg.py` untouched (a reader in one of them that needs changing is a row and the issuer's hookup).

### `RIV-wc-2` -- the audit's exclusion line reads as its own line, naming what it excludes; the header Period bar is gone (WS3 items 4 and 7)
- Measured: `render.py` writes, inside each audit window above the trade table, "<n> money-market line(s) traded: cash
  management, not a holding decision, so not shown as trades (as in the rankings and the trend)." (about lines 392 and 431).
  Andrew read it as naming the trade beneath it ("Tokyo Electron being "excluded" becuse its a cash management operation?").
  The page header carries a PERIOD row (30d / 90d / 365d with their dates) beside the peer-group rows; the ranking panels
  have their own period controls. Andrew: "we do not need this "Period" component in the top of the page anymore".
- Interface (`render.py` and its tests; the next order on wc-1's chain, so it starts from wc-1's merged `render.py`):
  1. The exclusion line names the excluded line(s): the security name (or identifier) and the amount traded, e.g.
     "Left out: 1 money-market line traded (JPMorgan US Government Money Market, $2.1m): cash management, not a holding
     decision." It sits in its own block, visually apart from the trade table (not immediately above the first row), so it
     cannot be read as describing the row beneath it.
     The carrier: the audit window dict gains `cash_equiv_lines`, a list of `{security_key, name, est_notional}`, one per
     excluded money-market line; render from it when present, and from the count alone (as today) when absent. The
     window dict is built in `publish_page.py`, which RIV-wa-1 owns: populating `cash_equiv_lines` there is the issuer's
     hookup at the merge, not this cell's.
  2. The header's PERIOD row is removed from the main page. The ranking panels' period controls and the 30/90/365 data stay.
     No other header row changes; the page keeps exactly ONE inline script.
- Out of bounds: no S3, no deploy, no other module.

### `RIV-we-1` -- a Bloomberg canonical row's report date is the vendor's claimed as-of date; the delivery day is kept as `delivered_on` (WS3 item 6, the repeat-day remedy; CTO ruling ADDENDUM 2 @9f0a957c00, row ETFS_RIVALS-D1-S5) -- APPENDED 2026-10-09, revision 1.21
- Measured: for every CGIC capture 2026-10-02..10-06 the Bloomberg bronze sidecar's `claimed_report_date` is one trading day
  BEFORE the delivery (requested) date (10-05 capture claims 10-02; 10-06 claims 10-05), while
  `gold_canonical_shape.build_bloomberg_rows` stamps `extra_attributes.bloomberg.source_report_date` from the silver row
  (= the delivery date). The calendar (`gold_holdings_coverage`) reads the claim and so marks those days `repeat`; the trade
  windows (`gold_trade_schedule.infer_windows`, RIV-wd-1) read `source_report_date`. Ruled: the claim is the as-of (the
  delivery carries a one-trading-day lag); `source_report_date` takes it.
- Interface (`gold_canonical_shape.py` only, plus tests; NOT loaded by the site-Z vehicle, so no site-Z half):
  1. `build_bloomberg_rows(..., claimed_report_date=None)`: `extra_attributes["bloomberg"]` carries `source_report_date` =
     the claim (ISO), `delivered_on` = the function's `report_date` (the delivery day), `report_date_claim` = `"MEASURED"`.
  2. No claim (None): `source_report_date` = the trading day before `delivered_on` (`lib.trading_calendar`),
     `report_date_claim` = `"INFERRED"`.
  3. The caller (around line 894) passes the claim of the capture it read: the bronze sidecar's
     `claimed_report_date[fund]` for that silver object (the sidecar `_bbg_latest` selected), so every Bloomberg row carries it.
  4. The canonical `report_date` column (the partition / delivery day) is unchanged; only the attributes above move. Existing
     tests stay green except those pinning the old `source_report_date` (each named in the report).
- Out of bounds: `gold_trade_schedule.py`, `gold_holdings_coverage.py`, `render.py`, `publish_page.py`,
  `enrichment_bloomberg.py`; no S3, no deploy. The proof that CGIC's windows move a trading day earlier (and a control fund
  stays byte-equal) is the issuer's real run at the drain; the deploy follows the round-28 J1 reads under its own pair.

### `RIV-we-2` -- a trade window is dated by its reports' AS-OF dates; the delivery days ride along (completes CTO ADDENDUM 2 with RIV-we-1; ADDENDUM 3 @9f0a957c00) -- APPENDED 2026-10-09, revision 1.22
- Measured (2.0.0_SA_COO~V1's real run, ~08:2xZ): with RIV-we-1 merged and canonical_shape rebuilt fresh, every fund's
  trade windows were UNCHANGED (0 dates changed of 164 across 13 funds), because `gold_trade_schedule.infer_windows`
  labels each window with the canonical `report_date` (the delivery day) and reads `source_report_date` only for RIV-wd-1's
  repeat test. The ruling says CGIC's windows move a trading day earlier; that needs the window dates themselves.
- Interface (`gold_trade_schedule.py`, plus tests):
  1. Every trade row's `window_start` / `window_end` are the as-of dates of its two reports: the modal
     `extra_attributes.bloomberg.source_report_date` of each report's rows (`_actual_dates`), falling back to the
     canonical `report_date` where no as-of is carried (issuer and home rows).
  2. Two new columns, `window_start_delivered` / `window_end_delivered`, carry the canonical `report_date`s (the delivery
     days); the G5 schema gains them; recon rows carry the same pair.
  3. A fund whose as-of equals its delivery day is unchanged in every column but the two new ones.
  4. Readers that key on window dates (publish_page's audit windows, trade markers, the buying trend) keep working on the
     as-of dates; the existing tests stay green except those pinning a delivery-day window (each named in the report).
- Out of bounds: `gold_canonical_shape.py`, `render.py`, `publish_page.py`, `price_series.py`, `enrichment_bloomberg.py`;
  no S3, no deploy. The served rebuild of the affected (fund, capture) pairs is the issuer's act under its own pair, after
  the round-28 J1 reads (ADDENDUM 3).

### `RIV-wf-1` -- the holdings calendar classifies a capture against the PREVIOUS capture's claim (new / repeat / regressed); a Bloomberg row's delivered_on is the requested date (CTO ruling ADDENDUM 4, msg 2128; row D1-S7) -- APPENDED 2026-10-09, revision 1.23
- Measured: canonical_shape partitions are the vendor's claimed as-of (date=2026-10-05 holds capture 20261007T110910Z,
  requested 10-06, claims 10-05); the calendar (`gold_holdings_coverage.classify`) compares the claim with the REQUESTED
  day, so CGIC, whose file always lags one trading day, reads `repeat` every day (10-01..10-06) although each capture is a
  new report. RIV-we-1 set `delivered_on` to the partition (the as-of), not the delivery day.
- Interface:
  1. `classify(expected, actual, periodic, prev_actual=None)`: with a previous capture's claim for the same fund and
     source: newer -> `new`, equal -> `repeat`, older -> `regressed`. With none (the first capture), today's rule. `gap`
     (no capture, undated, or dated after the expected day) and `periodic` keep their meaning. `STATUSES` gains `regressed`.
  2. `build_rows` passes each fund-source's previous capture claim, in expected-day order.
  3. `gold_canonical_shape.build_bloomberg_rows(..., requested_date=None)`: `delivered_on` = the capture's requested date
     (the sidecar's `requested_date`, passed by the caller); None -> the partition, as today. Forward-only (no rebuild).
  4. `render.py` `CAL_STATUSES` and `page_theme.py` show `regressed` with its own label and color; the page keeps ONE script.
- Out of bounds: `gold_trade_schedule.py`, `publish_page.py`, `price_series.py`, `enrichment_bloomberg.py`; no S3, no
  deploy (WS2 guards).

### `RIV-wg-1` -- the Direction Verdict leads with what is particular to the fund; a below-tolerance row is never offered to the model as a trade (WS3 item 8; row W26-S1's ai_accounts half) -- APPENDED 2026-10-09, revision 1.24
- Measured: on the served 2026-10-08 page, 13 of 19 distinct Direction Verdicts open "The last thirty days ..."
  (`ws3_item8_prep/verdict_openers_check.py`: FAIL, limit one quarter). Andrew-direct comment 7: "when every single
  fund is saying the same thing, its not very interesting for the reader ... We may need to give more token budget or
  more specific prompting". `P_DIRECTION` (ai_accounts.py ~line 90) asks four questions in a fixed order and SYSTEM caps
  every item at 120-180 words. Row W26-S1: `fact_pack`'s trade facts (~line 170) keep `below_tolerance` rows (RIV-wd-1),
  so on a fixture a below-tolerance row is trade fact T1, ahead of the real buy and sell.
- Interface:
  1. `P_DIRECTION` asks the verdict to OPEN with the single finding most particular to this fund (a named security,
     sector or trade and its fact), and never with a sentence about the periods agreeing or disagreeing in general. The
     verdict's `text` budget is 180-260 words; the 30-day account keeps 120-180.
  2. `wording_check` (or a sibling the chain calls for the `direction_verdict` item only) names a GENERIC OPENING as a
     defect: the text's first sentence begins with a period phrase ("the last thirty days", "the last 30 days", "over the
     last", "these trades", "the trades") followed within its first twelve words by one of "add to", "support",
     "contradict", "borne out", "bear out", "bore out", "confirm"; OR the first sentence begins with the period's dates
     ("From <date> to <date>", "Between <date> and <date>", "Over <date> to <date>") -- the lead the live prompt
     a1-chain/7 produced on 2026-10-09 for both funds of the issuer's two-fund base run (CGIC, IDVZ), and on the
     served 13:00Z sweep for 13 of 13 funds (row D1-S8). The two dates are
     still stated once in `text` (RIV-aw-1), just not as the lead. The ONE correction already in `run_chain` sends it back
     quoting the opening. A generic opening never sets grounding FAIL by itself: after the correction the reply stands.
  3. `fact_pack` drops trade rows whose `action` is `below_tolerance`, as `publish_page` already does for the trade log.
  4. `PROMPT_VERSION` moves to `a1-chain/8`.
- Out of bounds: `publish_page.py`, `render.py`, `gold_trade_schedule.py`, `enrichment_bloomberg.py`; no vendor call, no S3,
  no deploy (WS2 guards). The real-model read is the issuer's, at the drain.
- Checks: `ws3_item8_prep/item8_generic_opener_check.py` (AC1; base FAIL 3 on arms A and C, control arm B PASS) and
  `ws3_item8_prep/w26s1_ai_below_tolerance_check.py` (AC2; base FAIL 1, control arm PASS). J1 (CVO): on the issuer's real
  run over the 13 funds, no opening leads more than a quarter of the verdicts (`verdict_openers_check.py`), and the
  verdicts read as fund-specific.

### `RIV-wh-1` -- no AI fact prints '$0.0 million' or a bare security identifier; a zero notional is never a fact (repair of RIV-aw-1's J1 NOT MET; rows D1-C-S4, D1-S9) -- APPENDED 2026-10-09, revision 1.25
- Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 5 @ceab50de56
  (1.0.0_SA_CTO~DELL1 msg 2497).
- Measured: the served 13:00Z sweep of 2026-10-09 (research_hypotheses-20261009T130227Z-ai, a1-chain/7) carries '$0.0
  million' 7 times (WCMG, ETFT) and the bare CUSIP 037833100 for Apple Inc in GQGU's 30-day account ("The fund added
  037833100 for $8.1 million"; cited row `GQGU|037833100|2026-09-10`). The issuer's a1-chain/8 real run repeats the '$0.0
  million' (WCMG, ETFT, three each). Causes: `_mn` shows millions at one decimal, so any |v| < 50,000 is '$0.0 million';
  `fact_pack` names a trade `names.get(key) or _name(...)`, which falls back to the raw key when no name resolves.
- Interface (all in `ai_accounts.py`):
  1. `_mn(v)`: |v| < 50,000 -> thousands, e.g. '$42 thousand' (whole thousands); |v| >= 50,000 -> millions at one
     decimal, as today. The facts' `display:` form follows, so the model copies it (SYSTEM rule 1 allows the display form).
  2. `fact_pack` leaves out a trade whose notional is exactly 0 (never '$0 thousand').
  3. `fact_pack` never puts a bare identifier (the raw `security_key` or `security_id`) in a fact's text: the name comes
     from `names`, then the row's own name field(s) if the trade row carries one, then any name the function can already
     reach for that security; a trade with no name left is left out of the facts.
  4. SYSTEM rule 1 names the thousands form beside the millions form.
- Out of bounds: every other file; no vendor call, no S3, no deploy. The real-model read is the issuer's, at the drain.
- Check: `ws3_item8_prep/wh1_small_notional_and_unnamed_check.py` (AC1; base FAIL 4; the EDGE negative arm and the NAMED
  control PASS). J1 (CVO): on the issuer's real 13-fund run, 0 '$0.0 million' and 0 bare identifiers in any item.

### `RIV-wi-1` -- the 13:00Z sweep runs the dramatic-move lookup before publish, so a split found on the web adjusts the served history (row D1-S10; CTO ruling ADDENDUM 6) -- APPENDED 2026-10-09, revision 1.26
- Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 6 @04214e638c
  (1.0.0_SA_CTO~DELL1 msg 2508). Its own cell and its own deploy pair; WS2/WS3 ship first.
- Measured (row D1-S10 @0d4f7cc409): no Lambda calls `dramatic_move`; no Lambda carries `BRIGHT_DATA_API_KEY`;
  `rivalfunds_package.STAGED` (7 paths) does not stage `data/find/dualbiz/scripts/serp.py`, and `serp_search` finds it
  only at the repository layout (`pathlib.Path(__file__).resolve().parents[4]`). `price_series._actions` READS gold
  `corporate_actions`; `dramatic_move.write_rows` is its only writer. Andrew-direct comment 1: "there should be a google
  search for corporate action and an automatic refactoring of historical prices by the split multiple".
- Interface:
  1. `dramatic_move.run_for_day(day, sink, *, g4=None, actions=None, search=None, cap=MAX_LOOKUPS_PER_RUN, names=None)
     -> dict`. With `g4`/`actions` None it reads the stored closes (G4) and the stored corporate actions from `sink` for
     the 30 days before `day`; it runs `detect`, searches at most `cap` candidates (`lookup`), writes every find with
     `write_rows` (one object, source_url per row), and returns a report `{candidates, searched, calls, written, failed,
     capped, uri}`. It PRINTS one line naming the cap and the counts. A search that raises is counted in `failed` and the
     run goes on; `run_for_day` itself never raises for a search or write failure. A name with no discontinuity draws 0
     searches. `MAX_LOOKUPS_PER_RUN` is a module constant (8).
  2. `sweep.run_sweep` calls `dramatic_move.run_for_day(date, sink)` after the canonical / trade-schedule stages and
     before the day's publish, inside a `try` that records the failure and does not re-raise (a failed lookup never
     blocks publish; the price stays unadjusted and the chart's gap flag stays).
  3. The key: `serp_search` takes `BRIGHT_DATA_API_KEY` from the environment, else reads the Secrets Manager secret named
     by `RIVALFUNDS_SERP_SECRET` (one `GetSecretValue`, cached per process). With neither, the search raises (counted as
     failed by item 1).
  4. `infra/aws/lambda/etfs-pipeline/rivalfunds_package.py` `STAGED` stages `data/find/dualbiz/scripts/serp.py`, and
     `serp_search` finds it in a Lambda tree (a `_serp_dir()` that tries the staged destination first, then the
     repository layout).
- Out of bounds: Terraform, IAM, the Lambda environment and any deploy (the deploy pair's applier sets
  `RIVALFUNDS_SERP_SECRET` and the one-ARN read); `price_series.py`, `publish_page.py`, `render.py`,
  `enrichment_bloomberg.py`; no live search, no S3.
- Checks: `ws3_item8_prep/wi1_lookup_run_check.py` (AC1; base FAIL: run_for_day absent) and
  `ws3_item8_prep/wi1_wiring_check.py` (AC2; base FAIL 3). Acceptance (the pair's read, CTO ADDENDUM 6): Tokio Marine
  adjusted on the served page; a name with no discontinuity makes 0 calls.

### `RIV-wj-1` -- the generated stack grants the daily Lambda ONE read of the existing Bright Data key secret and names it in that Lambda's environment (CTO ruling ADDENDUM 7; RIV-wi-1's grant) -- APPENDED 2026-10-09, revision 1.27
- Placement: `ledger/CTO_RULING_WORKSTREAM2_SPLIT_ADJUST_TRADE_LIST_SCOPE_20261009.md` ADDENDUM 7 @aa290d707e
  (1.0.0_SA_CTO~DELL1 msg 2555): option (a) -- GetSecretValue on exactly
  `arn:aws:secretsmanager:us-east-1:313476888478:secret:find-insure/bright-data/api-key-7ojPkd`, no wildcard, no other
  action, no copy of the secret; `BD_SERP_ZONE` stays plain environment; the generated policy diff shows ONE new
  statement. Row D1-S11 tells FIND_INSURE's owner of the second consumer.
- Measured (14:2xZ, key names only): the SERP key is `find-insure/bright-data/api-key` (a raw string);
  `find-dualbiz/bright-data/serp` names it as `api_key_secret` and gives `zone` = `serp_opal`. RIV-wi-1 (merged
  @e17ab4e69d) reads the key from `BRIGHT_DATA_API_KEY`, else from the secret named by `RIVALFUNDS_SERP_SECRET`, and the
  zone from `BD_SERP_ZONE`. The stack's one existing secrets grant is the OpenAI secret (`gen_policies._ai_secret`,
  statement `GetOpenAISecret`, the daily Lambda's environment `RIVALFUNDS_AI_ENABLE`, `RIVALFUNDS_OPENAI_SECRET`).
- Interface (`infra/aws/terraform/etfs-rivalfunds/gen_policies.py` and its committed outputs):
  1. A constant for the ONE ARN with a comment citing ADDENDUM 7 (a foreign secret has no builder home; R19: this existing
     pipeline is not migrated by this cell).
  2. For the sweep stage (the daily Lambda) only: one more statement, `Sid` `GetSerpSecret`, `Effect` `Allow`, `Action`
     `["secretsmanager:GetSecretValue"]`, `Resource` `[<the ARN>]`; and the environment gains `RIVALFUNDS_SERP_SECRET` =
     the ARN and `BD_SERP_ZONE` = `serp_opal`, keeping its two keys.
  3. The committed `generated.auto.tfvars.json` and `policies/*.json` are regenerated with `--out
     infra/aws/terraform/etfs-rivalfunds` and equal a fresh regeneration (line endings aside).
- Out of bounds: every `.tf` file, every other Lambda, any `terraform plan` or `apply`, any AWS call; the rivalfunds code.
- Check: `ws3_item8_prep/wj1_serp_grant_check.py` (AC1; base FAIL 2: limbs (1) and (3); limbs (2) and (4) PASS at the
  base and must keep passing).

### `RIV-wk-1` -- a stored corporate-action row can be VOIDED without a delete: an append-only void object, written by a CLI, that `price_series` honours (CTO half condition 11 of the lookup deploy) -- APPENDED 2026-10-09, revision 1.28
- Placement: `1.0.0_SA_CTO~DELL1`'s half of the lookup deploy pair,
  `deliverables/1.0.0_SA_CTO~DELL1/round28/NEVER_WIDEN_HALF_CTO_WI1_LOOKUP_DEPLOY.md` @63bdddfbb9 (msg 2581), condition
  11: the COO half's rollback of a wrong `corporate_actions` row rested on an S3 delete, which no seat may do; "No void
  path, no apply."
- Measured: `price_series._actions(s, lo, hi)` (~line 216) concatenates EVERY `.parquet` under
  `gold/corporate_actions/date=<D>/` for D in [lo, hi]; `_adjustments` (~128) applies each `split` row. The inferred rows
  (`dramatic_move._row` ~249, `write_rows` ~330) carry `security_id`, `event_type`, `ratio`, `ex_date`, `source_url` and the
  object's `revision` (stamped by `write_rows`). There is no void path: a wrong row adjusts forever.
- Interface:
  1. `dramatic_move.void_rows(s, revision, security_id, reason, day=None) -> uri`: writes ONE new object
     `actions-void-<rev>.parquet` under `gold/corporate_actions/date=<day or today UTC>/` with one row per voided action:
     `void_revision`, `security_id`, `reason`, `voided_at`, `producer_version`. Append-only; it never rewrites or deletes.
  2. A CLI: `python -m rivalfunds.dramatic_move void --sink <s3 | local:<dir>> --revision <rev> --security-id <sid>
     --reason <text> [--day <D>]`, exit 0 on a written void, non-zero with a message when no stored action row matches
     (`revision`, `security_id`).
  3. `price_series._actions` reads `actions-void-*` objects separately (never as action rows) and drops every action row
     whose (`revision`, `security_id`) a void names, over all dates. A void for an unknown row changes nothing.
- Out of bounds: `sweep.py`, `publish_page.py`, `render.py`, `gen_policies.py`, every infra path; no S3, no search, no
  deploy. The void CLI is never run against S3 by this cell.
- Check: `ws3_item8_prep/wk1_void_check.py` (AC1; base FAIL 2 -- arms B and C; arm A, both rows adjusting before any void,
  PASSES at the base and must keep passing).

## ROUND 29 (the round-28 analysis's enrichment list) -- APPENDED 2026-10-12, revision 1.29 of this file

Input: `ledger/ROUND_ANALYSIS.round28.md` (1.0.0_SA_CTO~DELL1, msg 4558); the CVO's slug msg 4557 @995a0646f4; this seat's close
packet `deliverables/2.0.0_SA_COO~V1/round28/ROUND28_GRADED_READS_PACKET.md` @55a689301c. PRD v0.21 (ADMITTED); no FWD moves.

Cut this round: RIV-xa-1, RIV-xb-1, RIV-xc-1, RIV-xd-1 (section 3 items 1, 2, 4, 5). Not cut, with the reason:
- item 3 (aw-1's re-read on the next sweep): a READ of the 2026-10-13 13:00Z page, not a cell; a cell only if NOT MET.
- item 6 (the trading-day gate on the enrichment leg; C-S85's clock advance): STAGED for site Z, un-park 2026-10-14 06:00Z;
  `enrichment_bloomberg.py` is the vehicle's file and the deploy is site Z's under `1.0.0_SA_CTO~Z`'s half.
- item 7 (the queue-state READER cell, row D1-S2, and the switch-on): carried by the analysis. Its precondition is now MET
  (the state address is builder output in `MDPF_DEMQUE/requests/ETFS_RIVALS-HISTORY-OWED-DAILY.json`, the writer DQ-t-16 is
  complete); it edits the same vehicle file as item 6 and deploys in the same pair, so it is held for that window: asked of
  the CTO in the issuance report.

Chains (M = 3): A = RIV-xb-1 then RIV-xd-1 (one file, `dramatic_move.py`: a write-set serialization, not a data edge),
B = RIV-xa-1 (`render.py`), C = RIV-xc-1 (`ai_accounts.py`). Write sets are otherwise disjoint; each cell adds one new test
file. Checks: `deliverables/2.0.0_SA_COO~V1/round29/checks/`, dry-run at the base before the cut (xa1 FAIL 2, xb1 FAIL 6,
xc1 FAIL 4, xd1 FAIL 2 with its control PASS).

### `RIV-xa-1` -- the audit page states its calendar's day axis in VISIBLE text (round 28 analysis section 2.1; RIV-wd-1's repeat clause NOT MET) -- APPENDED 2026-10-12, revision 1.29
- Placement: `ledger/ROUND_ANALYSIS.round28.md` section 2.1 and section 3 item 1 (1.0.0_SA_CTO~DELL1 msg 4558); CVO ADDENDUM 14
  @9d49b613e9, row D1-C-S15.
- Measured (the 2026-10-12 `audit.html`, 13 fund sections): BIDD, CGIC and SCHY each carry a trade window ending 2026-10-02
  (2, 16 and 4 trades) beside a 10-02 calendar cell marked `repeat`. The calendar's day axis (`data-day`, the column header
  `MM-DD`) is the day a report was EXPECTED; the report's own date is in each cell's hover `title` ("report dated ...") only.
  The visible text never names it: the legend paragraph (`render.py:2469`) reads "Calendar legend: new / repeat / regressed
  (older than the previous report) / gap / periodic per day; BBG = Bloomberg, ISS = issuer, HOME = home producer."
- Interface: in `render._render_audit_body`, the legend paragraph gains, after "HOME = home producer.", ONE space and exactly
  this sentence (ASCII; the apostrophe is U+0027): `Each calendar column is the day a holdings report was expected; a cell reads repeat when the report received that day is the same holdings window as the previous report. Trade windows are dated by the report's own date, so a window can end on a day this calendar marks repeat.` It stays in the same `<p class="muted">`. The cell markup,
  the hover titles, the statuses and every other word of the page are unchanged.
- Out of bounds: `render._calendar`, `gold_holdings_coverage.py`, `publish_page.py`, the page's main document, any status
  rule (the classification of repeat is not touched).
- Checks: `round29/checks/xa1_axis_line_check.py` (AC1 and AC2; base FAIL 2). J1 (the CVO's): on the next published audit
  page the sentence reads beside the calendar for BIDD, CGIC and SCHY.

### `RIV-xb-1` -- the lookup's search retries a vendor 5xx or a transport failure, at most twice with backoff, never a 4xx (round 28 analysis section 2.2) -- APPENDED 2026-10-12, revision 1.29
- Placement: `ledger/ROUND_ANALYSIS.round28.md` section 2.2 and section 3 item 2 (msg 4558).
- Measured (2026-10-12, zone `serp_opal`, this seat's `WI1_SCRATCH_WALK_20261012.md`): 5 of 9 Bright Data searches failed (4
  `VENDOR`: HTTP 200 with `x-brd-status-code` 502, `brd_error_code` `expect_element`; 1 `TRANSPORT`); the same query failed
  once and succeeded once. `serp.classify_serp_attempt` classes a failure `VENDOR` (5xx or a vendor-error header),
  `TRANSPORT` (no HTTP status or a connection error) or `CONFIG` (a 4xx). `dramatic_move.serp_search` (about line 341) makes
  ONE call and raises `RuntimeError("SERP FAILED: <kind>")`; `run_for_day` counts that as `failed` and the candidate waits for
  the next walk.
- Interface: `dramatic_move.serp_search(query, *, _call=None, _sleep=None) -> list[dict]`. `_call(query)` defaults to the
  current body (key lookup, the staged `serp` import, `serp_module.serp_brightdata_records(query, max_pages=1, gl="us",
  hl="en")` returning its dict); `_sleep` defaults to `time.sleep`. With `_call` given the key lookup and the import are
  skipped. Policy: a result with `status` `FAILED` and `failure.kind` in (`VENDOR`, `TRANSPORT`) is retried, at most 2
  retries (3 attempts), sleeping 1.0 then 2.0 seconds between attempts; a `CONFIG` or any other kind is raised at once;
  the first OK result is returned in the same `[{title, url, snippet}]` shape as today. The final failure raises
  `RuntimeError` whose message names the class, the attempts and the vendor's own words, in the form
  `SERP FAILED: <kind> after <n> attempts: <brd_error_code> <brd_error>` (`1 attempt` for a CONFIG).
- Out of bounds: `serp.py` (the staged vendor client), `lookup`, `detect`, the cap, `write_rows`, `sweep.py`, any key or
  environment change; no live search.
- AMENDMENT 1 (issuer, 2026-10-12, on worker row D1-W35-S2): a `VENDOR` failure whose `brd_error_code` is `captcha` is NOT retried
  here; the staged client already retries a captcha and a 5xx itself (`serp.py:459-461`), so an outer retry would turn one
  search into up to 9 requests. It raises after one attempt. AC1's check gains one arm (7 tests).
- Checks: `round29/checks/xb1_retry_check.py` (AC1; base FAIL 6 -- the call has no `_call`) and the existing lookup tests
  (AC2: must stay green). J1 is not set: a retry is read in the next sweep's `failed` count when a candidate exists.

### `RIV-xc-1` -- no two funds' Direction Verdict openings share a name-abstracted frame on one page (round 28 analysis section 2.7; the CVO's round-29 item at ADDENDUM 4) -- APPENDED 2026-10-12, revision 1.29
- Placement: `ledger/ROUND_ANALYSIS.round28.md` section 2.7 and section 3 item 4 (msg 4558); CVO ADDENDUM 4 (row D1-C-S5).
- Measured (the 2026-10-12 page, `sweep_read.py`): 13 Direction Verdict openings; the CVO's own measure found 6 of 13 sharing a
  name-abstracted frame ("<name> is the clearest fund-specific tell: ..." is the common one). `ai_accounts.opening_check`
  (RIV-wg-1) tests one opening alone (a generic period phrase); no code compares openings ACROSS funds. `run_chain` (one fund,
  two chats and at most one correction per item) is called once per fund by `run_day`, in a loop with no shared state.
- Interface (`data/etfs/scripts/rivalfunds/ai_accounts.py` only; `PROMPT_VERSION` stays `a1-chain/8`; no prompt text changes):
  1. `frame_of(text) -> str`: take the first sentence (split as `opening_check` does, at the first sentence-final `.`, `!` or
     `?` followed by whitespace); tokenise on whitespace; strip any of `,;.!?"'()` from both ends of a token (keep `:`); a
     token containing a digit is `<n>`; a token that begins with an uppercase letter and is not one of the sentence-initial
     words `the a an in on over from between these this its it for with as at by` is NAME-like, and a maximal run of NAME-like
     tokens (a connector token `&`, `-`, `of`, `de` or `and` counts inside a run when a NAME-like token follows it) is ONE
     `<name>`; consecutive `<n>` collapse to one; lowercase everything else; the frame is the first FIVE resulting tokens
     joined by single spaces (fewer if fewer). `frame_of("")` is `""`. Examples that must hold: "Alpha Co is the clearest
     fund-specific tell: it was bought." and "Beta Corp is the clearest fund-specific tell: it was sold." both give
     `<name> is the clearest fund-specific`; "Alpha Co is the clearest tell: it was bought." gives `<name> is the clearest
     tell:`; "Alpha Co added $2.7 million over 2026-09-01 to 2026-09-30." gives `<name> added <n> million over`.
  2. `run_chain(..., seen_frames: dict | None = None)`: when given, a `direction_verdict` item whose `frame_of(text)` is already
     a key of `seen_frames` (frame -> the fund id that first used it) gets ONE more defect in the item's existing
     `opening` list, so the chain's existing one-correction path sends it back once and the corrected reply replaces it and is
     graded as today: `the opening shares its frame "<frame>" with <fund>'s verdict on this page: open with the single finding
     most particular to this fund, in different words from that opening`. After the final reply, `seen_frames.setdefault(
     frame_of(final text), fund_id)` (a non-empty frame only). With `seen_frames` None nothing changes.
  3. `run_day` creates ONE `seen_frames = {}` before its fund loop and passes it to every `run_chain` call (in the universe's
     order), including the retry attempt.
- Out of bounds: every prompt constant, `opening_check`, `grounding_check`, `wording_check`, `ai_stage.py`, `sweep.py`, any vendor
  call (a stub client only), `PROMPT_VERSION`.
- Checks: `round29/checks/xc1_frame_check.py` (AC1; base FAIL 4) and the existing AI tests (AC2: must stay green). J1 (the
  CVO's): on the next sweep page no two openings share a frame by the CVO's own measure, or a correction is on the record for
  each that did.

### `RIV-xd-1` -- a move the lookup finds is adjusted on the page of the SAME day, shown by an offline render of a planted discontinuity (round 28 analysis section 2.8) -- APPENDED 2026-10-12, revision 1.29
- Placement: `ledger/ROUND_ANALYSIS.round28.md` section 2.8 and section 3 item 5 (msg 4558); CVO ADDENDUM 12 (row D1-C-S13).
- Measured (this seat, `WI1_SCRATCH_WALK_20261012.md` and the dry-run of the check below): `sweep.run_dag` calls
  `dramatic_move.run_for_day(day, sink)` with `day` = the page day; `run_for_day` writes the find with `write_rows(s, rows,
  day)`, so the object lands in `gold/corporate_actions/date=<page day>/`; but the page's charts read the series with
  `price_series.load(s, keys, lo, asof)` where `asof = gold_holding_contribution.as_of(day)` (the previous trading day), and
  `_actions` reads only partitions `lo <= date <= asof`. A find on page day D is therefore invisible to page D's chart and
  appears one trading day late. Measured: the same row read with a window ending 2026-10-07 gives `adjustment == []`, ending
  2026-10-12 gives the INFERRED split.
- Interface: `dramatic_move.run_for_day` writes with the partition day `gold_holding_contribution.as_of(day)` instead of
  `day` (`uri = write_rows(s, rows, <as_of(day)>)`); every other behaviour is unchanged: the candidate window (30 days up to
  `day`, which includes that partition), the report, the printed line, the idempotence (a second run reads the stored row
  and searches nothing). Where an existing test pins the partition date of a lookup row, change that assertion to the
  as-of date and say so in the report.
- Out of bounds: `price_series.py`, `publish_page.py`, `render.py`, `sweep.py`, `write_rows`'s own signature, `void_rows`,
  everything the retry cell (RIV-xb-1) changes in `serp_search` (it lands first, on the same file: yours is the one call
  site); no S3, no live search.
- Checks: `round29/checks/xd1_planted_render_check.py` (AC1 and AC2; base FAIL 2, its control PASSES at the base and must
  keep passing). The organic case (no name with a discontinuity) is the negative arm, read when it occurs.

- APPLY LEG (round-less executor order, not a cell; 2026-10-12, issuer): `TO-APPLY-R29.rivalfunds-packages-deploy-dell1` deploys the four cells'
  code to the rivalfunds packages at pin de3c6bf211 under the signed pair (COO @ff7e96adf6, CTO `ledger/NEVER_WIDEN_ROUND29_DEPLOY_CTO_HALF.md`);
  window ruled by the CTO: after the 2026-10-13 13:00Z sweep is read. It adds no cell and changes no criterion.

## ROUND 30 (main workstream, the round-29 analysis's two recuts) -- APPENDED 2026-10-14, revision 1.30 of this file

Input: `ledger/ROUND_ANALYSIS.round29.md` @cb3614782c (1.0.0_SA_CTO~DELL1, msg 5567); the CVO's slug msg 5565 and
`surprise-channel/adjudications/ADJUDICATION_v2.dell1.md` @ceffeac94e (rows D1-C-S19 and D1-C-S20, both NOT MET on the cut, not the
workers); this seat's packet `deliverables/2.0.0_SA_COO~V1/round29/ROUND29_CLOSE_PACKET.md` @76190e0167. PRD v0.21 (ADMITTED); no FWD moves.
`round-close-check --round 29` reads MAY-CLOSE (4 of 4 orders, 2 of 2 J1 graded, 0 self-graded).

Cut this round (workstream `page`): RIV-xa-2 and RIV-xc-2 (section 3 items 1 and 2). Chains (M = 2): A = RIV-xa-2 (`render.py`), B = RIV-xc-2
(`ai_accounts.py` and its own test file). Write sets are disjoint; no edge. Checks: `deliverables/2.0.0_SA_COO~V1/round30/checks/`, dry-run at
the base before the cut (xa2 FAIL 2, xc2 FAIL 2).

Not cut in THIS issuance, with the reason (analysis section 3 item 3, "carried, unchanged"): the site-Z producer cells RIV-xe-1 (trading-day gate
and queue-state reader), RIV-xe-2 (Z3 dividends and the field-matched owed request, C1) and RIV-xf-1 (Z4 ACWI and IWM). Their write surface
(`enrichment_bloomberg.py`, `history_owed.py`, `universe.py`, `collector_bloomberg.py`) is disjoint from this issuance's, so they are workstream
`sz` of round 30, issued by this same seat as its own issuance once three prerequisites are done: the consumer read for xe-2's never-widen question
(how G3 readers treat a date partition), the `owed_size.py` re-read, and the check files dry-run at the base. Staged spec:
`deliverables/2.0.0_SA_COO~V1/round30_prep/STAGED_CELL_enrichment_trading_gate_and_queue_reader.md`. Z-S81 goes to its owner as the analysis rules; it is not a cell.

### `RIV-xa-2` -- the audit page's day-axis sentence sits beside EVERY calendar, inside each fund's own article (round-29 analysis ruling 1; row D1-C-S19; recut of RIV-xa-1) -- APPENDED 2026-10-14, revision 1.30
- Placement: `ledger/ROUND_ANALYSIS.round29.md` section 2 ruling 1 and section 3 item 1 (msg 5567); CVO row D1-C-S19.
- Measured (the 2026-10-14 13:00Z page): the sentence is on the page once, in the trades-section legend (`render.py:2471`); the BIDD, CGIC and SCHY
  calendars render 13,384, 19,461 and 20,425 px below it, so with a calendar centred the legend is out of view (3 of 3). Round 28's ruling 2.1 asked
  for the sentence "next to the calendar"; RIV-xa-1 put `render._calendar` out of bounds, so the fault was the cut.
- Interface (`data/etfs/scripts/rivalfunds/render.py` only): a module constant `CALENDAR_AXIS_SENTENCE` holds the sentence EXACTLY as the legend
  carries it today (ASCII; the apostrophe is U+0027): `Each calendar column is the day a holdings report was expected; a cell reads repeat when the
  report received that day is the same holdings window as the previous report. Trade windows are dated by the report's own date, so a window can end
  on a day this calendar marks repeat.` The legend paragraph reads it from the constant and its bytes do not change. `render._calendar(f)`, when it
  renders the calendar table (the `ok` status), returns `<p class="muted" data-calendar-axis>` + the sentence (HTML-escaped as the file's `_e` does) +
  `</p>` IMMEDIATELY BEFORE `<div class="calwrap">`, with nothing between them. When `f.get("calendar")` is empty (the `unavailable` status) `_calendar` is
  unchanged: no sentence, because no calendar renders. The cell markup, hover titles, statuses and every other word of the page are unchanged.
- Out of bounds: the legend's other words, any status rule, `_trades`, `gold_holdings_coverage.py`, `publish_page.py`, every file but `render.py`
  and the cell's one new test file.
- Checks: `round30/checks/xa2_axis_beside_calendar_check.py` (AC1 and AC2; base FAIL 2). J1 (the CVO's): on the served audit page at the production URL
  (not a local render) after the deploy and the next 13:00Z sweep, the BIDD, CGIC and SCHY calendars each have the sentence visible in the same
  viewport as the calendar when the calendar is centred (3 of 3).

### `RIV-xc-2` -- the frame instrument compares FAMILIES, and a correction's reason is stored (round-29 analysis ruling 2; row D1-C-S20; recut of RIV-xc-1) -- APPENDED 2026-10-14, revision 1.30
- Placement: `ledger/ROUND_ANALYSIS.round29.md` section 2 ruling 2 and section 3 item 2 (msg 5567); CVO row D1-C-S20.
- Measured (the 2026-10-14 page): repetition fell from 5 of 13 to 2 of 13, but IDVZ ("is the clearest fund-specific tell") and TXUE ("is the clearest
  tell") share one frame family with 0 corrections: `frame_of`'s five-token window splits them at token 5, so the code's own instrument passed what a
  reader sees as one frame. `input_manifest` recorded no correction reason.
- Interface (`data/etfs/scripts/rivalfunds/ai_accounts.py` only; `PROMPT_VERSION` stays `a1-chain/8`; no prompt text changes): `frame_of` v2.
  1. Steps as v1 up to the token list: first sentence (split at the first `.`, `!` or `?` followed by whitespace), whitespace tokens, each stripped of
     `,;.!?"'()` at both ends (`:` kept), a digit token is `<n>` (consecutive `<n>` collapse), a run of name-like tokens is one `<name>`, the rest lowercased.
  2. THE CLAUSE: the tokens up to and including the first whose raw form ends in `:`; with none, the whole first sentence.
  3. THE STOP-LIST: a module constant `FRAME_STOP = frozenset(("fund-specific", "most", "single", "particular"))`; those tokens are removed from the clause.
     `clearest` is not in it: it stays as the head word. (The stop-list is data in the cell; its denominator is the 13 openings of the 2026-10-14 page,
     two of which the planted pair reproduces.)
  4. The frame is the first EIGHT tokens of the clause, joined by single spaces. `frame_of("")` is `""`.
  Examples that must hold (the check pins them): "Alpha Co is the clearest fund-specific tell: it was bought. More." and "Beta Corp is the clearest tell:
  it was sold." both give `<name> is the clearest tell:`; "Gamma Co stands out most: it was sold." gives `<name> stands out:`; "Alpha Co added $2.7 million
  over 2026-09-01 to 2026-09-30." gives `<name> added <n> million over <n> to <n>`.
  5. `run_chain`: when a direction verdict's first reply shares its frame (the existing `seen_frames` path, unchanged: ONE correction through the chain's
     existing path), the item's `input_manifest` gains `"shared_frame_with": "<fund>"` (the fund that first used the frame), whether or not the correction
     succeeded. A reply that STILL shares the family after the one correction is marked, not re-sent: its manifest also gains `"frame_still_shared": true`.
     A first fund, a distinct frame and an `activity_30d` row carry neither key. First fund wins the `seen_frames` record, as today.
- Out of bounds: every prompt constant, `opening_check`, `grounding_check`, `wording_check`, `ai_stage.py`, `sweep.py`, any vendor call (a stub client only),
  `PROMPT_VERSION`. The round-29 check `round29/checks/xc1_frame_check.py` is SUPERSEDED by this cell's check (its AC1 pins the v1 frame) and is not run.
- Checks: `round30/checks/xc2_frame_family_check.py` (AC1 the families and the planted IDVZ/TXUE pair reading SAME, with its control; AC2 the stored
  reason and the marking; base FAIL 2) and the AI tests including `tests/test_riv_xc1_verdict_frame.py`, which the worker REWRITES to the v2 rule (AC3: must
  be green). J1 (the CVO's): on the next sweep page 13 of 13 openings fall in distinct families by the normalized `frame_of`, or each shared one carries a stored
  correction reason.

## ROUND 30, workstream `sz` (the site-Z producer and its reader) -- APPENDED 2026-10-14, revision 1.31 of this file

Input: the same analysis `ledger/ROUND_ANALYSIS.round29.md` @cb3614782c section 3 item 3 ("carried, unchanged") and the CTO's msgs 4568, 4932, 4969, 5166, 5197 and 5577; this seat's consumer read
`deliverables/2.0.0_SA_COO~V1/round30_prep/XE2_CONSUMER_READ_G3_PARTITIONS_20261014.md` @8c6eab1456 (it found that `gold_trade_schedule.load_actions` keeps only a security's latest pull, so Z3's incremental pull needs a union reader first;
the CTO accepted, msg 5577, and named the rule). Workstream `sz` is the second workstream of round 30: its write surface is disjoint from workstream 4's (`render.py`, `ai_accounts.py`), so it is its own issuance by the same seat.

Cut in this issuance: RIV-xe-3, RIV-xe-1, RIV-xf-1. Chains (M = 3): A = RIV-xe-1 (`enrichment_bloomberg.py`; RIV-xe-2 follows it on the same file), B = RIV-xe-3 (`gold_trade_schedule.py`), C = RIV-xf-1 (`peer_groups.json`, `bbg_budget.json`
and three tests). Write sets are disjoint; no edge among the three. Checks: `deliverables/2.0.0_SA_COO~V1/round30/checks/`, dry-run at the base before the cut (xe3 FAIL 3 with its empty-store control PASS; xe1 FAIL 10 with one control PASS; xf1 FAIL 5 with
its all-gates-off control PASS).

NOT cut in this issuance, with the reason: RIV-xe-2 (Z3: dividends incremental and the field-matched owed request, C1) waits on RIV-xe-3 DEPLOYED and read once (CTO msg 5577) and follows RIV-xe-1 on the same file; it is cut when both are in. The deploys of xe-1, xe-2 and xf-1
are site Z's under `1.0.0_SA_CTO~Z`'s half and of xe-3 a Lambda deploy under its own pair, each by a CloudOps seat; none is a worker's act.

### `RIV-xe-3` -- `gold_trade_schedule.load_actions` reads the UNION of every pull's actions per security, so a short incremental pull keeps every older action (CTO msg 5577; the precondition of RIV-xe-2) -- APPENDED 2026-10-14, revision 1.31
- Placement: this seat's consumer read `round30_prep/XE2_CONSUMER_READ_G3_PARTITIONS_20261014.md` @8c6eab1456; CTO ruling msg 5577 (REC accepted): "the UNION of every pull's
  actions per security, de-duplicated on the action's own key, with the latest pull winning on a key collision"; `xe-2` waits on this cell deployed and read once.
- Measured (code at box/dell1 HEAD): `gold_trade_schedule.load_actions` (`gold_trade_schedule.py:983-994`) concatenates every `corporate_actions` object and keeps, per
  `security_id`, only the rows of its LATEST pull (`as_of|revision` greatest). Today that is a full snapshot (every pull asks 730 days); a short incremental pull (RIV-xe-2) would
  become a security's latest pull and drop its older actions from G5 (moved served output). `price_series._actions` and `dramatic_move` already read the union.
- Interface (`data/etfs/scripts/rivalfunds/gold_trade_schedule.py`, `load_actions` only; its signature and return triple are unchanged): an EVENT row (`row_kind == "event"`) is kept
  from EVERY pull; its key is (`security_id`, `event_type`, `raw_event_type`, `ex_date`), a column the frame lacks reading as the empty string; of several rows with one key the row of the
  greatest (`as_of`, `revision`) pull is kept. A STATUS row (`row_kind == "status"`) follows the rule as it was: kept only when it belongs to the security's LATEST pull. The label is the
  `+`-joined sorted revisions of the rows returned; an empty store returns `(None, None, [])`.
- Out of bounds: every other function of the file, `sweep.py`, `price_series.py`, `dramatic_move.py`, the G5 schema and every stage output; no S3 read (a local sink only).
- Checks: `round30/checks/xe3_union_reader_check.py` (AC1 the short pull keeps the older actions; AC2 one action in two pulls appears once with the latest pull's values; AC3 status rows follow the
  old rule, a full-snapshot store reads as before, an empty store returns the old triple; base FAIL 3, the empty-store control PASS). The live-store arm (the new reader's G5 output equals today's,
  DELTA = 0, read-only, BEFORE any deploy) is the issuer's drain act, not a worker criterion. J1: none (a LOCAL cell; the Lambda deploy goes under its own pair).
- AMENDMENT 1 (2026-10-14, issuer 2.0.0_SA_COO~V1, on the worker's row ETFS_RIVALS-D1-W40-S1, ARMED): `load_actions` honours the void records exactly as `price_series._actions` does. An object under
  `corporate_actions/date=<D>/` whose file name starts `actions-void-` (`price_series._is_void_uri`) is NOT an action row: its rows are not in the returned frame, and the (`void_revision`, normalised
  `security_id`) pairs of every such object (`price_series._voids(s)`, over all dates) drop every EVENT row whose (`revision`, normalised `security_id`) they name, before the union is taken. Reuse those two
  functions (import them lazily inside `load_actions` if a module import would be circular); do not copy the normalisation. The returned `uris` still lists every object read, void objects included (lineage).
  The live store holds 11 objects, none a void or an inferred object, so the live DELTA = 0 read is unaffected. The check gains AC4 (`-k ac4`, 1 passed). Row S2 (a row that is neither event nor status follows the old
  latest-pull rule) is accepted as built.

### `RIV-xe-1` -- the enrichment leg runs on TRADING days only, and reads the standing request's queue state before a history-owed draw (analysis section 2.3; CTO msg 4568; row D1-S2; round-22 ADDENDUM 7 condition 1) -- APPENDED 2026-10-14, revision 1.31
- Placement: this seat's staged cell `round30_prep/STAGED_CELL_enrichment_trading_gate_and_queue_reader.md` (items 1 and 2); CTO msg 4568 ("one cell with the gate, at the site-Z window -- accepted").
- Measured: 2026-10-10 (a Saturday) exited 97 (the MON-FRI daily Lambda had not built the previous trading day's G1 before the leg looked) and 2026-10-11 (a Sunday) exited 95 on a signed-out Terminal; the
  leg has no trading-day gate. The standing request `ETFS_RIVALS-HISTORY-OWED-DAILY` has a queue state at
  `s3://opal-data-assets/bloomberg/global/silver/request_state/request=ETFS_RIVALS-HISTORY-OWED-DAILY/state.json` (`{"state": active|paused|stopped, ...}`, writer DQ-t-16, reader
  `data.mdpf.scripts.demque.standing.read_state`, which returns "unreadable" for a missing object or a failed read, never "active"); the leg does not read it.
- Interface (`data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` only):
  1. GATE. In `main(argv)`: with NO `--date` and `--mode` in (`daily`, `market`), when `_run_date_et()` is not a trading day by `lib.trading_calendar.is_trading_day` (imported lazily, as `main` already does), print
     ONE line beginning `SKIP:` (naming the date) and return 0 WITHOUT calling `handler_entry`. An explicit `--date` run, any other mode and a trading day are not gated. The calendar is the only source: no typed date list.
  2. READER. A new function `_queue_state() -> str`: `data.mdpf.scripts.demque.standing.read_state("ETFS_RIVALS-HISTORY-OWED-DAILY")`, imported lazily; any exception (an ImportError included) returns `"unreadable"`.
     In `_history_owed`, for `mode == "ask"` only, after the owed set is computed and BEFORE the stored-currency read or any Bloomberg request: state `active` proceeds exactly as today; any other value asks ZERO
     (no `_blp_call`, a currency lookup included), prints ONE `HISTORY OWED:` line naming the state (through `_owed_line` with `refusal="queue state <state>"`), and returns `asked` 0, `carried` = `owed`, and
     `refused` naming the state. `print` mode does not read the state. `RIVALFUNDS_HISTORY_OWED` is NOT set by this cell.
- Out of bounds: every other function of the file, `history_owed.py`, the switch-on, any window or cap constant, the vehicle's scripts and `integrations/bloomberg/pipeline/` (Andrew's no-modify order), any Bloomberg or S3 call in a check.
- Checks: `round30/checks/xe1_gate_and_queue_reader_check.py` (AC1 the gate: a Saturday, a Sunday and Labor Day print one `SKIP:` line and exit 0 without the leg, a trading day, an explicit `--date` and another mode are not gated, the calendar
  is the source; AC2 the reader: `active` draws, `paused`/`stopped`/`unreadable`/anything else draw zero and name the state, the reader fails closed, `print` does not read it; base FAIL 10, one control PASS) and the existing
  enrichment tests (AC3: must be green after your edits to the test files named in your paths). J1: none (a LOCAL cell; the deploy is site Z's under the CTO~Z half).

### `RIV-xf-1` -- ACWI and IWM are removed from the universe and from the holdings pull (Andrew's DEMQUE form A3, row Z4; CTO msgs 4932 and 4969) -- APPENDED 2026-10-14, revision 1.31
- Placement: this seat's staged cell (`round30_prep/STAGED_CELL_enrichment_trading_gate_and_queue_reader.md`, xf-1); CTO msgs 4932 and 4969; form `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md` A3 and row Z4.
- Measured (box/dell1): `peer_groups.json` (map_version 2, 15 entries) carries ACWI (group IDVZ) and IWM (group PFOE) as `role: index_control`, `"leg": "pending"`; with `leg_gates.json` reading ENABLE 0, D12 1, D13 0 they are dropped from
  `universe.funds()` (13 funds) and never pulled, so served output does not move. `bbg_budget.json` still sizes them (`est_rows_per_fund_date`: ACWI 2198, IWM 1979). The 2026-10-13 owed read: units whose only holders are ACWI or IWM: 0.
- Interface: delete the two entries from `data/etfs/scripts/rivalfunds/peer_groups.json` (every other entry and `map_version` unchanged); delete the `ACWI` and `IWM` keys of `est_rows_per_fund_date` in `data/etfs/scripts/rivalfunds/bbg_budget.json`
  (every other key and value unchanged). The generic machinery stays: the `index_control` role value, the `"leg": "pending"` mechanism, the gates, `collector_bloomberg.CONTROL_ROW_CAP` and `split_units`, because no served output depends on them and a
  benchmark may return as a map entry. Rewrite the tests that name the two funds to the new facts (a map entry for a benchmark is exercised through a synthetic map or a monkeypatched `_is_control`, never the shipped map).
- Out of bounds: `universe.py`, `collector_bloomberg.py` (code), every other map entry, any gate value in `leg_gates.json`, any S3 or vendor call.
- Checks: `round30/checks/xf1_acwi_iwm_removed_check.py` (AC1 in four gate states no ACWI or IWM and the same 13 funds; AC2 the holdings plan with every gate on is the 7 bloomberg_primary funds in one unit (AMENDMENT 1, issuer, row W42-S1: `request_plan` plans the `bloomberg_primary` funds only, 7 with ENABLE on, so the prior plan was these 7 plus ACWI and IWM and the change removes exactly the two); AC3 the budget config no longer sizes the two funds;
  base FAIL 5, the all-gates-off control PASS = DELTA 0) and the tests you rewrite (AC4: the three test files below, green). J1: none (a LOCAL cell; the deploy is site Z's under the CTO~Z half).

## ROUND 31 (main workstream, the FIX-ONLY round before the park) -- APPENDED 2026-10-15, revision 1.32 of this file

Input: Andrew-direct "Call bbd5: yes fix only round now" (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_205xZ_CALLS_BCCC_3ADB_BBD5.md` @cb7075dd11; CTO msg 6232) for the D1-S16 precedence cell, and Andrew at the `2.0.0_SA_COO~RV` terminal 2026-10-15
~16:5x ET: "the openai model being used for that analysis should be updated from 5.4 to 6 because it needs to be smarter and not make mistakes on figure representations" ("gpt 6 astra"). The round-30 analysis `ledger/ROUND_ANALYSIS.round30.md` @19136d1eda
cut no enrichment list (the project parks); this round is the two fixes only and the project parks after its analysis. Lane `2.0.0_SA_COO~RV` (CTO ruling @f8191183f6).

Cut in this issuance: RIV-ya-1, RIV-yb-1. Chains (M = 2): A = RIV-ya-1 (`gold_trade_schedule.py`, `price_series.py`), B = RIV-yb-1 (`ai_accounts.py`, `ai_client.py`). Write sets are disjoint; no edge. Checks:
`deliverables/2.0.0_SA_COO~RV/round31/checks/`, dry-run at the base before the cut (ya1 FAIL 4; yb1 FAIL 3; the round-30 xe3 control check PASS 5).
NOT in this round: RIV-xe-2 and the site-Z deploys of xe-1 and xf-1 (they ride site Z's producer deploy under `1.0.0_SA_CTO~Z`'s half; the park stops further cells).
The deploy of both cells is ONE act by a CloudOps seat (the five rivalfunds Lambda packages), under its own never-widen pair (COO half and CTO half), as round 30's TO-APPLY-R30 was.

### `RIV-ya-1` -- a Bloomberg corporate-action row beats an inferred row of the same (security_id, event_type, ex_date) in BOTH readers, and the drop is counted (CTO half condition C1, msg 5612; disarms row D1-S16) -- APPENDED 2026-10-15, revision 1.32
- Placement: this seat's staged cell `deliverables/2.0.0_SA_COO~V1/round31_prep/STAGED_CELL_bloomberg_wins_cross_source.md`; Andrew "Call bbd5: yes fix only round now".
- Measured (2026-10-15, S3 LIST+GET read-only): `gold/corporate_actions/` holds 12 objects, all plain Bloomberg pulls (`actions-<rev>`), 0 `actions-inferred-*`, 0 `actions-void-*`. A Bloomberg row carries `claim` "MEASURED"; an inferred row (written by
  `dramatic_move`) carries `claim` "INFERRED", a `source_url` and a `raw_event_type` that is the lookup's own phrase, so it never shares the union's own key (`gold_trade_schedule._ACTION_KEY`) with Bloomberg's row. The chart reader
  `price_series._adjustments` already collapses an IDENTICAL (ex_date, ratio) split (MEASURED first) but applies BOTH when the two ratios differ.
- Interface: (1) `gold_trade_schedule.load_actions(s)`: after the void rows leave and BEFORE the union is taken, of the EVENT rows that share (normalised security_id as `price_series._norm_key`, `event_type`, `ex_date`), where at least one has `claim` == "MEASURED" and
  another has `claim` == "INFERRED", the INFERRED rows are dropped. The returned triple is unchanged; the frame carries the number of rows dropped in `df.attrs["precedence_dropped"]` (an int, 0 when none; set on every frame returned, an empty one included). A frame with no `claim` column
  behaves exactly as before. The G5 stage (`gold_trade_schedule.py`, the function that calls `load_actions` at about line 1140) adds `"precedence_dropped": <n>` to its result `detail` dict (the one holding `corporate_actions_revision`, about line 1225), `0` when `actions` is None; no new log line. (2) `price_series.series(...)`: the same rule over the `actions` frame before `_adjustments`, so a Bloomberg split and an inferred split of the same
  ex_date apply ONCE (the Bloomberg row) whatever the two ratios; each key's result gains `"precedence_dropped": <int>` (0 when none). One inferred row with no Bloomberg row for its key is applied as before; two MEASURED rows are never dropped by this rule.
- Out of bounds: `dramatic_move.py` (the writer stays as is: no switch stops it, the disarm is the readers' rule), every other reader and stage file, the void rules (`actions-void-*` behave as before), any S3 write or vendor call, any Lambda or Terraform act.
- Checks: `round31/checks/ya1_bloomberg_wins_check.py` (AC1 the G5 reader, two tests; AC2 the chart reader, two tests; base FAIL 4) and the round-30 control `round30/checks/xe3_union_reader_check.py` (AC3: must stay green, 5 passed). The live-store DELTA = 0 read (today's 12 plain pulls, 0 inferred, through
  both readers) is the issuer's drain act, not a worker criterion. J1: none (a LOCAL cell; the deploy is its own pair, a `SERVED` path).

### `RIV-yb-1` -- the rivalfunds AI writer runs on `gpt-6-astra`, and the request it sends is one that model accepts (Andrew at the `~RV` terminal 2026-10-15) -- APPENDED 2026-10-15, revision 1.32
- Placement: Andrew's word above; the 2026-10-15 13:00Z sweep graded 24 of 26 AI items grounded on `gpt-5.4`, with TXUE's two items served as Grounding FAIL after the one allowed correction (row ETFS_RIVALS-D1-S18).
- Measured (2026-10-15, the live API with the project key `rivalfunds/openai-api-key`, read-only calls): `gpt-6-astra` is listed among 133 models; a chat completion with `response_format` json_object and NO `temperature` returns 200; the same request with `temperature: 0.2` (what both clients send today)
  returns HTTP 400 "'temperature' does not support 0.2 with this model. Only the default (1) value is supported", so changing only the model string would fail EVERY AI call. `gpt-5.4` accepts both. A trial of the production chain (prompt `a1-chain/8`, nothing written) on `gpt-6-astra` for TXUE returned both
  items PASS with 0 corrections where `gpt-5.4` returned FAIL after 1. The live Lambda sets `RIVALFUNDS_AI_ENABLE` and `RIVALFUNDS_OPENAI_SECRET` and NO `RIVALFUNDS_AI_MODEL`, so the model in force is the code default `ai_accounts.DEFAULT_MODEL`.
- Interface: (1) `ai_accounts.DEFAULT_MODEL` defaults to `"gpt-6-astra"` (the env var `RIVALFUNDS_AI_MODEL` still overrides). (2) `ai_client.RestClient.chat` and `ai_accounts.OpenAIClient.chat` send `temperature` (0.2) ONLY when the model name starts with "gpt-5"; for every other model the key is omitted; nothing else in either
  request changes. (3) `PROMPT_VERSION` and every prompt constant are unchanged: the stored `model_version` column is how a row names the model, and the page footer prints it.
- Out of bounds: the prompts, `PROMPT_VERSION`, the grounding and wording checks, `run_chain`, `render.py`, Terraform and the Lambda environment (no env key is added), any vendor call, any Secrets Manager call.
- Checks: `round31/checks/yb1_model_gpt6_astra_check.py` (AC1 the default and the override, one test; AC2 the two clients, two tests; base FAIL 3). The grounded-count comparison on the live sweep is the CVO's J1 read after the deploy: on the first 13:00Z sweep after the deploy, `model_version` reads `gpt-6-astra` on 26 of 26 rows and the
  Grounding FAIL count is no greater than the 2 of 26 of 2026-10-15.

## ROUND 32 (main workstream, Andrew-direct "completely filled" -- the held-day total return writer) -- APPENDED 2026-10-17, revision 1.33 of this file

Input: Andrew-direct 2026-10-17 ~04:2xZ, verbatim "Yeah I want all those completely filled", then "now" (record `org/tier1_exec/2.0.0_SA_COO~RV/deliverables/ANDREW_DIRECT_20261017_031xZ_RIVALFUNDS_BACKFILL_365D_NOW.md`; `2.0.0_SA_COO~Q1`'s record @1438d1fb76), and
`1.0.0_SA_CTO~DELL1` msg 7291: "TR-HELD: cut the TR writer cell in your next issuance now. Its served-rankings never-widen pair comes to me before any TR row lands where the rankings read." Round 31 stays open on its own L2 read; this round is one cell on a disjoint write surface. Lane `2.0.0_SA_COO~RV`.

Cut in this issuance: RIV-za-1. Chains (M = 1): A = RIV-za-1 (`enrichment_bloomberg.py`). Check: `deliverables/2.0.0_SA_COO~RV/round32/checks/za1_held_tr_check.py`, dry-run at the base before the cut (FAIL 5).
NOT in this round: the live run (site Z, `0.0.3_BG_BBGTerminal`, over the TR-HELD D30/D90/D365 units, 123,933 at the 2026-10-12 quote) and the Lambda deploy; each is its own act under its own never-widen pair (the run moves the served rankings).

### `RIV-za-1` -- a `held-tr` mode asks PX_LAST and DAY_TO_DAY_TOT_RETURN_GROSS_DVDS together for named (security, trading day) units and lands each date as ONE timed G4 object the rankings read (Andrew-direct 2026-10-17; CTO msg 7291) -- APPENDED 2026-10-17, revision 1.33
- Placement: the queued `MDPF_DEMQUE/requests/ETFS_RIVALS-C1-TR-HELD-{D30,D90,D365}` (held at 04:2xZ by `1.0.0_SA_CTO~DELL1` msg 7280: DEMQUE output lands in ZQ_STANDING, not the page store) are the units; no rivalfunds writer lands total return history today (`BACKFILL_FIELDS = ["PX_LAST"]`; the history-owed ask is PX_LAST only).
- Measured (2026-10-17, code read): `gold_holding_contribution._g4_merge` copies the PRICE GROUP (`px_close`, `total_return_index`, `currency`, `as_of`, `source`, `as_of_source`, `price_date`) WHOLE from the first ranked row whose `px_close` is not null, and ranks a non-backfill row before a backfill row; `drop_backfill` removes rows whose `as_of_source` is exactly "backfill". So a TR value reaches the rankings only on a NON-backfill row that carries its own `px_close` -- a TR-only row never does.
- Interface: (1) `handler_entry` accepts mode `held-tr`, event {"units": [{"bloomberg": <key>, "dates": [ISO trading days]}], "max_points": int >= 0 (required), "dry_run": bool (absent = true), "batch_id", "sink"}; the request shape is the DEMQUE dates-entry shape, so a request file's `securities` list is a valid `units`. (2) Plan: units = the (security, date) pairs; fields `["PX_LAST", "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"]`; currency lookups = the unit securities with no stored currency by `_stored_currencies(s, secs, <first unit date>, _run_date_et())`; points = 2 x units + lookups. REFUSED before any request when points > max_points or `bbg_budget.check_points(points)` refuses; a dry run returns OK with the plan and requests and records nothing. (3) Live: ONE reference CRNCY request for the lookups; then per date, batches of `DEFAULT_BATCH`, `_blp_historical_data(batch, fields, day, day)`; every request sent is recorded with `bbg_budget.record("held-tr", ...)`; a returned value dated other than the asked day is not written and is counted `misdated`; a security whose PX_LAST is missing is not written. Each date's rows are `market_rows(..., MARKET_SOURCE_HIST, prov, "held-tr")` with `price_date` = the day and `currency` = the stored or looked-up currency, landed as ONE new object `market_target_uri(day, f"{rev_mod.compact(rev_mod.capture_time(produced_at))}-{_digest(data)[:12]}")`, never overwriting a name. Result {"status", "plan", "units", "asked", "landed", "carried", "failed", "misdated", "currency_lookups"} and one printed line `HELD TR: units <n>; asked <a>; landed <l>; carried <c>; failed <f>; misdated <m>; currency lookups <k>`. (4) CLI: `--mode held-tr --units-file <json: a list, or an object whose "securities" is the list> --max-points <n> [--live]`.
- Out of bounds: every reader and stage (`gold_holding_contribution.py`, `price_series.py`, the rankings), `bbg_budget.py` and its config, `history_owed.py`, the existing modes' behaviour (market-range, history-owed, daily), any S3 write outside a LocalSink, any vendor call, Terraform and the Lambda.
- Checks: `round32/checks/za1_held_tr_check.py` (AC1 the plan, dry run and refusal, two tests; AC2 the live landing and no overwrite, two tests; AC3 the merged row takes the held-tr price group over a backfill row and `drop_backfill` keeps it, one test; base FAIL 5). J1: none (a LOCAL cell; the run is its own pair, a `SERVED` path).
