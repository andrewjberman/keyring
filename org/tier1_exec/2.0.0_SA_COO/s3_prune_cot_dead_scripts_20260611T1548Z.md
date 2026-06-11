# Andrew-direct destructive-op record — cot gold S3 dead-script prune

**When:** 2026-06-11 ~15:48Z
**Authorization:** Andrew direct (1535Z): "yes, delete the 30 dead script copies" — explicit human confirmation per CLAUDE.md (deleting S3 objects requires human confirmation).
**Executor:** 2.0.0_SA_COO
**Op:** delete 31 dead script copies from `s3://opal-data-cot/code/gold/`

## Context
DS's NFRA_DTAFLP.TO-1c (commit 2be899cec) git-rm'd 30 dead 49F-incident scripts from the cot gold fork (prune-from-fork per the classification brief). Their S3 copies lingered in `opal-data-cot/code/gold/` from the 06-10 09:2xZ bulk seed (safe-deploy cp's, never deletes). Closing the S3-side of the CVO AC10 0-residual close-gate. Originally to fold into AE TO-2; TO-2 was already done (AE~B 06-10), so COO executed the prune directly on Andrew's confirm.

## Method (precise + guarded)
1. Diff: listed all S3 keys under `code/gold/` (102) vs the committed git gold tree `data/cot/scripts/gold/` (72 files). DEAD = S3 keys with no git-tree counterpart = 31.
2. Allowlist guard: regex-matched every dead key against known-dead patterns (`E_\d`, `gldrst/`, `run_[bc]\d`, `run_c01c`, `diag_sleeve_fix`, `_partial_chain`, `adhoc/auagap`, `auagap002_cascade`); would have ABORTED on any unexpected/live-looking name. 0 unexpected.
3. boto3 `delete_objects` (in-process, not shell loop). 0 errors.

## Deleted (31): all non-live diagnostics/runners/incident-artifacts
18 E_* diagnostics (E_02..E_17/E_19/E_25), 6 run_*_auagap002 runners (b00/b03/c00/c01c/c02/c03), 3 gldrst/ migration-rollback (preflight_snapshot/restore_old_keys/verify_migration), diag_sleeve_fix.py, 3 dead .sh (_partial_chain_b01, adhoc/auagap002_option_a_cascade, auagap002_cascade).

## Post-verify
71 keys remain under `code/gold/` (was 102) = EXACTLY the 71 live scripts (in both S3 + git). 0 dead-still-present. 71 LIVE intact (untouched). S3-side 0-residual CONFIRMED.

## Notified
AE 0.7.0 (was carrying it in TO-2/CHAIN-FIX — dropped), CVO 3.0.0 (AC10 owner — S3-side leg closed). Remaining AC10 legs: DS §8 inf-tree sweep (in progress) + P3 + cosmetic ssm.tf:272 (rides CHAIN-FIX apply).
