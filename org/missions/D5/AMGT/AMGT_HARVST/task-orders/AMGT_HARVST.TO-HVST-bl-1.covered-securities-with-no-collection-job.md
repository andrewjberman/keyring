# AMGT_HARVST task order -- `HVST-bl-1` -- ROUND 67 (`1.0.0_SA_CTO~Z` msg 31631 (R18), on `3.0.0_SA_CVO~Z`'s grade of `bk-1` @e84dcdce42): THE COVERED LIST LESS THE SECURITIES THAT EVER HAD A COLLECTION JOB -- BY SUBTRACTION, BOTH DENOMINATORS PRINTED, THE TWO RUN-RECORD COUNTS RECONCILED FIRST; NO JOB IS RUN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~119</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL script and records, plus READ-ONLY reads: S3 GET of the collector's uploaded run records and of the newest gold part, and a read of run-record files under the shared tree's `.runtime`. NO put, NO delete, NO job of any kind, NO collector, backfill_driver or emitter run, NO vendor or publisher host. One collection leg is LIVE and writes under that `.runtime`: open its files read-only, copy nothing back, touch nothing else outside your worktree.
comp-adversary: RUN at L5 -- the adversary is a set printed without both denominators, a zero read from one store taken as a zero in the other, a job run to see what it returns, or a cause asserted where only a request was read.
</preflight>

## 0. THE CELL

The collector (`lib/opal_data_harvest`) has only ever run as a per-security backfill: one job for one security per source.
A reviewer read the run records on this device and found that `CAT_US_Equity` and `CSL_AU_Equity` have NO job at all: their
served pairs come from articles collected for other names (`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND66_BK1_COLLECTION_GAP_GRADE_20261008.md` @e84dcdce42). Those are two members of a set whose
size nobody has printed.

Two counts of the run records disagree and must be reconciled FIRST:
- `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~116/bk1_per_source_per_day.out` read 1,248 run records and 1,251 jobs through
  `lib/research/harvest/publication_gold.py` `_iter_run_records()` (the records the collector uploads to S3);
- the reviewer read 1,161 files, 1,168 jobs, 323 distinct securities with a job, from the files on this device, under
  `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\opal-data-harvest*\run_records\` (the SHARED tree's runtime folder; your worktree has none; read it
  read-only at that absolute path).

The covered list is the served gold list `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/securities.universe.r64.json` (242 securities).

## 1. THE BUILD (read-only; NO job, NO collector run)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~119/bl1_never_collected.py`.
2. **Reconcile first.** Print for each store: files or records read, jobs, distinct run ids, distinct securities with a job,
   and per source the job count. Then `IN S3 ONLY: <n> run ids`, `ON THIS DEVICE ONLY: <n> run ids`, `IN BOTH: <n>`, with five
   example ids for each one-sided set and what distinguishes them (a runtime root, a date range, a source). If a job's
   security is named two ways in the records (a collector id such as `security-<hash>` and a `gold_security_key`), print
   which field you joined on and how many jobs lack it.
3. **The subtraction**, on the UNION of the two stores: `COVERED: 242`; `WITH AT LEAST ONE JOB: <j> of 242`;
   `NEVER COLLECTED: <242 - j>`, and the same three lines per source (bbg, wsj, barrons, sa, ft). A security with a job is
   one with any job in any status. Also `SECURITIES WITH A JOB THAT ARE NOT ON THE COVERED LIST: <x>` (the reviewer's 323
   is larger than 242).
4. For EVERY never-collected security: security_key, company, and its served pair count from the newest gold part
   (`pg._latest_gold_snapshot_rows(pg.GOLD_TABLE)`), largest first. Write the full list to `BL1_NEVER_COLLECTED.md` and
   `.json`; print the first 25 in the output.
5. `CAT_US_Equity: jobs <n>; CSL_AU_Equity: jobs <n>; AIG_US_Equity: jobs <n>; NOKIA_FH_Equity: jobs <n>` on the union, as a
   check against the reviewer's 0, 0, 6 and 4.
6. Also print, per source, the securities with a job whose EVERY job ended in a status that stored nothing (name the
   statuses you count as such), as a count only: `COLLECTED BUT NEVER STORED, per source`.
7. Last line: `CENSUS OK` only if both stores were read with a count above 0, the reconcile lines printed, and
   `WITH AT LEAST ONE JOB + NEVER COLLECTED == 242`. Otherwise `CENSUS FAIL` and the failing condition. Write the output as
   `bl1_never_collected.out`.
8. A store that cannot be read is a FINDING, printed whole; do not treat it as empty. Change no product file.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/store.py
lib/opal_data_harvest/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/securities.universe.r64.json
org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND66_BK1_COLLECTION_GAP_GRADE_20261008.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~116/
.runtime/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~119/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bl-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~119/bl1_never_collected.out</invocation><expect>CENSUS OK</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W119-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~119/AMGT_HARVST.TO-HVST-bl-1.covered-securities-with-no-collection-job.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bl-1.covered-securities-with-no-collection-job`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31631 (R18), on `3.0.0_SA_CVO~Z`'s grade of `bk-1` @e84dcdce42. Decomposition section 81.
- R18: "Cell one: the census by subtraction, the covered list (242 securities at round 64) less the securities with a job, printed
  with both denominators, the worker's 1,248 and the CVO's 1,168 reconciled first; Caterpillar and CSL are two members of a set
  whose size nobody has printed." "Neither cell runs a job."
- `.runtime/` is in `<paths>` so the shared tree's run-record files may be READ; nothing is written there.
- Slot ~119's queue: `bl-1`, then `bl-2`. **Checks dry-run at the base:** AC1 base FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>67</round>
<slot>~119</slot>
<fabric>site-z</fabric>
