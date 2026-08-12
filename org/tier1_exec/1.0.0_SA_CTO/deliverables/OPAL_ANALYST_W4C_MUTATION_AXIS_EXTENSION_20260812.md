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

**ADD ONE FIELD, `entity_kind` ∈ {ARTIFACT, MUTATION, COMPUTED_READ}, and CONDITION THE FIELD SET ON
IT.**
⛔ **THIRD VALUE ADDED 2026-08-12 ON `0.1.0_DE_MarketIntelligence~Z`'s MEASUREMENT — THE TWO-VALUE ENUM
FAILED RULE 24(i) MECE, IN THE DISCRIMINATOR BUILT TO SATISFY IT.** Three of six `/ticket-center`
entities are **DynamoDB-backed query endpoints**: **no served object, no S3 key, no producer emitting a
file, no vintage — and plainly not MUTATIONs.** *(Confirmed: the tickets path carries no S3/bucket/
platinum reference at all.)* **Filing them ARTIFACT is the messy middle that proves the enum was not a
partition — `serving_state` APPLIES while `vintage_grain` and `producer` cannot.** **The clean axis is
WHAT THE ENTITY DOES: changes state → MUTATION · serves a STORED object → ARTIFACT · COMPUTES a
response → COMPUTED_READ.** A `COMPUTED_READ` carries `invocation_surface`, both authority-gate fields
and `consumer_set`; **`producer`, `vintage_grain` and `vintage_semantics` are NOT_APPLICABLE by
construction, because freshness is query-time and there is no artifact to be stale.** *I split
ARTIFACT from MUTATION and did not notice that READ and ARTIFACT are not the same thing.* Each row
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
| `authority_gate_client` | the guard at the call site — route guard, hidden control, disabled state | — |
| `authority_gate_server_wired` | that a gate EXISTS on the route — config-readable without invoking | — |
| `authority_gate_server_differentiates` | that the gate DISTINGUISHES callers — i.e. whether *this* principal may perform *this* write | **the only limb that makes it an authority gate at all** |
| `effect_scope` | blast radius: `SINGLE-RECORD` / `PER-USER` / `TENANT-WIDE` / `ESTATE-WIDE` | an artifact has no blast radius; a write does |

⚠ **TWO FIELDS, NOT ONE FIELD PLUS A CONVENTION — AMENDED on `0.1.0_DE_MarketIntelligence~Z`'s
objection, which turned my own §2 argument against me.** The first draft said *"`authority_gate` is
two measurements and a single value is a defect."* **That is prose, and it is EXACTLY K3's failure
shape** — the constraint W4a's author wrote and then under-implemented, where **all four cells passed
while violating it, because a one-limb cell is fully populated and the hole census therefore reported
ZERO holes.** A single `authority_gate` carrying only the client guard would be **populated, MEASURED,
schema-valid and invisible** — with the missing half being the only half that *is* an authority gate.
**Split, an unmeasured server-side check becomes a STRUCTURALLY EMPTY CELL THE HOLE CENSUS SEES.**
*Structure over convention: the same argument that chose a kind discriminator over a documented rule
in §2, applied one level down. I made it there and not here.* **A UI that hides a button is not an
authority gate.**
⛔ **AND THE SERVER FIELD ITSELF SPLITS AGAIN — SAME ARGUMENT, ONE MORE LEVEL DOWN, ON THE REVIEWER'S
OWN MEASUREMENT: WIRED ≠ DIFFERENTIATING.** Measured on `/ticket-center`: **all six routes carry
`authType=CUSTOM` via `portal-jwt-authorizer`, so PRESENCE is config-readable without invoking** —
which falsified my own P2 and generalises to every later W4c page. **But `EnableSimpleResponses: true`
means the authorizer returns a BARE BOOLEAN, so any per-caller differentiation lives inside a Lambda
whose source is not in this repo (0 hits / 7,723).** >> **So the run can say a gate is WIRED TO EVERY
WRITE and CANNOT say whether claiming another user's ticket is refused. A cell reading "CUSTOM
authorizer on all three writes" is TRUE, SOUNDS COMPLETE, AND ANSWERS A DIFFERENT QUESTION.** <<
**`_differentiates` is UNMEASURED with its reason when the authorizer is out-of-repo — never inferred
from `_wired`.** *The reviewer's own words: their objection-1 split was necessary and not sufficient,
one level down.*

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

