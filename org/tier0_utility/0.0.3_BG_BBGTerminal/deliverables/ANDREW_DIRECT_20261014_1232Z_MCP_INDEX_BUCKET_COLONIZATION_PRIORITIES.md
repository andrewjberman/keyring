# ANDREW-DIRECT 2026-10-14T12:32:18.803Z -- MCP index: bucket colonization priorities

**Channel:** Microsoft Teams, 1:1 Andrew Berman <-> Opal Bloomberg
(`19:2e21f8e5-55ca-45c1-91b9-a4607bf28d4f_517aa5ee-b4d0-425a-b493-5a22ff77ac4f@unq.gbl.spaces`).
**Time:** `2026-10-14T12:32:18.803Z`. **Msg id:** `1791981138803`. **Sender:** `Andrew@opalinvest.com`
(his own account, confirmed on the message's `sender_upn`).
**Recorded by:** `0.0.3_BG_BBGTerminal`, same turn as reading it, per `org/XXX.md`.
**Acked in-thread:** `2026-10-14T13:58:24.552Z` (msg `1791986304552`).
**Voice-dictated**, so it carries transcription artefacts: "Opal Indest" = Opal Invest,
"MCP.oponevest.dev" = mcp.opalinvest.dev, "Acuzu" = Kuzu, "comp witch" = `comp-which`,
"Y charts"/"why charts" = YCharts, "smart X" = SmartX. **The artefacts are left IN the quote below and
corrected only here**, because the phrasing is the ruling and I will not silently normalise it.

## ⛔ UNRESOLVED BEFORE ANYONE ACTS: a "Disregard this" 32 seconds later, from the WRONG ACCOUNT

| clock | msg id | sender (`sender_upn`) | body |
|---|---|---|---|
| 12:32:18.803Z | `1791981138803` | **Andrew@opalinvest.com** | the directive quoted below |
| **12:32:50.005Z** | `1791981170005` | **opalbloomberg@opalinvest.com** | **"Disregard this"** |
| 13:58:24.552Z | `1791986304552` | opalbloomberg@opalinvest.com | my ack (sent before I had read either) |

**"Disregard this" came from THIS SEAT'S OWN ACCOUNT, 32 seconds after his directive, and this session
did not send it.** Every send this session made is accounted for in the thread (19:45:08, 20:08:52,
20:11:14, 20:13:21, 20:16:44 on 10-13, and 13:58:24 today); that message is none of them.

**Two readings, and they lead to opposite work:**
1. Andrew typed it himself from the Opal Bloomberg account -- he is at this terminal and the
   credential is reachable to him -- meaning *"disregard the message I just sent"*, probably because
   the dictation transcribed badly. **The directive is then WITHDRAWN.**
2. It refers to something else, or came from another holder of this account. **The directive then
   STANDS.**

**I am not choosing between them.** Timing favours (1) strongly, but a 32-second gap is inference, not
measurement, and the cost of guessing wrong is symmetric and large: build a multi-bucket tooling
programme nobody wants, or drop a major directive. **Asked in-thread; this record exists either way,
and if it is withdrawn this section is why the file is still here.**

**Separately and smaller: a send from this seat's account that this session did not make is an
identity fact worth recording** regardless of who did it. Not raised as an alarm -- the mundane
explanation is almost certainly right -- but `prompt.md` makes this seat's identity binding
load-bearing, so the observation is logged rather than assumed away.

## VERBATIM

> So the purpose of this message is to focus on our MCP index, specifically what tools we have
> available that hit what endpoints and or tables in AWS, to provide data access and functionalities,
> workflows of all kinds, to the Opal Indest employee team. Now, I've gone through the
> MCP.oponevest.dev slash gateway list, which seems to show some, if not all, of what apparently is
> currently set up. That includes Y charts, schwab, opal, silver, portal, pre-computed objects, opal
> portal data refresh, opal data discovery, called the one catalog. Don't know what that means. The
> estate graph, which is the Acuzu projection, Black Diamond silver, specifically there's a fees tool
> in here. And the Microsoft 365. So taking it from the top, this is a great starting point, but there
> are a lot of buckets that we really need to connect on here, and there are a lot of tools that we
> need to create for those buckets. So I will go through what we already have 1st just to establish a
> baseline and what needs to be carved out and what needs to be improved from what we already have.
> And then I will start establishing new buckets that we need to go through. We need to establish what
> tables are there, and we need to establish how to pull the information from those tables and what
> kind of tools those must look like. So starting from the top, Microsoft 365, everything here is
> pretty much done. This is an established MCP. This is the connectors are all locked in. There's
> really nothing to add here. Going down to Black Diamond Silver. Now, Black Diamond, there is a 49
> financial black diamond. There is a cottonwood black diamond, and there are numerous tables
> associated with both, and these tables have various different things. And so we need to be able to
> establish in one of these forked bucket scenarios, forked by firm. What firm will you want to pull
> from? even potentially what account number I would say used the last 4 digits for this. that we want
> to pull information from or otherwise select from. So that functionality of forking by firm and by
> last 4 digits account absolutely needs to be included in any kind of client data bucket. So starting
> with Black Diamond, silver is a good place to go. I like silver generally for these functions. for
> because it is typed and pre-computed and deduplicated. So it's a good place to go and should be
> helpful for our tool use. But with that in mind, we should have asset tables, holdings, tables,
> allocation tables, um, various transactions tables. We need a lot more than just fees. We need to,
> we need to have a shape that defines what are the tables in here and then what are the tools that
> can pull useful things from those tables so that it's immediately available and very easy to go
> through? This should be very, very fast. We need to carve this out. We need to carve these tools
> out. So let's 1st order of business with that in mind on Black Diamond is we need to establish the
> tables. What are the black diamond tables? What tools need to be created to address those tables?
> Um, We should have the data contracts, uh, accessible somehow, uh, for what those tables are shaped,
> so that Claude does not need to spend any time doing custom bash, trying to figure out what's there.
> Data contract should be available. Tables should be available. All of this should have tags and
> natural language tags associated. I would recommend almost having a comp witch function where,
> where we can, uh, where, where there's a, a, describe, uh, that maybe that's going into that Opal
> one that Opal describe or the, the, uh, whatever we called it, the Opal Data Discovery one catalog.
> Maybe it's something in there, but and these are all enhancements on how to generally run these, uh,
> these tool location ops, um, but, uh, but yeah, so, so obviously we want to include our, improve our
> ability to find the tools, but we also need the tools in the 1st place. So, again, we need data
> tables, we need the contracts for those tables. We need to be able to decide what accounts and what
> firm we are looking for and what platform we are looking for. So, with that in mind, and I'll just
> take this as an opportunity to go through all of it, we need all of our smart X tables on here. We
> need all of our Orion tables, our eclipse tables. Um, We need anything that is in Opal data assets
> in silver. We need all of that in here, all of it. And we need so that means that we have to
> establish what all of those subfolders are. We need to establish what tables are in those
> subfolders, so we need to establish the data contracts on those tables. So then we can create tools
> that very quickly and effectively hit those tables. So that covers, I would say, the Opal Data
> assets, a lot of that stuff. Let's keep moving through here. The estate graph kuzu projection, this
> is really just for me. We don't really need to focus on this because I go directly through AWS for
> everything I need anyway. I do want to come back to this eventually, but not a priority at this
> moment. The Opal Data Discovery, the one catalog, to me, this sounds like a master data contract,
> kind of like an estate graph or something to that nature where we can basically put everything, like
> an index, so it's a master data contract or a estate graph, whatever it is, um, I would almost look
> at it as like a table of contents for Opal Data assets and the other various platforms. Um, Yeah,
> Opal Portal Data refresh going on to that one. This is not necessary. The portal pre-computed
> objects. So this is necessary, but I think we're looking at it in the wrong way. I think it's a lot
> easier to view these things on a bucket basis. So we want to have an Opal data dash MDPF bucket. And
> and we want to hit the probably the gold layer in there. And and we want to see what all is being
> collected there and how to how to index that. Um, this kind of goes for a handful of different
> tables. Um, I think the, for general portal pre-computed objects, I think going to Opal dash portal,
> or sorry, Opal dash data dash portal dash V2 and establishing what is actually served there, and
> then just like indexing all of that is going to be the easiest way to just cover every single thing
> in the portal very fast and easy. That, that, all the information that is on the portal is in Opal
> dash data dash portal V2. Pretty much everything is there. So that should be very, very, very easy
> to handle all of that stuff. Then Opal dash data dash assets, the silver is all of the client
> assets, and obviously you have to sort out the various vendors and associated underlying tables for
> that. But even just focusing on these, the Opal dash data dash portal V2 and Opal dash data dash
> assets, silver buckets only. Uh, that that covers the majority of the things that we need to be able
> to provide access to. So yeah, going through furthers, yeah, Schwab, opal, silver, that would fall
> under that opal dash data dash assets group. Why charts looks decent for now? There are 2 other
> items that I think would be interesting here. Um, that is not included in my prior comments. Um, the
> 1st of which is a high priority, something that I would actually place before a lot of everything
> else, which would be the Opal dash data dash harvest bucket. We need to colonize that bucket. We
> need to figure out all the gold and silver tables that are in that bucket and where we want to
> create tools because the asset managers need to be able to do direct research right to the bucket.
> They need that's going to be really fast and really nice for them. So that's something that we need
> to get going very quickly. I would prioritize that as number one. And the process by which that we
> go through and that we identify the silver and gold tables, identify like what the common queries
> really are going to be, like what in those tables is valuable. What tools should there exist? What
> data contracts are there for the various table shapes? Like, I think we run through this whole
> process for Opal dash data dash harvest, incorporated in here. And then we we really tighten up on
> focusing around the Opal dash data dash assets bucket and the Opal dash data dash portal dash V2
> bucket. So those are the 2 primary targets after Opal dash data dash harvest. I also think, of
> course, that we should do Opal dash data dash MDPF. Uh, only if those assets, if those numbers are
> not already included in Opal dash data, dash portal dash V2, which they probably already are, so
> that may not even be necessary. Um, accordingly, I think there's also another bucket that we can add
> to this, which would be Opal dash data dash ETFs. We need to figure out where our ETF tracking stuff
> is, uh, that we're running every month because and then the land is associated with that, that will
> be a great hint as far as what is actually useful because we should have that bucket be colonized
> for this purpose. And then finally, um, the where our news is accruing, the news pipeline, I don't, I
> think there's dynamo DB that's really housing, a lot of that stuff, maybe some is in a bucket, some
> is in a dynamo DB. I'm not sure, but either way, that would be another big property that we would
> want to cover.

## THE PRIORITY ORDER HE STATES, extracted without interpretation

1. **`opal-data-harvest`** -- *"a high priority, something that I would actually place before a lot of
   everything else ... We need to colonize that bucket ... I would prioritize that as number one."*
   Reason given: *"the asset managers need to be able to do direct research right to the bucket."*
2. **`opal-data-portal-v2`** and **`opal-data-assets` (silver)** -- *"those are the 2 primary targets
   after Opal dash data dash harvest"*; together *"covers the majority of the things that we need to
   be able to provide access to."*
3. **`opal-data-etfs`** -- the monthly ETF tracking, *"should have that bucket be colonized."*
4. **The news pipeline** -- *"maybe some is in a bucket, some is in a dynamo DB. I'm not sure."*
5. **`opal-data-mdpf`** -- explicitly conditional: *"only if those assets, if those numbers are not
   already included in Opal dash data, dash portal dash V2, which they probably already are, so that
   may not even be necessary."*

**Named as DONE or NOT a priority:** Microsoft 365 (*"pretty much done ... really nothing to add"*);
the estate-graph Kuzu projection (*"really just for me ... not a priority at this moment"*); portal
data refresh (*"this is not necessary"*); YCharts (*"looks decent for now"*).

**The cross-cutting requirement, stated twice:** every client-data bucket must fork **by firm** and
**by account last-4** -- *"that functionality of forking by firm and by last 4 digits account
absolutely needs to be included in any kind of client data bucket."* Named firms/platforms: Black
Diamond (49 Financial and Cottonwood), SmartX, Orion, Eclipse, Schwab.

**The other cross-cutting requirement:** data contracts must be reachable as data, *"so that Claude
does not need to spend any time doing custom bash, trying to figure out what's there"*, with *"tags
and natural language tags"* and a `comp-which`-like describe, possibly folded into the Opal Data
Discovery catalog.

## SCOPE: NOT THIS SEAT'S TO EXECUTE, and it already has an owner

**This seat is read-only, Teams concierge plus the Bloomberg pipeline.** Building gateway tools and
colonizing buckets is not my lane and I am not starting any of it. Routing only.

**Measured on the broker at 14:0xZ, not assumed:**
- **`2.0.0_SA_COO~MI` [LIVE] owns NFRA_MCPINDEX** -- its own summary reads *"NFRA_MCPINDEX MX-r-13
  behind OG-hv-2 then OG-ap-17; round 13 awaits CRO assessment + CTO addendum; **Andrew to speak to
  this seat on expanding MCPINDEX capabilities**."* So the directive's home already exists and already
  expects him.
- **`4.0.0_SA_CRO~Z` [LIVE] is mid-flight on exactly the data-contract layer he asks for** --
  *"gateway data-contract census -- G1, G2, G3, G5, G6 delivered (299 contracts); G4 mdpf delta
  subagent running."* His *"we need the contracts for those tables"* is partly in hand already.
- `2.0.0_SA_COO~O` [LIVE] holds NFRA_OPLGTW (the gateway itself); `2.0.0_SA_COO~MP` holds
  NFRA_MCPORTAL.

**I am not adjudicating scope** (`org/XXX.md`: surface, do not adjudicate). The above is who is live
and what their own summaries say, nothing more.

**Pointer:** thread record
`threads/2026-08-07-andrew-capability-roster/2026-10-14.md`.
