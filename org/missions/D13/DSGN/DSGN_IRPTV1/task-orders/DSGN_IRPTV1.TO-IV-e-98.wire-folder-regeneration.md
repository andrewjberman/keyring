# TO DSGN_IRPTV1.TO-IV-e-98 -- the portal's generated wire folder holds generator output and nothing else: every hand-added export is emitted or moved out, one command runs both generators, the drift test covers both -- candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-98</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~54</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 4798 (2026-10-11 ~11:12Z): "DSGN_IRPTV1 owns the wire folder's regeneration with its consumers ... a generated folder holds generator output and nothing else ... The two generators (gen-wire, gen-consumed) are run by one command, and the drift test covers both." Rows IRPT_ANLREQ-D2-W51-S6 (BLOCKING) and -S7, moved to this issuer with it | **Decomp cell:** `IV-e-98` (decomposition v18) | **outcome_ref:** FWD-1 (the suite bar; IVE26-AC3) | **depends_on:** IV-e-96 (the portal slot).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's existing worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~54/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo). Its base for this order is the commit
your spawn prompt names. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your
author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never
commit the workspace `portal` gitlink. Resolve bun with `command -v bun`. No `bun install`, no package change. COMMIT FIRST, then run, then
make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file that has no uncommitted work of yours.

**What is wrong today.** The portal's wire-type folder (`src/pages/InvestorReporting/contracts/wire/`, with `responses.ts`, `index.ts` and
`consumed.ts` beside or inside it: establish the exact generated set from the two generators' own output lists) is committed as if generated,
but it is NOT generator output: a fresh run of `gen-wire.ts` breaks 13 types in 8 files and drops exports that were added by hand (portal
1c306eb3, YCD-v-6) and that the generator never emits; a second generator, `gen-consumed.ts`, writes `consumed.ts`; the drift test covers one
of them. Consumers lean on the hand edits. A sibling workstream regenerated the folder and stopped: its result is the INPUT to this cell,
portal branch `wk-IRPT_ANLREQ-51-portal-r4` @890f1d0f3d on origin (fetch it; read it; it is NOT merged and not for DEV as it is). Its three
members `report_id`, `revision`, `retention_ref` are now typed in the contract (workspace @35c17fdd07), which is what unblocks the generator
on `OwnedAnalysisRequest`.

**The cell (`IV-e-98`).** The rule it lands under: **a generated folder holds generator output and nothing else.**

1. **Census first, before any edit** (`WIRE_REGEN.json`, `hand_exports`): run both generators into a scratch folder OUTSIDE both worktrees
   and diff against the committed folder. For EACH export or type present in the committed folder that the generators do not emit: its name,
   the file it is in (`was_in`), and how many source files import it (`consumers`, with the search and its denominator printed). State the
   generated folder (`generated_folder`) and the exact file list each generator owns.
2. **Place each one, one of two ways, never a third:**
   - `GENERATOR_EMITS`: the generator is changed to emit it (because it IS derivable from the contract); or
   - `MOVED_OUTSIDE`: it moves to a hand-written file OUTSIDE the generated folder, and every consumer imports it from there (`now_in`).
   No hand edit survives inside the generated folder (`hand_edits_left_in_generated: 0`). A hand-added export with ZERO consumers is deleted
   and listed with `consumers: 0` and disposition `MOVED_OUTSIDE`, `now_in: "(deleted, no consumer)"`.
3. **One command** runs both generators (a `package.json` script is a package-file change this order does NOT permit: add a small runner
   script under the generators' own folder instead, and name it in `one_command` {command, runs: [...]}).
4. **The drift test covers both generators**: regenerate, compare byte for byte against the committed files of BOTH, fail on any difference.
   One temporary mutant (a hand edit inside the generated folder) makes it fail. `drift`: {test_id, covers, passes, mutant {what, failed}}.
5. **The consumers.** Fix the 13 type errors the regeneration surfaces AT THEIR CAUSE: a consumer that leaned on a hand-edited type is
   brought to the generated type or to the moved export. Never a cast to silence one (`as any`, `as unknown as`), never a `@ts-ignore`. If a
   consumer needs a member the contract does not declare, STOP on that consumer with a row naming the member and the contract file.
   `bun run typecheck` reads 0 errors (`typecheck_errors`).
6. **IVE26-AC3** (`dsgn-irptv1/iv-e-26.wire-regen.test.ts`) fails at base because the generator could not render three members; it should now
   pass. `ive26`: {outcome FIXED or NOT_FIXED, reason}.
7. One whole-scope run before any edit (your base) and one after: `suite_after` {failed, fixed_ids, new_failing_ids}; `product_files_changed`;
   `portal_commit`. Every changed page-facing behaviour (a consumer that now reads a different member) is listed under `behaviour_changes`
   with before and after; "none" is a value you state only after checking each fixed consumer.

<criterion id="IV98-AC1" cell_refs="IV-e-98"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r18/p18_round18.py" . IV98-AC1</invocation><expect>IV98-AC1 PASS</expect></criterion>
`IV98-AC1` -- every hand-added export is emitted by the generator or moved outside the generated folder, none is left inside, and one command runs both generators. Base: FAIL.

<criterion id="IV98-AC2" cell_refs="IV-e-98"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r18/p18_round18.py" . IV98-AC2</invocation><expect>IV98-AC2 PASS</expect></criterion>
`IV98-AC2` -- the drift test covers both generators and can fail, typecheck reads 0 errors, IVE26-AC3 is fixed or reasoned, and no new id fails. Base: FAIL.

<expected_criteria>IV98-AC1,IV98-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract files (`docs/contracts`) are read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no package
  change, no dev server.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W54-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~54/
portal/src/pages/InvestorReporting/
portal/src/api/endpoints/
portal/scripts/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-98.wire-folder-regeneration.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v18 (round 18), cell `IV-e-98`.
<owned_cells>IV-e-98</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV98-AC1,IV98-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~54/DSGN_IRPTV1.TO-IV-e-98.wire-folder-regeneration.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV98-AC1,IV98-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order with one line each, each criterion's last line, the generated folder and each generator's file list, every hand-added export with its consumer count and where it went, the one command, the drift test and its mutant, each of the 13 type errors with its cause and fix, IVE26-AC3, every behaviour change (or "none" with how you checked), `product_files_changed`, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the cell changes types and their consumers on a client-facing page, the consumer count per export is the cell's own first step, and the candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; both criteria FAIL at base (no record). NOT measured by the issuer: the 13 errors and the dropped exports are 2.0.0_SA_COO~Y2's worker's report (msg 4796).
lane: the <paths> block IS the grant.
</preflight>
