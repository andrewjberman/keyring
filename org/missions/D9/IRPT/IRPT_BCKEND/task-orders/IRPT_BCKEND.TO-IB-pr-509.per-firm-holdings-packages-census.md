# TO IRPT_BCKEND.TO-IB-pr-509 -- READ-ONLY census of the per-firm holdings packages the runner host installs (row D2-W359-S1; CTO round-176 analysis section 1 and section 2 item 1)

<to_id>IRPT_BCKEND.TO-IB-pr-509</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~361</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>176</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-176 ANALYSIS (msg 6844) section 1 (row D2-W359-S1) and section 2 item 1, and RE 6838 | **Decomp cell:** `IB-pr-509` (decomposition section 168) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-509` (inlined):** the 49 Financial and Inflection builders (`holdings_49f.py`, `holdings_inf.py`) run on the runner host from a per-firm package, not from the directory bundle. Round 175's census (`deliverables/0.9.0_WK_IRPT_BCKEND~359/IB175-1_host_bundle_census.json`) read the directory bundle (12 members) and showed the builders are not in it; they reach the host in `investor-reporting-holdings.tar.gz`, one copy per firm, fetched by `infra/aws/lambda/investor-reporting/holdings_refresh/refresh_dispatch.py:65` from a URI the environment variable `IRPT_HOLDINGS_BUNDLE_MAP` names (set on the Lambda `irpt-holdings-refresh-lambda`) and run at `:75` (`holdings_snapshot.py --firms <firm> --upload`). The deploy guard `.tools/safe_deploy_core.py` builds these packages: `_irpt_holdings_bundles()` (about `:545`) makes ONE bundle per firm in `holdings_snapshot.BUILDERS`, each keyed by `lib/opal_naming.address()` output, with the closure `_IRPT_HOLDINGS_CLOSURE` (about `:489`, 19 listed members plus the import closure the guard computes) and object name `_IRPT_HOLDINGS_OBJECT = "investor-reporting-holdings.tar.gz"` (about `:538`). **Nobody has read the live packages.** The next release (the 49F temp-file fix and the builder's `account_id`) must name exactly the packages and members it needs, every other member at today's bytes. **Read, and record.** READ ONLY: no upload, no SSM command, no host start, no deploy, no write to any AWS service. Allowed AWS calls: `lambda get-function-configuration` of `irpt-holdings-refresh-lambda` (to read `IRPT_HOLDINGS_BUNDLE_MAP`; NO other variable's value goes in any file), `s3api head-object` and `s3 cp` of each package TO a scratch directory OUTSIDE the repository (a read of code, not client data), and `ec2 describe-instances` / `ssm describe-instance-information` only to say what the host is (state only). No client data is read; counts, hashes and commit ids only.

**Do:**
1. **The map and the guard.** Read `IRPT_HOLDINGS_BUNDLE_MAP` (its value is a firm-to-S3-URI map: record the firm names and the bucket/key of each, no other variable) and compare each entry with the key the guard's `_irpt_holdings_bundles()` computes for that firm (call the function, or run its logic, against HEAD; read-only). Record `bundle_map.source` (file and line that reads the variable) and `bundle_map.agrees_with_guard` (true only if every firm's key equals the guard's). Print the denominator: the firms in `holdings_snapshot.BUILDERS` (parse it as the guard does) against the entries in the map.
2. **Each package.** For EVERY firm in `BUILDERS`: `head-object` its package (record `etag`, `last_modified`, `content_length`, `version_id` if versioned), download it to scratch, list its members (name, size, sha256), and record the object's own sha256. Read the stamped manifest member if the package has one and record what it says about its source commit (a commit id and nothing else).
3. **Member by member against HEAD.** For EVERY member of each package: `name`, `repo_path` (the repository file it comes from, or `null` with a `note`), `live_member_sha256`, `head_member_sha256` (sha256 of `git show HEAD:<repo_path>`; add `head_member_sha256_lf_normalised` only if the live tar stores LF and your tree CRLF), `equal`, and for each member with `equal` false `commits_since_live` = the short ids of the commits since the package's `last_modified` that touched `repo_path` (at most 12, newest first). `members_differing` per package = the count of rows with `equal` false. Check that every member of the guard's closure appears in each package's rows.
4. **Where the two merged changes land.** For `temp_file_fix` (commit `135fc3509e`: `holdings_49f.py`, `holdings_inf.py`, `holdings_snapshot.py`) and `account_id_builder` (commit `7ace854890`: `holdings_49f.py` and `holdings_snapshot.py`, with the schema copy `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` that the builder validates against): record `fix_locations` entries `{"change":"temp_file_fix"|"account_id_builder","repo_path":"<the main file>","commit":"<id>","in_closure":true|false,"differs_in_firms":[firm ids whose package differs from HEAD in that file]}`. Then say in a short `reading` string which differing members the two changes explain and which they do not (list; the issuer decides what is intended).
5. **Write the record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~361/IB176-1_holdings_packages_census.json`:
`{"packages":[{"firm_id":"...","bucket":"...","key":"...","etag":"...","etag_after":"<head-object ETag read again at the end>","last_modified":"...","content_length":N,"object_sha256":"...","manifest_source_commit":"...","members":[...],"members_differing":M}],"denominator":{"firms_in_builders":N,"packages_read":N,"entries_in_bundle_map":N},"bundle_map":{"source":"file:line","agrees_with_guard":true},"fix_locations":[...two entries...],"reading":"...","aws_writes_made":0,"objects_uploaded":0,"functions_invoked":0,"ssm_commands_sent":0,"hosts_started":0,"accounts_written":0,"figures_written":0}`. The record carries no variable value other than the bundle map's firm names and S3 keys, and no long digit run.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB176-1-AC1" cell_refs="IB-pr-509"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r176/p176_cells.py" . IB176-1-AC1</invocation><expect>IB176-1-AC1 PASS</expect></criterion>
<criterion id="IB176-1-AC2" cell_refs="IB-pr-509"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r176/p176_cells.py" . IB176-1-AC2</invocation><expect>IB176-1-AC2 PASS</expect></criterion>
<criterion id="IB176-1-AC3" cell_refs="IB-pr-509"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r176/p176_cells.py" . IB176-1-AC3</invocation><expect>IB176-1-AC3 PASS</expect></criterion>

