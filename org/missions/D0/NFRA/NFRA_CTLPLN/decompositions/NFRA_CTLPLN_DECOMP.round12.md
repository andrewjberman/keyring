# NFRA_CTLPLN decomposition -- round 12: the Dell users get the admin group, the fence goes back to tier-only, the seat-boundary and cross-box gate fixes, the SSH tools, the box list from the register, the naming gate's test folders, the S9112 purge, and the dell1 summary sentence (issuer 2.0.0_SA_COO~C; cut 2026-10-13)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round11.md` section 3 (1.0.0_SA_CTO msg 108646) and the later inputs: the Dell-identity ruling @1161dc05fc as superseded by Andrew's rec (b) (record `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md` @ff6d6d5fd7; CTO ruling @53acd6fe5f), PRD v0.29/v0.30, Andrew's round-12 answers @a7d5d7955c, the S9117 addenda (msgs 108728, 108730), D2-S32 (@374118e5cd), the SSH defect (msg 108698), dell1 row D1-W60-S3 (msg 108754, taken), the CVO re-grade of all 28 outcomes (`org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_FWD_REGRADE_20261013.md`).

## Cells

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-ab-1` | `infra/aws/terraform/nfra-ctlpln-identity/`: both Dell users become members of `AdministratorAccessOpalCapital`; every Deny reaching them is removed except `DenyCloudTrailWrites`, `DenyAuditTrailBucketWrites`, `DenyS3DeletesOnProductionData`, `DenyTableAndDatabaseDeletes`; a static check proves it. Nothing applied by this cell. | FWD-10, FWD-5 | WORLD (path floor; no apply) | DELLADMIN / 1 | `0.9.0_WK_NFRA_CTLPLN~77` |
| `CT-aa-5` | the data proxy fence goes back to `tier == 'internal'` only; the Dev clause removed; tests inverted into a tier-only file. Nothing deployed. | FWD-28 | WORLD (path floor; no deploy) | DEVFENCE / 3 | `0.9.0_WK_NFRA_CTLPLN~76` |
| `CT-ab-3` | dell1: the one missing egress sentence in the plain click-route summary; the CVO regrades. | FWD-17, FWD-1 | LOCAL | THREAD / 12 | `0.7.0_AE_CloudOps~CT1` |
| `CT-ab-4` | `kill-agent.ps1` targets a process only when its OWN launch serial equals the target; neither kill tool stops a descendant `claude.exe` of another serial; `spawn-agent.ps1`'s non-wt branch spawns detached; a selftest with a two-serial fake tree. | FWD-21, FWD-25 | LOCAL | SEATKILL / 1 | `0.9.0_WK_NFRA_CTLPLN~78` |
| `CT-ab-5` | `crossbox-deploy-check.py`: the OPEN-DEPLOY arm counts a worktree sentinel only when that worktree's HEAD is not an ancestor of the shared HEAD (and the two race cases 83/84 pass); the OPEN-CALL arm matches a root path or a named root, never a bare token; both print denominators. | FWD-5, FWD-10 | LOCAL | XBLIMB / 1 | `0.9.0_WK_NFRA_CTLPLN~79` |
| `CT-ab-7` | `ssh-tailnet-verify.py` grades keyboard-interactive by whether the server sends a prompt, and takes the key file explicitly; `ssh-tailnet-enable.ps1` re-plans after it installs OpenSSH Server, so the default rule the install creates is disabled. | FWD-27 | LOCAL | SSHTOOLS / 1 | `0.9.0_WK_NFRA_CTLPLN~80` |
| `CT-ab-8` | the hand-typed box lists in `.tools/to-pipeline-gate.py:93` and `.tools/box-status-report-check.py:33` come from `lib/devices.py`; the census of hand-listed boxes drops by those two. | FWD-2 | LOCAL | REGISTER / 1 | `0.9.0_WK_NFRA_CTLPLN~81` |
| `CT-ab-9` | `.tools/naming-gate.py` exempts `*/tests/*` AND `*/test/*` by an explicit list of both spellings (never a substring), at both sites (:996, :2169) (row D1-W60-S3). | FWD-2 (C-NAMING) | LOCAL | NAMEGATE / 1 | `0.9.0_WK_NFRA_CTLPLN~82` |
| `CT-ab-10` | S9112: purge the data proxy log group's pre-fix events; print each leaked token set's latest expiry; read the signing secret's home and whether a rotation path exists (CTO ruling @53acd6fe5f section 2); NO account disabled. | FWD-28 (hygiene) | WORLD | LOGFIX / 2 | `0.7.0_AE_CloudOps~U7` (re-seated) |

**Staged next, cut as a recut when their build merges (each under its own signed pair):** `CT-ab-2` the apply of `CT-ab-1` (pair 6; read-backs by the Dell seats: an IRPT-key decrypt on dell2, a policy simulation on dell1, a formerly protected function described, a production S3 delete still refused); `CT-aa-6` the apply of `CT-aa-5` (pair 5); a rotation of the signing secret only if `CT-ab-10` finds a path.

**Carried with a reason (not cut this round):** the fence checker re-baseline (ADVI_FIRMBKTS-D1-S43: reason 2 clears with `CT-ab-2`; reasons 1, 3, 4 are cut after it, when the checker can be run under the new identity); the package route on a lane that needs a package (FWD-15/18/19: the needing lane is named first, `pandas_market_calendars` the candidate); the two deliberate dell1 outages (FWD-9/FWD-11: after `CT-ab-2`, so the manager's restart runs with the new identity); FWD-27's per-box cells (Andrew: "We dont need to focus on the local account and macbook ops right now"); FWD-4/FWD-7/FWD-8 reads and FWD-23/25 seat acts (next issuance).

## Rule 24

**Domain:** the round-11 list (6 items), the later inputs above, and the 17 class-A outcomes of the re-grade. Every item is a cell, a staged recut, or carried with a reason. **Same grain; one intent per cell; disjoint write surfaces** (each `<paths>` names no file another cell writes). **State coherence:** `CT-ab-1` moves no live permission (its apply is `CT-ab-2`); `CT-aa-5` moves no live code; `CT-ab-10` deletes log events only.

## Dependency chains and fan-out

Nine independent chains (each cell is its own; the staged applies follow their builds). `fanout: 9 of 9 chains, cap 8, reason: seven laptop worker cells (the cap's 8 holds them), plus one dell1 seat cell and one laptop CloudOps seat cell that take no worker slot`
