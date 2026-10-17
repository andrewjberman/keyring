# AMGT_RESAPP task order -- `AMGT-bp-1` -- A CHANGED FIGURE WHOSE VALUE IS A LIST NEVER CRASHES THE MODEL TAB (ONE PORTAL FEATURE CUT FROM PROD `15bc21b3`, WITH ITS RECEIPT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bp-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~488</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bp-1.changed-figure-list-value-never-crashes-the-model-tab</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1's harness `src/pages/SecurityAnalysis/__harness__/changedListValue.harness.cjs` does not exist at PROD `15bc21b3`: `node` exits 1 with MODULE_NOT_FOUND (read here), so AC1 reads FAIL there as expected; AC2 run on a detached worktree at PROD `15bc21b3` itself (since removed) reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 21 of 27 pass, base 21 of 27, ...)`, so its expectation of 28 harness files and 22 passing is unmet there as expected; AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs AC1 against the unchanged page before any product edit (step 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-488` (branch `wk-AMGT_RESAPP-488`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-488`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bp-1` (round 109, decomposition s.118)

On the Security Analysis page, the Model tab of RIO LN shows the page error screen ("Something went wrong ... `TypeError: value.trim is not a function`") on PROD. This ONE portal feature (Opal-internal, cut from PROD `15bc21b3`) removes the crash. Page side only: no served value moves, no figure is changed, no existing sentence is reworded.

**The cause, measured at the cut.** The served RIO LN compare (`opal-amgt-scoped-api` `/compare`, fixture below) lists 50 changed figures. 49 carry a number in `from` and `to`; ONE, the header figure `header|None|ERN_ANN_DT_AND_PER` (`mnemonic` `ERN_ANN_DT_AND_PER`, `scope` `header`, `fiscal_year` null), carries a LIST of records `{"announcement_date": "2026-10-13", "period": "2026:Q3"}` in `from` and in `to` (newest first). In `src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx` the function `numeric(value: number | string | null | undefined)` runs `value.trim()` on every value that is not a number, and `ChangedRow` and the formatter call it with `change.from` and `change.to`. A list has no `.trim`, so it throws while the panel renders and the page error boundary replaces the whole page. (The bug is older than round 108; a name shows it only when its compare lists that figure as changed.)

**The change.**
1. `numeric` NEVER throws: it returns the number for a finite number, parses a string as today, and returns `null` for anything else (a list, an object, a boolean). Fix every other call in `WhatChangedPanel.tsx` that assumes a scalar the same way (read the whole file: if another call would also throw or print `[object Object]` on a list value, it is in scope; if you find one outside this file, file a BLOCKING row and do not edit it).
2. A changed row whose `from` or `to` is a list prints that side as a plain reading, never `[object Object]` and never a blank: for the earnings-dates figure (every list entry has `announcement_date` and `period`) its NEWEST entry (the first), as `<announcement_date> (<period>)`, for example `2026-10-13 (2026:Q3)`; for any other list, `<n> entries`. Before and after each print their own side. Nothing else about the row changes: the figure name, the arrow, the percentage column where a number pair gives one (a list pair gives none and prints the dash the row already prints for a missing percentage), and every numeric row stay byte-for-byte as today.
3. The `Changed` count tile and the rows listed still agree exactly as they do today (this change drops no row).

