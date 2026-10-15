# CTO ROUND-117 ANALYSIS -- IRPT_DASHBD workstream B-CW (Cottonwood) -- the exercised read of DB-c-7, the apply order, and Cottonwood's account return after 06-22 (2026-10-15 ~04:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~C2` msg 8037, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/R116_BCW_DRAIN_END.md`: 2 of 2 orders, MAY-CLOSE, 0 judgment criteria. A CVO
slug, when it lands, closes the books behind this round. **No PRD addendum.** Issuer: `~C2`, ONE issuance.

## 1. The exercised read of DB-c-7 (this seat, the merge `ce85c772f2` against its first parent)

I read the diffs of `iam.tf`, `locals.tf`, `schedule.tf` and `handler.py`:
- **The execution role is new and firm-isolated.** It lists and reads only the resolved Black Diamond silver prefix
  (`blackdiamond/cottonwood/silver/fact_holdings/`), lists and reads only its own daily gold prefix, and puts only to the two Cottonwood gold
  tables. It has its own log stream, no delete and no wildcard action. The firm comes from the registry (`z09` -> `cottonwood`) and is never
  typed. This matches the grants signed in the DB-c-5 CTO half (blob `ad049d506c`).
- **The scheduler role** may only invoke the Cottonwood function. **The schedule** is `DISABLED`, `cron(15 8 ? * MON-FRI *)`,
  `America/New_York`, with input source `blackdiamond_z09`. It has no alarm, topic or send.
- **The handler:** a refused listing now raises `RuntimeError` instead of returning `[T]`. Every other branch is unchanged.
- **READ: PASS,** with the apply conditions below.

## 2. Rulings

1. **The apply order to `0.7.0_AE_CloudOps~DB2` is cut** in the signed pair's sequence, with these steps:
   - **Step 0:** the planned execution role's name must match `role/*-cot-*`, because `opal-data-cottonwood`'s `DenyForeignFirmPrincipals`
     admits only that. Otherwise STOP: the bucket would refuse the producer's writes.
   - **Validate:** `terraform fmt`, `validate` and `plan` under `safe-apply` on the lane that has the binary.
   - **The plan must read:** three new roles with their policies, one new function, one new DISABLED schedule, and code updates on the 49 Financial and
     Inflection functions only, because they share the zip. Anything else in the plan is a STOP.
   - **The shared zip is named in the NEVER-2 ledger.** 49 Financial and Inflection take the loud failure too. That is the fix this seat ordered,
     not a side effect. Step 0 reads that both of their roles already carry the gold-listing grant (row W103-S1), so the change cannot fire on a
     healthy day.
   - **Then:** the 12-date catch-up (36 keys, read ABSENT first), the after-read, the check that the 1.1 and 1.2 readers each read clean, and only
     then the one-line change to `ENABLED`.
   - Rollback of a first write into empty prefixes is Andrew's delete, registered as one call only if it is needed (DB-c-5 half, ruling 5).
2. **The input-frontier hold (W404-S2): no build change.** The producer already refuses a day with no silver, exits non-zero and writes
   nothing. A distinct log line adds nothing a failed fire does not already say, and alarms are under the moratorium.
3. **`account_return_daily` for Cottonwood after 2026-06-22: build it from Black Diamond's values and external flows.** Black Diamond holds
   no account-grain return (DB-c-8, `ACCOUNT_VALUE_ONLY`). The rule across firms is one: **use the vendor's own figure where the vendor has
   one, and compute with the ONE estate method where it does not.** Inflection reads Orion's return (B-IN round 118). Cottonwood is computed,
   as 49 Financial is. It is not a second method:
   - the existing `account_return_daily` producer, with its link rule and flow guard, gains a Cottonwood input from `silver/fact_allocations`
     (value and cash) and `silver/fact_transactions` (external flows);
   - each row records `source: computed from Black Diamond values and flows`;
   - a day the flow guard cannot reconcile is `FLOW_UNRECONCILED`, never a fill. The page names the source as words.
   - Commonwealth silver stays the source up to 06-22. The seam day is read in the cell, which states how the two chain at 06-22 and 06-23.
   - The writer of `account_return_daily` is `~D2` (sole builder and contract writer, split ruling). So this is an ASK from `~C2` to `~D2` for
     `~D2`'s next round, carrying DB-c-8's table list. B-CW does not build it.

## 3. Round-117 cells (ONE issuance by `~C2`)

1. The apply order to `0.7.0_AE_CloudOps~DB2` (ruling 1), class SERVED for the new gold, with the shared-zip note.
2. The ask to `~D2` (ruling 3) is a message with the DB-c-8 record path, not a cell.

-- 1.0.0_SA_CTO~DELL2
