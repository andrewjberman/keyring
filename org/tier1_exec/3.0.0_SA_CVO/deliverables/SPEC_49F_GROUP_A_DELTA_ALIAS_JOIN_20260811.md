# SPEC -- 49F GROUP A DELTA: THE JOINABLE ALIAS SURFACE (the ACTUAL $113.2M closer -- join layer)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~1954Z** · **archetype:** DESIGN (spec-delta on A_07, join layer).
**Supersedes the coverage intent of** SPEC_49F_GROUP_A_DELTA_ALIAS_SET @23f23ea039 (which correctly
closes DIM-CLASSIFICATION coverage but STRUCTURALLY CANNOT close the join mass -- grounded by ~B's d08
re-run @6355392782, cot fold unchanged at $75,094,285.23). **Producer:** 0.4.0_DS_ClientPlatform~B
(holds implementation until this lands). **Justification:** the $113.2M ($74.1M cot + $39.1M 49F) that
the classification delta did NOT close -- because it was a CONSUMER-JOIN mass all along.

## 1. THE MECHANISM (grounded, ~B's characterization + my dim-producer read)
Consumers join book rows to the A_07 dim through n_maps built from the dim's CARRIED REPRESENTATIVE
name only (the `rep` collapse at a07_dim_asset_classification.py:240). A book row whose name variant
differs from the representative's spelling MISSES THE JOIN entirely -- so its value is unclassified AT
THE CONSUMER regardless of how the dim classified that security_key. The classification delta feeds
more spellings to classify() (dim-side); it does NOT change what the dim CARRIES for consumers to join
on. So the join mass stays open.

## 2. THE CHANGE: the dim EMITS a joinable alias/variant surface
The A_07 dim emits an ALIAS-KEY-EXPANSION surface: for each security_key, one row PER distinct name
variant (the DDB alias set UNION the population variants), each mapping `normalize_name(variant) ->
security_key + asset_class + classification_source`. Consumers build their n_maps from THIS surface, so
ANY variant spelling in a book row joins to the correct security_key and class WITHOUT the consumer
touching DDB (the A5-A07 no-emitter-DDB law holds -- the expansion is built once, in the dim producer,
at build time, from the same materialized DDB scan already there).

## 3. THE PARITY-PRESERVING INVARIANT (again load-bearing)
⛔ **The expansion adds JOIN COVERAGE ONLY; it NEVER re-maps a row that already joined.** A
`normalize_name(variant)` that ALREADY resolves to a security_key keeps that resolution; the expansion
only adds resolutions for previously-UNjoined variants. So every already-joined book row keeps its exact
served key and class -- JOIN-PARITY holds by construction. A variant that would re-map an
already-joined name to a DIFFERENT key is a CONFLICT (two securities claiming one spelling): resolve by
the dim's own security_key precedence, COUNT it, never silently overwrite.

## 4. PROOF-OF-SPEC CRITERIA (A5-A07-ALIASJOIN-*)
- **A5-A07-ALIASJOIN-COVERAGE-CLOSES** -- the CONSUMER-JOIN unjoined mass drops from $113.2M toward
  residual; MEASURED by re-running the ACTUAL CONSUMER (d08 cot fold $75.09M -> target; 49F $39.1M ->
  target), before/after, per firm, with denominators. This is the criterion the classification delta's
  COVERAGE row should have been -- measured at the consumer, not the dim.
- **A5-A07-ALIASJOIN-PARITY-PRESERVED** -- EXACT: 0 already-joined book rows change security_key or
  class under the expansion (the safety gate; a single re-map FAILS). Denominator = the pre-expansion
  joined-row count.
- **A5-A07-ALIASJOIN-NO-CONSUMER-DDB** -- consumers read the emitted expansion surface, never DDB
  (mechanically asserted, --qa-consumer-grep, the A5-A07 law one layer up).
- **A5-A07-ALIASJOIN-CONFLICT-CENSUS** -- variants mapping to 2+ security_keys, counted not hidden.
- **A5-A07-ALIASJOIN-DETERMINISM** -- sorted expansion, two runs identical hash.
- **A5-A07-ALIASJOIN-MUTANT-CATCHES** -- plant a variant that would re-map an already-joined row; the
  invariant must REFUSE it. If it re-maps, the expansion is overriding a live join -> FAIL. AND: plant a
  book row with a known unjoined variant; the expansion must now JOIN it (the coverage teeth, positive).

## 5. SYSTEM_DEFINITIONS mint
`alias_key_expansion` (the emitted joinable surface) registers per the row-5 law, conforming to
check_system_definitions.py (N/0), comp-estate live-serve verified, at landing.

## 6. WHY TWO DELTAS, NOT ONE (the layer discipline)
The classification delta (@23f23ea039) closes CLASSIFICATION coverage (a key gets a class); this closes
JOIN coverage (a book row reaches its key). Different intents, different layers, different consumers --
one delta each (the Rule-24 one-intent-per-axis discipline applied to deltas). The classification delta
lands narrow (2 keys); this is where the $113.2M actually closes.

-- 3.0.0_SA_CVO
