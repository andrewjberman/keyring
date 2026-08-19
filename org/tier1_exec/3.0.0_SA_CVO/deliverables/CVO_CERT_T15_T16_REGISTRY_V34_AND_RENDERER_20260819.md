# CVO CERTIFICATION — T15/T16 registry v3.4 + the definitions-renderer generic fix

**Certifier:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Author (separate seat, SoD split per CRO `@d72e711b07`):** `4.0.0_SA_CRO`
**Scope certified:** `SYSTEM_DEFINITIONS.yaml` v3.3→v3.4 (`binding_residue` on `Substrate_Side` and
`Territory`) + the generic annex-field serve fix in `org/modules/graph/opal_estate_infrastructure.py`.
**Authority:** Andrew-direct "All approved" (CRO terminal), executed `@7241d0dfd7`.

## VERDICT: **PASS** on the ruled scope. One residual finding, non-blocking.

**Every leg re-run by me, not accepted from the author's report** — the producer's self-report is not
evidence (CLAUDE.md NEVER#8).

| Control | Result |
|---|---|
| Registry carries the field | `binding_residue` present at `:64` (Substrate_Side) and `:70` (Territory); `version: "3.4"` |
| **Positive** — `--definitions Substrate_Side` | **SERVES** — *"THE REPORTING RULE SURVIVES, BINDING … A consumer filtering status=deprecated MUST NOT drop this rule"* |
| **Positive** — `--definitions Territory` | **SERVES** — carries the T15 two-sense scoping **and** the ~30-homonym measurement in-entry |
| **Negative** — `--definitions C0` (no annex field) | 4 lines, **no phantom field**. Does not sprout one. |
| **Generic, not special-cased** | `Plane.resolves` = 1 · `Lifecycle_Value.do_not` = 1 · **`Lifecycle_Value.the_collision` = 1** |
| Schema checker | **68 entries, 0 violations** |

**The generic-fix leg is the one that mattered and I tested it beyond the author's claim.** CRO cited
`Plane.resolves`; I additionally exercised `the_collision`, a field they did **not** name. It serves.
So the fix is genuinely generic rather than anticipating only the fields its author knew about — which
is the exact failure my own lint falsification named, avoided here.

## MY OWN NEAR-MISS, recorded because the discipline is the point

**My first serve-exercise returned ZERO and I nearly filed a FAILED certification against CRO's work.**
The bare `comp-estate --definitions` is the **LIST** view (one summary line per term); `cmd_definitions`
takes a *term* argument and the annex fields live in the **DETAIL** view. **My zero was an invocation
artifact, not a defect.**

I caught it by checking my own instrument before concluding — the provenance header read `v3.4`, which
ruled out a stale snapshot and pointed at my call shape instead. **A false FAIL costs exactly what a
false PASS costs**, and on a certification it costs it in the direction of destroying trust in work
that was correct. *Third self-correction of the night — but the first caught **before** it left my
seat, which is the only difference that matters.*

## RESIDUAL FINDING (follow-on, not a certification failure)

**The fix serves the content to whoever asks for a term BY NAME. The filtering decision that causes
the T16 harm is made from the LIST.**

The list view renders:

```
  Substrate_Side         [deprecated] DEMOTED 2026-08-12 (Andrew-direct) FROM AN AXIS TO A REPORTING RULE. THE RULE, which is wh
  Territory              [deprecated] RETIRED 2026-08-12 (Andrew-direct, VERBATIM -- "Territory is not actually useful here, tha
```

Status shown, definition truncated mid-sentence, **no indicator that a `binding_residue` exists.** A
consumer scanning the list to decide what to filter out sees `[deprecated]` and nothing else — which is
precisely T16's harm path (*"a consumer filtering status=deprecated MUST NOT drop this rule"*).

**Scoped honestly:** a program parsing the YAML directly is safe (the field is there), and the ruled
scope did not name the list view. **So this is a follow-on, not a failure** — but it is the one surface
where the original harm can still occur, and it is the cheapest possible fix: one marker per line
(e.g. `[deprecated +residue]`), no schema change.

**Recommend** routing as a small follow-on to the same seat. Certification stands regardless.

## Compounding, worth recording

Four layers in one act, each caught by the discipline the previous layer installed: my schema finding →
Andrew's word → **the execution's own serve-exercise finding a deeper renderer defect that had been
hiding EVERY annex field from EVERY consumer** → a generic fix → this certification finding the one
surface the fix does not reach. The renderer defect was invisible until someone exercised the field
rather than reading the diff.

— 3.0.0_SA_CVO
