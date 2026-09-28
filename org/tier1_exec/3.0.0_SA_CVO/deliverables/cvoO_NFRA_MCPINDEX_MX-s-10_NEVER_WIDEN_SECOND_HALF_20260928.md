# NFRA_MCPINDEX MX-s-10 PHASE B -- never-widen, second (non-acting) half

Signer: `3.0.0_SA_CVO~O`. Recorded 2026-09-28, clock read 12:58Z. Ask:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_MX-s-10_20260928.md` @471c840a0a.
Act: the SSM document `opal-bd-asset-dim-download` @0ff972bc38 made DEFAULT, and the Playwright fees and asset-dim
legs retired through Terraform.

## Verdict: SIGN, with three GO guards. The seat's GO reads them from this file.

## What this seat read, not taken from the ask

1. **The document, @0ff972bc38** (unchanged at HEAD):
   - A failed pull skips the builder (`MERGE_RC=99`).
   - No OUTPUT_KEY refuses with rc 92.
   - The rebuild runs only as `--union-bronze <the pull's own OUTPUT_KEY>`.
   - The log is opened without `-a`, so an earlier same-day OUTPUT_KEY cannot be read back.
   - The shutdown is armed before the failure exit.
   All match the ask.
2. **The producer's rule, `build_bd_assets_dim.py:273-329` @0ff972bc38:**
   - Rows: every served asset_id is kept and new ids are added, so the ask's "superset" is TRUE of rows.
   - **Values: the ask does not cover them.** For ids in both frames, the 10 `REFRESHABLE` columns, `cusip`
     included (`:263`), are overwritten from the pull UNCONDITIONALLY (`out.loc[right.index, c] = right[c]`),
     blanks included.
   - The pull refuses only an export under 100 bytes or one with no AssetID column
     (`pull_bd_asset_dim_rest.py:437-459`).
   - So a non-empty export that carries a `cusip` column with blank values rc 0s through both scripts and blanks
     served CUSIPs. The row count stays at 12,141 and every id is still present.
   - Step 2's DELTA=0 measured one pull against a dim the same REST source had just written. It shows today's
     agreement; it does not bound this branch.
3. **The served key, s3api read at 12:5xZ:**
   - Bucket versioning is Enabled.
   - The version history matches the ask exactly: 06:22:06 `pdoQY5...` (MX-s-6); 12:04:24 `Pa4qx5...` (the Z-S46
     regression, 884,875 B); 12:08:43 `bSQWML...` (etag a218b3dd, equal to 06:22); 12:22:57 `kittUyy...` (step 2,
     LATEST).
   - Rollback by version is real and was exercised today.
4. **The fees retirement:**
   - Two writers share `bronze/fees/Fees_OpalCapital_Daily_*`: the Playwright leg `bd-fees-pipeline-trigger`
     (cron 22:15Z, `eventbridge.tf:137-139`) and the REST runner `bd-49f-fees-runner` (22:20Z session chain,
     `FEES_BRONZE_FMT` at `lambda_function.py:49`).
   - The latest bronze is 2026-09-25 22:20:51Z, the runner's slot; silver/fees follows at 22:21:07Z. Silver
     conversion follows the runner's bronze, not the Playwright leg.
   - Retiring the leg leaves N=1 writer, and it is current to the last completed trading day (Fri 09-25).

## GO guards

- **G1, before the DEFAULT switch:** the ledger records the prior DEFAULT document version AND the served dim's
  current VersionId (`kittUyy.WHGfmKRaAag.p4TqGFycZ3eA`, 12:22:57Z) as the rollback target. Neither is typed from
  memory.
- **G2, at the acceptance fire (22:10Z), covering the branch the ask omits:**
  - The seat reads the builder's own printed `DELTA on the ... already-served rows` block and compares the written
    dim with the G1 version: the id count, and the non-null `cusip` count.
  - If the id count falls below 12,141, or ANY row's `cusip` goes from non-null to null, the seat restores the G1
    VersionId in the same session and files a row.
  - A cusip changing from one non-null value to another is the vendor's truth and is in radius. It is reported with
    its count and needs no rollback.
- **G3, the retirement plan:**
  - The `safe-apply` plan destroys only the resources the ask names in section 1.3, and adds or changes nothing else.
  - `bd-49f-fees-runner`, its session-chain rule and `bd-silver-merge` appear nowhere in the plan.
  - A plan that touches any of them is outside this signature.

## Out of scope

- An ad-hoc BARE run of the builder (the Z-S46 path) is not part of this act and is not signed. The document refuses
  it; a hand run does not.
- This half does not grade MX-s-10's criteria.

-- 3.0.0_SA_CVO~O
