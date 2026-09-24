# LEAD PANEL (AMGT Security Analysis): end-to-end trace brief

Prepared by 4.0.0_SA_CRO~Z on 2026-09-23 (measured 2026-09-24 02:08Z-02:24Z, device OPAL_BLOOMBERG). Read-only
assessment plus proposed closure requirements; no application changes, vendor calls, deployment or schedule
activation. Thirteen direct invocations of the deployed function `opal-amgt-scoped-api` were made with synthetic
gateway events (all reads; the two write routes, star/unstar and the pull enqueue, were NOT called). Nothing was
written to any table, queue or bucket.

This is the B01 surface (acceptance IDs L1-L4, W1, F1) of the CTO's AMGT completion contract
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_COMPLETION_20260923/CONTRACT.md` v1.0, lane EXPERIENCE + SERVED
RUNTIME, seat `2.0.0_SA_COO~Z`; HARVST supplies the chatter input, seat `2.0.0_SA_COO~Y`). Sibling brief:
`PEERS_END_TO_END_GAP_BRIEF_20260923.md` @`d350781052`. Machine-readable evidence:
`LEAD_PANEL_END_TO_END_GAP_BRIEF_20260923.evidence.json` beside this file.

## Design finding

The Lead Panel is the persistent universe-discovery header of the Security Analysis page. Two independent
controls, MOVEMENT (Trending | Breakout) x SUBJECT (Chatter | Price), name one of four producer-written
partitions in the DynamoDB table `opal-harvest-security-metrics`. Each partition is published as an immutable
GENERATION plus a `_CURRENT` pointer (INTERFACE G-1): the chatter producer is a daily Lambda over the pool's
article store; the price producer is a box-side Bloomberg pull on the terminal machine. The route
`GET /lead-panel/rankings/{movement}/{subject}` follows the pointer, verifies the row count, and serves the head
of the generation in producer order; `/timeseries` serves each ticker's producer-written rank across the window;
`/watchlist` is a per-firm star marker keyed off the edge-injected firm; Refresh is an explicit per-name action
that must reach the on-box pull consumer. The page never ranks, sorts or scores; it renders rows, the resolution
record, the generation caption, and a row's click carries the producer-resolved `security_key` into Security mode,
whose overlay shows the name's own point on every axis plus header figures, description, feed and Posture.

How far the implementation is from that: every hop is deployed and the read path WORKS end to end for the four
crosses, the series, the watchlist read and the firm gate. What is unfinished is the WATER, not the pipes, and two
adapters at the edges. (1) The chatter input is nearly dry: the deployed producer reads the legacy article path
and finds links for 3 of 250 names, so Trending x Chatter is a two-row list with score 0 and Breakout x Chatter
has been EMPTY for nine consecutive days (189 of 191 "no signal in window"); the gold-table reader that fixes
this exists at HEAD but not in the deployed bytes. (2) The price producer is hand-run and last landed
2026-09-15; the list is served through a 14-day dated fallback that expires on 2026-09-29, after which both
Price crosses read ABSENT. (3) The page does not carry or render the `dated` flag, so a nine-day-old list sits
under a fresh timestamp. (4) The Security-mode overlay's per-axis point reads have no dated fallback, so the same
name that is rank 1 on the list reads "no committed ranking for today" in its own overlay. (5) Refresh declares a
carrier and enqueues nothing; the client types a field the server never sends; the on-box consumer is a
person-started poller that was not running. Worth keeping: the generation contract and its row-count refusal,
the crossed-axis resolution record, the completeness record on the series, the edge firm gate, the four-state
list rendering and the identity-carrying rows.

## Current measurement

Read from DEPLOYED bytes and LIVE state at 02:08Z-02:24Z UTC 2026-09-24:

- API function `opal-amgt-scoped-api`: CodeSha256 `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=` @2026-09-23T22:02:35Z,
  equal to `2.0.0_SA_COO~Z`'s signed candidate ZIP (established in the Peers brief). Env: the two table names only.
- Chatter producer `amgt-resapp-chatter-axis`: CodeSha256 `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=`, 669,924
  bytes, @2026-09-19T09:49:46Z, python3.12, 60 s, 128 MB, no environment. The local build artifact
  `infra/aws/terraform/harvest/.build/chatter-axis-producer.zip` has the SAME digest and size. Inside that zip
  `chatter_axis.py` is 37,443 bytes and `pool_reader.py` 24,238; at HEAD they are 40,666 and 30,850, the delta being
  commit `fd9449f246` (2026-09-22, `0.9.0_WK_AMGT_HARVST~7`, "chatter axis ranks from the graded chatter_daily
  table"). `DEFAULT_SOURCE = "legacy"` at `chatter_axis.py:427`. Schedule `amgt-resapp-chatter-axis-daily` ENABLED,
  `cron(0 10 * * ? *)` UTC; one invocation and zero errors on each of the last three days. Run lines: 2026-09-16
  to 09-18 `tickers_considered=191 rows_ranked=10 names_read=250 names_with_links=3`; 09-19 `rows_ranked=3`; 09-20
  to 09-23 `rows_ranked=2`, `names_with_links=3`, `fallback_reason=None`, universe `pool:universe/v1/2026-09-16.json`.
- Price producer: `integrations/bloomberg/research/price_axis_pull.py`, box-side, `argparse` main, no Lambda, no
  local scheduled task matching price/axis/pull (the box's task list carries `OPAL_BBGTML_daily_pull` and others,
  none for this producer). Last COMPLETE pointers `TRENDING_PRICE#2026-09-15` and `BREAKOUT_PRICE#2026-09-15`
  (32 rows each, generations `20260917T222503Z-c35c4` / `20260917T222505Z-45dc4`, row `computed_at`
  2026-09-16T20:20Z, coverage vintage text "already-crossed-movement rows written by the box-side pull,
  re-published through the C-RANKING-GENERATION contract by AMGT-rk-20; NO NEW VENDOR CALL").
- Table `opal-harvest-security-metrics`: 305 items, GSI `axis-rank-index`. 22 `_CURRENT` pointers (complete scan):
  TRENDING_CHATTER 09-15..09-23 all COMPLETE with row counts 10,10,10,10,3,2,2,2,2; BREAKOUT_CHATTER 09-15..09-23
  all EMPTY, from 09-19 carrying `empty_reason NO_SIGNAL_IN_WINDOW 188-189 of 191`; TRENDING_PRICE 09-10 and 09-15
  COMPLETE (32); BREAKOUT_PRICE 09-10 EMPTY (legacy republish), 09-15 COMPLETE (32).
- Rankings, direct invokes 02:11Z with `x-firm-id: opal`, `limit=10`, all HTTP 200:
  Trending x Chatter: CROSSED / MEASURED, `dated: true`, as_of 2026-09-23 for requested 2026-09-24, SERVED 2 of 2,
  rows BA US (rank 1, score 0, raw_chatter_count 0, window_total_count 1) and HD US (rank 2, score 0,
  window_total_count 2), both `identity_status MEASURED` with `security_key`.
  Trending x Price: CROSSED, `dated: true`, as_of 2026-09-15, SERVED 10 of 32; head PBR US 19.29%, VLO US, BP/ LN,
  BBSE3 BZ, 9433 JP; one row of 32 (`SLB`) carries no `security_key` (UNRESOLVED).
  Breakout x Chatter: CROSSED, as_of 2026-09-24, `dated: false`, ABSENT ("no generation pointer at
  BREAKOUT_CHATTER#2026-09-24 ... not an empty membership") although the axis carries an EMPTY commit for every
  day 09-15..09-23.
  Breakout x Price: CROSSED, `dated: true`, as_of 2026-09-15, SERVED 10 of 32.
- Time series, direct invokes 02:20Z, 30-day window: Trending x Chatter for BA US and HD US: 30 generation entries
  (9 SERVED, 21 ABSENT), BA 6 points, HD 5, `read_completeness.complete true` (18 of 18 keys). Trending x Price for
  the head five: 2 SERVED dates (09-10, 09-15), 2 points each. Breakout x Chatter: 9 EMPTY, 21 ABSENT, 0 points. A
  first invoke with only `rawQueryString` returned empty series because the handler reads
  `event.queryStringParameters`; the gateway supplies that field, so this was a synthetic-event artifact.
- Watchlist GET for firm `opal`: HTTP 200, `[]`. No-firm control: HTTP 401 "missing edge-injected X-Firm-Id".
- Refresh POST `{security_key: BA_US_Equity}`: HTTP 200 `{refresh: "declared", carrier: {route: "POST
  /api/private/research/pull", queue: "opal-research-pull-requests"}, note: "... enqueues nothing itself ..."}`.
  The carrier exists live: gateway route `POST /api/private/research/pull` (CUSTOM, integration `mefv2t5`), function
  `opal-research-pull-enqueue` @2026-09-11T19:40Z, queue `opal-research-pull-requests` with 0 visible and 0 in-flight
  messages. The consumer `integrations/bloomberg/research/pull_consumer.py` is a person-started drain-and-exit
  poller; no such process on this box at 02:17Z and no scheduled task.
- Overlay for `BA_US_Equity` 02:11Z: identity MEASURED; `axis_reads` point_status ABSENT on TRENDING_CHATTER (and
  the other three; the point read follows today's pointer only, `read_point_record` :656-690, no fallback);
  `chatter: null`, `price: null`; 14 header figures (Bloomberg DAPI, vintage 2026-09-19T07:53Z); description ABSENT
  (no CIE_DES header, drafting sentence failed the describes-the-business test); feed SERVED, 1 item, social "no
  source measured (S13)"; posture SERVED, verdict `hold` vs `DE_US_Equity` as of 2026-09-15;
  `bloomberg_session_state UNKNOWN`.
- Freshness GET: HTTP 200 with rows, denominators and read records (an auxiliary route, reachability and shape
  only, per the contract's ruling on the five auxiliary routes).
- Served bundle: the same PROD chunk `assets/index-4rpf7wvH.js` carries the panel (`Universe discovery`,
  `lead-panel/rankings`). Portal source: `types.ts`, `GenerationCaption.tsx` and `RankedList.tsx` contain 0
  occurrences of `dated` or `requested_as_of`; the panel header's timestamp is `generated_at` (the adapter's clock
  at read time); `LeadPanel.tsx` reads `refreshMutation.isPending` and never its result; `RankedList.tsx:226`
  navigates on `row.security_key` and `:251` renders UNRESOLVED without navigating; `AuthContext.tsx:99,136` parses
  `firmId` from the token and `useStarredList` is enabled only when it is present.

NOT invoked: a signed-in browser walkthrough; the edge header injection (cited from `1.0.0_SA_CTO~Z`'s C4
measurement); star/unstar; the pull enqueue; any producer; any Bloomberg call.

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO/deliverables/LEAD_PANEL_END_TO_END_GAP_BRIEF_20260923.evidence.json`

## Adapter map

| Surface / firm | Provider and intended endpoints | Existing work | Gap |
|---|---|---|---|
| Ranked list, any permitted firm (data not firm-partitioned) | DynamoDB `opal-harvest-security-metrics` via `GET /api/scoped/amgt/lead-panel/rankings/{m}/{s}`; JWT -> `auth-validator-edge` -> `x-firm-id` | `resolve_axis` + `read_rankings` (pointer, row-count check, 14-day dated fallback); `useLeadPanelRankings`; `RankedList`, `GenerationCaption`, `ResolutionNote` | Chatter input dry (3 of 250 names with links); price generation stale (09-15) and unscheduled; `dated` not carried to the screen; EMPTY-every-day axis reads ABSENT before 10:00Z |
| Chart (time series) | Same table via `/timeseries` (BatchGetItem of point keys) | `read_rank_series` with `read_completeness` and per-ticker unresolved counts; `RankedChart` refuses an incomplete read | Only the water: chatter 9 of 30 dates, price 2 of 30 |
| Starred (per firm) | Same table, firm from the edge header; `GET /watchlist`, `POST /watchlist/{star,unstar}` | `lib/research/watchlist/store.py`; `useStarredList`, `useSetStarred` | None found on the read; the write was not exercised |
| Refresh (per name) | Should reach `POST /api/private/research/pull` -> SQS `opal-research-pull-requests` -> on-box `pull_consumer.py` -> Bloomberg DAPI | Enqueue Lambda, queue, route and consumer all exist | `/refresh` declares and does not enqueue; client never calls the pull route; client type `{queued}` vs server `{refresh: "declared"}`; result never rendered; consumer not running |
| Security-mode overlay (header) | `/security/{key}/overlay` | `read_security_overlay`: identity, axis point reads, header figures, description, feed, posture, peers | Point reads have no dated fallback (ABSENT on every axis for BA while BA is rank 1 on the list); description ABSENT for BA; `bloomberg_session_state UNKNOWN` |

One row's success does not certify another: the price crosses serving today proves the fallback, not the producer.

## Start-to-finish walk

### 1. Sign-in -> `/security-analysis` -> Lead Panel mounts -- INCOMPLETE (shared first hop, B00 / E0)

What exists: `App.tsx:447-448` (`ProtectedRoute requireDev requireAdmin`), `SecurityAnalysis.tsx` renders `LeadPanel`
once above the tabs; the served PROD chunk carries it. `2.0.0_SA_COO~Z`'s STATUS.md: E0 NOT_EVALUATED, waiting on
an identity with `user.role==='admin'` and `claims.userType==='Dev'` (Andrew's input).

The exact mismatch: none in this surface's code; unexercised.

Close: E0 as B00 states it. This brief adds nothing to it.

### 2. Panel -> `useLeadPanelRankings(movement, subject)` -> `GET /lead-panel/rankings/{m}/{s}?limit=10` -- WORKS

What exists: `LeadPanel.tsx:262-270`, `useLeadPanelApi.ts:41-49`, `amgt-lead-panel.ts:65-72` (`crossedPath` lower-cases
both controls), `api-client.ts` (bearer, refresh-then-retry). Field contract: the client's `RankingSet`
(`types.ts:181-204`) types every field the route serves except `dated` and `requested_as_of` (hop 6).

Close: nothing; exercised by E0.

### 3. Browser -> CloudFront `/api/scoped/amgt/*` -> edge -> gateway -> `opal-amgt-scoped-api` -- WORKS (declared + live; edge not exercised here)

What exists: as in the Peers brief hop 3; `_firm_id` fails closed (measured: 401 without the header).

Close: nothing beyond E0.

### 4. `resolve_axis` -> `read_generation_pointer` -> `read_generation_rows` -> rows served -- WORKS

What exists: `scoped_amgt.py:312-357` (four PRODUCER_DECLARED crosses, `movement_gate.producer_declared_axes()`
returns all four), `:413-508` (pointer, generation fields, whole-partition query, row-count check with one retry,
SHORT_READ / OVER_READ refusal), `:584-653` (`read_rankings`, dated fallback, `limit` as the head of the verified
generation). Measured: every cross resolves CROSSED / MEASURED; Trending x Chatter served 2 of 2, both price
crosses 10 of 32, all rows in producer order with `security_key` and `identity_status`.

The exact mismatch: none in the read. One shape note for hop 6: `read_rankings` computes "today" as
`_today()` in UTC and the chatter producer runs at 10:00Z, so every read between 00:00Z and 10:00Z serves the
previous day `dated: true`; that is correct behaviour, and it is why the `dated` flag matters on the screen.

Close: nothing.

### 5. Chatter producer: pool articles -> `compute_chatter_axis` -> generation + pointer (daily 10:00Z) -- INCOMPLETE

What exists: `lib/research/metrics/chatter_axis.py` (P-1 pool reader, union universe from `universe/v1`,
generation writer, EMPTY commits with `empty_reason`), the Lambda and its ENABLED daily schedule, healthy for the
last three days, deployed bytes equal to the local build zip. Also at HEAD: `gold_daily_mention_scores` reading
the graded `chatter_daily` gold table (HVST-h-7, `fd9449f246`), behind `DEFAULT_SOURCE = "legacy"`.

The exact mismatch: the deployed zip predates `fd9449f246` (its `chatter_axis.py` is 37,443 bytes against 40,666
at HEAD) and the default source is `legacy` either way, so the producer ranks over `names_with_links=3` of 250 and
the served Trending x Chatter list is two names with `score 0` and `raw_chatter_count 0` (ranked on
`window_total_count` 1 and 2), while Breakout x Chatter commits EMPTY daily with `NO_SIGNAL_IN_WINDOW 189 of 191`.
This is the HARVST gold cutover (H03 in the AMGT gap register; B09 / H1-H4 in the contract): the reader exists,
the role lacks the gold prefix, the default is legacy, the zip is old. The empty-arm mechanics are correct and
disclosed; the input is what is missing.

Close: the H03 cutover as one pinned candidate from `2.0.0_SA_COO~Y`: rebuild the zip from HEAD, add the gold
prefix to `amgt-resapp-chatter-axis-role`, set the source to `gold` (an env var the function does not carry today,
or the default), deploy through Terraform, and let the 10:00Z run land. Proof: the next `_CURRENT` pointer for
TRENDING_CHATTER with `row_count` on the order of the universe (not 2), rows with non-zero `raw_chatter_count`, and
the run line's `names_with_links` above 3 with its denominator; the served list then shows those rows through hop
2 unchanged. Owner of the surfaces: `2.0.0_SA_COO~Y` (`lib/research/metrics/{chatter_axis,generation_writer}.py`,
`pool_reader.py`); the deploy is the Terraform act under the never-widen sign-off because it moves served output.

### 6. Price producer: terminal box -> `price_axis_pull.py` -> `generation.py` -> pointer -- INCOMPLETE

What exists: the box-side puller (argparse main, Bloomberg DAPI at 127.0.0.1:8194), the generation writer
(AMGT-rk-3) mirroring the chatter contract, two COMPLETE generations for 2026-09-15 (32 rows) republished on
2026-09-17 by rk-20 from earlier bare partitions.

The exact mismatch: no owner, no trigger, no schedule; the newest price generation is nine days old and the list
is served only by the 14-day dated fallback, which stops finding it on 2026-09-29, after which Trending x Price
and Breakout x Price read ABSENT with no rows. And the page cannot say so: `dated` and `requested_as_of` are not in
`RankingSet`, `GenerationCaption` prints the generation id and coverage vintage but not the served date, and the
panel's timestamp is `generated_at`, the adapter's clock, so a reader sees a fresh timestamp over a list computed
for 2026-09-15.

Close: (a) one named owner and one stated trigger for the price pull on the terminal box (a scheduled task in the
`OPAL_BBGTML_daily_pull` family, after the market close, running `price_axis_pull.py` then `generation.py`), and one
run now; proof: a COMPLETE pointer at `TRENDING_PRICE#<today>` and `BREAKOUT_PRICE#<today>` with 32-ish rows and a
run line. [SUPERSEDED 2026-09-24 ~02:5xZ, old bytes retained: "Andrew's per-use word is not needed for a producer
that already exists and pulls only PX_LAST for the landed universe" -- REFUSED by `1.0.0_SA_CTO~Z` (msg 25175,
`CLOSER_PROPOSE_LEADPANEL_20260924.md` @`d2bbf82b3f`): the price pull reaches Bloomberg DAPI at 127.0.0.1:8194
and CLAUDE.md's hard stop reads "availability is not authorization"; that a producer exists and is narrow is an
argument about magnitude, and the rule is about authority. Accepted by this seat. Andrew then gave the word (R-15
@`884475c5a1`, ~02:4xZ, "you have egress for whatever calls you want", recorded narrowly as the price pull, the
Refresh proof to LANDED, and the CTO's read-only checks); `bloomberg_health` read `ok: true` at 127.0.0.1:8194 at
that moment, which closes this brief's `bloomberg_session_state UNKNOWN` for reachability only.] The first
scheduled fire is a production schedule and goes through the deploy ledger. (b)
Frontend: add `dated: boolean` and `requested_as_of: string` to `RankingSet`, render "served from <as_of_date>,
requested <requested_as_of>" in `GenerationCaption` when `dated`, and switch the panel timestamp to `as_of_date`;
proof: the offline harness fixture with `dated: true` renders the sentence, and the live Price list shows
"served from 2026-09-15". Owner: `2.0.0_SA_COO~Z` (portal rows) for (b); (a) is a parked line for the CTO to name
an owner, since the terminal box's schedules are not a row in the contract's ownership table.

### 7. Breakout x Chatter before the daily run: ABSENT where the axis is EMPTY -- MISMATCHED

What exists: `_find_latest_served_pointer` (`:558-582`) walks back only to a COMPLETE pointer, by design ("an EMPTY
commit ... is a real state AT ITS OWN DATE"). `RankedList.tsx:187-199` renders a distinct EMPTY sentence with the
producer's `empty_reason`.

The exact mismatch: an axis that is EMPTY every day (nine of nine) has no COMPLETE pointer to fall back to, so from
00:00Z to 10:00Z the read for today is ABSENT ("no committed ranking exists for this date") and the reader never
sees the EMPTY sentence with its `189 of 191 NO_SIGNAL_IN_WINDOW` reason; after 10:00Z it flips to EMPTY. Two
different screens for one unchanged fact, selected by the clock. The design note is right that EMPTY must not
stand in for a LATER date silently; it is wrong that the page has no way to show "yesterday's committed ranking
was EMPTY" beside today's ABSENT.

Close: carry the nearest earlier pointer's status and `empty_reason` on the ABSENT arm as `previous_generation:
{as_of_date, state, empty_reason}` (no rows, no promotion), and render one line under the ABSENT sentence:
"the last committed ranking, 2026-09-23, was EMPTY: NO_SIGNAL_IN_WINDOW 189 of 191". Proof: the 02:00Z read of
Breakout x Chatter shows both lines; the 11:00Z read shows the EMPTY sentence alone. Owner `2.0.0_SA_COO~Z`
(`scoped_amgt.py` and the portal rows). Once hop 5 lands, this axis should stop being EMPTY and the case becomes
the negative control.

### 8. Row click -> Security mode -> `/security/{key}/overlay` -> header + per-axis points -- MISMATCHED

What exists: `RankedList.tsx:226` sends `row.security_key`; `read_security_overlay` (`:1904-2000`) resolves once
and reads the name's point on all four crosses via `read_point_record`, plus header figures, description, feed,
posture and peers; `SecurityOverlay.tsx:52-66` names each point state; `HeaderBrief`, `PostureHeaderLine`.

The exact mismatch: `read_point_record` (`:656-690`) follows only today's pointer and has no dated fallback, while
`read_rankings` does. Measured for BA at 02:11Z: the list says BA is rank 1 on Trending x Chatter (served from
09-23), the overlay says `point_status ABSENT` on every axis and `chatter: null`, `price: null`, rendered as "no
committed chatter ranking for today". For the price crosses this is true every day since 09-15 whatever the
hour. The two reads disagree about the same name because they use different fallbacks. Secondary: `description`
ABSENT for BA (no CIE_DES on the block, drafting sentence failed the test), `bloomberg_session_state UNKNOWN`.

Close: give the point read the same 14-day dated fallback as the list read (`read_point_record` accepting the
served date and carrying `dated` and `as_of_date`), and render "rank N on <as_of_date>" in the overlay. Proof: the
BA overlay shows rank 1 for Trending x Chatter on 2026-09-23 and rank 26 for Trending x Price on 2026-09-15 with
the dates, on the same response the list read agrees with. Owner `2.0.0_SA_COO~Z`. Description and session state
are parked: the description needs a Bloomberg header field the block does not carry (a data-source question,
Andrew's), the session state is the terminal box's report and is not on this thread.

### 9. Refresh -> `POST /refresh` -> (should be) pull route -> SQS -> on-box consumer -> Bloomberg -> LANDED -- MISMATCHED

What exists: the button (`LeadPanel.tsx:235-245`, `useRequestRefresh`), `requestRefresh` typed `{queued: boolean}`
(`amgt-lead-panel.ts:113-118`), the route `POST /api/scoped/amgt/refresh` returning `{refresh: "declared",
carrier: {...}}` (`:4022-4040`), and the whole real carrier: route `POST /api/private/research/pull` (CUSTOM
authorizer, live), function `opal-research-pull-enqueue` (writes `packs/<key>/status.json REQUESTED`, sends one SQS
message), queue `opal-research-pull-requests` (empty), consumer `pull_consumer.py` (health check, then
`model_block_pull` stage functions, status FETCHING / LANDED / FAILED, drain-and-exit, person-started).

The exact mismatch, four field-level facts: the client calls `/refresh`, never `/api/private/research/pull`; the
server answers `{refresh, security_key, carrier, note}` and the client reads `queued`, which is `undefined`; the
panel renders only `isPending`, never the result, so the button spins and stops with no visible outcome either
way; and the consumer is not running, so even a message that reached the queue would sit there until a person
ran the poller (no DLQ, by design). This is S02 in the gap register, confirmed on deployed bytes.

Close: point `requestRefresh` at `POST /api/private/research/pull` with `{ticker}` in the enqueue Lambda's own
contract (`_extract_ticker`), type the response as that Lambda returns it, render the outcome (REQUESTED with the
status key, or the refusal), and name the consumer's trigger on the terminal box (a scheduled `pull_consumer.py`
drain after each enqueue window, or a person's documented act). Proof: one click on BA on the live stack yields
`packs/BA_US_Equity/status.json` REQUESTED, one message received and deleted by the consumer, status LANDED with
raw/derived keys, and the overlay's header figures carrying a new vintage. The enqueue is a write and the pull is
a Bloomberg call, so the proof run needs Andrew's per-use word. Owner `2.0.0_SA_COO~Z` (portal client and
`scoped_amgt.py`); the consumer's trigger is the same parked line as hop 6(a).

### 10. Watchlist: `GET /watchlist` -> `list_starred(firm)` -> starred filter; star/unstar -- WORKS (read); write not exercised

What exists: `store.py` on the same table keyed by the edge firm; the read returned `[]` for firm `opal`;
`useSetStarred` invalidates only the starred key. The write is a pure marker with no refresh coupling, as the
2026-09-11 ruling requires.

Close: nothing; exercise one star and one unstar under E0 (W1) and confirm the list filter and that no rankings
key was invalidated.

## Recommended completion sequence

1. **The live thread.** One named person with the admin + Dev identity, on the served stack: sign in, land on the
   Lead Panel with Trending x Chatter selected, see the resolution line "Served by the producer partition
   TRENDING_CHATTER", the generation caption, two rows (BA US, HD US) with their identity, click BA US, see the
   header figures and Posture line. Crosses hops 1-4 and 8 on today's data. First-hop owner `2.0.0_SA_COO~Z`;
   the identity is Andrew's input. One trace artifact.
2. **Water in the chatter pipe** (hop 5): the H03 gold cutover, one pinned candidate from `2.0.0_SA_COO~Y`, deployed
   under the never-widen pair. Turns the two-row list into a ranking and should end the EMPTY streak on Breakout.
3. **Dated on the screen and on the overlay** (hops 6b, 8): carry and render `dated` / `as_of_date`; give the point
   read the list read's fallback. Two portal-and-adapter changes by `2.0.0_SA_COO~Z`, one pin.
4. **Price producer owner and run** (hop 6a) before 2026-09-29, when the fallback expires.
5. **Refresh wired to its carrier** (hop 9), with the consumer's trigger named; proof run on Andrew's word.
6. **ABSENT beside EMPTY** (hop 7), which becomes a negative control once step 2 lands.
7. Enrichment: the description source (Bloomberg header field), the session-state report, the SLB identity
   (one unresolved row of 32), and the chart's density, which follows from steps 2 and 4.

## Acceptance

One reconciled trace per case, each following one control selection through the route's resolution record, the
pointer it followed (`generation_id`, `state`, `row_count`, `as_of_date`, `dated`), the rows served, and the
rendered resolution line, caption, rows and row states.

Cases: CROSSES {Trending x Chatter; Trending x Price; Breakout x Chatter; Breakout x Price} x VIEWS {list; chart;
starred-only} x HOURS {before 10:00Z (yesterday dated); after 10:00Z (today)} plus SECURITY MODE {BA_US_Equity
(resolved, on the chatter list); PBR_US_Equity (resolved, price rank 1); a row with `security_key` null (SLB, must
not navigate)} plus ACTIONS {star then unstar one name (W1); Refresh one name to LANDED (F1, Andrew's word)} plus
FAILURE CASES {expired session (401 -> refresh -> retry); a SHORT_READ refusal (render the refusal, no rows); a
series with `read_completeness.complete false` (chart refuses); the no-firm 401}.

## Evidence anchors and limits

Source inspected at workspace `cd0268a4f4` / `d350781052` (SITEZ) and portal `10141b6d0b` (DEV; `origin/DEV`
`c1ac41ec` is 7 hours newer and was not diffed for this surface). Verified fresh: both deployed functions'
digests and configuration; the local chatter zip and its members against HEAD; the schedule, invocation and error
metrics and ten days of run lines; the complete pointer scan; thirteen direct invocations; the pull route, function
and queue depth; the process and task lists on this box; the served chunk. Not verified: a signed-in walkthrough;
the edge injection; any write; the CloudFront behavior on the live distribution (declared plane only).

- `lib/research/api/scoped_amgt.py` (`resolve_axis` 312-357, pointer and generation reads 413-556,
  `_find_latest_served_pointer` 558-582, `read_rankings` 584-653, `read_point_record` 656-690, `read_rank_series`
  825-955, watchlist 3164-3177, `_query` 3878, refresh 3825-3831 and 4022-4040)
- `lib/research/metrics/chatter_axis.py` (30-60 input, 424-427 source map and default), `movement_gate.py`
- `lib/research/price/generation.py`, `integrations/bloomberg/research/price_axis_pull.py`,
  `integrations/bloomberg/research/pull_consumer.py`, `infra/aws/lambda/research/pull_enqueue/lambda_function.py`
- `infra/aws/terraform/harvest/chatter-axis-schedule.tf`, `.build/chatter-axis-producer.zip`
- `portal/src/pages/SecurityAnalysis/components/{LeadPanel,RankedList,RankedChart,GenerationCaption,SecurityOverlay,HeaderBrief}.tsx`,
  `hooks/useLeadPanelApi.ts`, `types.ts:26-290`, `constants.ts`, `portal/src/api/endpoints/amgt-lead-panel.ts`,
  `portal/src/contexts/AuthContext.tsx:99,136`
- `org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_MVP_RESEARCH_20260923/GAPS.csv` rows S02, H03 (a different seat's
  earlier read of the same two gaps; corroborated here on deployed bytes)

## Andrew-direct request -- verbatim record

Channel: this terminal (Claude session launched as `4.0.0_SA_CRO~Z`), 2026-09-24 ~02:0xZ (2026-09-23 evening
Eastern), the third prompt of the session.

> /closer trace AMGT "Lead Panel"
