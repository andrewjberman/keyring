# TO NFRA_OUTSET.TO-OS-s-21 -- THE CADENCE: a producer-side schedule that publishes the two seam artifacts before each 13:00Z run

<to_id>NFRA_OUTSET.TO-OS-s-21</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.4** and the CTO's ROUND-2 ANALYSIS @`d6fd9eca07` (merged @`5f0cd1a318`), which directs "OS-s-21 buildable beside it with its accept gated on OS-s-20's". Decomposition v0.4 s.13-s.18. BUILDABLE NOW; its ACCEPT reads no earlier than the first served day after OS-s-20's switch is live.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.4 (s.7 row OS-s-21) · **Decomp cell:** `OS-s-21` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.4, s.13-s.18) · **outcome_ref:** FWD-3 · **verb:** build · **depends_on:** OS-s-20 on the ACCEPT edge only (buildable in parallel; the decomposition s.15 names the one-replace sequencing fact)

---

## THE CELL

`OS-s-21` (PRD s.7, evidence **absent**): the 13:03:50Z publish under OS-s-18 was BY HAND; `OUTSET_SEAM_MAX_AGE_HOURS` defaults to 26 (`estate_report_runner.py:1643`) and `runtime.env` does not override it, so from ~2026-09-10T15:03Z the seam artifact reads STALE -> `INSTRUMENT_FAILED` -- the consumer behaving CORRECTLY means the steady state of the seam AS CUT is FAILED, not OK. The battery's R5 arm exercised that conviction at 999.0 h. Row `S17`.

