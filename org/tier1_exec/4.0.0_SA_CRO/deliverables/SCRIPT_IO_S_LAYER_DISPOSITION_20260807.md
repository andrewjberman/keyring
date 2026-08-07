# DISPOSITION — the Script I/O "S-layer": **DISSOLVED, NOT BUILT**

**Author:** `4.0.0_SA_CRO` · **Date:** 2026-08-07 · **Status:** CLOSING RECORD
**Supersedes:** `SCRIPT_IO_ONTOLOGY_SPEC_20260806.md` REV 1–3 (@72279a7c2 / @785ed481f / @2d40590fa)
— **that document is now HISTORY, not a design.**
**Team:** `4.0.0_SA_CRO` (driving) · `3.0.0_SA_CVO~C` (review + exercise) · `1.0.0_SA_CTO~D` (arch)
per Andrew-direct 2026-08-07.

---

## 1. THE ANSWER

> **There is no S-layer. There never needed to be one.**
> **Every capability I specified across three revisions already exists, ratified and materialized, on
> live D1 edges. The real gap is that D1's field grain has NO PYTHON PRODUCER.**

**The work is a BUILD — populate D1 field grain on the `aws`/`pipeline` substrates.**
It is **not** a naming act, **not** a new rung, **not** new vocabulary, and **not in the CRO lane.**

**THE NAMING ACT SHRINKS TO ZERO.** No `S0`/`S1`, no `sits_inside:`, no collision disclosure, no new
bank section, no version bump.

---

## 2. THE MEASUREMENT THAT DECIDED IT

Andrew asked, near-verbatim: *since it's all about data flow anyway, could we just tag on a registry
of input fields and output fields that flow through that point — wouldn't that sit at D1 anyway?
What is in D1?*

A live `FLOWS_TO` edge's `props`:

```json
{"srcField":"MarketTickerData.entity_type","dstField":"entity_type",
 "kind":"recompute/guarded","rename":false,"condition":null,
 "via":"mapping portal/src/api/endpoints/market.ts:249",
 "resolution":"getSymbol on field-read prop access -> declaring type (TypeChecker)"}
```

| I specified the S-layer would add… | already live in D1 |
|---|---|
| Axis 5 IDENTITY (rename tracking) | `srcField` / `dstField` / `rename` |
| Axis 1 DIRECTION | `srcField → dstField` |
| Axis 4 CONDITION | `condition` + `kind` |
| Axis 2 GRAIN | `D1.grain_axis` |
| Axis 3 RESOLUTION | `resolution` |
| **S0 SITE (file:line)** | **`via`** |
| **`observer:(recognizer,tier)`** *(added in REV 3)* | **`resolution` already is it** |

**Seven for seven.** The one thing measured absent everywhere: **a Python-side producer.**

**AND THE ZERO HAS A MECHANISM, so it is not a wrong-predicate artifact and holds at any graph
vintage:** every emitter of `READS_FIELD` / `HAS_FIELD` / `srcField` / `dstField` / `PROP_PASSES` is a
`.ts` extractor, `comp_recognizers_tsx.py`, or `cse_schema.py`. **Zero Python/AWS/pipeline producers
of field grain exist.**

---

## 3. HOW I GOT IT WRONG — one sentence, because it is the transferable part

**I ran the BUILD LADDER rung-2 check ("the estate already has it") against EXTRACTION twice — it
caught `recognizer_sdk` on the second pass — and NEVER ONCE against the ONTOLOGY SLOT.** I proposed a
new rung beside a ratified rail that already carried the exact grain, populated on one substrate and
absent on the other.

> **THE BUILD LADDER APPLIES TO SCHEMA, NOT ONLY TO CODE.** Rung 2 says *the estate already has it*
> and I read *it* as CODE. `1.0.0_SA_CTO~D` is raising this as a law-surface finding on its own; **I
> co-sign it as the party who committed the error.**

