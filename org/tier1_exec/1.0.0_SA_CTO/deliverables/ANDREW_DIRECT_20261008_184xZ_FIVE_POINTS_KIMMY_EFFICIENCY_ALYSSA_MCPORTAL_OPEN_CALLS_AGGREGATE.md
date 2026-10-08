# ANDREW_DIRECT 2026-10-08 ~18:4xZ -- five points: Kimmy comms routing, efficiency status, Alyssa's Schwab channels, MC portal control plane, aggregated open calls

**Channel:** laptop terminal, to 1.0.0_SA_CTO, pasted transcript ("I have a transcript of a bunch of stuff I want looked into
right now, please see the below and let's start going through it"). **Recorded by:** 1.0.0_SA_CTO, same turn.

## Andrew's words, verbatim

> "There are a handful of projects floating around, and I want to know status on them because I do not believe they were
> officially laid out, and so they were really just ideas that may or may not have appeared in the context of a brief or
> otherwise. One of these is the process surrounding the Kimmy agent that will effectively route text messages via Quo QUO. To
> me, for new teams messages. So something I've noticed for that is that I feel like I am not getting all the team's messages.
> It seems like a lot of them are falling through or it's otherwise unclear. what is happening there. So I definitely want to
> clean that up. I also want to know about any project or work stream dedicated to the email aspect of that because I need to
> have the same exact process accessible via email. Um, This that project is probably big enough at this point to graduate to
> an official macro project code if it is not already and that code would cover the teams and outlook, uh, Kimmy agent and how
> that is routed to me and all processes associated with cues and communications to that end. So that is point one. Moving on
> to .2. I want to understand the various efficiency gains that we're working on, where are we with the get processes, the get
> operations, which is CROA, where are we with the Kuzu DB operations, that is CRO base? Where are we with the garbage collector
> solutions? That is C-R-O-B. I want to make sure that these are properly implemented across the boxes because We need to make
> sure that we are not getting jammed up on get. Git is the biggest problem for us. These merges that fail and kind of
> catalyze the concurrency storm with the git commence, all of that is big, big, big hold up, and we need to get to the bottom
> of that and make sure that if nothing else that that is cleared immediately, So put that as point number two, uh, point
> number three, I believe on the site Z box, I have some ongoing work for the Schwab workflows. as it pertains to Alyssa. I want
> to know status on that, because we need to open up some of those channels. We're getting to a point where we are inevitably
> going to have to, uh, probably push ahead with what I will call uh, point number 3 shortly with MC portal that's NFRA
> underscore MC portal. We need a control plane. There needs to be a advancement on our on our efforts on the control plane
> side. Um, I will get into that in a second. continuing on with, yeah, .3 So .3 being the Schwab workflows MCP index, MCP
> operations, Opal Gateway, need to know where we are at for Alyssa. We need to have all of those channels working
> functionally. We need to have the entitlements proper and the fields cannot be so anonymized. This was all handled on site Ze
> already. I just want to know status if we need to reauthenticate the gateways or what needs to happen there to get Alyssa off
> to the races. Moving on to point four, the MC portal. So clearly we are having a lot going on moving very, very quickly.
> We're already seeing some failures in the context of earlier today when we set up the The new email account for Kenny at
> Cottonwood, one of the partners. He had an internal server error where he was not able to log in. So I had to manually read
> the email and go to a Codex agent on the laptop box, 0.7.0 cloud ops, and go troubleshoot what was going on with the email.
> First of all, this is something that should be handled entirely in the context of .one, when emails and teams come in, I
> should be notified when they come in from a client that should go directly to my phone, and then I should be able to run the
> remote drive or issue a hashtag dev command to get those handled immediately. So that's part one, circling back to the .one
> aspect. Beyond that, We really need to be able to understand very quickly, not only where we are, like have certain processes
> with user management, be able to poll users off the platform at a moment's notice. We need to, so that means that MC portal
> needs to be set up. We need to have a lot of things on this MC portal, obviously, the entitlements, managing the
> entitlements, managing what is this, we need a, 1st of all, like what even is on the Opal Gateway, what are all of the
> channels that are open and what tools are available associated with those channels? What an index per channel needs to be
> displayed? Um, and what fields, what information is available through those tools? If they're going to data tables, what is
> there? We need an index. We need a map. And we probably need a ultimately like a risk rating based on how sensitive that
> information is. So in the event that we want to create policies for riskier MCP channels, That's a little further downstream,
> but something that we want to make sure is covered now. At least in the context of a brief that we can return to later. The
> more immediate ones are probably functions around our ongoing agentic infrastructure. We want to be able to see what is
> happening on our control plane so that covers the The graph, we want to have those, that activity overlap function, that
> should be streaming to that portal. We should be able to see get operations. We should know, commit pace, what commits are
> coming from where, what projects are they touching? Um, potential risk for overlap, what that what those risk ratings look
> like. pushes across boxes. We need to be able to see all of these features down the line, moving on to the Yeah, so I just
> want to make it clear that as we get these processes locked in, it's like we're going to need to be able to have a visible
> dashboard control plane on item 4 there. So on .4, That is infra underscore MC portal. I believe that covers everything for
> now. Um, Actually, let's go on to .5. is that I noticed that we are building out these uh, open calls JSON, um, that are
> that are built per box. Um, we need to have a skill um, that can be run from any box, but that effectively aggregates all of
> these open calls with a timestamp. Um, It's like as calls come up, there's there's 2 types of open calls. There's the main, I
> mean, really any of them, open calls or things that only Andrew can do. Sometimes they call this different things, like
> things that we're waiting on Andrew for. If it's like a big policy change or something, uh, all of this, however, should
> really be resolved in open calls, but, um, Because otherwise agents want to say everything is reserved for Andrew. So maybe
> it's better that we keep that all in open calls. But the premise is that we need to be able to see at any given moment where
> the forks are, on what projects, on what box, and that all needs to be manageable, open calls need to be manageable
> instantly. So I don't know if those JSons, if it makes more sense to have them be something that is committed, or if they are
> just constantly overridden directly in the cloud and like accessible through SQS or something like that, so that there is no
> lag. We do not want lag. It's like, it's like there should be no canvassing. There should be no, oh, we have to go around and
> talk to all the different agents to figure out what all the open calls are. The moment that an open call appears on a given
> channel, that needs to be pushed to, like I would say, I think it makes the most sense in the cloud, NAWS. And the MSTR agents
> all have access to wherever that is. Um, Yeah, or maybe all agents have access to it. The point being is that it's there just
> should be a skill that runs with a script that checks that, um, queue, that checks the open calls queue, and it breaks down,
> um, Where are these open calls, what project, what agent, what box? And that's, and those need to get handled accordingly so
> that we can have instant viewpoint into that. So those are the issues that we need to cover. Thank you."

(Voice transcription. "Kimmy" = the concierge agent that relays Teams messages to Andrew's phone by text; "Quo QUO" = the Quo
texting service; "get" = git; "MC portal" / "infra underscore MC portal" = NFRA_MCPORTAL; "Site Ze" = site Z; "NAWS" = in AWS.)

## The five points, as placed by 1.0.0_SA_CTO

1. **Kimmy comms routing** (Teams + Outlook to Andrew's phone; missed Teams messages; client mail and Teams notify his phone;
   `/remote-drive` or `#dev` to act). Status, then a macro project code if none exists.
2. **Efficiency status** across the boxes: GitOps (4.0.0_SA_CRO~A), graph (4.0.0_SA_CRO), garbage collection (4.0.0_SA_CRO~B);
   git congestion cleared first.
3. **Alyssa's Schwab channels** (site Z: MCP index, MCP operations, Opal Gateway): status, entitlements, fields too anonymized,
   whether gateways need re-authentication.
4. **NFRA_MCPORTAL control plane**: user management (remove a user at once), entitlements, an index and map of every gateway
   channel, its tools and fields, a risk rating per channel (brief now, policy later), and live views of the control plane
   (graph activity overlap, git operations, commit pace by box and project, overlap risk, pushes across boxes).
5. **Open calls aggregated cluster-wide** with no lag: every box's calls pushed to AWS the moment they appear, one skill on any
   box reads them by project, agent and box.

## Addendum ~19:2xZ -- Andrew answers the five calls

Cards (~19:1xZ): 1 grade a merge only on the paths it changes; 2 macro COMM under D9; 3 Alyssa's sitting now; 4 how far to
loosen Schwab account anonymization (REC: account title and last 4 digits to entitled advisors, tax ID and address hidden);
5 Alyssa downloads (REC: no for now). Verbatim answer:

> "1.) Yes. 2.) Yes agreed. 3.)She can do that any time, i will have her do it right now. Are you saying that account names
> and etc are there with 13 month lookback now? 4.) Yes that's fine, I just asked that any "name" file regarding client name or
> account name is included. 5.) no downloads needed yet, but she can read it and have her agent compose CSVs with the findings
> so its kind of moot anyway."

Placement: (1) 4.0.0_SA_CRO~A builds path-scoped merge grading in `safe-merge.sh` (cross-file checks still read every file both
sides changed); 0.0.0_AB_MSTR lands. (2) Macro COMM is ratified for D9 (Teams and Outlook, the LDO-001 assistant, routing to
Andrew, its queues and communications); 1.0.0_SA_CTO lands the MACROS.yaml row. (3) Alyssa reconnects now. His question is
answered from the contract: account names are NOT served today, and the grant's date mode is `rolling_complete_window`, whose
contract default is 30 calendar days, not 13 months. (4) Client name and account name fields are included in Alyssa's
Schwab scope; tax ID and mailing address stay out (he named only names). (5) No download operation; read access only.
(3)-(5) go to site Z's 1.0.0_SA_CTO~O (NFRA_MCPINDEX / NFRA_OPLGTW).
