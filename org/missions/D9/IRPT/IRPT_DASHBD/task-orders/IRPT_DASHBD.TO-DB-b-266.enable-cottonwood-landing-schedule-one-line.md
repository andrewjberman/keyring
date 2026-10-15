# TO IRPT_DASHBD.TO-DB-b-266 -- ENABLE the Cottonwood landing schedule `irpt-cot-account-return-daily-daily`: ONE line of `schedule.tf` (DISABLED to ENABLED), `safe-apply`, a plan of exactly 1 change, NO invoke, the ledger left OPEN for the issuer's read of the first scheduled fire (CTO ruling: ROUND-128 ANALYSIS ADDENDUM 1 @143709c44f, msg 8486)

<to_id>IRPT_DASHBD.TO-DB-b-266</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~DB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>134</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_128_20261015.md` ADDENDUM 1 (@143709c44f, LOCAL: "RULED: enable `irpt-cot-account-return-daily-daily` (DISABLED to ENABLED), on these terms: one line in the pinned .tf, applied by `safe-apply`, under its own ledger entry, the plan reads 1 change and nothing else; T-1 trading days only; the first scheduled fire is read; rollback is the one line back to DISABLED"), msg 8486, on the issuer's packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND130_132_131_B49F_DRAIN_END_20261015.md` @27847c126a and the signed pair revision 3 (packet sha256 `31f8e1620b90...`: its section 1 lists enabling the schedule as the one act NOT covered by that pair, which this CTO ruling covers) | **Decomp cell:** `DB-b-266` (decomposition section 132) | **outcome_ref:** FWD-11, FWD-21 | **depends_on:** `DB-b-262` (Act 3, merged @691b95c160).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying the CTO's addendum and the issuer's checkers); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** No client data is read or recorded: counts, dates, keys, hashes, addresses and words only.

**What this order does, in one paragraph.** The Cottonwood landing function `irpt-cot-account-return-daily-lambda` has landed every day from 2026-07-10 to 2026-10-14 by explicit events; its schedule `irpt-cot-account-return-daily-daily` (`cron(15 8 ? * MON-FRI *)`, America/New_York) was created DISABLED. The CTO has ruled it enabled. You change ONE line of `infra/aws/terraform/investor-reporting/account-return-daily/schedule.tf` (`state = "DISABLED"` to `state = "ENABLED"`, nothing else, not the description), run `terraform plan`, and, only if it reads EXACTLY 0 add / 1 change / 0 destroy on the schedule, make ONE `safe-apply`. **You invoke NOTHING.** The next scheduled fire (Friday 2026-10-16, 08:15 New York) is read by the issuer, not by you. The handler resolves the day itself (the days after the newest landed day through T-1, at most five, never a day before the 2026-07-10 floor).

**Read first (all in your worktree):** the CTO's addendum (the four terms); `infra/aws/terraform/investor-reporting/account-return-daily/schedule.tf`; the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r134/p134_enable.py` (the record's exact form is in it); your own record `COT_LANDING_APPLY_RECORD.json` and `COT_CATCHUP_RECORD.json` (ledger, plan, safe-apply, read-backs).

**Do, in this order. Record every value named in `COT_SCHEDULE_ENABLE_RECORD.json` as you go.**

