# TO IRPT_DASHBD.TO-DB-b-242 -- the MEASURED RUN of the hop-1 `filled_report_values` stage (round 121, workstream B-49F): the stage of the 49 Financial reporting-gold handler run LOCAL against the real gold with nothing written, the time of reading its inputs and of building a day, the fire estimate against the 600 second line, and the verdict SHARE_FIRE or OWN_INVOCATION; counts and seconds only

<to_id>IRPT_DASHBD.TO-DB-b-242</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~196</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>121</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 121 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-121 ANALYSIS (B-49F) section 2 ruling 2 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_121_20261015.md @9d4bd6adf3`: "a measured run of the stage against the real gold, LOCAL, counts and duration only, before the pair is applied. The stage shares one invocation with the earlier tables, so a run near the 900 s ceiling would time out the whole fire after the earlier writes. If the measured duration is over 600 s, the pair splits the stage into its own invocation") | **Rows:** IRPT_DASHBD-D2-W196-S<k> | **Decomp cell:** `DB-b-242` (decomposition section 119) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-196` (branch `wk-IRPT_DASHBD-196`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~196/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~196/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 120 merged a GUARDED `filled_report_values` stage into `infra/aws/lambda/investor-reporting/reporting-gold/handler.py`: `filled_inputs(s3, firm, accounts)` reads EVERY partition of the returns, activity, realized-lot and class tables, the newest unrealized-lot partition, the served model series and the household crosswalk; `filled_day_rows(inp, firm, day, accounts)` builds one day's rows; `filled_write`/`emit_filled` write (you will NOT call those). The stage shares the 07:41 fire with the earlier tables inside the function's 900 second timeout, and nothing has measured it. This cell measures it, LOCAL, so the apply pair can state a number and the CTO's rule can choose SHARE_FIRE or OWN_INVOCATION. A READ: nothing is written, planned, applied or deployed.

**The cell (`DB-b-242`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_measured.py` (your criteria; the rule, the record's exact form and what the checker recomputes are in its docstring and clauses); the handler (`run`, `filled_stage`, `filled_write`, `filled_inputs`, `filled_day_rows`, `filled_households`, `MAX_DAYS_PER_FIRE`) and its stage tests `tests/test_filled_report_values_stage.py` (how the handler module is imported and how a fake client is used: copy the import style).
2. **The script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~196/stage_measure_r121.py`: it imports the handler of YOUR worktree, makes a boto3 S3 client (default credentials, region us-east-1), and (a) takes the population `accounts` the scheduled stage would pass for the newest returns day (the accounts of the newest `account_return_daily` partition of the firm, the way `run` derives them; read `run` and say in the record's words exactly which set you used), (b) times `filled_inputs(s3, "49financial", accounts)` with `time.perf_counter()` (read_inputs_seconds, including every S3 read it makes), (c) takes the newest returns day as `day` and times `filled_day_rows(inp, "49financial", day, accounts)` (build_day_seconds; if you build more than one day, `days_built` is the number of days and build_day_seconds is the TOTAL for them), counting `households` (the second value it returns) and `rows`, (d) counts the S3 requests the client makes (wrap the client to count GET and LIST calls; it must have no put/copy/delete). It calls NO writing function (`filled_write`, `filled_stage`, `emit_filled` and every put/upload/stream_to_parquet are refused by the checker even in a comment), writes no file but a private counts copy under your private folder, and names no other firm's place.
3. **The estimate and verdict** (the checker recomputes them): `fire_estimate_seconds = read_inputs_seconds + max_days_per_fire * build_day_seconds / days_built`, with `max_days_per_fire` read from the handler's `MAX_DAYS_PER_FIRE`; `verdict` is `OWN_INVOCATION` when the estimate is over `threshold_seconds` (600), otherwise `SHARE_FIRE`.
4. **Record** `RD_STAGE_MEASURED_R121.json` in your folder with EXACTLY these fields: `firm` ("49financial"); `day` (the newest returns partition date; the checker lists S3 for it); `max_days_per_fire` (integer, the handler's); `threshold_seconds` (600); `accounts`, `households`, `rows`, `days_built` (integers, each at least 1; households <= accounts <= ..., rows >= households); `read_inputs_seconds`, `build_day_seconds`, `fire_estimate_seconds` (positive numbers); `verdict`; `measured_on` {`where` ("local"), `words` (this machine, its network path to S3, and how that differs from a Lambda in us-east-1: say whether you expect the Lambda to be faster or slower on the S3 reads, as an INFERENCE, and say nothing about it as a measurement)}; `words` (one paragraph: what was measured, the population used, the verdict, and what the pair must state); `analysis` {`file` "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~196/stage_measure_r121.py", `sha256`, `tracked` true}; `reads` {`s3_reads` (the requests you counted), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `claim` ("measured"); `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `day` field.

<criterion id="DB121-1-AC1" cell_refs="DB-b-242"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_measured.py" . DB121-1-AC1</invocation><expect>DB121-1-AC1 PASS</expect></criterion>
`DB121-1-AC1` -- `RD_STAGE_MEASURED_R121.json` has exactly the form of step 4; `day` equals the newest `account_return_daily` partition the checker lists; `max_days_per_fire` equals the handler's constant; the estimate equals the rule's arithmetic within half a second and the verdict follows the 600 second line; households <= accounts and rows >= households; zero writes, flags false, no long digit run. Base: FAIL (no record).
<criterion id="DB121-1-AC2" cell_refs="DB-b-242"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_measured.py" . DB121-1-AC2</invocation><expect>DB121-1-AC2 PASS</expect></criterion>
`DB121-1-AC2` -- the script is tracked, its hash equals the recorded one, it calls the stage's `filled_inputs` and `filled_day_rows` through the handler, names no other firm's place and holds no write call. Base: FAIL (no script).

<expected_criteria>DB121-1-AC1,DB121-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the handler, the module, every test, every Terraform file, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET the stage itself makes (the firm's irpt gold tables, the household crosswalk and the served model series object) through the handler's functions. Writes: the repo files of the grant and the private folder. No put, copy or delete of any kind, no deploy, no Terraform, no push, no vendor call, no secret read.
- **Client data.** Counts, seconds, dates and words only; never an account id or a client value.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a read is refused (AccessDenied on the served series or the crosswalk is a FACT the pair needs: record the surface and the refusal in a BLOCKING row, record `claim` "absent" and stop on that point), or the run takes over 20 minutes, file a row with the phase and stop. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W196-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~196/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-242.measured-run-of-the-hop-1-stage-against-the-real-gold-duration-and-counts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 119 (round 121, workstream B-49F), cell `DB-b-242`.
<owned_cells>DB-b-242</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB121-1-AC1, DB121-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~196/IRPT_DASHBD.TO-DB-b-242.measured-run-of-the-hop-1-stage-against-the-real-gold-duration-and-counts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB121-1-AC1,DB121-1-AC2` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the population, households, rows and days built; the two measured times and the estimate; the verdict; the S3 request count; anything the pair must state. Counts and seconds only: no account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a tracked measuring script and a counts-and-seconds record in a branch; nothing is wired, served, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the S3 reads are GET and LIST of prefixes the stage itself reads.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were dry-run at the base (no record, no script) and exercised by its self-test (a green and seven red record arms, two text arms).
lane: the <paths> block IS the grant.
</preflight>
