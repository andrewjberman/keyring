# Andrew-direct 2026-09-22 -- delete confirmed; 0.0.3_BG_BBGTerminal becomes a microproduct in its own repo `opal_analyst`; OPLGTW and MCPINDEX to be modular and templated; D9 moves to site Z

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal (site Z), before any act on it. **Channel:** Andrew, direct, in
this session, answering the report on the device's gateway MCP setup.

## Verbatim, entire

> You have my word on the delete. Regarding 0.0.3_BG_BBGTerminal agent, that whole thing is going to have to become a
> microproduct; it should not live inside the ajb_workspace repo. We are going to want to make a new repo explicitly
> devoted to that project, I'd call it "opal_analyst". It can be a submodule of ajb_workspace like the Portal, but it
> is getting to a point where we are going to need to make a modular version of it and a modular version of the
> OPLGTW and MCPINDEX because this is going to be explicitly productized, and all of it needs to be refined and
> templated. We are actually going to be moving D9 over to sitez shortly because there is more compute on this device
> to handle the D9 workstreams than on the laptop device. Relay that message about D9 to MSTR~Z, and then let's begin
> assessing the implementation of the OPLGTW, MCPINDEX, and What I'm discussing with you about templating the
> function of the teams agent, which in the Opal case is the Opal Analyst, currently rendered as
> 0.0.3_BG_BBGTerminal.

## Reading, narrow

1. **Delete: his word is given** for the untracked working-tree folder `infra/aws/ec2/m365-mcp-gateway/` on this
   device (the one this seat put to him). Nothing else is covered by that word.
2. **`0.0.3_BG_BBGTerminal` becomes a MICROPRODUCT in its own repo, named `opal_analyst`**, wired as a submodule of
   `ajb_workspace` the way `portal/` is. It "should not live inside the ajb_workspace repo".
3. **A modular, templated version is wanted of THREE things:** the Teams agent function (the Opal Analyst), OPLGTW
   (the Opal Gateway, `NFRA_OPLGTW`) and MCPINDEX (`NFRA_MCPINDEX`) -- "explicitly productized ... refined and
   templated".
4. **D9 moves to site Z "shortly"**, because this device has more compute for the D9 workstreams than the laptop.
   He asks that this be RELAYED to `0.0.0_AB_MSTR~Z`. Relay, not adjudication: the timing ("shortly") and the
   mechanics are his and MSTR's.
5. **Asked of this seat now:** begin the ASSESSMENT of the implementation of OPLGTW, MCPINDEX and the Teams-agent
   function, toward templating. An assessment (read-only) first; the repo carve-out and any move are later acts on
   his word.
6. **Not asked:** creating the repo, moving files, changing a submodule, or cutting any cell. No L2+ route is
   assigned here; that is `1.0.0_SA_CTO~Z`'s.
