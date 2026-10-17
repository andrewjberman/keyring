# AMGT_RESAPP task order -- `AMGT-bs-2` -- THE HEADER TILES AND THE PEERS TABLE READ THE PAGE NAME'S PRICE CURRENCY BY ONE RULE FROM ONE HELPER, AND THE ROUND-111 PEERS HARNESS PASSES ON ANY CHECKOUT (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bs-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~497</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bs-2.one-currency-rule-header-peers</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the harness file does not exist, so it FAILS (exit 1); AC2 run in a provisioned worktree cut at `932cea99` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 28 of 32 pass, base 25 of 32, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs peersCurrency.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected; `peersCurrency.harness.cjs` is pre-existing there because of the CRLF checkout defect named in the order of `AMGT-bs-2`); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new harness against the unedited head before any product edit (step 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-497` (branch `wk-AMGT_RESAPP-497`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-497/portal` is cut at PROD `932cea99`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-497`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bs-2` (round 112, decomposition s.121)

Two rules read the page name's price currency today (row `AMGT_RESAPP-D1-W495-S2`). `HeaderCards.tsx` has a local `priceCurrencyOf(bundle)` (read it on PROD `932cea99`): the served `PX_LAST` figure's `currency` if it is a non-empty string, else the served `CRNCY` figure's `value` if it is a non-empty string, else `null`. `PeersTab.tsx` has its own local `priceCurrencyOf(bundle)` (added by round 111's `AMGT-br-4`): the `PX_LAST` currency only, else `null`. On a name whose `PX_LAST` carries no currency but whose `CRNCY` is served, the header prints `USD ` for a USD figure while the Peers table prints `$`: the header and the table disagree. This cell makes ONE helper, read by both.

**The change.** (a) Create `src/pages/SecurityAnalysis/priceCurrency.ts` (NEW FILE, yours) exporting `priceCurrencyOf(figures: ReadonlyArray<{ mnemonic?: string | null; currency?: string | null; value?: unknown }> | null | undefined): string | null` with EXACTLY the header's rule above (`PX_LAST` currency, trimmed non-empty; else `CRNCY` value, trimmed non-empty string; else `null`); a one-comment header naming the rule and its two callers. (b) `HeaderCards.tsx`: delete its local helper and import the shared one (call it with `bundle.header_figures`); behaviour byte-identical. (c) `PeersTab.tsx`: delete its local helper and import the shared one (call it with the overlay bundle's `header_figures`). Nothing else changes in those two files. Display only.

**W495-S1 is NOT a cell and you must not change it.** The GOOGL US control's member SPCX prints its Price cell as `148.07 currency not stated`: the served peer body for that member carries `price_currency_reason` = "The scanner price for this peer carries no currency, and this peer is not matched to a company record that states its trading currency." The currency of that price is genuinely not known, so the words are the served truth and the rule never invents a currency. Leave that cell's text as it is; the harness (R6 below) asserts it does not change.

**A defect to fix in the same cell (found by the issuer, instrument trap).** Round 111's `peersCurrency.harness.cjs` check K5 compares the ratio cells' rendered text with the committed `peersCurrencyFixture.base_ratio.txt` byte for byte. On this machine git checks text files out with CRLF (`core.autocrlf=true`), so on ANY fresh checkout the recorded file reads CRLF and K5 FAILS (`ratio cells 24; byte-identical to the base recording: false`), although the harness passed in the worktree where the file was written. Fix K5 by normalising line endings on BOTH sides before the comparison (replace `\r\n` with `\n` in the recorded text and in the rendered text), never by re-recording the base file. Edit only that comparison in `src/pages/SecurityAnalysis/__harness__/peersCurrency.harness.cjs` and run it: it must print `PEERS CURRENCY HARNESS: YES (6 of 6 checks)`.

**Fixtures (committed; copy into `src/pages/SecurityAnalysis/__harness__/` only what you need).** Round 111's `peersCurrencyFixture.ICT_PM_overlay.json` and `peersCurrencyFixture.ICT_PM_peers.json`, `peersCurrencyFixture.GOOGL_US_overlay.json` and `peersCurrencyFixture.GOOGL_US_peers.json` are ALREADY in that folder on PROD. Build the synthetic cases in the harness from them (`structuredClone`).

