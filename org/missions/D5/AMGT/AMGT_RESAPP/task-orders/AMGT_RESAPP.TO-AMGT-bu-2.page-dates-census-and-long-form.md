# AMGT_RESAPP task order -- `AMGT-bu-2` -- EVERY DATE THE SECURITY ANALYSIS PAGE PRINTS FROM A SERVED ISO DAY PASSES THROUGH THE HOUSE LONG-DATE HELPER: A CENSUS OF EVERY DATE SITE FIRST, THEN THE BYPASSES ROUTED THROUGH IT, GRADED ON THE RENDERED TEXT (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bu-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~505</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bu-2.page-dates-census-and-long-form</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the new harness file does not exist, so it FAILS (exit 1); AC2 run in a provisioned worktree cut at `d1bed0fb` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 32 of 35 pass, base <Q> of <U>, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new check against the unedited head before any product edit (step 2 or 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-505` (branch `wk-AMGT_RESAPP-505`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-505/portal` is cut at PROD `d1bed0fb`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-505`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bu-2` (round 114, decomposition s.123)

The CTO's ruling (round-113 analysis, item 2): ONE date rule for the page and its printed pack: every date the Security Analysis page shows passes through the house long-date helper `longDate` in `src/pages/SecurityAnalysis/dateWords.ts` (read its header: the house form is `September 28th, 2026`; ISO stays only where no one reads it: `data-` attributes, URLs, export fields). Round 113's `AMGT-bt-1` routed the What Changed EARNINGS-DATES LIST through it. A real-browser walk of PROD `d1bed0fb` still reads the walker's `format:dates` finding on ICT PM (`2 date formats: 2026-09-22 | September 22nd, 2026`, in the older-version select states), and the shot shows the cause: the What Changed row `Date of the issuer's next expected earnings report (a DATE, not a number)` (mnemonic `EXPECTED_REPORT_DT`, scope `header`) prints its before and after values `2026-11-06` and `2026-11-11` as served ISO. A scalar date-valued changed figure takes a different path from the list. **This cell is census-first.**

**Step A, the census (a deliverable: the receipt's `## Date census` section and a committed fixture `src/pages/SecurityAnalysis/__harness__/dateSites.fixture.json`).** List EVERY site under `src/pages/SecurityAnalysis/` (not `__harness__/`) that prints a date or a day to a reader from a served value: for each, `file:line`, the served field or value it reads, whether it goes through `longDate` / `longStamp` / `etStamp` / `etDay` / `daysInWords` (or `formatPanelTimestamp`) or prints the served string directly (`bypass: true`), and its disposition (`fixed_here`, `deferred_to` with a named reason, or `no_date_shown` with why). Method: read the date helpers in `dateWords.ts` and `src/lib/dateUtils`, then search the folder for `announcement_date`, `_date`, `as_of`, `vintage`, `period_end`, `slice(0, 10)`, `toISOString`, `toLocaleDateString`, `Date(`, the helper names, and every string that is rendered from a field named like a date; read each hit in context (the folder holds about 250 hits across 32 files: a hit is not a site until you read it). Print the denominator: the number of files read and the number of sites. **Two files belong to other cells of this round and you must NOT edit them:** `src/pages/SecurityAnalysis/tabs/ModelTab.tsx` and `src/pages/SecurityAnalysis/tabs/PeersTab.tsx`: a bypass found there goes in the census as `deferred_to` (name the cell: `AMGT-bu-4` for ModelTab, `AMGT-bu-1` for PeersTab) and in a surprise row.

**Step B, the fix.** Route every `bypass: true` site you can reach (every file in your grant) through the right helper (`longDate` for a bare day; `longStamp`/`etStamp` for a stamped moment), starting with the scalar date row in `components/model/WhatChangedPanel.tsx`: a changed figure whose before or after value is a bare ISO day (`/^\d{4}-\d{2}-\d{2}$/`) prints it through `longDate` in the visible before and after cells AND in its expandable detail (`Earlier version: <long form>`); the change column and the change % column stay `--`. A value that is not a bare day prints as it came. Display only: no served value, no `data-` attribute, no ordering changes. Do not reword any existing sentence.

**Fixture.** Copy `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round114_prep/fixtures/ICT_PM_compare_scalar_date_20261014T130735Z_20261016T130554Z.json` (the live ICT PM compare of versions `20261014T130735Z` to `20261016T130554Z`, unedited, read 2026-10-17; it holds the `EXPECTED_REPORT_DT` row `2026-11-06` to `2026-11-11`) to `src/pages/SecurityAnalysis/__harness__/dateRuleFixture.ICT_PM_compare_scalar_date.json`. The ICT PM header fixture `changedListFixture.ICT_PM_header.json` and the RIO LN fixtures are already in the harness folder.

