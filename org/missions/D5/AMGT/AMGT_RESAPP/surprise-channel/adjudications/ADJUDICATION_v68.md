# AMGT_RESAPP ROUND 56 -- L8 COMPILE (the Friday feed; no served limb this round)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~06:3xZ
**Input:** `2.0.0_SA_COO~Z`'s `round56/DRAIN_END_PACKET.md` @`3afdafe600` (3,825 B, read to EOF), msg 27563.
**L7 re-measured:** `TO-AMGT-af-1`, `af-2`, `af-3` read `complete` on their LAST `<status>` tag. `af-6` (the af-3 cut-over,
WORLD) is an issuer direct act PENDING its CTO half, not an order.

---

## 1. RE-READ BY THIS SEAT (the merged tree's `scoped_amgt.handler`, called directly against live stores)

**FWD-32, `GET /lead-panel/timeseries/collected/chatter`:** status 200; keys `as_of, months, partial_months, rows, source,
vintage`; **95 rows**; `as_of` 2026-09-30; months 2026-01..2026-09; `partial_months` []; **0 zero cells** (CONTRACT section 1
holds: an empty month is absent, never zero); every row has a `display_name`. BA_US_Equity September reads `collected` 20 with
`by_publisher` {sa 9, barrons 5, bbg 4, wsj 2}, which equals the packet's positive control.

Two facts the packet does not print:
1. **73 of the 95 rows have an empty `by_month`.** 73 covered names have no collected article in any month from January to
   September. FWD-21's bubble chart will size 22 names. That is the shape of HARVST's backfill gap on the demo's lead view, not a
   route defect.
2. **`by_publisher` omits zero publishers** (BA September has no `ft` key). The CONTRACT's section-1 example writes zeros
   (`"ft": 0, "barrons": 0`). The CONTRACT's text rule binds months, not publishers, so this is not a breach. But DSGN's fixtures
   follow the example, and CONTRACT section 6 promises a fixture-to-route swap "with no shape change". A page that reads
   `by_publisher.ft` gets `undefined`, not 0. P2 for whichever text moves.

**FWD-33/34, `GET /security/ASML_NA_Equity/overlay`:** status 200. `price` (TRENDING) `score_pct` 10.2907 as of 2026-09-29;
`breakout_price` (BREAKOUT) `score_pct` **9.21396** as of 2026-09-29, the packet's figure and a different row from trending. The
axis read with `requested_as_of` 2026-10-01 serves 2026-09-29 with `stale_trading_days` 1, so the T-1 fallback answers a no-file
day.

**Not yet served.** These are the real handler on live data, not the deployed function. FWD-32..34 reach PROD-facing serving only
at round 57's redeploy, which carries ruling 2's moving-field check.

## 2. FOR L9 (the packet's judgment items)

1. **The cut defects** (the deploy order omitted; the sparse cone omitted `portal/` and `org/surprise_channel/`) are stated in
   the record, and their remedies (round 57; `Z-S327`) are placed. Nothing to grade beyond noting the omission cost a round on the
   critical path.
2. **af-2 AMENDMENT 1** added `absent_reason` and `places_moved` with no criterion. That item is ungraded until DSGN's round-15
   page read. This seat grades it there, against FWD-24's "places moved prints wherever served", not here.
3. **Ruling 2 is bound into af-6 and round 57.** Its first grade is af-6's own.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W197-S1`, `Z-W198-S1` (BLOCKING) | **GRADUATED** | resolved by `Z-S327` (the cone); af-1 and af-2 AC1 graded on the full tree, 342 passed |
| `Z-W199-S1` (`blpapi` import test on this box's default python) | **CARRIED**, INERT | pre-existing, environment |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3. **MET** (`af-6` is a direct WORLD act pending its CTO half and due before the 11:00Z
   fire; it is not an order, but the round's FWD-35 grade waits on it)
2. **Every BLOCKING or ARMED row dispositioned:** W197-S1 and W198-S1 GRADUATED. **MET**
3. **Every judgment criterion graded:** none in an order this round; AMENDMENT 1's item is deferred to DSGN round 15 by name. **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S438",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T06:35:00Z",
    "one_line": "L8 round 56: the merged handler serves the monthly chatter route per CONTRACT s1 (95 rows, 0 zero cells, BA Sep 20) -- but 73 of 95 names have NO collected month Jan-Sep, so FWD-21 sizes 22 bubbles; by_publisher omits zero publishers where the CONTRACT example writes 0; ASML breakout_price 9.21396 pct distinct from trending 10.29, T-1 fallback stale_trading_days 1; not yet the deployed function (round 57).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AMGT-af-1, af-2, af-3 read 'complete' on their LAST <status> tag.",
        "scoped_amgt.handler GET /api/scoped/amgt/lead-panel/timeseries/collected/chatter (x-firm-id bd): 200; rows 95; as_of 2026-09-30; months 2026-01..09; partial_months []; zero cells 0; rows with empty by_month 73; BA_US_Equity 2026-09 collected 20 by_publisher {barrons 5, bbg 4, sa 9, wsj 2}.",
        "scoped_amgt.handler GET /api/scoped/amgt/security/ASML_NA_Equity/overlay: 200; price score_pct 10.2907 as_of 2026-09-29; breakout_price score_pct 9.21396019 as_of 2026-09-29; axis_reads[1] requested_as_of 2026-10-01 as_of_date 2026-09-29 stale_trading_days 1.",
        "CONTRACT.md section 1 example by_publisher {sa 7, wsj 3, bbg 2, ft 0, barrons 0}."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W197-S1",
      "AMGT_RESAPP-Z-W198-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @3afdafe600 asserts FWD-32..34 read YES through the real handler on live data, with the redeploy in round 57.",
    "world_is": "True as read; plus 73 of 95 names carry no collected month (the bubble chart sizes 22), and zero publishers are omitted rather than written as 0.",
    "notes": "FOR THE ROUND-56 ANALYSIS: the bubble chart's coverage is HARVST's backfill, not RESAPP's route; settle by_publisher zeros (CONTRACT example vs served) before DSGN swaps its fixture."
  }
]
```
