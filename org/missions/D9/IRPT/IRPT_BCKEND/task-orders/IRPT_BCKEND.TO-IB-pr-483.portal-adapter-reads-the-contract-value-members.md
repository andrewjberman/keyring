# TO IRPT_BCKEND.TO-IB-pr-483 -- BUILD ONLY (a portal candidate): the portal adapter reads `start_value` and `end_value` from `value_facts` (C-VALUEFACTS), keeping the market-value names as a read for the Black Diamond path only

<to_id>IRPT_BCKEND.TO-IB-pr-483</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~338</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>167</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6517 (PRD ADDENDUM v0.51 section 2 item 3, step 1; ROUND-166 ANALYSIS section 2 row D2-W321-S1; contract C-VALUEFACTS, ADDENDUM v0.50 line 1320) | **Decomp cell:** `IB-pr-483` (decomposition section 159) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-338/` (bash `/c/dev/wk-irpt-bckend-338`). **Two repos.** `C:/dev/wk-irpt-bckend-338/portal` is a PORTAL worktree (its own git repo, cut from the portal `DEV` head `53506d4903aeabac675d87b7fe208fc9945c8ce7`; verify with `git -C portal rev-parse HEAD`). Portal files commit in the portal repo with plain git and your author line;
records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `git rev-parse HEAD` in the WORKSPACE repo before your first commit there is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY a portal candidate. No AWS call, no live request, no sign-in, no portal push, no DEV or PROD act, no dev-server or browser run, no `bun install` (the worktree's `node_modules` is a link; leave it). Every value in a test is SYNTHETIC; no real account, client or figure appears in any file.

**Why (read `deliverables/0.9.0_WK_IRPT_BCKEND~334/IB166-4_value_facts_readers.json` and its READ file first; the portal part is yours to re-read at the DEV head).** PRD ADDENDUM v0.50 names the contract C-VALUEFACTS: `optional_facts.value_facts`, when not null, carries `start_value` and `end_value`. Three backend emitters write those names (`holdings_gold.py`, `f49_engine.py`, `orion_adapter.py`); `bd_adapter.py` alone writes `beginning_market_value` and `ending_market_value`
(its rename is a separate order in this round). The portal adapter, `src/pages/InvestorReporting/contracts/adapt.ts` (about lines 797-800 and 839-840 at the portal checkout `dbeb6764ea`; the DEV head's file differs by about 60 lines, so read it AT YOUR WORKTREE, not from the older checkout), reads only `beginning_market_value` and `ending_market_value`, so for holdings, 49F and orion answers the value tiles
(`tabs/reporting/PerformanceHeadline.tsx`, `render/performance/Summary.tsx`) read "not supplied" today. The CTO's order for this pair (analysis @1cfe2eb0df section 2, ruling D2-W321-S1) is **reader first**: step 1, this order, the portal adapter reads the contract members and keeps the market-value names as a read for the Black Diamond path ONLY until `bd_adapter.py`'s rename is live;
step 2, the rename (another order); step 3, the pair's close: the fallback is removed (a later order, not this one).

**Build (one change, small).** In `adapt.ts`, the opening and closing value come from `value_facts.start_value` and `value_facts.end_value` for every provider path. For the Black Diamond path ONLY (find how the adapter tells that path apart, by the answer's basis or provider member, and cite it), if the contract member is absent the adapter falls back to `beginning_market_value` and `ending_market_value`. For every other path there is NO fallback to the market-value names.
Keep every other behaviour: the `supported` flag, the window and currency match, `finiteValue`, the "not supplied" rendering when a value is absent, and the unavailable reasons. State in the record (`fallback_removal_condition_in_words`) the condition at which the fallback is removed (the rename live on every emitter, shown by the pair's consumer read).

**Tests (the candidate's own, in the portal worktree):**
- NEW `portal/src/pages/InvestorReporting/__tests__/value-facts-members.test.ts`, run as `bun test src/pages/InvestorReporting/__tests__/value-facts-members.test.ts` from the portal worktree: at least THREE tests over synthetic wire answers: (1) a holdings-path answer carrying `start_value`/`end_value` supplies both tiles' values; (2) a Black Diamond-path answer carrying only the market-value names still supplies both (the fallback); (3) a non-Black-Diamond answer carrying ONLY the market-value names supplies neither (no fallback), and an answer with neither supplies neither (`unavailableReason` as today).
- The existing `portal/src/pages/InvestorReporting/__tests__/fe-s-5/performance-wire-journey.test.ts` pins the market-value spelling (5 pass at the older checkout). Update ONLY what must change for the new read, keep its intent, and weaken no assertion; it must pass (`0 fail`).
- After your portal commit run `bun run lint` and `bun run typecheck` from the portal worktree; a lint ERROR is fixed before you report; record both results (the counts of errors) in the record. Do not fix findings in files you did not change; report them.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~338/IB167-3_portal_candidate_record.json`: `{base_commit, portal_base_commit: "53506d4903aeabac675d87b7fe208fc9945c8ce7", portal_candidate_commit: <your 40-hex portal commit>, portal_files_changed:[paths relative to the portal root, all inside src/pages/InvestorReporting/], black_diamond_path_test_in_words, market_value_names_kept_for: "black-diamond-path-only",
fallback_removal_condition_in_words, tests:{new_file:{pass, fail}, wire_journey:{pass, fail}}, lint:{errors_before, errors_after}, typecheck:{rc_before, rc_after}, pushed:false, not_established:[...]}`.

