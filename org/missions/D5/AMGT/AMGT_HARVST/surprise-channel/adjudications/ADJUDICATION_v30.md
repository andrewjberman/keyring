# AMGT_HARVST ROUND 22 -- L8 COMPILE + L9 (l-2 AC4)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~01:1xZ
**Input:** `2.0.0_SA_COO~H`'s `round22/ROUND22_DRAIN_END_PACKET.md` @`f6276a`, msg 26817. The packet was read to EOF (3,362 B).
**L7 re-measured, not adopted:** `l-1`, `l-2` read `complete` on their LAST `<status>` tag. There is 1 judgment criterion (`l-2`
AC4). Class: SERVED.

---

## 1. THE SERVED STATE, RE-READ BY THIS SEAT

- **S3:** `chatter_event` `date=2026-09-30/part-20260930T001658Z`, ETag `f57dca9bac8ac402ace2286548ea7c96`, **8 rows**. This seat
  read them with pyarrow. The 3 changed events are exactly:
  - 992_HK `8be45608...` 08-13..08-14, "Lenovo Posts Record Revenue ...";
  - AMZN `db2286aa...` 09-06..09-07, "Amazon Cargo Plane Overshoots Runway in Miami, Killing Five";
  - HD `3edd3079...` 08-17..08-18, "Home Depot Stock Rises as Earnings Defy Housing Slump".
  - The other 5 keep their ids.
- **The deployed function:** `/api/scoped/amgt/security/HD_US_Equity/timeline` returns 200 with one event, 08-17..08-18, led by
  "Home Depot Stock Rises as Earnings Defy Housing Sl...". The served read equals the landed part.

## 2. L9 -- `l-2` AC4: "is each CHANGED event ONE story about its own company, and does its lead name that story?"

Read from `0.9.0_WK_AMGT_HARVST~52/l2_ac4_output.txt` (members read from S3) against the part above.

| event | verdict |
|---|---|
| **992_HK** 08-13..08-14, 3 members, all Lenovo's Q1 (the report, the stock's jump, the BofA upgrade) | **MET.** One story, and the lead names Lenovo. |
| **AMZN** 09-06..09-07, 5 members, all the Miami cargo-plane crash; the 09-08 Boeing-jet explainer is guarded (`co_mention_count` 5) | **MET.** One story, and the lead is the first report, naming Amazon. |
| **HD** 08-17..08-18, 3 earnings pieces plus the guarded 08-20 roundup | **MET.** One story, and the lead names Home Depot. The lead's stored day is a day early and **disclosed** under ruling 3, since k-2 found no updated time. It is now visible to a PM: the served lead moved from bbg (08-18) to the barrons piece (08-17). |

**AC4: MET, 3 of 3.**

**A correction to this seat's v29 note.** v29 said `is_roundup` "fires on single-subject stories". l-1 measured that
`is_roundup` equals `co_mention_count >= 5` on 304 of 304 rows. So the flag is a peer-count rule, not a topic classifier, and it
does exactly what it says. The substantive point survives in sharper form: **a peer-count guard cannot tell a single-subject
story that names its peers from a roundup.** NVDA's two "Nvidia's PC push" pieces and AMZN's crash explainer each name 5 or more
companies and are guarded for that reason. l-1 now guards on `co_mention_count >= 4` alone, which is outcome-identical on 8 of 8
events today.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W41-S1` (ARMED: the AMZN crash forms a narrow 3-article, one-day event led by a non-first report) | **GRADUATED** | Served now as 09-06..09-07, 5 articles, led by bbg's first report (section 1). The pictured 09-10 NTSB piece stays outside; that is the link window, carried by `Z-W48-S1`. |
| `Z-W48-S1` (the link window) | **CARRIED** -> the analysis | the only remaining gap to the pictured burst |
| `Z-W49-S3`, `Z-W49-S4`, `Z-W50-S1` and the other INERT notes | **CARRIED** | unchanged |
| RESAPP `yy-5` shipping HARVST's code INERT | noted, not a row | ruled by the CTO; `get_timeline_event` is unwired and unmounted |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W41-S1` GRADUATED on the served read. **MET**
3. **Every judgment criterion graded:** 1 of 1 MET. **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S40",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T01:15:00Z",
    "one_line": "L9 round 22: l-2 AC4 MET 3 of 3 -- the served 992_HK, AMZN and HD events (part f57dca9b, 8 rows, read by this seat; HD live on /timeline) are each one own-company story led by a headline naming it; Z-W41-S1 graduates (AMZN now led by the first report); v29's is_roundup note corrected: it is co_mention>=5 by measurement, a peer-count rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S3 opal-data-harvest amgt/harvest/gold/chatter_event/date=2026-09-30/part-20260930T001658Z.parquet ETag f57dca9bac8ac402ace2286548ea7c96, 8 rows; changed events 8be45608d81b (992_HK 08-13..08-14), db2286aabb9f (AMZN 09-06..09-07), 3edd30795cb9 (HD 08-17..08-18).",
        "Deployed /api/scoped/amgt/security/HD_US_Equity/timeline -> 200, events [(08-17, 08-18, 'Home Depot Stock Rises as Earnings Defy Housing Sl...')].",
        "l2_ac4_output.txt: members per changed event with guard status; AMZN barrons:WP-BAR-0001904706 GUARDED (is_roundup=True co_mention_count=5).",
        "Packet s.1: l-1 'is_roundup differs from co_mention_count >= 5 on 0 of 304 rows'."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W41-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @f6276a asserts l-1 and l-2 terminal and VALID, chatter_event served on the span rule (KEPT 5 / CHANGED 3 / GONE 0), a close run 6 of 6 OK, and asks l-2 AC4 of the three changed events.",
    "world_is": "True as read on S3 and on the deployed function; each changed event is one own-company story. The peer-count guard cannot tell a subject story that names its peers from a roundup -- a limit, not a defect, today.",
    "notes": "FOR THE ROUND-22 ANALYSIS: the link window (Z-W48-S1) is the only gap to the pictured AMZN burst; HD's served lead now shows a day-early date, disclosed under ruling 3."
  }
]
```
