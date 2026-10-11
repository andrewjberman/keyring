# TO IRPT_BCKEND.TO-IB-pr-455 -- BUILD, nothing released: the submission admits the optional boolean `commentary_requested`; acceptance copies it into the record only when sent

<to_id>IRPT_BCKEND.TO-IB-pr-455</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~311</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>151</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5863 (IRPT_YCDGEN PRD v0.13 @e31454a778, signed @6f8aeb03b7) | **Decomp cell:** `IB-pr-455` (decomposition section 143) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-311/` (bash `/c/dev/wk-irpt-bckend-311`), cut at the issuance commit on box/dell2, which CONTAINS
`2.0.0_SA_COO~G2`'s worker half (`resident_worker.py`: `analysis_ready` only with a ticket id AND `commentary_requested` exactly
true). Work only there. No AWS call, no network call, NO DEPLOY, no terraform, no source-map edit: this cell changes code,
tests and one contract file in the tree. Its release is a later act under its own signed pair.

**The contract.** Read `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` ADDENDUM v0.13 (its last section) whole. In
short: whether commentary was asked for is the CALLER's statement, made once in the submission and carried. The submission's
closed set gains ONE optional boolean, `commentary_requested`; acceptance copies it into the accepted record ONLY when it was
sent; absent stays absent (the worker reads absent as false, so every earlier record and every caller that does not send it
behave exactly as today).

**Build, in these files only:**
1. `infra/aws/lambda/investor-reporting/ycharts/generate/submission.py`: `PUBLIC_FIELDS` admits `commentary_requested`
   (line 16 today). In `validate_public_request`, when the member is present it must be exactly `True` or `False` (`type(x) is
   bool`: the integers 1 and 0, the strings, `None`, a list, an object and a float are all REFUSED), with ONE new refusal code,
   `COMMENTARY_REQUESTED`, raised as `SubmissionRefused`. An unknown member is still refused `UNKNOWN_OR_SERVER_OWNED_FIELD`.
   Do NOT bind it to `ticket_id` here (the PRD puts the ticket condition in the worker; if the addendum says otherwise, follow
   the addendum and say so in a row). A submission without the member validates to exactly what it does today.
2. `infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py`: in `accept`, beside the existing
   `if "ticket_id" in browser: record["ticket_id"] = browser["ticket_id"]` (about line 121), copy `commentary_requested` into
   `record` when and only when `"commentary_requested" in browser`. Nothing else in the record changes; a prior record is
   still returned exactly as stored (read `lookup` and say in your report what a REPLAY of the same `request_id` with a
   different `commentary_requested` returns: the code decides, you report it; do not change replay behaviour).
3. `docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json`: declare `commentary_requested` as
   `{"type": "boolean", "description": ...}` in `properties`; the object stays `additionalProperties: false`; the member is NOT
   added to `required`. If any OTHER file in this repository is a copy of that schema or enumerates the submission's members
   (search with the native Grep tool for `AnalysisSubmissionRequest` and for the member list; `routes.json`,
   `REQUEST_COMPOSITION.md`, `RequestComposition.schema.json`, `_scope/maintained_sources.py` name it today), read each and
   change ONLY those that would refuse or drop the member; list every one you read and what you did in your report. The
   portal's vendored copy is NOT yours (another seat moves it with the form).
4. Tests, new file `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_commentary_requested_member.py` (follow
   `test_acceptance_actor.py` for how acceptance is exercised offline with its fake client): the member admitted as true and
   as false; each wrong type refused with `COMMENTARY_REQUESTED`; an unknown member still refused; acceptance writes the member
   into the record when sent (true, and false) and omits it when not sent; the record without the member is equal, member for
   member, to the record the same submission produced before this change (`browser_sha256` included: it is the digest of the
   validated submission, so it differs ONLY when the member is sent; assert both directions); a replay returns the prior
   record. The test also WRITES `tests/commentary_requested_records.json`: an object with exactly the keys `sent_true`,
   `sent_false`, `not_sent`, each the accepted `record` (the decoded JSON acceptance stored) for the same planted submission
   sent three ways, with `browser_sha256` and `accepted_at` REMOVED from each (so the three differ only by the member).
   Commit that file; it is synthetic (planted ids, no firm name, no real account).

<criterion id="IB151-1-AC1" cell_refs="IB-pr-455"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r151/p151_cells.py" . IB151-1-AC1</invocation><expect>IB151-1-AC1 PASS</expect></criterion>
<criterion id="IB151-1-AC2" cell_refs="IB-pr-455"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r151/p151_cells.py" . IB151-1-AC2</invocation><expect>IB151-1-AC2 PASS</expect></criterion>
<criterion id="IB151-1-AC3" cell_refs="IB-pr-455"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r151/p151_cells.py" . IB151-1-AC3</invocation><expect>IB151-1-AC3 PASS</expect></criterion>

<expected_criteria>IB151-1-AC1, IB151-1-AC2, IB151-1-AC3</expected_criteria>

AC1 is the built behaviour (the issuer's cases on the validator, and your test file). AC2 is the seam: the public contract and
the record acceptance writes. AC3 is the CONTROL and passes today: a submission without the member validates to itself, and
the existing acceptance, submission and worker-gate tests still pass. It must still pass when you finish.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No deploy, no terraform, no source-map edit, no portal file.
- **Refusal clause:** if the addendum and this face disagree, if a copy of the schema you may not edit would refuse the member,
  or if a criterion cannot be met as written: stop, file a row and report. Never weaken a check; do not edit `p151_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W311-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- Every `.py` passes `bash .tools/commit-gate.sh <file>` before the commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~311" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~311@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~311 <0.9.0_WK_IRPT_BCKEND~311@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/submission.py
infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_commentary_requested_member.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/commentary_requested_records.json
docs/contracts/investor-reporting/v1/
infra/aws/lambda/investor-reporting/_scope/maintained_sources.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~311/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-455.submission-admits-commentary-requested.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 143 (round 151, workstream ~P), cell `IB-pr-455`.
<owned_cells>IB-pr-455</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB151-1-AC1, IB151-1-AC2, IB151-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~311/IRPT_BCKEND.TO-IB-pr-455.submission-admits-commentary-requested.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the lines changed in each file; every file naming the schema or the member list that you
read, and what you did with each; what a replay with a different `commentary_requested` returns; which Lambda functions package
`submission.py` and `acceptance.py` (read `infra/aws/lambda/ci/lambda-source-map.json`, names only: the release pair needs
them); the test count; each criterion's last line; the commit gate's and the proof checker's results; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell edits two source files, one contract file and adds tests in the tree; nothing is built, packaged or deployed. The blast radius of the RELEASE is the release pair's to name (every function packaging the two files, every reader of the accepted record).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change and no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is added or moved; routes.json is read and edited only if it would refuse the member.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p151_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~21:3xZ: AC1 FAIL as expected (the member is refused UNKNOWN_OR_SERVER_OWNED_FIELD), AC2 FAIL as expected (the schema does not declare it), AC3 PASS as expected (control: 19 passed, 20 skipped); commit-gate clean. The issuer read submission.py:1-91 and acceptance.py:84-140 at HEAD and the schema's member list. The reader census of the accepted record (IB-pr-453, 50 readers) is at a stale vintage (row IRPT_BCKEND-D2-S99) and is re-counted for the release pair, not relied on here. WORLD by the L6 floor (paths under infra/); nothing is released by this order.
lane: the <paths> block IS the grant.
</preflight>
