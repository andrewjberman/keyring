# ANDREW-DIRECT 2026-09-22 ~16:3xZ-17:2xZ -- the Claude analysis layer: platinum per security in opal-data-harvest, the equity-research skill lifted, run on top of existing data

| Field | Value |
|---|---|
| Channel | Andrew at the `4.0.0_SA_CRO~F` terminal (site Z), four messages after reading the RCN-0012 briefs |
| Time | 2026-09-22 ~16:3xZ-17:2xZ (the fourth message at ~17:2xZ; `date -u` read 17:21Z at the record's write) |
| Receiving seat | `4.0.0_SA_CRO~F` |
| Scope adjudication | NONE at this seat. Recorded verbatim; surfaced by broadcast. The seat's replies between the messages are in the session transcript and in the L1 brief this record feeds; they are the seat's assessment, not his word. |

## Verbatim, first message

> Now tell me based on your research if there is anything claude API can help us backfill more effectively than the existing opal-data-harvest. My impression is that claude API isnt a data retrieval tool as much as a "send claude in with a few tools to get some excerpts" tool. That is fine, and we can maybe employ that in some analysis layer that displays on the "Security Analysis" page, e.g., Claude for Finance is what assembles those page contents rather than doing it all by python off the data. But that's what I want to spec out, essentially where in the infrastructure there is room for this function. I essentially want to plug any gaps with it, potentially having it run on top of existing data.

## Verbatim, second message

> So What yang provided in the LLY folder was basically a skill that did not use any of claude for finance, it was just open source claude using web search and maybe yang used a skill?

## Verbatim, third message

> Ok so we could basically pull the public Claude for Finance repo, pull the equity analysis skill out of it, and craft a layer that draws against gold jsons for the opal-data-harvest bucket, and make a "platinum" bucket inside opal-data-harvest that will hold a folder for each security we are tracking and basically drop the Claude for Finance "Analysis" json, which will be a structured format that fits the frontend for perhaps "Thesis", any rich text included in the remainder of the tabs (need to assess what that looks like currently if there is a frontend layout/component architecture deisgned already, and likely the "Posture" tab (when we get to that).

## Verbatim, fourth message

> Ok adjust the claude for finance implementation brief based on my notes here. I will then take that brief and run a PRD with CTO from it.

## Verbatim, fifth message (~17:3xZ, after the seat proposed no broadcast yet was needed)

> no need to update other sitez seats just yet

## Verbatim, sixth message (~17:4xZ, on the seat's four message-design questions)

> we need to decide how to craft the message properly first, which is the focus of the brief

## Verbatim, seventh message (~17:5xZ, the four calls and the corpus-scan instruction)

> 1.) Per part. I think this is where we actually design "Posture" tab as well, because Posture should take the per-part analysis outputs and essentially synthesize into a position. I also want to identify in the Sharepoint human-written earnings reports what sections they have consistently, because these should factor into both the per part and synthesized "Posture" analyses outputs. For example, if they have a "why we own this" or some kind of KPI, the analysis should assess the delta on those features as part of its job. 2.) Agreed. The main interest in the historical forms are also design inspiration in terms of how the "Export" should be generated, i.e., using Opal Brand Colors/Guidelines/logos/etc to create a very similar output shape with all of this information + enriched with our new channels which we're bringing into the mix. 3.) Agreed with your rec here. 4.) Rec is fine. Something else I want you to do is scan through those earnings reports and look for those idiocyncrasies per sector/business type (e.g. banks, or insurance companies, particularly). This is important because the shapes we generate should be dictated by how the Opal team structures the models/reports per company/function, this is especialy important for the "Model" function, as we should effectively be looking to bridge the gap from the prior art earnings reports to the new generations in two key ways. 1.) We need to assess sector (and business type in the case of banks and insurance companies) consistencies between the prior earnings reports so that we take that same shape for future inductions to the opal-data-harvest pipeline/database. That means on "Model" we want to typecast "Model" formats (what ratios are they using) and how on a sector-level, so we can better abstract how to structure new inductions into the database in that sector. 2.) For securities that already existed in the database, we need a continuation of how the reports were generated. That means that the pre-existing models, pre-existing theses and etc., we want to use those shapes and build on those concepts. I think this is the proper brief to build that in because here is where we're really focused on the LLM layer so we can properly wield the use of that LLM layer to effectively fill in these gaps as needed.

## Verbatim, eighth message (~18:3xZ, while the brief was being rewritten)

> Yes also it is clear that the backlog set that we want for "Security Analysis" is just every single company listed in the Asset Management/Research/ bucket in the Opal Capital "Shared" Sharepoint. That should probably be mentioned in this brief.

## What the seat reads from it (NOT an adjudication)

- The Claude API is placed as an ANALYSIS LAYER that assembles page contents on top of data the harvest already holds, not as a retrieval or backfill tool.
- The layer's home is a PLATINUM tier inside `opal-data-harvest`, one partition per tracked security, holding a structured "Analysis" JSON that fits the frontend: Thesis first, prose for the remaining tabs, Posture when that tab is reached.
- The public `anthropics/financial-services` repo's equity-research skill is the source of the layer's method (lifted, adapted), not its data path.
- The RCN-0012 threading proposal is to be REVISED into the brief he takes to `1.0.0_SA_CTO~Z` for a PRD -- i.e. an L1 brief, midstream on AMGT_RESAPP, for `/endpoint --forward`.

## Disposition

- Broadcast same turn to `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `0.0.0_AB_MSTR~Z`.
- The revised brief: `docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md` (L1, MIDSTREAM). The RCN-0012 proposal file carries a supersession note pointing at it.
