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

## 7. STATE

Naming act **LANDED** (v3.25). Data act **SPECIFIED, NOT EXECUTED**. Owner **UNASSIGNED** - it needs
an infra seat plus a CVO re-sign, and both lanes are closed out as of this writing.
