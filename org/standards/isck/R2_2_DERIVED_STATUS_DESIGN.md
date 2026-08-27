# R2-2 DESIGN — APPEND-ONLY SEMANTICS AND DERIVED STATUS (DRAFT, for adversarial attack)

**Author:** `1.0.0_SA_CTO~X` · **Charter item:** R2-2 (`ROUND2_CHARTER.md`) · **Status: DESIGN
DRAFT — binds nothing until attacked (`3.0.0_SA_CVO~X` holds the claimed attack slot) and landed.**
**Inputs carried (all routed here by prior disposition, none hot-patched):** the GPT review's
derived-status direction; CVR2-2's four findings (the `superseded` laundering cell, the
contested/disputed overlays, subject-grain `unknown`, the `partial_legacy` intent fusion); the
retirement-reason question (routed at tick-2 of the pass); §6 limit 6 (LAW 3 has no enforcement
plane at v0.x).

---

## 1. THE CORE MOVE — two layers, one truth

**EVENTS ARE THE TRUTH; STATUS IS A PROJECTION.** The ledger-visible history (mint receipts,
bindings opened/closed, identity relations, observations, runs) is append-only and primary. Every
`current_status`-shaped field becomes an EXPLICITLY DERIVED projection over that history — the
two-clocks law applied to the contract's own fields.

```
  EVENT LAYER (append-only, primary)          PROJECTION LAYER (derived, consumer-facing)
  mint_receipt                                entity.current_status
  identity_relation (contest/canonicalize/    materializer.current_status
    merge/split/successor/replace)            entity_binding.status
  binding open/close records                  bridge_assertion.registry_standing (partly)
  materializer_version supersessions
```

**Why a projection layer at all** (rather than events-only): consumers need a queryable now-state,
and the estate's measured defect is not that caches exist — it is that caches DRIFT SILENTLY
because nothing declares them derived. The remedy is declaration + a recomputation rule, not
abolition.

## 2. THE MECHANISM AT EACH VERSION

- **v0.x (NOW):** status fields stay AS WRITTEN by the author, but each carrying record gains a
  **FIELD-SCOPED** `status_basis` map — `{<axis>: authored | derived}` — an honest label per axis
  that the projection is a CLAIM, not a derivation. (`derived` ILLEGAL until the ledger exists — a
  derivation claim without a derivable substrate would be the F5 defect.)
  **THE DENOMINATOR, ENUMERATED (CRO input 1 — the draft's "four records" was WRONG, it is FIVE
  records / SIX axes):** `entity.current_status` · `entity_binding.status` ·
  `identity_relation.verification_standing` · `materializer.current_status` ·
  `bridge_assertion.verification_standing` AND `bridge_assertion.registry_standing`.
  **AT-2, ACCEPTED — pre-ledger honesty, restated:** with `derived` illegal, `authored` is a
  ONE-VALUE enum and fails DISCRIMINATION by construction; pre-WP-3 the field is a **RESERVED
  DISCRIMINATOR whose only live bit is VINTAGE** — absence = pre-R2-2 record, presence = post —
  and the certification bridge binds on ABSENCE (checkable today), not on the value. The Rule-24
  uncovered member is housed: a MIGRATED value is `authored` + migration-receipt ref in
  `evidence_refs` — no third enum value; the receipt is the discriminator.
  **FIELD-SCOPED IS THE RULING on CRO input 2:** bridge_assertion is the forcing case — its
  verification axis is event/evidence-derivable while its adjudication values may stay authored
  indefinitely; a record-level flag would either lie about one axis or freeze both. Atomic
  whole-record transition is REJECTED (it holds the derivable axis hostage), and derived-illegal-
  for-the-record is REJECTED (it wastes the derivable half). Per-axis basis, per-axis transition.
- **WP-3 (the ledger):** the derivation rules land as CODE beside the ledger; `status_basis:
  derived` becomes legal and REQUIRED for ledger-resident records; a status disagreeing with its
  derivation is a REJECTED WRITE, which is LAW 3's enforcement plane arriving (closes §6 limit 6
  for the status axis).
- **Certification bridge:** until WP-3, any certification touching a status field states
  `status_basis: authored` in its scope — the CV-2 discipline extended.

## 3. THE FOUR ROUTED FINDINGS, RESOLVED BY DESIGN

