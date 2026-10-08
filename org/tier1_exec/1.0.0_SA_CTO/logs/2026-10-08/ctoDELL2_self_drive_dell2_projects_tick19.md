# /self-drive dell2 projects -- tick 19 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since tick 18 (@772b921be5), plus tick 19 (2026-10-08 00:53Z). **state: ARMED**

## Scope state (00:53Z)

7 of 7 are active / EXECUTING. Sequence flags are unchanged (the known NEEDS-SLOT gap on IRPT_CUSTDY and ADVI_COTBKF). Inbox: 0 unread
after acks.

Live `irpt-ycharts-generate` still reads `uFTONal...` (2026-10-04). Release 1 waits on dell2's `ssm:GetParameter` grant (below).

## Andrew-direct received

**~00:0xZ** (laptop msg 106648, MSTR msg 1162), verbatim:
- "Why is laptop running any of this, that's the whole point of the dell boxes is to run the heavy jobs there";
- "I think we need to start giving dell boxes more permissions. Their entire point is to be work horses and laptop is control plane."

The laptop CTO rules:
1. no new Dell run on a laptop seat; an access refusal is answered by the grant;
2. the secrets grant widens (OpenAI excepted);
3. each AccessDenied is reported by ACTION and RESOURCE the same hour.

**Executed by this seat:** my msg 1155 rec (a), the laptop applies release 1, is withdrawn.
- Release 1 is applied by `~Y2` from dell2 once the grant reads back.
- The BD split pull runs on dell2 by `~D2`'s seat (CTO half AMENDMENT 1 @1f0b2d2654; runner only).

Msgs 1170-1172.

## Calls closed and acts

| input | ruling or act | carrier |
|---|---|---|
| `~P2` 1169 (IB-pr-356 conditions) | Both MET on 63b9382a:<br>- `validateCustodyReport` gates the custody read;<br>- the wire regeneration writes to tmpdir.<br>PASS for DEV. The exposed AnalysisReport wire drift goes to a row, not a rider. | msg 00:50Z |
| `~T2` 1177 (NFRA_TRNSPT round 4 drain-end) | **FWD-7's positive arm is MET by the schedule:** the 23:30Z EventBridge fire landed 3 admitted messages unattended (12 objects, hashes 9/9, held_out 3/3), and APPLY 2 returned the window to 7 days. Not landed: 2026-08-11 (row D2-S2). `listed=100 = 2 x 2 x 25` points at a page cap, not a near miss; to be read at the L10. `~T2` refused an APPLY 2 plan that would have reverted the Dell key policy, which was right. The CVO's slug follows. | -- |

## Acts only Andrew can do

1. **IB-pr-356 portal DEV landing** (63b9382a), then the PROD promote of the print page.
2. The on-behalf filing entitlement (TCKT_VNEXT X-1).
3. Running the Python 3.12 installer elevated.
4. His F1 retry, after release 1 applies and after-read 4 passes.
5. TCKT_VNEXT: confirming the DONE WHEN lines.
6. The PROD advisor hold; the pre-fix export residual disclosure.
7. NFRA_TRNSPT: the 14 words (now 3 more held-out rows), the second reader, Alyssa's corpus.
8. The ADVI_COTBKF near-match page to Cottonwood.
9. R13; FWD-17 to FWD-23.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- `get-function-configuration` re-read: release 1 not applied (the grant is pending).
