# ANDREW-DIRECT 2026-10-02 ~17:3xZ -- /ui-walk of Security Analysis, UI/UX briefs: frontend to COO~D, news-scanner backend to COO~H, everything to CTO~Z first

- Channel: the site-Z terminal of `4.0.0_SA_CRO~Z` (session 4e738056-15d5-47b4-a4ac-fe228981a44c), typed by Andrew.
- Time: 2026-10-02 ~17:33Z (13:33 ET).
- Recorded by: `4.0.0_SA_CRO~Z`, in the same turn.

## Verbatim

Andrew: "I wnat you to run a /ui-walk of the "Security Analysis" application on the portal. I think that there are a lot of
opportunities to improve UIUX that need to be addressed. I'll give you a list of things I noticed that i wnt addressed and you
can infer off that basis what other things could be similarly improved. Starting from the top, on the Lead Panel there is some
design disparity where we're using the light card style but superimposing them on the dark card. That is not good design, it
should either stick to the light style unilaterally, e.g. the header section in /philosophy, or go with the standard darker
style, e.g. the header section and chart placement/cards in the header of /advisor-intelligence, a good reference is also the
/book tab layout at L0 drill on /advisor-intelligence page as well because it has a mix of component layouts that may be useful
for illustrating the various functions here. I think the timeline spine is very poorly developed visually; we should be using
whatever our in-pattern library (apex or recharts, i forget) to have a chart element for this. also there should be progressive
disclosure built in whereby you hover over a given date and it just shows some key metrics about the
articles/sources/mention-count/etc in the tool tip. I also think there should be a layer for selecting headlines or earnings
report releases, or whatever was going on at the time of a big spike in the overall spine, so that there is an immediately
visible layer to the spine where you can see what was happening laid out chronologically at key points. Also there is so much
text laid out vertically betwen the "selected date" news and the most current news then sitting beneath that, there is no
distinction visually between the two, probably the recent news should be "above" the timeline spine somewhere. All of this needs
to be better diagrammed out/carded out, so things sit in clear pockets, with easy to read text. If we need more information, the
main feature should be clickable and we get a popup modal with the details laid out in a preexisting modal pattern, e.g. the
topic cloud analyses pop up modal from market overview portal page. Beyond that, in the various chatter/price views, the bubble
view is not displayed well, doing one bubble per security laid out alphabetically requires too much scrolling. I was thinking it
could be more of a collage kind of like how its done in Topic Cloud component where all the bubbles are centered around the
largest one, getting smaller as they go outward, something like that. We also should look into the finbert scoring mechanism for
the current news scanner and probably inflect the same sentiment scoring colorway that is used in Topic Cloud for this. Beyond
that the only mechanism i notice is in "Model", the "what changed" is an interesting thing to see and i think that should be
larger, more of a moment and cleanly viewable with proper design and progressive disclosure and in-pattern fixtures/components.
Please go through and assess all these things, and then also set up a fork or subagent specific to the bubble chart sentiment
scoring pattern for the news scanner because i want COO~H to go get that feature incorporated, also we should have a better
period function than just clicking month/earlier month. I would suggest a rolling 30 day, 90 day, and 365 day view. Please go
and spawn any agents needed to investigate and ui-walk. I want briefs written for frontend work that will go to COO~D, backend
news scanner tie in feature work should go to COO~H. CTO~Z should receive everything first to filter and properly fold in to
their /canonical-flow. Go now."

## Scope as given, no wider

1. A `/ui-walk` of Security Analysis on the local build, plus an assessment of each named item and of similar items inferred
   from them.
2. A dedicated fork or subagent for the bubble-chart sentiment-scoring pattern for the news scanner (FinBERT and the Topic Cloud
   colorway). Its work is for `2.0.0_SA_COO~H` to incorporate.
3. Frontend briefs for `2.0.0_SA_COO~D`. Backend news-scanner tie-in briefs for `2.0.0_SA_COO~H`.
4. **Routing:** everything goes to `1.0.0_SA_CTO~Z` first, to filter and fold into its `/canonical-flow`. This seat sends no
   brief straight to a COO.

## The named items

| # | item |
|---|---|
| N1 | Lead Panel: light cards on a dark card. Use one style throughout: light as in the `/philosophy` header, or the standard dark as in the `/advisor-intelligence` header and chart cards. `/advisor-intelligence` `/book` at L0 is a layout reference. |
| N2 | Timeline spine: replace it with a chart from the in-pattern chart library. |
| N3 | Timeline hover: a tooltip with key metrics (articles, sources, mention count). |
| N4 | Timeline event layer: headlines, earnings releases and what happened at big spikes, laid out chronologically on the spine. |
| N5 | Selected-date news and recent news run together as one long column of text. Separate them visually; recent news probably goes above the spine. |
| N6 | Card everything into clear pockets with easy-to-read text. The main feature is clickable and opens a modal in an existing pattern (the Market Overview topic-cloud analysis modal). |
| N7 | Chatter and price bubble views: one bubble per security, alphabetical, too much scrolling. Use a Topic-Cloud-style collage instead, centred on the largest bubble. |
| N8 | The news scanner's FinBERT sentiment scoring, shown in the Topic Cloud sentiment colorway. |
| N9 | Model "what changed": larger, more of a moment, with progressive disclosure and in-pattern components. |
| N10 | Period: replace month and earlier-month with rolling 30-day, 90-day and 365-day views. |