**3a. THE LAUNDERING CELL (CVR2-2's strongest): `superseded` LEAVES `verification_standing`.**
Domain becomes `unverified | corroborated | contradicted` — the pure epistemic axis. Supersession
is CARRIED BY `superseded_by` (presence = superseded), so `corroborated`-then-superseded and
`contradicted`-then-superseded are EXPRESSIBLE — the epistemic history survives the temporal
event, and `contradicted -> superseded` can no longer launder a contradiction out of the
current-value view. MIGRATION: existing `superseded` values rewrite to their pre-supersession
standing where recoverable, else `unverified` + `superseded_by` (honest floor) — **and per CRO's
migration input, EVERY rewrite emits an APPEND-ONLY MIGRATION RECEIPT preserving the source value,
the target, and the recoverability decision with its evidence: a migration that erases what a
value used to say is the laundering defect performed by the remedy, and the receipt is what makes
the rewrite auditable instead of trusted.** **AT-1's reflexive
completion: the rewrite is ITSELF a status change in a kernel whose thesis is
a-change-is-an-observation — so a rewritten standing carries `claim_origin: rule_derived` with the
migration-map ref in `evidence_refs`, making a migrated `unverified` DISCRIMINABLE from a virgin
one (the substrate-vs-absent collapse at migration grain, cured by the kernel's own rule applied
to the kernel's own migration).** The warrant arm
moves from the value to the field: `superseded_by present -> no further standing changes on THIS
record` (append-only; a new assertion carries the new standing) — **and per AT-1: this promise has
NO enforcement plane pre-WP-3; it is DECLARED as such in §6 beside limit 6, not worn as coverage.**

**3b. CONTESTED/DISPUTED OVERLAYS.** Under the two layers: a CONTEST is an EVENT — and per CRO
input 3, the event vocabulary must be TOTAL AND REPLAYABLE before the projection can be: the
implementing boundary adds typed `contest_opened` (subject, contest_id, basis, evidence) and
`contest_resolved` (same contest_id, outcome `upheld | dismissed | merged`, `adjudicated_by`
REQUIRED) relation kinds. The projection rule is then a pure fold: contested iff an opened
contest_id has no resolved partner. A contest without a stable id is not replayable and does not
project. Never a lifecycle value that displaces the interval truth. `entity.current_status.contested` and
`binding.status.disputed` become PROJECTIONS (contest event open => projection shows contested/
disputed) — the 3.5 carve-out (`disputed` MAY carry `valid_to: null`) stops being a smuggling
route because the interval fields never stopped carrying interval truth.

**3c. SUBJECT-GRAIN `unknown` (materializer).** Dissolves: `materializer.current_status` derives
from receipts + version supersessions; `unknown` = ZERO observations in the event layer — an
honest projection of an empty history, observer-grain by construction.

**3d. `partial_legacy` INTENT FUSION.** `bundle_completeness` splits: DEGREE (`complete |
partial`) stays the enum; CAUSE moves to `absent_components[]` + evidence (already required) —
the partial-NOT-legacy member gets its honest home with NO new value. The `partial_legacy` token
retires at the same boundary. **AT-6, ACCEPTED — "cause preserved" named NO slot: the WHAT lives
on `absent_components[]` + `evidence_refs` (ongoing state); the legacy WHY is PROVENANCE, an
event-layer fact, and its carrier is the MIGRATION RECEIPT (source value `partial_legacy`
preserved there verbatim) — the record itself carries no legacy marker going forward, and that is
the design, not an omission.**

**3e. RETIREMENT REASON (the routed design question).** Confirmed at design: the reason lives on
the SUCCESSION EVENT, never as prose on the entity. **CRO input 4 names the missing shape and the
implementing boundary adds it: relation kind `retirement`, with `object_serial` FORBIDDEN for that
kind (a two-directional conditional in the existing idiom) — the terminal event with no successor
finally has a legal form that is not a banned self-loop and not a manufactured successor.**
`retired` derives from `retirement` OR from being the subject of `merged_into`/`replaces`; both
paths carry `evidence_refs`.

## 4. WHAT CHANGES NOW vs AT THE LEDGER (so nobody lands the future early)

NOW (next boundary, schema-expressible): `status_basis: authored` on the four status-bearing
records; the 3a domain change + migration; the 3d split. AT WP-3: derivation rules as code;
`derived` legality; rejected-write enforcement; the projection recompute contract.
**NOT PROPOSED: removing any status field.** Consumers keep their query surface; what changes is
that the contract stops pretending authored claims are derivations.

## 5. FOUR-POSTULATE IMPACT (records to be cut with the implementing boundary)

`verification_standing` (3-value form) — re-recorded; `status_basis` — new 2-value enum, record
drafted with it; `bundle_completeness` (split form) — re-recorded; every projection names its
DERIVATION RULE ID in the doctrine when WP-3 lands. Collision census impact: `superseded` leaves
one domain (the allowlist entry narrows); `partial_legacy` token retires.

## 6. ATTACK SURFACE, NAMED FOR THE ATTACKERS

The migration rules (3a's rewrite floor especially); whether `status_basis: authored` is itself
an unenforced honesty field (its consuming half: certifications must read it — is that enough
before WP-3?); whether 3b's projection erases any state the overlay values currently carry;
whether dropping `superseded` breaks any existing consumer (census owed before landing);
the un-derivability of `registry_standing`'s adjudication values from events that are messages
(AT-5's split is the standing answer; attack the split). DECLARED LIMIT (AT-1, beside limit 6):
the `superseded_by`-freezes-standing promise is UNENFORCED pre-WP-3 — a validator arm cannot see
cross-version writes; it becomes a rejected-write rule when the ledger lands.
