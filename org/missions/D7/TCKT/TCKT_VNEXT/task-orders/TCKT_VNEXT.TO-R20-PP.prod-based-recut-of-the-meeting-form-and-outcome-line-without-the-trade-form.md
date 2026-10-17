# TO TCKT_VNEXT.TO-R20-PP -- BUILD the PROD-based re-cut of the meeting form (12c164a0) and the outcome line (8e4f0885) WITHOUT the Trade Request upload (c05e3dda) (FWD-11 PROD leg; portal source and tests only)

<to_id>TCKT_VNEXT.TO-R20-PP</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~51</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>PRODCUT</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (a portal candidate branch; the worker pushes and deploys NOTHING)
**Decomp cell:** `R20-pt-4` (`decompositions/TCKT_VNEXT_DECOMP_R20.md`, AMENDMENT 1) | **outcome_ref:** FWD-11, the PROD leg; the CTO's rulings bc18 and 4e37 | **depends_on:** none to build

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~51`.
- **Worktree:** `C:/dev/wk-tckt-vnext-51` (workspace, branch `wk-TCKT_VNEXT-51`) and its portal worktree `C:/dev/wk-tckt-vnext-51/portal` (the portal's own repository, branch `wk-TCKT_VNEXT-51-portal`, cut from portal `origin/PROD` at `fa21a303d87271a1e2d60c514d13501d71f9f020`), both provisioned by the issuer. Work and commit only there:
  - Workspace files (your record, your proof): `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~51 <0.9.0_WK_TCKT_VNEXT~51@opal.agent>" -F <msgfile> -- <paths>` in the workspace worktree.
  - Portal files: `git -c user.name=0.9.0_WK_TCKT_VNEXT~51 -c user.email=0.9.0_WK_TCKT_VNEXT~51@opal.agent commit -F <msgfile>` in the PORTAL worktree, after staging only the files you changed. **Never push, never run a dev server against the live API, never call a live endpoint.**
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `TCKT_VNEXT-D2-W51-S<k>`. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in the code you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call of any kind. Run portal tests with `bun test <file>` from the portal worktree only. Scratch outside the product tree.
- **Portal law you obey:** the canvas is light `#F4F6FA`; white panels with a `#C4CBDB` hairline and navy ink; ONE `#5F3BE3` primary action per view. You add NO new colour, route, write or principal.

### WHY

The CTO ruled (4e37): FWD-11 reaches PROD by a PROD-based re-cut of the meeting form `12c164a0` and the outcome line `8e4f0885`, WITHOUT `c05e3dda`, because Andrew's hold on the Trade Request ("we should not push this til we actually have a functioning channel for that") must stay untouched: no Trade Request code reaches PROD, hidden or not.

### THE CELL (`R20-pt-4`, inlined) -- BUILD ONLY. Nothing is pushed, deployed or called.

The commits `12c164a0`, `c05e3dda` and `8e4f0885` exist in the portal repository (read them with `git -C <portal> show <sha>`); `12c164a0` and `8e4f0885` are the parts you re-cut onto PROD. `c05e3dda` is NOT.

1. **Pick `12c164a0` onto this PROD-based branch** (`git cherry-pick -x 12c164a0`). The CTO measured it applies with no conflict (4 files: `src/api/endpoints/tickets.ts`, `MeetingRequestParts.tsx`, `TicketCenter.tsx`, `__tests__/meeting-request.test.tsx`). `tickets.ts` is touched by both `12c164a0` and `c05e3dda`: take ONLY the meeting hunks; if the pick carries any Trade Request line, remove it.
2. **Pick `8e4f0885` next** (`git cherry-pick -x 8e4f0885`). It conflicts in `src/pages/TicketCenter/TicketCenter.tsx` ONLY, and the conflict is textual: its side carries two DEV-only neighbours, the `TradeFormOpen` import (from `c05e3dda`) and the `AnalysisPackageRow` row (a DEV feature not on PROD). Resolve EXACTLY so:
   1. keep PROD's import of `TradeRequestForm` alone, no `TradeFormOpen`;
   2. take the meeting imports, including `showsMeetingOutcome` and `viewerIsCoordinator`;
   3. keep PROD's `AnalysisDraftAndPackage` row; `AnalysisPackageRow` is NOT pulled;
   4. the meeting row's condition becomes `showsMeetingOutcome(t)`, with the coordinator controls behind `internal && viewerIsCoordinator(t, auth.user?.email)`.
   The other files of `8e4f0885` (`MeetingRequestParts.tsx`, the new `__tests__/meeting-outcome-visibility.test.tsx`, the fixture line in `__tests__/meeting-request.test.tsx`) apply as they are; if one does not apply cleanly on PROD, resolve it to the same meaning and list the lines in your record.
