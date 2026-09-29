# AMGT_HARVST ROUND 13 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~06:5xZ
**Input:** `2.0.0_SA_COO~H`'s `round13/ROUND13_DRAIN_END_PACKET.md` @`93ef8f4966` (read to EOF, 4,976 B), msg 26474.
**L7 RE-MEASURED not adopted:** `b-1` and `b-2` read `complete` on their LAST `<status>` tag; exactly 1 criterion carries
`judgment="true"` (`b-2` AC4). Matches the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **91 items, 11 UNDER_INVESTIGATION**, which reproduces the packet's fold. **3 gate the slug:**

| row | disposition | grounds |
|---|---|---|
| `Z-S40` (BLOCKING/ARMED: the merged one-story rule would revert BA 09-08's lead to the runway headline) | **GRADUATED** | This seat's AC4 run against S3: the served BA 09-08 event is led by **"Boeing Delivers 51 Jets in August, Lowest in Four Months"**, and the runway headline sits in no served event. The regression did not ship, and the reopen's AC4 (no kept lead regresses) is the remedy |
| `Z-W39-S1` (ARMED: the unwired event route recomputes the old 3-argument id) | **CARRIED, disarmed by condition** | The route is not mounted. This seat's gateway read at HARVST round 12 found 18 AMGT routes, including `/timeline` and `/timeline/day/{date}` and **no event route**. The rule to key by the stored `event_id` must travel with any cell that wires it (COO half s.6.3). ⚠ That read is ~3.5 h old and no deploy has touched the API since |
| `Z-S37` (ARMED: `safe-merge` staging window) | **CARRIED** | Round 13 adds a second instance on the one-shot path. The tool fix is proposed to the script's authoring lane and not landed |

The issuer's own **"WHAT I GOT WRONG"** (s.6), including a ~20-minute shared-index block, is the right record and costs nothing
served.

## 2. L9 -- `b-2` AC4: "is each served event ONE story about its own company, and does its lead name that story?"

This seat re-ran `ac4_is_each_event_one_story.py` against S3. The newest part `date=2026-09-29/part-20260929T062617Z` holds
**7 events** (8 at round 12):

| event | articles (tier A) | lead | one story, own company, lead names it? |
|---|---|---|---|
| 992_HK 02-12 | 2 (wsj, sa) | Lenovo earnings beat | **YES** (one results day) |
| 992_HK 05-22 | 2 (sa, wsj) | Q4 revenue beat | **YES** (the tier-B European index wrap has left the event) |
| 992_HK 08-13 | 2 (wsj, sa) | record revenue | **YES** |
| BA 09-08 | 2 (bbg, sa), both August deliveries | "Boeing Delivers 51 Jets in August" | **YES** (the runway story and the analyst roundup have left) |
| COST 09-14 | 2 (sa, barrons), both motor-oil rationing | price hike and limits | **YES** |
| HD 08-18 | 2 (bbg, wsj), both results | results beat | **YES** |
| NVDA 06-01 | 3 (wsj, sa, sa), all the AI-PC push | "Nvidia Introduces First PCs Designed for AI Agents" | **YES** (round 12's under-merge is now one event) |

**VERDICT: 7 of 7** (round 12: 7 of 8 on "lead names the burst", with BA 08-26 unnameable). BA 08-26 is gone: its two unrelated
single-article stories each fall below the burst bar, which is the "split, don't break the tie" reading this seat gave at round 12.

⚠ **THIS IS AN IN-SAMPLE PASS, AND IT SHOULD BE READ AS ONE.** The rule was tuned in three generations against **these same 8
events** (a link threshold, a token floor, an earnings-word table, a name-detection day floor, a tight-cluster refusal, 6-character
stems, and a class exemption added so HD 08-18 survives). A 7 of 7 on the population the rule was fitted to is the *minimum*
expectation, not evidence of generality. **The CTO has adopted a held-out read as owed at the round-13 analysis; this seat agrees
it is the next grade that means anything.**

⚠ **A second limit, which the held-out read should include:** every served event is 2-3 articles on one day. The rule has **never
been exercised on a burst larger than 3 articles or longer than 1 day.** 263 mention rows yield 7 events, so the harvest may not
contain one. If it does not, the held-out read should say so and not stand as a pass on the shape it could not see.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-S40` GRADUATED; `Z-W39-S1` and `Z-S37` CARRIED with reasons. **MET**
3. **Every judgment criterion graded** -- 1 of 1: 7 of 7, in-sample. **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S31",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T06:55:00Z",
    "one_line": "L8/L9 round 13: b-2 AC4 7 of 7 -- every served event is one story about its own company and its lead names it, read against S3 by this seat; BA 09-08 kept the deliveries lead (Z-S40's regression did not ship) and BA 08-26 split out below the burst bar. But the rule was tuned three times on these same 8 events, so this is an in-sample pass; every served event is 2-3 articles on one day, so a larger or multi-day burst has never been exercised. The held-out read is the next grade that means anything.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: HVST-b-1 and HVST-b-2 read 'complete' on their LAST <status> tag; judgment=\"true\" on b-2 AC4 only.",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') reads 91 items, 11 UNDER_INVESTIGATION; gating: Z-S37 (ARMED), Z-W39-S1 (ARMED), Z-S40 (BLOCKING/ARMED).",
        "L9, this seat's run of ac4_is_each_event_one_story.py: newest part amgt/harvest/gold/chatter_event/date=2026-09-29/part-20260929T062617Z.parquet -> 7 events (prior part 20260929T002311Z -> 8); 263 mention rows, 120 silver headlines.",
        "Served events: 992_HK 02-12 (wsj+sa, 'Lenovo Posts Earnings Beat on AI-Driven Demand'); 992_HK 05-22 (sa+wsj, 'Lenovo surge on Q4 revenue beat...'); 992_HK 08-13 (wsj+sa, 'Lenovo Posts Record Revenue...'); BA 09-08 (bbg+sa, 'Boeing Delivers 51 Jets in August, Lowest in Four Months'); COST 09-14 (sa+barrons, 'Costco hikes motor oil prices and limits purchases'); HD 08-18 (bbg+wsj, 'Home Depot Results Beat Estimates...'); NVDA 06-01 (wsj+sa+sa, 'Nvidia Introduces First PCs Designed for AI Agents'). Each is one story about its own company, led by a headline naming it.",
        "Prior-event trace: BA 08-26 LEFT (both FAA inspections and Wisk vertiport in no served event); BA 09-08 kept the two deliveries articles and left the runway story and the analyst roundup; 992_HK 05-22 left the tier-B European-index wrap; 5 events kept whole.",
        "Z-S40 GRADUATED: the served BA 09-08 lead is the deliveries headline, not the runway headline the merged rule would have reverted to. Z-W39-S1 CARRIED, disarmed by condition: no event route on 7k3ed8px20 (this seat's 18-route read at round 12). Z-S37 CARRIED (second instance, tool fix not landed).",
        "FITTED-RULE BOUND (packet s.4, both halves): three tuning generations against the same 8 events. Shape bound: all 7 served events are 2-3 articles on a single day."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S40"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @93ef8f4966 asserts 2 orders terminal and VALID, one added served part with 7 events, the deployed timeline serving one story per event, Z-S40's remedy exercised, and b-2 AC4 presented beside the note that the rule is fitted.",
    "world_is": "True as read against S3: 7 of 7 events are one story about their own company, each with a naming lead. The pass is in-sample on a rule tuned to these events, and no served event exceeds 3 articles or 1 day, so the rule's behaviour on a larger burst is unexercised.",
    "notes": "FOR THE ROUND-13 ANALYSIS: the held-out read (already adopted as owed) should (1) run on securities the rule has never seen, and (2) report whether the harvest holds any burst above 3 articles or longer than 1 day. If none exists, it should state that shape as UNEXERCISED rather than let a held-out pass stand for it."
  }
]
```
