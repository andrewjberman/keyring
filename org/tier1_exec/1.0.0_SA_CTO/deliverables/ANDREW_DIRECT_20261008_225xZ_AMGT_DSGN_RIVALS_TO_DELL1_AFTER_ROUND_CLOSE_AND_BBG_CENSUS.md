# ANDREW-DIRECT 2026-10-08 ~22:5xZ -- AMGT, DSGN_AMGTV1 and ETFS_RIVALS move to DELL1, after round close, push, and a BBG-dependency census

**Channel:** the `1.0.0_SA_CTO~Z` terminal, site Z. Two messages, minutes apart, recorded the same turn by `1.0.0_SA_CTO~Z`.

## His words, VERBATIM

**Message 1 (~22:5xZ):**

> "Another thing I want to handle with you, is that I think all the AMGT work should go to DELL1. That means AMGT_CORPUS RESAPP
> HARVST and also DSGN_AMGTV1. I think we can also put ETFS_RIVALS over there as well. Let me know if I'm forgetting anything, but I
> would like to get that done and that leaves us more bandwidth here to focus on NFRA and heavy ops-focused workflows."

**Message 2 (~23:0xZ, sent while this seat was measuring):**

> "I think we need to first have whatever current round the related agents are on make sure that they get everything committed and
> pushed at the end of their round to the relevant repo branches, then those need to get pushed/merged into PROD or CLOUD depending
> on the repo. Once that is done, I think we need to effectively identify if there are any aspects of those processes that are tied
> closely to BBG pulls whereby there is some dependency or local function that depends on the morning BBG pulls. If their
> dependencies on BBG can be handled from the DELL1 device (which they really should be, that should not be an issue), then we are
> 100% clear. If not, then we need to assess how to bridge the gap as needed."

## Scope as worded (not widened, not narrowed)

Projects named: AMGT_CORPUS, AMGT_RESAPP, AMGT_HARVST, DSGN_AMGTV1, ETFS_RIVALS. Destination: the DELL1 fabric. Purpose in his words:
site Z keeps "NFRA and heavy ops-focused workflows". He asked whether anything is forgotten; candidates are surfaced to him, never
added on this seat's own reading.

## Order, as he gave it

1. Each related seat ends its CURRENT round, then commits and pushes it to the relevant repo branches.
2. Those are pushed/merged into CLOUD (the workspace) or PROD (the portal), per repo.
3. Then a census: every process of these projects tied to the morning BBG pulls, or to any local function on this box.
4. If DELL1 can serve each such dependency, the move is clear. If not, a bridge is assessed for that gap.

The fabric re-placement of the five tree rows (`fabric`, `coo_lane`, seats) comes after step 4. This record changes no carrier by
itself.

## Carriers this record binds when the move executes

The five `project.json` tree rows (`fabric`, `coo_lane`, `seats`) and the generated index (`derive --write`), which `1.0.0_SA_CTO~Z`
writes as their L3 owner. Then `org/ref/LIVE_ARMS.md`: this seat's `/self-drive` row, whose scope is exactly these five, and
the four COO `/canonical-drive` rows. A cross-fabric act goes MSTR to MSTR (CLAUDE.md rule 32): `0.0.0_AB_MSTR~Z` to
`0.0.0_AB_MSTR~DELL1`, with `1.0.0_SA_CTO~DELL1` taking the projects.

-- 1.0.0_SA_CTO~Z
