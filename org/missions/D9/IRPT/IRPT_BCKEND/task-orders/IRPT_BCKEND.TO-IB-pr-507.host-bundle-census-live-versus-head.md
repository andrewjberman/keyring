# TO IRPT_BCKEND.TO-IB-pr-507 -- READ-ONLY census of the investor-reporting host bundle: the live object against repository HEAD, member by member (CTO round-175 analysis section 3 item 1)

<to_id>IRPT_BCKEND.TO-IB-pr-507</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~359</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>175</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-175 ANALYSIS (msg 6829) section 2 and section 3 item 1 | **Decomp cell:** `IB-pr-507` (decomposition section 167) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-507` (inlined):** the builder's host bundle must carry two merged changes to the runner host: the 49F temp-file fix (`holdings_49f.py`, `holdings_inf.py`, `holdings_snapshot.py`) and the builder's `account_id` (merged in round 170). It lands at the host's next SCHEDULED Online, as a never-widen pair, and no seat starts the host for it. **Before that pair can be written, someone must know exactly what the live bundle holds and which members differ from HEAD.** The deploy guard (`.tools/safe_deploy_core.py`, `find_bundle("investor_reporting")`) declares the bundle as the S3 object `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` with TWELVE members (each has a `sha_metadata_key`): but `holdings_49f.py` and `holdings_inf.py` are NOT among those twelve, and nobody has read how they reach the host. **Read, and record.** READ ONLY: no upload, no SSM command, no host start, no deploy, no write to any AWS service. Allowed AWS calls: `aws s3api head-object` and `aws s3 cp` of that ONE object TO a scratch directory OUTSIDE the repository (a read of code, not client data), and `aws ec2 describe-instances` / `aws ssm describe-instance-information` only if you need them to say what the host is (state only). No client data is read; counts, hashes and commit ids only.

**Do:**
1. **The host's way of reading the bundle.** Find the code that runs on the runner host and fetches or unpacks this object (start from `infra/aws/lambda/investor-reporting/holdings_refresh/refresh_dispatch.py`, which sends the SSM command, and follow the command it sends; also `infra/aws/ec2/` runner scripts and `.tools/safe_deploy_core.py` for how the guard builds the tarball). Cite each site as `file`, `line` and an exact one-line `quote` in `host_reads_bundle.sites`; say in `host_reads_bundle.summary` (two sentences) how `holdings_49f.py` and `holdings_inf.py` reach the host if they are not among the twelve declared members (are they inside the tarball under another rule, or fetched separately?).
2. **The live object.** `head-object` it: record `etag`, `last_modified`, `content_length`, `version_id` if versioned, and the object's metadata `*-sha256` keys. Download it to scratch (outside the repo), list its members (name, size, sha256 of each), and record the object's own sha256.
3. **Member by member against HEAD.** For EVERY member of the live tar (all of them, not only the twelve): `name`, `repo_path` (the repository file it comes from, or `null` with a `note` if it has none), `live_member_sha256`, `head_member_sha256` (sha256 of `git show HEAD:<repo_path>`; if the live tar stores LF and your working tree has CRLF, hash the blob, and add `head_member_sha256_lf_normalised` only if you must), `equal` (true iff the two hashes are equal), and for each member with `equal` false: `commits_since_live` = the short ids of the commits since the object's `last_modified` that touched `repo_path` (`git log --since=<last_modified> --format=%h -- <repo_path>`), at most 12, newest first. Also record any file the guard declares that is NOT in the live tar (`declared_but_absent_in_tar`).
4. **Write the record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~359/IB175-1_host_bundle_census.json`:
`{"live_object":{"bucket":"opal-data-mdpf","key":"...","etag":"...","last_modified":"...","content_length":N,"object_sha256":"...","metadata_sha256_keys":{"holdings-snapshot-sha256":"..."}},"etag_after":"<head-object ETag read again at the end>","members":[...],"denominator":{"members_in_live_bundle":N,"members_differing":M},"declared_but_absent_in_tar":[],"host_reads_bundle":{"summary":"...","sites":[{"file":"...","line":N,"quote":"..."}]},"aws_writes_made":0,"objects_uploaded":0,"functions_invoked":0,"ssm_commands_sent":0,"hosts_started":0,"accounts_written":0,"figures_written":0}`
5. **Then state, in a short `reading` string in the record, which differing members the two merged changes explain and which they do not** (the issuer decides what is intended; do not judge, list).

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB175-1-AC1" cell_refs="IB-pr-507"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r175/p175_cells.py" . IB175-1-AC1</invocation><expect>IB175-1-AC1 PASS</expect></criterion>
<criterion id="IB175-1-AC2" cell_refs="IB-pr-507"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r175/p175_cells.py" . IB175-1-AC2</invocation><expect>IB175-1-AC2 PASS</expect></criterion>
<criterion id="IB175-1-AC3" cell_refs="IB-pr-507"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r175/p175_cells.py" . IB175-1-AC3</invocation><expect>IB175-1-AC3 PASS</expect></criterion>

<expected_criteria>IB175-1-AC1, IB175-1-AC2, IB175-1-AC3</expected_criteria>

What the checks grade: AC1 the record's arithmetic (the denominator equals the member rows and the differing rows; every hash is 64-hex; each `equal` flag agrees with its two hashes; the live object fields present); AC2 the check re-hashes `git show HEAD:<repo_path>` for every member that has a `repo_path` and compares, requires all twelve guard-declared members to appear, and requires `commits_since_live` on every differing member; AC3 at least one cited host-read site resolves (file exists, quote within 3 lines of the line), the seven bound counters read 0, `etag_after` equals the live ETag, and the record carries no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the scratch directory outside the repository (delete what you downloaded at the end, file by file), and the read-only AWS calls above. No upload, no copy to any bucket, no SSM command, no host start or stop, no deploy, no Lambda invoke, no vendor call, no edit of any file outside your folder.
- **Refusal clause:** STOP, file a row, change nothing more, if the object cannot be read with the Opal principal in this session, if the live tar holds a member you cannot attribute to a repository file and cannot name (say which), or if you find yourself needing any write.
- **Row ids** are `IRPT_BCKEND-D2-W359-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~359/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-507.host-bundle-census-live-versus-head.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 167 (round 175, workstream ~P), cell `IB-pr-507`.
<owned_cells>IB-pr-507</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB175-1-AC1, IB175-1-AC2, IB175-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~359/IRPT_BCKEND.TO-IB-pr-507.host-bundle-census-live-versus-head.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- read-only: the order reads one S3 object of host code and writes nothing; the bundle's members and consumers are what the order records.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; read calls only under the session's existing principal.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched and the host is not started.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p175_cells.py dry-run at base on dell2 2026-10-13 ~07:0xZ: IB175-1 AC1, AC2, AC3 FAIL (no record). Positive control: a synthetic record naming the twelve guard members with HEAD hashes passes AC1 and AC2; AC3 rejects an all-digit hash by design (a real sha256 cannot trigger it).
lane: the paths block IS the grant; worker slot ~359 of IRPT_BCKEND. Class SERVED (a read of the object that decides what the host runs).
</preflight>
