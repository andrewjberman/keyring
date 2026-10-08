# ANDREW-DIRECT 2026-10-08 ~18:3x-18:5xZ (4.0.0_SA_CRO~Z terminal, site Z) -- a backfill demand queue project: this seat writes the official brief; site Z's MSTR issues it to DELL1's MSTR for DELL1's CTO; DELL2's CRO supplies the Cottonwood operations analysis

Given in-session at the `4.0.0_SA_CRO~Z` terminal, in two messages.

## His words, VERBATIM AND ENTIRE

First (~18:3xZ):

> "yeah but when we get a row, isnt that a row with fields attached? that is why im saying "cells" as in every row and
> column/field as a single cell, and counting off the basis of cells, so that way we have a more fine tuned view into what
> we know we can get away with. Regardless, there is a lot of backfill that is being required shortly, for the rivalfunds
> ops, for the "Positioning" performance views, for the backfill on ADVI and IRPT surfaces as new clients come in bringing
> in more securities that are summarily classified and ingested. We need to start understanding our demand ops as it
> relates to these surfaces because we may need to start being more clever with how we script these ingestions, truly
> pulling in whatever we actually truly need, and developing our reserves. I want you to look into these processes as I've
> described them, as well as keeping that "cell" logic in mind as you do so, and put together an analysis of what we're
> pulling daily on what jobs and what we pull versus what we actually need, which in some cases can be assessed by looking
> at what component they are going to (which I can help with if you can provide a simple summary with the surface in
> question when you do so;"

Second (~18:5xZ):

> "Yes we are going to need a backfill demand queue project, i am actually asking the DELL2 CRO for this because there are
> multiple layers to it that we need to account for, e.g. resolving securities, whether we go to BBG or YFinance and
> associated methodology per surface, api rate limiting on yfinance and cell limits and management on BBG as well as
> tracking daily jobs that we have to account for as fixed quota utilization, and where that quota is going. This needs to
> be built out into a full project, I would recommend putting as much information as you can on the subject, and CRO on
> the DELL2 box will do the same. I think both of you need to send your findings on the matter, with yours being the more
> official project brief, theirs being more specific to the operations surrounding the COTBKF and related ADVI/IRPT
> surfaecs for Cottonwood. I want you to put that brief together that im asking for here and have your MSTR agent issue it
> to DELL1 MSTR to hand off to DELL1 CTO. Also let your MSTR know to tell DELL1 MSTR that they need to get the analysis from
> CRO on DELL2 to bring in for DELL1 CTO as well, as that project is going to get set up on that box and proceeded."

## What it orders, at the width written

| Item | Owner | Reading |
|---|---|---|
| The unit | all | **A cell is one row x one field.** Demand is counted in cells |
| A demand analysis: what is pulled daily, by job, versus what is needed, with a short summary per surface | `4.0.0_SA_CRO~Z` | Andrew offers to judge need per surface from the summaries |
| **A full project: the backfill demand queue** | set up and driven on **DELL1** | layers he names: resolving securities; BBG or YFinance, and the methodology, per surface; YFinance API rate limits; BBG cell limits and their management; daily jobs counted as fixed quota use, and where that quota goes |
| **The official project brief** | `4.0.0_SA_CRO~Z` | "as much information as you can on the subject" |
| A second analysis, specific to ADVI_COTBKF and the related ADVI/IRPT surfaces for Cottonwood | the CRO on DELL2 | he is asking DELL2's CRO directly |
| Issue the brief | `0.0.0_AB_MSTR~Z` -> DELL1's MSTR -> DELL1's CTO | |
| Tell DELL1's MSTR to obtain DELL2's CRO analysis for DELL1's CTO | `0.0.0_AB_MSTR~Z` | |

## Not said (stated so nothing is read into it)

- No project code is named. Registering one is DELL1's CTO's act at L3.
- Nothing authorises a Bloomberg call, a YFinance call, a backfill, or a change to any running job. The demand analysis
  is read-only.
- He does not say whether the queue manages only Bloomberg and YFinance, or every vendor feed. The brief keeps to the
  two he named and marks the rest as a boundary question.
- He does not set a deadline.

## Acts taken on it, same turn

- Two read-only research agents measuring daily demand and backfill demand; their files feed the brief.
- The brief written to `docs/briefs/`, committed, and sent to `0.0.0_AB_MSTR~Z` with both asks.
