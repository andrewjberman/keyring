# TO IRPT_BCKEND.TO-IB-pr-375 -- the Performance client statement record names who persisted it and binds its content to the retained request's composition hash

<to_id>IRPT_BCKEND.TO-IB-pr-375</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~183</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>87</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO half of IB-pr-373 condition 1 (row D2-W181-S2; msg 1719: "before any firm reads
a Performance client statement, a cell adds a persisted_by field and binds the content to the retained request's composition hash") |
**Decomp cell:** `IB-pr-375` (decomposition section 80) | **outcome_ref:** FWD-8 / IRPT_CUSTDY hop S08 | **depends_on:** IB-pr-373 (drained).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-183` (branch `wk-IRPT_BCKEND-183`). Work and commit only there. `L` =
`infra/aws/lambda/investor-reporting`. Paths below are relative to the worktree.

**Why.** The Performance client statement writer (IB-pr-373, `L/export/custody_persist.py`, code kind CUSTODY_REPORT) derives the owner
and accounts on the server. But the stored record:
- names the retained submission's creator, not the Opal operator who persisted it;
- takes the document as supplied, so nothing binds it to the submission it claims to come from.

The CTO requires both fixed before any firm reads a statement.

**Your cell. Code and tests only; nothing is built, uploaded or applied.**
1. **`persisted_by`.**
   - The stored report record carries `persisted_by`: the verified caller's principal id from `ports["principal"]()`, never a request
     field.
   - Add it where the record is built: `L/export/custody_persist.py` and, if the record schema lives there, `L/reports/custody_write.py`.
   - A read through `custody-report-read` returns it unchanged.
2. **Content binding.**
   - The statement's record carries the retained submission's composition hash (the `REQUEST_COMPOSITION` artifact's own content hash,
     as already stored).
   - The persist REFUSES, with an existing refusal code and nothing written, when the document does not declare that same hash.
   - Equivalently, if the code admits it: the document is recomputed or verified against that composition.
   - Choose the strongest binding the existing data allows, and say why.
3. **Tests**, in `L/export/tests/test_custody_writer_composed.py`, with test names containing:
   - `persisted_by`: the stored record names the verified caller; a body field named `persisted_by` is refused by key name and cannot
     set it.
   - `content_bound`: a document bound to the retained composition persists; a document for a different composition, or with no
     binding, is refused and writes 0 blobs.
   - Show one negative control per group: remove the field or the binding, and the test fails.
   - The whole file still passes.

<criterion id="IB87-2-AC1" cell_refs="IB-pr-375"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r87/p87_cells.py" . IB87-2-AC1</invocation><expect>IB87-2-AC1 PASS</expect></criterion>
`IB87-2-AC1` -- `-k persisted_by` passes. Base: FAIL (no such tests).

<criterion id="IB87-2-AC2" cell_refs="IB-pr-375"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r87/p87_cells.py" . IB87-2-AC2</invocation><expect>IB87-2-AC2 PASS</expect></criterion>
`IB87-2-AC2` -- `-k content_bound` passes, and the whole test file passes. Base: FAIL (no such tests).

<expected_criteria>IB87-2-AC1, IB87-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else. No AWS call, build, upload or source-map edit (the release is a later pair).
- **No route, operation, IAM, bucket, table or principal change.**
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Naming.** In prose and row text, call the report the "Performance client statement"; code ids stay unchanged (Andrew-direct, CTO
  msg 1653).
- **Row ids** are `IRPT_BCKEND-D2-W183-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~183" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~183@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~183 <0.9.0_WK_IRPT_BCKEND~183@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool. **ASCII only**, no control bytes.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/export/custody_persist.py
infra/aws/lambda/investor-reporting/reports/custody_write.py
infra/aws/lambda/investor-reporting/export/tests/test_custody_writer_composed.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-375.pcs-persisted-by-and-content-binding.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~183/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 80 (round 87, workstream ~P), cell `IB-pr-375`.
<owned_cells>IB-pr-375</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB87-2-AC1, IB87-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~183/IRPT_BCKEND.TO-IB-pr-375.pcs-persisted-by-and-content-binding.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the commit hashes, the binding chosen and why, each criterion's last line, the negative controls, and
any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- two source files of irpt-export-render (custody_persist.py, custody_write.py), both added by IB-pr-373 and not yet live; no other function packages them; nothing is released by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p87_cells.py dry-run at base ece42ad420 on dell2 2026-10-08 ~22:0xZ: IB87-2-AC1 FAIL (-k persisted_by: 44 deselected), IB87-2-AC2 FAIL (-k content_bound: 44 deselected).
lane: the <paths> block IS the grant; export/ and reports/custody_write.py are ~P's.
</preflight>
