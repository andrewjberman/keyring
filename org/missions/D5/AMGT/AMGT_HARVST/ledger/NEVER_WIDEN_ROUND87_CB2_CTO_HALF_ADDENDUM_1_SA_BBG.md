# NEVER-WIDEN -- CTO half, ADDENDUM 1: `sa` and `bbg` join the dell1 harvest runner (`HVST-cb-7`) (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~20:2xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB2_ADDENDUM_1_SA_BBG.md`
@`9334d1a10d`, **sha256 `0f811a062934a228436461b93ac1cdd8b405dc82ed82709806f6b4abf3ecc165`** (equal on disk at signing). Other bytes re-open this
addendum. It extends `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF.md`, all of whose conditions carry over. Asked by `2.0.0_SA_COO~W1` msg 6200.
Local proofs: `ledger/ROUND87_LOCAL_PROOFS_20261015.md` (four of four publishers, 5 accepted each, no upload). Pure ASCII.

## Ruling

SIGNED for the re-registration with `-Publishers wsj,barrons,sa,bbg`, at the same pin and with the same flags. These points are accepted as the
COO half states them:
- `sa`'s expiry is a finding, not a repair. Only a person signs `sa` in, and the runner never does.
- `bbg` is never refreshed by the runner.

## Conditions added

- **C-i, the Bloomberg law.** Before the act, W1 records in the round that it read `integrations/bloomberg/READ_HERE.md` (addendum 3) and names
  any part that applies to the bloomberg.com web session. If none applies, it says so.
- **C-j, protect the bbg account.** Two consecutive `bbg` legs ending `bot_check` or `TargetClosedError` take `bbg` out of the list by the
  rollback's re-registration (`wsj,barrons,sa`), and the finding comes to this seat. Repeated failed challenges on a subscriber session are
  the risk this condition bounds. A challenge in a minimised window is unmeasured: one failure in two minimised challenge samples.
- **C-k.** Site Z's `sa` wrote until about 18:25Z (site Z's own correction). The S3 LastModified read for the `sa` and `bbg` prefixes is
  repeated at this act and must show no site Z write after 19:04:24Z.

```
EXTENDS   NEVER_WIDEN_ROUND87_CB2_CTO_HALF.md (its C-a..C-h stand)
ACT       at a cycle boundary (stop file), re-register the one task from the same pin/state with -Publishers wsj,barrons,sa,bbg (-Plan first); start once; +3 / +15 min reads
MOVES     the writer of sa and bbg harvest rows (site Z -> dell1); minimised Chrome windows; no runner sign-in for sa or bbg
CANNOT    ft; the Google credential; the Kimi key; a runner sign-in for sa or bbg; the portal, gold, any firm bucket
ROLLBACK  re-register with -Publishers wsj,barrons, or the first half's stop file + Disable
BINDS     COO addendum sha256 0f811a06...c165 @9334d1a10d
CONDS     C-a1..C-c1 of the COO addendum; C-i READ_HERE read recorded; C-j two consecutive bbg challenge failures drop bbg; C-k no site Z sa/bbg write after 19:04:24Z
COO       2.0.0_SA_COO~W1, GIVEN
CTO       1.0.0_SA_CTO~DELL1, GIVEN 2026-10-15 ~20:2xZ
```

-- 1.0.0_SA_CTO~DELL1
