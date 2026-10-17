# AMGT_RESAPP task order -- `AMGT-bt-1` -- THE EARNINGS ROW AND ITS DETAIL PRINT DATES IN THE PAGE'S LONG FORM, NEVER THE SERVED ISO DAY (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~500</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bt-1.earnings-dates-in-long-form</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the new harness file does not exist, so it FAILS (exit 1); AC2 run in a provisioned worktree cut at `856fb37b` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 30 of 33 pass, base <Q> of <U>, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new check against the unedited head before any product edit (step 2 or 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-500` (branch `wk-AMGT_RESAPP-500`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-500/portal` is cut at PROD `856fb37b`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-500`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bt-1` (round 113, decomposition s.122)

The walker's `format:dates` finding (`2 date formats: 2026-09-22 | September 22nd, 2026`, on RIO LN's and ICT PM's Model tab in the older-version select states) is the What Changed earnings row printing the served ISO `announcement_date`: its visible before and after cells read `2026-10-13 (2026:Q3), 135 entries` (the `listReading` function in `src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx`) and its expandable detail reads `<ISO date> (<period>); ...; <n> entries in all` (the `fullReading` function in the same file), while every other date on the page reads the house long form, `October 13th, 2026`. The house form is `longDate` in `src/pages/SecurityAnalysis/dateWords.ts` (read its header: ISO stays only where no one reads it).

**The change (display only).** In `WhatChangedPanel.tsx` ONLY: import `longDate` from the page's `dateWords` module (the path resolves from `components/model/` as `../../dateWords`) and pass the `announcement_date` of every entry the earnings reading prints through it, in BOTH `listReading` (the visible cells) and `fullReading` (the detail). The period text, the comma, the `<n> entries` count, the `; ` joins and the `<n> entries in all` tail do not change. A value that is not a bare day (`longDate` returns it as it came) prints as it came. No other row, helper or sentence changes; the served value is untouched.

**Existing checks that pin the ISO text (you update ONLY these, naming each).** Round 110's `changedListValue.harness.cjs` (its checks for the earnings row's detail, L10 and any other that spells an ISO date) and round 111's `changedObjectCells.harness.cjs` (O3 and O4, and the recorded files `changedObjectFixture.base_rio_row.txt` and `changedObjectFixture.base_digests.json`) record the earnings row's text with the ISO dates. Update their EXPECTATIONS for the earnings row to the long form and re-record the base text for that ONE row deliberately (name in your report that you re-recorded it and why); the byte-identity controls on every OTHER row (O5: the other RIO LN rows and the ICT PM rows) must stay exactly as recorded. A recorded text file is compared after normalising `\r\n` to `\n` on BOTH sides (git writes CRLF on this machine and a byte-for-byte compare fails on a fresh checkout; round 112 row S58): fix any comparison you touch, never re-record to hide it.

**Expected strings are written by hand from the fixture, never by importing the helper** (a harness must not grade `longDate` with `longDate`). Read the committed fixture `changedListFixture.RIO_LN_Equity.json` / `changedListFixture.RIO_LN_compare.json` (already in the harness folder): its first date `2026-10-13` reads `October 13th, 2026`; write the long form of each of the first five dates of the `from` and of the `to` list as literals (ordinals: 1st, 2nd, 3rd, 4th to 20th with `th`, 21st, 22nd, 23rd, 31st).

**The grade is on the RENDERED text.** The new harness `src/pages/SecurityAnalysis/__harness__/earningsLongDates.harness.cjs` (YOURS: create it; MODEL it on `changedObjectCells.harness.cjs`, which renders the whole `WhatChangedPanel` to static markup with the hooks stubbed and reads the visible `<td>` text) checks, each named in the output: D1 the earnings row's visible before and after cells read exactly `October 13th, 2026 (2026:Q3), 135 entries` and `October 13th, 2026 (2026:Q3), 136 entries`; D2 the expanded detail of that row reads the first five dates of each list in long form joined by `; ` and then `135 entries in all` (before) and `136 entries in all` (after); D3 NO text matching `\d{4}-\d{2}-\d{2}` in the earnings row's visible cells or in its detail; D4 the period text `(2026:Q3)` is unchanged and present; D5 a synthetic list whose entries carry `announcement_date` `n/a` prints `n/a` as it came, never an empty string or `undefined`; D6 CONTROL: every other row of the RIO LN render and of the ICT PM render is byte-identical to the recorded base digests; D7 the two updated harnesses still print `CHANGED LIST VALUE HARNESS: YES (16 of 16 checks)` and `CHANGED OBJECT CELLS HARNESS: YES (6 of 6 checks)` when spawned by yours. Print `EARNINGS LONG DATES HARNESS: YES (<n> of <n> checks)` or `NO` (at least 7 checks, D1 to D7 named).

