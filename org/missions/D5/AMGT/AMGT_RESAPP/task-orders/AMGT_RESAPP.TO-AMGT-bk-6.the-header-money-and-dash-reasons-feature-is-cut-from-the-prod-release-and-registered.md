# AMGT_RESAPP task order -- `AMGT-bk-6` -- THE HEADER MONEY-AND-DASH-REASONS FEATURE IS CUT FROM THE PROD RELEASE AS `cand/dell1/amgt-sa-header-money-and-dash-reasons`, WITH ITS RECEIPT AND ITS APPROVAL ROW (A PORTAL BRANCH; NEVER DEV, NEVER PROD, NEVER PUSHED BY THE WORKER)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bk-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~417</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bk-6.the-header-money-and-dash-reasons-feature-is-cut-from-the-prod-release-and-registered</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository and one registry row; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, bun and the open-calls tool only.
comp-adversary: RUN at the cut -- `r103_feature_surface_check.py --selftest` reads YES (7 arms) and, run with `--base 10e7664d --head 3dcbb6ef` over the DEV-BASED candidate reads `NO (14 files: 4 page, 0 shared named, 10 forbidden, 0 unnamed)` (the candidate carries the DEV commits that PROD lacks: ten files of the Ticket Center), which is WHY it is re-cut onto PROD; the same check over the re-cut four-file branch is AC3 and must read YES (the control arm for a branch with only its own commits). The old `YES` claim in an earlier draft of this line was not measured and is withdrawn. EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-417` (branch `wk-AMGT_RESAPP-417`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-417`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bk-6` (round 104, decomposition s.113)

CTO msg 5281: the portal candidate `3dcbb6ef` (AMGT-bk-3: USD prints `$`, every dash tile shows its reason) is APPROVED as Opal-internal and lands as a FEATURE CUT FROM PROD `10e7664d` through the portal's contributing-boxes flow (`portal/CONTRIBUTING-BOXES.md`, read it first: it is the authority for this order), and the same commits reach DEV by `.tools/portal-merge-forward.sh`, so the trunks do not diverge. YOU CUT THE BRANCH, WRITE THE RECEIPT AND REGISTER THE APPROVAL ROW; you do not push, merge forward or promote.

Your nested portal worktree is `C:/dev/wk-resapp-417/portal`, at portal PROD `10e7664d` on branch `wk-AMGT_RESAPP-417-portal`. Do this, in order:
1. `cd C:/dev/wk-resapp-417/portal && git switch -c cand/dell1/amgt-sa-header-money-and-dash-reasons` (the feature branch, from PROD; the name carries the box `dell1`).
2. Take the four files EXACTLY as the approved candidate has them: `git checkout 3dcbb6ef -- src/pages/SecurityAnalysis/components/HeaderCards.tsx src/pages/SecurityAnalysis/components/StatTile.tsx src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx src/pages/SecurityAnalysis/__harness__/tileMoneyAndReasons.harness.cjs` (the object `3dcbb6ef` is in the shared portal repository; verify with `git cat-file -t 3dcbb6ef` first). Edit nothing by hand: the branch is blob-equal to the candidate on those four paths.
3. Run AC2 (typecheck, lint and the harness suite against PROD `10e7664d` as the base): the suite must read no regression. If it does, STOP and file a BLOCKING row naming the harness.
4. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~417/FEATURE_RECEIPT.md` with exactly these sections: `## What the branch carries` (the branch name, its head commit, its base `10e7664d`, the four paths); `## Pages changed` (a table: page | route | class | gate; Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect); `## Shared files` (`- none`); `## Not carried` (AdvisorBookFeePanel, the /portfolios change, package.json and bun.lock, firmAccess.ts: each stated absent with the `git diff 10e7664d HEAD -- <path> | wc -l` count, 0); `## How to look` (the dev build: `cd portal && bun run dev:live --port 5174`, the page `/security-analysis`, names `TSM US`, `HSBA LN`).
5. Commit the branch in the nested worktree (cwd `C:/dev/wk-resapp-417/portal`, the same `.tools/safe-commit.sh` from the OUTER checkout's `.tools` with the author line below, `-F` a message file written with the Write tool, `--` the four paths relative to the portal root; the portal commit identity may need the per-call env the previous workers used: report what you needed). Do not stage `portal` in the outer worktree. NEVER push.
6. Register the approval row: `python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-header-money-and-dash-reasons --purpose "AMGT_RESAPP bk-3: the Security Analysis header prints USD as $ and every dash tile shows its reason" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, TSM US and HSBA LN" --portal portal`. (`python .tools/open-calls.py add --help` is the authority on options; the tool reads the head and the commit count itself and REFUSES a branch carrying commits already on DEV: report its output verbatim.) The CTO has already approved this feature (msg 5281) and closes the row `approved`; you do not close it.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-417/portal`, branch `cand/dell1/amgt-sa-header-money-and-dash-reasons` from PROD `10e7664d`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; no `bun install` (`node_modules` is a link to the main checkout's).
2. The branch's content is `git checkout 3dcbb6ef -- <path>` of the approved candidate's bytes on the four paths; edit no product file by hand. The receipt, and the one registry row, are the only other things you write.
3. Never take `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `AdvisorBookFeePanel` or any file of another page.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/devices/state/dell1/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~417/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bk-6"><invocation>cd C:/dev/wk-resapp-417/portal &amp;&amp; for f in src/pages/SecurityAnalysis/components/HeaderCards.tsx src/pages/SecurityAnalysis/components/StatTile.tsx src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx src/pages/SecurityAnalysis/__harness__/tileMoneyAndReasons.harness.cjs; do a=$(git rev-parse HEAD:$f); b=$(git rev-parse 3dcbb6ef:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done; echo "changed: $(git diff --name-only 10e7664d HEAD | wc -l)"; git branch --show-current</invocation><expect>four lines `EQUAL <path>` (one per path, none `DIFFERS`), then `changed: 4`, then the branch name `cand/dell1/amgt-sa-header-money-and-dash-reasons`</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bk-6"><invocation>cd C:/dev/wk-resapp-417 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-resapp-417/portal" 10e7664d | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` with T equal to U plus one (the new harness); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bk-6"><invocation>cd C:/dev/wk-resapp-417/portal &amp;&amp; python "C:/dev/wk-resapp-417/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 10e7664d --head HEAD --receipt "C:/dev/wk-resapp-417/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~417/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (4 files: 4 page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~417 <0.9.0_WK_AMGT_RESAPP~417@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~417/AMGT_RESAPP.TO-AMGT-bk-6.the-header-money-and-dash-reasons-feature-is-cut-from-the-prod-release-and-registered.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-417`.

Report once:
- the branch name, its head commit and base;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## Pages changed` and `## Not carried` sections, verbatim;
- the open-calls tool's output for the approval row (its row id), verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** THE FLOW is `portal/CONTRIBUTING-BOXES.md` (C-FEATURE / C-APPROVAL / C-MERGE-FORWARD / C-PROMOTE of NFRA_DEVPLN): the branch is `cand/<box>/<slug>`, cut from the last PROD release (PROD `10e7664d` at the cut), pushed under that name, registered as an approval row, merged forward onto DEV by `.tools/portal-merge-forward.sh` once the row reads `approved`, and promoted by LIST (`.tools/portal-release-build.sh --features <list>`) by the portal release seat. The ISSUER pushes the branch and asks the box manager for the merge-forward; the promote is the portal release seat's. Saturday's walk (bk-5) reads the page after the promote. The class is Opal-internal (route `requireInternal`): no word from Andrew.

<status>complete</status>
<round>104</round>
<workstream>LAND</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~417</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
