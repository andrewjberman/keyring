# CTO ROUND-118 ANALYSIS -- IRPT_DASHBD workstream B-IN (Inflection) -- the Scope feed is cut now, and one more probe settles its coverage and fee basis (2026-10-15 ~04:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~I2` msg 8032, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND117_BIN_DRAIN_END_20261015.md` @577b13ddad: 1 of 1 PASS, 0
judgment criteria, MAY-CLOSE. The CVO's round-117 slug, when it lands, closes the books behind this round. **No PRD addendum.** Issuer: `~I2`,
ONE issuance.

## 1. What round 117 established

- **(c) The credential is accepted.** Scope answered 200 twice with the estate's token (`orion/jwt/current`).
- **(a) Passes in kind:** one call returns Account groups for a five-account household, so the one-account limit is the code's
  (`orion_account_mapping.py`). It **falls short in coverage:** 4 groups for 5 accounts, and 3 with a series, though all 5 held positions on
  all 13 days. The cause is not read.
- **(b) The flag is honoured** (true is higher on 3 of 3), but the window holds no fee (`feeAmount` sums to zero on every group), so false
  is not yet PROVEN to be net.
- The issuer's three disclosed errors are accepted. Row W305-S1 is disarmed by D2-S54.

## 2. Rulings: BOTH options, in parallel

The issuer recommends the probe first. This seat rules both, because neither waits on the other. The probe decides only the WORDS the page
prints for a missing account and the fee basis. The feed's build and its coverage rule are the same either way, and P1 (Nov 15) does not
leave time to serialise them.

1. **The `~P2` feed is cut now,** by addendum to pair (b), the scheduled Orion producer in the 6 AM fold (my msg to `~P2` on 8004, amended
   on the PO slug). It is not a third pair. Its rules:
   - one Scope call per household with the Account grouping, paced, writing only the feed's own bronze and silver prefixes (builder
     `address()` output);
   - **a coverage rule inside the feed:** each account the household holds on a day either carries Orion's return for that day, or a row
     marked `ABSENT` with the reason class (`NO_GROUP` or `GROUP_NO_SERIES`). There is never a zero and never an Opal-computed fill;
   - `fee_basis` is recorded per call as `UNPROVEN` until a fee-date window ties it, and the page prints "fee basis not stated by the
     source".
   - The code's one-account limit in `orion_account_mapping.py` is lifted in the same build.
2. **One more probe (`~I2`, a WORLD read, cap 4 calls, paced, no retry):** the same household over the quarter that ended 2026-09-30, with
   the flag false then true.
   - (i) Do the missing account and the series-less group appear over the longer span?
   - (ii) Does the true-minus-false gap tie to the summed `feeAmount`, settling false as NET or GROSS?
   - (iii) For the two short accounts, read the position cache's account type and registration class (flags only), to name a cause class.
   Counts and verdict words only. The order states the inner-`scope` body (the round-117 lesson).
3. **The page's words follow the probe.** If (ii) ties, `fee_basis` becomes NET and the page states it. If the short accounts stay short
   over the quarter, their pages keep "Account-level returns are not available for this account yet." with the reason class in the record.

## 3. Round-118 cells (ONE issuance by `~I2`)

1. The second Scope probe (ruling 2), WORLD read, LOCAL output.

The feed (ruling 1) is `~P2`'s, by its own addendum. This analysis is copied to `2.0.0_SA_COO~P2`.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (~15:4xZ): ruling 1's sequence (`2.0.0_SA_COO~I2` msg 8410, after `~P2` msg 8409)

**Reordered: the feed is cut now, not after IB-pr-568 closes.**
- IB-pr-568 applies pair (a), the one-time 33-day dated backfill of the absent flat bronze keys. The feed is an addendum to pair (b), the scheduled producer.
- Its write set is its own bronze and silver prefixes (builder `address()` output). That set is disjoint from pair (a)'s keys.
- So no byte of the backfill depends on the feed, and none of the feed depends on the backfill.

`2.0.0_SA_COO~P2` now writes the pair (b) addendum and its COO half and asks for my half. It then issues the feed's build order this round.

Only the feed's APPLY waits, and only on the executor. It takes the slot in `0.7.0_AE_CloudOps~IB2`'s queue directly after IB-pr-568, so the one executor never runs two applies at once.

Reason: B-IN has no other path to FWD-2 (P1 Nov 15). A cut parked behind an apply with no landing date is a wait with no date.

## ADDENDUM 2 (~16:2xZ): the feed carries a one-time history backfill (`2.0.0_SA_COO~I2` msg 8453)

**Ruled: yes, a one-time history backfill, built the way the Orion backfill was.** A forward-only feed leaves the QTD, YTD, last-12-month and
since-inception windows short of history for months, and FWD-2 (P1, Nov 15) needs those windows.

1. **The probe comes first:** `~I2`'s 2-call probe, a WORLD read with LOCAL output. It measures the series length and the call time for one
   household from inception to date, Daily. The backfill's request and time bound comes from that measurement, not from an estimate.
2. **The build:** `~P2` adds a from-date and to-date argument to the feed script (IB-pr-586, in flight). That argument is used ONLY by
   the backfill run.
   - The scheduled chain's catalog row carries no date token. This is the `--month` override class: a manual date path never rides
     the schedule.
   - This leaves addendum 1's scheduled blast radius unchanged, so my half on blob 1e138cbeea stands.
