# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-nn-7: redeployed at the re-pinned build, ledger closed

**Date:** 2026-10-11 (04:46Z session start; apply 04:56:11Z; ledger closed 05:01:50Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-nn-7.redeploy-peer-identity-subject-cap-and-dossier
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED; record commit LOCAL)

## Objective

The prior session of this lane STOPPED before any upload because the GO's pin 8f2f3339c2 carried nn-5's crosswalk.py write
guard. The issuer re-pinned to a943b1b412 (msg 3493) and the CTO ruled option A (ADDENDUM 1, msg 3495). This session
resumed with the live function still on KlosR/ap8O3.., verified the re-pinned build, and ran the act.

## The act
**archetype:** DEPLOY

1. Read the live function first (KlosR.., LastModified 2026-10-09T22:55:03Z), the open ledger (L1-L5 closed at the
   superseded pin) and both pair halves with ADDENDUM 1.
2. Re-read the new pin myself: 7 of 7 ancestors, nn-5 merge 04ecb2d528 and commit 0e14335de2 NOT ancestors, three blobs
   equal the CTO table, crosswalk.py 48d7e7d9983b equal to live, METHOD /11.
3. Did not rebuild: the prior session's nn7a_built.zip existed from a clean detached worktree at the pin. Re-derived the
   whole content diff from the two zips (ADDED 8, CHANGED 2, REMOVED 0) and byte-compared each of the 10 members with the
   pin's blob (10 of 10 equal) before closing L6.
4. Uploaded through upload_verified.sh (read-back match), graded the untargeted saved plan from its JSON (1 of 53 moving),
   applied through safe-apply.
5. Post-act: CodeSha256 l8egBo.. equals the built file; re-plan rc=0; AC2 and AC3 YES; three-name baseline compare; AC1 in
   the build worktree; record step committed LOCAL at fb1d570c2d.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | close-leg L6-L11, close | PASS | refuses a close with an unproven leg |
| terraform show -json | over the saved plan | PASS | 1 moving of 53, update only |
| safe-apply.sh | -chdir=harvest apply <plan> | PASS | tagauthz and tombstone gates clean |
| record-terraform-deploy.sh | harvest --plan --deploy-ledger --code-sha256 | PASS | fb1d570c2d |
| proof-of-spec-check.py | on the nn-7 instance | PASS | VALID rc=0, 12 of 12 controls discriminate |
| comp-rail hook | a recursive find over org/ for a ledger file | DENIED | used native Glob; the file was named by the order |

**What worked:** re-deriving the content diff from the zips instead of the build log; grading the plan from JSON; a
hasher chosen by reproducing the baseline's own top-key hashes before comparing any moved field.
**What failed:** one recursive find denied by the rail (F1), correctly.
**Gap found:** the baseline file carries no script; the per-key hash function had to be recovered by reproduction. A kept
capture script beside nn7_base.json would remove that step.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not rebuild the package | built from a clean pin worktree by this lane; every non-identical member re-proved equal to the pin's blob and the zip re-hashed |
| Closed L6 with the L1 re-read inside it | L1 was closed at the superseded pin; legs do not reopen, so the new-pin reads ride L6 and say so |
| Did not push | TO BOUNDS 4 and the shared-branch law; push state is LOCAL @fb1d570c2d, origin box/dell1 at dc14ea7726 by ls-remote |

## Files Modified

- `org/critical_paths/change_management/20261011T0421Z_amgt-resapp-r89-nn7-scoped-api-dell1_deploy_completion.md` (CLOSED)
- `org/critical_paths/.open_deploys/amgt-resapp-r89-nn7-scoped-api-dell1.json` (sentinel removed)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-nn-7.redeploy-peer-identity-subject-cap-and-dossier.proof_of_spec.json`
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit fb1d570c2d)

## Next Steps

1. `[2.0.0_SA_COO~R1]` Report in the instance; flip is by this seat. 2. `[2.0.0_SA_COO~C1]` Read TSM US, SAN FP, ROG SW on
the live function (this seat's L9 compare is the delta baseline). 3. `[0.0.0_AB_MSTR~DELL1 / box-sync]` Push fb1d570c2d.
