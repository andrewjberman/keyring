# ETFS_RIVALS (rivalfunds) -- status (FULL; round 14 DEPLOYED and proven; rounds 15-20 MERGED on site-Z CLOUD, NOT deployed)

Seat `2.0.0_SA_COO~RV` (CLAUDE). Mode FULL (`/canonical-drive`, hourly session cron; authority `org/ref/LIVE_ARMS.md`
~RV row and the relaunch record of 2026-10-07 ~08:2xZ). Reviewer `3.0.0_SA_CVO~RV`. Open calls on this project are being
ruled by `1.0.0_SA_CTO~Z`.

As of 2026-10-07 ~13:2xZ. The drive logs are the hour-by-hour record:
`org/tier1_exec/2.0.0_SA_COO~RV/drive_log_20261007T{08,09,10,11,12}Z_opal_bloomberg.md`.

## Pins

| What | Value |
|---|---|
| Deployed artifact pin | CLOUD **22844f744f** in the five rivalfunds Lambdas (round 14). Ledger `etfs-rivalfunds-r14` CLOSED @cc02eeac7d |
| pk-1 / al-1 (parsekey join, pin 92cf1f322b) | Ledger `etfs-rivalfunds-pk1-al1` CLOSED 4 of 4 @b74bdc238b on the 2026-10-07 morning pass |
| Round 14 proof | The 2026-10-07 13:00Z sweep read: four gate items MET (`round14/SWEEP_READ_2026-10-07.md` @93f23ea2f4) |
| Built, not deployed | Rounds 15 to 20 on site-Z CLOUD; last merge 42462181c1; suite 865 passed, 2 skipped, 0 failed at 6bee8e3a91 |
| Push state | LOCAL. Origin CLOUD f1260c7754 (ls-remote 12:17Z); site Z carries 189 commits not on its tracking ref |
| Worktrees | None of this project's. Deploy tree `C:/tmp/rv-r8` (pin 22844f744f) and `C:/tmp/rv-replay` remain |

## Rounds 15 to 19 (2026-10-07)

| Round | Issuance | Cells | What it does | Merge |
|---|---|---|---|---|
| 15 | d06e19f939 | pd-1, pd-2, pd-3, ps-1, tm-1, co-1, bf-1, rt-1, md-1 | 30d / 90d / 365d calendar days (FWD-23); the security dialog's price curve, trade markers, chart object, gateway route, the page's one script, the Bloomberg range backfill (FWD-22) | 8b9455602b, 6bf5bb0251, ca77f9dda6, f7f2cb7c2e, 116eadfa37 (+ fix 370ae7a279) |
| 16 | 49a74229dd | pc-1 | A holding-implied price only for a listing stored as USD; the chart says the currency (row S55; CTO ruling msg 30787) | efea405c1e |
| 17 | 7a27742b3a | nc-1 | No stored currency: no curve, "No price history is stored for this holding yet." (CTO ruling msg 30817) | 1cbee3e716 |
| 18 | 8813da6c04 | tl-1 | The dialog's trade list is written from the chart object's markers (row S56) | 4c10ccc170 |
| 19 | d309f31b5d | ml-1 | The month strip labels each cell with its month, counted back from the window end (row S58) | 233b033a9f |
| 20 | 312c34ca27 | bk-1 | Backfill rows feed the price curve only and carry their currency; a range is finished on later days; the trend's parsekey join reads its column (rows S60, S61; CTO ruling msg 30897) | 42462181c1 |

Each round's packet, real-run record and screenshots: `deliverables/2.0.0_SA_COO~RV/round{15..20}/`. The round-19 run
(`round19/DRAIN_END_PACKET.round19.md` @629a94a0e8) is the artifact for the seven open J1 grades.

Measured on the real run of day 2026-10-06 (live inputs, local writes only), latest build:
- Currency: jumps over 3x at the market / implied boundary 0 (was 152 of 598); USD points identical 263 of 263.
- Priced points 49,639 of 174,445 (was 137,292): 335 non-dollar securities draw only the 2 to 3 closes on file and 97
  draw none, until the Bloomberg backfill lands a year of closes.
- Trade list agrees with the chart object on 702 of 702 frames. Month strips labelled on 393 of 393; 382 agree with the
  markers' months.
- Page 1,640,613 B, 15.9 percent under the 1,950,000 cap (round 14: 34.4 percent).

## THE ORDER OF ACTS (each waits on the one before it)