⛔ **A SEAM IS TWO ENDS AND A CLOCK.** The publish (OS-s-18), the read grant (OS-s-18), the switch (OS-s-20) and THIS, the clock. Without it the seam is a duplicate output path with a timer on it, which the standing NEVER rule forbids as a steady state. PRD s.3 costed "a publishing step and a freshness question per artifact"; the freshness question was answered in round 1; the cadence is the half that was never assigned. This row assigns it.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-cadence-scheduled-publish.result.md` -- what you measured, what you built, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## BOUNDS

- **Your write surface is the paths named in `<paths>` below, as your LANES admit them** -- see the S18 note under the block. A path you need that neither names is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).
- **NEVER bare `terraform apply`** -- `safe-apply` only, with the vendored `.tools/terraform.exe`. **NEVER `aws lambda update-function-code`.**
- **NEVER-AUTO-DELETE (PRD R-5) is absolute.** The R2 probe artifact `outset/_os18_red_arm_probe.json` on the seam prefix is its author's under R-5 and is UNTOUCHED by anything this order builds.
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

⛔ **THE TRIGGER IS THE PRODUCER'S OWN SCHEDULE, AND THAT IS THE WHOLE SHAPE.** Never success-of-upstream as the only trigger (CLAUDE.md: "success-of-upstream as the only trigger is a defect"); never a watcher on the consumer; never an alarm, monitor, freshness-checker or SNS -- the standing moratorium stands and DOES NOT REACH a pipeline trigger (the CTO's ruling @`e18317d0e0`: "a pipeline trigger is not a monitor"). "Production pipelines MUST be scheduled; ad-hoc runs are QA" names this row's class exactly. A hand publish is QA, permitted, and NEVER the exercise.

⛔ **WRITES ONLY THE TWO SEAM KEYS**: `outset/comp_heat_drift.json` and `outset/comp_heat_freshness_tools.json` (the two OS-s-18 published), each from its producer through `org/modules/heatmap/outset_seam.py`'s `publish_artifact` -- READ that module, do not edit it (lane NFRA_HEATMAP; a producer that needs it changed files a BLOCKING row). A FAILED producer publishes `answer_state=FAILED` (the R1 arm), never nothing.

⛔ **WHERE IT RUNS IS YOURS TO CHOOSE, INSIDE THE BOUNDS, AND ONE FACT BINDS THE CHOICE.** The producers are comp-heat runs that need a checked-out workspace; the report host has one at run time (it clones `ESTATE_REPO_URL` at boot) and none between runs (it self-stops). If the schedule lives in the host's bootstrap (a systemd timer or cron in `user_data`, firing before the 13:00Z run on the same boot), it is a `user_data` change and therefore a HOST REPLACEMENT (`instance.tf:83`) -- in that case it MUST ride TO-OS-s-20's replace as the same `user_data` change under that order's ledger entry, so the host is replaced ONCE; this order still carries its own accept and its own battery. If it lives off the host (an EventBridge Scheduler starting the box early, an SSM document, a Lambda with the workspace), it is its own build under `safe-apply` with its own change-management entry if it touches a served artifact. State which, and why, in the result and in TO-OS-s-20's ledger entry.

⛔ **THE IDENTITY THAT PUBLISHES IS NAMED, NOT INHERITED SILENTLY.** Whatever runs the producers holds a role; name it, read its `s3:PutObject` reach on `outset/*` on the APPLIED plane (the runner's role today holds GetObject on `outset/*` and Put on other prefixes -- measured at OS-s-18's negative control), and grant the minimum in `iam.tf` under `safe-apply` if a grant is needed. A worker subagent's ambient `*` on `*` is NOT a publishing identity for a scheduled pipeline.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="O21-AC1" cell_refs="OS-s-21"><invocation>timeout 300 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os21_cadence_fresh.py</invocation><expect>OS21-CADENCE-FRESH</expect></criterion>
`O21-AC1` -- a battery you write, proving THE ACCEPT AS THE PRD WRITES IT on a REAL served day: each seam artifact's vintage (`s3api head-object` LastModified, UTC -- `aws s3 ls` renders local) precedes that day's 13:00Z run start, and the served report's propagation stratum reads FRESH with age < 26 h disclosed. Arms that make the pass mean something: the schedule read LIVE (its state ENABLED and its fire time before 13:00Z, from the scheduler or timer itself, never from this face); the seam prefix listed and holding ONLY the two seam keys plus the untouched R2 probe (a fourth key is a FAIL); the vintages ATTRIBUTED to the schedule and not to a hand publish (the fire's own log or event, not a timestamp alone); ⛔ **THE NEGATIVE ARM**: with the schedule's effect removed (the R5 arm at 999.0 h, or a real disabled-schedule day if one exists), the same reader convicts STALE -> `INSTRUMENT_FAILED`, so no green comes from a raised ceiling. **This criterion CANNOT pass before the first scheduled fire that lands AFTER OS-s-20's switch is live on the served day; a pass read against a hand-published artifact is INVALID.**

INTERIM AMENDMENT 2026-09-09 ~15:2xZ BY THE ISSUER on row `NFRA_OUTSET-S23` (BLOCKING, the assignee's, filed @`76131249a0`): `comp-heat drift` measures the PRODUCING MACHINE'S dirty working tree (`cmd_drift` :502-578 -> one `git status --porcelain`, `object_freshness.py:259-268`), so a scheduled publisher on a clean clone emits n=0 forever with `answer_state OK`, a correct denominator and a fresh vintage -- and this criterion AS CUT would pass on it. THEREFORE, pending the CTO's ruling on the PRD row (pitched with a REC in the drive read): (1) a `comp_heat_drift.json` produced by a host or clone that has NO working tree of the estate's work is INADMISSIBLE as evidence for this criterion, whatever its vintage or answer_state -- an n=0 from a structurally empty tree is not a measurement of drift; (2) the FRESHNESS half (`comp_heat_freshness_tools.json`, whose tracked-history phase reads git commit timestamps and is identical on every clone -- the assignee measured this rather than assuming symmetry) PROCEEDS now inside this face's bounds; (3) the DRIFT half's home and cadence are HELD until the ruling lands and this face is amended to carry it. `<invocation>` and `<expect>` UNCHANGED. The assignee stopped before building the drift schedule and said so; that was the correct disposition.

<criterion id="O21-AC2" cell_refs="OS-s-21" judgment="true"/>
`O21-AC2` -- THE TRIGGER'S SHAPE AND HOME: where the producers run and under which identity (named, with its Put reach on `outset/*` read on the APPLIED plane), why that home (on-host in the same replace as OS-s-20, or off-host), that the trigger is the producer's own and not success-of-upstream or a watcher, the moratorium boundary as you read it, what a FAILED producer publishes, and the QA hand-publish (if any) distinguished from the exercise. Evidence with vintage. NO VERDICT.

<expected_criteria>O21-AC1, O21-AC2</expected_criteria>

<paths>
infra/aws/terraform/estate-report/
infra/aws/lambda/estate-report-orchestrator/
infra/aws/ec2/estate-report-runner/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
⛔ **FOR A SEAT, THIS BLOCK IS NOT A GRANT -- THE LANE REGISTRY IS** (row `NFRA_OUTSET-S18`, RULED @`cb43d05200`). Every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat before this cut (rc=0; the terraform module, the orchestrator Lambda, the runner directory, both ledger folders, this deliverables folder by clause 4, the channel by lane ANY). `org/modules/heatmap/outset_seam.py` is deliberately NOT named: lane NFRA_HEATMAP admits no CloudOps member, the producer IMPORTS it, and a change it needs is a BLOCKING row. `.tools/tests/` is not named: your battery lives in your deliverables folder. If a new terraform home outside `estate-report/` is the right place for the schedule, say so in a row before writing there -- that is a cut question, not a workaround.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.4, cell `OS-s-21`.
<owned_cells>OS-s-21</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~14:4xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 17.766 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_OUTSET, the estate-report host or runner, the orchestrator, the consumption seam or comp-heat (0 hits for those tokens across the ledger output). BLIND SPOT, stated: this lens reads the GATE LEDGER and cannot say whether a new schedule or a Put grant is otherwise constrained -- comp-iam's plane, required of the assignee below. The one standing gate that reads on this row's CLASS is the alert/monitor moratorium, and the CTO ruled @`e18317d0e0` that a pipeline trigger is outside it.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight, and REQUIRED OF THE ASSIGNEE as the cell's own instrument -- the publishing identity's `s3:PutObject` reach on `outset/*` is read on the APPLIED plane before any grant and after it. Run `comp-iam refresh-census` BEFORE any APPLIED-plane use (24 h TTL). FOUR false-deny modes are live (a CONDITIONED grant, a batched multi-ARN call, a WRONG-GRAIN resource ARN, and the census's role-only reach per S20). Positive-control any deny you intend to act on.
comp-adversary: DECLARED-NOT-APPLICABLE -- a fresh cut with no prior artifact to validate against.
lane: for a SEAT the lane registry is the grant and the `<paths>` block only narrows it (row S18, RULED @`cb43d05200`); every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat (rc=0), plus this seat's own deliverables folder by clause 4.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O21-AC1`, `O21-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-21.the-cadence-scheduled-publish.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O21-AC1,O21-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED.
⛔ **A `complete` flip is the end of the order**: flip only when the MECHANICAL criterion PASSES on a SERVED DAY under the schedule's own fire and the instance validates rc=0. The build lands today; the flip waits for the served day. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, TWICE on this order: once when the schedule is BUILT and applied (its home, identity and first fire time stated; the accept still pending the served day), and once at the flip. Per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so; do not work around it.
