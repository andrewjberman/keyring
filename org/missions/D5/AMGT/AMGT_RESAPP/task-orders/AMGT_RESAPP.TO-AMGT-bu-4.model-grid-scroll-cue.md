# AMGT_RESAPP task order -- `AMGT-bu-4` -- THE ALL FIGURES GRID SHOWS THE READER THAT IT SCROLLS SIDEWAYS: A VISIBLE CUE ABOVE THE GRID AND A VISIBLE SCROLLBAR THUMB (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bu-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~507</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bu-4.model-grid-scroll-cue</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the new harness file does not exist, so it FAILS (exit 1); AC2 run in a provisioned worktree cut at `d1bed0fb` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 32 of 35 pass, base <Q> of <U>, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new check against the unedited head before any product edit (step 2 or 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-507` (branch `wk-AMGT_RESAPP-507`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-507/portal` is cut at PROD `d1bed0fb`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-507`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bu-4` (round 114, decomposition s.123)

The Model tab's `All figures` fold holds a wide grid (one label column and one column per fiscal year, 1494 px of table in a 1266 px panel on RIO LN). The grid's scroller is `div.overflow-x-auto`; the portal's global CSS (`src/index.css`, section `SCROLLBAR STYLING`) paints every scrollbar thumb TRANSPARENT until the pointer hovers over the scrolled element, and the scroller is about 9,300 px tall, so its horizontal scrollbar sits at the bottom of the grid, far below the first screen: a reader has no sign that 228 px of year columns lie to the right. The CTO ruled (msg 7741, round-113 analysis item 3) that the horizontal scroll is by design and that the DISCOVERABILITY gap is a round-114 cell: "a scroll affordance the reader can see, either a bounded-height scroller or a visible scroll cue, graded on a built page in a real browser". **The mechanism chosen by the issuer is a visible cue, not a bounded-height scroller** (a bounded scroller would clip the figure tooltips at its edge, which round 113's `bt-6` just repaired).

**The change (display only; no served value, figure or sentence changes).** In `src/pages/SecurityAnalysis/tabs/ModelTab.tsx` ONLY, in the `All figures` fold (around line 804, `<summary ...>All figures</summary>`; read the markup of the fold and of the grid scroller `div.overflow-x-auto`): (1) put ONE line of words directly above the grid inside the fold, `<p data-grid-scroll-cue="">Scroll sideways to see every year.</p>` styled as quiet navy secondary text like the page's other small captions (read how a nearby caption is styled; no new colour, no `text-white`; the page's colour law is in `portal/CLAUDE.md`), visible whenever the fold is open; (2) give the grid's scroller a VISIBLE horizontal scrollbar thumb at all times, with Tailwind arbitrary variants on that one element (a thumb colour from the page's tokens, for example `[&::-webkit-scrollbar-thumb]:bg-[hsl(var(--palette-navy)/0.35)]`, and `[scrollbar-width:thin]` with a `[scrollbar-color:...]` for Firefox), leaving the scroller's `overflow-x-auto` and its other classes as they are. Do not edit `src/index.css`.

