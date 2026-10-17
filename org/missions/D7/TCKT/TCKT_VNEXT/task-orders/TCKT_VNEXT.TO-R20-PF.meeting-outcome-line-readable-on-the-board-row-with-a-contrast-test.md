# TO TCKT_VNEXT.TO-R20-PF -- BUILD the meeting outcome line readable on the Ticket Center board row, with a contrast test (row S59; FWD-11; portal source and tests only)

<to_id>TCKT_VNEXT.TO-R20-PF</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~52</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>PRODFIX</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (a portal candidate branch; the worker pushes and deploys NOTHING)
**Decomp cell:** `R20-pt-5` (`decompositions/TCKT_VNEXT_DECOMP_R20.md`, AMENDMENT 2) | **outcome_ref:** FWD-11; row `TCKT_VNEXT-D2-S59`; the CTO's ruling msg 10423 | **depends_on:** none to build

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~52`.
- **Worktree:** `C:/dev/wk-tckt-vnext-52` (workspace, branch `wk-TCKT_VNEXT-52`) and its portal worktree `C:/dev/wk-tckt-vnext-52/portal` (the portal's own repository, branch `wk-TCKT_VNEXT-52-portal`, cut from `4e1e35bfa0826bbf07971b4cc0bad76ff79edc9d`), both provisioned by the issuer. Work and commit only there:
  - Workspace files (your record, your proof): `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~52 <0.9.0_WK_TCKT_VNEXT~52@opal.agent>" -F <msgfile> -- <paths>` in the workspace worktree.
  - Portal files: `git -c user.name=0.9.0_WK_TCKT_VNEXT~52 -c user.email=0.9.0_WK_TCKT_VNEXT~52@opal.agent commit -F <msgfile>` in the PORTAL worktree, after staging only the files you changed. **Never push, never run a dev server against the live API, never call a live endpoint.**
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `TCKT_VNEXT-D2-W52-S<k>`. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in the code you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call of any kind. Run portal tests with `bun test <file>` from the portal worktree only. Scratch outside the product tree.
- **Portal law you obey:** the canvas is light `#F4F6FA` on the light-theme pages; white panels with a `#C4CBDB` hairline and navy ink; ONE `#5F3BE3` primary action per view. You add NO new colour token, route, write or principal.

### WHY

