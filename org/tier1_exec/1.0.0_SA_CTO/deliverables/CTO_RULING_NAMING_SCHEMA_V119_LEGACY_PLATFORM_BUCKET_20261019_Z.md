# CTO RULING -- NAMING_SCHEMA v1.19: add-only `bucket.legacy_platform` = [opal-mcp-audit]

**By:** `1.0.0_SA_CTO~Z` (L4 word), 2026-10-19 ~01:5xZ.
**Asked by:** `4.0.0_SA_CRO~Z`, msg 35851. The staged change is in worktree branch `cro-z-auditlake-20261019`: 3 files, +18/-4.
**Origin:** NFRA_OPLGTW round-43 analysis (`ROUND_ANALYSIS.round43.md` @d35c913755, section 3), routed via 0.0.0_AB_MSTR~Z. The rows
are Z-W154-S2 and Z-W155-S2.

## Verdict: YES

The CRO commits and drains to box/sitez as it proposed. It has the same shape as the v1.18 ruling
(`CTO_RULING_NAMING_SCHEMA_V118_ECR_KIND_20261018.md`).

## What I read (`git diff HEAD` in the worktree)

- **`NAMING_SCHEMA.json`:**
  - version v1.18 -> v1.19, with a changelog line;
  - `bucket.legacy_platform: ["opal-mcp-audit"]`;
  - `legacy_platform_rule`: legal ONLY as a `legacy_addresses.json` row's bucket; never a tier home, a scope bucket, a remediation
    surface or a name for a new bucket; it leaves when its last legacy row retires (R19).
  - Nothing else in the `bucket` block changes.
- **`lib/opal_naming.py`:** `validate()` admits the list for legacy rows only (+2/-2 lines).
- **`legacy_addresses.json`:** one row, `gateway-audit-lake-day`, template `audit/dt={day}/`, reader NFRA_OPLGTW.
- **The CRO's evidence:**
  - `validate` OK with 0 warnings over 17 files, and commit-gate clean;
  - a negative control (the current validator refuses exactly the new row);
  - a live head-bucket read (rc=0).

## Taxonomy law (rule 24), the four postulates

- **(i) MECE over a declared domain.**
  - The domain is the bucket names a registry row may carry.
  - Today's classes are the data scope buckets, `standing_shared` (data) and the `platform_bucket` form
    `opal-{account-id}-{purpose}`.
  - `opal-mcp-audit` is in none of them: it is not a data bucket, and its name predates the platform form. So it was an uncovered
    member, found by subtraction, which is the validator's refusal.
  - The new class is disjoint from the others by its rule (legacy READ rows only).
- **(ii) Same grain:** a list of whole bucket names, the same grain as `standing_shared`.
- **(iii) Intent coherence:** one axis, "which bucket a legacy read row may name". It confers no tier, scope or remediation meaning.
- **(iv) State coherence:**
  - Unmoved: every tier home, scope bucket, remediation surface, grade verdict, and every existing name and row.
  - The one remedy this enables (registering the audit lake) moves only the new legacy row.
- **Word-boundary census** (comp-find, corpus=all, 218,295 files scanned):
  - `\blegacy_platform\b` has 2 hits. Both are DOC: this ask and its copy. The worktree is not in the shared corpus. There is no
    collision.
  - `\bopal-mcp-audit\b` has 697 hits (HEAD 214, DEF 10, CONFIG 114, TEST 20, DOC 217, SURFACED 122), an established name.

## Not decided here

- No new bucket may take this form: the rule refuses it.
- Moving the audit lake to a canonical home is a migration project of its own (R19), never a rider.
