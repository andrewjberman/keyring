# ANDREW-DIRECT 2026-08-21 ~14:1xZ — ETFS_POSITIONING: formalize + execute END TO END; daily Bloomberg pull in addition to the existing morning pull

**Channel:** direct at the base `1.0.0_SA_CTO` terminal, 2026-08-21 ~14:1xZ (mid-session, after the
LD-0429 chain close). Recorded same turn per the record+broadcast law. VERBATIM:

> "I also want you to check what CTO~A was briefing/logging last night and let's get this ETFs work
> sorted. MSTR~Z i believe also had a brief they put together that covered the shape of the data in
> bloomberg and updates to the script so we can start pulling all that in from there daily in
> addition to the existing morning pull. We put a handful of stuff in opal-data-etfs, i believe in a
> subfolder called bbgpull-test or something like that. I want to get that project / directive
> formalized and executed end to end, so let's get that registered as needed if it's not done
> already, PRD adjusted to the reality of the bbgpull-test data shape and so on if not already, and
> let's get that show on the roadl"

## What his word does (operative readings, stated so they can be corrected in one word)

1. **BUILD IS AUTHORIZED, END TO END.** The PRD's standing "BUILD NOT AUTHORIZED" (research fence,
   CTO~A v0.1) is lifted by this instruction. The execution plan is PRD s.10.5.
2. **THE DAILY BLOOMBERG PULL IS EXPLICITLY ORDERED** — "pulling all that in from there daily in
   addition to the existing morning pull." Grounded referents: "there" = Bloomberg (site-Z terminal
   box); "the existing morning pull" = the `OPAL_BBGTML_daily_pull` scheduled task (07:00 local,
   `scheduled_daily_pull.cmd`, tplus1 models pipeline); "all that" = the ETF positioning data the
   bbg-testpull proved (characteristics + history + fund daily series). This is his explicit
   per-use word for the recurring Bloomberg egress on the site-Z box.
3. **Registration/PRD asks are CONFIRM-AND-REFRESH, not green-field** — `ETFS_POSITIONING` is
   registered (@e0c7276d00), is D4's member project, and the PRD exists; what his word requires is
   the reality-adjustment to the delivered pull (PRD s.10) and the register event-refresh (MSTR).
4. **NOT adjudicated wider:** this word does not by itself extend the TrueShares one-time egress
   (2026-07-31, @cfdddb5d8d) to a STANDING daily sheet pull — that is a distinct vendor-egress act
   and the per-use law wants his explicit word. Carded back to him same turn as the one open
   confirm, with the capture-forward urgency stated (the sheet is current-day-only; every
   uncaptured day is permanently lost).

**Actor bindings this session:** base CTO records + amends PRD/JSON + cuts the site-Z work order
(agentbus, spec inline per the CTO~A precedent); MSTR owns the DIRECTIVES.yaml D4 event-refresh +
push window; COO owns the D4_ETFPOS TO re-grounds (spec routed, seat dark, queued); MSTR~Z executes
the daily-pull productionization on the defined deliverable.
