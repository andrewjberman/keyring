# AMGT_RESAPP task order -- `AMGT-br-1` -- AN OBJECT-VALUED WHAT CHANGED CELL RENDERS AS READABLE TEXT, NEVER RAW JSON (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-br-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~493</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-br-1.object-cells-as-text</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1's harness file does not exist on the PROD head `99d2b2a7`, so AC1 FAILS at the base as expected (node exits non-zero on a missing file, read here); AC2 run in a provisioned worktree cut at `99d2b2a7` reads `R103 FEATURE GREEN: YES (... harness 26 of 29 pass, base 23 of 29, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs AC1 against the unedited head before any product edit (step 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-493` (branch `wk-AMGT_RESAPP-493`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-493/portal` is cut at PROD `99d2b2a7`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-493`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-br-1` (round 111, decomposition s.120)

A changed figure whose served value is an OBJECT (not a list) prints raw JSON in its VISIBLE before and after cells today. Round 110's `AMGT-bq-1` fixed the row's expandable detail (it prints `key: value` pairs) and the list case, but its worker found (row `AMGT_RESAPP-D1-W492-S3`) that `listReading` in `src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx` still ends with `return JSON.stringify(value)` for a non-list object, so the visible cell of an object row prints braces and quotes (`{"window":"x"}`); and its harness graded only the formatter and the detail, never the visible cell. This cell makes the VISIBLE before and after cells of an object-valued row print the same readable text the expanded detail prints, and grades the RENDERED cell.

**What the file does today (read it first, on the PROD head `99d2b2a7`).** `listReading(value)`: a list prints `<announcement_date> (<period>), <n> entries` for the earnings-dates list or `<n> entries` for any other list; any other object falls through to `JSON.stringify(value)`. The expandable detail is built by a helper named `full` in the same file; for an object it prints `key: value` pairs joined by `; ` (never braces, brackets or quotes). The existing harness `src/pages/SecurityAnalysis/__harness__/changedListValue.harness.cjs` (prints `CHANGED LIST VALUE HARNESS: YES (16 of 16 checks)` on this head) stubs `useModelCompare` and the other hooks so a static `react-dom/server` render of `WhatChangedPanel` resolves in one pass: it is YOUR MODEL; read it first and copy its stubbing, do not edit it.

**The change.** In `WhatChangedPanel.tsx` only: the visible before and after cell of a changed row whose value is a non-list object prints through the SAME object-to-text helper the expanded detail uses (extract or reuse; the cell and the detail must agree for every object). A nested list inside an object prints as `<n> entries`, a nested object prints its own `key: value` pairs in parentheses `(k: v; k2: v2)`; a scalar, a list, and every row that is not an object print exactly as today (the list reading `<announcement_date> (<period>), <n> entries` is a CONTROL that already renders and must stay byte-identical). Display only: no served value or figure changes, no existing sentence is reworded.

**The grade is on the RENDERED cell.** The new harness `src/pages/SecurityAnalysis/__harness__/changedObjectCells.harness.cjs` (YOURS: create it; model it on the existing one) renders the whole `WhatChangedPanel` to static markup, takes the text of every visible before and after `<td>` (NOT the formatter's return value; strip tags the way a reader sees the cell), and checks, each named in the output: O1 a synthetic compare whose changed row has the object value `{"window":"x","limit":3}` renders before and after cells with NO `{`, `}`, `[`, `]` or `"` character and contains `window: x` and `limit: 3`; O2 a synthetic object holding a list and an object (`{"dates":[1,2,3],"inner":{"a":1}}`) renders `dates: 3 entries` and `inner: (a: 1)` and no brace, bracket or quote; O3 the object row's expanded detail text equals its visible cell text for the same side (the cell and the detail agree); O4 CONTROL: the RIO LN compare (committed fixture `changedListFixture.RIO_LN_compare.json` with `changedListFixture.RIO_LN_Equity.json`, already in the harness folder) renders the earnings-dates row's visible cells exactly as the base head does (record the base head's visible text for that row in a fixture file `changedObjectFixture.base_rio_row.txt` BEFORE the product edit, from this same render, and compare); O5 CONTROL: every other row of that RIO LN render and of the ICT PM compare (`changedListFixture.ICT_PM_compare.json` with `changedListFixture.ICT_PM_header.json`) is byte-identical to the base head's render (record both base renders' visible-text sha256 in `changedObjectFixture.base_digests.json` before the edit); O6 the existing harness `changedListValue.harness.cjs` still prints `YES (16 of 16 checks)` when spawned by yours. Print `CHANGED OBJECT CELLS HARNESS: YES (<n> of <n> checks)` or `NO` (at least 6 checks, O1 to O6 named).

