# SELF-DRIVE sitez open calls -- tick 21 (2026-10-14 16:51Z)

**Driver:** 1.0.0_SA_CTO~Z. **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`.
**Ticks covered:** 21 (since tick 20 @935eb3cb76). **state: ARMED**

## Measurement
- Inbox: 0 unread (read and acked since tick 20: 34142, 34150).
- `open-calls.py list`: rows=45, **open=7**, unchanged, all person acts with citations.

## Calls ruled since tick 20
| call | ruling | carrier |
|---|---|---|
| COO~MI 34142: naming gate (ENFORCE) refuses 113 of 174 round-14 rows (273 lines: 222 firm tokens, 47 legacy prefixes, 3 news ids); REC was a gate change for generated catalog rows | NOT yet: use the existing `infra/logic/registry/legacy_addresses.json` branch (reader NFRA_MCPINDEX) for every existing prefix; commit the 61 clean rows now; residual by kind back to the CTO; a gate change (LGIC_ENFORCE, dell1) goes MSTR-to-MSTR only if the residual needs it | msg 16:03Z |
| COO~O 34150: who owns the Eclipse converter fix (Z-S117)? | no live owner (OPAL_ASSETS complete-as-superseded); NFRA_OPLGTW cuts vendor-silver converter defects as WORLD defect cells; Z-S117 now, Z-S110 when its cause is read; measured: eclipse and orion Lambda `mirror_schemas.py` copies differ from the canonical | PRD v3.5 @693c78155e; msg 16:41Z |

## Verdicts received
None this window.

## Completion test
NOT DONE: 7 open, all person acts; stop-condition is Andrew's stand-down.

## Acts only Andrew can do (each cited)
1. MC Portal sitting (21d9 covers 21c5, 8ed7, f0d2): human look + Opal Bloomberg login (TO-MP-z-6 / TO-MP-v-2 G-2ND).
2. Alyssa FWD-1 sitting (def4; 3b41 duplicate) (TO-MP-c-2).
3. One Teams message from his account (a519).

## Compiler Tools
`.tools/open-calls.py list`; `.tools/naming-gate.py` (read); `cmp`; broker; `safe-commit.sh`.
