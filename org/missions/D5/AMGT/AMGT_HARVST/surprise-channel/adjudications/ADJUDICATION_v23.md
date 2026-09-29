# AMGT_HARVST ROUND 15 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~10:1xZ
**Input:** `2.0.0_SA_COO~H`'s `round15/ROUND15_DRAIN_END_PACKET.md` @`c16e2e5a93` (read to EOF, 6,408 B), msg 26557.
**L7 RE-MEASURED not adopted:** `d-1` and `d-2` read `complete` on their LAST `<status>` tag; 1 judgment criterion (`d-2` AC4).

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions`: **97 items, 16 UNDER_INVESTIGATION**, which reproduces the packet's fold. ARMED: `Z-S37`, `Z-W39-S1`, `Z-W40-S1`,
`Z-W41-S1`, `Z-W41-S2`.

| row | disposition | grounds |
|---|---|---|
| `Z-W41-S1` (the AMZN event is narrower than the ruling pictured: 3 of 6 crash articles, 1 day) | **CARRIED, disarmed by acceptance under the pair** | It is the rule as written, named in both halves before the put. **It is never read as a pass for the >= 5-article, multi-day shape**, which stays UNEXERCISED |
| `Z-W41-S2` (nested aliases double-count `mention_count`; `mention_score` moves) | **CARRIED, disarmed by specification** | Visible in this seat's run: the crash headline "Scene of Fatal Amazon Plane Crash..." reads `count=7`. The remedy (count distinct matched spans) is a round-16 candidate. Until it lands, `mention_count` and `mention_score` are not magnitudes |
| `Z-S37`, `Z-W39-S1`, `Z-W40-S1` | **CARRIED**, as at round 14 | unchanged |

## 2. L9 -- `d-2` AC4, re-run by this seat against S3 (newest parts: mention `...T092419Z`, event `...T092439Z`)

### (1) "Is each of the 12 new mention matches a real mention of that company, or a false hit on a common word?" -- **12 of 12 REAL; 0 false hits**

This seat read the TEXT around each match in the silver articles (`_iter_latest_articles`, 10 of 10 bodies found; the 2 crash
articles name Amazon in the headline). Every "Amazon" is the company:

| match | text around it |
|---|---|
| Sam's Club one-hour delivery (ft, B) | "a fresh competitive front with retail rivals **Amazon** and Costco"; "weeks after **Amazon** introduced one-hour delivery" |
| Costco, everyone agrees (wsj, D) | "Over 200 million American shoppers use **Amazon** Prime" |
| digital store labels (ft, D) | "retail behemoths such as Walmart, Costco and **Amazon**" |
| Home Depot earnings (barrons, D) | "a direct shot at **Amazon** / Walmart-style speed competition" |
| Kelce / Publicis NIL (wsj, D) | "**Amazon** is ordering large quantities of older books, scanning them to train A[I]" |
| When brands lose their magic (ft, D) | "market share that Walmart, Costco and **Amazon** add" |
| Walmart six-year low (ft, D) | "**Amazon** moving its Prime Day back to June" |
| Iran conflict market column (barrons, C) | "the **Amazon** cargo plane crash at Miami International Airport"; "**Amazon**, Boeing stocks slip" |
| Costco motor oil (sa, B) | "Walmart ( WMT ), **Amazon** ( AMZN ), and AutoZone" |
| TSM, memory costs (sa, D) | "manufacturing partners such as **Taiwan Semiconductor Manufacturing** ( TSM )" |

**VERDICT: 12 of 12 are the company.** None is the river or the rainforest. **Ten are co-mentions**: Amazon named as a rival or a
stock inside another company's story. The tier gate already places them low (B/C/D), and none forms or joins an event. The alias
adds recall without adding false events.

### (2) "The new AMZN 09-07 event: ONE story about its own company, and does its lead name it?" -- **YES**

The event holds 3 articles on 2026-09-07: barrons A **"Scene of Fatal Amazon Plane Crash in Miami Is 'Devastating'"** (the lead);
wsj A "Amazon Plane Crash Probe Examines Aircraft Speed, Runway Safeguards"; bbg B "NTSB Says Amazon Cargo Jet Hit Van, Car After
Runway Overrun". One story, Amazon's own crash, and the lead names it.

**This is the first HELD-OUT event** (AMZN was never tuned on), and it is correct, **but it is a sample of ONE.** It is not a
precision rate, and the larger shape stays UNEXERCISED.

### ⚠ A CORRECTION TO THIS SEAT'S ROUND-14 GRADE

ADJUDICATION_v22 said the AMZN crash articles missed tier A because "the lead lacks the name or is absent -- which is unmeasured".
**Neither held.** This round's run shows the same bbg articles, e.g. **"Amazon Cargo Plane Overshoots Runway in Miami, Killing Five"**,
now at **tier A**, with no change to their text. The cause was the **matcher's alias coverage**: "Amazon" was not a recognised form
of the company's name, so neither title nor lead counted as a mention. My round-14 two-way split left out the third cause. The fix
the COO cut (`d-1`, the alias) is the right one, and my stated mechanism was not.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 5 ARMED, all CARRIED with reasons. **MET**
3. **Every judgment criterion graded** -- 1 of 1: 12 of 12 real mentions; the event YES (a sample of one). **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S33",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T10:15:00Z",
    "one_line": "L9 round 15, re-run against S3 with the article text read: the 12 new mention matches are 12 of 12 the real company, 0 river or rainforest false hits (10 are co-mentions the tier gate keeps low). The new AMZN 09-07 event is one story, Amazon's own crash, led by a headline that names it -- the first held-out event, a sample of one. Correcting v22: the crash articles missed tier A because 'Amazon' was not a recognised name form, not because the lead lacked the name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: HVST-d-1 and HVST-d-2 read 'complete' on their LAST <status> tag; judgment=\"true\" on d-2 AC4.",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') reads 97 items, 16 UNDER_INVESTIGATION; ARMED Z-S37, Z-W39-S1, Z-W40-S1, Z-W41-S1, Z-W41-S2, all carried with reasons.",
        "L9 part 1, this seat's run of ac4_new_matches_and_events.py: 'new matches = 12 (2 on tier-A rows)'; 11 AMZN via alias 'Amazon', 1 TSM via 'Taiwan Semiconductor Manufacturing'. This seat read each match's surrounding text from publication_gold._iter_latest_articles (10 of 10 bodies): e.g. 'retail rivals Amazon and Costco', 'use Amazon Prime', 'Amazon moving its Prime Day back to June', 'Amazon ( AMZN )', 'Amazon is ordering large quantities of older books', 'the Amazon cargo plane crash at Miami International Airport', 'Taiwan Semiconductor Manufacturing ( TSM )'. None is the river or the rainforest.",
        "L9 part 2: 'NEW event c9e34b38e4ba: AMZN_US_Equity span 2026-09-07..2026-09-07 (1 day) articles=3 tier-A publishers=[barrons, wsj]', lead 'Scene of Fatal Amazon Plane Crash in Miami Is Devastating'; members wsj 'Amazon Plane Crash Probe Examines Aircraft Speed, Runway Safeguards', bbg 'NTSB Says Amazon Cargo Jet Hit Van, Car After Runway Overrun'.",
        "CORRECTION of ADJUDICATION_v22: the same run lists bbg 'Amazon Cargo Plane Overshoots Runway in Miami, Killing Five' (2026-09-06) and 'Amazon Jet Tried to Abort Landing Before Fatal Crash, NTSB Says' (2026-09-10) at tier=A, where round 14's run read them tier B. The text did not change; the alias did. So the round-14 cause was the matcher's name-form coverage, not a missing or name-less lead.",
        "Z-W41-S2 visible in the run: barrons 'Scene of Fatal Amazon Plane Crash...' reads count=7."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: adjudicates no investigation item; the ARMED rows are carried with their reasons.",
    "spec_asserts": "The packet @c16e2e5a93 asserts 2 orders terminal and VALID, three served tables rebuilt inside the pair, the deployed API serving the new AMZN event, and d-2 AC4 presented.",
    "world_is": "True as re-run against S3. The 12 matches are the real company in every case, and the AMZN event is one own-company story with a naming lead. It is held-out but a sample of one, and the multi-day shape stays unexercised. This seat's round-14 causal claim is corrected here.",
    "notes": "FOR THE ROUND-15 ANALYSIS: (1) the alias fix is the right mechanism for the tier gap, and the recall it adds is clean on 12 of 12; (2) the held-out read now has ONE event, and a precision rate needs more held-out bursts, which is bounded by capture, as the packet says; (3) Z-W41-S2's double count must land before any page presents mention_score as a magnitude."
  }
]
```
