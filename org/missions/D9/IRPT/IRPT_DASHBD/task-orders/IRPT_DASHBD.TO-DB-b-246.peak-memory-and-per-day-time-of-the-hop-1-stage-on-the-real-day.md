# TO IRPT_DASHBD.TO-DB-b-246 -- the PEAK MEMORY AND PER-DAY TIME of the hop-1 `filled_report_values` stage on the real day (round 122, workstream B-49F): the stage's two reading functions run LOCAL for the newest returns day with a sampler recording the process's resident memory, against 70 percent of the function's configured memory; the verdict WHOLE_DAY or CHUNK and the chunk rule; counts, seconds and megabytes only; nothing written

<to_id>IRPT_DASHBD.TO-DB-b-246</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~200</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>122</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 122 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-122 ANALYSIS (B-49F) section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_122_20261015.md @e690365741`: "First cell: measure peak memory and per-day time on the real day at the configured memory. If peak memory is over 70 percent of the configured memory, chunk the households inside the day; the cell states the chunk rule") | **Rows:** IRPT_DASHBD-D2-W200-S<k> | **Decomp cell:** `DB-b-246` (decomposition section 120) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-200` (branch `wk-IRPT_DASHBD-200`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~200/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~200/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 121 measured the stage LOCAL for one real day: 4,012 households and 4,693,967 rows, 85.3 s to read the inputs and 76.3 s to build the day (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~196/RD_STAGE_MEASURED_R121.json`), so the stage goes to one invocation per owed day (CTO ruling B). Its MEMORY was not measured; the function has `memory_size = 3008` (MB, `infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf`). A day built as Python objects may not fit. This cell measures the peak resident memory of one real day and states whether the household loop must be chunked. A READ: nothing is written, planned, applied or deployed.

**The cell (`DB-b-246`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_mem.py` (your criteria; the rules and the record's exact form are in its docstring and clauses); round 121's script and record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~196/stage_measure_r121.py` and `RD_STAGE_MEASURED_R121.json` (how the handler is imported, the population `accounts` and the counting client: copy what you need into YOUR script, never import or edit it); the handler's `filled_inputs`, `filled_day_rows` and `run`.
2. **The script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~200/stage_memory_r122.py`: imports the handler of YOUR worktree, makes a boto3 S3 client, takes the same population round 121 used for the newest returns day, and runs `filled_inputs` then `filled_day_rows` for that day exactly once, while a background THREAD samples `psutil.Process().memory_info().rss` at an interval of at most 1 second (record the interval, the number of samples and the method). Record the resident memory at the start (`baseline_rss_mb`), the highest sample at the end of `filled_inputs` (`peak_after_inputs_mb`) and the highest sample over the whole run (`peak_rss_mb`), in megabytes (1 MB = 1,048,576 bytes), and the two times. It calls NO writing function (`filled_write`, `filled_stage`, `emit_filled`, any put/upload/`stream_to_parquet` are refused by the checker even in a comment), writes no file but a private copy of the numbers under your private folder, and names no other firm's place. The process also holds other things (the interpreter, pandas, pyarrow): say so in the words; do not subtract them.
3. **The rules** (the checker recomputes them): `configured_memory_mb` is read from `lambda.tf`'s `memory_size`; `threshold_mb = 0.7 * configured_memory_mb`; `day_seconds = read_inputs_seconds + build_day_seconds`; `verdict` is `CHUNK` when `peak_rss_mb > threshold_mb`, otherwise `WHOLE_DAY`; when `CHUNK`, `chunk_rule` = {`households_per_chunk` = max(1, floor((threshold_mb - peak_after_inputs_mb) / ((peak_rss_mb - peak_after_inputs_mb) / households))), `basis` (words)}, and when `WHOLE_DAY` it is null.
4. **Record** `RD_STAGE_MEMORY_R122.json` in your folder with EXACTLY these fields: `firm` ("49financial"), `day` (the newest returns partition date; the checker lists S3), `configured_memory_mb` (integer), `threshold_fraction` (0.7), `threshold_mb`, `accounts`, `households`, `rows` (integers, each at least 1), `read_inputs_seconds`, `build_day_seconds`, `day_seconds`, `baseline_rss_mb`, `peak_after_inputs_mb`, `peak_rss_mb` (positive numbers; baseline <= after inputs <= peak), `sampler` {`interval_seconds`, `samples` (at least 10), `method`}, `verdict`, `chunk_rule`, `measured_on` {`where` ("local"), `words` (this machine; a Lambda's memory is the function's allocation and its Python build may differ: say whether you expect the Lambda peak to be higher or lower than this process's as an INFERENCE, never as a measurement)}, `words` (one paragraph: what was measured, the peak against the line, the verdict, the chunk rule when there is one, and what the split build must therefore do), `analysis` {`file` "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~200/stage_memory_r122.py", `sha256`, `tracked` true}, `reads` {`s3_reads` (the requests you counted), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `day` field.

<criterion id="DB122-1-AC1" cell_refs="DB-b-246"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_mem.py" . DB122-1-AC1</invocation><expect>DB122-1-AC1 PASS</expect></criterion>
`DB122-1-AC1` -- `RD_STAGE_MEMORY_R122.json` has exactly the form of step 4; `day` equals the newest `account_return_daily` partition the checker lists; `configured_memory_mb` equals `lambda.tf`'s; the threshold, `day_seconds`, the verdict and (when CHUNK) the chunk rule equal the checker's arithmetic; the sampler took at least 10 samples at 1 s or less; zero writes, flags false, no long digit run. Base: FAIL (no record).
<criterion id="DB122-1-AC2" cell_refs="DB-b-246"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_mem.py" . DB122-1-AC2</invocation><expect>DB122-1-AC2 PASS</expect></criterion>
`DB122-1-AC2` -- the script is tracked, its hash equals the recorded one, it imports the handler, calls `filled_inputs` and `filled_day_rows`, samples `psutil` from a thread, names no other firm's place and holds no write call. Base: FAIL (no script).

<expected_criteria>DB122-1-AC1,DB122-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the handler, the module, every test, every Terraform file, round 121's script and record, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET the stage itself makes through the handler's functions. Writes: the repo files of the grant and the private folder. No put, copy or delete of any kind, no deploy, no Terraform, no push, no vendor call, no secret read.
- **Client data.** Counts, seconds, megabytes, dates and words only; never an account id or a client value.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a read is refused, or the run takes over 25 minutes or exhausts this machine's memory, file a BLOCKING row with the phase and the last sample and stop. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W200-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~200/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-246.peak-memory-and-per-day-time-of-the-hop-1-stage-on-the-real-day.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 120 (round 122, workstream B-49F), cell `DB-b-246`.
<owned_cells>DB-b-246</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB122-1-AC1, DB122-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~200/IRPT_DASHBD.TO-DB-b-246.peak-memory-and-per-day-time-of-the-hop-1-stage-on-the-real-day.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB122-1-AC1,DB122-1-AC2` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the population, households and rows; the three memory marks, the two times, the line and the verdict; the chunk rule if any; the sampler (interval, samples); anything the split build must state. Counts, seconds and megabytes only: no account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a tracked measuring script and a counts-seconds-megabytes record in a branch; nothing is wired, served, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the S3 reads are GET and LIST of prefixes the stage itself reads.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were dry-run at the base (no record, no script) and exercised by its self-test (two green and ten red record arms, two text arms).
lane: the <paths> block IS the grant.
</preflight>
