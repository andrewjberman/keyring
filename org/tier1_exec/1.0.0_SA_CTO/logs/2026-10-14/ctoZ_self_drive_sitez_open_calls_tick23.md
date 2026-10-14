# SELF-DRIVE sitez open calls -- tick 23 (2026-10-14 18:52Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 23 (since tick 22 @49ef0ae5be). **state: ARMED**

## Measurement
- Inbox: 1 unread at tick time (34188, read and acked); also acked since tick 22: 34165, 34171, 34174.
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Calls ruled and acts since tick 22
| item | ruling / act | carrier |
|---|---|---|
| Relay 34165: Andrew's four priorities (P2 Ticket Center Oct 24, P1 Investor Reporting Nov 15, P3 Advisor Intelligence before Dec 1, P4 OPLGTW/MCPINDEX secondary; MC Portal finish then close or hold) | passed to COO~O and COO~MI (P4 unchanged, Friday target stands) and COO~MP (finish the R1+F2+U2 round, then close or hold) | msgs 18:14Z |
| COO~O 34171: naming gate refuses legacy platinum/ keys in gateway code and Terraform | no gate edit: code reads keys from the catalog rows; Terraform uses the existing legacy_addresses branch (committing project derived from a project-home path staged with the .tf); grant prefixes carry no firm token | msg 18:29Z |
| COO~O 34174: G2 cannot all land by Friday | staged cut accepted; Friday = G1, G3, G5 wave A, G6 (+ Schwab if it fits); G2 order Schwab first (existing role) | msg 18:30Z |
| **Andrew-direct ~18:3xZ**: "We can allow 49F Black Diamond pulls from opal-data-bd" + the target layout (BD 49F into opal-data-assets/blackdiamond; 49F gold in opal-data-49financial, LGIC_NAMING form) | recorded; OPLGTW v3.6 / MCPINDEX v0.15 (49F BD adapter reads opal-data-bd via its own scoped role; G2 order Schwab, 49F BD, Orion/Inflection, BD Cottonwood, SmartX, Commonwealth); target layout relayed MSTR to MSTR (dell1 ADVI_FIRMBKTS) | @6d6702425a; msgs 18:50-18:51Z |
| Relay 34188: Andrew, ETFS_RIVALS done, backfill to MDPF_DEMQUE (dell1) | noted; no site Z act (G5 wave B reads the rival gold tables, which keep flowing) | -- |

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).

## Compiler Tools
`.tools/open-calls.py list`; `git fetch` + `git show` (CLOUD records); `.tools/naming-gate.py` (read); broker; `safe-commit.sh`.
