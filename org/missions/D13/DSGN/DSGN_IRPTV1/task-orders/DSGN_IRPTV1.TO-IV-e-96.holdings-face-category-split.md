# TO DSGN_IRPTV1.TO-IV-e-96 -- the Holdings face opens on the PICKED account's Models / SMAs / Client split -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-96</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~53</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-17 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_17_20261011.md` @e4345abd6e, section 4 item 2 (row DSGN_IRPTV1-D2-S7, second half) | **Decomp cell:** `IV-e-96` (decomposition v17) | **outcome_ref:** FWD-1 | **depends_on:** IV-e-95.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's existing worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo). Its base for this order is the commit
your spawn prompt names. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your
author line (`git -c user.name="<serial>" -c user.email="<serial>@opal.agent" commit -F <msgfile> -- <paths>`); records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. Resolve bun
with `command -v bun`. Several tests in this scope diff or pin COMMITTED state: COMMIT FIRST, then run, then make any temporary mutant, and
revert a mutant only with `git checkout -- <file>` on a file that has NO uncommitted work of yours in it.

Measure your base first: one whole-scope run before any edit (`bun test src/pages/InvestorReporting`, about 100 seconds, output to a file under
`C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~53/`); the failing ids there are what `new_failing_ids` is measured
against (file path plus full test name, spelled as `deliverables/0.9.0_WK_DSGN_IRPTV1~43/SUITE_SAMPLE.json` spells them).

**The cell (`IV-e-96`).** FWD-1's words: the user reads the picked account's holdings split into Models, SMAs and Client. Two rendered walks
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/UI_WALK_DSGN_IRPTV1_FWD1_20261011T0730Z.md` and `...T0945Z.md`, hop 7) found the Holdings tab's
default view splits the total BY ACCOUNT (Trust / Brokerage), and the Models / SMAs / Client category split appears only after opening an
account tile. The CTO reversed its earlier "do not change the page" (analysis section 3, row D2-S7): the Holdings face opens on the PICKED
account's category split.

1. **Find it.** Read the Holdings tab's default-view code under `portal/src/pages/InvestorReporting/` and state, with file and line, what
   decides the default view today and where the picked account is known (`default_view_before`).
2. **Change it, minimally.** When an account is picked (the header's account picker, hop 4 of the walk), the Holdings tab opens on THAT
   account's Models / SMAs / Client split, using the components and data the one-layer-in view already uses: no new request, no new figure, no
   new component library, no new colour. When NO single account is picked (the client-level view), today's by-account view stays. The path
   back to the by-account view stays reachable. State the rule in one sentence (`default_view_after`).
3. **A test that holds it** under the scope's `__tests__/dsgn-irptv1/`: rendered, with a picked account, the default Holdings view shows the
   three category rows for that account; with no picked account it shows the by-account view. One temporary mutant (the old default restored)
   makes it fail. `behaviour`: {test_id, passes, mutant {what, failed}}. Existing tests that pinned the OLD default for a picked account are
   updated to the new rule and listed (`tests_updated`, each with before and after); a test you cannot bring in line without weakening is a row.
4. **Look at it** (portal law: render, look, then commit). Build the portal (`bun run build`) and screenshot from the built folder with
   `node scripts/ui-smoke.mjs <route-without-leading-slash> <out.png> --dist <built dir> --fixtures <f.json>`: NO dev server on any port. At
   least two states, each saved under your deliverables folder: a picked account (the category split) and no picked account (by account).
   Fixture bodies are synthetic (no client figure, no real name or account number). READ each PNG: the script's `LOC` matches the route, its
   `CANVAS` reads `rgb(244, 246, 250)`, no light text or ghost-white fill off the one navy band, content inside panels. Record `screenshots`
   [{state, path, canvas}] and `contract_clauses` (the `portal/DESIGN.md` clause numbers you checked, with what you saw). If the script cannot
   reach the state, say exactly where it stops; do not substitute another route.
5. `bun run typecheck` reads 0 errors. One whole-scope run after; `suite_after`; `product_files_changed`; `portal_commit`.

<criterion id="IV96-AC1" cell_refs="IV-e-96"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r17/p17_round17.py" . IV96-AC1</invocation><expect>IV96-AC1 PASS</expect></criterion>
`IV96-AC1` -- the Holdings default view moved to the picked account's category split, a test holds it and a mutant breaks it, and no new id fails. Base: FAIL.

<criterion id="IV96-AC2" cell_refs="IV-e-96"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r17/p17_round17.py" . IV96-AC2</invocation><expect>IV96-AC2 PASS</expect></criterion>
`IV96-AC2` -- at least two screenshots of the built page exist in the worker's folder on the light canvas, read against the design contract. Base: FAIL.

<expected_criteria>IV96-AC1,IV96-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no package change, no dev server on any port.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W53-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-96.holdings-face-category-split.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v17 (round 17), cell `IV-e-96`.
<owned_cells>IV-e-96</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV96-AC1,IV96-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/DSGN_IRPTV1.TO-IV-e-96.holdings-face-category-split.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV96-AC1,IV96-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order, each criterion's last line, what decided the default view before (file and line) and the rule after, the test and its mutant, every existing test updated with before and after, the screenshots with what each shows and the clauses checked, typecheck, `product_files_changed`, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one tab's default view on a client-facing page; the candidate, with its screenshots, is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the base state is measured by the check's own dry run, every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
