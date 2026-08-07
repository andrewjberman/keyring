# CVO~C EXERCISE REPORT — the S-layer engine, RUN

**Seat:** `3.0.0_SA_CVO~C` · **Requested by:** `4.0.0_SA_CRO` (5-item scope) · **Date:** 2026-08-07
**Plane:** **EXERCISED.** Every result below is a real run against real estate code at `HEAD 72279a7c27`.
**Harness:** scratchpad `slayer_exercise.py` (not committed — a proving rig, not production).

> **THIS IS THE FIRST TIME ANY OF THE THREE SEATS HAS RUN THE OBJECTS THE SPEC IS BUILT ON.**
> Three seats had agreed from source reads. Two of the five items came back **differently than the
> source read implied**, and one of them falsifies a leg of my own P0-1.

---

## HEADLINE — five items, three clean, two findings

| # | Question | Result |
|---|---|---|
| 1 | Does the engine run? | **YES** — 16/16 self-test, `rc=0` unmasked; smoke 3/3 front-ends |
| 2 | Does `Site` populate on a real file? | **YES** — real loci, anti-fabrication control 2/2 |
| 3 | Is the Python RESOLVED tier real? | **YES — but at MODULE grain, not VALUE grain.** See F-1 |
| 4 | Does `Coverage.unresolved` populate? | **PARTLY — one of two paths is invisible.** See F-2 |
| 5 | Is §10.5 blocked? | **YES, and for a sharper reason than we had** |

---

## 1 — THE ENGINE RUNS

```
python org/modules/graph/comp_recognizer_sdk.py   -> === self-test: 16/16 PASS ===   true rc = 0
python gensdk/recognizer_sdk/smoke.py             -> ALL THREE front-ends PASS       true rc = 0
   smoke[python_ast/LEXICAL_AST]:        n_trees=1 cses=2 resolved=2 unresolved=0
   smoke[raw_text/RAW_TEXT]:             n_trees=1 cses=1 resolved=1 unresolved=0
   smoke[python_resolved/RESOLVED_SEM.]: n_trees=3 cses=1 resolved=1 unresolved=0
```

`rc` was taken **without a pipe** (a piped `rc` reports the tail, not the program).

**Bound on what this proves:** these are the SDK's **own fixtures**, authored by the SDK's author, in
`tempfile` directories. **Passing them proves the engine EXECUTES. It does not prove it works on real
estate code** — which is why items 2–4 use a file I chose.

---

## 2 — `Site` POPULATES ON A REAL FILE, AND THE LOCI ARE REAL

**Target — mine, not CRO's:** `data/inf/scripts/gold/INF_A_00.accounts_dimension.py`, 395 lines.
INF tree → **non-held-out** (not ADVI_PERFORMANCE, not MDPF_GLOBAL). Deliberately **not**
`data/etfs/scripts/gold/avgcap_monthly_average.py` — CRO chose that one, and a control the author
selects measures the author.

```
n_trees=1  cses=2  attempted=2  resolved=2  unresolved=0
LOCI EMITTED (denominator 2): ['L90', 'L91']
well-formed L{n} loci: 2 of 2
ANTI-FABRICATION: loci whose evidence is ACTUALLY on that source line: 2 of 2
```

**The third line is the one that matters.** A locus is only worth anything if it points at the code it
claims. I re-opened the target, indexed to each emitted line, and confirmed the recorded `evidence`
literally appears there. **2 of 2.** Without that control, "emitted 2 loci" is compatible with emitting
two fabricated integers.

**VERDICT: S0's landed substrate is real and anchors correctly.** P0-2 is now EXERCISED, not inferred.

---

## F-1 (from item 3) — THE RESOLVED TIER IS REAL, AND IT DOES NOT DO WHAT `folded` NEEDS

**The tier works.** Over the real estate scope `org/modules/graph`:

```
trees built = 245        trees WITH resolved local_imports = 67 of 245
example: module=cli   local_imports=['grain_sentinel', 'nerves_resolve']
```

Real whole-project cross-file resolution, on real code. **Not a stub. CRO's source read was right
about that much.**

**But the grain is MODULE, not VALUE — and `folded` is a value claim.** The complete set of keys a
recognizer can see:

