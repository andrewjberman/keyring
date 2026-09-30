# AMGT_HARVST ROUND 18 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~20:1xZ
**Input:** `2.0.0_SA_COO~H`'s `round18/ROUND18_DRAIN_END_PACKET.md` @`0994b9332f`, msg 26686. The packet was read to EOF
(3,749 B).
**L7 re-measured, not adopted:** `g-1` and `g-2` read `complete` on their LAST `<status>` tag. There are 2 judgment criteria
(`g-1` AC4, `g-2` AC4). Class: SERVED.

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions('.', 'AMGT_HARVST')` returns **108 items: 58 GRADUATED, 25 DISMISSED_WITH_REASON,
25 UNDER_INVESTIGATION**. It reads 30 files.

| row | disposition | grounds |
|---|---|---|
| `Z-S37`, `Z-W39-S1`, `Z-W41-S1` (ARMED) | **CARRIED** | as in v25. `Z-W41-S1` (the AMZN crash event is narrow) stands unchanged, because the served events did not move (below). |
| `Z-W45-S1` (limb (a) refuses the ruling's own whole-brand `UBS`) | **CARRIED, INERT** | Harmless on this round's output. The exact-case ticker `UBS` still admits 7 hits, and all 7 are the bank (section 2). The list and the refusal limb disagree; that is for the analysis. |
| `Z-W45-S2` (the whole-brand `ASML` entered the listing_hit identifiers; 148 daily cells moved) | **CARRIED -- analysis input** | See section 3. |
| `Z-W45-S3` (a pre-cell producer ignores `ticker_aliases` silently) | **CARRIED, INERT** | a standing hazard for any old-code run |
| `Z-W45-S4` (the AC1 BEFORE record was overwritten, then restored) | **CARRIED, INERT** | The served comparison does not rest on it. This seat read the event parts directly (below). |
| `Z-S41` (the scoped API was redeployed between the pair's reader read and the puts) | **CARRIED, INERT** | The reader is not a writer of the moved keys. The close run read the combined state, and this seat reproduced it (below). |

**Served-plane reads by this seat:**
- The chatter_event parts `part-20260929T092439Z` and `part-20260929T192706Z` are byte-identical: both are ETag
  `c146a325c98963f965b8b1bd69ca3393`, 6,457 B (`s3api head-object`, bucket `opal-data-harvest`).
- This seat's re-run of `close_run_round18.py` printed **CLOSE RUN: OK**:
  - ASML_NA, DELL, BA and FDX all returned HTTP 200 from the deployed `/timeline`;
  - each series matched its landed daily on 272 of 272 days, with 0 field mismatches;
  - "events served == newest landed: True" for all 4;
  - BA's one event is "Boeing Delivers 51 Jets in August, Lowest in Four Months".

## 2. L9 -- THE TWO JUDGMENTS

| order | verdict | what the read shows |
|---|---|---|
| **g-1 AC4** (per form, how many of the added hits are the company?) | **MET -- 179 of 179 presented hits are the company, in 52 of 52 form blocks** | This seat read every presented hit in context. The short exact-case tickers the packet names as the adversary all pass: `BA` 10/10 (of 31), `COST` 10/10 (of 19, every one an upper-case "( COST )" or "COST US"), `HD` 9/9, `KO` 5/5, `MU` 3/3. Every whole-brand form is the company: `Dell` 10/10 (of 40), `TJX` 9/9, `Micron` 5/5, `Uber` 5/5, `ASML` 3/3 on each listing, `Spotify` 3/3. The hardest reads are named here. `UBS` 7/7 are the bank, as its analysts. `GS` 1/1 is Goldman's analysts ("GS expects the company to ship"). Micron's "It's not Micron, but it's very simple and very defensive" is the stock, named as a comparison. `Dell` and `Uber` inside a related-articles headline run are the company. **v25's two residual false-hit classes are absent:** there is no `RTX` or `ST` form (refusal list), and 0 parent-brand forms (no Walmart, Coca-Cola or Kimberly-Clark on a subsidiary). The rule's own output therefore reads 100% on this sample, against v25's ~97% prediction. |
| **g-2 AC4** (every NEW or MOVED served event: one story about its own company, led by it?) | **MET -- nothing to grade: 0 new or moved of 8** | The new newest event part is byte-identical to the part served since 09:24Z (ETag above), so no event entered, moved or left. The 11 new or newly tier-A/B mention rows the packet adds are **11 of 11 the right entity**. Only 3 of the 11 are the company as the story's subject: Spotify (narrated articles), TJX in Barron's (its same-store sales), and AMD (in the title, "pressures ... AMD"). The other 8 are list or passing mentions: the ClearBridge position lists (ASML x2 listings, NU), a market wrap (ASML x2, SAP), TJX in a list, and UBS as the analyst on a Costco piece. That is a tier-rule question, not the alias rule's; no event is affected. |

⚠ **Bounds:**
- g-1 was read on the presented sample: 179 of 244 added hits, up to 10 per form, seed 20260929. That is not every hit.
- The 65 unread hits sit in BA (21), Dell (30), COST (9), NVDA (3) and AAPL (2), forms that read 10/10 in sample.
- Unlike v25, every hit here was read by this seat. No subagent made a first pass.

## 3. OBSERVATIONS FOR THE ROUND-18 ANALYSIS (not grades)

1. **ASML's daily status moved for an identifier reason, not a coverage reason.** The close run serves ASML_NA **74 PARTIAL
   days with `publishers_covered=None`**, while DELL, with 40 added whole-brand hits, stays **DENIED on 272 of 272**. Row
   `Z-W45-S2` says why: the whole-brand `ASML` also entered the listing_hit query identifiers, so both listings (74 cells
   each) flipped. A PARTIAL day that names no covered publisher is a status the page will show a PM. The call to make is
   whether whole-brand aliases belong in listing_hit identifiers, and whether both listings of one company should each
   carry the flip. The pair signed the moved cells, so this is a correctness question, not a scope breach.
2. **The whole-brand list and limb (a) disagree on `UBS`** (`Z-W45-S1`). The ruling listed UBS as a whole brand; the limb
   refuses it because a keyless coverage row carries the name. No hit is lost today, since the ticker catches UBS.
3. **Mention rows at tier B are mostly passing mentions:** 8 of 11 new rows are lists, wraps or analyst attributions. Once
   these rows feed an event, they would test the "one story about its own company" rule. Events are unmoved this round.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-S37`, `Z-W39-S1`, `Z-W41-S1` CARRIED as before; the round's 5 new rows are
   INERT. **MET**
