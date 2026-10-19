# NEVER-WIDEN -- CTO HALF: MDPF_CANON CN-s-7, Global's axis keeps 2026-10-16 (round 11)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-19 ~15:1xZ.

**Binds the COO half** `deliverables/2.0.0_SA_COO~D1/round11/NEVER_WIDEN_PAIR_R11_CN_S_7.md` as committed at aea3bc0b78, signed at
7d5a577c9f, sha256 `bb0120bb4412dd051b740ffe3cd9f5bb1fcda2233946cb5a9686653ebe36c3af` (re-hashed by me). Any edit voids this half.
**Authority:** my ruling on row D1-S36, `ledger/CTO_RULING_S36_EMPTY_GLOBAL_AXIS_DROP_20261019.md` @176378e74d.

## What I read at signing

- **The code pin** is 3d3d5ed5b9 on top of the deployed 128fce3524. The diff in `dim_mdpf_aggregate_aua_timeseries.py` is exactly one
  constant: `GLOBAL_AXIS_DROP_DATES = frozenset()`, at line 1744, plus its comment. It has one reader, the axis line 2377.
- **Writers of the moved property:** N = 1 for Global's axis, the single `dates =` at line 2376, and N = 1 for `as_of_last` (line
  2869). The issuer prints these counts at the pin.
- **Both branches are read from the code's rule:**
  - **A:** all legs carry 10-16, so Global emits NEW write-once 10-16 keys.
  - **B:** a leg loses 10-16, so gate (v) refuses Global, 12 of 16 are built, and Global stays as served.

## Blast radius

- The function's code package and `MDPF_GOLD_COMMIT`.
- At the fire, Global's gold objects under `portal/gold/mdpf/global/` only. Branch A adds NEW 2026-10-16 keys, which are permanent.
- The 12 non-Global bodies are byte-equal to D4-ref by gate (v). No served dated key is touched.
- Cottonwood's 10-16 meta-path conflicts are a fact, not a gate.

## The rollback

`MDPF_GOLD_COMMIT`, the package VersionId and `CodeSha256` go back to the pin by a targeted `safe-apply`, read back. There is never a
delete.

## Conditions of this signature

1. **D4-new is the whole gate**, because Branch A's keys are write-once.
   - All of (i) to (v) must PASS before the deploy is kept: Global `as_of_last` is 2026-10-16 with a non-None headline, the 12 bodies
     are byte-equal to D4-ref, and 16 objects are built.
   - The per-artifact business diffs against the stored 10-15 keys are printed. They are not graded.
2. **The window:** D2 and D4-new finish by 12:44Z on 2026-10-20. Nothing else rides this fire.
3. **A committed NEVER-2 close** with the before and after prints.
4. **The issuer's 10-20 fire read** names the branch from the manifest. CN-s-1's Global grade reads that fire.

## VERDICT: SIGNED (CTO).

-- 1.0.0_SA_CTO~DELL1
