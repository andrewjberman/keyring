# AMGT_RESAPP task order -- `AMGT-br-3` -- THE `P/E NOT SHOWN` FOOTER NAMES THE MISSING FIGURE IN PLAIN WORDS, NEVER A VENDOR MNEMONIC, WITH A CENSUS OF EVERY MNEMONIC IT CAN PRINT (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-br-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~494</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-br-3.pe-footer-in-words</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1's harness file does not exist on the PROD head `99d2b2a7`, so AC1 FAILS at the base as expected (node exits non-zero on a missing file, read here); AC2 run in a provisioned worktree cut at `99d2b2a7` reads `R103 FEATURE GREEN: YES (... harness 26 of 29 pass, base 23 of 29, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs AC1 against the unedited head before any product edit (step 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-494` (branch `wk-AMGT_RESAPP-494`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-494/portal` is cut at PROD `99d2b2a7`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-494`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-br-3` (round 111, decomposition s.120)

On the Model tab's Key Figures table, a name with no P/E row prints ONE line `P/E not shown: <reasons joined by "; ">` (`ModelTab.tsx` line ~685: `<p data-model-summary-pe-reason="">`). Each reason is a SERVED sentence the page prints verbatim: for a historical year `fiscalPeReason(data, year)` (line ~197) returns the `reason` of the `fiscal_unresolved` `PE_RATIO` entry; for an estimate year `withheldPeReason(data, year)` returns its own. The served historical sentence is built by `lib/research/api/scoped_amgt.py` lines 2728-2765 as `price / reported EPS (IS_EPS), FY{year}, is not shown: {why}` where `{why}` is one of: `an input is absent (PX_LAST or IS_EPS)`; `reported EPS (IS_EPS) is not positive`; `the fiscal-year price (PX_LAST) is not positive`; `the currency of the price or of reported EPS is not stated`; `the price is in {ccy} and reported EPS in {ccy}, and a ratio of different currencies is not shown`. Walker findings `UIW-20261017T145445Z-007` and `-012` read, on RIO LN and ICT PM: `P/E not shown: price / reported EPS (IS_EPS), FY2025, is not shown: the price is in GBp and reported EPS in USD, ...`. `IS_EPS` and `PX_LAST` are vendor field mnemonics; a reader must never see one.

**The change (display only; the served sentence and the served backend are NOT touched).** In `ModelTab.tsx` only, put the reason through ONE local pure function `plainPeReason(reason: string): string` before it is printed (both the historical and the estimate-year source), which: (a) replaces the closed table `IS_EPS` -> `reported earnings per share` and `PX_LAST` -> `share price`, removing the parentheses that held them, so the five sentences above read, for example, `price / reported earnings per share, FY2025, is not shown: the price is in GBp and reported earnings per share in USD, and a ratio of different currencies is not shown`, `an input is absent (the share price or reported earnings per share)` and `the fiscal-year share price is not positive`; (b) replaces the bare phrase `reported EPS` with `reported earnings per share`; (c) as a safety net for a mnemonic the table does not know, replaces any remaining token matching `/\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b/` with `a vendor figure`. A reason with no mnemonic prints unchanged. The function never changes a number, a year or a currency code.

**THE CENSUS (a deliverable, in the receipt under `## Mnemonic census`).** List EVERY source of a string the footer can print and every vendor-mnemonic-shaped token each can contain: read `lib/research/api/scoped_amgt.py` (`fiscal_unresolved` PE_RATIO reasons, lines 2728-2765, AND every other place a P/E reason is built for an estimate year: search that file for `withheld`, `PE_RATIO`, `forward` and `reason`), and the portal side (`withheldPeReason`, and any other text `ModelTab.tsx` adds to the footer). Print the denominator: the number of reason-producing sites read, with `file:line` each, and the token set found (expected to contain at least `IS_EPS` and `PX_LAST`). A token found that the table does not name is added to the table (in plain words) AND reported. You may read `lib/` and write nothing there.

