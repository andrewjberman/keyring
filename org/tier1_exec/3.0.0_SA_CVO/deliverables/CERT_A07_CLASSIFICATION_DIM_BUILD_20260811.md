# RULE-14e CERTIFICATION -- A_07 asset-classification dim BUILD (the first spec-delta built to a CVO spec)

**Certifier:** 3.0.0_SA_CVO · **2026-08-11 ~1815Z** · **archetype:** VALIDATE
**Subject:** PROOF_OF_SPEC_A07_CLASSIFICATION_DIM_20260811.json @c998ff19db (6 rows VALID) against
the A_07 spec-delta @93d12a82f2 (my own spec). Built by 0.4.0_DS_ClientPlatform~B.
**Method:** structural VALID + the PARITY-VS-SERVED control RE-RUN ADVERSARIALLY at source, not
accepted from the instance's own claim.

## VERDICT: CERTIFIED. The port is faithful BY INDEPENDENT RE-DERIVATION, not by self-report.

## THE PARITY-VS-SERVED CONTROL -- re-run at source (the row I designed to catch a reclassifying port)
The instance claims 3784/3784 agree with the original lib, 0 mismatches. I did NOT accept that -- I
re-derived it: compared the ported `a07_dim_asset_classification.py:classify()` against the ORIGINAL
`data/black_diamond/scripts/gold/lib/etf_classifier.py` at the level that determines every
classification:
- **The three regex families, compiled-object comparison** (`.pattern`, positive-controlled): `_RE_ALT`
  IDENTICAL (118/118 chars) · `_RE_CASH` IDENTICAL (69/69) · `_RE_FI` IDENTICAL (260/260).
- **The classify() layering** (the ordered class-precedence that decides ties): IDENTICAL 7-element
  sequence [fixed_income(override), alt, alt, alt, fixed_income, fixed_income, equity].
- **Behavioral battery** on the pure-regex path (empty DDB maps): alt->alternatives, cash-family->
  fixed_income (the lib's own cash-under-FI convention, faithfully reproduced), coupon+maturity->
  fixed_income, plain equity->equity, CASH_USD override->fixed_income. All correct.
**CONTROL DISCIPLINE NOTE (on the record):** my FIRST diff attempt used a text-scrape that returned
`None` for the lib's `_RE_FI` (its inline comment broke my capture) and reported "DIFFERS" -- a
retrieval-returns-a-value false positive, the exact class I have policed all session. I caught it on
the positive control (a nonzero length proves extraction ran) and re-derived on the compiled objects.
The port is faithful; the first "difference" was my instrument, not the port. A ported classifier that
secretly reclassified is exactly what this control exists to catch -- it did not, verified two ways.

## THE OTHER FIVE ROWS
- COVERAGE: 3,378/3,784 classified (89.27%), 406 UNCLASSIFIED-LOUD (0 silent nulls) -- the loud-token
  discipline held; population = the UNION across firms (the spec's union requirement met).
- NO-EMITTER-DYNAMODB: 0 D-group emitter files touch ETFClassifier/dynamodb across 3 runner trees --
  the coupling this delta exists to remove is removed BY CONSTRUCTION (mechanically asserted); the
  DDB scan is the ONE sanctioned build-time materialization (9,393 items).
- SOURCE-CENSUS: dynamodb-ticker 2126 / regex-name 1131 / dynamodb-alias 121 / unclassified 406 --
  the decay-visibility census present (a shift toward regex-fallback would be visible, not silent).
- DETERMINISM + PROVENANCE: PASS.

## COVERAGE STEP-ZERO
6 instance rows == the A5-A07 battery I wrote (ROWCOUNT folded into COVERAGE, PARITY-VS-SERVED,
NO-EMITTER-DYNAMODB, SOURCE-CENSUS, DETERMINISM, PROVENANCE); no battery criterion omitted, no
unexpected addition. Coverage clean.

## CARRIED (not cert blockers, routed)
The 406 UNCLASSIFIED (10.7%) is honest loud-tokened, not a silent gap -- but the ~B mix_summary
overlay's $75.1M UNCLASSIFIED-fold + the name-variants spec-delta candidate (CTO 181402Z) address
exactly this population; that delta is a FUTURE A_07 amendment (carry ALL name variants per security
key), queued at my discretion -- it does not block THIS cert (the built dim is faithful and its
uncovered rows are loud). The cot three-way class-split INFERRED divergence ($24.5M alternatives, a
possible diverged legacy classifier copy) is ~B's one-source-read characterization in flight -- a
COT-cutover sovereign-row candidate, not an A_07 build defect.

-- 3.0.0_SA_CVO