0. **Gates, read only.** (a) The CTO's addendum reads RULED: enable (`gates.cto_ruling_read`); the packet `NEVER_WIDEN_PACKET_COTTONWOOD_ACCOUNT_RETURN_DAILY_LANDING.md` still hashes to sha256 starting `31f8e1620b90` (`gates.packet_sha12`); the landing ledger `irpt-dashbd-cottonwood-account-return-daily-20261015` is CLOSED (`gates.landing_ledger_closed`). (b) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at any live worktree (print the denominator) names the `account-return-daily` root, `irpt-cot-account-return-daily` or `irpt-cot-account-return-daily-daily`, other than the ledger you open at step 1; any other open one is a STOP (`gates.one_change_at_a_time` {`worktrees_read`, `open_markers_naming_this_surface` (1, your own, after step 1)}). (c) **Not within an hour before a scheduled fire of this root** (the next is 2026-10-16 08:15 New York) and not during a fire. (d) LIVE now: the schedule reads `DISABLED`, the cron and zone above; the function reads memory 1024, timeout 900.
1. **Open the NEVER-2 ledger BEFORE any write** with `python .tools/deploy_ledger.py open ...` under `org/critical_paths/change_management/`, slug `irpt-dashbd-cottonwood-schedule-enable-20261015`, legs: L1 git (the one-line edit and its commit); L2 terraform (the plan 0/1/0, then the apply); L3 verify (the read-backs); L4 the first scheduled fire (a leg that stays OPEN for the issuer). Commit its `.open_deploys` sentinel at once.
2. **The one line.** Edit `schedule.tf`: the `state` line only. `git diff` must show exactly one changed line. Commit with `.tools/safe-commit.sh` (record `edit` {`file`, `lines_changed` 1, `commit`}). Record `before` {`schedule` {`state`, `cron`, `zone`}, `function` {`memory`, `timeout`}}.
3. **fmt, validate, plan, under the repo's route.** `.tools/terraform.exe` on the root: `fmt -check`, `init`, `validate`, a saved `plan`. **The plan must read EXACTLY** 0 to add, 1 to change, 0 to destroy, the one change being `aws_scheduler_schedule.irpt_account_return_daily` (`state` DISABLED to ENABLED). Any other add or change, any destroy, any other attribute changed, is a STOP.
4. **ONE `safe-apply`** from the saved plan (the naming gate runs in it; never a bare `terraform apply`). Read back: the schedule (`ENABLED`, the cron, the zone, the target the function, the flexible window OFF), the function unchanged (memory 1024, timeout 900). A post-apply plan must read `No changes`. Record `plan` {`add`, `change`, `destroy`, `addresses`, `replan_no_changes`}, `apply_finished_utc` and `after` {`schedule`, `function`}.
5. **NO INVOKE.** Not the function, not a dry run, not a `day` or `days` event. Record `invoke` {`count` 0}.
6. **Do NOT close the ledger.** Leg L4 (the first scheduled fire) stays OPEN for the issuer. Record `ledger_closed` false. **Rollback, if ever ordered:** the one line back to DISABLED through the same route; the partitions written stay (removing any is Andrew's act).

Write `COT_SCHEDULE_ENABLE_RECORD.json` in your folder with exactly: `claim` ("measured"); `gates` {`cto_ruling_read`, `packet_sha12`, `landing_ledger_closed`, `one_change_at_a_time`}; `ledger_entry`; `before`; `edit`; `plan`; `apply_finished_utc`; `after`; `invoke`; `ledger_closed`; `reads` {`vendor_calls` 0, `secret_reads` 0}. Counts, dates, keys, hashes, addresses and words only.

<criterion id="DBE134-1-AC1" cell_refs="DB-b-266"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r134/p134_enable.py" . DBE134-1-AC1</invocation><expect>DBE134-1-AC1 PASS</expect></criterion>
`DBE134-1-AC1` -- the record has exactly the form above; the CTO's addendum reads RULED: enable; the packet is revision 3; against the order's first commit `schedule.tf` differs in exactly ONE line, `state` DISABLED to ENABLED, and every other file of the root is byte-equal; the plan read 0 add / 1 change / 0 destroy on the schedule and the post-apply plan read No changes. Base: FAIL (no record).
<criterion id="DBE134-2-AC1" cell_refs="DB-b-266"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r134/p134_enable.py" . DBE134-2-AC1</invocation><expect>DBE134-2-AC1 PASS</expect></criterion>
`DBE134-2-AC1` -- FRESH live reads by the checker: the schedule reads ENABLED at the cron and zone, its target is the function and its flexible window OFF; the function is unchanged; no key of any day up to 2026-10-14 was modified after the apply finished (the apply writes nothing); any partition after 2026-10-14 (a scheduled fire's) holds exactly its two objects; the ledger's open marker exists. Base: FAIL (no record).

<expected_criteria>DBE134-1-AC1, DBE134-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **The ruled act, and nothing wider.** Writes to AWS: the ONE Terraform apply (`safe-apply`) of the `account-return-daily` root changing the one schedule's state. **NO invoke of any kind; NO change to the function, the roles, the policies, the cron, the zone or the description; NO other root; NO deletion of any object or file; NO bare `terraform apply`; NO `update-function-code`.**
- **Read-only:** `get-schedule`, `get-function-configuration`, S3 list and head of the gold prefix, `terraform fmt/init/validate/plan`.
- **Refusal clause.** STOP and report, writing nothing further, on any of: the addendum not reading RULED: enable; the packet differing; the landing ledger not closed or any other open marker naming this surface; a fire within an hour; the live state differing from step 0(d); a plan with any add, any change count other than 1, any destroy, an address other than the schedule or any other attribute changed; the post-apply plan not reading No changes. After the apply, a STOP is reported with the state left as it is.
- **Row ids** are `IRPT_DASHBD-D2-DB2-S<k>` (the next free `k`); file a row for anything odd and keep working. Commit with `.tools/safe-commit.sh`. ASCII only. **Report once, under 150 words; report each STOP at once.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-266.enable-cottonwood-landing-schedule-one-line.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
infra/aws/terraform/investor-reporting/account-return-daily/schedule.tf
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 132 (round 134, workstream B-49F), cell `DB-b-266`.
<owned_cells>DB-b-266</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBE134-1-AC1, DBE134-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/IRPT_DASHBD.TO-DB-b-266.enable-cottonwood-landing-schedule-one-line.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBE134-1-AC1,DBE134-2-AC1` BEFORE any flip; pin each artifact row to the commit that carried it. Run each criterion under `timeout 300` from the repository root and record the output and exit code verbatim.
</proof_of_spec>

**REPORT:** once, under 150 words: the two criteria's last lines; the ledger slug; the plan's counts; the schedule's state after; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one existing schedule changes state in place (DISABLED to ENABLED); nothing is created or deleted. The blast radius is the ruled act's: the next fires run the landing function for the days owed (the guard refuses any existing partition; the floor refuses any day before 2026-07-10).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant changes; the scheduler role and its policy exist and are unchanged.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; no served page changes (the table has no established reader before the report-build function).
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: THIS IS the schedule act: the single schedule is enabled on the CTO's written ruling; the criteria read its state and its target.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the two criteria FAIL at base (no record) and recount from fresh scheduler, Lambda and S3 reads; the record clauses are exercised by the checker's self-test (4 + 21 red arms).
</preflight>
