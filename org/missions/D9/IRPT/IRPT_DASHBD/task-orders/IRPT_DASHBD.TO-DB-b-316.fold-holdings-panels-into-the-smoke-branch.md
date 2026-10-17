# TO IRPT_DASHBD.TO-DB-b-316 -- FOLD the holdings panels (branch `cand/dell2/irpt-performance-holdings-panels` @f26fb258) INTO the smoke branch `cand/dell2/irpt-49f-performance-template-mount` @355b3bf8 by a MERGE commit, no rebase: one head, one smoke (CTO ruling A, msg 10016) (CLIENT-FACING, portal repo) (round 149)

<to_id>IRPT_DASHBD.TO-DB-b-316</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~251</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>PORTALFOLD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PORTALFOLD, round 149 | **Ordered by:** the CTO's ruling A on the issuer's question (msg 10016): fold the panels into the template branch (Andrew's point 4 asked for them, so he smokes them with the rest); merge `f26fb258` onto `355b3bf8`, no rebase; re-run `p180` and `p181` on the merged head | **Decomp cell:** `DB-b-316` (decomposition section 176).

**Risk class SERVED, client-facing:** a merge commit on the feature branch Andrew smokes; nothing is pushed to DEV or PROD.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-251` (branch `wk-IRPT_DASHBD-251`) and its portal worktree `C:/dev/wk-irpt-dashbd-251/portal`, which the provisioner cut from DEV. **First act:** in the portal worktree run `git fetch origin`, then `git checkout -B cand/dell2/irpt-49f-performance-template-mount origin/cand/dell2/irpt-49f-performance-template-mount` (the head is `355b3bf85fd2e565ae121c5be6562668a9c94072`), then `git merge --no-ff origin/cand/dell2/irpt-performance-holdings-panels` (head `f26fb258b5a6257ee5a62c9f140440c8f5b2597a`). **Never rebase, never force-push.** Never push the workspace; never commit the workspace `portal` gitlink. Every portal commit (the merge included) carries the explicit identity: `git -C <portal> -c user.name="0.9.0_WK_IRPT_DASHBD~251" -c user.email="0.9.0_WK_IRPT_DASHBD~251@opal.agent" ...`. Portal files in this branch use CRLF line endings: keep them (resolve a conflict with a script that reads and writes bytes). Counts, dates, hashes and words only in the workspace repo. Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them. Resolve `bun` from the PATH.

**The cell (`DB-b-316`).**
1. **The merge.** Expect ONE conflict in `src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx` at the `PerformanceTemplateView` mount (the template side wraps the mount in a `49financial` test; the panels side adds `<PerformanceHoldingsPanels snapshot={header?.snapshot ?? null} failed={header?.snapshotFailed ?? false} />` and its import just above). **Resolution: keep BOTH.** The panels line stays immediately before the DB-b-307 comment (outside the `49financial` gate: it shows for every firm), and the template mount stays inside its `49financial` gate exactly as in `355b3bf8`. No other file may differ from the union of the two sides. Do not change any other line.
2. **Run the checks yourself from the workspace root** (the checkers read the portal repo at `<root>/portal`): the panels checker `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py" . DBP180-1-AC1`, then AC2, then AC3; and the firm-gate checker `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py" . DBP181-1-AC1`, then AC2, then AC3. (Both checkers were amended for the merged branch in the issuer's commit; if your workspace copy predates it, copy both from `C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/` before the final run.) AC3 runs the test directory, the typecheck and the production build (2 to 20 minutes). The merged head must pass all six.
3. **Push** ONLY `cand/dell2/irpt-49f-performance-template-mount` (a fast-forward of `355b3bf8` by the merge commit), and tell the issuer the pushed head (ls-remote read).
4. **Record** `RD_PORTAL_FOLD_FACTS_R149.json` in your folder (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~251/`) with EXACTLY these fields: `portal_branch`; `portal_head` (40 hex pushed); `first_parent` ("355b3bf85fd2e565ae121c5be6562668a9c94072"); `second_parent` ("f26fb258b5a6257ee5a62c9f140440c8f5b2597a"); `files_changed_vs_first_parent` (sorted portal paths); `conflict` (one sentence: the file, and how both sides were kept); `tests` (one sentence: counts of irpt-dashbd tests passing); `words` (one paragraph, 80 to 1800 characters: what was merged and why, and what is NOT proven: no browser walk at Global, no DEV or PROD change).

