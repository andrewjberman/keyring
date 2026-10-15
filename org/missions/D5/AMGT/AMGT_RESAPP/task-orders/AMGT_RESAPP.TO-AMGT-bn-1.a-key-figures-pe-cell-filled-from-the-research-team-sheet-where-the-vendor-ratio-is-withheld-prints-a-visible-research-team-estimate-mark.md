# AMGT_RESAPP task order -- `AMGT-bn-1` -- A SECURITY ANALYSIS KEY FIGURES P/E CELL THAT THE PAGE FILLS FROM THE RESEARCH TEAM'S SHEET, WHERE THE VENDOR RATIO IS WITHHELD, PRINTS A VISIBLE `research team estimate` MARK (ONE PORTAL FEATURE CUT FROM PROD `e0b43076`, WITH ITS RECEIPT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bn-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~471</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bn-1.a-key-figures-pe-cell-filled-from-the-research-team-sheet-where-the-vendor-ratio-is-withheld-prints-a-visible-research-team-estimate-mark</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- the harness `src/pages/SecurityAnalysis/__harness__/teamEstimateMark.harness.cjs` does not exist at PROD `e0b43076`, so AC1 reads FAIL there as expected (node exits 1, read here); the worker runs it against the unchanged page before any product edit (step 3). `r103_feature_surface_check.py --selftest` reads YES (7 arms).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-471` (branch `wk-AMGT_RESAPP-471`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-471`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bn-1` (round 107, decomposition s.116)

The CTO ruled (round-106 analysis, `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round106.md`, section 1): on a Security Analysis Model tab's Key Figures P/E row, where the served block WITHHOLDS a vendor ratio and the page fills the cell from the research team's own sheet, that team value stays and prints with a visible source mark. The withheld ratio's reason prints only where no team value exists (it does already); the vendor figure never prints once withheld (it does not). This ONE portal feature (Security Analysis, Opal-internal, cut from PROD `e0b43076`) adds the mark. Page side only: no served value moves, no team figure is changed, no reason sentence is changed.

**What the page does today (read at PROD `e0b43076`).** `src/pages/SecurityAnalysis/tabs/ModelTab.tsx`, the Key Figures table (`<section data-model-summary>`), renders each year cell through `SheetCellView`. When the model block has no value for a (P/E, year) the sheet builder (`modelSheet.ts`, `summarizeSheet`) takes the research team's own `P/E` line, and the cell is a TEAM cell (`isTeamCell(figure)`, rendered by `TeamModelCell`: `<td data-model-source="team">`, the cite only in a `title` tooltip). So on SHOP CN the cells read 2025 `74x-193.1x` (a team text range), 2026E `67.8x`, 2027E `53.0x`, and nothing on the page says they are the team's. The served block says why the vendor ratio is absent: `model.forecast_withheld` (entries `{mnemonic: "BEST_PE_RATIO", fiscal_year, fiscal_period, reason}`; the helper `withheldPeReason(data, year)` reads it) for forecast columns, and `model.fiscal_unresolved` (entries `{mnemonic: "PE_RATIO", fiscal_year, reason}`) for historical columns.

