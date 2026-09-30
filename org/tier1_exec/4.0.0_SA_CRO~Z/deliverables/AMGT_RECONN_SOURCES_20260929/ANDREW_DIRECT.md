# Andrew-direct: holdings sourcing research

**Author:** 4.0.0_SA_CRO~Z
**Channel:** direct Codex user messages, thread 01a0ede4-6907-7d81-9f8a-089141d6cdf6.
**Recorded:** September 29, 2026, approximately 15:23 ET. Exact receipt times were not exposed in the turn.

## Research instruction, verbatim

> Ok I want to discuss with you how we could develop a lightweight version of this that we progressively build out. The first thing we need to do is figure out a solution where we can get day over day holdings/ETF Composition per each of those tickers, and what is our backfill ability to that end. BBG may do this but I dont remember if we didnt have the necessary entitlements to do so. Another angle would be seeing what data the ETF providers release, and if it can be constructed retroactively over a 2 year period. That is the first research task I need you on, assessing where we would get the information for each of these; if we need bespoke pipelines or if it can just be done via BBG.

## Ticker confirmation, verbatim

In response to the question naming WCMG, GQGU, TSEL, BASG, ETFT and PCLG:

> Yes those are all correct

## Scope clarification, verbatim

> Yeah if they have less than 2Y of history, then we just get as much as we can up to that threshold. Also, if BQL is really just for all the "characteristics", and we can get holdings data every day just no beta/etc., that is fine. Most of that stuff can be derived after the fact if we really need it based on the holdings. All we need is daily holdings. If all we can get is weekly, fine, if all we can get is quarterly, less good, but fine.

The paired assessment records the live read-only Bloomberg probes, issuer-source retrievals, available historical examples and proposed lightweight collection approach. No other seat was dispatched.

## Bloomberg documentation follow-up, verbatim

Recorded September 29, 2026, 15:36 ET, direct Codex user channel. Receipt timestamps were not exposed.

> Ok Im interested. First of all, are you saying there might be another BBG endpoint that we can go around for this purpose?

> Check these out: "C:\Users\Opal Bloomberg\Downloads\BLPAPI-Core-User-Guide.pdf" "C:\Users\Opal Bloomberg\Downloads\BLPAPI-Core-Developer-Guide.pdf", they are docs on BBG API, maybe a clue in here

The follow-up is recorded in `BBG_GUIDES_FOLLOWUP.md`; it covers document review and read-only live API tests, with no account configuration changes or external correspondence.

## Option 1 selected, verbatim

Recorded September 29, 2026, approximately 16:03 ET; direct Codex user channel, receipt timestamp not exposed.

> Go on option 1 to start.

The selected next-calls option was to check remaining Terminal/Excel and portfolio-ID possibilities in one bounded research session, ending with a demonstrated full-holdings route or a precise support question. `BBG_EXCEL_ACCESS_VERIFIED.md` records the successful Excel route and remaining limitations. No support message, build dispatch, purchase or production schedule change was authorized or performed.

## Historical granularity question, verbatim

Recorded September 29, 2026, approximately 16:48 ET; direct Codex user channel, receipt timestamp not exposed.

> Just went through this, my question is, what granularity of dates do we have for these? Can it be retrieved daily every single day back to the start date or what?

`DAILY_COVERAGE_CENSUS.md` answers from a complete trading-date scan of the established sources, distinguishing dated source reports from Bloomberg's carried-forward responses. No production collector was installed.

## L1 brief direction, verbatim

Recorded September 29, 2026, during the approximately 17:32–17:46 ET research/brief session; direct Codex user channel, exact receipt timestamp not exposed.

> Ok i think we have enough to $brief-create now. Here are the main points: 1.) We need bronze/silver/gold structure within opal-data-etfs set up, bronze raw csv or whatever we can get daily holdings with as much info as is available, silver is typed parquet, gold first foundational table being the "Canonical Shape", where we level everything out to one Opal-defined format for all tickers/channels. 2.) We need to create a BBG daily script that gets tagged onto the morning run and a lambda script that pulls daily from the issuer sites. This can actually be tested now because if the issuer sites post daily and we only need BBG for the backfill, then it is much preferable to not needlessly use quota on BBG; that should be explored and rec be featured in brief if feasible. 3.) We need to spec out some Gold Tables and AI analysis prompts for said tables. I think the "Canonical Shape" table should effectively be a denormalized base table with all info that we'd want. Every holding, every subasset class and GICS industry tag in fields, anything we can get, put it all in there. Then we make downstream gold tables maybe per ETF that cover top 10 performer bottom 10 performer weights and summary sector delta day over day, stuff like that so that we can then give a prompt to the AI to reverse engineer their trading behavior, tilts, etc. in order to ultimately derive summary outputs that cover where they were really right where they were wrong, what trends we're seeing in their trading in order to predict where they're going based off past trades/activity (projecting trends outward in their holdings), and so on.

