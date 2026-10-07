# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-06 18Z -> 19Z (host opal_bloomberg)

**archetype:** COORDINATE

Relaunch on Andrew-direct "GET COO~MI relaunched and active" (record
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20261006_1809Z_RELAUNCH_COO_MI_ACTIVE.md` @057974a128, already
committed by 3.0.0_SA_CVO~O, so it was not duplicated). Lease FULL.

- **Arm:** `/canonical-drive NFRA_MCPINDEX` every 30 minutes, off the unstruck DIRECTED row in `org/ref/LIVE_ARMS.md` (1.0.0_SA_CTO~O
  `/self-drive` pairing).
- **Hold lifted:** the Bloomberg-only hold (msg 30072) was lifted at ~17:44Z (@8555ce7e12).

## Decisions closed

- **MX-m-2:**
  - Drained @2234389ca8.
  - Issuer re-ran m2.AC1 on CLOUD: orion 24/24, eclipse 8/8, smartx 13/13, PASS.
  - Status flipped to complete @042668d9fa.
- **MX-f-1:**
  - Drained @c387810e85. The channel conflict was resolved as a union: 238 rows parse; W26-S1/S2 come first, then
    W25-S1/S2.
  - f1.AC1-AC3 PASS on CLOUD.
  - comp-system regenerated `06_current_state` @9b0481b68c (rc=0, 0 managed-region drift).
- **Row Z-W24-S11 ruled, option (a)** (s-18 A1 @27501e83dd): one statement, GetObject on
  `opal-data-bd/bronze/*/_BRONZE_COMPLETE.json`. The plan must read 0/2/0.
- **s-17 A1:** disarm Z-W24-S9 (boto3/pandas import on the instance) before the publish.
- **s-19 A1:** acceptance re-dated to 2026-10-12/13. The 10-05/06 sentinels read ABSENT at 18:29Z.
- **Never-widen ask** for s-17 + s-18: COO half SIGNED @27501e83dd. Base measured at 18:29:41Z: documents 3/3, runner
  `q37ovM...` = artifact `AVNCLX4F...`.
- **CTO half HELD** @ba005db3b0 (msg 30220). The CTO put the scope of Andrew's 2026-10-03 data-ops word to him. PHASE B
  does not GO until that file reads SIGNED.

## Open (each with its condition)

- **s-17 / s-18 PHASE B:** on the CTO half reading SIGNED. Worker ~24 is not live, so PHASE B respawns a worker into
  `wk-mcpindex-r7-24` (@3709ae40d6).
- **s-19 PHASE A:** deferred to the same word, since its act is the writer retirement the question covers.
- **Round 7:** 3 of 6 terminal. L8 compile at the round's drain-end.
- **Worktrees:** r7-25/26/27 removed; r7-24 kept.

## Compiler Tools

- `safe-merge.sh`, including `--continue` after a union resolve; tree checks dropped 0.
- `safe-commit.sh`, `comp-system` (rc=0), `comp-which`, the round-7 battery (m2, f1, s19.AC2 re-dated).
- Gap: `audit-archive-invoker.py` reports FAILCLOSED baselines on this device. Those are owned classes, not re-filed.
