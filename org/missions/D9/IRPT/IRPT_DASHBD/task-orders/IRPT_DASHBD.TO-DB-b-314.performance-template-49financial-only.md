# TO IRPT_DASHBD.TO-DB-b-314 -- the Performance tab mounts the 49 Financial TEMPLATE for a 49 Financial client ONLY (CTO ruling msg 9933 after the page owner's R154 check): Cottonwood joins when its filled report publishes, Inflection never and Inflection keeps its PATH A performance; a follow-up commit on the DB-b-309 branch (CLIENT-FACING, portal repo) (round 149)

<to_id>IRPT_DASHBD.TO-DB-b-314</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~250</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>PORTALFIRMGATE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PORTALFIRMGATE, round 149 | **Ordered by:** the CTO's ruling msg 9933 and the page owner's check `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/R154_INFLECTION_PATH_A_CHECK_ON_75A71AE3.md` (@84ff9c5bcc): `PerformanceTemplateView` is mounted at `ReportingTab.tsx` for any client with no firm test, so an Inflection client's page shows the SYNTHETIC PREVIEW banner and the 49 Financial fixture under its PATH A performance | **Decomp cell:** `DB-b-314` (decomposition section 174).

**Risk class SERVED, client-facing:** a page cell in the portal repo on the feature branch Andrew is smoking; nothing is pushed to DEV or PROD.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-250` (branch `wk-IRPT_DASHBD-250`) and its portal worktree `C:/dev/wk-irpt-dashbd-250/portal`, which the provisioner cut from DEV. **First act:** in the portal worktree run `git fetch origin` then `git checkout -B cand/dell2/irpt-49f-performance-template-mount origin/cand/dell2/irpt-49f-performance-template-mount` (the head is `75a71ae39089baf9fdddcc34cd3075dea4b31701`); you add ONE commit on top of it and push the same branch (a fast-forward). Never push the workspace; never commit the workspace `portal` gitlink. Every portal commit carries the explicit identity: `git -C <portal> -c user.name="0.9.0_WK_IRPT_DASHBD~250" -c user.email="0.9.0_WK_IRPT_DASHBD~250@opal.agent" commit ...`. Portal files in this branch use CRLF line endings: keep them (edit with a script that reads and writes bytes); the change must stay a few lines, never a whole-file diff. Counts, dates, hashes and words only in the workspace repo; the tests are synthetic. Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them. Resolve `bun` from the PATH.

**The cell (`DB-b-314`).**
1. **Read first, whole:** the page owner's file named above; the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py` (your three criteria); `tabs/reporting/ReportingTab.tsx` around the one `<PerformanceTemplateView` mount (its `firmId` prop is `scope?.scope.firmId ?? header?.selection?.scope.firmId ?? null`).
2. **The gate:** in `ReportingTab.tsx` render `<PerformanceTemplateView ... />` ONLY when that same firm id equals `'49financial'`; otherwise render nothing for it. Read the firm id once into a `const` above the return or inline, as the code's style allows, but the string `49financial` must sit within 400 characters before the mount, and the file may change by at most 8 lines in all. Do NOT edit `PerformanceTemplateView.tsx`, `index.tsx` or any other file. Cottonwood is OUT until its filled report publishes; Inflection is never in this template; the PATH A performance of an Inflection client must render exactly as before.
3. **ONE new test file `__tests__/irpt-dashbd/performance-template-firm-gate.test.tsx`** (its name starts exactly so) with one test per firm: a `49financial` client mounts the template block (its `data-section="cover"` or live/loading/unavailable state is in the markup); a `cottonwood` client does not (no template markup, no SYNTHETIC PREVIEW words); an `inflection` client does not AND keeps its PATH A performance (assert the PATH A report markup the tab renders for that client is still present, as the existing Inflection tests of `__tests__/irpt-dashbd/` show; the test text must contain the words `PATH A`). Use the seeding patterns of the existing `__tests__/irpt-dashbd/performance-tab-global-and-firm.test.tsx`. The suite's failing names, if any, are a subset of the base's.
4. **Files you may change:** `tabs/reporting/ReportingTab.tsx` and the one new test file. **Not** anything else.
5. **Run the checks yourself from the workspace root** (the checker reads the portal repo at `<root>/portal`): `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py" . DBP181-1-AC1`, then AC2, then AC3 (AC3 runs the test directory, the typecheck and the production build, 10 to 20 minutes). Commit on the portal branch (explicit identity), push ONLY `cand/dell2/irpt-49f-performance-template-mount`, and tell the issuer the pushed head (ls-remote read).
6. **Record** `RD_PORTAL_FIRM_GATE_FACTS_R149.json` in your folder (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~250/`) with EXACTLY these fields: `portal_branch`; `portal_head` (40 hex pushed); `base_head` ("75a71ae39089baf9fdddcc34cd3075dea4b31701"); `files_changed` (sorted portal paths); `gate` (one sentence: the condition and where); `tests_added` (the new test file name); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: no browser walk, no live render of an Inflection client, nothing on DEV or PROD).

<criterion id="DBP181-1-AC1" cell_refs="DB-b-314"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py" . DBP181-1-AC1</invocation><expect>DBP181-1-AC1 PASS</expect></criterion>
`DBP181-1-AC1` -- the branch is still `cand/dell2/irpt-49f-performance-template-mount` and descends from `75a71ae3`; only `ReportingTab.tsx` (at most 8 changed lines) and the one new test file changed; the single `<PerformanceTemplateView` mount sits behind a `49financial` test. Base: FAIL.
<criterion id="DBP181-1-AC2" cell_refs="DB-b-314"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py" . DBP181-1-AC2</invocation><expect>DBP181-1-AC2 PASS</expect></criterion>
`DBP181-1-AC2` -- the cell's test file names 49 Financial, Cottonwood, Inflection and PATH A, and passes under bun. Base: FAIL.
<criterion id="DBP181-1-AC3" cell_refs="DB-b-314"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p181_template_firm_gate.py" . DBP181-1-AC3</invocation><expect>DBP181-1-AC3 PASS</expect></criterion>
`DBP181-1-AC3` -- the cell's test file exists; every test under `__tests__/irpt-dashbd/` passes; the typecheck passes; the production build succeeds and its output carries neither the `SYNTHETIC PREVIEW` words nor the synthetic fixture. Base: FAIL (the cell's test file is missing).

<expected_criteria>DBP181-1-AC1,DBP181-1-AC2,DBP181-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and in the portal repo the write set of step 4. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. Writes: the portal feature branch (pushed to origin under its own name only), the workspace folder and files named below. No AWS call, no Terraform command, no push of the workspace, no push to DEV or PROD.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W250-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit workspace files with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~250/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-314.performance-template-49financial-only.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 174 (round 149, workstream PORTALFIRMGATE), cell `DB-b-314`.
<owned_cells>DB-b-314</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBP181-1-AC1, DBP181-1-AC2, DBP181-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~250/IRPT_DASHBD.TO-DB-b-314.performance-template-49financial-only.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBP181-1-AC1,DBP181-1-AC2,DBP181-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the pushed head (ls-remote read); the gate in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a portal feature branch; no plan, no apply, nothing deployed; nothing is pushed to DEV or PROD.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and AC1 and AC2 PASS on a reference edit in a scratch portal worktree (AC3 is the same proof as p177 AC3, run by the worker).
lane: the <paths> block and the page owner's agreed portal write set ARE the grant.
</preflight>
