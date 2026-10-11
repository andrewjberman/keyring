# TO DSGN_IRPTV1.TO-IV-e-104 -- ONE batched repair cell: the smoke map takes the two corrected routes, the ids that waited on the response schemas are re-run, IVE26-AC3's third arm, and IV-e-97's flip -- test and fixture files only

<to_id>DSGN_IRPTV1.TO-IV-e-104</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~58</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msgs 4864 ("when those land the smoke map takes the two routes") and 4992 ("Row D2-W54-S1 ...: a cell in your next issuance, not a hold"); 2.0.0_SA_COO~P2 msg 4959 (the two producer fixtures corrected and four response schemas declare unprojected_grant, workspace @d8fb17b6d5) | **Rows:** DSGN_IRPTV1-D2-W53-S4 (the excuses), D2-W54-S1 (IVE26-AC3), D2-W53-S10 (IV-e-97's flip) | **Decomp cell:** `IV-e-104` (decomposition v22) | **outcome_ref:** FWD-1 (the suite bar) | **depends_on:** IV-e-105 (the slot).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~58/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` is a real local install that another worktree junctions to: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~58/`) is your base for `new_failing_ids`.

**The cell (`IV-e-104`).** Test, fixture and fixture-generator files ONLY: no product file changes (`product_files_changed: []`), and the
production build is byte-equal before and after (`bun run build`, one sha256 over the built `dist`: for each file in sorted relative-path
order -- sort the paths case-insensitively, as rows of this project note -- update with the path then the bytes). Record in `REPAIRS_22.json`.
1. **The smoke map takes two routes.** IRPT_BCKEND corrected the producer's `DirectoryPage.valid.json` and `AnalysisUploadResult.valid.json`
   (workspace @d8fb17b6d5). RE-MEASURE first: does `parseIrEnvelope` now accept each, wrapped as the map wraps a payload? If yes, the route
   gets an ENTRY (the producer's bytes) and its excuse is REMOVED from `fe-s-1/fixtures.test.ts` and `fe-s-14/published-map.test.ts`
   (those tests fail if an excused route has an entry: that is the forcing). If a reader STILL refuses a corrected fixture, keep that excuse
   with `still_refused: true` and the `refusal_text` you printed, and file a row for 2.0.0_SA_COO~P2 (they asked to be told). Expected: 19
   entries, 3 excuses (the two custody routes and `analysis-request-original`). `smoke_map`: {routes_declared, keys, excused}.
2. **Five ids re-run.** The same commit made four response schemas declare `unprojected_grant`. Run alone, at your base, each of: the three
   failing ids of `fe-s-13/content-pins.test.ts`, `fe-s-13/producer-fixtures.test.ts` "RESPONSE ENVELOPE", and `iv-e-17` IVE17-AC3.
   `rerun_ids`: [{id, result PASS or FAIL, reason}]. One that still fails is READ (its own error first): if a stale pin or count in the TEST
   is the cause and the contract is right, bring the pin to the contract, as strict as before; otherwise leave it red with the reason.
3. **IVE26-AC3's third arm** (row D2-W54-S1): it hard-codes 17 operations where the client consumes 24. Derive the count from the generated
   `contracts/wire/consumed.ts` or the contract's `routes.json` (state which, and why it is the right source), exact and printed, never a
   literal; the arm must still fail if a consumed operation is dropped (one temporary mutant). `ive26`: {outcome, reason}.
4. **IV-e-97's flip.** That order's AC1 was ruled met by its AMENDMENT 1 (a measured no-op on the lock). From the workspace worktree root
   run `python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r17/p17_round17.py" . IV97-AC1` and `... IV97-AC2`;
   if both end PASS, rewrite that order's proof instance (in `deliverables/0.9.0_WK_DSGN_IRPTV1~53/`) to record AC1 as PASS citing
   AMENDMENT 1, validate it with `proof-of-spec-check.py`, and flip that order's `<status>` to `complete`. `ive97_flip`:
   {status_complete, proof_valid}. If either criterion does not pass, do not flip; say why.
5. One whole-scope run after; `suite_after` {failed, fixed_ids, new_failing_ids}; `build_hash_before`, `build_hash_after`, `build_equal`;
   `portal_commit`.

<criterion id="IV104-AC1" cell_refs="IV-e-104"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r22/p22_round22.py" . IV104-AC1</invocation><expect>IV104-AC1 PASS</expect></criterion>
`IV104-AC1` -- the smoke map holds every route whose corrected fixture the reader accepts, the five ids are re-run with their results, IVE26-AC3's third arm is derived or reasoned, and IV-e-97's flip is recorded. Base: FAIL.

<criterion id="IV104-AC2" cell_refs="IV-e-104"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r22/p22_round22.py" . IV104-AC2</invocation><expect>IV104-AC2 PASS</expect></criterion>
`IV104-AC2` -- the production build is byte-equal, no product file changed and no new id fails. Base: FAIL.

<expected_criteria>IV104-AC1,IV104-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract and the producer's fixtures (workspace files)
  are read, never edited. No file under `contracts/wire/` is hand-edited (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W58-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~58/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-104.batched-test-repairs-2.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-97.tooling-hygiene.md
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v22 (round 22), cell `IV-e-104`.
<owned_cells>IV-e-104</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV104-AC1,IV104-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~58/DSGN_IRPTV1.TO-IV-e-104.batched-test-repairs-2.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV104-AC1,IV104-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order, each criterion's last line, whether each corrected fixture is now accepted (with any refusal text), the map's keys and remaining excuses, each of the five ids with its result, IVE26-AC3's third arm before and after with its mutant, IV-e-97's flip, both build hashes, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; test and fixture files only; the production build is proven byte-equal.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
