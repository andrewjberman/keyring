# AMGT_HARVST task order -- `HVST-au-1` -- ROUND 48 CHAIN A (round-47 analysis ruling 3; row Z-S87; CTO @acc5c6e750): THE DRIVER CATCHES ITS UPLOAD TIMEOUT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-au-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~96</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and plants with a stub collector. NO network, NO S3 call, NO collector run. Never run the backfill driver for real, `upload-harvest`, or the collector, and never touch any `.runtime` directory.
comp-adversary: RUN at L5 -- the adversary is a timeout that still escapes `drive()`, a stop that is written to the checkpoint but not printed (or the reverse), an auto-resume that loops past its budget, or a job-timeout path (already caught at `run_job`) that changes behaviour.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/backfill_driver.py`:
- `Collector.run_job` already catches `subprocess.TimeoutExpired` from the job spawn (around line 182) and returns status `error`.
- `Collector.upload` (around line 204) does NOT catch it. `_spawn` runs `subprocess.run(..., timeout=JOB_TIMEOUT_SECONDS)`.
- Measured on site Z (row Z-S87): an upload that ran past 14,400 s raised `subprocess.TimeoutExpired` out of `drive()`. The driver
  exited with a traceback, no `SUMMARY:` line, and no checkpoint status for the stop.
- `drive()` calls `collector.upload(pending)` after each job (around line 312). `STOP_STATUSES` and `TRANSIENT_STOPS` are at the top
  of the file (lines 34-42). A transient stop auto-resumes while `resumes[pub] < auto_resume`; otherwise the leg stops: the stop
  is written to `checkpoint["stopped"][pub]` and the run ends with its SUMMARY.

## 1. THE BUILD (LOCAL; stub collector only)

1. `Collector.upload` catches `subprocess.TimeoutExpired` and returns a value `drive()` can tell apart from an rc. Its docstring
   says so.
2. `drive()` treats an upload timeout as stop status **`upload_timeout`**:
   - add it to `STOP_STATUSES` and `TRANSIENT_STOPS`, with a comment naming row Z-S87;
   - within the auto-resume budget it resumes exactly as `error` and `upstream_unavailable` do;
   - past the budget, `checkpoint["stopped"][pub] = "upload_timeout"` is written and the driver ends normally: the summary file is
     written and `SUMMARY:` is printed.
   - Pending outbox objects are untouched; they upload on the next pass.
3. **Plants** in `lib/opal_data_harvest/test_au1_upload_timeout.py`, with a stub collector whose `upload` raises
   `subprocess.TimeoutExpired` (no network, a temp checkpoint):
   - (i) with `auto_resume=0`, `drive()` returns without raising, the checkpoint reads `stopped == {pub: "upload_timeout"}`, and
     the output stream carries a `STOP <pub>: upload_timeout` line;
   - (ii) with `auto_resume=1`, the first timeout resumes and the second stops;
   - (iii) `main()`-level: a run whose upload times out prints `SUMMARY:`;
   - (iv) a mutant that removes the catch makes (i) raise.
4. The collector suite stays green: `python -m pytest lib/opal_data_harvest -q`. Report the count.

Worktree: given in your spawn prompt (sparse cone, cut from CLOUD at the issuance commit).

<paths>
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/test_au1_upload_timeout.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~96/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-au-1"><invocation>python -m pytest lib/opal_data_harvest/test_au1_upload_timeout.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-au-1"><invocation>python -m pytest lib/opal_data_harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~96/AMGT_HARVST.TO-HVST-au-1.upload-timeout-caught.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-au-1.upload-timeout-caught`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-47 analysis @acc5c6e750 ruling 3 and enrichment item 1; decomposition section 61. Every collection leg is
stopped (Z-S89), so this lands with no stop-and-resume dance; a resumed leg picks it up from the working tree.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>48</round>
<slot>~96</slot>
<fabric>site-z</fabric>
