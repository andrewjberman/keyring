# DSGN_AMGTV1 round 40 -- CTO review of portal e6ab82ad (Security Analysis open to every Opal employee), `1.0.0_SA_CTO~Z`, 2026-10-05 ~15:2xZ

**Input:** `2.0.0_SA_COO~D` msg 29639, drain @793c52cb25. **Andrew-direct ~15:0xZ**, record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261005_150xZ_SECURITY_ANALYSIS_ALL_OPAL_EMPLOYEES_REQUIREINTERNAL_LEADPANEL_LOAD_TO_COO_Z.md`:
"Yeah should not require admin access to see."

## Read

- **Placement:** `e6ab82ad` CONTAINS `origin/DEV` `71097b53`, so it is a fast-forward. 1 file, `src/App.tsx`, +6/-9.
- **The nav item** `/security-analysis` drops `requiresDev` and `requiresAdmin` and gains `requiresTier: 'internal'`.
- **Both routes** (`/security-analysis` and `/security-analysis/:securityKey`) move from `ProtectedRoute requireDev requireAdmin` to
  `ProtectedRoute requireInternal`.
- **`requireInternal`** denies unless `claims.firmId === 'opal-capital'` (`ProtectedRoute.tsx:119`), so partner-firm users are refused.
  It is the same guard 9 other routes in `App.tsx` use.
- **Investor Reporting is unchanged** (still admin + internal).
- **The backend admits on firm identity**, with no change (COO~D). The page's API calls therefore work for any Opal employee, and an
  external user is refused at both layers.

## Verdict

**APPROVED for DEV.** The change is exactly Andrew's instruction. The DEV push follows `0.0.0_AB_MSTR~Z`'s practice for his word: his
instruction is on record for this change, and MSTR~Z confirms the push with him if its practice requires a per-push word.

**Owed after the push:** a non-admin internal walk (an Opal employee without admin) shows the page, and a partner-firm identity is
refused. The walker has only the admin role (msg 29610), so the negative arm is read from the guard's own test (access40) until a
non-admin account exists. That account is Andrew's to grant.
