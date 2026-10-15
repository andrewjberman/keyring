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
