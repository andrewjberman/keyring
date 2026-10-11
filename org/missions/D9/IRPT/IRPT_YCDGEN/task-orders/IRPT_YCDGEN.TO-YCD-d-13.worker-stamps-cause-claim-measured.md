# TO-YCD-d-13 -- the worker stamps `cause_claim: "measured"` on the dead-letter record it writes (PRD v0.12), and two stale tests are repaired

<to_id>IRPT_YCDGEN.TO-YCD-d-13</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~16</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-d-13` (`decompositions/IRPT_YCDGEN_DECOMP_R13.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none.

---

## 0.9.0_WK_IRPT_YCDGEN~16 FACE

### Read first

`infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`: the function `_record_deliveries_exhausted` (search `def _record_deliveries_exhausted`).
`infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_dead_letter_record.py` (its tests of that function). `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_package_poll.py`: the two tests
named `test_e_both_bindings_carry_the_packager_and_ready_sends_to_the_bound_url` and
`test_e_only_the_commentary_binding_adds_the_packager_and_leaves_i3_unset`, and the helper `rewrite`.
`infra/aws/lambda/investor-reporting/reports/resident_installed.py`: `PACKAGER_KEYS` and the function that
raises `RESIDENT_PACKAGER_REQUIRED` (what a valid `packager` member is: exactly `api_base` and `secret_name`).
`infra/aws/lambda/investor-reporting/reports/tests/test_resident_packager_binding.py` (a passing example of a bindings
document that carries a packager). The contract: `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md`, search
`cause_claim`.

### THE CELL

Two small things, one commit or two.

**A. The stamp.** The contract says a dead-letter record carries FOUR members: `code`, `cause`, `receives`, `cause_claim`.
`cause_claim` is `measured` when the worker writes the record at the moment of the failure. The worker writes three today.

1. In `_record_deliveries_exhausted`, the detail passed to `store.put_state` becomes
   `{"code": "DELIVERIES_EXHAUSTED", "cause": cause, "receives": receives, "cause_claim": "measured"}`.
2. Nothing else in the function changes: the journal line it prints is byte-for-byte as today (it does NOT gain the new
   member), the limit, the early returns, the claim and release, and the second-error line are untouched.
3. `cause_claim` appears NOWHERE else in `resident_worker.py`. No constant, no helper, no second writer. The worker never
   writes the value `inferred`.
4. In `test_dead_letter_record.py`, every assertion on the written detail expects the four members (there are two today,
   search `table.detail ==`). Add no new test unless one is needed to keep the file honest.

**B. Two stale tests.** `test_package_poll.py`'s two tests named above fail today with `RESIDENT_PACKAGER_REQUIRED`: the
runtime now refuses a bindings document that binds the commentary queue without a `packager` member, and these two tests
bind the queue and give none. The runtime is right. Repair the TESTS only:

5. Give each of the two tests a valid `packager` member in the bindings it rewrites (an `https://` `api_base` on an
   invented example host and an invented `secret_name`; no real host, no real secret name). If `rewrite` cannot carry a
   dict member as written, extend it minimally.
6. Their assertions on the runtime's keys and on I3 stay. If the runtime now needs a secrets client to BUILD the packager
   port, give the fake one that fails loudly if called at build (the port must not read the secret at build; if it does,
   that is a row, not something to hide).
7. Do NOT change `resident_installed.py`, `opal_packager.py` or any file outside `<paths>`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="D13-AC1" cell_refs="YCD-d-13"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r13/r13_checks.py d13</invocation><expect>^R13-D13-OK</expect></criterion>

<criterion id="D13-AC2" cell_refs="YCD-d-13"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r13/r13_checks.py d13suite</invocation><expect>^R13-D13SUITE-OK</expect></criterion>

<expected_criteria>D13-AC1,D13-AC2</expected_criteria>

- AC1 reads the record function for exactly one `"cause_claim": "measured"`, counts 0 uses of `cause_claim` elsewhere in the
  worker, counts at least 2 test assertions carrying it, and runs the dead-letter test file: 0 failed, at least 9 passed.
  At base it FAILs (no stamp).
- AC2 runs the whole `ycharts/generate/tests` folder: 0 failed, 0 errors, at least 507 passed. At base it FAILs (2 failed,
  505 passed). It takes about two minutes.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. Every `.py` edit passes
  `.tools/commit-gate.sh`. This cell ships to the host only in a later resident release under its own pair.
- **Refusal clause.** If a criterion cannot be met as written, or the commit is refused because these files are another
  project's lane: stop, file a row with the refusal text, report, and do not weaken a check or force a commit.
- **Rows** are `IRPT_YCDGEN-D2-W16-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel
  file below. Each row's `surfaced_at` is the output of `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type
  a time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~16" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~16@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~16 <0.9.0_WK_IRPT_YCDGEN~16@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_dead_letter_record.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_package_poll.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~16/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-d-13.worker-stamps-cause-claim-measured.md
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R13.md</decomp_doc> round 13, cell `YCD-d-13`.
<owned_cells>YCD-d-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: D13-AC1, D13-AC2. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~16/IRPT_YCDGEN.TO-YCD-d-13.worker-stamps-cause-claim-measured.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-d-13`.
- Each criterion's `output_evidence` BEGINS with the check's own OK line. `artifacts_produced.commit_or_etag` is the hash of
  your code commit, never a placeholder: commit the code first, then write the proof.
- Validate with `python .tools/proof-of-spec-check.py <instance> D13-AC1,D13-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~15/IRPT_YCDGEN.TO-YCD-e-11.dead-lettered-job-states-its-failure.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the changed line of the record function, and the journal line shown unchanged;
- what each of the two repaired tests now binds, and whether building the runtime read any secret;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one dict literal in _record_deliveries_exhausted of ycharts/generate/resident_worker.py gains one member; the function runs only for an analysis_generate message whose handler raises at the fifth receive. Readers of a job's detail: 8, none exact on a FAILED detail (r13/CONDITION1_READERS_OF_A_JOBS_DETAIL_20261011.md @a7223f76aa). Two test files change. Ships only in resident release st32 under its own pair; nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the worker already writes its job row.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read _record_deliveries_exhausted (lines 810-841 at HEAD), the 2 detail assertions of test_dead_letter_record.py, the 2 failing tests of test_package_poll.py and resident_installed.py lines 96-107; denominator: 1 writer of DELIVERIES_EXHAUSTED in the tree (native search), 8 readers of a detail. NOT seen: whether building the packager port reads a secret at build (the order makes that a row). Traps: adding the member to the journal line a reader parses; a second writer of cause_claim; the worker writing `inferred`; repairing the two tests by weakening the runtime's refusal.
lane: ycharts/generate/resident_worker.py -- the resident worker; if the owned-paths gate names another project's lane the worker stops and the issuer re-points.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 5179 (st32's packet carries: the worker stamps cause_claim "measured"); IRPT_YCDGEN PRD
ADDENDUM v0.12 @aa4a647f6e ("that is one line in the worker and rides st32"), ratified-text half signed @ff5dff8c74; row
IRPT_YCDGEN-D2-S57 (the two stale tests).
