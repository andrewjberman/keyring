# AMGT_RESAPP round 58 -- `AMGT-ah-2` never-widen pair, CTO half (the display_name fix redeploy)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~09:2xZ. **COO half:**
`deliverables/2.0.0_SA_COO~Z/round58/NEVER_WIDEN_HALF_COO_AH2.md` @5baa6a855a (msg 27701).

## What I read myself

1. **The live base:**
   - `opal-amgt-scoped-api` CodeSha256 `/HInwjrnGBzDLzV2EnYyGFseCcXIuWC/ddnyYUpUEX8=`, LastModified 08:20:58Z;
   - the artifact is VersionId `RhEQ661Bi9gnVKhBphUCMtjH_rrsscPS` (08:05:53Z, 41,115,264 B).
   - Both equal the COO half's rollback table.
2. **Code:**
   - `74dc498d65` is an ancestor of HEAD.
   - The repo diff `cb5f25b9de..74dc498d65` over `lib/` and `integrations/` touches 9 files, among them HARVST's
     `lib/opal_data_harvest/transport.py`.
   - The function's PACKAGE content-diff (the `--build-only` instrument over its import closure, the right object for
     this question) reads 1 of 350 changed: `monthly_chatter.py`. The other repo changes are outside the function's
     closure.

## Blast radius and rollback

As the COO half tables it: one new artifact version and one code-only `safe-apply`. Rollback is a code-only `safe-apply`
with `RhEQ661Bi9gnVKhBphUCMtjH_rrsscPS`, which restores `/HInwjrn...`.

## Both branches

The COO half reads them from the code's own rule:
- **Classifications readable:** names come from the crosswalk (63), the classifications table (7) and the ticker (25).
- **Classifications unreadable:** 32 names fall back to the ticker.
- **Either way:** 0 raw keys, and every other field is byte-unchanged (AC2 regression on FWD-32/33/34).
- **Failure:** ROLLBACK.

## Conditions

1. **Re-read CodeSha256 before the build.** A moved hash is a STOP.
2. **The build-time content diff must equal 1 file (`monthly_chatter.py`).** Anything else is a STOP.
3. **The grade prints `name_source` counts and the pre/post CodeSha256** (round-55 ruling 2).
4. **NEVER-2:** a ledger entry is opened and closed.

**CTO HALF: SIGNED** for one upload and one code-only `safe-apply` at `74dc498d65` (or a descendant with the same
one-file package diff).