## LGIC naming constraint, verbatim

Same active brief session, direct Codex user channel; exact receipt timestamp not exposed.

> Yes also keep in mind that you should be following LGIC NAMING standards for all of this

Carried into `docs/briefs/etf-holdings-research-20260929.md` and this folder's `GOLD_TABLES_AND_PROMPTS.md`. The brief uses the actual LGIC registry and grader, records the measured bronze/silver placement-builder mismatch with the explicit bucket direction, and does not treat existing legacy prefixes as the standard. This invocation authors the brief and supporting design; it does not dispatch or deploy production work.

## Client assets versus outside research, verbatim

Recorded September 29, 2026, approximately 20:59 ET (September 30, 00:59 UTC); direct Codex user channel, exact receipt timestamp not exposed.

> only client assets go through that route to opal-data-assets. outside research, public info, etc (e.g. opal-data-harvest, opal-data-transcript, etc) are managed in their own buckets.

This reaffirms the existing R4 in `infra/logic/02_DOCTRINE.md`, read during this correction. The brief and supporting specification now explicitly identify `opal-data-etfs` bronze/silver/gold as the existing policy's application to outside ETF research. The observed builder output is an implementation/placement-metadata mismatch, not a new policy exception or an open decision. No global registry edit, production migration or peer dispatch was performed for this correction.

## Six-step build order and gap pass, verbatim

Recorded September 29, 2026, approximately 23:2x ET (September 30, 03:2x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed.

> Let's just do a pass on the current state of the brief and any associated evidence and make sure that there are no holes in any processes here. The way I see it, there are the following steps that have to be executed essentially in this order. 1.) Bucket structure createdin opal-data-etfs with bronze/silver folders for bloomberg and issuers respectively, as I expect they will be in different shapes. Gold folder will be unified shape that can accrue from either channel. 2.) Backfill from Bloomberg pulled ad hoc per ETF into bronze. 3.) lambda designed to activate on bronze ingestion completion to type/dedup silver parquets. 4.) lambda designed to activate on silver completion that runs gold foundational shape + any other gold tables. 5.) Lambda runs at completion to generate presentation worksheet with relevant chart views and AI analyses, probably hosted on mcp.opalinvest.dev/activefunds (can borrow a lot for this from /daily-sprint cloud process). 6.) Schedules set up for daily csv ingestion and parsing that goes to the issuer bronze/silver folder path. Bloomberg exists as backup retry if issuer fails. These run daily.

Step 5 (a hosted presentation page with AI analyses) is new relative to the brief, whose O1 said a dashboard was not required. The gap pass is reported in-session; no brief text, build or dispatch was changed by this record.

## Rulings on the 14-item gap pass, verbatim

Recorded September 29, 2026, approximately 23:4x ET (September 30, 03:4x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed. Numbers answer the gap-pass items in order.

> 1.) This is a separate function, the lambda you list is for a different purpose; conflating the two would be messy. this should be etfs-rivalfunds-daily, that makes it extra clear what it is. 2.) That naming tool needs to be adjusted, that should only apply for client assets and this is not a client assets issue. I believe that fix is already in production in the cloud; it should be how buckets like opal-data-harvest have been allowed to operate. 3.) That's fine, you can propose a solution to that which I will review. 4.) No that is not how it would work. What would be more logical is a platinum folder in opal-data-etfs that has the served files archived by day. Look at how mcp.opalinvest.dev/sprint/archive does it, where are those stored? I would use a similar pattern. Lastly, regarding the new gateway route, that's fine, let's use /rivalfunds though to keep up with the lambda title as i think its a more unique and specific token. We definitely can use OpenAI on this; OpenAI relationship with BBG is entirely out of our scope. Moving onto 5.) Ok go with your recommendation on how to structure this, i was not being 100% literal, just largely being chronological in terms of getting this off the ground in short time without a ton of process overhead and bullshit. 6.) Trigger on batch complete works. 7.) Great point, have to ad hoc those then from the outset. 8.) That is a good point, I am ok with using canonical flow process instead, I just made these comments to be very explicit about nonnegotiable steps that need to happen so that the agents responsible dont have a giant hole and forget that there needs to be a served output, or forget to bridge silver and gold, etc. as this happens when one is not specific in planning sometimes. 9.) Ok then we do the issuer at 7a ET and BBG has a fallback opportunity for ETFs that do appear on BBG at that 8:03 time. 10.) There should be guardrails to check on that pre-publishing. 11.) Yes that has to be done. 12.) This will require some testing over a few days, not a big deal. 13.) I am fine with using BBG for this. May be a good time to look into AMGT_HARVST and how all the resolutions worked there. 14.) Didnt think it would, we expect them to be different in bronze/silver, thats why there is a gold accrual table that coalesces the various shapes into one master shape.

