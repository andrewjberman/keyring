# TO IRPT_DASHBD.TO-DB-b-255 -- the MEMORY of the Cottonwood landing function from a MEASUREMENT (round 125, workstream B-49F): one LOCAL dry-run of the merged handler with the real Black Diamond silver reader on 2026-07-10's real inputs and on the newest silver day, a sampler recording the resident memory, and the smallest standard Lambda size that keeps the peak under 70 percent (at least 512 MB); counts, seconds and megabytes only; nothing written

<to_id>IRPT_DASHBD.TO-DB-b-255</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~208</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>125</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 125 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-124 ANALYSIS (B-49F) section 2 ruling 2 and section 3 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_124_20261015.md @4285776c5c`: "The Cottonwood function's memory is set from a measurement, not copied from the sibling. One LOCAL run of the handler on 2026-07-10's real inputs (peak and duration). The packet sets memory at the smallest standard size that keeps the peak under 70 percent (at least 512 MB) and states the number") | **Rows:** IRPT_DASHBD-D2-W208-S<k> | **Decomp cell:** `DB-b-255` (decomposition section 123) | **outcome_ref:** FWD-11, FWD-21 | **depends_on:** none (it measures the merged handler; the guard and floor of `DB-b-254` change neither the inputs nor the work, only what is refused)

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-208` (branch `wk-IRPT_DASHBD-208`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~208/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~208/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The Terraform root of the Cottonwood landing function (`infra/aws/terraform/investor-reporting/account-return-daily/lambda.tf`) carries `memory_size = 8192`, copied from the 49 Financial sibling whose day is 4.7 million rows. The Cottonwood data is far smaller and the function's memory is unmeasured. The CTO ruled the memory is set from a measurement. This cell measures it. A READ: nothing is written, planned, applied or deployed.

**The cell (`DB-b-255`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_cotmem.py` (your two criteria; the rules and the record's exact form are in its docstring and clauses); round 122's script `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~200/stage_memory_r122.py` and record (how the sampler thread works: copy the idea into YOUR script, never import or edit it); the handler `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (`lambda_handler(event, context=None, s3=None, reader=None)`) and the adapter's `CottonwoodBlackDiamondSilverReader`.
2. **The script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~208/cot_memory_r125.py`: imports the handler of YOUR worktree (the way its tests do), builds ONE real `CottonwoodBlackDiamondSilverReader()` (GET and LIST only) and an `s3` argument that is an object with NO methods (any use of it would raise), and for each of the two days calls `handler.lambda_handler({"day": <day>, "dry_run": True}, None, s3=<that object>, reader=<the reader>)` while a background THREAD samples `psutil.Process().memory_info().rss` at most 1 second apart. The days are, in this order: `2026-07-10`, and the newest partition of `fact_allocations` (the checker lists it). Record per day the accounts and rows the derivation produced (from the handler's returned results), the seconds, and the day's highest sample. A day the handler HOLDS (an absent or empty silver partition) measures nothing: report it and stop on that point. The script names no other firm's place, holds no write call and writes only a private counts copy under your private folder.
3. **The rule** (the checker recomputes it): `peak_rss_mb` is the larger of the two days' peaks; the standard sizes are `[512, 1024, 1536, 2048, 3008, 4096, 6144, 8192, 10240]` MB; `chosen_memory_mb` is the smallest size, at least 512, with `peak_rss_mb <= 0.7 * size`.
4. **Record** `RD_COT_MEMORY_R125.json` in your folder with EXACTLY these fields: `firm` ("cottonwood"); `days` (two entries in the order above, each {`day`, `accounts`, `rows` (both at least 1), `seconds`, `peak_rss_mb`, `held` (false)}); `baseline_rss_mb` (the process before any read); `peak_rss_mb`; `threshold_fraction` (0.7); `sizes_mb` (the list above); `chosen_memory_mb`; `sampler` {`interval_seconds`, `samples` (at least 10), `method`}; `measured_on` {`where` ("local"), `words` (this machine; the process holds the interpreter, pandas, pyarrow and boto3, which a Lambda also holds, but nothing is subtracted; Lambda CPU scales with memory, so a smaller size runs the same work more slowly: say what the measured seconds imply for the 900 s timeout as an INFERENCE)}; `words` (one paragraph: the peak, the chosen size, how far it is below the 8192 MB the root carries today, and what the packet must set); `analysis` {`file` "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~208/cot_memory_r125.py", `sha256`, `tracked` true}; `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `claim`; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `day` field; no account id.

<criterion id="DB125-2-AC1" cell_refs="DB-b-255"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_cotmem.py" . DB125-2-AC1</invocation><expect>DB125-2-AC1 PASS</expect></criterion>
`DB125-2-AC1` -- `RD_COT_MEMORY_R125.json` has exactly the form of step 4; the days are 2026-07-10 and the newest silver `fact_allocations` partition the checker lists, neither held, each with at least one account and one row; `peak_rss_mb` equals the larger day peak; `chosen_memory_mb` equals the smallest standard size at least 512 with the peak under 70 percent of it; the sampler took at least 10 samples at 1 s or less; zero writes, flags false, no long digit run. Base: FAIL (no record).
<criterion id="DB125-2-AC2" cell_refs="DB-b-255"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_cotmem.py" . DB125-2-AC2</invocation><expect>DB125-2-AC2 PASS</expect></criterion>
`DB125-2-AC2` -- the script is tracked, its hash equals the recorded one, it samples `psutil` from a thread, calls the handler's `lambda_handler` with `dry_run`, uses the real silver reader, names no other firm's place and holds no write call. Base: FAIL (no script).

<expected_criteria>DB125-2-AC1,DB125-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the handler, the adapter, every test, every Terraform file, round 122's script and record, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the Cottonwood Black Diamond silver `fact_allocations` and `fact_transactions` partitions that the handler's reader reads. Writes: the repo files of the grant and the private folder. No put, copy or delete of any kind, no deploy, no Terraform, no push, no vendor call, no secret read, no read of another firm's place.
- **Client data.** Counts, seconds, megabytes, dates and words only; never an account id or a client value.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a day is held or a read is refused, record it, file a BLOCKING row with the phase and stop on that point; a held day is never a zero. If the run takes over 25 minutes or exhausts this machine's memory, file a BLOCKING row and stop. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W208-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~208/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-255.cottonwood-function-memory-from-a-measurement.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 123 (round 125, workstream B-49F), cell `DB-b-255`.
<owned_cells>DB-b-255</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB125-2-AC1, DB125-2-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~208/IRPT_DASHBD.TO-DB-b-255.cottonwood-function-memory-from-a-measurement.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB125-2-AC1,DB125-2-AC2` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the two days (accounts, rows, seconds, peak); the baseline; the chosen size and the 70 percent line it implies; the sampler (interval, samples); what the seconds imply for the timeout (inference). Counts, seconds and megabytes only: no account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a tracked measuring script and a counts-seconds-megabytes record in a branch; nothing is wired, served, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the S3 reads are GET and LIST of the two Black Diamond silver tables the adapter's reader already reads.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were dry-run at the base (no record, no script) and exercised by its self-test (one green and fifteen red record arms and the size rule).
lane: the <paths> block IS the grant.
</preflight>
