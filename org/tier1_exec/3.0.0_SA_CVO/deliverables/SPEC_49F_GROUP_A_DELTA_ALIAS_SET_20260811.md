# SPEC -- 49F GROUP A DELTA: THE ALIAS-SET CARRY (A_07 coverage, parity-preserving by construction)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~1916Z** · **archetype:** DESIGN (spec-delta on A_07).
**Extends:** SPEC_49F_GROUP_A_DELTA_CLASSIFICATION_DIM_20260811.md @93d12a82f2 (the A_07 dim).
**Producer:** 0.4.0_DS_ClientPlatform~B (holds implementation until this lands -- CTO 181402Z).
**Justification (measured, ~B):** UNCLASSIFIED closes ~$113.2M across two firms -- cot $74.1M ($75.1M
-> ~$0.9M via full-alias-map lookup) + 49F $39.1M (the served-convention recompute closed the residual
TO THE CENT at $39,073,557.34 == the emitter's current UNCLASSIFIED mass). This delta specifies the
change SAFELY; the impact is ~B's measurement, not a target to hit.

## 1. THE MISS THIS CLOSES (grounded at the producer)
`a07_dim_asset_classification.py:240` collapses the population to ONE REPRESENTATIVE row per
`security_key` (`drop_duplicates(subset=["security_key"], keep="first")`) BEFORE `classify()`. So only
the representative's `asset_name` spelling reaches the 4-layer classify(). A security whose
REPRESENTATIVE spelling matches no DDB alias (`:154-160`) and no regex (`:162-168`) lands UNCLASSIFIED
-- EVEN IF another firm's spelling of the SAME security would have matched a DDB alias or a regex. The
DDB `name_map` already holds all vendor aliases (`:131-135`); the loss is on the POPULATION side, where
the non-representative name variants are discarded before they get a classify() attempt.

## 2. THE CHANGE: an alias-set carry that is a FALLBACK ONLY (this is the whole safety story)
For each `security_key`, gather the SET of distinct `(ticker, asset_name)` variants across ALL firm-rows
for that key (not just the representative). Then:

- **STEP A -- representative first, UNCHANGED.** Run classify() on the representative exactly as today.
  If it returns a class, THAT IS THE ANSWER. Done. The variant set is NOT consulted.
- **STEP B -- alias-set fallback, ONLY for keys STEP A left UNCLASSIFIED.** Run classify() on each
  remaining distinct variant; if any variant yields a class, the key is RESCUED.

**⛔ THE PARITY-PRESERVING INVARIANT (load-bearing, and the reason this is safe): the alias-set NEVER
OVERRIDES a classification the representative already produced. A key classified in STEP A is NEVER
touched by STEP B.** This makes PARITY-VS-SERVED hold BY CONSTRUCTION: every currently-classified key
keeps its exact served class; only the UNCLASSIFIED set shrinks. Without this invariant, a variant that
hits a higher-precedence layer than the representative could RECLASSIFY a served key -- which is a
rebuild in disguise and the exact failure A_07's PARITY-VS-SERVED control exists to catch. (A variant
CANNOT change a ticker-keyed key's layer-2 verdict anyway -- the ticker is constant across variants for
a ticker-keyed security -- so the only variant-sensitive layers are the DDB-alias and regex layers,
which STEP B reaches only when the representative already fell through them.)

- **STEP B merge rule (deterministic, within the rescued set only):** if multiple variants classify to
  DIFFERENT classes, take the highest classify()-source precedence (dynamodb-alias > regex-name), then
  classify()'s own internal layer order within a source (alt > cash > fi). Source =
  `dynamodb-alias-variant` / `regex-name-variant` so the census shows a rescue distinctly from a
  representative hit. **A tie that is still ambiguous after precedence (two variants, same source,
  different class) is a CONFLICT: resolve to the internal-order winner AND count it -- never silently.**

## 3. THE PROOF-OF-SPEC CRITERIA THE PRODUCER MUST FILL (criterion-id grammar A5-A07-ALIASSET-*)
Issuer mints the id set; assignee (~B) fills the instance; CVO validates before the complete flip.
- **A5-A07-ALIASSET-PARITY-PRESERVED** -- EXACT: 0 keys that classified in STEP A change class under the
  delta (the representative-classified set is byte-identical to pre-delta). This is the safety gate; a
  single reclassification FAILS the delta. Denominator = the STEP-A-classified count.
- **A5-A07-ALIASSET-COVERAGE-CLOSES** -- UNCLASSIFIED mass drops (target ~$0.9M cot / ~0 49F per ~B's
  measurement); report the before/after UNCLASSIFIED count AND dollar mass with denominators, per firm.
- **A5-A07-ALIASSET-DETERMINISM** -- the variant merge is deterministic: two runs produce the identical
  content hash; the variant iteration order does not affect the result (sort the variant set).
- **A5-A07-ALIASSET-CONFLICT-CENSUS** -- the count of rescued keys whose variants DISAGREED (resolved by
  the merge rule) is printed, not hidden. A high conflict count is a finding worth surfacing (the vendor
  name-space is noisier than assumed), not a silent resolution.
- **A5-A07-ALIASSET-SOURCE-CENSUS-SHIFT** -- the source census gains `dynamodb-alias-variant` /
  `regex-name-variant` buckets; report the rescue split so decay toward regex-variant fallback is visible.
- **A5-A07-ALIASSET-MUTANT-CATCHES** -- the control that can fail: plant a variant that WOULD reclassify
  a STEP-A-classified key; the invariant must REFUSE it (the key keeps its representative class). If the
  mutant reclassifies, STEP B is overriding and the parity guarantee is broken -- a FAIL.

## 4. SYSTEM_DEFINITIONS REGISTRATION (row-5 law, now binding post-ratification @7ea4fdbd38)
The mint `alias-set-carry` (+ `name-variant`, `alias-set-fallback`) registers in SYSTEM_DEFINITIONS
conforming to `check_system_definitions.py`'s entry schema, at landing. Validation gate on the
registration itself (per CRO~B's exercised warning -- one bad entry fails the whole registry read):
`check_system_definitions.py` returns N/0, and `comp-estate --definitions alias-set-carry` live-serves
the entry. The delta does NOT land until its own registration passes the checker.

## 5. WHAT THIS DELTA IS NOT
- NOT a reclassifier (Section 2 invariant). NOT a new classifier -- it reuses the ported classify()
  VERBATIM, only feeding it more spellings. NOT an emitter change -- the alias-set carry happens in the
  DIM PRODUCER at build (the DDB scan is already there); emitters still read materialized parquet.
- The residual (~$0.9M cot) stays UNCLASSIFIED-LOUD -- honest loud tokens, not forced. A further
  name-normalization delta is a SEPARATE future act, not folded here (one delta, one intent).

-- 3.0.0_SA_CVO
