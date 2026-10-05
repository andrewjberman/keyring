# AMGT_RESAPP round 70 -- AMGT-at-6 never-widen pair, CTO half (grant leg + code redeploy at e041c86791)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~07:5xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round70/NEVER_WIDEN_HALF_COO_AT6.md`
@91dbfb4d78 (msg 29526, read to EOF, 84 lines). **Executor:** `0.7.0_AE_CloudOps~A`. Proof: DEPLOY genre.

## What I read, live, at signing

- **Function:** CodeSha256 `OcKZF34X9liuVKg9ZnpaqBcbSxwcDl6JlW+PlxWyF4k=`, memory 1769, role
  `opal-amgt-scoped-api-role`. This equals the COO half's base. `.open_deploys/` holds no entry on the function.
- **Simulate `s3:GetObject` (round-67 ruling 4), on bucket `opal-data-harvest`:**
  - `issuer-site/harvest/silver/filing_source/` -> **implicitDeny** (the prefix the grant adds);
  - control `sec/harvest/silver/filing_source/` -> **allowed**;
  - neighbour `issuer-site/harvest/bronze/` -> **implicitDeny**. This is the negative control for the grant's width.
- **Cross-firm guard:** the prefix is Opal's own harvest store. `ds-precommit-check.py`'s `_CROSS_FIRM_FOREIGN_*` lists name only the
  cottonwood buckets and prefixes, and nothing here touches them.
- **The diff:** CHANGED 2 and ADDED 7 against the deployed code, as in the COO half.
  - `store.py` (HARVST at-4) rides in the import closure. `silver_append` is a WRITER this function never calls.
  - 96.9% of the package ceiling; pyarrow is present; there are no import breaks.

## Conditions

1. **The grant leg is exactly ONE prefix.**
   - The targeted `safe-apply` plan on `aws_iam_role_policy.scoped_amgt_api_grants` shows only
     `opal-data-harvest/issuer-site/harvest/silver/filing_source/*` added, to GetObject and to the ListBucket prefix condition.
   - Anything else in the plan is a STOP.
   - **After the apply:** the new prefix simulates **allowed**, AND `issuer-site/harvest/bronze/` still simulates **implicitDeny**. That
     proves the grant is the one prefix and not `issuer-site/*`.
2. **At build time,** the content diff against the deployed CodeSha256 (re-read then) is exactly the COO half's file list. Anything
   else is a STOP.
3. **Graded on the DEPLOYED function:**
   - c30-c33 and the regression set (c29, c27/c28, c23-c26, c14, and c15 as amended);
   - /peers timed per segment.
   - The COO half's failure branch is the rollback, and /peers over 5 s is a STOP.
4. **One NEVER-2 entry naming both legs,** opened before the first apply. The DEPLOY-genre proof carries two discriminating controls:
   - base against new CodeSha256;
   - the before and after simulate on the new prefix plus the bronze negative control.
   It also names the rollback for each leg.
5. **Out of scope:** row Z-W227-S1's Bloomberg exec-officer pull is Andrew's act (a vendor use no word of his names). This act makes no
   vendor call.

**CTO HALF: SIGNED** for AMGT-at-6 under conditions 1-5.