```
meta KEYS AVAILABLE TO A RECOGNIZER: ['all_local_modules', 'local_imports', 'module', 'resolved']
meta keys carrying VALUES / SYMBOLS / BINDINGS: NONE   (denominator: 4 keys total)
can a recognizer reach another module's AST from this tree?
   NO -- emit(site, tree) receives ONE tree; no other file's AST is in meta
```

Direct test, mirroring the real `s3_layout` pattern: `s3_layout.py` defines
`BUCKET = "s3://opal-data-assets/gold/x"`; `consumer.py` does `KEY = s3_layout.BUCKET`. The tier
resolves `consumer.local_imports = ['s3_layout']` — **it tells you the module is local. It does not
hand you `BUCKET`'s value, and the consumer's recognizer cannot reach `s3_layout`'s AST to fold it.**

### F-1a — THIS FALSIFIES A LEG OF MY OWN P0-1, AND I AM REPORTING IT AGAINST MYSELF

P0-1's **Leg B** was CRO's mid-review contribution, which I adopted: *"a site cannot be `folded` if the
front-end tier serving it cannot resolve across files — so Axis 3's achievable values are bounded by
front-end capability."* **I adopted it without testing it. The exercise tests it, and the mechanism is
wrong:**

- **Same-file folding is already available at `LEXICAL_AST`.** `script_io_ast.py:60` — *"Module-level
  `NAME = "literal"` bindings, for constant folding at call sites"*, with `:82` `rebound.add(tgt.id)
  # ambiguous -> refuse to fold`. Single-file, and it works at the LOWER tier.
- **Cross-file folding is available at NO tier**, per the measurement above.

**So climbing the capability ladder buys `folded` NOTHING.** `LEXICAL_AST → RESOLVED_SEMANTIC` gains
you module-import edges and zero value resolution. The tier ladder and Axis 3 are not in the
bounding relationship either of us described.

**P0-1's CONCLUSION STANDS AND IS STRENGTHENED; ONE OF ITS THREE LEGS NEEDS REPLACING.** Leg A
(`opaque` nullifies Axes 1/2/5) and Leg C (the landed `Coverage` channel sits at run/recognizer grain)
are untouched — and the exercise supplies a **better Leg B**: `folded` is bounded by **the
RECOGNIZER's folding implementation**, not by the front-end tier. That is still "a property of the
extractor, not of the line of code" — which is the claim P0-1 rests on — but it is a *different part
of the extractor*, and the corrected version is sharper.

### F-1b — `folded` IS TWO VALUES WEARING ONE NAME

Same-file folding: **reachable today, at the lowest AST tier.**
Cross-file folding: **unreachable at every tier.**
One axis value whose two cases have opposite reachability and require different remedies is
**Rule 24 (ii) SAME GRAIN + (iv) STATE COHERENCE** on the value itself. **Recommend splitting
`folded` into `folded_local` / `folded_imported`, with the second declared `forward: true`** — CRO's
call to author, not mine.

---

## F-2 (from item 4) — `Coverage.unresolved` POPULATES ON ONE PATH AND IS BLIND ON THE OTHER. TEST 7 CAN PASS VACUOUSLY.

**The path that works** — a recognizer whose `emit()` returns nothing (`comp_recognizer_sdk.py:254`):

```
emit-returns-nothing (:254)   attempted=2 resolved=0 unresolved=2
   [('L90', 'emit returned no CSE (unresolved, not silent)'),
    ('L91', 'emit returned no CSE (unresolved, not silent)')]
   TEST-7 INVARIANT attempted == resolved + len(unresolved):  True
```

**Real loci, real reasons, no silent drop.** CRO's proposed test 7 has a live assertion surface here.
Driven by a **mutation** (I broke `emit()` deliberately) — a passing assertion never mutated has never
been tested.

**The path that is blind** — a recognizer requiring a tier the tree cannot serve:

```
over-tier honest-degrade (:246)   attempted=0 resolved=0 unresolved=0
   sample unresolved entries: []
   TEST-7 INVARIANT attempted == resolved + len(unresolved):  True   <-- 0 == 0 + 0
```

**Source-confirmed mechanism, and it is TWO gates, not one:**

- `comp_recognizer_sdk.py:243-246` — `Recognizer.recognize()` honest-degrades and **does** append to
  `unresolved`… **but only for recognizers that get dispatched.**
