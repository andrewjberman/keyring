# AMGT_RESAPP task order -- `AMGT-br-4` -- THE PEERS TAB PRINTS A MONEY FIGURE'S CURRENCY CODE WHEN IT IS NOT THE PAGE NAME'S PRICE CURRENCY, SIGN FIRST (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-br-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~495</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-br-4.peers-currency-code</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1's harness file does not exist on the PROD head `99d2b2a7`, so AC1 FAILS at the base as expected (node exits non-zero on a missing file, read here); AC2 run in a provisioned worktree cut at `99d2b2a7` reads `R103 FEATURE GREEN: YES (... harness 26 of 29 pass, base 23 of 29, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs AC1 against the unedited head before any product edit (step 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-495` (branch `wk-AMGT_RESAPP-495`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-495/portal` is cut at PROD `99d2b2a7`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-495`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-br-4` (round 111, decomposition s.120)

Round 110's `AMGT-bp-4` made the header tiles (`HeaderCards.tsx`, with `StatTile.tsx`'s `formatStatValue(..., priceCurrency)`) print `USD ` for a USD figure on a name whose price is in another currency, and `bq-1` did the same in What Changed. The Peers tab was outside both grants. The walker (finding `UIW-20261017T145445Z-011`, `format:money`) reads, on ICT PM's Peers tab, money written as `USD 1,234` and `$1,234` on the SAME page. This cell extends the rule to the Peers table so one page carries one notation.