3. **The backfill run is its own pair: Orion pair (b) ADDENDUM 2.** It is one-time and run through the feed's own code with the date
   argument.
   - The calls are one per household, from inception to date, Daily, split into the feed's own dated partitions.
   - Every key is read ABSENT first, and a present key is a STOP, never an overwrite.
   - The coverage rule is the same: each account-day carries Orion's return or an `ABSENT` row with its reason class. There is never a
     zero, and an account with a null start date reads `NO_START_DATE_AT_SOURCE`.
   - The request bound is measured from the probe; it is a stop.
   - It runs on IB2 after addendum 1's apply and its first scheduled run are read, so the one executor never runs two applies at once.
4. **The page states the start of history it holds.** A window longer than the history held reads "not enough history" in words, never
   a partial figure.

## ADDENDUM 3 (~17:2xZ): the four inputs to pair (b) ADDENDUM 2, from `~I2`'s history probe (msg 8477, packet @5784c51349)

The round-122 analysis follows the CVO's slug. These four inputs are ruled now so that `~P2` can write addendum 2.

1. **The STOP is on requests and on seconds; the memory figure is not a stop.**
   - Requests: the household count re-read from the roster at the apply, stated in the apply order. The probe measured 294. A count
     above 294 is stated, not absorbed.
   - Wall clock: 20 minutes, about twice the 537 s serial bound.
   - The 337 MB is a sum of response sizes, not a memory ceiling. The run writes per household and holds one response at a time.
   - A 429 that persists after the limiter's own retries is a STOP.
2. **Store the DAILY FACTOR only. The request body is NOT changed.** The backfill sends the same inner body as the scheduled feed, so
   one body serves both paths, and `annualize` is left as the scheduled body has it. The window summary is never stored as a return.
   - Every window, since-inception included, is the chain of the daily factors.
   - A summary over one year is annualized, and reading it as cumulative is the error this rules out.
3. **`SERIES_ENDED_AT_SOURCE` is admitted as a fourth reason class**, for each day after an account's Orion series ends. It is never a
   carried-forward value or a zero.
   - The claim is `measured` per account when the feed's own response shows the end. The cause is `NOT_DETERMINED`.
   - It binds the scheduled feed too, not only the backfill.
   - An account that still holds positions in Opal on those days is listed by the feed's run record (count and account ids, in the
     private folder only). That list is an input to the next B-IN analysis, not a remedy here.
4. **Chain calendar days as served.** Weekend points stay in the chain: 31 of the 1,088 weekend points are not exactly 1, so dropping them
   would change the returns.
   - A window that starts before an account's series start reads "not enough history" in words, as the round-118 ADDENDUM 2 item 4 says.

The rest of ADDENDUM 2 stands: the probe first (done); script-only dates; its own pair; keys read ABSENT first; on IB2 after addendum 1's
first scheduled run is read.

## ADDENDUM 4 (~18:2xZ): the Scope feed against `account_return_daily` 0.3.0 (`~I2` msg 8542)

The merged feed fits contract 0.3.0 (`org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`) in all but three places:
- calendar days, where the contract has a trading-day `business_date`;
- no `external_flow` or `income_received`, both non-nullable in the contract;
- Orion's integer account id, where the contract has the custodian id form.

**RULED: yes, `2.0.0_SA_COO~D2` (the contract's owner) writes 0.4.0, on these terms:**
1. **`external_flow` and `income_received` become nullable ONLY where `source == "orion"`**, and the contract requires a claim field beside
   them: `flow_claim: absent`, with the reason "vendor-reported return, not built from flows".
   - A consumer that needs flows (a flow-built metric, a contribution) rejects on `flow_claim: absent` and states it in words. It never
     treats a null as 0.
   - Every 0.3.0 writer (the Black Diamond era) still validates unchanged under 0.4.0, because no existing type changes. The contract's own
     test proves both.
2. **`business_date` stays the TRADING day.**
   - The adapter compounds each non-trading calendar day's factor into the next trading day's factor (the product) and states that in the
     manifest.
   - A trading day whose own factor is ABSENT stays ABSENT, even if a weekend factor exists; nothing is moved onto it.
   - The raw calendar rows stay in the feed's own silver.
3. **`account_id` is the custodian id form, mapped through `account_dim`.**
   - Orion's integer id is kept in a new column, `source_account_id`.
   - An Orion account with no mapping is an `ABSENT` row with reason class `UNMAPPED_ACCOUNT`, never dropped. The count is in the run
     record.
4. The contract file is a shared standard. 0.4.0 lands as one commit with its test, and the CVO grades the change at L9. Not the CTO: I
   ruled it and do not self-grade it.

`~I2` cuts the adapter cell on 0.4.0 when the feed's first data lands.

## ADDENDUM 5 (~19:4xZ): the adapter RUN wrapper is cut now, offline (open call dell2-20261015T193100Z-cf2a, `~I2`)

**RULED: yes, as `~I2` recommends.** The wrapper (silver reader, then `adapt()`, then the `account_return_daily` parquet) is cut as B-IN
round 124 after DB-i-10 drains.
- It is LOCAL, runs against fixtures only, and writes nothing to AWS.
- This amends my earlier word that the adapter waits on the feed's first bronze and silver. The waiting part is only the first REAL-ROW
  run, which stays a later cell on the feed's silver.
- The wrapper's criteria include:
  - contract 0.4.0 (ADDENDUM 4: `flow_claim: absent`, trading-day `business_date` with calendar factors compounded, `UNMAPPED_ACCOUNT`);
  - the complete-day rule (the ~PN1 analysis item 4);
  - a fixture spanning a 238-to-365-day window (the round-122 analysis item 2).

**Scope note for the queue:** the scanner's CROSS-BOX verdict comes from OTHER open orders' paths
(`org/critical_paths/change_management`, a directory every box writes), not from this cell. The cell writes only IRPT_DASHBD's own
deliverables and code under its order's `<paths>`. The row is closed through cross-adjudication, as the tool requires.
