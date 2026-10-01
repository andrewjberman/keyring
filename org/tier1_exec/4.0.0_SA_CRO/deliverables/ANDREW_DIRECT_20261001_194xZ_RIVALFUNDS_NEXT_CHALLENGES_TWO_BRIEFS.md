# ANDREW-DIRECT 2026-10-01 ~19:4xZ -- rivalfunds next challenges: two briefs (backend data + AI synthesis; frontend MCP page)

**Channel:** terminal, session of `4.0.0_SA_CRO~RV` (site Z), received 2026-10-01 ~19:47Z, with two dictated transcripts
Andrew supplied as local files:
- `Downloads/Rival funds data ops_9838.txt` (805 words);
- `Downloads/Rival fund uiux_8461.txt` (1,276 words).

Both are Andrew's own dictation and are carried below verbatim. The source files are not committed.
**Recipient:** `4.0.0_SA_CRO~RV`.

## Verbatim -- the directive

> While we're here, I want to run a brief on the next challenges for rivalfunds. there are two sides we need to bang
> out, on one side it is the data and ai synthesis aspect, what needs to be built for that to be completed. on the
> other side it is the ui and how it is presented on the mcp landing page. i have included two transcripts for your
> analysis to this end. I want you to write a brief for each of these workstreams, essentially backend rivalfnsd and
> frontend . only note on the subject is toward the end of the ui transcript i started having ideas on how the AI
> accesses data and that should probably be covered in the backend brief. read these now and get started

## Verbatim -- transcript 1, "Rival funds data ops"

> What I'd like to focus on in this message is the content and presentation of the Rival Fund's MCP page product.
> Currently it functions as something of an audit log that extends deeply down into the page. It feels like the user
> is scrolling from miles. It is more of an audit log than a presentation and my interest today is establishing the
> nature of our data collection because if we have effectively locked in bronze ingestion for all relevant funds
> including IDVZ and PFOE, then and if we also have included all the relevant table structure and that is complete in
> silver and we also have our data tabled out in gold with the necessary analytics layers to provide our three
> ultimate goals which are assessing by trading, by reverse engineering trading, the outperformance and
> underperformance of these managers by sector and by security and being able to granularly track that and make those
> distinctions. That's point one. Point two is you'll have to refer to our documents to remember what point two is.
> And then point three was the hands on the door miscellaneous AI analysis. Oh, point two was the projected trades,
> projected trades, reverse engineering their tilts. So again, point one is underperformance and outperformance by
> sector and by security. Point two is projected trades, projected which we which should be summarized effectively as
> their tilts and bets, not only by security, but also by sector. And point three, I would say is not only just the
> hands on the door AI analysis. Point three is a AI synthesis. It is looking at the trends that they are making. It is
> looking at the really looking at both points one and point two. And from those making assessments on what it thinks
> these managers are doing right, what they are doing wrong, what it expects them to be doing. Being able to
> distinguish that just because there is a trend does not mean it is expected to continue indefinitely. I think that
> at this point there is a big opportunity for web search and even search throughout the existing opal database,
> particularly opal data harvest and the opal news scanner, because I think that the, and this may be an easier
> mechanism, frankly, than web search for the AI to distinguish and to synthesize those points that I requested.
> Because then it can look at not only the activity of those funds managers, the performance and activity of the
> trading in those funds, but it can look at the broader world. It can look at what is happening in the news. It can
> look at and make assessments based on what it expects these managers to do. Some things that I think would be
> interesting to include in that assessment is essentially all of the sentiment layers from the market overview page
> in the portal. I think that it should bring in the the word cloud, daily word cloud, I think is interesting. Or like
> if we have it in a more ranked columnar setting back in the news scanner, that could be interesting to corroborate
> yeah, outperformance, underperformance, and projected trends with that phrasing, right, with the effectively the
> topic cloud phrases, how these phrases are appearing. And that so that would be one I think global RSI is also a
> very big one to to be looking at. And also, of course, the I would I would use maybe the S&P like market momentum
> from fear and greed, as kind of like a general market, maybe, maybe some of the the fear and greed aspects. Um, even
> because we should have data saved for those, I believe we have an appended setup. So we should have further than 90
> days, even if we only display 90 days. So I think that there are some axes in that fear and greed, which I think
> would be interesting to potentially bring in here, like the put call ratio is a good one, the index for the breadth
> of the market and the concentration of the market. And of course, S&P momentum, I think those three would be a great
> starts. So that should give you more clarity on how the AI should be prompted and what tooling or what tables should
> be accessible to it. Um, if we have to make any staging tables, so be it. But, but that, that's how I would
> recommend doing that. Preferably, it can be light, I hope that we can just kind of have a very simple structure to
> assess how that sentiment data is stored. So we can have a, a light reading or figure out how to, yeah, lightly and
> athletically incorporate that into the AI analysis and synthesis. So this comprises the data side and the
> effectively the operations as well.

## Verbatim -- transcript 2, "Rival fund uiux"

