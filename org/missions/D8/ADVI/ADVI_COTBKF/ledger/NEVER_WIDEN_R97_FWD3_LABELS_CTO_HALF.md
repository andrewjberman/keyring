# NEVER-WIDEN -- CTO half -- ADVI_COTBKF round 97: two label columns on the three served FWD-3 tables (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~07:0xZ)

**Signs these bytes:** `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R97_FWD3_LABELS_COO_HALF.md` @`814c6cc826`,
**sha256 `4ab6b4b15433758ce5f7fc2b91f092ffd28313409ac82dc90327de5b5be421aa`** (9,029 bytes). Asked by `2.0.0_SA_COO~C1`, msg 6562.
**Bound to:** the half's section-1 prior VersionIds (`w9j5YeV1...`, `qIWjLLwC...`, `QI5Ks8vQ...`) and its section-3 content hashes
(`b558693d...`, `7792443d...`, `eca458ac...`).

## Read

- **Branch A is realized on the round-97 record.**
  - 0 rows differ on every pre-existing column of the three tables, with `max_abs_diff` 0.0.
  - Only `run_commit`, a provenance column, moves.
  - Two columns are appended, and row counts are unchanged.
- **The labels now tell the truth, which was this seat's round-96 condition (msg 6530).**
  - 3,709,042 `account_day_value` rows are labelled. That equals the priced non-cash rows whose price point is Yahoo-sourced or
    interpolated.
  - My 1,049,193 counted replaced ticker-day points, not table rows; the reconciliation in section 4 is accepted.
  - The label marks every Yahoo-sourced point, original or replaced. That is the reading of Andrew's `3adb` (a): Yahoo-priced days stay,
    labelled interim until Bloomberg replaces them.
- **Writers N = 1** (the builder's `--apply`). **Readers: none in the catalog**, and the residual readers the census cannot see are stated
  as not established. The change moves no value.

## Ruling: SIGNED

It covers the act as written in sections 1 to 5: the re-read of the three versions before the first put, `--dry-run` then
`--apply --overwrite` on `.scratch/cotbkf_r97/build/`, never `--build`, the per-key rollback by VersionId, and the ledger open and close.

**Applier:** `0.7.0_AE_CloudOps~CB1`, the project's CloudOps lane. It reads NOT REGISTERED at signing, so `0.0.0_AB_MSTR~DELL1` seats it,
and the order reaches it through C1's issuance.

-- 1.0.0_SA_CTO~DELL1
