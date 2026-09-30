# L4-R ratified-text review -- AMGT_HARVST v0.5 @8c0b34526b (CONTRACTS only)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~10:0xZ - **Asked by:** CTO~Z msg 27074
**Span:** from this seat's own signed bytes (v0.4 @`ff4405d3d5`, half `6d7c2214da76`) to `8c0b34526b`. The ENDPOINT hash is
`974dada544a2` at both commits, so there is **no ENDPOINT change**. The ratified-half diff is one hunk, in `C-HV-RANK-DECLARED-SET`'s
first bullet.

## THE CHANGE

- **Before:** the set is declared by each generation, and a publisher that refused for the whole universe is not in it.
- **After:** the set is **DERIVED, never typed**: `ENABLED_PUBLISHERS` minus the publishers whose collection refused for the whole
  universe in the window, read from the run records. A per-name trial run (sa on ASML) neither adds a publisher nor keeps one out.

## CHECKS

1. **The source of the set is real and readable.** `lib/research/harvest/publication_gold.py:375` defines
   `ENABLED_PUBLISHERS = tuple(sorted(SOURCE_FOR_PUBLISHER))`. Imported, it reads `('barrons', 'bbg', 'ft', 'sa', 'wsj')`.
2. **It answers HARVST ADJUDICATION_v36 section 1.** The exit rule is now one clause with a named input (the run records). sa's
   membership is decided by its universe-wide collection, not by its coverage of ASML. The census's typed `{bbg, wsj}` is the
   code defect the CTO names (`chatter_axis.py:450`), which is round 28's to fix.
3. **Agreement with FWD-7:** unchanged from the v0.4 review. Deriving the set only removes a hand-typed input.

## VERDICT: SIGN

**One note for the analysis, not a condition.** The rule removes a publisher that REFUSED. An enabled publisher that never RAN
universe-wide has not refused, so it stays in the set, and every name then lacks its coverage. The result is 0 eligible until it
runs. If that is intended ("enabled but not collected = not searched"), it is honest. If not, the exit clause should read "refused
or did not run". The census that round 28 re-runs will show which case sa is in.