**The grade is on the RENDERED footer.** The new harness `src/pages/SecurityAnalysis/__harness__/peFooterWords.harness.cjs` (YOURS: create it; MODEL it on the existing `withheldReasons.harness.cjs`, whose check R6 renders the footer `<p data-model-summary-pe-reason="">` for a ZURN SW bundle; copy its rendering approach, do not edit it unless a check there pins the OLD words, in which case update ONLY that check's expected text in the same commit and name it in your report) renders the Key Figures footer with served bundles whose `fiscal_unresolved` carries each of the five `{why}` variants (build the reason strings the way `scoped_amgt.py` does, with `{ccy}` = `GBp` and `USD`), and checks, each named in the output: P1 the rendered footer text of EACH of the five variants contains NO token matching `/[A-Z][A-Z0-9]*_[A-Z0-9_]+/`; P2 the GBp/USD variant reads exactly `P/E not shown: price / reported earnings per share, FY2025, is not shown: the price is in GBp and reported earnings per share in USD, and a ratio of different currencies is not shown`; P3 the absent-input variant reads `...an input is absent (the share price or reported earnings per share)`; P4 a reason carrying an unknown token (`FOO_BAR`) prints `a vendor figure` and no `FOO_BAR`; P5 CONTROL: a reason with no mnemonic (`the currency of the price or of reported EPS is not stated` becomes `...reported earnings per share is not stated`, but a reason such as `the price is in GBp` alone) prints unchanged, and every number, year and currency code of the five variants survives; P6 the existing `withheldReasons.harness.cjs` still passes when spawned by yours (or fails only on a check you updated and named). Print `PE FOOTER WORDS HARNESS: YES (<n> of <n> checks)` or `NO` (at least 6 checks, P1 to P6 named).

**Do this in order.** (1) `cd C:/dev/wk-resapp-494/portal && git switch -c cand/dell1/amgt-sa-pe-footer-words` (your nested worktree is cut at PROD `99d2b2a7`; confirm `git log -1 --format=%h` reads `99d2b2a7`). (2) Read the existing `withheldReasons.harness.cjs` and the `scoped_amgt.py` lines above; write the census. (3) Create the harness FIRST and run it ONCE on the unedited head: it must print `NO` with P1 to P4 failing and P5 passing; record that run. (4) Make the product edit (`ModelTab.tsx` alone). (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~494/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `99d2b2a7`, every path changed since `99d2b2a7`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 99d2b2a7 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names), and a `## Mnemonic census` section (the sources read with file:line, the denominator, the token set). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-pe-footer-words --purpose "AMGT_RESAPP br-3: the P/E not shown footer names the missing figure in plain words, never a vendor mnemonic" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, RIO LN and ICT PM, Model tab, Key Figures footer" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W494-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-494/portal`, new branch `cand/dell1/amgt-sa-pe-footer-words` cut from PROD `99d2b2a7`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the one file this cell names (`src/pages/SecurityAnalysis/tabs/ModelTab.tsx`) and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `components/StatTile.tsx`, `components/HeaderCards.tsx` (unless this cell's body grants it), `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~494/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-br-3"><invocation>cd C:/dev/wk-resapp-494/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/peFooterWords.harness.cjs; echo "exit=$?"</invocation><expect>the line `PE FOOTER WORDS HARNESS: YES (<n> of <n> checks)` with n at least 6, every check of the cell's list named PASS, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-br-3"><invocation>cd C:/dev/wk-resapp-494 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-494/portal" 99d2b2a7 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base 23 of 29, regressions 0, pre-existing: <names>)` with P at least 27 and T at least 30, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-br-3"><invocation>cd C:/dev/wk-resapp-494/portal &amp;&amp; python "C:/dev/wk-resapp-494/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 99d2b2a7 --head HEAD --receipt "C:/dev/wk-resapp-494/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~494/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~494 <0.9.0_WK_AMGT_RESAPP~494@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~494/AMGT_RESAPP.TO-AMGT-br-3.pe-footer-in-words.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-494` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-494`.

Report once:
- the branch name, its head commit and the base `99d2b2a7`;
- the harness run at the unedited head (the NO line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-110 analysis (`ledger/ROUND_ANALYSIS.round110.md`, msg 7692) item list, the CTO's round-110 analysis item 3 and the walker findings 007 and 012 (the IS_EPS footer). One cell, one file, one candidate branch cut from PROD `99d2b2a7`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other two round-111 portal cells (`WhatChangedPanel.tsx`, `ModelTab.tsx`, `PeersTab.tsx`), so the three merge-forward in any order. AC2's totals were measured in a provisioned worktree cut at `99d2b2a7` at the cut (26 of 29, three pre-existing names); a new harness adds one file, so T is at least 30 and P at least 27. The grade of each cell is on the RENDERED output (the CTO's direction on W492-S3), the new harness reading visible text, never a formatter's return.

<status>pending</status>
<round>111</round>
<slot>0.9.0_WK_AMGT_RESAPP~494</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
