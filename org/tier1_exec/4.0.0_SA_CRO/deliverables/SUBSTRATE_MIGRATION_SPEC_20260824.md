# SUBSTRATE MIGRATION - buildable spec (NOT executable at this seat)

**Author:** `4.0.0_SA_CRO` · **Date:** 2026-08-24
**Authorized:** Andrew-direct, "All recs approved" on the /open-calls set (Call 1: authorize the
migration; rule the coupling to me or to a named seat).
**Status:** ⛔ **SPEC ONLY. I AM NOT THE LANE.** Reasoning in section 5 - measured, not assumed.

The naming act landed at registry **v3.25** (`e46082b78d`). This is the DATA half, and it was
deliberately kept as a separate act because naming is reversible and moving 20,779 live nodes is not.

---

## 1. What changes

| Layer | Artifact | Change |
|---|---|---|
| Type map | `infra/aws/globgrph/derive_runner.py:2052` `NODE_TYPE_LAYER` | remap node types to the new axis set |
| Relabeller | `derive_runner.py` `relabel_layers_by_node_type` | must not fail-closed on the new values |
| Extractors | `extract_pipeline_cloud.py` (`layer='pipeline'`, `layer='aws'`), `ms_cloud_extract.py` (`layer='ms'`) | emit the new triple rather than a single value |
| Default | `derive_runner.py:1323` - a layer-less node defaults to `layer='aws'` | **this default is now wrong and is the sharpest item here** - see section 4 |
| Column | `layer` -> `substrate` | the open CTO arch-call of 2026-08-12, **coupled** - see section 3 |

## 2. The value map (measured at HEAD 2026-08-24; total closes at 20,779)

| today `layer` | live | `Substrate_Class` | `Substrate` | `Substrate_Path` |
|---|---|---|---|---|
| `portal` | 11,338 | CLOUD | `github` | `portal` |
| `ms` | 6,006 | CLOUD | `ms` | *(tenant/site - to declare)* |
| `aws` | 2,075 | CLOUD | `aws` | *(account - to declare)* |
| `pipeline` | 1,337 | CLOUD | `github` | *(the workspace repo)* |
| `codebase` | 0 | CLOUD | `github` | *(the workspace repo)* |
| `semctl` | 23 | **CLASS_GRAIN sentinel** | - | - |

20,756 map cleanly. The 23 are `C2Motif` (19) and `C3System` (4) - class-grain objects, correctly
excluded via a **countable** sentinel rather than dropped.

## 3. Why the column rename is COUPLED and cannot be sequenced separately

Renaming `layer` -> `substrate` while the values still carry the old single-grain vocabulary produces
a column named for the new model holding the old one. Remapping the values while the column is still
`layer` produces the inverse. **Either alone leaves the graph in a state where the column name and
its contents disagree, and every consumer reading it is silently reading a half-migration.** One act,
one re-derive, one acceptance.

## 4. THE DEFAULT IS THE DANGEROUS ITEM, and it is not on the value map

`derive_runner.py:1323` defaults a layer-less node to `layer='aws'`. **Under the new model that
default is actively wrong in a way the old one merely was imprecise about**: it would assert
`Substrate=aws` for a node whose substrate is genuinely unknown, and `aws` is a real value, so the
mistake is INDISTINGUISHABLE from a correct assignment downstream.

**REQUIRED: the default becomes an explicit UNRESOLVED, never a substrate value.** The ontology
already has the vocabulary for this - `Homeless` exists precisely because *mis-routing is less honest
than an admitted absence*, and the whole coverage obligation (registry section on `CLASS_GRAIN`)
turns on exclusions being countable. A silent default to a real value is the one shape that defeats
both.

**This is the single item in this spec I would not let an executor skip**, because it is the only one
that makes the graph confidently wrong rather than visibly incomplete.

## 5. WHY THIS SEAT DOES NOT EXECUTE IT

Measured, not assumed:

1. **It is infra lane.** Every write lands in `infra/aws/globgrph/`. Rule 13 puts `infra/*` with
   DT/AE, not with an exec research seat.
2. **It is deploy-scope.** The derive runs as an ECS task; the change requires a deploy and a full
   re-derive of 20,779 nodes.
3. **`NODE_TYPE_LAYER` is a CVO-SIGNED FROZEN BASELINE.** The CVO logs record sign-offs against
   specific commits (`derive_runner.py:1497`, signed 2026-07-08, re-signed for the aws COND-A set).
   **Changing a signed baseline needs the signer, not a seat that happens to have write access.**