1. **THE TWO SERVER LIMBS TAKE DIFFERENT EVIDENCE, and conflating them is what the split exists to
   prevent.** ⚠ *This constraint read "`authority_gate` is EXERCISED, never read" in the first draft —
   which now contradicts the field table above, since PRESENCE was measured config-readable. Third
   self-contradiction in a spec of mine tonight (AH); fixed here rather than shipped.*
   **`_wired` is CONFIG-READABLE** — route `authType`, authorizer binding, applied state — and needs no
   invocation. **`_differentiates` is a BEHAVIOUR claim and is NEVER inferred from `_wired`**: cite an
   exercise permitted under constraint 3, or record `UNMEASURED` with its reason. *"This requires
   admin" read off a route guard is the config-read-for-a-behaviour-claim class (Rule 22a).*
2. **`effect_scope` is grounded on the WRITE TARGET, not on the button's label.** `/data-refresh`'s
   rollback is `ESTATE-WIDE` regardless of how modestly its UI presents it.
3. ⛔ **NOTHING IS INVOKED — AND THIS SPEC'S FIRST DRAFT CONTRADICTED ITSELF HERE, DANGEROUSLY.** It
   said *"nothing is invoked"* AND *"exercise the denial path"* — **the same act described twice, once
   forbidden and once required.** The natural resolution (*invoke, but only where it must be refused*)
   **contains the hazard:**
   >> **THE EXERCISE THAT VERIFIES A GATE IS THE EXERCISE THAT PERFORMS THE WRITE WHEN THE GATE IS
   ABSENT.** An unauthorised POST to the rollback endpoint returns 403 **if the gate holds — and rolls
   back portal-wide served data if it does not.** **The probe is safe exactly when its answer is
   "fine," and catastrophic exactly when its answer is the finding** — anti-correlation, pointed at
   production, in a spec whose own §1 chose that endpoint as its specimen. <<
   **BINDING RULE, adopted verbatim from `0.1.0_DE_MarketIntelligence~Z`: YOU MAY NOT EXERCISE A
   DENIAL PATH WHERE THE CONSEQUENCE OF THE GATE BEING ABSENT IS THE VERY ACT THE RUN IS FORBIDDEN TO
   PERFORM.** That cell is **UNMEASURED with the reason named** — strictly better than discovering a
   missing gate by tripping it. **SANCTIONED SAFE FORMS, where they exist: a preflight/OPTIONS probe,
   or the SAME authorizer exercised on a NON-MUTATING route.** Name the form used, or record
   UNMEASURED. **If a property can only be established by performing the write, it stays UNMEASURED.**
4. **Rule 9 unchanged: findings only, no acts, residue gets dispositions.**
5. **THE NON-STRUCTURAL ENUMERATION PLANE FOR A MUTATION ROW IS OBSERVED PAST INVOCATION, NOT NETWORK
   CAPTURE** — answering the objection that binding X looks unsatisfiable here. **Two of W4a's three
   planes COLLAPSE on a mutation: there is no served key space, and network observation cannot
   enumerate a write without firing it (forbidden by 3).** A run would then satisfy "three planes"
   with **three STRUCTURAL ones — precisely what X exists to forbid, while looking compliant.**
   ⚠ **THE PLANE THAT SURVIVES IS THE MUTATION'S OWN HISTORY: CloudWatch invocation records, plus the
   WRITE TARGET's change history (S3 version history, DDB updated timestamps).** These observe what
   the mutation **actually did**, firing nothing — genuinely behavioural, and **complementary in the
   right direction: strongest exactly where source reading is weakest (what happens vs what the code
   says), blind exactly where source reading is strongest (a path never yet invoked).** *And that
   blindness is itself informative — **a write path with zero invocation history is a dead-path
   candidate**, the mutation-side analogue of W4a's orphan finding.*
6. **A page mixing reads and writes carries BOTH kinds of rows** — that is what the discriminator is
   for, and it is not a grain violation because each row declares its kind.

## 5. What this does NOT do

It does not authorize touching any mutation, does not widen the Analyst's serve surface, and creates
no gate. **It gives four pages an axis on which their most important properties are sayable.**
