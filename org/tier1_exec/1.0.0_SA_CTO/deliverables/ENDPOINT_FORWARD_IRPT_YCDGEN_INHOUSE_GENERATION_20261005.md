# ENDPOINT (step 2, /endpoint --forward) -- IRPT_YCDGEN revision for in-house generation

Author `1.0.0_SA_CTO`, 2026-10-05 ~20:3xZ (4:3x PM Eastern). **STATUS: PROPOSED. NOT YET LANDED in the PRD.** It replaces the
ENDPOINT section of `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` (v0.1, RATIFIED) when Andrew confirms it; PRD
v0.2 follows.

## Brief read

| Input | Vintage | Size |
|---|---|---|
| `docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md` (parent, `4.0.0_SA_CRO`) | @69141b561e | 223 lines |
| `docs/briefs/irpt-ycharts-inhouse-generation-yfinance-probe-20261005.md` (addendum, `4.0.0_SA_CRO`) | @8e50ace95c | 100 lines |
| Andrew's word: "all recs approved, but were out of quota for today on bloomberg + we cant get BQL, so id like to explore if this can be done via yfinance for now" | `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_195xZ_YCDGEN_FIVE_RECS_APPROVED_EXPLORE_YFINANCE.md` | -- |

This is a re-entry on an existing endpoint with a new brief. Ids are permanent: an amended outcome keeps its number, a retired
one leaves its number vacant, a new one takes the next unused number.

## What happened to each v0.1 outcome

| id | v0.1 | v0.2 | Why |
|---|---|---|---|
| FWD-1 | the thread, made from YCharts answers asked for live | **AMENDED in place** | the direction changed: Opal makes the report from data it keeps, with no YCharts call |
| FWD-2 | an analyst reads what any YCharts call gave back | **RETIRED; number vacant** | an in-house run makes no YCharts call. The project no longer promises a look-up of YCharts' answers per run, or the changed-since-last-run flag. Answers already kept stay in the store. FWD-9 carries the need that remains: knowing what went into a figure |
| FWD-3 | every element of the three YCharts reports traced | unchanged | the three maps are the list the in-house report is built against |
| FWD-4 | Comparison and Multi made by Opal's script | unchanged | still right; batch 267's coverage ruling binds it |
| FWD-5 | report and YCharts answers private to the firm | **AMENDED in place** | "YCharts answers" becomes "the data behind it" |
| FWD-6 | a wait at the desk; YCharts' time apart from Opal's | **AMENDED in place** | no YCharts time exists in an in-house run |
| FWD-7 | one-time side-by-side per type | unchanged | it becomes the check before YCharts is retired (FWD-11) |

## The outcomes

