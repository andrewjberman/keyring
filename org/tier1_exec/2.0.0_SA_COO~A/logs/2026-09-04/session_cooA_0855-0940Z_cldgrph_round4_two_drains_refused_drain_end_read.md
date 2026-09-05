# 2.0.0_SA_COO~A -- session 2026-09-04 08:55Z-09:40Z -- NFRA_CLDGRPH ROUND 4: two drains refused by the row gate, the round blocked on two v3 gates, the drain-end read sent

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

## Objective

Drain workers ~2 (TO-CG-D-2) and ~1 (TO-CG-D-1) as their reports landed, hand the next orders, and send the round's ONE message to `1.0.0_SA_CTO` when the round ended.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| proof-of-spec-check | on D-2's instance (10 ids) and D-1's (8 ids), from the COO seat | PASS (VALID rc=0 both) | a VALID instance carried 4 FAIL rows on each -- validity is structural, not the closes-on |
| safe-merge.sh | on wk-NFRA_CLDGRPH-2 (x3 to read the verdict whole) and wk-NFRA_CLDGRPH-1 (x1) | FAIL (REFUSED, aborted clean) | the row gate's `_coordinate_violations` reads the merge COMMITTER (a seat) and refuses every W row; 7 of 7 and 8 of 8 on that one clause; no collision |
| surprise-row-gate (via safe-merge) | the merged index, 16 paths each | FAIL (by design of the committer clause) | its co-worker sweep admitted the same rows as a co-worker's riding along |
| aws (shim) | ecr describe-images; ecs describe-task-definition x3; s3 cp the pointer | PASS | `:latest` = sha256:1b89853f...; three families still on the tag; pointer 08:49:20Z |
| comp-read / grep (pipe receivers) | safe-merge.sh, surprise-row-gate.py, safe-commit.sh, halt-gate-check.sh:134-154 | PASS | traced how the override marker is carried (safe-commit only; `--only` refuses a merge) |

**What worked:** the refusals were clean (no MERGE_HEAD left) and legible once read whole. **What failed:** the drain of any worker branch carrying a row is impossible through the lawful refuser today, and the audited override cannot ride a merge commit. **Gap found:** (1) `surprise-row-gate.py` `_coordinate_violations` reads the committer, not the row's `surfaced_by`, at a merge; (2) `safe-merge.sh` grades with no message, so the override marker has no carrier; (3) `halt-gate-check.sh` admits no worker serial (both deploy orders blocked); (4) `worker.md` flips `complete` on rc 0 with FAIL rows; (5) sibling subagents share one scratchpad dir; (6) `deploy_ledger.py list` cannot print CLOSED (my D2-AC9 defect); (7) the ledger sentinel path is outside both orders' grants (my defect); (8) D-1's apply set is eight addresses, not four (my defect). Nothing was overridden by hand.

## Work Completed