- `comp_recognizer_sdk.py:304-308` — the registry's dispatch set is
  `[r for r in ... if r.requires <= capability]`, commented verbatim: *"A recognizer needing more
  resolution than the tree offers is **NOT dispatched here**."*

**The registry filters the recognizer out BEFORE `recognize()` is ever called, so `attempted` never
increments and the recognizer is invisible to the coverage arithmetic entirely.**

> **THE CONSEQUENCE, AND IT IS EXACTLY THE FAILURE MODE TEST 7 EXISTS TO CATCH:**
> **`Coverage` measures what was DISPATCHED, never what was WANTED.** A run in which *none* of the
> registered recognizers could be dispatched is **byte-identical in Coverage** to a run in which there
> was genuinely nothing to find: `attempted=0, resolved=0, unresolved=0`, invariant satisfied,
> **test 7 GREEN.** That is a clean zero from a silenced instrument — the precise defect
> `script_io_ast`'s whole posture, and this spec's Axis 3, exist to prevent.

**To be fair to the SDK: the registry filter is CORRECT.** You should not run a recognizer at a tier
where it cannot be honest. **The defect is not the filter — it is that nothing records that a wanted
recognizer was EXCLUDED.** The exclusion is silent, and silence is the defect.

**Recommend test 7 assert on a denominator the filter cannot shrink** — e.g.
`registered_for_artifact_class` vs `dispatched`, with the difference enumerated by
`(recognizer, required_tier, served_tier)`. As written, test 7 gates the **output** and needs to gate
the **precondition**. CRO's to author.

---

## 5 — §10.5 IS BLOCKED, CONFIRMED BY EXERCISE, FOR A SHARPER REASON THAN WE HAD

```
RESOLVED_TIER_AVAILABLE (TS/JS) = False
TS/JS stub trees yielded over portal/ : 0   -> yields NOTHING, exactly as its docstring declares
comp_recognizers_tsx.py -> its recognizers require: ['RESOLVED_SEMANTIC']
```

**The estate's existing TSX recognizers require `RESOLVED_SEMANTIC`, and TS/JS `RESOLVED_SEMANTIC`
yields zero trees. So they are NOT dispatchable today** — and by F-2, that non-dispatch is **silent**:
it produces `attempted=0`, not a warning.

So §10.5's cross-language field join is blocked, CRO's REV-2 stop is **correct**, and the reason is
stronger than "the stub is empty": *the estate already has the TSX recognizers, and they are gated out
at exactly the tier that is stubbed.* This also settles the open remnant of my retracted P1-5 —
`comp_recognizers_tsx.py` existing does **not** make the join reachable.

*Correction to my own harness output: it printed a garbled line here (`"...at RESOLVED_SEMANTIC tier
is dispatchable TODAY; one at RESOLVED_SEMANTIC is not"`) from a sloppy conditional. The measurements
above are correct; that one printed sentence was not. Stated rather than quietly re-run.*

---

## WHAT THIS CHANGES

| Claim | Before | After |
|---|---|---|
| Engine runs | inferred | **EXERCISED** |
| S0 substrate real (P0-2) | source-read | **EXERCISED**, anti-fabrication controlled |
| P0-1 conclusion | 3 source-derived legs | **STANDS**, Leg B replaced by a measured one |
| `folded` reachable | assumed tier-bounded | **two values, opposite reachability** (F-1b) |
| Test 7 sound | proposed | **can pass vacuously** (F-2) |
| §10.5 blocked | source-read | **EXERCISED**, sharper reason |

**What I did NOT exercise, so nobody inherits it as settled:** the five axes themselves (nothing
implements them — S1 is greenfield, per the state-coherence finding), the C1 aggregation of R1, and
any claim about the *portal* TS toolchain outside the stub. **Those remain DESIRED-plane.**

---

# ADDENDUM — CRO ATTACK POINT 4: DOES THE PORTAL POPULATION ACTUALLY WORK?

CRO's reframe rests on *"do for Python what portal already does."* They measured **961/961 FLOWS_TO
carrying a `via` locus and a `resolution` observer** and correctly flagged that as a **COMPLETENESS**
figure, not a **CORRECTNESS** one. This is the correctness audit.

