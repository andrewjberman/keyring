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

- **v0.x (NOW):** status fields stay AS WRITTEN by the author, but each carrying record gains
  `status_basis: authored` — an honest label that the projection is a CLAIM, not a derivation.
  (One field, enum `authored | derived`; `derived` ILLEGAL until the ledger exists — a derivation
  claim without a derivable substrate would be the F5 defect.)
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
standing where recoverable, else `unverified` + `superseded_by` (honest floor). The warrant arm
moves from the value to the field: `superseded_by present -> no further standing changes on THIS
record` (append-only; a new assertion carries the new standing).

**3b. CONTESTED/DISPUTED OVERLAYS.** Under the two layers: a CONTEST is an EVENT
(identity_relation `candidate_equivalence` with `contest: true`, or a binding-dispute record),
never a lifecycle value that displaces the interval truth. `entity.current_status.contested` and
`binding.status.disputed` become PROJECTIONS (contest event open => projection shows contested/
disputed) — the 3.5 carve-out (`disputed` MAY carry `valid_to: null`) stops being a smuggling
route because the interval fields never stopped carrying interval truth.

**3c. SUBJECT-GRAIN `unknown` (materializer).** Dissolves: `materializer.current_status` derives
from receipts + version supersessions; `unknown` = ZERO observations in the event layer — an
honest projection of an empty history, observer-grain by construction.

**3d. `partial_legacy` INTENT FUSION.** `bundle_completeness` splits: DEGREE (`complete |
partial`) stays the enum; CAUSE moves to `absent_components[]` + evidence (already required) —
the partial-NOT-legacy member gets its honest home with NO new value. The `partial_legacy` token
retires at the same boundary (migration: `partial_legacy -> partial` + cause preserved).

**3e. RETIREMENT REASON (the routed design question).** Confirmed at design: the reason lives on
the SUCCESSION EVENT (`identity_relation` `successor_of`/`replaces`, or a terminal relation with
`evidence_refs`), never as prose on the entity — `retired` is a projection of a retirement event,
and an event can honestly say "ceased, no successor."

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
the un-derivability of `registry_standing`'s adjudication values from events that are messages.
