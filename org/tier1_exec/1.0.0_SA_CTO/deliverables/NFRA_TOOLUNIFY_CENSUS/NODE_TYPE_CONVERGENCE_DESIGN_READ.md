# NODE-TYPE CONVERGENCE — DESIGN READ (no edits, per GO 20260725T203045Z)

**Author:** `0.8.0_AE_CloudComp~B` · 2026-07-25 · **Status:** DESIGN READ. Zero edits made.
**Grounding:** kuzu store queried live (provenance header read: `kuzu_nessie_db`, 20,419 nodes /
40,834 edges, Nessie HEAD **current**, built 14:59:43Z, age 5.5h). Mechanism read at source, not
inferred.

---

## HEADLINE — I recommend **DO NOT CONVERGE.** Build the mapping layer instead.

And one correction to the dispatch's own premise before anything else.

---

## 0. THE DISPATCH'S TYPE COUNT DOES NOT REPRODUCE

The GO states **"42 node types = 28 SCREAMING_SNAKE + 14 CamelCase."** I measure **58 = 37 + 21.**

**Two independent routes, and a scope control:**
- Route 1 — group-by over `n.node_type`, classified in python: **58** (37 snake / 21 camel).
- Route 2 — `count(DISTINCT n.node_type)` computed **by the DB itself**, independent of my
  classification: **58**.
- Scope control — `CALL show_tables()` returns exactly one NODE table (`CloudNode`). **So 58 is the
  whole population; there is no second label whose subset could be the 42.**

I am **not** claiming the dispatch is wrong about the *shape* — two conventions do coexist, exactly
as described, and the infra-vs-code split is real. I am reporting that **the population is 38%
larger than the brief states**, which matters because every cost estimate below scales with it.
The likeliest explanation is a different vintage or a filtered denominator; I could not reproduce
42 under any reading I tried. **Per today's own lesson: state what the number is OF.** Mine is: all
distinct `node_type` values in `CloudNode` at the store's current vintage.

---

## 1. WHICH CONVENTION "WINS" — the answer flips depending on what you count

| | SCREAMING_SNAKE | CamelCase |
|---|---|---|
| distinct types | **37** | 21 |
| **nodes** | 7,489 | **12,930 (63.3%)** |

**By type count SNAKE wins; by node count CamelCase wins, and it is not close.** A "converge on
SCREAMING_SNAKE" instruction reads as tidying 21 stragglers; it would in fact **rename the
majority of the graph by volume.**

**Third input, and it breaks the tie in the other direction:** `grain_baseline.json` `per_class`
holds **35 keys, 100% SCREAMING_SNAKE, zero CamelCase.** The certified control speaks only snake.

**So the honest answer to "which wins" is: neither, on these numbers.** The two conventions are not
a style inconsistency — **they encode a real producer distinction** (AWS/M365 infra vs
code/portal/pipeline). A rename erases information that is currently free to read off the name.

---

## 2. AUTHORITATIVE INVENTORY — method, denominator, **and an honest limit**

**Method:** queried the live store and let the DB compute the distinct count; classified by
`fullmatch(r'[A-Z0-9_]+')`. **Denominator: 58 types / 20,419 nodes** at the stated vintage.
**No grep was used to derive the inventory.**

> **LIMIT I AM NOT GLOSSING: the GO asked for a SCHEMA/PRODUCER-derived inventory. I derived a
> STORE-derived one.** These are different quantities. The store shows what **was emitted at this
> vintage**; the producer defines what **can be emitted**. A type that exists in a producer but has
> emitted zero nodes today is **invisible to my method**, and my 58 is therefore a **FLOOR, not a
> census.** Closing that needs the producer/extractor enumeration, which I have not done. I would
> rather hand you a labelled floor than a census I cannot support.

---

## 3. THE GENERIC-WORD SET — exclude, and the reason is quantitative

`Field` `Module` `Page` `Prop` `Hook` `Pipeline` = **6 types, 5,831 nodes, 28.6% of the entire
graph.** `Field` alone is 4,969 — **the single largest node type in the store.**

**They cannot be renamed by any text-driven method, and I would not try.** Their grep counts are
contaminated by ordinary English usage, so a match set cannot be trusted even as a starting point.
A rename here would have to be driven entirely by producer emission sites.

**This alone is close to decisive:** any convergence that excludes the generic set leaves 28.6% of
the graph un-converged — i.e. **it does not achieve convergence**, it achieves a partial rename
plus a new inconsistency. Any convergence that includes it is the riskiest text operation in the
repo.

---

## 4. **IS CONVERGENCE THE RIGHT FIX? NO. RECOMMEND A DOCUMENTED CROSSWALK.**

You said you were not assuming the answer. Mine is a recommendation, not a preference:

1. **Blast radius is the majority of the graph** (12,930 nodes / 63%), not a tail.
2. **28.6% of nodes cannot be safely renamed by text at all** (§3) — so full convergence is either
   unsafe or incomplete.