The first rendered read of the meeting outcome line (the issuer's six shots of the Ticket Center on the DEV build) shows the behaviour right and the line unreadable: `MeetingOutcomeLine` in `src/pages/TicketCenter/MeetingRequestParts.tsx` (about line 222) draws `text-xs font-medium ${INK}` where `INK` (line 29) is `text-[hsl(var(--palette-navy))]`, the ink of a WHITE panel, but the line sits directly on the board's dark row (not in a white panel): measured from the saved PNGs, background rgb(25,38,67) and ink rgb(23,51,114), a contrast of 1.25:1 (readable text needs 4.5:1). The ten existing visibility tests assert the words and never a colour, so they pass. The board's `<tbody>` in `TicketCenter.tsx` carries `text-white/80`; neighbouring text uses `text-white/50` and `text-white/70`.

### THE CELL (`R20-pt-5`, inlined) -- BUILD ONLY. Nothing is pushed, deployed or called.

1. **The fix.** In `MeetingRequestParts.tsx`, `MeetingOutcomeLine` takes a light ink suited to the board row (use the board's own `text-white/80`, or the class its neighbours use if you can show it reads at 4.5:1 or better) instead of `${INK}`. NOTHING ELSE changes: `INK`, `PANEL`, `FIELD`, `BUTTON`, the controls panel (`MeetingOutcomeControls`, a WHITE panel, keeps navy), the words (`outcomeLineWords`), every other component and `TicketCenter.tsx` stay as they are. Keep the `data-slot="meeting-outcome-line"` attribute.
2. **The contrast test.** New file `src/pages/TicketCenter/__tests__/meeting-outcome-contrast.test.tsx` (style of `meeting-outcome-visibility.test.tsx`: `renderToStaticMarkup`, no network). It computes the WCAG relative-luminance contrast ratio of the line's EFFECTIVE ink over the board row's background FROM THE CSS TOKENS (read `src/index.css`: resolve the page layer the board row sits on and the ink colour including its alpha, composited over that background; show the arithmetic in the test) and asserts at least 4.5:1. Named tests (the issuer's check scans for the file and counts at least two new passing tests): `the outcome line reads at 4.5:1 or better on the board row`, `the outcome line carries no navy ink class`, `the coordinator's controls panel keeps navy ink on its white panel`. If the board's background token cannot be resolved from `src/index.css`, use the measured value rgb(25,38,67) and say so in the test comment and in your record (a CLAIM, labelled measured from the rendered page, not from the tokens).
3. **Before the fix, the new contrast test FAILS on the base** (record that run in your record: the line's class and the computed ratio). After the fix, all pass.
4. **Run, once, and record the counts:** `bun test` of the three files (`meeting-outcome-contrast`, `meeting-outcome-visibility`, `meeting-request`), `bun test src/pages/TicketCenter` (the folder), and `bun x tsc -b`. A test outside your two files that fails because of your change: STOP and file a BLOCKING row (do not edit it).
5. **ONE portal commit** carrying exactly the two files, subject `fix(TicketCenter): the meeting outcome line takes a light ink on the dark board row, with a contrast test (row TCKT_VNEXT-D2-S59)`. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~52/R20_PF_RECORD.json`**: the commit sha, the class before and after, the computed ratio before and after and the token path, the test counts, tsc, `not_read`.

### ACCEPTANCE

<criterion id="R20PF-AC1" cell_refs="R20-pt-5"><invocation>python C:/dev/wk-tckt-vnext-52/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_pf_checks.py pf-diff --portal C:/dev/wk-tckt-vnext-52/portal --base 4e1e35bfa0826bbf07971b4cc0bad76ff79edc9d</invocation><expect>^R20-PF-DIFF-OK</expect></criterion>
`R20PF-AC1`: the committed diff against the base touches only `MeetingRequestParts.tsx` and the new contrast test, with no Trade Request upload code and no `AnalysisPackageRow` in an added line.

<criterion id="R20PF-AC2" cell_refs="R20-pt-5"><invocation>python C:/dev/wk-tckt-vnext-52/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_pf_checks.py pf-tests --portal C:/dev/wk-tckt-vnext-52/portal</invocation><expect>^R20-PF-TESTS-OK</expect></criterion>
`R20PF-AC2`: the new contrast test file exists and `bun test` of it with the two meeting test files passes with no failure (at least 26 pass).

<criterion id="R20PF-AC3" cell_refs="R20-pt-5"><invocation>python C:/dev/wk-tckt-vnext-52/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_checks.py portal-tsc --portal C:/dev/wk-tckt-vnext-52/portal</invocation><expect>^R20-TSC-OK</expect></criterion>
`R20PF-AC3`: the portal typechecks (`tsc -b`).

<criterion id="R20PF-AC4J" cell_refs="R20-pt-5" judgment="true"/>
`R20PF-AC4J` (judgment, graded at L9, never by you): the line now takes a light ink that reads on the board row at 4.5:1 or better computed from the tokens (or the stated measured value); the controls panel keeps navy on white; nothing else changed.

<expected_criteria>R20PF-AC1 R20PF-AC2 R20PF-AC3 R20PF-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~52/` and this order's file (status flip only).
- READ only: everything else, including `src/index.css`, `TicketCenter.tsx` and every Trade Request file.

<paths>
portal/src/pages/TicketCenter/MeetingRequestParts.tsx
portal/src/pages/TicketCenter/__tests__/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R20.md</decomp_doc>
<owned_cells>R20-pt-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~52/TCKT_VNEXT.TO-R20-PF.meeting-outcome-line-readable-on-the-board-row-with-a-contrast-test.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R20-PF`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R20PF-AC1,R20PF-AC2,R20PF-AC3,R20PF-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal source change in a worker worktree; nothing is pushed, deployed or called. comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-adversary: RUN -- by reading the six shots, the row S59 and the file against this cell; the lens: a contrast test that asserts a class name instead of a computed ratio, a fix that also turns the white controls panel light, an ink alpha composited over the wrong background, and a test that passes on the base. BLIND to: the rendered page after the fix (the issuer's re-shot reads it).
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling msg 10423 (yes: one cell, a one-class fix with a contrast test, a PROD-based branch, a follow-up PROD release) in round 20, decomposition AMENDMENT 2, `<workstream>PRODFIX</workstream>`; fan-out 1 of 1 added chain, cap 4. Base: `R20PF-AC1` FAILS as expected (no diff against the base), `R20PF-AC2` FAILS as expected (the new test file is absent), `R20PF-AC3` PASSES at the base (a bound check).
