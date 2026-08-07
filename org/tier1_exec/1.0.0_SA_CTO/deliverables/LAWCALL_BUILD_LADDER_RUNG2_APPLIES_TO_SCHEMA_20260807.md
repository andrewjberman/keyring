# LAW CALL for Andrew -- Build Ladder rung 2 enumerates where it should name a class

**Author:** `1.0.0_SA_CTO~D` | **Co-signed by:** `4.0.0_SA_CRO` (the party who committed the error)
**Date:** 2026-08-07 | **Status:** ⛔ **PROPOSAL. NOT LANDED. Andrew's rule, Andrew's call.**

> The Build Ladder is **Andrew-direct 2026-08-06**. Extending its scope is a change to his ruling, so
> this is drafted and surfaced, **not landed**. No gate is created and nothing is held behind it.

---

## The rule as it stands

> **(2) The estate already has it — CODE *AND* INFRASTRUCTURE.**

Then two worked paths: for **code**, reuse the helper (`comp-which` / `comp-grep` first); for
**infrastructure**, sweep `comp-estate --layers`.

## What happened tonight

`4.0.0_SA_CRO` spent three revisions of `SCRIPT_IO_ONTOLOGY_SPEC` designing a new ontology layer
(`S0` sites / `S1` bindings, five axes, a new `sits_inside:` structural relation, a new rule-bank
section, and a naming act to Andrew for new canonical tokens).

**Every capability it would have added was already materialized on 961 live graph edges.** Measured
independently by CRO and by me, converging:

| the spec would add | already live | coverage |
|---|---|---|
| S0 site (file:line) | `props.via` | **961 / 961** |
| resolution / observer | `props.resolution` | **961 / 961** |
| direction | `srcField -> dstField` | 961 |
| grain | D1 `grain_axis` | ratified |
| condition | `props.condition` + `kind` | ratified (capture sparse -- see the D1 finding) |

**In CRO's own words, which is the sentence that belongs in the ladder:**

> *"I ran rung 2 against extraction twice, caught `recognizer_sdk` the second time, and never once ran
> it against the ontology slot -- then spent three revisions designing a layer whose every capability
> was sitting materialized on 961 live edges. **Rung 2 says 'the estate already has it' and I read
> 'it' as CODE.**"*

CRO **did** obey rung 2 -- twice, correctly, against code, and it worked (it caught the duplicate-SDK
question). The rung simply did not point them at the third thing an estate can already have.

## The mechanism -- and the estate has already ratified the name for it

Rung 2 states its scope as an **enumeration of two** (code, infrastructure). `SYSTEM_DEFINITIONS.yaml`
already carries the ratified term for why that fails:

> **`limitation_class_form`** -- *"A contract carries the limitations of its artifact as a CLASS --
> 'every stated limitation survives verbatim' -- never as an ENUMERATION, because an enumerated list
> of three silently authorises deleting a fourth."*
> `measured:` *"the author objected that naming three caveats authorises deleting a fourth, then
> COUNTED and found at least TWELVE -- 'my own three was the very under-enumeration I was warning
> about, written into the warning itself.'"*

**Rung 2 is that defect, in the Build Ladder, at the rung whose whole job is "check before you
build."** Schema was the silently-excluded fourth. It will not be the last: a taxonomy, an enum, a
status vocabulary, a routing table and a naming convention are all things the estate can already have
and none is code or infrastructure.

**This is not a new principle -- it is an existing ratified principle applied to a rule that predates
its application.** That is the cheapest kind of fix and the reason I think it is worth Andrew's minute.

## Proposed amendment -- name the CLASS, keep the worked paths

Replace rung 2's scope line only. **No other rung changes; no gate is added.**

> **(2) The estate already has it — in ANY form it can already exist in.** Code, infrastructure,
> **schema/ontology, taxonomy, or convention.** For **code**: `comp-which "<what you're about to
> write>"` / `comp-grep` first. For **infrastructure**: `comp-estate --layers` (c0–c4). **For a
> SCHEMA, TAXONOMY, VOCABULARY or ONTOLOGY term: check the ratified registry and the live graph
> before proposing a new one — `comp-estate --definitions <term>`, and query the rail/edge that
> already carries the grain you want.** An existing rung, rail, term or field you did not find is a
> duplicate you are about to legislate — **and a duplicated SCHEMA is worse than duplicated code,
> because it requires a naming act to remove.**

**The last clause is the load-bearing addition.** Duplicated code is deleted by whoever notices.
A duplicated ratified token needs a naming act, a version bump and a changelog entry to retire --
so the asymmetry runs the wrong way relative to how carefully each is currently checked.

## Why this is a proposal and not an edit

The Build Ladder is Andrew's, ruled 2026-08-06. Its final line -- *"Every rung skipped is a duplicate
the next agent finds beside the original and must adjudicate"* -- is exactly what happened, so the
rule diagnosed its own miss; it just did not have the vocabulary to prevent it.

**Three ways Andrew may reasonably rule, and I do not have a preference strong enough to argue past
his:**
1. **Take the amendment** as drafted (or reworded -- the phrasing is his).
2. **Reject it as prose tax** -- CLAUDE.md's own rule is that gates teach at violation time while
   prose taxes every session forever. A one-instance failure may not warrant a law edit.
3. **Route it as a gate candidate instead** -- e.g. a commit-time lint on new `*_LAYER:` / enum /
   registry-token definitions requiring evidence the term was checked against
   `comp-estate --definitions` and the live graph. That fits the file's stated preference for gates
   over prose, and I would draft it if he wants it.

**Cost of doing nothing:** one wasted spec, already absorbed, and the class stays open. It is not
urgent. It is cheap.

---

## Provenance

- Error committed and self-caught by `4.0.0_SA_CRO`; they asked that the correction go into the
  ladder rather than their postmortem, and offered the co-sign.
- Measurements: `comp-kuzu` at Nessie HEAD (pin == marker HEAD), 20605 nodes / 41181 edges, run
  independently by CRO and CTO~D, converging; census by `3.0.0_SA_CVO~C` @a950cd593.
- Arch ruling that produced it: `SCRIPT_IO_ONTOLOGY_ARCH_RULING_S_LAYER_20260807.md` @8b0ed3212.
