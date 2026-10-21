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

## COO finding ~17:45Z (msg 9187, FIDUPL_schwab_household_finding_20261021.md @41fa1eeff4) + design implication

**Correction to the earlier .fam claim:** "Schwab has no household table" held only for master **08242234** (the one the CRO checked).
Master **08335338 DOES carry `fam` (stale 2026-08-10) and `slm` (live)**. The Option B decision stands regardless (fam is stale, slm is
per-taxpayer not per-family, and households span advisor groups -- see below), but the clincher was overstated: it is now "no CLEAN,
current family grouping," not "no table."

**What Schwab actually has:** `slm` col_6 = the account **TIN** (7,589/7,589 cottonwood), i.e. per-taxpayer, not per-family. `tcf/tcfx/tnn`
= confirmations + 1099s, no grouping. Master Account Number is one value per account file; accounts sit under several masters (7,589
shared -> a double-count hazard if a master is treated as a household).

**Households are synthesizable:** 4,471 TIN-households over 7,638 open accounts (~3,432 by the CRO household rule).

**DESIGN IMPLICATION (feeds the PRD):** firm/advisor **attribution** and **household** are TWO SEPARATE dimensions -- 90 households span
>1 advisor group. So the gold config models them separately: (a) firm-attribution config keyed by custodian-native grouping id (G Number /
Master Account Number); (b) a household dimension keyed by TIN on Schwab and by native Groups on Fidelity. Not one key. Surprise D1-S19 filed.