3. **The names carry information.** SNAKE=infra, Camel=code is a real, currently-free signal. A
   crosswalk *preserves* it and documents it; a rename *destroys* it and documents nothing.
4. **The grain sentinel makes every rename a candidate false-collapse** (§5) — and it was dark 17
   days. The cost of being wrong here is not a bad merge, it is a blind control.
5. **I have built exactly this crosswalk shape before and know its cost** — WS-4 source↔deployed,
   4 entities, 12/12 including 4 mutants, landed in one session. **A tested mapping layer is
   cheap, reversible, and its failure mode is a missing row rather than a corrupted store.**

**A rename is irreversible-in-practice across two stores and a certified baseline; a crosswalk is
a file.** Given a choice between them at equal information value, the reversible one wins.

**What I would build instead:** a `node_type` crosswalk with a conformance suite (one mutant per
settled mapping, each confirmed to actually flip), reporting its own denominator and its
**unmapped set** in-band — so a concept present in one store and absent from the other is
*surfaced*, not silently dropped. That unmapped set is where the 57-vs-85 class lives (§6).

---

## 5. GRAIN SENTINEL — the coupling, read at source (`grain_sentinel.py:116-137`)

```python
for ntype, base in baseline.items():      # <-- iterates the BASELINE, not the live stream
    if base <= 0: continue
    cur = live.get(ntype, 0)              # <-- a renamed class yields 0
    ratio = cur / base                    # <-- 0.00x == a real collapse, byte-identical
```

**Two consequences, and the second is not in the brief:**

**(a) Confirmed as you stated it.** Rename a baselined class without moving `grain_baseline.json`
in lockstep → `live.get()` returns 0 → `0.00x` → renders identically to a true collapse. The
`_naming_fragility_note` already in `grain_baseline.json` (surfaced by this lane 2026-07-25,
ruled not-firing-today by you) documents precisely this.

**(b) THE BASELINE IS THE DENOMINATOR — so anything live-but-unbaselined is never examined.**
The loop iterates baseline keys, so a class present in the live stream and absent from the
baseline is **not checked, and nothing says so.** The docstring calls this "skipped (new class)",
which is a reasonable policy, but the *coverage consequence* is unstated at the output: **the
sentinel's all-clear is over the baseline's 35 keys, not over the stream.** That is the same shape
as this week's Phase-2 finding — a verdict whose denominator is narrower than its reading — and
it is why I would want the sentinel to **print its covered/uncovered counts** whatever is decided
about naming.

> **SCOPE HONESTY:** I verified the *mechanism* at source. I did **not** verify which stream is
> passed at the call site (`:148` `run_grain_sentinel`), so I am **not** asserting how many live
> classes are currently unbaselined. `baseline.source` reads `"kuzu_stitch_db unioned"` while the
> fragility note says the sentinel runs on the stitch stream; **those two readings are not
> obviously the same scope and I did not resolve it.** Naming that as open rather than guessing.

**Lockstep plan (if a rename happens anyway):** rename + `grain_baseline.json` key migration in
**one commit**, never two; a pre-flight asserting `set(baseline) - set(live) == empty` and
`set(live) - set(baseline)` printed; and a **mutant confirmed to actually flip** — rename one class
without migrating its key and prove the sentinel reddens, *before* trusting it on the real change.
A migration verified only by "it still passes" is indistinguishable from a sentinel that stopped
looking.

---

## 6. THE 57-vs-85 GAP — **it does not survive convergence, and it is a separate defect**

`ReactQueryKey` = 57 in kuzu (confirmed live this session); `REACT_QUERY_KEY` = 85 in stitch.

**A naming change cannot close a count gap.** Renaming makes the two rows *comparable*; it does
nothing to the 28 missing members. **Convergence would in fact make this worse in one specific
way: once the names match, the gap becomes easy to mistake for a reconciliation problem rather than
a coverage problem** — two stores disagreeing about a count reads as sync lag, whereas today the
different names at least advertise that these are two different pipelines' outputs.

**Naming it now, as instructed: this is a COVERAGE defect, owner unassigned, independent of the
naming decision.** It should be tracked whether or not anything converges, and it should not be
listed as an expected benefit of convergence.

---

## 7. WHAT I DID NOT DO

- **No edits.** Nothing renamed, no baseline touched, `sovereign_held.py` not opened.
- **No producer-derived inventory** (§2 limit) — my 58 is a store-derived FLOOR.
- **Did not resolve which stream the sentinel consumes** (§5 scope honesty).
- **Did not re-derive the stitch-side 43,633 edges or its type inventory** — I read the store I
  could query live; the stitch figures in this read are the dispatch's, not mine, and are labelled
  as such.
- **Did not measure the generic-word grep counts** (30/40/14/10/13/15 in the brief). I deliberately
  did not reproduce them: they are contaminated by construction, and reproducing a contaminated
  number would only lend it false weight.
