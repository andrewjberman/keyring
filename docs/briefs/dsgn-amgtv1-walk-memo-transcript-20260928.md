# DSGN_AMGTV1 -- Andrew's AMGT walk memo, transcribed and split by surface (2026-09-28)

**Source audio:** `C:\Users\Opal Bloomberg\Downloads\AMGT WALK_3557.m4a` (18:11, mono 16 kHz, recorded by Andrew
2026-09-28; not committed). **Snapshots he refers to by file name:** `C:\Users\Opal Bloomberg\OneDrive - Opal
Capital\Pictures\Screenshots\AMGT_walk_v1\` (12 PNGs, taken 17:31-17:34 local on the localhost build; not committed).
**Transcriber:** `openai-whisper` 20250625, model `turbo`, run locally on site Z (CPU, 587 s), `language=en`,
`fp16=False`, with an initial prompt carrying the page's vocabulary (Lead Panel, Trending, Breakout, Chatter, Thesis,
Exec Mgmt, Peers, Model, Posture, Holdings Breakdown, ETF Classifier, RSI, Topic Cloud). **Transcribed by:**
4.0.0_SA_CRO~Z on Andrew's word (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260928_223xZ_DSGN_AMGTV1_WALK_MEMO_UIWALK_FIXTURE_PORT_BRIEF.md`).

**This is the machine transcript, uncorrected.** Mis-hearings stay in the lines and are glossed here, never edited:
"Lucia" = Lusha; "clawed web search" = Claude web search; "SERP bright data" = Bright Data SERP; "new scanner
pipeline" = the News Scanner pipeline; "factor tilts" = the Factor Charts page (`/factor-tilts`); "Adam" = the asset
management analyst whose model sheet the Model tab ports. The headings M0-M15 are this seat's split by surface, cut
at the sentence where Andrew names the next PNG or tab; the brief cites them as `M<n>`.

| Section | Surface | Andrew's snapshot |
|---|---|---|
| M1 | Lead Panel, Breakout x Chatter, chart | `breakout_chatter_chart.png` |
| M2 | Lead Panel, Breakout x Price, chart | `breakout_price_chart.png` |
| M3 | Lead Panel, Trending x Chatter, chart | `trending_chatter_chart.png` |
| M4 | Lead Panel, Trending x Chatter, list | `trending_chatter_list.png` |
| M5 | Lead Panel, Trending x Price, chart | `trending_price_chart.png` |
| M6 | Lead Panel, Trending x Price, list | `trending_price_list.png` |
| M7, M8, M15 | Lead Panel with a security selected (header cards; timeline) | `security_leadpanel.png` (992 HK) |
| M9 | Thesis tab | `thesis_pbr.png` (PBR US) |
| M10 | Exec Management tab | `execmgmt_pbr.png` |
| M11 | Peers tab | `peers_pbr.png` |
| M12 | Model tab | `model_pbr.png` |
| M13 | Posture tab | `posture_pbr.png` |
| M14 | Synthesis: which estate fixtures to reuse | -- |

---

### M0 intro

[00:00] I'd like to go through a handful of visual smoke tests of the asset management page so that we can develop a project designated to the front-end design and improving that user interface and user experience.

### M1 Lead Panel: Breakout x Chatter, chart

[00:19] So starting from the very top of the page, which I will refer to by the named PNG files, we will begin with the breakout chatter chart.
[00:32] Now there is nothing displaying here at the moment. We see a caption, quote-unquote, no rank history has been requested for this combination yet.
[00:41] I look at that as a missing data issue, not a front-end issue, so we can clear that for now.

### M2 Lead Panel: Breakout x Price, chart

[00:48] Moving on to the breakout price chart.
[00:52] So it's very difficult here to actually understand, based on the interface design, what the prices are, what the ranks are, what even the securities are,
[01:06] because we're referring to them based on identifiers, which, for example, in the case of what I believe to be Lenovo is 992HK.
[01:16] We're going to need some kind of library here.
[01:22] What I suggest is actually building these securities in to the ETF classifier route so that we have a definitive asset class and sub-asset class and all Opal-based taxonomy
[01:40] so that we have a stable key for names that the front-end can rely on.
[01:47] I think that is a more logical way to approach this.
[01:50] Beyond that, the ranking is not particularly easy to follow, especially as we expand this to 10-plus securities or however many.
[02:04] Currently, obviously, there are five, and it's already difficult to understand.
[02:10] So I think probably what makes more sense here is, I don't know, we need another type of visual format.
[02:19] That's something that we should discuss, what visual format really makes sense here.

