# AMGT_RESAPP task order -- `AMGT-bs-1` -- THE P/E FOOTER IS PROVEN TO PRINT IN PLAIN WORDS EVERY REASON THE STORED MODEL-BLOCK PRODUCER CAN EMIT: THE PRODUCER READ AT SOURCE, EVERY TOKEN LISTED, THE MAP EXTENDED WHERE A TOKEN IS NOT COVERED (A NEW CANDIDATE FROM PROD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bs-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~496</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bs-1.pe-footer-census-at-source</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- commits on a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1 at the base: the harness file does not exist, so it FAILS (exit 1); AC2 run in a provisioned worktree cut at `932cea99` reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 28 of 32 pass, base 25 of 32, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs peersCurrency.harness.cjs timelineFourStates.harness.cjs)`, so AC2 is a REGRESSION guard here (it PASSES at the base as expected; `peersCurrency.harness.cjs` is pre-existing there because of the CRLF checkout defect named in the order of `AMGT-bs-2`); AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs the new harness against the unedited head before any product edit (step 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP; the source read of `integrations/bloomberg/research/` is a file read only.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-496` (branch `wk-AMGT_RESAPP-496`, cut from the issuance commit; its nested portal worktree `C:/dev/wk-resapp-496/portal` is cut at PROD `932cea99`). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-496`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bs-1` (round 112, decomposition s.121)

Round 111's `AMGT-br-3` made the Key Figures `P/E not shown` footer print plain words through `plainPeReason` in `src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (a closed table `IS_EPS` -> `reported earnings per share`, `PX_LAST` -> `share price`, `reported EPS` spelled out, and a safety net that turns any other vendor-mnemonic-shaped token into `a vendor figure`). Its census had ONE gap (row `AMGT_RESAPP-D1-W494-S1`): the footer also prints the reason of a STORED model-block `unresolved` row (served as `fiscal_unresolved`, `lib/research/api/scoped_amgt.py` lines ~5803-5807 pass the stored rows through; the footer reads the one whose `mnemonic` is `PE_RATIO`, `fiscalPeReason`), and the PRODUCER of those stored rows was not read at source. This cell reads it, lists every token it can emit, and proves the footer prints each in plain words.

**The producer (read it first).** `integrations/bloomberg/research/model_block_pull.py`: the model block's `unresolved` list is built at the sites that read `unresolved.append(` (around lines 1390, 1403, 1421, 1542, 1674, 1712, 1723, 1753) with a `reason` that is a literal, an f-string, a named constant (for example `FORECAST_NOT_ANNUAL_REASON`, `_FY_NOT_CLOSED_REASON`) or a variable (`reason`, `gap["fallback_status"]`); the block is returned with `"unresolved": unresolved` (~line 1792). Read the WHOLE function around each site and every constant it names; resolve each variable's possible values by reading where it is assigned. This is a source read: no Bloomberg call, no pull, nothing leaves this machine. The served side, `lib/research/api/scoped_amgt.py` (the `fiscal_unresolved` passthrough and the `forecast_withheld` / `pe_withheld` builders around lines 2728-2806 and 5760-5816), is YOUR SECOND SOURCE; the portal readers are `fiscalPeReason` and `components/model/withheldPeReason.ts`.

**The census (a deliverable, in the receipt under `## Producer census`, and as a committed fixture `src/pages/SecurityAnalysis/__harness__/peFooterCensus.fixture.json`).** One entry per reason the producer can emit, each with: `site` (`file:line`), `scope` (the row's `scope` value), `mnemonic` (the row's `mnemonic` value or `null`), `reason_template` (the literal text, with `{x}` for each interpolated part), `reaches_footer` (`yes` only if a row with `mnemonic` `PE_RATIO` and a fiscal year can carry it, or it is an estimate-year `BEST_PE_RATIO` reason the footer prints; otherwise `no` with the one-line why), and `tokens` (every vendor-mnemonic-shaped token in the text, matching `/\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b/`, listed; `[]` if none). Print the denominator: the number of `unresolved.append(` sites read and the number of entries. If a reason is built from a variable you cannot resolve at source, say so in that entry (`unresolved_at_source: true`, why) rather than guessing.

**The change.** If every token found on a `reaches_footer: yes` entry is already named in the `plainPeReason` table or caught by its safety net, change NOTHING in `ModelTab.tsx` and say so. If a token (or a phrase such as a bare field word) would print as `a vendor figure` where a plain word is the right reading, add it to the closed table in `ModelTab.tsx` with its plain words, as the existing two are, and report it. Never reword a number, a year or a currency code; display only.

**The grade is on the RENDERED footer.** The new harness `src/pages/SecurityAnalysis/__harness__/peFooterCensus.harness.cjs` (YOURS: create it; MODEL it on the existing `peFooterWords.harness.cjs`, which renders the Key Figures footer for synthetic served bundles, and read `withheldReasons.harness.cjs`; do not edit either) reads `peFooterCensus.fixture.json`, and for EVERY entry with `reaches_footer: yes` builds a served bundle whose `fiscal_unresolved` (or `forecast_withheld` for an estimate-year entry) carries that reason (each `{x}` filled with a realistic value) and renders the footer to static markup, and checks, each named in the output: C1 the fixture holds at least one entry per `unresolved.append(` site you read, and the printed denominator equals the number of entries; C2 for every `reaches_footer: yes` entry the RENDERED footer text contains NO token matching `/[A-Z][A-Z0-9]*_[A-Z0-9_]+/`; C3 for every such entry, the rendered text keeps every number, year and currency code of the reason (compare the digit and code sequences before and after); C4 every token listed in the fixture on a `reaches_footer: yes` entry is either in the table (prints its plain words) or is reported as safety-net-only in the receipt (name each); C5 CONTROL: the two br-3 variants (`price / reported EPS (IS_EPS), FY2025, is not shown: the price is in GBp and reported EPS in USD, and a ratio of different currencies is not shown` and the absent-input one) render exactly as `peFooterWords.harness.cjs` expects (spawn it and require its `YES (7 of 7 checks)` line). Print `PE FOOTER CENSUS HARNESS: YES (<n> of <n> checks)` or `NO` (at least 5 checks, C1 to C5 named).