**The grade is on the RENDERED output.** The new harness `src/pages/SecurityAnalysis/__harness__/priceCurrencyRule.harness.cjs` (YOURS: create it; MODEL the Peers render on `peersCurrency.harness.cjs`, which renders `PeersTab` statically with the hooks stubbed, and the header render on whatever static-render approach an existing harness uses for `HeaderCards`; if `HeaderCards` cannot be rendered statically, say so in a row and use the static-source check in R2 alone) checks, each named in the output: R1 the shared helper over four cases: `PX_LAST` with currency `PHP` returns `PHP`; `PX_LAST` with no currency and `CRNCY` value `PHP` returns `PHP`; neither returns `null`; `PX_LAST` currency a blank string and `CRNCY` blank returns `null`; R2 both consumers use the one helper: the source of `HeaderCards.tsx` and of `PeersTab.tsx` each imports it from `../priceCurrency` (or `../../priceCurrency`, as the path resolves) and neither defines a function named `priceCurrencyOf`; R3 on a synthetic ICT PM overlay whose `PX_LAST` carries NO currency and whose `CRNCY` is `PHP`, the rendered Peers table prints every USD figure as `USD ` and no bare `$` (the cell texts read as a reader sees them); R4 the same synthetic overlay rendered through `HeaderCards` prints the USD enterprise-value tile as `USD ` (the header and the table agree); R5 CONTROL: with `PX_LAST` currency `PHP` (the committed overlay) the Peers table renders byte-identically to the render of the committed peers harness (spawn `peersCurrency.harness.cjs` and require `YES (6 of 6 checks)`, which also proves the K5 fix); R6 CONTROL GOOGL US (USD-priced): the table keeps `$`, no `USD ` cell, and the SPCX member Price cell still reads `currency not stated` (W495-S1 unchanged). Print `PRICE CURRENCY RULE HARNESS: YES (<n> of <n> checks)` or `NO` (at least 6 checks, R1 to R6 named; if R4 is impossible say so and name R4 as not run, not passed).

**Do this in order.** (1) `cd C:/dev/wk-resapp-497/portal && git switch -c cand/dell1/amgt-sa-price-currency-rule` (your nested worktree is cut at PROD `932cea99`; confirm `git log -1 --format=%h` reads `932cea99` before and after). (2) Run `node src/pages/SecurityAnalysis/__harness__/peersCurrency.harness.cjs` on the unedited head and record the line (expected `NO (5 of 6 checks)`, K5 failing: the CRLF defect). (3) Create the new harness FIRST and run it ONCE on the unedited head: it must print `NO` with R1 failing (the helper does not exist), R2 failing, R3 failing (the table reads `PX_LAST` only) and R6 passing; record that run. (4) Make the edits (the new helper file, `HeaderCards.tsx`, `PeersTab.tsx`, the K5 comparison). (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~497/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `932cea99`, every path changed since `932cea99`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 932cea99 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-price-currency-rule --purpose "AMGT_RESAPP bs-2: the header tiles and the Peers table read the name's price currency by one rule from one helper" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, ICT PM, header tiles and Peers tab; GOOGL US as the USD-priced control" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W497-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-497/portal`, new branch `cand/dell1/amgt-sa-price-currency-rule` cut from PROD `932cea99`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `components/StatTile.tsx`, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states. Read-only sources outside the portal (`lib/`, `integrations/`) are never written.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/priceCurrency.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~497/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bs-2"><invocation>cd C:/dev/wk-resapp-497/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/priceCurrencyRule.harness.cjs; echo "exit=$?"</invocation><expect>the line `PRICE CURRENCY RULE HARNESS: YES (<n> of <n> checks)` with n at least 6, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bs-2"><invocation>cd C:/dev/wk-resapp-497 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-497/portal" 932cea99 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 29 and T at least 33, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs peersCurrency.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bs-2"><invocation>cd C:/dev/wk-resapp-497/portal &amp;&amp; python "C:/dev/wk-resapp-497/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 932cea99 --head HEAD --receipt "C:/dev/wk-resapp-497/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~497/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~497 <0.9.0_WK_AMGT_RESAPP~497@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~497/AMGT_RESAPP.TO-AMGT-bs-2.one-currency-rule-header-peers.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-497` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-497`.

Report once:
- the branch name, its head commit and the base `932cea99`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-111 analysis (`ledger/ROUND_ANALYSIS.round111.md`, msg 7711) item list, W495-S2 and the CTO's round-111 analysis item 3 (one currency rule for the Peers header and table), plus the K5 CRLF defect the issuer found. One cell, one candidate branch cut from PROD `932cea99`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-112 portal cell. AC2's totals were measured in a provisioned worktree cut at `932cea99` at the cut (28 of 32, four pre-existing names); a new harness adds one file, so T is at least 33 and P at least 29. The grade of each cell is on the RENDERED output. 

<status>complete -- drained by the issuer (2.0.0_SA_COO~R1) 2026-10-17: worker ~497 at 33dad39edb (merged 0a56033117); proof VALID rc=0 on the worker's checker; issuer re-run in a FRESH checkout of the candidate: PRICE CURRENCY RULE HARNESS YES (6 of 6) and PEERS CURRENCY HARNESS YES (6 of 6, the K5 CRLF defect fixed: it failed on the unedited head in the same kind of checkout); diff read: priceCurrency.ts (new, the header's rule), HeaderCards.tsx and PeersTab.tsx import it, six files; candidate cand/dell1/amgt-sa-price-currency-rule head 937f15a01d on PROD 932cea99; at the unedited head the new harness read NO (2 of 6: R1, R2, R3, R5 failing), R4 passed there (the header already applied the rule: a control, not a discriminator); ISSUER RULING on row W497-S2 (the helper returns the header's UNTRIMMED code where the old Peers helper trimmed): kept, as the order said EXACTLY the header's rule and HeaderCards stays byte-identical; a whitespace-padded served currency is an unmeasured edge (no committed fixture carries one), carried to the CTO as a note; rows W497-S1..S3 INERT; approval row dell1-20261017T194202Z-32d8</status>
<round>112</round>
<slot>0.9.0_WK_AMGT_RESAPP~497</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
