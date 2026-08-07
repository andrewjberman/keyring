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

---

# SECOND CALL (separate, independent) -- a gate candidate, and it is NOT the one I first described

**Author of the predicate: `3.0.0_SA_CVO~C`.** I proposed a weaker version; they sharpened it before
it reached Andrew. Attributing the better one.

## What I was going to propose (and it was wrong)

A lint keyed on **nullable fields** -- "any `LIVE: N` / 'carries' claim naming a NULLABLE field must
publish its population, not only its typed count."

## What the measurement actually shows -- the discriminator is **STAMPED vs UNSTAMPED**

CVO~C applied the re-aimed sweep. The whole at-risk set in the rule bank is **three declarations**,
all measured against the 961 census:

| line | claim | verdict |
|---|---|---|
| `:322` | *"graph SERIALIZES `props.kind` as `recompute/guarded`"* | **HOLDS** |
| `:303` | *"884/961 FLOWS_TO carry a non-null dstField"* | **STALE** -- measured 961/961 |
| `:321` | *"props.condition carries the guard. LIVE: 482/961"* | **FAILS** -- 23/482 |

And the block-level pattern is the finding:

```
:301  edge_grain_binding   STAMPED  -- "# denominators printed (comp-kuzu 2026-07-23)"
                           -> :303 is STALE BUT HONEST. It says when it was true. NOT A DEFECT.
:326  coverage_boundary    UNSTAMPED -> :330 has gone FALSE, silently
:318  edgekind_semantic    UNSTAMPED -> :321 FAILS
```

**Both defects live in the two UNSTAMPED blocks. The one STAMPED block ages honestly.** CVO~C's
formulation, which is the rule:

> **A published figure WITH a measurement vintage degrades into a DATED FACT. The same figure WITHOUT
> one degrades into a FALSE STATEMENT** -- in whichever direction the estate happens to move. Stamping
> does not keep a number true; it keeps it **honest about being old**, which is the only property a
> hand-copied denominator can actually hold.

**This is CLAUDE.md's own frozen-not-live class, one rail over** -- the same reason this file refuses
to print a comp-tool count and defers to the gate that maintains it.

## F-5 -- and it drifts the OTHER way, which is why the union matters

`:330` `coverage_boundary` declares *"77/961 FLOWS_TO carry no dstField -- coarser-than-field flow."*
**Measured: 0/961. The gap has CLOSED, silently.**

CVO~C audited their own predicate before claiming a ratified figure had moved -- dstField key absent 0,
None 0, empty string 0, literal `"null"` 0, whitespace-only 0; 961 real values across 386 distinct
strings; **control: the same predicate returns 23 on `condition`, so it is not a predicate that always
passes.** And the bank is internally consistent at its own vintage: 884 + 77 = 961.

> **`:321` OVERSTATES capability. `:330` UNDERSTATES it.** A reader planning work off the bank today
> would scope a **77-edge field-grain remediation that no longer exists.** That is the second time in
> this engagement a stale figure would have driven unnecessary build work -- **the first was the
> S-layer itself.**

**So the gate needs BOTH arms, and they catch different things:**
- **nullable-field** catches a claim that was **never** true (`:321`)
- **unstamped** catches a figure that has **stopped** being true (`:330`)
- **Only the union catches both.**

## ⚠ THE FRAMING I WAS ASKED TO CARRY, AND IT IS THE FAIREST POINT IN THE PILE

CVO~C's words, and I agree with them:

> *"A gate proposal that only indicts reads unfairly. **NONE OF THIS WOULD BE CHECKABLE IF THE BANK DID
> NOT PRINT ITS DENOMINATORS IN THE FIRST PLACE.** The practice that exposed three drifted figures is
> the same practice that makes the rail auditable at all, and the stamping convention WORKS exactly
> where it is applied."*

**The ask is therefore to EXTEND AN EXISTING GOOD HABIT to two blocks that lack it -- not to install a
new one.** That is a much cheaper ask and a truer description of the file. **The rule bank is in good
shape**: 3 of 4 `LIVE: N` claims clear, counts exact, the `rename` cross-check genuinely passes, the
`forward` marker honest. Nothing here should travel as "D1 is unreliable."

**Proposed, for Andrew:** stamp the two unstamped blocks with a measurement vintage (the convention
`:301` already uses), and -- **only if he wants the mechanised half** -- a commit-time lint that denies
a new population figure in those blocks without a vintage stamp. **Not built. Not routed. His call.**

---

## Provenance

- Error committed and self-caught by `4.0.0_SA_CRO`; they asked that the correction go into the
  ladder rather than their postmortem, and offered the co-sign.
- Measurements: `comp-kuzu` at Nessie HEAD (pin == marker HEAD), 20605 nodes / 41181 edges, run
  independently by CRO and CTO~D, converging; census by `3.0.0_SA_CVO~C` @a950cd593.
- Arch ruling that produced it: `SCRIPT_IO_ONTOLOGY_ARCH_RULING_S_LAYER_20260807.md` @8b0ed3212.
