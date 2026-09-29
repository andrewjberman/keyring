# AMGT_HARVST -- ROUND 13 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~06:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26477, READ-acked, subject *"L10 SLUG AMGT_HARVST round 13
@6ab411d537"*, citing `surprise-channel/adjudications/ADJUDICATION_v21.md`. Issuer packet
`deliverables/2.0.0_SA_COO_H/round13/ROUND13_DRAIN_END_PACKET.md` @`93ef8f4966`.

**Round 13 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

**One story per event is served.** The CVO re-ran `ac4_is_each_event_one_story.py` against S3: the newest part
`date=2026-09-29/part-20260929T062617Z` holds 7 events (8 at round 12), and **7 of 7** are one story about their own
company with a lead that names it. BA 08-26 left (its two unrelated stories each fall below the burst bar); NVDA 06-01 is
one event (round 12's under-merge fixed); BA 09-08 kept the deliveries lead, so `Z-S40`'s regression did not ship.

**This is an IN-SAMPLE pass, and this analysis reads it as one.** The rule was tuned in three generations on these same
8 events, and every served event is 2-3 articles on one day. Both halves of the b-2 pair and the CVO say so.

## 2. THE DECISIONS THE SLUG AND THE PACKET HAND ME

1. **The held-out read (the CVO's DECISION; adopted as owed at my b-2 half @`78d6115535`) -- RULED: round 14 cuts it, and
   it spends no new vendor use.** Its population is articles the rule was never tuned on: securities other than BA, 992_HK,
   COST, HD and NVDA, or captures dated after the rule froze (the b-2 put, 06:26Z). The source is only what the harvest
   already holds or what an already-worded capture brings in; no new vendor leg is opened for it. The cell reports:
   (a) the held-out denominator (articles, securities, dates) and the events the rule forms on it, each graded by the
   same JUDGMENT question as b-2 AC4; (b) **the burst-shape census the CVO asked for**: over the whole harvest, does any
   burst exceed 3 articles or 1 day? If none, that shape is reported **UNEXERCISED**, and no held-out pass stands for it.
   (c) If the held-out denominator is 0 at the cut, the cell says so, and the round-13 pass stays marked IN-SAMPLE on
   every surface that cites it; it is never promoted by default.
   A planted fixture of the larger shape (5+ articles over 2+ days) may be run as a MECHANISM test of what the rule does
   with it. It is labelled a fixture and never counts as a held-out grade.
2. **The event route (`Z-W39-S1`) -- NOT CUT.** No FWD needs it: `FWD-6`'s served half is met on `/timeline` and
   `/timeline/day/{date}`. The row stays disarmed by condition: any future cell that wires an event route keys it by the
   stored `event_id`.
3. **`Z-S37` (the `safe-merge` staging window, second instance)** stays with the script's authoring lane. It is not a
   HARVST cell, because this project owns no write surface on `.tools/safe-merge.sh`.

## 3. FWD GRADES

- **`FWD-6` (events as spans on the timeline): NOT REALIZED, served half met.** One story per event is now served. The page
  half is the timeline panel `92a2576254`, on local portal DEV only. Andrew's hold, VERBATIM *"lets hold on pushes and
  merges for now"* (~20:3xZ 09-28, to `0.0.0_AB_MSTR~Z`), is the one thing between it and the walk.
- **`FWD-5`**: the same page-half hold.
- Every other FWD stands as `ROUND_ANALYSIS.round12.md` left it.

**Rule 27's close condition is not met, so this analysis ends in an enrichment list.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 14 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **The held-out read of the one-story rule** (s.2 ruling 1) | LOCAL; reads S3 and the harvest only. MECHANICAL: the held-out denominator printed, and the burst-shape census over the whole harvest with its denominator. JUDGMENT (L9): every held-out event, the b-2 AC4 question. No rebuild and no served move, so no never-widen pair. If the read finds a failing event, the next round ships the fix under a pair, and the pass on the 8 is not re-cited as evidence |

**Fan-out:** 1 cell. **NOT cells:** the event route (s.2 ruling 2); the portal push (Andrew's hold); the Seeking Alpha 402
(`Z-W37-S4`: the account holder's to read); a further bbg diagnostic (its own word).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Read the Seeking Alpha account's subscription state (`Z-W37-S4`, HTTP 402) [his entitlement].
- Lift *"lets hold on pushes and merges for now"* if he wishes the timeline panel pushed [a hold he set by name].

## 6. WHAT THIS ANALYSIS DOES NOT DO

It does not close the project, moves no outcome, and does not re-open the PRD (no ENDPOINT change; `prd-signoff.py status
AMGT_HARVST` reads ADMITTED at v0.3 @`094cc1f110`).

## Compiler Tools

The CVO's S3 re-run of `ac4_is_each_event_one_story.py` (ADJUDICATION_v21) taken as the measurement; the packet's sections
4-7 read to EOF; `prd-signoff.py status AMGT_HARVST` read once.
