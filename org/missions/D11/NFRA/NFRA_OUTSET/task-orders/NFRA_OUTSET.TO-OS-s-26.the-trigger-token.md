# TO NFRA_OUTSET.TO-OS-s-26 -- THE TRIGGER TOKEN: the orchestrator writes a token before it starts the host, and the runner stamps `run_bundle.trigger` / `run_bundle.run_id` from it

<to_id>NFRA_OUTSET.TO-OS-s-26</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>complete 2026-09-10T13:22Z -- O26-AC1 PASSES by its own output (OS26-TRIGGER-TOKEN-CARRIED, rc=0 captured UNPIPED, 5 arms / 5 evaluated / 0 FAIL); proof instance VALID rc=0. The carrier is proven END TO END on the real plane: the orchestrator's token @QRHqSjmNPdImTp_rmka.gCcoK1MLWfDR carries run_id a588a7ea-8ad2-4f03-a814-4f02668a66d6 and the served report carries the SAME id -- matched on the ID, never on the clock. Both negative arms were produced WITHOUT a served-key write, and the same function's fresh-token positive control returned 'scheduled', so neither negative is a constant. O26-AC2 RECORDED with evidence and NO verdict for 3.0.0_SA_CVO at L9, including the stated blindness (a forged trigger from a third caller is trusted; the only control is IAM). Arm (e), the published 'scheduled' reading, printed NOT-YET-FIRED at grading and is CONFIRMATION the face says is never waited for. PRIOR STATUS: pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.8** @`dc6a33c3e3` (the manual-trigger addendum v0.7 @`0d44fdd1ee` amended on this seat's four cut-shaping facts, 94739/94751; Andrew's ~21:4xZ word "we need to not be 'waiting' on anything"), s.9 row OS-s-26; decomposition v0.7 s.27-s.30. FIRST of the three: OS-s-25 and OS-s-24 read their artifacts through the field this cell carries.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.8 (s.9 row OS-s-26) · **Decomp cell:** `OS-s-26` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.7, s.27-s.30) · **outcome_ref:** FWD-3 (rule (3)'s carrier) · **verb:** build · **depends_on:** none (buildable now; OS-s-25 and OS-s-24 depend on it)

---

## THE CELL

`OS-s-26` (PRD s.9, evidence **absent**): the served report's `run_bundle` carries exactly `{coverage, run_pin, stages, started_at}` -- a git commit and a clock -- and there is NO channel from an invoke to the runner: `estate-report-orchestrator`'s handler ignores its event (`StartInstances` and return; the rule's `Target.Input` `{"mode":"daily-run"}` is decoration on both paths) and the runner starts from a systemd oneshot at boot (`0.7.0_AE_CloudOps~W`, 94738, measured 21:5xZ). So a manual run and a scheduled run are told apart by NOTHING but the clock, which the manual-trigger rule (3) forbids. This cell builds the carrier, in your own shape (i), adopted by the CTO.

⛔ **THE MECHANISM, AS THE PRD WRITES IT.** The orchestrator writes ONE small object BEFORE `StartInstances`: `s3://opal-estate-report/config/last-trigger.json` carrying `{trigger, run_id, invoked_at}` -- `trigger` taken from the rule's payload for a scheduled fire and `manual` for a hand invoke; `run_id` minted per invoke; `invoked_at` in UTC. The runner reads it at boot and stamps `run_bundle.trigger` and `run_bundle.run_id`. **The field's domain is `{scheduled, manual, UNKNOWN}`, and an ABSENT token or a STALE one (its `invoked_at` older than this boot) reads `UNKNOWN`, never `scheduled`** -- a missing token that reads as a scheduled claim is the confident-zero shape this project keeps meeting. Not an instance tag (a stale tag reads fresh), not CloudTrail inference (a second system, lagging).

⛔ **HOW THE ORCHESTRATOR KNOWS WHICH PATH IT IS ON, since it ignores its event today:** read the event. The rule's payload carries `mode`; a hand invoke carries what the invoker sends. The face fixes the contract: the scheduled rule's `Target.Input` stays `{"mode":"daily-run"}` and maps to `trigger=scheduled`; a hand invoke sends `{"mode":"daily-run","trigger":"manual"}` and maps to `trigger=manual`; any other event shape maps to `UNKNOWN` and still starts the host (the token is evidence, never a gate on the run). State the mapping in the deliverable; OS-s-24's invoke uses exactly that manual payload.

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-trigger-token.result.md` -- what you measured, what you built, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## BOUNDS

- **Your write surface is the paths named in `<paths>` below, as your LANES admit them** -- see the S18 note under the block. A path you need that neither names is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).
- **NEVER bare `terraform apply`** -- `safe-apply` only. **NEVER `aws lambda update-function-code`** -- the orchestrator's code ships through Terraform, as it does today.
- **No alarm, monitor, freshness-checker or SNS** (standing moratorium). **NEVER-AUTO-DELETE (PRD R-5) is absolute** for every served and seam key; the token key is the orchestrator's own config object and its planted-absent negative arm is exercised at the runner's READ function against the real bucket (below), never by deleting a served artifact.
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

⛔ **THE GRANTS ARE EXACT-KEY AND CHANGE-MANAGED.** The orchestrator's role gains `s3:PutObject` on `config/last-trigger.json` only; the runner's role gains `s3:GetObject` on that one key only; both in `estate-report/iam.tf` under `safe-apply`, the applied reach re-read after (comp-iam; the four false-deny modes named in the preflight). No widening to `config/*`.

⛔ **THE RUNNER UPLOAD IS A DEPLOY UNDER ITS OWN NEVER-2 ENTRY (the OS-s-19 shape):** `estate_report_runner.py` gains the token read and the two stamps; the deploy is the S3 upload of the runner (`instance.tf:94-96`) with the served ETag equal to md5 of the HEAD blob, the control from OS-s-19 (a different blob's md5 does NOT match). It does NOT replace the host (no `user_data` change; `instance.tf:83` not triggered). The CloudComp half named in the PRD (the runner's fields) is seated on you because the runner directory is inside your lane's grant (resolved at this cut); the seam module is not touched.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="O26-AC1" cell_refs="OS-s-26"><invocation>timeout 600 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os26_trigger_token.py</invocation><expect>OS26-TRIGGER-TOKEN-CARRIED</expect></criterion>
`O26-AC1` -- a battery you write, proving THE CARRIER END TO END ON THE REAL PLANE: (a) the POSITIVE arm reads OS-s-24's manual served day's report (2026-09-10 keys): `run_bundle.trigger == "manual"` and `run_bundle.run_id` present and EQUAL to the token the orchestrator wrote for that invoke (the token object's `run_id`, head-object + get-object with the invoke's UTC), never inferred from `started_at`; (b) the two NEGATIVE arms are exercised at the runner's own token-read function against the REAL bucket, without a served-key write: with the token key ABSENT the function returns `UNKNOWN` (the key read via head-object 404 beside a 200 on a present key as the control), and with a STALE token (`invoked_at` older than a supplied boot instant) the function returns `UNKNOWN`; a token whose `invoked_at` is newer than the boot instant returns its `trigger` value (the positive control of the same function); (c) the grants read on the APPLIED plane: the orchestrator role's Put reach is exactly the one key and the runner role's Get reach is exactly the one key (comp-iam or `get-role-policy`, DESIRED == APPLIED, printed), with a negative control (a sibling key under `config/` is NOT reachable); (d) the runner's served ETag equals md5 of the HEAD blob, with the OS-s-19 control; (e) the 13:00Z scheduled fire's report, IF PRESENT at the read, carries `run_bundle.trigger == "scheduled"` -- read as CONFIRMATION and recorded, never waited for. Denominators on every list; `timeout 600`.

<criterion id="O26-AC2" cell_refs="OS-s-26" judgment="true"/>
`O26-AC2` -- THE CARRIER'S SHAPE AND WHAT IT CANNOT SEE: the event-to-trigger mapping as built, the token's fields, how the runner decides STALE (the boot instant it compares against and where it reads it), the two grants' applied reach before and after, the runner deploy's NEVER-2 entry (opened before, closed after, ETag control), and the one blindness worth stating -- a token written by a third caller with a forged `trigger` value is trusted (the carrier proves provenance of the INVOKE, not of the caller's honesty; the exact-key Put grant is the whole defence). Evidence with vintage. NO VERDICT.

<expected_criteria>O26-AC1, O26-AC2</expected_criteria>

<paths>
infra/aws/terraform/estate-report/
infra/aws/lambda/estate-report-orchestrator/
infra/aws/ec2/estate-report-runner/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
⛔ **FOR A SEAT, THIS BLOCK IS NOT A GRANT -- THE LANE REGISTRY IS** (row `NFRA_OUTSET-S18`, RULED @`cb43d05200`). Every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat at this cut (22:2xZ) -- the terraform module, the orchestrator Lambda, the runner directory, both ledger folders, the channel by lane ANY -- and this deliverables folder by clause 4 (the resolver names it TREE_DELIVERABLES / nobody-by-enumeration and admits the serial in the path). The negative control `org/modules/heatmap/outset_seam.py` read VIOLATION for your serial: it is READ, never edited.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.7, cell `OS-s-26`.
<owned_cells>OS-s-26</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~22:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_OUTSET, the estate-report host or runner, the orchestrator, the consumption seam, comp-heat or fedobs (0 hits for those tokens across the ledger output). BLIND SPOT, stated: this lens reads the GATE LEDGER and cannot say whether a Put/Get grant or a Lambda change is otherwise constrained -- comp-iam's plane, required of the assignee below.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight, and REQUIRED OF THE ASSIGNEE as the cell's own instrument -- both roles' reach on the one token key read on the APPLIED plane before and after the grants. Run `comp-iam refresh-census` BEFORE any APPLIED-plane use (24 h TTL). FOUR false-deny modes are live (a CONDITIONED grant, a batched multi-ARN call, a WRONG-GRAIN resource ARN, and the census's role-only reach per S20). Positive-control any deny you intend to act on.
comp-adversary: DECLARED-NOT-APPLICABLE -- a fresh cut with no prior artifact to validate against.
lane: for a SEAT the lane registry is the grant and the `<paths>` block only narrows it (row S18, RULED @`cb43d05200`); every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat, plus this seat's own deliverables folder by clause 4; the seam module refused as the negative control.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O26-AC1`, `O26-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-26.the-trigger-token.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O26-AC1,O26-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED.
⛔ **A `complete` flip is the end of the order**: flip only when O26-AC1 PASSES on OS-s-24's manual served day and the instance validates rc=0. The build lands tonight; the flip follows the manual day. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, TWICE on this order: once when the carrier is BUILT and deployed (the orchestrator's mapping, the two grants' applied reach, the runner's served ETag under its entry; the negative arms at the read function), and once at the flip. Per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so; do not work around it.
