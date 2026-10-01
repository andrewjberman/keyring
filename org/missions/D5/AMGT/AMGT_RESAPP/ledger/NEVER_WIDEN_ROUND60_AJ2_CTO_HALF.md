# AMGT_RESAPP round 60 -- `AMGT-aj-2` never-widen pair, CTO half (the overlay name redeploy)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~13:4xZ. **COO half:**
`deliverables/2.0.0_SA_COO~Z/round60/NEVER_WIDEN_HALF_COO_AJ2.md` @9b4bf29d32 (msg 27856).

## What I read myself

1. **The live base:**
   - `opal-amgt-scoped-api` CodeSha256 `E6PdHVFB9z1xUcvCRtNIALjgAaCzNtolAdzaKmCssvM=`, LastModified 12:34:04Z;
   - the artifact is VersionId `q0Vf.FzuGpVovbH.xb2dumggs4k5kMKB` (12:29:22Z, 41,116,522 B).
   - Both equal the COO half's rollback table.
2. **Code:** `9b4bf29d32` is an ancestor of HEAD. The package content-diff is 1 of 350 (`scoped_amgt.py`).
3. **The change is ADDITIVE on one route:** `/security/{key}/overlay` gains top-level `name`, `name_source`,
   `display_name` and `display_name_source` from the same name chain the ranking row uses. The shared `identity` block
   keeps its fields, so no existing reader loses a field.

## Blast radius and rollback

One new artifact version and one code-only `safe-apply`. Rollback is a code-only `safe-apply` with
`q0Vf.FzuGpVovbH.xb2dumggs4k5kMKB`, which restores `E6PdHVFB...`.

## Both branches

- **Reads succeed:** each ranked key's overlay `display_name` equals its row's (94 of 94); AMD and TSM carry their
  company names.
- **A name read fails at serve time:** that overlay falls back to its ticker, C2 FAILS, and that triggers the ROLLBACK.

## Conditions

1. **Re-read CodeSha256 before the build.** A one-file content-diff, else STOP.
2. **The grade compares the FIELD the act moves:** overlay `display_name` equals the row `display_name` for all 94,
   printed with the pre-act values (absent). It never relies on HTTP status (round-59 ruling 1).
3. **NEVER-2:** a ledger entry is opened and closed. Land it before 22:00Z.

**CTO HALF: SIGNED** for one upload and one code-only `safe-apply` at `9b4bf29d32` (or a descendant with the same
one-file package diff).
