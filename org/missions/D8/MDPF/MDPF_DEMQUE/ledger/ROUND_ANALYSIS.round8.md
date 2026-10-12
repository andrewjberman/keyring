# MDPF_DEMQUE -- ROUND 8, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~15:3xZ)

**Input:** `3.0.0_SA_CVO` slug L10 slug, `surprise-channel/adjudications/ADJUDICATION_v8.md` @50398613b5. 5 of 5 orders complete, MAY-CLOSE;
every criterion re-run green on the CVO's session (C-S18). ARMED 0. `REMEDIATION_v7` holds two rows owned by this seat: D1-S9 and D1-W22-S1.
Calendar per `lib/trading_calendar.py`: T-1 frontier 2026-10-09 (Fri); 2026-10-12 (Mon) is trading.

## 1. Graded

- **FWD-3:** still APPLIED, not REALIZED. Its ACCEPT read is Monday 2026-10-12's morning production run, carried as round 7 stated. Round 8's
  t-27 drew 5,858 of 5,858 on its first fire.
- **C-PRICES (seven columns on every price table): NOT met, 127 of 141.** The 32 re-drew: 18 LOCKED and written, 14 REJECTED by the lock's
  90 pct trade-agreement floor (D1-S9). D1-S8 stays open on those 14.
- **FWD-1, FWD-2, FWD-4 to FWD-9:** not graded this round; the round-6 and round-7 reads stand.
- **Z-S2 and Z-S3** (re-quote of a partly drawn request; a weekday-priced quote that can never be met): routed by the CVO to `2.0.0_SA_COO~Q1`,
  whose cells they are. **The ruling rule is round 7's R2:** grade against ONE quote, frozen under the rule in force. A request whose every
  security reached its end date is CLOSED, with no 0-cell DRAWN lines after completion.

## 2. Rulings

### R1, D1-W22-S1 -- the price store MUST reach the T-1 frontier, daily. Its window is not fixed by design.

The CVO's read (C-S19): 141 files, every one ending 2026-06-22 or 2026-06-23, which is 76 trading days behind 2026-10-09. The cause is in the
build: `lock.py:23` pins `TX_PARTITION = "date=2026-06-23"`, so every request window is built from a June snapshot of the client's
transactions, and nothing extends the store after it.
- **Why the frontier binds:**
  - CLAUDE.md: everything is T-1 unless declared, and this PRD declares no fixed window.
  - FWD-1's ACCEPT is a LIVING client's holdings valued on the client's pages, and a living client holds today.
  - FWD-8's "unchanged history is not pulled again the next day" presumes a daily incremental: append the new dates only.
- **The remedy has three parts:**
  - (a) A STANDING tier-1 production request extends every locked symbol's file to the T-1 frontier each trading morning, through the
    shared pacer (C-YAHOO), appending only new dates (FWD-8). It is scheduled (production pipelines are scheduled, CLAUDE.md section 5) and
    reaches the frontier by trading days (`lib/trading_calendar`).
  - (b) The lock reads the LATEST transactions partition, resolved through `opal_naming`, not a pinned date. New trades since June are
    checked.
  - (c) The one-time 76-trading-day gap is a tier-2 backfill through the queue, quoted, at the measured ceiling.
- **Close:**
  - a served read of 141 of 141 files at max(date) = the T-1 frontier, the denominator printed;
  - the schedule read as DESIRED and APPLIED;
  - its first scheduled fire's receipt.
  The freshness entry carries `freshness_basis: trading-day-frontier`.

### R2, D1-S9 -- the 14 rejected names. NOT a wider band. Measure the cause first; serve the existing files meanwhile, with an honest claim.

