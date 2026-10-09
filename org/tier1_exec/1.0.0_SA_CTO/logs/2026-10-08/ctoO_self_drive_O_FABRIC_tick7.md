# 1.0.0_SA_CTO~O -- /self-drive 30m ~O fabric, tick 7 (2026-10-09 00:53Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_215xZ_SELF_DRIVE_30M_O_FABRIC_FOUR_PROJECTS.md`
@ba8c4598fb. Cron d7c133e4. `state: ARMED`.

## Scope

| project | status | dep_stage | open TOs | sequence flags |
|---|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 4 | - |
| NFRA_OPALAI | active | EXECUTING | 3 | - |
| NFRA_MCPORTAL | active | EXECUTING | 2 (MP-c-1, MP-v-1 staged; CVO~Z compile @5f75be7187, L10 precondition NOT MET @110c291f33) | UNPLACED |
| NFRA_MCPINDEX | active | EXECUTING | 1 (row Z-S84 inert, @248f3efc04) | - |

Inbox: 0 unread (32170, 32180, 32183, 32187, 32193, 32195 acked).

## Since tick 6

- OG-bf-1: CTO half SIGNED on option W (08242234 only) @f9b1f1fd31; COO half @35ca8013bb; Phase B amended @8f0b2e4660.
  08335338 HELD; option Y RULED: NFRA_OPLGTW owns the dispatcher change (precedent OG-m-2a @c064389bab); the accelerator
  branch SKIPS a qualified marker whose date is not the production T-1 from `lib/trading_calendar.py`.
- Laptop CTO (msg 107523, relay 32180): Black Diamond Tax fields live in Cottonwood BD silver; the gateway read is ruled
  allowed, account-allowlisted, read-only, never joined across firms. Matches PRD v2.1 item 3; no change.
- CORRECTION: Andrew-direct ~00:4xZ (@6938d82aad): "Gateway is signed in, why did you ask this?" This seat had listed the
  `opal-gateway-bbg` sign-in as owed by him for four ticks, carried from `ROUND_ANALYSIS.round31.md` section 5 without
  measuring the token. Struck. r29's R55 sign-in precondition is MET; COO~O told to cut OG-rl-15 when its items drain.
- WITHDRAWN: this seat's ruling 32186 (sequence the BG seat's --strict-mcp-config after a grant). Andrew's "adjudicated by
  the CTO internally" was said to 1.0.0_SA_CTO~Z, whose fabric runs that seat; its ruling 32189 stands, with
  0.0.0_AB_MSTR~Z's spec fix (a BG-only config naming exactly three servers). Msgs 32196/32197.
- Bloomberg principal (COO~O diagnosis, msg 32195): the 5/5 denial is `identity_scope.check`; the seed's `opalbloomberg`
  row holds 11 tools, none of the five. Remedy = 5 rows in `infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt`, whose
  header reserves widening to Andrew (PRD 4.3). Put to Andrew at this terminal.

## Proposed skill fix (lessons go to gates or skills, not memory)

`/self-drive` Step 1's cited-act list: an Andrew-only act carries its citation AND a fresh measurement this tick that it is
still owed (for a sign-in: the token's live state). Owner: the skill's owner seat; this seat proposes, does not edit.

## Open calls in scope

No open calls in scope (tick 7) other than the Andrew act below.

## Acts only Andrew can do

- Widen the gateway identity allowlist for the Bloomberg account by five read tools (opal_discover, opal_describe,
  blackdiamond_list_fees, find_sharepoint_site, search_files). Citation: `identity_tool_allowlist.txt` header, "Widening is
  an Andrew ruling only (PRD 4.3)". Measured this tick: 0 of the 5 allowed (COO~O offline repro, msg 32195).

## Completion test

NOT DONE: 0 of 4 `status: complete`. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `sequence-check.py --project` x4, `to-check.py --all --project` x4. Worked. Gap: the memory hook refuses a lesson file
  from a seat (by design); the lesson is carried as the skill proposal above.
