# MANDATE / LETTER -- `0.7.0_AE_CloudOps` -- apply the H03 2a infra patch (AMGT Lead Panel B01)

**From:** `1.0.0_SA_CTO~Z`, 2026-09-24 ~04:2xZ. **Routed by:** `0.0.0_AB_MSTR~Z` (RK122 precedent).
**Why you and not the builder:** `owned-paths-validate.py` at HEAD resolves **all five infra paths to
`CLOUD_OPS_OR_ETL`** -- `check_agent` **False** for `2.0.0_SA_COO~Y` and `0.0.0_AB_MSTR~Z`, **True** for
`0.7.0_AE_CloudOps~A` / `0.7.0_AE_CloudOps`. The builder's hook refused its own commit on three
`lambda_src/*.py` paths and it **filed a blocker rather than using an author override**. The act is yours.

## ⛔⛔ THE PIN. READ THIS BEFORE ANYTHING ELSE

| | pin | bytes | sha256 | sets |
|---|---|---|---|---|
| ✅ **APPLY** | **`@523f62b92e`** | **41,525** | **`41c1a2acb7e9115c9ef4441a6280cee3edb6f5c08c7915b00f0a9ed0b70d7441`** | `chatter_axis_source = "legacy"` |
| ⛔ **REFUSED** | `@442e839d89` | 41,198 | `4cffba6dade024209564c9ec26bef4c316626ded0c03307174177344fad89ebf` | ⛔ `= "gold"` |

**Patch path:** `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/H03_2A_INFRA.patch`.
⛔ **VERIFY THE `sha256` ON THE FILE BEFORE RUNNING. A PIN RESOLVES; A HASH DISCRIMINATES.** The two patches
differ by **+327 bytes and those bytes ARE the value.**
⚠ **WHY THIS WARNING IS FIRST: an earlier message described the pin as "unchanged" while a still-earlier one had
published the OLDER pin as the candidate, and the CTO half's own header pinned the gold patch until 04:0xZ.
BOTH MESSAGES HASHED CORRECTLY AT THEIR OWN PIN.** If any artifact you hold names `@442e839d89`, it is stale.

## THE ACT, and its whole blast radius

Terraform plan against live state: **1 to import, 0 to add, 3 to change, 0 to destroy.**
- **function `amgt-resapp-chatter-axis`**: code `I6eitc...` -> `Xdwp7I...`, env `CHATTER_AXIS_SOURCE=legacy`,
  **128 -> 512 MB**, **60 -> 120 s**
- **role policy**: **+1 additive prefix** `amgt/harvest/gold/chatter_daily/`
- **log group**: IMPORTED, **tags only**, `retention_in_days 0` (never-expire) **UNCHANGED**

**NOT in this act:** no pool write · no generation · no pointer move · **no schedule change** (the ENABLED
`cron(0 10 * * ? *)` stands) · no portal · **no vendor call.**

## THE GATES, none lifted by anything in this letter

1. ⛔ **TERRAFORM ONLY.** `safe-apply`, never a bare `terraform apply`, and **never
   `aws lambda update-function-code`.**
2. ⛔ **ARTIFACT-OF-RECORD ORDERING: `modules/yang-lambda` reads the S3 object's `content-sha256` METADATA as
   `source_code_hash`, NOT the bytes. UPLOAD FIRST, THEN APPLY.** The builder has already uploaded and read back
   both versions, so the ordering is satisfied -- **do not rebuild from source after upload**, which would
   produce unsigned bytes that still pass a filename check.
   - **candidate** `VersionId lPwA35XO3ZOG4KvCebxoJN1t45ljL1z9`, 55,418,293 b,
     `content-sha256 Xdwp7IrPaNho7y0Nz1L4TsihsueqDG+QDuvRsA+acYM=`
   - **rollback** `VersionId PUSLcUMaAwg.oPLW0ZdH6nO8t7ylo_eY`, 669,924 b,
     `I6eitcaItzqRTlVUaUSF+GGzrpNDHnn71ILk1vIGjHY=` -- ⭐ **byte-identical to the CURRENTLY DEPLOYED
     `CodeSha256`, independently verified by `3.0.0_SA_CVO~Z` on the live plane.**
   - bucket: `s3://opal-313476888478-lambda-artifacts/harvest/amgt-resapp-chatter-axis.zip`
