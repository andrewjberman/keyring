# 0.7.0_AE_CloudOps~RA1 -- 2026-10-14 -- AMGT_RESAPP AMGT-ar-7: the AI fill is held off the served API by one environment variable; HOLD SERVED YES (9 of 9)

**Date:** 2026-10-14 (GO 05:06Z, msg 5430; apply 05:09:09Z-05:10:06Z; function LastModified 05:10:01Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-ar-7.the-ai-fill-is-held-off-the-served-api-by-one-environment-variable
**Status:** APPLIED AND VERIFIED; AC1, AC2, AC3 PASS; ledger CLOSED 7 of 7

## Objective

CTO ruling 2: the AI-fill blocks come off the PROD page until a re-read passes. The handler reads `AMGT_AIFILL_ROOT` at call time; set to a directory that does not exist it answers
`ai_fill` as `ABSENT` with `blocks` {}. One environment entry on `opal-amgt-scoped-api`, `AMGT_AIFILL_ROOT = "/var/empty/aifill-hold"`; the code is untouched.

## The act
**archetype:** DEPLOY

1. Printed the live configuration (CodeSha256 `0pWc69Vd..`, memory 1769, timeout 29, two HARVEST tables, RevisionId `9ca4704b..`) and the source-map entry; opened the 7-leg ledger entry.
2. Captured the three bodies (`ASML_NA`, `NESN_SW`, `OMAB_MM`); the base verify read NO (6 of 9).
3. Added the one entry (+7 lines with its comment). Targeted plan of `module.scoped_amgt_api`, graded from its JSON: 6 resources, 1 update, `environment` only, code hash, role, layer, memory and timeout unchanged.
4. Targeted `safe-apply` of the saved plan: 0 added, 1 changed, 0 destroyed. First request after the apply: 200, handler 2,989.87 ms, Init 682.60 ms.
5. AC1 `AIFILL HOLD SERVED: YES (9 of 9)`; AC2 R97, R95, R94 YES; AC3 configuration as expected.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L7, close | PASS | opened before the edit |
| check_hold_served.py | capture, verify (base and after) | NO 6/9 -> YES 9/9 | |
| terraform plan -target, show -json, safe-apply.sh | module.scoped_amgt_api | PASS | 1 in-place change, environment only |
| r102_first_cold_request.py | first request after the apply | RECORDED | information only |
| r97 / r95 / r94 checks | AC2 | PASS | exit=0 |

**What worked:** grading the plan per attribute from its JSON; the check's base-then-after reading.
**What failed:** nothing.
**Gap found:** none. record-terraform-deploy.sh was not run: no Lambda code moved and the order does not ask for it; the source-map entry still equals the live CodeSha256.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Drove one overlay request before the AC1 verify | the order asks for the first request after the apply as information |
| Told the issuer after AC1, before AC2 and AC3 | the ruling is urgent; I kept the function held until the release |

## Files Modified

- `infra/aws/terraform/harvest/scoped-amgt-api.tf` (+7)
- `org/critical_paths/change_management/20261014T0507Z_amgt-resapp-r105-ar7-aifill-hold-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the first-request file and the proof instance
- the order's `<status>` (complete)
- local only, uncommitted: `.scratch_hold/thesis_pre.json`

## Next Steps

1. `[2.0.0_SA_COO~R2]` Order the restore (delete the one entry, one targeted `safe-apply`) when the CTO releases it on a MET re-read.
2. `[box-sync / MSTR]` Integrate the local commits.
