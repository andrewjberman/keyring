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

---

# CERT LEDGER — subsequent acts under the same SoD split

Every leg re-run at this seat; no producer self-report accepted as evidence.

| Act | Verdict | Legs run |
|---|---|---|
| **@118529c8d1** v3.6 provenance repair (`Observation_Not_Assertion` specimen→doctrine) | **PASS** | Read the doctrine home myself (`estate-contracts/README.md` prohibition 2 carries the separation); diff confirms definition untouched; checker 68/0. **Added corroboration CRO did not cite: README:13 points AT the specimen**, so the doctrine names its own downstream instance and the registry had the arrow reversed. |
| **@b86a0bbb23** v3.7 lifecycle two-objects ruling | **PASS** | `Lifecycle_Stage` minted (C3.ii vertical grain, sibling-by-contrast of `Lifecycle_Class` at contract-record grain); `Lifecycle_Value`→deprecated alias, `do_not` discharged; `Lifecycle_Class` semantics untouched, `contested_with`→`distinct_from`; checker **69/0**. **Did NOT accept the no-`binding_residue` call** — verified the content MOVED (Lifecycle_Stage carries the 07-31 naming verbatim) rather than being stranded. ⚠ First negative control (`C0`) was **not negative** — it carries `+resolves_via`; re-ran with `Map`/`Federation`/`Surface`/`C3`. |
| **@1528973e5e** v3.5 `resolves_via` seeding | **PASS, no finding** | **17 entry fields** at field grain (indent-4 under a term) = CRO's declared 17. Token grain reads 19. ⚠ **My earlier "18 occurrences" was a SHIPPED artifact** — a token count presented as a field count, caught by CRO, not by me. |
| **@68399b92ad** list-view annex-marker fix | **DISCHARGED-BY @b86a0bbb23's serve-exercise** | Not formally re-certified: the v3.7 cert already ran the exact legs a formal cert would — generic marker on a NON-`binding_residue` field (`+distinct_from`, `+resolves_via`) plus a TRUE negative control. **Recorded as a line rather than allowed to vanish: an absorbed cert with no line is indistinguishable from a skipped one.** |
| **@899052ed51** T4 (served ladder doc) + T5 (README §9 index) | **PASS** | See below. |

## @899052ed51 — T4/T5 certified against my own originating findings

**T4 — the served ladder doc (my F4 / CRO's F-C).** All three sub-findings addressed:
- The retired segment name survives ONLY as a **rename record** (`:8` "estate-infrastructure →
  andrew-infrastructure"; `:18` "the segment's then-name; renamed"). **Correct handling** — the same
  class my census scored as NOT-a-defect for changelog and dated-ledger entries.
- The C4 block is now a **pointer**: *"MEMBER NAMES NOT RESTATED"*, *"QUERIES over the C4 Subject x
  Function grid (3 rows x 4 columns)"* — grid present at the C4 rung, membership cited not restated.
- **Build-collapse carried and dated** (*"provisional `build` column COLLAPSED 2026-08-19, the grid is
  the clean 3x4"*).

**T5 — README §9 (my F-D).** All four sub-findings addressed:
- Stale version pins **gone** from §9; rows cite bare paths + block anchors (the digit-strip variant).
- The **ROUTE_LOGIC row now labels itself** *"POINTER STUB since 2026-08-05"* with its Andrew-direct
  reason — the exact row I flagged as describing content that had been a stub for two weeks.
- C4 described as **segments + the Subject×Function grid**, not verticals-at-C4.
- **Self-disclosing failure mode retained** (*"THIS INDEX IS HAND-MAINTAINED, AND THAT IS ITS FAILURE
  MODE"*) — honest, and the right form given the compile variant was not fully implemented.

**CERT QUEUE NOW CLEAR.**

## Rate series at this seat (recorded because the shipped one matters most)

**7 instrument artifacts / 6 self-caught before filing / 1 SHIPPED**, caught by the counterparty.
The shipped one — a token count presented as a field count — landed on **the exact class I policed all
night** (line-vs-node, token-vs-structure, frozen digits). *Expertise in a failure mode does not
protect the axis.* **A blindness map that only records catches is measuring the catcher, not the
blindness.**

— 3.0.0_SA_CVO
