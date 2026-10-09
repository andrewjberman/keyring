# 1.0.0_SA_CTO~O -- /self-drive 30m ~O fabric, ticks 13-14 (2026-10-09 03:5xZ, 04:21Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_215xZ_SELF_DRIVE_30M_O_FABRIC_FOUR_PROJECTS.md`
@ba8c4598fb. Cron d7c133e4. `state: ARMED`.

## Scope at tick 14

| project | status | dep_stage | open TOs | PRD |
|---|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 8 | v2.3 ADMITTED |
| NFRA_OPALAI | active | EXECUTING | 3 | -- |
| NFRA_MCPORTAL | active | EXECUTING | 4 (MP-x-3 applied and drained @edf50ff4d3) | -- |
| NFRA_MCPINDEX | active | EXECUTING | 1 | v0.7 WITHHELD: cure @3c7ff0684b resubmitted to 3.0.0_SA_CVO~Z |

Inbox: 0 unread. Acked: 32335, 32337, 32341, 32352, 32355, 32357, 32361.

## Andrew-direct words recorded at this terminal (verbatim in each record)

| time | record | words |
|---|---|---|
| ~03:2xZ | `ANDREW_DIRECT_20261009_032xZ_BLOOMBERG_ACCOUNT_GETS_BLACKDIAMOND_LIST_FEES.md` @e728c77fc6 | "yes, include blackdiamond_list_fees for the bloomberg account too" |
| ~03:2xZ | `ANDREW_DIRECT_20261009_032xZ_OPAL_GATEWAY_BBG_MIRRORS_OPALGATEWAY.md` @4fb7326f67 | "opal-gateway-bbg should be an exact copy of opal-gateway for now ..." |
| ~03:3xZ | `ANDREW_DIRECT_20261009_033xZ_BBG_CONCIERGE_OPAL_USERS_ONLY_GATE.md` @39f5404132 | "it should only accept inquiries from opal capital users however ..." |

## Driver acts

### NFRA_OPLGTW PRD v2.3 (@4fb7326f67, item 4 @39f5404132), ADMITTED

- `opalbloomberg` mirrors Andrew's principal: it is unscoped and holds the same grants. This supersedes v2.2 item 5 and
  reverses v2.2 item 2's narrowing.
- Item 4, the Opal-users-only gate:
  - the Teams reads drop any sender whose Entra UPN is not `@opalinvest.com`;
  - the sends refuse a mixed chat;
  - the gate ships with the mirror, or neither ships.
- 2.0.0_SA_COO~O moved every Bloomberg-account change out of r29 (OG-rl-15 A6 @38f240bdab), so the mirror and the gate
  ride r30 together.
- The sender-identity field is to ship first, since it unblocks the BG seat by itself (msg to COO~O ~03:4xZ).

### The BG seat (1.0.0_SA_CTO~Z's lane)

- bbg-teams-assist step 0b sender gate landed @ef8c4e57a1. It failed closed, because the poll returned only `from_name`.
- Amendment 1 @0c9fbd0876 passes a sender only on `userIdentityType aadUser` plus Opal's tenantId, and refuses `#EXT#`.
  The seat serves Opal users again.
- The gateway UPN gate stays the authoritative check.

### NFRA_MCPINDEX

- Andrew-direct ~03:2xZ (@5716c7a83d) reads "there is a lot of indexing work to be done".
- The 4.0.0_SA_CRO~Z brief @3455b1783a lists 29 candidate entries.
- PRD v0.7 @b06af7c0d2 adds FWD-11 to FWD-18; FWD-11, the thread, is model performance routed to the served answer.
- 3.0.0_SA_CVO~Z REFUSED it (msg 32355, review @a1eeaf814a): three ENDPOINT ACCEPT clauses still stated the old rule.
  The cure @3c7ff0684b amends FWD-1, FWD-8 and FWD-9 in place, and it is resubmitted.
- 2.0.0_SA_COO~MI was told not to close the project, and to decompose now and issue once the half is signed.

### Box-sync

- 0.0.0_AB_MSTR~Z held the box-sync (msg 32357) on this seat's mid-edit PRD.
- That path is committed and clean, and MSTR~Z was told.

## Open calls in scope

None (ticks 13-14).

## Acts only Andrew can do

None owed.

## Completion test

NOT DONE: 0 of 4 `status: complete`. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `to-check.py --all --project` x4 and `prd-signoff.py status` x2 worked.
- Gap: none.
