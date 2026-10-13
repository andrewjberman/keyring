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