The 14 (LCEYX, FTHSX, HLMEX, IWS, IWP, IWN, IWO, VSEIX, PFORX, RPIFX, VSS, VWO, MISIX, PIMSX) each passed a lock on 2026-10-09 and fail now. Their
agreement runs 79 to 88 pct, with two near 40 pct. The cause is NOT measured: a floor that post-dates their first lock (`52b8a3cca2`,
2026-10-09T03:35Z), a column difference in the new draw, or the transaction set.
- **Refused: lowering the floor or widening the band to admit them.** That moves the instrument until the reading passes. C-IDENTITY locks a
  mapping only when prices agree.
- **Serving, unchanged, while the cause is measured.** The existing three-column files keep serving. They are as-traded prices that the
  pages already read, so this is not a new served state. Their lock records carry the claim `held`, not `measured`, with the reason
  "trade agreement N pct below the 90 pct floor; cause under measurement". C-IDENTITY's own rule for a lock that cannot be proved is
  applied.
- **The two names near 40 pct are a different class:** at 40 pct agreement the symbol is likely the WRONG security. Each is read for whether any
  client page values a holding with it.
  - If one does, that is a BLOCKING row to this seat BEFORE any page change: Cottonwood pages are client-facing, so a PROD change waits on
    Andrew's word.
  - Either way, both go on the unresolved list (FWD-5) with their reason and open dates.
- **The cause instrument,** per name:
  - agreement of the client's trade prices against (i) the old locked file's close and (ii) the new draw's `as_traded_close`;
  - the disagreeing dates listed against the name's ex-dividend and split dates and the trade type (`by`, `sl`, `dvr`);
  - whether its first lock pre-dates `52b8a3cca2`.
  The reading decides between three remedies: a draw-column defect (fix the draw), a lock that never met the floor (the claim stays `held`
  until the data supports it), or a wrong symbol (re-resolve).

## 3. ENRICHMENT LIST (round 9, ONE issuance by `2.0.0_SA_COO~Q1`)

1. **R1 (a) and (b):** the standing daily extension to T-1 and the lock's latest-partition read. Close as R1 states; the schedule is under
   its own never-widen pair (a new served write cadence).
2. **R1 (c):** the 76-trading-day backfill, quoted and drawn through the queue. Close: 141 of 141 at the frontier.
3. **R2's cause instrument over the 14,** read-only, and the `held` claim with its reason on their lock records. Close:
   - the per-name table, with the cause classed;
   - the two near-40 pct names read for client-page use, and listed as unresolved.
4. **Z-S2 and Z-S3** (`~Q1`'s own cells) under round 7's R2.
5. **Carried, a read only:** FWD-3's Monday 2026-10-12 morning production read.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None now. If R2's read finds a near-40 pct name valued on a client page, its correction is a client-facing change that waits on his word.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~15:4xZ) -- row D1-S11: the transactions store is a June snapshot. A `held` tail is ACCEPTED; t-31's extension applies under its pair.

`2.0.0_SA_COO~Q1` msg 3954, round 9 issued @477921e3dc. `commonwealth/cottonwood/silver/transactions/` holds ONE partition, `date=2026-06-23`,
with max `Trade_Date` 2026-06-22. So R1 (b) has no later trades to check. That premise was this seat's, and it failed on measurement.

**Ruling:**
- **A `held` tail on all 141 files is acceptable, and correct.** Each symbol's identity was PROVED on the client's trades through 2026-06-22. The
  prices after that are the same proven symbol's prices, unproved only because no later trade exists in the store. C-IDENTITY's own rule
  applies: a lock with no trade prices to check carries `held`, not `measured`. The lock record states `trades_through` and the claim per
  window. Serving June prices for a living client's October holdings is the worse state.
- **The t-31 extension (SERVED) applies when it merges, under its never-widen pair** (R1, section 3 item 1). This word releases the hold on
  `~Q1`'s side; it is not the pair. Send the COO half and this seat signs the CTO half.
- **t-30's dynamic resolve stays:** the day a later partition lands, the next lock run reads it, and the tail moves from `held` to `measured`
  wherever trades agree.
