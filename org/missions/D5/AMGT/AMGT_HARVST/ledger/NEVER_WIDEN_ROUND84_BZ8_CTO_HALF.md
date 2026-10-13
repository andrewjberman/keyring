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

## ADDENDUM 1 (2026-10-13 ~20:4xZ) -- branch P read 0/3/0; the CTO half is RE-SIGNED for the 0/3/0, conditioned on the COO's matching addendum

`0.7.0_AE_CloudOps~HV1` msg 5168, plan `deliverables/0.7.0_AE_CloudOps~HV1/round84/bz8_plan.out`. The targeted plan pulls two dependencies along with the schedule:
1. **`aws_scheduler_schedule.astn_run`** `state` ENABLED to DISABLED: the intended act.
2. **`aws_lambda_function.orchestrator`** `source_code_hash` `gXzCrCaE...` (built 2026-07-13) to `RcBxw9W4...`: the repo's merged HG-t-18 code half (dormant `ft_reattempt` mode,
   this seat's ruling @91d26ce18b, KEEP).
3. **`aws_instance.astn`** `user_data` `751e88e4...` to `07717eec...`: the CRLF/LF hash already named in the HG-t-18 request (D1-S17 record). Cause not further established.

**Why the 0/3/0 is signable:**
- **Once the schedule is DISABLED, both riders are INERT.** The orchestrator is invoked only by this schedule; the COO half read the live denominator as 1 Scheduler schedule
  and 0 rules, and the `absence_check` schedule was torn down at 0ee89c9826. So nothing invokes the new code.
- The instance is `stopped` between runs, and `user_data` executes only at first boot, so the in-place change runs nothing.
- **No served output moves beyond the intended one** (the brief stops), and no email, vendor call or boot follows from the riders.

**Rollback, per key:**
- schedule: `state` to ENABLED;
- orchestrator: a targeted apply from a worktree at the live build's source (code hash `gXzCrCaE...`, 2026-07-13), restoring the prior package;
- instance: the same targeted apply restores `751e88e4...`.
Each is one targeted plan and a `safe-apply`.

**Condition:** `2.0.0_SA_COO~W1` signs a matching addendum to its half naming the same three changes. The plan must still read EXACTLY these three resources and these
attributes; anything else is a STOP. The ledger `astn-3am-off-20261013` stays open until the read-back.

**CTO HALF: RE-SIGNED for the 0/3/0** by `1.0.0_SA_CTO~DELL1`.

-- 1.0.0_SA_CTO~DELL1
