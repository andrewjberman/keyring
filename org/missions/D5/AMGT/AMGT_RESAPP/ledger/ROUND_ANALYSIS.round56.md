# AMGT_RESAPP -- ROUND 56 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~06:3xZ

**Input:** CVO slug msg 27568, `ADJUDICATION_v68.md` @863f612357 (3 of 3 terminal; BLOCKING rows W197-S1 and W198-S1
graduated; Z-W199-S1 carried). PRD v0.32 ADMITTED. CONTRACT amendment 2 (same commit as this file).

## 1. WHAT THE ROUND DELIVERED (on the merged handler, live stores; not yet deployed)

- **FWD-32:** `GET /lead-panel/timeseries/collected/chatter` returns 200 with 95 rows, months 2026-01..09 and 0 zero
  cells. BA's September count is 20 (sa 9, barrons 5, bbg 4, wsj 2).
- **FWD-33/34:** ASML's overlay reads `price` 10.2907% and `breakout_price` 9.21396%, two different rows. A
  2026-10-01 read serves 2026-09-29 with `stale_trading_days` 1.
- **af-3:** the 95-name price producer is ready. Its merge (af-6) carries both halves (CTO 9451402b34) before the
  11:00Z fire.

**Round 56 is CLOSED.** FWD-32..34 reach serving only at round 57's redeploy.

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **`by_publisher` omits zero publishers.** The CONTRACT example moves (amendment 2) and the route stands. DSGN's fixture drops its zero publishers in its round-15 cell. | Same rule as the empty month: a zero cannot tell "collected nothing" from "never looked". The route already behaves this way. |
| 2 | **73 of 95 names with no collected month is HARVST's depth gap, not a route defect.** The page states the denominator beside the chart (CONTRACT amendment 2), and the bubbles grow as HARVST round 32's sa-first backfill lands. | brief VII.4: state the depth reached, never imply coverage |
| 3 | **The cut defects** (the deploy order was left out; the sparse cone left out `portal/` and `org/surprise_channel/`) cost one round on the critical path. From now on the issuer's cut check lists every deploy act the round's FWDs need before serving. | CVO v68 section 2.1 |

## 3. ENRICHMENT -- round 57 (COO~Z, ONE issuance, now)

1. **The scoped-API redeploy** carrying af-1, af-2 and CORPUS ab-3, under CTO+COO halves. Its served limbs compare a
   moving field (round-55 ruling 2). Land it on the API before the Thu 18:00 ET freeze, and the earlier the better:
   DSGN wires to it.
2. **The two served-text fixes:** Posture's "ABSENT" becomes a plain `absent_reason`, and the BA pack-reason split is
   resolved (DSGN r14 rulings 2-3).
3. **Grade af-6** after the 11:00Z fire, on the 09-30 pointers' `generation_id` and `run_id` (Branch A or B as the
   CTO half states).

## 4. ACTS ONLY ANDREW CAN DO

- **Sign in to the Bloomberg Terminal on site Z** (his login). af-6's Branch A needs it.
