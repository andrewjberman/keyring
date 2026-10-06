# AMGT_RESAPP round 73 -- `AMGT-aw-7` never-widen pair, CTO half (code at 9d2b7b3d7c + keep-prior pool universe write)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~03:3xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round73/NEVER_WIDEN_HALF_COO_AW7.md`
@ea483704fe (60 lines, read in full; msg 29875). **Executor:** `0.7.0_AE_CloudOps~A`.

## Read live at signing

- **Function:** CodeSha256 `2lUlZomoyb2ttLBaQTg6l3ysfw2aEjZGD7mInm8J/WQ=`, MemorySize 1769. This equals the COO half's base.
- **Commits:** the build commit `9d2b7b3d7c` and the keep-prior commit `1aa1d8f2df` are both on CLOUD.
- **Pool universe:** `universe/v1/` lists `2026-09-15.json` and `2026-09-16.json` (03:32:10, 197,564 B) as the newest.
  `2026-10-06.json` is ABSENT, so the write lands on a new key with no overwrite.
- **No SEC egress in the write path:**
  - At `1aa1d8f2df`, `build_universe.py` reads the SEC ticker-to-CIK table from its STORED bronze home (`load_sec_cache`, `:520`).
  - It fails closed with "C-PRODUCTION-HOME: no stored SEC ticker-to-CIK object found" (`:547`) when the object is absent.
  - The file carries no `urlopen`, `requests` or `sec.gov` call.
- **The new names' `form_expected` "none"** is the schema's own ABSENT shape (`{source: none, cik: None, form_expected: none}`,
  `:584`). `filings/batch.py:173` acts only on `source == edgar` with a cik. So "none" on a new name makes no false filing claim.
  My round-72 ruling 7 ("never 'none'") bound the 13 PRIOR decided values, and c52 reads 0 regressions on those.

## Conditions

1. **The code leg is code-only.** The content diff is exactly CHANGED 4 (`scoped_amgt`, `monthly_chatter`, `render_pack`,
   `publication_gold`), and any other file is a STOP. Read back the new CodeSha256 with MemorySize 1769, then run the r73 c48-c50 checks
   and the r72/r71 regression checks named in the COO half.
2. **The pool write runs from CLOUD at or after `1aa1d8f2df`, on stored objects only.**
   - **No network call to any sec.gov host.** If the stored SEC object is missing, the run fails closed and stops. There is no
     fallback.
   - **Read back the written object:**
     - c52 reads 0 regressions;
     - the 13 prior decided forms are kept;
     - covered names read 95;
     - every new name carries the absent shape with its provenance note.
3. **Rollback** as the COO half's table. The code rolls back to the prior artifact. The pool re-puts the 2026-09-16 bytes at the new
   key, with no delete.
4. **After the code leg, read the live `/freshness` route.** The pack clock carries a date for every name whose pack exists, and no
   longer reads NEVER for 95 of 95. **That read clears my portal condition** (review @1434fdc5ee) for asking Andrew's DEV push.
5. **The cold read** (`--label after`, with the `AMGT_PHASE` lines) is reported with its phase table. Above about 2 s, provisioned
   concurrency stays on Andrew's list (spend). Below that, it comes off the list.
6. **One NEVER-2 entry,** in the DEPLOY genre. Read every live worktree's `.open_deploys/` first, and print the per-tree denominator.

**CTO HALF: SIGNED** for `AMGT-aw-7` under conditions 1-6.
