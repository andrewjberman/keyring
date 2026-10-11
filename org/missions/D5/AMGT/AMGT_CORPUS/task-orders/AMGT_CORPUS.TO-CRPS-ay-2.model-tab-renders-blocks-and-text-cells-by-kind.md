# AMGT_CORPUS task order -- `CRPS-ay-2` -- ROUND 49: the Model tab renders each served block under its own header and a text cell by what it is (FWD-20, portal half; C-S64 and C-S65)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ay-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- portal source only; no AWS call.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV ad774c6f -- ay2_check.cjs: `ay2 build 0/8 control 2/2` at the base (every build arm fails, both controls pass), `build 8/8 control 2/2` on the issuer's reference patch applied to a fresh tree at that ref (`git apply` clean; `bun run typecheck` rc 0). Blind spot: pure-function level and a string read of `ModelTab.tsx`; the rendered read over every served name is the issuer's (CRPS-ay-5), after the API serves the new fields.
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's review of the candidate.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 49.
**Your portal.** The nested `portal/` directory in your worktree is a portal git worktree on branch `wk-AMGT_CORPUS-49-2-portal`, based on portal `origin/DEV` `ad774c6f`.
Portal files commit INSIDE `portal/` on that branch; the outer commit holds only the outer files. Never commit the portal gitlink. NEVER run `bun install`.
**Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas; reuse the file's classes.

## 1. THE CELL -- `CRPS-ay-2`

Outcome FWD-20 (PRD lines 593-606). The Model tab prints the team sheet's rows aligned to the sheet's ONE period header
(`portal/src/pages/SecurityAnalysis/modelSheet.ts` `buildModelSheet`, the classed team block from about :740; `tabs/ModelTab.tsx` `TeamModelCell`). A parallel cell (`CRPS-ay-1`)
makes the API serve the sheet's OTHER tables as `blocks`, each with its own header rows, and class their rows `BLOCK`. This cell renders them, and prints a text cell by what it is.

**The CTO's principle (round-48 analysis ADDENDUM 1):** every value renders under the header row of ITS OWN BLOCK, as the sheet wrote it. A block headed by periods (any years,
quarters or `E` forms) is a PERIOD grid aligned to that block's periods; a block headed by non-period words is a CASE table under those words; a block whose header the reader cannot read
is UNREAD and stays out of both, with a why.

**The served shape** (`data.model.team_sheet`, the 7th argument; every earlier key stays). It may now carry:

```
row_classes[i]  may be "BLOCK": a row of a block; row_values[i] and row_formats[i] are null. It prints in its block and never in the period grid.
blocks          present only when there is a BLOCK row; in sheet order:
  { first_row, last_row,                        # 1-based sheet rows
    kind: "period" | "case" | "unread",
    why: null | <words, unread only>, withheld: <integer>,
    columns: ["B","C",...]   ([] for unread),
    rows: [ { row_number, kind: "title" | "years" | "body", block_row: <bool>,
              cells: [ null | { v: <number|string>, f: <Excel number format | null> } per column ]   ([] for unread) } ] }
```

A payload captured before this cell carries neither.

**What you build is already written.** The issuer's reference patch is
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay2_reference.patch.txt` (3 files: `modelSheet.ts`, `tabs/ModelTab.tsx`, `types.ts`; 185 insertions,
4 deletions; clean against `ad774c6f`). **Build:**

1. From your worktree: `cd portal && git apply --whitespace=nowarn ../org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay2_reference.patch.txt`
   (LF/CRLF warnings are harmless). `git diff --stat` must show the three files above. Read the diff and the header comment of the issuer's check
   (`.../checks/round49/ay2_check.cjs`): that comment is the contract (arms d1 to d8). Behaviour you may NOT change: every observable in that header.
2. What the patch does, so you can verify it by reading:
   - `types.ts`: `row_classes` admits `'BLOCK'`; `team_sheet.blocks` is typed as above.
   - `modelSheet.ts`: `buildModelSheet` carries `sheetBlocks` (type `SheetBlock`, present ONLY with a non-empty `blocks`): per block `firstRow, lastRow, kind, why, withheld, columns,
     rows[{rowNumber, kind, blockRow, cells}]`; a number cell is `{value, format, display}` where `display` is `formatTeamValue(value, format)`, except an integer 1990..2100 in a
     `title` or `years` row, which prints as the plain integer (`2026`, never `2,026`); a text cell is `{text}` verbatim; an empty cell stays null; an `unread` block carries NO cell. A
     served `BLOCK` row is in NO group's rows. `teamCensus.classes.BLOCK` counts them (the key exists only when one is served) and the classes still sum to the sheet's row count;
     `teamCensus.blocks = {period:{blocks,rows}, case:{...}, unread:{...}, withheld}` (rows = rows with `blockRow` true).
   - C-S65, `modelSheet.ts`: in a team FIGURE row that also holds a number, a string cell is carried as a `TeamCell` with `text` and `textKind`: a string starting with `#` is `'error'`,
     any other non-empty string is `'word'`; blank or null stays null; `TeamCell.value` is `NaN` for a text cell and is never printed; `renderedFigureCount` does not count it. A row
     with NO number keeps its row-level why, unchanged. `teamCensus.text = {error, word, empty, unclassed}` over the rendered team FIGURE rows' cells for the displayed years,
     `unclassed` 0.
   - `tabs/ModelTab.tsx`: a `TeamCell` with `text` prints `error in team sheet` (title: `The research team's own sheet shows an error ("<text>") here, so no value is shown.`) for an
     error and the word verbatim for a word; a `period` or `case` block renders as its own `<table data-sheet-block="<firstRow>">` below the period grid, every raw row of the block
     verbatim, title and years rows as header cells; an `unread` block renders one line per BLOCK row, the row's label (the team sheet's `rows[i]` where `row_numbers[i]` equals the
     block row's number) and the block's `why`, and never a value. Keys are unique (`sheet-block-<firstRow>-<rowNumber>`).
