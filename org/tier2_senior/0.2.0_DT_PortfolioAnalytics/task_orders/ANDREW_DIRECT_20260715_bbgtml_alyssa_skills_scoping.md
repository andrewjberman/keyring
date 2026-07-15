# ANDREW-DIRECT — OPAL_BBGTML: Bloomberg-terminal intake skills for Alyssa (pull -> validate -> /data-refresh upload)

**Channel:** in-session direct (Claude Code session 1d68178d, 0.2.0_DT_PortfolioAnalytics, sovereign-delegate mode)
**Time received:** 2026-07-15 ~15:4xZ (recorded same turn)
**Recorded by:** 0.2.0_DT_PortfolioAnalytics

## Verbatim (message 1)

> Do we have any existing registered project for Bloomberg? What i'd like to do is just set up the
> skills for Alyssa. The premise behind the skills should be a workflow whereby she pulls the
> requisite data with one skill, the data is then validated for cleanliness/expected shape (there
> should never be an issue with this as the python scripts are the same and BBG shape should always
> be the same, but still good to have some light check for duplication and etc.), and lastly the
> data is programmatically sent through the /data-refresh portal channel backend through the m365
> Opal MCP, with confirmation upon successful upload and display. Most of this work is on us to
> realize and entirely in our control, the only things we need Yang for is the retreival py
> scripts, which are in the sharepoint at the following address, quoted from Yang in the paste
> here: [<C:\Users\YangLiu\Opal Capital\Shared - Documents\OCIO Models\Dashboard\202511 Model
> Portfolio Exposure
>
> two python scripts in the folder of "src"
> >]

## Verbatim (message 2, project-code correction)

> register it as OPAL_BBGTML

## Scope (surfaced, not adjudicated)

Three-leg Alyssa skill workflow: (1) one-skill pull running Yang's two retrieval scripts against
the Bloomberg terminal (their machine, their entitlement -- the existing manual workflow,
wrapped); (2) light validation of cleanliness/expected shape (duplication etc. -- shape expected
stable); (3) programmatic send through the /data-refresh portal channel backend via the m365 Opal
MCP, with confirmation on successful upload AND display. Only Yang dependency = the two retrieval
py scripts at the quoted SharePoint path (Shared - Documents / OCIO Models / Dashboard / 202511
Model Portfolio Exposure / src). Registered as OPAL_BBGTML per message 2 (supersedes my earlier
YALP_PKLAUT working name).
