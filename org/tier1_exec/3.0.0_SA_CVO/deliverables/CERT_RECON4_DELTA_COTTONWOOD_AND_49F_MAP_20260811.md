# RULE-14e DELTA-CERTIFICATION -- RECON-4 POST-CERT ADDENDUM (cottonwood re-grade + 49F map path)

**Certifier:** 3.0.0_SA_CVO · **2026-08-11, pass run 0607-0615Z** · **archetype:** VALIDATE
**Subject:** the @314689f20a amendments to `RECON4_GOAL3_JOIN_FEASIBILITY_20260811.md` (post-cert
addendum: cottonwood INGEST-EXISTS-LIVE; 49F verdict cell re-graded RESOLVED-99.8% via
`fact_allocation_account_map`). Extends my base cert @4918e8b48f. Live reads 2026-08-11T06:07-06:14Z.

---

## VERDICT: **CERTIFIED** -- both re-grades confirmed by independent recomputation, with two grain
## corrections on the 49F cell (the headline percentage is map-side, not end-to-end) and one live
## trap documented (the map table's own name-vs-content defect, which bit my own instruments twice).

## COTTONWOOD (ingest exists live, three tiers)

| Claim @314689f20a | My re-derivation (06:07-06:10Z) | Verdict |
|---|---|---|
| bronze `rebalancer_models` 21 / `_model_detail` 561 / `_accounts` 105, newest 08-10 06:00Z, daily meta markers | Measured 22 / 590 / 110, newest **2026-08-11 06:00:43-48Z** -- the daily 06:00Z pull fired BETWEEN the addendum's authoring and my read (+1 day everywhere, `meta/2026-08-11-complete.json` at 06:00:49Z, a conversion marker at 06:00:55Z) | **CONFIRMED at vintage; the +1-day advance is the claim "daily, live" proving itself in real time** |
| silver `fact_model_{roster,definition,assignment,blend}` 21 daily partitions each | 22 each, newest `date=2026-08-11` (same advance) | **CONFIRMED** |
| gold `dim_model_portfolio` 13 objects, newest 08-10 13:00Z | 13 objects exact, newest 2026-08-10T13:00:41Z (today's gold not yet run at read time) | **CONFIRMED exact** |
| `fact_model_assignment` ACCOUNT-GRAIN: 921 rows / 21 cols, `account_number` 921 distinct (len 9 x662 + len 11 x86, digit-rate 0.84), `account_id` 8-digit BD internal, strategy/program/SMA/UMA cols | date=2026-08-10 pulled: **921 rows / 21 cols / 921 distinct** exact; len modes {9: 662, 11: 86} exact, digit-rate 0.845; full tail measured: 173 further entries across len 5-50 (incl. 13 x len-50) -- the claim's two modes are honest, the tail is now on the record; `account_id` len {8: 921} exact; named cols present | **CONFIRMED** (tail characterized) |

The three-generation correction chain (NO-INPUT -> SOURCE-EXISTS -> INGEST-EXISTS-LIVE) ends here:
the at-rest truth is now measured twice independently. Cottonwood's goal-3 question is indeed the
same spine-overlap measurement as the other firms; the follow-up cell (cottonwood ADVI spine
identification + overlap vs `account_number`) remains open as the addendum states.

## 49F MAP PATH (the RESOLVED-99.8% re-grade)

| Quantity | CRO~A claim | My recomputation (map `date=2026-08-10`, feed 2026-08-11, fact_acc date=2026-08-07) | Verdict |
|---|---|---|---|
| Map rows | 7,262 daily | 7,262 exact | CONFIRMED |
| MAP-side match | 5,701 of 5,715 = 99.8% | 5,701 of 5,715 = 99.76% -- **count-exact** (zfill(10) on `account_number` vs `fact_acc.account_id`) | **CONFIRMED** |
| SPINE-side | 5,701 of 7,239 = 78.8% (remainder = accounts in no model, expected asymmetry) | 78.75% exact; asymmetry reading accepted | **CONFIRMED** |
| Residual | "12 nine-digit entries + 2 misses" (=14) | 14 total exact; split measures **3 x len-8 + 11 x len-9** | CONFIRMED total; split corrected |
| **FEED->MAP coverage** | **not claimed anywhere** | **7,220 of 7,230 = 99.86%** (10 feed allocation UUIDs absent from the map) | NEW -- the number the end-to-end claim needed |
| **END-TO-END** | consequence-1 says "end-to-end 99.8%" | **7,205 of 7,230 = 99.65%** (compounds the 10 feed-side + the map-side residual). The 99.8% figure is the MAP-side leg only | **GRAIN CORRECTION: the headline percentage is a leg, not the path.** 25 feed allocations reach no spine account today -- name that denominator in the build TO |

## THE LIVE TRAP, DOCUMENTED (name-vs-content, second instance, and it bit the certifier)

`fact_allocation_account_map` carries the SAME defect class RECON-4 flagged in the feed: its column
NAMED `account_id` holds a 36-char SmartX UUID (5,715 distinct), while `account_number` holds the
digit Schwab number. **My own first two computation passes selected the wrong column** (a
comprehension-order bug, then a reused variable) **and returned a clean-looking 0.0%** -- caught
only because the length-distribution print was beside the percentage (the print-the-frame
discipline doing its job). A builder who joins on the map's `account_id` gets 0% silently. The 2a
field-registry discipline should catch this table; until then the build TO for the 49F join should
name the column pair explicitly (`allocation_id -> account_number -> zfill(10)`).

## What you should have asked but did not (Doctrine §7)

Whether the map is COMPLETE-BY-CONSTRUCTION or complete-by-coincidence: 7,262 rows / 7,262 distinct
allocation_ids TODAY covers 99.86% of TODAY's feed -- but nothing measured says the map's producer
enumerates the same universe as the feed's producer (two SmartX pulls, two schedules, two universes
that happen to overlap at 99.86% this morning). If the map pull scopes by model/rebalancer
membership while the feed scopes by allocation existence, the 10-absent residual GROWS with every
allocation the feed sees first. One source read of the map's puller (its endpoint + filter params
vs the feed's) settles whether 99.86% is an invariant or a coincidence -- worth doing before the
join lands in a serving path.

-- 3.0.0_SA_CVO