- **Why the transactions store is a June snapshot is NOT this project's to answer.** Cottonwood's custodian feed and its silver transactions
  belong to another fabric (the store sits beside ADVI_COTBKF's inputs; dell2). It is routed MSTR to MSTR as a cross-fabric question: is the
  store meant to refresh, who owns it, and when. It is not a condition of round 9.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~15:5xZ) -- the owner answered: that transactions store is a ONE-TIME backfill. The `held` tail stands by design.

`1.0.0_SA_CTO~DELL2`, dell2 msg 5256, relayed by `0.0.0_AB_MSTR~DELL2` (bus 053013ba), verbatim in part: "that partition is NOT meant to
refresh ... ADVI_COTBKF is a ONE-TIME backfill by its PRD (contract C-ONE-TIME): Commonwealth's delivery of Cottonwood's history, ending
2026-06-22 ... If MDPF_DEMQUE needs Cottonwood transactions after 2026-06-22, that is a different source, Cottonwood's ongoing custodian feed,
and not this prefix." The owner's stated limits: the prefix was not listed today, and "no schedule" is read from the PRD's contract, not from a
Terraform sweep.

**Consequences:**
- **t-30's dynamic resolve is harmless but will not, by itself, ever upgrade the tail.** No later partition is planned in that prefix.
- **The `held` tail after 2026-06-22 is the steady state** until a second trades source is wired. It is not a gap to chase in round 9.
- **For round 10's list:** locate Cottonwood's ONGOING custodian transaction feed on this estate (`comp-which` first, then the served graph,
  with the denominator printed).
  - If it exists, the lock reads it as a second trades source, and the tail moves to `measured` wherever trades agree.
  - If it does not, the tail stays `held` by design, and that is stated on the lock records.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (2026-10-11 ~16:0xZ) -- row D1-S12 (BLOCKING): TRACE the valuation path now, read-only; re-resolve the three by CUSIP; no page change without Andrew

`2.0.0_SA_COO~Q1` msg 3975, table `deliverables/2.0.0_SA_COO~Q1/ROUND9_LOCK_CAUSE_14.md`.
- Old and new agreement are EQUAL on all 14, so there is no draw defect.
- 11 never met the floor, and their `held` claim stands.
- THREE are classed wrong-symbol: RPIFX 39.2 pct, FTHSX 40.7 pct and PFORX 42.9 pct.
- `silver/positions` `date=2026-06-23`: FTHSX is held by 4 accounts, PFORX by 11, RPIFX by 0.
- The 14 lock records now read `held`.

**Ruling:**
1. **Trace the valuation path NOW, read-only, as a round-9 cell.** For FTHSX and PFORX, which served artifact values those 15 accounts'
   positions, from which price file, and onto which client page (route and firm), the denominator printed. A trace changes no byte, so it
   needs no word. Not tracing would leave a possibly wrong client figure unmeasured.
2. **Re-resolve the three by CUSIP through the EXISTING resolvers** (C-IDENTITY: no second resolver). A mutual fund whose prices agree about 40
   pct of the time within the 0.5 pct band is typical of a WRONG SHARE CLASS of the right fund, not a different company. The read prints:
   - per CUSIP, the share class and ticker the resolver returns;
   - the agreement of that candidate's as-traded close against the client's trades.
   A candidate at or above the 90 pct floor is the proposed correction.
3. **No page or served price changes yet.** If the trace shows a client page values a position from a wrong-symbol file, the exposure is
   EXISTING (served before this round). The correction (new lock, re-drawn file, re-valued page) is a client-facing change, so it is written
   up with the before and after values per account and waits on Andrew's word (CLAUDE.md Agent Autonomy: a client-facing PROD change). If
   the trace shows no page reads them, the correction proceeds under its own never-widen pair.
4. **RPIFX** (held by 0 accounts) is re-resolved and corrected under its pair, with no wait.

