# ANDREW-DIRECT 2026-09-30 ~06:xxZ -- client reporting dashboard: two briefs, scope answers

**Channel:** Andrew at the 4.0.0_SA_CRO terminal (laptop). Recorded by 4.0.0_SA_CRO the same turn. Two messages.

## Verbatim

Message 1 (the request, with four screenshots of a Black Diamond client dashboard: net worth, activity summary, transactions):

> Yes what I need from you is a brief that effectively develops an incredibly high quality reporting dashboard for the client. I don't think we need to exactly recreate the Black Diamond dashboard, because it sucks, its not good. But, there are a few things that would be nice, and that means you need to figure out the backend we need to put together in order to allow for that. I will give you a list of things i want, and then you have to figure out how we have to structure tables from assets/holdings to be able to track day over day performance with ease at low latency at load time. So in addition to the obvious time series and custom bookended performance views, we want to be able to demonstrate performance across various asset classes, we want to be able to demonstrate period over period views of how asset allocation has changed (asset allocation relying on Opal canonical ETF-Classifier asset classes), we want to be able to show unrealized gain + realized gain over the given period, we want to show net worth (includes deposits/withdrawals) [Image #2] as well as an activity summary view [Image #4] which feels like theyd be included in the same component maybe activity summary default loads and you hit a toggle to see networth or something, we should be able to show transactions [Image #3], and lastly i think what would be most interesting is figuring out some way to show a view that shows the news stories/word cloud of what was trending at key points in the given view, e.g. wherever the biggest drawdown is should absolutely have a snapshot of the topic cloud phrases from the period (this is a feature cottonwood really wanted, and i think it would be very cool to be able to work in here as a signature view). Accordingly, i think this is really two briefs, one of them is a backend brief on what needs to be done to effectively coopt what we already have in opal-data-assets and how that needs to be shaped in gold to provide these views (gold should be an Opal shape, all firm-specific shapes should be adapted into one gold shape for these functions). So all the engineering and pipeline work is one brief, but on the other side there is a brief for the frontend stuff I was describing and how that ties into that backend work. The idea would be that we would essentially set off two COOs at once, COO~P on the backend and bucketing and COO~D on the frontend, so we could run this whole function in concert.

Message 2 (answering this seat's data-gap table and its three decisions):

> 1.) Cottonwood will eventually have Black Diamond backfill their data. We just have to get the shape right and one day it will just click. 2.) Some agents should be sent to go looking for this, we have an entire API Swagger doc for Orion (Inflection) that surely could point this out. In the case of Black Diamond, we did do a whole DATA_PLATFORM sweep and maybe found the relevant endpoint in there. 3.) Net worth is not needed, i already dont care about it, scratch it. 4.) Account level is all that matters, I don't mind aggregating for household/client level, should not be a big leap. 5.) Performance needs to be total return, we need to figure out how to manage dividends and whatever else goes into total return. Moving on now to your three decisions that shape the briefs: 1.) 49 Financial should be the first. 2.) They will come out with it at some point on BD. 3.) Forget this view.

## Effect (this seat's reading; scope not widened)
1. Two briefs, one backend (COO~P: gold shape, pipelines, bucketing) and one frontend (COO~D), to run in concert. The seating is the CTO's and the COO's; this seat writes the briefs.
2. Views in scope: time series and custom start-and-end performance; performance by asset class (canonical ETF-Classifier classes); period-over-period allocation change; realized and unrealized gain over a period; activity summary; transactions; the topic-cloud snapshot at key points (biggest drawdown) as the signature view.
3. NET WORTH IS OUT (the net-worth view, held-away accounts, liabilities): "scratch it", "forget this view". The activity summary stays; it does not toggle to a net-worth view.
4. Account grain is what matters; household and client levels are aggregates built from it.
5. Performance is TOTAL RETURN: how dividends and other income enter it is a design question the brief must settle.
6. 49 Financial is built first; Cottonwood follows with its Black Diamond backfill arriving later, so the shape must be firm-agnostic and get right now. Inflection's Orion API and Black Diamond's endpoints are to be searched for the missing lot, cost-basis and transaction feeds (agents sent).

## Addendum (~07:0xZ) -- Message 3, the gold layer is always the Opal shape

> Yes again I want to make the point that when we have these data pipelines, the gold layer is always the opal shape. that means that whatever these various firms shapes are, that is fine for bronze in raw form, that is fine in silver in typed deduplicated parquet, but gold is the adapter layer, thats when we take opal shape and everything has to be coalesced into that. Just want to make that extra clear as you're going through the plumbing on the subject.

Effect (this seat's reading): a standing rule for both dashboard briefs and the commentary work. Bronze holds each source's raw shape; silver holds it typed and de-duplicated in parquet, still in the source's own shape; GOLD is the adapter layer, where every firm's shape is coalesced into ONE Opal shape. Firm-specific columns do not survive into gold; where a firm lacks a field, gold carries it as null with a coverage marker, not as a firm-specific variant of the table.

## Addendum 2 (~07:1xZ) -- Messages 4-5, total return: conservative GIPS methodology, cash-receipt income, gross of fees, a fee rail for later

This seat had recommended: total return = price return plus income, external flows still ignored (per Andrew-direct 2026-09-28 "cash movements should not matter at all"). Rulings requested: 1 basis, 2 income timing, 3 fees and labels.

Message 4:

> 1.) I'd say External flows do matter insofar as they change the weighting of a portfolio. My issue with this is that Im trying to structure this in a way where we avoid flows having hyperexaggerated effects on performance. I want to use a conservative, GIPS methodology. I think you can probably fill in the rest, no need to reinvent the wheel here. 2.) Yes yor recommendation is right. 3.) Yes gross of fees is correct, we're not dealing with these fuckers fees because we don' tknow their fee methodology.

Message 5:

> There should be a "rail" for fees, which we can employ later once we have a proper field set up to manage that

Effect (this seat's reading; scope not widened):
1. The basis is TOTAL RETURN on a conservative GIPS methodology: external flows DO enter (they change the portfolio's weighting) but under GIPS-style rules that keep a flow from distorting the return; income counts. This supersedes this seat's "flows ignored" recommendation and narrows the 2026-09-28 holdings-only ruling: flows re-enter as a weighting input, not as a return. The detailed rules are this seat's to fill in from GIPS; the CTO records the change to the endpoint.
2. Income is recognised when the cash is received (cash-receipt), as recommended.
3. Returns are GROSS of fees, and labelled so. A fee RAIL is designed in now (a place and a field set for advisory fees) and left unused until a proper fee field exists, because the custodians' fee methodology is unknown.

