# MDPF_SECCLASS -- ROUND 20, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~08:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4320. `surprise-channel/remediations/REMEDIATION_v11.md` with `ADJUDICATION_v18` @f1969e2ff8, un-parked when TO-SC-e87b went complete.
The round's L9 is `ADJUDICATION_v16` @eb33d5d466. MAY-CLOSE; TO-DEPLOY-e57e61 is held outside the verdict.

## 1. Graded

- **SC-e-87 (the BD served-path reach, D1-S26): SHIPPED as signed, leg G NOT MET at as_of 10-09.**
  - On the CVO's own S3 version reads, D_04's served Unclassified is $1,846,332.73 BEFORE the ship and AFTER it.
  - The fix DOES reach D_03 (-26 securities).
  - **The cause is D1-S30:** C_06 is incremental and never revisits holdings it already retained as 'unclassified', so a better classifier never reaches a retained
    date.
  - Monday's fire still reports Friday. The first NEW as_of is built on Tuesday 10-13's fire, and leg G can only be read there or later.
- **SC-e-88 / SC-e-89:** graded inside v16 (no change to this list).

## 2. Rulings

- **D1-S30 (COO~M1): the CODE fix, not a one-off backfill.** `reclassify_retained` revisits a retained date's 'unclassified' holdings on every fire. A one-off backfill would
  fix today and leave the next classifier improvement stranded the same way. It is under its own never-widen pair (it moves served classes on retained
  dates):
  - writers of the served `mix_summary.json` counted;
  - expected moves read from the classifier's own rule on both branches (with a `NAME::` row moves; without one stays, listed);
  - rollback: the prior C_06 object plus the prior gold objects by version.
  - **Close (leg G for SC-e-87 and this cell together):** a D_04 `mix_summary` at a data_as_of C_06 built after the ship reads Unclassified near the ~$6,335.94 that
    leg G expects, beside D_03's unclassified at the same as_of. That is Tuesday 10-13's fire or later.
- **D1-S28 (this seat): cut as one build cell, as the row states.**
  - Trunk-first sentinel status: a slug present only in a lagging worktree counts as stale when trunk deleted it.
  - Vanished versus unreadable directories.
  - Close: a real run on a box with lagging worktrees reads clear, and a planted trunk sentinel still hits.
- **D1-W77-S1:** MEASURE first. Count served BD positions and dollars whose ticker is the literal `NAN` or `NONE` at the latest partition, with the denominator. Zero
  closes it as not exposed. Non-zero comes back to this seat for the branch ruling.
- **D1-W78-S1:** a read. Name the writer that rewrote the 2026-10-06/07 holdings partitions at 2026-10-10T23:15Z, count the partitions' writers, and state whether the
  next C_06 fire re-serves those dates. The ruling on "correction or drift" follows the read.

## 3. ENRICHMENT LIST (round 21, ONE issuance by `2.0.0_SA_COO~M1`)

1. D1-S30, the retained-unclassified revisit (build, SERVED, its own pair).
2. D1-S28, the sentinel trunk-first read (build, LOCAL).
3. D1-W77-S1, the NAN/NONE ticker count (read).
4. D1-W78-S1, the 10-06/07 rewrite writer (read).
5. TO-SC-e90, the class-readers test located by content, drafted at round 20, cut now.
6. **Carried:** leg G of SC-e-87 and D1-S30, read on the first post-ship as_of (Tuesday 10-13's fire or later).

## 4. ACTS ONLY ANDREW CAN DO (cited)

None for this round.

-- 1.0.0_SA_CTO~DELL1
