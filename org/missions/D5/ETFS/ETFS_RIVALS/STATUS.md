# ETFS_RIVALS (rivalfunds) -- status (FULL; LIVE = rounds 15-27 at pin 325bd4e0f8; round 28 built: RIV-aw-1 merged, RIV-tc-1 held on its branch; the 2026-10-09 11:00Z run grades tw-1 and opens the order of acts below; the switch is unset)

Seat `2.0.0_SA_COO~RV` (CLAUDE). Mode FULL (`/canonical-drive`, hourly session cron; authority `org/ref/LIVE_ARMS.md`
~RV row and the relaunch record of 2026-10-07 ~08:2xZ). Reviewer `3.0.0_SA_CVO~RV`. Open calls on this project are being
ruled by `1.0.0_SA_CTO~Z`.

As of 2026-10-08 ~07:1xZ. The drive logs are the hour-by-hour record:
`org/tier1_exec/2.0.0_SA_COO~RV/drive_log_20261007T{08,09,10,11,12,13,14}Z_opal_bloomberg.md`.

## Round 27 (FWD-24, the vendor request OFF) -- where it stands

Issued @21b3614f93 (three cells), amended @9c349b8d0a (a note). Packet `deliverables/2.0.0_SA_COO~RV/round27/L8_PACKET_ROUND27.md`
@09e99a3532. CVO slug @f78a9b6cb1 (ADJUDICATION_v35.Z): ho-1 J1 MET, rk-1 J1 MET, tw-1 J1 owed (C-S80).

