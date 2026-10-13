# TO IRPT_BCKEND.TO-IB-pr-511 -- READ-ONLY provenance of the three holdings package objects and the evidence archive of the four unattributed live members (row D2-W361-S3 (b) and (c); CTO round-177 analysis section 1)

<to_id>IRPT_BCKEND.TO-IB-pr-511</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~363</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>177</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-177 ANALYSIS (msg 6863) section 1 (row D2-W361-S3) and section 2 item 2 | **Decomp cell:** `IB-pr-511` (decomposition section 169) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-511` (inlined):** round 176's census (`deliverables/0.9.0_WK_IRPT_BCKEND~361/IB176-1_holdings_packages_census.json`) found four live members that equal NO blob in the repository's history: `49financial` `infra/logic/registry/reporting_policies.json` and `infra/logic/registry/resources.json`, and `inflection` and `cottonwood` `infra/logic/registry/resources.json` (rows flagged `"unattributed": true`). The CTO's ruling: the host-bundle pair carries these four UNCHANGED and does not block on them, and **one read-only provenance read** plus **an evidence archive** follow: (b) for each of the three package objects, the S3 object's metadata and the CloudTrail `PutObject` event at its `last_modified` (the principal and the session, no payload); for each of the four members, a line diff against its nearest historical blob (which commit, how many lines, what kind of change; code only, no client data); (c) the four live members' bytes archived as evidence under the project's deliverables with their sha256 and source package, so the live package can be rebuilt (and rolled back to) from the repository from now on. **READ ONLY: no AWS write, no upload, no host start, no deploy.** Allowed AWS calls: `s3api head-object`, `s3 cp` of the package objects to scratch OUTSIDE the repository (delete after), and `cloudtrail lookup-events` (read; `--lookup-attributes AttributeKey=ResourceName,AttributeValue=<the object key>` or `EventName=PutObject` filtered to the object, around the `last_modified`). Code and registry JSON only; no client data is in any of these members, and none is read.

**Do:**
1. **The four members.** Read the flagged rows from the census record (`unattributed` true). For each: extract it from its package (scratch), copy it to `deliverables/0.9.0_WK_IRPT_BCKEND~363/archive/<firm>/<repo_path with / as __>` byte for byte, and record `live_sha256` (equal to the census row's `live_member_sha256`).
2. **The nearest historical blob.** For each member, find in `git log` of its `repo_path` the blob that differs from the live bytes by the FEWEST changed lines (compare the live bytes against each historical blob of that path; line diff ignoring only end-of-line characters), record its commit as `nearest_blob_commit`, and the counts `lines_added` / `lines_removed` of `diff(nearest blob -> live)` (added = lines in live not in the blob), a `change_kind` in `comment`, `data`, `code`, `eol` or `mixed`, and a one-sentence `note` of what kind of change it is (for a registry JSON: which keys or entries differ, by name only).
3. **The provenance of the three objects.** For each BUILDERS firm: `head-object` its package key (from the census) and record its S3 metadata keys (names and values; if a value looks like a person's name or a secret, record its length only), and the CloudTrail `PutObject` event for that key at its `last_modified` (within 120 seconds): `event_time`, `event_name` `PutObject`, `principal` (the IAM role or user NAME and type, never an access key), `session_name` (the assumed-role session name if any), `user_agent_family` (for example `aws-cli`, `terraform`, `boto3`: the product name only, no version, no IP). If CloudTrail returns no event (history window, data events not logged), record `"event_found": false` with a `reason` and a `data_events_logged` reading if you can state it; do not guess a principal.
4. **Write the record** `deliverables/0.9.0_WK_IRPT_BCKEND~363/IB177-2_provenance_and_archive.json`:
`{"unattributed_members":[{"firm_id":"...","repo_path":"...","package_key":"...","live_sha256":"...","archived_file":"deliverables/0.9.0_WK_IRPT_BCKEND~363/archive/<firm>/<name>","nearest_blob_commit":"<id>","lines_added":N,"lines_removed":N,"change_kind":"...","note":"..."}],"cloudtrail":[{"firm_id":"...","package_key":"...","last_modified":"...","event_found":true,"event_name":"PutObject","event_time":"...","principal":"...","principal_type":"...","session_name":"...","user_agent_family":"..."}],"s3_metadata":{"<firm>":{"<key>":"<value>"}},"reading":"...","aws_writes_made":0,"objects_uploaded":0,"functions_invoked":0,"ssm_commands_sent":0,"hosts_started":0,"accounts_written":0,"figures_written":0}`. In `reading`, say in two sentences whether the four members look like a hand edit of a deployed file, a build from another tree, or something else, and what the nearest-blob counts support; the CTO rules on whether any is then committed as source.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB177-2-AC1" cell_refs="IB-pr-511"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r177/p177_cells.py" . IB177-2-AC1</invocation><expect>IB177-2-AC1 PASS</expect></criterion>
<criterion id="IB177-2-AC2" cell_refs="IB-pr-511"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r177/p177_cells.py" . IB177-2-AC2</invocation><expect>IB177-2-AC2 PASS</expect></criterion>
<criterion id="IB177-2-AC3" cell_refs="IB-pr-511"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r177/p177_cells.py" . IB177-2-AC3</invocation><expect>IB177-2-AC3 PASS</expect></criterion>

<expected_criteria>IB177-2-AC1, IB177-2-AC2, IB177-2-AC3</expected_criteria>

What the checks grade: AC1 the record names exactly the census' four unattributed rows, each with a commit id, integer counts and a `change_kind`; AC2 each archived file hashes to its recorded sha256 and to the census' `live_member_sha256`, and the check re-derives `lines_added` / `lines_removed` from `git show <nearest_blob_commit>:<repo_path>` against the archived file; AC3 one CloudTrail reading per `BUILDERS` firm (a `PutObject` event within 120 seconds of the package's `last_modified`, or `event_found` false with a reason) and the seven bound counters read 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the scratch directory (delete what you downloaded at the end, file by file) and the read-only AWS calls above. No upload, no copy to any bucket, no SSM command, no host start, no deploy, no Lambda invoke, no vendor call.
- **Refusal clause:** STOP, file a row, change nothing more, if a package cannot be read, if an archived member turns out to hold anything that looks like a credential, an account number or a person's name (archive nothing, name the path and the kind only), or if CloudTrail access is denied (record `event_found` false with that reason and continue with the rest).
- **Row ids** are `IRPT_BCKEND-D2-W363-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~363/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-511.package-provenance-read-and-evidence-archive.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 169 (round 177, workstream ~P), cell `IB-pr-511`.
<owned_cells>IB-pr-511</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB177-2-AC1, IB177-2-AC2, IB177-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~363/IRPT_BCKEND.TO-IB-pr-511.package-provenance-read-and-evidence-archive.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- read-only: the order reads three package objects, their S3 metadata and CloudTrail events, and archives four code/registry files into the repository; nothing is written to AWS.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; read calls only under the session's existing principal (CloudTrail lookup-events is a read).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched and the host is not started.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p177_cells.py dry-run at base on dell2 2026-10-13 ~08:1xZ: IB177-2 AC1, AC2, AC3 FAIL (no record). The census record it reads (IB176-1) names the four unattributed rows.
lane: the paths block IS the grant; worker slot ~363 of IRPT_BCKEND. Class SERVED (a read of the objects that decide what the host runs).
</preflight>
