# PEERS TAB (AMGT Security Analysis): end-to-end trace brief

Prepared by 4.0.0_SA_CRO~Z on 2026-09-23 (measured 2026-09-24 01:33Z-01:56Z, device OPAL_BLOOMBERG). Read-only
assessment plus proposed closure requirements; no application changes, vendor calls, deployment or schedule
activation. Four direct invocations of the deployed function `opal-amgt-scoped-api` were made with a synthetic
gateway event (reads only); nothing was written to the pool.

This is the B04 / P1 surface of the CTO's AMGT completion contract (`org/tier1_exec/1.0.0_SA_CTO/deliverables/
AMGT_COMPLETION_20260923/CONTRACT.md` v1.0, lane EXPERIENCE + SERVED RUNTIME, seat `2.0.0_SA_COO~Z`). The B04 row
in `TRACE_BRIEF_SET.md` @`fd51c46d81` (branch `closer/amgt-r-20260923`, not on SITEZ) named the walk; this brief
measures it hop by hop from deployed bytes. Machine-readable evidence: `PEERS_END_TO_END_GAP_BRIEF_20260923.evidence.json`
beside this file.

## Design finding

The Peers tab is Adam's `CSC` sheet as a served table: for a selected security, ONE ranker
(`lib/research/peers/engine.py`) computes the comparable set over ONE database (the Security Scanner universe
UNION the landed model-block headers), by four lexicographic rungs (sector, 0.2x-5x size band, country, industry
group), capped at 12, and writes it as INTERFACE R-1 to `s3://opal-data-harvest/peers/v1/<security_key>/<as_of>.json`.
Opal retains the object; the route `GET /api/scoped/amgt/security/{key}/peers` serves the LATEST object whole after
resolving the identity ONCE at the route boundary; the tab renders one row per comparable and one column per
declared CSC column (17), with Average / Median / Min / Max rows computed on the page over member values. The page
must never compute a peer set, invent a column value, or show a lookup key as a label. No Bloomberg call sits on
the request path.

How far the implementation is from that: every component exists, is deployed, and the backend journey WORKS for a
resolved key (Boeing: 12 members, served from the pool by the signed candidate bytes). The two unfinished
connections are both identity-and-field adapters, not missing parts. (1) The producer and the route resolve
identity in DIFFERENT key spaces: the ranker minted 191 keys through a widened identity set, the route resolves
through `crosswalk/v1` alone (36 MEASURED keys), so 158 of the 191 landed peer objects are UNRESOLVED at the
route and 111 of those carry a real derived set that no screen can reach. (2) The producer's member rows and the
tab's column map do not agree on where a present column's value lives, so the served table shows a value in 1 of
17 columns while the payload carries a second. Worth keeping: the ranker, its MECE denominators, the R-1 absent
arm, the pool reader's three-status record, the one-identity route boundary, the CSC table builder and the offline
render harness. Unfinished: one key space, the present-column carry, and any owner or trigger for the batch.

## Current measurement

Read from DEPLOYED bytes at 01:40Z-01:52Z UTC 2026-09-24:

- Function `opal-amgt-scoped-api`: CodeSha256 `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`, CodeSize 807,904,
  LastModified 2026-09-23T22:02:35Z, python3.11, handler `lambda_function.lambda_handler`, layer
  `opal-amgt-print-deps:1`, timeout 29 s, 1769 MB. The digest decodes to hex
  `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55`, which EQUALS the candidate ZIP SHA256 in
  `2.0.0_SA_COO~Z`'s STATUS.md: the deployed bytes are the signed no-span repair package. Environment carries only
  the two DynamoDB table names; `AMGT_MODEL_BLOCK_ROOT` and `AMGT_POOL_ROOT` are unset, so the route's second
  identity surface (a landed `model_block_<key>.json` on disk) cannot fire on the deployed function and every
  pool read goes to `s3://opal-data-harvest`.
- Gateway `7k3ed8px20`: route `GET /api/scoped/amgt/security/{security_key}/peers`, AuthorizationType CUSTOM,
  authorizer `naqxlm`, target `integrations/352l7td` (live read, 01:52Z).
