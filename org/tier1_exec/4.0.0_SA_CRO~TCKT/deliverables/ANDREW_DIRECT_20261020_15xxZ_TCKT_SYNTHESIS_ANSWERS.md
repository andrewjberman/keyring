# ANDREW_DIRECT 2026-10-20 ~15:xxZ -- answers to the CRO's synthesis of his walkthrough memo; "let's get started"

Channel: Claude Code session, seat 4.0.0_SA_CRO~TCKT (box dell2), typed by Andrew in reply to this seat's synthesis of
`ANDREW_DIRECT_20261020_14xxZ_TCKT_WALKTHROUGH_VOICE_MEMO.md` (@9de85135f0). The numbers 1-9 answer the synthesis's
section-1 table rows 1-9; "Section 2" and "Section 3" are the synthesis's back-end gaps and decisions.

Verbatim:

> 1.) Service Request is the catchall default, that is fine to have as an option if the request doesn't fit into
> analysis/trade/meeting. Any usertype has access to all request types, regardless what firm they are associated with.
> 2.) Yes, it is redundant to have to retype this. The only case where it makes sense to write the Advisor name is if
> the advisor who is filing the request is not the advisor presenting. What I would do is have a field where the
> advisor types their name, it defaults to the advisor filing the request, but it can be edited. In essence it
> pre-fills the requesting user but that can be changed. 3.) Yes. 4.) Yes. 5.) Yes. 6.) Yes. 7.) Yes, no need to
> reference variants, its implicit. Also Add Commentary does not need to be included as a selection box, we add
> commentary every single time, that is not a selection. 8.) Yes. 9.) The current state is fine, we dont need to change
> from how it operates currently that was my misunderstanding. Moving on from here to the BackEnd comments in your
> Section 2, the agent-built one on October 3 is likely fine, I just need to see that export in a sample run to gauge
> whether it looks correct and has the right information. We almost certainly do not need to refer to Alyssa's as I'm
> sure anything that the agents built is good to go. Let's now move on to Section 3, Decisions you need from me. We can
> start with Core to get a functioning chart out, but as soon as we get that done, the build for the full parity
> version should get started. Regarding Alyssa's script, not needed, what we do will be better, the more important part
> is that we have the sample y charts output so you can see what they provide ive attached one here
> "C:\Users\Test\Downloads\Hinton - Comprehensive Overview (No Benchmark) - 2026-09-16.pdf". I believe we just have an
> analysis-report folder in each firm's bucket that these get dropped off within, using lgic naming standards of
> course. Gate field almost certainly was date field typo. I agree with your positioning let's get started.

## The rulings, as this seat reads them (his words above govern)

| Item | Ruling |
|---|---|
| Request types | Service Request stays as the catch-all option. Every user type, at any firm, may file every request type. |
| Advisor name | One field, PRE-FILLED with the filing user's name, editable (the filer may not be the presenting advisor). Export attribution only; never authorization. |
| Date field | Removed (the "gate field" in the memo was the date field). |
| Other ETFs | Type a ticker, press Enter, it becomes a chip; no comma entry. |
| Household, Title | Stay required. |
| Variant | Never referenced on any screen or attachment; implicit from the comparables. |
| Commentary | Always produced; never a selection anywhere (form or Form-as-filled). |
| Confirmation | Always shown after filing, with the request id. |
| Ticket status | NO CHANGE: the current open / claim / in progress / complete behaviour stands. |
| Opal report | The agent-built generator (10-03) is the base; Alyssa's script is not needed. Andrew must see an Opal export from a sample run to judge it. |
| Comparison / Multi-Comp | Core first (a functioning comparison chart and figures); the full-parity build starts as soon as Core is done. |
| Reference output | The YCharts sample at `C:\Users\Test\Downloads\Hinton - Comprehensive Overview (No Benchmark) - 2026-09-16.pdf` (client document; read locally, never committed). |
| Audit record | Lands in an analysis-report folder in each firm's bucket, LGIC-named. Retention: not stated. |
| Execution | "I agree with your positioning let's get started": the front-end set plus the swap wiring and the audit record go in one closer pass; the report engine (Core then parity) is briefed separately to its owner. |
