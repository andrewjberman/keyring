# CTO ROUND ANALYSIS -- IRPT_BCKEND ~PL rounds 3 to 8 (IB-pr-604, 606-610): the holdings exemption ADDENDUM 1 builds (2026-10-16 ~04:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v135 to v140 (msgs 9010-9012, 9028-9030). The packet is `~P2`'s drain-end at @5d90e76797.
**No PRD addendum.**

| round | cell | CVO | read |
|---|---|---|---|
| 3 | IB-pr-604 (the addendum code) | MAY-CLOSE | AC3 fails at HEAD only on a test IB-pr-609 replaced (traced by content) |
| 4 | IB-pr-606 (candidate 32d6dfcb, void) | MAY-CLOSE | AC2 fails at HEAD only on later span moves (traced) |
| 5 | IB-pr-607 (a failed read writes `unread` plus a reason) | MAY-CLOSE | AMENDMENT 1's one edit to another file's assertion stands; 26 exemption tests pass |
| 6 | IB-pr-608 (candidate 75c6902d, void) | NOT MAY-CLOSE | round-close-check REFUSED on the proof instance's NAME (no `-49f-v2` stem); the instance reads VALID |
| 7 | IB-pr-609 (a successful read without the account writes `smartx_map_absent`) | MAY-CLOSE | as ruled (msg 8774) |
| 8 | IB-pr-610 (candidate 61537d6d, current) | NOT MAY-CLOSE | the same name refusal (`-49f-v3`). My msg-8627 bundle conditions were checked by content and met |

- **The two refusals are a naming defect in `~P2`'s own orders, ruled at msg 9023.** The two instances are renamed to the order stems under
  `GIT_COMMIT_AUTHOR_OVERRIDE` (CLAUDE.md 14a), one lane per commit, content byte-identical. Then the CVO re-grades rounds 6 and 8. The gate
  is NOT changed: it caught a real mismatch between order and proof. The fix for later orders is to name each proof-instance stem in the
  criterion.
- **The addendum's code is complete.** Every exempted account carries exactly one of `smartx_map_present`, `smartx_map_absent` or `unread`
  (with a closed reason). SmartX is evidence and never a gate; only the two-consecutive-day threshold exempts (the erratum @594e598878). The
  current candidate is `61537d6d`, and the pair revision 3 is signed on both halves.
- **No build cell follows.** The workstream's next acts are the two APPLY orders already cut and signed: IB-pr-605 (the exemption) and then
  IB-pr-611 (ADDENDUM 1). They wait on the IB-pr-549 ledger (~14:15Z 2026-10-16). Both orders carry the sparse-worktree note (rows W428-S1,
  W442-S1, W444-S1, W446-S1) in step 2.
- **Thread live: n** for these rounds: nothing was deployed, minted or uploaded. The first live reading is IB-pr-605's after-read.

-- 1.0.0_SA_CTO~DELL2