### M3 Lead Panel: Trending x Chatter, chart

[02:22] Moving on to the trending side.
[02:27] So we will go through the trending chatter charts.
[02:32] Again, a lot of x-axis ticks overlaying or crossing over, overlapping with the bottom x-axis line.
[02:44] That's not great design.
[02:46] A chart here.
[02:52] We need to figure out a better chart solution for this either way.
[02:55] I think there's the possibility of...
[03:00] I don't know.
[03:00] We need to figure out a better chart solution for this because it's going to get overly complex.

### M4 Lead Panel: Trending x Chatter, list

[03:05] Moving on to the trending chatter list.
[03:08] This is fine.
[03:09] A ranking list is probably going to make way more sense, likely with maybe a day-over-day or iteration-over-iteration plus sign or minus sign,
[03:24] demonstrating how many leaps it's taken or how the rankings have shifted since the last run.
[03:31] Obviously, we need to display the names, not just the symbols here.
[03:36] I think this is an opportunity to develop a lot more visual information.
[03:42] It's quite sparse right now, in part, because we simply don't have a lot of data.
[03:46] But also, as you can see, there is data for Boeing and Home Depot, and we're really just showing nothing here.
[03:54] Furthermore, in the bottom panel, as you can see, quote-unquote, served by the producer partition, trending chatter.
[04:01] All of this footnote stuff is non-canonical.
[04:06] We always do footnotes the exact same way on all portal services.
[04:10] It is always source and timestamp.
[04:12] That is a pattern that is in every single portal panel.
[04:15] So that is going to have to be adhered to as well.

### M5 Lead Panel: Trending x Price, chart

[04:19] Moving on to the trending price chart.
[04:21] Again, this chart information is going to have to be represented another way.
[04:29] I don't know what way that is quite yet, but it's going to be very, very complex to try to overlay all of this stuff
[04:36] when there's going to be much more securities.
[04:42] And again, we need a stable name.
[04:45] And also, as you can see, the design here is really just suboptimal in every conceivable way.
[04:50] So that's going to need some work.

### M6 Lead Panel: Trending x Price, list

[04:53] Briefly moving to the trending price list.
[04:56] Yes, this is good, but this is an opportunity for us, again, as I said, to increase the visual information.
[05:05] Less text.
[05:06] Again, need the titles of the actual companies.
[05:08] That's where that ETF classifier route is going to come in handy for making a canonical form for this.
[05:15] What I suspect would actually make this very nice is if each row actually has not only the name, the ticker,
[05:27] the period over which there was this price appreciation or depreciation, this price delta,
[05:34] but because we're going to run this through the ETF classifier system,
[05:40] that means we should also be able to display asset class, which, of course, will be equity for all of them,
[05:46] and subasset class, including the industry sector and how we have done that for the ETFs on the positioning
[05:56] opalinvest.dev portal page, the POSN positioning page.
[06:02] On the ETFs toggle on the positioning page, you will see how we lay that information out.
[06:08] This could be a great opportunity to reuse that same fixture so that we can lay this out in a clean table that has not only the
[06:19] performance figure and the ranking, but, of course, the name, the asset class, and subasset class all listed out.
[06:25] I might suggest using that positioning component, that holdings breakdown component from the positioning page.

### M7 Lead Panel: Security (header cards)

