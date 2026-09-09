# TO ETFS_GUARDRAIL.TO-EG-s-14 -- THE AUGUST RE-RENDER: the SAME monthly orchestrator started by hand with the rule's own payload, the August report re-published to the served key WITH the coverage line, delivered to both inboxes -- a served-output move under a NEVER-2 entry with both never-widen halves quoted

<to_id>ETFS_GUARDRAIL.TO-EG-s-14</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- issued in round 2's ONE issuance on PRD v0.4 @`a830ea1cc0` (the manual-trigger addendum on Andrew's ~21:4xZ word: "we are not going to just wait for October and hope it works, that needs to be closed out and proven"), s.9 row S14; decomposition v0.2 s.8-s.11. FIRST on slot ~1; EG-s-15 and EG-s-16 follow on the same slot. The base COO drives round 2 (2.0.0_SA_COO~B is not seated).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.4 (s.9 row S14; s.0 the carve-out; s.6 rulings 3 and 5) | **Decomp cell:** `EG-s-14` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.2, s.8-s.11) | **outcome_ref:** FWD-3, FWD-5, FWD-6 | **verb:** verify | **depends_on:** none (round 1 built the coverage line `EG-s-5`, the gate `EG-s-6`, the JOIN `EG-s-9` and the alignment `EG-s-13`; this order EXERCISES them on the real August month)

---

## THE CELL