3. Add NO other behaviour. If a hunk does not apply, apply it by hand from the patch text; report which.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's check, snapshot or patch. No `__harness__/` edit.
2. NO push of any branch, NO deploy, NO AWS, Bloomberg or vendor call.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W2-S<k>` (next free k across every file under `surprise-channel/`), `disarm_owner 2.0.0_SA_COO~C1`, and `surfaced_at` = `date -u +%FT%TZ` at filing.
5. Outer commits with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~2 <0.9.0_WK_AMGT_CORPUS~2@opal.agent>" -F <msgfile> -- <paths>`; the portal commit with `git -C portal commit`
   on branch `wk-AMGT_CORPUS-49-2-portal` (identity `-c user.name=0.9.0_WK_AMGT_CORPUS~2 -c user.email=0.9.0_WK_AMGT_CORPUS~2@opal.agent`). Your proof instance's `to_id` is this
   order's FULL id: `AMGT_CORPUS.TO-CRPS-ay-2.model-tab-renders-blocks-and-text-cells-by-kind`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-ay-2.model-tab-renders-blocks-and-text-cells-by-kind.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ay-2.model-tab-renders-blocks-and-text-cells-by-kind.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay2_check.cjs`
with `ay2_base_snapshot.json`, and the reference patch beside them.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ay-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round49/ay2_check.cjs" portal 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^ay2 build 8/8 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ay-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^CHECKS-WRONG-WAY short_read_refused,short_read_control_served,generation_captions_present$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ay-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; grep -c "data-sheet-block" src/pages/SecurityAnalysis/tabs/ModelTab.tsx</invocation><expect>(?m)^[1-9]\d*$</expect></criterion>
</proof_of_spec>

- AC1: blocks (period, case, unread) with their own header cells and the display strings by the cell's own format; BLOCK rows in no period group; the three-way text cell and its census; a
  figure row holding `NA`, `#N/A` and a range stays a FIGURE row; without `blocks` the sheet is byte-equal to the base's (except the added `teamCensus.text`); an inconsistent payload does not throw;
  the unread block prints no value; a block headed by `1Q26..4Q26` is a period block; `ModelTab.tsx` carries the render strings.
- AC2: the page's tab harness fails at portal `ad774c6f` on three CHECKS that are not this cell's (`short_read_refused`, `short_read_control_served`, `generation_captions_present`:
  other teams' DEV merges). The criterion pins that the failing set is exactly those three: your change introduces no new failure and masks none. Do not touch them.
- AC3: the Model tab renders a block.

## 5. WHEN YOU ARE DONE

1. Run `bun run typecheck` inside `portal/` and report its exit code (the reference reads rc 0).
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit; rc 0.
3. Only if AC1-AC3 pass, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change, AC1's, AC2's and AC3's lines, the typecheck exit code, the portal branch and FULL 40-character portal commit, your outer commit hash, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-48 analysis (msg 4158) and ADDENDUM 1 (msg 4165): "Close: the 3,103 split three ways with the denominator, three walks (a second period block, a case block, a
master template), and 0 values under a header that is not their block's own." The CTO reviews the candidate before portal DEV (a product file). The rendered read over every served name
(CRPS-ay-5) follows once the /15 write (ay-3) and an API redeploy serve the fields and this is on DEV. Portal base: origin/DEV `ad774c6f` (fetched 2026-10-11; local `DEV` `cb76f857` lacks
aw-2). The tabs harness at that base fails three checks that are other teams' (reported as a surprise row by the issuer). Base at the cut: AC1 FAIL (`build 0/8`), AC2 PASS (as a control
must), AC3 FAIL (no `data-sheet-block`), typecheck not run at the cut.
<risk>LOCAL</risk>
<status>pending</status>
<round>49</round>
<slot>~2</slot>
<fabric>dell1</fabric>
