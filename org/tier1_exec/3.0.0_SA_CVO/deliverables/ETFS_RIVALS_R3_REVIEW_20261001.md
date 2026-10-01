# ETFS_RIVALS round 3 -- CVO review and L10 slug basis

**Seat:** 3.0.0_SA_CVO~RV (Andrew's pairing with 2.0.0_SA_COO~RV). 2026-10-01 ~12:1xZ.
**Packet:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/DRAIN_END_READ_ROUND3.md` @058d094e4a (msg
27797, acked). 6 of 6 orders terminal; ledger `etfs-rivalfunds-round3` CLOSED.
**Carriers:** `ADJUDICATION_v3.Z.md` (4 rows, 21 items); `REMEDIATION_v3.Z.md` (7 items, W1-S27 ARMED); clock advances in
place on v1 (S1, W1-S5) and v2 (W2-S4 DISARMED, W1-S8, W5-S28), all REMEDIATED.
**Open after this commit: 18** remediation items (round 1: 6, round 2: 5, round 3: 7), every one owned by
1.0.0_SA_CTO~Z.

## Correction of this seat's round-2 work

Round 2's slug graduated **W2-S4 as ARMED** on my census "issuer silver 325/325 old-format ids". **That was a
wrong-object measurement.** The fix (1faa6d4f8d, 2026-09-30 19:12Z) was already in the tree my slug committed on.
`_capture_id` strips the requested date, so the ordering no longer depends on the key format. I counted the formats and
never read the comparator. The packet's claim was wrong the same way, and my number corroborated it instead of testing
it. The CTO retracted ruling 1's premise at the cut (row Z-S4), and round 3 spent its first cell on the real residual
(issuer-side retain). The cost was one re-cut cell. The clock is now advanced: DISARMED at 2026-10-01T04:10Z (the d-3
apply that made the fix live). **Rule I'm applying from here:** a "hazard still live" verdict about code is graded by
reading the code path at HEAD, never by a census of the data the code reads.

## Measured by this seat (not taken from the packet)

| claim | read | result |
|---|---|---|
| the page | get `platinum/page/date=2026-10-01/manifest.json` | status published, generated 11:16:08Z, 12 of 13 updated, not-updated only `PFOE/GQGU` |
| S8 disarmed | `d4_live.json` gates.1 | BASG 0/0 (was 1489 added / 322 removed); 12 of 12 inside the COO half's table |
| issuer retain (S4) | silver_issuer.py at HEAD | :240-247 retain and mark; no delete call |
| package | pytest | 249 passed, 2 skipped, 0 failed |
| gateway route | SSM `f546a351-221a-4968-bd19-cebb8842c5e1`, read-only | /rivalfunds 401, /health 200, after NFRA_OPLGTW's 10:43Z redeploy (daa56d81ac); the route has now survived two other-seat deploys |

## Recommendations by driver

**For CTO (1.0.0_SA_CTO~Z), the round-3 analysis**
- **P0 -- W1-S27, ARMED.** The served daily G5 pairs a date only with the previous GLOBAL date, so a fund that skips it
  (TSEL, WCMG: Bloomberg-lagging) loses that window's trades every day it happens. The page still reads those funds
  "updated". It is the one live served-correctness defect left. Fix: pair each fund with its own prior date, as the
  replay does.
- **P1 -- W4-S5 with v2 W1-S11: one revision contract.** Three tables (G1, G4, trade_schedule) now order "newest" by hash.
  On 2026-09-29 the served G1 joins a 172-row, price-less QA import over the 434-row live pull. Decide one contract for all
  three, not three patches.
- **P1 -- W4-S2: identity floor.** The floor is honestly PROVISIONAL 0.0, and your refusal of key 4 was right. BASG's
  newest date resolves 0/33 because the daily Bloomberg request excludes it. Choose a route for issuer-only days or
  per-source floors.
- **P1 -- S6: GQGU.** The issuer route is measured (305 archived days, BASG's parser). It is the last not-updated fund
  and needs no vendor word.
- **P2 -- W4-S1** (ratify or narrow the ListBucket the act added beyond key 2's text), **W3-S15** (G4 prices as of the
  pull moment), **S7** (fix the seating lint before it enforces), and W2-S7's dead `guardrails.report_date_freshness`
  path. v1 W1-S5's marker shipped, but the PRD still carries no contract line for it; carry it into the next PRD bump.

**For COO (2.0.0_SA_COO~RV)**
- **P1 -- W1-S27's disarm is yours** until the cell ships. No act of yours makes it worse, but read the page's "updated"
  as freshness only, not completeness of trades.

## Deferrals and close-reads still owed

- FWD-1 is not graded here. It still needs the signed-in /rivalfunds read (Andrew) and the next trading day's 08:03 leg
  and 09:00 sweep read from the schedules alone (packet :91-93). The Terminal read healthy at 11:07Z today.
- Round 4's carried items (analysis ruling 7: W1-S11, W3-S11, W3-S12, W5-S21) and fabric S2 are untouched this round.

## What you should have asked but did not

What "updated" means on the page. The manifest says 12 of 13 updated, and the checks behind that word are freshness,
completeness of holdings, identity coverage and render. None of them checks that a fund's trade windows were formed.
W1-S27 shows a fund can be "updated" with its newest trades missing, and W4-S5 shows a date can be "updated" from the
lesser of two G4 objects. The page's headline number now overstates what it serves, and every check is green. A
`trade_windows_formed` check per fund (G5 windows against the fund's own consecutive G1 dates) would make the
headline honest. Proposal only; it is a guardrail cell for you to place or decline.

-- 3.0.0_SA_CVO
