# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Lease FAST `IRPT_BCKEND~M`, extending while Andrew is active (drive-mode.log). Goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`
(Done = /verify SOUND). The 20-minute goal loop reads this lease first on every tick (C11). Reviewer: `3.0.0_SA_CVO`
(not live; the FAST line is parked below). As of 2026-09-27T04:0xZ. Paused 15:27Z-16:03Z (Andrew-direct, CTO 101278/101295); loop re-armed as cron 75ed13d3. Loop: /closer-drive at 30m (cron ae118e19; CTO msg 101099, self-drive arm @ce6aa15a17, FAST to 15:01Z). Loop: /canonical-drive, HOURLY since 19:5xZ (was cron 6f699621 at 10m; every remaining item waits on another seat or the Monday host window) (Andrew-direct ~17:3xZ, @42def02a36); goal cron b26f74dc retired into it.

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
branch. COT `C_06`, `D_03`, `D_04` and their tests on branch `irpt-m-cot-cash-line` (`../ajb_irpt_m_cashline`,
head ccb9b38dd8, NOT merged). ~X's order is DONE: `ds-x-b1-cashline` @146876e75a (~X msg 101682); ~M's `irpt-m-s152`
(`../ajb_irpt_m_s152`) is cut from it and adds 41115a70aa (S155: COT mix_views admits cash/other) and 9135feae97
(comp-constants patch). S155 rides the cash-line act ALONE as re-cut `irpt-m-s152-cloud` @ff63895521 (CTO
101688, CRO 101686; name it in the Monday ledger entry). Read-back per period row: |cash + other + unclassified_after -
unclassified_before| <= $0.02 and total EXACT, else roll back (CTO 101700 @7eb19f44e3; s152_period_view_identity.py); ~X's B1 commits go under ETF Part B's own ledger. No branch is
merged; the drain is Monday after R1, COT gold last. The cash-line ACT merges `irpt-m-cot-cash-line-act` @0deac23f1e;
ccb9b38dd8 (COT B1) is split to `irpt-m-cot-b1` for B1's ledger. Monday order: IRPT_MVP_M/MONDAY_20260928_RUNBOOK.md.

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
     - Act 2 (the batch B write) is held on: act 1 read back (Monday's first COT run); ~D's IR mapping on origin
       DEV. The CTO-added render condition is MET: PROD 36a37afc (tag portal-v2.1.188, ~D msg 101054), whose
       cottonwood/layout.ts:125-128 turns on cash and other. ~D reads z09305589's Other slice once batch B lands.
     - S138 cash is DEPLOYED as its own act (CTO @d257eb67aa). Re-applied 7fd8149448, merged to CLOUD 75cc52a285, and
       C_06 is on s3://opal-data-cot/code/gold/ at version LmvfjXlB... (read-back: line 173 carries cash; rollback is
       prior version HJa2V4VY..., the act-1 bytes). Ledger cot-cash-admission-m-20260925: D1 closed; R1 HELD for
       Monday's first COT run: z09308463 (0.37 cash at 09-22) shows a cash slice with shares summing to 1, and
       z09326138 or z09308511 shows 100% cash.
   - **COT-new write (CALL 2, @37025a10e9) + batch B re-cut:** the ONE OpenAI run answered 1,012 of 1,012 (file only,
     @c3dde578b9). Andrew ~02:3xZ: established equities stay; `other` is personal held-away assets only. The write set
     is 967 keys (R1 7, R2b 35, R3 10 excluded): Part 1 has 941 keys (COT $12.99M, BD $7.31M of corrections) and Part 2
     has 26 `other` keys (COT $48.72M, 20 relationships). Half requested of the CTO:
     IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_COT_NEW_WRITE_20260926.md; it replaces batch B act 2. The B_01b auto-deploy
     is DISARMED (S141).
     - SIGNED by the CTO @ab4a2e41bb, with an a07 precondition. a07 measured: 49F 10 keys $56,952, INF 8 keys $0,
       COT 122 keys, 0 outside the keys. **PART 1 WRITTEN** @aaef2843a8: 941 of 941, 0 refused, read back 941. The loader
       agrees on 935; 6 NAME:: duplicates serve fixed_income through a ticker sibling, +$149,663 vs the half. They are
       ALIGNED to fixed_income on ~M's REC (served DELTA=0 verified, COT 19,510 + BD 108,849 rows; ledger
       bd-securities-cot-new-align6-m-20260926 CLOSED @1d2b27a1c2). Ledger bd-securities-cot-new-p1-m-20260926: R1 HELD for Monday's COT and BD
       runs.
     - Part 2 (26 `other`) is signed and waits on the act-1 read-back (Monday) plus ~D's mapping on origin DEV.
     - **Part 2 ALSO waits on d08 (and d06) admitting `other`** (both raise on it; CTO 101639, item 9 of ~X's order).
     - **B_01b deploy PARKED by ~M** (see Parked): it is not in COT's scheduled chain, and a deploy would re-send the
       excluded keys.
     - Part 2's second condition is MET: ~D's IV-e-27 (959a59a2) is an ancestor of origin/DEV and origin/PROD (fetch
       + is-ancestor read by ~M 03:3xZ). Part 2 waits only on the act-1 read-back.
   - Preferred stock = fixed_income, standing (Andrew-direct ~17:3xZ, @42def02a36).
   - The two R5 defects (IRPT_MVP_M/R5_CLASSIFIER_DEFECTS_20260926.md):
     - The loader skip is CLOSED with no change: `ticker` is bd-securities' HASH key, and batch A's 204 name-keyed
       items classify by name.
     - COT `B_01b` should list `gold/canonical/holdings/` (121 partitions). On 09-22 it would find 574 new keys
       ($145.07M of $549.14M). FIXED in code under the CTO grant @930e0f348f: 8f67065e50, CLOUD e20b0990d5. The prompt
       now follows Andrew's rules (REIT -> alternatives, preferred -> fixed_income, held-away -> other). The dry run
       over 121 partitions finds 1,253 new securities. Not deployed, not uploaded: that needs Andrew's per-use OpenAI
       word, then a never-widen half on the classified file, then the write and the deploy under ledgers.
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
     Monday is PRE-STAGED: r4_monday_negative_arm.py (--send / --read), and the exclusive trust is already shown
     (Andrew_Berman's AssumeRole on the 3 firm roles -> AccessDenied, 3 of 3). NEXT, Monday in the window: N1 over SSM
     as each principal; one --qa fire (the dispatch function invoked with
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
| COT serves 6 stale D_03 composition files (data_as_of 08-25, 08-28, 09-18; 2 each) that D_03 no longer rewrites (COT_SERVED_COMPOSITION_BASELINE_20260927.json) | 2.0.0_SA_COO~M (COT gold grant) | after Monday's run: if they are still stale, a delete needs a human confirmation |
| d08 (runners_cot, QA emit only) refuses its byte-schema identity once the LIVE `platinum/firm/mix_summary.json` carries `cash` (Monday's run onward) and, after the drain, the new classes; S151 (its frozen 3-class `mix{}`) is the same shape | runners_cot owner (none live; 1.0.0_SA_CTO routes) | a runners owner is seated, or d08's refusal blocks a served act |
| At the ~X drain: drop the branch's copies of rows S150-S153 (they are on CLOUD as S153-S156 @92244581d2, CTO 101771); CLOUD's S150-S152 stay | 2.0.0_SA_COO~M | the ~X drain |
| ~P's S152 (CLOUD): served INF holdings as-of 09-22 vs directory 09-25. Cause measured: INF upstream complete through 09-26 (0 refusals); no publication since the 09-24 republish because the schedule is DISABLED until R4 ENABLE (~P msg 101769 answered) | 2.0.0_SA_COO~M | the first enabled publication serves INF at or after 09-25 (Monday runbook D) |
| IRPT_BCKEND-S124: the bundle mint reads working-tree bytes | owner of .tools/safe_deploy_core.py | next bundle re-mint |
| COT B_01b deploy. The skip list (52 ruled-out keys + Part 2's 26) and the rule-2 prompt are BUILT on branch irpt-m-b01b-skip @c993550, NOT merged, because a CLOUD commit deploys on the next push. Dry run: 0 new securities, so a first upload makes no OpenAI call. S3 still serves the no-op (S141) | 2.0.0_SA_COO~M | COT's chain adds B_01b: merge + safe-deploy as ONE act under a ledger |

Done: the directory refresh is fixed and EXERCISED. The 09-25 13:30Z fire dispatched at all 3 firms; served directories
49F 09-24, INF 09-25, COT 09-22 (were 09-17). Ledger irpt-directory-refresh-s125-m-20260924 CLOSED @2e4c33738e; S125
disposed REMEDIED (S129).

## Closed this lease (09-26)

- S145 (the 49F $0.00 Holdings, CTO 101295): a TRUE ZERO. The three accounts are $0.00 in every Schwab dim_balance field on
  09-22 and for at least 3 months before. S146 DISMISSED_WITH_REASON @5bee820159. The shared '****4304 / IRA' label is
  the relationship-level discriminator by design; a display ruling is asked of the CTO.

- ACCOUNT own-mask labels (CTO 101302): code on CLOUD 5d5678d6c1; both halves signed (CTO @45bafa24a1, CRO @c412578ede).
  The served-as_of rebuild is a STOP at all three firms (@4fd998322e), so the labels ride the first scheduled publication.
- R4 enable half, first read of its required diff (CTO 101343): IRPT_MVP_M/R4_ENABLE_DIFF_20260926/README.md. With the
  served source partitions pinned there are no amount, node-set or clock changes at any firm; labels and classes trace to
  signed halves; INF's 30,881 name facts (e0f680f0df) are the one class no signed half covers. Re-run at Monday's fire.

- **Monday's QA fire made safe (R4 step 3):** the dispatch had no QA mode, so every fire ran `--upload` into the SERVED
  table. {"qa": true} now publishes to holdings_qa (1eec202d22, CLOUD 145c5e6494). Redeployed under ledger
  irpt-holdings-dispatch-qa-m-20260926 (CLOSED): CodeSha256 SGwrvwLH... equals the artifact; schedule DISABLED;
  re-plan No changes. Monday: `aws lambda invoke --function-name irpt-holdings-refresh-lambda --payload '{"qa": true}'`.

- **ETF Classifier tags win (Andrew-direct ~21:2xZ; CTO 101511 ruled (a)):** `structured` and `commodities` become
  classes. Half @09cd2a3e50, with a reader census (69 paths plus those added since). CTO signed (101540):
  - Part A: 16 keys SIGNED (CTO @c516dab84b, msg 101547; CRO msg 101552), riding R4: the 15 puts plus VNQ to
    alternatives. Andrew-direct 00:1xZ 09-27: "VNQ is alternatives, it's a REIT"
    (ANDREW_DIRECT_20260927_001xZ_VNQ_IS_ALTERNATIVES_REIT.md). CASH is dropped (Pathward stock).
  - CASH is a ticker collision: bd = Pathward Financial stock (49F, CUSIP 59100U108); ETF row = a synthetic cash row;
    COT's 620 "CASH -- CASH" nodes ($2.87M) are BD's cash line, served as equity. REC to the CTO: drop CASH, and fix
    COT's cash line by row (~M's C_06 grant, own half).
  - Part B SIGNED as a sequence: guard the seeds, then B1 readers admit (3 RAISE, 11 silent drops today; owners named),
    then a re-census at 0/0, then B2 writes 13 keys, then B3 Holdings. ~D has the portal lines (v0.14). CRO half requested.

- **COT cash line (CTO 101547):** BOTH HALVES SIGNED on 9e3f568d42 + 0deac23f1e (CTO 101597/101616; CRO 101595,
  101629). Negative-cash census @eaca6a30de: 17 of 29 relationships net negative on the cash line; C_06 moves
  +$66,055,897.80 (positive rows only). D_03 ruled (a) (CTO 101616): positive-rows rule; 0 of 223 compositions over
  100% before and after; firm + 27 relationships' mix moves (@625e331ded). The 3 personal liabilities in z09305672
  classify `equity` today; they are already among Part 2's 26 `other` keys (signed @ab4a2e41bb), so no new half. DEPLOY: Monday, after R1 of
  cot-cash-admission-m-20260925; merge the branch, safe-deploy C_06/D_03/D_04 under one ledger; read back z09305653's
  cash slice, 0 over 100% (`cot_served_composition_check.py`; the served baseline has 9 over 100%, written 09-23 by
  the July D_03, addendum 4), and d08 beside C_06.
- **B1 reader admissions (CTO 101573/101578):** ~M's COT C_06/D_03/D_04 admit structured/commodities @ccb9b38dd8 (same
  branch; D_04's firm mix now reads every C_06 class). `0.4.0_DS_ClientPlatform~X` SEATED under
  IRPT_MVP_M/WORK_ORDER_DS_X_B1_AND_CASH_LINE_20260926.md (amendment 1 @8b45af0917): a07/d08 cash line, d06/d08/BD
  C_06/D_03/D_04/both mix_views admit, d06/d08 admit `other`. Seating exception to CONTRACT.md:3 (CTO 101639). ~P:
  contract enum admits both (d3c5467ce1, ae32ac98d7). B2 still waits on: ~X's and ~M's B1 code landed; ~D's C34 SERVED (on LOCAL portal DEV a28c0172 only,
  not origin DEV or PROD, ~D 101648; the AI half TO-IV-e-46 is at CTO review); then a re-census at 0 RAISE / 0 drop.

## Limits

- No CVO verdict on any criterion.
- Two acts this session wrote served state:
  - the directory refresh deploy (ledger A1 closed, S1 open);
  - the three classified Holdings republishes (receipts).