Neither reviewer caught it either — both were reviewing *inside the frame I had set*. **The question
that dissolved two hours of work came from Andrew, in one sentence, from outside the frame.**

---

## 4. WHAT THE BUILD LANE INHERITS — declared, not discovered later

**The portal population is the right template. It must be copied WITH ITS DEFECTS DECLARED rather
than inherited as strengths.** Four known-open items:

| # | defect | measured |
|---|---|---|
| 1 | **No locus at all on `PROP_PASSES`** | **0 of 1,382** — the LARGER of the two field-flow carriers. Field-flow locus is **41%**, not 100%. |
| 2 | **Locus imprecision where present** | **9 of 14** line-precise; misses land on the enclosing construct (`return {`, a JSX opening tag, a blank line, one inside a JSDoc comment) |
| 3 | **`condition` null-guard rate** | `recompute_guarded` count is EXACT at 482, but `condition` is present on **23/482 = 4.8%** |
| 4 | **`row` grain is unpopulated ANYWHERE** | Python field extraction is artifact-in / row-out, so it likely **forces** `row` — and DDB items and parquet rows are graph nodes nowhere in the estate. **The largest cost in the reframe.** |

**The observer half is genuinely universal** — `resolution` is 100% on both edge types. **It is
specifically the LOCUS that is thin.**

> ⚠ **SCOPE BOUND, and none of these may be quoted as estate figures:** `FLOWS_TO` + `PROP_PASSES`
> are CENSUS; `RENDERS` (2447), `READS_FIELD` (2110), `HAS_FIELD` (4269) are **UNSWEPT**. 95.2% is a
> `FLOWS_TO` figure; 41% is `FLOWS_TO`+`PROP_PASSES`; 9-of-14 is n=14 across 14 of 35 files.

**AND THE GOOD NEWS, so "D1 is unreliable" does not travel out of this:** D1's own `LIVE: N` claims
were audited — **3 of 4 clear.** Counts EXACT on all three, the `rename` cross-check genuinely passes
(142 == 142), and the `PROP_PASSES` EdgeKind `forward` marker is correctly declared at 0 of 1,382.
**The rail is precise. The defect is a one-off, not a class.**

---

## 5. THE MOST PORTABLE THING WE GOT — carry this into the PRD

> **A DECLARATION NAMING A MANDATORY FIELD HOLDS TRIVIALLY. A DECLARATION NAMING AN OPTIONAL FIELD IS
> THE SHAPE THAT GOES SILENTLY UNPOPULATED WHILE ITS COUNT STAYS TRUE.**

The two D1 mechanism claims that HOLD name `rename` — a boolean, always present. The one that FAILS
names `condition` — nullable. **An optional field declared as "carried" is a claim that cannot fail
loudly.** When the build declares what it populates, that is the shape to watch **in its own
declarations.**

**Second, from the exercise:** `Coverage{attempted, resolved, unresolved}` **measures what was
DISPATCHED, never what was WANTED.** A recognizer needing more resolution than the tree offers is
filtered OUT of the dispatch set *before* `recognize()` runs, so `attempted` never increments. **A run
where none of the build's recognizers could be dispatched is byte-identical to a run with nothing to
find: 0/0/0, invariant satisfied, green.** Remedy: assert on a denominator the filter cannot shrink —
`registered_for_artifact_class` vs `dispatched`, difference enumerated by
`(recognizer, required_tier, served_tier)`. **Gate the PRECONDITION, not the OUTPUT.**

**Third:** the resolved tier is **MODULE-grain, not VALUE-grain** — it resolves `local_imports`, and
hands back **no values, symbols or bindings**, and `emit(site, tree)` gets ONE tree so a recognizer
cannot reach another file's AST. **Climbing LEXICAL_AST → RESOLVED_SEMANTIC buys cross-file constant
folding NOTHING.** `folded_local` works at the LOWEST tier; `folded_imported` works at NO tier.

---

## 6. OPEN AT ANDREW — two, and neither blocks the build

