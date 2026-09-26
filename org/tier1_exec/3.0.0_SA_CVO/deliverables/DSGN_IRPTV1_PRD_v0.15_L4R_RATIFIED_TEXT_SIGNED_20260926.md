# L4-R review -- DSGN_IRPTV1 PRD v0.15, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`f12fcbb16e` (v0.15). **Half:** ratified-text,
`half_hash` `b86083922c4a`, ENDPOINT hash `a3636b80d49e`, re-measured with `prd_signoff_lib` at the pin and matching
delivery 101520. **Prior:** REFUSED at v0.14, review @`78d777ddad`, stamp @`6d5f83ffe9`.

**Verdict: SIGN.** The ENDPOINT delta is FWD-23's classification clause only. CONTRACTS is byte-equal, and the section
holds 0 seat serials.

- **R1, CLOSED.** "every security shows its correct class" is gone from the ENDPOINT slice (census: 0 hits). The clause
  now reads: "a security the ETF Classifier already tags keeps that class (VXX is Structured, GLD is Commodities),
  PHYS is Commodities as Andrew named it, and none of them shows as a lumped 'Alternatives'".
  - That is Andrew's precedence rule (record @`714ba46408`: "securities which were already listed/tagged in the ETF
    CLassifier table should retain the same classification") plus the three securities he named.
  - PHYS is named on his word, not on the table's, because the backend COO (~M) found PHYS is not in the Classifier
    (CTO msg 101521). His record names it Commodities and routes the fix to ~M.
  - The clause no longer contradicts FWD-13's "unclassified" (:164) or the "Not promised" classifier widening (:259).

-- `3.0.0_SA_CVO`, 2026-09-26 ~21:4xZ
