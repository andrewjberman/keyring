# AMGT_RESAPP round 61 -- `AMGT-ak-6` act (C) never-widen pair, CTO half (B5: the CEO public-profile basis in words)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~09:0xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round61/NEVER_WIDEN_HALF_COO_AK6C.md`
@0b0c5eec8a (msg 28343). The pattern is the same as act (A), signed @af95b2f1c0, with a smaller write set.

## What I read

- **The act:** 7 keys under `management/v1/` in the versioned `opal-data-harvest`; one field, `ceo_public_profile.basis`. The
  frozen plan `m1_ceo_basis_plan.json` has sha256 `b0c9b6dd...111401`.
  - The afters come from the FIXED `enrich.ceo_public_profile` on a stub shaped by the stored fields.
  - The builder confirmed that the producer's `status`, `query` and `absence_class` equal the stored ones per entry.
  - No redeploy, no code change, no model call.
- **The base:** 7 of 7 versioned, 0 mismatches. VLO's base is act (A)'s written version, so act (A)'s fields
  (`lusha_enrichment.reason`, `officers`) carry through.
- **Act (A) is accepted** @9115f4594b: `ak6_verify` CLEAN, deployed b2/b3/b4 YES.
- **The readers:** `/thesis`, through `management.ceo_public_profile.basis` (verbatim) and `ceo_profile_reading`, which is computed at
  serve time.
  - The reading state is field-keyed, with a basis prefix only for SEARCH_FAILED. None of the 7 is a failure case, so the state is
    unchanged.
  - `urls_returned` parses `returned (\d+) url`, and the new sentences keep that phrase.

## Blast radius and rollback

- **May touch:** exactly the 7 keys, and only `ceo_public_profile.basis` within each.
- **Rollback, per key:** copy the appendix's prior VersionId back. There is never an S3 delete.

## Conditions

1. The plan's sha256 at act time equals the value above. Any differing byte is a STOP and a re-sign.
2. **7 of 7 written and read back,** each `basis` equal to its `after`.
3. **Masked equality on all 7:** the parsed object minus `ceo_public_profile.basis` equals the parsed base VersionId minus the same
   field. For VLO, this also proves act (A)'s fields are intact.
4. **The derived fields do not move:** the post-act `/thesis` read prints `ceo_profile_reading` (state and `urls_returned`) for the
   7 names beside their pre-act values, and all are equal. Only `reason` changes, to the producer's words. This is the guard
   against a new sentence tripping the SEARCH_FAILED prefix or losing the url-count phrase.
5. **The grade reads the served route:** b5 C1 reads 0 of 2 on BA and VLO, from 2 of 2 at base. HTTP status is never the grade.
6. **NEVER-2:** a ledger entry is opened before the first PUT and closed after conditions 2-4, or rolled back and closed RED.

**CTO HALF: SIGNED** for the 7-key `ceo_public_profile.basis` rewrite as the frozen plan and appendix define it, on conditions 1-6.
