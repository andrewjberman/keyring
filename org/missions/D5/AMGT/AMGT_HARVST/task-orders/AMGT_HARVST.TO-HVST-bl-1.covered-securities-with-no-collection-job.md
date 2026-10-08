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

**COMPLETE 2026-10-08 ~08:5xZ (issuer):**
- **Built:** worker ~119 @4dbc4164ba; merged (hash in this close's commit message). No product file changed; no job run.
- **AC1 PASS:** CENSUS OK; 234 + 8 == 242.
- **Reconcile:** S3 1,248 records and 1,251 jobs; this device 1,161 records and 1,168 jobs; in both 1,158; S3 only 90 run ids
  (89 Seeking Alpha jobs and 1 Bloomberg, 2026-10-01 to 10-03, absent from the device files); device only 3 (2026-09-30,
  absent from S3). The reviewer's "323 securities with a job" counted raw keys in mixed forms; after the join it is 234.
- **NEVER COLLECTED: 8 of 242, not the 3 named so far:** `MRNA_US_Equity` Moderna (150 served pairs), `CAT_US_Equity` Caterpillar
  (85), `DG_US_Equity` Dollar General (51), `GEV_US_Equity` GE Vernova (48), `CSL_AU_Equity` CSL (39), `BE_US_Equity` Bloom
  Energy (29), `ED_US_Equity` Consolidated Edison (25), `6861_JP_Equity` Keyence (0). Together 427 of 48,358 served pairs,
  every one from an article collected for another name.
- **Per source, with at least one job:** bbg, wsj and barrons 234 of 242 each; Seeking Alpha 115 of 242; FT 3 of 242.
- **Collected but never stored** (every job of the security ended in a status other than `new_articles`): bbg 95 of 234, wsj
  185, barrons 200, sa 42 of 115, ft 2 of 3; on every source it has, 70 of 234.
- **Bound, row Z-W119-S1:** 240 of 1,258 jobs (58 collector keys whose per-job files carry no ticker) could not be joined to a
  covered security. The 8 is exact only if none of those 58 keys is one of the 8; a read of their stored article titles
  found none naming the 8 companies. Check line: CAT 0, CSL 0, AIG 6, Nokia 4, equal to the reviewer's.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<status>complete</status>
<round>67</round>
<slot>~119</slot>
<fabric>site-z</fabric>
