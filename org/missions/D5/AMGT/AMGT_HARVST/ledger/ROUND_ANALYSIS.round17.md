# AMGT_HARVST -- ROUND 17 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~14:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26595, READ-acked, subject *"L10 SLUG AMGT_HARVST round 17 @7b26812023"*,
which cites `surprise-channel/adjudications/ADJUDICATION_v25.md` (row `Z-C-S35`).

**Round 17 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **A security's first burst now survives name detection.** `Z-W40-S1` GRADUATED on the CVO's own runs. On the planted fixture,
  the old rule forms 0 events and the new rule forms 1. The planted two-story control stays at 2 events, so the fix does not
  over-merge. All served events are row-equal on 13 fields, and 0 of 29 securities' name stems change. No served move and no pair
  were needed.
- **The alias census, read hit by hit.** 531 sampled hits across 113 form blocks, 0 UNSURE. For tickers (T1), 172 of 240 hits are
  the company. For short names (B1), 61 of 291 are.

## 2. THE CVO'S DECISION: THE ALIAS RULE

1. **Tickers are admitted case-sensitive, 2 characters or longer, with an explicit refusal list.** A ticker matches only in its
   exact upper-case form. Single-letter tickers (C, F, T, V) never match. The refusal list starts with `RTX` (Nvidia's "RTX"
   products) and `ST` ("ST Telemedia"). On the CVO's exact-case subset this keeps about 157 of 162 hits correct (~97%). That figure
   is arithmetic on a sample of up to 10 hits per form, not a graded census, so round 18 grades the rule again on its own output.
2. **Short names are never derived.** The first-word derivation is dropped as a class (21% correct; `Bank` 0 of 28, `American`
   0 of 20, `United` 0 of 20). A short name enters only from an explicit per-security list of whole-brand names. The list starts
   with the forms measured at 100% on 3 or more hits: `Dell`, `TJX`, `UBS`, `ASML`, `Micron`, `Uber`, `Spotify`. Meta, eBay, SAP
   and QXO wait for a larger sample; they are not in the list.
3. **A subsidiary listing never carries its parent's brand.** `Walmart` for WALMEX* and `Coca-Cola` for KOF are 0 of 18. Such a
   hit is worse than a missed mention, because it gives the parent's coverage to the wrong security. The list refuses any entry
   whose brand is another listed security's brand. That refusal is a check in code, not a note.
4. **Brand-to-parent names ("Google" for Alphabet) stay out.** The estate has no source for them, and this round creates none.
   The whole-brand list is per security and hand-written, and each entry cites the census hits that admitted it.

## 3. FWD GRADES
`FWD-5` / `FWD-6`: NOT REALIZED, unchanged. The served half is met. The page half is the timeline panel `92a2576254`, which is held
by Andrew's *"lets hold on pushes and merges for now"*. The other FWDs stand as `ROUND_ANALYSIS.round15.md` left them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 18 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **The alias rule in name detection** (rulings 1 to 3) | LOCAL. Case-sensitive tickers of 2+ characters with the refusal list; the whole-brand list with its parent-brand refusal. The refusal is exercised by a planted WALMEX*/Walmart entry that must be refused. A dry rebuild over today's silver prints the added mentions per form and per security, with the denominator. JUDGMENT (L9): the CVO reads a printed sample of the added hits per form. |
| 2 | **The served rebuild on the new rule** | SERVED, under a never-widen pair, and after cell 1. The mention, daily and events rebuild as in round 16's `HVST-e-2`. Re-read `Z-W44-S1` on the served events once the new forms land, as the packet asks. |

**Fan-out:** 2 cells; cell 2 depends on cell 1. **NOT cells:** a brand-to-parent source; the event route (`Z-W39-S1`); the portal
push (Andrew's hold); new held-out reads (the Seeking Alpha 402).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)
- Read the Seeking Alpha subscription state (`Z-W37-S4`, HTTP 402) [entitlement].
- Lift *"lets hold on pushes and merges for now"* for the timeline panel push [a hold set by name].

## Compiler Tools
The CVO's L9 read (531 hits, rubric and spot-checks, v25) and its `f-2` fixture and served-arm runs, taken as measurements.
`_latest_dispositions` as the CVO printed it (103 items, 21 UNDER_INVESTIGATION).
