# `/self-drive 30m` every site-Z project -- ticks 2-3 (2026-10-09 ~08:48Z to ~09:3xZ), `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_SELF_DRIVE_30M_EVERY_SITEZ_PROJECT.md` @4752d8dfcc.
Cron `fff05062`. Previous log: `ctoZ_self_drive_SITEZ_ALL_tick1.md` @7f4072125a. **state: ARMED.**

## Scope

7 non-terminal SITEZ-placed projects (2 closed at tick 1): COMM_ASSIST (~ZZ), NFRA_IAMROLES202609 (~ZI), NFRA_MCPINDEX (~MI), NFRA_MCPMSP (~MS),
NFRA_MCPORTAL (~MP), NFRA_OPALAI (~AI), NFRA_OPLGTW (~O). **Completion test: NOT DONE**, 2 of 9 closed.

| project | REACHABLE? | why |
|---|---|---|
| NFRA_MCPMSP | **UNREACHABLE (G-MSPID)** | round-3 analysis @2016db240c: enrichment list EMPTY, every remaining FWD waits on the MSP calling identity |
| the other six | REACHABLE | each has a live COO and a next act |

## Acts and rulings

| item | ruling / act | carrier |
|---|---|---|
| NFRA_OPALAI UB-9a05 (CRO approach) | FOLDED: step 4 runs now, J2 pinned to arm (a)'s minute; withdrew my own msg 32432 "after r29" | @f200ec49f6, CVO~Z signs |
| UB-9a05 step 4, fixed first prompt (COO~AI 32600) | YES as built; close the Analyst after the gate reads so it never double-serves Teams beside the BG concierge | msg 32603 |
| step-4 result (MSTR~Z 32613) | GATE PASS, no sign-in, but the positional first prompt never runs under Opal_Agent: Z-S63 is NOT fixed live. Routed to COO~AI as its round's repair before r29 | msg to COO~AI 09:19Z |
| SECHIST-Z-S1 disarm (dell1 H1 via MSTR 32596) | delivered to `0.7.0_AE_CloudOps~Z` as information (LD-0529 admits it) | 09:02Z |
| COMM_ASSIST round 11 slug (32599) | round 12 = the FWD-4 deploy pair after r29's commassist secret, naming the round-9 code it ships; a FWD-3 cell only if tonight's count fails | @4c14e95965 |
| NFRA_MCPMSP round 3 slug (32617) | EMPTY list; HELD on G-MSPID | @2016db240c |

## Never-widen halves signed

AMGT_RESAPP hh-3 @7537de8e1d (3 files, test_document 32 passed); NFRA_MCPORTAL MP-k-2 @b94c8e0f8a (re-pointed from CTO~O; live: 20 inline
policies, the new one absent, `requests/` PutObject simulates `implicitDeny` today).

## Acts only Andrew can do (cited)

- **G-MSPID** (NFRA_MCPMSP): the MSP calling identity and its MFA sign-in. Decomp G-MSPID/G-MSPCL; "Not yet" 2026-09-30, "doesnt matter right
  now" 2026-10-01. Not asked again.
- **Barron's sign-in** (AMGT_HARVST, open call `sitez-20261008T231757Z-9f24`): his login; his words "We can handle Barron's sign in any time".
- **Forced removal of two drained MCPORTAL worktrees** (call `sitez-20261009T083926Z-84ef`, HELD): a recursive delete of untracked `.scratch/`
  (CLAUDE.md Agent Autonomy). Both heads contained in box/sitez.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `open-calls.py list`, `unblock.py list/show/fold` | PASS | fold recorded; CVO~Z signs |
| `git archive` + pytest | PASS | hh-3 test_document 32/32 |
| `iam list-role-policies`, `simulate-principal-policy` | PASS | before-state read for MP-k-2 |
| `Get-ScheduledTask` + EncodedCommand decode | PASS | confirmed DQ-t14's C1/C2 on the live task |
| `send_message` to a Tier-2 seat | WORKED AS BUILT | an information-only notice passes LD-0529; an act does not |

-- 1.0.0_SA_CTO~Z
