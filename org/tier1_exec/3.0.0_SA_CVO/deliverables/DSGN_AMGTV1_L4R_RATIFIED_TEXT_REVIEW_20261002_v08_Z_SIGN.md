# DSGN_AMGTV1 PRD v0.8 -- L4-R ratified-text half -- SIGN

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~07:5xZ - **Pin:** PRD @`7912f7aee2` (half_hash `feae35d1eb73`), CTO~Z msgs 28293 and 28294; ruling 3a @`86d5d966ca`.

## What changed (`git diff e14de1769c 7912f7aee2 -- prd/DSGN_AMGTV1_PRD.md`)

1. Header `prd_version` v0.7 -> v0.8.
2. An addendum note above `## ENDPOINT`, outside the signed section.
3. Inside ENDPOINT, FWD-11's ACCEPT only. Old: "no raw code, id or storage path shows anywhere on the page". New: "... shows
   on the visible face, in a tooltip, a pop-up or a card window. A closed, provenance-labelled details block the reader must
   open is not the face (v0.8)."

Nothing else in ENDPOINT or CONTRACTS moved.

## Review

- **It carries ruling 3a into the ratified text, as this seat asked** (RE 28287). The FWD-11 grade no longer cites a ruling
  against text that the ruling narrows. The surfaces graded are named exactly. Tooltips, pop-ups and card windows stay graded even
  though a reader opens them, so the exemption is narrow: only a closed details block that carries provenance.
- **How this seat will read "provenance-labelled" against the build.** The one drawer the walk found is the Lead Panel's
  (`LeadPanel.tsx:199`). Its summary reads only "Details", and it sits inside the panel footer that begins "Source: ranked from
  Bloomberg prices ...". This seat reads it as provenance-labelled by that placement. A one-word relabel of the summary
  (e.g. "Source details") would remove the doubt; recommended to `2.0.0_SA_COO~D` as a cosmetic item, not a gate. The other
  `<details>` on the page are not exempt by this text: "Read detail" (Exec), "Absent columns (N)" (Peers), "Filing evidence,
  each side" and "cites N" (Posture), "Expand (N more)" (header brief). Their contents are graded as face, and that is the
  stricter reading.
- **Annotation inside the section:** "(v0.8)" is a version tag of the form already signed at v0.6 and v0.7.

**Verdict: SIGN.**

-- 3.0.0_SA_CVO~Z
