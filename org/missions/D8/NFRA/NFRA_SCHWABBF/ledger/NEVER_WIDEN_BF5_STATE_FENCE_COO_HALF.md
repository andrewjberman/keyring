# NEVER-WIDEN co-sign -- the COO half: admit two roles to the firm buckets' fence for the STATE prefixes of the Schwab masters (`TO-BF-h5`, row NFRA_SCHWABBF-W4-S9)

**Signer:** `2.0.0_SA_COO~SB` | **Date:** 2026-10-20 ~19:3xZ | **Act covered:** THREE new rows in `infra/logic/registry/exemptions.json` (two under `opal-data-49financial`, one under `opal-data-cottonwood`) and the shared-infra apply that regenerates the two fences from them |
**Read against:** `infra/aws/terraform/shared-infra/s3-49financial.tf:114-137` and `s3-lgic-firm-buckets.tf:142-170` (statement `DenyForeignFirmPrincipals`, read by worker `0.9.0_WK_NFRA_SCHWABBF~4`); `infra/aws/terraform/modules/opal_name/main.tf:140-300` (the scoped-row renderer); the precedent row `opal-clientops-ews-role` and its pair `org/missions/D7/TCKT/TCKT_EARLYWARN/ledger/NEVER_WIDEN_EWS_D2_STORE_FENCE_COO_HALF.md`; PRD v1.0 C-TIERS (Andrew-direct ~17:0xZ: "a, yes. this needs to go through the same full bronze/silver process that the other masters go through.") |
**The other half:** `1.0.0_SA_CTO`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_BF5_STATE_FENCE_CTO_HALF.md` @4b0036c6cb (msg 109991) -- WRITTEN and SIGNED at the same blast radius (3 rows, 2 principals, 2 buckets, no delete); this half's condition is met. The CTO's one condition, adopted here: within the one cutover window the fence applies first, then the converter deploy, then the puller upload.

**Verdict:** SIGNED for the blast radius below, and ONLY it, once the CTO half is written.

## Why the fence needs rows

R21 homes a tenancy's state in the tenancy's bucket (builder output `address('schwab','49financial','state',<table>,'date=D')` is `s3://opal-data-49financial/schwab/49financial/state/<table>/date=D`; Cottonwood's is `s3://opal-data-cottonwood/schwab/cottonwood/state/...`). The identity-side grants of `BF-g-5` (merged) are necessary and not sufficient: the bucket policy denies every principal outside the firm fence, and neither role is inside it.

## What the act MAY touch (the whole permitted set)

| what | change | rollback |
|---|---|---|
| `exemptions.json`, key `opal-data-49financial` | ROW 1: principal `quartz-si2-spike-role` (the 0840 box), `actions` [`s3:PutObject`], `prefix` [`schwab/49financial/state/pulls/`, `schwab/49financial/state/daily_pull/`]. ROW 2: principal `opal-assets-silver-schwab-role` (the Schwab converter), `actions` [`s3:GetObject`, `s3:ListBucket`, `s3:PutObject`], `prefix` [`schwab/49financial/state/complete/`, `.../conversions/`, `.../backfill_status/`] | revert the rows, replan, apply: the generated `ArnNotLike` list loses the entries |
| `exemptions.json`, key `opal-data-cottonwood` | ROW 3: principal `opal-assets-silver-schwab-role`, same three actions, `prefix` the three `schwab/cottonwood/state/` tables | same |
| the two fences | each principal list gains the named ARNs, cut down by the three generated Denies (any other action; object keys outside the prefixes; a listing outside them) | same apply, reverse |
| objects under those prefixes | created by the first writes after the cutover | versioning is read at the apply entry; the roles hold no `s3:DeleteObject`; the move tool and the writers never delete |

**3 rows, 2 principals, 2 buckets, 5 prefixes in 49financial and 3 in cottonwood.** No other prefix, no `s3:DeleteObject`, no `s3:Get*` outside the prefixes, no other principal, no other bucket. Per-master narrowing (`08403355.*` for the box; the five master prefixes for the converter) is on the identity side (`BF-g-5`, `monolith-iam.tf` `MonolithSchwabStateWrite`, `silver.tf` `silver_state_write_schwab_firm`); the registry grammar scopes by prefix only, so the fence is table-wide and the identity side is master-wide. That asymmetry is named, not hidden.

## Writers of the named property, counted

The property is "who can write an object under `schwab/<firm>/state/`". **N = 2 writer roles in this act**: the box role (two tables, 08403355 only) and the converter role (three tables; 08403355 and the four Cottonwood masters). The Alongside box's own role (the Cottonwood puller) is `2.0.0_SA_COO~SA`'s act and is not covered here. The repo is the population measured (`BF-p-5`, `BF-v-5`, `BF-g-5` merged on `box/laptop`), not the account: an operator with account admin identity can already write any key.

## Both branches named

- **Object absent (the first write of a partition):** created. Signed.
- **Object present (a rolling object rewritten within one UTC day, or a re-run):** overwritten under versioning; the previous version is the rollback. Signed.
- **Write refused (fence not yet applied):** the puller logs WARN and does not fail the pull; the converter's marker write raises and the Lambda retries; the cutover order puts this apply BEFORE the converter deploy and the puller upload.

## What the act may NOT touch

Any other bucket or firm; any other principal's row; any existing row; the monolith (`opal-data-assets`) keys of any master; 0824 and 0833. Nothing sends.

-- `2.0.0_SA_COO~SB`
