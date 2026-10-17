# AMGT_RESAPP task order -- `AMGT-bu-1` -- THE PEERS SUBJECT ROW'S MONEY CELLS READ THEIR CURRENCY CODE THROUGH ONE TRIMMING HELPER IN priceCurrency.ts, LIKE EVERY OTHER CELL (CLOSES W497-S2 THROUGH W502-S1; A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bu-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~504</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bu-1.peers-subject-currency-trim</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the existing harness reads `YES (7 of 7 checks)` and the expectation is n at least 8 with R8 named, so it FAILS on the count (R8 absent); AC2 run in a provisioned worktree cut at `d1bed0fb` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 32 of 35 pass, base <Q> of <U>, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new check against the unedited head before any product edit (step 2 or 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-504` (branch `wk-AMGT_RESAPP-504`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-504/portal` is cut at PROD `d1bed0fb`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-504`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bu-1` (round 114, decomposition s.123)

Round 113's `AMGT-bt-3` made the shared helper `priceCurrencyOf` in `src/pages/SecurityAnalysis/priceCurrency.ts` return a TRIMMED code, so the header tiles and the Peers table's price-currency reading are trimmed. Row `AMGT_RESAPP-D1-W502-S1` (which keeps `W497-S2` open): the Peers SUBJECT row's money cells do not go through the helper. In `src/pages/SecurityAnalysis/tabs/PeersTab.tsx`, `cellOf` (around lines 148-160) builds a subject cell for a header-tiled column (Price, Mkt Cap, EV) as `{ value: served, code: figure?.currency || null, ... }`: the figure's own served `currency` UNTRIMMED. A padded served code (`' PHP '`) therefore prints `PHP  860.00` (two spaces) on the subject Price cell, although the same code is trimmed everywhere the helper is used. No live name carries a padded code (unmeasured on live bodies); the repair is defensive and closes the row.

**The change (display only).** (1) In `priceCurrency.ts` add one exported function `currencyCodeOf(figure)`: given a header figure (`{ currency?: string | null }` or `null`/`undefined`) it returns the figure's `currency` TRIMMED when it is a non-empty string, else `null` (a one-line doc comment naming its callers). The existing `priceCurrencyOf` stays byte-identical. (2) In `PeersTab.tsx` replace `figure?.currency || null` in the subject cell's `code` with `currencyCodeOf(figure)` (import it beside `priceCurrencyOf`). Nothing else changes in `PeersTab.tsx`. Report (do not edit) whether `cscTable.ts`'s `currencyOf`, which feeds the MEMBER rows' codes, trims a served code: it is outside your grant; name what you read.

**The grade is on the RENDERED cell.** The harness is the existing `src/pages/SecurityAnalysis/__harness__/priceCurrencyRule.harness.cjs` (round 112/113; it prints `PRICE CURRENCY RULE HARNESS: YES (7 of 7 checks)` on this head and an extra `R7 OBSERVED (not graded)` line showing the padded subject Price cell as `PHP  860.00`; read it first). YOU EXTEND it (edit that file; it is yours for this cell): add R8, named in the output: on the synthetic ICT PM overlay used by R7 (PX_LAST currency `' PHP '`), the rendered Peers table's subject Price cell reads exactly the text of the UNPADDED render (`PHP 860.00`), AND on a synthetic copy whose served header figures carry padded own currencies (`' USD '` on the EV figure, `' PHP '` on Mkt Cap) the subject EV and Mkt Cap cells read exactly their unpadded renders; the R7 observed line becomes a graded part of R8 (remove the `OBSERVED (not graded)` print). Keep R1 to R7 as they are. A recorded text file is compared after normalising `\r\n` to `\n` on both sides (round 112 row S58). Print `PRICE CURRENCY RULE HARNESS: YES (<n> of <n> checks)` (at least 8, R1 to R8 named) or `NO`.

**Do this in order.** (1) `cd C:/dev/wk-resapp-504/portal && git switch -c cand/dell1/amgt-sa-peers-subject-currency` (your nested worktree is cut at PROD `d1bed0fb`; confirm `git log -1 --format=%h` reads `d1bed0fb` before and after). (2) Add R8 to the harness FIRST and run it ONCE on the unedited head: it must print `NO` with R8 failing (the subject cell reads two spaces) and R1 to R7 passing; record that run. (3) Make the two-file product edit. (4) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~504/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `d1bed0fb`, every path changed since `d1bed0fb`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff d1bed0fb HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-peers-subject-currency --purpose "AMGT_RESAPP bu-1: the Peers subject row's money cells read their currency code through one trimming helper" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, ICT PM, Peers tab, the subject row's Price, Mkt Cap and EV cells (no visible change on live names)" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W504-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-504/portal`, new branch `cand/dell1/amgt-sa-peers-subject-currency` cut from PROD `d1bed0fb`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `src/components/Tooltip.tsx` or any other shared file, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/priceCurrency.ts
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~504/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bu-1"><invocation>cd C:/dev/wk-resapp-504/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/priceCurrencyRule.harness.cjs; echo "exit=$?"</invocation><expect>the line `PRICE CURRENCY RULE HARNESS: YES (<n> of <n> checks)` with n at least 8, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bu-1"><invocation>cd C:/dev/wk-resapp-504 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-504/portal" d1bed0fb | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 32 and T at least 35, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bu-1"><invocation>cd C:/dev/wk-resapp-504/portal &amp;&amp; python "C:/dev/wk-resapp-504/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base d1bed0fb --head HEAD --receipt "C:/dev/wk-resapp-504/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~504/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~504 <0.9.0_WK_AMGT_RESAPP~504@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~504/AMGT_RESAPP.TO-AMGT-bu-1.peers-subject-currency-trim.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-504` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-504`.

Report once:
- the branch name, its head commit and the base `d1bed0fb`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-113 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round113.R1.md`, msg 7763) item list. One cell, one candidate branch cut from PROD `d1bed0fb`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-113 cells. AC2's totals were measured in a provisioned worktree cut at `d1bed0fb` at the cut (32 of 35, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs). The CTO's round-113 item 1 (closes W497-S2 through W502-S1). A defensive repair: no live name carries a padded code.

<status>pending</status>
<round>114</round>
<slot>0.9.0_WK_AMGT_RESAPP~504</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
