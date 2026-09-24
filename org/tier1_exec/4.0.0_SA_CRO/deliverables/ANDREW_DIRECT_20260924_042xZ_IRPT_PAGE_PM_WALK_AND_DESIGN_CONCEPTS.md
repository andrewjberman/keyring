# ANDREW-DIRECT 2026-09-24 ~04:2xZ -- Investor Reporting page: PM walk, /draw design concepts, then a brief

**Channel:** the `4.0.0_SA_CRO~F` terminal, mid-startup (first message after `/watcher`).
**Received by:** `4.0.0_SA_CRO~F`.
**Class:** DIRECTED scope for this lane. Recon -> design concepts -> brief. Does NOT dispatch.
**Scope:** the portal Investor Reporting page (IRPT_FNTEND / IRPT_BCKEND surface). This is a CRO recon+spec act;
it does not touch the IRPT post-slug HOLD (org/XXX.md Step 1b-F), which binds the CTO/COO canonical progression,
not a CRO design read.

## VERBATIM

> I need you to take on a role play as a "Product Manager" and walk the "Investor Reporting" page and identify all the points that need to be fixed. Random GUIDs everywhere? No holdings list? Clients list in
>   a paginated dropdown that is cut off (this is the worst UI design I have seen in my entire life)? Analysis page has one thousand hashes in the middle of the page. The design on this page is so atrocious
>   in every conceivable way it has to be remediated desperately. I was going to have a separate DSGN project address it but I think it needs a pass or several now to even get it ready to be taken seriously by
>   design team. What I would look at for reference is a handful of references, namely "Model Portfolios" and "Positioning" for the Holdings tab. Model Portfolios fixtures/radials and Positioning Security
>   list with classifications give a clear design framework that the Holdings tab could use. I would say "Advisor Intelligence" client drilldowns and the "Benchmark" tab of "Model Portfolios" provide good
>   frameworks for "Performance". For "Analysis", it is just structurally not acceptable, I feel like you should be able to intuit an infinitely better layout based on the flow which is really just an upload.
>   Maybe what we can do here real quick is you take a look at it as it stands now, look at the data that is being queued up for it, and /draw some design concepts for the header section (this paginated
>   dropdown panel thing is an abomination), for the Performance tab, for the Analysis tab, and for the Holdings tab. I will work with you on the component layout based on the data we want to display, and then
>   you write a brief on exactly what needs to happen to realize that.

Typos and line breaks his, preserved.

## What this lane does with it (surface, not adjudicate)

1. Walk the Investor Reporting page as a Product Manager: enumerate every defect (identity leakage / GUIDs, missing
   holdings list, the paginated client dropdown, the hash wall on Analysis, and whatever else the read finds).
2. Read the data queued for the page (IRPT_BCKEND response shapes) so the concepts are drawn from the data, not invented.
3. `/draw` design concepts: header/client selector, Holdings tab (refs: Model Portfolios fixtures/radials, Positioning
   security list with classifications), Performance tab (refs: Advisor Intelligence client drilldowns, Model Portfolios
   Benchmark tab), Analysis tab (upload-flow layout).
4. Iterate the component layout with Andrew.
5. Write the brief (`/brief-create`) naming exactly what has to happen. The brief is the L1 carrier; nothing dispatches
   from this lane.

## Interaction with standing holds

- IRPT post-slug HOLD (Andrew-direct 2026-09-22 ~15:17 ET at `1.0.0_SA_CTO`): holds CTO analysis / PRD revision /
  next-round issuance on IRPT_FNTEND round 15 and IRPT_BCKEND round 18. A CRO design read and brief are upstream of
  that and are exactly the "alterations" he said he might want to bring in. Not adjudicated here -- surfaced to the
  CTO in the broadcast.
- DSGN: he considered a separate DSGN project and chose a CRO pass first. Recorded as his call.
