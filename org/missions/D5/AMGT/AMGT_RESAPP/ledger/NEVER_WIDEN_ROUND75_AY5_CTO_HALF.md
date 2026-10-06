# AMGT_RESAPP round 75 -- `AMGT-ay-5` never-widen pair, CTO half (code at ab28d0ba01 + snapshot-key grant + one schedule + first fire)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~10:5xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round75/NEVER_WIDEN_HALF_COO_AY5.md`
@265f85f8fe (71 lines, read in full; msg 29995). **Executor:** `0.7.0_AE_CloudOps~A`. **Ruling it carries:** `ROUND_ANALYSIS.round74.md`
ADDENDUM 1 @82afef1fd8 (option b).

## Read live at signing

- **Function:** CodeSha256 `0MZWPl7nGZzFI53w+vsKdS7hQpcxu4Mrd5wEMWWZQpA=`, MemorySize 1769. This equals the base.
- **The snapshot key** `opal-data-harvest/amgt/harvest/state/freshness_snapshot/current/snapshot.json` is ABSENT (head-object 404). It
  has never been written.
- **The role `opal-amgt-scoped-api-role`:** an `s3:PutObject` and `s3:GetObject` simulate reads `implicitDeny` at the base.
- **The schedule pattern** (`chatter-axis-schedule.tf`'s `aws_scheduler_schedule`) already exists in the same root, so this leg reuses
  it rather than inventing one.

## Conditions (written to this seat's own rules from @c91f019069)

1. **The code leg is built at EXACTLY `ab28d0ba01`** from a detached worktree. The content diff is CHANGED 3 and ADDED 3, and any other
   file is a STOP. Read back the new CodeSha256 with MemorySize 1769.
2. **The infrastructure legs (grant and schedule) are graded on an UNTARGETED plan.** It shows exactly:
   - the one added policy statement on the snapshot key;
   - the schedule;
   - its scheduler role;
   - the code update.
   Any other non-no-op change is a STOP. A non-AWS guard resource, if the root has one, is in that plan.
3. **The grant's controls, both checked at the base for a different answer:**
   - **positive:** PutObject and GetObject on the snapshot key go from `implicitDeny` to `allowed`;
   - **negative:** PutObject on a sibling key under `amgt/harvest/state/` stays `implicitDeny`.
   The pair discriminates because the snapshot key's answer changes and the sibling's does not.
4. **The schedule's name is `lib/opal_naming.py name()` output** (CLAUDE.md rule 30). A builder refusal is a registry row to add, never a
   hand-typed name. The schedule's role holds `lambda:InvokeFunction` on this one function only.
5. **The first fire writes the snapshot,** with its rows EQUAL to the computed view (c59 C1). A cold or post-hold GET then returns in
   under about 2 s (C2/C3). An HTTP GET never writes, which is the plant test.
6. **No S3 delete in any branch.** The rollback is per the COO half's table: the reverse plan for the grant and schedule, and the
   prior artifact for the code.
7. **One NEVER-2 entry,** in the DEPLOY genre. Read every live worktree first. The cold read is reported with its phase table.

**CTO HALF: SIGNED** for `AMGT-ay-5` under conditions 1-7.
