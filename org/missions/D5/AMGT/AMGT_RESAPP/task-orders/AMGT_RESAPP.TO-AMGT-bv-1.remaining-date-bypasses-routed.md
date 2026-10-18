# AMGT_RESAPP task order -- `AMGT-bv-1` -- THE FOUR REMAINING DATE BYPASSES IN MODELTAB.TSX AND PEERSTAB.TSX PRINT IN THE HOUSE LONG FORM, AND THE CENSUS RE-RUNS TO ZERO BYPASSES (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bv-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~508</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bv-1.remaining-date-bypasses-routed</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the new harness file does not exist, so it FAILS (exit 1); AC2 run in a provisioned worktree cut at `26d998f7` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 34 of 37 pass, base <Q> of <U>, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new check against the unedited head before any product edit (step 2 or 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-508` (branch `wk-AMGT_RESAPP-508`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-508/portal` is cut at PROD `26d998f7`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-508`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bv-1` (round 115, decomposition s.124)

Round 114's `AMGT-bu-2` censused every date site under `src/pages/SecurityAnalysis/` (the committed fixture `src/pages/SecurityAnalysis/__harness__/dateSites.fixture.json`, 102 sites, 30 of them bypassing the house long-date helper) and fixed 26. FOUR it could not reach, because `ModelTab.tsx` and `PeersTab.tsx` belonged to other cells of that round: they are the fixture's entries `C-18`, `C-20`, `C-33` and `C-34`, each `bypass: true`, `disposition: deferred_to`; rows `AMGT_RESAPP-D1-W505-S1` and `W505-S2`. The CTO's round-114 analysis item 1: route the remaining bypassing sites through the house helper and re-run the census to ZERO bypasses. The four: (1) `tabs/ModelTab.tsx` around line 196-199, `priceBasisLine`: prints the served `PX_LAST` `period_end_date` or `fiscal_period_end` raw in `at the close of <date>` (entry `C-18`); (2) `tabs/ModelTab.tsx` around line 972: the Model tab's gap-reason notes print `{reason}` raw in a list item, and served reasons embed ISO days (`at universe vintage 2026-10-02`) (entry `C-20`); (3) `tabs/PeersTab.tsx` around line 407: the absent-peers reason `{data.reason}` printed raw (entry `C-33`); (4) `tabs/PeersTab.tsx` around line 235: a column reason shown in a tooltip goes through `guardedReason`, which keeps a date as served (entry `C-34`).