**Andrew ruled the COUPLING to me. The coupling is an ONTOLOGICAL question - whether the rename and
the remap are one act - and I have answered it: they are (section 3). That is different from owning
the infra change, and conflating the two would be exactly the quiet absorption I said I would not
do.**

## 6. ACCEPTANCE - what a correct migration must show

1. **Denominator closes.** Post-re-derive counts sum to the node total, with the `CLASS_GRAIN`
   population reported as a number rather than omitted.
2. **No node carries a defaulted substrate.** Count of UNRESOLVED is printed and is a finding if
   non-zero - not silently absorbed into `aws`.
3. **The 1,360 frozen residue nodes have moved.** `pipeline` and `semctl` were measured unchanged
   across 08-19 to 08-24; if they are still unchanged after the re-derive, the migration did not run.
4. **Column and contents agree** - no half-migration state.
5. **A positive control**: at least one node of each new value, verified by query, not by reading the
   map.
6. **CVO re-signs** the baseline.

## 6a. ⛔ AMENDMENT — THIS SPEC COVERED ONE OF TWO TABLES. `edge.layer` IS NOT `node.layer`.

**Found 2026-08-24 ~20:15Z while evaluating the B0 gating predicate. This is a defect in the spec
above, authored by me, and it would have been executed.**

Measured live at HEAD:

```
edge.layer :  aws 24,475 · ms 11,979 · semctl 5,049                          41,503 edges, 3 values
node.layer :  portal 11,338 · ms 6,006 · aws 2,075 · pipeline 1,337 ·
              semctl 23                                                      20,779 nodes, 5 values
```

**Same field name. Same graph. DIFFERENT AXES.** `semctl` is **23 nodes and 5,049 edges**. `portal`
is **11,338 nodes and ZERO edges**. Those are not the same population measured two ways; they are two
different things sharing a name.

The estate already knew and already wrote it down — `infra/system/ontology/LAYER_FIELD_ANATOMY.md`
records that **`edge.layer` records WHICH PRODUCER RAN, not endpoint substrate**, and that
`WHERE e.layer='portal'` returns a clean zero while 4,453 portal field edges exist. *A correct-looking
query returning a confident zero, on a field whose name promises otherwise.*

### What this does to the act as specified

Section 1 names the column rename `layer` → `substrate` and does not scope it to a table. **Applied to
both, it renames a producer-identity field to `substrate` — asserting substrate semantics on a field
that carries none.** That is strictly worse than the current state: today the two senses share an
ambiguous name and a careful reader can catch it; afterwards one sense would carry a name that
positively misdescribes it, and the reader has no tell.

**This is the sense-fence class one layer down — a shared word carrying two live meanings — except
that here a migration would have RESOLVED THE AMBIGUITY IN THE WRONG DIRECTION.**

### Corrected scope

| | |
|---|---|
| **IN this migration** | `node.layer` only. The value map in section 2 is a NODE map and always was — every count in it is a node count. |
| **OUT, and now explicitly named** | `edge.layer`. It is a **producer-identity axis with no ratified name**, and giving it one is a separate Rule-24 act with its own four-postulate record and token census. |
| **FORBIDDEN** | applying the `layer` → `substrate` rename to `CloudEdge`. A table-blind rename executes the defect. |

**The honest end state after this migration is two DIFFERENTLY-named fields** — `CloudNode.substrate`
and `CloudEdge.layer` — which is not elegant but is *true*, and it retires the homonym by leaving
only one claimant to the substrate name. Naming the edge axis correctly is the follow-on act.

### Why this matters beyond the fix

The spec above was written carefully, reviewed by me, committed, and cited to the coordinator's own
program as a worked example. **It was wrong in a way no amount of re-reading it would have caught,
because the defect was not in the spec — it was in an unstated assumption the spec inherited: that
`layer` means one thing.** It surfaced only when a different question (does this migration gate the
freeze?) forced a count of who reads the field.

*Recorded here rather than silently corrected, because a spec that was quietly right the second time
teaches nothing to whoever writes the next one.*

---

## 7. STATE

Naming act **LANDED** (v3.25). Data act **SPECIFIED, NOT EXECUTED**. Owner **UNASSIGNED** - it needs
an infra seat plus a CVO re-sign, and both lanes are closed out as of this writing.
