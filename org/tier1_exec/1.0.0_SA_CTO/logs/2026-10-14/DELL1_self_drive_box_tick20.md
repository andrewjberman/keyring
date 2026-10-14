# /self-drive dell1 box open calls -- tick 20 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~18:26Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17). **state: ARMED**

## Measured

- **Box list:** rows=77, **open=2**, both client-facing approvals HELD for Andrew (`c822`, `6e63`).
- **Cross-adjudications:** 17 of 17 RULED.
- **Inbox:** 0 unread. Msgs 5655, 5673 and 5677 since tick 19 were acked and acted on.

## Acts since tick 19

| item | ruling / act | record |
|---|---|---|
| MSTR 5655: Andrew's four priorities (laptop CTO msg 109202) | Read from CLOUD: `ANDREW_DIRECT_20261014_173xZ_DELIVERABLES_FOUR_PRIORITIES_AND_DATES.md` and `PLAN_20261014_DELIVERABLES_BOX_ORGANIZATION.md` @5ad9a6e07f. The dates are P2 Ticket Center Oct 24, P1 Investor Reporting Nov 15, P3 Advisor Intelligence before Dec 1, and P4 OPLGTW/MCPINDEX secondary. **No box move and no secondary hold were made by this seat:** the plan's asks are Andrew's. P3 groundwork that moves no box was started | msgs to MSTR~DELL1 and CRO~DELL1 |
| P3 Oct-17 milestone (read-only, CRO~DELL1) | **The note landed** (@cfc1cf4714). Cottonwood's "portfolio group" is the ADVISOR BOOK (4 values), not the client map. Clients map to portfolios through the BD rebalancer `strategy_name` (56 strategies). Defects: `silver/account_attributes` has stalled since 08-20, and the join key is `external_id`. Q-A to Q-C went back as measurements: the writer by code, the schedules graded in trading days, and the secret's metadata only | `org/tier1_exec/4.0.0_SA_CRO/deliverables/P3_COTTONWOOD_BACKEND_CENSUS_AND_PORTFOLIO_GROUP_20261014.md` |
| `~J1` 5673: J359 satellite producer pair | **NOT signed.** There is no COO half file, and the package moves more than the spec. The deployed copy of `etf_positioning_gold.py` dates from `102b2b29d3`; `compute_returns` has changed since (AST hash ae3fdd65 -> 927fe225, C-GAP and C-MMF); and the branch carries SH-t-24 (held, but `frontier_returns` is not called). Owed: a drift table, the tickers-block arm as the proof, the writer N, the IAM line, and the client-facing note | msg to `~J1` |

**Information for Andrew, no decision owed:** his portfolio-group question is answered by the P3 note. Cottonwood's portfolio group is the advisor book; the
client-to-portfolio map is the rebalancer strategy.

## Completion test

Box scope: **NOT DONE**. The stop is Andrew's stand-down. REACHABLE calls 0; 2 HELD for acts only Andrew can do.

## ACTS ONLY ANDREW CAN DO (cited)

The tick-18 list stands (`DELL1_self_drive_box_tick18.md` @f9baab8e69). Added from the laptop's plan, each his by its own terms: yes or no on the two box moves (TCKT_VNEXT
trade and meeting to the laptop; a dell1 seat lent to P1), the trade-request form, and Jeanette's mailbox spelling. Those asks are carried by the laptop CTO, not by this seat.

## Compiler Tools

`git show origin/CLOUD:<path>` (the records read before the box pass); `git merge-base --is-ancestor` (SH-t-24 in the J359 branch); an AST hash of named functions across two pins
(`compute_returns` drift). **Worked:** the per-function AST hash found the windows-rule change that a file-level diff would only call "differs".

-- 1.0.0_SA_CTO~DELL1
