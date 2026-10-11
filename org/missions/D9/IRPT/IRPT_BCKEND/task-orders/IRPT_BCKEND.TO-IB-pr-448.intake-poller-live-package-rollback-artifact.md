# TO IRPT_BCKEND.TO-IB-pr-448 -- the live irpt-intake-poller package held as the rollback artifact: find its version id among the artifact key's versions, or stop

<to_id>IRPT_BCKEND.TO-IB-pr-448</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>144</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5611 ("the live package's bytes are saved once as the rollback artifact, by an applier, version id recorded") | **Decomp cell:** `IB-pr-448` (decomposition section 136) | **outcome_ref:** FWD-9

---

## WORKER FACE

**Why.** Row `IRPT_ANLREQ-D2-W53-S3`: 21 of the 28 live members of `irpt-intake-poller` have no blob in git, so the tree cannot
rebuild what the function runs. Its rollback target is therefore the live package itself and nothing else. Until the poller
is released from the tree, that package must be held, once, at an address with a recorded version id.

**THIS ORDER WRITES NOTHING.** The artifact bucket is versioned if the function's own artifact key has versions; the live
package was uploaded there by the deploy that made it live. So the rollback artifact probably ALREADY EXISTS as one version
of that key. Find it by content. If it is not there, STOP: the address of a new copy is a naming-canon question
(`lib/opal_naming.py address()`), not yours to type, and the issuer cuts that as its own order.

**Steps, reads only (through `.tools/aws`):**
1. `lambda get-function-configuration` on `irpt-intake-poller`: record `CodeSha256` (`live_code_sha256`) and the read time.
2. The artifact address: read `artifact_s3_bucket` and `artifact_s3_key` from the function's entry in
   `infra/aws/lambda/ci/lambda-source-map.json` (key `irpt-intake-poller`); record where you read it
   (`artifact_bucket_and_key_from`). Do not type the address from memory.
3. `s3api get-bucket-versioning` on that bucket (record the status), then `s3api list-object-versions` for that exact key,
   auto-paginated (never `--no-paginate`); count client-side. For EACH version: `s3api get-object --version-id <id>` to a
   NEW EMPTY folder outside the repo, compute the base64 sha256 of the bytes, record `{version_id, last_modified, size,
   is_latest, content_sha256}` (a delete marker is listed with `content_sha256: null`). State `artifact_versions_count`.
4. **Outcome.** `FOUND`: exactly the version(s) whose `content_sha256` equals `live_code_sha256`; take the newest such as
   `rollback_artifact:{version_id, content_sha256, last_modified, size}`, re-read it with `s3api head-object --version-id`
   and set `re_read_by_head_object: true`. Also record whether the bucket has a lifecycle rule that expires NONCURRENT
   versions (`s3api get-bucket-lifecycle-configuration`; a NoSuchLifecycleConfiguration answer is "none"): state
   `noncurrent_expiry:{rule_present, days}`; a rule that would expire the found version is a row for the issuer, not an act.
   `NOT_FOUND`: no version carries the live digest; set `stopped_because` and report. Write nothing in either case.
5. Record every command you ran, in order, in `commands`.

**Bounds.** No put, copy, delete, update, publish, invoke, terraform or apply. No other function, no other key. The
downloaded bytes are data: hash them, never run them; remove the folder when done. No ledger entry is opened: nothing is
deployed and nothing moves.

**Output:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB144-2_poller_rollback_artifact.json` with
`{live_code_sha256, live_read_at_utc, artifact_bucket_and_key_from, bucket_versioning, artifact_versions:[...],
artifact_versions_count, outcome, rollback_artifact:{...}, noncurrent_expiry:{...}, stopped_because, writes_made:0,
commands:[...]}`.

<criterion id="IB144-2-AC1" cell_refs="IB-pr-448"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r144/p144_cells.py" . IB144-2-AC1</invocation><expect>IB144-2-AC1 PASS</expect></criterion>
<criterion id="IB144-2-AC2" cell_refs="IB-pr-448"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r144/p144_cells.py" . IB144-2-AC2</invocation><expect>IB144-2-AC2 PASS</expect></criterion>
<criterion id="IB144-2-AC3" cell_refs="IB-pr-448"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r144/p144_cells.py" . IB144-2-AC3</invocation><expect>IB144-2-AC3 PASS</expect></criterion>

<expected_criteria>IB144-2-AC1, IB144-2-AC2, IB144-2-AC3</expected_criteria>

Both outcomes pass the checks; which one holds is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else.
- **Refusal clause:** an AWS read refused, or a criterion that cannot be met as written: stop, file a row, report. Never
  weaken a check; do not edit `p144_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-S<n>` (next free at filing; check before you commit); `grounding.status` is `GROUNDED` or
  `INFERRED`; append only.
- Commit with `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~IB2 <0.7.0_AE_CloudOps~IB2@opal.agent>" -F <msgfile> -- <paths>`;
  message file by a non-shell writer; ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-448.intake-poller-live-package-rollback-artifact.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 136 (round 144, workstream ~P), cell `IB-pr-448`.
<owned_cells>IB-pr-448</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB144-2-AC1, IB144-2-AC2, IB144-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-448.intake-poller-live-package-rollback-artifact.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P2`, under 150 words: the outcome, the version id and its digest (or the stop), the
versions counted, the noncurrent-expiry reading, the three criteria's last lines, the commit hash and its push state.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes nothing: one function read, one bucket's versioning and lifecycle reads, one key's version list and downloads.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; the applier's existing read rights are used, and a refusal is a row.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p144_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~19:1xZ: IB144-2-AC1..3 FAIL (no record); commit-gate clean. The CTO's "saved once" is read narrowly: where a version of the artifact key already holds the live bytes, recording its version id IS the save and no second copy is made; where none does, the order stops and the copy's address is cut from the canon's builder in its own order. Declared WORLD although it writes nothing: it reads a live function and a served bucket through an applier.
lane: the <paths> block IS the grant. Assignee measured LIVE and idle at 19:0xZ (get_agent_status, liveness limb), on this project.
</preflight>