- CloudFront (declared plane, `comp-routes trace`): behavior `/api/scoped/amgt/*` -> origin `APIGateway-portal`,
  viewer-request `auth-validator-edge`. Served bundle at `d2n2nzpeqf34ge.cloudfront.net`: index chunk
  `assets/index-BFAZki1o.js`; of 51 chunks fetched (3,940,231 bytes) exactly one, `assets/index-4rpf7wvH.js`,
  carries `data-csc-table`, the Peers subtitle and the `/api/scoped/amgt` prefix. Portal CI on DEV only builds an
  artifact; `deploy.yml` on PROD is the only S3 + CloudFront publisher, so this is the PROD bundle. `origin/PROD`
  @`a0690a03` and `origin/DEV` @`c1ac41ec` both carry all 53 `src/pages/SecurityAnalysis/` files.
- Direct invocations (API Gateway v2 proxy event, header `x-firm-id: opal`), all HTTP 200:
  `BA_US_Equity` -> identity MEASURED, basis derived, 12 members, `peer_read.status` SERVED at
  `peers/v1/BA_US_Equity/2026-09-17T0240Z.json`; `992_HK_Equity` (Lenovo) -> MEASURED, derived, 12 members, with
  the producer's own FX caveat (subject cap in HKD, database cap in USD, band graded across currencies);
  `ASML_US_Equity` -> identity UNRESOLVED, basis absent, `peer_read` null, "identity UNRESOLVED -- no peer set
  was read", although `peers/v1/ASML_US_Equity/2026-09-17T0240Z.json` exists (9,404 bytes); `NOSUCHKEY_ZZ_Equity`
  -> UNRESOLVED (negative control, same shape).
- Pool `peers/v1/`: 797 objects (one page, not truncated), newest LastModified 2026-09-17T02:42:18Z; five
  partitions, the newest `2026-09-17T0240Z` holding 191 keys. Of the 190 downloaded: basis derived 141, absent
  49 (47 "no classification", 2 "no candidate reaches rung 2"); member_count 12 on 132, 0 on 49; universe vintage
  2026-08-06 on all 190; subject cap from a model block on 33, from the scanner row on 110; 22 subjects carry the
  FX caveat. One key (`WALMEX*_MM_Equity`) cannot be materialised on Windows because of the asterisk.
- Universe: the scanner file `json/security_scanner/latest/universes/sp500/universe_data.json` in
  `opal-data-portal-v2` has `asOf` 2026-08-06, LastModified 2026-08-07T21:59Z, 502 securities; pool
  `universe/v1/` newest 2026-09-16.
- Identity: `crosswalk/v1/2026-09-22.json` (newest of three) has denominators input_names 89, records 96,
  MEASURED 36, UNRESOLVED 60. Running the route's own resolver (`lib.research.identity.crosswalk.resolve`, HEAD
  `cd0268a4f4`, pointed at the downloaded object) over the 191 newest pool keys: MEASURED 33, UNRESOLVED 158. Of the
  33: derived 30, absent 2, one not downloaded. Of the 158: 111 have basis derived in the pool. Three crosswalk keys
  (`6861_JP_Equity`, `CAT_US_Equity`, `CSL_AU_Equity`) have no peer object in any partition.
- Producer cadence: no Lambda writes `peers/v1/` (the two functions named `amgt` are the chatter axis and this API);
  the only local scheduled task matching amgt/peer/resapp/harvest/universe is "Opal Data Harvest - Local
  Publications", Disabled. The writer is the hand-run `python -m lib.research.peers.engine --write-pool`; the last
  batch landed 02:41Z-02:42Z on 2026-09-17 (engine last changed 2026-09-16 by `0.9.0_WK_AMGT_RESAPP~25`).
- CSC carry: the served object's `csc_columns` declares 17, present 5 (Price, Mkt Cap, EV, P/E 2025 = 1/ey trailing,
  P/E 2026 = 1/ey_ntm NTM), absent 12 with reasons. Member rows carry `market_cap_musd` top-level and 26 factor codes
  under `factors`; `ey_ntm` is present on 1,641 of 1,646 member rows in the newest partition; `price`, `ev`, `ey`,
  `mkt_val_sec` appear on none. The frontend map `MEMBER_FIELD_FOR_CODE` (`portal/src/pages/SecurityAnalysis/cscTable.ts`)
  holds one entry, `mkt_val_sec -> market_cap_musd`.

