# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Lease FAST `IRPT_BCKEND~M`, extending while Andrew is active (drive-mode.log). Goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`
(Done = /verify SOUND). The 20-minute goal loop reads this lease first on every tick (C11). Reviewer: `3.0.0_SA_CVO`
(not live; the FAST line is parked below). As of 2026-09-25T21:3xZ (tick 15). Loop: /canonical-drive, HOURLY since 19:5xZ (was cron 6f699621 at 10m; every remaining item waits on another seat or the Monday host window) (Andrew-direct ~17:3xZ, @42def02a36); goal cron b26f74dc retired into it.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `codex/irpt-m-completion` at `../ajb_irpt_m`; MERGED into CLOUD through @de042e1e4b (batch A, retained inputs, COT screen); merged CLOUD 420 tests passed |
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
   - **Batch B (37 `other`) stays held.** Its prerequisites:
     - Holdings enum and contract: DONE (~P @3d5a590ad0; ~M @82eaf1a581).
     - ~D's IR `other` mapping: on local DEV 959a59a2 (TO-IV-e-27); origin DEV follows via the CTO and MSTR.
     - COT gold (CTO 101022, ~M owns it): census @c2aa94d8c8; code: C_06 admits `other`, D_03/D_04 unknown ->
       `unclassified` (7889280827, CLOUD 68a732b792, NOT deployed); per client: 22 relationships, $48.5M
       (COT_OTHER_PER_CLIENT_20260925.json).
     - SIGNED: act 1 by the CTO @4fdc4284c9. ACT 1 DEPLOYED and verified (ledger cot-other-admission-m-20260925:
       D1 closed; R1 HELD for the first scheduled COT run, Mon 2026-09-28).
     - Act 2 (the batch B write) is held on: act 1 read back; ~D's IR mapping on origin DEV; and (CTO-added) the AI
       Cottonwood views rendering Other on PROD, proven on z09305589's $19.65M, which the CTO routes to ~D.
     - S138 is ~M-owned and MEASURED (S139 @5cc4fc3367): C_06 drops $19.23M of `cash` across 178 clients, and 2
       all-cash clients publish an all-zero mix. The CTO SIGNED cash as its OWN deploy (@d257eb67aa, msg 101038):
       only after the AI Cottonwood views render cash and `other` on PROD (added to ~D's order). The read-back names
       one client's cash slice summing to 1 and one all-cash client at 100%. The cash line is WITHDRAWN from the M
       branch (b6cfa36f91) so no merge carries it early; re-apply 74feb04b1e then.
   - Preferred stock = fixed_income, standing (Andrew-direct ~17:3xZ, @42def02a36).
   - The two defects (COT `B_01b` scanning an empty prefix; the loader skipping rows without a ticker) are ~M's under
     exact-file grants on request.
3. **The scheduled daily Holdings producer is ~M's** (CTO R4, msg 100947;
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_IRPT_20260925.md` @75156f2b18):
   - Plan: `HOLDINGS_SCHEDULED_PRODUCER_PLAN_20260925.md` @875dc1f64b (M branch). 7 prerequisites are measured;
     Row 3 (package) blocks a fire. A real 49F+INF build traced at 16:1xZ loads 16 repo modules and opens 11 data files
     (the registry JSONs, NAMING_SCHEMA, CurrencyAuthorities, the contract, firm_registry), plus the classifier and
     COT's modules, so 30 or more members. A per-member sha stamp cannot fit the 2,048-byte cap; the package needs a
     hash manifest INSIDE the tar with one digest in metadata. DONE as opt-in `"stamp": "manifest"` in
     safe_deploy_core (7d3e4255a8, test fix cc4eeb51d2, M branch): the declared bundles build byte-identical, and 40
     members fit the cap. Traced closure on CLOUD (run_firm for all 3 firms, no env
     vars, no upload): 29 modules and 11 data files = 40 members. Keys from address(): one package per firm at
     s3://opal-data-{49financial,inflection,cottonwood}/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz.
     Constraint found: CODE_TREES bundles are commit-routed (bundle_for_member returns the FIRST bundle; a
     non-distribution member LEAVES its loose leg). The closure holds 12 MDPF gold scripts, lib/ and the registry
     JSONs, so declaring it there would freeze other pipelines' deploys. DONE: STANDALONE_BUNDLES (ec48c5d144, M branch):
     irpt_holdings_{49f,inf,cot}, 40 members each, manifest-stamped (92 bytes of metadata), never commit-routed.
     MERGED to CLOUD @4f58a95c84 (432 tests passed). The PACKAGES ARE MINTED from CLOUD: ledger
     irpt-holdings-packages-m-20260925 CLOSED; irpt_holdings_{49f,inf,cot} at
     s3://opal-data-<firm>/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz, members-sha256 83f6a81aab34.
     Remaining in R4: Terraform for the dispatch function and the schedule retarget (kept DISABLED), and row 4b as
     ONE principal per firm holding exactly its reads and writes. The fence denies the host role, and a firm
     principal is NEVER-WIDEN-CLASS (R-44), so both halves are needed before any apply. Grants were measured from each
     firm build's receipts (plan addendum 2), then from EVERY botocore call:
     HOLDINGS_FIRM_PRINCIPAL_GRANTS_20260925.json (4e995812bb). No read crosses into another firm. The Terraform
     is COMMITTED on CLOUD under the CTO's exact-file grant @800e5c8f75 (ce30073582; merge 33972b6da8). Real plan
     (-lock=false): 10 to add, all ~M's (3 holdings roles and policies, the dispatch role, policy, attachment and
     log group). It stops at the missing Lambda artifact: its lambda-source-map member is ~P's lane, and a grant
     is asked of the CTO (msg 20260925T190215Z; the diff is ready). The plan ALSO shows
     irpt_directory_refresh cron(30 9)->cron(0 9): ~P's S126 fix lives only on ~P's branch, so an apply from CLOUD
     would revert it. S135 is DISARMED (S136): ~P's fix is landed at afefa09d7e, and the re-plan reads 10 to add,
     0 to change. The dispatch moved to its own granted dir holdings_refresh/ (CTO @8f23a84826; 4a49b03031), and its
     artifact is built and uploaded (ledger irpt-holdings-refresh-artifact-m-20260925 CLOSED @a045790a3b). Full plan:
     11 add / 2 change / 0 destroy, all R4's. BOTH HALVES ARE SIGNED (COO @885ae2f3d6, CTO @6c5c27a666), and it is
     APPLIED: ledger irpt-holdings-principals-dispatch-m-20260925 has P1, AP1 and V1 closed (@253d92d48b).
     - The first apply half-landed: IAM refused the 3 firm policies because the grants record's dynamodb_scan was
       empty. Fixed @674a9c02f6 and finished in-session; a fresh plan reads No changes.
     - Read-back: the schedule is DISABLED with target irpt-holdings-refresh-lambda; the CodeSha256 equals the
       artifact's; 4 of 4 policies equal the planned JSON.
     - N1 (the exercised negative arm) is HELD until the host's next window, Mon 2026-09-28 ~12:52Z. Interim
       simulation: cross-firm reads are implicitDeny, own reads allowed.
     NEXT, Monday in the window: N1 over SSM as each principal; one --qa fire (the dispatch function invoked with
     the runner writing holdings_qa); then the ENABLE half to the CTO (R4 step 4). ~P is told that the holdings/
     resolve.py pin drift refuses its next build.
     Then the never-widen packet (both halves), the apply, one --qa fire, and the enable half.
     Row 4a DONE (3e1ca981ab): the publication writes through a firm-scoped publish principal when the dispatch
     names one (IRPT_HOLDINGS_PUBLISH_ROLE_ARN); reads stay on the host (R-44 split by bucket). Rows 2 and 4b are
     designed in the plan addendum (M branch). NEXT: the CLOUD merge (another seat's staged
     trade-cash-indicator ledger file blocks it), the mint from CLOUD under a ledger, then row 2's dispatch
     function and row 4b's principals (infra, safe-apply).
     Row 2 CODE DONE (0154b4f03a): refresh_dispatch.py sends one SSM command per firm, verifies SHA256SUMS,
     exports the firm principal, and is stateless (the previous outcome comes from SSM history). The local host-script
     run from the extracted 40-member COT package built with rc=0. Owed: Terraform (function, schedule DISABLED,
     roles) with row 4b. Merge to CLOUD is waiting on other seats' staged files.
   - **S131 / S134 DISPOSED** (S137 @d3ab268cb0, GRADUATED). Explained at 9c0fb0c8f2: the served COT revision is a BOUNDED publication of 841 of 981 accounts.
     The 53 repeated relationship groups sit in 2 unserved accounts ($729,826.75). The source is unchanged (same
     version and sha as served). A full-firm (scheduled) COT build refuses the whole firm for those 2 accounts.
     **DONE** @ce64116275 (M branch): a full-firm COT build screens each account and refuses the account, not the
     firm. Live run at cutoff 09-24: 981 / 841 / 140 (138 missing fields, 2 repeated rows), valid, $548,412,662.59, and
     the 841 built accounts equal the served set. The 140 are carried as explicitly refused, with reasons.
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
