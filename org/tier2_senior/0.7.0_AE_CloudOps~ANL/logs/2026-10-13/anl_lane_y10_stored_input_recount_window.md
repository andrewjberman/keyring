# Recount at the window: 56 template inputs, 0 turned back, 0 carry a reader_version -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-13
**Task Order:** IRPT_ANLREQ.TO-READS-Y10.stored-input-recount-at-the-window-laptop
**Status:** COMPLETE

---

## Objective

The Y9 count rerun at the window of the reader's release (read_at in the result), plus the number of stored template inputs that carry a `reader_version`, so the resident install can proceed (R0d, row S35).

## What was done

- Acked crossbox e261 (05:32Z). Step 0 as Y9 AMENDMENT 1: commit a665d34dd3 present, blob 09ddebd883, no write call; self-test exit 0 in a throwaway worktree at 35c3c4bd45 (removed). Both reader hashes equal the order's values.
- One run, exit 0, read_at 2026-10-13T05:35:03Z, 1946 items scanned: 56 template inputs (49financial 10, cottonwood 45, inflection 1), 56 read differently (one cause, a non-finding member), 0 turned back, 0 with a report, 0 unreadable. Identical to Y9; no template stored since.
- `reader_version_inputs`: 0 of 56 (0 per tenant), read by a separate read-only helper that imports the script's own read path (the script does not read that member); path stored document -> template -> reader_version. Recorded in `not_read`.
- Result `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y10_stored_input_count_r19_window.json`; scratch deleted.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| reads9_check | python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/reads9_check.py --result org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y10_stored_input_count_r19_window.json | PASS | READS9-OK |
| comp-iam | none | SKIPPED | read-only order; the identity read the table and bucket without a denial |

**What worked:** the Y9 procedure and amendment carried over unchanged.
**What failed:** nothing.
**Gap found:** the script does not read reader_version; the helper stands in and the result says so.
