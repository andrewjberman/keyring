# AMGT_RESAPP task order -- `AMGT-bm-1` -- THE SECURITY ANALYSIS MODEL TAB PRINTS THE PRICE BEHIND A HISTORICAL P/E, GIVES EVERY ALL-FIGURES TEAM-GRID DASH ITS REASON AND SHOWS A WITHHELD FORWARD P/E'S SERVED REASON (ONE PORTAL FEATURE CUT FROM PROD `7db035e4`, WITH ITS RECEIPT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bm-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~441</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bm-1.the-historical-pe-prints-its-price-basis-and-every-team-grid-dash-and-withheld-forward-pe-says-why</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- the harness `src/pages/SecurityAnalysis/__harness__/basisAndReasons.harness.cjs` does not exist at PROD `7db035e4`, so AC1 reads FAIL there as expected (node exits 1, read here); the worker runs it against the unchanged page before any product edit (step 3). `r103_feature_surface_check.py --selftest` reads YES (7 arms).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-441` (branch `wk-AMGT_RESAPP-441`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-441`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bm-1` (round 106, decomposition s.115)

CTO round-105 analysis (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round105.md`, msg 5426, section 2): three rows are carried as remediation. This ONE portal feature (Security Analysis, Opal-internal, cut from PROD `7db035e4`) fixes the page side of all three. Page-side only: no served value moves, the research team's prose is never rewritten.

1. **The historical P/E prints its price basis.** On the Model tab's Key Figures table a historical P/E (a column of a fiscal year, e.g. GOOGL US 2025 `28.7x`) is the served row `PE_RATIO` of that year, whose `basis.derived_from` is `[PX_LAST, IS_EPS]` (price / reported EPS of the SAME fiscal year since round 104). The page prints `28.7x` and nothing says which price: the header price `$351.66` over EPS 10.91 is 32.2x, so a reader cannot recompute it. Under that P/E cell print one small visible line naming the price it used: `price <value> <currency> at the close of fiscal year <YYYY>` (GOOGL US 2025: `price 313.00 USD at the close of fiscal year 2025`), taking the value and currency from the served `PX_LAST` row of the SAME fiscal year in `fiscal_year_figures` (`value`, `currency`). The served figures carry NO date for that price (`period_end_date` and `fiscal_period_end` are null), so print a date ONLY when one of them is served non-null (then `... at the close of <date>`). A P/E cell with no `derived_from` (a stored Bloomberg P/E; a model cell) or whose same-year `PX_LAST` is absent prints no basis line. Use the existing money formatter (`currencyPrefix` in `components/StatTile.tsx`: `$` only for USD, `<code> ` otherwise). The fixture is `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/googl_model_slice.json` (the live GOOGL US model block: `fiscal_year_figures` of PX_LAST, IS_EPS and PE_RATIO for 2024 and 2025, `forecast_figures`, `fiscal_unresolved`).
2. **A team-row dash on the Model tab's All-figures grid states its reason**, as the Key Figures dashes do since round 105 (same component, same idiom: visible text in or under the dash, never a tooltip). The All-figures grid is the table under the `All figures` disclosure on the Model tab (the research team's own sheet rows beside the served figures, built in `src/pages/SecurityAnalysis/modelSheet.ts` and rendered in `tabs/ModelTab.tsx`). Where the model block serves a reason for the cell (`cellReasons`, `absentReason` on the sheet row), print it; where none is served, print the fixed words `The research team's sheet has no value for this cell.` A cell that holds a value prints it as today.
3. **A withheld forward P/E shows its served reason.** The served change `AMGT-bm-2` (a separate cell, applied later) adds `model.forecast_withheld: [{mnemonic: "BEST_PE_RATIO", fiscal_year, fiscal_period, reason}]` for each forward P/E it withholds (the reason reads like `the price is in USD and consensus EPS in BRL, and a ratio of different currencies is not shown`). On the Key Figures table's P/E row, a forecast-year cell (`2026E`, `2027E`) with no value whose `(BEST_PE_RATIO, fiscal_year)` has such an entry shows THAT reason in place of the generic `No consensus estimate is served for this line`. A response with no `forecast_withheld` key (every response until the apply) behaves exactly as today. Add the optional field to the type in `types.ts`. There is no live example yet: build the harness's fixture BY SPEC from the GOOGL US slice (`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/googl_model_slice.json`): remove its `BEST_PE_RATIO` rows from `forecast_figures` and add two `forecast_withheld` entries for 2026 and 2027 with the reason above (GOOGL US has no research-team sheet in the slice, so the forecast P/E cells are dashes). CORRECTED by the issuer at the amendment (the first reading used the PBR US slice and the worker's row `AMGT_RESAPP-D1-W441-S1` showed why that cannot work): PBR US HAS a research-team sheet with its own P/E line (`5.9x`, `6.1x` for 2026E and 2027E), and the page fills a forecast cell from the team's own value when the consensus row is absent, so on PBR US a withheld consensus P/E shows the TEAM's value, not a dash: that is correct and stays (the team's value carries the team's own label). The reason is shown only where a dash would otherwise appear (a name without a team P/E line).

**RE-SEAT NOTE (second pass).** The first pass is committed: portal `9a1adc6e35` on `cand/dell1/amgt-sa-pe-basis-and-reasons` (items 1 and 2 pass their harness checks; B5 and B6 failed only on the wrong fixture) and outer `d7bdcd1172`. Do NOT redo items 1 and 2. Your remaining work: switch the harness's B5 and B6 to the GOOGL fixture as item 3 now says (keep every other check), re-run AC1 to AC3, a second portal commit on the same branch, the receipt's `## What the branch carries` updated, the instance re-recorded and re-checked, the `--check-only` output again, and one more row only if something new surfaces. Row W441-S1's premise was the order's (corrected here); S2 and S3 are accepted as filed.

**Do this in order.** (1) `cd C:/dev/wk-resapp-441/portal && git switch -c cand/dell1/amgt-sa-pe-basis-and-reasons` (from PROD `7db035e4`, which your nested worktree is at). (2) Write the harness `src/pages/SecurityAnalysis/__harness__/basisAndReasons.harness.cjs` FIRST, in the style of `currencyAndReasons.harness.cjs` and `tileMoneyAndReasons.harness.cjs` in the same folder (transpile the page's own files with the installed typescript, render with react-dom/server, stub only the boundaries you do not own, write no file); fixtures go in the same folder as `basisFixture.GOOGL_US_Equity.json` (a copy of the GOOGL slice) and `basisFixture.PBR_US_Equity.json` (a copy of `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round105_prep/fixtures/pbr_model_slice.json`). It must check at least: B1 GOOGL US 2025 P/E prints the basis line with `313.00`, `USD` and `fiscal year 2025`; B2 a P/E cell with no `derived_from` prints no basis line; B3 a currency other than USD prints its code in the basis line (synthetic row); B4 an All-figures team-grid dash with a served reason shows it, one without shows the fixed words; B5 a forecast P/E cell with a `forecast_withheld` entry shows that reason; B6 the same cell with no `forecast_withheld` key shows `No consensus estimate is served for this line`; B7 the saved values are unchanged. Print `BASIS AND REASONS HARNESS: YES (<n> of <n> checks)` or `NO`. (3) Run it ONCE on the unchanged page: it must print `NO` with B1, B4 and B5 failing; record that run. (4) Then make the product edits, only in `src/pages/SecurityAnalysis/`. (5) Run AC1 to AC3. (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~441/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, head commit, base `7db035e4`, every changed path), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 7db035e4 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis`, names `GOOGL US`, `PBR US`, `ISP IM`). (7) Commit the branch in the nested worktree (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-pe-basis-and-reasons --purpose "AMGT_RESAPP bm-1: the Security Analysis Model tab prints the price behind a historical P/E, gives every All-figures team-grid dash its reason and shows a withheld forward P/E's reason" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, GOOGL US, PBR US and ISP IM" --portal portal` and report its output verbatim. Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

If a premise of this order does not reproduce on the fixtures (a cell, a field, a component named here is not where the order says), do not guess and do not patch around it: file a BLOCKING row naming exactly what you found, finish the other items, and report.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-441/portal`, branch `cand/dell1/amgt-sa-pe-basis-and-reasons` from PROD `7db035e4`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only under `src/pages/SecurityAnalysis/` (the page's own files, its harness folder and its fixtures); never `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~441/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bm-1"><invocation>cd C:/dev/wk-resapp-441/portal &amp;&amp; node src/pages/SecurityAnalysis/__harness__/basisAndReasons.harness.cjs; echo "exit=$?"</invocation><expect>the line `BASIS AND REASONS HARNESS: YES (<n> of <n> checks)` with n at least 7 and every check named PASS; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bm-1"><invocation>cd C:/dev/wk-resapp-441 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-resapp-441/portal" 7db035e4 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` with T equal to U plus one (the new harness); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bm-1"><invocation>cd C:/dev/wk-resapp-441/portal &amp;&amp; python "C:/dev/wk-resapp-441/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 7db035e4 --head HEAD --receipt "C:/dev/wk-resapp-441/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~441/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~441 <0.9.0_WK_AMGT_RESAPP~441@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~441/AMGT_RESAPP.TO-AMGT-bm-1.the-historical-pe-prints-its-price-basis-and-every-team-grid-dash-and-withheld-forward-pe-says-why.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-441`.

Report once:
- the branch name, its head commit and base;
- the harness run at the unchanged page (the NO line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 5426 (round 105 analysis, section 2): W418-S3 (the historical P/E's price basis), W419-S3 (the All-figures grid's team-row dashes) land as one Opal-internal feature approved by the CTO; this feature also carries the page side of W418-S2 (item 3) so the page can land before the served change. Lessons carried: the branch is cut from PROD, never from DEV; the order names the component after a measured look at the served body, not a guess (round 105's first pass named the wrong tab); the worker files a BLOCKING row rather than patching around a premise that does not hold.

<status>pending</status>
<round>106</round>
<slot>0.9.0_WK_AMGT_RESAPP~441</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