**The grade is on the RENDERED markup, and the real grade is the issuer's screenshot read.** Your harness is a STRUCTURAL check (a static render has no layout engine or pixels); the issuer reads a real-browser screenshot of a built page after the merge, so say plainly in your receipt what your checks can and cannot prove. The new harness `src/pages/SecurityAnalysis/__harness__/gridScrollCue.harness.cjs` (YOURS: create it; MODEL the static render of `ModelTab` on `modelTooltipRows.harness.cjs`, which renders it with the hooks stubbed on the RIO LN fixture) checks, each named in the output: S1 the `All figures` fold contains exactly ONE `data-grid-scroll-cue` element whose text is exactly `Scroll sideways to see every year.` and it comes BEFORE the grid's `<table>` in document order inside the fold; S2 the grid scroller keeps `overflow-x-auto` and carries a scrollbar-thumb class that is NOT transparent (`[&::-webkit-scrollbar-thumb]:bg-...` with a non-`transparent` value) and no scrollbar-hiding class (`scrollbar-none`, `overflow-x-hidden`, `overflow-hidden`); S3 CONTROL: the Model tab's served text of the RIO LN fixture render is byte-identical to the base head's EXCEPT the one cue sentence (compare the text with every `class="..."` removed and the cue element removed: record the base text digest BEFORE the edit); S4 CONTROL: `modelTooltipRows.harness.cjs` still prints `YES (9 of 9 checks)` when spawned by yours (the round-113 tooltip placement is untouched); S5 the cue is inside the fold (a descendant of the `details`), so a closed fold shows no cue. Print `GRID SCROLL CUE HARNESS: YES (<n> of <n> checks)` or `NO` (at least 5 checks, S1 to S5 named). A recorded text file is compared after normalising `\r\n` to `\n` on both sides (round 112 row S58).

**Do this in order.** (1) `cd C:/dev/wk-resapp-507/portal && git switch -c cand/dell1/amgt-sa-model-grid-scroll-cue` (your nested worktree is cut at PROD `d1bed0fb`; confirm `git log -1 --format=%h` reads `d1bed0fb` before and after). (2) Read the fold's markup and a nearby caption's classes. (3) Create the harness FIRST (record the S3 base digest) and run it ONCE on the unedited head: it must print `NO` with S1 and S2 failing and S3, S4, S5 as they read (S5 fails too if the cue is absent: say which); record that run. (4) Make the edit. (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~507/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `d1bed0fb`, every path changed since `d1bed0fb`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff d1bed0fb HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-model-grid-scroll-cue --purpose "AMGT_RESAPP bu-4: the All figures grid shows the reader that it scrolls sideways" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, RIO LN, Model tab, open All figures" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W507-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-507/portal`, new branch `cand/dell1/amgt-sa-model-grid-scroll-cue` cut from PROD `d1bed0fb`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `src/components/Tooltip.tsx` or any other shared file, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~507/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bu-4"><invocation>cd C:/dev/wk-resapp-507/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/gridScrollCue.harness.cjs; echo "exit=$?"</invocation><expect>the line `GRID SCROLL CUE HARNESS: YES (<n> of <n> checks)` with n at least 5, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bu-4"><invocation>cd C:/dev/wk-resapp-507 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-507/portal" d1bed0fb | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 33 and T at least 36, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bu-4"><invocation>cd C:/dev/wk-resapp-507/portal &amp;&amp; python "C:/dev/wk-resapp-507/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base d1bed0fb --head HEAD --receipt "C:/dev/wk-resapp-507/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~507/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~507 <0.9.0_WK_AMGT_RESAPP~507@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~507/AMGT_RESAPP.TO-AMGT-bu-4.model-grid-scroll-cue.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-507` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-507`.

Report once:
- the branch name, its head commit and the base `d1bed0fb`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-113 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round113.R1.md`, msg 7763) item list. One cell, one candidate branch cut from PROD `d1bed0fb`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-113 cells. AC2's totals were measured in a provisioned worktree cut at `d1bed0fb` at the cut (32 of 35, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs). The CTO's round-113 item 3 (the scroll affordance). THE REAL GRADE IS THE ISSUER'S SCREENSHOT READ of a built page; mechanism chosen: a visible cue plus a visible thumb, not a bounded scroller (it would clip tooltips). The CTO's item 4 (W503-S1, the short-grid tooltip) is NOT cut: the issuer counted value-bearing figure mnemonics over the 95 resolved names (smallest 36; RIO LN counts 76 and renders 60 rows), so by that ratio no live name is under about 20 rows (inferred; the grid row count per name was not measured). Decomposition s.123 decision (b).

<status>pending</status>
<round>114</round>
<slot>0.9.0_WK_AMGT_RESAPP~507</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
