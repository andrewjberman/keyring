# ANDREW-DIRECT 2026-10-08 ~17:5xZ -- commits go into the graph as metadata; keep building; map the comp-tools

**Channel:** Andrew at the 4.0.0_SA_CRO terminal, laptop, 2026-10-08 ~17:5xZ (13:5x ET).

## The exchange, verbatim

Andrew asked (~17:4xZ):

> The other thing that I think is important regarding the graph, is how does git commits work with it in its current state? Is it more efficient to just have some kind of shared git checkout or is that a surface that would live on the kuzudb projection?

This seat answered that today no commit, branch or box is a node in the served graph. The recommendation was that git
keeps the bytes and the graph holds commit METADATA (commit -> box, seat, project -> the estate thing it touched) as the
fabric layer. A more-shared checkout was not recommended: the seats on one box already share one, and that is where
today's commit stalls come from. The fold-in into the served projection needs a CTO+COO never-widen sign-off and a
CloudOps deploy of the projection worker.

Andrew, verbatim:

> I agree with this, let's continue building accordingly as well as mmake sure that the relevant comp-tools that scan for these things are properly mapped

## Placement (no scope adjudicated)

- Continue the build: fold the activity records into the served graph as a fabric layer. This seat leads, under the
  never-widen sign-off and the CloudOps deploy the rules require.
- Map the comp-tools that scan for these things: `fabric-activity` must be reachable through the comp-tool routing
  (`comp-which`, the tool registry and the graph-call manifest). Every comp-tool that reads the served graph must
  handle the new layer deliberately, either by including it or by filtering it out.