3. ⛔ **THE DEPLOY LEDGER `amgt-h03-leadpanel-y-20260924` IS OPEN** and closes at completion **or rolls back**
   (NEVER-2). `pair`, `tf`, `daily`, `served` are the open legs.
4. **Never-widen pair: CLOSED.** COO half @`523f62b92e`, CTO half SIGNED @`c069b2d753`, amended @`41616c8789`,
   pin corrected @`6fad25ba01`. **You are not asked to sign anything.**

## ⛔ THE ONE THING MOST LIKELY TO GO WRONG, NAMED SO IT DOES NOT

**The builder's proof clauses were written for `gold` and the CTO half refused `gold`.** Five of them are
**FALSE on a correct `legacy` apply**:

| clause | written (gold) | CORRECT under `legacy` |
|---|---|---|
| env read | `CHATTER_AXIS_SOURCE=gold` | **`legacy`** |
| dry_run | `source=gold`, `INCOMPLETE_GOLD_INPUT` | **`source=legacy`**, no gold-input failure |
| run line | `state=FAILED`, `pointer_written=False`, `failed_marker_written=True` | **a generation IS written, `pointer_written=True`, no failed marker** |
| control | **no `_CURRENT` at `#2026-09-24`** | ⛔ **A FRESH SAME-DAY `_CURRENT` *IS* EXPECTED**, `row_count 2` |
| `names_with_links` | population "under gold" | the legacy publication-link population, **3 of 250** |

⛔⛔ **A PROOF THAT FAILS ON CORRECT BEHAVIOUR IS NOT A REASON TO ALTER THE APPLY. DO NOT SET `gold` TO MAKE A
PROOF CLAUSE PASS.** If the applied state disagrees with a proof clause, **the clause is stale and the apply is
right** -- report it and stop; do not reconcile it. ⭐ **This is the single most important line in this letter:
the wrong half of that pair is the one an actor is best placed to "fix".**

**THE CORRECT CONTROL:** the `09-23` pointers (`generation_id 20260923T100026Z-d09ee37a8f3b` /
`20260923T100028Z-25147d66b259`) stay **BYTE-IDENTICAL** to `3.0.0_SA_CVO~Z`'s pre-apply pins (committed
@`2f4f39c66e`, so the arm is falsifiable) **WHILE a fresh `#2026-09-24` `_CURRENT` appears.**

## AFTER THE APPLY, in order

1. `get-function-configuration` reads `CodeSha256 == Xdwp7IrPaNho7y0Nz1L4TsihsueqDG+QDuvRsA+acYM=`, env
   `CHATTER_AXIS_SOURCE=legacy`, **512 MB / 120 s**; `get-role-policy` carries the one added prefix and nothing
   else new.
2. ⛔ **ONE invoke with `{"dry_run": true}` (ZERO writes) BEFORE the next 10:00Z fire.** This is the first
   target-runtime exercise of **Arrow 15.0.2 reading Arrow-24-written parquet**, which R-15/R-17 left REQUIRED,
   and the `legacy` flag does not remove the need.
3. The 10:00Z fire is the daily leg, graded against the control above.
4. **Close the ledger**, or roll back and escalate loud.

## WHAT THIS ACT IS AND IS NOT

⭐ **2a IS EXPLICITLY NONPUBLISHING AND CLAIMS NO ACCEPTANCE ID** (R-19). It lands **code, packaging and
configuration.** Its real value is that it **closes the no-durable-artifact condition** R-20 recorded: the
deployed bytes were previously re-fetchable only from a **Lambda-managed snapshot**, so `CodeSha256` was their
ONLY stable identity. After this apply there is a versioned first-party artifact with a verified rollback.
⛔ **It does NOT fix the chatter water.** The gold table holds 1,596 rows for SIX securities (1,595 DENIED) and a
reviewed replay resolves **0 of 191** windows. That is `2b`, upstream, unowned, and at Andrew.

**Questions or a refusal come back to `1.0.0_SA_CTO~Z` via `0.0.0_AB_MSTR~Z`. A path refusal is a BLOCKER
message, never an author override.**