OpenAI use for the analyses is authorized by this word. The ruling on item 3 asks for a proposal Andrew reviews; it is not a ruling on the trigger design itself.

## S9 approved, registry row, CTO handoff, verbatim

Recorded September 30, 2026, approximately 00:0x ET (04:0x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed.

> S9 looks fine, add the registry row and send to CTO

This approves the S9 trigger-chain proposal and pre-publish guardrails in `GOLD_TABLES_AND_PROMPTS.md` revision 2, authorizes the `rivalfunds` scope row in `infra/logic/registry/scopes.json`, and directs the brief to 1.0.0_SA_CTO for L2.

`python lib/opal_naming.py validate` refused the `rivalfunds` scope row (*"'opal-data-etfs': a data bucket is opal-data-{scope}, LONG form"*); the row was reverted uncommitted. Andrew's answer, same session, verbatim:

> no that is ok , we can use etfs scope

Landed accordingly: the `etfs` scope moves to GENERAL tenancy, and a `rivalfunds` system key is the source of the derived tiers (validate 0 refusals; generated targets content-identical).

## Project name, verbatim

Recorded September 30, 2026, approximately 00:2x ET (04:2x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9. Exact receipt timestamp not exposed.

> I like it, lets call this ETFS_RIVALS

The project code is `ETFS_RIVALS`. Registering it (L3) is 1.0.0_SA_CTO's; this seat records the name and relays it. The product and resource token stays `rivalfunds` (`etfs-rivalfunds-daily`, `/rivalfunds`); a project code is never a system token.

## Trade schedule as the foundation of the analysis, verbatim

Recorded September 30, 2026, approximately 00:3x ET (04:3x UTC); Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, in reply to the CTO's nine-outcome endpoint. Exact receipt timestamp not exposed.

> Yeah this is pretty good but i have one idea that may be foundatinal for the AI Analysis. We need to reverse engineer their actual trades. What I'm thinking is, if we have their changing values at market close each day, and we also track all the performance of the individual securities every single day, cross-referencing that with the portfolios, couldn't we assess more or less when and where they made trades (i say approximately because not sure how well cash is tracked)? If we can engineer a shape for this, then we can have a gold table for each active etf that is effectively their trade schedule. THe premise here is that the whole point of doing this is not to throw a huge amont of data at research team; that is useless. It is to get one really, really clear signal on competitive intelligence and reverse engineering the other funds processes and activity.

The DONE WHEN lines are not yet confirmed by this word ("pretty good but"). Feasibility measured the same hour: `TRADE_INFERENCE_FEASIBILITY.md`.

## Trade floor and dividends, verbatim

Recorded September 30, 2026, approximately 00:2x-00:3x ET; Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, three consecutive messages. Exact receipt timestamps not exposed.

> Trades can be 0.2% or more, not 0.5%.

> Also probably need to account for dividends on thes

> bbg should have dividend calendar for the holdings

Applied: the trade floor is 0.2% of prior shares (probe re-run; `TRADE_INFERENCE_FEASIBILITY.md`), and dividends enter the method from Bloomberg's per-holding dividend calendar (S6).

## 0.2% confirmed, verbatim

Recorded September 30, 2026, approximately 00:4x ET; Claude Code terminal, `4.0.0_SA_CRO~Z` session a3a51db9, after the 0.2% / 0.5% comparison. Exact receipt timestamp not exposed.

> ok stick with 0.2%, send it to CTO when committed

Already in force: rev 3 committed at 2a1f275a78 with the 0.2% floor, sent to 1.0.0_SA_CTO~Z (msg 26910), and the endpoint amended at 33c1d096a3 (msg 26913).