**Do this in order.** (1) `cd C:/dev/wk-resapp-496/portal && git switch -c cand/dell1/amgt-sa-pe-footer-census` (your nested worktree is cut at PROD `932cea99`; confirm `git log -1 --format=%h` reads `932cea99` before and after). (2) Read the producer and the served side; write the census fixture. (3) Create the harness and run it ONCE on the unedited head: it prints `NO` only where the head really fails a check (a token the table does not name prints `a vendor figure` and C4 reports it); record that run honestly, whether it prints YES or NO (this cell does not promise a failing base: say which). (4) Make the product edit only if C4 found a token the table should name (`ModelTab.tsx` alone). (5) Run AC1 to AC3. Steps (6) to (8) follow.

**Common steps (6) to (8).** (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~496/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, the new head commit, base `932cea99`, every path changed since `932cea99`), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 932cea99 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis` and the names this cell names), and a `## Producer census` section (every `unresolved.append(` site read with file:line, the denominator, every entry's tokens, every token that is safety-net-only). (7) Commit in the nested worktree on the new branch (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push; never rebase or amend any commit. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-pe-footer-census --purpose "AMGT_RESAPP bs-1: the P/E not shown footer is proven plain for every reason the stored model-block producer can emit" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, RIO LN and ICT PM, Model tab, Key Figures footer" --portal portal` and report its output verbatim (a refusal naming a branch-history or overlap reason is a finding to report, not to work around). Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W496-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-496/portal`, new branch `cand/dell1/amgt-sa-pe-footer-census` cut from PROD `932cea99`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; never rewrite an existing commit; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only in the files this cell names and new or named harness files under `src/pages/SecurityAnalysis/__harness__/`; never `components/StatTile.tsx`, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence beyond what this cell states. Read-only sources outside the portal (`lib/`, `integrations/`) are never written.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~496/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bs-1"><invocation>cd C:/dev/wk-resapp-496/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/peFooterCensus.harness.cjs; echo "exit=$?"</invocation><expect>the line `PE FOOTER CENSUS HARNESS: YES (<n> of <n> checks)` with n at least 5, every check of the cell's list named PASS (a check the order allows to be `not run` is named as such), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bs-1"><invocation>cd C:/dev/wk-resapp-496 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-496/portal" 932cea99 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness <P> of <T> pass, base <Q> of <U>, regressions 0, pre-existing: <names>)` with P at least 29 and T at least 33, every `<names>` entry among `assembled.harness.cjs exportCompare.harness.cjs peersCurrency.harness.cjs timelineFourStates.harness.cjs`, and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bs-1"><invocation>cd C:/dev/wk-resapp-496/portal &amp;&amp; python "C:/dev/wk-resapp-496/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 932cea99 --head HEAD --receipt "C:/dev/wk-resapp-496/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~496/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~496 <0.9.0_WK_AMGT_RESAPP~496@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~496/AMGT_RESAPP.TO-AMGT-bs-1.pe-footer-census-at-source.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-496` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-496`.

Report once:
- the branch name, its head commit and the base `932cea99`;
- the harness run at the unedited head (the line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-111 analysis (`ledger/ROUND_ANALYSIS.round111.md`, msg 7711) item list, W494-S1 and the CTO's round-111 analysis item 2 (the producer of the stored model-block rows read at source). One cell, one candidate branch cut from PROD `932cea99`, one approval row (opal-internal, Security Analysis; the CTO approves). Disjoint write surface from the other round-112 portal cell. AC2's totals were measured in a provisioned worktree cut at `932cea99` at the cut (28 of 32, four pre-existing names); a new harness adds one file, so T is at least 33 and P at least 29. The grade of each cell is on the RENDERED output. The worktree is provisioned with `--sparse-add integrations/bloomberg/research` so the producer source is on disk (a read of source, not a Bloomberg call).

<status>complete -- drained by the issuer (2.0.0_SA_COO~R1) 2026-10-17: worker ~496 at 3d1fccf474 (merged c6a2c69697); proof VALID rc=0 on the worker's checker; issuer re-run of the harness in a FRESH checkout of the candidate: PE FOOTER CENSUS HARNESS YES (5 of 5), 8 of 8 unresolved.append( sites covered, 25 entries (19 producer, 6 served), 8 reach the footer, distinct tokens on them IS_EPS and PX_LAST only, both in the table, none safety-net-only; NO product change (ModelTab.tsx unchanged): the candidate cand/dell1/amgt-sa-pe-footer-census head 618a39dd5f carries the census fixture and harness only; the base run printed NO once (the worker's own fixture transcription, corrected) and the order promised no failing base; rows W496-S1..S2 INERT (the producer's forecast-scope reasons route to forecast_reason, which the footer never reads); approval row dell1-20261017T193744Z-48c7</status>
<round>112</round>
<slot>0.9.0_WK_AMGT_RESAPP~496</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
