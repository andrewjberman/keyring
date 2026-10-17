# AMGT_RESAPP task order -- `AMGT-bt-3` -- THE SHARED PRICE-CURRENCY HELPER TRIMS A PADDED SERVED CURRENCY CODE, WITH A FIXTURE (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bt-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~502</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bt-3.price-currency-trims-padding</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the existing harness reads `YES (6 of 6 checks)` and the expectation is n at least 7 with R7 named, so it FAILS on the count (R7 absent); AC2 run in a provisioned worktree cut at `856fb37b` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 30 of 33 pass, base <Q> of <U>, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new check against the unedited head before any product edit (step 2 or 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-502` (branch `wk-AMGT_RESAPP-502`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-502/portal` is cut at PROD `856fb37b`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-502`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bt-3` (round 113, decomposition s.122)

Round 112's `AMGT-bs-2` made ONE helper, `priceCurrencyOf`, in `src/pages/SecurityAnalysis/priceCurrency.ts`, read by the header tiles (`components/HeaderCards.tsx`) and the Peers table (`tabs/PeersTab.tsx`). Row `AMGT_RESAPP-D1-W497-S2`: the helper checks a code with `.trim()` for emptiness but RETURNS the served string untrimmed, where the Peers table's older helper returned it trimmed; a whitespace-padded served currency (`' PHP '`) therefore reaches `formatStatValue` as served and can fail to match a currency comparison. No live name carries a padded code (unmeasured on live bodies); the repair is defensive.

**The change.** In `priceCurrency.ts` ONLY: return the TRIMMED code on both branches (the `PX_LAST` currency and the `CRNCY` value). Nothing else changes in that file; `HeaderCards.tsx` and `PeersTab.tsx` are NOT edited (they already call the helper). For every unpadded input the helper's result is byte-identical to today.

**The grade.** The harness is the existing `src/pages/SecurityAnalysis/__harness__/priceCurrencyRule.harness.cjs` (round 112; it prints `PRICE CURRENCY RULE HARNESS: YES (6 of 6 checks)` on this head; read it first). YOU EXTEND it (edit that file; it is yours for this cell): add R7, named in the output: R7 the helper over padded inputs: `PX_LAST` currency `' PHP '` returns `PHP`; `PX_LAST` with no currency and `CRNCY` value `' PHP '` returns `PHP`; `PX_LAST` currency `'\tUSD\n'` returns `USD`; AND, on a synthetic ICT PM overlay whose `PX_LAST` currency is `' PHP '`, the rendered Peers table prints every USD figure as `USD ` and no bare `$` (the padded code behaves exactly as the unpadded `PHP` does in R3). Keep R1 to R6 as they are; if an existing check pins the untrimmed return, name it and update ONLY that expectation. A recorded text file is compared after normalising `\r\n` to `\n` on both sides (round 112 row S58). Print `PRICE CURRENCY RULE HARNESS: YES (<n> of <n> checks)` (at least 7, R1 to R7 named) or `NO`.

**Do this in order.** (1) `cd C:/dev/wk-resapp-502/portal && git switch -c cand/dell1/amgt-sa-price-currency-trim` (your nested worktree is cut at PROD `856fb37b`; confirm `git log -1 --format=%h` reads `856fb37b` before and after). (2) Add R7 to the harness FIRST and run it ONCE on the unedited head: it must print `NO` with R7 failing (the helper returns the padded string) and R1 to R6 passing; record that run. (3) Make the one-file product edit. (4) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~502/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `856fb37b`, every path changed since `856fb37b`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 856fb37b HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-price-currency-trim --purpose "AMGT_RESAPP bt-3: the shared price-currency helper trims a padded served currency code" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, ICT PM, header tiles and Peers tab (no visible change on live names)" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W502-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-502/portal`, new branch `cand/dell1/amgt-sa-price-currency-trim` cut from PROD `856fb37b`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `src/components/Tooltip.tsx` or any other shared file, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/priceCurrency.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~502/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bt-3"><invocation>cd C:/dev/wk-resapp-502/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/priceCurrencyRule.harness.cjs; echo "exit=$?"</invocation><expect>the line `PRICE CURRENCY RULE HARNESS: YES (<n> of <n> checks)` with n at least 7, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bt-3"><invocation>cd C:/dev/wk-resapp-502 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-502/portal" 856fb37b | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 30 and T at least 33, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bt-3"><invocation>cd C:/dev/wk-resapp-502/portal &amp;&amp; python "C:/dev/wk-resapp-502/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 856fb37b --head HEAD --receipt "C:/dev/wk-resapp-502/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~502/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~502 <0.9.0_WK_AMGT_RESAPP~502@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~502/AMGT_RESAPP.TO-AMGT-bt-3.price-currency-trims-padding.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-502` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-502`.

Report once:
- the branch name, its head commit and the base `856fb37b`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-112 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round112.R1.md`, msg 7733) item list. One cell, one candidate branch cut from PROD `856fb37b`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-113 cells. AC2's totals were measured in a provisioned worktree cut at `856fb37b` at the cut (30 of 33, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs). A defensive repair (no live name carries a padded code): the CTO's item 5 first half. The landing is the issuer's and a DT seat's (AMGT-bt-5, placed).

<status>pending</status>
<round>113</round>
<slot>0.9.0_WK_AMGT_RESAPP~502</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