**Fixtures (copy them into `src/pages/SecurityAnalysis/__harness__/`; all are committed in this repository, unedited live bodies read 2026-10-17).** From `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round109_prep/fixtures/`: `RIO_LN_compare_live.json` to `changedListFixture.RIO_LN_compare.json` (50 changed rows, one list-valued); `RIO_LN_model_slice_live.json` to `changedListFixture.RIO_LN_Equity.json` (the model block of the same name, for the withhold lookups the panel makes). ALREADY at PROD in that folder and not to be edited: `withheldFixture.ZURN_SW_compare.json` and `withheldFixture.ZURN_SW_Equity.json` (a compare with 33 numeric changed rows, the difference control) and the harness `withheldReasons.harness.cjs` (your model: it stubs `useModelCompare` and the other hooks so a static render of `WhatChangedPanel` resolves in one pass; transpile the page's own files with the installed typescript, render with react-dom/server, stub only the boundaries you do not own, write no file).

**Do this in order.** (1) `cd C:/dev/wk-resapp-488/portal && git switch -c cand/dell1/amgt-sa-changed-list-value` (from PROD `15bc21b3`, which your nested worktree is at). (2) Write the harness `src/pages/SecurityAnalysis/__harness__/changedListValue.harness.cjs` FIRST. It must check at least these 8, each named in the output: L1 the RIO LN compare renders `WhatChangedPanel` without throwing; L2 the rendered table lists every changed row the page lists for that compare and the `Changed` tile reads that same number (read both from the output, print both); L3 the earnings-dates row prints `<announcement_date> (<period>)` of the FIRST entry of `from` on its before side and of the FIRST entry of `to` on its after side, both read from the fixture, not typed; L4 the rendered output contains no `[object Object]` and no `undefined`; L5 a synthetic copy of the compare whose list-valued row is replaced by an object value, a boolean value and a list of strings (three variants, one render each) renders without throwing and prints `<n> entries` for the list of strings; L6 a numeric row of the RIO LN compare (`forecast|2026|BEST_BPS`) prints exactly the two numbers and the movement it printed before your edit (record its rendered row text at step 3 into `changedListFixture.base_row.json` and compare to it); L7 the difference control: the ZURN SW compare's whole rendered output after the edit has the SAME sha256 as before the edit (record the before-hash at step 3 into `changedListFixture.base_zurn.sha256`; the harness compares to that file); L8 a compare with NO list-valued row renders as before (the ZURN SW compare, L7 covers it; also assert its 33 rows). Print `CHANGED LIST VALUE HARNESS: YES (<n> of <n> checks)` or `NO`. If a premise above does not reproduce on a fixture (a field or a cell is not where this order says), file a BLOCKING row naming exactly what you found, finish what you can, and report; do not patch around it. (3) Run it ONCE on the unchanged page (create the two base files first by a small step of the harness run in a record-base mode, or a one-off node line; commit them): it must print `NO` (or exit 1 on a failing check) with L1 failing (the TypeError); record that run. (4) Then make the product edits, only in `src/pages/SecurityAnalysis/` (expected: `components/model/WhatChangedPanel.tsx` alone, plus the harness folder). (5) Run AC1 to AC3. (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~488/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, head commit, base `15bc21b3`, every changed path), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 15bc21b3 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis`, the name `RIO LN`, its Model tab). (7) Commit the branch in the nested worktree (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-changed-list-value --purpose "AMGT_RESAPP bp-1: a changed figure whose value is a list no longer crashes the Security Analysis Model tab (RIO LN)" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, RIO LN, Model tab" --portal portal` and report its output verbatim. Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-488/portal`, branch `cand/dell1/amgt-sa-changed-list-value` from PROD `15bc21b3`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only under `src/pages/SecurityAnalysis/` (the page's own files, its harness folder and its fixtures); never `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~488/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bp-1"><invocation>cd C:/dev/wk-resapp-488/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/changedListValue.harness.cjs; echo "exit=$?"</invocation><expect>the line `CHANGED LIST VALUE HARNESS: YES (<n> of <n> checks)` with n at least 8 and every check named PASS; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bp-1"><invocation>cd C:/dev/wk-resapp-488 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-488/portal" 15bc21b3 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 22 of 28 pass, base 21 of 27, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs posture.harness.cjs posturePattern.harness.cjs tabs.harness.cjs timelineFourStates.harness.cjs)` (the base's 27 harness files plus the new one is 28; the six names fail at PROD itself and read pre-existing) and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bp-1"><invocation>cd C:/dev/wk-resapp-488/portal &amp;&amp; python "C:/dev/wk-resapp-488/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 15bc21b3 --head HEAD --receipt "C:/dev/wk-resapp-488/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~488/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~488 <0.9.0_WK_AMGT_RESAPP~488@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~488/AMGT_RESAPP.TO-AMGT-bp-1.changed-figure-list-value-never-crashes-the-model-tab.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-488` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-488`.

Report once:
- the branch name, its head commit and base;
- the harness run at the unchanged page (the NO line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 7490 and `ROUND_ANALYSIS.round108.md` item 1 (W477-S1). Root cause found by the issuer at the cut (2026-10-17 ~12:0xZ) from the served RIO LN compare: one changed header figure `ERN_ANN_DT_AND_PER` whose `from`/`to` are lists; `numeric()` in `WhatChangedPanel.tsx` calls `.trim()` on it. Not in `AMGT-bo-1`'s diff. The wording of a list value (the newest entry, or `<n> entries`) is the issuer's decision (s.118 (a)); the CTO asked only that the page not crash. The placed cell `AMGT-bp-2` (the grid-opened walk of VLO US, RIO LN and WALMEX* MM on a local build of PROD plus this candidate) is cut when this order is complete. Lessons carried from `AMGT-bo-1`: the branch is cut from PROD, never from DEV; fixtures are live bodies, never hand-edited; AC2 grades lint on the feature's own folder; the order's file name is short so the instance's canonical path opens. AC2's totals (28 files, 22 passing, base 21 of 27, six pre-existing names) were measured at the cut on a detached worktree at PROD `15bc21b3`.

<status>pending</status>
<round>109</round>
<slot>0.9.0_WK_AMGT_RESAPP~488</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
