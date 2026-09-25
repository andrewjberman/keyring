# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Lease FAST `IRPT_BCKEND~M`, extending while Andrew is active (drive-mode.log). Goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`
(Done = /verify SOUND). The 20-minute goal loop reads this lease first on every tick (C11). Reviewer: `3.0.0_SA_CVO`
(not live; the FAST line is parked below). As of 2026-09-25T15:0xZ.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m`; MERGED into CLOUD @f606108549 (safe-merge, 16 files, 0 overlap); investor_reporting suite on merged CLOUD 267 passed |
| Served holdings (since 23:14-23:21Z) | COT fc199c8e (index ykQofbha); INF ba9001d5 (ipomYxTG); 49F 9ab377ce (OqjgF6qs) -- the prior served revisions plus the v0.6 classification members |
| Prior revisions (rollback) | COT dec293d6, INF d32e50c6, 49F 5a25ae76, retained |
| Receipts | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/HOLDINGS_{COT,INF,49F}_CLASSIFIED_PUBLICATION_RECEIPT_20260924.json` @7e57abcabd |
| Push state | LOCAL: origin/CLOUD aa5568155e (ls-remote read 14:1xZ) does not carry f606108549; shared pushes are 0.0.0_AB_MSTR's |

## Live thread

LIVE END TO END through the deployed API at all three firms, signed in:
- **INF:** Greene SIMPLE (HAR 18:36Z).
- **49F:** Alison Horton IRA, with a model leaf (HAR 18:36Z).
- **COT:** Anna (HAR 14:17Z).

The screen fixes landed on portal DEV a65a8db5 (~D): exact amounts, firm-tab filter. Andrew walked it ~19:0xZ
("it looks great"). The classification members are served since 23:2xZ, and ~D's colour cells read them. The PROD
a0690a03 parser reads READY at every firm.

## Goal criteria

| Criterion | State | Evidence |
|---|---|---|
| (1) signed-in journey, 49F / INF / COT | API EXERCISED at all three; screen walked by Andrew on the fixed build; the firm-tab HAR is the one artifact asked | VERIFY_HOLDINGS_GOAL_20260924.md addenda |
| (2) every active 49F/INF account resolvable, or refused explicitly | MET on the CURRENT directories (49F 09-24, INF 09-25): 49F 7,443 resolve + 54 refused, 0 empty of 7,497; INF 876 resolve + 2 refused, 0 empty of 878. Of the refusals, 37 at 49F are the no-custody accounts known since 09-17, and 19 (17 at 49F, 2 at INF) are new to the directory since 09-17 (that they postdate the 09-22 holdings date is INFERRED) | census @f247a922a5; VERIFY addendum 09-25 (M branch) |
| (3) COT soundness + window disclosed | disclosed in the receipts | COT_LABELLED_PUBLICATION_RECEIPT_20260924.json |

## Write claims

`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/*` and `data/assets/scripts/gold/investor_reporting/*` on the M
branch. No code edit is open.

## Next list (in order)

