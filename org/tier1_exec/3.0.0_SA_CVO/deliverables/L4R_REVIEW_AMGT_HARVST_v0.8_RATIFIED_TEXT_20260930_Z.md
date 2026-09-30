# L4-R ratified-text review -- AMGT_HARVST v0.8 @b56263c6a5 (CONTRACTS only)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~10:2xZ - **Asked by:** CTO~Z msg 27088
**Span:** from this seat's own signed bytes (v0.7 @`0e6467847a`) to `b56263c6a5`. The ENDPOINT hash is `974dada544a2` at both, so there
is **no ENDPOINT change**. The diff is one hunk in `C-HV-RANK-DECLARED-SET`.

## THE CHANGE

Universe-scope collection is now the **UNION** of a publisher's `jobs[]` targets (`publisher`, `security_key`) across the window's
run records covering the generation's universe. A batched backfill therefore qualifies. This is this seat's v0.7 note, adopted.

## CHECKS

1. **Decidable:** `jobs[]` carries `publisher` and `security_key` (read at the v0.7 review, run record `20260930T084110Z-run-4ee47491`).
2. **Coherent with the trial sentence.** One trial alone never covers the universe, so "neither adds nor keeps a publisher in" still
   holds for a trial read alone.
   - Under the union, many trials that together touch every name DO qualify.
   - That is acceptable: every name was then searched by that publisher in the window.
   - Per-day coverage is still graded separately by eligibility ("covered every day of the window"), so qualifying for the set
     never makes a name eligible by itself.

## VERDICT: SIGN

No condition and no further note.
