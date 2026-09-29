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
