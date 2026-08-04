# ANDREW DESIGN DISCUSSION -- G(N) tool-grain schema threaded onto the C0-C4 ontology (CVO assessment)

**Channel:** direct at the 3.0.0_SA_CVO terminal (in-session). **Time:** 2026-08-04 ~14:1xZ.
**Status:** DISCUSSION -- Andrew asked for CVO's position; nothing ruled yet. Feeds CTO's
two-grain PRD as a premise-under-discussion.

## Verbatim (Andrew)

> "I think we basically break down several types of grains here with the intent of tracking our
> C4 C3 C2 C1 C0 ontological schema. We need to perhaps consider first what our G(N) layout can
> be abstractly. Clearly there is filesystem trace level, and filecontent trace level, in terms
> of dependency/relational views. we could make filesystem trace G1, as a mirror for C1 in terms
> of interactions broadly, and G0 of filecontent (e.g. script io) as the C0 node fact proxy. The
> question then becomes, do we have comp-tools that would be G2 G3 G4, e.g. maybe comp-estate is
> G4, as a function of semantics. I just want to make sure we have a defined ruleset and very
> tight system and classification here. Please discuss, I want to know what you think on the
> subject,as we need to idenitfy how to thread ontology here for coherence sake."

## Grounding (read before opining)

Canon ladder quoted live from `comp-estate --layers` (STABLE CANON v1.3, Andrew-ratified
2026-07-30): C4 SEGMENTS (5, legislated) / C3 dual partition (C3.i 14 discovered structures,
C3.ii 27 declared verticals) / C2 MOTIFS (12, discovered, recurrence>=2) / C1 INTERACTIONS
(~40k edges, 10 relations) / C0 FACTS (~20k role-typed nodes). Between rungs: D1 value-grain
(C0-C1), D2 path-flow (C1-C2; "a chain is a D2 instance"), D3 contract (C2-C3). Invariant pair:
C2+C3.i discovered-never-declared; C3.ii+C4 declared-never-discovered.

## CVO position (summary; full argument delivered in-session)

1. **G0/G1 anchoring: AGREE, principled, with one refinement.** G-coordinates must classify the
   ANSWER SUBJECT (what one output row is ABOUT), never the implementation or data source --
   and for multi-mode instruments they attach PER MODE, not per binary.
2. **G(N) should INDEX INTO the existing ontology, not mirror it.** A parallel G-ladder that
   approximates C is a second vocabulary that drifts; the coherence move is G(N) := C(N)
   subject-anchoring BY DEFINITION, one authority file, no separate G definitions to maintain.
3. **The D-rails are the fork the sketch has not yet decided.** Chains/freshness/contract tools
   (comp-dispatch, comp-chainrun, comp-freshness, comp-validate, comp-drift) answer about
   D-objects, not C-objects -- per canon a chain is a D2 INSTANCE. Coordinate tuple should
   allow G in {G0..G4} XOR D in {D1..D3}.
4. **comp-estate is not "a G4 tool" -- it is the ladder-spanning world-model reader**: --segments
   = C4, <thread> = C3.ii, --matrix = C3 reconciliation, key-derivation = C0-adjacent. Andrew's
   semantic instinct is right; the refinement is per-mode coordinates.
5. **The intra-file axis already exists**: the CONTAINS ladder (container->file->function->
   statement->field) + the stage-2 grain enum (field/artifact/...). G0 ~= {function/statement/
   field} subjects, G1 ~= artifact subjects + C1 edges. Existing enum values MAP -- migration,
   not rebuild. Two grain vocabularies coexisting is the incoherence class this effort exists
   to kill; reconcile in one pass.
