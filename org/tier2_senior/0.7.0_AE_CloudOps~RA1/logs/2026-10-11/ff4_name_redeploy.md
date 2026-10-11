# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-ff-4: the registered-name rule redeployed, compare equals the table

**Date:** 2026-10-11 (GO 14:25Z; baseline 14:51-14:56Z; apply 14:57:16Z; function LastModified 14:57:44Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-ff-4.redeploy-the-scoped-api-carrying-the-display-name-rule
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 10 of 10)

## Objective

One code redeploy of `opal-amgt-scoped-api` at pin 15b7af1601: AMGT-ff-1's registered-name rule (Sanofi and CSL named as
themselves on every route that serves a name), carrying AMGT_CORPUS leg p's dossier `/12` and other projects' additive
members. The pair is a route-by-route measurement; this act is read against it path by path.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin (ff-1 and AMGT_CORPUS ancestors); ran the GO's two instruments at the pin:
   `r94_admission_table.py` (9 of 9 blobs equal the half's columns) and `r94_naming_replay.py` (YES, 81 builder calls, 0
   differ); confirmed AMGT_CORPUS's PRE-ACT SNAPSHOTS DONE (msg 3909) is on record before the apply.
2. Captured the rollback package (hash-checked), the wheel and source-map records and the sweep; built at the pin (offline):
   CHANGED 7, ADDED 1, every one inside the admitted nine.
3. Ran the three table scripts in local mode: they reproduced the half's table on the GO day. Recorded a full BASELINE of
   519 requests immediately before the apply.
4. Uploaded, graded the plan from JSON (1 of 53), applied at 14:57:16Z, sent the CodeSha256 and apply time to the issuer at once
   (the GO asks it for AMGT_CORPUS), then replayed the baseline's requests and compared path by path.
5. AC1-AC3 PASS. The compare: 79 name paths and 50 corpus paths, exactly the table; 28 noise paths (generated_at clocks),
   listed; 0 paths outside; status moved 0.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L10, close | PASS | opened before the build |
| r94_admission_table.py / r94_naming_replay.py | at the pin | PASS | 9 of 9; YES |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline |
| r94_*_table.py x3 | local-mode prediction | PASS | equal to the half |
| ff4_capture.py | capture, replay, compare | PASS | the instrument the scripts could not be after an apply |
| r94_name_census.py / r89 checks / r92 census | AC1-AC3 | PASS | exit 0 |

**What worked:** recording a before-apply baseline of every request the half's table names, because the scripts' own
`--after deployed` mode reads the live function twice and would have printed "0 changes" after an apply, a pass that proves
nothing; sending the CodeSha256 the moment it existed so AMGT_CORPUS was not waiting on the compare.
**What failed:** nothing in the act.
**Gap found:** the table scripts' `--after deployed` arm cannot compare across an apply; a future half should name a
baseline file the script reads. I did not edit the issuer's scripts.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Wrote my own capture and replay instead of using `--after deployed` | the scripts' deployed arm reads live twice; a before-and-after compare needs a before |
| Listed all 28 noise paths | the scripts count noise apart; a count is not a list, and a reader should see they are clocks |
| Reported the CodeSha256 before the compare finished | the GO asks it for AMGT_CORPUS, and the compare could only add a STOP, which would go to the same seat first |

## Files Modified

- `org/critical_paths/change_management/20261011T1430Z_amgt-resapp-r94-ff4-name-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the compare report and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit 14f56caa80)
- the order's `<status>` (complete)

## Next Steps

1. `[2.0.0_SA_COO~C1]` Post-act read of the four names then all 95, and portal PROD against the 13:26Z snapshot.
2. `[1.0.0_SA_CTO~DELL1]` D1-S26 (CSL AU's classification) is round 95's cell after the idempotency cell.
3. `[box-sync / MSTR]` Push the local commits.
