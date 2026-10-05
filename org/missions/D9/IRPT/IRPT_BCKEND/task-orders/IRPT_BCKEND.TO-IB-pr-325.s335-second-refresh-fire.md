# TO IRPT_BCKEND.TO-IB-pr-325 -- a second directory refresh fire 10 minutes after the first, and the never-widen packet for the first fire that succeeds (S335; CTO batch 264)

<to_id>IRPT_BCKEND.TO-IB-pr-325</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~128</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>57</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 264 @f49b5958b0 (msg 105302), on row S335: "(a) a second
schedule at 13:40Z, same target and input", with a never-widen packet first for the first fire that succeeds | **Decomp cell:** `IB-pr-325`
(decomposition section 50) | **outcome_ref:** FWD-9 (the directory) | **depends_on:** none. The risk is WORLD because the cell edits Terraform
under infra/. It applies nothing: the apply is the issuer's, after both halves.

---

## WORKER FACE

**Row S335.** The directory refresh (`infra/aws/lambda/investor-reporting/directory/refresh.py:687-705`) fires once a day at 09:30
America/New_York (`infra/aws/terraform/investor-reporting/directory/schedule.tf:389-409`). When the runner host's SSM agent is not Online, it
issues ONE start and ends with HAND_OVER_RUNNER_OFFLINE, on the design that a later fire finds the host up. The next fire is a day later, so
the refresh has failed every day since 09-29 at all three firms. The directory is served from the 09-25 build: latest.json holds 4,620 /
292 / 258 entries.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-128`; run everything from its root.

1. **The second schedule.** In `schedule.tf`, add `aws_scheduler_schedule` `irpt_directory_refresh_retry` beside the existing one, with:
   - name `irpt-directory-refresh-retry` (check the naming registry: `.tools/naming-gate.py` must not refuse it; if it does, file a row
     and propose the registry row, do not hand-type around it);
   - the SAME target function, role and input `kind`, and the input `note` naming it the S335 retry;
   - `cron(40 9 ? * MON-FRI *)` in `America/New_York`, so the zone keeps the 10-minute gap across DST;
   - ENABLED, with flexible window OFF;
   - a comment block saying why: S335, batch 264, the start-then-next-fire design, and the 10-minute gap.

   The first schedule is unchanged. Add an output for the retry's name and state, like the existing outputs. Run `terraform fmt` on the
   file. Run NO plan or apply against AWS: the issuer plans and applies.
2. **The never-widen packet** at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~128/S335_SECOND_FIRE_PACKET.json`:
   - `firms`: for each of 49financial, inflection and cottonwood, the `bucket` (opal-data-bd, opal-data-inf, opal-data-cot), the `key`
     `investor-reporting/directory/latest.json`, its current `version_id` and `last_modified` (s3 head-object, a read), its
     `entry_count` (read the object and count its entries; name the field you counted), and `rollback` (copy that version back over
     the key, by version id);
   - `writer`: who writes latest.json when a build lands (the runner script on the host, or the refresh; read `refresh.py` and
     `runner_script`), with file:line;
   - `branches`: (1) the host is Online at the retry, so the build runs and latest.json is REPLACED, with before and after counts per firm
     read by the issuer after; (2) the host is still not Online, so nothing is written and the manifest reads OFFLINE again;
   - a `note` that the 12:52Z start by mdpf-feeder-trigger (schedule.tf:381-387) did not happen on 2026-10-05: the host's LaunchTime
     was 13:30:36Z, started by the refresh itself. That is the MDPF chain's lane; the retry does not depend on it.

<criterion id="IB57-1-AC1" cell_refs="IB-pr-325"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r57/p57_second_fire.py" . IB57-1-AC1</invocation><expect>IB57-1-AC1 PASS</expect></criterion>
`IB57-1-AC1` -- two refresh schedules (09:30 and 09:40 ET) target the function with the same role and input kind, both ENABLED, and the file
passes fmt. Base: FAIL.

<criterion id="IB57-1-AC2" cell_refs="IB-pr-325"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r57/p57_second_fire.py" . IB57-1-AC2</invocation><expect>IB57-1-AC2 PASS</expect></criterion>
`IB57-1-AC2` -- the packet covers the three firms with version id, count and rollback, plus the writer and both branches. Base: FAIL.

<expected_criteria>IB57-1-AC1,IB57-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only (s3 head-object and get-object on the three latest.json keys). NO terraform plan or apply, and no write.
- **Refusal clause.** Any change to the first schedule, the function, its role or its code is out of scope: file a row.

<paths>
infra/aws/terraform/investor-reporting/directory/schedule.tf
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~128/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-325.s335-second-refresh-fire.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 50 (round 57, workstream ~P), cell `IB-pr-325`.
<owned_cells>IB-pr-325</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB57-1-AC1, IB57-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~128/IRPT_BCKEND.TO-IB-pr-325.s335-second-refresh-fire.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB57-1-AC1,IB57-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the per-firm version ids and counts, the writer,
and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one new EventBridge Scheduler schedule invoking an existing function 10 minutes after the existing one; the first successful fire replaces three latest.json keys (the never-widen packet covers them); the apply is the issuer's after both halves.
comp-iam: DECLARED-NOT-APPLICABLE -- the existing scheduler role already grants lambda:InvokeFunction on this one function.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: RUN -- a second fire at 09:40 America/New_York (13:40Z EDT, 14:40Z EST), inside the runner's 12:52Z-16:41Z window.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB57-1-AC1 base FAIL (one schedule), IB57-1-AC2 base FAIL (no packet), dry-run at base 795a128808 2026-10-05 ~15:1xZ.
lane: the <paths> block IS the grant.
</preflight>