D1-S12 stays BLOCKING until the trace prints. It then disarms to either "waiting on Andrew, cited" or "no client page reads it".

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 4 (2026-10-11 ~16:5xZ) -- D1-S12's trace: no client page reads the file. DISARMED. But the trace shows FWD-1's last hop is not connected.

`2.0.0_SA_COO~Q1` msg 4018. t-35 merged @9ae2f2d054, `deliverables/0.9.0_WK_MDPF_DEMQUE~27/VALUATION_TRACE.md`.
- The production bucket of the Cottonwood page is `opal-data-cot` (SSM `opal-cot-gold-run` sets `BD_S3_BUCKET`). Its Yahoo-tier inputs
  (`historical_prices.parquet`, `ticker_lookup.json`) are 404.
- So the page values FTHSX (188 current accounts, ~57.6) and PFORX (334, ~9.45) as B_00's Black Diamond market value divided by units. It does
  NOT read this project's price file.
- Re-resolve by CUSIP: FTHSX none; RPIFX none; PFORX's candidates PFBPX 42.9 pct and PFONX 42.5 pct. None reaches 90, so there is no correction,
  and all three are on the unresolved list.

**Ruling:**
1. **D1-S12 DISARMS** with the reason "no client page reads the file; the page values from the custodian's market value". No client-facing
   change is owed, and nothing goes to Andrew.
2. **The trace's larger finding is FWD-1's, and it is round 10's first cell.** FWD-1's ACCEPT is "has its daily prices value that client's holdings on
   the client's pages". The Cottonwood page's Yahoo-tier inputs are ABSENT from its production bucket, so this project's prices reach NO
   client page today, for any security.
   - The cell traces the land step (`land_cot.py`, which t-29 exercised: "COLLECT-OK n=111 land=7") to the page's bucket.
   - It names where its output lands, and why `opal-data-cot` holds neither input.
   - It makes the one real security of FWD-1 value on the page, end to end.
   - It is a client-facing change at its last step, so the before and after per account go to Andrew before PROD.
3. **The three funds stay unresolved, with the agreement printed.** That PFORX's two other share classes also sit at about 42 pct suggests the
   trade prices for these funds are not comparable to a daily close: dividend reinvestments booked at a different NAV, or loads. That is a
   reading for the lock's owner to measure, not a symbol to change. It is carried as a row, not a cell.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 5 (2026-10-11 ~17:5xZ) -- t-31 ran as signed. The 11 never-met-floor names should not stay frozen in June; carried to round 10.

`2.0.0_SA_COO~Q1` msg 4046, receipt `deliverables/2.0.0_SA_COO~Q1/ROUND9_EXTENSION_RECEIPT.md`, read by this seat:
- 127 of 141 at 2026-10-09, seven-column, claim `held` with `trades_through`;
- 0 cells of the old range differ, 0 files lost rows, 0 splits added (the split condition held nothing back);
- the 14 D1-S9 names untouched, ending 2026-06-23.

**For round 10's list:**
- **The 11 names that NEVER met the floor** (79-88 pct agreement; the symbol is likely right, the proof weak) are left 76 trading days behind
  only because each run's lock rejects them again. A `held` identity with current prices is the same state ADDENDUM 1 accepted for the
  127's tail. So they extend with claim `held` and the stated agreement.
  - The draw admits a name whose lock record is an explicit `held` hold record, without re-proving it.
  - Close: 138 of 141 at the frontier.
- **The 3 wrong-symbol names** (RPIFX, FTHSX, PFORX) stay frozen and unresolved. No page reads them (ADDENDUM 4).

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 6 (2026-10-12 ~03:1xZ) -- dell2's two requests are quoted. The daily extension for 1,034 symbols: BATCH the incremental pull; do NOT raise the cap

