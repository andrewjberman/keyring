# AMGT_CORPUS task order -- `CRPS-aw-2` -- ROUND 47: the Model tab prints a field-code row by its served label in words and a team value by its own number format (FWD-20, portal half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aw-2, CRPS-aw-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- portal source only; no AWS call.
comp-adversary: RUN by the issuer at the cut on portal DEV cb76f857 -- aw2_check.cjs: `aw2 build 0/4 control 2/2` at the base, `build 4/4 control 2/2` on a throwaway reference patch (not shipped). Blind spot: pure-function level; the rendered read over every served name is the issuer's (CRPS-aw-6), after the API serves the new fields.
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's review of the candidate.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 47.
**Your portal.** The nested `portal/` directory in your worktree is a portal git worktree on branch `wk-AMGT_CORPUS-47-2-portal`, based on
portal DEV `cb76f857`. Portal files commit INSIDE `portal/` on that branch; the outer commit holds only the outer files. Never commit the
portal gitlink. NEVER run `bun install`. **Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas; reuse the file's classes.

## 1. THE CELL -- `CRPS-aw-2`

Outcome FWD-20 (PRD lines 593-606, read them). With a served team sheet the Model tab already prints each FIGURE row's team values verbatim
(`portal/src/pages/SecurityAnalysis/modelSheet.ts` `buildModelSheet`, the block from about :540; `tabs/ModelTab.tsx` `TeamModelCell`). Measured on
the live page: 1348 of 3381 FIGURE rows are labelled by a raw field code, and 72% of the team's float cells print past 4 decimals. A parallel cell
(`CRPS-aw-1`) makes the API serve, per name, a label in words and each cell's own Excel number format. This cell renders them.

**The served shape** (`data.model.team_sheet`, the 7th argument; every round-46 key stays). It gains, aligned with `rows`:

```
row_labels   [null | {"text", "source": "bloomberg"|"factset", "claim": "held"|"absent", "cite": <path>|null, "code", "why": <words>|null}, ...]
row_formats  [null | [<the period cell's Excel number format string, or null> per period, ...], ...]     (non-null only for a FIGURE row)
```

A payload captured before this cell carries neither key.

**Build:**

