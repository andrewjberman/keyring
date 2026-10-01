# Security Analysis Lead Panel: end-to-end trace brief

Prepared by 4.0.0_SA_CRO~Z on 2026-10-01 for 1.0.0_SA_CTO~Z's Friday CONTRACT (msg 27500). This is a read-only
assessment with proposed closure requirements. It made no application changes, vendor calls, deployments or schedule
changes. AWS was read only: one `lambda get-function` and S3 list/get through the producer's own reader.

Thread source: brief `docs/briefs/amgt-security-analysis-friday-demo-brief-20261001.md` Part I (@`1391c2f70a`).

## Design finding

The Lead Panel is meant to show two things:
- **Chatter:** which names are being talked about. It reads HARVST's article gold (`chatter_daily`) as one
  per-security, per-month collected count, drawn as bubbles with a month cursor.
- **Price:** which names moved. It reads the 07:00 ET Bloomberg price leg's rankings, drawn as ranked horizontal bars.

Clicking a name opens a header showing that name's latest served (T-1) chatter and price readings. Opal computes ranks
and aggregates in the producers and the scoped API. The page only presents what is served (DSGN's rule).

How far the build is from that design:
- **Price:** the price leg, the scoped API and the rankings fallback work and are worth keeping.
- **Chatter:** chatter is wired to a dead input, and no route aggregates HARVST gold by month.
- **Units:** breakout units are mismatched between producer and page.
- **Selected-name header:** it reads today's date with no fallback.
- **Mislabelled cell:** one header cell reads the wrong axis.

## Current measurement

Deployed bytes read at 04:22:06Z UTC: `lambda get-function opal-amgt-scoped-api`.
- **Configuration:** LastModified 2026-09-30T15:22:01Z, CodeSha256 `/QP4upEVzTjnHV2bAeIXIud0k0DgjDDGrlMgtm0uo7o=`,
  handler `lambda_function.lambda_handler`, python3.11, env `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`.
- **Bundle vs workspace HEAD (sha256 prefix):**
  - `lib/research/api/scoped_amgt.py` `95124d0531b3fe13`, equal to HEAD, which is commit `f044cdd240`
    (2026-09-30 13:36Z);
  - `lib/research/coverage/pool_reader.py` `326240260e13cfb0`, equal to HEAD;
  - `lib/research/metrics/chatter_axis.py` `3b1f5fed285a51b0`, equal to HEAD.
  - So **the deployed API is the repo's code.** Line citations below are at workspace HEAD and hold for the deployed
    function.
- **Live gold read at 04:26:24Z:** through `publication_gold._latest_gold_snapshot_rows("chatter_daily")` (bucket
  `opal-data-harvest`, prefix `amgt/harvest/gold/chatter_daily/`): 52,143 rows, 191 security keys, `data_status`
  DENIED 51,722 / PARTIAL 421.
- **Frontend:** read at portal DEV `b336b141` (2026-09-30 22:16 ET). The deployed bundle was NOT downloaded.
- **Not invoked:** no route was called through API Gateway, and no signed-in walk was taken. The page's sign-in hop is
  inferred from the DSGN UI-walk captures of 2026-09-30T23:53Z, which render served rows.

## Adapter map

| Surface | Producer and endpoint | Existing work | Gap |
|---|---|---|---|
| Chatter (bubbles) | HARVST gold `chatter_daily`; served route: none | the producer's snapshot reader; the timeline routes read it | no monthly route; the chatter axis reads the legacy layout |
| Price (bars) | Lambda price leg, 07:00 ET on the terminal box; `GET /api/scoped/amgt/lead-panel/rankings/{movement}/price` | scheduled since 09-24; dated fallback | breakout units; coverage 29 of 95 |
| Selected-name header | `GET /api/scoped/amgt/security/{key}/overlay` | identity, model block, feed, axis reads | no date fallback; mislabelled cell; dead feed input |

The price rows working does not certify chatter. They have different producers and different storage.

## Start-to-finish walk

### 1. Browser -> scoped API (sign-in, scope, rankings route) -- WORKS

What exists:
- the portal client `src/api/endpoints/amgt-lead-panel.ts`;
- the server route table at `scoped_amgt.py:4660-4695` (18 routes, prefix `/api/scoped/amgt`, `:4221`);
- deployed bytes equal HEAD (above).

The rankings route returns served rows with a dated fallback (`scoped_amgt.py:762-769` ->
`_find_latest_served_pointer`, `:561-583`).

Close: none needed. This hop is the shared first hop, and every later hop crosses it. Owner: AMGT_RESAPP (COO~Z).

### 2. Chatter producer -> rankings -- MISMATCHED

What exists: Lambda `amgt-resapp-chatter-axis`, scheduled `cron(0 10 * * ? *)`, env `CHATTER_AXIS_SOURCE=legacy`
(live configuration, from the RESAPP read at 03:49-04:01Z).

The mismatch:
- The producer reads `publications/v1` and `publication-links/v1`: 7 + 7 objects, newest 2026-09-15, from a harvester
  task that is DISABLED.
- HARVST writes `amgt/harvest/gold/chatter_daily/`, which only the timeline reads (`scoped_amgt.py:4349-4350`).
- Switching to `gold` HOLDs under `ELIGIBLE_FLOOR=10` (`chatter_axis.py:456`), because 0 of 191 names are fully
  covered in September.

Close: the bubbles do not use this producer. The CONTRACT should retire the chatter *rankings* from the Lead Panel and
serve chatter only through hop 3. Re-pointing this producer is enrichment once coverage exists.

### 3. Gold `chatter_daily` -> scoped API -> page (monthly collected count) -- MISSING

What exists:
- One seam to landed gold, `_timeline_snapshot_rows(table)` (`scoped_amgt.py:4336-4346`). It calls
  `publication_gold._latest_gold_snapshot_rows_cached`, which lists the newest `date=` partition, takes its newest
  part, and caches the decode per ETag.
- Its schema, `GOLD_DAILY_SCHEMA` (`publication_gold.py:377-400`), has one row per (`security_key`, `day`) with
  `articles_total`, `mention_count_total`, `publishers_distinct`, `data_status`, and more.
- No route aggregates by month. `TIMELINE_ROUTES` (`:4309-4312`) serve one security at a time.

Where the route should sit:
- Put it in `scoped_amgt.py` beside the timeline routes. Read through the same seam and aggregate on read:
  `sum(articles_total)` grouped by (`security_key`, calendar month of `day`), returning N months back from the latest
  served month.
- **No new storage, so no new S3 address and no LGIC row.** The snapshot is a single 52,143-row parquet that the
  cache already holds warm.
- It needs:
  - a `scoped_amgt_route_table()` entry;
  - the gateway mount in `infra/aws/terraform/harvest/scoped-amgt-api.tf`, diffed both ways by
    `lib/research/api/tests/test_scoped_amgt_mount.py`;
  - a portal client function;
  - the DSGN bubble component.
- Proposed path for the CONTRACT to fix: `GET /api/scoped/amgt/lead-panel/chatter/monthly?months=N`.

Per-row claim fields: so that "collected" is never read as "market chatter" (A VALUE MUST CARRY ITS CLAIM), each row
carries:
- `security_key`;
- `month`;
- `articles_collected` (`sum(articles_total)`);
- `mentions` (`sum(mention_count_total)`);
- `days_with_data`;
- `coverage_class`: the row's DENIED/PARTIAL mix.

What the bubbles would show today (measured at 04:26Z):

| Month | Names with >0 articles | Articles | Top names |
|---|---:|---:|---|
| 2026-01 | 8 | 13 | 992 HK 4, AAPL 2, DELL 2 |
| 2026-02 | 26 | 51 | 992 HK 10, AAPL 5, NVDA 5 |
| 2026-03 | 5 | 7 | 992 HK 2, MSFT 2 |
| 2026-04 | 6 | 6 | AMZN 1, COST 1, HD 1 |
| 2026-05 | 10 | 15 | 992 HK 5, GS 2 |
| 2026-06 | 14 | 28 | 992 HK 5, DELL 3, MSFT 3 |
| 2026-07 | 11 | 23 | BA 8, COST 4 |
| 2026-08 | 29 | 91 | HD 20, COST 11, BA 9 |
| 2026-09 | 38 | 103 | BA 20, AMZN 11, COST 9 |

Close: the route plus its mount. The proof is one call through API Gateway returning 9 months for the 191 keys, with
the September row for BA reading `articles_collected` 20. Every article HARVST lands raises these counts with no route
or page change. That is the coupling between the HARVST backfill and the demo.

### 4. Price producer -> rankings -- WORKS, coverage INCOMPLETE

What exists:
- the price leg, scheduled 07:00 ET on the terminal box since 09-24;
- Trending x Price and Breakout x Price served as of 2026-09-29 (the expected T-1), 32 rows each (RESAPP read).

The gaps:
- The universe is a 34-name file in an old worker folder, which covers 29 of the 95 covered names.
- History is 6 points per 30 days; `price_axis_pull.py:231` uses `prev_trading_day(now)` and has no as-of option.
- It needs the Bloomberg Terminal signed in. It was not at about 00:5xZ.

Close: point the leg at the 95-name universe. The proof is the 07:00 ET run serving rows for more than 29 names.
History is not needed for bars of one period.

### 5. Breakout units: producer -> API -> `RankedList.tsx` -- MISMATCHED

What exists:
- `movement_gate.breakout_pct` returns `(last - baseline) / (baseline + smoothing)`, a FRACTION
  (`lib/research/metrics/movement_gate.py:386-400`; live ASML 0.0921).
- The Trending price score is already a percent (`price/axis.py:36`, x100).
- The API passes `score` through unchanged.
- The page renders `${row.score.toFixed(2)}%` for every price row (`RankedList.tsx:155-157`).
- So ASML's +9.2% reads "+0.09%".

Close: ONE writer, the scoped API (RESAPP).
- Serve every price row with a `score_unit` field. Convert the Breakout x Price score to percent on read, which applies
  uniformly across stored history; changing the producer would mix units across generations.
- The page reads `score_unit` and does no arithmetic. DSGN must NOT also multiply by 100. The RESAPP and DSGN reads
  both proposed fixing this, which is the double-fix risk.
- Proof: the ASML breakout row reads 9.21 with `score_unit: "percent"`.

### 6. Selected name -> overlay -> header cells (date read) -- MISMATCHED

What exists:
- `read_security_overlay` sets `as_of_date = as_of_date or _today()` (`scoped_amgt.py:2105`).
- It calls `read_point_record(served_axis, ticker, as_of_date)` for each axis (`:2123`) with **no dated fallback**,
  unlike `read_rankings` (`:762-769`).
- The producer files T-1, so every name reads "no committed price ranking for today", every day. Measured by the
  RESAPP read: 992 HK is ABSENT at 2026-10-01 and SERVED at 2026-09-29.
- Also MISMATCHED: the bundle's `price` is the TRENDING x PRICE row (`scoped_amgt.py:2165`), but the page labels it
  "Breakout (price)" (`SecurityOverlay.tsx:379`). The page's own `axisRead(bundle, 'TRENDING', 'PRICE')` (`:296`)
  agrees with the bundle, so the label is the defect.

Close:
- The overlay resolves each axis through `_find_latest_served_pointer` and returns per-axis `as_of_date` and `dated`.
  The page labels the cell from the served axis.
- Proof: the 992 HK overlay reads SERVED, as of 2026-09-29, dated true.
- For the 66 of 95 names outside the price generation, the cell will read NOT_IN_GENERATION until hop 4's widening.

### 7. Served rows -> rendered Lead Panel -- MISMATCHED (presentation)

What exists:
- `LeadPanel.tsx` has the List/Chart toggle (`:420-429`).
- `RankedChart.tsx` draws one line chart of rank over time, with neon colours at `:73-86`. Andrew rejected both.
- `RankedList.tsx:263-266` hard-codes `places_moved` as unserved, although the server sends it
  (`scoped_amgt.py:689-727`).

Close (DSGN): remove the toggle and the line chart. Build:
- the bubbles over hop 3, with the month cursor;
- the ranked horizontal bars over hop 4/5 rows;
- the header in the /philosophy card family.

Also remove the `places_moved` hard-code. The proof is one served-data render, looked at (`/frontend-dev`).

## Recommended completion sequence

1. **The live thread.**
   - **Person and setting:** Andrew, signed in on the DEV build, real backend.
   - **Journey:** open the Lead Panel and see bubbles for 2026-09 from hop 3. Step the cursor to 2026-08 and 2026-07,
     and watch BA, HD and COST resize. See price bars from hop 4/5 with correct percent units. Click 992 HK and see its
     header populated as of the latest T-1 (hop 6).
   - **Record:** one trace artifact. It crosses hops 1, 3, 5, 6 and 7.
   - **First hop owner:** COO~Z (RESAPP owns the scoped API).
2. Widen the price universe to 95 names (hop 4). This needs the Terminal signed in.
3. Deepen chatter through the HARVST backfill. No route or page work is needed; the counts in hop 3 grow.
4. Enrichment: re-point the chatter axis (hop 2) once coverage passes the floor; price history backfill (an as-of
   option).

## Acceptance

One reconciled trace per case. Each follows one request from the click, through the route and the gold or rankings
read, to the served JSON and the rendered element.

Cases:
- **Names:** BA (the most collected), 992 HK (price rank 1), and a name with 0 collected.
- **Months:** 2026-09, 2026-08 and 2026-02 (the sparse early month).
- **Failure cases:**
  - a month with no rows (it must render empty, not error);
  - a name outside the price generation (it must read NOT_IN_GENERATION, not "today");
  - a snapshot timeout (it must surface the route's timeout state).

## Evidence anchors and limits

Source inspected at workspace `1391c2f70a` and portal DEV `b336b141`.
- **Verified fresh:**
  - the deployed API bytes against HEAD (04:22Z);
  - the gold snapshot read and the monthly aggregate (04:26Z);
  - every cited line printed at HEAD.
- **Carried from the RESAPP and DSGN reads (03:49-04:06Z), not re-measured:**
  - the chatter Lambda's environment and schedule;
  - the rankings states;
  - the 992 HK point read;
  - the price universe counts.
- **Not done:**
  - the deployed portal bundle diff;
  - a signed-in walkthrough;
  - any API Gateway call.

Anchors:
- `lib/research/api/scoped_amgt.py`
- `lib/research/harvest/publication_gold.py`
- `lib/research/metrics/movement_gate.py`
- `lib/research/metrics/chatter_axis.py`
- `infra/aws/terraform/harvest/scoped-amgt-api.tf`
- `portal/src/pages/SecurityAnalysis/components/{LeadPanel,RankedList,RankedChart,SecurityOverlay}.tsx`

## Andrew-direct request -- verbatim record

The trace was asked for by 1.0.0_SA_CTO~Z (msg 27500, 04:20Z) under Andrew's self-drive word (@`8f56ef5f81`). The
originating order is Andrew's 03:4xZ instruction, recorded verbatim at
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261001_034xZ_AMGT_SECURITY_ANALYSIS_DEMO_FRIDAY.md`. The
chart forms:

> I think chattter is always that bubble chart form, with size being the indicator. I think price is always those
> horizontal bars. No other views for chatter, no other views for price, so that gets rid of the toggle that flips
> between the different charts.
