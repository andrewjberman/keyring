# ANDREW_DIRECT 2026-10-21 ~15:35Z -- the gold master attributes accounts by CUSTODIAN-NATIVE grouping id

- Channel: in-session, Claude Code terminal, dell1, to 4.0.0_SA_CRO~FIDELITY. ~15:35Z (11:35 AM ET). Follows NFRA_FIDSLVR L1 delivery.

## Verbatim
> Yeah I think what would need to happen in the gold master is that we'd have to use the "G Number" from Fidelity and the "Master
> Account Number" from Schwab to be in some mapping config so that we'd be able to parse who is who at the Custodial level rather than
> rely on downstream data vendor inputs to assign accounts to advisors.

## Design directive (gold layer, NFRA_FIDSLVR O3)
The master gold layer attributes every account to its advisor/firm from the **custodian-native grouping identifier** -- Fidelity's
**G Number**, Schwab's **Master Account Number** -- held in a **mapping config** (`(custodian, native_group_id) -> advisor/firm`). This is
the source of truth for account->advisor attribution, REPLACING any downstream data-vendor assignment. Attribution is resolved at the
custodial level, upstream of vendors.
