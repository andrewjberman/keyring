# AMGT_HARVST -- ROUND 46 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-05 ~06:1xZ

**Input:** CVO slug msg 29503, `surprise-channel/adjudications/ADJUDICATION_v58.md` @66e10523bb (precondition MET; ARMED 0). The
drain-end packet is `deliverables/2.0.0_SA_COO_H/round46/ROUND46_DRAIN_END_PACKET.md` @e51fb4ddac. It was drained on ruling
@7cd62976f1, with the collection run continuing across the round boundary as signed.

## 1. WHAT THE ROUND DELIVERED

- **as-1:** the collector's universe is the rank's 191 names, each keyed to the pool key: 191 of 191 resolved.
- **as-2:** `chatter_window` over the union: 636 -> 699 rows (233 names x 3), 0 gone, 0 changed. A served write under the pair COO
  @c5b6e09bd1 + CTO @a8f17796de. It cured RESAPP FWD-36 (graded REALIZED at RESAPP round 68).
- **as-3:** the named census picks the served row via `store.supersedes` (row Z-S85 closed).
- **as-1b, THE collection run:** launched 01:44:37Z under COO @30ed1c8b83 + CTO @138b152f2a. Concluded of 191 at the drain (05:46Z):
  sa 4, barrons 0 (queued behind sa), ft 0 (held on Andrew's word), bbg 14, wsj 31. DECLARED SET: EMPTY.

**Round 46 is CLOSED.** The run is the issuer's act under its pair, not a task order, so it continues.

## 2. GRADES AND THE BOARD

- **FWD-17: REALIZED** (re-confirmed): 699 = 233 x 3, tone is null iff voters are 0 on every row, and all 95 RESAPP names are present.
- The collection outcomes are **not gradeable** while the run is in flight. Round 47 grades them from the run's per-leg report, read
  with `publisher_universe_verdicts` (CTO condition 4).

**The board** (latest grade per outcome; rounds 29-46; denominator 17):

| state | outcomes |
|---|---|
| REALIZED (8) | FWD-2, FWD-4, FWD-5, FWD-6, FWD-8, FWD-12, FWD-16, FWD-17 |
| Open, finishing needs NO new collection (0) | -- |
| Open, waiting on THE run (9) | FWD-1, FWD-3, FWD-7, FWD-9, FWD-10, FWD-11, FWD-13, FWD-14, FWD-15 |

8 + 0 + 9 = 17.

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **Row Z-S86:** the sa leg is upload-bound (0.6 pages/min; every small group re-reads the whole sa `listing_hit` prefix); barrons is starved behind it | Ruled @7cd62976f1: the run continues; the batched listing upload is a **round-47 cell**; a separate barrons root is refused. | The cost grows with what is already stored, so sa slows as it runs. |
| 2 | **wsj has spent its 2 auto-resumes** (2 transport errors) | A transport stop on any leg is resumed by the issuer from the leg's OWN checkpoint. That is the same run (condition 1), with no new word and no cell. A concluded job is never re-run. | Condition 1 already covers it; a stopped leg left idle is lost collection time. |
| 3 | **FWD-7 guidance** (Andrew's carried card 5: admit a publisher at 95% or more of 191, with uncovered names shown as not searched) | It stays with Andrew until it is needed: at the round-47 grade, from the per-leg report. If it is still unanswered then, this seat rules on the REC (CTO self-adjudication at L10, as `/open-calls --adjudicate`). | Nothing grades FWD-7 before the run reports, so nothing waits on it now. |

## 4. ENRICHMENT LIST (round 47, ONE issuance by `2.0.0_SA_COO~H`)

1. **The batched listing upload** (ruling 1): one `silver_append` per job's listing batch, or a prefix read cached across groups.
   - Proof: identical silver ROWS on a planted set (only the object count differs), plus a timing control over 100 listing pages,
     old against new.
   - Landing: place `R46_STOP_SA_BARRONS`, land the code, then resume the sa_barrons leg from its OWN checkpoint. No harvest code lands
     while any leg is running, because each job spawns from the working tree. The bbg and wsj legs are stopped and resumed the same
     way for that landing.
2. **The run's per-leg report at the round-47 drain** (condition 4): concluded and stopped jobs by status, out of 191, plus
   `publisher_universe_verdicts` for each publisher.

## 5. ACTS FOR ANDREW (cited)

- **The ft leg:** "Dont attempt FT until I return" (his hold, quoted). ft stays STOPPED.
- **Card 5 (FWD-7 guidance):** his answer is welcome before the round-47 grade, and ruling 3 covers the case where none comes.