6. **Enforcement is the ruleset**: declarations land in comp-output-contracts.yaml as closed
   enums; comp-manifest-check gains the coordinate invariant (announce-then-enforce, like
   registration/retired-alias); the 49-pending contract tail becomes the motivated worklist;
   non-subject tools get explicit classes (SUBSTRATE / ROUTER / GATE / PRODUCER) so the
   partition is exhaustive-with-reasons (the manifest's proven three-section pattern).
7. **Known thin rungs print as declared gaps**: C2 motif grain has no query instrument (only
   the scorer comp-canon-motif, an excluded gate-class tool); ms-cloud zero coverage; container
   grain no dedicated tool. The ladder makes gaps visible -- that is a feature.
8. **Vocabulary hazard**: the "two-grain initiative" surfaces (breadth nav / drill) must not
   collide with G(N) grain vocabulary -- surfaces are UX, coordinates are ontology. Non-grain
   surface names (navigate/drill) = a naming act at Andrew.

## Round 2 (~143xZ) -- Andrew verbatim

> "I agree completely with indexing into C ladder versus adding mirrored G. The only question
> becomes how exactly is C ladder indexed if there is technically some overlap, e.g. comp-estate
> could really be c4 and c3."

**RESOLVED BY THIS WORD: fork F-B closes as INDEX-INTO-C (no mirrored G ladder).**

CVO answer on the indexing mechanics (delivered in-session, summary):
- The indexable unit is the MODE / manifest ENTRY (the answer-type), never the binary. Overlap
  dissolves at mode granularity: comp-estate --segments=C4, <thread>=C3.ii, --matrix=C3-recon,
  --layers/--definitions=CANON-SERVER, key-derivation=C0. The manifest's entries: rows and the
  output-contract per-mode blocks (comp-pipescript's `deployed:{plane:applied}` precedent) are
  the EXISTING machinery -- the index lives there, gate-checked; the tool-level list is DERIVED
  from mode declarations (a predicate, not a roster).
- SUBJECT-vs-CONTENT rule: the coordinate is the rung of the question's SUBJECT; constituents
  rendered in the body do not change it ("what is in this thread" = C3.ii even though the answer
  lists C0s/C1s).
- C3 keeps its sub-partition in the enum (C3.i vs C3.ii) because the invariant pair assigns
  different OBLIGATIONS (a C3.i-indexed mode may never hand-insert membership; a C3.ii mode
  serves legislation).
- Proposed closed enum: {C0, C1, C2, C3.i, C3.ii, C4, D1, D2, D3} + non-subject classes
  {SUBSTRATE, ROUTER, GATE, PRODUCER, CANON-SERVER}. Cross-rung JOURNEYS are surface UX
  composing crisply-indexed steps; surfaces carry no coordinate.

## Round 3 (~144xZ) -- Andrew verbatim

> "Interesting, I like it, my only question on this regard is where/how this is structured into
> the registry. i want to make sure that all these modes and coordinates (and the prose "why")
> are rigidly categorized, preferably according to our 3-tiered ontology (1.) MECE 2.) Grain
> 3.) Intent)"

**GROUNDING NOTE (honest):** "MECE / Grain / Intent" as a NAMED TRIPLE does not appear in the
ontology canon (grep: 0 hits for MECE in NFRA_ONTOLOGY_RULE_BANK.yaml + SYSTEM_DEFINITIONS.yaml)
-- **this verbatim is therefore the triple's defining act**, recorded here as a naming-act
candidate for ratification into the rule bank. Tier 3 however has EXISTING ratified law to bind
to: `intent_source` / `intent_from_above` (rule bank :389/:557-558) -- intent comes from a
governance level ABOVE the artifact, never the artifact's own config (the
denominator-is-its-own-configuration defect, REJECTED at declaration).

CVO structural answer (delivered in-session, summary):
- ONE DECLARATION HOME: comp-output-contracts.yaml per-mode blocks gain `coordinate:` +
  `intent:` (the per-mode shape already exists -- comp-pipescript's `deployed:{plane:applied}`).
  Manifest `entries:` rows are the ROUTING VIEW, validated against the contract (mismatch =
  gate FAIL); tools_index rollups DERIVED. Declare once, derive elsewhere.
- TIER 1 MECE = two invariants in comp-manifest-check: EXCLUSIVITY (every mode exactly one
  value from the closed enum {C0,C1,C2,C3.i,C3.ii,C4,D1,D2,D3} + classes {SUBSTRATE,ROUTER,
  GATE,PRODUCER,CANON-SERVER}) x EXHAUSTIVENESS (declared-mode set reconciles with the tool's
  ACTUAL argparse surface -- the existing subcommand census IS the oracle; its current 41
  UNKNOWN + 12 drifted tail is the measured gap, visible and bounded).
- TIER 2 GRAIN = the `coordinate:` field (round-2 mechanics: subject-rung, per mode).
- TIER 3 INTENT = the `intent:` prose field, ADMISSIBLE ONLY WITH AN ABOVE-SOURCE (consumer /
  registry / PRD / ruling citation) per intent_from_above -- a tool describing itself is
  rejected at declaration. Prose hangs off gate-checked structured rows (TRIGGER_LAYER: lint
  the field, never text-match prose).
- Rollout: pure-add on the 20 declared contracts; the 49-pending tail is the worklist;
  announce-then-enforce per comp-rail precedent.

## Open forks needing a word (Andrew or PRD treatment)

- F-A: D-rail tools -- separate D-coordinate (recommended) vs folded into G?
- F-B: spelling -- "G(N)" as the tool-side alias of C(N), or drop G entirely and declare
  C-subject directly? (Either is coherent; ONE authority file either way.)
- F-C: surface naming (navigate/drill vs other) to clear the grain-vocabulary collision.
- F-D: the existing stage-2 grain enum migration -- one reconciliation pass, gate-checked.

-- 3.0.0_SA_CVO