NOT invoked: a signed-in browser walkthrough; the CloudFront edge (the `x-firm-id` header was supplied to the
function directly, so header injection after JWT validation is not exercised here); a producer run; any vendor or
Bloomberg call; any pool write. A configured behavior and a live route are not an executed connector; hop 3 below
says which half was measured.

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO/deliverables/PEERS_END_TO_END_GAP_BRIEF_20260923.evidence.json`

## Adapter map

| Surface / firm | Provider and intended endpoints | Existing work | Gap |
|---|---|---|---|
| Peers tab, any permitted firm (route is firm-gated at the edge, data is not firm-partitioned) | Opal pool: `s3://opal-data-harvest/peers/v1/<key>/<as_of>.json` (R-1), read through `GET /api/scoped/amgt/security/{key}/peers`; auth = portal JWT -> `auth-validator-edge` -> `x-firm-id` | `engine.py` ranker + `csc.py` map + `universe.py` loader; `scoped_amgt.py` `resolve_identity` / `read_peer_set` / `read_pool_object`; `amgt-lead-panel.ts` `getPeerSet`; `useLeadPanelApi.ts` `usePeerSet`; `PeersTab.tsx` + `cscTable.ts` + `IdentityLine.tsx`; offline harness `__harness__/tabs.harness.cjs` | Producer keys minted in the widened identity set, route resolves only `crosswalk/v1`: 158 of 191 objects unreachable, 111 real sets among them |
| Same tab, present-column values | R-1 `csc_columns.present` (5 codes) vs member rows | `cscTable.ts` renders PRESENT_CARRIED only where `MEMBER_FIELD_FOR_CODE` names a member field | Map has 1 entry; producer carries `ey_ntm` under `factors` on 1,641 of 1,646 rows and does not copy `price`, `ev`, `ey` onto rows; served table shows 1 of 17 columns |
| Same tab, freshness | Scanner universe `asOf` 2026-08-06 -> `universe/v1` -> batch | Universe loader with printed vintage; hand-run batch | No owner or trigger for the batch; universe seven weeks old; 3 crosswalk names without any object; 47 absent for "no classification" |
| Posture tab (second consumer of the same read) | Same route, called for the subject AND the comparable (`PostureTab.tsx:339-347`) | Shared `usePeerSet` | Any change above lands on both consumers; a fix checked on Peers alone is half-checked |

One row's success does not certify another: Boeing resolving proves the crosswalk arm, not the 158 keys outside it.

## Start-to-finish walk

### 1. Sign-in -> `/security-analysis/:securityKey` -> Peers tab click -- INCOMPLETE

What exists: `portal/src/App.tsx:447-448` (`ProtectedRoute requireDev requireAdmin`), `SecurityAnalysis.tsx:78-86`
(five tabs from `constants.ts:72-78`, `activeTab === 'peers'` mounts `PeersTab`), the served chunk
`assets/index-4rpf7wvH.js` carrying the page. This is the shared first hop (`B00` / `E0`), owned by
`2.0.0_SA_COO~Z`; its STATUS.md reads E0 NOT_EVALUATED and names the missing input: an identity holding both
`user.role==='admin'` and `claims.userType==='Dev'`, which is Andrew's to supply. A `/market` redirect fails the case.

The exact mismatch: none in this surface's code; the hop is unexercised, not wrong.

Close: E0 as B00 states it, one real permitted identity reaching this route on the served stack, recorded as one
trace. This brief adds no requirement to it.

### 2. `PeersTab` -> `usePeerSet` -> `getPeerSet` -> `GET /api/scoped/amgt/security/{key}/peers` -- WORKS

What exists: `PeersTab.tsx:140` (`usePeerSet(securityKey)`, disabled until a key is selected), `useLeadPanelApi.ts:125-133`
(react-query, retry 2), `amgt-lead-panel.ts:137-139` (`encodeURIComponent(key)`, `BASE = '/api/scoped/amgt'`),
`api-client.ts` (Bearer from `localStorage.accessToken`, proactive refresh after 10 min, 401 -> refresh-then-retry).
The served chunk carries the route prefix once.

The exact mismatch: none. Field contract: the client types the response as `PeerSet` (`types.ts:467-484`); every
field the route serves (measured above) is either typed or falls into the typed optionals; `identity` is typed
optional and the route always sends it.

Close: nothing; exercised live by E0.

### 3. Browser -> CloudFront `/api/scoped/amgt/*` -> `auth-validator-edge` -> API GW route -> `opal-amgt-scoped-api` -- WORKS (declared + live route; edge injection not exercised here)

What exists: behavior and edge association per `comp-routes trace` (desired plane, parsed terraform); the live
route with CUSTOM authorizer `naqxlm` and integration `352l7td` (read 01:52Z); `scoped_amgt.py:3838-3850`
`_firm_id` fails closed with 401 when `x-firm-id` is absent; `lambda_function.py` catches everything into a 500
rather than a 502.

