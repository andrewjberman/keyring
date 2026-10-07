# ANDREW-DIRECT 2026-10-06 ~20:1xZ -- the Bloomberg no-modify order covers the Positioning pipeline and ETFS view operations; research is outside it

Channel: typed by Andrew at the `1.0.0_SA_CTO~Z` terminal (Claude Code session), ~20:13Z (4:13 PM ET). It answered this seat's
`/open-calls` card: "Does your 'do not modify integrations/bloomberg/' order cover integrations/bloomberg/research/model_block_pull.py?
(a) no ... (b) yes".

## VERBATIM

> Research is outside it, yes. What i wanted to avoid with this process was accidentally overwriting any operations in the
> "Positioning" pipeline and ETFS view operations. Research is outside of that edict. if there is an opportunity here to improve
> research is open season, your discretion on that basis is accepted, and you have egress.

## What it settles (as written)

- The no-modify order on `integrations/bloomberg/` protects the "Positioning" pipeline and ETFS view operations.
- Research is outside that order. `integrations/bloomberg/research/` (the AMGT model-block pull) may be modified.
- Improving research is at this seat's discretion ("open season, your discretion on that basis is accepted").
- "you have egress" is recorded as said. This seat reads it as egress for that research work, at this seat's discretion. It has
  not been read wider than research.

## What it unblocks

`org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND39_AO2_CTO_HALF.md` flips from HELD to SIGNED.

## Unchanged

The order still stands for the Positioning and ETFS-view files (`integrations/bloomberg/pipeline/`, the vehicle and the sign-in
scripts), per call 5 of `ANDREW_DIRECT_20261006_1818Z_ALL_RECS_APPROVED_MSTRZ_OPEN_CALLS.md`.
