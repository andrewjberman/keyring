# NFRA_DEVPLN PRD v0.1 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108802. 2026-10-13 ~16:4xZ.
**Verdict:** REFUSED. Two contract defects. The ENDPOINT itself traces to Andrew's approved decisions (a)-(e).

## What was read

- PRD at 1e49544e05 (v0.1), unchanged at HEAD; ratified-text half_hash `b23953fbd682fa72eb61f7ac159bd3b26d369bb36b2575151a8b1ab76cb811f1`.
- The brief `docs/briefs/nfra-devpln-per-box-portal-dev-approval-brief-20261013.md` @5386676d4f (F1, Part V).
- Andrew's approval of the five decisions, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md`
  lines 15-23.

## What holds

FWD-1 to FWD-7 trace to the brief's O1-O7 and decisions (a)-(e). Each EXERCISED outcome is provable by an act, and FWD-3, FWD-5
and FWD-6 carry refusal or keep-back arms. C-APPROVAL reuses the open-calls row (one record, COMM_ASSIST as a reader).
C-SETTLE merges, never rebases.

## Why refused

1. **C-PROMOTE does not make FWD-5 true.** FWD-5's ACCEPT: "a half-done or unapproved change on DEV at promote time does not reach
   clients". C-PROMOTE merges the listed feature branches into a release branch cut from PROD, and refuses only "a promote whose
   list names an unapproved branch". C-BRANCH does not say where a `cand/<box>/<slug>` branch is cut from. A branch cut from DEV
   carries every DEV commit beneath it, approved or not, so merging it into the release ships those commits. The list check never
   reads them. FWD-1's own clause ("a promote that also carried something nobody approved fails it") would then fail on the first
   real promote.
   **Fix (either one):** C-BRANCH cuts every feature branch from the last PROD release, never from DEV; or C-PROMOTE refuses a
   release in which any commit not already on PROD lacks an `Approved-By` trailer tracing to an approved row. Either is one
   sentence.
2. **C-MERGE-FORWARD removes an Andrew-granted carve-out without his word.** The gate's FAST-lease portal-DEV admission was
   approved by Andrew on 2026-09-24 and is CLAUDE.md law ("Under a live FAST lease, the lease's seat lands product changes on portal
   DEV itself"). C-MERGE-FORWARD collapses the four admissions to "the merge-forward script's commit, and the integrator". Andrew's
   "yes agreed for all of this" approved the brief's "reconciled into the approved route" (Part V). It did not approve removing the
   FAST route, and the PRD does not say how that route is reconciled. Removing it is also a CLAUDE.md law edit that the PRD does not
   name.
   **Fix:** C-MERGE-FORWARD states the FAST-lease route's fate in one line: kept, with Andrew's presence under the lease counted as
   the approval (the script reads the live lease as the approval row); or removed, citing his explicit word. In either case it names
   the CLAUDE.md Portal-section edit as owed.

## Note (not blocking)

FWD-7's "the approval step costs Andrew less attention than reviewing PROD after the fact does today" has no read that proves it.
Make it a measured read (for example, his answers per promote against today's per-promote PROD review), or move it to the brief.
