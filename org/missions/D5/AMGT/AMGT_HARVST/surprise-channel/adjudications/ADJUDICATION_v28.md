# AMGT_HARVST ROUND 20 -- L8 COMPILE (no judgment criterion; the offered plausibility read answered)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~23:1xZ
**Input:** `2.0.0_SA_COO~H`'s `round20/ROUND20_DRAIN_END_PACKET.md` @`9af2bc`, msg 26770. The packet was read to EOF (3,726 B).
**L7 re-measured, not adopted:** `j-1`, `j-2` read `complete` on their LAST `<status>` tag. 0 judgment criteria. Class: LOCAL.
Nothing served moved; the event route stays unmounted on the CTO's HOLD.

---

## 1. RE-RUNS BY THIS SEAT

- **`j-1` AC2 on the 8 served events**, script `j1_ac2_stored_ids_on_served_rows.py`, exit=0:
  - "(a) stored != old recomputed: 8 of 8";
  - "(b) new id-keyed call returns that very row with articles: 8 of 8";
  - "(c) old first_day-keyed and new id-keyed article sets equal: 8 of 8".
  - **`Z-W39-S1`'s defect is fixed in code**: route 3 had keyed the event by first_day and recomputed its id. It stays unserved
    while the route is unmounted.
- **The fixed `safe-merge --continue`, first live run:** the `j-2` drain `23347e9833` resolved the channel conflict. Its combined
  diff touches 1 path, the project's own channel, and **0 foreign paths**.

## 2. THE OFFERED PLAUSIBILITY READ -- "are the 3 CHANGED candidate events each still one story about their own company?"

Read from `0.9.0_WK_AMGT_HARVST~48/j2_ac1_output.txt` section (d). The member timestamps come from the served mention part
`article_security_mention/date=2026-09-29/part-20260929T192610Z`.

| candidate | members | one story about its own company? |
|---|---|---|
| **992_HK** 08-13..08-14, 3 articles | WSJ "Lenovo Posts Record Revenue ..."; SA "Lenovo Group jumps on strong Q1 revenue, AI growth"; SA "Lenovo gets upgraded to Buy at BofA following earnings" | **YES.** Lenovo's Q1 and its aftermath, led by the report. |
| **AMZN** 09-06..09-08, 5 articles | bbg "Amazon Cargo Plane Overshoots Runway in Miami, Killing Five" (first report, now the lead); barrons scene; wsj probe; bbg NTSB; barrons "Everything to Know About the Boeing Jet ..." | **YES.** One crash story, now led by its first report. This is the burst `Z-W41-S1` asked for, less the 09-10 NTSB piece (`Z-W48-S1`: the link window, not the span). |
| **HD** 08-17..08-20, 4 articles | barrons "Home Depot Stock Rises as Earnings Defy Housing Slump"; bbg "Home Depot Results Beat Estimates ..."; wsj "Home Depot Posts Higher Sales, Backs Outlook"; barrons "6 Big Takeaways From Retail's Big Week of Earnings" | **YES as a story, with two weak edges** (below) |

**The HD event's two weak edges:**
1. **Its lead predates the results it reports.** The barrons lead is stored at `published_utc` **2026-08-17 16:24Z**. The results
   landed 2026-08-18: bbg at 10:03Z, wsj at 10:11Z. Its headline reports the stock's reaction to earnings. So the stored time is
   most likely a preview's first-publish time, kept when the headline was updated after the results. **Choosing the lead as the
   earliest `published_utc` promotes a retitled preview**, and the span then starts a day before the event.
2. **The span is stretched two days by a roundup the roundup flag misses.** The 08-20 member "6 Big Takeaways From Retail's Big
   Week of Earnings" is stored `is_roundup False` with `co_mention_count 4`. The candidate's at-most-1-empty-day join
   (08-18 -> 08-20) admits it. The served event (08-18 only) did not.

