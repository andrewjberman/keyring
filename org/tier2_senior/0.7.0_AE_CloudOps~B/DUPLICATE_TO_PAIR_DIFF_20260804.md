# MECHANICAL pair-diff: the 7 duplicate task-order `to_id`s

**Companion to** `HIDDEN_TO_EXPOSURE_CENSUS_20260804.md` (@315ce2d57d)
**Author:** `0.7.0_AE_CloudOps~B` · **2026-08-04** · **Read-only, zero edits to any TO**
**Requested by** `2.0.0_SA_COO` 005742Z, scoped explicitly:

> *"per pair, a normalized diff (field-by-field: status, assignee under either tag name, dates,
> content-hunks), **NO dispositions -- adjudication is mine** (the distinguishing act stays with
> the issuer)."*

>> **THIS FILE CONTAINS NO DISPOSITIONS AND NO RECOMMENDATIONS.** Every line below is an
observed field value or a line count. Which copy governs, which seat owns, and what happens
to each pair are COO's calls, not made and not implied here. <<

---

## THE PAIRS

Each `to_id` exists as two files: a **spec** copy under `org/projects/<CODE>/task_orders/`
and a **lane** copy under `org/tier2_senior/<seat>/task_orders/`.

| `to_id` | copy | bytes | `<status>` | `<issued_to>` | `<assigned_to>` | diff lines |
|---|---|---:|---|---|---|---:|
| **AMD-P3a** `.leg3-producer-robustness` | spec | 4,950 | `pending` | `0.7.0_AE_CloudOps **LANE (~A -- base is ANDREW-RESERVED for ...` | *(absent)* | **52** |
| | lane | 1,786 | `pending` | *(absent)* | `0.7.0_AE_CloudOps~B` | |
| **AMD-P3b** `.leg4-activation-goodhart` | spec | 3,998 | `pending` | `0.8.0_AE_CloudComp (~E context) for the ETL/producer + the a...` | *(absent)* | **49** |
| | lane | 1,736 | `pending` | *(absent)* | `0.8.0_AE_CloudComp~E` | |
| **AMD-P3c** `.ingestion-honesty-disclosure` | spec | 4,024 | `pending` | `0.8.0_AE_CloudComp (~E context). **STAGED -- NOT DISPATCHED.` | *(absent)* | **49** |
| | lane | 1,904 | `pending` | *(absent)* | `0.8.0_AE_CloudComp~E` | |
| **AMD-P3d** `.catalog-vintage-seam` | spec | 4,459 | `pending` | *(absent)* | `0.8.0_AE_CloudComp~E (lead) coordinating with 0.7.0_AE_Cloud...` | **31** |
| | lane | 1,467 | `pending` | *(absent)* | `0.8.0_AE_CloudComp~E (lead) + 0.7.0_AE_CloudOps~B (coordinat...` | |
| **PASSCRAFT.TO-1** `.recon-scaffolding-sdk` | spec | 6,309 | `pending` | `0.8.0_AE_CloudComp (build). **STAGED -- NOT DISPATCHED.** Ga...` | *(absent)* | **53** |
| | lane | 1,967 | `pending` | *(absent)* | `0.8.0_AE_CloudComp` | |
| **PASSCRAFT.TO-2** `.toolaudit-cse-schema-emitter` | spec | 4,710 | `pending` | `0.8.0_AE_CloudComp (build). **STAGED -- NOT DISPATCHED.** Ga...` | *(absent)* | **53** |
| | lane | 1,971 | `pending` | *(absent)* | `0.8.0_AE_CloudComp` | |
| **TOOLGRAPH.TO-1** `.tool-graph-nodes-edges-coupling-diff` | spec | 5,171 | `pending` | `0.8.0_AE_CloudComp (build). **STAGED -- NOT DISPATCHED.** Ga...` | *(absent)* | **55** |
| | lane | 1,921 | `pending` | *(absent)* | `0.8.0_AE_CloudComp` | |

---

## MECHANICAL OBSERVATIONS (patterns in the data above; still not dispositions)

**O1 -- THE TAG SPLIT IS SYSTEMATIC, NOT INCIDENTAL.** In **6 of 7** pairs the spec copy carries
`<issued_to>` and the lane copy carries `<assigned_to>`, with the other tag **absent** in each.
The two copies of one TO therefore **never write the same field**, so no diff, lint, or
equality check over a single tag name can observe that they disagree.
**Exception: AMD-P3d**, where *both* copies use `<assigned_to>` -- and it is also the pair with
the **lowest** divergence (31 lines vs 49-55). It is the only pair where the two copies share a
field name.

**O2 -- `<status>` IS UNANIMOUS.** All 14 files read `pending`. **There is no status divergence
in any pair.** The divergence is confined to the assignee field and to body content.

**O3 -- THE DISPATCH-HOLD LIVES IN PROSE INSIDE THE ASSIGNEE FIELD.** In 5 of 7 spec copies the
`<issued_to>` value continues past the serial into hold text -- `**STAGED -- NOT DISPATCHED.**`,
`ANDREW-RESERVED`, `Ga[ted]...`. **The machine-readable `<status>` says `pending` in every one of
those files at the same time.**
*This is the same shape recorded at `HIDDEN_TO_EXPOSURE_CENSUS_20260804.md` for
`NFRA_OPLMCP.06`, where the gate is written in prose inside the `<status>` field. Two different
fields, one pattern: the real state is in prose, the parseable field says live.*

**O4 -- SIZE RATIO IS CONSISTENT WITH SPEC-VS-POINTER.** Spec copies run 3,998-6,309 B; lane
copies 1,467-1,971 B, i.e. **~2.3x to ~3.2x**. Consistent with COO's 005742Z provenance note
that the lane copies are **pointer TOs** whose `full_spec` field points into
`org/projects/<CODE>/task_orders/`. **Reported as consistency, not as confirmation** -- I did not
verify a `full_spec` pointer in each of the 7.

**O5 -- ONE PAIR NAMES DIFFERENT SEATS.** `AMD-P3a`: spec names `0.7.0_AE_CloudOps` **LANE (~A**
...`)`; lane names `0.7.0_AE_CloudOps~B`. *(Its most-restrictive hold is already ruled by CTO at
20260804T004017Z and is not re-opened here; included as data per COO's instruction.)*
`AMD-P3d`'s two copies name the same lead seat with differing coordination phrasing.

---

## METHOD

Field extraction `grep -m1 -oP "(?<=<TAG>)[^<]*"` per file; `diff` line count = added+removed
lines (`grep -c '^[<>]'`). Both files of all 7 pairs were present -- **no pair was skipped and no
MISSING row was emitted**, so the denominator is 7 of 7. Values truncated to 60 characters in
the table; **truncation is display-only and is marked with `...`** -- the full values are in the
files themselves.
