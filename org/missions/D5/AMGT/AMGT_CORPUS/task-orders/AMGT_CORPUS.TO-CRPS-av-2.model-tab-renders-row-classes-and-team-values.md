# AMGT_CORPUS task order -- `CRPS-av-2` -- ROUND 46: the Model tab honours the row class and shows the team's own values, Bloomberg first (FWD-12 / FWD-20, portal half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-av-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- portal source only; no AWS call.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV 00989b8b -- av2_check.cjs: `av2 build 0/5 control 2/2` at the base, `build 5/5 control 2/2` on a throwaway reference patch (not shipped). Blind spot: pure-function level; the rendered census over every served name is the issuer's read (CRPS-av-10), after the API serves the new fields.
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's review of the candidate.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 46.
**Your portal.** The nested `portal/` directory in your worktree is a portal git worktree on branch `wk-AMGT_CORPUS-46-2-portal`, based on
portal origin/DEV. Portal files commit INSIDE `portal/` on that branch; the outer commit holds only the outer files. Never commit the
portal gitlink. NEVER run `bun install`. **Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas; reuse the file's classes.

## 1. THE CELL -- `CRPS-av-2`

Outcome FWD-12 and FWD-20 (PRD lines 433-456 and 593-606, read them). Today, with a served team sheet,
`portal/src/pages/SecurityAnalysis/modelSheet.ts` `buildModelSheet` (the 7th argument `teamSheet`, about line 377 and the block from
about :487) renders EVERY team label as a row, and a label that matches no row spec shows "no figure is pulled yet". Measured on the live
page: 3210 of 9233 rendered rows read that way, many of them the sheet's own header rows and control tokens. A parallel cell
(`CRPS-av-1`) makes the API serve, per name, a row class and the team's own period values. This cell renders them.

**The served shape** (`data.model.team_sheet`, the 7th argument; every round-44 key stays: `class`, `workbook_key`, `sheet`, `rows`,
`model_rows_beside`, `reason`). It gains, all aligned with `rows`:

```
row_classes   ["FIGURE" | "HEADING" | "CONTROL", ...]
row_numbers   [<1-based sheet row>, ...]
row_values    [null | [<cell as the workbook saved it> per period, ...], ...]   (non-null only for a FIGURE row)
periods       [{"label": "2016", "column": "E"}, ...]                            (the period header; [] when none)
```

A cell is a number, a text such as `#VALUE!`, or null. A payload captured before this cell carries none of the new keys.

**Build:**