<criterion id="IB167-3-AC1" cell_refs="IB-pr-483"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-3-AC1</invocation><expect>IB167-3-AC1 PASS</expect></criterion>
<criterion id="IB167-3-AC2" cell_refs="IB-pr-483"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-3-AC2</invocation><expect>IB167-3-AC2 PASS</expect></criterion>
<criterion id="IB167-3-AC3" cell_refs="IB-pr-483"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-3-AC3</invocation><expect>IB167-3-AC3 PASS</expect></criterion>

<expected_criteria>IB167-3-AC1, IB167-3-AC2, IB167-3-AC3</expected_criteria>

What the checks grade: AC1 your new test file exists in the portal worktree and at least 3 of its tests pass with 0 fail (`bun test`, run from `<root>/portal`); AC2 the wire journey test reads 0 fail (AC2 PASSes at base BY DESIGN: it is the regression guard); AC3 the record: both portal commits are 40-hex, the base equals the DEV head named above, `portal_files_changed` equals `git diff --name-only base candidate` in the portal repo and sits inside `src/pages/InvestorReporting/`, the fallback is kept for the Black Diamond path only, `pushed` false.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Edit no backend file; do not touch `bd_adapter.py`; do not remove the market-value read for the Black Diamond path.
- **Refusal clause:** if the adapter cannot tell the Black Diamond path apart from the others by what the answer carries, STOP, file a row and report; do not guess a discriminator. Never weaken a check or a test; do not edit `p167_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W338-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Workspace commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~338" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~338@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~338 <0.9.0_WK_IRPT_BCKEND~338@opal.agent>" -F <msgfile> -- <workspace paths>`; the **portal commit** is plain `git -C portal commit` with the same author and committer values, message from a file written with the Write tool OUTSIDE the worktree. ASCII only. Do not push.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/__tests__/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~338/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-483.portal-adapter-reads-the-contract-value-members.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 159 (round 167, workstream ~P), cell `IB-pr-483`.
<owned_cells>IB-pr-483</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB167-3-AC1, IB167-3-AC2, IB167-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~338/IRPT_BCKEND.TO-IB-pr-483.portal-adapter-reads-the-contract-value-members.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base and the portal base; how the adapter tells the Black Diamond path apart (cite); the change in a sentence; the new test's arms; the wire journey test before and after; lint and typecheck before and after; the fallback's removal condition; each criterion's last line; the proof checker's result; both commit hashes (portal and workspace); row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell edits one portal adapter file and its tests in a portal worktree; nothing is pushed, built for PROD, deployed or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p167_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~20:4xZ: IB167-3 AC1 FAIL (the new portal test is absent), AC2 PASS (the regression guard: the wire journey test reads 5 pass at the portal checkout dbeb6764ea), AC3 FAIL (no record); commit-gate clean. The issuer read adapt.ts:839-840 at that checkout (the market-value names); it did NOT read the DEV head's adapt.ts, which differs by about 60 lines. bun 1.4.2 runs the test file here.
lane: the <paths> block IS the grant. Class LOCAL: a portal candidate with no infra path and no deploy verb; it lands nowhere until the pair is signed. A portal product file: the CTO reviews the candidate; a PROD push that changes a client-facing page (the Reporting tab is one) waits on Andrew's word, which this order does not seek.
</preflight>
