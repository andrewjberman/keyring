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
 "revision": "1.2",
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
