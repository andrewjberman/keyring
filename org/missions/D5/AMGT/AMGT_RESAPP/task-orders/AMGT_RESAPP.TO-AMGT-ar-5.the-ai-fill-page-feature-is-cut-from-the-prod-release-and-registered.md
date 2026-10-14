# AMGT_RESAPP task order -- `AMGT-ar-5` -- THE AI-FILL PAGE FEATURE IS CUT FROM THE PROD RELEASE AS `cand/dell1/aifill-blocks-prod`, WITH ITS RECEIPT AND ITS APPROVAL ROW (A PORTAL BRANCH; NEVER DEV, NEVER PROD, NEVER PUSHED BY THE WORKER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ar-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~429</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ar-5.the-ai-fill-page-feature-is-cut-from-the-prod-release-and-registered</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository and one registry row; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, bun and the open-calls tool only.
comp-adversary: RUN at the cut -- `r103_feature_surface_check.py --selftest` reads `arms passed 7 of 7` and `R103 FEATURE SURFACE ARMS: YES` (the check `AMGT-bk-6` used); the re-cut branch does not exist yet, so its own run (AC3) is the order's proof, and it must read YES on exactly the eleven files below with no forbidden or unnamed file. EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-429` (branch `wk-AMGT_RESAPP-429`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-429`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-ar-5` (round 104, workstream AIFILLLAND, decomposition s.10)

The CTO APPROVED the AI-fill page candidate `cand/dell1/aifill-blocks` @`85d5749f` as Opal-internal (call `dell1-20261013T234218Z-cf85`, `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_APPROVAL_PORTAL_CAND_AIFILL_BLOCKS_20261014.md`, msg 5283) and ruled that it lands as a FEATURE CUT FROM THE CURRENT PROD RELEASE through the portal's contributing-boxes flow
(`portal/CONTRIBUTING-BOXES.md`: read it first, it is the authority for this order), live together with the server side, which is now deployed (`opal-amgt-scoped-api` serves `ai_fill` for all 95 names). The candidate was cut from PROD `63c4f9e3`; PROD is now `7d5cb34d`, and the release build refuses a stale head, so you RE-CUT the same eleven files onto the
current PROD. YOU CUT THE BRANCH, WRITE THE RECEIPT AND REGISTER THE APPROVAL ROW; you do not push, merge forward or promote.

Your nested portal worktree is `C:/dev/wk-resapp-429/portal`, at portal PROD `7d5cb34d` on branch `wk-AMGT_RESAPP-429-portal`. Do this, in order:
1. `cd C:/dev/wk-resapp-429/portal && git switch -c cand/dell1/aifill-blocks-prod` (the feature branch, from PROD; the name carries the box `dell1`).
2. Take the eleven files EXACTLY as the approved candidate has them: verify the object with `git cat-file -t 85d5749f` (it must read `commit`), then
   `git checkout 85d5749f -- src/pages/SecurityAnalysis/SecurityAnalysis.tsx src/pages/SecurityAnalysis/types.ts src/pages/SecurityAnalysis/components/AiFillBlock.tsx src/pages/SecurityAnalysis/components/SecurityOverlay.tsx src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx src/pages/SecurityAnalysis/tabs/ThesisTab.tsx src/pages/SecurityAnalysis/__harness__/aiFill.harness.cjs src/pages/SecurityAnalysis/__harness__/aiFill.fixture.json src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs src/pages/SecurityAnalysis/__harness__/execText.harness.cjs`.
   Edit nothing by hand: the branch is blob-equal to the candidate on those eleven paths. (PROD moved from `63c4f9e3` to `7d5cb34d` by four OTHER files of this page directory, `HeaderCards.tsx`, `StatTile.tsx`, `model/WhatChangedPanel.tsx` and `tileMoneyAndReasons.harness.cjs`, none of which is among the eleven.)
