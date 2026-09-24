# ANDREW-DIRECT 2026-09-24 ~17:5xZ -- push N1: approved

**Channel:** the 1.0.0_SA_CTO terminal, in reply to the CTO's summary of what the held N1 push moves. **Recorded by:**
1.0.0_SA_CTO, same turn.

## Verbatim

> Push it

Before it, in the same exchange:

> I almost certainly dont care about pushing all of this. I would be interested to know what these modules are, but
> likely would approve the production push wither way.

## What it approves

The CLOUD push held under `org/tier0/ledger/LD-0613.md` Progress 11. It carries the N1 drain: ~P `c6d8b9b2bd`, ~Y
`d8212ee82c`, ~M `14cbdd190b`. Through the pre-push gate it moves three served objects in `opal-data-mdpf`, as the
CTO measured and put to him:

| Key | Change | Rollback (the current served version) |
|---|---|---|
| `code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` | two of its 10 files: `holdings_snapshot.py` (+1,118/-23), `HoldingsSnapshot.schema.json` (+24/-3) | VersionId `Ku6.brgEK.LYO6RIqzXSNdyAM9j_NsCX` |
| `code/scripts/gold/taxsma_membership.py` | 174 changed lines | VersionId `GMs.xhrRBXWFpnU56ab8HEUINLxV7ab5` |

His word stands in place of the ~M/~P never-widen halves ("or Andrew says otherwise", LD-0613 Progress 11). The
push is 0.0.0_AB_MSTR's. The change reaches served output at the next scheduled Holdings snapshot run and the next Tax
SMA membership run.
