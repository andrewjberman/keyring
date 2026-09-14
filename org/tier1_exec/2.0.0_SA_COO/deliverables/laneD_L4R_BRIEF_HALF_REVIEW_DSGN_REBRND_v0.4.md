# L4-R BRIEF-HALF RE-REVIEW -- DSGN_REBRND PRD v0.4 @4ebd24684b (half hash c1bc0896e75a)

**Reviewer:** `2.0.0_SA_COO~D`, the designated brief-half signer. The designation is on the project row, by Andrew's word
@`2daf4d8b85`.
**Supersedes:** `laneD_L4R_BRIEF_HALF_REVIEW_DSGN_REBRND_v0.3.md`@`64dd54e67f`, SIGNED @`02c038df19` against
`364fa381f608`.
**Delivered by:** `1.0.0_SA_CTO`, msg 96642.
**Scope:** the delta. The instrument is a word-level diff of the PRD at `179884e46b` (v0.3) against `4ebd24684b` (v0.4),
line by line. That is a different instrument from the v0.3 review's hunk read. 249 -> 250 lines, 5 lines changed:

| line | section | half | change |
|---|---|---|---|
| 8 | header | (header) | `v0.3` -> `v0.4` |
| 48 | ENDPOINT, FWD-4 SOURCE | ratified-text | adds "Andrew-direct 2026-09-14 ~15:0xZ (the identity set; PROVENANCE v0.3)" |
| 109 | BRIEF COVERAGE, R5 | **brief** | inserts the single word `ACTION` |
| 122 | CONTRACTS preamble | ratified-text | the identity role classed DERIVED (`3.0.0_SA_CVO` R1) |
| 228 | PROVENANCE | **brief** | the new v0.4 entry |

So the brief half moved in exactly two places. Everything else in it is byte-identical to the v0.3 bytes signed
@`02c038df19`.

## VERDICT: SIGN

## 1 -- R5 `:109` is this seat's correction, verbatim, and nothing more

- The word diff shows ONE insertion, `ACTION`. So the clause now reads "...and the persistent ACTION count stays one".
- That is exactly the correction the v0.3 review returned by pinned line (review @64dd54e67f section 4; msg 96639,
  READ by `1.0.0_SA_CTO` at 17:10:38Z).
- It now matches FWD-4's PROOF ("the persistent ACTION count stays one") and the reopened order's `RB5-AC6`.
- No other word in the row moved. The closed identity set signed at v0.3 is unchanged.

## 2 -- The v0.4 provenance entry is accurate

Each claim in the entry was checked against its source:
- It cites `3.0.0_SA_CVO`'s refusal by path, and states R1 as that review states it: `:122` classed "the accent's two
  roles" as MEASURED, and the measured website carries exactly two.
- It records the remedy the CVO recommended, the identity role classed DERIVED with its rule beside it. The diff shows
  that at `:122`.
- It records N1 taken. The diff shows that at `:48`.
- It cites this seat's review as msg 96639. `get_delivery_state(96639)` reads `2.0.0_SA_COO~D -> 1.0.0_SA_CTO`, subject
  "DSGN_REBRND v0.3 brief half SIGNED @02c038df19; one-word R5 correction", READ. The citation resolves.

## 3 -- The heading denominator is unchanged

`brief_ref` is still `docs/briefs/portal-visual-elevation-brief-20260911.md@bed01b226a`, and no BRIEF COVERAGE row was
added or removed (R5 was edited in place).

## NOT CLAIMED

- **The ratified-text half** (`:48`, `:122`). It is `3.0.0_SA_CVO`'s.
- **That the built `portal/DESIGN.md` classes the identity accents DERIVED.** It lives on the feature branch, where
  worker `0.9.0_WK_DSGN_REBRND~2` is rewriting clause C8 now. It is checked at that order's issuer re-grade, and is
  not a question for this half.
