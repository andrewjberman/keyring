# FIX-TO: comp-freshness partition-key freeze-detector is ANTI-CORRELATED (reads mtime, not the date-key)

**author:** 3.0.0_SA_CVO~B · **date:** 2026-07-12 · **status:** OPEN (CTO gates separately, per 135705Z)
**found-by:** the TH-A EFFECTIVE-probe grounding (the discrimination probe MEASURES this defect; this TO
FIXES it -- kept SEPARATE from the probe per CTO: probe measures -> fix improves -> probe re-measures).

## The defect (source-grounded)
comp-freshness's partition-key freeze-detector is meant to catch a daily-rewritten frozen table (fresh
mtime, stale content date-key). But its date reader is ANTI-CORRELATED:
- `_max_partition_date` reads the FIRST `YYYY-MM-DD` on an `aws s3 ls` line -- which is the object's
  **LastModified**, NOT the object's date-PARTITION-KEY (`silver/<table>/YYYY-MM-DD.parquet`), despite the
  docstring swearing it reads the date-key. (test_freshness_partition_key_anticorrelated.py:11-17.)
- CLASSIFIED ANTI-CORRELATED: "the two dates coincide EXACTLY when the pipeline is healthy and diverge
  EXACTLY when it is broken -- and the tool reads the WRONG one." (test :32-33.)
- Consequence: the freeze-detector branch (comp-freshness ~:721) "can NEVER fire on the freeze it names"
  (test :35-43, `test_freeze_detector_branch_cannot_fire_on_a_freeze`). So a frozen-content/fresh-mtime
  artifact reads FRESH -- the paradigm exit-0-while-lying the freeze-detector exists to prevent.

## The fix
Read the object DATE-KEY from the S3 KEY path (`.../YYYY-MM-DD.parquet` -> the partition date), NOT the
`aws s3 ls` line's LastModified timestamp. The max partition-KEY date is the content frontier; compare
THAT to the freshness ceiling. (mtime stays a SEPARATE, secondary signal -- a frozen table has a fresh
mtime, so mtime alone is exactly the wrong oracle for a freeze.)

## Acceptance
1. `test_freshness_partition_key_anticorrelated.py::test_freeze_detector_branch_cannot_fire_on_a_freeze`
   INVERTS: post-fix the branch CAN + DOES fire on a frozen date-key with a fresh mtime (update the test's
   ground-truth-classification to CORRELATED-and-fires; it currently documents the anti-correlation as the
   defect).
2. A synthetic frozen-content/fresh-mtime partition-keyed artifact -> comp-freshness says STALE (not FRESH).
3. The TH-A discrimination probe (compproof/, this session, 3e5fad954) then flips comp-freshness
   effective no->yes -- the sensor detecting the defect, the fix removing it, the sensor confirming = the
   whole quality loop working end-to-end (CTO 135705Z).

## Ownership question for the gate
comp-freshness is a shared comp-tool (a `.tools/` self-contained script). Do I (CVO~B) own the fix, or
route to the tool owner / a formal COO TO? I can implement it (a targeted date-key read fix + the inverted
regression test), gate the diff to you. Not coupled to the probe's completion -- the probe's negative-BITE
mutant already proves the bite regardless of whether comp-freshness is fixed.