**The change (display only).** Read `src/pages/SecurityAnalysis/dateWords.ts` first: `longDate` (a bare day), `longStamp`, and `daysInWords` (replaces every ISO day inside a sentence; read how round 114's `bu-2` used it at 26 reason sites: for example `tabs/ExecManagementTab.tsx` and `components/HeaderCards.tsx`). Route site (1) through `longDate` (a bare day) and sites (2) to (4) through `daysInWords` (served prose), in the same way. A value that is not a date prints as it came. No served value, `data-` attribute, ordering or sentence changes; do not reword any existing sentence. In `PeersTab.tsx` ONLY these two sites change; in `ModelTab.tsx` ONLY the two. `dateWords.ts` is in your grant for a helper tweak only if a site genuinely needs one: say so in the receipt if you touch it (expected: not touched).

**Update the census fixture and re-run it to zero.** In `dateSites.fixture.json` the four entries become `fixed_here` (set `disposition` and drop `deferred_to`; keep `bypass: true` as the record of what the site was, or set it as the file's own schema directs: read its header `note`), and the file's printed `denominator` still equals its entry count. **Re-run the census to ZERO bypasses:** re-read each of the four sites at the new head and record in the receipt's `## Date census re-run` the file:line now, what it reads and the helper it passes through; then re-search the two files for `_date`, `as_of`, `vintage`, `period_end`, `slice(0, 10)`, `toISOString`, `toLocaleDateString`, `Date(` and `reason` printed raw, reading each hit in context, and print the NEW denominator (hits read, sites) and the count of sites still bypassing (the expectation is 0 in these two files; any other bypass you find is a surprise row and a census entry `deferred_to` with a named reason, never silently left).

**The grade is on the RENDERED text.** The new harness `src/pages/SecurityAnalysis/__harness__/dateBypass.harness.cjs` (YOURS: create it; MODEL the static render of `ModelTab` on `gridScrollCue.harness.cjs` or `modelTooltipRows.harness.cjs` and the static render of `PeersTab` on `priceCurrencyRule.harness.cjs`, both of which render with the hooks stubbed on committed fixtures) checks, each named: D1 a Model tab render whose price figure carries `period_end_date` `2026-09-30` reads `at the close of September 30th, 2026` and no ISO day on that line; D2 a Model tab render whose served gap reasons embed `2026-10-02` prints `October 2nd, 2026` in the list item and no ISO day; D3 a Peers tab render with an absent-peers `reason` embedding an ISO day prints the long form; D4 a Peers tab column reason (the tooltip title) embedding an ISO day prints the long form; D5 the census: `dateSites.fixture.json` has no entry with `bypass: true` whose `disposition` is not `fixed_here` or `deferred_to` a named cell, its `denominator` equals its entry count, and `C-18`, `C-20`, `C-33` and `C-34` read `fixed_here`; D6 CONTROL: a render with NO date in the served text (the committed RIO LN fixture, as the other harnesses use) reads the same visible text as the base head for both tabs, once every long-form date is mapped back to ISO by a hand-written inverse: record each tab's base visible-text sha256 BEFORE the product edit; D7 the older date harnesses still pass when spawned by yours (`dateRule.harness.cjs` YES 7 of 7, `gridScrollCue.harness.cjs` YES 5 of 5, `modelTooltipRows.harness.cjs` YES 9 of 9, `priceCurrencyRule.harness.cjs` YES 8 of 8). Expected strings are written by hand, never by importing the helper. Print `DATE BYPASS HARNESS: YES (<n> of <n> checks)` or `NO` (at least 7, D1 to D7 named). A recorded text file is compared after normalising `\r\n` to `\n` on both sides (round 112 row S58).

**If an intended text change moves a sibling control.** `modelTooltipRows.harness.cjs` check B5 and `gridScrollCue.harness.cjs` check S3 compare the RIO LN Model tab's served text to a recorded digest. If your change moves either (the RIO LN fixture's price basis line may carry an ISO day), re-record ONLY that digest constant and its one-line comment (name this cell as the reason), after proving the new text equals the old text with the ISO days replaced by their long forms (print old and new digest); the grant covers the `__harness__/` folder. Round 114's `AMGT-bu-4` hit exactly this.

**Do this in order.** (1) `cd C:/dev/wk-resapp-508/portal && git switch -c cand/dell1/amgt-sa-remaining-date-bypasses` (your nested worktree is cut at PROD `26d998f7`; confirm `git log -1 --format=%h` reads `26d998f7` before and after). (2) Read the four sites and `dateWords.ts`. (3) Create the harness FIRST (record the D6 base digests) and run it ONCE on the unedited head: it must print `NO` with D1 to D5 failing and D6 and D7 passing; record that run. (4) Make the edits and update the fixture. (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~508/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `26d998f7`, every path changed since `26d998f7`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 26d998f7 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-remaining-date-bypasses --purpose "AMGT_RESAPP bv-1: the four remaining date bypasses in the Model and Peers tabs print in the house long form" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, ICT PM and RIO LN, Model tab (the price basis line, the gap notes) and Peers tab (an absent-peers reason, a column tooltip)" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W508-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-508/portal`, new branch `cand/dell1/amgt-sa-remaining-date-bypasses` cut from PROD `26d998f7`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `src/components/Tooltip.tsx` or any other shared file, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/dateWords.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~508/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bv-1"><invocation>cd C:/dev/wk-resapp-508/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/dateBypass.harness.cjs; echo "exit=$?"</invocation><expect>the line `DATE BYPASS HARNESS: YES (<n> of <n> checks)` with n at least 7, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bv-1"><invocation>cd C:/dev/wk-resapp-508 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-508/portal" 26d998f7 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 35 and T at least 38, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bv-1"><invocation>cd C:/dev/wk-resapp-508/portal &amp;&amp; python "C:/dev/wk-resapp-508/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 26d998f7 --head HEAD --receipt "C:/dev/wk-resapp-508/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~508/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~508 <0.9.0_WK_AMGT_RESAPP~508@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~508/AMGT_RESAPP.TO-AMGT-bv-1.remaining-date-bypasses-routed.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-508` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-508`.

Report once:
- the branch name, its head commit and the base `26d998f7`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-114 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round114.R1.md`, msg 7824) item list. One cell, one candidate branch cut from PROD `26d998f7`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-113 cells. AC2's totals were measured in a provisioned worktree cut at `26d998f7` at the cut (34 of 37, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs). The CTO's round-114 item 1 (W505-S1 and S2, the census re-run to zero). Disjoint write surface from bv-2 (a Python file). THE REAL GRADE for the dates is the rendered text; the close walk reads format:dates on ICT PM and RIO LN again.

<status>pending</status>
<round>115</round>
<slot>0.9.0_WK_AMGT_RESAPP~508</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
