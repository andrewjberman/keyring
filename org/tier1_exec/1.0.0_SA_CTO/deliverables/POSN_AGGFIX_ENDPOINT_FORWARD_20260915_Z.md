# POSN_AGGFIX -- ENDPOINT (step 2, /endpoint --forward)

**Author:** `1.0.0_SA_CTO~Z` (spine L2). **Date:** 2026-09-15.
**Status:** CONFIRMED by Andrew-direct ~17:0xZ, record
`ANDREW_DIRECT_20260915_170xZ_POSN_AGGFIX_L2_ANSWERS_DONE_WHEN_D4_FULL_FLOW.md` (this folder). FWD-1, FWD-2, FWD-3,
FWD-4, FWD-6, FWD-7 and FWD-8 are confirmed, with his scoping applied to FWD-1, FWD-3 and FWD-6. FWD-5 is RETIRED on
his word. FWD-9 is written from his D4 answer.
**Two lines differ from the text he answered, and both go back to him:** FWD-2 and FWD-7 were amended at ~17:1xZ,
after he answered, to test an advisor as well as a client (`aa24709901`). His b) "nobody outside Opal sees it" is
the principle both serve. FWD-9's DONE WHEN is this seat's wording of his D4 sentence.
**Lands verbatim** under `## ENDPOINT (step 2, /endpoint --forward)` in
`org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md`: the fenced block only.

**Input:** the plan Andrew designated,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md`, blob `0765b9af1f`, on
origin/CLOUD @ `2033ff3ea6` and on SITEZ since `1e268c164e`.
**L1 brief:** `docs/briefs/posn-aggfix-opal-only-agg-view-brief-20260915.md` @ `1e268c164e` (blob `8a527c8aa0`).
Every `:n` below is a line of the plan blob.

---

## The endpoint

```
ENDPOINT -- POSN_AGGFIX (confirmed by Andrew 2026-09-15)

  FWD-1  Opal staff can view one aggregate book of Opal's primary models on the
         Positioning page
         DONE WHEN  EXERCISED -- an Opal user has opened Positioning, chosen the
                    aggregate, and read both the composition picture and the
                    holdings table for it
         ACCEPT     An Opal staff member opens Positioning, picks the aggregate,
                    and both the composition chart and the holdings table show
                    the combined positions of Opal's primary models and blends of
                    them, as one book for all of Opal.

  FWD-2  Nobody outside Opal sees the aggregate on the page
         DONE WHEN  EXERCISED -- the page has been opened as an advisor and as a
                    client, each including a viewer whose browser remembers the
                    aggregate as its last choice, and no aggregate choice appeared
                    for either
         ACCEPT     An advisor or a client looking for the aggregate cannot find
                    it, and one whose browser remembered it lands on an ordinary
                    model instead.

  FWD-3  Each aggregate holding shows how the models share it, marked as all of Opal
         DONE WHEN  EXERCISED -- an Opal user has read the per-model split on
                    aggregate holdings, laid out as it was before the view was
                    removed, on the page as it looks today
         ACCEPT     For any aggregate holding, an Opal user can read how much of it
                    each model accounts for, in the layout the page used before,
                    plainly marked as all of Opal rather than any advisor's own
                    book, and as easy to read as the columns beside it.

  FWD-4  The aggregate uses Opal's current model mix
         DONE WHEN  EXERCISED -- the aggregate's model mix has been compared with
                    Opal's most recent assets-by-model figures, and they agree
         ACCEPT     The share each model carries in the aggregate matches Opal's
                    latest assets by model, not a mix left over from months ago.

  FWD-6  Every primary model's money counts in the aggregate, blends included
         DONE WHEN  EXERCISED -- the aggregate's inputs have been read: each blend of
                    primary models counts through the models it is split between,
                    nothing outside the primary models and their blends counts,
                    and the per-model figures have been reconciled to Opal's own
                    total
         ACCEPT     No primary model and no blend of primary models is left out of
                    the aggregate, nothing else is let in, and any gap between the
                    per-model figures and Opal's own total is explained, never
                    silently dropped.

  FWD-7  The aggregate figures are not sent to anyone outside Opal
         DONE WHEN  EXERCISED -- what an advisor's and a client's signed-in
                    sessions receive has been read and neither carries the
                    aggregate, while an Opal session still receives it
         ACCEPT     Looking at what an advisor's or a client's browser is given
                    shows nothing about Opal's model mix or Opal's total, while
                    Opal staff still get the aggregate and the page still works
                    for them.

  FWD-8  What clients and advisors already see on Positioning does not change
         DONE WHEN  EXERCISED -- each of the five model views has been compared
                    before and after the change, and they match
         ACCEPT     A client or advisor viewing any of the five models sees the same
                    holdings and weights after the change as before it.

  FWD-9  An Opal user who opens Positioning starts on the aggregate, unless they
         last chose another book
         DONE WHEN  EXERCISED -- Positioning has been opened as an Opal user with no
                    remembered choice and landed on the aggregate, and opened again
                    with a different book remembered and landed on that book
         ACCEPT     An Opal staff member who opens Positioning fresh sees the
                    aggregate first, and one who last looked at a particular model
                    comes back to that model.
