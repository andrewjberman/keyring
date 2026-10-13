# TO IRPT_BCKEND.TO-IB-pr-501 -- READ: which packaged HoldingsSnapshot schema copies are validated at serve (row D2-W348-S2; CTO round-172 analysis section 4 item 1)

<to_id>IRPT_BCKEND.TO-IB-pr-501</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~352</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>172</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-172 ANALYSIS (msg 6783) section 4 item 1 | **Decomp cell:** `IB-pr-501` (decomposition section 164) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-501` (inlined):** the builder is about to write an additive `account_id` member on each 49 Financial ACCOUNT node. A Lambda that VALIDATES an answer against its packaged copy of `HoldingsSnapshot.schema.json` at serve would refuse that node (the old node schema has `additionalProperties: false`), so such a copy must be re-pinned and deployed first. The CVO has corrected the earlier assumption: `irpt-holdings` appears NOT to validate at serve. Nobody has read the other packager. **Read, and record, for each function that packages the copy, whether any runtime path validates against it.** READ ONLY: no AWS call, no function invocation, no deploy, no edit of any file outside your folder. Client data is not involved.

**Do:**
1. Compute the set of packagers yourself from `infra/aws/lambda/ci/lambda-source-map.json` (key `functions`): every function whose JSON value contains the string `contracts/HoldingsSnapshot.schema.json`. Expected today: `irpt-holdings` and `irpt-ycharts-generate`. Print the denominator (functions in the map, functions that package the copy).
2. For each packager, find every NON-TEST code reader of the packaged copy: follow the function's `source_dir`, its `files`, and its staged or pinned members (the entries that carry `repo_path` and `pin`; read a pinned member's bytes with `git show <pin>:<repo_path>`, never from the working tree when they differ). A reader is any code that opens, loads or passes the copy. For `irpt-ycharts-generate` the code that runs is the resident package: start from its handler and follow the load of `contracts/` and of `HoldingsSnapshot`. Cite each as `file`, `line` and an exact one-line `quote` (for a pinned member, cite the repo path, and say the pin in a `pin` field).
3. Classify each reader with a `use`: `VALIDATES_AT_SERVE` (a request-time path runs a JSON-schema validator, for example `jsonschema` `validate` or `Draft202012Validator`, over a response or a slice against the copy); `PRESENCE_ONLY` (it reads the copy for a property or a flag without validating a document, as `snapshot.py` `target_admitted()` does); `TEST_ONLY` (only a test calls it); `NOT_READ` (named for completeness). If you find no reader, list the paths you searched in `searched_paths` and leave `readers` empty.
4. Per packager write `validated_at_serve` (true only if some reader is `VALIDATES_AT_SERVE`) and `minimal_repin_members`: when validated, the repo paths that must move in that function's release for the copy to move (the copy's `repo_path`, and any other member that reads something the copy newly admits, with a one-sentence `why`); when not validated, an empty list.
5. Write the record to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~352/IB172-1_serve_validation_read.json`:
`{"packagers":[{"function":"...","readers":[{"file":"...","line":N,"quote":"...","use":"...","pin":"..."}],"searched_paths":[...],"validated_at_serve":false,"minimal_repin_members":[],"why":"..."}],"denominator":{"functions_in_source_map":N,"functions_packaging_the_copy":M},"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"accounts_written":0,"figures_written":0,"vendor_requests_sent":0}`

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB172-1-AC1" cell_refs="IB-pr-501"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r172/p172_cells.py" . IB172-1-AC1</invocation><expect>IB172-1-AC1 PASS</expect></criterion>
<criterion id="IB172-1-AC2" cell_refs="IB-pr-501"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r172/p172_cells.py" . IB172-1-AC2</invocation><expect>IB172-1-AC2 PASS</expect></criterion>
<criterion id="IB172-1-AC3" cell_refs="IB-pr-501"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r172/p172_cells.py" . IB172-1-AC3</invocation><expect>IB172-1-AC3 PASS</expect></criterion>

<expected_criteria>IB172-1-AC1, IB172-1-AC2, IB172-1-AC3</expected_criteria>

What the checks grade: AC1 the record's packagers equal the set the source map gives, with the denominators; AC2 every reader cited resolves (file exists, quote within 3 lines of the line) and carries a `use` from the closed set; AC3 `validated_at_serve` agrees with the readers, the re-pin members are named only for a validated copy and exist as repo files, and the six bound counters read 0. Do not edit the checks. The issuer reads your verdicts against the code before relying on them.

## BOUNDS

- **Grant:** the `paths` block and nothing else. No AWS call, no invocation, no deploy, no edit of product code, tests or the source map.
- **Refusal clause:** STOP, file a row, change nothing more, if a function packages the copy through a mechanism the source map does not show (name it), or a reader cannot be classified from the code (say what you could not read).
- **Row ids** are `IRPT_BCKEND-D2-W352-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~352/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-501.which-holdingssnapshot-copies-validate-at-serve.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 164 (round 172, workstream ~P), cell `IB-pr-501`.
<owned_cells>IB-pr-501</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB172-1-AC1, IB172-1-AC2, IB172-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~352/IRPT_BCKEND.TO-IB-pr-501.which-holdingssnapshot-copies-validate-at-serve.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of repository code; no served artifact, no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p172_cells.py dry-run at base on dell2 2026-10-13 ~04:3xZ: IB172-1 AC1, AC2, AC3 FAIL (no record). Positive control: a synthetic record naming the two packagers with one resolving reader passes all three; flipping validated_at_serve against its readers fails AC3.
lane: the paths block IS the grant; worker slot ~352 of IRPT_BCKEND. Class LOCAL.
</preflight>