**The rule (decided by the issuer; one reference currency per page).** The reference is the PAGE NAME's price currency: the served `PX_LAST` figure's `currency` in the overlay's `header_figures` (the name whose Security Analysis page is open: ICT PM is PHP, GOOGL US is USD). EVERY money cell of the Peers table, the subject's row AND each member's row AND the summary rows (Average, Median, Min, Max), prints through `formatStatValue(value, format, code, unit, basis, priceCurrency)` with that ONE `priceCurrency` as its sixth argument (today the calls in `PeersTab.tsx` lines ~171-191 pass at most five arguments). So on ICT PM (PHP) a USD figure prints `USD 1,234` wherever it sits, including a USD-priced member's row; on GOOGL US (USD) a USD figure keeps `$`; every other code prints as today. The sign still leads. The price currency is read from the overlay bundle the tab already loads (`useSecurityOverlay`, already imported): add a small local helper `priceCurrencyOf(bundle)` (about five lines) to `PeersTab.tsx`; do NOT import it from `HeaderCards.tsx` and do NOT edit `StatTile.tsx` or `HeaderCards.tsx` (they are not in your grant). If no price currency is served, pass `null` (today's behaviour).

**Fixtures (committed in this repository; unedited live bodies read 2026-10-17; copy them into `src/pages/SecurityAnalysis/__harness__/`).** From `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round111_prep/fixtures/`: `ICT_PM_peers_live.json` to `peersCurrencyFixture.ICT_PM_peers.json` (the `/peers` body: one member, price and cap currency USD, plus the subject), `ICT_PM_overlay_slice_live.json` to `peersCurrencyFixture.ICT_PM_overlay.json` (`header_figures`; `PX_LAST` 860.0 in `PHP`), `GOOGL_US_peers_live.json` to `peersCurrencyFixture.GOOGL_US_peers.json`, `GOOGL_US_overlay_slice_live.json` to `peersCurrencyFixture.GOOGL_US_overlay.json` (`PX_LAST` in `USD`). The existing harnesses `peersCarry.harness.cjs`, `peersPattern.harness.cjs` and `peersReadFailed.harness.cjs` in the same folder render `PeersTab` statically with the hooks stubbed: they are YOUR MODEL for the stubbing (read them first; do not edit them).

**The grade is on the RENDERED table.** The new harness `src/pages/SecurityAnalysis/__harness__/peersCurrency.harness.cjs` (YOURS: create it) renders `PeersTab` to static markup and reads the visible text of every money `<td>` (the table's cells, as a reader sees them), and checks, each named in the output: K1 ICT PM (PHP-priced): no money cell carries a bare `$` (every USD cell reads `USD `), and at least one cell reads `USD ` followed by digits; K2 ICT PM: the SAME notation holds for the subject row, the member row and the summary rows (list the notations found: the set of money prefixes in the whole table is exactly `{USD }` plus any other served code, never `$` and `USD ` together); K3 CONTROL GOOGL US (USD-priced): the money cells keep `$`, and no cell reads `USD `; K4 a negative money cell on ICT PM prints sign first (`-USD `), built by a synthetic copy of the body with one value negated; K5 CONTROL: a ratio column (no money) renders byte-identical to the base head's render (record the base head's ratio-cell texts in a fixture file `peersCurrencyFixture.base_ratio.txt` BEFORE the product edit, from this same harness); K6 the three existing peers harnesses still print their YES line when spawned by yours. Print `PEERS CURRENCY HARNESS: YES (<n> of <n> checks)` or `NO` (at least 6 checks, K1 to K6 named).

**Do this in order.** (1) `cd C:/dev/wk-resapp-495/portal && git switch -c cand/dell1/amgt-sa-peers-currency` (your nested worktree is cut at PROD `99d2b2a7`; confirm `git log -1 --format=%h` reads `99d2b2a7`). (2) Create the harness FIRST with K1 to K6 and record the base ratio text. (3) Run it ONCE on the unedited head: it must print `NO` with K1, K2 and K4 failing (a USD cell reads `$` beside `USD `) and K3, K5, K6 passing; record that run (if K1 or K2 already pass on the base head because the premise does not reproduce on the fixture, file a BLOCKING row naming exactly what the render shows and finish what you can). (4) Make the product edit (`PeersTab.tsx` alone). (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~495/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `99d2b2a7`, every path changed since `99d2b2a7`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 99d2b2a7 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-peers-currency --purpose "AMGT_RESAPP br-4: the Peers tab prints a money figure's currency code when it is not the name's price currency" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, ICT PM, Peers tab; GOOGL US as the USD-priced control" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W495-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-495/portal`, new branch `cand/dell1/amgt-sa-peers-currency` cut from PROD `99d2b2a7`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the one file this cell names (`src/pages/SecurityAnalysis/tabs/PeersTab.tsx`) and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `components/StatTile.tsx`, `components/HeaderCards.tsx` (unless this cell's body grants it), `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~495/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-br-4"><invocation>cd C:/dev/wk-resapp-495/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/peersCurrency.harness.cjs; echo "exit=$?"</invocation><expect>the line `PEERS CURRENCY HARNESS: YES (<n> of <n> checks)` with n at least 6, every check of the cell's list named PASS, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-br-4"><invocation>cd C:/dev/wk-resapp-495 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-495/portal" 99d2b2a7 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base 23 of 29, regressions 0, pre-existing: <names>)` with P at least 27 and T at least 30, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-br-4"><invocation>cd C:/dev/wk-resapp-495/portal &amp;&amp; python "C:/dev/wk-resapp-495/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 99d2b2a7 --head HEAD --receipt "C:/dev/wk-resapp-495/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~495/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~495 <0.9.0_WK_AMGT_RESAPP~495@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~495/AMGT_RESAPP.TO-AMGT-br-4.peers-currency-code.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-495` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-495`.

Report once:
- the branch name, its head commit and the base `99d2b2a7`;
- the harness run at the unedited head (the NO line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-110 analysis (`ledger/ROUND_ANALYSIS.round110.md`, msg 7692) item list, the CTO's round-110 analysis item 4 and the walker finding 011 (two money notations on one Peers page). One cell, one file, one candidate branch cut from PROD `99d2b2a7`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other two round-111 portal cells (`WhatChangedPanel.tsx`, `ModelTab.tsx`, `PeersTab.tsx`), so the three merge-forward in any order. AC2's totals were measured in a provisioned worktree cut at `99d2b2a7` at the cut (26 of 29, three pre-existing names); a new harness adds one file, so T is at least 30 and P at least 27. The grade of each cell is on the RENDERED output (the CTO's direction on W492-S3), the new harness reading visible text, never a formatter's return.

<status>pending</status>
<round>111</round>
<slot>0.9.0_WK_AMGT_RESAPP~495</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
