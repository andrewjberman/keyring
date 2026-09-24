# AMGT_RESAPP round 21 -- never-widen pair, `AMGT-rk-82` (H0-iam) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-21 ~22:2xZ. **Status: SIGNED.** Pairs with
`ledger/NEVER_WIDEN_ROUND21_RK82_COO_HALF.md` (signed by `2.0.0_SA_COO~Z` at issuance @`6fb0f4d0bf`).
**Sources:** `ROUND_ANALYSIS.round20.md` @`ab54fb15e0` s.3; PRD v0.17 @`1f7459456a` C-HARVEST-HOME and
C-FORMAT-SEQUENCE; the order `task-orders/AMGT_RESAPP.TO-AMGT-rk-82.harvest-iam-grants.md`.

## `AMGT-rk-82` -- ADD read grants on the new harvest prefixes

### 1. PRE-ACT STATE, read live by this seat (`iam get-role-policy`, ~22:2xZ)

| policy (role) | statements | S3 read resources | list prefixes | new-grammar entries | sha256 (sorted JSON), first 16 |
|---|---|---|---|---|---|
| `opal-amgt-scoped-api-grants` (`opal-amgt-scoped-api-role`) | 4 | 13 (`ReadThePoolPrefixesTheAdapterReads`) | 13 (`ListOnlyThePoolPrefixesTheAdapterReads`) | 0 | `f85199f9b5a08635` |
| `amgt-resapp-chatter-axis-lambda-policy` (`amgt-resapp-chatter-axis-lambda-role`) | 4 | 4 (`ReadThePoolPrefixesTheProducerReads`) | 4 (`ListOnlyThePoolPrefixesTheProducerReads`) | 0 | `d60b058257b60bfb` |

- Both hashes EQUAL the COO half's cut values. The hash method is the same (sha256 over sorted JSON), so this confirms
  the vintage; it does not corroborate the method. The worker's AC3 remains the rollback target.
- **Emptiness of the new grammar, read live:** `opal-data-harvest` holds 0 objects under each of `bloomberg/harvest/`,
  `seeking-alpha/harvest/`, `sec/harvest/`, `barrons/harvest/`, `wsj/harvest/` and `ft/harvest/`. The control
  `management/v1/` holds 18, so the instrument does see objects. Counted client-side over the full listing.

### 2. WHAT THIS HALF COVERS -- both branches

Exactly two `PutRolePolicy` calls through one targeted Terraform apply (plan `0 to add, 2 to change, 0 to destroy`),
each ADDING only:
- **scoped-api:** 8 `arn:aws:s3:::opal-data-harvest/{p}*` read resources, plus the same 8 list prefixes, where `p` is
  one of the eight builder-printed prefixes in the COO half (B1). Counts go 13 -> 21.
- **chatter-axis:** 4 of the same form (B2). Counts go 4 -> 8.

In both, the statement count stays at 4 and no other statement, role, trust policy or resource moves.
- **Branch A (success):** both roles may read empty prefixes. The served output of every route is unchanged, because
  no reader points at the new grammar until its move cell.
- **Branch B (partial):** additive and on empty prefixes, so nothing is exposed. The rollback below runs on AC5's
  mismatch.

### 3. ROLLBACK

Restore the two locals lists to AC3's snapshot, re-run the SAME targeted apply, and re-read both policies. The sha256
must equal AC3's pre-act values (`f85199f9b5a08635` / `d60b058257b60bfb` at this read). Nothing is deleted.

### 4. THE COO'S OPEN QUESTION -- RULED

**Pre-granting read on EMPTY new prefixes, ahead of each move: ACCEPTED.**
- Least privilege is about what a role CAN READ, and an empty prefix yields nothing.
- The grants are read-only and scoped to the builder's exact prefixes (no wildcard beyond `{p}*`).
- Splitting them into each move's window would add an IAM change to every move and make each move riskier.
- **Condition:** each move cell (M1-M4) that REMOVES an old grant must also re-read that the matching new grant is
  present, so a later drift cannot leave a reader with neither.
- The `issuer-site/`, `filings-xbrl/` and `amgt/harvest/state/` grants stay with H2/M2, under their own pair.

### 5. NOT COVERED

Everything in the COO half's NOT COVERED, plus: any apply other than the two named `-target`s, and any grant on a
prefix the builder did not print.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-21 ~22:2xZ. The vintage is this file's commit.
