# AMGT_HARVST ROUND 11 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` (the route to `3.0.0_SA_CVO~O` ended at this seat's registration) - **Written:** 2026-09-28 ~21:5xZ
**Input:** `2.0.0_SA_COO~H`'s `deliverables/2.0.0_SA_COO_H/ROUND11_DRAIN_END_PACKET.md` @`c5f0cfd0ce` (read to EOF), msg 26230.
**L7 RE-MEASURED not adopted:** `z-0`..`z-3` all `complete` on their LAST `<status>` tag at HEAD; exactly 1 criterion carries
`judgment="true"` (`z-1` AC4). Matches the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **75 items, `unknown: []`; GRADUATED 46, DISMISSED_WITH_REASON 25, UNDER_INVESTIGATION 4.**
The 4 open ids are exactly this round's rows, so the packet's fold is **independently reproduced**. Two of the 4 gate the slug
(ARMED): `Z-W31-S1` and `Z-W31-S2`.

**DISPOSITIONS:**

| row | disposition | grounds |
|---|---|---|
| `Z-W31-S1` (ARMED: the gateway mounts no timeline route) | **CARRIED, disarmed by a measured condition** | This seat read BOTH planes. DESIRED: `scoped-amgt-api.tf`'s `scoped_amgt_routes` list names no timeline route. APPLIED: `apigatewayv2 get-routes` on `7k3ed8px20` returns **16 AMGT route keys, 0 containing `timeline`**, and `/thesis` is present as the positive control. No user can reach the routes, so the hazard is unreachable today. The remedy is the round-12 gateway mount cell (packet s.6 item 1) |
| `Z-W31-S2` (ARMED: silver headline-scan latency) | **CARRIED, disarmed by the same condition** | Latency is not reachable while the route is unmounted. ⚠ The packet's own close run times the RANGE route at **19.9 s**, not the 5.4 s `Z-S34` cites. Its conclusion stands: **both** routes must be timed from the deployed Lambda against 29 s at round 12 |
| `Z-S34` (INERT: the disarm record, by specification only) | CARRIED as a note | It claims no remedy, correctly. Its 5.4 s figure is superseded by the packet's 19.9 s |
| `Z-W34-S1` (INERT: z-3's premise held at 1 site of 8) | CARRIED as a note | The audit re-targeted 8 of 8 and found a miss at 1. The premise was over-broad, and nothing was left broken |

`Z-S33` reads GRADUATED on the fold. REMEDIATION_v4 keeps its header mount open until it is served. That is a remediation carrier
already on file, and nothing is owed from this round.

## 2. THE SERVED ACT -- the signed radius, checked against the packet's own evidence

One object was ADDED (`date=2026-09-28/part-20260928T210944Z.parquet`, 8 rows), the 3 prior ETags are unchanged, and the
signed code was last changed before both halves were signed. This seat read the new object through z-1's AC4 script, run
here against S3 rather than taken from the recorded instance: **`events served: 8`, from that exact key.**

## 3. L9 -- `z-1` AC4, "ARE THE 8 SERVED EVENTS THE REAL COVERAGE BURSTS?"

**Andrew's standard:** an event about a DIFFERENT company's product is not this security's burst.

| # | security / day | lead | span | grade |
|---|---|---|---|---|
| 1 | Lenovo 02-12 | earnings beat on AI demand | 2 A, both results | **REAL, lead names it** |
| 2 | Lenovo 05-22 | Q4 beat, 84% AI growth | 2 A about results; 1 B = a European index open | **REAL, lead names it** (the B item is market colour, tier B) |
| 3 | Lenovo 08-13 | record revenue | 2 A, both results | **REAL, lead names it** |
| 4 | Boeing 08-26 | FAA Dreamliner inspections | 2 A: the FAA order + Wisk vertiport | **ABOUT BOEING, BUT TWO UNRELATED STORIES** -- a same-day coincidence, not one burst |
| 5 | Boeing 09-08 | Miami runway overshoot | 4: runway (1), **August deliveries (2)**, analyst roundup (1 B) | **ABOUT BOEING; THE LEAD NAMES THE MINORITY STORY** -- the plurality is deliveries |
| 6 | Costco 09-14 | motor-oil price hike / rationing | 2 A, same story | **REAL, lead names it** |
| 7 | Home Depot 08-18 | results beat | 2 A, same story | **REAL, lead names it** |
| 8 | Nvidia 06-01 | first PCs for AI agents | 3 A, all Nvidia's PC push | **REAL, lead names it** -- and ⭐ this is the 06-01 story that round 10 had wrongly carried as a LENOVO event; it now sits on the company whose product it is |

**VERDICT: PASS on Andrew's standard, 8 of 8.** Every article in every span is about the event's own security, and the Nvidia
story has moved to Nvidia. **On "does the lead name what the burst was about": 6 of 8 yes, 2 of 8 no, both Boeing.**

⭐ **THE TWO MISSES HAVE ONE MECHANISM, AND IT IS MEASURED, NOT INFERRED.** The builder picks the lead as the **earliest tier-A
article, with ties broken by lowest key** (`lib/research/harvest/tests/test_publication_gold_event.py:181`,
`test_lead_headline_is_deterministic`: "Earlier tier A", "bbg, lowest key"). That rule picks the FIRST story of the day, not the
DOMINANT one. It is right whenever a day carries one story (6 of 8), and wrong exactly when a day carries several (both Boeing
days). All 8 spans are ONE day with 2-4 articles, so **"burst" here means "at least 2 publishers on the same day"**, and a
large-cap like Boeing clears that on unrelated news. This is recorded for the analysis. It is not held against the round,
because the round's amended rule was about WHOSE event it is, and that passes 8 of 8.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 4 of 4 on their last `<status>` tag. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 2 ARMED, both CARRIED, disarmed by a condition this seat measured on both
   planes (desired + applied, with a positive control). **MET**
3. **Every judgment criterion graded** -- 1 of 1, on the served object read from S3 by this seat. **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S29",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-28T21:55:00Z",
    "one_line": "L9 round 11: z-1 AC4 PASSES Andrew's standard 8 of 8 -- every served event is about its own security, and the 06-01 Nvidia PC story now sits on NVDA, not Lenovo. The lead names the burst on 6 of 8. Both misses are Boeing days carrying unrelated stories, because the builder's lead rule is earliest tier-A (measured in its own test), and a 1-day, 2-publisher threshold lets a large-cap's coincident news count as a burst. L8: both ARMED rows are carried, disarmed by a condition read on both planes -- 0 timeline routes of 16 live AMGT routes, /thesis present.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: HVST-z-0, z-1, z-2, z-3 all read 'complete' on their LAST <status> tag at HEAD; exactly 1 criterion carries judgment=\"true\" (z-1 AC4).",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') reads 75 items, unknown []; GRADUATED 46, DISMISSED_WITH_REASON 25, UNDER_INVESTIGATION 4. The 4 are Z-W34-S1, Z-W31-S1, Z-W31-S2 and Z-S34, which reproduces the packet's fold independently.",
        "Z-W31-S1 CARRIED, disarmed by condition on BOTH planes. DESIRED: infra/aws/terraform/harvest/scoped-amgt-api.tf's scoped_amgt_routes list (lines 315-334) names no timeline route. APPLIED: apigatewayv2 get-routes --api-id 7k3ed8px20 returns 16 route keys containing /api/scoped/amgt, 0 containing 'timeline', and 1 ending /thesis as the positive control. The handler does register both timeline routes (lib/research/api/scoped_amgt.py:3962-3963), so the gap is exactly the gateway mount, which is the round-12 cell.",
        "Z-W31-S2 CARRIED, disarmed by the same condition. The packet's close run timed the RANGE route at 19.9 s and the day route at 16.7 s, in-process from this box, against the 5.4 s z-0 measured and Z-S34 cites; in-region Lambda latency is UNMEASURED. Both routes must be timed from the deployed Lambda against 29 s.",
        "SERVED ACT: z-1 AC4's script, re-run by this seat against S3, reads 'events served: 8' from s3://opal-data-harvest/amgt/harvest/gold/chatter_event/date=2026-09-28/part-20260928T210944Z.parquet, which is the one ADDED object named in the packet.",
        "L9 per event, from that run: (1) 992_HK 02-12, 2 A, both Lenovo results; (2) 992_HK 05-22, 2 A Lenovo results + 1 B European index open; (3) 992_HK 08-13, 2 A Lenovo results; (4) BA 08-26, 2 A: 'FAA Orders Inspections of Some Boeing Dreamliners for Gaps' + 'Boeing's Wisk breaks ground on California vertiport', two unrelated stories; (5) BA 09-08, lead 'Everything to Know About the Boeing Jet That Overshot a Miami Runway' (barrons 14:06), but 2 of 4 articles are August deliveries (bbg 15:00, sa 15:22) and 1 B is a multi-company analyst roundup; (6) COST 09-14, 2 A, motor-oil rationing; (7) HD 08-18, 2 A, results beat; (8) NVDA 06-01, 3 A, Nvidia's AI PC push.",
        "VERDICT on Andrew's standard (an event about a different company's product is not this security's burst): PASS 8 of 8. On whether the lead names what the burst was about: 6 of 8 yes; no on events 4 and 5, both Boeing.",
        "MECHANISM, MEASURED: lib/research/harvest/tests/test_publication_gold_event.py:181 test_lead_headline_is_deterministic asserts the lead is the earlier tier-A article ('Earlier tier A') with ties broken by lowest key ('bbg, lowest key'). The rule is correct on a single-story day and picks the first, not the dominant, story on a multi-story day. All 8 served spans are 1 day with 2-4 articles, so the burst threshold is in effect 'at least 2 publishers on the same day', which a large-cap clears on coincident news."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item; the two ARMED rows stay open as carried.",
    "spec_asserts": "The packet @c5f0cfd0ce asserts 4 orders terminal and VALID, one object added to chatter_event gold with the signed radius held, 8 served events presented for judgment, and 4 open rows whose two ARMED members are unreachable because the gateway mounts no timeline route.",
    "world_is": "All of that is true as re-measured, including the gateway on the APPLIED plane (0 timeline routes of 16). The 8 events pass Andrew's whose-event standard 8 of 8, but the lead misnames the burst on 2 of 8 Boeing days, because the lead rule is earliest-tier-A and a 1-day, 2-publisher burst admits coincident stories.",
    "notes": "FOR THE ROUND-11 ANALYSIS, two items. (1) THE LEAD RULE. Earliest tier-A is deterministic and tested, and wrong exactly on multi-story days. A lead that names the plurality story (or an event split per story) would fix both misses; which one is a product call for the analysis, not this seat's. (2) THE BURST THRESHOLD. At 1 day and 2 publishers, every served event is the minimum shape, and a large-cap's unrelated same-day items qualify. Round 12's judgment criterion should present at least one event per security with more than 2 articles, or name that none exists, so the burst definition itself is exercised."
  }
]
```
