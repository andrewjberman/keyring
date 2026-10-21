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

## Addendum ~15:38Z (VERBATIM)
> we may not even need the master gold table because you could just construct the necessary tables in gold by the config

Refinement: a standing master gold UNION TABLE may be unnecessary. Because the two silvers are formulated identically, the gold layer can
**construct the needed tables by configuration** -- union the uniform silvers and attribute via the mapping config -- rather than
materialize one bespoke master. Whether gold is a config-driven assembly (views/queries) or a materialized table is a gold-layer/DS
decision at L2/L4; the design does not presume a physical master.

## Addendum ~16:3xZ (VERBATIM): the Schwab household question goes to the COO
> Yes, put the COO on the Schwab household question

Directive: 2.0.0_SA_COO~P1 investigates how households exist on the Schwab side, since Schwab has NO family/household table in silver OR
bronze (measured; feed = acc, rld/rlu/rlw/rly, rps, rtu/rty, sec, tcf/tcfx, tnn, trn, uln/ult, upn/upt). Questions: (1) does any Schwab
feed field carry household/grouping/relationship data (the Master Account Number master->sub structure, or the unexplained tcf/tcfx/tnn
types)? (2) if not, can households be SYNTHESIZED from the Master Account relationships? (3) how does that reconcile with Fidelity's 58
native Groups so the gold household/attribution dimension is consistent across custodians? Output: a finding the NFRA_FIDSLVR config/gold
attribution design consumes. Read-only.
