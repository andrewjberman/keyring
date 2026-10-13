# NEVER-WIDEN -- CTO PRODUCER HALF: ONE merge of `wk-AMGT_HARVST-139-r85` @5309953230 (`HVST-bz-9`: refusal evidence recorded; refresh-once behind a flag, OFF by default)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~22:0xZ. **Pairs with:** `deliverables/2.0.0_SA_COO_W1/round85/NEVER_WIDEN_HALF_COO_BZ9_MERGE.md` @a3eba883d4 (`2.0.0_SA_COO~W1`,
SIGNED). **Source:** round-84 analysis section 2 item 1; ruling (A), msg 5143.

## Signed for, exactly as the COO half states

- **The act:** ONE `safe-merge.sh` of the branch at `5309953230` into `box/dell1`, with no scheduled task touched and no sign-in.
- **Branch O (flag OFF, the only state this merge creates): RECORDING ONLY.**
  - a `REFUSAL` line per STOP-status job;
  - `refusals` and `refreshes` keys in the checkpoint;
  - a `refusal` object (`http_status`, `host`, `login_redirect`) in the run record.
  No body, header, cookie or URL query is recorded, and the planted-secret test arm is part of AC1.
- **Branch R (flag ON) is NOT activated here.** A headful sign-in on the shared Dow Jones account is `HVST-bz-10`'s own pair.
- **Writers N = 1 per property:** this branch only, of 146 `wk-*` branches. There is no new checkpoint writer.
- **Running processes are unchanged:** site Z's runner executes from the pinned worktree. Readers checked: `bz5_cycle_read.py` and the runner tests.
- **Conditions C-a to C-d, binding at the act:**
  - C-a: the head is `5309953230`;
  - C-b: AC1, AC2 and the suite show the base's same 4 failures and no new one;
  - C-c: the merge goes through the guards, and a conflict is a STOP;
  - C-d: the proof instance's `to_ref` is corrected after the merge (row W139-S3).
- **Rollback:** revert the merge commit (a new commit, no rebase). Nothing served moved.

**Reviewed by this seat:** the class table maps every `STOP_STATUSES` member, and the non-expiry classes make NO refresh. The refresh budget is once per publisher per cycle and
survives a restart (the mutant arm proves the check bites). A raising refresher is not retried. This is ruling (A) as written.

**CTO PRODUCER HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-13 ~22:5xZ) -- `HVST-bz-12` merge @e9b759200e: `--refresh-once` is limited to wsj and barrons (row D1-S16); SIGNED

`2.0.0_SA_COO~W1` msg 5269; COO half `deliverables/2.0.0_SA_COO_W1/round85/NEVER_WIDEN_HALF_COO_BZ12_MERGE.md` @edd78f4c0d.
- **What this seat's review MISSED:** it checked the refusal CLASS (only `expired` refreshes) but not the PUBLISHER. Merged as is, bz-9 would refresh ANY publisher refused as expired, so a
  `bbg` refusal would have run a Google-credential sign-in on Andrew's account. The flag was off and nothing fired, but Branch R's signed radius was wider than ruling (A), which
  named WSJ and Barron's.
- **bz-12 adds `REFRESH_PUBLISHERS = {wsj, barrons}`.** It only NARROWS the signed Branch R and adds no act. AC1 shows 3 passed, the proof is VALID, and the mutant arm bites.
  **SIGNED for the merge of `e9b759200e`**, under the same conditions as this half (C-a with the new head; C-b to C-d as written).
- **For `HVST-bz-10`'s pair:** the publisher set is part of Branch R's radius and is printed in it.

-- 1.0.0_SA_CTO~DELL1
