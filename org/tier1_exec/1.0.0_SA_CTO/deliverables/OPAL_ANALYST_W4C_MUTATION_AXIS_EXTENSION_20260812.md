# OPAL_ANALYST W4c — the MUTATION AXIS EXTENSION (the deliverable I owed since splitting W4c)

**Author:** `1.0.0_SA_CTO~Z` · **2026-08-12** · **Status: SPEC, ready for W4c. Not a gate on anything.**
**Unblocks:** `/portfolio-management` `/trade-submission` `/data-refresh` `/ticket-center`.

## 1. The problem, restated from measurement

W4 introduced writes to this program for the first time — **20 write operations plus 11 `useMutation`
across four of six pages**, against **zero** in the entire decomposed corpus. §9.2.4's discriminator
puts mutations on the STOP side, and the reason is precise:

> **A mutation's what/where/under-whose-authority are not "not applicable," they are ABSENT** — so a
> rectangle built on the artifact axis **certifies while saying nothing about the property that
> matters**, and 14f then forbids citing the cells that would have said it.

The live specimen: `/data-refresh` carries an **emergency rollback restoring portal-wide served
data**. On today's axis its most important properties have nowhere to live.

## 2. The fix is a KIND DISCRIMINATOR, not a wider field list

⛔ **Do NOT bolt mutation fields onto every row.** That mixes artifact-grain and mutation-grain values
on one axis — Rule 24(ii) — and leaves most cells structurally unmeasurable on most rows, which is
exactly the concealing silence the extension exists to remove.

**ADD ONE FIELD, `entity_kind` ∈ {ARTIFACT, MUTATION}, and CONDITION THE FIELD SET ON IT.** Each row
then carries exactly the fields its kind admits. Rule 24 check: **(i) MECE** — a row is one or the
other, never both; **(ii) same grain** — every value on a given axis describes the same kind of
thing; **(iii) intent coherence** — one axis, one intent, kind declared rather than inferred;
**(iv) state coherence** — one remedy (declare the kind) moves every value together.

## 3. The mutation field set

**PLANE A — MEASURED FACT** (evidence class DATA/SOURCE/CONSUMER, re-grounded live; exercised, never
config-read, per Rule 22a):

| field | what it records | why it has no artifact analogue |
|---|---|---|
| `write_target` | the resource actually written — table / bucket+prefix / key / external system | `serving_state` describes a thing SERVED; this describes a thing CHANGED |
| `invocation_surface` | every call site that can trigger it, with its UI path | the inverse of `consumer_set`: who CALLS, not who reads |
| `authority_gate` | the authorization required, **at the call site AND enforced server-side, stated separately** | **no analogue exists — this is the field whose absence is the whole defect** |
| `effect_scope` | blast radius: `SINGLE-RECORD` / `PER-USER` / `TENANT-WIDE` / `ESTATE-WIDE` | an artifact has no blast radius; a write does |

⚠ **`authority_gate` IS TWO MEASUREMENTS AND A SINGLE VALUE IS A DEFECT.** A client-side guard and a
server-side check are different claims; recording one is the config-read-for-a-behaviour-claim class
(22a). **A UI that hides a button is not an authority gate.**

**PLANE B — RATIFIED SEMANTIC** (CVO~Z under the 2026-08-11 delegation): `canonical_name`,
`business_meaning`, `disposition`, `notes` carry over unchanged, plus:

| field | what it records |
|---|---|
| `reversibility` | is the effect reversible, **by what named mechanism**, and within what window — `IRREVERSIBLE` is a legitimate and important value |

**PLANE C — WIDENING-GATED:** `analyst_serve_verdict` carries over **and matters more here than
anywhere in the program**, because for a mutation the question is not *may the Analyst read this* but
**may the Analyst TRIGGER this.** *A widening answer rides to Andrew as a one-line confirm; the
delegation answers, it does not ratify.*

**NOT_APPLICABLE on a MUTATION row, declared rather than left empty:** `serving_state`,
`vintage_grain`, `vintage_semantics`, `producer`, `consumer_set`. **Per §9.2.4 this is now INFORMATIVE
silence — the reader is correctly told these do not exist — where before the extension it was
CONCEALING.**

## 4. Binding constraints on W4c runs

1. **`authority_gate` is EXERCISED, never read.** The claim *"this requires admin"* is a behaviour
   claim; a route guard in source is a config read. **Cite the exercise or mark it UNMEASURED.**
2. **`effect_scope` is grounded on the WRITE TARGET, not on the button's label.** `/data-refresh`'s
   rollback is `ESTATE-WIDE` regardless of how modestly its UI presents it.
3. **NOTHING IS INVOKED. This is a decomposition, not a test.** ⛔ **No mutation is fired to
   discover its effect** — ground `write_target` and `effect_scope` at source and on served state.
   *Exercising `authority_gate` means testing a DENIAL path (unauthorised → refused), never a
   successful write.* **If a property can only be established by performing the write, it is
   UNMEASURED and stays UNMEASURED.**
4. **Rule 9 unchanged: findings only, no acts, residue gets dispositions.**
5. **A page mixing reads and writes carries BOTH kinds of rows** — that is what the discriminator is
   for, and it is not a grain violation because each row declares its kind.

## 5. What this does NOT do

It does not authorize touching any mutation, does not widen the Analyst's serve surface, and creates
no gate. **It gives four pages an axis on which their most important properties are sayable.**
