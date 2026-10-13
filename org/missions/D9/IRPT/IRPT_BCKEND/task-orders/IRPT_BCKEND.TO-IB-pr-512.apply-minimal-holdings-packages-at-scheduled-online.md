# TO IRPT_BCKEND.TO-IB-pr-512 -- APPLY the signed host-bundle pair: put the two minimal holdings packages at the runner host's next SCHEDULED Online, digest-gated, then the first read (CTO RE 6867; pair IB-pr-510 signed by both halves at packet sha256 c2b7275939d0)

<to_id>IRPT_BCKEND.TO-IB-pr-512</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>178</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's RE 6867 ("cut the apply order with that step") on the round-177 slug, the round-176 and round-177 analyses (apply at the runner host's next SCHEDULED Online; no start for it), and the signed pair: COO half `deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_510_MINIMAL_HOLDINGS_PACKAGES_COO_HALF.md`, CTO half `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_510_MINIMAL_HOLDINGS_PACKAGES_CTO_HALF.md` | **Decomp cell:** `IB-pr-512` (decomposition section 170) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-512` (inlined):** two per-firm S3 objects hold the code the runner host runs to build holdings snapshots: `s3://opal-data-49financial/irpt/49financial/code/gold/investor-reporting-holdings.tar.gz` and `s3://opal-data-inflection/irpt/inflection/code/gold/investor-reporting-holdings.tar.gz` (cottonwood's object is NOT in this apply). Both halves of the never-widen pair have signed replacing them with two minimal candidate packages (the live bytes plus only the temp-file fix and, for 49financial, the `account_id` builder), built and censused in round 177. **This order APPLIES them, once, at the host's next SCHEDULED Online, and then reads the host's leftover temp-file counts.** The packet `deliverables/0.9.0_WK_IRPT_BCKEND~362/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-510.md` (sha256 `c2b7275939d05d633220c29450e7c75574f5bb92276aaa65911866560ebddaca`: re-hash it first; a different sha256 means STOP) is your procedure: its tables carry the live ETags, VersionIds and sha256 values, the candidate sha256 values, the metadata stamps and Branches A and B. The record `deliverables/0.9.0_WK_IRPT_BCKEND~362/IB177-1_candidate_packages.json` carries the same values as data, and `deliverables/0.9.0_WK_IRPT_BCKEND~362/pack_candidate_package.py` with `candidate/<firm>/` rebuilds each candidate from its live object. **No seat starts the host for this order. You may not start it, wake it, or ask anyone to.**

**Do, in this order:**