1. `types.ts`: add the four optional fields to the `team_sheet` type (about line 1139), so an old payload still type-checks.
2. `modelSheet.ts`, `buildModelSheet`: when `teamSheet.row_classes` is present and as long as `teamSheet.rows`, build the FIRST group
   (the team rows) from the sheet's rows IN ORDER, by class:
   - **CONTROL:** not a row. It is counted only.
   - **HEADING:** a row with `rowKind: 'heading'`, no figure cell (every cell null), no `absentReason`. It is neither absent nor unmapped.
   - **FIGURE, precedence 1, Bloomberg:** the label matches a row spec's label (case and whitespace insensitive, as the existing
     match does) AND that row carries at least one served figure: the row is that spec's row with the team's label, plus
     `source: 'bloomberg'`. Bloomberg wins even when the team's own values exist.
   - **FIGURE, precedence 2, the team's own value:** otherwise, when `row_values[i]` holds a finite number for at least one sheet year, the
     row's cells are the team's values VERBATIM, one per sheet year: a period label `YYYY` fills the sheet year `'YYYY'` AND the forecast
     column `'YYYYE'`; a year with no numeric value is null. Each cell is `{mnemonic: null, fiscal_year: <the year as a number>, value:
     <the saved value>, unit: null}`. The row carries `type: 'other'`, `source: 'team'`, `sourceLabel: 'team model'` and `teamCite:
     {workbook: <the file name after the last "/" of workbook_key>, sheet: <teamSheet.sheet>, row: <row_numbers[i]>, label: <the label>}`.
     Never rounded, never re-derived, no label-to-field map.
   - **FIGURE, precedence 3, a why in words:** otherwise the row has no cells (all null), `source: 'why'` and an `absentReason` a PM
     reads: when a period cell is a text (for example `#VALUE!`), a sentence naming that text ("The research team's own sheet shows an
     error (\"#VALUE!\") for this line, so no value is shown."); else "The research team's sheet holds no value for this line in the years
     shown." Never "ABSENT", "REFUSED --" or "not read", and no vendor mnemonic in the words.
   - Every OTHER group the base builds without a team sheet stays BELOW the team rows, unchanged and in order (the hard-coded Financial
     Summary group, which the team rows replace, is the only one dropped). The forecast years (2026E-2028E) survive.
   - `ModelSheet` gains `teamCensus: {classes: {FIGURE, HEADING, CONTROL}, bySource: {bloomberg, team, why}, unmapped: 0}`:
     the class counts over the sheet's rows (they sum to `rows.length`), the FIGURE rows by source (they sum to `classes.FIGURE`), and
     `unmapped` the number of FIGURE rows with no source, which is 0 by construction.
   - `ModelSheetRow` gains the optional `rowKind`, `source`, `sourceLabel` and `teamCite` used above.
3. When `teamSheet` has `rows` but NO `row_classes` (an old payload), the function builds EXACTLY as it does today (round 44's rows-only
   branch, byte for byte); with no `teamSheet` it builds exactly as the base does.
4. `tabs/ModelTab.tsx`: render a `rowKind: 'heading'` row as a heading line in the sheet's order with `data-model-row-kind="heading"` and
   no value cells; render a `source: 'team'` row's cells as the figures with the visible text `team model` on the row and the cite
   (workbook, sheet, row label, period column) in the cell's or row's `title`; a `source: 'why'` row says its `absentReason`. Add no new
   summary line elsewhere. When the served `class` is `master_absent` keep the existing one-line reason above the table.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's check or snapshot. No `__harness__/` edit.
2. NO push of any branch, NO deploy, NO AWS, Bloomberg or vendor call.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W2-S<k>` (next free k across every file under `surprise-channel/`), `disarm_owner 2.0.0_SA_COO~C1`, and
   `surfaced_at` = `date -u +%FT%TZ` at filing.
5. Outer commits with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~2 <0.9.0_WK_AMGT_CORPUS~2@opal.agent>" -F <msgfile> -- <paths>`;
   the portal commit with `git -C portal commit` on branch `wk-AMGT_CORPUS-46-2-portal` (identity `-c user.name=0.9.0_WK_AMGT_CORPUS~2 -c
   user.email=0.9.0_WK_AMGT_CORPUS~2@opal.agent`). Your proof instance's `to_id` is this order's FULL id:
   `AMGT_CORPUS.TO-CRPS-av-2.model-tab-renders-row-classes-and-team-values`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-av-2.model-tab-renders-row-classes-and-team-values.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-av-2.model-tab-renders-row-classes-and-team-values.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md` and the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round46/av2_check.cjs` with `av2_base_snapshot.json`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-av-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round46/av2_check.cjs" portal 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^av2 build 5/5 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-av-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs &gt; /dev/null 2&gt;&amp;1; echo "tabs rc=$?"</invocation><expect>(?m)^tabs rc=0$</expect></criterion>
</proof_of_spec>

- AC1: heading and control handling, the census, Bloomberg-first precedence, the team's value cited and labelled, a why in words; and
  without row classes the output is byte-equal to the base.
- AC2: the page's tab harness still exits 0.

## 5. WHEN YOU ARE DONE

1. Run `bun run typecheck` inside `portal/` and report its exit code.
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2 --governing-order <this order>` AFTER your final commit; rc 0.
3. Only if AC1 and AC2 pass, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change, AC1's and AC2's lines, the typecheck exit code, the portal branch and FULL 40-character portal commit, your
   outer commit hash, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-45 analysis item 1 and ADDENDUM 1 (msg 3846), built in parallel to av-1 against the shape the decomposition fixes. The CTO reviews the candidate before portal DEV (a product file). The rendered census over every served name (av-10) follows once the /12 write (av-3) and the API redeploy (av-4) serve the fields and this is on DEV. Base at the cut: portal origin/DEV 00989b8b: AC1 FAIL (`build 0/5`), AC2 PASS (`tabs rc=0`, as a control must), typecheck not run at the cut.
<risk>LOCAL</risk>
<status>pending</status>
<round>46</round>
<slot>~2</slot>
<fabric>dell1</fabric>
