# TCKT_VNEXT TO-R18-RUN PART 1: one Meeting Request on DEV, RUN-OK (meeting only) -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-16
**Task Order:** TCKT_VNEXT.TO-R18-RUN (AMENDMENTS 4, 5 and 6), PART 1 (FWD-11)
**Status:** COMPLETE except the order's `<status>` flip (held, see Blockers)

---

## Objective

Run the Meeting Request journey once for real on portal DEV in one sitting: a synthetic internal filer files it in the browser, a second synthetic internal coordinator is the SOLE `meeting_request.primary` for one routing window and confirms one proposed time in the browser, the routing is restored, both identity rows are deleted after the later token expiry. Pair: `R18_RUN/R18_RUN_PAIR.md` AMENDMENT 2 (COO blob `000c3467f5`, CTO half `5e89bca0c2`, origin half `cf7c856072`); criterion `r18_run_check_meeting.py` (blob `d4a45af2d5`).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open 8 legs, close-leg x8, close | PASS | `tckt-vnext-r18-run-meeting-20261016` CLOSED 8 of 8 |
| terraform plan / safe-apply | window open (scratch copy), window close (committed tree) | PASS | each plan 0 add, 1 change, 0 destroy, ROUTING_MATRIX `meeting_request.primary` only; both applies rc=0 |
| r18_run_meeting.py (this seat) | one process, gate files between phases | PASS | ticket filed 201, confirm 200, rows deleted and ABSENT |
| r18_run_check_meeting.py (issuer) | criterion | PASS | `RUN-OK (meeting only)` |
| commit-gate.sh | on the script | PASS | py_compile, ds-precommit, ruff clean |
| proof-of-spec-check.py | with --governing-order | FAIL (1 violation) | `R18-tf-6` is in the order's `<owned_cells>` but no criterion references it |
| comp-* graph tools | not run | SKIPPED | no code, IAM or infra change beyond one Lambda environment value applied by the pair's method |

**What worked:** gate files between a background run process and my terraform steps kept the key and tokens in one process while I read each plan before every apply. **What failed:** a first scratch plan errored (`opal_name` reads `infra/logic/registry/exemptions.json`, outside the sparse cone); widening the cone fixed it. **Gap found:** the issuer's AMENDMENT 5 narrowed the criterion but left `R18-tf-6` in `<owned_cells>`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Hold at the start gate (earlier) | STOP msg 9764: Trade Request hidden in the DEV type list (row `TCKT_VNEXT-D2-S56`); issuer narrowed to PART 1 (AMENDMENT 5) and told me to reuse the server (AMENDMENT 6) |
| 1 | Measure 4 blobs, re-read start gate | `000c3467f5`, `5e89bca0c2`, `cf7c856072`, `d4a45af2d5` equal; REL-OK; routing jeanette alone; origin/DEV carries both candidates; 89-tree sweep, no live open ledger; port 5174 served by `C:/dev/smoke-template-5174` HEAD `1779d67606` (clean, carries `c05e3dda`, `12c164a0`, `dc057891b086`), not started or stopped |
| 2 | Ledger opened, S1 closed | 8 legs |
| 3 | Mint filer, open browser | page origin `http://localhost:5174`; firm list offered `cottonwood`; token exp 19:38:08Z |
| 4 | Plan in scratch copy, `GO_WINDOW`, mint coordinator (exp 19:39:28Z) | plan: only `jeanette@opalinvest.com -> tckt-r18-coord-20261016@opal.invalid` |
| 5 | Window opened | `safe-apply` rc=0 at 19:23:42Z; read back: coordinator alone |
| 6 | Filing | ticket `TCK-20261016-9d7654eb`, POST 201, ConsistentRead: `meeting_request`, `open`, `routing.primary` = coordinator; CREATE log token `WE_DL_UNCONFIGURED` only |
| 7 | Confirm | coordinator context (origin printed), POST 200; `meeting.status` confirmed, `meeting.time` the clicked first time, `meeting.by` the coordinator, ticket still `open` |
| 8 | Window closed FIRST | committed tree (blob `748e680fd7f8`), plan one change back, `safe-apply` rc=0 at 19:28:01Z; read back: jeanette alone |
| 9 | Removal | both rows deleted 19:39:33Z (after the later exp 19:39:28Z), ConsistentRead ABSENT |
| 10 | Check, result file, ledger | `RUN-OK (meeting only)`; `R18_RUN_RESULT.json`; ledger CLOSED |

## Verification

```
r18_run_check_meeting.py -> RUN-OK (meeting only) meeting confirmed by the synthetic coordinator inside a routing window now restored; both identity rows absent
live meeting_request.primary now -> ["jeanette@opalinvest.com"]
```
Aborted requests: 50, all non-allow-listed (23 POSTs to an external API Gateway host, GETs of dashboard and portal-content reads), none needed by the journey. No `/api/general/trades` path was requested. The signing key's current slot was read twice (one token per identity), in memory only.

---

## Decisions Made

- Held the run at the first STOP and changed no method; ran only what the issuer's amended order and the CTO-signed pair named.
- Did not flip the order to `complete` and did not edit its `<owned_cells>`: the instance fails the gate for a cell (`R18-tf-6`) that belongs to PART 2.

## Blockers

The order's `<status>` stays `pending`: `proof-of-spec-check.py` returns 1 violation (`R18-tf-6` named in `<owned_cells>`, referenced by no criterion). The issuer owns the order text; the fix is one line in `<owned_cells>` (or a deferred-cell form the gate admits). Everything else is done.

## Current State

The routing is restored (Jeanette alone), both identity rows are ABSENT, the ledger is closed, `localhost:5174` was never touched. The test meeting ticket `TCK-20261016-9d7654eb` is left open for the issuer's closing card. Records: `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r18_run/` (result, trace, script, plan and apply texts, instance). Kept until the issuer says: worktrees `C:/dev/tv2-r18run-scratch` (main.tf reverted to the committed blob) and `C:/dev/tv2-rel-r1819`.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Amend the order's `<owned_cells>` (drop `R18-tf-6` for PART 1); I then re-validate the instance and flip `complete`.
2. `[2.0.0_SA_COO~V2]` Close the test meeting ticket by its own card; PART 2 (FWD-10) needs port 5174 free or the CTO's scratch build elsewhere.
3. `[0.0.0_AB_MSTR~DELL2]` The signing-key read (two token mints) is reported after the fact here.
4. `[0.0.0_AB_MSTR]` Carry this seat's local commits from box/dell2.
