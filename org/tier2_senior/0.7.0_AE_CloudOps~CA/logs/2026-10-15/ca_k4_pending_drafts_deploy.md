# COMM_ASSIST TO-CA-k-4 -- list of open mail drafts deployed to module.ldo_001 (Branch A, code only)

**archetype:** DEPLOY

**Serial:** 0.7.0_AE_CloudOps~CA (laptop) | **Issuer:** 2.0.0_SA_COO~CA | **Window:** 2026-10-15 ~05:25Z to ~06:25Z | **Risk:** WORLD

## Summary

Deployed the CA-k-1 code (`mail_requests.py`, `tenant.py`: `state["pending_list"]`, reply by tag, list of every open draft) to `teams-global-chat-assist-handler-lambda` and `-ingress-lambda` through one targeted `safe-apply` of `module.ldo_001`, built from a detached worktree at the pin `93a3f55d25`. Branch A held at every gate. The order is `complete`; the proof instance is VALID at the final head.

## Deployment Sequence and Verification

| step | result |
|---|---|
| 0 disk | `C:` 18 GB free (floor 5 GB); time 05:30Z, after the 05:00Z reset |
| 1 worktree | detached at `93a3f55d25`, `status --porcelain` 0 |
| 2 ledger | `comm-assist-r19-pending-deploy` opened, 4 legs, entry + sentinel committed at `bbd328c0a1` before the act |
| 3 BEFORE | both functions `BBiNwhfKGcPciG5+zFa2KCIsJ/kF18g+x4ozNN2EnIA=`, 297733 B, mode `enforce`, 15 key names; live zip saved (sha256 base64 equal to CodeSha256); dead-letter queue 0/0/0; `check_j5_obs` CLEAN |
| 4 build | `build.sh` 39 files, 320236 B, base64 sha256 `nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju62S4xa9k=`; import test OK; AC1 `K4-EQUIV ok=True files=2 foreign=4 probes=17 same=17` |
| 5 plan | new `TF_DATA_DIR`, `init` no prompt; saved locked targeted plan `0 to add, 2 to change, 0 to destroy`; JSON read: changed keys exactly `last_modified`, `source_code_hash`, environment equal, after-hash equal to the build |
| 5 apply | `safe-apply.sh`: `LDO001-MODE verdict=OK default=enforce live=enforce`; `Apply complete! 0 added, 2 changed, 0 destroyed` at 05:56Z |
| 6 AFTER | both `nQlJW0j...`, 320236 B, mode `enforce`, 15 keys unchanged; AC2 `RESULT: PASS`; re-plan rc=0 "No changes"; 06:07Z log read: 11 `ingress_poll`, 2 mail polls, 0 errors, 0 `AccessDenied`; dead-letter queue 0/0/0 UNCHANGED |
| 8 close | ledger CLOSED at `b54cf099a8` (sentinel deleted); AC3 PASS; pinned worktree removed |

Evidence: `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/r19/`. Commits: `bbd328c0a1`, `b54cf099a8`, `0421c82aeb`, `4bda3f20ad`, `49d9d28c62`, `cc54603dd4`. Push state: LOCAL @cc54603dd4 (ls-remote read: origin box/laptop is cb843928c1); box-sync pushes.

## Files Modified

See commit messages. New: the r19 evidence folder, the proof instance, the ledger entry. Changed: the order's `<status>` to `complete`.

## Blockers

None.

## Current State

Both Lambdas serve `nQlJW0j/a2nE1om0ZbXm9CTMxAVDXwUQNju62S4xa9k=` (pin `93a3f55d25`); `INGRESS_MARK_MODE=enforce`. BLIND, as the COO half states: no real pair of considered mails has run through the list, only the served-code probe. Rollback copy of the prior package is device-local at `C:/tmp/ca19_rollback_BBiNwhfK.zip` (rollback is a targeted apply from a detached worktree at `0774100edc`, never `afa8752f44`; a redeploy after a rollback must reconcile `pending_list` against `pending`). Left on the device: `C:/tmp/ca-k4-tfdata` (a recursive delete was declined by the permission layer; provider binaries only, no plan files).

## Next Steps

1. [2.0.0_SA_COO~CA] Read the proof instance, grade, and carry CA-k-5 (the dell2 pick-up and the FWD-13 exercise).
2. [2.0.0_SA_COO~CA] The first End of Day window 20:00Z-21:45Z is the first live traffic over the new writer; an exception or dead letter from the list writer belongs to this deploy.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| comp-which | not run | PASS-NA: the comp-rail denied two compound calls (recursive grep over named files); redone with native Grep/Read |
| comp-iam | not run | NA: order declares no policy move; plan JSON confirmed only the two functions change, AC2 simulated both roles |
| comp-blast | not run | NA: blast read by issuer, CTO and CVO |
| check_l4_equiv / check_l4_live / check_l4_ledger / check_j5_obs | as the order | PASS x4 |

What worked: the issuer's three checks and the ledger tool. What failed: the checker wanted `N/A-SPEC-NAMES-NONE`, not `N/A-WITH-REASON`, for the mutant control (fixed, `49d9d28c62`). Gap found: none.
