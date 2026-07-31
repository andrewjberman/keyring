# WS-C1 ROUND 2 -- THE `layer` AXIS: RULING

**CORE design, `1.0.0_SA_CTO~Z`, CORE owner.** Mechanism only -- an axis decision, populating nothing.
**Not touched by the Andrew-direct lifecycle-value gate.**

## RULING 1 -- DO NOT NAME A `type_tuple` AXIS `layer`. THE TOKEN IS ALREADY OVERLOADED THREE WAYS.

**Measured, live, today:**

| # | Meaning of `layer` | Where it lives |
|---|---|---|
| 1 | **data tier** -- bronze / silver / gold | CLAUDE.md Rules 15, 17, 17a; `data/*/scripts/{gold,silver,bronze}` |
| 2 | **CSE algebra layer** | rule bank `/meta/layers/layer_1_cse_algebra`, `/meta/layers/layer_2_archetype` |
| 3 | **graph subsystem** | `CloudNode.layer` / `CloudEdge.layer` -- `portal`, `ms`, `aws`, `pipeline`, `semctl` |

**Adding a fourth to the `type_tuple` would be the `scope` two-rail collision KNOWINGLY REPEATED, at
larger scale.** This morning `scope` cost a valid `PERMANENT` declaration -- silently demoted to
`UNDECLARED` by a reader that held the right token in the wrong rail -- and the defect neither the
ruling seat nor I named was that **A TOKEN CANNOT CARRY ITS RAIL.** `scope` was overloaded **twice**
and produced a live misresolution. **`layer` is already overloaded three times.**

**If the estate needs this axis in the type_tuple, it gets a NEW NAME.** I am not choosing one here:
naming is cheap to defer and expensive to redo, and the axis has a prior question (Ruling 2).

## RULING 2 -- THE ACTUAL DEFECT IS A VALUE-SET ASYMMETRY, NOT A MISSING COLUMN

**AND THIS CORRECTS MY OWN PRIOR FRAMING.** I had carried WS-C3's finding as *"nodes carry
portal/pipeline and EDGES CARRY NEITHER."* **That is false at the schema and false at the data.**

```
CloudEdge schema        : `layer` COLUMN EXISTS
CloudEdge population    : aws 24377 | ms 11423 | semctl 5112   = 40912
edge count (provenance) : 40912                                 -> ZERO nulls
CloudNode population    : portal 11338 | ms 5728 | aws 2046 | pipeline 1337 | semctl 23
```

**The column exists and is 100% populated on both sides.** The defect is that the two populations
carry **different value sets**:

>> **NODES CARRY 5 VALUES. EDGES CARRY 3. THE TWO MISSING FROM EDGES ARE EXACTLY `portal` AND
`pipeline` -- 12,675 nodes, 61.9% of the graph, sitting on axis values that ZERO edges carry.** <<

So a per-`layer` edge census **cannot report the portal or the pipeline at all**; every edge incident
to a portal node is counted as `aws`, `ms` or `semctl`. **That is WS-C3's "reports the frontend as
cloud", and it is real** -- but the mechanism is not absence.

### WHY THIS SHAPE IS DANGEROUS RATHER THAN MERELY WRONG

**Every cheap check passes.** *Does the edge table have a `layer` column?* Yes. *Is it populated?*
100%, zero nulls. *Do the counts reconcile?* Exactly -- 40912 = 40912. **A well-formed schema,
fully populated, reconciling perfectly, returning a well-formed wrong answer.** Only a **value-set
comparison across the two populations** detects it, and nothing runs one.

**This is why "edges carry neither" was the more comfortable diagnosis: it names a gap you can fix by
adding something. The real defect is that the axis is PRESENT ON BOTH SIDES AND MEANS DIFFERENT
THINGS ON EACH** -- which is Ruling 1's disease, one level down, in the same estate, on the same
token. **The overload is not only across documents; it is across the two halves of one graph.**

## WHAT I AM NOT RULING

- **Whether `portal`/`pipeline` SHOULD be edge values.** Zero edges carry them is a MEASUREMENT; it
  is not evidence about what the producer can or should emit. That is a producer question and I have
  not asked it.
- **The name.** Deferred deliberately -- see Ruling 1.
- **Whether the node axis and the edge axis are one axis or two.** If they are two, they need two
  names and the current shared name is the bug. **If they are one, the edge producer is incomplete.**
  **Nothing in the estate records which was intended** -- the same shape as `dormant_guard`'s
  convergent vocabulary, found this afternoon: *if they are one thing the estate has a silent fork;
  if two, nothing records that decision.*

## THE CONTROL THIS EARNS

**Any axis shared between two populations must have its VALUE SETS compared, not merely its presence
checked.** Presence, population rate, and count reconciliation all pass here. The check that fails is
`set(node.layer) - set(edge.layer)`, which is one line and which nobody runs.
