# AMGT_RESAPP task order -- `AMGT-bl-1` -- THE SECURITY ANALYSIS MODEL TAB PRINTS A MONEY SYMBOL ONLY FOR THE FIGURE'S OWN CURRENCY, DROPS A PERIOD COLUMN THAT HAS NO VALUES, AND SAYS WHY ON EVERY KEY-FIGURES DASH (ONE PORTAL FEATURE CUT FROM PROD `7d5cb34d`, WITH ITS RECEIPT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~419</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bl-1.the-symbol-follows-the-figures-own-currency-the-empty-period-column-is-gone-and-key-figure-dashes-say-why</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- `r103_feature_surface_check.py --selftest` reads YES (7 arms); the new harness does not exist at PROD `7d5cb34d`, so AC1 reads FAIL there as expected; the worker runs it against the unchanged page before any product edit (step 3) and again after.
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads two committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-419` (branch `wk-AMGT_RESAPP-419`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-419`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bl-1` (round 105, decomposition s.114)

CTO round-104 analysis (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round104.md`, msg 5350): the CVO found two confirmed broken values on the Security Analysis page and one more defect class; this ONE feature fixes all three, page-side only, Opal-internal, cut from PROD `7d5cb34d`.

1. **A currency symbol follows the figure's own currency.** PBR US (a Brazilian company, ADR in USD) prints `$` on its research team's model figures although they are BRL: the team's own sheet carries the Excel number format `_("$"* #,##0_)...` with a literal `$`, and `formatTeamValue` in `src/pages/SecurityAnalysis/modelSheet.ts` prints that literal. `$` must print ONLY when the figure's own currency is USD; a BRL figure prints `BRL ` (use the exported `currencyPrefix` of `components/StatTile.tsx`, the round-104 formatter, which prints `$` for USD and `<code> ` otherwise); a figure with NO known currency prints its number with NO symbol (never a default, never the trading currency). The sheet itself carries no currency: take it from the served model block the same way the page already does for the rows beside it (`figureCurrency`, `rowCurrency`, `FORECAST_MNEMONICS` in `modelSheet.ts`; the model's money figures in `fiscal_year_figures` and `forecast_figures` carry `currency`). For PBR US the served money figures carry BRL (the price `PX_LAST` carries USD, the header `CRNCY` is USD, the trading currency; the reporting currency is BRL). A USD-reporting name keeps `$`.
2. **A column with no values and no header text is never shown.** BATS LN shows a column headed `Period 4` with nothing under it on the Model tab (`team_sheet.periods` is `[]` and the case blocks' `years` row carries 2026..2030 over columns whose cells are empty). Find where the page builds that header, and either show the values (if the served sheet holds them) or drop the empty column and say so in one visible sentence (`The research team's sheet has no values for <the period>, so the column is not shown.`). Never an empty header.
3. **Key Figures dashes carry their reasons,** as the header tiles do since round 104. On the Model tab's Key Figures table (EPS, EBITDA, EBITDA margin, P/E, EV/EBITDA, ROE, debt by year) a `--` cell shows no reason (GOOGL US EBITDA margin 2026E and 2027E; every name). The model block already serves reasons for some (`absentReason`, `cellReasons` on the sheet rows in `modelSheet.ts`; `fiscal_unresolved[].reason`); where none is served, print the same fixed words the header uses (`NOT_SERVED_WORDS` = `Not served for this name`). The reason is visible text next to or under the dash, not a tooltip.

**Do this in order.** (1) `cd C:/dev/wk-resapp-419/portal && git switch -c cand/dell1/amgt-sa-currency-symbol-and-reasons` (from PROD `7d5cb34d`, which your nested worktree is at). (2) Write the harness `src/pages/SecurityAnalysis/__harness__/currencyAndReasons.harness.cjs` FIRST, in the style of `tileMoneyAndReasons.harness.cjs` in the same folder (transpile the page's own files with the installed typescript, render with react-dom/server, stub only the boundaries you do not own, write no file); its fixtures are the two prepared slices of the live `/thesis` bodies, `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round105_prep/fixtures/pbr_model_slice.json` and `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round105_prep/fixtures/bats_model_slice.json` (copy them to `src/pages/SecurityAnalysis/__harness__/currencyFixture.PBR_US_Equity.json` and `...BATS_LN_Equity.json`; each holds `model.team_sheet`, `forecast_figures`, `team_cases`, `fiscal_currency_by_mnemonic`, `header_currency`). It must check at least: C1 PBR US team-sheet money prints with `BRL ` and no `$` anywhere in the model tab's team figures; C2 a USD-reporting synthetic row keeps `$`; C3 a row with no currency prints no symbol; C4 BATS LN renders no column with an empty header and the sentence of item 2 appears once; C5 a Key Figures dash with a served reason shows it, one without shows `Not served for this name`; and print `CURRENCY AND REASONS HARNESS: YES (<n> of <n> checks)` or `NO`. (3) Run it ONCE on the unchanged page: it must print `NO` with the PBR arm (C1) and the BATS arm (C4) failing; record that run. (4) Then make the product edits, only in `src/pages/SecurityAnalysis/`. (5) Run AC1 to AC3. (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~419/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, head commit, base `7d5cb34d`, every changed path), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 7d5cb34d HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis`, names `PBR US`, `BATS LN`, `GOOGL US`). (7) Commit the branch in the nested worktree (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-currency-symbol-and-reasons --purpose "AMGT_RESAPP bl-1: the Security Analysis Model tab prints a money symbol only for the figure's own currency, drops a period column with no values and says why on every key-figures dash" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, PBR US, BATS LN and GOOGL US" --portal portal` and report its output verbatim. Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

If the cause of item 2 or item 3 is in the SERVED block (a value the function should have served), do not hide it with a page patch: file a row naming the field, finish the other two items, and report.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-419/portal`, branch `cand/dell1/amgt-sa-currency-symbol-and-reasons` from PROD `7d5cb34d`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only under `src/pages/SecurityAnalysis/` (the page's own files, its harness folder and its fixtures); never `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only; the research team's prose is never rewritten.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~419/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bl-1"><invocation>cd C:/dev/wk-resapp-419/portal &amp;&amp; node src/pages/SecurityAnalysis/__harness__/currencyAndReasons.harness.cjs; echo "exit=$?"</invocation><expect>the line `CURRENCY AND REASONS HARNESS: YES (<n> of <n> checks)` with n at least 5 and every check named PASS; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bl-1"><invocation>cd C:/dev/wk-resapp-419 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-resapp-419/portal" 7d5cb34d | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` with T equal to U plus one (the new harness); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bl-1"><invocation>cd C:/dev/wk-resapp-419/portal &amp;&amp; python "C:/dev/wk-resapp-419/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 7d5cb34d --head HEAD --receipt "C:/dev/wk-resapp-419/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~419/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~419 <0.9.0_WK_AMGT_RESAPP~419@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~419/AMGT_RESAPP.TO-AMGT-bl-1.the-symbol-follows-the-figures-own-currency-the-empty-period-column-is-gone-and-key-figure-dashes-say-why.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-419`.

Report once:
- the branch name, its head commit and base;
- the harness run at the unchanged page (the NO line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 5350 (round 104 analysis): FWD-40 (a) NOT MET on two confirmed values (PBR US `$` on BRL figures; BATS LN empty `Period 4`) plus the Key Figures dashes. Round 105 cuts items 1 and 3 as one Opal-internal feature approved by the CTO; item 2 rides the same branch (page side: a drop with a stated reason). THE FLOW is `portal/CONTRIBUTING-BOXES.md`: branch `cand/<box>/<slug>` cut from PROD, approval row, merge-forward by `.tools/portal-merge-forward.sh`, promote by LIST by the portal release seat (a DT; bl-2, cut when this lands). Lesson from round 104: the branch is cut from PROD, never from DEV, so the surface check reads YES. The proof-of-spec instance and the worker's commits are in the outer worktree; the approval row is the issuer's.

<status>pending</status>
<round>105</round>
<slot>0.9.0_WK_AMGT_RESAPP~419</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
