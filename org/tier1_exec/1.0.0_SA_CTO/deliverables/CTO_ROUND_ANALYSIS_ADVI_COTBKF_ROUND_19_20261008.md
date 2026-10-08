# ADVI_COTBKF -- ROUND ANALYSIS, round 19

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~17:5xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1354), the L9 grade @42ebe97a39 (CB19s1-AC3 MET), and REMEDIATION_v12.
- 1 of 1 order complete and VALID (CB-s-1 @bf424e274b).
- D2-W39-S1 is REMEDIATED: 42 of the 74 double-counted months now MATCH.
- D2-S29 and D2-S30 are OPEN to this seat. ARMED 0.

## 1. Ruling -- a custodian's core money-market position is a sweep vehicle (D2-S30)

Round 18 ruled that "a bank sweep is the account's cash parked in an interest-bearing vehicle", so moving money between cash and the
vehicle is not an investment flow. That reason does not depend on the vehicle being a bank deposit. A custodian's CORE position is the
account's cash: the custodian moves uninvested cash into it and out of it to settle trades, without an investment decision. So:

**Ruling.** A security goes on the declared sweep list when it is EITHER:
- (a) a bank deposit sweep by its stated source (round 18); OR
- (b) the custodian's designated core cash position for the account.

The list entry for (b) names two things:
- the custodian's designation (the custodian's own documentation or account data naming it the core position); and
- a list-level behavior census, using the CVO's measure: accounts holding it, the share of its rows paired same-day with another CUSIP,
  and its dividend cadence.

Membership is still decided per CUSIP on the list, never per row. A security not on the list is never cash.

**316067107 (Fidelity Government Cash Reserves) goes on the list, sweeps-v2, under (b).** The CVO's census shows the core signature:
- 232 accounts and 8,768 rows since 2023-03-17;
- monthly `dv`/`dvr` (dividend) rows;
- 91% of its rows paired same-day with another CUSIP, against 75% and 78% for the two listed bank sweeps.

E2 records the custodian's designation as the source line. If no designation can be cited, the entry does not land and the cell says so.

**The other 22 money-market funds stay off.** They are elected fund holdings unless the same census and a designation show otherwise.
E2 lists any that do, and adds none.

## 2. D2-S29 -- the 163 months that moved MATCH -> DIFF

The control holds: 642 of 642 non-sweep months are unchanged. So the 163 movers are all in sweep accounts. The CVO's lead is that an
account holding an unlisted core position now has its bank-sweep side made INTERNAL while the core side is still a trade. The ruling
above may close most of them. E1 classes them first, so that E2's re-grade can be read against that classing.

## 3. ENRICHMENT -- round 20, ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Class the 163 MATCH -> DIFF months (D2-S29)** | (1) each of the 163 months is classed by its account: holds 316067107 / holds another unlisted money-market fund / neither, with counts per class summing to 163; (2) the month grades are persisted this time, as a file beside the report, so the next re-grade compares months rather than day values | LOCAL |
| E2 | **sweeps-v2: 316067107 under rule (b), then re-grade** | (1) the list prints 316067107 with its custodian-designation source line and the behavior census; (2) the whole chain re-graded, with MATCH/DIFF before and after, plus E1's 163 months shown with their result; (3) the control (months of accounts with no listed sweep or core position) grades the same before and after | LOCAL |

E2 also prints the same core census for the other 22 money-market funds, as a list only.

The real run of cells B-D stays bound by the price load (unchanged).

## 4. Packet correction

The drain-end packet's class counts (CD 279, cash-merger 61, bank issuer 33, money-market 22) are prose errors, and the cited report
(385 / 52 / 32 / 23, summing to 517) is the record. No artifact moves.

-- 1.0.0_SA_CTO~DELL2
