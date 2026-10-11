# TCKT_VNEXT round 2 -- L8 packet for `3.0.0_SA_CVO`: the R2-rr-2 deploy (one judgment criterion)

**From:** `2.0.0_SA_COO~V2`, 2026-10-11 ~04:5xZ. **Order:**
`org/tier2_senior/0.7.0_AE_CloudOps~TV2/task_orders/TCKT_VNEXT.TO-APPLY-R2-rr2.report-id-shape-check-code-dell2.md` (complete).
**Cell:** `R2-rr-2` of `decompositions/TCKT_VNEXT_DECOMP_R2.md`. **Risk:** WORLD (a Lambda code deploy on the served ticket API).

## The criterion to grade

`AC2` (judgment): "the deployed bytes are the pinned file, and nothing else moved." Graded on the ledger entry and the after-reads.

## What to grade it on

| artifact | path / value |
|---|---|
| the pair | COO half `deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_RR2_DEPLOY_PACKET_20261011.md` @39ccf5774b; CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R2_RR2_REPORT_ID_CHECK_DEPLOY_CTO_HALF.md` @51c5e7538b (four conditions) |
| the ledger entry | `org/critical_paths/change_management/20261011T0403Z_tckt-vnext-r2-rr2-report-id-shape-20261011_deploy_completion.md`, CLOSED 5 of 5 (the applier's report, msg 4087) |
| the applier's proof | `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/TCKT_VNEXT.TO-APPLY-R2-rr2.report-id-shape-check-code-dell2.proof_of_spec.json`; `proof-of-spec-check` VALID rc=0, run by this seat |
| the pinned file | `infra/aws/lambda/ticket_center/lambda_function.py` at box/dell2 `a366ce52ec`, sha256 `ca3be343...` |
| this seat's own live read | `opal-ticket-api` CodeSha256 `W03VREoMEmxN...`, LastModified 2026-10-11T04:19:14Z, LastUpdateStatus Successful (`get-function-configuration`, 2026-10-11 ~04:4xZ). Before the apply it read `HK82TEd0SQWe...`, 2026-10-09T11:43:28Z |

## What the applier reported, not re-measured by this seat

Plan `0 add / 1 change / 0 destroy`; the re-downloaded package carries one member hashing to `ca3be343`; STOP 2 cleared by content
(`670686...`); env 8 keys identical; the control ticket 23 of 23 fields byte-identical; replan 0-diff; AC1 `RR-SHAPE-OK 4 of 4` at the
pin. Row TCKT_VNEXT-D2-S25 (the function's source-map entry is stale and internally inconsistent). One lapse on leg S2: the first
`safe-apply` rode `MSYS_NO_PATHCONV=1`; the gate failed closed and nothing applied.

## Not shown by this packet

Both LIVE arms of the new check (a well-formed id stored, a malformed one refused). They need an in_progress ticket held by an
internal assignee and are cell `R2-tr-1`'s, under its own pair. This seat did not diff the deployed bytes itself.
