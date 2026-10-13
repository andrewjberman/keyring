# ADVI_COTBKF decomposition -- ROUND 85 (issuer 2.0.0_SA_COO~C2 on dell2; drafted 2026-10-14T00:05Z) -- ONE cell, then the PARK

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 7343 (2026-10-13 23:17Z), RULED: "'active' = an account OPEN at Black Diamond in the latest snapshot, cash-only included; not a 90-day window. ... Rerun the set and the reverse match with: open at BD on the latest snapshot (any position, cash included).
Print the new count against 769 and against the 90-day 875, re-hash, and keep the exemption current. Then I carry the path and counts to dell1. Fold it into round 84's drain if the gate allows; otherwise it is round 85's one cell before the PARK."
The gate does not allow a second order into round 84 (one issuer per round number), and the cell depends on round 84's output (the committed closed list `NONE_REASON_LIST.md` and the reasons for the 273), merged @cdca442759.
PRD v0.10 @4d488ab2f0, no addendum. The backfill floor (record @82c7c92449) and the ruling on row D2-S131 bind.

**Why a rebuild and not an append (measured by round 83/84 workers):** the salt that tokenised the Commonwealth-side keys and 312 of the 769 Black Diamond keys of the round-82 files is in no committed file and its worktree is gone (rows W164-S1, W164-S3, W167-S2). Old keys therefore cannot be re-derived or joined to a raw snapshot. The new files are keyed by the RAW account number on both sides, which Andrew's word (client data in the private git is fine, record `ANDREW_DIRECT_20261009_192xZ_*`) allows;
the rebuild is checked against the round-82 files by AGGREGATE invariants (below), not by key.

**Rule 24.** Domain: the CTO's ruling (new definition; rerun both files; counts against 769 and 875; re-hash; the none-row reasons by the committed list). -> ONE cell.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-cg-1` | the active set and the reverse match rebuilt under "open at Black Diamond on the latest snapshot, cash included", raw keys, reasons for every `none` row by the committed list; invariants against the round-82 files; counts against 769 and 875 | FWD-3 | LOCAL | CB-cf-1 (merged) | `0.9.0_WK_ADVI_COTBKF~168` |

**Fan-out:** `1 of 1 chain, cap 8`. Read-only on S3 and the tree. The two new files are written OUTSIDE the repository; their commit into the deliverables folder, their sha256 and the scan-test exemption are the ISSUER's acts at the drain (ONE exemption commit that also retires the two round-82 pins if the new files replace them).