```
  FWD-1  Andrew submits one real Cottonwood portfolio for an Overview and opens an Opal-made
         report in the same sitting, with nothing asked of YCharts
         DONE WHEN  EXERCISED -- one live run, ending in Andrew opening the report
         ACCEPT     Andrew, signed in as himself, submits a real Cottonwood portfolio the way he does
                    today and opens an Opal-branded Overview without coming back to it later. Every
                    figure was worked out by Opal from data Opal already keeps. Nothing was asked of
                    YCharts during the run. A figure Opal cannot work out says so on the page, with the
                    reason. A step that used a saved example fails the outcome
         SOURCE     parent section 6, stage 1; addendum section 6

  FWD-2  (retired 2026-10-05; number vacant)

  FWD-3  For each of the three report types, an analyst can point at anything on a YCharts-made
         report and say where it came from
         DONE WHEN  EXERCISED -- an analyst has traced one element of each type
         ACCEPT     unchanged from v0.1
         SOURCE     base brief O2; parent section 3

  FWD-4  An analyst can make the Comparison and Multi reports too, Opal-branded, with Opal's own
         script
         DONE WHEN  EXERCISED -- one of each made and opened
         ACCEPT     unchanged from v0.1
         SOURCE     base brief O3; parent section 6, stage 4

  FWD-5  The Opal-made report and the data behind it are found in Opal's own store, private to the
         client's firm
         DONE WHEN  EXERCISED -- an analyst has found one by its request
         ACCEPT     given a request, an analyst finds its report and the client's own holdings behind
                    it in the client firm's private area. Nobody at another firm can reach them
         SOURCE     base brief O4; parent section 4

  FWD-6  A report run is something Andrew waits for at his desk, and every run shows where its time
         went
         DONE WHEN  EXERCISED -- Andrew has waited for one, and its timing record has been read
         ACCEPT     Andrew asks for a report and has it in the same sitting. The run's record shows how
                    long each stage took: reading the holdings, working out the figures, and making the
                    pages
         SOURCE     parent section 1 item 4, and section 9 ("in-house run time is not measured")

  FWD-7  For the same inputs, an analyst sees which figures on the YCharts report and the Opal report
         agree, and why any differ
         DONE WHEN  EXERCISED -- once for each of the three report types
         ACCEPT     unchanged from v0.1
         SOURCE     base brief O6; parent section 6, stage 6

  FWD-8  Opal keeps the market and fund data the report needs for every security a live client
         holds, refreshed on a schedule, so a report never waits on an outside source
         DONE WHEN  EXERCISED -- a scheduled refresh has run, and a report has been made from what it left
         ACCEPT     for each security in a live client portfolio, Opal has its price history as far back
                    as the report's longest period (or as long as the security has existed), and a
                    description of it: for a stock its sector, country and size; for a fund what it
                    holds, what it costs and when it started. Each carries the date it was true. A
                    security Opal has never seen is fetched once, when a client's file first names it.
                    A report made at any hour reads only what Opal already has
         SOURCE     parent section 5 ("three properties"); addendum sections 3 and 5

  FWD-9  For any figure on an Opal-made report, an analyst can see how it was worked out, from what
         data, and how old that data was
         DONE WHEN  EXERCISED -- an analyst has picked one figure and followed it back
         ACCEPT     an analyst picks any figure and finds the method in words, the holdings it covered
                    and the date of each input. A figure that covers too little of the portfolio, or
                    rests on an input that has gone stale, is printed as not available with the reason,
                    never as a number
         SOURCE     parent section 7 (coverage, stale inputs); RULINGS batch 267

  FWD-10 Returns on the report count dividends
         DONE WHEN  EXERCISED -- one dividend-paying holding checked by hand
         ACCEPT     for one holding that pays dividends, the one-year return on the report equals the
                    price change plus the dividends paid, worked out by hand from the same dates
         SOURCE     parent G1 and section 7, first risk; addendum section 5, last condition

  FWD-11 Everyone who uses the Analysis tab gets the Opal-made report, and Opal stops calling
         YCharts for it
         DONE WHEN  EXERCISED -- an advisor other than Andrew has submitted a portfolio and opened one
         ACCEPT     after the one-time side-by-side of each report type, and on Andrew's word, an
                    advisor who submits a portfolio gets the Opal-made report. No step signs in to
                    YCharts or waits on it. The old way is switched off in the same change, not left
                    running beside the new one
         SOURCE     parent section 6, stage 6; parent section 4 ("contract note")

  FWD-12 An analyst can run the same portfolio again as another report type, or against another
         comparison, without a fresh wait
         DONE WHEN  EXERCISED -- a second run of one portfolio, timed against the first
         ACCEPT     having made one report for a portfolio, an analyst asks for a second with a
                    different comparison or type and gets it at least as quickly as the first, with no
                    limit on how many they ask for
         SOURCE     parent section 1 item 5

  FWD-13 The sector and bond-quality pages show what the client's funds actually hold
         DONE WHEN  EXERCISED -- one fund-heavy portfolio's sector page read against its funds
         ACCEPT     for a portfolio mostly in funds, the sector page adds up each fund's own mix by the
                    fund's share of the portfolio, not one label per fund. Where a fund's mix is not
                    known, as with countries today, the page says so
         SOURCE     parent section 1 item 3 and stage 2; addendum sections 3 and 4

  FWD-14 Opal records each day, from Bloomberg, how the funds its clients hold are spread across
         sectors and countries, so a report as of a past date can be made later
         DONE WHEN  EXERCISED -- two days recorded, and the first day's figures read back on the second
         ACCEPT     for the funds live clients hold, each day's spread is kept under its date and is
                    still there the next day
         SOURCE     parent section 5, "capture starts the clock"; Andrew's card 2 (approved, not started)
```

## Reachability (who owes an act no seat can perform)

- **FWD-14 waits on Bloomberg quota.** Approved, not started; Andrew's own word says today's quota is spent.
- **FWD-11 waits on Andrew's word** to release to advisors, and on FWD-7.
- **FWD-1, FWD-4, FWD-8 to FWD-10, FWD-12, FWD-13** need no Bloomberg call and no new vendor (addendum section 6). They need
  an issuing seat: `2.0.0_SA_COO~Y` is not seated today.
- **Yahoo pulls** stand on card 1 (approved): scoped to the securities in live client portfolios.

## Three calls this endpoint puts to Andrew

1. **Where FWD-1 is submitted.** Recommended: the Analysis tab on the development build, for Andrew's own sign-in, while every
   other user stays on YCharts until FWD-11. One request has one producer; nothing compares the two on a schedule. The
   alternative is a run at a terminal that prints a link, as v0.1 did; it is quicker to reach and proves less of the journey.
2. **Sector names while Yahoo is the source.** Card 3 approved GICS sectors when Bloomberg was the assumed source. Yahoo serves
   the Morningstar-style names for stocks and funds alike. Recommended (the CRO's addendum, section 3): print Yahoo's names,
   say so on the page, and revisit when Bloomberg is the source.
3. **Retiring FWD-2.** Recommended. It is the only outcome this revision drops.

## Provenance

- GROUNDED ON: the two briefs and the Andrew-direct record above, read in full; PRD v0.1 read in full at CLOUD @bcf546c25d;
  `3.0.0_SA_CVO`'s round-5 grade table for the v0.1 outcomes' standing.
- NOT READ: the task-order register, the round-5 decomposition, `project.json`, the handoff from `2.0.0_SA_COO~Y`, the base
  brief of 2026-10-03 (its outcome lines are carried through PRD v0.1), any code, any store object. No vendor was called.
- Every measurement in the SOURCE briefs is `4.0.0_SA_CRO`'s; this seat re-measured none of it.

-- 1.0.0_SA_CTO
