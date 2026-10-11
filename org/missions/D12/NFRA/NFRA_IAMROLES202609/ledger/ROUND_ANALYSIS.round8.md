# NFRA_IAMROLES202609 -- ROUND-8 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~18:3xZ. **Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33357,
`surprise-channel/remediations/REMEDIATION_v8.Z.md` @28b6af06ae. **Recut by:** `2.0.0_SA_COO~ZI`, in ONE issuance.

## Round 8, as read

2 of 2 orders are complete (`ledger/COMPLETION_REPORT.round8.json` @be0536cad9), MAY-CLOSE.
- **y-1 FAIL, narrow (Z-C-S42):** `/cloud-ops` 18a's fallback counted `2026*.md`. **Fixed by this seat @f326f70e16:** the
  pattern is now the filename grammar `[0-9]{8}T*.md`, exercised on a planted inbox (one 2026 message, one 2027 message,
  one in `read/` and one dotfile give `unread=2 state_markers=1`). Z-C-S42 is met, for the CVO's next compile.
- **y-2 PASS:** the sweep's three classes are exercised; 7 ABSENT names re-read at 404, and 2 foreign names at 403.

## Rulings on the sweep's findings

| finding | ruling | cell |
|---|---|---|
| **5 ABSENT names with live Allows nobody decided:** `ajb-workflow`, `opal-data-portal-s3`, `opal-data-smartx-v2`, `opal-market-update`, `opal-data-smartx` | **NARROW, resource grain**, the x-2/x-5 shape: per role, a reference census (env and deployed code, positive control), then remove only the dead ARNs. Write-bearing grants go first. One pair per module or IAM-API act | **E1** |
| **`opal-data-schwab` (404) -- a READER, not just a grant.** `/49-schwab-conv` marks `s3://opal-data-schwab/01_raw/` DEAD (frozen 2026-07-15), yet `data/canonical/schwab/build_canonical_daily.py:154-156` STILL enumerates it, by the skill's own note | **Higher stakes than a dead grant: whoever claims the name could feed bytes into the canonical Schwab build.** Two acts in one cell. (a) The canonical builder stops enumerating the dead bucket: its owner removes the read, and this project routes it through `0.0.0_AB_MSTR~Z` if the owner is off site Z. (b) Then the Allow is narrowed. **Order: (a) before (b)**, because narrowing first would turn a silent dead read into a loud AccessDenied that the builder might not handle. Also correct the skill's description line naming `opal-data-schwab` as the sync target | **E2** |
| **Z-S43:** `opal-market-data-v2`, deleted on Andrew's ruling (2026-07-30) and tombstoned, still has its Terraform declaration and one live Allow with write | **One pair:** remove the declaration (TF-debt A7) and the Allow together. `safe-apply` already refuses the re-create. This also settles round 7's E2 market-overview read | **E3** |
| **3 wildcard grants** (`opal*`, `opal-*`, `opal-data-*`) skipped by the sweep | **READ-ONLY census first:** for each grant, its role, actions, and the concrete buckets that role actually addresses (env, deployed code, and the bucket list under our account that matches). A wildcard is replaced by that explicit list next round. A wildcard has no single name for `head-bucket` to classify, so it is graded by what the role actually uses | **E4** |
| R20 bridge (Z-S34, cutoff 2026-12-31) | Carried. Retire it when dell1's FWD-8 is in `box/sitez` | this seat |

## ENRICHMENT LIST -- round 9 (cut in ONE issuance)

E1 (narrow 5), E2 (schwab: reader out, then grant), E3 (market-data-v2 declaration plus Allow), E4 (wildcard census,
read-only). The Z-S40 and Z-C-S36 standing clauses apply to every pair and table.

-- 1.0.0_SA_CTO~Z
