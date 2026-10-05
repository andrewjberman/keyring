# DSGN_AMGTV1 task order -- `AV-zm-1` -- WHAT CHANGED READS IN WORDS: EVERY CHANGED LINE HAS A NAME; NO MOVE BETWEEN TWO EQUAL PRINTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zm-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~94</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from fixtures captured on the deployed route.
comp-adversary: RUN by the issuer at the cut on portal 055ba370 -- changed35.cjs 2 of 5 (NAMED FAIL: 32 of 37 rows print no name; ONE NAME PER LINE FAIL: 11 mnemonics share the fixed phrase; NO MOVE BETWEEN EQUAL PRINTS FAIL: 6 equal-print rows print a move, e.g. BEST_DIV_YLD 2026 "0.0%" -> "0.0%" prints "-100.0%"; KEEP and PLANTED pass). It reads 5 of 5 with a scratch reference fix loaded through CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zm-1` (round 35, decomposition v35; serves FWD-25 and FWD-27)

The Model tab's What changed table, `portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx`, has two faults on
today's served Boeing compare (37 changed rows).

1. **32 of 37 changed rows read "a line this page has no name for yet"** (`UNNAMED_CHANGED_LINE`, `:31`).
   - 32 of the 37 rows are consensus forecasts (`scope: "forecast"`, mnemonics `BEST_EPS`, `BEST_SALES`, `BEST_DPS`,
     `BEST_DIV_YLD`, `BEST_CAPEX` and others). The page's maps (`LINE_NAMES`, `HEADER_LABELS`) do not name them.
   - `changedLineWords` (`:103-112`) falls back to the served figure's own `basis.definition`. For a forecast row, though, it never
     finds the figure. The served thesis bundle carries every forecast figure in `model.forecast_figures`, keyed by `mnemonic` and
     `fiscal_year`, each with a `basis.definition` such as "Bloomberg consensus (BEST) estimate of earnings per share for the
     overridden fiscal period.". Header rows are in `header_figures`.
   - Requirements:
     - Every changed line prints a name in words, taken from served data in this order: the served `model.line_names`, the page's
       maps, then the served figure's definition (look the figure up by scope, mnemonic and fiscal year).
     - Two different lines never print the same name in one table.
     - No printed name carries a vendor mnemonic (`BEST_EPS`), "BEST" in capitals, or the vendor's period jargon. "Consensus
       estimate of earnings per share" is the kind of name meant.
     - The fixed phrase stays only as the last resort for a line with no served name at all.
2. **A move is printed between two equal prints.** Where a row's before and after print the same text, for example `0.0%` and
   `0.0%`, the row still prints a change and a percent move such as `-100.0%`.
   - A row whose printed before and printed after are the same text prints no number in its change cell or its percent cell.
     Write a short word such as "unchanged at this precision" or a dash.
   - The full served values stay in the "Full figures" details, as now.
   - Do NOT pass this by printing more digits until no two prints are equal: the fixture has 6 such rows at the row's display
     precision (for example BEST_DIV_YLD 2026 and EQY_BETA "1.36" -> "1.36"), and a fix that removes them reads NOT_EXERCISED,
     which fails.

**Contracts:**
- C-PRESENTATION-ONLY: served values are formatted, never changed, and rounding is display precision. A name is chosen from served
  text; nothing is looked up outside the served bundle and the page's own maps.
- No hard-coded colour outside `lib/chartColors.ts` tokens and the panel ink tokens the file already uses.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each
   file's existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~94/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zm-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round35/checks/changed/changed35.cjs"; echo "exit=$?"</invocation><expect>WHAT CHANGED READS IN WORDS: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zm-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

The KEEP arms inside changed35.cjs run the round-29 What changed checks and the round-34 precision check over the same file, and each
must exit 0. battery29 includes the CI's ESLint step.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~94/DSGN_AMGTV1.TO-AV-zm-1.what-changed-in-words.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W94-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** ROUND34_CLOSE.md section 4 item 2 (@a408efb24a). The close walk of 055ba370 read 33 of 37 changed rows unnamed and
  "-100.0%" on rows printing 0.0% both sides. Fixtures: `round35/fixtures/{compare,thesis,versions}.BA_US_Equity.json`, captured
  read-only on code FcVBPafw at 03:08Z.
- **Not graded here** (the issuer's close walk): how the names read in place on the served compare.

<status>complete</status>
<round>35</round>
<slot>~94</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