0. **STEP 0 (now; READ ONLY; before anything is written).** The 49 Financial holdings run does NOT use the host's own role: by design it ASSUMES the firm's own principal, whose name carries the firm's scope token (`infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf` header, items 1 and 2; `refresh_dispatch.py`), so the bucket fence admits it. The CTO read the fence at ~08:3xZ (RE 6867 and the round-178 analysis): `opal-data-49financial`'s policy (34 statements) carries `DenyForeignFirmPrincipals`, which admits `role/*-49f-*` plus a named list; two `PutBucketPolicy` writes by `cloudops-dell1-agent-user` landed there on 2026-10-11 (15:27Z and 16:07Z), after the package was written. **Confirm, for EACH of the two firms (`49financial`, `inflection`), before any write:** (a) the per-firm principal the run assumes EXISTS (name it: `run_principal`); (b) the host's role can ASSUME it (`assume_ok`: read the principal's trust policy, or `iam simulate-principal-policy` for `sts:AssumeRole`; you cannot assume it as the host, so say which you did); (c) that principal is ALLOWED, by `iam simulate-principal-policy` and the bucket policy's deny statements read together, to `s3:GetObject` the package key and to `s3:PutObject` the builder's gold keys of that firm (the keys the run writes; read them from `holdings_snapshot.py` / `directory/holdings_refresh.tf`); (d) YOUR principal may `s3:PutObject` the package key (simulate; the bucket policy's deny statements read for it). Record per firm `runner_role_admitted` (true only if (a), (b), (c) hold) with `run_principal`, `assume_ok`, and the Sids that admit it; no policy text beyond Sids and principal ARNs; and `apply_principal_may_put`. **If any firm fails (a) to (d): STOP. Write nothing, apply nothing, report to the issuer; the policy then goes to ADVI_FIRMBKTS through `0.0.0_AB_MSTR`.**
1. **The schedule (now; READ ONLY).** Find how the runner host comes Online on a schedule (the EventBridge rules and Lambdas that start it: start from `infra/aws/lambda/smartx-ec2-autostart`, `infra/aws/terraform/investor-reporting/directory/schedule.tf` and the holdings refresh schedule; `events list-rules`, `ec2 describe-instances` state) and compute `next_scheduled_online_utc` and its `source` (file and line, or the rule name). **Send the issuer ONE message (under 150 words) with that fact and the instance's current state,** then go on.
2. **Wait for the scheduled Online, without starting anything.** Poll read-only (`ec2 describe-instances` state; `ssm describe-instance-information` PingStatus) at a sensible interval (every 10 minutes is enough) until the host is Online. When it is, read who started it (`cloudtrail lookup-events` `EventName=StartInstances` for that instance, around the transition) and record `started_by`: `scheduler` if the principal is the schedule's own (an EventBridge rule target or the autostart Lambda's role), otherwise `other` with the principal NAME. **If `started_by` is not `scheduler`: do not apply; report to the issuer and wait for a ruling.** If the host has not come Online within 48 hours of this order, report to the issuer (do not start it).
3. **Open the NEVER-2 ledger entry** under `org/critical_paths/change_management/` (your usual form) BEFORE the first write, naming both keys, both rollback VersionIds (49financial `fMLoOI6a8ZwNFWZCJjjP90ZadyRg9nFg`, inflection `qR5sZza4EjUT_cbGA5hLo0ar6zu2NfpI`), and this order.
4. **Branch A of the packet, one firm at a time, 49financial first, then inflection:** (1) START READ: `head-object` ETag and VersionId must equal the packet's live values; download that VersionId to scratch OUTSIDE the repository; its sha256 must equal the packet's live object sha256, else STOP; (2) rebuild the candidate with `python -I pack_candidate_package.py <firm> <live tar> candidate/<firm> <out>`; its sha256 must equal the packet's candidate package sha256, else ABORT; (3) `s3api put-object` to the same key with `--server-side-encryption AES256 --metadata members-sha256=<the packet's candidate stamp>,member-count=44`; (4) READ BACK: `head-object` shows a NEW VersionId, and a download of the new version hashes to the candidate package sha256 and carries the candidate metadata. Only then the next firm. **Never write cottonwood's key.** Record cottonwood's ETag before and after (unchanged).
5. **On any trigger of Branch B** (a read-back that disagrees; a refresh failure; a `TypeError` or 5xx; a figure that differs): restore that firm's live VersionId by `s3api copy-object` with the live metadata, read back, and report at once; set `rollback_performed` true in the record.
6. **The first read, on the host (it is Online now), READ ONLY:** one SSM Run Command per firm's pattern that COUNTS leftover files: `*-taxsma_workbook_projected_snapshot.json` (49financial) and `*-membership_map.json` (inflection) in the host's temp folder (count with `find ... | wc -l`; print the number only; no names, no contents, no age beyond a count; NO delete). A non-zero count is reported; a person deletes the files; you do not. Then, if the host's holdings refresh runs while you are watching, read its `sha256sum -c` result from the log group (a pass/fail line only).
7. **Close the ledger entry; write the record** `deliverables/0.7.0_AE_CloudOps~IB2/IB178-1_apply_record.json`:
`{"step0":{"bucket_policies":[{"firm_id":"49financial","bucket":"opal-data-49financial","run_principal":"<name>","assume_ok":true,"runner_role_admitted":true,"statement_ids":"...","apply_principal_may_put":true},{"firm_id":"inflection",...}]},"schedule":{"next_scheduled_online_utc":"...","source":"...","host_online_observed_at":"...","started_by":"scheduler","start_principal":"<name>"},"ledger_entry":"org/critical_paths/change_management/<file>","applies":[{"firm_id":"49financial","start_read":{"etag":"...","version_id":"...","sha256":"..."},"candidate_sha256":"...","put":{"new_version_id":"...","new_etag":"..."},"readback":{"version_id":"...","sha256":"...","metadata":{"members-sha256":"...","member-count":"44"}}},{"firm_id":"inflection",...}],"cottonwood_untouched":{"etag_before":"...","etag_after":"..."},"rollback_performed":false,"first_read":{"command_run":"find <temp folder> -name '<pattern>' | wc -l","temp_file_counts":{"49financial":0,"inflection":0}},"objects_uploaded":2,"hosts_started":0,"functions_invoked":0,"accounts_written":0,"figures_written":0,"files_deleted":0}`. The record carries no path beyond the ledger entry, no file name found on the host, no long digit run.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IB178-1-AC1" cell_refs="IB-pr-512"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r178/p178_cells.py" . IB178-1-AC1</invocation><expect>IB178-1-AC1 PASS</expect></criterion>
<criterion id="IB178-1-AC2" cell_refs="IB-pr-512"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r178/p178_cells.py" . IB178-1-AC2</invocation><expect>IB178-1-AC2 PASS</expect></criterion>
<criterion id="IB178-1-AC3" cell_refs="IB-pr-512"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r178/p178_cells.py" . IB178-1-AC3</invocation><expect>IB178-1-AC3 PASS</expect></criterion>

<expected_criteria>IB178-1-AC1, IB178-1-AC2, IB178-1-AC3</expected_criteria>

What the checks grade: AC1 step 0 admitted the per-firm run principal on both buckets (named, assume ok, with the Sids), the schedule fields are present and `started_by` reads `scheduler`, and the ledger entry exists under `org/critical_paths/change_management/` and names both rollback VersionIds; AC2 for 49financial and inflection the start read equals the packet's live VersionId and sha256, the rebuilt candidate equals the packet's candidate sha256, the put made a NEW VersionId, the read-back of that version hashes to the candidate and carries the candidate `members-sha256` (found in the packet) and `member-count` 44, cottonwood's ETag is unchanged and `rollback_performed` is false; AC3 the first-read counts are integers for both firms from a read-only command, no path or long digit run, and the counters read `objects_uploaded` 2, `hosts_started` 0, `functions_invoked` 0, `accounts_written` 0, `figures_written` 0, `files_deleted` 0. Do not edit the checks. If the apply STOPS (step 0, the digest gates or `started_by`), the criteria are not run; report the stop and its reason to the issuer.

## BOUNDS

- **Grant:** the two keys named above and nothing else for writes (`put-object` each once, `copy-object` only for Branch B), the ledger entry, and your record folder. Reads: bucket policies, IAM simulate, EC2/SSM state, CloudTrail lookup, EventBridge rules, the log group's `sha256sum -c` line, and one read-only SSM Run Command per firm for the counts. **No host start, stop or wake; no cottonwood write; no deletion of any file on the host or in S3; no Lambda invoke; no figure or account written.**
- **Refusal clause:** STOP and report, writing nothing further, on any of: the packet's sha256 differs; step 0 finds a bucket that does not admit the runner role; your principal cannot put; a live ETag, VersionId or sha256 differs from the packet; a candidate rebuild differs from the packet's sha256; `started_by` is not `scheduler`; a read-back disagrees (then Branch B). A STOP is reported, not worked around.
- **Row ids** are `IRPT_BCKEND-D2-IB2-S<k>` (the next free `k`); file a row for anything odd and keep working. **Report once at the end, under 150 words**, plus the one message of step 1.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/critical_paths/change_management/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-512.apply-minimal-holdings-packages-at-scheduled-online.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 170 (round 178, workstream ~P), cell `IB-pr-512`.
<owned_cells>IB-pr-512</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB178-1-AC1, IB178-1-AC2, IB178-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-512.apply-minimal-holdings-packages-at-scheduled-online.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the two objects' only consumer is the runner host's holdings refresh (refresh_dispatch.py:65 fetches, :75 runs); the candidates are the live bytes plus the signed hunks; cottonwood's object is not written. The pair (IB-pr-510) carries the blast radius, Branch B and the rollback per key.
comp-iam: RUN -- no permission is changed; step 0 READS both bucket policies and simulates the apply principal's PutObject before any write; two PutBucketPolicy writes by another fabric's agent user on opal-data-49financial (2026-10-11) are why.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created; the apply is gated on the host's existing scheduled Online and the order forbids starting, stopping or waking the host.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p178_cells.py dry-run at base on dell2 2026-10-13 ~08:5xZ: IB178-1 AC1, AC2, AC3 FAIL (no record). Positive control: a synthetic apply record built from the IB-pr-510 record's live and candidate values and the packet's stamp passes all three (record and test ledger removed).
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (live, idle, holds no other IRPT_BCKEND order; the parked IB-pr-497 is a read of the same host, closed by the CTO's RE). Class WORLD.
</preflight>