1. `types.ts`: add the two optional fields to the `team_sheet` type (next to `row_values`, about line 1150), so an old payload still type-checks.
2. `modelSheet.ts`:
   - export `formatTeamValue(value: number, format?: string | null): string`. Prints by the Excel format string: the digits after `.` set the
     decimals (rounded half away from zero), a `,` in the integer part sets the thousands separator, a `%` multiplies by 100 and prints `%`, a
     second `;` section is the negative form (`#,##0;(#,##0)` prints -1234.5 as `(1,235)`), quoted text is kept literally, `[...]` tags and `_x`
     padding are dropped; `General`, null or an empty format prints at most 4 decimals with trailing zeros trimmed. The table the issuer's check
     asserts: `(1234.567,'#,##0')` -> `1,235`; `(0.087,'0.0%')` -> `8.7%`; `(1.2345,'0.00')` -> `1.23`; `(-1234.5,'#,##0;(#,##0)')` -> `(1,235)`;
     `(28.066938033222375,'General')` -> `28.0669`; `(100,'General')` -> `100`; `(-0.028,'0.0%')` -> `-2.8%`; `(0.5,'0%')` -> `50%`;
     `(1234.5,'#,##0.00')` -> `1,234.50`; `(7,null)` -> `7`; `(1234.5,'"$"#,##0.00')` -> `$1,234.50`.
   - `TeamCell` gains `format?: string | null`: set on a team cell ONLY when `row_formats[i]` is an array (then `format` = that array's entry for the
     cell's period, else null). The cell's `value` stays the saved value.
   - `ModelSheetRow` gains `labelTitle?: string | null`.
   - In the classed team branch, for a FIGURE row that takes the team's value or a why (never a Bloomberg-first row), when `row_labels[i]` is a
     dict: `label` = its `text`; `labelTitle` = `code` when `claim` is `held`, else `` `${code}: ${why}` ``; and when `source` is `factset` and the
     row is a team row, `sourceLabel` = `FactSet, via team model` (every other team row keeps `team model`). `teamCite.label` stays the sheet's own
     label (the code as read). A row with no `row_labels[i]` keeps its sheet label.
   - `TeamCensus` gains optional `labels: {held, factset_line, bloomberg_line, raw}`, present ONLY when the payload carries `row_labels`:
     `held` counts rendered rows whose entry has `claim` held; `factset_line` rows with `source` factset and `claim` absent; `bloomberg_line` rows
     with `source` bloomberg and `claim` absent; `raw` counts rendered rows whose final `label` still matches `^[A-Z][A-Z0-9]*(_[A-Z0-9]+)+$`
     (it must be 0 on a complete payload). Every round-46 census key is unchanged.
   - Without `row_labels` and `row_formats` the built sheet is byte-equal to the base's (no `labels` key, no `format` key, no `labelTitle`); with
     no `teamSheet` the build is exactly the base's.
3. `tabs/ModelTab.tsx`: a team row's label cell carries `title={row.labelTitle}` when set; the visible source text under the label on a team row
   is `row.sourceLabel` (today the literal `team model`); `TeamModelCell` prints `formatTeamValue(figure.value, figure.format)` (the
   `data-model-cell` attribute keeps the full value) and its title adds the full value: the cite then `; full value <value>`. **Unique keys:** the
   row `key` at about :687 is `${group.title}:${row.label}`; after this change many rows share the label "FactSet line", so every team-row key must
   be unique (use the sheet row `row.teamCite?.row` when present, else the index) in EVERY place the group's rows are keyed (heading rows too).
   Add no new summary line elsewhere.

**AMENDMENT 1 (issuer, 2026-10-11 ~17:3xZ; cell `CRPS-aw-11` folded into this order; build it after your committed work and commit it
separately).** The lib half now also serves a THIRD claim: a code row's label MEASURED from the team's own workbook:
`row_labels[i] = {"text": <the team's own label>, "source": "factset"|"bloomberg", "claim": "measured", "cite": "<sheet>!<cell>", "code", "why": null}`
(for example `{"text": "Revenue", "source": "factset", "claim": "measured", "cite": "Model NEW VERSION!D4", "code": "FF_SALES", "why": null}`).
Render it: (1) `TeamRowLabel.claim` is `'held' | 'absent' | 'measured'`; (2) the row's `label` is its `text`; (3) its `labelTitle` is
`` `${code}: measured from the team's sheet at ${cite}` `` (the code alone when `cite` is null); (4) a `factset` source keeps `sourceLabel`
`FactSet, via team model`; (5) `TeamCensus.labels` gains `measured`: the rendered rows whose entry's claim is `measured`; those rows are NOT
counted in `held`, `factset_line` or `bloomberg_line`, and `raw` is unchanged (0 on a complete payload); the key `measured` is present
whenever `row_labels` is. Without `row_labels` nothing changes. The issuer's check gained a fifth arm: `aw2 build <b>/5 control <c>/2`; AC1's
expectation below reads `5/5`. Your two rows W2-S3 (a null why) and W2-S4 stand as filed.

**AMENDMENT 2 (issuer, 2026-10-11 ~19:5xZ; the CTO's ruling at the /13 write, msg 4086 point 1: a master answer is labels only).** The lib half now stores,
for a name with no workbook of its own, `team_sheet.class = 'master'`: the template's rows, classes and labels, with `row_values` and `row_formats` all null and
`periods` `[]` (the template is filled with one sample company's figures; none is served). Render it: for a teamSheet whose `class` is `'master'`, a FIGURE
row keeps the existing precedence (the name's own Bloomberg figure when the label matches a row spec and the block carries it), and otherwise takes
`source: 'why'` with `absentReason` EXACTLY `The research team keeps no workbook for this company; this row is from the team's template.` (the sentence for an own-workbook name stays
`The research team's sheet holds no value for this line in the years shown.`). HEADING rows stay headings and CONTROL rows stay out; the census is
unchanged in shape. The issuer's check gained a sixth arm d6: `aw2 build <b>/6 control <c>/2`; AC1 below expects `6/6`. Nothing else changes.

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's check or snapshot. No `__harness__/` edit.
2. NO push of any branch, NO deploy, NO AWS, Bloomberg or vendor call.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W2-S<k>` (next free k across every file under `surprise-channel/`), `disarm_owner 2.0.0_SA_COO~C1`, and
   `surfaced_at` = `date -u +%FT%TZ` at filing.
5. Outer commits with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~2 <0.9.0_WK_AMGT_CORPUS~2@opal.agent>" -F <msgfile> -- <paths>`;
   the portal commit with `git -C portal commit` on branch `wk-AMGT_CORPUS-47-2-portal` (identity `-c user.name=0.9.0_WK_AMGT_CORPUS~2 -c
   user.email=0.9.0_WK_AMGT_CORPUS~2@opal.agent`). Your proof instance's `to_id` is this order's FULL id:
   `AMGT_CORPUS.TO-CRPS-aw-2.model-tab-prints-labels-in-words-and-team-number-formats`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-aw-2.model-tab-prints-labels-in-words-and-team-number-formats.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aw-2.model-tab-prints-labels-in-words-and-team-number-formats.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md` and the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw2_check.cjs` with `aw2_base_snapshot.json`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aw-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw2_check.cjs" portal 2&gt;&amp;1 | tail -1</invocation><expect>(?m)^aw2 build 6/6 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aw-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs &gt; /dev/null 2&gt;&amp;1; echo "tabs rc=$?"</invocation><expect>(?m)^tabs rc=0$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-aw-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; grep -c "formatTeamValue(" src/pages/SecurityAnalysis/tabs/ModelTab.tsx</invocation><expect>(?m)^[1-9]\d*$</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-aw-11"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw2_check.cjs" portal 2&gt;&amp;1 | grep -c '^aw2 d5 .* ok true$'</invocation><expect>(?m)^1$</expect></criterion>
</proof_of_spec>

- AC4: the measured claim renders (AMENDMENT 1); a fourth mechanical criterion because the folded cell `CRPS-aw-11` needs its own.
- AC1: the label in words and its title, the source label, `formatTeamValue`'s table, the cell's format, the label census with `raw` 0, the measured claim (amendment 1); and without
  the new keys the output is byte-equal to the base.
- AC2: the page's tab harness still exits 0.
- AC3: the Model tab calls `formatTeamValue`.

## 5. WHEN YOU ARE DONE

1. Run `bun run typecheck` inside `portal/` and report its exit code.
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit; rc 0.
3. Only if AC1-AC3 pass, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change, AC1's, AC2's and AC3's lines, the typecheck exit code, the portal branch and FULL 40-character portal commit, your
   outer commit hash, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-46 analysis ADDENDUM 1 (msg 3972): the cell says "FactSet, via team model" on a FactSet row; "0 raw codes visible over 1,348, split by source, with the fallback count printed"; team values by their own format with the full value in the title. The CTO reviews the candidate before portal DEV (a product file). The rendered read over every served name (aw-6) follows once the /13 write (aw-3) and the API redeploy (aw-4) serve the fields and this is on DEV. Duplicate display labels make the existing `key` unsafe: named on the face. Base at the cut: portal DEV cb76f857: AC1 FAIL (`build 0/4`), AC2 PASS (as a control must), AC3 FAIL (no `formatTeamValue` call), typecheck not run at the cut.
<risk>LOCAL</risk>
<status>pending</status>
<round>47</round>
<slot>~2</slot>
<fabric>dell1</fabric>
