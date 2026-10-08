# AMGT_HARVST task order -- `HVST-bh-8` -- ROUND 62 (`1.0.0_SA_CTO~Z` msg 31493, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 1 @c75d056652): A SEEKING ALPHA JOB RECORD'S `finished_at` IS THE JOB'S OWN END, NOT THE RUN'S -- THE RUN RECORD CARRIES IT PER JOB; AN OLD RUN RECORD KEEPS ITS ADDRESS; NO EMIT, NO SWITCH CHANGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bh-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~113</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants only. NO S3 call of any kind, NO vendor or publisher host, NO collector run, NO `emit_job_records.py --write`. `.runtime` is not read or written. Two collection legs are LIVE on the shared tree and run this package: touch nothing outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a record already written whose address moves, a job written live and later emitted landing at two addresses, a changed config switch, or a plant with no negative control.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest` writes one job record per finished Seeking Alpha job (`job_record.py` `build_record`, `address`,
`write`; schema `lib/research/freshness/seeking_alpha_job_record.schema.json`, where `finished_at` is "when the job ended").
The record's object name is a stamp of `finished_at`, and a record is write-once at its address.

Today both writers take the RUN record's `finished_at`:
- the live writer, `worker.py` `_write_job_records` (`finished_at = record["finished_at"]`);
- the one-time emitter, `emit_job_records.py`, which reads the same run records back.
A run record's `jobs[]` entries carry no `finished_at` (`worker.write_run_record`); the job's own end time exists only in
`runs/<job_id>.json` (`result["finished_at"]`, set at the end of `run_job`). So every job of a multi-job run gets one
`finished_at`, the run's (row AMGT_HARVST-Z-W108-S2). The collector makes one-job runs today, so the two differ by milliseconds.

## 1. THE BUILD (LOCAL; no S3, no run of the collector)

1. **The run record** (`worker.py`): each `jobs[]` entry gains `finished_at`, the job result's own value.
2. **Both writers** read `job.get("finished_at")` and fall back to the run record's `finished_at` when the entry has none. ONE
   helper in `job_record.py` does this and both call it, so the live writer and the emitter cannot disagree.
3. **An old run record keeps its address.** A run record written before this change has no per-job value, so both writers
   give its jobs the run's `finished_at`, exactly as today: the emitter over old records computes the same addresses it did.
4. `seeking_alpha_job_record.enabled` in `config.json` is not changed. The schema file is not changed. No other field of the
   run record or the job record changes.
5. **Plants** in `lib/opal_data_harvest/test_bh8_job_finished_at.py` (no network; use the fixtures and the capturing client
   the existing `test_bf1_job_record.py` uses):
   - (i) a two-job run whose jobs end at different times yields two records with two different `finished_at` values, each
     the job's own, at two different addresses;
   - (ii) THE NEGATIVE CONTROL: an old-shape run record (no per-job `finished_at`) yields the run's `finished_at` for its job
     and the SAME address the current code computes -- assert the address string against one computed from the run's value;
   - (iii) a job written by the live writer and then emitted from its run record maps to ONE address (the emitter's write is
     `skipped_exists`);
   - (iv) the mutant: with the helper returning the run's value always, (i) gives one `finished_at` for both -- assert that;
   - (v) the run record's `jobs[]` entry carries `finished_at` equal to the job result's.
6. Run nothing against S3 and do not run `emit_job_records.py` in any mode that reads `.runtime` or writes.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/opal_data_harvest/worker.py
lib/opal_data_harvest/job_record.py
lib/opal_data_harvest/emit_job_records.py
lib/opal_data_harvest/test_bh8_job_finished_at.py
lib/opal_data_harvest/test_bf1_job_record.py
lib/research/freshness/seeking_alpha_job_record.schema.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~113/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bh-8"><invocation>python -m pytest lib/opal_data_harvest/test_bh8_job_finished_at.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bh-8"><invocation>python -m pytest lib/opal_data_harvest/test_bf1_job_record.py lib/opal_data_harvest/test_ba1_stopped_pair_is_retried.py lib/opal_data_harvest/test_az1_alias_set.py lib/research/freshness/tests -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W113-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~113/AMGT_HARVST.TO-HVST-bh-8.a-job-records-finished-at-is-the-jobs-own.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bh-8.a-job-records-finished-at-is-the-jobs-own`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31493, `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round60.md` ADDENDUM 1 @c75d056652. Decomposition section 76. Cut as round 62 because `.tools/to-pipeline-gate.py` admits one issuance per round and round 61's was committed (@fcf5542a36) minutes before the addendum; the analysis names these two as round 61's items 7 and 8.
- ADDENDUM 1: "Z-W108-S2, a job record's `finished_at` is the run's end, is the collector's cell"; the amended list's item 8.
- **Issuer rulings inside the decomposition** (no gate limb graded them): the per-job value rides the run record so the live
  writer and the emitter read one source; an old record keeps the run's value so no address already written moves.
- **The merge is the issuer's act and is not a plain drain:** two collection legs run this package from the shared tree, so the
  merge changes what the next Seeking Alpha job writes. It is merged with a change-management entry, after `1.0.0_SA_CTO~Z` and
  `2.0.0_SA_COO~Z` (the reader, `AMGT-bb-16`) have the change in one message; the first live record after it is read back.
- Chain of one, slot ~113. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2 base PASS as
  expected (count in the issuance commit).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>62</round>
<slot>~113</slot>
<fabric>site-z</fabric>