## F-3 — THE FIELD PAIRS ARE GOOD. THE LOCI ARE NOT. And that split is the worst possible one for this plan.

**Method.** 400 FLOWS_TO edges pulled (of 961); 400/400 carried a parseable `file:line`; **35 distinct
files**. Sample = **first edge of each distinct file, alphabetical — SYSTEMATIC, never hand-picked**
(a hand-chosen sample measures the auditor). For each, I opened the file at the claimed line and asked
whether it performs the claimed `srcField -> dstField`.

**NEGATIVE CONTROL (mandatory, and it is what makes the number mean anything):** the same predicate run
at 81 unrelated lines in the same files fired **2 of 81 = 2.5%**. Against a 64% hit rate, **the
predicate discriminates.**

```
RESULT   hits=9  miss=5  file/line-missing=0   DENOMINATOR=14
NEGATIVE CONTROL  2 of 81 unrelated lines (2.5%)
```

**WHERE THE LOCUS LANDS, THE EDGE IS RIGHT — and impressively so.** Not just trivial identity pairs:

| line | claim | reality |
|---|---|---|
| `ticker: record.Symbol,` | `Symbol -> ticker` | **rename, correct** |
| `articleCount: topic.article_count \|\| 0,` | `article_count -> articleCount` | **rename, correct** |
| `color: getConfidenceColor(data.confidence),` | `confidence -> color` | **recompute through a function, correct** |
| `timestamp: keywordData?.generated_at,` | `generated_at -> timestamp` | **rename, correct** |
| `firmId: parseNullable(userData.firmId),` | `firmId -> firmId` | **passthrough-with-coercion, correct** |

**THE FIVE MISSES ARE LOCUS-PRECISION FAILURES, NOT SEMANTIC ONES.** I walked ±6 lines around each:

| locus | claim | the real mapping | offset |
|---|---|---|---|
| `aum.ts:368` → `return {` | `period->period` | `total_periods` L370, `latest_period` L372 | **+2 / +4 — and AMBIGUOUS between two** |
| `BenchmarkHeatmap.tsx:546` → `key={...}` | `primary->borderLeft` | L550 `borderLeft: ...${modelColor.primary}` | **+4 — edge CORRECT, locus off** |
| `ReturnVolatilityScatter.tsx:354` → **BLANK LINE** | `name->name` | L353 `getModelColor(model.name)` | **−1** |
| `portal-proxy.ts:607` → **inside a JSDoc `*`** | `bullish->bullish` | **not within ±6 lines at all** | **unlocated** |

**The pattern is legible:** the locus tends to point at the **enclosing construct** — the object
literal's `return {`, the JSX element's opening — rather than the property line, and in two cases at a
**blank line or a comment**. A locus on a blank line or inside documentation is not a judgement call;
**no mapping occurs there.**

> ### WHY THIS IS THE MOST CONSEQUENTIAL RESULT IN THE ADDENDUM
> **The estate's one worked example of field-grain extraction is STRONG exactly where CRO's layer was
> REDUNDANT (the field pair, already in D1) and WEAK exactly where his layer CLAIMED ITS VALUE (the
> line).** `via` at 961/961 is a presence figure; on a discriminating, systematically-sampled,
> negative-controlled audit it is **line-accurate in 9 of 14**.
>
> This does **not** rescue the S-layer — the pair is still already there, and a locus-precision defect
> is a producer bug, not a missing ontology rung. **But it does mean "copy portal for Python" inherits
> a locus-precision defect into the exact field the S-layer existed to provide**, and it qualifies
> CTO~D's "`via` carries the locus, so S dissolves into a D1+D2 query": **it carries A locus, at
> ~64% line precision in this sample.** Anyone building the Python population should treat locus
> precision as a known-open defect of the template, not an inherited strength.

**BOUND ON THIS FINDING, stated because the sample is small:** n=14 across 14 distinct files out of 35.
It is systematic and negative-controlled, but it is **not** a census — **do not quote 64% as an estate
figure.** It is sufficient to establish that locus precision is **materially below 100% and not
uniformly reliable**; it is not sufficient to put a number on the population. A real figure needs the
full 961 audited.

## ⚠ HELD-OUT FENCE — SELF-DISCLOSURE, and a structural tension worth Andrew's attention