[06:35] So now that we have covered the trending and breakout, let's briefly go through the lead panel if a user selects a security.
[06:47] This is a lot of information. As you can see, there is text everywhere.
[06:53] When there's too much information on display, the user does not want to look at any of it,
[06:59] so I think it's a lot more sensible to adhere to frameworks around progressive disclosure,
[07:07] figure out what are stable fixtures within this panel, never more than I would say four cards.
[07:13] That's just too much information. They should be four consistent cards,
[07:18] and maybe those cards can be clicked for a modal pop-up, for a fixture pop-up.
[07:24] Again, I would recommend looking at the philosophy page cards for how those modal pop-ups work.
[07:31] I think that is how we should probably design here, because those modal pop-ups, we can display more information.
[07:39] So really what this means is codifying or templating, like a handful of cards here,
[07:46] I would say probably price and market cap, like all of that can probably go together.
[07:54] Maybe price is what is displayed immediately, and then when you open up that card, you see price, market cap, etc.
[08:02] Maybe there's another card that does like financials and then leads with enterprise value or something,
[08:08] and then it shows net debt, etc., etc.
[08:11] Then maybe there's another panel that leads with a beta, and that's market features,
[08:16] and that shows volatility, beta, all those kind of features, something like that.
[08:21] Yeah, that would be like three cards, maybe like price and volume or something.
[08:28] Then financials, some kind of financial header, so enterprise value might be a good one to go with there.
[08:34] And then the third being some kind of market function.
[08:41] That's why I say beta, like looking at beta and then expanding, and you see volatility and duration.
[08:47] I guess duration wouldn't be relevant here, but features like that.
[08:53] And then probably a fourth card, just to have a fourth, would be like something like trading technicals or something.
[08:59] And we show whether there's been a bullish or a bearish trend, the average volume and short interest, all of the trading technical stuff.
[09:08] So again, four cards on this lead panel that do progressive disclosure that open up to display more information on those subjects.

### M8 Lead Panel: Security timeline

[09:17] Now, moving to this timeline, currently you can see that it could not be loaded,
[09:21] so we're going to need to actually see that to really know what this displays.
[09:29] There's a lot of opportunity there.
[09:31] I just can't comment on it because we don't know what is actually there.

### M0 halfway flag

[09:35] Moving on now to the individual pages.
[09:40] So I'm going to offer a handful of comments here.
[09:43] I want to write a flag.
[09:44] This is the halfway point.
[09:46] So up until now, we've discussed the lead panel and the various views displayed there,
[09:52] which include the trending, breakouts, and security-specific lead panel.
[09:58] Now we are moving on to the next part of our segment here, which is going to be focused on the tabs, like per-specific security.

### M9 Thesis tab

[10:07] So as we go into the initial tab thesis here, the recommendation, I would love to know how we come to that conclusion,
[10:19] but that's another matter.
[10:22] The citations, I like these citations.
[10:26] I wish it was more clear where they came from.
[10:30] There's a lot of text.
[10:31] We're showing a lot of text here.
[10:32] This is another opportunity for progressive disclosure.
[10:36] I think it probably makes sense to figure out how to card some of these items so that it's not just so much information.
[10:45] There are obviously a couple sections that would be cards.
[10:50] Clearly, the investment thesis would be a card.
[10:54] I believe you should be able to drill into that.
[10:57] Not something that just does a little drop-down.
[10:59] That does not look good.
[11:01] It should be like a modal.
[11:03] I think a modal would make a lot more sense for this because that way we have the opportunity to do some proper visuals.
[11:12] But, yeah, so with that in mind, the investment thesis would be a modal pop-up.
[11:22] There should be some nice and clean depiction of that that is clear to click on.
[11:28] And then whatever other items there are.
[11:31] Let's see.
[11:32] Yeah, so investment thesis, risks, recommendation.
[11:38] Those seem to be three solid cards that would maybe sit beneath the principal charts.
[11:47] The whole description section and recommendation needs to be laid out better.
[11:53] That's just not good enough.
[11:55] I don't like these little drop-down things.
[11:59] I just feel like that would be a lot better served in a modal pop-up, which then has drop-downs.
[12:04] So we need to get away from showing this much text.
[12:07] It's just too much information.

### M10 Exec Management tab

[12:09] Let's go into exec management.
[12:12] So in the exec management tab, as you can see in the case displayed here, we actually don't have any, which shows that we're going to need a solution if Lucia cannot find anything and if Bloomberg doesn't display anything.
[12:28] So I would say that if there's really nothing displaying for exec management, then we need to have a third fallback, which is a clawed web search or something.
[12:42] And maybe this is the opportunity for an SERP bright data search engine moment.
[12:50] That could be a great fallback if we are lacking exec management information.

