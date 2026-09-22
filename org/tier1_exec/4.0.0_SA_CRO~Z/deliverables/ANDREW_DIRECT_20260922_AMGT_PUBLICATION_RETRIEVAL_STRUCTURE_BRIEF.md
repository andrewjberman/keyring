# Andrew-direct 2026-09-22 -- AMGT_RESAPP publication channels: retrieval, structure, bronze/silver/gold, gold metrics, as a brief

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal, before any act on it. **Channel:** Andrew, direct, in this session.

## Verbatim, entire

> I want you to take a look at the current state of wave 27/28 and what we are trying to do with Lenovo, then I want
> you to take a look at the data fields we have collected for the various ingestion channels. How have we organized
> those fields? I think they should be laid out in there based on what component they feed (e.g. Lead Panel, Exec
> Mgmt, etc) and/or by channel. There should be clear description in that file that covers both the component and the
> channel in either case. with that said, particularly for the news publication channels, we need to figure out how to
> refine the mechanism for picking up news/information. The issue that we're discovering thus far is that when
> searching for the tickers on the various channels, we are picking up literally any time they are mentioned and as a
> result it is much lower signal. There is that aspect, which I'd call aspect #1 "Retrieval", and there is another
> aspect, #2 "Structure". The different news channels may have different structure, i think we have figured out how to
> get clean json from each one, but that has to be verified. If we have clean json for each, that clears out the first
> big Structure challenge. The second challenge is how to collect and organize these things based on timestamp. I am
> not necessarily phased if the articles are low signal as long as the security is mentioned. The more important thing
> is how to categorize the articles based on strength of signal (e.g. how much the security is mentioned in them, is it
> mentioned in headline?, etc) and also by time. The idea is that we should be able to construct a timeline graph of
> all mentions where we can dissect them at any point. This is getting into gold layer logic. Bronze we simply need to
> know what we're getting. Silver we need to make sure that these things are organized in clean queryable format with
> no fidelity loss, just standard typing. Gold is where we start to get into mention count, and other analytical
> factors, which we need to decide. I essentially want you to go through all publication ingestion and figure out the
> bronze silver and gold strategy. I want you to come up with derived metrics that we can incorporate in the gold
> layer. Go now, investigate, come up with the plan, and structure it in a brief.

## Reading, narrow

1. **Asked of this seat:**
   - read the current state of rounds 27/28 and the Lenovo trial;
   - review how the field map organizes channel fields (by component and/or channel, each with a clear description);
   - for EVERY publication ingestion channel: a bronze/silver/gold strategy covering aspect #1 RETRIEVAL and
     aspect #2 STRUCTURE (clean JSON per channel VERIFIED; organisation by timestamp);
   - derived gold metrics, including mention strength (count, headline) and time;
   - all of it as a BRIEF.
2. **His stated tolerances:**
   - low-signal articles are acceptable if the security is mentioned;
   - bronze = know what we get;
   - silver = clean, queryable, no fidelity loss, standard typing;
   - gold = mention count and analytical factors, to be decided.
3. **Not asked:** a vendor call, a pull, a code change or a cut. This seat investigates read-only and writes the brief.
   The L2+ route is `1.0.0_SA_CTO~Z`'s.

## Addendum, minutes later, verbatim

> Also keep in mind, that all of this is going to feed into a gold layer table in harvest which we use to track the
> "Chatter" axis of all these companies. This is how we will be able to get to that analytics layer, it is the base
> for that as well as for company-specific event spine.

**Reading, narrow:** the gold layer is (1) the base table for the Chatter axis across all companies and (2) the base
for a company-specific EVENT SPINE. Both are gold outputs of this plan, and the gold design serves both.

## Addendum 2, after the brief landed (@fefee2f360), verbatim, two messages

> Yes something I would advise regarding how this is handled is by sticking to absolute figures or derived absolute
> figures, never do relative, because relative can be handled in a lambda or some other more ephemeral function

> Also keep in mind how you're going to handle this retroactively considering that the first job is basically going
> to be doing a backfill back to the start of 2026

**Reading, narrow:** (1) gold carries ABSOLUTE figures (counts, sums, timestamps) and figures DERIVED from them by
fixed rules; anything RELATIVE (a ratio against a baseline, a z-score, a min-max normalisation across companies) is
computed at serve time in a Lambda or similar, never stored in gold. (2) The first run is a BACKFILL to 2026-01-01,
so retrieval, silver and gold must work backward in time from a floor, not only forward from a watermark. Both are
folded into the brief (s.3.3, s.6, s.7, new s.6.5) at the next commit.