`2.0.0_SA_COO~Q1` msg 4239. Both requests are filed and quoted (@40b40dea3c, @12f3262550), in the live queue for Monday's 22:30 run:
- ADVI_COTBKF: 15 funds, 23,340 cells, finish 2026-10-12, accepted by dell2;
- IRPT_BCKEND: 878 securities, 113,262 cells, finish 2026-10-14.
The standing daily extension re-pulls each symbol: 141 + 782 new + 15, about 938 requests a day against the shared pacer cap of 400. A T-1 frontier for all is
not reachable one request per symbol.

**Ruling: (b) BATCH, then (c) TIER only if batching fails. Raising the cap is refused.** The cap is a measured, gentle pace (C-YAHOO; round-6 R1: the ceiling is
only ever a measured figure), and raising it to fit demand would be the instrument moving to meet the reading.
- **(b) The daily extension is INCREMENTAL and BATCHED.** It asks only for the dates after each symbol's stored max, for many symbols in ONE vendor request (the
  vendor library's multi-ticker download, as-traded with corporate actions, the same unadjusted read as today's per-symbol path). The pacer counts vendor REQUESTS,
  so 1,034 symbols at, say, 100 per request is about 11 requests a day.
  - **Proof before use** (it changes how served prices are pulled, so it runs under its own never-widen pair):
    - (1) on a sample of at least 50 symbols across share classes, funds and foreign listings, the batched rows equal the per-symbol rows, cell for cell
      (as-traded close, dividends, splits);
    - (2) a symbol the vendor refuses inside a batch is recorded as a FAILURE for that symbol alone, never as a price, and the rest of the batch stands (C-YAHOO);
    - (3) a split or dividend inside the new dates lands exactly as the per-symbol path lands it.
  - **Close:** a day's run lands all enrolled symbols at T-1 within the cap, with the request count printed.
- **(c) Only if (1) to (3) cannot hold:** a tiered daily set, where held and served symbols are daily and the rest weekly, with the stated lag on each.
- **The IRPT_BCKEND enrolment waits on that cell; no partial enrolment.** Its 125-day history lands on the quoted 2026-10-14 regardless.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 7 (2026-10-12 ~03:3xZ) -- batching does not reduce vendor requests. Branch (c) is RULED: daily for the served and held set, a stated rolling cycle for the rest

`2.0.0_SA_COO~Q1` msg 4251, t-40 merged @34040149bb, `deliverables/0.9.0_WK_MDPF_DEMQUE~32/EQUALITY_REPORT.json`.
- Equality HOLDS: 50 of 50 symbols, 4 classes, 0 mismatches over 154,984 price, 1,252 dividend and 20 split cells. A planted bad ticker failed alone.
- But the library's multi-ticker download makes one HTTP request PER SYMBOL: 51 per-symbol against 58 batched, for the same 50.
- **Counting a batch as one pacer request would be the instrument moving to meet the reading, and it is refused, exactly as the issuer says.** That is the right
  call.

**Ruling: (c).**
- **DAILY (T-1):** the 141 names the price store serves today and ADVI_COTBKF's 15 funds. That is 156 requests a day.
- **ROLLING:** IRPT_BCKEND's 782 new names on a cycle of at most 5 trading days. That is 313 to 352 requests a day in total, with 48 to 87 spare under the cap of 400.
  - Every value served from a rolling name carries its own `as_of` (its stored max date), so a consumer reads the lag, never infers freshness.
  - The cycle order follows FWD-9's ranking.
  - The freshness entry states the cycle (`freshness_basis: trading-day-frontier`, with the rolling lag declared per tier).
- **IRPT_BCKEND is told the lag in words:** its 878 names land T-1 within 5 trading days, not daily. If IRPT needs strict daily, that is a CAPACITY question:
  - a higher Yahoo cap, raised only on a measured vendor limit;
  - or the Bloomberg route under C-BUDGET.
  It comes to this seat; it is not absorbed silently.
- **Close:** a week of runs, every name within its tier's lag, request count under 400 each day, the per-name `as_of` printed.

-- 1.0.0_SA_CTO~DELL1
