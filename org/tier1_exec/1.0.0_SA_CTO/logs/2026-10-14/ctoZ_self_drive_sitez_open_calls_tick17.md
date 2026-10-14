# SELF-DRIVE sitez open calls -- tick 17 (2026-10-14 12:50Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 17 (since tick 16 @554186a189, 11:51Z). **state: ARMED**

## Measurement
- Inbox: 0 unread at tick time (messages since tick 16 read and acked: 34041, 34045, 34050, 34051, 34057, 34060, 34062, 34068).
- `open-calls.py list`: boxes=1, rows=45, **open=7**, all person acts with citations (unchanged since tick 16):
  MC Portal sitting (21d9, 21c5, 8ed7, f0d2); Alyssa FWD-1 sitting (def4, 3b41 duplicate, both CROSS-BOX); Teams message to the Opal Bloomberg account (a519).
- No new call rows; no governance or design forks pitched.

## Driver acts since tick 16
| act | carrier |
|---|---|
| Site Z joins MP-20261010 model policy (Andrew-direct) | @b03d97ac20; relaunch census by MSTR~Z: 9 of 15 claude.exe request sonnet-5-5 (msg 34068) |
| OG-hv-2 role correction (CVO row Z-S107): PRD v2.8 wording to gateway-global-internal-reader-role | @7f90a792ea; COO~O amended the order @ff91700f3b (verified; msg 34057 answered) |
| NFRA_CTLPLN-Z-S8 (6 CloudOps lanes exited without a KILL line): disarm_owner re-pointed to 0.0.0_AB_MSTR~Z (infrastructure, rule 32) | msg to MSTR~Z re 34060 |
| Andrew-direct gateway data-contract census: record + directive to 4.0.0_SA_CRO~Z (six bucket groups, per-table JSON contracts; G1 harvest due 20:00Z); MCPINDEX round 13 now cuts from the per-group addendum (msg to COO~MI) | @06ae2a3485 |

## Verdicts received
None (no CVO verdicts this window).

## Completion test
Scope is the box's open calls (no directive member set). NOT DONE: 7 open, every one a person act; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting -- human look + Opal Bloomberg login (21d9 covers 21c5, 8ed7, f0d2); citation: TO-MP-z-6 / TO-MP-v-2 G-2ND (a login is his).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate); citation: TO-MP-c-2 (a person sitting).
3. One Teams message from his account to Opal Bloomberg (a519); citation: his own send, answered "later" 10-10.

## Compiler Tools
`.tools/open-calls.py list`; broker check_inbox/ack_messages; `git log`; `safe-commit.sh`.