**(a) THE HELD-OUT FENCE.** `ADVI_PERFORMANCE` and `MDPF_GLOBAL` are the held-out test set and must
not shape the rails. **`ATOM_DECOMP`'s case study IS `ADVI_REFACTOR`.** Three readings are open
(fence covers D-rails only / it binds here too / it is discharged) — **his fence, his call.**

> ⛔ **AND IT IS SHARPER THAN A PRINCIPLE — IT IS A DIRECTORY LISTING.** ADVI endpoints sort
> **alphabetically FIRST** in `portal/src/api/endpoints/`. **Any systematic audit of the portal
> template hits held-out surfaces BY CONSTRUCTION.** "Validate portal, then copy it for Python" and
> "do not touch ADVI_PERFORMANCE" conflict mechanically. Additionally, the live C3 `EmergentSystem`'s
> `shared_constituents` are ADVI surfaces — **the graph's own materialization is entangled with the
> held-out set.**
> *The CRO's own shaping-corpus obligation is DISCHARGED (spec §8.0, positive declaration, 8 rows).*

**(b) PLACEMENT.** `projects\ATOM_DECOMP\` is lane `TIER0_MSTR` — not a CRO write lane. If artifacts
belong there, **MSTR places them.**

---

## 7. OWNERSHIP FROM HERE — this leaves the CRO lane

| step | owner |
|---|---|
| PRD for D1 Python field-grain population | **`1.0.0_SA_CTO~D`** (arch/PRD) |
| Decomposition into TOs | **`2.0.0_SA_COO`** (CTO~D does not issue TOs) |
| Verification / mutation batteries | **`3.0.0_SA_CVO~C`** |
| Research input, on request | `4.0.0_SA_CRO` |

**Research proposes; it does not staff.** The CRO's part is complete.

---

## 8. WHAT SURVIVES THE DEAD SPEC

1. **The exercise** (`CVO_C_EXERCISE_SLAYER_ENGINE_20260807.md`) — the only exercised evidence anyone
   has. Engine runs; `Site` populates on real code with loci verified against **re-opened source**.
2. **The `Coverage` dispatch blindness** — a defect in the SDK, not in my spec, so it outlives the
   spec entirely.
3. **`folded` is two values wearing one name** — `folded_local` reachable at the lowest tier,
   `folded_imported` at none. Opposite reachability, one name.
4. **The mandatory-vs-optional declaration discriminator** (§5).
5. **`LAYER_FIELD_ANATOMY.md`** — the eight-layer field-shape reference this engagement produced as a
   side effect, now at `infra/system/ontology/`.
6. **The build-ladder-applies-to-schema law finding** (§3).

---

## 9. METHOD NOTE — the record of a night of mutual correction

Four agents; **nine corrections; not one of them caught by its own author acting alone.**

- Andrew's one-sentence question dissolved the whole design. **Twice** (D1; then the "seven layers"
  count that was eight, sitting beside its own enumeration).
- `CVO~C` retracted a phantom second SDK in 13 min, named the mechanism (*a symbol-table comparison
  cannot distinguish a fork from a re-export*), and **applied to itself the could-not-have-said-
  otherwise standard it had just applied to my Axis 3.**
- `CTO~D` retracted a 10-of-10 that was 8-of-10 — its verifying grep **could not match** `C3.i`/`C3.ii`
  — then corrected its own 961/961 as a per-edge-type figure stated as a population claim, **naming it
  the third instance of the same error at the same seat in one night.**
- I withdrew an occupancy argument that counted repo prose when the serving path matches term keys;
  published `75` first-party AST users that included vendored deps (true: `56`); read a rendered
  `M ` as *staged*; and specified an entire ontological layer whose every capability was already
  materialized on 961 live edges.

> **THE PATTERN, STATED ONCE:** in every single case the measurement was real and **the thing it was
> evidence OF was not what was claimed.** Positive limb measured, negative limb reasoned. **Success on
> the limb you checked is what makes the unchecked limb feel checked** — and that point arrives one
> call early.
