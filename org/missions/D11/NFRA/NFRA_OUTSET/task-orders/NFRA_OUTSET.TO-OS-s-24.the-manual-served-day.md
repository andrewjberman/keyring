# TO NFRA_OUTSET.TO-OS-s-24 -- THE MANUAL SERVED DAY: the seam refreshed by hand, the report host started by the 13:00Z rule's own mechanism after 00:00Z, the report on the same served key with `trigger=manual`, and every round-3 accept read on that run

<to_id>NFRA_OUTSET.TO-OS-s-24</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.8** @`dc6a33c3e3` (the manual-trigger addendum v0.7 @`0d44fdd1ee` amended on this seat's four cut-shaping facts -- all four adopted, 94751; Andrew's ~21:4xZ word), s.9 row OS-s-24; decomposition v0.7 s.27-s.30. THIRD of the three: runs AFTER 00:00Z 2026-09-10 (09-10 keys, nothing overwritten), after OS-s-26 is deployed and OS-s-25 has run. Every accept of OS-s-19 / OS-s-20 / OS-s-21 / OS-s-22 / OS-s-23 reads on THIS run before 13:00Z; the 13:00Z fire confirms.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.8 (s.9 row OS-s-24) · **Decomp cell:** `OS-s-24` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.7, s.27-s.30) · **outcome_ref:** FWD-2, FWD-3, FWD-4, FWD-7 · **verb:** verify · **depends_on:** OS-s-26 (the trigger token, deployed), OS-s-25 (the device row's on-demand run), OS-s-19, OS-s-20, OS-s-21, OS-s-22, OS-s-23 (the acts landed today; their accepts read here)

---

## THE CELL

`OS-s-24` (PRD s.9, evidence **absent**): round 3's four open accepts all read "on a served day" and would wait for 2026-09-10 13:00Z and 2026-09-11. Andrew's word: *"we need to not be 'waiting' on anything, anything that we'd be waiting for needs a manual trigger of some kind depending on the test type."* Under the manual-trigger rule the served day is MADE, by the rule's own target, and the scheduled fire is confirmation. The 13:00Z scheduler's own firing is already proven from history (seven consecutive rule-initiated runs 09-03..09-09, listed by `0.7.0_AE_CloudOps~W` in 94738 with the 15:32Z creation-boot run correctly excluded) -- rule (4) is MET for this schedule; the two never-fired schedules take OS-s-25's and OS-s-26's forms.

⛔ **THE ORDER OF THE NIGHT, AS THE PRD WRITES IT (v0.8, all four of this seat's facts adopted):**
(i) OS-s-25's on-demand drift run (done before this order starts) -- the device artifact fresh under the scoped role;
(ii) the freshness CodeBuild started by hand: `aws codebuild start-build --project-name estate-report-seam-freshness-publisher` -- the SAME target the 08:30 ET rule invokes (its `Target.Arn` is the project, its action `codebuild:StartBuild`, `Target.Input` NULL, so the hand start and the rule start are the same call), writing BOTH seam keys (freshness and group B); the build's `initiator` recorded;
(iii) AFTER 00:00Z 2026-09-10, the orchestrator invoked with the rule's OWN payload plus the manual marker OS-s-26 fixed: `aws lambda invoke --function-name estate-report-orchestrator --payload '{"mode":"daily-run","trigger":"manual"}'` -- which writes the trigger token and starts the replaced host (`i-0584e17d283fa7ef4`), whose boot units run the report by design;
(iv) the report on the SAME served keys -- `daily/2026/09/10/estate-report-2026-09-10.{json,md}` and `manifest/2026-09-10.json` -- new keys for the day, overwriting NOTHING (the 09-09 keys, the only artifact proving OS-s-20, stay at their pinned VersionIds); `run_bundle.trigger == "manual"` with a `run_id`;
(v) every accept of OS-s-19 / OS-s-20 / OS-s-21 (both halves) / OS-s-22 / OS-s-23 READ ON THAT RUN before 13:00Z -- each order's own battery run against the 09-10 manual artifacts; each order's face amended today to say so;
(vi) the 13:00Z scheduled fire writes the same day's keys again with `run_bundle.trigger == "scheduled"` -- CONFIRMATION, read if present, never a gate.

⛔ **RULE (2) AND THE NEVER-2 ENTRY.** A report run writes served output the estate reads (`daily/`, `manifest/`): this is a served-output move. **The entry is OPENED FIRST**, naming: the keys the run will create (09-10) and that no existing key is overwritten; the four 09-09 pins as the protected record (`.json` `M.3hYlFn8PRvTcqxCUouBTNygDd73huK` (15:32:41Z, switched host) and `8SP4fGAuhE8twzBpucMPsYbotD6Tddty` (13:11:02Z, O20-AC1's negative arm); `.md` `xfSKTGqkdljsQTyUt20nC1RJsPtPGBSU` and `GcEjGK_GwkDzyyvVo190fPSODn9svmLx`); the rollback (one `copy-object` from a pinned VersionId, bucket versioning ENABLED); and the NEVER-WIDEN SIGN-OFF, CTO + COO, as two quoted message ids. **The COO's half is GIVEN HERE, in this face, for exactly this run: 09-10 keys, nothing overwritten, the four pins named, the rollback named -- quote this face's commit hash as the COO's line. The CTO's half is asked for in the drive read that carries this issuance; do not start step (iii) until the entry quotes both.** The `outset/` seam writes in (i) and (ii) are producer artifacts under their faces' QA clauses and are NOT served-output moves (rule (2) as adopted; not retroactive).

⛔ **THE HOST SELF-STOPS.** The run ends with the host stopped (the boot units' design; O20's ledger shape); a host still running 30 minutes after the report landed is a finding, not a wait.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-manual-served-day.result.md` -- what you measured, what you ran, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed. The five re-read accepts each go in THEIR OWN order's deliverable and proof instance, not here; this deliverable indexes them by path + hash.

## BOUNDS

- **Your write surface is the paths named in `<paths>` below, as your LANES admit them** -- see the S18 note under the block. A path you need that neither names is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).
- **NEVER bare `terraform apply`** -- `safe-apply` only. **NEVER `aws lambda update-function-code`.** This order applies nothing: OS-s-26's deploy is OS-s-26's.
- **NEVER-AUTO-DELETE (PRD R-5) is absolute.** Nothing is deleted; the 09-09 keys keep their pinned versions as the latest for their day; the probes stay.
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium; a scheduler target invoked by hand is not a monitor).
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="O24-AC1" cell_refs="OS-s-24"><invocation>timeout 900 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os24_manual_served_day.py</invocation><expect>OS24-MANUAL-SERVED-DAY</expect></criterion>
`O24-AC1` -- a battery you write, proving THE MANUAL SERVED DAY ON THE REAL PLANE: (a) the NEVER-2 entry exists and was opened BEFORE step (iii) (its opened-at precedes the invoke's UTC), names the four pins and the rollback, and quotes BOTH sign-off halves (this face's hash for the COO; the CTO's message id); (b) the seam artifacts' vintages precede the run's start (`s3api head-object` LastModified in UTC on `outset/comp_heat_freshness_tools.json`, `outset/comp_fedobs_coevolution.json`, `outset/laptop/comp_heat_drift.json`; each earlier than `run_bundle.started_at`), and the CodeBuild's `initiator` recorded; (c) the served report at `daily/2026/09/10/estate-report-2026-09-10.json` carries `run_bundle.trigger == "manual"` and a `run_bundle.run_id` equal to the token OS-s-26 wrote for this invoke -- never inferred from the clock; (d) group A renders OK from the seam with each device's vintage disclosed (`laptop` present by name with OS-s-25's vintage; a silent device SILENT/INSTRUMENT_FAILED as the negative arm); group B renders from its seam artifact with its grain disclosed (`[grain=file-pair, NOT resource-grain]`) and a non-zero row count equal to an independent count of the artifact; (e) the NEGATIVE ARM on the protected record: the four 09-09 pins are STILL the latest versions of their keys (`list-object-versions` on each key, IsLatest true on the pinned id) -- the manual day overwrote nothing; (f) the host is STOPPED at the read (`describe-instances`, `stopped`, with `StateTransitionReason`), and (g) IF PRESENT at the read, the 13:00Z fire's report on the same keys carries `run_bundle.trigger == "scheduled"` -- recorded as confirmation, never waited for. Denominators on every list; `timeout 900`.

<criterion id="O24-AC2" cell_refs="OS-s-24" judgment="true"/>
`O24-AC2` -- THE FIVE ACCEPTS READ ON THIS RUN: for each of OS-s-19, OS-s-20, OS-s-21 (freshness half by the hand-started build with the rule's configuration read as (4)'s form; drift half by OS-s-25), OS-s-22 and OS-s-23 -- the path and hash of that order's deliverable and proof instance as re-read against the 09-10 manual artifacts, PASS or FAIL as ITS battery printed (never restated here), and what the 13:00Z confirmation added if present. Plus the mechanism identity: that steps (ii) and (iii) invoked the rule's own targets with the rule's own payload shape (the `Target.Arn` / `Target.Input` reads beside the hand invocations). Evidence with vintage. NO VERDICT.

<expected_criteria>O24-AC1, O24-AC2</expected_criteria>

<paths>
infra/aws/terraform/estate-report/
infra/aws/lambda/estate-report-orchestrator/
infra/aws/ec2/estate-report-runner/
infra/aws/ec2/outset-drift-device/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
⛔ **FOR A SEAT, THIS BLOCK IS NOT A GRANT -- THE LANE REGISTRY IS** (row `NFRA_OUTSET-S18`, RULED @`cb43d05200`). Every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat at this cut (22:2xZ); the deliverables folder by clause 4; the seam module refused as the negative control and never edited. This order WRITES no code path: it runs, reads and records; the ledger folders are named for the NEVER-2 entry.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.7, cell `OS-s-24`.
<owned_cells>OS-s-24</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~22:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_OUTSET, the estate-report host or runner, the orchestrator, the consumption seam, comp-heat or fedobs (0 hits for those tokens across the ledger output). BLIND SPOT, stated: this lens reads the GATE LEDGER and cannot say whether a served-output write is otherwise constrained -- the NEVER-2 entry and the never-widen sign-off ARE that constraint, and both are named in the accept.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight; this order grants nothing (OS-s-26's grants are OS-s-26's). The scheduler role's ability to start the host and the CodeBuild rule's target were read on the applied plane by the assignee (94738) and are cited, not re-derived.
comp-adversary: DECLARED-NOT-APPLICABLE -- a verify cell over artifacts the round already validates; the controls are the pinned versions and the independent row count.
lane: for a SEAT the lane registry is the grant and the `<paths>` block only narrows it (row S18, RULED @`cb43d05200`); every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat, plus this seat's own deliverables folder by clause 4.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O24-AC1`, `O24-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-24.the-manual-served-day.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O24-AC1,O24-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED.
⛔ **A `complete` flip is the end of the order**: flip only when O24-AC1 PASSES on the 09-10 manual artifacts and the instance validates rc=0 -- before 13:00Z; the scheduled fire is confirmation and never a gate. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, THREE times on this order: when the NEVER-2 entry is OPEN with both sign-off halves quoted (before step iii); when the manual report has landed (keys, VersionIds, `run_bundle.trigger`, the host stopped); and at the flip with the five re-read accepts indexed. Per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so; do not work around it.
