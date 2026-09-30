# Never-widen sign-off packet -- the resident st2 -> st3: a saved portfolio type other than fixed refuses a tolerated setting

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-29 ~01:5xZ.
**Asked by:** ~Y 102524 (the resident + generate build of @ec8f69f718), ~Y 102429/102430. **Order:** TO-IB-yr-1
(drained by ~Y @ec8f69f718; Y19-1-AC1 1 passed, AC2 2 passed; proof VALID). **Ledger:**
`irpt-resident-saved-type-st3-20260929` (U1 closed, D1 open).

## 1. What ships

| change | commit | files |
|---|---|---|
| the read-back records the saved portfolio's type when the settings come from a saved portfolio | ec8f69f718 (build 0a1fc245cb) | ycharts/generate/recipe.py (+1 line) |
| the worker keeps that field in the read_back checkpoint and raises `WorkerAttention("TOLERANCE_REQUIRES_STATIC")` when any read-back row is tolerated and the saved type is present and not `fixed` | ec8f69f718 (build 0a1fc245cb) | ycharts/generate/resident_worker.py (+6/-1) |

`git diff 12a67ed5ee ec8f69f718` on the two files is exactly this change (7 insertions, 1 deletion).

**Generate Lambda: NOT moved.** irpt-ycharts-generate imports `recipe` only for `load_templates()`
(`reports/generate_installed.py:130`), which this change does not touch; `step_read_back` runs on the resident only.
Its packaged recipe.py / resident_worker.py stay the resident-side "STALE" members already named in the GRANT packet.

## 2. The one move

**D1 -- the resident** `fe64236bbb-st2` -> `fe64236bbb-st3`
- Built by `build_resident_package.py --pin fe64236bbb` with st2's 12 overrides (read from the st2 tar's bindings
  provenance), recipe.py and resident_worker.py re-pinned 12a67ed5ee -> ec8f69f718.
- SUMS vs st2: 225/225; ONLY recipe.py (982d8171 -> 4fde9ac9), resident_worker.py (9b2dbd18 -> 95f79dad) and
  resident_bindings.json (generated_at) differ. Tar 266 members = st2's 266.
- Tar `26769a37..` at `ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st3.tar.gz`, S3 version
  `vDS2rcSqdOEi90kjFAV5oadXrF7hlHSP`, read back by version: sha equal.
- `resident_host_install_st3_20260929.sh` (sha 87c70e76) = st2's script with NEW/OLD/KEY/tar/recipe/worker shas and the
  receipt's ledger changed only: 10 member shas checked, factory pre-check on resident_main.py's own sys.path, stops
  the unit only on an empty queue (0/0), rolls back to st2 automatically on rc != 0, not active, no poll, or a
  Traceback in 30 s.

## 3. Blast radius -- both branches

Writers of the job outcome (irpt-jobs status for an Analysis generation): 1 -- `ResidentGenerationWorker`; its rule is
read at `resident_worker.py:200-215` @ec8f69f718.

- **Branch A (moves):** a job whose settings come from a SAVED portfolio (`settings_source == "saved_portfolio"`),
  whose read-back has at least one TOLERATED row (today only `level_as_of_type`, 12a67ed5ee), and whose saved
  `model_portfolio_type` is not `fixed`. Today: generation proceeds with the tolerated value. After: the job stops
  before `step_validate` with ATTENTION `TOLERANCE_REQUIRES_STATIC`; no report is generated or published for it.
- **Branch B (unchanged):** every other job -- no tolerated row, a saved type of `fixed`, a type the vendor did not
  return (None), or settings not from a saved portfolio. A job resumed from an st2 checkpoint lacks the field, reads
  None, and proceeds as today.
- **Nothing else moves:** no Lambda, no table schema, no IAM, no queue. The checkpoint gains one key.
- **Reachable:** Analysis submissions, which today means the walk windows.

## 4. Apply protocol

1. ~Y runs its four gates on the BUILT st3 (S3 version vDS2rcSq) and posts PASS.
2. Both halves at HEAD naming this file's blob.
3. LIVE before-read: running root `fe64236bbb-st2`, queue 0/0 (script line 1).
4. SSM run of the install script; running root + member shas read back; polls and 0 Tracebacks.
5. Any unnamed difference means a same-turn rollback to st2 (the script's own limb, or a re-run of st2's install).

**Rollback per key:** the resident root `fe64236bbb-st2` stays on the host; the cutover receipt is copied to
`cutover_receipt.fe64236bbb-st2.json` before the write.
