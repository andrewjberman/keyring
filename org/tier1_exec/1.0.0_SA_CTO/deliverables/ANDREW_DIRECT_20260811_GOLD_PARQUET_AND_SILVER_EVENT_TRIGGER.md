# ANDREW-DIRECT — Option A confirmed; GOLD-AS-PARQUET + the silver-completeness event trigger (the three coverage requirements)

**Channel:** Andrew-direct at the 1.0.0_SA_CTO terminal, 2026-08-11 ~0757Z (the thing he held the
wrap-up to show). **Recorded by:** 1.0.0_SA_CTO same turn. **Broadcast:** COO + CVO + CRO base +
CRO~A + CRO~B + MSTR + DS.

## VERBATIM

> "Option A confirmed, that is what I wanted to show you, the gold parquet approach as opposed to
> gold in json. That is a crucial aspect of the advi pipeline because it is an output change, but I
> think it is very positive overall. The only thing we would need to bring in as well is an
> event-based trigger where once all necessary silver tables appear it triggers the gold ec2
> runner for the given firm. that needs to be covered and the fact that the final output of gold
> runner is parquet needs to be covered, in addition to the fact that any portal publisher to
> platinum would need to be reading parquet not json."

## THE THREE COVERAGE REQUIREMENTS (each landed as a ruled amendment to the FINAL-ratified set)

1. **THE SILVER-COMPLETENESS EVENT TRIGGER (per firm):** when ALL NECESSARY silver tables for a
   firm appear, the gold EC2 runner for that firm fires. Composes with the ratified Group W
   doctrine — the event is the ACCELERATOR and is now REQUIRED (not optional); the clock floor
   remains beneath it (event-only stays prohibited — the mdpf/INF starvation class); the
   completeness PREDICATE is declared per firm (the necessary-table set, a single-homed
   definition), and the L2 no-data-day contract governs its calendar behavior (a non-trading day
   correctly never fires; the floor's catch-up detection covers a trading day whose silver never
   lands).
2. **GOLD RUNNER FINAL OUTPUT = PARQUET.** The gold tier is parquet by law —
   `portal/gold/{product}/{scope}/{table}/date={D}/` parquet, mirroring silver's queryable
   grammar (CRO's refactor spec form, now Andrew-confirmed). JSON leaves the gold tier entirely.
3. **EVERY PORTAL PUBLISHER TO PLATINUM READS PARQUET, NOT JSON.** The publisher becomes the ONLY
   JSON producer in the estate — serving-shape JSON is minted exactly once, at the platinum
   boundary, from parquet gold. The D-group frozen-shape census contract is UNCHANGED (the served
   bytes never move); what changes is the emitter/publisher INPUT plane. The one-producer-per-
   served-key law becomes enforceable BY CONSTRUCTION (nothing else emits JSON at all).

## COMPOSITION NOTES (so the amendments land without re-opening the reviews)

- The A/B/C specs already carry parquet artifact grammars — requirement 2 makes it LAW-EXPLICIT
  rather than convention. The D spec's emitters re-read as PUBLISHERS (parquet in, frozen JSON
  out) — CVO folds the input-format cell (their own flagged hook) + the W trigger row.
- The M7 gold-input format flip × the in-flight wo2 publisher repoint remain ONE ORDERED ACT
  through the CTO arch gate (CVO amendment 1, unchanged by this ruling).
- Rule 17b gains its one-line amendment (the ~0754Z + ~0757Z authority): the `portal/` gold
  subtree is the ratified product-gold home, parquet-serialized; vendor trees keep bronze+silver;
  platinum serving unchanged.
