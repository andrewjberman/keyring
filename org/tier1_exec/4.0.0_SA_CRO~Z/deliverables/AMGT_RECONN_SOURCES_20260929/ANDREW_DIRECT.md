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