### 1. Worker ~2 / TO-CG-D-2 (CG-s-5), 09:12Z-09:40Z
Report read; branch read (4 commits, the worker's; override audit PASS in-lane); proof VALID rc=0 at this seat with D2-AC3/4/6/9 FAIL: the gateway traversal BUILT and DECLARED (the integration, the `/graph/*` bearer path, TF plan 2 to add), NOT APPLIED -- `safe-apply.sh` and `safe-ec2-deploy.sh` rc=3, the halt gate resolves no worker serial (row W2-S1). `safe-merge.sh` REFUSED the seven W2 rows on the committer clause; the ledger sentinel captured; branch + worktree KEPT. Step-log row 5 @221b63aacc.

### 2. Worker ~1 / TO-CG-D-1 (CG-s-15), 09:20Z-09:30Z
Report read; branch read (1 commit, the worker's); the image rebuilt and exercised (a real projection task on the new digest advanced the pointer), the pins NOT applied (W1-S1, the same gate), TRIGGERS = 0 because the derive task role lacks `s3:GetBucketNotification` (W1-S7 -- S20's real cause; the cloud derive printed `read=0 / unreadable=34`). `safe-merge.sh` REFUSED the eight W1 rows the same way; sentinel captured; branch + worktree KEPT. Live plane re-read at this seat.

### 3. The drain-end read, 09:34Z
ONE message to `1.0.0_SA_CTO` (`org/mcp/inbox/1.0.0_SA_CTO/20260904T093436Z_2.0.0_SA_COO_A_DRAIN-END_READ_NFRA_CLDGRPH_round_4__2.0.md`): outcomes, the IAM finding, the two gate defects, nine instrument gaps, every unseated armed row with its owner, the watermark (32 at HEAD vs 47 minted), the live plane and the two OPEN ledgers, five recommendations for the round-4 analysis. Step-log rows 6-7 in this commit.

## Decisions Made

1. **No by-hand merge.** The override the gate names is audited only through `safe-commit.sh`, which cannot commit a merge (`--only` + pathspec); a direct `git commit` with `SURPRISE_ROW_OVERRIDE` would be an unaudited override. The branches stay unmerged and intact; the CTO's analysis decides.
2. **No hand-off of D-3, D-5, D-6.** Each premise (D-2's live path; D-3 merged) fails; a hand-off would produce a BLOCKING row and nothing else.
3. **The rebuilt image was not rolled back.** Only `comp_aws_cli.py` changed in the COPY set; two consumers ran it clean; the pin never started, so nothing is half-landed. The nightly will print `unreadable=34` until the IAM grant lands -- stated to the CTO.
4. **The round ends here** (v3.1: an armed row whose owner the COO cannot seat rides the drain-end read; every remaining order is blocked on the CTO's gates), with the three subagents kept alive for re-hands.

## Files Modified

See commit messages: `221b63aacc` (step-log row 5) and this commit (step-log rows 6-7 + this log). No project surface edited by this seat this window.

## Blockers

BLOCKED, evidence-cited, owner named: every remaining order of round 4 -- on `.tools/halt-gate-check.sh:134-154` (no worker serial admitted; measured rc=3 by two workers with both env escapes set) and on `.tools/surprise-row-gate.py` `_coordinate_violations` at a merge (measured: 7/7 and 8/8 refusals naming the committer, aborted clean by `safe-merge.sh`). Both owned by `1.0.0_SA_CTO` (the v3 carriers), the merge half with `2.0.0_SA_COO` base. Routed in the drain-end read 09:34Z.

## Current State

NFRA_CLDGRPH round 4 at L7-blocked -> L10 (the CTO's analysis pending). CLOUD HEAD after this commit carries D-4 merged (CG-s-7 DONE) and the step log through row 7. Two worker branches unmerged and kept: `wk-NFRA_CLDGRPH-2` @d4ab452051 (D-2 built, 7 W2 rows) and `wk-NFRA_CLDGRPH-1` @8b8f2caae2 (D-1 rebuilt/exercised, 8 W1 rows), worktrees at `C:/Users/AndrewBerman/Desktop/wk-NFRA_CLDGRPH-{1,2}`; `wk-3` removed. Live: ECR `:latest` = sha256:1b89853f... (the fix's image); the three families on the tag; the pointer 2026-09-04T08:49:20Z; the serving task rev 1 unrestarted. Two NEVER-2 ledgers OPEN on the branches (sentinels in this seat's scratchpad, not in the main tree). Three subagents alive and idle. Push state LOCAL everywhere; origin/CLOUD @351f309e0a at the last read on the record.

## Next Steps

1. **[1.0.0_SA_CTO]** The round-4 analysis: the two gate fixes; ONE added cell for the `s3:GetBucketNotification` grant on `opal-globgrph-derive-runner-task` ahead of the pins and CG-x-2's night; D-1/D-2 reopened with the eight-address set and the face fixes; the G8 arch-gate ruled; worker.md's flip rule.
2. **[2.0.0_SA_COO~A]** On the analysis: recut in ONE issuance; drain the two kept branches through the fixed refuser; continue ~1/~2/~3 on their next faces; the laptop-seat half of D6-AC4 and the local-DB switch-off at the drains as planned.
3. **[3.0.0_SA_CVO]** L8/L9 on the 15 W rows readable on the two branches; the round-3 remediation clocks (S20/S28 must not disarm on the rebuild -- W1-S7 is the cause).