**The change.**
1. In the Key Figures table, a P/E cell that is a TEAM cell AND whose vendor ratio is WITHHELD prints, beneath the figure, ONE small visible line with the exact words `research team estimate`. WITHHELD means: forecast column (`2026E`, `2027E`, ...): `model.forecast_withheld` holds an entry with mnemonic `BEST_PE_RATIO` whose fiscal year equals the column's; historical column (`2025`): `model.fiscal_unresolved` holds an entry with mnemonic `PE_RATIO` whose fiscal year equals the column's. Both team numbers and team TEXT cells (the range `74x-193.1x`) take the mark.
2. Nothing else is marked: a vendor cell (a `ModelCell`), a team cell on another row, a team P/E cell in a column with no withhold entry, and any dash are exactly as today.
3. The mark is visible text in the cell, never only a tooltip and never only a colour: build it as the existing basis line is built (`ModelCell`'s `basisLine`: `<span data-model-basis="" className="block text-[11px] font-normal ${INK_MUTED}">`), with its own attribute `data-model-team-mark=""`. The cell's `title` cite and `data-model-source="team"` stay.

**Fixtures (copy them into `src/pages/SecurityAnalysis/__harness__/`; all three are committed in this repository).**
- `teamMarkFixture.SHOP_CN_Equity.json`: a copy of `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/fixtures/shop_model_slice.json` (the live SHOP CN body's model slice, read 2026-10-15; its `forecast_withheld` names 2026, 2027 and 2028, its `fiscal_unresolved` names `PE_RATIO` for 2020 to 2025, its team sheet row 24 `P/E` reads `74x-193.1x`, 67.77, 53.03).
- `teamMarkFixture.PBR_US_Equity.json`: a copy of `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/fixtures/pbr_model_slice_live.json` -- the LIVE PBR US body read after round 106's served withhold, committed unedited: it carries NO vendor `BEST_PE_RATIO` forecast row, `model.forecast_withheld` entries for 2026, 2027 and 2028 (reason `the price is in USD and consensus EPS in BRL, and a ratio of different currencies is not shown`), and the team sheet's `P/E` row 5.95 and 6.15 for 2026 and 2027. Do NOT hand-edit it. (AMENDMENT 1 replaces the first pass's fixture, which was the round-105 slice plus two hand-added entries and still served vendor rows: W471-S1.)
- `teamMarkFixture.GOOGL_US_Equity.json`: a copy of `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106_prep/googl_model_slice.json` (a vendor P/E, no withhold).

**RE-SEAT NOTE (AMENDMENT 1, issuer, 2026-10-15 ~22:1xZ).** Your first pass is committed and is INHERITED STATE: portal `844d72eb` on `cand/dell1/amgt-sa-team-estimate-mark` and outer `f4d2a7a6f8`, `f96e98e32f`. Do NOT redo the product edit unless a check below demands it. Two of your rows are the ORDER'S defects and are RULED, not to be filed again: `W471-S1` (the fixture: the first pass's PBR fixture still served vendor forward P/E rows, so a team cell could not stand in 2026E and 2027E; the fixture is now the live post-withhold body, see Fixtures) and `W471-S4` (AC2 demanded repo-wide `lint rc 0` while PROD itself reads repo-wide lint rc 1 on `TicketCenter/filing-hint.test.tsx`; AC2 now runs `r107_feature_green_v3.sh`, which grades lint on `src/pages/SecurityAnalysis`). `W471-S2` and `W471-S3` are accepted as filed. Your remaining work: (a) replace the PBR fixture with the live copy, (b) re-run the harness (T3a, T3b and T5 are expected to pass now; if one still fails, file ONE row naming what you read), (c) re-run AC1 to AC3, (d) update the receipt and the instance (re-record `expect` against the new outputs, re-check VALID), (e) re-run the `--check-only` and report it verbatim, (f) a second portal commit on the same branch, never an amend.

**Do this in order.** (1) `cd C:/dev/wk-resapp-471/portal && git switch -c cand/dell1/amgt-sa-team-estimate-mark` (a re-seat: the branch exists, so `git switch cand/dell1/amgt-sa-team-estimate-mark`; the steps that are already done above stay done) (from PROD `e0b43076`, which your nested worktree is at). (2) Write the harness `src/pages/SecurityAnalysis/__harness__/teamEstimateMark.harness.cjs` FIRST, in the style of `basisAndReasons.harness.cjs` in the same folder (transpile the page's own files with the installed typescript, render with react-dom/server, stub only the boundaries you do not own, write no file). It must check at least: T1 SHOP CN 2026E and 2027E (`67.8x`, `53.0x`) each print `research team estimate` inside their own cell; T2 SHOP CN 2025 (the text range `74x-193.1x`) prints it; T3 PBR US 2026E (`5.9x`) and 2027E (`6.1x`) print it; T4 a vendor P/E cell (GOOGL US) prints none; T5 a team P/E cell in a column with no withhold entry (the PBR US fixture with its `forecast_withheld` entries removed; the vendor rows are already absent from it) prints none; T6 a P/E cell with no value and no team value shows its reason words and no mark; T7 the mark is rendered text, not only a `title`; T8 the team cell's `data-model-source="team"` and its title cite are unchanged. Print `TEAM ESTIMATE MARK HARNESS: YES (<n> of <n> checks)` or `NO`. If a premise above does not reproduce on a fixture (a field or a cell is not where this order says), file a BLOCKING row naming exactly what you found, finish what you can, and report; do not patch around it. (3) Run it ONCE on the unchanged page: it must print `NO` with T1, T2 and T3 failing; record that run. (4) Then make the product edits, only in `src/pages/SecurityAnalysis/`. (5) Run AC1 to AC3. (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~471/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, head commit, base `e0b43076`, every changed path), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff e0b43076 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis`, names `SHOP CN`, `PBR US`, `GOOGL US`). (7) Commit the branch in the nested worktree (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-team-estimate-mark --purpose "AMGT_RESAPP bn-1: a Security Analysis Key Figures P/E cell filled from the research team's sheet, where the vendor ratio is withheld, prints a visible research team estimate mark" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, SHOP CN, PBR US and GOOGL US" --portal portal` and report its output verbatim. Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-471/portal`, branch `cand/dell1/amgt-sa-team-estimate-mark` from PROD `e0b43076`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only under `src/pages/SecurityAnalysis/` (the page's own files, its harness folder and its fixtures); never `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~471/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bn-1"><invocation>cd C:/dev/wk-resapp-471/portal &amp;&amp; node src/pages/SecurityAnalysis/__harness__/teamEstimateMark.harness.cjs; echo "exit=$?"</invocation><expect>the line `TEAM ESTIMATE MARK HARNESS: YES (<n> of <n> checks)` with n at least 8 and every check named PASS; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bn-1"><invocation>cd C:/dev/wk-resapp-471 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-471/portal" e0b43076 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` with T equal to U plus one (the new harness) and `lint rc 0` read on `src/pages/SecurityAnalysis` (the script's first line also prints the repo-wide lint rc as information: PROD itself reads it non-zero in a TicketCenter test file this feature does not touch); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bn-1"><invocation>cd C:/dev/wk-resapp-471/portal &amp;&amp; python "C:/dev/wk-resapp-471/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base e0b43076 --head HEAD --receipt "C:/dev/wk-resapp-471/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~471/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~471 <0.9.0_WK_AMGT_RESAPP~471@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~471/AMGT_RESAPP.TO-AMGT-bn-1.a-key-figures-pe-cell-filled-from-the-research-team-sheet-where-the-vendor-ratio-is-withheld-prints-a-visible-research-team-estimate-mark.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-471`.

Report once:
- the branch name, its head commit and base;
- the harness run at the unchanged page (the NO line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 6249 (round-106 analysis @08a12d383e, sections 1 and 2 item 1): `D1-S32` ruled, a team figure stands where a withheld vendor ratio's reason would print, with a visible source mark; the mark is round 107's cell. Lessons carried from round 106: the branch is cut from PROD, never from DEV; the order names the component after a measured look at the served body and the page code (this order read the live SHOP CN body and `ModelTab.tsx` at `e0b43076`); the worker files a BLOCKING row rather than patching around a premise that does not hold (round 106's `W441-S1` was exactly this premise on the PBR fixture, never ruled until D1-S32). The words `research team estimate` are the issuer's choice inside the CTO's "(team estimate)". AC5-style judgment: none on this order; the CTO re-grades bm-5 AC5 change 3 at the walk `AMGT-bn-4`.

<status>pending</status>
<round>107</round>
<slot>0.9.0_WK_AMGT_RESAPP~471</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
