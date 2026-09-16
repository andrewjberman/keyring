# L4-R BRIEF-HALF RE-REVIEW -- DSGN_REBRND PRD v0.5 @01378b0a5b (half hash 2ff743682880)

**Reviewer:** `2.0.0_SA_COO~D`, the designated brief-half signer. The designation is on the project row, by Andrew's word
@`2daf4d8b85`.
**Supersedes:** `laneD_L4R_BRIEF_HALF_REVIEW_DSGN_REBRND_v0.4.md`@`dbde53ad1c`, SIGNED @`382ecbef8b` against
`c1bc0896e75a`.
**Delivered by:** `1.0.0_SA_CTO`, msgs 96654 and 96656.

**The pin is the HEAD of the path, not the delivered commit.**
- The request (96654) named `40d6e992c9`, with half hash `08a38fbb5d9b`.
- Its successor `01378b0a5b` (provenance only, "10 of 10" -> "9 of 9") landed at 17:36Z, before this review began.
- Computed with `prd_signoff_lib.half_hashes` itself:

| read | brief half hash |
|---|---|
| the working copy | `2ff743682880` |
| HEAD | `2ff743682880` |
| `40d6e992c9` | `08a38fbb5d9b` |

This review covers `2ff743682880`, and the stamp binds it with `--expect-half-hash`. 96656 confirms that one re-sign
covers both commits.

**Scope:** the delta from the bytes signed at v0.4. The instrument is a word-level diff, v0.4 `4ebd24684b` -> v0.5
`40d6e992c9` -> `01378b0a5b`:

| line | section | half | change |
|---|---|---|---|
| 8 | header | (header) | `v0.4` -> `v0.5` |
| 122 | CONTRACTS preamble | ratified-text | the selection highlight moved MEASURED -> DERIVED (`3.0.0_SA_CVO` R2) |
| 229 | PROVENANCE | **brief** | the new v0.5 entry, and the count in it corrected at `01378b0a5b` |

So the brief half moved in ONE place: the v0.5 provenance entry.

## VERDICT: SIGN

## 1 -- Every claim in the v0.5 provenance entry was checked

- **R2, as stated in the refusal.** The entry says v0.4's MEASURED "transient roles" covered the focus ring and the
  selection highlight, and the website carries only the ring. That matches
  `PRD_REVIEW_DSGN_REBRND_v0.4_RATIFIED_TEXT_HALF_20260914.md`, R2.
- **The absence check.** The entry says "selection" matches 0 lines over `design/brand/opalinvest.com.{json,md}`,
  against 10 for "focus". I re-derived it with a different instrument, a native Grep, case-insensitive, over both
  files: "selection" 0; "focus" 10 lines (`.md:18,48,53,54,75,131`; `.json:14,56,57,76,107`). That confirms it.
- **The count, "9 of 9".** The CVO's census had ten rows, one of them the selection highlight. Ten less the highlight
  leaves nine, and `01378b0a5b` corrects the entry from "10 of 10" to "9 of 9" with that reason. It is correct, and
  it agrees with 96656's full listing of MEASURED (9 members).
- **"The same gap was in v0.2's text."** The CVO's review says this about its own v0.2 signature.

## 2 -- Nothing else in the half moved

R5 still reads "the persistent ACTION count stays one", unchanged from v0.4. The BRIEF COVERAGE table is unchanged,
and `brief_ref` is unchanged at `bed01b226a`. So the heading denominator still matches.

## NOT CLAIMED

- **The ratified-text half** (`:122`). It is `3.0.0_SA_CVO`'s.
- **That the built `portal/DESIGN.md` carries the class labels the CONTRACTS clause asks for.** A case-insensitive
  read of the drained RB-s-5 tree finds no "derived" in it anywhere. That is a gap in the contract as RB-s-7 built it,
  not in this half, and it is carried to the drain-end read for L9 (FWD-6).
