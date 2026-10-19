# /self-drive dell2-box -- tick 115 (2026-10-17 ~20:27Z-20:57Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 114 and 115, since the tick 113 log (@4eeb47ea62, 19:57Z). Written for a substantive delta and the
hourly floor. state: ARMED. Inbox: 0 unread at 20:56Z.

## Acts taken: the synthetic commentary end-to-end run, three attempts' worth of rulings

| act | carrier |
|---|---|
| Run 1 (IB2 msg 10661): mint and login ok; the upload was refused `NOT_AUTHORIZED`; deletes 1 of 1; ledger closed. Ruled: a LOCAL door-vs-mint read before any retry. | ruling ADDENDUM 2 @58ce580def |
| The read (~Y2 msg 10663, worker 294): `served.py:1089-1091` requires `advisor_email` when the tenant is in the actor's `allowedFirmIds`. The run's steps lacked an advisor; neither the door nor the mint is wrong. **Pair ADDENDUM 1 (a synthetic advisor) CTO half SIGNED**, with 3 conditions. | @fec24f492d (blob 0214956486, sha256 491648a2) |
| Run 2 (IB2 msg 10667): **the door AUTHORIZED the actor**, the first run in this series to pass it. The upload answered `RESOLVING` (a wait) after the one try allowed. Deletes 6 of 7; one synthetic 118-byte CSV is left (AccessDenied for the CloudOps principal, index rows deleted). Ruled: re-post per the portal's protocol; delete the leftover through the application's own path, or carry it as a surprise row. No IAM change. | ruling ADDENDUM 3 @f4be348491 |
| **Pair ADDENDUM 2 (up to 5 identical posts, 3 s apart) CTO half SIGNED.** `uploads.py:522-533` shows the re-post resumes the same row. If five tries all answer `RESOLVING`, the portal's 15 s limit is shorter than the resident's resolve time, and that is a product finding. | @57f931e207 (blob 5bddf32c3b, sha256 523d0f83) |

## Open calls in scope

3 OPEN rows out of 127. All three are Andrew's acts.

## Acts only Andrew can do

- **449e:** press Retry on TCK-20261017-5af976ff in PROD Ticket Center. Citation: ticket_center `lambda_function.py:1750-1753`
  records only for the creator or assignee.
- **3c22:** lift or keep his named hold C-V1 ("let's avoid pricing for the v1"). Citation: IRPT_YCDGEN PRD :251 and :312.
- **c02c:** send or not the Inflection ops ask on accountStartDate. POSTPONED on his word.

## Waiting on

- `~Y2`: the third run order to IB2, and `AR-y-402`, the read of the leftover CSV's delete path.
- The box's apply order: Monday 10-19 the 49 Financial fire read; Tuesday 10-20 the Inflection pair; then the Cottonwood
  REVISION 2 release; then `~D2`'s all-days pair; then the class_series publisher.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

## Compiler Tools

`python .tools/open-calls.py list`; `git hash-object`, `sha256sum`; reads of `served.py` and `uploads.py`; `git grep` on
portal origin/PROD; MCP send and ack.

state: ARMED
