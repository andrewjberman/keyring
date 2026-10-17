# NEVER-WIDEN co-sign -- the COO half: admit `opal-clientops-ews-role` to the 49financial fence for ONE prefix (`TO-EWS-d2`, row TCKT_EARLYWARN-D1-S7)

**Signer:** `2.0.0_SA_COO~Q1` | **Date:** 2026-10-17 ~09:3xZ | **Act covered:** ONE new row in `infra/logic/registry/exemptions.json` under `opal-data-49financial`, and the shared-infra apply that regenerates the fence from it |
**Read against:** `lib/opal_naming.py address()` output as recorded by `0.7.0_AE_CloudOps~TM1` in row D1-S7; the launcher at `3ca3785007` (`infra/aws/ec2/client-ops-early-warning/Dockerfile`, `fetch_store`, `persist_store`); `infra/logic/registry/exemptions.json` at HEAD (the 29 existing 49financial rows, including the scoped-prefix precedent `opal-ticket-api-role`) |
**The other half:** `1.0.0_SA_CTO~DELL1`, `ledger/NEVER_WIDEN_EWS_D2_STORE_FENCE_CTO_HALF.md` -- NOT yet written; this half is **SIGNED CONDITIONALLY: it takes effect only when the CTO half exists and names the same blast radius.** Source: `TO-EWS-d2` (CTO exercised read of `TO-EWS-d1`, msg 7455).

**Verdict:** SIGNED for the blast radius below, and ONLY it, once the CTO half is written.

## Why this bucket, and why not the other way

R21 homes a tenancy's state in the tenancy's bucket. Both Schwab masters the container reads (08335338, 08242234) are FIRM scopes homed in `opal-data-49financial` (`scopes.json`, read by TM1), so the open-items store belongs there, and the store never mixes firms. The alternative (B), a registry deviation homing it in `opal-data-assets`, needs Andrew's acknowledgement (CLAUDE.md rule 30, R20) and moves client-ops findings out of the firm's own bucket. The scoped-prefix exemption is the routine instrument and has a precedent in this file (`opal-ticket-api-role`, Get and Put on one prefix). I recommend (A).

## What the act MAY touch (the whole permitted set)

| what | change | measured before | rollback |
|---|---|---|---|
| `exemptions.json`, key `opal-data-49financial` | ONE row appended: principal `opal-clientops-ews-role`, arn `arn:aws:iam::313476888478:role/opal-clientops-ews-role`, `actions` [`s3:GetObject`, `s3:ListBucket`, `s3:PutObject`], `prefix` [`schwab/49financial/state/ews_store/current/`], `signoff_ref` = this file and the CTO half | 29 rows; the role is in none | revert the row, replan, apply: the generated `ArnNotLike` list loses the one entry |
| the fence statement `DenyForeignFirmPrincipals` on `opal-data-49financial` (generated in `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`) | the principal list gains that one ARN, scoped by action and prefix like the precedent row | statement present, 31 entries read by TM1 | same apply, reverse |
| the object `s3://opal-data-49financial/schwab/49financial/state/ews_store/current/ews.db` | created by the first persist | the prefix `schwab/49financial/state/ews_store/` holds 0 objects (list read at 09:3xZ) | bucket versioning is **Enabled** (read): restore or remove the newest version; the role has no Delete |

**1 key, 1 prefix, 1 principal.** No other prefix, no `s3:DeleteObject`, no `s3:Get*` outside the prefix, no other principal, no other bucket.

## Writers of the named property, counted

The property is "who can write the store object". **N = 1 writer**: `persist_store` in the container launcher (`put_object` to `PERSIST_KEY`, `Dockerfile` launcher at `3ca3785007`), run by the one task. The launcher is the only code that names the key; the repo is the population measured, not the account (a human operator with account admin identity can already write any key).

## Both branches named

- **Object absent (today):** the launcher logs `store_fetch none_found`, starts empty and replays all 573 dates (about 3.5 hours at 0.25 vCPU, no resize), then persists. Signed: that is the true first state.
- **Object present and readable:** the launcher resumes at `last_processed`. Signed.
- **Object present and NOT a readable SQLite file** (a corrupt upload): `fetch_store` downloads it, `SqliteStore` opens it and the first statement raises outside the loop; the task would exit and restart, repeating. **Not signed away: it is a named risk.** The rollback above (restore the previous object version) clears it; nobody but an operator writes the key, and `persist_store` writes a `sqlite3.backup` copy, never a live file.
- **Fetch denied or any S3 error:** logged by exception type, the store starts empty and replays (the same cost as the absent branch), never a partial read.

## What the act may NOT touch

Any other firm bucket; any other principal's row; any existing row's actions or prefixes; the secret scope; the role's Schwab silver read grants; the task size. Nothing sends. `AC1` of `TO-EWS-d2` simulates the identity policy only and ignores the bucket policy, so the grade of "the Put really works" is `AC3` (the object exists), not `AC1`.

-- `2.0.0_SA_COO~Q1`
