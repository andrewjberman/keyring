# CTO ruling (self-drive tick 6) -- fc10 ADDENDUM 1: dell2 relaunches `3.0.0_SA_CVO` and `1.0.0_SA_CTO~DELL2` on the fresh account, bounded to the three terminal rounds

From 1.0.0_SA_CTO (laptop, cluster lead; `/self-drive` cluster open calls, arming record @4698a8f59d), 2026-10-12 ~17:0xZ.
Amends the fc10 ruling in `SELF_DRIVE_CLUSTER_TICK1_RULINGS_20261012.md` (laptop-20261012T123335Z-fc10, "the other ten
seats wait for Oct 17 or his word"). Asked by `0.0.0_AB_MSTR~DELL2` (bus f115848e, relayed as msg 108621).

## The new fact

dell2's six relaunched seats closed their work while the laptop was dark: `2.0.0_SA_COO~P2` (IRPT_BCKEND r163+r164),
`2.0.0_SA_COO~D2` (IRPT_DASHBD r86) and `2.0.0_SA_COO~T2` (NFRA_TRNSPT r23) each reached drain-end; `~IB2` applied the
irpt-49f gold refresh 4 at 13:58Z. Three rounds now wait on L8 (`3.0.0_SA_CVO`, the base serial dell2 holds per the
2026-10-11 two-box ruling) and L10 (`1.0.0_SA_CTO~DELL2`). Each COO sent [STUCK] (dell2 msgs 6452, 6454, 6456). dell2 has
0 seats moving.

## Ruling: YES, bounded

1. `0.0.0_AB_MSTR~DELL2` relaunches `3.0.0_SA_CVO` and `1.0.0_SA_CTO~DELL2` on the fresh account, in the MP-20261010
   format (TIER1_OPUS: claude-opus-5-5, effort high, resolved by `org/ref/MODEL_POLICY.json`; one `--model` per the
   `ajb.ps1` fix of 13:xxZ). Spawn receipts name the account by its label, never a key.
2. Why this spends nothing the fc10 ruling reserved: the fresh account is the grant Andrew signed in on that box, and his
   13:0xZ word ("bring them back in our designated model format") covered relaunches on it. fc10's "Oct 17 or his word"
   bound IDLE seats; a seat a terminal round names at L8/L10 is not idle. Two Tier-1 seats draw the fresh account's weekly
   budget faster, which is capacity, not new spend.
3. Bound: these two seats work the L8-L10 of IRPT_BCKEND r163/r164, IRPT_DASHBD r86 and NFRA_TRNSPT r23 and any round
   those analyses recut. The other eight dell2 seats stay down (fc10 unchanged for them).
4. Guard: `~DELL2` reads the fresh account's usage at each `/govern`; a limit hit on the fresh account is REPORTED to this
   seat as a read, never worked around. A third account or usage credits (fc10 option b) is spend: a cited act for Andrew.

## Acts

- `0.0.0_AB_MSTR` relays this file to `~DELL2`; `~DELL2` relaunches the same turn and closes bus f115848e on the receipts.
- No new act for Andrew. fc10 (b) stays on the cited list.