**Do this in order.** (1) `cd C:/dev/wk-resapp-500/portal && git switch -c cand/dell1/amgt-sa-earnings-long-dates` (your nested worktree is cut at PROD `856fb37b`; confirm `git log -1 --format=%h` reads `856fb37b` before and after). (2) Create the new harness FIRST and run it ONCE on the unedited head: it must print `NO` with D1, D2 and D3 failing and D4 to D6 passing (D7 passes: the two old harnesses still match the old text); record that run. (3) Make the product edit and update the two old harnesses and their recorded base row. (4) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~500/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `856fb37b`, every path changed since `856fb37b`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 856fb37b HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-earnings-long-dates --purpose "AMGT_RESAPP bt-1: the earnings row and its detail print dates in the page's long form" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, RIO LN and ICT PM, Model tab, What Changed, the earnings row (older version pairs)" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W500-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-500/portal`, new branch `cand/dell1/amgt-sa-earnings-long-dates` cut from PROD `856fb37b`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `src/components/Tooltip.tsx` or any other shared file, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~500/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bt-1"><invocation>cd C:/dev/wk-resapp-500/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/earningsLongDates.harness.cjs; echo "exit=$?"</invocation><expect>the line `EARNINGS LONG DATES HARNESS: YES (<n> of <n> checks)` with n at least 7, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bt-1"><invocation>cd C:/dev/wk-resapp-500 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-500/portal" 856fb37b | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 31 and T at least 34, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bt-1"><invocation>cd C:/dev/wk-resapp-500/portal &amp;&amp; python "C:/dev/wk-resapp-500/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 856fb37b --head HEAD --receipt "C:/dev/wk-resapp-500/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~500/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~500 <0.9.0_WK_AMGT_RESAPP~500@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~500/AMGT_RESAPP.TO-AMGT-bt-1.earnings-dates-in-long-form.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-500` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-500`.

Report once:
- the branch name, its head commit and the base `856fb37b`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-112 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round112.R1.md`, msg 7733) item list. One cell, one candidate branch cut from PROD `856fb37b`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-113 cells. AC2's totals were measured in a provisioned worktree cut at `856fb37b` at the cut (30 of 33, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs). The three-way expectation: the new harness fails at the base on D1 to D3. The grade is the rendered text (the CTO's item 1, RIO LN and ICT PM).

<status>complete -- drained by the issuer (2.0.0_SA_COO~R1) 2026-10-17: worker ~500 at c350f8b500 (merged 2a575f68cd); proof VALID rc=0 on the worker's checker; issuer re-runs in a FRESH checkout of the candidate: EARNINGS LONG DATES HARNESS YES (7 of 7), CHANGED LIST VALUE HARNESS YES (16 of 16), CHANGED OBJECT CELLS HARNESS YES (6 of 6); diff read: WhatChangedPanel.tsx three lines (the longDate import and its two uses in listReading and fullReading), the two older harnesses' pinned expectations updated, the earnings row's recorded base text re-recorded for that ONE row (the other 46 RIO LN and 13 ICT PM rows byte-identical to the recorded digests) and the recorded-text comparison normalising CRLF; candidate cand/dell1/amgt-sa-earnings-long-dates head c4e4f96af3 on PROD 856fb37b; at the unedited head the new harness read NO (4 of 7: D1, D2, D3 failing); rows W500-S1..S2 INERT; approval row dell1-20261017T210225Z-5058</status>
<round>113</round>
<slot>0.9.0_WK_AMGT_RESAPP~500</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
