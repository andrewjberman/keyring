# Deploy Completion Record
**Date opened:** 2026-09-25T18:03:34.972519+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T185529Z
**Deploy:** AMGT_RESAPP rq-2: the redeploy -- opal-amgt-scoped-api carries rq-1's export rule
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.scoped_amgt_api.aws_lambda_function.this (opal-amgt-scoped-api) | CodeSha256 AFTER differs from BEFORE pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo= and LastUpdateStatus=Successful (AC1); prior artifact VersionId VTj2mj_gOKupat_bPjetck3HPD0N6PIJ recorded as the rollback | AC1 exit=0. CodeSha256 moved pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo= -> FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw=, LastUpdateStatus=Successful, LastModified 2026-09-25T18:31:46Z. The deployed sha EQUALS the uploaded artifact's metadata content-sha256 and the locally computed sha. Artifact VersionId VTj2mj_gOKupat_bPjetck3HPD0N6PIJ -> ujFHMNbjbg6Yv3wFotVvfDPnF4reNQdO, 848867 -> 856314 bytes, ETag b2e056eb7cf4ecfc1489a7461e5b190e; the prior version is preserved by bucket versioning (Enabled) and is the rollback both halves name. Plan was exactly 0 add 1 change 0 destroy, in-place, only s3_object_version + source_code_hash + last_modified, 28 attributes and 4 blocks unchanged, no second resource, so the order's refusal never fired. 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Replan reads 'No changes. Your infrastructure matches the configuration.' All three stop limbs were graded CLEAR before the apply and are enumerated in this entry: limb 1 (3 of 14 changed files ship, exactly the half's table; backlog.py outside the table does not ship; the 6 Lambda-called crosswalk functions 6 of 6 identical), limb 2 (build_pack byte-identical, with build_rich_text CHANGED as the negative control), limb 3 (scoped_amgt.py untouched entirely). | CLOSED 20260925T183511Z |
| L2 | verify | the served /print?format=rich body across the 89-name snapshot | AC2 served over 89 of 89 folders: OK 89, NOT_OK 0, CAPTURE_FAILED 0, exit=0 | AC2 exit=0, matching the order's expected string exactly: 'served over 89 of 89 folders: OK 89, NOT_OK 0, CAPTURE_FAILED 0'. Read on the DEPLOYED bytes FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= after the apply. NON-VACUITY CHECKED rather than assumed, because a clean 89-of-89 is the shape a short-circuit also produces: the script passes --cache into a FRESH mktemp -d, so every one of the 89 is a live capture and not a replayed one; CAPTURE_FAILED 0 is printed beside the denominator, so 89 captures actually happened; and the script's own non-OK filter (grep -v ' OK $' over '^[0-9]+/89 ' lines) printed NOTHING, which is the correct output only when no name failed. The exit I recorded is the sweep's own rc (the script ends 'exit $rc'), not a wrapper's or a pipe's. LIMIT STATED RATHER THAN IMPLIED: unlike ro-7's AC2, this criterion carries NO pre-act negative arm from this session -- the sweep was run once, after the apply, so the world did not supply a failing arm here. What stands in its place is indirect and is named as such: AC1 proves the deployed bytes moved, and the limb-1 subtraction proves render_pack.py (rq-1's rule, the changed build_rich_text at L788-941) is one of exactly 3 files that shipped. I did not manufacture a planted-mutant control after the fact. | CLOSED 20260925T185319Z |

## Log

- 20260925T180334Z OPENED by 0.7.0_AE_CloudOps~A with 2 leg(s)
- 20260925T183511Z LEG L1 closed: AC1 exit=0. CodeSha256 moved pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo= -> FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw
- 20260925T185319Z LEG L2 closed: AC2 exit=0, matching the order's expected string exactly: 'served over 89 of 89 folders: OK 89, NOT_OK 0, CAPTURE_FAILED
- 20260925T185529Z CLOSED -- all 2 legs proven