**The grade is on the RENDERED text.** The new harness `src/pages/SecurityAnalysis/__harness__/dateRule.harness.cjs` (YOURS: create it; MODEL it on `earningsLongDates.harness.cjs`, which renders the whole `WhatChangedPanel` to static markup with the hooks stubbed and reads the visible `<td>` text) checks, each named in the output: E1 the `EXPECTED_REPORT_DT` row's visible before and after cells read exactly `November 6th, 2026` and `November 11th, 2026`; E2 its expanded detail reads `November 6th, 2026` and `November 11th, 2026` (the earlier and later version lines) and no ISO; E3 NO text matching `\d{4}-\d{2}-\d{2}` in the rendered visible text (tags stripped, attributes excluded) of the WHOLE What Changed render of that compare; E4 CONTROL: the RIO LN compare render (`changedListFixture.RIO_LN_compare.json` with `changedListFixture.RIO_LN_Equity.json`) is byte-identical to its render at the base head (record its visible-text sha256 BEFORE the edit); E5 the census: `dateSites.fixture.json` exists, its printed denominator equals its entry count, and every entry with `bypass: true` is either `fixed_here` (and the harness renders it with no ISO day) or `deferred_to` a named cell, never blank; E6 a value that is not a bare day (`n/a`) in a scalar date row prints as it came; E7 the three older What Changed harnesses still pass when spawned by yours (`changedListValue.harness.cjs` YES 16 of 16, `changedObjectCells.harness.cjs` YES 6 of 6, `earningsLongDates.harness.cjs` YES 7 of 7). Print `DATE RULE HARNESS: YES (<n> of <n> checks)` or `NO` (at least 7 checks, E1 to E7 named). A recorded text file is compared after normalising `\r\n` to `\n` on both sides (round 112 row S58).

**Do this in order.** (1) `cd C:/dev/wk-resapp-505/portal && git switch -c cand/dell1/amgt-sa-page-dates-long-form` (your nested worktree is cut at PROD `d1bed0fb`; confirm `git log -1 --format=%h` reads `d1bed0fb` before and after). (2) Write the census (Step A) and the fixture. (3) Create the new harness FIRST (record the E4 base digest) and run it ONCE on the unedited head: it must print `NO` with E1, E2 and E3 failing and E4, E6 and E7 passing; record that run. (4) Make the Step B edits. (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~505/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `d1bed0fb`, every path changed since `d1bed0fb`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff d1bed0fb HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-page-dates-long-form --purpose "AMGT_RESAPP bu-2: every date the page prints from a served ISO day passes through the house long-date helper" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, ICT PM, Model tab, What Changed (older version pairs), the next-expected-earnings-report row; RIO LN as the control" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W505-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-505/portal`, new branch `cand/dell1/amgt-sa-page-dates-long-form` cut from PROD `d1bed0fb`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `src/components/Tooltip.tsx` or any other shared file, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/
portal/src/pages/SecurityAnalysis/dateWords.ts
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~505/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bu-2"><invocation>cd C:/dev/wk-resapp-505/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/dateRule.harness.cjs; echo "exit=$?"</invocation><expect>the line `DATE RULE HARNESS: YES (<n> of <n> checks)` with n at least 7, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bu-2"><invocation>cd C:/dev/wk-resapp-505 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-505/portal" d1bed0fb | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 33 and T at least 36, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bu-2"><invocation>cd C:/dev/wk-resapp-505/portal &amp;&amp; python "C:/dev/wk-resapp-505/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base d1bed0fb --head HEAD --receipt "C:/dev/wk-resapp-505/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~505/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~505 <0.9.0_WK_AMGT_RESAPP~505@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~505/AMGT_RESAPP.TO-AMGT-bu-2.page-dates-census-and-long-form.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-505` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-505`.

Report once:
- the branch name, its head commit and the base `d1bed0fb`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-113 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round113.R1.md`, msg 7763) item list. One cell, one candidate branch cut from PROD `d1bed0fb`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-113 cells. AC2's totals were measured in a provisioned worktree cut at `d1bed0fb` at the cut (32 of 35, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs). The CTO's round-113 item 2, page half (census first, then the bypasses): the pack half is AMGT-bu-3 (a served path, a redeploy under a never-widen pair, AMGT-bu-7 placed). Files: the grant excludes ModelTab.tsx (bu-4) and PeersTab.tsx (bu-1) so the three candidates do not conflict at the merge-forward.

<status>pending</status>
<round>114</round>
<slot>0.9.0_WK_AMGT_RESAPP~505</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