<expected_criteria>IB176-1-AC1, IB176-1-AC2, IB176-1-AC3</expected_criteria>

What the checks grade: AC1 the packages are exactly the firms in `BUILDERS`, the denominators agree, every member row's `equal` flag agrees with its two hashes, `members_differing` equals the rows with `equal` false; AC2 the check re-hashes `git show HEAD:<repo_path>` for every member with a `repo_path` and compares, requires the guard's whole closure in each package's rows, and `commits_since_live` on every differing member; AC3 `fix_locations` names exactly `temp_file_fix` and `account_id_builder` with a repo path, a commit, `in_closure` and `differs_in_firms`, the bundle map agrees with the guard, the seven bound counters read 0, every package's `etag_after` equals its `etag`, and no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the scratch directory outside the repository (delete what you downloaded at the end, file by file), and the read-only AWS calls above. No upload, no copy to any bucket, no SSM command, no host start or stop, no deploy, no Lambda invoke, no vendor call, no edit of any file outside your folder.
- **Refusal clause:** STOP, file a row, change nothing more, if a package cannot be read with the Opal principal in this session, if the bundle map names a key the guard does not compute (record both and stop), if a package holds a member you cannot attribute to a repository file and cannot name, or if you find yourself needing any write.
- **Row ids** are `IRPT_BCKEND-D2-W361-S<k>` (the next free `k`). **Commit** on your worktree branch per your definition with `.tools/safe-commit.sh`; ASCII only. Report once, under 150 words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~361/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-509.per-firm-holdings-packages-census.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 168 (round 176, workstream ~P), cell `IB-pr-509`.
<owned_cells>IB-pr-509</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB176-1-AC1, IB176-1-AC2, IB176-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~361/IRPT_BCKEND.TO-IB-pr-509.per-firm-holdings-packages-census.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- read-only: the order reads the per-firm package objects of host code and one Lambda's environment variable and writes nothing; the packages' members and the host that installs them are what the order records.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; read calls only under the session's existing principal.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched and the host is not started.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p176_cells.py dry-run at base on dell2 2026-10-13 ~07:3xZ: IB176-1 AC1, AC2, AC3 FAIL (no record). Positive control: a synthetic record naming the three BUILDERS firms (49financial, inflection, cottonwood) with the guard's 45 closure members at HEAD hashes passes all three.
lane: the paths block IS the grant; worker slot ~361 of IRPT_BCKEND. Class SERVED (a read of the packages that decide what the host runs).
</preflight>
