# VALIDATION VERDICT -- A_07 alias-set delta implementation @6355392782 (+ my spec's layer finding, owned)

**Validator:** 3.0.0_SA_CVO · **2026-08-11 ~1952Z** · **archetype:** VALIDATE
**Subject:** ~B's implementation @6355392782 of SPEC_49F_GROUP_A_DELTA_ALIAS_SET @23f23ea039 (mine).
**Verdict: the IMPLEMENTATION is VALID. My SPEC under-specified the LAYER -- I own that, ~B's build exposed it.**

## THE SAFETY CONTROLS ALL FIRE (the implementation is correct and safe)
- **PARITY-PRESERVED:** the mutant (a planted reclassifying variant on STEP-A key '01179R4F7') is
  REFUSED -- never consulted, because STEP B iterates ONLY the STEP-A-unclassified set. The invariant I
  designed holds STRUCTURALLY, not by check. Full parity control still 3,784/3,784.
- **CONFLICT-CENSUS 0 · DETERMINISM** hash stable across 2 runs · **SOURCE-CENSUS-SHIFT** +2
  dynamodb-alias-variant. All the safety machinery works.

## COVERAGE-CLOSES: A GROUNDED FINDING, exactly per the spec's "if it lands at a different number, report it"
The delta rescued TWO keys (406 -> 404 UNCLASSIFIED), NOT the $113.2M. ~B did NOT stop at "the number
didn't close" -- they GROUNDED the mechanism: **the $113.2M lives at the CONSUMER-JOIN layer, not
dim-side classification.** Book rows join the dim through n_maps built from the dim's CARRIED
representative name only; a book row whose name variant differs from the rep-name misses the JOIN
entirely, regardless of how the dim classified that key. PROOF: d08 re-run against the delta dim -- the
cot fold is UNCHANGED at $75,094,285.23. A dim-side CLASSIFICATION fallback structurally cannot fix a
JOIN. STEP B correctly rescued the only 2 keys where a population variant reached an unclassified rep.

## I OWN THE SPEC DEFECT (the profile-the-mechanism / unread-basis discipline, on myself)
My COVERAGE-CLOSES criterion assumed the $113.2M was a CLASSIFICATION-COVERAGE mass. It is a
CONSUMER-JOIN mass. The $113.2M number was a consumer-join measurement all along (both firm figures);
my spec mis-attributed the LAYER, and the mechanism was a HYPOTHESIS I did not ground before writing the
criterion. ~B's implementation is the control that caught my spec -- the right direction (build validates
spec). This is the same class as every finding I have policed this session, turned on my own deliverable.

## DISPOSITION (my ruling)
- **The dim-side delta LANDS, narrow.** It is correct + safe, rescues 2 genuine keys, and establishes
  the alias-set-carry vocabulary (mints registered @da501bf2a7 -- see the registration note below). Its
  COVERAGE claim RE-SCOPES: it closes DIM-CLASSIFICATION coverage (2 keys), NEVER the $113.2M.
- **The $113.2M is a SEPARATE JOIN delta** (the dim carries a JOINABLE alias/variant key surface so
  consumer n_maps cover the alias space without touching DDB). One delta, one intent, one layer -- I spec
  it (SPEC_49F_GROUP_A_DELTA_ALIAS_JOIN); ~B's $113.2M bound transfers to IT intact. ~B holds
  implementation of the join delta until it lands (correctly did not widen).
- **The COVERAGE-CLOSES instance row lands PASS-WITH-FINDING at 2 keys** -- the delta did what a dim-side
  fallback CAN do, and the mechanism for the rest is grounded, not hand-waved.

## REGISTRATION NOTE (a finding of its own, caught + fixed)
~B's tooling STAGED a yaml.dump ROUND-TRIP of SYSTEM_DEFINITIONS that STRIPPED THE HEADER COMMENT BLOCK
(the FORM doc, the status-enum vocabulary incl. 'homeless', the Andrew-direct UNDERSCORES-NEVER-DASHES
rule) -- and the checker passed it GREEN 63/0, because the checker validates ENTRY schema, not header
comments (necessary-not-sufficient). I refused that commit, restored my ontology home to HEAD (comments
intact), and PURE-APPENDED the 3 mints (0 deletions, 63/0, comp-estate live-serve verified) @da501bf2a7.
The mint CONTENT was ~B's and accurate; only the re-serialization was destructive. Lesson banked: never
commit a checker-green whole-file re-serialization of a commented canon.

-- 3.0.0_SA_CVO
