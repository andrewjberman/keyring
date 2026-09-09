# TO NFRA_OUTSET.TO-OS-s-20 -- THE CONSUMER SWITCH: `ESTATE_OUTSET_SEAM_PREFIX` set on the report host, so the served runner's propagation stratum composes the seam key

<to_id>NFRA_OUTSET.TO-OS-s-20</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.4** and the CTO's ROUND-2 ANALYSIS @`d6fd9eca07` (merged @`5f0cd1a318`), which directs "2.0.0_SA_COO recuts from this analysis: two rows, both CloudOps, no worker fan-out; OS-s-20 after OS-s-19 (done)". Decomposition v0.4 s.13-s.18. Andrew's GO in principle for THIS host replacement is on the record @`e1b44ba4cc` and rides this face.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.4 (s.7 row OS-s-20) · **Decomp cell:** `OS-s-20` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.4, s.13-s.18) · **outcome_ref:** FWD-3 · **verb:** deploy · **depends_on:** OS-s-19 (COMPLETE @`9e023d20b5`) -- a DEPENDENCY EDGE, not a preference: the host boots whatever runner sits in S3 (`instance.tf:94-96`, `:215`)

---

## THE CELL

`OS-s-20` (PRD s.7, evidence **absent**): the `runtime.env` heredoc at `infra/aws/terraform/estate-report/instance.tf:130-151` sets eleven variables and NOT `ESTATE_OUTSET_SEAM_PREFIX`; the served runner reads it unset (`estate_report_runner.py:1611`) and `_stratum_propagation` returns `INSTRUMENT_UNAVAILABLE` without composing a key (`:1810-1846`). Row `S16`.

⛔ **THIS IS THE CELL THAT MAKES ROUND 2 REAL OR LEAVES IT ON PAPER.** Round 2 landed the grant (`OS-s-18`: the runner's role reads `outset/*`, EXERCISED from inside the host) and the deploy (`OS-s-19`: the served runner is HEAD's, carrying the consumer -- `ESTATE_OUTSET_SEAM_PREFIX` 5, `_outset_read` 4 in the served bytes, 0 before) and the served report still renders `A_propagation` exactly as it did on 2026-08-25, because the consumer is not configured to look. A SEAM IS TWO ENDS AND A CLOCK; this is the consumer's switch.

⛔ **SETTING IT IS A HOST REPLACEMENT, NOT A CONFIG EDIT.** `instance.tf:83` carries `user_data_replace_on_change = true`, deliberately (an in-place `user_data` update is recorded as applied and never executes). The apply DESTROYS AND RECREATES the instance and THE INSTANCE ID CHANGES. `instance.tf:114-121` says what that costs: the orchestrator Lambda starts this box BY ID; a stale ID makes the 13:00Z fire start nothing, silently.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-consumer-switch-host-replace.result.md` -- what you measured, what you changed, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## BOUNDS

- **Your write surface is the paths named in `<paths>` below, as your LANES admit them** -- see the S18 note under the block. A path you need that neither names is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).
- **NEVER bare `terraform apply`** -- `safe-apply` only, with the vendored `.tools/terraform.exe` (the PATH substitute re-pins remote state). **NEVER `aws lambda update-function-code`.**
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium). **NEVER-AUTO-DELETE (PRD R-5) is absolute.**
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

⛔ **THIS IS A NEVER-2 CELL OF THE "STOPPING EC2 / UNRECOVERABLE" CLASS, AND THE WORD FOR IT IS ALREADY GIVEN.** Andrew-direct 2026-09-09 ~14:2xZ at the `1.0.0_SA_CTO` terminal, VERBATIM "All recs approved", record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260909_142xZ_ALL_RECS_APPROVED_THREE_CALLS_COOA_REGISTERING.md` @`e1b44ba4cc`, CALL 2: the estate-report host is REPLACED to set `ESTATE_OUTSET_SEAM_PREFIX`, under its own NEVER-2 change-management entry, outside the run window, after OS-s-19, with the orchestrator's target instance ID re-pointed and verified LIVE before the entry closes. **You do not ask again for this act. It authorises ONE replace of ONE host and no mechanism change; anything wider is a row, not an act.**