<criterion id="DBP180-1-AC1" cell_refs="DB-b-316"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py" . DBP180-1-AC1</invocation><expect>DBP180-1-AC1 PASS</expect></criterion>
`DBP180-1-AC1` -- on the merged head: the branch is `cand/dell2/irpt-49f-performance-template-mount` and descends from `355b3bf8`; against it only the agreed panels files changed (ReportingTab.tsx by the one mount and import, the new component, the one test file); the component carries its sentences and reuse and never says "mover". Base: FAIL.
<criterion id="DBP180-1-AC2" cell_refs="DB-b-316"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py" . DBP180-1-AC2</invocation><expect>DBP180-1-AC2 PASS</expect></criterion>
`DBP180-1-AC2` -- the panels probe passes on the merged head. Base: FAIL.
<criterion id="DBP180-1-AC3" cell_refs="DB-b-316"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p180_portal_holdings_panels.py" . DBP180-1-AC3</invocation><expect>DBP180-1-AC3 PASS</expect></criterion>
`DBP180-1-AC3` -- every test under `__tests__/irpt-dashbd/` passes on the merged head, the typecheck passes and the production build carries neither the banner nor the fixture. Base: FAIL.
<criterion id="DBP181-1-AC1" cell_refs="DB-b-316"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py" . DBP181-1-AC1</invocation><expect>DBP181-1-AC1 PASS</expect></criterion>
`DBP181-1-AC1` -- the firm gate still holds on the merged head: the branch descends from `75a71ae3`; against it only ReportingTab.tsx (at most 8 changed lines), the firm-gate test, the panels component and the panels test changed; the single template mount sits behind a `49financial` test. Base: FAIL.
<criterion id="DBP181-1-AC2" cell_refs="DB-b-316"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py" . DBP181-1-AC2</invocation><expect>DBP181-1-AC2 PASS</expect></criterion>
`DBP181-1-AC2` -- the firm-gate test names the three firms and PATH A and passes on the merged head. Base: FAIL.
<criterion id="DBP181-1-AC3" cell_refs="DB-b-316"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py" . DBP181-1-AC3</invocation><expect>DBP181-1-AC3 PASS</expect></criterion>
`DBP181-1-AC3` -- the same full proof (tests, typecheck, build, dist scan) on the merged head. Base: FAIL.

<expected_criteria>DBP180-1-AC1,DBP180-1-AC2,DBP180-1-AC3,DBP181-1-AC1,DBP181-1-AC2,DBP181-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and in the portal repo the merge of step 1. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. Writes: the portal feature branch (pushed to origin under its own name only, as a fast-forward), the workspace folder and files named below. No AWS call, no Terraform command, no push of the workspace, no push to DEV or PROD, no rebase, no force.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the conflict is larger than the one described, or a checker clause is wrong rather than your edit, file a BLOCKING row naming it and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W251-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit workspace files with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~251/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-316.fold-holdings-panels-into-the-smoke-branch.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 176 (round 149, workstream PORTALFOLD), cell `DB-b-316`.
<owned_cells>DB-b-316</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBP180-1-AC1, DBP180-1-AC2, DBP180-1-AC3, DBP181-1-AC1, DBP181-1-AC2, DBP181-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~251/IRPT_DASHBD.TO-DB-b-316.fold-holdings-panels-into-the-smoke-branch.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBP180-1-AC1,DBP180-1-AC2,DBP180-1-AC3,DBP181-1-AC1,DBP181-1-AC2,DBP181-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the pushed head (ls-remote read); the conflict in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a portal feature branch merge; no plan, no apply, nothing deployed; nothing is pushed to DEV or PROD.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the six criteria are the two earlier cells' validated checkers, amended for the merged branch; they FAIL at the base (the shared tree's portal is not on the branch).
lane: the <paths> block and the CTO's agreed portal merge ARE the grant.
</preflight>
