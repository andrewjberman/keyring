# AMGT_HARVST ROUND 14 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~07:5xZ
**Input:** `2.0.0_SA_COO~H`'s `round14/ROUND14_DRAIN_END_PACKET.md` @`f9f4378a8c` (read to EOF, 4,325 B), msg 26494.
**L7 RE-MEASURED not adopted:** `c-1` reads `complete` on its LAST `<status>` tag; 1 judgment criterion (`c-1` AC4).

---

## 1. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **94 items, 13 UNDER_INVESTIGATION**, which reproduces the packet's fold. **Gating (ARMED): `Z-S37`,
`Z-W39-S1`, `Z-W40-S1`.**

| row | disposition | grounds |
|---|---|---|
| `Z-W40-S1` (ARMED: name detection strips a single-story security's own recurring words, so its FIRST burst forms no event) | **CARRIED, disarmed by specification** | A planted-fixture defect, latent: no security in today's harvest has that shape. The reading rule (any cell onboarding or grading a new security reads this row first) travels with the round-15 fix |
| `Z-W39-S1`, `Z-S37` | **CARRIED**, as at round 13 | unchanged |
| `Z-W40-S2`, `Z-W40-S3` | **CARRIED** as INERT notes | the rule as written; the unit choice named |

## 2. L9 -- `c-1` AC4

This seat re-ran `ac4_held_out_for_l9.py`: 130 held-out rows over 50 securities (44 tier-A/B rows over 24), with the five tuned
securities excluded.

### (1) HELD-OUT EVENTS -- **NONE; NOT A PRECISION GRADE.** Round 13's 7 of 7 stays IN-SAMPLE, as the packet says.

### (2) "IS ANY OF THE 6 NEAR-MISS CLUSTERS A REAL BURST ABOUT ITS OWN COMPANY THAT THE RULE DECLINED?" -- **YES, ONE.**

| cluster | articles | about its own company? | a real burst? |
|---|---|---|---|
| 2b-1 AMZN 09-01..09-02 | YouTube partnership; DOJ beef-price probe | yes, but two unrelated stories | **NO** |
| **2b-2 AMZN 09-06..09-10** | **"Amazon Cargo Plane Overshoots Runway in Miami, Killing Five" (bbg); "Everything to Know About the Boeing Jet That Overshot a Miami Runway" (barrons); "Amazon Jet Tried to Abort Landing Before Fatal Crash, NTSB Says" (bbg)** | **YES -- one story, Amazon's cargo jet and its fatal crash** | **YES -- DECLINED** |
| 2b-3 DELL, 2b-4 INTC, 2b-5 MSFT, 2b-6 QCOM (06-01) | Nvidia's PC push, from the neighbours' side | no -- co-mentions of another company's product | **NO**, correctly declined (the round-9 shape) |

⭐ **WHY IT WAS DECLINED -- the tier rule, not the story rule.** All three AMZN articles read tier B, and "the rule never forms a
story without a tier-A article". `assign_tier` (`publication_gold.py:93-106`) gives tier A only when the security is in the title
**and** the lead. Amazon is the subject of two of the three headlines, so the missing condition must be the lead: either no stored
lead or one that does not name Amazon. *Which of the two is UNMEASURED here.* If headline-only captures carry no lead, **tier A is
structurally unreachable for them, and every such burst is declined whatever its size.**

⭐ **AND IT CLOSES A THREAD FROM ROUND 13.** The Barrons article in this cluster is the "runway" headline that round 13 split out of
Boeing's 09-08 event, a split this seat graded right. **Its story is Amazon's crash, not Boeing's news**, and it has now surfaced
where it belongs, one tier short of an event.

⭐ **AND IT IS THE BURST SHAPE THIS SEAT SAID HAD NEVER BEEN EXERCISED:** 3 articles over **5 days**. Every served event is 1 day. The
packet's census defines "larger" as >= 5 articles over >= 2 days, so it reads that shape UNEXERCISED, correctly by its own
definition. But a multi-day burst **does exist in the held-out harvest**, and it is being declined at the tier step, not
measured.

**VERDICT: AC4 -- (1) no held-out event, no precision grade; (2) ONE real declined burst (AMZN 09-06..09-10), declined at the tier
gate.** This is a recall finding.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- 1 of 1. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 3 ARMED, all CARRIED with reasons (one disarmed by specification, one by
   condition). **MET**
3. **Every judgment criterion graded** -- 1 of 1. **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S32",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T07:55:00Z",
    "one_line": "L9 round 14: the held-out read forms 0 events, so round 13 stays in-sample. But ONE of the 6 near-misses is a real burst the rule declined: AMZN 09-06..09-10, three articles on Amazon's fatal Miami cargo-jet crash (bbg, barrons, bbg), declined because all three are tier B and tier A needs the name in title AND lead (publication_gold.py:93-106). It is the multi-day shape this seat said had never been exercised, and its Barrons piece is the runway article round 13 correctly split off Boeing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: HVST-c-1 reads 'complete' on its LAST <status> tag; judgment=\"true\" on AC4.",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') reads 94 items, 13 UNDER_INVESTIGATION; ARMED: Z-S37, Z-W39-S1, Z-W40-S1.",
        "L9, this seat's run of ac4_held_out_for_l9.py: 'held-out population: 130 rows over 50 securities (44 tier-A/B rows over 24 securities)'; 'PART 1: HELD-OUT EVENTS (0)'; '2a count: 0'; '2b count: 6'.",
        "2b-2 AMZN_US_Equity, 3 articles, tier-A 0: 'B bbg 2026-09-06 19:40 Amazon Cargo Plane Overshoots Runway in Miami, Killing Five'; 'B barrons 2026-09-08 14:06 Everything to Know About the Boeing Jet That Overshot a Miami Runway'; 'B bbg 2026-09-10 00:49 Amazon Jet Tried to Abort Landing Before Fatal Crash, NTSB Says'.",
        "2b-1 AMZN (YouTube partnership 09-01; DOJ beef-price probe 09-02) is two unrelated stories; 2b-3..2b-6 (DELL, INTC, MSFT, QCOM, 06-01) are the Nvidia AI-PC headlines seen from other companies.",
        "TIER RULE, lib/research/harvest/publication_gold.py:93-106 assign_tier: tier 'A' iff mention_in_title and mention_in_lead; 'B' if title or lead or share >= share_b. The AMZN headlines name Amazon in the title, so their lead lacks the name or is absent; which is unmeasured.",
        "CROSS-ROUND: the barrons 09-08 'Boeing Jet That Overshot a Miami Runway' article is the runway headline round 13 removed from BA_US_Equity's 09-08 event (ADJUDICATION_v21)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row adjudicates no investigation item; the ARMED rows are carried with their reasons.",
    "spec_asserts": "The packet @f9f4378a8c asserts c-1 terminal and VALID, 0 held-out events (not a precision grade), the larger burst shape UNEXERCISED, and 6 near-miss clusters presented for L9.",
    "world_is": "True as re-run by this seat. One of the 6 is a real burst about its own company, Amazon's fatal cargo-jet crash over 5 days, declined because every article is tier B, not because of the story rule. A multi-day burst does exist in the held-out harvest and is lost at the tier gate.",
    "notes": "FOR THE ROUND-14 ANALYSIS: (1) measure why the AMZN crash articles miss tier A (no stored lead on headline-only captures, or a lead without the name). If headline-only items carry no lead, tier A is unreachable for them, and a headline naming the security as its subject should be allowed to qualify. That is a recall fix at the tier gate, separate from Z-W40-S1's name-detection fix. (2) With that gate open, the AMZN crash becomes the first held-out event AND the first multi-day one, which is exactly what the precision read and the shape census both lack."
  }
]
```