`EG-s-14` (PRD s.9 S14): the published August CSV at `s3://opal-data-etfs/platinum/reports/2026-08/` ends on its numeric rows and PREDATES round 1 -- so FWD-3 (the coverage line on a SERVED artifact) and FWD-5 (delivery at both inboxes on a monthly fire) graded NOT_EVALUATED "on the 10-01 fire". Under the manual-trigger rule the fire is MADE: the SAME target the rule invokes (`etfs-reports-monthly-run` -> `arn:aws:lambda:us-east-1:313476888478:function:etfs-reports-orchestrator`, `Target.Input` `{"mode":"run"}`, `infra/aws/terraform/etfs-reports/orchestrator.tf:178-188`), invoked by hand with THAT payload. The handler's `run` mode renders LAST month (`lambda_function.py:81-88 _last_month()`, `:383`), so a `run` invoked in September renders 2026-08 -- the August re-render is the rule's own behaviour, not a copy of it. The reporter box starts, renders with `--gate` (EG-s-8's seam, S8-AC9), publishes the PDF/HTML/CSV to the served key, SES-sends the report to the JOINED recipients (aj@opalinvest.com + andrew@opalinvest.com, EG-s-9), and stops. 10-01 confirms; nothing waits for it.

⛔ **THE FIVE CONDITIONS OF THE RULE, ON THIS ORDER:** (1) SAME TARGET -- the Lambda ARN the schedule targets, the payload `{"mode":"run"}` byte-equal to the schedule's `input`; (2) REAL PLANE -- the served key, the real inboxes; this is a SERVED-OUTPUT MOVE: the NEVER-2 entry is OPENED FIRST and BOTH never-widen halves are quoted in it (the COO's half = the hash of the issuance that created this file, `git log -1 --format=%h -- <this file>`; the CTO's half = the message id GIVEN IN YOUR PROMPT); (3) TOLD APART ON THE ARTIFACT -- read step (d) below; (4) the schedule's OWN firing from history is `EG-s-18`'s cell, not yours; (5) the 10-01 fire is CONFIRMATION.

⛔ **NEVER-2, THE ENTRY, THE ARCHIVE AND THE ROLLBACK.** Before the invoke: `python .tools/deploy_ledger.py open --slug etfs-guardrail-eg-s-14-august-rerender ...` (read `python .tools/deploy_ledger.py open --help` for the leg shape; legs: the archive, the invoke, the served objects, the delivery-send, the box stopped) naming the served keys the run will REWRITE (`platinum/reports/2026-08/etf_ownership.pdf`, `.html`, the CSV -- read `_report_keys` at `lambda_function.py:90-105` and `render_month_end.py`'s `--s3-out` layout for the exact names), the PRIOR objects ARCHIVED before the run (read `get-bucket-versioning` on `opal-data-etfs`: if ENABLED, the archive is the pinned VersionId of each prior object, listed; if not, `copy-object` each prior object to `platinum/reports/2026-08/_archive_<UTC>/<name>` and record both sha256s -- byte-equal), the ROLLBACK (one `copy-object` back per key from the pin or the archive), and the two sign-off ids. The entry + its sentinel are COMMITTED (their paths are in `<paths>`). **No object is deleted** (NEVER-AUTO-DELETE; S3 deletes need a human's word).

⛔ **DELIVERY AT THE INBOXES IS THE ISSUER'S READ, NOT YOURS.** You hold no mailbox instrument. Your criteria prove the SEND (the SES `MessageId`s in the orchestrator's CloudWatch log for this run, one per recipient or one with both destinations, and CloudTrail `SendRawEmail` for the run's minute); `2.0.0_SA_COO` reads the two inboxes through the gateway and cites the message ids on this face by amendment. Do not send anything yourself; the orchestrator's run is the one send.

## DELIVERABLE

1. The ledger entry (opened before, every leg closed with proof after) + its sentinel, COMMITTED.
2. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs14_august_rerender.py` -- the battery, and `the-august-re-render.result.md` -- criteria verbatim with rc and denominator, the invoke's request id and UTC, the archive table (key, prior sha256, VersionId or archive key), the served objects' LastModified after, the SES MessageIds, the box's state transitions, and any row you filed.
3. The proof-of-spec instance (below).

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** A path you need that it does not name is a BLOCKING row, never an override.
- **YOUR AWS IDENTITY IS THE LAUNCHING SEAT'S** (decomposition s.3 decision 1): every invocation and its output are recorded VERBATIM in the proof instance; the CVO grades what was printed.
- **NO CODE CHANGE, NO DEPLOY under this order.** The orchestrator and the renderer run AS DEPLOYED by round 1; if the deployed renderer does NOT carry the coverage line (`# coverage:` absent from the served CSV after the run), that is a FINDING against round 1's deploy -- a BLOCKING row naming the served vs built hashes -- never a hot fix.
- **NEVER `aws lambda update-function-code`. NEVER bare `terraform apply`.** (You apply nothing here.)
- **The carve-out (PRD s.0):** the terminal SES send belongs to `EG-s-15`'s refusal path; this order's send is the ordinary monthly delivery to the JOINED recipients, which the orchestrator already performs. No topic, alarm, monitor, schedule or env var is added by you.
- **EVERY invocation is bounded.** `timeout 120` on reads; the orchestrator invoke itself returns in seconds (it starts the box and returns); the RUN takes minutes on the box -- poll the served key and the box state with bounded reads, at most every 60 s, for at most 30 minutes; a run still absent at 30 minutes is recorded as NOT-LANDED with the box's state, never waited on further.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>` (append; cite `path@commit`; never edit an existing row).
- **NEVER `git push`.** Report push state as MEASURED (`git ls-remote origin refs/heads/CLOUD`).

## ACCEPTANCE

<criterion id="S14-AC1" cell_refs="EG-s-14"><invocation>timeout 900 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs14_august_rerender.py</invocation><expect>EGS14-AUGUST-RERENDERED</expect></criterion>
`S14-AC1` -- a battery you write, printing the token ONLY when every arm holds: (a) the ledger entry exists, was opened BEFORE the invoke (its opened-at precedes the invoke's UTC), names the served keys, the archive table (prior sha256 per key) and the rollback, and quotes BOTH sign-off ids; (b) the schedule read LIVE (`aws scheduler get-schedule --name etfs-reports-monthly-run`): `State ENABLED`, `ScheduleExpression cron(0 10 1 * ? *)`, timezone `America/New_York`, `Target.Arn` = the orchestrator's ARN, `Target.Input` `{"mode":"run"}` -- and your invoke used THAT ARN and THAT payload (`aws lambda invoke --function-name etfs-reports-orchestrator --payload '{"mode":"run"}' out.json`; the shim is CLI v1 -- pass the payload as a plain JSON string; record the response's `StatusCode 200` and the `x-amzn-RequestId`); (c) `_last_month()` on the invoke day resolves to `2026-08` (print `python -c` against the handler's own function, imported from the file); (d) after the run: the served CSV's LAST ROW begins `# coverage:` and carries the month's denominator (trading days in 2026-08 per `lib/trading_calendar.py`, printed beside it), the PDF and HTML exist at the publish keys with `LastModified` after the invoke (UTC), and each prior object's archive sha256 matches what you recorded before -- printed as a table; (e) TOLD APART: CloudTrail `Invoke` for the function in the run's minute shows the invoking identity = the launching seat's user (not `etfs-reports-scheduler-role`), and the orchestrator's CloudWatch log for the run carries the request id from (b); if any served artifact carries a trigger/run-id field, print it; if none does, PRINT `ARTIFACT-CARRIES-NO-TRIGGER-FIELD` and file the row (the OUTSET carrier's shape is a cut question for the issuer); (f) the SEND: the orchestrator's log shows the report send with its SES `MessageId`(s) and `Destinations` naming BOTH aj@opalinvest.com and andrew@opalinvest.com (JOIN, ruling 3), and CloudTrail `SendRawEmail` in the run's minute; (g) the reporter box is `stopped` at the read (`describe-instances`). Denominators on every list; every S3 time in UTC via `s3api`.

<criterion id="S14-AC2" cell_refs="EG-s-14" judgment="true"/>
`S14-AC2` -- graded by the CVO at L9: FWD-6's alignment re-read on the LIVE render (the three partners' as-of aligned on the served August artifact, `EG-s-13`'s qualifier), the served CSV before vs after (numeric rows unchanged, the coverage line added -- a diff, printed), what the run wrote beyond the three publish keys (`coverage_verdict.json`, `coverage_unresolved.json` if any, under the month prefix), and the one thing this order cannot see -- delivery at the inboxes, the issuer's read. Evidence with vintage. NO VERDICT.

<expected_criteria>S14-AC1, S14-AC2</expected_criteria>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
No code path is granted: this order runs, reads and records. The ledger directory and the sentinel are named so the NEVER-2 entry can be COMMITTED. `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py`, `data/etfs/scripts/presentation/render_month_end.py` and `lib/trading_calendar.py` are READ (import the handler's `_last_month` and `_report_keys` for the battery's own checks; never edit).

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.2, cell `EG-s-14`.
<owned_cells>EG-s-14</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~22:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names ETFS_GUARDRAIL, etfs-reports-orchestrator, the reporter box, the two daily producers or opal-data-etfs (0 hits for those tokens across the ledger output). BLIND SPOT, stated: the gate ledger cannot see a served-output rewrite -- the NEVER-2 entry and the two sign-off halves ARE that control, named in the accept.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight -- this order grants nothing and applies nothing; the orchestrator's reach (S3 Put on `platinum/reports/*`, `ses:SendRawEmail`, the reporter instance start/stop) was read at L5 round 1 (16 calls / 9 statements) and is exercised as deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a verify cell over a mechanism round 1 built; the controls are the archive sha256s, the schedule read and the CloudTrail initiator.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants (your deliverables folder, this face's `<status>`).
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S14-AC1`, `S14-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-14.the-august-re-render.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> S14-AC1,S14-AC2` BEFORE the complete flip, which you commit yourself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when S14-AC1 PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (what you measured, what you ran, each criterion's output verbatim with rc and denominator, the ledger entry's path and hash, the rows you filed, push state as MEASURED). You cannot send or receive messages -- anything you would ask is a surprise row. The issuer hands you `EG-s-15` next by continuing you.