```

**FWD-5 is RETIRED and its id stays vacant.** Andrew, e): "no this is irrelevant". The capability no longer promised:
the page does not show which day's figures the aggregate's model mix comes from.

**No outcome above is a wait.** Each is proven by opening the page as a named kind of viewer, by reading what a
session receives, or by reading and comparing figures that already exist.

---

## Per-outcome notes (outside the ratified text)

| Id | Andrew | Source in the plan / brief | Note |
|---|---|---|---|
| FWD-1 | a) yes, "solely ... the primary models or blends of the primary models (e.g. 50/50 ST INT)"; b) "we just need it at global level" | plan :27, :21, :129; brief O1 | Scoped by a) and b): primary models and their blends; one Opal-wide book |
| FWD-2 | b) "nobody outside Opal sees it" | plan :27, :126-128, :133-135; brief O3 | Advisor arm added ~17:1xZ on the brief's finding 1 (portal tiers internal, advisor, client) |
| FWD-3 | c) "how it was before is the right layout" | plan :49-50, :131-132, :86-89; brief O2 | Prior layout is the target; the colours follow today's page |
| FWD-4 | d) "yes of course" | plan :22-23, :74-76, :147-148; brief O4 | Settles D1 as "together" |
| FWD-5 | e) "no this is irrelevant" | plan :150-151 | RETIRED |
| FWD-6 | f) "yes blends count but only of primary models UST ST INT LT ULT" | plan :23-24, :77-79, :109-111, :149; brief O5, O6, F4 | Settles D2 as "fold in", primary blends only. The "explained" bar is the one he confirmed |
| FWD-7 | g) "correct"; b) "nobody outside Opal sees it" | plan :82-85, :158-160; brief O7 | Settles D3 as "move it". Advisor arm added ~17:1xZ; the plan's precedent route refuses clients only |
| FWD-8 | h) "correct" | plan :153-154, :126-128; brief Part III item 4 | Unchanged |
| FWD-9 | "yes this would be the default view when an Opal user goes to Positioning, if they don't have another one cached" | plan :170 (D4) | New at the next unused id |

## Decisions, settled

| Decision | Settled as | By |
|---|---|---|
| s.6 process | the full canonical flow | Andrew 3.) "might as well do it properly" |
| D1 current weights | together with the view | this seat's reading of d); relayed back |
| D2 blends | folded in, blends of primary models only | this seat's reading of f); relayed back |
| D3 aggregate data | kept from anyone outside Opal, not only hidden on screen | this seat's reading of g) with b); relayed back |
| D4 default | the aggregate, unless another book is remembered | Andrew 2.) |

## Out of scope

- The aggregate on Attribution and Factor Tilts (plan :178).
- The AGG bond-fund ticker, which shares the string (plan :179-180).
- A per-advisor aggregate (plan :181-182).
- An aggregate per partner firm. Andrew b): "We don't even necessarily need it to display at the firm level".

## Provenance

```
GROUNDED ON: the plan @2033ff3ea6 (read whole, line-numbered); the L1 brief @1e268c164e (read whole);
             Andrew-direct msgs 23156 and 23176; 4.0.0_SA_CRO~Z msgs 23175 and 23178; portal-proxy.ts
             @edf85ce503 :1405-1435 (the viewer tiers); ruling 5's text
NOT READ:    the task-order register (none exists for this project), portal source beyond the tier
             docstring, the served files, the producer source
```