The exact mismatch: none found. What this trace measured is the function behind the route with the header
supplied; the edge's JWT verification and header injection were measured by `1.0.0_SA_CTO~Z` for C4 (an
identical 401 on a nonexistent path) and are cited, not re-derived.

Close: nothing beyond E0's live trace, which crosses this hop by construction.

### 4. Route boundary: `resolve_identity(requested)` -> `crosswalk/v1` -- MISMATCHED

What exists: `scoped_amgt.py:1785-1889` resolves ONCE: surface 1 `crosswalk.resolve` over
`crosswalk/v1/2026-09-22.json` (36 MEASURED keys of 89 input names); surface 2 a landed `model_block_<key>.json`
under `AMGT_MODEL_BLOCK_ROOT`, unset on the deployed function; otherwise UNRESOLVED and `read_peer_set(None)`
returns the absent arm WITHOUT reading the pool. On the producer side, `engine.py:208-244` (AC2, AMGT-rk-13) tries
the crosswalk first and, when it is UNRESOLVED, falls through to AMGT-rk-4's widened identity set
(`universe/v1`, CUSIP/FIGI/SEDOL-deduped) and mints `<ROOT>_<CC>_Equity` keys from it; 191 keys landed that way.

The exact mismatch: two resolvers, two key spaces. Producer: 191 keys, identity `resolution: MEASURED`
(`matched_as: widened_identity_set`) on every object. Route: 36 keys. Overlap 33. The route answers UNRESOLVED for
158 pool keys; 111 of those objects are `basis: derived` (real sets, e.g. `AAPL_US_Equity`, `AMZN_US_Equity`,
`AVGO_US_Equity`, `CVX_US_Equity`). Measured with the route's own function over the route's own object. The
deployed invoke for `ASML_US_Equity` shows the served effect: `identity_status UNRESOLVED`, `peer_read null`, and the
page will print the raw string marked UNRESOLVED, while the pool holds an object at exactly that key (basis absent,
reason "no classification"). The same economic security sits in the crosswalk as `ASML_NA_Equity` (record 0).

Close: ONE key space. Recommended: the crosswalk builder (`lib/research/identity/crosswalk.py`, writer of
`crosswalk/v1`) takes the widened identity set (`universe/v1`) as a second registration source beside the 89-name
coverage list, so every key the ranker can mint is a key the route can resolve; re-mint `crosswalk/v1/<as_of>.json`
with `--write-pool`. Proof: `crosswalk.resolve()` over the 191 newest pool keys prints 191 MEASURED, or a printed
list of refusals with reasons; then the deployed `/peers` for `AAPL_US_Equity` returns `basis: derived` with its
members and `peer_read.status SERVED`. Not recommended: letting the route accept a landed peers object's own
identity block as a third surface, because it would make any pool key resolvable and is the guess the crosswalk's
ratified text forbids. Owner: `2.0.0_SA_COO~Z` (sole writer of `lib/research/identity/**`); the ranker's
fall-through is a contract question for `1.0.0_SA_CTO~Z` (one exchange, then a ruling) because it changes which
names get a set at all.

### 5. `read_peer_set` -> `read_pool_object('peers/v1/', key)` -> latest object served whole -- WORKS

What exists: `scoped_amgt.py:1193-1323` (list under `peers/v1/<key>/`, take the last `.json` in key order, three
statuses SERVED / ABSENT / READ_FAILED that never collapse, `_foreign` refuses an object naming another key);
`handler():3977-3980` returns the dict plus the identity block. Measured: Boeing 12 members, tickers DE ETN UNP
UBER PH LMT HWM VRT TT GD PWR GEV, `reason` printing the four rung counts over 2,850 graded of 2,851; Lenovo 12
members with the FX caveat in `reason`. Absent arm: `CAT_US_Equity` resolves in the crosswalk and has no object, so
the route will answer "no R-1 peer set has landed for this name" with `peer_read.status ABSENT`.

The exact mismatch: none for a resolved key. One shape hazard: "latest" is the LAST `.json` key in string order,
which is correct only while every partition name sorts by time; the newest partition names carry a `THHMMZ` suffix
and the older ones do not (`2026-09-16` sorts before `2026-09-16T1930Z`, fine), and a future date-only partition
would sort AFTER a same-day timed one. Not a defect today; named so the producer's `--write-as-of` convention stays
time-sortable.