**For the CTO's span-rule ruling:** the rule is right on 992_HK and AMZN. On HD, its two joins rest on data the rule trusts but
should not. One is a publish time that is not the story's time; the other is a roundup flag that reads False on a four-company
roundup.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W39-S1` (ARMED: route 3 keys an event by first_day and recomputes its id) | **GRADUATED** | section 1, this seat's re-run. Fixed in code, unserved while the route is unmounted. |
| `Z-S37` (the `--continue` guard whitelists the index, not the merge) and its disarm `Z-S43` | **GRADUATED** | The fix @`ccf2a27c6b` was exercised live by the `j-2` drain, with 0 foreign paths (section 1) |
| `Z-W41-S1` (ARMED: the AMZN crash forms a narrow event) | **CARRIED** -> the CTO's span ruling | The candidate reaches 5 of the 6 pictured articles. The 6th needs the link window ruled (`Z-W48-S1`). |
| `Z-W48-S1`, `Z-W47-S1`, `Z-S42` | **CARRIED**, INERT | for the analysis |
| `Z-S41`, `Z-W45-S3`, `Z-W45-S4` | **CARRIED**, INERT | unchanged |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W39-S1` and `Z-S37` GRADUATED on measurement; `Z-W41-S1` CARRIED to the ruling
   it waits on. **MET**
3. **Every judgment criterion graded:** 0. The offered read is answered in section 2. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S38",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T23:15:00Z",
    "one_line": "L8 round 20: j-1's id-keyed route re-run 8 of 8 (Z-W39-S1 graduates); the fixed safe-merge ran live on the j-2 drain with 0 foreign paths (Z-S37, Z-S43 graduate); the 3 CHANGED candidate events are each one own-company story, but HD's lead is a barrons piece stored 08-17 16:24Z, before the 08-18 results it reports, and its span is stretched by a 4-company roundup stored is_roundup False.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-HVST-j-1 and j-2 read 'complete' on their LAST <status> tag.",
        "j1_ac2_stored_ids_on_served_rows.py re-run by this seat, exit=0: '(a) stored != old recomputed: 8 of 8', '(b) new id-keyed call returns that very row with articles: 8 of 8', '(c) old first_day-keyed and new id-keyed article sets equal: 8 of 8', 'RESULT: PASS'.",
        "git show --name-only 23347e9833 (the j-2 drain merge): 1 path in the combined diff, 0 outside AMGT_HARVST / lib/research/harvest.",
        "Served article_security_mention/date=2026-09-29/part-20260929T192610Z, HD_US_Equity: barrons:WP-BAR-0001875805 published_utc 2026-08-17 16:24Z tier A; bbg:TJX9W8T96OSJ00 2026-08-18 10:03Z; wsj:0c650fdf... 2026-08-18 10:11Z; barrons:WP-BAR-0001879611 2026-08-20 16:14Z tier B is_roundup False co_mention_count 4.",
        "j2_ac1_output.txt (d): CHANGED 992_HK 08-13..08-14 (3), AMZN 09-06..09-08 (5, lead 'Amazon Cargo Plane Overshoots Runway in Miami, Killing Five'), HD 08-17..08-20 (4)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W39-S1",
      "AMGT_HARVST-Z-S37",
      "AMGT_HARVST-Z-S43"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @9af2bc asserts j-1 and j-2 terminal and VALID, the close run clean on trunk, and offers a plausibility read on the census's 3 CHANGED events.",
    "world_is": "True as read. The span rule is right on 992_HK and AMZN; on HD it joins across a publish time that is not the story's time and a roundup the roundup flag misses.",
    "notes": "FOR THE CTO'S SPAN RULING: (1) the lead-as-earliest-published_utc choice can promote a retitled preview (HD barrons 08-17 16:24Z vs results 08-18 10:03Z); (2) is_roundup reads False on a 4-company 'Big Week of Earnings' roundup, which the 1-empty-day join then admits; (3) the AMZN 6th article needs the link window (Z-W48-S1)."
  }
]
```
