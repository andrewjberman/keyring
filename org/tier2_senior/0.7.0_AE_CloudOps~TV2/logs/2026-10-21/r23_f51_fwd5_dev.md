# TCKT_VNEXT TO-R23-F51 -- FWD-5 on DEV: a picker claims one of two open tickets from the board (0.7.0_AE_CloudOps~TV2)
**archetype:** VALIDATE

Result: RUN-OK (fwd5), check blob c3efc11f3d, R23-FWD5-SELFTEST-OK (32 mutants). Ledgers f51 (stopped at S65), f51b, f51c, f51d (final); GO 11773, amendments 1 to 5 (V2 11795, 11809, 11821, 11828; CTO 11794, 11808, 11820, 11825, 11835).

- Filer and picker are staff-shaped synthetic rows (firmId opal-capital, scope_all_firms BOOL true, no allowedFirmIds). Two tickets filed through the page's form (a Service Request and an Other), ids read back from the table. The picker, in its own context, read both rows from the board (type, age, Claim control), chose the Service Request, pressed Claim in the row without opening either: 200. Chosen ticket in_progress under the picker with events created then claimed; the other open.
- Evidence: private full-board shots OUTSIDE the repo (sha256 only in the result); committed clips r23_rows_before (two rows), r23_rows_claimed (the chosen row on In Progress), r23_other_row_after_claim, each read before written and viewed after. Items saved whole by hand (the first script's get-item call lacked .cmd).
- Deviation: a SECOND picker token (03:36:18Z, 10 minutes, GETs only) to take the two post-claim clips after part 1 stopped on this seat's stale-DOM read; CTO msg 11835.
- Removal 03:46:23Z after both exps: tickets and rows deleted by key, read ABSENT; the protected tickets and Andrew's ticket untouched.
- This seat's faults along the way: a label pattern for single quotes (served uses double); a response-listener race lost a ticket id (that stopped ticket was deleted without being saved whole); the get-item call lacked .cmd; a stale-DOM row read after the tab switch; shots written before they were reviewed (deleted, row S66).

## Compiler Tools
- `deploy_ledger.py` open, close-leg, close (f51b, f51c, f51d): worked. `r23_fwd5.py`, `r23_fwd5_clips.py`: run; `r23_fwd5_check.py` and `--self-test`: worked. `commit-gate.sh`: caught unused names. Gaps: the committed-shot review is the DOM text of the rows plus a human view after writing; there is no pre-write image reader.