Close: nothing to change; the hop is the positive control for hop 4.

### 6. Scanner universe + model-block headers -> `engine.py --write-pool` -> `peers/v1/` -- INCOMPLETE

What exists: `universe.py` (six scanner files read by boto3, `asOf` carried as the vintage; model-block header
scalars joined by US ticker root; caps normalised to USD millions with NO FX applied, the caveat carried), the
ranker with MECE denominators, the batch CLI. Landed: 797 objects, five partitions, newest 2026-09-17T02:42Z, 191
keys; 141 derived / 49 absent, 47 of the absent for "no classification" (no landed model block and no scanner row
for the US root).

The exact mismatch: the batch has no owner and no trigger (no Lambda, the only related local task is Disabled), so
the served set is whatever the last worker ran; the candidate database is seven weeks old (scanner `asOf`
2026-08-06, files written 2026-08-07); 22 subjects are band-graded across currencies; three names the route CAN
resolve have no object at all.

Close: one named owner and one stated trigger for the batch ("after each `crosswalk/v1` or `universe/v1` re-mint,
run `python -m lib.research.peers.engine --write-pool --as-of <stamp>` over the current crosswalk"), and one run
now, after hop 4's re-mint, so `6861_JP_Equity`, `CAT_US_Equity` and `CSL_AU_Equity` gain an object (derived or an
explicit absent). Proof: a new partition whose key set equals the crosswalk's MEASURED set, printed with both
denominators. Parked, not on this thread: the scanner universe refresh (upstream `opal-data-portal-v2`
`security_scanner/latest`, owner unknown to this trace, un-parks when its writer is named) and an FX source for the
band (a data-source decision, Andrew's).

### 7. Served R-1 -> `buildCscTable` -> rendered CSC table -- MISMATCHED

What exists: `cscTable.ts` (columns from R-1's map in R-1's order; PRESENT_CARRIED only when
`MEMBER_FIELD_FOR_CODE[code]` names a member field; summary rows over member values with n), `PeersTab.tsx`
(`data-csc-column-state`, the counts line, the reasons list). R-1's map on every served object: 17 declared, 5
present (`price`, `mkt_val_sec`, `ev`, `ey`, `ey_ntm`), 12 absent with reasons, and the rk-14 rule that a fiscal-year
label never sits over an NTM figure (`display_label` states the grain).

The exact mismatch: producer sends `market_cap_musd` at the row top level and `ey_ntm` inside `factors` (1,641 of
1,646 member rows); it does not put `price`, `ev` or `ey` on the row at all, although the universe row it was
drawn from carries 284 value codes. The frontend map knows only `mkt_val_sec -> market_cap_musd`. So the screen
shows values in Mkt Cap only; "P/E 2026" is rendered "not carried" while the value is in the payload; Price, EV and
"P/E 2025" are "not carried" because they truly are not on the row; 12 columns say ABSENT. The summary rows are
computed over one column.

Close: (a) frontend: `MEMBER_FIELD_FOR_CODE` gains `ey_ntm -> factors.ey_ntm` rendered as `1 / ey_ntm` under the
R-1 `display_label` (NTM grain), with a nested-field reader in `valueOf`; (b) producer: copy the row's `price`, `ev`
and `ey` values onto each member row as top-level fields the map can name, and re-run the batch. Proof: a served
Boeing object whose members carry all five present codes, and the rendered table (offline harness first, then E0's
live screen) reporting "5 present / 12 absent of 17 declared; 5 column(s) carry a per-member value" with summary
rows at n=12. Owner: `2.0.0_SA_COO~Z` for `portal/src/pages/SecurityAnalysis/**`; the peers module is not a row in
the contract's ownership table, so the producer half goes to whichever seat the CTO names (parked line for the
contract, un-parks on that ruling).

### 8. Same read -> `PostureTab` (subject + comparable) -- WORKS, checked against both

What exists: `PostureTab.tsx:339-347` calls `usePeerSet` for the subject and again for the comparable key. Any
change in hops 4 and 7 lands here unchanged; the acceptance below runs the Posture read as a second consumer.

Close: nothing separate; every Peers case in the matrix is also read through Posture once.

## Recommended completion sequence

