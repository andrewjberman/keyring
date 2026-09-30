# AMGT_HARVST ROUND 21 -- L8 COMPILE (no judgment criterion; the offered plausibility read answered)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~00:0xZ
**Input:** `2.0.0_SA_COO~H`'s `round21/ROUND21_DRAIN_END_PACKET.md` @`016b21`, msg 26792. The packet was read to EOF (3,232 B).
**L7 re-measured, not adopted:** `k-1`, `k-2` read `complete` on their LAST `<status>` tag. 0 judgment criteria. Class: LOCAL.

---

## 1. RE-RUN BY THIS SEAT

`k1_ac2_dry_rebuild.py` (the k-1 AC2 invocation) on the trunk read:
- "COUNTS of 8 served: KEPT=5 CHANGED=3 MERGED=0 GONE=0 (sum 8); NEW events ... =0";
- "AC2 RESULT: PASS ((b)=True (c)=True (d)=True (e)=True)".

It left `0.9.0_WK_AMGT_HARVST~49/`'s committed files unchanged (`git status` empty on that folder before and after). That is the
effect the issuer had to self-correct.

## 2. THE OFFERED PLAUSIBILITY READ -- "is each of the 3 CHANGED events one story about its own company, led by a headline that names it?"

Read from `0.9.0_WK_AMGT_HARVST~49/k1_ac2_output.txt`, with guard status per member.

| event | members (core / guarded) | verdict |
|---|---|---|
| **992_HK** 08-13..08-14 | 3 core, all Lenovo's Q1: "Lenovo Posts Record Revenue ...", "... jumps on strong Q1 revenue ...", "... upgraded to Buy at BofA following earnings" | **YES.** The lead names Lenovo. |
| **AMZN** 09-06..09-07 | 4 core, the crash story, led by bbg's first report "Amazon Cargo Plane Overshoots Runway in Miami, Killing Five"; 1 guarded, barrons "Everything to Know About the Boeing Jet That Overshot a Miami Runway" (`is_roundup`) | **YES.** The lead names Amazon, and the span no longer runs past the story. |
| **HD** 08-17..08-18 | 3 core earnings pieces; 1 guarded, the 08-20 "6 Big Takeaways From Retail's Big Week of Earnings" (`co_mention=4`) | **YES.** The lead names Home Depot. The span no longer reaches 08-20, which fixes the stretch v28 named. The 08-17 start rests on the retitled barrons preview. It is accepted and disclosed under the CTO's ruling 3: k-2 finds no updated time on any barrons, bbg or ft article (0 of 15, 0 of 19, 0 of 14). |

**The guard's `is_roundup` input is unreliable in both directions.** The ruled threshold 4 works around this, and the analysis
should know it:
- **It misses a real roundup:** HD's 4-company "Big Week of Earnings" piece is caught only by `co_mention=4`.
- **It fires on single-subject stories:**
  - NVDA's "Nvidia targets the PC market; Which stocks stand to gain?" and "Nvidia's PC push lifts PC maker, Arm; pressures
    Qualcomm, Intel, AMD" are both about Nvidia's own move;
  - AMZN's "Everything to Know About the Boeing Jet ..." is the crash story itself.
  - At threshold 3 the misfire deleted NVDA's served event outright (`Z-W49-S1`). At 4 it only trims members.
  - A flag that marks a company's own story as a roundup is a future GONE waiting for a lower threshold.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W49-S1`, `Z-W49-S2` (BLOCKING: AC2 cannot hold at threshold 3) | **GRADUATED** | The CTO ruled 4 (@`168acda05e`); AMENDMENT 1 `c4f2fedc94`; `Z-W49-S5` records the disarm; this seat's re-run PASSes at 4 (section 1) |
| `Z-W49-S5` (the amendment record) | **GRADUATED** | as above |
| `Z-W41-S1` (ARMED: the AMZN crash forms a narrow event) | **CARRIED** -> round 22's served rebuild | The new rule forms the 09-06..09-07 event of 5, led by the first report, but only in LOCAL code. The served event is still the old one until round 22. The 6th (09-10 NTSB) article still needs the link window (`Z-W48-S1`). |
| `Z-W49-S3`, `Z-W49-S4`, `Z-W50-S1`, `Z-W48-S1` | **CARRIED**, INERT | for the analysis. `Z-W50-S1`'s fact (today's served HD event is bbg-led, 08-18) means round 22's rebuild moves HD's lead to the retitled barrons preview. That is disclosed under ruling 3, but it is a visible change for a PM. |

`_latest_dispositions('.', 'AMGT_HARVST')` before this row returned **118 items: 63 GRADUATED, 25 DISMISSED_WITH_REASON,
30 UNDER_INVESTIGATION**, read from 33 files, with 0 unknown targets.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W49-S1`/`S2` GRADUATED on the ruling and this seat's re-run; `Z-W41-S1`
   CARRIED to the served round. **MET**
3. **Every judgment criterion graded:** 0. The offered read is answered in section 2. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S39",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T00:05:00Z",
    "one_line": "L8 round 21: k-1 AC2 re-run PASS at the ruled threshold 4 (KEPT 5, CHANGED 3, GONE 0; committed files untouched); the 3 CHANGED events are each one own-company story led by a headline naming it; is_roundup misses HD's 4-company roundup and fires on NVDA's and AMZN's own stories; Z-W49-S1/S2/S5 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-HVST-k-1 and k-2 read 'complete' on their LAST <status> tag.",
        "k1_ac2_dry_rebuild.py re-run by this seat: 'COUNTS of 8 served: KEPT=5 CHANGED=3 MERGED=0 GONE=0 (sum 8)', 'AC2 RESULT: PASS ((b)=True (c)=True (d)=True (e)=True)'; git status on 0.9.0_WK_AMGT_HARVST~49/ empty after.",
        "k1_ac2_output.txt members: NVDA sa:4598755 and sa:4598761 GUARDED(is_roundup); AMZN barrons:WP-BAR-0001904706 GUARDED(is_roundup); HD barrons:WP-BAR-0001879611 GUARDED(co_mention=4); new-rule 992_HK 08-13..08-14 (3), AMZN 09-06..09-07 (5, lead bbg:TKYJAAVTTCZL00), HD 08-17..08-18 (4).",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') 118 items (63 GRADUATED, 25 DISMISSED_WITH_REASON, 30 UNDER_INVESTIGATION), 33 files."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W49-S1",
      "AMGT_HARVST-Z-W49-S2",
      "AMGT_HARVST-Z-W49-S5"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @016b21 asserts k-1 and k-2 terminal and VALID at the ruled guard threshold 4, the close run clean, and offers a plausibility read on the 3 CHANGED events.",
    "world_is": "True as read. The rule is right on all three changed events; the guard reaches the right answer at 4 despite an is_roundup flag that is wrong in both directions.",
    "notes": "FOR THE ROUND-21 ANALYSIS: is_roundup marks own-company stories as roundups (NVDA x2, AMZN's crash explainer) and misses a 4-company roundup (HD); at threshold 3 that deleted NVDA's served event. Round 22's served rebuild will move HD's lead from bbg (08-18) to the retitled barrons preview (08-17), disclosed under ruling 3 but visible to a PM."
  }
]
```