| cell | state | what is next |
|---|---|---|
| RIV-ho-1 (`history_owed.py`, new) | MERGED aca932cd3f. Live read 2026-10-08: 742 securities, 184,600 units owed over 251 dates | nothing; it is called only when the switch is on |
| RIV-rk-1 (reader: a close only on its own trading date) | MERGED d99155c49a. From the branch: 0 moved rows of 6,066 and 1,406; 13 of 13 charts as served. NOT deployed to the Lambdas | a never-widen pair, then the Lambda deploy, AFTER the 11:00Z run (ledger r26 L4 reads the round-26 package) |
| RIV-tw-1 (the daily leg's top-up writer) | complete on branch `wk-ETFS_RIVALS-19` @de25db03ea (worktree `C:/tmp/wk-riv-r27-19`), NOT merged. Pair WHOLE: COO half `round27/NEVER_WIDEN_HALF_COO_R27_TW1_MERGE.md`, CTO half msg 31588 @d969c62f46 | merge AFTER the 2026-10-08 11:00Z vehicle run is read (ruling msg 31584); the first scheduled run after the merge is the pair's read and tw-1's J1 |

- The switch is the environment variable `RIVALFUNDS_HISTORY_OWED`: OFF unless exactly `print` or `ask`; set nowhere on this
  box. `print` needs a one-line ask to 1.0.0_SA_CTO~Z naming where it would be set; `ask` waits on Andrew's recorded answer
  relayed by the CTO, and (CTO half C2) on the writer storing a currency and each close's trading date, and on a ruled cap.
- Standing term (ruling msg 31596, row Z-S75): before ANY merge to site-Z CLOUD, list the merged paths against
  `round27/vehicle_load_set.json` (18 modules the vehicle's two working-tree legs load); a merge touching one carries a
  pair or a stated reason it needs none. The rk-1 merge touched one (`gold_holding_contribution.py`) unpaired: left in
  place by that ruling; the 11:00Z log read grades it (ImportError or a new top-level failure = revert the same hour).
- For the round-28 list: top-up rows carry no currency; the leg passes the report date as the owed window's end;
  `HISTORY_OWED_CAP` 5,000 is unruled; row Z-S73 and the day-early 2026-09-29 pull are untraced; two cell ids (rk-1, cu-1)
  each name two orders (row Z-S74) -- list existing ids before naming a cell.

## 2026-10-08 11:00Z -- the Terminal was signed out (row Z-S76)

- Vehicle log `bbg_tplus1_20261008_070001.log`: rivalfunds legs exit 93 and 97, nothing written, no import failure; the
  names step was NOT reached, so the run graded neither round-27 merge. RIV-tw-1's merge stays HELD until a vehicle log
  whose enrichment leg reaches the names step is read (the re-pull after a human sign-in, or the next day's run).
- Page date=2026-10-08 published 11:06:19Z: 11 of 13 funds updated (CGIC, SCHY held), no close of 2026-10-07.
  Lambda chain 337.5 s, publish 1,015 MB. Ledger r26 CLOSED 4 of 4; r22 L4 closed, L5 = the 13:00Z sweep.
- Owner of the sign-in and re-pull: 0.0.3_BG_BBGTerminal and a human (CTO msg 31689). Not this seat.
- AFTER the re-pull's log shows both rivalfunds legs landed: ONE republish of 2026-10-08, no pair, on the four terms
  of CTO ruling msg 31697: (1) the payload is the one run under ledger `etfs-rivalfunds-r26` leg L3 (round 26, 01:41Z:
  only publish-page, refresh_a1 true) -- name it in the record; (2) print the keys it may write before, and the same
  keys with sizes and times after; (3) funds_updated and both tables before and after, plus one hand read of a CGIC or
  SCHY holding's weight against its Bloomberg bronze object; (4) once, on 2026-10-08 only -- a re-pull landing on a
  later day republishes nothing for today without a new ask.

## 2026-10-08 12:20Z to 13:08Z -- recovery, the writer's merge, the sweep

- 0.0.3_BG_BBGTerminal re-ran both rivalfunds legs (logs `bbg_recovery_rivalfunds_20261008_122034Z.log`,
  `..._collector_20261008_122319Z.log`): enrichment OK (581 market rows for 2026-10-07, 578 closes; names step ran on
  the merged reader; no HISTORY OWED line), collector OK. Enrichment ran before the collector: it reads G1
  canonical_shape, which only the Lambda chain builds, so the order did not change what it read.
- RIV-tw-1 MERGED @93264049f6 under its whole pair (CTO ruling msg 31740). All three round-27 cells are on site-Z CLOUD:
  suite 910 passed, 3 skipped; 39 of 39 check files PASS. No round-27 worktree remains. The switch is unset. tw-1's J1
  and the pair's read: the first scheduled vehicle run that pulls (2026-10-09 11:00Z).
- The 13:00Z sweep (486.4 s, 1,002 MB) published 2026-10-08 at 13:08:17Z: 13 of 13 funds updated, 2,252 of 2,252 fund
  sections, 6 of 6 checks PASS, AI account in 13 of 13 panels, 0 naming a to-date period. The one manual republish
  ruled in msg 31697 was NOT used: the sweep is the scheduled product and did it. Ledger r22 CLOSED 5 of 5; r26 CLOSED.
  No rivalfunds ledger entry is open.
- NEXT: the ONE round-27 Lambda deploy (the packager stages the whole rivalfunds folder, so all three cells go at one
  pin) under a never-widen pair; before and after from a real run of 2026-10-08 on the round-27 code.

## 2026-10-08 14:57Z -- round 27 DEPLOYED

- Pin 325bd4e0f8 in the five Lambdas (ledger `etfs-rivalfunds-r27`: L1 CLOSED, L2 OPEN = the 2026-10-09 11:00Z chain and
  13:00Z sweep). Pair: COO half `round27/NEVER_WIDEN_HALF_COO_R27_DEPLOY.md` @d9f31a4fb0, CTO half @4457ff34cf.
  Rollback: a plan at pin 0576fb051f. Deploy tree `C:/tmp/rv-r8` is detached at 325bd4e0f8; `C:/tmp/rv_apply27.tfplan` is spent.
- First run of the package (CTO ruling msg 31818): one publish of 2026-10-08 at 15:07Z, OK, 132.3 s, 930 MB; one
  input_census object written and nothing else; page byte-equal to the 13:08Z page
  (`round27/SERVED_READ_2026-10-08.after_r27.md` @0c26726e2b).
- The seat gate warned that a COO does not apply. CTO: the next apply is the executor seat's (a task order to
  0.7.0_AE_CloudOps~RV), as the gate says.
- Site-Z CLOUD was merged with origin and pushed by 0.0.0_AB_MSTR~Z (origin 2d0d4296bf, its read, 15:1xZ). The merge
  changed `lib/opal_naming.py` (+12, the name-typing checker) and five registry files, which the vehicle and the
  packager both load; the pin predates it. The NEXT deploy carries them: list them in its half.
- `.tools/round-close-check.py` returns MAY-CLOSE over 0 orders for round 27 (row Z-S77: it reads the first status
  tag). Round 27 is not closed: tw-1's J1 is open until the 2026-10-09 11:00Z vehicle run (C-S80).
- ROUND 28 list so far (the CTO's analysis is not in the ledger yet): R19 the AI accounts say "the last 30 days", never
  R30 / R90 / R365 (row C-S83); R20 every dollar figure in an account cites a row (`round28_prep/R20_TXUE_GROUNDING_FAIL_READ_20261008.md`);
  the top-up writer stores a currency and each close's trading date; the owed window ends on the page day; the cap is
  ruled; rows Z-S73 and the day-early 2026-09-29 pull are read.

## 2026-10-08 ~20:2xZ -- round 28, and THE ORDER OF ACTS FOR 2026-10-09

- Issuance 222194aee0; AMENDMENT 1 to RIV-tc-1 @8d50ab6e32 (cap 20,000). Packet `deliverables/2.0.0_SA_COO~RV/round28/L8_PACKET_ROUND28.md`
  @954c16bb49. Msg 31984 to 3.0.0_SA_CVO~RV READ by that seat at 2026-10-08T21:02:03Z (`get_delivery_state`, read 21:1xZ);
  L9 is the CVO's. The 20:2xZ park is closed.
- **Round-28 analysis: ADDENDUM 7 @0820f6b0b7 (CTO msg 32023, ~21:35Z).** Round 29 cuts nothing. Round 28 closes on three
  paired acts: (1) the aw-1 Lambda deploy (R31); (2) the tc-1 merge after tw-1's J1; (3) the switch-on (R24). R32 (row
  Z-S78): from the next slug, `round` is the task-order round; that header note is 3.0.0_SA_CVO~RV's write.
- **R31 COO half SIGNED** `round28/NEVER_WIDEN_HALF_COO_R28_AW1_DEPLOY.md` @d3d6c3e73f, pin 39889dd4d7.
  - Measured: 0 of 28 addresses differ; 0 of 26 served items change their recheck verdict.
  - CTO half SIGNED `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_ETFS_RIVALS_R28_AW1_DEPLOY_20261008.md`
    @a0ee589cc2 (msg 32046, 22:06Z): the pair is WHOLE; the five conditions stand unchanged.
  - Window: 2026-10-09, after the 11:00Z chain's REPORT lines and before 12:55Z.
  - **PARKED, the apply:** owner 0.7.0_AE_CloudOps~Z, site Z's applier, seated 22:1xZ by 0.0.0_AB_MSTR~Z. Andrew-direct
    ~22:0xZ, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_220xZ_ONE_LAPTOP_APPLIER_EXCEPTION_YES.md`,
    msg 32058. Order `task-orders/ETFS_RIVALS.TO-APPLY-R28-aw1.rivalfunds-lambda-deploy-sitez.md` @137fb33429.
    - Steps 1-3 are DONE (msg 32094, 22:53Z). Plan `C:/tmp/rv_apply28.tfplan` in `C:/tmp/rv-r8` at the exact pin reads
      0/5/0: BRANCH A.
    - This seat read `C:/tmp/rv_plan28.json` itself: 45 changes, 40 no-op and 5 update; each update changes only
      `source_code_hash` and `last_modified`; the daily function's environment is identical.
    - The second GO (apply) is this seat's to send on 2026-10-09, after the 11:00Z REPORT lines are read, inside
      11:15Z-12:55Z.
- RIV-aw-1 MERGED (branch tip a2283fc349). Merged CLOUD: suite 919 passed, 3 skipped; 40 of 42 checks PASS (tc-1.AC1 and
  tw-1.AC1 arm e grade the unmerged tc-1).
- RIV-tc-1 complete on `wk-ETFS_RIVALS-22` @b0b65368fb (worktree `C:/tmp/wk-riv-r28-22`), NOT merged.
- Andrew-direct ~17:1xZ (CTO msg 31926, R24): YES to the standing daily request, up to 20,000 a morning. The ledger's unit
  is returned records (msg 31941).

The order, each waiting on the one before:
1. 2026-10-09 11:00Z vehicle run: read its log (exit codes, names step, no HISTORY OWED line) -> RIV-tw-1 J1 (C-S80) and
   ledger `etfs-rivalfunds-r27` L2's first half; the Lambda chain's REPORT lines (>720 s = BLOCKING).
2. RIV-tc-1's merge: a short pair (a deploy to the vehicle; list its paths against `round27/vehicle_load_set.json`).
3. ONE round-28 Lambda deploy at the pin after that merge, BEFORE 12:55Z so the 13:00Z sweep writes the first `a1-chain/7`
   accounts: a pair; the apply is the executor seat's (R22) -- a task order to it; the pin now also carries origin's
   `lib/opal_naming.py` (+12) and five registry files: list them in the half.
4. The 13:00Z sweep: ledger r27 L2's second half; RIV-aw-1's J1 count (codes 0 of 26, dates 26 of 26, FAILs, attached).
5. The switch `RIVALFUNDS_HISTORY_OWED` to `ask` where the vehicle reads it, under a pair (R24), only after 1 and 2.

**Sections below this one were written before round 23 and are history where they disagree with the title line and this section.**

## Pins

| What | Value |
|---|---|
| Deployed artifact pin | CLOUD **0576fb051f** in the five rivalfunds Lambdas (rounds 15 to 26: the shared reader of gold security_market, narrowed to timed object names), 3,008 MB each. Ledger `etfs-rivalfunds-r26`: L1 to L3 CLOSED, L4 OPEN = the 2026-10-08 11:00Z daily run (first run of gold_canonical_shape and gold_trade_schedule on the shared reader). Ledger `etfs-rivalfunds-r22`: L4, L5 OPEN = the 11:00Z and 13:00Z REPORT lines. Rollback: content pin fd633ec4d2 on branch `rv-deploy-r25mr` (rounds 15-24 + mr-1), then f9f8334ef6. Deploy tree `C:/tmp/rv-r8` |
| Withdrawn plan | `C:/tmp/rv_apply25.tfplan` belongs to the WITHDRAWN round-25 deploy (pin acf83a5716, the un-narrowed readers): never apply it. CLOUD HEAD is deployable again as of round 26 |
| Served page | 2026-10-07; last written 00:11Z 2026-10-08 (RIV-mr-1). The round-26 republish of 01:41Z rebuilt the tables with the new readers and wrote nothing but one input_census object and its state record: the tables' content hash and the page's bytes were unchanged (`round26/served_read_2026-10-07.after_r26.json`). Andrew's look at the round-24 / 25 chart is not yet had |
| PRD | v0.19 ADMITTED (FWD-24: the year of closes kept by the daily leg; the standing request stays OFF until Andrew's recorded answer). Reader census `round25_prep/READER_CENSUS_SECURITY_MARKET_20261007.md` @33e8bbe318 |
| pk-1 / al-1 (parsekey join, pin 92cf1f322b) | Ledger `etfs-rivalfunds-pk1-al1` CLOSED 4 of 4 @b74bdc238b on the 2026-10-07 morning pass |
| Round 14 proof | The 2026-10-07 13:00Z sweep read: four gate items MET (`round14/SWEEP_READ_2026-10-07.md` @93f23ea2f4) |
| Built, not deployed | Rounds 15 to 22 on site-Z CLOUD; last merge c6ac7335a5; suite 876 passed, 2 skipped, 0 failed and 26 of 26 check files PASS at 23d65887ca |
| Deploy pin (prepared) | CLOUD **beb13d39ff**: rounds 15 to 22 plus memory_size 1024 -> 3008 (CTO ruling msg 31149, row Z-S63). Plan 0 add, 5 change, 0 destroy. COO half SIGNED `round22/NEVER_WIDEN_HALF_COO_R22_DEPLOY.md` @b2ed0588f4; CTO half asked 16:58Z |
| Gateway | Release r26 live since 14:03:49Z (2.0.0_SA_COO~O msg 31038); the chart route is not yet exercised: no chart object is served |
| Push state | Rounds 15 to 20 are ON ORIGIN: 0.0.0_AB_MSTR~Z pull-merged origin and pushed, origin CLOUD fad25b1527 (its ls-remote read, msg 30999; re-read by this seat 14:1xZ). Round 21's merge and later were LOCAL at 16:5xZ (origin CLOUD 28e3a2082a by ls-remote; the deploy pin is not on it) |
| Worktrees | None of this project's. Deploy tree `C:/tmp/rv-r8` is detached at beb13d39ff with the packages staged and `C:/tmp/rv_apply22.tfplan` saved |

## Rounds 15 to 19 (2026-10-07)

| Round | Issuance | Cells | What it does | Merge |
|---|---|---|---|---|
| 15 | d06e19f939 | pd-1, pd-2, pd-3, ps-1, tm-1, co-1, bf-1, rt-1, md-1 | 30d / 90d / 365d calendar days (FWD-23); the security dialog's price curve, trade markers, chart object, gateway route, the page's one script, the Bloomberg range backfill (FWD-22) | 8b9455602b, 6bf5bb0251, ca77f9dda6, f7f2cb7c2e, 116eadfa37 (+ fix 370ae7a279) |
| 16 | 49a74229dd | pc-1 | A holding-implied price only for a listing stored as USD; the chart says the currency (row S55; CTO ruling msg 30787) | efea405c1e |
| 17 | 7a27742b3a | nc-1 | No stored currency: no curve, "No price history is stored for this holding yet." (CTO ruling msg 30817) | 1cbee3e716 |
| 18 | 8813da6c04 | tl-1 | The dialog's trade list is written from the chart object's markers (row S56) | 4c10ccc170 |
| 19 | d309f31b5d | ml-1 | The month strip labels each cell with its month, counted back from the window end (row S58) | 233b033a9f |
| 21 | 722eb2804e | pl-1 | The month strip shows every month of its window (13 cells, the two Octobers with their year); the trade list is headed by its window; the chart fills its frame and its currency label clears the axis (CVO ADJUDICATION_v20) | e3ea0014bc |
| 22 | 96792f2f46 (+6ce602bd1e) | pm-1 | The oldest strip cell is marked as a part month; no curve without two prices; markers through the page day; no zero-dollar marker; one security has one key on the page, so GQGU's markers are found (row C-S64; CVO: pm-1 J1 MET, C-S64 REMEDIATED @8ee36f16f5) | c6ac7335a5 |
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

1. ~~The push of site-Z CLOUD~~ DONE 2026-10-07 ~13:51Z (origin CLOUD fad25b1527, holding rounds 15 to 20).
2. ~~The gateway release that serves the chart route~~ DONE: r26 live 14:03:49Z.
3. ~~DONE 2026-10-07 17:3xZ~~ the rivalfunds Lambda deploy at pin beb13d39ff, under a NEVER-2 ledger entry and a never-widen pair (COO half
   signed; CTO half owed). Then ONE republish of 2026-10-07 with `refresh_a1` true, the served grade, and the first-run
   Max Memory Used and Duration of each function (above 720 s is a BLOCKING row before backfill day 1).
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
2. **NFRA_OPLGTW (ask carried by 1.0.0_SA_CTO~Z):** the gateway release that serves the chart route; its commits are on
   origin. The Lambda deploy waits on the release (the page's script calls the new route).
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
| Z-S57, Z-S61 | OBSERVATION | Repaired in round 20 and SERVED: GQGU's Meta is under one key in both served tables (read 19:4xZ); the 16 remaining same-name pairs are different listings or share classes and stay (CTO ruling msg 31341); the CVO re-reads Z-S57 |
| Z-S63 | BLOCKING, INERT | The deployed daily Lambda used 864 MB of 1,024 MB; the new stages peak at 1,552 MB on site Z. Ruled: 3,008 MB in the same apply; the first runs' REPORT lines are ledger legs |
| Z-S65, Z-S66 | OBSERVATION | Repaired by round 23 (RIV-ks-1) and SERVED 19:19Z: 0 missing; ks-1 J1 MET on the real run (CVO ADJUDICATION_v25); disposition is the CVO's |
| Z-S71 (replaces Z-S69, Z-S70) | BLOCKING, disarmed by round 26 | The 2026-09-29 live object of gold security_market holds 2026-09-30's closes. Round 26 RIV-rg-2 is DEPLOYED: the union reads only objects whose name carries a capture time, so that object is never opened by the price readers; rg-2 J1 MET (ADJUDICATION_v33). Disposition is the CVO's. Still true: the rule is a name's shape plus one named object; round 27 carries the per-close trading date |
| Z-S73 | OBSERVATION | A replay of build-canonical-shape and build-trade-schedule made today does not reproduce the served objects (alike under old and new code); four GQGU trims of 2026-10-01 carry a ticker key in the replay and a CUSIP as served. Read in round 27 |
| Z-S72 | OBSERVATION | The 11:00Z vehicle's enrichment leg loads the module holding the round-25 reader and calls nothing of it; no revert (CTO msg 31489); the first read of the 2026-10-08 vehicle log states the leg's exit code and its security_names step |
| Z-S67, Z-S68 | OBSERVATION, ARMED / INERT | bbg_budget's two checks use different units (surfaced by 0.0.3_BG_BBGTerminal); Z-S68 is this seat's disarm statement: the backfill's guard is check_points, points requested bound records returned. Day 1's log gives the measured ratio |
| Z-S62 | OBSERVATION | The 11:00Z vehicle runs the working tree: round 20's enrichment change first runs 2026-10-08 11:00Z; its log line is owed a read |
| Z-W10-S1 | OBSERVATION | The backfill's one CRNCY lookup is unmeasured at real size (282 keys) |
| Z-S59 | OBSERVATION | Down to 4 of 393 strips, each a marker in the part month before the window's first day (by design, marked with an asterisk) |
| Z-W1-S53 | OBSERVATION | The audit page keeps "History not yet backfilled" (it carries no script by Andrew's word) |
| Z-W2-S16 | OBSERVATION | Chart objects are written only when the page's bytes change |
| Z-W4-S19 | OBSERVATION | 29 gateway-suite failures at base, none in rivalfunds; owner NFRA_OPLGTW |
| Z-W1-S49, Z-W1-S50 | INERT | Carried from round 14 |

## The round analysis (1.0.0_SA_CTO~Z, `ledger/ROUND_ANALYSIS.round20.md` @c9a9e27770)

Seven rulings and the round-21 list. Done from that list: the three reads (`round21/READ_R3_S59_CAUSE.md`,
`round21/READ_R5_R6.md`) and the first display cell (round 21). Owed: the second display cell (the oldest strip cell marked
as a part month; no curve for a holding with markers and no prices, or for a range with fewer than two prices; markers
through the page day; no zero-dollar marker), then the deploy and its served grades, then the backfill's days.
FWD-22 and FWD-23 stay NOT REALIZED until served.

## Not exercised by any run so far

- The served gateway chart route. A page deployed before it serves reads "Chart could not load" in every frame.
- RIV-pd-3 on real data: the AI accounts still name MTD / QTD / YTD until a sweep's AI run on the new build.
- RIV-bf-1 live.

## Standing directives

- Periods are 30d / 90d / 365d CALENDAR days on the rivalfunds page only; QTD, YTD, MTD keep computing and are not shown.
- The page carries exactly ONE inline script; the audit page carries none (@efc0acb127).
- No agent-turn vendor call; Bloomberg only through the scripted vehicle; workers never call a vendor, write S3 or deploy.
- No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact.
