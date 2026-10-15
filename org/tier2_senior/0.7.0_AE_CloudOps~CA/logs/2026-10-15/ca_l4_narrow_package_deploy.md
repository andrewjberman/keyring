# COMM_ASSIST TO-CA-l-4 -- narrower package (39 to 34 files) deployed to module.ldo_001 (Branch A, code only)

**archetype:** DEPLOY

**Serial:** 0.7.0_AE_CloudOps~CA (laptop) | **Issuer:** 2.0.0_SA_COO~CA | **Window:** 2026-10-15 ~09:04Z to ~09:40Z | **Risk:** WORLD

## Summary

Deployed the CA-l-2 build (`registry_files.txt` manifest: 12 registry files instead of 17) to `teams-global-chat-assist-handler-lambda` and `-ingress-lambda` through one targeted `safe-apply` of `module.ldo_001`, built from a detached worktree at the pin `863dc0f739`. Branch A held at every gate, including the CTO's C1 static scan. The order is `complete`; the proof instance is VALID at the final head.

## Deployment Sequence and Verification

| step | result |
|---|---|
| 0 disk | `C:` 13 GB free (floor 5 GB); time 09:04Z |
| 1 worktree | detached at `863dc0f739`, `status --porcelain` 0 |
| 2 ledger | `comm-assist-r20-narrow-deploy` opened, 4 legs, entry + sentinel committed at `381af0bcba` before the act |
| 3 BEFORE | both functions `nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju62S4xa9k=`, 320236 B, mode `enforce`, 15 key names; live zip saved (39 files, sha256 base64 equal to CodeSha256); dead-letter queue 0/0/0; `check_j5_obs` CLEAN |
| 4 build | `build.sh` `(34 files)`, 235445 B, base64 sha256 `gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=`; import test OK; AC1 `M4-EQUIV ok=True dropped=5 foreign=2 probes=17 same=17` |
| 4b C1 scan | `M4-SCAN ok=True named=14 manifest=12 outside=2 excluded=2`; `name_rulings.json` and `root_map.json` excluded behind the `opal_naming_rootcheck` guard (lines 3505, 3810) |
| 5 plan | new `TF_DATA_DIR`, `init` no prompt; saved locked targeted plan `0 to add, 2 to change, 0 to destroy`; JSON read: changed keys exactly `last_modified`, `source_code_hash`, environment equal, after-hash equal to the build |
| 5 apply | `safe-apply.sh`: `LDO001-MODE verdict=OK default=enforce live=enforce`; `Apply complete! 0 added, 2 changed, 0 destroyed`, 09:17:00Z to 09:18:59Z |
| 6 AFTER | both `gSq68yr2...`, 235445 B, mode `enforce`, 15 keys unchanged; AC2 `RESULT: PASS`; re-plan rc=0 "No changes"; 09:29Z log read: 11 `ingress_poll`, 2 mail polls, 0 errors, 0 `AccessDenied`; dead-letter queue 0/0/0 UNCHANGED |
| 8 close | ledger CLOSED at `4c9a6d1932` (sentinel deleted); AC3 PASS; pinned worktree removed |

Evidence: `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/r20/`. Commits: `381af0bcba`, `4c9a6d1932`, `831b9ece74`, `5391bd3374`, `80ff129057`. Push state: LOCAL @80ff129057 (ls-remote read: origin box/laptop is 09459142a9); box-sync pushes.

## Files Modified

See commit messages. New: the r20 evidence folder, the proof instance, the ledger entry. Changed: the order's `<status>` to `complete`.

## Blockers

None.

## Current State

Both Lambdas serve `gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=` (34 files, pin `863dc0f739`); `INGRESS_MARK_MODE=enforce`. The CTO's C2 is the issuer's: read the 20:00Z-21:45Z End of Day window for a missing-file error and the dead-letter queue against 0/0/0; roll back the same hour otherwise. Apply time for placement: 09:17:00Z to 09:18:59Z. Rollback copy of the prior package (39 files) is device-local at `C:/tmp/ca20_rollback_nQlJW0j.zip`; rollback is a targeted apply from a detached worktree at `93a3f55d25`, never `afa8752f44`. Left on the device: `C:/tmp/ca-l4-tfdata` and `C:/tmp/ca-k4-tfdata` (provider binaries only, no plan files).

## Next Steps

1. [2.0.0_SA_COO~CA] Read the proof instance, grade, carry the round.
2. [2.0.0_SA_COO~CA] CTO C2: read the first End of Day window (20:00Z-21:45Z) logs and the dead-letter queue.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| comp-which | not run | NA: native Grep/Read used for named files |
| comp-iam | not run | NA: order declares no policy move; plan JSON confirmed only the two functions change, AC2 simulated both roles |
| comp-blast | not run | NA: blast read by issuer, CTO and CVO |
| check_m4_equiv / check_m4_scan / check_m4_live / check_m4_ledger / check_j5_obs | as the order | PASS x5 |

What worked: the issuer's checks, the ledger tool, and the lessons of the previous order (`N/A-SPEC-NAMES-NONE` for the mutant control, no recursive delete). What failed: nothing. Gap found: none.