3. **Every judgment criterion graded:** 2 of 2 MET. **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S36",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T20:15:00Z",
    "one_line": "L9 round 18: g-1 AC4 MET, 179 of 179 presented added hits are the company over 52 form blocks (no RTX/ST, no parent-brand form); g-2 AC4 MET vacuously, the served event part is byte-identical (ETag c146a325, 6,457 B); close run reproduced OK; ASML flips 74 days to PARTIAL with no covered publisher while DELL stays DENIED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-HVST-g-1 and TO-HVST-g-2 read 'complete' on their LAST <status> tag.",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') 108 items (58 GRADUATED, 25 DISMISSED_WITH_REASON, 25 UNDER_INVESTIGATION) over 30 files; ARMED Z-S37, Z-W39-S1, Z-W41-S1 carried.",
        "g-1: ac4_output.txt read in full by this seat -- 'FORM BLOCKS presented: 52; hits presented: 179 of 244 added hits'; BA 10/10, COST 10/10, HD 9/9, KO 5/5, MU 3/3, Dell 10/10, TJX 9/9, UBS 7/7, GS 1/1.",
        "g-2: s3api head-object opal-data-harvest amgt/harvest/gold/chatter_event/date=2026-09-29/part-20260929T092439Z.parquet and part-20260929T192706Z.parquet both ETag c146a325c98963f965b8b1bd69ca3393, 6457 B.",
        "Close run re-run by this seat: 'CLOSE RUN: OK'; ASML_NA 'served data_status counts: {DENIED: 198, PARTIAL: 74}', 'publishers_covered=None'; DELL '{DENIED: 272}'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The drain-end packet @0994b9332f asserts 2 orders terminal and VALID, the served moves inside the pair, a CLOSE RUN OK, and presents g-1 AC4 (179 hits) and g-2 AC4 (0 new or moved events, 11 new tier-A/B rows) for L9.",
    "world_is": "True as read, with the close run and the event-part identity re-measured by this seat. The rule's output is 179 of 179 correct on the sample. The one served effect that needs a ruling is ASML's DENIED->PARTIAL flip on both listings, produced by the listing_hit identifier path with no covered publisher.",
    "notes": "FOR THE ROUND-18 ANALYSIS: (1) should whole-brand aliases enter listing_hit identifiers, and should both listings of one company carry the flip (Z-W45-S2)? (2) reconcile the whole-brand list with limb (a) on UBS (Z-W45-S1); (3) 8 of 11 new tier-B mention rows are passing mentions, a tier-rule question before they feed events."
  }
]
```
