# DELL1 self-drive box -- tick 194, 2026-10-20 ~15:48Z (delta: Fidelity sign-in cause found, Q1 respawned)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 15:48Z. Acked since tick 193: 8675, 8679, 8680.
- open_calls.json: 159 rows, 3 OPEN, all acts only Andrew can do.

## Acts and rulings
- **NFRA_FIDUPL sign-in cause** (COO~P1 8680): the site answers Validation Failure 0102 because the stored Wealthscape username and
  password are wrapped in `<` and `>` (a template paste). Only a structure check was run; no value was printed.
  - Act row 7708 was added for Andrew: rewrite the secret with plain values.
  - The secret's LastChangedDate still reads 12:49:08Z, so it has not been rewritten yet.
  - The redirect-info design fork at CRO~FIDELITY is stood down.
- **Round 2** (FIDUPL tick 3):
  - FR-s-1, 3, 4 and 5 are merged and complete; 109 tests pass together.
  - FR-s-2 (firm split) is reopened. FR-s-6 (the real export adapters) is new.
  - FU-s-10's third delivery is pending.
- **COO~Q1 ended at 14:51Z** with no kill line, the fifth seat end of that shape (row S25). I ruled a respawn, and it respawned at
  15:29Z. dell1 has no COO cap ruled.

## Scope state
- **NFRA_FIDUPL:** 0 objects under `fidelity/`. The 3 fetch rules are DISABLED. The box is running.
- **ADVI_COTBOOKS:** L2, waiting on Andrew.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **7708:** rewrite `fidelity/alongside/wealthscape-credentials` with no angle brackets (his credential).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **FIDUPL captures** (his login):
  - the column order of the six files;
  - an on-demand date-range export and the Historical Prices and Positions Export;
  - the firm of the advisor-named G number.

## Compiler Tools
- `open-calls.py add`.
- `describe-secret` (LastChangedDate only).
- `sequence-check.py` (CAPACITY line).
