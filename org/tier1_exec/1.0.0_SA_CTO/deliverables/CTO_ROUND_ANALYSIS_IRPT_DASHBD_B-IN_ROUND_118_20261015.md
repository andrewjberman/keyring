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