1. Andrew's firm-tab HAR, then /verify on the goal.
2. **The scheduled daily Holdings producer is ~M's** (CTO R4, msg 100947;
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_IRPT_20260925.md` @75156f2b18):
   - Step 1 (the code on CLOUD): DONE @f606108549.
   - Step 3 (does the resident runner take a holdings message off irpt-generation): asked of 2.0.0_SA_COO~P, msg
     20260925T143825Z.
   - Step 2 (re-mint the bundle) is blocked on a limit, not a person. One `investor_reporting` bundle carrying all 12
     runner files is 17 members, whose sha stamps plus `source-repo-paths` come to 2,440 bytes of S3 user metadata
     against the 2,048 cap (local build 14:5xZ, 121,448 bytes, no dirty member). The mint would refuse at upload, and a
     committed 17-member declaration would break the next member-detector re-mint, including the directory runner's.
     Not committed; reverted. The package shape (a separate holdings bundle, or a hash manifest inside the tar) follows
     step 3's host answer.
   - Step 4 (the enable) goes to the CTO as a never-widen half.
3. **CTO R5 and Andrew's two answers** (msg 100951;
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260925_144xZ_CLASSIFIER_OTHER_OPENAI_RUN_AND_DEV_PUSH.md`
   @705be61575):
   - DONE: the 49F no-ticker rows are named from the Schwab security master (cb8cd03113 on the M branch; CLOUD
     @6c54a74490). Real dry run on 09-24 sources: 66 of 66 no-ticker rows with a CUSIP are named. The master carries no
     ticker for any of them, so only the name is filled.
   - NEXT: ONE OpenAI classification run (B_01b's method) over the named unclassified rows only (COT 101, 49F 78,
     INF 108). This is Andrew's per-use word; there is no second run. First freeze the exact input list (ids, names,
     count) as a file.
   - Then a never-widen half to the CTO for the `bd-securities` write, naming the flipped securities and their
     readers (69 paths, Positioning included).
   - The classification rule: investment real estate such as a REIT is `alternatives`; personal and held-away assets
     are the new class `other`. The Holdings enum and the contract gain `other`. ~D colours it through Positioning's
     existing mapping.
   - The two defects (COT `B_01b` scanning an empty prefix; the loader skipping rows without a ticker) are ~M's under
     exact-file grants on request. The loader's sign-off counts the securities that flip from NONE.

Done this lease:
- The investor_reporting suite is green, 267 passed and 0 failed, on the M branch @1848e5caef and on merged CLOUD.
  Each stale test's premise is pinned (unattested currency, the required Eclipse capture, the lib.opal_naming
  binding); no assertion was loosened.
- The deployed `refresh.py` is landed on CLOUD @fecbf0dc43. Before it, CLOUD carried neither S125 fix, so the next
  build from CLOUD would have rolled the directory back to the 09-17 freeze. The deployed zip's `refresh.py` equals
  a7e5c59042's by content.
- `holdings/tests` on CLOUD: 147 passed and 0 failed. ~P's parked "44 fail" belongs to ~P's worktree HEAD, not CLOUD.

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Merging CLOUD into a seat branch is REFUSED by the law-lock budget: `.claude/skills/canonical-flow/SKILL.md` is 52,132 bytes and `dispatch/SKILL.md` 33,599, against 25,600 (org/law-edit-audit.log line `2026-09-24T23:04:17Z REFUSED-BUDGET author=2.0.0_SA_COO~M`) | 1.0.0_SA_CTO (the skills' owners) | the two files shrink under budget, or the gate exempts a merge carrying files the author did not change |
| Public reason for a selected account with no custody row: NOT_READY (transient) vs NOT_FOUND (`_authz/errors.py:58`) | 1.0.0_SA_CTO (contract) | the CTO rules the code |
| The FULL -> FAST line to the CVO ("FAST from 18:1xZ; pins graded after the fact") | 2.0.0_SA_COO~M | 3.0.0_SA_CVO registers live |
| `directory/tests` on CLOUD has 6 failures that predate the refresh port (control: unmodified HEAD, the same 6): test_custody_owner.py x4, test_entry.py x2, AttributeError 'NoneType' has no attribute 'headers' | 2.0.0_SA_COO~P (directory-search entry and custody owner) | the next change to directory/entry.py or the custody owner read |
| IRPT_BCKEND-S124: the bundle mint reads working-tree bytes | owner of .tools/safe_deploy_core.py | next bundle re-mint |

Done: the directory refresh is fixed and EXERCISED. The 09-25 13:30Z fire dispatched at all 3 firms; served directories
49F 09-24, INF 09-25, COT 09-22 (were 09-17). Ledger irpt-directory-refresh-s125-m-20260924 CLOSED @2e4c33738e; S125
disposed REMEDIED (S129).

## Limits

- No CVO verdict on any criterion.
- Two acts this session wrote served state:
  - the directory refresh deploy (ledger A1 closed, S1 open);
  - the three classified Holdings republishes (receipts).