3. **Nothing else changes.** The final diff of `HEAD` against `fa21a303d87271a1e2d60c514d13501d71f9f020` touches ONLY these five files: `src/api/endpoints/tickets.ts`, `src/pages/TicketCenter/MeetingRequestParts.tsx`, `src/pages/TicketCenter/TicketCenter.tsx`, `src/pages/TicketCenter/__tests__/meeting-request.test.tsx`, `src/pages/TicketCenter/__tests__/meeting-outcome-visibility.test.tsx`. The string `TradeFormOpen` and the file `trade-form-upload.test.tsx` are ABSENT from it. Keep the two commits as two commits (the two picks, `-x` trailers kept), so the CTO can read each against its origin.
4. **Run, once, and record the counts in your record:** `bun test src/pages/TicketCenter` (the folder) from the portal worktree, and `bun x tsc -b`. A test OUTSIDE the five files that fails because of your change: STOP and file a BLOCKING row naming it (do not edit it). A test failing on the PROD base without your change is not yours: note it.
5. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~51/R20_PP_RECORD.json`**: the two commit shas and their `-x` origins, the resolution lines you chose (the four points above, one line each), the diff `--stat` against the PROD base, the test counts (the two meeting files, the folder, base vs after), the tsc result, `not_read`.

### ACCEPTANCE

<criterion id="R20PP-AC1" cell_refs="R20-pt-4"><invocation>python C:/dev/wk-tckt-vnext-51/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_pp_checks.py prod-diff --portal C:/dev/wk-tckt-vnext-51/portal --base fa21a303d87271a1e2d60c514d13501d71f9f020</invocation><expect>^R20-PP-DIFF-OK</expect></criterion>
`R20PP-AC1`: the committed diff against the PROD base is the five meeting files only, with no Trade Request upload code and no `AnalysisPackageRow` in an added line.

<criterion id="R20PP-AC2" cell_refs="R20-pt-4"><invocation>python C:/dev/wk-tckt-vnext-51/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_pp_checks.py prod-tests --portal C:/dev/wk-tckt-vnext-51/portal</invocation><expect>^R20-PP-TESTS-OK</expect></criterion>
`R20PP-AC2`: `bun test` of `meeting-request.test.tsx` and `meeting-outcome-visibility.test.tsx` passes with no failure.

<criterion id="R20PP-AC3" cell_refs="R20-pt-4"><invocation>python C:/dev/wk-tckt-vnext-51/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_checks.py portal-tsc --portal C:/dev/wk-tckt-vnext-51/portal</invocation><expect>^R20-TSC-OK</expect></criterion>
`R20PP-AC3`: the portal typechecks (`tsc -b`).

<criterion id="R20PP-AC4J" cell_refs="R20-pt-4" judgment="true"/>
`R20PP-AC4J` (judgment, graded at L9, never by you): the resolution of `TicketCenter.tsx` is the CTO's four points; the meeting row shows on `showsMeetingOutcome(t)` and the controls only for a viewer in `routing.primary`; no Trade Request code reached the branch, hidden or not.

<expected_criteria>R20PP-AC1 R20PP-AC2 R20PP-AC3 R20PP-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~51/` and this order's file (status flip only). If a test outside the grant fails because of your change, STOP and file a BLOCKING row.
- READ only: everything else, including `portal/src/pages/TicketCenter/TradeRequestParts.tsx` and every Trade Request file. You pull NONE of `c05e3dda`.

<paths>
portal/src/api/endpoints/tickets.ts
portal/src/pages/TicketCenter/MeetingRequestParts.tsx
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/pages/TicketCenter/__tests__/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R20.md</decomp_doc>
<owned_cells>R20-pt-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~51/TCKT_VNEXT.TO-R20-PP.prod-based-recut-of-the-meeting-form-and-outcome-line-without-the-trade-form.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R20-PP`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R20PP-AC1,R20PP-AC2,R20PP-AC3,R20PP-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal source change in a worker worktree; nothing is pushed, deployed or called. comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-adversary: RUN -- by reading the CTO's rulings bc18 and 4e37 and the three commits against this cell; the lens: Trade Request code riding in through `tickets.ts` or the `TicketCenter.tsx` import, `AnalysisPackageRow` pulled from DEV into a PROD file, the coordinator controls left behind the old condition, and a test copied from DEV that mocks a DEV-only module. BLIND to: the rendered page (the issuer's later run renders the DEV build; the PROD build is read after the promote).
</preflight>

---

## RECORD FACE

- Cut on the CTO's rulings bc18 (msg 10089) and 4e37 (msg 10097, ruling file `1.0.0_SA_CTO~DELL2/RULING_4E37_FWD11_PROD_RECUT_WITHOUT_TRADE_FORM_20261017.md`) in round 20, decomposition AMENDMENT 1; fan-out 1 of 1 added chain, cap 4. Base: `R20PP-AC1` FAILS as expected (no diff against the PROD base), `R20PP-AC2` FAILS as expected (the new test file is absent on PROD), `R20PP-AC3` PASSES at the base (a bound check).
