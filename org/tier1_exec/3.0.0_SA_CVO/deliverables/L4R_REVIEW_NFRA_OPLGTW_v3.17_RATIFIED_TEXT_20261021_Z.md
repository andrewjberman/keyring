# L4-R review, NFRA_OPLGTW PRD v3.17 (FWD-23 withdrawn), ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-21 ~14:3xZ)

**Asked by** `1.0.0_SA_CTO~Z`, ferry 20261021T135339Z, which withdraws msgs 36278, 36280 and 36283. Read. It is not acked:
this seat's broker tools are disconnected.

**Bytes reviewed:** `git diff 1ae82e6749 0723d15aa8` on the PRD, read whole.
- FWD-23 is removed from the ENDPOINT section and from the header's outcome list.
- The v3.17 addendum records Andrew's word: "yeah the purpose here is to intentionally be light, i will transcribe a spec on
  the intention of how this should work and send it to CRO for a brief."
- The PRD at HEAD equals the pin.

## The ENDPOINT is the bytes I already signed

`prd_signoff_lib.endpoint_hash`, computed by this seat over the PRD at each commit from my last SIGN (`95d985d1a5`, v3.1)
to HEAD:
- every commit from `7fc8fb3907` through `f2b066d9ad` (v3.14) reads `18622a31f500`;
- `866ccad604` (v3.15) reads `6d2d825f09d4`, and `1ae82e6749` (v3.16) reads `147af003ff58`;
- `0723d15aa8` (v3.17, HEAD) reads `18622a31f500` again.

The ENDPOINT is therefore byte-equal to the section this seat signed at v3.1. The "drift" the status line shows is only my
own last stamp's bytes.

**The bound.**
- The ratified-text half's own hash is `555c74c021f7`, computed at HEAD. It also covers CONTRACTS, which moved from v3.2 to
  v3.14 in CONTRACTS-side addenda.
- This seat did not re-read those addenda as text here. Several reached it piece by piece through never-widen halves, for
  example the v3.2 firm-scoped reader roles (this seat's REC) and the v3.14 client_* fail-closed admission.
- The stamp binds to the ENDPOINT (spine v3.19). A CONTRACTS wording change re-opens nothing, and this signature says no
  more than that.

## A correction to my own record

- My refusal stamp of 13:5xZ (`L4R_REVIEW_NFRA_OPLGTW_v3.15_RATIFIED_TEXT_20261021_Z.md` @30e41b770c) bound to
  ENDPOINT hash `147af003ff58`, which is v3.16.
- `prd-signoff` reads the PRD at HEAD, and v3.16 (`1ae82e6749`) had landed before the stamp ran.
- So the stamp's bytes were v3.16 while its review graded v3.15. Both versions are now withdrawn, so nothing turns on it.
  It is recorded so the stamp history reads true.

## Verdict: SIGN the ratified-text half at v3.17

## For the brief, not grounds

The v3.15 and v3.16 text stays in the PRD as INPUT to the CRO's brief. This seat's two reviews of them are input of the same
kind, and the brief should carry both points:
1. **v3.15 (@30e41b770c):** keep "a column whose class is not decided is forbidden". `date_of_birth`
   (`schwab_schemas.py:155`) is in neither the served class nor the four forbidden ones, so it is Andrew's call.
2. **v3.16 (`L4R_REVIEW_NFRA_OPLGTW_v3.16_RATIFIED_TEXT_20261021_Z.md`, committed with this file):** a column-name drop
   protects Parquet only. A read of "any object ... text as text" over `opal-data-assets` reaches the raw vendor extracts in
   `schwab/<master>/bronze` (`schwab_schemas.py:8`), which carry tax ids, addresses, email and phone. The forbidden fields
   must be dropped on every read path, or the raw prefixes left out.

-- 3.0.0_SA_CVO~Z
