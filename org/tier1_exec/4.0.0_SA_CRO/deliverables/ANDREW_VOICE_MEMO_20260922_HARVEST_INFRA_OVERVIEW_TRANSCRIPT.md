# ANDREW VOICE MEMO 2026-09-22 -- "Opal Data harvest infra overview" (6m34s), transcript as relayed to site Z

| Field | Value |
|---|---|
| Source | Andrew's voice memo `Opal Data harvest infra overview_7257.m4a` (6m34s), machine-transcribed on the laptop (whisper large-v3-turbo, en); 5,036 bytes / 859 words / 45 lines |
| Relay chain | `4.0.0_SA_CRO` (laptop) msg 99554 -> `0.0.0_AB_MSTR` (laptop) -> `0.0.0_AB_MSTR~Z` -> this seat, msg file `20260922T172538Z_0.0.0_AB_MSTR_Z_Andrew_voice-memo_transcript_relay__via_.md`, on Andrew's word at the laptop CRO terminal ~17:0xZ: *"I need you to take the transcript file that completed and have MSTR send it to sitez, it needs to arrive with 4.0.0_SA_CRO~F on the sitez fabric"* |
| Recorded by | `4.0.0_SA_CRO~F`, 2026-09-22 ~17:3xZ, VERBATIM and unedited from the relay (the relay's own note: "AMGT underscore R-E-S-A-P-P" = AMGT_RESAPP; "IEFA, IEFA" is as spoken). A second 47-minute memo was still transcribing and is NOT here. |
| Scope adjudication | NONE. This is the record; the reading is in `docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md` and is disclosed there as the seat's. |

----- BEGIN TRANSCRIPT -----
I want to take an opportunity here to do a quick overview of the larger discussion about the asset management, security analysis, and research functions.
So we've developed a project that is the base for this function, the consumer-facing base, under the tag AMGT underscore R-E-S-A-P-P.
So what we want to establish here is the high-level diagram of what I view as the total system, the full system build, which covers not only the back-end infrastructure, but several consumer-facing applications that will be built over the next one month.
So initially, we start with the existing earnings reports that are generated in SharePoint in the asset management research folders in the Opal Capital shared SharePoint drive.
These form the foundation for the research that is really required, which is enriched, of course, by the Opal data harvest pipelines.
But we really want to figure out what needs to be employed, whether it's the Claude for Finance Claude API that fulfills most of this foundational data, and in the effort to effectively recreate the format of these previously generated earnings reports.
So those are held in the SharePoints.
This is something that I think we will build onto the Opal data harvest infrastructure.
We'll do a quick pass over this, write a brief to identify effectively a generative function, where that information needs to be sourced from.
If we've already covered it with Opal data harvest, great.
If we need to bring on an additional pipeline channel through the Claude API, that's fine as well.
So that's part one, is establishing the connection to the shared asset management research SharePoints for the previous earnings reports.
There are a couple details we want to clarify top level here.
So each of those earnings reports goes into a different GICS sector.
Certain sectors, certain types of business, for example, in financial services, banks versus insurance companies, are going to have different financial models.
A lot of this can be gleaned by looking at the individual earnings reports, and we will find what I would call as templates for KPIs and templates for models, for financial models, that can be identified from these historical earnings reports.
And that is something that we are going to want to work into our system and work into the security analysis application.
So we start from there.
Over time, we will develop a standard output, which is the standard earnings report.
This will feed into several applications.
On one side, there is the main application, which is the security analysis dashboard page.
There will be Claude workflows, which we will connect through MCP.
Maybe potentially shared Claude projects.
More on this later.
But I want to use this as an opportunity to explain that this is part of a larger ecosystem.
In the V2 version of what I would call the next application development sprint, we're going to add a function where we are tracking active ETFs that are of interest to the team.
And we are going to be tracking the day over day financial ratios for all of the watch list companies, which should take the form of a Bloomberg poll on those securities.
Now, there are two things that trigger what I would call a flag here.
The flag can be triggered by a 20% change in some key financial metric, which we are tracking.
The list of that is forthcoming.
The list of relevant financial metrics.
And also, if there is a significant movement in the holdings, either a new addition, a big divestment of in one of those active ETFs that also the details of that are forthcoming.
The plan for this is that as these flags occur, we will have a teams group, which the Opal AI, the Opal Analyst AI, will send out a message of some flag, something that's happening.
And if it's a security we don't already track, we will have the option to include it into the Opal Data Harvest pipeline.
The Opal Data Harvest is the centralized infrastructure that facilitates all these downstream applications.
So, as you can see, on one side, we have the ingestion function for the backfill.
We're going to be pulling all of that SharePoint Asset Management Research Earnings Reports.
Our initial deliverable, which is to be able to make the export that comes out of the security analysis dashboard tool,
will be an earnings report analysis report that fits that description, that fits that kind of format.
Obviously, the second is going to be a user-facing tool that uses the Opal Analyst to track notable moments, flags one and two,
which offer the group channel members the opportunity to add new securities to that Opal Data Harvest.
There is a third application, which will be a function of tracking a calendar of all universe securities.
I think we should get an IEFA, IEFA, ETF calendar to track all of the earnings reports to know the calendar of when those things come in.
Because as they come in, we are going to want to run their whole Opal Data Harvest for that security.
We're going to want to run them.
Thank you.
----- END TRANSCRIPT -----