1. **The live thread.** One named person with the admin + Dev identity, one journey: sign in, reach
   `/security-analysis/BA_US_Equity` on the served stack (`d2n2nzpeqf34ge` bundle, PROD authorizer, deployed
   function `DEQQiCH+...`), click Peers, see the identity line "BA US", the derived badge, 12 comparables, the
   counts line "5 present / 12 absent of 17". Crosses hops 1, 2, 3, 5, 7. First hop owner `2.0.0_SA_COO~Z`; the
   identity is Andrew's input. Recorded as one trace artifact with the request, the route's identity block, the
   `peer_read` record and the rendered counts.
2. **One key space** (hop 4): crosswalk re-mint over the widened set; the 111 stranded sets become servable.
3. **Carry the present columns** (hop 7): frontend map + producer row fields; the table gains four columns.
4. **Owner and trigger for the batch** (hop 6): one run now over the re-minted crosswalk; the three holes close.
5. Enrichment, in order of user gain: the scanner-universe refresh (upstream), FX for the band, and the 12 absent
   CSC columns, which need Bloomberg fields the scanner does not carry (shares, debt, preferred, minority, cash,
   five-year growth) and are a data-source decision for Andrew, not an adapter fix.

## Acceptance

One reconciled trace per case, each following one request from the user's selection through the route's identity
block, the `peer_read` record, the pool object key, the served member rows and the rendered column states and
counts. The surface is complete when these reconcile, not when `tabs.harness.cjs` passes on a fixture.

Cases: SELECTIONS {`BA_US_Equity` (resolved, derived 12, USD); `992_HK_Equity` (resolved, derived 12, FX caveat
shown); `ASML_US_Equity` (today UNRESOLVED at the route with an object in the pool; after step 2, resolved with
basis absent and its "no classification" reason shown); `CAT_US_Equity` (resolved, no object; after step 4, an
object); `NOSUCHKEY_ZZ_Equity` (UNRESOLVED, raw string shown, negative control)} x CONSUMERS {Peers tab, Posture
comparable read} x FAILURE CASES {expired session (edge 401 -> refresh -> retry), `peer_read.status READ_FAILED`
(a permission or parse failure must not render as ABSENT), a pool key with a literal `/` (`BP/_LN_Equity` shape,
10 objects)}.

## Evidence anchors and limits

Source inspected at workspace `cd0268a4f4` (SITEZ) and portal `10141b6d0b` (DEV; an ancestor of `origin/DEV`
`c1ac41ec`, which is 7 hours newer); shared work may advance concurrently. Verified fresh: the deployed function
digest, environment and four direct invocations; the live gateway route and authorizer; the served bundle's 51
chunks; the full `peers/v1/` listing and the newest partition's 190 objects; the crosswalk object and the resolver
run; the scanner universe file; the local task list. Not verified: a signed-in walkthrough; the edge header
injection (cited from `1.0.0_SA_CTO~Z`'s C4 measurement); the CloudFront behavior on the LIVE distribution
(`comp-routes` reads the declared plane only; a raw `get-distribution` is rail-gated).

- `lib/research/api/scoped_amgt.py` (`resolve_identity` 1785-1889, `read_pool_object` 1193-1269, `read_peer_set`
  1287-1323, `handler` 3892-3980, `FIRM_HEADER` 3822)
- `lib/research/peers/engine.py` (header 1-120, identity fall-through 197-280), `lib/research/peers/csc.py`,
  `lib/research/peers/universe.py` (1-40, 615-640)
- `lib/research/identity/crosswalk.py` (header, `resolve` 885)
- `portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx`, `cscTable.ts`, `types.ts:392-484`,
  `hooks/useLeadPanelApi.ts:125-133`, `components/IdentityLine.tsx`, `tabs/PostureTab.tsx:339-347`
- `portal/src/api/endpoints/amgt-lead-panel.ts:135-139`, `portal/src/api/api-client.ts`, `portal/src/App.tsx:447-448`
- `infra/aws/terraform/harvest/scoped-amgt-api.tf`, `infra/aws/lambda/research/scoped_amgt_api/lambda_function.py`
- `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_EXPERIENCE/STATUS.md` (E0 NOT_EVALUATED, candidate ZIP SHA256)
- `org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_MVP_RESEARCH_20260923/evidence/MEASUREMENTS.json` (13:23Z reads of
  the same pool and route, corroborating count 797 and the route key; a different seat's instrument)

## Andrew-direct request -- verbatim record

Channel: this terminal (Claude session launched as `4.0.0_SA_CRO~Z`), 2026-09-24 ~01:3xZ (2026-09-23 evening
Eastern), the second prompt of the session.

> /closer trace AMGT "Peers" tab