⛔ **THE LEDGER IS NOT OPTIONAL AND ITS ORDER IS THE PROOF.** Open a change-management entry in `org/critical_paths/change_management/` and COMMIT IT OPEN before the apply (the OS-s-19 pattern: opened-before is a fact in git history, not prose); close it at completion in a second commit. The entry names: the host (`i-0512bd3cbaf602b7f` today, and the NEW id after), the runner bytes the new host will boot (`s3://opal-estate-report/code/estate_report_runner.py`, VersionId `GQny85Je837UhagoFc0FY8eoJzcB1RFy`, ETag `e75c59a35457535ca0d339c9f59589f5`, 159,687 B -- read it live before acting, never from this face), the rollback (a destroyed instance is not restored: the rollback is a further replace under the prior `user_data`, stated before the act), and WHICH of the two shapes below you took. **NEVER leave a confirmed deploy half-landed** -- finish in-session or roll back and escalate loud. ⛔ **Before acting on ANY open or red entry you find, MEASURE THE ARTIFACT.**

⛔ **OUTSIDE THE RUN WINDOW.** The host self-stops after each 13:00Z run (today: started 13:00:45Z, stopped 13:11:04Z); the next scheduled fire is 2026-09-10 13:00Z. Read the instance state and the schedule LIVE immediately before the apply and state plainly that the replace lands outside the window. **Do not start the box to force an early exercise**: the accept is the SCHEDULED fire, and an ad-hoc run would consume the discriminator that fire exists to produce.

⛔ **THE ORCHESTRATOR'S TARGET, MEASURED NOT ASSUMED.** `orchestrator.tf:37` reads `ESTATE_INSTANCE_ID = aws_instance.estate_report_runner.id` -- a Terraform reference, so the apply re-points the Lambda's environment; and `lambda_function.py:34` reads it at IMPORT, so a warm container could hold the old id until the configuration change retires it. Before the entry closes: `get-function-configuration` on `estate-report-orchestrator` must read the NEW instance id, `describe-instances` on that id must read a live instance, and the two must agree. That read is a CONTROL on the ledger's close, never the accept.

⛔ **ONE REPLACE, NOT TWO -- READ THIS BEFORE THE APPLY.** TO-OS-s-21 (the cadence) is issued beside this order. If its mechanism lives in this host's bootstrap (a systemd timer or cron in `user_data`), every further `user_data` edit is ANOTHER replacement. In that case land the cadence in the SAME `user_data` change as the prefix, so the host is replaced ONCE under ONE ledger entry (the two orders' accepts are still read separately). If the cadence lives off the host (EventBridge Scheduler / SSM / a Lambda), this replace carries only the prefix. State which in the ledger entry.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="O20-AC1" cell_refs="OS-s-20"><invocation>timeout 300 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os20_served_day_reads_seam.py</invocation><expect>OS20-SEAM-READ-ON-SERVED-DAY</expect></criterion>
`O20-AC1` -- a battery you write, proving THE ACCEPT AS THE PRD WRITES IT: on a SCHEDULED 13:00Z run of the REPLACED host, the published report's propagation stratum returns an answer state other than `INSTRUMENT_UNAVAILABLE` with the seam artifact's vintage disclosed. Read the served day's report from the bucket (the `daily/` artifact of that day), never a local render. ⛔ **THE NEGATIVE ARM IS A REAL DAY, NOT A MUTANT**: the 2026-09-09 served report (run under the un-switched host) reads `INSTRUMENT_UNAVAILABLE` on the same stratum -- the same reader must return that on the old day and the new state on the new day, or the comparator is a constant. Add an arm that reads the orchestrator's live target against `describe-instances` (equal ids, instance exists) and a planted-stale-id copy that reports MISMATCH. **This criterion CANNOT pass before the first scheduled fire of the replaced host (2026-09-10 13:00Z at the earliest); that is correct and is the point of the cell.** The env line present in the live `runtime.env` (read via SSM) is a CONTROL arm, never the deciding line.

