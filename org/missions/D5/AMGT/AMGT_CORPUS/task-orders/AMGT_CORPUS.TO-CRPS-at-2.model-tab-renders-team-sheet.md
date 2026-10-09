# AMGT_CORPUS task order -- `CRPS-at-2` -- ROUND 44: the Model tab renders each name's own team sheet rows (FWD-12, portal half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-at-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check runs the real modelSheet.ts on a fixture.
comp-adversary: RUN by the issuer at the cut on portal DEV 3af36f28 -- at2_check.cjs: build 0/2 control 1/1 (62 hard-coded rows for a 6-row team sheet). Blind spot: pure-function level; the rendered page is the issuer's FWD-20 read (CRPS-at-3).
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's render review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 44.

**Your portal.** The nested `portal/` directory in your worktree is a portal git worktree on branch `wk-AMGT_CORPUS-44-portal`, based on
portal origin/DEV. Portal files commit INSIDE `portal/` on that branch; the outer commit holds only the outer files. Never commit the
portal gitlink. NEVER run `bun install`. **Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas; reuse the file's classes.

## 1. THE CELL -- `CRPS-at-2`

Outcome FWD-12 (PRD lines 433-456): the Model tab's rows are each served name's OWN research-team sheet rows, in that sheet's order
and labels. Today `portal/src/pages/SecurityAnalysis/modelSheet.ts` `buildModelSheet` (about line 367) builds one hard-coded row list
(`FINANCIAL_SUMMARY_ROWS` :96, `MARGIN_HISTORY_ROWS` :112, `V3_LINE_ROWS` :123) for every name; `tabs/ModelTab.tsx` (about :542 and
:550) calls it. A parallel cell serves the team sheet on the `/thesis` payload as
`model.team_sheet = {class, workbook_key, sheet, rows: string[], model_rows_beside: string[] | null, reason: string | null}`.

**Build:**
1. `buildModelSheet` takes a 7th optional argument `teamSheet?: {sheet: string; rows: string[]} | null`. When it is given with rows,
   the sheet's rows are EXACTLY those labels in that order (one group is fine): no hard-coded row the team sheet does not carry, none
   of its rows dropped. A team-sheet label that matches an existing row spec's label (case and whitespace insensitive) takes that
   spec's figures; any other row shows no figure and carries `absentReason` in words a PM reads (for example "The research team's
   sheet carries this line; no figure for it is pulled yet."), never "ABSENT", "REFUSED --" or "not read".
2. When `teamSheet` is absent, null, or has no rows, `buildModelSheet` returns exactly what it returns today, byte for byte.
3. `tabs/ModelTab.tsx` passes `data.model?.team_sheet` as that argument in the main sheet call (about :542); when the served class
   is `master_absent`, the tab shows the served `reason` as one line above the table. Leave `historySheet` (about :550) as it is.
4. Add the field to the payload type in `portal/src/pages/SecurityAnalysis/types.ts` (optional, so an old API still type-checks).

## 2. BOUNDS

1. Only the files in `<paths>` change. Never edit the issuer's check or snapshot. No `__harness__/` edit.
2. NO push of any branch, NO deploy, NO AWS, Bloomberg or vendor call.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-D1-W2-S<k>`, `disarm_owner 2.0.0_SA_COO~C1`.
5. Outer commits with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~2 <0.9.0_WK_AMGT_CORPUS~2@opal.agent>" -F <msgfile> -- <paths>`;
   the portal commit with `git -C portal commit` on branch `wk-AMGT_CORPUS-44-portal`. Your proof instance's `to_id` is this order's
   FULL id: `AMGT_CORPUS.TO-CRPS-at-2.model-tab-renders-team-sheet`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-at-2.model-tab-renders-team-sheet.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-at-2.model-tab-renders-team-sheet.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md` and the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round44/at2_check.cjs` with `at2_base_snapshot.json`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-at-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round44/at2_check.cjs" portal</invocation><expect>(?m)^at2 build 2/2 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-at-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs &gt; /dev/null 2&gt;&amp;1; echo "tabs rc=$?"</invocation><expect>(?m)^tabs rc=0$</expect></criterion>
</proof_of_spec>

- AC1: given a team sheet, the rows are exactly its labels in order, and every row with no figure says why in words; without one, the
  output is byte-equal to the base.
- AC2: the page's tab harness still exits 0.

## 5. WHEN YOU ARE DONE

1. Run `bun run typecheck` inside `portal/` and report its exit code.
2. Write the instance at the proof path (genre BUILD), with its mutant control; run `python .tools/proof-of-spec-check.py <instance>
   AC1,AC2 --governing-order <this order>` AFTER your final commit; rc 0.
3. Only if AC1 and AC2 pass, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change, AC1's and AC2's lines, the typecheck exit code, the portal branch and FULL 40-character portal commit, your
   outer commit hash, any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** close read @987284b18e item 1, render half; built in parallel to at-1 against the field shape the decomposition fixes. Candidate to the CTO's render review, then portal DEV (MSTR lands it). FWD-20's rendered census (at-3) follows once at-1 is served and at-2 is on DEV.
<risk>LOCAL</risk>
<status>pending</status>
<round>44</round>
<slot>~2</slot>
<fabric>dell1</fabric>
