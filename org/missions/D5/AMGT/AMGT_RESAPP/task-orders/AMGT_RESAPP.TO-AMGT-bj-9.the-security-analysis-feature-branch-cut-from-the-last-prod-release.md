# AMGT_RESAPP task order -- `AMGT-bj-9` -- THE SECURITY ANALYSIS FEATURE BRANCH, CUT FROM THE LAST PROD RELEASE, WITH ITS RECEIPT (FWD-40 PROMOTE; A PORTAL BRANCH, NEVER DEV AND NEVER PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~410</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-9.the-security-analysis-feature-branch-cut-from-the-last-prod-release</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git and bun only.
comp-adversary: RUN at the cut -- `r103_feature_surface_check.py --selftest` reads `arms passed 7 of 7 ... YES`; at the base (head = PROD 15c9754975) it reads `R103 FEATURE SURFACE: NO (0 files)` and over DEV whole (origin/DEV c1d367231c) it reads `NO (196 files: 17 page, 0 shared named, 170 forbidden, 9 unnamed)`, so a whole-DEV promote can never pass.
EGRESS CLASS, declared: NONE beyond `git fetch origin` in the nested portal repository (read) and `bun install` from its lockfile.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-410` (branch `wk-AMGT_RESAPP-410`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-410`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bj-9` (round 103, decomposition s.112)

ADDENDUM 1 item 1 of the CTO's round-102 analysis (msg 5021), on PRD v0.44 FWD-40: the Security Analysis feature is promoted as ONE FEATURE cut from the last PROD release (portal PROD `15c9754975`), approved by `1.0.0_SA_CTO~DELL1` as Opal-internal (route `requireInternal`), with a receipt naming every page changed and its class (NFRA_DEVPLN C-FEATURE). It is NEVER the live DEV whole; it never carries `AdvisorBookFeePanel`, the `/portfolios` change, the dependency files (`package.json`, `bun.lock`) or `src/lib/firmAccess.ts`. YOU CUT THE BRANCH AND WRITE THE RECEIPT; the approval and the promote are not yours and not this order's.

Your nested portal worktree is `C:/dev/wk-resapp-410/portal`, at PROD `15c9754975` on branch `wk-AMGT_RESAPP-410-portal`. Do this, in order:
1. `cd C:/dev/wk-resapp-410/portal && git switch -c feature/amgt-security-analysis-v1` (the feature branch, from PROD) and `git fetch origin DEV` (read-only).
2. Take the page as DEV has it: `git checkout origin/DEV -- src/pages/SecurityAnalysis`. DEV's page state carries the Model tab's team-sheet rendering that replaced the raw data codes (the e7f2 breakdown's 'not ready' item: `CRPS-av-2` to `CRPS-ay-2`); the harness suite below is what shows it.
3. `bun install --frozen-lockfile` (bun on PATH; never a baked path), then `bun run typecheck`. Every error that names a file OUTSIDE `src/pages/SecurityAnalysis/` is a shared file the page needs from DEV: `git checkout origin/DEV -- <that file>`, then typecheck again, until it exits 0. For each such file record its OTHER READERS: `git grep -l "<its import path>" -- src` outside the page directory (print the list; 'none' is a valid answer). If typecheck can only pass by taking `package.json`, `bun.lock`, `src/lib/firmAccess.ts` or a file of another page, STOP: file a BLOCKING row naming the file and the error, and do not take it.
4. Run AC2 (`r103_feature_green.sh`): typecheck, lint, and every `__harness__/*.harness.{cjs,mjs}` as `node <file>`. Fix nothing by editing product code: a failing harness or lint rule is a BLOCKING row naming it (the DEV state may carry a failure PROD never had; the issuer rules).
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~410/FEATURE_RECEIPT.md` with exactly these sections: `## What the branch carries` (the branch's commit hash, its base `15c9754975`, the count of page files and shared files); `## Pages changed` (a table, one row per page changed: page | route | class | gate; Security Analysis | /security-analysis | Opal-internal | internal; any other page changed would be a defect); `## Shared files` (one line per shared file, the form `- `<path>` -- other readers: <comma-separated paths, or none>`; a client-facing reader, `ModelPortfolios` or `AdvisorIntelligence`, is written as such); `## Not carried` (AdvisorBookFeePanel, the /portfolios change, package.json and bun.lock, firmAccess.ts: each stated absent, with the diff line count that proves it).
6. Commit the branch in the nested worktree (cwd `C:/dev/wk-resapp-410/portal`): `.tools/safe-commit.sh` from the OUTER checkout's `.tools` with the author line below, `-F` a message file written with the Write tool, `--` the page directory and each shared file, paths relative to the portal root. Do not stage `portal` in the outer worktree. NEVER push.

The branch is judged on the surface (AC1), the suite (AC2), the receipt (AC1 reads it) and one walk (AC3, the CVO's): a build of the branch, `bun run dev --port 5174`, opened on three names (`ASML_NA_Equity`, `VLO_US_Equity`, `UBSG_SW_Equity`), each tab visited, screenshots saved under your deliverables folder.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W410-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-410/portal`, branch `feature/amgt-security-analysis-v1` from PROD `15c9754975`; never push; never touch `DEV` or `PROD`; never `git merge` DEV.
2. Edit NO product file by hand: the branch's content is `git checkout origin/DEV -- <path>` of DEV's own bytes (the receipt states each path). The receipt and screenshots are the only files you write.
3. Never take `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `AdvisorBookFeePanel` or any file of another page. No new dependency.
4. The dev server uses port 5174 ONLY and is stopped when you are done.

## 3. SURFACES

<paths>
portal/src/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~410/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1500)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bj-9"><invocation>cd C:/dev/wk-resapp-410/portal &amp;&amp; python "C:/dev/wk-resapp-410/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 15c9754975 --head HEAD --receipt "C:/dev/wk-resapp-410/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~410/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page or shared (named in the receipt), none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (N files: P page, S shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-9"><invocation>cd C:/dev/wk-resapp-410 &amp;&amp; timeout 1400 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green.sh" "C:/dev/wk-resapp-410/portal" | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness H of H)`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bj-9" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~410 <0.9.0_WK_AMGT_RESAPP~410@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~410/AMGT_RESAPP.TO-AMGT-bj-9.the-security-analysis-feature-branch-cut-from-the-last-prod-release.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash of the branch and its base;
- AC1's and AC2's output lines;
- the receipt's `## Pages changed` and `## Shared files` sections, verbatim;
- the screenshots' paths (three names, each tab) and, per name, one line saying what you saw (a raw code, a placeholder, an empty section with no reason: name it);
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** THE SPEC: CTO ADDENDUM 1 item 1 and PRD v0.44 FWD-40; the grade of the promote is the CTO's approval as Opal-internal and the portal release seat's act under the push law (staff-only page: no word from Andrew). AC3 is a JUDGMENT criterion (the walk, screenshots read): graded by the CVO, never self-graded. The cut base is PROD `15c9754975` (read at the cut: `git ls-remote`/`origin/PROD` in the nested repository); DEV was `c1d367231c`, 206 commits ahead, 40 of them on this page, 17 page files differing. If a harness fails on DEV's state the row carries the harness name and the failing line; the issuer rules. The portal worktree is provisioned with `--portal-ref 15c9754975`. `AMGT-bj-11` (the ten-name walk on `bun run dev:live`) is staged behind the promote.

<status>pending</status>
<round>103</round>
<workstream>V1</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~410</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
