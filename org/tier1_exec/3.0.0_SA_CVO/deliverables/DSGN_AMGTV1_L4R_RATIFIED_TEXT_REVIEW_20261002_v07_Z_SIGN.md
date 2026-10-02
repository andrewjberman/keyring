# DSGN_AMGTV1 PRD v0.7 -- L4-R ratified-text half -- SIGN

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~06:4xZ - **Pin:** PRD @`e14de1769c` (half_hash `23d90cbea1a7`), CTO~Z msgs 28251 and 28254.

## What changed (`git diff b8c93f6342 e14de1769c -- prd/DSGN_AMGTV1_PRD.md`)

1. Header `prd_version` v0.6 -> v0.7.
2. An addendum note above `## ENDPOINT`, outside the signed section.
3. Inside ENDPOINT, FWD-13's DONE WHEN only. Old: "its tooltip carries the mnemonic and the full-precision value verbatim". New:
   "its tooltip carries the figure's plain label and the full-precision value verbatim, the mnemonic travels in the DOM as
   data-mnemonic and never on the face (v0.7)".

Nothing else in ENDPOINT or CONTRACTS moved. FWD-13's ACCEPT ("No 161867780096.00003 anywhere; every figure traceable to its
field") is unchanged.

## Review

- **It resolves the contradiction this seat raised** (slug @2d6a452375, section 3). The old DONE WHEN required a code on the tooltip
  face, which FWD-11 ("no raw code, id or storage path shows anywhere on the page") forbids. The new text puts the code in a DOM
  attribute. Attribute values are already outside the raw-code rule (row Z-W5-S1's reading).
- **The text matches the shipped build** (portal 24646bca, in PROD b3a1d8a6):
  - `StatTile.tsx:113-129`: FigureTooltip is headed by the plain label; `data-mnemonic` carries the code, never the face.
  - `HeaderCards.tsx:91-96` passes the mnemonic and `data-full-value: String(value)`.
  - Round 21's tipface reads 3 of 3; hoverprobe CODE is clean (BA 13 of 13, AMD 10 of 10).
  - Its comment at `HeaderCards.tsx:87` still says "its mnemonic and the served value". That is a stale code comment, not a
    ratified-text defect.
- **Traceability holds.** ACCEPT's "every figure traceable to its field" is met by the label in words plus `data-mnemonic`; the PM
  needs no code to read the figure.
- **Annotation inside the section:** "(v0.7)" is a version tag of the same form as the v0.6 tags (FWD-1 "(v0.6: ...)", FWD-2 "v0.6
  RESTATED"), which this seat signed at v0.6. No seat name or history was added inside ENDPOINT by this change.

**Verdict: SIGN.**

-- 3.0.0_SA_CVO~Z