<criterion id="O20-AC2" cell_refs="OS-s-20" judgment="true"/>
`O20-AC2` -- THE REPLACE UNDER ITS LEDGER: the entry opened-before and closed-after (both commits cited), the window as measured, the old and new instance ids, the runner bytes the new host booted (head-object at boot time), the orchestrator's target read LIVE after the apply, the rollback shape stated before the act, which of the two shapes (cadence in `user_data` or off-host) you took and why, and Andrew's GO @`e1b44ba4cc` cited as the authority. Evidence with vintage. NO VERDICT.

<expected_criteria>O20-AC1, O20-AC2</expected_criteria>

<paths>
infra/aws/terraform/estate-report/
infra/aws/lambda/estate-report-orchestrator/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
⛔ **FOR A SEAT, THIS BLOCK IS NOT A GRANT -- THE LANE REGISTRY IS** (row `NFRA_OUTSET-S18`, RULED @`cb43d05200`: `owned-paths-validate.py` `_WORKER_SERIAL_RE` gates the `<paths>` grant on a `0.9.0_WK_*` serial; for a seat the block only narrows). Every path above was resolved for `0.7.0_AE_CloudOps~W` at the issuer's seat before this cut: 8 of 8 candidates PERMITTED, rc=0 (the two terraform files, the orchestrator Lambda source, the runner, both ledger folders, this deliverables folder by clause 4, the channel by lane ANY). Your battery lives in your deliverables folder from the start. `org/critical_paths/change_management/` and `.open_deploys/` are named BECAUSE THIS CELL CAN DEPLOY. `infra/system/06_current_state.{json,md}` is deliberately NOT named: the comp-system gate keys on `.tools/comp-` and `org/modules/graph/` and neither is touched here; if it fires anyway that is a CUT DEFECT and it is the issuer's.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.4, cell `OS-s-20`.
<owned_cells>OS-s-20</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~14:4xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 17.766 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_OUTSET, the estate-report host or runner, the orchestrator, the consumption seam or comp-heat (0 hits for those tokens across the ledger output). BLIND SPOT, stated because a denominator without one is half an answer: this lens reads the GATE LEDGER, so it can say no armed gate names these surfaces and it CANNOT say whether a host replacement or an IAM change is otherwise constrained -- that is comp-iam's plane and is required separately below. The one gate this cell DOES sit under is not in the ledger: it is Andrew's own word on stopping EC2, and it is given @`e1b44ba4cc`.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight, and REQUIRED OF THE ASSIGNEE as the cell's own instrument -- the same disposition OS-s-6, OS-s-7, OS-s-18 and OS-s-19 carried. This issuer did not run it and does not claim to. THE ASSIGNEE MUST -- a replaced host assumes its instance profile afresh and the orchestrator's role starts it. Run `comp-iam refresh-census` BEFORE any APPLIED-plane use; the census carries a 24 h TTL and nothing refreshes it. FOUR false-deny modes are known and all four are live (the fourth, a resource ARN at the WRONG GRAIN, landed in /cloud-ops @`4e22065278` from this project's own S3): a CONDITIONED grant, a batched multi-ARN call poisoning sibling verdicts, a wrong-grain ARN, and the census's own gap (S20: it enumerates no users or groups, so a reach read from it is role-only). Positive-control any deny you intend to act on.
comp-adversary: DECLARED-NOT-APPLICABLE -- a fresh cut with no prior artifact to validate against.
lane: for a SEAT the lane registry is the grant and the `<paths>` block only narrows it (row S18, RULED @`cb43d05200`); every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat (8 of 8, rc=0), plus this seat's own deliverables folder by clause 4 (the serial in the path).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O20-AC1`, `O20-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-20.the-consumer-switch-host-replace.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O20-AC1,O20-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED with "NO proof-of-spec instance was found beside it" while a valid instance sits on disk.
⛔ **A `complete` flip is the end of the order**: flip only when every MECHANICAL criterion PASSES on a SERVED DAY and the instance validates rc=0. The replace itself lands today; the flip waits for the served day. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, TWICE on this order: once when the replace has landed and its ledger entry is CLOSED (the act; the accept still pending the served day), and once at the flip. Per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so; do not work around it.
