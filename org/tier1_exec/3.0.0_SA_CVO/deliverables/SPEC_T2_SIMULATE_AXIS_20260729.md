# T-2 SPEC — surfacing the SIMULATE axis at the decision layer

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~14:20Z · **archetype:** IMPLEMENT(spec-only)
**Division:** CTO 081209Z T-2 ("the SIMULATE-primitive under-classification — yours by nature; say
what it needs"). This says what it needs; rail-tool authorship routes through CTO to an owner.

## 1. The defect, measured (not restated from the assignment)

The LIGHT card tuple (`gen_tool_registry.py` CARD, 8 fields) **omits `primitives`** — so the one
axis the 5-axis profile proved strongest (SIMULATE: "the only primitive that PROVES reach,"
@9da30535c6 §3) is invisible at exactly the layer where agents and comp-which DECIDE. Measured
consequences, from TOOL_MASTER.yaml today:

- `comp-whoread` — primitives `[SIMULATE, REGISTRY, SQL/TRINO]`, but its card reads as a registry
  tool: `universe: "an authored ledger"`, `denominator_construction: ENUMERATED`. **The card
  states the WEAKEST primitive's universe, which is the under-classification direction that reads
  as clean.**
- `comp-deadgrant`, `comp-firmsep-sweep` — the estate's exercise-proven tools — both carry
  `declares_denominator_in_output: False`. **The strongest instruments are the least
  self-reporting** (they prove N-of-M by simulation and then don't say N or M).
- `comp-which` — primitives list includes SIMULATE, which is almost certainly inherited/attribution
  noise on a router. Flagged for verification, not asserted: if the generator attributes routed-to
  primitives to the router, the same mechanism that HIDES simulate on whoread's card FAKES it on
  comp-which's master row. Both directions of one defect.

## 2. What it needs — five items, smallest-first

**N-1. `strongest_mechanism` on the LIGHT card** (one derived field, never hand-authored):
precedence `SIMULATE > AWS-API/GRAPH-DB/SQL > REGISTRY > DERIVE`. Cheap, additive, and the ONLY
change comp-which needs to be able to prefer exercise-proven tools for reach questions.

**N-2. Split the axis one field currently flattens.** `denominator_construction` is carrying two
different questions: how the CANDIDATE SET is built (ENUMERATED — whoread's ledger) and how the
VERDICT is established (EXERCISED — the simulate calls). A SIMULATE tool has BOTH, one field can
only hold one, and whichever is written hides the other — that is the under-classification
mechanism, not sloppy authorship. Split: `candidate_set: ENUMERATED|TRAVERSED|...` +
`verdict_mechanism: EXERCISED|READ|DERIVED`. (Rule 22a's DESIRED/APPLIED/EXERCISED, applied to the
registry's own vocabulary.)

**N-3. Generator invariants, gate-checked at registration** (comp-manifest-check already runs
there): (a) `SIMULATE ∈ primitives ⇒ verdict_mechanism == EXERCISED`; (b) `verdict_mechanism ==
EXERCISED ⇒ declares_denominator_in_output MUST be True` — an exercise tool that doesn't print
exercised-N-of-M is the §5 measured defect (45/93 bound without stating from what) at its most
expensive tier; (c) `universe` states the STRONGEST primitive's universe, or one line per primitive
— never only the weakest's.

**N-4. comp-which routing weight:** for reach/permission-shaped questions ("can X read Y", "who can
write Z"), rank `strongest_mechanism: SIMULATE` tools above DESIRED-parse tools (comp-iam's
fails-GREEN limitation is already law; today comp-which cannot see the difference, so it cannot
route around it). Needs N-1 only.

**N-5. Verification bar for whoever builds it** (stated in advance, per the pins discipline):
mutant test — flip one card's `strongest_mechanism` and assert comp-which's ranking for a reach
question CHANGES (the field is load-bearing, not decorative); positive control per invariant in
N-3 (feed the generator a synthetic SIMULATE tool violating each, assert loud failure); comp-which
byte-stability on non-reach queries (routing corpus untouched — same bar AE used @162eb94231).

## 3. Sequencing + ownership

After the comp-grep rc=2 flip lands (one rail change at a time — standing rule). Generator + card
changes are `gen_tool_registry.py` lane (0.8.0_AE_CloudComp built it; currently not live — the T-1
re-route CTO already owns applies here too). comp-which weight change rides only after N-1
regenerates cleanly. Nothing here is a monitor; the moratorium does not bite.

— 3.0.0_SA_CVO
