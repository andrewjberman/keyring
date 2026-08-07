# §B1 second-amendment exercise record — `absent_to_null_only` proven both directions

**Run:** 2026-08-07 00:46Z by `3.0.0_SA_CVO~Z` · amendment @6c50710af (Andrew-direct via CTO~Z,
verbatim relayed: *"yeah no carve outs thats waste of time, we're trying to avoid extra patchy
nonsense code"*) · routed by COO~Z 004315Z

**What changed:** `basis`/`source` at GLOBAL = `null` (honest absence under one schema); the composite
requirement is STRUCK. Named transition: `absent→null`. Firm scopes unchanged (real values, no exemption).

**Encoding decision, stated so it is visible:** the exemption class is `absent_to_null_only`, NOT the
broad `absent_to_present` — a broad class would silently excuse an off-contract composite emission at
exactly the path Andrew just ruled null. Narrow-as-named is the fail-closed reading of the amendment.

## A4 — positive control (the contract transition is excused)

Candidate = pinned global account-distribution body (`Pka1VcXTAS8sOAV3`) + `basis: null, source: null`:

```
EXCUSED-ONLY: global/account-distribution  paths_compared=623 diffs=2 excused=2 regressions=0
DENOMINATOR: 1 of 1 pairs compared; total regressions=0; CITABLE
```

## A5 — mutant (the STRUCK requirement is mechanically rejected)

Same body + `basis: "composite(49financial+inflection+cottonwood)", source: null`:

```
REGRESSIONS(1): global/account-distribution  paths_compared=623 diffs=2 excused=1 regressions=1
  REGRESSION basis: ABSENT -> STRING  baseline=<absent> candidate="composite(49financial+inflection+cottonwood)"
DENOMINATOR: 1 of 1 pairs compared; total regressions=1; CITABLE
```

Same candidate carries both cases at once: `source: null` excused beside `basis: composite` rejected —
the class discriminates per path, not per file.

## Two instrument notes from this exercise, on the record

1. **COULD-NOT-VERIFY hardening:** the first A4 attempt could not find its candidate (my own
   MSYS-path-into-native-Python error writing to a phantom `C:\c\...` tree) and the comparator
   correctly reported COULD-NOT-VERIFY — but exited rc=0. That invites a downstream reader to treat a
   not-run comparison as clean. Hardened: `could_not_verify > 0` now exits rc=3, never 0.
2. The `+DIRTY` suffix on the derivation-commit citation in these runs is the instrument telling the
   truth mid-re-derivation (list edited, not yet committed); the commit landing after this record makes
   the next run's citation clean.

— 3.0.0_SA_CVO
