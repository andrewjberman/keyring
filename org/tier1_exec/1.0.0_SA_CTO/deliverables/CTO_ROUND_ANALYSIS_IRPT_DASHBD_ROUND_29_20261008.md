# IRPT_DASHBD -- ROUND ANALYSIS, round 29

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~21:0xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1627), ADJUDICATION_v15 @fc95763a6f, and `~D2`'s record @047176ff76. MAY-CLOSE, ARMED 0. S34 is
closed.

## 1. State

- **E1:** 437 of the 440 non-recomposing accounts are an artifact of round 18's fee ADD-BACK. Adding fees back is not additive across
  date ranges, while BD's net returns do chain. The other 3 are net misses on near-zero opening values. **The BD self-inconsistency is
  ours, not BD's.**
- **E2:** on the 1,528 real right-half misses, the gap is a median +0.567 pp, with Opal ABOVE BD on 94.7%. No Opal component explains it
  (largest |r| 0.144). `fee_amount` is 0 on every day.
- **E3:** the default batch is 2000, the default run took 667 s, and one run read 757 s (W31-S2). The margin is thin but under 900 s.

## 2. Ruling -- the CVO's decision: test the advisory-fee lead first

Opal sits above BD on 94.7% of misses, and Opal records no fee on any day. That is the signature of an advisory fee BD deducts and
Opal's return does not. It is probably debited at the custodian and classed as an external flow, so it never touches return.

The test therefore leaves the add-back behind and compares like with like on the NET basis, where BD's figures chain.

## 3. ENRICHMENT -- round 30, ONE issuance by `2.0.0_SA_COO~D2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Is the gap the advisory fee?** Per account over the right half, compare Opal's gap with BD's own gross-minus-net for the same range, from the existing pulls with no new vendor call | (1) the distribution of (gap minus BD fee drag), with the share within the 0.35 pp tolerance printed; (2) the result stated before a fix is cut: confirmed if the share is >= 80%, otherwise the lead is refuted and the share is named | LOCAL |
| E2 | **Opal's fee leg, measured** | (1) a census of Schwab's advisory-fee transaction rows for the 1,528 accounts (type codes, count, $), and how `account_return_daily` classes them today (flow or performance), from source lines; (2) one account traced end to end: fee debits, then Opal's flow, then the return effect | LOCAL |
| E3 | **W31-S2: runtime margin** | (1) the lots stage's p95 over 5 full runs at batch 2000 is under 750 s, or the batch is lowered until it is | LOCAL |

E1 and E2 together decide round 31. If confirmed, Opal publishes a net return as well, treating the fee as performance, and FWD-8 is
graded on net against BD net. If refuted, the gap gets its next stated reason. Either way, every day of disagreement must carry a reason
(FWD-8's ACCEPT).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-08 ~21:0xZ, on `~D2` msg 1639): E1 as written was an identity; the COO's recast is adopted

The recorded gap is already Opal minus (BD net + BD's add-back drag). So "gap minus BD drag" returns the gap itself: the maximum
difference is 1.8e-12 over 1,527 accounts, and 0 fall within tolerance before any work. The test could not discriminate. This seat's
error.

**E1 now reads:** the net-basis gap (Opal minus BD net) against an **OPAL-SIDE fee drag**, compounded daily from E2's Schwab fee rows
and Opal's own market value. It is confirmed when at least 80% of accounts fall within 0.35 pp; otherwise it is refuted, with the share
named. E2 is E1's input (one chain). E3 is unchanged.

The lead is still alive: BD's add-back drag has a median of 2.39 pp, and Opal is a median 2.92 pp above BD net.

-- 1.0.0_SA_CTO~DELL2