**My alphabetical systematic sample put `portal/src/api/endpoints/advisor-intelligence.ts` FIRST** — an
**ADVI** surface. I read one line at `:833`; it was a code comment, and it scored as a MISS. **I did not
use it as a vocabulary example and nothing in this audit or my review is shaped by it.** Disclosing
because the fence's own `obligation_on_every_author` is that an undeclared corpus is indistinguishable
from a breached one, and this is my corpus.

**Fence-clean figure, ADVI row excluded: 9 hits / 4 misses of 13 — the finding is unchanged.**

**The structural tension, which is NOT mine to resolve:** the portal field population is **one
population in one directory tree**, and ADVI endpoints sort alphabetically first in
`portal/src/api/endpoints/`. **Any systematic audit or validation of the portal template encounters
held-out surfaces immediately, by construction.** So "validate the portal population, then copy it for
Python" and "do not touch ADVI_PERFORMANCE" are in mechanical conflict — not in principle, but in the
directory listing. **Surfacing, not adjudicating: it is Andrew's fence.**

## F-4 — THE PORTAL POPULATION'S OWN VALIDATOR COVERS 8 PAIRS

`org/modules/graph/tsgraph_spike/field_parity_check.ts` (64 lines) is a **methodologically strong**
instrument — it explicitly rejects name-grep (*"grep on the field NAME is ambiguous … the authoritative
ground truth is findReferences ON THE FIELD SYMBOL"*) and validates against ts-morph symbol resolution.

**But its `SAMPLE` is a HAND-WRITTEN literal of 8 type/field pairs** — `BenchmarkModelData.{name,code,
returns}`, `ModelPortfolioData.{code,name,returns}`, `BenchmarkPeriodReturn.{spread,model}` — against
**4,969 `Field` nodes: 0.16%**, all drawn from **two benchmark/model types**.

**So the confidence anyone is entitled to in the portal field population is much narrower than
`961/961` and `4969` suggest:** a strong method applied to an author-selected 0.16%, plus my
independent 14-edge locus audit above. **CRO is right to have asked — nobody had checked the thing
being proposed as the template.**

## Retrieval controls that fired during this addendum (reported because they changed my answers)

- **`MATCH ()-[r:READS_FIELD]->()` → `Binder exception: Table READS_FIELD does not exist`.** The graph
  is **two generic tables** — `CloudNode` / `CloudEdge` — with the label as a **property**
  (`edge_type`), not typed relationship tables. My first query shape was unbindable.
- **`r.label` → `Cannot find property label for r`.** Second control failure; the property is
  `edge_type`.
- **Both failed LOUDLY, and that is the point.** On this schema a wrong **property name** errors, but a
  wrong **label VALUE** in a `WHERE` clause **binds and returns 0 silently.** That is precisely the
  hazard CRO warned me about — *"a zero from a wrong predicate is byte-identical to a true zero"* — and
  it is live on this exact schema. **I ran the controls because CRO asked me to ground the class first;
  I had skipped that step, and the controls caught me twice.**
- **`CloudEdge` carries exactly 4 properties: `edge_type`, `layer`, `snapshot_ts`, `props`.** No
  top-level `locus`/`source`/`provenance` column — the locus lives **inside the `props` JSON**, which is
  where CRO correctly found it and where a column-level check would have falsely reported absence.
- **Producer-side corroboration of CRO's portal-only zero, independent of the graph and of its
  vintage:** every emitter of `READS_FIELD` / `HAS_FIELD` / `srcField` / `dstField` / `PROP_PASSES` is
  `extractor.ts`, `extractor_full.ts`, `field_parity_check.ts`, `comp_recognizers_tsx.py`, or the
  schema declaration `cse_schema.py`. **Zero Python/AWS/pipeline-side producers emit field grain.** So
  the zero is not a wrong-predicate artifact — **it has a mechanism: no producer exists.**
- **`RelationshipDelta` (`cse_schema.py:208`) carries `rtype, target, verb, kind, condition` and NO
  provenance field.** Provenance is **CSE-scoped, not edge-scoped** — one emission event carries one
  `Provenance` and may carry N edges. Relevant to R1: the schema supports **one site → many edges**,
  which is the inverse of R1's **many sites → one edge**.

— 3.0.0_SA_CVO~C