**Do this in order.** (1) `cd C:/dev/wk-resapp-493/portal && git switch -c cand/dell1/amgt-sa-changed-object-cells` (your nested worktree is cut at PROD `99d2b2a7`; confirm `git log -1 --format=%h` reads `99d2b2a7` before and after the switch). (2) Create the harness FIRST with O1 to O6 and record the base fixtures (O4, O5 need the base head's text: capture them with the harness itself before any product edit). (3) Run it ONCE on the unedited head: it must print `NO` with O1, O2 and O3 failing (the cell prints JSON) and O4 to O6 passing; record that run. (4) Make the product edit (`WhatChangedPanel.tsx` alone). (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~493/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `99d2b2a7`, every path changed since `99d2b2a7`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 99d2b2a7 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-changed-object-cells --purpose "AMGT_RESAPP br-1: an object-valued What Changed cell renders as readable text, never raw JSON" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, RIO LN and ICT PM, Model tab, What Changed" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W493-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-493/portal`, new branch `cand/dell1/amgt-sa-changed-object-cells` cut from PROD `99d2b2a7`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the one file this cell names (`src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx`) and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `components/StatTile.tsx`, `components/HeaderCards.tsx` (unless this cell's body grants it), `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~493/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-br-1"><invocation>cd C:/dev/wk-resapp-493/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/changedObjectCells.harness.cjs; echo "exit=$?"</invocation><expect>the line `CHANGED OBJECT CELLS HARNESS: YES (<n> of <n> checks)` with n at least 6, every check of the cell's list named PASS, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-br-1"><invocation>cd C:/dev/wk-resapp-493 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-493/portal" 99d2b2a7 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base 23 of 29, regressions 0, pre-existing: <names>)` with P at least 27 and T at least 30, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-br-1"><invocation>cd C:/dev/wk-resapp-493/portal &amp;&amp; python "C:/dev/wk-resapp-493/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 99d2b2a7 --head HEAD --receipt "C:/dev/wk-resapp-493/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~493/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~493 <0.9.0_WK_AMGT_RESAPP~493@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~493/AMGT_RESAPP.TO-AMGT-br-1.object-cells-as-text.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-493` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-493`.

Report once:
- the branch name, its head commit and the base `99d2b2a7`;
- the harness run at the unedited head (the NO line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-110 analysis (`ledger/ROUND_ANALYSIS.round110.md`, msg 7692) item list, W492-S3 (the visible object cell) and the CTO's round-110 analysis item 1 (graded on the rendered cell). One cell, one file, one candidate branch cut from PROD `99d2b2a7`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other two round-111 portal cells (`WhatChangedPanel.tsx`, `ModelTab.tsx`, `PeersTab.tsx`), so the three merge-forward in any order. AC2's totals were measured in a provisioned worktree cut at `99d2b2a7` at the cut (26 of 29, three pre-existing names); a new harness adds one file, so T is at least 30 and P at least 27. The grade of each cell is on the RENDERED output (the CTO's direction on W492-S3), the new harness reading visible text, never a formatter's return.

<status>pending</status>
<round>111</round>
<slot>0.9.0_WK_AMGT_RESAPP~493</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
