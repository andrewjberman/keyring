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
 "revision": "1.4",
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