> The other brief that I would like established is focused on the user interface and user experience. Now, this is a
> simple presentation. We are just hosting it on that MCP page. There's no dashboard function yet. But with that in
> mind, I think now that we have established deeper what the AI is going to be analyzing, what tables we have put
> together for the outperformance, underperformance. Maybe if we have tables that can do projections, if those exist,
> like I guess the trend lines of their security and sector allocation holdings over time. We want to think about how
> the presentation works by just coming down very simply from these views. We effectively want a view that shows how
> the – like where – like maybe like a ranking list of where these managers have really been outperforming and a
> ranking list of where they are most underperforming. And we want that ranking list by individual securities, and we
> also want it by sectors. So for the individual securities, I think we pull the top ten best performers and then also
> the bottom ten starting from the worst performers. I think that's a rank to view. We want to be able to present that
> on a QTD and YTD or a quarter to date, year to date, and month to date probably is the best way to do it basis so
> that you can click – you can toggle MTD, QTD, YTD, and see those tables change. And we should, of course, be using
> fixtures that already exist on the dashboard to do this. You should not be reinventing the wheel. We have all of the
> toggle logic. We have all of the components for this. We just need a nice little ranking layout, probably rely on the
> philosophy fixture cards for this. I think it's the cleanest for how these lay out. And then have some toggles in
> there to do quarter to date, month to date, year to date, or in order, ordinarily speaking, it would be month to
> date, quarter to date, year to date. So, again, that is the first view, which is by fund. I would have – I would
> display probably just one, like, wide – this should be one wide component, which just shows the – yeah, these high
> performers and underperformers. And then I think you can select by fund. So, I think it should maybe default to
> IDVZ. And I think we have a little dropdown that has IDVZ and all of the IDVZ comparisons, including the benchmark.
> And the same for PFOE, where we have their Russell 2000 IWM benchmark and all their comparisons. And we can
> effectively choose if we want to look at IDVZ and their competitors slash benchmark or PFOE and their competitors
> slash benchmark on this basis. Like, what are the top ten performers? What are the bottom ten on the given
> timeframes? So, that is view slash component one. That answers the first of our things that we want to be able to
> present. Component two is going to be a table that effectively shows projections, like, like, the trend line. We
> need to be able to show some kind of intuitive trend line of where the most – like, where the buying activity has
> been for those top ten and bottom ten securities and for the sector, overall sector. So, top ten – and this is
> another thing that you really want to thread and synthesize across these two views, across both components, which
> is that top ten and bottom ten are two different functions. Top sectors, we just want to see – I think that
> actually, you know what, let's do this. There's top ten and bottom ten for performers on the security level. And
> then there's top sectors and bottom sectors. And we probably only need five for this. We only need the five top
> sectors and the five bottom sectors. And this way, there's a clear continuity where in component one, we are showing
> effectively a ranked list, just a nice table, very good UI table, with the necessary toggles that I already
> described for time interval and fund selection. Then for component two, where we are doing the projections, I would
> look at this as a naive view, just, like, effectively doing projections based on trends, trying to assess if there
> are trends in their buying activity. And probably – yeah, this should be a very simple table. I would also structure
> it based on the securities, top ten, bottom ten securities, top five, bottom five sectors. And this should be a
> naive trend and probably want to include some – and I think this only needs to be on the year-to-day basis. That's –
> yeah, this is – or, yeah, year-to-day is enough for this. So – and that's just established. There's no toggles.
> It's just year-to-date. Moving from that, now I think we can go to component three. Component three is an AI
> analysis that will effectively be run on each – not only on the – so it should have a different prompt. We only
> need it to address the rival funds, not the benchmark, and the IDVZ PFOE OPAL funds. We do not need to apply any
> analysis to the benchmark. And the purpose of this view is that the AI should essentially look at where the top and
> bottom performers were, where the top and bottom sectors were for these various funds, for the rival funds. And it
> should also look at the sentiment channels that I mentioned in the data brief or the data transcript on the same
> subject. And what the AI is there to do is to effectively make a judgment call or a synthesis on what it has – what
> it expects these managers to do, what it thinks that they have done well, like – I think that there's actually
> several parts that this AI is going to – there's several prompts that it effectively has to deliver. And I think
> that these prompts are – they should be effectively cached. They should be run one after another so that it has the
> context built up as it continues to do this. So the first one is, what has this fund been doing? What have they done
> lately? Have they done anything of interest in the last rolling 30 days? Anything unusual? Any big wins? We want us
> to kind of have, like, a rolling 30-day view of just, like, what's happened recently with this fund. Where were our
> big wins they've had? Where were our big losses they've had? Just anything notable on those kind of axes. The second
> point the AI has to make is effectively on the projected function, so on component two. Now, what it's trying to do
> here is it's effectively trying to corroborate or otherwise – or corroborate, refute, or enrich the view of the
> projections based – or the view of the trends of this fund based on their trading activity. We need to know what the
> trading activity is like. Is it more systematic? Is there systematic trading identified? Is it more discretionary,
> just big concentrated blocks? We want to use that. We want to use the sentiment from overview, and we want to use,
> of course, the components one and two data. And so in the second part, the AI is basically making a claim on what it
> believes is happening and what it believes will happen to corroborate, refute, or otherwise enrich its position on
> these funds and what it expects them to do.

## Scope as given (not adjudicated)

- Two briefs:
  - backend: the data and AI synthesis, including how the AI accesses data (the end of transcript 2);
  - frontend: the UI and presentation on the MCP landing page.
- Transcript 2 names the PFOE benchmark as "their Russell 2000 IWM benchmark". That answers, in Andrew's words, the
  instrument question left open in `ANDREW_DIRECT_20261001_182xZ_ETFS_RIVALS_THREE_CALLS_ANSWERED.md`.
