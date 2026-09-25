# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Lease FAST `IRPT_BCKEND~M`, extending while Andrew is active (drive-mode.log). Goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`
(Done = /verify SOUND). The 20-minute goal loop reads this lease first on every tick (C11). Reviewer: `3.0.0_SA_CVO`
(not live; the FAST line is parked below). As of 2026-09-25T15:4xZ.

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
2. **CTO R5, with Andrew's two answers** (msg 100951;
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260925_144xZ_CLASSIFIER_OTHER_OPENAI_RUN_AND_DEV_PUSH.md`
   @705be61575). Done so far:
   - **49F fill:** no-ticker rows named from the Schwab master (cb8cd03113); 66 of 66 with a CUSIP on the 09-24 dry
     run.
   - **INF fill:** rows named by Orion's own `name` (e0f680f0df). The served "names" were masked CUSIPs. On the
     CURRENT table, 121 of 124 masked rows classify with no write. 1,541 of 31,170 INF answers move: 960 from NONE, and
     581 off a ticker-shape `equity`, all at $0.
   - **The ONE OpenAI run:** 285 of 285 answered, 0 invalid, 8 needs_review (input sha 0bafa803..., 8c1e79083b;
     results 9c769fba15). Andrew's rule reads back: Voya and the Home are `other`, the Eiger LPs and the Vornado REIT
     are `alternatives`.
   - **The write set:** 41 of the 285 keys already exist in bd-securities, and B_01b's own rule excludes them, which
     leaves 244 new `NAME::` keys. Over those 244: 112 unchanged, 128 NONE to a class (66 equity, 37 other, 16
     fixed_income, 9 alternatives), 4 flips (2 fixed_income to alternatives, 2 preferreds fixed_income to equity).
   - **Batch A is WRITTEN.** The CTO signed 204 keys (the three preferreds struck; @8214723353). Ledger
     bd-securities-batch-a-m-20260925 is CLOSED @f99c664dd0: 204 of 204 put, 0 condition refusals, read-back 204,
     and a fresh loader classifies 204 of 204 by name. Census sha e7b289a26d08a3f4; receipt 9f84ff97ee (M branch).
     Holdings classes these at its next publication; COT C_06 moves about $21.6M out of equity at its next run.
   - **Batch B (37 `other`) stays held** until: C_06 admits `other`; D_03 and D_04 separate their unknown sentinel;
     the Holdings enum and the v1 contract admit `other`; ~D maps it.
   - ORDER: Holdings must admit `other` (ASSET_CLASS_VALUES and the v1 contract) BEFORE the write, because
     classify_security refuses a class outside its enum. ~D colours it.
   - The two defects (COT `B_01b` scanning an empty prefix; the loader skipping rows without a ticker) are ~M's under
     exact-file grants on request.
3. **The scheduled daily Holdings producer is ~M's** (CTO R4, msg 100947;
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_IRPT_20260925.md` @75156f2b18):
   - Plan: `HOLDINGS_SCHEDULED_PRODUCER_PLAN_20260925.md` @875dc1f64b (M branch). 7 prerequisites are measured;
     rows 3 (package) and 5 (the local-only retained inputs) block a fire.
   - Step 1: DONE (code on CLOUD).
   - Step 3 is answered by 2.0.0_SA_COO~P (msg 100955): the resident runner REJECTS a holdings message
     (resident_worker.py:262-270 routes resolve_upload only). Every fire would be a poison message ending in the DLQ,
     so the retarget is ~M's.
   - The candidate target is the directory refresh's own path: an SSM dispatch to the mdpf-daily-runner. It needs
     the host's IAM (mdpf-pipeline/iam.tf grants "the directory chain's prefixes, and NOTHING wider") and a package
     under the 2,048-byte S3 metadata cap: 17 members measured 2,440 bytes, so a separate holdings bundle.
   - Step 4 (the enable) goes to the CTO as a never-widen half.

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
| The M branch's last merge (batch A script, receipt, plan) was REFUSED because the shared index carried 4 staged ledger-open files belonging to other seats (irpt-render-keys-a1, pm-autosave-list) | 2.0.0_SA_COO~M | those seats commit their ledger opens; then safe-merge again |
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