1. The push of site-Z CLOUD (Andrew's word at 0.0.0_AB_MSTR~Z).
2. The gateway release that serves the chart route (NFRA_OPLGTW; cut from origin).
3. The rivalfunds Lambda deploy at a pin holding rounds 15 to 20, under a NEVER-2 ledger entry and a never-widen pair.
   The page's script calls the route, so the Lambdas do not go before the release.
4. The Bloomberg backfill, over two days or more. **It does NOT run before step 3:** the DEPLOYED round-14 rankings stage
   does not ignore backfill rows, so a backfill written to live S3 before the round-20 code is deployed would move the
   served rankings at the next run. The DELTA 0 proof (`round20/delta0_2026-10-06.json`, 13 of 13 funds equal) holds
   for the round-20 code only.

Confirmed by 1.0.0_SA_CTO~Z (msg 30935), with two terms on step 4:
- after the Lambda deploy and BEFORE backfill day 1, read the DEPLOYED rankings stage ignoring a backfill-marked row (one
  planted row in a scratch prefix, or the deployed code's bytes against the round-20 source, by content);
- on day 1, after the first publish with backfill rows present, print the served rankings equal to the publish before it,
  13 of 13.
The Lambda deploy's never-widen pair goes to 1.0.0_SA_CTO~Z as usual.

## What is open, and on whom

1. **3.0.0_SA_CVO~RV:** seven J1 grades (pd-2, md-1, co-1, pc-1, nc-1, tl-1, ml-1) on the round-19 run, RIV-ab-1's J1
   (round 14) on the served 2026-10-07 page, and the slug.
2. **Andrew, at 0.0.0_AB_MSTR~Z:** the push of site-Z CLOUD. The gateway release is cut from origin, so it waits on the
   push; the Lambda deploy waits on the release (the page's script calls the new route).
3. **1.0.0_SA_CTO~Z:** carries the gateway release ask to NFRA_OPLGTW (msg 30755; route shape
   `round15/GATEWAY_CHART_ROUTE_AS_BUILT.md`); the CTO never-widen halves for the Lambda deploy and the backfill run.
4. **2.0.0_SA_COO~RV (this seat):**
   - the COO never-widen halves; then the deploy in the order gateway route -> Lambdas -> backfill dry run -> backfill;
   - the Bloomberg backfill: Andrew-authorized (@96d0ab2f4b, @69c7f24b44), securities of the rivalfunds funds only, about
     365 calendar days, ad hoc on the existing route, ONLY after a day's 11:00Z vehicle run, dry run first, inside the
     bbg_budget ledger; its security list includes formerly-held keys, split by day if over a day's allowance (CTO
     ruling msg 30817). No worker ever calls Bloomberg.

## Open rows (owner 2.0.0_SA_COO~RV unless named)

| Row | Class | State |
|---|---|---|
| Z-S55, Z-S56, Z-S58, Z-S60 | BLOCKING, INERT | Repaired in rounds 16, 18, 19, 20; disposition is the CVO's |
| Z-S57, Z-S61 | OBSERVATION | Served: buying_trend carries 7 securities under two keys; cause read (its G4 read omitted the parsekey column) and repaired in round 20, not yet deployed |
| Z-W10-S1 | OBSERVATION | The backfill's one CRNCY lookup is unmeasured at real size (282 keys) |
| Z-S59 | OBSERVATION | 11 of 393 month strips disagree with the markers' months; a 365-day window's oldest month is off the 12-cell strip |
| Z-W1-S53 | OBSERVATION | The audit page keeps "History not yet backfilled" (it carries no script by Andrew's word) |
| Z-W2-S16 | OBSERVATION | Chart objects are written only when the page's bytes change |
| Z-W4-S19 | OBSERVATION | 29 gateway-suite failures at base, none in rivalfunds; owner NFRA_OPLGTW |
| Z-W1-S49, Z-W1-S50 | INERT | Carried from round 14 |

## Not exercised by any run so far

- The served gateway chart route. A page deployed before it serves reads "Chart could not load" in every frame.
- RIV-pd-3 on real data: the AI accounts still name MTD / QTD / YTD until a sweep's AI run on the new build.
- RIV-bf-1 live.

## Standing directives

- Periods are 30d / 90d / 365d CALENDAR days on the rivalfunds page only; QTD, YTD, MTD keep computing and are not shown.
- The page carries exactly ONE inline script; the audit page carries none (@efc0acb127).
- No agent-turn vendor call; Bloomberg only through the scripted vehicle; workers never call a vendor, write S3 or deploy.
- No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact.
