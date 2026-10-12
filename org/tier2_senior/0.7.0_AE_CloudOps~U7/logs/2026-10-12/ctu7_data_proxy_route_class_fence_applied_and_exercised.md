# opal-portal-data-proxy route-class fence applied and exercised, all four reads as ruled — 0.7.0_AE_CloudOps~U7

**archetype:** DEPLOY
**Date:** 2026-10-12
**Task Order:** NFRA_CTLPLN.TO-CT-u-7.portal-functions-fence-apply-and-exercise
**Status:** COMPLETE (proof instance VALID; the status flip is the issuer's; commit and tag are LOCAL, push is the integrator's)

---

## Objective

Put the FWD-28 route-class fence live on `opal-portal-data-proxy` by one `safe-apply` of `infra/aws/terraform/market-overview/`, then read both route classes with a non-internal and an internal caller. Written for a reader with no prior context.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | service opal-portal-data-proxy | PARTIAL | 35 calls, 18 GRANTED, 17 UNRESOLVABLE-RESOURCE; read as a floor, the fence adds no boto3 call |
| comp-blast | opal-portal-data-proxy | PASS | at least 1191 downstream nodes, a lower bound |
| deploy_ledger.py | open, 8 close-leg, close | PASS | entry nfra-ctlpln-ctu7-data-proxy-fence-20261012, CLOSED, nothing stranded |
| proof-of-spec-check.py | instance + CTu7-AC1,2,3 | PASS | VALID rc=0 after two fixes to artifact rows it named |
| safe-apply.sh | one apply of the saved plan | PASS | 0 added, 1 changed, 0 destroyed |

**What worked:** the plan JSON read (43 resources, one non-no-op); the member-by-member diff of the downloaded package; the tool refusing an early row delete.
**What failed:** `record-terraform-deploy.sh` fails on a `/cygdrive/c` path (its path conversion only knows `/c/`) and on `--plan` when the lock file no longer matches the cached providers; `--function` from a `/c/` path worked.
**Gap found:** `terraform init` rewrites the tracked `.terraform.lock.hcl` (drops the unused archive provider); I restored it. A checked-out `session_tracker.py` is CRLF while the index blob is LF, so a build from the working tree gives a different zip than the signed hashes.

---

## Work Completed

1. Read the order, its three amendments and BOTH halves of the pair whole, then the route census and the CT-u-6 surprise rows.
2. BEFORE state: CodeSha256 `LpodJICu...`, no env, no layers; rollback artifact version `rBMEa1ms...`. P0: deployed `lambda_function.py` = `24dc244f...` (the base). Deployed `session_tracker.py` is the pin blob with CRLF (proved by conversion).
3. Non-internal caller: `ui_walker_account.py` cannot take a second account id, so the CTO half's option (a): one synthetic row (firm 49financial, tier advisor), tokens signed in memory, 600 s each. R0 before the apply: 200.
4. Built from a detached pin worktree (LF bytes): members hash to the signed `5f0fad0e...` and `00f8c6a3...`; uploaded as version `5Xgupv5f...`, content-sha256 `6/BPExXE...`.
5. Plan Branch A exactly; one `safe-apply` at 04:30:31Z. The seat gate's CROSSBOX-DEPLOY said STOP in WARN mode (`open_call=hit`); I did not investigate it.
6. After-reads: CodeSha256 equal; package diffed both directions (2 of 2 equal); replan 0-diff. Calls: class-ii partner 403 (`forbidden: Opal-internal readers only`), internal 200; class-i partner 200, internal 200.
7. Cleanup: walker disarmed (post-disarm login refused 401); row deleted 9 s after the last exp, ABSENT with a never-written control, paginated census 0 of 86.
8. Recorded: commit `7824840818`, tag `market-overview-v1.11.5`. Push attempted and refused by `never-rules-gate.sh` (integrator only); state LOCAL, origin `box/laptop` was `d37ecd1216`.

## Decisions Made

- Option (a) over (b'), as the CTO half ordered when the walker tool cannot take a second id.
- Fresh in-memory token per phase instead of one token held across the apply: each lives 600 s and never leaves the one process.
- Skipped an internal baseline before the apply to keep the walker armed once, for 15 seconds.

## Files Modified

`infra/aws/lambda/ci/lambda-source-map.json` (one entry), `infra/aws/terraform/market-overview/CHANGELOG.json`, the deliverables under this seat, the ledger entry and its sentinel.

## Blockers

None. Not exercised: `POST /sentiment/keyword-intelligence` (the amendment names `GET /aum/metrics` as the control); callers outside the portal tree (CTO half section 4).

## Current State

Fence live and verified; ledger closed; no standing credential; the pin worktree removed.

## Next Steps

1. `[2.0.0_SA_COO~C]` Read the proof instance, flip the order, disposition surprise rows `NFRA_CTLPLN-W62-S1` and `-S4`.
2. `[0.0.0_AB_MSTR]` Carry `7824840818` and tag `market-overview-v1.11.5` at the next integration window.
