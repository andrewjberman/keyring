# AMGT_HARVST -- ROUND 18 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~20:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26691, READ-acked, subject *"L10 slug AMGT_HARVST round 18 @579b6774ea"*,
which cites `surprise-channel/adjudications/ADJUDICATION_v26.md` (row `Z-C-S36`). Issuer packet: `round18/ROUND18_DRAIN_END_PACKET.md`
@`0994b9332f`.

**Round 18 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **The alias rule is in name detection, and it is served.**
  - `g-1` drained @`a802677065`. `g-2`'s rebuild is served inside the signed pair (COO @`294e28bcbe`, CTO @`9a25d2d5d3`) and
    drained @`8c02ff0b12`.
  - Mention 275 -> 304. Daily: 4,286 ALIAS cells over 50 securities, DRIFT 0. Events are unmoved: the new part is
    byte-identical, ETag `c146a325...`.
- **The rule's own output is 179 of 179 correct** on the CVO's hit-by-hit read (52 of 52 form blocks). That beats round 17's
  ~97% prediction.
  - The adversarial short tickers all pass: `BA` 10/10, `COST` 10/10, `HD` 9/9, `KO` 5/5, `MU` 3/3.
  - No refused form (`RTX`, `ST`) and no parent-brand form appears.
- **The CVO reproduced the close run:** CLOSE RUN OK, 272 of 272 days served equal to landed for ASML_NA, DELL, BA and FDX.

## 2. RULINGS ON THE CVO'S THREE OBSERVATIONS

1. **ASML's DENIED -> PARTIAL flip (`Z-W45-S2`): RULED CORRECT, keep it, on both listings.** The CVO asked whether
   whole-brand aliases belong in the listing_hit identifiers. They do, because the identifier rule mirrors the writer
   (`publication_gold.py:514-536`): a Seeking Alpha row's `search_query` is the vendor symbol the harvester actually queried,
   and every other publisher's row carries the company name.
   - The Seeking Alpha listing rows for "ASML" are that publisher's coverage of ASML. The days they span are covered days, so
     PARTIAL is the TRUE status.
   - DENIED was the missed-join class that row `Z-W22-S3` named ("filed against NO security").
   - DELL stays DENIED because no publisher's listing rows exist for it. That is a real absence, not a missed join.
   - Both listings carry the flip because a publisher covering a company covers each of its listings. The daily status
     describes the company's coverage, not a venue's.
   - **The defect is the other half: the served day cannot say WHO covered it.**
     - Gold stores `publishers_covered` as a count (`publication_gold.py:675`).
     - The served timeline passes `data_status` and omits the count (`timeline_api.py:219`).
     - So a PM reads PARTIAL with no publisher named (the CVO reads `publishers_covered=None`).
   - Cell 1 fixes this.
2. **`UBS` -- the whole-brand list and limb (a) disagree (`Z-W45-S1`): RULED, drop `UBS` from the whole-brand list.** The
   exact-case ticker `UBS` already carries all 7 hits, and all 7 are the bank. The whole-brand entry adds nothing and makes the
   list contradict its own refusal limb. A list the code refuses is a latent failure the next time the limb is tightened. The
   check becomes a test: no list entry is one that limb (a) refuses. Cell 2.
3. **Tier-B passing mentions (8 of 11 new rows are lists, wraps or analyst attributions): NOT a cell.** Events are unmoved.
   The event rule ("one story about its own company, led by it") is the guard that sits between a tier-B row and an event,
   and the CVO grades every new or moved event at L9 (g-2 AC4's form). Carried as an observation. The tier rule is re-read
   the first round a passing mention feeds an event.

## 3. FWD GRADES

- `FWD-5` / `FWD-6`: NOT REALIZED, unchanged.
  - The served half is met and now carries the alias rule.
  - The page half is the timeline panel `92a2576254`. It is still on site-Z portal DEV only, because Andrew's
    *"lets hold on pushes and merges for now"* holds it.
- The other FWDs stand as `ROUND_ANALYSIS.round15.md` left them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 19 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **A PARTIAL day names its publisher** | SERVED, under a never-widen pair, after cell 2. Gold `chatter_daily` gains the covered publisher codes per day beside the existing count. The rule already computes them (`covered` at `publication_gold.py:647`) and keeps only `len()`. The served `/timeline` and `timeline_day` carry both. The rebuild follows round 18's `g-2` form: the expected diff is read from the rule at signing, with ASML_NA/US's 74 PARTIAL days naming `sa` and every other daily cell unmoved. At most 3 mechanical criteria; the page's wording of the publisher is DSGN_AMGTV1's. |
| 2 | **The whole-brand list agrees with its refusal limb** | LOCAL. `UBS` leaves the whole-brand list. A test asserts that no whole-brand entry is refused by limb (a) and that `UBS` hits are unchanged via the exact-case ticker (7 of 7). A dry rebuild prints mention rows unchanged (304) with 0 moved. |

**Fan-out:** 2. Cell 1 depends on cell 2.

**NOT cells:**
- the tier rule for passing mentions (ruling 3);
- a brand-to-parent source;
- the event route (`Z-W39-S1`);
- the portal push (Andrew's hold);
- new held-out reads (the Seeking Alpha 402).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Lift *"lets hold on pushes and merges for now"* for the timeline panel push [a hold set by name].
- The Seeking Alpha subscription (`Z-W37-S4`, HTTP 402) [spend/entitlement].

## Compiler Tools

- The CVO's v26: its hit-by-hit L9 read (179 hits), its `head-object` on both event parts, and its close-run re-run.
- This seat read the listing_hit identifier rule at `publication_gold.py:514-580`, the daily status rule at `:647-676`,
  and the served timeline fields at `timeline_api.py:113, 219, 335`.
