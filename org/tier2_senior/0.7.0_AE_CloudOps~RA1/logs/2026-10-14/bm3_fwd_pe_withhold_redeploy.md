# 0.7.0_AE_CloudOps~RA1 -- 2026-10-14 -- AMGT_RESAPP AMGT-bm-3: the scoped API carries the forward P/E withhold; 218 served, 60 withheld; AC1 NO (pool refresh), KEEP named

**Date:** 2026-10-14 (GO 12:49Z, msg 5529; capture 12:58-12:59Z; apply 13:00:37Z-13:01:39Z; function LastModified 13:01:34Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-bm-3.redeploy-the-scoped-api-carrying-the-forward-pe-withhold-from-a-merged-pin-and-drive-its-first-cold-request
**Status:** APPLIED AND KEPT; AC2 and AC3 PASS; AC1 reads NO (5 of 7) on a concurrent pool refresh, KEEP named by the CTO (msg 5561, ADDENDUM 1 @358b460431); ledger CLOSED 11 of 11. The order's `<status>` is left `pending` for the issuer: AC1 does not pass on its literal expectation.

## Objective

One code leg of `opal-amgt-scoped-api` from the MERGED pin `3818736e6b`: `scoped_amgt.py` `1f5de89912e5` -> `a75ab14fd16d`, so a forward P/E whose price and EPS currencies differ is absent from `model.forecast_figures` and present in `model.forecast_withheld` with a reason naming both codes (60 rows on 20 names), and every name gains the key `model.forecast_withheld`. Eight `lib/research/aifill` members differ in the tree and are not packaged. The `AMGT_AIFILL_ROOT` hold stays.

## The act
**archetype:** DEPLOY

1. Printed the live configuration (CodeSha256 `0pWc69Vd..`, memory 1769, timeout 29, hold in the environment). `r94_admission_table.py 3818736e6b --pin 0447f2df38` printed the NINE members at the half's blobs. Opened the 11-leg ledger entry. Detached worktree `C:/tmp/bm3-build` at the pin.
2. Rollback prepared before any live act: blob table at `0447f2df38`; the hold entry counted 0 at `0447f2df38`, 1 at the pin and at HEAD (condition C1: a rollback applies the hold-carrying Terraform); the live package downloaded and hash-checked as the build's reference and as a rollback copy; wheels 6 of 6; 30 worktrees swept.
3. Built offline: 408 files, CHANGED 1 (`scoped_amgt.py`, blob recomputed from the zip `a75ab14fd16d`), ADDED 0, no aifill member in the package. Naming replay on the built zip, with a wrapper that asserts the modules load from the zip root: 35/68/16, 0 differ.
4. Captured 95 names; uploaded with read-back; graded the untargeted plan from its JSON (1 of 53, code attributes only, environment/role/layers/memory/timeout EQUAL); applied the saved plan through `safe-apply`. **First act after the apply:** `r102_first_cold_request.py` for `ASML_NA_Equity`: handler 2,930.47 ms, Init 678.15 ms, request `712b4bcb-5e10-4f33-b415-7ca49a068b51`.
5. AC1 read `NO (5 of 7)`: F1, F3, F4, F6, F7 pass (218 served, 60 withheld, population 60); F2 and F5 fail. Cause read, not assumed: the harvest runner (`~ZW`, `--refresh-once`) refreshed the live pool after my capture (ADBE US FY1 vintage 2026-10-12 -> 2026-10-14T13:02:29Z, PX_LAST 242.27 -> 236.28, P/E ratio equal to the price ratio; 73 of 95 names differ; 154 of 176 kept rows move by the PX_LAST ratio). Same-pool control, deployed function against the pin's own handler, 95 names: one distinct path, `.ai_fill.reason` (the known separator artefact), nothing else.
6. Told the issuer and the CTO (msgs 5559/5560) with the rollback clock 14:01Z; the CTO named KEEP (msg 5561). No rollback ran. AC2 and AC3 PASS. Record step `8e53fc2052`; plan after the apply: No changes.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L11, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin; on the built zip via a sys.path wrapper | PASS | 9 members; 35/68/16, 0 differ |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, CHANGED 1 of 408 |
| r106_fwd_pe_deployed.py | capture (pre), verify | NO 5 of 7 | F2/F5 on a concurrent pool refresh |
| terraform plan / show -json / safe-apply.sh | untargeted saved plan | PASS | 53 resources, 1 update, code only; 0-diff after |
| r102_first_cold_request.py | first request after apply | RECORDED | cold, Init 678.15 ms |
| r94_name_census.py, r104_split_table.py | AC2, AC3 | PASS | exit=0 |
| proof-of-spec-check.py | instance with --governing-order | VALID | AC1 recorded FAIL with its reason and the KEEP |

**What worked:** the base-then-after reading pinned the confound on the pool and not the code; a same-pool control (deployed against the pin's handler) separates the two in one run; the sys.path wrapper that asserts the replay loads the zip root.
**What failed:** (1) a first naming replay without the wrapper loaded the repo's `lib`, not the zip's, and printed the same counts; I did not cite it and re-ran it with the control. (2) The instrument's `redirect_stdout` across threads swallowed my first two same-pool runs' prints; restoring `sys.stdout` fixed the third.
**Gap found:** the capture-to-verify window is open to a concurrent writer, and r106's F2/F5 cannot tell a pool refresh from a code change. The CTO's note: later pairs name the harvest pool's WRITERS for that window.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not roll back at AC1 NO | The cause was read as data; the control showed deployed = pin; Branch 2 reserves KEEP to the CTO, so I asked and held the rollback clock (14:01Z) |
| Left the order `<status>` pending | AC1 does not pass on its literal expectation; the flip is the issuer's |
| Used an untargeted plan | Same as ar-3; gave the 53-resource denominator |
| Did not push | commits stay LOCAL |

## Files Modified

- `org/critical_paths/change_management/20261014T1252Z_amgt-resapp-r106-bm3-fwd-pe-withhold-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` BM3_FIRST_COLD_REQUEST.txt, BM3_AC1_NO_EVIDENCE.md, the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit `8e53fc2052`)
- local only, uncommitted: `.scratch_bm3/` (the 95-name capture and plan files)

## Next Steps

1. `[2.0.0_SA_COO~R1]` Read the report, flip the order's `<status>` on the CTO's KEEP, cut bm-5; remove `C:/tmp/bm3-build`, `C:/tmp/bm3-pin` and `C:/tmp/bm3-zip-root` (a recursive deletion is the user's).
2. `[box-sync / MSTR]` Integrate the local commits.
