# NEVER-WIDEN -- CTO HALF: disable `astn-wsjft-3am-run`, `HVST-bz-8` (round 84, workstream BRIEFOFF)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~20:2xZ. **Pairs with:** the COO half
`deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ8_BRIEF_OFF.md` @e56b1f595c (`2.0.0_SA_COO~W1`, SIGNED).
**Authority:** Andrew-direct ~20:0xZ, call 7: "No let's turn that off we don't need that." Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_200xZ_NINE_OPEN_CALLS_ANSWERED_FIRMBKTS_DEMQUE_BRIEF_HARVEST.md`.

## Signed for

- **The act:** one attribute, `aws_scheduler_schedule.astn_run` `state` from `"ENABLED"` to `"DISABLED"` in
  `infra/aws/terraform/astn-pipeline/orchestrator.tf`. A targeted plan must read exactly 0 to add, 1 to change, 0 to destroy, and is applied by `safe-apply` from the saved plan.
  No CLI edit.
- **Writers, N = 1:** the one Terraform resource. The live denominator is 1 Scheduler schedule and 0 EventBridge rules with the `astn` prefix, as the COO half read.
- **Blast radius:** the nightly 03:00 ET invocation of `astn-wsjft-orchestrator` stops, and with it the digest email, which has failed to send on 31 of 31 retained days
  (MDPF_HEALGAP D1-S17). So in practice the served change is a run that sent nothing now not running. Nothing is deleted.
- **All three branches as the COO half states them:** D (disable); S (already disabled, so the source is aligned, with a plan reading No changes); P (any other plan reading is a
  STOP with no apply).
- **Rollback:** `state` back to `"ENABLED"`, a targeted plan reading 0/1/0, and `safe-apply`.

## The seat

The order names `0.7.0_AE_CloudOps~HV1`. That lane was left stopped on Andrew's 17:2xZ word because it held nothing in flight. This act IS in flight, on Andrew's own 20:0xZ
word, so `0.0.0_AB_MSTR~DELL1` re-seats `~HV1` for this act. It stands down after AC1-AC3 read and the ledger closes. That is not a standing re-seat.

## Not covered

Anything the COO half excludes: deletes, an untargeted apply, the digest's content or recipients, and re-enabling.

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`.

-- 1.0.0_SA_CTO~DELL1
