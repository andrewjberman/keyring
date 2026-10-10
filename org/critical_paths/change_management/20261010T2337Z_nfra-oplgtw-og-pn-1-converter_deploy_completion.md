# Deploy Completion Record
**Date opened:** 2026-10-10T23:37:42.218004+00:00
**Status:** OPEN
**Deploy:** OG-ap-5 / OG-pn-1 Phase B: opal-assets-silver-schwab D-tag routing apply + re-run of the six held 08403355 RPS dates
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | box/sitez carries the pin move and the pre-swap record | hashes d40a3cd977 (silver_build_commit.schwab -> b3e481b261) and 4b93e8681b (ap5_build.json) |  | OPEN |
| L2 | s3-prefix | new artifact uploaded to opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-schwab.zip | head-object VersionId + Metadata.content-sha256 equal to the built hash uibjggn93MPPtuIh33Yvehv1xECqrfhPxsWLdmcdYjE= |  | OPEN |
| L3 | activation | terraform apply via safe-apply, -target module.silver_converter[schwab], expecting exactly 3 rows (OPAL_BUILD_COMMIT, s3_object_version, source_code_hash) | live CodeSha256 equals the built hash, State Active, LastUpdateStatus Successful |  | OPEN |
| L4 | verify | 0-diff targeted plan after the apply | terraform plan reads No changes |  | OPEN |
| L5 | activation | ONE direct invoke naming exactly the six bronze RPS keys of 08403355 (no bronze write) | invoke response plus every written key VersionId recorded in ap5_rerun.json |  | OPEN |
| L6 | verify | closure read of all six dates and the served history | bh1.sh AC2 reads qualified 758 open 0, and ap5.AC1 PASS |  | OPEN |

## Log

- 20261010T233742Z OPENED by 0.7.0_AE_CloudOps~Z with 6 leg(s)
