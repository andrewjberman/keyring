# TO IRPT_BCKEND.TO-IB-pr-619 -- REPAIR: four stale comments and one docstring in retained_export.py still describe the pinned-VersionId filled-report read; make them true after IB-pr-617 (comments and docstring only, no code token)

<to_id>IRPT_BCKEND.TO-IB-pr-619</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~481</issued_to>
<issued_by>2.0.0_SA_COO~S2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** your own row `IRPT_BCKEND-D2-W481-S1` on TO-IB-pr-617 (the four statements), IB-pr-551 ADDENDUM 3.

---

## WORKER FACE

**Cell `IB-pr-619` (inlined).** Your build `302d7fc367` made `read_pinned_filled` read the CURRENT object. Four statements in `infra/aws/lambda/investor-reporting/export/retained_export.py`, outside the function you changed, now say the opposite (your row W481-S1). Replace each with the true statement below. **Comments and one docstring only: no code token, no other function, no other file.** Use exact string replacement of the old text (spacing and line breaks as in the file at your HEAD `dae909c87f`); if an old text is not found verbatim, STOP and report it.

1. The PATH C banner (near line 316). OLD (two comment lines, each starting `# `):
`# report by its client, S3 VersionId, sha256 and byte count. The freeze reads that VersionId through the injected reader,`
`# refuses bytes whose sha256 or size differ from the pin,`
NEW:
`# report by its client, S3 VersionId, sha256 and byte count. The freeze re-reads the CURRENT object through the injected reader`
`# (no VersionId is passed: the export role holds no GetObjectVersion), refuses bytes whose sha256 or size differ from the pin,`
2. The IB-pr-563 block (near line 411). OLD (one comment line):
`# id is the only input taken from the wire). The pinned read that follows reads back exactly that VersionId.`
NEW:
`# id is the only input taken from the wire). The read that follows re-reads the CURRENT object and refuses unless its sha256 and size equal this pin.`
3. The FILLED-REPORT-F banner (near line 495). OLD (two comment lines):
`# server-pins the CURRENT object; the frozen row rides the marked event as `pinned_filled`; the asynchronous leg reads back`
`# exactly the pinned VersionId and never the current object.`
NEW:
`# server-pins the CURRENT object; the frozen row rides the marked event as `pinned_filled`; the asynchronous leg re-reads the`
`# CURRENT object and refuses unless its sha256 and size equal the frozen pin.`
4. The `filled_leg_read` docstring (near lines 554 to 556). OLD (inside the docstring, two lines):
`    the client the item pins; the pinned VersionId is read back through filled_render_read, whose key, sha256 and size must`
`    be the frozen ones, and coverage is judged on those bytes. The current object is never consulted.`
NEW:
`    the client the item pins; the CURRENT object is re-read through filled_render_read, whose key, sha256 and size must`
`    be the frozen ones (a changed object is refused), and coverage is judged on those bytes.`

Leave the module head (the PATH B paragraph about the platinum series read through the route) as it is: it is still true. Touch nothing else.

**Do, in this order. A STOP is reported to the issuer at once and writes nothing further.**
1. Make the four replacements. Run the three export filled-report test files (`python -I -m pytest -q -p no:cacheprovider tests/<file>` from `infra/aws/lambda/investor-reporting/export/`): 31 passed, as before.
2. Run the three criteria below from the repository root (C:/dev/wk-IRPT_BCKEND-481); record each output and exit code verbatim in `IB249-1_criteria_output.txt` under org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/ .
3. Write the proof instance named under proof_of_spec, validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~481 <0.9.0_WK_IRPT_BCKEND~481@opal.agent>" -F <msgfile> -- <explicit paths>` (the message file written with a file-writing tool), flip this order to `complete` only if all three criteria PASS. Report once, under 150 words.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IB249-1-AC1" cell_refs="IB-pr-619"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r249/p249_cells.py" . IB249-1-AC1</invocation><expect>IB249-1-AC1 PASS</expect></criterion>
<criterion id="IB249-1-AC2" cell_refs="IB-pr-619"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r249/p249_cells.py" . IB249-1-AC2</invocation><expect>IB249-1-AC2 PASS</expect></criterion>
<criterion id="IB249-1-AC3" cell_refs="IB-pr-619"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r249/p249_cells.py" . IB249-1-AC3</invocation><expect>IB249-1-AC3 PASS</expect></criterion>

<expected_criteria>IB249-1-AC1, IB249-1-AC2, IB249-1-AC3</expected_criteria>

What the checks grade: AC1 the three test files still pass (31 passed); AC2 the module's syntax tree with docstrings removed equals the one at your build commit `302d7fc367` and no other source file differs from it; AC3 the four stale statements are gone and each site says the CURRENT object is re-read and refused on a sha256 or size mismatch.

## BOUNDS

- **Grant:** edit `infra/aws/lambda/investor-reporting/export/retained_export.py` (comments and the one docstring named above); read anything in the repo; write your deliverables folder, the surprise channel and this order's status. **NO** other file, **NO** AWS call, **NO** deploy, **NO** push, **NO** code change.
- **Refusal clause:** STOP and report if an old text is not found verbatim, or if AC2 reports a code difference.
- **Row ids** `IRPT_BCKEND-D2-W481-S<k>` (next free after S2). `surfaced_at` = `date -u +%FT%TZ` at filing. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/
infra/aws/lambda/investor-reporting/export/retained_export.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-619.make-four-stale-filled-report-comments-true.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 244 (round 9, workstream ~PS), cell `IB-pr-619`.
<owned_cells>IB-pr-619</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB249-1-AC1, IB249-1-AC2, IB249-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~481/IRPT_BCKEND.TO-IB-pr-619.make-four-stale-filled-report-comments-true.proof_of_spec.json` (the file stem of this order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: comments and one docstring in one repo file; no cloud resource is read or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p249_cells.py IB249-1 dry-run at the worker's state dae909c87f on dell2 2026-10-17 ~02:2xZ: AC1 PASS and AC2 PASS (bound checks, nothing changed yet), AC3 FAIL (the four stale statements remain). AC3 also run against a scratch copy with the four planned replacements applied: PASS.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~481` in its own worktree. Class WORLD by the path floor; a repo-only comment repair, no cloud call.
</preflight>
