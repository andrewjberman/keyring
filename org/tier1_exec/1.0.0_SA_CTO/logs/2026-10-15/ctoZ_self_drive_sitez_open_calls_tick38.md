# SELF-DRIVE sitez open calls -- tick 38 (2026-10-15 09:51Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 38 (since tick 37 @cf06cf8c43). **state: ARMED**

## Measurement
- Inbox: 0 unread (acked since tick 37: 34405).
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Calls ruled and acts since tick 37
| item | ruling / act | carrier |
|---|---|---|
| COO~MI 34405: widen F1 past the 24 firm-valued rows? | YES: the 93 single-clean-firm rows in the next round, after the 24 are live and the difference control reads 0, with their own never-widen pair; the three-firm taxsma row stays Opal-internal (no guessed firm) | msg 09:37Z; recorded at R17.3a `d57e9af469` |
| OG-ap-20 never-widen (five ETF tools + mdpf_get_category_views + one ETF grant) | CTO half SIGNED at `06cfb6db64` on `1b18b94979`. Conditions before GO: Z-S141 (AC1 script fixed and re-graded), Z-S142 (naming gate on the release in ENFORCE; the sentinel added to release cones). The Z-S139 window is corrected to 10 min 25 s from CloudTrail; the ruling stands | @d53b7dbba1; msg 09:55Z |

## Landed since tick 37 (measured from commits)
- OG-rv-1 drained: five rival-fund tools (A) (`be90fc548d`).
- MCPINDEX round 17 issued (`2d9d5c4503`): MX-c-18 (T1), MX-c-19 (F1, 24 rows), MX-r-14 (release); R1 held on OG-ap-20.

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).

## Compiler Tools
`.tools/open-calls.py list`; `git diff --stat`/`git show`; broker; `safe-commit.sh`.