### M11 Peers tab

[12:56] Moving along to peers.
[13:01] Peers looks pretty good here.
[13:03] I actually kind of like what we're displaying.
[13:05] My only comment is that the absent columns kind of need to clean that up.
[13:12] We need a more elegant way of covering this.
[13:17] And again, as you can see, there are a lot of random strings, not only here on the peers, like where you see identity crosswalk v1.
[13:24] All of this stuff is, it's just not very pretty.
[13:29] It's not very organized.
[13:31] That should all be cleaned up significantly.
[13:34] We will proceed now into model.

### M12 Model tab

[13:37] So to clarify, model, as I understand it, is simply porting whatever Adam had put together or whatever was existing in the corpus for the asset management research folder on the SharePoint.
[13:48] That's fine, but that should be qualified.
[13:52] We also want some explanation as to why all of these features list as refused, as not yet built, not measured.
[14:01] If that's just a back-end data issue, so be it.
[14:04] But if that's a lack of front-end adapter, then that's something that we're going to need to clarify and handle in this project.
[14:11] In any case, it needs to be brought up and handled on the back-end if there is also a back-end issue, but that is outside the scope of the front-end work.

### M13 Posture tab

[14:24] Now, finally, as we go into posture, so nothing is displaying here, and there's really just no UI of any kind.
[14:34] This is an opportunity to make another template.
[14:38] I like to think of everything as cards and modals because we want to be able to standardize.
[14:44] We want to standardize a pretty, clean, branded visual component architecture, whether it's charts or cards or whatever the fixture may be,
[14:54] rather than just laying out a fucking shit-ton of text all over the place because that is going to be very difficult to read.
[15:01] Nobody wants to read that.
[15:02] And if we hammer in our component architecture, this will do a lot of work for us across this entire project.
[15:11] And that component architecture, again, is all throughout the portal.
[15:14] We don't need to reinvent the wheel, and in fact, we should not invent the wheel.
[15:17] We should reuse the fixtures we've already developed.

### M14 Synthesis: fixtures to reuse

[15:22] So to cover it from the top, that means in that lead panel, in the ranking, I think the positioning page, holdings breakdown components,
[15:31] using both the ETF classifier DynamoDB tables for importing all these securities and sorting out their names and asset and sub-asset classes, industries, and so on.
[15:44] That should all be taken care of in the lead panel.
[15:49] The charts, we have plenty of charts all over the place, particularly in factor tilts.
[15:55] There could be some recharts or apex, whatever language we're using for the charts.
[16:00] That should be brought in to handle that.
[16:04] I think potentially if we do better charting and better labeling of those charts,
[16:08] maybe we can have a more effective trend line function for those views.
[16:15] Moving through the various tab groups,
[16:21] yeah, we really want to use a lot of our card fixtures and modal pop-ups.
[16:26] I recommend looking at the global RSI from the market overview page.
[16:31] I think that could be a nice modal opportunity.
[16:37] I also recommend looking at the philosophy page and the philosophy cards.
[16:42] Those may be more effective for qualitative information,
[16:46] while the global RSI U.S. regime modal pop-ups may be better for the chart information.

### M15 Synthesis: timeline spine, news, harvest

[16:54] Finally, going back to the lead panel with the timeline,
[17:01] we really just need to see what we have.
[17:04] That's hard to really gauge it.
[17:05] But again, we want to reuse a lot of our existing component fixtures,
[17:09] and we should have plenty of opportunities for a timeline spine for any given security.
[17:16] And I think the bigger function here is how that front end draws against the Opal Data Harvest news coverage,
[17:27] how we want to design that,
[17:30] because our goal is to really put together effectively just a timeline with keywords,
[17:37] like word cloud if we've got it, with headlines if we've got it.
[17:42] We need to kind of work to figure out what that component looks like
[17:47] and how we can reuse a lot of our information,
[17:50] not only from Opal Data Harvest, but also from the new scanner pipeline,
[17:54] because it's very possible that there is relevant information on these securities from there.
[18:00] Although, of course, we are going to be leading with the Opal Data Harvest publication information,
[18:05] the likes of which we are going to have to engage a backfill on very shortly.