3. Run AC2 (typecheck, lint and the harness suite against PROD `7d5cb34d` as the base): the suite must read no regression. If it does, STOP and file a BLOCKING row naming the harness.
4. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~429/FEATURE_RECEIPT.md` with exactly these sections: `## What the branch carries` (the branch name, its head commit, its base `7d5cb34d`, the eleven paths); `## Pages changed` (a table: page | route | class | gate; Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect); `## Shared files` (`- none`); `## Not carried` (AdvisorBookFeePanel, the /portfolios change, package.json and bun.lock, firmAccess.ts: each stated absent with the `git diff 7d5cb34d HEAD -- <path> | wc -l` count, 0); `## How to look` (the dev build: `cd portal && bun run dev:live --port 5174`, the page `/security-analysis`, names `AMD US`, `COST US` and `ASML NA`: the AI-fill blocks show on the Exec Management and Thesis tabs and in the header only where the research team's pack or the header holds nothing).
5. Commit the branch in the nested worktree (cwd `C:/dev/wk-resapp-429/portal`, the same `.tools/safe-commit.sh` from the OUTER checkout's `.tools` with the author line below, `-F` a message file written with the Write tool, `--` the eleven paths relative to the portal root; the portal commit identity may need the per-call env the previous workers used: report what you needed). Do not stage `portal` in the outer worktree. NEVER push.
6. Register the approval row: `python .tools/open-calls.py add --kind approval --project AMGT_RESAPP --subject "AMGT_RESAPP FWD-41: the AI-fill page blocks, re-cut from PROD 7d5cb34d (approved at call cf85)" --asked-by 2.0.0_SA_COO~R2 --box dell1 --branch cand/dell1/aifill-blocks-prod --class opal-internal --pages "Security Analysis" --purpose "Five machine-written text blocks on the Security Analysis page (management bio summary, recent management developments, and gap fills for the research team's management passage, the thesis pillars and the header description), each with its source class, citations as links and a Machine-written chip; the server side is deployed and serves ai_fill for 95 names" --how "cd portal && bun run dev:live --port 5174; /security-analysis, AMD US and COST US" --portal portal`. (`python .tools/open-calls.py add --help` is the authority on options; the tool reads the head and the commit count itself and REFUSES a branch carrying commits already on DEV: report its output verbatim.) The CTO has already approved this feature (call cf85) and closes the new row `approved`; you do not close it.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W429-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-429/portal`, branch `cand/dell1/aifill-blocks-prod` from PROD `7d5cb34d`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; no `bun install` (`node_modules` is a link to the main checkout's).
2. The branch's content is `git checkout 85d5749f -- <path>` of the approved candidate's bytes on the eleven paths; edit no product file by hand. The receipt, and the one registry row, are the only other things you write.
3. Never take `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `AdvisorBookFeePanel` or any file of another page.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/devices/state/dell1/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~429/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ar-5"><invocation>cd C:/dev/wk-resapp-429/portal &amp;&amp; for f in src/pages/SecurityAnalysis/SecurityAnalysis.tsx src/pages/SecurityAnalysis/types.ts src/pages/SecurityAnalysis/components/AiFillBlock.tsx src/pages/SecurityAnalysis/components/SecurityOverlay.tsx src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx src/pages/SecurityAnalysis/tabs/ThesisTab.tsx src/pages/SecurityAnalysis/__harness__/aiFill.harness.cjs src/pages/SecurityAnalysis/__harness__/aiFill.fixture.json src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs src/pages/SecurityAnalysis/__harness__/execText.harness.cjs; do a=$(git rev-parse HEAD:$f); b=$(git rev-parse 85d5749f:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done; echo "changed: $(git diff --name-only 7d5cb34d HEAD | wc -l)"; git branch --show-current</invocation><expect>eleven lines `EQUAL <path>` (one per path, none `DIFFERS`), then `changed: 11`, then the branch name `cand/dell1/aifill-blocks-prod`</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ar-5"><invocation>cd C:/dev/wk-resapp-429 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-resapp-429/portal" 7d5cb34d | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` with T equal to U plus one (the new harness); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ar-5"><invocation>cd C:/dev/wk-resapp-429/portal &amp;&amp; python "C:/dev/wk-resapp-429/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 7d5cb34d --head HEAD --receipt "C:/dev/wk-resapp-429/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~429/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (11 files: 11 page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~429 <0.9.0_WK_AMGT_RESAPP~429@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~429/AMGT_RESAPP.TO-AMGT-ar-5.the-ai-fill-page-feature-is-cut-from-the-prod-release-and-registered.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-429`.

Report once:
- the branch name, its head commit and base;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## Pages changed` and `## Not carried` sections, verbatim;
- the open-calls tool's output for the approval row (its row id), verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** THE FLOW is `portal/CONTRIBUTING-BOXES.md` (C-FEATURE / C-APPROVAL / C-MERGE-FORWARD / C-PROMOTE of NFRA_DEVPLN), as `AMGT-bk-6` ran it for `2.0.0_SA_COO~R1`: the branch is `cand/<box>/<slug>` cut from the last PROD release (`7d5cb34d` at the cut, `2.0.0_SA_COO~R1`'s header feature having been promoted), pushed under that name by the ISSUER, merged forward onto DEV by `.tools/portal-merge-forward.sh` once the row reads `approved`, and promoted by LIST (`.tools/portal-release-build.sh --features <list>`) by the portal release seat (`AMGT-ar-6`). The server side is DEPLOYED (`AMGT-ar-3`, step 4 read: all 95 names serve `ai_fill` equal to the stored documents), so the page may now go live, as the CTO ruled ("live together with the server side"). Class: Opal-internal (route `requireInternal`): no word from Andrew.

<status>pending</status>
<round>104</round>
<workstream>AIFILLLAND</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~429</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
