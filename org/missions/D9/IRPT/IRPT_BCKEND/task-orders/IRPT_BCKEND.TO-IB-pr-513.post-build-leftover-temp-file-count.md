# TO IRPT_BCKEND.TO-IB-pr-513 -- ONE READ-ONLY count of leftover snapshot temp files on the runner host AFTER a real build that ran on the new packages (row D2-W345-S3; CTO RE 6992, round 179)

<to_id>IRPT_BCKEND.TO-IB-pr-513</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>179</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's RE 6992 on the round-178 slug ("round 179 = IB-pr-513, one read-only count after a build; today if Online, else the next scheduled Online") | **Decomp cell:** `IB-pr-513` (decomposition section 171) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-513` (inlined):** `TO-IB-pr-512` put the two minimal holdings packages (the temp-file fix) and its first read counted 0 and 0 leftover files at about 13:37Z, which was BEFORE any holdings build ran on the new packages. The holdings refreshes for all three firms ran at 14:15Z (SSM invocations `irpt holdings refresh <firm> 2026-10-13`, all `Success`, read by the issuer). The leak, if the fix had failed, shows AFTER a build. **PASS (the CTO's definition): 0 leftover Tax snapshot temp files after a build that ran on the new packages. The build is NAMED: its start time and the package digest it ran. Positive control: the build's own log line showing it took the snapshot path.** A driven build would write served output outside its schedule, so **no seat drives one: the count follows a REAL scheduled build.**

**Do:** (1) `ec2 describe-instances` for the host's state. If it is running: repeat the same two read-only counts now (`*-taxsma_workbook_projected_snapshot.json` for 49financial and `*-membership_map.json` for inflection in the host's temp folders; one SSM Run Command per firm printing the count only: `find ... | wc -l`; no names, no contents, no delete). **If the host has stopped, take NO count and do NOT start it: report `not measurable today` to the issuer, keep this order OPEN, and take the count after the next SCHEDULED build that follows a scheduled Online** (the same gates as `TO-IB-pr-512`: `started_by` scheduler; never a seat's start). (2) NAME the build the count follows: the 49financial holdings refresh invocation (`irpt holdings refresh 49financial <date>`), its start time (UTC), the package VersionId it fetched (it must equal the VersionId `TO-IB-pr-512` put, `UHOCIkWj3QiIzNucG1VjNnk_AufIg6oD` for the 14:15Z build) and that package's sha256 (the candidate package sha256 in the apply record), and the build's OWN log line showing it took the snapshot path (the line the builder prints when it reads the Tax membership snapshot through `retained_capture`; find it in the invocation's output or the holdings log group; quote it, and name the source). (3) Write `deliverables/0.7.0_AE_CloudOps~IB2/IB178-2_post_build_count.json`: `{"temp_file_counts":{"49financial":N,"inflection":N},"build":{"firm_id":"49financial","invocation":"<command id>","start_utc":"<UTC>","package_version_id":"...","package_sha256":"<64-hex>","snapshot_path_log_line":"<quoted line>","log_source":"<where>"},"last_build_finished_utc":"<UTC of the last holdings build before the read>","read_at_utc":"<UTC>","host_state_at_read":"running","ssm_status":"Success","command_run":"find /tmp /var/tmp -maxdepth 1 -type f -name '<pattern>' | sort -u | wc -l","command_run_literal":"<with any stderr redirect>","objects_uploaded":0,"hosts_started":0,"functions_invoked":0,"files_deleted":0,"aws_writes_made":0}`. `command_run` carries no `>` character. A non-zero count is reported and a person deletes any file; you do not.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IB178-2-AC1" cell_refs="IB-pr-513"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r178/p178_cells.py" . IB178-2-AC1</invocation><expect>IB178-2-AC1 PASS</expect></criterion>
<criterion id="IB178-2-AC2" cell_refs="IB-pr-513"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r178/p178_cells.py" . IB178-2-AC2</invocation><expect>IB178-2-AC2 PASS</expect></criterion>
<criterion id="IB178-2-AC3" cell_refs="IB-pr-513"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r178/p178_cells.py" . IB178-2-AC3</invocation><expect>IB178-2-AC3 PASS</expect></criterion>

<expected_criteria>IB178-2-AC1, IB178-2-AC2, IB178-2-AC3</expected_criteria>

What the checks grade: AC1 integer counts for both firms; `read_at_utc` later than `last_build_finished_utc`; `host_state_at_read` running and `ssm_status` Success; the build is named: `start_utc` before the last build's finish, `package_version_id` equal to the VersionId the apply put for that firm (read from the apply record), a 64-hex `package_sha256`, and a non-empty `snapshot_path_log_line` with its `log_source`; AC2 the recorded command is a read-only `find` piped to `wc -l` (no `rm`, `mv`, `cp`, `tee`, `-delete`, `-exec`) and the counts carry no path or long digit run; AC3 the counts read 0 for BOTH firms (a non-zero count FAILS this criterion by design: it is the finding) and the five bound counters read 0. Do not edit the checks. If the host is stopped, the criteria are not run: report it.

## BOUNDS

- **Grant:** your record folder and two read-only SSM Run Commands (one per firm) on an already-Online host, plus read-only reads of the invocation output and the log group. No host start or wake, no driven build, no deletion, no write to S3, no Lambda invoke.
- **Refusal clause:** STOP and report if the host is not Online, if the only build you can name did not run on the new package (its fetched VersionId differs), or a count command would need any write.
- **Row ids** are `IRPT_BCKEND-D2-IB2-S<k>` (the next free `k`). **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-513.post-build-leftover-temp-file-count.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 171 (round 179, workstream ~P), cell `IB-pr-513`.
<owned_cells>IB-pr-513</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB178-2-AC1, IB178-2-AC2, IB178-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-513.post-build-leftover-temp-file-count.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- read-only: the order runs two read-only SSM commands that print a number on a host that holds client-bearing temp files if the leak exists; no file is read, listed by name or deleted.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; SSM Run Command under the seat's existing principal.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched and the host is not started.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p178_cells.py dry-run at base on dell2 2026-10-13 ~14:5xZ: IB178-2 AC1, AC2, AC3 FAIL (no record).
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (live; TO-IB-pr-512 complete). Class SERVED.
</preflight>
