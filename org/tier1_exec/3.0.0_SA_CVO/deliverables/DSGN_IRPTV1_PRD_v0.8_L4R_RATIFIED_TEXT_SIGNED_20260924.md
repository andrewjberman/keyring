# L4-R review -- DSGN_IRPTV1 PRD v0.8, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`31a61d0466` (v0.8). **Half:** ratified-text,
`half_hash` `9f2702c16e62`, ENDPOINT hash `0193ebd965d7`, both re-measured with `prd_signoff_lib` at the pin and
matching delivery 100926. **Prior:** REFUSED at v0.7, review
`DSGN_IRPTV1_PRD_v0.7_L4R_RATIFIED_TEXT_REVIEW_20260924.md` @`12b89b8dd4`, stamp @`0bcd1f9437`.

**Verdict: SIGN.** The bump changes exactly the clauses the refusal named. Everything else in the half is the v0.7
text that the refusal already checked clean.

## What changed (`git diff -U0 8942931687 31a61d0466` on the PRD)

- **R1, CLOSED.**
  - FWD-5 :89-90 now reads "method and lineage sit behind the panel's help tip, and the bottom bar carries only the
    source and the time".
  - FWD-6 :99-100 now reads "basis, denominator and provenance sit behind the panel's help tip, not in the bottom
    bar".
  - Both now agree with FWD-18 and with Andrew's P:26-28.
- **R2, CLOSED.** FWD-7 :107 now reads "the variant step is three cards". FWD-8's upload-first step for a prospect
  now stands alone.
- **Other bytes:** the header `prd_version` and one history line. No other line of the ENDPOINT or CONTRACTS section
  changed.

## Observations (not blocking; for the next ENDPOINT bump, not a re-open)

- FWD-5 and FWD-6 now end with "(v0.8, FWD-18)" inside the ACCEPT line. It is a cross-reference and does not change
  what a grader tests. Its proper place is the SOURCE line, since the spine keeps history out of the section.
- CONTRACTS :245 still lists the disclosure surfaces as "(footer line, popover, Details)". My v0.7 review asked
  for "help tip" in that list. It is outside the ENDPOINT hash, and "popover" already covers a help tip, so no L9
  object is lost.

## Instruments

| question | instrument | result |
|---|---|---|
| half and ENDPOINT hash at the pin | `prd_signoff_lib.half_hashes()`, `endpoint_hash()` on `git show 31a61d0466:<prd>` | `9f2702c16e62`, `0193ebd965d7`; match the delivery |
| what changed v0.7 -> v0.8 | `git diff -U0 8942931687 31a61d0466` on the PRD | 4 hunks: header version, FWD-5, FWD-6, FWD-7; plus the history line |

-- `3.0.0_SA_CVO`, 2026-09-24 ~23:0xZ
