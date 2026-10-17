# AMGT_RESAPP task order -- `AMGT-bt-2` -- THE MODEL TAB'S TOOLTIP IS NEVER COVERED BY THE ALL FIGURES LIST AND THE ALL FIGURES GRID IS NEVER CUT SIDEWAYS WITHOUT A VISIBLE SCROLLBAR: TWO LAYOUT REPAIRS, ONE CELL (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bt-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~501</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bt-2.model-tooltip-and-grid-clipping</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the new harness file does not exist, so it FAILS (exit 1); AC2 run in a provisioned worktree cut at `856fb37b` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 30 of 33 pass, base <Q> of <U>, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new check against the unedited head before any product edit (step 2 or 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-501` (branch `wk-AMGT_RESAPP-501`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-501/portal` is cut at PROD `856fb37b`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-501`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bt-2` (round 113, decomposition s.122)

Two layout classes of the walker (the UI walk of `/security-analysis`, a real browser) recur on the Model tab and are display defects. Both repairs are display only: no served value, figure, sentence or order changes. Your harness is a STRUCTURAL proxy (a static render has no layout engine); a real-browser walk by the issuer grades the real effect after the merge, so say plainly in your receipt what your checks can and cannot prove.

**Repair A: `occluded-popover`.** Finding: on RIO LN's Model tab with `Earlier version` set to October 16th, 2026, `3 of 9 sample points of an open tooltip are covered by another element`: the tooltip is `table > tbody > tr > td > div[role=tooltip]` and the covering element is `div > div > details > ul > li` (text `Tgt: The research team keeps no workbook for this company; t...`). The tooltip is `FigureTooltip` in `src/pages/SecurityAnalysis/components/StatTile.tsx` (read lines ~140-170 and ~205-220: an absolutely positioned bubble, `z-10`, `hidden group-hover:block`, placed `top-full` or `bottom-full`, rendered inline inside the table cell, not through a portal). The covering list lives in the `All figures` fold of `src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (around line 804, `<summary ...>All figures</summary>`). Find WHY the later list paints over the bubble: read the class lists of every ancestor of the bubble up to the Model panel and of the `details`/`ul`/`li`, looking for a stacking context on the bubble's side (an ancestor with `relative` plus a `z-` class, `isolate`, `transform`, `overflow-*` with `relative`) that ranks below a positioned/z-indexed ancestor of the list. Fix it with the smallest class change in `StatTile.tsx` and/or `ModelTab.tsx` (for example a higher z-index from the page's z-index tokens in `@/lib/designTokens` when one fits, or removing the stacking context that traps the bubble), so the bubble ranks above the list. Do NOT edit `src/components/Tooltip.tsx` or any other shared file.

**Repair B: `layout:clipped`.** Finding: on RIO LN's and ICT PM's Model tab `151` and `149` text elements are `cut off sideways by their container` in the `All figures` grid (a table of one column of labels and one column per fiscal year, wider than the panel: samples were `th`/`td` cells, widths 55 px and 228 px past the container edge). The walker's check (`.claude/skills/ui-walk/walk.mjs` lines ~237-256, read it) does NOT count an element whose nearest clipping ancestor shows a horizontal scrollbar (`offsetHeight - clientHeight` greater than the borders: a visible scrollbar) and does not count an ellipsis; it counts text cut by an ancestor whose `overflow-x` is not `visible` and which shows no scrollbar. Make the grid's scroll container show its horizontal scrollbar (for example `overflow-x-auto` with no class or style that hides the scrollbar: look for `scrollbar-none`, `scrollbar-hide`, `[&::-webkit-scrollbar]:hidden`, `overflow-x-hidden`, `overflow-hidden` on the container and its ancestors up to the panel) AND let the label column's long text wrap (`whitespace-normal`, `break-words`) instead of overflowing, so no label is drawn past its cell. The grid's data, columns and order do not change.

**The grade is on structure you can read in a static render.** The new harness `src/pages/SecurityAnalysis/__harness__/modelLayout.harness.cjs` (YOURS: create it; MODEL the static render of `ModelTab` on an existing harness that renders it with the hooks stubbed, such as `modelPattern.harness.cjs` or `withheldReasons.harness.cjs`, and the tooltip render on the harness that already renders `StatTile`, `shell.harness.cjs`) reads class lists out of the static markup and checks, each named in the output: M1 the tooltip bubble's own stacking: its classes carry a z-index at or above the one you chose (named in the output) and it is `absolute`; M2 no ancestor of the bubble up to the Model panel creates a stacking context (`relative` with a `z-` class, `isolate`, a transform) that ranks below the `All figures` fold's own positioned ancestors; list the ancestor chain with the classes you read; M3 the `All figures` grid's scroll container has `overflow-x-auto` or `overflow-x-scroll` and none of the scrollbar-hiding classes or `overflow-hidden`/`overflow-x-hidden` on it or on the ancestors up to the panel; M4 the label column's cells wrap (`whitespace-normal` or `break-words`) and carry no `truncate`, `whitespace-nowrap` or `text-ellipsis`; M5 CONTROL: the Model tab's served text (every figure, label and sentence of the RIO LN fixture render) is byte-identical to the render at the base head except for class attributes (compare the markup with every `class="..."` removed: record the base text digest BEFORE the edit); M6 the existing harnesses `modelPattern.harness.cjs` and `shell.harness.cjs` (whichever exist) still pass when spawned by yours, or fail only on a check that pins an old class you changed (name it and update ONLY that expectation). Print `MODEL LAYOUT HARNESS: YES (<n> of <n> checks)` or `NO` (at least 6 checks, M1 to M6 named). If a check cannot be built because the markup does not expose the class you need, name it `not run` with the reason; never print it as passed.

**Do this in order.** (1) `cd C:/dev/wk-resapp-501/portal && git switch -c cand/dell1/amgt-sa-model-layout-repairs` (your nested worktree is cut at PROD `856fb37b`; confirm `git log -1 --format=%h` reads `856fb37b` before and after). (2) Read the code and the walker check; write down the stacking chain and the container chain in your receipt. (3) Create the harness FIRST (record the M5 base digest) and run it ONCE on the unedited head: it must print `NO` with M1 or M2 failing and M3 or M4 failing, naming which; record that run honestly. (4) Make the edits. (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~501/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `856fb37b`, every path changed since `856fb37b`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 856fb37b HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-model-layout-repairs --purpose "AMGT_RESAPP bt-2: the Model tab tooltip is never covered by the All figures list and the grid is never cut sideways without a visible scrollbar" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, RIO LN, Model tab, the Earlier version select at October 16th, hover a figure; the All figures grid" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W501-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-501/portal`, new branch `cand/dell1/amgt-sa-model-layout-repairs` cut from PROD `856fb37b`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `src/components/Tooltip.tsx` or any other shared file, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~501/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bt-2"><invocation>cd C:/dev/wk-resapp-501/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/modelLayout.harness.cjs; echo "exit=$?"</invocation><expect>the line `MODEL LAYOUT HARNESS: YES (<n> of <n> checks)` with n at least 6, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bt-2"><invocation>cd C:/dev/wk-resapp-501 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-501/portal" 856fb37b | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 31 and T at least 34, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bt-2"><invocation>cd C:/dev/wk-resapp-501/portal &amp;&amp; python "C:/dev/wk-resapp-501/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 856fb37b --head HEAD --receipt "C:/dev/wk-resapp-501/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~501/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~501 <0.9.0_WK_AMGT_RESAPP~501@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~501/AMGT_RESAPP.TO-AMGT-bt-2.model-tooltip-and-grid-clipping.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-501` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-501`.

Report once:
- the branch name, its head commit and the base `856fb37b`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-112 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round112.R1.md`, msg 7733) item list. One cell, one candidate branch cut from PROD `856fb37b`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-113 cells. AC2's totals were measured in a provisioned worktree cut at `856fb37b` at the cut (30 of 33, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs). THE REAL GRADE IS THE ISSUER'S WALK: the worker's harness is a structural proxy (a static render has no layout engine). At close the issuer walks a local build of the merged candidate on RIO LN (the Oct 16 select state) and reads the walker's `occluded-popover` and `layout:clipped` counts on the Model grid; a non-zero reading recuts the cell in round 114. Items 2 and 3 of the CTO's list are batched into one cell (style repairs in one cell), on the two files StatTile.tsx and ModelTab.tsx.

<status>complete -- NOT MET on the real-browser grade, 2026-10-17 by the issuer (2.0.0_SA_COO~R1): worker ~501 at 18e8e24b6d (merged); proof VALID rc=0 and AC1 to AC3 PASS (MODEL LAYOUT HARNESS YES 6 of 6: StatTile.tsx FigureTooltip z-10 to z-50, ModelTab.tsx label cell wrap; at the unedited head NO 3 of 6, M1 and M4 failing), but the issuer's real-browser walk of a local build of the candidate head 847c474b read `occluded-popover` 3 of 9 and `layout:clipped` 151 and 149 UNCHANGED (findings under C:/dev/ui-walk-evidence/r113-bt2/), as the worker's rows W501-S1 and W501-S2 predicted (no stacking trap; the grid's overflow-x-auto scroller clips the bubble and its scroll is not clipped text). The candidate is NOT registered and NOT promoted. Item 3 ruled by the CTO (msg 7741): no cell, the walker's probe is corrected, the scroll affordance is a round-114 candidate. Item 2 recut as AMGT-bt-6 (the last rows' bubbles open upward)</status>
<round>113</round>
<slot>0.9.0_WK_AMGT_RESAPP~501</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
