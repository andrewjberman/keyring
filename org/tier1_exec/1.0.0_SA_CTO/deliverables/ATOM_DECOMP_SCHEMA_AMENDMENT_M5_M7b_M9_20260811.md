# atom_decomp schema amendment — M-5 / M-7b / M-9 — BLOCKING W1's remaining five pages

**Authored:** `1.0.0_SA_CTO~Z` 2026-08-11 ~1750Z (method owner per `00_ATOMIC_DECOMPOSITION_SPEC.md`).
**TO BE LANDED BY:** a seat on the `ATOM_DECOMP` owned-paths lane — **`0.0.0_AB_MSTR~Z`** (permitted:
MSTR · CRO · CRO~A; **CTO is NOT on this lane**, and the lock is Andrew-direct).
**Status:** authored, exercised-by-inspection, **NOT COMMITTED — awaiting a permitted seat.**

## Why this is blocking, not advisory

`3.0.0_SA_CVO~Z` refused certification on W1 page 1 (`/cma`) — correctly:

```
rectangle -> "SCHEMA: 'meta' is a required property"                    rc=1
patch     -> "PATCH-SCHEMA: 'patch_meta' is a required property"        rc=1, nothing written
POSITIVE CONTROL (separate invocation): certified W0 rectangle -> 0 violations, rc=0
```

Rule 14(c) is *patches merge ONLY through the validator*, so the mechanical tier **never ran** on
that page. A certifier cannot certify a mechanical limb that could not have executed.

**The cause is the method's own defect, not the assignee's error.** `0.5.0_AE_OpalETL~Z` extended
the rectangle to carry a **`relations` plane** — which is **CVO~Z's own W0 `M-5` recommendation**,
implemented, with a correct note that widening the *field set* instead would be a Rule 24(ii) grain
violation. **They did the right architectural thing and the method gave them no sanctioned way to
land it.** That is `M-9` exactly. Two seats, on two runs, have now been forced into local forks to
record improvements the method itself asked for.

**On the CMA page the relations plane is where findings R1 and R2 live** — both are properties of
panel/manifest **EDGES**, and 0.5.0 measured that an entity-row lens would have found **neither**.
Dropping the plane to pass validation would discard exactly the findings atom_decomp adds over a
census.

## The amendment — THREE OPTIONAL ADDITIONS, ALL BACKWARD-COMPATIBLE

File: `projects/ATOM_DECOMP/skill/atomic-decomposition/references/ssot_establishment.schema.json`

All three `$defs` below are `additionalProperties: false`, which is why each fork REFUSES. **Every
change is an OPTIONAL property added to `properties` — none is added to `required`.** Existing
artifacts (including W0's certified rectangle) therefore continue to validate unchanged.

**1. `$defs.rectangle` — add optional `relations` (M-5).** The grain-safe home for findings that are
properties of an EDGE rather than of an entity: a panel whose footer date belongs to a different
artifact than the numbers under it; two panel-mates a day apart in vintage; a nav link to a route
that does not exist. Shape: array of objects, each carrying at minimum
`{relation_id, relation_type, endpoints[], value, status, evidence}` — **`status` and `evidence`
mirroring the cell contract so a relation is measurable, refusable, and countable in the hole census
on the same terms as a cell.** ⚠ **NOT a widened field set** — a page-level field on an
artifact-grained axis is the Rule 24(ii) violation this avoids.

**2. `$defs.patch` — add optional `structural_changes` (M-9).** The typed path for landing a
structural or constraint addition through the validator instead of by hand-editing the rectangle
(which the method rightly forbids). Shape: array of
`{target: "constraints"|"relations"|"fields", op: "add", payload, rationale, discovered_by}`.
**This is what makes a verifier's discovered axis landable in the object that produced it** — today
a certification can *find* a missing constraint and the rectangle has nowhere to record it, while
the schema's own migration rule ("a semantic finding that can be formalized moves DOWN to
mechanical") assumes a path down that does not exist.

**3. `$defs.run_manifest` — add optional `notes` (M-7b).** A free-form object for a run's narrative,
boundaries and declared limitations. Its **absence** is what made an author reach for a custom
`_run_notes` key and silently invalidate their own `run.json` against `additionalProperties: false`
— reported PASS by a `C7` row whose invocation had never been executed. Without this, all fifteen
remaining runs hit the same wall and each `C7`-equivalent row reads PASS.

## Required exercise before the landing commit (do NOT skip — this is a schema, and a permissive schema fails silently)

1. **POSITIVE CONTROL:** W0's certified rectangle (`rectangle.final.certified.json`) still validates,
   0 violations, rc=0 — proves the change is backward-compatible.
2. **NEW SHAPE PASSES:** 0.5.0's `/cma` rectangle + patches validate rc=0 once conformed.
3. **NEGATIVE CONTROL, THE ONE THAT MATTERS:** a *malformed* `relations` entry (missing `status`, or
   an unknown key inside a relation) must still **REFUSE**. **An optional block added carelessly
   makes the schema permissive exactly where the new findings live** — and a schema that stopped
   refusing would be worse than the fork it replaces, because the fork failed LOUDLY.

## Interim handling (already issued)

- **CVO~Z has told 0.5.0 NOT to strip the relations plane.** Correct — re-emission follows the
  amendment, it does not precede it.
- **W1's remaining five pages should not run until this lands**, or each one either forks the shape
  and fails certification, or drops the plane and loses the findings it exists to hold.

## Second-order note, recorded because it is the same shape one level up

**The fix for "the method gives you no sanctioned way to land an improvement" is itself unlandable by
the seat that found it** — I am the method owner and I am not on the `ATOM_DECOMP` lane. The gate is
right and I am not overriding it (`GIT_COMMIT_AUTHOR_OVERRIDE` exists and would be the letter of the
rule against its spirit on another party's locked research folder — the identical call
`0.5.0_AE_OpalETL~Z` made correctly on `ARTIFACT_CENSUS_MP.yaml` two hours ago). Routed instead.
