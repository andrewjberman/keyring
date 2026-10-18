# NEVER-WIDEN -- CTO HALF: `HVST-cn-3`, the 93-name deliberate dossier refresh (round 99)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~18:3xZ.

**Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round99/NEVER_WIDEN_HALF_COO_CN3_DOSSIER_REFRESH_DELIBERATE_RUN.md` as
committed at 184cfe4b73, sha256 `f4bff167da62e20e9f8a22a1aaee2268cb828b3e989053a13db2175fd0b285e8` (re-hashed by me). Any edit to that file
voids this half. The earlier bytes (ca850150 @45bf9ebe6b) carried a budget line no instrument enforced. My one named edit (msg 8204)
replaced it, and the diff changes only that line.

## What I read at signing

- **The writer of the property (N = 1).** `dossier.write_one` at 56bacbc853 (`dossier.py:1651`):
  - it first reads the newest stored object's inputs, and writes nothing when they are equal;
  - otherwise it puts a new object beside the old one, in the partition `store.entity_partition`. Gold never overwrites.
  - Its one production caller is `dossier_refresh.py`. I did not re-run the COO's census of callers; it is printed in the half.
- **The guard.** `dossier_refresh.guard_facts` reads the record through `dossier._model_block_read` on the same client
  (`dossier_refresh.py:232-234`), since `build()` returns no record. That is the reader I confirmed at cl-4.
- **The budget is the driver's own:** `BUDGET_REQUESTS=14000` and `BUDGET_BYTES=1.8 GiB` on the read client
  (`dossier_refresh.py:61-62`, `BudgetExceeded`). cm-4's 95-name read used 5,720 gets and 919 MB, so one process fits.
- **The dry run** (`refresh_run_dry.out`): `names=95 would_write=93 unchanged=1 skipped_guard=1 errors=0`.
  - NG is level.
  - PBR is a correct guard stop: one `BEST_DPS` FY1 figure is absent from the 10-18 block (cn-2).

## Blast radius

- **93 gold keys are added under `amgt/harvest/gold/research_dossier/`.** 92 are plain partitions, and BP is at
  `security_key=BP-SLASH-_LN_Equity/`.
- **Served moves:** `model_rows` to the 10-18 block, plus `dossier_key`, `content_sha256`, the dossier entry of `source_keys` and the
  counts.
- **Nothing else moves:**
  - all other served values stay equal;
  - KMB's new dossier cites today's continuation, and no continuation is written;
  - no overwrite and no delete.
- **Rollback:** ADD-ONLY. Removing the manifest's keys is an S3 delete, which is Andrew's act and is not pre-approved here.

## Both branches

The half covers both branches, and I accept them as written:
- Branch A (a name WRITTEN): read back, A-1 to A-3;
- Branch B (a name SKIPPED by the driver): nothing written, the partition count unchanged, no retry.

## Conditions of this signature

1. **The code pin.** The worktree is AT 56bacbc853, with `git diff 56bacbc853 HEAD -- lib/research` printing empty. Any diff is a STOP.
2. **Condition 1 of cl-4, now A-3:** the guard's printed block key must equal the written object's `inputs` model-block key. A mismatch
   is a STOP for that name.
3. **Site Z is told first** and answers CLEAR before the GO (C-10). No other dossier writer may run in the window, and the window closes
   by 12:30Z on 10-19.
4. **The measurement is the point of the run.** Step 2's wall time in seconds goes to my addendum-2 rule: over 600 s, cn-4's host is
   Fargate. This run executes from dell1, so its wall time includes the box-to-S3 path. It counts as an upper bound for an in-region
   Lambda, not a reason to slice.
5. **The NEVER-2 entry** is opened at start and the close is COMMITTED, with the manifest's 93 keys (or the count written) in it.

## Not covered

The schedule (cn-4/cn-5, its own pair), PBR, NG, any second run, and any change to the build rule or the driver.

## VERDICT: SIGNED (CTO).

-- 1.0.0_SA_CTO~DELL1
